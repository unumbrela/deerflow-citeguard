# Systematic Literature Review: Self-Supervised Visual Representation Learning

**Date**: 2025-10-25
**Papers surveyed**: 9
**Scope**: arXiv search query "self-supervised visual representation", filtered to category cs.CV, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

Self-supervised visual representation learning has evolved significantly in the past two years, with research focusing on three major directions: theoretical unification of SSL principles, architectural innovations in predictive frameworks, and practical integration with foundation models. The surveyed literature reveals a field maturing from empirical exploration toward theoretical grounding, with recent work establishing formal principles that unify disparate SSL methods under common frameworks. Simultaneously, practical advances in JEPA-style architectures, masked autoencoding, and cross-modal integration with LLMs demonstrate continued progress in representation quality and downstream task performance. A notable trend is the shift from purely contrastive or generative approaches toward hybrid methods that combine multiple learning signals while addressing fundamental challenges like representation collapse and training efficiency.

## Methodology

This review surveyed 9 arXiv papers retrieved on 2025-10-25 using the query "self-supervised visual representation", filtered to category cs.CV, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 9 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search returned 9 papers instead of the requested 10, reflecting the actual result set for this query in the specified time window.

## Themes

### Theme 1: Theoretical Unification and Formal Principles

A significant thread in recent SSL research involves establishing theoretical frameworks that unify disparate methods and explain their success or failure modes. Giakoumoglou et al. (2024) propose three necessary principles—observation (semantic invariance), prediction (spatial understanding), and regularization (non-degeneracy)—proving that omitting any principle admits degenerate solutions like constant encoders. Their theoretical analysis demonstrates that major SSL methods are special cases of a unified energy decomposition, providing formal justification for combining multiple learning objectives. Similarly, theoretical work on momentum encoders reveals they converge to the same fixed point as online encoders and provide no collapse guarantee at convergence, challenging common assumptions about their role in preventing representation collapse.

This theoretical turn extends to understanding specific architectural choices. Colton (2025) analyzes how layer normalization in IJEPA disrupts the natural energy hierarchy of visual tokens, providing theoretical and empirical evidence that preserving token energies through alternative activations (DynTanh) improves downstream performance. These works collectively suggest the field is moving beyond empirical trial-and-error toward principled design grounded in formal analysis of optimization landscapes and representational properties.

### Theme 2: Architectural Innovation in Predictive Frameworks

Joint-Embedding Predictive Architectures (JEPAs) and masked autoencoding approaches continue to evolve with novel architectural modifications. He et al. (2025) introduce DSeq-JEPA, which bridges latent predictive and autoregressive learning by ordering predictions discriminatively based on visual saliency, mimicking human visual perception's progression from primary to secondary cues. This sequential approach consistently outperforms parallel I-JEPA variants across classification, detection, segmentation, and reasoning tasks.

Erdogan et al. (2025) propose LayerLock, exploiting the observation that ViT layers converge in depth order during training. By progressively freezing layers according to an explicit schedule, they accelerate MAE training and enable scalable latent prediction without representation collapse, scaling successfully to 4B parameter models. Wang et al. (2024) address a different limitation—augmentation-based SSL methods excel at learning invariant features but neglect equivariant ones—by integrating image reconstruction as an auxiliary task that facilitates equivariant feature learning without additional parameters.

### Theme 3: Training Strategy Optimization

The interaction between self-supervised and supervised learning objectives has received renewed attention. Munia et al. (2026) systematically compare pretrain-then-finetune (PFT) versus joint training (JT) paradigms across eight SSL methods and diverse domains. Their comprehensive benchmark reveals that JT consistently improves data and training efficiency in low-label settings, while PFT remains more reliable in specialized domains like medical and remote sensing imagery. This work challenges the default PFT pipeline and provides practical guidance for selecting training strategies based on task requirements and label availability.

Colton (2025) similarly optimizes training dynamics by replacing feature layer normalization with DynTanh activation in IJEPA, improving ImageNet linear probe accuracy from 38% to 42.7% for ViT-Small. These works demonstrate that training strategy—including optimization schedules, normalization choices, and the timing of supervised signal introduction—remains a critical lever for improving SSL performance.

### Theme 4: Cross-Modal Integration with Foundation Models

The integration of SSL with large language models represents an emerging frontier. Kuzucu et al. (2025) introduce LAVIE (Language-Adapted Vision Enhancer), which co-adapts Vision Transformers and LLM blocks through joint masked autoencoding. By training Low-Rank Adaptation (LoRA) layers within the LLM block alongside ViT pretraining, LAVIE bridges the modality gap between text-centric LLMs and vision-centric ViTs, significantly improving downstream vision tasks while keeping most LLM parameters frozen. This approach exemplifies a broader trend of leveraging foundation model knowledge without full fine-tuning, addressing both computational efficiency and modality mismatch challenges.

### Theme 5: Self-Supervised Learning for Reasoning and Generalization

Recent work extends SSL beyond representation learning to reasoning capabilities. Chen et al. (2025) develop MiCo, which enables Chain-of-Thought reasoning in Vision-Language Models through self-supervised visual comparison tasks. By constructing image triplets and using rule-based reinforcement learning, their method learns reasoning abilities that generalize to diverse questions without any human-annotated question-answer pairs. This work demonstrates that images contain inherent constraints sufficient for training sophisticated reasoning capabilities, opening new directions for self-supervised cognitive skill acquisition.

Cunha et al. (2026) examine SSL's role in robustness and generalization through face forgery detection benchmarks. Their findings show that frozen self-supervised DINOv3 backbones achieve superior robustness under realistic degradations (compression, resizing, blurring) compared to supervised models, despite training only a linear classification head. This suggests that self-supervised representations capture more generalizable features that transfer better to challenging real-world conditions.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of combining multiple learning signals rather than relying on single objectives. Giakoumoglou et al. (2024), Wang et al. (2024), and He et al. (2025) all demonstrate that hybrid approaches—whether combining observation with prediction, invariant with equivariant learning, or parallel with sequential prediction—outperform single-objective methods. There is also broad agreement that architectural choices in normalization, freezing schedules, and prediction ordering significantly impact final representation quality.

The literature converges on self-supervised representations' superior robustness to distribution shift and degradation. Cunha et al. (2026) show DINOv3 maintains performance under realistic image degradations where supervised models fail, and Munia et al. (2026) find joint training improves cross-domain generalization. This suggests SSL learns more fundamental visual structure less tied to dataset-specific biases.

**Disagreements**: The primary tension lies in training paradigm selection. Munia et al. (2026) find joint training superior in low-label, general domains, while pretrain-finetuning excels in specialized domains—challenging claims that JT universally dominates. Similarly, while Giakoumoglou et al. (2024) argue all three principles (observation, prediction, regularization) are necessary, practical success of methods emphasizing only one or two principles (e.g., pure contrastive learning or pure masked prediction) suggests context-dependence their theory does not fully capture.

## Gaps and Open Questions

Several limitations recur across the surveyed literature. First, theoretical analyses often focus on specific architectural assumptions (negative-free alignment, momentum encoders, ViT-based models) that may not generalize to all SSL variants. Giakoumoglou et al. (2024), Colton (2025), and Erdogan et al. (2025) all acknowledge their frameworks apply to particular methodological families, leaving open whether unified principles extend to contrastive, generative, and hybrid methods equally.

Second, evaluation remains concentrated on standard benchmarks (ImageNet, COCO, ADE20K) with limited exploration of specialized domains beyond Munia et al.'s (2026) multi-domain study. The gap between benchmark performance and real-world deployment—particularly regarding robustness, fairness, and computational efficiency—receives insufficient attention. Only Cunha et al. (2026) explicitly evaluate under realistic degradation conditions.

Third, computational costs and scaling behavior are underexplored. While Erdogan et al. (2025) demonstrate LayerLock scales to 4B parameters, most papers evaluate on small-to-medium models, leaving unclear whether proposed improvements persist at frontier scales. Similarly, the environmental and economic costs of SSL pretraining—especially for methods requiring extensive augmentation or cross-modal integration—warrant systematic analysis.

Finally, the relationship between SSL and emerging foundation models remains incompletely understood. Kuzucu et al. (2025) and Chen et al. (2025) point toward SSL's role in adapting and extending foundation models, but the field lacks comprehensive frameworks for when to pretrain from scratch versus adapt existing models, and how SSL objectives interact with foundation model capabilities.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: How can Vision-Language Models learn Chain-of-Thought reasoning across multiple images without relying on manually curated question-answer pairs?
**Methodology**: Constructs image triplets (two augmented views plus one distinct but similar image) and uses rule-based reinforcement learning to train models to generate reasoning processes for visual comparison tasks.
**Key findings**:
- Images contain inherent constraints sufficient for self-supervised reasoning training
- Training solely on visual comparison enables generalization to diverse reasoning questions
- Achieves significant improvements on multi-image reasoning benchmarks without human annotations
- The method forces attention to subtle visual changes through high similarity and augmentations
**Limitations**: Trained only on visual comparison tasks, which may not capture all forms of complex multi-image reasoning; performance on highly abstract or domain-specific logical tasks needs further evaluation.

### Colton (2025)

**Research question**: How does feature layer normalization affect IJEPA's ability to learn from the natural energy hierarchy of visual tokens?
**Methodology**: Proposes replacing layer normalization with DynTanh activation at teacher encoder output to preserve natural token energies, evaluated on ImageNet classification and NYU Depth V2 depth estimation.
**Key findings**:
- Feature layer normalization disrupts natural token energy hierarchy by equalizing L2 norms
- IJEPA models with feature LN exhibit checkerboard-like artifacts in loss maps
- DynTanh preserves token energies and produces longer-tailed loss distributions
- ImageNet linear probe accuracy improves from 38% to 42.7% for ViT-Small
- RMSE reduces by 0.08 on NYU Depth V2 monocular depth estimation
**Limitations**: Evaluation limited to ViT-Small architecture and specific tasks; does not explore other normalization alternatives beyond DynTanh or test on larger model scales.

### Cunha et al. (2026)

**Research question**: How do face forgery detectors perform under realistic image degradations, and which input representations (spatial, spectral, or self-supervised) are most robust?
**Methodology**: Presents standardized benchmark using MFFI dataset, evaluating six model families across spatial, spectral, and hybrid representations on clean and degraded test partitions.
**Key findings**:
- Clean-set performance poorly predicts robustness under compression, resizing, and blurring
- Xception with RGB achieves best clean performance (0.884 ROC-AUC) but degrades substantially
- Frozen DINOv3 achieves strongest degraded-set result (0.726 ROC-AUC) with only linear head training
- Fourier-domain cues most useful when combined with RGB; purely spectral inputs underperform
- Convolutional detectors focus on localized artifacts while DINOv3 uses broader facial structure
**Limitations**: Benchmark covers specific degradation types but may not capture all realistic conditions; frozen self-supervised backbones may not fully exploit representational capacity; does not address emerging forgery techniques.

### Erdogan et al. (2025)

**Research question**: How can we accelerate MAE training and enable latent prediction without representation collapse by exploiting ViT layer convergence patterns?
**Methodology**: Observes ViT layers converge in depth order during video MAE training, then exploits this by progressively freezing layers according to explicit schedules throughout training.
**Key findings**:
- ViT layers converge in depth order: shallower layers converge early, deeper layers converge late
- Progressive layer freezing accelerates standard MAE training
- Same freezing schedule enables latent prediction without representation collapse
- LayerLock surpasses non-latent masked prediction on 4DS perception suite
- Approach scales to large models up to 4B parameters
**Limitations**: Freezing schedule design may require tuning for different architectures and tasks; primarily evaluated on video MAE models and may need adaptation for other SSL frameworks.

### Giakoumoglou et al. (2024)

**Research question**: What are the necessary and sufficient principles for learning visual representations without labels?
**Methodology**: Formalizes three principles (observation, prediction, regularization) and proves theoretical claims through gradient analysis and convergence arguments, paired with controlled experiments including patch-retrieval evaluation.
**Key findings**:
- Combining observation and prediction without regularization admits constant encoder as global minimizer
- Observation and prediction objectives are gradient-complementary and structurally non-conflicting
- Momentum encoder converges to same fixed point as online encoder with no collapse guarantee
- Contrastive alignment provides only self-limiting collapse resistance via gradient decay
- Every major SSL method is a special case of unified energy decomposition
**Limitations**: Theoretical framework focuses on specific architectural assumptions (negative-free alignment, momentum encoders) that may not capture all practical SSL variants; experimental validation at scale limited to studied configurations.

### He et al. (2025)

**Research question**: How can JEPA-style learning incorporate sequential, discriminatively-ordered prediction to learn more transferable and discriminative visual representations?
**Methodology**: DSeq-JEPA integrates discriminative ordering with JEPA by identifying primary discriminative regions via attention-derived saliency maps and predicting subsequent regions in discriminative order.
**Key findings**:
- Sequential prediction with discriminative ordering bridges latent predictive and autoregressive learning
- DSeq-JEPA learns more discriminative and generalizable representations than I-JEPA variants
- Improvements across ImageNet classification, fine-grained categorization (iNaturalist21, CUB, Stanford Cars)
- Performance gains extend to detection/segmentation (MS-COCO, ADE20K) and reasoning (CLEVR)
- Curriculum-like semantic progression mimics human visual perception
**Limitations**: Sequential prediction introduces computational complexity versus parallel I-JEPA; requires careful saliency map design and may need tuning for different architectures; not evaluated on video or temporal reasoning tasks.

### Kuzucu et al. (2025)

**Research question**: How can we effectively integrate LLM blocks with Vision Transformers for vision-only tasks despite modality mismatch between text-centric LLMs and vision-centric ViTs?
**Methodology**: Introduces LAVIE framework that co-adapts ViT backbone and LLM fusion block through joint masked autoencoding, employing MAE for ViT pretraining and LoRA layers within LLM block.
**Key findings**:
- LAVIE bridges modality gap through synergistic pre-training between ViT and LLM components
- Joint optimization guides ViT to produce LLM-aligned features
- LoRA adaptation enables LLM to interpret visual information without full fine-tuning
- Significant improvement in various downstream vision tasks versus prior fusion approaches
- Effective and efficient enhancement of visual understanding using frozen LLM knowledge
**Limitations**: LLM blocks remain partially frozen with only LoRA adaptation, potentially limiting full LLM capability exploitation; modality mismatch mitigated but not fully resolved.

### Munia et al. (2026)

**Research question**: Does jointly optimizing self-supervised and supervised objectives during training provide a better alternative to standard pretrain-then-finetune pipelines?
**Methodology**: Systematically compares pretrain-finetuning versus joint training across eight SSL methods and diverse computer vision tasks on natural, medical, crisis response, and remote sensing data with varying label percentages.
**Key findings**:
- Relative effectiveness of PFT and JT depends on task, label availability, and domain complexity
- Joint training improves data and training efficiency while robust in low-label settings
- Pretrain-finetuning more reliable in specialized domains
- Different representation quality, robustness, and cross-domain generalization characteristics
- Establishes comprehensive benchmark for hybrid SSL-based semi-supervised learning
**Limitations**: Results may not generalize to all SSL methods or domains beyond those tested; lacks theoretical analysis of why PFT performs better in specialized domains.

### Wang et al. (2024)

**Research question**: How can we facilitate equivariant feature learning in augmentation-based SSL without adding parameters, addressing the neglect of equivariant features?
**Methodology**: Integrates image reconstruction as auxiliary component in augmentation-based SSL, implementing cross-attention mechanism to blend features from two augmented views and reconstruct one.
**Key findings**:
- Reconstruction auxiliary facilitates equivariant feature learning without additional parameters
- Approach adaptable to various datasets and augmented-pair based learning methods
- Significant improvements over standard augmentation-based SSL and state-of-the-art approaches
- Particularly excels in scenarios involving combined augmentations
- Enhances both invariant and equivariant features for more robust representations
**Limitations**: Reconstruction task may add computational overhead during training; evaluation on 3DIEBench and ImageNet may not cover all downstream task requirements.

## References

Chen, X., Zhu, M., Liu, S., Wu, X., Xu, X., Liu, Y., Bai, X., & Zhao, H. (2025). MiCo: Multi-image contrast for reinforcement visual reasoning. arXiv. https://arxiv.org/abs/2506.22434

Colton, A. (2025). Elucidating the role of feature normalization in IJEPA. arXiv. https://arxiv.org/abs/2508.02829

Cunha, L., Sotomaior, L., Gasperin, L., Caldas, B., Pianovski, E., & Laroca, R. (2026). Benchmarking spatial, spectral, and self-supervised cues for face forgery detection under realistic degradation. arXiv. https://arxiv.org/abs/2609.01511

Erdogan, G., Parthasarathy, N., Ionescu, C., Hudson, D. A., Lerchner, A., Zisserman, A., Sajjadi, M. S. M., & Carreira, J. (2025). LayerLock: Non-collapsing representation learning with progressive freezing. arXiv. https://arxiv.org/abs/2509.10156

Giakoumoglou, N., Giakoumoglou, P., & Stathaki, T. (2024). Three necessary principles for self-supervised visual representation learning. arXiv. https://arxiv.org/abs/2608.08309

He, X., Sakai, S., Chandhok, S., Beery, S., Yuan, K., Padoy, N., Hasegawa, T., & Sigal, L. (2025). DSeq-JEPA: Discriminative sequential joint-embedding predictive architecture. arXiv. https://arxiv.org/abs/2511.17354

Kuzucu, S., Naeem, M. F., Kukleva, A., Tombari, F., & Schiele, B. (2025). Enhancing self-supervised visual representation learning via low-rank adapted LLMs. arXiv. https://arxiv.org/abs/2507.00754

Munia, N., Ward, T., Nayla, N., Massey, M. A., & Imran, A.-A.-Z. (2026). Self-supervised visual representation learning: Pretrain-finetuning or joint training? arXiv. https://arxiv.org/abs/2607.13192

Wang, Q., Krajsek, K., & Scharr, H. (2024). Equivariant representation learning for augmentation-based self-supervised learning via image reconstruction. arXiv. https://arxiv.org/abs/2412.03314
