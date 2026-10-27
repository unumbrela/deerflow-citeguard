"""Full text of selected papers: fetch arXiv's HTML, split it into numbered paragraphs, check quotes.

Why this exists (P2.4): a claim could only be checked against the abstract, so a
sentence about a paper's experiments was either unsupported or untraceable.
arXiv renders papers to HTML with LaTeXML, which numbers every paragraph
(``S4.p2`` = section 4, paragraph 2). Code keeps those numbers, so a quote can
be checked against the paragraph it claims to come from, and a reader can jump
to it (``https://arxiv.org/html/<id>#S4.p2``).

Paper text is untrusted input. It reaches the model only as data inside tool
results, never as instructions, and quotes are checked here, not by a model.

Parsing and quote matching use the standard library only: the offline eval
loads this file to read papers the same way for both arms.
"""

from __future__ import annotations

import re
import time
import unicodedata
from datetime import date
from html.parser import HTMLParser
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import httpx

HTML_ENDPOINT = "https://arxiv.org/html/"
MAX_HTML_BYTES = 6_000_000  # DeepSeek-R1's page is about 2 MB; a cap keeps one huge page from stalling a batch
REQUEST_TIMEOUT = 12.0
MIN_QUOTE_WORDS = 6
MAX_QUOTE_CHARS = 600
ABSTRACT_ID = "abstract"

_SECTION_CLASSES = {"ltx_chapter", "ltx_section", "ltx_subsection", "ltx_subsubsection", "ltx_paragraph", "ltx_appendix"}
_OUTLINE_CLASSES = {"ltx_chapter", "ltx_section", "ltx_appendix"}  # the outline lists only top-level sections
_SKIP_CLASSES = {
    "ltx_bibliography",  # references are someone else's titles, not this paper's claims
    "ltx_note",  # footnotes would land in the middle of a sentence
    "ltx_equation",
    "ltx_equationgroup",
    "ltx_tabular",  # table cells; the caption is kept
    "ltx_tag_item",  # list bullets
    "ltx_authors",
    "ltx_dates",
    "ltx_TOC",
    "ltx_page_navbar",
    "ltx_page_logo",
    "ltx_pagination",
    "ltx_keywords",
    "ltx_classification",
    "ltx_listing",  # code listings
}
_SKIP_TAGS = {"script", "style", "nav", "header", "footer", "noscript", "svg", "button", "form"}
_VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
_CITATION = re.compile(r"\([^()]*\b(?:19|20)\d{2}[a-z]?\b[^()]*\)|\[\d+(?:\s*[,–-]\s*\d+)*\]")
_LATEX_COMMAND = re.compile(r"\\[A-Za-z]+")
_WORD = re.compile(r"[a-z0-9]+")


class FulltextError(RuntimeError):
    """The HTML could not be fetched; the paper falls back to its abstract."""


class _Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.sections: list[dict] = []
        self.paragraphs: list[dict | None] = []  # a slot is reserved when a paragraph opens, so nested lists keep reading order
        self._stack: list[tuple[str, str | None]] = []
        self._skip = 0
        self._section_stack: list[dict] = []
        self._buffers: list[tuple[int, str, list[str]]] = []  # (paragraph slot, paragraph id, text parts)
        self._figures: list[str] = []
        self._heading: list[str] | None = None
        self._heading_for: dict | None = None
        self._doc_title = False

    # Elements are pushed with a role so the matching end tag can undo exactly what the start tag did.
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in _VOID:
            return
        a = dict(attrs)
        classes = set((a.get("class") or "").split())
        role: str | None = None
        if self._skip:
            role = None
        elif tag in _SKIP_TAGS or classes & _SKIP_CLASSES or "ltx_title_abstract" in classes:
            role = "skip"
            self._skip += 1
        elif tag == "math":
            role = "skip"
            self._skip += 1
            alt = a.get("alttext")
            if alt:
                self._text(f" {alt} ")
        elif tag == "section" and classes & _SECTION_CLASSES:
            parent = self._section_stack[-1]["id"] if self._section_stack else None
            sec = {"id": a.get("id") or f"sec{len(self.sections) + 1}", "title": "", "parent": parent, "top": bool(classes & _OUTLINE_CLASSES) or parent is None}
            self.sections.append(sec)
            self._section_stack.append(sec)
            role = "section"
        elif tag == "div" and "ltx_abstract" in classes:
            sec = {"id": ABSTRACT_ID, "title": "Abstract", "parent": None, "top": True}
            self.sections.append(sec)
            self._section_stack.append(sec)
            role = "section"
        elif re.fullmatch(r"h[1-6]", tag) and "ltx_title" in classes:
            if "ltx_title_document" in classes:
                self._doc_title = True
                role = "doc_title"
            elif self._section_stack and not self._section_stack[-1]["title"] and self._heading is None:
                self._heading, self._heading_for = [], self._section_stack[-1]
                role = "heading"
        elif tag == "figure":
            self._figures.append(a.get("id") or "")
            role = "figure"
        elif (tag == "div" and "ltx_para" in classes) or (tag == "p" and "ltx_p" in classes and not self._buffers and self._section_stack):
            self._open(a.get("id") or f"p{len(self.paragraphs) + 1}")
            role = "para"
        elif tag == "figcaption" and self._section_stack:
            fig = next((f for f in reversed(self._figures) if f), "")
            self._open(fig or f"fig{len(self.paragraphs) + 1}")
            role = "para"
        self._stack.append((tag, role))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "math":
            self.handle_starttag(tag, attrs)
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        if tag in _VOID or not any(t == tag for t, _ in self._stack):
            return  # stray end tag
        while self._stack:
            open_tag, role = self._stack.pop()
            self._close(role)
            if open_tag == tag:
                break

    def handle_data(self, data: str) -> None:
        if self._skip:
            return
        if self._doc_title:
            self.title_parts.append(data)
        elif self._heading is not None:
            self._heading.append(data)
        else:
            self._text(data)

    def _text(self, data: str) -> None:
        if self._buffers:
            self._buffers[-1][2].append(data)

    def _open(self, pid: str) -> None:
        self.paragraphs.append(None)
        self._buffers.append((len(self.paragraphs) - 1, pid, []))

    def _close(self, role: str | None) -> None:
        if role == "skip":
            self._skip -= 1
        elif role == "section":
            self._section_stack.pop()
        elif role == "heading":
            self._heading_for["title"] = _clean("".join(self._heading or []))
            self._heading = self._heading_for = None
        elif role == "doc_title":
            self._doc_title = False
        elif role == "figure":
            self._figures.pop()
        elif role == "para":
            slot, pid, parts = self._buffers.pop()
            text = _clean("".join(parts))
            if text and self._section_stack:
                sid = self._section_stack[-1]["id"]
                if sid == ABSTRACT_ID:  # same id as the abstract-only fallback, so quotes from either check the same way
                    n = sum(1 for p in self.paragraphs if p and p["s"] == ABSTRACT_ID)
                    pid = ABSTRACT_ID if n == 0 else f"{ABSTRACT_ID}.{n + 1}"
                self.paragraphs[slot] = {"p": pid, "s": sid, "text": text}


def _clean(text: str) -> str:
    return " ".join(text.split())


def parse_html(html: str, pid: str) -> dict:
    """Paper text as sections and numbered paragraphs, in reading order."""
    parser = _Parser()
    parser.feed(html)
    parser.close()
    paragraphs = [p for p in parser.paragraphs if p]
    used = {p["s"] for p in paragraphs}
    sections = [{k: s[k] for k in ("id", "title", "parent", "top")} for s in parser.sections if s["id"] in used or any(_ancestor(t, s["id"], parser.sections) for t in used)]
    return {"id": pid, "status": "html", "title": _clean("".join(parser.title_parts)), "sections": sections, "paragraphs": paragraphs}


def _ancestor(section_id: str, candidate: str, sections: list[dict]) -> bool:
    parents = {s["id"]: s["parent"] for s in sections}
    current = parents.get(section_id)
    while current:
        if current == candidate:
            return True
        current = parents.get(current)
    return False


def abstract_only(paper: dict, reason: str) -> dict:
    """The fallback when no HTML exists: the arXiv abstract, as one paragraph that quotes can still be checked against."""
    text = _clean(paper.get("abstract", ""))
    return {
        "id": paper["id"],
        "status": "abstract_only",
        "reason": reason,
        "title": paper.get("title", ""),
        "sections": [{"id": ABSTRACT_ID, "title": "Abstract", "parent": None, "top": True}],
        "paragraphs": [{"p": ABSTRACT_ID, "s": ABSTRACT_ID, "text": text}] if text else [],
    }


async def fetch(client: httpx.AsyncClient, paper: dict, *, deadline: float, today: date | None = None) -> dict:
    """Fetch and parse one paper's HTML; raises ``FulltextError`` when there is none or it cannot be read in time."""
    import httpx

    remaining = deadline - time.monotonic()
    if remaining < 1.0:
        raise FulltextError("time budget")
    url = HTML_ENDPOINT + paper["id"]
    try:
        async with client.stream("GET", url, timeout=min(REQUEST_TIMEOUT, remaining)) as resp:
            if resp.status_code == 404:
                raise FulltextError("no HTML version")
            if resp.status_code != 200:
                raise FulltextError(f"HTTP {resp.status_code}")
            chunks, size = [], 0
            async for chunk in resp.aiter_bytes():
                size += len(chunk)
                if size > MAX_HTML_BYTES:
                    raise FulltextError("page too large")
                chunks.append(chunk)
            final_url = str(resp.url)
    except (httpx.TimeoutException, httpx.TransportError) as exc:
        raise FulltextError(type(exc).__name__) from exc
    html = b"".join(chunks).decode("utf-8", errors="replace")
    if "ltx_page_main" not in html and "ltx_document" not in html:
        raise FulltextError("not a LaTeXML page")
    parsed = parse_html(html, paper["id"])
    if len([p for p in parsed["paragraphs"] if p["s"] != ABSTRACT_ID]) < 3:
        raise FulltextError("HTML has almost no body text")  # failed conversions render a stub page
    parsed["url"] = final_url
    parsed["fetched_on"] = (today or date.today()).isoformat()
    return parsed


def outline(doc: dict) -> str:
    """One line per paper for the batch result: top-level sections with paragraph counts."""
    counts: dict[str, int] = {}
    tops = {s["id"]: s for s in doc["sections"] if s["top"]}
    parents = {s["id"]: s["parent"] for s in doc["sections"]}
    for para in doc["paragraphs"]:
        sid = para["s"]
        while sid not in tops and parents.get(sid):
            sid = parents[sid]
        counts[sid] = counts.get(sid, 0) + 1
    parts = [f"{sid} {tops[sid]['title'] or sid} ({counts[sid]}¶)" for sid in tops if counts.get(sid)]
    return "; ".join(parts)


def section_paragraphs(doc: dict, section: str) -> list[dict]:
    """Paragraphs of a section and its subsections. ``section`` is an id (``S4``, ``S4.SS2``) or a title fragment."""
    ids = {s["id"] for s in doc["sections"]}
    wanted = section.strip()
    if wanted not in ids:
        low = wanted.lower()
        match = next((s["id"] for s in doc["sections"] if low and low in s["title"].lower()), None)
        if match is None:
            return []
        wanted = match
    keep = {wanted} | {s["id"] for s in doc["sections"] if _ancestor(s["id"], wanted, doc["sections"])}
    return [p for p in doc["paragraphs"] if p["s"] in keep]


def section_title(doc: dict, section_id: str) -> str:
    return next((s["title"] for s in doc["sections"] if s["id"] == section_id), section_id)


def normalise_for_match(text: str) -> str:
    """Words only: case, punctuation, citations, LaTeX commands and line breaks do not count against a quote."""
    text = unicodedata.normalize("NFKC", text)
    text = _CITATION.sub(" ", text)
    text = _LATEX_COMMAND.sub(" ", text)
    return " " + " ".join(_WORD.findall(text.lower())) + " "


def find_quote(doc: dict, quote: str, para: str | None) -> tuple[dict | None, str | None]:
    """``(paragraph, problem)``. The stated paragraph is tried first; a quote found elsewhere in the paper still counts."""
    words = normalise_for_match(quote)
    if len(quote) > MAX_QUOTE_CHARS:
        return None, f"quote is longer than {MAX_QUOTE_CHARS} characters; quote one sentence or less"
    if len(words.split()) < MIN_QUOTE_WORDS:
        return None, f"quote has fewer than {MIN_QUOTE_WORDS} words; quote a full clause"
    paragraphs = doc["paragraphs"]
    stated = [p for p in paragraphs if p["p"] == para]
    for candidate in stated + [p for p in paragraphs if p["p"] != para]:
        if words in normalise_for_match(candidate["text"]):
            return candidate, None
    where = f"paragraph {para}" if stated else "this paper"
    return None, f"quote not found word for word in {where}; copy it exactly from read_paper output (no paraphrase, no ellipsis, one paragraph only)"
