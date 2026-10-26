# Systematic Literature Review: World Models for Robotic Manipulation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "world models robotic manipulation", filtered to category cs.RO, published between 2024-05-27 and 2026-05-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on world models for robotic manipulation reveals a rapidly evolving field transitioning from conceptual frameworks to practical implementations. Recent work demonstrates three dominant paradigms: (1) large-scale data platforms enabling scalable policy learning, (2) world models as neural simulators for reinforcement learning and policy refinement, and (3) multimodal integration combining vision, language, and tactile sensing. Collectively, these papers show that world models are no longer purely theoretical constructs but are being deployed as functional components that enable robots to predict future states, refine policies in imagined environments, and bridge sim-to-real gaps. However, significant challenges remain in achieving physical executability, accurate geometric perception, and generalization across diverse manipulation tasks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "world models robotic manipulation", filtered to category cs.RO, published between 2024-05-27 and 2026-05-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: World Models as Neural Simulators for Policy Training

A prominent direction treats world models as learned simulators that enable policy training entirely within imagined environments, avoiding costly and potentially unsafe real-world reinforcement learning. World-Gymnast (Sharma et al., 2026) demonstrates that training policies by rolling out in an action-conditioned video world model can outperform supervised finetuning by 18x and software simulators by 2x. Similarly, World4RL (Jiang et al., 2025) employs diffusion-based world models as high-fidelity simulators for policy refinement, pre-training on multi-task datasets and refining policies entirely within a frozen world model. GWM (Lu et al., 2025) extends this paradigm by reconstructing future states using Gaussian primitives, serving as a neural simulator that supports model-based reinforcement learning with impressive data scaling potential. These approaches share the core insight that world models can provide sufficient fidelity to enable effective policy learning without real-world interaction, though they differ in their representation choices—video, diffusion, and Gaussian splatting respectively.

### Theme 2: Large-Scale Data Platforms for Scalable Policy Learning

Another major thread emphasizes the critical role of large-scale, standardized datasets in advancing robotic manipulation capabilities. AgiBot World Colosseo (AgiBot World Contributors et al., 2025) introduces a platform with over 1 million trajectories across 217 tasks, achieving an order-of-magnitude increase in data scale compared to existing datasets. Their Genie Operator-1 (GO-1) policy, using latent action representations, demonstrates 30% performance improvement over Open X-Embodiment baselines and over 60% success rate on complex dexterous tasks. This theme reflects a broader recognition that data quality, scale, and standardization are prerequisites for developing generalist policies capable of handling diverse manipulation scenarios. The platform's extensibility from grippers to dexterous hands and visuo-tactile sensors suggests a trajectory toward increasingly comprehensive embodied learning systems.

### Theme 3: Bridging Sim-to-Real Gaps Through Advanced Perception

Multiple papers address the persistent challenge of transferring policies from simulation to real-world deployment by improving perception and sensor modeling. RealD²iff (Liang et al., 2025) proposes a hierarchical diffusion framework that decomposes depth noise into global structural distortions and fine-grained local perturbations, enabling zero-shot sim2real robot manipulation without additional fine-tuning. Manipulation as in Simulation (Liu et al., 2025) introduces Camera Depth Models (CDMs) that achieve nearly simulation-level accuracy in depth prediction, allowing policies trained on raw simulated depth to generalize seamlessly to real-world robots. These approaches recognize that sensor noise and geometric perception accuracy are fundamental bottlenecks, and that explicitly modeling sensor characteristics—rather than treating them as afterthoughts—is essential for robust real-world deployment.

### Theme 4: Multimodal Integration and Language-Action Models

The integration of multiple sensory modalities with language-based reasoning represents a fourth major direction. MLA (Liu et al., 2025) introduces a multisensory language-action model that aligns 2D images, 3D point clouds, and tactile tokens through an encoder-free scheme, repurposing the LLM itself as a perception module. This approach outperforms previous 2D VLA methods by 12% and 3D VLA methods by 24% in complex, contact-rich tasks. The survey by Shao et al. (2025) systematically categorizes large VLM-based Vision-Language-Action models into monolithic and hierarchical architectural paradigms, highlighting integration with world models as a key advancement. These works collectively suggest that effective manipulation requires not just visual prediction but comprehensive multimodal understanding encompassing geometry, touch, and semantic reasoning.

### Theme 5: Benchmarking and Evaluation of World Model Capabilities

As the field matures, attention is turning to systematic evaluation of world model capabilities beyond visual plausibility. RoboWM-Bench (Jiang et al., 2026) introduces a manipulation-centric benchmark that converts generated videos into embodied action sequences and validates them through execution in physically grounded simulation environments. Their key finding—that visual plausibility and embodied executability are not always aligned—highlights a critical gap in current evaluation practices. Spatial reasoning, contact prediction, and non-physical geometric distortions emerge as recurring factors affecting execution performance, particularly for complex and long-horizon interactions. This theme reflects a growing recognition that world models must be evaluated not just on their ability to generate realistic-looking predictions, but on their utility for actual robot control and task execution.

### Theme 6: Conceptual Foundations and Taxonomy of World Models

Underpinning these technical advances is ongoing work to clarify what constitutes a world model and what capabilities it should possess. The survey by Zhang et al. (2025) examines approaches exhibiting core world model capabilities across perception, prediction, and control, noting that the definition, scope, architectures, and essential capabilities of world models remain ambiguous in current research. This conceptual work is essential for guiding future development and ensuring that the term "world model" denotes more than marketing—it should refer to internal representations that encode environmental states, capture dynamics, and support prediction, planning, and reasoning. The survey's examination of methods beyond those explicitly labeled as world models suggests that the field would benefit from clearer taxonomies and more precise terminology.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that world models must provide more than visual prediction—they must support actionable reasoning about physical dynamics and enable policy learning or refinement. There is broad consensus that sim-to-real transfer remains a fundamental challenge requiring explicit modeling of sensor characteristics and physical interactions. Multiple papers converge on the insight that large-scale, diverse data is essential for developing generalist policies capable of handling novel scenarios. The surveyed literature also agrees that multimodal integration—combining vision, language, touch, and potentially other senses—is necessary for complex, contact-rich manipulation tasks.

**Disagreements**: The literature reveals divergence on optimal architectural choices for world models. Video-based approaches (Sharma et al., 2026) compete with diffusion-based methods (Jiang et al., 2025) and Gaussian representation approaches (Lu et al., 2025), with no clear consensus on which provides the best trade-off between fidelity, computational efficiency, and generalization. There is also disagreement implicit in the scale of ambition: some work focuses on incremental improvements to specific components (e.g., depth perception), while other efforts aim to build comprehensive platforms encompassing data collection, policy learning, and deployment. The question of whether world models should be task-specific or general-purpose remains unresolved, with different papers adopting different assumptions.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are discussed only in full papers or that the field has not yet developed standardized practices for acknowledging constraints. Second, while multiple papers demonstrate impressive results on specific benchmarks or tasks, there is limited evidence of cross-task or cross-platform generalization—most evaluations remain within controlled settings. Third, the computational costs of training and deploying world models are rarely discussed, yet they may pose significant barriers to real-world adoption. Fourth, safety considerations—particularly for world models used in reinforcement learning—are mentioned only briefly (Jiang et al., 2025 note avoiding safety concerns of real-robot RL), suggesting this area requires more systematic attention. Finally, the relationship between world models and human-robot interaction, including interpretability and explainability of model predictions, remains largely unexplored in the surveyed literature.

## Per-Paper Annotations

### AgiBot World Contributors et al. (2025)

**Research question**: How can scalable robot data address real-world challenges for generalized robotic manipulation?
**Methodology**: The authors introduce AgiBot World, a large-scale platform with over 1 million trajectories across 217 tasks in five deployment scenarios, collected via a standardized pipeline with human-in-the-loop verification. They propose Genie Operator-1 (GO-1), a generalist policy using latent action representations to maximize data utilization, and evaluate policies pre-trained on their dataset against Open X-Embodiment baselines.
**Key findings**:
- AgiBot World achieves an order-of-magnitude increase in data scale compared to existing datasets with over 1 million trajectories.
- Policies pre-trained on AgiBot World dataset achieve an average 30% performance improvement over those trained on Open X-Embodiment in both in-domain and out-of-distribution scenarios.
- GO-1 demonstrates exceptional capability in real-world dexterous and long-horizon tasks with over 60% success rate on complex tasks.
- GO-1 outperforms prior RDT approach by 32% on complex tasks.
- The platform is extensible from grippers to dexterous hands and visuo-tactile sensors for fine-grained skill acquisition.
**Limitations**: Not stated in abstract

### Jiang et al. (2025)

**Research question**: How can diffusion model-based world models be used as high-fidelity simulators to refine pre-trained robotic manipulation policies entirely in imagined environments?
**Methodology**: The authors propose World4RL, a framework employing diffusion-based world models as high-fidelity simulators for policy refinement, pre-training a diffusion world model on multi-task datasets and refining policies entirely within a frozen world model, with a two-hot action encoding scheme tailored for robotic manipulation.
**Key findings**:
- World4RL enables consistent policy refinement yielding significantly higher success rates compared to imitation learning and other baselines.
- The framework provides high-fidelity environment modeling without online real-world interactions.
- Training entirely within a frozen world model avoids the costs and safety concerns of real-robot reinforcement learning training.
- The two-hot action encoding scheme and diffusion backbones improve modeling fidelity for robotic manipulation tasks.
**Limitations**: Not stated in abstract

### Jiang et al. (2026)

**Research question**: How can video world models for robotic manipulation be evaluated for physical executability rather than just perceptual realism?
**Methodology**: The authors introduce RoboWM-Bench, a manipulation-centric benchmark that converts generated human-hand and robotic manipulation videos into embodied action sequences and validates them through execution in physically grounded simulation environments, built on real-to-sim scene reconstruction and diverse manipulation tasks.
**Key findings**:
- Visual plausibility and embodied executability are not always aligned in state-of-the-art video world models.
- Spatial reasoning, contact prediction, and non-physical geometric distortions are recurring factors that affect execution performance.
- Complex and long-horizon interactions present particular challenges for world model executability.
- Embodiment-aware evaluation provides a more fine-grained view of current model capabilities than visual quality assessment alone.
**Limitations**: Not stated in abstract

### Liang et al. (2025)

**Research question**: How can depth diffusion models bridge the visual sim-to-real gap in robot manipulation by learning to synthesize realistic sensor noise from simulation?
**Methodology**: The authors propose RealD²iff, a hierarchical coarse-to-fine diffusion framework that decomposes depth noise into global structural distortions and fine-grained local perturbations, using Frequency-Guided Supervision for global structure modeling and Discrepancy-Guided Optimization for localized refinement within a six-stage imitation learning pipeline.
**Key findings**:
- RealD²iff enables generation of real-world-like depth to construct clean-noisy paired datasets without manual sensor data collection.
- The framework achieves zero-shot sim2real robot manipulation, substantially improving real-world performance without additional fine-tuning.
- The coarse-to-fine decomposition effectively separates global structural distortions from local perturbations in depth sensor noise.
- Purely simulation-driven robotic learning can bridge the visual sim2real gap through the proposed clean-to-noisy paradigm.
**Limitations**: Not stated in abstract

### Liu et al. (2025a)

**Research question**: How can robots achieve accurate 3D geometric perception for manipulation tasks using depth cameras despite their inherent noise and accuracy limitations?
**Methodology**: The authors propose Camera Depth Models (CDMs) as a plugin for daily-use depth cameras that take RGB images and raw depth signals as input and output denoised, accurate metric depth. They developed a neural data engine that generates high-quality paired training data from simulation by modeling depth camera noise patterns.
**Key findings**:
- CDMs achieve nearly simulation-level accuracy in depth perception, effectively bridging the sim-to-real gap for manipulation tasks.
- A policy trained on raw simulated depth without adding noise or real-world fine-tuning generalizes seamlessly to real-world robots.
- The approach successfully handles two challenging long-horizon tasks involving articulated, reflective, and slender objects with minimal performance degradation.
- Using depth cameras for manipulation is challenging due to their limited accuracy and susceptibility to various types of noise.
**Limitations**: The abstract does not explicitly state limitations of the approach, though it notes that depth cameras inherently have limited accuracy and susceptibility to noise, which CDMs aim to address.

### Liu et al. (2025b)

**Research question**: How can robotic manipulation models achieve comprehensive understanding of robot-specific multisensory information for complex, contact-rich control tasks?
**Methodology**: The authors introduce a multisensory language-action (MLA) model with an encoder-free multimodal alignment scheme that repurposes the LLM itself as a perception module, aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence, combined with a future multisensory generation post-training strategy for physical dynamics understanding.
**Key findings**:
- MLA outperforms previous state-of-the-art 2D VLA methods by 12% in complex, contact-rich real-world tasks.
- MLA outperforms previous state-of-the-art 3D VLA methods by 24% in complex, contact-rich real-world tasks.
- The encoder-free multimodal alignment scheme enables direct interpretation of multimodal cues without separate encoders.
- Future multisensory generation enables reasoning about semantic, geometric, and interaction information for more robust action generation.
- MLA demonstrates improved generalization to unseen configurations.
**Limitations**: Not stated in abstract

### Lu et al. (2025)

**Research question**: How can Gaussian World Models improve robotic manipulation by providing robust geometric information for three-dimensional world understanding?
**Methodology**: The authors propose Gaussian World Model (GWM), which reconstructs future states by inferring propagation of Gaussian primitives under robot actions, using a latent Diffusion Transformer combined with a 3D variational autoencoder for scene-level future state reconstruction with Gaussian Splatting. They evaluate GWM through both simulated and real-world experiments.
**Key findings**:
- GWM reconstructs future states by inferring propagation of Gaussian primitives under robot actions using Gaussian Splatting.
- The model enhances visual representation for imitation learning agents through self-supervised future prediction training.
- GWM can serve as a neural simulator supporting model-based reinforcement learning.
- Both simulated and real-world experiments show GWM precisely predicts future scenes conditioned on diverse robot actions.
- Policies trained using GWM outperform state-of-the-art methods by impressive margins, demonstrating data scaling potential of 3D world models.
**Limitations**: Not stated in abstract

### Shao et al. (2025)

**Research question**: What is the current state and taxonomy of large VLM-based Vision-Language-Action models for robotic manipulation?
**Methodology**: The authors conduct a systematic, taxonomy-oriented review of large VLM-based VLA models, delineating two principal architectural paradigms (monolithic and hierarchical models) and examining integration with advanced domains, distinctive characteristics, and promising future directions.
**Key findings**:
- Large VLM-based VLA models are categorized into two principal architectural paradigms: monolithic models (single-system and dual-system designs) and hierarchical models (decoupling planning from execution).
- The survey synthesizes integration with advanced domains including reinforcement learning, training-free optimization, learning from human videos, and world model integration.
- The work consolidates architectural traits, operational strengths, and supporting datasets and benchmarks for VLA model development.
- Promising future directions include memory mechanisms, 4D perception, efficient adaptation, and multi-agent cooperation.
- The survey resolves inconsistencies in existing taxonomies and mitigates research fragmentation in the field.
**Limitations**: Not stated in abstract

### Sharma et al. (2026)

**Research question**: Can training a policy in a learned world model be more effective than supervised learning or software simulation for achieving better real-robot performance?
**Methodology**: The authors propose World-Gymnast, which performs RL finetuning of a vision-language-action policy by rolling out the policy in an action-conditioned video world model and rewarding rollouts with a vision-language model. They evaluate on the Bridge robot setup comparing against SFT and software simulator baselines.
**Key findings**:
- World-Gymnast outperforms supervised finetuning (SFT) by as much as 18x on the Bridge robot setup.
- World-Gymnast outperforms software simulator by as much as 2x.
- The approach enables training on diverse language instructions and novel scenes from the world model.
- World-Gymnast supports test-time training in novel scenes.
- The method enables online iterative world model and policy improvement.
**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: What are the core components, capabilities, and functions that a fully realized world model should possess for robotic manipulation?
**Methodology**: The authors conduct a survey examining approaches in robotic manipulation that exhibit core world model capabilities, analyzing their roles across perception, prediction, and control to identify key challenges, solutions, and essential components.
**Key findings**:
- World models serve as internal representations that encode environmental states, capture dynamics, and support prediction, planning, and reasoning.
- The definition, scope, architectures, and essential capabilities of world models remain ambiguous in current research.
- The survey examines methods beyond those explicitly labeled as world models, focusing on approaches exhibiting core world model capabilities.
- The analysis identifies key challenges and solutions in perception, prediction, and control for autonomous agents in complex environments.
**Limitations**: The abstract does not explicitly state limitations of the survey methodology or scope.

## References

AgiBot World Contributors, Bu, Q., Cai, J., Chen, L., Cui, X., Ding, Y., Feng, S., Gao, S., He, X., Hu, X., Huang, X., Jiang, S., Jiang, Y., Jing, C., Li, H., Li, J., Liu, C., Liu, Y., Lu, Y., Luo, J., et al. (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. arXiv. https://arxiv.org/abs/2503.06669

Jiang, F., Chen, Y., Xu, K., Liu, Y., Wang, H., Shen, Z., Lu, J., Huang, S., Wang, Y., Xie, C., & Wu, R. (2026). RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation. arXiv. https://arxiv.org/abs/2604.19092

Jiang, Z., Liu, K., Qin, Y., Tian, S., Zheng, Y., Zhou, M., Yu, C., Li, H., & Zhao, D. (2025). World4RL: Diffusion world models for policy refinement with reinforcement learning for robotic manipulation. arXiv. https://arxiv.org/abs/2509.19080

Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD$^2$iff: Bridging real-world gap in robot manipulation via depth diffusion. arXiv. https://arxiv.org/abs/2511.22505

Liu, M., Zhu, Z., Han, X., Hu, P., Lin, H., Li, X., Chen, J., Xu, J., Yang, Y., Lin, Y., Li, X., Yu, Y., Zhang, W., Kong, T., & Kang, B. (2025). Manipulation as in simulation: Enabling accurate geometry perception in robots. arXiv. https://arxiv.org/abs/2509.02530

Liu, Z., Liu, J., Xu, J., Han, N., Gu, C., Chen, H., Zhou, K., Zhang, R., Hsieh, K. C., Wu, K., Che, Z., Tang, J., & Zhang, S. (2025). MLA: A multisensory language-action model for multimodal understanding and forecasting in robotic manipulation. arXiv. https://arxiv.org/abs/2509.26642

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. arXiv. https://arxiv.org/abs/2508.17600

Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). Large VLM-based vision-language-action models for robotic manipulation: A survey. arXiv. https://arxiv.org/abs/2508.13073

Sharma, A. K., Sun, Y., Lu, N., Zhang, Y., Liu, J., & Yang, S. (2026). World-Gymnast: Training robots with reinforcement learning in a world model. arXiv. https://arxiv.org/abs/2602.02454

Zhang, P.-F., Cheng, Y., Sun, X., Wang, S., Li, F., Zhu, L., & Shen, H. T. (2025). A step toward world models: A survey on robotic manipulation. arXiv. https://arxiv.org/abs/2511.02097
