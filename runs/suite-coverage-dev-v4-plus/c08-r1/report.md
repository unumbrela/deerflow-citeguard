# Systematic Literature Review: Advances in GRPO for Generation Models

**Review Period:** February 21, 2024 – February 20, 2026  
**Category:** cs.LG (Machine Learning)  
**Format:** APA Style  
**Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines 10 key papers on Group Relative Policy Optimization (GRPO) and related reinforcement learning algorithms for generation models published between February 2024 and February 2026. The review reveals significant advances in understanding GRPO's mechanisms, developing more efficient variants, and extending its applications to diverse generation tasks including language reasoning, diffusion models, and multi-modal systems.

Key themes emerging from this body of work include: (1) theoretical analysis revealing GRPO's implicit contrastive nature, (2) development of more stable and sample-efficient variants, (3) extensions to multi-layer and self-correction frameworks, and (4) applications beyond language models to diffusion-based generation.

---

## Annotated Bibliography

### 1. Group Sequence Policy Optimization

**Citation:**  
Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C., Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J., & Lin, J. (2025). *Group Sequence Policy Optimization*. arXiv preprint arXiv:2507.18071. https://arxiv.org/abs/2507.18071v2

**Summary:**  
This paper introduces Group Sequence Policy Optimization (GSPO), a reinforcement learning algorithm that defines importance ratios based on sequence likelihood rather than token-level metrics. GSPO performs sequence-level clipping, rewarding, and optimization, achieving superior training efficiency and performance compared to GRPO. The algorithm notably stabilizes Mixture-of-Experts (MoE) RL training and has been instrumental in improvements to Qwen3 models.

**Key Contributions:**
- Sequence-level importance ratio definition
- Improved stability for MoE RL training
- Demonstrated superior performance over GRPO

**Relevance to GRPO:**  
GSPO represents a direct evolution from GRPO, addressing limitations in token-level optimization by operating at the sequence level.

---

### 2. It Takes Two: Your GRPO Is Secretly DPO

**Citation:**  
Wu, Y., Ma, L., Ding, L., Li, M., Wang, X., Chen, K., Su, Z., Zhang, Z., Huang, C., Zhang, Y., Coates, M., & Nie, J.-Y. (2025). *It Takes Two: Your GRPO Is Secretly DPO*. arXiv preprint arXiv:2510.00977. https://arxiv.org/abs/2510.00977v3

**Summary:**  
This paper challenges the prevailing view that GRPO's efficacy stems from large group sizes for accurate statistical estimates. Instead, the authors propose that GRPO's effectiveness arises from its implicit contrastive objective, structurally related to preference learning methods like DPO. This insight motivates 2-GRPO, a variant using only two rollouts that retains 97.6% of 16-GRPO's performance while requiring only 12.5% of rollouts and 21% of training time.

**Key Contributions:**
- Theoretical analysis revealing GRPO's contrastive nature
- 2-GRPO variant with minimal group size
- Significant efficiency improvements with maintained performance

**Relevance to GRPO:**  
Provides fundamental theoretical insights into GRPO's mechanisms and demonstrates that large group sizes are unnecessary.

---

### 3. A Minimalist Approach to LLM Reasoning: from Rejection Sampling to REINFORCE

**Citation:**  
Xiong, W., Yao, J., Xu, Y., Pang, B., Wang, L., Sahoo, D., Li, J., Jiang, N., Zhang, T., Xiong, C., & Dong, H. (2025). *A Minimalist Approach to LLM Reasoning: from Rejection Sampling to REINFORCE*. arXiv preprint arXiv:2504.11343. https://arxiv.org/abs/2504.11343v2

**Summary:**  
This work revisits GRPO from a REINFORCE-like algorithm perspective, finding that a simple rejection sampling baseline (RAFT) yields competitive performance. The main advantage of GRPO arises from discarding prompts with entirely incorrect responses rather than reward normalization. The authors propose Reinforce-Rej, filtering both entirely incorrect and entirely correct samples, improving KL efficiency and stability.

**Key Contributions:**
- Critical analysis of GRPO's effectiveness sources
- RAFT as a robust baseline
- Reinforce-Rej as a lightweight alternative

**Relevance to GRPO:**  
Questions the necessity of GRPO's complexity and advocates for simpler, more interpretable approaches.

---

### 4. Multi-Layer GRPO: Enhancing Reasoning and Self-Correction in Large Language Models

**Citation:**  
Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). *Multi-Layer GRPO: Enhancing Reasoning and Self-Correction in Large Language Models*. arXiv preprint arXiv:2506.04746. https://arxiv.org/abs/2506.04746v1

**Summary:**  
MGRPO addresses inefficient exploration dynamics in standard GRPO by introducing a two-layer architecture. The first layer generates initial responses, while the second layer identifies and corrects errors, creating a self-correction loop. This provides implicit process-level supervision without requiring densely-annotated reward models, significantly outperforming standard GRPO on mathematical reasoning benchmarks.

**Key Contributions:**
- Two-layer architecture with self-correction
- Implicit process-level supervision
- Superior performance on reasoning tasks

**Relevance to GRPO:**  
Extends GRPO to enable self-correction capabilities, addressing the single-error invalidation problem in complex reasoning chains.

---

### 5. DiffusionNFT: Online Diffusion Reinforcement with Forward Process

**Citation:**  
Zheng, K., Chen, H., Ye, H., Wang, H., Zhang, Q., Jiang, K., Su, H., Ermon, S., Zhu, J., & Liu, M.-Y. (2025). *DiffusionNFT: Online Diffusion Reinforcement with Forward Process*. arXiv preprint arXiv:2509.16117. https://arxiv.org/abs/2509.16117v2

**Summary:**  
This paper extends GRPO-style training to diffusion models through DiffusionNFT, optimizing directly on the forward process via flow matching. DiffusionNFT contrasts positive and negative generations, incorporating reinforcement signals into supervised learning. It achieves up to 25× efficiency improvement over FlowGRPO, eliminates likelihood estimation needs, and works with arbitrary black-box solvers.

**Key Contributions:**
- Extension of GRPO principles to diffusion models
- Forward process optimization via flow matching
- Dramatic efficiency improvements (25× over FlowGRPO)

**Relevance to GRPO:**  
Demonstrates GRPO's applicability beyond language models to diffusion-based generation, addressing intractable likelihood challenges.

---

### 6. Soft Adaptive Policy Optimization

**Citation:**  
Gao, C., Zheng, C., Chen, X.-H., Dang, K., Liu, S., Yu, B., Yang, A., Bai, S., Zhou, J., & Lin, J. (2025). *Soft Adaptive Policy Optimization*. arXiv preprint arXiv:2511.20347. https://arxiv.org/abs/2511.20347v2

**Summary:**  
SAPO replaces hard clipping with smooth, temperature-controlled gating that adaptively attenuates off-policy updates while preserving useful learning signals. Unlike GSPO's hard clipping that suppresses all gradients for sequences with off-policy tokens, SAPO selectively down-weights only offending tokens. Compared to GRPO, SAPO replaces hard token-level clipping with smooth scaling, enabling more informative and stable updates.

**Key Contributions:**
- Soft gating mechanism replacing hard clipping
- Token-adaptive while maintaining sequence coherence
- Improved training stability and Pass@1 performance

**Relevance to GRPO:**  
Addresses GRPO's hard clipping limitations through adaptive, smooth scaling for more stable optimization.

---

### 7. DAPO: An Open-Source LLM Reinforcement Learning System at Scale

**Citation:**  
Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai, W., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., & Zhu, H. (2025). *DAPO: An Open-Source LLM Reinforcement Learning System at Scale*. arXiv preprint arXiv:2503.14476. https://arxiv.org/abs/2503.14476v2

**Summary:**  
DAPO introduces Decoupled Clip and Dynamic Sampling Policy Optimization, achieving 50 points on AIME 2024 using Qwen2.5-32B base model. The paper open-sources a complete state-of-the-art RL system with four key techniques, training code built on the verl framework, and curated datasets, addressing the reproducibility challenges in large-scale LLM RL.

**Key Contributions:**
- Decoupled clip and dynamic sampling techniques
- Open-source large-scale RL system
- Reproducible results on reasoning benchmarks

**Relevance to GRPO:**  
Provides open-source infrastructure and techniques that complement GRPO-based approaches for large-scale training.

---

### 8. Learning to Reason under Off-Policy Guidance

**Citation:**  
Yan, J., Li, Y., Hu, Z., Wang, Z., Cui, G., Qu, X., Cheng, Y., & Zhang, Y. (2025). *Learning to Reason under Off-Policy Guidance*. arXiv preprint arXiv:2504.14945. https://arxiv.org/abs/2504.14945v5

**Summary:**  
LUFFY addresses the on-policy limitation of existing RLVR approaches by augmenting training with off-policy reasoning traces. The framework combines Mixed-Policy GRPO with theoretically guaranteed convergence and policy shaping via regularized importance sampling. LUFFY achieves +6.4 average gain across six math benchmarks and enables training in scenarios where on-policy RLVR fails completely.

**Key Contributions:**
- Off-policy guidance integration with GRPO
- Mixed-Policy GRPO framework
- Significant improvements on math benchmarks

**Relevance to GRPO:**  
Extends GRPO to incorporate off-policy demonstrations, transcending inherent on-policy limitations.

---

### 9. Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model

**Citation:**  
Hu, J., Zhang, Y., Han, Q., Jiang, D., Zhang, X., & Shum, H.-Y. (2025). *Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model*. arXiv preprint arXiv:2503.24290. https://arxiv.org/abs/2503.24290v2

**Summary:**  
This paper demonstrates that vanilla PPO with GAE (λ=1, γ=1) and rule-based rewards, without KL regularization, is sufficient to scale up reasoning performance, replicating DeepSeek-R1-Zero scaling phenomena. The approach achieves superior performance across AIME2024, MATH500, and GPQA Diamond with only 1/10 of DeepSeek-R1-Zero's training steps.

**Key Contributions:**
- Minimalist RL approach matching state-of-the-art
- Open-source implementation and models
- 10× efficiency improvement over DeepSeek-R1-Zero

**Relevance to GRPO:**  
Questions the necessity of complex algorithms like GRPO, showing that simpler approaches can achieve comparable results.

---

### 10. Tapered Off-Policy REINFORCE: Stable and Efficient Reinforcement Learning for LLMs

**Citation:**  
Le Roux, N., Bellemare, M. G., Lebensold, J., Bergeron, A., Greaves, J., Fréchette, A., Pelletier, C., Thibodeau-Laufer, E., Toth, S., & Work, S. (2025). *Tapered Off-Policy REINFORCE: Stable and Efficient Reinforcement Learning for LLMs*. arXiv preprint arXiv:2503.14286. https://arxiv.org/abs/2503.14286v2

**Summary:**  
TOPR uses asymmetric, tapered importance sampling for stable learning without KL regularization. The algorithm handles positive and negative examples in a unified framework with Monte Carlo simplicity. Experiments show TOPR matches 70B-parameter model performance with 8B models by properly leveraging both positive and negative examples in the off-policy regime.

**Key Contributions:**
- Tapered importance sampling for stability
- Unified positive/negative example handling
- Matching larger model performance with smaller models

**Relevance to GRPO:**  
Provides an alternative approach to GRPO that achieves similar goals through off-policy REINFORCE with tapered sampling.

---

## Synthesis and Analysis

### Theoretical Understanding

The reviewed literature reveals a deepening theoretical understanding of GRPO's mechanisms. Wu et al. (2025) fundamentally challenge the assumption that large group sizes are necessary, demonstrating that GRPO's efficacy stems from implicit contrastive learning rather than statistical accuracy. This insight has profound implications for efficiency, enabling 2-GRPO to achieve near-equivalent performance with minimal rollouts.

Xiong et al. (2025) and Hu et al. (2025) further question GRPO's complexity, showing that simpler approaches like rejection sampling and vanilla PPO can achieve competitive or superior results. These findings suggest that GRPO's success may be attributable to specific design choices (like discarding entirely incorrect prompts) rather than its overall algorithmic complexity.

### Algorithmic Improvements

Several papers propose direct improvements to GRPO:

1. **Stability Enhancements:** Gao et al. (2025) introduce SAPO's soft gating mechanism, replacing hard clipping with adaptive scaling for more stable updates. Zheng et al. (2025) propose GSPO's sequence-level optimization, particularly beneficial for MoE architectures.

2. **Efficiency Improvements:** Wu et al. (2025) demonstrate that minimal group sizes suffice, while Ding et al. (2025) show that multi-layer architectures with self-correction improve sample efficiency.

3. **Off-Policy Extensions:** Yan et al. (2025) and Le Roux et al. (2025) extend GRPO-related approaches to incorporate off-policy data, addressing fundamental limitations of on-policy training.

### Applications Beyond Language Models

Zheng et al. (2025) successfully extend GRPO principles to diffusion models through DiffusionNFT, achieving 25× efficiency improvements. This demonstrates GRPO's broader applicability to generation tasks beyond language, opening new research directions for multi-modal and continuous-domain generation.

### Open-Source Infrastructure

Yu et al. (2025) and Hu et al. (2025) provide crucial open-source implementations, addressing reproducibility challenges in large-scale RL training. These resources enable the community to build upon GRPO-related advances without starting from scratch.

---

## Future Directions

Based on this review, promising future directions include:

1. **Theoretical Analysis:** Further investigation into why simple baselines compete with complex algorithms like GRPO
2. **Hybrid Approaches:** Combining GRPO's strengths with off-policy learning and self-correction mechanisms
3. **Multi-Modal Extensions:** Extending GRPO principles to video, audio, and other continuous generation domains
4. **Efficiency Optimization:** Leveraging contrastive insights to minimize computational requirements
5. **Stability Guarantees:** Developing theoretical guarantees for soft-clipping and adaptive methods

---

## Conclusion

The literature from 2024-2026 reveals significant advances in understanding and improving GRPO for generation models. Key insights include the recognition of GRPO's implicit contrastive nature, the development of more stable and efficient variants, and successful extensions to diffusion models. While GRPO has proven effective, emerging work suggests that simpler approaches may achieve comparable results, warranting careful consideration of algorithmic complexity versus performance gains. The open-source initiatives accompanying these advances promise to accelerate future research and applications.

---

## References

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-Layer GRPO: Enhancing Reasoning and Self-Correction in Large Language Models. *arXiv preprint arXiv:2506.04746*. https://arxiv.org/abs/2506.04746v1

Gao, C., Zheng, C., Chen, X.-H., Dang, K., Liu, S., Yu, B., Yang, A., Bai, S., Zhou, J., & Lin, J. (2025). Soft Adaptive Policy Optimization. *arXiv preprint arXiv:2511.20347*. https://arxiv.org/abs/2511.20347v2

Hu, J., Zhang, Y., Han, Q., Jiang, D., Zhang, X., & Shum, H.-Y. (2025). Open-Reasoner-Zero: An Open Source Approach to Scaling Up Reinforcement Learning on the Base Model. *arXiv preprint arXiv:2503.24290*. https://arxiv.org/abs/2503.24290v2

Le Roux, N., Bellemare, M. G., Lebensold, J., Bergeron, A., Greaves, J., Fréchette, A., Pelletier, C., Thibodeau-Laufer, E., Toth, S., & Work, S. (2025). Tapered Off-Policy REINFORCE: Stable and Efficient Reinforcement Learning for LLMs. *arXiv preprint arXiv:2503.14286*. https://arxiv.org/abs/2503.14286v2

Wu, Y., Ma, L., Ding, L., Li, M., Wang, X., Chen, K., Su, Z., Zhang, Z., Huang, C., Zhang, Y., Coates, M., & Nie, J.-Y. (2025). It Takes Two: Your GRPO Is Secretly DPO. *arXiv preprint arXiv:2510.00977*. https://arxiv.org/abs/2510.00977v3

Xiong, W., Yao, J., Xu, Y., Pang, B., Wang, L., Sahoo, D., Li, J., Jiang, N., Zhang, T., Xiong, C., & Dong, H. (2025). A Minimalist Approach to LLM Reasoning: from Rejection Sampling to REINFORCE. *arXiv preprint arXiv:2504.11343*. https://arxiv.org/abs/2504.11343v2

Yan, J., Li, Y., Hu, Z., Wang, Z., Cui, G., Qu, X., Cheng, Y., & Zhang, Y. (2025). Learning to Reason under Off-Policy Guidance. *arXiv preprint arXiv:2504.14945*. https://arxiv.org/abs/2504.14945v5

Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai, W., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., & Zhu, H. (2025). DAPO: An Open-Source LLM Reinforcement Learning System at Scale. *arXiv preprint arXiv:2503.14476*. https://arxiv.org/abs/2503.14476v2

Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C., Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J., & Lin, J. (2025). Group Sequence Policy Optimization. *arXiv preprint arXiv:2507.18071*. https://arxiv.org/abs/2507.18071v2

Zheng, K., Chen, H., Ye, H., Wang, H., Zhang, Q., Jiang, K., Su, H., Ermon, S., Zhu, J., & Liu, M.-Y. (2025). DiffusionNFT: Online Diffusion Reinforcement with Forward Process. *arXiv preprint arXiv:2509.16117*. https://arxiv.org/abs/2509.16117v2
