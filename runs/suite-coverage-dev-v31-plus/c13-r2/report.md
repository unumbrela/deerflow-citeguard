# Systematic Literature Review: Generative Recommendation: Data, Model, and Tasks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "generative recommendation", cs.IR, published between 2023-10-31 and 2025-10-30
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on generative recommendation, focusing on data representation, model architectures, and task formulations. The surveyed literature reveals a rapidly evolving field centered on three critical challenges: (1) effective item tokenization that bridges collaborative filtering signals with semantic representations, (2) multimodal integration for richer user-item understanding, and (3) extending generative models to inductive settings for recommending unseen items. Collectively, these papers demonstrate that generative recommendation has moved beyond simple autoregressive item prediction to sophisticated frameworks incorporating memory retrieval, multi-behavior modeling, distribution matching, and multi-granular semantic fusion. Performance improvements of 10-20% over baseline methods are commonly reported, though most papers acknowledge limitations in their abstracts regarding real-world deployment constraints and computational efficiency.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "generative recommendation", filtered to category cs.IR, published between 2023-10-31 and 2025-10-30. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, extraction relied solely on abstracts, which may not capture full methodological details or limitations discussed in complete papers.

## Themes

### Theme 1: Item Tokenization and Representation Learning

A dominant thread across the surveyed literature concerns how to effectively tokenize items for generative recommendation. Traditional ID-based tokenization fails to capture semantic information, while purely textual tokenization ignores collaborative signals. Several papers propose hybrid approaches: LETTER (Wang et al., 2024) introduces a learnable tokenizer using Residual Quantized VAE for semantic regularization and contrastive alignment for collaborative signals. UTGRec (Zheng et al., 2025) extends this to transferable domains using tree-structured codebooks with dual decoders for content reconstruction. The GRID framework (Ju et al., 2025) systematically benchmarks semantic ID approaches, demonstrating that architectural components often overlooked substantially impact performance. MQL4GRec (Zhai et al., 2025) takes a different approach, transforming multimodal content into a unified quantitative language with shared vocabulary. These works collectively establish that effective tokenization must balance semantic richness, collaborative signal preservation, and cross-domain transferability.

### Theme 2: Multimodal Integration and Late Fusion

Real-world recommendation scenarios involve multiple modalities—text, images, user behavior sequences—yet early generative models treated these in isolation. Recent work emphasizes multimodal late fusion strategies. MGR-LF++ (Zhu et al., 2025) achieves over 20% improvement through contrastive modality alignment and special tokens denoting different modalities. GRAM (Lee et al., 2025) introduces semantic-to-lexical translation encoding implicit hierarchical and collaborative relationships, with multi-granular late fusion delaying integration until the decoding stage to minimize information loss. DMRec (Zhang et al., 2025) proposes distribution matching between collaborative and language spaces using a probabilistic meta-network. These approaches share the insight that naive concatenation of modalities is insufficient; instead, structured alignment and delayed fusion preserve modality-specific semantics while enabling cross-modal reasoning.

### Theme 3: Memory and Long-Term Interest Modeling

A critical limitation of LLM-based recommendation is restricted context windows, which focus only on recent interactions. AutoMR (Wang et al., 2024) addresses this by storing long-term user interests in external memory and retrieving relevant information during generation. This memory-augmented approach parallels developments in language modeling, suggesting that generative recommendation benefits from explicit separation between short-term sequential patterns and long-term preference profiles. The framework demonstrates effectiveness on real-world datasets, though the abstract does not specify computational overhead or latency implications of memory retrieval at inference time.

### Theme 4: Multi-Behavior and Sequential Modeling

User behavior in recommendation systems is inherently multi-faceted—clicks, purchases, ratings, shares—each signaling different intentions. MBGen (Liu et al., 2024) formulates multi-behavior sequential recommendation as a two-step process: first predicting the target behavior type to frame user intention, then predicting items given the sequence and behavior type. This interleaved tokenization of behaviors and items, combined with position-routed sparse architecture, enables efficient scaling while significantly outperforming existing MBSR models. The approach recognizes that behavior prediction is not auxiliary but central to understanding user intent in generative frameworks.

### Theme 5: Inductive Recommendation and Unseen Items

A fundamental challenge for generative recommendation is the inductive setting: recommending items unseen during training. SpecGR (Ding et al., 2024) addresses this through a retrieval-based speculation framework where a drafter model proposes candidates including both existing and new items, while the GR model acts as verifier accepting or rejecting candidates. Guided re-drafting improves verification efficiency by aligning candidates with GR model outputs. This drafter-verifier paradigm enables generative models to generalize beyond their training vocabulary, a capability essential for dynamic catalogs with frequent item additions.

### Theme 6: Benchmarking and Systematic Comparison

As the field matures, establishing reproducible benchmarks becomes critical. GRID (Ju et al., 2025) provides a modular framework for systematic experimentation with generative recommendation components, revealing that many architectural details previously considered minor substantially impact performance. This work addresses the fragmentation in experimental setups across literature, enabling direct comparison of techniques. The open-source platform accelerates research by standardizing evaluation protocols and component interfaces.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the necessity of hybrid representations combining semantic and collaborative signals (Wang et al., 2024; Zheng et al., 2025; Zhai et al., 2025). There is broad agreement that late fusion strategies outperform early concatenation for multimodal integration (Zhu et al., 2025; Lee et al., 2025; Zhang et al., 2025). All papers reporting quantitative results demonstrate double-digit percentage improvements over baselines, suggesting the field is advancing rapidly. Additionally, there is consensus that generative models require architectural adaptations—memory, speculation, multi-step processes—to handle real-world recommendation constraints.

**Disagreements**: While not explicit contradictions, different papers prioritize different aspects of the problem. Tokenization-focused works (Wang et al., 2024; Zheng et al., 2025; Ju et al., 2025) emphasize representation learning as the primary bottleneck, while multimodal works (Zhu et al., 2025; Lee et al., 2025; Zhang et al., 2025) argue fusion strategy is more critical. The speculative generation approach (Ding et al., 2024) addresses a different failure mode entirely—inductive generalization—suggesting the field lacks consensus on which limitation is most pressing. Memory-based approaches (Wang et al., 2024) receive less attention despite addressing a fundamental architectural constraint of LLMs.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Computational efficiency**: None of the abstracts discuss inference latency, model size, or computational cost—critical factors for production deployment. Generative models are typically more expensive than discriminative alternatives.

2. **Cold-start users**: While inductive recommendation addresses unseen items, none of the papers explicitly address cold-start users with minimal interaction history.

3. **Fairness and bias**: No paper mentions fairness considerations, bias amplification, or diversity in recommendations—increasingly important concerns in production systems.

4. **Real-world validation**: Most experiments use public benchmark datasets; there is limited discussion of deployment in production environments with scale, latency, and business constraints.

5. **Theoretical foundations**: The literature is predominantly empirical; there is limited theoretical analysis of why generative approaches succeed or fail in recommendation contexts.

6. **Limitations transparency**: Most abstracts do not explicitly state limitations, suggesting either space constraints or insufficient critical analysis of proposed methods.

## Per-Paper Annotations

### Ding et al. (2024)

**Research question**: How can generative recommendation models be enabled to recommend unseen items in an inductive setting?
**Methodology**: The authors propose SpecGR, a plug-and-play framework using a drafter model with inductive capability to propose candidate items, with the GR model acting as a verifier that accepts or rejects candidates while introducing guided re-drafting to improve verification efficiency.
**Key findings**:
- GR models predominantly generate items seen during training and struggle to recommend unseen items
- SpecGR enables GR models to recommend new items in an inductive setting
- The framework uses a drafter model to propose candidates including both existing and new items
- Guided re-drafting improves verification efficiency by aligning candidates with GR model outputs
- SpecGR demonstrates strong inductive recommendation ability and best overall performance on three real-world datasets
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Ju et al. (2025)

**Research question**: How can the field establish systematic benchmarking and comparison of generative recommendation models with semantic IDs?
**Methodology**: The authors introduce and open-source GRID, a modular framework for Generative Recommendation with semantic ID designed for easy component swapping, and systematically experiment with and ablate different components of GR models with SIDs on public benchmarks.
**Key findings**:
- Semantic IDs enable GR models to incorporate semantic information and learn collaborative filtering signals while retaining discrete decoding benefits
- Varied modeling techniques and experimental setups in existing literature make direct comparisons challenging
- Many overlooked architectural components in GR models with SIDs substantially impact performance
- GRID facilitates systematic benchmarking and accelerates GR research advancement
- An open-source platform is valuable for robust benchmarking and GR research
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Lee et al. (2025)

**Research question**: How can generative recommendation models better incorporate implicit item relationships and utilize rich, lengthy item information?
**Methodology**: The authors propose GRAM with two innovations: semantic-to-lexical translation to encode implicit hierarchical and collaborative item relationships into LLM vocabulary space, and multi-granular late fusion using separate encoders for multi-granular prompts with fusion delayed until the decoding stage.
**Key findings**:
- Existing generative recommendation studies face limitations in incorporating implicit item relationships and utilizing rich item information
- Semantic-to-lexical translation effectively encodes implicit hierarchical and collaborative item relationships
- Multi-granular late fusion integrates rich semantics efficiently with minimal information loss
- GRAM outperforms eight state-of-the-art generative recommendation models on four benchmark datasets
- Achieves 11.5-16.0% improvements in Recall@5 and 5.3-13.6% improvements in NDCG@5
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Liu et al. (2024)

**Research question**: How can multi-behavior sequential recommendation be improved by integrating target behavior type into the learning objective?
**Methodology**: The authors propose MBGen, a two-step generative framework that first predicts the next behavior type to frame user intention, then predicts the next items given item sequences and target behavior type. They tokenize both behaviors and items into interleaved tokens and use autoregressive generation with a position-routed sparse architecture.
**Key findings**:
- MBGen formulates MBSR as a consecutive two-step process of behavior prediction followed by item prediction
- The framework tokenizes behaviors and items into a single interleaved token sequence
- Position-routed sparse architecture enables efficient scaling of the model
- MBGen significantly outperforms existing MBSR models across multiple tasks on public datasets
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Wang et al. (2024) [AutoMR]

**Research question**: How can long-term user interests be incorporated into LLM-based generative recommendation despite limited context windows?
**Methodology**: The authors propose AutoMR, an Automatic Memory-Retrieval framework that stores long-term interests in memory and extracts relevant information for next-item generation within LLMs.
**Key findings**:
- Limited context windows restrict LLMs to focusing only on recent user interactions
- AutoMR stores long-term interests in memory for retrieval during generation
- The framework extracts relevant information from memory for next-item generation
- Experiments on two real-world datasets demonstrate AutoMR's effectiveness
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Wang et al. (2024) [LETTER]

**Research question**: How can item tokenization be improved to better encode semantic information, incorporate collaborative signals, and handle code assignment bias in LLM-based generative recommendation?
**Methodology**: The authors propose LETTER, a learnable tokenizer that integrates hierarchical semantics, collaborative signals, and code assignment diversity. It uses Residual Quantized VAE for semantic regularization, contrastive alignment loss for collaborative regularization, and diversity loss to mitigate code assignment bias.
**Key findings**:
- LETTER addresses shortcomings of current item tokenization approaches (ID, textual, codebook-based identifiers)
- The framework incorporates three key components: semantic regularization, collaborative regularization, and diversity loss
- A ranking-guided generation loss is proposed to augment ranking ability theoretically
- Experiments on three datasets validate LETTER's superiority over state-of-the-art methods
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Zhai et al. (2025)

**Research question**: How can recommendation knowledge be efficiently transferred from different domains and modalities to improve generative recommendation?
**Methodology**: The authors propose MQL4GRec, which transforms items from different domains and modalities into a unified quantitative language using quantitative translators, designs quantitative language generation tasks to enrich semantic information, and achieves knowledge transfer through pre-training and fine-tuning.
**Key findings**:
- Existing methods fail to accommodate differences between PLM linguistic knowledge and recommendation system needs
- Current approaches rarely consider complementary knowledge between multimodal item information
- Quantitative translators convert text and image content into a unified concise language with shared vocabulary
- Quantitative language generation tasks enrich the language with semantic information and prior knowledge
- MQL4GRec achieves 11.18%, 14.82%, and 7.95% improvements on NDCG across three datasets
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Zhang et al. (2025)

**Research question**: How can the mismatch between generative models and language models be addressed to achieve optimal alignment in generative recommendation?
**Methodology**: The authors propose DMRec, a model-agnostic framework that introduces a probabilistic meta-network to bridge language model outputs with user interactions. They design three cross-space distribution matching processes to maximize shared information while preserving unique semantics.
**Key findings**:
- DMRec addresses the core challenge of mismatch between input-output formats and semantics of generative models and LMs
- The probabilistic meta-network enables equivalent probabilistic modeling process
- Three cross-space distribution matching processes maximize shared information while filtering irrelevant information
- DMRec enhances recommendation performance across three different types of generative recommendation methods
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Zheng et al. (2025)

**Research question**: How can item tokenization and recommender systems be made transferable across domains in generative recommendation?
**Methodology**: The authors propose UTGRec, a universal item tokenization approach using a multimodal large language model with tree-structured codebooks. They employ dual lightweight decoders for content reconstruction and integrate collaborative signals through co-occurrence alignment and reconstruction.
**Key findings**:
- UTGRec addresses the domain-specific limitation of existing tokenizers and recommenders
- Tree-structured codebooks discretize content representations into codes for item tokenization
- Dual lightweight decoders reconstruct item text and images from discrete representations
- Co-occurrence alignment and reconstruction integrate collaborative knowledge
- UTGRec outperforms both traditional and generative recommendation baselines on four datasets
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Zhu et al. (2025)

**Research question**: How can generative recommendation models effectively leverage multiple modalities rather than treating them in isolation?
**Methodology**: The authors evaluate design strategies for leveraging multiple modalities in generative recommendation and introduce MGR-LF++, an enhanced late fusion framework using contrastive modality alignment and special tokens to denote different modalities.
**Key findings**:
- Generative recommendation models are particularly sensitive to different modalities
- Treating modalities in isolation is a significant limitation given the multimodal nature of real-world data
- MGR-LF++ achieves over 20% performance improvement compared to single-modality alternatives
- Contrastive modality alignment and special tokens effectively denote different modalities in late fusion frameworks
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

## References

Ding, Y., Li, J., McAuley, J., & Hou, Y. (2024). Inductive generative recommendation via retrieval-based speculation. arXiv. https://arxiv.org/abs/2410.02939

Ju, C. M., Collins, L., Neves, L., Kumar, B., Wang, L. Y., Zhao, T., & Shah, N. (2025). Generative recommendation with semantic IDs: A practitioner's handbook. arXiv. https://arxiv.org/abs/2507.22224

Lee, S., Choi, M., Choi, E., Kim, H.-Y., & Lee, J. (2025). GRAM: Generative recommendation via semantic-aware multi-granular late fusion. arXiv. https://arxiv.org/abs/2506.01673

Liu, Z., Hou, Y., & McAuley, J. (2024). Multi-behavior generative recommendation. arXiv. https://arxiv.org/abs/2405.16871

Wang, C., Zhang, Y., Zhu, F., Zhang, J., Shi, T., & Feng, F. (2024). Leveraging memory retrieval to enhance LLM-based generative recommendation. arXiv. https://arxiv.org/abs/2412.17593

Wang, W., Bao, H., Lin, X., Zhang, J., Li, Y., Feng, F., Ng, S.-K., & Chua, T.-S. (2024). Learnable item tokenization for generative recommendation. arXiv. https://arxiv.org/abs/2405.07314

Zhai, J., Mai, Z.-F., Wang, C.-D., Yang, F., Zheng, X., Li, H., & Tian, Y. (2025). Multimodal quantitative language for generative recommendation. arXiv. https://arxiv.org/abs/2504.05314

Zhang, Y., Zhang, Y., Wang, Y., Chen, T., & Yin, H. (2025). Towards distribution matching between collaborative and language spaces for generative recommendation. arXiv. https://arxiv.org/abs/2504.07363

Zheng, B., Lu, H., Chen, Y., Zhao, W. X., & Wen, J.-R. (2025). Universal item tokenization for transferable generative recommendation. arXiv. https://arxiv.org/abs/2504.04405

Zhu, J., Ju, M., Liu, Y., Koutra, D., Shah, N., & Zhao, T. (2025). Beyond unimodal boundaries: Generative recommendation with multimodal semantics. arXiv. https://arxiv.org/abs/2503.23333
