# Systematic Literature Review: LLM-Based Recommender Systems

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "LLM recommender", filtered to category cs.IR, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM-based recommender systems has evolved rapidly over the past two years, with research focusing on critical challenges including hallucination and catalog faithfulness, evaluation methodologies, optimization strategies, and efficiency-accuracy trade-offs. Recent work reveals significant concerns about the reliability of LLM recommenders, with hallucination rates varying dramatically across catalogs (0.6-61.0%) and models exhibiting poor confidence calibration. The field is shifting from semantic plausibility toward behavior-grounded utility metrics, with new benchmarks like RecoAtlas emphasizing real-world performance over surface-level coherence. Simultaneously, researchers are developing sophisticated optimization techniques including reinforcement learning with windowed partial AUC objectives, selective LLM-guided regularization, and multi-head early exit architectures for RAG-enhanced systems. A critical finding across multiple studies is that evaluation protocols matter enormously—oracle protocols overestimate performance by 92-95%, and synthetic benchmarks often misalign with user intent.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "LLM recommender", filtered to category cs.IR, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Hallucination and Catalog Faithfulness

A major line of research addresses the fundamental reliability challenge of LLM recommenders: their tendency to hallucinate items outside the target catalog. Ravikumar (2026) conducted a comprehensive audit of four zero-shot LLM recommenders across three catalogs, finding that hallucination rates are strongly catalog-dependent, ranging from 0.6-2.7% on MovieLens to 49.3-61.0% on Amazon Toys. Critically, models maintain near-constant confidence levels regardless of catalog, creating systematic over-confidence or under-confidence depending on the domain. The study reveals that verbalized confidence elicits generic quality ratings rather than catalog-membership probabilities, and conformal abstention thresholds provide minimal improvement (at most 1.65 percentage points).

This work highlights a fundamental elicitation mismatch in current LLM recommender deployments: asking models "how confident are you?" does not produce the catalog-membership probability needed for reliable recommendations. The audit methodology itself matters significantly, as string matching approaches can shift reported hallucination rates by an order of magnitude.

### Theme 2: Evaluation Protocol Reform

Multiple recent studies challenge prevailing evaluation practices in LLM recommendation research. Wang (2026) demonstrates that oracle evaluation protocols—which guarantee the ground-truth item is present in the candidate set—overestimate realistic NDCG@10 by 92-95% across Amazon datasets. The root cause is a "recall ceiling": realistic retrieval covers only 2-19% of relevant items at K=100, imposing a deterministic upper bound on any closed-candidate reranker's performance. Under realistic retrieval conditions, none of the tested optimization strategies (including prompt engineering, model scaling over 168× parameter range, LoRA fine-tuning, and LLM+CF fusion) significantly improved over collaborative-filtering baselines.

Complementing this analysis, Aouali et al. (2026) introduced RecoAtlas, a benchmark that moves beyond semantic plausibility to measure behavior-grounded utility including relevance, complementarity, and diversity. Their controlled experiments reveal that semantic plausibility does not necessarily capture behavior-grounded utility, and performance degrades under noisy or misaligned tool signals. Suresh (2026) similarly identified a critical misalignment in synthetic conversational benchmarks, finding that official labels contradict user requests in 50% of exact-song turns in the RecSys Challenge 2026 TalkPlay benchmark.

These studies collectively argue for Recall-Aware Evaluation Protocol (RAEP) and behavior-grounded metrics that reflect real-world deployment constraints rather than oracle conditions.

### Theme 3: Optimization Objectives and Reinforcement Learning

Research on optimization objectives has revealed important theoretical insights about how reinforcement learning shapes LLM recommender behavior. Shi et al. (2026) provided theoretical analysis showing that optimizing LLM recommenders with Group Relative Policy Optimization (GRPO) under binary reward feedback is equivalent to maximizing Area Under the ROC Curve (AUC), which is often misaligned with Top-K recommendation metrics. Their key finding is that replacing random negatives with beam-search negatives reshapes the objective toward partial AUC, improving alignment with Top-K performance.

Building on this insight, they introduced Windowed Partial AUC (WPAUC), which constrains the false positive rate to a window [α,α+d] to more directly align with Top-K metrics, optimized via Threshold-Adjusted Windowed reweighting (TAWin). This method enables explicit control over targeted Top-K performance and achieved state-of-the-art results across four real-world datasets.

Yang and Shi (2025) proposed Selective LLM-Guided Regularization, which activates LLM-based pairwise ranking supervision only when a trainable gating mechanism predicts the LLM to be reliable. This selective approach outperforms global distillation baselines and yields substantial gains in cold start and long tail regimes while avoiding the cost of forcing imitation of inaccurate LLM predictions.

### Theme 4: Efficiency and Architectural Innovation

Addressing the computational cost of LLM deployment, Zhou et al. (2025) developed a multi-head early exit architecture for RAG-enhanced LLM recommender systems. Their approach integrates Graph Convolutional Networks as efficient retrieval mechanisms and employs dynamic inference termination based on real-time predictive confidence assessments. Experiments demonstrated that this architecture decreases computation time without sacrificing accuracy, establishing a new standard for real-time LLM deployment in commercial recommender systems.

Kim et al. (2025) tackled efficiency from a different angle, proposing I-LLMRec which leverages images as alternatives to lengthy textual descriptions for item representation. Their key observation was significant information overlap between images and descriptions, allowing token usage reduction while preserving rich semantic information. I-LLMRec outperformed existing methods in both efficiency and effectiveness, with the additional benefit of reduced sensitivity to description noise.

Zheng et al. (2024) introduced LSVCR, a hybrid architecture combining a sequential recommendation model as the primary backbone with a supplemental LLM recommender for capturing underlying user preferences from heterogeneous interactions. Their two-stage training paradigm (personalized preference alignment followed by recommendation-oriented fine-tuning) achieved a 4.13% cumulative gain in comment watch time on KuaiShou platform, with the supplemental LLM discarded in deployment while retaining alignment benefits.

### Theme 5: Bias and Fairness Considerations

The question of whether LLMs exacerbate or alleviate bias in recommender systems has received attention. Lichtenberg et al. (2024) investigated popularity bias—the tendency to disproportionately recommend popular items—and found that LLM recommenders exhibit less popularity bias than traditional systems, even without explicit mitigation. This counterintuitive finding challenges concerns that LLM training data dominated by popular items would translate to biased recommendations. Their study introduced a principled popularity bias metric fulfilling specific desiderata and demonstrated that LLMs present opportunities to address bias via prompt tuning rather than exacerbating it.

However, this finding must be contextualized within the broader reliability challenges identified by other studies: reduced popularity bias does not necessarily imply improved overall recommendation quality if hallucination rates remain high.

## Convergences and Disagreements

**Convergences**: Multiple studies converge on the conclusion that evaluation methodology fundamentally shapes observed performance. Wang (2026), Aouali et al. (2026), and Suresh (2026) all demonstrate that prevailing evaluation protocols—whether oracle protocols, semantic plausibility metrics, or synthetic dialogue benchmarks—systematically overestimate real-world performance. There is strong agreement that behavior-grounded metrics and realistic retrieval conditions are essential for meaningful evaluation.

Researchers also converge on the importance of selective or conditional LLM deployment rather than wholesale replacement of traditional recommenders. Yang and Shi (2025), Zheng et al. (2024), and Wang (2026) all find that LLMs excel in specific regimes (cold start, long tail, re-ranking) but do not uniformly outperform collaborative filtering across all contexts.

**Disagreements**: While Lichtenberg et al. (2024) found LLMs reduce popularity bias, this finding appears somewhat isolated and has not been replicated across domains. The extent to which LLMs introduce or mitigate various forms of bias remains an open question requiring broader investigation across recommendation domains beyond movies.

Additionally, there is tension between studies emphasizing LLM capabilities (e.g., Zhou et al., 2025; Kim et al., 2025) and those highlighting fundamental limitations (Ravikumar, 2026; Wang, 2026). This likely reflects different deployment contexts: LLMs may provide value in specific niches (efficiency optimization, multimodal representation) while failing as general-purpose recommenders under realistic retrieval constraints.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature:

1. **Cross-domain validation**: Most studies focus on single domains (movies, music, e-commerce). Findings about hallucination rates, bias, and optimization strategies need validation across diverse recommendation contexts.

2. **Longitudinal deployment studies**: Nearly all evaluations are offline. The 4.13% improvement reported by Zheng et al. (2024) from KuaiShou A/B testing is an exception. More real-world deployment evidence is needed to understand how LLM recommenders perform under live traffic with feedback loops.

3. **Calibration improvement methods**: Ravikumar (2026) identifies poor confidence calibration but offers limited solutions beyond catalog-anchored elicitation. Developing effective calibration methods remains an open challenge.

4. **Retrieval-recall improvement**: Wang (2026) emphasizes that improving retrieval is more consequential than reranker sophistication in low-recall regimes, but does not provide solutions for achieving higher recall. This represents a critical infrastructure gap.

5. **Privacy and security**: None of the surveyed papers address privacy implications of LLM recommenders, including potential leakage of user data through model outputs or vulnerabilities to adversarial attacks.

6. **Computational cost transparency**: While efficiency is mentioned in several papers, detailed computational cost analysis (training FLOPs, inference latency, carbon footprint) is largely absent, making it difficult to assess practical deployment feasibility.

## Per-Paper Annotations

### Aouali et al. (2026)

**Research question**: How can we properly evaluate LLM recommendation agents that produce structured recommendation reports with natural-language justifications beyond semantic plausibility?

**Methodology**: Introduced RecoAtlas benchmark complementing held-out interaction metrics with learned utility proxies for relevance, complementarity, and diversity derived from interaction data, while separately measuring semantic coherence and explanation quality in a controlled tool environment.

**Key findings**:
- Performance scales with model capacity and test-time compute
- Performance improves with stronger and better-aligned tools
- Performance degrades under noisy or misaligned signals
- Semantic plausibility does not necessarily capture behavior-grounded utility
- Controlled tool environment enables diagnosis of whether performance gains arise from stronger reasoning, better signals, or more effective tool-use policies

**Limitations**: Focus on shopping agents; learned utility proxies derived from interaction data may not generalize to all recommendation domains.

### Kim et al. (2025)

**Research question**: How can we address the trade-off between efficiency and effectiveness in representing items for LLM-based recommender systems?

**Methodology**: Proposed I-LLMRec leveraging images as alternatives to lengthy textual descriptions for representing items, aiming to reduce token usage while preserving rich semantic information, with extensive experiments comparing against attribute-based and description-based representations.

**Key findings**:
- Significant information overlap exists between images and descriptions associated with items
- I-LLMRec outperforms existing methods in both efficiency and effectiveness
- Reduces token usage while preserving rich semantic information of item descriptions
- More robust to noise in descriptions, leading to more robust recommendations

**Limitations**: Requires image availability for items; may not work for text-only catalogs or items without visual representations.

### Lichtenberg et al. (2024)

**Research question**: Do Large Language Models contribute to or can they alleviate popularity bias in recommender systems?

**Methodology**: Introduced a principled approach to measure popularity bias by discussing existing metrics and proposing a novel metric fulfilling specific desiderata, then comparing a simple LLM-based recommender to traditional systems on a movie recommendation task.

**Key findings**:
- The LLM recommender exhibits less popularity bias than traditional recommender systems, even without any explicit mitigation
- The proposed novel popularity bias metric fulfills a series of desiderata for principled measurement
- LLM integration presents an opportunity to address popularity bias via prompt tuning rather than exacerbating it
- LLM training data dominance by popular items does not necessarily translate to biased recommendations

**Limitations**: The study is limited to a movie recommendation task; findings may not generalize to other domains or more complex LLM-based recommender architectures.

### Ravikumar (2026)

**Research question**: Do LLM recommenders know when they're hallucinating by producing items outside the target catalog?

**Methodology**: Jointly audit hallucination rate (OOD@10) and verbalized-confidence calibration (ECE, Brier, reliability) for four zero-shot LLM recommenders from independent vendors across three catalogs, stratified by item popularity, with validation against 201 human judgments.

**Key findings**:
- Hallucination rates are strongly catalog-dependent: 0.6-2.7% on MovieLens, 11.6-38.7% on Yelp, 49.3-61.0% on Amazon Toys
- Models maintain near-constant confidence levels barely responsive to catalog changes, while catalog-hit rates swing 60 points
- 7 of 12 model-catalog cells are under-confident and 5 over-confident, with all four models under-confident on MovieLens and over-confident on Amazon Toys
- String matching method significantly affects reported hallucination rates, with adopted matcher off by -0.040 vs +0.144 for common fuzzy rule
- Conformal abstention threshold over verbalized confidence changes hallucination by at most 1.65 percentage points because the channel cannot separate correct items from hallucinations

**Limitations**: Only tested zero-shot models without grounding or fine-tuning; verbalized confidence elicitation produces generic quality ratings rather than catalog-membership probabilities.

### Shi et al. (2026)

**Research question**: Why do beam-search negatives outperform random negatives in RL-based LLM recommenders, and how can objectives be better aligned with Top-K metrics?

**Methodology**: Theoretical analysis showing GRPO with binary rewards equals AUC maximization, then introducing Windowed Partial AUC (WPAUC) constraining false positive rate to a window, optimized via Threshold-Adjusted Windowed reweighting (TAWin) RL method.

**Key findings**:
- Under binary reward feedback, optimizing LLM recommenders with GRPO is theoretically equivalent to maximizing Area Under the ROC Curve (AUC)
- Replacing random negatives with beam-search negatives reshapes the objective toward partial AUC, improving alignment with Top-K metrics
- WPAUC constrains false positive rate to window [α,α+d] to more directly align with Top-K metrics
- TAWin method enables explicit control over targeted Top-K performance
- Experiments on four real-world datasets validate the theory and deliver consistent state-of-the-art performance

**Limitations**: Focus limited to RL-based recommenders; theoretical analysis assumes binary reward feedback which may not hold in all practical scenarios.

### Suresh (2026)

**Research question**: Do policy-selected labels in synthetic conversational music recommendation benchmarks accurately reflect what the simulated user requested?

**Methodology**: Audited the RecSys Challenge 2026 TalkPlay benchmark by examining turns where the user asks for an exact song by name, using visible dialogue and catalog metadata to identify label-request contradictions, then tested a training-time supplement adding catalog-resolved request-satisfying targets.

**Key findings**:
- Official labels contradict the user's exact-song request in half of the audited development turns
- Adding catalog-resolved request-satisfying targets to a small fraction of training turns yields a 53.3% relative gain in nDCG@20 on conflict turns
- The improvement is verified against a matched control that detects the same requests but trains only on official labels
- Naming the desired item is the dominant intent in real music search, making label-request alignment critical for user satisfaction

**Limitations**: The audit focuses on only one benchmark (RecSys Challenge 2026 TalkPlay) and specifically on exact-song request turns; findings may not generalize to other conversational recommendation scenarios or intent types.

### Wang (2026)

**Research question**: Why do oracle evaluation protocols overestimate LLM reranker performance, and what is the realistic recall ceiling for closed-candidate reranking?

**Methodology**: Analyzed recall across three primary Amazon datasets and eight datasets in three domains under realistic retrieval versus oracle protocols, tested multiple optimization strategies, and proposed the Recall-Aware Evaluation Protocol (RAEP) to classify retrieval-recall regimes before evaluating reranking.

**Key findings**:
- Oracle protocol overestimates realistic NDCG@10 by 92-95% across three primary Amazon datasets
- Realistic retrieval covers only 2-19% of relevant items at K=100, imposing a deterministic upper bound on any closed-candidate reranker's top-k NDCG
- None of the tested optimization strategies (prompt engineering, model scaling over 168× parameter range, sequential models, supervised neural rerankers, LoRA fine-tuning, hybrid retrieval, score-aware prompting, LLM+CF fusion) significantly improve over collaborative-filtering baseline under realistic retrieval
- Text-aware retrieval increases recall on one dataset but does not improve end-to-end NDCG
- In low-recall regimes, improving retrieval is more consequential than increasing reranker sophistication

**Limitations**: Findings may not hold in production systems with higher recall, richer features, or online feedback; the ordering of retrieval importance over reranker sophistication need not hold in all deployment scenarios.

### Yang and Shi (2025)

**Research question**: How can LLMs be leveraged to enhance recommendation models without the costs and drawbacks of standalone LLM recommenders or global knowledge distillation?

**Methodology**: Introduced Selective LLM-Guided Regularization, a model-agnostic framework that activates LLM-based pairwise ranking supervision only when a trainable gating mechanism (informed by user history length, item popularity, and model uncertainty) predicts the LLM to be reliable, with all LLM scoring performed offline.

**Key findings**:
- Selective activation strategy consistently improves overall accuracy across multiple datasets
- Substantial gains are achieved in cold start and long tail regimes where LLM guidance is most reliable
- The approach outperforms global distillation baselines while avoiding forcing imitation of inaccurate LLM predictions
- Offline LLM scoring transfers knowledge without increasing inference cost
- The framework is model-agnostic and computation efficient

**Limitations**: Requires offline LLM scoring infrastructure; the gating mechanism's effectiveness depends on the quality of features (user history length, item popularity, model uncertainty) used to predict LLM reliability.

### Zheng et al. (2024)

**Research question**: How can we leverage both video and comment interaction histories to improve personalized recommendations on online video platforms?

**Methodology**: Proposed LSVCR combining a sequential recommendation model as primary backbone with a supplemental LLM recommender, using two-stage training: personalized preference alignment followed by recommendation-oriented fine-tuning.

**Key findings**:
- LSVCR effectively integrates video and comment interactions for joint personalized recommendation
- Two-stage training paradigm enhances semantics of the SR model through preference alignment
- Online A/B testing on KuaiShou platform attains 4.13% cumulative gain in comment watch time
- Supplemental LLM recommender can be discarded in deployment while retaining alignment benefits

**Limitations**: Tested primarily on video platforms; adding LLM component increases training complexity despite being discarded in deployment.

### Zhou et al. (2025)

**Research question**: How can Large Language Models in recommender systems balance computational efficiency with predictive accuracy for Click-Through Rate prediction?

**Methodology**: Presented an optimization framework combining Retrieval-Augmented Generation with a multi-head early exit architecture, using Graph Convolutional Networks for efficient retrieval and dynamic inference termination based on real-time predictive confidence assessments.

**Key findings**:
- GCNs as retrieval mechanisms significantly reduce data retrieval times while maintaining high model performance
- Multi-head early exit strategy dynamically terminates inference, quickening LLM responsiveness without sacrificing accuracy
- The architecture effectively decreases computation time while upholding or improving accuracy for reliable recommendations
- The approach establishes a new standard for efficient, real-time LLM deployment in commercial recommender systems

**Limitations**: The abstract does not explicitly acknowledge limitations; the approach may be specific to CTR prediction scenarios and requires confidence assessment infrastructure across multiple heads.

## References

Aouali, I., Vasile, F., Sakhi, O., Gilotte, A., & Heymann, B. (2026). RecoAtlas: From semantic plausibility to set-level utility in LLM recommendation agents. arXiv. https://arxiv.org/abs/2605.18805

Kim, K., Kim, S., Kang, H., Kim, J., Noh, H., In, Y., Yoon, K., Oh, J., McAuley, J., & Park, C. (2025). Token-efficient item representation via images for LLM recommender systems. arXiv. https://arxiv.org/abs/2503.06238

Lichtenberg, J. M., Buchholz, A., & Schwöbel, P. (2024). Large language models as recommender systems: A study of popularity bias. arXiv. https://arxiv.org/abs/2406.01285

Ravikumar, S. (2026). Do LLM recommenders know when they're hallucinating? Auditing confidence calibration in catalog faithfulness. arXiv. https://arxiv.org/abs/2608.10008

Shi, W., Wang, Q., Chen, C., Liu, F., Liu, D., Liu, X., Ma, W., Pan, J., Zhu, L., & Feng, F. (2026). Objective shaping with hard negatives: Windowed partial AUC optimization for RL-based LLM recommenders. arXiv. https://arxiv.org/abs/2604.22504

Suresh, S. (2026). When the label ignores the request: Auditing policy-selected targets in synthetic conversational music recommendation. arXiv. https://arxiv.org/abs/2609.39696

Wang, Z. (2026). The recall ceiling of LLM recommendation reranking. arXiv. https://arxiv.org/abs/2609.27953

Yang, S., & Shi, Z. (2025). Selective LLM-guided regularization for enhancing recommendation models. arXiv. https://arxiv.org/abs/2512.21526

Zheng, B., Lin, Z., Liu, E., Yang, C., Bai, E., Ling, C., Zhao, W. X., & Wen, J.-R. (2024). Enhancing sequential recommender with large language models for joint video and comment recommendation. arXiv. https://arxiv.org/abs/2403.13574

Zhou, H., Gu, H., Liu, X., Zhou, K., Liang, M., Xiao, Y., Govindan, S., Chawla, P., Yang, J., Meng, X., Li, H., Zhang, B., Luo, L., Chen, W.-Y., Han, Y., Long, B., Zhang, R., & Chen, T. (2025). The efficiency vs. accuracy trade-off: Optimizing RAG-enhanced LLM recommender systems using multi-head early exit. arXiv. https://arxiv.org/abs/2501.02173
