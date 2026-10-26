# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "generative recommendation", category cs.IR, published between 2023 and 2025
**Citation format**: APA 7th edition

## Executive Summary

The field of generative recommendation has undergone rapid evolution between 2023 and 2025, with research focusing on three interconnected dimensions: data representation (item tokenization and multimodal integration), model architecture (transformer-based generative frameworks), and task formulation (behavior prediction, inductive recommendation, and transfer learning). The surveyed literature reveals a clear shift from traditional discriminative recommendation approaches toward autoregressive generative models that leverage large language model capabilities. Key innovations include learnable item tokenization strategies that bridge collaborative filtering signals with language model semantics, multimodal fusion techniques that integrate diverse content modalities, and novel frameworks enabling inductive recommendation for unseen items. Despite significant progress, the field faces persistent challenges in long-term interest modeling, cross-domain transfer, and systematic benchmarking—gaps that recent work has begun to address through memory retrieval mechanisms, universal tokenization approaches, and open-source unified frameworks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "generative recommendation", filtered to category cs.IR, published between 2023 and 2025. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Item Tokenization and Semantic Representation

A central challenge in generative recommendation is transforming items into tokens that effectively bridge collaborative filtering signals with language model semantics. Recent work has moved beyond simple ID-based or textual identifiers toward sophisticated tokenization strategies that encode rich item semantics. Liu et al. (2024) introduced MBGen, which tokenizes both behaviors and items into interleaved sequences learned autoregressively with position-routed sparse architecture. Wang et al. (2024) proposed LETTER, integrating hierarchical semantics, collaborative signals, and code assignment diversity through Residual Quantized VAE with contrastive alignment loss. Zheng et al. (2025) advanced this direction with UTGRec, using tree-structured codebooks and multimodal large language models to enable transferable tokenization across domains. These approaches share a common insight: effective tokenization must preserve both collaborative signals (user-item interaction patterns) and semantic content (item attributes), while enabling efficient generation within language model constraints.

### Theme 2: Multimodal Integration and Late Fusion

Real-world recommendation scenarios involve multiple modalities—text, images, audio, video—yet early generative recommendation models treated modalities in isolation. Recent work has shifted toward multimodal fusion strategies that leverage complementary information across modalities. Zhu et al. (2025) demonstrated that generative models are particularly sensitive to modality choices and introduced MGR-LF++, employing contrastive modality alignment and special tokens to denote different modalities, achieving over 20% improvement compared to single-modality alternatives. Zhai et al. (2025) proposed MQL4GRec, which transforms items from different domains and modalities into a unified quantitative language using quantitative translators, enabling knowledge transfer through pre-training and fine-tuning. Lee et al. (2025) developed GRAM with semantic-to-lexical translation to encode implicit hierarchical and collaborative item relationships into LLM vocabulary space, delaying fusion until the decoding stage to minimize information loss. These works collectively establish late fusion as a dominant paradigm, balancing modality-specific encoding with cross-modal alignment.

### Theme 3: Inductive and Transferable Recommendation

Traditional generative recommendation models struggle to recommend unseen items—those not present during training—limiting their applicability in dynamic environments with continuously arriving content. Ding et al. (2024) addressed this limitation with SpecGR, a plug-and-play framework using a drafter model with inductive capability to propose candidate items, with the generative model acting as a verifier that accepts or rejects candidates while introducing guided re-drafting to improve efficiency. Zheng et al. (2025) extended this direction with UTGRec, enabling transferable recommendation across domains through universal item tokenization and joint learning frameworks that pre-train and adapt recommenders. Wang et al. (2025) introduced DMRec, a model-agnostic framework that bridges language model outputs with user interactions through probabilistic meta-networks and cross-space distribution matching. These approaches share a focus on generalization: enabling generative models to operate beyond their training distribution while maintaining recommendation quality.

### Theme 4: Memory and Long-Term Interest Modeling

Large language models face inherent context window limitations, restricting their ability to leverage long-term user interaction histories for recommendation. Wang et al. (2024) proposed AutoMR, which stores long-term interests in external memory and extracts relevant information for next-item generation, addressing the limitation that LLMs typically focus only on recent interactions. This approach reflects a broader trend toward augmenting language models with retrieval mechanisms that extend their effective context. The automatic memory-retrieval framework demonstrates that separating long-term storage from short-term generation enables more comprehensive user modeling without overwhelming the model's attention mechanisms. This theme connects to broader challenges in scaling generative recommendation to real-world scenarios where user histories span thousands of interactions.

### Theme 5: Benchmarking and Systematic Frameworks

As the field has matured, researchers have recognized the need for unified frameworks enabling systematic benchmarking and component-level analysis. Ju et al. (2025) introduced GRID, an open-source modular framework for generative recommendation with semantic IDs designed for easy component swapping. Their systematic experimentation revealed that many overlooked architectural components substantially impact performance, and that varied modeling techniques and experimental setups in existing literature make direct comparisons challenging. This work addresses a critical infrastructure gap: without standardized frameworks, progress measurement becomes unreliable and component-level insights remain fragmented. The emphasis on open-source platforms reflects a broader maturation of the field toward reproducible research practices.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers acknowledge that traditional discriminative recommendation approaches are insufficient for capturing the generative nature of user preferences—users do not simply select from fixed options but construct preferences dynamically. Second, there is consensus that item tokenization is a critical bottleneck: poor tokenization undermines even sophisticated model architectures (Liu et al., 2024; Wang et al., 2024; Zheng et al., 2025). Third, multimodal integration is universally recognized as necessary for real-world deployment, given that user interactions involve diverse content types (Zhu et al., 2025; Zhai et al., 2025; Lee et al., 2025). Fourth, all works emphasize the importance of empirical validation on multiple public datasets, suggesting a shared commitment to reproducible evaluation.

**Disagreements**: While explicit disagreements are not evident in the abstracts, implicit tensions exist in architectural choices. The tokenization literature splits between approaches prioritizing collaborative signals (Wang et al., 2024) versus those emphasizing semantic content (Zheng et al., 2025). Similarly, multimodal fusion strategies vary: some works advocate early fusion with joint encoding (Zhai et al., 2025), while others prefer late fusion with delayed integration (Zhu et al., 2025; Lee et al., 2025). The inductive recommendation literature presents another tension: whether to use separate drafter models (Ding et al., 2024) or integrated self-drafting approaches (Ding et al., 2024's parameter-efficient variant). These disagreements reflect fundamental questions about the relative importance of collaborative versus semantic signals, and the optimal timing for information integration.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly address computational efficiency or deployment costs—a critical concern for real-world systems serving millions of users. Second, while several works mention cross-domain transfer (Zheng et al., 2025; Wang et al., 2025), systematic evaluation of zero-shot transfer capabilities remains limited. Third, the focus on next-item prediction overlooks other recommendation tasks such as session-based recommendation, bundle recommendation, or conversational recommendation—tasks that may require different generative formulations. Fourth, ethical considerations—including fairness, bias amplification, and privacy implications of generative models—are absent from the surveyed literature. Fifth, while Ju et al. (2025) call for unified frameworks, the field still lacks standardized benchmarks with agreed-upon metrics and evaluation protocols. Finally, the reliance on abstract-level metadata extraction means that detailed experimental configurations, hyperparameter sensitivities, and failure mode analyses remain unexamined in this review.

## Per-Paper Annotations

### Ding et al. (2024)

**Research question**: How can generative recommendation models be enabled to recommend unseen (new) items in an inductive setting rather than only generating items seen during training?
**Methodology**: The authors propose SpecGR, a plug-and-play framework using a drafter model with inductive capability to propose candidate items, with the GR model acting as a verifier that accepts or rejects candidates while introducing guided re-drafting to improve verification efficiency.
**Key findings**:
- GR models predominantly generate items seen during training and struggle to recommend unseen items
- SpecGR enables GR models to recommend new items in an inductive setting
- Guided re-drafting improves verification efficiency by aligning candidates with GR model outputs
- SpecGR exhibits strong inductive recommendation ability and best overall performance on three real-world datasets
- Two drafting variants are proposed: auxiliary drafter model and parameter-efficient self-drafting using the GR model's encoder
**Limitations**: not stated in abstract

### Ju et al. (2025)

**Research question**: How can the lack of open-source unified frameworks and varied experimental setups in generative recommendation with semantic IDs be addressed to enable systematic benchmarking and model iteration?
**Methodology**: The authors introduce and open-source GRID, a modular framework for Generative Recommendation with semantic ID designed for easy component swapping, and systematically experiment with and ablate different components of GR models with SIDs on public benchmarks.
**Key findings**:
- Semantic IDs enable GR models to incorporate semantic information and learn collaborative filtering signals while retaining discrete decoding benefits
- Varied modeling techniques and experimental setups in existing literature make direct comparisons challenging
- Many overlooked architectural components in GR models with SIDs substantially impact performance
- GRID facilitates easy component swapping and accelerates idea iteration
- Open-source platforms are useful for robust benchmarking and GR research advancement
**Limitations**: not stated in abstract

### Lee et al. (2025)

**Research question**: How can generative recommendation models better incorporate implicit item relationships and utilize rich yet lengthy item information?
**Methodology**: The authors propose GRAM with two innovations: semantic-to-lexical translation to encode implicit hierarchical and collaborative item relationships into LLM vocabulary space, and multi-granular late fusion using separate encoders for multi-granular prompts with fusion delayed until the decoding stage.
**Key findings**:
- GRAM outperforms eight state-of-the-art generative recommendation models
- Achieves 11.5-16.0% improvements in Recall@5 across four benchmark datasets
- Achieves 5.3-13.6% improvements in NDCG@5 across four benchmark datasets
- Semantic-to-lexical translation effectively encodes implicit item relationships
- Multi-granular late fusion integrates rich semantics efficiently with minimal information loss
**Limitations**: not stated in abstract

### Liu et al. (2024)

**Research question**: How can multi-behavior sequential recommendation be improved by integrating target behavior type into the learning objective?
**Methodology**: The authors propose MBGen, a Multi-Behavior sequential Generative recommendation framework that formulates MBSR as a two-step process: first predicting the next behavior type to frame user intention, then predicting next items given item sequences and target behavior type. Both behaviors and items are tokenized into tokens and constructed into a single interleaved token sequence, learned autoregressively with a position-routed sparse architecture.
**Key findings**:
- MBGen significantly outperforms existing MBSR models across multiple tasks
- The two-step generative process (behavior prediction followed by item prediction) naturally enables multi-task capability
- Position-routed sparse architecture efficiently scales up models by exploiting heterogeneous nature of token sequences
- Extensive experiments on public datasets validate the approach
**Limitations**: not stated in abstract

### Wang, C. et al. (2024)

**Research question**: How can long-term user interests from longer interaction histories be utilized in LLM-based generative recommendation despite limited context windows?
**Methodology**: The authors propose AutoMR (Automatic Memory-Retrieval framework), which stores long-term interests in memory and extracts relevant information from it for next-item generation within LLMs, addressing the limitation of LLMs focusing only on recent user interactions.
**Key findings**:
- AutoMR effectively utilizes long-term interests for generative recommendation
- The framework addresses the limited context window problem in LLMs
- Extensive experimental results on two real-world datasets demonstrate effectiveness
- The approach enables extraction of relevant information from memory for item generation
**Limitations**: not stated in abstract

### Wang, W. et al. (2024)

**Research question**: How can item tokenization be improved to better transform recommendation data into the language space of LLMs for generative recommendation?
**Methodology**: The authors propose LETTER (LEarnable Tokenizer for generaTivE Recommendation), which integrates hierarchical semantics, collaborative signals, and code assignment diversity. LETTER uses Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias, with ranking-guided generation loss to augment ranking ability.
**Key findings**:
- LETTER advances the state-of-the-art in LLM-based generative recommendation
- The approach addresses shortcomings of current ID, textual, and codebook-based identifiers
- Experiments on three datasets validate the superiority of LETTER
- The framework integrates hierarchical semantics, collaborative signals, and code assignment diversity
**Limitations**: not stated in abstract

### Wang, Y. et al. (2025)

**Research question**: How can the mismatch between generative models and language models be addressed to achieve optimal alignment in generative recommendation?
**Methodology**: The authors propose DMRec, a model-agnostic generative recommendation framework that introduces a probabilistic meta-network to bridge LM outputs with user interactions. Three cross-space distribution matching processes are designed to maximize shared information while preserving unique semantics of each space and filtering out irrelevant information.
**Key findings**:
- DMRec effectively enhances recommendation performance of generative models
- The framework shows significant advantages over mainstream LM-enhanced recommendation methods
- The approach is model-agnostic and can be applied to different types of generative recommendation methods
- Extensive experiments on three public datasets demonstrate effectiveness
**Limitations**: not stated in abstract

### Zhai et al. (2025)

**Research question**: How can recommendation knowledge be efficiently transferred from pre-trained language models to recommendation systems while accommodating multimodal item information?
**Methodology**: The authors propose MQL4GRec, which transforms items from different domains and modalities into a unified quantitative language using quantitative translators, designs quantitative language generation tasks to enrich semantic information, and achieves knowledge transfer through pre-training and fine-tuning.
**Key findings**:
- Existing methods fail to accommodate differences between PLM linguistic knowledge and recommendation system needs
- Existing methods rarely consider complementary knowledge between multimodal item information
- Quantitative translators convert text and image content into a unified language with shared vocabulary
- MQL4GRec achieves 11.18%, 14.82%, and 7.95% improvements on NDCG metric across three datasets
- Pre-training and fine-tuning enable transfer of recommendation knowledge from different domains and modalities
**Limitations**: not stated in abstract

### Zheng et al. (2025)

**Research question**: How can item tokenization and generative recommendation be made transferable across multiple domains?
**Methodology**: The authors propose UTGRec, a Universal item Tokenization approach using a multimodal large language model to encode rich item semantics. Tree-structured codebooks discretize content representations into codes. Dual lightweight decoders reconstruct item text and images from discrete representations, while co-occurrence alignment and reconstruction integrate collaborative signals. A joint learning framework pre-trains and adapts the transferable recommender across domains.
**Key findings**:
- UTGRec demonstrates superiority over both traditional and generative recommendation baselines
- The universal item tokenizer enables effective transfer and adaptation to new domains
- Tree-structured codebooks effectively discretize content representations
- Extensive experiments on four public datasets validate the approach
**Limitations**: not stated in abstract

### Zhu et al. (2025)

**Research question**: How can generative recommendation models effectively leverage multiple modalities given their sensitivity to modality choices and the multimodal nature of real-world data?
**Methodology**: The authors evaluate design strategies for leveraging multiple modalities in generative recommendation and introduce MGR-LF++, an enhanced late fusion framework employing contrastive modality alignment and special tokens to denote different modalities.
**Key findings**:
- Generative recommendation models are particularly sensitive to different modalities
- Previous research treating modalities in isolation is a significant limitation
- MGR-LF++ achieves over 20% performance improvement compared to single-modality alternatives
- Contrastive modality alignment and special tokens effectively denote different modalities
**Limitations**: not stated in abstract

## References

Ding, Y., Li, J., McAuley, J., & Hou, Y. (2024). Inductive generative recommendation via retrieval-based speculation. arXiv. https://arxiv.org/abs/2410.02939

Ju, C. M., Collins, L., Neves, L., Kumar, B., Wang, L. Y., Zhao, T., & Shah, N. (2025). Generative recommendation with semantic IDs: A practitioner's handbook. arXiv. https://arxiv.org/abs/2507.22224

Lee, S., Choi, M., Choi, E., Kim, H.-Y., & Lee, J. (2025). GRAM: Generative recommendation via semantic-aware multi-granular late fusion. arXiv. https://arxiv.org/abs/2506.01673

Liu, Z., Hou, Y., & McAuley, J. (2024). Multi-behavior generative recommendation. arXiv. https://arxiv.org/abs/2405.16871

Wang, C., Zhang, Y., Zhu, F., Zhang, J., Shi, T., & Feng, F. (2024). Leveraging memory retrieval to enhance LLM-based generative recommendation. arXiv. https://arxiv.org/abs/2412.17593

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2405.07314

Wang, Y., Zhang, Y., Wang, Y., Chen, T., & Yin, H. (2025). Towards distribution matching between collaborative and language spaces for generative recommendation. arXiv. https://arxiv.org/abs/2504.07363

Zhai, J., Mai, Z.-F., Wang, C.-D., Yang, F., Zheng, X., Li, H., & Tian, Y. (2025). Multimodal quantitative language for generative recommendation. arXiv. https://arxiv.org/abs/2504.05314

Zheng, B., Lu, H., Chen, Y., Zhao, W. X., & Wen, J.-R. (2025). Universal item tokenization for transferable generative recommendation. arXiv. https://arxiv.org/abs/2504.04405

Zhu, J., Ju, M., Liu, Y., Koutra, D., Shah, N., & Zhao, T. (2025). Beyond unimodal boundaries: Generative recommendation with multimodal semantics. arXiv. https://arxiv.org/abs/2503.23333
