# Systematic Literature Review: Neural Radiance Fields

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "neural radiance fields", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on Neural Radiance Fields (NeRF) published within the last two years in the computer vision category. The surveyed literature reveals a field rapidly evolving beyond basic novel view synthesis toward specialized applications addressing real-world constraints. Key research directions include uncertainty quantification, temporal modeling, domain generalization, handling complex visual phenomena (reflections, flare, anisotropic surfaces), and practical deployment in constrained settings. The collective work demonstrates NeRF's maturation from a novel representation technique to a versatile framework adaptable to diverse challenges spanning satellite imagery, human avatars, and material digitization. Despite significant advances, common limitations persist around computational efficiency, data requirements, and the need for specialized handling of edge cases.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "neural radiance fields", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Uncertainty Quantification and Reliability

A critical emerging direction addresses the need for NeRFs to quantify their own uncertainty. Duan and Wong (2026) identify that existing uncertainty quantification methods fail to separately capture both aleatoric (data) and epistemic (model) uncertainties, often compromising rendering quality or incurring significant computational overhead. Their Evidential Neural Radiance Fields approach integrates probabilistic reasoning directly into the rendering process, enabling direct quantification of both uncertainty types from a single forward pass. This theme reflects a broader maturation of the field toward trustworthy, reliable deployments where understanding prediction confidence is as important as the prediction itself.

### Theme 2: Temporal and Dynamic Scene Modeling

Several papers address the challenge of modeling scenes that change over time. Hung et al. (2025) introduce TimeNeRF, which builds generalizable neural radiance fields across time from few-shot input views without per-scene optimization. Their approach harnesses multi-view stereo, NeRF, and disentanglement strategies to construct implicit content radiance fields, enabling novel view synthesis that transitions smoothly across different times and captures natural scene changes from dawn to dusk. This theme represents a significant advance beyond static scene reconstruction toward dynamic, temporally coherent representations.

### Theme 3: Domain Generalization and Transfer

A persistent challenge in NeRF research is enabling models to generalize across diverse scenes and conditions without retraining. Qazi et al. (2025) propose NeuGen, a brain-inspired normalization technique that extracts domain-invariant features and integrates seamlessly into existing NeRF architectures like MVSNeRF and GeoNeRF. Their approach markedly improves rendering quality in novel view synthesis and surpasses existing models in generalizability on benchmark evaluations. Similarly, Huang et al. (2026) investigate how accelerated NeRF variants (DS-NeRF, TensoRF, HashNeRF) can be extended to work effectively in low-compute, low-data regimes, presenting architectural variants and depth-supervision extensions to characterize tradeoffs under constrained settings.

### Theme 4: Handling Complex Visual Phenomena

Multiple papers tackle specific visual challenges that standard NeRF formulations struggle with. Gao et al. (2024) address planar reflections, which standard NeRF interprets as erroneous geometries, by introducing a reflection-aware NeRF that jointly models planar reflectors and explicitly casts reflected rays. Matta et al. (2024) tackle lens flare removal as a multi-view image problem, proposing GN-FR within the Generalizable NeRF Transformer framework that leverages the view-dependent nature of flare artifacts to recover obscured details. Barreiro et al. (2025) focus on anisotropic specular surfaces like brushed metals with ShinyNeRF, which jointly estimates surface normals, tangents, specular concentration, and anisotropy magnitudes. These works collectively demonstrate NeRF's adaptability to handle complex real-world visual phenomena.

### Theme 5: Specialized Application Domains

The surveyed literature shows NeRF being adapted to highly specialized application domains. Wagner et al. (2025) propose Semantic Neural Radiance Fields for multi-date satellite data, deriving 3D semantic neural fields from satellite images with pixel-wise semantic labels to address temporal inconsistencies caused by non-stationary categories such as vehicles. Gu et al. (2025) introduce MaintaAvatar, a maintainable avatar based on NeRF using continual learning to update human avatars with new appearances and poses while avoiding catastrophic forgetting of past states. These applications demonstrate NeRF's versatility beyond traditional novel view synthesis toward domain-specific solutions.

### Theme 6: Survey and Synthesis Work

Xiao et al. (2025) provide a comprehensive survey of NeRF for real-world applications, compiling key theoretical advancements and alternative scene representations, investigating emerging challenges, exploring applications in reconstruction, and reviewing essential datasets and toolkits. Their work identifies gaps in the literature and discusses open challenges with directions for future research, serving as a valuable synthesis of the field's progress and remaining obstacles.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the need for NeRFs to operate efficiently under constrained conditions. Both Huang et al. (2026) and Qazi et al. (2025) emphasize reducing computational requirements and improving generalization, suggesting broad agreement that accessibility and deployability are critical barriers. There is also convergence on the value of multi-view information: Matta et al. (2024), Wagner et al. (2025), and Gao et al. (2024) all leverage multiple views to overcome limitations of single-image approaches, whether for flare removal, semantic labeling, or reflection handling.

**Disagreements**: The surveyed papers do not exhibit fundamental disagreements about core NeRF principles, but rather differ in their methodological priorities. Some works prioritize rendering quality above all (Duan & Wong, 2026; Barreiro et al., 2025), while others emphasize generalization and transferability (Qazi et al., 2025; Hung et al., 2025). The tension between specialization and generalization remains unresolved: highly specialized methods like ShinyNeRF achieve state-of-the-art results on specific tasks but may not transfer to other domains.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Computational efficiency**: Huang et al. (2026) note that long training times and reliance on dense input views limit NeRF accessibility, yet none of the extensions they tested conclusively outperformed baselines under iso-time evaluation. This suggests fundamental architectural innovations may be needed.

2. **Dataset limitations**: Hung et al. (2025) explicitly note the lack of dedicated datasets for temporal 3D scene modeling, while Wagner et al. (2025) created a new dataset with manually generated labels for multi-view satellite images. The field would benefit from standardized benchmarks.

3. **Uncertainty quantification**: Duan and Wong (2026) identify that existing methods fail to capture both uncertainty types effectively, suggesting this remains an open challenge despite their proposed solution.

4. **Generalization under constraints**: The tension between domain-specific optimization and cross-domain generalization persists. Qazi et al. (2025) and Huang et al. (2026) propose complementary approaches, but a unified framework remains elusive.

5. **Real-world deployment**: Xiao et al. (2025) identify gaps between research advances and practical deployment, particularly in robotics and industrial applications where reliability and efficiency are paramount.

## Per-Paper Annotations

### Barreiro et al. (2025)

**Research question**: How can Neural Radiance Fields accurately model anisotropic specular surfaces like brushed metals?
**Methodology**: The authors introduce ShinyNeRF, which jointly estimates surface normals, tangents, specular concentration, and anisotropy magnitudes of an Anisotropic Spherical Gaussian distribution by learning an approximation of outgoing radiance as an encoded mixture of isotropic von Mises-Fisher distributions.
**Key findings**:
- ShinyNeRF handles both isotropic and anisotropic reflections effectively
- The method achieves state-of-the-art performance on digitizing anisotropic specular reflections
- The framework offers plausible physical interpretations of material properties
- The approach enables editing of material properties compared to existing methods
**Limitations**: not stated in abstract

### Duan and Wong (2026)

**Research question**: How can neural radiance fields quantify both aleatoric and epistemic uncertainties without compromising rendering quality or incurring significant computational overhead?
**Methodology**: The authors introduce Evidential Neural Radiance Fields, a probabilistic approach that integrates with the NeRF rendering process to enable direct quantification of both aleatoric and epistemic uncertainties from a single forward pass. They compare multiple uncertainty quantification methods on three standardized benchmarks.
**Key findings**:
- Existing uncertainty quantification methods for NeRFs fail to separately capture both aleatoric and epistemic uncertainties
- Many existing methods either compromise rendering quality or incur significant computational overhead
- The proposed approach demonstrates state-of-the-art scene reconstruction fidelity and uncertainty estimation quality
- The method enables direct quantification of both uncertainty types from a single forward pass
**Limitations**: not stated in abstract

### Gao et al. (2024)

**Research question**: How can Neural Radiance Fields be improved to accurately handle complex planar reflections?
**Methodology**: The authors introduce a reflection-aware NeRF that jointly models planar reflectors and explicitly casts reflected rays to capture high-frequency reflections, using sparse edge regularization to prevent duplicate scene representations.
**Key findings**:
- The method accurately handles planar reflections that standard NeRF interprets as erroneous geometries
- Rendering along the primary ray produces clean, reflection-free views
- Explicitly rendering along reflected rays reconstructs highly detailed reflections
- The approach obtains accurate scene geometry without duplicated representations
**Limitations**: not stated in abstract

### Gu et al. (2025)

**Research question**: How can NeRF-based human avatars be updated with new appearances and poses while maintaining rendering quality of past states?
**Methodology**: The authors propose MaintaAvatar, which uses a Global-Local Joint Storage Module and Pose Distillation Module with continual learning to update avatars while avoiding catastrophic forgetting of past appearances and poses.
**Key findings**:
- The model resolves color bleeding issues and incorrect human body poses that occur with standard continual learning approaches
- MaintaAvatar requires only limited data collection to quickly fine-tune the model
- The approach avoids catastrophic forgetting of past appearance rendering quality
- Experimental results validate the effectiveness of the maintainable virtual avatar model
**Limitations**: not stated in abstract

### Huang et al. (2026)

**Research question**: How can accelerated NeRF variants be extended to work effectively in low-compute, low-data regimes?
**Methodology**: The authors present a comparative study of three accelerated NeRF variants (DS-NeRF, TensoRF, and HashNeRF) with extensions for constrained settings. They add depth-supervision loss to TensoRF, ablate the feature-decoding MLP, and propose four architectural variants of HashNeRF color and density networks, reporting PSNR/training-time tradeoffs under matched iteration budgets.
**Key findings**:
- Long training times and reliance on dense input views limit NeRF accessibility
- Depth-supervision loss derived from COLMAP keypoints was added to TensoRF and evaluated on LLFF dataset under reduced view counts
- Under iso-time evaluation, none of the extensions conclusively outperform the published baselines
- The experiments characterize which extensions transfer to constrained settings and surface design questions for future work
**Limitations**: not stated in abstract

### Hung et al. (2025)

**Research question**: How can neural radiance fields render novel views at arbitrary viewpoints and times from few input views without per-scene optimization?
**Methodology**: The approach harnesses multi-view stereo, neural radiance fields, and disentanglement strategies across diverse datasets to construct an implicit content radiance field for scene representation and enable building neural radiance fields at any arbitrary time. Novel views are synthesized via volume rendering.
**Key findings**:
- TimeNeRF can render novel views in a few-shot setting without per-scene optimization
- The model excels in creating realistic novel views that transition smoothly across different times
- It adeptly captures intricate natural scene changes from dawn to dusk
- Current NeRF techniques have limited exploration for temporal 3D scene modeling with no dedicated datasets available
**Limitations**: not stated in abstract

### Matta et al. (2024)

**Research question**: How can flare removal be addressed as a multi-view image problem using neural radiance fields to overcome limitations of single-image approaches?
**Methodology**: The authors propose GN-FR, a framework within the Generalizable NeRF Transformer that incorporates Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules. They introduce a masking loss function for unsupervised settings and present a 3D multi-view flare dataset with 17 real flare scenes, 782 images, 80 flare patterns, and annotated flare-occupancy masks.
**Key findings**:
- Flare removal is highly ill-posed when relying on single-image approaches
- The multi-view approach leverages view-dependent nature of flare artifacts and information from neighboring views to recover obscured details
- GN-FR can render flare-free views from sparse input images affected by lens flare and generalizes across different scenes unsupervised
- This is the first work to address flare removal within a Neural Radiance Fields framework
- A new 3D multi-view flare dataset was created with 17 real flare scenes and 782 images
**Limitations**: not stated in abstract

### Qazi et al. (2025)

**Research question**: How can Neural Radiance Fields be improved to generalize better across diverse scenes and conditions?
**Methodology**: The authors propose NeuGen, a brain-inspired normalization technique that extracts domain-invariant features and can be seamlessly integrated into existing NeRF architectures like MVSNeRF and GeoNeRF to enhance generalization capabilities.
**Key findings**:
- NeuGen improves generalization capabilities of NeRF models across diverse scenes
- The technique surpasses existing models in generalizability on benchmark evaluations
- NeuGen markedly improves rendering quality in novel view synthesis
- The approach merges neuroscientific principles with deep learning frameworks for enhanced efficiency
**Limitations**: not stated in abstract

### Wagner et al. (2025)

**Research question**: How can Neural Radiance Fields be adapted to generate three-dimensional semantic representations from multi-date satellite images?
**Methodology**: The authors propose a satellite-specific NeRF model that derives 3D semantic neural fields from multi-date satellite images with pixel-wise semantic labels, enhancing color prediction by utilizing semantic information to address temporal inconsistencies.
**Key findings**:
- The approach demonstrates robustness in generating 3D semantic representations from multi-date satellite imagery
- The model improves noisy input labels through its neural semantic field approach
- Semantic information helps address temporal image inconsistencies caused by non-stationary categories such as vehicles
- A new dataset with manually generated labels for multi-view satellite images was created to facilitate research
**Limitations**: not stated in abstract

### Xiao et al. (2025)

**Research question**: What are the key theoretical advancements, applications, challenges, and future directions for Neural Radiance Fields in real-world settings?
**Methodology**: This survey compiles key theoretical advancements and alternative scene representations, investigates emerging challenges, explores applications in reconstruction, highlights NeRFs' impact on computer vision and robotics, and reviews essential datasets and toolkits through comprehensive literature review.
**Key findings**:
- NeRFs have remodeled 3D scene representation since release and can effectively reconstruct complex 3D scenes from 2D images
- NeRFs advance different fields including scene understanding, 3D content generation, and robotics
- Despite significant research progress, a thorough review of recent innovations, applications, and challenges was lacking
- The survey identifies gaps in the literature and discusses open challenges with directions for future research
**Limitations**: not stated in abstract

## References

Barreiro, A., Marí, R., Redondo, R., Haro, G., & Bosch, C. (2025). ShinyNeRF: Digitizing anisotropic appearance in neural radiance fields. arXiv. https://arxiv.org/abs/2512.21692

Duan, R., & Wong, A. (2026). Evidential neural radiance fields. arXiv. https://arxiv.org/abs/2602.23574

Gao, C., Wang, Y., Kim, C., Huang, J.-B., & Kopf, J. (2024). Planar reflection-aware neural radiance fields. arXiv. https://arxiv.org/abs/2411.04984

Gu, S., Qiu, Y.-K., Tang, Y.-M., Wu, A., & Zheng, W.-S. (2025). MaintaAvatar: A maintainable avatar based on neural radiance fields by continual learning. arXiv. https://arxiv.org/abs/2502.02372

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-cost neural radiance fields. arXiv. https://arxiv.org/abs/2605.09312

Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building generalizable neural radiance fields across time from few-shot input views. arXiv. https://arxiv.org/abs/2507.13929

Matta, G. R., Siddartha, R., Venkata Girish, R. S., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable neural radiance fields for flare removal. arXiv. https://arxiv.org/abs/2412.08200

Qazi, A., Basit, A., & Iqbal, A. (2025). NeuGen: Amplifying the 'neural' in neural radiance fields for domain generalization. arXiv. https://arxiv.org/abs/2505.06894

Wagner, V., Bullinger, S., Bodensteiner, C., & Arens, M. (2025). Semantic neural radiance fields for multi-date satellite data. arXiv. https://arxiv.org/abs/2502.16992

Xiao, W., Chierchia, R., Santa Cruz, R., Li, X., Ahmedt-Aristizabal, D., Salvado, O., Fookes, C., & Lebrat, L. (2025). Neural radiance fields for the real world: A survey. arXiv. https://arxiv.org/abs/2501.13104
