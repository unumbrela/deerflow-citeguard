"""Full-text evidence for the claim judge (v3): the passages of a cited paper that best match a claim.

Judge v2 saw only the title and abstract, so a claim about a paper's experiments was "unsupported" even when
the paper says it. v3 adds up to K passages from the paper's arXiv HTML, picked by BM25 overlap with the
sentence. The same retrieval runs for every arm: v5 reports carry quotes of their own, but the judge never
sees them, so it cannot favour the arm that wrote them.

Papers are parsed with the scholar plugin's own parser (``fulltext.py``, standard library only), loaded by
path so this stays a stdlib-only tool. Parsed papers are cached in eval/.fulltext_cache/<id>.json.
"""

from __future__ import annotations

import importlib.util
import json
import math
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CACHE = HERE / ".fulltext_cache"
PARSER = ROOT / "extensions" / "scholar" / "deerflow_extension_scholar" / "fulltext.py"
USER_AGENT = "deerflow-citeguard-eval/0.1 (+https://github.com/unumbrela/deerflow-citeguard)"
K = 3
PASSAGE_CHARS = 1200
MAX_HTML_BYTES = 6_000_000

_EVIDENCE_MARK = re.compile(r"\s*\[\s*E\d+(?:\s*[,;]\s*E\d+)*\s*\]")
_CITATION = re.compile(r"\([^()]*\b(?:19|20)\d{2}[a-z]?\b[^()]*\)|\[\d+(?:\s*[,–-]\s*\d+)*\]")
_TOKEN = re.compile(r"[a-z][a-z0-9\-]+|\d+(?:\.\d+)?%?")
STOPWORDS = set(
    "the a an and or of to in on for with by from as at is are was were be been being this that these those it its their "
    "they we our us which who whom whose what when where how than then also such can may might could would should will "
    "into over under between across about after before more most less least other others both each all any some no not "
    "only very via using use used based paper papers work works study studies approach approaches method methods "
    "propose proposes proposed show shows shown demonstrate demonstrates find finds found et al while whereas however "
    "further new novel results result".split()
)


def _load_parser():
    spec = importlib.util.spec_from_file_location("scholar_fulltext", PARSER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


fulltext = _load_parser()


def strip_markers(text: str) -> str:
    """Claim text as the judge sees it: v5's [E#] markers removed, so both arms look the same."""
    return _EVIDENCE_MARK.sub("", text)


def tokens(text: str) -> list[str]:
    return [t for t in _TOKEN.findall(_CITATION.sub(" ", text.lower())) if t not in STOPWORDS]


def passages(doc: dict, claim: str, k: int = K) -> list[dict]:
    """The k body paragraphs with the highest BM25 score for the claim; none when nothing overlaps."""
    paras = [p for p in doc.get("paragraphs", []) if p["s"] != fulltext.ABSTRACT_ID]
    if not paras:
        return []
    docs = [tokens(p["text"]) for p in paras]
    query = set(tokens(strip_markers(claim)))
    n, avg = len(docs), sum(map(len, docs)) / len(docs) or 1.0
    df = {t: sum(t in set(d) for d in docs) for t in query}
    scored = []
    for para, words in zip(paras, docs, strict=True):
        tf = {t: words.count(t) for t in query}
        score = sum(math.log(1 + (n - df[t] + 0.5) / (df[t] + 0.5)) * tf[t] * 2.2 / (tf[t] + 1.2 * (0.25 + 0.75 * len(words) / avg)) for t in query if tf[t])
        if score > 0:
            scored.append((score, para))
    scored.sort(key=lambda x: -x[0])
    return [{"p": para["p"], "text": para["text"][:PASSAGE_CHARS]} for _, para in scored[:k]]


def _fetch_html(pid: str) -> str | None:
    req = urllib.request.Request(f"https://arxiv.org/html/{pid}", headers={"User-Agent": USER_AGENT})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read(MAX_HTML_BYTES + 1).decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return None
        except Exception:  # noqa: BLE001 - retried, then treated as no HTML
            pass
        time.sleep(3 * 2**attempt)
    return None


def load_docs(ids: set[str], abstracts: dict[str, dict]) -> dict[str, dict]:
    """id -> parsed paper; papers without usable HTML get an abstract-only record (no passages)."""
    CACHE.mkdir(exist_ok=True)
    out = {}
    for pid in sorted(ids):
        path = CACHE / f"{pid}.json"
        if path.exists():
            out[pid] = json.loads(path.read_text(encoding="utf-8"))
            continue
        html = _fetch_html(pid)
        doc = None
        if html and len(html) <= MAX_HTML_BYTES and ("ltx_page_main" in html or "ltx_document" in html):
            doc = fulltext.parse_html(html, pid)
            if len([p for p in doc["paragraphs"] if p["s"] != fulltext.ABSTRACT_ID]) < 3:
                doc = None
        if doc is None:
            doc = fulltext.abstract_only({"id": pid, **abstracts.get(pid, {"title": "", "abstract": ""})}, "no usable HTML")
        path.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        out[pid] = doc
        time.sleep(1.0)
    return out


def passage_block(found: list[dict]) -> str:
    if not found:
        return "(no passage of the full text matches the sentence's words; judge from the abstract)"
    return "\n".join(f"[{p['p']}] {p['text']}" for p in found)
