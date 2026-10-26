# Systematic Literature Review: Domain Generalization for Semantic Segmentation

## Executive Summary

This systematic literature review examines 10 peer-reviewed research papers published between October 2023 and October 2025 on Domain Generalized Semantic Segmentation (DGSS), retrieved from arXiv's Computer Vision (cs.CV) category. The review synthesizes recent advances in addressing domain shift challenges in semantic segmentation, with particular focus on leveraging foundation models, geometric consistency, multi-modal fusion, and style-invariant feature learning.

**Key Findings:**
- Vision Foundation Models (VFMs) have emerged as the dominant paradigm for DGSS, with frozen backbones and parameter-efficient fine-tuning becoming standard practice
- Geometric cues (depth information) are increasingly recognized as more robust than visual features under domain shifts
- Multi-modal approaches combining visual, linguistic, and geometric modalities show superior generalization capabilities
- Recent methods achieve state-of-the-art performance improvements of 4-7% mIoU over prior approaches

---

## Introduction

Domain Generalized Semantic Segmentation (DGSS) addresses the critical challenge of training semantic segmentation models on labeled source domains while ensuring robust generalization to unseen target domains during inference. This problem is particularly challenging due to significant variations in image style, lighting conditions, and scene composition across different domains (e.g., synthetic vs. real images, day vs. night, various weather conditions).

Traditional approaches relying on domain randomization or feature normalization have shown limitations in capturing both content diversity and style variation simultaneously. Recent research has shifted toward leveraging pre-trained Vision Foundation Models (VFMs) and incorporating complementary modalities such as depth information and language embeddings to achieve more robust cross-domain generalization.

---

## Methodological Taxonomy

Based on the reviewed literature, we categorize DGSS approaches into five primary methodological themes:

### 1. Foundation Model-Based Fine-Tuning Strategies

#### CLOUDS: Collaborating Foundation Models (Benigmim et al., 2023)
The CLOUDS framework introduces an orthogonal approach by assembling multiple foundation models rather than relying solely on domain randomization. Key innovations include:
- **CLIP backbone** for robust feature representation
- **Generative models** for content diversification across target distribution modes
- **Segment Anything Model (SAM)** for iterative prediction refinement

CLOUDS achieved notable improvements of 5.6% and 6.7% averaged mIoU on synthetic-to-real benchmarks and varying weather conditions respectively.

#### Rein: Stronger, Fewer, Superior (Wei et al., 2023)
Rein demonstrates that stronger pre-trained models with fewer trainable parameters yield superior generalizability through:
- Trainable tokens linked to distinct instances for precise feature refinement
- Layer-wise feature forwarding within the frozen backbone
- Parameter efficiency with only 1% additional trainable parameters

Remarkably, Rein achieved 78.4% mIoU on Cityscapes without accessing any real urban-scene datasets.

#### MFuser: Mamba-Based Fusion Framework (Zhang & Tan, 2025)
MFuser addresses the challenge of integrating VFMs and Vision-Language Models (VLMs) by:
- **MVFuser**: Co-adapter jointly fine-tuning VFM and VLM with sequential-spatial dynamics capture
- **MTEnhancer**: Hybrid attention-Mamba module refining text embeddings with image priors
- Linear scalability maintaining computational efficiency

MFuser achieved 68.20 mIoU (synthetic-to-real) and 71.87 mIoU (real-to-real).

### 2. Spectral and Frequency-Domain Approaches

#### SET: Spectral-Decomposed Token Learning (Yi et al., 2024)
SET leverages frequency-space decomposition to separate content and style information:
- **Phase-amplitude decomposition** of frozen VFM features (phase = content, amplitude = style)
- Separate processing by learnable tokens for task-specific extraction
- **Attention optimization** bridging style-affected representations with static tokens

This approach specifically targets style-invariant feature learning from learnable tokens, advancing beyond conventional fine-tuning paradigms.

#### MGFC: Multi-Granularity Feature Calibration (Li & Guo, 2025)
MGFC performs coarse-to-fine hierarchical alignment of VFM features:
- **Coarse-grained**: Global contextual semantics and scene-level structure
- **Medium-grained**: Category-level feature discriminability
- **Fine-grained**: High-frequency spatial detail enhancement

Multi-granularity adaptation effectively transfers VFM generalization strengths to DGSS tasks.

### 3. Geometric Consistency and Depth-Aware Methods

#### DepthForge: Geometric Consistency Framework (Chen et al., 2025)
DepthForge exploits the stability of underlying geometry versus susceptibility of visual cues:
- Integrates **DINOv2/EVA02** visual features with **Depth Anything V2** depth cues
- **Depth-aware learnable tokens** decoupling domain-invariant visual and spatial information
- **Depth refinement decoder** adapting multi-layer features

Outstanding performance under extreme conditions (night, snow) demonstrated.

#### Vireo: Open-Vocabulary DGSS (Chen et al., 2025)
Vireo unifies open-vocabulary segmentation with domain generalization:
- **GeoText Prompts**: Aligning geometric features with language cues
- **Coarse Mask Prior Embedding (CMPE)**: Enhancing gradient flow and convergence
- **DOV-VEH**: Fusing refined structural and semantic features

Surpasses existing methods significantly in both domain generalization and open-vocabulary recognition.

### 4. Style Diversity and Semantic Consistency

#### SCSD: Semantic Consistency and Style Diversity (Niu et al., 2024)
SCSD addresses limitations of feature normalization and domain randomization:
- **Semantic Query Booster**: Enhancing object query awareness and discrimination
- **Text-Driven Style Transform**: Controllable style transformation via domain difference embeddings
- **Style Synergy Optimization**: Synergistic weighting of contrastive and aggregation losses

Achieved 49.11 mIoU on four unseen domains (+4.08 mIoU improvement over SOTA).

#### BlindNet: Style Blind Approach (Ahn et al., 2024)
BlindNet blinds style without external modules through:
- **Covariance Alignment**: Training encoder to uniformly recognize styles while preserving content
- **Semantic Consistency Contrastive Learning**: Constructing discriminative class embedding space in decoder

Addresses entanglement of style and content that plagues existing methods.

### 5. Inverse Evolution and Noise Suppression

#### IELFormer: Inverse Evolution Layers (Fan et al., 2025)
IELFormer suppresses domain-specific noise in diffusion-generated data:
- **Inverse Evolution Layers (IELs)**: Highlighting spatial discontinuities using Laplacian-based priors
- **IELDM**: Enhanced diffusion augmentation framework producing higher-quality images
- **Multi-Scale Frequency Fusion (MFF)**: Frequency-domain analysis for structured multi-resolution integration

Strengthens generalization capability in cross-domain scenarios while filtering generative artifacts.

---

## Comparative Analysis

### Performance Benchmarks

| Method | Year | Key Achievement | mIoU Improvement |
|--------|------|-----------------|------------------|
| CLOUDS | 2023 | Multi-FM collaboration | +5.6% / +6.7% |
| Rein | 2023 | Parameter efficiency | 78.4% (Cityscapes) |
| BlindNet | 2024 | Style-blind learning | Outperforms SOTA |
| SET | 2024 | Spectral decomposition | State-of-the-art |
| SCSD | 2024 | Text-driven style control | +4.08 mIoU |
| MFuser | 2025 | VFM-VLM fusion | 68.20 / 71.87 mIoU |
| DepthForge | 2025 | Geometric consistency | Outstanding extremes |
| Vireo | 2025 | Open-vocabulary DGSS | Large margin SOTA |
| MGFC | 2025 | Multi-granularity calibration | Outperforms SOTA |
| IELFormer | 2025 | Noise suppression | Superior generalization |

### Evolution of Methodological Trends

**2023-2024: Foundation Model Emergence**
- Initial exploration of VFM fine-tuning strategies
- Focus on parameter-efficient approaches
- Early integration of CLIP and SAM components

**2024-2025: Multi-Modal Integration**
- Incorporation of depth information as domain-invariant cue
- Fusion of visual and linguistic modalities
- Open-vocabulary capabilities emerging

**2025: Advanced Architectural Innovations**
- Mamba-based efficient transformers
- Hierarchical multi-granularity processing
- Inverse evolution for noise suppression

---

## Critical Assessment

### Strengths of Current Approaches

1. **Foundation Model Leverage**: Frozen VFM backbones provide strong generalization priors while requiring minimal fine-tuning
2. **Geometric Robustness**: Depth-aware methods demonstrate superior performance under extreme conditions
3. **Parameter Efficiency**: Many methods achieve SOTA with <1% additional trainable parameters
4. **Multi-Modal Fusion**: Combining complementary modalities yields consistent improvements

### Limitations and Challenges

1. **Computational Complexity**: Multi-FM assemblies increase inference time and memory requirements
2. **Data Dependency**: Some methods require specific pre-trained models not always available
3. **Evaluation Scope**: Most benchmarks limited to synthetic-to-real transitions; diverse real-world domains underexplored
4. **Open-Vocabulary Gap**: Limited work addressing both domain generalization and novel category recognition simultaneously

### Research Gaps

- **Real-Time Deployment**: Most methods optimized for accuracy rather than inference speed
- **Cross-Task Transfer**: Limited exploration of DGSS techniques applied to related dense prediction tasks
- **Uncertainty Quantification**: Insufficient handling of model confidence under severe domain shifts
- **Ethical Considerations**: Minimal discussion of bias propagation across domains

---

## Future Directions

### Technical Frontiers

1. **Efficient Architecture Design**: Developing lightweight DGSS methods suitable for edge deployment
2. **Dynamic Adaptation**: Real-time model adjustment based on detected domain characteristics
3. **Self-Supervised Pre-training**: Leveraging unlabeled target domain data for continued adaptation
4. **Causal Representation Learning**: Disentangling domain-invariant causal factors from spurious correlations

### Application Domains

- **Autonomous Driving**: Robust segmentation across weather, lighting, geographic conditions
- **Medical Imaging**: Cross-hospital and cross-device generalization
- **Satellite Imagery**: Seasonal and geographic domain adaptation
- **Robotics**: Sim-to-real transfer in manipulation and navigation tasks

### Evaluation Standards

Need for standardized benchmark suites including:
- Diverse real-world domain shifts
- Extreme condition testing (adverse weather, low light)
- Computational efficiency metrics
- Long-tail category performance

---

## Conclusion

The field of Domain Generalized Semantic Segmentation has advanced rapidly from 2023 to 2025, transitioning from traditional domain randomization approaches to sophisticated foundation model-based frameworks. The integration of geometric cues, multi-modal fusion, and spectral decomposition techniques represents a maturing understanding of domain-invariant feature learning.

Vision Foundation Models have become the cornerstone of modern DGSS, providing robust pre-trained representations that significantly reduce the need for extensive target domain data. Recent innovations in geometric consistency (DepthForge), multi-modal fusion (MFuser, Vireo), and inverse evolution layers (IELFormer) demonstrate the community's commitment to addressing fundamental challenges in cross-domain generalization.

However, several critical gaps remain, particularly regarding real-time deployment, comprehensive evaluation standards, and ethical considerations. Future research should prioritize developing efficient architectures suitable for resource-constrained environments while expanding evaluation to more diverse and challenging domain shift scenarios.

The convergence of foundation models, geometric reasoning, and multi-modal integration offers promising pathways toward truly robust semantic segmentation systems capable of operating reliably across the vast diversity of real-world conditions.

---

## References

### Primary Sources

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style blind domain generalized semantic segmentation via covariance alignment and semantic consistence contrastive learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating foundation models for domain generalized semantic segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

Chen, S., Han, T., Zhang, C., Luo, X., Wu, M., Cai, G., & Su, J. (2025). Stronger, steadier & superior: Geometric consistency in depth VFM forges domain generalized semantic segmentation. *arXiv preprint arXiv:2504.12753*. https://arxiv.org/abs/2504.12753v3

Chen, S., Han, T., Fu, C., Zhang, C., Wang, C., Su, J., Cai, G., & Wu, M. (2025). Leveraging depth and language for open-vocabulary domain-generalized semantic segmentation. *arXiv preprint arXiv:2506.09881*. https://arxiv.org/abs/2506.09881v3

Fan, Q., Liu, C., Qiao, Z., & Shen, X. (2025). IELDGM: Suppressing domain-specific noise with inverse evolution layers for domain generalized semantic segmentation. *arXiv preprint arXiv:2508.19604*. https://arxiv.org/abs/2508.19604v1

Li, X., & Guo, X. (2025). Multi-granularity feature calibration via VFM for domain generalized semantic segmentation. *arXiv preprint arXiv:2508.03007*. https://arxiv.org/abs/2508.03007v1

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring semantic consistency and style diversity for domain generalized semantic segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, fewer, & superior: Harnessing vision foundation models for domain generalized semantic segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning spectral-decomposed tokens for domain generalized semantic segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

Zhang, X., & Tan, R. T. (2025). Mamba as a bridge: Where vision foundation models meet vision language models for domain-generalized semantic segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

---

*Systematic Literature Review conducted on October 26, 2026*
*Search criteria: 10 papers, cs.CV category, publication window 2023-10-03 to 2025-10-02*
*Format: APA 7th Edition*
