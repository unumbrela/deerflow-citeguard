# Systematic Literature Review: Advances in GRPO for Generation Models

**Review Period:** February 21, 2024 – February 20, 2026  
**Category:** cs.LG (Machine Learning)  
**Format:** APA Style

---

## Executive Summary

This systematic literature review examines recent advances in Group Relative Policy Optimization (GRPO) and related reinforcement learning methods for generation models. The review encompasses 10 peer-reviewed papers published between February 2024 and February 2026 in the cs.LG category. The selected papers demonstrate significant developments in RL-based fine-tuning approaches for large language models and diffusion models, with GRPO emerging as a central algorithm enabling breakthrough capabilities in reasoning and generation tasks.

Key themes identified include: (1) theoretical understanding of GRPO's mechanisms, (2) efficiency improvements through novel variants, (3) extensions to multi-layer and adaptive frameworks, (4) applications to diffusion models, and (5) open-source implementations enabling reproducibility.

---

## Methodology

### Search Strategy
A systematic search was conducted in the arXiv repository for papers published between February 21, 2024, and February 2026, within the cs.LG (Machine Learning) category. The search query focused on "GRPO generation models" to capture papers addressing Group Relative Policy Optimization and related policy optimization methods for generative AI systems.

### Selection Criteria
Papers were included based on the following criteria:
- Primary focus on GRPO, policy optimization, or reinforcement learning for generation models
- Publication date between February 21, 2024, and February 2020
- Primary category cs.LG
- Peer-reviewed preprints with substantial technical contributions

### Screening Process
From an initial pool of 50 papers, citation expansion added 58 additional papers from references. A total of 30 papers were shortlisted and screened. Papers were scored based on their centrality to GRPO and generation models, with the top 10 most-cited and relevant papers selected for this review.

---

## Annotated Bibliography (APA Format)

### 1. Sequence-Level Policy Optimization

Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C., Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J., & Lin, J. (2025). Group Sequence Policy Optimization. *arXiv preprint arXiv:2507.18071*. https://arxiv.org/abs/2507.18071v2

**Summary:** This paper introduces Group Sequence Policy Optimization (GSPO), a stable and efficient RL algorithm for training large language models. Unlike previous approaches using token-level importance ratios, GSPO defines importance ratios based on sequence likelihood with sequence-level clipping, rewarding, and optimization. The authors demonstrate that GSPO achieves superior training efficiency and performance compared to GRPO, particularly stabilizing Mixture-of-Experts (MoE) RL training. The method has contributed to improvements in the Qwen3 models.

**Key Contributions:**
- Novel sequence-level importance ratio definition
- Improved stability for MoE RL training
- Demonstrated superiority over GRPO in training efficiency

**Relevance to GRPO:** Direct extension and improvement of GRPO methodology.

---

### 2. Theoretical Analysis of GRPO

Wu, Y., Ma, L., Ding, L., Li, M., Wang, X., Chen, K., Su, Z., Zhang, Z., Huang, C., Zhang, Y., Coates, M., & Nie, J.-Y. (2025). It Takes Two: Your GRPO Is Secretly DPO. *arXiv preprint arXiv:2510.00977*. https://arxiv.org/abs/2510.00977v3

**Summary:** This paper challenges the prevailing view that GRPO's efficacy stems from large group sizes for accurate statistical estimates. Instead, the authors propose that GRPO's effectiveness arises from its implicit contrastive objective, which reduces variance via the control variate method, making it structurally related to preference learning methods like DPO. This insight motivates 2-GRPO, a variant using only two rollouts to construct contrastive signals. Theoretical analysis and empirical validation show that 2-GRPO retains 97.6% of 16-GRPO's performance while requiring only 12.5% of rollouts and 21% of training time.

**Key Contributions:**
- Theoretical analysis revealing GRPO's contrastive nature
- 2-GRPO variant with minimal group size
- 79% reduction in training time with minimal performance loss

**Relevance to GRPO:** Fundamental theoretical understanding and efficiency improvement.

---

### 3. Minimalist RL Approaches

Xiong, W., Yao, J., Xu, Y., Pang, B., Wang, L., Sahoo, D., Li, J., Jiang, N., Zhang, T., Xiong, C., & Dong, H. (2025). A Minimalist Approach to LLM Reasoning: From Rejection Sampling to REINFORCE. *arXiv preprint arXiv:2504.11343*. https://arxiv.org/abs/2504.11343v2

**Summary:** This work revisits GRPO from a REINFORCE-like algorithm perspective to understand its effectiveness. Surprisingly, the authors find that a simple rejection sampling baseline (RAFT), training only on positively rewarded samples, yields competitive performance compared to GRPO and PPO. Ablation studies reveal that GRPO's main advantage arises from discarding prompts with entirely incorrect responses rather than from reward normalization. The proposed Reinforce-Rej extension filters both entirely incorrect and entirely correct samples, improving KL efficiency and stability.

**Key Contributions:**
- Critical analysis of GRPO's core components
- RAFT baseline demonstrating competitive performance
- Reinforce-Rej as a lightweight alternative

**Relevance to GRPO:** Provides foundational understanding of GRPO's mechanisms and simpler alternatives.

---

### 4. Multi-Layer Extensions

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-Layer GRPO: Enhancing Reasoning and Self-Correction in Large Language Models. *arXiv preprint arXiv:2506.04746*. https://arxiv.org/abs/2506.04746v1

**Summary:** Addressing GRPO's lack of intermediate supervision, this paper proposes MGRPO (Multi-layer GRPO) operating in two layers. The first layer employs standard GRPO to generate initial responses, while the second layer is trained to identify and correct errors, creating a self-correction loop. This mechanism provides implicit process-level supervision without requiring explicit reward models. Experimental results on mathematical reasoning benchmarks demonstrate MGRPO's superior performance over standard GRPO.

**Key Contributions:**
- Two-layer architecture enabling self-correction
- Implicit process-level supervision
- Enhanced reasoning capabilities

**Relevance to GRPO:** Novel architectural extension improving GRPO's reasoning and stability.

---

### 5. Diffusion Model Applications

Zheng, K., Chen, H., Ye, H., Wang, H., Zhang, Q., Jiang, K., Su, H., Ermon, S., Zhu, J., & Liu, M.-Y. (2025). DiffusionNFT: Online Diffusion Reinforcement with Forward Process. *arXiv preprint arXiv:2509.16117*. https://arxiv.org/abs/2509.16117v2

**Summary:** This paper addresses the challenge of extending online RL to diffusion models, where likelihood estimation is intractable. While recent works discretize reverse sampling for GRPO-style training, they inherit drawbacks including solver restrictions and forward-reverse inconsistency. The authors introduce DiffusionNFT, optimizing diffusion models directly on the forward process via flow matching. DiffusionNFT contrasts positive and negative generations, enabling training with arbitrary black-box solvers without likelihood estimation. The method is up to 25× more efficient than FlowGRPO.

**Key Contributions:**
- Forward process optimization for diffusion models
- Elimination of likelihood estimation requirements
- 25× efficiency improvement over FlowGRPO

**Relevance to GRPO:** Extends GRPO-style RL to diffusion generative models with significant efficiency gains.

---

### 6. Adaptive Policy Optimization

Gao, C., Zheng, C., Chen, X.-H., Dang, K., Liu, S., Li, S., Yu, B., Yang, A., Bai, S., Zhou, J., & Lin, J. (2025). Soft Adaptive Policy Optimization. *arXiv preprint arXiv:2511.20347*. https://arxiv.org/abs/2511.20347v2

**Summary:** This paper proposes Soft Adaptive Policy Optimization (SAPO), addressing the high variance in token-level importance ratios that leads to unstable updates, particularly in Mixture-of-Experts models. SAPO replaces hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates while preserving useful learning signals. Compared to GSPO and GRPO, SAPO is both sequence-coherent and token-adaptive, selectively down-weighting only off-policy tokens while preserving learning signals from near-on-policy ones.

**Key Contributions:**
- Soft gating mechanism replacing hard clipping
- Token-adaptive updates with sequence coherence
- Improved training stability and Pass@1 performance

**Relevance to GRPO:** Addresses stability limitations in GRPO and GSPO through adaptive smoothing.

---

### 7. Open-Source RL Systems

Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai, W., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., & Zhu, H. (2025). DAPO: An Open-Source LLM Reinforcement Learning System at Scale. *arXiv preprint arXiv:2503.14476*. https://arxiv.org/abs/2503.14476v2

**Summary:** This paper addresses the lack of reproducibility in state-of-the-art reasoning LLMs, where key technical details remain concealed. The authors propose DAPO (Decoupled Clip and Dynamic Sampling Policy Optimization) and fully open-source a large-scale RL system achieving 50 points on AIME 2024 using Qwen2.5-32B base model. Four key techniques are introduced, along with open-source training code built on the verl framework and a curated dataset.

**Key Contributions:**
- Fully open-source large-scale RL system
- Decoupled clip and dynamic sampling techniques
- Reproducible achievement of state-of-the-art results

**Relevance to GRPO:** Provides open-source infrastructure and techniques for GRPO-style training at scale.

---

### 8. Off-Policy Guidance

Yan, J., Li, Y., Hu, Z., Wang, Z., Cui, G., Qu, X., Cheng, Y., & Zhang, Y. (2025). Learning to Reason under Off-Policy Guidance. *arXiv preprint arXiv:2504.14945*. https://arxiv.org/abs/2504.14945v5

**Summary:** This paper addresses the limitation of existing RLVR (Reinforcement Learning with Verifiable Rewards) approaches being inherently on-policy, restricting learning to a model's own outputs. The authors introduce LUFFY (Learning to Reason Under oFF-policY guidance), augmenting RLVR with off-policy reasoning traces. LUFFY combines Mixed-Policy GRPO with theoretically guaranteed convergence and policy shaping via regularized importance sampling. The framework achieves over +6.4 average gain across six math benchmarks and +6.2 points in out-of-distribution tasks.

**Key Contributions:**
- Mixed-Policy GRPO framework with convergence guarantees
- Dynamic balance between imitation and exploration
- Successful training of weak models where on-policy RLVR fails

**Relevance to GRPO:** Extends GRPO to off-policy settings, overcoming fundamental limitations.

---

### 9. Scalable Base Model Training

Hu, J., Zhang, Y., Han, Q., Jiang, D., Zhang, X., & Shum, H.-Y. (2025). Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model. *arXiv preprint arXiv:2503.24290*. https://arxiv.org/abs/2503.24290v2

**Summary:** This paper introduces Open-Reasoner-Zero, the first open-source implementation of large-scale reasoning-oriented RL training on base models focusing on scalability, simplicity, and accessibility. The authors demonstrate that vanilla PPO with GAE (λ=1, γ=1) and straightforward rule-based rewards, without KL regularization, is sufficient to replicate the scaling phenomenon observed in DeepSeek-R1-Zero. Using Qwen2.5-32B base, the implementation achieves superior performance across AIME2024, MATH500, and GPQA Diamond with only 1/10 of the training steps.

**Key Contributions:**
- Minimalist approach achieving state-of-the-art results
- 10× improvement in training efficiency
- Open-source code, data, and model weights

**Relevance to GRPO:** Demonstrates that simpler approaches can match GRPO-based systems, with full reproducibility.

---

### 10. Flow and Diffusion Fine-tuning

Domingo-Enrich, C., Drozdzal, M., Karrer, B., & Chen, R. T. Q. (2024). Adjoint Matching: Fine-tuning Flow and Diffusion Generative Models with Memoryless Stochastic Optimal Control. *arXiv preprint arXiv:2409.08861*. https://arxiv.org/abs/2409.08861v5

**Summary:** This paper addresses reward fine-tuning for dynamical generative models including Flow Matching and diffusion models. The authors cast reward fine-tuning as stochastic optimal control (SOC) and prove that a specific memoryless noise schedule must be enforced during fine-tuning. They propose Adjoint Matching, casting SOC problems as regression problems. The approach achieves better consistency, realism, and generalization to unseen human preference reward models while retaining sample diversity.

**Key Contributions:**
- Theoretically-sound SOC formulation for fine-tuning
- Memoryless noise schedule enforcement
- Superior performance in reward fine-tuning

**Relevance to GRPO:** Provides alternative theoretical framework for RL-based fine-tuning of generative models.

---

## Thematic Analysis

### Theme 1: Theoretical Understanding

Several papers provide fundamental insights into why GRPO works. Wu et al. (2025) reveal that GRPO's effectiveness stems from implicit contrastive learning rather than group statistics, while Xiong et al. (2025) demonstrate that simpler rejection sampling can achieve competitive results. These findings challenge assumptions about GRPO's necessity for complex mechanisms.

### Theme 2: Efficiency Improvements

Multiple works focus on improving GRPO's efficiency. The 2-GRPO variant (Wu et al., 2025) reduces training time by 79% with minimal performance loss. DiffusionNFT (Zheng et al., 2025) achieves 25× efficiency gains for diffusion models. Open-Reasoner-Zero (Hu et al., 2025) requires only 1/10 of training steps compared to DeepSeek-R1-Zero.

### Theme 3: Stability and Adaptivity

Stability improvements are addressed through sequence-level optimization (Zheng et al., 2025), soft adaptive gating (Gao et al., 2025), and multi-layer architectures (Ding et al., 2025). These approaches tackle the high variance problem in token-level updates, particularly important for MoE models.

### Theme 4: Extended Applications

GRPO-style methods are successfully extended to diffusion models (Zheng et al., 2025; Domingo-Enrich et al., 2024) and off-policy settings (Yan et al., 2025), demonstrating the versatility of the core approach beyond language models.

### Theme 5: Open-Source Reproducibility

A significant trend toward open-source implementations (Yu et al., 2025; Hu et al., 2025) addresses the reproducibility crisis in large-scale RL training, providing the community with accessible tools and benchmarks.

---

## Conclusions and Future Directions

The literature from 2024-2026 reveals rapid advancement in GRPO and related policy optimization methods for generation models. Key findings include:

1. **Simplicity vs. Complexity:** Surprisingly, simpler approaches like RAFT and vanilla PPO can match GRPO performance, suggesting that core mechanisms rather than complexity drive success.

2. **Efficiency Gains:** New variants achieve order-of-magnitude improvements in training efficiency while maintaining or improving performance.

3. **Theoretical Grounding:** Better theoretical understanding reveals GRPO's contrastive nature and enables more principled design.

4. **Broader Applications:** Successful extension to diffusion models and off-policy settings demonstrates GRPO's versatility.

5. **Reproducibility:** Open-source initiatives are critical for community progress and validation.

**Future Research Directions:**
- Further theoretical analysis of policy optimization mechanisms
- Integration of off-policy and on-policy learning
- Extension to multimodal generation models
- Development of standardized benchmarks and evaluation protocols
- Investigation of sample efficiency improvements

---

## References

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-Layer GRPO: Enhancing Reasoning and Self-Correction in Large Language Models. *arXiv preprint arXiv:2506.04746*. https://arxiv.org/abs/2506.04746v1

Domingo-Enrich, C., Drozdzal, M., Karrer, B., & Chen, R. T. Q. (2024). Adjoint Matching: Fine-tuning Flow and Diffusion Generative Models with Memoryless Stochastic Optimal Control. *arXiv preprint arXiv:2409.08861*. https://arxiv.org/abs/2409.08861v5

Gao, C., Zheng, C., Chen, X.-H., Dang, K., Liu, S., Li, S., Yu, B., Yang, A., Bai, S., Zhou, J., & Lin, J. (2025). Soft Adaptive Policy Optimization. *arXiv preprint arXiv:2511.20347*. https://arxiv.org/abs/2511.20347v2

Hu, J., Zhang, Y., Han, Q., Jiang, D., Zhang, X., & Shum, H.-Y. (2025). Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model. *arXiv preprint arXiv:2503.24290*. https://arxiv.org/abs/2503.24290v2

Wu, Y., Ma, L., Ding, L., Li, M., Wang, X., Chen, K., Su, Z., Zhang, Z., Huang, C., Zhang, Y., Coates, M., & Nie, J.-Y. (2025). It Takes Two: Your GRPO Is Secretly DPO. *arXiv preprint arXiv:2510.00977*. https://arxiv.org/abs/2510.00977v3

Xiong, W., Yao, J., Xu, Y., Pang, B., Wang, L., Sahoo, D., Li, J., Jiang, N., Zhang, T., Xiong, C., & Dong, H. (2025). A Minimalist Approach to LLM Reasoning: From Rejection Sampling to REINFORCE. *arXiv preprint arXiv:2504.11343*. https://arxiv.org/abs/2504.11343v2

Yan, J., Li, Y., Hu, Z., Wang, Z., Cui, G., Qu, X., Cheng, Y., & Zhang, Y. (2025). Learning to Reason under Off-Policy Guidance. *arXiv preprint arXiv:2504.14945*. https://arxiv.org/abs/2504.14945v5

Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai, W., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., & Zhu, H. (2025). DAPO: An Open-Source LLM Reinforcement Learning System at Scale. *arXiv preprint arXiv:2503.14476*. https://arxiv.org/abs/2503.14476v2

Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C., Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J., & Lin, J. (2025). Group Sequence Policy Optimization. *arXiv preprint arXiv:2507.18071*. https://arxiv.org/abs/2507.18071v2

Zheng, K., Chen, H., Ye, H., Wang, H., Zhang, Q., Jiang, K., Su, H., Ermon, S., Zhu, J., & Liu, M.-Y. (2025). DiffusionNFT: Online Diffusion Reinforcement with Forward Process. *arXiv preprint arXiv:2509.16117*. https://arxiv.org/abs/2509.16117v2

---

**Review Completed:** October 26, 2026  
**Total Papers Reviewed:** 10  
**Publication Window:** February 21, 2024 – February 20, 2026
