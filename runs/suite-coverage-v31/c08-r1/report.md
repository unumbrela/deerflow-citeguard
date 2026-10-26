# Systematic Literature Review: Advances in GRPO for Generation Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "GRPO Group Relative Policy Optimization", filtered to primary category cs.LG
**Citation format**: APA 7th edition

## Executive Summary

Group Relative Policy Optimization (GRPO) has emerged as a significant reinforcement learning paradigm for generation models, particularly in the context of large language model reasoning and multi-objective optimization. The surveyed literature from 2024-2026 reveals a rapidly evolving field focused on addressing GRPO's core limitations: reward hacking in multi-objective settings, inefficiency in rollout allocation, sensitivity to small sample sizes, and incompatibility with safety constraints. Recent advances extend GRPO through median-centered baselines for stability, weakly-supervised guidance for rollout efficiency, distributionally robust optimization for dynamic resource allocation, and constrained formulations for safety-critical domains. The collective work demonstrates GRPO's adaptability across diverse applications including LLM reasoning, masked diffusion models, hyperparameter optimization, and autonomous systems.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "GRPO Group Relative Policy Optimization", filtered to category cs.LG, published between 2024-02-21 and 2026-02-21. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Stabilizing GRPO Through Improved Baseline Estimation

A central challenge in GRPO is the sensitivity of advantage estimation to the baseline used for within-group normalization. When rollout budgets are small, the shared baseline becomes noisy, leading to advantage sign flips where rollouts receive incorrect policy update signals. Kim (2026) addresses this through MC-GRPO, which replaces the mean baseline with a median baseline that is far less sensitive to outlier rewards. The median-centered approach reduces the accuracy gap between G=2 and G=8 rollout sizes to within 1%, enabling resource-constrained training without sacrificing performance. Similarly, Sane (2025) proposes Hybrid GRPO, which balances empirical multi-sample evaluation with bootstrapped value estimation to mitigate variance amplification observed in purely empirical GRPO methods. Both approaches recognize that the quality of the baseline fundamentally determines update stability, and that robust statistics or hybrid estimation can preserve signal quality even under tight computational budgets.

### Theme 2: Multi-Objective Reward Alignment and Anti-Hacking Mechanisms

GRPO's tendency to optimize single objectives at the expense of others poses significant challenges for multi-objective reinforcement learning. Ichihara et al. (2025) introduce MO-GRPO, which automatically reweights reward functions according to their value variances, ensuring even contribution across objectives without manual tuning. The method analytically preserves preference ordering while preventing reward hacking—a critical failure mode where the policy exploits one reward component while neglecting others. This automatic balancing mechanism demonstrates stable learning across multi-armed bandits, Mo-Gymnasium, machine translation, and instruction following tasks. The broader implication is that GRPO's within-group normalization, when left unmodified, creates implicit reward weighting that can be pathological; explicit variance-based reweighting restores balanced optimization across competing objectives.

### Theme 3: Rollout Efficiency and Weakly-Supervised Guidance

The computational cost of multi-rollout generation has motivated work on reducing redundant deliberation while maintaining correctness. Mundada et al. (2026) propose WS-GRPO, which converts terminal rewards into correctness-aware guidance over partial trajectories by training a preference model from outcome-only correctness. This provides continue/stop signals for prefixes without requiring global length penalties, which are difficult to calibrate across problems of varying difficulty. The approach substantially reduces rollout length compared to GRPO baselines while remaining competitive in accuracy. This theme reflects a broader recognition that GRPO's rollout inefficiency stems from overthinking—extended deliberation that does not improve correctness—and that weakly-supervised prefix-level signals can terminate unproductive computation earlier.

### Theme 4: Distributionally Robust Optimization for Dynamic Resource Allocation

Static uniform prompt sampling and fixed rollout allocation represent structural inefficiencies in standard GRPO paradigms. Panaganti et al. (2026) introduce Multi-Adversary Group Distributionally Robust Optimization (GDRO) with two independent games: Prompt-GDRO dynamically partitions prompts into difficulty groups and upweights hard ones using an EMA-debiased multiplicative-weights bandit sampler, while Rollout-GDRO employs a shadow-price controller to reallocate rollouts across groups under a compute-neutral budget. The adversarial controllers achieve no-regret guarantees and form an emergent curriculum where resources shift to the evolving reasoning frontier, yielding +10.6% and +10.1% gains in pass@8 accuracy respectively. This work reframes GRPO training as a dynamic allocation problem where adversaries learn to identify and prioritize challenging examples rather than treating all prompts equally.

### Theme 5: Constrained GRPO for Safety-Critical Domains

Extending GRPO to safety-critical applications requires compatibility with constrained policy optimization, but standard Lagrangian methods fail due to GRPO's within-group normalization creating shared-denominator coupling. Girgis et al. (2026) address this by scalarizing standardized advantages rather than rewards, which eliminates the coupling issue and yields better-conditioned multiplier dynamics. The constrained GRPO formulation achieves better adherence to specified constraints while maintaining or improving task performance across gridworld, autonomous driving, and mathematical reasoning tasks. This modification is critical for deploying GRPO in domains like surgical robotics and autonomous drones where constraint violations are unacceptable, and it reveals that GRPO's normalization structure requires careful reformulation when combined with Lagrangian constraint enforcement.

### Theme 6: GRPO Applications Beyond Language Models

While much GRPO research targets LLM post-training, recent work extends the paradigm to diverse generation tasks. Zhou et al. (2025) reformulate masked diffusion model (MDM) generation as a unified Markov Decision Process and apply trajectory-level GRPO to cooperatively optimize both model parameters and inference schedule parameters under a shared reward. Co-GRPO aligns training with inference more thoroughly than single-step BERT-style objectives, substantially improving generation quality across ImageReward, HPS, GenEval, and DPG-Bench without backpropagation through multi-step generation. Guo et al. (2025) integrate GRPO with Transformer-based hyperparameter optimization in GRPOformer, using policy churn regularization to enhance training stability while learning optimization strategies from scratch. These applications demonstrate GRPO's flexibility as a general-purpose policy optimization tool for generation problems beyond language modeling.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the insight that GRPO's within-group normalization structure creates specific failure modes requiring targeted modifications. Kim (2026), Girgis et al. (2026), and Ichihara et al. (2025) all identify that the shared baseline or normalization denominator introduces coupling that degrades performance under specific conditions (small rollouts, constraints, multi-objective settings). There is also broad agreement that GRPO benefits from additional structure—whether median baselines, variance-based reweighting, or adversarial controllers—to stabilize training and improve sample efficiency.

**Disagreements**: The literature does not show direct contradictions, but there is tension between approaches that modify GRPO's core advantage computation (Kim, 2026; Girgis et al., 2026) versus those that add auxiliary mechanisms without changing the baseline (Mundada et al., 2026; Panaganti et al., 2026). Mroueh et al. (2025) demonstrate that off-policy GRPO can match or exceed on-policy performance, challenging the assumption that GRPO requires fresh on-policy samples—a finding that could significantly impact the computational efficiency of all other GRPO variants if widely adopted.

## Gaps and Open Questions

The collective literature reveals several unaddressed gaps:

1. **Limited empirical scope**: Most papers validate on specific benchmarks (DAPO 14.1k, MuJoCo, specific LLM scales) without cross-domain comparison, making it difficult to assess which GRPO variants generalize best across task types.

2. **Absence of theoretical analysis**: While several papers provide empirical improvements, few offer theoretical guarantees beyond no-regret bounds for adversarial controllers. The stability properties of median-centered baselines, variance-based reweighting, and advantage scalarization remain empirically observed but theoretically uncharacterized.

3. **Computational overhead**: Several methods (trajectory-level optimization in Co-GRPO, adversarial controllers in GDRO, preference model training in WS-GRPO) introduce additional computation, but none provide detailed cost-benefit analysis comparing improvement gains to overhead.

4. **Interaction between variants**: The papers propose orthogonal modifications (median baseline, constrained formulation, multi-objective reweighting, rollout efficiency), but no work explores whether combining these yields compounding benefits or conflicting interactions.

5. **Off-policy GRPO underutilization**: Mroueh et al. (2025) demonstrate off-policy GRPO's viability, but no other surveyed paper incorporates off-policy training, suggesting a missed opportunity for sample efficiency improvements across all variants.

## Per-Paper Annotations

### Girgis et al. (2026)

**Research question**: How can Group Relative Policy Optimization be made compatible with constrained policy optimization for safety-critical domains?
**Methodology**: Constrained GRPO introduces a Lagrangian-based extension that scalarizes standardized advantages rather than rewards to address shared-denominator coupling, yielding better-conditioned updates and more stable constraint enforcement.
**Key findings**:
- Addresses critical Lagrangian-specific failure mode in GRPO's within-group normalization
- Scalarizing standardized advantages eliminates shared-denominator coupling issues
- Results in better-behaved multiplier dynamics and more stable constraint enforcement
- Achieves better adherence to specified constraints while maintaining or improving task performance
- Validated across gridworld, autonomous driving benchmark, and mathematical reasoning tasks
**Limitations**: not stated in abstract

### Guo et al. (2025)

**Research question**: How can reinforcement learning techniques, specifically Group Relative Policy Optimization, be integrated with Transformer-based methods to improve hyperparameter optimization efficiency and performance?
**Methodology**: GRPOformer uses Transformers to generate hyperparameter configurations from historical optimization trajectories while applying GRPO for rapid trajectory construction and optimization strategy learning, with Policy Churn Regularization (PCR) to enhance training stability.
**Key findings**:
- GRPOformer integrates reinforcement learning with Transformers for hyperparameter optimization
- The framework can learn optimization strategies from scratch without relying on large-scale historical trajectories
- Policy Churn Regularization enhances the stability of GRPO training
- Experimental results on OpenML show GRPOformer consistently outperforms baseline methods across diverse tasks
**Limitations**: not stated in abstract

### Ichihara et al. (2025)

**Research question**: How can Group Relative Policy Optimization be extended to prevent reward hacking in multi-objective settings where it tends to optimize only one objective at the cost of others?
**Methodology**: MO-GRPO extends GRPO with a normalization method that automatically reweights reward functions according to the variances of their values, analytically proven to ensure even contribution of all reward functions while preserving preference order.
**Key findings**:
- Ensures all reward functions contribute evenly to the loss function without manual tuning
- Preserves the order of preferences across objectives
- Achieves stable learning by evenly distributing correlations among reward components
- Outperforms standard GRPO across multi-armed bandits, Mo-Gymnasium, machine translation, and instruction following tasks
- Demonstrates promise for multi-objective reinforcement learning problems
**Limitations**: not stated in abstract

### Kim (2026)

**Research question**: How can Group Relative Policy Optimization maintain accuracy in resource-constrained settings where the rollout budget is small?
**Methodology**: MC-GRPO replaces the mean baseline with a median baseline to mitigate advantage sign flips caused by noise in the shared baseline, generating one additional rollout for median reference (G+1) and excluding the pivot rollout from backpropagation.
**Key findings**:
- Mitigates advantage sign flips where rollouts receive incorrect advantage signs under small rollout sizes
- Consistently improves stability and final accuracy in the low-rollout regime
- Reduces the gap between G=2 and G=8 rollout sizes to within 1%
- The median baseline is far less sensitive to outlier rewards than the mean
- Preserves the core update cost of standard G-rollout training
**Limitations**: not stated in abstract

### Mroueh et al. (2025)

**Research question**: Can Group Relative Policy Optimization (GRPO) be effectively adapted to off-policy training regimes to improve stability, sampling efficiency, and memory usage similar to off-policy PPO?
**Methodology**: The authors adapt GRPO to the off-policy setting and theoretically show that both on-policy and off-policy GRPO objectives yield reward improvement, motivating clipped surrogate objectives for off-policy GRPO, with empirical comparison during post-training with verifiable rewards.
**Key findings**:
- Both on-policy and off-policy GRPO objectives theoretically yield an improvement in the reward
- Off-policy GRPO either significantly outperforms or performs on par with its on-policy counterpart in empirical evaluations
- The analysis supports using clipped surrogate objectives in the off-policy version of GRPO
- Off-policy training can improve training stability, sampling efficiency, and memory usage for GRPO
**Limitations**: The abstract does not explicitly state limitations of the off-policy GRPO approach or the empirical evaluation scope

### Mundada et al. (2026)

**Research question**: How can Group Relative Policy Optimization control inefficient reasoning and overthinking while maintaining the trade-off between correctness and rollout efficiency?
**Methodology**: WS-GRPO converts terminal rewards into correctness-aware guidance over partial trajectories by training a preference model from outcome-only correctness to produce prefix-level signals, providing outcome-derived continue/stop guidance without requiring global length penalties.
**Key findings**:
- Substantially reduces rollout length compared to GRPO baselines
- Remains competitive with GRPO in terms of accuracy
- Reduces redundant deliberation while maintaining correctness
- Supplies outcome-derived continue/stop guidance for partial trajectories
- Addresses the difficulty of calibrating length penalties for problems of varying difficulty
**Limitations**: not stated in abstract

### Panaganti et al. (2026)

**Research question**: How can reinforcement learning for LLM reasoning overcome the structural inefficiencies of static uniform prompt sampling and fixed rollout allocation in standard GRPO paradigms?
**Methodology**: Multi-Adversary Group Distributionally Robust Optimization (GDRO) uses two independent games: Prompt-GDRO with an EMA-debiased multiplicative-weights bandit sampler to dynamically partition prompts into difficulty groups, and Rollout-GDRO with a shadow-price controller to reallocate rollouts under a compute-neutral budget.
**Key findings**:
- Prompt-GDRO achieves an average relative gain of +10.6% in pass@8 accuracy across model scales compared to the GRPO baseline
- Rollout-GDRO achieves an average relative gain of +10.1% in pass@8 accuracy across model scales compared to the GRPO baseline
- The adversarial controllers provide no-regret guarantees and a variance-proxy analysis motivating square-root optimal rollout allocation
- An emergent curriculum forms where adversaries dynamically shift resources to the evolving reasoning frontier
- The Online Difficulty Classifier successfully partitions prompts into dynamic pass@k difficulty groups for targeted training
**Limitations**: The abstract does not explicitly state limitations, though the validation is specific to the DAPO 14.1k dataset and Qwen3-Base models

### Rahman (2025)

**Research question**: How can Proximal Policy Optimization overcome the brittle trade-off between aggressive clipping that stifles early exploration and late-stage updates that destabilize convergence?
**Methodology**: PPO-BR fuses exploration and convergence signals into a single bounded trust region by combining entropy-driven expansion for high-uncertainty states with reward-guided contraction for convergence stability, evaluated on six diverse benchmarks including MuJoCo, Atari, and sparse-reward environments.
**Key findings**:
- Achieves 29.1% faster convergence with statistical significance (p < 0.001)
- Reduces reward variance by 2.3x compared to standard PPO
- Introduces less than 1.8% runtime overhead with only five lines of code change
- Enables deployment in safety-critical domains like surgical robotics and autonomous drones
- Offers a unified entropy-reward mechanism applicable to both language models and general reinforcement learning
**Limitations**: not stated in abstract

### Sane (2025)

**Research question**: How can a hybrid approach combining empirical multi-sample action evaluation with value function-based learning improve upon purely empirical GRPO and standard PPO methods?
**Methodology**: Hybrid GRPO introduces a structured advantage computation method balancing empirical action sampling with bootstrapped value estimation, with mathematical comparison between PPO, DeepSeek GRPO, and Hybrid GRPO, and experimental validation in a controlled reinforcement learning environment.
**Key findings**:
- Hybrid GRPO achieves superior convergence speed compared to existing PPO and GRPO methods
- The hybrid approach provides more stable policy updates than purely empirical methods
- Hybrid GRPO improves sample efficiency by balancing empirical sampling with value function-based learning
- The framework mitigates variance amplification observed in purely empirical GRPO methods
- Extensions including entropy-regularized sampling, hierarchical multi-step sub-sampling, and adaptive reward normalization are explored
**Limitations**: The abstract does not explicitly state limitations, though experimental validation appears to be in a controlled reinforcement learning environment rather than large-scale LLM post-training

### Zhou et al. (2025)

**Research question**: How can the discrepancy between Masked Diffusion Model training (single-step BERT-style objective) and inference (multi-step iterative process with schedules) be addressed to improve generation quality?
**Methodology**: Co-GRPO reformulates MDM generation as a unified Markov Decision Process that jointly incorporates both the model and inference schedule, then applies GRPO at the trajectory level to cooperatively optimize model parameters and schedule parameters under a shared reward without backpropagation through the multi-step generation process.
**Key findings**:
- Co-GRPO aligns training with inference more thoroughly by optimizing both model and schedule parameters at the trajectory level
- The approach substantially improves generation quality without requiring costly backpropagation through multi-step generation
- Empirical results demonstrate effectiveness across four benchmarks: ImageReward, HPS, GenEval, and DPG-Bench
- The MDP formulation successfully treats MDM generation as a cooperative optimization problem between model and schedule
**Limitations**: The abstract does not explicitly state limitations, though the computational cost of trajectory-level optimization and generalization to other diffusion model variants are not discussed

## References

Girgis, R., de Schaetzen, R., Rowe, L., Robitaille, A., Pal, C., & Paull, L. (2026). Constrained group relative policy optimization. arXiv. https://arxiv.org/abs/2602.05863

Guo, H., Pan, J., & Zhai, W. (2025). GRPOformer: Advancing hyperparameter optimization via group relative policy optimization. arXiv. https://arxiv.org/abs/2509.17105

Ichihara, Y., Jinnai, Y., Morimura, T., Sakamoto, M., Mitsuhashi, R., & Uchibe, E. (2025). MO-GRPO: Mitigating reward hacking of group relative policy optimization on multi-objective problems. arXiv. https://arxiv.org/abs/2509.22047

Kim, Y. (2026). MC-GRPO: Median-centered group relative policy optimization for small-rollout reinforcement learning. arXiv. https://arxiv.org/abs/2601.22582

Mroueh, Y., Dupuis, N., Belgodere, B., Nitsure, A., Rigotti, M., Greenewald, K., Navratil, J., Ross, J., & Rios, J. (2025). Revisiting group relative policy optimization: Insights into on-policy and off-policy training. arXiv. https://arxiv.org/abs/2505.22257

Mundada, G., Huang, Z., Surana, R., Yu, S., Zhang, J. Y., Li, X., Yu, T., Yao, L., Shang, J., McAuley, J., & Wu, J. (2026). WS-GRPO: Weakly-supervised group-relative policy optimization for rollout-efficient reasoning. arXiv. https://arxiv.org/abs/2602.17025

Panaganti, K., Liang, Z., Yu, W., Mi, H., & Yu, D. (2026). Group distributionally robust optimization-driven reinforcement learning for LLM reasoning. arXiv. https://arxiv.org/abs/2601.19280

Rahman, B. (2025). PPO-BR: Dual-signal entropy-reward adaptation for trust region policy optimization. arXiv. https://arxiv.org/abs/2505.17714

Sane, S. (2025). Hybrid group relative policy optimization: A multi-sample approach to enhancing policy optimization. arXiv. https://arxiv.org/abs/2502.01652

Zhou, R., Ni, Z., Chen, T., Liu, Z., Yue, Y., Wang, Y., Wang, Y., Liu, J., & Huang, G. (2025). Co-GRPO: Co-optimized group relative policy optimization for masked diffusion model. arXiv. https://arxiv.org/abs/2512.22288
