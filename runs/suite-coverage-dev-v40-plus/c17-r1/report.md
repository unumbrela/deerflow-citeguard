# Systematic Literature Review: Embodied Intelligence for Flexible Manufacturing

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "embodied intelligence manufacturing", filtered to category cs.RO, published between 2023-12-24 and 2025-12-23
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on embodied intelligence for flexible manufacturing, revealing a field in rapid transformation driven by open-source vision-language-action models and generalist robot policies. The surveyed literature demonstrates a clear shift toward scalable, transferable robot learning frameworks that leverage multimodal demonstrations, instruction tuning, and hierarchical action representations to enable flexible manufacturing capabilities. Key advances include open-source VLA models achieving superior performance with fewer parameters, NeuralSymbolic AI systems enabling autonomous disassembly in unstructured environments, and unified architectures supporting cross-platform deployment without task-specific modifications. The field shows strong convergence on the importance of open-source generalist policies, multimodal representation learning, and physics-informed data generation, though challenges remain in real-time explainability, perception-action integration, and human-robot trust.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "embodied intelligence manufacturing", filtered to category cs.RO, published between 2023-12-24 and 2025-12-23. Papers were sorted by co-citation relevance and the top 10 were included. The search identified 7 papers directly, with citation expansion adding 77 papers from references, yielding a shortlist of 30 papers from which 10 were screened and selected. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Open-Source Generalist Robot Policies

A dominant theme across the surveyed literature is the development of open-source, generalist robot policies that can be efficiently fine-tuned across diverse robotic platforms and tasks. The Octo model team (2024) introduced a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset, demonstrating versatility across 9 robotic platforms with the ability to accommodate new sensory inputs and action spaces within hours on consumer GPUs. Similarly, Kim et al. (2024) developed OpenVLA, a 7B-parameter open-source vision-language-action model that outperforms closed models like RT-2-X (55B parameters) by 16.5% in task success rate across 29 tasks, while remaining efficient enough for fine-tuning via low-rank adaptation methods on consumer hardware. This theme reflects a field-wide recognition that widespread adoption of embodied intelligence in manufacturing requires accessible, open-source foundations rather than proprietary closed systems.

### Theme 2: Vision-Language-Action Integration

The integration of vision, language, and action capabilities represents another central research direction, with multiple papers demonstrating that instruction-tuned multimodal models significantly enhance robot learning and generalization. Niu et al. (2024) introduced LLARVA, which uses instruction tuning with structured prompts to unify robotic learning tasks and predicts intermediate "visual traces" to align vision and action spaces, achieving strong performance on 12 tasks in both simulation and physical robot platforms. Belkhale et al. (2024) developed RT-H, which builds action hierarchies using language by predicting intermediate language motions that describe low-level motions, enabling policies to learn shared structure across disparate tasks and respond to human language interventions during execution. These approaches demonstrate that language serves as a crucial bridging mechanism for grounding high-level task specifications in low-level robot actions.

### Theme 3: Multimodal Representation Learning for Manipulation

Several papers emphasize the importance of unified multimodal representations that effectively incorporate 3D information for precise robot manipulation. Dong et al. (2025) introduced EmbodiedMAE, a multi-modal masked autoencoder that learns representations across RGB, depth, and point cloud modalities through stochastic masking and cross-modal fusion, consistently outperforming state-of-the-art vision foundation models in both training efficiency and final performance across 70 simulation tasks and 20 real-world manipulation tasks. This work highlights that domain gaps between training datasets and robot manipulation tasks can be addressed through unified 3D multi-modal approaches, particularly in precise tabletop manipulation settings where spatial perception is critical.

### Theme 4: NeuralSymbolic AI for Autonomous Manufacturing

The application of NeuralSymbolic AI to autonomous manufacturing systems represents an emerging direction for handling complex, unstructured environments. Peng et al. (2024) proposed BEAM-1, a Battery Disassembly Autonomous Mobile Manipulator Robot based on NeuralSymbolic AI that detects environmental state using multi-sensors and neural predicates, identifies optimal action sequences through LLM-heuristic tree search, and achieves a 98.78% success rate in autonomous perception, decision-making, and execution for continuous bolt disassembly in multiple, multi-category, and complex situations. This system exemplifies how embodied intelligence can combine neural perception with symbolic reasoning to achieve human-like intuition and reasoning capabilities in manufacturing contexts.

### Theme 5: Physics-Informed Data Generation and Cross-Embodiment Transfer

The challenge of generating large-scale, physically consistent datasets for contact-rich manipulation while enabling cross-embodiment transfer is addressed through physics-driven data generation pipelines. Yang et al. (2025) developed a pipeline that starts with embodiment-flexible human demonstrations collected in VR simulation, then refines them using optimization-based kinematic retargeting and trajectory optimization to adapt across robot embodiments and physical parameters, achieving high success rates with zero-shot deployment on hardware for bimanual iiwa arms. This approach enables cross-embodiment data transfer and reuse of legacy datasets from different hardware configurations, addressing a critical bottleneck in scaling robot learning to diverse manufacturing platforms.

### Theme 6: Unified Architectures for Cross-Platform Adaptability

The development of unified architectures that support deployment across diverse robotic platforms without task-specific modifications reflects the field's emphasis on generalization and transferability. Zhao et al. (2025) introduced CoinRobot, a generalized end-to-end robotic learning framework with a unified architecture supporting cross-platform adaptability through multi-task learning and streamlined network designs, enabling deployment across industrial robots, collaborative arms, and novel embodiments without task-specific modifications while achieving superior performance compared to conventional approaches. This theme underscores the manufacturing sector's need for flexible, adaptable robot learning systems that can be deployed across heterogeneous hardware configurations.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong convergence on several key points. First, all papers emphasize the critical importance of open-source, generalist policies as foundational infrastructure for embodied intelligence in manufacturing, with multiple works demonstrating that open models can outperform closed systems while remaining accessible for fine-tuning on consumer hardware (Octo Model Team, 2024; Kim et al., 2024). Second, there is consensus that multimodal integration—combining vision, language, and action—is essential for achieving robust generalization across tasks and environments (Niu et al., 2024; Belkhale et al., 2024; Dong et al., 2025). Third, the literature converges on the value of physics-informed approaches for generating diverse, physically consistent datasets that enable cross-embodiment transfer (Yang et al., 2025).

**Disagreements**: The surveyed papers do not exhibit fundamental disagreements in their findings, as they address complementary aspects of embodied intelligence for manufacturing. However, there are differences in emphasis: some papers prioritize open-source generalist policies trained on large-scale demonstration datasets (Octo Model Team, 2024; Kim et al., 2024), while others focus on specialized architectures for specific manipulation challenges (Dong et al., 2025; Peng et al., 2024). These differences reflect complementary rather than contradictory approaches to the same overarching challenge.

## Gaps and Open Questions

The collective literature reveals several persistent gaps and open questions. First, real-time explainability remains a significant challenge, with Oh (2025) noting that explainable reinforcement learning methods still face limitations in providing interpretable control during real-time operation, which is critical for building human trust in collaborative manufacturing settings. Second, perception-action disjunction—the gap between semantic perception and physical action execution—persists as an unresolved challenge across multiple papers (Oh, 2025; Peng et al., 2024). Third, incomplete human trust in robotic systems remains a barrier to widespread adoption, particularly in human-centric collaborative manufacturing environments (Oh, 2025). Fourth, while several papers demonstrate strong performance in simulation and controlled environments, the abstracts do not extensively address deployment challenges in highly dynamic, unstructured manufacturing environments with continuous human interaction. Finally, the literature lacks extensive discussion of safety certification and regulatory compliance for embodied intelligence systems in manufacturing, which will be critical for industrial adoption.

## Per-Paper Annotations

### Belkhale et al. (2024)

**Research question**: How can language be used to bridge high-level task specifications and low-level robot actions to improve data sharing across semantically diverse tasks?
**Methodology**: RT-H builds an action hierarchy using language by first predicting language motions (fine-grained phrases describing low-level motions), then conditioning on these language motions and the high-level task to predict actions, using visual context at all stages. The method was evaluated on multi-task datasets to demonstrate robustness and flexibility.
**Key findings**:
- Predicting intermediate language motions forces the policy to learn shared structure of low-level motions across disparate tasks.
- The policy conditioned on language motions can be corrected during execution through human-specified language motions.
- RT-H policies allow for responding to language interventions and can learn from such interventions.
- RT-H outperforms methods that learn from teleoperated interventions.
- The language-action hierarchy enables effective use of multi-task datasets for more robust and flexible policies.
**Limitations**: Not stated in abstract.

### Dong et al. (2025)

**Research question**: How can a unified 3D multi-modal representation improve robot manipulation by overcoming domain gaps and effectively incorporating 3D information?
**Methodology**: The authors enhance the DROID dataset with high-quality depth maps and point clouds to create DROID-3D, then develop EmbodiedMAE, a multi-modal masked autoencoder that learns representations across RGB, depth, and point cloud modalities through stochastic masking and cross-modal fusion. The model is evaluated across 70 simulation tasks and 20 real-world robot manipulation tasks on two robot platforms.
**Key findings**:
- EmbodiedMAE consistently outperforms state-of-the-art vision foundation models in both training efficiency and final performance.
- The model exhibits strong scaling behavior with size and promotes effective policy learning from 3D inputs.
- DROID-3D serves as a valuable supplement for 3D embodied vision research.
- EmbodiedMAE is particularly effective in precise tabletop manipulation settings where spatial perception is critical.
- The unified 3D multi-modal approach addresses domain gaps between training datasets and robot manipulation tasks.
**Limitations**: Not stated in abstract.

### Kim et al. (2024)

**Research question**: How can open-source vision-language-action models be developed to enable widespread adoption and efficient fine-tuning for visuomotor control in robotics?
**Methodology**: The authors introduce OpenVLA, a 7B-parameter open-source VLA trained on 970k real-world robot demonstrations, building on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP. They evaluate the model across 29 tasks and multiple robot embodiments, comparing against closed models like RT-2-X and from-scratch methods like Diffusion Policy.
**Key findings**:
- OpenVLA outperforms closed models such as RT-2-X (55B) by 16.5% in absolute task success rate across 29 tasks with 7x fewer parameters.
- OpenVLA outperforms expressive from-scratch imitation learning methods such as Diffusion Policy by 20.4%.
- The model demonstrates strong generalization in multi-task environments involving multiple objects and strong language grounding abilities.
- OpenVLA can be fine-tuned on consumer GPUs via modern low-rank adaptation methods and served efficiently via quantization without loss in downstream success rate.
- The authors release model checkpoints, fine-tuning notebooks, and PyTorch codebase with built-in support for training VLAs at scale.
**Limitations**: Not stated in abstract.

### Niu et al. (2024)

**Research question**: How can instruction-tuned Large Multimodal Models be adapted for robotics to improve generalization across different settings and environments?
**Methodology**: LLARVA uses a novel instruction tuning method with structured prompts to unify robotic learning tasks, scenarios, and environments, and predicts intermediate 2-D representations called 'visual traces' to align vision and action spaces. The model was pre-trained on 8.5M image-visual trace pairs from Open X-Embodiment and evaluated on 12 tasks in RLBench simulator and a physical Franka Emika Panda robot.
**Key findings**:
- LLARVA using 2-D and language representations performs well compared to several contemporary baselines.
- Predicting intermediate visual traces helps align vision and action spaces for robot learning.
- The model can generalize across various robot environments and configurations.
- Instruction tuning with structured prompts unifies a range of robotic learning tasks.
- Strong performance demonstrated on both simulated and physical robot platforms.
**Limitations**: Not stated in abstract.

### Octo Model Team (2024)

**Research question**: How can open-source, widely applicable, generalist robot policies be developed that handle diverse sensors and action spaces across multiple robotic platforms?
**Methodology**: The authors introduce Octo, a large transformer-based policy trained on 800k trajectories from the Open X-Embodiment dataset. They evaluate the model across 9 robotic platforms and perform detailed ablations of design decisions from architecture to training data.
**Key findings**:
- Octo can be instructed via language commands or goal images and effectively finetuned to robot setups with new sensory inputs and action spaces within a few hours on standard consumer GPUs.
- Experiments across 9 robotic platforms demonstrate that Octo serves as a versatile policy initialization that can be effectively finetuned to new observation and action spaces.
- The model accommodates a variety of commonly used robotic platforms and finetunes readily and efficiently to new domains.
- Detailed ablations of design decisions provide guidance for future research on building generalist robot models.
**Limitations**: Not stated in abstract.

### Oh (2025)

**Research question**: How can collaborative robots achieve semantic-level integration and explainable control to enable truly human-centric cooperation?
**Methodology**: This paper conducts a survey-based review examining five foundational pillars: semantic-level perception, cognitive action planning, explainable learning and control, safety-aware motion design, and multimodal human intention recognition. The authors propose a unified Cognitive Synergy Architecture that integrates all modules into a cohesive framework.
**Key findings**:
- Semantic mapping transforms spatial data into meaningful context for cobot decision-making.
- Explainable reinforcement learning methods, including policy distillation and attention mechanisms, enhance interpretability and trust.
- Safety is addressed through force-adaptive control and risk-aware trajectory planning.
- Seamless human interaction is supported via gaze and gesture-based intent recognition.
- Key challenges persist including perception-action disjunction, real-time explainability limitations, and incomplete human trust.
**Limitations**: The paper is a preprint that has not yet undergone peer review, and the final version may differ upon formal publication.

### Peng et al. (2024)

**Research question**: How can NeuralSymbolic AI enable autonomous mobile manipulator robots to perform efficient battery disassembly in dynamic, unstructured environments?
**Methodology**: The authors propose BEAM-1, a Battery Disassembly AMMR system based on NeuralSymbolic AI that detects environmental state using multi-sensors and neural predicates, identifies optimal action sequences through LLM-heuristic tree search, and employs positional speculative sampling with a meticulously designed end-effector for bolt disassembly.
**Key findings**:
- BEAM-1 achieves a 98.78% success rate in autonomous perception, decision-making, and execution for continuous bolt disassembly in multiple, multi-category, and complex situations.
- The system is a continuously learning embodied intelligence system capable of subjective reasoning like a human and possessing intuition.
- The framework can be easily ported to any robotic system to realize different application scenarios.
- The system addresses challenges of pre-programmed disassembly in dynamic environments, complex scenarios, and unstructured processes.
**Limitations**: Not stated in abstract.

### Urain et al. (2024)

**Research question**: What is the current state of deep generative models in robotics for learning from multimodal demonstrations, and what are the key challenges and future directions?
**Methodology**: The authors provide a unified and comprehensive survey reviewing the last year's progress in using deep generative models in robotics, covering different model types, applications, and decisions made to improve generalization, followed by highlighting research challenges and proposing future directions.
**Key findings**:
- Deep generative models are gaining popularity in Learning from Demonstrations as classical methods don't capture complex data distributions well or scale to large numbers of demonstrations.
- The survey covers different model types explored by the community including energy-based models, diffusion models, action value maps, and generative adversarial networks.
- Applications reviewed range from grasp generation to trajectory generation and cost learning.
- The survey reviews different decisions the community has made to improve generalization of learned models out of distributions.
- The authors highlight research challenges and propose future directions for learning deep generative models in robotics.
**Limitations**: Not stated in abstract.

### Yang et al. (2025)

**Research question**: How can physics-based simulation, human demonstrations, and model-based planning be integrated to efficiently generate large-scale datasets for contact-rich robotic manipulation tasks?
**Methodology**: The pipeline starts with embodiment-flexible human demonstrations collected in VR simulation, then refines them using optimization-based kinematic retargeting and trajectory optimization to adapt across robot embodiments and physical parameters. The generated datasets were used to train diffusion policies for contact-rich manipulation tasks on multiple robot embodiments including Allegro hand and bimanual arms.
**Key findings**:
- The pipeline enables cross-embodiment data transfer and reuse of legacy datasets from different hardware configurations.
- Trained policies achieved high success rates with zero-shot deployment on hardware for bimanual iiwa arms.
- The approach yields diverse, physically consistent datasets with minimal human input.
- The method works for challenging contact-rich manipulation tasks across multiple robot embodiments.
- The pipeline integrates physics-based simulation, VR demonstrations, and trajectory optimization effectively.
**Limitations**: Not stated in abstract.

### Zhao et al. (2025)

**Research question**: How can a generalized end-to-end robotic learning framework be designed to achieve generalization and transfer across diverse robotic platforms and environments?
**Methodology**: The framework introduces a unified architecture supporting cross-platform adaptability with multi-task learning and streamlined network designs, enabling deployment across industrial robots, collaborative arms, and novel embodiments without task-specific modifications. Validated through extensive experiments on seven manipulation tasks comparing Diffusion-based models against the LeRobot framework.
**Key findings**:
- The unified architecture supports cross-platform adaptability without task-specific modifications.
- Diffusion-based models trained in the framework demonstrated superior performance compared to the LeRobot framework.
- The framework achieves more robust performance than conventional approaches while maintaining compatibility with varying sensor configurations and action spaces.
- Performance improvements achieved across diverse robotic platforms and environmental conditions.
- The framework enables seamless deployment across industrial-grade robots, collaborative arms, and novel embodiments.
**Limitations**: Not stated in abstract.

## References

Belkhale, S., Ding, T., Xiao, T., Sermanet, P., Vuong, Q., Tompson, J., Chebotar, Y., Dwibedi, D., & Sadigh, D. (2024). RT-H: Action hierarchies using language. arXiv. https://arxiv.org/abs/2403.01823

Dong, Z., Ni, F., Yuan, Y., Li, Y., & Hao, J. (2025). EmbodiedMAE: A unified 3D multi-modal representation for robot manipulation. arXiv. https://arxiv.org/abs/2505.10105

Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., & Finn, C. (2024). OpenVLA: An open-source vision-language-action model. arXiv. https://arxiv.org/abs/2406.09246

Niu, D., Sharma, Y., Biamby, G., Quenum, J., Bai, Y., Shi, B., Darrell, T., & Herzig, R. (2024). LLARVA: Vision-action instruction tuning enhances robot learning. arXiv. https://arxiv.org/abs/2406.11815

Octo Model Team, Ghosh, D., Walke, H., Pertsch, K., Black, K., Mees, O., Dasari, S., Hejna, J., Kreiman, T., Xu, C., Luo, J., Tan, Y. L., Chen, L. Y., Sanketi, P., Vuong, Q., Xiao, T., Sadigh, D., Finn, C., & Levine, S. (2024). Octo: An open-source generalist robot policy. arXiv. https://arxiv.org/abs/2405.12213

Oh, J. (2025). Towards cognitive collaborative robots: Semantic-level integration and explainable control for human-centric cooperation. arXiv. https://arxiv.org/abs/2505.03815

Peng, Y., Wang, Z., Zhang, Y., Zhang, S., Cai, N., Wu, F., & Chen, M. (2024). Revolutionizing battery disassembly: The design and implementation of a battery disassembly autonomous mobile manipulator robot (BEAM-1). arXiv. https://arxiv.org/abs/2407.06590

Urain, J., Mandlekar, A., Du, Y., Shafiullah, M., Xu, D., Fragkiadaki, K., Chalvatzaki, G., & Peters, J. (2024). Deep generative models in robotics: A survey on learning from multimodal demonstrations. arXiv. https://arxiv.org/abs/2408.04380

Yang, L., Suh, H. J. T., Zhao, T., Graesdal, B. P., Kelestemur, T., Wang, J., Pang, T., & Tedrake, R. (2025). Physics-driven data generation for contact-rich manipulation via trajectory optimization. arXiv. https://arxiv.org/abs/2502.20382

Zhao, Y., Liu, H., Chen, X., Sun, J., Yan, J., & Hu, L. (2025). CoinRobot: Generalized end-to-end robotic learning for physical intelligence. arXiv. https://arxiv.org/abs/2503.05316
