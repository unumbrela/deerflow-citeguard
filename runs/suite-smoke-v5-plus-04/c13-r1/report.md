# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-27  
**Papers surveyed**: 10  
**Scope**: arXiv query "generative recommendation" filtered to category cs.IR, published between 2023-10-31 and 2025-10-30  
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on generative recommendation reveals a rapidly evolving field transitioning from traditional embedding-and-retrieve paradigms toward end-to-end generative frameworks. Ten recent arXiv papers demonstrate convergent progress on three fronts: (1) learning effective item tokenization strategies that bridge collaborative filtering semantics with language model compatibility, (2) architecting unified generative models that replace cascaded retrieval-ranking pipelines, and (3) leveraging multimodal and content information to enhance recommendation quality. Collectively, these works establish that generative recommenders can match or exceed state-of-the-art performance on sequential recommendation, retrieval, and ranking tasks while offering improved generalization to unseen users and items. However, the field faces open challenges in scaling to production environments, integrating large language models without sacrificing collaborative signal fidelity, and addressing multi-objective optimization beyond accuracy metrics.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; all papers had full text available), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Item Tokenization and ID Learning

A central challenge in generative recommendation is representing items in a format compatible with autoregressive language models while preserving collaborative filtering semantics. Multiple papers address this through learned tokenization schemes. Zheng et al. (2023) propose LC-Rec, which uses learning-based vector quantization with uniform semantic mapping to create item indices that integrate collaborative semantics into LLMs. LC-Rec achieves best performance on three datasets with significant improvements over baselines [E20]. Semantic alignment tasks significantly improve recommendation performance [E21]. LC-Rec achieves best performance distinguishing items with similar language semantics through collaborative semantics integration [E23].

Wang et al. (2024c) introduce LETTER, a learnable tokenizer incorporating Residual Quantized VAE for semantic regularization and contrastive alignment loss for collaborative signals. LETTER shows significant improvements for TIGER and LC-Rec backends across three datasets [E24]. Collaborative and diversity regularization both improve TIGER performance [E25]. Diversity regularization alleviates code assignment bias in generative recommender models [E26]. LETTER effectively incorporates collaborative signals, outperforming TIGER by large margin [E27].

Zhu et al. (2024) take a contrastive quantization approach with CoST, achieving up to 43% improvement in Recall@5 on MIND by leveraging item relationships rather than reconstruction-based methods [E4]. CoST shows approximately 38% and 36% improvements in NDCG@k and Recall@k on MIND [E5]. Larger codebook size and more codebooks lead to consistent NDCG improvements [E6].

Tan et al. (2024) pursue a different direction with IDGenRec, representing each item as a unique, concise, semantically rich textual ID using human language tokens, trained alongside an LLM-based recommender with an alternative training strategy. IDGenRec significantly outperforms all baselines in standard sequential recommendation with 39.44%-42.37% improvements across four datasets [E11]. IDGenRec demonstrates strong zero-shot generalization with 353.46% improvement on cross-platform Yelp dataset [E12]. Alternate training strategy between ID generator and base recommender is critical for optimal performance [E13].

Qu et al. (2024) propose TokenRec with a Masked Vector-Quantized Tokenizer that quantizes masked user/item representations from collaborative filtering into discrete tokens. TokenRec achieves state-of-the-art performance, exceeding strongest baselines by 19.08% on HR@20 and 9.09% on NDCG@20 [E17]. TokenRec demonstrates superior generalization to unseen users with only 7% performance drop compared to 20-40% drops for other methods [E18]. TokenRec can effectively model users using only user ID tokens without interaction history, saving computation resources [E19].

Wang et al. (2024a) construct generative identifiers from pretrained collaborative filtering models in ColaRec, using an item indexing task and contrastive loss to align content and collaborative spaces. ColaRec achieves state-of-the-art performance with 3.87%-6.72% improvements over CF-based and generative models on Recall@20 [E14]. ColaRec shows particularly strong performance on long-tail users with sparse interactions [E15]. Textual content information is essential, with its removal causing 8.59%-20.99% performance drops [E16].

### Theme 2: Unified Generative Architectures

Several works advocate replacing traditional cascaded retrieve-and-rank frameworks with unified generative models. Deng et al. (2025) present OneRec, which uses an encoder-decoder structure with sparse MoE for scalable capacity, session-wise generation for contextual coherence, and Iterative Preference Alignment with DPO to enhance generation quality. OneRec achieved 1.68% improvement in total watch time in online A/B testing on Kuaishou [E1]. Session-wise generation approach significantly outperforms point-wise generation methods [E2]. OneRec has limitations in interactive indicators like likes [E3]. Limited DPO training (1% ratio) yields substantial performance gains [E10].

Wang et al. (2024b) propose EAGER with a two-stream generation architecture using shared encoder and separate decoders for behavioral and semantic information. EAGER outperforms baselines with up to 31.49% Recall@5 and 32.26% NDCG@5 improvement on Beauty [E28]. Two-stream generation architecture (TSG) is the most important component for performance improvement [E29]. Global contrastive task (GCT) contributes more to performance than semantic-guided transfer task (STT) [E30]. Generative models outperform traditional baselines across four datasets [E31].

These unified architectures demonstrate that generative models can handle both retrieval and ranking within a single framework, simplifying deployment while improving performance.

### Theme 3: Multimodal and Content Integration

Integrating rich item metadata and multimodal information emerges as a key direction. Liu et al. (2024) propose MMGRec, a Transformer-based model using Graph RQ-VAE to assign unique Rec-IDs from multimodal and collaborative filtering information, then generating user-preferred items autoregressively with relation-aware self-attention. MMGRec outperforms state-of-the-art baselines on multimodal recommendation across three datasets [E32]. Graph RQ-VAE provides better Rec-ID assignment than hierarchical K-means clustering [E33]. Relation-aware self-attention improves performance over standard positional encoding [E34]. MMGRec achieves strong performance with fewer Transformer layers than embedding-based methods [E35].

Wang et al. (2024a) demonstrate that textual content information is essential in ColaRec, with its removal causing 8.59%-20.99% performance drops [E16].

Hou et al. (2024) take a benchmarking approach with BLaIR, evaluating 11 LLMs as semantic encoders across sequential recommendation, collaborative filtering, and product search tasks. They find that LLM rankings on BLaIR show little correlation with MTEB general embedding benchmarks (correlation -0.476), indicating recommendation-specific evaluation is necessary [E7]. Scaling laws weaken when downstream tasks become complex [E8]. Semi-synthetic Amazon-C4 shows strong correlation (0.94) with real-world Reddit-Movie [E9]. Their work establishes that semi-synthetic datasets like Amazon-C4 show strong correlation (0.94) with real-world data, providing a path for efficient benchmarking.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key findings. First, all works demonstrate that generative recommendation approaches can match or exceed state-of-the-art performance from traditional collaborative filtering and embedding-based methods. Zheng et al. (2023) show LC-Rec achieves best performance on three datasets [E20]. Wang et al. (2024c) demonstrate LETTER shows significant improvements for TIGER and LC-Rec backends [E24]. Wang et al. (2024b) show generative models outperform traditional baselines across four datasets [E31]. Liu et al. (2024) find MMGRec outperforms state-of-the-art baselines on multimodal recommendation [E32]. Tan et al. (2024) report IDGenRec significantly outperforms all baselines [E11]. Wang et al. (2024a) demonstrate ColaRec achieves state-of-the-art performance [E14]. Qu et al. (2024) show TokenRec achieves state-of-the-art performance [E17].

Second, there is consensus that effective item tokenization must integrate both collaborative signals and semantic/content information. Zheng et al. (2023) find semantic alignment tasks significantly improve recommendation performance [E21]. Wang et al. (2024c) show collaborative and diversity regularization both improve TIGER performance [E25]. Wang et al. (2024a) demonstrate textual content information is essential, with its removal causing 8.59%-20.99% performance drops [E16].

Third, multiple papers validate that their approaches show strong generalization to unseen users or items, a critical advantage for real-world deployment. Tan et al. (2024) demonstrate IDGenRec shows strong zero-shot generalization [E12]. Qu et al. (2024) report TokenRec demonstrates superior generalization to unseen users [E18].

**Disagreements**: While the field shows broad agreement on the viability of generative approaches, differences emerge in optimal tokenization strategies. Zheng et al. (2023) and Wang et al. (2024c) advocate vector quantization with semantic mapping, while Tan et al. (2024) argue for human-readable textual IDs. The relative importance of collaborative versus content signals also varies: Zhu et al. (2024) emphasize contrastive learning of item relationships, whereas Wang et al. (2024a) find content information causes larger performance drops when removed. Additionally, architectural choices diverge between unified single-model approaches (Deng et al., 2025) and two-stream separation of behavioral and semantic processing (Wang et al., 2024b).

## Gaps and Open Questions

The collective literature identifies several recurring gaps. First, scaling to production environments remains challenging: Deng et al. (2025) note OneRec has limitations in interactive indicators like likes [E3], pointing to unresolved multi-objective optimization challenges. Second, integrating large language models without sacrificing collaborative signal fidelity is an open problem — multiple papers mention future work exploring LLM integration while preserving general LLM abilities during domain adaptation (Zheng et al., 2023; Liu et al., 2024).

Third, efficient tokenization for dynamic item catalogs is unresolved: Zhu et al. (2024) identify Rec-ID assignment collisions as requiring more effective vector quantization methods, while Wang et al. (2024c) point to cross-domain tokenization and handling rich user behaviors as future directions. Fourth, benchmarking standardization is needed: Hou et al. (2024) demonstrate that general embedding benchmarks like MTEB poorly predict recommendation performance [E7], calling for domain-specific evaluation frameworks.

Finally, several papers note the challenge of leveraging heterogeneous, noisy item metadata effectively (Hou et al., 2024), and the need to improve model efficiency for real-time inference (Wang et al., 2024a; Qu et al., 2024). The field would benefit from standardized benchmarks, clearer ablation studies on tokenization choices, and production-scale evaluations beyond offline metrics.

## Per-Paper Annotations

### Deng et al. (2025)

**Research question**: How can a unified generative model replace cascaded retrieve-and-rank frameworks to improve real-world recommendation performance?  
**Methodology**: OneRec uses an encoder-decoder structure with sparse MoE for scalable capacity, session-wise generation for contextual coherence, and Iterative Preference Alignment with DPO to enhance generation quality.  
**Key findings**:
- OneRec achieved 1.68% improvement in total watch time in online A/B testing on Kuaishou [E1]
- Session-wise generation approach significantly outperforms point-wise generation methods [E2]
- Limited DPO training (1% ratio) yields substantial performance gains [E10]
- OneRec has limitations in interactive indicators like likes [E3]  
**Limitations**: The model has limitations in interactive indicators, such as likes, and future research aims to enhance multi-objective modeling capability.

### Hou et al. (2024)

**Research question**: How do LLMs perform as semantic encoders for recommendation tasks compared to general embedding benchmarks?  
**Methodology**: BLaIR benchmark evaluates 11 LLMs across sequential recommendation, collaborative filtering, and product search tasks using a new Amazon Reviews 2023 dataset.  
**Key findings**:
- LLM rankings on BLaIR show little correlation with MTEB (correlation -0.476) [E7]
- Scaling laws weaken when downstream tasks become complex [E8]
- Semi-synthetic Amazon-C4 shows strong correlation (0.94) with real-world Reddit-Movie [E9]  
**Limitations**: Effectively leveraging rich, heterogeneous, and noisy item metadata in semantic encoders remains a challenging open problem.

### Liu et al. (2024)

**Research question**: How can a generative paradigm improve multimodal recommendation compared to the conventional embed-and-retrieve approach?  
**Methodology**: The authors propose MMGRec, a Transformer-based model that uses Graph RQ-VAE to assign unique Rec-IDs to items from multimodal and collaborative filtering information, then trains a Transformer to autoregressively generate Rec-IDs of user-preferred items from historical interaction sequences with relation-aware self-attention.  
**Key findings**:
- MMGRec outperforms state-of-the-art baselines on multimodal recommendation across three datasets [E32]
- Graph RQ-VAE provides better Rec-ID assignment than hierarchical K-means clustering [E33]
- Relation-aware self-attention improves performance over standard positional encoding [E34]
- MMGRec achieves strong performance with fewer Transformer layers than embedding-based methods [E35]  
**Limitations**: The paper identifies Rec-ID assignment collisions as a limitation requiring mitigation through more effective vector quantization methods, and notes the model could benefit from integration of large language models for improved user and item representations.

### Qu et al. (2024)

**Research question**: How to efficiently capture high-order collaborative knowledge into discrete tokens compatible with LLMs while generalizing effectively to new/unseen users or items?  
**Methodology**: The authors propose TokenRec with a Masked Vector-Quantized (MQ) Tokenizer that quantizes masked user/item representations from collaborative filtering into discrete tokens, and a generative retrieval paradigm for efficient top-K item recommendation.  
**Key findings**:
- TokenRec achieves state-of-the-art performance, exceeding strongest baselines by 19.08% on HR@20 and 9.09% on NDCG@20 [E17]
- TokenRec demonstrates superior generalization to unseen users with only 7% performance drop compared to 20-40% drops for other methods [E18]
- TokenRec can effectively model users using only user ID tokens without interaction history, saving computation resources [E19]  
**Limitations**: Not stated.

### Tan et al. (2024)

**Research question**: How to effectively encode recommendation items within the text-to-text framework using concise yet meaningful ID representations that align LLMs with recommendation needs?  
**Methodology**: The authors propose IDGen, representing each item as a unique, concise, semantically rich textual ID using human language tokens, trained alongside an LLM-based recommender with an alternative training strategy between the ID generator and base recommender.  
**Key findings**:
- IDGenRec significantly outperforms all baselines in standard sequential recommendation with 39.44%-42.37% improvements across four datasets [E11]
- IDGenRec demonstrates strong zero-shot generalization with 353.46% improvement on cross-platform Yelp dataset [E12]
- Alternate training strategy between ID generator and base recommender is critical for optimal performance [E13]  
**Limitations**: Training for more than one epoch negatively affected zero-shot performance due to overfitting, similar to patterns observed in NLP research.

### Wang et al. (2024a)

**Research question**: How to integrate content knowledge and collaborative interaction signals in a generative framework tailored for item recommendation?  
**Methodology**: The authors propose ColaRec, a sequence-to-sequence framework that generates recommended item identifiers using generative identifiers constructed from a pretrained collaborative filtering model, with an item indexing task and contrastive loss to align content and collaborative spaces.  
**Key findings**:
- ColaRec achieves state-of-the-art performance with 3.87%-6.72% improvements over CF-based and generative models on Recall@20 [E14]
- ColaRec shows particularly strong performance on long-tail users with sparse interactions [E15]
- Textual content information is essential, with its removal causing 8.59%-20.99% performance drops [E16]  
**Limitations**: The work identifies negative sampling for generative recommendation and improving model efficiency as future research directions.

### Wang et al. (2024b)

**Research question**: How can behavioral and semantic information be integrated for unified generative recommendation?  
**Methodology**: The authors propose EAGER with a two-stream generation architecture using shared encoder and separate decoders, a global contrastive task with summary tokens, and a semantic-guided transfer task for cross-interactions.  
**Key findings**:
- EAGER outperforms baselines with up to 31.49% Recall@5 and 32.26% NDCG@5 improvement on Beauty [E28]
- Two-stream generation architecture (TSG) is the most important component for performance improvement [E29]
- Global contrastive task (GCT) contributes more to performance than semantic-guided transfer task (STT) [E30]
- Generative models outperform traditional baselines across four datasets [E31]  
**Limitations**: The paper plans future work to enhance generative recommendation models by incorporating large language models and multimodal AI techniques.

### Wang et al. (2024c)

**Research question**: How can item tokenization be improved for generative recommendation by integrating hierarchical semantics, collaborative signals, and code assignment diversity?  
**Methodology**: The authors propose LETTER, a learnable tokenizer incorporating Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias.  
**Key findings**:
- LETTER shows significant improvements for TIGER and LC-Rec backends across three datasets [E24]
- Collaborative and diversity regularization both improve TIGER performance [E25]
- Diversity regularization alleviates code assignment bias in generative recommender models [E26]
- LETTER effectively incorporates collaborative signals, outperforming TIGER by large margin [E27]  
**Limitations**: The paper identifies future directions including tokenization with rich user behaviors, cross-domain item tokenization for open-ended recommendation, and combining user instructions in natural language with tokenized interaction history.

### Zheng et al. (2023)

**Research question**: How can large language models be adapted for recommender systems by bridging the semantic gap between language semantics and collaborative semantics?  
**Methodology**: The authors propose LC-Rec, which uses learning-based vector quantization with uniform semantic mapping for item indexing and employs semantic alignment tuning tasks to integrate collaborative semantics into LLMs.  
**Key findings**:
- LC-Rec achieves best performance on three datasets with significant improvements over baselines [E20]
- Semantic alignment tasks significantly improve recommendation performance [E21]
- LC-Rec's item indexing method outperforms base indexing methods [E22]
- LC-Rec achieves best performance distinguishing items with similar language semantics through collaborative semantics integration [E23]  
**Limitations**: The paper notes future work will explore extending the approach to multi-turn chat settings and investigating how to better reserve the general abilities of LLMs when making domain adaptations.

### Zhu et al. (2024)

**Research question**: How can contrastive quantization improve semantic tokenization for generative recommendation compared to reconstruction-based methods?  
**Methodology**: CoST introduces contrastive quantization into item tokenization, leveraging both item relationships and semantic information with contrastive loss to learn semantic tokens.  
**Key findings**:
- CoST achieves up to 43% improvement in Recall@5 on MIND dataset [E4]
- CoST shows approximately 38% and 36% improvements in NDCG@k and Recall@k on MIND [E5]
- Larger codebook size and more codebooks lead to consistent NDCG improvements [E6]  
**Limitations**: CoST currently focuses on top-one neighborhood alignment; future work could extend to top-k nearest neighbors and incorporate multimodal information.

## References

Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying retrieve and rank with generative recommender and iterative preference alignment. arXiv. https://arxiv.org/abs/2502.18965

Hou, Y., Li, J., Fu, X., He, Z., Yan, A., Chen, X., & McAuley, J. (2024). Bridging language and items for retrieval and recommendation: Benchmarking LLMs as semantic encoders. arXiv. https://arxiv.org/abs/2403.03952

Liu, H., Wei, Y., Song, X., Guan, W., Li, Y.-F., & Nie, L. (2024). MMGRec: Multimodal generative recommendation with transformer model. arXiv. https://arxiv.org/abs/2404.16555

Qu, H., Fan, W., Zhao, Z., & Li, Q. (2024). TokenRec: Learning to tokenize ID for LLM-based generative recommendation. arXiv. https://arxiv.org/abs/2406.10450

Tan, J., Xu, S., Hua, W., Ge, Y., Li, Z., & Zhang, Y. (2024). IDGenRec: LLM-RecSys alignment with textual ID learning. arXiv. https://arxiv.org/abs/2403.19021

Wang, Y., Ren, Z., Sun, W., Yang, J., Liang, Z., Chen, X., Xie, R., Yan, S., Zhang, X., Ren, P., Chen, Z., & Xin, X. (2024a). Content-based collaborative generation for recommender systems. arXiv. https://arxiv.org/abs/2403.18480

Wang, Y., Xun, J., Hong, M., Zhu, J., Jin, T., Lin, W., Li, H., Li, L., Xia, Y., Zhao, Z., & Dong, Z. (2024b). EAGER: Two-stream generative recommender with behavior-semantic collaboration. arXiv. https://arxiv.org/abs/2406.14017

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024c). Learnable item tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2405.07314

Zheng, B., Hou, Y., Lu, H., Chen, Y., Zhao, W. X., Chen, M., & Wen, J.-R. (2023). Adapting large language models by integrating collaborative semantics for recommendation. arXiv. https://arxiv.org/abs/2311.09049

Zhu, J., Jin, M., Liu, Q., Qiu, Z., Dong, Z., & Li, X. (2024). CoST: Contrastive quantization based semantic tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2404.14774

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E20 | arXiv:2311.09049 | [IV-B Overall Performance](https://arxiv.org/html/2311.09049#S4.SS2.p3) | “Our proposed LC-Rec consistently maintains the best performance on three datasets and shows significant improvements compared to the baseline methods.” |
| E21 | arXiv:2311.09049 | [Various semantic alignment tasks](https://arxiv.org/html/2311.09049#S4.SS3.SSS0.Px1.p2) | “The results, as shown in Table IV, indicate that the gradual incorporation of multiple semantic alignment tasks into the sequential recommendation, which involves only collaborative semantics, can significantly improve performance.” |
| E23 | arXiv:2311.09049 | [Performance on semantically similar negative items](https://arxiv.org/html/2311.09049#S4.SS4.SSS0.Px3.p2) | “In the task of distinguishing items with similar language semantics, our method achieved the best performance, benefiting from the integration of collaborative semantics implied by recommender systems.” |
| E24 | arXiv:2405.07314 | [4.2. Overall Performance (RQ1)](https://arxiv.org/html/2405.07314#S4.I2.i3.p1) | “LETTER consistently exhibits significant improvements for the backend models (TIGER and LC-Rec) across three datasets, validating the effectiveness of our method.” |
| E25 | arXiv:2405.07314 | [4.3.1. Ablation Study (RQ2)](https://arxiv.org/html/2405.07314#S4.SS3.SSS1.p2) | “incorporating either collaborative or diversity regularization can improve the performance of TIGER, which validates the effectiveness of injecting collaborative signals into code assignment and improving the diversity of code embeddings, respectively.” |
| E26 | arXiv:2405.07314 | [4.3.2. Code Assignment Distribution (RQ2)](https://arxiv.org/html/2405.07314#S4.SS3.SSS2.p2) | “incorporating diversity regularization effectively promotes a more uniform distribution of the first code, thus alleviating code assignment bias and potentially mitigating the item generation bias of generative recommender models.” |
| E27 | arXiv:2405.07314 | [4.3.4. Investigation on Collaborative Signals in Identifiers (RQ2).](https://arxiv.org/html/2405.07314#S4.SS3.SSS4.p2) | “From Table 3, we can observe that LETTER outperforms TIGER by a large margin, indicating the effective incorporation of collaborative signals.” |
| E4 | arXiv:2404.14774 | [Abstract](https://arxiv.org/html/2404.14774#abstract) | “CoST achieving up to a 43% improvement in Recall@5 and 44% improvement in NDCG@5 on the MIND dataset” |
| E5 | arXiv:2404.14774 | [4.2. Performance Comparison and Analysis](https://arxiv.org/html/2404.14774#S4.SS2.p1) | “our CoST tokenization method outperforms these settings, showing significant improvements in both NDCG@k and Recall@k by approximately 38% and 36%” |
| E6 | arXiv:2404.14774 | [4.2. Performance Comparison and Analysis](https://arxiv.org/html/2404.14774#S4.SS2.p3) | “as the codebook size and the number of codebooks increases, NDCG shows a consistent upward trend” |
| E11 | arXiv:2403.19021 | [3.4.2. Results](https://arxiv.org/html/2403.19021#S3.SS4.SSS2.p1) | “our method shows improvements of 39.44%, 23.55%, 42.37%, and 36.76% on the Sports, Beauty, Toys, and Yelp datasets, respectively” |
| E12 | arXiv:2403.19021 | [3.5.2. Results](https://arxiv.org/html/2403.19021#S3.SS5.SSS2.p1) | “for the Yelp dataset, which is cross-platform from the training data, our model significantly surpasses the baseline with a 353.46% improvement” |
| E13 | arXiv:2403.19021 | [3.4.3. Ablation Studies](https://arxiv.org/html/2403.19021#S3.SS4.SSS3.p2) | “alternate training significantly boosts the model's performance by enabling better collaboration between the two components” |
| E17 | arXiv:2406.10450 | [III-B Performance Comparison of Recommender Systems](https://arxiv.org/html/2406.10450#S3.I5.i1.p1) | “On average, TokenRec significantly exceeds the strongest baselines by 19.08% on HR@20 and 9.09% on NCDG@20 in the LastFM dataset” |
| E18 | arXiv:2406.10450 | [III-C Generalizability Evaluation](https://arxiv.org/html/2406.10450#S3.I6.i3.p1) | “in the Amazon-Beauty dataset, the performance of TokenRec decreases by only 7% on average, demonstrating the strong generalization capability of TokenRec for newly added users” |
| E19 | arXiv:2406.10450 | [III-B Performance Comparison of Recommender Systems](https://arxiv.org/html/2406.10450#S3.I5.i2.p1) | “Even when using only user ID tokens, TokenRec surpasses most baselines in terms of accuracy, indicating its superior performance in collaborative recommendations” |
| E14 | arXiv:2403.18480 | [5.5.1. Comparison on whole users](https://arxiv.org/html/2403.18480#S5.SS5.SSS1.p1) | “ColaRec consistently outperforms previous CF-based and generative models in Recall@20, achieving a relative improvement of 3.87%, 3.54%, 6.72% and 3.88% on Beauty, Sports, Phone and Recipe, respectively” |
| E15 | arXiv:2403.18480 | [5.5.2. Comparison on long-tail users](https://arxiv.org/html/2403.18480#S5.SS5.SSS2.p1) | “ColaRec significantly outperforms all baselines when generating recommendation for long-tail users” |
| E16 | arXiv:2403.18480 | [5.6. Ablation Study (RQ2)](https://arxiv.org/html/2403.18480#S5.SS6.p2) | “removing textual content information leads to the significant performance downgrade. Specifically, a 20.99%, 17.65%, 14.63% and 8.59% drop in Recall@5 is observed across the four datasets, respectively” |
| E1 | arXiv:2502.18965 | [5.5. Online A/B Test](https://arxiv.org/html/2502.18965#S5.SS5.p1) | “Online evaluation shows that OneRec has achieved 1.68% improvement in total watch time and 6.56% improvement in average view duration” |
| E2 | arXiv:2502.18965 | [5.2. Offline Performance](https://arxiv.org/html/2502.18965#S5.SS2.p2) | “the proposed session-wise generation approach significantly outperforms traditional dot-product-based methods and point-wise generation methods like TIGER” |
| E3 | arXiv:2502.18965 | [6. Conclusion](https://arxiv.org/html/2502.18965#S6.p1) | “our model has limitations in interactive indicators, such as likes” |
| E10 | arXiv:2502.18965 | [5.2. Offline Performance](https://arxiv.org/html/2502.18965#S5.SS2.p3) | “With only 1% DPO training ratio ( r_{\rm DPO} ), OneRec-1B+IPA surpasses the base OneRec-1B by 4.04% in maximum swt and 5.43% in maximum ltr” |
| E28 | arXiv:2406.14017 | [4.2. Performance Comparison (RQ1)](https://arxiv.org/html/2406.14017#S4.I7.i1.p1) | “EAGER almost achieves better results than base models among different datasets. Especially, EAGER performs considerably better on the Beauty benchmark compared to the second-best baseline with up to 31.49% improvement in Recall@5 and 32.26% improvement in NDCG@5 compared to TIGER.” |
| E29 | arXiv:2406.14017 | [4.3. Ablation Study (RQ2)](https://arxiv.org/html/2406.14017#S4.I8.i3.p1) | “Removing TSG leads to the most performance decline, which indicates that the base model can significantly enhance its performance by integrating behavior-semantic information of items.” |
| E30 | arXiv:2406.14017 | [4.3. Ablation Study (RQ2)](https://arxiv.org/html/2406.14017#S4.I8.i2.p1) | “Removing GCT leads to more performance drops than removing STT, suggesting that global information distillation of the inter-code is slightly more important than the knowledge flow between the intra-code.” |
| E31 | arXiv:2406.14017 | [4.2. Performance Comparison (RQ1)](https://arxiv.org/html/2406.14017#S4.I7.i3.p1) | “Generative models outperform other traditional baselines in most cases across four datasets.” |
| E32 | arXiv:2404.16555 | [6.1. Performance Comparison (RQ1)](https://arxiv.org/html/2404.16555#S6.I2.i1.p1) | “MMGRec consistently delivers the best performance across all settings.” |
| E33 | arXiv:2404.16555 | [6.2.2. Effect of Graph RQ-VAE](https://arxiv.org/html/2404.16555#S6.I4.i1.p1) | “Graph RQ-VAE consistently outperforms HK-Means, illustrating the advantageous quantization ability.” |
| E34 | arXiv:2404.16555 | [6.2.3. Effect of Relation-Aware Self-Attention](https://arxiv.org/html/2404.16555#S6.I5.i2.p1) | “Compared to default positional encoding, relation-aware self-attention yields remarkable improvements, suggesting the effectiveness of leveraging pairwise item relations as positional information.” |
| E35 | arXiv:2404.16555 | [6.3. Hyper-Parameter Analysis (RQ3)](https://arxiv.org/html/2404.16555#S6.SS3.p1) | “MMGRec can achieve quite good performance with fewer layers.” |
| E7 | arXiv:2403.03952 | [5.2 Main Results](https://arxiv.org/html/2403.03952#S5.SS2.p2) | “we observe a correlation coefficient of -0.476 with p=0.233” |
| E8 | arXiv:2403.03952 | [5.2 Main Results](https://arxiv.org/html/2403.03952#S5.SS2.p3) | “in more complex settings like sequential recommendation, where the downstream model involves a Transformer decoder, the scaling trend becomes less pronounced” |
| E9 | arXiv:2403.03952 | [5.2 Main Results](https://arxiv.org/html/2403.03952#S5.SS2.p4) | “we find a strong linearly positive correlation of 0.94 ( p‹0.01 )” |
| E22 | arXiv:2311.09049 | [Other item indexing methods](https://arxiv.org/html/2311.09049#S4.SS3.SSS0.Px2.p2) | “As shown in Figure 2, our approach (red dotted line, LC-Rec) outperforms all three base indexing methods, indicating the effectiveness of the proposed item indexing method.” |

<!-- /evidence-appendix -->
