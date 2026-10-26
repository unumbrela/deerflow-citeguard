# Systematic Literature Review: World Action Models

**Date:** October 26, 2026  
**Category:** cs.RO (Robotics)  
**Search Period:** June 18, 2024 – June 17, 2026  
**Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in World Action Models (WAMs) and related Vision-Language-Action (VLA) frameworks in robotics. The reviewed papers, published between 2024 and 2026, demonstrate a paradigm shift toward unified models that jointly learn physical dynamics through video prediction and action generation. Key innovations include diffusion-based architectures, cross-embodiment transfer capabilities, and efficient action tokenization schemes that enable real-time closed-loop control.

---

## Methodology

Papers were identified through arXiv search in the cs.RO category with publication dates between June 18, 2024, and June 17, 2026. The search query focused on "world action models" with citation expansion to capture related work. From an initial pool of 50 papers and 92 additional references, 30 papers were shortlisted and screened based on relevance to world models, action models, and robotics applications. The 10 most central papers were selected for this review.

---

## Annotated Bibliography (APA Format)

### 1. DreamZero: World Action Models as Zero-shot Policies

Ye, S., Ge, Y., Zheng, K., Gao, S., Yu, S., Kurian, G., Indupuru, S., Tan, Y. L., Zhu, C., Xiang, J., Malik, A., Lee, K., Liang, W., Ranawaka, N., Gu, J., Xu, Y., Wang, G., Hu, F., Narayan, A., & Bjorck, J. (2026). World Action Models are Zero-shot Policies. *arXiv preprint arXiv:2602.15922*. https://arxiv.org/abs/2602.15922v1

**Summary:** This paper introduces DreamZero, a World Action Model built on pretrained video diffusion backbones. Unlike traditional VLAs that struggle with unseen physical motions, WAMs learn physical dynamics by jointly predicting future world states and actions using video as dense representation. DreamZero achieves over 2x improvement in generalization compared to state-of-the-art VLAs and enables real-time closed-loop control at 7Hz despite using a 14B autoregressive video diffusion model. The model demonstrates remarkable cross-embodiment transfer capabilities, achieving 42% improvement on unseen tasks with only 10-20 minutes of video-only demonstrations from other robots or humans.

**Key Contributions:**
- Novel WAM architecture using video diffusion for physical dynamics learning
- Real-time control optimization for large autoregressive models
- Few-shot embodiment adaptation with 30 minutes of play data
- Heterogeneous robot data integration without repetitive demonstrations

---

### 2. Unified World Models: Coupling Video and Action Diffusion

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3

**Summary:** This work presents Unified World Models (UWM), a framework that integrates action diffusion and video diffusion processes within a unified transformer architecture. UWM addresses the challenge of scaling imitation learning by leveraging both action-annotated robot data and action-free video data. The independent control of modality-specific diffusion timesteps enables flexible representation of policies, forward dynamics, inverse dynamics, and video generation. Experiments demonstrate that UWM enables effective pretraining on large-scale multitask robot datasets, producing more generalizable and robust policies than traditional imitation learning approaches.

**Key Contributions:**
- Unified transformer architecture with independent diffusion timesteps for video and action
- Learning from action-free video data through timestep control
- Improved policy generalization and robustness through multimodal pretraining
- Code and video demonstrations available at https://weirdlabuw.github.io/uwm/

---

### 3. GR-2: Generative Video-Language-Action Model with Web-Scale Knowledge

Cheang, C.-L., Chen, G., Jing, Y., Kong, T., Li, H., Li, Y., Liu, Y., Wu, H., Xu, J., Yang, Y., Zhang, H., & Zhu, M. (2024). GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation. *arXiv preprint arXiv:2410.06158*. https://arxiv.org/abs/2410.06158v1

**Summary:** GR-2 represents a state-of-the-art generalist robot agent pre-trained on 38 million internet video clips (over 50 billion tokens) to capture world dynamics before fine-tuning for robot manipulation. This large-scale pretraining enables exceptional generalization across novel backgrounds, environments, objects, and tasks. GR-2 achieves an average success rate of 97.7% across more than 100 tasks and demonstrates effective scaling with model size. The model exhibits impressive multi-task learning capabilities and generalization to previously unseen scenarios.

**Key Contributions:**
- Web-scale pretraining on 38M video clips for world dynamics understanding
- 97.7% average success rate across 100+ manipulation tasks
- Effective scaling properties with model size
- Exceptional generalization to novel environments and objects

---

### 4. WorldVLA: Autoregressive Action World Model

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards Autoregressive Action World Model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

**Summary:** WorldVLA integrates VLA models and world models in a single autoregressive framework. The world model predicts future images using action and image understanding to learn environmental physics, while the action model generates subsequent actions based on image observations. The authors identify that autoregressive action sequence generation suffers from error propagation due to limited generalization capability. To address this, they propose an attention mask strategy that selectively masks prior actions during current action generation, showing significant improvement in action chunk generation tasks.

**Key Contributions:**
- Unified autoregressive framework combining VLA and world models
- Mutual enhancement between world model and action model components
- Attention mask strategy to mitigate error propagation in autoregressive action generation
- Improved performance over standalone action and world models

---

### 5. mimic-video: Video-Action Models Beyond VLAs

Pai, J., Achenbach, L., Montesinos, V., Forrai, B., Mees, O., & Nava, E. (2025). mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs. *arXiv preprint arXiv:2512.15692*. https://arxiv.org/abs/2512.15692v2

**Summary:** This paper critiques prevailing VLAs for relying on disconnected static web data, forcing policies to implicitly infer physical dynamics from robot trajectories alone. The authors introduce mimic-video, a Video-Action Model (VAM) pairing Internet-scale pretrained video models with flow matching-based action decoders. The decoder serves as an Inverse Dynamics Model, generating low-level actions from latent video-space action plan representations. This approach achieves state-of-the-art performance with 10x improved sample efficiency and 2x faster convergence compared to traditional VLA architectures.

**Key Contributions:**
- Video-based pretraining capturing both semantics and visual dynamics
- Flow matching-based action decoder as Inverse Dynamics Model
- 10x improvement in sample efficiency over VLA architectures
- 2x faster convergence in training

---

### 6. UniVLA: Task-centric Latent Actions for Cross-embodiment Learning

Bu, Q., Yang, Y., Cai, J., Gao, S., Ren, G., Yao, M., Luo, P., & Li, H. (2025). UniVLA: Learning to Act Anywhere with Task-centric Latent Actions. *arXiv preprint arXiv:2505.06111*. https://arxiv.org/abs/2505.06111v3

**Summary:** UniVLA addresses limitations in existing approaches that rely heavily on action-annotated data and struggle with cross-embodiment transfer. The key innovation is deriving task-centric action representations from videos using a latent action model in the DINO feature space, incorporating language instructions to mitigate task-irrelevant dynamics. This enables exploitation of extensive data across diverse embodiments and perspectives. UniVLA achieves superior performance over OpenVLA with less than 1/20 of pretraining compute and 1/10 of downstream data, with continuous improvements from heterogeneous data including human videos.

**Key Contributions:**
- Task-centric latent action representations from video
- DINO feature space modeling with language instruction integration
- Cross-embodiment policy learning from internet-scale videos
- Superior performance with dramatically reduced compute requirements

---

### 7. Unified Video Action Model (UVA)

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

**Summary:** UVA addresses challenges in combining video generation and action prediction by learning a joint video-action latent representation with decoupled decoding. The joint latent representation bridges visual and action domains, effectively modeling relationships between video and action sequences. Decoupled decoding via two lightweight diffusion heads enables high-speed action inference by bypassing video generation during inference. The unified framework supports diverse tasks including policy learning, forward/inverse dynamics modeling, and video observation prediction through masked input training.

**Key Contributions:**
- Joint video-action latent representation learning
- Decoupled decoding for high-speed action inference
- Versatile functionality through masked input training
- General-purpose solution without performance compromise across robotics tasks

---

### 8. Fine-Tuning Vision-Language-Action Models: Optimized Fine-Tuning Recipe

Kim, M. J., Finn, C., & Liang, P. (2025). Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success. *arXiv preprint arXiv:2502.19645*. https://arxiv.org/abs/2502.19645v2

**Summary:** This work systematically studies VLA adaptation design choices including action decoding schemes, representations, and learning objectives using OpenVLA as the base model. The resulting Optimized Fine-Tuning (OFT) recipe integrates parallel decoding, action chunking, continuous action representation, and L1 regression-based learning. OpenVLA-OFT achieves state-of-the-art results on the LIBERO benchmark, boosting success rates from 76.5% to 97.1% while increasing throughput by 26x. Real-world evaluations demonstrate successful execution of dexterous, high-frequency control tasks on bimanual ALOHA robots.

**Key Contributions:**
- Systematic analysis of VLA fine-tuning design choices
- OFT recipe: parallel decoding, action chunking, continuous representation, L1 regression
- 26x improvement in action generation throughput
- 97.1% success rate on LIBERO benchmark (from 76.5%)

---

### 9. Genie Envisioner: Unified World Foundation Platform

Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025). Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation. *arXiv preprint arXiv:2508.05635*. https://arxiv.org/abs/2508.05635v3

**Summary:** Genie Envisioner (GE) introduces a unified world foundation platform integrating policy learning, evaluation, and simulation within a video-generative framework. GE-Base is a large-scale instruction-conditioned video diffusion model capturing spatial, temporal, and semantic dynamics. GE-Act maps latent representations to executable action trajectories through flow-matching decoders. GE-Sim serves as an action-conditioned neural simulator for closed-loop policy development. The platform includes EWMBench, a standardized benchmark suite measuring visual fidelity, physical consistency, and instruction-action alignment.

**Key Contributions:**
- Integrated platform for policy learning, evaluation, and simulation
- Instruction-conditioned video diffusion model (GE-Base)
- Neural simulator (GE-Sim) for high-fidelity rollouts
- EWMBench standardized benchmark suite

---

### 10. FAST: Efficient Action Tokenization for VLAs

Pertsch, K., Stachowicz, K., Ichter, B., Driess, D., Nair, S., Vuong, Q., Mees, O., Finn, C., & Levine, S. (2025). FAST: Efficient Action Tokenization for Vision-Language-Action Models. *arXiv preprint arXiv:2501.09747*. https://arxiv.org/abs/2501.09747v1

**Summary:** This paper addresses poor performance of current action tokenization approaches for autoregressive VLA models on dexterous, high-frequency tasks. The authors propose Frequency-space Action Sequence Tokenization (FAST), a compression-based scheme using discrete cosine transform. FAST enables training autoregressive VLAs for highly dexterous tasks where standard discretization fails. FAST+ is released as a universal robot action tokenizer trained on 1M real robot trajectories, compatible with diverse action spaces and control frequencies. Combined with π0 VLA, the method scales to 10k hours of robot data, matching diffusion VLA performance with 5x reduced training time.

**Key Contributions:**
- DCT-based compression tokenization for continuous actions
- FAST+ universal tokenizer trained on 1M trajectories
- Enables autoregressive VLAs for high-frequency dexterous tasks
- 5x training time reduction while matching diffusion VLA performance

---

## Thematic Analysis

### 1. Unified Architectures

A dominant theme across the reviewed literature is the move toward unified architectures that jointly model video and action. Six papers (Zhu et al., 2025; Li et al., 2025; Cen et al., 2025; Liao et al., 2025; Cheang et al., 2024; Pai et al., 2025) propose frameworks integrating video diffusion and action prediction within single architectures. This unification enables models to learn physical dynamics from video data while simultaneously generating appropriate actions, addressing the fundamental limitation of traditional VLAs that must implicitly infer dynamics from action trajectories alone.

### 2. Cross-embodiment Transfer

Three papers explicitly address cross-embodiment transfer capabilities (Ye et al., 2026; Bu et al., 2025; Pai et al., 2025). DreamZero demonstrates few-shot embodiment adaptation with only 30 minutes of play data, while UniVLA achieves transfer through task-centric latent actions learned in DINO feature space. This capability is critical for scalable robot deployment across diverse hardware platforms without extensive retraining.

### 3. Efficiency and Real-time Performance

Multiple works address computational efficiency challenges. Ye et al. (2026) enable 7Hz closed-loop control with 14B parameter models through system optimizations. Kim et al. (2025) achieve 26x throughput improvement through parallel decoding and optimized fine-tuning. Pertsch et al. (2025) reduce training time by 5x while maintaining performance through efficient action tokenization. These advances make world action models increasingly practical for real-world deployment.

### 4. Leveraging Internet-scale Video Data

Five papers emphasize pretraining on large-scale internet video data (Cheang et al., 2024; Zhu et al., 2025; Bu et al., 2025; Pai et al., 2025; Ye et al., 2026). GR-2's pretraining on 38M video clips exemplifies this trend. This approach addresses the data scarcity problem in robotics by leveraging readily available video data to learn world dynamics before fine-tuning on limited robot trajectories.

### 5. Diffusion-based Architectures

Diffusion models emerge as the dominant architectural choice, appearing in seven papers (Zhu et al., 2025; Li et al., 2025; Pai et al., 2025; Liao et al., 2025; Ye et al., 2026; Kim et al., 2025; Pertsch et al., 2025). The flexibility of diffusion processes enables unified modeling of video and action through independent timestep control, supporting diverse functionalities including policy learning, dynamics prediction, and video generation from single models.

---

## Research Gaps and Future Directions

### 1. Physical Consistency Validation

While several papers claim improved physical understanding through video-based pretraining, only Genie Envisioner (Liao et al., 2025) provides standardized benchmarks (EWMBench) for measuring physical consistency. Future work should establish rigorous evaluation protocols for assessing whether world models truly capture physical dynamics versus superficial visual correlations.

### 2. Theoretical Understanding of Error Propagation

WorldVLA (Cen et al., 2025) identifies error propagation in autoregressive action generation but provides only heuristic mitigation through attention masking. Theoretical analysis of error propagation mechanisms in world action models remains an open research direction.

### 3. Human-Robot Transfer Learning

DreamZero (Ye et al., 2026) demonstrates promising results with human video demonstrations, but systematic study of sim-to-real and human-to-robot transfer remains limited. Understanding the domain gap and developing principled transfer methods warrants further investigation.

### 4. Computational Accessibility

Despite efficiency improvements, many approaches still require substantial computational resources (e.g., 14B parameter models, 38M video pretraining). Research on making world action models accessible to researchers with limited compute resources remains important for democratizing progress.

---

## Conclusion

The reviewed literature demonstrates rapid progress in World Action Models from 2024 to 2026. The field has converged on unified architectures combining video diffusion and action prediction, leveraging internet-scale video data for pretraining, and achieving remarkable improvements in generalization, sample efficiency, and cross-embodiment transfer. Key challenges remain in physical consistency validation, theoretical understanding of error propagation, and computational accessibility. The integration of world modeling with action prediction represents a promising paradigm shift toward more physically grounded and generalizable robot learning systems.

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

---

**Search Methodology:**
- Database: arXiv
- Category: cs.RO (Robotics)
- Date Range: June 18, 2024 – June 17, 2026
- Initial Pool: 50 papers + 92 cited references
- Shortlisted: 30 papers
- Final Selection: 10 papers based on centrality to World Action Models topic
- Screening Criteria: Focus on world models, action models, or world action models in robotics and planning contexts
