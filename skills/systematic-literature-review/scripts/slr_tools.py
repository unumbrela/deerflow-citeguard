#!/usr/bin/env python3
"""Deterministic helpers for the systematic-literature-review skill.

Why this exists: when the model has to re-type paper metadata (from a tool
result into a subagent prompt, or from subagent output into a report), it can
silently invent papers. In measured runs, every run where the search output was
swapped for a synopsis and never read back fabricated most of its citations.
These subcommands keep paper data in files and let code, not the model, move
and check it.

  search  Query arXiv, write papers.json + batch_N.json, print a COMPACT index.
  verify  Check that every arXiv id in a finished report came from papers.json.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

import arxiv_search

ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})|arXiv:\s*(\d{4}\.\d{4,5})", re.I)
RETRY_STATUS = ("429", "502", "503", "504")
MAX_ATTEMPTS = 5


def window_start(today: date, years: int) -> date:
    try:
        return today.replace(year=today.year - years)
    except ValueError:  # Feb 29
        return today.replace(year=today.year - years, day=28)


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _search_with_retry(**kwargs) -> list[dict]:
    for attempt in range(MAX_ATTEMPTS):
        try:
            return arxiv_search.search(**kwargs)
        except Exception as exc:
            transient = any(code in str(exc) for code in RETRY_STATUS) or "timed out" in str(exc).lower()
            if not transient or attempt == MAX_ATTEMPTS - 1:
                raise
            time.sleep(5 * 2**attempt)
    return []


def run_search(args: argparse.Namespace, today: date | None = None) -> dict:
    today = today or date.today()
    start = args.start_date or (window_start(today, args.years).isoformat() if args.years else None)
    fetch_n = args.max_results
    if args.category and not args.include_cross_lists:
        # cat: also matches cross-listed papers; fetch the maximum so filtering
        # to the primary category can still fill the requested count.
        fetch_n = arxiv_search.MAX_RESULTS_UPPER_BOUND

    def fetch(match: str) -> list[dict]:
        found = _search_with_retry(
            query=args.query,
            max_results=fetch_n,
            category=args.category,
            sort_by="relevance",
            start_date=start,
            end_date=args.end_date,
            match=match,
        )
        if args.category and not args.include_cross_lists:
            found = [p for p in found if p.get("primary_category") == args.category]
        return found

    papers = fetch("phrase")
    match_used = "phrase"
    if len(papers) < args.max_results and " " in args.query.strip():
        # The exact phrase is too narrow. Widen the QUERY (never the category or
        # date window, which are the user's constraints) so the model has no
        # reason to drop those filters itself to reach the requested count.
        time.sleep(3)  # arXiv asks for >= 3 s between calls
        seen = {p["id"] for p in papers}
        papers += [p for p in fetch("all_terms") if p["id"] not in seen]
        match_used = "phrase+all_terms"
    papers = papers[: args.max_results]

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for stale in out.glob("batch_*.json"):
        stale.unlink()
    batches = [papers[i : i + args.batch_size] for i in range(0, len(papers), args.batch_size)]
    batch_files = []
    for n, batch in enumerate(batches, 1):
        path = out / f"batch_{n}.json"
        path.write_text(json.dumps(batch, ensure_ascii=False, indent=1), encoding="utf-8")
        batch_files.append(str(path))
    meta = {
        "query": args.query,
        "category": args.category,
        "window": {"start": start, "end": args.end_date},
        "requested": args.max_results,
        "match": match_used,
        "retrieved_on": today.isoformat(),
        "papers": papers,
    }
    papers_file = out / "papers.json"
    papers_file.write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")

    # Compact on purpose: must stay far below the tool-output externalization
    # threshold so the model sees the whole index, not a synopsis of it.
    index = [
        {
            "id": p["id"],
            "title": p["title"][:80],
            "first_author": p["authors"][0] if p["authors"] else "",
            "published": p["published"],
            "cat": p.get("primary_category", ""),
        }
        for p in papers
    ]
    return {
        "count": len(papers),
        "requested": args.max_results,
        "window": meta["window"],
        "match": match_used,
        "papers_file": str(papers_file),
        "batch_files": batch_files,
        "index": index,
    }


def surname(author: str) -> str:
    parts = author.replace(",", " ").split()
    return parts[-1] if parts else ""


def run_verify(report_text: str, papers_meta: dict) -> dict:
    by_id = {p["id"]: p for p in papers_meta["papers"]}
    cited: list[str] = []
    for a, b in ID_RE.findall(report_text):
        pid = a or b
        if pid not in cited:
            cited.append(pid)
    lines = report_text.splitlines()
    norm_report = _norm(report_text)
    unknown, warnings = [], []
    for pid in cited:
        paper = by_id.get(pid)
        if paper is None:
            unknown.append(pid)
            continue
        if _norm(paper["title"]) not in norm_report:
            warnings.append(f"{pid}: official title not found verbatim ({paper['title']!r})")
        if paper["authors"]:
            sn = surname(paper["authors"][0]).lower()
            id_lines = " ".join(ln for ln in lines if pid in ln).lower()
            if sn and sn not in id_lines:
                warnings.append(f"{pid}: first author {paper['authors'][0]!r} not on the reference line")
    return {
        "ok": not unknown,
        "cited": len(cited),
        "retrieved": len(by_id),
        "unknown_ids": unknown,
        "warnings": warnings,
        "not_cited": [pid for pid in by_id if pid not in cited],
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="query arXiv and write batch files")
    s.add_argument("query")
    s.add_argument("--max-results", type=int, default=20)
    s.add_argument("--category", default=None, help="e.g. cs.CL; matched against the PRIMARY category")
    s.add_argument("--include-cross-lists", action="store_true", help="also accept papers merely cross-listed in --category")
    s.add_argument("--years", type=int, default=None, help="only papers submitted within the last N years (computed from today)")
    s.add_argument("--start-date", default=None, help="YYYY-MM-DD; overrides --years")
    s.add_argument("--end-date", default=None)
    s.add_argument("--batch-size", type=int, default=5)
    # Required, never defaulted: the sandbox only maps /mnt/user-data/... paths
    # that appear in the command line. A path defaulted inside this script lands
    # outside the thread's real workspace, invisible to subagents and file tools.
    s.add_argument("--out-dir", required=True, help="e.g. /mnt/user-data/workspace/slr")

    v = sub.add_parser("verify", help="check a finished report against papers.json")
    v.add_argument("report")
    v.add_argument("--papers", required=True, help="papers.json written by `search`")
    return parser


def main() -> int:
    args = _build_parser().parse_args()
    try:
        if args.cmd == "search":
            result = run_search(args)
            if result["count"] == 0:
                print("slr_tools.py: 0 papers matched. Broaden the topic or drop the category/date filter.", file=sys.stderr)
            json.dump(result, sys.stdout, ensure_ascii=False, separators=(",", ":"))
            sys.stdout.write("\n")
            return 0
        meta = json.loads(Path(args.papers).read_text(encoding="utf-8"))
        result = run_verify(Path(args.report).read_text(encoding="utf-8"), meta)
        json.dump(result, sys.stdout, ensure_ascii=False, indent=1)
        sys.stdout.write("\n")
        return 0 if result["ok"] else 1
    except Exception as exc:
        print(f"slr_tools.py: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
