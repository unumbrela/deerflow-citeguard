# Systematic Literature Review: Self-Supervised Visual Representation Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "self-supervised visual representation learning", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review surveys 10 recent arXiv papers on self-supervised visual representation learning in the computer vision domain. The surveyed literature reveals a field undergoing significant theoretical and methodological maturation, with researchers addressing fundamental questions about representation collapse, training paradigms, and architectural innovations. Key developments include formal theoretical frameworks establishing necessary principles for avoiding collapse [citation:2608.08309](https://arxiv.org/abs/2608.08309), novel approaches leveraging large language models for visual representation enhancement [citation:2507.00754](https://arxiv.org/abs/2507.00754), and comparative studies between traditional pretrain-finetune pipelines versus joint training approaches [citation:2607.13192](https://arxiv.org/abs/2607.13192). The collective work demonstrates strong progress in both theoretical understanding and practical applications, spanning domains from medical imaging to audio-visual correlation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "self-supervised visual representation learning", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Foundations and Collapse Prevention

A significant thread in recent work focuses on formalizing the theoretical underpinnings of self-supervised learning, particularly around the representation collapse problem. Giakoumoglou et al. (2026) provide rigorous proofs establishing three necessary principles—observation, prediction, and regularization—demonstrating that combining observation and prediction without regularization admits constant encoder as a global minimizer [citation:2608.08309](https://arxiv.org/abs/2608.08309). This theoretical work unifies major self-supervised methods under a single energy decomposition framework.

Complementing this theoretical work, Erdogan et al. (2025) address collapse through architectural innovation with LayerLock, exploiting the observation that ViT layers converge in depth order during training [citation:2509.10156](https://arxiv.org/abs/2509.10156). Their progressive freezing strategy enables non-collapsing latent prediction at scale, achieving superior results on the 4DS perception suite for models up to 4B parameters.

### Theme 2: Training Paradigm Comparisons and Optimization

The field is actively debating optimal training strategies, with Munia et al. (2026) providing systematic empirical comparison between pretrain-then-finetune (PFT) and joint training (JT) paradigms [citation:2607.13192](https://arxiv.org/abs/2607.13192). Their comprehensive study across eight SSL methods and diverse domains reveals that the effectiveness depends critically on task type, labeled data availability, and domain complexity. Joint training shows consistent improvements in data efficiency and robustness in low-label settings, while PFT remains more reliable in specialized domains like medical imaging and remote sensing.

Colton (2025) contributes to optimization understanding by examining feature normalization effects in IJEPA models [citation:2508.02829](https://arxiv.org/abs/2508.02829). The study reveals that feature layer normalization disrupts natural token energy hierarchies, and replacing it with DynTanh activation preserves token energies, improving ImageNet linear probe accuracy from 38% to 42.7%.

### Theme 3: Cross-Modal and Multi-Image Learning

Recent work extends self-supervised visual representation learning beyond single-image contexts. Chen et al. (2025) introduce MiCo, which enables Chain-of-Thought reasoning across multiple images without human-annotated question-answer pairs [citation:2506.22434](https://arxiv.org/abs/2506.22434). By constructing image triplets and using rule-based reinforcement learning, their approach eliminates manual curation needs while achieving significant improvements on multi-image reasoning benchmarks.

Krishnamurthy (2024) demonstrates effective audio-visual representation learning from unlabeled videos [citation:2412.07406](https://arxiv.org/abs/2412.07406). The attention-based method learns relative importance of convolutional features across audio and visual streams, improving audio-visual correlation accuracy by 18% and sound recommendation accuracy by 10% on VGG-Sound.

### Theme 4: Architectural Innovations and Sequential Processing

He et al. (2025) bridge latent predictive and autoregressive learning with DSeq-JEPA, incorporating discriminative sequential ordering into JEPA-style architectures [citation:2511.17354](https://arxiv.org/abs/2511.17354). The method mimics human visual perception by attending selectively from primary to secondary cues, creating curriculum-like semantic progression. This approach demonstrates improved discriminative power across image classification, fine-grained categorization, and detection/segmentation tasks.

Wang et al. (2024) address a critical gap in augmentation-based SSL by integrating image reconstruction tasks [citation:2412.03314](https://arxiv.org/abs/2412.03314). Their cross-attention mechanism facilitates equivariant feature learning without additional parameters, showing significant improvements particularly in scenarios involving combined augmentations.

### Theme 5: Leveraging External Knowledge and Model Fusion

Kuzucu et al. (2025) explore bridging the modality gap between text-centric LLMs and vision-centric ViTs through LAVIE [citation:2507.00754](https://arxiv.org/abs/2507.00754). Their framework co-adapts ViT backbones and LLM fusion blocks using Masked Auto-Encoding, addressing the unstable finetuning that plagues direct fusion approaches. This work represents an efficient pathway to enhancing visual understanding using frozen LLM knowledge.

### Theme 6: Security and Privacy Considerations

Zhu et al. (2025) introduce PartCrop, a unified membership inference method for visual self-supervised encoders [citation:2505.10351](https://arxiv.org/abs/2505.10351). Exploiting shared part-aware capability among models, PartCrop operates in black-box settings where training methods are unknown. Their work quantitatively studies scaling impacts and demonstrates that early stopping, differential privacy, and shrinking crop scale ranges all serve as effective defenses.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of architectural and methodological innovations to prevent representation collapse (Giakoumoglou et al., 2026; Erdogan et al., 2025). There is broad agreement that self-supervised methods benefit from incorporating additional structural constraints—whether through sequential ordering (He et al., 2025), progressive freezing (Erdogan et al., 2025), or equivariant learning (Wang et al., 2024). The surveyed literature also collectively demonstrates that domain-specific considerations significantly impact method effectiveness (Munia et al., 2026).

**Disagreements**: The literature reveals tension between general-purpose and domain-specific approaches. While joint training shows advantages in data efficiency and low-label settings (Munia et al., 2026), the same study acknowledges that pretrain-finetune remains more reliable in specialized domains. This suggests unresolved questions about when to prioritize generalization versus domain adaptation. Additionally, while Kuzucu et al. (2025) advocate for LLM integration, the modality mismatch challenges they identify suggest the field has not yet converged on optimal fusion strategies.

## Gaps and Open Questions

The collective literature reveals several notable gaps:

1. **Theoretical-practical translation**: While Giakoumoglou et al. (2026) provide rigorous theoretical foundations, most papers do not explicitly connect their methods to these principles, suggesting a gap between theory and practice.

2. **Computational efficiency**: Several papers mention scaling to large models (Erdogan et al., 2025 scale to 4B parameters), but systematic analysis of computational trade-offs remains absent from most abstracts.

3. **Evaluation standardization**: The diversity of evaluation benchmarks (ImageNet, VGG-Sound, 4DS suite, medical imaging, crisis response data) suggests the field lacks unified evaluation standards, making cross-method comparison difficult.

4. **Long-term representation stability**: While collapse prevention is well-studied, longer-term stability and degradation of representations over extended training or deployment remains underexplored.

5. **Privacy-security trade-offs**: Zhu et al. (2025) identify effective defenses against membership inference, but the performance-privacy trade-off landscape remains largely unmapped.

## Per-Paper Annotations

### Giakoumoglou et al. (2026)

**Research question**: What are the necessary principles for self-supervised visual representation learning to avoid representation collapse?

**Methodology**: The authors formalize three principles (observation, prediction, regularization) and provide theoretical proofs showing that combining observation and prediction without regularization admits constant encoder as a global minimizer. They pair every theoretical claim with controlled experiments, including patch-retrieval evaluation.

**Key findings**:
- Three non-overlapping objectives are necessary: semantic invariance across augmented views, patch-level spatial prediction, and representational non-degeneracy.
- Combining observation and prediction without regularization admits the constant encoder as a global minimizer under negative-free alignment.
- The two objectives (observation and prediction) are gradient-complementary and structurally non-conflicting at the encoder output.
- The momentum encoder converges to the same fixed point as the online encoder and provides no collapse guarantee at convergence.
- Every major self-supervised method is a special case of a single unified energy decomposition.

**Limitations**: Not stated in abstract.

### Kuzucu et al. (2025)

**Research question**: How can the modality mismatch between text-centric LLMs and vision-centric ViTs be bridged to leverage LLM knowledge for vision-only tasks?

**Methodology**: The authors introduce LAVIE, a framework that co-adapts a ViT backbone and an LLM fusion block by employing Masked Auto-Encoding to pre-train the ViT and concurrently training Low-Rank Adaptation layers within the LLM block using the same MAE objective. Performance is evaluated through extensive experiments on various downstream vision tasks.

**Key findings**:
- Direct fusion of LLM blocks with ViTs often fails due to modality mismatch and suffers from unstable finetuning.
- LAVIE guides the ViT to produce LLM-aligned features and the LLM to effectively interpret visual information through joint optimization.
- The framework significantly improves performance in various downstream vision tasks.
- The approach offers an effective and efficient way to enhance visual understanding using frozen LLM knowledge.

**Limitations**: Not stated in abstract.

### Munia et al. (2026)

**Research question**: Does jointly optimizing self-supervised and supervised objectives during training provide a better alternative to the traditional pretrain-then-finetune pipeline?

**Methodology**: The authors systematically compare two training paradigms: pretraining followed by finetuning (PFT) and joint training (JT) where self-supervised and supervised losses are optimized simultaneously. They evaluate across eight SSL methods and diverse computer vision tasks on natural, medical, crisis response, and remote sensing data under varying percentages of labeled data.

**Key findings**:
- The relative effectiveness of PFT and JT depends strongly on the task, availability of labeled data, and domain complexity.
- Joint training consistently improves data and training efficiency while being robust in low-label settings.
- Pretrain-finetuning is more reliable in more specialized domains.
- The study establishes a comprehensive empirical benchmark for hybrid SSL-based semi-supervised learning.

**Limitations**: Not stated in abstract.

### Erdogan et al. (2025)

**Research question**: Can progressive layer freezing during training accelerate masked autoencoding and enable non-collapsing latent prediction?

**Methodology**: The authors observe that during video MAE training, ViT layers converge in order of depth (shallower first, deeper later) and exploit this by progressively freezing layers according to an explicit schedule. They apply LayerLock to large models up to 4B parameters and evaluate on the 4DS perception suite.

**Key findings**:
- During video MAE training, ViT layers converge in the order of their depth: shallower layers converge early, deeper layers converge late.
- Progressive freezing according to an explicit schedule accelerates standard MAE throughout training.
- The same schedule enables a simple and scalable approach to latent prediction that does not suffer from representation collapse.
- LayerLock results surpass those of non-latent masked prediction on the 4DS perception suite for models up to 4B parameters.

**Limitations**: Not stated in abstract.

### Wang et al. (2024)

**Research question**: Can integrating an image reconstruction task into augmentation-based self-supervised learning facilitate equivariant feature learning without additional parameters?

**Methodology**: The authors propose a cross-attention mechanism to blend features learned from two augmented views and reconstruct one of them as an auxiliary component in augmentation-based SSL algorithms. They evaluate effectiveness through multiple linear regression tasks and downstream applications on 3DIEBench and ImageNet datasets.

**Key findings**:
- Augmentation-based SSL methods excel at learning invariant features but often neglect equivariant ones, reducing generalizability.
- The proposed image reconstruction task facilitates equivariant feature learning without additional parameters.
- The method is adaptable to various datasets and augmented-pair based learning methods.
- Results show significant improvements over standard augmentation-based SSL and state-of-the-art approaches, particularly in scenarios involving combined augmentations.

**Limitations**: Not stated in abstract.

### Colton (2025)

**Research question**: How does feature layer normalization affect the energy hierarchy of visual tokens in IJEPA models?

**Methodology**: The study proposes replacing layer normalization with DynTanh activation in IJEPA to preserve natural token energies. Empirical evaluation was conducted on ImageNet linear probe accuracy and NYU Depth V2 monocular depth estimation.

**Key findings**:
- Feature layer normalization disrupts the natural energy hierarchy of visual tokens by forcing all features to have identical L2 norms.
- IJEPA models trained with feature LN exhibit checkerboard-like artifacts in loss maps.
- Replacing LN with DynTanh preserves token energies and produces a longer-tailed loss distribution.
- ImageNet linear probe accuracy improved from 38% to 42.7% for ViT-Small.
- RMSE reduced by 0.08 on NYU Depth V2 monocular depth estimation.

**Limitations**: Not stated in abstract.

### Chen et al. (2025)

**Research question**: Can self-supervised visual representation learning principles enable Chain-of-Thought reasoning across multiple images without human-annotated question-answer pairs?

**Methodology**: The method constructs image triplets with two augmented views of the same image and one similar but distinct image, then optimizes the model using rule-based reinforcement learning to generate reasoning processes for visual comparison tasks.

**Key findings**:
- Images contain inherent constraints that can serve as supervision for training.
- The approach eliminates the need for manually curated question-answer pairs.
- Visual comparison training generalizes effectively to a wide range of questions.
- Significant improvements achieved on multi-image reasoning benchmarks.
- Strong performance demonstrated on general vision tasks.

**Limitations**: Not stated in abstract.

### He et al. (2025)

**Research question**: Can incorporating discriminative sequential ordering into JEPA-style learning improve the discriminative power and generalizability of visual representations?

**Methodology**: DSeq-JEPA integrates a discriminatively ordered sequential process with JEPA-style learning by identifying primary discriminative regions using attention-derived saliency maps and predicting subsequent regions in discriminative order, creating a curriculum-like semantic progression.

**Key findings**:
- DSeq-JEPA bridges latent predictive and autoregressive self-supervised learning.
- The architecture mimics human visual perception by attending selectively from primary to secondary cues.
- Consistently learns more discriminative representations compared to I-JEPA variants.
- Demonstrated effectiveness across image classification, fine-grained categorization, detection/segmentation, and low-level reasoning tasks.
- Shows improved generalizability across diverse visual tasks.

**Limitations**: Not stated in abstract.

### Zhu et al. (2025)

**Research question**: Can a unified membership inference method attack visual self-supervised models in a black-box setting where training methods and details are unknown?

**Methodology**: PartCrop crops parts of objects in images to query responses within the representation space, exploiting shared part-aware capability among models. PartCrop-v2 introduces two structural improvements for scalability. Defense approaches including early stop, differential privacy, and shrinking crop scale range were evaluated.

**Key findings**:
- PartCrop is effective against self-supervised models with different training protocols and structures.
- The method demonstrates strong generalization across three widely used image datasets.
- Early stop, differential privacy, and shrinking crop scale range are all effective defenses.
- Scaling impacts were quantitatively studied from both data and model aspects.
- PartCrop-v2 improves scalability through two structural enhancements.

**Limitations**: Not stated in abstract.

### Krishnamurthy (2024)

**Research question**: Can self-supervised audio-visual representations learned from unlabeled videos improve sound effect recommendations for visual scenes?

**Methodology**: The approach uses an attention mechanism to learn the relative importance of convolutional features at different resolutions from audio and visual streams, encoding inputs based on their correspondence. Cross-modal contrastive learning was also evaluated for additional performance improvements.

**Key findings**:
- Attention-based representations improve audio-visual correlation accuracy by 18% compared to baseline.
- Sound recommendation accuracy improved by 10% on VGG-Sound dataset.
- Cross-modal contrastive learning further enhances recommendation performance.
- The method works effectively on both public video datasets and challenging gameplay video recordings.
- Self-supervised learning from unlabeled videos enables effective audio-visual representation learning.

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
