"""Run one task against the local DeerFlow gateway and record the result.

Usage:
    python3 -I run_task.py --prompt "..." --model qwen3.5-plus --out ../runs/baseline-01

Reads the session from ../.local/cookies.txt (Netscape format, gitignored).
Writes into --out:
    meta.json     prompt, model, wall time, event counts, token usage
    final.json    last `values` snapshot of the thread state
    events.jsonl  every SSE event, one JSON object per line
"""

import argparse
import json
import time
import urllib.error
import urllib.request
import uuid
from pathlib import Path

BASE = "http://localhost:2026"
COOKIES = Path(__file__).resolve().parent.parent / ".local" / "cookies.txt"


def load_cookies() -> dict[str, str]:
    jar = {}
    for line in COOKIES.read_text().splitlines():
        parts = line.split("\t")
        if len(parts) >= 7:
            jar[parts[5]] = parts[6]
    return jar


def request(method: str, path: str, body: dict | None, cookies: dict[str, str], timeout: int = 60):
    headers = {
        "Content-Type": "application/json",
        "Origin": BASE,
        "Cookie": "; ".join(f"{k}={v}" for k, v in cookies.items()),
        "X-CSRF-Token": cookies.get("csrf_token", ""),
    }
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, headers=headers, method=method)
    return urllib.request.urlopen(req, timeout=timeout)


def sum_usage(messages: list[dict]) -> dict[str, int]:
    total = {"input_tokens": 0, "output_tokens": 0, "total_tokens": 0}
    for m in messages:
        u = m.get("usage_metadata") or {}
        for k in total:
            total[k] += int(u.get(k) or 0)
    return total


def usage_over_stream(seen: dict[str, dict]) -> dict[str, int]:
    """Usage of every AI message the stream ever showed, deduplicated by id.

    The final state alone undercounts: once the context is summarized, earlier messages leave it. In v5 smoke
    runs the final state held 0.18-0.69M tokens where the stream showed 0.75-2.94M. Subagent usage is
    backfilled onto the lead message that dispatched them, so it is included once. The summarizer's own
    model calls do not appear as messages and are still missing.
    """
    return sum_usage(list(seen.values()))


RECORD_FIELDS = ("total_tokens", "total_input_tokens", "total_output_tokens", "lead_agent_tokens", "subagent_tokens", "middleware_tokens", "llm_call_count")


def usage_from_run_record(thread_id: str, cookies: dict[str, str]) -> dict[str, int] | None:
    """Token totals DeerFlow's run journal recorded for the thread's runs, or None if they cannot be read.

    This is the most complete count: the journal is a callback on every model call, so it also sees calls that
    never appear as messages (the summarizer, title generation and the plugin's screening model). On published
    suites it was 0-5% above the event-stream count.
    """
    try:
        with request("GET", f"/api/threads/{thread_id}/runs", None, cookies) as r:
            data = json.load(r)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None
    runs = data if isinstance(data, list) else data.get("runs", [])
    return {k: sum(int(run.get(k) or 0) for run in runs) for k in RECORD_FIELDS} if runs else None


def subagents_config_digest() -> str | None:
    """sha256 of the tracked subagent definition merged into config.yaml (scripts/apply_subagents.py), or None."""
    config = Path(__file__).resolve().parent.parent / "deer-flow" / "config.yaml"
    for line in config.read_text(encoding="utf-8").splitlines() if config.exists() else []:
        if line.startswith("# BEGIN citeguard subagents sha256="):
            return line.split("sha256=", 1)[1].split()[0]
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True)
    ap.add_argument("--model", default="qwen3.5-plus")
    ap.add_argument("--out", required=True)
    ap.add_argument("--recursion-limit", type=int, default=1000, help="1000 matches the web UI default")
    ap.add_argument("--timeout", type=int, default=1800, help="max seconds to wait on the stream")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    cookies = load_cookies()

    with request("POST", "/api/langgraph/threads", {"metadata": {"purpose": "baseline"}}, cookies) as r:
        thread_id = json.load(r)["thread_id"]
    print("thread", thread_id, flush=True)

    body = {
        "input": {"messages": [{"role": "user", "content": args.prompt, "id": str(uuid.uuid4())}]},
        "config": {
            "recursion_limit": args.recursion_limit,
            "configurable": {
                "model_name": args.model,
                "thinking_enabled": False,
                "is_plan_mode": False,
                "subagent_enabled": True,
            },
        },
        "stream_mode": ["values"],
    }

    t0 = time.time()
    counts: dict[str, int] = {}
    last_values: dict | None = None
    seen_ai: dict[str, dict] = {}
    error = None
    try:
        with request("POST", f"/api/langgraph/threads/{thread_id}/runs/stream", body, cookies, timeout=args.timeout) as r, (out / "events.jsonl").open("w") as ev_f:
            event = None
            for raw in r:
                line = raw.decode("utf-8", "replace").rstrip("\n")
                if line.startswith("event:"):
                    event = line[6:].strip()
                elif line.startswith("data:"):
                    payload = line[5:].strip()
                    counts[event or "?"] = counts.get(event or "?", 0) + 1
                    try:
                        data = json.loads(payload)
                    except json.JSONDecodeError:
                        data = payload
                    ev_f.write(json.dumps({"t": round(time.time() - t0, 2), "event": event, "data": data}, ensure_ascii=False) + "\n")
                    if event == "values" and isinstance(data, dict):
                        last_values = data
                        for m in data.get("messages", []):
                            if m.get("type") == "ai" and m.get("id"):
                                seen_ai[m["id"]] = m  # the latest copy: the gate may rewrite a message under the same id
                        n = len(data.get("messages", []))
                        print(f"[{time.time() - t0:6.1f}s] values: {n} messages", flush=True)
    except (urllib.error.URLError, TimeoutError) as e:
        error = repr(e)
    wall = time.time() - t0

    if last_values is not None:
        (out / "final.json").write_text(json.dumps(last_values, ensure_ascii=False, indent=1))
    messages = (last_values or {}).get("messages", [])
    meta = {
        "thread_id": thread_id,
        "model": args.model,
        "prompt": args.prompt,
        "wall_seconds": round(wall, 1),
        "event_counts": counts,
        "message_count": len(messages),
        "usage_attributed_total": sum_usage(messages),  # final state only: undercounts once the context is summarized
        "usage_events_total": usage_over_stream(seen_ai),  # every AI message in the stream, subagents included
        "usage_run_record": usage_from_run_record(thread_id, cookies),  # DeerFlow's run journal: also summarizer and screening calls
        "artifacts": (last_values or {}).get("artifacts"),
        "subagents_config_sha256": subagents_config_digest(),
        "error": error,
    }
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))
    print(json.dumps(meta, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
