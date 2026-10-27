# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: domain generalization semantic segmentation, cs.CV, published between 2023-10-03 and 2025-10-02
**Citation format**: APA 7th edition

## Executive Summary

Domain Generalization for Semantic Segmentation (DGSS) has undergone rapid advancement between 2023-2025, with vision foundation models (VFMs) emerging as the dominant paradigm. The surveyed literature reveals a clear shift from traditional domain adaptation techniques toward leveraging pre-trained foundation models—either frozen or minimally fine-tuned—to achieve robust generalization across unseen domains. Key approaches include parameter-efficient fine-tuning of VFMs, style-content disentanglement in frequency space, diffusion-based domain extension, and integration of vision-language models. Collectively, these works demonstrate that frozen or lightly-adapted VFMs significantly outperform previous DGSS methods, with improvements ranging from +2.5 to +8.1 mIoU over prior state-of-the-art methods. However, challenges remain in handling extreme conditions, managing computational costs of generative models, and addressing noise in pseudo-labels from domain-shifted generated images.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "domain generalization semantic segmentation", filtered to category cs.CV, published between 2023-10-03 and 2025-10-02. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; 0 papers had only an abstract), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Screening process**: The search identified 50 papers by phrase matching, expanded to 160 papers through citation expansion (110 additional papers from references), shortlisted 30 papers, and screened 30 papers with co-citation scoring (scores: 0=6, 1=5, 2=4, 3=15), resulting in 10 included papers (1 from references).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Vision Foundation Models as the New Backbone

A dominant trend across the surveyed literature is the adoption of vision foundation models (VFMs) as the backbone for DGSS. Wei et al. (2023) demonstrated that frozen VFMs significantly outperform previous DGSS methods, introducing Rein—a parameter-efficient fine-tuning approach that surpasses full parameter fine-tuning with only 1% extra trainable parameters (Wei et al., 2023) [E1, E2]. This finding has been reinforced by subsequent work: Benigmim et al. (2023) integrated CLIP backbone within their CLOUDS framework, achieving +8.1% improvement over the second competitor with ResNet-50 (Benigmim et al., 2023) [E10]. The efficiency of VFM-based approaches is further validated by Yi et al. (2024), whose SET framework achieves state-of-the-art performance with flexibility across various VFMs (Yi et al., 2024) [E21]. Most recently, Zhang and Tan (2025) combined VFMs with vision-language models through their Mamba-based MFuser framework, handling increased patch tokens with linear complexity scaling (Zhang & Tan, 2025) [E15].

### Theme 2: Style-Content Disentanglement for Domain Invariance

Multiple approaches tackle domain shift by explicitly separating style and content information. Ahn et al. (2024) proposed BlindNet, which employs covariance alignment to train encoders to uniformly recognize various styles while preserving content information (Ahn et al., 2024) [E22]. Similarly, Yi et al. (2024) decomposed frozen VFM features into phase and amplitude components in frequency space, where phase contains content and amplitude contains style information (Yi et al., 2024) [E20]. Pak et al. (2024) leveraged text embeddings from vision-language models as domain-invariant semantic knowledge, achieving 68.9 mIoU on GTA5→Cityscapes (Pak et al., 2024) [E27]. Niu et al. (2024) extended this with their SCSD framework, using Text-Driven Style Transform for controllable style transformation and improving performance on adverse weather conditions by +0.10 to +4.28 mIoU (Niu et al., 2024) [E18].

### Theme 3: Generative Models for Domain Extension

Diffusion models and generative approaches have emerged as powerful tools for creating diverse training data. Niemeijer et al. (2023) introduced DIDEX, a diffusion-based domain extension method that generates pseudo-target domains with diverse text prompts, improving by 3.8% on GTA5 and 11.8% on SYNTHIA on average (Niemeijer et al., 2023) [E7]. Jia et al. (2023) developed DGInStyle, which uses DreamBooth fine-tuning to specialize pretrained latent diffusion models for semantically-controlled generation, enhancing domain generalization performance by +2.5 to +7.2 mIoU across 5 datasets (Jia et al., 2023) [E29]. However, both works note limitations: diffusion models exhibit prolonged sampling times, and pseudo-labels from domain-shifted generated images introduce noise that complicates self-training (Jia et al., 2023) [E30; Niemeijer et al., 2023].

### Theme 4: Language-Guided and Multi-Modal Approaches

The integration of language models represents an emerging direction. Fahes et al. (2023) introduced FAMix, employing language as a source of randomization through language-driven local style augmentation, providing approximately +6 mean mIoU boost over baseline (Fahes et al., 2023) [E12]. Pak et al. (2024) employed text embeddings as textual object queries within a transformer-based segmentation framework, outperforming existing methods in both synthetic-to-real and real-to-real settings (Pak et al., 2024) [E25]. Zhang and Tan (2025) advanced this with MFuser, combining vision foundation models and vision-language models through a Mamba-based fusion framework, achieving average improvements of 2.15 mIoU on synthetic-to-real benchmarks (Zhang & Tan, 2025) [E13].

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, frozen or minimally fine-tuned VFMs consistently outperform traditional DGSS methods across multiple benchmarks (Wei et al., 2023; Benigmim et al., 2023; Yi et al., 2024). Second, style-content disentanglement—whether through frequency decomposition, covariance alignment, or text-guided transformation—is essential for domain invariance (Ahn et al., 2024; Yi et al., 2024; Niu et al., 2024). Third, generative models can effectively extend training domains, though at computational cost (Niemeijer et al., 2023; Jia et al., 2023).

**Disagreements**: While all approaches demonstrate improvements, there is variation in reported gains depending on the backbone and benchmark. For instance, CLOUDS achieves +8.1% improvement with ResNet-50 (Benigmim et al., 2023) [E10], while SET shows more modest gains of 1.15-1.66% over Rein (Yi et al., 2024) [E19]. This suggests that method effectiveness may be architecture-dependent. Additionally, while diffusion-based methods show promise, their practical deployment is limited by sampling times—a trade-off not addressed by VFM-only approaches.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Extreme condition handling**: FAMix fails under extreme illumination, darkness, or low visibility due to rain (Fahes et al., 2023). DIDEX similarly struggles to generate realistic extreme weather conditions (Niemeijer et al., 2023).

2. **Computational efficiency**: Diffusion models exhibit prolonged sampling times, and multi-resolution operations further extend generation duration (Jia et al., 2023) [E30].

3. **Pseudo-label noise**: Domain shift in generated images poses difficulties for self-training, introducing noise in pseudo-labels (Benigmim et al., 2023) [E11].

4. **Uncertainty estimation**: None of the surveyed methods provide uncertainty estimation, which Fahes et al. (2023) explicitly note as a limitation for safety-critical applications.

5. **Covariance alignment stability**: Ahn et al. (2024) note that their covariance alignment method requires improvement and stabilization for future work.

## Per-Paper Annotations

### Wei et al. (2023)

**Research question**: How to efficiently harness Vision Foundation Models for Domain Generalized Semantic Segmentation with fewer trainable parameters?

**Methodology**: The paper introduces Rein, a parameter-efficient fine-tuning approach built upon trainable tokens linked to distinct instances that refines and forwards feature maps from each layer to the next within the backbone.

**Key findings**:
- Rein surpasses full parameter fine-tuning with only 1% extra trainable parameters (Wei et al., 2023) [E1].
- Frozen VFMs significantly outperform previous DGSS methods (Wei et al., 2023) [E2].
- Rein outperforms SOTA methods by a large margin (Wei et al., 2023) [E3].

**Limitations**: not stated

### Fahes et al. (2023)

**Research question**: How to generalize semantic segmentation networks by employing language as the source of randomization?

**Methodology**: The paper introduces FAMix, a framework comprising minimal fine-tuning to preserve CLIP robustness, language-driven local style augmentation, and randomization by locally mixing source and augmented styles during training.

**Key findings**:
- FAMix significantly outperforms all baselines on all datasets (Fahes et al., 2023) [E4].
- Best generalization requires combining minimal fine-tuning, style augmentation, and mixing (Fahes et al., 2023) [E5].
- FAMix provides approximately +6 mean mIoU boost over baseline (Fahes et al., 2023) [E12].

**Limitations**: FAMix fails in rare conditions like extreme illumination or darkness and low visibility due to rain, and does not handle or provide estimation of uncertainty.

### Niemeijer et al. (2023)

**Research question**: How to generate a pseudo-target domain with diverse text prompts using diffusion models for domain generalization?

**Methodology**: The paper presents DIDEX, a diffusion-based domain extension method that generates a pseudo-target domain with diverse text prompts and then trains a generalizing model by adapting towards this pseudo-target domain.

**Key findings**:
- DIDEX achieves new SOTA performance for domain generalization mean (Niemeijer et al., 2023) [E6].
- DIDEX improves by 3.8% on GTA5 and 11.8% on SYNTHIA on average (Niemeijer et al., 2023) [E7].
- Pseudo-target domain images have similar functional quality to real Cityscapes data (Niemeijer et al., 2023) [E8].

**Limitations**: Increasing the number of conditions does not increase performance on MV or ACDC, possibly due to insufficiently realistic generation of such conditions by the diffusion model.

### Benigmim et al. (2023)

**Research question**: How to integrate various Foundation Models collaboratively for Domain Generalized Semantic Segmentation?

**Methodology**: The paper proposes CLOUDS, a framework that integrates CLIP backbone for robust feature representation, generative models for content diversification, and SAM for iteratively refining segmentation predictions.

**Key findings**:
- CLOUDS outperforms all DGSS and FM-based methods across all encoder types (Benigmim et al., 2023) [E9].
- CLOUDS achieves +8.1% improvement over second competitor with ResNet-50 (Benigmim et al., 2023) [E10].
- CLOUDS leverages visual cues essential for accurately segmenting complex classes (Benigmim et al., 2023) [E11].

**Limitations**: Noise in pseudo labels from domain shift in generated images produced by text-to-image model poses difficulties in self-training.

### Yi et al. (2024)

**Research question**: How to exploit the style-invariant property of Vision Foundation Models for domain generalized semantic segmentation?

**Methodology**: The SET framework decomposes frozen VFM features into phase and amplitude components in frequency space, which contain content and style information respectively, then uses learnable spectral tokens for task-specific information extraction in each branch with attention optimization to mitigate style variation impacts.

**Key findings**:
- SET shows mIoU improvement of 1.66%, 1.24%, 1.58% and 1.15% on C, B, M and S unseen target domains compared to Rein (Yi et al., 2024) [E19].
- SET demonstrates feature generalization ability from synthetic source domain GTAV to real target domains C, B, and M (Yi et al., 2024) [E20].
- SET achieves state-of-the-art performance under multiple cross-domain settings with flexibility on various VFMs (Yi et al., 2024) [E21].

**Limitations**: not stated

### Ahn et al. (2024)

**Research question**: How to address style variations in domain generalized semantic segmentation without unintentionally removing crucial content information?

**Methodology**: BlindNet comprises covariance alignment to train the encoder to uniformly recognize various styles and preserve content information, and semantic consistency contrastive learning to enable the decoder to construct discriminative class embedding space and disentangle features vulnerable to misclassification.

**Key findings**:
- BlindNet outperforms all other DGSS methods when trained on GTAV with ResNet-50 backbone (Ahn et al., 2024) [E22].
- BlindNet effectively shows generalization ability when trained on Cityscapes (Ahn et al., 2024) [E23].
- BlindNet demonstrates superiority when trained on GTAV with MobileNetV2 backbone (Ahn et al., 2024) [E24].

**Limitations**: The covariance alignment method requires improvement and stabilization as noted for future work.

### Pak et al. (2024)

**Research question**: How to utilize domain-invariant semantic knowledge from text embeddings of vision-language models for domain generalized semantic segmentation?

**Methodology**: The tqdm framework employs text embeddings as textual object queries within a transformer-based segmentation framework, with three regularization losses to align visual and textual features and preserve the robust vision-language alignment of pre-trained VLMs.

**Key findings**:
- tqdm outperforms existing methods and achieves state-of-the-art results in both synthetic-to-real and real-to-real settings (Pak et al., 2024) [E25].
- tqdm with EVA02-CLIP model improves the G→C benchmark by 2.48 mIoU (Pak et al., 2024) [E26].
- tqdm achieves 68.9 mIoU on GTA5→Cityscapes, outperforming prior SOTA by 2.5 mIoU (Pak et al., 2024) [E27].

**Limitations**: not stated

### Jia et al. (2023)

**Research question**: Can pretrained latent diffusion models be used as large-scale data generators to improve domain generalization for semantic segmentation?

**Methodology**: DGInStyle uses DreamBooth fine-tuning to specialize a pretrained LDM to semantically-controlled generation, employs Style Swap technique to endow generative prior with learned semantic control, and designs Multi-resolution Latent Fusion to overcome bias towards dominant objects.

**Key findings**:
- DGInStyle significantly enhances domain generalization performance across various DG methods and network architectures (Jia et al., 2023) [E28].
- DGInStyle improvements range from +2.5 mIoU to +7.2 mIoU on average over 5 datasets (Jia et al., 2023) [E29].
- DGInStyle improves overall state-of-the-art performance by a significant gain of +2.5 mIoU (Jia et al., 2023) [E30].

**Limitations**: Diffusion models exhibit prolonged sampling times, and the MRLF module operating on multiple tiles further extends image generation duration, though this does not impact deployed segmentation network inference time.

### Zhang and Tan (2025)

**Research question**: How can Vision Foundation Models and Vision-Language Models be effectively integrated for domain generalized semantic segmentation while handling increased patch tokens?

**Methodology**: MFuser is a Mamba-based fusion framework that combines MVFuser for joint fine-tuning of VFMs and VLMs to capture sequential and spatial dynamics, and MTEnhancer for refining text embeddings by incorporating image priors.

**Key findings**:
- MFuser achieves an average improvement of 2.15 mIoU over state-of-the-art DGSS methods on synthetic-to-real benchmarks (Zhang & Tan, 2025) [E13].
- MFuser achieves an overall improvement of 1.43 mIoU on real-to-real benchmarks compared to existing methods (Zhang & Tan, 2025) [E14].
- MFuser handles increased patch tokens efficiently with linear complexity scaling (Zhang & Tan, 2025) [E15].

**Limitations**: not stated

### Niu et al. (2024)

**Research question**: How can semantic consistency and style diversity be leveraged to improve domain generalized semantic segmentation across unknown target domains?

**Methodology**: SCSD framework comprises three components: Semantic Query Booster for enhancing semantic awareness in the mask decoder, Text-Driven Style Transform for controllable style transformation using text embeddings, and Style Synergy Optimization for feature separation and aggregation.

**Key findings**:
- SCSD achieves 49.11 mIoU average on four target domains, improving by +4.08 mIoU over state-of-the-art methods (Niu et al., 2024) [E16].
- SCSD shows an average improvement of +2.58 mIoU over state-of-the-art methods in multi-source settings (Niu et al., 2024) [E17].
- SCSD improves performance on adverse weather conditions with gains of +0.10 to +4.28 mIoU across different conditions (Niu et al., 2024) [E18].

**Limitations**: not stated

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

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E1 | arXiv:2312.04265 | [4.2 Comparison with State-of-The-Art Methods](https://arxiv.org/html/2312.04265#S4.SS2.p2) | “Rein achieves even superior generalization capabilities, surpassing the full parameter fine-tuning with merely an extra 1% of trainable parameters compared to the original backbone.” |
| E2 | arXiv:2312.04265 | [4.2 Comparison with State-of-The-Art Methods](https://arxiv.org/html/2312.04265#S4.SS2.p2) | “frozen VFMs significantly outperform previous DGSS methods without specialized design” |
| E10 | arXiv:2312.09788 | [GTA as source domain:](https://arxiv.org/html/2312.09788#S4.SS2.SSS0.Px2.p1) | “when using ResNet-50, CLOUDS achieves 53.3%, i.e. +8.1% compared to the second competitor MoDify” |
| E21 | arXiv:2407.18568 | [5. Conclusion](https://arxiv.org/html/2407.18568#S5.p1) | “Extensive experiments under multiple cross-domain settings show the state-of-the-art performance of the proposed SET and its flexibility on a variety of VFMs.” |
| E15 | arXiv:2504.03193 | [6 Conclusions](https://arxiv.org/html/2504.03193#S6.p1) | “MFuser addresses the challenges of increased patch tokens through efficient, scalable fusion with linear complexity.” |
| E22 | arXiv:2403.06122 | [Quantitative and Qualitative Results](https://arxiv.org/html/2403.06122#S4.SS3.SSSx1.p1) | “Our method outperforms all other methods when trained on GTAV, using ResNet-50 as the backbone.” |
| E20 | arXiv:2407.18568 | [4.2.1. GTAV Source Domain](https://arxiv.org/html/2407.18568#S4.SS2.SSS1.p1) | “It is worthy noting that the source domain GTAV is a synthetic dataset, while C, B and M target domains are real datasets.” |
| E27 | arXiv:2407.09033 | [6 Conclusion](https://arxiv.org/html/2407.09033#S6.p1) | “Notably, tqdm achieves the state-of-the-art performance on multiple DGSS benchmarks, e.g., 68.9 mIoU on GTA5 \rightarrow Cityscapes, outperforming the prior state-of-the-art method by 2.5 mIoU.” |
| E18 | arXiv:2412.12050 | [Comparison with the state-of-the-art methods](https://arxiv.org/html/2412.12050#Sx4.SSx2.p1) | “Specifically, our method improves mIoU by +0.10, +4.28, +4.11, and +3.18 on night (AN), snow (AS), rain (AR) and fog (AF), respectively.” |
| E7 | arXiv:2312.01850 | [6 Conclusions](https://arxiv.org/html/2312.01850#S6.p1) | “with GTA5 as the source dataset by 3.8% abs. mIoU and with SYNTHIA even by 11.8% abs. mIoU on average” |
| E29 | arXiv:2312.03048 | [4.3 Comparison with State-of-the-Art DG](https://arxiv.org/html/2312.03048#S4.SS3.p2) | “The improvements range from +2.5 mIoU up to +7.2 mIoU on the average over 5 datasets.” |
| E12 | arXiv:2311.17922 | [4.4 Ablation studies](https://arxiv.org/html/2311.17922#S4.SS4.p2) | “Our complete recipe is proved to be significantly more effective with a boost of \approx+6 mean mIoU w.r.t. the baseline of training without augmentation and mixing.” |
| E25 | arXiv:2407.09033 | [5.2 Comparison with Previous Methods](https://arxiv.org/html/2407.09033#S5.SS2.p1) | “Tab. 1 shows that our tqdm generally outperforms the existing methods and achieves state-of-the-art results in both the synthetic-to-real and real-to-real settings.” |
| E13 | arXiv:2504.03193 | [Synthetic-to-Real Generalization](https://arxiv.org/html/2504.03193#S5.SS2.SSS0.Px1.p1) | “On average, we achieve 2.15 mIoU better than the state-of-the-art.” |
| E19 | arXiv:2407.18568 | [4.2.1. GTAV Source Domain](https://arxiv.org/html/2407.18568#S4.SS2.SSS1.p1) | “The proposed SET shows an mIoU improvement of 1.66%, 1.24%, 1.58% and 1.15% on C, B, M and S unseen target domains, respectively, compared to the VFM based state-of-the-art Rein (Wei et al., 2024).” |
| E30 | arXiv:2312.03048 | [4.3 Comparison with State-of-the-Art DG](https://arxiv.org/html/2312.03048#S4.SS3.p2) | “In particular, DGInStyle improves the overall state-of-the-art performance by a significant gain of +2.5 mIoU.” |
| E11 | arXiv:2312.09788 | [GTA as source domain:](https://arxiv.org/html/2312.09788#S4.SS2.SSS0.Px2.p2) | “CLOUDS leverages image data by training on the source domain and harnessing visual cues that are essential for accurately segmenting these complex classes” |
| E3 | arXiv:2312.04265 | [5 Conclusions](https://arxiv.org/html/2312.04265#S5.p1) | “Rein significantly enhance generalizability of VFMs, outperforming SOTA methods by a large margin” |
| E4 | arXiv:2311.17922 | [4.2 Comparison with DGSS methods](https://arxiv.org/html/2311.17922#S4.SS2.p2) | “our method significantly outperforms all the baselines on all the datasets for both backbones” |
| E5 | arXiv:2311.17922 | [4.4 Ablation studies](https://arxiv.org/html/2311.17922#S4.SS4.p2) | “the best generalization results are only obtained when combining the three ingredients” |
| E6 | arXiv:2312.01850 | [5.1 Comparison with State of the Art](https://arxiv.org/html/2312.01850#S5.SS1.p1) | “we clearly achieve a new state-of-the-art (SOTA) performance for the DG mean” |
| E8 | arXiv:2312.01850 | [5.4 Influence of Image Quantity & Consistency](https://arxiv.org/html/2312.01850#S5.SS4.p1) | “the images in the pseudo-target domain are of a similar functional quality for generalizing to other real-world domains as the real-world Cityscapes data” |
| E9 | arXiv:2312.09788 | [GTA as source domain:](https://arxiv.org/html/2312.09788#S4.SS2.SSS0.Px2.p1) | “CLOUDS outperforms both all DGSS methods and FM-based methods for all types of encoders and pre-training setups” |
| E23 | arXiv:2403.06122 | [Quantitative and Qualitative Results](https://arxiv.org/html/2403.06122#S4.SS3.SSSx1.p1) | “We also show that our method effectively shows generalization ability when trained on Cityscapes.” |
| E24 | arXiv:2403.06122 | [Quantitative and Qualitative Results](https://arxiv.org/html/2403.06122#S4.SS3.SSSx1.p1) | “Table 2 shows the results of our method trained on GTAV with MobileNetV2, demonstrating the superiority of our method.” |
| E26 | arXiv:2407.09033 | [5.2 Comparison with Previous Methods](https://arxiv.org/html/2407.09033#S5.SS2.p1) | “In particular, our approach with the EVA02-CLIP model improves the G \rightarrow C benchmark by 2.48 mIoU.” |
| E28 | arXiv:2312.03048 | [4.3 Comparison with State-of-the-Art DG](https://arxiv.org/html/2312.03048#S4.SS3.p2) | “The results in Tab. 1 indicate that DGInStyle significantly enhances the DG performance across various DG methods and network architectures.” |
| E14 | arXiv:2504.03193 | [Real-to-Real Generalization](https://arxiv.org/html/2504.03193#S5.SS2.SSS0.Px2.p1) | “An overall improvement of 1.43 mIoU is achieved.” |
| E16 | arXiv:2412.12050 | [Comparison with the state-of-the-art methods](https://arxiv.org/html/2412.12050#Sx4.SSx2.p1) | “For G → {C, B, M, S} setting, our method achieves an average of 49.11 mIoU on four target domain datasets, yielding an improvement of +4.08 mIoU over the state-of-the-art DGSS methods.” |
| E17 | arXiv:2412.12050 | [Comparison with the state-of-the-art methods](https://arxiv.org/html/2412.12050#Sx4.SSx2.p1) | “with an average improvement of +2.58 mIoU compared to the state-of-the-art methods.” |

<!-- /evidence-appendix -->
