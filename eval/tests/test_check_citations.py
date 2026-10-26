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

    def test_apa_full_date_and_italic_title(self):
        text = "Balesni, M., & Evans, O. (2024, November 25). *Lessons from studying two-hop latent reasoning*. arXiv preprint arXiv:2411.16353v4."
        [ref] = cc.parse_references(text)
        self.assertEqual((ref["parsed"], ref["first_author"], ref["year"], ref["title"]), (True, "balesni", "2024", "Lessons from studying two-hop latent reasoning"))

    def test_bracketed_arxiv_id_after_title(self):
        text = "Ding, Y., & Hou, Y. (2024). *Inductive generative recommendation via retrieval-based speculation* [arXiv:2410.02939]. https://arxiv.org/abs/2410.02939v2"
        [ref] = cc.parse_references(text)
        self.assertEqual((ref["parsed"], ref["first_author"], ref["title"]), (True, "ding", "Inductive generative recommendation via retrieval-based speculation"))


if __name__ == "__main__":
    unittest.main()
