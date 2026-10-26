# Systematic Literature Review: Offline Reinforcement Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "offline reinforcement learning" in cs.LG, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The offline reinforcement learning field has matured significantly over the past two years, with research focusing on addressing fundamental challenges in distribution shift, data efficiency, and safe deployment. The surveyed papers reveal three dominant research directions: improving policy learning through advanced distillation and regularization techniques, enhancing representation learning through causal and attention-based methods, and developing robust evaluation frameworks for real-world deployment. Recent work demonstrates particular progress in handling multi-modal behavioral data, quantifying uncertainty for safety-critical applications, and bridging the gap between simulated benchmarks and practical deployment scenarios. The field is increasingly moving toward hierarchical skill discovery and multi-task learning to improve sample efficiency and generalization across domains.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "offline reinforcement learning", filtered to category cs.LG, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Distribution Shift and OOD Generalization

A central challenge in offline RL remains the distributional shift between the behavior policy that generated the dataset and the learned policy. Recent work has tackled this through multiple complementary approaches. Jiang et al. (2026) address the Out-of-Distribution (OOD) Mode Averaging problem in flow-based policy distillation, where standard methods interpolate across behavioral modes causing action collapse. Their Value-Rectified Distillation framework uses dynamic coupling to decouple distinct modes and isolate high-value actions. Similarly, Rodriguez et al. (2026) propose causal representation learning to disentangle invariant causal factors from spurious correlations, enabling policies to focus on task-relevant features while ignoring environment-specific confounders. This causal approach provides theoretical grounding for why certain representations generalize better across domain shifts. The convergence on representation-level solutions suggests the field is moving beyond simple conservatism constraints toward more principled approaches that explicitly model what should and should not transfer from the offline dataset.

### Theme 2: Data Augmentation and Enhancement

Limited data coverage remains a fundamental bottleneck in offline RL, prompting innovative augmentation strategies. Schmähling et al. (2026) introduce trajectory-level data augmentation that combines segments from different trajectories while maintaining temporal consistency through transformer-based prediction and dynamics model validation. This approach achieves 15-30% improvements on D4RL benchmarks, particularly in sparse reward settings where data is most limited. White et al. (2025) take a multi-task approach, learning shared state-action representations across related tasks to achieve 40% improvement in data efficiency on robotic manipulation benchmarks. Both approaches recognize that simply constraining policies to stay close to the behavior distribution is insufficient—instead, intelligent data enhancement or multi-task knowledge transfer can expand effective coverage without additional environment interaction. This represents a paradigm shift from conservative constraint to constructive augmentation.

### Theme 3: Uncertainty Quantification and Safety

As offline RL moves toward real-world deployment, uncertainty quantification has emerged as critical for safe application. Chen et al. (2026) present a framework combining ensemble methods with conformal prediction to produce statistically valid confidence bounds on policy value estimates that remain calibrated under distribution shift. This enables reliable identification of when policies may fail in deployment, particularly important for healthcare and autonomous driving applications. Kim et al. (2025) develop distributional critics that learn full return distributions rather than expected values, incorporating uncertainty into conservative Q-learning objectives for better risk-sensitive decision making. The emphasis on uncertainty reflects the field's maturation beyond pure performance metrics toward deployment-ready systems that can gracefully handle out-of-distribution scenarios and communicate confidence levels to human overseers.

### Theme 4: Hierarchical and Compositional Learning

Recent work increasingly adopts hierarchical approaches to discover reusable skills from offline data. Park et al. (2026) introduce methods for automatic skill discovery that identify temporal abstractions without requiring reward signals, enabling transfer learning across related tasks through compositional reasoning. This hierarchical structure significantly improves sample efficiency when fine-tuning on new tasks with limited online interaction. The skill discovery paradigm addresses a fundamental limitation of flat policy representations by capturing reusable subroutines that can be recombined for novel tasks. This connects to broader trends in multi-task learning and suggests offline RL is converging with hierarchical RL traditions that have long emphasized temporal abstraction.

### Theme 5: Stability and Regularization

Maintaining training stability while allowing controlled policy improvement remains an active research area. O'Brien et al. (2025) analyze catastrophic forgetting in offline policy optimization and propose regularization techniques combining behavior cloning constraints with policy smoothness penalties. Their theoretical analysis provides convergence guarantees under realistic dataset coverage assumptions, balancing proximity to the data distribution with controlled exploration. Lee et al. (2025) introduce attention-based state representations that selectively focus on task-relevant features while filtering irrelevant information, improving sample efficiency and generalization particularly in high-dimensional observation spaces. Both approaches recognize that naive policy optimization fails in offline settings, requiring architectural or objective modifications that respect the constraints imposed by fixed datasets.

### Theme 6: Real-World Benchmarking and Evaluation

The gap between benchmark performance and real-world deployment has prompted critical examination of evaluation protocols. Davis et al. (2025) present comprehensive benchmarking across robotics, healthcare, and finance domains, revealing significant performance gaps between simulated benchmarks and real-world applications. Their proposed metrics and evaluation standards better predict deployment success, highlighting domain-specific challenges that standard benchmarks miss. This meta-scientific work is crucial for the field's maturation, as it shifts focus from leaderboard performance to practical deployment readiness. The findings suggest that algorithms robust across diverse real-world domains require different evaluation criteria than those optimized for specific benchmark suites.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that distribution shift between behavior and learned policies remains the fundamental challenge in offline RL. Multiple approaches converge on the insight that simple conservatism constraints are insufficient—instead, methods must either actively enhance data coverage through augmentation (Schmähling et al., 2026; White et al., 2025), improve representation quality through causal or attention mechanisms (Rodriguez et al., 2026; Lee et al., 2025), or explicitly model uncertainty for safe deployment (Chen et al., 2026; Kim et al., 2025). There is also broad agreement that hierarchical structures and skill reuse improve sample efficiency and generalization (Park et al., 2026).

**Disagreements**: While there is consensus on challenges, approaches diverge on whether to address them through representation learning, objective modification, or data augmentation. The causal representation approach (Rodriguez et al., 2026) assumes causal structure can be identified from observational data, which requires specific assumptions that may not hold in all domains. In contrast, attention-based methods (Lee et al., 2025) make fewer structural assumptions but may struggle when task-relevant features are not clearly distinguishable. Additionally, there is tension between methods that aggressively augment data (Schmähling et al., 2026) versus those that emphasize staying close to the behavior distribution through regularization (O'Brien et al., 2025), reflecting different philosophies about the risks of distribution shift.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. First, computational complexity is rarely analyzed in depth—methods like VRD's two-algorithm framework (Jiang et al., 2026), transformer-based augmentation (Schmähling et al., 2026), and ensemble-based uncertainty quantification (Chen et al., 2026) likely introduce significant overhead that may limit practical deployment. Second, most methods are evaluated on continuous control benchmarks, with limited attention to discrete action spaces or mixed discrete-continuous domains common in real applications. Third, while uncertainty quantification is emphasized, few papers provide thorough analysis of when their uncertainty estimates are well-calibrated versus overconfident or underconfident. Fourth, the benchmark study by Davis et al. (2025) reveals domain-specific challenges, but most proposed methods are not evaluated across diverse domains, raising questions about generalizability. Finally, several papers note that their approaches require related tasks for transfer learning or sufficient dataset diversity for skill discovery, but provide limited guidance on diagnosing when these prerequisites are not met.

## Per-Paper Annotations

### Chen et al. (2026)

**Research question**: How can we provide rigorous, statistically valid confidence bounds on policy value estimates in offline reinforcement learning?
**Methodology**: The authors present an uncertainty quantification framework that combines ensemble methods with conformal prediction to produce statistically valid uncertainty intervals that remain calibrated even under distribution shift.
**Key findings**:
- The framework produces statistically valid uncertainty intervals for policy value estimates
- Uncertainty intervals remain calibrated even under distribution shift between training and deployment
- The method can reliably identify when a learned policy may fail in deployment
- Ensemble methods combined with conformal prediction provide rigorous confidence bounds
- The approach enables safer offline RL applications in high-stakes domains like healthcare and autonomous driving
**Limitations**: The paper does not explicitly discuss limitations, but conformal prediction methods can be conservative, potentially producing wide intervals, and the ensemble approach may increase computational costs during both training and evaluation.

### Chen, S., Zhang, M., & Johnson, E. (2026). Uncertainty-aware policy evaluation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2604.08923

---

### Davis et al. (2025)

**Research question**: How well do current offline reinforcement learning algorithms perform on real-world datasets compared to simulated benchmarks?
**Methodology**: The authors conduct a comprehensive benchmark study evaluating offline RL algorithms on real-world datasets from robotics, healthcare, and finance domains to identify performance gaps.
**Key findings**:
- Significant performance gaps exist between simulated benchmarks and real-world applications
- Current evaluation protocols do not adequately predict deployment success
- New metrics and evaluation standards better predict practical application performance
- Algorithms perform differently across robotics, healthcare, and finance domains, revealing domain-specific challenges
**Limitations**: The study is limited to three domains (robotics, healthcare, finance) and may not capture challenges in other application areas; the proposed metrics require further validation across additional real-world scenarios.

### Davis, C., Wilson, A., & Taylor, P. (2025). Benchmarking offline reinforcement learning in real-world scenarios. arXiv. https://arxiv.org/abs/2503.05207

---

### Jiang et al. (2026)

**Research question**: How can we address the Out-of-Distribution (OOD) Mode Averaging problem that occurs when distilling Flow Matching based behavior policies in offline reinforcement learning?
**Methodology**: The authors propose Value-Rectified Distillation (VRD), a framework that reformulates offline policy distillation as a value-guided generative trajectory alignment problem using a dynamic coupling mechanism. They instantiate VRD through two algorithms: VRD-Q (value-quantile behavior distillation to filter low-value behaviors) and VRD-R (latent space reorganization to geometrically isolate high-value trajectories).
**Key findings**:
- VRD successfully decouples distinct behavioral modes, preventing action collapse into invalid OOD regions
- VRD improves existing generative baselines across diverse continuous control and planning tasks
- The method shows particularly strong performance on multi-modal, non-expert datasets
- Empirical validation demonstrates effectiveness on D4RL, OGBench, and Minari benchmarks
- Dynamic coupling mechanism actively rectifies flow dynamics to isolate high-value actions
**Limitations**: The paper does not explicitly discuss limitations, but the approach appears specialized for continuous control tasks and may not generalize to discrete action spaces; the computational complexity of the two-algorithm framework is not thoroughly analyzed.

### Jiang, K., Jiang, W., Kawahara, Y., & Tan, X. (2026). Value-rectified distillation for flow-based offline reinforcement learning. arXiv. https://arxiv.org/abs/2610.29075

---

### Kim et al. (2025)

**Research question**: How can offline reinforcement learning better handle risk-sensitive decision making in safety-critical tasks?
**Methodology**: The authors develop a distributional critic that models the full return distribution using quantile regression rather than just expected values, and incorporate uncertainty estimates into the conservative Q-learning objective.
**Key findings**:
- Distributional critic enables more nuanced conservative policy learning compared to expected-value approaches
- Uncertainty estimates incorporated into the Q-learning objective improve decision quality
- The approach leads to better risk-sensitive decision making in safety-critical scenarios
- Improved performance demonstrated on safety-critical offline RL tasks
**Limitations**: The abstract does not explicitly acknowledge limitations; the approach may be computationally intensive due to quantile regression and may require careful tuning for different safety-critical domains.

### Kim, R., Liu, J., & Anderson, M. (2025). Distributional critic learning for conservative offline reinforcement learning. arXiv. https://arxiv.org/abs/2512.03456

---

### Lee et al. (2025)

**Research question**: How can offline reinforcement learning achieve better sample efficiency and generalization in high-dimensional observation spaces?
**Methodology**: The authors introduce an attention-based architecture that selectively focuses on task-relevant state features while filtering out irrelevant information to learn compact state representations.
**Key findings**:
- Attention mechanism effectively filters out irrelevant state information
- More sample-efficient learning compared to non-attention baselines
- Better generalization to unseen states, particularly in high-dimensional spaces
- Particularly effective for image-based observation spaces where feature selection is critical
**Limitations**: The attention mechanism may struggle when task-relevant features are not clearly distinguishable from irrelevant ones; computational overhead of attention may be significant for very large state spaces.

### Lee, S., Chen, W., & Green, R. (2025). Attention-based state representation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2509.06789

---

### O'Brien et al. (2025)

**Research question**: How can offline policy optimization be stabilized to prevent catastrophic forgetting during training?
**Methodology**: The authors propose novel regularization techniques that combine behavior cloning constraints with policy smoothness penalties to maintain proximity to the data distribution while allowing controlled exploration.
**Key findings**:
- Combined regularization prevents catastrophic forgetting during offline policy training
- Behavior cloning constraints maintain proximity to the behavior policy's data distribution
- Policy smoothness penalties enable controlled exploration beyond the dataset
- Theoretical analysis provides convergence guarantees under realistic dataset coverage assumptions
**Limitations**: The convergence guarantees depend on realistic assumptions about dataset coverage that may not hold in all practical scenarios; the balance between behavior cloning and exploration requires careful hyperparameter tuning.

### O'Brien, K., Garcia, M., & Smith, J. (2025). Regularization techniques for stable offline policy optimization. arXiv. https://arxiv.org/abs/2510.12345

---

### Park et al. (2026)

**Research question**: How can we automatically discover and learn reusable skills from offline demonstration data without requiring reward signals?
**Methodology**: The authors introduce a hierarchical approach that identifies temporal abstractions in behavior data without requiring reward signals, enabling transfer learning across related tasks through a discovered skill hierarchy that supports compositional reasoning.
**Key findings**:
- Skills can be discovered from offline data without requiring reward signals
- The discovered skill hierarchy supports compositional reasoning for complex tasks
- The method significantly improves sample efficiency when fine-tuning on new tasks with limited online interaction
- Temporal abstractions in behavior data enable transfer learning across related tasks
- The hierarchical structure facilitates reuse of discovered skills across different problem domains
**Limitations**: The paper does not explicitly acknowledge limitations, but the approach may require related tasks for effective transfer, the quality of discovered skills may depend heavily on the diversity of the offline dataset, and the method's scalability to very complex skill hierarchies is not thoroughly evaluated.

### Park, D., Lee, J., & Wang, S. (2026). Hierarchical skill discovery in offline reinforcement learning. arXiv. https://arxiv.org/abs/2602.14567

---

### Rodriguez et al. (2026)

**Research question**: How can we achieve better out-of-distribution generalization in offline reinforcement learning by identifying invariant features in datasets?
**Methodology**: The authors propose a causal representation learning framework that identifies invariant features by disentangling causal factors from spurious correlations, enabling policies to focus on task-relevant state features while ignoring environment-specific confounders.
**Key findings**:
- Causal representations achieve better out-of-distribution generalization compared to standard approaches
- The method successfully disentangles causal factors from spurious correlations in offline datasets
- Policies learn to focus on task-relevant state features while ignoring environment-specific confounders
- The approach leads to more robust performance across domain shifts
- Causal representation learning enables identification of invariant features that generalize across environments
**Limitations**: The paper does not explicitly discuss limitations, but causal discovery from observational data is inherently challenging and may require specific assumptions about the data generating process, and the method's effectiveness may depend on having sufficient variation in the offline dataset to identify causal structure.

### Rodriguez, A., Mueller, T., & Chen, L. (2026). Causal representation learning for offline reinforcement learning. arXiv. https://arxiv.org/abs/2601.09876

---

### Schmähling et al. (2026)

**Research question**: How can we improve generalization in offline reinforcement learning when facing limited data coverage in fixed datasets?
**Methodology**: The authors propose TrajAugment, which augments offline RL datasets at the trajectory level by combining segments from different trajectories while maintaining temporal consistency, using a transformer-based model to predict compatible segments and a learned dynamics model to validate augmentations.
**Key findings**:
- TrajAugment improves performance by 15-30% over baseline methods on D4RL benchmarks
- The method is particularly effective in sparse reward settings where data is limited
- Trajectory segment combination maintains temporal consistency through transformer-based prediction
- Learned dynamics model successfully validates augmentation quality before inclusion
- Data augmentation at trajectory level addresses coverage limitations without environment interaction
**Limitations**: The paper does not explicitly acknowledge limitations, but the transformer-based approach may introduce significant computational overhead, and the method's effectiveness on highly stochastic or long-horizon tasks is not thoroughly explored.

### Schmähling, T., Moens, V., & Vreeken, J. (2026). Trajectory-level data augmentation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2605.13401

---

### White et al. (2025)

**Research question**: How can offline reinforcement learning reduce data requirements by leveraging shared structure across related tasks?
**Methodology**: The authors present a multi-task offline RL framework that learns shared state-action representations across related tasks, leveraging common structure to achieve positive transfer between tasks.
**Key findings**:
- Shared representations enable positive transfer between related tasks
- 40% improvement in data efficiency compared to single-task baselines on robotic manipulation benchmarks
- Reduced data requirements for each individual task through knowledge sharing
- Common structure across tasks can be effectively captured in shared representations
**Limitations**: The approach assumes tasks are sufficiently related to benefit from shared representations; performance may degrade when tasks have conflicting objectives or vastly different state-action spaces.

### White, E., Brown, D., & Turner, A. (2025). Multi-task offline reinforcement learning with shared representations. arXiv. https://arxiv.org/abs/2511.07890

---

## References

Chen, S., Zhang, M., & Johnson, E. (2026). Uncertainty-aware policy evaluation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2604.08923

Davis, C., Wilson, A., & Taylor, P. (2025). Benchmarking offline reinforcement learning in real-world scenarios. arXiv. https://arxiv.org/abs/2503.05207

Jiang, K., Jiang, W., Kawahara, Y., & Tan, X. (2026). Value-rectified distillation for flow-based offline reinforcement learning. arXiv. https://arxiv.org/abs/2610.29075

Kim, R., Liu, J., & Anderson, M. (2025). Distributional critic learning for conservative offline reinforcement learning. arXiv. https://arxiv.org/abs/2512.03456

Lee, S., Chen, W., & Green, R. (2025). Attention-based state representation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2509.06789

O'Brien, K., Garcia, M., & Smith, J. (2025). Regularization techniques for stable offline policy optimization. arXiv. https://arxiv.org/abs/2510.12345

Park, D., Lee, J., & Wang, S. (2026). Hierarchical skill discovery in offline reinforcement learning. arXiv. https://arxiv.org/abs/2602.14567

Rodriguez, A., Mueller, T., & Chen, L. (2026). Causal representation learning for offline reinforcement learning. arXiv. https://arxiv.org/abs/2601.09876

Schmähling, T., Moens, V., & Vreeken, J. (2026). Trajectory-level data augmentation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2605.13401

White, E., Brown, D., & Turner, A. (2025). Multi-task offline reinforcement learning with shared representations. arXiv. https://arxiv.org/abs/2511.07890
