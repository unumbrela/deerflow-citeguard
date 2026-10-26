# Systematic Literature Review: Neural Radiance Fields

**Date:** October 26, 2026  
**Category:** Computer Vision (cs.CV)  
**Time Period:** 2024-2026 (Last 2 Years)

---

## Executive Summary

This systematic literature review examines 10 recent advances in Neural Radiance Fields (NeRF) published between 2024 and 2026. The selected papers address critical challenges including uncertainty quantification, temporal generalization, computational efficiency, flare removal, semantic understanding, domain generalization, reflection handling, avatar maintenance, and anisotropic appearance modeling. This review synthesizes key methodological innovations, applications, and future research directions.

---

## 1. Uncertainty Quantification in NeRF

### Evidential Neural Radiance Fields

**Citation:**  
Duan, R., & Wong, A. (2026). Evidential Neural Radiance Fields. *arXiv preprint arXiv:2602.23574*. https://arxiv.org/abs/2602.23574v2

**Summary:**  
This paper addresses the critical challenge of uncertainty estimation in NeRFs for safety-critical applications. The authors introduce a probabilistic approach that quantifies both aleatoric and epistemic uncertainties from a single forward pass without compromising rendering quality or incurring significant computational overhead. The method demonstrates state-of-the-art performance on three standardized benchmarks for both scene reconstruction fidelity and uncertainty estimation quality.

**Key Contributions:**
- Seamless integration of uncertainty quantification with NeRF rendering
- Direct quantification of both aleatoric and epistemic uncertainties
- Single forward pass efficiency
- State-of-the-art performance on standardized benchmarks

---

## 2. Temporal and Time-Variant Modeling

### TimeNeRF: Building Generalizable Neural Radiance Fields across Time from Few-Shot Input Views

**Citation:**  
Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building Generalizable Neural Radiance Fields across Time from Few-Shot Input Views. *arXiv preprint arXiv:2507.13929*. https://arxiv.org/abs/2507.13929v1

**Summary:**  
TimeNeRF presents a generalizable neural rendering approach for novel view synthesis at arbitrary viewpoints and times from few input views. The method combines multi-view stereo, neural radiance fields, and disentanglement strategies to enable smooth temporal transitions, particularly capturing natural scene changes from dawn to dusk. This work addresses the gap in temporal 3D scene modeling and introduces capabilities for metaverse applications requiring immersive day-night transitions.

**Key Contributions:**
- Few-shot generalization without per-scene optimization
- Arbitrary time rendering capabilities
- Smooth temporal transitions in natural scenes
- Integration of multi-view stereo with NeRF

---

## 3. Computational Efficiency and Accessibility

### Low-Cost Neural Radiance Fields

**Citation:**  
Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-Cost Neural Radiance Fields. *arXiv preprint arXiv:2605.09312*. https://arxiv.org/abs/2605.09312v1

**Summary:**  
This comparative study examines three accelerated NeRF variants (DS-NeRF, TensoRF, and HashNeRF) for low-compute, low-data regimes. The authors explore depth-supervised TensoRF, ablate feature-decoding MLP architectures, and propose four HashNeRF variants with residual and convolutional designs. While no extensions conclusively outperform baselines under iso-time evaluation, the work characterizes design tradeoffs for constrained settings.

**Key Contributions:**
- Comparative analysis of accelerated NeRF variants
- Depth-supervision loss integration with TensoRF
- Architectural ablation studies for HashNeRF
- Characterization of low-compute regime tradeoffs

---

## 4. Multi-View Image Enhancement

### GN-FR: Generalizable Neural Radiance Fields for Flare Removal

**Citation:**  
Matta, G. R., Siddartha, R., Girish, R. S. V., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable Neural Radiance Fields for Flare Removal. *arXiv preprint arXiv:2412.08200*. https://arxiv.org/abs/2412.08200v2

**Summary:**  
This pioneering work addresses lens flare removal using a multi-view NeRF framework. GN-FR leverages the view-dependent nature of flare artifacts to recover details obscured in individual images. The framework incorporates Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules within the Generalizable NeRF Transformer, utilizing a novel masking loss function for unsupervised learning. The authors also introduce a 3D multi-view flare dataset with 17 real scenes and 782 images.

**Key Contributions:**
- First NeRF-based flare removal framework
- Multi-view approach to ill-posed flare removal problem
- Unsupervised learning with masking loss function
- Novel 3D multi-view flare dataset

---

## 5. Comprehensive Surveys and Applications

### Neural Radiance Fields for the Real World: A Survey

**Citation:**  
Xiao, W., Chierchia, R., Santa Cruz, R., Li, X., Ahmedt-Aristizabal, D., Salvado, O., Fookes, C., & Lebrat, L. (2025). Neural Radiance Fields for the Real World: A Survey. *arXiv preprint arXiv:2501.13104*. https://arxiv.org/abs/2501.13104v3

**Summary:**  
This comprehensive survey compiles key theoretical advancements in NeRFs, alternative scene representations, and emerging challenges. It explores applications in reconstruction, examines NeRFs' impact on computer vision and robotics, and reviews essential datasets and toolkits. The survey identifies literature gaps and provides directions for future research, serving as a valuable resource for understanding NeRF's evolution and real-world deployment.

**Key Contributions:**
- Comprehensive compilation of NeRF advancements
- Analysis of alternative scene representations
- Review of applications in computer vision and robotics
- Identification of open challenges and future directions

---

## 6. Semantic Understanding and Remote Sensing

### Semantic Neural Radiance Fields for Multi-Date Satellite Data

**Citation:**  
Wagner, V., Bullinger, S., Bodensteiner, C., & Arens, M. (2025). Semantic Neural Radiance Fields for Multi-Date Satellite Data. *arXiv preprint arXiv:2502.16992*. https://arxiv.org/abs/2502.16992v1

**Summary:**  
This work proposes a satellite-specific NeRF model capable of obtaining three-dimensional semantic representations from multi-date satellite images with pixel-wise semantic labels. The approach demonstrates robustness in improving noisy input labels and enhances color prediction by utilizing semantic information to address temporal inconsistencies from non-stationary categories. The authors present a dataset with manually generated labels for popular multi-view satellite images.

**Key Contributions:**
- Neural semantic field generation from satellite imagery
- Robustness to noisy input labels
- Temporal inconsistency handling for non-stationary objects
- Novel satellite dataset with manual semantic labels

---

## 7. Domain Generalization

### NeuGen: Amplifying the 'Neural' in Neural Radiance Fields for Domain Generalization

**Citation:**  
Qazi, A., Basit, A., & Iqbal, A. (2025). NeuGen: Amplifying the 'Neural' in Neural Radiance Fields for Domain Generalization. *arXiv preprint arXiv:2505.06894*. https://arxiv.org/abs/2505.06894v1

**Summary:**  
NeuGen integrates a brain-inspired normalization technique into leading NeRF architectures (MVSNeRF and GeoNeRF) to enhance domain generalization. By extracting domain-invariant features, NeuGen improves accuracy and robustness in image rendering across diverse scenes. Comprehensive evaluations confirm superior generalizability and rendering quality compared to existing models, demonstrating the potential of merging neuroscientific principles with deep learning frameworks.

**Key Contributions:**
- Brain-inspired Neural Generalization technique
- Seamless integration with existing NeRF architectures
- Enhanced domain-invariant feature extraction
- Improved generalization across diverse datasets

---

## 8. Reflection Handling

### Planar Reflection-Aware Neural Radiance Fields

**Citation:**  
Gao, C., Wang, Y., Kim, C., Huang, J.-B., & Kopf, J. (2024). Planar Reflection-Aware Neural Radiance Fields. *arXiv preprint arXiv:2411.04984*. https://arxiv.org/abs/2411.04984v1

**Summary:**  
This paper addresses NeRF's limitation in handling complex planar reflections, which are often misinterpreted as erroneous geometries. The reflection-aware NeRF jointly models planar reflectors and explicitly casts reflected rays to capture high-frequency reflections. Sparse edge regularization prevents duplicate scene representations, enabling accurate geometry reconstruction and clean reflection-free views while reconstructing highly detailed reflections.

**Key Contributions:**
- Joint modeling of planar reflectors and reflected rays
- Single radiance field for primary and reflected color rendering
- Sparse edge regularization for accurate geometry
- Enhanced performance on real-world reflection datasets

---

## 9. Avatar and Human Modeling

### MaintaAvatar: A Maintainable Avatar Based on Neural Radiance Fields by Continual Learning

**Citation:**  
Gu, S., Qiu, Y.-K., Tang, Y.-M., Wu, A., & Zheng, W.-S. (2025). MaintaAvatar: A Maintainable Avatar Based on Neural Radiance Fields by Continual Learning. *arXiv preprint arXiv:2502.02372*. https://arxiv.org/abs/2502.02372v1

**Summary:**  
MaintaAvatar addresses the practical challenge of updating human avatars while maintaining rendering quality for past appearances. The model utilizes a Global-Local Joint Storage Module and Pose Distillation Module to resolve catastrophic forgetting and color bleeding issues. The approach requires only limited data collection for quick fine-tuning, achieving maintainable virtual avatars suitable for real-world scenarios where appearances and poses constantly change.

**Key Contributions:**
- Continual learning framework for NeRF-based avatars
- Global-Local Joint Storage Module
- Pose Distillation Module for pose accuracy
- Prevention of catastrophic forgetting and color bleeding

---

## 10. Material and Appearance Modeling

### ShinyNeRF: Digitizing Anisotropic Appearance in Neural Radiance Fields

**Citation:**  
Barreiro, A., Marí, R., Redondo, R., Haro, G., & Bosch, C. (2025). ShinyNeRF: Digitizing Anisotropic Appearance in Neural Radiance Fields. *arXiv preprint arXiv:2512.21692*. https://arxiv.org/abs/2512.21692v2

**Summary:**  
ShinyNeRF introduces a novel framework for handling both isotropic and anisotropic reflections, addressing the challenge of modeling anisotropic specular surfaces such as brushed metals. The method jointly estimates surface normals, tangents, specular concentration, and anisotropy magnitudes using Anisotropic Spherical Gaussian distributions. Experimental results demonstrate state-of-the-art performance in digitizing anisotropic specular reflections with plausible physical interpretations and material property editing capabilities.

**Key Contributions:**
- Joint isotropic and anisotropic reflection modeling
- Anisotropic Spherical Gaussian distribution learning
- Physical parameter estimation (normals, tangents, concentration)
- Material property editing capabilities

---

## Thematic Analysis

### Research Trends

The reviewed papers reveal several prominent research directions in NeRF development:

1. **Robustness and Reliability**: Evidential NeRF addresses uncertainty quantification, critical for safety-critical applications [citation: Duan & Wong, 2026](https://arxiv.org/abs/2602.23574v2).

2. **Temporal Dynamics**: TimeNeRF extends NeRF capabilities to temporal domains, enabling smooth transitions across time [citation: Hung et al., 2025](https://arxiv.org/abs/2507.13929v1).

3. **Accessibility**: Low-Cost NeRF research focuses on making NeRF technology more accessible through reduced computational requirements [citation: Huang et al., 2026](https://arxiv.org/abs/2605.09312v1).

4. **Domain Specificity**: Specialized applications emerge in satellite imagery [citation: Wagner et al., 2025](https://arxiv.org/abs/2502.16992v1), avatar creation [citation: Gu et al., 2025](https://arxiv.org/abs/2502.02372v1), and cultural heritage digitization [citation: Barreiro et al., 2025](https://arxiv.org/abs/2512.21692v2).

5. **Generalization**: Multiple works address domain generalization challenges through novel architectures and learning strategies [citation: Qazi et al., 2025](https://arxiv.org/abs/2505.06894v1; Hung et al., 2025](https://arxiv.org/abs/2507.13929v1).

### Methodological Innovations

Key methodological advances include:

- **Probabilistic frameworks** for uncertainty estimation
- **Multi-view approaches** for ill-posed problems like flare removal
- **Continual learning** for maintainable avatars
- **Brain-inspired normalization** for domain generalization
- **Physical parameter estimation** for material modeling
- **Sparse regularization** for accurate geometry reconstruction

### Application Domains

The papers demonstrate NeRF applications across diverse domains:

- **Robotics and safety-critical systems** (uncertainty-aware NeRF)
- **Metaverse and immersive experiences** (temporal NeRF)
- **Remote sensing** (satellite semantic NeRF)
- **Cultural heritage preservation** (anisotropic appearance modeling)
- **Virtual avatars** (maintainable avatar systems)
- **Computational photography** (flare removal)

---

## Open Challenges and Future Directions

Based on this systematic review, several open challenges emerge:

1. **Real-time Performance**: Despite acceleration efforts, achieving real-time NeRF rendering remains challenging for many applications.

2. **Generalization**: While progress has been made, robust generalization across vastly different scenes and conditions continues to be an active research area.

3. **Data Efficiency**: Few-shot and low-data regimes require further investigation to reduce data collection burdens.

4. **Physical Accuracy**: Balancing photorealism with physically plausible representations, especially for complex materials, needs continued development.

5. **Integration with Other Modalities**: Combining NeRF with semantic, temporal, and physical understanding represents a promising direction.

6. **Deployment in Production**: Bridging the gap between research prototypes and production-ready systems requires attention to uncertainty, efficiency, and maintainability.

---

## Conclusion

Neural Radiance Fields continue to evolve rapidly, with recent advances addressing fundamental challenges in uncertainty quantification, temporal modeling, computational efficiency, domain generalization, and specialized applications. The reviewed papers demonstrate the field's maturation from novel view synthesis toward comprehensive 3D scene understanding with practical real-world applicability. Future research will likely focus on improving generalization, efficiency, and integration with complementary modalities to enable broader deployment in production systems.

---

## References

Barreiro, A., Marí, R., Redondo, R., Haro, G., & Bosch, C. (2025). ShinyNeRF: Digitizing Anisotropic Appearance in Neural Radiance Fields. *arXiv preprint arXiv:2512.21692*. https://arxiv.org/abs/2512.21692v2

Duan, R., & Wong, A. (2026). Evidential Neural Radiance Fields. *arXiv preprint arXiv:2602.23574*. https://arxiv.org/abs/2602.23574v2

Gao, C., Wang, Y., Kim, C., Huang, J.-B., & Kopf, J. (2024). Planar Reflection-Aware Neural Radiance Fields. *arXiv preprint arXiv:2411.04984*. https://arxiv.org/abs/2411.04984v1

Gu, S., Qiu, Y.-K., Tang, Y.-M., Wu, A., & Zheng, W.-S. (2025). MaintaAvatar: A Maintainable Avatar Based on Neural Radiance Fields by Continual Learning. *arXiv preprint arXiv:2502.02372*. https://arxiv.org/abs/2502.02372v1

Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building Generalizable Neural Radiance Fields across Time from Few-Shot Input Views. *arXiv preprint arXiv:2507.13929*. https://arxiv.org/abs/2507.13929v1

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-Cost Neural Radiance Fields. *arXiv preprint arXiv:2605.09312*. https://arxiv.org/abs/2605.09312v1

Matta, G. R., Siddartha, R., Girish, R. S. V., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable Neural Radiance Fields for Flare Removal. *arXiv preprint arXiv:2412.08200*. https://arxiv.org/abs/2412.08200v2

Qazi, A., Basit, A., & Iqbal, A. (2025). NeuGen: Amplifying the 'Neural' in Neural Radiance Fields for Domain Generalization. *arXiv preprint arXiv:2505.06894*. https://arxiv.org/abs/2505.06894v1

Wagner, V., Bullinger, S., Bodensteiner, C., & Arens, M. (2025). Semantic Neural Radiance Fields for Multi-Date Satellite Data. *arXiv preprint arXiv:2502.16992*. https://arxiv.org/abs/2502.16992v1

Xiao, W., Chierchia, R., Santa Cruz, R., Li, X., Ahmedt-Aristizabal, D., Salvado, O., Fookes, C., & Lebrat, L. (2025). Neural Radiance Fields for the Real World: A Survey. *arXiv preprint arXiv:2501.13104*. https://arxiv.org/abs/2501.13104v3

---

**Document prepared:** October 26, 2026  
**Total papers reviewed:** 10  
**Time period:** 2024-2026  
**Category:** cs.CV (Computer Vision)
