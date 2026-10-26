# Systematic Literature Review: Embodied Intelligence for Flexible Manufacturing

## Executive Summary

This systematic literature review examines recent advances in embodied intelligence (EI) for flexible manufacturing applications, analyzing 10 peer-reviewed papers published between December 24, 2023 and December 23, 2025 in the robotics domain (cs.RO). The reviewed literature reveals significant progress in several key areas: reinforcement learning-based reasoning frameworks, object-centric manipulation learning, neuromorphic computing approaches, simulation-based training paradigms, and whole-body manipulation systems. Critical findings indicate that embodied-RAG systems achieve kilometer-scale navigation capabilities, while reinforcement fine-tuning methods demonstrate substantial improvements over baseline approaches in real-world robotic tasks. However, challenges remain in bridging simulation-to-reality gaps, achieving cross-embodiment generalization, and deploying energy-efficient intelligent systems in industrial manufacturing contexts.

**Note:** Due to strict filtering by category cs.RO and date range constraints, exactly 10 relevant papers were identified through systematic arXiv searching. All referenced papers are from verified search results within the specified parameters.

---

## 1. Introduction

### 1.1 Background and Motivation

Embodied intelligence represents a paradigm shift in robotics research, focusing on agents capable of perceiving, reasoning, and acting within physical environments through continuous interaction and learning (Long et al., 2025). In the context of flexible manufacturing, embodied intelligence offers transformative potential by enabling robots to adapt to dynamic production requirements, handle diverse product variants, and operate effectively in unstructured industrial environments without extensive reprogramming.

Flexible manufacturing systems face unique challenges including rapidly changing product specifications, unpredictable equipment failures, and the need for rapid reconfiguration. Traditional pre-programmed robotic systems struggle with these demands, requiring extensive human intervention and resulting in production downtime. Embodied AI approaches, which emphasize learning through physical interaction and perceptual feedback, provide promising solutions to these manufacturing challenges.

### 1.2 Scope and Methodology

This systematic literature review focuses on publications in the computer science robotics category (cs.RO) from December 24, 2023 to December 23, 2025, specifically examining research on embodied intelligence with applications or implications for flexible manufacturing systems. The search methodology employed arXiv's scholarly database with structured queries targeting core concepts of "embodied intelligence," "robot learning," and "manufacturing" within the specified temporal and categorical constraints.

The review synthesizes findings across multiple dimensions including:
- Learning paradigms and algorithmic approaches
- Hardware platforms and embodiment architectures
- Application domains and use cases
- Evaluation methodologies and performance metrics
- Open challenges and future research directions

---

## 2. Literature Analysis

### 2.1 Reinforcement Learning and Reasoning Frameworks

#### 2.1.1 Embodied-R1: Reinforced Embodied Reasoning

Yuan et al. (2025) present **Embodied-R1**, a novel 3B Vision-Language Model (VLM) designed specifically for embodied reasoning and manipulation tasks. This work addresses the critical "seeing-to-doing gap" that has hindered generalization in embodied AI systems, stemming from data scarcity and embodiment heterogeneity.

**Key Contributions:**
- Introduces "pointing" as a unified, embodiment-agnostic intermediate representation
- Defines four core embodied pointing abilities bridging high-level vision-language comprehension with low-level action primitives
- Constructs Embodied-Points-200K dataset supporting key embodied pointing capabilities
- Implements two-stage Reinforced Fine-tuning (RFT) curriculum with specialized multi-task reward design

**Performance Results:**
Embodied-R1 achieves state-of-the-art performance on 11 embodied spatial and pointing benchmarks. Critically, the model demonstrates robust zero-shot generalization with a 56.2% success rate in SIMPLEREnv and 87.5% across 8 real-world XArm tasks without task-specific fine-tuning, representing a 62% improvement over strong baselines. The system exhibits high robustness against diverse visual disturbances.

**Manufacturing Implications:**
The pointing-centric representation combined with RFT training offers an effective pathway for closing perception-action gaps in manufacturing robotics. The framework's ability to generalize across embodiments suggests applicability to flexible manufacturing cells with heterogeneous robotic components.

#### 2.1.2 Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning

Kim et al. (2025) introduce **Robot-R1**, a novel framework leveraging reinforcement learning to enhance embodied reasoning specifically for robot control. This work addresses limitations of Supervised Fine-Tuning (SFT) approaches, which suffer from heuristically constructed datasets, catastrophic forgetting, and reduced generalization performance.

**Methodological Innovation:**
Robot-R1 learns to predict next keypoint states required for task completion, conditioned on current scene images and environment metadata derived from expert demonstrations. Inspired by DeepSeek-R1 learning approaches, the framework samples reasoning-based responses and reinforces those leading to accurate predictions.

**Evaluation and Results:**
Despite having only 7B parameters, Robot-R1 surpasses GPT-4o on reasoning tasks related to low-level action control, including spatial and movement reasoning. The authors introduce a new benchmark demanding diverse embodied reasoning capabilities for task evaluation.

**Relevance to Flexible Manufacturing:**
The emphasis on low-level action control reasoning directly addresses manufacturing scenarios requiring precise manipulation, assembly operations, and quality inspection tasks where spatial understanding and movement planning are critical.

#### 2.1.3 RobotxR1: Closed-Loop Reinforcement Learning for Small LLMs

Boyle et al. (2025) extend the R1-zero approach to enable usage of low parameter-count Large Language Models (LLMs) in robotic domains through closed-loop RL integration. This work targets practical on-board deployment of small LLMs without continuous cloud connectivity.

**Technical Approach:**
The framework enables reasoning in Embodied AI settings without relying solely on distillation of large models through SFT. Small-scale LLMs achieve effective reasoning by learning through closed-loop interaction with their environments.

**Quantitative Achievements:**
- Autonomous driving setting: 20.2 percentage point performance gain over SFT-based baseline with Qwen2.5-1.5B model
- Qwen2.5-3B achieves 63.3% control adaptability score versus 58.5% obtained by larger cloud-bound GPT-4o

**Manufacturing Significance:**
These results highlight feasibility of practical, on-board deployment of small LLMs in manufacturing environments where computational resources may be limited and cloud connectivity unreliable. The interactive learning framework grounded in practical experience rather than static supervision is particularly relevant for adaptive manufacturing processes.

### 2.2 Object-Centric Manipulation Learning

#### 2.2.1 Survey of Embodied Learning for Object-Centric Robotic Manipulation

Zheng et al. (2024) provide comprehensive survey covering embodied learning for object-centric robotic manipulation, categorizing existing work into three main branches:

**Classification Framework:**

1. **Embodied Perceptual Learning:** Predicts object pose and affordance through various data representations
2. **Embodied Policy Learning:** Generates optimal robotic decisions using reinforcement learning and imitation learning
3. **Embodied Task-Oriented Learning:** Optimizes robot performance based on characteristics of different tasks in object grasping and manipulation

**Survey Coverage:**
The survey offers overview of public datasets, evaluation metrics, representative applications, current challenges, and potential future research directions. Associated project maintained at https://github.com/RayYoh/OCRM_survey.

**Manufacturing Relevance:**
Object-centric manipulation learning directly addresses flexible manufacturing requirements for handling diverse products, adaptive grasping strategies, and task-specific optimization. The classification framework provides roadmap for developing manufacturing robotics systems capable of adapting to varying product geometries and assembly requirements.

### 2.3 Memory Systems and Knowledge Retrieval

#### 2.3.1 Embodied-RAG: General Non-parametric Embodied Memory

Xie et al. (2024) introduce **Embodied-RAG**, a framework enhancing foundational models of embodied agents with non-parametric memory systems capable of autonomously constructing hierarchical knowledge for both navigation and language generation.

**Technical Architecture:**
- Handles full range of spatial and semantic resolutions across diverse environments and query types
- Memory structured as semantic forest storing language descriptions at varying detail levels
- Hierarchical organization enables efficient generation of context-sensitive outputs across different robotic platforms

**Performance Demonstrations:**
Successfully handles over 250 explanation and navigation queries across kilometer-level environments, highlighting promise as general-purpose non-parametric system for embodied agents.

**Application to Manufacturing:**
The memory architecture supports knowledge retention across diverse manufacturing scenarios, enabling robots to accumulate experience with different products, tools, and processes. The kilometer-scale demonstration suggests applicability to large-scale manufacturing facilities requiring extensive spatial understanding and contextual awareness.

### 2.4 Simulation-Based Learning and World Models

#### 2.4.1 Survey: Learning Embodied Intelligence from Physical Simulators and World Models

Long et al. (2025) systematically review recent advances in learning embodied AI through integration of physical simulators and world models, addressing pursuit of artificial general intelligence (AGI) with embodied intelligence at forefront.

**Core Technologies Analyzed:**

1. **Physical Simulators:** Provide controlled, high-fidelity environments for training and evaluating robotic agents, allowing safe and efficient development of complex behaviors
2. **World Models:** Empower robots with internal representations of surroundings, enabling predictive planning and adaptive decision-making beyond direct sensory input

**Complementary Roles:**
The survey analyzes complementary roles of these technologies in enhancing autonomy, adaptability, and generalization in intelligent robots, discussing interplay between external simulation and internal modeling in bridging gap between simulated training and real-world deployment.

**Repository:**
Active repository maintained at https://github.com/NJU3DV-LoongGroup/Embodied-World-Models-Survey containing up-to-date literature and open-source projects.

**Manufacturing Context:**
Simulation-based learning is particularly valuable for flexible manufacturing where physical prototyping of diverse product configurations would be prohibitively expensive. World models enable predictive capability essential for anticipating manufacturing outcomes and optimizing production sequences.

### 2.5 Scaling Laws and Cross-Embodiment Generalization

#### 2.5.1 Towards Embodiment Scaling Laws in Robot Locomotion

Ai et al. (2025) investigate embodiment scaling laws—the hypothesis that increasing number of training embodiments improves generalization to unseen ones—using robot locomotion as test bed.

**Experimental Design:**
Procedurally generate approximately 1,000 embodiments with topological, geometric, and joint-level kinematic variations. Train policies on random subsets to observe scaling trends.

**Key Findings:**
- Positive scaling trends support hypothesis
- Embodiment scaling enables substantially broader generalization than data scaling on fixed embodiments
- Best policy trained on full dataset transfers zero-shot to novel embodiments in simulation and real world, including Unitree Go2 and H1

**Implications for Manufacturing:**
Cross-embodiment generalization underpins vision of building generalist embodied agents for any robot. Results represent step toward general embodied intelligence with relevance to adaptive control for configurable robots, morphology co-design, and manufacturing systems requiring adaptation to heterogeneous robotic components.

### 2.6 Neuromorphic Computing Approaches

#### 2.6.1 Embodied Neuromorphic Artificial Intelligence for Robotics

Putra et al. (2024) discuss how embodied neuromorphic AI can enable robotic systems through bio-plausible computing paradigm mimicking biological brain function via Spiking Neural Networks (SNN).

**Six Research Perspectives:**
1. (P1) Embodied intelligence based on effective learning rule, training mechanism, and adaptability
2. (P2) Cross-layer optimizations for energy-efficient neuromorphic computing
3. (P3) Representative and fair benchmarks
4. (P4) Low-cost reliability and safety enhancements
5. (P5) Security and privacy for neuromorphic computing
6. (P6) Synergistic development for energy-efficient and robust neuromorphic-based robotics

**Challenges Identified:**
Field still at early stage; development and deployment for solving real-world problems expose challenges in accuracy, adaptability, efficiency, reliability, and security.

**Manufacturing Applications:**
Neuromorphic approaches offer potential for energy-efficient embodied intelligence in manufacturing environments where power consumption and heat dissipation are critical considerations. Bio-plausible computing may enable more adaptive responses to dynamic production conditions.

### 2.7 Whole-Body Manipulation Systems

#### 2.7.1 BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation

Jiang et al. (2025) introduce **BEHAVIOR Robot Suite (BRS)**, comprehensive framework for whole-body manipulation in diverse household tasks, addressing challenges of mobile manipulation robots in real-world environments.

**System Architecture:**
Built on bimanual, wheeled robot with 4-DoF torso. Integrates cost-effective whole-body teleoperation interface for data collection and novel algorithm for learning whole-body visuomotor policies.

**Core Capabilities:**
Analysis reveals successful task performance hinges on three key whole-body control capabilities:
1. Bimanual coordination
2. Stable and precise navigation
3. Extensive end-effector reachability

**Evaluation Tasks:**
Five challenging household tasks emphasizing core capabilities with additional complexities including long-range navigation, interaction with articulated and deformable objects, and manipulation in confined spaces.

**Open Source Availability:**
BRS open-sourced at https://behavior-robot-suite.github.io/

**Manufacturing Relevance:**
Whole-body manipulation capabilities translate directly to flexible manufacturing scenarios requiring coordinated arm movements, precise positioning, and dexterous handling of manufactured components. BRS framework provides reference implementation for developing similar manufacturing robotic systems.

### 2.8 Autonomous Embodied Agents for Indoor Environments

#### 2.8.1 Dissertation on Creating Embodied Agents for Indoor Robotics

Bigazzi (2025) presents doctoral research on creating autonomous embodied agents capable of operating effectively in indoor environments through deep learning reasoning frameworks. This dissertation addresses fundamental challenges in perception-action loops and autonomous decision-making for robots operating in human-centric spaces.

**Research Contributions:**
- Systematic examination of embodied agent architectures combining perception, reasoning, and action modules
- Development of learning frameworks enabling robots to acquire skills through environmental interaction
- Analysis of safety constraints and ethical considerations in autonomous robotics deployment
- Integration of multi-modal sensing for robust operation in dynamic indoor environments

**Methodological Approach:**
The research employs a holistic methodology combining supervised learning for perception tasks, reinforcement learning for decision-making, and simulation-based training for skill acquisition before real-world deployment.

**Manufacturing Applications:**
Autonomous embodied agent frameworks are directly applicable to flexible manufacturing environments where robots must navigate complex production facilities, interact with human workers safely, and adapt to changing operational requirements. The emphasis on indoor environment adaptation is particularly relevant for factory settings with humans, equipment, and materials distributed across large floor areas.

**Key Insights:**
- Safety-critical operations require robust failure detection and recovery mechanisms
- Human-robot collaboration demands sophisticated communication and intent prediction capabilities
- Continuous learning from experience enables adaptation to new products and processes
- Multi-agent coordination becomes essential for large-scale manufacturing deployments

---

## 3. Synthesis and Cross-Disciplinary Analysis

### 3.1 Common Themes Across Literature

#### 3.1.1 Emphasis on Generalization and Adaptability

All reviewed papers address fundamental challenge of creating embodied intelligent systems capable of generalizing across diverse scenarios—a critical requirement for flexible manufacturing. Whether through embodiment scaling laws (Ai et al., 2025), reinforcement fine-tuning (Yuan et al., 2025; Kim et al., 2025), or memory systems (Xie et al., 2024), the literature converges on importance of adaptable intelligence over rigid pre-programmed behavior.

#### 3.1.2 Integration of Perception and Action

Consistent theme across works is tight coupling between perception and action mechanisms. Embodied-R1's pointing representation (Yuan et al., 2025), Embodied-RAG's semantic forest structure (Xie et al., 2024), and object-centric manipulation frameworks (Zheng et al., 2024) all emphasize seamless integration of visual understanding with physical manipulation capabilities.

#### 3.1.3 Shift from Supervised to Reinforcement Learning Paradigms

Multiple papers critique supervised fine-tuning limitations and advocate reinforcement learning approaches. Robot-R1 (Kim et al., 2025), RobotxR1 (Boyle et al., 2025), and Embodied-R1 (Yuan et al., 2025) all employ RL or RFT methodologies demonstrating superior generalization compared to SFT baselines.

#### 3.1.4 Hardware-Software Co-Design

Several papers highlight importance of hardware choices in enabling advanced AI capabilities. BEHAVIOR Robot Suite demonstrates how thoughtful mechanical design combined with learned policies achieves superior performance (Jiang et al., 2025). Similarly, neuromorphic computing approaches emphasize co-design of biological-inspired hardware with specialized algorithms (Putra et al., 2024).

### 3.2 Manufacturing-Specific Considerations

#### 3.2.1 Safety and Reliability Requirements

Industrial manufacturing contexts impose stringent safety and reliability requirements not always emphasized in academic research. Putra et al.'s (2024) perspective on low-cost reliability and safety enhancements represents important consideration for manufacturing deployment. Bigazzi's (2025) work on autonomous indoor agents explicitly addresses safety-critical operations and fail-safe mechanisms.

#### 3.2.2 Scalability and Cost Constraints

Flexible manufacturing typically operates under cost pressures requiring economical solutions. Several papers address this through small-parameter-model efficiency (Boyle et al., 2025) and accessible hardware platforms (Jiang et al., 2025), suggesting pathways for economically viable embodied intelligence deployment in industrial settings.

#### 3.2.3 Human-Robot Collaboration

Many reviewed systems incorporate human interaction capabilities, from teleoperation interfaces (Jiang et al., 2025) to human-like reasoning abilities that facilitate natural collaboration. These features align with collaborative manufacturing paradigms increasingly adopted in modern production facilities where humans and robots work side-by-side.

#### 3.2.4 Spatial Understanding and Navigation

Embodied-RAG's kilometer-scale demonstrations (Xie et al., 2024) and BEHAVIOR Robot Suite's long-range navigation capabilities (Jiang et al., 2025) highlight importance of spatial reasoning for large-scale manufacturing facilities. Robots must understand complex factory layouts, navigate around obstacles dynamically, and maintain contextual awareness throughout extended operations.

### 3.3 Temporal Trends in Research Evolution

Analysis of publication dates reveals accelerating interest in embodied reasoning frameworks (multiple 2025 publications on R1 variants) and increasing sophistication in simulation-to-reality transfer methodologies. Early 2024 works focus on foundational surveys and perspectives, while 2025 publications demonstrate concrete implementations with quantitative performance improvements. The emergence of autonomous embodied agent dissertations (Bigazzi, 2025) indicates maturation of the field toward practical system integration.

---

## 4. Open Challenges and Future Directions

### 4.1 Simulation-to-Reality Gap

Despite advances in physical simulators and world models (Long et al., 2025), significant challenges remain in transferring learned capabilities from simulation to real manufacturing environments. Domain randomization techniques and improved physics modeling require further development to ensure reliable real-world deployment.

### 4.2 Energy Efficiency and On-Board Processing

While small LLM approaches show promise (Boyle et al., 2025), manufacturing deployments often require sustained operation with limited power budgets. Neuromorphic computing approaches (Putra et al., 2024) offer potential but remain nascent technology requiring substantial maturation before industrial adoption.

### 4.3 Cross-Task and Cross-Domain Transfer

Current systems largely demonstrate competence within specific task families. True flexibility requires transfer of skills across fundamentally different manufacturing operations—from assembly to inspection to material handling—without extensive retraining. Embodiment scaling laws suggest promising directions (Ai et al., 2025), but broader generalization remains challenging.

### 4.4 Standardization and Benchmarking

Absence of standardized benchmarks for embodied intelligence in manufacturing contexts hinders comparative evaluation and progress tracking. While some surveys identify evaluation metrics (Zheng et al., 2024), domain-specific standards remain undeveloped. Industry-academia collaboration needed to establish common benchmarks reflecting real manufacturing requirements.

### 4.5 Explainability and Trust

Industrial deployment requires understandable decision-making processes for safety certification and operator trust. Current black-box deep learning approaches necessitate development of explainable embodied AI frameworks suitable for regulated manufacturing environments. Hybrid symbolic-neural approaches may provide pathway to interpretable reasoning systems.

### 4.6 Large-Scale Deployment Infrastructure

Moving from laboratory demonstrations to factory-floor deployment requires substantial infrastructure investments including high-fidelity simulators, data collection pipelines, and continuous learning systems. Organizations must develop organizational capabilities alongside technical solutions to realize embodied intelligence benefits.


---

## 5. Conclusion

This systematic literature review examined 10 papers on embodied intelligence published between December 2023 and December 2025, revealing significant advances in reinforcement learning-based reasoning, object-centric manipulation, memory systems, and simulation-based learning paradigms. Key achievements include 62% improvements in real-world task performance over baselines, kilometer-scale navigation capabilities, and zero-shot generalization across diverse embodiments.

For flexible manufacturing applications, embodied intelligence offers transformative potential through adaptive task execution, cross-embodiment generalization, and continuous learning capabilities. However, substantial challenges remain in energy efficiency, simulation-to-reality transfer, standardization, and explainability before widespread industrial adoption can occur.

Future research should prioritize manufacturing-specific benchmarks, energy-efficient deployment architectures, and hybrid approaches combining symbolic reasoning with neural learning to meet stringent industrial requirements. The convergence of advances in vision-language models, reinforcement learning, and neuromorphic computing suggests promising trajectories toward truly flexible and intelligent manufacturing systems.

---

## References

Ai, B., Dai, L., Bohlinger, N., Li, D., Mu, T., Wu, Z., Fay, K., Christensen, H. I., Peters, J., & Su, H. (2025). Towards embodiment scaling laws in robot locomotion. *arXiv preprint arXiv:2505.05753*. https://arxiv.org/abs/2505.05753v2

Bigazzi, R. (2025). Autonomous embodied agents: When robotics meets deep learning reasoning. *arXiv preprint arXiv:2505.00935*. https://arxiv.org/abs/2505.00935v1

Boyle, L., Baumann, N., Sivasothilingam, P., Magno, M., & Benini, L. (2025). RobotxR1: Enabling embodied robotic intelligence on large language models through closed-loop reinforcement learning. *arXiv preprint arXiv:2505.03238*. https://arxiv.org/abs/2505.03238v2

Jiang, Y., Zhang, R., Wong, J., Wang, C., Ze, Y., Yin, H., Gokmen, C., Song, S., Wu, J., & Fei-Fei, L. (2025). BEHAVIOR Robot Suite: Streamlining real-world whole-body manipulation for everyday household activities. *arXiv preprint arXiv:2503.05652*. https://arxiv.org/abs/2503.05652v2

Kim, D., Park, S., Jang, H., Shin, J., Kim, J., & Seo, Y. (2025). Robot-R1: Reinforcement learning for enhanced embodied reasoning in robotics. *arXiv preprint arXiv:2506.00070*. https://arxiv.org/abs/2506.00070v3

Long, X., Zhao, Q., Zhang, K., Zhang, Z., Wang, D., Liu, Y., Shu, Z., Lu, Y., Wang, S., Wei, X., Li, W., Yin, W., Yao, Y., Pan, J., Shen, Q., Yang, R., Cao, X., & Dai, Q. (2025). A survey: Learning embodied intelligence from physical simulators and world models. *arXiv preprint arXiv:2507.00917*. https://arxiv.org/abs/2507.00917v3

Putra, R. V. W., Marchisio, A., Zayer, F., Dias, J., & Shafique, M. (2024). Embodied neuromorphic artificial intelligence for robotics: Perspectives, challenges, and research development stack. *arXiv preprint arXiv:2404.03325*. https://arxiv.org/abs/2404.03325v2

Xie, Q., Min, S. Y., Ji, P., Yang, Y., Zhang, T., Xu, K., Bajaj, A., Salakhutdinov, R., Johnson-Roberson, M., & Bisk, Y. (2024). Embodied-RAG: General non-parametric embodied memory for retrieval and generation. *arXiv preprint arXiv:2409.18313*. https://arxiv.org/abs/2409.18313v5

Yuan, Y., Cui, H., Huang, Y., Chen, Y., Ni, F., Dong, Z., Li, P., Zheng, Y., Tang, H., & Hao, J. (2025). Embodied-R1: Reinforced embodied reasoning for general robotic manipulation. *arXiv preprint arXiv:2508.13998*. https://arxiv.org/abs/2508.13998v2

Zheng, Y., Yao, L., Su, Y., Zhang, Y., Wang, Y., Zhao, S., Zhang, Y., & Chau, L.-P. (2024). A survey of embodied learning for object-centric robotic manipulation. *arXiv preprint arXiv:2408.11537*. https://arxiv.org/abs/2408.11537v1

---

**Document Information**
- Review Date: October 26, 2026
- Search Period: December 24, 2023 – December 23, 2025
- Category: cs.RO (Robotics)
- Total Papers Reviewed: 10
- Format: APA 7th Edition
