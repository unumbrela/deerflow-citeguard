# Systematic Literature Review: Offline Reinforcement Learning

**Date:** October 26, 2026  
**Topic:** Offline Reinforcement Learning  
**Papers Reviewed:** 10  
**Time Window:** Last 2 years (2024-2026)  
**Category:** cs.LG  
**Citation Format:** APA 7th Edition

---

## Executive Summary

Offline reinforcement learning has evolved significantly over the past two years, with research addressing fundamental challenges including distributional shift, data efficiency, generalization, and epistemic uncertainty. This review synthesizes 10 recent papers from arXiv's cs.LG category, revealing six major research themes: (1) addressing out-of-distribution mode averaging in generative policies, (2) adaptive conservatism through uncertainty calibration, (3) data augmentation and small-data learning, (4) policy constraint methods balancing conservatism and performance, (5) zero-shot generalization across environments, and (6) epistemic robustness without large ensembles. The literature demonstrates a shift from static policy deployment toward adaptive priors that support online fine-tuning, with practical emphasis on computational efficiency and sample complexity. Key convergences include the recognition that uniform conservatism is suboptimal, small datasets require specialized regularization, and generalization remains an open theoretical challenge. Notable gaps include limited validation beyond standard benchmarks (D4RL, MuJoCo) and insufficient exploration of discrete action spaces.

---

## Research Themes

### Theme 1: Generative Policy Distillation and Mode Averaging

Recent work addresses the critical problem of Out-of-Distribution (OOD) Mode Averaging in flow-based behavior policies. When distilling multi-modal datasets, standard approaches inadvertently interpolate across behavioral modes, causing action collapse into invalid regions. Jiang et al. (2026) propose Value-Rectified Distillation (VRD), which reformulates policy distillation as value-guided generative trajectory alignment. This theme represents a significant advancement in handling multi-modal, non-expert datasets common in real-world applications.

### Theme 2: Adaptive Conservatism and Uncertainty Calibration

A major convergence across recent literature recognizes that fixed, uniform conservatism penalties are suboptimal. Traditional offline RL methods apply identical penalties across all states regardless of local data coverage. Upadhyay (2026) introduces UNIQ, which uses conformal prediction to compute state-adaptive uncertainty estimates, relaxing conservatism in well-covered regions while strengthening it near data frontiers. This approach achieves 10x memory reduction compared to ensemble-based methods like EDAC while maintaining competitive performance.

### Theme 3: Data Augmentation and Small-Data Learning

Multiple papers address the gap between benchmark datasets (often 1M+ transitions) and real-world applications with limited data. Arnob et al. (2025) demonstrate that offline RL algorithms overfit on small datasets and propose Sparse-Reg, a sparsity-based regularization technique. Schmähling et al. (2026) introduce trajectory-level augmentation exploiting geometric relationships between rewards and value functions. Cao et al. (2025) present adversarial data augmentation in model-based RL, dynamically selecting ensemble models to expand training data without rollout horizon tuning.

### Theme 4: Policy Constraint Methods

The tension between conservatism and performance drives innovation in policy constraints. Gao et al. (2025) propose Only Support Constraint (OSC), which restricts policies to the behavior policy's support without imposing extra constraints on in-support actions. Using diffusion models to characterize support boundaries, OSC significantly outperforms prior policy constraint methods while mitigating excessive conservatism that prevents surpassing behavior policy performance.

### Theme 5: Zero-Shot Generalization

Generalization to unseen environments remains a fundamental challenge. Wang et al. (2025) show that classical offline RL fails to generalize to new environments and propose pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO). Their theoretical results establish the first foundation for understanding zero-shot generalization in offline RL, demonstrating that pessimistic policy evaluation can guide learning toward policies that transfer across environments.

### Theme 6: Epistemic Robustness Without Ensembles

Ensemble-based methods for epistemic uncertainty require large ensembles and conflate epistemic with aleatoric uncertainty. Chenreddy and Delage (2026) propose replacing discrete ensembles with compact uncertainty sets over Q-values, achieving improved robustness across tabular and continuous domains. This unified framework addresses limitations of SAC-N and similar approaches while introducing a benchmark for risk-sensitive behavior policy evaluation.

### Theme 7: From Static Deployment to Adaptive Priors

A paradigm shift emerges in how offline RL objectives are conceptualized. Ni et al. (2026) argue that offline RL should prioritize learning adaptive policy priors—policies preserving capacity for improvement during subsequent online interaction—rather than static deployment. This position paper formalizes adaptive offline RL (AORL) and proposes Bayesian offline RL as a principled direction for preserving epistemic uncertainty over plausible environments.

### Theme 8: Theoretical Foundations in Large State Spaces

Jiang and Xie (2025) provide a comprehensive survey of offline RL theory in large state spaces, mapping the landscape of algorithms based on expressivity assumptions (Bellman completeness vs. realizability) and data coverage requirements (all-policy vs. single-policy). This theoretical work clarifies what sample and computational complexity guarantees are achievable under different assumptions.

---

## Per-Paper Annotations

### Paper 1: Value-Rectified Distillation for Flow-based Offline Reinforcement Learning

**Citation:** Jiang, K., Jiang, W., Kawahara, Y., & Tan, X. (2026). Value-Rectified Distillation for Flow-based Offline Reinforcement Learning. *arXiv preprint arXiv:2610.29075*.

**Research Question:** How can we address the Out-of-Distribution Mode Averaging problem that occurs when distilling Flow Matching based behavior policies in offline reinforcement learning?

**Methodology:** The authors propose Value-Rectified Distillation (VRD), a framework that reformulates offline policy distillation as a value-guided generative trajectory alignment problem using a dynamic coupling mechanism. They instantiate VRD through two algorithms: VRD-Q (value-quantile behavior distillation to filter low-value behaviors) and VRD-R (latent space reorganization to geometrically isolate high-value trajectories).

**Key Findings:**
- VRD actively rectifies flow dynamics to explicitly decouple distinct behavioral modes, preventing action collapse into invalid OOD regions
- The framework cleanly isolates high-value actions from multi-modal datasets
- VRD improves existing generative baselines across diverse continuous control and planning tasks
- Performance gains are especially pronounced on multi-modal, non-expert datasets
- Empirical validation spans D4RL, OGBench, and Minari benchmarks

**Limitations:** Evaluation is limited to continuous control and planning tasks on specific benchmarks; the approach may not generalize to discrete action spaces or other RL domains beyond the tested environments.

---

### Paper 2: Trajectory-Level Data Augmentation for Offline Reinforcement Learning

**Citation:** Schmähling, T., Burkhardt, M., & Windisch, T. (2026). Trajectory-Level Data Augmentation for Offline Reinforcement Learning. *arXiv preprint arXiv:2605.13401*.

**Research Question:** How can we effectively train off-policy models from a limited number of suboptimal trajectories in offline reinforcement learning?

**Methodology:** The authors introduce a trajectory-based augmentation technique that exploits task structure and the geometric relationship between rewards, value functions, and mathematical properties of logging policies. The approach supports suboptimal logging policies during data collection to improve data quality.

**Key Findings:**
- Trajectory-level augmentation enables training from limited suboptimal trajectories
- The method supports suboptimal logging policies during data collection, leading to higher data quality
- Theoretical justification is provided for the augmentation strategies
- Empirical validation shows improved offline RL performance across positioning tasks
- The approach works under varying dimensionality and partial observability conditions

**Limitations:** The method is motivated by and validated primarily on active positioning problems; generalization to other task domains beyond positioning tasks remains unexplored.

---

### Paper 3: Provable Zero-Shot Generalization in Offline Reinforcement Learning

**Citation:** Wang, Z., Yang, C., Lui, J. C. S., & Zhou, D. (2025). Provable Zero-Shot Generalization in Offline Reinforcement Learning. *arXiv preprint arXiv:2503.07988*.

**Research Question:** How can an agent trained on offline data from multiple environments achieve zero-shot generalization to unseen test environments without further interaction?

**Methodology:** The authors propose two algorithms: pessimistic empirical risk minimization (PERM) and pessimistic proximal policy optimization (PPPO), both leveraging pessimistic policy evaluation to guide policy learning and enhance generalization across environments.

**Key Findings:**
- Classical offline RL methods fail to generalize to new, unseen environments
- Both PERM and PPPO can find near-optimal policies with zero-shot generalization property
- Pessimistic policy evaluation effectively guides policy learning for enhanced generalization
- This work provides the first theoretical understanding of the generalization phenomenon in offline RL
- The results establish a foundation for understanding zero-shot generalization in offline settings

**Limitations:** This work represents a first step in understanding generalization in offline RL; the theoretical results may rely on assumptions that limit practical applicability, and empirical validation scope is not extensively detailed.

---

### Paper 4: Sparse-Reg: Improving Sample Complexity in Offline Reinforcement Learning using Sparsity

**Citation:** Arnob, S. Y., Fujimoto, S., & Precup, D. (2025). Sparse-Reg: Improving Sample Complexity in Offline Reinforcement Learning using Sparsity. *arXiv preprint arXiv:2506.17155*.

**Research Question:** How can we prevent overfitting in offline reinforcement learning when working with considerably smaller datasets than typical benchmarks?

**Methodology:** The authors introduce Sparse-Reg, a regularization technique based on sparsity designed to mitigate overfitting in offline RL, enabling effective learning in limited data settings.

**Key Findings:**
- Offline RL algorithms overfit on small datasets, resulting in poor performance
- Many offline RL applications rely on datasets considerably smaller than the million+ data points in common benchmarks
- Sparse-Reg enables effective learning in limited data settings
- The method outperforms state-of-the-art baselines in continuous control tasks
- Sparsity-based regularization addresses the sample complexity challenge in small-data offline RL

**Limitations:** The focus is primarily on small dataset scenarios; evaluation is concentrated on continuous control tasks, and applicability to other RL domains or larger datasets is not thoroughly explored.

---

### Paper 5: UNIQ: Conformal Calibration for Adaptive Conservatism in Offline Reinforcement Learning

**Citation:** Upadhyay, A. (2026). UNIQ: Conformal Calibration for Adaptive Conservatism in Offline Reinforcement Learning. *arXiv preprint arXiv:2606.07592*.

**Research Question:** How can offline RL apply state-adaptive conservatism instead of fixed uniform penalties across all states regardless of local data coverage?

**Methodology:** UNIQ (Uncertainty-Informed Quantile) is built on the IQL backbone and trains a multi-expectile value ensemble, computes distribution-free uncertainty estimates using split conformal prediction, and maps the uncertainty signal to a state-dependent expectile that adjusts conservatism based on data coverage.

**Key Findings:**
- UNIQ introduces state-adaptive conservatism through conformally calibrated uncertainty estimation
- The method relaxes conservatism in well-covered regions while strengthening it in uncertain regions near the data frontier
- UNIQ consistently improves over IQL on D4RL MuJoCo benchmarks, with largest gains on Walker2d and replay-heavy tasks
- Memory cost is approximately 250 MB peak VRAM, providing roughly 10x reduction compared to EDAC
- The approach improves the performance-efficiency trade-off in offline reinforcement learning

**Limitations:** UNIQ is positioned as a practical mechanism contribution rather than pursuing overall state-of-the-art performance; evaluation is primarily on D4RL MuJoCo benchmarks, and generalization to other domains is not extensively validated.

---

### Paper 6: From Static Policies to Adaptive Priors in Offline Reinforcement Learning

**Citation:** Ni, T., Jain, V., Karthikeyan, A., & Bacon, P.-L. (2026). From Static Policies to Adaptive Priors in Offline Reinforcement Learning. *arXiv preprint arXiv:2609.35880*.

**Research Question:** How should offline RL be reformulated when offline-trained policies are subsequently updated through online interaction rather than deployed statically?

**Methodology:** Position paper that formalizes adaptive offline reinforcement learning (AORL), distinguishes it from offline-to-online RL, and proposes Bayesian offline RL as a principled direction for constructing adaptive policy priors that preserve epistemic uncertainty.

**Key Findings:**
- Offline RL objective should extend beyond immediate deployment to prioritize learning adaptive policy priors with capacity for improvement during subsequent interaction
- Adaptability becomes critical under distributional shift, limited dataset coverage, and changing test-time conditions
- Bayesian offline RL can preserve epistemic uncertainty over plausible environments, enabling better test-time adaptation
- Offline RL should be treated as preparation for future experience rather than as a static deployment problem

**Limitations:** This is a position paper outlining conceptual frameworks and research directions rather than presenting empirical validation; open challenges remain for practically implementing adaptive policy priors.

---

### Paper 7: Offline Reinforcement Learning in Large State Spaces: Algorithms and Guarantees

**Citation:** Jiang, N., & Xie, T. (2025). Offline Reinforcement Learning in Large State Spaces: Algorithms and Guarantees. *arXiv preprint arXiv:2510.04088*.

**Research Question:** What are the theoretical foundations, algorithms, and guarantees for offline reinforcement learning in large state spaces?

**Methodology:** Survey article introducing theory covering expressivity assumptions on function approximation (Bellman completeness vs. realizability) and data coverage requirements (all-policy vs. single-policy coverage), mapping the landscape of algorithms under different assumptions.

**Key Findings:**
- Different expressivity assumptions on function approximation lead to distinct algorithmic approaches and theoretical guarantees
- Data coverage requirements (all-policy vs. single-policy) fundamentally affect what sample and computational complexity guarantees are achievable
- Rich landscape of algorithms exists depending on which assumptions one is willing to make
- Important connections exist between offline RL theory and adjacent research areas

**Limitations:** As a survey article, it synthesizes existing work rather than proposing new algorithms; theoretical guarantees depend on assumptions that may not hold in practical applications.

---

### Paper 8: Policy Constraint by Only Support Constraint for Offline Reinforcement Learning

**Citation:** Gao, Y., Guo, J., Wu, F., & Zhang, R. (2025). Policy Constraint by Only Support Constraint for Offline Reinforcement Learning. *arXiv preprint arXiv:2503.05207*.

**Research Question:** How can policy constraint methods reduce excessive conservatism while still addressing distributional shift in offline RL?

**Methodology:** Proposes Only Support Constraint (OSC) derived from maximizing total probability of learned policy within the behavior policy's support, using a diffusion model to effectively characterize the support of behavior policies.

**Key Findings:**
- OSC presents a regularization term that restricts policies to the support without imposing extra constraints on actions within the support
- Diffusion model effectively characterizes the support of behavior policies for constraint enforcement
- Significantly enhances performance across various offline RL benchmarks compared to existing policy constraint methods
- Successfully alleviates distributional shift challenges while mitigating excessive conservatism of prior policy constraint approaches

**Limitations:** Requires diffusion model for support characterization which adds complexity; evaluation limited to standard offline RL benchmarks without demonstration on real-world tasks.

---

### Paper 9: Epistemic Robust Offline Reinforcement Learning

**Citation:** Chenreddy, A. R., & Delage, E. (2026). Epistemic Robust Offline Reinforcement Learning. *arXiv preprint arXiv:2604.07072*.

**Research Question:** How can offline RL better handle epistemic uncertainty from limited or biased data coverage without relying on large ensembles?

**Methodology:** Proposes unified framework replacing discrete ensembles with compact uncertainty sets over Q-values, and introduces a benchmark for evaluating offline RL algorithms under risk-sensitive behavior policies.

**Key Findings:**
- Compact uncertainty sets over Q-values provide unified and generalizable alternative to discrete ensemble methods
- Achieves improved robustness and generalization over ensemble-based baselines (e.g., SAC-N) across both tabular and continuous state domains
- Avoids conflation of epistemic with aleatoric uncertainty that plagues ensemble-based approaches
- New benchmark enables evaluation of offline RL algorithms under risk-sensitive behavior policies

**Limitations:** Requires further validation on additional real-world benchmarks; uncertainty set construction may have computational considerations not fully explored.

---

### Paper 10: Model-Based Offline Reinforcement Learning with Adversarial Data Augmentation

**Citation:** Cao, H., Feng, F., Huo, J., Yang, S., Fang, M., Yang, T., & Gao, Y. (2025). Model-Based Offline Reinforcement Learning with Adversarial Data Augmentation. *arXiv preprint arXiv:2503.20285*.

**Research Question:** How can model-based offline RL develop robust policies from static data without requiring rollout horizon tuning?

**Methodology:** Introduces MORAL framework employing adversarial data augmentation with alternating sampling from ensemble models, integrating a differential factor for regularization to minimize extrapolation errors.

**Key Findings:**
- Adversarial process dynamically selects ensemble models against policy for biased sampling, mitigating optimistic estimation of fixed models
- Robustly expands training data for policy optimization without requiring rollout horizon tuning
- Differential factor regularization ensures error minimization in extrapolations
- Outperforms other model-based offline RL methods on D4RL benchmark in terms of policy learning and sample efficiency
- Shows remarkable applicability across diverse offline tasks without task-specific tuning

**Limitations:** Evaluation primarily on D4RL benchmarks; adversarial sampling process introduces additional computational overhead compared to standard model-based approaches.

---

## Convergences and Disagreements

### Convergences

1. **Adaptive Conservatism:** Multiple papers converge on the insight that uniform conservatism is suboptimal. Both UNIQ (Upadhyay, 2026) and OSC (Gao et al., 2025) advocate for state-dependent or support-aware constraint mechanisms rather than fixed penalties.

2. **Small-Data Challenges:** Three papers independently address the gap between benchmark datasets and real-world applications (Arnob et al., 2025; Schmähling et al., 2026; Cao et al., 2025), converging on the need for specialized regularization and augmentation techniques.

3. **Beyond Static Deployment:** The shift from viewing offline RL as static policy deployment toward adaptive preparation for online interaction appears in both the AORL position paper (Ni et al., 2026) and the generalization work (Wang et al., 2025).

4. **Ensemble Alternatives:** Both UNIQ and the epistemic robustness work (Chenreddy & Delage, 2026) propose alternatives to large ensembles, converging on compact uncertainty representations for efficiency.

### Disagreements

1. **Pessimism vs. Adaptivity:** While Wang et al. (2025) emphasize pessimistic policy evaluation for generalization, Upadhyay (2026) and Gao et al. (2025) advocate for adaptive mechanisms that relax conservatism in well-covered regions. This tension between pessimism and adaptivity remains unresolved.

2. **Model-Based vs. Model-Free:** The literature includes both model-based approaches (Cao et al., 2025) and model-free methods (most others), with no clear convergence on which paradigm dominates for specific scenarios.

---

## Research Gaps

1. **Limited Benchmark Diversity:** Nearly all empirical validation relies on D4RL, MuJoCo, OGBench, and Minari benchmarks. Real-world applications beyond simulated continuous control remain underexplored.

2. **Discrete Action Spaces:** Most papers focus on continuous control tasks. Offline RL for discrete action spaces receives minimal attention in this set.

3. **Computational Overhead:** Several methods (diffusion models in OSC, adversarial sampling in MORAL, multi-expectile ensembles in UNIQ) introduce computational costs that are acknowledged but not thoroughly analyzed.

4. **Theoretical-Practical Gap:** Theoretical results (Wang et al., 2025; Jiang & Xie, 2025) rely on assumptions that may not hold in practice, and empirical papers often lack theoretical grounding.

5. **Generalization Validation:** While generalization is a stated goal (Wang et al., 2025), most papers do not test on genuinely unseen environments or distribution shifts beyond standard benchmark splits.

6. **Human-in-the-Loop:** None of the reviewed papers address offline RL with human preference data or human-in-the-loop scenarios, despite growing interest in RLHF.

---

## Methodology

This systematic literature review followed a structured methodology:

1. **Search Strategy:** Queried arXiv's cs.LG category using the phrase "offline reinforcement learning" with relevance-based sorting and a 2-year time window (October 2024 - October 2026).

2. **Selection Criteria:** Retrieved the top 10 most relevant papers matching the query. All papers were peer-reviewed preprints focused on offline RL algorithms, theory, or methodology.

3. **Data Extraction:** Structured metadata (research question, methodology, key findings, limitations) was extracted from each paper's abstract using parallel subagent processing.

4. **Synthesis:** Thematic analysis identified recurring research directions, convergences, disagreements, and gaps across the literature set.

5. **Citation Format:** APA 7th Edition format was applied throughout, with arXiv preprints cited as `arXiv:XXXX.XXXXX`.

---

## References

Arnob, S. Y., Fujimoto, S., & Precup, D. (2025). Sparse-Reg: Improving sample complexity in offline reinforcement learning using sparsity. *arXiv preprint arXiv:2506.17155*. https://arxiv.org/abs/2506.17155

Cao, H., Feng, F., Huo, J., Yang, S., Fang, M., Yang, T., & Gao, Y. (2025). Model-based offline reinforcement learning with adversarial data augmentation. *arXiv preprint arXiv:2503.20285*. https://arxiv.org/abs/2503.20285

Chenreddy, A. R., & Delage, E. (2026). Epistemic robust offline reinforcement learning. *arXiv preprint arXiv:2604.07072*. https://arxiv.org/abs/2604.07072

Gao, Y., Guo, J., Wu, F., & Zhang, R. (2025). Policy constraint by only support constraint for offline reinforcement learning. *arXiv preprint arXiv:2503.05207*. https://arxiv.org/abs/2503.05207

Jiang, K., Jiang, W., Kawahara, Y., & Tan, X. (2026). Value-rectified distillation for flow-based offline reinforcement learning. *arXiv preprint arXiv:2610.29075*. https://arxiv.org/abs/2610.29075

Jiang, N., & Xie, T. (2025). Offline reinforcement learning in large state spaces: Algorithms and guarantees. *arXiv preprint arXiv:2510.04088*. https://arxiv.org/abs/2510.04088

Ni, T., Jain, V., Karthikeyan, A., & Bacon, P.-L. (2026). From static policies to adaptive priors in offline reinforcement learning. *arXiv preprint arXiv:2609.35880*. https://arxiv.org/abs/2609.35880

Schmähling, T., Burkhardt, M., & Windisch, T. (2026). Trajectory-level data augmentation for offline reinforcement learning. *arXiv preprint arXiv:2605.13401*. https://arxiv.org/abs/2605.13401

Upadhyay, A. (2026). UNIQ: Conformal calibration for adaptive conservatism in offline reinforcement learning. *arXiv preprint arXiv:2606.07592*. https://arxiv.org/abs/2606.07592

Wang, Z., Yang, C., Lui, J. C. S., & Zhou, D. (2025). Provable zero-shot generalization in offline reinforcement learning. *arXiv preprint arXiv:2503.07988*. https://arxiv.org/abs/2503.07988

---

## Appendix: Search Parameters

- **Query:** "offline reinforcement learning"
- **Category:** cs.LG (Machine Learning)
- **Time Window:** October 26, 2024 - October 26, 2026 (2 years)
- **Sort Strategy:** Relevance (BM25-style scoring)
- **Papers Retrieved:** 10
- **Citation Style:** APA 7th Edition
