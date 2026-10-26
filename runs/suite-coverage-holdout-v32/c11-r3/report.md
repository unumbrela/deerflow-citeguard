# Systematic Literature Review: 3D and 4D World Modeling

**Search Parameters:**
- **Database:** arXiv
- **Category:** cs.CV (Computer Vision)
- **Publication Period:** September 4, 2023 – September 3, 2025
- **Number of Papers:** 10

---

## References (APA Format)

1. Li, W., Zhou, R., Zhou, J., Song, Y., Herter, J., Qin, M., Huang, G., & Pfister, H. (2025). 4D LangSplat: 4D Language Gaussian Splatting via Multimodal Large Language Models. *arXiv preprint arXiv:2503.10437*. https://arxiv.org/abs/2503.10437v2

2. Cao, Y., Lu, J., Huang, Z., Shen, Z., Zhao, C., Hong, F., Chen, Z., Li, X., Wang, W., Liu, Y., & Liu, Z. (2025). Reconstructing 4D Spatial Intelligence: A Survey. *arXiv preprint arXiv:2507.21045*. https://arxiv.org/abs/2507.21045v2

3. Xie, H., Chen, Z., Hong, F., & Liu, Z. (2025). Compositional Generative Model of Unbounded 4D Cities. *arXiv preprint arXiv:2501.08983*. https://arxiv.org/abs/2501.08983v4

4. Wang, L., Zheng, W., Ren, Y., Jiang, H., Cui, Z., Yu, H., & Lu, J. (2024). OccSora: 4D Occupancy Generation Models as World Simulators for Autonomous Driving. *arXiv preprint arXiv:2405.20337*. https://arxiv.org/abs/2405.20337v1

5. Zhen, H., Sun, Q., Zhang, H., Li, J., Zhou, S., Du, Y., & Gan, C. (2025). TesserAct: Learning 4D Embodied World Models. *arXiv preprint arXiv:2504.20995*. https://arxiv.org/abs/2504.20995v1

6. Hu, Y., Wang, L., Liu, X., Chen, L.-H., Guo, Y., Shi, Y., Liu, C., Rao, A., Wang, Z., & Xiong, H. (2025). Simulating the Real World: A Unified Survey of Multimodal Generative Models. *arXiv preprint arXiv:2503.04641*. https://arxiv.org/abs/2503.04641v3

7. Liang, D., Zhang, D., Zhou, X., Tu, S., Feng, T., Li, X., Zhang, Y., Du, M., Tan, X., & Bai, X. (2025). UniFuture: A 4D Driving World Model for Future Generation and Perception. *arXiv preprint arXiv:2503.13587*. https://arxiv.org/abs/2503.13587v2

8. Zhao, Y., Lin, C.-C., Lin, K., Yan, Z., Li, L., Yang, Z., Wang, J., Lee, G. H., & Wang, L. (2024). GenXD: Generating Any 3D and 4D Scenes. *arXiv preprint arXiv:2411.02319*. https://arxiv.org/abs/2411.02319v2

9. Sun, W., Chen, S., Liu, F., Chen, Z., Duan, Y., Zhang, J., & Wang, Y. (2024). DimensionX: Create Any 3D and 4D Scenes from a Single Image with Controllable Video Diffusion. *arXiv preprint arXiv:2411.04928*. https://arxiv.org/abs/2411.04928v1

10. Liao, Z., Wei, P., Zhang, R., Chen, S., Wang, H., & Ren, Z. (2025). $I^{2}$-World: Intra-Inter Tokenization for Efficient Dynamic 4D Scene Forecasting. *arXiv preprint arXiv:2507.09144*. https://arxiv.org/abs/2507.09144v2

---

## Thematic Analysis

### 1. Survey and Framework Papers

**Cao et al. (2025)** present a comprehensive survey organizing 4D spatial intelligence reconstruction into five progressive levels: (1) low-level 3D attributes (depth, pose, point maps), (2) 3D scene components (objects, humans, structures), (3) 4D dynamic scenes, (4) interactions among scene components, and (5) physical laws and constraints. This hierarchical framework provides a structured understanding of the field's evolution.

**Hu et al. (2025)** offer a unified survey of multimodal generative models, tracing the progression from 2D (appearance) to video (appearance+dynamics), 3D (appearance+geometry), and finally 4D generation integrating all dimensions. This work bridges previously isolated domains and provides a systematic framework for understanding real-world simulation.

### 2. Autonomous Driving Applications

**Wang et al. (2024)** introduce OccSora, a diffusion-based 4D occupancy generation model that serves as a world simulator for autonomous driving. Using a 4D scene tokenizer and diffusion transformer, OccSora generates 16-second videos with authentic 3D layout and temporal consistency, conditioned on trajectory prompts.

**Liang et al. (2025)** propose UniFuture, a unified 4D driving world model that bridges appearance and geometry through Dual-Latent Sharing (DLS) and Multi-scale Latent Interaction (MLI) mechanisms. The model forecasts geometrically consistent 4D scene sequences from single frames, outperforming specialized models in both future generation and geometry perception.

**Liao et al. (2025)** present $I^{2}$-World, an efficient 4D occupancy forecasting framework using intra-scene and inter-scene tokenizers. The encoder-decoder architecture achieves state-of-the-art performance with 25.1% improvement in mIoU and real-time inference at 37.0 FPS, requiring only 2.9 GB training memory.

### 3. General 3D/4D Scene Generation

**Zhao et al. (2024)** develop GenXD, a framework for joint 3D and 4D scene generation using multiview-temporal modules that disentangle camera and object movements. The authors introduce CamVid-30K, a large-scale real-world 4D scene dataset curated from videos with camera poses and object motion annotations.

**Sun et al. (2024)** introduce DimensionX, which generates photorealistic 3D and 4D scenes from single images using controllable video diffusion. The ST-Director component decouples spatial and temporal factors through dimension-aware LoRAs, enabling precise manipulation of spatial structure and temporal dynamics.

**Xie et al. (2025)** propose CityDreamer4D, a compositional generative model for unbounded 4D cities. The approach separates dynamic objects (vehicles) from static scenes (buildings, roads) and uses different neural fields for different object types, supporting downstream applications like instance editing and urban simulation.

### 4. Language-Grounded and Embodied World Models

**Li et al. (2025)** present 4D LangSplat, which learns 4D language fields for time-sensitive open-vocabulary queries in dynamic scenes. The method uses Multimodal Large Language Models to generate temporally consistent object-wise video captions, bypassing the limitations of CLIP for temporal dynamics.

**Zhen et al. (2025)** introduce TesserAct, which learns 4D embodied world models predicting dynamic 3D scene evolution in response to agent actions. Training on RGB-DN (RGB, Depth, Normal) videos enables accurate inverse dynamic models, novel view synthesis, and policy learning surpassing prior video-based world models.

---

## Key Trends and Insights

1. **Temporal Dynamics Integration:** Recent work increasingly focuses on incorporating temporal consistency into 4D representations, moving beyond static 3D reconstruction.

2. **Multimodal Integration:** The integration of language, geometry, and appearance in unified frameworks represents a significant advancement toward more comprehensive world models.

3. **Efficiency Improvements:** New tokenization strategies and architectural designs (e.g., $I^{2}$-World's dual tokenizer) achieve substantial computational efficiency gains while maintaining or improving quality.

4. **Application-Specific Solutions:** Autonomous driving emerges as a dominant application area, with multiple specialized world models addressing trajectory prediction, occupancy forecasting, and scene simulation.

5. **Compositional Approaches:** Separating scene components (static vs. dynamic, instance vs. background) enables more controllable and editable 4D scene generation.

6. **Data Curation:** Several works emphasize the importance of large-scale, high-quality datasets (CamVid-30K, OSM, GoogleEarth, CityTopia) for training effective 4D models.

---

## Research Gaps and Future Directions

Based on the surveyed literature:

1. **Physical Realism:** While geometric and temporal consistency have improved, explicit modeling of physical laws (Level 5 in Cao et al.'s hierarchy) remains underexplored.

2. **Interactive Capabilities:** Most current models focus on passive observation rather than active interaction with 4D environments.

3. **Generalization:** Many approaches are domain-specific (e.g., autonomous driving), limiting cross-domain applicability.

4. **Real-Time Performance:** Despite efficiency improvements, real-time 4D scene generation and forecasting remain challenging for complex scenarios.

5. **Evaluation Metrics:** Standardized benchmarks and evaluation metrics for 4D world models need further development.

---

**Report Generated:** October 26, 2026  
**Search Executed:** arXiv cs.CV category, September 4, 2023 – September 3, 2025
