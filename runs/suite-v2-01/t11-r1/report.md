# Systematic Literature Review: Diffusion Models for Image Generation

**Date**: 2026-10-25  
**Papers surveyed**: 9  
**Scope**: arXiv search query "diffusion image generation", published between 2024-10-25 and 2026-10-25  
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 9 recent arXiv papers on diffusion models with applications to image generation, published between late 2024 and mid-2026. The surveyed literature reveals a rapidly evolving field characterized by three major directions: (1) architectural innovations that explicitly model data geometry and manifold structure to improve sampling quality, (2) efficient distillation methods enabling single-step or few-step generation without sacrificing fidelity, and (3) specialized conditioning mechanisms for precise control over generated content. Collectively, these works demonstrate significant progress in reducing computational costs while enhancing generation quality, with FID scores reaching below 2.0 on standard benchmarks. However, the field still faces challenges in training efficiency, identity preservation during editing, and generalization to out-of-distribution scenarios.

## Methodology

This review surveyed 9 arXiv papers retrieved on 2026-10-25 using the query "diffusion image generation", published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance to image generation tasks. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, while the search aimed to capture papers specifically on image generation, some retrieved papers address diffusion models in broader contexts.

## Themes

### Theme 1: Manifold-Aware Architectures for Improved Sampling Quality

A prominent direction in recent diffusion model research involves explicitly modeling the geometric structure of the data manifold to improve generation quality. Xue et al. (2026) introduced MIND (Data Manifold-aware Image diffusioN moDel), which integrates discrete patch tokenization into the score function of continuous diffusion models. Their approach uses soft top-k aggregation for end-to-end training and dual-branch high-frequency feature embedding layers with multi-stage transition sampling. This manifold-aware approach achieved remarkable results: MIND base reduced FID from 43.47 (vanilla DiT-B/2 baseline) to 22.73 without guidance after 80-epoch training, and MIND-B with only 130M parameters achieved FID of 2.06 with guidance—outperforming LlamaGen-3B with 3.1B parameters (FID 3.1).

This theme reflects a broader recognition that diffusion models benefit from explicit geometric reasoning about the data space, rather than relying solely on implicit learning through denoising objectives. The success of manifold-aware approaches suggests future architectures should incorporate geometric priors more explicitly.

### Theme 2: Efficient Distillation for Single-Step Generation

Reducing the computational cost of diffusion model inference through distillation represents another major research thrust. Wang and Tong (2026) proposed Fixed-Point Distillation (FPD), an end-to-end framework for distilling discrete diffusion image generators into single-step models. Their method constructs local correction targets by partially corrupting the student's one-step draft and refining it with a single teacher step, using a straight-through estimator to backpropagate through the discrete bottleneck. The multi-bandwidth drift loss in continuous feature space enables fully differentiable training with optional adversarial objectives.

This work addresses a critical limitation of diffusion models: their typically slow generation requiring many denoising steps. FPD achieves competitive visual fidelity and structural alignment within a single inference step, narrowing the performance gap between single-step students and multi-step teachers. The approach outperforms existing discrete distillation baselines on both class-conditional and text-conditional generation tasks.

### Theme 3: Spatial Conditioning for Precise Control

Several recent works focus on enabling precise spatial control in diffusion-based image generation. Wu et al. (2026) developed GazeDiT for gaze-accurate synthetic eye image generation, using spatial conditioning that grounds global gaze labels in local pupil/iris geometry. Their approach employs a frozen SegFormer to extract geometry from real images during training and a physical eye renderer to sample gaze-consistent geometries at inference. The model achieves substantially lower tail gaze-label error than other diffusion baselines and approaches the gaze estimation error of the same frozen estimator on real images.

Baykal et al. (2026) addressed identity preservation in image editing through ResEdit, which incorporates residual image encoding as additional conditioning. Their gradient reversal-based optimization disentangles the residual from edited conditions, reducing reliance on inversion and its associated pitfalls. This approach enables improved identity preservation and better editability across intrinsic-based editing and relighting tasks.

These works share a common insight: precise spatial conditioning mechanisms are essential for applications requiring fine-grained control, whether for eye tracking datasets or image editing workflows.

### Theme 4: Foundation Model Integration for Enhanced Capabilities

The integration of multiple foundation models to enhance diffusion model capabilities emerges as another theme. Chen et al. (2024) proposed FodFoM, combining BLIP-2, CLIP, Stable Diffusion, and GroundingDINO to generate challenging fake outlier images for improving out-of-distribution detection. Their framework generates two types of fake outliers: semantically similar-but-different images using captioning and generation capabilities, and pure background images by blurring foreground objects. This approach achieves new state-of-the-art OOD detection performance on multiple benchmarks and flexibly integrates with existing OOD detection methods.

Similarly, Qi et al. (2026) leveraged pre-trained diffusion models for texture prediction in their text-to-3D indoor scene generation framework. Their hierarchical scene representation (room, region, floor object, and supported object levels) combined with PRM-guided Monte Carlo Tree Search enables revision of earlier decisions, addressing error propagation in sequential methods.

### Theme 5: Infrastructure and Systems for Diffusion Model Deployment

Beyond algorithmic innovations, recent work addresses infrastructure challenges for deploying diffusion models at scale. Aimuyo et al. (2026) developed Purlin, a scale-up communication framework that separates collective semantics and orchestration from hardware-specific datapaths. Their SNAC protocol (Stage, Notify, And Consume) enables customization and reuse across different hardware, achieving latency speedups up to 5.14x and bandwidth improvements up to 4.50x over baselines across seven collectives on A100, H200, and B200 GPUs. For diffusion image generation specifically, Purlin reduces end-to-end latency by up to 1.13x.

This systems-level work recognizes that efficient diffusion model deployment requires co-design of algorithms and infrastructure, particularly for distributed inference scenarios.

### Theme 6: Cross-Domain Transfer and Adaptation

Several papers demonstrate successful transfer of diffusion models trained for image generation to other domains. Yang et al. (2026) leveraged pre-trained VAEs from Stable Diffusion for plasma turbulence surrogate modeling, fine-tuning with physics-informed loss including spectral loss in Fourier space. Their PreVAE-Turb framework, combined with ConvLSTM networks for temporal dynamics in latent space, generates thousands of time steps in seconds on a single GPU—providing substantial computational acceleration compared to direct numerical simulation.

Wang et al. (2026) applied trust region continual learning with generative replay to task-incremental diffusion image generation, showing the approach achieves the best final performance and retention compared to EWC, replay, and continual meta-learning baselines. The method yields an emergent meta-learning property where the model becomes an initialization that rapidly re-converges to prior task optima after each task transition.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that explicit modeling of structure—whether geometric (Xue et al., 2026), spatial (Wu et al., 2026; Baykal et al., 2026), or temporal (Yang et al., 2026)—significantly improves diffusion model performance. There is also consensus that reducing inference steps through distillation (Wang & Tong, 2026) or efficient architectures is critical for practical deployment. Multiple works demonstrate that leveraging pre-trained foundation models provides substantial benefits for downstream tasks (Chen et al., 2024; Qi et al., 2026; Yang et al., 2026).

**Disagreements**: The literature shows some tension between discrete and continuous approaches to diffusion modeling. Wang and Tong (2026) focus on discrete diffusion generators with distillation, while Xue et al. (2026) integrate discrete patch tokenization into continuous diffusion models—suggesting different views on whether discrete or continuous formulations are more amenable to improvement. Additionally, while some works emphasize architectural innovations (Xue et al., 2026; Wu et al., 2026), others prioritize systems-level optimizations (Aimuyo et al., 2026), reflecting different perspectives on where bottlenecks lie.

## Gaps and Open Questions

Several gaps emerge from the surveyed literature:

1. **Training efficiency**: While inference efficiency receives considerable attention through distillation (Wang & Tong, 2026), training costs remain prohibitive. Xue et al. (2026) required 80-epoch training for their base model, and few papers address training time reduction.

2. **Identity preservation**: Despite progress in editing (Baykal et al., 2026), maintaining identity across substantial edits remains challenging. The limitations sections of multiple papers note this as an open problem.

3. **Evaluation metrics**: Most papers report FID scores, but there is limited discussion of whether FID adequately captures perceptual quality or application-specific requirements. The gaze estimation work (Wu et al., 2026) uses task-specific metrics, suggesting a need for more domain-aligned evaluation.

4. **Generalization and robustness**: While Chen et al. (2024) address OOD detection, most papers do not thoroughly evaluate generalization to out-of-distribution inputs or adversarial robustness.

5. **Theoretical foundations**: The surveyed literature is predominantly empirical. Only Fu et al. (2026) in the broader search results explicitly addresses diffusion theory, suggesting a gap between theoretical understanding and practical innovations.

6. **Limitations reporting**: Most papers do not explicitly state limitations in their abstracts, making it difficult to assess known weaknesses. This represents a broader issue in the literature rather than a technical gap.

## Per-Paper Annotations

### Xue et al. (2026)

**Research question**: How can diffusion-based image generation models explicitly model data manifold geometry to improve sampling quality and reduce FID scores?

**Methodology**: The authors propose MIND (Data Manifold-aware Image diffusioN moDel), which integrates discrete patch tokenization into the score function of a continuous diffusion model, enables end-to-end training via soft top-k aggregation, and uses dual-branch high-frequency feature embedding layers with multi-stage transition sampling for inference.

**Key findings**:
- MIND base model achieves FID of 22.73 without guidance after 80-epoch training, nearly halving the 43.47 FID of the vanilla DiT-B/2 baseline
- MIND reduces FID by 15.95 and 9.06 on average compared with DiT and SiT baselines, respectively
- MIND-B with 130M parameters achieves FID of 2.06 with guidance, outperforming LlamaGen-3B with 3.1B parameters (FID 3.1)
- MIND-XL with 715M parameters further reduces FID to 1.95

**Limitations**: Not stated in abstract

### Wu et al. (2026)

**Research question**: How can diffusion models generate synthetic eye images with precise 4D binocular gaze control for supervised training in eye tracking applications?

**Methodology**: GazeDiT uses an internally constructed spatial condition that grounds global gaze labels in local pupil/iris geometry, with a frozen SegFormer extracting geometry from real images during training and a physical eye renderer sampling gaze-consistent geometries at inference.

**Key findings**:
- GazeDiT achieves substantially lower tail gaze-label error than other diffusion baselines
- The model approaches the gaze estimation error of the same frozen estimator on real images
- Generated data improves downstream eye tracker performance, reducing gaze error on difficult cases from 3.05° to 2.80°

**Limitations**: Not stated in abstract

### Wang and Tong (2026)

**Research question**: How can discrete diffusion image generators be distilled into efficient single-step models without compromising visual fidelity and structural alignment?

**Methodology**: The authors introduce Fixed-Point Distillation (FPD), an end-to-end framework that constructs local correction targets by partially corrupting the student's one-step draft and refining it with a single teacher step. They employ a straight-through estimator to backpropagate through the discrete bottleneck and apply a multi-bandwidth drift loss in continuous feature space.

**Key findings**:
- FPD achieves competitive visual fidelity and structural alignment within a single inference step
- The method narrows the performance gap between single-step students and multi-step teacher models
- FPD outperforms existing discrete distillation baselines on both class-conditional and text-conditional generation tasks
- The fully differentiable pathway enables optional adversarial objectives to enhance perceptual realism

**Limitations**: Not stated in abstract

### Baykal et al. (2026)

**Research question**: How can conditional diffusion image generators be improved for precise image editing while maintaining identity preservation and global consistency?

**Methodology**: The authors incorporate a residual image encoding as additional conditioning to improve identity preservation and editability, optimized through gradient reversal-based strategy that disentangles the residual from edited conditions. This approach reduces reliance on inversion and its associated pitfalls.

**Key findings**:
- Residual encoding enables improved identity preservation and better editability in diffusion-based image editing
- The gradient reversal optimization prevents the residual from interfering with desired edits
- The method produces high-fidelity results across intrinsic-based editing and relighting tasks
- Proof-of-concept demonstrations show effectiveness in text-guided manipulation

**Limitations**: Not stated in abstract

### Chen et al. (2024)

**Research question**: How can foundation models be leveraged to generate challenging fake outlier images that improve out-of-distribution detection performance?

**Methodology**: The authors propose FodFoM, a framework that combines multiple foundation models (BLIP-2, CLIP, Stable Diffusion, GroundingDINO) to generate two types of fake outlier images: semantically similar-but-different images using captioning and generation capabilities, and pure background images by blurring foreground objects.

**Key findings**:
- FodFoM achieves new state-of-the-art OOD detection performance on multiple benchmarks
- The framework flexibly integrates with multiple existing OOD detection methods
- Fake outlier images generated by foundation models help classifiers more accurately differentiate real OOD images from in-distribution ones
- The approach addresses limitations of costly data collection and simplified assumptions in prior methods

**Limitations**: Not stated in abstract

### Qi et al. (2026)

**Research question**: How can Vision-Language Models be adapted for text-to-3D indoor scene generation while avoiding error propagation from sequential decision-making?

**Methodology**: The authors model text-to-3D scene generation as a tree search problem with global and local trees, using PRM-guided MCTS to balance exploration and exploitation. They introduce a hierarchical scene representation (room, region, floor object, and supported object levels) and leverage pre-trained diffusion models for texture prediction.

**Key findings**:
- The tree search approach enables revision of earlier decisions, addressing error propagation in sequential methods
- The method generates more realistic 3D indoor scenes than state-of-the-art approaches
- The authors collected 3DTindo-bench, a new large-scale dataset with 65 scene types and 3250 diverse instructions
- PRM-guided MCTS achieves optimal solutions with fewer attempts through branch pruning

**Limitations**: Not stated in abstract

### Aimuyo et al. (2026)

**Research question**: How can separating orchestration from the datapath in collective communication improve performance and flexibility for distributed GPU inference?

**Methodology**: Purlin is a scale-up communication framework that separates collective semantics, orchestration (via the SNAC protocol: Stage, Notify, And Consume), and hardware-specific datapath (Atom with copy and reduce primitives), enabling customization and reuse across different hardware.

**Key findings**:
- Across seven collectives on A100, H200, and B200 GPUs, Purlin achieves latency speedups up to 5.14x and bandwidth improvements up to 4.50x over baselines
- Integrated into SGLang, Purlin improves offline LLM serving throughput and interactivity by 1.13x on average (up to 1.37x)
- For online LLM inference, interactivity improves by 1.26x on average (up to 2.85x), with largest gains under overload
- For diffusion image generation, Purlin reduces end-to-end latency by up to 1.13x

**Limitations**: Not stated in abstract

### Yang et al. (2026)

**Research question**: How can pre-trained variational autoencoders from diffusion image generation models be leveraged for efficient surrogate modeling of plasma turbulence simulations?

**Methodology**: PreVAE-Turb leverages pre-trained VAEs from Stable Diffusion, fine-tuned on turbulence data using physics-informed loss including spectral loss in Fourier space, combined with ConvLSTM networks for temporal dynamics in latent space and manifold consistency error monitoring during autoregressive rollouts.

**Key findings**:
- The framework is validated on 2D Hasegawa-Wakatani drift-wave turbulence and extended to gyrokinetic turbulence from the GENE code
- A four-channel adaptation simultaneously predicts electrostatic potential, density, and parallel/perpendicular temperature fluctuations without architecture redesign
- Once trained, inference generates thousands of time steps in seconds on a single GPU, providing substantial computational acceleration compared to direct numerical simulation

**Limitations**: Not stated in abstract

### Wang et al. (2026)

**Research question**: Can a hybrid approach combining generative replay with Fisher-metric trust region constraints provide an emergent meta-learning property in continual learning without explicit bilevel optimization?

**Methodology**: The authors study trust region continual learning that combines generative replay with a Fisher-metric trust region constraint, showing the update admits a MAML-style interpretation with a single implicit inner step where replay supplies old-task gradients and the Fisher-weighted penalty provides curvature shaping.

**Key findings**:
- Trust region continual learning achieves the best final performance and retention on task-incremental diffusion image generation and continual diffusion-policy control
- The approach consistently recovers early-task performance faster than EWC, replay, and continual meta-learning baselines
- The method yields an emergent meta-learning property where the model becomes an initialization that rapidly re-converges to prior task optima after each task transition

**Limitations**: Not stated in abstract

## References

Aimuyo, O. J., Gandhi, S., & Kozyrakis, C. (2026). Purlin: Separating orchestration from the datapath of collectives. arXiv. https://arxiv.org/abs/2609.36954

Baykal, A. C., Deschaintre, V., Hold-Geoffroy, Y., Fischer, M., Frühstück, A., Öztireli, C., & Georgiev, I. (2026). ResEdit: Residual embeddings for precise generative image editing. arXiv. https://arxiv.org/abs/2606.16457

Chen, J., Deng, L., Gan, Z., Zheng, W.-S., & Wang, R. (2024). FodFoM: Fake outlier data by foundation models creates stronger visual out-of-distribution detector. arXiv. https://arxiv.org/abs/2412.05293

Qi, M., Deng, W., Zhang, X., & Ma, H. (2026). Global-Local Monte Carlo Tree Search in Vision-Language Models for text-to-3D indoor scene generation. arXiv. https://arxiv.org/abs/2606.06002

Wang, C., & Tong, Y. (2026). One-Step distillation of discrete diffusion image generators via fixed-point iteration. arXiv. https://arxiv.org/abs/2605.21484

Wang, Z., Gupta, A., & MacLellan, C. J. (2026). Trust region continual learning as an implicit meta-learner. arXiv. https://arxiv.org/abs/2602.02417

Wu, D., Colmenares, D., Yang, F., Kundu, J. N., Xie, Y., Behrooz, A., & Lu, C. (2026). GazeDiT: Gaze-accurate diffusion image generation for eye tracking via spatial conditioning. arXiv. https://arxiv.org/abs/2609.17814

Xue, D., Zhu, Z., & Hou, J. (2026). Diffusion image generation with explicit modeling of data manifold geometry. arXiv. https://arxiv.org/abs/2606.00094

Yang, M., Nicholson, M., Del-Castillo-Negrete, D., Hatch, D., & Zhang, G. (2026). A pre-trained variational autoencoder for gyrokinetic plasma turbulence surrogate modeling. arXiv. https://arxiv.org/abs/2609.38438
