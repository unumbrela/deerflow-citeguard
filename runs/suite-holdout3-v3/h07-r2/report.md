# Systematic Literature Review: Offline Reinforcement Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "offline reinforcement learning", category cs.LG, last 2 years (2024-10-26 to 2026-10-26)
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on offline reinforcement learning published between 2025 and 2026. The surveyed literature reveals a field maturing beyond foundational challenges of distributional shift and conservatism toward more nuanced concerns: adaptability for online fine-tuning, uncertainty quantification, sample efficiency in limited-data regimes, and theoretical guarantees for large state spaces. A dominant thread across papers is the recognition that offline RL must balance conservatism with capacity for improvement—whether through adaptive policy priors, state-adaptive uncertainty estimation, or regularization techniques that prevent overfitting without excessive constraint. The literature collectively suggests that offline RL is transitioning from a static deployment paradigm to one that prepares policies for future interaction and adaptation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "offline reinforcement learning", filtered to category cs.LG, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive Conservatism and Uncertainty Calibration

Traditional offline RL algorithms apply uniform conservatism to mitigate distributional shift, but recent work recognizes that this approach is suboptimal when data coverage varies across the state space. Upadhyay (2026) introduces UNIQ, which uses conformal prediction to estimate uncertainty and applies state-adaptive expectiles—relaxing conservatism in well-covered regions while strengthening it in uncertain areas. Similarly, Chenreddy and Delage (2026) propose replacing discrete ensembles with compact uncertainty sets over Q-values to better address epistemic uncertainty without the computational cost of large ensembles. This theme reflects a shift from blanket conservatism toward calibrated, uncertainty-informed policy learning that preserves performance in well-covered regions while remaining cautious elsewhere.

### Theme 2: Policy Constraints and Support Characterization

A second thread focuses on refining policy constraints to reduce excessive conservatism while still mitigating distributional shift. Gao et al. (2025) present Only Support Constraint (OSC), which restricts policies to the support of the behavior policy without imposing extra constraints on actions within that support. Their approach uses diffusion models to characterize the support, enabling policies to exceed behavior performance while avoiding out-of-distribution actions. This work addresses a key limitation of earlier policy constraint methods that hindered improvement beyond the behavior policy by applying overly restrictive penalties.

### Theme 3: Generalization and Zero-Shot Transfer

Several papers address the challenge of generalizing offline RL policies to unseen environments. Wang et al. (2025) propose pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to enhance zero-shot generalization. Their theoretical analysis shows both methods can find near-optimal policies that generalize to new environments—a capability classical offline RL lacks. This theme highlights growing recognition that offline RL must prepare for deployment in conditions that differ from the training data distribution.

### Theme 4: Sample Efficiency and Limited Data Regimes

Practical offline RL often operates with datasets considerably smaller than standard benchmarks, creating overfitting risks. Arnob et al. (2025) introduce Sparse-Reg, a sparsity-based regularization technique that mitigates overfitting in limited-data settings. Their work addresses the gap between benchmark performance and real-world applications where datasets may contain far fewer than a million data points. Similarly, Schmähling et al. (2026) propose trajectory-level data augmentation that enables training from limited suboptimal trajectories by exploiting task structure and geometric relationships between rewards and value functions.

### Theme 5: Offline-to-Online Transition and Adaptive Priors

A position paper by Ni et al. (2026) reframes offline RL as preparation for future online interaction rather than static deployment. They formalize adaptive offline RL (AORL) and argue that offline-trained policies should preserve epistemic uncertainty to enable improvement during subsequent fine-tuning. This perspective shifts the objective from learning a final policy to learning an adaptive prior—a conceptual contribution that influences how we evaluate offline RL methods when online interaction is anticipated.

### Theme 6: Theoretical Foundations for Large State Spaces

Jiang and Xie (2025) provide theoretical foundations for offline RL in large state spaces, mapping the landscape of algorithms based on expressivity assumptions (Bellman completeness vs. realizability) and data coverage requirements (all-policy vs. single-policy coverage). Their work establishes the conditions under which different algorithms achieve sample and computational complexity guarantees, providing a framework for understanding when and why various approaches succeed.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the insight that uniform conservatism is suboptimal. Both Upadhyay (2026) and Chenreddy and Delage (2026) independently argue for uncertainty-aware, adaptive approaches to policy learning. There is also broad agreement that offline RL must address generalization—Wang et al. (2025), Ni et al. (2026), and Schmähling et al. (2026) all emphasize preparing policies for conditions beyond the training distribution.

**Disagreements**: The literature shows tension between model-based and model-free approaches. Cao et al. (2025) advocate for adversarial data augmentation with ensemble models, while Chenreddy and Delage (2026) argue that ensembles conflate epistemic and aleatoric uncertainty and propose compact uncertainty sets instead. Additionally, while Ni et al. (2026) call for preserving uncertainty to enable adaptation, other papers focus on eliminating uncertainty through better regularization or constraint methods.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. First, most papers do not state limitations explicitly in their abstracts, suggesting a need for more transparent discussion of method boundaries. Second, while theoretical guarantees are provided for some methods (Wang et al., 2025; Jiang & Xie, 2025), empirical validation across diverse benchmarks remains limited in several cases. Third, the computational requirements of advanced methods—particularly ensemble-based approaches versus compact uncertainty representations—are not systematically compared. Finally, the transition from offline training to online fine-tuning, while recognized as important (Ni et al., 2026), lacks concrete algorithmic prescriptions in most surveyed work.

## Per-Paper Annotations

### Arnob et al. (2025)

**Research question**: How can offline RL algorithms avoid overfitting when learning from small datasets with considerably fewer than a million data points?
**Methodology**: The authors introduce Sparse-Reg, a regularization technique based on sparsity designed to mitigate overfitting in offline reinforcement learning, enabling effective learning in limited data settings with evaluation in continuous control tasks.
**Key findings**:
- Offline RL algorithms can overfit on small datasets, resulting in poor performance
- Sparse-Reg uses sparsity-based regularization to mitigate overfitting
- The method enables effective learning in limited data settings
- Sparse-Reg outperforms state-of-the-art baselines in continuous control
- Many offline RL applications rely on considerably smaller datasets than common benchmarks
**Limitations**: not stated in abstract

### Cao et al. (2025)

**Research question**: How can model-based offline RL develop robust policies from static data without access to new environment interactions?
**Methodology**: The authors introduce MORAL, which replaces fixed horizon rollout with adversarial data augmentation that executes alternating sampling with ensemble models. A differential factor is integrated for regularization, and the method is evaluated on D4RL benchmarks.
**Key findings**:
- Existing model-based offline RL approaches focus on learning state transitions through ensemble models with conservative estimation
- MORAL employs adversarial data augmentation to dynamically select ensemble models against the policy for biased sampling
- The adversarial process mitigates optimistic estimation of fixed models and robustly expands training data
- A differential factor ensures error minimization in extrapolations
- MORAL outperforms other model-based offline RL methods on D4RL benchmarks in policy learning and sample efficiency
**Limitations**: The abstract does not specify which D4RL tasks were used or provide quantitative performance comparisons.

### Chenreddy and Delage (2026)

**Research question**: How can offline RL better address epistemic uncertainty arising from limited or biased data coverage without relying on large ensembles?
**Methodology**: The authors propose a unified framework that replaces discrete ensembles with compact uncertainty sets over Q-values, and introduce a benchmark for evaluating offline RL algorithms under risk-sensitive behavior policies. The method is evaluated across tabular and continuous state domains.
**Key findings**:
- Epistemic uncertainty from limited or biased data coverage leads to inaccurate value estimates and unreliable generalization
- Ensemble-based methods like SAC-N require large ensembles and conflate epistemic with aleatoric uncertainty
- The proposed framework replaces discrete ensembles with compact uncertainty sets over Q-values
- The method achieves improved robustness and generalization over ensemble-based baselines
- A benchmark for evaluating offline RL under risk-sensitive behavior policies is introduced
**Limitations**: The abstract does not specify the size of uncertainty sets or computational requirements compared to ensemble methods.

### Gao et al. (2025)

**Research question**: How can policy constraint methods in offline RL reduce excessive conservatism while still mitigating distributional shift?
**Methodology**: The authors present Only Support Constraint (OSC), derived from maximizing the total probability of the learned policy in the support of the behavior policy, and utilize a diffusion model to characterize the support of behavior policies. Experimental evaluations are conducted across offline RL benchmarks.
**Key findings**:
- Current policy constraint methods exhibit excessive conservatism that hinders surpassing the behavior policy's performance
- OSC presents a regularization term that restricts policies to the support without imposing extra constraints on actions within the support
- A diffusion model effectively characterizes the support of behavior policies
- OSC significantly enhances performance across offline RL benchmarks
- OSC alleviates challenges associated with distributional shifts and mitigates conservatism of policy constraints
**Limitations**: The abstract does not specify which benchmarks were used or quantify the performance improvements.

### Jiang and Xie (2025)

**Research question**: What are the theoretical foundations, algorithms, and guarantees for offline reinforcement learning in large state spaces?
**Methodology**: This article introduces the theory of offline reinforcement learning in large state spaces by describing key concepts including expressivity assumptions on function approximation and data coverage, and mapping the landscape of algorithms and results based on different assumptions.
**Key findings**:
- Offline RL learns good policies from historical data without online interactions with the environment
- Key theoretical concepts include expressivity assumptions (Bellman completeness vs. realizability) and data coverage (all-policy vs. single-policy coverage)
- A rich landscape of algorithms and results exists depending on assumptions about function approximation and data coverage
- Different assumptions lead to different sample and computational complexity guarantees
- Open questions and connections to adjacent areas are identified
**Limitations**: The abstract does not specify which particular open questions or adjacent areas are discussed.

### Jiang et al. (2026)

**Research question**: How can we address Out-of-Distribution Mode Averaging when distilling Flow Matching based behavior policies in offline Reinforcement Learning?
**Methodology**: The authors propose Value-Rectified Distillation (VRD), a framework that reformulates offline policy distillation as a value-guided generative trajectory alignment problem using dynamic coupling to decouple behavioral modes. They instantiate VRD through two algorithms: VRD-Q (value-quantile behavior distillation) and VRD-R (latent space reorganization), evaluated on D4RL, OGBench, and Minari benchmarks.
**Key findings**:
- VRD resolves OOD Mode Averaging by actively rectifying flow dynamics to decouple distinct behavioral modes
- VRD-Q filters out low-value behaviors through value-quantile behavior distillation
- VRD-R geometrically isolates high-value generative trajectories from the FM-based behavior policy
- VRD improves existing generative baselines across diverse continuous control and planning tasks
- VRD shows especially strong performance on multi-modal, non-expert datasets
**Limitations**: not stated in abstract

### Ni et al. (2026)

**Research question**: How should offline reinforcement learning be reformulated when offline-trained policies are subsequently updated through online interaction?
**Methodology**: This position paper formalizes adaptive offline reinforcement learning (AORL) as a conceptual framework and distinguishes it from offline-to-online RL. It discusses Bayesian offline RL as a principled direction for constructing adaptive policy priors by preserving epistemic uncertainty.
**Key findings**:
- Traditional offline RL's conservative objectives are incomplete when policies undergo online fine-tuning or test-time adaptation
- The objective of offline RL should prioritize learning adaptive policy priors that preserve capacity for improvement during subsequent interaction
- Adaptability becomes important under distributional shift, limited dataset coverage, and changing test-time conditions
- Bayesian offline RL offers a principled approach for constructing adaptive policy priors by preserving epistemic uncertainty over plausible environments
- Offline RL should be treated as preparation for future experience rather than as a static deployment problem
**Limitations**: As a position paper, specific algorithmic implementations or empirical validations are not provided in the abstract.

### Schmähling et al. (2026)

**Research question**: How can data augmentation enable training off-policy models from a limited number of suboptimal trajectories in offline reinforcement learning?
**Methodology**: The authors introduce a trajectory-based augmentation technique that exploits task structure and geometric relationships between rewards, value functions, and mathematical properties of logging policies, with theoretical justification and empirical validation across positioning tasks of varying dimensionality and partial observability.
**Key findings**:
- Trajectory-based augmentation supports suboptimal logging policies during data collection
- The method leads to higher data quality and improved offline RL performance
- The approach enables training from limited suboptimal trajectories
- Theoretical justification is provided for the augmentation strategies
- Empirical validation shows effectiveness across tasks with varying dimensionality and partial observability
**Limitations**: not stated in abstract

### Upadhyay (2026)

**Research question**: How can offline RL apply state-adaptive conservatism rather than fixed uniform penalties to better mitigate distribution shift?
**Methodology**: The authors present UNIQ (Uncertainty-Informed Quantile), built on IQL, which trains a multi-expectile value ensemble, computes distribution-free uncertainty estimates using split conformal prediction, and maps uncertainty to state-dependent expectiles that adjust conservatism based on local data coverage.
**Key findings**:
- UNIQ introduces state-adaptive conservatism through conformally calibrated uncertainty estimation
- The method relaxes conservatism in well-covered regions while strengthening it in uncertain regions
- UNIQ consistently improves over IQL on D4RL MuJoCo benchmarks, especially on Walker2d and replay-heavy tasks
- UNIQ operates at near-IQL memory cost (~250 MB peak VRAM), approximately 10x reduction compared to EDAC
- UNIQ improves the performance-efficiency trade-off in offline reinforcement learning
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can offline reinforcement learning achieve zero-shot generalization to unseen test environments using offline datasets from different training environments?
**Methodology**: The authors propose two methods: pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to guide policy learning and enhance generalization, with theoretical analysis showing both can find near-optimal policies with zero-shot generalization.
**Key findings**:
- Classical offline RL fails to generalize to new, unseen environments
- PERM and PPPO use pessimistic policy evaluation to enhance generalization
- Both methods are capable of finding near-optimal policies with zero-shot generalization
- This work provides theoretical foundation for understanding generalization in offline RL
- The approach leverages offline datasets including experiences from different environments
**Limitations**: not stated in abstract

## References

Arnob, S. Y., Fujimoto, S., & Precup, D. (2025). Sparse-Reg: Improving sample complexity in offline reinforcement learning using sparsity. arXiv. https://arxiv.org/abs/2506.17155

Cao, H., Feng, F., Huo, J., Yang, S., Fang, M., Yang, T., & Gao, Y. (2025). Model-based offline reinforcement learning with adversarial data augmentation. arXiv. https://arxiv.org/abs/2503.20285

Chenreddy, A. R., & Delage, E. (2026). Epistemic robust offline reinforcement learning. arXiv. https://arxiv.org/abs/2604.07072

Gao, Y., Guo, J., Wu, F., & Zhang, R. (2025). Policy constraint by only support constraint for offline reinforcement learning. arXiv. https://arxiv.org/abs/2503.05207

Jiang, K., Jiang, W., Kawahara, Y., & Tan, X. (2026). Value-rectified distillation for flow-based offline reinforcement learning. arXiv. https://arxiv.org/abs/2610.29075

Jiang, N., & Xie, T. (2025). Offline reinforcement learning in large state spaces: Algorithms and guarantees. arXiv. https://arxiv.org/abs/2510.04088

Ni, T., Jain, V., Karthikeyan, A., & Bacon, P.-L. (2026). From static policies to adaptive priors in offline reinforcement learning. arXiv. https://arxiv.org/abs/2609.35880

Schmähling, T., Burkhardt, M., & Windisch, T. (2026). Trajectory-level data augmentation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2605.13401

Upadhyay, A. (2026). UNIQ: Conformal calibration for adaptive conservatism in offline reinforcement learning. arXiv. https://arxiv.org/abs/2606.07592

Wang, Z., Yang, C., Lui, J. C. S., & Zhou, D. (2025). Provable zero-shot generalization in offline reinforcement learning. arXiv. https://arxiv.org/abs/2503.07988
