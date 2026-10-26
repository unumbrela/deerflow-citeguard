"""Render docs/holdout.svg from the held-out run summaries (no hard-coded numbers).

    python3 -I docs/make_chart.py

Reads runs/suite-holdout3-{base,v3}/summary.json (round two: 10 topics x 3 runs per arm). Colors are the validated
categorical slots 1 and 2 (light + dark); the SVG switches with prefers-color-scheme.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def stats(name: str) -> dict:
    rows = [r for r in json.loads((ROOT / "runs" / f"suite-{name}" / "summary.json").read_text())["rows"] if r["status"] == "ok"]
    refs = sum(r["refs"] for r in rows)
    runs = len(json.loads((ROOT / "runs" / f"suite-{name}" / "summary.json").read_text())["rows"])
    # The pre-registered primary metric (eval/holdout_report.py): 10 papers delivered, all three checks pass.
    clean = sum(1 for r in rows if r["refs"] == r["verified"] == r["in_window"] == r["in_category"] == 10)
    return {
        "verified": 100 * sum(r["verified"] for r in rows) / refs,
        "window": 100 * sum(r["in_window"] for r in rows) / refs,
        "category": 100 * sum(r["in_category"] for r in rows) / refs,
        "clean": 100 * clean / runs,  # an undelivered run counts as a miss
        "clean_n": f"{clean}/{runs}",
        "refs": refs,
    }


base, v3 = stats("holdout3-base"), stats("holdout3-v3")
groups = [
    ("引用真实(已验证)", base["verified"], v3["verified"], f"{base['verified']:.1f}%", f"{v3['verified']:.1f}%"),
    ("满足「近两年」", base["window"], v3["window"], f"{base['window']:.1f}%", f"{v3['window']:.1f}%"),
    ("满足指定类别", base["category"], v3["category"], f"{base['category']:.1f}%", f"{v3['category']:.1f}%"),
    ("三项全满足的运行", base["clean"], v3["clean"], base["clean_n"], v3["clean_n"]),
]

W, H = 760, 450
L, R, T, B = 64, 24, 124, 86
plot_w, plot_h = W - L - R, H - T - B
group_w = plot_w / len(groups)
bar_w, gap = 54, 4
y = lambda v: T + plot_h * (1 - v / 100)


def bar(x: float, v: float, cls: str) -> str:
    top, r = y(v), 4
    r = min(r, bar_w / 2, plot_h * v / 100)
    base_y = T + plot_h
    # rounded data end (top), square at the baseline
    return f'<path class="{cls}" d="M{x:.1f},{base_y:.1f} V{top + r:.1f} Q{x:.1f},{top:.1f} {x + r:.1f},{top:.1f} H{x + bar_w - r:.1f} Q{x + bar_w:.1f},{top:.1f} {x + bar_w:.1f},{top + r:.1f} V{base_y:.1f} Z"/>'


out = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">',
    "<title id=\"t\">留出评测:上游 skill 与 v3 的约束遵守对比</title>",
    "<desc id=\"d\">" + "; ".join(f"{g[0]}: 上游 {g[3]}, v3 {g[4]}" for g in groups) + "</desc>",
    """<style>
  .bg{fill:#fcfcfb}.ink{fill:#0b0b0b}.sub{fill:#52514e}.grid{stroke:#e4e3df;stroke-width:1}.axis{stroke:#bdbcb6;stroke-width:1}
  .s1{fill:#eb6834}.s2{fill:#2a78d6}
  text{font-family:-apple-system,'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC','Microsoft YaHei',Helvetica,Arial,sans-serif}
  @media (prefers-color-scheme: dark){.bg{fill:#1a1a19}.ink{fill:#f0efec}.sub{fill:#c3c2b7}.grid{stroke:#34332f}.axis{stroke:#55544e}.s1{fill:#d95926}.s2{fill:#3987e5}}
</style>""",
    f'<rect class="bg" width="{W}" height="{H}"/>',
    f'<text class="ink" x="{L}" y="34" font-size="18" font-weight="600">未见过的 10 个主题 × 3 次:三项全满足的运行,上游 {base["clean_n"]} → v3 {v3["clean_n"]}</text>',
    f'<text class="sub" x="{L}" y="56" font-size="12.5">前三组按引用计(上游 {base["refs"]} 条 / v3 {v3["refs"]} 条);最后一组按运行计,要求交付 10 篇,未交付算未满足</text>',
    # legend: swatch + label, ink text
    f'<rect class="s1" x="{L}" y="68" width="12" height="12" rx="2"/><text class="ink" x="{L + 18}" y="78.5" font-size="12.5">上游 skill</text>',
    f'<rect class="s2" x="{L + 100}" y="68" width="12" height="12" rx="2"/><text class="ink" x="{L + 118}" y="78.5" font-size="12.5">v3</text>',
]
for v in (0, 25, 50, 75, 100):
    out.append(f'<line class="{"axis" if v == 0 else "grid"}" x1="{L}" x2="{W - R}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>')
    out.append(f'<text class="sub" x="{L - 8}" y="{y(v) + 4:.1f}" font-size="11.5" text-anchor="end">{v}%</text>')
for i, (name, bv, nv, bl, nl) in enumerate(groups):
    cx = L + group_w * (i + 0.5)
    x1, x2 = cx - bar_w - gap / 2, cx + gap / 2
    out.append(bar(x1, bv, "s1"))
    out.append(bar(x2, nv, "s2"))
    out.append(f'<text class="ink" x="{x1 + bar_w / 2:.1f}" y="{y(bv) - 7:.1f}" font-size="12.5" text-anchor="middle">{bl}</text>')
    out.append(f'<text class="ink" x="{x2 + bar_w / 2:.1f}" y="{y(nv) - 7:.1f}" font-size="12.5" text-anchor="middle">{nl}</text>')
    out.append(f'<text class="ink" x="{cx:.1f}" y="{T + plot_h + 24}" font-size="13" text-anchor="middle">{name}</text>')
out.append(f'<text class="sub" x="{W - R}" y="{H - 14}" font-size="11" text-anchor="end">数据:runs/suite-holdout3-{{base,v3}}/summary.json · 主指标 95% CI:上游 0.6%–16.7%,v3 83.3%–99.4%</text>')
out.append("</svg>")
(ROOT / "docs" / "holdout.svg").write_text("\n".join(out), encoding="utf-8")
print("wrote docs/holdout.svg", {k: round(v, 1) if isinstance(v, float) else v for k, v in {**{"base_" + k: v for k, v in base.items()}, **{"v3_" + k: v for k, v in v3.items()}}.items()})
