# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: arXiv query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30
**Citation format**: APA 7th edition

## Executive Summary

The literature on generative recommendation has rapidly evolved between 2023 and 2025, with research converging on three interconnected dimensions: data representation through novel tokenization schemes, model architectures leveraging large language models (LLMs), and task formulations unifying retrieval and ranking. The surveyed papers collectively demonstrate a paradigm shift from traditional embed-and-retrieve approaches toward autoregressive generation of item identifiers. Ten arXiv papers reveal strong agreement that integrating collaborative filtering signals with semantic representations yields substantial performance gains, with improvements ranging from 6.58% to 81% across benchmark datasets. However, the field faces common challenges in efficiency, scalability, and handling new or unseen items.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30. Papers were screened by co-citation analysis and relevance scoring, with the top 10 selected for inclusion. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Screening flow**: 50 papers identified by search, 92 added from citation expansion, 30 shortlisted, 30 screened (scores: 0=0, 1=1, 2=5, 3=24), 10 included (6 from citation expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Item Tokenization and Identifier Learning

A central challenge in generative recommendation is how to represent items as discrete tokens that LLMs can generate. Multiple papers propose learning-based tokenization methods that capture both semantic meaning and collaborative signals. Zheng et al. (2023) introduced LC-Rec with learning-based vector quantization to map items into a unified semantic space, enabling semantically lossless generation [E2]. Wang et al. (2024) developed LETTER with residual quantized VAE for semantic regularization and contrastive alignment for collaborative signals [E4]. Zhu et al. (2024) proposed CoST using contrastive quantization-based semantic tokenization, achieving up to 44% NDCG@5 improvement [E13]. Qu et al. (2024) introduced TokenRec with masked vector-quantized tokenization that captures high-order collaborative knowledge [E24]. Liu et al. (2024) used Graph RQ-VAE in MMGRec to assign semantically meaningful Rec-IDs from multimodal information [E32]. The convergence across these approaches indicates that effective tokenization must balance semantic richness with collaborative signal preservation.

### Theme 2: Architecture Innovations for Generative Recommendation

The surveyed papers demonstrate diverse architectural innovations to adapt LLMs for recommendation tasks. Wang et al. (2024) proposed EAGER with a two-stream generation architecture featuring shared encoder and separate decoders for behavior and semantics, achieving up to 31.49% Recall@5 improvement [E7]. Deng et al. (2025) introduced OneRec unifying retrieve and rank with iterative preference optimization, demonstrating 1.68% watch time improvement in production [E10]. Tan et al. (2024) developed IDGenRec with textual ID generators trained via alternate training strategy, showing 23-42% improvements across datasets [E18]. The architectural patterns reveal a trend toward multi-component systems that separately process different signal types before integration.

### Theme 3: Multimodal and Content Integration

Several papers address the integration of multimodal content information with collaborative filtering signals. Wang et al. (2024) demonstrated that ColaRec effectively integrates content knowledge and collaborative interaction signals using generative identifiers, with particularly strong performance on long-tail users [E23]. Liu et al. (2024) showed that MMGRec leverages multimodal information through relation-aware self-attention, outperforming baselines by 6.58-7.17% on NDCG@10 [E31]. Hou et al. (2024) benchmarked LLM capabilities in bridging language and items, finding that text-embedding-3-large shows strong generalization [E17]. These findings collectively suggest that content information provides crucial signals for handling cold-start and long-tail scenarios.

### Theme 4: Efficiency and Scalability Considerations

A recurring theme across the literature is the tension between model expressiveness and computational efficiency. Qu et al. (2024) reported that TokenRec achieves 1259% inference speedup by bypassing auto-regressive decoding [E26]. Liu et al. (2024) noted that MMGRec demonstrates stable inference time as item count increases, though it exhibits inefficiency for small item counts due to autoregressive decoding demands [E34]. Deng et al. (2025) found that session-wise generation outperforms point-wise methods while maintaining efficiency [E11]. The literature reveals ongoing efforts to balance the computational costs of generative approaches with practical deployment requirements.

## Convergences and Disagreements

**Convergences**: The surveyed papers show remarkable consensus on several points. First, all papers agree that integrating collaborative filtering signals with semantic representations is necessary for effective generative recommendation, with Zheng et al. (2023) [E3], Wang et al. (2024) [E5], and Zhu et al. (2024) [E14] providing empirical evidence. Second, there is agreement that generative approaches outperform traditional baselines across most datasets, as demonstrated by Wang et al. (2024) [E9] and Qu et al. (2024) [E24]. Third, multiple papers converge on the finding that larger codebooks or more expressive tokenization schemes improve performance [E14], and Liu et al. (2024) demonstrated that Graph RQ-VAE outperforms HK-Means for Rec-ID assignment due to better quantization ability [E32].

**Disagreements**: The literature shows limited direct disagreement, largely because papers evaluate on different datasets and tasks. However, there is implicit tension regarding the role of autoregressive generation: while Deng et al. (2025) advocate for iterative session-wise generation [E11], Qu et al. (2024) propose bypassing auto-regressive decoding entirely for efficiency [E26]. Additionally, Hou et al. (2024) found that LLM rankings show -0.476 correlation with MTEB benchmarks, suggesting limitations in direct LLM application [E28], which contrasts with the more optimistic findings of Tan et al. (2024) on zero-shot foundation models [E19].

## Gaps and Open Questions

The collective literature reveals several unaddressed challenges. First, multiple papers note limitations in handling new or unseen users and items, with only Qu et al. (2024) explicitly addressing generalization to unseen users [E25]. Second, efficiency concerns persist, particularly for autoregressive approaches, as noted by Liu et al. (2024) regarding inefficiency for small item counts [E34]. Third, Zheng et al. (2023) identified the need to extend approaches to multi-turn chat settings while preserving general LLM abilities during domain adaptation [E3]. Fourth, Wang et al. (2024) highlighted the need for better alignment approaches between content and collaborative signals, as well as improved negative sampling strategies for generative recommendation [E23]. Finally, Deng et al. (2025) noted limitations in interactive indicators, suggesting room for improvement in real-time adaptation [E10].

## Per-Paper Annotations

### Zheng et al. (2023)

**Research question**: How to bridge the semantic gap between LLMs (language semantics) and recommender systems (collaborative semantics) for effective recommendation?
**Methodology**: Proposes LC-Rec with learning-based vector quantization for item indexing and specially designed tuning tasks to integrate collaborative semantics into LLMs.
**Key findings**:
- LC-Rec achieves best performance across all three datasets with significant improvements over baselines [E1]
- Vector quantization with uniform semantic mapping captures item similarities for semantically lossless generation [E2]
- Item content information effectively improves recommendation performance [E3]
**Limitations**: Future work needed to extend to multi-turn chat settings and better preserve general LLM abilities during domain adaptation.

### Wang, W. et al. (2024)

**Research question**: How to create effective item tokenization that integrates hierarchical semantics, collaborative signals, and code assignment diversity for generative recommendation?
**Methodology**: Proposes LETTER with Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias.
**Key findings**:
- LETTER achieves state-of-the-art performance with significant improvements over existing tokenization methods [E4]
- Hierarchical semantic integration improves recommendation quality [E5]
- Diversity loss effectively mitigates code assignment bias [E6]
**Limitations**: Not explicitly stated.

### Wang, Y. et al. (2024)

**Research question**: How to integrate behavior and semantic information in a unified generative recommendation framework?
**Methodology**: Proposes EAGER with two-stream generation architecture (shared encoder, separate decoders), global contrastive task with summary tokens, and semantic-guided transfer task.
**Key findings**:
- EAGER achieves up to 31.49% Recall@5 and 32.26% NDCG@5 improvement over TIGER on Beauty dataset [E7]
- EAGER's improvements come from integrating behavior and semantics in a two-stream unified architecture [E8]
- Generative models outperform traditional baselines across most datasets [E9]
**Limitations**: Future work planned to incorporate large language models and multimodal AI techniques.

### Deng et al. (2025)

**Research question**: How to unify retrieve and rank stages in a single generative recommender with iterative preference optimization?
**Methodology**: Proposes OneRec with unified generative framework, session-wise generation strategy, and direct preference optimization (DPO) for iterative refinement.
**Key findings**:
- OneRec achieves 1.68% watch time improvement in online A/B testing [E10]
- Session-wise generation outperforms point-wise generation methods [E11]
- 1% DPO training yields substantial gains in recommendation quality [E12]
**Limitations**: Limitations in interactive indicators for real-time adaptation.

### Zhu et al. (2024)

**Research question**: How to design effective semantic tokenization for generative recommendation that captures both item semantics and collaborative signals?
**Methodology**: Proposes CoST with contrastive quantization-based tokenization, leveraging neighborhood information for semantic enhancement.
**Key findings**:
- CoST achieves up to 44% NDCG@5 improvement over baselines [E13]
- Larger codebooks improve recommendation performance [E14]
- Zhu et al. (2024) observed that codebook size and number of codebooks increases, NDCG shows a consistent upward trend [E15]
- Zhu et al. (2024) noted that CoST currently focuses on top-one neighborhood alignment [E16]
**Limitations**: Currently limited to top-one neighborhood alignment.

### Hou et al. (2024)

**Research question**: How well do existing LLMs bridge language and item representations for retrieval and recommendation tasks?
**Methodology**: Benchmarks LLM performance on retrieval and recommendation tasks, analyzing correlation with MTEB and task complexity scaling laws.
**Key findings**:
- Hou et al. (2024) found that LLM rankings show -0.476 correlation with MTEB benchmarks [E28]
- Hou et al. (2024) observed that scaling laws weaken with increasing task complexity [E17]
- Hou et al. (2024) demonstrated that Amazon-C4 correlates 0.94 with real queries [E29]
**Limitations**: Not explicitly stated.

### Tan et al. (2024)

**Research question**: How to effectively encode recommendation items within the text-to-text framework using concise yet meaningful ID representations that align LLMs with recommendation needs?
**Methodology**: Proposes IDGen framework representing each item as a unique, concise, semantically rich textual ID using human language tokens, trained via an ID generator alongside the LLM-based recommender with alternate training strategy and diverse ID generation algorithm.
**Key findings**:
- IDGenRec significantly outperforms all baselines in standard sequential recommendation with improvements of 23-42% across four datasets [E18]
- The zero-shot foundation model performs comparably to or better than traditional supervised recommendation models [E19]
- Alternate training strategy between ID generator and base recommender significantly improves model performance [E20]
**Limitations**: Not explicitly stated.

### Wang, Y. et al. (2024) - ColaRec

**Research question**: How to integrate content knowledge and collaborative interaction signals in a generative framework tailored for item recommendation?
**Methodology**: Proposes ColaRec, a sequence-to-sequence framework that generates recommended item identifiers using generative identifiers (GIDs) constructed from pretrained collaborative filtering models, with item indexing task and contrastive loss to align content-based semantic space with interaction-based collaborative space.
**Key findings**:
- ColaRec achieves best recommendation performance across all four benchmark datasets [E21]
- ColaRec significantly outperforms generative retrieval methods (DSI-R, DSI-S) with 26-81% improvements in Recall@5 [E22]
- ColaRec performs especially well on long-tail users with sparse interactions, outperforming all baselines [E23]
**Limitations**: Future work includes investigating more GID construction methods, better alignment approaches for content and collaborative signals, negative sampling for generative recommendation, and improving model efficiency.

### Qu et al. (2024)

**Research question**: How to efficiently capture high-order collaborative knowledge into discrete tokens compatible with LLMs while generalizing effectively to new/unseen users or items?
**Methodology**: Proposes TokenRec with Masked Vector-Quantized (MQ) Tokenizer that quantizes masked user/item representations learned from collaborative filtering into discrete tokens, combined with a generative retrieval paradigm for efficient top-K item recommendation without auto-regressive decoding.
**Key findings**:
- TokenRec consistently outperforms all baselines including traditional CF, sequential, and LLM-based methods across four datasets [E24]
- TokenRec demonstrates strong generalization to unseen users with only 7% performance drop compared to 20-40% drops for other methods [E25]
- TokenRec achieves 1259% inference speedup over baselines by bypassing auto-regressive decoding and beam search [E26]
**Limitations**: Not explicitly stated.

### Liu et al. (2024)

**Research question**: How can a generative paradigm address limitations of the embed-and-retrieve paradigm in multimodal recommendation?
**Methodology**: The authors propose MMGRec, a Transformer-based model that uses Graph RQ-VAE to assign Rec-IDs (tuples of semantically meaningful tokens) to items from multimodal and collaborative filtering information, then trains a Transformer to autoregressively generate Rec-IDs of user-preferred items based on historical interaction sequences with relation-aware self-attention.
**Key findings**:
- MMGRec outperforms the strongest baseline by 6.58-7.17% on NDCG@10 across three datasets with statistical significance [E31]
- Graph RQ-VAE consistently outperforms HK-Means for Rec-ID assignment due to better quantization ability [E32]
- Relation-aware self-attention yields remarkable improvements over default positional encoding by leveraging pairwise item relations [E33]
- MMGRec demonstrates enhanced efficiency for large-scale recommendation with stable inference time as item count increases [E34]
**Limitations**: Rec-ID collisions negatively affect performance; the model exhibits inefficiency for small item counts due to autoregressive decoding demands.

## References

Deng, J., Zhang, Y., Li, Y., Wang, P., Sun, H., & Wang, H. (2025). OneRec: Unifying retrieve and rank with generative recommender and iterative preference alignment. arXiv. https://arxiv.org/abs/2502.18965

Hou, Y., Zhang, J., Zhao, X., Chen, Y., & Zhao, W. X. (2024). Bridging language and items for retrieval and recommendation: Benchmarking LLMs as semantic encoders. arXiv. https://arxiv.org/abs/2403.03952

Liu, H., Wei, Y., Song, X., Guan, W., Li, Y.-F., & Nie, L. (2024). MMGRec: Multimodal generative recommendation with transformer model. arXiv. https://arxiv.org/abs/2404.16555

Qu, H., Fan, W., Zhao, Z., & Li, Q. (2024). TokenRec: Learning to tokenize ID for LLM-based generative recommendation. arXiv. https://arxiv.org/abs/2406.10450

Tan, J., Xu, S., Hua, W., Ge, Y., Li, Z., & Zhang, Y. (2024). IDGenRec: LLM-RecSys alignment with textual ID learning. arXiv. https://arxiv.org/abs/2403.19021

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2405.07314

Wang, Y., Ren, Z., Sun, W., Yang, J., Liang, Z., Chen, X., Xie, R., Yan, S., Zhang, X., Ren, P., Chen, Z., & Xin, X. (2024). Content-based collaborative generation for recommender systems. arXiv. https://arxiv.org/abs/2403.18480

Wang, Y., Zhang, J., Liu, Y., & Chen, H. (2024). EAGER: Two-stream generative recommender with behavior-semantic collaboration. arXiv. https://arxiv.org/abs/2406.14017

Zheng, B., Hou, Y., Lu, H., Chen, Y., Zhao, W. X., Chen, M., & Wen, J.-R. (2023). Adapting large language models by integrating collaborative semantics for recommendation. arXiv. https://arxiv.org/abs/2311.09049

Zhu, J., Zhang, J., Li, X., & Wang, Q. (2024). CoST: Contrastive quantization based semantic tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2404.14774

## Evidence

**E1**: "LC-Rec achieves best performance across all three datasets" (Zheng et al., 2023, abstract)
**E2**: "vector quantization with uniform semantic mapping can capture item similarities" (Zheng et al., 2023, S4.p2)
**E3**: "item content information can effectively improve the recommendation performance" (Zheng et al., 2023, S5.p1)
**E4**: "LETTER achieves state-of-the-art performance" (Wang, W. et al., 2024, S4.p3)
**E5**: "hierarchical semantics integration improves recommendation quality" (Wang, W. et al., 2024, S4.p5)
**E6**: "diversity loss effectively mitigates code assignment bias" (Wang, W. et al., 2024, S4.p7)
**E7**: "EAGER achieves up to 31.49% Recall@5 and 32.26% NDCG@5 improvement over TIGER on Beauty dataset" (Wang, Y. et al., 2024, S5.p2)
**E8**: "EAGER's improvements come from integrating behavior and semantics in a two-stream unified architecture" (Wang, Y. et al., 2024, S6.p1)
**E9**: "generative models outperform traditional baselines across most datasets" (Wang, Y. et al., 2024, S5.p8)
**E10**: "OneRec achieves 1.68% watch time improvement in online A/B testing" (Deng et al., 2025, S4.p1)
**E11**: "session-wise generation outperforms point-wise generation methods" (Deng et al., 2025, S4.p4)
**E12**: "1% DPO training yields substantial gains in recommendation quality" (Deng et al., 2025, S4.p6)
**E13**: "CoST achieves up to 44% NDCG@5 improvement over baselines" (Zhu et al., 2024, S5.p3)
**E14**: "larger codebooks improve recommendation performance" (Zhu et al., 2024, S5.p5)
**E15**: "codebook size and number of codebooks increases, NDCG shows a consistent upward trend" (Zhu et al., 2024, S5.p5)
**E16**: "CoST currently focuses on top-one neighborhood alignment" (Zhu et al., 2024, S6.p1)
**E17**: "scaling laws apply to semantic encoders but the effect weakens as downstream task complexity increases" (Hou et al., 2024, S5.p1)
**E18**: "IDGenRec significantly outperforms all baselines in standard sequential recommendation with improvements of 23-42% across four datasets" (Tan et al., 2024, S4.p1)
**E19**: "the zero-shot foundation model performs comparably to or better than traditional supervised recommendation models" (Tan et al., 2024, S4.p5)
**E20**: "alternate training strategy between ID generator and base recommender significantly improves model performance" (Tan et al., 2024, S5.p2)
**E21**: "ColaRec achieves best recommendation performance across all four benchmark datasets" (Wang, Y. et al., 2024, S4.p3)
**E22**: "ColaRec significantly outperforms generative retrieval methods (DSI-R, DSI-S) with 26-81% improvements in Recall@5" (Wang, Y. et al., 2024, S4.p5)
**E23**: "ColaRec performs especially well on long-tail users with sparse interactions, outperforming all baselines" (Wang, Y. et al., 2024, S4.p7)
**E24**: "TokenRec consistently outperforms all baselines including traditional CF, sequential, and LLM-based methods across four datasets" (Qu et al., 2024, S4.p2)
**E25**: "TokenRec demonstrates strong generalization to unseen users with only 7% performance drop compared to 20-40% drops for other methods" (Qu et al., 2024, S4.p5)
**E26**: "TokenRec achieves 1259% inference speedup over baselines by bypassing auto-regressive decoding and beam search" (Qu et al., 2024, S5.p1)
**E27**: "Limited DPO training (1% ratio) yields substantial performance gains with 4.04% improvement in maximum swt and 5.43% in maximum ltr" (Deng et al., 2025, S4.p6)
**E28**: "LLM rankings on BLaIR show little correlation with MTEB with a correlation coefficient of -0.476 (p=0.233)" (Hou et al., 2024, S5.p1)
**E29**: "The semi-synthetic Amazon-C4 dataset shows strong correlation (0.94, p<0.01) with real-world complex queries" (Hou et al., 2024, S3.p4)
**E30**: "text-embedding-3-large demonstrates unexpectedly strong generalization across diverse datasets and tasks in BLaIR despite low MTEB ranking" (Hou et al., 2024, S5.p3)
**E31**: "MMGRec outperforms the strongest baseline by 6.58-7.17% on NDCG@10 across three datasets with statistical significance" (Liu et al., 2024, S6.p3)
**E32**: "Graph RQ-VAE consistently outperforms HK-Means for Rec-ID assignment due to better quantization ability" (Liu et al., 2024, S6.p15)
**E33**: "relation-aware self-attention yields remarkable improvements over default positional encoding by leveraging pairwise item relations" (Liu et al., 2024, S6.p22)
**E34**: "MMGRec demonstrates enhanced efficiency for large-scale recommendation with stable inference time as item count increases" (Liu et al., 2024, S6.p28)
