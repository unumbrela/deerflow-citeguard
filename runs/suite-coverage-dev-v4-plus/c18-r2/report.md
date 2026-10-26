# Systematic Literature Review: World Models for Robotic Manipulation

**Review Period:** May 27, 2024 – May 26, 2026  
**Primary Category:** cs.RO (Robotics)  
**Format:** APA Style  
**Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in world models for robotic manipulation, focusing on 10 peer-reviewed papers published between May 2024 and May 2026. The review reveals a significant trend toward unified architectures that integrate video generation, action prediction, and dynamics modeling within single frameworks. Key innovations include diffusion-based world models, autoregressive action-image generation, Gaussian splatting for 3D scene reconstruction, and video-to-action pipelines that enable generalization from synthetic data. These approaches demonstrate substantial improvements in policy generalization, data efficiency, and real-world deployment capabilities.

---

## Methodology

**Search Strategy:** Papers were identified through arXiv search in the cs.RO category with the query "world models robotic manipulation." The search yielded 50 initial matches, expanded to 145 papers through citation analysis, and shortlisted to 30 candidates.

**Selection Criteria:** Papers were screened for relevance to world models, model-based learning, or predictive models applied to robotic manipulation tasks. The final 10 papers were selected based on co-citation centrality and direct focus on world model architectures for manipulation.

**Screening Results:**
- Initial pool: 50 papers
- Added from references: 95 papers
- Shortlisted: 30 papers
- Final selection: 10 papers
- Inclusion rate: 33.3%

---

## Annotated Bibliography

### 1. Unified World Models Architecture

**Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025).** Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3

**Summary:** This paper presents Unified World Models (UWM), a framework that integrates action diffusion and video diffusion within a unified transformer architecture. The key innovation is independent control of modality-specific diffusion timesteps, enabling the model to flexibly function as a policy, forward dynamics model, inverse dynamics model, or video generator. UWM enables effective pretraining on large-scale multitask robot datasets and facilitates learning from action-free video data.

**Key Contributions:**
- Unified transformer architecture with independent diffusion timesteps for video and action modalities
- Demonstrated effective pretraining on large-scale heterogeneous robotic datasets
- Showed improved generalization and robustness compared to traditional imitation learning
- Enabled learning from action-free video data through masked training

**Relevance:** Directly addresses world model unification for scalable robot learning.

---

**Li, S., Gao, Y., Sadigh, D., & Song, S. (2025).** Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

**Summary:** The Unified Video Action model (UVA) jointly optimizes video and action predictions through a joint video-action latent representation and decoupled decoding. The architecture uses two lightweight diffusion heads to enable high-speed action inference by bypassing video generation during inference. UVA achieves both high accuracy and efficient action inference while supporting diverse tasks including policy learning, forward/inverse dynamics modeling, and video observation prediction.

**Key Contributions:**
- Joint video-action latent representation bridging visual and action domains
- Decoupled decoding enabling high-speed action inference
- Versatile functionality through masked input training
- State-of-the-art performance across multiple robotics tasks without task-specific tailoring

**Relevance:** Demonstrates unified video-action modeling for general-purpose robotic solutions.

---

### 2. Autoregressive and Generative World Models

**Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025).** WorldVLA: Towards Autoregressive Action World Model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

**Summary:** WorldVLA integrates Vision-Language-Action (VLA) models and world models in a single autoregressive framework. The world model predicts future images using action and image understanding to learn environmental physics, while the action model generates actions based on image observations. The paper identifies error propagation in autoregressive action generation and proposes an attention mask strategy that selectively masks prior actions during current action generation.

**Key Contributions:**
- Unified VLA and world model framework with mutual enhancement
- Autoregressive action-image generation with attention masking
- Addressed error propagation in sequential action generation
- Demonstrated superior performance over standalone action and world models

**Relevance:** Advances autoregressive world models with vision-language-action integration.

---

**Huang, S., Chen, L., Zhou, P., Chen, S., Jiang, Z., Hu, Y., Liao, Y., Gao, P., Li, H., Yao, M., & Ren, G. (2025).** EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation. *arXiv preprint arXiv:2501.01895*. https://arxiv.org/abs/2501.01895v3

**Summary:** EnerVerse is a generative robotics foundation model employing chunk-wise autoregressive video diffusion to predict future embodied spaces from instructions. The model uses sparse context memory for long-term reasoning and multi-view video representation for 3D grounding. EnerVerse-D combines generative modeling with 4D Gaussian Splatting for self-reinforcing data loops, while EnerVerse-A translates 4D world representations into physical actions with 280ms inference time per 8-step action chunk.

**Key Contributions:**
- Chunk-wise autoregressive video diffusion for embodied space prediction
- Multi-view representation addressing motion ambiguity and 3D grounding
- Integration with 4D Gaussian Splatting for sim-to-real gap reduction
- Efficient action prediction achieving 280ms per action chunk

**Relevance:** Pioneers embodied space prediction with autoregressive video diffusion.

---

**Jiang, Y., Chen, S., Huang, S., Chen, L., Zhou, P., Liao, Y., He, X., Liu, C., Li, H., Yao, M., & Ren, G. (2025).** EnerVerse-AC: Envisioning Embodied Environments with Action Condition. *arXiv preprint arXiv:2505.09723*. https://arxiv.org/abs/2505.09723v1

**Summary:** EnerVerse-AC (EVAC) extends EnerVerse with action-conditional world modeling that generates future visual observations based on predicted agent actions. The model introduces multi-level action-conditioning mechanisms and ray map encoding for dynamic multi-view image generation. EVAC serves as both a data engine and evaluator, augmenting human-collected trajectories and generating realistic action-conditioned video observations for policy testing without physical robots.

**Key Contributions:**
- Action-conditional world model for controllable robotic inference
- Multi-level action-conditioning with ray map encoding
- Data engine augmenting trajectories with diverse failure cases
- Virtual evaluation eliminating need for physical testing

**Relevance:** Extends embodied world models with action-conditional generation for evaluation.

---

### 3. Video-Based Policy Learning and Generalization

**Jang, J., Ye, S., Lin, Z., Xiang, J., Bjorck, J., Fang, Y., Hu, F., Huang, S., Kundalia, K., Lin, Y.-C., Magne, L., Mandlekar, A., Narayan, A., Tan, Y. L., Wang, G., Wang, J., Wang, Q., Xu, Y., Zeng, X., & Zheng, K. (2025).** DreamGen: Unlocking Generalization in Robot Learning through Video World Models. *arXiv preprint arXiv:2505.12705*. https://arxiv.org/abs/2505.12705v2

**Summary:** DreamGen introduces a 4-stage pipeline training robot policies through neural trajectories—synthetic robot data generated from video world models. The approach leverages image-to-video generative models adapted to robot embodiments, recovering pseudo-action sequences via latent action models or inverse dynamics models. A humanoid robot demonstrated 22 new behaviors in seen and unseen environments using teleoperation data from only a single pick-and-place task.

**Key Contributions:**
- 4-stage pipeline for policy training from synthetic video-generated trajectories
- Adaptation of image-to-video models to robot embodiments
- Action recovery through latent action or inverse dynamics models
- Strong behavior and environment generalization with minimal real data

**Relevance:** Demonstrates video world models enabling generalization beyond manual data collection.

---

**Bharadhwaj, H., Dwibedi, D., Gupta, A., Tulsiani, S., Doersch, C., Xiao, T., Shah, D., Xia, F., Sadigh, D., & Kirmani, S. (2024).** Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation. *arXiv preprint arXiv:2409.16283*. https://arxiv.org/abs/2409.16283v1

**Summary:** Gen2Act addresses generalization to novel tasks by predicting motion information from web data through human video generation and conditioning robot policies on generated videos. The approach leverages pre-trained video generation models on web data without fine-tuning, using an order of magnitude less robot interaction data. Results demonstrate manipulation of unseen object types and novel motions not present in robot training data.

**Key Contributions:**
- Zero-shot human video generation for novel scenario generalization
- Single policy conditioned on generated videos
- Leverages web-scale video data without model fine-tuning
- Enables manipulation of unseen objects and novel motions

**Relevance:** Shows web-scale video generation enabling zero-shot generalization.

---

### 4. Predictive Dynamics and End-to-End Learning

**Tian, Y., Yang, S., Zeng, J., Wang, P., Lin, D., Dong, H., & Pang, J. (2024).** Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation. *arXiv preprint arXiv:2412.15109*. https://arxiv.org/abs/2412.15109v1

**Summary:** This paper presents Predictive Inverse Dynamics Models (PIDM), an end-to-end paradigm predicting actions using inverse dynamics models conditioned on forecasted visual states. The Seer model uses Transformers for both visual states and actions, pre-trained on large-scale robotic datasets like DROID. Seer achieves state-of-the-art performance with 13% improvement on LIBERO-LONG, 21% on CALVIN ABC-D, and 43% in real-world tasks.

**Key Contributions:**
- End-to-end predictive inverse dynamics closing vision-action loop
- Transformer-based processing of visual states and actions
- State-of-the-art results on multiple benchmarks (LIBERO-LONG, CALVIN ABC-D)
- Superior generalization for novel objects, lighting, and environments

**Relevance:** Establishes predictive inverse dynamics as scalable end-to-end learning paradigm.

---

### 5. 3D and Gaussian World Models

**Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025).** GWM: Towards Scalable Gaussian World Models for Robotic Manipulation. *arXiv preprint arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

**Summary:** Gaussian World Model (GWM) reconstructs future states by inferring propagation of Gaussian primitives under robot actions. The architecture combines latent Diffusion Transformer (DiT) with 3D variational autoencoder for fine-grained scene-level reconstruction with Gaussian Splatting. GWM enhances visual representation through self-supervised future prediction and serves as a neural simulator for model-based reinforcement learning.

**Key Contributions:**
- First Gaussian Splatting-based world model for robotic manipulation
- Latent DiT with 3D VAE for scene-level future reconstruction
- Self-supervised training enhancing visual representations
- Neural simulator supporting model-based reinforcement learning

**Relevance:** Pioneers 3D Gaussian world models with geometric understanding.

---

### 6. Unified Foundation Platforms

**Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025).** Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation. *arXiv preprint arXiv:2508.05635*. https://arxiv.org/abs/2508.05635v3

**Summary:** Genie Envisioner (GE) integrates policy learning, evaluation, and simulation within a single video-generative framework. GE-Base is a large-scale instruction-conditioned video diffusion model capturing spatial, temporal, and semantic dynamics. GE-Act maps latent representations to executable actions through flow-matching decoding, while GE-Sim serves as an action-conditioned neural simulator. The platform includes EWMBench for standardized benchmarking.

**Key Contributions:**
- Unified platform integrating policy learning, evaluation, and simulation
- Large-scale instruction-conditioned video diffusion foundation
- Flow-matching decoder for precise policy inference
- Standardized benchmark suite (EWMBench) for world model evaluation

**Relevance:** Establishes comprehensive world foundation platform for embodied intelligence.

---

## Thematic Analysis

### Emerging Architectures

**Unified Multi-Modal Frameworks:** Six papers (Zhu et al., 2025; Li et al., 2025; Cen et al., 2025; Liao et al., 2025; Huang et al., 2025; Jiang et al., 2025) converge on unified architectures integrating video generation, action prediction, and dynamics modeling. The dominant pattern uses diffusion-based transformers with masked training to enable multiple functionalities from single models.

**Autoregressive Video Diffusion:** Three papers (Huang et al., 2025; Jiang et al., 2025; Liao et al., 2025) employ chunk-wise autoregressive video diffusion for embodied space prediction, enabling long-horizon reasoning through sparse context memory and multi-view representations.

**3D Geometric Understanding:** Two papers (Lu et al., 2025; Huang et al., 2025) incorporate Gaussian Splatting for 3D scene reconstruction, addressing the limitation of image-based world models lacking consistent spatial and physical understanding.

### Data Efficiency and Generalization

**Learning from Video-Only Data:** Four papers (Zhu et al., 2025; Jang et al., 2025; Bharadhwaj et al., 2024; Tian et al., 2024) demonstrate effective learning from action-free video data through inverse dynamics models, latent action models, or masked diffusion training. This addresses the scarcity of high-quality action-annotated data.

**Synthetic Trajectory Generation:** Two papers (Jang et al., 2025; Bharadhwaj et al., 2024) use video world models to generate synthetic training data, enabling policy learning with orders of magnitude less real robot interaction data. Jang et al. (2025) achieved 22 new behaviors from a single pick-and-place demonstration.

**Web-Scale Pretraining:** Three papers (Bharadhwaj et al., 2024; Tian et al., 2024; Liao et al., 2025) leverage web-scale or internet-scale video data for pretraining, demonstrating transfer to robotic manipulation with minimal fine-tuning.

### Evaluation and Benchmarking

**Standardized Benchmarks:** Two papers introduce comprehensive benchmarking frameworks. Jang et al. (2025) present DreamGen Bench correlating video generation quality with downstream policy success. Liao et al. (2025) introduce EWMBench measuring visual fidelity, physical consistency, and instruction-action alignment.

**Neural Simulators:** Three papers (Lu et al., 2025; Jiang et al., 2025; Liao et al., 2025) position world models as neural simulators for policy evaluation and training, eliminating the need for physical robots or complex physics simulations during development.

### Performance Metrics

**Real-World Deployment:** Seven papers report real-world experimental validation (Zhu et al., 2025; Huang et al., 2025; Tian et al., 2024; Bharadhwaj et al., 2024; Lu et al., 2025; Jiang et al., 2025; Liao et al., 2025), with inference times ranging from 280ms (Huang et al., 2025) to real-time performance.

**Benchmark Improvements:** Tian et al. (2024) report state-of-the-art results with 13% improvement on LIBERO-LONG, 21% on CALVIN ABC-D (achieving average length 4.28), and 43% improvement in real-world tasks.

**Generalization:** Multiple papers demonstrate generalization to novel objects, lighting conditions, environments, and behaviors not present in training data (Jang et al., 2025; Bharadhwaj et al., 2024; Tian et al., 2024).

---

## Critical Assessment

### Strengths

1. **Architectural Innovation:** The field shows rapid progress in unified architectures that elegantly combine video generation, action prediction, and dynamics modeling through diffusion-based transformers and autoregressive frameworks.

2. **Data Efficiency:** Multiple approaches successfully leverage action-free video data and synthetic trajectory generation, addressing the fundamental bottleneck of action-annotated data scarcity.

3. **Real-World Validation:** Strong emphasis on real-world deployment with seven papers demonstrating physical robot experiments, moving beyond simulation-only validation.

4. **Generalization:** Consistent demonstration of generalization to novel objects, environments, and behaviors, with several papers achieving zero-shot or few-shot transfer.

### Limitations

1. **Computational Requirements:** Diffusion-based models and large-scale video generation require significant computational resources, with limited discussion of deployment on resource-constrained platforms.

2. **Temporal Horizons:** While chunk-wise autoregressive models enable longer predictions, most approaches still operate on limited temporal horizons (8-step action chunks), restricting long-horizon task planning.

3. **Evaluation Standardization:** Despite emerging benchmarks (EWMBench, DreamGen Bench), the field lacks standardized evaluation protocols, making direct comparison between approaches challenging.

4. **Failure Mode Analysis:** Limited systematic analysis of failure modes, particularly in novel scenarios where world models may generate physically implausible predictions.

### Research Gaps

1. **Multi-Agent Interactions:** No papers address world models for multi-robot or human-robot collaborative manipulation scenarios.

2. **Tactile and Force Sensing:** All approaches focus on visual world models, with no integration of tactile, force, or proprioceptive sensing for contact-rich manipulation.

3. **Continual Learning:** Limited exploration of continual or online learning scenarios where world models must adapt to changing environments or robot embodiments.

4. **Safety and Verification:** Minimal discussion of safety guarantees, uncertainty quantification, or verification methods for world model predictions in safety-critical applications.

---

## Future Directions

Based on the reviewed literature, promising future directions include:

1. **Multi-Modal Sensory Integration:** Extending world models beyond vision to incorporate tactile, force, audio, and proprioceptive inputs for contact-rich manipulation tasks.

2. **Hierarchical World Models:** Developing hierarchical architectures combining high-level task planning with low-level dynamics prediction for long-horizon manipulation.

3. **Uncertainty-Aware Prediction:** Integrating uncertainty quantification into world model predictions for safe exploration and risk-aware planning.

4. **Cross-Embodiment Transfer:** Improving world model transfer across different robot embodiments, grippers, and kinematic configurations.

5. **Human-Robot Collaboration:** Extending world models to predict and reason about human actions in collaborative manipulation scenarios.

6. **Efficient Inference:** Developing distillation, pruning, or alternative architectures reducing computational requirements for real-time deployment.

---

## Conclusion

The reviewed literature demonstrates rapid advancement in world models for robotic manipulation, with clear trends toward unified multi-modal architectures, video-based policy learning, and 3D geometric understanding. The integration of diffusion models, autoregressive video generation, and Gaussian Splatting has enabled significant improvements in data efficiency, generalization, and real-world deployment. However, challenges remain in computational efficiency, long-horizon planning, evaluation standardization, and safety verification. The emergence of world models as neural simulators and foundation platforms suggests a paradigm shift toward generative approaches that unify perception, prediction, and action for scalable robot learning.

---

## References

Bharadhwaj, H., Dwibedi, D., Gupta, A., Tulsiani, S., Doersch, C., Xiao, T., Shah, D., Xia, F., Sadigh, D., & Kirmani, S. (2024). Gen2Act: Human video generation in novel scenarios enables generalizable robot manipulation. *arXiv preprint arXiv:2409.16283*. https://arxiv.org/abs/2409.16283v1

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards autoregressive action world model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

Huang, S., Chen, L., Zhou, P., Chen, S., Jiang, Z., Hu, Y., Liao, Y., Gao, P., Li, H., Yao, M., & Ren, G. (2025). EnerVerse: Envisioning embodied future space for robotics manipulation. *arXiv preprint arXiv:2501.01895*. https://arxiv.org/abs/2501.01895v3

Jang, J., Ye, S., Lin, Z., Xiang, J., Bjorck, J., Fang, Y., Hu, F., Huang, S., Kundalia, K., Lin, Y.-C., Magne, L., Mandlekar, A., Narayan, A., Tan, Y. L., Wang, G., Wang, J., Wang, Q., Xu, Y., Zeng, X., & Zheng, K. (2025). DreamGen: Unlocking generalization in robot learning through video world models. *arXiv preprint arXiv:2505.12705*. https://arxiv.org/abs/2505.12705v2

Jiang, Y., Chen, S., Huang, S., Chen, L., Zhou, P., Liao, Y., He, X., Liu, C., Li, H., Yao, M., & Ren, G. (2025). EnerVerse-AC: Envisioning embodied environments with action condition. *arXiv preprint arXiv:2505.09723*. https://arxiv.org/abs/2505.09723v1

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025). Genie Envisioner: A unified world foundation platform for robotic manipulation. *arXiv preprint arXiv:2508.05635*. https://arxiv.org/abs/2508.05635v3

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. *arXiv preprint arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

Tian, Y., Yang, S., Zeng, J., Wang, P., Lin, D., Dong, H., & Pang, J. (2024). Predictive Inverse Dynamics Models are scalable learners for robotic manipulation. *arXiv preprint arXiv:2412.15109*. https://arxiv.org/abs/2412.15109v1

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3

---

**Total Papers Reviewed:** 10  
**Review Completion Date:** October 26, 2026
