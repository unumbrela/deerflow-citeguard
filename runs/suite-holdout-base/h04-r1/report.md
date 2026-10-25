# Systematic Literature Review: Neural Radiance Fields

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "neural radiance fields", category cs.CV, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Neural Radiance Fields (NeRF) have evolved significantly over the past two years, expanding beyond novel view synthesis into specialized domains including medical imaging, remote sensing, hyperspectral reconstruction, and uncertainty quantification. The surveyed literature reveals a field maturing from proof-of-concept demonstrations toward practical applications addressing real-world constraints such as motion blur, lens flare, limited computational resources, and temporal dynamics. A dominant trend involves extending NeRF architectures to handle degraded or sparse input data through multi-view fusion, event-based sensing, and generalizable representations that eliminate per-scene optimization. Simultaneously, researchers are exploring semantic integration, enabling scene understanding and editing capabilities that transcend pure geometric reconstruction. While rendering quality and training efficiency have improved, key challenges remain in deploying NeRF systems to safety-critical applications, acquiring specialized sensor data, and standardizing evaluation protocols across emerging application domains.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "neural radiance fields", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search was restricted to cs.CV, potentially excluding relevant work in adjacent categories such as cs.LG or eess.IV that may have primary contributions to NeRF methodology.

## Themes

### Theme 1: Uncertainty Quantification and Trustworthiness

As NeRF technology approaches deployment in safety-critical settings, understanding and quantifying uncertainty has emerged as a fundamental concern. Duan and Wong (2026) directly address this gap by introducing Evidential Neural Radiance Fields, which quantify both aleatoric (data-driven) and epistemic (model-driven) uncertainties from a single forward pass without compromising rendering quality. This probabilistic approach represents a significant advance over prior methods that either captured only one uncertainty type or required multiple forward passes, incurring computational overhead. The work demonstrates state-of-the-art performance on standardized benchmarks, suggesting that uncertainty-aware NeRF systems can maintain high reconstruction fidelity while providing reliable confidence estimates. This theme reflects a broader maturation of the field from purely accuracy-driven metrics toward deployment-ready systems that can articulate their own limitations.

### Theme 2: Handling Degraded and Sparse Input Data

A substantial portion of recent NeRF research addresses the challenge of reconstructing high-quality 3D representations from imperfect input data. Multiple papers tackle different forms of degradation: Qi et al. (2024) focus on motion blur using event cameras, Matta et al. (2024) address lens flare through multi-view fusion, and Huang et al. (2026) explore low-compute, low-data regimes. These works share a common strategy of leveraging complementary information sources—whether temporal data from event sensors, view-dependent flare patterns, or depth supervision from sparse keypoints—to compensate for missing or corrupted information. The EBAD-NeRF approach (Qi et al., 2024) exemplifies this trend by jointly optimizing camera poses and NeRF parameters using hybrid event-RGB data, achieving sharper reconstructions than prior deblurring methods. Similarly, GN-FR (Matta et al., 2024) exploits the view-dependent nature of lens flare to recover occluded details from neighboring views in an unsupervised manner. These advances collectively push NeRF toward robustness in real-world capture conditions where ideal multi-view datasets are unavailable.

### Theme 3: Domain-Specific Applications

The surveyed literature demonstrates NeRF's expansion into specialized application domains beyond traditional computer vision benchmarks. Castorena (2024) applies NeRF to forest monitoring, showing that neural fields can express fine 3D structural features and fuse multiple remote sensing modalities to improve forestry metrics. Wang et al. (2024) survey NeRF applications in medical imaging, identifying unique challenges such as inner structure requirements, object boundary definition, and the mismatch between NeRF's color-density representation and medical imaging's physical principles. Chen et al. (2024) extend NeRF to hyperspectral imaging, enabling wavelength-dependent radiance and transmittance at every spatial point—a capability with significant potential for material and chemical composition analysis. These domain-specific adaptations reveal that NeRF's core strength—continuous volumetric representation from sparse projections—translates across diverse sensing modalities, but each domain introduces constraints requiring architectural modifications and new evaluation protocols.

### Theme 4: Generalization and Few-Shot Learning

Eliminating the need for per-scene optimization has emerged as a critical research direction for practical NeRF deployment. Hung et al. (2025) present TimeNeRF, a generalizable approach that renders novel views at arbitrary viewpoints and times from few-shot inputs, addressing the prohibitive cost of collecting dense multi-view data for real-world applications. Their method harnesses multi-view stereo, neural radiance fields, and disentanglement strategies to construct implicit content radiance fields without scene-specific retraining. Similarly, Matta et al. (2024) demonstrate that GN-FR generalizes across different scenes in an unsupervised manner, leveraging the Generalizable NeRF Transformer framework. This shift from optimization-based to generalizable NeRF reflects a broader trend in neural rendering toward models that can handle unseen scenes without expensive per-scene training, enabling applications where rapid deployment and data efficiency are paramount.

### Theme 5: Temporal and Dynamic Scene Modeling

Capturing temporal dynamics in 3D scenes represents a frontier where NeRF research is actively expanding. Hung et al. (2025) explicitly address this with TimeNeRF, which models natural scene transitions across times of day, capturing dawn-to-dusk changes from few-shot inputs. Their work highlights a significant gap in the literature: the lack of dedicated datasets for temporal 3D scene modeling, which has limited progress in this area. The ability to render photorealistic transitions between temporal states has implications for immersive experiences in digital environments and the metaverse, where static 3D reconstructions are insufficient for representing naturally evolving scenes. This theme intersects with generalization, as temporal modeling requires learning representations that separate time-varying content from static scene structure.

### Theme 6: Architectural Innovations for Context and Efficiency

Improving NeRF's architectural foundations continues to yield performance gains in challenging scenarios. Ni et al. (2024) propose Torch-NeRF, which replaces the standard MLP with distance-aware convolutions and enables each camera ray to render a patch of pixels rather than a single point, capturing contextual information that pixel-independent inference misses. This approach directly addresses limitations in complex, large-scale scenes where background variance across views challenges conventional NeRF formulations. Huang et al. (2026) conduct systematic ablation studies on accelerated NeRF variants, exploring architectural modifications such as residual and convolutional designs in HashNeRF networks. While their extensions did not conclusively outperform baselines under iso-time evaluation, the work characterizes which design choices transfer to resource-constrained settings. These architectural explorations reflect ongoing efforts to improve both the quality and efficiency of NeRF representations through structural innovations rather than solely increased model capacity.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the necessity of moving beyond per-scene optimization toward generalizable models (Hung et al., 2025; Matta et al., 2024). There is broad agreement that NeRF must handle real-world data imperfections—whether motion blur, lens flare, or sparse views—through multi-view fusion and complementary sensor modalities (Qi et al., 2024; Matta et al., 2024; Huang et al., 2026). The surveyed literature also consistently emphasizes the importance of domain-specific adaptations, with medical imaging, remote sensing, and hyperspectral reconstruction each requiring tailored solutions that respect domain constraints (Wang et al., 2024; Castorena, 2024; Chen et al., 2024).

**Disagreements**: While Huang et al. (2026) report that their architectural extensions to accelerated NeRF variants did not conclusively outperform baselines, Ni et al. (2024) demonstrate that their Torch-NeRF architecture achieves excellent performance on large-scale scenes. This apparent tension may reflect differences in evaluation settings—Huang et al. focus on low-compute regimes with reduced view counts, while Ni et al. target complex scenes with full data availability. The field has not yet reached consensus on which architectural modifications provide reliable benefits under constrained conditions.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, uncertainty quantification remains underexplored beyond the recent work by Duan and Wong (2026); most NeRF papers do not provide confidence estimates, limiting deployment in safety-critical applications such as medical imaging and autonomous systems. Second, temporal scene modeling lacks dedicated datasets, as noted by Hung et al. (2025), hindering systematic progress in dynamic scene reconstruction. Third, domain-specific applications—particularly medical imaging—face challenges in standardizing evaluation metrics and datasets, with Wang et al. (2024) highlighting the absence of protocols that account for medical imaging's unique requirements. Fourth, several papers note reliance on specialized sensors (event cameras, hyperspectral cameras) that are not widely available, raising questions about accessibility and practical deployment (Qi et al., 2024; Chen et al., 2024). Finally, while generalizable NeRF approaches show promise, their performance under extreme few-shot conditions and across diverse scene types requires further validation.

## Per-Paper Annotations

### Castorena (2024)

**Research question**: Can neural radiance fields improve forest monitoring by expressing fine 3D structural features, fusing remote sensing modalities, and improving derived forest metrics?
**Methodology**: The work leverages neural radiance fields combined with remote sensing for forestry applications, presenting experiments that demonstrate NeRF's potential across multiple forest monitoring capabilities.
**Key findings**:
- NeRFs can express fine features of forest 3D structure that existing remote sensing methods cannot capture
- NeRFs enable fusion of multiple available remote sensing modalities
- NeRFs improve upon forest metrics derived from 3D structure
- Neural fields represent an attractive computational tool for advancing forest monitoring programs
- The approach offers potential for both scalability and accuracy improvements in forest monitoring
**Limitations**: The abstract presents potential and possibilities rather than conclusive quantitative results; specific performance metrics and comparative baselines against existing forestry monitoring methods are not detailed.

### Chen et al. (2024)

**Research question**: Can Neural Radiance Fields be extended to create 3D hyperspectral reconstructions that provide both spatial and spectral information for material and chemical composition analysis?
**Methodology**: The authors propose hyperspectral NeRF that computes wavelength-dependent radiance and transmittance spectra for every point in space and view direction, evaluated on a custom dataset of nearly 2000 hyperspectral images across 8 scenes and 2 cameras with comparisons against RGB NeRF baselines.
**Key findings**:
- Successfully creates fast, accurate volumetric 3D hyperspectral scenes with wavelength-dependent radiance and transmittance
- Mitigates common HSI challenges such as non-Lambertian surfaces and translucent objects through 3D reconstruction
- Outperforms traditional RGB NeRF baselines in hyperspectral reconstruction quality
- Enables new applications including hyperspectral super-resolution and imaging sensor simulation
- Collected comprehensive dataset with nearly 2000 hyperspectral images across 8 scenes and 2 cameras for evaluation
**Limitations**: Traditional 3D reconstruction with HSI remains difficult due to technological limitations of hyperspectral cameras, and the approach requires specialized hyperspectral imaging equipment that may not be widely available.

### Duan and Wong (2026)

**Research question**: How can we quantify both aleatoric and epistemic uncertainties in Neural Radiance Fields without compromising rendering quality or incurring significant computational overhead?
**Methodology**: The authors introduce Evidential Neural Radiance Fields, a probabilistic approach that seamlessly integrates with the NeRF rendering process, enabling direct quantification of both aleatoric and epistemic uncertainties from a single forward pass.
**Key findings**:
- Enables simultaneous quantification of both aleatoric and epistemic uncertainties in NeRFs
- Achieves uncertainty estimation from a single forward pass without significant computational overhead
- Maintains high rendering quality while providing uncertainty estimates
- Demonstrates state-of-the-art scene reconstruction fidelity on three standardized benchmarks
- Demonstrates state-of-the-art uncertainty estimation quality compared to existing methods
**Limitations**: The abstract does not explicitly acknowledge limitations; however, the approach requires validation in real-world safety-critical deployment scenarios beyond benchmark evaluations.

### Huang et al. (2026)

**Research question**: How can Neural Radiance Field variants be adapted and optimized for low-compute, low-data regimes while maintaining reconstruction quality?
**Methodology**: The authors conduct a comparative study of three accelerated NeRF variants (DS-NeRF, TensoRF, and HashNeRF) with novel extensions including depth-supervision loss for TensoRF, MLP ablation studies, and four architectural variants of HashNeRF networks evaluated under reduced view counts and matched iteration budgets.
**Key findings**:
- Added depth-supervision loss derived from COLMAP keypoints to TensoRF and evaluated on LLFF dataset under reduced view counts
- Ablation of TensoRF's feature-decoding MLP revealed effects of input downsampling on PSNR and runtime
- Four architectural variants of HashNeRF color and density networks (including residual and convolutional designs) were proposed and evaluated
- Under iso-time evaluation, none of the proposed extensions conclusively outperformed the published baselines
- Experiments characterized which extensions transfer to constrained settings and identified design questions for future work
**Limitations**: None of the proposed extensions conclusively outperform existing baselines under iso-time evaluation, suggesting limited practical advantage in their current form for low-cost regimes.

### Hung et al. (2025)

**Research question**: How can we build generalizable NeRFs that render novel views at arbitrary viewpoints and times from few-shot input views, particularly for natural day-night transitions?
**Methodology**: TimeNeRF harnesses multi-view stereo, neural radiance fields, and disentanglement strategies across diverse datasets to construct an implicit content radiance field for scene representation, enabling neural radiance field construction at any arbitrary time via volume rendering without per-scene optimization.
**Key findings**:
- TimeNeRF renders novel views in a few-shot setting without requiring per-scene optimization
- The approach creates realistic novel views that transition smoothly across different times of day
- The model captures intricate natural scene changes from dawn to dusk
- TimeNeRF achieves generalizability across diverse datasets
- The work addresses the lack of dedicated datasets for temporal 3D scene modeling in NeRF research
**Limitations**: The few-shot setting may have constraints on the quality and diversity of input views; the approach is particularly optimized for natural temporal transitions (day-night cycles) and may not generalize equally well to all types of temporal scene changes.

### Matta et al. (2024)

**Research question**: How can lens flare artifacts be effectively removed from images by leveraging multi-view information within a Neural Radiance Fields framework?
**Methodology**: The authors propose GN-FR, a framework within the Generalizable NeRF Transformer that incorporates Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules, using an unsupervised masking loss function to overcome the lack of paired flare-corrupted and flare-free training data.
**Key findings**:
- Successfully renders flare-free views from sparse sets of input images affected by lens flare
- Generalizes across different scenes in an unsupervised manner without requiring paired training data
- Leverages view-dependent nature of flare artifacts to recover details obscured in individual images
- Introduced first 3D multi-view flare dataset with 17 real scenes, 782 images, 80 real flare patterns, and annotated flare-occupancy masks
- First work to address flare removal within a Neural Radiance Fields framework
**Limitations**: Requires multi-view images which may not always be available in practical scenarios, and as the first work in this area, the approach has not been extensively validated across diverse flare conditions and camera systems.

### Ni et al. (2024)

**Research question**: How can Neural Radiance Fields be improved to handle complex and large-scale scene reconstruction with better contextual information capture?
**Methodology**: The authors propose Torch-NeRF, which enlarges the ray perception field by enabling single camera rays to render pixel patches simultaneously and replaces the standard MLP with distance-aware convolutions to enhance feature propagation among sample points on each ray.
**Key findings**:
- Novel inference pattern allows each camera ray to possess more contextual information by rendering patches instead of individual pixels
- Distance-aware convolutions enhance feature propagation among sample points from the same camera ray
- Effectively addresses large variance in backgrounds across different views in complex scenes
- Demonstrates excellent performance on KITTI-360 and LLFF benchmark datasets
- Successfully handles challenging large-scale scene reconstruction where previous methods struggle
**Limitations**: The patch-based rendering approach may increase computational requirements compared to standard ray-based inference, and performance on extremely large-scale outdoor scenes beyond KITTI-360 remains to be validated.

### Nguyen et al. (2024)

**Research question**: What is the current state, progression, and range of applications of semantically-aware Neural Radiance Fields in visual scene understanding?
**Methodology**: This comprehensive review analyzes over 250 scholarly papers on semantically-aware NeRFs, examining their capabilities in 3D representation inference for stationary and dynamic objects and their applications across various visual scene understanding tasks.
**Key findings**:
- NeRFs adeptly infer 3D representations for both stationary and dynamic objects in a scene
- Semantically-aware NeRFs enable high-quality novel viewpoint generation and scene inpainting
- The technology supports panoptic segmentation, 3D bounding box prediction, and 3D scene editing
- Semantic labels function as viewpoint-invariant functions mapping spatial coordinates to semantic label spectra
- Object-centric 3D models can be extracted from semantically-aware NeRF representations
**Limitations**: As a survey paper, it synthesizes existing work rather than proposing novel methods; the field is rapidly evolving with over 250 papers analyzed, suggesting some findings may become outdated as new techniques emerge.

### Qi et al. (2024)

**Research question**: How can we improve NeRF reconstruction quality in motion-blurred scenes by accurately estimating pose and lighting changes during exposure time?
**Methodology**: The authors propose EBAD-NeRF (Event-driven Bundle Adjustment for Deblurring Neural Radiance Fields) that jointly optimizes learnable poses and NeRF parameters by leveraging hybrid event-RGB data, introducing an intensity-change-metric event loss and a photo-metric blur loss for explicit motion blur modeling.
**Key findings**:
- Event cameras compensate for information deficiency in estimating pose and lighting changes during exposure time
- EBAD-NeRF obtains accurate camera trajectory estimates during exposure time
- The method learns sharper 3D representations compared to prior deblurring NeRF works
- The approach is validated on both synthetic and real-captured data
- Joint optimization of poses and NeRF parameters with event-RGB hybrid data effectively models motion blur
**Limitations**: The approach requires event camera data which may not be widely available in standard imaging setups; the method is specifically designed for motion blur scenarios and may not generalize to other image quality degradation types.

### Wang et al. (2024)

**Research question**: What are the unique challenges, current applications, and future research directions for applying Neural Radiance Fields to medical imaging?
**Methodology**: This comprehensive survey examines NeRF applications in medical imaging by analyzing fundamental challenges, reviewing current methods across different organs, evaluating datasets and metrics, and proposing promising future research directions.
**Key findings**:
- Identified four imminent challenges: fundamental imaging principles differences, inner structure requirements, object boundary definition, and color density significance in medical contexts
- Reviewed current NeRF methods applied to different organs and documented their specific limitations
- Surveyed available datasets and evaluation metrics specific to medical NeRF applications
- NeRF offers significant potential for synthesizing 3D representations from 2D medical image data
- Medical imaging presents unique constraints not addressed by standard computer vision NeRF approaches
**Limitations**: As a survey paper, it identifies challenges and limitations but does not provide novel solutions; the field is still emerging with limited standardized datasets and evaluation protocols for medical NeRF applications.

## References

Castorena, J. (2024). Learning neural radiance fields of forest structure for scalable and fine monitoring. arXiv. https://arxiv.org/abs/2401.15029

Chen, G., Narayanan, S. K., Ottou, T. G., Missaoui, B., Muriki, H., Pradalier, C., & Chen, Y. (2024). Hyperspectral neural radiance fields. arXiv. https://arxiv.org/abs/2403.14839

Duan, R., & Wong, A. (2026). Evidential neural radiance fields. arXiv. https://arxiv.org/abs/2602.23574

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-cost neural radiance fields. arXiv. https://arxiv.org/abs/2605.09312

Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building generalizable neural radiance fields across time from few-shot input views. arXiv. https://arxiv.org/abs/2507.13929

Matta, G. R., Siddartha, R., Girish, R. S. V., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable neural radiance fields for flare removal. arXiv. https://arxiv.org/abs/2412.08200

Ni, B., Wang, H., Bai, D., Weng, M., Qi, D., Qiu, W., & Liu, B. (2024). Neural radiance fields with Torch units. arXiv. https://arxiv.org/abs/2404.02617

Nguyen, T.-A.-Q., Bourki, A., Macudzinski, M., Brunel, A., & Bennamoun, M. (2024). Semantically-aware neural radiance fields for visual scene understanding: A comprehensive review. arXiv. https://arxiv.org/abs/2402.11141

Qi, Y., Zhu, L., Zhao, Y., Bao, N., & Li, J. (2024). Deblurring neural radiance fields with event-driven bundle adjustment. arXiv. https://arxiv.org/abs/2406.14360

Wang, X., Chen, Y., Hu, S., Fan, H., Zhu, H., & Li, X. (2024). Neural radiance fields in medical imaging: A survey. arXiv. https://arxiv.org/abs/2402.17797
