# Systematic Literature Review: Neural Radiance Fields

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "neural radiance fields", filtered to category cs.CV, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on Neural Radiance Fields (NeRF) from 2024-2026 reveals a field rapidly diversifying beyond novel view synthesis into specialized application domains and technical refinements. Research has shifted from foundational NeRF architectures toward addressing practical deployment challenges including uncertainty quantification, computational efficiency, motion artifacts, and domain-specific adaptations for forestry, medical imaging, and hyperspectral reconstruction. A strong emphasis on generalizability emerges across multiple works, with researchers developing methods that work from few-shot inputs, handle temporal variations, and transfer across scenes without per-scene optimization. The literature demonstrates NeRF's maturation from a research curiosity to a versatile 3D representation framework, though significant challenges remain in computational cost, data requirements, and deployment in safety-critical settings.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "neural radiance fields", filtered to category cs.CV, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Uncertainty Quantification and Trustworthy NeRF

A critical direction emerging in NeRF research addresses the fundamental lack of uncertainty estimation in standard NeRF models, which limits deployment in safety-critical applications. Duan and Wong (2026) directly tackle this challenge by introducing Evidential Neural Radiance Fields, which quantify both aleatoric (data) and epistemic (model) uncertainties in a single forward pass without compromising rendering quality. This work responds to a broader recognition in the field that accurate reconstructions alone are insufficient when downstream applications—such as autonomous navigation or medical diagnosis—require calibrated confidence estimates. The approach demonstrates that uncertainty quantification need not incur prohibitive computational overhead, addressing a key barrier to practical adoption.

### Theme 2: Generalizability and Few-Shot Learning

Multiple surveyed papers address the computational and data-collection burden of per-scene NeRF optimization by developing generalizable models that transfer across scenes and conditions. Hung et al. (2025) present TimeNeRF, which achieves few-shot generalization across both viewpoint and time, enabling novel view synthesis at arbitrary times of day without scene-specific retraining. Similarly, Matta et al. (2024) develop GN-FR for flare removal that generalizes across different scenes in an unsupervised manner. This theme reflects a maturing understanding that NeRF's practical utility depends on reducing the expensive per-scene optimization that characterized early approaches, moving toward models that can be deployed with sparse inputs and adapt to new conditions.

### Theme 3: Domain-Specific Applications

The literature demonstrates NeRF's expansion into specialized application domains, each presenting unique technical challenges. In forestry, Castorena (2024) applies NeRF to forest structure monitoring, leveraging the technology's ability to express fine 3D structural features and fuse multiple remote sensing modalities. In medical imaging, Wang et al. (2024) survey applications of NeRF to 3D reconstruction from 2D medical scans, identifying domain-specific challenges around internal structure requirements and object boundary definition. Chen et al. (2024) extend NeRF to hyperspectral imaging, enabling wavelength-dependent radiance and transmittance at every spatial point. These domain adaptations reveal that NeRF's core strength—continuous volumetric 3D representation—translates across diverse sensing modalities, though each domain introduces specialized constraints.

### Theme 4: Handling Real-World Imaging Artifacts

Several works address practical imaging challenges that degrade NeRF reconstruction quality in real-world capture conditions. Qi et al. (2024) tackle motion blur by integrating event camera data with NeRF through Event-driven Bundle Adjustment (EBAD-NeRF), jointly optimizing camera poses and NeRF parameters to recover sharp 3D representations from blurred inputs. Matta et al. (2024) address lens flare by framing flare removal as a multi-view problem within a NeRF framework, leveraging view-dependent flare artifacts to recover occluded details. These works recognize that NeRF's assumption of high-quality, static multi-view inputs is often violated in practice, and develop methods to either compensate for or explicitly model imaging artifacts.

### Theme 5: Computational Efficiency and Accessibility

Addressing NeRF's computational demands, recent work explores architectural modifications and training strategies for resource-constrained settings. Huang et al. (2026) conduct a systematic study of accelerated NeRF variants (DS-NeRF, TensoRF, HashNeRF) in low-compute, low-data regimes, testing extensions such as depth supervision and architectural modifications. Ni et al. (2024) propose Torch-NeRF, which replaces the standard MLP with distance-aware convolutions and renders pixel patches rather than individual rays to capture contextual information in large-scale scenes. While Huang et al. (2026) report that their extensions did not conclusively outperform baselines under iso-time evaluation, this line of work reflects important recognition that NeRF's computational requirements limit accessibility and practical deployment.

### Theme 6: Semantic Understanding and Scene Interpretation

Beyond geometric reconstruction, NeRF research increasingly integrates semantic understanding for higher-level scene interpretation. Nguyen et al. (2024) survey semantically-aware NeRFs, documenting how semantic labels function as viewpoint-invariant functions mapping spatial coordinates to object categories, enabling applications including panoptic segmentation, 3D bounding box prediction, and object-centric model extraction. This theme represents NeRF's evolution from purely geometric representation toward semantic scene understanding, bridging 3D reconstruction with computer vision tasks that require object-level reasoning.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the view that NeRF's practical deployment requires addressing computational efficiency, data efficiency, and robustness to real-world capture conditions. There is broad agreement that per-scene optimization is a significant barrier to deployment, motivating the emphasis on generalizable models (Hung et al., 2025; Matta et al., 2024). The surveyed literature also converges on the importance of uncertainty quantification for safety-critical applications (Duan & Wong, 2026), and on the value of domain-specific adaptations for specialized applications in forestry (Castorena, 2024), medical imaging (Wang et al., 2024), and hyperspectral reconstruction (Chen et al., 2024).

**Disagreements**: The literature shows less direct disagreement than complementary focus on different challenges. However, there is an implicit tension between works pursuing architectural modifications for efficiency (Ni et al., 2024; Huang et al., 2026) versus those pursuing generalization-based approaches (Hung et al., 2025; Matta et al., 2024) as the primary path to practical deployment. Huang et al. (2026) report that their architectural extensions did not conclusively outperform baselines, suggesting that efficiency gains may require more fundamental algorithmic changes rather than incremental modifications.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. First, computational efficiency remains unresolved: Huang et al. (2026) explicitly note that their proposed extensions did not outperform baselines under iso-time evaluation, indicating that low-compute NeRF remains an open challenge. Second, many papers acknowledge limitations around data requirements and capture conditions—Qi et al. (2024) require specialized event cameras, Chen et al. (2024) depend on hyperspectral imaging equipment, and Matta et al. (2024) collected a custom multi-view flare dataset—suggesting that NeRF methods often require specialized or expensive sensing beyond standard RGB cameras. Third, several survey and review papers (Nguyen et al., 2024; Wang et al., 2024) identify domain-specific challenges without proposing complete solutions, particularly in medical imaging where fundamental challenges around internal structure reconstruction and clinical validity remain significant barriers. Finally, while uncertainty quantification is recognized as critical (Duan & Wong, 2026), few works beyond this address calibrated confidence estimation, suggesting this remains an underexplored direction despite its importance for deployment.

## Per-Paper Annotations

### Castorena (2024)

**Research question**: How can Neural Radiance Fields combined with remote sensing improve the scalability and accuracy of forest monitoring programs?
**Methodology**: The work leverages NeRFs with remote sensing data to express fine features of forest 3D structure, fuse available remote sensing modalities, and improve upon 3D structure-derived forest metrics through experimental demonstration.
**Key findings**:
- NeRFs can express fine features of forest 3D structure that existing remote sensing methods cannot capture
- NeRFs enable fusion of multiple available remote sensing modalities
- NeRFs improve upon forest metrics derived from 3D structure compared to existing methods
- Neural fields demonstrate potential as a computational tool for advancing forest monitoring
- The approach offers both scalability and accuracy improvements for forestry applications
**Limitations**: The abstract does not explicitly state limitations, focusing instead on demonstrating potential; practical deployment challenges and computational requirements for large-scale forest monitoring are not addressed.

### Chen et al. (2024)

**Research question**: How can Neural Radiance Fields be extended to create 3D hyperspectral reconstructions that provide both spatial and spectral information?
**Methodology**: The authors propose hyperspectral NeRF that computes wavelength-dependent radiance and transmittance spectra for every point in space and view direction, evaluated on a custom dataset of nearly 2000 hyperspectral images across 8 scenes.
**Key findings**:
- Hyperspectral NeRF characterizes every point in space by wavelength-dependent radiance and transmittance spectra
- A dataset containing nearly 2000 hyperspectral images across 8 scenes and 2 cameras was collected for evaluation
- The approach enables fast, accurate volumetric 3D hyperspectral scene reconstruction
- Comparisons against traditional RGB NeRF baselines and ablation testing with alternative spectra representations were performed
- Demonstrated applications include hyperspectral super-resolution and imaging sensor simulation
**Limitations**: The abstract does not explicitly state limitations, though the approach depends on the availability of hyperspectral cameras and the technological limitations of hyperspectral imaging equipment mentioned in the background may constrain practical deployment.

### Duan and Wong (2026)

**Research question**: How can Neural Radiance Fields quantify both aleatoric and epistemic uncertainties without compromising rendering quality or incurring significant computational overhead?
**Methodology**: The authors introduce Evidential Neural Radiance Fields, a probabilistic approach that seamlessly integrates with the NeRF rendering process, enabling direct quantification of both aleatoric and epistemic uncertainties from a single forward pass.
**Key findings**:
- The approach successfully captures both aleatoric and epistemic uncertainties separately, unlike existing methods
- Achieves state-of-the-art scene reconstruction fidelity on three standardized benchmarks
- Delivers state-of-the-art uncertainty estimation quality
- Computational efficiency is maintained through single forward pass uncertainty quantification
- Rendering quality is not compromised despite uncertainty estimation integration
**Limitations**: The abstract does not explicitly acknowledge limitations, though the work addresses known issues where existing uncertainty quantification methods either compromise rendering quality or incur significant computational overhead.

### Huang et al. (2026)

**Research question**: How can Neural Radiance Fields be adapted to work effectively in low-compute, low-data regimes?
**Methodology**: The authors conduct a comparative study of three accelerated NeRF variants (DS-NeRF, TensoRF, HashNeRF) and propose extensions including depth-supervision loss for TensoRF, MLP ablation studies, and four architectural variants of HashNeRF's color and density networks.
**Key findings**:
- Added depth-supervision loss derived from COLMAP keypoints to TensoRF and evaluated on LLFF dataset under reduced view counts
- Ablation of TensoRF's feature-decoding MLP revealed effects of input downsampling on PSNR and runtime
- Four HashNeRF architectural variants (including residual and convolutional designs) were tested with PSNR/training-time tradeoffs
- Under iso-time evaluation, none of the proposed extensions conclusively outperformed published baselines
- Experiments characterized which extensions transfer to constrained settings and identified design questions for future work
**Limitations**: None of the proposed extensions conclusively outperformed the published baselines under iso-time evaluation, suggesting limited practical improvement in the low-compute regime.

### Hung et al. (2025)

**Research question**: How can Neural Radiance Fields be made generalizable across time from few-shot input views to enable temporal 3D scene modeling without per-scene optimization?
**Methodology**: TimeNeRF harnesses multi-view stereo, neural radiance fields, and disentanglement strategies across diverse datasets to construct an implicit content radiance field for scene representation, enabling neural radiance field building at arbitrary times with novel view synthesis via volume rendering.
**Key findings**:
- TimeNeRF renders novel views in few-shot settings without requiring per-scene optimization
- The approach creates realistic novel views that transition smoothly across different times of day
- TimeNeRF adeptly captures intricate natural scene changes from dawn to dusk
- The model achieves generalizability across time and viewpoints simultaneously
- The work addresses the previously unexplored potential of NeRFs for temporal 3D scene modeling and notes the absence of dedicated datasets for this purpose
**Limitations**: The abstract does not explicitly acknowledge limitations, though the approach depends on disentanglement strategies and the authors note that no dedicated datasets were previously available for temporal 3D scene modeling, suggesting data availability may be a constraint.

### Matta et al. (2024)

**Research question**: How can lens flare artifacts be removed from images by leveraging multi-view information rather than single-image approaches?
**Methodology**: The authors propose GN-FR, a framework within the Generalizable NeRF Transformer that incorporates Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules, using a masking loss function for unsupervised learning across different scenes.
**Key findings**:
- GN-FR can render flare-free views from sparse sets of flare-corrupted input images
- The framework generalizes across different scenes in an unsupervised manner
- Introduced a 3D multi-view flare dataset with 17 real flare scenes, 782 images, 80 real flare patterns, and annotated flare-occupancy masks
- The masking loss function overcomes the impracticality of capturing both flare-corrupted and flare-free ground truth data
- First work to address flare removal within a Neural Radiance Fields framework
**Limitations**: As the first work addressing flare removal in NeRF, the approach requires validation on broader datasets, and the unsupervised masking loss may have limitations in handling complex flare patterns without any ground truth supervision.

### Ni et al. (2024)

**Research question**: How can NeRF be improved to handle complex and large-scale scenes with high background variance?
**Methodology**: The authors propose Torch-NeRF, which enlarges the ray perception field by having each camera ray render a patch of pixels simultaneously and replaces the MLP with distance-aware convolutions to enhance feature propagation among sample points.
**Key findings**:
- Each camera ray renders a patch of pixels simultaneously rather than individual pixels, capturing more contextual information
- Distance-aware convolutions replace the traditional MLP to model relationships among sample points on each camera ray
- The approach builds up sample point interactions to improve feature propagation
- Extensive experiments on KITTI-360 and LLFF datasets demonstrate excellent performance
- The method effectively addresses large variance in backgrounds across different views in complex scenes
**Limitations**: The abstract does not explicitly acknowledge limitations, though the patch-based rendering approach may introduce computational overhead and the method's effectiveness on extremely large-scale scenes beyond KITTI-360 and LLFF remains unexplored.

### Nguyen et al. (2024)

**Research question**: What is the current state, progression, and range of applications of semantically-aware Neural Radiance Fields in visual scene understanding?
**Methodology**: This comprehensive review analyzes over 250 scholarly papers on semantically-aware NeRFs, exploring their capabilities in 3D representation inference for stationary and dynamic objects and their applications across multiple visual scene understanding tasks.
**Key findings**:
- NeRFs adeptly infer 3D representations for both stationary and dynamic objects in a scene
- Semantically-aware NeRFs enable high-quality novel viewpoint generation, scene inpainting, panoptic segmentation, 3D bounding box prediction, 3D scene editing, and object-centric 3D model extraction
- Semantic labels function as viewpoint-invariant functions that map spatial coordinates to semantic labels, facilitating distinct object recognition within scenes
- The survey documents significant progression in semantically-aware NeRF capabilities
- Diverse applications have emerged in visual scene interpretation contexts
**Limitations**: As a comprehensive review rather than original research, the paper synthesizes existing work rather than proposing new methods; specific gaps in the literature or challenges requiring future research are not detailed in the abstract.

### Qi et al. (2024)

**Research question**: How can motion blur in input images be addressed to improve NeRF reconstruction quality in low-light and high-speed motion scenes?
**Methodology**: The authors propose Event-driven Bundle Adjustment for Deblurring Neural Radiance Fields (EBAD-NeRF), which jointly optimizes learnable poses and NeRF parameters by leveraging hybrid event-RGB data, introducing an intensity-change-metric event loss and a photo-metric blur loss for explicit camera motion blur modeling.
**Key findings**:
- EBAD-NeRF obtains accurate camera trajectory estimates during exposure time, addressing a key deficiency in prior methods
- The approach learns sharper 3D representations compared to prior deblurring NeRF works
- Event cameras provide high temporal resolution intensity-change measurements that compensate for missing pose and lighting information during exposure
- The method is validated on both synthetic and real-captured data
- Joint optimization of poses and NeRF parameters enables accurate motion blur modeling
**Limitations**: The abstract does not explicitly acknowledge limitations, though the method requires event camera data which may not be available in all capture scenarios, potentially limiting practical applicability.

### Wang et al. (2024)

**Research question**: What are the unique challenges and current applications of Neural Radiance Fields when applied to medical imaging?
**Methodology**: This survey paper provides a comprehensive examination of NeRF applications in medical imaging, analyzing challenges across different organs, reviewing datasets and evaluation metrics, and proposing future research directions.
**Key findings**:
- NeRF faces four imminent challenges in medical imaging: fundamental imaging principles, inner structure requirement, object boundary definition, and color density significance
- Current NeRF methods have been applied to different organs with varying degrees of success and specific limitations
- The survey reviews available datasets and evaluation metrics specific to medical NeRF applications
- Medical imaging presents unique challenges compared to standard computer vision applications due to the need for internal structure reconstruction
- Several promising directions for future research are identified to address current limitations
**Limitations**: As a survey paper, it identifies limitations in current methods rather than proposing solutions; the unique requirements of medical imaging (internal structures, precise boundaries, clinical validity) remain significant barriers to NeRF adoption in this domain.

## References

Castorena, J. (2024). Learning neural radiance fields of forest structure for scalable and fine monitoring. arXiv. https://arxiv.org/abs/2401.15029

Chen, G., Narayanan, S. K., Ottou, T. G., Missaoui, B., Muriki, H., Pradalier, C., & Chen, Y. (2024). Hyperspectral neural radiance fields. arXiv. https://arxiv.org/abs/2403.14839

Duan, R., & Wong, A. (2026). Evidential neural radiance fields. arXiv. https://arxiv.org/abs/2602.23574

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-cost neural radiance fields. arXiv. https://arxiv.org/abs/2605.09312

Hung, H.-H., Do, H.-P., Li, Y., & Huang, C.-C. (2025). TimeNeRF: Building generalizable neural radiance fields across time from few-shot input views. arXiv. https://arxiv.org/abs/2507.13929

Matta, G. R., Siddartha, R., Venkata Girish, R. S., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable neural radiance fields for flare removal. arXiv. https://arxiv.org/abs/2412.08200

Ni, B., Wang, H., Bai, D., Weng, M., Qi, D., Qiu, W., & Liu, B. (2024). Neural radiance fields with Torch units. arXiv. https://arxiv.org/abs/2404.02617

Nguyen, T.-A.-Q., Bourki, A., Macudzinski, M., Brunel, A., & Bennamoun, M. (2024). Semantically-aware neural radiance fields for visual scene understanding: A comprehensive review. arXiv. https://arxiv.org/abs/2402.11141

Qi, Y., Zhu, L., Zhao, Y., Bao, N., & Li, J. (2024). Deblurring neural radiance fields with event-driven bundle adjustment. arXiv. https://arxiv.org/abs/2406.14360

Wang, X., Chen, Y., Hu, S., Fan, H., Zhu, H., & Li, X. (2024). Neural radiance fields in medical imaging: A survey. arXiv. https://arxiv.org/abs/2402.17797
