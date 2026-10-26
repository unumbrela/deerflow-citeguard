# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30
**Citation format**: APA 7th edition

## Executive Summary

The field of generative recommendation has experienced rapid development between late 2023 and late 2025, with researchers fundamentally reimagining how recommendation systems leverage large language models. The surveyed literature reveals a clear paradigm shift from traditional retrieve-and-rank architectures toward end-to-end generative frameworks that directly generate item recommendations using learned token representations. A central challenge addressed across multiple papers is the effective tokenization of items to bridge collaborative filtering signals with language model semantics. The field demonstrates strong convergence around vector quantization techniques, contrastive learning objectives, and the integration of both behavioral and semantic information streams. Real-world deployment results from industrial systems demonstrate substantial performance gains, with OneRec achieving a 1.6% increase in watch-time when deployed in Kuaishou's production system.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30. Papers were sorted by co-citation relevance and the top 10 were included. The screening process identified 50 papers through search, added 92 from reference expansion, shortlisted 30 candidates, and included 10 papers after scoring (6 from reference expansion). Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Learnable Item Tokenization for LLM Integration

A dominant research direction focuses on transforming recommendation items into discrete tokens compatible with large language models. Traditional recommendation systems rely on ID-based representations that cannot be directly processed by LLMs, creating a fundamental mismatch. Multiple papers propose learnable tokenization frameworks that map items to textual or semantic tokens while preserving collaborative filtering signals.

Zheng et al. (2023) introduced LC-Rec with learning-based vector quantization for semantic-aware item indexing, enabling LLMs to generate items directly from the entire item set without candidate pre-selection. Wang et al. (2024) proposed LETTER, which uses Residual Quantized VAE for semantic regularization combined with contrastive alignment loss for collaborative regularization and diversity loss to mitigate code assignment bias. Qu et al. (2024) developed TokenRec with a Masked Vector-Quantized Tokenizer that quantizes masked user/item representations learned from collaborative filtering into discrete tokens, achieving generalizable tokenization for unseen users and items.

These tokenization approaches share the goal of creating meaningful item representations that capture both semantic content and collaborative relationships, enabling LLMs to reason about recommendations in their native language space.

### Theme 2: Two-Stream and Multi-Modal Architectures

Several papers advocate for architectures that separately process behavioral and semantic information before combining them, recognizing their complementary nature. This two-stream approach acknowledges that user behavior patterns and item semantic content provide distinct but complementary signals for recommendation.

Wang et al. (2024) introduced EAGER with a two-stream generation architecture featuring a shared encoder and separate decoders for behavior and semantic tokens, using global contrastive learning with summary tokens for discriminative decoding. Liu et al. (2024) proposed MMGRec, which uses Graph RQ-VAE to assign Rec-ID tokens from both multimodal and collaborative filtering information, then employs relation-aware self-attention to handle non-sequential interaction sequences.

The relation-aware self-attention mechanism in MMGRec represents an important innovation, exploring element pairwise relations instead of absolute positional encoding to better model user-item interactions that lack inherent sequential ordering.

### Theme 3: End-to-End Generative Frameworks Replacing Cascaded Systems

A significant trend involves replacing traditional cascaded retrieve-and-rank architectures with unified end-to-end generative models. This paradigm shift promises simpler deployment, better optimization, and improved performance by jointly learning retrieval and ranking objectives.

Deng et al. (2025) presented OneRec as the first end-to-end generative model to significantly surpass complex well-designed recommender systems in real-world scenarios. The system uses an encoder-decoder structure with sparse Mixture-of-Experts for scaling and implements session-wise generation for coherent results. The deployment in Kuaishou achieved a 1.6% increase in watch-time, providing strong empirical validation for the end-to-end approach.

Tan et al. (2024) proposed IDGenRec with textual ID learning that enables seamless integration of personalized recommendations into natural language generation, demonstrating zero-shot performance comparable to supervised models on unseen datasets, suggesting potential for foundational generative recommendation models decoupled from original training datasets.

### Theme 4: Contrastive Learning for Better Representations

Contrastive learning objectives emerge as a critical technique across multiple papers for improving item representations and recommendation quality. These methods create discriminative embeddings by contrasting positive and negative examples.

Zhu et al. (2024) developed CoST with contrastive quantization-based semantic tokenization that captures item neighborhood relationships vital for effective item modeling, achieving up to 43% improvement in Recall@5 and 44% improvement in NDCG@5 on the MIND dataset over previous baselines. Wang et al. (2024) incorporated contrastive alignment loss in LETTER to integrate collaborative signals into the tokenization process. EAGER uses global contrastive learning with summary tokens to achieve discriminative decoding for each information type.

The consistent success of contrastive objectives across different frameworks suggests they are essential for learning high-quality representations in generative recommendation systems.

### Theme 5: Content and Collaboration Integration

Multiple approaches seek to integrate content-based item information with collaborative filtering signals, addressing the limitations of purely interaction-based or purely content-based methods.

Wang et al. (2024) proposed ColaRec as a sequence-to-sequence framework that generates recommended item identifiers by modeling both item content and user-item collaborative interactions, using an item indexing task with contrastive loss to align content-based and interaction-based spaces. Hou et al. (2024) introduced BLaIR, a comprehensive benchmark for evaluating LLMs as semantic encoders in recommendation scenarios, including a new large-scale Amazon Reviews 2023 dataset with over 570 million reviews and 48 million items.

The BLaIR benchmark revealed that LLM rankings on recommendation tasks show little correlation with general-purpose embedding benchmarks like MTEB, highlighting the unique challenges of semantic encoding in recommendation contexts and the need for task-specific evaluation.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong agreement on several key points. First, all papers agree that traditional ID-based recommendation systems require fundamental rearchitecting to leverage LLM capabilities effectively. Second, there is consensus that vector quantization techniques are essential for creating discrete token representations from continuous embeddings. Third, multiple papers converge on the importance of contrastive learning objectives for improving representation quality. Fourth, the field agrees that end-to-end generative frameworks offer advantages over cascaded architectures in terms of both performance and deployment simplicity.

**Disagreements**: The literature shows some divergence in architectural choices. While some papers advocate for two-stream architectures that separately process behavioral and semantic information (Wang et al., 2024; Liu et al., 2024), others propose unified single-stream approaches (Zheng et al., 2023; Deng et al., 2025). Additionally, there is variation in how papers handle the item indexing problem—some use learned semantic tokens (Zhu et al., 2024; Qu et al., 2024), while others propose textual IDs using human language tokens (Tan et al., 2024). The optimal balance between content information and collaborative signals also remains an open question, with different frameworks prioritizing these signals differently.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the surveyed papers explicitly address computational efficiency and inference latency in detail, despite the practical importance of these factors for real-world deployment. Second, while several papers mention zero-shot or generalization capabilities, systematic evaluation of cross-domain transfer remains limited. Third, the treatment of cold-start users and items—those with minimal interaction history—is not thoroughly addressed in most frameworks. Fourth, interpretability and explainability of generative recommendations receive limited attention, which may hinder adoption in domains requiring transparent decision-making.

The BLaIR benchmark (Hou et al., 2024) highlights a critical gap in evaluation methodology, showing that general-purpose embedding benchmarks poorly predict recommendation performance. This suggests the need for more standardized, recommendation-specific evaluation protocols across the field.

## Per-Paper Annotations

### Deng et al. (2025)

**Research question**: Can a unified end-to-end generative model replace the cascaded retrieve-and-rank framework in real-world recommender systems while achieving superior performance?

**Methodology**: OneRec uses an encoder-decoder structure with sparse Mixture-of-Experts for scaling, implements session-wise generation for coherent results, and introduces Iterative Preference Alignment with customized Direct Preference Optimization using a reward model to simulate user interactions.

**Key findings**:
- OneRec is the first end-to-end generative model to significantly surpass complex well-designed recommender systems in real-world scenarios
- Sparse MoE architecture scales model capacity without proportionally increasing computational costs
- Session-wise generation produces more elegant and contextually coherent results than point-by-point prediction
- Iterative Preference Alignment with customized DPO sampling significantly improves generated result quality
- Deployment in Kuaishou achieved a 1.6% increase in watch-time, demonstrating substantial real-world improvement

**Limitations**: not stated in abstract

### Hou et al. (2024)

**Research question**: How do large language models perform as semantic encoders for recommendation tasks compared to general-purpose embedding benchmarks?

**Methodology**: The paper introduces BLaIR, a comprehensive benchmark for evaluating LLMs as semantic encoders in recommendation scenarios, including a new large-scale Amazon Reviews 2023 dataset and experiments with 11 leading LLMs across sequential recommendation, collaborative filtering, and product search tasks.

**Key findings**:
- Feature engineering has long been central to recommender systems, but effectively leveraging textual item features remains challenging
- Prior studies rely on general-purpose embedding benchmarks (e.g., MTEB) when selecting LLMs, overlooking unique characteristics of recommendation tasks
- The BLaIR benchmark includes a new Amazon Reviews 2023 dataset with over 570 million reviews and 48 million items
- LLM rankings on BLaIR show little correlation with MTEB rankings, highlighting unique challenges of semantic encoding in recommendation

**Limitations**: not stated in abstract

### Liu et al. (2024)

**Research question**: How can we address the inference cost, interaction modeling, and false-negative issues in multimodal recommendation systems that use the traditional embed-and-retrieve paradigm?

**Methodology**: The authors propose MMGRec, a generative paradigm for multimodal recommendation that uses Graph RQ-VAE to assign Rec-ID tokens to items from multimodal and collaborative filtering information, then trains a Transformer-based recommender with relation-aware self-attention to autoregressively generate Rec-IDs of user-preferred items based on historical interaction sequences.

**Key findings**:
- The generative paradigm systematically predicts token tuples identifying recommended items in an autoregressive manner
- Graph RQ-VAE creates semantically meaningful Rec-ID tokens from multimodal and collaborative filtering information
- Relation-aware self-attention handles non-sequential interaction sequences by exploring element pairwise relations instead of absolute positional encoding
- Extensive experiments demonstrate MMGRec's effectiveness compared with state-of-the-art methods

**Limitations**: not stated in abstract

### Qu et al. (2024)

**Research question**: How can we efficiently capture high-order collaborative knowledge into discrete tokens compatible with LLMs while generalizing to new/unseen users or items in recommendation systems?

**Methodology**: The authors propose TokenRec, a framework featuring a Masked Vector-Quantized (MQ) Tokenizer that quantizes masked user/item representations learned from collaborative filtering into discrete tokens, combined with a generative retrieval paradigm that recommends top-K items without auto-regressive decoding or beam search.

**Key findings**:
- TokenRec achieves smooth incorporation of high-order collaborative knowledge into LLM-based recommendation systems
- The MQ Tokenizer enables generalizable tokenization of users and items, including those not seen during training
- The generative retrieval paradigm significantly reduces inference time by eliminating time-consuming auto-regressive decoding and beam search
- Comprehensive experiments show TokenRec outperforms both traditional recommender systems and emerging LLM-based recommender systems

**Limitations**: not stated in abstract

### Tan et al. (2024)

**Research question**: How can recommendation items be effectively encoded within the text-to-text framework using concise yet meaningful ID representations?

**Methodology**: The paper proposes IDGen, representing each item as a unique, concise, semantically rich textual ID using human language tokens, trained alongside an LLM-based recommender. The approach is evaluated on sequential recommendation tasks and tested as a foundation model on 6 unseen datasets in a zero-shot setting.

**Key findings**:
- Current generative recommendation research struggles to encode items using concise yet meaningful ID representations within the text-to-text framework
- IDGen enables seamless integration of personalized recommendations into natural language generation
- The framework consistently surpasses existing models in sequential recommendation under standard experimental settings
- The zero-shot performance of the pre-trained foundation model is comparable to or better than some traditional recommendation models based on supervised training
- The approach suggests potential for a foundational generative recommendation model decoupled from original datasets

**Limitations**: not stated in abstract

### Wang, Wenjie et al. (2024)

**Research question**: How can item tokenization be improved to effectively transform recommendation data into the language space of LLMs for generative recommendation?

**Methodology**: The authors propose LETTER, a learnable tokenizer that uses Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias, instantiated on two models with ranking-guided generation loss.

**Key findings**:
- LETTER integrates hierarchical semantics, collaborative signals, and code assignment diversity to satisfy identifier requirements
- Residual Quantized VAE enables semantic regularization of item representations
- Contrastive alignment loss incorporates collaborative signals into the tokenization process
- Diversity loss successfully mitigates code assignment bias in tokenization
- Experiments on three datasets show LETTER advances state-of-the-art in LLM-based generative recommendation

**Limitations**: not stated in abstract

### Wang, Ye et al. (2024)

**Research question**: How can behavioral and semantic information be effectively combined in generative retrieval for sequential recommendation to leverage their complementary nature?

**Methodology**: EAGER employs a two-stream generation architecture with a shared encoder and separate decoders for behavior and semantic tokens, uses global contrastive learning with summary tokens for discriminative decoding, and implements semantic-guided transfer tasks for cross-interaction.

**Key findings**:
- Two-stream architecture successfully handles both behavioral and semantic feature types with confidence-based ranking
- Global contrastive task with summary tokens achieves discriminative decoding for each information type
- Semantic-guided transfer task promotes cross-interactions through reconstruction and estimation objectives
- EAGER demonstrates superior performance compared to existing methods on four public benchmarks

**Limitations**: not stated in abstract

### Wang, Yidan et al. (2024)

**Research question**: How can content knowledge and collaborative interaction signals be integrated in a generative framework tailored for item recommendation?

**Methodology**: The paper proposes ColaRec, a sequence-to-sequence framework that generates recommended item identifiers by modeling both item content and user-item collaborative interactions. The framework uses generative identifiers from a pretrained collaborative filtering model and introduces an item indexing task with contrastive loss to align content-based and interaction-based spaces.

**Key findings**:
- Generative models have emerged as a promising utility to enhance recommender systems
- Existing LLM-based methods fundamentally rely on textual language generation, which is not fully aligned with recommendation tasks
- ColaRec captures both collaborative signals and content information in a unified framework
- The contrastive loss ensures that items with similar collaborative GIDs have similar content representations
- Empirical results on four benchmark datasets demonstrate the superior performance of ColaRec

**Limitations**: not stated in abstract

### Zheng et al. (2023)

**Research question**: How can large language models be adapted to better integrate collaborative semantics from recommender systems to overcome the semantic gap between language and item ID-based recommendation?

**Methodology**: The authors propose LC-Rec, an LLM-based recommendation model with two main components: a learning-based vector quantization method for semantic-aware item indexing, and specially designed fine-tuning tasks to align collaborative semantics with language semantics in LLMs.

**Key findings**:
- LC-Rec successfully generates items directly from the entire item set without requiring candidate item pre-selection
- The vector quantization method assigns meaningful and non-conflicting item indices that capture collaborative semantics
- Fine-tuning tasks enable deep integration of language and collaborative semantics in LLMs
- LC-Rec outperforms both traditional recommenders and existing LLM-based recommenders in extensive experiments

**Limitations**: not stated in abstract

### Zhu et al. (2024)

**Research question**: How can semantic tokenization for generative recommendation better capture item neighborhood relationships vital for effective item modeling?

**Methodology**: The paper proposes CoST, a contrastive quantization-based semantic tokenization approach that harnesses both item relationships and semantic information to learn semantic tokens. The method is evaluated on the MIND dataset comparing against previous baselines.

**Key findings**:
- Existing vector quantization methods with reconstruction loss (e.g., RQ-VAE) fail to capture essential neighborhood relationships for effective item modeling
- CoST achieves up to 43% improvement in Recall@5 on the MIND dataset over previous baselines
- CoST achieves up to 44% improvement in NDCG@5 on the MIND dataset over previous baselines
- Semantic tokenization has a significant impact on generative recommendation performance

**Limitations**: not stated in abstract

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
