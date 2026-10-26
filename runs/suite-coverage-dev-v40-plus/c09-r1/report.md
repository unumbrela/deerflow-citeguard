# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Review Period:** October 3, 2023 – October 2, 2025  
**Category:** cs.CV (Computer Vision)  
**Total Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in Domain Generalization for Semantic Segmentation (DGSS) from October 2023 to October 2025. The reviewed papers demonstrate significant progress in leveraging vision foundation models (VFMs), vision-language models (VLMs), diffusion models, and novel architectural innovations to address the challenge of segmenting images from unseen target domains without accessing target data during training. Key trends include parameter-efficient fine-tuning of VFMs, multi-modal integration, diffusion-based domain extension, and frequency-domain feature decomposition.

---

## Methodology

### Search Strategy
- **Database:** arXiv preprint repository
- **Primary Category:** cs.CV (Computer Vision)
- **Date Range:** October 3, 2023 – October 2, 2025
- **Search Query:** "domain generalization semantic segmentation"
- **Selection Criteria:** Papers focusing on domain generalization techniques specifically applied to semantic segmentation tasks

### Screening Process
- Initial pool: 50 papers retrieved
- Citation expansion: 110 additional papers from references checked
- Shortlisted: 30 papers
- Final selection: 10 papers based on centrality to DGSS topic and citation impact

---

## Annotated Bibliography (APA Format)

### 1. Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

**Summary:** This paper introduces Rein, a parameter-efficient fine-tuning approach for harnessing Vision Foundation Models (VFMs) in domain generalized semantic segmentation. The method uses trainable tokens linked to distinct instances to refine feature maps from each layer within a frozen backbone. With only 1% additional trainable parameters, Rein achieves 78.4% mIoU on Cityscapes without accessing real urban-scene datasets, significantly outperforming full parameter fine-tuning and state-of-the-art methods.

**Key Contributions:** Parameter-efficient VFM fine-tuning, instance-linked trainable tokens, layer-wise feature refinement, superior generalizability with minimal trainable parameters.

**Citations:** 14

---

### 2. Fahes, M., Vu, T.-H., Bursuc, A., Pérez, P., & de Charette, R. (2023). A Simple Recipe for Language-guided Domain Generalized Segmentation. *arXiv preprint arXiv:2311.17922*. https://arxiv.org/abs/2311.17922v2

**Summary:** The authors propose FAMix, a framework that employs language as the source of randomization for domain generalization in semantic segmentation. The approach comprises three components: (i) preserving CLIP's intrinsic robustness through minimal fine-tuning, (ii) language-driven local style augmentation, and (iii) randomization by locally mixing source and augmented styles during training. The method achieves state-of-the-art results on various generalization benchmarks.

**Key Contributions:** Language-guided style augmentation, CLIP-based minimal fine-tuning, style mixing randomization, vision-language model integration for DGSS.

**Citations:** 10

---

### 3. Niemeijer, J., Schwonberg, M., Termöhlen, J.-A., Schmidt, N. M., & Fingscheidt, T. (2023). Generalization by Adaptation: Diffusion-Based Domain Extension for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.01850*. https://arxiv.org/abs/2312.01850v1

**Summary:** This paper presents DIDEX, a diffusion-based domain extension method that generates pseudo-target domains with diverse text prompts. Unlike existing methods, DIDEX allows control over style and content of generated images while introducing high diversity. The approach adapts models toward the pseudo-target domain without using any real target data, improving state-of-the-art mIoU by 3.8% on GTA5 and 11.8% on SYNTHIA benchmarks.

**Key Contributions:** Diffusion-based domain extension, pseudo-target domain generation, text-prompt control for style/content diversity, significant performance gains on synthetic-to-real benchmarks.

**Citations:** 8

---

### 4. Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

**Summary:** The authors propose CLOUDS, a framework integrating multiple foundation models for DGSS: (i) CLIP backbone for robust feature representation, (ii) generative models for content diversification, and (iii) Segment Anything Model (SAM) for iterative prediction refinement. CLOUDS takes an orthogonal approach to domain randomization by diversifying content rather than just style, outperforming prior methods by 5.6% and 6.7% on averaged mIoU across different benchmarks.

**Key Contributions:** Multi-foundation model collaboration, content diversification beyond style, SAM-based prediction refinement, comprehensive FM integration framework.

**Citations:** 7

---

### 5. Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

**Summary:** This paper introduces the Spectral-decomposed Token (SET) learning framework, which decomposes frozen VFM features into phase and amplitude components in frequency space. Phase components contain content information while amplitude contains style information. The method separately processes these components with learnable tokens and develops an attention optimization method to bridge the gap between style-affected representation and static tokens during inference, achieving state-of-the-art cross-domain performance.

**Key Contributions:** Frequency-domain feature decomposition, phase-amplitude separation, style-invariant token learning, attention optimization for style-affected representations.

**Citations:** 6

---

### 6. Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

**Summary:** The authors propose BlindNet, a novel DGSS approach that blinds style without external modules or datasets. The method comprises two components: (i) covariance alignment that trains the encoder to uniformly recognize various styles while preserving content information, and (ii) semantic consistency contrastive learning that enables the decoder to construct discriminative class embedding space. This approach addresses the limitation of existing methods that struggle with style-content entanglement.

**Key Contributions:** Style-blind feature learning, covariance alignment for style-invariant encoding, semantic consistency contrastive learning, disentangled encoder-decoder architecture.

**Citations:** 6

---

### 7. Pak, B., Woo, B., Kim, S., Kim, D.-h., & Kim, H. (2024). Textual Query-Driven Mask Transformer for Domain Generalized Segmentation. *arXiv preprint arXiv:2407.09033*. https://arxiv.org/abs/2407.09033v2

**Summary:** This paper introduces tqdm, a textual query-driven mask transformer that utilizes domain-invariant semantic knowledge from text embeddings of vision-language models. Text embeddings serve as object queries (textual object queries) for pixel grouping in DGSS. The framework generates textual object queries that maximally encode domain-invariant semantics and enhances semantic clarity of dense visual features through three regularization losses, achieving 68.9 mIoU on GTA5→Cityscapes.

**Key Contributions:** Textual object queries for segmentation, vision-language model integration, domain-invariant semantic extraction, query-driven mask transformer architecture.

**Citations:** 6

---

### 8. Jia, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, K., & Obukhov, A. (2023). DGInStyle: Domain-Generalizable Semantic Segmentation with Image Diffusion Models and Stylized Semantic Control. *arXiv preprint arXiv:2312.03048*. https://arxiv.org/abs/2312.03048v3

**Summary:** The authors propose DGInStyle, an efficient data generation pipeline using large pretrained latent diffusion models (LDMs) for domain-generalizable semantic segmentation. The method includes: (i) specializing pretrained LDMs to semantically-controlled generation within narrow domains, (ii) Style Swap technique for combining generative prior with learned semantic control, and (iii) Multi-resolution Latent Fusion to overcome LDM bias toward dominant objects. The approach consistently increases performance across multiple autonomous driving datasets.

**Key Contributions:** Diffusion-based data generation pipeline, stylized semantic control, Style Swap technique, multi-resolution latent fusion, diverse street scene generation.

**Citations:** 6

---

### 9. Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

**Summary:** This paper proposes MFuser, a Mamba-based fusion framework that efficiently combines Vision Foundation Models (VFMs) and Vision-Language Models (VLMs) for DGSS. MFuser consists of MVFuser (co-adapter for joint fine-tuning capturing sequential and spatial dynamics) and MTEnhancer (hybrid attention-Mamba module for refining text embeddings with image priors). The approach achieves 68.20 mIoU on synthetic-to-real and 71.87 mIoU on real-to-real benchmarks with linear scalability in sequence length.

**Key Contributions:** VFM-VLM fusion via Mamba architecture, co-adaptation mechanism, hybrid attention-Mamba module, linear scalability for long sequences, complementary strength integration.

**Citations:** 4

---

### 10. Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

**Summary:** The authors introduce SCSD framework for Semantic Consistency prediction and Style Diversity generalization. SCSD comprises: (i) Semantic Query Booster for enhancing semantic awareness in mask decoder, (ii) Text-Driven Style Transform module using domain difference text embeddings for controllable style transformation, and (iii) Style Synergy Optimization mechanism preventing similar domain feature space collapse. SCSD achieves 49.11 mIoU on four unseen domain datasets, surpassing previous state-of-the-art by 4.08 mIoU.

**Key Contributions:** Semantic consistency prediction, text-driven controllable style transformation, style synergy optimization, semantic query enhancement, feature space separation and aggregation.

**Citations:** 3

---

## Thematic Analysis

### 1. Vision Foundation Models (VFMs) and Parameter-Efficient Fine-Tuning
Three papers (Wei et al., 2023; Yi et al., 2024; Zhang & Tan, 2025) focus on leveraging VFMs for DGSS. The trend shows a shift toward parameter-efficient approaches that freeze most VFM parameters while training minimal additional components. Wei et al. (2023) demonstrate that just 1% trainable parameters can outperform full fine-tuning, while Yi et al. (2024) introduce frequency-domain decomposition for style-invariant token learning.

### 2. Vision-Language Model Integration
Four papers (Fahes et al., 2023; Pak et al., 2024; Zhang & Tan, 2025; Niu et al., 2024) exploit vision-language models, particularly CLIP, for domain generalization. The common theme is using text embeddings as domain-invariant semantic representations. Language serves multiple roles: style augmentation guide (Fahes et al.), object queries (Pak et al.), fusion bridge (Zhang & Tan), and style transformation controller (Niu et al.).

### 3. Diffusion Models for Domain Extension
Three papers (Niemeijer et al., 2023; Benigmim, 2023; Jia et al., 2023) leverage diffusion models for generating diverse training data. DIDEX (Niemeijer et al.) generates pseudo-target domains, CLOUDS (Benigmim et al.) uses generative models for content diversification, and DGInStyle (Jia et al.) creates stylized semantic-controlled street scenes. All demonstrate that synthetic data generation significantly improves generalization.

### 4. Style-Content Disentanglement
Multiple approaches address the fundamental challenge of separating style from content. Ahn et al. (2024) propose covariance alignment to preserve content while recognizing style variations. Yi et al. (2024) decompose features in frequency space. Niu et al. (2024) introduce controllable style transformation with semantic consistency constraints.

### 5. Multi-Model Collaboration
A emerging trend is combining multiple foundation models for complementary strengths. CLOUDS (Benigmim et al., 2023) integrates CLIP, generative models, and SAM. MFuser (Zhang & Tan, 2025) fuses VFMs and VLMs via Mamba architecture. This reflects recognition that no single model captures all aspects needed for robust generalization.

---

## Performance Comparison

| Method | Key Innovation | Best mIoU | Benchmark |
|--------|---------------|-----------|-----------|
| Rein (Wei et al., 2023) | Parameter-efficient VFM fine-tuning | 78.4% | Cityscapes |
| FAMix (Fahes et al., 2023) | Language-guided style augmentation | SOTA | Multiple benchmarks |
| DIDEX (Niemeijer et al., 2023) | Diffusion-based domain extension | +3.8% improvement | GTA5→Cityscapes |
| CLOUDS (Benigmim et al., 2023) | Multi-FM collaboration | +5.6% avg improvement | Synthetic-to-real |
| SET (Yi et al., 2024) | Spectral-decomposed tokens | SOTA | Cross-domain |
| BlindNet (Ahn et al., 2024) | Covariance alignment | SOTA | Multiple benchmarks |
| tqdm (Pak et al., 2024) | Textual object queries | 68.9% | GTA5→Cityscapes |
| DGInStyle (Jia et al., 2023) | Diffusion data generation | SOTA improvement | Autonomous driving |
| MFuser (Zhang & Tan, 2025) | VFM-VLM Mamba fusion | 71.87% | Real-to-real |
| SCSD (Niu et al., 2024) | Semantic consistency + style diversity | 49.11% | Four unseen domains |

---

## Research Gaps and Future Directions

### Identified Gaps:
1. **Computational Efficiency:** While parameter-efficient methods show promise, the computational cost of using multiple foundation models remains high.
2. **Theoretical Understanding:** Limited theoretical analysis of why certain approaches generalize well across domains.
3. **Domain Shift Characterization:** Insufficient work on characterizing different types of domain shifts and tailoring methods accordingly.
4. **Real-World Deployment:** Most evaluations focus on benchmark datasets; limited validation in real-world deployment scenarios.

### Future Directions:
1. **Adaptive Fusion:** Dynamic selection and fusion of foundation models based on input characteristics.
2. **Causal Reasoning:** Incorporating causal inference to understand domain-invariant mechanisms.
3. **Continual Generalization:** Extending DGSS to continual learning settings where domains arrive sequentially.
4. **Multi-Task Generalization:** Joint generalization across multiple vision tasks beyond segmentation.
5. **Efficient Architectures:** Developing lighter-weight architectures that maintain generalization capabilities.

---

## Conclusion

The reviewed literature demonstrates rapid progress in domain generalized semantic segmentation from 2023 to 2025. Key advances include: (1) parameter-efficient fine-tuning of vision foundation models achieving superior performance with minimal trainable parameters, (2) strategic integration of vision-language models for domain-invariant semantic representations, (3) diffusion models for generating diverse training data with controllable style and content, and (4) novel architectural innovations for style-content disentanglement. The field is moving toward multi-model collaboration frameworks that leverage complementary strengths of different foundation models. Future work should address computational efficiency, theoretical foundations, and real-world deployment validation.

---

## References

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

Fahes, M., Vu, T.-H., Bursuc, A., Pérez, P., & de Charette, R. (2023). A Simple Recipe for Language-guided Domain Generalized Segmentation. *arXiv preprint arXiv:2311.17922*. https://arxiv.org/abs/2311.17922v2

Jia, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, K., & Obukhov, A. (2023). DGInStyle: Domain-Generalizable Semantic Segmentation with Image Diffusion Models and Stylized Semantic Control. *arXiv preprint arXiv:2312.03048*. https://arxiv.org/abs/2312.03048v3

Niemeijer, J., Schwonberg, M., Termöhlen, J.-A., Schmidt, N. M., & Fingscheidt, T. (2023). Generalization by Adaptation: Diffusion-Based Domain Extension for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.01850*. https://arxiv.org/abs/2312.01850v1

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

Pak, B., Woo, B., Kim, S., Kim, D.-h., & Kim, H. (2024). Textual Query-Driven Mask Transformer for Domain Generalized Segmentation. *arXiv preprint arXiv:2407.09033*. https://arxiv.org/abs/2407.09033v2

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

---

**Review Generated:** October 26, 2026  
**Total Citation Count:** 70 citations across all papers  
**Average Citations per Paper:** 7.0
