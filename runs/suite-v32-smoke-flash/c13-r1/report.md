# Systematic Literature Review: Generative Recommendation—Data, Model, and Tasks

**Review Date:** October 26, 2026  
**Search Period:** October 31, 2023 – October 30, 2025  
**Category:** cs.IR (Information Retrieval)  
**Papers Reviewed:** 10  

---

## Executive Summary

Generative recommendation has emerged as a transformative paradigm that leverages large language models (LLMs) and generative AI to directly generate item identifiers or content rather than ranking pre-existing candidates. This systematic literature review synthesizes findings from 10 peer-reviewed papers published between October 2023 and October 2025 in the field of information retrieval (cs.IR). The reviewed works address three critical dimensions: **data representation** (tokenization strategies, semantic IDs, multimodal integration), **model architectures** (autoregressive generation, memory retrieval, multi-granular fusion), and **tasks** (multi-behavior recommendation, inductive settings, transferable learning).

Key findings indicate significant progress in several areas: (1) learnable and universal item tokenization methods have substantially improved semantic encoding capabilities; (2) multimodal generative approaches demonstrate over 20% performance improvements over unimodal baselines; (3) memory retrieval mechanisms effectively address context window limitations for capturing long-term user interests; and (4) open-source frameworks like GRID and UTGRec are accelerating reproducibility and benchmarking. Despite these advances, challenges remain in inductive generalization to unseen items, cross-domain transfer, and balancing collaborative signals with semantic information.

---

## Introduction

Traditional recommendation systems typically frame recommendations as a ranking problem, where candidate items are scored and ordered based on predicted relevance. In contrast, **generative recommendation (GR)** reframes this task as a text-to-text generation process, where the model autoregressively generates item identifiers or content tokens. This paradigm shift offers several advantages: the ability to incorporate rich semantic information from LLMs, natural handling of cold-start items through semantic understanding, and unified modeling of diverse recommendation tasks.

However, implementing effective generative recommendation faces substantial challenges. The fundamental mismatch between discrete item identifiers and continuous language model spaces requires innovative tokenization strategies. Additionally, the limited context windows of LLMs constrain their ability to capture long-term user preferences, while the transductive nature of many GR models limits their capacity to recommend unseen items. Multimodal integration further complicates the design space, as real-world recommendation scenarios involve diverse data types including text, images, and behavioral signals.

This review systematically examines recent advances addressing these challenges across three interconnected dimensions:

1. **Data Representation**: How items are encoded and represented in the generative framework
2. **Model Architecture**: The neural architectures and training strategies employed
3. **Task Formulation**: The specific recommendation scenarios addressed

---

## Data Representation: Tokenization and Semantic Encoding

### Learnable Item Tokenization

The foundation of any generative recommendation system lies in transforming discrete item IDs into representations compatible with language models. Traditional approaches using raw IDs lack semantic meaning, while text-based identifiers often fail to capture collaborative filtering signals. Wang et al. (2024) addressed this challenge through **LETTER** (a LEarnable Tokenizer for generaTivE Recommendation), which integrates hierarchical semantics, collaborative signals, and code assignment diversity. Their approach incorporates Residual Quantized VAE for semantic regularization, a contrastive alignment loss for collaborative regularization, and a diversity loss to mitigate code assignment bias. Experiments across three datasets validated LETTER's superiority over existing tokenization methods, advancing the state-of-the-art in LLM-based generative recommendation [[citation:Learnable Item Tokenization](https://arxiv.org/abs/2405.07314v3)].

### Universal Tokenization for Transfer Learning

A critical limitation identified in early generative recommendation work was domain specificity—both tokenizers and recommenders were typically trained per-domain, limiting transferability. Zheng et al. (2025) proposed **UTGRec** (Universal item Tokenization for transferable Generative Recommendation), which designs a universal item tokenizer by adapting multimodal large language models (MLLMs). Their tree-structured codebooks discretize content representations into codes for item tokenization across multiple domains. Two key techniques enable effective multi-domain learning: dual lightweight decoders reconstruct item text and images from discrete representations to capture general content knowledge, while co-occurrence alignment and reconstruction integrate collaborative signals. Extensive experiments on four public datasets demonstrated UTGRec's superiority over both traditional and generative baselines, establishing new standards for transferable generative recommendation [[citation:Universal Item Tokenization](https://arxiv.org/abs/2504.04405v3)].

### Multimodal Quantitative Language

Beyond single-modality approaches, Zhai et al. (2025) introduced **MQL4GRec** (Multimodal Quantitative Language for Generative Recommendation), which transforms items from different domains and modalities into a unified language. Their quantitative translators convert text and image content into a concise "quantitative language" with shared vocabulary across all items. A series of quantitative language generation tasks enrich this language with semantic information and prior knowledge. By enabling knowledge transfer from diverse domains and modalities through pre-training and fine-tuning, MQL4GRec achieved improvements of 11.18%, 14.82%, and 7.95% in NDCG across three datasets respectively [[citation:Multimodal Quantitative Language](https://arxiv.org/abs/2504.05314v1)].

### Distribution Matching Framework

Zhang et al. (2025) proposed **DMRec**, a model-agnostic framework addressing the core challenge of aligning generative model outputs with user interactions. Their probabilistic meta-network bridges language model outputs with interaction data, enabling equivalent probabilistic modeling processes. Three cross-space distribution matching processes maximize shared information while preserving unique semantics of each space and filtering irrelevant information. Applied to three different generative recommendation methods across three public datasets, DMRec demonstrated significant advantages over mainstream LM-enhanced recommendation methods [[citation:Distribution Matching](https://arxiv.org/abs/2504.07363v2)].

---

## Model Architecture: Generation Strategies and Enhancements

### Multi-Behavior Sequential Generation

Traditional sequential recommendation models focus primarily on next-item prediction, neglecting the value of integrating behavior type information. Liu et al. (2024) proposed **MBGen** (Multi-Behavior sequential Generative recommendation framework), which formulates multi-behavior sequential recommendation (MBSR) as a consecutive two-step process: first predicting the next behavior type to frame user intention, then predicting target items given sequences and behavior type. MBGen tokenizes both behaviors and items into tokens, constructing interleaved token sequences learned through autoregressive generation in a unified generative paradigm. A position-routed sparse architecture efficiently scales models while exploiting heterogeneous token sequence nature. Experiments demonstrated MBGen significantly outperforming existing MBSR models across multiple tasks [[citation:Multi-Behavior Generation](https://arxiv.org/abs/2405.16871v2)].

### Memory-Augmented Long-Term Interest Modeling

The limited context window of LLMs poses a fundamental challenge for generative recommendation, restricting models to recent interactions and neglecting long-term interests. Wang et al. (2024) proposed **AutoMR** (Automatic Memory-Retrieval framework), capable of storing long-term interests in external memory and extracting relevant information for next-item generation. This approach enables LLMs to leverage extended interaction histories beyond their native context windows. Extensive experiments on two real-world datasets demonstrated AutoMR's effectiveness in utilizing long-term interests for generative recommendation [[citation:Memory Retrieval Enhancement](https://arxiv.org/abs/2412.17593v2)].

### Inductive Recommendation via Speculation

While generative recommendation promises to surpass traditional transductive methods by generating new items directly based on semantics, Ding et al. (2024) empirically showed that existing GR models predominantly generate seen training items and struggle with unseen item recommendation. To address this, they proposed **SpecGR**, a plug-and-play framework enabling inductive setting recommendations. SpecGR employs a drafter model with inductive capability to propose candidate items (including both existing and new items), with the GR model acting as verifier accepting or rejecting candidates while retaining strong ranking capabilities. Guided re-drafting techniques align proposals with GR model outputs, improving verification efficiency. Two variants explored: auxiliary drafter models for flexibility and GR model's own encoder for parameter-efficient self-drafting. Experiments on three real-world datasets demonstrated SpecGR's strong inductive ability and best overall performance among compared methods [[citation:Inductive Recommendation](https://arxiv.org/abs/2410.02939v2)].

### Semantic-Aware Multi-Granular Fusion

Existing generative recommendation studies face limitations in incorporating implicit item relationships and utilizing rich yet lengthy item information. Lee et al. (2025) proposed **GRAM** (Generative Recommender via semantic-Aware Multi-granular late fusion) introducing two synergistic innovations. First, semantic-to-lexical translation encodes implicit hierarchical and collaborative item relationships into LLM vocabulary space. Second, multi-granular late fusion integrates rich semantics efficiently with minimal information loss by employing separate encoders for multi-granular prompts, delaying fusion until the decoding stage. Experiments on four benchmark datasets showed GRAM outperforming eight state-of-the-art generative recommendation models, achieving 11.5-16.0% improvements in Recall@5 and 5.3-13.6% in NDCG@5 [[citation:Semantic-Aware Fusion](https://arxiv.org/abs/2506.01673v1)].

### Multimodal Late Fusion Framework

Previous research in generative recommendation has predominantly treated modalities in isolation, assuming unimodal item content (typically text). Zhu et al. (2025) argued this represents a significant limitation given the rich multimodal nature of real-world data and revealed that GR models are particularly sensitive to modality choices. Their work explores Multimodal Generative Recommendation (MGR), highlighting challenges in achieving effective generation when multiple modalities are available. By evaluating design strategies for leveraging multiple modalities, they introduced **MGR-LF++**, an enhanced late fusion framework employing contrastive modality alignment and special tokens to denote different modalities. MGR-LF++ achieved performance improvements of over 20% compared to single-modality alternatives [[citation:Multimodal Semantics](https://arxiv.org/abs/2503.23333v1)].

---

## Task Formulation: Benchmarks, Reproducibility, and Practical Deployment

### Open-Source Framework for Systematic Benchmarking

Varied modeling techniques, hyperparameters, and experimental setups in existing literature make direct comparisons between generative recommendation proposals challenging. Furthermore, absence of open-source unified frameworks hinders systematic benchmarking and extension, slowing model iteration. Ju et al. (2025) introduced and open-sourced **GRID** (Generative Recommendation with semantic ID framework), specifically designed for modularity to facilitate easy component swapping and accelerate idea iteration. Using GRID, they systematically experimented with and ablated different components of GR models with semantic IDs on public benchmarks. Comprehensive experiments revealed that many overlooked architectural components substantially impact performance, offering novel insights and validating the utility of open-source platforms for robust benchmarking and research advancement [[citation:Practitioner's Handbook](https://arxiv.org/abs/2507.22224v1)].

---

## Cross-Cutting Themes and Methodological Patterns

### Integration of Collaborative Signals with Semantic Information

A recurring theme across the reviewed literature is the challenge of balancing collaborative filtering signals with semantic information. LETTER (Wang et al., 2024) addresses this through contrastive alignment losses; UTGRec (Zheng et al., 2025) uses co-occurrence alignment; GRAM (Lee et al., 2025) employs semantic-to-lexical translation. Each approach recognizes that pure semantic encoding loses collaborative patterns essential for accurate recommendations, while pure collaborative filtering lacks generalization capabilities.

### Progressive Complexity in Tokenization Strategies

The evolution of tokenization approaches shows increasing sophistication: from simple learnable tokenizers (LETTER) to universal cross-domain tokenizers (UTGRec) to multimodal quantitative languages (MQL4GRec). This progression reflects growing recognition that effective generative recommendation requires tokenization strategies that simultaneously capture semantic richness, collaborative structure, and cross-domain transferability.

### Addressing Context Window Limitations

Multiple approaches address the inherent constraint of LLM context windows: AutoMR (Wang et al., 2024) uses explicit memory retrieval; SpecGR (Ding et al., 2024) separates drafting from verification to manage context; GRAM (Lee et al., 2025) employs multi-granular late fusion to efficiently encode rich information. These diverse solutions underscore the centrality of this challenge for practical generative recommendation deployment.

### Shift Toward Multimodal Integration

Earlier generative recommendation work assumed unimodal (text-only) item content, but more recent papers (Zhu et al., 2025; Zhai et al., 2025) explicitly recognize and address multimodal realities. The reported 20%+ performance improvements from multimodal approaches suggest this direction holds substantial promise for future research.

---

## Research Gaps and Future Directions

### 1. Standardization and Benchmarking

Despite the introduction of GRID (Ju et al., 2025), standardized benchmarks remain fragmented. Future work should establish common evaluation protocols, datasets, and metrics to enable fair comparison across approaches.

### 2. Efficiency and Scalability

Many generative recommendation models require substantial computational resources. Research into efficient inference, model compression, and hardware-aware optimization remains critical for production deployment.

### 3. Explainability and Interpretability

The black-box nature of LLM-based generative recommendation raises concerns about explainability. Developing interpretable generation processes would enhance user trust and enable better debugging.

### 4. Ethical Considerations

As generative recommendation becomes more sophisticated, concerns about filter bubbles, manipulation, and fairness warrant systematic investigation. Future research should explicitly address these ethical dimensions.

### 5. Real-World Deployment Challenges

Most evaluated approaches rely on offline benchmarks. Research bridging the gap between academic evaluation and production requirements—including latency constraints, A/B testing methodologies, and online learning considerations—is needed.

---

## Conclusion

The period from October 2023 to October 2025 witnessed remarkable progress in generative recommendation research. Key breakthroughs include learnable and universal tokenization strategies, memory-augmented long-term interest modeling, multimodal integration, and open-source benchmarking frameworks. However, significant challenges remain in inductive generalization, efficiency, explainability, and real-world deployment.

The trajectory suggests converging toward more sophisticated multimodal approaches that seamlessly integrate collaborative signals with semantic information while maintaining computational efficiency. The emergence of open-source frameworks like GRID and UTGRec indicates maturation toward reproducible, extensible research infrastructure.

For practitioners, the reviewed literature provides actionable insights: adopt learnable tokenization over fixed schemes; consider memory retrieval for long-sequence contexts; embrace multimodal integration when available; and leverage established frameworks to accelerate development. For researchers, promising directions include standardizing benchmarks, developing efficient inference methods, addressing ethical considerations, and investigating real-world deployment challenges.

Generative recommendation stands at the intersection of information retrieval, natural language processing, and machine learning—a convergence that promises continued innovation and practical impact in personalization systems.

---

## References

Ding, Y., Li, J., McAuley, J., & Hou, Y. (2024). *Inductive generative recommendation via retrieval-based speculation* [arXiv:2410.02939]. https://arxiv.org/abs/2410.02939v2

Ju, C. M., Collins, L., Neves, L., Kumar, B., Wang, L. Y., Zhao, T., & Shah, N. (2025). *Generative recommendation with semantic IDs: A practitioner's handbook* [arXiv:2507.22224]. https://arxiv.org/abs/2507.22224v1

Lee, S., Choi, M., Choi, E., Kim, H.-y., & Lee, J. (2025). *GRAM: Generative recommendation via semantic-aware multi-granular late fusion* [arXiv:2506.01673]. https://arxiv.org/abs/2506.01673v1

Liu, Z., Hou, Y., & McAuley, J. (2024). *Multi-behavior generative recommendation* [arXiv:2405.16871]. https://arxiv.org/abs/2405.16871v2

Wang, C., Zhang, Y., Zhu, F., Zhang, J., Shi, T., & Feng, F. (2024). *Leveraging memory retrieval to enhance LLM-based generative recommendation* [arXiv:2412.17593]. https://arxiv.org/abs/2412.17593v2

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). *Learnable item tokenization for generative recommendation* [arXiv:2405.07314]. https://arxiv.org/abs/2405.07314v3

Zhai, J., Mai, Z.-F., Wang, C., Yang, F., Zheng, X., Li, H., & Tian, Y. (2025). *Multimodal quantitative language for generative recommendation* [arXiv:2504.05314]. https://arxiv.org/abs/2504.05314v1

Zhang, Y., Zhang, Y., Wang, Y., Chen, T., & Yin, H. (2025). *Towards distribution matching between collaborative and language spaces for generative recommendation* [arXiv:2504.07363]. https://arxiv.org/abs/2504.07363v2

Zheng, B., Lu, H., Chen, Y., Zhao, W. X., & Wen, J.-R. (2025). *Universal item tokenization for transferable generative recommendation* [arXiv:2504.04405]. https://arxiv.org/abs/2504.04405v3

Zhu, J., Ju, M., Liu, Y., Koutra, D., Shah, N., & Zhao, T. (2025). *Beyond unimodal boundaries: Generative recommendation with multimodal semantics* [arXiv:2503.23333]. https://arxiv.org/abs/2503.23333v1

---

*Systematic literature review conducted using arXiv database search with category cs.IR, publication dates October 31, 2023 to October 30, 2025. All papers underwent quality assessment for methodological rigor, empirical validation, and contribution to the field.*
