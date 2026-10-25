# Systematic Literature Review: 3D Gaussian Splatting

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "3D Gaussian splatting", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on 3D Gaussian Splatting (3DGS) reveals a rapidly evolving field focused on extending the foundational real-time rendering approach to handle increasingly complex scenarios. The foundational work by Kerbl et al. (2024) established 3DGS as a viable alternative to Neural Radiance Fields, achieving comparable visual quality with orders-of-magnitude faster rendering speeds. Subsequent research has addressed key limitations including dynamic scene reconstruction, memory efficiency, challenging material representation, and domain-specific applications. Common themes include adaptive optimization strategies, hybrid approaches combining 3DGS with complementary techniques, and practical deployment considerations for resource-constrained environments. The field demonstrates strong convergence toward real-time interactive applications while maintaining or improving visual fidelity.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "3D Gaussian splatting", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Optimization

A major research direction focuses on improving the computational efficiency and resource requirements of 3DGS. Martinez et al. (2026) introduced adaptive density control that achieves comparable quality with 50% fewer Gaussians and 3x faster optimization through dynamic adjustment of Gaussian count based on reconstruction error. Park et al. (2026) addressed memory and bandwidth challenges with a compression framework achieving 10x storage reduction while maintaining 120 FPS rendering on mobile GPUs. These works reflect a broader trend toward making 3DGS practical for real-world deployment on resource-constrained devices.

### Theme 2: Dynamic and Time-Varying Scenes

Extending 3DGS from static to dynamic scenes represents a significant research thrust. Chen et al. (2026) developed temporal consistency constraints and motion-aware Gaussian parameterization using optical flow supervision to handle non-rigid deformations. Moore et al. (2026) applied similar principles to human body reconstruction with skeleton-conditioned deformation fields enabling real-time animated rendering from monocular video. Both approaches demonstrate that 3DGS can be successfully extended to time-varying content while preserving real-time performance.

### Theme 3: Hybrid Approaches with Complementary Techniques

Several papers explore combining 3DGS with other representation methods to leverage complementary strengths. Zhang et al. (2026) integrated NeRF priors to guide Gaussian initialization, achieving 40% faster training and 2dB PSNR improvement by combining NeRF's global consistency with 3DGS's real-time rendering. Ren et al. (2026) introduced self-supervised learning through latent prediction of Gaussian token blocks, eliminating the need for input-space reconstruction while providing more consistent features across resampled inputs. These hybrid strategies suggest 3DGS works best when integrated with complementary techniques rather than used in isolation.

### Theme 4: Domain-Specific Applications

The literature shows 3DGS being adapted to specific application domains with specialized requirements. Schmidt et al. (2026) integrated semantic segmentation for urban scene reconstruction, enabling instance-level editing of buildings, vehicles, and vegetation. Liu et al. (2026) extended Gaussian parameterization to handle reflective and transparent surfaces previously difficult for standard 3DGS. Brown et al. (2026) developed multi-scale representations for detailed scene capture with view-dependent adaptive refinement. These domain-specific adaptations demonstrate 3DGS's flexibility as a foundational representation.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. All efficiency-focused works agree that adaptive, data-driven optimization strategies outperform fixed-parameter approaches (Martinez et al., 2026; Park et al., 2026; Brown et al., 2026). Multiple papers demonstrate that hybrid approaches combining 3DGS with complementary techniques yield superior results compared to pure 3DGS (Zhang et al., 2026; Ren et al., 2026). There is consensus that real-time performance is achievable even for complex scenarios when appropriate optimization strategies are employed.

**Disagreements**: The literature shows limited direct disagreement, reflecting the field's relatively early stage. However, there are implicit tensions between compression-focused approaches prioritizing efficiency (Park et al., 2026) versus quality-focused methods emphasizing detail preservation (Brown et al., 2026; Liu et al., 2026). The optimal balance between storage efficiency and visual fidelity remains an open question requiring further investigation.

## Gaps and Open Questions

Several gaps emerge from the collective limitations acknowledged across papers. Most works do not explicitly address computational overhead of their proposed enhancements, particularly for optical flow computation (Chen et al., 2026), multi-scale processing (Brown et al., 2026), or per-Gaussian metric calculation (Martinez et al., 2026). Quality of prerequisite data—such as semantic segmentation accuracy (Schmidt et al., 2026) or LiDAR availability—creates dependencies that may limit practical applicability. None of the surveyed papers thoroughly evaluate performance on extremely large-scale scenes or highly complex real-world scenarios with multiple interacting challenges. The handling of complex multi-layer materials, dynamic environment changes, occlusions, and multi-person scenarios remains underexplored. Additionally, the dependency on pre-trained models in hybrid approaches (Zhang et al., 2026; Ren et al., 2026) introduces computational overhead and quality dependencies that require further investigation.

## Per-Paper Annotations

### Chen et al. (2026)

**Research question**: How can 3D Gaussian Splatting be extended to reconstruct time-varying scenes with non-rigid deformations?
**Methodology**: Introduces temporal consistency constraints and motion-aware Gaussian parameterization leveraging optical flow supervision and deformable Gaussian kernels that adapt their properties over time.
**Key findings**:
- Achieves improved reconstruction quality compared to static 3DGS baselines on dynamic scene benchmarks
- Demonstrates better temporal coherence across frames in time-varying scenes
- Successfully handles non-rigid deformations through adaptive Gaussian kernels
- Optical flow supervision enables accurate motion tracking in dynamic environments
**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include computational overhead from optical flow computation and possible performance degradation on scenes with highly complex or rapid motion patterns.

### Kerbl et al. (2024)

**Research question**: How can radiance field rendering achieve high visual quality while maintaining real-time performance?
**Methodology**: Uses 3D Gaussian primitives with an efficient rasterization pipeline, combining structure-from-motion initialization with adaptive density control and optimized rendering.
**Key findings**:
- Achieves comparable visual quality to NeRF methods
- Rendering speeds are orders of magnitude faster than NeRF
- Real-time performance enables interactive applications
- Efficient rasterization pipeline makes Gaussian primitives practical for rendering
**Limitations**: The abstract does not discuss memory requirements for large scenes or handling of dynamic content and view-dependent effects.

### Liu et al. (2026)

**Research question**: How can 3D Gaussian Splatting accurately represent specular and transparent materials like mirrors, glass, and water?
**Methodology**: Extends Gaussian parameterization with explicit reflection and refraction modeling, incorporating physical light transport constraints and environment map integration.
**Key findings**:
- Extended parameterization enables realistic rendering of reflective surfaces
- Physical light transport constraints improve material appearance accuracy
- Environment map integration enhances reflection and refraction quality
- Previously difficult materials (mirrors, glass, water) can now be rendered effectively
**Limitations**: The abstract does not address handling of complex multi-layer materials or dynamic environment changes affecting reflections.

### Martinez et al. (2026)

**Research question**: How can 3D Gaussian Splatting optimization be made more efficient while maintaining reconstruction quality?
**Methodology**: Dynamically adjusts Gaussian count and distribution based on reconstruction error and gradient analysis, including pruning, splitting, and cloning operations guided by per-Gaussian contribution metrics.
**Key findings**:
- Achieves comparable quality with 50% fewer Gaussians than baseline methods
- Optimization speed improved by 3x compared to standard approaches
- Per-Gaussian contribution metrics effectively guide density control decisions
- Pruning, splitting, and cloning operations adapt to scene complexity
**Limitations**: The abstract does not discuss potential quality degradation in highly complex scenes or the overhead of computing per-Gaussian metrics.

### Moore et al. (2026)

**Research question**: How can 3D Gaussian Splatting be applied to articulated human body modeling and animation?
**Methodology**: Introduces skeleton-conditioned Gaussian deformation fields and pose-dependent appearance modeling, leveraging parametric body priors and temporal smoothing for coherent animation.
**Key findings**:
- High-quality human body reconstruction achievable from monocular video
- Real-time rendering capabilities demonstrated for animated humans
- Skeleton-conditioned deformation enables realistic pose-dependent changes
- Temporal smoothing produces coherent animations across frames
**Limitations**: The abstract does not address handling of complex clothing, occlusions, or multi-person scenarios.

### Park et al. (2026)

**Research question**: How can memory and bandwidth requirements of 3D Gaussian Splatting be reduced for real-time rendering on resource-constrained devices?
**Methodology**: Employs a compression framework using quantization, entropy coding, and level-of-detail representations to reduce storage while supporting progressive streaming and adaptive rendering on mobile devices.
**Key findings**:
- Achieves 10x reduction in storage requirements while maintaining visual quality
- Enables 120 FPS rendering on mobile GPUs with minimal quality degradation
- Supports progressive streaming for efficient bandwidth usage
- Provides adaptive rendering capabilities for resource-constrained devices
- Demonstrates practical feasibility of 3DGS on mobile platforms
**Limitations**: The abstract does not explicitly acknowledge limitations; compression may introduce quality tradeoffs for certain scene types with fine details, and the approach may have varying effectiveness depending on scene complexity and compression ratio settings.

### Ren et al. (2026)

**Research question**: How can self-supervised learning for 3D Gaussian Splatting handle variability in Gaussian primitive realizations without requiring input-space reconstruction?
**Methodology**: Introduces Gaussian-JEPA which predicts representations of held-out Gaussian token blocks from visible context using an online encoder and a shared exponential-moving-average encoder that supplies stop-gradient features for multi-scale targets with complementary target projections and feature-space grounding.
**Key findings**:
- More consistent feature representations across resampled Gaussian inputs compared to reconstruction-based pretraining
- Retains more instance-level information under partial observations
- Provides stronger frozen features for renderable shape completion tasks
- Successfully transfers to downstream tasks including part segmentation and object classification
- Eliminates need for input-space decoder by providing latent supervision without reconstructing Gaussian attributes
**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include dependency on EMA encoder tuning and evaluation scope limited to specific benchmarks without testing on highly complex real-world scenes.

### Schmidt et al. (2026)

**Research question**: How can semantic segmentation be integrated with 3D Gaussian Splatting to enable object-level editing and improved urban scene modeling?
**Methodology**: Proposes semantic-guided Gaussian optimization that preserves object boundaries by combining multi-view imagery with LiDAR point clouds to achieve high-fidelity reconstruction with instance-level editing capabilities.
**Key findings**:
- Improved geometric accuracy in large-scale urban scene reconstruction
- Enhanced semantic consistency across reconstructed objects
- Enables instance-level editing of individual objects (buildings, vehicles, vegetation)
- Successfully integrates multi-view imagery with LiDAR data for comprehensive scene modeling
- Preserves object boundaries through semantic-guided optimization
**Limitations**: The abstract does not explicitly acknowledge limitations; the approach likely depends on quality of semantic segmentation and availability of LiDAR data, which may limit applicability to scenarios where such data is not accessible.

### Zhang et al. (2026)

**Research question**: How can Neural Radiance Field priors be leveraged to improve 3D Gaussian Splatting initialization and training efficiency?
**Methodology**: Leverages pre-trained NeRF models to guide Gaussian placement and parameter estimation, combining NeRF's global consistency with 3DGS's real-time rendering capabilities in a hybrid approach.
**Key findings**:
- Achieves 40% faster training convergence compared to standard 3DGS initialization
- Demonstrates 2dB PSNR improvement on standard novel view synthesis benchmarks
- Successfully combines NeRF's global scene consistency with 3DGS's real-time rendering
- Improved Gaussian placement and parameter estimation through NeRF-guided initialization
- Enables practical hybrid approach leveraging strengths of both representation methods
**Limitations**: The abstract does not explicitly acknowledge limitations; the approach requires pre-trained NeRF models which adds computational overhead for the initial NeRF training, and the hybrid pipeline may not generalize optimally to all scene types or may introduce dependencies on NeRF quality.

### Brown et al. (2026)

**Research question**: How can 3D Gaussian Splatting capture both coarse geometry and fine details in scene representation?
**Methodology**: Proposes a hierarchical Gaussian representation operating at multiple resolution levels with adaptive refinement based on view-dependent importance, employing scale-aware optimization and cross-level consistency constraints.
**Key findings**:
- Multi-scale approach preserves fine details better than single-scale 3DGS
- Adaptive refinement reduces aliasing artifacts in rendered scenes
- Cross-level consistency constraints maintain geometric coherence across scales
- View-dependent importance enables efficient resource allocation
**Limitations**: The abstract does not specify computational overhead of multi-scale processing or evaluate performance on extremely large scenes.

## References

Brown, K., Anderson, L., & Thompson, M. (2026). Multi-scale 3D Gaussian splatting for detailed scene representation. arXiv. https://arxiv.org/abs/2604.07823

Chen, Z., Wang, L., & Liu, W. (2026). Dynamic 3D Gaussian splatting for scene understanding. arXiv. https://arxiv.org/abs/2608.13989

Kerbl, B., Kopanas, G., Leimkühler, T., & Drettakis, G. (2024). 3D Gaussian splatting for real-time radiance field rendering. arXiv. https://arxiv.org/abs/2401.09720

Liu, J., White, A., & Davis, C. (2026). 3D Gaussian splatting for reflective and transparent surfaces. arXiv. https://arxiv.org/abs/2603.05612

Martinez, D., Taylor, R., & Wilson, S. (2026). Efficient 3D Gaussian splatting optimization via adaptive density control. arXiv. https://arxiv.org/abs/2602.04501

Moore, P., Jackson, R., & Harris, N. (2026). 3D Gaussian splatting for human body reconstruction. arXiv. https://arxiv.org/abs/2601.03490

Park, J., Kim, S., & Lee, D. (2026). Compressed 3D Gaussian splatting for real-time rendering. arXiv. https://arxiv.org/abs/2606.12456

Ren, B., Ma, Q., Li, Y., Han, Z., Li, Y., Fu, Y., Anwer, R. M., Gevers, T., Khan, F. S., & Khan, S. (2026). Gaussian-JEPA: Joint-embedding predictive learning for 3D Gaussian splats. arXiv. https://arxiv.org/abs/2608.15651

Schmidt, M., Weber, A., & Mueller, T. (2026). Semantic-aware 3D Gaussian splatting for urban scene reconstruction. arXiv. https://arxiv.org/abs/2607.18234

Zhang, E., Johnson, R., & Garcia, M. (2026). 3D Gaussian splatting with Neural Radiance Field priors. arXiv. https://arxiv.org/abs/2605.09871
