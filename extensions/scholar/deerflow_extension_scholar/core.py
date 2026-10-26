"""Pure logic: date windows, result selection, batching, and citation checks.

Why this exists: when the model re-types paper metadata (from a tool result
into a subagent prompt, or from subagent output into a report) it can silently
invent papers. In measured runs, every run where the search output was swapped
for a synopsis and never read back fabricated most of its citations. So code,
not the model, filters, moves and checks paper data.
"""

from __future__ import annotations

import json
import re
from collections.abc import Awaitable, Callable
from datetime import date

DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})|arXiv:\s*(\d{4}\.\d{4,5})", re.IGNORECASE)
BATCH_CHAR_BUDGET = 9000  # stays under the host's 12,000-char tool-output externalization threshold
BATCH_MAX_PAPERS = 5
MAX_AUTHORS = 20  # APA 7 lists at most 20 authors; huge collaborations would blow the batch budget
INDEX_TITLE_CHARS = 80


def window_start(today: date, years: int) -> date:
    try:
        return today.replace(year=today.year - years)
    except ValueError:  # Feb 29
        return today.replace(year=today.year - years, day=28)


def resolve_window(today: date, years: int | None, start_date: str | None, end_date: str | None) -> dict:
    """``years`` becomes an exact start date here, so the model never computes dates itself."""
    start = start_date or (window_start(today, years).isoformat() if years else None)
    return {"start": start, "end": end_date}


Fetch = Callable[[str, int], Awaitable[list[dict]]]


async def select_papers(fetch: Fetch, *, query: str, max_results: int, category: str | None, include_cross_lists: bool) -> tuple[list[dict], str]:
    """Run the phrase query, widen to all-terms if short, keep only primary-category matches.

    ``fetch(match, n)`` performs one arXiv query. Only the QUERY is widened, never
    the category or date window: those are the user's constraints, and when the
    tool stopped short the model used to drop them itself to reach the count.
    """
    primary_only = bool(category) and not include_cross_lists
    # cat: also matches cross-listed papers; over-fetch so primary filtering can still fill the count.
    fetch_n = 50 if primary_only else max_results

    def keep(found: list[dict]) -> list[dict]:
        return [p for p in found if p.get("primary_category") == category] if primary_only else found

    papers = keep(await fetch("phrase", fetch_n))
    match = "phrase"
    if len(papers) < max_results and len(query.split()) > 1:
        seen = {p["id"] for p in papers}
        papers += [p for p in keep(await fetch("all_terms", fetch_n)) if p["id"] not in seen]
        match = "phrase+all_terms"
    return papers[:max_results], match


def batch_paper(paper: dict) -> dict:
    """The fields a subagent needs, with the author list capped for size."""
    authors = paper.get("authors", [])
    out = {
        "id": paper["id"],
        "title": paper["title"],
        "authors": authors[:MAX_AUTHORS],
        "published": paper.get("published", ""),
        "primary_category": paper.get("primary_category", ""),
        "abs_url": paper.get("abs_url", ""),
        "abstract": paper.get("abstract", ""),
    }
    if len(authors) > MAX_AUTHORS:
        out["authors_total"] = len(authors)
    return out


def _size(batch: list[dict]) -> int:
    return len(json.dumps(batch, ensure_ascii=False))


def make_batches(papers: list[dict], budget: int = BATCH_CHAR_BUDGET, max_papers: int = BATCH_MAX_PAPERS) -> list[list[str]]:
    """Greedy split into id lists whose serialized batch stays under ``budget`` characters."""
    batches: list[list[str]] = []
    current: list[dict] = []
    for paper in papers:
        item = batch_paper(paper)
        if current and (len(current) >= max_papers or _size(current + [item]) > budget):
            batches.append([p["id"] for p in current])
            current = []
        current.append(item)
    if current:
        batches.append([p["id"] for p in current])
    return batches


def compact_index(papers: list[dict]) -> list[dict]:
    """Small on purpose: the model must see the whole index, never a synopsis of it."""
    return [
        {
            "id": p["id"],
            "title": p["title"][:INDEX_TITLE_CHARS],
            "first_author": p["authors"][0] if p.get("authors") else "",
            "published": p.get("published", ""),
            "cat": p.get("primary_category", ""),
        }
        for p in papers
    ]


def _norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def surname(author: str) -> str:
    parts = author.replace(",", " ").split()
    return parts[-1] if parts else ""


def extract_ids(text: str) -> list[str]:
    ids: list[str] = []
    for a, b in ID_RE.findall(text):
        pid = a or b
        if pid not in ids:
            ids.append(pid)
    return ids


def verify_report(report_text: str, papers: list[dict]) -> dict:
    """Every arXiv id in the report must come from the search; titles and first authors should match."""
    by_id = {p["id"]: p for p in papers}
    cited = extract_ids(report_text)
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
        if paper.get("authors"):
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


def wrong_year_dates(report_text: str, anchors: list[str], known: set[str]) -> list[str]:
    """Dates that share an anchor's month and day but not its year.

    Reports wrote "today" from the model's own sense of the date, about half of
    them with the wrong year (2025-10-26 on 2026-10-26), contradicting the
    window the code had searched. ``anchors`` are the dates the search used
    (retrieval date, window start); ``known`` are real paper dates, which may
    legitimately share a month and day.
    """
    # "Last N years" starts on today's month and day, so one month-day can have several valid dates.
    by_month_day: dict[str, list[str]] = {}
    for anchor in anchors:
        if anchor and anchor not in by_month_day.setdefault(anchor[5:], []):
            by_month_day[anchor[5:]].append(anchor)
    problems: list[str] = []
    for found in DATE_RE.findall(report_text):
        expected = by_month_day.get(found[5:], [])
        if expected and found not in expected and found not in known:
            problem = f"{found} (search used {' / '.join(expected)})"
            if problem not in problems:
                problems.append(problem)
    return problems


# arXiv categories a user may name: dotted (cs.CL, physics.comp-ph) or archives without subjects (quant-ph).
CATEGORY_RE = re.compile(
    r"(?<![\w.-])(?:(?:cs|econ|eess|math|stat|q-bio|q-fin|astro-ph|cond-mat|physics|nlin)\.(?:[a-z]{2}|[a-z]+-[a-z]+)"
    r"|gr-qc|hep-ex|hep-lat|hep-ph|hep-th|math-ph|nucl-ex|nucl-th|quant-ph)(?![\w-])",
    re.IGNORECASE,
)


def normalise_category(category: str | None) -> str | None:
    """``cs.cl`` -> ``cs.CL``; ``physics.comp-ph`` keeps its lowercase subject."""
    if not category:
        return None
    archive, _, subject = category.strip().partition(".")
    if not subject:
        return archive.lower()
    return f"{archive.lower()}.{subject.upper() if len(subject) == 2 else subject.lower()}"


def user_categories(text: str) -> set[str]:
    """Categories named in the user's request. Flash dropped the category from the search call in 9 of 16 runs."""
    return {normalise_category(m) for m in CATEGORY_RE.findall(text)}
