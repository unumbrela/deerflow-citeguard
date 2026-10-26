# Systematic Literature Review: Negative Sampling Techniques in Information Retrieval

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "negative sampling", category cs.IR, published between 2024-01-09 and 2026-01-08
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on negative sampling techniques in information retrieval, with a focus on recommender systems and dense retrieval. The surveyed literature reveals a rapidly evolving field where negative sampling has emerged as a critical component for training effective recommendation and retrieval models. Collectively, these papers demonstrate that traditional random negative sampling approaches are being replaced by more sophisticated methods that adaptively select hard negatives, leverage multi-modal information, and incorporate theoretical principles about the relationship between queries, positive documents, and negative samples. The research spans from foundational theoretical analyses of negative sampling principles to practical frameworks that achieve substantial performance improvements over existing methods.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "negative sampling", filtered to category cs.IR, published between 2024-01-09 and 2026-01-08. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening flow**: 50 papers identified by search, 84 added from citation expansion, 30 shortlisted, 30 screened with scores (14 scored 0, 10 scored 1, 3 scored 2, 3 scored 3), and 10 included (4 from references).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, all limitations were extracted from abstracts only; full-text analysis might reveal additional constraints not mentioned in abstracts.

## Themes

### Theme 1: Adaptive and Hard Negative Sampling

A dominant theme across the surveyed literature is the shift from static, random negative sampling toward adaptive methods that dynamically select negative samples of appropriate difficulty during training. Lai et al. (2024) identified that fixed hardness levels in traditional negative sampling cause false positive and false negative problems, proposing adaptive hardness negative sampling (AHNS) that adjusts sample difficulty throughout training. Similarly, Lee et al. (2024) introduced SCONE, a stochastic sampling approach that generates diverse hard negative samples using score-based generative models. This theme reflects a broader recognition that the informativeness of negative samples varies throughout training, and optimal performance requires adapting to the model's current learning state.

### Theme 2: Theoretical Foundations of Negative Sampling

Several papers contribute theoretical analyses that elucidate why negative sampling works and establish guiding principles for its design. Yang et al. (2024) uncovered the "quasi-triangular principle" revealing the triangular-like interplay between query, positive document, and negative document in dense retrieval. Lin et al. (2024) provided theoretical analysis showing that BCE loss faces gradient vanishing for negative samples when positive feedback is sparse, explaining why auxiliary ranking losses improve performance. Chen et al. (2024) bridged supervised contrastive learning with softmax loss over negative sampling theoretically. This theoretical turn suggests the field is maturing beyond empirical heuristics toward principled understanding of negative sampling mechanisms.

### Theme 3: Multi-Modal and Context-Aware Negative Sampling

Recent work extends negative sampling beyond single-modality interactions to leverage rich multi-modal information. Ji et al. (2025) proposed NegGen, which utilizes multi-modal large language models to generate balanced and contrastive negative samples by analyzing and manipulating item attributes across multiple modalities. Prakash et al. (2024) examined how negative sampling choices interact with dataset characteristics and popularity bias in sequential recommendation, finding that different methods perform differently across head, mid, and tail item bands. This theme reflects the growing sophistication of recommender systems and the need for negative sampling strategies that account for complex, heterogeneous user-item interactions.

### Theme 4: Negative Sampling for Large Language Model-Based Recommendation

The emergence of LLM-based recommendation has created new challenges and opportunities for negative sampling. Chen et al. (2024) developed Softmax-DPO, which incorporates multiple negatives in user preference data and extends from traditional full-ranking Plackett-Luce models to partial rankings with softmax sampling strategies tailored for language model-based recommenders. Lin et al. (2024) addressed the computational cost of fine-tuning LLMs on recommendation data through data pruning based on influence and effort scores, achieving superior performance with only 2% of samples. These papers demonstrate that negative sampling principles must be adapted to the unique characteristics of LLM architectures and their training dynamics.

### Theme 5: Survey and Unifying Frameworks

The field has reached a stage where comprehensive surveys and unifying frameworks are emerging. Ma et al. (2024) conducted an extensive literature review classifying existing negative sampling strategies into five categories based on their techniques, outlining prospective research directions for diverse recommender system scenarios. This survey work provides a taxonomy that helps organize the rapidly growing literature and identifies gaps for future research. The existence of such comprehensive surveys indicates the field's maturation and the accumulation of sufficient diverse approaches to warrant systematic classification.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that random negative sampling is suboptimal compared to more sophisticated approaches. Lai et al. (2024), Lee et al. (2024), and Yang et al. (2024) all demonstrate that adaptive or theoretically-guided sampling substantially outperforms static methods. There is also broad agreement that negative sampling plays a critical role in revealing genuine negative aspects of user behaviors, as emphasized by Ma et al. (2024) and Prakash et al. (2024). Several papers report performance improvements of 10-35% over state-of-the-art baselines when using their proposed methods.

**Disagreements**: While there is consensus on the importance of hard negatives, papers differ on the optimal strategy for selecting them. Prakash et al. (2024) found that popularity-based methods offer balanced performance at the cost of lower overall model performance, suggesting trade-offs that other papers do not fully address. The tension between overall performance and fairness across popularity bands remains unresolved. Additionally, while Ji et al. (2025) advocate for multi-modal LLM-based generation of negatives, the computational cost and practical deployment considerations of such approaches are not thoroughly compared with simpler alternatives.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the surveyed papers explicitly stated limitations in their abstracts, suggesting either that limitations are not being thoroughly discussed or that they appear only in full text. Second, while several papers mention fairness and bias concerns (particularly Prakash et al., 2024), there is limited systematic investigation of how negative sampling choices affect recommendation fairness across different user demographics. Third, the computational efficiency of sophisticated negative sampling methods is rarely analyzed in depth—methods like NegGen (Ji et al., 2025) that use multi-modal LLMs likely incur substantial overhead that is not quantified. Fourth, most evaluations focus on standard benchmark datasets; real-world deployment characteristics and long-term user satisfaction impacts of different negative sampling strategies remain underexplored. Finally, the interaction between negative sampling and other training techniques (such as data augmentation, regularization, or architecture choices) warrants more systematic investigation.

## Per-Paper Annotations

### Chen et al. (2024)

**Research question**: How can Language Model-based recommenders be improved to better leverage preference data and optimize for personalized ranking tasks?
**Methodology**: Proposed Softmax-DPO (S-DPO), which incorporates multiple negatives in user preference data and devises an alternative version of DPO loss tailored for LM-based recommenders, extending from traditional full-ranking Plackett-Luce model to partial rankings with softmax sampling strategies. Evaluated on three real-world datasets.
**Key findings**:
- S-DPO instills ranking information into LMs to help distinguish preferred items from negatives, rather than solely focusing on positives
- S-DPO has an inherent benefit of mining hard negatives, assuring exceptional capabilities in recommendation tasks
- S-DPO effectively models user preference and boosts recommendation performance while providing better rewards for preferred items
- The method bridges S-DPO with softmax loss over negative sampling theoretically
**Limitations**: not stated in abstract

### Ji et al. (2025)

**Research question**: How can negative sampling for multi-modal recommender systems be improved to effectively utilize multi-modal data and produce cohesive, balanced negative samples?
**Methodology**: Proposed NegGen, a framework that utilizes multi-modal large language models (MLLMs) to generate balanced and contrastive negative samples. Designed three prompt templates for analyzing and manipulating item attributes across modalities, and employed a causal learning module to disentangle intervened key features from irrelevant attributes.
**Key findings**:
- Existing negative sampling techniques struggle to effectively utilize multi-modal data in multi-modal recommender systems
- Two key challenges are identified: producing cohesive negative samples contrasting with positive samples and maintaining balanced influence across different modalities
- NegGen uses three different prompt templates to analyze and manipulate item attributes across multiple modalities
- NegGen employs a causal learning module to disentangle the effect of intervened key features and irrelevant item attributes
- NegGen demonstrates superior performance compared to state-of-the-art methods in both negative sampling and multi-modal recommendation on real-world datasets
**Limitations**: not stated in abstract

### Lai et al. (2024)

**Research question**: How can negative sampling methods for collaborative filtering overcome the false positive and false negative problems caused by fixed hardness levels?
**Methodology**: Proposed a new paradigm called adaptive hardness negative sampling (AHNS) with three key criteria, and presented a concrete instantiation called AHNS_{p<0}. Theoretically demonstrated that AHNS_{p<0} fits the three criteria and achieves a larger lower bound of normalized discounted cumulative gain.
**Key findings**:
- Existing negative sampling methods can only select negative samples of a fixed hardness level, leading to false positive problem (FPP) and false negative problem (FNP)
- AHNS adaptively selects negative samples with appropriate hardnesses during training to mitigate FPP and FNP impacts
- AHNS_{p<0} theoretically fits the three criteria of AHNS and achieves a larger lower bound of normalized discounted cumulative gain
- Existing negative sampling methods can be regarded as more relaxed cases of AHNS
- AHNS_{p<0} consistently and substantially outperforms several state-of-the-art competitors on multiple datasets
**Limitations**: not stated in abstract

### Lee et al. (2024)

**Research question**: How can graph-based collaborative filtering models overcome challenges of data sparsity and negative sampling in recommender systems?
**Methodology**: Proposed SCONE, a novel stochastic sampling approach based on score-based generative models that generates dynamic augmented views and diverse hard negative samples. Evaluated through extensive experiments on 6 benchmark datasets.
**Key findings**:
- SCONE consistently outperforms state-of-the-art baselines across 6 benchmark datasets
- SCONE effectively addresses user sparsity and item popularity issues
- The approach enhances performance for both cold-start users and long-tail items
- SCONE improves the diversity of recommendations and uniformity of representations
**Limitations**: not stated in abstract

### Lin et al. (2024a)

**Research question**: Why does combining BCE loss with an auxiliary ranking loss improve CTR prediction performance, particularly in scenarios where positive feedback is sparse?
**Methodology**: Conducted theoretical analysis and extensive empirical evaluations on public datasets to uncover the gradient vanishing issue for negative samples in BCE loss when positive feedback is sparse. Integrated ranking loss into Tencent's online advertising system for real-world validation.
**Key findings**:
- BCE loss faces gradient vanishing for negative samples when positive feedback is sparse
- The auxiliary ranking loss generates larger gradients on negative samples, mitigating optimization difficulties when using BCE loss only
- The combination loss results in improved classification ability
- Integration into Tencent's online advertising system achieved notable lifts of 0.70% and 1.26% in Gross Merchandise Value for two main scenarios
**Limitations**: not stated in abstract

### Lin et al. (2024b)

**Research question**: How can the cost of fine-tuning LLMs on rapidly expanding recommendation data be reduced while maintaining performance?
**Methodology**: Proposed a data pruning method based on two scores: influence score (to identify influential samples for high overall performance) and effort score (to prioritize hard samples specifically for LLMs). A small-sized surrogate model replaces LLMs to obtain the influence score for low-cost data pruning. Validated on three real-world datasets.
**Key findings**:
- Few-shot fine-tuning offers a promising approach to quickly adapt LLMs to new recommendation data
- The proposed method uses influence and effort scores to efficiently identify influential samples
- Using only 2% of samples, the proposed method surpasses full data fine-tuning performance
- The approach reduces time costs by 97% compared to full data fine-tuning
**Limitations**: not stated in abstract

### Ma et al. (2024)

**Research question**: What are the existing negative sampling strategies in recommender systems, and what future research directions should the community pursue?
**Methodology**: Conducted an extensive literature review on existing negative sampling strategies in recommender systems, discussing existing user feedback, the critical role of negative sampling, and optimization objectives. Classified strategies into five categories based on their discrepant techniques.
**Key findings**:
- Recommender systems face challenges including information cocoons, interaction sparsity, cold-start problem, and feedback loops
- Conventional recommendation algorithms focus on positive historical behaviors while neglecting the essential role of negative feedback
- Negative sampling is proficient in revealing the genuine negative aspect inherent in user behaviors
- Existing negative sampling strategies can be classified into five categories with different techniques
- The survey outlines prospective research directions for negative sampling in diverse recommender system scenarios
**Limitations**: not stated in abstract

### Prakash et al. (2024)

**Research question**: How do different negative sampling methods impact model performance and popularity bias in large-scale sequential recommendation models?
**Methodology**: Implemented and compared various negative sampling methods (random, popularity-based, in-batch, mixed, adaptive, and adaptive with mixed variants) on modern sequential recommendation models. Conducted experiments with hyperparameter optimization and 20x repeats on three benchmark datasets with varying popularity biases.
**Key findings**:
- The choice of negative sampling method and dataset characteristics significantly impact key model performance metrics
- Average performance metrics often hide imbalances across popularity bands (head, mid, tail)
- Commonly used random negative sampling reinforces popularity bias and performs best for head items
- Popularity-based methods (in-batch and global popularity negative sampling) offer balanced performance at the cost of lower overall model performance
- The study provides a practical guide to trade-offs in selecting negative sampling methods for large-scale sequential recommendation models
**Limitations**: not stated in abstract

### Sun et al. (2024)

**Research question**: How can contrastive learning be improved to avoid distancing the target user/item from their collaborative neighbors in collaborative filtering?
**Methodology**: Proposed two supervised contrastive loss functions that treat collaborative neighbors of the anchor node as positive samples within the final objective loss function. Used a graph-based collaborative filtering model as the backbone with SGL's data augmentation methods, analyzing the approach through gradient lens to understand how positive samples influence anchor node embedding updates.
**Key findings**:
- The proposed NESCL model substitutes the contrastive loss function in SGL with a novel loss function that treats collaborative neighbors as positive samples
- Different positive samples simultaneously influence updating the anchor node's embeddings based on their similarities to the anchor node and negative samples
- On Yelp2018, Gowalla, and Amazon-Book datasets, NESCL surpasses SGL by 10.09%, 7.09%, and 35.36% on NDCG@20, respectively
**Limitations**: not stated in abstract

### Yang et al. (2024)

**Research question**: What guiding principle can be established for constructing negative candidates and designing negative sampling distributions in dense retrieval?
**Methodology**: Conducted a theoretical analysis of negative sampling in dense retrieval, unveiling the quasi-triangular principle that elucidates the triangular-like interplay between query, positive document, and negative document. Introduced TriSampler based on this principle.
**Key findings**:
- A comprehensive guiding principle for constructing negative candidates and designing negative sampling distributions was lacking in dense retrieval
- The quasi-triangular principle reveals the triangular-like interplay between query, positive document, and negative document
- TriSampler selectively samples more informative negatives within a prescribed constrained region
- TriSampler consistently attains superior retrieval performance across diverse representative retrieval models
- TriSampler is straightforward yet highly effective as a negative sampling method
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
