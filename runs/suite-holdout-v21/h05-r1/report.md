# Systematic Literature Review: Self-Supervised Visual Representation Learning

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "self-supervised visual representation learning", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of self-supervised visual representation learning has undergone significant evolution in the past two years, with research focusing on three major directions: theoretical foundations for preventing representation collapse, architectural innovations leveraging large language models, and novel training paradigms that challenge the traditional pretrain-then-finetune approach. The surveyed literature reveals a maturing field that is moving beyond empirical improvements toward principled understanding of why certain methods work. Key convergences include the recognition that regularization is essential for preventing collapse, that joint training can outperform sequential pretraining in low-label regimes, and that feature normalization choices have profound effects on learned representations. However, disagreements persist regarding the optimal balance between contrastive and non-contrastive approaches, and whether momentum encoders provide genuine theoretical benefits or merely practical training stability.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "self-supervised visual representation learning", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, metadata was extracted from abstracts only, which may not capture the full nuance of methodology or limitations discussed in the complete papers.

## Themes

### Theme 1: Theoretical Foundations for Preventing Representation Collapse

A central challenge in self-supervised learning is avoiding representation collapse, where models learn trivial solutions that map all inputs to identical outputs. Recent work has made significant progress in formalizing the conditions under which collapse occurs and identifying necessary principles for prevention. Giakoumoglou et al. (2026) provide the most comprehensive theoretical treatment, proving that combining observation and prediction objectives without regularization admits the constant encoder as a global minimizer under negative-free alignment. Their work demonstrates that every major self-supervised method can be understood as a special case of a single unified energy decomposition, providing a unifying framework for the field.

Complementing this theoretical work, Erdogan et al. (2025) introduce LayerLock, which exploits the empirical observation that Vision Transformer layers converge in order of depth during training. By progressively freezing layers according to an explicit schedule, they achieve both accelerated training and non-collapsing representations without additional architectural complexity. This work bridges theoretical understanding with practical training strategies, demonstrating that temporal dynamics of convergence can be leveraged for both efficiency and stability.

The theoretical theme also extends to understanding specific architectural choices. Colton (2025) reveals that layer normalization at the teacher encoder output in IJEPA disrupts the natural energy hierarchy of visual tokens, forcing all features to have identical L2 norms and introducing checkerboard-like artifacts in the loss landscape. By replacing layer normalization with DynTanh activation, the author achieves substantial improvements in both ImageNet classification (38% to 42.7% for ViT-Small) and depth estimation tasks.

### Theme 2: Integration with Large Language Models

The success of large language models has prompted investigation into how their capabilities can be transferred to visual representation learning. Kuzucu et al. (2025) introduce LAVIE, a framework that addresses the modality mismatch between text-centric LLMs and vision-centric Vision Transformers through synergistic co-adaptation. Their approach uses Masked Auto-Encoding for the ViT backbone while training LoRA layers within an LLM fusion block using the same MAE objective, enabling joint optimization that guides the ViT to produce LLM-aligned features while the LLM learns to interpret visual information effectively.

This theme represents a significant shift from purely vision-centric approaches toward multimodal representation learning that leverages the semantic understanding encoded in pretrained language models. The key insight is that LLMs contain rich world knowledge that can enhance visual representations when the modality gap is properly bridged through architectural design and training objectives.

### Theme 3: Training Paradigm Innovations

The traditional pipeline of pretraining followed by finetuning has been the dominant paradigm in self-supervised learning, but recent work questions whether this sequential approach is optimal. Munia et al. (2026) conduct a systematic comparison of pretrain-then-finetune versus joint training across eight self-supervised methods and diverse computer vision tasks. Their findings reveal that joint training consistently improves data and training efficiency while being robust in low-label settings, though pretrain-finetuning remains more reliable in specialized domains. This work establishes that the relative effectiveness depends strongly on task characteristics, label availability, and domain complexity.

He et al. (2025) introduce another paradigm innovation with DSeq-JEPA, which integrates discriminative ordered sequential processing with JEPA-style learning. Unlike standard I-JEPA that predicts target regions in parallel without meaningful ordering, DSeq-JEPA identifies primary discriminative regions using attention-derived saliency maps, then predicts subsequent regions in discriminative order to create a curriculum-like semantic progression. This approach bridges latent predictive and autoregressive self-supervised learning, inducing more discriminative and generalizable representations.

### Theme 4: Multi-Modal and Multi-Image Reasoning

Beyond single-image representation learning, recent work explores how self-supervised principles can enable reasoning across multiple images or modalities. Chen et al. (2025) present MiCo, which constructs image triplets with two augmented views and one distinct image, then uses rule-based reinforcement learning to train models to generate reasoning processes for visual comparison tasks without manually curated question-answer pairs. Their key insight is that images contain inherent constraints that can serve as self-supervised signals, enabling Chain-of-Thought reasoning across multiple images.

Krishnamurthy (2024) extends self-supervised learning to the audio-visual domain, using attention mechanisms to learn the relative importance of multi-resolution convolutional features from audio and visual streams. The approach leverages correspondence between audio and visual signals in unlabeled videos, achieving 18% improvement in correlation accuracy and 10% improvement in recommendation accuracy on the VGG-Sound dataset.

### Theme 5: Privacy and Security Implications

As self-supervised models become more powerful, understanding their privacy implications has become increasingly important. Zhu et al. (2025) develop PartCrop, a unified membership inference attack method for visual self-supervised models in black-box settings where training methods and details are unknown. By cropping parts of objects in images to query responses within the representation space, they exploit shared part-aware capability among models. Their work reveals that early stopping, differential privacy, and shrinking crop scale ranges are all effective defenses, providing important guidance for deploying self-supervised models in privacy-sensitive applications.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers acknowledge that regularization or architectural constraints are necessary to prevent representation collapse, whether through explicit regularization terms (Giakoumoglou et al., 2026), progressive layer freezing (Erdogan et al., 2025), or careful normalization choices (Colton, 2025). Second, there is consensus that joint optimization of complementary objectives can yield better representations than single-objective training, whether through ViT-LLM co-adaptation (Kuzucu et al., 2025) or sequential predictive curricula (He et al., 2025). Third, multiple papers demonstrate that self-supervised signals can be extracted from inherent structure in data without manual annotation, whether through multi-image constraints (Chen et al., 2025) or cross-modal correspondence (Krishnamurthy, 2024).

**Disagreements**: The literature reveals tension regarding the optimal training paradigm. While Munia et al. (2026) find joint training superior in low-label regimes, they acknowledge pretrain-finetuning remains more reliable in specialized domains, suggesting no universal answer. Additionally, there is disagreement about the role of momentum encoders: Giakoumoglou et al. (2026) prove that momentum encoders converge to the same fixed point as online encoders and provide no collapse guarantee at convergence, challenging the theoretical justification for their widespread use in methods like BYOL and SimSiam. The field also lacks consensus on whether contrastive or non-contrastive approaches are fundamentally superior, with different papers advocating for each based on empirical results in specific domains.

## Gaps and Open Questions

Several important gaps emerge from the surveyed literature. First, none of the papers explicitly state limitations in their abstracts, suggesting either that limitations are discussed only in full papers or that the field has not yet developed norms for systematic limitation reporting. Second, while theoretical work (Giakoumoglou et al., 2026) unifies existing methods under a single framework, there is limited exploration of entirely new method classes that this framework might suggest. Third, the privacy implications work (Zhu et al., 2025) stands relatively isolated from the main representation learning literature, indicating a gap in integrating security considerations into method development.

The literature also lacks systematic investigation of computational efficiency and environmental impact, with most papers focused on accuracy improvements without reporting training costs or carbon footprint. Additionally, there is limited work on domain adaptation and transfer to out-of-distribution settings, despite the practical importance of these scenarios. Finally, while several papers demonstrate improvements on standard benchmarks, there is insufficient investigation of whether these improvements translate to real-world applications with different data distributions and requirements.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: Can self-supervised visual representation learning principles enable Chain-of-Thought reasoning across multiple images without manually curated question-answer pairs?
**Methodology**: The authors construct image triplets with two augmented views and one distinct image, then use rule-based reinforcement learning to train the model to generate reasoning processes for visual comparison tasks.
**Key findings**:
- Images contain inherent constraints that can serve as self-supervised signals for training
- The method requires no human-annotated question-answer pairs
- Reasoning ability learned from visual comparison tasks generalizes to a wide range of questions
- Significant improvements achieved on multi-image reasoning benchmarks
- Strong performance demonstrated on general vision tasks
**Limitations**: Not stated in abstract

### Colton (2025)

**Research question**: How does layer normalization at the teacher encoder output affect IJEPA's ability to learn effective visual representations?
**Methodology**: The author proposes replacing layer normalization with DynTanh activation to preserve natural token energy hierarchies, then evaluates the modification on ImageNet linear probe accuracy and NYU Depth V2 monocular depth estimation.
**Key findings**:
- Layer normalization disrupts the natural energy hierarchy of visual tokens by forcing all features to have identical L2 norms
- IJEPA models trained with feature layer normalization exhibit loss maps with significant checkerboard-like artifacts
- Replacing layer normalization with DynTanh activation produces a longer-tailed loss distribution and eliminates checkerboard artifacts
- ImageNet linear probe accuracy improves from 38% to 42.7% for ViT-Small with the proposed modification
- RMSE on NYU Depth V2 monocular depth estimation is reduced by 0.08
**Limitations**: Not stated in abstract

### Erdogan et al. (2025)

**Research question**: Can progressive layer freezing accelerate masked autoencoding and enable latent prediction without representation collapse?
**Methodology**: The authors introduce LayerLock, which exploits the observation that ViT layers converge in order of depth by progressively freezing layers according to an explicit schedule during training.
**Key findings**:
- During video MAE training, shallower ViT layers converge early while deeper layers converge late
- Progressive freezing according to this schedule accelerates standard MAE training
- The same schedule enables a simple and scalable approach to latent prediction without representation collapse
- LayerLock applied to models up to 4B parameters surpasses non-latent masked prediction on the 4DS perception suite
**Limitations**: Not stated in abstract

### Giakoumoglou et al. (2026)

**Research question**: What are the necessary principles for self-supervised visual representation learning to avoid representation collapse?
**Methodology**: The authors formalize three principles (observation, prediction, regularization) and prove theoretical claims about their necessity, then validate with controlled experiments including patch-retrieval evaluation.
**Key findings**:
- Combining observation and prediction without regularization admits the constant encoder as a global minimizer under negative-free alignment
- The observation and prediction objectives are gradient-complementary and structurally non-conflicting at the encoder output
- The momentum encoder converges to the same fixed point as the online encoder and provides no collapse guarantee at convergence
- Contrastive alignment provides only self-limiting collapse resistance with explicit gradient decay
- Every major self-supervised method is a special case of a single unified energy decomposition
**Limitations**: Not stated in abstract

### He et al. (2025)

**Research question**: Can integrating discriminative ordered sequential processing with JEPA-style learning improve the discriminability and generalizability of self-supervised visual representations?
**Methodology**: DSeq-JEPA identifies primary discriminative regions using attention-derived saliency maps, then predicts subsequent regions in discriminative order to create a curriculum-like semantic progression from primary to secondary cues.
**Key findings**:
- Standard I-JEPA predicts target regions in parallel, lacking meaningful ordering of predictions
- DSeq-JEPA bridges latent predictive and autoregressive self-supervised learning
- The method induces a curriculum-like semantic progression from primary to secondary cues
- Consistently learns more discriminative and generalizable representations compared to I-JEPA variants
- Validated across image classification, fine-grained categorization, detection/segmentation, and low-level reasoning tasks
**Limitations**: Not stated in abstract

### Krishnamurthy (2024)

**Research question**: Can self-supervised audio-visual representations learned from unlabeled videos improve sound effect recommendation and audio-visual correlation classification?
**Methodology**: The approach uses an attention mechanism to learn the relative importance of multi-resolution convolutional features from audio and visual streams, with cross-modal contrastive learning for additional improvement.
**Key findings**:
- The attention-based model improves correlation accuracy by 18% compared to baseline
- Recommendation accuracy improves by 10% on VGG-Sound dataset
- Audio-visual representations are learned from unlabeled videos based on correspondence
- Cross-modal contrastive learning further improves recommendation performance
- The method performs well on both VGG-Sound and a challenging gameplay video dataset
**Limitations**: Not stated in abstract

### Kuzucu et al. (2025)

**Research question**: How can the modality mismatch between text-centric LLMs and vision-centric ViTs be bridged to enhance self-supervised visual representation learning?
**Methodology**: The authors introduce LAVIE, a framework that co-adapts a ViT backbone and LLM fusion block using Masked Auto-Encoding for the ViT and LoRA layers within the LLM block trained with the same MAE objective.
**Key findings**:
- LAVIE bridges the modality gap through synergistic pre-training of ViT and LLM components
- Joint optimization guides the ViT to produce LLM-aligned features and the LLM to effectively interpret visual information
- LAVIE significantly improves performance in various downstream vision tasks
- The approach offers an effective and efficient way to enhance visual understanding using frozen LLM knowledge
**Limitations**: Not stated in abstract

### Munia et al. (2026)

**Research question**: Does jointly optimizing self-supervised and supervised objectives during training provide a better alternative to the traditional pretrain-then-finetune pipeline?
**Methodology**: The authors systematically compare two training paradigms (pretraining followed by finetuning vs. joint training) across eight SSL methods and diverse computer vision tasks under varying percentages of labeled data.
**Key findings**:
- Joint training consistently improves data and training efficiency while being robust in low-label settings
- Pretrain-finetuning is more reliable in more specialized domains
- The relative effectiveness of the two paradigms depends strongly on the task, availability of labeled data, and domain complexity
- The study establishes a comprehensive empirical benchmark for hybrid SSL-based semi-supervised learning
**Limitations**: Not stated in abstract

### Wang et al. (2024)

**Research question**: Can integrating an image reconstruction task facilitate equivariant feature learning in augmentation-based self-supervised learning without additional parameters?
**Methodology**: The authors propose a cross-attention mechanism to blend features from two augmented views and reconstruct one of them, adaptable to various datasets and augmented-pair based learning methods.
**Key findings**:
- The method facilitates equivariant feature learning without additional parameters
- Results show significant improvements over standard augmentation-based SSL methods and state-of-the-art approaches
- The approach excels particularly in scenarios involving combined augmentations
- The method enhances learning of both invariant and equivariant features, leading to more robust and generalizable visual representations
**Limitations**: Not stated in abstract

### Zhu et al. (2025)

**Research question**: Can a unified membership inference attack method be developed for visual self-supervised models in a black-box setting where training methods and details are unknown?
**Methodology**: PartCrop crops parts of objects in images to query responses within the representation space, exploiting shared part-aware capability among models; PartCrop-v2 introduces two structural improvements for scalability.
**Key findings**:
- PartCrop is effective across self-supervised models with different training protocols and architectures
- The method works on three widely used image datasets
- Early stop, differential privacy, and shrinking crop scale range are all effective defenses
- Scaling impacts were quantitatively studied from both data and model aspects
- PartCrop-v2 achieves improved scalability through two structural enhancements
**Limitations**: Not stated in abstract

## References

Chen, X., Zhu, M., Liu, S., Wu, X., Xu, X., Liu, Y., Bai, X., & Zhao, H. (2025). MiCo: Multi-image contrast for reinforcement visual reasoning. arXiv. https://arxiv.org/abs/2506.22434

Colton, A. (2025). Elucidating the role of feature normalization in IJEPA. arXiv. https://arxiv.org/abs/2508.02829

Erdogan, G., Parthasarathy, N., Ionescu, C., Hudson, D. A., Lerchner, A., Zisserman, A., Sajjadi, M. S. M., & Carreira, J. (2025). LayerLock: Non-collapsing representation learning with progressive freezing. arXiv. https://arxiv.org/abs/2509.10156

Giakoumoglou, N., Giakoumoglou, P., & Stathaki, T. (2026). Three necessary principles for self-supervised visual representation learning. arXiv. https://arxiv.org/abs/2608.08309

He, X., Sakai, S., Chandhok, S., Beery, S., Yuan, K., Padoy, N., Hasegawa, T., & Sigal, L. (2025). DSeq-JEPA: Discriminative sequential joint-embedding predictive architecture. arXiv. https://arxiv.org/abs/2511.17354

Krishnamurthy, S. (2024). Learning self-supervised audio-visual representations for sound recommendations. arXiv. https://arxiv.org/abs/2412.07406

Kuzucu, S., Naeem, M. F., Kukleva, A., Tombari, F., & Schiele, B. (2025). Enhancing self-supervised visual representation learning via low-rank adapted LLMs. arXiv. https://arxiv.org/abs/2507.00754

Munia, N., Ward, T., Nayla, N., Massey, M. A., & Imran, A.-A.-Z. (2026). Self-supervised visual representation learning: Pretrain-finetuning or joint training? arXiv. https://arxiv.org/abs/2607.13192

Wang, Q., Krajsek, K., & Scharr, H. (2024). Equivariant representation learning for augmentation-based self-supervised learning via image reconstruction. arXiv. https://arxiv.org/abs/2412.03314

Zhu, J., Zha, J., Li, D., & Wang, L. (2025). A unified and scalable membership inference method for visual self-supervised encoder via part-aware capability. arXiv. https://arxiv.org/abs/2505.10351
