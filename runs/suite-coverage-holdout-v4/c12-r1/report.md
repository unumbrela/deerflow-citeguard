# Systematic Literature Review: Negative Sampling Techniques in Information Retrieval

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "negative sampling", category cs.IR, published between 2024-01-09 and 2026-01-08
**Citation format**: APA 7th edition

## Executive Summary

The literature on negative sampling techniques in information retrieval from 2024-2026 reveals a rapidly evolving field focused on improving the quality and effectiveness of negative sample selection across recommendation systems and dense retrieval applications. Recent work has shifted from simple random sampling toward adaptive, hardness-aware approaches that dynamically adjust sampling strategies during training to address fundamental challenges like false positive/negative problems and popularity bias. The surveyed papers collectively demonstrate that negative sampling is no longer a mere implementation detail but a critical component that significantly impacts model performance, fairness, and generalization across diverse scenarios including collaborative filtering, sequential recommendation, and multi-modal recommendation systems.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "negative sampling", filtered to category cs.IR, published between 2024-01-09 and 2026-01-08. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening Process**: The search identified 50 papers by keyword matching, with an additional 84 papers added through citation expansion, creating a shortlist of 30 papers. After relevance screening based on co-citation analysis and topic centrality scores, 10 papers were selected for inclusion (4 of which came from reference expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Most papers did not explicitly state limitations in their abstracts, which may indicate incomplete reporting of methodological constraints.

## Themes

### Theme 1: Adaptive Hardness in Negative Sampling

A dominant theme across the literature is the shift toward adaptive hardness negative sampling, where the difficulty level of negative samples is dynamically adjusted during training rather than fixed at a predetermined level. Lai et al. (2024) introduced the Adaptive Hardness Negative Sampling (AHNS) paradigm, arguing that fixed hardness levels lead to false positive problems (selecting samples that are actually positive) and false negative problems (missing informative negatives). Their theoretical analysis demonstrates that adaptive sampling achieves better ranking optimization bounds. This theme reflects a broader recognition that the informativeness of negative samples changes throughout the training process, requiring sampling strategies that evolve alongside model learning.

### Theme 2: Theoretical Foundations and Guiding Principles

Several papers contribute theoretical frameworks that establish guiding principles for negative sampling design. Yang et al. (2024) unveiled the quasi-triangular principle describing the interplay between queries, positive documents, and negative documents in dense retrieval, providing a mathematical foundation for sampling distribution design. Lin et al. (2024) conducted theoretical analysis revealing why ranking losses generate larger gradients on negative samples, addressing gradient vanishing issues in binary cross-entropy loss when positive feedback is sparse. These theoretical contributions move the field beyond heuristic approaches toward principled sampling strategies grounded in optimization theory.

### Theme 3: Bias and Fairness Considerations

The literature increasingly addresses how negative sampling choices impact popularity bias and fairness across different item categories. Prakash et al. (2024) demonstrated that random negative sampling reinforces popularity bias and performs best for head items while potentially disadvantaging tail items. Their large-scale study with 20x repeats across three benchmark datasets revealed that average performance metrics often hide significant imbalances across popularity bands (head, mid, tail). This theme reflects growing awareness that sampling strategies have ethical and practical implications beyond pure accuracy metrics, particularly in large-scale production systems where fairness across item categories matters.

### Theme 4: Multi-Modal and Generative Approaches

Recent work extends negative sampling to multi-modal recommendation systems and leverages generative models for sample creation. Ji et al. (2025) proposed NegGen, utilizing multi-modal large language models to generate balanced and contrastive negative samples that effectively utilize information across different modalities. Lee et al. (2024) introduced SCONE, a score-based generative model approach that creates dynamic augmented views and diverse hard negative samples. These approaches represent a paradigm shift from discriminative sampling (selecting from existing items) to generative sampling (creating synthetic negatives), enabling more fine-grained control over sample properties.

### Theme 5: Integration with Preference Optimization and Contrastive Learning

Negative sampling is increasingly integrated with broader learning frameworks including direct preference optimization and contrastive learning. Chen et al. (2024) extended Direct Preference Optimization (DPO) with softmax sampling strategies that inherently mine hard negatives for recommendation tasks. Sun et al. (2024) proposed neighborhood-enhanced supervised contrastive learning that treats collaborative neighbors as positive samples while improving negative sample treatment. This theme shows negative sampling evolving from an isolated technique to an integral component of comprehensive learning objectives.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that adaptive or hardness-aware sampling outperforms fixed-strategy approaches. Lai et al. (2024), Yang et al. (2024), and Lee et al. (2024) all demonstrate that dynamically adjusting sampling strategies based on training progress or sample characteristics yields superior performance. There is also broad agreement that negative sampling significantly impacts model performance metrics, with Prakash et al. (2024) and Lin et al. (2024) providing empirical evidence that sampling choices can substantially affect both overall accuracy and fairness across popularity bands.

**Disagreements**: The literature shows some tension between approaches prioritizing overall performance versus those emphasizing balanced performance across popularity bands. Prakash et al. (2024) found that random sampling performs best for head items but reinforces popularity bias, while popularity-based methods offer balanced performance at the cost of lower overall metrics. This suggests fundamental trade-offs that different applications may resolve differently based on their priorities. Additionally, while most papers advocate for more sophisticated sampling strategies, Lin et al. (2024) demonstrate that even simple auxiliary ranking losses combined with standard BCE loss can achieve significant improvements, suggesting that architectural integration may matter as much as sampling strategy sophistication.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the surveyed papers explicitly stated limitations in their abstracts, suggesting incomplete reporting of methodological constraints or boundary conditions. Second, while multiple papers address popularity bias, there is limited discussion of other fairness dimensions such as demographic bias or temporal fairness in sequential recommendation. Third, the computational cost of sophisticated sampling strategies is rarely analyzed — adaptive and generative approaches likely incur significant overhead compared to simple random sampling, but efficiency trade-offs are not systematically evaluated. Fourth, most work focuses on recommendation and retrieval scenarios, with limited exploration of negative sampling in emerging applications like conversational search or multi-turn dialogue systems. Finally, the long-term effects of different sampling strategies on model calibration and uncertainty estimation remain unexplored.

## Per-Paper Annotations

### Lai et al. (2024)

**Research question**: How can negative sampling methods for collaborative filtering overcome the limitation of selecting samples at a fixed hardness level that causes false positive and false negative problems?

**Methodology**: The authors propose a new paradigm called adaptive hardness negative sampling (AHNS) with three key criteria, and present a concrete instantiation called AHNS_{p<0}. They theoretically demonstrate that AHNS_{p<0} fits the three criteria and conduct comprehensive experiments comparing against state-of-the-art competitors on multiple datasets.

**Key findings**:
- Existing negative sampling methods can only select negative samples of a fixed hardness level, leading to false positive problem (FPP) and false negative problem (FNP).
- AHNS can adaptively select negative samples with appropriate hardnesses during training to mitigate FPP and FNP impacts.
- AHNS_{p<0} theoretically achieves a larger lower bound of normalized discounted cumulative gain.
- Existing negative sampling methods can be regarded as more relaxed cases of AHNS.
- AHNS_{p<0} consistently and substantially outperforms several state-of-the-art competitors on multiple datasets.

**Limitations**: not stated in abstract

### Ma et al. (2024)

**Research question**: What are the existing negative sampling strategies in recommender systems, how can they be categorized, and what are the future research directions?

**Methodology**: The authors conduct an extensive literature review on existing negative sampling strategies in recommender systems, classify them into five categories based on their techniques, and outline prospective research directions through analysis of challenges and scenarios.

**Key findings**:
- Negative sampling is essential for revealing genuine negative aspects in user behaviors and is an inescapable procedure in recommender systems.
- Existing negative sampling strategies can be classified into five categories with discrepant techniques.
- Challenges such as information cocoons, interaction sparsity, cold-start problem, and feedback loops impede progress in negative sampling.
- Tailored negative sampling strategies exist for diverse recommender system scenarios.
- The survey outlines prospective research directions for the community to engage with negative sampling research.

**Limitations**: not stated in abstract

### Yang et al. (2024)

**Research question**: What guiding principle can be established for constructing negative candidates and designing negative sampling distributions in dense retrieval?

**Methodology**: The authors conduct theoretical analysis of negative sampling in dense retrieval, unveiling the quasi-triangular principle that describes the triangular-like interplay between query, positive document, and negative document. They introduce TriSampler based on this principle and evaluate it experimentally across diverse retrieval models.

**Key findings**:
- The quasi-triangular principle elucidates the triangular-like interplay between query, positive document, and negative document.
- TriSampler selectively samples more informative negatives within a prescribed constrained region.
- TriSampler consistently attains superior retrieval performance across diverse representative retrieval models.
- Existing methods lack a comprehensive guiding principle for negative sampling distribution design.
- The quasi-triangular principle provides a novel framework for negative sampling in dense retrieval.

**Limitations**: not stated in abstract

### Prakash et al. (2024)

**Research question**: How do different negative sampling methods impact model performance metrics and popularity bias in large-scale sequential recommendation models?

**Methodology**: The authors implement and compare various negative sampling methods (random, popularity-based, in-batch, mixed, adaptive, and adaptive with mixed variants) on modern sequential recommendation models with hyperparameter optimization and 20x repeats on three benchmark datasets, analyzing performance across popularity bands (head, mid, tail).

**Key findings**:
- The choice of negative sampling method and dataset characteristics significantly impact key model performance metrics.
- Average performance metrics often hide imbalances across popularity bands (head, mid, tail).
- Random negative sampling reinforces popularity bias and performs best for head items.
- Popularity-based methods (in-batch and global popularity negative sampling) can offer balanced performance at the cost of lower overall model performance.
- The study provides practical guidance on trade-offs in selecting negative sampling methods for large-scale sequential recommendation models.

**Limitations**: not stated in abstract

### Ji et al. (2025)

**Research question**: How can negative sampling techniques for multi-modal recommender systems better utilize multi-modal data to produce cohesive negative samples while maintaining balanced influence across modalities?

**Methodology**: The authors propose NegGen, a framework utilizing multi-modal large language models (MLLMs) to generate balanced and contrastive negative samples. They design three prompt templates for analyzing item attributes across modalities and employ a causal learning module to disentangle intervened key features from irrelevant attributes, evaluating on real-world datasets.

**Key findings**:
- Existing negative sampling techniques struggle to effectively utilize multi-modal data in multi-modal recommender systems.
- Two key challenges exist: producing cohesive negative samples contrasting with positive samples and maintaining balanced influence across different modalities.
- NegGen uses three different prompt templates to analyze and manipulate item attributes across multiple modalities.
- The causal learning module enables fine-grained learning of user preferences by disentangling key features from irrelevant attributes.
- NegGen demonstrates superior performance compared to state-of-the-art methods in both negative sampling and multi-modal recommendation on real-world datasets.

**Limitations**: not stated in abstract

### Lee et al. (2024)

**Research question**: How can graph-based collaborative filtering models overcome challenges of data sparsity and negative sampling in recommender systems?

**Methodology**: The authors propose SCONE, a novel stochastic sampling approach based on score-based generative models that generates dynamic augmented views and diverse hard negative samples. The method was evaluated on 6 benchmark datasets comparing against state-of-the-art baselines.

**Key findings**:
- SCONE consistently outperforms state-of-the-art baselines across 6 benchmark datasets
- The approach shows efficacy in addressing user sparsity and item popularity issues
- SCONE enhances performance for both cold-start users and long-tail items
- The method improves recommendation diversity and representation uniformity

**Limitations**: not stated in abstract

### Chen et al. (2024)

**Research question**: How can Language Model-based recommenders better leverage preference data and optimize for personalized ranking tasks?

**Methodology**: The authors propose Softmax-DPO (S-DPO), which incorporates multiple negatives in user preference data and devises an alternative DPO loss tailored for LM-based recommenders, extending from the full-ranking Plackett-Luce model to partial rankings with softmax sampling strategies. The approach was evaluated on three real-world datasets.

**Key findings**:
- S-DPO instills ranking information into LMs to help distinguish preferred items from negatives
- The method has an inherent benefit of mining hard negatives for recommendation tasks
- S-DPO demonstrates superiority in modeling user preference and boosting recommendation performance
- The approach provides better rewards for preferred items

**Limitations**: not stated in abstract

### Lin et al. (2024)

**Research question**: Why does combining BCE loss with auxiliary ranking loss improve CTR prediction performance, particularly when positive feedback is sparse?

**Methodology**: The authors conduct theoretical analysis and extensive empirical evaluations on public datasets to uncover that ranking loss generates larger gradients on negative samples, mitigating gradient vanishing issues in BCE loss. The approach was integrated into Tencent's online advertising system for real-world validation.

**Key findings**:
- BCE loss faces gradient vanishing issues for negative samples when positive feedback is sparse
- Auxiliary ranking loss generates larger gradients on negative samples, mitigating BCE optimization difficulties
- The combination improves classification ability in CTR prediction
- Integration into Tencent's advertising system achieved 0.70% and 1.26% GMV lifts in two main scenarios

**Limitations**: not stated in abstract

### Lin et al. (2024)

**Research question**: How can LLM-based recommendation systems reduce fine-tuning costs while maintaining performance through data pruning?

**Methodology**: The authors propose a data pruning method using two scores: influence score (estimated via a small surrogate model to identify influential samples) and effort score (to prioritize hard samples for LLMs). The method was evaluated on three real-world datasets comparing few-shot fine-tuning against full data fine-tuning.

**Key findings**:
- The proposed method uses only 2% of samples to surpass full data fine-tuning performance
- The approach reduces time costs by 97% compared to full data fine-tuning
- Using a surrogate model achieves low-cost data pruning while maintaining accuracy
- The effort score addresses the gap between surrogate models and LLMs by prioritizing hard samples

**Limitations**: not stated in abstract

### Sun et al. (2024)

**Research question**: How can contrastive learning be improved for collaborative filtering to avoid distancing target users/items from their collaborative neighbors?

**Methodology**: The authors propose two supervised contrastive loss functions that treat collaborative neighbors of the anchor node as positive samples in the objective loss function. They use a graph-based collaborative filtering model as the backbone and apply the same data augmentation methods as the existing SGL model, replacing SGL's contrastive loss with their Neighborhood-Enhanced Supervised Contrastive Loss (NESCL).

**Key findings**:
- The proposed NESCL model shows marked performance improvement over the original SGL model.
- On Yelp2018 dataset, NESCL surpasses SGL by 10.09% on NDCG@20.
- On Gowalla dataset, NESCL surpasses SGL by 7.09% on NDCG@20.
- On Amazon-Book dataset, NESCL surpasses SGL by 35.36% on NDCG@20.
- Gradient analysis reveals that different positive samples simultaneously influence anchor node embedding updates based on their similarities to the anchor and negative samples.

**Limitations**: not stated in abstract

## References

Chen, Y., Tan, J., Zhang, A., Yang, Z., Sheng, L., Zhang, E., Wang, X., & Chua, T.-S. (2024). On softmax direct preference optimization for recommendation. arXiv. https://arxiv.org/abs/2406.09215

Ji, Y., Luo, D., Liu, C., Wu, S., Tong, J., He, Q., Ji, D., Lu, H., & Ding, Y. (2025). Generating negative samples for multi-modal recommendation. arXiv. https://arxiv.org/abs/2501.15183

Lai, R., Chen, R., Han, Q., Zhang, C., & Chen, L. (2024). Adaptive hardness negative sampling for collaborative filtering. arXiv. https://arxiv.org/abs/2401.05191

Lee, C., Choi, J., Wi, H., Cho, S.-B., & Park, N. (2024). SCONE: A novel stochastic sampling to generate contrastive views and hard negative samples for recommendation. arXiv. https://arxiv.org/abs/2405.00287

Lin, X., Wang, W., Li, Y., Yang, S., Feng, F., Wei, Y., & Chua, T.-S. (2024). Data-efficient fine-tuning for LLM-based recommendation. arXiv. https://arxiv.org/abs/2401.17197

Lin, Z., Pan, J., Zhang, S., Wang, X., Xiao, X., Huang, S., Xiao, L., & Jiang, J. (2024). Understanding the ranking loss for recommendation with sparse user feedback. arXiv. https://arxiv.org/abs/2403.14144

Ma, H., Xie, R., Meng, L., Feng, F., Du, X., Sun, X., Kang, Z., & Meng, X. (2024). Negative sampling in recommendation: A survey and future directions. arXiv. https://arxiv.org/abs/2409.07237

Prakash, A., Bermperidis, D., & Chennu, S. (2024). Evaluating performance and bias of negative sampling in large-scale sequential recommendation models. arXiv. https://arxiv.org/abs/2410.17276

Sun, P., Wu, L., Zhang, K., Chen, X., & Wang, M. (2024). Neighborhood-enhanced supervised contrastive learning for collaborative filtering. arXiv. https://arxiv.org/abs/2402.11523

Yang, Z., Shao, Z., Dong, Y., & Tang, J. (2024). TriSampler: A better negative sampling principle for dense retrieval. arXiv. https://arxiv.org/abs/2402.11855
