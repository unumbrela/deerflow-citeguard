# Systematic Literature Review: Neural Radiance Fields

**Search Parameters:**
- **Category:** cs.CV (Computer Vision)
- **Time Window:** Last 2 years (2024-2026)
- **Papers Reviewed:** 10
- **Format:** APA

---

## Annotated Bibliography

### 1. Evidential Neural Radiance Fields

Duan, R., & Wong, A. (2026). Evidential Neural Radiance Fields. *arXiv preprint arXiv:2602.23574*. https://arxiv.org/abs/2602.23574v2

**Summary:** This paper addresses the critical challenge of uncertainty quantification in neural radiance fields for safety-critical applications. The authors introduce Evidential Neural Radiance Fields, a probabilistic approach that quantifies both aleatoric and epistemic uncertainties from a single forward pass without compromising rendering quality or incurring significant computational overhead. The method demonstrates state-of-the-art performance on three standardized benchmarks for both scene reconstruction fidelity and uncertainty estimation quality.

**Key Contributions:**
- First method to separately capture both aleatoric and epistemic uncertainties in NeRF
- Single forward pass uncertainty estimation
- State-of-the-art performance on standardized benchmarks

---

### 2. TimeNeRF: Building Generalizable Neural Radiance Fields across Time from Few-Shot Input Views

Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building Generalizable Neural Radiance Fields across Time from Few-Shot Input Views. *arXiv preprint arXiv:2507.13929*. https://arxiv.org/abs/2507.13929v1

**Summary:** TimeNeRF presents a generalizable neural rendering approach for rendering novel views at arbitrary viewpoints and times from few input views. The method combines multi-view stereo, neural radiance fields, and disentanglement strategies to enable temporal 3D scene modeling without per-scene optimization. The approach excels at creating realistic novel views that transition smoothly across different times, capturing intricate natural scene changes from dawn to dusk.

**Key Contributions:**
- Few-shot generalizable NeRF for temporal scene modeling
- No per-scene optimization required
- Smooth transitions across different times of day

---

### 3. Low-Cost Neural Radiance Fields

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-Cost Neural Radiance Fields. *arXiv preprint arXiv:2605.09312*. https://arxiv.org/abs/2605.09312v1

**Summary:** This comparative study examines three accelerated NeRF variants (DS-NeRF, TensoRF, and HashNeRF) in low-compute, low-data regimes. The authors explore extensions including depth-supervision loss for TensoRF, feature-decoding MLP ablation, and four architectural variants of HashNeRF color and density networks. While none of the extensions conclusively outperform published baselines under iso-time evaluation, the experiments characterize which extensions transfer to constrained settings.

**Key Contributions:**
- Systematic comparison of accelerated NeRF variants
- Depth-supervision extensions for reduced view counts
- Architectural variants for low-cost deployment

---

### 4. GN-FR: Generalizable Neural Radiance Fields for Flare Removal

Matta, G. R., Siddartha, R., Venkata Girish, R. S., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable Neural Radiance Fields for Flare Removal. *arXiv preprint arXiv:2412.08200*. https://arxiv.org/abs/2412.08200v2

**Summary:** This work addresses flare removal as a multi-view image problem using generalizable neural radiance fields. The proposed GN-FR framework incorporates Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules within the Generalizable NeRF Transformer framework. The method introduces a masking loss function for unsupervised learning and presents a new 3D multi-view flare dataset with 17 real flare scenes and 782 images.

**Key Contributions:**
- First NeRF-based approach to flare removal
- Unsupervised learning with masking loss
- New 3D multi-view flare dataset

---

### 5. Neural Radiance Fields for the Real World: A Survey

Xiao, W., Chierchia, R., Santa Cruz, R., Li, X., Ahmedt-Aristizabal, D., Salvado, O., Fookes, C., & Lebrat, L. (2025). Neural Radiance Fields for the Real World: A Survey. *arXiv preprint arXiv:2501.13104*. https://arxiv.org/abs/2501.13104v3

**Summary:** This comprehensive survey compiles key theoretical advancements and alternative scene representations in NeRF research. It investigates emerging challenges, explores applications in reconstruction, highlights NeRF's impact on computer vision and robotics, and reviews essential datasets and toolkits. The survey identifies gaps in the literature and discusses open challenges with directions for future research.

**Key Contributions:**
- Comprehensive review of NeRF theoretical advancements
- Analysis of real-world applications and challenges
- Identification of research gaps and future directions

---

### 6. Semantic Neural Radiance Fields for Multi-Date Satellite Data

Wagner, V., Bullinger, S., Bodensteiner, C., & Arens, M. (2025). Semantic Neural Radiance Fields for Multi-Date Satellite Data. *arXiv preprint arXiv:2502.16992*. https://arxiv.org/abs/2502.16992v1

**Summary:** This work proposes a satellite-specific NeRF model capable of obtaining a three-dimensional semantic representation from multi-date satellite images with corresponding pixel-wise semantic labels. The model demonstrates robustness in improving noisy input labels and enhances color prediction by utilizing semantic information to address temporal inconsistencies caused by non-stationary categories such as vehicles.

**Key Contributions:**
- First semantic NeRF for satellite data
- Improved handling of temporal inconsistencies
- New labeled dataset for multi-view satellite images

---

### 7. NeuGen: Amplifying the 'Neural' in Neural Radiance Fields for Domain Generalization

Qazi, A., Basit, A., & Iqbal, A. (2025). NeuGen: Amplifying the 'Neural' in Neural Radiance Fields for Domain Generalization. *arXiv preprint arXiv:2505.06894*. https://arxiv.org/abs/2505.06894v1

**Summary:** This paper proposes integrating a brain-inspired normalization technique called Neural Generalization (NeuGen) into leading NeRF architectures including MVSNeRF and GeoNeRF. NeuGen extracts domain-invariant features, enhancing models' generalization capabilities across diverse scenes and conditions. The approach demonstrates improved performance on benchmarks across diverse datasets and state-of-the-art NeRF architectures.

**Key Contributions:**
- Brain-inspired normalization technique for NeRF
- Enhanced domain generalization capabilities
- Improved rendering quality across varied scenes

---

### 8. Planar Reflection-Aware Neural Radiance Fields

Gao, C., Wang, Y., Kim, C., Huang, J.-B., & Kopf, J. (2024). Planar Reflection-Aware Neural Radiance Fields. *arXiv preprint arXiv:2411.04984*. https://arxiv.org/abs/2411.04984v1

**Summary:** This work addresses NeRF's limitation in handling complex planar reflections by introducing a reflection-aware NeRF that jointly models planar reflectors and explicitly casts reflected rays. The method proposes sparse edge regularization to utilize true sources of reflections, obtaining accurate scene geometry. The approach enables both clean, reflection-free views and highly detailed reflection reconstruction.

**Key Contributions:**
- Joint modeling of planar reflectors and scene geometry
- Sparse edge regularization for accurate reflections
- Dual capability: reflection-free and detailed reflection views

---

### 9. MaintaAvatar: A Maintainable Avatar Based on Neural Radiance Fields by Continual Learning

Gu, S., Qiu, Y.-K., Tang, Y.-M., Wu, A., & Zheng, W.-S. (2025). MaintaAvatar: A Maintainable Avatar Based on Neural Radiance Fields by Continual Learning. *arXiv preprint arXiv:2502.02372*. https://arxiv.org/abs/2502.02372v1

**Summary:** This work addresses the practical challenge of updating human avatars while maintaining the ability to render past appearances. The proposed MaintaAvatar resolves catastrophic forgetting issues through a Global-Local Joint Storage Module and a Pose Distillation Module. The model requires only limited data collection for quick fine-tuning while avoiding color bleeding and incorrect pose issues.

**Key Contributions:**
- Continual learning framework for maintainable avatars
- Global-Local Joint Storage Module
- Pose Distillation Module for avoiding catastrophic forgetting

---

### 10. ShinyNeRF: Digitizing Anisotropic Appearance in Neural Radiance Fields

Barreiro, A., Marí, R., Redondo, R., Haro, G., & Bosch, C. (2025). ShinyNeRF: Digitizing Anisotropic Appearance in Neural Radiance Fields. *arXiv preprint arXiv:2512.21692*. https://arxiv.org/abs/2512.21692v2

**Summary:** This paper introduces ShinyNeRF, a novel framework capable of handling both isotropic and anisotropic reflections for 3D digitization of cultural heritage. The method jointly estimates surface normals, tangents, specular concentration, and anisotropy magnitudes of an Anisotropic Spherical Gaussian distribution. Experimental results demonstrate state-of-the-art performance in digitizing anisotropic specular reflections with plausible physical interpretations.

**Key Contributions:**
- First NeRF framework for anisotropic reflections
- Joint estimation of multiple material properties
- State-of-the-art performance on specular surface digitization

---

## Thematic Analysis

### Emerging Research Directions

**1. Uncertainty Quantification**
The field is moving toward more trustworthy NeRF systems with proper uncertainty estimation. Evidential NeRF represents a significant advancement in capturing both aleatoric and epistemic uncertainties, crucial for safety-critical applications.

**2. Temporal and Dynamic Scene Modeling**
TimeNeRF and related works address the challenge of modeling scenes that change over time, enabling applications in metaverse and immersive experiences with smooth day-to-night transitions.

**3. Domain Generalization**
Multiple papers (NeuGen, GN-FR, Low-Cost NeRF) focus on improving generalization across diverse scenes and conditions, reducing the need for per-scene optimization and making NeRF more practical for real-world deployment.

**4. Specialized Applications**
Research is expanding into domain-specific applications including satellite imagery (Semantic NeRF), cultural heritage preservation (ShinyNeRF), flare removal (GN-FR), and avatar creation (MaintaAvatar).

**5. Computational Efficiency**
Several works address the computational challenges of NeRF, exploring accelerated variants and low-cost deployments while maintaining rendering quality.

### Key Challenges Identified

1. **Generalization:** Most NeRF methods still require per-scene optimization, limiting practical deployment
2. **Uncertainty:** Lack of reliable uncertainty estimation hinders safety-critical applications
3. **Dynamic Scenes:** Modeling temporal changes remains challenging
4. **Complex Reflections:** Planar and anisotropic reflections are difficult to handle accurately
5. **Catastrophic Forgetting:** Continual learning for maintainable models is an open problem
6. **Computational Cost:** Training times and data requirements limit accessibility

### Future Research Directions

Based on the surveyed literature, promising directions include:

- Integration of uncertainty quantification into production NeRF systems
- Development of more efficient few-shot and zero-shot generalization methods
- Better handling of complex material properties and lighting conditions
- Continual learning frameworks for evolving scenes and objects
- Domain-specific adaptations for robotics, cultural heritage, and remote sensing
- Reduction of computational requirements for broader accessibility

---

## References

Barreiro, A., Marí, R., Redondo, R., Haro, G., & Bosch, C. (2025). ShinyNeRF: Digitizing Anisotropic Appearance in Neural Radiance Fields. *arXiv preprint arXiv:2512.21692*. https://arxiv.org/abs/2512.21692v2

Duan, R., & Wong, A. (2026). Evidential Neural Radiance Fields. *arXiv preprint arXiv:2602.23574*. https://arxiv.org/abs/2602.23574v2

Gao, C., Wang, Y., Kim, C., Huang, J.-B., & Kopf, J. (2024). Planar Reflection-Aware Neural Radiance Fields. *arXiv preprint arXiv:2411.04984*. https://arxiv.org/abs/2411.04984v1

Gu, S., Qiu, Y.-K., Tang, Y.-M., Wu, A., & Zheng, W.-S. (2025). MaintaAvatar: A Maintainable Avatar Based on Neural Radiance Fields by Continual Learning. *arXiv preprint arXiv:2502.02372*. https://arxiv.org/abs/2502.02372v1

Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building Generalizable Neural Radiance Fields across Time from Few-Shot Input Views. *arXiv preprint arXiv:2507.13929*. https://arxiv.org/abs/2507.13929v1

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-Cost Neural Radiance Fields. *arXiv preprint arXiv:2605.09312*. https://arxiv.org/abs/2605.09312v1

Matta, G. R., Siddartha, R., Venkata Girish, R. S., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable Neural Radiance Fields for Flare Removal. *arXiv preprint arXiv:2412.08200*. https://arxiv.org/abs/2412.08200v2

Qazi, A., Basit, A., & Iqbal, A. (2025). NeuGen: Amplifying the 'Neural' in Neural Radiance Fields for Domain Generalization. *arXiv preprint arXiv:2505.06894*. https://arxiv.org/abs/2505.06894v1

Wagner, V., Bullinger, S., Bodensteiner, C., & Arens, M. (2025). Semantic Neural Radiance Fields for Multi-Date Satellite Data. *arXiv preprint arXiv:2502.16992*. https://arxiv.org/abs/2502.16992v1

Xiao, W., Chierchia, R., Santa Cruz, R., Li, X., Ahmedt-Aristizabal, D., Salvado, O., Fookes, C., & Lebrat, L. (2025). Neural Radiance Fields for the Real World: A Survey. *arXiv preprint arXiv:2501.13104*. https://arxiv.org/abs/2501.13104v3

---

**Generated:** 2026-10-26  
**Search Database:** arXiv  
**Primary Category:** cs.CV (Computer Vision)  
**Time Range:** 2024-10-26 to 2026-10-26
