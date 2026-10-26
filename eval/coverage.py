"""Score coverage runs against the survey answer key built by build_coverage_set.py.

Usage:
    python3 -I coverage.py --name coverage-v31

For each run, the arXiv ids cited in report.md are compared with the survey's gold set (its in-scope arXiv
references). Reported per run and averaged over topics:
    precision   cited papers that the survey also cites / cited papers. Headline: the gold sets (13-183 papers)
                are much larger than a 10-paper review, so this is the fair "did it pick what an expert picked" rate.
    recall      cited papers in the gold set / min(10, gold size). Bounded by the 10-paper request.
    in_scope    cited papers inside the task's date window and category (from the citation check, when present).
The answer key only contains references that carry an arXiv id, and one survey's choices are not the only good
ones, so these numbers compare configurations; they are not absolute quality scores.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})|arXiv:\s*(\d{4}\.\d{4,5})", re.I)


def cited_ids(text: str) -> list[str]:
    return list(dict.fromkeys(a or b for a, b in ID_RE.findall(text)))


def score(cited: list[str], gold: set[str]) -> dict:
    hits = [i for i in cited if i in gold]
    return {
        "cited": len(cited),
        "hits": len(hits),
        "precision": round(len(hits) / len(cited), 3) if cited else 0.0,
        "recall": round(len(hits) / min(10, len(gold)), 3) if gold else None,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--name", required=True)
    args = ap.parse_args()
    topics = {t["id"]: t for t in json.loads((HERE / "coverage_topics.json").read_text())["topics"]}
    root = ROOT / "runs" / f"suite-{args.name}"
    rows = []
    for run in sorted(p for p in root.iterdir() if p.is_dir()):
        topic = topics[run.name.split("-")[0]]
        report = run / "report.md"
        if not report.exists():
            rows.append({"run": run.name, "status": "no_report", "precision": 0.0, "recall": 0.0})
            continue
        # The survey itself is in the search window; citing it is reasonable but it is not in its own reference list.
        cited = [i for i in cited_ids(report.read_text(errors="replace")) if i != topic["survey"]]
        row = {"run": run.name, "status": "ok", "gold": len(topic["gold"]), "cites_survey": len(cited) < len(cited_ids(report.read_text(errors="replace"))), **score(cited, set(topic["gold"]))}
        rows.append(row)
    ok = [r for r in rows if r["status"] == "ok"]
    summary = {
        "runs": len(rows),
        "delivered": len(ok),
        # Undelivered runs count as zero, so a configuration cannot look better by failing hard topics.
        "mean_precision": round(statistics.mean(r["precision"] for r in rows), 3) if rows else None,
        "mean_recall": round(statistics.mean(r["recall"] for r in rows), 3) if rows else None,
        "runs_with_no_hit": sum(r.get("hits", 0) == 0 for r in rows),
        "runs_citing_the_survey": sum(bool(r.get("cites_survey")) for r in rows),
    }
    (root / "coverage.json").write_text(json.dumps({"summary": summary, "rows": rows}, indent=1))
    print(f"{'run':10}{'gold':>6}{'cited':>7}{'hits':>6}{'prec':>7}{'recall':>8}")
    for r in rows:
        print(f"{r['run']:10}{r.get('gold', ''):>6}{r.get('cited', ''):>7}{r.get('hits', ''):>6}{r['precision']:>7}{r['recall']:>8}")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
