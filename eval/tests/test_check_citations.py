"""Offline tests for check_citations.py reference parsing."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_citations as cc  # noqa: E402


class ParseReferencesTest(unittest.TestCase):
    def test_apa_same_year_suffix(self):
        text = "Chen, S., & Wu, M. (2025a). Leveraging depth and language. arXiv. https://arxiv.org/abs/2506.09881"
        [ref] = cc.parse_references(text)
        self.assertEqual((ref["parsed"], ref["first_author"], ref["year"], ref["title"]), (True, "chen", "2025", "Leveraging depth and language"))


if __name__ == "__main__":
    unittest.main()
