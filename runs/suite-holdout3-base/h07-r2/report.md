# Systematic Literature Review: Offline Reinforcement Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "offline reinforcement learning", category cs.LG, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on offline reinforcement learning from the past two years reveals a field maturing from purely algorithmic innovation toward addressing practical deployment challenges. The surveyed papers collectively demonstrate three major shifts: (1) moving beyond batch-constrained learning to enable more flexible policy improvement through state-constrained frameworks and optimal transport formulations; (2) tackling data scarcity through reward imputation, sparsity-based regularization, and trajectory-level augmentation; and (3) establishing theoretical foundations for generalization, convergence guarantees, and robustness analysis. Recent work increasingly emphasizes real-world applicability through domain-specific benchmarks in autonomous driving and robot control, while simultaneously identifying critical vulnerabilities in existing methods when faced with action perturbations. The field shows strong convergence on pessimistic approaches for generalization and value-guided methods for handling multi-modal behavioral data, though significant gaps remain in discrete action spaces and cross-domain transfer.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "offline reinforcement learning", filtered to category cs.LG, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review focuses exclusively on cs.LG category and may miss relevant work published in adjacent categories such as cs.RO or cs.AI without cross-listing.

## Themes

### Theme 1: Overcoming Distributional Shift Through Flexible Constraints

A central challenge in offline RL is the distributional shift between the learned policy and the behavior policy that generated the dataset. Traditional batch-constrained methods restrict policies to state-action pairs present in the dataset, which prevents extrapolation but also limits improvement. Recent work has proposed more flexible approaches that maintain safety while enabling broader exploration.

Hepburn et al. (2024) introduce state-constrained offline RL, which shifts focus from constraining the state-action distribution to constraining only the state distribution. This allows policies to take out-of-distribution actions as long as they lead to in-distribution states, significantly expanding the learning horizon. Their StaCQ algorithm achieves state-of-the-art performance on D4RL benchmarks by combining this theoretical framework with practical deep learning implementation.

Asadulaev et al. (2024) take a different approach by reframing offline RL as an optimal transport problem. Their algorithm maps states to partial distributions of the best expert actions, effectively "stitching" together optimal behaviors from heterogeneous datasets containing both expert and sub-optimal demonstrations. This perspective enables extracting high-quality policies even when individual trajectories are sub-optimal, provided the collective dataset contains sufficient optimal behavior fragments.

Jiang et al. (2026) address the specific problem of OOD mode averaging in flow-based policy distillation. When distilling behavior policies with multi-modal data, standard methods interpolate across behavioral modes, causing action collapse. Their Value-Rectified Distillation framework uses value-guided trajectory alignment to decouple distinct modes and isolate high-value actions, demonstrating particular effectiveness on multi-modal, non-expert datasets.

### Theme 2: Learning from Limited and Imperfect Data

Many real-world offline RL applications face severe data constraints compared to standard benchmarks that use millions of data points. Several papers address this challenge through different mechanisms.

Arnob et al. (2025) identify that offline RL algorithms overfit on small datasets and propose Sparse-Reg, a sparsity-based regularization technique. Their work highlights the gap between benchmark datasets with over a million data points and real-world applications with considerably smaller datasets. Sparse-Reg enables effective learning in these limited data settings by preventing overfitting through sparsity constraints, outperforming state-of-the-art baselines in continuous control tasks.

Romeo and Bagdanov (2024) tackle the related problem of reward scarcity. Many offline RL algorithms require extensive reward annotations, which are costly or impossible to obtain in real-world scenarios. Their reward imputation approach learns a reward model from just 1% of reward-labeled transitions, then uses this model to impute rewards for the remaining 99% of transitions. This enables applying offline RL techniques in data-scarce scenarios where only minimal reward supervision is available.

Schmähling et al. (2026) propose trajectory-level data augmentation to enable training from limited suboptimal trajectories. Their method exploits task structure and geometric relationships between rewards, value functions, and logging policies to augment the effective dataset size. By supporting suboptimal logging policies during data collection, the approach increases practical applicability in scenarios where collecting expert data is infeasible.

### Theme 3: Theoretical Foundations for Generalization and Convergence

As offline RL moves toward real-world deployment, theoretical understanding of when and why methods work has become increasingly important. Recent work has established formal guarantees for generalization and convergence in offline settings.

Wang et al. (2025) provide the first theoretical analysis of zero-shot generalization in offline RL, where agents trained on multiple environments must perform well on unseen test environments. They show that classical offline RL fails to generalize and propose two algorithms—pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO)—that leverage pessimistic policy evaluation to achieve near-optimal policies with zero-shot generalization. This work establishes pessimism as a key mechanism for enabling generalization beyond training environments.

Hoischen et al. (2025) address the statistical understanding of approximation errors in continuous-time offline RL. By linking RL to the Hamilton-Jacobi-Bellman equation and using operator-theoretic methods in reproducing kernel Hilbert spaces, they establish global convergence guarantees under sufficiently small generator-approximation error. Their finite-sample guarantees provide explicit bounds tied to system properties like smoothness and stability, offering theoretical grounding for operator-based approaches to continuous-time optimal control.

### Theme 4: Domain-Specific Benchmarks and Real-World Applications

The field has moved beyond abstract benchmarks toward domain-specific datasets and evaluation frameworks that reflect real-world deployment scenarios.

Lee et al. (2024) address the over-reliance on game tasks and synthetic datasets by creating AD4RL, a comprehensive autonomous driving benchmark for offline RL. They provide 19 datasets including real-world human driver trajectories, implement seven popular offline RL algorithms, and establish three realistic driving scenarios. Their unified decision-making process model serves as a reference framework, enabling practical offline RL research that captures the complexities of autonomous driving rather than simplified game environments.

Ayabe et al. (2024) conduct a critical robustness evaluation of offline RL for robot control, specifically examining vulnerability to action perturbations that simulate joint actuator faults. Their experiments with legged robots reveal that existing offline RL methods are significantly more vulnerable to perturbations than online RL methods. This work highlights a crucial gap: while offline RL is promising for robot control due to its ability to learn from historical data without environment interaction, current methods lack the robustness needed for real-world deployment where actuator faults and perturbations are common.

### Theme 5: Pessimism and Value-Guided Learning

A recurring methodological theme across multiple papers is the use of pessimistic estimation and value-guided mechanisms to improve offline RL performance.

Wang et al. (2025) demonstrate that pessimistic policy evaluation enables zero-shot generalization, with both PERM and PPPO relying on pessimism to guide policy learning toward robust solutions that transfer across environments. This aligns with broader trends in offline RL where pessimism serves as a mechanism for handling distributional shift.

Jiang et al. (2026) employ value-guided mechanisms in their VRD framework, using value-quantile behavior distillation (VRD-Q) to statistically filter low-value behaviors and value-guided trajectory alignment to isolate high-value actions. This value-guided approach prevents the policy from collapsing into OOD regions by explicitly incorporating value information into the distillation process.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key insights. First, there is broad agreement that traditional batch-constrained offline RL is too restrictive, with multiple approaches (state-constrained RL, optimal transport formulations, value-rectified distillation) seeking to enable broader policy improvement while maintaining safety. Second, pessimism emerges as a unifying principle across different papers for handling distributional shift and enabling generalization. Third, there is consensus that data efficiency—whether through reward imputation, sparsity regularization, or data augmentation—is critical for real-world applicability, as benchmark-scale datasets are rarely available in practice.

**Disagreements**: The surveyed papers do not exhibit fundamental disagreements but rather address different facets of the offline RL problem. One potential tension exists between methods that assume access to some reward signal (reward imputation approaches) versus those that work with purely offline data without reward modeling. Additionally, theoretical work establishing convergence guarantees under specific conditions (small generator-approximation error) may not align with practical scenarios where these conditions are difficult to verify or ensure.

## Gaps and Open Questions

Several significant gaps emerge from the collective literature:

1. **Discrete Action Spaces**: Most surveyed methods focus on continuous control tasks (D4RL, locomotion, autonomous driving). The applicability of these approaches to discrete action spaces remains largely unexplored, particularly for methods like value-rectified distillation that rely on continuous flow matching formulations.

2. **Cross-Domain Transfer**: While zero-shot generalization across environments within a domain has been studied, transfer across fundamentally different domains (e.g., from simulation to reality, or from one task domain to another) remains an open challenge.

3. **Robustness Solutions**: Ayabe et al. (2024) identify critical vulnerabilities to action perturbations but do not propose solutions. The field lacks systematic approaches for building robustness into offline RL algorithms, representing a significant gap between problem identification and solution development.

4. **Reward Model Errors**: While reward imputation enables learning from minimal reward annotations, the propagation of reward model errors through the learning process is not well understood. Errors in the 1% labeled sample could cascade through the 99% imputed rewards, but this failure mode is not systematically analyzed.

5. **Computational Scalability**: Methods like optimal transport formulations and operator-theoretic approaches may introduce significant computational overhead. The scalability of these methods to large-scale problems with high-dimensional state and action spaces remains unaddressed.

6. **Theoretical-Practical Gap**: Theoretical guarantees often require conditions (sufficiently small approximation error, specific smoothness properties) that are difficult to verify in practice. Bridging this gap between theoretical assurances and practical verification remains an open challenge.

## Per-Paper Annotations

### Arnob et al. (2025)

**Research question**: How can offline RL algorithms overcome overfitting when trained on small datasets considerably smaller than the million-plus data points common in benchmarks?

**Methodology**: Introduces Sparse-Reg, a regularization technique based on sparsity designed to mitigate overfitting in offline reinforcement learning for limited data settings.

**Key findings**:
- Offline RL algorithms overfit on small datasets, resulting in poor performance
- Many real-world offline RL applications rely on considerably smaller datasets than common benchmarks
- Sparse-Reg enables effective learning in limited data settings
- Outperforms state-of-the-art baselines in continuous control tasks with small datasets

**Limitations**: Focus primarily on continuous control domains; sparsity-based regularization may not generalize optimally to all offline RL application areas and dataset characteristics.

### Asadulaev et al. (2024)

**Research question**: How can we extract efficient policies from offline RL datasets containing behaviors from various experts, some of whom are sub-optimal?

**Methodology**: The authors reframe offline reinforcement learning as an optimal transportation problem and present an algorithm that finds a policy mapping states to a partial distribution of the best expert actions for each given state, effectively stitching together optimal behaviors.

**Key findings**:
- Optimal transport formulation enables stitching the best behaviors from heterogeneous expert datasets
- The algorithm maps states to partial distributions of best expert actions rather than full action distributions
- Demonstrates improvements over existing methods on D4RL continuous control benchmarks
- Effectively handles datasets with mixed expert quality levels
- Provides a novel theoretical perspective on offline RL through optimal transport theory

**Limitations**: Evaluation is limited to continuous control problems from D4RL; optimal transport computations may introduce significant computational overhead for large-scale problems.

### Ayabe et al. (2024)

**Research question**: How robust are existing offline reinforcement learning methods for robot control against real-world challenges such as joint actuator faults and action perturbations?

**Methodology**: Evaluates existing offline RL methods using legged robots from OpenAI Gym based on average episodic rewards, simulating failures by incorporating both random and adversarial perturbations into joint torque signals.

**Key findings**:
- Existing offline RL methods exhibit significant vulnerabilities to action perturbations
- Offline RL methods are more vulnerable to perturbations than online RL methods
- Both random and adversarial perturbations to joint torque signals significantly degrade performance
- Highlights critical need for more robust offline RL approaches in robot control applications

**Limitations**: Evaluation limited to legged robots in OpenAI Gym; study identifies vulnerabilities but does not propose or validate solutions to improve robustness.

### Hepburn et al. (2024)

**Research question**: How can offline RL overcome the limitation of batch-constrained methods that restrict policies to only actions present in the dataset?

**Methodology**: Introduces state-constrained offline RL framework that focuses on the dataset's state distribution rather than state-action distribution, allowing out-of-distribution actions that lead to in-distribution states, and proposes StaCQ deep learning algorithm.

**Key findings**:
- State-constrained approach allows policies to take high-quality out-of-distribution actions leading to in-distribution states
- Broadens the learning horizon compared to traditional batch-constrained offline RL
- Improves ability to combine different trajectories from the dataset effectively
- StaCQ achieves state-of-the-art performance on D4RL benchmark datasets

**Limitations**: Theoretical findings require further development; the new framework needs additional exploration and validation across more diverse domains beyond D4RL benchmarks.

### Hoischen et al. (2025)

**Research question**: How can we establish statistical guarantees for approximation errors when learning policies from offline datasets in continuous-time stochastic systems?

**Methodology**: Links reinforcement learning to the Hamilton-Jacobi-Bellman equation and proposes an operator-theoretic algorithm based on dynamic programming recursion, representing the world model as the infinitesimal generator of controlled diffusion processes learned in a reproducing kernel Hilbert space.

**Key findings**:
- Establishes global convergence of the value function under sufficiently small generator-approximation error
- Derives explicit finite-sample guarantees with bounds tied directly to system properties such as smoothness and stability
- Integrates statistical learning methods and operator theory to analyze offline RL
- Proof-of-concept results indicate operator-based approaches show promise for solving offline RL using continuous-time optimal control

**Limitations**: Results are primarily theoretical with proof-of-concept validation only; convergence guarantees require sufficiently small generator-approximation error which may be difficult to ensure in practice.

### Jiang et al. (2026)

**Research question**: How can we address Out-of-Distribution (OOD) Mode Averaging that occurs when distilling Flow Matching based behavior policies in offline reinforcement learning?

**Methodology**: The authors propose Value-Rectified Distillation (VRD), a framework that reformulates offline policy distillation as a value-guided generative trajectory alignment problem with a dynamic coupling mechanism. They instantiate VRD through two algorithms: VRD-Q (value-quantile behavior distillation to filter low-value behaviors) and VRD-R (latent space reorganization to geometrically isolate high-value trajectories).

**Key findings**:
- VRD actively rectifies flow dynamics to explicitly decouple distinct behavioral modes, preventing action collapse into invalid OOD regions
- VRD-Q statistically filters out low-value behaviors through value-quantile distillation
- VRD-R geometrically isolates high-value generative trajectories from the Flow Matching-based behavior policy
- VRD improves existing generative baselines across D4RL, OGBench, and Minari benchmarks
- Performance gains are especially pronounced on multi-modal, non-expert datasets

**Limitations**: The evaluation focuses on continuous control and planning tasks; the approach may not generalize to discrete action spaces or domains without clear value hierarchies.

### Lee et al. (2024)

**Research question**: How can we address the limitation that offline RL research relies primarily on game tasks with synthetic datasets rather than real-world practical applications?

**Methodology**: The authors provide 19 autonomous driving datasets including real-world human driver data, implement seven popular offline RL algorithms, and create a unified decision-making process model that operates across three realistic driving scenarios as a benchmark framework.

**Key findings**:
- Provides 19 datasets including real-world human driver trajectories for offline RL research
- Benchmarks seven popular offline RL algorithms across three realistic driving scenarios
- Offers a unified decision-making process model serving as a reference framework for algorithm design
- Enables practical offline RL research beyond synthetic game environments
- Facilitates community collaboration on practical aspects of reinforcement learning methods

**Limitations**: The benchmark is focused specifically on autonomous driving applications; findings and algorithm performance may not generalize to other domains, and the unified decision model may not capture all driving scenario complexities.

### Romeo and Bagdanov (2024)

**Research question**: How can we apply offline reinforcement learning in data-scarce scenarios where only a very limited sample of transitions are annotated with ground-truth rewards?

**Methodology**: The authors propose a Reward Model that estimates the reward signal from a limited sample of reward-annotated transitions, then uses this model to impute rewards for the remaining reward-free transitions, enabling ORL techniques to be applied to the augmented dataset.

**Key findings**:
- A learned reward model can effectively impute rewards using only 1% of reward-labeled transitions from original datasets
- The imputed rewards enable training of performant agents using standard Offline RL techniques
- The approach makes ORL applicable in scenarios where reward annotation is costly or limited
- Demonstrated successfully on D4RL continuous locomotion tasks
- Enables ORL deployment in real-world applications with limited reward supervision

**Limitations**: The approach still requires at least some reward-labeled transitions (minimum 1% tested); reward imputation quality depends on the representativeness of the initial labeled sample and may propagate errors.

### Schmähling et al. (2026)

**Research question**: How can we enable effective training of off-policy models from a limited number of suboptimal trajectories in offline reinforcement learning?

**Methodology**: The authors introduce a trajectory-based augmentation technique that exploits task structure and geometric relationships between rewards, value functions, and mathematical properties of logging policies to support suboptimal logging policies during data collection.

**Key findings**:
- Trajectory-level augmentation enables training from limited suboptimal trajectories
- The approach exploits geometric relationships between rewards and value functions for data quality improvement
- Supports suboptimal logging policies during data collection, increasing practical applicability
- Empirically validated across positioning tasks of varying dimensionality
- Demonstrates improved performance under partial observability conditions

**Limitations**: The method is motivated by and validated on active positioning problems; theoretical justification and empirical results may not transfer directly to other task domains.

### Wang et al. (2025)

**Research question**: How can offline RL agents trained on experiences from multiple environments generalize to unseen test environments without further interaction?

**Methodology**: Proposes two algorithms: pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to guide policy learning and enhance generalization.

**Key findings**:
- Classical offline RL fails to generalize to new, unseen environments
- Both PERM and PPPO can find near-optimal policies with zero-shot generalization property
- Pessimistic policy evaluation effectively guides policy learning for enhanced generalization
- Provides first theoretical understanding of the generalization phenomenon in offline reinforcement learning

**Limitations**: Represents only a first step in understanding generalization in offline RL; theoretical framework may not cover all environment types and generalization scenarios.

## References

Arnob, S. Y., Fujimoto, S., & Precup, D. (2025). Sparse-Reg: Improving sample complexity in offline reinforcement learning using sparsity. arXiv. https://arxiv.org/abs/2506.17155

Asadulaev, A., Korst, R., Korotin, A., Egiazarian, V., Filchenkov, A., & Burnaev, E. (2024). Rethinking optimal transport in offline reinforcement learning. arXiv. https://arxiv.org/abs/2410.14069

Ayabe, S., Otomo, T., Kera, H., & Kawamoto, K. (2024). Robustness evaluation of offline reinforcement learning for robot control against action perturbations. arXiv. https://arxiv.org/abs/2412.18781

Hepburn, C. A., Jin, Y., & Montana, G. (2024). State-constrained offline reinforcement learning. arXiv. https://arxiv.org/abs/2405.14374

Hoischen, N., Bevanda, P., Beier, M., Sosnowski, S., Houska, B., & Hirche, S. (2025). Infinitesimal operator world models: Finite-sample guarantees for offline reinforcement learning. arXiv. https://arxiv.org/abs/2511.10383

Jiang, K., Jiang, W., Kawahara, Y., & Tan, X. (2026). Value-rectified distillation for flow-based offline reinforcement learning. arXiv. https://arxiv.org/abs/2610.29075

Lee, D., Eom, C., & Kwon, M. (2024). AD4RL: Autonomous driving benchmarks for offline reinforcement learning with value-based dataset. arXiv. https://arxiv.org/abs/2404.02429

Romeo, C., & Bagdanov, A. D. (2024). Offline reinforcement learning with imputed rewards. arXiv. https://arxiv.org/abs/2407.10839

Schmähling, T., Burkhardt, M., & Windisch, T. (2026). Trajectory-level data augmentation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2605.13401

Wang, Z., Yang, C., Lui, J. C. S., & Zhou, D. (2025). Provable zero-shot generalization in offline reinforcement learning. arXiv. https://arxiv.org/abs/2503.07988
