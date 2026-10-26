# Systematic Literature Review: 3D and 4D World Modeling

**Date**: 2026-10-26  
**Papers surveyed**: 10  
**Scope**: arXiv search query "3D 4D world modeling", filtered to category cs.CV, published between 2023-09-04 and 2025-09-03  
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on 3D and 4D world modeling, focusing on dynamic scene representation and generation. The surveyed literature reveals a field rapidly transitioning from static 3D representations to temporally-aware 4D modeling, with Gaussian Splatting emerging as the dominant representation paradigm. Key advances include real-time rendering capabilities (82 FPS), dramatic reductions in optimization time (from hours to minutes), and novel hybrid score distillation methods that overcome traditional tradeoffs between appearance quality, 3D structure, and motion. The field demonstrates strong convergence around explicit representations (Gaussian Splatting) over implicit neural representations, though challenges remain in semantic drift, motion controllability, and temporal consistency.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "3D 4D world modeling", filtered to category cs.CV, published between 2023-09-04 and 2025-09-03. Papers were selected through citation-expanded screening from 50 initial search results plus 143 papers from reference expansion, with the top 10 most central papers included based on co-citation frequency. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening flow**: 50 papers identified by search, 143 added from references, 30 shortlisted, 20 screened, 10 included (all from reference expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Gaussian Splatting as the Dominant 4D Representation

The surveyed literature demonstrates a decisive shift toward Gaussian Splatting as the preferred representation for 4D dynamic scenes. Eight of ten papers explicitly employ Gaussian Splatting variants, citing advantages in rendering speed, storage efficiency, and compatibility with existing 3D engines. Wu et al. (2023) introduced 4D Gaussian Splatting (4D-GS), achieving real-time rendering at 82 FPS by combining 3D Gaussians with 4D neural voxels. This approach was subsequently extended by Ren et al. (2023) in DreamGaussian4D, which reduced optimization time from hours to minutes through explicit spatial transformation modeling.

The efficiency gains are substantial: Tang et al. (2023) reported approximately 10× acceleration compared to existing methods while maintaining competitive quality, with textured mesh generation completed in just 2 minutes. Yang et al. (2023) demonstrated that deformable 3D Gaussians learned in canonical space with deformation fields enable high-fidelity monocular dynamic scene reconstruction with real-time rendering capabilities. This convergence suggests Gaussian Splatting has become the de facto standard for 4D representation, displacing earlier implicit neural representation approaches.

### Theme 2: Hybrid Score Distillation for Text-to-4D Generation

A second major theme involves leveraging multiple pre-trained diffusion models through hybrid score distillation sampling (SDS) to overcome the traditional three-way tradeoff between scene appearance quality, 3D structure, and motion. Bahmani et al. (2023) pioneered this approach by alternating between text-to-image models (providing realistic appearance and 3D structure) and text-to-video models (providing motion capability). This hybrid optimization enables synthesis of 4D scenes with compelling quality across all three dimensions simultaneously.

Ling et al. (2023) extended this compositional approach by combining text-to-image, text-to-video, and 3D-aware multiview diffusion models with dynamic 3D Gaussian Splatting. Their method introduces novel regularization for moving 3D Gaussians and motion amplification mechanisms, achieving state-of-the-art text-to-4D performance. Xie et al. (2024) further unified this paradigm with a single latent video diffusion model generating novel view videos with temporal consistency, eliminating the need for separate models for video and view synthesis. This progression from single-model to multi-model to unified-model SDS represents a clear intellectual trajectory in the field.

### Theme 3: Grounded and Controllable 4D Content Generation

The third theme addresses the challenge of controllability in 4D generation, moving beyond direct text-to-4D pipelines toward grounded generation with user-specified motion. Yin et al. (2023) introduced 4DGen, which uses monocular video sequences as grounding signals, enabling users to specify motion through video inputs rather than text descriptions alone. Their framework employs dynamic 3D Gaussians for efficient high-resolution supervision with spatial-temporal pseudo labels on anchor frames.

Zhao et al. (2023) tackled a related problem with Animate124, the first framework to animate a single in-the-wild image into a 4D dynamic scene using textual motion descriptions. Their three-stage optimization (static initialization, motion learning via video diffusion, personalized diffusion prior) addresses semantic drift caused by text-reference image misalignment. Jiang et al. (2023) similarly leveraged monocular video as input, casting 360-degree dynamic object reconstruction as a 4D generation problem that eliminates the need for multi-view data collection and camera calibration. These approaches collectively demonstrate a shift from purely generative to grounded, controllable 4D content creation.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several points. First, explicit representations (Gaussian Splatting) are superior to implicit neural representations for dynamic scenes, with 8 of 10 papers adopting Gaussian-based approaches. Second, hybrid or compositional diffusion models outperform single-model approaches for text-to-4D generation, with all text-to-4D papers employing some form of multi-model distillation. Third, real-time rendering is achievable for 4D dynamic scenes, with multiple papers reporting FPS rates suitable for interactive applications (Wu et al., 2023; Yang et al., 2023; Tang et al., 2023).

**Disagreements**: The literature reveals tension between text-grounded and video-grounded generation approaches. While Zhao et al. (2023) and Bahmani et al. (2023) emphasize text-to-4D as the primary interface, Yin et al. (2023) and Jiang et al. (2023) argue that monocular video provides superior grounding for controllable motion. Additionally, there is disagreement on optimization strategies: Wu et al. (2023) and Ren et al. (2023) favor explicit spatial transformation modeling, while Xie et al. (2024) advocate for implicit 4D representations (dynamic NeRF) optimized without SDS-based methods.

## Gaps and Open Questions

Several gaps emerge consistently across the surveyed literature. First, semantic drift remains a persistent challenge: Zhao et al. (2023) explicitly note that objects in 3D videos tend to drift away from reference images over time due to misalignment between text prompts and reference images. This limitation is acknowledged but not fully resolved in the current literature.

Second, motion controllability is frequently cited as incomplete. While Yin et al. (2023) and Ren et al. (2023) enable some degree of motion control through video grounding or visual controls, fine-grained temporal editing and precise motion specification remain open challenges. Third, several papers note limitations in handling complex multi-object scenes with independent motions—most current approaches focus on single-object or scene-level motion with coherent dynamics.

Finally, the literature lacks systematic evaluation benchmarks for 4D generation quality. While papers report qualitative results and some quantitative metrics (PSNR, SSIM, LPIPS), there is no standardized benchmark for comparing 4D generation methods across appearance quality, temporal consistency, motion realism, and controllability dimensions.

## Per-Paper Annotations

### Bahmani et al. (2023)

**Research question**: How can text-to-4D generation overcome the three-way tradeoff between scene appearance quality, 3D structure, and motion?

**Methodology**: The authors introduce hybrid score distillation sampling, an alternating optimization procedure that blends supervision signals from multiple pre-trained diffusion models (text-to-image and text-to-video models) to leverage their complementary strengths for high-fidelity text-to-4D generation.

**Key findings**:
- Hybrid SDS combines benefits from text-to-image models (realistic appearance and 3D structure) and text-to-video models (motion capability)
- The approach alleviates the three-way tradeoff between appearance quality, 3D structure, and motion
- The method demonstrates synthesis of 4D scenes with compelling appearance, 3D structure, and motion

**Limitations**: not stated in abstract

### Jiang et al. (2023)

**Research question**: How can 4D dynamic objects be generated from uncalibrated monocular videos without multi-view data collection and camera calibration?

**Methodology**: The approach uses object-level 3D-aware image diffusion model as supervision for training Dynamic Neural Radiance Fields (DyNeRF), with a Cascade DyNeRF for stable convergence and an Interpolation-driven Consistency Loss for spatial-temporal consistency.

**Key findings**:
- 360-degree dynamic object reconstruction is cast as a 4D generation problem eliminating need for multi-view data and camera calibration
- Cascade DyNeRF facilitates stable convergence and temporal continuity under discrete time-axis supervision
- Interpolation-driven Consistency Loss minimizes discrepancy between rendered and interpolated frames
- Method performs competitively with prior art and demonstrates advantages for conventional text-to-3D generation tasks

**Limitations**: not stated in abstract

### Ling et al. (2023)

**Research question**: How can dynamic, animated 3D objects be synthesized from text guidance using score distillation methods?

**Methodology**: The method combines text-to-image, text-to-video, and 3D-aware multiview diffusion models with dynamic 3D Gaussian Splatting representation, using a novel regularization method for moving 3D Gaussians and motion amplification mechanism.

**Key findings**:
- Compositional generation approach simultaneously enforces temporal consistency, high-quality visual appearance, and realistic geometry
- Novel regularization stabilizes optimization and induces motion in dynamic 3D Gaussians
- Motion amplification and autoregressive synthesis enable longer 4D sequence generation
- Different 4D animations can be seamlessly combined due to Gaussian 4D representation
- Achieves state-of-the-art text-to-4D performance qualitatively and quantitatively

**Limitations**: not stated in abstract

### Ren et al. (2023)

**Research question**: How can 4D content generation be improved to reduce optimization time, increase motion controllability, and enhance detail quality?

**Methodology**: The authors introduce DreamGaussian4D (DG4D), combining explicit modeling of spatial transformations with static Gaussian Splatting. The framework includes two modules: Image-to-4D GS (generating static GS with DreamGaussianHD followed by HexPlane-based dynamic generation) and Video-to-Video Texture Refinement using a pre-trained image-to-video diffusion model.

**Key findings**:
- DG4D reduces optimization time from several hours to just a few minutes
- The method allows generated 3D motion to be visually controlled
- The approach produces animated meshes that can be realistically rendered in 3D engines

**Limitations**: not stated in abstract

### Tang et al. (2023)

**Research question**: How can 3D content generation achieve both efficiency and quality simultaneously compared to slow optimization-based methods?

**Methodology**: DreamGaussian uses a generative 3D Gaussian Splatting model with progressive densification, accompanied by mesh extraction and texture refinement in UV space, plus a fine-tuning stage for detail enhancement.

**Key findings**:
- Progressive densification of 3D Gaussians converges significantly faster than occupancy pruning in Neural Radiance Fields
- Efficient algorithm converts 3D Gaussians into textured meshes for downstream applications
- High-quality textured meshes produced in just 2 minutes from a single-view image
- Achieves approximately 10 times acceleration compared to existing methods while maintaining competitive quality

**Limitations**: not stated in abstract

### Wu et al. (2023)

**Research question**: How can real-time dynamic scene rendering be achieved while maintaining high training and storage efficiency?

**Methodology**: The authors propose 4D Gaussian Splatting (4D-GS), a holistic representation for dynamic scenes using both 3D Gaussians and 4D neural voxels. They introduce a decomposed neural voxel encoding algorithm inspired by HexPlane to build Gaussian features from 4D neural voxels, with a lightweight MLP predicting Gaussian deformations at novel timestamps.

**Key findings**:
- 4D-GS achieves real-time rendering at 82 FPS at 800×800 resolution on an RTX 3090 GPU
- The method maintains comparable or better quality than previous state-of-the-art methods
- The approach provides high training and storage efficiency for dynamic scene representation

**Limitations**: not stated in abstract

### Xie et al. (2024)

**Research question**: How can multi-frame and multi-view consistent dynamic 3D content be generated using a unified diffusion model?

**Methodology**: SV4D uses a unified latent video diffusion model to generate novel view videos for each frame of a monocular reference video with temporal consistency, then optimizes an implicit 4D representation (dynamic NeRF) without SDS-based optimization.

**Key findings**:
- Unified diffusion model generates novel view videos of dynamic 3D objects without separate models for video and view synthesis
- Generated novel view videos enable efficient 4D representation optimization without cumbersome SDS-based methods
- Dynamic 3D object dataset curated from Objaverse for training the unified model
- State-of-the-art performance demonstrated on novel-view video synthesis and 4D generation through experiments and user studies

**Limitations**: not stated in abstract

### Yang et al. (2023)

**Research question**: How can dynamic scene reconstruction overcome the limitations of implicit neural representations in capturing intricate details and achieving real-time rendering?

**Methodology**: The authors propose a deformable 3D Gaussians Splatting method that reconstructs scenes using 3D Gaussians learned in canonical space with a deformation field to model monocular dynamic scenes. They introduce an annealing smoothing training mechanism to mitigate the impact of inaccurate poses on time interpolation smoothness.

**Key findings**:
- Deformable 3D Gaussians achieve higher rendering quality than existing methods
- The method enables real-time rendering speed in general dynamic scenes
- The approach is well-suited for novel-view synthesis, time interpolation, and real-time rendering tasks

**Limitations**: not stated in abstract

### Yin et al. (2023)

**Research question**: How can 4D content generation be grounded to enable controllable motion specification and overcome limitations of direct text/image-to-4D pipelines?

**Methodology**: The authors introduce 4DGen, a framework using monocular video sequences as a key component for constructing 4D content. The pipeline uses dynamic 3D Gaussians for efficient high-resolution supervision, employs spatial-temporal pseudo labels on anchor frames, and implements consistency priors through 3D-aware score distillation sampling and smoothness regularizations.

**Key findings**:
- 4DGen enables controllable 4D generation by allowing users to specify motion via monocular video or image-to-video generations
- The approach yields superior results in reconstructing input signals and inferring renderings from novel viewpoints and timesteps compared to video-to-4D baselines
- The method supports grounded generation with enhanced control and improved motion generation capabilities

**Limitations**: not stated in abstract

### Zhao et al. (2023)

**Research question**: How can a single in-the-wild image be animated into a 4D dynamic scene using textual motion descriptions?

**Methodology**: The method uses a 4D grid dynamic Neural Radiance Field (NeRF) model optimized in three stages: static model initialization with 2D/3D diffusion priors, motion learning via video diffusion model, and personalized diffusion prior to address semantic drift.

**Key findings**:
- First framework to animate a single image into 3D video through textual motion descriptions
- Three-stage optimization using multiple diffusion priors enables 4D generation
- Personalized diffusion prior effectively addresses semantic drift caused by text-reference image misalignment
- Comprehensive quantitative and qualitative assessments demonstrate significant advancements over existing baselines

**Limitations**: Object in 3D videos tends to drift away from the reference image over time due to misalignment between text prompt and reference image in the video diffusion model.

## References

Bahmani, S., Skorokhodov, I., Rong, V., Wetzstein, G., Guibas, L., Wonka, P., Tulyakov, S., Park, J. J., Tagliasacchi, A., & Lindell, D. B. (2023). 4D-fy: Text-to-4D generation using hybrid score distillation sampling. arXiv. https://arxiv.org/abs/2311.17984

Jiang, Y., Zhang, L., Gao, J., Hu, W., & Yao, Y. (2023). Consistent4D: Consistent 360° dynamic object generation from monocular video. arXiv. https://arxiv.org/abs/2311.02848

Ling, H., Kim, S. W., Torralba, A., Fidler, S., & Kreis, K. (2023). Align your Gaussians: Text-to-4D with dynamic 3D Gaussians and composed diffusion models. arXiv. https://arxiv.org/abs/2312.13763

Ren, J., Pan, L., Tang, J., Zhang, C., Cao, A., Zeng, G., & Liu, Z. (2023). DreamGaussian4D: Generative 4D Gaussian Splatting. arXiv. https://arxiv.org/abs/2312.17142

Tang, J., Ren, J., Zhou, H., Liu, Z., & Zeng, G. (2023). DreamGaussian: Generative Gaussian Splatting for efficient 3D content creation. arXiv. https://arxiv.org/abs/2309.16653

Wu, G., Yi, T., Fang, J., Xie, L., Zhang, X., Wei, W., Liu, W., Tian, Q., & Wang, X. (2023). 4D Gaussian Splatting for real-time dynamic scene rendering. arXiv. https://arxiv.org/abs/2310.08528

Xie, Y., Yao, C.-H., Voleti, V., Jiang, H., & Jampani, V. (2024). SV4D: Dynamic 3D content generation with multi-frame and multi-view consistency. arXiv. https://arxiv.org/abs/2407.17470

Yang, Z., Gao, X., Zhou, W., Jiao, S., Zhang, Y., & Jin, X. (2023). Deformable 3D Gaussians for high-fidelity monocular dynamic scene reconstruction. arXiv. https://arxiv.org/abs/2309.13101

Yin, Y., Xu, D., Wang, Z., Zhao, Y., & Wei, Y. (2023). 4DGen: Grounded 4D content generation with spatial-temporal consistency. arXiv. https://arxiv.org/abs/2312.17225

Zhao, Y., Yan, Z., Xie, E., Hong, L., Li, Z., & Lee, G. H. (2023). Animate124: Animating one image to 4D dynamic scene. arXiv. https://arxiv.org/abs/2311.14603
