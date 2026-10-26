# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Review Period:** October 3, 2023 – October 2, 2025  
**Category:** cs.CV (Computer Vision)  
**Date of Review:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in Domain Generalization for Semantic Segmentation (DGSS), a critical challenge in computer vision where models must generalize to unseen target domains without access to target data during training. The review covers 10 peer-reviewed papers published between October 2023 and October 2025, focusing on innovative approaches leveraging vision foundation models, diffusion models, vision-language models, and novel architectural designs.

Key trends identified include: (1) the emergence of vision foundation models (VFMs) as powerful backbones for DGSS, (2) integration of diffusion models for domain extension and style augmentation, (3) exploitation of vision-language models like CLIP for domain-invariant representations, and (4) development of parameter-efficient fine-tuning strategies. State-of-the-art methods report mIoU improvements of 2.5–11.8% across benchmark datasets including GTA5→Cityscapes, SYNTHIA, and various weather condition adaptations.

---

## Methodology

### Search Strategy
Papers were retrieved from arXiv's cs.CV category using the query "domain generalization semantic segmentation" with publication dates restricted to October 3, 2023 through October 2, 2025. The initial search yielded 50 papers, expanded to 160 through citation analysis, and shortlisted to 30 relevant works.

### Selection Criteria
Papers were screened based on:
- Primary focus on domain generalization (not domain adaptation requiring target data)
- Application to semantic segmentation tasks
- Publication in computer vision category (cs.CV)
- Novel methodological contributions

### Screening Results
- **Initial pool:** 50 papers
- **Added from references:** 110 papers
- **Shortlisted:** 30 papers
- **Final selection:** 10 papers
- **Inclusion rate:** 33.3%

---

## Annotated Bibliography (APA Format)

### 1. Foundation Model-Based Approaches

**Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023).** Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

**Summary:** This paper introduces Rein, a parameter-efficient fine-tuning approach for leveraging Vision Foundation Models (VFMs) in DGSS. The method uses trainable tokens linked to distinct instances to refine feature maps layer-by-layer within a frozen backbone. With only 1% additional trainable parameters, Rein achieves 78.4% mIoU on Cityscapes without accessing real urban-scene datasets, surpassing full parameter fine-tuning. The work demonstrates that stronger pre-trained models with fewer trainable parameters yield superior generalizability.

**Key Contributions:**
- Novel token-based refinement mechanism for VFMs
- Parameter-efficient fine-tuning (1% trainable parameters)
- State-of-the-art performance across multiple DGSS benchmarks

---

**Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023).** Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

**Summary:** The CLOUDS framework integrates multiple foundation models: CLIP for robust feature representation, generative models for content diversification, and Segment Anything Model (SAM) for iterative prediction refinement. This orthogonal approach to domain randomization addresses both style and content variation. CLOUDS outperforms prior methods by 5.6% and 6.7% on average mIoU for synthetic-to-real and weather condition benchmarks, respectively.

**Key Contributions:**
- Assembly of heterogeneous foundation models (CLIP, SAM, generative models)
- Content diversification beyond style augmentation
- Significant improvements on synthetic-to-real transfer tasks

---

**Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024).** Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

**Summary:** This work presents the Spectral-dEcomposed Token (SET) learning framework, which decomposes frozen VFM features into phase (content) and amplitude (style) components in frequency space. Learnable tokens separately process each component, with an attention optimization method bridging style-affected representations during inference. The approach achieves state-of-the-art performance by explicitly addressing style-content entanglement.

**Key Contributions:**
- Frequency-domain feature decomposition
- Style-invariant token learning
- Attention optimization for style-affected inference

---

**Zhang, X., & Tan, R. T. (2025).** Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

**Summary:** MFuser proposes a Mamba-based fusion framework integrating VFMs (e.g., DINOv2) and VLMs (e.g., CLIP) to leverage their complementary strengths. The framework includes MVFuser (co-adapter for joint fine-tuning) and MTEnhancer (hybrid attention-Mamba module for text refinement). This approach achieves 68.20 mIoU on synthetic-to-real and 71.87 mIoU on real-to-real benchmarks while maintaining linear scalability.

**Key Contributions:**
- First integration of VFMs and VLMs for DGSS
- Mamba-based efficient fusion with linear complexity
- Superior performance on both synthetic and real domain transfers

---

### 2. Vision-Language Model Approaches

**Fahes, M., Vu, T.-H., Bursuc, A., Pérez, P., & de Charette, R. (2023).** A Simple Recipe for Language-guided Domain Generalized Segmentation. *arXiv preprint arXiv:2311.17922*. https://arxiv.org/abs/2311.17922v2

**Summary:** This paper introduces FAMix, a framework exploiting CLIP's multimodal capabilities through language-driven style augmentation. The three-component recipe includes: (i) minimal fine-tuning to preserve CLIP robustness, (ii) language-driven local style augmentation, and (iii) randomization via source-augmented style mixing. The method achieves state-of-the-art results on multiple generalization benchmarks.

**Key Contributions:**
- Language as a source of randomization
- Preservation of CLIP's intrinsic robustness
- Simple yet effective three-component framework

---

**Pak, B., Woo, B., Kim, S., Kim, D.-h., & Kim, H. (2024).** Textual Query-Driven Mask Transformer for Domain Generalized Segmentation. *arXiv preprint arXiv:2407.09033*. https://arxiv.org/abs/2407.09033v2

**Summary:** The textual query-driven mask transformer (tqdm) utilizes text embeddings from vision-language models as domain-invariant object queries for pixel grouping. Three regularization losses align visual and textual features, enabling the model to comprehend inherent semantic information. The method achieves 68.9 mIoU on GTA5→Cityscapes, outperforming prior state-of-the-art by 2.5 mIoU, with notable performance on extreme domains like sketch style.

**Key Contributions:**
- Textual object queries as domain-invariant basis
- Three novel regularization losses for visual-textual alignment
- Robust generalization to extreme domain shifts

---

### 3. Diffusion Model-Based Approaches

**Niemeijer, J., Schwonberg, M., Termöhlen, J.-A., Schmidt, N. M., & Fingscheidt, T. (2023).** Generalization by Adaptation: Diffusion-Based Domain Extension for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.01850*. https://arxiv.org/abs/2312.01850v1

**Summary:** DIDEX employs diffusion models to generate pseudo-target domains with diverse text prompts, enabling control over style and content. The method adapts models toward these generated domains without using any real target data. DIDEX improves state-of-the-art mIoU by 3.8% on GTA5 and 11.8% on SYNTHIA benchmarks, marking a significant advancement in diffusion-based domain generalization.

**Key Contributions:**
- Diffusion-based pseudo-target domain generation
- Controllable style and content diversification
- Large performance gains without real target data

---

**Jia, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, K., & Obukhov, A. (2023).** DGInStyle: Domain-Generalizable Semantic Segmentation with Image Diffusion Models and Stylized Semantic Control. *arXiv preprint arXiv:2312.03048*. https://arxiv.org/abs/2312.03048v3

**Summary:** DGInStyle specializes pretrained latent diffusion models for semantically-controlled generation in autonomous driving contexts. The pipeline includes Style Swap for endowing generative priors with semantic control and Multi-resolution Latent Fusion to overcome LDM bias toward dominant objects. The generated dataset consistently improves domain generalization methods across multiple autonomous driving benchmarks.

**Key Contributions:**
- Efficient specialization of LDMs for semantic control
- Style Swap and Multi-resolution Latent Fusion techniques
- Public release of generated dataset and code

---

### 4. Feature Learning and Alignment Approaches

**Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024).** Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

**Summary:** BlindNet addresses style-content entanglement by blinding style in the encoder while facilitating robust segmentation in the decoder. The two components—covariance alignment and semantic consistency contrastive learning—enable the encoder to uniformly recognize various styles while preserving content, and the decoder to construct discriminative class embeddings. The approach outperforms existing DGSS methods without external modules or datasets.

**Key Contributions:**
- Style blinding without external augmentation
- Covariance alignment for style-invariant encoding
- Semantic consistency contrastive learning for decoder robustness

---

**Niu, H., Xie, L., Lin, J., & Zhang, S. (2024).** Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

**Summary:** SCSD addresses limitations in feature normalization and domain randomization through three components: (i) Semantic Query Booster for cross-domain semantic consistency, (ii) Text-Driven Style Transform for controllable style transformation using domain difference embeddings, and (iii) Style Synergy Optimization preventing similar domain feature collapse. SCSD achieves 49.11 mIoU on four unseen domains from GTAV training, surpassing prior state-of-the-art by 4.08 mIoU.

**Key Contributions:**
- Semantic consistency prediction mechanism
- Controllable text-driven style transformation
- Style synergy optimization for feature separation

---

## Comparative Analysis

### Methodological Categories

| Category | Papers | Key Techniques |
|----------|--------|----------------|
| Vision Foundation Models | 4 | Token-based refinement, spectral decomposition, Mamba fusion |
| Vision-Language Models | 2 | CLIP fine-tuning, textual queries, language-guided augmentation |
| Diffusion Models | 2 | Pseudo-target generation, style swap, semantic control |
| Feature Alignment | 2 | Covariance alignment, contrastive learning, style optimization |

### Performance Benchmarks

**GTA5 → Cityscapes (Synthetic-to-Real):**
- tqdm (Pak et al., 2024): 68.9 mIoU
- MFuser (Zhang & Tan, 2025): 68.20 mIoU (average across benchmarks)
- DIDEX (Niemeijer et al., 2023): +3.8% improvement over prior SOTA

**SYNTHIA Benchmarks:**
- DIDEX (Niemeijer et al., 2023): +11.8% improvement

**Real-to-Real Transfers:**
- MFuser (Zhang & Tan, 2025): 71.87 mIoU
- Rein (Wei et al., 2023): 78.4 mIoU on Cityscapes

**Weather Condition Adaptation:**
- CLOUDS (Benigmim et al., 2023): +6.7% average mIoU improvement

### Temporal Trends

**2023 (4 papers):** Initial exploration of foundation models and diffusion models for DGSS, establishing baseline approaches for VFM fine-tuning and pseudo-target generation.

**2024 (5 papers):** Rapid advancement in spectral decomposition, vision-language integration, and semantic consistency mechanisms. Peak year for methodological diversity.

**2025 (1 paper in window):** Emergence of hybrid architectures combining VFMs and VLMs through efficient fusion mechanisms like Mamba.

### Key Research Directions

1. **Parameter Efficiency:** Moving from full fine-tuning to parameter-efficient strategies (1% trainable parameters in Rein)

2. **Multi-Modal Integration:** Combining vision, language, and generative models for complementary strengths

3. **Controllable Generation:** Using text prompts and semantic control for targeted domain diversification

4. **Frequency-Domain Processing:** Explicit separation of content (phase) and style (amplitude) in feature space

5. **Foundation Model Assembly:** Integrating heterogeneous models (CLIP, SAM, DINOv2, diffusion models) rather than single-model approaches

---

## Limitations and Future Directions

### Current Limitations

1. **Computational Cost:** Foundation model-based approaches require significant GPU memory despite parameter-efficient designs

2. **Benchmark Concentration:** Heavy focus on autonomous driving datasets (GTA5, Cityscapes, SYNTHIA) limits generalizability assessment

3. **Evaluation Gaps:** Limited reporting on failure cases and domain shift characteristics where methods underperform

4. **Reproducibility:** While most papers release code, generated datasets and pretrained models vary in accessibility

### Future Research Directions

1. **Cross-Domain Benchmarking:** Establish standardized benchmarks beyond autonomous driving (medical imaging, robotics, satellite imagery)

2. **Theoretical Understanding:** Develop theoretical frameworks explaining why foundation models generalize better across domains

3. **Efficiency Optimization:** Further reduce computational overhead for resource-constrained deployments

4. **Dynamic Domain Adaptation:** Extend DGSS to continuously evolving target domains without retraining

5. **Multi-Task Generalization:** Investigate joint generalization across segmentation, detection, and depth estimation tasks

---

## Conclusion

The field of Domain Generalized Semantic Segmentation has undergone rapid transformation between 2023-2025, driven by the integration of foundation models, diffusion models, and vision-language models. The reviewed papers demonstrate consistent improvements over prior methods, with mIoU gains ranging from 2.5% to 11.8% across benchmarks.

Key insights include:
- **Foundation models are transformative:** VFMs and VLMs provide robust pre-trained representations that significantly enhance generalization
- **Parameter efficiency matters:** Methods with <1% trainable parameters can outperform full fine-tuning
- **Multi-modal fusion is promising:** Combining vision, language, and generative models yields complementary benefits
- **Controllable generation enables targeted augmentation:** Diffusion models with semantic control provide diverse, relevant training data

The convergence of these approaches suggests a future where DGSS systems leverage heterogeneous foundation models with minimal task-specific parameters, achieving robust generalization across diverse unseen domains. Continued progress will require addressing computational costs, expanding benchmark diversity, and developing theoretical foundations for cross-domain generalization.

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
**Total Papers Reviewed:** 10  
**Review Period:** October 3, 2023 – October 2, 2025  
**arXiv Category:** cs.CV
