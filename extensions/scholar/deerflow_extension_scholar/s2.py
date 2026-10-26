"""Semantic Scholar client: the arXiv references of a set of arXiv papers.

Only backward references are fetched. Forward citations ("cited by") would reach
papers written after the user's window, including any survey of the topic, and
today's citation counts carry hindsight; neither is used.

Unauthenticated requests share one rate limit across all callers, so 429 is
normal: requests are retried until the deadline, and the caller treats a
failure as "no expansion", never as a failed search. An API key, when the
deployment configures one, raises the limit.
"""

from __future__ import annotations

import asyncio
import time

import httpx

BATCH_ENDPOINT = "https://api.semanticscholar.org/graph/v1/paper/batch"
MAX_IDS = 500  # the batch endpoint's limit
RETRY_STATUS = frozenset({429, 500, 502, 503, 504})
REQUEST_TIMEOUT = 12.0


class S2Error(RuntimeError):
    """Expansion is unavailable; the search continues without it."""


def _arxiv_refs(entry: dict | None) -> list[str] | None:
    if not entry:
        return None
    out: list[str] = []
    for ref in entry.get("references") or []:
        pid = (ref.get("externalIds") or {}).get("ArXiv")
        if pid and pid not in out:
            out.append(pid)
    return out


async def references(client: httpx.AsyncClient, ids: list[str], *, deadline: float, api_key: str | None = None) -> dict[str, list[str] | None]:
    """arXiv id -> arXiv ids it cites (None when Semantic Scholar does not know the paper)."""
    headers = {"x-api-key": api_key} if api_key else {}
    out: dict[str, list[str] | None] = {}
    for start in range(0, len(ids), MAX_IDS):
        chunk = ids[start : start + MAX_IDS]
        attempt = 0
        while True:
            remaining = deadline - time.monotonic()
            if remaining < 1.0:
                raise S2Error("Semantic Scholar did not answer within the time budget")
            try:
                resp = await client.post(BATCH_ENDPOINT, params={"fields": "references.externalIds"}, json={"ids": [f"arXiv:{i}" for i in chunk]}, headers=headers, timeout=min(REQUEST_TIMEOUT, remaining))
            except (httpx.TimeoutException, httpx.TransportError) as exc:
                reason = type(exc).__name__
            else:
                if resp.status_code == 200:
                    out.update(zip(chunk, (_arxiv_refs(e) for e in resp.json())))
                    break
                if resp.status_code not in RETRY_STATUS:
                    raise S2Error(f"Semantic Scholar returned HTTP {resp.status_code}")
                reason = f"HTTP {resp.status_code}"
            wait = 1.5 * 2**attempt
            if time.monotonic() + wait > deadline - 1.0:
                raise S2Error(f"Semantic Scholar unavailable ({reason})")
            await asyncio.sleep(wait)
            attempt += 1
    return out
