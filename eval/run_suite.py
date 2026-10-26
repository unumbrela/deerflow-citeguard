"""Run the literature-review eval suite against the local DeerFlow gateway.

Usage:
    python3 -I run_suite.py --name pre-01 --reps 1 --workers 3 [--limit N] [--model qwen3.5-plus]

For each (topic, rep) it runs eval/run_task.py, then downloads the delivered report.
Resumable: a run directory that already has meta.json is skipped.
Outputs go to ../runs/suite-<name>/<topic id>-r<rep>/ (meta.json, final.json, events.jsonl, report.md).
Citation checking is a separate step (aggregate.py), so this script never calls arXiv itself.
"""

import argparse
import json
import shutil
import subprocess
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BASE = "http://localhost:2026"
# Where the scholar plugin keeps per-thread citation-gate decisions (storage_path in config.yaml, seen from the host).
GATE_LOGS = ROOT / "deer-flow" / "backend" / ".deer-flow" / "scholar" / "threads"
PROMPT = "Do a systematic literature review on {topic}. 10 papers, last 2 years, category {category}, APA format. Save to default output location."


def cookies() -> dict[str, str]:
    jar = {}
    for line in (ROOT / ".local" / "cookies.txt").read_text().splitlines():
        parts = line.split("\t")
        if len(parts) >= 7:
            jar[parts[5]] = parts[6]
    return jar


def download_report(meta: dict, dest: Path) -> bool:
    arts = [a for a in (meta.get("artifacts") or []) if a.endswith(".md")]
    if not arts:
        return False
    ck = cookies()
    # The latest delivery: after a citation-gate rejection the model may present a corrected file under a new name.
    req = urllib.request.Request(
        f"{BASE}/api/threads/{meta['thread_id']}/artifacts{arts[-1]}",
        headers={"Cookie": "; ".join(f"{k}={v}" for k, v in ck.items()), "Origin": BASE},
    )
    dest.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    return True


def run_one(job: dict, out_root: Path, model: str) -> str:
    out = out_root / f"{job['id']}-r{job['rep']}"
    if (out / "meta.json").exists():
        return f"{out.name}: skipped (done)"
    out.mkdir(parents=True, exist_ok=True)
    prompt = PROMPT.format(topic=job["topic"], category=job["category"])
    t0 = time.time()
    with (out / "run.log").open("w") as log:
        subprocess.run(
            [sys.executable, "-I", str(HERE / "run_task.py"), "--prompt", prompt, "--model", model, "--out", str(out), "--timeout", "1500"],
            stdout=log,
            stderr=subprocess.STDOUT,
        )
    if not (out / "meta.json").exists():
        return f"{out.name}: FAILED before meta ({time.time() - t0:.0f}s)"
    meta = json.loads((out / "meta.json").read_text())
    gate_log = GATE_LOGS / meta["thread_id"] / "gate.jsonl"
    if gate_log.exists():
        shutil.copy(gate_log, out / "gate.jsonl")
    got = False
    try:
        got = download_report(meta, out / "report.md")
    except Exception as e:  # noqa: BLE001 - record and move on
        (out / "download_error.txt").write_text(repr(e))
    infra = ""
    try:
        last_ai = [m for m in json.loads((out / "final.json").read_text())["messages"] if m.get("type") == "ai"][-1]
        if "out of quota" in str(last_ai.get("content")):
            infra = " INFRA-FAILURE(provider quota): not an agent result, archive and rerun"
    except Exception:  # noqa: BLE001
        pass
    return f"{out.name}: {meta['wall_seconds']}s, {meta['usage_attributed_total']['total_tokens']} tok, report={got}, error={meta['error']}{infra}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--workers", type=int, default=2, help="keep low: agents and the checker share one IP and arXiv rate-limits it")
    ap.add_argument("--limit", type=int, help="only the first N topics")
    ap.add_argument("--model", default="qwen3.5-plus")
    ap.add_argument("--topics", default="topics.json", help="topics file inside eval/ (use holdout_topics.json for the held-out set)")
    args = ap.parse_args()

    probe = urllib.request.Request("https://export.arxiv.org/api/query?id_list=1706.03762&max_results=1", headers={"User-Agent": "deerflow-eval-preflight/0.1"})
    try:
        urllib.request.urlopen(probe, timeout=20).read()
    except Exception as e:  # noqa: BLE001
        raise SystemExit(f"arXiv preflight failed ({e!r}); not starting, a throttled run would measure the rate limit, not the agent")

    topics = json.loads((HERE / args.topics).read_text())[: args.limit]
    out_root = ROOT / "runs" / f"suite-{args.name}"
    out_root.mkdir(parents=True, exist_ok=True)
    jobs = [{**t, "rep": r} for r in range(1, args.reps + 1) for t in topics]
    print(f"{len(jobs)} jobs -> {out_root}", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for line in ex.map(lambda j: run_one(j, out_root, args.model), jobs):
            print(line, flush=True)


if __name__ == "__main__":
    main()
