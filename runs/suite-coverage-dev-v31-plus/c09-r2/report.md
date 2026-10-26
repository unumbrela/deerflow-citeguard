# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Date:** October 26, 2026  
**Search Period:** October 3, 2023 – October 2, 2025  
**Category:** cs.CV (Computer Vision and Pattern Recognition)  
**Total Papers:** 10

---

## Executive Summary

This systematic literature review examines recent advances in Domain Generalized Semantic Segmentation (DGSS) from October 2023 to October 2025. The reviewed literature reveals a significant paradigm shift toward leveraging Vision Foundation Models (VFMs) and multi-modal approaches to address domain shift challenges. Key trends include: (1) parameter-efficient fine-tuning of VFMs, (2) integration of depth and geometric information, (3) vision-language model fusion, (4) spectral and frequency-domain feature decomposition, and (5) diffusion-based data augmentation with quality control mechanisms.

---

## Annotated Bibliography (APA Format)

### 1. Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*.

**Abstract:** This paper proposes CLOUDS, a framework that integrates multiple foundation models for DGSS. The approach combines CLIP backbone for robust feature representation, generative models for content diversification, and Segment Anything Model (SAM) for iterative prediction refinement. The method achieves 5.6% and 6.7% improvements on average mIoU on synthetic-to-real benchmarks and varying weather conditions, respectively.

**Key Contributions:**
- Novel assembly of collaborative foundation models (CLIP, generative models, SAM)
- Content diversification beyond style randomization
- State-of-the-art performance on synthetic-to-real and weather condition benchmarks

**Methodology:** The framework leverages Domain Randomization orthogonally by using foundation models to cover various modes of the target distribution rather than relying solely on style diversification.

---

### 2. Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*.

**Abstract:** This work introduces Rein, a parameter-efficient fine-tuning approach that harnesses VFMs for DGSS. Using trainable tokens linked to distinct instances, Rein refines feature maps within frozen backbones, achieving superior generalizability with only 1% additional trainable parameters. The method reaches 78.4% mIoU on Cityscapes without accessing real urban-scene datasets.

**Key Contributions:**
- Parameter-efficient VFM fine-tuning with minimal trainable parameters
- Instance-specific token-based feature refinement
- Surpassing full parameter fine-tuning performance with fraction of parameters

**Methodology:** The approach produces diverse refinements for different categories within single images through layer-by-layer feature map refinement using trainable tokens.

---

### 3. Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*.

**Abstract:** This study proposes BlindNet, which addresses style-content entanglement by blinding style without external modules. The method employs covariance alignment in the encoder to uniformly recognize various styles while preserving content, and semantic consistency contrastive learning in the decoder to construct discriminative class embedding space.

**Key Contributions:**
- Style blinding without external modules or datasets
- Covariance alignment for style-invariant encoding
- Semantic consistency contrastive learning for decoder robustness

**Methodology:** The encoder is trained to recognize various styles uniformly rather than removing style-sensitive factors, while the decoder builds discriminative embeddings to disentangle features vulnerable to misclassification.

---

### 4. Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*.

**Abstract:** This paper presents SET (Spectral-decomposed Token), a framework that decomposes frozen VFM features into phase and amplitude components in frequency space, representing content and style respectively. The method develops attention optimization to bridge style-affected representation and static tokens during inference, achieving state-of-the-art cross-domain performance.

**Key Contributions:**
- Frequency-space feature decomposition (phase/amplitude)
- Style-invariant token learning from decomposed features
- Attention optimization for style-affected inference

**Methodology:** VFM features are decomposed into content (phase) and style (amplitude) components, with separate token-based processing and attention optimization to handle style variation during inference.

---

### 5. Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*.

**Abstract:** This work introduces SCSD framework addressing limitations of feature normalization and domain randomization approaches. SCSD comprises Semantic Query Booster for cross-domain semantic consistency, Text-Driven Style Transform for controllable style transformation, and Style Synergy Optimization for inter-domain feature separation. Training on GTAV achieved 49.11 mIoU on four unseen domains, surpassing previous SOTA by 4.08 mIoU.

**Key Contributions:**
- Semantic consistency prediction with query enhancement
- Text-driven controllable style transformation
- Style synergy optimization for feature space separation

**Methodology:** The framework enhances semantic awareness in mask decoders, uses domain difference text embeddings to guide style transformation, and applies synergistic weighting of style contrastive and aggregation losses.

---

### 6. Chen, S., Han, T., Zhang, C., Luo, X., Wu, M., Cai, G., & Su, J. (2025). Stronger, Steadier & Superior: Geometric Consistency in Depth VFM Forges Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.12753*.

**Abstract:** This paper proposes DepthForge, integrating depth information with VFM features to improve geometric consistency. The framework incorporates depth-aware learnable tokens in each VFM layer to decouple domain-invariant visual and spatial information, with a depth refinement decoder for multi-layer feature refinement. The method exhibits outstanding performance under extreme conditions (night, snow).

**Key Contributions:**
- Depth VFM integration with visual VFMs
- Depth-aware learnable tokens for spatial information decoupling
- Superior performance under extreme weather conditions

**Methodology:** DepthForge combines frozen DINOv2/EVA02 visual features with frozen Depth Anything V2 depth cues, using depth-aware tokens and refinement decoder for enhanced geometric consistency.

---

### 7. Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*.

**Abstract:** This work proposes MFuser, a Mamba-based fusion framework combining VFMs (DINOv2) and VLMs (CLIP). The approach addresses complementary strengths: VFMs excel at fine-grained features while VLMs provide robust text alignment. MFuser achieves 68.20 mIoU on synthetic-to-real and 71.87 mIoU on real-to-real benchmarks with linear scalability.

**Key Contributions:**
- VFM-VLM fusion via Mamba architecture
- MVFuser co-adapter for joint fine-tuning
- MTEnhancer for text embedding refinement with image priors

**Methodology:** The framework uses MVFuser as co-adapter capturing sequential and spatial dynamics, and MTEnhancer as hybrid attention-Mamba module for text embedding refinement with linear sequence length scalability.

---

### 8. Chen, S., Han, T., Fu, C., Zhang, C., Wang, C., Su, J., Cai, G., & Wu, M. (2025). Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2506.09881*.

**Abstract:** This paper introduces Vireo, the first single-stage framework unifying Open-Vocabulary Semantic Segmentation (OVSS) and DGSS for Open-Vocabulary Domain-Generalized Semantic Segmentation (OV-DGSS). The method incorporates Depth VFMs for domain-invariant structural features and proposes GeoText Prompts, Coarse Mask Prior Embedding, and Domain-Open-Vocabulary Vector Embedding Head for robust cross-domain open-vocabulary recognition.

**Key Contributions:**
- First unified OVSS-DGSS framework
- GeoText Prompts for geometric-textual alignment
- Domain-Open-Vocabulary Vector Embedding Head

**Methodology:** Vireo builds on frozen VFMs with depth integration, using GeoText Prompts to align geometric features with language, CMPE for enhanced gradient flow, and DOV-VEH for structural-semantic feature fusion.

---

### 9. Li, X., & Guo, X. (2025). Multi-Granularity Feature Calibration via VFM for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2508.03007*.

**Abstract:** This work proposes MGFC framework performing coarse-to-fine alignment of VFM features across three granularities: coarse-grained for global contextual semantics, medium-grained for category-level discriminability, and fine-grained for high-frequency spatial detail enhancement. The hierarchical calibration effectively transfers VFM generalization strengths to DGSS tasks.

**Key Contributions:**
- Multi-granularity hierarchical feature calibration
- Coarse-to-fine VFM feature alignment
- High-frequency spatial detail enhancement

**Methodology:** MGFC performs sequential calibration from coarse (scene-level structure) to medium (category discriminability) to fine (spatial details) granularities for robust dense prediction under domain shifts.

---

### 10. Fan, Q., Liu, C., Qiao, Z., & Shen, X. (2025). IELDG: Suppressing Domain-Specific Noise with Inverse Evolution Layers for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2508.19604*.

**Abstract:** This paper addresses diffusion model-generated data defects in DGSS by proposing IELDM, integrating inverse evolution layers (IELs) with Laplacian-based priors to highlight spatial discontinuities and semantic inconsistencies. The work also introduces IELFormer with IELs embedded in decoder and multi-scale frequency fusion module for cross-scale coherence.

**Key Contributions:**
- Inverse evolution layers for defect suppression
- Laplacian-based prior for quality filtering
- Multi-scale frequency fusion for cross-scale coherence

**Methodology:** IELs use Laplacian priors to filter undesirable generative patterns in diffusion-based augmentation, while IELFormer embeds IELs in decoder with MFF module for frequency-domain multi-resolution feature integration.

---

## Thematic Analysis

### Theme 1: Vision Foundation Model Fine-Tuning (4 papers)

**Papers:** Wei et al. (2023), Chen et al. (2025), Zhang & Tan (2025), Li & Guo (2025)

A dominant trend involves parameter-efficient fine-tuning of pre-trained VFMs. Wei et al. (2023) demonstrated that minimal trainable parameters (1%) can surpass full fine-tuning. Chen et al. (2025) extended this by integrating depth VFMs, while Zhang & Tan (2025) combined VFMs with VLMs using Mamba architecture. Li & Guo (2025) introduced hierarchical calibration across feature granularities.

**Common Approach:** Frozen backbone + trainable components (tokens, adapters, calibration modules)

**Performance:** Consistent state-of-the-art results across benchmarks, with particular strength in preserving generalization capacity while adapting to domain-specific tasks.

### Theme 2: Multi-Modal Integration (3 papers)

**Papers:** Benigmim et al. (2023), Chen et al. (2025), Zhang & Tan (2025)

Multi-modal approaches leverage complementary strengths of different model types. Benigmim et al. (2023) combined CLIP, generative models, and SAM. Chen et al. (2025) integrated visual and depth modalities for geometric consistency. Zhang & Tan (2025) fused VFM spatial features with VLM textual alignment.

**Rationale:** Single-modality approaches face inherent limitations; multi-modal integration addresses complementary weaknesses.

### Theme 3: Style-Content Disentanglement (3 papers)

**Papers:** Ahn et al. (2024), Yi et al. (2024), Niu et al. (2024)

These works address the fundamental challenge of separating style variations from semantic content. Ahn et al. (2024) used covariance alignment to blind style without removing content. Yi et al. (2024) employed spectral decomposition in frequency domain. Niu et al. (2024) developed text-driven controllable style transformation.

**Innovation:** Moving beyond simple style randomization to controlled, semantically-aware style manipulation.

### Theme 4: Data Augmentation Quality Control (1 paper)

**Papers:** Fan et al. (2025)

Fan et al. (2025) addressed a critical gap in diffusion-based augmentation: generated data quality. The inverse evolution layers provide mechanistic quality control using Laplacian priors to filter defective samples before training.

**Significance:** Addresses error accumulation from training on flawed synthetic data.

### Theme 5: Open-Vocabulary Extension (1 paper)

**Papers:** Chen et al. (2025)

The OV-DGSS framework by Chen et al. (2025) represents an emerging direction combining open-vocabulary recognition with domain generalization, enabling segmentation of unseen categories across unseen domains.

**Future Direction:** Bridges two previously separate research areas for real-world applicability.

---

## Methodological Trends

### Parameter Efficiency
- **2023:** Wei et al. demonstrated 1% trainable parameters can exceed full fine-tuning
- **2024-2025:** Universal adoption of frozen VFM backbones with minimal trainable components

### Multi-Modal Fusion Architecture
- **Early (2023):** Simple ensemble approaches (Benigmim et al.)
- **Late (2025):** Sophisticated fusion mechanisms (Mamba-based in Zhang & Tan; geometric-textual in Chen et al.)

### Feature Decomposition Strategies
- **Spatial-Frequency:** Yi et al. (2024) spectral decomposition
- **Visual-Depth:** Chen et al. (2025) geometric consistency
- **Visual-Textual:** Zhang & Tan (2025) VFM-VLM alignment
- **Multi-Granularity:** Li & Guo (2025) hierarchical calibration

### Quality Assurance Mechanisms
- **Fan et al. (2025):** First work addressing synthetic data quality control in DGSS
- Uses Laplacian-based priors for defect detection

---

## Performance Benchmarks

| Paper | Synthetic-to-Real | Real-to-Real | Notable Conditions |
|-------|------------------|--------------|-------------------|
| Benigmim et al. (2023) | +5.6% mIoU | - | Weather conditions: +6.7% |
| Wei et al. (2023) | - | 78.4% (Cityscapes) | No real urban training data |
| Niu et al. (2024) | 49.11 mIoU (GTAV→4 domains) | - | +4.08 over previous SOTA |
| Zhang & Tan (2025) | 68.20 mIoU | 71.87 mIoU | Linear scalability |
| Chen et al. (2025) [DepthForge] | - | - | Outstanding in night/snow |
| Chen et al. (2025) [Vireo] | - | - | OV-DGSS SOTA |

*Note: Not all papers reported identical benchmark metrics; some emphasized qualitative improvements or specific condition performance.*

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Standardized Benchmarking:** Inconsistent reporting metrics across papers makes direct comparison challenging.

2. **Computational Efficiency:** While parameter efficiency improved, computational overhead of multi-modal fusion remains underexplored.

3. **Real-Time Deployment:** No papers addressed inference speed or real-time application constraints.

4. **Long-Term Domain Adaptation:** All methods assume static domain shift; temporal domain evolution unaddressed.

5. **Failure Mode Analysis:** Limited discussion of scenarios where DGSS methods fail catastrophically.

### Emerging Directions

1. **Open-Vocabulary DGSS:** Chen et al. (2025) pioneered OV-DGSS; likely to expand significantly.

2. **Geometric-Semantic Fusion:** Depth integration (Chen et al., 2025) suggests 3D information critical for robustness.

3. **Frequency-Domain Methods:** Spectral approaches (Yi et al., 2024; Fan et al., 2025) offer new feature manipulation paradigms.

4. **Quality-Controlled Synthesis:** Fan et al. (2025) opened avenue for reliable synthetic data generation.

5. **Mamba Architecture:** Zhang & Tan (2025) demonstrated state-space models for efficient long-sequence modeling in DGSS.

---

## Conclusion

The DGSS field underwent significant transformation between 2023-2025, characterized by:

1. **Paradigm Shift:** From domain randomization to foundation model fine-tuning
2. **Multi-Modal Integration:** Visual, depth, textual, and generative model fusion
3. **Parameter Efficiency:** Minimal trainable components with frozen backbones
4. **Quality Assurance:** Mechanisms for synthetic data validation
5. **Capability Expansion:** Open-vocabulary recognition integration

The reviewed literature demonstrates consistent progress toward robust, generalizable semantic segmentation capable of handling unseen domains. The integration of VFMs, depth information, and language models represents a maturation of the field beyond style-based augmentation toward comprehensive multi-modal understanding.

Future research should address standardized benchmarking, computational efficiency, real-time deployment, and failure mode analysis to enable practical real-world deployment of DGSS systems.

---

## References

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788

Chen, S., Han, T., Fu, C., Zhang, C., Wang, C., Su, J., Cai, G., & Wu, M. (2025). Leveraging Depth and Language for Open-Vocabulary Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2506.09881*. https://arxiv.org/abs/2506.09881

Chen, S., Han, T., Zhang, C., Luo, X., Wu, M., Cai, G., & Su, J. (2025). Stronger, Steadier & Superior: Geometric Consistency in Depth VFM Forges Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.12753*. https://arxiv.org/abs/2504.12753

Fan, Q., Liu, C., Qiao, Z., & Shen, X. (2025). IELDG: Suppressing Domain-Specific Noise with Inverse Evolution Layers for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2508.19604*. https://arxiv.org/abs/2508.19604

Li, X., & Guo, X. (2025). Multi-Granularity Feature Calibration via VFM for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2508.03007*. https://arxiv.org/abs/2508.03007

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568

Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193

---

**Search Methodology:**
- Database: arXiv
- Category: cs.CV (primary category match)
- Date Range: October 3, 2023 – October 2, 2025
- Search Query: "domain generalization semantic segmentation"
- Results: 10 papers retrieved and reviewed
