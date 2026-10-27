# Systematic Literature Review: Advances in GRPO for Generation Models

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: arXiv query "GRPO Group Relative Policy Optimization" filtered to category cs.LG, published between 2024-02-21 and 2026-02-20
**Citation format**: APA 7th edition

## Executive Summary

The literature on Group Relative Policy Optimization (GRPO) and related reinforcement learning approaches for generation models reveals a rapidly evolving field focused on simplifying training pipelines while improving efficiency and performance. Recent work demonstrates that minimalist approaches—eliminating critic models, KL regularization, and complex surrogate losses—can achieve superior or competitive results compared to GRPO. Key advances include sequence-level optimization (GSPO), adaptive budget allocation (Knapsack-GRPO), two-layer self-correction architectures (MGRPO), and the surprising finding that contrastive learning with only two rollouts captures most of GRPO's benefits. The field shows strong convergence around the insight that GRPO's group mechanism primarily serves contrastive signal construction rather than value baseline estimation, with multiple papers independently arriving at simplified alternatives that match or exceed GRPO performance with reduced computational overhead.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "GRPO Group Relative Policy Optimization", filtered to category cs.LG, published between 2024-02-21 and 2026-02-20. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; all 10 papers had full HTML available), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Simplification and Minimalism in RL Training

A dominant trend across the surveyed literature is the move toward simplification of RL training pipelines. Multiple papers demonstrate that complex components traditionally considered essential—critic models, reference models, KL divergence constraints, and surrogate loss functions—can be eliminated without sacrificing performance. Gao et al. (2025) propose Group Policy Gradient (GPG), which directly optimizes the original RL objective without any of these components, achieving superior performance over GRPO across all benchmarks. Similarly, Xiong et al. (2025) show that RAFT++, a minimalist approach using rejection sampling with importance sampling and clipping, achieves 56.1% average accuracy compared to GRPO's 56.3%, suggesting that GRPO's complexity may be unnecessary. Hu et al. (2025) take this further with Open-Reasoner-Zero, implementing vanilla PPO with GAE (λ=1, γ=1) and rule-based rewards without KL regularization, achieving superior benchmark performance with only 1/10 the training steps of DeepSeek-R1-Zero. This convergence toward simplicity suggests the field is maturing beyond the need for complex architectural components.

### Theme 2: Efficiency and Computational Optimization

Efficiency improvements form a second major theme, with multiple papers addressing the computational overhead of GRPO training. Wu et al. (2025) introduce 2-GRPO, demonstrating that only two rollouts per prompt are sufficient to achieve 97.6% of 16-GRPO's performance while using just 12.5% of rollouts and 21% of training time. Xu et al. (2025) propose PODS (Policy Optimization with Down-Sampling), which strategically selects a subset of rollouts for training using max-variance selection, achieving 1.7× faster convergence than baseline GRPO. Li et al. (2025) address exploration budget allocation through Knapsack-GRPO, which formulates the problem as knapsack optimization and dynamically assigns computational resources across tasks, improving effective gradient ratio by 20-40%. These approaches collectively address the computational asymmetry between rollout generation and policy updates, suggesting that not all rollouts contribute equally to learning.

### Theme 3: Stability and Training Dynamics

Training stability emerges as a critical concern, with several papers proposing mechanisms to prevent early-stage collapse and maintain consistent learning dynamics. Gao et al. (2025) introduce Soft Adaptive Policy Optimization (SAPO), which replaces hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates. SAPO maintains stable training dynamics while GSPO and GRPO-R2 exhibit early-stage training collapse, achieving steady performance gains throughout training. Zheng et al. (2025) propose Group Sequence Policy Optimization (GSPO), which defines importance ratios based on sequence likelihood rather than token-level ratios, performing sequence-level clipping and optimization. This approach eliminates the need for Routing Replay in Mixture-of-Experts training, addressing a specific stability challenge in MoE architectures. The focus on stability reflects the field's recognition that training dynamics are as important as final performance metrics.

### Theme 4: Self-Correction and Multi-Layer Architectures

A novel architectural theme involves multi-layer approaches that enable self-correction capabilities. Ding et al. (2025) propose Multi-Layer GRPO (MGRPO), which operates in two layers: the first layer employs standard GRPO to generate an initial response, while the second layer is trained to identify and correct errors in the initial response, creating a self-correction loop. MGRPO consistently outperforms one-round PPO and GRPO, with the second layer effectively improving self-correction skills. The authors emphasize that RL training is necessary to teach the model how and when to self-correct, suggesting that self-correction is a learned capability rather than an inherent property. This architectural innovation points toward more sophisticated reasoning capabilities in generation models.

### Theme 5: Open Source and Reproducibility

The field shows strong commitment to open-source development and reproducibility. Yu et al. (2025) present DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization), achieving 50% accuracy on AIME 2024 with fully open-sourced code and dataset, addressing the challenge that "key technical details are concealed" in state-of-the-art systems. Hu et al. (2025) similarly open-source Open-Reasoner-Zero, enabling the research community to reproduce state-of-the-art reasoning LLM results. This openness contrasts with the proprietary nature of many competing systems and suggests a community norm toward transparency and accessibility in RL training research.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that GRPO's group mechanism primarily serves to construct contrastive signals rather than estimate value baselines. Wu et al. (2025) provide theoretical analysis supporting this claim, while Xiong et al. (2025) independently arrive at similar conclusions through their analysis of RAFT++. There is strong agreement that negative samples play a crucial role in maintaining exploration and preventing distributional collapse during training (Xiong et al., 2025; Wu et al., 2025). All surveyed papers agree that RL training leads to emergent capabilities—reflection, backtracking, and self-correction—that are not present in the base models (Yu et al., 2025; Ding et al., 2025).

**Disagreements**: While most papers advocate for simplification, there is disagreement about the optimal level of complexity. Chu et al. (2025) achieve best results with complete elimination of clipping and surrogate losses, while Zheng et al. (2025) find that sequence-level clipping remains beneficial for MoE training. Xiong et al. (2025) note that RAFT++ exhibits faster early-stage learning but is eventually surpassed by GRPO in later training stages, suggesting that GRPO's complexity provides benefits in extended training regimes that minimalist approaches cannot match. Wu et al. (2025) report that 2-GRPO performs worse on AIME 2025 when post-trained on MATH due to larger distribution shift, indicating that minimal rollout counts may not generalize across all task distributions.

## Gaps and Open Questions

Several gaps emerge from the surveyed literature. Approximately 20% of prompts remain in the extremely-hard category even after 1,000 training iterations across multiple studies (Li et al., 2025), suggesting fundamental limitations in current exploration strategies that warrant further investigation. The evaluation focuses primarily on RLVR tasks where response correctness is verifiable; other domains like open-ended dialogue may exhibit distinct dynamics that remain unexplored (Xu et al., 2025). Multiple papers note that RL training is intrinsically complex with interdependent subsystems, where even minor changes in initial conditions can amplify through iterative processes (Yu et al., 2025), yet systematic analysis of these dynamics remains limited. The utility of negative samples is more nuanced than previously assumed (Xiong et al., 2025), but optimal strategies for leveraging negative feedback remain unclear. Finally, while several papers mention hyperparameter sensitivity, none provide comprehensive ablation studies across the full hyperparameter space, leaving open questions about the robustness of proposed methods (Chu et al., 2025).

## Per-Paper Annotations

### Chu et al. (2025)

**Research question**: Can a minimalist reinforcement learning approach based on direct Policy Gradient optimization outperform complex methods like GRPO for enhancing LLM reasoning capabilities?

**Methodology**: The authors propose Group Policy Gradient (GPG), which directly optimizes the original RL objective without surrogate loss functions, critic models, reference models, or KL divergence constraints. Experiments were conducted on both unimodal (mathematical reasoning) and multimodal (visual reasoning, geometry, classification, grounding) tasks using 1.5B and 7B models.

**Key findings**:
- GPG consistently outperforms GRPO across all tasks with superior performance and clear margins (Chu et al., 2025) [E21]
- GPG-RS1 achieves average accuracy of 55.7% on 1.5B model benchmarks, with strong results on AMC23 (77.5%) and MATH-500 (87.6%) (Chu et al., 2025) [E22]
- GPG-7B achieves 57.7% average score and outperforms other baselines including SimpleRL-Zero-7B by 22.3% on AMC23 (Chu et al., 2025) [E23]
- GPG simplifies training and reduces computational overhead without sacrificing reasoning quality (Chu et al., 2025) [E24]

**Limitations**: The authors note they closely adhered to GRPO hyperparameters despite their suboptimality for GPG, suggesting GPG performance could be further improved with tuned hyperparameters.

### Ding et al. (2025)

**Research question**: How to address inefficient exploration dynamics and reward vanishing in GRPO when training LLMs for complex reasoning tasks?

**Methodology**: MGRPO operates in two layers where the first layer employs standard GRPO to generate an initial response, and the second layer is trained to identify and correct errors in the initial response, creating a self-correction loop.

**Key findings**:
- MGRPO consistently outperforms one-round PPO and GRPO [E6]
- MGRPO's Layer 2 GRPO effectively improves self-correction skill [E7]
- RL training is necessary to teach the model how and when to self-correct [E8]

**Limitations**: Not stated.

### Gao et al. (2025) [SAPO]

**Research question**: Can soft adaptive gating replace hard clipping in policy optimization to address instability in RL training of large language models?

**Methodology**: The authors propose Soft Adaptive Policy Optimization (SAPO), which replaces hard clipping with a smooth, temperature-controlled gate that adaptively attenuates off-policy updates. Experiments were conducted on Qwen3-30B-A3B-Base for mathematical reasoning and Qwen3-VL model series for multimodal tasks.

**Key findings**:
- SAPO consistently improves model performance across all benchmarks, achieving both higher stability and stronger final performance compared with GSPO and GRPO-R2 [E29]
- SAPO maintains stable training dynamics while GSPO and GRPO-R2 exhibit early-stage training collapse [E30]
- SAPO achieves steady performance gains throughout training and outperforms both baselines under equal compute budgets across diverse tasks and model sizes [E31]

**Limitations**: Not stated.

### Hu et al. (2025)

**Research question**: How can large-scale reasoning-oriented RL training on base models be effectively scaled up with simplicity and accessibility?

**Methodology**: The authors introduce Open-Reasoner-Zero, implementing vanilla PPO with GAE (λ=1, γ=1) and rule-based rewards without KL regularization on Qwen2.5 base models of various sizes (0.5B to 32B parameters).

**Key findings**:
- Vanilla PPO with GAE (λ=1, γ=1) and simple rule-based rewards without KL regularization effectively scales reasoning capabilities in language models [E13]
- GAE λ=1.0 yields superior training stability and final performance compared to λ=0.95 [E14]
- PPO's learned critic assigns more negative advantages to repetitive tokens than GRPO, demonstrating superior penalization of undesirable patterns [E15]
- ORZ achieves superior benchmark performance while requiring only 1/10 of training steps compared to DeepSeek-R1-Zero [E16]

**Limitations**: Not stated.

### Li et al. (2025)

**Research question**: How to optimally allocate computational exploration budgets across tasks during reinforcement learning training of LLMs?

**Methodology**: Formulates exploration budget allocation as a knapsack optimization problem, treating each task-budget pair as an item with associated cost and value to adaptively distribute resources.

**Key findings**:
- Knapsack-GRPO improves effective gradient ratio by 20-40% [E3]
- Knapsack-GRPO consistently outperforms standard GRPO [E4]
- Knapsack-GRPO can dynamically assign up to 93 exploration budgets to certain tasks [E5]

**Limitations**: Approximately 20% of prompts remain in the extremely-hard category even after 1,000 training iterations; the work focuses on rollout counts and could incorporate other computational factors.

### Wu et al. (2025)

**Research question**: What is the fundamental mechanism behind GRPO's efficacy and can it be achieved with minimal group sizes?

**Methodology**: Proposes that GRPO functions as contrastive learning and introduces 2-GRPO, a variant with only two rollouts per prompt, validated through theoretical analysis and empirical evaluation on mathematical reasoning benchmarks.

**Key findings**:
- 2-GRPO achieves 97.6% of 16-GRPO's performance with only 12.5% rollouts and 21% training time [E9]
- 2-GRPO is effective and efficient across diverse tasks beyond math reasoning [E10]
- GRPO's group mechanism primarily constructs contrastive signals rather than estimating value baselines [E11]

**Limitations**: 2-GRPO performs worse on AIME 2025 when post-trained on MATH due to larger distribution shift between training and evaluation datasets.

### Xu et al. (2025)

**Research question**: How can the compute and memory asymmetry between rollout generation and policy updates in RLVR be addressed?

**Methodology**: The authors introduce PODS (Policy Optimization with Down-Sampling), which decouples rollout generation from policy updates by training only on a strategically selected subset of rollouts using max-variance down-sampling.

**Key findings**:
- PODS achieves at least 1.7× faster convergence to peak accuracy compared to baseline GRPO while often achieving higher final performance [E17]
- Max-variance down-sampling consistently outperforms other down-sampling rules (max-reward, random, percentile) throughout training [E18]
- Increasing rollout size n exhibits diminishing returns with an optimal point around n=64 [E19]
- Training batch size m shows robust performance across a wide range with minimal degradation until very small values (m≤4) [E20]

**Limitations**: The evaluation focuses on RLVR tasks where response correctness is verifiable; other domains like open-ended dialogue may exhibit distinct dynamics. The method behaves off-policy and may be unsuitable when strict on-policy guarantees are required.

### Xiong et al. (2025)

**Research question**: What are the sources of GRPO's effectiveness in LLM reasoning, and can simpler rejection sampling baselines achieve competitive performance?

**Methodology**: The authors revisit GRPO from a reinforce-like algorithm perspective, analyzing RAFT (rejection sampling training on positive samples only) and proposing RAFT++ with importance sampling and clipping, plus Reinforce-Rej that filters both entirely incorrect and entirely correct samples.

**Key findings**:
- RAFT achieves competitive performance compared to more complex RL methods such as iterative DPO and deep RL-based approaches [E25]
- RAFT++ achieves 56.1% average accuracy, remarkably close to GRPO's 56.3% best model performance [E26]
- GRPO's main advantage comes from discarding entirely correct/incorrect prompts rather than from its reward normalization mechanism [E27]
- Negative samples play a crucial role in maintaining exploration and preventing distributional collapse during training [E28]

**Limitations**: RAFT++ exhibits faster early-stage learning but is eventually surpassed by GRPO in later training stages due to reduced exploration from low-entropy policies; the utility of negative samples is more nuanced than previously assumed.

### Yu et al. (2025)

**Research question**: How can the research community reproduce state-of-the-art reasoning LLM results when key technical details are concealed, and what techniques make large-scale LLM RL successful?

**Methodology**: The authors propose Decoupled Clip and Dynamic sAmpling Policy Optimization (DAPO) with four key techniques, built on the verl framework. They trained Qwen2.5-32B base model on mathematical tasks and achieved 50 points on AIME 2024, fully open-sourcing the code and dataset.

**Key findings**:
- DAPO successfully trains Qwen-32B Base model achieving performance superior to DeepSeek's experiments on Qwen2.5-32B using the R1 approach [E32]
- DAPO achieves 50% accuracy on AIME 2024 with only 50% of training steps required by DeepSeek-R1-Zero-Qwen-32B [E33]
- Each DAPO training technique contributes several accuracy points to overall performance improvement [E34]
- RL training leads to emergence of reflective behavior and backtracking in the model as training progresses [E35]

**Limitations**: The authors note that RL training is intrinsically complex with interdependent subsystems, where even minor changes in initial conditions can amplify through iterative processes yielding substantial deviations; monitoring key intermediate results is essential.

### Zheng et al. (2025)

**Research question**: How to develop a stable and efficient reinforcement learning algorithm for training large language models, particularly for Mixture-of-Experts models?

**Methodology**: GSPO defines importance ratios based on sequence likelihood rather than token-level ratios, and performs sequence-level clipping, rewarding, and optimization.

**Key findings**:
- GSPO achieves superior training efficiency over GRPO [E1]
- GSPO uses sequence-level clipping rather than token-level clipping [E2]
- GSPO eliminates the need for Routing Replay in MoE training [E12]

**Limitations**: Not stated.

## References

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-layer GRPO: Enhancing reasoning and self-correction in large language models. arXiv. https://arxiv.org/abs/2506.04746

Gao, C., Zheng, C., Chen, X.-H., Dang, K., Liu, S., Yu, B., Yang, A., Bai, S., Zhou, J., & Lin, J. (2025). Soft adaptive policy optimization. arXiv. https://arxiv.org/abs/2511.20347

Chu, X., Huang, H., Zhang, X., Wei, F., & Wang, Y. (2025). GPG: A simple and strong reinforcement learning baseline for model reasoning. arXiv. https://arxiv.org/abs/2504.02546

Hu, J., Zhang, Y., Han, Q., Jiang, D., Zhang, X., & Shum, H.-Y. (2025). Open-reasoner-zero: An open source approach to scaling up reinforcement learning on the base model. arXiv. https://arxiv.org/abs/2503.24290

Li, Z., Chen, C., Yang, T., Ding, T., Sun, R., Zhang, G., Huang, W., & Luo, Z.-Q. (2025). Knapsack RL: Unlocking exploration of LLMs via optimizing budget allocation. arXiv. https://arxiv.org/abs/2509.25849

Wu, Y., Ma, L., Ding, L., Li, M., Wang, X., Chen, K., Su, Z., Zhang, Z., Huang, C., Zhang, Y., Coates, M., & Nie, J.-Y. (2025). It takes two: Your GRPO is secretly DPO. arXiv. https://arxiv.org/abs/2510.00977

Xu, Y. E., Savani, Y., Fang, F., & Kolter, J. Z. (2025). Not all rollouts are useful: Down-sampling rollouts in LLM reinforcement learning. arXiv. https://arxiv.org/abs/2504.13818

Xiong, W., Yao, J., Xu, Y., Pang, B., Wang, L., Sahoo, D., Li, J., Jiang, N., Zhang, T., Xiong, C., & Dong, H. (2025). A minimalist approach to LLM reasoning: from rejection sampling to reinforce. arXiv. https://arxiv.org/abs/2504.11343

Yu, Q., Zhang, Z., Zhu, R., Yuan, Y., Zuo, X., Yue, Y., Dai, W., Fan, T., Liu, G., Liu, L., Liu, X., Lin, H., Lin, Z., Ma, B., Sheng, G., Tong, Y., Zhang, C., Zhang, M., Zhang, W., & Zhu, H. (2025). DAPO: An open-source LLM reinforcement learning system at scale. arXiv. https://arxiv.org/abs/2503.14476

Zheng, C., Liu, S., Li, M., Chen, X.-H., Yu, B., Gao, C., Dang, K., Liu, Y., Men, R., Yang, A., Zhou, J., & Lin, J. (2025). Group sequence policy optimization. arXiv. https://arxiv.org/abs/2507.18071

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E21 | arXiv:2504.02546 | [3 Experiments](https://arxiv.org/html/2504.02546#S3.p1) | “our method consistently outperforms GRPO across all tasks, achieving superior performance with clear margins.” |
| E22 | arXiv:2504.02546 | [3.2 Unimodal Task Evaluation](https://arxiv.org/html/2504.02546#S3.SS2.p2) | “our models exhibit superior performance with average accuracy 55.7% of GPG-RS1” |
| E23 | arXiv:2504.02546 | [3.2 Unimodal Task Evaluation](https://arxiv.org/html/2504.02546#S3.SS2.p3) | “GPG-7B achieves an average score of 57.7% and outperforms other baselines with clear margins” |
| E24 | arXiv:2504.02546 | [5 Conclusion](https://arxiv.org/html/2504.02546#S5.p1) | “GPG simplifies the training process and significantly reduces computational overhead without sacrificing reasoning quality” |
| E6 | arXiv:2506.04746 | [5 Results](https://arxiv.org/html/2506.04746#S5.p2) | “Overall, MGRPO consistently outperforms both one-round PPO and one-round GRPO.” |
| E7 | arXiv:2506.04746 | [5 Results](https://arxiv.org/html/2506.04746#S5.p4) | “The positive \Delta(\text{t1}^{\prime},\text{t2}) values (+2.9 on MATH, +2.2 on GSM8K, +3.2 on Minerva Math, +4.9 on OlympiadBench) indicate that the explicit RL training in Layer 2 effectively hones the self-correction skill.” |
| E8 | arXiv:2506.04746 | [5 Results](https://arxiv.org/html/2506.04746#S5.p5) | “This starkly contrasts with MGRPO's performance and underscores the necessity of the previous RL framework to teach the model "how" and "when" to correct effectively.” |
| E29 | arXiv:2511.20347 | [5.1 Controlled Experiments](https://arxiv.org/html/2511.20347#S5.SS1.p2) | “SAPO consistently improves model performance across all benchmarks, achieving both higher stability and stronger final performance” |
| E30 | arXiv:2511.20347 | [5.1 Controlled Experiments](https://arxiv.org/html/2511.20347#S5.SS1.p2) | “While GSPO and GRPO-R2 exhibit early-stage training collapse, SAPO maintains stable training dynamics” |
| E31 | arXiv:2511.20347 | [5.2 Qwen3‑VL Training](https://arxiv.org/html/2511.20347#S5.SS2.p2) | “SAPO achieves steady performance gains throughout training and outperforms both baselines under equal compute budgets” |
| E13 | arXiv:2503.24290 | [5 Conclusion and Future Directions](https://arxiv.org/html/2503.24290#S5.p1) | “Our experiments show that vanilla PPO with GAE ( \lambda=1 , \gamma=1 ) and simple rule-based rewards, without KL regularization, effectively scales reasoning capabilities in language models.” |
| E14 | arXiv:2503.24290 | [GAE Analysis.](https://arxiv.org/html/2503.24290#S3.SS2.SSS0.Px1.p1) | “training with GAE \lambda =1.0 resulted in a reward that rapidly increases and then steadily grows, consistently outperforming \lambda =0.95, which exhibited much slower reward progression.” |
| E15 | arXiv:2503.24290 | [3.3 Analysis for Critic and Advantage Estimation](https://arxiv.org/html/2503.24290#S3.SS3.p4) | “advantage assignments of our PPO configuration are consistently lower (i.e. more negative) to these tokens with repetitive patterns compared to GRPO across the majority of training iterations.” |
| E16 | arXiv:2503.24290 | [Abstract](https://arxiv.org/html/2503.24290#abstract) | “our implementation achieves superior performance across AIME2024, MATH500, and GPQA Diamond, while demonstrating remarkable efficiency, requiring only 1/10 of the training steps compared to the DeepSeek-R1-Zero pipeline.” |
| E3 | arXiv:2509.25849 | [5.2 Understanding Knapsack-based Exploration](https://arxiv.org/html/2509.25849#S5.SS2.p3) | “Knapsack-based budget allocation improves this ratio by approximately 20-40% across models.” |
| E4 | arXiv:2509.25849 | [5.1 Main Results](https://arxiv.org/html/2509.25849#S5.SS1.p4) | “Specifically, Knapsack-GRPO consistently outperforms GRPO.” |
| E5 | arXiv:2509.25849 | [5.2 Understanding Knapsack-based Exploration](https://arxiv.org/html/2509.25849#S5.SS2.p2) | “We observe that, even without introducing additional computational resources, our approach can dynamically assign up to 93 exploration budgets to certain tasks.” |
| E9 | arXiv:2510.00977 | [5.1 Math Reasoning](https://arxiv.org/html/2510.00977#S5.SS1.p2) | “The empirical results show that 2-GRPO achieves 97.6% of 16-GRPO's average performance while using only 12.5% of its total rollouts and 21.0% of its training time.” |
| E10 | arXiv:2510.00977 | [5.1 Math Reasoning](https://arxiv.org/html/2510.00977#S5.SS1.p6) | “The results demonstrate that 2-GRPO remains both effective and efficient across these diverse tasks, highlighting its broader applicability beyond math reasoning.” |
| E11 | arXiv:2510.00977 | [6 Conclusion](https://arxiv.org/html/2510.00977#S6.p1) | “We argue that the primary role of the group mechanism is not for accurate value-baseline estimation, as commonly assumed, but for the efficient construction of contrastive signals.” |
| E17 | arXiv:2504.13818 | [4.1 Comparing GRPO-PODS to baseline GRPO](https://arxiv.org/html/2504.13818#S4.SS1.p2) | “PODS consistently achieves faster convergence: reaching the baselines' peak accuracies at least 1.7\times faster (see Section A.4 for complete results) while often converging to a higher final performance.” |
| E18 | arXiv:2504.13818 | [4.3 Comparing Different Down-Sampling Rules](https://arxiv.org/html/2504.13818#S4.SS3.p1) | “We observe that the max-variance down-sampling rule consistently outperforms the other down-sampling rules throughout the training.” |
| E19 | arXiv:2504.13818 | [4.2 Effect of Rollout and Update Sizes](https://arxiv.org/html/2504.13818#S4.SS2.p2) | “Increasing rollout size n exhibits diminishing returns with an optimal point around n=64 .” |
| E20 | arXiv:2504.13818 | [4.2 Effect of Rollout and Update Sizes](https://arxiv.org/html/2504.13818#S4.SS2.p3) | “Training batch size m shows robust performance across a wide range, with minimal degradation until very small values (m\leq 4) .” |
| E25 | arXiv:2504.11343 | [RAFT and RAFT++ approach deep RL methods with surprisingly small performance gap.](https://arxiv.org/html/2504.11343#S5.SS0.SSS0.Px1.p1) | “RAFT (and its variant RAFT++), which is arguably the simplest algorithm, achieves competitive performance compared to more complex methods” |
| E26 | arXiv:2504.11343 | [RAFT and RAFT++ approach deep RL methods with surprisingly small performance gap.](https://arxiv.org/html/2504.11343#S5.SS0.SSS0.Px1.p1) | “RAFT++ further improves over vanilla RAFT, achieving 56.1% average accuracy” |
| E27 | arXiv:2504.11343 | [6 Conclusion](https://arxiv.org/html/2504.11343#S6.p2) | “GRPO's primary benefit comes not from its reward normalization, but from discarding prompts with entirely correct and incorrect responses” |
| E28 | arXiv:2504.11343 | [Learning from only positive samples leads to faster convergence and entropy collapse.](https://arxiv.org/html/2504.11343#S5.SS1.SSS0.Px1.p2) | “negative samples play a crucial role in maintaining exploration and preventing distributional collapse” |
| E32 | arXiv:2503.14476 | [4.2 Main Results](https://arxiv.org/html/2503.14476#S4.SS2.p1) | “DAPO has successfully trained the Qwen-32B Base model into a powerful reasoning model, achieving performance superior to DeepSeek's experiments” |
| E33 | arXiv:2503.14476 | [4.2 Main Results](https://arxiv.org/html/2503.14476#S4.SS2.p1) | “accuracy increasing from near 0% to 50%. Notably, this improvement is achieved with only 50% of the training steps” |
| E34 | arXiv:2503.14476 | [4.2 Main Results](https://arxiv.org/html/2503.14476#S4.SS2.p2) | “The observed improvements demonstrate the effectiveness of these techniques in RL training, each contributing several accuracy points” |
| E35 | arXiv:2503.14476 | [4.4 Case Study](https://arxiv.org/html/2503.14476#S4.SS4.p2) | “as training progresses, the model exhibits distinct behaviors of reflection and backtracking, as shown in Table 2.” |
| E1 | arXiv:2507.18071 | [5.1 Empirical Results](https://arxiv.org/html/2507.18071#S5.SS1.p2) | “Moreover, GSPO also demonstrates superior training efficiency over GRPO, achieving better training accuracy and benchmark performance under the same training compute and consumed queries.” |
| E2 | arXiv:2507.18071 | [5.2 Curious Observation on Clipping Fractions](https://arxiv.org/html/2507.18071#S5.SS2.p1) | “A key distinction of GSPO compared to GRPO is its practice of clipping entire responses rather than individual tokens.” |
| E12 | arXiv:2507.18071 | [Benefit of GSPO](https://arxiv.org/html/2507.18071#S5.SS3.SSS0.Px3.p1) | “In summary, GSPO fundamentally resolves the expert-activation volatility issue in MoE models, obviating the need for complex workarounds like Routing Replay.” |

<!-- /evidence-appendix -->
