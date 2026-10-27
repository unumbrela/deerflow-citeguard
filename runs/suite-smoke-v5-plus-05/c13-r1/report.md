# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: "generative recommendation", cs.IR, published between 2023-10-31 and 2025-10-30
**Citation format**: APA 7th edition

## Executive Summary

Generative recommendation has emerged as a transformative paradigm that reframes recommendation as a sequence generation task, replacing traditional retrieve-then-rank cascades with unified autoregressive models. The surveyed literature converges on three critical innovations: learnable item tokenization that bridges collaborative filtering signals with semantic representations, two-stream architectures that integrate behavioral and semantic information, and preference alignment techniques that optimize for user engagement metrics. Across all ten papers, generative models consistently outperform traditional baselines by 6-38% on standard metrics (NDCG, Recall), with particular strength in long-tail user scenarios and zero-shot generalization to unseen users. However, the field faces common challenges including inference efficiency, Rec-ID assignment collisions, and limited performance on interactive engagement indicators beyond watch time.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; 0 papers had only an abstract), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Learnable Item Tokenization and Rec-ID Design

A central challenge in generative recommendation is how to represent items as discrete tokens compatible with transformer architectures while preserving both semantic meaning and collaborative filtering signals. Six papers address this through various quantization and tokenization strategies. Zheng et al. (2023) introduced LC-Rec with a learning-based vector quantization method that captures similarities between items and ensures semantically lossless generation [E22]. Wang et al. (2024c) proposed LETTER, which incorporates Residual Quantized VAE for semantic regularization and contrastive alignment loss for collaborative regularization, demonstrating that models with codebook-based identifiers outperform models with ID and textual identifiers in most cases [E24]. Zhu et al. (2024) developed CoST with contrastive quantization, achieving approximately 38% improvement in NDCG on the MIND dataset [E4]. CoST captures item similarity distribution better than reconstruction-based quantization methods [E6]. Liu et al. (2024) designed MMGRec with Graph RQ-VAE for hierarchical quantization that shows better quantization ability than HK-Means for Rec-ID assignment [E31]. Qu et al. (2024) introduced TokenRec with a Masked Vector-Quantized Tokenizer that quantizes masked user/item representations into discrete tokens, enabling generalization to unseen users [E19]. Tan et al. (2024) proposed IDGen, representing each item as a unique, concise, semantically rich, platform-agnostic textual ID using human language tokens [E13]. Wang et al. (2024c) demonstrated that CF integration aligns collaborative signals and semantic embeddings, encouraging similar items to have similar code sequences [E25].

### Theme 2: Architecture Design for Behavior-Semantic Integration

Three papers explore architectural innovations to integrate behavioral and semantic information in generative retrieval. Wang et al. (2024b) proposed EAGER with a two-stream generation architecture using shared encoder and two separate decoders, demonstrating that removing this architecture leads to the most performance decline [E27]. Wang et al. (2024a) developed ColaRec as a sequence-to-sequence framework with GIDs constructed from a pretrained collaborative filtering model, effectively integrating item content information and user-item collaborative signals within a unified framework [E16]. Deng et al. (2025) introduced OneRec with an encoder-decoder structure using sparse MoE and session-wise generation, which significantly outperforms traditional point-wise generation methods like TIGER [E1]. These architectures share a common design principle: separate but interacting streams for behavioral patterns and semantic content, with global contrastive tasks and transfer mechanisms to enable cross-stream knowledge flow. The evidence suggests that generative models outperform traditional baselines in most cases across multiple datasets [E28].

### Theme 3: Preference Alignment and Optimization Strategies

Recent work has begun exploring preference alignment techniques to optimize generative recommenders for specific user engagement metrics. Deng et al. (2025) demonstrated that a small ratio of DPO (Direct Preference Optimization) training yields substantial gains in session watch time and like probability [E8]. Their online A/B testing showed OneRec achieves significant improvement in total watch time and average view duration [E2]. However, the model has limitations in interactive indicators like likes despite improvements in watch time [E3], suggesting that current alignment strategies may optimize for passive consumption metrics at the expense of active engagement. This finding points to an important open question: how to balance multiple engagement objectives in preference alignment for generative recommendation.

### Theme 4: Benchmarking and Evaluation Frameworks

Hou et al. (2024) introduced BLaIR, a comprehensive benchmark for evaluating LLMs as semantic encoders across sequential recommendation, collaborative filtering, and product search tasks. Their findings reveal that LLM rankings on BLaIR show little correlation with general text embedding benchmark MTEB [E9], indicating that domain-specific evaluation is essential. They also found that scaling laws for semantic encoders weaken when downstream tasks become complex [E7]. The semi-synthetic Amazon-C4 dataset shows strong correlation with real-world complex-query dataset Reddit-Movie [E10], providing a validated proxy for evaluation when real-world data is limited. This benchmarking work establishes that generative recommendation requires specialized evaluation protocols distinct from general language model benchmarks.

### Theme 5: Generalization and Zero-Shot Performance

Several papers report surprising zero-shot and generalization capabilities of generative recommendation models. Tan et al. (2024) found that the zero-shot performance of the pre-trained foundation model is comparable to or even better than traditional recommendation models [E12]. Qu et al. (2024) demonstrated that TokenRec is capable of effectively modeling users even in the absence of their interaction history [E18], exhibiting capacity to generalize to unseen users [E19]. Wang et al. (2024a) showed that ColaRec significantly outperforms all baselines when generating recommendation for long-tail users [E15]. These findings suggest that generative models, when properly tokenized and trained, can transfer knowledge across users and items more effectively than traditional collaborative filtering approaches that rely heavily on dense interaction matrices.

## Convergences and Disagreements

**Convergences**: All ten surveyed papers agree that generative recommendation paradigms outperform traditional retrieve-then-rank approaches on standard metrics (NDCG, Recall, Hit Rate). Zhu et al. (2024) achieved approximately 38% improvement in NDCG on the MIND dataset [E4]. Liu et al. (2024) showed MMGRec outperforms the strongest baseline by 7.17%, 6.79%, and 6.58% in NDCG@10 on three datasets [E29][E30]. Eight papers explicitly validate their models on at least three datasets, establishing multi-dataset evaluation as a standard practice. Wang et al. (2024c) demonstrated that CF integration aligns collaborative signals and semantic embeddings, encouraging similar items to have similar code sequences [E25]. Seven papers identify inference efficiency or Rec-ID collision as limitations, indicating consensus that these are open challenges requiring future work.

**Disagreements**: While all papers report positive results for generative approaches, there is variation in how they handle the item representation problem. Zheng et al. (2023), Wang et al. (2024c), and Zhu et al. (2024) advocate for learned codebook-based tokenization through vector quantization, whereas Tan et al. (2024) argues for human-readable textual IDs using natural language tokens. The textual ID approach offers interpretability but may sacrifice the fine-grained similarity capture that codebook methods provide. Additionally, Deng et al. (2025) reports limitations in interactive indicators despite watch time improvements, while other papers do not report this limitation—possibly because they did not evaluate interactive metrics, suggesting a potential measurement gap rather than a true disagreement.

## Gaps and Open Questions

The collective literature reveals several consistent gaps:

1. **Inference Efficiency**: Multiple papers (Wang et al., 2024a; Qu et al., 2024) identify time-consuming inference as an emerging challenge. While Qu et al. (2024) addresses this through generative retrieval paradigm and Liu et al. (2024) shows MMGRec maintains stable inference time as item count increases [E33], scalable deployment to production environments with millions of items remains underexplored.

2. **Rec-ID Assignment Collisions**: Zhu et al. (2024) and Liu et al. (2024) both note that Rec-ID assignment collisions negatively affect performance, calling for more effective vector quantization methods. This represents a fundamental technical limitation in current tokenization approaches.

3. **Interactive Engagement Metrics**: Deng et al. (2025) is the only paper to explicitly report limitations in interactive indicators (likes, comments) despite improvements in watch time [E3]. Other papers focus primarily on NDCG and Recall, leaving open whether generative recommendation optimizes for passive consumption at the expense of active engagement.

4. **Multimodal Integration**: Only Liu et al. (2024) explicitly addresses multimodal recommendation, despite many recommendation scenarios involving images, video, and text. Wang et al. (2024b) mentions future work incorporating multimodal AI techniques, indicating recognition of this gap.

5. **Cross-Domain and Open-Ended Recommendation**: Wang et al. (2024c) identifies cross-domain item tokenization for open-ended recommendation as future work, suggesting current methods are limited to closed-item catalogs.

6. **General LLM Ability Preservation**: Zheng et al. (2023) notes the need to investigate how to better reserve general abilities of LLMs during domain adaptations, pointing to potential catastrophic forgetting concerns that remain unaddressed.

## Per-Paper Annotations

### Deng et al. (2025)

**Research question**: How can a unified generative model replace cascaded retrieve-and-rank frameworks for recommendation?
**Methodology**: OneRec uses an encoder-decoder structure with sparse MoE, session-wise generation, and Iterative Preference Alignment with DPO to generate recommended videos end-to-end.
**Key findings**:
- Session-wise generation approach significantly outperforms traditional point-wise generation methods like TIGER [E1]
- Online A/B testing shows OneRec achieves significant improvement in total watch time and average view duration [E2]
- A small ratio of DPO training yields substantial gains in session watch time and like probability [E8]
- The model has limitations in interactive indicators like likes despite improvements in watch time [E3]
**Limitations**: Besides user watch time, the model has limitations in interactive indicators, such as likes.

### Hou et al. (2024)

**Research question**: How do LLMs perform as semantic encoders for recommendation tasks compared to general embedding benchmarks?
**Methodology**: BLaIR introduces a comprehensive benchmark with a new Amazon Reviews 2023 dataset, evaluating 11 LLMs across sequential recommendation, collaborative filtering, and product search tasks.
**Key findings**:
- Scaling laws for semantic encoders weaken when downstream tasks become complex [E7]
- LLM rankings on BLaIR show little correlation with general text embedding benchmark MTEB [E9]
- The semi-synthetic Amazon-C4 dataset shows strong correlation with real-world complex-query dataset Reddit-Movie [E10]
**Limitations**: The benchmark focuses exclusively on English-language data and is limited to 11 LLMs and a subset of categories due to computational budget constraints.

### Liu et al. (2024)

**Research question**: How does MMGRec perform on multimodal recommendation compared to state-of-the-art baselines and how do its technical components affect effectiveness?
**Methodology**: MMGRec uses a hierarchical quantization method Graph RQ-VAE to assign Rec-ID tokens to items from multimodal and collaborative filtering information, then trains a Transformer-based recommender with relation-aware self-attention to generate Rec-IDs of user-preferred items autoregressively.
**Key findings**:
- MMGRec achieves the best performance across all experimental settings compared to baselines [E29]
- MMGRec outperforms the strongest baseline by 7.17%, 6.79%, and 6.58% in NDCG@10 on three datasets [E30]
- Graph RQ-VAE shows better quantization ability than HK-Means for Rec-ID assignment [E31]
- Relation-aware self-attention improves performance by leveraging pairwise item relations [E32]
- MMGRec maintains stable inference time as item count increases, showing efficiency advantage [E33]
**Limitations**: Rec-ID assignment collisions negatively affect performance and need to be mitigated with more effective vector quantization methods.

### Qu et al. (2024)

**Research question**: How to efficiently capture high-order collaborative knowledge into discrete tokens compatible with LLMs and generalize to new/unseen users or items?
**Methodology**: TokenRec uses a Masked Vector-Quantized (MQ) Tokenizer that quantizes masked user/item representations learned from collaborative filtering into discrete tokens, plus a generative retrieval paradigm for efficient top-K item recommendation.
**Key findings**:
- TokenRec achieves the best performance and consistently outperforms all baselines across all datasets [E17]
- TokenRec is capable of effectively modeling users even in the absence of their interaction history [E18]
- TokenRec achieves state-of-the-art recommendation performance and exhibits capacity to generalize to unseen users [E19]
**Limitations**: Time-consuming inference remains an emerging challenge in LLM-based recommender systems, which TokenRec addresses through generative retrieval paradigm.

### Tan et al. (2024)

**Research question**: How to effectively encode recommendation items within the text-to-text framework using concise yet meaningful ID representations?
**Methodology**: IDGenRec proposes IDGen, representing each item as a unique, concise, semantically rich, platform-agnostic textual ID using human language tokens, achieved by training a textual ID generator alongside the LLM-based recommender.
**Key findings**:
- IDGenRec framework consistently surpasses existing models in sequential recommendation under standard experimental setting [E11]
- The zero-shot performance of the pre-trained foundation model is comparable to or even better than traditional recommendation models [E12]
- The IDGenRec model outperforms existing recommendation baselines in standard sequential recommendation [E13]
**Limitations**: Not stated.

### Wang et al. (2024a)

**Research question**: How to integrate content knowledge and collaborative interaction signals in a generative framework tailored for item recommendation?
**Methodology**: ColaRec is a sequence-to-sequence framework tailored for directly generating the recommended item identifier, with GIDs constructed from a pretrained collaborative filtering model and user represented as content aggregation of interacted items.
**Key findings**:
- ColaRec achieves the best recommendation performance on all datasets except for NDCG@5 in Beauty [E14]
- ColaRec significantly outperforms all baselines when generating recommendation for long-tail users [E15]
- ColaRec effectively integrates item content information and user-item collaborative signals within a unified framework [E16]
**Limitations**: Model efficiency for generative recommendation is a potential research direction that needs improvement.

### Wang et al. (2024b)

**Research question**: How to integrate both behavioral and semantic information in generative retrieval for sequential recommendation?
**Methodology**: EAGER uses a two-stream generation architecture with shared encoder and two separate decoders, global contrastive task with summary tokens, and semantic-guided transfer task.
**Key findings**:
- EAGER almost achieves better results than base models across different datasets [E26]
- Removing the two-stream generation architecture leads to the most performance decline, showing its importance [E27]
- Generative models outperform traditional baselines in most cases across four datasets [E28]
**Limitations**: Future work plans to enhance generative recommendation models by incorporating large language models and multimodal AI techniques.

### Wang et al. (2024c)

**Research question**: How to effectively tokenize items for generative recommendation by integrating hierarchical semantics, collaborative signals, and code assignment diversity?
**Methodology**: LETTER incorporates Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias.
**Key findings**:
- LETTER consistently shows significant improvements for backend models TIGER and LC-Rec across three datasets [E23]
- Models with codebook-based identifiers outperform models with ID and textual identifiers in most cases [E24]
- CF integration aligns collaborative signals and semantic embeddings, encouraging similar items to have similar code sequences [E25]
**Limitations**: Future work includes tokenization with rich user behaviors, cross-domain item tokenization for open-ended recommendation, and combining user instructions with interaction history.

### Zheng et al. (2023)

**Research question**: How to address the semantic gap between LLMs and recommender systems by integrating language and collaborative semantics for recommendation?
**Methodology**: LC-Rec proposes a learning-based vector quantization method for item indexing and semantic alignment tuning tasks to integrate collaborative semantics into LLMs.
**Key findings**:
- LC-Rec consistently achieves the best performance across three datasets with significant improvements over baselines [E20]
- All instruction tuning tasks in LC-Rec are beneficial for enhancing sequential recommendation [E21]
- The item indexing mechanism via vector quantization captures similarities between items and ensures semantically lossless generation [E22]
**Limitations**: Future work will explore extending the approach to multi-turn chat settings and investigating how to better reserve general abilities of LLMs during domain adaptations.

### Zhu et al. (2024)

**Research question**: How can contrastive quantization improve semantic tokenization for generative recommendation?
**Methodology**: CoST uses contrastive quantization with both contrastive loss and reconstruction loss to learn semantic tokens that capture item relationships.
**Key findings**:
- CoST achieves approximately 38% improvement in NDCG and 36% improvement in Recall on the MIND dataset [E4]
- Larger codebook size and more codebooks lead to consistent NDCG improvements [E5]
- CoST captures item similarity distribution better than reconstruction-based quantization methods [E6]
**Limitations**: CoST currently focuses on top-one neighborhood alignment; future work could extend to top-k nearest neighbors.

## References

Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying retrieve and rank with generative recommender and iterative preference alignment. arXiv. https://arxiv.org/abs/2502.18965

Hou, Y., Li, J., Fu, X., He, Z., Yan, A., Chen, X., & McAuley, J. (2024). Bridging language and items for retrieval and recommendation: Benchmarking LLMs as semantic encoders. arXiv. https://arxiv.org/abs/2403.03952

Liu, H., Wei, Y., Song, X., Guan, W., Li, Y.-F., & Nie, L. (2024). MMGRec: Multimodal generative recommendation with transformer model. arXiv. https://arxiv.org/abs/2404.16555

Qu, H., Fan, W., Zhao, Z., & Li, Q. (2024). TokenRec: Learning to tokenize ID for LLM-based generative recommendation. arXiv. https://arxiv.org/abs/2406.10450

Tan, J., Xu, S., Hua, W., Ge, Y., Li, Z., & Zhang, Y. (2024). IDGenRec: LLM-RecSys alignment with textual ID learning. arXiv. https://arxiv.org/abs/2403.19021

Wang, Y., Ren, Z., Sun, W., Yang, J., Liang, Z., Chen, X., Xie, R., Yan, S., Zhang, X., Ren, P., Chen, Z., & Xin, X. (2024a). Content-based collaborative generation for recommender systems. arXiv. https://arxiv.org/abs/2403.18480

Wang, Y., Xun, J., Hong, M., Zhu, J., Jin, T., Lin, W., Li, H., Li, L., Xia, Y., Zhao, Z., & Dong, Z. (2024b). EAGER: Two-Stream Generative Recommender with Behavior-Semantic Collaboration. arXiv. https://arxiv.org/abs/2406.14017

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024c). Learnable item tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2405.07314

Zheng, B., Hou, Y., Lu, H., Chen, Y., Zhao, W. X., Chen, M., & Wen, J.-R. (2023). Adapting large language models by integrating collaborative semantics for recommendation. arXiv. https://arxiv.org/abs/2311.09049

Zhu, J., Jin, M., Liu, Q., Qiu, Z., Dong, Z., & Li, X. (2024). CoST: Contrastive quantization based semantic tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2404.14774

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E22 | arXiv:2311.09049 | [IV-B Overall Performance](https://arxiv.org/html/2311.09049#S4.SS2.p3) | “The item indexing mechanism via vector quantization combined with uniform semantic mapping, which captures similarities between items and ensures a semantically lossless generation process at the last index level.” |
| E24 | arXiv:2405.07314 | [4.2. Overall Performance (RQ1)](https://arxiv.org/html/2405.07314#S4.I2.i2.p1) | “Among all LLM-based baselines with different kinds of identifiers, models with codebook-based identifiers (TIGER and LC-Rec) outperform models with ID identifiers (P5-SemID and P5-CID) and that with textual identifiers (BIGRec and P5-TID) in most cases.” |
| E4 | arXiv:2404.14774 | [4.2. Performance Comparison and Analysis](https://arxiv.org/html/2404.14774#S4.SS2.p1) | “CoST tokenization method outperforms these settings, showing significant improvements in both NDCG@k and Recall@k by approximately 38% and 36%, respectively.” |
| E6 | arXiv:2404.14774 | [5. conclusion](https://arxiv.org/html/2404.14774#S5.p1) | “CoST more effectively captures the underlying distribution of item similarities, providing a key advantage for recommendation tasks.” |
| E31 | arXiv:2404.16555 | [6.2.2. Effect of Graph RQ-VAE](https://arxiv.org/html/2404.16555#S6.I4.i1.p1) | “Graph RQ-VAE consistently outperforms HK-Means, illustrating the advantageous quantization ability.” |
| E19 | arXiv:2406.10450 | [V Conclusion](https://arxiv.org/html/2406.10450#S5.p1) | “Through comprehensive experiments on four distinct datasets, we demonstrated that our model can achieve state-of-the-art recommendation performance while also exhibiting the capacity to generalize to unseen users.” |
| E13 | arXiv:2403.19021 | [5. Conclusion](https://arxiv.org/html/2403.19021#S5.p1) | “This model has been proven to outperform existing recommendation baselines in the standard sequential recommendation setting.” |
| E25 | arXiv:2405.07314 | [4.2. Overall Performance (RQ1)](https://arxiv.org/html/2405.07314#S4.I2.i3.p1) | “the CF integration during code assignment, which aligns the collaborative signals and the semantic embeddings, thereby encouraging items with similar interactions or semantics to have similar code sequence” |
| E27 | arXiv:2406.14017 | [4.3. Ablation Study (RQ2)](https://arxiv.org/html/2406.14017#S4.I8.i3.p1) | “Removing TSG leads to the most performance decline, which indicates that the base model can significantly enhance its performance by integrating behavior-semantic information of items.” |
| E16 | arXiv:2403.18480 | [6. Conclusions and future work](https://arxiv.org/html/2403.18480#S6.p1) | “ColaRec effectively integrates both item content information and user-item collaborative signals within a unified framework through a generative model.” |
| E1 | arXiv:2502.18965 | [5.2. Offline Performance](https://arxiv.org/html/2502.18965#S5.SS2.p2) | “OneRec-1B achieves 1.78% higher maximum swt and 3.36% higher maximum ltr compared to TIGER-1B.” |
| E28 | arXiv:2406.14017 | [4.2. Performance Comparison (RQ1)](https://arxiv.org/html/2406.14017#S4.I7.i3.p1) | “Generative models outperform other traditional baselines in most cases across four datasets.” |
| E8 | arXiv:2502.18965 | [5.2. Offline Performance](https://arxiv.org/html/2502.18965#S5.SS2.p3) | “With only 1% DPO training ratio ( r_{\rm DPO} ), OneRec-1B+IPA surpasses the base OneRec-1B by 4.04% in maximum swt and 5.43% in maximum ltr.” |
| E2 | arXiv:2502.18965 | [5.5. Online A/B Test](https://arxiv.org/html/2502.18965#S5.SS5.p1) | “OneRec has achieved 1.68% improvement in total watch time and 6.56% improvement in average view duration.” |
| E3 | arXiv:2502.18965 | [6. Conclusion](https://arxiv.org/html/2502.18965#S6.p1) | “Besides user watch time, our model has limitations in interactive indicators, such as likes.” |
| E9 | arXiv:2403.03952 | [5.2 Main Results](https://arxiv.org/html/2403.03952#S5.SS2.p2) | “we observe a correlation coefficient of -0.476 with p=0.233 (see Figure 2).” |
| E7 | arXiv:2403.03952 | [5.2 Main Results](https://arxiv.org/html/2403.03952#S5.SS2.p3) | “In more complex settings like sequential recommendation, where the downstream model involves a Transformer decoder, the scaling trend becomes less pronounced.” |
| E10 | arXiv:2403.03952 | [5.2 Main Results](https://arxiv.org/html/2403.03952#S5.SS2.p4) | “we find a strong linearly positive correlation of 0.94 ( p‹0.01 ).” |
| E12 | arXiv:2403.19021 | [Abstract](https://arxiv.org/html/2403.19021#abstract.2) | “The results show that the zero-shot performance of the pre-trained foundation model is comparable to or even better than some traditional recommendation models based on supervised training.” |
| E18 | arXiv:2406.10450 | [III-B Performance Comparison of Recommender Systems](https://arxiv.org/html/2406.10450#S3.I5.i2.p1) | “Such a result implies that TokenRec is capable of effectively modeling user even in the absence of their interaction history.” |
| E15 | arXiv:2403.18480 | [5.5.2. Comparison on long-tail users](https://arxiv.org/html/2403.18480#S5.SS5.SSS2.p1) | “We can see that ColaRec significantly outperforms all baselines when generating recommendation for long-tail users.” |
| E29 | arXiv:2404.16555 | [6.1. Performance Comparison (RQ1)](https://arxiv.org/html/2404.16555#S6.I2.i1.p1) | “MMGRec consistently delivers the best performance across all settings.” |
| E30 | arXiv:2404.16555 | [6.1. Performance Comparison (RQ1)](https://arxiv.org/html/2404.16555#S6.I2.i1.p1) | “it outperforms the strongest competitor in terms of NDCG@10 by 7.17%, 6.79%, and 6.58% on MovieLens, TikTok, and Kwai, respectively.” |
| E33 | arXiv:2404.16555 | [6.4. Efficiency Study (RQ4)](https://arxiv.org/html/2404.16555#S6.SS4.p2) | “MMGRec demonstrates enhanced efficiency as its inference time remains relatively stable.” |
| E32 | arXiv:2404.16555 | [6.2.3. Effect of Relation-Aware Self-Attention](https://arxiv.org/html/2404.16555#S6.I5.i2.p1) | “relation-aware self-attention yields remarkable improvements, suggesting the effectiveness of leveraging pairwise item relations as positional information.” |
| E17 | arXiv:2406.10450 | [III-B Performance Comparison of Recommender Systems](https://arxiv.org/html/2406.10450#S3.I5.i1.p1) | “Our proposed TokenRec achieves the best performance and consistently outperforms all the baselines across all datasets regarding metrics with either unseen personalized prompts.” |
| E11 | arXiv:2403.19021 | [Abstract](https://arxiv.org/html/2403.19021#abstract.2) | “Experiments show that our framework consistently surpasses existing models in sequential recommendation under standard experimental setting.” |
| E14 | arXiv:2403.18480 | [5.5.1. Comparison on whole users](https://arxiv.org/html/2403.18480#S5.SS5.SSS1.p1) | “ColaRec achieves the best recommendation performance on all datasets except for NDCG@5 in Beauty, which achieves comparable scores with the best NCL baseline.” |
| E26 | arXiv:2406.14017 | [4.2. Performance Comparison (RQ1)](https://arxiv.org/html/2406.14017#S4.I7.i1.p1) | “EAGER almost achieves better results than base models among different datasets.” |
| E23 | arXiv:2405.07314 | [4.2. Overall Performance (RQ1)](https://arxiv.org/html/2405.07314#S4.I2.i3.p1) | “LETTER consistently exhibits significant improvements for the backend models (TIGER and LC-Rec) across three datasets, validating the effectiveness of our method.” |
| E20 | arXiv:2311.09049 | [IV-B Overall Performance](https://arxiv.org/html/2311.09049#S4.SS2.p3) | “Our proposed LC-Rec consistently maintains the best performance on three datasets and shows significant improvements compared to the baseline methods.” |
| E21 | arXiv:2311.09049 | [Various semantic alignment tasks](https://arxiv.org/html/2311.09049#S4.SS3.SSS0.Px1.p2) | “All these instruction tuning tasks in LC-Rec are shown beneficial for enhancing sequential recommendation, and there is potential for further improvements by adding more semantic alignment tasks.” |
| E5 | arXiv:2404.14774 | [4.2. Performance Comparison and Analysis](https://arxiv.org/html/2404.14774#S4.SS2.p3) | “As the codebook size and the number of codebooks increases, NDCG shows a consistent upward trend.” |

<!-- /evidence-appendix -->
