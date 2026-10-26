"""Offline tests for coverage_compare.py's paired statistics."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import coverage_compare as cc  # noqa: E402


class WilcoxonTest(unittest.TestCase):
    def test_exact_values(self):
        # All 5 differences positive: 1 of 32 sign patterns is as extreme on each side.
        self.assertEqual(cc.wilcoxon_exact([0.1, 0.2, 0.3, 0.4, 0.5]), 2 / 32)
        self.assertEqual(cc.wilcoxon_exact([0.0, 0.0]), 1.0)
        self.assertEqual(cc.wilcoxon_exact([0.1, -0.1]), 1.0)


class BootstrapTest(unittest.TestCase):
    def test_brackets_the_mean(self):
        self.assertEqual(cc.bootstrap_ci([0.2] * 11, resamples=200), (0.2, 0.2))
        lo, hi = cc.bootstrap_ci([0.0, 0.1, 0.2, 0.3], resamples=2000)
        self.assertTrue(0.0 <= lo < 0.15 < hi <= 0.3)


if __name__ == "__main__":
    unittest.main()
