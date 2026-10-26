# Systematic Literature Review: World Models for Robotic Manipulation

**Review Period:** May 27, 2024 – May 26, 2026  
**Category:** cs.RO (Robotics)  
**Total Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in world models for robotic manipulation published between May 2024 and May 2026. The field has experienced significant growth, with research focusing on three primary directions: (1) Gaussian and diffusion-based world models for high-fidelity scene prediction, (2) integration of world models with reinforcement learning and vision-language-action architectures, and (3) benchmarking and evaluation frameworks for embodied AI systems. Key findings indicate that world models trained on real-world data can bridge the sim-to-real gap, enable policy refinement without physical interaction, and support complex long-horizon manipulation tasks.

---

## Annotated Bibliography (APA Format)

### 1. AgiBot World Platform and Scalable Data Collection

**Citation:**  
AgiBot World Contributors, Bu, Q., Cai, J., Chen, L., Cui, X., Ding, Y., Feng, S., Gao, S., He, X., Hu, X., Huang, X., Jiang, S., Jiang, Y., Jing, C., Li, H., Li, J., Liu, C., Liu, Y., Lu, Y., & Luo, J. (2025). *AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems*. arXiv:2503.06669. https://arxiv.org/abs/2503.06669v5

**Summary:**  
This paper introduces AgiBot World, a large-scale robotic manipulation platform comprising over 1 million trajectories across 217 tasks in five deployment scenarios. The platform achieves an order-of-magnitude increase in data scale compared to existing datasets through a standardized collection pipeline with human-in-the-loop verification. The authors propose Genie Operator-1 (GO-1), a generalist policy leveraging latent action representations that demonstrates predictable performance scaling with increased data volume. Policies pre-trained on this dataset achieve 30% average performance improvement over Open X-Embodiment baselines, with over 60% success rate on complex dexterous and long-horizon tasks.

**Key Contributions:**
- Largest-scale robotic manipulation dataset (1M+ trajectories)
- Novel generalist policy architecture (GO-1) with latent action representations
- Demonstrates 32% improvement over prior RDT approaches
- Open-source dataset, tools, and models for community access

**Relevance to World Models:**  
Provides foundational data infrastructure for training world models at scale, demonstrating that data quantity and quality directly correlate with policy generalization capabilities.

---

### 2. VLM-based Vision-Language-Action Models Survey

**Citation:**  
Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). *Large VLM-based vision-language-action models for robotic manipulation: A survey*. arXiv:2508.13073. https://arxiv.org/abs/2508.13073v3

**Summary:**  
This comprehensive survey provides the first systematic, taxonomy-oriented review of large VLM-based VLA models for robotic manipulation. The authors delineate two principal architectural paradigms: (1) monolithic models (single-system and dual-system designs) and (2) hierarchical models (decoupling planning from execution via interpretable intermediate representations). The survey examines integration with advanced domains including reinforcement learning, training-free optimization, learning from human videos, and world model integration. Promising future directions identified include memory mechanisms, 4D perception, efficient adaptation, and multi-agent cooperation.

**Key Contributions:**
- First systematic taxonomy of VLM-based VLA models
- Comprehensive analysis of architectural paradigms
- Integration pathways with world models identified
- Project page for ongoing progress tracking: https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation

**Relevance to World Models:**  
Identifies world model integration as a critical advanced domain for VLA systems, providing architectural frameworks for combining language-action models with predictive world representations.

---

### 3. Gaussian World Models (GWM)

**Citation:**  
Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). *GWM: Towards scalable Gaussian world models for robotic manipulation*. arXiv:2508.17600. https://arxiv.org/abs/2508.17600v2

**Summary:**  
This paper proposes Gaussian World Model (GWM), a novel branch of world models that reconstructs future states by inferring the propagation of Gaussian primitives under robot actions. The architecture combines a latent Diffusion Transformer (DiT) with a 3D variational autoencoder, enabling fine-grained scene-level future state reconstruction with Gaussian Splatting. Unlike image-based world models, GWM provides robust geometric information requiring consistent spatial and physical understanding of the 3D world. The model serves dual purposes: enhancing visual representation for imitation learning through self-supervised future prediction training, and functioning as a neural simulator for model-based reinforcement learning.

**Key Contributions:**
- First Gaussian Splatting-based world model for robotics
- Combines DiT with 3D VAE for geometric consistency
- Outperforms state-of-the-art methods by significant margins
- Demonstrates data scaling potential of 3D world models

**Relevance to World Models:**  
Represents a paradigm shift from 2D image-based to 3D geometric world models, addressing critical limitations in spatial reasoning and physical consistency for manipulation tasks.

---

### 4. World-Gymnast: RL Training in World Models

**Citation:**  
Sharma, A. K., Sun, Y., Lu, N., Zhang, Y., Liu, J., & Yang, S. (2026). *World-Gymnast: Training robots with reinforcement learning in a world model*. arXiv:2602.02454. https://arxiv.org/abs/2602.02454v1

**Summary:**  
World-Gymnast addresses the fundamental bottleneck of physical interaction costs in robot learning by performing RL finetuning of VLA policies through rollout in an action-conditioned video world model, with rewards assessed by a vision-language model. On the Bridge robot setup, World-Gymnast outperforms supervised finetuning by 18x and software simulators by 2x. The framework demonstrates emergent capabilities including training on diverse language instructions, novel scene generalization, test-time training, and online iterative world model and policy improvement.

**Key Contributions:**
- RL finetuning entirely within learned world models
- VLM-based reward assessment for imagined rollouts
- 18x improvement over supervised learning baselines
- Test-time training and online iterative improvement capabilities

**Relevance to World Models:**  
Demonstrates that world models can serve as effective training environments for RL, potentially eliminating the sim-to-real gap and enabling cloud-based robot policy training.

---

### 5. RealD²iff: Depth Diffusion for Sim-to-Real Gap

**Citation:**  
Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). *RealD²iff: Bridging real-world gap in robot manipulation via depth diffusion*. arXiv:2511.22505. https://arxiv.org/abs/2511.22505v2

**Summary:**  
This work addresses the visual sim-to-real gap in robot manipulation through a clean-to-noisy diffusion paradigm that learns to synthesize realistic depth sensor noise. RealD²iff employs a hierarchical coarse-to-fine diffusion framework decomposing depth noise into global structural distortions and fine-grained local perturbations. The framework includes Frequency-Guided Supervision (FGS) for global structure modeling and Discrepancy-Guided Optimization (DGO) for localized refinement. Applications include generating real-world-like depth datasets without manual sensor collection and achieving zero-shot sim-to-real robot manipulation.

**Key Contributions:**
- Novel clean-to-noisy diffusion paradigm for depth synthesis
- Hierarchical decomposition of depth noise patterns
- Zero-shot sim-to-real transfer without fine-tuning
- Six-stage pipeline for seamless imitation learning integration

**Relevance to World Models:**  
Provides complementary technology for world models by enabling realistic depth simulation, critical for 3D perception and geometric reasoning in manipulation tasks.

---

### 6. MLA: Multisensory Language-Action Model

**Citation:**  
Liu, Z., Liu, J., Xu, J., Han, N., Gu, C., Chen, H., Zhou, K., Zhang, R., Hsieh, K. C., Wu, K., Che, Z., Tang, J., & Zhang, S. (2025). *MLA: A multisensory language-action model for multimodal understanding and forecasting in robotic manipulation*. arXiv:2509.26642. https://arxiv.org/abs/2509.26642v2

**Summary:**  
The Multisensory Language-Action (MLA) model extends beyond vision-language-action frameworks by collaboratively perceiving heterogeneous sensory modalities and predicting future multisensory objectives for physical world modeling. The encoder-free multimodal alignment scheme repurposes the LLM itself as a perception module, directly interpreting 2D images, 3D point clouds, and tactile tokens through positional correspondence. A future multisensory generation post-training strategy enables reasoning about semantic, geometric, and interaction information. MLA outperforms state-of-the-art 2D and 3D VLA methods by 12% and 24% respectively in complex, contact-rich real-world tasks.

**Key Contributions:**
- Encoder-free multimodal alignment using LLM as perception module
- Future multisensory generation for physical dynamics understanding
- Superior performance in contact-rich manipulation tasks
- Integration of tactile, visual, and geometric representations

**Relevance to World Models:**  
Advances world modeling by incorporating multisensory prediction capabilities, enabling comprehensive physical world understanding beyond visual prediction alone.

---

### 7. RoboWM-Bench: World Model Evaluation Benchmark

**Citation:**  
Jiang, F., Chen, Y., Xu, K., Liu, Y., Wang, H., Shen, Z., Lu, J., Huang, S., Wang, Y., Xie, C., & Wu, R. (2026). *RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation*. arXiv:2604.19092. https://arxiv.org/abs/2604.19092v2

**Summary:**  
RoboWM-Bench introduces a manipulation-centric benchmark for embodiment-grounded evaluation of video world models. The benchmark converts generated human-hand and robotic manipulation videos into embodied action sequences, validating them through execution in physically grounded simulation environments. Built on real-to-sim scene reconstruction and diverse manipulation tasks, RoboWM-Bench enables standardized evaluation of physical executability. Analysis reveals that visual plausibility and embodied executability are not always aligned, with recurring failure factors including spatial reasoning errors, contact prediction failures, and non-physical geometric distortions.

**Key Contributions:**
- First benchmark for embodied executability of world model predictions
- Real-to-sim scene reconstruction pipeline
- Reveals misalignment between visual quality and physical consistency
- Standardized, reproducible evaluation framework

**Relevance to World Models:**  
Provides critical evaluation infrastructure for world model research, highlighting the gap between perceptual realism and physical executability in manipulation contexts.

---

### 8. World4RL: Diffusion World Models for Policy Refinement

**Citation:**  
Jiang, Z., Liu, K., Qin, Y., Tian, S., Zheng, Y., Zhou, M., Yu, C., Li, H., & Zhao, D. (2025). *World4RL: Diffusion world models for policy refinement with reinforcement learning for robotic manipulation*. arXiv:2509.19080. https://arxiv.org/abs/2509.19080v2

**Summary:**  
World4RL employs diffusion-based world models as high-fidelity simulators to refine pre-trained policies entirely in imagined environments. Unlike prior works using world models primarily for planning, this framework enables direct end-to-end policy optimization. The approach involves pre-training a diffusion world model on multi-task datasets capturing diverse dynamics, then refining policies entirely within a frozen world model to avoid online real-world interactions. A two-hot action encoding scheme tailored for robotic manipulation and diffusion backbones improve modeling fidelity. Extensive experiments demonstrate consistent policy refinement with significantly higher success rates compared to imitation learning baselines.

**Key Contributions:**
- End-to-end policy optimization within frozen diffusion world models
- Two-hot action encoding for robotic manipulation
- Eliminates need for online real-world RL training
- Consistent improvement over imitation learning initialization

**Relevance to World Models:**  
Demonstrates practical application of diffusion world models as training environments, addressing safety and cost concerns of real-world RL while avoiding sim-to-real transfer issues.

---

### 9. Camera Depth Models for Simulation-Level Accuracy

**Citation:**  
Liu, M., Zhu, Z., Han, X., Hu, P., Lin, H., Li, X., Chen, J., Xu, J., Yang, Y., Lin, Y., Li, X., Yu, Y., Zhang, W., Kong, T., & Kang, B. (2025). *Manipulation as in simulation: Enabling accurate geometry perception in robots*. arXiv:2509.02530. https://arxiv.org/abs/2509.02530v1

**Summary:**  
This work addresses the challenge of using depth cameras for manipulation by proposing Camera Depth Models (CDMs) as plugins for daily-use depth cameras. CDMs take RGB images and raw depth signals as input, outputting denoised, accurate metric depth. A neural data engine generates high-quality paired data from simulation by modeling depth camera noise patterns. Results show CDMs achieve nearly simulation-level accuracy in depth prediction, enabling policies trained on raw simulated depth to generalize seamlessly to real-world robots on challenging long-horizon tasks involving articulated, reflective, and slender objects with minimal performance degradation.

**Key Contributions:**
- Neural data engine for depth camera noise modeling
- Simulation-level depth accuracy from commodity sensors
- Zero-shot sim-to-real transfer on complex manipulation tasks
- First demonstration of raw simulated depth policy generalization

**Relevance to World Models:**  
Provides critical perception infrastructure for world models by enabling accurate 3D geometric input, essential for physical reasoning and spatial prediction in manipulation.

---

### 10. Comprehensive Survey on World Models in Robotics

**Citation:**  
Zhang, P.-F., Cheng, Y., Sun, X., Wang, S., Li, F., Zhu, L., & Shen, H. T. (2025). *A step toward world models: A survey on robotic manipulation*. arXiv:2511.02097. https://arxiv.org/abs/2511.02097v2

**Summary:**  
This survey examines approaches exhibiting core world model capabilities in robotic manipulation, going beyond methods explicitly labeled as world models. The analysis covers perception, prediction, and control roles, identifying key challenges and solutions. The authors distill core components, capabilities, and functions that fully realized world models should possess, aiming to motivate development toward generalizable and practical world models for robotics. The survey addresses ambiguity in world model definitions, scope, architectures, and essential capabilities across the field.

**Key Contributions:**
- Comprehensive analysis of world model capabilities beyond explicit labeling
- Framework for perception, prediction, and control integration
- Identification of core components for practical world models
- Roadmap for generalizable world model development

**Relevance to World Models:**  
Provides conceptual foundation and unified framework for understanding world models in robotics, clarifying definitions and identifying critical research directions.

---

## Thematic Analysis

### Theme 1: 3D Geometric World Models

Three papers (Lu et al., 2025; Liang et al., 2025; Liu et al., 2025) emphasize the critical importance of 3D geometric reasoning over 2D image-based prediction. GWM (Lu et al.) introduces Gaussian Splatting for scene-level reconstruction, while RealD²iff (Liang et al.) and CDMs (Liu et al.) address depth perception challenges. This represents a paradigm shift recognizing that manipulation requires consistent spatial and physical understanding.

### Theme 2: World Models as Training Environments

Four papers (Sharma et al., 2026; Jiang et al., 2025; Sharma et al., 2026; Jiang et al., 2026) demonstrate world models functioning as neural simulators for policy training. World-Gymnast and World4RL show that RL training within learned world models can outperform both supervised learning and traditional software simulators, potentially eliminating the sim-to-real gap.

### Theme 3: Multisensory Integration

Two papers (Liu et al., 2025; Shao et al., 2025) highlight the need for integrating multiple sensory modalities beyond vision. MLA (Liu et al.) incorporates tactile and 3D point cloud information, while the VLA survey (Shao et al.) identifies multisensory perception as a critical future direction.

### Theme 4: Evaluation and Benchmarking

The emergence of RoboWM-Bench (Jiang et al., 2026) and AgiBot World (AgiBot World Contributors, 2025) reflects the field's maturation, providing standardized evaluation frameworks and large-scale datasets necessary for reproducible research and fair comparison.

---

## Key Findings

1. **Data Scale Matters:** AgiBot World demonstrates that order-of-magnitude increases in data scale (1M+ trajectories) yield predictable performance improvements, suggesting world models benefit from massive datasets.

2. **3D Over 2D:** Multiple works converge on the conclusion that 3D geometric representations (Gaussian primitives, depth maps, point clouds) outperform 2D image-based prediction for manipulation tasks.

3. **RL in World Models Works:** World-Gymnast's 18x improvement over supervised learning and 2x improvement over software simulators validates world models as effective training environments.

4. **Sim-to-Real Gap Closing:** RealD²iff, CDMs, and World4RL all demonstrate zero-shot or near zero-shot sim-to-real transfer, suggesting world models can eliminate traditional transfer learning requirements.

5. **Physical Executability ≠ Visual Realism:** RoboWM-Bench reveals that visually plausible predictions often fail physical consistency checks, highlighting the need for embodiment-aware evaluation.

6. **Multisensory Prediction:** MLA's superior performance in contact-rich tasks (12-24% improvement) demonstrates that predicting future tactile and geometric states enhances manipulation capabilities.

---

## Research Gaps and Future Directions

### Identified Gaps:

1. **Long-Horizon Prediction:** Current world models struggle with accurate prediction beyond short time horizons, limiting applicability to complex multi-stage tasks.

2. **Computational Efficiency:** Gaussian and diffusion-based models require significant computational resources, limiting real-time deployment on embodied systems.

3. **Generalization to Novel Objects:** Most models demonstrate in-distribution performance; out-of-distribution generalization to unseen object categories remains challenging.

4. **Contact Physics Modeling:** While visual prediction has advanced, accurate modeling of contact dynamics, friction, and deformable objects remains limited.

5. **Multi-Agent Coordination:** No papers address world models for multi-robot collaboration, a critical capability for industrial and household applications.

### Promising Directions:

1. **Hybrid Architectures:** Combining Gaussian representations for geometry with diffusion models for texture and dynamics may leverage complementary strengths.

2. **Memory Mechanisms:** The VLA survey identifies memory as a critical missing component for long-horizon task understanding and execution.

3. **4D Perception:** Incorporating temporal dynamics explicitly into world model representations may improve prediction accuracy and physical consistency.

4. **Efficient Adaptation:** Developing methods for rapid world model adaptation to new environments with minimal data collection.

5. **Embodiment-Aware Training:** RoboWM-Bench findings suggest training world models with explicit physical executability constraints rather than post-hoc evaluation.

---

## Conclusion

The literature from 2024-2026 demonstrates rapid maturation of world models for robotic manipulation, with convergence on several key principles: 3D geometric representations, multisensory integration, and world models as training environments. The field has moved beyond proof-of-concept demonstrations to systematic benchmarking and large-scale data collection. Critical challenges remain in long-horizon prediction, computational efficiency, and contact physics modeling, but the trajectory suggests world models will become foundational infrastructure for general-purpose robotic manipulation systems.

The emergence of evaluation benchmarks (RoboWM-Bench) and large-scale platforms (AgiBot World) indicates the field is transitioning from exploratory research to engineering discipline, with standardized methodologies and reproducible results. Future work should prioritize physical consistency over visual realism, develop efficient architectures for real-time deployment, and address multi-agent coordination scenarios.

---

## References

AgiBot World Contributors, Bu, Q., Cai, J., Chen, L., Cui, X., Ding, Y., Feng, S., Gao, S., He, X., Hu, X., Huang, X., Jiang, S., Jiang, Y., Jing, C., Li, H., Li, J., Liu, C., Liu, Y., Lu, Y., & Luo, J. (2025). AgiBot World Colosseo: A large-scale manipulation platform for scalable and intelligent embodied systems. *arXiv:2503.06669*. https://arxiv.org/abs/2503.06669v5

Jiang, F., Chen, Y., Xu, K., Liu, Y., Wang, H., Shen, Z., Lu, J., Huang, S., Wang, Y., Xie, C., & Wu, R. (2026). RoboWM-Bench: A benchmark for evaluating world models in robotic manipulation. *arXiv:2604.19092*. https://arxiv.org/abs/2604.19092v2

Jiang, Z., Liu, K., Qin, Y., Tian, S., Zheng, Y., Zhou, M., Yu, C., Li, H., & Zhao, D. (2025). World4RL: Diffusion world models for policy refinement with reinforcement learning for robotic manipulation. *arXiv:2509.19080*. https://arxiv.org/abs/2509.19080v2

Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD²iff: Bridging real-world gap in robot manipulation via depth diffusion. *arXiv:2511.22505*. https://arxiv.org/abs/2511.22505v2

Liu, M., Zhu, Z., Han, X., Hu, P., Lin, H., Li, X., Chen, J., Xu, J., Yang, Y., Lin, Y., Li, X., Yu, Y., Zhang, W., Kong, T., & Kang, B. (2025). Manipulation as in simulation: Enabling accurate geometry perception in robots. *arXiv:2509.02530*. https://arxiv.org/abs/2509.02530v1

Liu, Z., Liu, J., Xu, J., Han, N., Gu, C., Chen, H., Zhou, K., Zhang, R., Hsieh, K. C., Wu, K., Che, Z., Tang, J., & Zhang, S. (2025). MLA: A multisensory language-action model for multimodal understanding and forecasting in robotic manipulation. *arXiv:2509.26642*. https://arxiv.org/abs/2509.26642v2

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. *arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). Large VLM-based vision-language-action models for robotic manipulation: A survey. *arXiv:2508.13073*. https://arxiv.org/abs/2508.13073v3

Sharma, A. K., Sun, Y., Lu, N., Zhang, Y., Liu, J., & Yang, S. (2026). World-Gymnast: Training robots with reinforcement learning in a world model. *arXiv:2602.02454*. https://arxiv.org/abs/2602.02454v1

Zhang, P.-F., Cheng, Y., Sun, X., Wang, S., Li, F., Zhu, L., & Shen, H. T. (2025). A step toward world models: A survey on robotic manipulation. *arXiv:2511.02097*. https://arxiv.org/abs/2511.02097v2

---

**Review Completed:** October 26, 2026  
**Search Database:** arXiv (cs.RO category)  
**Total Papers Analyzed:** 10
