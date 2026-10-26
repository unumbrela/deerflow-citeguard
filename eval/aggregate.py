"""Check every report in a suite against arXiv and aggregate the results.

Usage:
    python3 -I aggregate.py --name pre-01 [--since 2024-10-25]

Runs check_citations.py on each <run>/report.md (serially, 3.5 s apart, to respect arXiv's rate limit),
caches the result in <run>/citations.json, and writes ../runs/suite-<name>/summary.json + prints a table.
"""

import argparse
import json
import re
import statistics
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
WINDOW_RE = re.compile(r"published between (\d{4}-\d{2}-\d{2}) and (\d{4}-\d{2}-\d{2})")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--name", required=True)
    ap.add_argument("--since", default="2024-10-25")
    ap.add_argument("--topics", default="topics.json")
    args = ap.parse_args()

    topics = {t["id"]: t for t in json.loads((HERE / args.topics).read_text())}
    root = ROOT / "runs" / f"suite-{args.name}"
    rows = []
    for run in sorted(p for p in root.iterdir() if p.is_dir()):
        meta_f = run / "meta.json"
        if not meta_f.exists():
            rows.append({"run": run.name, "status": "no_meta"})
            continue
        meta = json.loads(meta_f.read_text())
        row = {
            "run": run.name,
            "seconds": meta["wall_seconds"],
            "tokens": meta["usage_attributed_total"]["total_tokens"],
            "error": meta["error"],
        }
        ev = run / "events.jsonl"  # holds every state snapshot, so it still has tool output that summarization later dropped
        ev_text = ev.read_text(errors="replace") if ev.exists() else ""
        row["search_429"] = "HTTP Error 429" in ev_text or "Too Many Requests" in ev_text
        gate = run / "gate.jsonl"  # citation-gate decisions, only present when the scholar plugin ran
        if gate.exists():
            events = [json.loads(line)["event"] for line in gate.read_text().splitlines() if line.strip()]
            decisions = [e for e in events if e in ("accepted", "rejected", "released_unverified")]
            row["gate_rejections"] = decisions.count("rejected")
            row["gate_final"] = decisions[-1] if decisions else None
            row["gate_search_rejections"] = events.count("search_rejected")
            row["gate_auto_presented"] = "auto_presented" in events
        search = run / "search.json"  # v4 plugin: candidate pool, citation expansion and screening table
        if search.exists():
            record = json.loads(search.read_text())
            row["expansion"] = (record.get("expansion") or {}).get("status")
            row["screening"] = (record.get("screening") or {}).get("status", "not_run")
            row["included_from_references"] = ((record.get("screening") or {}).get("counts") or {}).get("included_from_references")
        report = run / "report.md"
        if not report.exists():
            row["status"] = "no_report"
            rows.append(row)
            continue
        cit_f = run / "citations.json"
        if not cit_f.exists():
            topic = topics[run.name.split("-")[0]]
            # Coverage topics fix their own window in the prompt; the others use "last 2 years" from --since.
            fixed = WINDOW_RE.search(topic.get("prompt", ""))
            window = ["--since", fixed[1], "--until", fixed[2]] if fixed else ["--since", args.since]
            subprocess.run(
                [sys.executable, "-I", str(HERE / "check_citations.py"), str(report), *window, "--category", topic["category"], "--json", str(cit_f)],
                stdout=subprocess.DEVNULL,
            )
            time.sleep(3.5)
        if not cit_f.exists():
            row["status"] = "check_failed"
            rows.append(row)
            continue
        m = json.loads(cit_f.read_text())["metrics"]
        row.update(status="ok", refs=m["references"], unparsed=m["unparsed"], **{k: m[k]["ok"] for k in ("verified", "resolved", "in_window", "in_category", "first_author")}, verified_of=m["verified"]["of"])
        rows.append(row)

    ok = [r for r in rows if r.get("status") == "ok"]
    summary = {
        "runs": len(rows),
        "delivered_report": len(ok),
        "no_report": sum(r.get("status") == "no_report" for r in rows),
        "runs_hit_arxiv_429": sum(bool(r.get("search_429")) for r in rows),
        "mean_seconds": round(statistics.mean(r["seconds"] for r in rows if "seconds" in r), 1) if rows else None,
        "mean_tokens": round(statistics.mean(r["tokens"] for r in rows if "tokens" in r)) if rows else None,
    }
    gated = [r for r in rows if "gate_rejections" in r]
    if gated:
        summary.update(
            gate_runs=len(gated),
            gate_runs_with_rejection=sum(r["gate_rejections"] > 0 for r in gated),
            # Last decision not "accepted": the model either gave up after a rejection or was released unverified.
            gate_final_not_accepted=sum(r["gate_final"] != "accepted" for r in gated),
            # The search dropped the user's category; the report was saved but not presented, so the gate presented it.
            gate_runs_with_search_rejection=sum(r["gate_search_rejections"] > 0 for r in gated),
            gate_runs_auto_presented=sum(r["gate_auto_presented"] for r in gated),
        )
    searched = [r for r in rows if "expansion" in r]
    if searched:
        # A degraded run (Semantic Scholar throttled, model call failed) measures the fallback, not the method.
        summary.update(
            runs_expansion_ok=sum(r["expansion"] == "ok" for r in searched),
            runs_screening_ok=sum(r["screening"] == "ok" for r in searched),
            included_from_references=sum(r["included_from_references"] or 0 for r in searched),
        )
    if ok:
        refs = sum(r["refs"] for r in ok)
        summary.update(
            refs_total=refs,
            verified_rate=round(sum(r["verified"] for r in ok) / refs, 3),
            in_window_rate=round(sum(r["in_window"] for r in ok) / refs, 3),
            in_category_rate=round(sum(r["in_category"] for r in ok) / refs, 3),
            runs_all_verified=sum(r["verified"] == r["refs"] for r in ok),
            runs_mostly_fabricated=sum(r["verified"] <= r["refs"] / 2 for r in ok),
        )
    (root / "summary.json").write_text(json.dumps({"summary": summary, "rows": rows}, ensure_ascii=False, indent=1))
    print(f"{'run':10}{'status':12}{'refs':>5}{'verif':>6}{'window':>7}{'cat':>5}{'sec':>7}{'tokens':>9}")
    for r in rows:
        print(f"{r['run']:10}{r.get('status', ''):12}{r.get('refs', ''):>5}{r.get('verified', ''):>6}{r.get('in_window', ''):>7}{r.get('in_category', ''):>5}{r.get('seconds', ''):>7}{r.get('tokens', ''):>9}")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
