"""How many gold papers can a bigger candidate pool reach? An offline ceiling for P2 retrieval changes.

Usage:
    python3 -I pool_probe.py [--set coverage_dev.json] [--depth 200] [--queries queries.json]

For each coverage topic, run the search the plugin would run (phrase, then all terms; same window and primary
category) but keep paging past the first page, and report how many gold papers sit in the top K for several K.
No model is called. ``--queries`` maps topic id -> list of query strings (default: the query the v3.1 agent
used on the dev set); with several queries the pools are merged in round-robin order of rank.
Only for the development set: running it on held-out topics would leak their answer keys into design choices.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
UA = {"User-Agent": "deerflow-citeguard-eval/0.1 (+https://github.com/unumbrela/deerflow-citeguard)"}
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
PAGE = 100
DEPTHS = (10, 25, 50, 100, 200)
# What the v3.1 agent (qwen3.5-plus) passed as `query` on the dev set (search.json of each r1 run; r2 used the same).
V31_QUERIES = {
    "c02": ["latent reasoning"],
    "c04": ["LLM mid-training"],
    "c05": ["Deep Research"],
    "c08": ["GRPO generation models"],
    "c09": ["domain generalization semantic segmentation"],
    "c13": ["generative recommendation"],
    "c17": ["embodied intelligence flexible manufacturing"],
    "c18": ["world models robotic manipulation"],
}


def build(query: str, category: str, start: str, end: str, match: str) -> str:
    words = query.split()
    if match == "all_terms" and len(words) > 1:
        q = "(" + " AND ".join(f"all:{w}" for w in words) + ")"
    elif len(words) > 1:
        q = f'all:"{" ".join(words)}"'
    else:
        q = f"all:{query}"
    return f"{q} AND cat:{category} AND submittedDate:[{start.replace('-', '')}0000 TO {end.replace('-', '')}2359]"


def fetch(search_query: str, start: int) -> list[tuple[str, str]]:
    params = urllib.parse.urlencode({"search_query": search_query, "start": start, "max_results": PAGE, "sortBy": "relevance", "sortOrder": "descending"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://export.arxiv.org/api/query?{params}", headers=UA), timeout=60) as resp:
                root = ET.fromstring(resp.read())
            break
        except Exception:  # noqa: BLE001 - rate limits and timeouts: back off and retry
            time.sleep(5 * 2**attempt)
    else:
        raise SystemExit(f"arXiv failed for {search_query!r}")
    out = []
    for e in root.findall("a:entry", NS):
        pid = e.findtext("a:id", "", NS).rsplit("/", 1)[-1].rsplit("v", 1)[0]
        prim = e.find("x:primary_category", NS)
        out.append((pid, prim.get("term", "") if prim is not None else ""))
    return out


def pool(query: str, topic: dict, depth: int) -> list[str]:
    """Primary-category papers in plugin order: phrase matches first, then all-terms matches, deduplicated."""
    ids: list[str] = []
    for match in ("phrase", "all_terms") if len(query.split()) > 1 else ("phrase",):
        sq = build(query, topic["category"], topic["start_date"], topic["end_date"], match)
        start = 0
        while len(ids) < depth:
            page = fetch(sq, start)
            time.sleep(3)
            ids += [pid for pid, prim in page if prim == topic["category"] and pid not in ids]
            if len(page) < PAGE:
                break
            start += PAGE
        if len(ids) >= depth:
            break
    return ids[:depth]


def merge(pools: list[list[str]]) -> list[str]:
    out: list[str] = []
    for rank in range(max(map(len, pools), default=0)):
        for p in pools:
            if rank < len(p) and p[rank] not in out:
                out.append(p[rank])
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", default="coverage_dev.json")
    ap.add_argument("--depth", type=int, default=200)
    ap.add_argument("--queries", help="JSON file: topic id -> list of queries")
    ap.add_argument("--out", help="write per-topic pools and hits here")
    args = ap.parse_args()
    if "holdout" in args.set:
        raise SystemExit("pool_probe is for the development set only")
    queries = json.loads(Path(args.queries).read_text()) if args.queries else V31_QUERIES
    topics = {t["id"]: t for t in json.loads((HERE / "coverage_topics.json").read_text())["topics"]}
    rows = []
    for task in json.loads((HERE / args.set).read_text()):
        topic = topics[task["id"]]
        gold = set(topic["gold"])
        merged = merge([pool(q, topic, args.depth) for q in queries[task["id"]]])
        hits = {k: sum(p in gold for p in merged[:k]) for k in DEPTHS if k <= args.depth}
        rows.append({"id": task["id"], "gold": len(gold), "pool": len(merged), "hits_at": hits, "hit_ids": [p for p in merged if p in gold], "pool_ids": merged})
        print(f"{task['id']} gold={len(gold):4} pool={len(merged):4} " + " ".join(f"@{k}:{v}" for k, v in hits.items()), flush=True)
    for k in DEPTHS:
        if k <= args.depth:
            print(f"total hits @{k}: {sum(r['hits_at'].get(k, 0) for r in rows)}")
    if args.out:
        Path(args.out).write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
