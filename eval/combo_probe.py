"""Combine citation expansion with model screening. (P2, offline; run ref_probe.py first to fill its caches)

Usage:
    python3 -I combo_probe.py --pools /tmp/pool.json [--pool 50] [--shortlist 30] [--model qwen3.5-plus]

Candidates = top ``--pool`` arXiv results + their in-window, in-category arXiv references. Each is ranked by
how many candidates cite it. Strategies compared (top 10 each):
    rank          arXiv relevance order (what v3.1 does)
    cocite        co-citation count, ties by arXiv rank
    cocite+screen the top ``--shortlist`` by co-citation are screened by the model (screen_probe prompt);
                  papers scored below 2 are dropped, the rest keep co-citation order
    half          5 from rank + 5 from cocite+screen (deduplicated, then filled from cocite+screen)
Development set only.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from claims import _api_key, load_abstracts  # noqa: E402
from ref_probe import arxiv_meta, references  # noqa: E402
from screen_probe import ABSTRACT_CHARS, PROMPT, call  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pools", required=True)
    ap.add_argument("--pool", type=int, default=50)
    ap.add_argument("--shortlist", type=int, default=30)
    ap.add_argument("--batch", type=int, default=10)
    ap.add_argument("--model", default="qwen3.5-plus")
    ap.add_argument("--out")
    args = ap.parse_args()
    key = _api_key()
    topics = {t["id"]: t for t in json.loads((HERE / "coverage_topics.json").read_text())["topics"]}
    totals: Counter = Counter()
    tokens = 0
    rows = []
    for r in json.loads(Path(args.pools).read_text()):
        topic = topics[r["id"]]
        gold = set(topic["gold"])
        cands = r["pool_ids"][: args.pool]
        refs = references(cands)
        counts = Counter(x for c in cands for x in set(refs[c] or []))
        meta = arxiv_meta(set(counts))
        expanded = [p for p in counts if p not in cands and (m := meta.get(p)) and m["primary"] == topic["category"] and topic["start_date"] <= m["published"] <= topic["end_date"]]
        union = cands + expanded
        by_cites = sorted(union, key=lambda p: (-counts.get(p, 0), union.index(p)))
        shortlist = by_cites[: args.shortlist]
        abstracts = load_abstracts(set(shortlist))
        scores: dict[str, int] = {}
        for i in range(0, len(shortlist), args.batch):
            chunk = shortlist[i : i + args.batch]
            papers = "\n\n".join(f"id: {p}\ntitle: {abstracts[p]['title']}\nabstract: {abstracts[p]['abstract'][:ABSTRACT_CHARS]}" for p in chunk)
            out, usage = call(PROMPT.format(topic=topic["topic"], category=topic["category"], papers=papers), args.model, key)
            tokens += usage.get("total_tokens", 0)
            scores.update({s["id"]: int(s.get("score", 0)) for s in out.get("scores", []) if s.get("id") in chunk})
        screened = [p for p in shortlist if scores.get(p, 0) >= 2]
        half = list(dict.fromkeys(cands[:5] + screened))[:10]
        picks = {"rank": cands[:10], "cocite": by_cites[:10], "cocite+screen": screened[:10], "half": half}
        hits = {k: sum(p in gold for p in v) for k, v in picks.items()}
        totals.update(hits)
        rows.append({"id": r["id"], **hits, "screened": [(p, counts.get(p, 0), scores.get(p), p in gold) for p in shortlist]})
        print(f"{r['id']} " + " ".join(f"{k}={v}" for k, v in hits.items()) + f"  kept {len(screened)}/{len(shortlist)}", flush=True)
    print("total:", dict(totals), "tokens:", tokens)
    if args.out:
        Path(args.out).write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
