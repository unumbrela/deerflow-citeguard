# Systematic Literature Review: 3D and 4D World Modeling

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "3D 4D world modeling", filtered to category cs.CV, published between 2023-09-04 and 2025-09-04
**Citation format**: APA 7th edition

## Executive Summary

The field of 3D and 4D world modeling has experienced rapid advancement between 2023 and 2025, with research progressing along multiple complementary directions. The surveyed literature reveals a field maturing from isolated methodological contributions toward comprehensive frameworks that integrate spatial and temporal dimensions. Two survey papers establish foundational taxonomies and definitions for the field, while the remaining works present novel generative models, embodied world models, and language-grounded 4D representations. A clear trend emerges toward compositional approaches that separate dynamic and static scene elements, leverage multimodal large language models for semantic grounding, and employ diffusion-based architectures for long-term temporal consistency. The literature demonstrates growing sophistication in handling real-world applications, particularly in autonomous driving and embodied AI, though challenges remain in standardization, scalability, and physical plausibility.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "3D 4D world modeling", filtered to category cs.CV, published between 2023-09-04 and 2025-09-04. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Foundational Taxonomies and Definitions

The field lacks standardized definitions for what constitutes a "world model" in 3D and 4D contexts. Kong et al. (2025) address this gap by establishing precise definitions and introducing a structured taxonomy spanning video-based (VideoGen), occupancy-based (OccGen), and LiDAR-based (LiDARGen) approaches. Their survey explicitly critiques prior work for emphasizing generative methods for 2D image and video data while overlooking native 3D and 4D representations such as RGB-D imagery, occupancy grids, and LiDAR point clouds. Similarly, Hu et al. (2025) propose a unified framework that systematically unifies 2D, video, 3D, and 4D generation within a single framework, investigating the progression of data dimensionality in real-world simulation. Cao et al. (2025) organize 4D spatial intelligence reconstruction into five progressive levels, ranging from low-level 3D attribute reconstruction to incorporation of physical laws and constraints. These three surveys collectively establish that the field requires clearer conceptual boundaries and hierarchical structures to enable meaningful comparison across methodologies.

### Theme 2: Compositional Generative Approaches for Complex Scenes

A prominent methodological trend involves decomposing complex 4D scenes into constituent elements that can be modeled separately and composed at inference time. Xie et al. (2025) propose CityDreamer4D, which separates dynamic objects (vehicles) from static scenes (buildings, roads) and uses different types of neural fields for each component. Their approach employs customized generative hash grids and periodic positional embeddings to handle the structural complexity and visual diversity of urban environments. Zhao et al. (2024) similarly disentangle camera and object movements through multiview-temporal modules in their GenXD framework, enabling seamless learning from both 3D and 4D data. This compositional paradigm addresses the challenge that generating 4D cities is more difficult than 3D scenes due to structurally complex objects, heightened visual diversity, and human sensitivity to distortions in urban environments. The compositional design also supports downstream applications such as instance editing, city stylization, and urban simulation.

### Theme 3: Diffusion-Based World Simulators for Autonomous Driving

Multiple works employ diffusion transformers to generate long-term temporally consistent 4D representations for autonomous driving applications. Wang et al. (2024) propose OccSora, a diffusion-based 4D occupancy generation model that employs a 4D scene tokenizer to obtain compact discrete spatial-temporal representations. Unlike autoregressive next-token prediction approaches, OccSora generates 16-second videos with authentic 3D layout and temporal consistency, demonstrating potential as a world simulator for autonomous driving decision-making. Liang et al. (2025) introduce UniFuture, which treats future RGB images and depth maps as coupled projections of the same 4D reality. Their Dual-Latent Sharing scheme maps visual and geometric modalities into a shared spatio-temporal latent space, forecasting high-fidelity, geometrically consistent 4D scene sequences from a single current frame. These approaches share the insight that trajectory-aware 4D generation is essential for practical autonomous driving applications, with both methods demonstrating superior performance on standard benchmarks like nuScenes and Waymo.

### Theme 4: Embodied World Models with Spatial-Temporal Consistency

Recent work emphasizes learning world models that predict dynamic evolution of 3D scenes in response to embodied agent actions. Zhen et al. (2025) present TesserAct, which trains on RGB-DN (RGB, Depth, and Normal) videos extended from robotic manipulation datasets using off-the-shelf models for depth and normal estimation. The approach fine-tunes a video generation model to jointly predict RGB-DN for each frame, then converts generated videos into high-quality 4D scenes. This method surpasses traditional 2D models by incorporating detailed shape, configuration, and temporal changes into predictions, enabling effective learning of accurate inverse dynamic models for embodied agents. The approach facilitates policy learning that significantly outperforms policies derived from prior video-based world models, demonstrating that embodied world models must ensure both temporal and spatial coherence to support downstream robotic tasks such as novel view synthesis and policy learning.

### Theme 5: Language-Grounded 4D Representations

Integrating natural language understanding with 4D scene representations enables open-vocabulary querying and semantic reasoning about dynamic scenes. Li et al. (2025) propose 4D LangSplat, which learns 4D language fields by bypassing vision features and instead learning directly from text generated via Multimodal Large Language Models (MLLMs). Their multimodal object-wise video prompting method generates detailed, temporally consistent captions for objects throughout a video, which are then encoded using a large language model into high-quality sentence embeddings. A status deformable network models smooth transitions across states in 4D scenes. This approach addresses a key limitation of CLIP-based methods like LangSplat, which cannot handle dynamic 4D fields because CLIP is designed for static image-text tasks and cannot capture temporal dynamics. The result is precise and efficient performance for both time-sensitive and time-agnostic open-vocabulary queries in dynamic scenes.

### Theme 6: Controllable Video Diffusion for 3D/4D Generation

Adapting video diffusion models for controllable 3D and 4D scene generation represents a promising direction that leverages existing video generation capabilities. Sun et al. (2024) propose DimensionX, a framework using controllable video diffusion with ST-Director to decouple spatial and temporal factors via dimension-aware LoRAs. Their trajectory-aware mechanisms bridge the gap between generated videos and real-world 3D scenes, while an identity-preserving denoising strategy improves 4D scene generation quality. The key insight is that video diffusion models can represent both 3D spatial structure and 4D temporal evolution through sequences of video frames when properly controlled. DimensionX achieves superior results in controllable video generation and 3D/4D scene generation compared to previous methods, demonstrating that single-image input can suffice for generating complex 3D and 4D scenes when combined with appropriate control mechanisms.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of separating dynamic and static scene elements for effective 4D generation (Xie et al., 2025; Zhao et al., 2024). There is broad agreement that native 3D and 4D representations (occupancy grids, LiDAR point clouds, RGB-D) are underexplored compared to 2D image and video generation (Kong et al., 2025; Hu et al., 2025). All autonomous driving-focused works emphasize the necessity of trajectory-aware generation for practical applications (Wang et al., 2024; Liang et al., 2025). The literature uniformly acknowledges that temporal consistency is a critical challenge that distinguishes 4D from 3D generation.

**Disagreements**: The surveyed papers do not exhibit fundamental methodological disagreements, likely reflecting the field's early stage of development. However, there is implicit tension between approaches that prioritize compositional, modular designs (Xie et al., 2025; Zhao et al., 2024) versus those that employ unified, end-to-end architectures (Sun et al., 2024; Zhen et al., 2025). The surveys differ in their proposed taxonomies: Kong et al. (2025) organize by data modality (VideoGen, OccGen, LiDARGen), while Cao et al. (2025) propose a five-level hierarchy of spatial intelligence, and Hu et al. (2025) organize by dimensionality progression (2D → video → 3D → 4D).

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are addressed only in full text or that the field has not yet developed standardized evaluation protocols for identifying failure modes. Kong et al. (2025) identify the absence of standardized definitions and taxonomies as a fundamental gap, though their own survey begins to address this. The compositional approaches (Xie et al., 2025; Zhao et al., 2024) require extensive datasets with real-world city layouts and large-scale imagery, raising questions about scalability and generalizability to less documented environments. Physical plausibility remains underexplored: while Cao et al. (2025) identify incorporation of physical laws as the highest level of 4D spatial intelligence, none of the generative models explicitly enforce physical constraints. The embodied world model literature (Zhen et al., 2025) depends on off-the-shelf models for depth and normal estimation, introducing potential error propagation that is not systematically analyzed. Finally, the language-grounded 4D representations (Li et al., 2025) rely on MLLM-generated captions, raising questions about caption quality, bias, and coverage of edge cases in dynamic scenes.

## Per-Paper Annotations

### Cao et al. (2025)

**Research question**: How can existing methods for 4D spatial intelligence reconstruction be organized into a comprehensive hierarchical structure that captures progressive levels of scene understanding?
**Methodology**: This survey presents a new perspective that organizes existing methods into five progressive levels of 4D spatial intelligence, ranging from low-level 3D attribute reconstruction to incorporation of physical laws and constraints, through comprehensive analysis of the hierarchical structure of 4D scene reconstruction.
**Key findings**:
- 4D spatial intelligence reconstruction can be organized into five progressive levels: low-level 3D attributes, 3D scene components, 4D dynamic scenes, interaction modeling, and physical laws incorporation.
- The field has evolved quickly, outpacing the scope of previous surveys, with applications ranging from entertainment to embodied AI.
- Existing surveys rarely offer a comprehensive analysis of the hierarchical structure of 4D scene reconstruction.
- Key challenges exist at each level that must be addressed to advance toward richer levels of 4D spatial intelligence.
- An up-to-date project page is maintained to track ongoing developments in the field.
**Limitations**: Not stated in abstract

### Hu et al. (2025)

**Research question**: How can we systematically unify the study of 2D, video, 3D, and 4D generation within a single framework for real-world simulation?
**Methodology**: This survey presents a unified framework for multimodal generative models by investigating the progression of data dimensionality in real-world simulation, starting from 2D generation (appearance), moving to video (appearance+dynamics) and 3D generation (appearance+geometry), and culminating in 4D generation that integrates all dimensions.
**Key findings**:
- Current methods often treat different modalities as independent domains, overlooking their interdependencies.
- This is the first attempt to systematically unify the study of 2D, video, 3D, and 4D generation within a single framework.
- The survey provides comprehensive review of datasets, evaluation metrics, and future directions.
- The framework serves as a bridge to advance the study of multimodal generative models and real-world simulation.
**Limitations**: Not stated in abstract

### Kong et al. (2025)

**Research question**: How can 3D and 4D world modeling be systematically defined, categorized, and advanced given the fragmented and inconsistent claims in current literature?
**Methodology**: This survey establishes precise definitions and introduces a structured taxonomy spanning video-based (VideoGen), occupancy-based (OccGen), and LiDAR-based (LiDARGen) approaches. It systematically summarizes datasets and evaluation metrics tailored to 3D/4D settings through comprehensive literature review.
**Key findings**:
- Prior world modeling work largely emphasizes generative methods for 2D image and video data while overlooking native 3D and 4D representations such as RGB-D imagery, occupancy grids, and LiDAR point clouds.
- The absence of a standardized definition and taxonomy for world models has led to fragmented and inconsistent claims in the literature.
- The survey provides the first comprehensive review explicitly dedicated to 3D and 4D world modeling and generation with precise definitions and structured taxonomy.
- Practical applications, open challenges, and promising research directions are identified to advance the field.
- A systematic summary of existing literature is maintained at a dedicated GitHub repository for ongoing reference.
**Limitations**: Not stated in abstract

### Li et al. (2025)

**Research question**: How can precise and efficient 4D language fields be learned to enable time-sensitive and time-agnostic open-vocabulary queries in dynamic scenes?
**Methodology**: The authors propose 4D LangSplat, which learns 4D language fields by bypassing vision features and instead learning directly from text generated via Multimodal Large Language Models (MLLMs) using a multimodal object-wise video prompting method. A status deformable network is further proposed to model smooth transitions across states in 4D scenes.
**Key findings**:
- Existing CLIP-based approaches like LangSplat cannot handle dynamic 4D fields because CLIP is designed for static image-text tasks and cannot capture temporal dynamics.
- 4D LangSplat uses MLLMs to generate detailed, temporally consistent, high-quality captions for objects throughout a video.
- Captions are encoded using a Large Language Model into high-quality sentence embeddings for open-vocabulary text queries through shared embedding spaces.
- The status deformable network effectively models continuous changes over time in 4D scenes.
- Results across multiple benchmarks demonstrate precise and efficient performance for both time-sensitive and time-agnostic open-vocabulary queries.
**Limitations**: Not stated in abstract

### Liang et al. (2025)

**Research question**: How can we bridge appearance and geometry to construct a holistic 4D representation for driving world models that overcomes the limitations of existing approaches focusing solely on 2D pixel-level video generation or static perception?
**Methodology**: The authors introduce UniFuture, which treats future RGB images and depth maps as coupled projections of the same 4D reality and models them jointly using a Dual-Latent Sharing (DLS) scheme that maps visual and geometric modalities into a shared spatio-temporal latent space, plus a Multi-scale Latent Interaction (MLI) mechanism for bidirectional consistency.
**Key findings**:
- UniFuture can forecast high-fidelity, geometrically consistent 4D scene sequences (image-depth pairs) from a single current frame.
- The Dual-Latent Sharing scheme implicitly entangles texture with structure.
- The Multi-scale Latent Interaction mechanism prevents structural hallucinations while refining geometric estimation.
- The method outperforms specialized models in both future generation and geometry perception on nuScenes and Waymo datasets.
**Limitations**: Not stated in abstract

### Sun et al. (2024)

**Research question**: How can video diffusion models be adapted to generate controllable 3D and 4D scenes from a single image?
**Methodology**: The authors propose DimensionX, a framework using controllable video diffusion with ST-Director to decouple spatial and temporal factors via dimension-aware LoRAs. They introduce trajectory-aware mechanisms for 3D generation and identity-preserving denoising for 4D generation, evaluating on real-world and synthetic datasets.
**Key findings**:
- Video diffusion models can represent both 3D spatial structure and 4D temporal evolution through sequences of video frames.
- ST-Director enables precise manipulation of spatial structure and temporal dynamics by learning dimension-aware LoRAs from dimension-variant data.
- Trajectory-aware mechanisms bridge the gap between generated videos and real-world 3D scenes.
- Identity-preserving denoising strategy improves 4D scene generation quality.
- DimensionX achieves superior results in controllable video generation and 3D/4D scene generation compared to previous methods.
**Limitations**: Not stated in abstract

### Wang et al. (2024)

**Research question**: How can we efficiently model long-term temporal evolutions of 3D scenes for autonomous driving without the inefficiencies of autoregressive next-token prediction?
**Methodology**: The authors propose OccSora, a diffusion-based 4D occupancy generation model that employs a 4D scene tokenizer to obtain compact discrete spatial-temporal representations and learns a diffusion transformer on these representations to generate 4D occupancy conditioned on trajectory prompts.
**Key findings**:
- OccSora can generate 16-second videos with authentic 3D layout and temporal consistency.
- The 4D scene tokenizer achieves high-quality reconstruction for long-sequence occupancy videos.
- The model demonstrates ability to understand spatial and temporal distributions of driving scenes.
- With trajectory-aware 4D generation, OccSora has potential to serve as a world simulator for autonomous driving decision-making.
**Limitations**: Not stated in abstract

### Xie et al. (2025)

**Research question**: How can unbounded 4D cities be generated effectively given the challenges of structurally complex objects, visual diversity, and human sensitivity to distortions in urban environments?
**Methodology**: The authors propose CityDreamer4D, a compositional generative model that separates dynamic objects from static scenes and uses different types of neural fields for buildings, vehicles, and background stuff. Traffic Scenario Generator and Unbounded Layout Generator produce dynamic traffic scenarios and static city layouts using compact BEV representation with customized generative hash grids and periodic positional embeddings.
**Key findings**:
- Generating 4D cities is more challenging than 3D scenes due to structurally complex objects, visual diversity, and heightened human sensitivity to distortions.
- 4D city generation should separate dynamic objects (e.g., vehicles) from static scenes (e.g., buildings and roads).
- Objects in 4D scenes should be composed of different types of neural fields employing customized generative hash grids and periodic positional embeddings.
- A comprehensive suite of datasets is provided including OSM, GoogleEarth, and CityTopia with real-world city layouts and large-scale city imagery.
- The compositional design supports downstream applications such as instance editing, city stylization, and urban simulation while delivering state-of-the-art performance.
**Limitations**: Not stated in abstract

### Zhao et al. (2024)

**Research question**: How can we jointly investigate general 3D and 4D generation by leveraging camera and object movements commonly observed in daily life despite the lack of large-scale 4D data?
**Methodology**: The authors propose a data curation pipeline to obtain camera poses and object motion strength from videos, introduce the CamVid-30K large-scale real-world 4D scene dataset, and develop GenXD framework with multiview-temporal modules that disentangle camera and object movements to learn from both 3D and 4D data.
**Key findings**:
- The data curation pipeline successfully extracts camera poses and object motion strength from videos.
- CamVid-30K provides a large-scale real-world 4D scene dataset.
- Multiview-temporal modules seamlessly learn from both 3D and 4D data by disentangling camera and object movements.
- GenXD can generate videos that follow camera trajectories as well as consistent 3D views that can be lifted into 3D representations.
- Extensive evaluations demonstrate GenXD's effectiveness and versatility compared to previous methods in 3D and 4D generation.
**Limitations**: Not stated in abstract

### Zhen et al. (2025)

**Research question**: How can we learn 4D embodied world models that predict dynamic evolution of 3D scenes over time in response to an embodied agent's actions with both spatial and temporal consistency?
**Methodology**: The authors train on RGB-DN (RGB, Depth, and Normal) videos by first extending existing robotic manipulation video datasets with depth and normal information using off-the-shelf models, then fine-tuning a video generation model to jointly predict RGB-DN for each frame, and finally converting generated videos into high-quality 4D scenes.
**Key findings**:
- The approach surpasses traditional 2D models by incorporating detailed shape, configuration, and temporal changes into predictions.
- The method enables effective learning of accurate inverse dynamic models for embodied agents.
- The approach ensures temporal and spatial coherence in 4D scene predictions from embodied scenarios.
- The method enables novel view synthesis for embodied environments.
- The approach facilitates policy learning that significantly outperforms those derived from prior video-based world models.
**Limitations**: Not stated in abstract

## References

Cao, Y., Lu, J., Huang, Z., Shen, Z., Zhao, C., Hong, F., Chen, Z., Li, X., Wang, W., Liu, Y., & Liu, Z. (2025). Reconstructing 4D spatial intelligence: A survey. arXiv. https://arxiv.org/abs/2507.21045

Hu, Y., Wang, L., Liu, X., Chen, L.-H., Guo, Y., Shi, Y., Liu, C., Rao, A., Wang, Z., & Xiong, H. (2025). Simulating the real world: A unified survey of multimodal generative models. arXiv. https://arxiv.org/abs/2503.04641

Kong, L., Yang, Y., Mei, J., Liu, Y., Liang, A., Zhu, D., Lu, D., Yin, W., Hu, X., Jia, M., Deng, J., Zhang, K., Wu, Y., Yan, T., Gao, S., Wang, S., Li, L., Pan, L., Liu, Y., & Zhu, J. (2025). 3D and 4D world modeling: A survey. arXiv. https://arxiv.org/abs/2509.07996

Li, W., Zhou, R., Zhou, J., Song, Y., Herter, J., Qin, M., Huang, G., & Pfister, H. (2025). 4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Model. arXiv. https://arxiv.org/abs/2503.10437

Liang, D., Zhang, D., Zhou, X., Tu, S., Feng, T., Li, X., Zhang, Y., Du, M., Tan, X., & Bai, X. (2025). UniFuture: A 4D driving world model for future generation and perception. arXiv. https://arxiv.org/abs/2503.13587

Sun, W., Chen, S., Liu, F., Chen, Z., Duan, Y., Zhang, J., & Wang, Y. (2024). DimensionX: Create any 3D and 4D scenes from a single image with controllable video diffusion. arXiv. https://arxiv.org/abs/2411.04928

Wang, L., Zheng, W., Ren, Y., Jiang, H., Cui, Z., Yu, H., & Lu, J. (2024). OccSora: 4D occupancy generation models as world simulators for autonomous driving. arXiv. https://arxiv.org/abs/2405.20337

Xie, H., Chen, Z., Hong, F., & Liu, Z. (2025). Compositional generative model of unbounded 4D cities. arXiv. https://arxiv.org/abs/2501.08983

Zhao, Y., Lin, C.-C., Lin, K., Yan, Z., Li, L., Yang, Z., Wang, J., Lee, G. H., & Wang, L. (2024). GenXD: Generating any 3D and 4D scenes. arXiv. https://arxiv.org/abs/2411.02319

Zhen, H., Sun, Q., Zhang, H., Li, J., Zhou, S., Du, Y., & Gan, C. (2025). TesserAct: Learning 4D embodied world models. arXiv. https://arxiv.org/abs/2504.20995
