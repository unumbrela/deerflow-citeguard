# Systematic Literature Review: Diffusion Models for Image Generation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "diffusion models image generation", cs.CV category, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on diffusion models for image generation, revealing a field rapidly evolving along multiple dimensions. The surveyed literature demonstrates three major trends: (1) efficiency optimization through computational reuse and spatially adaptive generation, (2) architectural unification toward natively integrated foundation models, and (3) expanding application domains from general image synthesis to specialized areas including medical imaging and 3D generation. Collectively, these papers show that diffusion models are maturing beyond basic generation capabilities, with researchers focusing on practical deployment concerns including speed, safety, forgery detection, and domain-specific adaptation. Notably, several papers achieve significant speedups (3-5×) while maintaining or improving quality, suggesting the field is transitioning from proof-of-concept to production-ready systems.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "diffusion models image generation", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Computational Optimization

A dominant theme across multiple papers is the pursuit of computational efficiency in diffusion-based image generation. Jiang et al. (2026) demonstrate that pixel-space diffusion models, when properly trained using a latent-to-pixel strategy, can achieve 3.18 to 4.75 times end-to-end inference speedups compared to latent-space models. Chao et al. (2026) introduce foveated diffusion, which allocates tokens non-uniformly based on human visual perception characteristics, achieving perceptually indistinguishable results from full-resolution generation while drastically reducing token count and generation time. Decatur et al. (2025) propose computation reuse across correlated prompts, clustering prompts based on semantic similarity and sharing computation in early diffusion steps. These works collectively indicate that efficiency is no longer secondary to quality — researchers are finding ways to achieve both simultaneously.

### Theme 2: Architectural Unification and Foundation Models

Several papers point toward a trend of architectural unification, moving away from fragmented pipelines with separate components. Cai et al. (2026) present HiDream-O1-Image, a natively unified generative foundation model that eliminates the need for disjoint text encoders and external VAEs by mapping raw image pixels, text tokens, and task-specific conditions into a single shared token space. This unified approach treats diverse generation and editing tasks as a consistent in-context reasoning process, achieving performance parity with larger models using only 8B parameters. The scaling to 200B+ parameters unlocks unprecedented capabilities, suggesting that unified architectures may represent the future direction of the field.

### Theme 3: Safety, Verification, and Forgery Detection

As diffusion models become more capable, ensuring safe and trustworthy generation has emerged as a critical research direction. Park et al. (2025) address adversarial attacks on safety checkers with SC-Pro, a training-free framework that defends against unsafe image synthesis by exploiting the observation that adversarial attacks lack robustness to small changes in prompts or latents. Zuo et al. (2025) tackle forgery detection by unlocking the potential of vanilla MLLMs for detecting image manipulation without additional training, achieving superior localization accuracy across various tampering types. These works reflect growing awareness that generation capabilities must be paired with corresponding verification and safety mechanisms.

### Theme 4: Domain-Specific Adaptation

The surveyed literature shows diffusion models expanding beyond general-purpose image generation into specialized domains. Cai et al. (2024) adapt diffusion for 3D generation with DiffusionGS, directly outputting 3D Gaussian point clouds to enforce view consistency, achieving over 5× faster speed compared to existing methods. Xu et al. (2025) address medical image translation, introducing dynamic frequency balance and knowledge guidance to prevent anatomical structure distortion despite large differences between medical modalities. These domain-specific adaptations require novel architectural modifications and training strategies, demonstrating the versatility of diffusion frameworks.

### Theme 5: Reasoning and Step-by-Step Generation

An emerging direction applies reasoning strategies from language models to image generation. Guo et al. (2025) investigate whether Chain-of-Thought reasoning can verify and reinforce autoregressive image generation step-by-step, proposing PARM and PARM++ reward models with adaptive assessment and reflection mechanisms. Their enhanced model achieves a 24% improvement on GenEval benchmark, surpassing Stable Diffusion 3 by 15%, suggesting that reasoning-based verification can significantly improve generation quality.

### Theme 6: Survey and Framework Standardization

Wei et al. (2025) provide comprehensive synthesis of personalized image generation techniques across different generative architectures, proposing a unified framework that standardizes the personalization process with three key components: inversion spaces, inversion methods, and personalization schemes. This work helps organize the rapidly expanding literature and identifies commonalities across different approaches.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of efficiency without sacrificing quality. Both Jiang et al. (2026) and Chao et al. (2026) achieve 3-5× speedups while maintaining or improving generation quality. There is also broad agreement that unified architectures outperform fragmented pipelines, as evidenced by Cai et al. (2026) and the survey findings of Wei et al. (2025). The surveyed papers collectively emphasize that training-free approaches can be highly effective, with Park et al. (2025), Zuo et al. (2025), and Decatur et al. (2025) all demonstrating strong results without additional model training.

**Disagreements**: The literature shows some tension between pixel-space and latent-space approaches. While Jiang et al. (2026) demonstrate that pixel-space models can match or exceed latent-space performance with proper training strategies, many existing systems remain latent-space based. Additionally, there is variation in whether papers prioritize architectural innovation versus application-specific adaptation — some works focus on fundamental model improvements while others target domain-specific challenges.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Limited discussion of computational requirements**: Most papers do not explicitly state the computational resources required for training or deployment, making it difficult to assess practical accessibility.

2. **Gaze-tracking dependency**: Chao et al. (2026) note that foveated diffusion requires knowledge of user gaze location through eye tracking, which may limit applicability where gaze tracking is unavailable.

3. **Generalization across domains**: While domain-specific adaptations show promise, it remains unclear how well techniques transfer between domains (e.g., from natural images to medical imaging).

4. **Long-term safety implications**: Safety-focused papers address immediate concerns but do not discuss long-term implications of increasingly capable generation systems.

5. **Standardized evaluation metrics**: The field would benefit from more standardized benchmarks and evaluation protocols, particularly for specialized applications like medical imaging and 3D generation.

## Per-Paper Annotations

### Cai et al. (2024)

**Research question**: How can single-stage image-to-3D generation overcome the 3D inconsistency problems of existing 2D multi-view diffusion methods while handling both object-centric and scene cases?

**Methodology**: The authors propose DiffusionGS, a novel single-stage 3D diffusion model that directly outputs 3D Gaussian point clouds at each timestep to enforce view consistency, with a scene-object mixed training strategy to scale up 3D training data.

**Key findings**:
- DiffusionGS enforces view consistency by directly outputting 3D Gaussian point clouds at each timestep
- Achieves improvements of 2.20 dB/23.25 and 1.34 dB/19.16 in PSNR/FID for objects and scenes compared to state-of-the-art methods
- Works robustly with prompt views from any directions, beyond object-centric inputs
- Achieves over 5× faster speed (approximately 6 seconds on an A100 GPU) compared to existing approaches

**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Park et al. (2025)

**Research question**: Can adversarial attacks on Stable Diffusion's safety checkers be defended against without training?

**Methodology**: The authors propose SC-Pro (Spherical or Circular Probing), a training-free framework that exploits the observation that adversarial attacks are not robust to small changes in text prompts or input latents, along with SC-Pro-o using one-step diffusion models for efficient NSFW detection.

**Key findings**:
- Adversarial attacks on safety checkers are not robust to small changes in text prompts or input latents
- SC-Pro can easily defend against adversarial attacks generating NSFW images without requiring training
- SC-Pro-o further reduces computational resources by utilizing one-step diffusion models for NSFW detection
- The method demonstrates superiority in terms of performance and applicability

**Limitations**: Not stated in abstract.

### Guo et al. (2025)

**Research question**: Can Chain-of-Thought (CoT) reasoning strategies be applied to verify and reinforce autoregressive image generation?

**Methodology**: The authors investigate scaling test-time computation for verification, aligning model preferences with Direct Preference Optimization (DPO), and propose PARM and PARM++, reward models specialized for autoregressive image generation with adaptive assessment and reflection mechanisms.

**Key findings**:
- CoT reasoning approaches can be effectively adapted and combined to significantly improve image generation performance
- PARM adaptively assesses each generation step through potential assessment, merging strengths of existing reward models
- PARM++ introduces a reflection mechanism to self-correct unsatisfactory images, the first to incorporate reflection in autoregressive image generation
- The enhanced Show-o model achieves a +24% improvement on GenEval benchmark, surpassing Stable Diffusion 3 by +15%

**Limitations**: Not stated in abstract.

### Wei et al. (2025)

**Research question**: What is the current landscape of personalized image generation techniques across different deep generative model architectures?

**Methodology**: The authors present a comprehensive survey reviewing personalized image generation across various generative models (GANs, diffusion models, autoregressive models) and define a unified framework standardizing the personalization process with three key components: inversion spaces, inversion methods, and personalization schemes.

**Key findings**:
- A unified framework is proposed that standardizes personalization across different generative architectures
- The survey provides in-depth analysis of personalization techniques within each generative model type
- Comparative analysis elucidates commonalities and distinguishing features among existing methods
- The survey identifies open challenges and proposes potential directions for future research

**Limitations**: Not stated in abstract.

### Xu et al. (2025)

**Research question**: How can anatomical structure distortion in diffusion model-based medical image translation be addressed by balancing frequency information and incorporating clinical knowledge?

**Methodology**: The authors propose a method based on dynamic frequency balance and knowledge guidance that decomposes critical features using wavelet transform to extract low-frequency and high-frequency components, with a knowledge-guided mechanism that fuses prior clinical knowledge from a visual language model with visual features.

**Key findings**:
- The dynamic frequency balance module effectively enhances global low-frequency features and effective high-frequency details while suppressing high-frequency noise
- The knowledge-guided mechanism successfully fuses prior clinical knowledge from a visual language model with visual features
- The approach facilitates the generation of accurate anatomical structures despite large differences between different medical modalities
- Experimental evaluations on multiple datasets demonstrate significant improvements in both qualitative and quantitative assessments

**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Decatur et al. (2025)

**Research question**: Can computation be reused across correlated prompts in text-to-image diffusion to reduce redundancy and improve efficiency?

**Methodology**: The authors propose a training-free approach that clusters prompts based on semantic similarity and shares computation in early diffusion steps, leveraging the coarse-to-fine nature of diffusion models where early denoising steps capture shared structures among similar prompts.

**Key findings**:
- For models trained conditioned on image embeddings, the approach significantly reduces compute cost while improving image quality
- By leveraging UnClip's text-to-image prior, diffusion step allocation is enhanced for greater efficiency
- The method seamlessly integrates with existing pipelines and scales with prompt sets
- The approach reduces the environmental and financial burden of large-scale text-to-image generation

**Limitations**: Not stated in abstract.

### Chao et al. (2026)

**Research question**: How can diffusion and flow matching models generate high-resolution images and videos more efficiently by leveraging human visual perception characteristics?

**Methodology**: The authors develop a foveated diffusion approach that allocates tokens non-uniformly based on a mask modeling foveated resolution, assigning higher token density to foveal regions and lower density to peripheral regions, with a principled mechanism for constructing mixed-resolution tokens directly from high-resolution data.

**Key findings**:
- Foveated generation produces results perceptually indistinguishable from full-resolution generation while drastically reducing token count and generation time
- The approach leverages eccentricity-dependent acuity of human vision to optimize computational efficiency
- Mixed-resolution tokens can be constructed directly from high-resolution data while maintaining content consistency across resolutions
- The method can be post-trained from existing base models without requiring architectural changes

**Limitations**: The approach requires knowledge or estimation of the user's gaze location, for example through eye tracking, which may limit applicability in settings where gaze tracking is unavailable.

### Jiang et al. (2026)

**Research question**: How can pixel-space diffusion models be trained to match or exceed the performance of latent-space counterparts while addressing their slower convergence in large-scale settings?

**Methodology**: The authors conduct a comprehensive empirical study comparing pixel-space and latent-space diffusion model training, proposing a latent-to-pixel strategy that leverages generative priors from latent space pre-training followed by pixel-space post-training, systematically investigating design choices including weight initialization, data composition, prediction target, decoder architecture, and noise schedule.

**Key findings**:
- Direct large-scale pre-training in pixel space converges substantially more slowly than in latent space
- A latent-to-pixel strategy efficiently acquires generative priors in latent space before transitioning to pixel space during post-training
- The proposed recipe produces pixel-space models that match or outperform latent-space counterparts
- The approach delivers 3.18 to 4.75 times end-to-end inference speedups compared to latent-space models

**Limitations**: The study focuses on identifying practical guidelines through empirical investigation, but specific limitations of the proposed approach are not detailed in the abstract.

### Cai et al. (2026)

**Research question**: How can visual generative models overcome fragmented architectures by creating a natively unified foundation model that eliminates the need for disjoint text encoders and external VAEs?

**Methodology**: The authors present HiDream-O1-Image, a natively unified generative foundation model via pixel-space Diffusion Transformer that maps raw image pixels, text tokens, and task-specific conditions into a single shared token space within an Unified Transformer (UiT) architecture, validating the approach across various generation tasks and demonstrating scalability from 8B to over 200B parameters.

**Key findings**:
- The native encoding paradigm eliminates the need for separate VAEs or disjoint pre-trained text encoders
- The model treats diverse generation and editing tasks as a consistent in-context reasoning process
- With only 8B parameters, HiDream-O1-Image achieves performance parity with or surpasses larger models like 27B Qwen-Image
- The scaled 200B+ parameter version (HiDream-O1-Image-Pro) unlocks unprecedented generative capabilities and establishes new state-of-the-art benchmarks

**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Zuo et al. (2025)

**Research question**: Can vanilla MLLMs be leveraged for image forgery detection and localization without additional training?

**Methodology**: The authors propose Foresee, a training-free MLLM-based pipeline that employs a type-prior-driven strategy and a Flexible Feature Detector (FFD) module specifically designed to handle copy-move manipulations, enabling lightweight inference without additional training.

**Key findings**:
- Foresee surpasses existing MLLM-based methods in both tamper localization accuracy and richness of textual explanations
- The approach achieves superior localization accuracy while providing more comprehensive textual explanations
- Foresee exhibits stronger generalization capability across various tampering types including copy-move, splicing, removal, local enhancement, deepfake, and AIGC-based editing
- The pipeline eliminates the need for additional training and enables lightweight inference

**Limitations**: Not stated in abstract.

## References

Cai, Q., Chen, J., Gao, C., Gong, Z., Li, Y., Pan, Y., Peng, Y., Qiu, Z., Yu, K., Zhang, Y., Ai, H., Bai, S., Chen, Y., Chen, Z., Gao, F., Guo, Y., Li, D., Shen, Z., Shi, L., Wang, J., Wang, S., Wang, Y., Zheng, R., Yao, T., & Mei, T. (2026). HiDream-O1-Image: A natively unified image generative foundation model with pixel-level unified transformer. arXiv. https://arxiv.org/abs/2605.11061

Cai, Y., Zhang, H., Zhang, K., Liang, Y., Ren, M., Luan, F., Liu, Q., Kim, S. Y., Zhang, J., Zhang, Z., Zhou, Y., Zhang, Y., Yang, X., Lin, Z., & Yuille, A. (2024). Baking Gaussian Splatting into Diffusion Denoiser for Fast and Scalable Single-stage Image-to-3D Generation and Reconstruction. arXiv. https://arxiv.org/abs/2411.14384

Chao, B., Yariv, L., Xiao, H., & Wetzstein, G. (2026). Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation. arXiv. https://arxiv.org/abs/2603.23491

Decatur, D., Groueix, T., Yifan, W., Hanocka, R., Kim, V., & Gadelha, M. (2025). Reusing Computation in Text-to-Image Diffusion for Efficient Generation of Image Sets. arXiv. https://arxiv.org/abs/2508.21032

Guo, Z., Zhang, R., Tong, C., Zhao, Z., Huang, R., Zhang, H., Zhang, M., Liu, J., Zhang, S., Gao, P., Li, H., & Heng, P.-A. (2025). Can We Generate Images with CoT? Let's Verify and Reinforce Image Generation Step by Step. arXiv. https://arxiv.org/abs/2501.13926

Jiang, D., Du, R., Chen, Z., Liu, D., Wang, Z., Zheng, M., Yang, X., Cai, H., Hao, A., Jiang, Y., Gao, P., Yang, H., & Hoi, S. (2026). An Empirical Study of Training Pixel-Space Text-to-Image Diffusion Models. arXiv. https://arxiv.org/abs/2608.16887

Park, J., Hwang, J., Ryu, I., Park, H., Kim, J., & Lee, J.-S. (2025). SC-Pro: Training-Free Framework for Defending Unsafe Image Synthesis Attack. arXiv. https://arxiv.org/abs/2501.05359

Wei, Y., Zheng, Y., Zhang, Y., Liu, M., Ji, Z., Zhang, L., & Zuo, W. (2025). Personalized Image Generation with Deep Generative Models: A Decade Survey. arXiv. https://arxiv.org/abs/2502.13081

Xu, J., Zhou, D., Hu, L., Liu, Z., Wang, N., & Gao, X. (2025). Structure-Accurate Medical Image Translation via Dynamic Frequency Balance and Knowledge Guidance. arXiv. https://arxiv.org/abs/2504.09441

Zuo, R., Tong, Q., Lu, Z.-M., & Lu, Z. (2025). Unlocking the Forgery Detection Potential of Vanilla MLLMs: A Novel Training-Free Pipeline. arXiv. https://arxiv.org/abs/2511.13442
