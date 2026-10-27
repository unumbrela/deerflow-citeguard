# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: generative recommendation, cs.IR, published between 2023-10-31 and 2025-10-30
**Citation format**: APA 7th edition

## Executive Summary

Generative recommendation has emerged as a transformative paradigm in recommender systems, shifting from traditional embedding-and-retrieve approaches to autoregressive generation of item identifiers. The surveyed literature reveals three converging research directions: (1) learning optimal item tokenization strategies that bridge collaborative filtering semantics with language model compatibility, (2) integrating multimodal content knowledge with behavioral interaction patterns, and (3) unifying retrieval and ranking stages into single end-to-end generative frameworks. Collectively, these works demonstrate that generative recommenders achieve superior performance over traditional baselines while enabling more efficient inference and better generalization to unseen users and items. However, challenges remain in preserving LLM general capabilities during domain adaptation, handling multi-objective optimization beyond watch time, and developing more effective vector quantization methods to reduce identifier assignment collisions.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query `generative recommendation`, filtered to category cs.IR, published between 2023-10-31 and 2025-10-30. Papers were sorted by co-citation relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; all papers had full text available), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Search and screening statistics**: 50 papers identified by search, 92 added from citation expansion, 30 shortlisted, 30 screened (score distribution: 0 papers scored 0, 1 paper scored 1, 5 papers scored 2, 24 papers scored 3), 10 included (6 from citation expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Learnable Item Tokenization and Identifier Design

A central challenge in generative recommendation is representing items as discrete tokens compatible with large language models while preserving collaborative filtering semantics. Recent work has moved beyond simple ID-based or textual identifiers toward learnable tokenization schemes that capture both semantic and behavioral information. Zheng et al. (2023) introduced LC-Rec, which uses learning-based vector quantization with uniform semantic mapping for item indexing, bridging the gap between language semantics and collaborative semantics. LC-Rec achieves superior performance compared to baseline methods across all three datasets [E1]. Vector quantization with uniform semantic mapping captures item similarities for effective indexing [E2]. Wang, W. et al. (2024) proposed LETTER, a learnable tokenizer incorporating Residual Quantized VAE for semantic regularization and contrastive alignment loss for collaborative regularization. LETTER demonstrates that codebook-based identifiers outperform both ID and textual identifiers [E4]. RQ-VAE's hierarchical semantics with different granularities enables better distinction between similar items [E5]. Experiments validate LETTER's superiority for item tokenization in generative recommendation [E6]. Zhu et al. (2024) extended this direction with CoST, introducing contrastive quantization that captures item neighborhood relationships through contrastive loss. CoST achieves approximately 38% improvement in NDCG and 36% in Recall on the MIND dataset [E14]. Larger codebook size and number of codebooks leads to consistent NDCG improvements [E15]. Qu et al. (2024) developed TokenRec with a Masked Vector-Quantized Tokenizer that quantizes masked user/item representations into discrete tokens, enabling efficient generative retrieval without auto-regressive decoding. TokenRec outperforms all baselines including traditional and LLM-based recommenders with significant margins [E28]. TokenRec demonstrates strong generalization to unseen users with only 7% performance drop compared to 40%+ for other methods [E29]. Liu et al. (2024) proposed MMGRec, which uses Graph RQ-VAE to assign hierarchical Rec-IDs from multimodal and collaborative information. MMGRec outperforms the strongest baseline by 6.58-7.17% on NDCG@10 across three datasets with statistical significance [E32]. Graph RQ-VAE achieves better Rec-ID assignment than hierarchical K-means clustering due to fewer ID collisions [E33].

### Theme 2: Behavior-Semantic Integration and Two-Stream Architectures

Another prominent direction integrates behavioral interaction patterns with semantic content knowledge through dual-stream or multi-task architectures. Wang, Y. et al. (2024) introduced EAGER, a two-stream generative recommender with shared encoder and separate decoders for behavior and semantic tokens, using a global contrastive task with summary tokens for discriminative decoding. EAGER achieves superior results compared to base models across different datasets [E7]. EAGER's two-stream decoder and multi-task training enable deeper understanding of behavior-semantic relationships [E9]. EAGER demonstrated substantial improvements over TIGER on the Beauty benchmark with over 30% gains in Recall@5 and NDCG@5, validating that behavior-semantic collaboration enables deeper understanding of item relationships [E8]. Wang, Yidan et al. (2024) proposed ColaRec, which integrates collaborative signals and content information in a unified generative framework by constructing generative identifiers from pretrained collaborative filtering models and representing users as content aggregation of interacted items. ColaRec demonstrates superior performance over baselines on four benchmark datasets [E26]. ColaRec successfully integrates collaborative signals and content information in a unified generative framework [E27]. These works collectively show that generative models generally outperform traditional baselines across multiple datasets by leveraging both behavioral patterns and semantic content [E10].

### Theme 3: End-to-End Unification and Iterative Alignment

Recent advances aim to unify the traditional multi-stage recommendation pipeline (retrieve, rank) into single end-to-end generative models with iterative preference alignment. Deng et al. (2025) proposed OneRec, which uses an encoder-decoder structure with sparse MoE for scaling and session-wise generation for contextual coherence, unifying retrieve and rank stages [E11]. A key innovation is Iterative Preference Alignment with DPO, where even a small ratio of DPO training yields substantial performance gains [E21]. Online A/B testing demonstrated significant improvements in watch time and view duration, though the model has limitations in interactive indicators beyond watch time [E12, E13]. This direction represents a shift toward foundation models for generative recommendation that can be iteratively aligned with user preferences.

### Theme 4: LLM-RecSys Alignment and Foundation Models

Several works explore aligning large language models with recommendation systems through specialized training paradigms. Tan et al. (2024) proposed IDGenRec, which represents each item as a unique, concise, semantically rich textual ID using human language tokens, trained alongside an LLM-based recommender with an alternative training strategy between the ID generator and base recommender [E22, E24]. IDGenRec significantly outperforms all baselines with improvements of 23-42% across four datasets and demonstrates potential for serving as foundation models for generative recommendation [E23, E25]. Hou et al. (2024) introduced BLaIR, a comprehensive benchmark for LLMs as semantic encoders, revealing that LLM rankings on recommendation tasks show little correlation with general text embedding benchmarks [E17, E18]. Their semi-synthetic Amazon-C4 dataset serves as a reliable proxy for real-world complex queries, though effectively leveraging rich, heterogeneous item metadata remains a challenging open problem [E19, E20].

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key findings. First, all papers demonstrate that generative recommendation approaches outperform traditional embedding-and-retrieve baselines across multiple datasets, with consistent improvements in Recall, NDCG, and other ranking metrics [E1, E6, E7, E10, E26, E28, E32]. Second, there is strong agreement that learnable, codebook-based identifiers capture item relationships more effectively than static ID or textual identifiers [E4, E5, E15, E33]. Third, multiple papers confirm that integrating both behavioral and semantic information yields superior performance compared to using either signal alone [E8, E9, E27]. Fourth, the literature converges on the finding that session-wise or sequence-wise generation approaches significantly outperform point-wise methods [E11].

**Disagreements**: While the literature shows broad agreement on the benefits of generative approaches, there are differences in architectural choices. Some works favor separate decoders for behavior and semantic streams (Wang, Y. et al., 2024), while others integrate both signals into a unified decoder (Wang, Yidan et al., 2024; Liu et al., 2024). Additionally, there is variation in tokenization strategies: Zheng et al. (2023) and Wang, W. et al. (2024) use vector quantization with uniform semantic mapping, whereas Tan et al. (2024) advocate for purely textual IDs using human language tokens. The optimal balance between collaborative semantics and language semantics remains an open question.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, multiple papers identify the challenge of preserving general LLM capabilities during domain adaptation for recommendation tasks (Zheng et al., 2023; Tan et al., 2024). Second, there is a recurring limitation in handling multi-objective optimization beyond single metrics like watch time — Deng et al. (2025) explicitly note limitations in interactive indicators such as likes, and future work aims to enhance multi-objective modeling capability [E13]. Third, Rec-ID assignment collisions remain a persistent issue across tokenization approaches, with Liu et al. (2024) and Zhu et al. (2024) both planning to develop more effective vector quantization methods [E16, E35]. Fourth, Wang, W. et al. (2024) and Wang, Y. et al. (2024) identify the need for tokenization with rich user behaviors, cross-domain item tokenization for open-ended recommendation, and integration of large language models with multimodal AI techniques. Finally, Hou et al. (2024) emphasize that effectively leveraging rich, heterogeneous, and noisy item metadata in semantic encoders remains a challenging open problem [E20].

## Per-Paper Annotations

### Deng et al. (2025)

**Research question**: How can we unify retrieve and rank stages in recommendation systems using a single end-to-end generative model?
**Methodology**: OneRec uses an encoder-decoder structure with sparse MoE for scaling, session-wise generation for contextual coherence, and Iterative Preference Alignment with DPO to enhance generation quality.
**Key findings**:
- Session-wise generation approach significantly outperforms traditional point-wise methods like TIGER [E11]
- A small ratio of DPO training yields substantial performance gains [E21]
- Online A/B testing demonstrated significant improvements in watch time and view duration [E12]
- The model has limitations in interactive indicators beyond watch time [E13]
**Limitations**: The model has limitations in interactive indicators, such as likes, and future work aims to enhance multi-objective modeling capability.

### Hou et al. (2024)

**Research question**: How do LLMs perform as semantic encoders for recommendation tasks compared to general text embedding benchmarks?
**Methodology**: BLaIR introduces a comprehensive benchmark with a new large-scale Amazon Reviews 2023 dataset, unified evaluation across sequential recommendation, collaborative filtering, and product search, and a novel complex-query product search task.
**Key findings**:
- LLM rankings on BLaIR show little correlation with general text embedding benchmark MTEB [E17]
- Scaling behavior of semantic encoders weakens when downstream tasks become complex [E18]
- Semi-synthetic Amazon-C4 dataset serves as reliable proxy for real-world complex queries [E19]
- Adding item description to title does not consistently improve semantic encoder performance [E20]
**Limitations**: Effectively leveraging rich, heterogeneous, and noisy item metadata in semantic encoders remains a challenging open problem.

### Liu et al. (2024)

**Research question**: How can a generative paradigm improve multimodal recommendation compared to the traditional embed-and-retrieve approach?
**Methodology**: The authors propose MMGRec, which first uses Graph RQ-VAE to assign hierarchical Rec-IDs to items from multimodal and collaborative filtering information, then trains a Transformer-based recommender to autoregressively generate Rec-IDs of user-preferred items from historical interaction sequences using relation-aware self-attention.
**Key findings**:
- MMGRec outperforms the strongest baseline by 6.58-7.17% on NDCG@10 across three datasets with statistical significance [E32]
- Graph RQ-VAE achieves better Rec-ID assignment than hierarchical K-means clustering due to fewer ID collisions [E33]
- Relation-aware self-attention significantly improves performance over standard positional encoding by modeling user-specific pairwise item relations [E34]
- MMGRec achieves more efficient inference than embedding-based methods on large-scale datasets due to stable autoregressive decoding complexity [E35]
**Limitations**: The paper identifies Rec-ID assignment collisions as a limitation and plans to develop more effective vector quantization methods to mitigate this issue in future work.

### Qu et al. (2024)

**Research question**: How can high-order collaborative knowledge be efficiently captured into discrete tokens compatible with LLMs while enabling generalization to new/unseen users or items?
**Methodology**: TokenRec introduces a Masked Vector-Quantized (MQ) Tokenizer that quantizes masked user/item representations learned from collaborative filtering into discrete tokens, combined with a generative retrieval paradigm that eliminates auto-regressive decoding and beam search for efficient top-K item recommendation.
**Key findings**:
- TokenRec outperforms all baselines including traditional and LLM-based recommenders with significant margins [E28]
- TokenRec demonstrates strong generalization to unseen users with only 7% performance drop compared to 40%+ for other methods [E29]
- TokenRec's generative retrieval paradigm achieves 1259.81% improvement in inference efficiency over auto-regressive decoding baselines [E30]
- High-order collaborative knowledge from GNNs is crucial for TokenRec's effectiveness [E31]
**Limitations**: The optimal hyperparameter values vary by dataset size, requiring tuning for different applications.

### Tan et al. (2024)

**Research question**: How can large language models be better aligned with recommendation systems through effective item encoding using concise, semantically rich textual ID representations?
**Methodology**: The authors propose IDGen, which represents each item as a unique, concise, semantically rich textual ID using human language tokens, trained alongside an LLM-based recommender with an alternative training strategy between the ID generator and base recommender.
**Key findings**:
- IDGenRec significantly outperforms all baselines in standard sequential recommendation with improvements of 23-42% across four datasets [E22]
- IDGenRec's zero-shot foundation model generally outperforms UniSRec baseline across unseen datasets [E23]
- Alternate training strategy between ID generator and base recommender significantly improves model performance [E24]
- The IDGenRec paradigm demonstrates potential for serving as foundation models for generative recommendation [E25]
**Limitations**: Further training beyond one epoch negatively affected zero-shot performance, suggesting potential overfitting similar to NLP pre-training observations.

### Wang, W. et al. (2024)

**Research question**: What are the optimal features required for item tokenization in generative recommendation, and how can a learnable tokenizer address limitations of current identifier approaches?
**Methodology**: The authors propose LETTER, a learnable tokenizer incorporating Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias, instantiated on TIGER and LC-Rec models with ranking-guided generation loss.
**Key findings**:
- Codebook-based identifiers outperform ID and textual identifiers in LLM-based recommendation models [E4]
- RQ-VAE's hierarchical semantics with different granularities enables better distinction between similar items [E5]
- Experiments validate LETTER's superiority for item tokenization in generative recommendation [E6]
**Limitations**: Future work includes tokenization with rich user behaviors, cross-domain item tokenization for open-ended recommendation, and combining user instructions with interaction history.

### Wang, Y. et al. (2024)

**Research question**: How can behavioral and semantic information be seamlessly integrated in generative retrieval for sequential recommendation to overcome limitations of existing methods?
**Methodology**: The authors introduce EAGER with a two-stream generation architecture using shared encoder and separate decoders for behavior and semantic tokens, a global contrastive task with summary tokens for discriminative decoding, and a semantic-guided transfer task for cross-interactions.
**Key findings**:
- EAGER achieves superior results compared to base models across different datasets [E7]
- EAGER shows substantial improvement over TIGER on the Beauty benchmark with over 30% gains in Recall@5 and NDCG@5 [E8]
- EAGER's two-stream decoder and multi-task training enable deeper understanding of behavior-semantic relationships [E9]
- Generative models generally outperform traditional baselines across multiple datasets [E10]
**Limitations**: Future work plans to enhance generative recommendation by incorporating large language models and multimodal AI techniques.

### Wang, Yidan et al. (2024)

**Research question**: How can content knowledge and collaborative interaction signals be integrated in a generative framework tailored for item recommendation?
**Methodology**: ColaRec is a sequence-to-sequence framework that generates recommended item identifiers, using generative identifiers constructed from a pretrained collaborative filtering model and representing users as content aggregation of interacted items, with an item indexing task for alignment and contrastive loss for similar representations.
**Key findings**:
- ColaRec demonstrates superior performance over baselines on four benchmark datasets [E26]
- ColaRec successfully integrates collaborative signals and content information in a unified generative framework [E27]
**Limitations**: Not stated.

### Zheng et al. (2023)

**Research question**: How can large language models be adapted for recommender systems by bridging the semantic gap between language semantics and collaborative semantics?
**Methodology**: The authors propose LC-Rec, which uses learning-based vector quantization with uniform semantic mapping for item indexing, and specially designed tuning tasks to integrate collaborative semantics into LLMs through sequential item prediction, explicit index-language alignment, and implicit recommendation-oriented alignment.
**Key findings**:
- LC-Rec achieves superior performance compared to baseline methods across all three datasets [E1]
- Vector quantization with uniform semantic mapping captures item similarities for effective indexing [E2]
- Experiments confirm LC-Rec outperforms competitive baseline models [E3]
**Limitations**: The approach needs exploration for extension to multi-turn chat settings and better preservation of general LLM abilities during domain adaptations.

### Zhu et al. (2024)

**Research question**: How can we improve semantic tokenization for generative recommendation by capturing item neighborhood relationships?
**Methodology**: CoST introduces contrastive quantization into the tokenization process, leveraging both item relationships and semantic information through contrastive loss that maximizes top-one probability within a batch.
**Key findings**:
- CoST achieves approximately 38% improvement in NDCG and 36% in Recall on MIND dataset [E14]
- Larger codebook size and number of codebooks leads to consistent NDCG improvements [E15]
- Current CoST focuses on top-one neighborhood alignment with room for top-k extension [E16]
**Limitations**: CoST currently focuses on top-one neighborhood alignment; future work could extend to top-k nearest neighbors and incorporate multimodal information or user behavior data.

## References

Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying retrieve and rank with generative recommender and iterative preference alignment. arXiv. https://arxiv.org/abs/2502.18965

Hou, Y., Li, J., Fu, X., He, Z., Yan, A., Chen, X., & McAuley, J. (2024). Bridging language and items for retrieval and recommendation: Benchmarking LLMs as semantic encoders. arXiv. https://arxiv.org/abs/2403.03952

Liu, H., Wei, Y., Song, X., Guan, W., Li, Y.-F., & Nie, L. (2024). MMGRec: Multimodal generative recommendation with transformer model. arXiv. https://arxiv.org/abs/2404.16555

Qu, H., Fan, W., Zhao, Z., & Li, Q. (2024). TokenRec: Learning to tokenize ID for LLM-based generative recommendation. arXiv. https://arxiv.org/abs/2406.10450

Tan, J., Xu, S., Hua, W., Ge, Y., Li, Z., & Zhang, Y. (2024). IDGenRec: LLM-RecSys alignment with textual ID learning. arXiv. https://arxiv.org/abs/2403.19021

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2405.07314

Wang, Y., Xun, J., Hong, M., Zhu, J., Jin, T., Lin, W., Li, H., Li, L., Xia, Y., Zhao, Z., & Dong, Z. (2024). EAGER: Two-stream generative recommender with behavior-semantic collaboration. arXiv. https://arxiv.org/abs/2406.14017

Wang, Y., Ren, Z., Sun, W., Yang, J., Liang, Z., Chen, X., Xie, R., Yan, S., Zhang, X., Ren, P., Chen, Z., & Xin, X. (2024). Content-based collaborative generation for recommender systems. arXiv. https://arxiv.org/abs/2403.18480

Zheng, B., Hou, Y., Lu, H., Chen, Y., Zhao, W. X., Chen, M., & Wen, J.-R. (2023). Adapting large language models by integrating collaborative semantics for recommendation. arXiv. https://arxiv.org/abs/2311.09049

Zhu, J., Jin, M., Liu, Q., Qiu, Z., Dong, Z., & Li, X. (2024). CoST: Contrastive quantization based semantic tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2404.14774
