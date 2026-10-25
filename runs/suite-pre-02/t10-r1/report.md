# Systematic Literature Review: Text Summarization Evaluation

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "summarization evaluation", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on text summarization evaluation reveals a field in rapid transition, moving from traditional n-gram-based metrics like ROUGE toward more sophisticated LLM-based and psychometric approaches. Collectively, the papers demonstrate that existing evaluation metrics suffer from critical limitations: instability across reference sets, saturation that prevents effective model ranking, poor alignment with human judgment when reader context matters, and reproducibility challenges with LLM-as-judge methods. Recent work addresses these gaps through statement-level frameworks, semantic scaffolds, composite hallucination indices, and psychometric analyses that decompose judging behavior. The field is converging on the need for multi-dimensional, interpretable evaluation that captures not just surface quality but faithfulness, information satisfaction, and the mechanisms by which evaluators make decisions.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "summarization evaluation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Instability and Reproducibility Challenges in Existing Metrics

A dominant theme across multiple papers is the fundamental instability of widely used summarization metrics. Casola et al. (2025) demonstrate that reference-based metrics, particularly ROUGE, exhibit significant sensitivity to the choice of reference sets, with model rankings varying depending on which references are selected. This instability undermines the reliability of model comparisons and calls into question the validity of evaluation results that do not account for reference set variation.

Herserant and Guigue (2025) extend this concern to reproducibility, showing that metrics with the highest alignment to human judgments tend to be computationally intensive and less stable across runs. Their AllSummedUp framework reveals significant discrepancies between reported performances in the literature and those observed in controlled experimental settings. This reproducibility crisis is particularly acute for LLM-based evaluators, which exhibit randomness, technical dependencies, and limited reproducibility across runs.

The convergence of these findings suggests that the field has been operating on unstable foundations, with model comparisons and benchmark results potentially reflecting arbitrary choices in reference selection and evaluation protocols rather than genuine differences in summarization quality.

### Theme 2: Beyond Aggregate Scores — Interpretable and Multi-Dimensional Evaluation

Multiple papers advocate for moving beyond single aggregate scores toward interpretable, multi-dimensional evaluation frameworks. Herserant and Guigue (2025) present SEval-Ex, which decomposes evaluation into atomic statements and achieves state-of-the-art correlation (0.580) with human judgments while providing statement-level evidence for its decisions. This approach bridges the typical trade-off between performance and interpretability.

Pottanigari et al. (2026) introduce Semantic Scaffolds, extracting hierarchical representations of facts, questions, and entity attributes to derive three diagnostic metrics: Fact Preservation Score (FPS), Question Preservation Score (QPS), and Entity Preservation Score (EPS). These metrics remain informative where conventional metrics saturate, providing interpretable diagnostics for production model selection.

Katwe et al. (2026) propose CHI (Composite Hallucination Index), which unifies three orthogonal dimensions of faithfulness errors: entity, relation, and quantity hallucination. Their composite score achieves the highest correlation with human judgments (rho = 0.66) on SummEval while providing decomposable error diagnostics unavailable from single-score baselines.

This theme reflects a maturing understanding that evaluation must support not just ranking but diagnosis — practitioners need to know not just which model is better, but why and in what ways.

### Theme 3: LLM-as-Judge Mechanisms and Limitations

A substantial cluster of papers examines LLM-as-judge methods, both their capabilities and their limitations. Vasava and Jiang (2026) provide mechanistic insights into how LLM evaluators assign ratings, revealing a structured two-stage evaluation pipeline where attention performs local error comparison below layer 15 and MLP integration writes the rating above layer 15, with decision crystallization at sharp late layers. This fine-tuning sculpts existing substrates rather than building evaluation pipelines from scratch.

Larionov et al. (2025) systematically compare reasoning LLMs with non-reasoning counterparts for summarization evaluation, finding architecture and task-dependent benefits. OpenAI o3-mini models show improved performance with increased reasoning, while DeepSeek-R1 generally underperforms except in consistency evaluation. Reasoning token usage correlates with evaluation quality only in specific models, limiting the universality of reasoning benefits.

Cong et al. (2026) challenge the standard validity assessment paradigm, showing that moderate alignment in latent summary quality does not imply alignment in residual hardness — humans and LLMs find different cases difficult. This mismatch is dimension-dependent, with consistency showing a pronounced LLM-hard shift and coherence showing a human-hard shift. Their psychometric analysis suggests aggregate human alignment reflects only part of LLM-as-judge reliability.

Cachola et al. (2026) demonstrate that both traditional and LLM-based metrics fail to measure information satisfaction for individual users with different personas and informational needs, agreeing poorly with human judgment when reader context is considered.

### Theme 4: Reader-Centered and Task-Specific Evaluation

Emerging work recognizes that summarization quality is not absolute but depends on reader needs and use cases. Cachola et al. (2026) introduce information satisfaction as a reader-centered axis, showing that current metrics fail basic perturbation tests of informational content and do not capture whether a summary satisfies a specific reader's background and use case. Their expert human evaluation reveals that reader persona is a practical, stable signal for assessing summary utility.

This theme represents a shift from generic quality assessment toward user-centered evaluation that considers the functional purpose of summaries in real-world contexts.

### Theme 5: Connections Between Summarization and Related Tasks

Magnifico and Barbu (2025) explore the relationship between summarization and simplification, finding that abstractive summarization can achieve moderate overlap with gold-standard simplifications (ROUGE-L of 0.654). This work highlights how evaluation methods are more streamlined for summarization compared to simplification, which lacks cohesion, and provides insight into where these related tasks converge and differ.

## Convergences and Disagreements

**Convergences**:
- Multiple papers converge on the inadequacy of traditional metrics: ROUGE captures only surface overlap (Pottanigari et al., 2026), exhibits instability across reference sets (Casola et al., 2025), and fails to measure information satisfaction (Cachola et al., 2026).
- There is broad agreement that LLM-as-judge methods, while promising, suffer from reproducibility challenges, randomness, and technical dependencies (Herserant & Guigue, 2025).
- Papers consistently find that metrics with highest alignment to human judgments tend to be computationally intensive and less stable (Herserant & Guigue, 2025; Larionov et al., 2025).
- All papers proposing new frameworks validate on SummEval, establishing it as the standard benchmark, though this concentration raises concerns about overfitting.

**Disagreements**:
- The utility of reasoning LLMs for evaluation is contested: Larionov et al. (2025) find reasoning benefits are architecture and task-dependent, with DeepSeek-R1 underperforming its non-reasoning variant except in consistency evaluation, while OpenAI o3-mini shows improvement with reasoning on machine translation.
- There is tension between interpretability and performance: while Herserant and Guigue (2025) claim SEval-Ex bridges this gap, other work suggests the trade-off remains structural (Herserant & Guigue, 2025).
- The validity of aggregate human alignment as the gold standard is questioned by Cong et al. (2026), who show it reflects only part of LLM-as-judge reliability, challenging the assumption underlying most evaluation research.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Limited generalization beyond SummEval**: Nearly all papers validate primarily on SummEval, with limited testing on other domains and datasets. This concentration risks overfitting and limits confidence in generalizability to production scenarios.

2. **Multilingual and cross-lingual evaluation**: Only Pottanigari et al. (2026) explicitly mention multilingual settings, and the literature is overwhelmingly English-centric. Evaluation methods may not transfer across languages with different morphological and syntactic properties.

3. **Scalability of interpretable methods**: While interpretability is widely advocated, the computational overhead of statement-level analysis (Herserant & Guigue, 2025), semantic scaffolds (Pottanigari et al., 2026), and composite indices (Katwe et al., 2026) may limit adoption in production systems requiring real-time evaluation.

4. **Reader persona coverage**: Cachola et al. (2026) introduce reader-centered evaluation but acknowledge limited scale in expert human evaluation and focus on specific use cases that may not capture all reader personas.

5. **Closed-source model evaluation**: Cong et al. (2026) limit analysis to 17 open-weight LLM judges, leaving closed-source models unexamined despite their widespread use in production.

6. **Longitudinal stability**: No paper addresses how evaluation metrics perform over time as models and data distributions shift, a critical concern for production monitoring.

7. **Integration of multiple dimensions**: While multi-dimensional evaluation is advocated, no unified framework integrates reference stability, faithfulness, information satisfaction, and interpretability into a single coherent approach.

## Per-Paper Annotations

### Cachola et al. (2026)

**Research question**: Do current summarization metrics adequately measure the utility of a summary to individual users with different informational needs and personas?
**Methodology**: Assesses how sensitive popular summarization metrics are to informational and persona differences through perturbation tests, and conducts expert human evaluation measuring summary preferences based on information satisfaction given specific reader backgrounds and use cases.
**Key findings**:
- Many popular metrics including strong LLM-as-judge metrics fail basic perturbation tests of informational content
- Both traditional and LLM-based metrics are insufficient measures of information satisfaction
- Current metrics agree poorly with human judgment when reader persona and background are considered
- Reader background/persona is a practical, stable signal for assessing whether a summary satisfies user needs
**Limitations**: Expert human evaluation may be limited in scale; focus on specific use cases may not capture all reader personas.

### Casola et al. (2025)

**Research question**: How does the choice of reference sets impact the reliability and stability of reference-based metrics in summarization evaluation?
**Methodology**: Examines the sensitivity of widely used reference-based metrics across three diverse multi-reference summarization datasets (SummEval, GUMSum, DUC2004) and collects human judgments on LLM outputs for genre-diverse data to examine correlation with metrics.
**Key findings**:
- Many popular reference-based metrics exhibit significant instability depending on reference set choice
- ROUGE model rankings vary substantially based on which reference sets are used, undermining reliability of model comparisons
- Human judgments on LLM outputs for genre-diverse data show weak-to-no correlation with existing metrics
- Incorporating reference set variation into evaluation enhances consistency alongside correlation with human judgments
**Limitations**: Analysis focuses primarily on reference-based metrics; human judgment collection may be limited in scope beyond newswire summaries.

### Cong et al. (2026)

**Research question**: Do humans and LLMs find the same evaluation cases difficult, beyond aggregate score alignment in summarization evaluation?
**Methodology**: Fit Many-Facet Rasch Models separately to human and LLM ratings to decompose scores into latent summary quality, rater severity, dimension severity, and rating-scale thresholds; defined residual hardness as a model-adjusted measure of judging difficulty across 17 open-weight LLM judges on SummEval.
**Key findings**:
- Moderate alignment in latent summary quality does not imply alignment in residual hardness between human and LLM judges
- Human and LLM judges differ in which summary-dimension units remain difficult, with mismatch strongly dimension-dependent
- Consistency shows a pronounced LLM-hard shift, whereas coherence shows a human-hard shift
- Human-easy but LLM-hard cases are partially predictable from observable source-summary properties
- Psychometric residual diagnostics support more informative judge evaluation than aggregate human alignment alone
**Limitations**: Limited to 17 open-weight LLM judges on SummEval; does not address closed-source models or other evaluation domains beyond summarization.

### Herserant and Guigue (2025a)

**Research question**: How can summarization evaluation achieve both high performance and interpretability without the typical trade-off between the two?
**Methodology**: SEval-Ex employs a two-stage pipeline: first extracting atomic statements from source text and summary using LLM, then performing matching between generated statements to produce statement-level alignments with detailed evidence.
**Key findings**:
- Achieves state-of-the-art 0.580 correlation on consistency with human judgments on SummEval benchmark
- Surpasses GPT-4 based evaluators which achieved 0.521 correlation
- Generates detailed evidence for decisions through statement-level alignments rather than only summary-level scores
- Framework demonstrates robustness against hallucination
**Limitations**: Evaluated primarily on SummEval benchmark; generalization to other domains and datasets requires further validation.

### Herserant and Guigue (2025b)

**Research question**: What are the reproducibility challenges in automatic text summarization evaluation, and how do reported metric performances compare to experimental observations?
**Methodology**: Conducted experiments across six representative metrics (from classical ROUGE to recent LLM-based methods like G-Eval and SEval-Ex) on the SummEval dataset using a unified open-source framework designed for fair and transparent comparison.
**Key findings**:
- Significant discrepancies exist between reported performances in literature and those observed in experimental settings
- Metrics with highest alignment with human judgments tend to be computationally intensive and less stable across runs
- LLM-based evaluation shows randomness, technical dependencies, and limited reproducibility
- Results reveal a structural trade-off between alignment quality and computational stability
- Highlights need for more robust evaluation protocols including exhaustive documentation and methodological standardization
**Limitations**: Limited to six metrics on the SummEval dataset; does not propose concrete solutions beyond advocating for standardization and better documentation.

### Katwe et al. (2026)

**Research question**: How can faithfulness evaluation of abstractive summaries be unified to capture co-occurring hallucination types across entity, relation, and quantity dimensions?
**Methodology**: Introduced CHI (Composite Hallucination Index) that decomposes faithfulness errors into three orthogonal dimensions (EHI, RHI*, QHI) using softmax-normalized architecture over Venn diagram-derived factors, validated on 800 source articles across four domains with summaries from five generation systems.
**Key findings**:
- The three dimensions are statistically orthogonal (mean rho = 0.148), confirming they capture distinct error types
- CHI achieves the highest system-level correlation with human judgments (rho = 0.66, p = 0.006) on SummEval, outperforming ROUGE (rho = 0.53) and EHI (rho = 0.58)
- Ablation studies confirm all three dimensions contribute unique variance, with the full composite outperforming any individual component
- The novel QHI component introduces tolerance-aware numerical matching with exact, epsilon, derived, and temporal comparison modes
- Provides decomposable error diagnostics unavailable from single-score baselines
**Limitations**: Validation limited to 800 articles across four domains (news, medical, legal, financial); may not generalize to all summarization scenarios or languages.

### Larionov et al. (2025)

**Research question**: How well can reasoning-enabled LLMs evaluate natural language generation compared to non-reasoning LLMs across machine translation and summarization tasks?
**Methodology**: Systematically compared eight models spanning state-of-the-art reasoning models (DeepSeek-R1, OpenAI o3), their distilled variants (8B-70B parameters), and equivalent non-reasoning LLMs on WMT23 and SummEval benchmarks with correlation analysis.
**Key findings**:
- OpenAI o3-mini models show improved performance with increased reasoning on machine translation tasks
- DeepSeek-R1 generally underperforms compared to its non-reasoning variant except in summarization consistency evaluation
- Reasoning token usage correlates with evaluation quality only in specific models, not universally
- Almost all models allocate more reasoning tokens when identifying more quality issues
- Distillation maintains reasonable performance up to 32B parameter models but degrades substantially at 8B scale
**Limitations**: Limited to eight models on WMT23 and SummEval benchmarks; reasoning benefits are architecture and task-dependent, limiting generalizability.

### Magnifico and Barbu (2025)

**Research question**: How closely can abstractive summarization resemble gold-standard simplification?
**Methodology**: Applied two BART-based BRIO summarization methods to the Newsela corpus, comparing outputs with manually annotated simplifications using ROUGE-L evaluation.
**Key findings**:
- Achieved a top ROUGE-L score of 0.654 when comparing summarization outputs to gold-standard simplifications
- Summarization evaluation methods are more streamlined compared to simplification, which lacks cohesion
- Results provide insight into where summarization and simplification outputs converge and differ
**Limitations**: Limited to BART-based BRIO methods and the Newsela corpus; does not address other summarization architectures or simplification datasets.

### Pottanigari et al. (2026)

**Research question**: How can summarization evaluation avoid metric saturation and provide interpretable diagnostics that effectively rank models for production deployment?
**Methodology**: Introduces Semantic Scaffold framework that extracts hierarchical representation of facts, questions, and entity attributes from source text labeled as main points or supporting details, then derives three diagnostic metrics (Fact Preservation Score, Question Preservation Score, Entity Preservation Score) using this structure as fixed reference.
**Key findings**:
- ROUGE captures only surface overlap while LLM-as-judge scores saturate to near-identical values failing to rank models effectively
- Metric saturation observed across three public datasets, two proprietary datasets, and multilingual settings
- Scaffold-based evaluation remains informative where conventional metrics collapse
- Identifies four recurring failure modes of ROUGE and LLM-as-judge scores
**Limitations**: Requires extracting hierarchical structure from source text which may add computational overhead; framework complexity may limit adoption.

### Vasava and Jiang (2026)

**Research question**: What internal mechanisms do LLM-as-judge evaluators use to assign ratings, and how does fine-tuning shape these evaluation procedures?
**Methodology**: Investigates mechanistically through eight-attack perturbation taxonomy across Readability and Adequacy dimensions, generates paired clean and corrupt summaries with controlled error intensity and token-level modification maps, and conducts four-experiment battery of causal tracing, logit-lens vocabulary projection, and attention-head knockout on Themis (Llama-3-8B) and Prometheus (Mistral-7B).
**Key findings**:
- Both evaluators implement structured two-stage evaluation pipeline operating coherently
- Below layer 15: attention performs local error comparison and routes to final input position; above layer 15: MLP cascade integrates signal and writes rating
- Decision crystallizes in residual stream at sharp late layer (L=26 on Themis, L=25 on Prometheus)
- Fine-tuning installs two specific mechanisms: suppression of below-L15 MLP contribution at last position and two-layer advance of crystallization depth
**Limitations**: Analysis focuses on two specific evaluator models (Themis and Prometheus); mechanisms may differ in other architectures and scales.

## References

Cachola, I., Walden, W., Kriz, R., & Dredze, M. (2026). Information satisfaction: A reader-centered axis for summarization evaluation. arXiv. https://arxiv.org/abs/2608.14457

Casola, S., Liu, Y. J., Peng, S., Kraus, O., Gatt, A., & Plank, B. (2025). References matter: Investigating the impact of reference set variation on summarization evaluation. arXiv. https://arxiv.org/abs/2506.14335

Cong, L., Hahn, S., Gombert, S., Camus, L., Zehner, F., Drachsler, H., & Kroehne, U. (2026). Evaluating LLM-as-a-judge beyond score alignment: A psychometric analysis of residual judging difficulty. arXiv. https://arxiv.org/abs/2610.02877

Herserant, T., & Guigue, V. (2025a). SEval-Ex: A statement-level framework for explainable summarization evaluation. arXiv. https://arxiv.org/abs/2505.02235

Herserant, T., & Guigue, V. (2025b). AllSummedUp: un framework open-source pour comparer les metriques d'evaluation de resume. arXiv. https://arxiv.org/abs/2508.21389

Katwe, P., Balabantaray, R. C., & Vittala, K. P. (2026). CHI: A composite hallucination index unifying entity, relation, and quantity dimensions for summarization evaluation. arXiv. https://arxiv.org/abs/2609.33343

Larionov, D., Takeshita, S., Zhang, R., Chen, Y., Leiter, C., Wang, Z., Greisinger, C., & Eger, S. (2025). DeepSeek-R1 vs. o3-mini: How well can reasoning LLMs evaluate MT and summarization? arXiv. https://arxiv.org/abs/2504.08120

Magnifico, G., & Barbu, E. (2025). Can summarization approximate simplification? A gold standard comparison. arXiv. https://arxiv.org/abs/2501.16181

Pottanigari, N. R., Fahimi, R., Bolger, N., Kharaghani, S., & Zhang, Y. (2026). Preserving what matters: Semantic scaffolds beyond saturation in summarization evaluation. arXiv. https://arxiv.org/abs/2609.22603

Vasava, H., & Jiang, M. (2026). Beyond scores: Understanding LLM-as-a-judge mechanisms in summarization evaluation. arXiv. https://arxiv.org/abs/2609.01604
