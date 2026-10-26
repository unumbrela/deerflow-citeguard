# Systematic Literature Review: World Models for Robotic Manipulation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "world models robotic manipulation", category cs.RO, published between 2024-05-27 and 2026-05-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on world models for robotic manipulation reveals a rapidly evolving field that is transitioning from theoretical frameworks to practical deployment systems. The surveyed papers demonstrate three dominant approaches: large-scale data-driven platforms for training generalist policies, neural simulation techniques using diffusion-based world models, and multimodal perception architectures that integrate vision-language-action reasoning. A critical insight emerging across multiple studies is that visual plausibility in world model predictions does not necessarily translate to embodied executability, highlighting the need for physically grounded evaluation benchmarks. The convergence of reinforcement learning with world model training—enabling policy refinement entirely in simulated environments—represents a particularly promising direction for bridging the sim-to-real gap in robotic manipulation tasks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "world models robotic manipulation", filtered to category cs.RO, published between 2024-05-27 and 2026-05-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Large-Scale Data Infrastructure for Generalist Policy Learning

The foundational work in this domain emphasizes the importance of massive, diverse datasets for training robots capable of generalized manipulation. AgiBot World Colosseo represents a paradigm shift in scale, introducing a platform with over 1 million trajectories across 217 tasks spanning five deployment scenarios [citation:AgiBot World Contributors et al. (2025)]. This approach leverages latent action representations through the Genie Operator-1 policy, demonstrating that performance scales predictably with increased data volume. The results show an order-of-magnitude increase in data scale compared to existing datasets, with policies achieving 30% average performance improvement over Open X-Embodiment baselines and over 60% success rates on complex dexterous and long-horizon tasks.

Parallel to this infrastructure development, survey work by Shao et al. (2025) contextualizes these efforts within the broader landscape of Vision-Language-Action models, delineating monolithic and hierarchical architectural paradigms [citation:Shao et al. (2025)]. The integration of world models into VLA frameworks emerges as a particularly promising research direction, suggesting that data-rich platforms and generative world modeling are complementary rather than competing approaches.

### Theme 2: Neural Simulation via Diffusion-Based World Models

A significant thread in the literature focuses on leveraging diffusion models as high-fidelity neural simulators for policy training and refinement. GWM introduces Gaussian World Models that reconstruct future states by propagating Gaussian primitives under robot actions, combining latent Diffusion Transformers with 3D variational autoencoders for fine-grained scene-level reconstruction [citation:Lu et al. (2025)]. This self-supervised approach enables imitation learning agents to train on predicted futures, while also supporting model-based reinforcement learning as a neural simulator.

World-Gymnast extends this paradigm by performing RL finetuning of vision-language-action policies through rollouts in action-conditioned video world models, where rollouts are rewarded by vision-language model evaluations [citation:Sharma et al. (2026)]. This approach achieves up to 18x performance improvements over supervised fine-tuning on the Bridge robot setup and outperforms software simulators by up to 2x. The framework supports test-time training in novel scenes and enables online iterative improvement of both world models and policies.

World4RL further refines this approach by employing diffusion-based world models as high-fidelity simulators specifically for policy refinement entirely in imagined environments [citation:Jiang et al. (2025)]. Their two-hot action encoding scheme tailored for robotic manipulation, combined with diffusion backbones, yields significantly higher success rates compared to imitation learning and other baselines, emphasizing the value of accurate dynamics modeling for reinforcement learning applications.

### Theme 3: Perception-Focused Approaches to Sim-to-Real Transfer

Beyond global world modeling, several works address specific perceptual challenges that hinder sim-to-real transfer. RealD$^2$iff tackles the depth noise problem in robotic manipulation by developing a hierarchical coarse-to-fine diffusion framework that decomposes depth noise into global structural distortions and fine-grained local perturbations [citation:Liang et al. (2025)]. Their Frequency-Guided Supervision and Discrepancy-Guided Optimization strategies enable zero-shot sim2real transfer with substantially improved real-world performance without additional fine-tuning.

Camera Depth Models take a different angle by providing neural plugins that denoise raw depth signals from cameras, achieving nearly simulation-level accuracy in metric depth prediction [citation:Liu et al. (2025)]. This approach effectively bridges the sim-to-real gap for manipulation tasks, with policies trained on raw simulated depth generalizing seamlessly to real-world robots without adding noise or fine-tuning. Successful demonstrations include challenging long-horizon tasks involving articulated, reflective, and slender objects.

### Theme 4: Multimodal Sensory Integration for Contact-Rich Manipulation

MLA addresses the fundamental challenge of how robots can achieve comprehensive understanding of multisensory information to perform complex, contact-rich control in the spatial-physical world [citation:Liu et al. (2025)]. Their encoder-free multimodal alignment scheme repurposes the LLM as a perception module to interpret 2D images, 3D point clouds, and tactile tokens. Combined with a future multisensory generation post-training strategy, MLA outperforms previous state-of-the-art 2D VLA methods by 12% and 3D VLA methods by 24% in complex, contact-rich real-world tasks.

### Theme 5: Benchmarking and Evaluation Frameworks

RoboWM-Bench addresses the critical need for systematic evaluation of world models beyond visual plausibility metrics [citation:Jiang et al. (2026)]. By converting generated human-hand and robotic manipulation videos into embodied action sequences validated through execution in physically grounded simulation environments, this benchmark reveals that visual plausibility and embodied executability are not always aligned. Spatial reasoning, contact prediction, and non-physical geometric distortions emerge as recurring factors affecting execution performance, with complex and long-horizon interactions proving particularly challenging.

### Theme 6: Conceptual Foundations and Taxonomies

Zhang et al. (2025) provide essential conceptual grounding by reviewing methods in robotic manipulation that exhibit world model capabilities across perception, prediction, and control functions [citation:Zhang et al. (2025)]. Their analysis identifies core components needed for generalizable and practical world models, noting that definitions, scope, architectures, and essential capabilities remain ambiguous in the field. This foundational work helps clarify what constitutes a "fully realized" world model for robotic manipulation.

## Convergences and Disagreements

**Convergences**: Multiple surveyed papers agree that diffusion-based world models offer superior fidelity for simulating robotic manipulation compared to traditional approaches. Both World-Gymnast and World4RL demonstrate substantial performance gains when using learned world models for policy refinement versus supervised fine-tuning or direct real-world interaction. There is also consensus across studies that visual plausibility alone is insufficient for evaluating world models—their ability to generate physically consistent, executable actions is paramount. Additionally, the literature converges on the importance of large-scale, diverse datasets as foundational infrastructure for training effective world models.

**Disagreements**: While most papers emphasize the benefits of learned world models, there appears to be methodological divergence regarding the optimal balance between simulation fidelity and computational efficiency. Some approaches like GWM prioritize geometric precision through 3D Gaussian representations, while others like World-Gymnast focus on video-based world models that may trade off some geometric accuracy for broader scene coverage. The literature also shows differing perspectives on whether world models should primarily serve as training environments for policy refinement or as direct policy generators.

## Gaps and Open Questions

Despite significant progress, several gaps persist in the world models for robotic manipulation literature. First, none of the surveyed papers explicitly address scalability concerns as world models grow increasingly complex—computational requirements and training costs are rarely quantified. Second, the "limitations" sections across extracted metadata frequently indicate "not stated in abstract," suggesting that important constraints around failure modes, safety considerations, and deployment limitations are not being highlighted in initial paper releases. Third, while benchmarks like RoboWM-Bench have begun addressing evaluation standards, there remains a lack of standardized metrics for comparing world models across different task domains and robot embodiments. Fourth, the literature shows limited exploration of lifelong learning scenarios where world models must adapt to new objects, environments, and skills without catastrophic forgetting. Finally, few papers address the question of how world models should handle multi-robot coordination and collaborative manipulation scenarios.

## Per-Paper Annotations

### AgiBot World Contributors et al. (2025)

**Research question**: How can scalable robot data address real-world challenges for generalized robotic manipulation?
**Methodology**: The authors introduce AgiBot World, a large-scale platform with over 1 million trajectories across 217 tasks in five deployment scenarios, using a standardized collection pipeline with human-in-the-loop verification. They propose Genie Operator-1 (GO-1), a generalist policy leveraging latent action representations to maximize data utilization.
**Key findings**:
- Achieves an order-of-magnitude increase in data scale compared to existing datasets
- Policies pre-trained on their dataset achieve 30% average performance improvement over Open X-Embodiment
- GO-1 exhibits over 60% success rate on complex dexterous and long-horizon tasks
- Outperforms prior RDT approach by 32%
- Demonstrates predictable performance scaling with increased data volume
**Limitations**: not stated in abstract

### Jiang et al. (2026)

**Research question**: How can video world models be systematically evaluated for their ability to generate physically consistent and executable robotic manipulation actions rather than just visually plausible videos?
**Methodology**: The authors introduce RoboWM-Bench, a manipulation-centric benchmark that converts generated human-hand and robotic manipulation videos into embodied action sequences and validates them through execution in physically grounded simulation environments. Using this benchmark, they evaluate state-of-the-art video world models and analyze factors affecting execution performance.
**Key findings**:
- Visual plausibility and embodied executability are not always aligned in world model predictions
- Spatial reasoning, contact prediction, and non-physical geometric distortions are recurring factors affecting execution performance
- Complex and long-horizon interactions are particularly challenging for current models
**Limitations**: not stated in abstract

### Liang et al. (2025)

**Research question**: How can diffusion models be used to bridge the visual sim2real gap in robot manipulation by learning to synthesize noisy depth from clean simulation data?
**Methodology**: The authors propose RealD$^2$iff, a hierarchical coarse-to-fine diffusion framework that decomposes depth noise into global structural distortions and fine-grained local perturbations. They develop two complementary strategies—Frequency-Guided Supervision (FGS) for global structure modeling and Discrepancy-Guided Optimization (DGO) for localized refinement—integrated into a six-stage imitation learning pipeline.
**Key findings**:
- Enables generation of real-world-like depth to construct clean-noisy paired datasets without manual sensor data collection
- Achieves zero-shot sim2real robot manipulation with substantially improved real-world performance without additional fine-tuning
- Demonstrates effectiveness through comprehensive empirical and experimental validation
**Limitations**: not stated in abstract

### Liu et al. (2025)

**Research question**: How can robots achieve accurate geometry perception for manipulation tasks using depth cameras despite their inherent noise and limited accuracy?
**Methodology**: The authors propose Camera Depth Models (CDMs), a neural network plugin that takes RGB images and raw depth signals as input to output denoised, accurate metric depth. They develop a neural data engine that generates high-quality paired training data from simulation by modeling a depth camera's noise pattern, then train policies on simulated depth without fine-tuning.
**Key findings**:
- CDMs achieve nearly simulation-level accuracy in depth prediction
- The approach effectively bridges the sim-to-real gap for manipulation tasks
- A policy trained on raw simulated depth generalizes seamlessly to real-world robots without adding noise or fine-tuning
- Successful performance on two challenging long-horizon tasks involving articulated, reflective, and slender objects with little to no degradation
**Limitations**: not stated in abstract

### Lu et al. (2025)

**Research question**: How can Gaussian primitives be used to create scalable world models for robotic manipulation that preserve geometric information?
**Methodology**: The authors propose a Gaussian World Model (GWM) that reconstructs future states by inferring the propagation of Gaussian primitives under robot actions. The core uses a latent Diffusion Transformer combined with a 3D variational autoencoder for fine-grained scene-level reconstruction with Gaussian Splatting.
**Key findings**:
- GWM enables self-supervised future prediction training for imitation learning agents
- Can serve as a neural simulator supporting model-based reinforcement learning
- Precisely predicts future scenes conditioned on diverse robot actions
- Trained policies outperform state-of-the-art by impressive margins
- Showcases initial data scaling potential of 3D world models
**Limitations**: not stated in abstract

### Sharma et al. (2026)

**Research question**: Can training robot policies in a learned world model be more effective than supervised learning or software simulation for achieving better real-robot performance?
**Methodology**: The authors propose World-Gymnast, which performs RL finetuning of a vision-language-action policy by rolling out the policy in an action-conditioned video world model and rewarding rollouts with a vision-language model. They evaluate on the Bridge robot setup comparing against SFT and software simulators.
**Key findings**:
- World-Gymnast outperforms SFT by as much as 18x on the Bridge robot setup
- Outperforms software simulators by as much as 2x
- Enables training on diverse language instructions and novel scenes from the world model
- Supports test-time training in novel scenes and online iterative world model and policy improvement
- Results suggest learning world models and training policies in the cloud could bridge the gap between demonstration robots and household robots
**Limitations**: not stated in abstract

### Shao et al. (2025)

**Research question**: What is the current state and taxonomy of large VLM-based Vision-Language-Action models for robotic manipulation?
**Methodology**: This survey provides a systematic, taxonomy-oriented review of large VLM-based VLA models for robotic manipulation. It delineates two principal architectural paradigms (monolithic and hierarchical models) and examines integration with advanced domains, distinctive characteristics, and promising research directions.
**Key findings**:
- VLM-based VLA models have emerged as a transformative paradigm for robotic manipulation
- Two principal architectural paradigms exist: monolithic models (single/dual-system designs) and hierarchical models (decoupling planning from execution)
- Integration areas include reinforcement learning, training-free optimization, learning from human videos, and world model integration
- Promising future directions include memory mechanisms, 4D perception, efficient adaptation, and multi-agent cooperation
- The survey consolidates recent advances to resolve inconsistencies in existing taxonomies
**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: What are the core components, capabilities, and functions that a fully realized world model should possess for robotic manipulation?
**Methodology**: This is a survey paper that reviews methods in robotic manipulation that exhibit world model capabilities, analyzing their roles across perception, prediction, and control. The authors examine approaches beyond fixed definitions of world models to identify key challenges, solutions, and essential capabilities.
**Key findings**:
- World models serve as internal representations that encode environmental states, capture dynamics, and support prediction, planning, and reasoning
- The definition, scope, architectures, and essential capabilities of world models remain ambiguous in the field
- The analysis identifies core components needed for generalizable and practical world models in robotics
**Limitations**: not stated in abstract

### Jiang et al. (2025)

**Research question**: How can diffusion model-based world models be combined with reinforcement learning to refine pre-trained policies entirely in imagined environments for robotic manipulation?
**Methodology**: The authors propose World4RL, a framework employing diffusion-based world models as high-fidelity simulators to refine pre-trained policies entirely in imagined environments. The framework is built on two principles: pre-training a diffusion world model that captures diverse dynamics on multi-task datasets, and refining policies within a frozen world model to avoid online real-world interactions. They design a two-hot action encoding scheme tailored for robotic manipulation and adopt diffusion backbones to improve modeling fidelity.
**Key findings**:
- Provides high-fidelity environment modeling for robotic manipulation
- Enables consistent policy refinement through training entirely in imagined environments
- Yields significantly higher success rates compared to imitation learning and other baselines
**Limitations**: not stated in abstract

### Liu et al. (2025)

**Research question**: How can robots achieve comprehensive understanding of multisensory information to perform complex, contact-rich control in the spatial-physical world?
**Methodology**: The authors introduce MLA, a multisensory language-action model that collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives. They propose an encoder-free multimodal alignment scheme that repurposes the LLM as a perception module to interpret 2D images, 3D point clouds, and tactile tokens, combined with a future multisensory generation post-training strategy for reasoning about physical dynamics.
**Key findings**:
- Outperforms previous state-of-the-art 2D VLA methods by 12% in complex, contact-rich real-world tasks
- Outperforms previous state-of-the-art 3D VLA methods by 24% in complex, contact-rich real-world tasks
- Demonstrates improved generalization to unseen configurations
**Limitations**: not stated in abstract

## References

AgiBot World Contributors, Q. B., Cai, J., Chen, L., Cui, X., Ding, Y., Feng, S., Gao, S., He, X., Hu, X., Huang, X., Jiang, S., Jiang, Y., Jing, C., Li, H., Li, J., Liu, C., Liu, Y., Lu, Y., & Luo, J. (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. arXiv. https://arxiv.org/abs/2503.06669

Jiang, F., Chen, Y., Xu, K., Liu, Y., Wang, H., Shen, Z., Lu, J., Huang, S., Wang, Y., Xie, C., & Wu, R. (2026). RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation. arXiv. https://arxiv.org/abs/2604.19092

Jiang, Z., Liu, K., Qin, Y., Tian, S., Zheng, Y., Zhou, M., Yu, C., Li, H., & Zhao, D. (2025). World4RL: Diffusion world models for policy refinement with reinforcement learning for robotic manipulation. arXiv. https://arxiv.org/abs/2509.19080

Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD²iff: Bridging real-world gap in robot manipulation via depth diffusion. arXiv. https://arxiv.org/abs/2511.22505

Liu, M., Zhu, Z., Han, X., Hu, P., Lin, H., Li, X., Chen, J., Xu, J., Yang, Y., Lin, Y., Li, X., Yu, Y., Zhang, W., Kong, T., & Kang, B. (2025). Manipulation as in simulation: Enabling accurate geometry perception in robots. arXiv. https://arxiv.org/abs/2509.02530

Liu, Z., Liu, J., Xu, J., Han, N., Gu, C., Chen, H., Zhou, K., Zhang, R., Hsieh, K. C., Wu, K., Che, Z., Tang, J., & Zhang, S. (2025). MLA: A multisensory language-action model for multimodal understanding and forecasting in robotic manipulation. arXiv. https://arxiv.org/abs/2509.26642

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. arXiv. https://arxiv.org/abs/2508.17600

Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). Large VLM-based vision-language-action models for robotic manipulation: A survey. arXiv. https://arxiv.org/abs/2508.13073

Sharma, A. K., Sun, Y., Lu, N., Zhang, Y., Liu, J., & Yang, S. (2026). World-Gymnast: Training robots with reinforcement learning in a world model. arXiv. https://arxiv.org/abs/2602.02454

Zhang, P.-F., Cheng, Y., Sun, X., Wang, S., Li, F., Zhu, L., & Shen, H. T. (2025). A step toward world models: A survey on robotic manipulation. arXiv. https://arxiv.org/abs/2511.02097
