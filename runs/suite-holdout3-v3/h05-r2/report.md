# Systematic Literature Review: Self-Supervised Visual Representation Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "self-supervised visual representation learning", cs.CV, last 2 years (2024-10-26 to 2026-10-26)
**Citation format**: APA 7th edition

## Executive Summary

The field of self-supervised visual representation learning has evolved significantly over the past two years, with research converging on several key principles and architectural innovations. The surveyed literature reveals a maturing field moving beyond simple contrastive learning toward unified theoretical frameworks that integrate semantic invariance, spatial prediction, and regularization. Recent work emphasizes the importance of preserving structural information in visual representations while leveraging cross-modal knowledge from language models. A notable trend is the shift from two-stage pretrain-finetune pipelines toward more efficient joint training paradigms, particularly for low-label scenarios. The literature also demonstrates growing attention to practical concerns including representation collapse prevention, computational efficiency through progressive freezing strategies, and security implications of self-supervised encoders.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "self-supervised visual representation learning", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Foundations and Unified Frameworks

Recent work has sought to establish rigorous theoretical foundations for self-supervised learning, moving beyond empirical observations to formal principles. Giakoumoglou et al. (2026) present perhaps the most comprehensive theoretical framework, arguing that effective self-supervised visual representation learning requires three non-overlapping objectives: semantic invariance across augmented views (observation), patch-level spatial prediction (prediction), and representational non-degeneracy (regularization). Their formal analysis proves that combining observation and prediction without regularization admits constant encoder solutions, while dropping any of the three principles forfeits critical learning signals. This unified energy decomposition framework subsumes existing major self-supervised methods as special cases, providing a theoretical lens through which to understand the field's progression.

The theoretical work connects to practical architectural choices, with several papers exploring how structural design decisions affect representation quality. The emphasis on formal guarantees represents a maturation of the field from heuristic approaches toward principled design.

### Theme 2: Architecture Innovation and Progressive Training Strategies

A second prominent theme involves novel architectural innovations and training schedules that improve both efficiency and representation quality. Erdogan et al. (2025) introduce LayerLock, which exploits the observation that ViT layers converge in depth order during training. By progressively freezing layers according to an explicit schedule, LayerLock accelerates training while preventing representation collapse in latent prediction tasks. This approach scales to models up to 4B parameters, demonstrating that thoughtful training schedules can enable both efficiency gains and improved performance.

Similarly, Kuzucu et al. (2025) address the modality mismatch between language and vision models through LAVIE, a framework that co-adapts ViT backbones with LLM fusion blocks using Masked Auto-Encoding and Low-Rank Adaptation. This joint optimization enables ViTs to produce LLM-aligned features while allowing LLMs to interpret visual information effectively, bridging the gap between text-centric pre-training and vision-centric applications.

### Theme 3: Joint Training vs. Pretrain-Finetune Paradigms

The field is actively reconsidering the standard two-stage pretrain-then-finetune pipeline. Munia et al. (2026) systematically compare pretrain-finetuning (PFT) against joint training (JT) across eight SSL methods and diverse domains including natural, medical, crisis response, and remote sensing imagery. Their comprehensive benchmark reveals that JT consistently improves data and training efficiency in low-label settings, while PFT remains more reliable in specialized domains. The relative effectiveness depends strongly on task characteristics, label availability, and domain complexity, suggesting that practitioners should choose training paradigms based on specific application constraints rather than defaulting to PFT.

This theme reflects broader questions about how self-supervised and supervised objectives interact during optimization, with implications for semi-supervised learning and transfer learning strategies.

### Theme 4: Preserving Structural and Equivariant Information

Several papers address the limitation that standard augmentation-based SSL methods excel at learning invariant features but neglect equivariant ones, reducing generalizability for downstream tasks requiring spatial reasoning. Wang et al. (2024) propose integrating image reconstruction as an auxiliary task in augmentation-based SSL, implementing cross-attention to blend features from augmented views before reconstructing one view. This approach learns both invariant and equivariant features without additional parameters, significantly improving performance on tasks involving combined augmentations.

Colton (2025) similarly examines how feature normalization affects representation structure in IJEPA, finding that standard layer normalization disrupts natural energy hierarchies of visual tokens. Replacing feature LN with DynTanh activation preserves token energies and eliminates checkerboard artifacts in loss maps, improving both classification and depth estimation performance. These works collectively emphasize that preserving structural information—whether spatial relationships, energy hierarchies, or equivariant properties—is critical for generalizable representations.

### Theme 5: Multi-Image and Sequential Reasoning

Emerging work extends self-supervised learning principles beyond single-image representations to multi-image reasoning and sequential prediction. Chen et al. (2025) demonstrate that images contain inherent constraints that can supervise multi-image reasoning without manually curated question-answer pairs. By constructing image triplets and training with rule-based reinforcement learning, their MiCo method learns reasoning abilities that generalize to diverse vision tasks beyond visual comparison.

He et al. (2025) introduce DSeq-JEPA, which incorporates discriminative sequential prediction into JEPA-style learning. By ordering predictions meaningfully using attention-derived saliency maps, DSeq-JEPA induces a curriculum-like semantic progression from primary to secondary cues, learning more discriminative and generalizable representations than standard I-JEPA variants. These approaches bridge latent predictive and autoregressive learning, expanding the scope of self-supervised visual representation learning.

### Theme 6: Security and Privacy Implications

As self-supervised models become foundational infrastructure, understanding their security properties becomes critical. Zhu et al. (2025) propose PartCrop, a unified membership inference attack method that works across different SSL training paradigms in black-box settings. By cropping object parts to query responses in representation space, PartCrop exploits shared part-aware capabilities among models and stronger part responses on training data. Their work reveals vulnerabilities in self-supervised encoders while proposing effective defenses including early stopping, differential privacy, and shrinking crop scale ranges.

This theme highlights that self-supervised learning research must consider not only representation quality but also privacy implications and attack surfaces, particularly as these models are deployed in sensitive applications.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of preserving structural information in visual representations. Giakoumoglou et al. (2026), Wang et al. (2024), and Colton (2025) all emphasize that standard approaches lose critical spatial or energy information, and that recovering this information improves downstream performance. There is also broad agreement that joint optimization strategies—whether co-adapting vision and language models (Kuzucu et al., 2025) or jointly training self-supervised and supervised objectives (Munia et al., 2026)—can improve efficiency and representation quality.

**Disagreements**: The literature reveals tension between unified theoretical frameworks and practical engineering solutions. While Giakoumoglou et al. (2026) argue for three necessary principles that all methods must satisfy, other papers demonstrate strong empirical results from more specialized approaches (e.g., LayerLock's progressive freezing or PartCrop's part-aware attacks). The field has not resolved whether a single unified framework can subsume all effective methods or whether domain-specific approaches remain necessary. Additionally, Munia et al. (2026) show that the effectiveness of joint training versus pretrain-finetune depends heavily on domain characteristics, suggesting no universal answer to the training paradigm question.

## Gaps and Open Questions

The collective literature reveals several important gaps:

1. **Limited evaluation diversity**: Most papers evaluate on standard benchmarks (ImageNet, VGG-Sound, NYU Depth V2), with limited exploration of how methods generalize to truly novel domains or under distribution shift.

2. **Computational cost concerns**: Several approaches (DSeq-JEPA, LAVIE, LayerLock at 4B parameters) introduce additional complexity, but few papers thoroughly analyze computational trade-offs or provide guidance for resource-constrained settings.

3. **Security implications underexplored**: Only Zhu et al. (2025) address membership inference attacks, suggesting that security analysis of self-supervised encoders remains nascent despite their widespread deployment.

4. **Theoretical-practical gap**: While Giakoumoglou et al. (2026) provide comprehensive theoretical analysis, the connection between formal guarantees and practical performance on real-world tasks requires further empirical validation.

5. **Multi-modal integration depth**: Current work on vision-language integration (Kuzucu et al., 2025) focuses on leveraging frozen LLM knowledge; deeper bidirectional integration and its effects on both vision and language capabilities remain unexplored.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: Can self-supervised visual representation learning principles be leveraged to enable Chain-of-Thought reasoning across multiple images without manually curated question-answer pairs?

**Methodology**: The authors construct image triplets comprising two augmented views of the same image and a third similar but distinct image, then train the model with rule-based reinforcement learning to generate reasoning processes comparing these images and determine if they are same or different.

**Key findings**:
- Images contain inherent constraints that can serve as supervision for multi-image reasoning, inspired by self-supervised visual representation learning
- The method trains without any human-annotated question-answer pairs, using only visual comparison tasks
- The learned reasoning ability generalizes effectively to a wide range of questions beyond visual comparison
- The approach achieves significant improvements on multi-image reasoning benchmarks
- The method shows strong performance on general vision tasks despite being trained solely on visual comparison

**Limitations**: The abstract does not explicitly state limitations; the approach relies on constructing image triplets which may not generalize to all multi-image reasoning scenarios.

### Colton (2025)

**Research question**: How does feature layer normalization affect the learning of visual representations in IJEPA, and can it be replaced to better preserve token energy hierarchies?

**Methodology**: The authors analyze the effect of layer normalization on feature representations in IJEPA, proposing that it disrupts natural energy hierarchies of visual tokens. They replace feature LN with DynTanh activation and evaluate on ImageNet linear probe and NYU Depth V2 monocular depth estimation tasks.

**Key findings**:
- Feature layer normalization in IJEPA disrupts the natural energy hierarchy of visual tokens by forcing all features to have identical L2 norms
- IJEPA models trained with feature LN exhibit loss maps with significant checkerboard-like artifacts
- Replacing feature LN with DynTanh activation better preserves token energies and fixes the checkerboard artifacts
- The modification improves ImageNet linear probe accuracy from 38% to 42.7% for ViT-Small
- The approach reduces RMSE by 0.08 on NYU Depth V2 monocular depth estimation

**Limitations**: The abstract does not explicitly state limitations; the evaluation is limited to specific architectures (ViT-Small) and datasets (ImageNet, NYU Depth V2).

### Erdogan et al. (2025)

**Research question**: Can progressive layer freezing accelerate masked autoencoding while preventing representation collapse in latent prediction?

**Methodology**: The authors observe that ViT layers converge in depth order during video MAE training, then exploit this by progressively freezing layers according to an explicit schedule. LayerLock transitions from pixel to latent prediction through this progressive freezing strategy.

**Key findings**:
- Progressive layer freezing accelerates standard MAE training by exploiting depth-ordered convergence
- The same schedule enables latent prediction without representation collapse
- LayerLock scales to models up to 4B parameters
- Results surpass non-latent masked prediction on the 4DS perception suite
- The approach is simple and scalable without requiring architectural changes

**Limitations**: The abstract does not explicitly state limitations; the effectiveness may depend on specific model architectures and the schedule design requires careful tuning.

### Giakoumoglou et al. (2026)

**Research question**: What are the necessary theoretical principles for self-supervised visual representation learning, and how do they interact to prevent representation collapse?

**Methodology**: The authors formalize three principles—observation (semantic invariance), prediction (patch-level spatial prediction), and regularization (representational non-degeneracy)—and prove theoretical claims about their interactions, pairing every claim with controlled experiments including patch-retrieval evaluation.

**Key findings**:
- Three non-overlapping objectives are necessary: observation, prediction, and regularization
- Combining observation and prediction without regularization admits constant encoder solutions under negative-free alignment
- The two objectives are gradient-complementary and structurally non-conflicting at encoder output
- Momentum encoders converge to the same fixed point as online encoders, providing no collapse guarantee at convergence
- Every major self-supervised method is a special case of a single unified energy decomposition

**Limitations**: The theoretical analysis applies to the scale studied; whether the principles hold at significantly different scales or with different architectural assumptions requires further investigation.

### He et al. (2025)

**Research question**: Can incorporating discriminative sequential prediction into JEPA-style learning improve the quality and generalizability of self-supervised visual representations?

**Methodology**: The authors propose DSeq-JEPA, which integrates a discriminatively ordered sequential process with JEPA-style learning by identifying primary discriminative regions using attention-derived saliency maps and predicting subsequent regions in discriminative order, inducing a curriculum-like semantic progression.

**Key findings**:
- DSeq-JEPA bridges latent predictive and autoregressive self-supervised learning by ordering predictions meaningfully
- The architecture uses attention-derived saliency maps as a proxy for visual importance to identify primary discriminative regions
- The sequential prediction process induces a curriculum-like semantic progression from primary to secondary cues
- DSeq-JEPA consistently learns more discriminative and generalizable representations compared to I-JEPA variants
- The approach shows improvements across diverse tasks: image classification, fine-grained categorization, detection/segmentation, and low-level reasoning

**Limitations**: The abstract does not explicitly state limitations; the approach adds complexity through sequential prediction which may increase computational cost during training.

### Krishnamurthy (2024)

**Research question**: Can self-supervised audio-visual representations learned from unlabeled videos improve sound effect recommendations for visual scenes?

**Methodology**: The author proposes an attention-based model that learns the relative importance of convolutional features extracted at different resolutions from audio and visual streams, encoding inputs based on their correspondence. The model is evaluated on audio-visual correlation classification and sound effect recommendation tasks, with additional cross-modal contrastive learning.

**Key findings**:
- The attention-based approach learns audio-visual representations from unlabeled videos based on correspondence
- The model improves correlation accuracy by 18% compared to baseline on VGG-Sound dataset
- The recommendation accuracy improves by 10% on VGG-Sound dataset
- Cross-modal contrastive learning further improves recommendation performance
- The approach works on both public datasets (VGG-Sound) and challenging gameplay video recordings

**Limitations**: The abstract does not explicitly state limitations; the evaluation is limited to specific datasets and the attention mechanism may not capture all audio-visual relationships.

### Kuzucu et al. (2025)

**Research question**: How can the modality gap between text-centric LLM pre-training and vision-centric ViT training be bridged to leverage LLM knowledge for vision-only tasks?

**Methodology**: LAVIE co-adapts a ViT backbone and an LLM fusion block by employing Masked Auto-Encoding to pre-train the ViT for richer visual representations, and concurrently training Low-Rank Adaptation layers within the LLM block using the same MAE objective.

**Key findings**:
- LAVIE bridges the modality gap through synergistic pre-training of vision and language components
- Joint optimization guides the ViT to produce LLM-aligned features and the LLM to interpret visual information effectively
- The framework significantly improves performance in various downstream vision tasks
- The approach offers an effective and efficient way to enhance visual understanding using frozen LLM knowledge
- Direct fusion without co-adaptation fails to fully exploit LLM potential and suffers from unstable finetuning

**Limitations**: The abstract does not explicitly state limitations; the approach requires careful coordination of MAE objectives across modalities and may not generalize to all LLM architectures.

### Munia et al. (2026)

**Research question**: Does jointly optimizing self-supervised and supervised objectives during training provide a better alternative to the standard pretrain-then-finetune pipeline?

**Methodology**: Across eight representative SSL methods and diverse computer vision tasks on natural, medical, crisis response, and remote sensing data, the authors compare pretrain-finetuning against joint training under varying percentages of labeled data, analyzing representation quality, robustness, and cross-domain generalization.

**Key findings**:
- The relative effectiveness of PFT and JT depends strongly on task, label availability, and domain complexity
- JT consistently improves data and training efficiency while being robust in low-label settings
- PFT is more reliable in more specialized domains
- The interaction between self-supervised and supervised objectives varies across domains
- The work establishes a comprehensive empirical benchmark for hybrid SSL-based semi-supervised learning

**Limitations**: The abstract does not explicitly state limitations; the comprehensive evaluation across eight methods and multiple domains may not cover all possible SSL approaches or application areas.

### Wang et al. (2024)

**Research question**: Can integrating image reconstruction as an auxiliary task in augmentation-based SSL facilitate equivariant feature learning without additional parameters?

**Methodology**: The authors implement a cross-attention mechanism to blend features learned from two augmented views, subsequently reconstructing one of them. This approach is adaptable to various datasets and augmented-pair based learning methods, evaluated on learning equivariant features through multiple linear regression tasks and downstream applications.

**Key findings**:
- Integration of image reconstruction facilitates equivariant feature learning without additional parameters
- The method is adaptable to various datasets and augmented-pair based learning methods
- Results demonstrate significant improvements over standard augmentation-based SSL and state-of-the-art approaches
- The approach particularly excels in scenarios involving combined augmentations
- The method enhances learning of both invariant and equivariant features, leading to more robust and generalizable representations

**Limitations**: The abstract does not explicitly state limitations; the cross-attention mechanism adds computational overhead during training though not during inference.

### Zhu et al. (2025)

**Research question**: Can a unified membership inference attack method be developed for visual self-supervised models that works across different training paradigms in a black-box setting?

**Methodology**: The authors propose PartCrop, a membership inference method that crops parts of objects in an image to query responses within the image in representation space, motivated by shared part-aware capability among models and stronger part response on training data. They evaluate on multiple datasets and propose defenses including shrinking crop scale range.

**Key findings**:
- PartCrop is effective and generalizes across self-supervised models with different training protocols and structures
- The method is motivated by shared part-aware capability among models and stronger part response on training data
- Common defenses like early stopping and differential privacy are effective against PartCrop
- The proposed tailored defense (shrinking crop scale range) is also effective
- PartCrop-v2 with structural improvements enables scalable attacks in realistic scenarios with larger data and models

**Limitations**: The abstract does not explicitly state limitations; the attack effectiveness may vary with different model architectures or defense mechanisms not evaluated in the study.

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
