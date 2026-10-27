"""Token use per run from the event stream, for runs recorded before meta.json had ``usage_events_total``.

    python3 -I tokens.py --suites coverage-holdout-v4 smoke-v5-plus-03

``meta.json``'s ``usage_attributed_total`` sums the final state's messages only, and summarization drops
earlier messages from that state. This re-reads ``events.jsonl`` (kept locally, not in git), deduplicates AI
messages by id and sums their usage; subagent usage is backfilled onto the lead message that dispatched
them. Also split out: subagent tokens (``subagent_token_usage`` on task results) and lead turns.
"""

from __future__ import annotations

import argparse
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run_tokens(run: Path) -> dict | None:
    events = run / "events.jsonl"
    if not events.exists():
        return None
    msgs: dict[str, dict] = {}
    for line in events.open(encoding="utf-8"):
        data = json.loads(line).get("data")
        if isinstance(data, dict):
            for m in data.get("messages") or []:
                if m.get("id"):
                    msgs[m["id"]] = m
    ai = [m for m in msgs.values() if m.get("type") == "ai"]
    total = sum(int((m.get("usage_metadata") or {}).get("total_tokens") or 0) for m in ai)
    sub = sum(int(((m.get("additional_kwargs") or {}).get("subagent_token_usage") or {}).get("total_tokens") or 0) for m in msgs.values() if m.get("type") == "tool" and m.get("name") == "task")
    meta = json.loads((run / "meta.json").read_text()) if (run / "meta.json").exists() else {}
    # The first baseline runs recorded usage_lead_agent_only, before subagent usage was counted.
    final = (meta.get("usage_attributed_total") or meta.get("usage_lead_agent_only") or {}).get("total_tokens")
    return {"run": run.name, "total": total, "subagents": sub, "lead": total - sub, "lead_turns": len(ai), "final_state_total": final}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--suites", nargs="+", required=True)
    args = ap.parse_args()
    out = {}
    for suite in args.suites:
        rows = [r for r in (run_tokens(p) for p in sorted((ROOT / "runs" / f"suite-{suite}").iterdir()) if p.is_dir()) if r]
        if not rows:
            continue
        mean = lambda k: round(statistics.mean(r[k] for r in rows if r[k] is not None))  # noqa: E731
        out[suite] = {"runs": len(rows), **{f"mean_{k}": mean(k) for k in ("total", "subagents", "lead", "lead_turns", "final_state_total")}, "max_total": max(r["total"] for r in rows)}
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
