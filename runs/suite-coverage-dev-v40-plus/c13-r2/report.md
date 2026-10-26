# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "generative recommendation", category cs.IR, published between 2023-10-31 and 2025-10-30
**Citation format**: APA 7th edition

## Executive Summary

The field of generative recommendation has undergone rapid transformation from 2023 to 2025, with researchers fundamentally reimagining how recommendation systems can leverage large language models and generative paradigms. The surveyed literature reveals a clear shift from traditional retrieve-and-rank cascades toward end-to-end generative frameworks that directly produce item recommendations as token sequences. A dominant research direction focuses on item tokenization strategies—learning to represent items as discrete tokens that bridge collaborative filtering semantics with language model capabilities. Multiple approaches including vector quantization, contrastive learning, and residual quantization have emerged to create meaningful item identifiers that preserve both semantic and collaborative information. The literature demonstrates strong convergence on the effectiveness of generative paradigms, with reported improvements of up to 44% over traditional baselines, and early real-world deployments showing measurable business impact.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30. Papers were sorted by relevance through citation-based ranking, and the top 10 were included. The screening process identified 50 papers through search, added 91 from citation expansion, shortlisted 30, and screened 30 with scores distributed as: 23 papers scored 3, 6 papers scored 2, and 1 paper scored 1. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Item Tokenization and ID Learning

A central challenge in generative recommendation is transforming items into discrete tokens that language models can effectively process while preserving collaborative semantics. Multiple papers address this through different quantization and learning strategies. Zheng et al. (2023) introduced LC-Rec with learning-based vector quantization and uniform semantic mapping for item indexing, directly generating items from the entire item set without candidate reliance. Wang et al. (2024) proposed LETTER, incorporating Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative signals, and diversity loss to mitigate code assignment bias. Zhu et al. (2024) developed CoST using contrastive quantization to better capture item neighborhood relationships, achieving 43-44% improvements on the MIND dataset. Qu et al. (2024) presented TokenRec with a Masked Vector-Quantized Tokenizer that quantizes masked user/item representations into discrete tokens, providing generalizable tokenization for unseen users and items. Liu et al. (2024) extended this to multimodal settings with Graph RQ-VAE assigning Rec-IDs as tuples of semantically meaningful tokens from both multimodal and collaborative information.

### Theme 2: Architecture Design for Generative Recommendation

The architectural patterns for generative recommendation have evolved to handle the unique requirements of integrating behavioral and semantic information. Wang et al. (2024) introduced EAGER with a two-stream generation architecture using a shared encoder and separate decoders for behavior and semantic tokens, plus global contrastive tasks with summary tokens. Deng et al. (2025) proposed OneRec with an encoder-decoder structure using sparse Mixture-of-Experts for scaling capacity without proportional FLOP increases, employing session-wise generation for coherent results. Tan et al. (2024) developed IDGenRec representing items as unique, concise, semantically rich textual IDs using human language tokens. Wang et al. (2024) designed ColaRec as a sequence-to-sequence framework generating item identifiers using generative identifiers from pretrained collaborative filtering models. Liu et al. (2024) employed Transformer-based recommenders with relation-aware self-attention to handle non-sequential interaction sequences.

### Theme 3: Integration of Collaborative and Semantic Information

A recurring challenge is effectively combining collaborative filtering signals with semantic content understanding. Zheng et al. (2023) designed specialized tuning tasks to enforce deep integration of language and collaborative semantics in LLMs. Wang et al. (2024) used contrastive alignment loss in LETTER to enable collaborative regularization alongside semantic regularization. Zhu et al. (2024) harnessed both item relationships and semantic information in CoST's contrastive quantization approach. Wang et al. (2024) conducted alignment between content-based semantic space and interaction-based collaborative space through item indexing tasks in ColaRec. Qu et al. (2024) incorporated high-order collaborative knowledge into discrete tokens through the MQ Tokenizer. The literature shows consistent emphasis on ensuring that generative models do not lose the collaborative signals that traditional recommenders excel at capturing.

### Theme 4: Efficiency and Scalability Considerations

As generative recommendation moves toward production deployment, efficiency concerns have become prominent. Qu et al. (2024) introduced a generative retrieval paradigm that recommends top-K items without requiring auto-regressive decoding and beam search, significantly reducing inference time. Deng et al. (2025) employed sparse Mixture-of-Experts in OneRec to scale model capacity without proportionally increasing computational costs, achieving deployment in Kuaishou with 1.6% watch-time increase. Liu et al. (2024) addressed the inference cost issues of traditional embed-and-retrieve paradigms through their generative approach. The shift from point-by-point to session-wise generation represents an architectural choice balancing coherence and computational efficiency.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. All papers converge on the effectiveness of generative paradigms over traditional retrieve-and-rank approaches, with consistent reporting of superior performance across benchmarks. There is consensus that item tokenization is a critical component requiring careful design to preserve both semantic and collaborative information. Multiple papers independently arrived at using vector quantization variants (Zheng et al., 2023; Wang et al., 2024; Zhu et al., 2024; Qu et al., 2024; Liu et al., 2024), suggesting this is a robust approach. The field agrees that end-to-end generative models can directly produce recommendations without candidate generation stages.

**Disagreements**: While the literature shows more convergence than disagreement, subtle differences exist in architectural choices. Some works favor two-stream architectures separating behavioral and semantic processing (Wang et al., 2024), while others pursue unified representations (Zheng et al., 2023; Tan et al., 2024). The choice between autoregressive generation (Liu et al., 2024) versus non-autoregressive retrieval (Qu et al., 2024) represents a trade-off between generation quality and inference speed that different papers prioritize differently. The extent to which textual IDs should carry semantic meaning versus serving as pure identifiers varies across approaches.

## Gaps and Open Questions

Several limitations emerge consistently across the literature. None of the papers explicitly stated limitations in their abstracts, suggesting either space constraints or reluctance to highlight weaknesses. However, implicit gaps include: the generalizability of tokenization strategies across domains remains underexplored; the computational cost of training generative recommenders compared to traditional approaches needs more systematic analysis; the interpretability of generative recommendations and their token sequences requires further investigation; the handling of cold-start scenarios for entirely new items or users needs more attention beyond Qu et al.'s (2024) mention of generalization to unseen entities; the integration of user feedback and preference alignment in generative frameworks is only beginning to be addressed (Deng et al., 2025); and the long-term user experience implications of generative versus traditional recommendation remains an open empirical question.

## Per-Paper Annotations

### Deng et al. (2025)

**Research question**: How can the cascaded retrieve-and-rank framework in recommender systems be replaced with a unified end-to-end generative model that surpasses existing complex systems?
**Methodology**: OneRec uses an encoder-decoder structure with sparse Mixture-of-Experts for scaling, session-wise generation approach for coherent results, and an Iterative Preference Alignment module with Direct Preference Optimization customized for recommendation systems with a reward model to simulate user generation.
**Key findings**:
- First end-to-end generative model that significantly surpasses current complex recommender systems in real-world scenarios
- Sparse MoE scales model capacity without proportionally increasing computational FLOPs
- Session-wise generation is more elegant and contextually coherent than point-by-point generation
- Iterative Preference Alignment with customized DPO sampling enhances generated result quality
- Deployment in Kuaishou achieved a 1.6% increase in watch-time
**Limitations**: not stated in abstract

### Hou et al. (2024)

**Research question**: How do large language models perform as semantic encoders for recommendation tasks compared to general-purpose embedding benchmarks?
**Methodology**: Introduced BLaIR, a comprehensive benchmark for evaluating LLMs as semantic encoders in recommendation scenarios, including a new large-scale Amazon Reviews 2023 dataset and experiments with 11 leading LLMs across sequential recommendation, collaborative filtering, and product search tasks.
**Key findings**:
- LLM rankings on BLaIR show little correlation with MTEB general-purpose embedding benchmarks
- Recommendation tasks present unique challenges not captured by general-purpose benchmarks
- The benchmark covers sequential recommendation, collaborative filtering, and product search
- New complex-query product search task includes both semi-synthetic and real-world evaluation datasets
**Limitations**: not stated in abstract

### Liu et al. (2024)

**Research question**: How can multimodal recommendation overcome the inference cost, interaction modeling, and false-negative issues of the traditional embed-and-retrieve paradigm?
**Methodology**: MMGRec uses Graph RQ-VAE to assign Rec-ID (a tuple of semantically meaningful tokens) to each item from multimodal and collaborative filtering information, then trains a Transformer-based recommender with relation-aware self-attention to generate Rec-IDs of user-preferred items in an autoregressive manner based on historical interaction sequences.
**Key findings**:
- The generative paradigm successfully replaces the embed-and-retrieve approach for multimodal recommendation
- Graph RQ-VAE effectively assigns unique Rec-IDs consisting of semantically meaningful tokens to items
- The Transformer-based recommender can systematically predict token tuples identifying recommended items in an autoregressive manner
- Relation-aware self-attention mechanism handles non-sequential interaction sequences by exploring element pairwise relations instead of absolute positional encoding
- Extensive experiments demonstrate MMGRec's effectiveness compared with state-of-the-art methods
**Limitations**: not stated in abstract

### Qu et al. (2024)

**Research question**: How can user and item tokenization be improved to efficiently capture high-order collaborative knowledge into discrete tokens compatible with LLMs while generalizing to unseen users and items?
**Methodology**: TokenRec features a Masked Vector-Quantized (MQ) Tokenizer that quantizes masked user/item representations learned from collaborative filtering into discrete tokens, combined with a generative retrieval paradigm that recommends top-K items without requiring auto-regressive decoding and beam search.
**Key findings**:
- Achieves seamless alignment of LLMs with recommendations through effective ID tokenization
- The MQ Tokenizer successfully incorporates high-order collaborative knowledge into discrete tokens
- Provides generalizable tokenization for new/unseen users and items not in the training corpus
- The generative retrieval paradigm significantly reduces inference time by eliminating time-consuming auto-regressive decoding and beam search
- Comprehensive experiments demonstrate TokenRec outperforms both traditional recommender systems and emerging LLM-based recommender systems
**Limitations**: not stated in abstract

### Tan et al. (2024)

**Research question**: How can recommendation items be effectively encoded within text-to-text frameworks using concise yet meaningful ID representations?
**Methodology**: IDGen represents each item as a unique, concise, semantically rich textual ID using human language tokens, trained alongside an LLM-based recommender. Evaluated on sequential recommendation tasks and tested as a foundation model on 6 unseen datasets in a zero-shot setting.
**Key findings**:
- IDGen framework consistently surpasses existing models in sequential recommendation under standard experimental settings
- Zero-shot performance of the pre-trained foundation model is comparable to or better than traditional recommendation models based on supervised training
- The approach enables seamless integration of personalized recommendations into natural language generation
- User history expressed in natural language is decoupled from the original dataset, suggesting potential for foundational generative recommendation models
**Limitations**: not stated in abstract

### Wang, J. et al. (2024) [EAGER]

**Research question**: How can generative recommendation frameworks effectively integrate both behavioral and semantic information to overcome the limitations of focusing on only one aspect?
**Methodology**: EAGER introduces a generative recommendation framework with a two-stream generation architecture using a shared encoder and two separate decoders for behavior and semantic tokens, plus global contrastive tasks with summary tokens and semantic-guided transfer tasks for cross-interactions.
**Key findings**:
- Seamlessly integrates both behavioral and semantic information through a two-stream architecture
- The shared encoder with two separate decoders enables discriminative decoding for each type of information
- Global contrastive tasks with summary tokens achieve discriminative decoding
- Semantic-guided transfer tasks promote cross-interactions through reconstruction and estimation objectives
- Demonstrates superior performance compared to existing methods on four public benchmarks
**Limitations**: not stated in abstract

### Wang, W. et al. (2024) [LETTER]

**Research question**: How can item tokenization be improved to effectively transform recommendation data into the language space of LLMs for generative recommendation?
**Methodology**: LETTER proposes a learnable tokenizer that incorporates Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias, instantiated on two models with ranking-guided generation loss.
**Key findings**:
- Integrates hierarchical semantics, collaborative signals, and code assignment diversity to satisfy essential identifier requirements
- Residual Quantized VAE provides semantic regularization for item tokenization
- Contrastive alignment loss enables collaborative regularization
- Diversity loss mitigates code assignment bias
- Experiments on three datasets validate LETTER's superiority, advancing the state-of-the-art in LLM-based generative recommendation
**Limitations**: not stated in abstract

### Wang, Y. et al. (2024) [ColaRec]

**Research question**: How can content knowledge and collaborative interaction signals be integrated in a generative framework tailored for item recommendation?
**Methodology**: ColaRec is a sequence-to-sequence framework that generates recommended item identifiers using generative identifiers constructed from pretrained collaborative filtering models, with item indexing task for alignment and contrastive loss to ensure similar collaborative GIDs have similar content representations.
**Key findings**:
- Captures both collaborative signals and content information in a unified framework
- The framework is tailored for directly generating recommended item identifiers rather than textual language generation
- Item indexing task conducts alignment between content-based semantic space and interaction-based collaborative space
- Empirical results on four benchmark datasets demonstrate superior performance of ColaRec
**Limitations**: not stated in abstract

### Zheng et al. (2023)

**Research question**: How can large language models be adapted to better integrate collaborative semantics for recommender systems given the semantic gap between language and item ID-based recommendations?
**Methodology**: LC-Rec is a new LLM-based recommendation model with two major contributions: a learning-based vector quantization method with uniform semantic mapping for item indexing, and specially designed tuning tasks to enhance integration of collaborative semantics in LLMs.
**Key findings**:
- LC-Rec can directly generate items from the entire item set for recommendation without relying on candidate items
- The learning-based vector quantization method assigns meaningful and non-conflicting item indices
- Fine-tuning tasks enforce LLMs to deeply integrate language and collaborative semantics characterized by learned item indices
- Extensive experiments show LC-Rec outperforms competitive baselines including traditional recommenders and existing LLM-based recommenders
**Limitations**: not stated in abstract

### Zhu et al. (2024)

**Research question**: How can semantic tokenization for generative recommendation better capture item neighborhood relationships vital for effective item modeling?
**Methodology**: CoST is a contrastive quantization-based semantic tokenization approach that harnesses both item relationships and semantic information to learn semantic tokens. Evaluated on the MIND dataset comparing against existing baselines using Recall@5 and NDCG@5 metrics.
**Key findings**:
- Achieves up to 43% improvement in Recall@5 on the MIND dataset over previous baselines
- Achieves up to 44% improvement in NDCG@5 on the MIND dataset over previous baselines
- Semantic tokenization has significant impact on generative recommendation performance
- Contrastive quantization better captures neighborhood relationships compared to vector quantization with reconstruction loss
**Limitations**: not stated in abstract

## References

Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying retrieve and rank with generative recommender and iterative preference alignment. arXiv. https://arxiv.org/abs/2502.18965

Hou, Y., Li, J., Fu, X., He, Z., Yan, A., Chen, X., & McAuley, J. (2024). Bridging language and items for retrieval and recommendation: Benchmarking LLMs as semantic encoders. arXiv. https://arxiv.org/abs/2403.03952

Liu, H., Wei, Y., Song, X., Guan, W., Li, Y.-F., & Nie, L. (2024). MMGRec: Multimodal generative recommendation with transformer model. arXiv. https://arxiv.org/abs/2404.16555

Qu, H., Fan, W., Zhao, Z., & Li, Q. (2024). TokenRec: Learning to tokenize ID for LLM-based generative recommendation. arXiv. https://arxiv.org/abs/2406.10450

Tan, J., Xu, S., Hua, W., Ge, Y., Li, Z., & Zhang, Y. (2024). IDGenRec: LLM-RecSys alignment with textual ID learning. arXiv. https://arxiv.org/abs/2403.19021

Wang, J., Xun, J., Hong, M., Zhu, J., Jin, T., Lin, W., Li, H., Li, L., Xia, Y., Zhao, Z., & Dong, Z. (2024). EAGER: Two-stream generative recommender with behavior-semantic collaboration. arXiv. https://arxiv.org/abs/2406.14017

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2405.07314

Wang, Y., Ren, Z., Sun, W., Yang, J., Liang, Z., Chen, X., Xie, R., Yan, S., Zhang, X., Ren, P., Chen, Z., & Xin, X. (2024). Content-based collaborative generation for recommender systems. arXiv. https://arxiv.org/abs/2403.18480

Zheng, B., Hou, Y., Lu, H., Chen, Y., Zhao, W. X., Chen, M., & Wen, J.-R. (2023). Adapting large language models by integrating collaborative semantics for recommendation. arXiv. https://arxiv.org/abs/2311.09049

Zhu, J., Jin, M., Liu, Q., Qiu, Z., Dong, Z., & Li, X. (2024). CoST: Contrastive quantization based semantic tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2404.14774
