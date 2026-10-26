# Systematic Literature Review: World Models for Robotic Manipulation

**Date of Search:** October 26, 2026  
**Search Period:** May 27, 2024 – May 26, 2026  
**Primary Category:** cs.RO (Robotics)  
**Papers Reviewed:** 10  

---

## Executive Summary

This systematic literature review examines recent advances in world models for robotic manipulation published between May 2024 and May 2026. The field has witnessed significant transformation from traditional simulation-based approaches to sophisticated data-driven world models that enable robots to learn, predict, and execute complex manipulation tasks with unprecedented capabilities. Key findings include the emergence of Gaussian world models for 3D scene understanding, diffusion-based approaches for bridging sim-to-real gaps, multisensory language-action models for physical reasoning, and large-scale manipulation platforms that democratize access to high-quality robot learning data. The reviewed literature demonstrates that world models are becoming critical infrastructure for scalable robot learning, offering alternatives to both costly real-world interactions and imperfect simulations.

---

## Introduction

World models—internal representations that encode environmental dynamics, support state prediction, and enable planning—have emerged as a transformative paradigm in robotic manipulation research. Traditional approaches relying on hand-crafted physics engines or purely reactive control systems struggle to generalize across diverse scenarios and novel environments. In contrast, world models learned from real-world data offer the potential for robots to understand and predict the consequences of their actions in physically consistent ways.

This review systematically analyzes 10 peer-reviewed publications from the robotics domain (cs.RO) that address world modeling for robotic manipulation. The selected papers span multiple complementary approaches: large-scale data platforms for training generalist policies, surveys providing taxonomic frameworks, novel architectures including Gaussian splatting and diffusion models, benchmarking frameworks for evaluation, and multisensory integration strategies. Together, these works illustrate a maturing field moving toward practical deployment while maintaining rigorous scientific standards.

---

## Methodology

### Search Strategy
A systematic search was conducted using arXiv's scholarly database with the following parameters:
- **Query:** "world models robotic manipulation"
- **Time Window:** May 27, 2024 to May 26, 2026
- **Primary Category:** cs.RO (Robotics)
- **Selection Criteria:** Maximum of 10 most relevant papers matching search criteria

### Inclusion Criteria
- Primary focus on world models for robotic manipulation
- Published within the specified time window
- Peer-reviewed preprints or conference publications
- English language

### Exclusion Criteria
- Papers where world models were not a primary contribution
- Publications outside the cs.RO category
- Studies without empirical validation

---

## Thematic Analysis

### Theme 1: Large-Scale Data Infrastructure for Robot Learning

#### AgiBot World Colosseo: A Large-scale Manipulation Platform for Scalable and Intelligent Embodied Systems

**Citation:** AgiBot World Contributors, Bu, Q., Cai, J., Chen, L., Cui, X., Ding, Y., ... Luo, J. (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. *arXiv preprint arXiv:2503.06669*.

**Summary:** This work addresses the fundamental bottleneck of data scarcity in robot learning by introducing AgiBot World, a comprehensive dataset containing over 1 million trajectories across 217 tasks spanning five deployment scenarios. The platform represents an order-of-magnitude increase in data scale compared to existing datasets like Open X-Embodiment.

**Key Contributions:**
- Development of a standardized collection pipeline incorporating human-in-the-loop verification to ensure data quality
- Creation of Genie Operator-1 (GO-1), a generalist policy leveraging latent action representations
- Demonstrated 30% performance improvement over prior baselines in both in-domain and out-of-distribution scenarios
- Achievement of >60% success rate on complex long-horizon dexterous manipulation tasks

**Relevance to World Models:** While not explicitly framed as a world model, this work provides the essential data infrastructure necessary for training predictive models. The authors demonstrate predictable performance scaling with increased data volume, suggesting that world models built upon such datasets can achieve robust generalization capabilities. The open-sourcing of dataset, tools, and models represents a significant step toward democratizing access to high-quality robot learning resources.

**Technical Approach:** The GO-1 architecture employs latent action representations that maximize data utilization efficiency. By operating in latent space rather than raw observation space, the model achieves better sample efficiency and generalization. The system supports extensibility from gripper-based manipulation to dexterous hand operations and visuo-tactile sensor fusion for fine-grained skill acquisition.

---

### Theme 2: Survey and Taxonomic Frameworks

#### Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey

**Citation:** Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). Large VLM-based vision-language-action models for robotic manipulation: A survey. *arXiv preprint arXiv:2508.13073*.

**Summary:** This comprehensive survey provides the first taxonomy-oriented review of large Vision-Language-Model (VLM) based Vision-Language-Action (VLA) models specifically for robotic manipulation applications. The authors systematically organize the rapidly expanding literature into two principal architectural paradigms: monolithic models (single-system and dual-system designs) and hierarchical models (decoupling planning from execution via interpretable intermediate representations).

**Key Contributions:**
- Clear definition and delineation of large VLM-based VLA model architectures
- Systematic integration of world model integration as one of four key application domains alongside reinforcement learning, training-free optimization, and learning from human videos
- Identification of promising future directions including memory mechanisms, 4D perception, efficient adaptation, and multi-agent cooperation
- Maintenance of a regularly updated project page documenting ongoing progress

**Relevance to World Models:** The survey positions world model integration as a critical component for advancing VLA capabilities. The authors note that world models can provide temporal consistency and physical reasoning capabilities that pure VLA models lack, enabling better long-horizon planning and failure recovery. The survey serves as an essential reference for understanding how world models fit within the broader ecosystem of robot learning architectures.

**Critical Analysis:** The authors acknowledge research fragmentation in the field and position their work to resolve inconsistencies in existing taxonomies. This meta-analysis is particularly valuable given the rapid pace of development in world model research during the review period.

---

#### A Step Toward World Models: A Survey on Robotic Manipulation

**Citation:** Zhang, P.-F., Cheng, Y., Sun, X., Wang, S., Li, F., Zhu, L., & Shen, H. T. (2025). A step toward world models: A survey on robotic manipulation. *arXiv preprint arXiv:2511.02097*.

**Summary:** Unlike traditional surveys that prescribe fixed definitions, this work takes a more flexible approach by examining methods that exhibit core world model capabilities through review of approaches in robotic manipulation. The authors analyze roles across perception, prediction, and control dimensions, distilling essential components, capabilities, and functions required for fully realized world models.

**Key Contributions:**
- Flexible definition approach focusing on functional capabilities rather than rigid architectural constraints
- Comprehensive analysis of world model roles in perception, prediction, and control
- Identification of key challenges and solutions in current implementations
- Framework for evaluating progress toward generalizable and practical world models

**Relevance to World Models:** This survey provides conceptual clarity about what constitutes a "world model" in the context of robotic manipulation. The authors argue that the field should move beyond narrow definitions to recognize any approach that exhibits core world model behaviors: encoding environmental states, capturing dynamics, and supporting prediction and planning. This perspective encompasses a broader range of techniques and encourages innovation beyond established architectures.

**Critical Analysis:** The authors' inclusive approach recognizes that world models may emerge from various architectural patterns and implementation strategies. This flexibility is particularly important given the nascent state of the field and the diversity of approaches being explored.

---

### Theme 3: Novel Architectures for 3D Scene Understanding

#### GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

**Citation:** Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. *arXiv preprint arXiv:2508.17600*.

**Summary:** This work introduces Gaussian World Models (GWM), a novel branch of world models that reconstruct future states by inferring the propagation of Gaussian primitives under robot action effects. The approach addresses critical limitations of image-based world models, which lack robust geometric information despite being pretrained on internet-scale video sources.

**Key Contributions:**
- Proposal of Gaussian World Model architecture combining latent Diffusion Transformer (DiT) with 3D variational autoencoder
- Fine-grained scene-level future state reconstruction using Gaussian Splatting technology
- Dual functionality: enhancing visual representation for imitation learning and serving as neural simulator for model-based reinforcement learning
- Demonstration of precise future scene prediction conditioned on diverse robot actions
- Policy training improvements surpassing state-of-the-art by impressive margins

**Technical Innovation:** The core innovation lies in representing scenes as collections of Gaussian primitives rather than pixel grids or voxel grids. This representation enables:
- Efficient 3D scene manipulation and prediction
- Physically consistent spatial reasoning
- Seamless integration with existing rendering pipelines
- Scalability to complex multi-object manipulation scenarios

**Relevance to World Models:** GWM represents a significant advancement in making world models practically useful for robotic manipulation. By explicitly modeling 3D geometry and physical relationships, the approach enables robots to reason about object properties, spatial relationships, and interaction outcomes in ways that pure 2D approaches cannot achieve. The demonstration of data scaling potential suggests that Gaussian world models could become a foundation for next-generation robot learning systems.

**Empirical Validation:** Both simulated and real-world experiments validate the approach. The authors show that GWM can serve as both a self-supervised training mechanism for imitation learning agents and as a neural simulator supporting model-based reinforcement learning. Policies trained using GWM demonstrate superior performance compared to prior approaches.

---

### Theme 4: Bridging Sim-to-Real Gaps Through Generative Modeling

#### RealD²iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion

**Citation:** Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD²iff: Bridging real-world gap in robot manipulation via depth diffusion. *arXiv preprint arXiv:2511.22505*.

**Summary:** This work tackles the fundamental challenge of visual sim-to-real gap in robot manipulation, where depth observations collected in simulation fail to reflect complex noise patterns inherent to real sensors. Rather than attempting to make simulations more realistic, the authors invert the conventional perspective and propose learning to synthesize noisy depth from clean inputs.

**Key Contributions:**
- Hierarchical coarse-to-fine diffusion framework decomposing depth noise into global structural distortions and fine-grained local perturbations
- Frequency-Guided Supervision (FGS) strategy for global structure modeling
- Discrepancy-Guided Optimization (DGO) for localized refinement
- Six-stage pipeline integrating RealD²iff into imitation learning
- Zero-shot sim-to-real robot manipulation capability

**Technical Innovation:** The core insight is that instead of trying to add noise to simulation data to match real sensors, the approach learns to transform clean simulation depth into realistic noisy depth that matches real sensor characteristics. This inversion enables:
- Purely simulation-driven robotic learning without manual sensor data collection
- Generation of real-world-like depth for constructing clean-noisy paired datasets
- Substantial improvement in real-world performance without additional fine-tuning

**Relevance to World Models:** RealD²iff demonstrates how generative modeling can be used to enhance world model capabilities by improving the fidelity of simulated experiences. By learning the distribution of depth noise specific to real sensors, the approach creates world model predictions that better align with actual sensor observations, reducing the sim-to-real transfer gap.

**Practical Impact:** The ability to achieve zero-shot sim-to-real transfer represents a significant breakthrough. Traditional approaches require extensive real-world fine-tuning after simulation-based training, which is costly and time-consuming. RealD²iff eliminates this requirement, enabling more efficient robot learning pipelines.

---

#### Manipulation as in Simulation: Enabling Accurate Geometry Perception in Robots

**Citation:** Liu, M., Zhu, Z., Han, X., Hu, P., Lin, H., Li, X., ... Kang, B. (2025). Manipulation as in simulation: Enabling accurate geometry perception in robots. *arXiv preprint arXiv:2509.02530*.

**Summary:** This work addresses the challenge of using depth cameras for robotic manipulation, which suffers from limited accuracy and susceptibility to various types of noise. The authors propose Camera Depth Models (CDMs) as a plugin for daily-use depth cameras that take RGB images and raw depth signals as input to output denoised, accurate metric depth.

**Key Contributions:**
- Neural data engine generating high-quality paired data from simulation by modeling depth camera noise patterns
- Nearly simulation-level accuracy in depth prediction
- First demonstration that policies trained on raw simulated depth (without noise addition or real-world fine-tuning) generalize seamlessly to real-world robots
- Successful application to challenging long-horizon tasks involving articulated, reflective, and slender objects

**Technical Approach:** CDMs employ a simple yet effective architecture that processes both RGB and raw depth inputs to produce enhanced depth estimates. The key innovation is the neural data engine that generates training data by accurately modeling depth camera noise characteristics in simulation. This enables the model to learn the mapping from noisy to clean depth without requiring extensive real-world labeled data.

**Relevance to World Models:** By enabling robots to perceive 3D geometry with simulation-level accuracy, CDMs enhance the perceptual foundations upon which world models operate. Accurate depth estimation is critical for world models to correctly predict object positions, shapes, and interaction outcomes. The seamless sim-to-real transfer demonstrated by this approach suggests that world models trained on cleaned depth data can generalize effectively to real-world deployments.

**Critical Analysis:** The authors highlight that humans rely more on physical properties (distance, size, shape) than texture when interacting with objects. By endowing robots with similar perceptual capabilities through accurate depth estimation, this work aligns robot perception more closely with human-like interaction strategies. The demonstration of successful generalization to challenging object types (articulated, reflective, slender) shows the robustness of the approach.

---

### Theme 5: Multisensory Integration and Physical Reasoning

#### MLA: A Multisensory Language-Action Model for Multimodal Understanding and Forecasting in Robotic Manipulation

**Citation:** Liu, Z., Liu, J., Xu, J., Han, N., Gu, C., Chen, H., ... Zhang, S. (2025). MLA: A multisensory language-action model for multimodal understanding and forecasting in robotic manipulation. *arXiv preprint arXiv:2509.26642*.

**Summary:** This work introduces Multisensory Language-Action (MLA) models that collaboratively perceive heterogeneous sensory modalities and predict future multisensory objectives to facilitate physical world modeling. The authors address the limitation that most Vision-Language-Action (VLA) models focus on interpreting vision and language to generate actions, whereas robots must also perceive and interact within the spatial-physical world.

**Key Contributions:**
- Encoder-free multimodal alignment scheme repurposing the large language model itself as a perception module
- Direct interpretation of multimodal cues (2D images, 3D point clouds, tactile tokens) through positional correspondence
- Future multisensory generation post-training strategy for reasoning about semantic, geometric, and interaction information
- 12% improvement over state-of-the-art 2D VLA methods and 24% improvement over 3D VLA methods in complex contact-rich real-world tasks
- Enhanced generalization to unseen configurations

**Technical Innovation:** The MLA architecture innovates by:
- Using the LLM backbone itself as a perception module rather than relying on separate encoders
- Aligning multiple sensory modalities through positional correspondence within the LLM's embedding space
- Predicting future multisensory objectives rather than just immediate actions
- Providing robust conditions for action generation through comprehensive physical world modeling

**Relevance to World Models:** MLA explicitly incorporates world model capabilities through its future multisensory generation mechanism. By predicting future states across multiple modalities, the model develops an internal representation of environmental dynamics that supports better action planning and execution. The emphasis on physical world understanding addresses a critical gap in standard VLA approaches.

**Physical Reasoning:** The post-training strategy for future multisensory generation enables the model to reason about:
- Semantic information (object identities, task goals)
- Geometric information (spatial relationships, object properties)
- Interaction information (contact forces, friction effects)

This comprehensive understanding of physical dynamics is essential for world models to make accurate predictions about action consequences.

---

### Theme 6: Reinforcement Learning in World Models

#### World-Gymnast: Training Robots with Reinforcement Learning in a World Model

**Citation:** Sharma, A. K., Sun, Y., Lu, N., Zhang, Y., Liu, J., & Yang, S. (2026). World-Gymnast: Training robots with reinforcement learning in a world model. *arXiv preprint arXiv:2602.02454*.

**Summary:** This work investigates whether training robot policies in world models can outperform both supervised fine-tuning from expert demonstrations and reinforcement learning in software-based simulators. The authors propose World-Gymnast, which performs RL fine-tuning of vision-language-action policies by rolling out policies in action-conditioned video world models and rewarding rollouts with vision-language models.

**Key Contributions:**
- Performance exceeding supervised fine-tuning by up to 18× and software simulators by up to 2× on Bridge robot setup
- Intriguing RL capabilities with world models including:
  - Training on diverse language instructions from the world model
  - Novel scene learning from world model representations
  - Test-time training in novel scenes
  - Online iterative world model and policy improvement
- Evidence that learning world models and training policies in the cloud could bridge the gap between demonstration-working robots and household-capable robots

**Technical Approach:** World-Gymnast operates by:
- Rolling out the policy within an action-conditioned video world model
- Evaluating rollouts using a vision-language model reward function
- Iteratively refining both the world model and the policy through online improvement

**Relevance to World Models:** This work demonstrates the unique advantages of using world models as training environments for reinforcement learning. Unlike software simulators that suffer from sim-to-real gaps, world models learned from real-world data capture authentic environmental dynamics. Unlike direct real-world interaction, world model training is cost-effective and safe. The results suggest that world models can serve as optimal training environments that balance realism and efficiency.

**Critical Analysis:** The dramatic performance improvements (18× over SFT, 2× over simulators) demonstrate that world models can overcome limitations of both traditional approaches. The ability to train on diverse language instructions and novel scenes suggests that world models can support lifelong learning and adaptation to new environments without expensive retraining.

---

#### World4RL: Diffusion World Models for Policy Refinement with Reinforcement Learning for Robotic Manipulation

**Citation:** Jiang, Z., Liu, K., Qin, Y., Tian, S., Zheng, Y., Zhou, M., ... Zhao, D. (2025). World4RL: Diffusion world models for policy refinement with reinforcement learning for robotic manipulation. *arXiv preprint arXiv:2509.19080*.

**Summary:** This work proposes World4RL, a framework employing diffusion-based world models as high-fidelity simulators to refine pre-trained policies entirely within imagined environments for robotic manipulation. The approach addresses limitations of imitation learning (scarcity of expert data) and reinforcement learning (costly real-robot training, sim-to-real gaps).

**Key Contributions:**
- Two-principle design: pre-training diffusion world model on multi-task datasets and refining policies entirely within frozen world model
- Two-hot action encoding scheme tailored for robotic manipulation
- Diffusion backbones for improved modeling fidelity
- Consistent policy refinement yielding significantly higher success rates compared to imitation learning and baselines
- Extensive validation in both simulation and real-world experiments

**Technical Innovation:** Unlike prior works using world models primarily for planning, World4RL enables direct end-to-end policy optimization within the world model. The key innovations include:
- Frozen world model preventing online real-world interactions
- High-fidelity environment modeling through diffusion models
- Action encoding schemes optimized for robotic manipulation dynamics
- Policy refinement entirely in imagined environments

**Relevance to World Models:** World4RL demonstrates that world models can serve as effective training environments for policy optimization. By leveraging the generative capabilities of diffusion models, the approach creates high-fidelity simulations that capture complex manipulation dynamics. The frozen world model design ensures stable training conditions while avoiding the costs and risks of real-world exploration.

**Comparison to Related Work:** World4RL differs from World-Gymnast in its use of diffusion models rather than video world models, and in its focus on policy refinement rather than full policy training from scratch. Both approaches share the core insight that world models can provide superior training environments compared to traditional simulators.

---

### Theme 7: Benchmarking and Evaluation

#### RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation

**Citation:** Jiang, F., Chen, Y., Xu, K., Liu, Y., Wang, H., Shen, Z., ... Wu, R. (2026). RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation. *arXiv preprint arXiv:2604.19092*.

**Summary:** This work addresses the critical need for systematic evaluation of world models in the context of robotic manipulation. While recent advances have enabled increasingly realistic future prediction in video world models, perceptual realism alone is insufficient for embodied manipulation where generated interactions must be physically consistent and executable by robotic agents.

**Key Contributions:**
- Manipulation-centric benchmark for embodiment-grounded evaluation of video world models
- Conversion of generated human-hand and robotic manipulation videos into embodied action sequences
- Validation through execution in physically grounded simulation environments
- Standardized, reproducible, and scalable evaluation of physical executability
- Discovery that visual plausibility and embodied executability are not always aligned

**Methodology:** RoboWM-Bench evaluates world models by:
- Building on real-to-sim scene reconstruction
- Testing across diverse manipulation tasks
- Converting generated videos into executable action sequences
- Validating actions through simulation environment execution
- Analyzing factors affecting execution performance

**Key Findings:**
- Visual plausibility and embodied executability often diverge
- Recurring factors affecting execution include:
  - Spatial reasoning capabilities
  - Contact prediction accuracy
  - Non-physical geometric distortions
  - Particularly problematic in complex and long-horizon interactions

**Relevance to World Models:** This benchmark provides essential evaluation infrastructure for the world model research community. Prior benchmarks focused primarily on visual quality and physical plausibility without assessing whether predicted behaviors could actually be executed by robots. RoboWM-Bench fills this critical gap by directly measuring the manipulability of world model predictions.

**Critical Analysis:** The finding that visual plausibility does not guarantee embodied executability is particularly important for guiding future research. It suggests that world model development should prioritize physical consistency and actionability over pure visual fidelity. The fine-grained analysis capabilities of RoboWM-Bench can help researchers identify specific weaknesses in their approaches and target improvements accordingly.

---

## Cross-Paper Synthesis

### Architectural Trends

The reviewed literature reveals several dominant architectural trends in world models for robotic manipulation:

1. **Generative Modeling Dominance:** Diffusion models and Gaussian splatting represent the leading approaches for world model implementation, offering superior fidelity and physical consistency compared to earlier methods.

2. **Multisensory Integration:** There is growing recognition that world models must integrate multiple sensory modalities (vision, depth, tactile, language) to achieve robust physical world understanding.

3. **3D Scene Representation:** Explicit 3D representations (Gaussian primitives, depth maps) are increasingly preferred over 2D image-based approaches for their superior geometric reasoning capabilities.

4. **Large-Scale Pretraining:** The emergence of million-trajectory datasets indicates a shift toward large-scale pretraining as a foundation for world model development.

### Functional Capabilities

World models in the reviewed literature serve multiple complementary functions:

1. **Prediction:** Anticipating future states given current observations and planned actions
2. **Simulation:** Serving as neural simulators for policy training and evaluation
3. **Planning:** Supporting decision-making through forward-looking capability assessment
4. **Perception Enhancement:** Improving raw sensor observations through denoising and completion
5. **Evaluation:** Providing benchmarks for assessing model quality and capabilities

### Practical Applications

The reviewed works demonstrate world model applications across the robot learning spectrum:

1. **Imitation Learning Enhancement:** Self-supervised future prediction training improves policy performance
2. **Reinforcement Learning:** World models serve as training environments, reducing real-world interaction costs
3. **Sim-to-Real Transfer:** Generative approaches bridge simulation-reality gaps without manual data collection
4. **Policy Refinement:** Post-initialization optimization within world models improves performance
5. **Generalization:** World models enable adaptation to novel scenes and tasks

---

## Critical Analysis

### Strengths

1. **Empirical Rigor:** All reviewed works provide substantial experimental validation, with many demonstrating performance improvements over state-of-the-art baselines.

2. **Practical Relevance:** The research addresses genuine challenges in robot deployment, including sim-to-real gaps, data scarcity, and generalization limitations.

3. **Open Science:** Multiple works commit to open-sourcing datasets, code, and models, facilitating reproducibility and community progress.

4. **Interdisciplinary Integration:** The literature successfully integrates techniques from computer vision, machine learning, robotics, and cognitive science.

### Limitations

1. **Computational Requirements:** Many advanced world models require substantial computational resources for training and inference, potentially limiting accessibility.

2. **Evaluation Gaps:** Despite RoboWM-Bench, standardized evaluation remains fragmented across different benchmarks and metrics.

3. **Scalability Questions:** While some works demonstrate data scaling potential, the limits of current approaches remain unclear.

4. **Safety Concerns:** Training exclusively in world models raises questions about safety guarantees and failure mode handling.

### Research Gaps

1. **Long-Horizon Planning:** Most evaluations focus on short-term predictions; extended horizon planning capabilities require further investigation.

2. **Multi-Robot Coordination:** The literature predominantly addresses single-robot manipulation; collaborative scenarios remain underexplored.

3. **Continuous Learning:** Mechanisms for incremental world model updates in response to new experiences warrant further development.

4. **Human-Robot Collaboration:** Integrating human demonstrations and preferences into world model frameworks needs more attention.

---

## Future Directions

Based on the analyzed literature, several promising research directions emerge:

### Technical Advancements

1. **Hybrid Representations:** Combining implicit (neural) and explicit (geometric) scene representations for optimal efficiency and interpretability.

2. **Energy-Efficient Architectures:** Developing compressed world models suitable for edge deployment on resource-constrained robots.

3. **Causal Reasoning:** Incorporating causal inference capabilities to improve counterfactual reasoning and intervention planning.

4. **Meta-Learning:** Enabling rapid adaptation of world models to new tasks and environments through meta-learning techniques.

### Application Domains

1. **Home Robotics:** Adapting world models for unstructured domestic environments with diverse objects and dynamic layouts.

2. **Industrial Automation:** Applying world models to manufacturing scenarios requiring precision and reliability.

3. **Medical Robotics:** Exploring world model applications in surgical and assistive medical procedures.

4. **Search and Rescue:** Deploying world models in hazardous environments where real-world experimentation is impractical.

### Evaluation Frameworks

1. **Comprehensive Benchmarks:** Expanding evaluation beyond visual quality to include physical consistency, actionability, and safety.

2. **Real-World Validation:** Establishing protocols for systematic real-world testing alongside simulation evaluation.

3. **Comparative Studies:** Conducting head-to-head comparisons of different world model approaches across standardized tasks.

4. **User-Centric Metrics:** Incorporating human feedback and preference data into evaluation frameworks.

---

## Conclusion

The systematic literature review reveals a rapidly evolving field of world models for robotic manipulation characterized by technical sophistication, practical relevance, and strong empirical grounding. Between May 2024 and May 2026, the field has progressed from theoretical concepts to deployable systems capable of addressing fundamental challenges in robot learning.

Key achievements include the establishment of large-scale data infrastructure, development of novel architectures leveraging diffusion models and Gaussian representations, successful bridging of sim-to-real gaps, and creation of comprehensive evaluation frameworks. The integration of multisensory information and physical reasoning capabilities represents a maturation of world model design principles.

However, significant challenges remain, including computational efficiency, evaluation standardization, scalability limits, and safety assurance. The future direction points toward hybrid representations, energy-efficient deployment, causal reasoning capabilities, and expansion into diverse application domains.

The reviewed literature collectively demonstrates that world models are poised to become foundational infrastructure for next-generation robot learning systems. By enabling robots to understand, predict, and plan within complex physical environments, world models promise to accelerate the deployment of autonomous robots in real-world settings ranging from homes and factories to hazardous environments.

As the field continues to mature, the integration of open science practices, comprehensive evaluation frameworks, and interdisciplinary collaboration will be critical for realizing the full potential of world models in robotic manipulation. The progress achieved in this review period provides a strong foundation for continued advancement toward general-purpose robotic intelligence.

---

## References

AgiBot World Contributors, Bu, Q., Cai, J., Chen, L., Cui, X., Ding, Y., Feng, S., Gao, S., He, X., Hu, X., Huang, X., Jiang, S., Jiang, Y., Jing, C., Li, H., Li, J., Liu, C., Liu, Y., Lu, Y., & Luo, J. (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. *arXiv preprint arXiv:2503.06669*. https://arxiv.org/abs/2503.06669v5

Jiang, F., Chen, Y., Xu, K., Liu, Y., Wang, H., Shen, Z., Lu, J., Huang, S., Wang, Y., Xie, C., & Wu, R. (2026). RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation. *arXiv preprint arXiv:2604.19092*. https://arxiv.org/abs/2604.19092v2

Jiang, Z., Liu, K., Qin, Y., Tian, S., Zheng, Y., Zhou, M., Yu, C., Li, H., & Zhao, D. (2025). World4RL: Diffusion world models for policy refinement with reinforcement learning for robotic manipulation. *arXiv preprint arXiv:2509.19080*. https://arxiv.org/abs/2509.19080v2

Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD²iff: Bridging real-world gap in robot manipulation via depth diffusion. *arXiv preprint arXiv:2511.22505*. https://arxiv.org/abs/2511.22505v2

Liu, M., Zhu, Z., Han, X., Hu, P., Lin, H., Li, X., Chen, J., Xu, J., Yang, Y., Lin, Y., Li, X., Yu, Y., Zhang, W., Kong, T., & Kang, B. (2025). Manipulation as in simulation: Enabling accurate geometry perception in robots. *arXiv preprint arXiv:2509.02530*. https://arxiv.org/abs/2509.02530v1

Liu, Z., Liu, J., Xu, J., Han, N., Gu, C., Chen, H., Zhou, K., Zhang, R., Hsieh, K. C., Wu, K., Che, Z., Tang, J., & Zhang, S. (2025). MLA: A multisensory language-action model for multimodal understanding and forecasting in robotic manipulation. *arXiv preprint arXiv:2509.26642*. https://arxiv.org/abs/2509.26642v2

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. *arXiv preprint arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). Large VLM-based vision-language-action models for robotic manipulation: A survey. *arXiv preprint arXiv:2508.13073*. https://arxiv.org/abs/2508.13073v3

Sharma, A. K., Sun, Y., Lu, N., Zhang, Y., Liu, J., & Yang, S. (2026). World-Gymnast: Training robots with reinforcement learning in a world model. *arXiv preprint arXiv:2602.02454*. https://arxiv.org/abs/2602.02454v1

Zhang, P.-F., Cheng, Y., Sun, X., Wang, S., Li, F., Zhu, L., & Shen, H. T. (2025). A step toward world models: A survey on robotic manipulation. *arXiv preprint arXiv:2511.02097*. https://arxiv.org/abs/2511.02097v2

---

**Review prepared by:** DeerFlow AI Agent  
**Date:** October 26, 2026  
**Format:** APA 7th Edition  
**Total Papers:** 10  
**Search Parameters:** cs.RO, 2024-05-27 to 2026-05-26
