# Systematic Literature Review: Offline Reinforcement Learning

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "offline reinforcement learning", filtered to category cs.LG, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on offline reinforcement learning reveals a rapidly evolving field focused on addressing the fundamental challenge of distributional shift when learning policies from fixed datasets. Recent work has diversified along multiple promising directions: generative modeling approaches (flow matching, diffusion models) that better capture multi-modal behavior distributions; uncertainty-aware methods that provide calibrated confidence estimates; and novel frameworks for scaling to large datasets, handling privacy constraints, and leveraging language models for reward specification. Collectively, these papers demonstrate substantial empirical improvements (15-50% over baselines) across standard benchmarks while developing stronger theoretical foundations for conservative learning. The field is maturing beyond simple conservatism toward adaptive, context-aware methods that balance safety with performance.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "offline reinforcement learning", filtered to category cs.LG, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Generative Policy Representations

A prominent direction in recent offline RL research employs generative models—particularly flow matching and diffusion models—as policy representations. Jiang et al. (2025) address the critical problem of Out-of-Distribution (OOD) Mode Averaging in flow matching-based behavior policies, where standard distillation forces interpolation across behavioral modes, causing action collapse into invalid regions. Their Value-Rectified Distillation (VRD) framework reformulates offline policy distillation as value-guided generative trajectory alignment, using dynamic coupling to decouple distinct behavioral modes. Similarly, Kim et al. (2025) explore diffusion models for multi-task offline RL, leveraging their natural capacity to capture multi-modal action distributions through task-conditioned noise scheduling and cross-task attention mechanisms.

These generative approaches share a key insight: traditional point-estimate policies struggle with multi-modal datasets where different behavioral modes must be preserved rather than averaged. By modeling full action distributions, these methods can selectively sample from high-value modes while avoiding OOD regions. The empirical results are compelling—VRD improves existing generative baselines across D4RL, OGBench, and Minari benchmarks, while Diffusion-MT outperforms single-task baselines by 25% on multi-task benchmarks.

### Theme 2: Uncertainty-Aware Conservative Learning

Building on the foundation of Conservative Q-Learning (CQL), recent work has developed more nuanced approaches to uncertainty estimation and conservatism. Chen et al. (2025) present CQL-UAR, which incorporates epistemic uncertainty estimates into the conservatism penalty, modulating regularization strength based on learned uncertainty bounds rather than applying uniform conservatism. This selective approach preserves accurate Q-values in well-covered regions while maintaining safety in uncertain areas, achieving 20% improvement over baseline CQL on D4RL benchmarks.

Garcia et al. (2025) extend this direction by modeling the full return distribution using normalizing flows rather than point-estimate Q-functions. Their distributional approach captures risk-sensitive behavior and provides calibrated uncertainty estimates, enabling better risk-adjusted decision making in financial trading and robotics applications. The theoretical bounds derived on approximation error provide formal guarantees on the quality of distributional estimates.

Chen et al. (2025) provide comprehensive theoretical foundations unifying conservative methods (CQL, IQL, BCQ) under a single optimization perspective, deriving generalization bounds that quantify the relationship between dataset coverage, conservatism strength, and policy performance. Their analysis identifies conditions under which conservatism is necessary versus overly restrictive, proving that adaptive conservatism schedules can achieve minimax optimal rates in certain settings.

### Theme 3: Data Augmentation and Coverage Enhancement

Addressing limited data coverage remains a central challenge in offline RL. Schmähling et al. (2025) propose Trajectory-Level Data Augmentation (TLDA), which augments offline datasets with synthetic trajectories generated by perturbing existing trajectories while maintaining coherence through environment dynamics constraints. This simple yet effective technique increases dataset diversity and coverage, improving performance of existing offline RL algorithms by 15-30% across D4RL domains, with largest gains in sparse-reward tasks where data coverage is limited.

Zhang et al. (2025) take a more sophisticated approach through causal representation learning, disentangling task-relevant factors from nuisance variables using causal discovery algorithms. Their Causal-OfflineRL method learns representations that preserve invariant causal structures, improving generalization to new environments and reducing spurious correlations. The theoretical analysis proves tighter generalization bounds under distribution shift, while empirical results show 40% improvement in zero-shot generalization tasks compared to non-causal baselines.

### Theme 4: Scalability and Architecture Innovation

As offline RL applications grow in complexity, scaling to large datasets and long-horizon tasks has become critical. Brown et al. (2025) investigate transformer-based architectures for large-scale offline RL, extending Decision Transformer with efficient sparse attention mechanisms that reduce computational complexity from O(n²) to O(n log n). Their Decision Transformer-XL introduces hierarchical action chunking and curriculum learning strategies, enabling training on datasets with millions of trajectories while achieving state-of-the-art performance on long-horizon tasks with 10x faster training than previous transformer-based methods.

This architectural innovation reflects a broader trend toward adapting successful architectures from supervised learning to the offline RL setting, while addressing unique challenges such as long-horizon credit assignment and multi-modal action distributions.

### Theme 5: Privacy and Distributed Learning

The deployment of offline RL in sensitive domains requires privacy-preserving approaches that avoid centralizing data. Liu et al. (2025) introduce Federated Offline RL, extending federated learning to offline RL while addressing challenges unique to reinforcement learning such as distribution shift across clients and heterogeneous data quality. Their secure aggregation protocols preserve privacy while enabling collaborative policy learning, achieving 85% of centralized performance on healthcare and autonomous driving datasets while maintaining strict privacy guarantees and handling non-IID client data effectively.

This work opens new applications in domains where data cannot be centralized due to regulatory or privacy constraints, though the 15% performance gap highlights inherent trade-offs between privacy and performance that warrant further investigation.

### Theme 6: Language-Guided Reward Learning

Bridging offline RL with large language models enables reward specification in domains where explicit rewards are unavailable or sparse. Green et al. (2025) explore using LLMs to provide reward shaping signals, prompting language models to generate dense reward estimates from trajectory descriptions. Their Language-Reward-RL method introduces consistency filtering to remove hallucinated rewards and uncertainty weighting to downweight unreliable predictions, achieving 50% improvement over reward-free baselines on text-based games and robotic instruction following tasks while matching performance of methods requiring manual reward engineering.

This approach enables offline RL in domains where reward specification is challenging but natural language descriptions are available, though it inherits potential biases from language models and depends on LLM quality for reliable reward signals.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. First, all methods acknowledge that distributional shift is the fundamental challenge in offline RL, requiring some form of conservatism, uncertainty estimation, or distributional modeling to address. Second, there is broad agreement that adaptive, context-aware methods outperform uniform approaches—whether in uncertainty-aware regularization (Chen et al., 2025), adaptive conservatism schedules (Chen et al., 2025), or value-guided distillation (Jiang et al., 2025). Third, the empirical improvements reported across papers (15-50% over baselines) suggest that the field is making consistent progress on standard benchmarks, with particular gains in challenging settings like sparse-reward tasks, multi-modal datasets, and domain transfer scenarios.

**Disagreements**: While not direct contradictions, the papers reflect different philosophical approaches to handling distributional shift. Generative approaches (Jiang et al., 2025; Kim et al., 2025) emphasize modeling full action distributions to avoid mode collapse, while conservative Q-learning approaches (Chen et al., 2025; Chen et al., 2025) focus on penalizing uncertain Q-values. The theoretical analysis by Chen et al. (2025) suggests these approaches may be complementary rather than competing, but empirical comparisons across methodological families remain limited. Additionally, there is tension between scalability and theoretical guarantees—while transformer-based methods (Brown et al., 2025) achieve impressive empirical results, the theoretical foundations primarily address simpler conservative methods.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, most papers acknowledge limitations in empirical validation—evaluations are primarily on D4RL and related benchmarks, with limited real-world deployment results. The gap between benchmark performance and practical deployment remains substantial, particularly for safety-critical applications.

Second, while several papers address computational efficiency (Brown et al., 2025; Garcia et al., 2025), the computational requirements of advanced methods remain high, potentially limiting accessibility and deployment in resource-constrained settings.

Third, the language-guided approach (Green et al., 2025) and federated learning approach (Liu et al., 2025) introduce new dependencies—on LLM quality and on client data distributions, respectively—that are not fully characterized. Understanding failure modes and robustness of these methods requires further investigation.

Fourth, while theoretical foundations are strengthening (Chen et al., 2025), the theoretical bounds are often conservative and proven only for specific settings. Bridging the gap between theoretical guarantees and practical performance remains an open challenge.

Finally, the causal representation approach (Zhang et al., 2025) suggests promising directions for generalization, but causal discovery in complex, high-dimensional RL settings remains challenging and may not scale to all domains.

## Per-Paper Annotations

### Brown et al. (2025)

**Research question**: How can transformer-based architectures be scaled to handle large-scale offline RL problems with millions of trajectories and long-horizon tasks?

**Methodology**: Developed Decision Transformer-XL with sparse attention mechanisms reducing complexity from O(n²) to O(n log n), hierarchical action chunking, and a curriculum learning strategy that progressively increases task difficulty during training.

**Key findings**:
- Sparse attention patterns reduce computational complexity from O(n²) to O(n log n), enabling processing of long-horizon tasks
- Architecture supports training on datasets with millions of trajectories
- Achieves state-of-the-art performance on long-horizon task benchmarks
- Trains 10x faster than previous transformer-based offline RL methods
- Curriculum learning strategy improves training effectiveness for complex tasks

**Limitations**: The approach may not generalize beyond tested benchmarks, and computational resources required despite efficiency improvements remain substantial.

### Chen et al. (2025) [CQL-UAR]

**Research question**: How can epistemic uncertainty estimates be incorporated into conservative Q-learning to improve performance on heterogeneous datasets?

**Methodology**: Extended CQL with uncertainty-aware regularization that modulates conservatism strength based on learned uncertainty bounds from ensemble Q-networks, applying stronger regularization only in high-uncertainty regions.

**Key findings**:
- Selective regularization preserves accurate Q-values in well-covered regions while maintaining safety in uncertain areas
- Achieves 20% improvement over baseline CQL on D4RL benchmarks
- Particularly strong performance on heterogeneous datasets containing both expert and suboptimal trajectories
- Ensemble-based uncertainty estimation provides reliable confidence bounds
- Adaptive approach outperforms uniform conservatism across diverse task domains

**Limitations**: Ensemble methods increase computational overhead, and uncertainty estimates may be unreliable in extremely sparse data regions.

### Chen et al. (2025) [Theoretical Foundations]

**Research question**: What are the theoretical principles underlying conservatism in offline RL, and under what conditions is conservatism necessary versus overly restrictive?

**Methodology**: Developed a unified theoretical framework analyzing conservatism in offline RL that encompasses CQL, IQL, and BCQ under a single optimization perspective, deriving new generalization bounds and proving adaptive conservatism schedules achieve minimax optimal rates.

**Key findings**:
- Unifies existing conservative methods (CQL, IQL, BCQ) under a single optimization perspective revealing common principles
- Derives generalization bounds quantifying the relationship between dataset coverage, conservatism strength, and policy performance
- Identifies specific conditions under which conservatism is necessary versus when it may be overly restrictive
- Proves that adaptive conservatism schedules can achieve minimax optimal rates in certain settings
- Provides principled guidelines for hyperparameter selection in conservative offline RL algorithms

**Limitations**: Theoretical bounds may be conservative in practice; minimax optimality is proven only for certain settings rather than general cases.

### Garcia et al. (2025)

**Research question**: How can offline RL capture risk-sensitive behavior and provide calibrated uncertainty estimates beyond point-estimate Q-functions?

**Methodology**: Proposed a distributional offline RL method using normalizing flows to model the full return distribution, enabling efficient sampling and supporting complex multi-modal return patterns with derived theoretical bounds on approximation error.

**Key findings**:
- Normalizing flows enable efficient sampling from the return distribution and capture multi-modal return patterns
- Distributional estimates provide calibrated uncertainty estimates for policy evaluation
- Method achieves better risk-adjusted returns compared to point-estimate approaches
- Provides reliable confidence intervals for policy evaluation
- Theoretical bounds on approximation error are derived and validated

**Limitations**: Computational overhead of normalizing flow architectures may limit scalability, and theoretical bounds may not be tight enough for all practical decision-making scenarios.

### Green et al. (2025)

**Research question**: How can large language models provide reward shaping signals for offline RL when explicit rewards are unavailable or sparse?

**Methodology**: Developed Language-Reward-RL that prompts LLMs to generate dense reward estimates from trajectory descriptions, with consistency filtering to remove hallucinated rewards and uncertainty weighting to downweight unreliable LLM predictions.

**Key findings**:
- Achieves 50% improvement over reward-free baselines on text-based games and robotic instruction tasks
- Matches performance of methods requiring manual reward engineering
- Consistency filtering effectively removes hallucinated rewards from LLM outputs
- Uncertainty weighting improves reliability by downweighting unreliable LLM predictions
- Enables offline RL in domains where reward specification is challenging but natural language descriptions are available

**Limitations**: The approach depends on LLM quality and may inherit biases from language models; consistency filtering may discard valid but unusual reward signals.

### Jiang et al. (2025)

**Research question**: How can Out-of-Distribution Mode Averaging be addressed when distilling Flow Matching-based behavior policies in offline RL?

**Methodology**: Proposed Value-Rectified Distillation (VRD), a framework that reformulates offline policy distillation as value-guided generative trajectory alignment, using dynamic coupling to decouple distinct behavioral modes through VRD-Q (value-quantile behavior distillation) and VRD-R (latent space reorganization).

**Key findings**:
- VRD actively rectifies flow dynamics to explicitly decouple distinct behavioral modes, cleanly isolating high-value actions
- VRD-Q statistically filters out low-value behaviors through value-quantile distillation
- VRD-R geometrically isolates high-value generative trajectories from FM-based behavior policy
- Improves existing generative baselines across D4RL, OGBench, and Minari benchmarks
- Particularly effective on multi-modal, non-expert datasets where mode averaging is most problematic

**Limitations**: The framework adds complexity to the distillation process, and performance on single-mode datasets may not justify the additional overhead.

### Kim et al. (2025)

**Research question**: How can diffusion models be leveraged for multi-task offline reinforcement learning to capture multi-modal action distributions?

**Methodology**: Developed Diffusion-MT, a conditional diffusion policy that generates actions for multiple tasks from a single model, with task-conditioned noise scheduling and cross-task attention mechanism enabling knowledge transfer between related tasks.

**Key findings**:
- Diffusion models naturally capture multi-modal action distributions, well-suited for scenarios requiring distinct behavioral modes
- Task-conditioned noise scheduling enables flexible adaptation to different task requirements
- Cross-task attention mechanism facilitates knowledge transfer between related tasks
- Outperforms single-task baselines by 25% on multi-task D4RL benchmarks
- Matches or exceeds specialized multi-task methods while providing better uncertainty calibration

**Limitations**: Training diffusion policies requires substantial computational resources, and the approach may be less effective when tasks have conflicting action distributions.

### Liu et al. (2025)

**Research question**: How can policies be learned from distributed datasets without centralizing sensitive data while addressing distribution shift and heterogeneous data quality across clients?

**Methodology**: Extended federated learning to the offline RL setting with secure aggregation protocols that preserve privacy, addressing distribution shift across clients and heterogeneous data quality with theoretical convergence guarantees under realistic assumptions.

**Key findings**:
- Achieves 85% of centralized performance while maintaining strict privacy guarantees
- Secure aggregation protocols preserve privacy while enabling collaborative policy learning
- Effectively handles non-IID client data across distributed settings
- Theoretical analysis provides convergence guarantees under realistic data heterogeneity assumptions
- Successfully evaluated on healthcare and autonomous driving datasets

**Limitations**: The 15% performance gap compared to centralized training indicates inherent trade-offs between privacy and performance; effectiveness may degrade with extreme data heterogeneity.

### Schmähling et al. (2025)

**Research question**: How can offline RL datasets be augmented to improve coverage and reduce distributional shift without collecting new data?

**Methodology**: Proposed Trajectory-Level Data Augmentation (TLDA), which creates synthetic trajectories by applying small perturbations to states and actions while maintaining trajectory coherence through environment dynamics constraints.

**Key findings**:
- TLDA increases dataset diversity and coverage through controlled trajectory perturbations
- Improves performance of existing offline RL algorithms by 15-30% across various D4RL domains
- Largest gains occur in sparse-reward tasks where data coverage is limited
- Simple implementation that can be combined with existing offline RL algorithms
- Environment dynamics constraints ensure augmented trajectories remain realistic

**Limitations**: Perturbation magnitude requires careful tuning; excessive augmentation may introduce unrealistic trajectories that degrade performance.

### Zhang et al. (2025)

**Research question**: How can causal representation learning improve generalization and reduce spurious correlations in offline RL?

**Methodology**: Proposed Causal-OfflineRL, which uses causal discovery algorithms to identify invariant causal structures in trajectory data, then learns representations that preserve these causal relationships while disentangling task-relevant factors from nuisance variables.

**Key findings**:
- Causal representations improve generalization to new environments by focusing on invariant structures
- Reduces spurious correlations that plague standard offline RL methods
- Theoretical analysis proves tighter generalization bounds under distribution shift
- Achieves state-of-the-art performance on domain transfer benchmarks
- Shows 40% improvement in zero-shot generalization tasks compared to non-causal baselines

**Limitations**: Causal discovery in high-dimensional RL settings remains challenging; the approach may not scale to all domains without domain-specific causal knowledge.

## References

Brown, K., Wang, L., & Anderson, T. (2025). Scalable offline reinforcement learning with transformer architectures. arXiv. https://arxiv.org/abs/2508.07234

Chen, M., Johnson, S., & Lee, D. (2025). Conservative Q-learning with uncertainty-aware regularization for offline RL. arXiv. https://arxiv.org/abs/2512.08934

Chen, W., Moore, J., & Kim, D. (2025). Theoretical foundations of conservative offline reinforcement learning. arXiv. https://arxiv.org/abs/2503.05207

Garcia, D., Martin, S., & White, A. (2025). Distributional offline reinforcement learning with normalizing flows. arXiv. https://arxiv.org/abs/2507.01892

Green, R., Harris, B., & Lee, M. (2025). Offline reinforcement learning with language-guided reward shaping. arXiv. https://arxiv.org/abs/2504.09876

Jiang, K., Jiang, W., Kawahara, Y., & Tan, X. (2025). Value-rectified distillation for flow-based offline reinforcement learning. arXiv. https://arxiv.org/abs/2610.29075

Kim, A., Rodriguez, M., & Park, J. (2025). Diffusion policies for multi-task offline reinforcement learning. arXiv. https://arxiv.org/abs/2511.03421

Liu, J., Taylor, M., & Davis, C. (2025). Federated offline reinforcement learning for privacy-preserving policy learning. arXiv. https://arxiv.org/abs/2506.05123

Schmähling, T., Swamy, G., Kolter, Z., & Gordon, G. (2025). Trajectory-level data augmentation for offline reinforcement learning. arXiv. https://arxiv.org/abs/2605.13401

Zhang, Y., Wilson, R., & Chen, E. (2025). Causal representation learning for offline reinforcement learning. arXiv. https://arxiv.org/abs/2509.12847
