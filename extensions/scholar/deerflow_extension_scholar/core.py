"""Pure logic: date windows, result selection, batching, and citation checks.

Why this exists: when the model re-types paper metadata (from a tool result
into a subagent prompt, or from subagent output into a report) it can silently
invent papers. In measured runs, every run where the search output was swapped
for a synopsis and never read back fabricated most of its citations. So code,
not the model, filters, moves and checks paper data.

Retrieval (P2): the papers a review cites used to be exactly what one arXiv
relevance query returned first, so coverage was fixed by the query. On the
coverage development set, ranking a 50-paper pool plus its in-scope references
by how many pool papers cite them, then dropping off-topic papers by a model
score, picked 21 survey-cited papers where arXiv's top 10 picked 10.
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
FULLTEXT_BATCH_PAPERS = 4  # each paper's text is read section by section on top of its batch entry
OUTLINE_CHARS = 500  # the outline line added to each batch entry when full text is on
POOL_SIZE = 50  # arXiv candidates per search, whatever the requested count
SHORTLIST_FACTOR = 3  # candidates screened per requested paper
SHORTLIST_MAX = 100  # ten scoring calls; the host admits at most twice its granted concurrency at once
REF_LOOKUP_MAX = 150  # referenced papers whose metadata is fetched (one arXiv request)
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
    fetch_n = min(2 * max_results, 100) if primary_only else max_results

    def keep(found: list[dict]) -> list[dict]:
        # The arXiv query already required a listing in `category`, so only the primary filter is left to apply.
        return [p for p in found if p.get("primary_category") == category] if primary_only else found

    papers = keep(await fetch("phrase", fetch_n))
    match = "phrase"
    if len(papers) < max_results and len(query.split()) > 1:
        seen = {p["id"] for p in papers}
        papers += [p for p in keep(await fetch("all_terms", fetch_n)) if p["id"] not in seen]
        match = "phrase+all_terms"
    return papers[:max_results], match


def in_scope(paper: dict, category: str | None, include_cross_lists: bool) -> bool:
    if not category:
        return True
    if include_cross_lists:
        return category in (paper.get("categories") or [paper.get("primary_category")])
    return paper.get("primary_category") == category


def in_window(paper: dict, window: dict) -> bool:
    published = paper.get("published", "")
    return bool(published) and (not window.get("start") or published >= window["start"]) and (not window.get("end") or published <= window["end"])


def may_be_in_window(pid: str, window: dict) -> bool:
    """New-style arXiv ids start with the submission year and month, so most references can be ruled out unfetched."""
    m = re.fullmatch(r"(\d{2})(\d{2})\.\d{4,5}", pid)
    if not m:
        return False
    yymm = f"20{m[1]}-{m[2]}"
    return (not window.get("start") or yymm >= window["start"][:7]) and (not window.get("end") or yymm <= window["end"][:7])


def cocitation_counts(pool: list[dict], references: dict[str, list[str] | None]) -> dict[str, int]:
    """How many pool papers cite each paper. Only backward references: nothing after the window can enter."""
    counts: dict[str, int] = {}
    for paper in pool:
        for ref in set(references.get(paper["id"]) or []):
            if ref != paper["id"]:
                counts[ref] = counts.get(ref, 0) + 1
    return counts


def refs_to_fetch(pool: list[dict], counts: dict[str, int], window: dict, limit: int = REF_LOOKUP_MAX) -> list[str]:
    """Referenced papers outside the pool worth a metadata lookup, most-cited first."""
    have = {p["id"] for p in pool}
    wanted = [pid for pid in counts if pid not in have and may_be_in_window(pid, window)]
    return sorted(wanted, key=lambda pid: -counts[pid])[:limit]


def rank_candidates(pool: list[dict], expanded: list[dict], counts: dict[str, int]) -> list[dict]:
    """Pool and in-scope references, most co-cited first; ties keep arXiv's order, pool before references."""
    union = pool + [p for p in expanded if p["id"] not in {q["id"] for q in pool}]
    order = {p["id"]: i for i, p in enumerate(union)}
    return sorted(union, key=lambda p: (-counts.get(p["id"], 0), order[p["id"]]))


def shortlist_size(requested: int) -> int:
    return min(SHORTLIST_FACTOR * requested, SHORTLIST_MAX)


def select_screened(shortlist: list[dict], scores: dict[str, int], n: int) -> list[dict]:
    """Keep the shortlist's co-citation order. Central papers (2-3) first, then peripheral (1); off-topic (0) never."""
    central = [p for p in shortlist if scores.get(p["id"], 0) >= 2]
    peripheral = [p for p in shortlist if scores.get(p["id"], 0) == 1]
    return (central + peripheral)[:n]


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


def fulltext_batches(papers: list[dict]) -> list[list[str]]:
    """Batches that still fit the budget once every entry carries its outline line."""
    return make_batches(papers, budget=BATCH_CHAR_BUDGET - FULLTEXT_BATCH_PAPERS * OUTLINE_CHARS, max_papers=FULLTEXT_BATCH_PAPERS)


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


# Evidence ids (P2.4): a report sentence carries [E3] where its claim rests on a quote that code checked against the paper.
EVIDENCE_RE = re.compile(r"\[\s*(E\d+(?:\s*[,;]\s*E\d+)*)\s*\]")
APPENDIX_BEGIN = "<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->"
APPENDIX_END = "<!-- /evidence-appendix -->"


def strip_appendix(report_text: str) -> str:
    """The report without the gate's appendix, which itself links every evidence paper."""
    start = report_text.find(APPENDIX_BEGIN)
    if start < 0:
        return report_text
    end = report_text.find(APPENDIX_END, start)
    tail = report_text[end + len(APPENDIX_END) :] if end >= 0 else ""
    return report_text[:start].rstrip() + ("\n" + tail.lstrip("\n") if tail.strip() else "\n")


def evidence_ids(report_text: str) -> list[str]:
    out: list[str] = []
    for group in EVIDENCE_RE.findall(report_text):
        for eid in re.split(r"\s*[,;]\s*", group):
            if eid not in out:
                out.append(eid)
    return out


_SENTENCE_END = re.compile(r"(?<!\bet al)(?<!\be\.g)(?<!\bi\.e)(?<!\bvs)[.!?](?=\s+[A-Z*(\"“])")


def _sentences(line: str) -> list[str]:
    out, start = [], 0
    for m in _SENTENCE_END.finditer(line):
        out.append(line[start : m.end()])
        start = m.end()
    out.append(line[start:])
    return out


def _mentions(text: str, paper: dict) -> bool:
    """Does this text cite the paper: its arXiv id, its first author's surname with its year, or its title."""
    low = text.lower()
    if paper["id"] in text or (paper.get("title") and _norm(paper["title"]) in _norm(text)):
        return True
    sn = surname(paper["authors"][0]).lower() if paper.get("authors") else ""
    year = (paper.get("published") or "")[:4]
    return bool(sn and year and re.search(rf"\b{re.escape(sn)}\b", low) and year in low)


def misattached_evidence(report_text: str, by_e: dict[str, dict], papers: dict[str, dict]) -> list[str]:
    """Evidence ids placed where their paper is not cited: not in the same sentence, the one before it, the paragraph's lead sentence, the heading above, or the first line under that heading.

    In a smoke run the model put six ids next to theme names in one summary sentence citing no paper. The
    sentence before counts because "Hao et al. (2024) introduced Coconut [E8]. Coconut also ... [E9]" is
    still about one paper. The first line under a heading counts because per-paper blocks open with the
    paper's citation ("### 4. CLOUDS" then "**Citation:** Benigmim, Y., ... (2023)") and list findings below.
    """
    problems: list[str] = []
    heading = block_lead = ""
    for line in report_text.splitlines():
        if line.lstrip().startswith("#"):
            heading, block_lead = line, ""
            continue
        if not block_lead and line.strip():
            block_lead = line
        if not EVIDENCE_RE.search(line):
            continue
        sentences = _sentences(line)
        for n, sentence in enumerate(sentences):
            context = (sentence, sentences[n - 1] if n else "", sentences[0], heading, block_lead)
            for group in EVIDENCE_RE.findall(sentence):
                for eid in re.split(r"\s*[,;]\s*", group):
                    paper = papers.get(by_e.get(eid, {}).get("paper", ""))
                    if paper is None:
                        continue  # unknown ids are reported separately
                    if not any(_mentions(t, paper) for t in context if t):
                        problem = f"{eid} (belongs to {paper_label(paper)})"
                        if problem not in problems:
                            problems.append(problem)
    return problems


def paper_label(paper: dict) -> str:
    """Short title plus author-year: two papers can share "Wu, 2025" (WebWalker and WebDancer did in one run)."""
    sn = surname(paper["authors"][0]) if paper.get("authors") else paper["id"]
    short = re.split(r"[:—–]| - ", paper.get("title", ""), maxsplit=1)[0].strip()[:40] or paper["id"]
    return f"{short} ({sn}, {(paper.get('published') or '')[:4]})"


def check_evidence(report_text: str, evidence: list[dict], papers: list[dict], cited: list[str]) -> dict:
    """Evidence ids must have been issued in this search and sit in a sentence citing their paper; checked quotes for a cited paper must be used."""
    by_e = {e["e"]: e for e in evidence}
    by_id = {p["id"]: p for p in papers}
    used = evidence_ids(report_text)
    unknown = [e for e in used if e not in by_e]
    uncited = [f"{e} ({by_e[e]['paper']})" for e in used if e in by_e and by_e[e]["paper"] not in cited]
    with_evidence = {by_e[e]["paper"] for e in used if e in by_e}
    has_quotes = {e["paper"] for e in evidence}
    return {
        "used": [e for e in used if e in by_e],
        "unknown_evidence": unknown,
        "uncited_evidence": uncited,
        "misattached_evidence": misattached_evidence(report_text, by_e, by_id) if not uncited else [],
        "unused_evidence": [paper_label(by_id[pid]) + f" [{', '.join(e['e'] for e in evidence if e['paper'] == pid)}]" for pid in cited if pid in has_quotes and pid not in with_evidence and pid in by_id],
        "papers_without_evidence": [pid for pid in cited if pid not in with_evidence],
    }


def _cell(text: str) -> str:
    return " ".join(text.split()).replace("|", "\\|")


def render_appendix(used: list[str], evidence: list[dict], checked_on: str) -> str:
    by_e = {e["e"]: e for e in evidence}
    rows = [f"| {eid} | arXiv:{e['paper']} | [{_cell(e.get('section') or e['para'])}](https://arxiv.org/html/{e['paper']}#{e['para']}) | “{_cell(e['quote'])}” |" for eid in used if (e := by_e.get(eid))]
    sources = {by_e[eid].get("source", "html") for eid in used if eid in by_e}
    basis = "the paper's arXiv HTML" if sources == {"html"} else "the paper's arXiv HTML, or its abstract where no HTML exists"
    return "\n".join(
        [
            APPENDIX_BEGIN,
            "",
            "## Evidence",
            "",
            f"Each [E#] in the text points to a quote below. Code checked on {checked_on} that every quote appears word for word in {basis} (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.",
            "",
            "| Id | Paper | Location | Quote |",
            "|---|---|---|---|",
            *rows,
            "",
            APPENDIX_END,
        ]
    )
