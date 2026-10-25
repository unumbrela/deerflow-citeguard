# Systematic Literature Review: Neural Radiance Fields

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "neural radiance fields", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Neural Radiance Fields (NeRF) have emerged as a transformative approach for 3D scene representation and novel view synthesis, with recent research focusing on addressing practical limitations and expanding applicability to real-world scenarios. The ten papers surveyed in this review collectively demonstrate significant progress in uncertainty quantification, temporal generalization, computational efficiency, artifact removal, and domain-specific adaptations. Key advances include methods for capturing both aleatoric and epistemic uncertainties in single forward passes, generalizable NeRFs that operate without per-scene optimization, and specialized frameworks for handling reflections, lens flares, and anisotropic materials. The field is increasingly moving toward practical deployment in resource-constrained environments and domain-specific applications such as satellite imagery, avatar creation, and material digitization.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "neural radiance fields", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Uncertainty Quantification and Reliability

A critical challenge in NeRF deployment is understanding and quantifying the reliability of reconstructions. Duan & Wong (2026) address this by introducing Evidential Neural Radiance Fields, which separately capture both aleatoric (data) and epistemic (model) uncertainties without compromising rendering quality or incurring significant computational overhead. This probabilistic approach integrates seamlessly with the NeRF rendering process, enabling direct quantification of both uncertainty types from a single forward pass. The method demonstrates state-of-the-art performance on both scene reconstruction fidelity and uncertainty estimation quality across three standardized benchmarks, representing a significant advance in making NeRF outputs more interpretable and trustworthy for safety-critical applications.

### Theme 2: Temporal and Cross-Time Generalization

Several papers address the challenge of modeling scenes across time, enabling NeRFs to capture dynamic changes and temporal variations. Hung et al. (2025) present TimeNeRF, which builds generalizable neural radiance fields across time from few-shot input views without requiring per-scene optimization. By combining multi-view stereo, neural radiance fields, and disentanglement strategies, the approach creates implicit content radiance fields that can render novel views at arbitrary viewpoints and times. The model excels at capturing intricate natural scene changes from dawn to dusk, producing realistic transitions that smoothly interpolate across different temporal states. This represents a significant step toward practical deployment of NeRFs in scenarios where scenes evolve over time.

### Theme 3: Computational Efficiency and Low-Resource Deployment

Making NeRFs accessible in resource-constrained environments remains an active research challenge. Huang et al. (2026) conduct a comprehensive comparative study of accelerated NeRF variants (DS-NeRF, TensoRF, and HashNeRF) with architectural extensions designed for low-compute, low-data regimes. Their work explores depth-supervision loss for TensoRF derived from COLMAP keypoints, ablation of feature-decoding MLPs, and four architectural variants of HashNeRF networks including residual and convolutional designs. While the experiments characterize which extensions transfer to constrained settings, none conclusively outperform published baselines under iso-time evaluation, highlighting the ongoing challenge of balancing computational efficiency with reconstruction quality.

### Theme 4: Artifact Removal and Quality Enhancement

Multiple papers focus on addressing specific artifacts that degrade NeRF rendering quality in real-world scenarios. Matta et al. (2024) propose GN-FR, the first framework to address lens flare removal within a NeRF framework by treating it as a multi-view image problem. Their approach leverages the view-dependent nature of flare artifacts and information from neighboring views through Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules within the Generalizable NeRF Transformer framework. The method introduces a masking loss function for unsupervised settings and is validated on a new 3D multi-view flare dataset with 17 real scenes and 782 images. Gao et al. (2024) tackle planar reflections, which cause erroneous scene geometries in standard NeRFs. Their reflection-aware NeRF jointly models planar reflectors and explicitly casts reflected rays to capture high-frequency reflections, using sparse edge regularization to prevent duplicate scene representations. The approach produces both clean, reflection-free views and highly detailed reflections, demonstrating enhanced performance on real-world datasets.

### Theme 5: Domain-Specific Adaptations

Recent work increasingly tailors NeRFs to specific application domains with unique requirements. Wagner et al. (2025) adapt NeRFs for multi-date satellite data, deriving 3D semantic representations from satellite images with pixel-wise semantic labels. Their satellite-specific model enhances color prediction by using semantic information to address temporal inconsistencies caused by non-stationary categories like vehicles, demonstrating robustness in generating 3D semantic neural fields from satellite data. Gu et al. (2025) present MaintaAvatar, which enables continual learning for NeRF-based avatars without catastrophic forgetting. The model utilizes a Global-Local Joint Storage Module and Pose Distillation Module to update avatars with new appearances and poses while maintaining the ability to render past appearances, requiring only limited data collection for fine-tuning. Barreiro et al. (2025) introduce ShinyNeRF for digitizing anisotropic specular surfaces such as brushed metals, jointly estimating surface normals, tangents, specular concentration, and anisotropy magnitudes through an encoded mixture of isotropic von Mises-Fisher distributions.

### Theme 6: Domain Generalization and Neural Architectures

Improving NeRF generalization across diverse scenes and conditions is a fundamental research direction. Qazi et al. (2025) integrate a brain-inspired normalization technique called Neural Generalization (NeuGen) into leading NeRF architectures (MVSNeRF and GeoNeRF) to extract domain-invariant features. This approach cultivates a comprehensive feature set that improves accuracy and robustness in image rendering, surpassing existing models in generalizability and rendering quality across diverse datasets. The work demonstrates the potential of merging neuroscientific principles with deep learning frameworks to enhance NeRF performance. Xiao et al. (2025) provide a comprehensive survey of NeRF advancements for real-world applications, compiling key theoretical developments, alternative scene representations, emerging challenges, and future directions. Their review highlights NeRFs' impact on computer vision and robotics, identifying gaps in the literature and offering directions for future research.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that generalizability without per-scene optimization is essential for practical NeRF deployment. Multiple works (Hung et al., 2025; Matta et al., 2024; Qazi et al., 2025) emphasize the importance of leveraging multi-view information and view-dependent features to improve reconstruction quality. There is also consensus that domain-specific adaptations are necessary for real-world applications, as evidenced by specialized approaches for satellite imagery (Wagner et al., 2025), avatars (Gu et al., 2025), and material digitization (Barreiro et al., 2025).

**Disagreements**: The literature shows divergence in approaches to computational efficiency. While Huang et al. (2026) find that architectural extensions to accelerated NeRF variants do not conclusively outperform baselines under constrained settings, other works (Qazi et al., 2025) demonstrate significant improvements through neural architecture modifications. This suggests that the effectiveness of efficiency-focused interventions may be highly dependent on the specific architectural choices and evaluation metrics employed.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, most papers do not explicitly state limitations in their abstracts, suggesting a need for more transparent discussion of methodological constraints and failure modes. Second, while several papers address computational efficiency, none provide conclusive evidence of superior performance in low-resource settings, indicating that the challenge of making NeRFs truly accessible remains unresolved. Third, the survey reveals limited attention to evaluation standards and benchmarks that would enable fair comparison across different NeRF variants and applications. Finally, while domain-specific adaptations are emerging, there is limited work on unified frameworks that could generalize across multiple domains while maintaining specialization benefits.

## Per-Paper Annotations

### Barreiro et al. (2025)

**Research question**: How can Neural Radiance Fields be improved to accurately model anisotropic specular surfaces such as brushed metals?
**Methodology**: The authors introduce ShinyNeRF, which jointly estimates surface normals, tangents, specular concentration, and anisotropy magnitudes by learning an approximation of outgoing radiance as an encoded mixture of isotropic von Mises-Fisher distributions.
**Key findings**:
- ShinyNeRF handles both isotropic and anisotropic reflections
- The method achieves state-of-the-art performance on digitizing anisotropic specular reflections
- The approach offers plausible physical interpretations of material properties
- The framework enables editing of material properties compared to existing methods
**Limitations**: not stated in abstract

### Duan & Wong (2026)

**Research question**: How can neural radiance fields separately capture both aleatoric and epistemic uncertainties without compromising rendering quality or incurring significant computational overhead?
**Methodology**: The authors introduce Evidential Neural Radiance Fields, a probabilistic approach that integrates with the NeRF rendering process to enable direct quantification of both aleatoric and epistemic uncertainties from a single forward pass. They compare multiple uncertainty quantification methods on three standardized benchmarks.
**Key findings**:
- Evidential Neural Radiance Fields seamlessly integrate with the NeRF rendering process
- The approach enables direct quantification of both aleatoric and epistemic uncertainties from a single forward pass
- The approach demonstrates state-of-the-art scene reconstruction fidelity on standardized benchmarks
- The approach demonstrates state-of-the-art uncertainty estimation quality on standardized benchmarks
**Limitations**: not stated in abstract

### Gao et al. (2024)

**Research question**: How can Neural Radiance Fields be enhanced to accurately handle complex planar reflections that cause erroneous scene geometries?
**Methodology**: The authors introduce a reflection-aware NeRF that jointly models planar reflectors and explicitly casts reflected rays to capture high-frequency reflections, using sparse edge regularization to prevent duplicate scene representations.
**Key findings**:
- The method obtains accurate scene geometry by addressing planar reflection challenges
- Rendering along the primary ray produces clean, reflection-free views
- Explicitly rendering along reflected rays enables reconstruction of highly detailed reflections
- Quantitative and qualitative evaluations on real-world datasets demonstrate enhanced performance
**Limitations**: not stated in abstract

### Gu et al. (2025)

**Research question**: How can NeRF-based avatars be updated with new appearances and poses while maintaining the ability to render past appearances without catastrophic forgetting?
**Methodology**: The authors propose MaintaAvatar, which utilizes a Global-Local Joint Storage Module and a Pose Distillation Module to enable continual learning while avoiding catastrophic forgetting and color bleeding issues.
**Key findings**:
- The model resolves catastrophic forgetting issues when learning new appearances and poses
- The approach avoids color bleeding issues and incorrect human body poses
- Only limited data collection is required to quickly fine-tune the model
- Experimental results validate the effectiveness of the MaintaAvatar model for maintainable virtual avatars
**Limitations**: not stated in abstract

### Huang et al. (2026)

**Research question**: Which accelerated NeRF variants and architectural extensions perform effectively in low-compute, low-data regimes?
**Methodology**: The authors present a comparative study of three accelerated NeRF variants (DS-NeRF, TensoRF, and HashNeRF) with extensions for the low-compute regime, including depth-supervision loss for TensoRF, ablation of feature-decoding MLP, and four architectural variants of HashNeRF networks. Experiments evaluate PSNR and training-time tradeoffs under reduced view counts and matched iteration budgets.
**Key findings**:
- Depth-supervision loss derived from COLMAP keypoints was added to TensoRF and evaluated on LLFF dataset under reduced view counts
- Ablation of TensoRF's feature-decoding MLP and input downsampling effects were studied on the synthetic Lego scene
- Four architectural variants of HashNeRF color and density networks were proposed, including residual and convolutional designs
- Under iso-time evaluation, none of the extensions conclusively outperform the published baselines
**Limitations**: The experiments characterize which extensions transfer to constrained settings but do not provide conclusive improvements over baselines.

### Hung et al. (2025)

**Research question**: How can neural radiance fields be made generalizable for rendering novel views at arbitrary viewpoints and times from few input views without per-scene optimization?
**Methodology**: The approach combines multi-view stereo, neural radiance fields, and disentanglement strategies across diverse datasets to construct an implicit content radiance field that enables building neural radiance fields at any arbitrary time. Novel views are synthesized via volume rendering in a few-shot setting.
**Key findings**:
- TimeNeRF can render novel views in a few-shot setting without per-scene optimization
- The model excels in creating realistic novel views that transition smoothly across different times
- The approach adeptly captures intricate natural scene changes from dawn to dusk
- The model achieves generalizability by leveraging strengths of multi-view stereo and disentanglement strategies
**Limitations**: not stated in abstract

### Matta et al. (2024)

**Research question**: How can flare removal be addressed as a multi-view image problem using generalizable neural radiance fields to leverage view-dependent flare artifact information?
**Methodology**: The authors propose GN-FR, a framework incorporating Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules within the Generalizable NeRF Transformer framework. They introduce a masking loss function for unsupervised settings and present a 3D multi-view flare dataset with 17 real scenes, 782 images, and annotated flare-occupancy masks.
**Key findings**:
- GN-FR can render flare-free views from sparse input images affected by lens flare
- The framework generalizes across different scenes in an unsupervised manner
- The approach leverages view-dependent nature of flare artifacts and information from neighboring views
- A new 3D multi-view flare dataset was created with 17 real scenes and 782 images
- This is the first work to address flare removal within a Neural Radiance Fields framework
**Limitations**: not stated in abstract

### Qazi et al. (2025)

**Research question**: How can Neural Radiance Fields be improved to achieve better generalization across diverse scenes and conditions?
**Methodology**: The authors integrate a brain-inspired normalization technique called Neural Generalization (NeuGen) into leading NeRF architectures (MVSNeRF and GeoNeRF) to extract domain-invariant features and enhance generalization capabilities.
**Key findings**:
- NeuGen can be seamlessly integrated into existing NeRF architectures
- The approach cultivates a comprehensive feature set that improves accuracy and robustness in image rendering
- Quantitative and qualitative evaluations show improved performance on benchmarks across diverse datasets
- The method surpasses existing models in generalizability and improves rendering quality
- The work demonstrates the potential of merging neuroscientific principles with deep learning frameworks
**Limitations**: not stated in abstract

### Wagner et al. (2025)

**Research question**: How can Neural Radiance Fields be adapted to generate three-dimensional semantic representations from multi-date satellite images?
**Methodology**: The authors propose a satellite-specific NeRF model that derives 3D semantic representations from multi-date satellite images with pixel-wise semantic labels, enhancing color prediction by using semantic information to address temporal inconsistencies.
**Key findings**:
- The approach demonstrates robustness in generating 3D semantic neural fields from satellite data
- The method can improve noisy input semantic labels
- Semantic information helps address temporal image inconsistencies caused by non-stationary categories like vehicles
- A new dataset with manually generated labels for multi-view satellite images was created and made available
**Limitations**: not stated in abstract

### Xiao et al. (2025)

**Research question**: What are the key theoretical advancements, applications, challenges, and future directions for Neural Radiance Fields in real-world scenarios?
**Methodology**: This survey compiles key theoretical advancements and alternative scene representations, investigates emerging challenges, explores applications in reconstruction, highlights NeRFs' impact on computer vision and robotics, and reviews essential datasets and toolkits through literature analysis.
**Key findings**:
- NeRFs have remodeled 3D scene representation and can effectively reconstruct complex 3D scenes from 2D images
- NeRFs have advanced applications in scene understanding, 3D content generation, and robotics
- A thorough review of recent innovations, applications, and challenges was previously lacking
- The survey identifies gaps in the literature and discusses open challenges
- The survey offers directions for future research in NeRF applications
**Limitations**: not stated in abstract

## References

Barreiro, A., Marí, R., Redondo, R., Haro, G., & Bosch, C. (2025). ShinyNeRF: Digitizing anisotropic appearance in Neural Radiance Fields. arXiv. https://arxiv.org/abs/2512.21692

Duan, R., & Wong, A. (2026). Evidential Neural Radiance Fields. arXiv. https://arxiv.org/abs/2602.23574

Gao, C., Wang, Y., Kim, C., Huang, J.-B., & Kopf, J. (2024). Planar Reflection-Aware Neural Radiance Fields. arXiv. https://arxiv.org/abs/2411.04984

Gu, S., Qiu, Y.-K., Tang, Y.-M., Wu, A., & Zheng, W.-S. (2025). MaintaAvatar: A Maintainable Avatar Based on Neural Radiance Fields by Continual Learning. arXiv. https://arxiv.org/abs/2502.02372

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-Cost Neural Radiance Fields. arXiv. https://arxiv.org/abs/2605.09312

Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building Generalizable Neural Radiance Fields across Time from Few-Shot Input Views. arXiv. https://arxiv.org/abs/2507.13929

Matta, G. R., Siddartha, R., Venkata Girish, R. S., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable Neural Radiance Fields for Flare Removal. arXiv. https://arxiv.org/abs/2412.08200

Qazi, A., Basit, A., & Iqbal, A. (2025). NeuGen: Amplifying the 'Neural' in Neural Radiance Fields for Domain Generalization. arXiv. https://arxiv.org/abs/2505.06894

Wagner, V., Bullinger, S., Bodensteiner, C., & Arens, M. (2025). Semantic Neural Radiance Fields for Multi-Date Satellite Data. arXiv. https://arxiv.org/abs/2502.16992

Xiao, W., Chierchia, R., Santa Cruz, R., Li, X., Ahmedt-Aristizabal, D., Salvado, O., Fookes, C., & Lebrat, L. (2025). Neural Radiance Fields for the Real World: A Survey. arXiv. https://arxiv.org/abs/2501.13104
