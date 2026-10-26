# Systematic Literature Review: World Models for Robotic Manipulation

**Review Period:** May 27, 2024 – May 26, 2026  
**Primary Category:** cs.RO (Robotics)  
**Papers Reviewed:** 10  

---

## Executive Summary

World models have emerged as a transformative paradigm in robotic manipulation, addressing fundamental challenges in data efficiency, sim-to-real transfer, and physical reasoning. This systematic review synthesizes ten recent papers published between May 2024 and May 2026 that advance world model architectures and applications for robot manipulation tasks. The reviewed works span four major thematic clusters: (1) geometry-enhanced video world models that improve physical consistency; (2) large-scale datasets and platforms enabling scalable policy learning; (3) diffusion-based world models for reinforcement learning and policy refinement; and (4) benchmarking frameworks for evaluating embodiment-grounded world models.

Key findings indicate significant progress in three critical areas. First, geometry-aware representations—through Gaussian Splatting [citation:GWM](https://arxiv.org/abs/2508.17600v2), 4D correspondences [citation:GEM-4D](https://arxiv.org/abs/2605.22882v4), and Camera Depth Models [citation:CDM](https://arxiv.org/abs/2509.02530v1)—have substantially improved spatial reasoning and physical grounding. Second, integration of world models with reinforcement learning has demonstrated dramatic performance improvements, with World-Gymnast achieving up to 18× improvement over supervised fine-tuning [citation:World-Gymnast](https://arxiv.org/abs/2602.02454v1). Third, large-scale data collection platforms like AgiBot World Colosseo with over 1 million trajectories have enabled predictable scaling laws for generalist policies [citation:AgiBot](https://arxiv.org/abs/2503.06669v5).

Despite these advances, persistent challenges remain around embodied executability, where visual plausibility does not always align with actionable predictions [citation:RoboWM-Bench](https://arxiv.org/abs/2604.19092v2). The reviewed literature collectively points toward future directions including memory mechanisms, multi-sensory integration, efficient adaptation, and multi-agent coordination.

---

## Introduction

Robotic manipulation remains one of the most challenging domains in embodied AI, requiring precise motor control, multimodal perception, and robust physical reasoning [citation:Survey-VLA](https://arxiv.org/abs/2508.13073v3). Traditional approaches relying on rule-based methods or direct imitation learning face fundamental limitations in generalization and scalability when deployed in unstructured environments. World models—internal representations that predict future states given current observations and actions—offer a promising solution by enabling robots to "imagine" outcomes before executing actions in the physical world.

The emergence of large-scale vision-language models and diffusion generative models has catalyzed rapid advances in world model capabilities. Recent work demonstrates that world models can serve multiple functions simultaneously: as simulators for policy training, as planners for trajectory optimization, and as evaluation tools for assessing physical consistency. However, the field lacks systematic benchmarks for evaluating whether world model predictions translate into executable robotic actions, highlighting the need for embodiment-grounded assessment frameworks.

This review systematically analyzes ten papers published within a two-year window to identify architectural trends, methodological innovations, and empirical advances in world models for robotic manipulation. The analysis reveals a clear progression from purely visual prediction models toward physics-grounded, multi-sensory representations that explicitly reason about 3D geometry and contact dynamics.

---

## Methodology

This systematic literature review followed a structured search protocol using arXiv's academic database. Search criteria were defined as follows:

- **Query terms:** "world models robotic manipulation" (phrase match with all terms)
- **Publication date range:** May 27, 2024 to May 26, 2026
- **Primary category:** cs.RO (Robotics)
- **Maximum results:** 10 papers
- **Format:** APA citation style

The search returned exactly ten papers matching the criteria, which were retrieved and analyzed for thematic clustering, methodological contributions, and empirical results. Papers were categorized based on their primary technical approach: geometry-enhanced models, data platform contributions, survey/taxonomy papers, diffusion-based approaches, and benchmarking frameworks.

---

## Thematic Analysis

### Theme 1: Geometry-Enhanced Video World Models

#### GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation

Zhou et al. (2026) address a critical limitation in video world models: the failure to track physical points consistently across time, resulting in plausible but physically inconsistent predictions. Their proposed GEM-4D framework injects dense 4D correspondence supervision distilled from pretrained geometry foundation models into the video generative backbone during training.

**Technical Approach:** The model employs a single-stream architecture that jointly captures appearance and geometric structure without additional inference costs. An inverse dynamics module converts correspondence-consistent video rollouts into executable robot trajectories, enabling direct deployment in both simulated and real-world manipulation scenarios.

**Results:** GEM-4D achieves state-of-the-art performance on video prediction and geometric consistency metrics across simulation and realistic scenarios. Critically, real-world manipulation success rates improved from 61% to 81%, demonstrating substantial practical benefits of geometry grounding [citation:GEM-4D](https://arxiv.org/abs/2605.22882v4).

#### GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

Lu et al. (2025) propose Gaussian World Model (GWM), a novel branch of world models that reconstructs future states by inferring the propagation of Gaussian primitives under robot action effects. This approach addresses the limitation of image-based world models in providing robust geometric information for consistent spatial and physical understanding.

**Technical Approach:** GWM combines a latent Diffusion Transformer (DiT) with a 3D variational autoencoder, enabling fine-grained scene-level future state reconstruction using Gaussian Splatting. The model serves dual purposes: enhancing visual representation for imitation learning through self-supervised future prediction, and functioning as a neural simulator supporting model-based reinforcement learning.

**Results:** Experiments demonstrate that GWM precisely predicts future scenes conditioned on diverse robot actions. Policies trained using GWM as a simulator outperform state-of-the-art methods by impressive margins, showcasing initial data scaling potential of 3D world models [citation:GWM](https://arxiv.org/abs/2508.17600v2).

#### Camera Depth Models: Enabling Accurate Geometry Perception

Liu et al. (2025) tackle the challenge of depth camera noise and limited accuracy in real-world manipulation tasks. Their Camera Depth Models (CDMs) function as a simple plugin for daily-use depth cameras, taking RGB images and raw depth signals as input to output denoised, accurate metric depth.

**Technical Approach:** The authors develop a neural data engine that generates high-quality paired data from simulation by modeling depth camera noise patterns. This enables training CDMs to achieve nearly simulation-level accuracy in depth prediction, effectively bridging the sim-to-real gap.

**Results:** Remarkably, policies trained on raw simulated depth without noise addition or real-world fine-tuning generalize seamlessly to real-world robots on challenging long-horizon tasks involving articulated, reflective, and slender objects, with little to no performance degradation [citation:CDM](https://arxiv.org/abs/2509.02530v1).

---

### Theme 2: Large-Scale Data Platforms and Generalist Policies

#### AgiBot World Colosseo: A Large-scale Manipulation Platform

AgiBot World Contributors et al. (2025) introduce AgiBot World Colosseo, a large-scale platform comprising over 1 million trajectories across 217 tasks in five deployment scenarios. This represents an order-of-magnitude increase in data scale compared to existing datasets.

**Technical Approach:** The platform employs a standardized collection pipeline with human-in-the-loop verification to guarantee high-quality and diverse data distribution. Built on this dataset is Genie Operator-1 (GO-1), a novel generalist policy leveraging latent action representations to maximize data utilization.

**Results:** Policies pre-trained on the AgiBot World dataset achieve an average performance improvement of 30% over Open X-Embodiment baselines in both in-domain and out-of-distribution scenarios. GO-1 exhibits exceptional capability in real-world dexterous and long-horizon tasks, achieving over 60% success rate on complex tasks and outperforming prior RDT approaches by 32% [citation:AgiBot](https://arxiv.org/abs/2503.06669v5).

---

### Theme 3: Survey and Taxonomy Contributions

#### Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey

Shao et al. (2025) provide the first systematic, taxonomy-oriented review of large Vision-Language-Model-based Vision-Language-Action (VLA) models for robotic manipulation. This survey consolidates research at the intersection of large VLMs and robotic manipulation, resolving inconsistencies in existing taxonomies.

**Taxonomic Framework:** The authors delineate two principal architectural paradigms: (1) monolithic models encompassing single-system and dual-system designs with differing integration levels, and (2) hierarchical models that explicitly decouple planning from execution via interpretable intermediate representations.

**Integration Domains:** The survey examines integration with advanced domains including reinforcement learning, training-free optimization, learning from human videos, and world model integration. Promising future directions identified include memory mechanisms, 4D perception, efficient adaptation, multi-agent cooperation, and emerging capabilities [citation:Survey-VLA](https://arxiv.org/abs/2508.13073v3).

---

### Theme 4: Reinforcement Learning with World Models

#### World-Gymnast: Training Robots with Reinforcement Learning in a World Model

Sharma et al. (2026) investigate whether training policies in world models can outperform both supervised fine-tuning from expert demonstrations and reinforcement learning in software simulators. They propose World-Gymnast, which performs RL fine-tuning of a vision-language-action policy by rolling out the policy in an action-conditioned video world model and rewarding rollouts with a vision-language model.

**Technical Innovation:** The framework enables training on diverse language instructions and novel scenes from the world model, test-time training in novel scenes, and online iterative world model and policy improvement.

**Results:** On the Bridge robot setup, World-Gymnast outperforms supervised fine-tuning by as much as 18× and software simulators by as much as 2×. These results suggest that learning world models and training robot policies in the cloud could be key to bridging the gap between demonstration-working robots and household-ready systems [citation:World-Gymnast](https://arxiv.org/abs/2602.02454v1).

#### World4RL: Diffusion World Models for Policy Refinement

Jiang et al. (2025) propose World4RL, a framework employing diffusion-based world models as high-fidelity simulators to refine pre-trained policies entirely in imagined environments. Unlike prior works primarily using world models for planning, World4RL enables direct end-to-end policy optimization.

**Technical Design:** The framework operates on two principles: (1) pre-training a diffusion world model capturing diverse dynamics on multi-task datasets, and (2) refining policies entirely within a frozen world model to avoid online real-world interactions. A two-hot action encoding scheme tailored for robotic manipulation improves modeling fidelity.

**Results:** Extensive simulation and real-world experiments demonstrate that World4RL provides high-fidelity environment modeling and enables consistent policy refinement, yielding significantly higher success rates compared to imitation learning and other baselines [citation:World4RL](https://arxiv.org/abs/2509.19080v2).

---

### Theme 5: Multisensory Integration and Forecasting

#### MLA: A Multisensory Language-Action Model for Multimodal Understanding

Liu et al. (2025) address the gap between vision-language-action models that interpret vision and language to generate actions, and the need for comprehensive understanding of multisensory information crucial for complex and contact-rich control.

**Technical Innovation:** The Multisensory Language-Action (MLA) model collaboratively perceives heterogeneous sensory modalities and predicts future multisensory objectives to facilitate physical world modeling. Key innovations include an encoder-free multimodal alignment scheme that repurposes the large language model itself as a perception module, directly interpreting 2D images, 3D point clouds, and tactile tokens through positional correspondence.

**Future Generation Strategy:** A future multisensory generation post-training strategy enables MLA to reason about semantic, geometric, and interaction information, providing more robust conditions for action generation.

**Results:** The MLA model outperforms previous state-of-the-art 2D and 3D VLA methods by 12% and 24% in complex, contact-rich real-world tasks, respectively, while demonstrating improved generalization to unseen configurations [citation:MLA](https://arxiv.org/abs/2509.26642v2).

---

### Theme 6: Benchmarking and Evaluation

#### RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation

Jiang et al. (2026) introduce RoboWM-Bench, a manipulation-centric benchmark for embodiment-grounded evaluation of video world models. The benchmark addresses a critical gap: existing evaluations assess visual quality and physical plausibility but do not systematically evaluate whether predicted behaviors translate into executable actions.

**Evaluation Framework:** RoboWM-Bench converts generated human-hand and robotic manipulation videos into embodied action sequences and validates them through execution in physically grounded simulation environments. Built on real-to-sim scene reconstruction and diverse manipulation tasks, it enables standardized, reproducible, and scalable evaluation of physical executability.

**Key Findings:** Evaluations reveal that visual plausibility and embodied executability are not always aligned. Analysis highlights recurring factors affecting execution performance, including spatial reasoning, contact prediction, and non-physical geometric distortions, particularly in complex and long-horizon interactions [citation:RoboWM-Bench](https://arxiv.org/abs/2604.19092v2).

---

### Theme 7: Sim-to-Real Transfer via Diffusion

#### RealD²iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion

Liang et al. (2025) address the visual sim2real gap in robot manipulation, where depth observations collected in simulation fail to reflect complex noise patterns inherent to real sensors. Inspired by diffusion model denoising capabilities, they invert the conventional perspective to propose a clean-to-noisy paradigm.

**Technical Approach:** RealD²iff is a hierarchical coarse-to-fine diffusion framework decomposing depth noise into global structural distortions and fine-grained local perturbations. Two complementary strategies enable progressive learning: Frequency-Guided Supervision (FGS) for global structure modeling and Discrepancy-Guided Optimization (DGO) for localized refinement.

**Applications:** The framework enables two key applications: (1) generating real-world-like depth to construct clean-noisy paired datasets without manual sensor data collection, and (2) achieving zero-shot sim2real robot manipulation with substantially improved real-world performance without additional fine-tuning [citation:RealD2diff](https://arxiv.org/abs/2511.22505v2).

---

## Cross-Cutting Insights

### Architectural Trends

The reviewed literature reveals several converging architectural patterns:

1. **Single-stream efficiency:** Multiple works (GEM-4D, MLA) demonstrate that carefully designed single-stream architectures can capture complex multimodal representations without additional inference costs.

2. **Diffusion backbone dominance:** Both GWM and World4RL leverage diffusion transformers as core components, reflecting the broader trend toward diffusion models for high-fidelity temporal and spatial prediction.

3. **3D representation integration:** Three distinct approaches (Gaussian Splatting in GWM, 4D correspondences in GEM-4D, Camera Depth Models) emphasize the critical importance of explicit 3D geometric reasoning for reliable manipulation.

### Methodological Innovations

Several methodological breakthroughs emerge:

1. **Inverse dynamics conversion:** GEM-4D's innovation of converting correspondence-consistent video rollouts directly into executable trajectories represents a novel bridge between video prediction and action execution.

2. **Encoder-free multimodal alignment:** MLA's repurposing of LLMs as perception modules eliminates traditional encoder bottlenecks while maintaining alignment across heterogeneous modalities.

3. **Clean-to-noisy paradigm inversion:** RealD²iff's counterintuitive approach of learning to synthesize noise rather than remove it fundamentally reframes the sim2real problem.

### Empirical Performance Patterns

Performance improvements across studies show consistent patterns:

- **Geometry grounding yields substantial gains:** From 61% to 81% success rate improvement (GEM-4D) and 30% overall improvement over baseline datasets (AgiBot World)
- **RL in world models scales dramatically:** Up to 18× improvement over supervised fine-tuning (World-Gymnast)
- **Multisensory integration improves complex tasks:** 12-24% improvements in contact-rich scenarios (MLA)

---

## Critical Discussion

### Strengths and Achievements

The reviewed literature demonstrates remarkable progress in addressing long-standing challenges in robotic manipulation:

1. **Physical consistency:** Geometry-enhanced world models successfully address the fundamental issue of temporally consistent physical tracking that plagued earlier video-based approaches.

2. **Data efficiency:** Large-scale platforms and world model-based training significantly reduce dependence on expensive real-world data collection, with some approaches achieving zero-shot sim2real transfer.

3. **Scalability evidence:** AgiBot World and related works provide empirical evidence of predictable scaling laws for generalist policies with increased data volume.

### Persistent Challenges

Despite significant advances, several critical challenges remain:

1. **Embodied executability gap:** RoboWM-Bench findings reveal that visual plausibility and embodied executability are not always aligned, indicating that world models may still produce physically implausible predictions despite appearing realistic.

2. **Complex interaction modeling:** Contact-rich scenarios and long-horizon tasks continue to present difficulties, particularly for models lacking explicit physical reasoning capabilities.

3. **Generalization boundaries:** While improvements are substantial, out-of-distribution generalization remains limited compared to human adaptability.

### Limitations of Current Approaches

Several limitations constrain current world model approaches:

1. **Computational complexity:** High-fidelity 3D world models require substantial computational resources, potentially limiting real-time applicability.

2. **Sensor modality constraints:** Most approaches rely heavily on vision and depth, with tactile and proprioceptive integration remaining nascent despite its importance for contact-rich manipulation.

3. **Evaluation fragmentation:** Despite RoboWM-Bench's introduction, standardized evaluation protocols remain fragmented, hindering fair comparison across approaches.

---

## Future Research Directions

Based on the systematic analysis, several promising research directions emerge:

### Technical Directions

1. **Memory-augmented world models:** Survey literature identifies memory mechanisms as a critical next step for handling long-horizon tasks and accumulating experience.

2. **Multi-agent coordination:** Emerging capabilities for multi-agent cooperation represent an important frontier for scalable robotic systems.

3. **Efficient adaptation:** Methods for rapid domain adaptation and few-shot learning will be essential for deploying world models in diverse real-world environments.

4. **4D perception integration:** Combining spatiotemporal perception with world model prediction promises enhanced physical reasoning capabilities.

### Methodological Directions

1. **Hybrid simulation-reality training:** Approaches that seamlessly integrate simulated and real-world data during training could further close the sim2real gap.

2. **Causal reasoning integration:** Incorporating causal structures into world models may improve physical intuition and counterfactual reasoning.

3. **Unified multimodal frameworks:** Developing truly unified models that natively process all relevant sensor modalities without separate encoders could simplify architectures and improve performance.

### Application Directions

1. **Household deployment:** The ultimate goal of bringing robots capable of working in arbitrary households requires continued advances in generalization and robustness.

2. **Industrial automation:** Scalable world models offer particular promise for flexible manufacturing and assembly tasks requiring rapid adaptation to new products.

3. **Human-robot collaboration:** World models that understand human intentions and predict human actions will be critical for safe and effective collaboration.

---

## Conclusion

This systematic literature review of ten papers on world models for robotic manipulation reveals a rapidly evolving field characterized by significant architectural and methodological advances. The convergence of geometry-enhanced representations, diffusion-based modeling, large-scale data platforms, and embodiment-grounded evaluation frameworks indicates maturing capabilities in physical reasoning and action prediction.

Key achievements include substantial improvements in manipulation success rates (up to 18× over baselines), effective sim2real transfer approaches, and empirical evidence of scaling laws for generalist policies. However, persistent challenges around embodied executability, complex interaction modeling, and generalization boundaries suggest substantial opportunities for future research.

The reviewed works collectively point toward a future where world models serve as central components in robotic systems, enabling efficient learning, robust planning, and seamless real-world deployment. Continued progress in this domain will depend on addressing the identified challenges while pursuing the highlighted research directions, ultimately advancing toward robots capable of reliable, adaptable manipulation in diverse real-world environments.

---

## References

AgiBot World Contributors, Bu, Q., Cai, J., Chen, L., Cui, X., Ding, Y., ... & Luo, J. (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. *arXiv preprint arXiv:2503.06669*. https://arxiv.org/abs/2503.06669v5

Jiang, F., Chen, Y., Xu, K., Liu, Y., Wang, H., Shen, Z., ... & Wu, R. (2026). RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation. *arXiv preprint arXiv:2604.19092*. https://arxiv.org/abs/2604.19092v2

Jiang, Z., Liu, K., Qin, Y., Tian, S., Zheng, Y., Zhou, M., ... & Zhao, D. (2025). World4RL: Diffusion world models for policy refinement with reinforcement learning for robotic manipulation. *arXiv preprint arXiv:2509.19080*. https://arxiv.org/abs/2509.19080v2

Li, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD²iff: Bridging real-world gap in robot manipulation via depth diffusion. *arXiv preprint arXiv:2511.22505*. https://arxiv.org/abs/2511.22505v2

Liu, Z., Liu, J., Xu, J., Han, N., Gu, C., Chen, H., ... & Zhang, S. (2025). MLA: A multisensory language-action model for multimodal understanding and forecasting in robotic manipulation. *arXiv preprint arXiv:2509.26642*. https://arxiv.org/abs/2509.26642v2

Liu, M., Zhu, Z., Han, X., Hu, P., Lin, H., Li, X., ... & Kang, B. (2025). Manipulation as in simulation: Enabling accurate geometry perception in robots. *arXiv preprint arXiv:2509.02530*. https://arxiv.org/abs/2509.02530v1

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. *arXiv preprint arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). Large VLM-based vision-language-action models for robotic manipulation: A survey. *arXiv preprint arXiv:2508.13073*. https://arxiv.org/abs/2508.13073v3

Sharma, A. K., Sun, Y., Lu, N., Zhang, Y., Liu, J., & Yang, S. (2026). World-Gymnast: Training robots with reinforcement learning in a world model. *arXiv preprint arXiv:2602.02454*. https://arxiv.org/abs/2602.02454v1

Zhou, K., Chen, Y., Zhan, F., Hua, H., Chen, G., Chang, X., ... & Wang, M. (2026). GEM-4D: Geometry-enhanced video world models for robot manipulation. *arXiv preprint arXiv:2605.22882*. https://arxiv.org/abs/2605.22882v4
