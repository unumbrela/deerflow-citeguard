# 人工标注说明：论断是否被论文支持（100 条）

目的：检验 LLM 评判器可不可信。你的标签会和评判器的标签对比，算出一致率（Cohen's κ）。**标注时请不要看评判器的结果**，它单独存放在 `claims-100.judge.json` 里。

## 怎么标

打开 `claims-100.csv`（Excel 或 Numbers 都可以），每行包含：

- `claim`：综述报告里的一句话
- `paper_title` / `abstract`：这句话引用的那篇论文的标题和摘要

**只根据摘要判断**，在 `human_label` 列填下面四个词之一（英文小写）：

| 标签 | 什么时候用 |
|---|---|
| `supported` | 摘要明确说了，或者能直接推出这句话里归到这篇论文身上的内容 |
| `partial` | 只支持一部分，或者这句话说过头了（夸大、泛化、加了摘要里没有的数字） |
| `unsupported` | 摘要里看不出来（可能论文正文里有，但摘要没提） |
| `contradicted` | 摘要说的正好相反 |

拿不准的话，可以在 `note` 列写一句理由。

## 几个容易犹豫的情况

- 一句话同时引用了好几篇论文：只看**这一行对应的这篇**，判断它是否支持这句话里与它有关的部分。
- 句子是综合性的（比如"多篇论文都发现……"）：只要这篇的摘要支持这个共同结论，就算 `supported`。
- 数字对不上（比如摘要写 2.5 倍，句子写 3 倍）：标 `partial`。

## 标完以后

保存为 CSV（UTF-8），文件名不变，然后告诉我。我会运行：

```bash
cd eval && python3 -I claims.py agreement --labels annotation/claims-100.csv
```

预计用时 2~3 小时。可以分几次标，没填的行会被跳过。

注：这 100 条是按评判器的四种标签各抽 25 条（分层抽样），目的是让少见的标签也有足够样本来检验。所以算出的一致率反映的是"评判器在各类情况下靠不靠谱"，不等于在全部数据上的准确率。

## 2026-10-27:先做了 LLM 交叉标注

Claude 不看评判器结果，按本说明标了全部 100 条：`claims-100.claude.csv`(先提交、后比对，见 commit d908d51)。**这不是人工标注**，只说明两个不同家族的模型一致到什么程度、分歧在哪里。结果见 BASELINE.md「论断支持率:LLM 交叉标注」。

两边不一致的 44 条单独放在 `claims-disputed.csv`,两边的标签都不显示。你只标这 44 条(约 40 分钟)就能裁定谁对。标法同上，标完运行:

```bash
cd eval
python3 -I claims.py agreement --labels annotation/claims-disputed.csv --judge annotation/claims-100.judge.json   # 你 vs 评判器
python3 -I claims.py agreement --labels annotation/claims-disputed.csv --judge annotation/claims-100.claude.json  # 你 vs Claude
```

## 2026-10-27:用户审阅后，以 Claude 标签为参考标准

不再需要人工标注，`claims-disputed.csv` 作废。之后又按同样规则盲标了一批新样本 `claims-holdout-100.claude.csv`,用来检验评判器 v2(见 `../HOLDOUT.md`)。验证新评判器：

```bash
cd eval
python3 -I claims.py judge-sample --labels annotation/claims-holdout-100.csv --prompt v2 --out annotation/claims-holdout-100.v2.json
python3 -I claims.py agreement --labels annotation/claims-holdout-100.claude.csv --judge annotation/claims-holdout-100.v2.json
```
