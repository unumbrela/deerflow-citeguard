import json
from datetime import date

from helpers import paper

from deerflow_extension_scholar import core


def test_window_years_back():
    assert core.window_start(date(2026, 10, 25), 2) == date(2024, 10, 25)


def test_window_leap_day():
    assert core.window_start(date(2028, 2, 29), 1) == date(2027, 2, 28)


def test_start_date_overrides_years():
    assert core.resolve_window(date(2026, 10, 25), 2, "2020-01-01", None) == {"start": "2020-01-01", "end": None}
    assert core.resolve_window(date(2026, 10, 25), None, None, None) == {"start": None, "end": None}


class FakeFetch:
    def __init__(self, by_match):
        self.by_match = by_match
        self.calls = []

    async def __call__(self, match, n):
        self.calls.append((match, n))
        return self.by_match[match]


async def test_primary_category_filter_overfetches():
    fetch = FakeFetch({"phrase": [paper(i, "cs.CL" if i % 2 else "cs.AI") for i in range(20)]})
    papers, match = await core.select_papers(fetch, query="agent", max_results=8, category="cs.CL", include_cross_lists=False)
    assert fetch.calls == [("phrase", 50)]
    assert len(papers) == 8 and all(p["primary_category"] == "cs.CL" for p in papers)
    assert match == "phrase"


async def test_cross_lists_requested_keeps_everything():
    fetch = FakeFetch({"phrase": [paper(i, "cs.AI") for i in range(5)]})
    papers, _ = await core.select_papers(fetch, query="agent", max_results=5, category="cs.CL", include_cross_lists=True)
    assert fetch.calls == [("phrase", 5)]
    assert len(papers) == 5


async def test_widens_query_not_constraints_and_deduplicates():
    fetch = FakeFetch({"phrase": [paper(i) for i in range(2)], "all_terms": [paper(i) for i in range(8)]})
    papers, match = await core.select_papers(fetch, query="robot manipulation models", max_results=10, category="cs.CL", include_cross_lists=False)
    assert [c[0] for c in fetch.calls] == ["phrase", "all_terms"]
    assert match == "phrase+all_terms"
    assert [p["id"] for p in papers] == [paper(i)["id"] for i in range(8)]


async def test_no_widening_when_phrase_is_enough_or_single_word():
    enough = FakeFetch({"phrase": [paper(i) for i in range(10)]})
    await core.select_papers(enough, query="agent evaluation", max_results=10, category=None, include_cross_lists=False)
    single = FakeFetch({"phrase": [paper(1)]})
    await core.select_papers(single, query="agents", max_results=10, category=None, include_cross_lists=False)
    assert len(enough.calls) == 1 and len(single.calls) == 1


def test_batches_respect_char_budget_and_size():
    papers = [paper(i, abstract_chars=1900) for i in range(12)]
    batches = core.make_batches(papers)
    by_id = {p["id"]: p for p in papers}
    assert sum(len(b) for b in batches) == 12
    for ids in batches:
        assert 1 <= len(ids) <= core.BATCH_MAX_PAPERS
        assert len(json.dumps([core.batch_paper(by_id[i]) for i in ids], ensure_ascii=False)) <= core.BATCH_CHAR_BUDGET


def test_small_papers_fill_batches_of_five():
    assert [len(b) for b in core.make_batches([paper(i, abstract_chars=300) for i in range(10)])] == [5, 5]


def test_author_list_is_capped_and_total_recorded():
    item = core.batch_paper(paper(1, n_authors=300))
    assert len(item["authors"]) == core.MAX_AUTHORS and item["authors_total"] == 300


def test_oversized_single_paper_still_gets_its_own_batch():
    assert core.make_batches([paper(1, abstract_chars=20000), paper(2)]) == [["2501.00001"], ["2501.00002"]]


def test_index_for_50_papers_stays_under_externalize_threshold():
    index = core.compact_index([paper(i) for i in range(50)])
    assert "abstract" not in json.dumps(index)
    assert len(json.dumps(index, separators=(",", ":"))) < 12000


PAPERS = [paper(1), paper(2)]


def test_verify_all_real_ids_pass():
    report = "Smith1, A., & Jones0, B. (2025). Benchmarking Agents Part 1. arXiv:2501.00001\nSmith2, A. (2025). Benchmarking Agents Part 2. https://arxiv.org/abs/2501.00002"
    res = core.verify_report(report, PAPERS)
    assert res["ok"] and res["cited"] == 2 and res["warnings"] == []


def test_verify_fabricated_id_fails():
    res = core.verify_report("Doe, J. (2025). Invented. arXiv:2506.45678", PAPERS)
    assert not res["ok"] and res["unknown_ids"] == ["2506.45678"]


def test_verify_rewritten_title_and_wrong_author_warn():
    res = core.verify_report("Zhou, S. (2025). A Different Title. arXiv:2501.00001", PAPERS)
    assert res["ok"] and len(res["warnings"]) == 2


def test_verify_reports_uncited_and_counts_duplicates_once():
    res = core.verify_report("arXiv:2501.00001 and again arxiv.org/abs/2501.00001", PAPERS)
    assert res["cited"] == 1 and res["not_cited"] == ["2501.00002"]


def test_verify_sees_html_links():
    assert core.extract_ids("https://arxiv.org/html/2506.45678v1") == ["2506.45678"]
