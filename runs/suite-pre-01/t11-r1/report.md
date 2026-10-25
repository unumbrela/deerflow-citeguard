# Systematic Literature Review: Diffusion Models for Image Generation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "diffusion models" query, cs.CV category, 2024-2026
**Citation format**: APA 7th edition

## Executive Summary

The literature on diffusion models for image generation from 2024-2026 reveals a field rapidly maturing beyond foundational generative capabilities toward practical deployment considerations. The surveyed papers collectively demonstrate three major shifts: (1) from latent-space to pixel-space generation for improved inference efficiency, (2) from monolithic training to decentralized and parameter-efficient architectures, and (3) from pure generation toward controllable, aligned, and robust systems. Survey papers dominate the early 2024 landscape, indicating field consolidation, while 2025-2026 papers focus on efficiency, control, and real-world applicability. Key convergences include consensus on the need for better computational efficiency, improved controllability beyond text prompts, and theoretical understanding of robustness properties. The literature remains fragmented on standardization of evaluation metrics and lacks extensive cross-domain transfer studies.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "diffusion models", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review focuses on cs.CV category, potentially missing relevant work from cs.LG or other categories.

## Themes

### Theme 1: Efficiency and Scalability Improvements

A dominant theme across multiple papers is the push toward more efficient diffusion model training and inference. Fixed Point Diffusion Models (Bai & Melas-Kyriazi, 2024) introduced implicit fixed point solving layers that reduced parameters by 87% and memory consumption by 60% while maintaining generation quality. Similarly, pixel-space diffusion research (Jiang et al., 2026) demonstrated that latent-to-pixel training strategies can achieve 3.18-4.75× inference speedups compared to traditional latent-space approaches. The decentralized diffusion framework (McAllister et al., 2025) addressed computational infrastructure constraints by enabling training across independent GPU clusters, successfully scaling to 24 billion parameters using only eight individual GPU nodes in under a week. These works collectively reflect the field's transition from proving generative capabilities to making diffusion models practically deployable at scale.

### Theme 2: Controllability and Conditional Generation

Multiple papers address the limitation of text-only conditioning in diffusion models. Cao et al. (2024) surveyed controllable text-to-image generation, categorizing approaches into specific conditions (spatial layouts, poses, edges), multiple simultaneous conditions, and universal control mechanisms. Their analysis reveals that introducing novel conditions into the denoising process requires careful theoretical grounding in how conditioning signals interact with the reverse diffusion trajectory. Anand et al. (2026) demonstrated illumination control through natural language instructions, achieving superior perceptual and structural similarity compared to baseline models requiring depth maps. The video diffusion survey (Melnik et al., 2024) extended controllability to temporal domains, emphasizing temporal consistency as a critical challenge when conditioning on multi-modal inputs spanning text, images, video, and audio. These works indicate a clear trajectory from unconditional or text-conditioned generation toward fine-grained, multi-modal control.

### Theme 3: Alignment and Safety

As diffusion models achieve high generative quality, alignment with human preferences and safety considerations have emerged as critical research directions. Liu et al. (2024) provided the first comprehensive review of diffusion model alignment, covering techniques adapted from large language model alignment research including reinforcement learning from human feedback (RLHF), direct preference optimization, and reward modeling. Their survey identified preference benchmarks and evaluation frameworks as essential but underdeveloped components. The alignment challenge extends beyond explicit human preferences to implicit robustness properties: Chen et al. (2024) proved that diffusion classifiers possess O(1) Lipschitzness, providing certified robustness guarantees against adversarial perturbations without additional training data. This theoretical foundation establishes diffusion models as inherently robust classifiers, achieving over 80% certified robustness on CIFAR-10 under ℓ₂ norm < 0.25 perturbations. Together, these papers indicate growing recognition that generative capability alone is insufficient—models must be aligned, safe, and robust for real-world deployment.

### Theme 4: Domain-Specific Applications

Several papers demonstrate diffusion models adapted to specialized domains beyond general image generation. Cho et al. (2024) addressed label scarcity in medical imaging by extracting 2D semantic features from diffusion models via orthogonal views, then fusing them into 3D representations for brain segmentation. Their approach achieved superior performance to self-supervised learning baselines using training data from only one subject, with promising results from sparse labeling of just nine slices. Vavilala et al. (2024) applied diffusion models to denoise Monte Carlo renders in physically-based rendering, conditioning on natural render information to eliminate fireflies and produce straight shadow boundaries while remaining competitive with state-of-the-art denoising methods across sampling rates. These domain-specific adaptations reveal diffusion models' flexibility but also highlight the need for specialized conditioning mechanisms and evaluation metrics tailored to application requirements.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of efficiency improvements. Bai and Melas-Kyriazi (2024), Jiang et al. (2026), and McAllister et al. (2025) all demonstrate that architectural innovations can substantially reduce computational costs without sacrificing quality. There is also broad agreement that text-only conditioning is insufficient for practical applications, with Cao et al. (2024), Anand et al. (2026), and Melnik et al. (2024) all proposing extended conditioning mechanisms. Finally, the surveyed papers collectively acknowledge that theoretical understanding lags behind empirical capabilities, motivating work on certified robustness (Chen et al., 2024) and alignment frameworks (Liu et al., 2024).

**Disagreements**: The literature shows tension between centralized versus decentralized training paradigms. McAllister et al. (2025) advocate for decentralized training across independent compute islands, arguing it reduces infrastructure costs and improves fault tolerance. However, this approach introduces coordination overhead and potential quality degradation from dataset partitioning that other works do not address. Similarly, there is divergence on pixel-space versus latent-space generation: Jiang et al. (2026) demonstrate pixel-space advantages for inference speed, while the broader literature has predominantly favored latent-space approaches for training stability. The optimal balance between these paradigms remains unresolved.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, evaluation metrics remain inconsistent across papers—some use FID and IS, others use perceptual similarity or task-specific metrics, making cross-paper comparison difficult. Second, while efficiency improvements are demonstrated individually, no paper provides comprehensive analysis of trade-offs between parameter reduction, memory savings, inference speed, and generation quality across multiple baselines. Third, domain-specific adaptations (medical imaging, rendering) lack systematic study of transfer learning: can models pre-trained on natural images be efficiently adapted to specialized domains, or is domain-specific pre-training necessary? Fourth, alignment research (Liu et al., 2024) identifies the need for preference benchmarks but does not provide standardized datasets or evaluation protocols. Finally, several papers acknowledge limitations in dataset diversity and scale—Cho et al. (2024) evaluated on single-subject data, Chen et al. (2024) on CIFAR-10 only, and Anand et al. (2026) on limited lighting conditions—raising questions about generalization to broader distributions.

## Per-Paper Annotations

### Anand et al. (2026)

**Research question**: How can open-source diffusion models achieve illumination control without requiring heavy control inputs like depth maps?
**Methodology**: Built a data engine that transforms well-lit images into supervised training triplets (poorly-illuminated input, natural language lighting instruction, well-illuminated output), then finetuned a diffusion model on this data.
**Key findings**:
- Significant improvements over baseline SD 1.5, SDXL, and FLUX.1-dev models in perceptual similarity, structural similarity, and identity preservation
- Provides a fully reproducible solution built entirely with open-source tools and publicly available data
- Natural language lighting instructions enable flexible illumination control without depth maps
- All code, data, and model weights released publicly for community use
**Limitations**: Built on older SD 1.5 architecture which may limit performance compared to newer models; generalization to diverse lighting conditions and scenes not fully evaluated.

### Bai and Melas-Kyriazi (2024)

**Research question**: Can fixed point solving be integrated into diffusion models to reduce parameter count and improve sampling efficiency?
**Methodology**: Embedded implicit fixed point solving layers into the denoising network, transforming the diffusion process into sequences of closely-related fixed point problems with stochastic training and computation reallocation across timesteps.
**Key findings**:
- FPDM contains 87% fewer parameters than state-of-the-art DiT model
- Consumes 60% less memory during training
- Improves image generation quality when sampling computation or time is limited
- Enables computation reallocation across timesteps and solution reuse between timesteps
- Validated on ImageNet, FFHQ, CelebA-HQ, and LSUN-Church datasets
**Limitations**: Performance gains primarily observed in computation-constrained sampling regimes; benefits in unlimited computation settings less pronounced.

### Cao et al. (2024)

**Research question**: How can pre-trained text-to-image diffusion models be extended to support novel conditioning mechanisms beyond text prompts?
**Methodology**: Conducted comprehensive survey analyzing theoretical foundations of conditioning in diffusion models, categorizing approaches by condition type and analyzing how novel conditions are introduced into the denoising process.
**Key findings**:
- Identified three categories: specific conditions (spatial, pose, edge), multiple simultaneous conditions, and universal control mechanisms
- Theoretical analysis reveals conditioning mechanisms must preserve the reverse diffusion trajectory structure
- Curated repository of controllable generation literature maintained at https://github.com/PRIV-Creation/Awesome-Controllable-T2I-Diffusion-Models
- Control mechanisms range from attention modulation to gradient-based guidance to fine-tuning approaches
**Limitations**: Survey focuses on theoretical analysis; empirical comparison of control mechanisms across unified benchmark lacking.

### Chen et al. (2024)

**Research question**: What is the theoretical basis for diffusion classifiers' robustness to adversarial attacks, and can certified robustness guarantees be established?
**Methodology**: Proved diffusion classifiers possess O(1) Lipschitzness and established certified robustness; generalized to Noised Diffusion Classifiers (NDCs) that classify Gaussian-corrupted data using ELBOs and Bayes' theorem for tighter certificates.
**Key findings**:
- Achieved over 80% certified robustness on CIFAR-10 under ℓ₂ norm < 0.25 adversarial perturbations
- Achieved over 70% certified robustness on CIFAR-10 under ℓ₂ norm < 0.5 adversarial perturbations
- Accomplished using single off-the-shelf diffusion model without additional training data
- NDCs obtain much tighter certified robustness through non-constant Lipschitzness
- Provides theoretical foundation explaining diffusion classifiers' inherent resilience to adversarial attacks
**Limitations**: Experimental validation limited to CIFAR-10 dataset; certified robustness on larger-scale datasets and different attack norms not demonstrated.

### Cho et al. (2024)

**Research question**: How can reliable 3D brain segmentation be achieved when extensive labeled training data is unavailable in clinical applications?
**Methodology**: Extract 2D semantic features from 2D diffusion models using orthogonal views as input, fuse them into 3D contextual feature representations, then train multi-layer perceptrons for segmentation label classification.
**Key findings**:
- Outperforms state-of-the-art self-supervised learning methods for brain subcortical structure segmentation
- Achieves reliable segmentation quality with training data from only one subject
- Promising results obtained with sparse labeling of just nine slices plus labeled background region
- Complementary orthogonal views effectively capture 3D contextual information from 2D diffusion models
- Significantly reduces annotation burden for clinical brain segmentation applications
**Limitations**: Evaluated on limited dataset with one subject for main experiments; generalization to diverse brain pathologies and anatomical variations requires further validation.

### Jiang et al. (2026)

**Research question**: What is a practical recipe for training pixel-space diffusion models that rival or exceed latent-space counterparts in quality and efficiency?
**Methodology**: Conducted comprehensive empirical study comparing direct pixel-space pre-training versus latent-to-pixel strategy, systematically investigating weight initialization, data composition, prediction target, decoder architecture, and noise schedule design choices.
**Key findings**:
- Direct large-scale pixel-space pre-training converges substantially slower than latent-space
- Latent-to-pixel strategy acquires generative priors efficiently in latent space then transitions to pixel space during post-training
- Identified practical recipe enables pixel-space models to match or outperform latent-space counterparts
- Achieves 3.18 to 4.75 times end-to-end inference speedups compared to latent-space models
- Key design choices include weight initialization from latent model, hybrid data composition, and modified noise schedule
**Limitations**: Empirical findings may not generalize to all model architectures; comprehensive ablation across all design choice combinations computationally prohibitive.

### Liu et al. (2024)

**Research question**: What are the fundamentals, techniques, benchmarks, and future directions for aligning diffusion models with human preferences and intentions?
**Methodology**: Conducted comprehensive review covering alignment fundamentals, technique taxonomy, preference benchmarks, and evaluation methods, drawing parallels to LLM alignment research while identifying diffusion-specific challenges.
**Key findings**:
- First comprehensive review paper on diffusion model alignment
- Identified alignment techniques including reward modeling, reinforcement learning, and direct preference optimization
- Surveyed existing preference benchmarks and evaluation frameworks
- Highlighted key challenges including reward hacking, distribution shift, and multi-objective optimization
- Proposed future directions including scalable oversight, value learning, and multi-modal alignment
**Limitations**: Review identifies need for standardized benchmarks but does not provide them; empirical comparison of alignment techniques across unified framework lacking.

### McAllister et al. (2025)

**Research question**: How can diffusion model training be distributed across independent clusters without requiring centralized high-bandwidth networking infrastructure?
**Methodology**: Train expert diffusion models on dataset partitions in complete isolation from each other, then ensemble the experts through a lightweight router at inference time to collectively optimize the same objective as a single model.
**Key findings**:
- Decentralized diffusion models FLOP-for-FLOP outperform standard diffusion models on ImageNet and LAION Aesthetics
- Successfully scaled to 24 billion parameters using just eight individual GPU nodes
- High-quality diffusion models can be trained in less than a week with decentralized approach
- Enables use of on-demand GPU nodes instead of centralized clusters, reducing infrastructure costs
- Improves resilience to localized GPU failures through compute island architecture
**Limitations**: Requires coordination across multiple independent compute clusters; ensemble inference through router may introduce additional latency; optimal partitioning strategies for different datasets not fully explored.

### Melnik et al. (2024)

**Research question**: What are the critical components, architectural designs, and temporal dynamics modeling approaches for diffusion models in video generation?
**Methodology**: Conducted comprehensive survey covering core principles, mathematical formulations, architectural choices, temporal consistency methods, application taxonomy by input modality, and training/evaluation practices.
**Key findings**:
- Identified key architectural components including temporal attention, 3D convolutions, and cascade approaches
- Categorized applications by input modality: text-to-video, image-to-video, video-to-video, and audio-to-video
- Surveyed temporal consistency methods including optical flow constraints and latent space interpolation
- Reviewed diverse video and image datasets used for training and evaluation
- Identified ongoing challenges including long video generation and computational cost management
- Curated repository at https://github.com/ndrwmlnk/Awesome-Video-Diffusion-Models
**Limitations**: Survey focuses on video generation; image generation advances not covered in depth.

### Vavilala et al. (2024)

**Research question**: Can diffusion models effectively denoise low-fidelity Monte Carlo renders to reduce computational costs in physically-based rendering?
**Methodology**: Applied diffusion models conditioned on natural render information to denoise physically-based renderings with Monte Carlo noise, leveraging the image prior learned by diffusion models.
**Key findings**:
- Diffusion models successfully denoise low-fidelity Monte Carlo renders
- Method is competitive with state-of-the-art denoising approaches across a range of sampling rates
- Conditioning on natural render information improves denoising performance
- Produces straight shadow boundaries, curved specularities, and eliminates fireflies
- Diffusion image prior strongly favors reconstructions resembling real images rather than artifacts
**Limitations**: Image prior bias toward real-image appearance may not suit all rendering scenarios; performance on scenes with extreme specular or refractive objects with heavy-tailed noise distributions needs further study.

## References

Anand, N., Suri, M., Metzler, C., Manocha, D., & Duraiswami, R. (2026). Learning illumination control in diffusion models. arXiv. https://arxiv.org/abs/2604.24877

Bai, X., & Melas-Kyriazi, L. (2024). Fixed point diffusion models. arXiv. https://arxiv.org/abs/2401.08741

Cao, P., Zhou, F., Song, Q., & Yang, L. (2024). Controllable generation with text-to-image diffusion models: A survey. arXiv. https://arxiv.org/abs/2403.04279

Chen, H., Dong, Y., Shao, S., Hao, Z., Yang, X., Su, H., & Zhu, J. (2024). Your diffusion model is secretly a certifiably robust classifier. arXiv. https://arxiv.org/abs/2402.02316

Cho, J., Ahn, S., Kim, B., Bae, H., Liu, X., Xing, F., Lee, K., Elfakhri, G., Wedeen, V., Woo, J., & Park, J. (2024). Label-efficient 3D brain segmentation via complementary 2D diffusion models with orthogonal views. arXiv. https://arxiv.org/abs/2407.12329

Jiang, D., Du, R., Chen, Z., Liu, D., Wang, Z., Zheng, M., Yang, X., Cai, H., Hao, A., Jiang, Y., Gao, P., Yang, H., & Hoi, S. (2026). An empirical study of training pixel-space text-to-image diffusion models. arXiv. https://arxiv.org/abs/2608.16887

Liu, B., Shao, S., Li, B., Bai, L., Xu, Z., Xiong, H., Kwok, J., Helal, S., & Xie, Z. (2024). Alignment of diffusion models: Fundamentals, challenges, and future. arXiv. https://arxiv.org/abs/2409.07253

McAllister, D., Tancik, M., Song, J., & Kanazawa, A. (2025). Decentralized diffusion models. arXiv. https://arxiv.org/abs/2501.05450

Melnik, A., Ljubljanac, M., Lu, C., Yan, Q., Ren, W., & Ritter, H. (2024). Video diffusion models: A survey. arXiv. https://arxiv.org/abs/2405.03150

Vavilala, V., Vasanth, R., & Forsyth, D. (2024). Denoising Monte Carlo renders with diffusion models. arXiv. https://arxiv.org/abs/2404.00491
