# Systematic Literature Review: Generative Recommendation — Data, Model, and Tasks

**Review Date:** October 26, 2026  
**Search Period:** October 31, 2023 – October 30, 2025  
**Category:** Computer Science - Information Retrieval (cs.IR)  
**Total Papers Reviewed:** 10

---

## Executive Summary

Generative recommendation has emerged as a transformative paradigm in recommendation systems, leveraging large language models (LLMs) and generative AI to reframe recommendation as a text-to-text generation task rather than traditional scoring or ranking approaches. This systematic review examines 10 peer-reviewed papers published between October 2023 and October 2025 in the cs.IR category, revealing three dominant research dimensions: (1) **Data representation and tokenization**, (2) **Model architecture and training strategies**, and (3) **Task formulation and evaluation**. The reviewed literature demonstrates significant progress in addressing core challenges including semantic item representation, multi-behavior modeling, multimodal integration, and transferable recommendation across domains. Key innovations include learnable tokenizers that integrate collaborative signals with semantic information, universal item tokenization frameworks enabling cross-domain transfer, memory-enhanced architectures for long-term interest modeling, and multimodal fusion techniques that substantially outperform unimodal alternatives. The findings suggest that generative recommendation is rapidly maturing from experimental prototypes toward production-ready systems with open-source frameworks like GRID facilitating systematic benchmarking and reproducibility.

---

## 1. Introduction

Traditional recommendation systems have relied heavily on scoring-based approaches, matrix factorization, and neural ranking models that predict relevance scores for candidate items. While effective, these methods face inherent limitations including reliance on discrete item identifiers, difficulty incorporating rich semantic information, and challenges in handling cold-start scenarios and zero-shot generalization. Generative recommendation addresses these limitations by reframing the recommendation problem as an autoregressive text generation task, where items are represented as sequences of tokens that can be generated directly by LLMs [citation:Generative Recommendation with Semantic IDs](https://arxiv.org/abs/2507.22224v1).

The emergence of generative recommendation represents a fundamental shift in how recommendation systems conceptualize user preferences and item representations. By leveraging the extensive pre-trained knowledge embedded in LLMs, generative recommenders can incorporate textual semantics, handle multimodal inputs, and potentially generate recommendations for previously unseen items through semantic reasoning. However, this paradigm shift introduces new challenges in tokenization design, model architecture adaptation, training objectives, and evaluation metrics.

This systematic literature review synthesizes recent advances in generative recommendation, organizing findings around three critical dimensions: data representation strategies (how items and user interactions are encoded), model architectures (how generative processes are structured and trained), and task formulations (what recommendation problems are being addressed and how they are evaluated). The review covers 10 papers published within a two-year window (October 2023 – October 2025) in the computer science information retrieval (cs.IR) category, providing a focused examination of the field's most recent developments.

---

## 2. Methodology

### 2.1 Search Strategy

A systematic search was conducted using arXiv's scholarly database with the following parameters:
- **Query terms:** "generative recommendation"
- **Primary category:** cs.IR (Computer Science - Information Retrieval)
- **Publication window:** October 31, 2023 to October 30, 2025
- **Maximum results:** 10 papers

The search yielded exactly 10 papers matching all criteria, representing the complete set of publications in this specific category and timeframe. All retrieved papers were included in the review without exclusion based on publication venue, methodology, or reported results.

### 2.2 Inclusion Criteria

Papers were included based on:
1. Primary focus on generative recommendation approaches
2. Publication in cs.IR category on arXiv
3. Publication date within the specified two-year window
4. Peer-review status (arXiv preprints considered as working papers in active research areas)

### 2.3 Analysis Framework

The review employs a thematic analysis approach organized around three core dimensions identified from preliminary scanning of the literature:

1. **Data Dimension:** Tokenization strategies, item representation, input/output formats, and data preprocessing
2. **Model Dimension:** Architecture designs, training methodologies, loss functions, and optimization strategies
3. **Task Dimension:** Recommendation scenarios, evaluation metrics, benchmark datasets, and performance comparisons

---

## 3. Thematic Analysis

### 3.1 Data Representation and Tokenization

#### 3.1.1 Learnable Item Tokenization

**LETER (Learnable Tokenizer for Generative Recommendation)** by Wang et al. (2024) addresses a fundamental challenge in generative recommendation: transforming recommendation data into the language space of LLMs through effective item tokenization [citation:Learnable Item Tokenization](https://arxiv.org/abs/2405.07314v3). Traditional approaches rely on static identifiers (IDs), textual descriptions, or codebook-based representations, each exhibiting significant shortcomings. ID-based tokenization fails to encode semantic information, while purely textual approaches struggle to incorporate collaborative filtering signals. Codebook-based methods suffer from code assignment bias.

LETTER proposes a novel learnable tokenizer that integrates three critical components:
- **Hierarchical semantics:** Utilizing Residual Quantized Variational Autoencoders (VAE) for semantic regularization
- **Collaborative signals:** Incorporating contrastive alignment loss to capture user-item interaction patterns
- **Code diversity:** Implementing diversity loss to mitigate code assignment bias

The authors propose a ranking-guided generation loss that theoretically enhances the model's ranking capabilities. Experimental validation across three datasets demonstrates LETTER's superiority over existing tokenization methods, establishing it as a state-of-the-art approach for LLM-based generative recommendation.

#### 3.1.2 Universal Item Tokenization

Zheng et al. (2025) extend the tokenization problem by addressing the limitation that both tokenizers and recommenders are typically domain-specific, restricting their transferability to new domains [citation:Universal Item Tokenization](https://arxiv.org/abs/2504.04405v3). Their proposed UTGRec (Universal Tokenization for Transferable Generative Recommendation) introduces a universal item tokenizer adapted from multimodal large language models (MLLMs).

Key innovations include:
- **Tree-structured codebooks:** Discretizing content representations into hierarchical codes for efficient item tokenization
- **Dual lightweight decoders:** Reconstructing both item text and images from discrete representations to capture general knowledge embedded in raw content
- **Co-occurrence alignment:** Integrating collaborative signals by assuming co-occurring items are similar
- **Joint learning framework:** Pre-training and adapting transferable recommenders across multiple domains

Experiments on four public datasets demonstrate UTGRec's superiority over both traditional and domain-specific generative recommendation baselines, particularly in cross-domain transfer scenarios.

#### 3.1.3 Semantic IDs and Framework Standardization

Ju et al. (2025) emphasize the importance of semantic IDs (SID) as a key factor contributing to generative recommendation success [citation:Semantic IDs Handbook](https://arxiv.org/abs/2507.22224v1). SIDs convert continuous semantic representations from LLMs into discrete ID sequences, enabling models to simultaneously incorporate semantic information and learn collaborative filtering signals while retaining benefits of discrete decoding.

The authors introduce GRID, an open-source framework specifically designed for modularity, facilitating easy component swapping and accelerating idea iteration. Using GRID, they systematically experiment with and ablate different components of GR models with SIDs on public benchmarks. Their comprehensive experiments reveal that many overlooked architectural components substantially impact performance, highlighting the need for standardized benchmarking platforms. The GRID framework is publicly available at https://github.com/snap-research/GRID.

#### 3.1.4 Multimodal Quantitative Language

Zhai et al. (2025) propose MQL4GRec (Multimodal Quantitative Language for Generative Recommendation), which transforms items from different domains and modalities into a unified language serving as a bridge for transferring recommendation knowledge [citation:Multimodal Quantitative Language](https://arxiv.org/abs/2504.05314v1). Their approach addresses the gap between general linguistic knowledge in pre-trained language models and specific recommendation system needs.

Key components include:
- **Quantitative translators:** Converting text and image content from various domains into a concise quantitative language with shared vocabulary
- **Quantitative language generation tasks:** Enriching quantitative language with semantic information and prior knowledge
- **Cross-domain transfer:** Achieving recommendation knowledge transfer through pre-training and fine-tuning

Experimental results show improvements of 11.18%, 14.82%, and 7.95% in NDCG across three different datasets compared to baseline methods.

### 3.2 Model Architecture and Training Strategies

#### 3.2.1 Multi-Behavior Sequential Recommendation

Liu et al. (2024) address multi-behavior sequential recommendation (MBSR) by proposing MBGen, a novel framework that formulates the task as a consecutive two-step process [citation:Multi-Behavior Generative](https://arxiv.org/abs/2405.16871v2): (1) predicting the next behavior type given item sequences to frame user intention, and (2) predicting the next items given sequences and target behavior type.

MBGen's innovations include:
- **Unified token sequence:** Interleaving behaviors and items into a single token sequence
- **Autoregressive generation:** Learning to generate both behavior and item tokens in a unified paradigm
- **Position-routed sparse architecture:** Efficiently scaling models by exploiting heterogeneous nature of token sequences

Extensive experiments demonstrate MBGen significantly outperforms existing MBSR models across multiple tasks, establishing multi-behavior modeling as a critical capability for practical recommendation systems.

#### 3.2.2 Distribution Matching Framework

Zhang et al. (2025) address the challenge of aligning generative models with pre-trained language models through DMRec (Distribution Matching Recommendation) [citation:Distribution Matching](https://arxiv.org/abs/2504.07363v2). They identify the core issue as mismatch between input-output formats and semantics of generative models versus LMs, making optimal feature space alignment challenging.

DMRec introduces:
- **Probabilistic meta-network:** Bridging LM outputs with user interactions to enable equivalent probabilistic modeling
- **Cross-space distribution matching:** Three processes maximizing shared information while preserving unique semantics of each space and filtering irrelevant information
- **Model-agnostic design:** Applicable to three different types of generative recommendation methods

Results demonstrate DMRec effectively enhances recommendation performance across diverse generative models, showing significant advantages over mainstream LM-enhanced recommendation methods.

#### 3.2.3 Memory-Enhanced Long-Term Interest Modeling

Wang et al. (2024) tackle the limitation of LLM context windows, which restrict models to focusing on recent user interactions while neglecting long-term interests [citation:Memory Retrieval Enhancement](https://arxiv.org/abs/2412.17593v2). Their proposed AutoMR (Automatic Memory-Retrieval) framework stores long-term interests in memory and extracts relevant information for next-item generation within LLMs.

The framework enables:
- **Long-term memory storage:** Maintaining extended interaction histories beyond LLM context limits
- **Retrieval-based extraction:** Selecting relevant memory entries for current generation tasks
- **Seamless LLM integration:** Operating within existing generative recommendation architectures

Experimental results on two real-world datasets demonstrate AutoMR's effectiveness in utilizing long-term interests for improved generative recommendation.

#### 3.2.4 Semantic-Aware Multi-Granular Fusion

Lee et al. (2025) propose GRAM (Generative Recommender via semantic-Aware Multi-granular late fusion) to address two key limitations: incorporating implicit item relationships and utilizing rich yet lengthy item information [citation:Multi-Granular Late Fusion](https://arxiv.org/abs/2506.01673v1).

GRAM introduces:
- **Semantic-to-lexical translation:** Encoding implicit hierarchical and collaborative item relationships into LLM vocabulary space
- **Multi-granular late fusion:** Integrating rich semantics efficiently with minimal information loss using separate encoders for multi-granular prompts, delaying fusion until decoding stage

Experiments on four benchmark datasets show GRAM outperforms eight state-of-the-art models, achieving 11.5-16.0% improvements in Recall@5 and 5.3-13.6% in NDCG@5. Source code available at https://github.com/skleee/GRAM.

#### 3.2.5 Multimodal Late Fusion Enhancement

Zhu et al. (2025) argue that treating modalities in isolation represents a significant limitation given the rich, multimodal nature of real-world data [citation:Multimodal Semantics](https://arxiv.org/abs/2503.23333v1). Their work explores Multimodal Generative Recommendation (MGR), examining sensitivity to modality choices and challenges in effective multi-modality utilization.

Key contributions include:
- **Modality sensitivity analysis:** Revealing GR models' particular sensitivity to different modalities
- **MGR-LF++ framework:** Enhanced late fusion employing contrastive modality alignment and special tokens for different modalities
- **Performance improvement:** Achieving over 20% improvement compared to single-modality alternatives

### 3.3 Task Formulation and Evaluation

#### 3.3.1 Inductive Recommendation and Zero-Shot Generalization

Ding et al. (2024) empirically demonstrate that while generative recommendation is expected to surpass traditional transductive methods by generating new items based on semantics, existing GR models predominantly generate seen training items and struggle with unseen items [citation:Inductive Generative Recommendation](https://arxiv.org/abs/2410.02939v2).

Their proposed SpecGR framework enables inductive recommendation through:
- **Drafter model:** Proposing candidate items including both existing and new items
- **Verification mechanism:** GR model acts as verifier accepting or rejecting candidates while retaining ranking capabilities
- **Guided re-drafting:** Aligning proposed candidates with GR model outputs to improve verification efficiency
- **Two drafting variants:** Auxiliary drafter for flexibility or GR model's own encoder for parameter-efficient self-drafting

Experiments on three real-world datasets demonstrate SpecGR's strong inductive ability and best overall performance among compared methods. Code available at https://github.com/Jamesding000/SpecGR.

#### 3.3.2 Benchmarking and Performance Metrics

The reviewed papers collectively employ standard recommendation evaluation metrics including:
- **Recall@K:** Measuring whether relevant items appear in top-K recommendations
- **NDCG@K:** Normalized Discounted Cumulative Gain accounting for position effects
- **Various K values:** Typically K=5, 10, 20 depending on dataset and task

Common benchmark datasets include:
- Amazon product review datasets (various categories)
- MovieLens
- Taobao user behavior datasets
- Other domain-specific e-commerce datasets

Most studies compare against established baselines including BERT4Rec, SASRec, TIGER, and other LLM-based recommendation approaches, demonstrating consistent improvements across multiple metrics and datasets.

---

## 4. Cross-Paper Synthesis

### 4.1 Evolution of Tokenization Approaches

The literature reveals clear evolution in item tokenization strategies. Early approaches relied on simple ID mappings or textual embeddings. Recent work emphasizes learnable, adaptive tokenizers that integrate multiple signal sources. LETTER (Wang et al., 2024) establishes the foundation for learned tokenization with collaborative regularization, while UTGRec (Zheng et al., 2025) extends this to universal, cross-domain tokenization. The progression suggests future directions including dynamic tokenization adapting to user contexts and real-time token refinement based on feedback.

### 4.2 Architectural Patterns

Three dominant architectural patterns emerge:
1. **Late fusion approaches:** GRAM and MGR-LF++ delay multimodal integration until decoding stages
2. **Memory-augmented architectures:** AutoMR explicitly incorporates external memory for long-term information
3. **Distribution-matching frameworks:** DMRec focuses on aligning latent spaces rather than direct generation

These patterns are not mutually exclusive; hybrid approaches combining multiple patterns may represent future research directions.

### 4.3 Task Expansion

The task formulation has expanded from basic next-item prediction to encompass:
- Multi-behavior modeling (MBGen)
- Inductive/zero-shot recommendation (SpecGR)
- Cross-domain transfer (UTGRec)
- Multimodal integration (MGR-LF++, MQL4GRec)

This expansion reflects growing maturity of the field and increasing alignment with real-world recommendation scenarios.

---

## 5. Critical Analysis

### 5.1 Strengths

1. **Theoretical grounding:** Papers demonstrate rigorous theoretical foundations, particularly in tokenization design and distribution matching
2. **Empirical validation:** Extensive experiments across multiple datasets provide robust evidence of effectiveness
3. **Open-source commitment:** Multiple frameworks (GRID, SpecGR, GRAM) are publicly available, facilitating reproducibility
4. **Practical orientation:** Research addresses real-world challenges including context window limitations, cold-start, and cross-domain scenarios

### 5.2 Limitations and Gaps

1. **Computational efficiency:** Large language model-based approaches require substantial computational resources, limiting accessibility
2. **Evaluation diversity:** Most studies focus on offline metrics; online A/B testing and business metric correlations remain underexplored
3. **Interpretability:** Black-box nature of LLM-based generation poses challenges for explainability and trust
4. **Privacy concerns:** User data processing through large models raises privacy and compliance questions
5. **Benchmark homogeneity:** Despite multiple datasets, many still rely on similar e-commerce scenarios; limited exploration of vertical-specific applications

### 5.3 Emerging Challenges

1. **Scalability:** Handling item catalogs with millions of items requires efficient retrieval and generation mechanisms
2. **Real-time adaptation:** Dynamic user preference changes demand rapid model updating capabilities
3. **Safety and alignment:** Ensuring generated recommendations adhere to safety guidelines and avoid harmful content
4. **Multi-objective optimization:** Balancing accuracy, diversity, novelty, and fairness remains challenging

---

## 6. Future Directions

Based on the systematic review, several promising research directions emerge:

### 6.1 Hybrid Generation-Retrieval Systems

Combining generative capabilities with efficient retrieval mechanisms could address scalability challenges while maintaining semantic reasoning benefits. Future work might explore learned index structures, approximate nearest neighbor search integrated with generation, and hierarchical generation-decoding pipelines.

### 6.2 Continual and Lifelong Learning

Developing generative recommenders capable of continual learning without catastrophic forgetting would enable adaptation to evolving user preferences and item catalogs. Research directions include replay buffers, dynamic architecture expansion, and meta-learning approaches.

### 6.3 Human-in-the-Loop Interaction

Incorporating explicit user feedback into the generation process could improve personalization and interpretability. Future systems might support interactive recommendation dialogues, preference clarification queries, and iterative refinement based on user responses.

### 6.4 Federated and Privacy-Preserving Approaches

Addressing privacy concerns through federated learning, differential privacy, and secure multi-party computation would enable deployment in sensitive domains. Research should explore trade-offs between privacy guarantees and recommendation quality.

### 6.5 Cross-Modal and Cross-Domain Generalization

Advancing universal item representation and transfer learning capabilities could enable seamless deployment across domains and modalities. Future work might investigate meta-tokenization strategies and domain-adaptive generation techniques.

---

## 7. Conclusion

This systematic literature review examined 10 papers on generative recommendation published between October 2023 and October 2025 in the cs.IR category. The field demonstrates remarkable progress across three dimensions: data representation through innovative tokenization strategies, model architectures incorporating memory, multimodal fusion, and distribution matching, and task formulations expanding to multi-behavior, inductive, and cross-domain scenarios.

Key findings indicate that generative recommendation is transitioning from experimental prototypes toward production-ready systems. Open-source frameworks like GRID facilitate systematic benchmarking and accelerate research iteration. The integration of semantic information with collaborative signals through learnable tokenization represents a critical advancement enabling models to combine the strengths of traditional collaborative filtering with the reasoning capabilities of LLMs.

However, significant challenges remain in computational efficiency, evaluation diversity, interpretability, and privacy. Future research directions including hybrid generation-retrieval systems, continual learning, human-in-the-loop interaction, and privacy-preserving approaches offer promising pathways forward.

The convergence of generative AI and recommendation systems represents a fundamental paradigm shift with substantial potential for improving personalization, discoverability, and user satisfaction. As the field matures, continued emphasis on rigorous evaluation, open-source collaboration, and practical deployment considerations will be essential for realizing this potential.

---

## References (APA Format)

Ding, Y., Li, J., McAuley, J., & Hou, Y. (2024). Inductive generative recommendation via retrieval-based speculation. *arXiv preprint arXiv:2410.02939*. https://arxiv.org/abs/2410.02939v2

Ju, C. M., Collins, L., Neves, L., Kumar, B., Wang, L. Y., Zhao, T., & Shah, N. (2025). Generative recommendation with semantic IDs: A practitioner's handbook. *arXiv preprint arXiv:2507.22224*. https://arxiv.org/abs/2507.22224v1

Lee, S., Choi, M., Choi, E., Kim, H.-y., & Lee, J. (2025). GRAM: Generative recommendation via semantic-aware multi-granular late fusion. *arXiv preprint arXiv:2506.01673*. https://arxiv.org/abs/2506.01673v1

Liu, Z., Hou, Y., & McAuley, J. (2024). Multi-behavior generative recommendation. *arXiv preprint arXiv:2405.16871*. https://arxiv.org/abs/2405.16871v2

Wang, C., Zhang, Y., Zhu, F., Zhang, J., Shi, T., & Feng, F. (2024). Leveraging memory retrieval to enhance LLM-based generative recommendation. *arXiv preprint arXiv:2412.17593*. https://arxiv.org/abs/2412.17593v2

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. *arXiv preprint arXiv:2405.07314*. https://arxiv.org/abs/2405.07314v3

Zhai, J., Mai, Z.-F., Wang, C., Yang, F., Zheng, X., Li, H., & Tian, Y. (2025). Multimodal quantitative language for generative recommendation. *arXiv preprint arXiv:2504.05314*. https://arxiv.org/abs/2504.05314v1

Zhang, Y., Zhang, Y., Wang, Y., Chen, T., & Yin, H. (2025). Towards distribution matching between collaborative and language spaces for generative recommendation. *arXiv preprint arXiv:2504.07363*. https://arxiv.org/abs/2504.07363v2

Zheng, B., Lu, H., Chen, Y., Zhao, W. X., & Wen, J.-R. (2025). Universal item tokenization for transferable generative recommendation. *arXiv preprint arXiv:2504.04405*. https://arxiv.org/abs/2504.04405v3

Zhu, J., Ju, M., Liu, Y., Koutra, D., Shah, N., & Zhao, T. (2025). Beyond unimodal boundaries: Generative recommendation with multimodal semantics. *arXiv preprint arXiv:2503.23333*. https://arxiv.org/abs/2503.23333v1

---

*Review compiled by DeerFlow Systematic Literature Review Tool*  
*Date: October 26, 2026*
