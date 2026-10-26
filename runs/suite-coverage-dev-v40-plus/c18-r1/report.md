# Systematic Literature Review: World Models for Robotic Manipulation

**Search Parameters:**
- **Category:** cs.RO (Robotics)
- **Publication Period:** May 27, 2024 – May 26, 2026
- **Number of Papers:** 10
- **Review Date:** October 26, 2026

---

## Selected Papers (APA Format)

### 1. Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3

**Abstract:** This work presents Unified World Models (UWM), a framework that integrates action diffusion and video diffusion processes within a unified transformer architecture. UWM enables effective pretraining on large-scale multitask robot datasets and facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, resulting in more generalizable and robust policies than imitation learning.

**Key Contributions:**
- Unified transformer architecture combining video and action diffusion
- Flexible representation supporting policy, forward dynamics, inverse dynamics, and video generation
- Effective pretraining on heterogeneous datasets without requiring action annotations

---

### 2. WorldVLA: Towards Autoregressive Action World Model

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards Autoregressive Action World Model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

**Abstract:** WorldVLA integrates Vision-Language-Action (VLA) models and world models in a single framework. The world model predicts future images by leveraging both action and image understanding to learn environmental physics, while the action model generates subsequent actions based on image observations. An attention mask strategy addresses error propagation in autoregressive action generation.

**Key Contributions:**
- Single framework unifying VLA and world model capabilities
- Mutual enhancement between world model and action model
- Attention mask strategy for selective masking of prior actions during generation

---

### 3. Unified Video Action Model

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

**Abstract:** The Unified Video Action model (UVA) jointly optimizes video and action predictions through a joint video-action latent representation and decoupled video-action decoding. This enables high-speed action inference by bypassing video generation during inference while maintaining versatility for diverse robotics tasks including policy learning, forward/inverse dynamics, and video observation prediction.

**Key Contributions:**
- Joint video-action latent representation bridging visual and action domains
- Decoupled decoding with lightweight diffusion heads for efficient inference
- General-purpose solution for multiple robotics tasks without performance compromise

---

### 4. DreamGen: Unlocking Generalization in Robot Learning through Video World Models

Jang, J., Ye, S., Lin, Z., Xiang, J., Bjorck, J., Fang, Y., Hu, F., Huang, S., Kundalia, K., Lin, Y.-C., Magne, L., Mandlekar, A., Narayan, A., Tan, Y. L., Wang, G., Wang, J., Wang, Q., Xu, Y., Zeng, X., & Zheng, K. (2025). DreamGen: Unlocking Generalization in Robot Learning through Video World Models. *arXiv preprint arXiv:2505.12705*. https://arxiv.org/abs/2505.12705v2

**Abstract:** DreamGen introduces a 4-stage pipeline for training robot policies through neural trajectories—synthetic robot data generated from video world models. The approach leverages image-to-video generative models adapted to target robot embodiments, recovering pseudo-action sequences using latent action models or inverse-dynamics models. A humanoid robot demonstrated 22 new behaviors in seen and unseen environments from teleoperation data of only a single pick-and-place task.

**Key Contributions:**
- 4-stage pipeline for policy training via synthetic video-generated trajectories
- Strong behavior and environment generalization from minimal demonstration data
- DreamGen Bench for systematic evaluation of video generation for robot learning

---

### 5. EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation

Huang, S., Chen, L., Zhou, P., Chen, S., Jiang, Z., Hu, Y., Liao, Y., Gao, P., Li, H., Yao, M., & Ren, G. (2025). EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation. *arXiv preprint arXiv:2501.01895*. https://arxiv.org/abs/2501.01895v3

**Abstract:** EnerVerse is a generative robotics foundation model employing chunk-wise autoregressive video diffusion to predict future embodied spaces from instructions. It adopts multi-view video representation for 3D robotics world modeling and incorporates EnerVerse-D, a data engine pipeline combining generative modeling with 4D Gaussian Splatting. EnerVerse-A achieves approximately 280 ms per 8-step action chunk on a single RTX 4090.

**Key Contributions:**
- Chunk-wise autoregressive video diffusion with sparse context memory
- Multi-view video representation addressing motion ambiguity and 3D grounding
- Self-reinforcing data loop reducing sim-to-real gap via 4D Gaussian Splatting

---

### 6. Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

Tian, Y., Yang, S., Zeng, J., Wang, P., Lin, D., Dong, H., & Pang, J. (2024). Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation. *arXiv preprint arXiv:2412.15109*. https://arxiv.org/abs/2412.15109v1

**Abstract:** This paper presents Predictive Inverse Dynamics Models (PIDM), an end-to-end paradigm predicting actions using inverse dynamics models conditioned on forecasted visual states. The Transformer-based model Seer is pre-trained on large-scale robotic datasets and adapted to real-world scenarios with minimal fine-tuning. Seer achieves improvements of 13% on LIBERO-LONG, 21% on CALVIN ABC-D, and 43% in real-world tasks.

**Key Contributions:**
- End-to-end paradigm closing the loop between vision and action
- Transformer architecture processing both visual states and actions
- State-of-the-art performance on CALVIN ABC-D benchmark (average length 4.28)

---

### 7. GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards Scalable Gaussian World Models for Robotic Manipulation. *arXiv preprint arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

**Abstract:** Gaussian World Model (GWM) reconstructs future states by inferring the propagation of Gaussian primitives under robot actions. The core architecture combines a latent Diffusion Transformer (DiT) with a 3D variational autoencoder, enabling fine-grained scene-level future state reconstruction with Gaussian Splatting. GWM serves as both a visual representation enhancer and a neural simulator for model-based reinforcement learning.

**Key Contributions:**
- Novel Gaussian-based world model for 3D geometric understanding
- Latent DiT combined with 3D VAE for Gaussian Splatting reconstruction
- Dual functionality for imitation learning enhancement and neural simulation

---

### 8. Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation

Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025). Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation. *arXiv preprint arXiv:2508.05635*. https://arxiv.org/abs/2508.05635v3

**Abstract:** Genie Envisioner (GE) integrates policy learning, evaluation, and simulation within a single video-generative framework. GE-Base is a large-scale instruction-conditioned video diffusion model capturing spatial, temporal, and semantic dynamics. GE-Act maps latent representations to executable action trajectories through flow-matching decoding, while GE-Sim serves as an action-conditioned neural simulator for closed-loop policy development.

**Key Contributions:**
- Unified platform integrating policy learning, evaluation, and simulation
- Large-scale instruction-conditioned video diffusion model
- EWMBench benchmark suite for visual fidelity, physical consistency, and instruction-action alignment

---

### 9. EnerVerse-AC: Envisioning Embodied Environments with Action Condition

Jiang, Y., Chen, S., Huang, S., Chen, L., Zhou, P., Liao, Y., He, X., Liu, C., Li, H., Yao, M., & Ren, G. (2025). EnerVerse-AC: Envisioning Embodied Environments with Action Condition. *arXiv preprint arXiv:2505.09723*. https://arxiv.org/abs/2505.09723v1

**Abstract:** EnerVerse-AC (EVAC) is an action-conditional world model generating future visual observations based on predicted agent actions. The model introduces multi-level action-conditioning mechanisms and ray map encoding for dynamic multi-view image generation. EVAC serves as both a data engine augmenting human-collected trajectories and an evaluator generating realistic video observations for policy testing without physical robots.

**Key Contributions:**
- Multi-level action-conditioning mechanism for controllable inference
- Ray map encoding for dynamic multi-view image generation
- Cost-effective policy testing eliminating need for physical robots or complex simulations

---

### 10. OpenVLA: An Open-Source Vision-Language-Action Model

Kim, M. J., Pertsch, K., Karamcheti, S., Xiao, T., Balakrishna, A., Nair, S., Rafailov, R., Foster, E., Lam, G., Sanketi, P., Vuong, Q., Kollar, T., Burchfiel, B., Tedrake, R., Sadigh, D., Levine, S., Liang, P., & Finn, C. (2024). OpenVLA: An Open-Source Vision-Language-Action Model. *arXiv preprint arXiv:2406.09246*. https://arxiv.org/abs/2406.09246v3

**Abstract:** OpenVLA is a 7B-parameter open-source Vision-Language-Action model trained on 970k real-world robot demonstrations. Building on Llama 2 with visual encoder fusing DINOv2 and SigLIP features, OpenVLA outperforms closed models like RT-2-X (55B) by 16.5% across 29 tasks with 7x fewer parameters. The model supports efficient fine-tuning via low-rank adaptation and quantization for consumer GPUs.

**Key Contributions:**
- First open-source VLA with strong generalist manipulation capabilities
- Superior performance to closed models despite significantly fewer parameters
- Efficient fine-tuning and deployment on consumer hardware

---

## Thematic Analysis

### Major Research Trends

**1. Unified Architectures for Video-Action Learning**
Multiple works (UWM, UVA, WorldVLA) converge on unified architectures that jointly process video and action modalities. This represents a shift from separate perception and action modules toward integrated world models that can flexibly switch between policy learning, dynamics prediction, and video generation.

**2. Generative World Models for Data Efficiency**
DreamGen, EnerVerse, and Genie Envisioner demonstrate that video world models can generate synthetic training data, dramatically reducing the need for expensive real-world robot demonstrations. This trend addresses a fundamental bottleneck in robot learning scalability.

**3. 3D and Geometric Understanding**
GWM and EnerVerse explicitly incorporate 3D geometric reasoning through Gaussian Splatting and multi-view representations, moving beyond 2D video prediction toward spatially consistent world models that better capture physical dynamics.

**4. Open-Source and Accessibility**
OpenVLA's release as an open-source model with consumer-GPU compatibility reflects a broader trend toward democratizing access to advanced robot learning capabilities, enabling wider research participation.

### Methodological Approaches

| Approach | Papers | Key Advantage |
|----------|--------|---------------|
| Diffusion-based | UWM, UVA, EnerVerse, Genie Envisioner | High-quality generation, flexible conditioning |
| Autoregressive | WorldVLA, EnerVerse | Sequential prediction, long-horizon reasoning |
| Gaussian Splatting | GWM, EnerVerse-D | 3D geometric consistency, neural simulation |
| Inverse Dynamics | PIDM/Seer, DreamGen (IDM) | Action recovery from video, end-to-end learning |
| Vision-Language-Action | WorldVLA, OpenVLA | Language grounding, semantic understanding |

### Performance Benchmarks

Several papers report results on standard benchmarks:
- **CALVIN ABC-D:** Seer (PIDM) achieves 4.28 average length, setting new state-of-the-art
- **LIBERO-LONG:** Seer shows 13% improvement
- **Real-world tasks:** Seer demonstrates 43% improvement, OpenVLA shows 20.4% improvement over Diffusion Policy

### Common Challenges Addressed

1. **Data Scarcity:** Video world models enable learning from action-free video data (UWM, DreamGen)
2. **Sim-to-Real Gap:** 4D Gaussian Splatting and multi-view representations improve transfer (EnerVerse, GWM)
3. **Error Propagation:** Attention masking strategies address autoregressive action generation errors (WorldVLA)
4. **Computational Efficiency:** Decoupled decoding and feature reuse enable real-time inference (UVA, EnerVerse-A)
5. **Generalization:** Synthetic data generation and large-scale pretraining improve out-of-distribution performance (DreamGen, OpenVLA)

---

## Conclusion

The selected papers from May 2024 to May 2026 reveal a rapidly evolving field where world models for robotic manipulation are transitioning from purely predictive models to generative, unified frameworks that serve multiple functions: policy learning, data generation, simulation, and evaluation. Key innovations include unified video-action architectures, 3D geometric understanding through Gaussian representations, and action-conditional generation enabling cost-effective policy testing. The emergence of open-source models like OpenVLA and comprehensive platforms like Genie Envisioner suggests the field is maturing toward practical, accessible solutions for general-purpose robotic manipulation.

---

**Review Methodology:**
- **Database:** arXiv
- **Primary Category:** cs.RO (Robotics)
- **Search Query:** "world models robotic manipulation"
- **Screening:** 30 shortlisted papers scored for centrality to topic; top 10 by citation centrality selected
- **Inclusion Criteria:** Published between 2024-05-27 and 2026-05-26, primary category cs.RO, focus on world models for robotic manipulation
