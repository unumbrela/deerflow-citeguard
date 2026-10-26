"""Offline tests for build_coverage_set.py (sources are synthetic, built in memory)."""

import io
import sys
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import build_coverage_set as b  # noqa: E402


def tar_with(files: dict[str, str]) -> bytes:
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tf:
        for name, text in files.items():
            data = text.encode()
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tf.addfile(info, io.BytesIO(data))
    return buf.getvalue()


class TopicTest(unittest.TestCase):
    def test_prefix_and_suffix_forms(self):
        self.assertEqual(b.topic_from_title("A Comprehensive Survey on Retrieval-Augmented Generation"), "Retrieval-Augmented Generation")
        self.assertEqual(b.topic_from_title("Agentic Memory: A Survey"), "Agentic Memory")
        self.assertEqual(b.topic_from_title("Survey of Hallucination in LLMs."), "Hallucination in LLMs")


class ReferenceIdsTest(unittest.TestCase):
    def test_ids_from_bbl_and_bib_deduplicated_without_self(self):
        src = tar_with({"main.tex": "arXiv:9999.99999 in body is ignored", "main.bbl": "\\bibitem{a} arXiv:2401.00001v2\n\\bibitem{b} 2401.00001 and 2502.12345", "refs.bib": "@misc{c, eprint={2309.00007}} @misc{self, eprint={2507.00001}}"})
        with tempfile.TemporaryDirectory() as d, mock.patch.object(b, "CACHE", Path(d)):
            (Path(d) / "src").mkdir()
            (Path(d) / "src" / "2507.00001").write_bytes(src)
            self.assertEqual(b.reference_ids("2507.00001"), ["2401.00001", "2502.12345", "2309.00007"])

    def test_pdf_only_submission_returns_none(self):
        with tempfile.TemporaryDirectory() as d, mock.patch.object(b, "CACHE", Path(d)):
            (Path(d) / "src").mkdir()
            (Path(d) / "src" / "2507.00002").write_bytes(b"%PDF-1.5 ...")
            self.assertIsNone(b.reference_ids("2507.00002"))


class TasksTest(unittest.TestCase):
    def test_window_ends_the_day_before_the_survey(self):
        self.assertEqual(b.window("2025-10-14"), (b.date(2023, 10, 14), b.date(2025, 10, 13)))
        self.assertEqual(b.window("2024-02-29"), (b.date(2022, 2, 28), b.date(2024, 2, 28)))

    def test_split_puts_inspected_surveys_in_dev_and_is_order_independent(self):
        topics = [{"id": f"c{i:02d}", "survey": f"2601.{i:05d}"} for i in range(1, 11)]
        dev, held = b.split(topics, dev_size=4, inspected={"2601.00007"})
        self.assertEqual(len(dev), 4)
        self.assertIn("c07", [t["id"] for t in dev])
        self.assertEqual({t["id"] for t in dev} | {t["id"] for t in held}, {t["id"] for t in topics})
        self.assertEqual(b.split(topics[::-1], dev_size=4, inspected={"2601.00007"})[0][::-1], dev)

    def test_task_prompt_carries_the_window(self):
        t = {"id": "c01", "topic": "X", "category": "cs.CL", "start_date": "2023-10-14", "end_date": "2025-10-13"}
        self.assertIn("published between 2023-10-14 and 2025-10-13, category cs.CL", b.task(t)["prompt"])


if __name__ == "__main__":
    unittest.main()


class CoverageScoreTest(unittest.TestCase):
    def test_precision_and_recall_bounded_by_ten(self):
        import coverage as cov

        ids = cov.cited_ids("arXiv:2401.00001 https://arxiv.org/abs/2401.00002 arXiv:2401.00001 arXiv:2401.00003")
        self.assertEqual(ids, ["2401.00001", "2401.00002", "2401.00003"])
        big = {f"2401.{i:05d}" for i in range(1, 40)}
        self.assertEqual(cov.score(ids, big), {"cited": 3, "hits": 3, "precision": 1.0, "recall": 0.3})
        self.assertEqual(cov.score(ids, {"2401.00002", "2509.11111"})["recall"], 0.5)
        self.assertEqual(cov.score([], big)["precision"], 0.0)
