# Systematic Literature Review: 3D Gaussian Splatting

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "3D Gaussian splatting", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on 3D Gaussian Splatting reveals a rapidly evolving field focused on improving rendering efficiency, extending representational capabilities, and enabling new application domains. Recent work addresses fundamental limitations including depth-sorting requirements, view-dependent content representation, gradient optimization stability, and compression for practical deployment. The research demonstrates strong convergence on stochastic and sorting-free approaches, progressive compression strategies, and integration with vision-language models for semantic understanding. However, limitations remain in handling complex topological structures, generalizing across diverse scenes, and achieving consistent multi-view alignment without per-scene optimization.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "3D Gaussian splatting", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Sorting-Free and Stochastic Rendering Approaches

A significant research direction focuses on eliminating the computational bottleneck of depth-sorting in 3D Gaussian Splatting. Kheradmand et al. (2025) introduced StochasticSplats, which combines 3D Gaussian splatting with stochastic rasterization through an unbiased Monte Carlo estimator of the volume rendering equation. This approach removes the need for sorting while enabling accurate 3D blending of overlapping Gaussians, rendering more than four times faster than sorted rasterization at reasonable visual quality. The number of Monte Carlo samples provides a mechanism to trade off computation time and quality, offering flexible control over render cost and visual fidelity.

### Theme 2: View-Dependent and Opacity-Aware Representations

Extending 3D Gaussian Splatting to better represent view-dependent content such as specular highlights and reflections represents another key research direction. Nowak et al. (2025) proposed VoD-3DGS, which introduces an additional symmetric matrix to enhance the opacity representation of each 3D Gaussian, allowing certain Gaussians to be suppressed based on the viewer's perspective. This view-dependent opacity representation enables more accurate modeling of specular highlights and reflections while maintaining rendering speed above 60 FPS with minimal memory overhead. The approach achieves state-of-the-art performance across multiple benchmarks including Mip-Nerf, Tanks&Temples, Deep Blending, and Nerf-Synthetic datasets.

### Theme 3: Progressive Compression and Efficient Storage

Addressing the storage and transmission challenges of 3D Gaussian Splatting models, Chen et al. (2025) developed PCGS (Progressive Compression of 3D Gaussian Splatting). Their approach features a progressive masking strategy that incrementally incorporates new anchors while refining existing ones, combined with progressive quantization that gradually reduces quantization step sizes. By leveraging existing quantization results to refine probability prediction, PCGS improves entropy coding efficiency across progressive levels while maintaining compression performance comparable to state-of-the-art non-progressive methods. This enables efficient utilization of existing bitstreams in on-demand applications.

### Theme 4: Semantic Understanding and Language-Guided Segmentation

Integrating semantic understanding with 3D Gaussian Splatting has emerged as a critical research direction. Ding et al. (2026) introduced ZeroSplat, a training-free framework that lifts 2D Vision-Language Model priors into 3D space through robust multi-view geometric constraints, enabling generalized referring segmentation with an arbitrary number of targets from ambiguous real-world instructions. Similarly, Tao et al. (2025) proposed CaRF (Camera-aware Referring Field), which addresses viewpoint drift and inconsistent predictions across views through camera-aware cross-view alignment. These approaches enable intrinsic 3D point-level understanding without requiring additional feature storage or per-scene optimization.

### Theme 5: Optimization Stability and Gradient Improvements

Addressing fundamental optimization challenges in 3D Gaussian Splatting, Morales et al. (2026) proposed TruncGradGS, which introduces a piecewise truncated gradient formulation to address the gradient vanishing phenomenon. This occurs when pixels far from Gaussian primitives have diminishing gradient magnitudes, leading to optimization instability. Their method consistently improves 3D Gaussian Splatting with both random and COLMAP initializations, demonstrating generalizability across static and dynamic scenarios. The authors also introduced a novel dataset for benchmarking dynamic Gaussian Splatting using synthetic 3D scenes.

### Theme 6: Specialized Applications and Domain Extensions

Extending 3D Gaussian Splatting to specialized domains represents another active research direction. Pan et al. (2025) developed HairGS for hair strand reconstruction, enabling strand-level hair geometry reconstruction from multi-view images through a differentiable Gaussian rasterizer and novel merging scheme. Ren et al. (2026) introduced Gaussian-JEPA for self-supervised learning applied to 3D Gaussian Splatting representations, predicting representations of held-out Gaussian token blocks from visible context. Vicente (2026) focused on high-performance re-implementation strategies, transitioning from Python to C++/CUDA kernels to balance reconstruction fidelity with computational efficiency.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that eliminating or reducing computational bottlenecks is essential for practical 3D Gaussian Splatting deployment. Multiple papers demonstrate that stochastic or sorting-free approaches (Kheradmand et al., 2025), view-dependent opacity representations (Nowak et al., 2025), and progressive compression strategies (Chen et al., 2025) can achieve significant efficiency gains without sacrificing visual quality. There is also consensus that integrating semantic understanding without per-scene optimization or additional feature storage is achievable through geometric constraints and vision-language model priors (Ding et al., 2026; Tao et al., 2025).

**Disagreements**: The literature shows different approaches to handling representational challenges. While some work focuses on architectural modifications to the Gaussian representation itself (Nowak et al., 2025; Ren et al., 2026), others emphasize implementation-level optimizations through low-level re-implementation (Vicente, 2026). Additionally, approaches to semantic segmentation differ fundamentally: ZeroSplat (Ding et al., 2026) advocates for training-free, zero-feature methods, while CaRF (Tao et al., 2025) employs camera-conditioned modulation and cross-view logit alignment during training, suggesting different philosophical approaches to the trade-off between flexibility and accuracy.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly address limitations in their abstracts, suggesting either space constraints or a focus on presenting positive results. Second, while multiple papers address specific application domains (hair reconstruction, referring segmentation), there is limited work on generalizing across diverse scene types or handling complex topological structures beyond specialized cases. Third, the tension between training-free approaches and optimized training-based methods remains unresolved, with insufficient comparative analysis of when each paradigm is preferable. Fourth, while dynamic Gaussian Splatting is mentioned (Morales et al., 2026), comprehensive benchmarks and standardized evaluation protocols for dynamic scenes remain underdeveloped. Finally, the integration of 3D Gaussian Splatting with other emerging representation paradigms (e.g., neural radiance fields, implicit representations) warrants further investigation.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: How can progressive compression be achieved for 3D Gaussian Splatting to efficiently utilize existing bitstreams in on-demand applications?
**Methodology**: The authors propose PCGS with a progressive masking strategy that incrementally incorporates new anchors while refining existing ones, and a progressive quantization approach that gradually reduces quantization step sizes. They leverage existing quantization results to refine probability prediction for improving entropy coding efficiency across progressive levels.
**Key findings**:
- PCGS enables progressive compression by adaptively controlling both the quantity and quality of Gaussians
- Progressive masking strategy incrementally incorporates new anchors while refining existing ones to enhance fidelity
- Progressive quantization gradually reduces quantization step sizes for finer modeling of Gaussian attributes
- The method improves entropy coding efficiency by leveraging existing quantization results to refine probability prediction
- PCGS achieves progressivity while maintaining compression performance comparable to state-of-the-art non-progressive methods
**Limitations**: Not stated in abstract

### Ding et al. (2026)

**Research question**: How can 3D Gaussian Splatting be extended to handle generalized referring segmentation with an arbitrary number of targets (0, 1, or N) from ambiguous real-world instructions?
**Methodology**: The authors propose ZeroSplat, a training-free and zero-feature framework that lifts 2D Vision-Language Model priors into 3D space through robust multi-view geometric constraints, enabling intrinsic point-level understanding without additional feature storage.
**Key findings**:
- ZeroSplat significantly outperforms state-of-the-art methods across generalized and single-target scenarios
- The method maintains exceptional efficiency without requiring per-scene optimization
- ZeroSplat enables intrinsic 3D point-level understanding without incurring additional feature storage
- The approach addresses fundamental technical bottlenecks in existing R3DGS paradigms
**Limitations**: Not stated in abstract

### Kheradmand et al. (2025)

**Research question**: How can 3D Gaussian splatting overcome rendering artifacts and lack of control over render cost and visual fidelity caused by depth-sorting requirements?
**Methodology**: The authors combine 3D Gaussian splatting with stochastic rasterization by leveraging an unbiased Monte Carlo estimator of the volume rendering equation, which removes the need for sorting and allows accurate 3D blending of overlapping Gaussians. The method is implemented using OpenGL shaders for efficient GPU rendering.
**Key findings**:
- Stochastic rasterization eliminates the need for depth-sorting in 3D Gaussian splatting
- The approach enables accurate 3D blending of overlapping Gaussians through Monte Carlo estimation
- The number of Monte Carlo samples provides a mechanism to trade off computation time and quality
- The method renders more than four times faster than sorted rasterization at reasonable visual quality
- The implementation enables efficient rendering on modern GPU hardware using OpenGL shaders
**Limitations**: Not stated in abstract

### Morales et al. (2026)

**Research question**: How can the gradient vanishing phenomenon in 3D Gaussian Splatting be addressed to improve optimization stability and robustness?
**Methodology**: The authors propose a piecewise truncated gradient formulation that improves optimization stability and robustness to initializations, addressing the gradient vanishing problem where pixels far from Gaussian primitives have diminishing gradient magnitudes. The method is evaluated on both static and dynamic Gaussian Splatting scenarios.
**Key findings**:
- Truncated gradient formulation addresses the gradient vanishing phenomenon in 3D Gaussian Splatting
- The method consistently improves 3D Gaussian Splatting with both random and COLMAP initializations
- The approach is generalizable across static and dynamic Gaussian Splatting
- Current benchmarks for dynamic scenes have limitations that the authors examine
- The authors introduce a novel dataset for benchmarking dynamic Gaussian Splatting using synthetic 3D scenes
**Limitations**: Not stated in abstract

### Nowak et al. (2025)

**Research question**: How can 3D Gaussian Splatting be extended to better represent view-dependent content such as specular highlights and reflections?
**Methodology**: The authors extend the 3D Gaussian Splatting model by introducing an additional symmetric matrix to enhance the opacity representation of each 3D Gaussian, allowing certain Gaussians to be suppressed based on the viewer's perspective for more accurate representation of view-dependent reflections and specular highlights.
**Key findings**:
- View-dependent opacity representation enables more accurate modeling of specular highlights and reflections
- The enhanced model achieves state-of-the-art performance on Mip-Nerf, Tanks&Temples, Deep Blending, and Nerf-Synthetic datasets
- The method maintains rendering speed above 60 FPS without significant loss
- The approach incurs only a minimal increase in memory usage
- View-opacity dependency allows the model to differentiate objects from light interacting with specular surfaces
**Limitations**: Not stated in abstract

### Pan et al. (2025)

**Research question**: How can 3D Gaussian Splatting be extended to enable strand-level hair geometry reconstruction from multi-view images?
**Methodology**: The authors propose a multi-stage pipeline that first reconstructs detailed hair geometry using a differentiable Gaussian rasterizer, then merges individual Gaussian segments into coherent strands through a novel merging scheme, and finally refines and grows the strands under photometric supervision.
**Key findings**:
- The method robustly handles a wide range of hairstyles
- Achieves efficient reconstruction, typically completing within one hour
- The proposed evaluation metric serves as a proxy for assessing topological accuracy in strand reconstruction
- The approach addresses the connectivity and topology of hair strands that existing methods neglect
**Limitations**: Not stated in abstract

### Ren et al. (2026)

**Research question**: How can self-supervised learning be applied to 3D Gaussian Splatting representations without being tied to specific sampled realizations?
**Methodology**: The authors introduce Gaussian-JEPA, which predicts representations of held-out Gaussian token blocks from visible context using an online encoder and a shared exponential-moving-average encoder that supplies stop-gradient features for multi-scale targets with complementary target projections and feature-space grounding.
**Key findings**:
- Gaussian-JEPA is more consistent across resampled inputs compared to matched reconstruction pretraining
- The method retains more instance information under partial observations
- Gaussian-JEPA provides stronger frozen features for Gaussian completion
- Latent prediction serves as an effective objective for reusable 3D Gaussian representations without requiring input-space decoding
**Limitations**: Not stated in abstract

### Tao et al. (2025)

**Research question**: How can viewpoint drift and inconsistent predictions across views be addressed in Referring 3D Gaussian Splatting Segmentation?
**Methodology**: The authors propose CaRF (Camera-aware Referring Field), a camera-aware cross-view alignment framework that introduces Camera-conditioned Alignment Modulation (CAM) to inject camera geometry into Gaussian-text interactions, and Gaussian-level Cross-view Logit Alignment (GCLA) to explicitly align referring responses of the same Gaussians across calibrated views during training.
**Key findings**:
- CaRF achieves state-of-the-art performance on three benchmarks for referring 3D Gaussian splatting segmentation
- The method improves mIoU by 16.8% on Ref-LERF benchmark
- The method improves mIoU by 4.3% on LERF-OVS benchmark
- The method improves mIoU by 2.0% on 3D-OVS benchmark
- Cross-view discrepancy can be turned into an optimizable objective for geometry-aware and view-consistent reasoning
**Limitations**: Not stated in abstract

### Vicente (2026)

**Research question**: How can 3D Gaussian Splatting be re-implemented at a low level to balance reconstruction fidelity with computational efficiency?
**Methodology**: The authors propose ImprovedGS+, a high-performance re-implementation within the LichtFeld-Studio framework that transitions from Python to C++/CUDA kernels, introducing a Long-Axis-Split CUDA kernel, custom Laplacian-based importance kernels with Non-Maximum Suppression, and an adaptive Exponential Scale Scheduler.
**Key findings**:
- The 1M-budget variant achieves a 26.8% reduction in training time compared to the MCMC baseline
- Uses 13.3% fewer Gaussians while maintaining superior visual quality
- The full variant demonstrates a 1.28 dB PSNR increase over the ADC baseline
- Achieves a 38.4% reduction in parametric complexity compared to the ADC baseline
- Establishes a new Pareto-optimal front for scene reconstruction on the Mip-NeRF360 dataset
**Limitations**: Not stated in abstract

### Xin et al. (2025)

**Research question**: How can 3D Gaussian Splatting be represented in neural networks to address the non-unique and heterogeneous nature of Gaussian parameterization?
**Methodology**: The authors propose an embedding representation of 3DGS based on continuous submanifold fields that encapsulate the intrinsic information of Gaussian primitives, preserving underlying color and geometric structure while enforcing unique mapping and channel homogeneity.
**Key findings**:
- The proposed embedding representation addresses the non-unique nature of Gaussian parameterization
- The method enforces unique mapping and channel homogeneity for 3DGS representations
- The approach benefits the learning of 3DGS by preserving intrinsic information of Gaussian primitives
**Limitations**: Not stated in abstract

## References

Chen, Y., Li, M., Wu, Q., Lin, W., Harandi, M., & Cai, J. (2025). Progressive compression of 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2503.08511

Ding, J., Song, M., Zhang, X., Jin, H., Jin, Y., & Si, X. (2026). ZeroSplat: Generalized referring segmentation in 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2607.18801

Kheradmand, S., Vicini, D., Kopanas, G., Lagun, D., Yi, K. M., Matthews, M., & Tagliasacchi, A. (2025). StochasticSplats: Stochastic rasterization for sorting-free 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2503.24366

Morales, T., Le-Pham, N.-Q., Atkins, R., & Hua, B.-S. (2026). TruncGradGS: Improved 3D Gaussian Splatting via truncated gradient updates. arXiv. https://arxiv.org/abs/2609.03534

Nowak, M., Jarosz, W., & Chin, P. (2025). VoD-3DGS: View-opacity-Dependent 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2501.17978

Pan, Y., Nießner, M., & Kirschstein, T. (2025). HairGS: Hair strand reconstruction based on 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2509.07774

Ren, B., Ma, Q., Li, Y., Han, Z., Li, Y., Fu, Y., Anwer, R. M., Gevers, T., Khan, F. S., & Khan, S. (2026). Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats. arXiv. https://arxiv.org/abs/2608.15651

Tao, Y., Zhou, K., Tan, X., & Xie, Y. (2025). Camera-Aware Cross-View Alignment for Referring 3D Gaussian Splatting Segmentation. arXiv. https://arxiv.org/abs/2511.03992

Vicente, J. M. (2026). ImprovedGS+: A High-Performance C++/CUDA Re-Implementation Strategy for 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2603.08661

Xin, Y., Liu, Y., Xie, X., & Li, X. (2025). Learning Unified Representation of 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2509.22917
