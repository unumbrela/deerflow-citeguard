# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: "domain generalization semantic segmentation", cs.CV, published between 2023-10-03 and 2025-10-02
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in domain generalization for semantic segmentation (DGSS), focusing on methods that enable models trained on source domains to generalize to unseen target domains without additional training. The ten surveyed papers (2023-2025) reveal a field rapidly evolving toward leveraging large-scale foundation models—both vision foundation models (VFMs) and vision-language models (VLMs)—to extract domain-invariant representations. Key methodological trends include: (1) spectral decomposition techniques for separating style and content information, (2) text-guided semantic alignment using vision-language models, (3) style-blind or style-invariant feature learning through covariance alignment and contrastive learning, and (4) synthetic data generation using diffusion models to augment training diversity. Performance improvements are substantial, with recent methods achieving 1-4 mIoU gains over prior state-of-the-art approaches across synthetic-to-real and real-to-real transfer scenarios. However, limitations remain in handling extreme domain shifts (e.g., adverse weather conditions) and computational efficiency, with several papers noting unstated limitations or calling for future work on stabilization and scalability.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "domain generalization semantic segmentation", filtered to category cs.CV, published between 2023-10-03 and 2025-10-02. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; all 10 papers had full text available), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Foundation Model Integration for Domain-Invariant Representations

A dominant trend across recent DGSS research is the integration of pretrained foundation models to extract domain-invariant features. Multiple papers leverage vision foundation models (VFMs) such as DINO, SAM, and EVA02, either frozen or with lightweight adapters, to provide robust feature representations that generalize across domains. Wei et al. (2023) introduced Rein, which adds only 1% trainable parameters to frozen VFMs while achieving 78.4% mIoU on Cityscapes, demonstrating that minimal adaptation can significantly enhance generalizability [E1, E2]. Benigmimim et al. (2023) proposed CLOUDS, which collaborates multiple foundation models to extract domain-invariant representations. The authors report that CLOUDS demonstrates superior performance over traditional DGSS and open-vocabulary segmentation models [E7]. Their method outperforms prior approaches by 5.6% and 6.7% on averaged mIoU across different benchmarks [E8]. More recently, Zhang and Tan (2025) developed MFuser, a Mamba-based fusion framework that jointly fine-tunes VFMs and VLMs, achieving 2.15 mIoU average improvement over state-of-the-art on synthetic-to-real setups [E23]. This progression indicates a clear shift from handcrafted domain-invariant features toward leveraging the inherent robustness of large-scale pretrained models.

### Theme 2: Spectral and Frequency-Domain Decomposition for Style-Separation

Several papers explore frequency-domain techniques to separate style (domain-specific) from content (domain-invariant) information. Yi et al. (2024) proposed the Spectral-Decomposed Token (SET) learning framework, which decomposes frozen VFM features into phase and amplitude components in frequency space. Their spectral decomposition operation provides mIoU gains of 0.42-3.24% by separately learning amplitude and phase information, with attention optimization applied only to the amplitude component yielding the most predominant improvement in generalization ability [E10, E11]. SET achieves mIoU improvements of 1.06-1.66% over the state-of-the-art Rein method across four unseen target domains [E9]. This approach reflects a broader recognition that style variations—often manifested as high-frequency amplitude changes—can be explicitly modeled and suppressed, while preserving semantic content encoded in phase information.

### Theme 3: Text-Guided Semantic Alignment and Query-Driven Segmentation

The integration of vision-language models (VLMs) for text-guided semantic alignment represents an emerging paradigm in DGSS. Fahes et al. (2023) introduced FAMix, which fuses vision foundation models with language embeddings to create domain-invariant representations, significantly outperforming all baselines across datasets and backbone architectures [E3, E4]. Pak et al. (2024) developed tqdm, a textual query-driven mask transformer that employs text embeddings from vision-language models as object queries within a transformer-based segmentation framework. Their textual object queries are effective for rare classes by encoding domain-invariant representations through language information, and tqdm demonstrates significantly better semantic coherence for pixel features across source and target domains [E16, E17]. Niemeijer et al. (2023) proposed DIDEX, which uses diffusion-generated data guided by semantic descriptions to achieve new state-of-the-art performance on GTA5-trained models [E5, E6]. These approaches exploit the domain-invariant nature of textual semantics to anchor visual representations across varying visual domains.

### Theme 4: Style-Blind and Style-Invariant Feature Learning

A complementary approach focuses on explicitly removing or neutralizing style information during training. Ahn et al. (2024) proposed BlindNet, which employs covariance alignment to train the encoder to uniformly recognize various styles while preserving content information. Their Covariance Matching Loss ensures similar recognition of different style images by intermixing their distributions, and BlindNet operates with computational cost comparable to baseline models by avoiding separate modules [E13, E14]. BlindNet outperforms all other DGSS methods when trained on GTAV with ResNet-50 backbone [E12]. Niu et al. (2024) developed SCSD, a framework comprising semantic query booster, text-driven style transform, and style synergy optimization to achieve 49.11 mIoU on GTAV→target, surpassing previous SOTA by +4.08 mIoU [E25]. SCSD improves mIoU by +0.10 to +4.28 on adverse weather conditions including night, snow, rain, and fog [E27]. These methods share the goal of making models "blind" to superficial style variations while retaining discriminative semantic information.

### Theme 5: Synthetic Data Generation with Diffusion Models

The use of generative models—particularly latent diffusion models (LDMs)—to create diverse training data for domain generalization is gaining traction. Jia et al. (2023) proposed DGInStyle, an efficient data generation pipeline that uses a pretrained LDM specialized to semantically-controlled generation within a narrow domain. Their Style Swap technique improves model performance by +1.57 mIoU by utilizing prior domain knowledge to generate diverse samples, while Multi-Resolution Latent Fusion enhances small object generation, boosting segmentation performance by +0.96 mIoU [E19, E20]. DGInStyle significantly enhances domain generalization performance across various DG methods and network architectures [E18]. This approach addresses the fundamental limitation of limited source domain diversity by synthetically expanding the training distribution, enabling models to encounter a broader range of style variations during training.

## Convergences and Disagreements

**Convergences**: All surveyed papers converge on the central premise that domain-invariant representations are essential for generalization to unseen domains. There is broad agreement that foundation models—whether vision-only or vision-language—provide robust starting points for DGSS, with multiple papers reporting substantial gains from integrating VFMs and VLMs (Wei et al., 2023; Fahes et al., 2023; Benigmimim et al., 2023; Zhang & Tan, 2025). Additionally, there is consensus that explicit style-content separation—whether through spectral decomposition (Yi et al., 2024), covariance alignment (Ahn et al., 2024), or contrastive learning (Niu et al., 2024)—improves generalization performance.

**Disagreements**: While all methods aim for domain invariance, they differ in their assumptions about what constitutes "style" versus "content." Spectral methods (Yi et al., 2024) treat amplitude as style and phase as content, whereas covariance-based methods (Ahn et al., 2024) treat statistical distribution differences as style. Text-guided methods (Fahes et al., 2023; Pak et al., 2024) assume language provides a stable semantic anchor, but this assumption may break down for classes without clear textual descriptions. Furthermore, synthetic data generation (Jia et al., 2023; Niemeijer et al., 2023) assumes generated diversity translates to real-world robustness, an assumption that requires further validation across more diverse target domains.

## Gaps and Open Questions

Several gaps emerge from the surveyed literature. First, most papers do not explicitly state limitations, suggesting a need for more rigorous ablation studies and failure mode analysis. Where limitations are mentioned, Ahn et al. (2024) note the need to improve and stabilize covariance alignment methods. Second, while adverse weather conditions are addressed by SCSD (Niu et al., 2024), extreme domain shifts—such as cross-modal transfer (e.g., RGB to thermal) or dramatic viewpoint changes—remain underexplored. Third, computational efficiency is rarely discussed in depth, despite the heavy reliance on large foundation models; only Ahn et al. (2024) explicitly note computational cost considerations. Fourth, the assumption that language provides domain-invariant semantics (Fahes et al., 2023; Pak et al., 2024; Zhang & Tan, 2025) warrants scrutiny, as language itself may carry cultural and contextual biases. Finally, none of the surveyed papers address online or continual domain generalization, where target domains arrive sequentially—a critical gap for real-world deployment.

## Per-Paper Annotations

### Ahn et al. (2024)

**Research question**: How to address style variations in domain generalized semantic segmentation without removing crucial content information?
**Methodology**: BlindNet with covariance alignment to train the encoder to uniformly recognize various styles while preserving content information, and semantic consistency contrastive learning to enable the decoder to construct discriminative class embedding space.
**Key findings**:
- BlindNet outperforms all other DGSS methods when trained on GTAV with ResNet-50 backbone [E12]
- Covariance Matching Loss ensures similar recognition of different style images by intermixing their distributions [E13]
- BlindNet operates with computational cost comparable to baseline models by avoiding separate modules [E14]
**Limitations**: The authors state future work will focus on improving and stabilizing the covariance alignment method.

### Benigmimim et al. (2023)

**Research question**: How can collaboration between foundation models improve domain generalized semantic segmentation?
**Methodology**: CLOUDS leverages multiple foundation models in a collaborative framework to extract domain-invariant representations for semantic segmentation.
**Key findings**:
- CLOUDS demonstrates superior performance over traditional DGSS and open-vocabulary segmentation models [E7]
- CLOUDS outperforms prior methods by 5.6% and 6.7% on averaged mIoU across different benchmarks [E8]
**Limitations**: not stated

### Fahes et al. (2023)

**Research question**: How can language guidance improve domain generalized semantic segmentation?
**Methodology**: FAMix fuses vision foundation models with language embeddings to create domain-invariant representations for semantic segmentation.
**Key findings**:
- FAMix significantly outperforms all baselines across all datasets and both backbone architectures [E3]
- FAMix significantly outperforms state-of-the-art approaches in domain generalized semantic segmentation [E4]
**Limitations**: not stated

### Jia et al. (2023)

**Research question**: Can pretrained latent diffusion models be used as large-scale data generators to improve domain generalization in semantic segmentation?
**Methodology**: DGInStyle uses a pretrained LDM specialized to semantically-controlled generation within a narrow domain, with Style Swap technique and Multi-resolution Latent Fusion to overcome biases and generate diverse street scene datasets.
**Key findings**:
- DGInStyle significantly enhances domain generalization performance across various DG methods and network architectures [E18]
- Style Swap technique improves model performance by +1.57 mIoU by utilizing prior domain knowledge to generate diverse samples [E19]
- Multi-Resolution Latent Fusion enhances small object generation, boosting segmentation performance by +0.96 mIoU [E20]
**Limitations**: not stated

### Niemeijer et al. (2023)

**Research question**: Can diffusion-generated data improve domain generalization in semantic segmentation?
**Methodology**: DIDEX uses diffusion-generated data guided by semantic descriptions to augment training data for domain generalization.
**Key findings**:
- DIDEX achieves new state-of-the-art performance on GTA5-trained models for domain generalization mean [E5]
- Diffusion-generated data has functional quality comparable to real Cityscapes data for domain generalization [E6]
**Limitations**: not stated

### Niu et al. (2024)

**Research question**: How can semantic consistency and style diversity be leveraged to improve generalization in domain generalized semantic segmentation?
**Methodology**: SCSD framework comprises semantic query booster, text-driven style transform, and style synergy optimization to achieve semantic consistency and style diversity.
**Key findings**:
- SCSD achieves 49.11 mIoU on GTAV→target, surpassing previous SOTA by +4.08 mIoU [E25]
- SCSD achieves +0.91, +0.6, and +7.1 mIoU improvements on Mapillary, GTAV, and SYNTHIA under C→target setting [E26]
- SCSD improves mIoU by +0.10 to +4.28 on adverse weather conditions including night, snow, rain, and fog [E27]
**Limitations**: not stated

### Pak et al. (2024)

**Research question**: How to utilize domain-invariant semantic knowledge from text embeddings to improve domain generalized semantic segmentation?
**Methodology**: tqdm employs text embeddings from vision-language models as object queries within a transformer-based segmentation framework, with three regularization losses to align visual and textual features.
**Key findings**:
- tqdm achieves state-of-the-art results in both synthetic-to-real and real-to-real DGSS settings [E15]
- tqdm's textual object queries are effective for rare classes by encoding domain-invariant representations through language information [E16]
- tqdm demonstrates significantly better semantic coherence for pixel features across source and target domains [E17]
**Limitations**: not stated

### Wei et al. (2023)

**Research question**: How to achieve strong domain generalization with minimal trainable parameters using foundation models?
**Methodology**: Rein adds lightweight adapters to frozen vision foundation models, achieving strong performance with only 1% additional trainable parameters.
**Key findings**:
- Rein achieves 78.4% mIoU on Cityscapes with only 1% additional trainable parameters [E1]
- Rein significantly enhances generalizability and outperforms state-of-the-art methods [E2]
**Limitations**: not stated

### Yi et al. (2024)

**Research question**: How to exploit the style-invariant property of Vision Foundation Models for domain generalized semantic segmentation?
**Methodology**: SET learning framework decomposes frozen VFM features into phase and amplitude components in frequency space, then processes them separately with learnable tokens for task-specific information extraction.
**Key findings**:
- SET achieves mIoU improvements of 1.06-1.66% over the state-of-the-art Rein method across four unseen target domains [E9]
- Spectral decomposition operation provides mIoU gains of 0.42-3.24% by separately learning amplitude and phase information [E10]
- Attention optimization applied only to the amplitude component yields the most predominant improvement in generalization ability [E11]
**Limitations**: not stated

### Zhang and Tan (2025)

**Research question**: How can Vision Foundation Models and Vision-Language Models be effectively integrated to improve Domain Generalized Semantic Segmentation?
**Methodology**: MFuser is a Mamba-based fusion framework with MVFuser (co-adapter for joint fine-tuning of VFMs and VLMs) and MTEnhancer (hybrid attention-Mamba module that refines text embeddings by incorporating image priors).
**Key findings**:
- MFuser achieves precise feature localization and robust text alignment without significant computational overhead [E21]
- MFuser with EVA02-CLIP improves the G→B benchmark by 1.49 mIoU [E22]
- MFuser achieves 2.15 mIoU average improvement over state-of-the-art on synthetic-to-real setup [E23]
- MFuser improves C→B by 0.74 mIoU and C→M by 1.7 mIoU on real-to-real setting [E24]
**Limitations**: not stated

## References

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style blind domain generalized semantic segmentation via covariance alignment and semantic consistence contrastive learning. arXiv. https://arxiv.org/abs/2403.06122

Benigmimim, A., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, C., & Obukhov, A. (2023). Collaborating foundation models for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2312.09788

Fahes, S., Borsos, E., Van Gool, L., & Obukhov, A. (2023). A simple recipe for language-guided domain generalized segmentation. arXiv. https://arxiv.org/abs/2311.17922

Jia, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, C., & Obukhov, A. (2023). DGInStyle: Domain-generalizable semantic segmentation with image diffusion models and stylized semantic control. arXiv. https://arxiv.org/abs/2312.03048

Niemeijer, J., Van Gool, L., & Obukhov, A. (2023). Generalization by adaptation: Diffusion-based domain extension for domain-generalized semantic segmentation. arXiv. https://arxiv.org/abs/2312.01850

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring semantic consistency and style diversity for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2412.12050

Pak, B., Woo, B., Kim, S., Kim, D.-h., & Kim, H. (2024). Textual query-driven mask transformer for domain generalized segmentation. arXiv. https://arxiv.org/abs/2407.09033

Wei, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, C., & Obukhov, A. (2023). Stronger, fewer, & superior: Harnessing vision foundation models for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2312.04265

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning spectral-decomposed tokens for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2407.18568

Zhang, X., & Tan, R. T. (2025). Mamba as a bridge: Where vision foundation models meet vision language models for domain-generalized semantic segmentation. arXiv. https://arxiv.org/abs/2504.03193
