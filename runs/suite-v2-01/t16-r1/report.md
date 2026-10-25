# Systematic Literature Review: Reinforcement Learning from Human Feedback

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "RLHF", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on Reinforcement Learning from Human Feedback (RLHF) published between late 2024 and 2026. The surveyed literature reveals a field maturing beyond foundational alignment methods, with researchers now addressing critical challenges in scalability, efficiency, robustness, and fairness. Key developments include theoretical advances in understanding KL-regularization effects, practical innovations in training acceleration and system design, security concerns around adversarial manipulation of RLHF platforms, and methodological improvements for handling diverse human preferences. Collectively, these papers demonstrate that RLHF research has evolved from proving feasibility to optimizing real-world deployment while grappling with fundamental questions about alignment quality, generalization, and vulnerability to adversarial attacks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "RLHF", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Training Efficiency and Acceleration

A prominent research direction focuses on making RLHF training faster and more computationally efficient. Yang et al. (2025) demonstrate that higher reward variance in the initial policy leads to faster training convergence, proposing an O(n log n) algorithm to increase reward variance while preserving preferences. Their GRPOVI method significantly improves training efficiency compared to standard GRPO. Similarly, Wu et al. (2025) address system-level scalability with G-Core, a framework featuring parallel controller programming and dynamic resource placement that reduces hardware idle time and adapts to variable training workloads. These works reflect a shift from purely algorithmic improvements to holistic system optimization for production-scale RLHF deployment.

### Theme 2: Theoretical Foundations and Generalization Bounds

Several papers establish rigorous theoretical frameworks for understanding RLHF behavior. Zhao et al. (2024) provide sharp analysis showing that KL-regularization achieves O(1/ε) sample complexity when ε is sufficiently small, substantially improving upon the O(1/ε²) complexity without regularization. Oko et al. (2026) revisit distortion in AI alignment, demonstrating that exponential degradation is not fundamental to RLHF but results from distribution mismatch between preference data and the KL reference policy. Tang et al. (2026) develop generalization theory accounting for reward shift and clipped KL regularization, identifying three error sources: sampling error, reward shift error, and KL clipping error. These theoretical contributions provide mathematical grounding for practical design choices in RLHF systems.

### Theme 3: Handling Diverse Human Preferences

Moving beyond uniform reward models, researchers are developing methods to capture preference diversity across populations. Mukherjee et al. (2025) introduce SharedRep-RLHF, which learns shared traits among annotation groups rather than separate reward models, achieving up to 20% gain in win rate compared to MaxMin-RLHF. This approach addresses the limitation that uniform-reward RLHF fails to capture diversity and favors dominant groups, while MaxMin-RLHF performs poorly when the minimum-reward group is a minority. The work represents a shift toward more nuanced models of human preference that acknowledge heterogeneity rather than assuming a single reward function.

### Theme 4: Security and Adversarial Vulnerabilities

As RLHF platforms become publicly accessible, security concerns emerge. Entezami and Naseh (2025) demonstrate that adversarial RLHF platforms can selectively manipulate preference datasets to corrupt reward models and misalign language models during fine-tuning. This attack vector is particularly concerning because RLHF platforms enable users to fine-tune models without requiring expertise in complex machine learning algorithms, potentially allowing bad actors to steer LLMs toward undesirable behaviors within targeted domains. This work highlights the need for robust verification and validation mechanisms in RLHF infrastructure.

### Theme 5: Iterated RLHF and Reward Model Overoptimization

Understanding long-term dynamics of repeated RLHF cycles is critical for production systems. Wolf et al. (2025) present the first comprehensive study of reward model overoptimization in iterated RLHF, finding that overoptimization tends to decrease over successive iterations as reward models increasingly approximate ground-truth preferences, though performance gains diminish over time. They observe that reinitializing from the base policy is robust but limits optimization flexibility, while other initialization strategies often fail to recover from early overoptimization. This work provides practical guidance for multi-round RLHF deployment.

### Theme 6: Novel Signals and Unified Frameworks

Researchers are exploring alternative information sources and conceptual unifications. Galliamov et al. (2025) enhance RLHF with human gaze modeling, using gaze-aware reward models and gaze-based distribution of sparse rewards at the token level to achieve faster convergence while maintaining or improving performance. Xiao et al. (2025) establish a theoretical connection revealing that RLHF implicitly performs imitation learning on the preference data distribution, proposing DIL as a unified framework that encompasses existing alignment algorithms as special cases and outperforms them on various benchmarks. These works expand both the input modalities and conceptual foundations of RLHF.

## Convergences and Disagreements

**Convergences**: Multiple papers agree that KL-regularization plays a critical role in RLHF performance and sample complexity (Zhao et al., 2024; Tang et al., 2026; Oko et al., 2026). There is consensus that distribution mismatch between preference data generation and the reference policy creates fundamental challenges (Oko et al., 2026; Tang et al., 2026). Several works converge on the importance of moving beyond uniform reward models to capture preference diversity (Mukherjee et al., 2025; Wolf et al., 2025). The literature also agrees that RLHF training efficiency requires both algorithmic and system-level innovations (Yang et al., 2025; Wu et al., 2025).

**Disagreements**: While Wolf et al. (2025) find that overoptimization decreases over iterations, they note tension between robust initialization strategies (reinitializing from base policy) and optimization flexibility, suggesting different priorities for different use cases. Mukherjee et al. (2025) critique MaxMin-RLHF as suboptimal for learning shared traits, while earlier work treated it as a viable approach for fairness—indicating evolving understanding of fairness objectives in RLHF. The theoretical analyses differ in their assumptions: Zhao et al. (2024) assume sufficient coverage from the reference policy, while Tang et al. (2026) explicitly model reward shift and KL clipping effects, suggesting different regimes of applicability.

## Gaps and Open Questions

Several limitations recur across the surveyed literature. Most papers do not explicitly state experimental constraints or deployment limitations in their abstracts, making it difficult to assess practical applicability. Wolf et al. (2025) note their study uses the controlled AlpacaFarm benchmark, which may not fully represent real-world RLHF deployment scenarios—a limitation echoed implicitly in other theoretical works that lack empirical validation at scale. The security analysis by Entezami and Naseh (2025) raises questions about defensive mechanisms that remain unaddressed in the current literature. Several papers acknowledge distribution mismatch as a fundamental challenge (Oko et al., 2026; Tang et al., 2026) but do not provide complete solutions for mitigating it in practice. The gaze-based approach by Galliamov et al. (2025) requires specialized human data that may not be available in many RLHF applications, limiting its generalizability. Finally, while theoretical works provide bounds and guarantees, the connection between these theoretical results and practical hyperparameter selection remains underexplored.

## Per-Paper Annotations

### Entezami and Naseh (2025)

**Research question**: How vulnerable are publicly available RLHF platforms to adversarial attacks that could manipulate the alignment process of large language models?
**Methodology**: The authors present an attack targeting publicly available RLHF tools where an adversarial RLHF platform selectively manipulates data samples in the preference dataset, demonstrating how this manipulation corrupts the reward model and leads to LLM misalignment during fine-tuning.
**Key findings**:
- RLHF platforms enable users to fine-tune models without requiring expertise in complex machine learning algorithms
- An adversarial RLHF platform can corrupt the LLM alignment process by selectively manipulating preference dataset samples
- The manipulation results in a corrupted reward model that leads to misalignment of the language model
- The attack can effectively steer LLMs toward undesirable behaviors within targeted domains
**Limitations**: The abstract does not explicitly state limitations of the study or attack methodology.

### Yang et al. (2025)

**Research question**: How can RLHF training efficiency be improved by leveraging the relationship between reward variance and training speed?
**Methodology**: The authors propose a practical reward adjustment model that provably increases reward variance while preserving relative preferences and reward expectation, designing a novel O(n log n) algorithm to solve the nonconvex optimization problem and integrating it into the GRPO algorithm to create GRPOVI.
**Key findings**:
- Higher reward variance of the initial policy model leads to faster RLHF training
- The reward adjustment method poses a nonconvex optimization problem that is NP-hard to solve in general
- The proposed O(n log n) algorithm finds a global solution by characterizing extreme points of the feasible set
- GRPOVI significantly improves RLHF training efficiency compared to the original GRPO algorithm
- The work provides an indirect explanation for the effectiveness of GRPO with rule-based reward as demonstrated in DeepSeek-R1
**Limitations**: The abstract does not explicitly state limitations of the proposed approach or experimental constraints.

### Mukherjee et al. (2025)

**Research question**: How can RLHF better capture diverse preferences across sub-populations while avoiding the limitations of existing group-specific approaches?
**Methodology**: The authors introduce SharedRep-RLHF, a framework that learns and leverages shared traits in annotations among various groups rather than learning separate reward models across groups, showing that MaxMin-RLHF is provably suboptimal in learning shared traits and quantifying the sample complexity of their approach.
**Key findings**:
- Uniform-reward RLHF fails to capture diversity of opinions across sub-populations and favors dominant groups
- MaxMin-RLHF has poor performance when the minimum-reward group is a minority
- SharedRep-RLHF learns shared traits in annotations among various groups instead of separate reward models
- MaxMin-RLHF is provably suboptimal in learning shared traits
- SharedRep-RLHF achieves up to 20% gain in win rate compared to MaxMin-RLHF across diverse natural language tasks
**Limitations**: The abstract does not explicitly state limitations of the SharedRep-RLHF approach or experimental constraints.

### Xiao et al. (2025)

**Research question**: What is the theoretical relationship between imitation learning and reinforcement learning from human feedback in the context of LLM alignment?
**Methodology**: The authors establish a theoretical connection between RLHF and imitation learning, revealing that RLHF implicitly performs imitation learning on the preference data distribution, and propose DIL, a principled framework that directly optimizes the imitation learning objective and encompasses existing alignment algorithms as special cases.
**Key findings**:
- RLHF implicitly performs imitation learning on the preference data distribution
- DIL provides a unified imitation learning perspective on alignment encompassing existing algorithms
- DIL naturally introduces new variants of alignment algorithms
- DIL outperforms existing methods on various challenging benchmarks
**Limitations**: The abstract does not explicitly state limitations of the theoretical framework or experimental scope.

### Wolf et al. (2025)

**Research question**: How does reward model overoptimization behave in iterated RLHF settings, and what design choices affect its dynamics?
**Methodology**: The authors present the first comprehensive study of overoptimization in iterated RLHF, systematically analyzing key design choices including reward model training data transfer across iterations, which reward function is used for optimization, and how policies are initialized, using the controlled AlpacaFarm benchmark.
**Key findings**:
- RLHF often suffers from reward model overoptimization where models overfit to the reward function
- Overoptimization tends to decrease over successive iterations as reward models increasingly approximate ground-truth preferences
- Performance gains diminish over time in iterated RLHF
- Reinitializing from the base policy is robust but limits optimization flexibility
- Other initialization strategies often fail to recover from early overoptimization
**Limitations**: The study uses the controlled AlpacaFarm benchmark, which may not fully represent real-world RLHF deployment scenarios.

### Galliamov et al. (2025)

**Research question**: Can human gaze modeling enhance RLHF efficiency by reducing computational costs while maintaining or improving performance?
**Methodology**: The authors explore two approaches: (1) gaze-aware reward models and (2) gaze-based distribution of sparse rewards at token level, conducting experiments comparing gaze-informed RLHF against standard RLHF.
**Key findings**:
- Gaze-informed RLHF achieves faster convergence compared to standard RLHF
- The approach maintains or slightly improves performance while reducing computational costs
- Human gaze provides a valuable and underused signal for policy optimization
**Limitations**: Not stated in abstract.

### Zhao et al. (2024)

**Research question**: What is the fundamental distinction between policy learning objectives with KL-regularization versus without KL-regularization in terms of sample complexity?
**Methodology**: The authors provide theoretical analysis of KL-regularized contextual bandits and RLHF, examining sample complexity and exploring the role of data coverage through a two-stage mixed sampling strategy.
**Key findings**:
- KL-regularization achieves O(1/ε) sample complexity when ε is sufficiently small, improving upon the O(1/ε²) complexity without KL-regularization
- With sufficient coverage from the reference policy, a simple two-stage mixed sampling strategy achieves sample complexity with only additive dependence on the coverage coefficient
- The analysis reveals the power of KL-regularization without requiring explicit exploration or additional structural assumptions on the reward function class
**Limitations**: Not stated in abstract.

### Oko et al. (2026)

**Research question**: Is the exponential distortion in RLHF a fundamental property of the algorithm or a consequence of distribution mismatch between preference data and the KL reference policy?
**Methodology**: The authors present a fine-grained analysis of RLHF distortion with reward clipping, establishing tight upper and lower bounds on distortion across multiple regimes of KL regularization strength under the Bradley-Terry model.
**Key findings**:
- Exponential degradation in distortion is not a fundamental property of RLHF but results from distribution mismatch between preference data generation and KL reference policy
- Under the Bradley-Terry model, distortion is Θ̃(βB + β) where B is the log density ratio bound between data distribution and reference policy
- When there is no distribution mismatch, RLHF achieves optimal distortion of O(β) up to a constant
**Limitations**: Not stated in abstract.

### Tang et al. (2026)

**Research question**: How do reward shift and clipped KL regularization affect the generalisability of RLHF when reward models are trained on preference data from earlier policies?
**Methodology**: The authors develop generalization theory for RLHF accounting for reward shift and clipped KL regularization, presenting generalization bounds and analyzing special cases including uniform prior initialization and stochastic gradient descent training.
**Key findings**:
- Generalization error in RLHF stems from three sources: sampling error from prompts and rollouts, reward shift error, and KL clipping error
- The theory yields practical implications for optimal KL clipping threshold selection
- The framework provides guidance for budget allocation in prompts, rollouts, and preference data
**Limitations**: Not stated in abstract.

### Wu et al. (2025)

**Research question**: How can RLHF training systems be improved to scale to multi-modal and diffusion workflows while adapting to dynamic workloads?
**Methodology**: The authors present G-Core, a framework featuring a parallel controller programming model for flexible orchestration and a dynamic placement schema that adaptively partitions resources and schedules workloads.
**Key findings**:
- G-Core's parallel controller model enables flexible orchestration of complex RLHF workflows without centralized controller bottlenecks
- The dynamic placement schema significantly reduces hardware idle time and improves utilization under variable training conditions
- G-Core has been successfully deployed to train models supporting WeChat product features serving a large-scale user base
**Limitations**: Not stated in abstract.

## References

Entezami, E., & Naseh, A. (2025). LLM misalignment via adversarial RLHF platforms. arXiv. https://arxiv.org/abs/2503.03039

Galliamov, K., Titov, I., & Pershin, I. (2025). Enhancing RLHF with human gaze modeling. arXiv. https://arxiv.org/abs/2507.09016

Mukherjee, A., Bullo, M., & Gündüz, D. (2025). SharedRep-RLHF: A shared representation approach to RLHF with diverse preferences. arXiv. https://arxiv.org/abs/2509.03672

Oko, K., Ulichney, A., Haghtalab, N., & Bao, H. (2026). Distortion of AI alignment revisited: RLHF is a decent utilitarian aligner. arXiv. https://arxiv.org/abs/2609.12651

Tang, K., Chen, Y., & He, F. (2026). Generalisation of RLHF under reward shift and clipped KL regularisation. arXiv. https://arxiv.org/abs/2602.21765

Wolf, L., Kirk, R., & Musolesi, M. (2025). Reward model overoptimisation in iterated RLHF. arXiv. https://arxiv.org/abs/2505.18126

Wu, J., Chang, W., Liu, X., He, G., Hong, H., Liu, B., Tian, H., Yang, T., Shi, Y., Lin, F., & Yao, T. (2025). G-Core: A simple, scalable and balanced RLHF trainer. arXiv. https://arxiv.org/abs/2507.22789

Xiao, T., Yuan, Y., Li, M., Chen, Z., & Honavar, V. G. (2025). On a connection between imitation learning and RLHF. arXiv. https://arxiv.org/abs/2503.05079

Yang, Z., Gu, Z., Qi, H., & Yuan, Y. (2025). Accelerating RLHF training with reward variance increase. arXiv. https://arxiv.org/abs/2505.23247

Zhao, H., Ye, C., Gu, Q., & Zhang, T. (2024). Sharp analysis for KL-regularized contextual bandits and RLHF. arXiv. https://arxiv.org/abs/2411.04625
