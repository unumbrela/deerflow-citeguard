# Systematic Literature Review: LLM-Based Recommender Systems

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "LLM recommender", filtered to category cs.IR, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM-based recommender systems from 2024-2026 reveals a field rapidly maturing from initial enthusiasm to critical examination. The surveyed papers collectively demonstrate that while LLMs offer powerful semantic understanding and reasoning capabilities for recommendation, significant challenges remain in hallucination control, evaluation validity, computational efficiency, and bias mitigation. Researchers are increasingly moving beyond simple LLM-as-recommender approaches toward hybrid architectures that combine LLMs with traditional collaborative filtering, selective activation strategies, and behavior-grounded evaluation frameworks. A notable shift is evident from purely semantic evaluation toward metrics that capture real user utility and catalog faithfulness.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "LLM recommender", filtered to category cs.IR, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Hallucination and Catalog Faithfulness

A critical challenge emerging in LLM-based recommendation is the tendency of models to hallucinate items outside the target catalog. Ravikumar (2026) conducted a comprehensive audit of four zero-shot LLM recommenders across three catalogs, finding hallucination rates ranging from 0.6-2.7% on MovieLens to 49.3-61.0% on Amazon Toys. The study revealed that models maintain near-constant confidence levels regardless of catalog, creating a dangerous mismatch between verbalized confidence and actual accuracy. This work established that catalog membership measurement itself is highly sensitive to the string matching methodology used, with reported rates varying by an order of magnitude depending on the instrument.

The hallucination problem is particularly acute in conversational recommendation settings. Suresh (2026) audited the RecSys Challenge 2026 TalkPlay benchmark and found that official labels contradict user exact-song requests in half of audited turns. This reveals a fundamental misalignment between synthetic evaluation protocols and real user intent, where naming the desired item is the dominant intent in music search. The proposed solution—adding catalog-resolved request-satisfying targets to a small fraction of training turns—yielded a 53.3% relative gain in nDCG@20 on conflict turns, demonstrating that targeted training interventions can substantially reduce hallucination-related failures.

### Theme 2: Evaluation Methodologies and Benchmarks

The field is experiencing a paradigm shift from semantic plausibility to behavior-grounded utility in evaluation. Aouali et al. (2026) introduced RecoAtlas, a benchmark that complements held-out interaction metrics with learned utility proxies for relevance, complementarity, and diversity derived from interaction data. Their controlled tool environment exposes agents to semantic, behavior-aligned, or faulty tools, enabling diagnosis of whether performance gains arise from stronger reasoning, better signals, or more effective tool-use policies. Critically, they demonstrated that semantic plausibility does not necessarily capture behavior-grounded utility, challenging the field's reliance on surface-level evaluation metrics.

Wang (2026) exposed a fundamental flaw in LLM reranker evaluation protocols, showing that oracle protocols (which guarantee the ground-truth item is present in the scored set) overestimate realistic NDCG@10 by 92-95%. The root cause is a "recall ceiling": realistic retrieval covers only 2-19% of relevant items at K=100 across eight datasets in three domains. Under realistic retrieval conditions, none of the tested optimization strategies—including prompt engineering, model scaling over a 168× parameter range, sequential models, supervised neural rerankers, LoRA fine-tuning, hybrid retrieval, score-aware prompting, and LLM+CF fusion—significantly improved over the collaborative-filtering baseline. This work proposes the Recall-Aware Evaluation Protocol (RAEP), which first classifies the retrieval-recall regime before evaluating reranking, establishing that in low-recall regimes, improving retrieval is more consequential than increasing reranker sophistication.

### Theme 3: Efficiency and Optimization

Computational efficiency remains a central concern for deploying LLM recommenders in production settings. Zhou et al. (2025) presented an optimization framework combining Retrieval-Augmented Generation (RAG) with a multi-head early exit architecture to balance computational efficiency and predictive accuracy for CTR prediction. By integrating Graph Convolutional Networks as efficient retrieval mechanisms and employing dynamic termination of model inference based on real-time predictive confidence assessments, their approach decreased computation time without sacrificing accuracy. This work established a new standard for efficient, real-time LLM deployment in commercial recommender systems.

Kim et al. (2025) addressed the efficiency-accuracy trade-off from a different angle, proposing I-LLMRec, which leverages images as alternatives to lengthy textual descriptions for item representation. Based on the observation of significant information overlap between images and descriptions, this method reduces token usage while preserving rich semantic information. Their experiments demonstrated that I-LLMRec outperforms existing attribute-based and description-based representation methods in both efficiency and effectiveness, while also reducing sensitivity to noise in descriptions.

Shi et al. (2026) provided theoretical insights into why beam-search negatives consistently outperform random negatives in RL-based LLM recommenders. They showed that under binary reward feedback, optimizing LLM recommenders with Group Relative Policy Optimization (GRPO) is theoretically equivalent to maximizing AUC, which is often misaligned with Top-K recommendation. Replacing random negatives with beam-search negatives reshapes the objective toward partial AUC, improving alignment with Top-K metrics. Their proposed Windowed Partial AUC (WPAUC) method, which constrains the false positive rate to a window [α,α+d], combined with Threshold-Adjusted Windowed reweighting (TAWin), delivered consistent state-of-the-art performance on four real-world datasets.

### Theme 4: Bias and Fairness

Popularity bias—where popular items are disproportionately recommended—remains a significant challenge in recommender systems, and the integration of LLMs raises concerns about exacerbation. Lichtenberg et al. (2024) explored whether LLMs contribute to or can alleviate popularity bias, introducing a principled metric for measuring popularity bias that fulfills a series of desiderata. Contrary to concerns that LLM training data dominated by popular items would worsen bias, they found that a simple LLM-based recommender exhibited less popularity bias than traditional recommender systems on a movie recommendation task, even without explicit mitigation. This surprising finding suggests that LLMs' broader knowledge may actually help surface less popular but relevant items.

Yang and Shi (2025) addressed bias through their Selective LLM-Guided Regularization framework, which activates LLM-based pairwise ranking supervision only when a trainable gating mechanism predicts the LLM to be reliable. Their gating mechanism considers user history length, item popularity, and model uncertainty, ensuring that LLM guidance is applied selectively rather than globally. This approach yielded substantial gains in cold start and long tail regimes, outperforming global distillation baselines. By performing all LLM scoring offline, the framework transfers knowledge without increasing inference cost, making it practical for production deployment.

### Theme 5: Integration Strategies with Traditional Recommenders

Rather than replacing traditional recommenders entirely, recent work emphasizes strategic integration of LLMs with established collaborative filtering approaches. Zheng et al. (2024) proposed LSVCR, which combines a sequential recommendation model as the primary backbone with a supplemental LLM recommender. The LLM is used during training to capture underlying user preferences from heterogeneous interaction behaviors but is discarded in deployment, retaining only the efficiency of the sequential model. Their two-stage training paradigm—personalized preference alignment followed by recommendation-oriented fine-tuning—achieved a 4.13% cumulative gain in comment watch time in online A/B testing on the KuaiShou platform.

This hybrid approach reflects a broader trend in the literature toward pragmatic integration rather than wholesale replacement. The recall ceiling findings by Wang (2026) further support this strategy, showing that improving retrieval (typically handled by collaborative filtering) is more consequential than increasing reranker sophistication in low-recall regimes. Similarly, the selective activation strategy proposed by Yang and Shi (2025) recognizes that LLMs excel particularly in challenging scenarios rather than uniformly across all contexts, advocating for targeted deployment rather than blanket application.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that pure LLM-based recommendation faces significant challenges in production deployment. Multiple studies converge on the need for behavior-grounded evaluation rather than semantic plausibility (Aouali et al., 2026; Wang, 2026), the importance of addressing hallucination through catalog-anchored approaches (Ravikumar, 2026; Suresh, 2026), and the value of hybrid architectures combining LLMs with traditional methods (Zheng et al., 2024; Yang & Shi, 2025). There is also broad agreement that efficiency considerations must be central to LLM recommender design, not an afterthought (Zhou et al., 2025; Kim et al., 2025).

**Disagreements**: The literature shows some tension regarding the role of LLMs in recommendation. While Lichtenberg et al. (2024) found that LLMs naturally exhibit less popularity bias without mitigation, Yang and Shi (2025) observed that standalone LLM recommenders are costly, biased, and unreliable across large regions of the user-item space, requiring selective activation. These seemingly contradictory findings may reflect differences in domains (movie recommendation vs. broader e-commerce) or LLM architectures (simple prompting vs. fine-tuned systems). Additionally, Wang's (2026) finding that advanced optimization strategies fail under realistic retrieval contrasts with Shi et al.'s (2026) reported state-of-the-art results, though the latter may have benefited from more favorable retrieval conditions.

## Gaps and Open Questions

Several significant gaps emerge from the collective limitations acknowledged in the surveyed literature:

1. **Domain specificity**: Most studies validate their approaches on specific domains (movies, music, shopping), with limited cross-domain generalization. The hallucination rates, bias characteristics, and optimal integration strategies may vary substantially across domains, yet systematic comparisons are lacking.

2. **Real-time vs. offline trade-offs**: While several papers propose offline LLM scoring to reduce inference costs (Yang & Shi, 2025; Zheng et al., 2024), the field lacks clear guidance on when offline knowledge transfer suffices versus when real-time LLM reasoning is necessary.

3. **User experience validation**: Despite calls for behavior-grounded evaluation, most studies still rely on offline metrics (NDCG, CTR) rather than direct user satisfaction measures. The connection between improved offline metrics and actual user experience remains underexplored.

4. **Scalability to large catalogs**: Most experiments use relatively small catalogs (MovieLens-25M, Amazon subsets), yet production systems operate on catalogs with millions or billions of items. The scalability of proposed hallucination detection, selective activation, and evaluation frameworks to industrial-scale catalogs is unclear.

5. **Longitudinal effects**: The literature lacks studies on how LLM recommenders affect user behavior and preference evolution over time. Short-term gains in engagement metrics may mask long-term effects on user satisfaction, filter bubbles, or preference manipulation.

## Per-Paper Annotations

### Aouali et al. (2026)

**Research question**: How can LLM recommendation agents be evaluated beyond semantic plausibility to measure behavior-grounded set-level utility?

**Methodology**: Introduced RecoAtlas benchmark with behavior-grounded metrics for relevance, complementarity, and diversity derived from interaction data, using a controlled tool environment that exposes agents to semantic, behavior-aligned, or faulty tools.

**Key findings**:
- Performance scales with model capacity and test-time compute
- Agent performance improves with stronger and better-aligned tools
- Performance degrades under noisy or misaligned signals
- Semantic plausibility does not necessarily capture behavior-grounded utility
- The benchmark successfully diagnoses whether performance gains arise from stronger reasoning, better signals, or more effective tool-use policies

**Limitations**: Benchmark focuses specifically on shopping agents and requires interaction data to derive learned utility proxies, which may not be available in all domains.

### Kim et al. (2025)

**Research question**: How can the trade-off between efficiency and effectiveness in item representation for LLM recommenders be addressed?

**Methodology**: Proposed I-LLMRec leveraging images as alternatives to lengthy textual descriptions for item representation, based on the observation of significant information overlap between images and descriptions, aiming to reduce token usage while preserving semantic information.

**Key findings**:
- I-LLMRec outperforms existing attribute-based and description-based representation methods in both efficiency and effectiveness
- Using images significantly reduces token usage compared to textual descriptions
- The method reduces sensitivity to noise in descriptions, leading to more robust recommendations
- Images preserve rich semantic information comparable to lengthy text descriptions
- The approach addresses the efficiency-effectiveness trade-off inherent in existing representation approaches

**Limitations**: Method requires items to have associated images, limiting applicability to domains where visual representations are unavailable or irrelevant.

### Lichtenberg et al. (2024)

**Research question**: Do Large Language Models contribute to or can they alleviate popularity bias in recommender systems?

**Methodology**: Introduced a principled way to measure popularity bias by discussing existing metrics and proposing a novel metric fulfilling specific desiderata, then compared a simple LLM-based recommender to traditional recommender systems on a movie recommendation task.

**Key findings**:
- The LLM recommender exhibits less popularity bias than traditional recommender systems, even without explicit mitigation
- LLM integration presents a novel opportunity to address popularity bias via prompt tuning
- The proposed novel metric fulfills a series of desiderata for measuring popularity bias
- Contrary to concerns, LLM training data dominance by popular items does not necessarily exacerbate popularity bias in recommendations

**Limitations**: The study is limited to a movie recommendation task and a simple LLM-based recommender; findings may not generalize to other domains, more complex LLM architectures, or real-world production systems with different user behavior patterns.

### Ravikumar (2026)

**Research question**: Do LLM recommender systems know when they're hallucinating by recommending items outside their target catalog?

**Methodology**: Jointly audit hallucination rate (OOD@10) and verbalized-confidence calibration (ECE, Brier, reliability) for four zero-shot LLM recommenders across three catalogs, validating the catalog membership instrument against 201 human judgments.

**Key findings**:
- Hallucination rates are strongly catalog-dependent, ranging from 0.6-2.7% on MovieLens to 49.3-61.0% on Amazon Toys
- Models maintain near-constant confidence levels barely responsive to catalog, while catalog-hit rates swing 60 points
- 7 of 12 model-catalog combinations are under-confident and 5 over-confident, with all four models under-confident on MovieLens and over-confident on Amazon Toys
- Conformal abstention thresholds over verbalized confidence change hallucination by at most 1.65 percentage points because the channel cannot separate correct items from hallucinations
- Catalog membership measurement is highly sensitive to the string matcher used, with reported rates varying by an order of magnitude

**Limitations**: Study focuses only on zero-shot LLM recommenders without grounding or fine-tuning, and catalog membership validation remains challenging with fuzzy matching introducing bias.

### Shi et al. (2026)

**Research question**: Why do beam-search negatives outperform random negatives in RL-based LLM recommenders, and how can optimization objectives be better aligned with Top-K recommendation metrics?

**Methodology**: Theoretical analysis showing GRPO with binary rewards equals AUC maximization, then propose Windowed Partial AUC (WPAUC) constraining false positive rate to a window, with efficient Threshold-Adjusted Windowed reweighting (TAWin) RL method.

**Key findings**:
- Under binary reward feedback, optimizing LLM recommenders with GRPO is theoretically equivalent to maximizing AUC, which is often misaligned with Top-K recommendation
- Replacing random negatives with beam-search negatives reshapes the objective toward partial AUC, improving alignment with Top-K metrics
- Windowed Partial AUC constraining FPR to [α,α+d] more directly aligns with Top-K performance
- TAWin method enables explicit control over targeted Top-K performance
- Experiments on four real-world datasets validate the theory and deliver consistent state-of-the-art performance

**Limitations**: Theoretical analysis assumes binary reward feedback, and the approach is specifically designed for RL-based recommenders rather than other recommendation paradigms.

### Suresh (2026)

**Research question**: How often do official labels in synthetic conversational recommendation benchmarks contradict the user's actual request, particularly for exact-song requests?

**Methodology**: Audited the RecSys Challenge 2026 TalkPlay benchmark by examining turns where users ask for exact songs by name, comparing official labels to user requests using visible dialogue and catalog metadata, and tested a training-time supplement adding catalog-resolved request-satisfying targets to a small fraction of training turns.

**Key findings**:
- Official labels contradict the user's exact-song request in half of the audited development turns
- Naming the desired item is the dominant intent in real music search
- Adding catalog-resolved request-satisfying targets to a small fraction of training turns yields a 53.3% relative gain in nDCG@20 on the 43 conflict turns
- The improvement is verified against a matched control that detects the same requests but trains only on official labels
- The issue matters beyond one benchmark as deployed systems avoid substituting alternatives for exactly named items

**Limitations**: The audit focuses only on exact-song request turns (a subset of all conversation turns), and the training supplement was tested on a limited number of conflict turns (43 development turns); results may not generalize to other types of user requests or larger-scale deployments.

### Wang (2026)

**Research question**: How does the oracle evaluation protocol affect measured performance of LLM-based recommendation rerankers, and what is the realistic upper bound on reranking performance given retrieval limitations?

**Methodology**: Analyzed three primary Amazon datasets to demonstrate oracle protocol overestimation, examined recall across eight datasets in three domains, tested multiple optimization strategies (prompt engineering, model scaling over 168× parameter range, sequential models, supervised neural rerankers, LoRA fine-tuning, hybrid retrieval, score-aware prompting, and LLM+CF fusion), and proposed the Recall-Aware Evaluation Protocol (RAEP).

**Key findings**:
- Oracle protocol overestimates realistic NDCG@10 by 92-95%
- Realistic retrieval covers only 2-19% of relevant items at K=100 across eight datasets in three domains, imposing a deterministic upper bound on reranker performance
- None of the tested optimization strategies significantly improves over the collaborative-filtering baseline under realistic retrieval
- Text-aware retrieval increases recall on one dataset but does not improve end-to-end NDCG
- Providing upstream CF scores mainly makes the LLM reproduce the CF order rather than improve recommendations
- In low-recall regimes, improving retrieval is more consequential than increasing reranker sophistication

**Limitations**: The author explicitly acknowledges that findings are specific to the evaluated datasets and may not hold in production systems with higher recall, richer features, or online feedback; the proposed RAEP requires classification of retrieval-recall regimes which may add evaluation complexity.

### Yang and Shi (2025)

**Research question**: How can LLMs be leveraged to improve recommendation models without incurring the costs and reliability issues of standalone LLM recommenders or global knowledge distillation?

**Methodology**: Introduced Selective LLM-Guided Regularization, a model-agnostic framework that activates LLM-based pairwise ranking supervision only when a trainable gating mechanism (informed by user history length, item popularity, and model uncertainty) predicts the LLM to be reliable, with all LLM scoring performed offline.

**Key findings**:
- The selective strategy consistently improves overall accuracy across multiple datasets
- Substantial gains are achieved in cold start and long tail regimes
- The approach outperforms global distillation baselines
- The framework is model-agnostic and computation efficient
- Knowledge transfer occurs without increasing inference cost since all LLM scoring is performed offline

**Limitations**: The approach requires offline LLM scoring infrastructure, and the gating mechanism's effectiveness depends on the quality of its input signals (user history length, item popularity, and model uncertainty estimates); performance may vary in scenarios where these signals are unreliable or unavailable.

### Zheng et al. (2024)

**Research question**: How can user interactions with both videos and comments be jointly modeled for personalized video and comment recommendation?

**Methodology**: Proposed LSVCR combining a sequential recommendation model as primary backbone with a supplemental LLM recommender, using two-stage training: personalized preference alignment followed by recommendation-oriented fine-tuning.

**Key findings**:
- LSVCR effectively performs joint video and comment recommendation by modeling heterogeneous interaction behaviors
- The two-stage training paradigm successfully aligns preference representations from SR and LLM components
- Online A/B testing on KuaiShou platform verified practical benefits with 4.13% cumulative gain in comment watch time
- The SR model retains deployment efficiency while the supplemental LLM is discarded after training
- Extensive experiments demonstrate effectiveness on both video and comment recommendation tasks

**Limitations**: The supplemental LLM recommender is discarded in deployment, limiting real-time LLM inference benefits, and validation was platform-specific on KuaiShou.

### Zhou et al. (2025)

**Research question**: How can Large Language Models be deployed in recommender systems for CTR prediction while balancing computational efficiency and predictive accuracy?

**Methodology**: Presented an optimization framework combining Retrieval-Augmented Generation (RAG) with a multi-head early exit architecture, using Graph Convolutional Networks (GCNs) as efficient retrieval mechanisms and dynamic termination of model inference based on real-time predictive confidence assessments across multiple heads.

**Key findings**:
- GCNs significantly reduce data retrieval times while maintaining high model performance
- The early exit strategy quickens LLM responsiveness while upholding or improving accuracy
- The architecture decreases computation time without sacrificing accuracy needed for reliable recommendations
- The approach is ideal for real-time application scenarios in commercial systems

**Limitations**: The abstract does not explicitly acknowledge limitations; the approach appears focused on CTR prediction specifically and may not generalize to all recommendation scenarios or address the computational cost of training the multi-head architecture.

## References

Aouali, I., Vasile, F., Sakhi, O., Gilotte, A., & Heymann, B. (2026). RecoAtlas: From semantic plausibility to set-level utility in LLM recommendation agents. arXiv. https://arxiv.org/abs/2605.18805

Kim, K., Kim, S., Kang, H., Kim, J., Noh, H., In, Y., Yoon, K., Oh, J., McAuley, J., & Park, C. (2025). Token-efficient item representation via images for LLM recommender systems. arXiv. https://arxiv.org/abs/2503.06238

Lichtenberg, J. M., Buchholz, A., & Schwöbel, P. (2024). Large Language Models as Recommender Systems: A Study of Popularity Bias. arXiv. https://arxiv.org/abs/2406.01285

Ravikumar, S. (2026). Do LLM Recommenders Know When They're Hallucinating? Auditing Confidence Calibration in Catalog Faithfulness. arXiv. https://arxiv.org/abs/2608.10008

Shi, W., Wang, Q., Chen, C., Liu, F., Liu, D., Liu, X., Ma, W., Pan, J., Zhu, L., & Feng, F. (2026). Objective Shaping with Hard Negatives: Windowed Partial AUC Optimization for RL-based LLM Recommenders. arXiv. https://arxiv.org/abs/2604.22504

Suresh, S. (2026). When the Label Ignores the Request: Auditing Policy-Selected Targets in Synthetic Conversational Music Recommendation. arXiv. https://arxiv.org/abs/2609.39696

Wang, Z. (2026). The Recall Ceiling of LLM Recommendation Reranking. arXiv. https://arxiv.org/abs/2609.27953

Yang, S., & Shi, Z. (2025). Selective LLM-Guided Regularization for Enhancing Recommendation Models. arXiv. https://arxiv.org/abs/2512.21526

Zheng, B., Lin, Z., Liu, E., Yang, C., Bai, E., Ling, C., Zhao, W. X., & Wen, J.-R. (2024). Enhancing Sequential Recommender with Large Language Models for Joint Video and Comment Recommendation. arXiv. https://arxiv.org/abs/2403.13574

Zhou, H., Gu, H., Liu, X., Zhou, K., Liang, M., Xiao, Y., Govindan, S., Chawla, P., Yang, J., Meng, X., Li, H., Zhang, B., Luo, L., Chen, W.-Y., Han, Y., Long, B., Zhang, R., & Chen, T. (2025). The Efficiency vs. Accuracy Trade-off: Optimizing RAG-Enhanced LLM Recommender Systems Using Multi-Head Early Exit. arXiv. https://arxiv.org/abs/2501.02173
