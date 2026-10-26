# Systematic Literature Review: Neural Radiance Fields

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: arXiv search "neural radiance fields", category cs.CV, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent papers on Neural Radiance Fields (NeRF) published on arXiv within the last two years in the computer vision category. The surveyed literature reveals a field rapidly maturing beyond novel view synthesis fundamentals toward addressing practical deployment challenges. Key research directions include uncertainty quantification for safety-critical applications, temporal modeling for dynamic scenes, domain generalization across diverse environments, specialized handling of optical phenomena (reflections, lens flare), and efficient architectures for resource-constrained settings. Collectively, these works demonstrate NeRF's expansion into real-world applications including satellite imagery, avatar creation, cultural heritage digitization, and computational photography. However, significant gaps remain in computational efficiency, long-term maintenance of deployed models, and handling of complex real-world conditions.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "neural radiance fields", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Uncertainty Quantification and Trustworthiness

As NeRF technology advances toward deployment in safety-critical applications, understanding and quantifying uncertainty has emerged as a fundamental challenge. Duan and Wong (2026) identify that existing uncertainty quantification methods fail to separately capture both aleatoric (data-related) and epistemic (model-related) uncertainties, often compromising rendering quality or incurring significant computational overhead. Their Evidential Neural Radiance Fields approach addresses this by integrating probabilistic methods directly into the NeRF rendering process, enabling direct quantification of both uncertainty types from a single forward pass. This work represents a critical step toward trustworthy 3D scene modeling, demonstrating state-of-the-art performance on both reconstruction fidelity and uncertainty estimation quality across three standardized benchmarks. The emphasis on maintaining rendering quality while providing uncertainty estimates reflects the field's growing recognition that theoretical guarantees must not come at the expense of practical performance.

### Theme 2: Temporal and Dynamic Scene Modeling

A significant research direction involves extending NeRF beyond static scenes to model temporal changes and dynamic environments. Hung et al. (2025) present TimeNeRF, which addresses the challenge of rendering novel views at arbitrary viewpoints and times from few-shot input views. This work is particularly motivated by metaverse applications requiring immersive 3D environments that naturally transition between different times of day. The approach combines multi-view stereo, neural radiance fields, and disentanglement strategies to construct implicit content radiance fields that can be queried at any arbitrary time. The key innovation lies in the model's ability to generalize across scenes without per-scene optimization while capturing intricate natural scene changes from dawn to dusk. This temporal extension addresses a critical limitation of standard NeRF formulations, which assume static scenes, and opens new applications in virtual environments and time-lapse 3D reconstruction.

### Theme 3: Domain Generalization and Transferability

The challenge of generalizing NeRF models across diverse scenes and conditions has attracted significant attention, with multiple approaches emerging to address this limitation. Qazi et al. (2025) propose NeuGen, a brain-inspired normalization technique that extracts domain-invariant features and can be seamlessly integrated into existing NeRF architectures including MVSNeRF and GeoNeRF. Their approach cultivates a comprehensive feature set that significantly improves both accuracy and robustness in image rendering across varied scenes. The work exemplifies a broader trend of incorporating insights from neuroscience into deep learning frameworks for computer vision. Similarly, the survey by Xiao et al. (2025) identifies domain generalization as one of the key emerging challenges in real-world NeRF deployment, compiling theoretical advancements and alternative scene representations that enable better transfer across domains. These works collectively recognize that per-scene optimization, while effective, limits NeRF's practical applicability, and that learning transferable representations is essential for widespread adoption.

### Theme 4: Specialized Handling of Optical Phenomena

Several recent works address specific optical challenges that standard NeRF formulations handle poorly. Gao et al. (2024) tackle the problem of planar reflections, which standard NeRF interprets as erroneous scene geometries, leading to duplicated and inaccurate representations. Their reflection-aware NeRF jointly models planar reflectors and explicitly casts reflected rays to capture high-frequency reflections, using sparse edge regularization to prevent duplicate scene representations. Barreiro et al. (2025) address an even more specialized challenge: anisotropic specular surfaces such as brushed metals, which existing methods struggle to model accurately. Their ShinyNeRF framework jointly estimates surface normals, tangents, specular concentration, and anisotropy magnitudes, achieving state-of-the-art performance on digitizing anisotropic specular reflections while offering plausible physical interpretations. Matta et al. (2024) frame lens flare removal as a multi-view NeRF problem, leveraging the view-dependent nature of flare artifacts to recover details obscured in individual images. These specialized approaches demonstrate the field's maturation from general-purpose novel view synthesis toward addressing specific real-world imaging challenges that require domain-specific solutions.

### Theme 5: Computational Efficiency and Accessibility

The computational demands of NeRF training and inference remain a significant barrier to accessibility, prompting research into low-cost variants. Huang et al. (2026) present a comparative study of three accelerated NeRF variants—DS-NeRF, TensoRF, and HashNeRF—exploring extensions targeted at the low-compute, low-data regime. Their work includes adding depth-supervision loss to TensoRF, ablating the feature-decoding MLP, and proposing architectural variants of HashNeRF with residual and convolutional designs. While their experiments reveal that none of the proposed extensions conclusively outperform published baselines under iso-time evaluation, the work characterizes which extensions transfer to constrained settings and surfaces important design questions for future research. This honest assessment of tradeoffs between PSNR, training time, and data requirements provides valuable guidance for practitioners working in resource-constrained environments.

### Theme 6: Application-Specific NeRF Variants

The literature reveals NeRF's expansion into diverse application domains, each requiring specialized adaptations. Wagner et al. (2025) develop a satellite-specific NeRF model capable of obtaining three-dimensional semantic representations from multi-date satellite images with pixel-wise semantic labels. Their approach addresses temporal inconsistencies caused by non-stationary categories such as vehicles and demonstrates the capability to improve noisy input labels. Gu et al. (2025) address the practical challenge of maintaining virtual avatars that must be updated with new appearances and poses while avoiding catastrophic forgetting of past information. Their MaintaAvatar utilizes a Global-Local Joint Storage Module and Pose Distillation Module to enable continual learning, requiring only limited data collection for fine-tuning while maintaining rendering quality of past appearances. These application-driven innovations demonstrate NeRF's versatility while highlighting that each domain—satellite imagery, avatar creation, cultural heritage—presents unique challenges requiring tailored solutions.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that standard NeRF formulations, while effective for novel view synthesis in controlled settings, require significant modifications for real-world deployment. Multiple works identify the need for uncertainty quantification (Duan & Wong, 2026), domain generalization (Qazi et al., 2025; Xiao et al., 2025), and computational efficiency (Huang et al., 2026) as critical prerequisites for practical applications. There is also consensus that leveraging multi-view information provides advantages over single-image approaches, particularly for handling view-dependent phenomena such as lens flare (Matta et al., 2024) and planar reflections (Gao et al., 2024).

**Disagreements**: The literature reveals tension between specialization and generalization approaches. While some works advocate for highly specialized architectures targeting specific challenges (e.g., ShinyNeRF for anisotropic surfaces, TimeNeRF for temporal modeling), others pursue more general solutions that can be integrated into existing frameworks (e.g., NeuGen's normalization technique). Additionally, there is implicit disagreement about the role of per-scene optimization: TimeNeRF explicitly avoids it for generalizability, while MaintaAvatar accepts limited per-scene fine-tuning as a practical compromise. The computational efficiency study by Huang et al. (2026) also reveals that proposed extensions to accelerated NeRF variants do not always improve upon baselines, suggesting that the optimal approach may be context-dependent rather than universally applicable.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Computational overhead of advanced features**: Multiple papers acknowledge that their improvements come with computational costs, but few provide systematic analysis of tradeoffs. Duan and Wong (2026) note computational overhead concerns but do not quantify them extensively. Barreiro et al. (2025) acknowledge complexity of jointly estimating multiple surface properties but do not report real-time rendering capabilities.

2. **Long-term maintenance and scalability**: While MaintaAvatar (Gu et al., 2025) addresses catastrophic forgetting, the approach still requires data collection for updates, and long-term accumulation of updates and storage requirements remain unaddressed. The field lacks systematic approaches to managing NeRF models over extended deployment periods.

3. **Evaluation under realistic conditions**: Most evaluations use standardized benchmarks that may not reflect real-world deployment conditions. Huang et al. (2026) explicitly note that their experiments characterize which extensions transfer to constrained settings, implying that standard benchmarks may not capture practical constraints.

4. **Integration of multiple specialized capabilities**: Individual papers address specific challenges (reflections, temporal changes, uncertainty), but the literature lacks work on integrating multiple capabilities into unified frameworks. A deployed system may need to handle reflections, temporal changes, and provide uncertainty estimates simultaneously.

5. **Data requirements and annotation burden**: Several approaches require specialized annotations (semantic labels for satellite NeRF, flare-occupancy masks) that may be expensive to obtain in practice. The field needs more work on reducing annotation requirements while maintaining performance.

## Per-Paper Annotations

### Barreiro et al. (2025)

**Research question**: How can Neural Radiance Fields accurately model anisotropic specular surfaces, such as brushed metals, that existing methods struggle to represent?

**Methodology**: The authors introduce ShinyNeRF that jointly estimates surface normals, tangents, specular concentration, and anisotropy magnitudes of an Anisotropic Spherical Gaussian distribution by learning an approximation of outgoing radiance as an encoded mixture of isotropic von Mises-Fisher distributions.

**Key findings**:
- ShinyNeRF achieves state-of-the-art performance on digitizing anisotropic specular reflections
- The method handles both isotropic and anisotropic reflections effectively
- The framework offers plausible physical interpretations of material properties
- Material properties can be edited compared to existing methods
- The approach successfully estimates multiple surface properties jointly

**Limitations**: The computational complexity of jointly estimating multiple surface properties and learning mixture distributions may be significant. The abstract does not address performance on non-specular surfaces or mixed material scenarios, and real-time rendering capabilities are not mentioned.

### Duan and Wong (2026)

**Research question**: How can Neural Radiance Fields separately capture both aleatoric and epistemic uncertainties without compromising rendering quality or incurring significant computational overhead?

**Methodology**: The authors introduce Evidential Neural Radiance Fields, a probabilistic approach that seamlessly integrates with the NeRF rendering process, enabling direct quantification of both aleatoric and epistemic uncertainties from a single forward pass.

**Key findings**:
- The approach quantifies both aleatoric and epistemic uncertainties simultaneously
- Integration with NeRF rendering is seamless, requiring only a single forward pass
- Demonstrates state-of-the-art scene reconstruction fidelity on three standardized benchmarks
- Achieves state-of-the-art uncertainty estimation quality compared to existing methods
- Code is publicly available at https://github.com/KerryDRX/EvidentialNeRF

**Limitations**: The evaluation focuses on standardized benchmarks, and real-world deployment in safety-critical settings is not demonstrated. The approach's performance under extreme viewing conditions or with highly ambiguous input data is not thoroughly explored.

### Gao et al. (2024)

**Research question**: How can Neural Radiance Fields accurately handle complex planar reflections that cause erroneous scene geometries and duplicated representations?

**Methodology**: The authors introduce a reflection-aware NeRF that jointly models planar reflectors and explicitly casts reflected rays to capture high-frequency reflections, using sparse edge regularization to prevent duplicate scene representations along primary rays.

**Key findings**:
- The method accurately handles planar reflections that standard NeRF interprets as erroneous geometries
- Rendering along primary rays produces clean, reflection-free views
- Explicitly rendering along reflected rays reconstructs highly detailed reflections
- Sparse edge regularization helps utilize true reflection sources rather than creating duplicates
- Extensive evaluations on real-world datasets demonstrate enhanced performance in reflection handling

**Limitations**: The approach specifically targets planar reflections (such as windows) and may not generalize to curved or complex reflective surfaces. The method requires proper identification of planar reflectors, which may need additional supervision or preprocessing.

### Gu et al. (2025)

**Research question**: How can human avatars based on Neural Radiance Fields be updated with new appearances and poses while maintaining rendering quality of past appearances without catastrophic forgetting?

**Methodology**: The authors propose MaintaAvatar utilizing a Global-Local Joint Storage Module and a Pose Distillation Module to enable continual learning that resolves catastrophic forgetting, color bleeding issues, and incorrect human body poses.

**Key findings**:
- The model requires only limited data collection to quickly fine-tune for new appearances and poses
- MaintaAvatar avoids catastrophic forgetting that typically degrades rendering quality of past appearances
- The approach resolves color bleeding issues common in continual learning scenarios
- Correct human body poses are maintained across updates
- Experimental results validate effectiveness in achieving maintainable virtual avatars

**Limitations**: The approach still requires some data collection for each update, and the abstract does not specify how many new samples are needed or how frequently the model can be updated. Long-term accumulation of updates and storage requirements are not addressed.

### Huang et al. (2026)

**Research question**: How can Neural Radiance Fields be accelerated and adapted for low-compute, low-data regimes while maintaining acceptable rendering quality?

**Methodology**: The authors present a comparative study of three accelerated NeRF variants (DS-NeRF, TensoRF, and HashNeRF), adding depth-supervision loss to TensoRF, ablating the feature-decoding MLP, and proposing four architectural variants of HashNeRF with residual and convolutional designs.

**Key findings**:
- Under iso-time evaluation, none of the proposed extensions conclusively outperform published baselines
- Depth-supervision from COLMAP keypoints can be integrated into TensoRF for reduced view counts
- Input downsampling affects PSNR and runtime in predictable ways on synthetic scenes
- Residual and convolutional designs for HashNeRF show different PSNR/training-time tradeoffs
- The experiments characterize which extensions transfer to constrained settings

**Limitations**: The study does not identify clearly superior extensions, limiting immediate practical recommendations. The evaluation is restricted to specific datasets (LLFF, synthetic Lego), and generalizability to other scenes is uncertain.

### Hung et al. (2025)

**Research question**: How can Neural Radiance Fields render novel views at arbitrary viewpoints and times from few-shot input views without per-scene optimization?

**Methodology**: The authors present TimeNeRF, combining multi-view stereo, neural radiance fields, and disentanglement strategies across diverse datasets to construct implicit content radiance fields that can be queried at any arbitrary time through volume rendering.

**Key findings**:
- TimeNeRF can render novel views in a few-shot setting without per-scene optimization
- The model excels at creating realistic novel views that transition smoothly across different times
- Captures intricate natural scene changes from dawn to dusk effectively
- The approach generalizes across diverse datasets without re-optimization
- Addresses the lack of dedicated datasets for temporal 3D scene modeling

**Limitations**: The approach requires diverse training datasets, and performance on scenes with dramatically different characteristics than training data is not thoroughly evaluated. The computational cost of temporal modeling compared to static NeRF is not quantified.

### Matta et al. (2024)

**Research question**: How can lens flare be removed from multi-view images by leveraging the view-dependent nature of flare artifacts within a Neural Radiance Fields framework?

**Methodology**: The authors propose GN-FR (Generalizable Neural Radiance Fields for Flare Removal), incorporating Flare-occupancy Mask Generation, View Sampler, and Point Sampler modules within the Generalizable NeRF Transformer framework, using a masking loss function for unsupervised learning.

**Key findings**:
- First work to address flare removal within a NeRF framework
- The approach generalizes across different scenes in an unsupervised manner
- Can render flare-free views from a sparse set of input images affected by lens flare
- A new 3D multi-view flare dataset was created with 17 scenes, 782 images, and 80 flare patterns
- The masking loss function effectively utilizes mask information without requiring paired flare-free data

**Limitations**: The approach requires multi-view input, limiting applicability to single-image scenarios. Performance on extremely severe flare or unusual flare patterns not represented in the training dataset is uncertain.

### Qazi et al. (2025)

**Research question**: How can Neural Radiance Fields be improved to generalize better across diverse scenes and conditions?

**Methodology**: The authors integrate a brain-inspired normalization technique called Neural Generalization (NeuGen) into leading NeRF architectures (MVSNeRF and GeoNeRF) to extract domain-invariant features and cultivate a comprehensive feature set.

**Key findings**:
- NeuGen seamlessly integrates into existing NeRF architectures without major modifications
- The approach shows improved performance on benchmarks across diverse datasets
- NeuGen surpasses existing models in generalizability across varied scenes
- Rendering quality is markedly improved compared to baseline NeRF models
- The work demonstrates potential of merging neuroscientific principles with deep learning frameworks

**Limitations**: The evaluation is limited to MVSNeRF and GeoNeRF architectures, and it is unclear how well NeuGen transfers to other NeRF variants. The abstract does not specify computational overhead or training time implications of the normalization technique.

### Wagner et al. (2025)

**Research question**: How can Neural Radiance Fields be adapted to obtain three-dimensional semantic representations from multi-date satellite images with pixel-wise semantic labels?

**Methodology**: The authors propose a satellite-specific NeRF model that derives 3D semantic representations from multi-date satellite images with corresponding pixel-wise semantic labels, enhancing color prediction by utilizing semantic information to address temporal inconsistencies.

**Key findings**:
- The approach demonstrates robustness in handling multi-date satellite imagery
- The model improves noisy input semantic labels through neural semantic field representation
- Semantic information effectively addresses temporal image inconsistencies caused by non-stationary categories such as vehicles
- A new dataset with manually generated labels for popular multi-view satellite images was created and released

**Limitations**: The approach requires pixel-wise semantic labels as input and is specifically designed for satellite imagery, which may limit applicability to other domains. The abstract does not address computational requirements or scalability to very large geographic areas.

### Xiao et al. (2025)

**Research question**: What are the key theoretical advancements, applications, and emerging challenges in Neural Radiance Fields for real-world deployment?

**Methodology**: The authors conduct a comprehensive survey compiling key theoretical advancements, alternative scene representations, emerging challenges, applications in reconstruction, impact on computer vision and robotics, and essential datasets and toolkits.

**Key findings**:
- NeRFs have significantly advanced 3D scene representation and reconstruction capabilities
- Multiple alternative scene representations have emerged to address specific limitations
- Key applications span scene understanding, 3D content generation, and robotics
- Essential datasets and toolkits have been developed to support the research community
- Significant gaps remain in real-world deployment capabilities

**Limitations**: As a survey paper, this work identifies gaps rather than addressing them directly. The rapidly evolving nature of the field means some recent developments may not be captured.

## References

Barreiro, A., Marí, R., Redondo, R., Haro, G., & Bosch, C. (2025). ShinyNeRF: Digitizing anisotropic appearance in Neural Radiance Fields. arXiv. https://arxiv.org/abs/2512.21692

Duan, R., & Wong, A. (2026). Evidential Neural Radiance Fields. arXiv. https://arxiv.org/abs/2602.23574

Gao, C., Wang, Y., Kim, C., Huang, J.-B., & Kopf, J. (2024). Planar Reflection-Aware Neural Radiance Fields. arXiv. https://arxiv.org/abs/2411.04984

Gu, S., Qiu, Y.-K., Tang, Y.-M., Wu, A., & Zheng, W.-S. (2025). MaintaAvatar: A maintainable avatar based on Neural Radiance Fields by continual learning. arXiv. https://arxiv.org/abs/2502.02372

Huang, A., Sonawane, P., Thorat, Y., & Rao, Y. (2026). Low-Cost Neural Radiance Fields. arXiv. https://arxiv.org/abs/2605.09312

Hung, H.-H., Do, H.-P., Li, Y.-H., & Huang, C.-C. (2025). TimeNeRF: Building generalizable Neural Radiance Fields across time from few-shot input views. arXiv. https://arxiv.org/abs/2507.13929

Matta, G. R., Siddartha, R., Girish, R. S. V., Sharma, S., & Mitra, K. (2024). GN-FR: Generalizable Neural Radiance Fields for flare removal. arXiv. https://arxiv.org/abs/2412.08200

Qazi, A., Basit, A., & Iqbal, A. (2025). NeuGen: Amplifying the 'Neural' in Neural Radiance Fields for domain generalization. arXiv. https://arxiv.org/abs/2505.06894

Wagner, V., Bullinger, S., Bodensteiner, C., & Arens, M. (2025). Semantic Neural Radiance Fields for multi-date satellite data. arXiv. https://arxiv.org/abs/2502.16992

Xiao, W., Chierchia, R., Santa Cruz, R., Li, X., Ahmedt-Aristizabal, D., Salvado, O., Fookes, C., & Lebrat, L. (2025). Neural Radiance Fields for the real world: A survey. arXiv. https://arxiv.org/abs/2501.13104
