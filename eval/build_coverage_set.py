"""Build the coverage benchmark: real arXiv surveys as the answer key for "did the agent find the papers that matter?".

Usage:
    python3 -I build_coverage_set.py select   # candidate surveys by a fixed rule -> coverage_candidates.json
    python3 -I build_coverage_set.py gold     # each survey's in-scope arXiv references -> coverage_topics.json

Selection rule (fixed in advance, no hand-picking): for each category, arXiv's top results by relevance for
title "survey", submitted in the window below, primary category equal to the category. A survey is kept when
its LaTeX source is available and at least MIN_GOLD of its arXiv-id references fall in the task's scope.

Gold set of a survey = references that carry an arXiv id in its .bbl/.bib, whose primary category equals the
survey's, and that were submitted in the two years before the survey (the window the agent is asked to search).
References without an arXiv id are invisible to this metric; that biases the key towards preprints, so the
metric is only used to compare configurations, not as an absolute recall.

Downloaded sources are untrusted: they are read with tarfile in memory, never extracted or executed.
"""

from __future__ import annotations

import argparse
import gzip
import io
import json
import re
import tarfile
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CACHE = HERE / ".coverage_cache"  # gitignored: raw sources and API responses
CATEGORIES = ["cs.CL", "cs.AI", "cs.LG", "cs.CV", "cs.IR", "cs.SE", "cs.RO", "cs.CR"]
SUBMITTED = ("202507010000", "202606302359")
PER_CATEGORY = 6
MIN_GOLD = 12
UA = {"User-Agent": "deerflow-citeguard-eval/0.1 (+https://github.com/unumbrela/deerflow-citeguard)"}
NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
REF_ID_RE = re.compile(r"(?<![\d.])(\d{4}\.\d{4,5})(?:v\d+)?(?!\d)")
TITLE_PREFIX = re.compile(r"^(?:a|an|the)?\s*(?:comprehensive|systematic|brief|short|unified|holistic)?\s*(?:survey|review|overview)\s+(?:on|of)\s+", re.I)


def _get(url: str, timeout: int = 90) -> bytes:
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as resp:
                return resp.read()
        except Exception:  # noqa: BLE001 - arXiv rate limits; back off and retry
            time.sleep(5 * 2**attempt)
    raise SystemExit(f"giving up on {url}")


def _entries(xml_bytes: bytes) -> list[dict]:
    out = []
    for e in ET.fromstring(xml_bytes).findall("a:entry", NS):
        prim = e.find("x:primary_category", NS)
        out.append(
            {
                "id": re.sub(r"v\d+$", "", e.findtext("a:id", default="", namespaces=NS).split("/abs/")[-1]),
                "title": " ".join(e.findtext("a:title", default="", namespaces=NS).split()),
                "published": e.findtext("a:published", default="", namespaces=NS)[:10],
                "primary_category": prim.get("term", "") if prim is not None else "",
            }
        )
    return out


def topic_from_title(title: str) -> str:
    """'A Survey on X' -> 'X'; 'X: A Survey' -> 'X'. Used verbatim in the agent prompt."""
    head, _, tail = title.partition(":")
    if re.search(r"survey|review|overview", tail, re.I) and not re.search(r"survey|review|overview", head, re.I):
        return head.strip()
    return TITLE_PREFIX.sub("", title).strip().rstrip(".")


def metadata(ids: list[str]) -> dict[str, dict]:
    cache_f = CACHE / "metadata.json"
    cache = json.loads(cache_f.read_text()) if cache_f.exists() else {}
    missing = [i for i in dict.fromkeys(ids) if i not in cache]
    for start in range(0, len(missing), 100):
        chunk = missing[start : start + 100]
        for e in _entries(_get("https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(chunk))):
            cache[e["id"]] = e
        for i in chunk:
            cache.setdefault(i, None)  # id does not exist on arXiv (typo in a bib file)
        cache_f.write_text(json.dumps(cache))
        time.sleep(3.5)
    return {i: cache[i] for i in ids if cache.get(i)}


def reference_ids(survey_id: str) -> list[str] | None:
    """arXiv ids in the survey's .bbl/.bib files, or None when no LaTeX source is available."""
    raw_f = CACHE / "src" / survey_id.replace("/", "_")
    if not raw_f.exists():
        raw_f.parent.mkdir(parents=True, exist_ok=True)
        raw_f.write_bytes(_get(f"https://arxiv.org/src/{survey_id}"))
        time.sleep(3.5)
    data = raw_f.read_bytes()
    texts: list[str] = []
    try:
        with tarfile.open(fileobj=io.BytesIO(data)) as tf:
            for m in tf.getmembers():
                if m.isfile() and m.name.endswith((".bbl", ".bib")) and m.size < 50_000_000:
                    texts.append(tf.extractfile(m).read().decode("utf-8", "replace"))
    except tarfile.ReadError:
        try:
            single = gzip.decompress(data).decode("utf-8", "replace")  # single-file submission
        except OSError:
            return None  # PDF-only submission
        if "\\bibitem" in single or "@" in single:
            texts.append(single)
    if not texts:
        return None
    return [i for i in dict.fromkeys(REF_ID_RE.findall("\n".join(texts))) if i != survey_id]


def cmd_select(_args) -> None:
    candidates = []
    for cat in CATEGORIES:
        q = f"ti:survey AND cat:{cat} AND submittedDate:[{SUBMITTED[0]} TO {SUBMITTED[1]}]"
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": q, "max_results": 30, "sortBy": "relevance"})
        found = [e for e in _entries(_get(url)) if e["primary_category"] == cat][:PER_CATEGORY]
        candidates += [{**e, "category": cat, "topic": topic_from_title(e["title"])} for e in found]
        time.sleep(3.5)
    (HERE / "coverage_candidates.json").write_text(json.dumps(candidates, ensure_ascii=False, indent=1))
    print(f"{len(candidates)} candidate surveys")


def cmd_gold(_args) -> None:
    candidates = json.loads((HERE / "coverage_candidates.json").read_text())
    topics, dropped = [], []
    for n, c in enumerate(candidates, 1):
        refs = reference_ids(c["id"])
        if refs is None:
            dropped.append({"id": c["id"], "reason": "no LaTeX bibliography"})
            continue
        end = date.fromisoformat(c["published"])
        start = end.replace(year=end.year - 2) if not (end.month == 2 and end.day == 29) else end.replace(year=end.year - 2, day=28)
        meta = metadata(refs)
        gold = [i for i, m in meta.items() if m["primary_category"] == c["category"] and start.isoformat() <= m["published"] <= end.isoformat()]
        if len(gold) < MIN_GOLD:
            dropped.append({"id": c["id"], "reason": f"only {len(gold)} in-scope arXiv references"})
            continue
        topics.append({"id": f"c{len(topics) + 1:02d}", "survey": c["id"], "survey_title": c["title"], "topic": c["topic"], "category": c["category"], "start_date": start.isoformat(), "end_date": end.isoformat(), "refs_with_arxiv_id": len(refs), "gold": sorted(gold)})
        print(f"[{n}/{len(candidates)}] {c['id']} {c['category']} gold={len(gold)} refs={len(refs)} :: {c['topic'][:60]}")
    (HERE / "coverage_topics.json").write_text(json.dumps({"rule": __doc__.split("Selection rule")[1].split("Downloaded")[0].strip(), "dropped": dropped, "topics": topics}, ensure_ascii=False, indent=1))
    print(f"kept {len(topics)}, dropped {len(dropped)}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["select", "gold"])
    args = ap.parse_args()
    {"select": cmd_select, "gold": cmd_gold}[args.cmd](args)
