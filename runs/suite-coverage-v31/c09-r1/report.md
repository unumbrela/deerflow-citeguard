# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Date:** October 26, 2026  
**Search Period:** October 3, 2023 – October 3, 2025  
**Category:** cs.CV (Computer Vision)  
**Number of Papers:** 10

---

## Executive Summary

This systematic literature review examines recent advances in Domain Generalized Semantic Segmentation (DGSS) from October 2023 to October 2025. The reviewed papers reveal a significant paradigm shift toward leveraging Vision Foundation Models (VFMs) and multi-modal approaches to address domain shift challenges. Key trends include: (1) parameter-efficient fine-tuning of VFMs, (2) integration of depth and geometric information, (3) spectral and frequency-domain feature decomposition, (4) vision-language model fusion, and (5) generative data augmentation with quality control mechanisms.

---

## Annotated Bibliography (APA Format)

### 1. Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

**Methodology:** Proposes CLOUDS, a framework integrating multiple foundation models: CLIP for robust feature representation, generative models for content diversification, and Segment Anything Model (SAM) for iterative prediction refinement.

**Key Contributions:** 
- Novel assembly of collaborative foundation models for DGSS
- Content diversification beyond style randomization
- Achieves 5.6% and 6.7% improvement on averaged mIoU on synthetic-to-real and weather condition benchmarks

**Significance:** Demonstrates the power of combining multiple foundation models rather than relying on single-model approaches.

---

### 2. Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

**Methodology:** Introduces Rein, a parameter-efficient fine-tuning approach using trainable tokens linked to distinct instances for refining feature maps within frozen VFM backbones.

**Key Contributions:**
- Parameter-efficient VFM fine-tuning with only 1% trainable parameters
- Surpasses full parameter fine-tuning performance
- Achieves 78.4% mIoU on Cityscapes without accessing real urban-scene datasets

**Significance:** Establishes that stronger pre-trained models with fewer trainable parameters yield superior generalizability, challenging the paradigm of extensive fine-tuning.

---

### 3. Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

**Methodology:** Proposes BlindNet with covariance alignment in the encoder to preserve content while recognizing various styles, and semantic consistency contrastive learning in the decoder for discriminative class embedding.

**Key Contributions:**
- Style blinding without external modules or datasets
- Covariance alignment for style-invariant feature learning
- Semantic consistency contrastive learning for feature disentanglement

**Significance:** Addresses the style-content entanglement problem by uniformly recognizing styles rather than removing style-sensitive factors.

---

### 4. Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

**Methodology:** Presents SET framework that decomposes frozen VFM features into phase (content) and amplitude (style) components in frequency space, processed separately by learnable tokens.

**Key Contributions:**
- Spectral decomposition for style-content separation
- Attention optimization bridging style-affected representation and static tokens
- Advanced fine-tuning token and frozen backbone paradigm

**Significance:** Introduces frequency-domain analysis to DGSS, providing theoretical grounding for style-content separation.

---

### 5. Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

**Methodology:** Introduces SCSD framework with Semantic Query Booster for cross-domain semantic consistency, Text-Driven Style Transform for controllable style transformation, and Style Synergy Optimization for feature space separation.

**Key Contributions:**
- Semantic consistency prediction mechanism
- Text-driven controllable style transformation
- Style synergy optimization preventing feature space collapse
- Achieves 49.11 mIoU on GTAV to four unseen domains (+4.08 mIoU over prior SOTA)

**Significance:** Addresses limitations of both feature normalization and domain randomization approaches through controlled style diversity.

---

### 6. Chen, S., Han, T., Zhang, C., Luo, X., Wu, M., Cai, G., & Su, J. (2025). Stronger, Steadier & Superior: Geometric Consistency in Depth VFM Forges Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.12753*. https://arxiv.org/abs/2504.12753v3

**Methodology:** Proposes DepthForge integrating visual cues from frozen DINOv2/EVA02 with depth cues from frozen Depth Anything V2, using depth-aware learnable tokens in each VFM layer.

**Key Contributions:**
- Depth-VFM integration for geometric consistency
- Depth-aware learnable tokens for visual-spatial decoupling
- Depth refinement decoder for multi-layer feature enhancement
- Outstanding performance under extreme conditions (night, snow)

**Significance:** Demonstrates that depth information provides more robust geometric consistency than visual cues alone, especially in adverse conditions.

---

### 7. Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

**Methodology:** Introduces MFuser, a Mamba-based fusion framework combining VFMs (DINOv2) and VLMs (CLIP) with MVFuser co-adapter and MTEnhancer hybrid attention-Mamba module.

**Key Contributions:**
- VFM-VLM fusion via Mamba architecture
- Linear scalability in sequence length
- Achieves 68.20 mIoU (synthetic-to-real) and 71.87 mIoU (real-to-real)

**Significance:** First work to effectively bridge VFMs and VLMs for DGSS, addressing computational challenges of attention-based fusion.

---

### 8. Chen, S., Han, T., Fu, C., Zhang, C., Wang, C., Su, J., Cai, G., & Wu, M. (2025). Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2506.09881*. https://arxiv.org/abs/2506.09881v3

**Methodology:** Presents Vireo, a single-stage OV-DGSS framework unifying open-vocabulary segmentation and domain generalization with GeoText Prompts, CMPE, and DOV-VEH components.

**Key Contributions:**
- First unified OV-DGSS framework
- GeoText Prompts aligning geometry with language
- Coarse Mask Prior Embedding for enhanced gradient flow
- Domain-Open-Vocabulary Vector Embedding Head

**Significance:** Pioneers the combination of open-vocabulary recognition with domain generalization, critical for real-world autonomous driving scenarios.

---

### 9. Li, X., & Guo, X. (2025). Multi-Granularity Feature Calibration via VFM for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2508.03007*. https://arxiv.org/abs/2508.03007v1

**Methodology:** Proposes MGFC framework performing coarse-to-fine alignment: coarse-grained for global context, medium-grained for category discriminability, fine-grained for spatial detail enhancement.

**Key Contributions:**
- Hierarchical multi-granularity feature calibration
- Coarse-to-fine VFM feature adaptation
- High-frequency spatial detail enhancement

**Significance:** Addresses the limitation of global-only feature fine-tuning by introducing hierarchical adaptation crucial for dense prediction tasks.

---

### 10. Fan, Q., Liu, C., Qiao, Z., & Shen, X. (2025). IELDG: Suppressing Domain-Specific Noise with Inverse Evolution Layers for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2508.19604*. https://arxiv.org/abs/2508.19604v1

**Methodology:** Introduces IELDM (diffusion-based data augmentation with Inverse Evolution Layers) and IELFormer (segmentation decoder with embedded IELs and multi-scale frequency fusion).

**Key Contributions:**
- Inverse Evolution Layers with Laplacian priors for defect suppression
- Enhanced diffusion model for high-quality data augmentation
- Multi-scale frequency fusion for cross-scale coherence
- Dual application: generative augmentation and decoder enhancement

**Significance:** Addresses the critical issue of structural/semantic defects in diffusion-generated training data through physics-informed filtering mechanisms.

---

## Thematic Analysis

### Theme 1: Vision Foundation Model Integration (6 papers)
The dominant trend is leveraging pre-trained VFMs through parameter-efficient fine-tuning:
- **Wei et al. (2023)**: Rein with trainable tokens (1% parameters)
- **Yi et al. (2024)**: SET with spectral decomposition
- **Chen et al. (2025)**: DepthForge with depth-VFM integration
- **Zhang & Tan (2025)**: MFuser combining VFM-VLM
- **Li & Guo (2025)**: MGFC with multi-granularity calibration
- **Benigmim et al. (2023)**: CLOUDS with multiple foundation models

### Theme 2: Multi-Modal Fusion (3 papers)
Integration of complementary modalities beyond RGB:
- **Depth integration**: Chen et al. (2025) - DepthForge; Chen et al. (2025) - Vireo
- **Language integration**: Zhang & Tan (2025) - MFuser; Chen et al. (2025) - Vireo
- **Geometry-Language alignment**: Chen et al. (2025) - Vireo with GeoText Prompts

### Theme 3: Style-Content Separation (4 papers)
Addressing the fundamental challenge of disentangling style and content:
- **Ahn et al. (2024)**: Covariance alignment for style blinding
- **Yi et al. (2024)**: Spectral decomposition in frequency domain
- **Niu et al. (2024)**: Text-driven controllable style transformation
- **Fan et al. (2025)**: Inverse Evolution Layers for noise suppression

### Theme 4: Generative Augmentation (2 papers)
Using generative models for domain randomization:
- **Benigmim et al. (2023)**: Generative models for content diversification
- **Fan et al. (2025)**: Diffusion models with quality control via IELs

### Theme 5: Emerging Directions (2025)
Recent papers show convergence toward:
- **Open-vocabulary DGSS**: Chen et al. (2025) - Vireo
- **Geometric consistency**: Chen et al. (2025) - DepthForge
- **Mamba architectures**: Zhang & Tan (2025) - MFuser
- **Multi-granularity adaptation**: Li & Guo (2025) - MGFC

---

## Methodological Trends

### Parameter Efficiency
All VFM-based approaches emphasize minimal trainable parameters:
- Token-based fine-tuning (Wei et al., 2023; Yi et al., 2024)
- Frozen backbones with adapters (Chen et al., 2025; Zhang & Tan, 2025)
- Layer-wise integration (Li & Guo, 2025; Fan et al., 2025)

### Evaluation Benchmarks
Common datasets across papers:
- **Source domains**: GTAV, Cityscapes
- **Target domains**: BDD100K, Mapillary, ACDC (weather conditions)
- **Metrics**: mIoU (mean Intersection over Union)

### Performance Improvements
Reported gains over prior SOTA:
- 4.08–6.7 mIoU improvement on standard benchmarks
- Significant gains in adverse conditions (night, snow)
- 78.4% mIoU achieved on Cityscapes without real urban data

---

## Critical Analysis

### Strengths of Current Approaches
1. **Leveraging pre-trained knowledge**: VFMs provide robust features learned from massive datasets
2. **Parameter efficiency**: Minimal fine-tuning reduces overfitting to source domains
3. **Multi-modal robustness**: Depth and language provide complementary invariants
4. **Controllable augmentation**: Quality-controlled generative approaches

### Limitations and Challenges
1. **Computational cost**: Multiple foundation models increase inference overhead
2. **Depth dependency**: Requires accurate depth estimation, which may fail in some scenarios
3. **Limited theoretical grounding**: Most approaches are empirically driven
4. **Evaluation gap**: Limited testing on truly diverse, in-the-wild domains

### Research Gaps
1. **Theoretical analysis**: Need for formal bounds on generalization guarantees
2. **Efficiency**: Real-time deployment considerations underexplored
3. **Failure modes**: Limited analysis of when methods fail
4. **Cross-task transfer**: DGSS insights applied to other dense prediction tasks

---

## Future Directions

Based on the reviewed literature, promising directions include:

1. **Unified frameworks**: Combining OVSS, DGSS, and continual learning
2. **Neural architecture search**: Automated discovery of optimal VFM combinations
3. **Test-time adaptation**: Bridging DGSS with test-time adaptation methods
4. **Causal reasoning**: Understanding causal factors of domain shift
5. **Efficient deployment**: Model compression for edge devices
6. **Benchmark standardization**: Unified evaluation protocols across diverse domains

---

## Conclusion

The field of Domain Generalized Semantic Segmentation has undergone rapid transformation from 2023 to 2025, with Vision Foundation Models emerging as the dominant paradigm. The reviewed papers demonstrate a clear evolution from style randomization approaches to sophisticated multi-modal, parameter-efficient fine-tuning strategies. Key innovations include spectral decomposition, depth integration, vision-language fusion, and quality-controlled generative augmentation.

The convergence toward geometric consistency, open-vocabulary recognition, and hierarchical feature adaptation suggests that future DGSS systems will be increasingly robust, flexible, and deployable in real-world scenarios. However, challenges remain in computational efficiency, theoretical understanding, and comprehensive evaluation across truly diverse domains.

---

## References

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

Chen, S., Han, T., Fu, C., Zhang, C., Wang, C., Su, J., Cai, G., & Wu, M. (2025). Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2506.09881*. https://arxiv.org/abs/2506.09881v3

Chen, S., Han, T., Zhang, C., Luo, X., Wu, M., Cai, G., & Su, J. (2025). Stronger, Steadier & Superior: Geometric Consistency in Depth VFM Forges Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.12753*. https://arxiv.org/abs/2504.12753v3

Fan, Q., Liu, C., Qiao, Z., & Shen, X. (2025). IELDG: Suppressing Domain-Specific Noise with Inverse Evolution Layers for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2508.19604*. https://arxiv.org/abs/2508.19604v1

Li, X., & Guo, X. (2025). Multi-Granularity Feature Calibration via VFM for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2508.03007*. https://arxiv.org/abs/2508.03007v1

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

---

**Report generated:** October 26, 2026  
**Search database:** arXiv  
**Primary category:** cs.CV  
**Total papers reviewed:** 10
