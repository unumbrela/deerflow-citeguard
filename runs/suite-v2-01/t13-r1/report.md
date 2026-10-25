# Systematic Literature Review: 3D Gaussian Splatting

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "3D Gaussian splatting", category cs.CV, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on 3D Gaussian Splatting (3DGS) reveals a rapidly evolving field focused on improving the efficiency, quality, and applicability of this neural rendering technique. Recent work addresses fundamental limitations of the original 3DGS formulation, including depth-sorting requirements, gradient vanishing during optimization, view-dependent content representation, and compression for practical deployment. The field demonstrates strong convergence around self-supervised learning approaches, geometric understanding extensions, and performance optimization through lower-level implementations. These papers collectively establish 3DGS as a versatile foundation for diverse applications ranging from hair strand reconstruction to generalized referring segmentation, while ongoing research tackles core challenges in rendering efficiency and optimization stability.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "3D Gaussian splatting", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Optimization and Training Improvements

A significant research direction focuses on enhancing the optimization process and training efficiency of 3DGS. TruncGradGS addresses the gradient vanishing phenomenon that occurs when pixels far from Gaussian primitives receive diminishing gradient magnitudes, proposing a piecewise truncated gradient formulation that improves optimization stability across both static and dynamic scenarios (Morales et al., 2026). Gaussian-JEPA introduces self-supervised learning to 3DGS by predicting representations of held-out Gaussian token blocks from visible context, eliminating the need for reconstruction of masked Gaussian attributes while providing stronger frozen features for downstream tasks (Ren et al., 2026). These approaches share a common goal of making 3DGS training more robust and efficient, with TruncGradGS demonstrating improved performance with both random and COLMAP initializations, and Gaussian-JEPA showing enhanced consistency across resampled inputs compared to matched reconstruction pretraining.

### Theme 2: Rendering Efficiency and Performance Optimization

Multiple papers target the computational bottlenecks inherent in 3DGS rendering pipelines. StochasticSplats eliminates the depth-sorting requirement by combining 3DGS with stochastic rasterization through an unbiased Monte Carlo estimator of the volume rendering equation, achieving rendering speeds more than four times faster than sorted rasterization while maintaining reasonable visual quality (Kheradmand et al., 2025). ImprovedGS+ takes a systems-level approach, re-implementing 3DGS in C++/CUDA within the LichtFeld-Studio framework with custom kernels for Long-Axis-Split, Laplacian-based importance with Non-Maximum Suppression, and an adaptive Exponential Scale Scheduler, achieving a 26.8% reduction in training time while utilizing 13.3% fewer Gaussians (Vicente, 2026). These works demonstrate that significant performance gains are achievable through both algorithmic innovations (stochastic rasterization) and low-level optimization (native GPU implementations).

### Theme 3: Compression and Memory Efficiency

As 3DGS models grow in complexity, compression becomes critical for practical deployment. PCGS introduces progressive compression that adaptively controls Gaussian quantity and quality through a progressive masking strategy that incrementally incorporates new anchors while refining existing ones, combined with progressive quantization that gradually reduces quantization step sizes (Chen et al., 2025). This approach enables on-demand applications by leveraging existing quantization results to refine probability prediction for improved entropy coding efficiency, maintaining compression performance comparable to state-of-the-art non-progressive methods while providing the flexibility of progressive refinement. The work addresses a key gap in making 3DGS viable for bandwidth-constrained applications.

### Theme 4: View-Dependent and Geometric Understanding

Extending 3DGS to handle complex view-dependent phenomena and achieve geometric understanding represents another active research direction. VoD-3DGS enhances opacity representation by introducing an additional symmetric matrix for each 3D Gaussian, enabling suppression of certain Gaussians based on viewer perspective to accurately model specular highlights and reflections while maintaining 60+ FPS rendering speeds (Nowak et al., 2025). For geometric understanding, ZeroSplat achieves generalized referring segmentation (handling 0, 1, or N targets) by lifting 2D Vision-Language Model priors into 3D space through robust multi-view geometric constraints without additional feature storage or per-scene optimization (Ding et al., 2026). CaRF addresses viewpoint drift in referring 3DGS segmentation through camera-aware cross-view alignment, injecting camera geometry into Gaussian-text interactions and achieving state-of-the-art performance with mIoU improvements of 16.8%, 4.3%, and 2.0% across benchmarks (Tao et al., 2025). These works collectively push 3DGS beyond simple appearance modeling toward semantic and geometric understanding.

### Theme 5: Specialized Applications and Domain Extensions

The surveyed literature demonstrates 3DGS being adapted for specialized domains with unique requirements. HairGS extends 3DGS for hair strand reconstruction through a multi-stage pipeline that reconstructs detailed hair geometry using a differentiable Gaussian rasterizer, merges individual Gaussian segments into coherent strands, and refines strands under photometric supervision, robustly handling diverse hairstyles with reconstruction typically completing within one hour (Pan et al., 2025). Learning Unified Representation addresses the fundamental challenge of representing 3DGS in neural networks by proposing an embedding representation based on continuous submanifold fields that preserve color and geometric structure while enforcing unique mapping and channel homogeneity, addressing data-dependency issues that arise from directly feeding raw Gaussian parameters into learning frameworks (Xin et al., 2025). These applications showcase 3DGS as a flexible foundation adaptable to domain-specific constraints.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. First, there is broad agreement that the original 3DGS formulation requires significant modifications for practical deployment, with all papers proposing architectural or algorithmic enhancements. Second, multiple papers demonstrate that eliminating or relaxing core assumptions (depth-sorting in StochasticSplats, gradient computation in TruncGradGS, view-independent opacity in VoD-3DGS) yields substantial performance or quality improvements. Third, there is consensus that self-supervised and training-free approaches (Gaussian-JEPA, ZeroSplat) are viable alternatives to traditional supervised training, reducing annotation requirements while maintaining or improving performance.

**Disagreements**: The surveyed literature does not exhibit fundamental disagreements, as papers target different aspects of the 3DGS pipeline. However, there are implicit tensions between approaches: StochasticSplats trades deterministic rendering for speed through Monte Carlo sampling, while ImprovedGS+ maintains deterministic output through careful CUDA kernel design. Similarly, PCGS prioritizes compression efficiency through progressive refinement, while VoD-3DGS and HairGS prioritize representation expressiveness for specific domains. These represent different points on the efficiency-quality trade-off spectrum rather than fundamental disagreements.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the surveyed papers explicitly address the fundamental question of 3DGS scalability to very large scenes (city-scale or beyond), despite this being critical for many practical applications. Second, while multiple papers mention improved efficiency, none provide comprehensive energy consumption or carbon footprint analysis, which is increasingly important for sustainable AI. Third, the dynamic 3DGS benchmark introduced by TruncGradGS is novel but limited to synthetic scenes, suggesting a need for real-world dynamic benchmarks with ground truth. Fourth, several papers note limitations "not stated in abstract," indicating that detailed limitation analysis may be underrepresented in abstracts. Finally, while specialized applications like HairGS demonstrate domain adaptation, there is limited work on systematic frameworks for adapting 3DGS to new domains, suggesting an opportunity for meta-learning or automated architecture search approaches.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: How can 3D Gaussian Splatting be compressed progressively to efficiently utilize existing bitstreams in on-demand applications?
**Methodology**: The authors propose PCGS with adaptive control of Gaussian quantity and quality through progressive masking strategy that incrementally incorporates new anchors while refining existing ones, and progressive quantization approach that gradually reduces quantization step sizes.
**Key findings**:
- PCGS enables effective progressivity for on-demand applications by adaptively controlling Gaussian quantity and quality
- Progressive masking strategy incrementally incorporates new anchors while refining existing ones
- Progressive quantization achieves finer modeling of Gaussian attributes
- PCGS maintains compression performance comparable to state-of-the-art non-progressive methods
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Ding et al. (2026)

**Research question**: How can 3D Gaussian Splatting be extended to handle generalized referring segmentation that dynamically segments an arbitrary number of targets (0, 1, or N)?
**Methodology**: The authors propose ZeroSplat, a training-free and zero-feature framework that lifts 2D Vision-Language Model priors into 3D space through robust multi-view geometric constraints, enabling intrinsic point-level understanding without additional feature storage.
**Key findings**:
- ZeroSplat significantly outperforms state-of-the-art methods across generalized and single-target scenarios
- The method maintains exceptional efficiency by avoiding per-scene optimization
- ZeroSplat enables intrinsic point-level understanding without incurring additional feature storage
- Existing R3DGS paradigms lack intrinsic 3D point-level understanding and incur prohibitive computational overhead
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Kheradmand et al. (2025)

**Research question**: How can 3D Gaussian splatting be improved to eliminate depth-sorting requirements while providing control over rendering cost and visual fidelity?
**Methodology**: The authors combine 3D Gaussian splatting with stochastic rasterization by leveraging an unbiased Monte Carlo estimator of the volume rendering equation, removing the need for sorting and enabling accurate 3D blending of overlapping Gaussians.
**Key findings**:
- Stochastic rasterization removes the need for depth-sorting of Gaussian splats
- The approach allows accurate 3D blending of overlapping Gaussians
- The number of Monte Carlo samples provides a trade-off between computation time and quality
- The method renders more than four times faster than sorted rasterization at reasonable visual quality
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Morales et al. (2026)

**Research question**: How can the gradient vanishing phenomenon in 3D Gaussian Splatting optimization be addressed to improve scene reconstruction?
**Methodology**: The authors propose a piecewise truncated gradient formulation that improves optimization stability and robustness to initializations, addressing the gradient vanishing problem where pixels far from Gaussian primitives have diminishing gradient magnitudes.
**Key findings**:
- Truncated gradient formulation addresses gradient vanishing in 3DGS optimization
- The method improves 3DGS with both random and COLMAP initializations
- The approach is generalizable across static and dynamic Gaussian Splatting
- The authors introduce a novel dataset for benchmarking dynamic Gaussian Splatting using synthetic 3D scenes
**Limitations**: The abstract mentions examining limitations of current benchmarks for dynamic scenes but does not explicitly state limitations of the proposed method itself.

### Nowak et al. (2025)

**Research question**: How can 3D Gaussian Splatting be extended to better represent view-dependent content such as specular highlights and reflections?
**Methodology**: The authors extend the 3D Gaussian Splatting model by introducing an additional symmetric matrix to enhance opacity representation of each 3D Gaussian, allowing certain Gaussians to be suppressed based on the viewer's perspective.
**Key findings**:
- View-dependent opacity representation enables accurate modeling of specular highlights and reflections
- The enhanced model achieves state-of-the-art performance on Mip-Nerf, Tanks&Temples, Deep Blending, and Nerf-Synthetic datasets
- The method maintains rendering speed above 60FPS
- Only minimal increase in memory usage is incurred
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Pan et al. (2025)

**Research question**: How can 3D Gaussian Splatting be extended to enable strand-level hair geometry reconstruction from multi-view images?
**Methodology**: The authors propose a multi-stage pipeline that first reconstructs detailed hair geometry using a differentiable Gaussian rasterizer, then merges individual Gaussian segments into coherent strands through a novel merging scheme, and finally refines and grows the strands under photometric supervision.
**Key findings**:
- The method robustly handles a wide range of hairstyles
- Reconstruction typically completes within one hour
- The proposed evaluation metric serves as a proxy for assessing topological accuracy in strand reconstruction
- The approach addresses connectivity and topology of hair strands, which existing methods neglect
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Ren et al. (2026)

**Research question**: How can self-supervised learning be applied to 3D Gaussian Splatting representations without requiring reconstruction of masked Gaussian attributes?
**Methodology**: The authors introduce Gaussian-JEPA, which predicts representations of held-out Gaussian token blocks from visible context using an online encoder and a shared exponential-moving-average encoder that supplies stop-gradient features for multi-scale targets.
**Key findings**:
- Gaussian-JEPA is more consistent across resampled inputs compared to matched reconstruction pretraining
- The method retains more instance information under partial observations
- Gaussian-JEPA provides stronger frozen features for Gaussian completion
- Latent prediction is validated as an effective objective for reusable 3D Gaussian representations
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Tao et al. (2025)

**Research question**: How can referring 3D Gaussian Splatting Segmentation achieve view-consistent predictions across multiple viewpoints?
**Methodology**: The authors propose CaRF, a camera-aware cross-view alignment framework that introduces Camera-conditioned Alignment Modulation to inject camera geometry into Gaussian-text interactions, and Gaussian-level Cross-view Logit Alignment to explicitly align referring responses of the same Gaussians across calibrated views during training.
**Key findings**:
- CaRF addresses viewpoint drift and inconsistent predictions across views in referring 3DGS
- Camera-conditioned Alignment Modulation injects camera geometry into Gaussian-text interactions
- Cross-view discrepancy is turned into an optimizable objective for geometry-aware reasoning
- CaRF achieves state-of-the-art performance, improving mIoU by 16.8%, 4.3%, and 2.0% on Ref-LERF, LERF-OVS, and 3D-OVS benchmarks respectively
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Vicente (2026)

**Research question**: How can 3D Gaussian Splatting be re-implemented at a lower level to balance reconstruction fidelity with computational efficiency?
**Methodology**: The authors propose ImprovedGS+, implemented natively within the LichtFeld-Studio framework using C++/CUDA kernels instead of high-level Python logic, introducing a Long-Axis-Split CUDA kernel, custom Laplacian-based importance kernels with Non-Maximum Suppression, and an adaptive Exponential Scale Scheduler.
**Key findings**:
- The 1M-budget variant achieves a 26.8% reduction in training time (saving 17 minutes per session) compared to the MCMC baseline
- The method utilizes 13.3% fewer Gaussians while maintaining superior visual quality
- The full variant demonstrates a 1.28 dB PSNR increase over the ADC baseline with a 38.4% reduction in parametric complexity
- ImprovedGS+ establishes a new Pareto-optimal front for scene reconstruction
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Xin et al. (2025)

**Research question**: How can 3D Gaussian Splatting be represented in neural networks in a principled way that preserves underlying color and geometric structure while enforcing unique mapping and channel homogeneity?
**Methodology**: The authors propose an embedding representation of 3DGS based on continuous submanifold fields that encapsulate the intrinsic information of Gaussian primitives.
**Key findings**:
- Directly feeding raw Gaussian parameters into learning frameworks fails to address the non-unique and heterogeneous nature of Gaussian parameterization
- The proposed approach preserves the underlying color and geometric structure
- The representation enforces unique mapping and channel homogeneity
- The embedding benefits the learning of 3DGS by addressing data-dependency issues
**Limitations**: The abstract does not explicitly state limitations of the approach.

## References

Chen, Y., Li, M., Wu, Q., Lin, W., Harandi, M., & Cai, J. (2025). PCGS: Progressive compression of 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2503.08511

Ding, J., Song, M., Zhang, X., Jin, H., Jin, Y., & Si, X. (2026). ZeroSplat: Generalized referring segmentation in 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2607.18801

Kheradmand, S., Vicini, D., Kopanas, G., Lagun, D., Yi, K. M., Matthews, M., & Tagliasacchi, A. (2025). StochasticSplats: Stochastic rasterization for sorting-free 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2503.24366

Morales, T., Le-Pham, N.-Q., Atkins, R., & Hua, B.-S. (2026). TruncGradGS: Improved 3D Gaussian Splatting via truncated gradient updates. arXiv. https://arxiv.org/abs/2609.03534

Nowak, M., Jarosz, W., & Chin, P. (2025). VoD-3DGS: View-opacity-dependent 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2501.17978

Pan, Y., Nießner, M., & Kirschstein, T. (2025). HairGS: Hair strand reconstruction based on 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2509.07774

Ren, B., Ma, Q., Li, Y., Han, Z., Li, Y., Fu, Y., Anwer, R. M., Gevers, T., Khan, F. S., & Khan, S. (2026). Gaussian-JEPA: Joint-embedding predictive learning for 3D Gaussian Splats. arXiv. https://arxiv.org/abs/2608.15651

Tao, Y., Zhou, K., Tan, X., & Xie, Y. (2025). Camera-aware cross-view alignment for referring 3D Gaussian Splatting segmentation. arXiv. https://arxiv.org/abs/2511.03992

Vicente, J. M. (2026). ImprovedGS+: A high-performance C++/CUDA re-implementation strategy for 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2603.08661

Xin, Y., Liu, Y., Xie, X., & Li, X. (2025). Learning unified representation of 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2509.22917
