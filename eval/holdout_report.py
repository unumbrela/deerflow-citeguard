"""Compare eval arms on the pre-registered metrics of eval/HOLDOUT.md (round two).

Usage:
    python3 -I holdout_report.py holdout3-v3 holdout3-base

Reads ../runs/suite-<name>/summary.json written by aggregate.py. A run is "clean" when it delivered a report
with exactly 10 references, every one verified, in the date window and in the requested category.
Repeats of one topic are not independent, so topics clean on every repeat are reported next to the run-level rate.
"""

from __future__ import annotations

import json
import math
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (max(0.0, centre - half), min(1.0, centre + half))


def clean(row: dict) -> bool:
    return row.get("status") == "ok" and row["refs"] == 10 and row["verified"] == row["in_window"] == row["in_category"] == 10


def arm(name: str) -> dict:
    data = json.loads((ROOT / "runs" / f"suite-{name}" / "summary.json").read_text())
    rows = data["rows"]
    by_topic = defaultdict(list)
    for r in rows:
        by_topic[r["run"].split("-")[0]].append(clean(r))
    k, n = sum(clean(r) for r in rows), len(rows)
    lo, hi = wilson(k, n)
    ok = [r for r in rows if r.get("status") == "ok"]
    refs = sum(r["refs"] for r in ok) or 1
    return {
        "arm": name,
        "clean_runs": f"{k}/{n}",
        "clean_rate": round(k / n, 3) if n else None,
        "wilson95": [round(lo, 3), round(hi, 3)],
        "topics_clean_every_repeat": f"{sum(all(v) for v in by_topic.values())}/{len(by_topic)}",
        "delivered": f"{len(ok)}/{n}",
        "verified_rate": round(sum(r["verified"] for r in ok) / refs, 3),
        "in_window_rate": round(sum(r["in_window"] for r in ok) / refs, 3),
        "in_category_rate": round(sum(r["in_category"] for r in ok) / refs, 3),
        "runs_with_10_refs": sum(r["refs"] == 10 for r in ok),
        "mean_seconds": round(statistics.mean(r["seconds"] for r in rows if "seconds" in r), 1),
        "mean_tokens": round(statistics.mean(r["tokens"] for r in rows if "tokens" in r)),
        **{k2: v for k2, v in data["summary"].items() if k2.startswith("gate_")},
    }


def main() -> None:
    print(json.dumps([arm(name) for name in sys.argv[1:]], ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
