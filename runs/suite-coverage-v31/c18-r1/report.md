# Systematic Literature Review: World Models for Robotic Manipulation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "world models robotic manipulation", filtered to category cs.RO, published between 2024-05-27 and 2026-05-27
**Citation format**: APA 7th edition

## Executive Summary

The literature on world models for robotic manipulation is rapidly evolving from task-specific dynamics predictors into comprehensive predictive infrastructure for robot learning. The surveyed papers reveal a field in transition, with researchers exploring diverse architectural paradigms ranging from Gaussian-based 3D scene reconstruction to diffusion-based video generation and large vision-language-action integration. A clear trend emerges toward leveraging world models not merely for planning but as neural simulators enabling policy training, refinement, and evaluation entirely within imagined environments. The integration of multimodal sensing (depth, tactile, vision) with language-conditioned action models represents another dominant direction, aiming to bridge the sim-to-real gap while enabling complex, contact-rich manipulation tasks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "world models robotic manipulation", filtered to category cs.RO, published between 2024-05-27 and 2026-05-27. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: World Models as Neural Simulators for Policy Training

A prominent theme across the literature is the use of world models as high-fidelity neural simulators that enable policy training and refinement without real-world interaction. World-Gymnast (Sharma et al., 2026) demonstrates that training policies via reinforcement learning within a world model can outperform supervised finetuning by 18x and software simulators by 2x. Similarly, World4RL (Jiang et al., 2025) employs diffusion-based world models as frozen simulators for policy refinement entirely in imagined environments, avoiding the need for online real-world interactions. GWM (Lu et al., 2025) extends this concept by using Gaussian world models that can serve as neural simulators supporting model-based reinforcement learning. This represents a paradigm shift from using world models primarily for planning to using them as complete training environments.

### Theme 2: Geometric and 3D Scene Understanding

Multiple papers emphasize the critical importance of robust geometric understanding for robotic manipulation. GWM (Lu et al., 2025) reconstructs future states by inferring the propagation of Gaussian primitives under robot actions, using 3D variational autoencoders for fine-grained scene-level reconstruction with Gaussian Splatting. The "Manipulation as in Simulation" work (Liu et al., 2025) introduces Camera Depth Models that achieve nearly simulation-level accuracy in depth prediction, effectively bridging the sim-to-real gap by providing human-like 3D geometric perception. RoboWM-Bench (Jiang et al., 2026) identifies spatial reasoning and contact prediction as recurring factors affecting execution performance, highlighting that visual plausibility alone is insufficient without embodied executability. These works collectively argue that world models must incorporate explicit 3D geometric reasoning rather than relying solely on 2D visual prediction.

### Theme 3: Multimodal Integration and Language-Action Models

The integration of multiple sensory modalities with language-conditioned action generation represents another dominant research direction. The survey by Shao et al. (2025) categorizes large VLM-based Vision-Language-Action models into monolithic and hierarchical architectural paradigms, examining their integration with world models, reinforcement learning, and learning from human videos. MLA (Liu et al., 2025) introduces a multisensory language-action model that aligns 2D images, 3D point clouds, and tactile tokens through positional correspondence, achieving 12% and 24% improvements over previous 2D and 3D VLA methods respectively in contact-rich tasks. AgiBot World Colosseo (AgiBot World Contributors et al., 2025) provides a large-scale platform with over 1 million trajectories across 217 tasks, enabling generalist policies that can handle complex real-world dexterous and long-horizon tasks. These works reflect a convergence toward unified architectures that process vision, language, touch, and 3D geometry simultaneously.

### Theme 4: Bridging Sim-to-Real and Reality Gaps

Several papers focus specifically on bridging the gap between simulation and real-world deployment. RealD²iff (Liang et al., 2025) proposes a hierarchical diffusion framework that decomposes depth noise into global structural distortions and fine-grained local perturbations, enabling zero-shot sim2real robot manipulation without additional fine-tuning. The Camera Depth Models approach (Liu et al., 2025) generates high-quality paired data from simulation by modeling depth camera noise patterns, allowing policies trained on simulated depth to generalize seamlessly to real robots. These methods share a common strategy: rather than collecting extensive real-world data, they learn to synthesize realistic sensor noise and imperfections from simulation, creating clean-noisy paired datasets that enable robust transfer.

### Theme 5: Benchmarking and Evaluation Frameworks

The emergence of dedicated benchmarks reflects the field's maturation. RoboWM-Bench (Jiang et al., 2026) introduces a manipulation-centric benchmark that converts generated videos into embodied action sequences and validates them through physically grounded simulation, revealing that visual plausibility and embodied executability are not always aligned. AgiBot World Colosseo (AgiBot World Contributors et al., 2025) provides standardized evaluation across five deployment scenarios with human-in-the-loop verification, achieving an order-of-magnitude increase in data scale compared to existing datasets. The comprehensive survey by Wang et al. (2026) reviews 34 manipulation datasets and evaluation protocols, highlighting the fragmentation in current benchmarking approaches and calling for standardized, reproducible evaluation under closed-loop use.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the view that world models should serve as more than passive predictors—they should function as active training environments enabling policy learning and refinement (Sharma et al., 2026; Jiang et al., 2025; Lu et al., 2025). There is also broad agreement that explicit 3D geometric understanding is essential for robust manipulation, with multiple works proposing Gaussian-based or depth-based representations (Lu et al., 2025; Liu et al., 2025; Jiang et al., 2026). The surveyed literature consistently emphasizes that visual realism alone is insufficient; physical executability and contact modeling are critical for real-world deployment (Jiang et al., 2026; Liu et al., 2025).

**Disagreements**: The literature reveals tension between monolithic end-to-end architectures and hierarchical modular approaches. Shao et al. (2025) delineate these as two principal paradigms without resolving which is superior. Similarly, there is divergence in how world models connect to action: some works use world models for direct policy training via RL (Sharma et al., 2026; Jiang et al., 2025), while others integrate them as components within larger vision-language-action systems (Liu et al., 2025; Wang et al., 2026). The choice between diffusion-based video generation (Jiang et al., 2025; Liang et al., 2025) and Gaussian-based 3D reconstruction (Lu et al., 2025) represents another architectural divide, with each approach offering different trade-offs in fidelity, efficiency, and geometric accuracy.

## Gaps and Open Questions

The collective literature reveals several consistent gaps. Contact modeling remains a persistent challenge, with multiple papers noting difficulties in predicting physical interactions accurately (Jiang et al., 2026; Liu et al., 2025; Wang et al., 2026). Hallucination control in generative world models is frequently mentioned but rarely solved—diffusion-based models in particular can generate visually plausible but physically impossible futures (Jiang et al., 2026). Action alignment—ensuring that predicted futures correspond precisely to executed actions—is identified as an open challenge across multiple works (Wang et al., 2026; Sharma et al., 2026). Benchmarking under closed-loop use remains underdeveloped; most evaluations test open-loop prediction quality rather than closed-loop policy performance (Wang et al., 2026; Jiang et al., 2026). Finally, the literature lacks consensus on operational definitions: Wang et al. (2026) explicitly distinguish world models from perception modules, inverse models, policies, rewards, and value functions, suggesting ongoing conceptual fragmentation in the field.

## Per-Paper Annotations

### AgiBot World Contributors et al. (2025)

**Research question**: How can scalable robot data address real-world challenges for generalized robotic manipulation?
**Methodology**: The authors introduce AgiBot World, a large-scale platform with over 1 million trajectories across 217 tasks in five deployment scenarios, collected via a standardized pipeline with human-in-the-loop verification. They propose Genie Operator-1 (GO-1), a generalist policy using latent action representations, and evaluate policies pre-trained on their dataset against Open X-Embodiment baselines.
**Key findings**:
- AgiBot World achieves an order-of-magnitude increase in data scale compared to existing datasets with over 1 million trajectories.
- Policies pre-trained on the AgiBot World dataset achieve an average performance improvement of 30% over those trained on Open X-Embodiment.
- GO-1 achieves over 60% success rate on complex real-world dexterous and long-horizon tasks.
- GO-1 outperforms prior RDT approach by 32% on complex tasks.
- The platform is extensible from grippers to dexterous hands and visuo-tactile sensors for fine-grained skill acquisition.
**Limitations**: not stated in abstract

### Jiang et al. (2025)

**Research question**: How can diffusion model-based world models be combined to enhance pre-trained policies in robotic manipulation?
**Methodology**: The authors propose World4RL, a framework that employs diffusion-based world models as high-fidelity simulators to refine pre-trained policies entirely in imagined environments. The approach involves pre-training a diffusion world model on multi-task datasets and refining policies within a frozen world model, using a two-hot action encoding scheme and diffusion backbones for improved modeling fidelity.
**Key findings**:
- World4RL provides high-fidelity environment modeling for robotic manipulation tasks.
- The framework enables direct end-to-end policy optimization within imagined environments, unlike prior works that use world models primarily for planning.
- Policy refinement within the frozen world model avoids the need for online real-world interactions.
- Extensive simulation and real-world experiments show significantly higher success rates compared to imitation learning and other baselines.
- The two-hot action encoding scheme tailored for robotic manipulation improves modeling fidelity.
**Limitations**: not stated in abstract

### Jiang et al. (2026)

**Research question**: How can video world models for robotic manipulation be systematically evaluated for physical executability rather than just perceptual realism?
**Methodology**: The authors introduce RoboWM-Bench, a manipulation-centric benchmark that converts generated human-hand and robotic manipulation videos into embodied action sequences and validates them through execution in physically grounded simulation environments. The benchmark is built on real-to-sim scene reconstruction and diverse manipulation tasks for standardized, reproducible, and scalable evaluation.
**Key findings**:
- Visual plausibility and embodied executability are not always aligned in video world models.
- Recurring factors affecting execution performance include spatial reasoning, contact prediction, and non-physical geometric distortions.
- These issues are particularly pronounced in complex and long-horizon interactions.
- Embodiment-aware evaluation provides a more fine-grained view of current model capabilities for guiding physically grounded world modeling.
**Limitations**: not stated in abstract

### Liang et al. (2025)

**Research question**: How can the visual sim2real gap in robot manipulation be bridged by learning to synthesize noisy depth observations from simulation?
**Methodology**: The authors propose RealD²iff, a hierarchical coarse-to-fine diffusion framework that decomposes depth noise into global structural distortions and fine-grained local perturbations. They develop Frequency-Guided Supervision (FGS) for global structure modeling and Discrepancy-Guided Optimization (DGO) for localized refinement, integrated into a six-stage imitation learning pipeline.
**Key findings**:
- RealD²iff enables generation of real-world-like depth to construct clean-noisy paired datasets without manual sensor data collection.
- The framework achieves zero-shot sim2real robot manipulation, substantially improving real-world performance without additional fine-tuning.
- The clean-to-noisy paradigm learns to synthesize noisy depth through purely simulation-driven robotic learning.
- Comprehensive empirical and experimental validation demonstrates the effectiveness of the proposed paradigm.
**Limitations**: not stated in abstract

### Liu et al. (2025)

**Research question**: Can robots be endowed with human-like 3D geometric perception capabilities using depth cameras for manipulation tasks?
**Methodology**: The authors propose Camera Depth Models (CDMs) as a plugin for daily-use depth cameras that take RGB images and raw depth signals as input and output denoised, accurate metric depth. They develop a neural data engine that generates high-quality paired data from simulation by modeling a depth camera's noise pattern to train the CDMs.
**Key findings**:
- CDMs achieve nearly simulation-level accuracy in depth prediction, effectively bridging the sim-to-real gap for manipulation tasks.
- A policy trained on raw simulated depth generalizes seamlessly to real-world robots without adding noise or real-world fine-tuning.
- The approach works on two challenging long-horizon tasks involving articulated, reflective, and slender objects with little to no performance degradation.
- Using depth cameras for manipulation is challenging due to limited accuracy and susceptibility to various types of noise.
- 3D geometric information from depth cameras can enable robots to have human-like perceptual capabilities for object interaction.
**Limitations**: not stated in abstract

### Liu et al. (2025)

**Research question**: How can robots achieve comprehensive understanding of robotic-specific multisensory information for complex and contact-rich control in the spatial-physical world?
**Methodology**: The authors introduce a multisensory language-action (MLA) model with an encoder-free multimodal alignment scheme that repurposes the large language model itself as a perception module, aligning 2D images, 3D point clouds, and tactile tokens through positional correspondence. They design a future multisensory generation post-training strategy to enable reasoning about semantic, geometric, and interaction information.
**Key findings**:
- MLA outperforms previous state-of-the-art 2D VLA methods by 12% in complex, contact-rich real-world tasks.
- MLA outperforms previous state-of-the-art 3D VLA methods by 24% in complex, contact-rich real-world tasks.
- The model demonstrates improved generalization to unseen configurations.
- The encoder-free approach directly interprets multimodal cues without separate perception encoders.
**Limitations**: not stated in abstract

### Lu et al. (2025)

**Research question**: How can world models for robotic manipulation incorporate robust geometric information for consistent spatial and physical understanding of the three-dimensional world?
**Methodology**: The authors propose Gaussian World Model (GWM), which reconstructs future states by inferring the propagation of Gaussian primitives under robot actions, using a latent Diffusion Transformer combined with a 3D variational autoencoder for fine-grained scene-level future state reconstruction with Gaussian Splatting.
**Key findings**:
- GWM reconstructs future states by inferring propagation of Gaussian primitives under robot actions.
- The model uses a latent Diffusion Transformer combined with a 3D variational autoencoder for Gaussian Splatting-based reconstruction.
- GWM enhances visual representation for imitation learning agents through self-supervised future prediction training.
- The model can serve as a neural simulator supporting model-based reinforcement learning.
- Both simulated and real-world experiments show GWM-trained policies outperform state-of-the-art methods by impressive margins.
**Limitations**: not stated in abstract

### Sharma et al. (2026)

**Research question**: Can training a policy in a world model be more effective than supervised learning or software simulation for achieving better real-robot performance?
**Methodology**: The authors propose World-Gymnast, which performs RL finetuning of a vision-language-action policy by rolling out the policy in an action-conditioned video world model and rewarding rollouts with a vision-language model, evaluated on the Bridge robot setup.
**Key findings**:
- World-Gymnast outperforms supervised finetuning by as much as 18x on the Bridge robot setup.
- World-Gymnast outperforms software simulator by as much as 2x.
- The approach demonstrates capabilities including training on diverse language instructions and novel scenes from the world model.
- World-Gymnast enables test-time training in novel scenes.
- The method supports online iterative world model and policy improvement.
**Limitations**: not stated in abstract

### Shao et al. (2025)

**Research question**: What is the current state and taxonomy of large VLM-based Vision-Language-Action models for robotic manipulation?
**Methodology**: The authors conduct a systematic, taxonomy-oriented review of large VLM-based VLA models, delineating two principal architectural paradigms (monolithic and hierarchical models) and examining integration with advanced domains, distinctive characteristics, and promising future directions.
**Key findings**:
- Large VLM-based VLA models are categorized into two principal architectural paradigms: monolithic models (single-system and dual-system designs) and hierarchical models (decoupling planning from execution).
- The survey covers integration with reinforcement learning, training-free optimization, learning from human videos, and world model integration.
- The work consolidates recent advances to resolve inconsistencies in existing taxonomies and mitigate research fragmentation.
- Promising future directions include memory mechanisms, 4D perception, efficient adaptation, and multi-agent cooperation.
- The authors provide a regularly updated project page to document ongoing progress in this field.
**Limitations**: not stated in abstract

### Wang et al. (2026)

**Research question**: How can the fragmented literature on world models for robotic manipulation be organized to clarify design choices and operational definitions across different predictive systems?
**Methodology**: The authors survey world models through three questions: what future representation is predicted, how prediction is connected to action, and when prediction is used in the robot-learning pipeline. They operationally define world models as action-conditioned predictive systems, organize existing work into five representation families, develop a functional taxonomy, and review 34 manipulation datasets and evaluation protocols.
**Key findings**:
- World models are evolving from task-specific dynamics predictors into predictive infrastructure for robot learning.
- The literature is fragmented across latent dynamics models, action-conditioned video generators, 3D/4D scene predictors, physics-informed simulators, and predictive modules inside vision-language-action systems.
- Open challenges include contact modeling, hallucination control, action alignment, and benchmarking under closed-loop use.
- The survey distinguishes world models from perception modules, inverse models, policies, rewards, and value functions.
**Limitations**: not stated in abstract

## References

AgiBot World Contributors, Bu, Q., Cai, J., Chen, L., Cui, X., Ding, Y., Feng, S., Gao, S., He, X., Hu, X., Huang, X., Jiang, S., Jiang, Y., Jing, C., Li, H., Li, J., Liu, C., Liu, Y., Lu, Y., Luo, J., et al. (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. arXiv. https://arxiv.org/abs/2503.06669

Jiang, F., Chen, Y., Xu, K., Liu, Y., Wang, H., Shen, Z., Lu, J., Huang, S., Wang, Y., Xie, C., & Wu, R. (2026). RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation. arXiv. https://arxiv.org/abs/2604.19092

Jiang, Z., Liu, K., Qin, Y., Tian, S., Zheng, Y., Zhou, M., Yu, C., Li, H., & Zhao, D. (2025). World4RL: Diffusion world models for policy refinement with reinforcement learning for robotic manipulation. arXiv. https://arxiv.org/abs/2509.19080

Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD$^2$iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion. arXiv. https://arxiv.org/abs/2511.22505

Liu, M., Zhu, Z., Han, X., Hu, P., Lin, H., Li, X., Chen, J., Xu, J., Yang, Y., Lin, Y., Li, X., Yu, Y., Zhang, W., Kong, T., & Kang, B. (2025). Manipulation as in simulation: Enabling accurate geometry perception in robots. arXiv. https://arxiv.org/abs/2509.02530

Liu, Z., Liu, J., Xu, J., Han, N., Gu, C., Chen, H., Zhou, K., Zhang, R., Hsieh, K. C., Wu, K., Che, Z., Tang, J., & Zhang, S. (2025). MLA: A multisensory language-action model for multimodal understanding and forecasting in robotic manipulation. arXiv. https://arxiv.org/abs/2509.26642

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. arXiv. https://arxiv.org/abs/2508.17600

Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey. arXiv. https://arxiv.org/abs/2508.13073

Sharma, A. K., Sun, Y., Lu, N., Zhang, Y., Liu, J., & Yang, S. (2026). World-Gymnast: Training robots with reinforcement learning in a world model. arXiv. https://arxiv.org/abs/2602.02454

Wang, F., Wang, Z., Pei, G., Zhang, M., Liang, C., Hu, J., Li, Z., Wu, J., Han, N., Zhang, Z., Qi, J., Wu, H., Zhang, S., Zheng, P., Pan, J., Navarro-Alarcon, D., Liu, S., & Zhou, P. (2026). World Models for Robotic Manipulation: A Survey. arXiv. https://arxiv.org/abs/2606.00113
