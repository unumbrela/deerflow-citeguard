"""Check the citations in a generated literature-review report against arXiv.

Usage:
    python3 -I check_citations.py REPORT.md [--since 2024-10-25] [--until 2026-10-24] [--category cs.CL] [--json OUT.json]

Metrics (all computed against the official arXiv API, never against the model):
    verified        HEADLINE: the cited id exists AND its title matches arXiv's (>= 0.85 similar).
                    Existence alone proves nothing: fabricated ids usually point at some other real paper.
    resolved        cited arXiv ids that exist (weak; kept for diagnosis only)
    first_author    reference's first author surname matches arXiv's first author (last APA line = reference list)
    consistent      all APA lines for the same paper agree on first author and year
    year            reference year matches arXiv's published year
    title           reference title is >= 0.85 similar to arXiv's title
    in_window       arXiv published date is within --since / --until
    in_category     arXiv primary category equals --category

Only the first author is compared, so `first_author` is a lenient check.
Only references written as "Authors (Year). Title. *arXiv preprint arXiv:ID*" (APA) are parsed;
unparsed references are counted in `unparsed`.
"""

import argparse
import difflib
import json
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})|arXiv:(\d{4}\.\d{4,5})")
# "(2025)", "(2025a)" or "(2024, November 25)"; the id may follow the title as "*arXiv preprint", "arXiv" or "[arXiv:ID]".
REF_RE = re.compile(r"(.+?)\((\d{4})[a-z]?(?:,[^)]*)?\)\.\s+(.+?)\s+[\[(]?\*?arXiv", re.S)


CACHE = Path(__file__).resolve().parent / ".arxiv_cache.json"  # arXiv id -> metadata; each id is fetched once
RETRYABLE = {429, 500, 502, 503, 504}


def _fetch(ids: list[str]) -> dict[str, dict]:
    url = "https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(ids)
    req = urllib.request.Request(url, headers={"User-Agent": "deerflow-citation-check/0.1 (research eval; contact: local)"})
    for attempt in range(10):  # arXiv throttles with 429/503; back off (up to ~15 min in total) and retry
        try:
            root = ET.fromstring(urllib.request.urlopen(req, timeout=60).read())
            break
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
            code = getattr(e, "code", None)
            if (code is not None and code not in RETRYABLE) or attempt == 9:
                raise
            retry_after = int(e.headers.get("Retry-After") or 0) if code is not None else 0
            time.sleep(max(retry_after, 15 * (attempt + 1)))
    truth = {}
    for e in root.findall("a:entry", NS):
        i = e.find("a:id", NS).text.split("/abs/")[-1].split("v")[0]
        pc = e.find("x:primary_category", NS)
        truth[i] = {
            "title": " ".join(e.find("a:title", NS).text.split()),
            "published": e.find("a:published", NS).text[:10],
            "authors": [a.find("a:name", NS).text for a in e.findall("a:author", NS)],
            "primary_category": pc.get("term") if pc is not None else None,
        }
    return truth


def fetch_truth(ids: list[str]) -> dict[str, dict]:
    cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
    missing = [i for i in ids if i not in cache]
    if missing:
        cache.update(_fetch(missing))
        CACHE.write_text(json.dumps(cache, ensure_ascii=False))
    return {i: cache[i] for i in ids if i in cache}


# markdown noise that can precede the authors: heading marks, section numbers, list bullets, "**Citation**:" labels
LIST_MARK = re.compile(r"^\s*(?:#+\s*)?(?:(?:[-*]|\d+(?:\.\d+)*\.?)\s+)*(?:\*{0,2}[A-Za-z ]{1,25}\*{0,2}:\s*)?")


def parse_references(text: str) -> list[dict]:
    """One entry per distinct arXiv id mentioned anywhere in the report.

    Report layouts vary (`## References`, `## Sources`, APA lines inside per-paper summaries...), so instead of
    locating a section we look, for each id, for a single-line APA entry that contains it.
    Ids with no such line are kept with parsed=False and counted as `unparsed`.
    """
    lines = text.splitlines()
    ids: list[str] = []
    for a, b in ID_RE.findall(text):
        if (a or b) not in ids:
            ids.append(a or b)
    refs = []
    for i in ids:
        ref = {"id": i, "parsed": False}
        found = []
        for line in lines:
            if i not in line:
                continue
            m = REF_RE.match(LIST_MARK.sub("", line).strip())
            if m:
                found.append((m.group(1).split(",")[0].strip().lower(), m.group(2), m.group(3).strip().rstrip(".").strip("*_")))
        if found:
            # The reference list comes last, so the last APA line is what gets checked.
            # `consistent` flags papers whose APA lines disagree on first author or year.
            ref.update(parsed=True, first_author=found[-1][0], year=found[-1][1], title=found[-1][2], consistent=len({(a, y) for a, y, _ in found}) == 1)
        refs.append(ref)
    return refs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--since", help="YYYY-MM-DD, earliest allowed publication date")
    ap.add_argument("--until", help="YYYY-MM-DD, latest allowed publication date")
    ap.add_argument("--category", help="required arXiv primary category, e.g. cs.CL")
    ap.add_argument("--json", help="write metrics to this file")
    args = ap.parse_args()

    refs = parse_references(open(args.report, encoding="utf-8").read())
    truth = fetch_truth(sorted({r["id"] for r in refs})) if refs else {}

    rows = []
    for r in refs:
        t = truth.get(r["id"])
        row = {"id": r["id"], "resolved": t is not None, "verified": False}
        if t:
            row["in_window"] = None if not (args.since or args.until) else (args.since or "") <= t["published"] <= (args.until or "9999")
            row["in_category"] = None if not args.category else t["primary_category"] == args.category
            if r["parsed"]:
                row["first_author"] = r["first_author"] == t["authors"][0].split()[-1].lower()
                row["year"] = r["year"] == t["published"][:4]
                row["title"] = difflib.SequenceMatcher(None, r["title"].lower().strip('"').rstrip("?"), t["title"].lower().rstrip("?")).ratio() >= 0.85
                row["verified"] = row["title"]
                row["consistent"] = r["consistent"]
        rows.append(row)

    def rate(key: str):
        vals = [x[key] for x in rows if x.get(key) is not None]
        return {"ok": sum(vals), "of": len(vals)}

    metrics = {k: rate(k) for k in ("verified", "resolved", "first_author", "year", "title", "consistent", "in_window", "in_category")}
    metrics["references"] = len(refs)
    metrics["unparsed"] = sum(not r["parsed"] for r in refs)
    out = {"metrics": metrics, "rows": rows}
    print(json.dumps(metrics, indent=1))
    if args.json:
        with open(args.json, "w") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
