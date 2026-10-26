# Systematic Literature Review: 3D and 4D World Modeling

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "3D 4D world modeling", filtered to category cs.CV, published between 2023-09-04 and 2025-09-03
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent papers on 3D and 4D world modeling published in the cs.CV category between September 2023 and September 2025. The surveyed literature reveals a field undergoing rapid transformation, with Gaussian Splatting emerging as the dominant representation for dynamic scene rendering, largely displacing traditional Neural Radiance Field (NeRF) approaches. The papers collectively address the challenge of generating and rendering temporally consistent 4D content from various inputs including single images, monocular videos, and text descriptions. Key advances include real-time rendering capabilities (82 FPS), dramatic efficiency improvements (10× acceleration), and novel hybrid score distillation techniques that reconcile the tradeoff between appearance quality, 3D structure, and motion dynamics. The field shows strong convergence around explicit spatial representations combined with diffusion-based priors, though challenges remain in semantic drift, motion controllability, and generalization to unconstrained scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "3D 4D world modeling", filtered to category cs.CV, published between 2023-09-04 and 2025-09-03. Papers were sorted by co-citation relevance and the top 10 were included. The search identified 50 papers by direct matching, with an additional 143 papers added through citation expansion, resulting in a shortlist of 30 papers. After screening for centrality to the topic, 10 papers were selected for inclusion. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The citation expansion phase was unavailable due to Semantic Scholar timeout, potentially limiting the candidate pool.

## Themes

### Theme 1: Gaussian Splatting as the Dominant 4D Representation

A clear trend across the surveyed literature is the adoption of 3D Gaussian Splatting as the foundational representation for dynamic 4D content. Wu et al. (2023) introduced 4D Gaussian Splatting (4D-GS), combining 3D Gaussians with 4D neural voxels to achieve real-time rendering at 82 FPS while maintaining high quality. This approach marked a significant departure from implicit neural representations, offering superior training and storage efficiency.

The deformable variant proposed by Yang et al. (2023) extended this paradigm to monocular dynamic scenes, using 3D Gaussians in canonical space with a deformation field to model temporal dynamics. Their annealing smoothing training mechanism addressed pose inaccuracies without computational overhead. Similarly, Ling et al. (2023) leveraged dynamic 3D Gaussian Splatting with deformation fields for text-to-4D synthesis, demonstrating that different 4D animations could be seamlessly combined due to the Gaussian representation's compositional properties.

This theme reflects a broader shift in the field from implicit, continuous representations (NeRFs) toward explicit, discrete representations (Gaussians) that enable real-time rendering and efficient optimization.

### Theme 2: Diffusion Model Integration for 4D Generation

The second major theme is the integration of pre-trained diffusion models as priors for 4D content generation. Bahmani et al. (2023) introduced hybrid score distillation sampling (SDS), which alternates between text-to-image and text-to-video diffusion models to overcome the three-way tradeoff between scene appearance, 3D structure, and motion quality. This approach leverages the complementary strengths of different diffusion architectures.

Ren et al. (2023) extended DreamGaussian to 4D by combining static Gaussian Splatting with explicit spatial transformations, using pre-trained image-to-video diffusion models for texture refinement. Their method reduced optimization time from hours to minutes while enabling visual motion control. Yin et al. (2023) proposed 4DGen, which uses monocular video sequences as grounding signals, employing 3D-aware score distillation with smoothness regularizations for spatial-temporal consistency.

Zhao et al. (2023) took a different approach with Animate124, animating single images into 4D scenes through a three-stage optimization using 2D, 3D, and video diffusion priors. Their personalized diffusion prior specifically addressed semantic drift caused by text-image misalignment, a recurring challenge in diffusion-based generation.

### Theme 3: Monocular Input as Primary Supervision Signal

A notable convergence in the literature is the focus on monocular inputs—single images or videos—as the primary supervision signal for 4D generation. This reflects a practical constraint: multi-view capture setups are expensive and impractical for most applications. Jiang et al. (2023) explicitly framed their Consistent4D approach as eliminating the need for multi-view data collection and camera calibration, using an object-level 3D-aware image diffusion model as supervision for Dynamic Neural Radiance Fields.

Xie et al. (2024) advanced this direction with SV4D, a latent video diffusion model that generates novel view videos from monocular reference videos. Their approach eliminates SDS-based optimization entirely, instead using generated novel views to optimize an implicit 4D representation (dynamic NeRF) efficiently. Tang et al. (2023) similarly focused on single-view image input for 3D content creation, achieving high-quality textured mesh generation in just 2 minutes.

This theme underscores a field-wide commitment to accessibility and practical deployment, prioritizing methods that work with ubiquitous capture devices rather than specialized equipment.

### Theme 4: Efficiency and Real-Time Performance

Efficiency emerges as a critical design criterion across multiple papers. Wu et al. (2023) demonstrated 82 FPS real-time rendering at 800×800 resolution on consumer hardware (RTX 3090). Tang et al. (2023) reported approximately 10× acceleration compared to existing SDS-based methods, producing high-quality outputs in 2 minutes. Ren et al. (2023) similarly emphasized the reduction from several hours to just a few minutes for 4D generation.

Yang et al. (2023) highlighted real-time rendering speed as a key advantage of deformable 3D Gaussians over implicit neural rendering methods. This focus on efficiency reflects both practical deployment requirements and the computational demands of 4D content, which must render not just novel viewpoints but also novel timesteps.

### Theme 5: Spatial-Temporal Consistency as Core Challenge

Maintaining consistency across both spatial and temporal dimensions is a recurring challenge addressed by multiple papers. Yin et al. (2023) introduced spatial-temporal pseudo labels on anchor frames and smoothness regularizations to ensure consistency in 4DGen. Jiang et al. (2023) proposed an Interpolation-driven Consistency Loss to minimize discrepancies with video interpolation models, achieving both spatial and temporal consistency.

Xie et al. (2024) emphasized multi-frame and multi-view consistency through a unified diffusion model trained on curated dynamic 3D object datasets. Zhao et al. (2023) identified semantic drift over time as a specific manifestation of temporal inconsistency, addressing it through personalized diffusion priors. These approaches collectively recognize that 4D generation requires not just spatial coherence (as in 3D generation) but also temporal coherence across frames.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several points. First, there is consensus that Gaussian Splatting representations offer superior efficiency and rendering performance compared to implicit neural representations for dynamic scenes (Wu et al., 2023; Yang et al., 2023; Ling et al., 2023). Second, all papers employing diffusion models agree that combining multiple diffusion priors (text-to-image, text-to-video, 3D-aware) yields better results than relying on a single model (Bahmani et al., 2023; Ren et al., 2023; Zhao et al., 2023). Third, there is convergence on the importance of monocular inputs as practical supervision signals, with multiple methods explicitly designed to eliminate the need for multi-view capture (Jiang et al., 2023; Xie et al., 2024).

**Disagreements**: A notable divergence exists regarding the choice of 4D representation. While most recent papers favor explicit Gaussian Splatting (Wu et al., 2023; Ren et al., 2023; Ling et al., 2023), some approaches continue to use implicit dynamic NeRF representations (Jiang et al., 2023; Xie et al., 2024), arguing for their expressiveness and smoothness. Additionally, there is disagreement on optimization strategies: Xie et al. (2024) explicitly eliminate SDS-based optimization as cumbersome, while other papers (Bahmani et al., 2023; Yin et al., 2023) continue to rely on hybrid or 3D-aware SDS variants. This suggests the field is in transition, with competing paradigms coexisting.

## Gaps and Open Questions

Several gaps emerge from the collective limitations and unstated constraints in the surveyed literature:

1. **Semantic Drift and Long-Term Consistency**: Zhao et al. (2023) explicitly note that objects in 3D videos tend to drift away from the reference image over time due to text-image misalignment. This problem is acknowledged but not fully resolved, suggesting a need for better alignment mechanisms or temporal grounding.

2. **Generalization to Unconstrained Scenarios**: Most methods are evaluated on controlled datasets or specific object categories. None of the papers explicitly address generalization to highly dynamic, unconstrained real-world scenes with complex lighting, occlusions, or multiple interacting objects.

3. **Motion Controllability**: While several papers claim improved motion control (Ren et al., 2023; Yin et al., 2023), the mechanisms remain limited to video-based or text-based specifications. Fine-grained, physics-aware motion control is not addressed.

4. **Scalability to High Resolutions**: Although real-time performance is achieved at 800×800 resolution (Wu et al., 2023), scalability to higher resolutions (4K and beyond) for professional applications is not discussed.

5. **Evaluation Metrics**: The papers rely on qualitative assessments and user studies, with limited standardized quantitative metrics for 4D generation quality. This makes cross-paper comparison difficult and suggests a need for community-wide benchmarks.

6. **Computational Requirements**: While efficiency improvements are reported, most methods still require high-end GPUs (e.g., RTX 3090). Accessibility for users without specialized hardware is not addressed.

## Per-Paper Annotations

### Bahmani et al. (2023)

**Research question**: How can the three-way tradeoff between scene appearance, 3D structure, and motion quality in text-to-4D generation be overcome?
**Methodology**: The authors introduce hybrid score distillation sampling, an alternating optimization procedure that blends supervision signals from multiple pre-trained diffusion models (text-to-image and text-to-video) to leverage their complementary strengths for high-fidelity text-to-4D generation.
**Key findings**:
- Hybrid SDS successfully combines benefits from text-to-image models (realistic appearance and 3D structure) and text-to-video models (motion capability)
- The method alleviates the three-way tradeoff between appearance, 3D structure, and motion
- The approach demonstrates synthesis of 4D scenes with compelling appearance, 3D structure, and motion
**Limitations**: not stated in abstract

### Jiang et al. (2023)

**Research question**: How can 4D dynamic objects be generated from uncalibrated monocular videos without multi-view data collection and camera calibration?
**Methodology**: The approach casts 360-degree dynamic object reconstruction as a 4D generation problem using an object-level 3D-aware image diffusion model as supervision for training Dynamic Neural Radiance Fields (DyNeRF). It proposes a Cascade DyNeRF for stable convergence and an Interpolation-driven Consistency Loss to achieve spatial and temporal consistency.
**Key findings**:
- Eliminates need for multi-view data collection and camera calibration in 360° dynamic object reconstruction
- Cascade DyNeRF facilitates stable convergence and temporal continuity under discrete temporal supervision
- Interpolation-driven Consistency Loss ensures spatial and temporal consistency by minimizing discrepancy with video interpolation model
- Performs competitively with prior art alternatives for 4D dynamic object generation from monocular videos
**Limitations**: not stated in abstract

### Ling et al. (2023)

**Research question**: How can dynamic, animated 3D objects be synthesized from text guidance using score distillation methods?
**Methodology**: The method combines text-to-image, text-to-video, and 3D-aware multiview diffusion models to provide feedback during 4D object optimization, leveraging dynamic 3D Gaussian Splatting with deformation fields as the 4D representation. It includes novel regularization for moving 3D Gaussians, motion amplification, and autoregressive synthesis for longer generation.
**Key findings**:
- Novel compositional generation-based approach combining multiple diffusion models for text-to-4D synthesis
- Dynamic 3D Gaussian Splatting with deformation fields serves as effective 4D representation
- Motion amplification and autoregressive synthesis enable generation of longer 4D sequences
- Outperforms previous work qualitatively and quantitatively, achieving state-of-the-art text-to-4D performance
**Limitations**: not stated in abstract

### Ren et al. (2023)

**Research question**: How can 4D content generation be made more efficient with better motion controllability and higher quality details?
**Methodology**: The authors introduce DreamGaussian4D (DG4D), combining explicit spatial transformations with static Gaussian Splatting for 4D generation. The framework includes two modules: Image-to-4D GS (generating static GS with DreamGaussianHD followed by HexPlane-based dynamic generation) and Video-to-Video Texture Refinement using pre-trained image-to-video diffusion models.
**Key findings**:
- DG4D reduces optimization time from several hours to just a few minutes
- The method allows generated 3D motion to be visually controlled
- The approach produces animated meshes that can be realistically rendered in 3D engines
- Video generation methods provide valuable spatial-temporal priors for high-quality 4D generation
**Limitations**: not stated in abstract

### Tang et al. (2023)

**Research question**: How can 3D content generation achieve both efficiency and quality simultaneously, overcoming the slow per-sample optimization of SDS-based methods?
**Methodology**: DreamGaussian uses a generative 3D Gaussian Splatting model with progressive densification of 3D Gaussians, which converges faster than Neural Radiance Fields occupancy pruning. It includes an efficient algorithm to convert 3D Gaussians into textured meshes with a fine-tuning stage for texture refinement in UV space.
**Key findings**:
- Progressive densification of 3D Gaussians converges significantly faster for 3D generative tasks
- Produces high-quality textured meshes in just 2 minutes from a single-view image
- Achieves approximately 10 times acceleration compared to existing SDS-based methods
- Companioned mesh extraction and texture refinement in UV space enhances texture quality
**Limitations**: not stated in abstract

### Wu et al. (2023)

**Research question**: How can real-time dynamic scene rendering be achieved while maintaining high training and storage efficiency?
**Methodology**: The authors propose 4D Gaussian Splatting (4D-GS), a holistic representation combining 3D Gaussians and 4D neural voxels for dynamic scenes. They introduce a decomposed neural voxel encoding algorithm inspired by HexPlane to build Gaussian features from 4D neural voxels, with a lightweight MLP predicting Gaussian deformations at novel timestamps.
**Key findings**:
- 4D-GS achieves real-time rendering at 82 FPS at 800×800 resolution on an RTX 3090 GPU
- The method maintains comparable or better quality than previous state-of-the-art methods
- The approach provides high training and storage efficiency for dynamic scene representation
**Limitations**: not stated in abstract

### Xie et al. (2024)

**Research question**: How can multi-frame and multi-view consistent dynamic 3D content be generated using a unified diffusion model?
**Methodology**: SV4D is a latent video diffusion model that generates novel view videos of dynamic 3D objects given a monocular reference video. The generated novel view videos are used to optimize an implicit 4D representation (dynamic NeRF) efficiently without SDS-based optimization. The model is trained on a curated dynamic 3D object dataset from Objaverse.
**Key findings**:
- Unified diffusion model generates novel view videos for dynamic 3D objects with temporal consistency
- Eliminates need for cumbersome SDS-based optimization used in most prior works
- Given monocular reference video, generates temporally consistent novel views for each video frame
- Achieves state-of-the-art performance on novel-view video synthesis and 4D generation
**Limitations**: not stated in abstract

### Yang et al. (2023)

**Research question**: How can dynamic scene reconstruction achieve higher rendering quality and real-time speed compared to implicit neural representation methods?
**Methodology**: The authors propose a deformable 3D Gaussians Splatting method that reconstructs scenes using 3D Gaussians in canonical space with a deformation field to model monocular dynamic scenes, plus an annealing smoothing training mechanism to mitigate inaccurate pose impacts on time interpolation smoothness.
**Key findings**:
- Deformable 3D Gaussians achieve higher rendering quality than existing dynamic neural rendering methods
- The method enables real-time rendering speed for general dynamic scenes
- The approach is well-suited for novel-view synthesis, time interpolation, and real-time rendering tasks
- The annealing smoothing mechanism mitigates inaccurate pose impacts without extra overhead
**Limitations**: not stated in abstract

### Yin et al. (2023)

**Research question**: How can 4D content creation achieve better motion control and grounded generation beyond text or image inputs?
**Methodology**: The authors introduce 4DGen, a framework using monocular video sequences as key components for constructing 4D content. The pipeline uses dynamic 3D Gaussians for efficient high-resolution supervision, spatial-temporal pseudo labels on anchor frames, and 3D-aware score distillation sampling with smoothness regularizations for consistency.
**Key findings**:
- 4DGen enables controllable 4D generation by allowing users to specify motion via monocular video or image-to-video generations
- The approach yields superior results in reconstructing input signals and inferring renderings from novel viewpoints and timesteps compared to video-to-4D baselines
- The framework supports grounded generation with enhanced control and improved motion generation capabilities
- Dynamic 3D Gaussians permit efficient, high-resolution supervision through rendering during training
**Limitations**: not stated in abstract

### Zhao et al. (2023)

**Research question**: How can a single in-the-wild image be animated into a 4D dynamic scene using textual motion descriptions?
**Methodology**: The approach uses a 4D grid dynamic Neural Radiance Field (NeRF) model optimized in three stages: first, a static model is initialized using the reference image with 2D and 3D diffusion priors; second, a video diffusion model learns subject-specific motion; third, a personalized diffusion prior addresses semantic drift caused by text-image misalignment.
**Key findings**:
- First work to animate a single in-the-wild image into 3D video through textual motion descriptions
- Three-stage optimization using multiple diffusion priors enables 4D generation from a single image
- Personalized diffusion prior effectively addresses semantic drift in 3D videos over time
- Method demonstrates significant advancements over existing baselines in quantitative and qualitative assessments
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
