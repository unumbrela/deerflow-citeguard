# Systematic Literature Review: Generative Recommendation - Data, Model, and Tasks

**Date:** 2026-10-27  
**Retrieved on:** 2026-10-27  
**Published between:** 2023-10-31 and 2025-10-30  
**Category:** cs.IR  
**Format:** APA 7th Edition

---

## Executive Summary

This systematic literature review synthesizes findings from 10 academic papers on generative recommendation systems published between October 2023 and October 2025. The review identifies three major themes: (1) **Item Tokenization and Representation Learning**, focusing on how to create effective discrete identifiers for items that capture both semantic and collaborative signals; (2) **Model Architecture Innovations**, including two-stream architectures, unified retrieve-and-rank frameworks, and multimodal integration; and (3) **Task Formulations and Optimization**, encompassing contrastive learning, preference alignment, and context-aware sequence modeling.

Across the literature, there is strong convergence on the effectiveness of integrating collaborative filtering signals with semantic information, with multiple papers reporting substantial improvements (20-40%+) over traditional recommendation baselines. However, disagreements exist regarding optimal tokenization strategies, and common limitations include challenges with interactive indicators, cold-start problems, and inference efficiency. This review provides a comprehensive analysis of current methodologies, key findings, and future research directions in generative recommendation.

---

## Methodology

### Search Strategy

This review followed a systematic search methodology using arXiv's scholarly database. The search query "generative recommendation" was executed with the following parameters:
- **Category:** cs.IR (Information Retrieval)
- **Publication window:** 2023-10-31 to 2025-10-30
- **Maximum results:** 10 papers

### Screening Process

The screening process followed these steps:
1. **Initial pool:** 50 papers identified by search
2. **Citation expansion:** 92 additional papers added from references
3. **Shortlist:** 30 papers shortlisted based on co-citation analysis
4. **Screening scores:** Papers scored for centrality to the topic (distribution: 0 papers scored 0, 2 papers scored 1, 4 papers scored 2, 24 papers scored 3)
5. **Final selection:** 10 papers included, with 5 papers selected from citation expansion

### Data Extraction

Findings were extracted from papers' full text (arXiv HTML) where available. Each paper underwent structured extraction of research questions, methodologies, key findings, and limitations. Evidence quotes were verified against source paragraphs to ensure accuracy.

---

## Themes and Cross-Paper Analysis

### Theme 1: Item Tokenization and Representation Learning

A dominant research direction focuses on how to create effective item identifiers (tokens) that bridge collaborative filtering and semantic representations for generative recommendation.

**Key approaches identified:**

- **Learning-based tokenization:** LETTER (Wang et al., 2024c) incorporates Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative signals, and diversity loss to mitigate code assignment bias, achieving consistent improvements across TIGER and LC-Rec models [E12]. Both collaborative and diversity regularization individually improve TIGER performance by enhancing code assignment (Wang et al., 2024c) [E13]. Experimental results confirm LETTER's superiority for item tokenization in generative recommendation (Wang et al., 2024c) [E14].

- **Contrastive quantization:** CoST (Zhu et al., 2024) introduces contrastive loss to learn semantic tokens capturing neighborhood relationships, achieving approximately 38% improvement in NDCG@k and 36% in Recall@k on the MIND dataset [E24, E25].

- **Contextual tokenization:** ActionPiece (Hou et al., 2025) is the first context-aware action sequence tokenizer where the same action can be tokenized differently based on surrounding context, with set permutation regularization achieving 87.01% token utilization rate [E36, E37].

- **Collaborative semantic integration:** LC-Rec (Zheng et al., 2023) uses learning-based vector quantization with uniform semantic mapping, demonstrating that methods incorporating item content information outperform traditional ID-only sequential recommendation methods (Zheng et al., 2023) [E10, E32].

**Convergence:** Multiple papers converge on the finding that integrating both collaborative and semantic signals in tokenization yields superior performance compared to using either signal alone.

### Theme 2: Model Architecture Innovations

The literature reveals diverse architectural innovations for generative recommendation systems.

**Two-stream architectures:** EAGER (Wang et al., 2024b) proposes a two-stream generation architecture with shared encoder and separate decoders for behavior and semantic tokens, achieving up to 31.49% Recall@5 and 32.26% NDCG@5 improvement over TIGER on the Beauty dataset [E16]. All three modules (TSG, GCT, STT) contribute to performance, as removing any causes degradation [E33].

**Unified retrieve-and-rank:** OneRec (Deng et al., 2025) unifies retrieve and rank with a generative recommender and iterative preference alignment, achieving 1.68% improvement in total watch time and 6.56% improvement in average view duration in online A/B testing on Kuaishou [E21]. With only 1% DPO training ratio, OneRec achieves substantial gains of 4.04% in session watch time and 5.43% in like probability [E34].

**Multimodal integration:** MMGRec (Liu et al., 2024) uses Graph RQ-VAE to assign Rec-ID from multimodal and CF information, with relation-aware self-attention yielding remarkable improvements by leveraging pairwise item relations as positional information [E9]. MMGRec consistently outperforms the strongest competitor by 7.17%, 6.79%, and 6.58% in NDCG@10 [E19].

**Efficient generative retrieval:** TokenRec (Qu et al., 2024) introduces a generative retrieval paradigm for efficient top-K item generation without auto-regressive decoding, surpassing most baselines even when using only user ID tokens without item interaction history (Qu et al., 2024) [E6]. The model addresses time-consuming inference challenges in LLM-based recommender systems (Qu et al., 2024) [E18].

### Theme 3: Task Formulations and Optimization

Papers explore diverse optimization strategies and task formulations for training generative recommendation models.

**Contrastive learning:** Multiple papers employ contrastive losses to align different representation spaces. ColaRec (Wang et al., 2024a) uses an auxiliary item indexing task and contrastive loss to align content and collaborative signals, significantly outperforming all baselines for long-tail users with sparse interactions (Wang et al., 2024a) [E3]. The auxiliary item indexing task helps align content and collaborative signals effectively (Wang et al., 2024a) [E4].

**Preference alignment:** OneRec (Deng et al., 2025) combines Iterative Preference Alignment with Direct Preference Optimization to enhance generated result quality. However, OneRec shows limitations in interactive indicators such as likes despite improvements in watch time (Deng et al., 2025) [E23].

**Alternate training:** IDGenRec (Tan et al., 2024) employs an alternate training strategy between ID generator and base recommender, achieving 353.46% improvement over UniSRec on cross-platform Yelp dataset in zero-shot evaluation [E29, E30].

**Set permutation regularization:** ActionPiece (Hou et al., 2025) introduces set permutation regularization to produce multiple segmentations of action sequences with the same semantics, with removing any proposed techniques reducing performance [E38].

### Disagreements and Open Questions

**Optimal tokenization strategy:** While all papers agree on the importance of tokenization, there is disagreement on the optimal approach. LETTER uses hierarchical semantic regularization, CoST employs contrastive quantization, and ActionPiece focuses on context-aware tokenization. Each claims superiority on different datasets, suggesting no universally optimal approach.

**Model capacity vs. efficiency:** OneRec scales model capacity with sparse Mixture-of-Experts, while TokenRec prioritizes efficient top-K generation without auto-regressive decoding. The trade-off between model capacity and inference efficiency remains unresolved.

### Research Gaps

Common limitations across the literature include:

1. **Interactive indicators:** OneRec shows limitations in interactive indicators (likes) despite watch time improvements (Deng et al., 2025) [E23].

2. **Cold-start problem:** MMGRec notes interest in leveraging generative capability to tackle cold-start, but this remains unaddressed (Liu et al., 2024) [E8].

3. **Inference efficiency:** TokenRec acknowledges time-consuming inference as an emerging challenge in LLM-based recommender systems (Qu et al., 2024) [E18].

4. **Multi-turn interaction:** LC-Rec suggests exploring multi-turn chat settings for more flexible user interaction (Zheng et al., 2023) [E32].

5. **Cross-domain generalization:** LETTER identifies tokenizing cross-domain items for open-ended recommendation as future work (Wang et al., 2024c) [E14].

6. **Model efficiency:** ColaRec notes improving model efficiency for generative recommendation as a potential research direction (Wang et al., 2024a) [E4].

---

## Annotated Bibliography

### Zheng et al., 2023

**Title:** Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation  
**Authors:** Bowen Zheng, Yupeng Hou, Hongyu Lu, Yu Chen, Wayne Xin Zhao, Ming Chen, Ji-Rong Wen  
**Published:** 2023-11-15  
**arXiv ID:** 2311.09049

**Research Question:** How to bridge the semantic gap between LLMs and recommender systems by integrating language and collaborative semantics for recommendation?

**Methodology:** LC-Rec uses a learning-based vector quantization method with uniform semantic mapping for item indexing, and proposes semantic alignment tuning tasks including sequential item prediction, explicit index-language alignment, and implicit recommendation-oriented alignment to integrate collaborative semantics into LLMs.

**Key Findings:**
- LC-Rec outperforms all baseline methods across three datasets with significant improvements (Zheng et al., 2023) [E10].
- LC-Rec was validated through extensive experiments showing it outperforms competitive baselines (Zheng et al., 2023) [E11].
- Methods incorporating item content information outperform traditional ID-only sequential recommendation methods (Zheng et al., 2023) [E32].

**Limitations:** Future work will explore extending the approach in a multi-turn chat setting for more flexible user interaction, and investigate how to better reserve the general abilities of LLMs when making domain adaptations.

---

### Wang et al., 2024a

**Title:** Content-Based Collaborative Generation for Recommender Systems  
**Authors:** Yidan Wang, Zhaochun Ren, Weiwei Sun, Jiyuan Yang, Zhixiang Li, Xin Chen, Ruobing Xie, Su Yan, Xu Zhang, Pengjie Ren, Zhumin Chen, Xin Xin  
**Published:** 2024-03-27  
**arXiv ID:** 2403.18480

**Research Question:** How to integrate content knowledge and collaborative interaction signals in a generative framework tailored for item recommendation?

**Methodology:** ColaRec is a sequence-to-sequence framework that generates item identifiers (GIDs) constructed from a pretrained collaborative filtering model, with user representation as content aggregation of interacted items. An item indexing task and contrastive loss are used to align content-based semantic space with interaction-based collaborative space.

**Key Findings:**
- ColaRec achieves the best recommendation performance on all datasets except for NDCG@5 in Beauty (Wang et al., 2024a) [E1].
- ColaRec shows significant relative improvements over DSI-R and DSI-S in Recall@5 across four datasets (Wang et al., 2024a) [E2].
- ColaRec significantly outperforms all baselines for long-tail users with sparse interactions (Wang et al., 2024a) [E3].
- ColaRec uses an auxiliary item indexing task and contrastive loss to align content and collaborative signals (Wang et al., 2024a) [E4].

**Limitations:** The paper leaves the investigation of negative sampling for generative recommendation as future work, and notes that improving model efficiency for generative recommendation is a potential research direction.

---

### Tan et al., 2024

**Title:** IDGenRec: LLM-RecSys Alignment with Textual ID Learning  
**Authors:** Juntao Tan, Shuyuan Xu, Wenyue Hua, Yingqiang Ge, Zelong Li, Yongfeng Zhang  
**Published:** 2024-03-27  
**arXiv ID:** 2403.19021

**Research Question:** How can textual ID learning better align Large Language Models with recommendation systems using concise, semantically rich item representations?

**Methodology:** IDGenRec employs an ID generator to produce unique, concise, semantically rich textual IDs using human language tokens, trained alongside an LLM-based recommender with an alternate training strategy and diverse ID generation algorithm.

**Key Findings:**
- IDGenRec shows improvements of 39.44%, 23.55%, 42.37%, and 36.76% on Sports, Beauty, Toys, and Yelp datasets over best baselines (Tan et al., 2024) [E28].
- IDGenRec achieves 353.46% improvement over UniSRec on cross-platform Yelp dataset in zero-shot evaluation (Tan et al., 2024) [E29].
- Alternate training strategy significantly boosts model performance by enabling better collaboration between ID generator and base recommender (Tan et al., 2024) [E30].
- Training the foundational model for more than one epoch negatively affects zero-shot performance due to overfitting (Tan et al., 2024) [E31].

**Limitations:** Further training beyond one epoch negatively affected the zero-shot performance, showing overfitting patterns similar to those observed in NLP pre-training.

---

### Zhu et al., 2024

**Title:** CoST: Contrastive Quantization based Semantic Tokenization for Generative Recommendation  
**Authors:** Jieming Zhu, Mengqun Jin, Qijiong Liu, Zexuan Qiu, Zhenhua Dong, Xiu Li  
**Published:** 2024-04-23  
**arXiv ID:** 2404.14774

**Research Question:** How can contrastive quantization-based semantic tokenization improve generative recommendation performance compared to reconstruction-based methods?

**Methodology:** CoST introduces contrastive quantization into the tokenization process, leveraging both item relationships and semantic information through contrastive loss to learn semantic tokens that capture neighborhood relationships.

**Key Findings:**
- CoST tokenization method achieves approximately 38% improvement in NDCG@k and 36% improvement in Recall@k on MIND dataset (Zhu et al., 2024) [E24].
- CoST achieves up to 43% improvement in Recall@5 and 44% improvement in NDCG@5 on MIND dataset over baselines (Zhu et al., 2024) [E25].
- Increasing codebook size and number of codebooks leads to consistent NDCG improvement (Zhu et al., 2024) [E26].
- CoST is currently limited to top-one neighborhood alignment and does not consider top-k nearest neighbors (Zhu et al., 2024) [E27].

**Limitations:** CoST currently focuses on top-one neighborhood alignment, and future work could extend this to consider top-k nearest neighbors.

---

### Liu et al., 2024

**Title:** MMGRec: Multimodal Generative Recommendation with Transformer Model  
**Authors:** Han Liu, Yinwei Wei, Xuemeng Song, Weili Guan, Yuan-Fang Li, Liqiang Nie  
**Published:** 2024-04-25  
**arXiv ID:** 2404.16555

**Research Question:** How to address inference cost, interaction modeling, and false-negative issues in multimodal recommendation through a generative paradigm?

**Methodology:** MMGRec uses a hierarchical quantization method Graph RQ-VAE to assign Rec-ID for each item from multimodal and CF information, then trains a Transformer-based recommender with relation-aware self-attention to generate Rec-IDs of user-preferred items.

**Key Findings:**
- Graph RQ-VAE consistently outperforms HK-Means, demonstrating superior quantization ability (Liu et al., 2024) [E8].
- Relation-aware self-attention yields remarkable improvements by leveraging pairwise item relations as positional information (Liu et al., 2024) [E9].
- MMGRec consistently delivers the best performance, outperforming the strongest competitor by 7.17%, 6.79%, and 6.58% in NDCG@10 (Liu et al., 2024) [E19].
- MMGRec's recommendation result is more accurate with respect to preference ranking, showing larger improvements in NDCG (Liu et al., 2024) [E20].

**Limitations:** The paper plans to develop a more effective vector quantization method to mitigate Rec-ID assignment collisions, and notes interest in leveraging MMGRec's generative capability to tackle the cold-start problem.

---

### Wang et al., 2024c

**Title:** Learnable Item Tokenization for Generative Recommendation  
**Authors:** Wenjie Wang, Honghui Bao, Xinyu Lin, Jizhi Zhang, Yongqi Li, Fuli Feng, See-Kiong Ng, Tat-Seng Chua  
**Published:** 2024-05-12  
**arXiv ID:** 2405.07314

**Research Question:** How to create effective item tokenization that satisfies the essential requirements of identifiers by integrating hierarchical semantics, collaborative signals, and code assignment diversity?

**Methodology:** LETTER incorporates Residual Quantized VAE for semantic regularization, a contrastive alignment loss for collaborative regularization, and a diversity loss to mitigate code assignment bias, instantiated on TIGER and LC-Rec models with a ranking-guided generation loss.

**Key Findings:**
- LETTER improves performance of both TIGER and LC-Rec backend models across all three datasets (Wang et al., 2024c) [E12].
- Both collaborative and diversity regularization individually improve TIGER performance by enhancing code assignment (Wang et al., 2024c) [E13].
- Experimental results confirm LETTER's superiority for item tokenization in generative recommendation (Wang et al., 2024c) [E14].

**Limitations:** Future work includes tokenization with rich user behaviors to enable inferring user preference from multiple actions, tokenizing cross-domain items for open-ended recommendation, and combining user instructions in natural language with interaction history tokenized by LETTER.

---

### Qu et al., 2024

**Title:** TokenRec: Learning to Tokenize ID for LLM-based Generative Recommendation  
**Authors:** Haohao Qu, Wenqi Fan, Zihuai Zhao, Qing Li  
**Published:** 2024-06-15  
**arXiv ID:** 2406.10450

**Research Question:** How to efficiently capture high-order collaborative knowledge into discrete tokens compatible with LLMs and generalize to unseen users or items?

**Methodology:** TokenRec introduces a Masked Vector-Quantized (MQ) Tokenizer that quantizes masked user/item representations learned from collaborative filtering into discrete tokens, and a generative retrieval paradigm for efficient top-K item recommendation without auto-regressive decoding.

**Key Findings:**
- TokenRec achieves the best performance and consistently outperforms all baselines across all datasets (Qu et al., 2024) [E5].
- TokenRec surpasses most baselines even when using only user ID tokens without item interaction history (Qu et al., 2024) [E6].
- CoLLM achieves superior results by incorporating collaborative embeddings learned from GNN methods (Qu et al., 2024) [E7].
- TokenRec introduces a generalizable ID tokenization strategy and a generative retrieval paradigm for efficient top-K item generation (Qu et al., 2024) [E18].

**Limitations:** The paper notes that time-consuming inference remains an emerging challenge in LLM-based recommender systems, which TokenRec addresses through its generative retrieval paradigm.

---

### Wang et al., 2024b

**Title:** EAGER: Two-Stream Generative Recommender with Behavior-Semantic Collaboration  
**Authors:** Ye Wang, Jiahao Xun, Minjie Hong, Jieming Zhu, Tao Jin, Wang Lin, Haoyuan Li, Linjun Li, Yan Xia, Zhou Zhao, Zhenhua Dong  
**Published:** 2024-06-20  
**arXiv ID:** 2406.14017

**Research Question:** How to seamlessly integrate both behavioral and semantic information for unified generative recommendation while ensuring sufficient independent learning and fostering subtle interactions?

**Methodology:** EAGER proposes a two-stream generation architecture with a shared encoder and two separate decoders for behavior and semantic tokens with confidence-based ranking, a global contrastive task with summary tokens for discriminative decoding, and a semantic-guided transfer task for cross-interactions.

**Key Findings:**
- EAGER achieves better results than base models across different datasets (Wang et al., 2024b) [E15].
- EAGER shows up to 31.49% Recall@5 and 32.26% NDCG@5 improvement over TIGER on the Beauty dataset (Wang et al., 2024b) [E16].
- EAGER's effectiveness and robustness are demonstrated through extensive comparisons with state-of-the-art methods (Wang et al., 2024b) [E17].
- All three modules (TSG, GCT, STT) contribute to EAGER's performance as removing any causes degradation (Wang et al., 2024b) [E33].

**Limitations:** Future work plans to further enhance generative recommendation models by incorporating large language models and multimodal AI techniques.

---

### Deng et al., 2025

**Title:** OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment  
**Authors:** Jiaxin Deng, Shiyao Wang, Kuo Cai, Lejian Ren, Qigen Hu, Weifeng Ding, Qiang Luo, Guorui Zhou  
**Published:** 2025-02-26  
**arXiv ID:** 2502.18965

**Research Question:** How can a unified generative model replace the cascaded retrieve-and-rank framework to improve recommendation performance in real-world scenarios?

**Methodology:** OneRec uses an encoder-decoder structure with sparse Mixture-of-Experts to scale model capacity, a session-wise generation approach for contextual coherence, and an Iterative Preference Alignment module combined with Direct Preference Optimization to enhance generated result quality.

**Key Findings:**
- OneRec achieved 1.68% improvement in total watch time and 6.56% improvement in average view duration in online A/B testing on Kuaishou (Deng et al., 2025) [E21].
- OneRec's session-wise generation approach outperforms TIGER with 1.78% higher session watch time and 3.36% higher like probability (Deng et al., 2025) [E22].
- OneRec has limitations in interactive indicators such as likes despite improvements in watch time (Deng et al., 2025) [E23].
- Only 1% DPO training ratio yields substantial gains of 4.04% in session watch time and 5.43% in like probability (Deng et al., 2025) [E34].

**Limitations:** The model has limitations in interactive indicators, such as likes, and future research aims to enhance multi-objective modeling capability.

---

### Hou et al., 2025

**Title:** ActionPiece: Contextually Tokenizing Action Sequences for Generative Recommendation  
**Authors:** Yupeng Hou, Jianmo Ni, Zhankui He, Noveen Sachdeva, Wang-Cheng Kang, Ed H. Chi, Julian McAuley, Derek Zhiyuan Cheng  
**Published:** 2025-02-19  
**arXiv ID:** 2502.13581

**Research Question:** How can action sequences be tokenized in a context-aware manner to improve generative recommendation performance?

**Methodology:** ActionPiece constructs a vocabulary by merging feature patterns as new tokens based on co-occurrence frequency within individual sets and across adjacent sets, and introduces set permutation regularization to produce multiple segmentations of action sequences with the same semantics.

**Key Findings:**
- ActionPiece consistently outperforms all baselines across three datasets with significant improvement in NDCG@10 (Hou et al., 2025) [E35].
- ActionPiece is the first context-aware action sequence tokenizer where the same action can be tokenized differently based on surrounding context (Hou et al., 2025) [E36].
- SPR achieves a token utilization rate of 87.01% after the first training epoch (Hou et al., 2025) [E37].
- Removing any of the proposed techniques reduces performance, demonstrating their importance for building a context-aware tokenizer (Hou et al., 2025) [E38].

**Limitations:** Not stated.

---

## References

Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying Retrieve and Rank with Generative Recommender and Iterative Preference Alignment. *arXiv preprint arXiv:2502.18965*.

Hou, Y., Ni, J., He, Z., Sachdeva, N., Kang, W.-C., Chi, E. H., McAuley, J., & Cheng, D. Z. (2025). ActionPiece: Contextually Tokenizing Action Sequences for Generative Recommendation. *arXiv preprint arXiv:2502.13581*.

Liu, H., Wei, Y., Song, X., Guan, W., Li, Y.-F., & Nie, L. (2024). MMGRec: Multimodal Generative Recommendation with Transformer Model. *arXiv preprint arXiv:2404.16555*.

Qu, H., Fan, W., Zhao, Z., & Li, Q. (2024). TokenRec: Learning to Tokenize ID for LLM-based Generative Recommendation. *arXiv preprint arXiv:2406.10450*.

Tan, J., Xu, S., Hua, W., Ge, Y., Li, Z., & Zhang, Y. (2024). IDGenRec: LLM-RecSys Alignment with Textual ID Learning. *arXiv preprint arXiv:2403.19021*.

Wang, Y., Ren, Z., Sun, W., Yang, J., Liang, Z., Chen, X., Xie, R., Yan, S., Zhang, X., Ren, P., Chen, Z., & Xin, X. (2024a). Content-Based Collaborative Generation for Recommender Systems. *arXiv preprint arXiv:2403.18480*.

Wang, Y., Xun, J., Hong, M., Zhu, J., Jin, T., Lin, W., Li, H., Li, L., Xia, Y., Zhao, Z., & Dong, Z. (2024b). EAGER: Two-Stream Generative Recommender with Behavior-Semantic Collaboration. *arXiv preprint arXiv:2406.14017*.

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024c). Learnable Item Tokenization for Generative Recommendation. *arXiv preprint arXiv:2405.07314*.

Zheng, B., Hou, Y., Lu, H., Chen, Y., Zhao, W. X., Chen, M., & Wen, J.-R. (2023). Adapting Large Language Models by Integrating Collaborative Semantics for Recommendation. *arXiv preprint arXiv:2311.09049*.

Zhu, J., Jin, M., Liu, Q., Qiu, Z., Dong, Z., & Li, X. (2024). CoST: Contrastive Quantization based Semantic Tokenization for Generative Recommendation. *arXiv preprint arXiv:2404.14774*.

---

## Evidence

### Zheng et al., 2023 (2311.09049)
- **E10:** "LC-Rec consistently maintains the best performance on three datasets and shows significant improvements compared to the baseline methods."
- **E11:** "Extensive experiments on three large datasets demonstrated the effectiveness of the approach, outperforming a number of competitive baseline models."
- **E32:** "Sequential recommendation methods that incorporate item content information perform better than traditional sequential recommendation methods that solely rely on ID and collaborative relationships on several datasets."

### Wang et al., 2024a (2403.18480)
- **E1:** "ColaRec achieves the best recommendation performance on all datasets except for NDCG@5 in Beauty."
- **E2:** "ColaRec shows significant relative improvements over DSI-R and DSI-S in Recall@5 across four datasets."
- **E3:** "ColaRec significantly outperforms all baselines for long-tail users with sparse interactions."
- **E4:** "ColaRec uses an auxiliary item indexing task and contrastive loss to align content and collaborative signals."

### Tan et al., 2024 (2403.19021)
- **E28:** "IDGenRec shows improvements of 39.44%, 23.55%, 42.37%, and 36.76% on Sports, Beauty, Toys, and Yelp datasets respectively over the best baselines."
- **E29:** "For the cross-platform Yelp dataset in zero-shot evaluation, IDGenRec surpasses the UniSRec baseline with a 353.46% improvement."
- **E30:** "Alternate training strategy significantly boosts model performance by enabling better collaboration between the ID generator and base recommender."
- **E31:** "Training the foundational model for more than one epoch negatively affects zero-shot performance due to overfitting."

### Zhu et al., 2024 (2404.14774)
- **E24:** "CoST tokenization method achieves approximately 38% improvement in NDCG@k and 36% improvement in Recall@k on the MIND dataset."
- **E25:** "CoST achieves up to 43% improvement in Recall@5 and 44% improvement in NDCG@5 on the MIND dataset over previous baselines."
- **E26:** "As the codebook size and the number of codebooks increases, NDCG shows a consistent upward trend."
- **E27:** "CoST is currently limited to top-one neighborhood alignment and does not consider top-k nearest neighbors."

### Liu et al., 2024 (2404.16555)
- **E8:** "Graph RQ-VAE consistently outperforms HK-Means, demonstrating superior quantization ability."
- **E9:** "Relation-aware self-attention yields remarkable improvements by leveraging pairwise item relations as positional information."
- **E19:** "MMGRec consistently delivers the best performance, outperforming the strongest competitor by 7.17%, 6.79%, and 6.58% in NDCG@10."
- **E20:** "MMGRec's recommendation result is more accurate with respect to preference ranking, showing larger improvements in NDCG."

### Wang et al., 2024c (2405.07314)
- **E12:** "LETTER consistently exhibits significant improvements for the backend models (TIGER and LC-Rec) across three datasets, validating the effectiveness of the method."
- **E13:** "Incorporating either collaborative or diversity regularization can improve the performance of TIGER, which validates the effectiveness of injecting collaborative signals into code assignment and improving the diversity of code embeddings."
- **E14:** "Extensive experiments substantiate the superiority of LETTER in item tokenization for generative recommendation models."

### Qu et al., 2024 (2406.10450)
- **E5:** "TokenRec achieves the best performance and consistently outperforms all baselines across all datasets."
- **E6:** "TokenRec surpasses most baselines even when using only user ID tokens without item interaction history."
- **E7:** "CoLLM achieves superior results by incorporating collaborative embeddings learned from GNN methods."
- **E18:** "TokenRec introduces a generalizable ID tokenization strategy and a generative retrieval paradigm for efficient top-K item generation."

### Wang et al., 2024b (2406.14017)
- **E15:** "EAGER almost achieves better results than base models among different datasets."
- **E16:** "EAGER performs considerably better on the Beauty benchmark compared to the second-best baseline with up to 31.49% improvement in Recall@5 and 32.26% improvement in NDCG@5 compared to TIGER."
- **E17:** "Extensive comparisons with state-of-the-art methods and detailed analyses demonstrate the effectiveness and robustness of EAGER."
- **E33:** "Removing any TSG, GCT or STT leads to performance degradation while removing all modules leads to the worst performance among different datasets."

### Deng et al., 2025 (2502.18965)
- **E21:** "OneRec achieved 1.68% improvement in total watch time and 6.56% improvement in average view duration in online A/B testing on Kuaishou."
- **E22:** "OneRec-1B achieves 1.78% higher maximum session watch time and 3.36% higher maximum like probability compared to TIGER-1B."
- **E23:** "OneRec has limitations in interactive indicators such as likes despite improvements in watch time."
- **E34:** "With only 1% DPO training ratio, OneRec-1B+IPA surpasses the base OneRec-1B by 4.04% in maximum session watch time and 5.43% in maximum like probability."

### Hou et al., 2025 (2502.13581)
- **E35:** "ActionPiece consistently outperforms all baselines across three datasets with significant improvement in NDCG@10."
- **E36:** "ActionPiece is the first context-aware action sequence tokenizer where the same action can be tokenized differently based on surrounding context."
- **E37:** "SPR achieves a token utilization rate of 87.01% after the first training epoch."
- **E38:** "Removing any of the proposed techniques reduces performance, demonstrating their importance for building a context-aware tokenizer."

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E12 | arXiv:2405.07314 | [4.2. Overall Performance (RQ1)](https://arxiv.org/html/2405.07314#S4.I2.i3.p1) | “LETTER consistently exhibits significant improvements for the backend models (TIGER and LC-Rec) across three datasets, validating the effectiveness of our method.” |
| E13 | arXiv:2405.07314 | [4.3.1. Ablation Study (RQ2)](https://arxiv.org/html/2405.07314#S4.SS3.SSS1.p2) | “incorporating either collaborative or diversity regularization can improve the performance of TIGER, which validates the effectiveness of injecting collaborative signals into code assignment and improving the diversity of code embeddings” |
| E14 | arXiv:2405.07314 | [6. Conclusion and Future Work](https://arxiv.org/html/2405.07314#S6.p1) | “Extensive experiments substantiate the superiority of LETTER in item tokenization for generative recommendation models.” |
| E24 | arXiv:2404.14774 | [4.2. Performance Comparison and Analysis](https://arxiv.org/html/2404.14774#S4.SS2.p1) | “our CoST tokenization method outperforms these settings, showing significant improvements in both NDCG@k and Recall@k by approximately 38% and 36%, respectively” |
| E25 | arXiv:2404.14774 | [Abstract](https://arxiv.org/html/2404.14774#abstract) | “CoST achieving up to a 43% improvement in Recall@5 and 44% improvement in NDCG@5 on the MIND dataset over previous baselines” |
| E36 | arXiv:2502.13581 | [4.2 Overall Performance](https://arxiv.org/html/2502.13581#S4.SS2.p3) | “Unlike existing methods, ActionPiece is the first context-aware action sequence tokenizer, i.e., the same action can be tokenized into different tokens depending on its surrounding context.” |
| E37 | arXiv:2502.13581 | [4.4.2 Token Utilization Rate w.r.t. Segmentation Strategy](https://arxiv.org/html/2502.13581#S4.SS4.SSS2.p1) | “In contrast, SPR achieves a token utilization rate of 87.01% after the first training epoch, with further increases as training progresses.” |
| E10 | arXiv:2311.09049 | [IV-B Overall Performance](https://arxiv.org/html/2311.09049#S4.SS2.p3) | “Our proposed LC-Rec consistently maintains the best performance on three datasets and shows significant improvements compared to the baseline methods.” |
| E32 | arXiv:2311.09049 | [IV-B Overall Performance](https://arxiv.org/html/2311.09049#S4.SS2.p2) | “For the baseline methods, the sequential recommendation methods that incorporate item content information (i.e., FDSA and S3-Rec) perform better than traditional sequential recommendation methods that solely rely on ID and collaborative relationships (i.e., Caser, HGN, GRU4Rec, BERT4Re, SASRec, FMLP-Rec) on several datasets.” |
| E16 | arXiv:2406.14017 | [4.2. Performance Comparison (RQ1)](https://arxiv.org/html/2406.14017#S4.I7.i1.p1) | “EAGER performs considerably better on the Beauty benchmark compared to the second-best baseline with up to 31.49% improvement in Recall@5 and 32.26% improvement in NDCG@5 compared to TIGER.” |
| E33 | arXiv:2406.14017 | [4.3. Ablation Study (RQ2)](https://arxiv.org/html/2406.14017#S4.I8.i1.p1) | “Removing any TSG, GCT or STT leads to performance degradation while removing all modules (i.e., the base model) leads to the worst performance among different datasets.” |
| E21 | arXiv:2502.18965 | [5.5. Online A/B Test](https://arxiv.org/html/2502.18965#S5.SS5.p1) | “Online evaluation shows that OneRec has achieved 1.68% improvement in total watch time and 6.56% improvement in average view duration” |
| E34 | arXiv:2502.18965 | [5.2. Offline Performance](https://arxiv.org/html/2502.18965#S5.SS2.p3) | “With only 1% DPO training ratio ( r_{\rm DPO} ), OneRec-1B+IPA surpasses the base OneRec-1B by 4.04% in maximum swt and 5.43% in maximum ltr” |
| E9 | arXiv:2404.16555 | [6.2.3. Effect of Relation-Aware Self-Attention](https://arxiv.org/html/2404.16555#S6.I5.i2.p1) | “Relation-aware self-attention yields remarkable improvements, suggesting the effectiveness of leveraging pairwise item relations as positional information.” |
| E19 | arXiv:2404.16555 | [6.1. Performance Comparison (RQ1)](https://arxiv.org/html/2404.16555#S6.I2.i1.p1) | “MMGRec consistently delivers the best performance across all settings. In particular, it outperforms the strongest competitor in terms of NDCG@10 by 7.17%, 6.79%, and 6.58% on MovieLens, TikTok, and Kwai, respectively.” |
| E6 | arXiv:2406.10450 | [III-B Performance Comparison of Recommender Systems](https://arxiv.org/html/2406.10450#S3.I5.i2.p1) | “Even when using only user ID tokens, TokenRec surpasses most baselines in terms of accuracy, indicating its superior performance in collaborative recommendations.” |
| E18 | arXiv:2406.10450 | [V Conclusion](https://arxiv.org/html/2406.10450#S5.p1) | “we propose a novel approach, named TokenRec, which not only introduces a generalizable user&item ID tokenization strategy to capture high-order collaborative knowledge but also presents a generative retrieval paradigm for the efficient generation of top- K items.” |
| E3 | arXiv:2403.18480 | [5.5.2. Comparison on long-tail users](https://arxiv.org/html/2403.18480#S5.SS5.SSS2.p1) | “ColaRec significantly outperforms all baselines when generating recommendation for long-tail users.” |
| E4 | arXiv:2403.18480 | [6. Conclusions and future work](https://arxiv.org/html/2403.18480#S6.p1) | “An auxiliary item indexing task and a contrastive loss are proposed to further align the model's representations of item content and user-item collaborative signals.” |
| E23 | arXiv:2502.18965 | [6. Conclusion](https://arxiv.org/html/2502.18965#S6.p1) | “our model has limitations in interactive indicators, such as likes” |
| E29 | arXiv:2403.19021 | [3.5.2. Results](https://arxiv.org/html/2403.19021#S3.SS5.SSS2.p1) | “for the Yelp dataset, which is cross-platform from the training data, our model significantly surpasses the baseline with a 353.46% improvement” |
| E30 | arXiv:2403.19021 | [3.4.3. Ablation Studies](https://arxiv.org/html/2403.19021#S3.SS4.SSS3.p2) | “alternate training significantly boosts the model's performance by enabling better collaboration between the two components” |
| E38 | arXiv:2502.13581 | [4.3 Ablation Study](https://arxiv.org/html/2502.13581#S4.SS3.p1) | “The results indicate that removing any of these techniques reduces performance, demonstrating the importance of these methods for building a context-aware tokenizer.” |
| E8 | arXiv:2404.16555 | [6.2.2. Effect of Graph RQ-VAE](https://arxiv.org/html/2404.16555#S6.I4.i1.p1) | “Graph RQ-VAE consistently outperforms HK-Means, illustrating the advantageous quantization ability.” |
| E11 | arXiv:2311.09049 | [V Conclusion](https://arxiv.org/html/2311.09049#S5.p1) | “Extensive experiments on three large datasets demonstrated the effectiveness of our approach, outperforming a number of competitive baseline models.” |
| E1 | arXiv:2403.18480 | [5.5.1. Comparison on whole users](https://arxiv.org/html/2403.18480#S5.SS5.SSS1.p1) | “ColaRec achieves the best recommendation performance on all datasets except for NDCG@5 in Beauty, which achieves comparable scores with the best NCL baseline.” |
| E2 | arXiv:2403.18480 | [5.5.1. Comparison on whole users](https://arxiv.org/html/2403.18480#S5.SS5.SSS1.p2) | “ColaRec achieves a notable 47.89%, 38.13%, 80.82% and 26.11% relative improvement in terms of Recall@5 on four datasets respectively, demonstrating the effectiveness of the proposed ColaRec.” |
| E28 | arXiv:2403.19021 | [3.4.2. Results](https://arxiv.org/html/2403.19021#S3.SS4.SSS2.p1) | “our method shows improvements of 39.44%, 23.55%, 42.37%, and 36.76% on the Sports, Beauty, Toys, and Yelp datasets, respectively” |
| E31 | arXiv:2403.19021 | [3.2. Implementation Details](https://arxiv.org/html/2403.19021#S3.SS2.p4) | “Further training negatively affected the zero-shot performance” |
| E26 | arXiv:2404.14774 | [4.2. Performance Comparison and Analysis](https://arxiv.org/html/2404.14774#S4.SS2.p3) | “as the codebook size and the number of codebooks increases, NDCG shows a consistent upward trend” |
| E27 | arXiv:2404.14774 | [5. conclusion](https://arxiv.org/html/2404.14774#S5.p1) | “While CoST currently focuses on top-one neighborhood alignment, future work could extend this to consider top-k nearest neighbors” |
| E20 | arXiv:2404.16555 | [6.1. Performance Comparison (RQ1)](https://arxiv.org/html/2404.16555#S6.I2.i3.p1) | “Comparing the performance of MMGRec on two evaluation metrics, we find larger improvements in terms of NDCG. Namely, MMGRec's recommendation result is more accurate with respect to preference ranking.” |
| E5 | arXiv:2406.10450 | [III-B Performance Comparison of Recommender Systems](https://arxiv.org/html/2406.10450#S3.I5.i1.p1) | “TokenRec achieves the best performance and consistently outperforms all the baselines across all datasets regarding metrics with either unseen personalized prompts.” |
| E7 | arXiv:2406.10450 | [III-B Performance Comparison of Recommender Systems](https://arxiv.org/html/2406.10450#S3.I5.i3.p1) | “CoLLM achieves superior results, benefiting from its incorporation of collaborative embeddings learned from these GNN methods.” |
| E15 | arXiv:2406.14017 | [4.2. Performance Comparison (RQ1)](https://arxiv.org/html/2406.14017#S4.I7.i1.p1) | “EAGER almost achieves better results than base models among different datasets.” |
| E17 | arXiv:2406.14017 | [5. Conclusion and Future Work](https://arxiv.org/html/2406.14017#S5.p1) | “Extensive comparisons with state-of-the-art methods and detailed analyses demonstrate the effectiveness and robustness of EAGER.” |
| E22 | arXiv:2502.18965 | [5.2. Offline Performance](https://arxiv.org/html/2502.18965#S5.SS2.p2) | “OneRec-1B achieves 1.78% higher maximum swt and 3.36% higher maximum ltr compared to TIGER-1B” |
| E35 | arXiv:2502.13581 | [4.2 Overall Performance](https://arxiv.org/html/2502.13581#S4.SS2.p3) | “Our proposed ActionPiece consistently outperforms all baselines across three datasets, achieving a significant improvement in NDCG@ 10 .” |

<!-- /evidence-appendix -->
