"""Shared offline fixtures: synthetic papers and an arXiv Atom feed builder."""

from __future__ import annotations

from xml.sax.saxutils import escape


def paper(i: int, primary: str = "cs.CL", abstract_chars: int = 800, n_authors: int = 2) -> dict:
    return {
        "id": f"2501.{i:05d}",
        "title": f"Benchmarking Agents Part {i}",
        "authors": [f"Alice Smith{i}"] + [f"Bob Jones{j}" for j in range(n_authors - 1)],
        "abstract": "x" * abstract_chars,
        "published": "2025-01-02",
        "updated": "2025-01-02",
        "categories": [primary],
        "primary_category": primary,
        "pdf_url": "",
        "abs_url": f"http://arxiv.org/abs/2501.{i:05d}v1",
    }


def atom_feed(papers: list[dict]) -> str:
    entries = []
    for p in papers:
        authors = "".join(f"<author><name>{escape(a)}</name></author>" for a in p["authors"])
        entries.append(
            f"""<entry>
  <id>http://arxiv.org/abs/{p["id"]}v2</id>
  <updated>{p["updated"]}T00:00:00Z</updated>
  <published>{p["published"]}T10:00:00Z</published>
  <title>{escape(p["title"])}</title>
  <summary>  {escape(p["abstract"])}
  </summary>
  {authors}
  <link href="http://arxiv.org/abs/{p["id"]}v2" rel="alternate" type="text/html"/>
  <link title="pdf" href="http://arxiv.org/pdf/{p["id"]}v2" rel="related" type="application/pdf"/>
  <arxiv:primary_category term="{p["primary_category"]}"/>
  <category term="{p["primary_category"]}"/>
</entry>"""
        )
    return '<?xml version="1.0" encoding="UTF-8"?><feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">' + "".join(entries) + "</feed>"


def latexml_page(title: str, sections: dict[str, list[str]], abstract: str = "We study agents.", extra: str = "") -> str:
    """A minimal arXiv HTML page in LaTeXML's markup: numbered sections and paragraphs, a citation, a footnote, a bibliography."""
    body = []
    for n, (heading, paragraphs) in enumerate(sections.items(), 1):
        paras = "".join(f'<div id="S{n}.p{i}" class="ltx_para"><p id="S{n}.p{i}.1" class="ltx_p">{text}</p></div>' for i, text in enumerate(paragraphs, 1))
        body.append(f'<section id="S{n}" class="ltx_section"><h2 class="ltx_title ltx_title_section"><span class="ltx_tag ltx_tag_section">{n} </span>{heading}</h2>{paras}</section>')
    return f"""<html><head><title>{title}</title><script>var x = "ignore me";</script></head><body>
<div class="ltx_page_main"><article class="ltx_document">
<h1 class="ltx_title ltx_title_document">{title}</h1>
<div class="ltx_authors"><span class="ltx_personname">Alice Smith</span></div>
<div id="abstract1" class="ltx_abstract"><h6 class="ltx_title ltx_title_abstract">Abstract</h6><p id="abstract1.1" class="ltx_p">{abstract}</p></div>
{"".join(body)}{extra}
<section id="bib" class="ltx_bibliography"><h2 class="ltx_title ltx_title_bibliography">References</h2>
<ul class="ltx_biblist"><li id="bib.bib1" class="ltx_bibitem">Someone. A cited paper title that is not this paper. 2021.</li></ul></section>
</article></div></body></html>"""
