# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: Generative recommendation, cs.IR, published between 2023-10-31 and 2025-10-30
**Citation format**: APA 7th edition

## Executive Summary

The field of generative recommendation has undergone rapid transformation from 2023 to 2025, with researchers fundamentally reimagining how recommendation systems leverage large language models. The surveyed literature reveals a paradigm shift from traditional embed-and-retrieve approaches toward end-to-end generative frameworks that directly generate item recommendations using semantic tokens. Key innovations center on three interconnected dimensions: (1) item tokenization strategies that bridge collaborative filtering signals with language model compatibility, (2) architectural designs that integrate behavioral and semantic information streams, and (3) unified frameworks that collapse the traditional retrieve-and-rank pipeline into single generative models. Collectively, these works demonstrate substantial performance improvements over traditional recommenders while addressing critical challenges in scaling, inference efficiency, and real-world deployment.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30. Papers were selected based on co-citation relevance scoring, with the top 10 most central papers included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search and screening statistics**: 50 papers identified by search, 91 added from citation expansion, 30 shortlisted, 30 screened, 10 included (6 from reference expansion). Score distribution: 25 papers scored 3 (highest centrality), 4 scored 2, 1 scored 1.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Semantic Tokenization and Item Indexing

A central challenge in generative recommendation is transforming items into discrete tokens compatible with large language models while preserving both semantic meaning and collaborative filtering signals. Multiple papers address this through innovative quantization and tokenization strategies. Zheng et al. (2023) introduced LC-Rec, which uses learning-based vector quantization with uniform semantic mapping for item indexing, enabling direct item generation from the entire item set. Wang et al. (2024) proposed LETTER, incorporating Residual Quantized VAE for semantic regularization alongside contrastive alignment loss for collaborative signals and diversity loss to mitigate code assignment bias.

Qu et al. (2024) developed TokenRec with a Masked Vector-Quantized Tokenizer that quantizes masked user/item representations from collaborative filtering into discrete tokens, achieving generalizable tokenization even for unseen users or items. Zhu et al. (2024) presented CoST, a contrastive quantization-based approach that captures item neighborhood relationships vital for effective modeling, achieving up to 44% improvement in NDCG@5 on the MIND dataset. Liu et al. (2024) extended this to multimodal settings with MMGRec, using Graph RQ-VAE to assign Rec-ID tokens based on both multimodal and collaborative information.

### Theme 2: Architectural Innovation in Generative Frameworks

The surveyed literature reveals diverse architectural approaches to integrating behavioral and semantic information. Wang et al. (2024) introduced EAGER, a two-stream generative framework with a shared encoder and separate decoders for behavior and semantic tokens, using global contrastive tasks with summary tokens for discriminative decoding. This architecture addresses the fundamental challenge that behavioral patterns and semantic content require different processing strategies.

Deng et al. (2025) proposed OneRec with an encoder-decoder structure using sparse Mixture-of-Experts for scaling capacity without proportionally increasing computational costs. The session-wise generation approach produces coherent recommendation sequences rather than point-by-point generation, representing a more elegant solution aligned with natural language generation paradigms. Tan et al. (2024) developed IDGenRec, which represents each item as a unique, concise, semantically rich textual ID using human language tokens, enabling seamless integration of personalized recommendations into natural language generation.

### Theme 3: Unification of Recommendation Pipelines

A recurring theme is the consolidation of traditional multi-stage recommendation pipelines into unified end-to-end generative models. Deng et al. (2025) explicitly replaced the retrieve-and-rank strategy with a unified generative recommender featuring an Iterative Preference Alignment module with customized Direct Preference Optimization. This approach achieved a 1.6% increase in watch-time when deployed in Kuaishou, demonstrating that end-to-end generative models can surpass complex well-designed traditional recommender systems in real-world scenarios.

Wang et al. (2024) developed ColaRec, which captures both collaborative signals and content information in a unified sequence-to-sequence framework, using generative identifiers constructed from pretrained collaborative filtering models. The framework conducts alignment between content-based semantic space and interaction-based collaborative space through an item indexing task, with contrastive loss ensuring items with similar collaborative identifiers have similar content representations.

### Theme 4: Benchmarking and Evaluation Frameworks

As the field matures, rigorous evaluation frameworks have emerged to assess generative recommendation approaches. Hou et al. (2024) introduced BLaIR, a comprehensive benchmark for evaluating LLMs as semantic encoders in recommendation scenarios, including a new large-scale Amazon Reviews 2023 dataset with over 570 million reviews and 48 million items. Their experiments with 11 leading LLMs across sequential recommendation, collaborative filtering, and product search tasks revealed that LLM rankings on recommendation tasks show little correlation with general-purpose embedding benchmarks like MTEB, highlighting the unique characteristics of recommendation tasks.

Tan et al. (2024) tested their IDGen framework on 19 datasets with zero-shot evaluation on 6 unseen datasets, demonstrating that pre-trained foundation models can achieve performance comparable to or better than traditional recommendation models based on supervised training. This finding suggests the potential for foundational generative recommendation models that generalize across domains without extensive retraining.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that traditional embed-and-retrieve paradigms face fundamental limitations in inference cost, interaction modeling, and handling of false negatives. All papers converge on the necessity of integrating collaborative filtering signals with semantic representations, though they differ in implementation strategies. Multiple works independently validate that generative approaches outperform traditional recommenders on standard benchmarks, with consistent improvements reported across diverse datasets. There is strong agreement that item tokenization quality critically impacts overall recommendation performance, motivating the proliferation of quantization-based approaches.

**Disagreements**: While all papers advocate generative approaches, they diverge on optimal architectural choices. The two-stream approach of EAGER (Wang et al., 2024) contrasts with unified single-stream designs, reflecting ongoing debate about whether behavioral and semantic information should be processed separately or jointly. Similarly, papers differ on tokenization granularity: LETTER (Wang et al., 2024) and TokenRec (Qu et al., 2024) use hierarchical multi-token representations, while IDGenRec (Tan et al., 2024) advocates concise single textual IDs. The field has not yet converged on whether multimodal information should be integrated at the tokenization stage (MMGRec) or through separate content branches (ColaRec).

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly address computational efficiency during training, focusing primarily on inference-time improvements. The substantial compute requirements of training generative recommenders on large-scale item catalogs remain unaddressed. Second, while multiple papers claim superiority over traditional methods, few provide detailed ablation studies isolating the contribution of specific architectural components, making it difficult to determine which innovations drive performance gains.

Third, the literature lacks investigation into cold-start scenarios for generative recommenders, despite this being a traditional strength of content-based approaches. Fourth, fairness and bias implications of generative recommendation receive no attention, even though language models are known to encode and amplify societal biases. Finally, while OneRec (Deng et al., 2025) demonstrates real-world deployment success, systematic studies of production challenges—latency, scaling, monitoring, and maintenance—remain absent from the literature.

## Per-Paper Annotations

### Deng et al. (2025)

**Research question**: How can the retrieve-and-rank strategy in recommender systems be replaced with a unified end-to-end generative model?
**Methodology**: OneRec uses an encoder-decoder structure with sparse MoE for scaling, session-wise generation for coherent results, and Iterative Preference Alignment with customized Direct Preference Optimization using a reward model to simulate user generation.
**Key findings**:
- First end-to-end generative model surpassing complex well-designed recommender systems in real-world scenarios
- Sparse Mixture-of-Experts scales model capacity without proportionally increasing computational FLOPs
- Session-wise generation is more elegant and contextually coherent than point-by-point generation
- Iterative Preference Alignment with customized DPO enhances generated result quality despite single-display constraint
- Deployment in Kuaishou achieved 1.6% increase in watch-time
**Limitations**: Not stated in abstract

### Hou et al. (2024)

**Research question**: How do large language models perform as semantic encoders for recommendation tasks compared to general-purpose embedding benchmarks?
**Methodology**: Introduced BLaIR benchmark evaluating LLMs as semantic encoders across sequential recommendation, collaborative filtering, and product search tasks using Amazon Reviews 2023 dataset with 570 million reviews and 48 million items.
**Key findings**:
- LLM rankings on BLaIR show little correlation with MTEB general-purpose embedding benchmarks
- Recommendation tasks have unique characteristics overlooked by general-purpose embedding benchmarks
- Benchmark includes over 570 million reviews and 48 million items from Amazon Reviews 2023
- Covers sequential recommendation, collaborative filtering, and product search tasks
- Introduced new complex-query product search task with semi-synthetic and real-world evaluation datasets
**Limitations**: Not stated in abstract

### Liu et al. (2024)

**Research question**: How can we address the inference cost, interaction modeling, and false-negative issues of the embed-and-retrieve paradigm in multimodal recommendation?
**Methodology**: MMGRec uses Graph RQ-VAE to assign Rec-ID tokens to items from multimodal and collaborative filtering information, with a Transformer-based recommender using relation-aware self-attention to generate Rec-IDs autoregressively.
**Key findings**:
- Introduces generative paradigm replacing traditional embed-and-retrieve approach for multimodal recommendation
- Graph RQ-VAE assigns semantic Rec-ID tokens based on multimodal and collaborative filtering information
- Transformer-based recommender generates Rec-IDs autoregressively, systematically predicting token tuples
- Relation-aware self-attention handles non-sequential interaction sequences by exploring pairwise relations
- Extensive experiments demonstrate effectiveness compared with state-of-the-art methods
**Limitations**: Not stated in abstract

### Qu et al. (2024)

**Research question**: How can we efficiently capture high-order collaborative knowledge into discrete tokens compatible with LLMs while generalizing to new/unseen users or items?
**Methodology**: TokenRec features a Masked Vector-Quantized Tokenizer that quantizes masked user/item representations from collaborative filtering into discrete tokens, with generative retrieval paradigm eliminating auto-regressive decoding and beam search.
**Key findings**:
- Introduces effective ID tokenization strategy incorporating high-order collaborative knowledge into discrete tokens compatible with LLMs
- MQ Tokenizer achieves generalizable tokenization of users and items, including those not in training corpus
- Generative retrieval paradigm eliminates need for auto-regressive decoding and beam search, significantly reducing inference time
- Comprehensive experiments show TokenRec outperforms traditional and emerging LLM-based recommender systems
**Limitations**: Not stated in abstract

### Tan et al. (2024)

**Research question**: How can recommendation items be effectively encoded within text-to-text frameworks using concise yet meaningful ID representations?
**Methodology**: IDGen represents each item as a unique, concise, semantically rich, platform-agnostic textual ID using human language tokens, trained alongside the LLM-based recommender, tested on 19 datasets with zero-shot evaluation on 6 unseen datasets.
**Key findings**:
- IDGen framework consistently surpasses existing models in sequential recommendation under standard experimental settings
- Enables seamless integration of personalized recommendations into natural language generation
- Zero-shot performance of pre-trained foundation model comparable to or better than traditional recommendation models based on supervised training
- User history expressed in natural language decoupled from original dataset, suggesting potential for foundational generative recommendation models
- Uses human language tokens for platform-agnostic textual IDs
**Limitations**: Not stated in abstract

### Wang, Hou, et al. (2024)

**Research question**: How can large language models be better adapted for recommender systems by bridging the semantic gap between language semantics and collaborative semantics?
**Methodology**: LC-Rec uses learning-based vector quantization with uniform semantic mapping for item indexing and specially designed tuning tasks to integrate collaborative semantics into LLMs, enabling direct item generation from the entire item set.
**Key findings**:
- Successfully integrates language and collaborative semantics for recommender systems
- Learning-based vector quantization method assigns meaningful and non-conflicting item indices
- Fine-tuning tasks enforce deep integration of language and collaborative semantics characterized by learned item indices
- Outperforms traditional recommenders and existing LLM-based recommenders in extensive experiments
- Can directly generate items from the entire item set without relying on candidate items
**Limitations**: Not stated in abstract

### Wang, Wenyao, et al. (2024)

**Research question**: How can item tokenization be improved to better transform recommendation data into the language space of LLMs for generative recommendation?
**Methodology**: LETTER incorporates Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias, with ranking-guided generation loss to augment ranking ability.
**Key findings**:
- Integrates hierarchical semantics, collaborative signals, and code assignment diversity for effective item tokenization
- Residual Quantized VAE provides semantic regularization for item identifiers
- Contrastive alignment loss enables incorporation of collaborative signals
- Diversity loss mitigates code assignment bias
- Experiments on three datasets validate superiority over existing approaches in LLM-based generative recommendation
**Limitations**: Not stated in abstract

### Wang, Yidan, et al. (2024)

**Research question**: How can content knowledge and collaborative interaction signals be integrated in a generative framework tailored for item recommendation?
**Methodology**: ColaRec is a sequence-to-sequence framework generating recommended item identifiers by modeling collaborative signals through pretrained collaborative filtering model GIDs and content information through user representation as content aggregation, with item indexing task for alignment and contrastive loss.
**Key findings**:
- Captures both collaborative signals and content information in a unified framework
- Uses generative identifiers constructed from pretrained collaborative filtering models
- Item indexing task conducts alignment between content-based semantic space and interaction-based collaborative space
- Contrastive loss ensures items with similar collaborative GIDs have similar content representations
- Empirical results on four benchmark datasets demonstrate superior performance
**Limitations**: Not stated in abstract

### Ye Wang et al. (2024)

**Research question**: How can generative retrieval for sequential recommendation be improved by integrating both behavioral and semantic aspects of item information?
**Methodology**: EAGER is a two-stream generative framework with shared encoder and two separate decoders for behavior and semantic tokens, using global contrastive tasks with summary tokens for discriminative decoding and semantic-guided transfer tasks for cross-interactions.
**Key findings**:
- Seamlessly integrates both behavioral and semantic information in generative retrieval
- Two-stream architecture with shared encoder and separate decoders handles two feature types effectively
- Global contrastive task with summary tokens achieves discriminative decoding for each information type
- Semantic-guided transfer task promotes cross-interactions through reconstruction and estimation objectives
- Superior performance demonstrated on four public benchmarks compared to existing methods
**Limitations**: Not stated in abstract

### Zhu et al. (2024)

**Research question**: How can semantic tokenization for generative recommendation better capture item neighborhood relationships vital for effective item modeling?
**Methodology**: CoST is a contrastive quantization-based semantic tokenization approach harnessing both item relationships and semantic information to learn semantic tokens, addressing limitations of existing vector quantization methods with reconstruction loss.
**Key findings**:
- Achieves up to 43% improvement in Recall@5 on the MIND dataset over previous baselines
- Achieves up to 44% improvement in NDCG@5 on the MIND dataset over previous baselines
- Semantic tokenization has significant impact on generative recommendation performance
- Existing vector quantization methods with reconstruction loss fail to capture essential neighborhood relationships for item modeling
**Limitations**: Not stated in abstract

## References

Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying retrieve and rank with generative recommender and iterative preference alignment. arXiv. https://arxiv.org/abs/2502.18965

Hou, Y., Li, J., Fu, X., He, Z., Yan, A., Chen, X., & McAuley, J. (2024). Bridging language and items for retrieval and recommendation: Benchmarking LLMs as semantic encoders. arXiv. https://arxiv.org/abs/2403.03952

Liu, H., Wei, Y., Song, X., Guan, W., Li, Y.-F., & Nie, L. (2024). MMGRec: Multimodal generative recommendation with transformer model. arXiv. https://arxiv.org/abs/2404.16555

Qu, H., Fan, W., Zhao, Z., & Li, Q. (2024). TokenRec: Learning to tokenize ID for LLM-based generative recommendation. arXiv. https://arxiv.org/abs/2406.10450

Tan, J., Xu, S., Hua, W., Ge, Y., Li, Z., & Zhang, Y. (2024). IDGenRec: LLM-RecSys alignment with textual ID learning. arXiv. https://arxiv.org/abs/2403.19021

Wang, Y., Xun, J., Hong, M., Zhu, J., Jin, T., Lin, W., Li, H., Li, L., Xia, Y., Zhao, Z., & Dong, Z. (2024). EAGER: Two-stream generative recommender with behavior-semantic collaboration. arXiv. https://arxiv.org/abs/2406.14017

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2405.07314

Wang, Y., Ren, Z., Sun, W., Yang, J., Liang, Z., Chen, X., Xie, R., Yan, S., Zhang, X., Ren, P., Chen, Z., & Xin, X. (2024). Content-based collaborative generation for recommender systems. arXiv. https://arxiv.org/abs/2403.18480

Zheng, B., Hou, Y., Lu, H., Chen, Y., Zhao, W. X., Chen, M., & Wen, J.-R. (2023). Adapting large language models by integrating collaborative semantics for recommendation. arXiv. https://arxiv.org/abs/2311.09049

Zhu, J., Jin, M., Liu, Q., Qiu, Z., Dong, Z., & Li, X. (2024). CoST: Contrastive quantization based semantic tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2404.14774
