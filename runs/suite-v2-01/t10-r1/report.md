# Systematic Literature Review: Text Summarization Evaluation

**Date**: 2025-10-25
**Papers surveyed**: 2
**Scope**: arXiv search query "text summarization evaluation", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review surveyed recent arXiv preprints on text summarization evaluation within the computational linguistics category (cs.CL). The search yielded only 2 papers from the past two years, suggesting that while text summarization remains an active research area, explicit work on evaluation methodologies specifically categorized under cs.CL is relatively limited. The two identified papers reveal critical concerns about reproducibility in automatic evaluation metrics and emerging investigations into reasoning-enabled large language models as evaluators. Both papers highlight significant challenges in current evaluation practices: discrepancies between reported and experimental performance, and the complex trade-offs between alignment with human judgment and computational efficiency.

## Methodology

This review surveyed 2 arXiv papers retrieved on 2025-10-25 using the query "text summarization evaluation", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top results were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Important note**: The search returned only 2 papers instead of the requested 10, indicating that this specific query with the cs.CL category filter captures a narrow subset of the literature. Researchers seeking broader coverage may need to expand the search to adjacent categories (cs.AI, cs.IR) or use broader search terms.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The small sample size limits the ability to identify robust thematic patterns.

## Themes

### Theme 1: Reproducibility Challenges in Automatic Evaluation

A critical theme emerging from the surveyed literature is the reproducibility crisis in automatic text summarization evaluation. Herserant & Guigue (2025) demonstrate significant discrepancies between reported performances in the literature and observed experimental performances when metrics are evaluated under unified, controlled conditions. This finding suggests that the field may be operating with inflated or unreliable expectations about metric performance, potentially due to inconsistent experimental setups, dataset variations, or implementation differences across research groups.

The structural trade-off identified between alignment quality and computational efficiency represents a fundamental challenge: metrics that best correlate with human judgment tend to be computationally intensive and exhibit instability across runs. This creates practical difficulties for researchers who must balance evaluation quality against resource constraints and reproducibility requirements.

### Theme 2: LLM-Based Evaluation and Reasoning Capabilities

The second theme concerns the emerging use of large language models, particularly reasoning-enabled variants, as evaluation tools. Larionov et al. (2025) systematically investigate whether reasoning capabilities in LLMs improve evaluation quality for machine translation and text summarization tasks. Their findings reveal a nuanced picture: reasoning tokens correlate with evaluation quality only in specific models, and the relationship between reasoning capacity and evaluation performance is not straightforward.

The observation that models allocate more reasoning tokens when identifying quality issues suggests that reasoning-enabled LLMs may be engaging in more sophisticated diagnostic processes during evaluation. However, the degradation of performance in heavily distilled models (particularly at 8B scale) indicates that compression techniques may compromise the nuanced reasoning required for reliable evaluation.

## Convergences and Disagreements

**Convergences**: Both papers converge on the finding that LLM-based evaluation methods exhibit significant variability and instability. Herserant & Guigue (2025) note that LLMs for evaluation show randomness and technical dependencies, while Larionov et al. (2025) demonstrate that reasoning token usage and evaluation quality relationships are model-specific. This suggests the field is grappling with fundamental reliability issues in neural evaluation approaches.

**Disagreements**: The papers do not directly contradict each other, as they address different aspects of evaluation. However, there is a tension between the findings: Herserant & Guigue (2025) emphasize the reproducibility problems with LLM-based metrics, while Larionov et al. (2025) explore whether reasoning capabilities might improve evaluation quality. The resolution of this tension remains an open question.

## Gaps and Open Questions

Several gaps emerge from this limited survey:

1. **Lack of standardized evaluation frameworks**: Herserant & Guigue (2025) highlight the need for open-source frameworks that enable fair comparison of metrics, suggesting the field lacks universally accepted evaluation protocols.

2. **Understanding reasoning mechanisms**: Larionov et al. (2025) note that the correlation between reasoning tokens and evaluation quality is model-specific, indicating gaps in understanding how reasoning actually contributes to evaluation performance.

3. **Scalability vs. quality trade-offs**: Both papers implicitly acknowledge but do not fully resolve the tension between computationally efficient metrics and those that align well with human judgment.

4. **Limited scope of cs.CL category**: The small number of papers returned suggests that evaluation research may be published under adjacent categories or in venues not captured by this search, indicating a potential gap in systematic coverage.

## Per-Paper Annotations

### Herserant & Guigue (2025)

**Research question**: This paper investigates reproducibility challenges in automatic text summarization evaluation and the discrepancies between reported performances in literature and observed experimental performances.

**Methodology**: Experiments conducted across six representative metrics ranging from classical approaches like ROUGE to recent LLM-based methods (G-Eval, SEval-Ex), applied to the SummEval dataset using a unified open-source framework designed for fair and transparent comparison.

**Key findings**:
- Significant discrepancies exist between reported performances in literature and observed experimental performances
- Metrics with highest alignment with human judgments tend to be computationally intensive and less stable across runs
- LLMs for evaluation exhibit randomness, technical dependencies, and limited reproducibility
- A structural trade-off exists between alignment quality and computational efficiency/stability

**Limitations**: Not stated in abstract

### Larionov et al. (2025)

**Research question**: How well can reasoning-enabled large language models evaluate natural language generation compared to non-reasoning LLMs across machine translation and text summarization tasks?

**Methodology**: Systematic comparison of eight models spanning state-of-the-art reasoning models (DeepSeek-R1, OpenAI o3), distilled variants (8B-70B parameters), and equivalent non-reasoning LLMs on WMT23 and SummEval benchmarks with correlation analysis of reasoning token usage.

**Key findings**:
- OpenAI o3-mini models show improved performance with increased reasoning on machine translation, while DeepSeek-R1 underperforms compared to its non-reasoning variant except in summarization consistency evaluation
- Reasoning token usage correlates with evaluation quality only in specific models
- Almost all models allocate more reasoning tokens when identifying more quality issues
- Distillation maintains reasonable performance up to 32B parameter models but degrades substantially at 8B scale

**Limitations**: Not stated in abstract

## References

Herserant, T., & Guigue, V. (2025). AllSummedUp: un framework open-source pour comparer les metriques d'evaluation de resume. arXiv. https://arxiv.org/abs/2508.21389

Larionov, D., Takeshita, S., Zhang, R., Chen, Y., Leiter, C., Wang, Z., Greisinger, C., & Eger, S. (2025). DeepSeek-R1 vs. o3-mini: How well can reasoning LLMs evaluate MT and summarization? arXiv. https://arxiv.org/abs/2504.08120
