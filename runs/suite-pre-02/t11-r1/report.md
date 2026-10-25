# Systematic Literature Review: Diffusion Models for Image Generation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "diffusion models", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on diffusion models for image generation reveals a field in rapid maturation, with research expanding beyond core generative capabilities toward efficiency, controllability, robustness, and practical deployment considerations. Recent work demonstrates significant advances in making diffusion models more efficient through architectural innovations like fixed-point solving and decentralized training, while simultaneously improving controllability through illumination control and multi-condition frameworks. The literature also shows growing attention to theoretical foundations, particularly in certified robustness, and expanding applications into specialized domains including medical imaging, computer graphics rendering, and 3D generation. Collectively, these papers indicate that diffusion models have transitioned from a novel generative approach to a versatile framework being optimized for real-world deployment across diverse application domains.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "diffusion models", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Scalability Improvements

A prominent research direction focuses on making diffusion models more computationally efficient and scalable. Fixed Point Diffusion Models (FPDM) introduce implicit fixed-point solving layers that significantly reduce model size and memory usage while accelerating training (Bai & Melas-Kyriazi, 2024). This approach reallocates computation across timesteps and reuses solutions between timesteps, achieving 87% fewer parameters and 60% less memory consumption compared to state-of-the-art DiT models. Complementing this, Decentralized Diffusion Models eliminate the need for centralized high-bandwidth networking by training expert models in isolation and ensembling them at inference time (McAllister et al., 2025). This framework enables training on distributed compute islands, demonstrating that high-quality 24-billion-parameter models can be trained with just eight GPU nodes in under a week. Additionally, pixel-space diffusion models have been investigated through latent-to-pixel strategies that acquire generative priors efficiently in latent space before transitioning to pixel space, achieving 3.18 to 4.75 times end-to-end inference speedups while matching or exceeding latent-space model quality (Jiang et al., 2026).

### Theme 2: Controllability and Conditional Generation

Multiple papers address the challenge of achieving precise control over diffusion model outputs. Controllable text-to-image generation has emerged as a critical area, with research revealing how novel conditions can be introduced into the denoising process through theoretical frameworks including novel score prediction and multi-condition generation (Cao et al., 2024). The literature organizes controllable generation into distinct categories: generation with specific conditions, multiple conditions, and universal controllable generation. More specialized work demonstrates illumination control through open-source pipelines that finetune diffusion models on supervised triplets of poorly-lit inputs, natural language instructions, and well-lit outputs (Anand et al., 2026). This approach achieves significant improvements in perceptual similarity, structural similarity, and identity preservation over baseline models without requiring heavy control inputs like depth maps. Video diffusion models extend these controllability concepts to temporal domains, with architectures designed to maintain temporal consistency across frames while supporting diverse input modalities including text, images, videos, and audio signals (Melnik et al., 2024).

### Theme 3: Theoretical Foundations and Robustness

Beyond practical improvements, recent work establishes theoretical foundations for diffusion models' properties. Diffusion classifiers have been proven to possess O(1) Lipschitzness and certified robustness against adversarial attacks (Chen et al., 2024). The Noised Diffusion Classifiers (NDCs) framework generalizes diffusion classifiers to handle Gaussian-corrupted data, achieving over 80% certified robustness on CIFAR-10 under ℓ₂ norm perturbations less than 0.25 using only off-the-shelf models without additional training data. This theoretical work addresses concerns about vulnerability to adversarial attacks and provides certifiable guarantees for diffusion-based systems. The alignment literature further examines how diffusion models can be aligned with human expectations and preferences, drawing inspiration from alignment techniques developed for large language models (Liu et al., 2024). This includes development of preference benchmarks and evaluation frameworks specifically designed for diffusion models.

### Theme 4: Specialized Applications and Domain Adaptation

The surveyed literature demonstrates diffusion models' versatility across specialized application domains. In medical imaging, label-efficient 3D brain segmentation leverages complementary 2D diffusion models with orthogonal views to achieve reliable segmentation with minimal annotated data (Cho et al., 2024). This approach outperforms state-of-the-art self-supervised methods while requiring training data from only one subject and as few as nine annotated slices. In computer graphics, diffusion models successfully denoise Monte Carlo renders containing heavy-tailed noise from specular and refractive objects (Vavilala et al., 2024). This conditioning-aware denoising approach is competitive with state-of-the-art methods across sampling rates while producing reconstructions with physically accurate shadow boundaries and specularities. The 3D generation survey establishes structured roadmaps connecting 3D representation choices to generation methodologies, categorizing approaches into feedforward, optimization-based, procedural, and novel view synthesis paradigms (Li et al., 2024).

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key points. Multiple papers emphasize that computational efficiency remains a primary bottleneck, with both Bai and Melas-Kyriazi (2024) and McAllister et al. (2025) independently developing approaches to reduce training infrastructure requirements. There is broad agreement that controllability is essential for practical deployment, as evidenced by parallel work on general controllable generation frameworks (Cao et al., 2024) and specialized illumination control (Anand et al., 2026). The literature also converges on the value of open-source reproducibility, with multiple papers explicitly releasing code, data, and model weights. Most papers acknowledge that the field's rapid evolution means current approaches will likely be superseded, indicating a mature understanding of the technology's trajectory.

**Disagreements**: The literature shows less direct disagreement than might be expected, partly because many papers address different problem formulations. However, there is an implicit tension between centralized versus decentralized training paradigms. While McAllister et al. (2025) demonstrate that decentralized training can outperform standard approaches FLOP-for-FLOP, other work on pixel-space models (Jiang et al., 2026) and fixed-point models (Bai & Melas-Kyriazi, 2024) assumes centralized training infrastructure. The optimal balance between distributed and centralized approaches remains unresolved. Additionally, while some papers focus on theoretical guarantees (Chen et al., 2024), others prioritize practical performance without formal guarantees, reflecting different research philosophies about what constitutes sufficient validation.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. First, evaluation standardization remains inconsistent — while Melnik et al. (2024) and Liu et al. (2024) call for better evaluation metrics, no unified benchmark suite emerges across papers. Second, most efficiency improvements focus on training costs rather than inference latency, despite inference being the primary cost for deployed applications. Third, the certified robustness work by Chen et al. (2024) is limited to CIFAR-10, leaving open whether theoretical guarantees scale to ImageNet-scale problems. Fourth, while several papers mention safety concerns about undesirable content generation (Cao et al., 2024; Liu et al., 2024), concrete mitigation techniques remain underdeveloped. Fifth, the medical imaging application by Cho et al. (2024) demonstrates promising label efficiency but requires validation across diverse anatomical structures and multi-institutional datasets before clinical adoption. Finally, the rapidly evolving nature of the field means survey papers risk quick obsolescence — several 2024 surveys already predate significant 2025-2026 advances, suggesting a need for living survey formats or more focused primary research.

## Per-Paper Annotations

### Anand et al. (2026)

**Research question**: How can we create a fully open-source and reproducible pipeline for learning illumination control in diffusion models without requiring heavy control inputs like depth maps?
**Methodology**: The authors build a data engine that transforms well-lit images into supervised training triplets consisting of a poorly-illuminated input image, a natural language lighting instruction, and a well-illuminated output image, then finetune a diffusion model on this data.
**Key findings**:
- The approach demonstrates significant improvements over baseline SD 1.5, SDXL, and FLUX.1-dev models in perceptual similarity, structural similarity, and identity preservation
- The pipeline is fully open-source and reproducible, built entirely with open-source tools and publicly available data
- Natural language lighting instructions enable effective illumination control without requiring depth maps or other heavy control inputs
**Limitations**: The work is built on SD 1.5 architecture which is relatively older; the abstract does not specify comparisons against the latest closed-source illumination control models or detail computational requirements.

### Bai and Melas-Kyriazi (2024)

**Research question**: Can fixed-point solving be integrated into diffusion models to reduce model size, memory usage, and training time while maintaining generation quality?
**Methodology**: The authors embed an implicit fixed-point solving layer into the denoising network, transforming the diffusion process into a sequence of closely-related fixed point problems, combined with a new stochastic training method that enables computation reallocation across timesteps and solution reuse between timesteps.
**Key findings**:
- FPDM contains 87% fewer parameters than state-of-the-art DiT models
- Training memory consumption is reduced by 60%
- The approach improves image generation quality when sampling computation or time is limited
- New techniques for reallocating computation across timesteps and reusing fixed point solutions significantly improve sampling efficiency
**Limitations**: Experiments focus on ImageNet, FFHQ, CelebA-HQ, and LSUN-Church datasets; the abstract does not address whether fixed-point approaches generalize to newer architectures beyond DiT or to conditional generation tasks.

### Cao et al. (2024)

**Research question**: How can precise control be achieved over text-to-image diffusion models to fulfill complex and diverse human needs beyond text-only conditioning?
**Methodology**: This survey undertakes a thorough review of controllable generation techniques, covering theoretical foundations including novel score prediction and multi-condition frameworks, alongside practical advancements organized by condition type.
**Key findings**:
- Achieving precise control over diffusion models is a critical challenge as generative capabilities advance
- Novel score prediction methods enable finer-grained control over the generation process
- Multi-condition frameworks allow integration of diverse control signals beyond text prompts
- Controllable generation techniques address both creative flexibility and safety concerns about undesirable content
**Limitations**: While comprehensive in reviewing existing methods, the survey notes that strong generative capabilities raise concerns about unsafe or undesirable content generation, and concept erasure techniques to mitigate these risks remain an active area of research with room for improvement.

### Chen et al. (2024)

**Research question**: Can diffusion classifiers be theoretically proven to have certified robustness against adversarial attacks, and can this robustness be tightened?
**Methodology**: The authors prove that diffusion classifiers possess O(1) Lipschitzness and establish their certified robustness, then generalize to Noised Diffusion Classifiers (NDCs) that classify Gaussian-corrupted data by deriving ELBOs, approximating likelihood, and calculating classification probabilities via Bayes' theorem.
**Key findings**:
- Diffusion classifiers possess O(1) Lipschitzness and have inherent resilience to adversarial attacks
- Noised Diffusion Classifiers achieve over 80% certified robustness on CIFAR-10 under ℓ₂ norm perturbations less than 0.25
- NDCs achieve over 70% certified robustness on CIFAR-10 under ℓ₂ norm perturbations less than 0.5
- The approach works with a single off-the-shelf diffusion model without requiring any additional training data
**Limitations**: Results are demonstrated primarily on CIFAR-10; the abstract does not address performance on larger-scale datasets like ImageNet or robustness against other attack types beyond ℓ₂ norm perturbations.

### Cho et al. (2024)

**Research question**: How can reliable 3D brain segmentation be achieved without requiring extensive labeled training data, which is challenging to acquire in clinical applications?
**Methodology**: The approach mines 2D features with semantic information from 2D diffusion models using orthogonal views as input, fuses them into 3D contextual feature representations, then trains multi-layer perceptrons to classify segmentation labels.
**Key findings**:
- The approach outperforms state-of-the-art self-supervised learning methods for brain subcortical structure segmentation
- Effective segmentation is achieved with training data from only one subject
- Promising results are obtained with minimal annotation requiring only nine slices and a labeled background region
- Complementary 2D diffusion models with orthogonal views effectively capture 3D contextual information
**Limitations**: Experiments focus on brain subcortical structure segmentation; the approach may need validation on other anatomical structures and larger multi-subject datasets to establish broader clinical applicability.

### Jiang et al. (2026)

**Research question**: What is a practical recipe for training pixel-space diffusion models that rival or exceed well-established latent-space counterparts?
**Methodology**: Through comprehensive empirical study, the authors develop a latent-to-pixel strategy that acquires generative priors efficiently in latent space and transitions to pixel space during post-training, systematically investigating weight initialization, data composition, prediction target, decoder architecture, and noise schedule.
**Key findings**:
- Direct large-scale pre-training in pixel space converges substantially more slowly than in latent space
- The latent-to-pixel strategy makes pixel-space models match or outperform latent-space counterparts
- The approach delivers 3.18 to 4.75 times end-to-end inference speedups
- Key design choices governing the transition include weight initialization, data composition, prediction target, decoder architecture, and noise schedule
**Limitations**: The study focuses on empirical findings without theoretical analysis of why the latent-to-pixel transition works; generalizability to architectures beyond those tested remains an open question.

### Li et al. (2024)

**Research question**: What are the fundamental methodologies for 3D generation and how can they be organized into a structured roadmap?
**Methodology**: This survey introduces fundamental methodologies of 3D generation methods and establishes a structured roadmap encompassing 3D representation, generation methods, datasets, and applications, while providing comprehensive overview of generation paradigms including feedforward, optimization-based, procedural generation, and generative novel view synthesis.
**Key findings**:
- 3D representations serve as the backbone for 3D generation, determining how objects are formatted and rendered
- Generation methods can be categorized by algorithmic paradigms: feedforward generation, optimization-based generation, procedural generation, and generative novel view synthesis
- Methods utilize various supervision signals including 2D supervision with rendering techniques to generate images
- The field encompasses diverse applications spanning computer graphics and computer vision domains
**Limitations**: The survey focuses on fundamental methodologies and may not cover all emerging techniques in the rapidly evolving 3D generation landscape. The comprehensive nature means some specialized or very recent approaches may not receive detailed treatment.

### Liu et al. (2024)

**Research question**: How can diffusion models be aligned with human expectations and preferences, and what are the current challenges and future directions in alignment research?
**Methodology**: This work reviews alignment of diffusion models, covering advancements in fundamentals of alignment, alignment techniques of diffusion models, preference benchmarks, and evaluation for diffusion models, drawing inspiration from alignment success in large language models.
**Key findings**:
- Diffusion models often misalign with human intentions and generate results with undesired properties or harmful content
- Alignment techniques from large language models can be adapted to diffusion models
- Preference benchmarks and evaluation frameworks specifically designed for diffusion models are emerging
- The field is in early stages compared to LLM alignment, with significant open challenges remaining
**Limitations**: As the first comprehensive review of diffusion model alignment, the work identifies many open problems but provides limited prescriptive solutions; the field requires substantial further research to mature.

### McAllister et al. (2025)

**Research question**: Can diffusion model training be distributed across independent clusters or datacenters without requiring centralized high-bandwidth networking infrastructure?
**Methodology**: The method trains a set of expert diffusion models over partitions of the dataset in full isolation from one another, then at inference time the experts ensemble through a lightweight router, collectively optimizing the same objective as a single model trained over the whole dataset.
**Key findings**:
- Decentralized diffusion models FLOP-for-FLOP outperform standard diffusion models on ImageNet and LAION Aesthetics
- The ensemble collectively optimizes the same objective as a single model trained over the whole dataset
- The approach scales to 24 billion parameters
- High-quality diffusion models can be trained with just eight individual GPU nodes in less than a week
**Limitations**: The router mechanism at inference time introduces additional complexity; the abstract does not address potential quality trade-offs compared to fully centralized training or communication overhead during the ensembling phase.

### Melnik et al. (2024)

**Research question**: What are the critical components, architectural designs, and temporal dynamics modeling approaches for diffusion models in video generation?
**Methodology**: This survey provides a comprehensive overview by consolidating recent research on video diffusion models, categorizing them based on applications, architectural choices, and temporal consistency mechanisms, while examining training and evaluation practices.
**Key findings**:
- Diffusion models have become powerful techniques for creating high-quality, coherent video content with impressive text-guided generative functions
- Architectural choices significantly impact temporal consistency, with various mechanisms proposed to maintain coherence across video frames
- Applications span multiple input modalities including text prompts, images, videos, and audio signals, each requiring different modeling approaches
- Current state-of-the-art faces challenges in generating longer videos and managing computational costs
**Limitations**: The survey acknowledges ongoing challenges in generating longer videos with consistent quality and the high computational costs associated with training and inference. Managing temporal dynamics over extended sequences remains an open problem.

### Vavilala et al. (2024)

**Research question**: Can diffusion models effectively denoise low-fidelity physically-based renderings containing Monte Carlo noise to enable faster rendering with fewer rays per pixel?
**Methodology**: The authors demonstrate that diffusion models can denoise low-fidelity renders, with the method conditioned on various natural render information to improve performance.
**Key findings**:
- Diffusion models successfully denoise low-fidelity physically-based renderings with Monte Carlo noise
- The method is competitive with state-of-the-art approaches across a range of sampling rates
- Conditioning on natural render information improves denoising performance
- The image prior applied by diffusion methods favors reconstructions resembling real images with straight shadow boundaries, curved specularities, and no fireflies
**Limitations**: The abstract does not specify computational costs of the diffusion denoising process itself or address performance on specific challenging render types beyond scenes with specular or refractive objects.

## References

Anand, N., Suri, M., Metzler, C., Manocha, D., & Duraiswami, R. (2026). Learning illumination control in diffusion models. arXiv. https://arxiv.org/abs/2604.24877

Bai, X., & Melas-Kyriazi, L. (2024). Fixed point diffusion models. arXiv. https://arxiv.org/abs/2401.08741

Cao, P., Zhou, F., Song, Q., & Yang, L. (2024). Controllable generation with text-to-image diffusion models: A survey. arXiv. https://arxiv.org/abs/2403.04279

Chen, H., Dong, Y., Shao, S., Hao, Z., Yang, X., Su, H., & Zhu, J. (2024). Your diffusion model is secretly a certifiably robust classifier. arXiv. https://arxiv.org/abs/2402.02316

Cho, J., Ahn, S., Kim, B., Bae, H., Liu, X., Xing, F., Lee, K., Elfakhri, G., Wedeen, V., Woo, J., & Park, J. (2024). Label-efficient 3D brain segmentation via complementary 2D diffusion models with orthogonal views. arXiv. https://arxiv.org/abs/2407.12329

Jiang, D., Du, R., Chen, Z., Liu, D., Wang, Z., Zheng, M., Yang, X., Cai, H., Hao, A., Jiang, Y., Gao, P., Yang, H., & Hoi, S. (2026). An empirical study of training pixel-space text-to-image diffusion models. arXiv. https://arxiv.org/abs/2608.16887

Li, X., Zhang, Q., Kang, D., Cheng, W., Gao, Y., Zhang, J., Liang, Z., Liao, J., Cao, Y.-P., & Shan, Y. (2024). Advances in 3D generation: A survey. arXiv. https://arxiv.org/abs/2401.17807

Liu, B., Shao, S., Li, B., Bai, L., Xu, Z., Xiong, H., Kwok, J., Helal, S., & Xie, Z. (2024). Alignment of diffusion models: Fundamentals, challenges, and future. arXiv. https://arxiv.org/abs/2409.07253

McAllister, D., Tancik, M., Song, J., & Kanazawa, A. (2025). Decentralized diffusion models. arXiv. https://arxiv.org/abs/2501.05450

Melnik, A., Ljubljanac, M., Lu, C., Yan, Q., Ren, W., & Ritter, H. (2024). Video diffusion models: A survey. arXiv. https://arxiv.org/abs/2405.03150

Vavilala, V., Vasanth, R., & Forsyth, D. (2024). Denoising Monte carlo renders with diffusion models. arXiv. https://arxiv.org/abs/2404.00491
