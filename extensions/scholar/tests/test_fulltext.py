import pytest
from helpers import latexml_page, paper

from deerflow_extension_scholar import fulltext

INTRO = [
    'Agents fail in long tasks <cite class="ltx_cite">(<a class="ltx_ref">Cobbe et al., 2021</a>)</cite>, and we measure why.',
    'Our method improves accuracy by <math alttext="12\\%" class="ltx_Math"><mn>12</mn></math> over the baseline<span class="ltx_note"><span class="ltx_note_content">Code is public.</span></span> on all benchmarks.',
]
PAGE = latexml_page(
    "Benchmarking Agents",
    {"Introduction": INTRO, "Experiments": ["We evaluate on five benchmarks with three random seeds each.", "The planner ablation removes most of the gain."], "Conclusion": ["Long horizons remain hard for every agent we tested."]},
).replace(
    '</section><section id="S3"',
    '<figure id="S2.F1" class="ltx_figure"><img src="x.png"/><figcaption class="ltx_caption"><span class="ltx_tag">Figure 1: </span>Accuracy against task length.</figcaption></figure></section><section id="S3"',
)


@pytest.fixture
def doc():
    return fulltext.parse_html(PAGE, "2501.00001")


def test_paragraphs_keep_latexml_numbers_and_drop_non_text(doc):
    assert doc["title"] == "Benchmarking Agents"
    assert [p["p"] for p in doc["paragraphs"]] == ["abstract", "S1.p1", "S1.p2", "S2.p1", "S2.p2", "S2.F1", "S3.p1"]
    text = " ".join(p["text"] for p in doc["paragraphs"])
    assert "Code is public" not in text  # footnote
    assert "A cited paper title" not in text  # bibliography
    assert "Alice Smith" not in text and "ignore me" not in text
    assert "by 12\\% over the baseline on all benchmarks" in doc["paragraphs"][2]["text"]  # math kept as its TeX source
    assert doc["paragraphs"][5]["text"] == "Figure 1: Accuracy against task length."


def test_outline_and_sections(doc):
    assert fulltext.outline(doc) == "abstract Abstract (1¶); S1 1 Introduction (2¶); S2 2 Experiments (3¶); S3 3 Conclusion (1¶)"
    assert [p["p"] for p in fulltext.section_paragraphs(doc, "experiments")] == ["S2.p1", "S2.p2", "S2.F1"]
    assert [p["p"] for p in fulltext.section_paragraphs(doc, "S3")] == ["S3.p1"]
    assert fulltext.section_paragraphs(doc, "Related Work") == []


def test_nested_paragraphs_keep_reading_order():
    nested = '<div id="S1.p1" class="ltx_para"><p class="ltx_p">We compare:</p><ul class="ltx_itemize"><li class="ltx_item"><span class="ltx_tag ltx_tag_item">•</span><div id="S1.I1.i1.p1" class="ltx_para"><p class="ltx_p">Greedy decoding at temperature zero.</p></div></li></ul></div>'
    page = latexml_page("T", {"Setup": []}).replace('<span class="ltx_tag ltx_tag_section">1 </span>Setup</h2>', '<span class="ltx_tag ltx_tag_section">1 </span>Setup</h2>' + nested)
    doc = fulltext.parse_html(page, "2501.00001")
    assert [(p["p"], p["text"]) for p in doc["paragraphs"][1:]] == [("S1.p1", "We compare:"), ("S1.I1.i1.p1", "Greedy decoding at temperature zero.")]


@pytest.mark.parametrize(
    "quote",
    [
        "Agents fail in long tasks, and we measure why.",  # citation dropped
        "agents fail in long tasks (Cobbe et al., 2021), and we measure why",  # citation kept, case changed
        "improves accuracy by 12% over the baseline on all benchmarks",  # math as plain text
    ],
)
def test_quotes_match_up_to_case_punctuation_and_citations(doc, quote):
    para, problem = fulltext.find_quote(doc, quote, "S1.p1")
    assert problem is None and para["s"] == "S1"


def test_quote_from_another_paragraph_is_found_and_relocated(doc):
    para, _ = fulltext.find_quote(doc, "We evaluate on five benchmarks with three random seeds", "S1.p1")
    assert para["p"] == "S2.p1"


@pytest.mark.parametrize(
    ("quote", "why"),
    [
        ("We evaluate on six benchmarks with three random seeds each.", "not found word for word"),  # changed fact
        ("We evaluate on five benchmarks ... three random seeds each.", "not found word for word"),  # ellipsis
        ("five benchmarks", "fewer than 6 words"),
        ("Experiments use five benchmarks. The planner ablation removes most of the gain.", "not found word for word"),  # stitched
    ],
)
def test_changed_short_or_stitched_quotes_are_rejected(doc, quote, why):
    para, problem = fulltext.find_quote(doc, quote, "S2.p1")
    assert para is None and why in problem


def test_quote_does_not_match_across_word_boundaries(doc):
    # "ard" is the tail of "hard", not a word of the paragraph.
    assert fulltext.find_quote(doc, "ard for every agent we tested", "S3.p1")[0] is None


def test_abstract_only_fallback_can_still_be_quoted():
    doc = fulltext.abstract_only(paper(1) | {"abstract": "We introduce a benchmark of long web tasks for agents."}, "no HTML version")
    assert doc["status"] == "abstract_only" and fulltext.outline(doc) == "abstract Abstract (1¶)"
    assert fulltext.find_quote(doc, "a benchmark of long web tasks for agents", "abstract")[0]["p"] == "abstract"
