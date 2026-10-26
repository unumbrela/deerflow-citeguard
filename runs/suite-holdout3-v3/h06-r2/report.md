# Systematic Literature Review: Test-Time Scaling of Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "test-time compute scaling", filtered to category cs.LG, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on test-time scaling of language models reveals a rapidly evolving field focused on improving reasoning capabilities and performance through increased inference-time computation. Recent work demonstrates that test-time compute scaling extends beyond traditional autoregressive language models to diverse domains including speech recognition, reinforcement learning, and diffusion models. Key advances include efficient tree search algorithms that reduce memory overhead, value-guided search methods that improve sampling efficiency, and architectural innovations like looped transformers that enable controllable test-time computation. The collective findings suggest that test-time scaling is most effective when combined with verification mechanisms, uncertainty estimation, and architectural designs that maintain trajectory diversity while managing computational costs.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "test-time compute scaling", filtered to category cs.LG, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficient Search Algorithms for Test-Time Scaling

A prominent research direction focuses on developing efficient search algorithms that enable test-time compute scaling while managing computational resources. Hooper et al. (2025) introduced Efficient Tree Search (ETS), which uses a linear programming cost model to promote KV cache sharing while maintaining semantic diversity across trajectories. Their approach achieves a 1.8× reduction in average KV cache size and 1.4× increased throughput compared to prior methods, with minimal accuracy degradation. Similarly, Wang et al. (2025) proposed block-wise value-guided search (VGS) that trains token-level value models without requiring fine-grained step definitions, collecting 2.5 million reasoning traces to train a 1.5B value model. Their results show that VGS significantly reduces inference FLOPs required to achieve the same performance as majority voting, demonstrating that value-guided approaches can make test-time scaling more computationally efficient.

### Theme 2: Architectural Innovations for Controllable Test-Time Computation

Several papers explore architectural modifications that make test-time computation more controllable and effective. Kaloga et al. (2026) introduced LARM, a depth-conditioned looped Transformer that structures recurrent encoder depth as a controllable test-time compute axis for automatic speech recognition. Their approach combines sparse CTC checkpoints, supervision-clock embeddings, FiLM depth conditioning, and delayed soft-posterior feedback to enable shared weights to specialize across recurrent steps. Labovich (2026) provided theoretical analysis of looped transformers, establishing a fixed-point based framework along three stability axes (reachability, input-dependence, geometry). Their findings reveal that recall combined with outer normalization produces regimes where fixed points are simultaneously reachable, locally smooth in the input, and supported by stable backpropagation, offering design principles for architectures that extrapolate to harder problems at test time rather than memorize training-specific solutions.

### Theme 3: Verification and Value Functions for Test-Time Scaling

A critical theme emerging from the literature is the importance of verification mechanisms and value functions for effective test-time scaling. Sareen et al. (2025) demonstrated that prevalent RL methods (GRPO, Leave-one-out PPO) abandon learned value functions, hindering test-time compute scaling that relies on verification. Their proposed RL^V approach jointly trains the LLM as both a reasoner and a generative verifier using RL-generated data, boosting MATH accuracy by over 20% with parallel sampling and enabling 8-32x more efficient test-time compute scaling. This work highlights that test-time scaling benefits substantially from having reliable verification signals that can guide search and selection among multiple generated trajectories.

### Theme 4: Uncertainty-Triggered Selective Computation

Recent work recognizes that not all instances benefit equally from increased test-time computation, motivating selective scaling approaches. Zhang et al. (2026) proposed UTTSI (Uncertainty-Triggered Test-Time Selective Inference), a training-free model-agnostic framework that uses a dual-signal estimator combining model logit confidence with data-level frequency prior to trigger adaptive feature filtering and stochastic feature-path explorations for uncertain instances. Their approach scales inference depth proportionally to per-instance uncertainty while keeping average overhead at approximately 2.8x base model cost. A seven-day online A/B test confirmed a 5.3% relative CTR gain (p < 0.01), demonstrating that selective test-time compute allocation serves as a practical complement to training-phase advances.

### Theme 5: Deliberation Stability and Drift Mitigation

An important challenge in test-time scaling is maintaining reasoning stability as computation depth increases. Jia (2026) identified a "Deliberation Drift Cliff" phenomenon where unconstrained recurrent latent models suffer catastrophic reasoning collapse at deeper thinking steps (K >= 16), with performance dropping 22-62% across benchmarks. The proposed Port-Hamiltonian Latent Deliberation (PH-LD) with Direct-Gradient Pure-Tensor Helmholtz-Hodge Decomposition (DG-HHD) decouples conservative and rotational flows in latent deliberation, achieving 58.67% peak accuracy (+25.94% over conservative HHD) while retaining 35.27% at K=32. This work reveals fundamental stability challenges in scaling test-time computation and provides theoretical tools for addressing them.

### Theme 6: Diversity in Test-Time Sampling

Maintaining diversity across samples emerges as a critical factor for effective test-time scaling. Olausson et al. (2026) studied diffusion language model sampling, introducing an idealized formal model of fork tokens to study the impact of remasking on expected entropy. Their tempered heuristics close the exploration gap (pass@k) between existing confidence-based and autoregressive sampling, outperforming both methods when controlling for cost (pass@NFE). Similarly, Hamid et al. (2025) introduced a polychromic objective for policy gradient methods that explicitly enforces exploration and refinement of diverse generations, adapting PPO with vine sampling and a modified advantage function. Their approach improves success rates by reliably solving a larger set of environment configurations and achieves substantially higher coverage in pass@k experiments, demonstrating that maintaining diverse repertoires of strategies is essential for effective test-time exploration.

### Theme 7: Fundamental Limits of Reasoning Depth

Several papers investigate the fundamental limits of reasoning depth and what factors constrain test-time scaling. Rodkin et al. (2025) used a controlled cellular-automata framework with disjoint training and test rules to exclude memorization, requiring models to infer hidden local rules from short state sequences and chain them to predict multiple future steps. Their findings reveal that while most neural architectures trained from scratch can learn rule inference with high next-step accuracy, performance drops sharply as the required number of intermediate reasoning steps increases. Increasing model depth is crucial for extending reasoning capability, and while extending effective depth via recurrence, memory, or test-time compute improves results, these improvements remain bounded, suggesting fundamental architectural constraints on reasoning depth.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that test-time compute scaling is most effective when combined with architectural modifications that enable controllable computation (Kaloga et al., 2026; Labovich, 2026) and verification mechanisms that can guide search (Sareen et al., 2025; Wang et al., 2025). There is broad agreement that naive increases in computation without structural support yield diminishing returns (Rodkin et al., 2025; Jia, 2026). The literature also converges on the importance of maintaining diversity in generated trajectories for effective exploration (Olausson et al., 2026; Hamid et al., 2025; Hooper et al., 2025).

**Disagreements**: The literature shows some tension between approaches that emphasize efficiency through selective computation (Zhang et al., 2026) versus those that focus on maximizing exploration through diverse sampling (Olausson et al., 2026; Hamid et al., 2025). While selective approaches aim to minimize computational overhead by targeting uncertain instances, diversity-focused approaches prioritize broad exploration even at higher computational cost. Additionally, there is disagreement about the relative importance of architectural modifications versus search algorithm improvements: some work suggests architectural changes are fundamental (Labovich, 2026; Kaloga et al., 2026), while others demonstrate significant gains from algorithmic improvements alone (Hooper et al., 2025; Wang et al., 2025).

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting a need for more transparent discussion of constraints and failure modes. Second, while several papers address stability challenges (Jia, 2026; Labovich, 2026), there remains limited understanding of the fundamental theoretical limits of test-time scaling across different architectures. Third, most work focuses on specific domains (speech recognition, CTR prediction, mathematical reasoning), with limited cross-domain generalization studies. Fourth, the computational cost-benefit tradeoffs of different approaches are not systematically compared, making it difficult to determine which methods offer the best efficiency. Finally, the interaction between training-time and test-time computation scaling remains underexplored, with most work treating them as separate concerns rather than complementary strategies.

## Per-Paper Annotations

### Hamid et al. (2025)

**Research question**: How can reinforcement learning fine-tuning maintain diversity in policy outputs to prevent collapse into easily exploitable behaviors while enabling effective exploration?
**Methodology**: The authors introduce a polychromic objective for policy gradient methods that explicitly enforces exploration and refinement of diverse generations, adapting proximal policy optimization (PPO) with vine sampling for on-policy rollouts and a modified advantage function reflecting the new objective. They evaluate on BabyAI, Minigrid, and Algorithmic Creativity environments.
**Key findings**:
- The polychromic objective improves success rates by reliably solving a larger set of environment configurations
- The method generalizes better under large perturbations compared to standard RLFT
- In pass@k experiments with multiple attempts, the policy achieves substantially higher coverage
- The approach maintains and exploits a diverse repertoire of strategies
**Limitations**: Not stated in abstract.

### Hooper et al. (2025)

**Research question**: How can tree search for test-time compute scaling maintain trajectory diversity for exploration while reducing memory consumption and latency through KV cache sharing?
**Methodology**: The authors propose Efficient Tree Search (ETS), which uses a linear programming cost model that penalizes the number of nodes retained to promote KV cache sharing, while incorporating a semantic coverage term to retain semantically different trajectories. They evaluate ETS by measuring KV cache size reduction and throughput improvement compared to prior methods.
**Key findings**:
- ETS achieves 1.8× reduction in average KV cache size during the search process
- ETS leads to 1.4× increased throughput relative to prior state-of-the-art methods
- The approach maintains minimal accuracy degradation compared to existing methods
- ETS does not require any custom kernel implementation
**Limitations**: Not stated in abstract.

### Jia (2026)

**Research question**: How can catastrophic deliberation drift in test-time latent reasoning be mitigated while preserving expressivity and computational efficiency?
**Methodology**: Through a 22-round empirical and theoretical investigation, the author establishes Port-Hamiltonian Latent Deliberation (PH-LD) and proposes Direct-Gradient Pure-Tensor Helmholtz-Hodge Decomposition (DG-HHD) to decouple conservative and rotational flows in latent deliberation. The approach is evaluated on logical benchmarks and small language model multi-hop causal reasoning tasks.
**Key findings**:
- Unconstrained recurrent latent models suffer a Deliberation Drift Cliff, with reasoning collapsing at deeper thinking steps (K >= 16), dropping 22-62% across benchmarks
- Strictly conservative scalar potential gradient flows suppress long-range drift (3.40% cliff) but bottleneck peak reasoning accuracy at 32.73%
- Unconstrained rotational flows achieve high symbolic expressivity (82.33%) but suffer a severe 36.87% drift cliff
- DG-HHD achieves 58.67% peak accuracy (+25.94% over conservative HHD) and retains 35.27% at K=32
- DG-HHD achieves 1.84x vector field and 2.09x RK45 rollout speedups by eliminating runtime autograd dependencies
- All 30 Level 0 deterministic invariants are certified with Hodge machine error 1.65e-17 and contraction error 5.55e-17
**Limitations**: The abstract does not explicitly state limitations, though the focus on Level 0 deterministic invariants suggests the approach may be constrained to specific problem classes.

### Kaloga et al. (2026)

**Research question**: How can test-time computation be scaled to improve automatic speech recognition (ASR) performance without training larger models?
**Methodology**: The authors introduce LARM, a depth-conditioned looped Transformer that uses sparse CTC checkpoints, supervision-clock embeddings, FiLM depth conditioning, and delayed soft-posterior feedback to structure recurrent encoder depth as a controllable test-time compute axis. The approach is evaluated on LibriSpeech, measuring word error rate (WER) as inference loops increase.
**Key findings**:
- Naive looping of shared Transformer blocks does not fully exploit additional recurrent compute for ASR
- LARM improves WER as the number of inference loops increases
- LARM achieves performance competitive with deeper unshared-parameter baselines
- Test-time compute scaling can extend beyond autoregressive language-model reasoning to continuous non-autoregressive speech recognition
- The combination of sparse CTC checkpoints, FiLM conditioning, and delayed feedback enables shared weights to specialize across recurrent steps
**Limitations**: The abstract does not report limitations of the approach or evaluation constraints.

### Labovich (2026)

**Research question**: Which architectural choices enable looped transformers to extrapolate to harder problems at test time rather than memorize training-specific solutions?
**Methodology**: The author introduces a fixed-point based framework analyzing looped architectures along three stability axes (reachability, input-dependence, geometry), proves theoretical results about fixed points in looped networks with and without recall, and empirically trains single-layer looped transformers on chess, sudoku, and prefix-sums tasks. A novel internal recall placement variant is also introduced and evaluated.
**Key findings**:
- Looped networks without recall have countable fixed points and cannot achieve strong input-dependence at any spectral regime
- Recall combined with outer normalization produces a regime where fixed points are simultaneously reachable, locally smooth in the input, and supported by stable backpropagation
- Downstream performance tracks the framework's predictions across tasks and architectural configurations
- Internal recall becomes competitive with—and on sudoku, substantially better than—standard recall placement when outer normalization is applied
**Limitations**: Not stated in abstract.

### Olausson et al. (2026)

**Research question**: How can diversity across samples be ensured in diffusion language model sampling while maintaining computational efficiency?
**Methodology**: The authors introduce an idealized formal model of fork tokens to study the impact of remasking on expected entropy, then propose using softened, tempered versions of confidence-based remasking heuristics to increase diversity while retaining computational benefits. They empirically evaluate tempered heuristics against existing confidence-based and autoregressive sampling methods.
**Key findings**:
- Tempered heuristics close the exploration gap (pass@k) between existing confidence-based and autoregressive sampling
- Tempered heuristics outperform both methods when controlling for cost (pass@NFE)
- Increased diversity translates to benefits in downstream post-training and test-time compute scaling
- The approach offers simple implementations with retained computational benefits
**Limitations**: Not stated in abstract.

### Rodkin et al. (2025)

**Research question**: How do neural architectures learn and execute multi-step reasoning, and what factors limit reasoning depth beyond memorization?
**Methodology**: The authors use a controlled cellular-automata (1dCA) framework with disjoint training and test rules to exclude memorization, requiring models to infer hidden local rules from short state sequences and chain them to predict multiple future steps. They evaluate LLMs and neural architectures trained from scratch, testing the effects of model depth, recurrence, memory, and test-time compute.
**Key findings**:
- LLMs largely fail to reliably solve a natural-language proxy of the proposed cellular-automata reasoning task
- Most neural architectures trained from scratch can learn rule inference and achieve high next-step accuracy
- Performance drops sharply as the required number of intermediate reasoning steps increases
- Increasing model depth is crucial for extending reasoning capability
- Extending effective depth via recurrence, memory, or test-time compute improves results but remains bounded
**Limitations**: The abstract does not explicitly state limitations, though the controlled 1dCA framework may not fully capture the complexity of real-world multi-step reasoning tasks.

### Sareen et al. (2025)

**Research question**: How can reinforcement learning for LLM fine-tuning be designed to support test-time compute scaling by jointly training reasoners and verifiers?
**Methodology**: The authors propose RL^V, which augments any value-free RL method by jointly training the LLM as both a reasoner and a generative verifier using RL-generated data. The approach is evaluated on MATH benchmarks with parallel sampling and sequential test-time compute scaling, including easy-to-hard and out-of-domain generalization tests.
**Key findings**:
- Prevalent RL methods (GRPO, Leave-one-out PPO) abandon learned value functions, hindering test-time compute scaling that relies on verification
- RL^V boosts MATH accuracy by over 20% with parallel sampling
- RL^V enables 8-32x more efficient test-time compute scaling compared to base RL methods
- RL^V exhibits strong generalization for easy-to-hard and out-of-domain tasks
- RL^V achieves 1.2-1.6x higher performance when jointly scaling parallel and sequential test-time compute with a long reasoning R1 model
**Limitations**: The abstract does not explicitly state limitations, though the approach requires joint training of reasoner and verifier capabilities, which may add complexity to the training pipeline.

### Wang et al. (2025)

**Research question**: How can value models be trained for long-context reasoning traces without requiring fine-grained step definitions, and can value-guided search improve test-time scaling efficiency?
**Methodology**: The authors propose a token-level value model training method that does not require fine-grained step definitions, collecting 2.5 million reasoning traces to train a 1.5B value model, then applying block-wise value-guided search (VGS) with final weighted majority vote to DeepSeek models for test-time compute scaling.
**Key findings**:
- Block-wise VGS with final weighted majority vote achieves better test-time scaling than standard majority voting or best-of-n
- VGS significantly reduces the inference FLOPs required to achieve the same performance as majority voting
- The dataset, model, and codebase are open-sourced
**Limitations**: Not stated in abstract.

### Zhang et al. (2026)

**Research question**: How can test-time compute be selectively scaled for industrial CTR prediction to address unreliable predictions on sparsely observed feature combinations?
**Methodology**: The authors propose UTTSI (Uncertainty-Triggered Test-Time Selective Inference), a training-free model-agnostic framework that uses a dual-signal estimator combining model logit confidence with data-level frequency prior to trigger adaptive feature filtering and stochastic feature-path explorations for uncertain instances. The approach is evaluated on four datasets with three backbone architectures and tested in a seven-day online A/B test.
**Key findings**:
- CTR models suffer from asymmetry: well-represented feature combinations yield confident predictions, while sparsely observed ones produce unreliable outputs
- UTTSI scales inference depth proportionally to per-instance uncertainty while keeping average overhead at approximately 2.8x base model cost
- Experiments on four datasets with three backbones demonstrate consistent, statistically significant gains over all training-phase baselines
- A seven-day online A/B test confirms a 5.3% relative CTR gain (p < 0.01)
- Selective test-time compute allocation serves as a practical complement to training-phase advances for CTR prediction
**Limitations**: The abstract does not explicitly state limitations, though worst-case latency remains unchanged, suggesting potential deployment constraints for real-time systems.

## References

Hamid, J. I., Orney, I. H., Xu, E., Finn, C., & Sadigh, D. (2025). Polychromic objectives for reinforcement learning. arXiv. https://arxiv.org/abs/2509.25424

Hooper, C., Kim, S., Moon, S., Dilmen, K., Maheswaran, M., Lee, N., Mahoney, M. W., Shao, S., Keutzer, K., & Gholami, A. (2025). ETS: Efficient tree search for inference-time scaling. arXiv. https://arxiv.org/abs/2502.13575

Jia, Z. (2026). Port-Hamiltonian latent deliberation: Mitigating the deliberation drift cliff in test-time compute scaling. arXiv. https://arxiv.org/abs/2609.37351

Kaloga, Y., Kumar, S., Sheikh, S. A., Khalil, D., Motlicek, P., & Kodrasi, I. (2026). Test-time compute scaling for ASR with depth-conditioned looped transformers. arXiv. https://arxiv.org/abs/2606.04678

Labovich, A. (2026). Stability and generalization in looped transformers. arXiv. https://arxiv.org/abs/2604.15259

Olausson, T. X., Jazbec, M., Wang, X., Solar-Lezama, A., Naesseth, C. A., Mandt, S., & Nalisnick, E. (2026). A tale of two temperatures: Simple, efficient, and diverse sampling from diffusion language models. arXiv. https://arxiv.org/abs/2604.09921

Rodkin, I., Orel, D., Smirnov, K., Bolatov, A., Elbouardi, B., Hassan, B., Kuratov, Y., Bulatov, A., Nakov, P., Baldwin, T., Shelmanov, A., & Burtsev, M. (2025). Beyond memorization: Extending reasoning depth with recurrence, memory and test-time compute scaling. arXiv. https://arxiv.org/abs/2508.16745

Sareen, K., Moss, M. M., Sordoni, A., Agarwal, R., & Hosseini, A. (2025). Putting the value back in RL: Better test-time scaling by unifying LLM reasoners with verifiers. arXiv. https://arxiv.org/abs/2505.04842

Wang, K., Zhou, J. P., Chang, J., Gao, Z., Kallus, N., Brantley, K., & Sun, W. (2025). Value-guided search for efficient chain-of-thought reasoning. arXiv. https://arxiv.org/abs/2505.17373

Zhang, M., Chen, Y., Jin, Y., Hu, J., Zhang, Y., & Zeng, X. (2026). Selective test-time compute scaling for click-through rate prediction via uncertainty-triggered feature path exploration. arXiv. https://arxiv.org/abs/2605.24989
