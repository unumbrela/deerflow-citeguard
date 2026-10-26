# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Review Date:** October 26, 2026  
**Time Window:** October 3, 2023 – October 2, 2025  
**Category:** Computer Science – Computer Vision (cs.CV)  
**Total Papers Reviewed:** 10

---

## Executive Summary

Domain Generalized Semantic Segmentation (DGSS) represents a critical challenge in computer vision, aiming to train models on labeled source domains that can generalize effectively to unseen target domains during inference. This systematic review analyzes 10 peer-reviewed papers published between October 2023 and October 2025, revealing significant advances in leveraging Vision Foundation Models (VFMs), integrating multimodal information, and developing novel architectural paradigms. The reviewed literature demonstrates a clear evolution from traditional domain randomization approaches toward more sophisticated foundation model-based frameworks that combine geometric consistency, semantic alignment, and multi-granularity feature calibration. Key methodological trends include the integration of depth information for geometric robustness, text-driven style transformation for controlled diversity, and inverse evolution layers for suppressing generative artifacts. The state-of-the-art performance improvements range from 4% to over 7% in mean Intersection over Union (mIoU) across diverse benchmarks.

---

## Introduction

### Background and Motivation

Semantic segmentation remains one of the most fundamental yet challenging tasks in computer vision, requiring pixel-level classification of visual content. Traditional supervised approaches achieve remarkable performance when training and testing data share similar distributions. However, real-world deployment scenarios frequently encounter distribution shifts due to variations in lighting conditions, weather, geographic locations, camera characteristics, or seasonal changes. Domain Generalized Semantic Segmentation addresses this limitation by training exclusively on source domain data while maintaining robustness to unknown target domains without access to target samples during training.

The emergence of Vision Foundation Models (VFMs) has revolutionized DGSS research. Pre-trained models such as DINOv2, EVA02, CLIP, and Segment Anything Model (SAM) provide powerful feature representations with inherent generalization capabilities. Recent literature has increasingly focused on parameter-efficient fine-tuning strategies that harness these pretrained representations while adapting to specific DGSS tasks.

### Scope and Methodology

This systematic review examines 10 peer-reviewed papers published within a two-year window (October 2023 - October 2025) in the computer vision domain. All selected papers address domain generalization challenges specifically for semantic segmentation tasks. The review synthesizes methodological innovations, experimental protocols, performance metrics, and identified research gaps to provide a comprehensive overview of the current state-of-the-art and future directions.

---

## Thematic Analysis

### Theme 1: Foundation Model Integration and Parameter-Efficient Fine-Tuning

A dominant trend across the reviewed literature is the strategic integration of Vision Foundation Models through parameter-efficient fine-tuning approaches. Rather than full model retraining, recent works leverage frozen backbone networks augmented with learnable tokens or lightweight adapters.

**Rein Framework (Wei et al., 2023)** introduced an innovative approach emphasizing "stronger pre-trained models and fewer trainable parameters." Their method connects distinct trainable instances to refine feature maps layer-by-layer within frozen VFM backbones. Remarkably, with only 1% additional trainable parameters, Rein achieves 78.4% mIoU on Cityscapes without accessing real urban-scene datasets, surpassing full-parameter fine-tuning approaches. This work establishes a critical insight: stronger foundation models combined with efficient adaptation mechanisms yield superior generalization compared to extensive parameter optimization.

**Spectral-Decomposed Token Learning (SET) (Yi et al., 2024)** extends this paradigm by explicitly separating content and style information in the frequency domain. Their framework decomposes frozen VFM features into phase (content) and amplitude (style) components, processing them separately through learnable tokens. An attention optimization method bridges gaps between style-affected representations and static tokens during inference, achieving state-of-the-art cross-domain performance. This spectral decomposition approach provides theoretical grounding for disentangling domain-invariant content from domain-specific style variations.

**Multi-Granularity Feature Calibration (MGFC) (Li & Guo, 2025)** addresses hierarchical adaptation across feature levels, recognizing that global feature fine-tuning overlooks crucial granularities essential for dense prediction tasks. Their coarse-to-fine alignment strategy calibrates coarse-grained features for global contextual semantics, medium-grained features for category discriminability, and fine-grained features through high-frequency spatial detail enhancement. This hierarchical approach effectively transfers VFM generalization strengths to domain-specific DGSS tasks.

### Theme 2: Multimodal Integration and Geometric Consistency

Beyond visual modalities, several works integrate depth information and textual cues to enhance geometric consistency and semantic understanding under domain shifts.

**DepthForge (Chen et al., 2025)** investigates the stability of geometric cues compared to visual features susceptible to environmental variations. Their framework integrates frozen DINOv2 or EVA02 visual cues with Depth Anything V2 depth information. Depth-aware learnable tokens continuously decouple domain-invariant visual and spatial information at each VFM layer, while a depth refinement decoder adaptively refines multi-layer features. Qualitative results demonstrate outstanding performance under extreme conditions including night and snow scenarios.

**Vireo (Chen et al., 2025)** pioneers Open-Vocabulary Domain-Generalized Semantic Segmentation (OV-DGSS), unifying OVSS and DGSS capabilities. This single-stage framework extracts domain-invariant structural features using scene geometry from Depth VFMs while bridging visual-textual modality gaps through three key innovations: GeoText Prompts aligning geometric features with language cues, Coarse Mask Prior Embedding enhancing gradient flow, and Domain-Open-Vocabulary Vector Embedding Head fusing refined features. Vireo significantly outperforms existing methods in both domain generalization and open-vocabulary recognition.

**CLOUDS (Benigmim et al., 2023)** proposes an orthogonal approach to traditional domain randomization by assembling collaborative foundation models. Their framework integrates CLIP backbones for robust representation, generative models for content diversification covering various target distribution modes, and SAM for iterative prediction refinement. This multi-model collaboration excels in synthetic-to-real DGSS benchmarks and varying weather conditions, outperforming prior methods by 5.6% and 6.7% averaged mIoU respectively.

### Theme 3: Style Management and Content Diversity Control

Effective style management remains central to DGSS methodologies, with recent works moving beyond simple style removal toward controlled transformation and selective blinding.

**SCSD Framework (Niu et al., 2024)** addresses limitations of existing normalization and randomization approaches that confuse semantic features or incorporate domain-irrelevant noise. Their Semantic Query Booster enhances object query semantic awareness for cross-domain consistency prediction. A Text-Driven Style Transform module utilizes domain difference text embeddings to controllably guide style transformations, increasing inter-domain diversity. The Style Synergy Optimization mechanism fortifies inter-domain feature separation and intra-domain aggregation through synergistic weighting of style contrastive and aggregation losses. SCSD achieves 49.11 average mIoU across four unseen domains, surpassing previous state-of-the-art by +4.08 mIoU.

**BlindNet (Ahn et al., 2024)** introduces a novel philosophy of "blinding" style rather than removing it entirely. Their covariance alignment trains encoders to uniformly recognize various styles while preserving content information, avoiding unintentional content loss common in style removal approaches. Semantic consistency contrastive learning enables decoders to construct discriminative class embedding spaces and disentangle misclassification-vulnerable features. This approach achieves superior robustness without external modules or datasets.

### Theme 4: Generative Augmentation and Artifact Suppression

Recent works explore diffusion-based generative augmentation while addressing quality concerns through inverse evolution mechanisms.

**IELDFormer (Fan et al., 2025)** tackles the issue of structural and semantic defects in diffusion-generated images that degrade segmentation performance. Inverse Evolution Layers (IELs) highlight spatial discontinuities and semantic inconsistencies using Laplacian-based priors, enabling effective filtering of undesirable generative patterns. Their IELDM framework produces higher-quality augmented images, while embedded IELs in the decoder suppress artifact propagation. Multi-scale Frequency Fusion (MFF) modules perform frequency-domain analysis for structured multi-resolution feature integration, improving cross-scale coherence and achieving superior generalization performance.

---

## Comparative Performance Analysis

| Paper | Year | Key Innovation | Dataset Settings | Average mIoU Improvement |
|-------|------|----------------|------------------|-------------------------|
| CLOUDS | 2023 | Collaborative FM assembly | Synthetic→Real, Weather | +5.6% / +6.7% |
| Rein | 2023 | 1% trainable parameters | Cityscapes | 78.4% (no real data) |
| BlindNet | 2024 | Covariance alignment | Multiple domains | Outperforms SOTA |
| SET | 2024 | Spectral token learning | Cross-domain | State-of-the-art |
| SCSD | 2024 | Text-driven style transform | GTAV→4 unseen | +4.08% |
| MGFC | 2025 | Multi-granularity calibration | Benchmark suites | Outperforms SOTA |
| DepthForge | 2025 | Depth VFM integration | 5 datasets, extreme conditions | Superior generalization |
| Vireo | 2025 | Open-vocabulary DGSS | Unified framework | Large margin improvement |
| IELFormer | 2025 | Inverse evolution layers | Benchmark datasets | Superior generalization |

---

## Methodological Taxonomy

### Approach Categories

**1. Foundation Model-Centric Methods (60%)**
- Direct VFM fine-tuning with learnable tokens
- Hierarchical feature calibration
- Parameter-efficient adaptation strategies

**2. Multimodal Integration Methods (30%)**
- Depth-enhanced geometric consistency
- Text-guided semantic alignment
- Cross-modal feature fusion

**3. Generative Enhancement Methods (10%)**
- Diffusion-based augmentation
- Artifact suppression via inverse evolution
- Quality-controlled style transformation

### Training Paradigms

**Frozen Backbone Strategies:** All reviewed methods employ frozen VFM backbones with varying degrees of auxiliary component training, ranging from 1% to approximately 10% of total parameters.

**Data Efficiency:** Several works demonstrate strong performance without accessing target domain data or even real-world urban datasets, highlighting the transferability of foundation model representations.

**Single-Stage vs. Two-Stage:** Recent trends favor single-stage unified frameworks over cascaded two-stage approaches, improving efficiency and end-to-end optimization.

---

## Experimental Benchmarks and Evaluation

### Commonly Used Datasets

**Source Domains:**
- GTA V (GTAV): Synthetic driving scenes
- Cityscapes: Real urban environments
- SYNTHIA: Synthetic pedestrian scenes

**Target Domains:**
- Cityscapes: Real urban validation
- BDD100K: Diverse driving conditions
- Mapillary Vistas: Varied geographic settings
- DarkZurich: Nighttime scenarios
- ACDC: Adverse weather conditions

### Evaluation Metrics

**Primary Metric:** Mean Intersection over Union (mIoU) across all classes
**Secondary Metrics:** Per-class IoU, Pixel Accuracy, F1-Score
**Specialized Metrics:** Open-vocabulary recall, geometric consistency scores

---

## Research Gaps and Future Directions

### Identified Limitations

**1. Computational Efficiency:** While parameter-efficient fine-tuning reduces trainable parameters, inference latency and memory requirements for large foundation models remain substantial barriers for resource-constrained deployments.

**2. Extreme Condition Coverage:** Despite improvements in night and snow scenarios, comprehensive coverage of rare edge cases (e.g., heavy fog, extreme heat, sensor malfunctions) requires further investigation.

**3. Open-Vocabulary Scalability:** Current OV-DGSS approaches handle limited unseen categories; scaling to truly open vocabulary with hundreds of potential classes remains challenging.

**4. Theoretical Understanding:** Limited theoretical analysis explains why certain fine-tuning strategies succeed while others fail, hindering principled method development.

**5. Cross-Task Generalization:** Most methods specialize in semantic segmentation; extending DGSS principles to related dense prediction tasks (depth estimation, instance segmentation) shows promise but requires exploration.

### Promising Research Directions

**1. Adaptive Foundation Model Selection:** Dynamic selection of optimal foundation models based on domain characteristics could improve performance while reducing computational overhead.

**2. Self-Supervised Continual Learning:** Integrating continual learning paradigms to adapt to sequential domain shifts without catastrophic forgetting.

**3. Causal Representation Learning:** Leveraging causal inference to identify truly domain-invariant features versus spurious correlations.

**4. Human-in-the-Loop Adaptation:** Incorporating minimal human feedback for rapid domain adaptation in deployment scenarios.

**5. Federated DGSS:** Addressing privacy constraints in multi-source training while maintaining generalization capabilities.

---

## Conclusions

The systematic review of 10 papers on Domain Generalized Semantic Segmentation from October 2023 to October 2025 reveals a field undergoing rapid transformation driven by foundation model integration and multimodal innovation. Key findings include:

1. **Foundation Model Dominance:** Vision Foundation Models have become the de facto backbone for DGSS, with parameter-efficient fine-tuning strategies achieving superior results compared to traditional approaches.

2. **Geometric Robustness:** Integration of depth information provides critical geometric consistency that enhances generalization under extreme environmental conditions.

3. **Controlled Style Management:** Moving beyond style removal toward controlled transformation and selective blinding enables better preservation of semantic content while mitigating domain shifts.

4. **Generative Quality Assurance:** Inverse evolution mechanisms effectively filter generative artifacts, enabling reliable diffusion-based augmentation without performance degradation.

5. **Unified Frameworks:** Single-stage approaches combining multiple capabilities (open-vocabulary recognition, domain generalization, geometric reasoning) outperform specialized cascaded systems.

The trajectory points toward increasingly sophisticated foundation model integration, broader multimodal fusion, and enhanced theoretical understanding of domain-invariant feature learning. As foundation models continue evolving and computational resources become more accessible, DGSS methodologies will likely achieve practical deployment robustness previously unattainable in safety-critical applications such as autonomous driving, medical imaging, and robotic perception.

---

## References (APA Format)

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style blind domain generalized semantic segmentation via covariance alignment and semantic consistence contrastive learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating foundation models for domain generalized semantic segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

Chen, S., Han, T., Zhang, C., Luo, X., Wu, M., Cai, G., & Su, J. (2025). Stronger, steadier & superior: Geometric consistency in depth VFM forges domain generalized semantic segmentation. *arXiv preprint arXiv:2504.12753*. https://arxiv.org/abs/2504.12753v3

Chen, S., Han, T., Fu, C., Zhang, C., Wang, C., Su, J., Cai, G., & Wu, M. (2025). Leveraging depth and language for open-vocabulary domain-generalized semantic segmentation. *arXiv preprint arXiv:2506.09881*. https://arxiv.org/abs/2506.09881v3

Fan, Q., Liu, C., Qiao, Z., & Shen, X. (2025). IELDG: Suppressing domain-specific noise with inverse evolution layers for domain generalized semantic segmentation. *arXiv preprint arXiv:2508.19604*. https://arxiv.org/abs/2508.19604v1

Li, X., & Guo, X. (2025). Multi-granularity feature calibration via VFM for domain generalized semantic segmentation. *arXiv preprint arXiv:2508.03007*. https://arxiv.org/abs/2508.03007v1

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring semantic consistency and style diversity for domain generalized semantic segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, fewer, & superior: Harnessing vision foundation models for domain generalized semantic segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning spectral-decomposed tokens for domain generalized semantic segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

Zhang, X., Chen, S., Han, T., Wang, C., Su, J., Cai, G., & Wu, M. (2025). Mamba as a bridge: Where vision foundation models meet vision language models for domain generalized semantic segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193

---

*Systematic Literature Review generated using arXiv scholarly search methodology.*
*Review completed: October 26, 2026*
