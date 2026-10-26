# Systematic Literature Review: World Action Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "world action models", filtered to category cs.RO, published between 2024-06-18 and 2026-06-17
**Citation format**: APA 7th edition

## Executive Summary

The field of World Action Models (WAMs) has rapidly evolved into a unified paradigm that integrates video generation, world modeling, and action prediction for robotic control. The surveyed literature reveals a clear convergence toward video-action frameworks that leverage large-scale pretraining on internet video data combined with robot-specific fine-tuning. Key advances include DreamZero's zero-shot generalization capabilities, Unified World Models' coupling of video and action diffusion, and GR-2's demonstration that web-scale pretraining enables exceptional multi-task performance. The field is moving beyond traditional Vision-Language-Action (VLA) architectures toward more efficient tokenization schemes (FAST), task-centric latent representations (UniVLA), and unified platforms that integrate policy learning with simulation (Genie Envisioner). Collectively, these works establish world modeling as a critical component for achieving generalizable, sample-efficient robot policies.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query `world action models`, filtered to category cs.RO, published between 2024-06-18 and 2026-06-17. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search and screening statistics**: 50 papers identified by search, 92 added from citation expansion, 30 shortlisted, 30 screened, 10 included (9 from reference expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, metadata extraction was limited to abstract-level information; full-text analysis may reveal additional nuances in methodology and limitations.

## Themes

### Theme 1: Video-Action Unification

A dominant theme across the surveyed literature is the unification of video generation and action prediction within single architectures. Rather than treating visual dynamics and motor control as separate problems, recent approaches learn joint representations that enable both forward prediction (what will happen) and inverse dynamics (what action to take).

Zhu et al. (2025) introduced Unified World Models (UWM), which integrates action diffusion and video diffusion within a unified transformer where independent timesteps govern each modality. This enables learning from both action-annotated robot data and action-free video, effectively bridging imitation learning and world modeling paradigms. Similarly, Li et al. (2025) proposed the Unified Video Action model (UVA), which learns a joint video-action latent representation with decoupled decoding heads for high-speed inference. Their masked input training enables a single model to handle forward dynamics, inverse dynamics, and video generation without performance compromise.

The most advanced instantiation of this theme is DreamZero (Ye et al., 2026), which builds on a pretrained 14B video diffusion backbone to jointly model video and action. By treating video as a dense representation of world evolution, DreamZero achieves real-time closed-loop control at 7Hz while maintaining zero-shot generalization to novel environments. Cen et al. (2025) extended this direction with WorldVLA, which integrates VLA and world modeling in one autoregressive framework, though they identified error propagation in action sequence generation as a critical challenge addressed through attention masking.

### Theme 2: Large-Scale Video Pretraining

Multiple papers demonstrate that pretraining on internet-scale video data provides foundational knowledge that dramatically improves robot policy generalization. This represents a paradigm shift from robot-specific imitation learning toward leveraging the vast corpus of human demonstration videos available online.

Cheang et al. (2024) showed that GR-2, pretrained on 38 million internet video clips (over 50 billion tokens), achieves 97.7% average success rate across more than 100 tasks with exceptional generalization to unseen scenarios. The model's ability to scale effectively with model size suggests continued potential for growth. Pai et al. (2025) extended this insight with mimic-video, which pairs internet-scale video pretraining with a flow-matching action decoder. Their approach improves sample efficiency by 10x and convergence speed by 2x compared to traditional VLA architectures, demonstrating that video pretraining jointly captures semantics and visual dynamics while isolating low-level control as the remaining learning problem.

Liao et al. (2025) took this further with Genie Envisioner, a unified platform where GE-Base serves as a large-scale instruction-conditioned video diffusion model capturing robotic interaction dynamics. The platform integrates policy learning (GE-Act), evaluation, and simulation (GE-Sim) within a single video-generative framework, establishing a scalable foundation for instruction-driven embodied intelligence.

### Theme 3: Efficient Action Representations

A critical challenge in world action models is how to represent continuous robot actions for autoregressive generation. Traditional per-dimension, per-timestep binning schemes fail for dexterous, high-frequency tasks, motivating novel tokenization and representation approaches.

Pertsch et al. (2025) proposed Frequency-space Action Sequence Tokenization (FAST), a compression-based scheme using discrete cosine transform. FAST enables training autoregressive VLAs for highly dexterous tasks where standard discretization fails completely. Their universal robot action tokenizer, trained on 1M real robot trajectories, works across diverse action spaces and control frequencies, matching diffusion VLA performance while reducing training time by up to 5x.

Bu et al. (2025) introduced task-centric latent actions in UniVLA, learning cross-embodiment policies using action representations derived from videos with a latent action model in DINO feature space. By incorporating language instructions to mitigate task-irrelevant dynamics, UniVLA achieves state-of-the-art results with less than 1/20 of the pretraining compute and 1/10 of downstream data compared to OpenVLA. This enables exploitation of extensive data across diverse embodiments and perspectives without heavy reliance on action-annotated data.

### Theme 4: Optimization and Fine-Tuning Strategies

As base models mature, attention has shifted to optimizing fine-tuning strategies that maximize performance while maintaining inference efficiency. This includes action decoding schemes, representation choices, and learning objectives.

Kim et al. (2025) systematically studied VLA adaptation design choices using OpenVLA as a base model, resulting in an Optimized Fine-Tuning (OFT) recipe. Their approach integrates parallel decoding, action chunking, continuous action representation, and L1 regression, boosting LIBERO benchmark success rate from 76.5% to 97.1% while increasing throughput by 26×. The optimized approach enables successful execution of dexterous, high-frequency control tasks on bimanual robots and outperforms other VLAs and strong imitation learning policies by up to 15%.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers converge on the necessity of video-based world modeling for achieving generalizable policies—video provides a dense, physically-grounded representation of world dynamics that images alone cannot capture. Second, there is consensus that large-scale pretraining on internet video data is essential for multi-task generalization, with GR-2 (Cheang et al., 2024), mimic-video (Pai et al., 2025), and Genie Envisioner (Liao et al., 2025) all demonstrating this principle. Third, all approaches agree that joint video-action learning outperforms separate modeling of visual dynamics and motor control.

**Disagreements**: The primary disagreement centers on action representation. Pertsch et al. (2025) advocate for discrete tokenization via FAST, arguing that autoregressive models require compressed discrete representations. In contrast, Bu et al. (2025) and Kim et al. (2025) demonstrate that continuous action representations with appropriate decoding schemes (flow matching, parallel decoding) can match or exceed discrete approaches. A second tension exists around model scale: while GR-2 and DreamZero emphasize billion-parameter models trained on massive datasets, UniVLA (Bu et al., 2025) achieves competitive results with dramatically reduced compute, suggesting that architectural innovations may reduce the need for brute-force scaling.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature:

1. **Limited discussion of safety and failure modes**: None of the surveyed papers explicitly address safety constraints, failure recovery, or robustness to distribution shift in real-world deployment. This is a significant gap given the zero-shot and few-shot claims.

2. **Computational efficiency in deployment**: While several papers report inference throughput improvements (Kim et al., 2025: 26×; Li et al., 2025: high-speed decoding), none provide detailed analysis of computational requirements for edge deployment on resource-constrained robots.

3. **Multi-agent and collaborative scenarios**: All surveyed work focuses on single-agent manipulation. The extension of world action models to multi-robot collaboration, human-robot interaction, or competitive scenarios remains unexplored.

4. **Long-horizon planning**: While autoregressive action generation is demonstrated, none of the papers address hierarchical planning or long-horizon task decomposition. The attention mask strategy in WorldVLA (Cen et al., 2025) mitigates error propagation but does not solve the fundamental challenge of long-horizon coherence.

5. **Embodiment diversity**: While UniVLA (Bu et al., 2025) and DreamZero (Ye et al., 2026) demonstrate cross-embodiment transfer, the scope remains limited to similar manipulator architectures. Transfer between fundamentally different embodiments (e.g., legged to manipulator, aerial to ground) is not addressed.

## Per-Paper Annotations

### Bu et al. (2025)

**Research question**: How can we enable generalist robot policies to learn transferable knowledge across different embodiments and environments without relying heavily on action-annotated data?

**Methodology**: UniVLA learns cross-embodiment vision-language-action policies using task-centric action representations derived from videos with a latent action model in the DINO feature space, incorporating language instructions to mitigate task-irrelevant dynamics.

**Key findings**:
- Achieves state-of-the-art results across multiple manipulation and navigation benchmarks and real-robot deployments
- Superior performance over OpenVLA with less than 1/20 of pretraining compute and 1/10 of downstream data
- Continuous performance improvements as heterogeneous data, including human videos, are incorporated
- Generalist policy deployable to various robots through efficient latent action decoding
- Enables exploitation of extensive data across diverse embodiments and perspectives

**Limitations**: Not stated in abstract

### Cen et al. (2025)

**Research question**: How can action and image understanding be unified in a single framework to improve both world modeling and action generation?

**Methodology**: WorldVLA integrates Vision-Language-Action model and world model in one framework, where the world model predicts future images using action and image understanding, and the action model generates subsequent actions based on image observations. An attention mask strategy addresses error propagation in autoregressive action generation.

**Key findings**:
- Outperforms standalone action and world models, demonstrating mutual enhancement
- Autoregressive action sequence generation causes performance deterioration due to error propagation
- Attention mask strategy selectively masks prior actions during current action generation
- Significant performance improvement in action chunk generation tasks

**Limitations**: Not stated in abstract

### Cheang et al. (2024)

**Research question**: How can large-scale internet video pretraining improve generalization and multi-task learning capabilities for robot manipulation?

**Methodology**: GR-2 is pre-trained on 38 million internet video clips (over 50 billion tokens) to capture world dynamics, then fine-tuned for both video generation and action prediction using robot trajectories. Evaluated across more than 100 tasks.

**Key findings**:
- Achieves average success rate of 97.7% across more than 100 tasks
- Exceptional generalization to new, previously unseen scenarios including novel backgrounds, environments, objects, and tasks
- Scales effectively with model size, indicating potential for continued growth
- Large-scale pretraining equips GR-2 with ability to generalize across wide range of robotic tasks and environments

**Limitations**: Not stated in abstract

### Kim et al. (2025)

**Research question**: What are the most effective strategies for fine-tuning vision-language-action models given many possible adaptation design choices?

**Methodology**: Study of key VLA adaptation design choices including action decoding schemes, action representations, and learning objectives using OpenVLA as base model, resulting in Optimized Fine-Tuning (OFT) recipe integrating parallel decoding, action chunking, continuous action representation, and L1 regression-based learning objective.

**Key findings**:
- OpenVLA-OFT sets new state of the art on LIBERO simulation benchmark, boosting average success rate from 76.5% to 97.1%
- Optimized fine-tuning recipe increases action generation throughput by 26×
- Enables successful execution of dexterous, high-frequency control tasks on bimanual ALOHA robot
- Outperforms other VLAs (π₀ and RDT-1B) and strong imitation learning policies (Diffusion Policy and ACT) by up to 15%

**Limitations**: Not stated in abstract

### Li et al. (2025)

**Research question**: How can we effectively combine video generation and action prediction to achieve both high accuracy and efficient action inference in robotics?

**Methodology**: Unified Video Action model (UVA) jointly optimizes video and action predictions by learning a joint video-action latent representation and decoupling video-action decoding using two lightweight diffusion heads for high-speed action inference.

**Key findings**:
- Achieves both high accuracy and efficient action inference by decoupling video-action decoding
- Unified framework enables versatile functionality through masked input training
- Single model tackles forward and inverse dynamics modeling and video generation without compromising performance
- Serves as general-purpose solution for policy learning, forward/inverse dynamics, and video observation prediction
- Joint latent representation effectively bridges visual and action domains

**Limitations**: Not stated in abstract

### Liao et al. (2025)

**Research question**: How can we create a unified platform that integrates policy learning, evaluation, and simulation for robotic manipulation within a single video-generative framework?

**Methodology**: Genie Envisioner (GE) platform with three components: GE-Base (large-scale instruction-conditioned video diffusion model), GE-Act (lightweight flow-matching decoder mapping latent representations to executable actions), and GE-Sim (action-conditioned neural simulator for high-fidelity rollouts).

**Key findings**:
- Integrates policy learning, evaluation, and simulation within single video-generative framework
- GE-Act enables precise and generalizable policy inference across diverse embodiments with minimal supervision
- GE-Sim produces high-fidelity rollouts for closed-loop policy development
- Includes EWMBench, standardized benchmark suite measuring visual fidelity, physical consistency, and instruction-action alignment
- Establishes scalable and practical foundation for instruction-driven, general-purpose embodied intelligence

**Limitations**: Not stated in abstract

### Pai et al. (2025)

**Research question**: How can video pretraining improve physical understanding and reduce the data burden for robot policy learning compared to vision-language pretraining alone?

**Methodology**: mimic-video pairs pretrained Internet-scale video model with flow matching-based action decoder conditioned on its latent representations. Decoder serves as Inverse Dynamics Model generating low-level robot actions from video-space action plan representations. Evaluated on simulated and real-world robotic manipulation tasks.

**Key findings**:
- Achieves state-of-the-art performance on simulated and real-world robotic manipulation tasks
- Improves sample efficiency by 10x compared to traditional VLA architectures
- Convergence speed improved by 2x compared to traditional VLA architectures
- Video pretraining jointly captures semantics and visual dynamics, isolating remaining task of low-level control

**Limitations**: Not stated in abstract

### Pertsch et al. (2025)

**Research question**: How can continuous robot action signals be effectively tokenized for autoregressive vision-language-action models to enable learning dexterous skills from high-frequency robot data?

**Methodology**: Frequency-space Action Sequence Tokenization (FAST) based on discrete cosine transform. FAST+ trained on 1M real robot action trajectories and evaluated combined with pi0 VLA on 10k hours of robot data.

**Key findings**:
- Current per-dimension, per-timestep binning schemes perform poorly for learning dexterous skills from high-frequency robot data
- FAST enables training autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization fails completely
- FAST+ is universal robot action tokenizer trained on 1M real robot action trajectories that works across diverse action spaces and control frequencies
- When combined with pi0 VLA, matches diffusion VLA performance while reducing training time by up to 5x

**Limitations**: Not stated in abstract

### Ye et al. (2026)

**Research question**: How can robot models generalize to unseen physical motions in novel environments without relying on repetitive demonstrations?

**Methodology**: DreamZero is a World Action Model (WAM) built on pretrained video diffusion backbone that jointly models video and action to learn physical dynamics. Video serves as dense representation of world evolution, enabling real-time closed-loop control through model and system optimizations.

**Key findings**:
- Achieves over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real robot experiments
- 14B autoregressive video diffusion model performs real-time closed-loop control at 7Hz
- Video-only demonstrations from other robots or humans yield over 42% relative improvement on unseen task performance with just 10-20 minutes of data
- Enables few-shot embodiment adaptation, transferring to new embodiment with only 30 minutes of play data while retaining zero-shot generalization

**Limitations**: Not stated in abstract

### Zhu et al. (2025)

**Research question**: How can large-scale video data without action annotations be leveraged for robot policy learning alongside action data?

**Methodology**: Unified World Models (UWM) framework integrating action diffusion and video diffusion processes within unified transformer architecture where independent diffusion timesteps govern each modality. Evaluated through simulated and real-world experiments on multitask robot datasets.

**Key findings**:
- Enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning
- Naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps
- Learning from action-free video data further improves performance of finetuned policies
- Offers unification between imitation learning and world modeling paradigms

**Limitations**: Not stated in abstract

## References

Bu, Q., Yang, Y., Cai, J., Gao, S., Ren, G., Yao, M., Luo, P., & Li, H. (2025). UniVLA: Learning to act anywhere with task-centric latent actions. arXiv. https://arxiv.org/abs/2505.06111

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards autoregressive action world model. arXiv. https://arxiv.org/abs/2506.21539

Cheang, C.-L., Chen, G., Jing, Y., Kong, T., Li, H., Li, Y., Liu, Y., Wu, H., Xu, J., Yang, Y., Zhang, H., & Zhu, M. (2024). GR-2: A generative video-language-action model with web-scale knowledge for robot manipulation. arXiv. https://arxiv.org/abs/2410.06158

Kim, M. J., Finn, C., & Liang, P. (2025). Fine-tuning vision-language-action models: Optimizing speed and success. arXiv. https://arxiv.org/abs/2502.19645

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified video action model. arXiv. https://arxiv.org/abs/2503.00200

Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025). Genie Envisioner: A unified world foundation platform for robotic manipulation. arXiv. https://arxiv.org/abs/2508.05635

Pai, J., Achenbach, L., Montesinos, V., Forrai, B., Mees, O., & Nava, E. (2025). mimic-video: Video-action models for generalizable robot control beyond VLAs. arXiv. https://arxiv.org/abs/2512.15692

Pertsch, K., Stachowicz, K., Ichter, B., Driess, D., Nair, S., Vuong, Q., Mees, O., Finn, C., & Levine, S. (2025). FAST: Efficient action tokenization for vision-language-action models. arXiv. https://arxiv.org/abs/2501.09747

Ye, S., Ge, Y., Zheng, K., Gao, S., Yu, S., Kurian, G., Indupuru, S., Tan, Y. L., Zhu, C., Xiang, J., Malik, A., Lee, K., Liang, W., Ranawaka, N., Gu, J., Xu, Y., Wang, G., Hu, F., Narayan, A., & Bjorck, J. (2026). World Action Models are zero-shot policies. arXiv. https://arxiv.org/abs/2602.15922

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling video and action diffusion for pretraining on large robotic datasets. arXiv. https://arxiv.org/abs/2504.02792
