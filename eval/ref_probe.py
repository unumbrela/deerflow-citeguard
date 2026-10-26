"""Do papers that many candidates cite pick more gold papers than arXiv's relevance order? (P2, offline)

Usage:
    python3 -I ref_probe.py --pools /tmp/pool.json [--pool 50]

For each topic, the references of the top ``--pool`` candidates come from Semantic Scholar (batch endpoint,
no key: retried on 429). A reference is eligible when it has an arXiv id, falls inside the task's window and
has the task's primary category (checked against arXiv). Eligible papers, together with the candidates
themselves, are ranked by how many candidates cite them (ties: candidates first, by arXiv rank).
Only backward references of in-window papers are used, so nothing published after the window can leak in;
the survey itself is after the window by construction. Development set only.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
S2_CACHE = HERE / ".s2_refs_cache.json"  # gitignored
ARXIV_CACHE = HERE / ".arxiv_meta_cache.json"  # gitignored
UA = {"User-Agent": "deerflow-citeguard-eval/0.1 (+https://github.com/unumbrela/deerflow-citeguard)"}
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}


def _load(path: Path) -> dict:
    return json.loads(path.read_text()) if path.exists() else {}


def references(ids: list[str]) -> dict[str, list[str]]:
    """arXiv id -> arXiv ids it references (Semantic Scholar)."""
    cache = _load(S2_CACHE)
    missing = [i for i in ids if i not in cache]
    for start in range(0, len(missing), 100):
        chunk = missing[start : start + 100]
        body = json.dumps({"ids": [f"arXiv:{i}" for i in chunk]}).encode()
        url = "https://api.semanticscholar.org/graph/v1/paper/batch?fields=references.externalIds"
        for attempt in range(12):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, data=body, headers={**UA, "Content-Type": "application/json"}), timeout=60) as resp:
                    out = json.loads(resp.read())
                break
            except Exception:  # noqa: BLE001 - unauthenticated requests share a rate limit; back off
                time.sleep(min(60, 3 * 2**attempt))
        else:
            raise SystemExit("Semantic Scholar unavailable")
        for i, r in zip(chunk, out):
            cache[i] = [ref["externalIds"]["ArXiv"] for ref in (r or {}).get("references") or [] if (ref.get("externalIds") or {}).get("ArXiv")] if r else None
        S2_CACHE.write_text(json.dumps(cache))
        time.sleep(3)
    return {i: cache.get(i) for i in ids}


def arxiv_meta(ids: set[str]) -> dict[str, dict]:
    """arXiv id -> {published, primary}."""
    cache = _load(ARXIV_CACHE)
    missing = sorted(i for i in ids if i not in cache)
    for start in range(0, len(missing), 100):
        chunk = missing[start : start + 100]
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"id_list": ",".join(chunk), "max_results": 100})
        for attempt in range(5):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as resp:
                    root = ET.fromstring(resp.read())
                break
            except Exception:  # noqa: BLE001
                time.sleep(5 * 2**attempt)
        else:
            raise SystemExit("arXiv unavailable")
        for e in root.findall("a:entry", NS):
            pid = e.findtext("a:id", "", NS).rsplit("/abs/", 1)[-1].rsplit("v", 1)[0]
            prim = e.find("x:primary_category", NS)
            cache[pid] = {"published": e.findtext("a:published", "", NS)[:10], "primary": prim.get("term", "") if prim is not None else ""}
        for i in chunk:
            cache.setdefault(i, None)
        ARXIV_CACHE.write_text(json.dumps(cache))
        time.sleep(3)
    return {i: cache.get(i) for i in ids}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pools", required=True)
    ap.add_argument("--pool", type=int, default=50)
    ap.add_argument("--out")
    args = ap.parse_args()
    topics = {t["id"]: t for t in json.loads((HERE / "coverage_topics.json").read_text())["topics"]}
    totals = Counter()
    rows = []
    for r in json.loads(Path(args.pools).read_text()):
        topic = topics[r["id"]]
        gold = set(topic["gold"])
        cands = r["pool_ids"][: args.pool]
        refs = references(cands)
        counts = Counter(x for c in cands for x in set(refs[c] or []))
        meta = arxiv_meta(set(counts))

        def eligible(pid: str) -> bool:
            m = meta.get(pid)
            return bool(m) and m["primary"] == topic["category"] and topic["start_date"] <= m["published"] <= topic["end_date"]

        expanded = [p for p in counts if eligible(p) and p not in cands]
        union = cands + expanded
        by_cites = sorted(union, key=lambda p: (-counts.get(p, 0), union.index(p)))
        picks = {"rank": cands[:10], "cited_by_pool": by_cites[:10]}
        hits = {k: sum(p in gold for p in v) for k, v in picks.items()}
        totals.update(hits)
        no_refs = sum(refs[c] is None for c in cands)
        row = {"id": r["id"], "cands": len(cands), "no_refs": no_refs, "expanded": len(expanded), "union_gold": sum(p in gold for p in union), **hits, "top": [(p, counts.get(p, 0), p in gold) for p in by_cites[:15]]}
        rows.append(row)
        print(f"{r['id']} cands={len(cands):3} s2_missing={no_refs:2} expanded={len(expanded):3} union_gold={row['union_gold']:3} " + " ".join(f"{k}={v}" for k, v in hits.items()), flush=True)
    print("total:", dict(totals))
    if args.out:
        Path(args.out).write_text(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
