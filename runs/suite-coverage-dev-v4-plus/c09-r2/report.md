# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Review Period:** October 3, 2023 – October 2, 2025  
**Category:** cs.CV (Computer Vision and Pattern Recognition)  
**Date of Review:** October 26, 2026

---

## Executive Summary

This systematic literature review examines 10 key research papers on Domain Generalization for Semantic Segmentation (DGSS) published between October 2023 and October 2025. The review reveals significant advances in leveraging vision foundation models (VFMs), vision-language models (VLMs), diffusion models, and novel architectural approaches to address the fundamental challenge of generalizing semantic segmentation models to unseen target domains without requiring target domain data.

Key trends identified include: (1) parameter-efficient fine-tuning of VFMs, (2) integration of language guidance for style augmentation, (3) diffusion-based domain extension and data generation, (4) collaborative multi-model frameworks, and (5) frequency-domain feature decomposition for style-content separation.

---

## Methodology

### Search Strategy
Papers were identified through arXiv search in the cs.CV category with the query "domain generalization semantic segmentation." The search pool included 50 papers, expanded through citation analysis to 160 total candidates (50 original + 110 from references).

### Selection Criteria
- **Focus:** Domain generalization techniques specifically applied to semantic segmentation tasks
- **Publication Date:** October 3, 2023 – October 2, 2025
- **Category:** cs.CV (primary category)
- **Selection Method:** Co-citation analysis and centrality scoring identified the 10 most influential papers from a shortlist of 30

### Screening Results
- Initial pool: 50 papers
- Citation expansion: +110 papers from references
- Shortlisted: 30 papers
- Final selection: 10 papers (screening scores: 8, 7, 1, 1, 14, 6, 6, 6, 6, 4, 3)

---

## Annotated Bibliography

### 1. Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

**Citations:** 14

This paper introduces Rein, a parameter-efficient fine-tuning approach for leveraging Vision Foundation Models (VFMs) in Domain Generalized Semantic Segmentation. The key innovation is using trainable tokens linked to distinct instances to refine and forward feature maps between backbone layers, producing diverse refinements for different categories within a single image. With only 1% additional trainable parameters within a frozen backbone, Rein achieves 78.4% mIoU on Cityscapes without accessing real urban-scene datasets. The approach demonstrates that stronger pre-trained models with fewer trainable parameters can achieve superior generalizability, significantly outperforming state-of-the-art methods and even full parameter fine-tuning.

**Key Contribution:** Parameter-efficient VFM fine-tuning with instance-linked trainable tokens

---

### 2. Fahes, M., Vu, T.-H., Bursuc, A., Pérez, P., & de Charette, R. (2023). A Simple Recipe for Language-guided Domain Generalized Segmentation. *arXiv preprint arXiv:2311.17922*. https://arxiv.org/abs/2311.17922v2

**Citations:** 10

This work presents a simple yet effective framework for domain generalization by employing language as the source of randomization. The approach leverages CLIP's inherent robustness through minimal fine-tuning, introduces language-driven local style augmentation, and employs randomization by locally mixing source and augmented styles during training. The three-ingredient recipe preserves CLIP's robustness while exploiting the textual modality for style diversification. Extensive experiments report state-of-the-art results on various generalization benchmarks, demonstrating that vision-language models can effectively bridge modalities for improved generalization.

**Key Contribution:** Language-guided style augmentation with minimal CLIP fine-tuning

---

### 3. Niemeijer, J., Schwonberg, M., Termöhlen, J.-A., Schmidt, N. M., & Fingscheidt, T. (2023). Generalization by Adaptation: Diffusion-Based Domain Extension for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.01850*. https://arxiv.org/abs/2312.01850v1

**Citations:** 8

The authors propose DIDEX, a diffusion-based domain extension method that generates a pseudo-target domain using diverse text prompts with diffusion models. Unlike existing methods, DIDEX allows control over both style and content of generated images while introducing high diversity. The method trains a generalizing model by adapting toward this pseudo-target domain without using any real target data. DIDEX outperforms previous approaches by large margins, improving state-of-the-art mIoU by 3.8% absolute on GTA5→Cityscapes and 11.8% on SYNTHIA benchmarks, marking a significant advancement in synthetic-to-real generalization.

**Key Contribution:** Diffusion-based pseudo-target domain generation with text-prompt control

---

### 4. Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

**Citations:** 7

This paper introduces CLOUDS, a framework that integrates multiple foundation models for DGSS: (i) CLIP backbone for robust feature representation, (ii) generative models for content diversification covering various target distribution modes, and (iii) Segment Anything Model (SAM) for iterative prediction refinement. Unlike domain randomization approaches limited to style diversification, CLOUDS takes an orthogonal approach by assembling collaborative foundation models. The framework excels in synthetic-to-real DGSS benchmarks and varying weather conditions, outperforming prior methods by 5.6% and 6.7% on averaged mIoU respectively.

**Key Contribution:** Multi-foundation model collaboration (CLIP + generative models + SAM)

---

### 5. Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

**Citations:** 6

The authors present SET (Spectral-dEcomposed Token), a novel framework focusing on learning style-invariant features from learnable tokens. SET decomposes frozen VFM features into phase and amplitude components in frequency space, where phase contains content information and amplitude contains style information. These components are separately processed by learnable tokens for task-specific extraction. An attention optimization method bridges the gap between style-affected representation and static tokens during inference. The approach achieves state-of-the-art performance in extensive cross-domain experiments by explicitly addressing the style-content entanglement challenge.

**Key Contribution:** Frequency-domain feature decomposition for style-content separation

---

### 6. Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

**Citations:** 6

This study proposes BlindNet, which addresses the limitation of existing DGSS methods that struggle with style-content entanglement. Instead of removing style-sensitive factors, BlindNet comprises two components: covariance alignment trains the encoder to uniformly recognize various styles while preserving content information, and semantic consistency contrastive learning enables the decoder to construct discriminative class embedding space. The approach blinds style without external modules or datasets, alleviating style effects in the encoder while facilitating robust segmentation in the decoder. Extensive experiments demonstrate superior performance and robustness on unseen target domains.

**Key Contribution:** Covariance alignment for style-blind encoding with semantic contrastive learning

---

### 7. Pak, B., Woo, B., Kim, S., Kim, D.-h., & Kim, H. (2024). Textual Query-Driven Mask Transformer for Domain Generalized Segmentation. *arXiv preprint arXiv:2407.09033*. https://arxiv.org/abs/2407.09033v2

**Citations:** 6

This paper introduces tqm (textual query-driven mask transformer), which utilizes domain-invariant semantic knowledge from text embeddings of vision-language models as object queries within a transformer-based segmentation framework. The textual object queries serve as domain-invariant basis for pixel grouping. The framework generates textual object queries that maximally encode domain-invariant semantics and enhances semantic clarity of dense visual features through three regularization losses aligning visual and textual features. The method achieves 68.9 mIoU on GTA5→Cityscapes, outperforming prior state-of-the-art by 2.5 mIoU, and demonstrates generalization to extreme domains including sketch-style images.

**Key Contribution:** Text embeddings as domain-invariant object queries in mask transformers

---

### 8. Jia, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, K., & Obukhov, A. (2023). DGInStyle: Domain-Generalizable Semantic Segmentation with Image Diffusion Models and Stylized Semantic Control. *arXiv preprint arXiv:2312.03048*. https://arxiv.org/abs/2312.03048v3

**Citations:** 6

DGInStyle investigates the use of large pretrained latent diffusion models (LDMs) as data generators for semantic segmentation in autonomous driving contexts. The pipeline includes: (1) specializing pretrained LDMs to semantically-controlled generation within narrow domains, (2) Style Swap technique to endow generative priors with learned semantic control, and (3) Multi-resolution Latent Fusion to overcome LDM bias toward dominant objects. The approach generates diverse street scene datasets for training domain-agnostic segmentation models, consistently increasing performance across multiple autonomous driving datasets compared to previous state-of-the-art methods.

**Key Contribution:** LDM-based data generation with stylized semantic control for autonomous driving

---

### 9. Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

**Citations:** 4

This recent work proposes MFuser, a Mamba-based fusion framework that efficiently combines VFMs (e.g., DINOv2) and VLMs (e.g., CLIP) while maintaining linear scalability in sequence length. MFuser consists of MVFuser (co-adapter capturing sequential and spatial dynamics for joint fine-tuning) and MTEnhancer (hybrid attention-Mamba module refining text embeddings with image priors). The approach addresses the challenge that existing methods rely exclusively on either VFMs or VLMs, overlooking their complementary strengths. MFuser achieves 68.20 mIoU on synthetic-to-real and 71.87 mIoU on real-to-real benchmarks, significantly outperforming state-of-the-art DGSS methods.

**Key Contribution:** Mamba-based VFM-VLM fusion with linear sequence scalability

---

### 10. Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

**Citations:** 3

This paper introduces SCSD (Semantic Consistency prediction and Style Diversity generalization) to address limitations in feature normalization and domain randomization approaches. SCSD comprises three components: (1) Semantic Query Booster enhancing semantic awareness in mask decoder for cross-domain consistency, (2) Text-Driven Style Transform using domain difference text embeddings for controllable style transformation, and (3) Style Synergy Optimization preventing similar domain feature space collapse through weighted style contrastive and aggregation losses. SCSD achieves 49.11 mIoU average on four unseen domains from GTAV training, surpassing previous state-of-the-art by +4.08 mIoU.

**Key Contribution:** Semantic consistency with text-driven controllable style transformation

---

## Thematic Analysis

### Theme 1: Vision Foundation Models and Parameter-Efficient Fine-Tuning

Three papers prominently feature VFMs as the backbone for DGSS. Wei et al. (2023) demonstrate that parameter-efficient fine-tuning with only 1% trainable parameters can surpass full fine-tuning. Yi et al. (2024) extend this by decomposing VFM features in frequency space for style-content separation. Zhang & Tan (2025) bridge VFMs with VLMs using Mamba architectures, achieving linear scalability.

**Consensus:** VFMs provide strong generalization capabilities, but efficient adaptation strategies are crucial for optimal performance.

### Theme 2: Vision-Language Models and Textual Guidance

Four papers leverage vision-language models, particularly CLIP. Fahes et al. (2023) use language for style randomization. Pak et al. (2024) employ text embeddings as domain-invariant object queries. Zhang & Tan (2025) fuse VLMs with VFMs. Niu et al. (2024) use text embeddings for controllable style transformation.

**Consensus:** Textual modalities provide domain-invariant semantic knowledge that enhances generalization to unseen domains.

### Theme 3: Diffusion Models for Domain Extension and Data Generation

Two papers utilize diffusion models. Niemeijer et al. (2023) generate pseudo-target domains with text-prompt control. Jia et al. (2023) create diverse training datasets using LDMs with semantic control. Both approaches demonstrate that synthetic data generation can significantly improve generalization without requiring real target data.

**Consensus:** Diffusion models enable controllable domain extension and data augmentation, addressing data scarcity in target domains.

### Theme 4: Style-Content Disentanglement

Multiple approaches address the fundamental challenge of separating style from content. Yi et al. (2024) use frequency decomposition. Ahn et al. (2024) employ covariance alignment. Niu et al. (2024) develop text-driven style transformation with semantic consistency.

**Consensus:** Explicit style-content separation is critical for domain generalization, with various mathematical frameworks achieving this goal.

### Theme 5: Multi-Model Collaboration

Benigmim et al. (2023) and Zhang & Tan (2025) demonstrate that combining multiple foundation models (CLIP, SAM, DINOv2, generative models) yields superior performance compared to single-model approaches.

**Consensus:** Collaborative frameworks leveraging complementary strengths of different foundation models outperform specialized single approaches.

---

## Performance Comparison

| Paper | Method | Key Benchmark | mIoU | Improvement |
|-------|--------|---------------|------|-------------|
| Wei et al. (2023) | Rein (VFM fine-tuning) | Cityscapes | 78.4% | Surpasses full fine-tuning |
| Niemeijer et al. (2023) | DIDEX (Diffusion) | GTA5→Cityscapes | +3.8% | Absolute improvement |
| Niemeijer et al. (2023) | DIDEX (Diffusion) | SYNTHIA→Cityscapes | +11.8% | Absolute improvement |
| Benigmim et al. (2023) | CLOUDS (Multi-FM) | Synthetic→Real | +5.6-6.7% | Averaged mIoU |
| Pak et al. (2024) | tqm (Text queries) | GTA5→Cityscapes | 68.9 | +2.5 over SOTA |
| Zhang & Tan (2025) | MFuser (Mamba fusion) | Synthetic→Real | 68.20 | SOTA performance |
| Zhang & Tan (2025) | MFuser (Mamba fusion) | Real→Real | 71.87 | SOTA performance |
| Niu et al. (2024) | SCSD | GTAV→4 domains | 49.11 | +4.08 over SOTA |

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Computational Efficiency:** While parameter-efficient methods show promise, the computational cost of leveraging multiple foundation models remains high, particularly for real-time applications.

2. **Extreme Domain Gaps:** Most methods focus on synthetic-to-real or weather variation scenarios. Generalization to more extreme domain shifts (e.g., artistic styles, non-photorealistic renderings) requires further investigation.

3. **Theoretical Understanding:** The mechanisms by which VFMs and VLMs achieve generalization are not fully understood, limiting principled architecture design.

4. **Multi-Target Generalization:** Most approaches optimize for average performance across targets. Methods that can adapt to specific target characteristics without target data warrant exploration.

5. **Evaluation Standardization:** The field lacks unified benchmarks and evaluation protocols, making direct comparison challenging.

### Future Directions

1. **Hybrid Architectures:** Combining frequency-domain analysis, language guidance, and diffusion-based augmentation in unified frameworks.

2. **Test-Time Adaptation:** Integrating domain generalization with test-time adaptation methods for improved target-specific performance.

3. **Foundation Model Evolution:** As VFMs and VLMs continue improving, investigating their zero-shot DGSS capabilities and minimal adaptation requirements.

4. **Causal Reasoning:** Incorporating causal inference to distinguish domain-invariant semantic features from spurious correlations.

5. **Cross-Task Generalization:** Extending DGSS insights to other dense prediction tasks like depth estimation and surface normal prediction.

---

## Conclusion

The systematic review of 10 papers published between October 2023 and October 2025 reveals rapid progress in Domain Generalized Semantic Segmentation. The field has evolved from traditional domain randomization and feature alignment approaches to sophisticated methods leveraging vision foundation models, vision-language models, diffusion models, and collaborative multi-model frameworks.

Key advances include parameter-efficient fine-tuning strategies achieving superior performance with minimal trainable parameters, language-guided approaches exploiting textual modalities for domain-invariant semantics, diffusion-based methods generating diverse pseudo-target domains, and frequency-domain techniques explicitly separating style from content.

The convergence of these approaches suggests that future DGSS systems will likely integrate multiple complementary strategies, leveraging the strengths of different foundation models while maintaining computational efficiency. The consistent outperformance of previous state-of-the-art methods across diverse benchmarks indicates that the field is maturing toward practical deployment in real-world applications where target domain data is unavailable or scarce.

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
**Format:** APA 7th Edition  
**Total Papers Reviewed:** 10  
**Date Range:** October 3, 2023 – October 2, 2025
