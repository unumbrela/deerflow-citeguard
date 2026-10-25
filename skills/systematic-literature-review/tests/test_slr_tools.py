"""Offline tests for slr_tools.py (arXiv is mocked)."""

import argparse
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import slr_tools  # noqa: E402


def paper(i: int, primary: str = "cs.CL") -> dict:
    return {
        "id": f"2501.{i:05d}",
        "title": f"Benchmarking Agents Part {i}",
        "authors": [f"Alice Smith{i}", "Bob Jones"],
        "abstract": "x" * 800,
        "published": "2025-01-02",
        "updated": "2025-01-02",
        "categories": [primary],
        "primary_category": primary,
        "pdf_url": "",
        "abs_url": "",
    }


def args(out_dir: str, **kw) -> argparse.Namespace:
    base = dict(query="agent", max_results=10, category=None, include_cross_lists=False, years=None, start_date=None, end_date=None, batch_size=5, out_dir=out_dir)
    base.update(kw)
    return argparse.Namespace(**base)


class WindowTest(unittest.TestCase):
    def test_years_back(self):
        self.assertEqual(slr_tools.window_start(date(2026, 10, 25), 2), date(2024, 10, 25))

    def test_leap_day(self):
        self.assertEqual(slr_tools.window_start(date(2028, 2, 29), 1), date(2027, 2, 28))


class SearchTest(unittest.TestCase):
    def test_writes_batches_and_compact_index(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(slr_tools.arxiv_search, "search", return_value=[paper(i) for i in range(10)]) as m:
            res = slr_tools.run_search(args(d), today=date(2026, 10, 25))
            self.assertEqual(res["count"], 10)
            self.assertEqual(len(res["batch_files"]), 2)
            self.assertEqual(len(json.loads(Path(res["batch_files"][0]).read_text())), 5)
            self.assertNotIn("abstract", json.dumps(res["index"]))
            self.assertLess(len(json.dumps(res)), 12000)
            self.assertEqual(m.call_args.kwargs["start_date"], None)

    def test_years_translates_to_start_date(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(slr_tools.arxiv_search, "search", return_value=[]) as m:
            slr_tools.run_search(args(d, years=2), today=date(2026, 10, 25))
            self.assertEqual(m.call_args.kwargs["start_date"], "2024-10-25")

    def test_index_for_max_papers_stays_under_externalize_threshold(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(slr_tools.arxiv_search, "search", return_value=[paper(i) for i in range(50)]):
            res = slr_tools.run_search(args(d, max_results=50))
            self.assertLess(len(json.dumps(res, separators=(",", ":"))), 12000)

    def test_primary_category_filter_fetches_max(self):
        pool = [paper(i, "cs.CL" if i % 2 else "cs.AI") for i in range(20)]
        with tempfile.TemporaryDirectory() as d, mock.patch.object(slr_tools.arxiv_search, "search", return_value=pool) as m:
            res = slr_tools.run_search(args(d, category="cs.CL", max_results=8))
            self.assertEqual(m.call_args.kwargs["max_results"], 50)
            self.assertEqual(res["count"], 8)
            self.assertTrue(all(p["cat"] == "cs.CL" for p in res["index"]))

    def test_stale_batches_removed(self):
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "batch_9.json").write_text("[]")
            with mock.patch.object(slr_tools.arxiv_search, "search", return_value=[paper(1)]):
                slr_tools.run_search(args(d))
            self.assertFalse((Path(d) / "batch_9.json").exists())

    def test_retries_on_429_then_succeeds(self):
        calls = {"n": 0}

        def flaky(**kw):
            calls["n"] += 1
            if calls["n"] < 3:
                raise RuntimeError("HTTP 429")
            return [paper(1)]

        with mock.patch.object(slr_tools.arxiv_search, "search", side_effect=flaky), mock.patch.object(slr_tools.time, "sleep"):
            self.assertEqual(len(slr_tools._search_with_retry(query="x")), 1)
        self.assertEqual(calls["n"], 3)

    def test_non_transient_error_not_retried(self):
        with mock.patch.object(slr_tools.arxiv_search, "search", side_effect=RuntimeError("HTTP 400")) as m, mock.patch.object(slr_tools.time, "sleep"):
            with self.assertRaises(RuntimeError):
                slr_tools._search_with_retry(query="x")
            self.assertEqual(m.call_count, 1)


class WidenQueryTest(unittest.TestCase):
    def test_widens_to_all_terms_keeping_category_and_window(self):
        calls = []

        def fake(**kw):
            calls.append(kw)
            return [paper(i) for i in range(2)] if kw["match"] == "phrase" else [paper(i) for i in range(8)]

        with tempfile.TemporaryDirectory() as d, mock.patch.object(slr_tools.arxiv_search, "search", side_effect=fake), mock.patch.object(slr_tools.time, "sleep"):
            res = slr_tools.run_search(args(d, query="robot manipulation models", category="cs.CL", years=2), today=date(2026, 10, 25))
        self.assertEqual([c["match"] for c in calls], ["phrase", "all_terms"])
        self.assertTrue(all(c["category"] == "cs.CL" and c["start_date"] == "2024-10-25" for c in calls))
        self.assertEqual(res["match"], "phrase+all_terms")
        self.assertEqual(res["count"], 8)
        self.assertEqual(len({p["id"] for p in res["index"]}), 8)  # deduplicated

    def test_no_widening_when_phrase_is_enough(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(slr_tools.arxiv_search, "search", return_value=[paper(i) for i in range(10)]) as m:
            res = slr_tools.run_search(args(d, query="agent evaluation"))
        self.assertEqual(m.call_count, 1)
        self.assertEqual(res["match"], "phrase")

    def test_single_word_query_never_widens(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(slr_tools.arxiv_search, "search", return_value=[paper(1)]) as m:
            slr_tools.run_search(args(d, query="agents"))
        self.assertEqual(m.call_count, 1)


class QueryBuilderTest(unittest.TestCase):
    def test_phrase_vs_all_terms(self):
        sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
        import arxiv_search

        self.assertIn('all:"a b"', arxiv_search._build_search_query("a b", None, None, None))
        q = arxiv_search._build_search_query("a b", "cs.CL", None, None, "all_terms")
        self.assertEqual(q, "(all:a AND all:b) AND cat:cs.CL")


class CliTest(unittest.TestCase):
    def test_out_dir_and_papers_are_required(self):
        parser = slr_tools._build_parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(["search", "agent"])
        with self.assertRaises(SystemExit):
            parser.parse_args(["verify", "report.md"])


class VerifyTest(unittest.TestCase):
    META = {"papers": [paper(1), paper(2)]}

    def test_all_real_ids_pass(self):
        report = "Smith1, A., & Jones, B. (2025). Benchmarking Agents Part 1. arXiv:2501.00001\nSmith2, A. (2025). Benchmarking Agents Part 2. https://arxiv.org/abs/2501.00002"
        res = slr_tools.run_verify(report, self.META)
        self.assertTrue(res["ok"])
        self.assertEqual(res["cited"], 2)
        self.assertEqual(res["warnings"], [])

    def test_fabricated_id_fails(self):
        res = slr_tools.run_verify("Doe, J. (2025). Invented. arXiv:2506.45678", self.META)
        self.assertFalse(res["ok"])
        self.assertEqual(res["unknown_ids"], ["2506.45678"])

    def test_rewritten_title_and_wrong_author_warn(self):
        res = slr_tools.run_verify("Zhou, S. (2025). A Different Title. arXiv:2501.00001", self.META)
        self.assertTrue(res["ok"])
        self.assertEqual(len(res["warnings"]), 2)

    def test_uncited_papers_reported(self):
        res = slr_tools.run_verify("Smith1 (2025). Benchmarking Agents Part 1. arXiv:2501.00001", self.META)
        self.assertEqual(res["not_cited"], ["2501.00002"])

    def test_duplicate_citations_counted_once(self):
        res = slr_tools.run_verify("arXiv:2501.00001 and again arxiv.org/abs/2501.00001", self.META)
        self.assertEqual(res["cited"], 1)


if __name__ == "__main__":
    unittest.main()
