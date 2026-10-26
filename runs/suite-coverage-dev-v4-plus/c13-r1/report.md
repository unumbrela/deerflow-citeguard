# Systematic Literature Review: Generative Recommendation - Data, Model, and Tasks

**Review Date:** October 26, 2026  
**Search Period:** October 31, 2023 - October 30, 2025  
**Category:** cs.IR (Information Retrieval)  
**Format:** APA Style

---

## Executive Summary

Generative recommendation has emerged as a transformative paradigm in recommender systems, leveraging large language models (LLMs) to shift from traditional ranking-based approaches to text-to-text generation frameworks. This review synthesizes 10 key papers published between 2023-2025 that address three critical dimensions: **data preparation** (item tokenization and indexing), **model architectures** (generative frameworks), and **task formulations** (alignment and optimization strategies). The literature reveals a clear evolution from simple ID-based representations to sophisticated learnable tokenization methods that integrate collaborative semantics, multimodal information, and behavioral signals.

---

## 1. Introduction

The integration of large language models into recommender systems has fundamentally changed how items are indexed, retrieved, and ranked. Traditional recommender systems rely on embedding-based retrieval with continuous representations, while generative approaches treat recommendation as an autoregressive sequence generation problem. This shift necessitates solving several fundamental challenges:

1. **Semantic Gap**: LLMs operate on language semantics while recommender systems require collaborative semantics derived from user-item interactions
2. **Item Tokenization**: Transforming discrete item IDs into meaningful tokens within LLM vocabulary
3. **Architecture Design**: Creating unified frameworks that handle both behavioral and semantic information
4. **Task Alignment**: Developing training objectives that effectively align LLM capabilities with recommendation goals

This review examines how recent research addresses these challenges across data, model, and task dimensions.

---

## 2. Methodology

### Search Strategy
- **Database**: arXiv preprint server
- **Category**: cs.IR (Information Retrieval)
- **Time Window**: October 31, 2023 - October 30, 2025
- **Search Query**: "Generative Recommendation"
- **Initial Pool**: 50 papers
- **Reference Expansion**: 92 additional papers from citations
- **Shortlist**: 30 papers
- **Final Selection**: 10 papers based on centrality to data, model, and tasks

### Selection Criteria
Papers were selected based on:
- Focus on generative approaches for recommendation
- Coverage of data preparation, model architectures, or task formulations
- Citation impact and relevance to core themes
- Methodological novelty and empirical validation

---

## 3. Thematic Analysis

### 3.1 Data: Item Tokenization and Indexing Strategies

The foundation of generative recommendation lies in how items are tokenized and indexed for LLM consumption. Five papers in this review focus primarily on data representation challenges.

#### **Learnable Tokenization Approaches**

**Wang et al. (2024)** introduced LETTER (Learnable Tokenizer for Generative Recommendation), addressing critical limitations in existing item tokenization methods. The framework integrates three key components:
- **Residual Quantized VAE** for semantic regularization
- **Contrastive alignment loss** for collaborative regularization
- **Diversity loss** to mitigate code assignment bias

Their approach satisfies essential identifier requirements by incorporating hierarchical semantics, collaborative signals, and code assignment diversity. Experiments across three datasets demonstrated state-of-the-art performance, validating the importance of learnable tokenization over fixed ID or textual representations.

**Zhu et al. (2024)** proposed CoST (Contrastive Quantization-based Semantic Tokenization), highlighting that traditional vector quantization with reconstruction loss fails to capture neighborhood relationships vital for recommendation. Their contrastive quantization approach leverages both item relationships and semantic information, achieving remarkable improvements: **43% gain in Recall@5** and **44% gain in NDCG@5** on the MIND dataset. This work establishes semantic tokenization as a crucial preliminary step with significant downstream impact.

**Qu et al. (2024)** developed TokenRec with a Masked Vector-Quantized (MQ) Tokenizer that quantizes masked user/item representations from collaborative filtering into discrete tokens. This approach achieves two goals:
1. Smooth incorporation of high-order collaborative knowledge
2. Generalizable tokenization for unseen users/items

Their generative retrieval paradigm eliminates time-consuming autoregressive decoding and beam search, significantly reducing inference time while maintaining recommendation quality.

#### **Semantic-Collaborative Integration**

**Zheng et al. (2023)** presented LC-Rec, addressing the semantic gap between LLMs and recommender systems through two major contributions:
- **Learning-based vector quantization** with uniform semantic mapping for meaningful, non-conflicting item indices
- **Specially designed tuning tasks** to enhance collaborative semantics integration in LLMs

Their approach directly generates items from the entire item set without candidate pre-selection, demonstrating that deep integration of language and collaborative semantics enables effective LLM adaptation for recommendation.

**Wang et al. (2024)** proposed ColaRec (Content-Based Collaborative Generation), a sequence-to-sequence framework generating item identifiers from user interaction sequences. Key innovations include:
- **Generative Identifiers (GIDs)** constructed from pretrained collaborative filtering models
- **Item indexing task** for alignment between content-based semantic and interaction-based collaborative spaces
- **Contrastive loss** ensuring items with similar collaborative GIDs have similar content representations

This unified framework captures both collaborative signals and content information, outperforming baselines across four benchmark datasets.

#### **Textual ID Learning**

**Tan et al. (2024)** introduced IDGen, representing items as unique, concise, semantically rich textual IDs using human language tokens. Their approach trains a textual ID generator alongside the LLM-based recommender, enabling seamless integration of personalized recommendations into natural language generation. Notably, they demonstrated **foundation model potential**: a model pretrained on 19 datasets achieved zero-shot performance on 6 unseen datasets comparable to or better than traditional supervised models, suggesting a path toward universal generative recommendation models.

### 3.2 Model: Architecture Design and Information Integration

Model architecture determines how behavioral and semantic information is processed and combined for generation.

#### **Two-Stream Architectures**

**Wang et al. (2024)** developed EAGER (Two-Stream Generative Recommender), addressing the limitation of existing methods that focus solely on behavioral OR semantic aspects. Their architecture features:
- **Shared encoder** with two separate decoders for behavior tokens and semantic tokens
- **Confidence-based ranking strategy** for combining decoder outputs
- **Global contrastive task** with summary tokens for discriminative decoding
- **Semantic-guided transfer task** promoting cross-interactions through reconstruction and estimation objectives

The two-stream design ensures sufficient and independent learning for each information type while fostering subtle interactions that enhance collaborative information utilization. Validation across four public benchmarks demonstrated superior performance over existing methods.

#### **Multimodal Integration**

**Liu et al. (2024)** extended generative recommendation to multimodal settings with MMGRec, addressing limitations of the embed-and-retrieve paradigm (inference cost, interaction modeling, false-negatives). Their approach includes:
- **Graph RQ-VAE** for hierarchical quantization assigning Rec-IDs from multimodal and collaborative filtering information
- **Transformer-based recommender** generating Rec-IDs autoregressively from historical interaction sequences
- **Relation-aware self-attention mechanism** handling non-sequential interaction sequences by exploring element pairwise relations

This work demonstrates that generative paradigms can effectively incorporate multimodal information (visual, textual, audio) alongside collaborative signals, moving beyond purely interaction-based recommendation.

#### **Unified Retrieve-and-Rank Frameworks**

**Deng et al. (2025)** proposed OneRec, the first end-to-end generative model unifying retrieve and rank stages, replacing cascaded learning frameworks. Deployed in Kuaishou's main scene, it achieved a **1.6% increase in watch-time**. Key components include:
- **Encoder-decoder structure** with sparse Mixture-of-Experts (MoE) scaling model capacity without proportional FLOP increases
- **Session-wise generation** producing contextually coherent results versus point-by-point generation with hand-crafted rules
- **Iterative Preference Alignment** with Direct Preference Optimization (DPO), customized for recommendation's single-opportunity display constraint

This work represents a significant industrial validation of generative recommendation, demonstrating real-world impact beyond academic benchmarks.

### 3.3 Tasks: Alignment, Benchmarking, and Optimization

Task formulation determines how models are trained and evaluated for generative recommendation.

#### **LLM Alignment Strategies**

Multiple papers address alignment between LLM capabilities and recommendation requirements:

**Zheng et al. (2023)** designed specially tuned tasks enforcing LLMs to integrate language and collaborative semantics through learned item indices, moving beyond simple instruction following to deep semantic integration.

**Deng et al. (2025)** customized DPO for recommendation by designing a reward model to simulate user generation and a specialized sampling strategy addressing the single-opportunity constraint. Their Iterative Preference Alignment module demonstrated that limited DPO samples can significantly align user interest preferences.

**Tan et al. (2024)** aligned LLMs with recommendation needs through textual ID learning, decoupling user history from original datasets and expressing it in natural language, suggesting foundational model potential.

#### **Benchmarking and Evaluation**

**Hou et al. (2024)** introduced BLaIR, a comprehensive benchmark for evaluating LLMs as semantic encoders in recommendation, addressing the gap between general-purpose embedding benchmarks (e.g., MTEB) and recommendation-specific requirements. Contributions include:
- **Large-scale Amazon Reviews 2023 dataset** with 570M reviews and 48M items
- **Unified benchmark** covering sequential recommendation, collaborative filtering, and product search
- **Complex-query product search task** with semi-synthetic and real-world evaluation datasets

Experiments with 11 leading LLMs revealed **low correlation between MTEB rankings and BLaIR performance**, highlighting unique challenges of semantic encoding in recommendation and the inadequacy of general-purpose benchmarks for model selection.

#### **Contrastive and Ranking-Guided Objectives**

Several papers employ contrastive learning and ranking-guided objectives:

**Wang et al. (2024)** (LETTER) used contrastive alignment loss for collaborative regularization and proposed ranking-guided generation loss to theoretically augment ranking ability.

**Zhu et al. (2024)** (CoST) demonstrated that contrastive quantization capturing item relationships significantly outperforms reconstruction-only objectives.

**Wang et al. (2024)** (ColaRec) introduced contrastive loss ensuring alignment between collaborative GIDs and content representations.

**Wang et al. (2024)** (EAGER) employed global contrastive tasks with summary tokens for discriminative decoding.

This consistent use of contrastive objectives across multiple works suggests they are essential for effective generative recommendation training.

---

## 4. Synthesis and Comparative Analysis

### 4.1 Evolution of Tokenization Strategies

The literature reveals a clear progression in tokenization approaches:

| Approach | Representation | Limitations | Solutions |
|----------|---------------|-------------|-----------|
| **ID-based** | Discrete indices | No semantic meaning | Learnable tokenization |
| **Textual** | Natural language | Missing collaborative signals | Collaborative alignment |
| **Codebook** | Vector quantization | Code assignment bias | Diversity loss |
| **Learnable** | Hierarchical tokens | - | LETTER, CoST, TokenRec |

**Key Insight**: Effective tokenization must simultaneously capture semantic meaning, collaborative signals, and assignment diversity—no single aspect suffices.

### 4.2 Architecture Patterns

Three dominant architecture patterns emerge:

1. **Encoder-Decoder** (LC-Rec, OneRec, ColaRec): Separates understanding (encoding user history) from generation (decoding item tokens)
2. **Two-Stream** (EAGER): Parallel processing of behavioral and semantic information with confidence-based fusion
3. **Transformer-based** (MMGRec, TokenRec): Leverages self-attention for interaction modeling with relation-aware mechanisms

**Key Insight**: Architecture choice depends on information types (unimodal vs. multimodal) and deployment constraints (inference latency vs. accuracy).

### 4.3 Task Design Principles

Effective task formulation follows three principles:

1. **Alignment**: Tasks must bridge LLM language semantics with recommendation collaborative semantics
2. **Contrastive Learning**: Positive-negative pair objectives improve discriminative capability
3. **Ranking Guidance**: Generation objectives should incorporate ranking metrics (e.g., NDCG, Recall)

**Key Insight**: Standard NLP tasks (e.g., next token prediction) are insufficient; recommendation-specific objectives are essential.

### 4.4 Industrial Validation

Only **OneRec** (Deng et al., 2025) reports real-world deployment results, achieving 1.6% watch-time improvement at Kuaishou. This gap between academic benchmarks and industrial validation represents an important limitation in current literature.

---

## 5. Research Gaps and Future Directions

### 5.1 Identified Gaps

1. **Limited Industrial Validation**: Only one paper reports production deployment metrics
2. **Cold Start Generalization**: While TokenRec addresses unseen users/items, comprehensive evaluation remains limited
3. **Multimodal Depth**: MMGRec introduces multimodal generative recommendation, but integration depth (beyond Rec-ID assignment) needs exploration
4. **Foundation Model Potential**: IDGen suggests foundation models, but systematic evaluation across domains is preliminary
5. **Computational Efficiency**: Generative approaches incur higher inference costs; only TokenRec explicitly addresses latency

### 5.2 Future Research Directions

1. **Scalable Deployment**: Research on efficient inference (caching, distillation, pruning) for production systems
2. **Cross-Domain Foundation Models**: Systematic evaluation of zero-shot transfer across recommendation domains
3. **Multimodal Generation**: Moving beyond multimodal Rec-ID assignment to multimodal content generation
4. **User Feedback Integration**: Incorporating explicit user feedback into generative loops beyond implicit interactions
5. **Ethical Considerations**: Addressing bias, fairness, and transparency in generative recommendation systems

---

## 6. Conclusion

Generative recommendation represents a paradigm shift from ranking-based to generation-based approaches, enabled by advances in large language models and learnable tokenization. This review of 10 key papers reveals three critical success factors:

1. **Data**: Effective item tokenization integrating semantic, collaborative, and diversity constraints (LETTER, CoST, TokenRec)
2. **Model**: Architectures handling multiple information types through two-stream or unified designs (EAGER, OneRec, MMGRec)
3. **Tasks**: Alignment objectives bridging LLM and recommendation semantics through contrastive and ranking-guided learning (LC-Rec, IDGen, ColaRec)

The field has progressed from proof-of-concept demonstrations to industrial validation (OneRec at Kuaishou), with foundation model potential emerging (IDGen). However, challenges remain in computational efficiency, cross-domain generalization, and comprehensive multimodal integration. Future work should prioritize production deployment studies, efficient inference methods, and ethical considerations to realize the full potential of generative recommendation systems.

---

## References

Deng, J., Wang, S., Cai, K., Ren, L., Hu, Q., Ding, W., Luo, Q., & Zhou, G. (2025). OneRec: Unifying retrieve and rank with generative recommender and iterative preference alignment. *arXiv preprint arXiv:2502.18965*. https://arxiv.org/abs/2502.18965

Hou, Y., Li, J., Fu, X., He, Z., Yan, A., Chen, X., & McAuley, J. (2024). Bridging language and items for retrieval and recommendation: Benchmarking LLMs as semantic encoders. *arXiv preprint arXiv:2403.03952*. https://arxiv.org/abs/2403.03952

Liu, H., Wei, Y., Song, X., Guan, W., Li, Y.-F., & Nie, L. (2024). MMGRec: Multimodal generative recommendation with transformer model. *arXiv preprint arXiv:2404.16555*. https://arxiv.org/abs/2404.16555

Qu, H., Fan, W., Zhao, Z., & Li, Q. (2024). TokenRec: Learning to tokenize ID for LLM-based generative recommendation. *arXiv preprint arXiv:2406.10450*. https://arxiv.org/abs/2406.10450

Tan, J., Xu, S., Hua, W., Ge, Y., Li, Z., & Zhang, Y. (2024). IDGenRec: LLM-RecSys alignment with textual ID learning. *arXiv preprint arXiv:2403.19021*. https://arxiv.org/abs/2403.19021

Wang, Y., Xun, J., Hong, M., Zhu, J., Jin, T., Lin, W., Li, H., Li, L., Xia, Y., Zhao, Z., & Dong, Z. (2024). EAGER: Two-stream generative recommender with behavior-semantic collaboration. *arXiv preprint arXiv:2406.14017*. https://arxiv.org/abs/2406.14017

Wang, Y., Ren, Z., Sun, W., Yang, J., Liang, Z., Chen, X., Xie, R., Yan, S., Zhang, X., Ren, P., Chen, Z., & Xin, X. (2024). Content-based collaborative generation for recommender systems. *arXiv preprint arXiv:2403.18480*. https://arxiv.org/abs/2403.18480

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. *arXiv preprint arXiv:2405.07314*. https://arxiv.org/abs/2405.07314

Zheng, B., Hou, Y., Lu, H., Chen, Y., Zhao, W. X., Chen, M., & Wen, J.-R. (2023). Adapting large language models by integrating collaborative semantics for recommendation. *arXiv preprint arXiv:2311.09049*. https://arxiv.org/abs/2311.09049

Zhu, J., Jin, M., Liu, Q., Qiu, Z., Dong, Z., & Li, X. (2024). CoST: Contrastive quantization based semantic tokenization for generative recommendation. *arXiv preprint arXiv:2404.14774*. https://arxiv.org/abs/2404.14774

---

## Appendix: Screening Statistics

- **Initial search results**: 50 papers
- **Papers added from reference expansion**: 92 papers
- **Total shortlist**: 30 papers
- **Papers screened**: 30 papers
- **Final selection**: 10 papers
- **Papers from references**: 6 out of 10 selected papers
- **Screening score distribution**:
  - Score 0: 0 papers
  - Score 1: 1 paper
  - Score 2: 6 papers
  - Score 3: 23 papers
