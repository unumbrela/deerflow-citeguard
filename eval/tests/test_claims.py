"""Offline tests for claims.py extraction and agreement (no model or arXiv calls)."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import claims  # noqa: E402

REPORT = """# Review

## Methodology

We searched arXiv (Smith et al., 2025) for papers.

## Themes

Smith et al. (2025) show that agents fail on long tasks. Later work disagrees (Lee & Park, 2026; Smith et al., 2025).
This sentence cites nobody. Ghost et al. (2024) claim something unreferenced.

| Table | (Smith et al., 2025) |

## Per-Paper Annotations

### Smith et al. (2025)

- **Key findings**: agents fail on tasks longer than ten steps
- short

## References

Smith, A., & Jones, B. (2025). Long Tasks Break Agents. *arXiv preprint arXiv:2501.00001*.
Lee, C., & Park, D. (2026). Agents Are Fine. *arXiv preprint arXiv:2601.00002*.
"""


class ExtractTest(unittest.TestCase):
    def setUp(self):
        self.claims, self.stats = claims.extract_claims(REPORT)

    def test_narrative_and_parenthetical_citations_resolve_to_ids(self):
        texts = {c["text"]: c["ids"] for c in self.claims}
        self.assertEqual(texts["Smith et al. (2025) show that agents fail on long tasks."], ["2501.00001"])
        self.assertEqual(texts["Later work disagrees (Lee & Park, 2026; Smith et al., 2025)."], ["2601.00002", "2501.00001"])

    def test_methodology_references_tables_and_uncited_sentences_skipped(self):
        joined = " ".join(c["text"] for c in self.claims)
        self.assertNotIn("We searched arXiv", joined)
        self.assertNotIn("cites nobody", joined)
        self.assertNotIn("Table", joined)
        self.assertNotIn("Agents Are Fine", joined)

    def test_unreferenced_citation_is_counted_not_guessed(self):
        self.assertEqual(self.stats["unmatched"], 1)
        self.assertNotIn("Ghost", " ".join(c["text"] for c in self.claims))

    def test_annotation_lines_inherit_the_heading_paper(self):
        ann = [c for c in self.claims if c["kind"] == "annotation"]
        self.assertEqual([c["ids"] for c in ann], [["2501.00001"]])  # "short" has under 5 words
        self.assertIn("ten steps", ann[0]["text"])

    def test_ambiguous_key_is_counted(self):
        text = REPORT.replace("Lee, C., & Park, D. (2026). Agents Are Fine. *arXiv preprint arXiv:2601.00002*.", "Smith, E. (2025). Another Smith. *arXiv preprint arXiv:2601.00002*.")
        _, stats = claims.extract_claims(text)
        self.assertGreater(stats["ambiguous"], 0)

    def test_sentence_split_keeps_et_al(self):
        self.assertEqual(claims.split_sentences("Smith et al. (2025) did X. Then Y happened."), ["Smith et al. (2025) did X.", "Then Y happened."])


class KappaTest(unittest.TestCase):
    def test_perfect_and_chance(self):
        self.assertEqual(claims.cohen_kappa(["a", "b", "a"], ["a", "b", "a"]), 1.0)
        self.assertAlmostEqual(claims.cohen_kappa(["a", "a", "b", "b"], ["a", "b", "a", "b"]), 0.0)


if __name__ == "__main__":
    unittest.main()


class ReferenceLineTest(unittest.TestCase):
    TEXT = """## Annotated Bibliography

### 1. Long Tasks Break Agents

Smith, A., & Jones, B. (2025). Long Tasks Break Agents. *arXiv preprint arXiv:2501.00001*. https://arxiv.org/abs/2501.00001v2

**Summary:** The authors show that agents fail on tasks longer than ten steps.

### 2. Something Else

Lee, C. (2026). Something Else. *arXiv preprint arXiv:2601.00002*. https://arxiv.org/abs/2601.00002

- Agents are mostly fine in short horizons according to this work.

## References

Smith, A., & Jones, B. (2025). Long Tasks Break Agents. *arXiv preprint arXiv:2501.00001*.
Lee, C. (2026). Something Else. *arXiv preprint arXiv:2601.00002*.
"""

    def test_reference_lines_are_not_claims_but_name_the_block(self):
        found, _ = claims.extract_claims(self.TEXT)
        self.assertEqual([(c["ids"], c["kind"]) for c in found], [(["2501.00001"], "annotation"), (["2601.00002"], "annotation")])
        self.assertTrue(all("preprint" not in c["text"] for c in found))

    def test_bare_citation_fragment_has_no_content(self):
        self.assertEqual(claims._content_words("arXiv preprint arXiv:2602.23574. https://arxiv.org/abs/2602.23574v2"), 0)
        self.assertGreater(claims._content_words("Smith et al. (2025) show agents fail on long tasks."), 3)


class PlaceholderTest(unittest.TestCase):
    def test_template_placeholder_is_not_a_claim(self):
        text = "## Per-Paper Annotations\n\n### Smith et al. (2025)\n\n- **Limitations**: not stated in abstract\n- **Findings**: agents fail on tasks longer than ten steps\n\n## References\n\nSmith, A. (2025). Long Tasks. *arXiv preprint arXiv:2501.00001*.\n"
        found, _ = claims.extract_claims(text)
        self.assertEqual([c["text"] for c in found], ["Findings: agents fail on tasks longer than ten steps"])
