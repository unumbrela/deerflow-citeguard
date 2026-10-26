# Systematic Literature Review: World Models for Robotic Manipulation

**Review Date:** October 26, 2026  
**Search Period:** May 27, 2024 – May 26, 2026  
**Category:** cs.RO (Robotics)  
**Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in world models for robotic manipulation published between May 2024 and May 2026. The selected papers demonstrate a clear trend toward unified architectures that integrate video prediction, action generation, and latent dynamics modeling. Key innovations include diffusion-based world models, latent action learning from action-free videos, and 3D-aware generative frameworks. The reviewed works collectively advance the field toward scalable, generalizable robot learning that leverages both robotic demonstrations and internet-scale video data.

---

## Methodology

### Search Strategy
Papers were identified through arXiv search in the cs.RO (Robotics) category with the query "world models robotic manipulation." The search returned 50 initial matches, expanded to 145 papers through citation analysis, and shortlisted to 30 candidates. Papers were screened based on relevance to world models, latent dynamics, or predictive modeling applied to robotic manipulation tasks.

### Inclusion Criteria
- Published between May 27, 2024 and May 26, 2026
- Primary category: cs.RO (Robotics)
- Focus on world models, latent dynamics, or predictive models for robotic manipulation
- Empirical validation through simulation or real-world experiments

### Selection Process
Papers were scored based on centrality to the topic, citation impact, and methodological contribution. The 10 most central papers were selected for this review.

---

## Reviewed Papers (APA Format)

### 1. Unified World Models: Coupling Video and Action Diffusion

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3

**Key Contribution:** Introduces Unified World Models (UWM), a framework integrating action diffusion and video diffusion within a unified transformer architecture. UWM enables flexible representation of policies, forward/inverse dynamics, and video generation through independent control of modality-specific diffusion timesteps.

**Methodology:** Combines imitation learning with world modeling by leveraging both action-annotated robot data and action-free video data. The unified architecture allows pretraining on large-scale heterogeneous datasets.

**Results:** Demonstrates improved generalization and robustness compared to pure imitation learning. Enables effective pretraining on video data without action labels, further enhancing policy performance after finetuning.

---

### 2. WorldVLA: Towards Autoregressive Action World Model

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards Autoregressive Action World Model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

**Key Contribution:** Presents WorldVLA, an autoregressive action world model unifying Vision-Language-Action (VLA) models with world modeling. The framework enables mutual enhancement between action generation and future image prediction.

**Methodology:** Integrates VLA and world model in a single framework where the world model predicts future images using action and image understanding, while the action model generates actions based on visual observations.

**Results:** Outperforms standalone action and world models. Identifies error propagation in autoregressive action generation and proposes an attention mask strategy that selectively masks prior actions, significantly improving action chunk generation.

---

### 3. Latent Action Pretraining from Videos

Ye, S., Jang, J., Jeon, B., Joo, S., Yang, J., Peng, B., Mandlekar, A., Tan, R., Chao, Y.-W., Lin, B. Y., Liden, L., Lee, K., Gao, J., Zettlemoyer, L., Fox, D., & Seo, M. (2024). Latent Action Pretraining from Videos. *arXiv preprint arXiv:2410.11758*. https://arxiv.org/abs/2410.11758v2

**Key Contribution:** Introduces LAPA (Latent Action Pretraining for general Action models), an unsupervised method for pretraining VLA models without ground-truth robot action labels using internet-scale videos.

**Methodology:** Employs VQ-VAE-based objective to learn discrete latent actions between image frames, pretrains a latent VLA model to predict these actions from observations and task descriptions, then finetunes on small-scale robot manipulation data.

**Results:** Significantly outperforms existing techniques for training robot manipulation policies from large-scale videos. Outperforms state-of-the-art VLA models trained with robotic action labels on tasks requiring language conditioning and semantic generalization.

---

### 4. Unified Video Action Model

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

**Key Contribution:** Proposes UVA (Unified Video Action model), which jointly optimizes video and action predictions through a joint video-action latent representation and decoupled decoding.

**Methodology:** Learns joint video-action latent representation bridging visual and action domains, with decoupled decoding powered by lightweight diffusion heads enabling high-speed action inference without video generation.

**Results:** Achieves both high accuracy and efficient action inference. Serves as a general-purpose solution for policy learning, forward/inverse dynamics, and video observation prediction without compromising performance compared to task-specific methods.

---

### 5. UniVLA: Learning to Act Anywhere with Task-centric Latent Actions

Bu, Q., Yang, Y., Cai, J., Gao, S., Ren, G., Yao, M., Luo, P., & Li, H. (2025). UniVLA: Learning to Act Anywhere with Task-centric Latent Actions. *arXiv preprint arXiv:2505.06111*. https://arxiv.org/abs/2505.06111v3

**Key Contribution:** Develops UniVLA, a framework for learning cross-embodiment VLA policies using task-centric action representations derived from videos with a latent action model.

**Methodology:** Incorporates language instructions and establishes a latent action model within the DINO feature space to mitigate task-irrelevant dynamics. Learns from internet-scale videos across diverse embodiments and perspectives.

**Results:** Achieves state-of-the-art results across multiple manipulation and navigation benchmarks with less than 1/20 of pretraining compute and 1/10 of downstream data compared to OpenVLA. Demonstrates continuous improvement with heterogeneous data including human videos.

---

### 6. DreamGen: Unlocking Generalization in Robot Learning through Video World Models

Jang, J., Ye, S., Lin, Z., Xiang, J., Bjorck, J., Fang, Y., Hu, F., Huang, S., Kundalia, K., Lin, Y.-C., Magne, L., Mandlekar, A., Narayan, A., Tan, Y. L., Wang, G., Wang, J., Wang, Q., Xu, Y., Zeng, X., & Zheng, K. (2025). DreamGen: Unlocking Generalization in Robot Learning through Video World Models. *arXiv preprint arXiv:2505.12705*. https://arxiv.org/abs/2505.12705v2

**Key Contribution:** Introduces DreamGen, a 4-stage pipeline for training robot policies that generalize across behaviors and environments through neural trajectories—synthetic robot data generated from video world models.

**Methodology:** Leverages image-to-video generative models adapted to target robot embodiments to produce photorealistic synthetic videos. Recovers pseudo-action sequences using latent action models or inverse dynamics models.

**Results:** Enables a humanoid robot to perform 22 new behaviors in seen and unseen environments with teleoperation data from only a single pick-and-place task. Introduces DreamGen Bench showing strong correlation between video generation performance and downstream policy success.

---

### 7. EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation

Huang, S., Chen, L., Zhou, P., Chen, S., Jiang, Z., Hu, Y., Liao, Y., Gao, P., Li, H., Yao, M., & Ren, G. (2025). EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation. *arXiv preprint arXiv:2501.01895*. https://arxiv.org/abs/2501.01895v3

**Key Contribution:** Presents EnerVerse, a generative robotics foundation model employing chunk-wise autoregressive video diffusion with sparse context memory for long-term reasoning and multi-view video representation.

**Methodology:** Uses multi-view video representation for 3D robotics world modeling, addressing motion ambiguity and 3D grounding. Introduces EnerVerse-D, a data engine combining generative modeling with 4D Gaussian Splatting for sim-to-real gap reduction.

**Results:** Achieves state-of-the-art performance in simulation and real-world tasks. EnerVerse-A achieves approximately 280 ms per 8-step action chunk on a single RTX 4090 through feature reuse from the first denoising step.

---

### 8. Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

Tian, Y., Yang, S., Zeng, J., Wang, P., Lin, D., Dong, H., & Pang, J. (2024). Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation. *arXiv preprint arXiv:2412.15109*. https://arxiv.org/abs/2412.15109v1

**Key Contribution:** Proposes PIDM (Predictive Inverse Dynamics Models), an end-to-end paradigm predicting actions using inverse dynamics models conditioned on forecasted visual states, implemented as Seer.

**Methodology:** Uses Transformers to process both visual states and actions in an end-to-end framework. Pre-trained on large-scale robotic datasets (e.g., DROID) with minimal fine-tuning for real-world adaptation.

**Results:** Achieves 13% improvement on LIBERO-LONG, 21% on CALVIN ABC-D, and 43% in real-world tasks. Sets new state-of-the-art on CALVIN ABC-D with average length of 4.28. Exhibits superior generalization for novel objects, lighting conditions, and environments.

---

### 9. Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation

Bharadhwaj, H., Dwibedi, D., Gupta, A., Tulsiani, S., Doersch, C., Xiao, T., Shah, D., Xia, F., Sadigh, D., & Kirmani, S. (2024). Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation. *arXiv preprint arXiv:2409.16283*. https://arxiv.org/abs/2409.16283v1

**Key Contribution:** Introduces Gen2Act, casting language-conditioned manipulation as zero-shot human video generation followed by execution with a single policy conditioned on generated video.

**Methodology:** Leverages pre-trained video generation models on web data to predict motion information for novel scenarios without fine-tuning. Uses an order of magnitude less robot interaction data compared to video prediction model training.

**Results:** Enables manipulation of unseen object types and novel motions not present in robot training data. Demonstrates generalization to diverse real-world scenarios through web-scale video generation.

---

### 10. GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards Scalable Gaussian World Models for Robotic Manipulation. *arXiv preprint arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

**Key Contribution:** Proposes GWM (Gaussian World Model), reconstructing future states by inferring propagation of Gaussian primitives under robot actions using latent Diffusion Transformer with 3D variational autoencoder.

**Methodology:** Enables fine-grained scene-level future state reconstruction with Gaussian Splatting. Serves both as visual representation enhancer for imitation learning and as neural simulator for model-based reinforcement learning.

**Results:** Precisely predicts future scenes conditioned on diverse robot actions in both simulated and real-world experiments. Trains policies outperforming state-of-the-art by significant margins, demonstrating initial data scaling potential of 3D world models.

---

## Thematic Analysis

### Theme 1: Unified Architectures
Multiple papers (Zhu et al., 2025; Li et al., 2025; Cen et al., 2025) converge on unified architectures integrating video prediction and action generation. This represents a shift from separate perception and control modules toward end-to-end frameworks where visual and action domains share latent representations.

### Theme 2: Learning from Action-Free Videos
A significant trend involves leveraging internet-scale videos without action annotations (Ye et al., 2024; Bu et al., 2025; Jang et al., 2025). Latent action models enable knowledge transfer from human manipulation videos to robot policies, dramatically expanding available training data.

### Theme 3: 3D and Geometric Awareness
Recent work emphasizes 3D-aware world models (Huang et al., 2025; Lu et al., 2025) using multi-view representations and Gaussian Splatting. This addresses limitations of image-based models lacking consistent spatial and physical understanding.

### Theme 4: Synthetic Data Generation
DreamGen (Jang et al., 2025) and Gen2Act (Bharadhwaj et al., 2024) demonstrate video world models as neural simulators generating synthetic training data. This approach scales beyond manual data collection constraints.

### Theme 5: Efficiency and Speed
Several works address inference efficiency through decoupled decoding (Li et al., 2025), feature reuse (Huang et al., 2025), and attention mechanisms (Cen et al., 2025), achieving real-time performance suitable for deployment.

---

## Comparative Summary

| Paper | Key Innovation | Data Source | 3D Awareness | Real-World Validation |
|-------|---------------|-------------|--------------|----------------------|
| Zhu et al. (2025) | Unified diffusion for video + action | Robot + video datasets | No | Yes |
| Cen et al. (2025) | Autoregressive VLA + world model | Robot data | No | Not specified |
| Ye et al. (2024) | Latent action from videos | Internet videos | No | Yes |
| Li et al. (2025) | Joint video-action latent | Robot data | No | Not specified |
| Bu et al. (2025) | Task-centric latent actions | Internet videos | No | Yes |
| Jang et al. (2025) | Synthetic neural trajectories | Generated videos | No | Yes |
| Huang et al. (2025) | Multi-view + 4D Gaussian Splatting | Robot + synthetic | Yes | Yes |
| Tian et al. (2024) | Predictive inverse dynamics | Robot datasets | No | Yes |
| Bharadhwaj et al. (2024) | Zero-shot human video generation | Web videos | No | Yes |
| Lu et al. (2025) | Gaussian primitives propagation | Robot data | Yes | Yes |

---

## Research Gaps and Future Directions

### Identified Gaps
1. **Limited Cross-Embodiment Transfer:** While UniVLA (Bu et al., 2025) addresses this, most approaches remain embodiment-specific.
2. **Simulation-to-Real Gap:** Despite advances (Huang et al., 2025; Lu et al., 2025), robust sim-to-real transfer remains challenging.
3. **Long-Horizon Reasoning:** Current models focus on short-term prediction; long-horizon task planning needs further development.
4. **Evaluation Standardization:** Diverse benchmarks (LIBERO, CALVIN, custom tasks) complicate cross-paper comparison.

### Future Directions
1. **Multimodal Integration:** Incorporating audio, tactile, and haptic feedback into world models.
2. **Causal Reasoning:** Moving beyond correlation-based prediction to causal understanding of physical interactions.
3. **Human-Robot Collaboration:** World models supporting collaborative tasks with dynamic human partners.
4. **Energy-Efficient Inference:** Reducing computational requirements for edge deployment.
5. **Safety Guarantees:** Integrating formal verification with learned world models for safe deployment.

---

## Conclusion

The reviewed literature demonstrates rapid progress in world models for robotic manipulation, with clear trends toward unified architectures, latent action learning from action-free videos, 3D-aware representations, and synthetic data generation. The field is moving beyond pure imitation learning toward frameworks that leverage internet-scale video data while maintaining real-world applicability. Key challenges remain in cross-embodiment transfer, long-horizon reasoning, and evaluation standardization. The convergence of diffusion models, latent action representations, and 3D reconstruction techniques positions world models as a foundational technology for scalable, generalizable robot learning.

---

## References

Bharadhwaj, H., Dwibedi, D., Gupta, A., Tulsiani, S., Doersch, C., Xiao, T., Shah, D., Xia, F., Sadigh, D., & Kirmani, S. (2024). Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation. *arXiv preprint arXiv:2409.16283*. https://arxiv.org/abs/2409.16283v1

Bu, Q., Yang, Y., Cai, J., Gao, S., Ren, G., Yao, M., Luo, P., & Li, H. (2025). UniVLA: Learning to Act Anywhere with Task-centric Latent Actions. *arXiv preprint arXiv:2505.06111*. https://arxiv.org/abs/2505.06111v3

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards Autoregressive Action World Model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

Huang, S., Chen, L., Zhou, P., Chen, S., Jiang, Z., Hu, Y., Liao, Y., Gao, P., Li, H., Yao, M., & Ren, G. (2025). EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation. *arXiv preprint arXiv:2501.01895*. https://arxiv.org/abs/2501.01895v3

Jang, J., Ye, S., Lin, Z., Xiang, J., Bjorck, J., Fang, Y., Hu, F., Huang, S., Kundalia, K., Lin, Y.-C., Magne, L., Mandlejar, A., Narayan, A., Tan, Y. L., Wang, G., Wang, J., Wang, Q., Xu, Y., Zeng, X., & Zheng, K. (2025). DreamGen: Unlocking Generalization in Robot Learning through Video World Models. *arXiv preprint arXiv:2505.12705*. https://arxiv.org/abs/2505.12705v2

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards Scalable Gaussian World Models for Robotic Manipulation. *arXiv preprint arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

Tian, Y., Yang, S., Zeng, J., Wang, P., Lin, D., Dong, H., & Pang, J. (2024). Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation. *arXiv preprint arXiv:2412.15109*. https://arxiv.org/abs/2412.15109v1

Ye, S., Jang, J., Jeon, B., Joo, S., Yang, J., Peng, B., Mandlejar, A., Tan, R., Chao, Y.-W., Lin, B. Y., Liden, L., Lee, K., Gao, J., Zettlemoyer, L., Fox, D., & Seo, M. (2024). Latent Action Pretraining from Videos. *arXiv preprint arXiv:2410.11758*. https://arxiv.org/abs/2410.11758v2

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3

---

**Review Methodology Summary:**
- Initial pool: 50 papers from arXiv search
- Citation expansion: 95 additional papers from references
- Shortlisted: 30 papers
- Final selection: 10 papers based on centrality scores and relevance criteria
- Screening period: May 27, 2024 – May 26, 2026
- Primary category: cs.RO (Robotics)
