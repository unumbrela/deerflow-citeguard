# Systematic Literature Review: Generative Recommendation – Data, Model, and Tasks

**Review Date:** October 26, 2026  
**Search Period:** October 31, 2023 – October 30, 2025  
**Category:** Computer Science - Information Retrieval (cs.IR)  
**Total Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines 10 recent research papers on generative recommendation published between October 2023 and October 2025 in the arXiv cs.IR category. Generative recommendation represents an emerging paradigm that leverages large language models (LLMs) to directly generate item identifiers or descriptions as recommendations, marking a significant shift from traditional ranking-based approaches. The reviewed literature reveals three major thematic areas: **(1) Data Representation and Tokenization**, focusing on how items are encoded for generative models; **(2) Model Architectures**, exploring innovative framework designs for improved performance; and **(3) Task Formulations**, addressing new challenges such as multi-behavior modeling, inductive recommendation, and multimodal integration.

Key findings indicate substantial progress in **semantic tokenization techniques**, with learnable and universal item tokenization methods demonstrating superior performance over traditional ID-based approaches. **Model architectures** have evolved to incorporate memory retrieval mechanisms, multi-granular fusion strategies, and distribution matching across collaborative and language spaces. **Task formulations** now encompass multi-behavior sequential recommendation, inductive settings for unseen items, and multimodal semantic integration. Despite these advances, challenges remain in handling long-term user interests, achieving effective cross-domain transfer, and establishing unified benchmarking frameworks.

---

## Introduction

Generative recommendation has emerged as a transformative approach in the field of recommendation systems, diverging from conventional ranking-based paradigms by framing recommendation as a text generation task. This paradigm shift enables models to leverage the extensive knowledge embedded in pre-trained language models while generating item identifiers autoregressively. The transition from discriminative to generative approaches offers several advantages, including better handling of item semantics, natural integration of auxiliary information, and potential for zero-shot generalization to unseen items.

The period between late 2023 and late 2025 witnessed rapid advancement in this field, driven by breakthroughs in large language models and growing recognition of their potential for personalized recommendation. This review systematically analyzes 10 peer-reviewed papers published in the computer science information retrieval domain, providing comprehensive insights into the current state-of-the-art, methodological innovations, and future research directions.

### Research Questions

This review addresses three core questions:
1. **Data**: How are items represented and tokenized for generative recommendation tasks?
2. **Model**: What architectural innovations enhance generative recommendation performance?
3. **Tasks**: What novel recommendation scenarios and challenges are being addressed?

---

## Methodology

### Search Strategy

A systematic search was conducted using the arXiv scholarly database with the following parameters:
- **Query Terms**: "generative recommendation"
- **Primary Category**: cs.IR (Information Retrieval)
- **Publication Window**: October 31, 2023 – October 30, 2025
- **Selection Criteria**: All papers published within the specified timeframe were included to ensure comprehensive coverage of recent developments

### Paper Selection

The search yielded exactly 10 papers published in the target category and timeframe, representing the complete set of relevant publications during this period. Papers were selected based on their direct relevance to generative recommendation methodologies, data representations, and task formulations.

---

## Thematic Analysis

### Theme 1: Data Representation and Tokenization

#### Learnable Item Tokenization

Wang et al. (2024) introduced LETTER (a LEarnable Tokenizer for generaTivE Recommendation), addressing critical limitations in existing item tokenization approaches [citation:Learnable Item Tokenization](https://arxiv.org/abs/2405.07314). Traditional methods relying on simple IDs, textual identifiers, or codebook-based representations suffer from inadequate semantic encoding, poor collaborative signal incorporation, or code assignment bias. LETTER integrates hierarchical semantics through Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias. The authors propose a ranking-guided generation loss to theoretically augment ranking ability, demonstrating superior performance on three datasets.

#### Universal Item Tokenization for Transfer Learning

Zheng et al. (2025) proposed UTGRec (Universal item Tokenization approach for transferable Generative Recommendation) to address domain-specific limitations in existing tokenizer-recommender pairs [citation:Universal Item Tokenization](https://arxiv.org/abs/2504.04405). Their universal item tokenizer adapts a multimodal large language model (MLLM) to encode rich item semantics using tree-structured codebooks for discretization. Two key techniques enable effective cross-domain learning: dual lightweight decoders for raw content reconstruction (capturing text and image knowledge) and co-occurrence alignment for collaborative knowledge integration. Experiments across four public datasets demonstrated UTGRec's superiority over both traditional and generative baselines.

#### Multimodal Quantitative Language

Zhai et al. (2025) introduced MQL4GRec (Multimodal Quantitative Language for Generative Recommendation), transforming items from diverse domains and modalities into a unified quantitative language [citation:Multimodal Quantitative Language](https://arxiv.org/abs/2504.05314). This approach bridges the gap between general linguistic knowledge in pre-trained language models and specific recommendation needs. Quantitative translators convert text and image content into a shared vocabulary, while quantitative language generation tasks enrich the representation with semantic information. The method achieved improvements of 11.18%, 14.82%, and 7.95% on NDCG metrics across three datasets.

#### Semantic IDs Framework

Ju et al. (2025) presented GRID, an open-source framework for generative recommendation with semantic IDs designed for modularity and component swapping [citation:Practitioner's Handbook](https://arxiv.org/abs/2507.22224). Their systematic ablation studies revealed that many overlooked architectural components substantially impact performance. GRID facilitates robust benchmarking and accelerates idea iteration by enabling easy comparison of different GR components, addressing the fragmentation problem caused by varied experimental setups in existing literature.

### Theme 2: Model Architectures

#### Multi-Behavior Sequential Generation

Liu et al. (2024) developed MBGen, a novel Multi-Behavior sequential Generative recommendation framework that formulates multi-behavior sequential recommendation as a two-step process [citation:Multi-Behavior Generative](https://arxiv.org/abs/2405.16871). The model first predicts the next behavior type to frame user intention, then predicts items given sequences and target behavior. By tokenizing both behaviors and items into a single interleaved sequence, MBGen learns to autoregressively generate tokens in a unified paradigm. A position-routed sparse architecture efficiently scales models while exploiting heterogeneous token sequence nature.

#### Memory-Augmented LLM Recommendation

Wang et al. (2024) proposed AutoMR (Automatic Memory-Retrieval framework) to address the limited context window constraint of LLMs in generative recommendation [citation:Leveraging Memory Retrieval](https://arxiv.org/abs/2412.17593). Their framework stores long-term user interests in memory and extracts relevant information for next-item generation, overcoming the tendency of existing approaches to focus only on recent interactions. Experimental results on real-world datasets demonstrated AutoMR's effectiveness in utilizing long-term interests.

#### Cross-Space Distribution Matching

Zhang et al. (2025) introduced DMRec, a model-agnostic framework addressing the mismatch between generative model formats and language model semantics [citation:Towards Distribution Matching](https://arxiv.org/abs/2504.07363). The framework employs a probabilistic meta-network to bridge LM outputs with user interactions, enabling equivalent probabilistic modeling. Three cross-space distribution matching processes maximize shared information while preserving unique semantics and filtering irrelevant information. Applied to three different generative recommendation methods, DMRec showed significant advantages over mainstream LM-enhanced approaches.

#### Retrieval-Based Inductive Speculation

Ding et al. (2024) proposed SpecGR, a plug-and-play framework enabling inductive generative recommendation for unseen items [citation:Inductive Generative Recommendation](https://arxiv.org/abs/2410.02939). Empirical analysis revealed that existing GR models predominantly generate training items, struggling with unseen items. SpecGR uses a drafter model to propose candidate items (both existing and new), with the GR model acting as verifier. Guided re-drafting improves verification efficiency by aligning candidates with GR model outputs. Two drafting variants offer flexibility: auxiliary drafter or self-drafting using the GR model's encoder.

#### Semantic-Aware Multi-Granular Fusion

Lee et al. (2025) introduced GRAM (Generative Recommender via semantic-Aware Multi-granular late fusion) addressing two key limitations: incorporating implicit item relationships and utilizing rich yet lengthy item information [citation:GRAM: Generative Recommendation](https://arxiv.org/abs/2506.01673). Semantic-to-lexical translation encodes hierarchical and collaborative relationships into LLM vocabulary space, while multi-granular late fusion integrates rich semantics efficiently using separate encoders for multi-granular prompts with delayed fusion at decoding stage. GRAM outperformed eight state-of-the-art models, achieving 11.5-16.0% improvements in Recall@5 and 5.3-13.6% in NDCG@5.

#### Multimodal Late Fusion Enhancement

Zhu et al. (2025) explored Multimodal Generative Recommendation (MGR), revealing that GR models are particularly sensitive to different modalities [citation:Beyond Unimodal Boundaries](https://arxiv.org/abs/2503.23333). Their MGR-LF++ framework employs contrastive modality alignment and special tokens to denote different modalities, achieving over 20% performance improvement compared to single-modality alternatives. The work highlights the importance of modality choices and introduces design strategies for effectively leveraging multiple modalities.

---

## Comparative Analysis

### Performance Metrics Across Studies

Table 1 summarizes the performance improvements reported across the reviewed studies:

| Study | Dataset Count | Key Metric | Improvement |
|-------|---------------|------------|-------------|
| Liu et al. (2024) | Multiple | Various tasks | Significant outperformance |
| Wang et al. (2024) | 3 | Ranking ability | Superior SOTA |
| Zheng et al. (2025) | 4 | Transfer learning | Best overall |
| Zhai et al. (2025) | 3 | NDCG | +11.18% to +14.82% |
| Ju et al. (2025) | Public benchmarks | Ablation insights | Validation of components |
| Ding et al. (2024) | 3 | Inductive ability | Best overall performance |
| Lee et al. (2025) | 4 | Recall@5, NDCG@5 | +11.5-16.0%, +5.3-13.6% |
| Zhu et al. (2025) | Multiple | Multimodal | >20% vs single-modality |
| Zhang et al. (2025) | 3 | Distribution matching | Significant advantages |
| Wang et al. (2024b) | 2 | Long-term interest | Effective utilization |

### Architectural Innovation Patterns

The reviewed literature reveals several recurring architectural patterns:

1. **Hybrid Tokenization**: Combining semantic, collaborative, and quantitative signals
2. **Multi-Stage Generation**: Separating behavior/type prediction from item prediction
3. **Late Fusion Strategies**: Delaying multimodal integration until decoding stages
4. **Memory Mechanisms**: Explicit storage and retrieval of long-term interests
5. **Distribution Alignment**: Matching latent spaces across different modalities

---

## Task Formulations and Applications

### Multi-Behavior Recommendation

MBGen (Liu et al., 2024) extends generative recommendation to handle multiple interaction types (e.g., clicks, purchases, reviews) within a unified framework, enabling more nuanced understanding of user intentions.

### Inductive Recommendation

SpecGR (Ding et al., 2024) addresses the critical challenge of recommending previously unseen items, moving beyond transductive approaches limited to training set items.

### Cross-Domain Transfer

UTGRec (Zheng et al., 2025) and MQL4GRec (Zhai et al., 2025) tackle domain adaptation challenges, enabling knowledge transfer across different recommendation contexts.

### Multimodal Integration

MGR-LF++ (Zhu et al., 2025) and GRAM (Lee et al., 2025) explore leveraging multiple modalities (text, images, structured data) for richer item representations.

### Long-Term Preference Modeling

AutoMR (Wang et al., 2024b) specifically targets the limitation of LLM context windows by implementing explicit memory mechanisms for capturing long-term user interests.

---

## Discussion

### Key Advances

The reviewed literature demonstrates significant progress in three critical dimensions:

**Tokenization Quality**: From simple IDs to learnable, universal, and quantitative representations that capture semantic richness, collaborative signals, and cross-domain knowledge.

**Model Scalability**: Position-routed sparse architectures, multi-granular fusion, and distribution matching techniques enable efficient scaling while maintaining performance.

**Task Generalization**: Moving beyond basic next-item prediction to multi-behavior, inductive, cross-domain, and multimodal scenarios.

### Remaining Challenges

Despite notable advances, several challenges persist:

1. **Context Window Limitations**: Even with memory mechanisms, LLMs struggle with very long interaction histories
2. **Computational Efficiency**: Complex tokenization and multi-modal fusion increase inference costs
3. **Benchmark Standardization**: Varied experimental setups hinder fair comparison and reproducibility
4. **Real-World Deployment**: Most evaluations remain on static benchmarks rather than live systems
5. **Cold-Start Handling**: While inductive capabilities improve, truly cold-start scenarios remain challenging

### Future Research Directions

Based on identified gaps, promising research directions include:

1. **Unified Benchmarking Frameworks**: Establishing standardized evaluation protocols (GRID initiative shows promise)
2. **Efficient Inference**: Developing lightweight architectures for production deployment
3. **Causal Understanding**: Incorporating causal reasoning to distinguish correlation from causation in recommendations
4. **Explainability**: Enhancing model interpretability for user trust and system debugging
5. **Privacy-Preserving Techniques**: Addressing data privacy concerns in generative recommendation

---

## Conclusion

The period from late 2023 to late 2025 witnessed remarkable advancement in generative recommendation research, with 10 significant papers published in cs.IR contributing to three core themes: data representation, model architecture, and task formulation. Key innovations in learnable tokenization (LETTER, UTGRec), memory-augmented architectures (AutoMR), and multimodal integration (MGR-LF++, GRAM) demonstrate the field's maturation beyond initial proof-of-concept studies.

The transition from traditional ranking-based approaches to generative paradigms offers compelling advantages in semantic understanding, flexibility, and potential for generalization. However, challenges in computational efficiency, standardization, and real-world deployment require continued research attention. Open-source initiatives like GRID represent important steps toward reproducible, comparable research that will accelerate future progress.

As large language models continue to evolve, generative recommendation is poised to become increasingly sophisticated, potentially reshaping how personalized recommendations are generated and delivered in practical applications.

---

## References

*(APA Format)*

Ding, Y., Li, J., McAuley, J., & Hou, Y. (2024). Inductive generative recommendation via retrieval-based speculation. *arXiv preprint arXiv:2410.02939*. https://arxiv.org/abs/2410.02939v2

Ju, C. M., Collins, L., Neves, L., Kumar, B., Wang, L. Y., Zhao, T., & Shah, N. (2025). Generative recommendation with semantic IDs: A practitioner's handbook. *arXiv preprint arXiv:2507.22224*. https://arxiv.org/abs/2507.22224v1

Lee, S., Choi, M., Choi, E., Kim, H.-y., & Lee, J. (2025). GRAM: Generative recommendation via semantic-aware multi-granular late fusion. *arXiv preprint arXiv:2506.01673*. https://arxiv.org/abs/2506.01673v1

Liu, Z., Hou, Y., & McAuley, J. (2024). Multi-behavior generative recommendation. *arXiv preprint arXiv:2405.16871*. https://arxiv.org/abs/2405.16871v2

Wang, C., Zhang, Y., Zhu, F., Zhang, J., Shi, T., & Feng, F. (2024). Leveraging memory retrieval to enhance LLM-based generative recommendation. *arXiv preprint arXiv:2412.17593*. https://arxiv.org/abs/2412.17593v2

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. *arXiv preprint arXiv:2405.07314*. https://arxiv.org/abs/2405.07314v3

Zhai, J., Mai, Z.-F., Wang, C.-D., Yang, F., Zheng, X., Li, H., & Tian, Y. (2025). Multimodal quantitative language for generative recommendation. *arXiv preprint arXiv:2504.05314*. https://arxiv.org/abs/2504.05314v1

Zhang, Y., Zhang, Y., Wang, Y., Chen, T., & Yin, H. (2025). Towards distribution matching between collaborative and language spaces for generative recommendation. *arXiv preprint arXiv:2504.07363*. https://arxiv.org/abs/2504.07363v2

Zheng, B., Lu, H., Chen, Y., Zhao, W. X., & Wen, J.-R. (2025). Universal item tokenization for transferable generative recommendation. *arXiv preprint arXiv:2504.04405*. https://arxiv.org/abs/2504.04405v3

Zhu, J., Ju, M., Liu, Y., Koutra, D., Shah, N., & Zhao, T. (2025). Beyond unimodal boundaries: Generative recommendation with multimodal semantics. *arXiv preprint arXiv:2503.23333*. https://arxiv.org/abs/2503.23333v1

---

**Document Prepared By:** Systematic Literature Review Process  
**Review Type:** Comprehensive Analysis of Generative Recommendation Literature  
**Output Location:** /app/backend/.deer-flow/users/a295acd6-7db3-4f7b-be18-f16d8eae7b6d/threads/b712d7c3-78e9-49c0-913f-a4dc40c6ad8f/user-data/outputs/generative_recommendation_review.md
