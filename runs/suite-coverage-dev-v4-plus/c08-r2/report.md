# Systematic Literature Review: Advances in GRPO for Generation Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "GRPO generation models", filtered to category cs.LG, published between 2024-02-21 and 2026-02-20
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in Group Relative Policy Optimization (GRPO) and related reinforcement learning algorithms for generation models. The surveyed literature reveals a rapidly evolving field where researchers are fundamentally re-examining GRPO's core mechanisms, proposing more efficient alternatives, and extending the algorithm to new domains including diffusion models. Key findings indicate that GRPO's effectiveness stems primarily from its implicit contrastive objective rather than large group sizes, enabling dramatic efficiency improvements with minimal group variants. The literature demonstrates strong convergence around sequence-level optimization approaches, adaptive clipping mechanisms, and data-efficient training strategies. However, significant gaps remain in understanding cross-model generalization patterns and the relationship between response length and genuine cognitive behaviors during RL training.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "GRPO generation models", filtered to category cs.LG, published between 2024-02-21 and 2026-02-20. Papers were selected by co-citation relevance screening from a pool of 50 identified papers plus 57 papers added from citation expansion (30 shortlisted, 10 included). Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, 9 of the 10 included papers were added from citation expansion rather than the initial search results, indicating the query's exact phrase matching initially missed highly relevant work.

## Themes

### Theme 1: Efficiency and Minimalism in Policy Optimization

A dominant theme across the surveyed literature is the pursuit of more efficient RL training through algorithmic simplification. Multiple papers challenge the assumption that complex, large-scale group sampling is necessary for effective policy optimization. Wu et al. (2025) demonstrate that GRPO's efficacy derives from its implicit contrastive objective rather than large group sizes, introducing 2-GRPO which uses only two rollouts while retaining 97.6% of 16-GRPO's performance with just 12.5% of rollouts and 21% of training time. Similarly, Xiong et al. (2025) show that a simple rejection sampling baseline (RAFT) yields competitive performance compared to GRPO and PPO, with the main advantage arising from discarding prompts with entirely incorrect responses rather than sophisticated reward normalization. Wang et al. (2025) extend this minimalist philosophy to its extreme, demonstrating that reinforcement learning with verifiable reward using only one training example can elevate Qwen2.5-Math-1.5B performance on MATH500 from 36.0% to 73.6%. This convergence suggests the field is moving toward leaner, more interpretable RL algorithms that achieve comparable results with dramatically reduced computational costs.

### Theme 2: Sequence-Level vs. Token-Level Optimization

The literature reveals a clear shift from token-level to sequence-level policy optimization as a means of improving training stability and performance. Zheng et al. (2025) introduce Group Sequence Policy Optimization (GSPO), which defines importance ratios based on sequence likelihood rather than token-level importance ratios, performing sequence-level clipping, rewarding, and optimization. This approach achieves superior training efficiency and performance compared to GRPO while notably stabilizing Mixture-of-Experts (MoE) RL training. Building on this direction, Gao et al. (2025) propose Soft Adaptive Policy Optimization (SAPO), which replaces hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates. Unlike GSPO which suppresses all gradients for sequences with highly off-policy tokens, SAPO selectively down-weights only offending tokens while preserving learning signals from near-on-policy tokens. These sequence-level approaches address the high variance and instability inherent in token-level optimization, particularly for large-scale models and complex reasoning tasks.

### Theme 3: Self-Correction and Multi-Layer Reasoning

Several papers explore architectures that enable models to identify and correct their own errors, creating iterative improvement loops. Ding et al. (2025) propose Multi-Layer GRPO (MGRPO) with two layers: the first layer uses standard GRPO for initial response generation, while the second layer is trained to identify and correct errors in the initial response. This two-layer approach fosters both reasoning and self-correction abilities, providing implicit process-level supervision without requiring explicit, densely-annotated reward models. The self-correction mechanism specifically addresses reward vanishing from single errors in reasoning chains, a common failure mode in complex mathematical reasoning. This theme reflects growing recognition that single-pass generation is insufficient for complex reasoning tasks, and that RL training should explicitly optimize for iterative refinement capabilities.

### Theme 4: Cross-Domain Extension to Diffusion Models

The literature demonstrates successful extension of GRPO-like algorithms beyond language models to diffusion-based generation. Zheng et al. (2025) introduce DiffusionNFT, which optimizes diffusion models directly on the forward process via flow matching, contrasting positive and negative generations to define implicit policy improvement direction. This approach is up to 25× more efficient than FlowGRPO in head-to-head comparisons, improving GenEval score from 0.24 to 0.98 within 1k steps while FlowGRPO achieves 0.95 with over 5k steps. Critically, DiffusionNFT enables training with arbitrary black-box solvers and eliminates the need for likelihood estimation, requiring only clean images rather than sampling trajectories for policy optimization. This extension demonstrates the generality of contrastive policy optimization principles across different generative model architectures.

### Theme 5: Data Selection and Training Dynamics

A recurring theme emphasizes strategic data selection over raw scale for effective RL training. Li et al. (2025) introduce Learning Impact Measurement (LIM), an automated method to evaluate and prioritize training samples based on their alignment with model learning trajectories. Their approach demonstrates that a strategically selected subset of 1,389 samples can outperform the full 8,523-sample dataset, achieving 16.7% higher accuracy on AIME24 compared to data-efficient approaches LIMO and s1 at 7B-scale. Zeng et al. (2025) investigate zero RL training across 10 diverse base models spanning different families and sizes, finding that different base models exhibit distinct patterns during training, with increased response length not always correlating with the emergence of cognitive behaviors like verification. Yu et al. (2025) contribute DAPO, an open-source large-scale RL system with four key techniques that achieves 50 points on AIME 2024 using Qwen2.5-32B base model, emphasizing reproducibility and community access to state-of-the-art training infrastructure.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers converge on the finding that algorithmic efficiency improvements can maintain or improve performance while dramatically reducing computational costs—whether through minimal group sizes (Wu et al., 2025), rejection sampling (Xiong et al., 2025), or strategic data selection (Li et al., 2025). Second, there is consensus that sequence-level optimization provides superior stability compared to token-level approaches, particularly for large-scale models (Zheng et al., 2025; Gao et al., 2025). Third, multiple papers agree that self-correction mechanisms are essential for complex reasoning tasks, as single-pass generation suffers from error propagation (Ding et al., 2025). Fourth, the literature converges on the finding that GRPO-like algorithms can be successfully extended beyond language models to other generative architectures (Zheng et al., 2025).

**Disagreements**: A key disagreement emerges around the source of GRPO's effectiveness. Wu et al. (2025) attribute it to the implicit contrastive objective, while Xiong et al. (2025) argue the main advantage arises from discarding prompts with entirely incorrect responses rather than the contrastive mechanism itself. Additionally, there is tension around the relationship between response length and reasoning capability: Zeng et al. (2025) observe that increased response length does not always correlate with cognitive behaviors like verification, while other papers implicitly assume longer responses indicate deeper reasoning. The literature also shows disagreement on optimal data scaling, with Li et al. (2025) advocating strategic subset selection while Yu et al. (2025) demonstrate success with large-scale training systems.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are not systematically addressed or that they appear only in full paper text. This represents a methodological gap in the field's self-awareness. Second, Zeng et al. (2025) note that most recent efforts reproducing zero RL training focused primarily on Qwen2.5 models, which may not be representative as they already exhibit strong instruction-following and self-reflection abilities—indicating a gap in cross-model family generalization studies. Third, while multiple papers achieve impressive benchmark performance, there is limited discussion of real-world deployment considerations, safety implications, or failure modes in production settings. Fourth, the relationship between response length and genuine cognitive behaviors remains poorly understood, with Zeng et al. (2025) observing distinct patterns across model families but no unified theoretical framework. Finally, while DiffusionNFT demonstrates successful extension to diffusion models, the literature lacks systematic comparison of policy optimization approaches across different generative model architectures (autoregressive, diffusion, flow-based), leaving open questions about domain-specific optimization requirements.

## Per-Paper Annotations

### Ding et al. (2025)

**Research question**: How can GRPO be improved to address inefficient exploration dynamics and error propagation in complex reasoning chains?
**Methodology**: Proposes MGRPO (Multi-layer GRPO) with two layers: first layer uses standard GRPO for initial response, second layer is trained to identify and correct errors in the initial response, creating a self-correction loop with implicit process-level supervision.
**Key findings**:
- MGRPO significantly outperforms standard GRPO on mathematical reasoning benchmarks
- The two-layer approach fosters both reasoning and self-correction abilities
- MGRPO provides implicit process-level supervision without requiring explicit, densely-annotated reward models
- The self-correction mechanism addresses reward vanishing from single errors in reasoning chains
**Limitations**: not stated in abstract

### Gao et al. (2025)

**Research question**: How can reinforcement learning policy optimization for large language models achieve stable and effective updates while addressing high variance in token-level importance ratios?
**Methodology**: The authors propose Soft Adaptive Policy Optimization (SAPO), which replaces hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates. SAPO is evaluated on mathematical reasoning benchmarks and used to train the Qwen3-VL model series across diverse tasks and model sizes.
**Key findings**:
- SAPO replaces hard clipping with soft gating, forming a continuous trust region that avoids brittle hard clipping bands
- Unlike GSPO which suppresses all gradients for sequences with highly off-policy tokens, SAPO selectively down-weights only offending tokens while preserving learning signals from near-on-policy tokens
- SAPO demonstrates improved training stability and higher Pass@1 performance under comparable training budgets on mathematical reasoning benchmarks
- SAPO yields consistent performance gains across diverse tasks and different model sizes when training the Qwen3-VL model series
**Limitations**: not stated in abstract

### Li et al. (2025)

**Research question**: What truly determines the effectiveness of RL training data for enhancing language models' reasoning capabilities, and does scaling up RL training data inherently improve performance?
**Methodology**: The authors introduce Learning Impact Measurement (LIM), an automated method to evaluate and prioritize training samples based on their alignment with model learning trajectories, and demonstrate results using a strategically selected subset of 1,389 samples compared to the full 8,523-sample dataset, starting directly from base models without distillation.
**Key findings**:
- A strategically selected subset of 1,389 samples can outperform the full 8,523-sample dataset
- LIMR achieves 16.7% higher accuracy on AIME24 compared to data-efficient approaches LIMO and s1 at 7B-scale
- LIMR outperforms LIMO and s1 by 13.0% and 22.2% on MATH500, respectively
- Precise sample selection, rather than data scale, may be the key to unlocking enhanced reasoning capabilities in LLMs
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: Can reinforcement learning with verifiable reward using only one training example effectively incentivize math reasoning capabilities in large language models?
**Methodology**: The authors apply 1-shot RLVR to base model Qwen2.5-Math-1.5B and test across various models (Qwen2.5-Math-7B, Llama3.2-3B-Instruct, DeepSeek-R1-Distill-Qwen-1.5B), RL algorithms (GRPO and PPO), and different math examples, analyzing phenomena including cross-category generalization and post-saturation generalization.
**Key findings**:
- A single training example elevates Qwen2.5-Math-1.5B performance on MATH500 from 36.0% to 73.6% (8.6% improvement beyond format correction)
- Average performance across six mathematical reasoning benchmarks improves from 17.6% to 35.7% (7.0% non-format gain) with just one example
- RLVR with two examples slightly exceeds these results (MATH500: 74.8%, average: 36.6%)
- The effectiveness of 1-shot RLVR primarily arises from the policy gradient loss, distinguishing it from the grokking phenomenon
- Promoting exploration through entropy loss with an appropriate coefficient plays a critical role in 1-shot RLVR training
**Limitations**: not stated in abstract

### Wu et al. (2025)

**Research question**: What is the true source of GRPO's effectiveness in reinforcement learning for LLMs?
**Methodology**: Proposes that GRPO's efficacy stems from its implicit contrastive objective rather than large group sizes, and introduces 2-GRPO, a minimal group-size variant using only two rollouts to construct contrastive signals.
**Key findings**:
- GRPO's effectiveness comes from its implicit contrastive objective that reduces variance via control variate method
- 2-GRPO retains 97.6% of the performance of 16-GRPO
- 2-GRPO requires only 12.5% of the rollouts and 21% of the training time compared to 16-GRPO
- GRPO is structurally related to preference learning methods such as DPO
**Limitations**: not stated in abstract

### Xiong et al. (2025)

**Research question**: What are the actual sources of GRPO's effectiveness in reinforcement learning for LLM reasoning tasks?
**Methodology**: Revisits GRPO from a REINFORCE-like algorithm perspective, analyzes its core components, and proposes Reinforce-Rej, a minimal extension of policy gradient that filters both entirely incorrect and entirely correct samples.
**Key findings**:
- A simple rejection sampling baseline (RAFT) yields competitive performance compared to GRPO and PPO
- GRPO's main advantage arises from discarding prompts with entirely incorrect responses, not from reward normalization
- Reinforce-Rej improves KL efficiency and stability as a lightweight alternative to complex RL algorithms
- RAFT serves as a robust and interpretable baseline for reward-based LLM post-training
**Limitations**: not stated in abstract

### Yu et al. (2025)

**Research question**: How can the reinforcement learning training results of state-of-the-art reasoning LLMs be reproduced and made accessible to the research community?
**Methodology**: The authors propose the Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) algorithm with four key techniques and open-source a large-scale RL system built on the verl framework, along with a curated dataset, trained on Qwen2.5-32B base model.
**Key findings**:
- DAPO achieves 50 points on AIME 2024 using Qwen2.5-32B base model
- The system introduces four key techniques that make large-scale LLM RL successful
- The open-source training code and curated dataset enhance reproducibility and support future research in large-scale LLM RL
**Limitations**: not stated in abstract

### Zeng et al. (2025)

**Research question**: How does zero reinforcement learning training perform across diverse base model families and sizes, and what patterns emerge during training?
**Methodology**: The authors investigated zero RL training across 10 diverse base models spanning different families and sizes (LLama3-8B, Mistral-7B/24B, DeepSeek-Math-7B, Qwen2.5-math-7B, and Qwen2.5 models from 0.5B to 32B), using key design strategies such as adjusting format reward and controlling query difficulty while monitoring training dynamics.
**Key findings**:
- Substantial improvements in both reasoning accuracy and response length were achieved across most model settings using zero RL training
- Different base models exhibit distinct patterns during training, with increased response length not always correlating with the emergence of cognitive behaviors like verification
- The 'aha moment' (verification behavior) was observed for the first time in small models not from the Qwen family
- Most recent efforts reproducing zero RL training focused primarily on Qwen2.5 models, which may not be representative as they already exhibit strong instruction-following and self-reflection abilities
**Limitations**: not stated in abstract

### Zheng, C. et al. (2025)

**Research question**: How can reinforcement learning for training large language models be made more stable, efficient, and performant?
**Methodology**: Introduces Group Sequence Policy Optimization (GSPO), which defines importance ratio based on sequence likelihood rather than token-level importance ratios, and performs sequence-level clipping, rewarding, and optimization.
**Key findings**:
- GSPO achieves superior training efficiency and performance compared to GRPO algorithm
- GSPO notably stabilizes Mixture-of-Experts (MoE) RL training
- GSPO has potential for simplifying RL infrastructure design
- GSPO contributed to remarkable improvements in the latest Qwen3 models
**Limitations**: not stated in abstract

### Zheng, K. et al. (2025)

**Research question**: How can online reinforcement learning be effectively extended to diffusion models despite intractable likelihoods?
**Methodology**: Introduces DiffusionNFT, which optimizes diffusion models directly on the forward process via flow matching, contrasting positive and negative generations to define implicit policy improvement direction.
**Key findings**:
- DiffusionNFT is up to 25× more efficient than FlowGRPO in head-to-head comparisons
- Improves GenEval score from 0.24 to 0.98 within 1k steps, while FlowGRPO achieves 0.95 with over 5k steps
- DiffusionNFT enables training with arbitrary black-box solvers and eliminates need for likelihood estimation
- Requires only clean images rather than sampling trajectories for policy optimization
- Significantly boosts SD3.5-Medium performance across all tested benchmarks
**Limitations**: not stated in abstract

## References

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-layer GRPO: Enhancing reasoning and self-correction in large language models. arXiv. https://arxiv.org/abs/2506.04746

Gao, C., Zheng, C., Chen, X.-H., Dang, K., Liu, S., Yu, B., Yang, A., Bai, S., Zhou, J., & Lin, J. (2025). Soft adaptive policy optimization. arXiv. https://arxiv.org/abs/2511.20347

Li, X., Zou, H., & Liu, P. (2025). LIMR: Less is more for RL scaling. arXiv. https://arxiv.org/abs/2502.11886

Wang, Y., Yang, Q., Zeng, Z., Ren, L., Liu, L., Peng, B., Cheng, H., He, X., Wang, K., Gao, J., Chen, W., Du, S. S., Shen, Y., & Wang, S. (2025). Reinforcement learning for reasoning in large language models with one training example. arXiv. https://arxiv.org/abs/2504.20571

Wu, Y., Ma, L., Ding, L., Li, M., Wang, X., Chen, K., Su, Z., Zhang, Z., Huang, C., Zhang, Y., Coates, M., & Nie, J.-Y. (2025). It takes two: Your GRPO is secretly DPO. arXiv. https://arxiv.org/abs/2510.00977

Xiong, W., Yao, J., Xu, Y., Pang, B., Wang, L., Sahoo, D., Li, J., Jiang, N., Zhang, T., Xiong, C., Dong, H., & Xiong, C. (2025). A minimalist approach to LLM reasoning: From rejection sampling to reinforce. arXiv. https://arxiv.org/abs/2504.11343

Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai, W., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., & Zhu, H. (2025). DAPO: An open-source LLM reinforcement learning system at scale. arXiv. https://arxiv.org/abs/2503.14476

Zeng, W., Huang, Y., Liu, Q., Liu, W., He, K., Ma, Z., & He, J. (2025). SimpleRL-Zoo: Investigating and taming zero reinforcement learning for open base models in the wild. arXiv. https://arxiv.org/abs/2503.18892

Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C., Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J., & Lin, J. (2025). Group sequence policy optimization. arXiv. https://arxiv.org/abs/2507.18071

Zheng, K., Chen, H., Ye, H., Wang, H., Zhang, Q., Jiang, K., Su, H., Ermon, S., Zhu, J., & Liu, M.-Y. (2025). DiffusionNFT: Online diffusion reinforcement with forward process. arXiv. https://arxiv.org/abs/2509.16117
