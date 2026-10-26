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
