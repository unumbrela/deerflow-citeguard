# Systematic Literature Review: Self-Supervised Visual Representation Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "self-supervised visual representation learning", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The field of self-supervised visual representation learning has matured significantly in the past two years, with research spanning theoretical foundations, architectural innovations, and practical applications. The surveyed literature reveals a field in transition: while foundational work continues to formalize the mathematical principles underlying representation collapse and learning guarantees, practitioners are increasingly exploring hybrid training paradigms that blur the lines between pretraining and finetuning. A notable trend is the integration of cross-modal knowledge—particularly from language models—into visual representation learning, alongside growing attention to advanced reasoning capabilities and security considerations. Collectively, these papers demonstrate that self-supervised learning is no longer solely about learning invariant features, but increasingly about learning structured, equivariant, and task-adaptive representations.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "self-supervised visual representation learning", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Foundations and Collapse Prevention

A foundational thread in recent work seeks to formalize the mathematical principles that govern successful self-supervised learning and prevent representation collapse. Giakoumoglou et al. (2026) provide a comprehensive theoretical framework identifying three necessary principles—observation, prediction, and regularization—and prove that combining observation and prediction without regularization admits the constant encoder as a global minimizer under negative-free alignment. Their work unifies major SSL methods as special cases of a single energy decomposition and challenges the assumed benefits of momentum encoders.

Complementing this theoretical work, Wang et al. (2024) address a different aspect of the collapse problem by showing that augmentation-based SSL methods excel at learning invariant features but neglect equivariant ones, limiting generalizability for downstream tasks requiring equivariance. Their image reconstruction approach facilitates equivariant feature learning without additional parameters, demonstrating that the collapse prevention problem extends beyond mere representation stability to encompass the richness and structure of learned features.

### Theme 2: Architectural Innovations in Training Paradigms

Several papers propose novel architectural modifications to improve the efficiency and effectiveness of self-supervised training. Erdogan et al. (2025) introduce LayerLock, which exploits the observation that ViT layers converge in order of depth during video MAE training. By progressively freezing layers according to an explicit schedule, they accelerate MAE training and enable latent prediction without representation collapse, achieving results that surpass non-latent masked prediction on the 4DS perception suite for models up to 4B parameters.

He et al. (2025) propose DSeq-JEPA, which integrates discriminatively-ordered sequential processing with JEPA-style learning. Unlike standard I-JEPA's parallel predictions, DSeq-JEPA identifies primary discriminative regions using attention-derived saliency maps and predicts subsequent regions in discriminative order, creating a curriculum-like semantic progression that learns more discriminative representations across classification, detection, segmentation, and reasoning tasks.

Colton (2025) focuses on a specific but critical architectural choice: feature normalization in IJEPA. The paper demonstrates that layer normalization of teacher encoder features disrupts the natural energy hierarchy of visual tokens by forcing all features to have identical L2 norms, producing loss maps with checkerboard-like artifacts. Replacing feature LN with DynTanh activation preserves token energies and improves ImageNet linear probe accuracy from 38% to 42.7% for ViT-Small.

### Theme 3: Training Strategy Comparisons - Pretrain-Finetune vs. Joint Training

Munia et al. (2026) provide a systematic empirical comparison of two training paradigms: pretraining followed by finetuning (PFT) versus joint training (JT) of self-supervised and supervised objectives. Their comprehensive study across eight SSL methods and diverse computer vision tasks reveals that the relative effectiveness depends strongly on task characteristics, labeled data availability, and domain complexity. Joint training consistently improves data and training efficiency while being robust in low-label settings, whereas pretrain-finetuning proves more reliable in specialized domains such as medical imaging and remote sensing. This work establishes an important empirical benchmark for hybrid SSL-based semi-supervised learning and challenges the assumption that PFT is universally superior.

### Theme 4: Cross-Modal Integration - Vision Meets Language and Audio

The integration of knowledge from other modalities represents a significant trend in recent SSL research. Kuzucu et al. (2025) propose LAVIE, a framework that bridges the modality mismatch between text-pretrained LLMs and vision transformers. Their key insight is that direct fusion of LLM blocks with ViTs fails due to unstable finetuning and frozen LLM components. LAVIE co-adapts a ViT backbone using Masked Auto-Encoding and LoRA layers within the LLM block, both optimized with the same MAE objective, guiding the ViT to produce LLM-aligned features while the LLM learns to interpret visual information effectively.

Krishnamurthy (2024) explores audio-visual representation learning from unlabeled videos, using an attention mechanism to learn the relative importance of convolutional features extracted at different resolutions from audio and visual streams. Their approach improves correlation accuracy by 18% and sound recommendation accuracy by 10% on VGG-Sound, demonstrating that cross-modal contrastive learning can effectively leverage naturally occurring audio-visual correspondences as self-supervision signals.

### Theme 5: Advanced Reasoning Capabilities

Beyond learning static representations, recent work explores self-supervised methods for developing reasoning capabilities. Chen et al. (2025) introduce MiCo, which learns Chain-of-Thought reasoning for multi-image visual tasks without manually curated question-answer pairs. By constructing image triplets and using rule-based reinforcement learning to train VLMs to generate reasoning processes for visual comparison tasks, they demonstrate that images contain inherent constraints that can serve as supervision. The learned reasoning ability generalizes effectively to a wide range of questions beyond visual comparison.

### Theme 6: Security and Privacy in Self-Supervised Learning

As SSL models become widely deployed, understanding their security properties becomes critical. Zhu et al. (2025) propose PartCrop, a unified membership inference method that exploits shared part-aware capability among self-supervised models by cropping object parts and querying responses within the representation space. Their method is effective across different SSL paradigms including masked image modeling and contrastive learning, demonstrating strong generalization across training protocols and model structures. The paper also evaluates defense strategies, finding that early stopping, differential privacy, and shrinking crop scale range are all effective countermeasures.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the insight that standard SSL approaches have important limitations that require architectural or methodological innovations. Both Wang et al. (2024) and Giakoumoglou et al. (2026) identify fundamental gaps in current methods—the former noting the neglect of equivariant features, the latter formalizing why regularization is necessary to prevent collapse. There is also broad agreement that self-supervision signals can be extracted from diverse sources: image augmentations (Wang et al., 2024), audio-visual correspondences (Krishnamurthy, 2024), multi-image constraints (Chen et al., 2025), and sequential structure (He et al., 2025).

**Disagreements**: The comparison between pretrain-finetune and joint training paradigms (Munia et al., 2026) reveals that there is no universal winner—the optimal choice depends on domain characteristics and label availability. This contrasts with earlier SSL literature that often assumed PFT was universally superior. Additionally, while Colton (2025) argues that feature normalization is harmful in IJEPA, this finding may be specific to the IJEPA architecture and mask-based prediction objectives, and may not generalize to other SSL frameworks that successfully employ normalization.

## Gaps and Open Questions

Several important gaps emerge from the surveyed literature:

1. **Limited experimental validation of theoretical claims**: Giakoumoglou et al. (2026) provide elegant theoretical proofs but validate them primarily on controlled settings and patch-retrieval tasks. Broader empirical validation across diverse datasets and downstream tasks remains an open challenge.

2. **Architecture-specific findings**: Many proposed improvements (LayerLock, DSeq-JEPA, DynTanh replacement) are evaluated on specific architectures (video MAE, I-JEPA) and may require substantial adaptation for other frameworks. Systematic cross-architecture evaluation is lacking.

3. **Scalability concerns**: While LayerLock demonstrates results on 4B parameter models, other methods have not been evaluated at similar scales. The behavior of these approaches at truly large scales (10B+ parameters) remains unknown.

4. **Defense-evasion arms race**: Zhu et al. (2025) demonstrate effective membership inference attacks and defenses, but this likely represents only the beginning of a security arms race. More sophisticated attacks and stronger defenses will likely emerge.

5. **Cross-modal generalization**: While LAVIE (Kuzucu et al., 2025) and audio-visual learning (Krishnamurthy, 2024) show promise, it remains unclear how broadly cross-modal knowledge transfer applies across different vision tasks and modalities.

## Per-Paper Annotations

### Colton (2025)

**Research question**: How does layer normalization of teacher encoder features affect IJEPA's ability to learn effective visual representations?
**Methodology**: The paper proposes replacing layer normalization with DynTanh activation in IJEPA to preserve natural token energy hierarchies, evaluated on ImageNet linear probe accuracy and NYU Depth V2 depth estimation.
**Key findings**:
- Feature layer normalization disrupts the natural energy hierarchy of visual tokens by forcing all features to have identical L2 norms
- IJEPA models trained with feature LN exhibit loss maps with significant checkerboard-like artifacts
- Replacing feature LN with DynTanh preserves token energies and produces a longer-tailed loss distribution
- ImageNet linear probe accuracy improves from 38% to 42.7% for ViT-Small with DynTanh
- RMSE on NYU Depth V2 monocular depth estimation is reduced by 0.08 with the proposed modification
**Limitations**: Not stated in abstract.

### Erdogan et al. (2025)

**Research question**: Can progressive layer freezing during training accelerate masked autoencoding and enable latent prediction without representation collapse?
**Methodology**: The authors observe that ViT layers converge in order of depth during video MAE training, then exploit this by progressively freezing layers according to an explicit schedule to accelerate MAE and enable latent prediction, evaluated on the 4DS perception suite.
**Key findings**:
- During video MAE training, shallower ViT layers converge early while deeper layers converge late
- Progressive freezing according to layer convergence order accelerates standard MAE training
- The same progressive freezing schedule enables a simple and scalable approach to latent prediction
- LayerLock does not suffer from representation collapse
- Results surpass those of non-latent masked prediction on the 4DS perception suite for models up to 4B parameters
**Limitations**: The abstract does not explicitly state limitations; the approach may be specific to video MAE models and the progressive freezing schedule may require tuning for different architectures.

### Giakoumoglou et al. (2026)

**Research question**: What are the necessary and sufficient principles for self-supervised visual representation learning to avoid representation collapse?
**Methodology**: The authors formalize three principles (observation, prediction, regularization) and provide theoretical proofs about their interactions, including gradient-complementarity and convergence analysis, validated with controlled experiments and patch-retrieval evaluation.
**Key findings**:
- Combining observation and prediction without regularization admits the constant encoder as a global minimizer under negative-free alignment
- The observation and prediction objectives are gradient-complementary and structurally non-conflicting at the encoder output
- The momentum encoder converges to the same fixed point as the online encoder and provides no collapse guarantee at convergence
- Contrastive alignment provides only self-limiting collapse resistance with explicit gradient-decay
- Every major self-supervised method is a special case of a single unified energy decomposition
**Limitations**: The theoretical analysis focuses on specific conditions (negative-free alignment, momentum encoder convergence); experimental validation is limited to controlled settings and patch-retrieval tasks.

### Chen et al. (2025)

**Research question**: Can Chain-of-Thought reasoning for multi-image visual tasks be learned without manually curated question-answer pairs?
**Methodology**: The method constructs image triplets (two augmented views of the same image plus one similar but distinct image) and uses rule-based reinforcement learning to train VLMs to generate reasoning processes for visual comparison tasks, evaluated on multi-image reasoning benchmarks and general vision tasks.
**Key findings**:
- Images contain inherent constraints that can serve as supervision for self-supervised learning
- The method requires no human-annotated question-answer pairs for training
- Reasoning ability learned from visual comparison tasks generalizes effectively to a wide range of questions
- Significant improvements are achieved on multi-image reasoning benchmarks
- Strong performance is demonstrated on general vision tasks
**Limitations**: Not stated in abstract.

### He et al. (2025)

**Research question**: Can incorporating sequential, discriminatively-ordered predictions into JEPA improve the quality and generalizability of learned visual representations?
**Methodology**: DSeq-JEPA integrates discriminatively-ordered sequential processing with JEPA-style learning by identifying primary discriminative regions using attention-derived saliency maps and predicting subsequent regions in discriminative order to create a curriculum-like semantic progression, evaluated across image classification, fine-grained categorization, detection/segmentation, and low-level reasoning tasks.
**Key findings**:
- Standard I-JEPA predicts target regions in parallel, lacking meaningful ordering of predictions
- DSeq-JEPA bridges latent predictive and autoregressive self-supervised learning approaches
- The method induces a curriculum-like semantic progression from primary to secondary cues during pre-training
- DSeq-JEPA consistently learns more discriminative representations compared to I-JEPA variants
- Improved generalizability is demonstrated across classification, fine-grained categorization, detection, segmentation, and reasoning tasks
**Limitations**: Not stated in abstract.

### Krishnamurthy (2024)

**Research question**: Can self-supervised audio-visual representations learned from unlabeled videos improve sound effect recommendation and audio-visual correlation classification?
**Methodology**: The approach uses an attention mechanism to learn the relative importance of convolutional features extracted at different resolutions from audio and visual streams, encoding inputs based on their correspondence, evaluated for audio-visual correlation classification and sound effect recommendation with cross-modal contrastive learning.
**Key findings**:
- The attention-based model improves correlation accuracy by 18% compared to baseline on VGG-Sound
- Sound recommendation accuracy improves by 10% on VGG-Sound dataset
- Audio-visual representations are learned from unlabeled videos based on correspondence
- Cross-modal contrastive learning further improves recommendation performance
- The method is evaluated on both VGG-Sound and a challenging gameplay video dataset
**Limitations**: Not stated in abstract.

### Kuzucu et al. (2025)

**Research question**: How can the modality mismatch between text-pretrained LLMs and vision transformers be bridged to effectively leverage LLM knowledge for vision-only tasks?
**Methodology**: The authors propose LAVIE, a framework that co-adapts a ViT backbone and LLM fusion block using Masked Auto-Encoding for the ViT and Low-Rank Adaptation layers within the LLM block, both optimized with the same MAE objective, evaluated on various downstream vision tasks.
**Key findings**:
- Direct fusion of LLM blocks with ViTs fails to fully exploit LLM potential and suffers from unstable finetuning
- Prior works typically keep LLM blocks frozen while learning only vision components
- LAVIE's joint optimization guides the ViT to produce LLM-aligned features and the LLM to effectively interpret visual information
- LAVIE significantly improves performance in various downstream vision tasks
- The approach offers an effective and efficient way to enhance visual understanding using frozen LLM knowledge
**Limitations**: The abstract does not specify limitations; potential constraints may include dependency on specific LLM architectures and the effectiveness of LoRA adaptation for different vision tasks.

### Munia et al. (2026)

**Research question**: Does jointly optimizing self-supervised and supervised objectives during training provide a better alternative to the standard pretrain-then-finetune pipeline for self-supervised learning?
**Methodology**: The authors systematically compare two training paradigms—pretraining followed by finetuning (PFT) and joint training (JT)—across eight representative SSL methods and diverse computer vision tasks on natural, medical, crisis response, and remote sensing data, evaluating performance under varying percentages of labeled data.
**Key findings**:
- The relative effectiveness of PFT and JT depends strongly on the task, availability of labeled data, and domain complexity
- Joint training consistently improves data and training efficiency while being robust in low-label settings
- Pretrain-finetuning is more reliable in more specialized domains
- The study provides new insights into how self-supervised and supervised objectives interact during optimization
- The work establishes a comprehensive empirical benchmark for hybrid SSL-based semi-supervised learning
**Limitations**: The abstract does not explicitly state limitations; the study's conclusions may be constrained by the specific SSL methods, datasets, and label percentages evaluated.

### Wang et al. (2024)

**Research question**: How can augmentation-based self-supervised learning methods be enhanced to learn equivariant features in addition to invariant ones for improved generalizability?
**Methodology**: The authors propose integrating an image reconstruction task as an auxiliary component using a cross-attention mechanism to blend features from two augmented views and reconstruct one of them, evaluated on equivariant feature learning through linear regression tasks and downstream applications on 3DIEBench and ImageNet datasets.
**Key findings**:
- Augmentation-based SSL methods excel at learning invariant features but often neglect equivariant ones
- This limitation reduces generalizability for downstream tasks requiring equivariance
- The proposed image reconstruction approach facilitates equivariant feature learning without additional parameters
- The method is adaptable to various datasets and augmented-pair based learning methods
- Results show significant improvements over standard methods and state-of-the-art approaches, particularly for combined augmentations
**Limitations**: The abstract does not explicitly state limitations; the method's effectiveness may depend on the choice of augmentations and the specific downstream tasks requiring equivariance.

### Zhu et al. (2025)

**Research question**: Can membership inference attacks be performed on visual self-supervised models in a black-box setting where training methods and details are unknown?
**Methodology**: PartCrop is proposed as a unified membership inference method that exploits shared part-aware capability among self-supervised models by cropping object parts in images and querying responses within the representation space, evaluated across different training protocols and architectures using three image datasets, with defense strategies also assessed.
**Key findings**:
- PartCrop is effective for membership inference across different self-supervised paradigms including masked image modeling and contrastive learning
- The method demonstrates strong generalization across different training protocols and model structures
- Early stopping, differential privacy, and shrinking crop scale range are all effective defense strategies
- Scaling impacts from both data and model aspects are quantitatively studied in realistic scenarios
- PartCrop-v2 introduces two structural improvements to enhance scalability
**Limitations**: Not stated in abstract.

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
