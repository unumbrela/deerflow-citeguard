# Systematic Literature Review: 3D and 4D World Modeling

**Review Date:** October 26, 2026  
**Search Period:** September 4, 2023 – September 3, 2025  
**Category:** Computer Vision (cs.CV)  
**Total Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in 3D and 4D world modeling, focusing on dynamic scene representation, reconstruction, and generation. The reviewed papers span from September 2023 to July 2024, representing cutting-edge research in Gaussian Splatting, Neural Radiance Fields (NeRF), and diffusion-based generation methods. Key themes include real-time rendering, text-to-4D generation, monocular video reconstruction, and spatiotemporal consistency.

---

## Methodology

**Search Strategy:** Papers were identified through arXiv search in the cs.CV category with publication dates between September 4, 2023 and September 3, 2025. The search query targeted "3D 4D world modeling" with phrase matching and all-terms matching.

**Selection Criteria:** Papers were screened for relevance to 3D and 4D world modeling, scene representation, dynamic scene understanding, and spatiotemporal modeling in computer vision. The screening process identified 50 papers from initial search, added 143 papers from citation expansion, shortlisted 30 papers, and selected the 10 most central papers based on co-citation analysis.

---

## Annotated Bibliography

### 1. 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering

**Citation:** Wu, G., Yi, T., Fang, J., Xie, L., Zhang, X., Wei, W., Liu, W., Tian, Q., & Wang, X. (2023). 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering. *arXiv preprint arXiv:2310.08528*. https://arxiv.org/abs/2310.08528v3

**Summary:** This paper introduces 4D Gaussian Splatting (4D-GS), a holistic representation for dynamic scenes that achieves real-time rendering at 82 FPS at 800×800 resolution on an RTX 3090 GPU. The method combines 3D Gaussians with 4D neural voxels and uses a decomposed neural voxel encoding algorithm inspired by HexPlane to efficiently build Gaussian features. A lightweight MLP predicts Gaussian deformations at novel timestamps, enabling high-fidelity dynamic scene rendering with superior training and storage efficiency compared to applying 3D-GS frame-by-frame.

**Key Contributions:** Real-time dynamic scene rendering, explicit 4D representation, efficient neural voxel encoding.

---

### 2. 4D-fy: Text-to-4D Generation Using Hybrid Score Distillation Sampling

**Citation:** Bahmani, S., Skorokhodov, I., Rong, V., Wetzstein, G., Guibas, L., Wonka, P., Tulyakov, S., Park, J. J., Tagliasacchi, A., & Lindell, D. B. (2023). 4D-fy: Text-to-4D Generation Using Hybrid Score Distillation Sampling. *arXiv preprint arXiv:2311.17984*. https://arxiv.org/abs/2311.17984v2

**Summary:** This work addresses the three-way tradeoff in text-to-4D generation between scene appearance, 3D structure, and motion quality. The authors introduce hybrid score distillation sampling (SDS), an alternating optimization procedure that blends supervision signals from multiple pre-trained diffusion models including text-to-image and text-to-video models. By combining the complementary strengths of these models, hybrid SDS enables high-fidelity text-to-4D generation with compelling appearance, 3D structure, and motion simultaneously.

**Key Contributions:** Hybrid score distillation sampling, multi-model supervision, balanced quality across appearance-structure-motion dimensions.

---

### 3. Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction

**Citation:** Yang, Z., Gao, X., Zhou, W., Jiao, S., Zhang, Y., & Jin, X. (2023). Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction. *arXiv preprint arXiv:2309.13101*. https://arxiv.org/abs/2309.13101v2

**Summary:** This paper proposes deformable 3D Gaussian Splatting for monocular dynamic scene reconstruction. The method reconstructs scenes using 3D Gaussians in canonical space with a deformation field to model dynamic content. An annealing smoothing training mechanism mitigates the impact of inaccurate poses on temporal interpolation smoothness. The differential Gaussian rasterizer achieves both higher rendering quality and real-time rendering speed, outperforming implicit neural representation methods that struggle with intricate details and real-time performance.

**Key Contributions:** Deformation field for dynamic scenes, annealing smoothing mechanism, real-time monocular reconstruction.

---

### 4. DreamGaussian4D: Generative 4D Gaussian Splatting

**Citation:** Ren, J., Pan, L., Tang, J., Zhang, C., Cao, A., Zeng, G., & Liu, Z. (2023). DreamGaussian4D: Generative 4D Gaussian Splatting. *arXiv preprint arXiv:2312.17142*. https://arxiv.org/abs/2312.17142v3

**Summary:** DreamGaussian4D (DG4D) is an efficient 4D generation framework combining explicit spatial transformation modeling with static Gaussian Splatting. The framework includes two major modules: (1) Image-to-4D GS that generates static GS with DreamGaussianHD followed by HexPlane-based dynamic generation with Gaussian deformation, and (2) Video-to-Video Texture Refinement that enhances temporal consistency using pre-trained image-to-video diffusion models. DG4D reduces optimization time from hours to minutes while enabling visual motion control and producing animated meshes renderable in 3D engines.

**Key Contributions:** Efficient 4D generation (minutes vs. hours), motion controllability, video-to-video texture refinement.

---

### 5. 4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency

**Citation:** Yin, Y., Xu, D., Wang, Z., Zhao, Y., & Wei, Y. (2023). 4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency. *arXiv preprint arXiv:2312.17225*. https://arxiv.org/abs/2312.17225v3

**Summary:** 4DGen addresses limitations in existing 4D content creation pipelines by using monocular video sequences as grounded input for controllable 4D generation. The pipeline enables users to specify motion via monocular video or image-to-video generation, offering superior control compared to text-only approaches. Dynamic 3D Gaussians permit efficient high-resolution supervision through rendering during training. Spatial-temporal pseudo labels on anchor frames, combined with 3D-aware score distillation sampling and smoothness regularizations, ensure spatial-temporal consistency. The approach excels at reconstructing input signals and inferring novel viewpoint renderings.

**Key Contributions:** Grounded 4D generation from video, user-controllable motion, spatial-temporal consistency priors.

---

### 6. Animate124: Animating One Image to 4D Dynamic Scene

**Citation:** Zhao, Y., Yan, Z., Xie, E., Hong, L., Li, Z., & Lee, G. H. (2023). Animate124: Animating One Image to 4D Dynamic Scene. *arXiv preprint arXiv:2311.14603*. https://arxiv.org/abs/2311.14603v2

**Summary:** Animate124 is the first framework to animate a single in-the-wild image into 3D video through textual motion descriptions. The method uses a 4D grid dynamic Neural Radiance Field optimized in three stages: (1) static model initialization using reference image with 2D and 3D diffusion priors, (2) motion learning via video diffusion model, and (3) personalized diffusion prior to address semantic drift caused by text-reference image misalignment. As the pioneering image-text-to-4D generation framework, it demonstrates significant advancements over existing baselines.

**Key Contributions:** Single-image-to-4D animation, three-stage optimization, personalized diffusion for drift correction.

---

### 7. Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models

**Citation:** Ling, H., Kim, S. W., Torralba, A., Fidler, S., & Kreis, K. (2023). Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models. *arXiv preprint arXiv:2312.13763*. https://arxiv.org/abs/2312.13763v2

**Summary:** Align Your Gaussians (AYG) presents a compositional generation approach for text-to-4D synthesis, combining text-to-image, text-to-video, and 3D-aware multiview diffusion models to enforce temporal consistency, visual quality, and realistic geometry simultaneously. The method leverages dynamic 3D Gaussian Splatting with deformation fields, introducing novel regularization for moving Gaussian distributions to stabilize optimization and induce motion. Motion amplification and autoregressive synthesis schemes enable longer 4D sequences. AYG achieves state-of-the-art text-to-4D performance with seamless combination of different 4D animations.

**Key Contributions:** Compositional multi-model approach, Gaussian distribution regularization, motion amplification mechanism.

---

### 8. Consistent4D: Consistent 360° Dynamic Object Generation from Monocular Video

**Citation:** Jiang, Y., Zhang, L., Gao, J., Hu, W., & Yao, Y. (2023). Consistent4D: Consistent 360° Dynamic Object Generation from Monocular Video. *arXiv preprint arXiv:2311.02848*. https://arxiv.org/abs/2311.02848v1

**Summary:** Consistent4D addresses 360-degree dynamic object reconstruction from uncalibrated monocular videos, eliminating the need for multi-view data collection and camera calibration. The approach casts reconstruction as a 4D generation problem using object-level 3D-aware image diffusion models as supervision for training Dynamic Neural Radiance Fields (DyNeRF). A Cascade DyNeRF facilitates stable convergence under discrete temporal supervision, while an Interpolation-driven Consistency Loss minimizes discrepancies between rendered frames and video interpolation model outputs to achieve spatial-temporal consistency.

**Key Contributions:** Monocular video to 360° 4D generation, Cascade DyNeRF, interpolation-driven consistency loss.

---

### 9. SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency

**Citation:** Xie, Y., Yao, C.-H., Voleti, V., Jiang, H., & Jampani, V. (2024). SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency. *arXiv preprint arXiv:2407.17470*. https://arxiv.org/abs/2407.17470v2

**Summary:** Stable Video 4D (SV4D) presents a unified latent video diffusion model for multi-frame and multi-view consistent dynamic 3D content generation. Unlike prior methods using separately trained models for video generation and novel view synthesis, SV4D generates novel view videos of dynamic 3D objects from monocular reference videos with temporal consistency. The generated novel view videos optimize an implicit 4D representation (dynamic NeRF) efficiently without cumbersome SDS-based optimization. Training leverages a curated dynamic 3D object dataset from Objaverse, achieving state-of-the-art performance in novel-view video synthesis and 4D generation.

**Key Contributions:** Unified diffusion model for multi-view video generation, elimination of SDS optimization, dynamic 3D dataset curation.

---

### 10. DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation

**Citation:** Tang, J., Ren, J., Zhou, H., Liu, Z., & Zeng, G. (2023). DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation. *arXiv preprint arXiv:2309.16653*. https://arxiv.org/abs/2309.16653v2

**Summary:** DreamGaussian addresses the slow optimization bottleneck in 3D content generation via score distillation sampling. The framework combines generative 3D Gaussian Splatting with mesh extraction and UV-space texture refinement. Progressive densification of 3D Gaussians converges significantly faster than Neural Radiance Field occupancy pruning. An efficient algorithm converts 3D Gaussians into textured meshes with fine-tuning for detail refinement. DreamGaussian produces high-quality textured meshes in approximately 2 minutes from single-view images, achieving 10× acceleration over existing methods.

**Key Contributions:** 10× generation speedup, Gaussian-to-mesh conversion, progressive densification strategy.

---

## Thematic Analysis

### Representation Methods

The reviewed papers demonstrate a clear shift from implicit neural representations (NeRF-based) toward explicit Gaussian Splatting representations. Seven of ten papers utilize Gaussian Splatting variants (4D-GS, deformable 3DGS, DreamGaussian4D, 4DGen, AYG, SV4D, DreamGaussian), while three employ Neural Radiance Fields (Animate124, Consistent4D, SV4D). Gaussian Splatting's advantages include real-time rendering capabilities, efficient storage, and faster convergence during optimization.

### Generation Approaches

Three primary generation paradigms emerge:

1. **Text-to-4D:** 4D-fy, DreamGaussian4D, and AYG leverage text prompts with hybrid or composed score distillation sampling from multiple diffusion models.

2. **Image/Video-to-4D:** 4DGen, Animate124, and Consistent4D use visual inputs (images or monocular videos) as grounded supervision, offering superior motion control.

3. **Reconstruction-based:** 4D-GS, Deformable 3DGS focus on reconstructing dynamic scenes from input data rather than generative synthesis.

### Temporal Consistency

Spatial-temporal consistency represents a central challenge addressed through various mechanisms: video-to-video texture refinement (DreamGaussian4D), spatial-temporal pseudo labels (4DGen), interpolation-driven consistency loss (Consistent4D), personalized diffusion priors (Animate124), and autoregressive synthesis (AYG). SV4D uniquely addresses both multi-frame and multi-view consistency through unified diffusion modeling.

### Efficiency Improvements

Runtime efficiency is a major focus, with 4D-GS achieving 82 FPS real-time rendering, DreamGaussian4D reducing optimization from hours to minutes, and DreamGaussian achieving 10× acceleration in 3D generation. These improvements enable practical applications in real-time rendering and interactive content creation.

---

## Research Gaps and Future Directions

1. **Long-term Motion Modeling:** Most methods generate short 4D sequences; extending temporal duration while maintaining consistency remains challenging.

2. **Complex Scene Understanding:** Current approaches focus primarily on object-level generation; holistic scene understanding with multiple interacting objects needs further development.

3. **Physics-aware Generation:** Integration of physical constraints and dynamics into 4D generation could improve realism and controllability.

4. **Dataset Limitations:** Several papers note the need for larger, more diverse 4D datasets for training, as highlighted by SV4D's curation efforts.

5. **Evaluation Metrics:** Standardized benchmarks and metrics for 4D generation quality assessment require further development.

---

## Conclusion

The period from 2023-2025 witnessed remarkable advances in 3D and 4D world modeling, characterized by the emergence of Gaussian Splatting as a dominant representation, innovative hybrid score distillation techniques, and significant efficiency improvements. The convergence of diffusion models with explicit 3D/4D representations has enabled unprecedented capabilities in dynamic scene generation, reconstruction, and rendering. Future research addressing temporal duration, complex scene understanding, and physics-aware modeling will further advance the field toward practical real-world applications.

---

## References

Bahmani, S., Skorokhodov, I., Rong, V., Wetzstein, G., Guibas, L., Wonka, P., Tulyakov, S., Park, J. J., Tagliasacchi, A., & Lindell, D. B. (2023). 4D-fy: Text-to-4D Generation Using Hybrid Score Distillation Sampling. *arXiv preprint arXiv:2311.17984*. https://arxiv.org/abs/2311.17984v2

Jiang, Y., Zhang, L., Gao, J., Hu, W., & Yao, Y. (2023). Consistent4D: Consistent 360° Dynamic Object Generation from Monocular Video. *arXiv preprint arXiv:2311.02848*. https://arxiv.org/abs/2311.02848v1

Ling, H., Kim, S. W., Torralba, A., Fidler, S., & Kreis, K. (2023). Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models. *arXiv preprint arXiv:2312.13763*. https://arxiv.org/abs/2312.13763v2

Ren, J., Pan, L., Tang, J., Zhang, C., Cao, A., Zeng, G., & Liu, Z. (2023). DreamGaussian4D: Generative 4D Gaussian Splatting. *arXiv preprint arXiv:2312.17142*. https://arxiv.org/abs/2312.17142v3

Tang, J., Ren, J., Zhou, H., Liu, Z., & Zeng, G. (2023). DreamGaussian: Generative Gaussian Splatting for Efficient 3D Content Creation. *arXiv preprint arXiv:2309.16653*. https://arxiv.org/abs/2309.16653v2

Wu, G., Yi, T., Fang, J., Xie, L., Zhang, X., Wei, W., Liu, W., Tian, Q., & Wang, X. (2023). 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering. *arXiv preprint arXiv:2310.08528*. https://arxiv.org/abs/2310.08528v3

Xie, Y., Yao, C.-H., Voleti, V., Jiang, H., & Jampani, V. (2024). SV4D: Dynamic 3D Content Generation with Multi-Frame and Multi-View Consistency. *arXiv preprint arXiv:2407.17470*. https://arxiv.org/abs/2407.17470v2

Yang, Z., Gao, X., Zhou, W., Jiao, S., Zhang, Y., & Jin, X. (2023). Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction. *arXiv preprint arXiv:2309.13101*. https://arxiv.org/abs/2309.13101v2

Yin, Y., Xu, D., Wang, Z., Zhao, Y., & Wei, Y. (2023). 4DGen: Grounded 4D Content Generation with Spatial-temporal Consistency. *arXiv preprint arXiv:2312.17225*. https://arxiv.org/abs/2312.17225v3

Zhao, Y., Yan, Z., Xie, E., Hong, L., Li, Z., & Lee, G. H. (2023). Animate124: Animating One Image to 4D Dynamic Scene. *arXiv preprint arXiv:2311.14603*. https://arxiv.org/abs/2311.14603v2

---

**Review Statistics:**
- Initial pool: 50 papers
- Citation expansion: +143 papers
- Shortlisted: 30 papers
- Final selection: 10 papers
- Citation count range: 9-19 citations per paper
