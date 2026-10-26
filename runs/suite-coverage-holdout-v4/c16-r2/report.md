# Systematic Literature Review: World Action Models

**Review Period:** June 18, 2024 – June 17, 2026  
**Category:** cs.RO (Robotics)  
**Papers Reviewed:** 10  
**Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in World Action Models (WAMs) and related frameworks in robotics. The selected papers represent cutting-edge research in integrating world modeling with action prediction, focusing on vision-language-action (VLA) models, video-action models, and unified frameworks that combine dynamics learning with policy execution. Key themes include: (1) leveraging video data for physical understanding, (2) unified architectures for joint video-action prediction, (3) efficient action tokenization and decoding, and (4) cross-embodiment generalization.

---

## Methodology

Papers were identified through arXiv search in the cs.RO category with publication dates between June 18, 2024, and June 17, 2026. The search query "world action models" yielded 50 initial papers, expanded to 142 through citation analysis. From a shortlist of 30 papers, 10 were selected based on relevance to world modeling, action prediction, and robot learning paradigms. Selection criteria emphasized papers introducing novel architectures, demonstrating significant empirical improvements, or proposing unified frameworks for video-action learning.

---

## Annotated Bibliography (APA Format)

### 1. DreamZero: World Action Models for Zero-shot Generalization

Ye, S., Ge, Y., Zheng, K., Gao, S., Yu, S., Kurian, G., Indupuru, S., Tan, Y. L., Zhu, C., Xiang, J., Malik, A., Lee, K., Liang, W., Ranawaka, N., Gu, J., Xu, Y., Wang, G., Hu, F., Narayan, A., & Bjorck, J. (2026). World Action Models are Zero-shot Policies. *arXiv preprint arXiv:2602.15922*. https://arxiv.org/abs/2602.15922v1

**Summary:** This paper introduces DreamZero, a World Action Model built on pretrained video diffusion backbones. Unlike traditional VLAs, WAMs learn physical dynamics by jointly predicting future world states and actions. The model achieves over 2x improvement in generalization to new tasks and environments compared to state-of-the-art VLAs. Key innovations include real-time closed-loop control at 7Hz using a 14B autoregressive video diffusion model and cross-embodiment transfer using video-only demonstrations (42% improvement with 10-20 minutes of data) and few-shot embodiment adaptation (30 minutes of play data).

**Key Contributions:** (1) Formalizes World Action Models as distinct from VLAs, (2) demonstrates zero-shot generalization to unseen physical motions, (3) enables efficient cross-embodiment transfer from video demonstrations.

---

### 2. Unified World Models: Video-Action Diffusion Integration

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3

**Summary:** This work presents Unified World Models (UWM), a framework integrating action diffusion and video diffusion within a unified transformer architecture. Independent diffusion timesteps govern each modality, enabling flexible representation of policies, forward/inverse dynamics, and video generation. UWM enables effective pretraining on large-scale multitask robot datasets and facilitates learning from action-free video data, improving finetuned policy performance.

**Key Contributions:** (1) Unified architecture for video and action diffusion, (2) independent timestep control for modality flexibility, (3) demonstrates improved generalization through video-data pretraining without action annotations.

---

### 3. GR-2: Web-Scale Video-Language-Action Pretraining

Cheang, C.-L., Chen, G., Jing, Y., Kong, T., Li, H., Li, Y., Liu, Y., Wu, H., Xu, J., Yang, Y., Zhang, H., & Zhu, M. (2024). GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation. *arXiv preprint arXiv:2410.06158*. https://arxiv.org/abs/2410.06158v1

**Summary:** GR-2 is a state-of-the-art generalist robot agent pretrained on 38 million video clips (over 50 billion tokens) to capture world dynamics. Fine-tuned for video generation and action prediction, it achieves 97.7% average success rate across 100+ tasks with exceptional generalization to novel backgrounds, environments, objects, and tasks. The model demonstrates effective scaling with model size.

**Key Contributions:** (1) Web-scale pretraining for robot manipulation, (2) demonstrates strong multi-task learning and generalization, (3) validates scaling laws for video-language-action models.

---

### 4. WorldVLA: Autoregressive Action-World Integration

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards Autoregressive Action World Model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

**Summary:** WorldVLA unifies VLA models and world models in a single autoregressive framework. The world model predicts future images using action and image understanding to learn environmental physics, while the action model generates actions based on observations. The paper identifies error propagation in autoregressive action generation and proposes an attention mask strategy that selectively masks prior actions, significantly improving action chunk generation.

**Key Contributions:** (1) Unified autoregressive framework for action and image understanding/generation, (2) identifies error propagation in autoregressive action sequences, (3) attention mask strategy for improved action chunk generation.

---

### 5. mimic-video: Video-Action Models Beyond VLAs

Pai, J., Achenbach, L., Montesinos, V., Forrai, B., Mees, O., & Nava, E. (2025). mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs. *arXiv preprint arXiv:2512.15692*. https://arxiv.org/abs/2512.15692v2

**Summary:** This paper argues that VLAs pretrained on static web data lack physical causality understanding. The authors introduce mimic-video, a Video-Action Model pairing internet-scale pretrained video models with flow matching-based action decoders. The decoder serves as an Inverse Dynamics Model, generating low-level actions from video-space latent representations. Results show 10x improvement in sample efficiency and 2x faster convergence compared to VLA architectures.

**Key Contributions:** (1) Critiques VLA limitations in physical understanding, (2) proposes Video-Action Models with video dynamics pretraining, (3) demonstrates superior sample efficiency and convergence speed.

---

### 6. UniVLA: Task-centric Latent Actions for Cross-embodiment Learning

Bu, Q., Yang, Y., Cai, J., Gao, S., Ren, G., Yao, M., Luo, P., & Li, H. (2025). UniVLA: Learning to Act Anywhere with Task-centric Latent Actions. *arXiv preprint arXiv:2505.06111*. https://arxiv.org/abs/2505.06111v3

**Summary:** UniVLA addresses limitations in cross-embodiment generalization by deriving task-centric action representations from videos using a latent action model. The framework incorporates language instructions and operates in DINO feature space to mitigate task-irrelevant dynamics. UniVLA achieves state-of-the-art results across manipulation and navigation benchmarks with less than 1/20 of OpenVLA's pretraining compute and 1/10 of downstream data.

**Key Contributions:** (1) Latent action model for cross-embodiment policy learning, (2) task-centric representations in DINO feature space, (3) demonstrates efficient learning from heterogeneous data including human videos.

---

### 7. UVA: Unified Video-Action Modeling

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

**Summary:** UVA jointly optimizes video and action predictions through a joint video-action latent representation and decoupled decoding. Two lightweight diffusion heads enable high-speed action inference by bypassing video generation during inference. The framework supports versatile functionality through masked input training, handling policy learning, forward/inverse dynamics, and video observation prediction without performance compromise.

**Key Contributions:** (1) Joint video-action latent representation, (2) decoupled decoding for efficient inference, (3) unified framework for multiple robotics tasks via masked training.

---

### 8. Optimized Fine-Tuning for Vision-Language-Action Models

Kim, M. J., Finn, C., & Liang, P. (2025). Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success. *arXiv preprint arXiv:2502.19645*. https://arxiv.org/abs/2502.19645v2

**Summary:** This work studies VLA adaptation design choices including action decoding schemes, representations, and learning objectives. The Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, continuous action representation, and L1 regression. OpenVLA-OFT achieves 97.1% success rate on LIBERO benchmark (vs. 76.5% baseline) with 26× throughput improvement, outperforming π₀, RDT-1B, Diffusion Policy, and ACT by up to 15%.

**Key Contributions:** (1) Systematic analysis of VLA fine-tuning strategies, (2) OFT recipe for improved efficiency and performance, (3) new state-of-the-art on simulation and real-world benchmarks.

---

### 9. Genie Envisioner: Unified World Foundation Platform

Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025). Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation. *arXiv preprint arXiv:2508.05635*. https://arxiv.org/abs/2508.05635v3

**Summary:** Genie Envisioner integrates policy learning, evaluation, and simulation in a video-generative framework. GE-Base is an instruction-conditioned video diffusion model capturing spatial, temporal, and semantic dynamics. GE-Act maps latents to action trajectories via flow-matching decoding. GE-Sim serves as an action-conditioned neural simulator for closed-loop development. EWMBench provides standardized benchmarking for visual fidelity, physical consistency, and instruction-action alignment.

**Key Contributions:** (1) Comprehensive platform integrating policy, evaluation, and simulation, (2) instruction-conditioned video diffusion for robotic dynamics, (3) standardized benchmark suite for world model evaluation.

---

### 10. FAST: Efficient Action Tokenization for VLAs

Pertsch, K., Stachowicz, K., Ichter, B., Driess, D., Nair, S., Vuong, Q., Mees, O., Finn, C., & Levine, S. (2025). FAST: Efficient Action Tokenization for Vision-Language-Action Models. *arXiv preprint arXiv:2501.09747*. https://arxiv.org/abs/2501.09747v1

**Summary:** This paper addresses poor performance of standard action tokenization in high-frequency robot data. FAST (Frequency-space Action Sequence Tokenization) uses discrete cosine transform-based compression for robot actions. FAST+, trained on 1M real robot trajectories, serves as a universal tokenizer for diverse action spaces and frequencies. Combined with π₀ VLA, it scales to 10k hours of robot data, matching diffusion VLA performance with 5× training time reduction.

**Key Contributions:** (1) DCT-based action tokenization for high-frequency control, (2) universal tokenizer trained on diverse robot data, (3) enables autoregressive VLAs for dexterous tasks with reduced training time.

---

## Synthesis and Trends

### Architectural Convergence

The reviewed papers demonstrate convergence toward unified architectures that jointly model video and actions. Five papers (Ye et al., 2026; Zhu et al., 2025; Li et al., 2025; Cen et al., 2025; Liao et al., 2025) propose frameworks integrating video diffusion with action prediction, suggesting this is becoming the dominant paradigm.

### Pretraining Strategies

A clear trend emerges toward leveraging internet-scale video data for pretraining. GR-2 (Cheang et al., 2024) uses 38M video clips, while mimic-video (Pai et al., 2025) and UniVLA (Bu et al., 2025) emphasize learning physical dynamics from video before fine-tuning on robot data. This addresses the fundamental limitation of VLAs pretrained on static images.

### Efficiency Improvements

Multiple papers focus on inference efficiency: DreamZero achieves 7Hz control with 14B parameters (Ye et al., 2026), UVA uses decoupled decoding for high-speed inference (Li et al., 2025), OpenVLA-OFT achieves 26× throughput improvement (Kim et al., 2025), and FAST reduces training time by 5× (Pertsch et al., 2025).

### Cross-embodiment Generalization

Three papers explicitly address cross-embodiment transfer: DreamZero demonstrates few-shot embodiment adaptation (Ye et al., 2026), UniVLA learns task-centric latent actions across embodiments (Bu et al., 2025), and Genie Envisioner supports diverse embodiments with minimal supervision (Liao et al., 2025).

### Evaluation Benchmarks

The field is maturing toward standardized evaluation: LIBERO benchmark (Kim et al., 2025), EWMBench (Liao et al., 2025), and consistent reporting of success rates across 100+ tasks (Cheang et al., 2024) indicate growing rigor in empirical validation.

---

## Research Gaps and Future Directions

1. **Physical Reasoning:** While video pretraining improves physical understanding, explicit reasoning about contact dynamics, friction, and multi-object interactions remains limited.

2. **Long-horizon Planning:** Most papers focus on short-horizon manipulation tasks. Extension to long-horizon tasks requiring hierarchical planning is underexplored.

3. **Sim-to-Real Transfer:** Limited discussion of sim-to-real gaps, particularly for world models trained primarily on real robot data.

4. **Multimodal Integration:** Beyond vision, integration of tactile, auditory, and proprioceptive sensing in world action models is minimally addressed.

5. **Safety and Verification:** None of the papers address formal verification or safety guarantees for world action models in deployment.

---

## Conclusion

World Action Models represent a significant evolution beyond traditional VLAs, emphasizing physical dynamics learning through video prediction and joint video-action modeling. The 10 papers reviewed demonstrate consistent improvements in generalization, sample efficiency, and cross-embodiment transfer. Key innovations include unified diffusion architectures, efficient tokenization schemes, and web-scale pretraining. The field is moving toward comprehensive platforms integrating policy learning, simulation, and evaluation, suggesting maturation toward practical deployment in diverse robotic applications.

---

## References

Bu, Q., Yang, Y., Cai, J., Gao, S., Ren, G., Yao, M., Luo, P., & Li, H. (2025). UniVLA: Learning to Act Anywhere with Task-centric Latent Actions. *arXiv preprint arXiv:2505.06111*. https://arxiv.org/abs/2505.06111v3

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards Autoregressive Action World Model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

Cheang, C.-L., Chen, G., Jing, Y., Kong, T., Li, H., Li, Y., Liu, Y., Wu, H., Xu, J., Yang, Y., Zhang, H., & Zhu, M. (2024). GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation. *arXiv preprint arXiv:2410.06158*. https://arxiv.org/abs/2410.06158v1

Kim, M. J., Finn, C., & Liang, P. (2025). Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success. *arXiv preprint arXiv:2502.19645*. https://arxiv.org/abs/2502.19645v2

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025). Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation. *arXiv preprint arXiv:2508.05635*. https://arxiv.org/abs/2508.05635v3

Pai, J., Achenbach, L., Montesinos, V., Forrai, B., Mees, O., & Nava, E. (2025). mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs. *arXiv preprint arXiv:2512.15692*. https://arxiv.org/abs/2512.15692v2

Pertsch, K., Stachowicz, K., Ichter, B., Driess, D., Nair, S., Vuong, Q., Mees, O., Finn, C., & Levine, S. (2025). FAST: Efficient Action Tokenization for Vision-Language-Action Models. *arXiv preprint arXiv:2501.09747*. https://arxiv.org/abs/2501.09747v1

Ye, S., Ge, Y., Zheng, K., Gao, S., Yu, S., Kurian, G., Indupuru, S., Tan, Y. L., Zhu, C., Xiang, J., Malik, A., Lee, K., Liang, W., Ranawaka, N., Gu, J., Xu, Y., Wang, G., Hu, F., Narayan, A., & Bjorck, J. (2026). World Action Models are Zero-shot Policies. *arXiv preprint arXiv:2602.15922*. https://arxiv.org/abs/2602.15922v1

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3
