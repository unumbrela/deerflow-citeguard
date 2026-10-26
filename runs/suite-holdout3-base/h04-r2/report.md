# Systematic Literature Review: Neural Radiance Fields

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "neural radiance fields", filtered to category cs.CV, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on Neural Radiance Fields (NeRF) from 2024-2026 reveals a field rapidly maturing beyond novel view synthesis into specialized application domains and robust real-world deployment. Recent research addresses three critical challenges: (1) uncertainty quantification for safety-critical applications, (2) computational efficiency for accessibility, and (3) domain-specific adaptations for forestry, medical imaging, hyperspectral imaging, and temporal scene modeling. The surveyed papers collectively demonstrate that NeRF technology has moved from proof-of-concept demonstrations to practical tools tackling concrete problems like motion blur removal, lens flare correction, and few-shot generalization. However, significant gaps remain in hardware requirements, computational costs, and validation across diverse real-world scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "neural radiance fields", filtered to category cs.CV, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Uncertainty Quantification and Trustworthiness

A critical direction in NeRF research addresses the fundamental question of when and how much to trust NeRF reconstructions. Duan and Wong (2026) introduced Evidential Neural Radiance Fields, which separately quantify both aleatoric (data) and epistemic (model) uncertainties from a single forward pass without compromising rendering quality. This represents a significant advance over prior methods that either captured only one uncertainty type or required multiple forward passes with significant computational overhead. The ability to estimate uncertainty is essential for deploying NeRFs in safety-critical applications such as autonomous vehicles, medical imaging, and robotics, where knowing the confidence bounds of 3D reconstructions is as important as the reconstructions themselves.

### Theme 2: Computational Efficiency and Accessibility

Multiple papers address the computational barriers that have limited NeRF adoption. Huang et al. (2026) conducted a systematic comparative study of accelerated NeRF variants (DS-NeRF, TensoRF, HashNeRF) in low-compute, low-data regimes, exploring extensions like depth supervision and architectural modifications. While their proposed extensions did not conclusively outperform baselines under iso-time evaluation, the work provides valuable characterization of which techniques transfer to constrained settings. This line of research is essential for democratizing NeRF technology beyond well-resourced labs and enabling deployment on edge devices.

### Theme 3: Domain-Specific Applications

The surveyed literature demonstrates NeRF's expansion into diverse application domains:

**Forestry and Environmental Monitoring**: Castorena (2024) showed that NeRFs can express fine features of forest 3D structure, fuse remote sensing modalities, and improve forest metrics derived from 3D structure. This positions NeRF as a computational tool for advancing scalability and accuracy of forest monitoring programs.

**Medical Imaging**: Wang et al. (2024) surveyed NeRF applications in medical imaging, identifying four critical challenges: fundamental imaging principles, inner structure requirements, object boundary definition, and color density significance. The unique requirements of medical imaging—such as the need to visualize internal structures rather than just surfaces—demand specialized adaptations of the NeRF framework.

**Hyperspectral Imaging**: Chen et al. (2024) extended NeRF to hyperspectral reconstruction, where every point in space is characterized by wavelength-dependent radiance and transmittance spectra. This enables both spatial and spectral information recovery, addressing common hyperspectral imaging challenges with non-Lambertian surfaces and translucent objects.

### Theme 4: Robustness to Real-World Imaging Challenges

Several papers address NeRF's robustness to imaging artifacts that commonly occur in real-world capture:

**Motion Blur**: Qi et al. (2024) proposed EBAD-NeRF, which leverages event cameras to jointly optimize learnable poses and NeRF parameters under motion blur. By using an intensity-change-metric event loss and photo-metric blur loss, their method obtains accurate camera trajectories during exposure time and learns sharper 3D representations than prior deblurring approaches.

**Lens Flare**: Matta et al. (2024) framed flare removal as a multi-view problem within the Generalizable NeRF Transformer framework. Their GN-FR method renders flare-free views from sparse flare-corrupted inputs by leveraging the view-dependent nature of flare artifacts, introducing the first 3D multi-view flare dataset with 17 real scenes.

**Large-Scale Scenes**: Ni et al. (2024) addressed reconstruction in complex and large-scale scenes with Torch-NeRF, which enlarges the ray perception field by rendering patches of pixels simultaneously and replaces the standard MLP with distance-aware convolutions for enhanced feature propagation.

### Theme 5: Temporal and Dynamic Scene Modeling

TimeNeRF (Hung et al., 2025) addresses the underexplored problem of temporal 3D scene modeling, enabling rendering at arbitrary viewpoints and arbitrary times from few-shot inputs. By combining multi-view stereo, NeRF, and disentanglement strategies, TimeNeRF constructs implicit content radiance fields that capture natural scene transitions from dawn to dusk without per-scene optimization. This capability is critical for applications in the metaverse and immersive experiences where environments must transition naturally across time.

### Theme 6: Semantic Understanding and Scene Interpretation

Nguyen et al. (2024) comprehensively reviewed semantically-aware NeRFs, which integrate semantic labels as viewpoint-invariant functions mapping spatial coordinates to semantic categories. This enables not just novel view synthesis but also scene understanding tasks including panoptic segmentation, 3D bounding box prediction, scene editing, and object-centric 3D model extraction. The integration of semantics transforms NeRF from a purely geometric/photometric representation into a structured scene understanding system.

## Convergences and Disagreements

**Convergences**:
- Multiple papers agree that NeRFs require domain-specific adaptations for specialized applications (medical, forestry, hyperspectral), as the vanilla NeRF formulation assumes natural images with specific properties that do not hold in these domains.
- There is consensus that computational efficiency remains a critical barrier to widespread NeRF adoption, motivating research into accelerated variants and low-data regimes.
- Several papers converge on the view that multi-view information is underutilized in single-image approaches, and that leveraging view-dependent phenomena (as in flare removal and deblurring) significantly improves results.

**Disagreements**:
- The literature reveals tension between specialization and generalization: while some papers (e.g., TimeNeRF, GN-FR) pursue generalizable NeRFs that work across scenes without per-scene optimization, others focus on maximizing quality for specific domains with specialized architectures.
- There is implicit disagreement about the role of specialized hardware: EBAD-NeRF requires event cameras, hyperspectral NeRF requires hyperspectral cameras, while other works aim to improve results from standard RGB inputs alone.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Hardware Dependencies**: Multiple approaches (event cameras for deblurring, hyperspectral cameras for spectral NeRF) require specialized sensors that limit practical deployment. Methods that achieve similar improvements from standard RGB cameras remain an open challenge.

2. **Quantitative Benchmarks**: Several papers acknowledge limited quantitative comparisons to baselines or evaluation on narrow benchmark sets. Standardized benchmarks across diverse real-world scenarios are needed.

3. **Computational Costs**: While efficiency is widely acknowledged as important, few papers report detailed computational analysis or achieve substantial speedups without quality tradeoffs.

4. **Real-World Validation**: Many methods are validated primarily on synthetic data or controlled captures. Performance in uncontrolled, real-world environments with diverse lighting, weather, and scene complexity remains underexplored.

5. **Integration of Multiple Capabilities**: Current methods typically address single challenges (uncertainty OR deblurring OR temporal modeling). Integrated systems that simultaneously handle multiple real-world challenges are largely absent.

6. **Few-Shot Generalization Limits**: While TimeNeRF and GN-FR demonstrate few-shot capabilities, the boundaries of generalization—what scene types, viewing conditions, and domain shifts are tolerable—remain poorly characterized.

## Per-Paper Annotations

### Castorena (2024)

**Research question**: Can neural radiance fields improve upon existing remote sensing methods for forestry applications and forest monitoring?

**Methodology**: The work presents experiments demonstrating NeRF's potential to express fine features of forest 3D structure, fuse available remote sensing modalities, and improve upon 3D structure-derived forest metrics.

**Key findings**:
- NeRFs can express fine features of forest 3D structure
- NeRFs can fuse available remote sensing modalities effectively
- NeRFs improve upon 3D structure-derived forest metrics
- Neural fields offer a wide range of possibilities to improve existing remote sensing methods in forest monitoring
- Neural fields are attractive computational tools for advancing scalability and accuracy of forest monitoring programs

**Limitations**: The abstract presents potential capabilities rather than fully validated results; specific experimental details, dataset scales, and quantitative improvements over baselines are not specified.

### Chen et al. (2024)

**Research question**: Can Neural Radiance Fields be extended to create 3D hyperspectral reconstructions that provide both spatial and spectral information?

**Methodology**: Proposed hyperspectral NeRF that computes wavelength-dependent radiance and transmittance spectra for every point in space and view direction, evaluated on a collected dataset of nearly 2000 hyperspectral images across 8 scenes and 2 cameras.

**Key findings**:
- Enables fast, accurate volumetric 3D hyperspectral scene reconstruction
- Every point in space and view direction characterized by wavelength-dependent radiance and transmittance spectra
- Outperforms traditional RGB NeRF baselines in hyperspectral reconstruction tasks
- Demonstrates potential for hyperspectral super-resolution applications
- Enables imaging sensor simulation and mitigates common HSI challenges with non-Lambertian surfaces and translucent objects

**Limitations**: Requires specialized hyperspectral camera data which has technological limitations; the approach depends on recent NeRF advances and may not address all traditional 3D reconstruction challenges with HSI.

### Duan and Wong (2026)

**Research question**: How can Neural Radiance Fields separately capture both aleatoric and epistemic uncertainties without compromising rendering quality or incurring significant computational overhead?

**Methodology**: The authors introduce Evidential Neural Radiance Fields, a probabilistic approach that seamlessly integrates with the NeRF rendering process, enabling direct quantification of both uncertainty types from a single forward pass.

**Key findings**:
- The approach demonstrates state-of-the-art scene reconstruction fidelity across three standardized benchmarks
- The method achieves state-of-the-art uncertainty estimation quality
- Both aleatoric and epistemic uncertainties are captured simultaneously from a single forward pass
- The approach does not compromise rendering quality compared to existing methods
- The method avoids significant computational overhead for obtaining uncertainty estimates

**Limitations**: The abstract does not explicitly acknowledge limitations; evaluation is limited to three standardized benchmarks which may not reflect all real-world deployment scenarios.

### Huang et al. (2026)

**Research question**: How can accelerated NeRF variants be adapted and extended for low-compute, low-data regimes?

**Methodology**: Conduct a comparative study of three accelerated NeRF variants (DS-NeRF, TensoRF, HashNeRF) with proposed extensions including depth-supervision loss for TensoRF, MLP architecture ablation, and four HashNeRF network variants with residual and convolutional designs.

**Key findings**:
- Added depth-supervision loss derived from COLMAP keypoints to TensoRF and evaluated on LLFF dataset under reduced view counts
- Ablation studies revealed the effect of input downsampling on PSNR and runtime for synthetic Lego scene
- Four architectural variants of HashNeRF color and density networks were proposed and evaluated
- Under iso-time evaluation, none of the extensions conclusively outperformed the published baselines
- Experiments characterized which extensions transfer to constrained settings and identified design questions for future work

**Limitations**: None of the proposed extensions conclusively outperformed existing baselines under iso-time evaluation, suggesting limited immediate practical benefit for constrained settings.

### Hung et al. (2025)

**Research question**: Can we build generalizable NeRFs that render novel views at arbitrary viewpoints and times from few-shot input views without per-scene optimization?

**Methodology**: TimeNeRF harnesses multi-view stereo, neural radiance fields, and disentanglement strategies across diverse datasets to construct an implicit content radiance field for scene representation, enabling neural radiance field construction at arbitrary times with novel view synthesis via volume rendering.

**Key findings**:
- TimeNeRF renders novel views in a few-shot setting without per-scene optimization
- The method creates realistic novel views that transition smoothly across different times
- It captures intricate natural scene changes from dawn to dusk effectively
- The approach addresses the lack of dedicated datasets for temporal 3D scene modeling
- Real-world applications benefit from reduced cost in collecting multiple views and avoiding re-optimization for unseen scenes

**Limitations**: The few-shot input constraint may limit performance in certain scenarios; the abstract does not specify computational requirements, generalization boundaries across scene types, or quantitative comparisons with temporal NeRF baselines.

### Matta et al. (2024)

**Research question**: How can lens flare artifacts be effectively removed from images by leveraging multi-view information rather than single-image approaches?

**Methodology**: Frame flare removal as a multi-view problem using the Generalizable NeRF Transformer framework with Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules, plus a masking loss function for unsupervised learning.

**Key findings**:
- Successfully renders flare-free views from sparse sets of flare-corrupted input images
- Generalizes across different scenes in an unsupervised manner without requiring paired flare-free training data
- Introduced the first 3D multi-view flare dataset with 17 real scenes, 782 images, 80 flare patterns, and annotated flare-occupancy masks
- Leverages view-dependent nature of flare artifacts to recover details obscured in individual images
- First work to address flare removal within a Neural Radiance Fields framework

**Limitations**: As the first work addressing flare removal in NeRF framework, comparisons to prior methods are limited; the unsupervised masking approach may have constraints in handling complex flare patterns without ground truth supervision.

### Ni et al. (2024)

**Research question**: How can NeRF be improved to handle complex and large-scale scene reconstruction where background variance and limited contextual information pose challenges?

**Methodology**: Propose Torch-NeRF that enlarges ray perception field by having each camera ray render a patch of pixels simultaneously, and replace the standard MLP with distance-aware convolutions to enhance feature propagation among sample points on each ray.

**Key findings**:
- Novel inference pattern enables single camera rays to possess more contextual information by rendering patches instead of individual pixels
- Distance-aware convolutions enhance feature propagation among sample points from the same camera ray
- Successfully addresses background variance challenges in complex scenes
- Extensive experiments on KITTI-360 and LLFF datasets demonstrate excellent performance
- Enables better reconstruction in complex and large-scale scenes compared to prevalent small-scale methods

**Limitations**: The patch-based rendering approach may increase computational requirements; performance on extremely large-scale outdoor scenes beyond KITTI-360 and LLFF remains to be validated.

### Nguyen et al. (2024)

**Research question**: How do semantically-aware Neural Radiance Fields contribute to visual scene understanding, and what applications do they enable?

**Methodology**: This comprehensive review analyzes over 250 scholarly papers on semantically-aware NeRFs, exploring how they infer 3D representations for stationary and dynamic objects, with semantic labels functioning as viewpoint-invariant functions mapping spatial coordinates to semantic labels.

**Key findings**:
- NeRFs adeptly infer 3D representations for both stationary and dynamic objects in a scene
- Semantic labels serve as viewpoint-invariant functions that facilitate recognition of distinct objects within scenes
- Applications include novel viewpoint generation, scene inpainting, panoptic segmentation, 3D bounding box prediction, 3D scene editing, and object-centric 3D model extraction
- The survey highlights significant progression in semantically-aware NeRF applications for visual scene interpretation
- The capability is pivotal for generating high-quality new viewpoints and completing missing scene details

**Limitations**: As a review paper, it synthesizes existing work rather than proposing novel methods; the analysis of 250+ papers may not capture all relevant research, and specific gaps or future directions are not detailed in the abstract.

### Qi et al. (2024)

**Research question**: How can motion blur in images be addressed to improve NeRF reconstruction quality in low-light and high-speed motion scenes?

**Methodology**: The authors propose Event-driven Bundle Adjustment for Deblurring Neural Radiance Fields (EBAD-NeRF) that jointly optimizes learnable poses and NeRF parameters using hybrid event-RGB data, with an intensity-change-metric event loss and a photo-metric blur loss to explicitly model camera motion blur.

**Key findings**:
- EBAD-NeRF obtains accurate camera trajectory during exposure time
- The method learns sharper 3D representations compared to prior works
- Event cameras compensate for information deficiency in pose and lighting estimation during exposure
- The approach works effectively on both synthetic and real-captured data
- Previous deblurring NeRF methods struggle with pose and lighting estimation during exposure time, which EBAD-NeRF addresses

**Limitations**: The method requires event camera data, which limits applicability to scenarios where such specialized hardware is available; standard RGB-only setups cannot benefit from this approach.

### Wang et al. (2024)

**Research question**: What are the unique challenges and opportunities when applying Neural Radiance Fields to medical imaging applications?

**Methodology**: Comprehensive survey examining NeRF applications in medical imaging, identifying four key challenges, reviewing current methods across different organs, and analyzing datasets and evaluation metrics.

**Key findings**:
- NeRF offers significant potential for synthesizing 3D representations from 2D medical image data
- Four imminent challenges identified: fundamental imaging principles, inner structure requirements, object boundary definition, and color density significance
- Current methods reviewed across different organ systems with associated limitations documented
- Existing datasets and evaluation metrics for medical NeRF applications catalogued
- Several promising directions proposed for future research in medical NeRF applications

**Limitations**: As a survey paper, does not propose novel solutions; medical NeRF applications face fundamental challenges due to differences between natural and medical imaging that remain unresolved.

## References

Castorena, J. (2024). Learning neural radiance fields of forest structure for scalable and fine monitoring. arXiv. https://arxiv.org/abs/2401.15029

Chen, G., Narayanan, S. K., Ottou, T. G., Missaoui, B., Muriki, H., Pradalier, C., & Chen, Y. (2024). Hyperspectral neural radiance fields. arXiv. https://arxiv.org/abs/2403.14839

Duan, R., & Wong, A. (2026). Evidential neural radiance fields. arXiv. https://arxiv.org/abs/2602.23574

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-cost neural radiance fields. arXiv. https://arxiv.org/abs/2605.09312

Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building generalizable neural radiance fields across time from few-shot input views. arXiv. https://arxiv.org/abs/2507.13929

Matta, G. R., Siddartha, R., Girish, R. S. V., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable neural radiance fields for flare removal. arXiv. https://arxiv.org/abs/2412.08200

Ni, B., Wang, H., Bai, D., Weng, M., Qi, D., Qiu, W., & Liu, B. (2024). Neural radiance fields with torch units. arXiv. https://arxiv.org/abs/2404.02617

Nguyen, T.-A.-Q., Bourki, A., Macudzinski, M., Brunel, A., & Bennamoun, M. (2024). Semantically-aware neural radiance fields for visual scene understanding: A comprehensive review. arXiv. https://arxiv.org/abs/2402.11141

Qi, Y., Zhu, L., Zhao, Y., Bao, N., & Li, J. (2024). Deblurring neural radiance fields with event-driven bundle adjustment. arXiv. https://arxiv.org/abs/2406.14360

Wang, X., Chen, Y., Hu, S., Fan, H., Zhu, H., & Li, X. (2024). Neural radiance fields in medical imaging: A survey. arXiv. https://arxiv.org/abs/2402.17797
