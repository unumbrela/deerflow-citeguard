"""Does citation count pick more gold papers from a candidate pool than arXiv's relevance order? (P2, offline)

Usage:
    python3 -I cite_probe.py --pools /tmp/pool.json [--screen /tmp/screen.json] [--pool 50]

Citation counts come from OpenAlex (arXiv DOI 10.48550/arxiv.<id>). Today's count carries hindsight the agent
would not have had at the survey's date, so two variants are reported:
    now      cited_by_count today
    to_end   citations received up to the end of the window's year (counts_by_year), i.e. at most a few months late
With ``--screen`` (output of screen_probe.py) papers scored below 2 are dropped before ranking. Development set only.
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE / ".openalex_cache.json"  # gitignored
UA = {"User-Agent": "deerflow-citeguard-eval/0.1 (+https://github.com/unumbrela/deerflow-citeguard)"}


def counts(ids: list[str]) -> dict[str, dict]:
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    missing = [i for i in ids if cache.get(i) is None]
    for start in range(0, len(missing), 25):
        chunk = missing[start : start + 25]
        # Preprints merged into a published version keep the arXiv page among their locations, not as the DOI.
        flt = "locations.landing_page_url:" + "|".join(f"{s}://arxiv.org/abs/{i}" for i in chunk for s in ("http", "https"))
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode({"filter": flt, "per-page": 50, "select": "cited_by_count,counts_by_year,locations"})
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as resp:
            results = json.loads(resp.read())["results"]
        found = {}
        for r in results:
            for loc in r.get("locations") or []:
                page = (loc.get("landing_page_url") or "").rsplit("/abs/", 1)
                if len(page) == 2 and page[1] in chunk and page[1] not in found:
                    found[page[1]] = r
        for i in chunk:
            r = found.get(i)
            cache[i] = {"now": r["cited_by_count"], "by_year": {str(c["year"]): c["cited_by_count"] for c in r["counts_by_year"]}} if r else None
        CACHE.write_text(json.dumps(cache))
        time.sleep(1)
    return {i: cache.get(i) for i in ids}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pools", required=True)
    ap.add_argument("--screen")
    ap.add_argument("--pool", type=int, default=50)
    args = ap.parse_args()
    topics = {t["id"]: t for t in json.loads((HERE / "coverage_topics.json").read_text())["topics"]}
    screen = {r["id"]: r["scores"] for r in json.loads(Path(args.screen).read_text())} if args.screen else {}
    totals = {"rank": 0, "now": 0, "to_end": 0}
    for r in json.loads(Path(args.pools).read_text()):
        topic = topics[r["id"]]
        gold = set(topic["gold"])
        cands = r["pool_ids"][: args.pool]
        if r["id"] in screen:
            cands = [p for p in cands if screen[r["id"]].get(p, 0) >= 2] or cands
        c = counts(cands)
        end_year = int(topic["end_date"][:4])

        def to_end(p: str) -> int:
            return sum(n for y, n in (c[p] or {}).get("by_year", {}).items() if int(y) <= end_year)

        picks = {
            "rank": cands[:10],
            "now": sorted(cands, key=lambda p: (-((c[p] or {}).get("now") or 0), cands.index(p)))[:10],
            "to_end": sorted(cands, key=lambda p: (-to_end(p), cands.index(p)))[:10],
        }
        hits = {k: sum(p in gold for p in v) for k, v in picks.items()}
        for k in totals:
            totals[k] += hits[k]
        unmatched = sum(c[p] is None for p in cands)
        print(f"{r['id']} cands={len(cands):3} pool_gold={sum(p in gold for p in cands):3} unmatched={unmatched:2} " + " ".join(f"{k}={v}" for k, v in hits.items()), flush=True)
    print("total:", totals)


if __name__ == "__main__":
    main()
