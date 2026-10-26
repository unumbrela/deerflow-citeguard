# Systematic Literature Review: Offline Reinforcement Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "offline reinforcement learning", category cs.LG, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review surveys 10 recent arXiv papers on offline reinforcement learning (offline RL) published within the last two years. The surveyed literature reveals a field maturing along multiple dimensions: addressing the fundamental challenge of distributional shift through adaptive conservatism and support constraints, improving data efficiency via augmentation and regularization techniques, and establishing theoretical foundations for generalization and large state spaces. A notable shift is emerging toward viewing offline-trained policies not as final products but as adaptive priors for subsequent online interaction. Collectively, these works demonstrate that offline RL is moving beyond simple conservative Q-learning toward more nuanced approaches that balance robustness with adaptability, particularly important for real-world deployment where dataset coverage is limited and test-time conditions may differ from training.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "offline reinforcement learning", filtered to category cs.LG, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive Conservatism and Distributional Shift

A central challenge in offline RL is handling out-of-distribution (OOD) actions without excessive conservatism that limits performance. Recent work has moved beyond uniform penalties toward state-adaptive approaches. Upadhyay (2026) introduces UNIQ, which uses conformal prediction to estimate uncertainty and applies conservatism only in uncertain regions near the data frontier, achieving roughly 10x memory reduction compared to ensemble methods like EDAC. Similarly, Gao et al. (2025) propose Only Support Constraint (OSC), which restricts policies to the support of the behavior policy without imposing extra constraints on actions within that support, using a diffusion model to characterize the support. Jiang et al. (2026) address OOD mode averaging in flow-based policies through Value-Rectified Distillation (VRD), which actively decouples distinct behavioral modes and isolates high-value actions. These approaches share a common insight: conservatism should be applied selectively and intelligently rather than uniformly across all states.

### Theme 2: Data Efficiency Through Augmentation and Regularization

Many offline RL algorithms struggle when dataset size is limited, a common scenario in real-world applications. Several papers address this through data augmentation and regularization. Schmähling et al. (2026) introduce trajectory-level data augmentation that exploits task structure and geometric relationships between rewards and value functions, enabling training from limited suboptimal trajectories. Arnob et al. (2025) propose Sparse-Reg, a sparsity-based regularization technique that mitigates overfitting in small datasets and outperforms state-of-the-art baselines in continuous control tasks. Cao et al. (2025) present MORAL, which replaces fixed horizon rollout with adversarial data augmentation that dynamically selects ensemble models against the policy, enriching training data without requiring rollout horizon tuning. These methods collectively address the gap between large benchmark datasets and smaller real-world datasets.

### Theme 3: Generalization and Epistemic Robustness

Offline RL systems must generalize to unseen test environments and handle epistemic uncertainty from limited or biased data coverage. Wang et al. (2025) demonstrate that classical offline RL fails to generalize to new environments and propose pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to achieve zero-shot generalization. Chenreddy and Delage (2026) address epistemic uncertainty through a unified framework that replaces discrete ensembles with compact uncertainty sets over Q-values, achieving improved robustness over ensemble-based baselines while avoiding the conflation of epistemic and aleatoric uncertainty. These works emphasize that robustness to distributional shift and epistemic uncertainty are prerequisites for reliable deployment.

### Theme 4: Theoretical Foundations in Large State Spaces

As offline RL moves toward practical applications, theoretical understanding becomes crucial. Jiang and Xie (2025) provide a comprehensive survey of offline RL theory in large state spaces, examining expressivity assumptions (Bellman completeness versus realizability) and data coverage assumptions (all-policy versus single-policy coverage) that significantly impact achievable guarantees. Their work maps the landscape of algorithms depending on assumptions made and desired sample/computational complexity, establishing connections between offline RL and adjacent areas. This theoretical foundation is essential for understanding when and why different algorithms succeed or fail.

### Theme 5: From Static Policies to Adaptive Priors

A conceptual shift is emerging in how offline RL objectives are framed when policies undergo online fine-tuning or test-time adaptation. Ni et al. (2026) formalize adaptive offline reinforcement learning (AORL), arguing that traditional conservative objectives are incomplete when policies will be updated through online interaction. They propose that offline RL should prioritize learning adaptive policy priors that preserve capacity for improvement during subsequent interaction, particularly important under distributional shift and changing test-time conditions. Bayesian offline RL is suggested as a principled approach by preserving epistemic uncertainty over plausible environments. This perspective reframes offline RL not as a final training stage but as preparation for adaptability.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that uniform conservatism is suboptimal—multiple works (Upadhyay, 2026; Gao et al., 2025; Jiang et al., 2026) advocate for selective, state-adaptive approaches to handling distributional shift. There is also broad agreement that data efficiency remains a critical challenge, with multiple approaches (Schmähling et al., 2026; Arnob et al., 2025; Cao et al., 2025) addressing the gap between benchmark datasets and real-world data constraints. The literature converges on the view that epistemic uncertainty from limited coverage is a fundamental challenge requiring explicit treatment (Wang et al., 2025; Chenreddy & Delage, 2026).

**Disagreements**: The surveyed papers do not exhibit direct methodological disagreements, but they represent different philosophical approaches to the offline RL problem. Some works focus on improving existing algorithmic frameworks (UNIQ building on IQL, OSC as a regularization term, VRD for flow-based policies), while others advocate for conceptual reframing (AORL as a new objective). The theoretical survey by Jiang and Xie (2025) presents multiple competing assumptions without resolving which is most appropriate, reflecting ongoing debate in the field about foundational assumptions.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, most papers do not state limitations in their abstracts, suggesting either space constraints or reluctance to highlight weaknesses—a limitation of this review is that deeper critique would require full paper analysis. Second, while multiple papers address data efficiency, none explicitly tackle the challenge of multi-task or multi-domain offline learning, where datasets span diverse tasks. Third, the AORL framework (Ni et al., 2026) is presented as a position paper without empirical validation, leaving open the question of how to practically construct adaptive priors. Fourth, while theoretical foundations are surveyed (Jiang & Xie, 2025), the gap between theory and practice remains—many algorithms with strong guarantees may not scale to real-world complexity. Finally, none of the surveyed papers explicitly address safety constraints or human preference alignment in offline RL, important considerations for deployment in safety-critical domains.

## Per-Paper Annotations

### Arnob et al. (2025)

**Research question**: How can overfitting in offline reinforcement learning be mitigated when working with small datasets?
**Methodology**: The authors introduce Sparse-Reg, a regularization technique based on sparsity designed to mitigate overfitting in offline reinforcement learning and enable effective learning in limited data settings.
**Key findings**:
- Offline RL algorithms can overfit on small datasets, resulting in poor performance.
- Sparse-Reg uses sparsity-based regularization to address overfitting.
- The technique enables effective learning in limited data settings.
- Sparse-Reg outperforms state-of-the-art baselines in continuous control tasks.
- The method addresses the gap between large benchmark datasets and smaller real-world datasets.
**Limitations**: Not stated in abstract.

### Cao et al. (2025)

**Research question**: How can model-based offline RL develop more robust policies from static data without access to new environment interactions?
**Methodology**: The authors introduce MORAL, which replaces fixed horizon rollout with adversarial data augmentation that dynamically selects ensemble models against the policy for biased sampling, integrating a differential factor for regularization.
**Key findings**:
- Existing model-based offline RL approaches struggle to develop robust policies from static data.
- Adversarial data augmentation enriches training data by executing alternating sampling with ensemble models.
- The adversarial process mitigates optimistic estimation of fixed models and robustly expands training data.
- MORAL outperforms other model-based offline RL methods on D4RL benchmarks in policy learning and sample efficiency.
- The approach adapts to diverse offline tasks without rollout horizon tuning.
**Limitations**: Not stated in abstract.

### Chenreddy and Delage (2026)

**Research question**: How can epistemic uncertainty in offline RL be addressed more effectively than ensemble-based methods?
**Methodology**: The authors propose a unified framework that replaces discrete ensembles with compact uncertainty sets over Q-values, and introduce a benchmark for evaluating offline RL algorithms under risk-sensitive behavior policies.
**Key findings**:
- Epistemic uncertainty from limited or biased data coverage leads to inaccurate value estimates and unreliable generalization.
- Ensemble-based methods like SAC-N require large ensembles and conflate epistemic with aleatoric uncertainty.
- The proposed uncertainty set framework achieves improved robustness and generalization over ensemble-based baselines.
- The method is demonstrated across both tabular and continuous state domains.
**Limitations**: Not stated in abstract.

### Gao et al. (2025)

**Research question**: How can policy constraint methods in offline RL reduce excessive conservatism while still addressing distributional shift?
**Methodology**: The authors propose Only Support Constraint (OSC), a regularization term derived from maximizing the total probability of the learned policy within the support of the behavior policy, using a diffusion model to characterize the behavior policy's support.
**Key findings**:
- Current policy constraint methods exhibit excessive conservatism that hinders surpassing behavior policy performance.
- OSC restricts policies to the support without imposing extra constraints on actions within the support.
- A diffusion model effectively characterizes the support of behavior policies.
- OSC significantly enhances performance across offline RL benchmarks by alleviating distributional shift challenges and mitigating conservatism.
**Limitations**: Not stated in abstract.

### Jiang and Xie (2025)

**Research question**: What are the key theoretical concepts, algorithms, and guarantees for offline reinforcement learning in large state spaces?
**Methodology**: This article introduces and surveys the theory of offline RL in large state spaces, describing key concepts including expressivity assumptions on function approximation and data coverage, along with their implications for algorithm design and guarantees.
**Key findings**:
- Expressivity assumptions such as Bellman completeness versus realizability are central to offline RL theory.
- Data coverage assumptions (all-policy vs. single-policy coverage) significantly impact achievable guarantees.
- A rich landscape of algorithms exists depending on the assumptions made and desired sample/computational complexity.
- Important connections exist between offline RL and adjacent areas.
**Limitations**: Not stated in abstract.

### Jiang et al. (2026)

**Research question**: How can Out-of-Distribution (OOD) Mode Averaging be addressed when distilling Flow Matching based behavior policies in offline Reinforcement Learning?
**Methodology**: The authors propose Value-Rectified Distillation (VRD), a framework that reformulates offline policy distillation as a value-guided generative trajectory alignment problem using a dynamic coupling mechanism to decouple distinct behavioral modes. They instantiate VRD through two algorithms: VRD-Q (value-quantile behavior distillation) and VRD-R (latent space reorganization).
**Key findings**:
- VRD actively rectifies flow dynamics to explicitly decouple distinct behavioral modes and isolate high-value actions.
- VRD-Q utilizes value-quantile behavior distillation to statistically filter out low-value behaviors.
- VRD-R reorganizes the latent space to geometrically isolate high-value generative trajectories from the FM-based behavior policy.
- VRD improves existing generative baselines across diverse continuous control and planning tasks on D4RL, OGBench, and Minari benchmarks.
- VRD shows particular improvement on multi-modal, non-expert datasets.
**Limitations**: Not stated in abstract.

### Ni et al. (2026)

**Research question**: How should the objective of offline RL be reformulated when offline-trained policies are subsequently updated through online interaction?
**Methodology**: This position paper formalizes adaptive offline reinforcement learning (AORL) as a conceptual framework, distinguishing it from offline-to-online RL and discussing Bayesian offline RL as a principled direction for constructing adaptive policy priors.
**Key findings**:
- Traditional offline RL's conservative objectives are incomplete when policies undergo online fine-tuning or test-time adaptation.
- Offline RL should prioritize learning adaptive policy priors that preserve capacity for improvement during subsequent interaction.
- Adaptability becomes important under distributional shift, limited dataset coverage, and changing test-time conditions.
- Bayesian offline RL offers a principled approach by preserving epistemic uncertainty over plausible environments.
**Limitations**: As a position paper, it outlines conceptual frameworks and research directions rather than providing empirical validation or algorithmic implementations.

### Schmähling et al. (2026)

**Research question**: How can offline reinforcement learning be trained effectively from a limited number of suboptimal trajectories?
**Methodology**: The authors introduce a trajectory-based augmentation technique that exploits task structure and the geometric relationship between rewards, value functions, and mathematical properties of logging policies, with theoretical justification and empirical validation across positioning tasks.
**Key findings**:
- The augmentation method enables training of off-policy models from limited suboptimal trajectories.
- The approach exploits task structure and geometric relationships between rewards and value functions.
- The augmentation supports suboptimal logging policies during data collection, leading to higher data quality.
- The method improves offline reinforcement learning performance empirically.
- The strategies are validated across positioning tasks of varying dimensionality and under partial observability.
**Limitations**: Not stated in abstract.

### Upadhyay (2026)

**Research question**: How can offline reinforcement learning apply state-adaptive conservatism rather than fixed uniform penalties across all states?
**Methodology**: The authors present UNIQ (Uncertainty-Informed Quantile), built on the Implicit Q-Learning backbone, which trains a multi-expectile value ensemble, computes distribution-free uncertainty estimates using split conformal prediction, and maps the signal to a state-dependent expectile for adaptive conservatism.
**Key findings**:
- UNIQ introduces state-adaptive conservatism through conformally calibrated uncertainty estimation.
- The method relaxes conservatism in well-covered regions while strengthening it in uncertain regions near the data frontier.
- UNIQ consistently improves over IQL on D4RL MuJoCo benchmarks, with largest gains on Walker2d and replay-heavy tasks.
- UNIQ operates at near-IQL memory cost (approximately 250 MB peak VRAM), providing roughly 10x reduction compared to EDAC.
- UNIQ improves the performance-efficiency trade-off in offline reinforcement learning.
**Limitations**: Not stated in abstract.

### Wang et al. (2025)

**Research question**: How can offline reinforcement learning achieve zero-shot generalization to unseen test environments using only offline datasets from different training environments?
**Methodology**: The authors propose pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), which leverage pessimistic policy evaluation to guide policy learning and enhance generalization to new environments.
**Key findings**:
- Classical offline RL fails to generalize to new, unseen environments.
- PERM and PPPO leverage pessimistic policy evaluation to guide policy learning.
- Both PERM and PPPO are capable of finding a near-optimal policy with zero-shot generalization.
- The work provides theoretical understanding of the generalization phenomenon in offline reinforcement learning.
- This represents a first step in understanding the foundation of generalization in offline RL.
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
