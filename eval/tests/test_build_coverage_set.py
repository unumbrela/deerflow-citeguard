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


if __name__ == "__main__":
    unittest.main()
