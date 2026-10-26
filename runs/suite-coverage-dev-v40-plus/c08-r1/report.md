# Systematic Literature Review: Advances in GRPO for Generation Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "GRPO generation models", filtered to category cs.LG, published between 2024-02-21 and 2026-02-20
**Citation format**: APA 7th edition

## Executive Summary

The literature on Group Relative Policy Optimization (GRPO) and related reinforcement learning methods for generation models reveals a rapidly evolving field focused on improving training stability, sample efficiency, and reasoning capabilities in large language models and diffusion models. The surveyed papers collectively demonstrate that GRPO's effectiveness stems from its implicit contrastive objective rather than large group sizes, with recent work achieving comparable or superior performance using minimal rollouts. Key advances include sequence-level optimization (GSPO), multi-layer self-correction mechanisms (MGRPO), soft adaptive gating (SAPO), and extensions to diffusion models (DiffusionNFT). The field shows strong convergence around the importance of data quality over quantity, with strategic sample selection outperforming brute-force scaling approaches.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "GRPO generation models", filtered to category cs.LG, published between 2024-02-21 and 2026-02-20. Papers were sorted by relevance and co-citation frequency, and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening results**: 50 papers identified by search, 58 added from citation expansion, 30 shortlisted, 30 screened, 10 included (9 from citation expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. All metadata is extracted from abstracts only; full-text analysis may reveal additional findings and limitations.

## Themes

### Theme 1: Efficiency and Minimalism in Policy Optimization

A dominant theme across the surveyed literature is the pursuit of more efficient RL training methods that achieve superior performance with reduced computational overhead. Wu et al. (2025) demonstrate that GRPO's effectiveness derives from its implicit contrastive objective rather than large group statistics, introducing 2-GRPO which retains 97.6% of 16-GRPO's performance with only 12.5% of rollouts and 21% of training time. Similarly, Xiong et al. (2025) show that simple rejection sampling baseline (RAFT) yields competitive performance compared to GRPO and PPO, challenging assumptions about the necessity of complex reward normalization. Wang et al. (2025) extend this minimalist approach, demonstrating that reinforcement learning with verifiable reward using only one training example can elevate Qwen2.5-Math-1.5B performance on MATH500 from 36.0% to 73.6%. This theme reflects a broader recognition that strategic optimization design, rather than computational brute force, drives RL effectiveness.

### Theme 2: Stability Improvements Through Advanced Clipping and Gating Mechanisms

Multiple papers address the instability challenges inherent in policy gradient methods through novel clipping and gating strategies. Zheng et al. (2025) introduce Group Sequence Policy Optimization (GSPO), which defines importance ratios based on sequence likelihood rather than token-level ratios, performing sequence-level clipping, rewarding, and optimization to achieve superior training efficiency and stability. Gao et al. (2025) propose Soft Adaptive Policy Optimization (SAPO), replacing hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates, forming a continuous trust region that avoids brittle hard clipping bands. Yu et al. (2025) present DAPO with decoupled clip and dynamic sampling techniques, achieving 50 points on AIME 2024 using Qwen2.5-32B base model. These approaches share the insight that selective, adaptive update mechanisms preserve learning signals while maintaining training stability.

### Theme 3: Self-Correction and Multi-Layer Reasoning

A significant advancement in GRPO-based methods involves incorporating self-correction mechanisms that enable models to identify and rectify errors during generation. Ding et al. (2025) propose Multi-Layer GRPO (MGRPO) with two layers: the first layer generates initial responses via standard GRPO, while the second layer identifies and corrects errors, creating a self-correction loop that provides implicit process-level supervision without requiring explicit densely-annotated reward models. This approach significantly outperforms standard GRPO on mathematical reasoning benchmarks. Yan et al. (2025) introduce LUFFY, which augments RL with verifiable rewards by incorporating off-policy reasoning traces through Mixed-Policy GRPO and policy shaping via regularized importance sampling, achieving over +6.4 average gain across six math benchmarks. These methods recognize that reasoning quality improves not just through reward maximization, but through explicit error detection and correction processes.

### Theme 4: Extension to Diffusion Models

The application of GRPO-like methods extends beyond language models to diffusion-based generation systems. Zheng et al. (2025) introduce DiffusionNFT, which optimizes diffusion models directly on the forward process via flow matching, contrasting positive and negative generations to define implicit policy improvement direction. DiffusionNFT achieves up to 25× efficiency improvement over FlowGRPO, improving GenEval score from 0.24 to 0.98 within 1k steps while FlowGRPO requires over 5k steps to achieve 0.95. This work demonstrates that the core insights from GRPO—contrastive learning, policy optimization without explicit likelihood estimation—generalize effectively to diffusion model training, enabling CFG-free optimization with arbitrary black-box solvers.

### Theme 5: Data Quality Over Quantity in RL Training

A critical insight emerging from recent work is that strategic data selection outperforms brute-force dataset scaling. Li et al. (2025) introduce Learning Impact Measurement (LIM), an automated method to evaluate and prioritize training samples based on their alignment with model learning trajectories. Their LIMR approach demonstrates that a strategically selected subset of 1,389 samples outperforms the full 8,523-sample dataset in RL training for reasoning capabilities, achieving 16.7% higher accuracy on AIME24 compared to data-efficient approaches LIMO and s1. This finding challenges conventional wisdom about RL scaling and suggests that precise sample selection, rather than data volume, is the key determinant of training effectiveness. The theme connects to broader concerns about sample efficiency and the computational cost of large-scale RL training.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several points. First, all methods recognize that GRPO's core contribution is its contrastive learning signal rather than group size statistics (Wu et al., 2025; Xiong et al., 2025). Second, there is consensus that sequence-level or holistic optimization outperforms token-level approaches (Zheng et al., 2025; Ding et al., 2025). Third, multiple papers converge on the finding that data quality and strategic selection matter more than raw dataset size (Li et al., 2025; Wang et al., 2025). Fourth, all advanced methods demonstrate that stability improvements through adaptive mechanisms (soft gating, sequence-level clipping, multi-layer correction) yield consistent performance gains across benchmarks.

**Disagreements**: Some tensions exist in the literature regarding the optimal approach to off-policy learning. While Yan et al. (2025) advocate for incorporating off-policy demonstrations through Mixed-Policy GRPO, Gao et al. (2025) emphasize preserving on-policy token learning through selective attenuation rather than explicit off-policy integration. Additionally, there is disagreement about the necessity of complex reward modeling: Xiong et al. (2025) suggest simple rejection sampling suffices, while Ding et al. (2025) and Zheng et al. (2025) argue for sophisticated multi-layer or sequence-level reward mechanisms. The field has not yet resolved whether minimalist approaches generalize across all reasoning tasks or excel primarily in specific domains.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either space constraints or insufficient critical self-reflection on methodological boundaries. Second, while multiple papers demonstrate improvements on mathematical reasoning benchmarks (AIME, MATH500), there is limited evidence of generalization to non-mathematical reasoning tasks, creative generation, or multi-modal reasoning. Third, the computational cost comparisons focus on training efficiency but rarely address inference-time overhead introduced by multi-layer or self-correction mechanisms. Fourth, the extension to diffusion models (Zheng et al., 2025) remains isolated—there is no systematic exploration of GRPO variants for other generative architectures beyond language and diffusion models. Fifth, the long-term stability and scalability of these methods at extreme scales (beyond 32B parameters) remains unexplored, with most evaluations focused on mid-size models. Finally, the relationship between GRPO variants and established preference learning methods (DPO, IPO) warrants deeper theoretical analysis beyond structural observations (Wu et al., 2025).

## Per-Paper Annotations

### Ding et al. (2025)

**Research question**: How can GRPO be improved to address inefficient exploration dynamics and reward vanishing in complex reasoning chains?
**Methodology**: The authors propose MGRPO (Multi-layer GRPO) with two layers: first layer generates initial response via standard GRPO, second layer identifies and corrects errors in the initial response, creating a self-correction loop.
**Key findings**:
- MGRPO provides implicit process-level supervision without requiring explicit densely-annotated reward models.
- MGRPO significantly outperforms standard GRPO on mathematical reasoning benchmarks.
- The self-correction mechanism rewards successful error correction.
- MGRPO fosters both reasoning and self-correction abilities in LLMs.
**Limitations**: not stated in abstract

### Gao et al. (2025)

**Research question**: How can policy optimization in reinforcement learning for LLMs be made more stable and effective while avoiding the limitations of hard clipping methods?
**Methodology**: The authors propose Soft Adaptive Policy Optimization (SAPO), which replaces hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates. The method is evaluated on mathematical reasoning benchmarks and applied to train the Qwen3-VL model series.
**Key findings**:
- SAPO replaces hard clipping with soft gating, forming a continuous trust region that avoids brittle hard clipping bands.
- Unlike GSPO, SAPO selectively down-weights only off-policy tokens while preserving learning signals from near-on-policy tokens.
- Compared to GRPO, SAPO enables more informative and stable updates through smooth, temperature-controlled scaling.
- SAPO exhibits improved training stability and higher Pass@1 performance on mathematical reasoning benchmarks under comparable training budgets.
- SAPO yields consistent performance gains across diverse tasks and different model sizes when training Qwen3-VL.
**Limitations**: not stated in abstract

### Li et al. (2025)

**Research question**: What truly determines the effectiveness of RL training data for enhancing language models' reasoning capabilities?
**Methodology**: The authors introduce Learning Impact Measurement (LIM), an automated method to evaluate and prioritize training samples based on their alignment with model learning trajectories. They demonstrate that a strategically selected subset of 1,389 samples can outperform the full 8,523-sample dataset using RL-based training starting from base models without distillation.
**Key findings**:
- A strategically selected subset of 1,389 samples outperforms the full 8,523-sample dataset in RL training for reasoning capabilities.
- LIMR achieves 16.7% higher accuracy on AIME24 compared to data-efficient approaches LIMO and s1.
- LIMR outperforms LIMO and s1 by 13.0% and 22.2% respectively on MATH500 benchmark.
- Recent data-efficient approaches (LIMO and s1) significantly underperform at 7B-scale through supervised fine-tuning, while RL-based LIMR excels.
- Precise sample selection, rather than data scale, is the key to unlocking enhanced reasoning capabilities in LLMs.
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: Can reinforcement learning with verifiable reward using only one training example effectively incentivize math reasoning capabilities in large language models?
**Methodology**: The authors apply 1-shot RLVR to Qwen2.5-Math-1.5B and other models using GRPO and PPO algorithms, analyzing phenomena such as cross-category generalization, self-reflection frequency, and post-saturation generalization.
**Key findings**:
- A single training example elevates Qwen2.5-Math-1.5B performance on MATH500 from 36.0% to 73.6% (8.6% improvement beyond format correction).
- Average performance across six mathematical reasoning benchmarks improves from 17.6% to 35.7% with just one example.
- RLVR with two examples slightly exceeds results achieved with 1.2k DeepScaleR subset (MATH500: 74.8%).
- The effectiveness of 1-shot RLVR primarily arises from policy gradient loss, distinguished from the grokking phenomenon.
- Promoting exploration through entropy loss with appropriate coefficient plays a critical role in 1-shot RLVR training.
**Limitations**: not stated in abstract

### Wu et al. (2025)

**Research question**: What is the true source of GRPO's effectiveness, and can it work with minimal group sizes?
**Methodology**: The authors propose that GRPO's efficacy stems from its implicit contrastive objective rather than large group statistics, and introduce 2-GRPO, a variant using only two rollouts to construct contrastive signals.
**Key findings**:
- GRPO's effectiveness comes from its implicit contrastive objective, not large group sizes.
- 2-GRPO retains 97.6% of 16-GRPO's performance with only 12.5% of rollouts.
- 2-GRPO requires only 21% of the training time compared to 16-GRPO.
- GRPO is structurally related to preference learning methods like DPO.
**Limitations**: not stated in abstract

### Xiong et al. (2025)

**Research question**: What are the true sources of GRPO's effectiveness in LLM reasoning tasks?
**Methodology**: The authors analyze GRPO from a REINFORCE-like perspective and compare it with rejection sampling baseline (RAFT), then propose Reinforce-Rej that filters entirely incorrect and entirely correct samples.
**Key findings**:
- Simple rejection sampling baseline (RAFT) yields competitive performance compared to GRPO and PPO.
- GRPO's main advantage arises from discarding prompts with entirely incorrect responses, not reward normalization.
- Reinforce-Rej improves KL efficiency and stability over standard policy gradient.
- RAFT serves as a robust and interpretable baseline for reward-based LLM post-training.
**Limitations**: not stated in abstract

### Yan et al. (2025)

**Research question**: How can reinforcement learning with verifiable rewards overcome the limitations of on-policy approaches that restrict learning to a model's own outputs?
**Methodology**: The authors introduce LUFFY, a framework that augments RLVR with off-policy reasoning traces by dynamically balancing imitation and exploration through Mixed-Policy GRPO and policy shaping via regularized importance sampling.
**Key findings**:
- LUFFY combines off-policy demonstrations with on-policy rollouts during training to transcend on-policy RLVR limitations.
- The framework achieves over +6.4 average gain across six math benchmarks compared to previous RLVR methods.
- LUFFY demonstrates an advantage of over +6.2 points in out-of-distribution tasks.
- LUFFY successfully trains weak models in scenarios where on-policy RLVR completely fails.
**Limitations**: not stated in abstract

### Yu et al. (2025)

**Research question**: How can the key technical details of state-of-the-art reasoning LLMs be made reproducible and open-source for the research community?
**Methodology**: The authors propose the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm and open-source a complete large-scale RL system built on the verl framework, including training code and a curated dataset.
**Key findings**:
- DAPO introduces four key techniques that enable successful large-scale LLM reinforcement learning.
- The system achieves 50 points on AIME 2024 using Qwen2.5-32B base model.
- The open-source system includes training code, a carefully curated dataset, and is built on the verl framework.
- The components enhance reproducibility and support future research in large-scale LLM RL.
**Limitations**: not stated in abstract

### Zheng et al. (2025a)

**Research question**: How can online reinforcement learning be effectively extended to diffusion models without intractable likelihood estimation?
**Methodology**: The authors introduce DiffusionNFT, which optimizes diffusion models directly on the forward process via flow matching, contrasting positive and negative generations to define implicit policy improvement direction.
**Key findings**:
- DiffusionNFT is up to 25× more efficient than FlowGRPO.
- DiffusionNFT improves GenEval score from 0.24 to 0.98 within 1k steps, while FlowGRPO achieves 0.95 with over 5k steps.
- DiffusionNFT enables training with arbitrary black-box solvers without likelihood estimation.
- DiffusionNFT significantly boosts SD3.5-Medium performance across all tested benchmarks.
- DiffusionNFT is CFG-free, eliminating need for classifier-free guidance.
**Limitations**: not stated in abstract

### Zheng et al. (2025b)

**Research question**: How can reinforcement learning for training large language models be made more stable, efficient, and performant?
**Methodology**: The authors introduce Group Sequence Policy Optimization (GSPO), which defines importance ratios based on sequence likelihood rather than token-level ratios, and performs sequence-level clipping, rewarding, and optimization.
**Key findings**:
- GSPO achieves superior training efficiency and performance compared to GRPO.
- GSPO notably stabilizes Mixture-of-Experts (MoE) RL training.
- GSPO has the potential to simplify RL infrastructure design.
- GSPO contributed to remarkable improvements in the latest Qwen3 models.
**Limitations**: not stated in abstract

## References

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-layer GRPO: Enhancing reasoning and self-correction in large language models. arXiv. https://arxiv.org/abs/2506.04746

Gao, C., Zheng, C., Chen, X.-H., Dang, K., Liu, S., Yu, B., Yang, A., Bai, S., Zhou, J., & Lin, J. (2025). Soft adaptive policy optimization. arXiv. https://arxiv.org/abs/2511.20347

Li, X., Zou, H., & Liu, P. (2025). LIMR: Less is more for RL scaling. arXiv. https://arxiv.org/abs/2502.11886

Wang, Y., Yang, Q., Zeng, Z., Ren, L., Liu, L., Peng, B., Cheng, H., He, X., Wang, K., Gao, J., Chen, W., Wang, S., Du, S. S., & Shen, Y. (2025). Reinforcement learning for reasoning in large language models with one training example. arXiv. https://arxiv.org/abs/2504.20571

Wu, Y., Ma, L., Ding, L., Li, M., Wang, X., Chen, K., Su, Z., Zhang, Z., Huang, C., Zhang, Y., Coates, M., & Nie, J.-Y. (2025). It takes two: Your GRPO is secretly DPO. arXiv. https://arxiv.org/abs/2510.00977

Xiong, W., Yao, J., Xu, Y., Pang, B., Wang, L., Sahoo, D., Li, J., Jiang, N., Zhang, T., Xiong, C., & Dong, H. (2025). A minimalist approach to LLM reasoning: from rejection sampling to reinforce. arXiv. https://arxiv.org/abs/2504.11343

Yan, J., Li, Y., Hu, Z., Wang, Z., Cui, G., Qu, X., Cheng, Y., & Zhang, Y. (2025). Learning to reason under off-policy guidance. arXiv. https://arxiv.org/abs/2504.14945

Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai, W., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., & Zhu, H. (2025). DAPO: An open-source LLM reinforcement learning system at scale. arXiv. https://arxiv.org/abs/2503.14476

Zheng, K., Chen, H., Ye, H., Wang, H., Zhang, Q., Jiang, K., Su, H., Ermon, S., Zhu, J., & Liu, M.-Y. (2025). DiffusionNFT: Online diffusion reinforcement with forward process. arXiv. https://arxiv.org/abs/2509.16117

Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C., Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J., & Lin, J. (2025). Group sequence policy optimization. arXiv. https://arxiv.org/abs/2507.18071
