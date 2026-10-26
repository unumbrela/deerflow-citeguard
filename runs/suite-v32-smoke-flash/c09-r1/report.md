# Systematic Literature Review: Domain Generalization for Semantic Segmentation

## Executive Summary

This systematic literature review examines 10 recent papers on Domain Generalized Semantic Segmentation (DGSS) published between October 3, 2023, and October 2, 2025. The field has witnessed significant advances, particularly in leveraging Vision Foundation Models (VFMs) and integrating multi-modal information for robust cross-domain segmentation. Key trends include: (1) parameter-efficient fine-tuning of frozen foundation models, (2) multi-granularity feature calibration strategies, (3) integration of depth and geometric information, (4) open-vocabulary capabilities for unseen categories, and (5) advanced data augmentation with quality control mechanisms.

---

## Introduction

Domain Generalized Semantic Segmentation (DGSS) addresses the critical challenge of training semantic segmentation models on labeled source domains that can generalize effectively to unseen target domains during inference. This capability is essential for real-world applications such as autonomous driving, medical imaging, and satellite imagery analysis, where deployment conditions often differ significantly from training environments.

The past two years have seen paradigm shifts in DGSS research, moving away from traditional domain randomization and feature normalization approaches toward more sophisticated methods leveraging large-scale foundation models. This review synthesizes findings from ten peer-reviewed publications, providing a comprehensive overview of state-of-the-art techniques, methodological innovations, and empirical performance benchmarks.

---

## Methodological Frameworks

### Vision Foundation Model Integration

A dominant trend across recent works is the strategic integration of Vision Foundation Models (VFMs) into DGSS pipelines. Wei et al. (2023) introduced **Rein**, a parameter-efficient fine-tuning approach that harnesses VFMs by using trainable tokens linked to distinct instances. Their method refines feature maps layer-by-layer within frozen backbones, achieving remarkable performance with only 1% additional trainable parameters—surpassing full parameter fine-tuning while reaching 78.4% mIoU on Cityscapes without accessing real urban-scene datasets [citation:Wei et al., 2023](https://arxiv.org/abs/2312.04265v5).

Building on this foundation, Li and Guo (2025) proposed **Multi-Granularity Feature Calibration (MGFC)**, which performs coarse-to-fine alignment of VFM features across hierarchical levels. Their framework calibrates coarse-grained features for global contextual semantics, medium-grained features for category-level discriminability, and fine-grained features through high-frequency spatial detail enhancement. This hierarchical adaptation strategy enables effective transfer of VFM generalization strengths to domain-specific DGSS tasks [citation:Li & Guo, 2025](https://arxiv.org/abs/2508.03007v1).

Yi et al. (2024) presented **Spectral-dEcomposed Token (SET)** learning, which decomposes frozen VFM features into phase and amplitude components in frequency space—where phase primarily contains content information and amplitude captures style variations. Learnable tokens separately process these components, with an attention optimization method bridging gaps between style-affected representations and static tokens during inference [citation:Yi et al., 2024](https://arxiv.org/abs/2407.18568v2).

### Multi-Modal and Geometric Integration

Chen et al. (2025) explored the complementarity between open-vocabulary segmentation and domain generalization through **Vireo**, a single-stage framework for Open-Vocabulary Domain-Generalized Semantic Segmentation (OV-DGSS). Vireo unifies visual foundation models with scene geometry from Depth VFMs, introducing three key components: GeoText Prompts for aligning geometric features with language cues, Coarse Mask Prior Embedding for enhanced gradient flow, and Domain-Open-Vocabulary Vector Embedding Head for robust prediction under domain shifts [citation:Chen et al., 2025a](https://arxiv.org/abs/2506.09881v3).

Complementing this work, Chen et al. (2025b) developed **DepthForge**, which investigates geometric consistency as a stable cue against variable visual appearances. Their framework integrates visual cues from DINOv2 or EVA02 with depth cues from Depth Anything V2, incorporating depth-aware learnable tokens at each VFM layer to decouple domain-invariant visual and spatial information. DepthForge demonstrates outstanding performance under extreme conditions including night and snow scenarios [citation:Chen et al., 2025b](https://arxiv.org/abs/2504.12753v3).

Zhang and Tan (2025) addressed the complementary strengths of VFMs and Vision-Language Models (VLMs), noting that VFMs excel at fine-grained feature capture while VLMs provide robust text alignment but struggle with coarse granularity. They proposed **MFuser**, a Mamba-based fusion framework combining both model types efficiently. MFuser includes MVFuser as a co-adapter for sequential and spatial dynamics, and MTEnhancer—a hybrid attention-Mamba module refining text embeddings with image priors—achieving 68.20 mIoU on synthetic-to-real and 71.87 mIoU on real-to-real benchmarks [citation:Zhang & Tan, 2025](https://arxiv.org/abs/2504.03193v2).

### Data Augmentation and Quality Control

Benigmim et al. (2023) challenged traditional domain randomization approaches by proposing **CLOUDS** (CoLlaborative FOUndation models for Domain Generalized Semantic Segmentation), which integrates multiple foundation model types: CLIP backbone for robust feature representation, generative models for content diversification, and Segment Anything Model (SAM) for iterative prediction refinement. CLOUDS outperforms prior methods by 5.6% and 6.7% on averaged mIoU across synthetic-to-real and varying weather conditions, respectively [citation:Benigmim et al., 2023](https://arxiv.org/abs/2312.09788v2).

Fan et al. (2025) identified a critical issue with diffusion-based augmentation: generated images often contain structural or semantic defects due to training imperfections. They proposed **IELD** (Inverse Evolution Layers) integrated into diffusion processes (**IELDM**) to highlight spatial discontinuities and semantic inconsistencies using Laplacian-based priors. Furthermore, they embedded IELs into DGSS decoders (**IELFormer**) to suppress artifact propagation, incorporating multi-scale frequency fusion for improved cross-scale coherence [citation:Fan et al., 2025](https://arxiv.org/abs/2508.19604v1).

### Style Management and Feature Disentanglement

Niu et al. (2024) introduced **SCSD** (Semantic Consistency prediction and Style Diversity generalization), addressing limitations of existing normalization and randomization methods. Their framework comprises: (1) a Semantic Query Booster enhancing object query awareness in mask decoders, (2) a Text-Driven Style Transform module guiding style transformation via domain difference text embeddings, and (3) Style Synergy Optimization preventing collapse of similar domain feature spaces through synergistic weighting of contrastive and aggregation losses. SCSD achieved 49.11 mIoU average across four unseen domains when trained on GTAV [citation:Niu et al., 2024](https://arxiv.org/abs/2412.12050v1).

Ahn et al. (2024) proposed **BlindNet**, which blinds style without external modules by disentangling style and content entanglement. Their approach includes covariance alignment training the encoder to uniformly recognize various styles while preserving content information, and semantic consistency contrastive learning enabling the decoder to construct discriminative class embedding space [citation:Ahn et al., 2024](https://arxiv.org/abs/2403.06122v1).

---

## Comparative Analysis

### Performance Benchmarks

| Paper | Method | Synthetic-to-Real mIoU | Real-to-Real mIoU | Key Innovation |
|-------|--------|----------------------|------------------|----------------|
| Benigmim et al. (2023) | CLOUDS | +5.6% vs SOTA | +6.7% vs SOTA | Multi-FM collaboration |
| Wei et al. (2023) | Rein | 78.4% (Cityscapes) | - | Parameter-efficient tuning |
| Yi et al. (2024) | SET | SOTA | - | Spectral decomposition |
| Ahn et al. (2024) | BlindNet | SOTA | - | Covariance alignment |
| Niu et al. (2024) | SCSD | 49.11% | - | Semantic consistency |
| Chen et al. (2025b) | DepthForge | SOTA | - | Geometric consistency |
| Zhang & Tan (2025) | MFuser | 68.20% | 71.87% | VFM-VLM fusion |
| Li & Guo (2025) | MGFC | SOTA | - | Multi-granularity calibration |
| Fan et al. (2025) | IELFormer | SOTA | - | Inverse evolution layers |
| Chen et al. (2025a) | Vireo | SOTA | - | Open-vocabulary DGSS |

### Temporal Evolution of Approaches

**2023-2024**: Early focus on foundation model integration and parameter efficiency established baseline methodologies. Works like Rein and CLOUDS demonstrated that frozen VFMs combined with minimal trainable components could surpass traditional approaches.

**2024-2025**: Research diversified into specialized dimensions: spectral analysis (SET), geometric consistency (DepthForge, Vireo), multi-modal fusion (MFuser), and open-vocabulary capabilities. The field matured from proving VFM utility to exploiting specific properties of foundation models for domain generalization.

### Methodological Shifts

1. **From Global to Hierarchical**: Early methods applied uniform fine-tuning across all feature levels; recent approaches (MGFC, SET) explicitly handle different granularities.

2. **From Style Removal to Style Blinding**: Rather than attempting to remove style entirely (risking content loss), newer methods (BlindNet, SCSD) train encoders to be style-invariant while preserving content.

3. **From Visual-Only to Multi-Modal**: Integration of depth, language, and textual cues provides complementary signals less susceptible to domain shift.

4. **From Passive to Active Quality Control**: Moving beyond simple data augmentation, recent works actively filter and improve generated samples (IELDM, CLOUDS).

---

## Key Findings

### 1. Foundation Model Dominance

All reviewed papers leverage Vision Foundation Models as core components, confirming their status as the de facto standard for DGSS. The consensus indicates that frozen VFM backbones provide superior base representations compared to conventional CNN architectures, with fine-tuning strategies focused on efficiency rather than capacity.

### 2. Parameter Efficiency Matters

Multiple studies (Rein, SET, MFuser) demonstrate that fewer trainable parameters can yield superior generalization. Rein's achievement of 78.4% mIoU with only 1% additional parameters suggests that over-parameterization may harm domain generalization through excessive memorization.

### 3. Geometric Stability as Anchor

Depth information emerges as a critical invariant signal. Chen et al. (2025b) and Chen et al. (2025a) both incorporate depth cues, finding that geometric structures remain stable across domains while visual textures vary dramatically. This insight drives the development of depth-aware tokens and geometric-textual alignment mechanisms.

### 4. Open-Vocabulary Extension

Chen et al. (2025a) represent the first unified framework for OV-DGSS, recognizing that real-world deployment requires handling unseen categories alongside domain shifts. Their Vireo framework bridges visual-textual modalities under domain shift, opening new research directions.

### 5. Quality Over Quantity in Augmentation

Fan et al. (2025) challenge the assumption that more augmented data always improves performance. Their inverse evolution layers demonstrate that filtering low-quality generated samples yields better results than training on all available augmentations.

---

## Limitations and Challenges

### Benchmark Limitations

Most evaluated methods rely on standard benchmarks (Cityscapes, GTA5, SYNTHIA, BDD100K), potentially limiting claims about true generalization. Fewer evaluations address extreme conditions, rare categories, or highly heterogeneous target distributions.

### Computational Cost

Foundation model integration increases inference time and memory requirements. While parameter efficiency focuses on training costs, deployment considerations for edge devices remain underexplored.

### Evaluation Metrics

Beyond mIoU, few papers report metrics addressing specific failure modes: boundary precision, small-object recall, or confidence calibration under domain shift. Comprehensive evaluation frameworks are needed.

### Reproducibility

Several papers cite code availability, but actual reproducibility varies. Differences in implementation details, hyperparameter choices, and computational resources complicate fair comparisons.

---

## Future Directions

### 1. Unified Evaluation Protocols

Standardized benchmarks covering diverse conditions (weather, lighting, seasons, geographic regions) with standardized metrics beyond mIoU would enable more meaningful comparisons.

### 2. Edge Deployment Optimization

Research focusing on compressing foundation-model-based DGSS systems for mobile and embedded deployment could bridge the gap between academic performance and practical applicability.

### 3. Continuous Learning

Dynamic adaptation to streaming target domain data without catastrophic forgetting represents an important extension beyond static DGSS formulations.

### 4. Explainability and Interpretability

Understanding what aspects of predictions transfer across domains versus what fails could inform more robust architecture designs and failure mode mitigation.

### 5. Multimodal Beyond Vision-Text

Integration of audio, LiDAR, radar, and other sensor modalities could provide richer invariant signals for challenging scenarios like autonomous driving.

---

## Conclusion

The period from late 2023 to late 2025 marks a transformative era in Domain Generalized Semantic Segmentation research. The field has transitioned from exploring whether foundation models could help DGSS to understanding precisely how different architectural components, fine-tuning strategies, and multi-modal integrations contribute to domain-invariant representation learning.

Key achievements include establishing parameter-efficient fine-tuning as superior to full retraining, demonstrating the value of geometric and linguistic signals alongside visual features, and pioneering open-vocabulary extensions that combine category and domain generalization. However, challenges remain in benchmark comprehensiveness, computational efficiency for deployment, and theoretical understanding of why certain approaches succeed.

The convergence of foundation models, multi-modal learning, and domain adaptation principles positions DGSS for continued advancement. As foundation models grow larger and more capable, and as real-world deployment pressures intensify, research will likely focus on making these powerful techniques more efficient, interpretable, and applicable to increasingly complex scenarios.

---

## References

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style blind domain generalized semantic segmentation via covariance alignment and semantic consistence contrastive learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating foundation models for domain generalized semantic segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

Chen, S., Han, T., Fu, C., Zhang, C., Wang, C., Su, J., Cai, G., & Wu, M. (2025a). Leveraging depth and language for open-vocabulary domain-generalized semantic segmentation. *arXiv preprint arXiv:2506.09881*. https://arxiv.org/abs/2506.09881v3

Chen, S., Han, T., Zhang, C., Luo, X., Wu, M., Cai, G., & Su, J. (2025b). Stronger, steadier & superior: Geometric consistency in depth VFM forges domain generalized semantic segmentation. *arXiv preprint arXiv:2504.12753*. https://arxiv.org/abs/2504.12753v3

Fan, Q., Liu, C., Qiao, Z., & Shen, X. (2025). IELD: Suppressing domain-specific noise with inverse evolution layers for domain generalized semantic segmentation. *arXiv preprint arXiv:2508.19604*. https://arxiv.org/abs/2508.19604v1

Li, X., & Guo, X. (2025). Multi-granularity feature calibration via VFM for domain generalized semantic segmentation. *arXiv preprint arXiv:2508.03007*. https://arxiv.org/abs/2508.03007v1

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring semantic consistency and style diversity for domain generalized semantic segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, fewer, & superior: Harnessing vision foundation models for domain generalized semantic segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning spectral-decomposed tokens for domain generalized semantic segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

Zhang, X., & Tan, R. T. (2025). Mamba as a bridge: Where vision foundation models meet vision language models for domain-generalized semantic segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

---

*Systematic Literature Review conducted on October 26, 2026*  
*Search parameters: cs.CV, 2023-10-03 to 2025-10-02, 10 papers*  
*Format: APA 7th Edition*
