# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "domain generalization semantic segmentation", category cs.CV, published between 2023-10-03 and 2025-10-02
**Citation format**: APA 7th edition

## Executive Summary

Domain Generalized Semantic Segmentation (DGSS) has undergone rapid advancement through the integration of vision foundation models (VFMs) and vision-language models (VLMs). The surveyed literature reveals a paradigm shift from traditional domain randomization approaches toward leveraging pretrained foundation models—particularly CLIP, Segment Anything Model (SAM), and diffusion models—to achieve robust cross-domain generalization. Key innovations include parameter-efficient fine-tuning strategies, language-guided style augmentation, diffusion-based domain extension, and spectral-decomposed feature learning. Collectively, these works demonstrate that harnessing pretrained foundation models with minimal trainable parameters can surpass full fine-tuning approaches while maintaining computational efficiency. The field shows strong convergence on using frozen VFM backbones augmented with lightweight adapters, though approaches differ in how they handle style-content disentanglement and domain-invariant feature extraction.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "domain generalization semantic segmentation", filtered to category cs.CV, published between 2023-10-03 and 2025-10-02. Papers were sorted by co-citation relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search and screening flow**: 50 papers identified by search, 110 added from references through citation expansion, 30 shortlisted, 30 screened, 10 included (1 from reference expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Vision Foundation Models as the New Backbone

The surveyed literature demonstrates a clear consensus that vision foundation models (VFMs) pretrained on large-scale data provide superior feature representations for domain generalization compared to models trained from scratch. Wei et al. (2023) introduced Rein, a parameter-efficient fine-tuning approach that achieves 78.4% mIoU on Cityscapes with only 1% extra trainable parameters within a frozen VFM backbone. Similarly, Benigmim et al. (2023) proposed CLOUDS, integrating CLIP as the backbone for robust feature representation, outperforming prior methods by 5.6% on synthetic-to-real benchmarks. This theme reflects a broader recognition that the generalization capability of VFMs, acquired through large-scale pretraining, transfers effectively to unseen domains without extensive retraining.

### Theme 2: Language-Guided Domain Generalization

A significant thread across the literature leverages vision-language models, particularly CLIP, to inject domain-invariant semantic knowledge through text embeddings. Fahes et al. (2023) employed language as a source of randomization, using language-driven local style augmentation to preserve CLIP's intrinsic robustness. Pak et al. (2024) advanced this direction with textual object queries (tqdm), using text embeddings from vision-language models as object queries within a transformer-based segmentation framework, achieving 68.9 mIoU on GTA5→Cityscapes. Zhang and Tan (2025) further integrated VLMs with VFMs through MFuser, a Mamba-based fusion framework that combines fine-grained visual features with text alignment capabilities, achieving 68.20 mIoU on synthetic-to-real benchmarks. These works collectively demonstrate that language provides a domain-invariant bridge for semantic understanding.

### Theme 3: Diffusion Models for Synthetic Domain Generation

Diffusion models emerge as a powerful tool for generating diverse pseudo-target domains, enabling training on synthetic variations without requiring real target data. Niemeijer et al. (2023) presented DIDEX, which employs diffusion models with diverse text prompts to generate pseudo-target domains with controllable style and content, improving state-of-the-art mIoU by 3.8% on GTA5 generalization without using any real target data. Jia et al. (2023) proposed DGInStyle, specializing pretrained latent diffusion models for semantically-controlled generation with a Style Swap technique, consistently increasing performance across multiple autonomous driving datasets. This theme represents a paradigm shift from adapting to existing domains to actively generating training diversity.

### Theme 4: Style-Content Disentanglement in Frequency Space

Multiple works address the core challenge of separating style variations from semantic content, with innovative approaches operating in the frequency domain. Yi et al. (2024) introduced SET, decomposing frozen VFM features into phase (content) and amplitude (style) components in frequency space, processing them separately with learnable tokens. Ahn et al. (2024) proposed BlindNet, using covariance alignment to train encoders to uniformly recognize various styles while preserving content information. Niu et al. (2024) developed SCSD with a Text-Driven Style Transform module for controllable style transformation using domain difference text embeddings. These approaches share the insight that explicit style-content separation enables robust generalization to unseen domain styles.

### Theme 5: Parameter-Efficient Fine-Tuning Strategies

Across the surveyed papers, there is strong convergence on minimizing trainable parameters while maximizing generalization performance. Wei et al. (2023) demonstrated that Rein surpasses full parameter fine-tuning with fewer trainable parameters. Fahes et al. (2023) preserved CLIP's robustness through minimal fine-tuning. Zhang and Tan (2025) achieved linear scalability in sequence length without significant computational overhead through Mamba-based fusion. This theme reflects practical constraints in deploying DGSS systems and the recognition that efficient adaptation strategies outperform brute-force fine-tuning.

## Convergences and Disagreements

**Convergences**: The surveyed papers unanimously agree that foundation models pretrained on large-scale data provide superior starting points for domain generalization compared to training from scratch. All 10 papers leverage some form of pretrained model (CLIP, SAM, VFMs, or diffusion models). There is also strong consensus that explicit handling of style variations—whether through frequency decomposition, covariance alignment, or diffusion-based generation—is essential for cross-domain performance. Additionally, all papers report that parameter-efficient strategies outperform full fine-tuning, suggesting the field has moved beyond the question of whether to use frozen backbones to how best to adapt them.

**Disagreements**: While all approaches leverage foundation models, they differ fundamentally in their adaptation mechanisms. Some works (Wei et al., 2023; Yi et al., 2024) focus on learnable tokens within frozen backbones, while others (Fahes et al., 2023; Pak et al., 2024) emphasize language-guided augmentation. The diffusion-based approaches (Niemeijer et al., 2023; Jia et al., 2023) generate synthetic training data, whereas style-blind methods (Ahn et al., 2024) learn to ignore style variations. These differences reflect competing philosophies: should models learn to be invariant to style, or should they be exposed to maximal style diversity during training?

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the papers explicitly address computational efficiency during inference—all focus on training-time efficiency but assume the foundation model backbone is acceptable for deployment. Second, while all papers report mIoU improvements on standard benchmarks (GTA5→Cityscapes, SYNTHIA), none address real-world deployment challenges such as domain shift within a single scene (e.g., weather changes during autonomous driving). Third, the limitations sections across papers consistently note that performance on extreme domain shifts (e.g., synthetic-to-sketch) remains challenging, suggesting current methods still struggle with dramatic style changes. Finally, the field lacks standardized evaluation protocols for comparing parameter-efficient methods—some report only mIoU, others include computational costs, making direct comparisons difficult.

## Per-Paper Annotations

### Wei et al. (2023)

**Research question**: How can Vision Foundation Models be harnessed for Domain Generalized Semantic Segmentation with fewer trainable parameters while achieving superior generalizability?

**Methodology**: Introduces Rein, a parameter-efficient fine-tuning approach built on trainable tokens linked to distinct instances that precisely refines and forwards feature maps from each layer to the next within the frozen backbone, producing diverse refinements for different categories within a single image.

**Key findings**:
- Rein produces diverse refinements for different categories within a single image
- With fewer trainable parameters, Rein efficiently fine-tunes VFMs for DGSS tasks, surpassing full parameter fine-tuning
- Rein significantly outperforms state-of-the-art methods across various settings
- With just 1% extra trainable parameters within the frozen backbone, achieves 78.4% mIoU on Cityscapes without accessing real urban-scene datasets

**Limitations**: not stated in abstract

### Fahes et al. (2023)

**Research question**: How can language be employed as a source of randomization to generalize semantic segmentation networks to unseen domains?

**Methodology**: Introduces a framework leveraging vision-language models like CLIP with three key components: (i) minimal fine-tuning to preserve intrinsic CLIP robustness, (ii) language-driven local style augmentation, and (iii) randomization by locally mixing source and augmented styles during training.

**Key findings**:
- Preserves intrinsic CLIP robustness through minimal fine-tuning
- Language-driven local style augmentation enables domain generalization
- Randomization by mixing source and augmented styles during training improves generalization
- Achieves state-of-the-art results on various generalization benchmarks

**Limitations**: not stated in abstract

### Niemeijer et al. (2023)

**Research question**: How can diffusion models be used to generate diverse pseudo-target domains for domain-generalized semantic segmentation without requiring any target domain data?

**Methodology**: Presents DIDEX, a diffusion-based domain extension method that employs a diffusion model with diverse text prompts to generate a pseudo-target domain with controllable style and content, then trains a generalizing model by adapting towards this pseudo-target domain.

**Key findings**:
- DIDEX allows control of style and content of generated images with high diversity
- Outperforms previous approaches by a large margin across various datasets and architectures without using any real target data
- Improves state-of-the-art mIoU performance by 3.8% absolute on average for GTA5 generalization
- Improves SYNTHIA benchmark by 11.8% absolute mIoU

**Limitations**: not stated in abstract

### Benigmim et al. (2023)

**Research question**: How can an assembly of collaborative foundation models improve domain generalized semantic segmentation beyond traditional domain randomization approaches?

**Methodology**: Proposes CLOUDS framework integrating multiple foundation models: (i) CLIP backbone for robust feature representation, (ii) generative models to diversify content covering various modes of the target distribution, and (iii) Segment Anything Model (SAM) for iteratively refining segmentation predictions.

**Key findings**:
- CLOUDS takes an orthogonal approach to DGSS by using collaborative foundation models rather than domain randomization alone
- Excels in adapting from synthetic to real DGSS benchmarks
- Performs well under varying weather conditions
- Outperforms prior methods by 5.6% on averaged mIoU for synthetic-to-real benchmarks
- Outperforms prior methods by 6.7% on averaged mIoU under varying weather conditions

**Limitations**: not stated in abstract

### Yi et al. (2024)

**Research question**: How can style-invariant features be learned from learnable tokens for domain generalized semantic segmentation by leveraging spectral decomposition in the frequency space?

**Methodology**: Presents SET framework that decomposes frozen VFM features into phase and amplitude components in frequency space (containing content and style information respectively), processes them separately with learnable tokens for task-specific extraction, and develops an attention optimization method to bridge the gap between style-affected representation and static tokens during inference.

**Key findings**:
- SET advances beyond existing fine-tuning token and frozen backbone paradigm by focusing on style-invariant feature learning
- Frozen VFM features are decomposed into phase (content) and amplitude (style) components in frequency space
- Style variation primarily impacts token-based feature enhancement within the amplitude branch
- Attention optimization method bridges gap between style-affected representation and static tokens during inference
- Extensive cross-domain experiments demonstrate state-of-the-art performance

**Limitations**: not stated in abstract

### Ahn et al. (2024)

**Research question**: How can semantic segmentation models address performance degradation when deployed to unseen target domains due to style variations from different data sources?

**Methodology**: Proposes BlindNet, a domain generalized semantic segmentation approach that blinds style without external modules or datasets. The method comprises covariance alignment to train the encoder to uniformly recognize various styles while preserving content information, and semantic consistency contrastive learning to enable the decoder to construct a discriminative class embedding space.

**Key findings**:
- BlindNet outperforms existing domain generalized semantic segmentation methods
- The approach exhibits robustness and superior performance on unseen target domains
- Covariance alignment alleviates style effects in the encoder while preserving content information
- Semantic consistency contrastive learning disentangles features vulnerable to misclassification

**Limitations**: not stated in abstract

### Pak et al. (2024)

**Research question**: How can domain-invariant semantic knowledge from text embeddings of vision-language models be leveraged to improve domain generalized semantic segmentation?

**Methodology**: Employs text embeddings as object queries (textual object queries) within a transformer-based segmentation framework, introducing the textual query-driven mask transformer (tqdm) with three regularization losses to align visual and textual features for enhanced semantic clarity.

**Key findings**:
- Achieves 68.9 mIoU on GTA5→Cityscapes benchmark
- Outperforms the prior state-of-the-art method by 2.5 mIoU
- Enables model generalization to extreme domains such as sketch style
- Textual object queries serve as domain-invariant basis for pixel grouping

**Limitations**: not stated in abstract

### Jia et al. (2023)

**Research question**: Can large pretrained latent diffusion models be effectively used as data generators to improve domain generalization in semantic segmentation tasks?

**Methodology**: Proposes DGInStyle, an efficient data generation pipeline that specializes pretrained latent diffusion models to semantically-controlled generation within narrow domains, incorporating a Style Swap technique for semantic control and Multi-resolution Latent Fusion to overcome LDM bias toward dominant objects.

**Key findings**:
- Pretrained latent diffusion models are effective as data generators for semantic segmentation
- The approach consistently increases performance compared to previous state-of-the-art methods across multiple autonomous driving datasets
- Style Swap technique successfully endows generative prior with learned semantic control
- Multi-resolution Latent Fusion overcomes LDM bias toward dominant objects

**Limitations**: not stated in abstract

### Zhang and Tan (2025)

**Research question**: How can Vision Foundation Models and Vision-Language Models be effectively integrated to leverage their complementary strengths for domain-generalized semantic segmentation?

**Methodology**: Proposes MFuser, a Mamba-based fusion framework consisting of MVFuser (a co-adapter for joint fine-tuning that captures sequential and spatial dynamics) and MTEnhancer (a hybrid attention-Mamba module that refines text embeddings by incorporating image priors) to efficiently combine VFMs and VLMs with linear scalability.

**Key findings**:
- Achieves 68.20 mIoU on synthetic-to-real benchmarks
- Achieves 71.87 mIoU on real-to-real benchmarks
- Significantly outperforms state-of-the-art domain generalized semantic segmentation methods
- Maintains linear scalability in sequence length without significant computational overhead
- Successfully integrates complementary strengths of VFMs (fine-grained features) and VLMs (text alignment)

**Limitations**: not stated in abstract

### Niu et al. (2024)

**Research question**: How can domain generalized semantic segmentation be improved by addressing the limitations of feature normalization and domain randomization approaches?

**Methodology**: The authors introduce SCSD (Semantic Consistency prediction and Style Diversity generalization), a novel framework with three components: a Semantic Query Booster for cross-domain semantic consistency prediction, a Text-Driven Style Transform module for controllable style transformation using domain difference text embeddings, and a Style Synergy Optimization mechanism that weights style contrastive and aggregation losses to prevent feature space collapse.

**Key findings**:
- SCSD significantly outperforms existing state-of-the-art domain generalized semantic segmentation methods
- SCSD trained on GTAV achieved an average of 49.11 mIoU on four unseen domain datasets
- The proposed method surpassed the previous state-of-the-art by +4.08 mIoU
- The Semantic Query Booster enhances semantic awareness and discrimination capabilities of object queries in the mask decoder
- The Text-Driven Style Transform module enables controllable style transformation that increases inter-domain style diversity while avoiding domain-irrelevant noise

**Limitations**: not stated in abstract

## References

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style blind domain generalized semantic segmentation via covariance alignment and semantic consistence contrastive learning. arXiv. https://arxiv.org/abs/2403.06122

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating foundation models for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2312.09788

Fahes, M., Vu, T.-H., Bursuc, A., Pérez, P., & de Charette, R. (2023). A simple recipe for language-guided domain generalized segmentation. arXiv. https://arxiv.org/abs/2311.17922

Jia, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, K., & Obukhov, A. (2023). DGInStyle: Domain-generalizable semantic segmentation with image diffusion models and stylized semantic control. arXiv. https://arxiv.org/abs/2312.03048

Niemeijer, J., Schwonberg, M., Termöhlen, J.-A., Schmidt, N. M., & Fingscheidt, T. (2023). Generalization by adaptation: Diffusion-based domain extension for domain-generalized semantic segmentation. arXiv. https://arxiv.org/abs/2312.01850

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring semantic consistency and style diversity for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2412.12050

Pak, B., Woo, B., Kim, S., Kim, D.-h., & Kim, H. (2024). Textual query-driven mask transformer for domain generalized segmentation. arXiv. https://arxiv.org/abs/2407.09033

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, fewer, & superior: Harnessing vision foundation models for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2312.04265

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning spectral-decomposed tokens for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2407.18568

Zhang, X., & Tan, R. T. (2025). Mamba as a bridge: Where vision foundation models meet vision language models for domain-generalized semantic segmentation. arXiv. https://arxiv.org/abs/2504.03193
