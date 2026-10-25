# Systematic Literature Review: Offline Reinforcement Learning

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "offline reinforcement learning", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on offline reinforcement learning (offline RL) published within the last two years. The surveyed literature reveals a field grappling with fundamental challenges around distributional shift, data coverage limitations, and the tension between conservatism and performance. Recent work has focused on developing adaptive mechanisms that adjust conservatism based on uncertainty, improving sample efficiency through regularization and data augmentation, and rethinking offline RL objectives to enable online adaptation. A notable trend is the shift from static policy learning toward adaptive priors that preserve capacity for improvement during subsequent interaction. The field demonstrates strong theoretical grounding with multiple papers providing formal guarantees, while also advancing practical algorithms that achieve state-of-the-art performance on standard benchmarks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "offline reinforcement learning", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive Conservatism and Uncertainty Calibration

A prominent research direction focuses on developing state-adaptive conservatism mechanisms rather than applying uniform penalties across all states. Traditional offline RL methods often employ fixed conservative penalties to avoid out-of-distribution actions, but this approach can be overly restrictive in well-covered regions while insufficiently cautious near data frontiers. Upadhyay (2026) introduced UNIQ, which uses conformal prediction to generate distribution-free uncertainty estimates and maps them to state-dependent expectiles that dynamically adjust conservatism. Similarly, Chenreddy and Delage (2026) proposed replacing discrete ensembles with compact uncertainty sets over Q-values to better handle epistemic uncertainty arising from limited or biased data coverage. These approaches share the insight that uncertainty is heterogeneous across the state space and that conservatism should be calibrated accordingly.

### Theme 2: Data Augmentation and Sample Efficiency

Multiple papers address the challenge of learning effectively from limited or suboptimal datasets through data augmentation and regularization techniques. Schmähling et al. (2026) developed trajectory-level data augmentation that exploits task structure and geometric relationships between rewards and value functions, enabling effective training from limited suboptimal trajectories. Cao et al. (2025) introduced MORAL, which replaces fixed horizon rollout with adversarial data augmentation that dynamically selects ensemble models against the policy for biased sampling. Arnob et al. (2025) proposed Sparse-Reg, a sparsity-based regularization technique designed to mitigate overfitting in small datasets. These methods share the goal of maximizing information extraction from static datasets while avoiding the optimistic bias that plagues model-based approaches.

### Theme 3: Distributional Shift and Policy Constraints

Managing distributional shift between the learned policy and the behavior policy remains a central challenge in offline RL. Gao et al. (2025) presented Only Support Constraint (OSC), which restricts policies to the support of the behavior policy without imposing extra constraints on actions within that support, reducing excessive conservatism while mitigating distributional shift. Jiang et al. (2026) addressed the Out-of-Distribution Mode Averaging problem in flow-based offline RL through Value-Rectified Distillation, which reformulates policy distillation as value-guided generative trajectory alignment. These approaches recognize that the key issue is not simply staying close to the behavior policy, but rather understanding and respecting the structure of the data distribution.

### Theme 4: Generalization and Adaptability

Recent work has begun to reconsider offline RL objectives beyond immediate deployment performance, emphasizing generalization and adaptability. Wang et al. (2025) tackled zero-shot generalization to unseen test environments through pessimistic empirical risk minimization and pessimistic proximal policy optimization, providing theoretical guarantees for finding near-optimal policies that generalize. Ni et al. (2026) argued in a position paper that offline RL should prioritize learning adaptive policy priors rather than static policies, preserving capacity for improvement through memory, exploration, and self-correction during subsequent online interaction. This represents a conceptual shift from viewing offline RL as a standalone solution to viewing it as a foundation for later adaptation.

### Theme 5: Theoretical Foundations and Guarantees

The field continues to develop rigorous theoretical foundations for offline RL in challenging settings. Jiang and Xie (2025) provided a comprehensive analysis of offline RL in large state spaces, examining how different assumptions on function approximation (Bellman completeness vs. realizability) and data coverage (all-policy vs. single-policy coverage) lead to different algorithmic approaches and theoretical guarantees. This work maps the landscape of possible algorithms based on the assumptions one is willing to make and the sample and computational complexity guarantees desired. Such theoretical work provides essential guidance for algorithm design and helps clarify the fundamental limits of offline RL.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. First, there is broad agreement that fixed, uniform conservatism is suboptimal — multiple papers demonstrate that adaptive, state-dependent mechanisms yield better performance (Upadhyay, 2026; Chenreddy & Delage, 2026). Second, the literature consistently shows that distributional shift remains a fundamental challenge that cannot be ignored, and that successful methods must explicitly account for the gap between training and deployment distributions (Gao et al., 2025; Jiang et al., 2026). Third, there is consensus that offline RL algorithms must be evaluated not just on standard benchmarks but also on their ability to generalize to new environments and adapt through online interaction (Wang et al., 2025; Ni et al., 2026).

**Disagreements**: Some tensions exist in the literature regarding the appropriate balance between model-based and model-free approaches. While Cao et al. (2025) advocate for adversarial model-based methods that actively select models against the policy, other work emphasizes the risks of model bias and prefers model-free approaches with careful policy constraints. Additionally, there is ongoing debate about whether offline RL should optimize for immediate deployment performance or for adaptability during subsequent online interaction — Ni et al. (2026) argue for the latter, but most algorithmic work continues to focus on the former.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, most papers do not explicitly state limitations of their proposed approaches in their abstracts, suggesting a need for more transparent discussion of failure modes and boundary conditions. Second, while several papers address sample efficiency, there is limited work on computational efficiency — only Upadhyay (2026) explicitly reports memory requirements, indicating a gap in practical deployment considerations. Third, the literature focuses heavily on continuous control benchmarks (D4RL, OGBench, Minari), with limited exploration of discrete action spaces or combinatorial domains. Fourth, while Ni et al. (2026) advocate for adaptive priors, there is limited empirical work demonstrating how to effectively construct and use such priors in practice. Finally, Jiang and Xie (2025) note unresolved theoretical questions about the interplay between function approximation assumptions and data coverage, suggesting foundational work remains to be done.

## Per-Paper Annotations

### Arnob et al. (2025)

**Research question**: How can offline reinforcement learning algorithms overcome overfitting when trained on small datasets with considerably fewer data points than typical benchmarks?

**Methodology**: The authors introduce Sparse-Reg, a regularization technique based on sparsity designed to mitigate overfitting in offline reinforcement learning, evaluated in limited data settings for continuous control tasks.

**Key findings**:
- Offline RL algorithms can overfit on small datasets, resulting in poor performance
- Sparse-Reg uses sparsity-based regularization to mitigate overfitting
- The method enables effective learning in limited data settings
- Sparse-Reg outperforms state-of-the-art baselines in continuous control

**Limitations**: Not stated in abstract.

### Cao et al. (2025)

**Research question**: How can model-based offline RL develop robust policies when static data prevents agents from accessing the environment to gather new data?

**Methodology**: The authors introduce MORAL, which replaces fixed horizon rollout with adversarial data augmentation that dynamically selects ensemble models against the policy for biased sampling, integrating a differential factor for regularization.

**Key findings**:
- MORAL employs adversarial data augmentation to execute alternating sampling with ensemble models to enrich training data
- The adversarial process dynamically selects ensemble models against policy for biased sampling, mitigating optimistic estimation of fixed models
- A differential factor is integrated into the adversarial process for regularization, ensuring error minimization in extrapolations
- MORAL adapts to diverse offline tasks without rollout horizon tuning, showing remarkable applicability
- Extensive experiments on D4RL benchmark demonstrate MORAL outperforms other model-based offline RL methods in policy learning and sample efficiency

**Limitations**: Not stated in abstract.

### Chenreddy and Delage (2026)

**Research question**: How can offline RL methods better handle epistemic uncertainty arising from limited or biased data coverage?

**Methodology**: The authors propose a unified framework that replaces discrete ensembles with compact uncertainty sets over Q-values, introducing a benchmark for evaluating offline RL algorithms under risk-sensitive behavior policies.

**Key findings**:
- Epistemic uncertainty arises from limited or biased data coverage, particularly when the behavior policy systematically avoids certain actions
- Ensemble-based methods like SAC-N require large ensembles and often conflate epistemic with aleatoric uncertainty
- The proposed method achieves improved robustness and generalization over ensemble-based baselines across both tabular and continuous state domains

**Limitations**: Not stated in abstract.

### Gao et al. (2025)

**Research question**: How can policy constraint methods in offline RL reduce excessive conservatism while mitigating distributional shift?

**Methodology**: The authors present Only Support Constraint (OSC), derived from maximizing the total probability of learned policy in the support of behavior policy, and utilize a diffusion model to characterize the support of behavior policies.

**Key findings**:
- OSC presents a regularization term that only restricts policies to the support without imposing extra constraints on actions within the support
- Current policy constraint methods tend to exhibit excessive conservatism, hindering the policy from surpassing the behavior policy's performance
- OSC significantly enhances performance across offline RL benchmarks by alleviating distributional shift challenges and mitigating conservatism
- A diffusion model effectively characterizes the support of behavior policies to fully harness the performance of the new policy constraints

**Limitations**: Not stated in abstract.

### Jiang and Xie (2025)

**Research question**: What are the theoretical foundations, algorithms, and guarantees for offline reinforcement learning in large state spaces?

**Methodology**: This article introduces the theory of offline RL in large state spaces by analyzing expressivity assumptions on function approximation (Bellman completeness vs. realizability) and data coverage (all-policy vs. single-policy coverage).

**Key findings**:
- Offline RL learns good policies from historical data without online interactions with the environment
- Different assumptions on function approximation and data coverage lead to different algorithmic approaches and theoretical guarantees
- A rich landscape of algorithms exists depending on the assumptions one is willing to make and the sample and computational complexity guarantees desired

**Limitations**: The article discusses open questions and connections to adjacent areas, indicating unresolved theoretical challenges.

### Jiang et al. (2026)

**Research question**: How can we address the Out-of-Distribution (OOD) Mode Averaging problem that occurs when distilling Flow Matching based behavior policies in offline Reinforcement Learning?

**Methodology**: The authors propose Value-Rectified Distillation (VRD), a framework that reformulates offline policy distillation as a value-guided generative trajectory alignment problem using a dynamic coupling mechanism to decouple distinct behavioral modes, instantiated through VRD-Q (value-quantile behavior distillation) and VRD-R (latent space reorganization).

**Key findings**:
- VRD actively rectifies flow dynamics to explicitly decouple distinct behavioral modes and isolate high-value actions
- VRD-Q utilizes value-quantile behavior distillation to statistically filter out low-value behaviors
- VRD-R reorganizes the latent space to geometrically isolate high-value generative trajectories
- VRD improves existing generative baselines across diverse continuous control and planning tasks on D4RL, OGBench, and Minari benchmarks
- VRD shows particular improvement on multi-modal, non-expert datasets

**Limitations**: Not stated in abstract.

### Ni et al. (2026)

**Research question**: How should offline RL objectives change when offline-trained policies are subsequently updated through online interaction?

**Methodology**: This position paper formalizes adaptive offline reinforcement learning (AORL) and distinguishes it from offline-to-online RL, discussing Bayesian offline RL as a direction for constructing adaptive policy priors by preserving epistemic uncertainty.

**Key findings**:
- Offline RL should prioritize learning adaptive policy priors rather than static policies for immediate deployment
- Adaptive policy priors preserve capacity to improve during subsequent interaction through memory, exploration, and self-correction
- Adaptability becomes important under distributional shift, limited dataset coverage, and changing test-time conditions
- Bayesian offline RL offers a principled direction for constructing adaptive policy priors by preserving epistemic uncertainty over plausible environments

**Limitations**: As a position paper, it outlines connections, open challenges, and research directions rather than providing empirical validation.

### Schmähling et al. (2026)

**Research question**: How can data augmentation methods enable effective training of off-policy models from limited suboptimal trajectories in offline reinforcement learning?

**Methodology**: The authors introduce a trajectory-based augmentation technique that exploits task structure and geometric relationships between rewards, value functions, and mathematical properties of logging policies, providing theoretical justification and empirical validation across positioning tasks of varying dimensionality and under partial observability.

**Key findings**:
- The trajectory-based augmentation technique supports suboptimal logging policies during data collection
- The approach leads to higher data quality and improved offline reinforcement learning performance
- The method enables training from a limited number of suboptimal trajectories
- The approach is validated across positioning tasks with varying dimensionality and partial observability

**Limitations**: Not stated in abstract.

### Upadhyay (2026)

**Research question**: How can offline reinforcement learning methods apply state-adaptive conservatism rather than fixed uniform penalties across all states?

**Methodology**: The authors present UNIQ (Uncertainty-Informed Quantile), built on the Implicit Q-Learning backbone, which trains a multi-expectile value ensemble, computes distribution-free uncertainty estimates using split conformal prediction, and maps the resulting signal to a state-dependent expectile that adjusts conservatism based on local data coverage.

**Key findings**:
- UNIQ introduces state-adaptive conservatism through conformally calibrated uncertainty estimation
- The method relaxes conservatism in well-covered regions while strengthening it in uncertain regions near the data frontier
- UNIQ consistently improves over IQL on D4RL MuJoCo benchmarks, with largest gains on Walker2d and replay-heavy tasks
- UNIQ operates at approximately 250 MB peak VRAM, providing roughly 10x memory reduction compared to EDAC
- UNIQ provides a practical mechanism that improves the performance-efficiency trade-off in offline reinforcement learning

**Limitations**: Not stated in abstract.

### Wang et al. (2025)

**Research question**: How can offline reinforcement learning achieve zero-shot generalization to unseen test environments when trained on experiences from different training environments?

**Methodology**: The authors propose two methods: pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to guide policy learning and enhance generalization, providing theoretical analysis showing both methods can find near-optimal policies with zero-shot generalization.

**Key findings**:
- Classical offline RL fails to generalize to new, unseen environments
- PERM and PPPO leverage pessimistic policy evaluation to guide policy learning
- Both PERM and PPPO are capable of finding a near-optimal policy with zero-shot generalization
- The work provides foundational understanding of the generalization phenomenon in offline reinforcement learning

**Limitations**: Not stated in abstract.

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
