"""Paired comparison of two configurations on the coverage benchmark (written before the P2 holdout run).

Usage:
    python3 -I coverage.py --name <A>; python3 -I coverage.py --name <B>
    python3 -I coverage_compare.py --base <A> --new <B>

Each run's hit rate comes from coverage.json (undelivered runs count as 0). Repetitions of a topic are not
independent, so they are averaged per topic first; the comparison is paired over topics:
    mean difference (new - base), bootstrap 95% CI over topics (10,000 resamples, fixed seed),
    exact two-sided Wilcoxon signed-rank p (zero differences dropped), topics better / same / worse.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESAMPLES = 10_000
SEED = 20261027


def per_topic(name: str) -> dict[str, float]:
    rows = json.loads((ROOT / "runs" / f"suite-{name}" / "coverage.json").read_text())["rows"]
    by_topic: dict[str, list[float]] = {}
    for r in rows:
        by_topic.setdefault(r["run"].split("-")[0], []).append(r["precision"])
    return {t: statistics.mean(v) for t, v in by_topic.items()}


def bootstrap_ci(diffs: list[float], resamples: int = RESAMPLES, seed: int = SEED) -> tuple[float, float]:
    rng = random.Random(seed)
    means = sorted(statistics.mean(rng.choices(diffs, k=len(diffs))) for _ in range(resamples))
    return means[int(0.025 * resamples)], means[int(0.975 * resamples) - 1]


def wilcoxon_exact(diffs: list[float]) -> float:
    """Two-sided exact p of the signed-rank statistic; ties get average ranks, zeros are dropped."""
    d = [x for x in diffs if abs(x) > 1e-12]
    if not d:
        return 1.0
    order = sorted(range(len(d)), key=lambda i: abs(d[i]))
    ranks = [0.0] * len(d)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and abs(abs(d[order[j + 1]]) - abs(d[order[i]])) < 1e-12:
            j += 1
        for k in range(i, j + 1):
            ranks[order[k]] = (i + j) / 2 + 1
        i = j + 1
    observed = sum(r for r, x in zip(ranks, d) if x > 0)
    centre = sum(ranks) / 2
    extreme = sum(abs(sum(r for r, s in zip(ranks, signs) if s) - centre) >= abs(observed - centre) - 1e-12 for signs in itertools.product((0, 1), repeat=len(d)))
    return extreme / 2 ** len(d)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", required=True)
    ap.add_argument("--new", required=True)
    args = ap.parse_args()
    base, new = per_topic(args.base), per_topic(args.new)
    if set(base) != set(new):
        raise SystemExit(f"topic sets differ: {sorted(set(base) ^ set(new))}")
    topics = sorted(base)
    diffs = [new[t] - base[t] for t in topics]
    lo, hi = bootstrap_ci(diffs)
    result = {
        "topics": len(topics),
        "base_mean": round(statistics.mean(base.values()), 3),
        "new_mean": round(statistics.mean(new.values()), 3),
        "mean_diff": round(statistics.mean(diffs), 3),
        "ci95": [round(lo, 3), round(hi, 3)],
        "wilcoxon_p": round(wilcoxon_exact(diffs), 4),
        "better_same_worse": [sum(d > 1e-12 for d in diffs), sum(abs(d) <= 1e-12 for d in diffs), sum(d < -1e-12 for d in diffs)],
        "per_topic": {t: {"base": round(base[t], 3), "new": round(new[t], 3)} for t in topics},
    }
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
