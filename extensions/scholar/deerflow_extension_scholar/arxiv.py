"""Async arXiv API client.

Query building and Atom parsing are ported from DeerFlow's upstream
``systematic-literature-review/scripts/arxiv_search.py`` (MIT). What changed:
it runs inside the Gateway process instead of a shell, so it needs no
``allow_host_bash``, and every retry fits inside one time budget because the
host cancels a plugin tool call after 30 seconds.
"""

from __future__ import annotations

import asyncio
import time
import xml.etree.ElementTree as ET

import httpx

ARXIV_ENDPOINT = "https://export.arxiv.org/api/query"
MAX_RESULTS_UPPER_BOUND = 100
RETRY_STATUS = frozenset({429, 500, 502, 503, 504})
REQUEST_TIMEOUT = 15.0
USER_AGENT = "deerflow-extension-scholar/0.1 (+https://github.com/unumbrela/deerflow-citeguard)"
NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


class ArxivError(RuntimeError):
    """A failure the model should report to the user, not work around."""


def build_search_query(query: str, category: str | None, start_date: str | None, end_date: str | None, match: str = "phrase") -> str:
    """arXiv's ``search_query`` grammar: ``all:``/``cat:``/``submittedDate:`` joined by AND.

    Multi-word topics are quoted as a phrase; ``all_terms`` instead requires every
    word, in any order. Without either, Lucene would OR the words together.
    """
    words = query.split()
    if match == "all_terms" and len(words) > 1:
        parts = ["(" + " AND ".join(f"all:{w}" for w in words) + ")"]
    elif len(words) > 1:
        parts = [f'all:"{" ".join(words)}"']
    else:
        parts = [f"all:{query.strip()}"]
    if category:
        parts.append(f"cat:{category}")
    if start_date or end_date:
        lo = (start_date or "1991-01-01").replace("-", "") + "0000"
        hi = (end_date or "2999-12-31").replace("-", "") + "2359"
        parts.append(f"submittedDate:[{lo} TO {hi}]")
    return " AND ".join(parts)


def normalise_id(raw_id: str) -> str:
    """``http://arxiv.org/abs/1706.03762v5`` -> ``1706.03762``; legacy ``hep-th/9901001v1`` keeps its archive."""
    tail = raw_id.split("/abs/", 1)[1] if "/abs/" in raw_id else raw_id.rsplit("/", 1)[-1]
    base, sep, suffix = tail.rpartition("v")
    return base if sep and suffix.isdigit() else tail


def _parse_entry(entry: ET.Element) -> dict:
    def text(path: str) -> str:
        node = entry.find(path, NS)
        return " ".join((node.text or "").split()) if node is not None else ""

    raw_id = text("atom:id")
    authors = [" ".join((a.findtext("atom:name", default="", namespaces=NS) or "").split()) for a in entry.findall("atom:author", NS)]
    categories = [c.get("term", "") for c in entry.findall("atom:category", NS) if c.get("term")]
    primary = entry.find("arxiv:primary_category", NS)
    pdf_url, abs_url = "", raw_id
    for link in entry.findall("atom:link", NS):
        if link.get("title") == "pdf":
            pdf_url = link.get("href", "")
        elif link.get("rel") == "alternate":
            abs_url = link.get("href", abs_url)
    return {
        "id": normalise_id(raw_id),
        "title": text("atom:title"),
        "authors": [a for a in authors if a],
        "abstract": text("atom:summary"),
        "published": text("atom:published").split("T", 1)[0],
        "updated": text("atom:updated").split("T", 1)[0],
        "categories": categories,
        "primary_category": primary.get("term", "") if primary is not None else (categories[0] if categories else ""),
        "pdf_url": pdf_url,
        "abs_url": abs_url,
    }


def parse_feed(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    return [_parse_entry(e) for e in root.findall("atom:entry", NS)]


def _retry_after(resp: httpx.Response, attempt: int) -> float:
    try:
        return max(float(resp.headers.get("Retry-After", "")), 1.0)
    except ValueError:
        return 3.0 * 2**attempt


async def _get(client: httpx.AsyncClient, params: dict, deadline: float) -> list[dict]:
    """One arXiv API request, retried on rate limits and transient errors until ``deadline`` (``time.monotonic()``)."""
    attempt = 0
    while True:
        remaining = deadline - time.monotonic()
        if remaining < 1.0:
            raise ArxivError("arXiv did not answer within the time budget; try again in a minute")
        try:
            resp = await client.get(ARXIV_ENDPOINT, params=params, timeout=min(REQUEST_TIMEOUT, remaining))
        except (httpx.TimeoutException, httpx.TransportError) as exc:
            reason, wait = type(exc).__name__, 3.0 * 2**attempt
        else:
            if resp.status_code == 200:
                return parse_feed(resp.text)
            if resp.status_code not in RETRY_STATUS:
                raise ArxivError(f"arXiv returned HTTP {resp.status_code}")
            reason, wait = f"HTTP {resp.status_code}", _retry_after(resp, attempt)
        if time.monotonic() + wait > deadline - 1.0:
            raise ArxivError(f"arXiv unavailable ({reason}); try again in a minute")
        await asyncio.sleep(wait)
        attempt += 1


async def fetch(
    client: httpx.AsyncClient,
    *,
    query: str,
    max_results: int,
    category: str | None,
    start_date: str | None,
    end_date: str | None,
    match: str,
    deadline: float,
) -> list[dict]:
    """One relevance-ranked arXiv query."""
    params = {
        "search_query": build_search_query(query, category, start_date, end_date, match),
        "start": 0,
        "max_results": min(max(max_results, 1), MAX_RESULTS_UPPER_BOUND),
        "sortBy": "relevance",
        "sortOrder": "descending",
    }
    return await _get(client, params, deadline)


async def fetch_ids(client: httpx.AsyncClient, ids: list[str], *, deadline: float) -> list[dict]:
    """Metadata for known arXiv ids (references found by citation expansion)."""
    if not ids:
        return []
    return await _get(client, {"id_list": ",".join(ids), "start": 0, "max_results": len(ids)}, deadline)
