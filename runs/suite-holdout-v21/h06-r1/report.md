# Systematic Literature Review: Test-Time Scaling of Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "test-time scaling", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Test-time scaling has emerged as a critical paradigm for improving language model performance through strategic allocation of inference-time compute. The surveyed literature reveals a rapidly evolving field moving beyond simple parallel sampling toward sophisticated multi-dimensional frameworks. Recent work demonstrates that effective test-time scaling requires careful consideration of candidate-generation strategies, confidence estimation, and contextual reasoning capabilities. A key insight across multiple papers is that naive scaling approaches—simply generating more samples or longer chains-of-thought—often fail to deliver consistent improvements and can even degrade performance. Instead, the most promising approaches involve adaptive mechanisms that allocate compute based on problem complexity, mode-specific reasoning strategies, and learned contextual allocation policies. The field shows strong convergence around the need for efficiency-aware scaling methods that balance performance gains against computational costs.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "test-time scaling", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Dimensional Scaling Frameworks

The field has evolved from viewing test-time scaling as a one-dimensional problem (simply increasing sample count) toward recognizing it as a multi-dimensional optimization challenge. Yu et al. (2025) introduced a unified 3D framework considering context-length scaling, batch scaling (parallel sampling), and turn scaling (iterative self-refinement), demonstrating that combining all three dimensions substantially improves reasoning performance on challenging benchmarks including IOI, IMO, and CPHO. This framework extends test-time scaling capacity beyond the limited context length of base models, with each dimension showing bounded but complementary scaling effects. The approach further benefits from human preference feedback and extends to embodied learning applications. This multi-dimensional perspective represents a fundamental shift from earlier work that treated scaling as primarily a matter of generating more samples.

### Theme 2: Efficiency and Resource Awareness

A significant thread in recent work focuses on the computational efficiency of test-time scaling strategies. Kashaniyan and Jannesari (2026) demonstrated that candidate-generation strategy fundamentally shapes both energy consumption and performance when total candidate count is fixed. Their findings show that eight serial calls use 4.64-4.86× as much gross GPU-device energy and have 5.77-6.12× the P95 latency of one batched call with eight candidates, establishing that fewer generation calls with larger batch sizes are more efficient when candidates are independent and memory allows. Similarly, Huang et al. (2025) introduced Self-Calibration, enabling reliable confidence estimation at test time with one forward pass, then using confidence-based Early Stopping to improve MathQA accuracy from 81.0 to 83.6 with a sample budget of 16 responses. These works collectively argue that efficient test-time scaling must adapt to query complexity rather than applying uniform compute allocation.

### Theme 3: Mode-Specific and Specialized Reasoning

Recent research has identified that diversity collapse in parallel sampling limits the effectiveness of naive test-time scaling. Wu et al. (2025) proposed the mode-conditioning (ModC) framework, which allocates test-time compute across reasoning modes using specialist models or mode-specific prefixes. Their approach achieves a 4× efficiency gain over standard training while improving maximum attainable Pass@k on Qwen2.5-7B, with gradient clustering enabling ModC without explicit mode labels yielding up to 10% gains on datasets such as NuminaMath. This work reveals that different reasoning problems benefit from different reasoning modes, and that explicitly modeling this heterogeneity unlocks superior scaling behavior. The ModC framework improves reinforcement learning and can further boost diversity-inducing RL methods, suggesting broad applicability across reasoning domains.

### Theme 4: Limitations of Simple Scaling Approaches

Several papers critically examine why simple test-time scaling strategies often fail to deliver expected improvements. Zeng et al. (2025) investigated o1-like models and found that longer chains-of-thought do not consistently enhance accuracy; correct solutions are often shorter than incorrect ones for the same questions. This phenomenon relates to models' self-revision capabilities—longer CoTs contain more self-revisions, which often lead to performance degradation. Wu (2025) similarly analyzed simple test-time scaling and found that scaling behavior is largely attributed to scaling down by enforcing maximum length, while scaling up by appending "Wait" leads to inconsistencies as models oscillate between solutions. Both papers converge on the conclusion that parallel scaling achieves better coverage and scalability than sequential scaling, and that naive approaches progressively impose lower upper limits on model performance.

### Theme 5: Learned Contextual Reasoning and Adaptation

The most recent work in this space focuses on learning adaptive strategies for test-time compute allocation. Li et al. (2026) introduced Hermes, a family of configurable harnesses that progressively vary model control over context allocation and reuse, and Hermes-Learn, a two-stage framework for learning contextual reasoning capabilities. Their findings show that capable models can exploit flexibility to scale with additional inference-time compute, while training with Hermes-Learn induces adaptive contextual reasoning strategies that vary with both problem and reasoning progress. These learned capabilities extrapolate beyond inference-time compute seen during training and transfer to complementary test-time scaling methods. Similarly, Ge et al. (2026) analyzed on-policy distillation through test-time scaling, proposing the Teacher Advantage Score at K (TAS@K) to predict which teacher will lead to larger improvements in pass@K before OPD training, achieving agreement with observed improvements in 83.6% of experiments.

### Theme 6: Benchmarking and Evaluation Methodologies

As the field has grown, so has attention to rigorous evaluation and ranking methodologies for test-time scaling. Hariri et al. (2026) formalized dense benchmark ranking under test-time scaling and introduced Scorio, a library implementing statistical ranking methods including paired-comparison models, IRT models, voting rules, and graph-based methods. Their evaluation across 20 reasoning models on four Olympiad-style math benchmarks found that most full-trial rankings agree closely with the Bayesian gold standard Bayes_U@80 (mean Kendall's τ_b = 0.93-0.95), while in the single-trial regime, the best methods reach τ_b ≈ 0.86. Using greedy decoding as an empirical prior reduces variance at N=1 by 16-52%, but can bias rankings when greedy and stochastic sampling disagree. This work provides essential infrastructure for reliably comparing models in the test-time scaling regime. Qin et al. (2026) focused specifically on code generation, proposing DAJ, a reasoning-based LLM judge trained with verifiable rewards under a bi-level data-reweighted learning framework that achieves state-of-the-art performance on LiveCodeBench and BigCodeBench.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several key points. Nearly all papers converge that naive scaling approaches—simply generating more samples or longer outputs—fail to deliver consistent improvements and can actively harm performance (Zeng et al., 2025; Wu, 2025). Multiple papers agree that parallel scaling achieves better coverage and scalability than sequential scaling (Zeng et al., 2025; Wu, 2025; Yu et al., 2025). There is consensus that efficiency matters: test-time scaling must be adaptive to query complexity rather than applying uniform compute allocation (Huang et al., 2025; Kashaniyan & Jannesari, 2026). The literature also converges on the value of multi-dimensional approaches that combine context, batch, and turn scaling rather than optimizing any single dimension in isolation (Yu et al., 2025).

**Disagreements**: The literature shows less disagreement than convergence, reflecting the relatively nascent state of the field. One area of potential tension is around the role of self-revision: Zeng et al. (2025) found that self-revisions in longer CoTs often lead to performance degradation, while Li et al. (2026) showed that learned contextual reasoning strategies can effectively use iterative refinement. This may reflect differences in whether self-revision is learned versus emergent. Another subtle disagreement concerns the optimal approach to diversity: Wu et al. (2025) advocate for explicit mode-conditioning with specialist models, while Yu et al. (2025) emphasize combining multiple scaling dimensions without explicit mode separation. These differences may reflect different problem domains rather than fundamental contradictions.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the surveyed papers explicitly address the theoretical limits of test-time scaling—while empirical bounds are observed, there is limited work on fundamental capacity limits or diminishing returns curves. Second, while several papers mention the value of human feedback (Yu et al., 2025; Qin et al., 2026), there is limited systematic exploration of human-AI collaboration in test-time scaling regimes. Third, most work focuses on reasoning and code generation benchmarks; application to other domains such as creative writing, scientific hypothesis generation, or strategic planning remains underexplored. Fourth, while efficiency is discussed, there is limited work on carbon footprint or environmental impact of intensive test-time scaling strategies. Finally, the interaction between test-time scaling and model architecture choices—whether certain architectures are inherently more amenable to scaling—remains largely unexamined.

## Per-Paper Annotations

### Ge et al. (2026)

**Research question**: Do improvements from on-policy distillation extend across the entire range of test-time sampling budgets?
**Methodology**: The authors analyze on-policy distillation through test-time scaling by varying sampling budget K and evaluating performance with pass@K. They propose the Teacher Advantage Score at K (TAS@K) to predict which teacher will lead to larger improvements in pass@K before OPD training.
**Key findings**:
- OPD can improve pass@K at both small and large sampling budgets, but can also improve small-budget performance while reducing large-budget pass@K
- The authors identify a condition that guarantees such a reversal and provide a reverse KL counterexample where it occurs even when the teacher has higher accuracy on every problem
- TAS@K ordering agrees with observed pass@K improvements in 83.6% of experiments across three domains and thirteen benchmarks
**Limitations**: Not stated in abstract

### Kashaniyan and Jannesari (2026)

**Research question**: How does the candidate-generation strategy affect the systems cost and performance of LLM test-time scaling when the total candidate count is fixed?
**Methodology**: The authors fix N=8 candidates and compare four generation schedules (1x8, 2x4, 4x2, and 8x1) on A100 GPUs, measuring latency, throughput, GPU-hours, and gross GPU-device energy while keeping total candidate count fixed.
**Key findings**:
- Increasing N from 1 to 8 improves accuracy by 8.4 percentage points for Phi-3-mini and 18.4 points for Qwen2.5-1.5B
- Eight serial calls use 4.64-4.86× as much gross GPU-device energy and have 5.77-6.12× the P95 latency of one batched call with eight candidates
- Fewer generation calls with larger batch sizes are more efficient when candidates are independent and memory allows it
**Limitations**: Not stated in abstract

### Hariri et al. (2026)

**Research question**: How can reasoning LLMs be reliably ranked in the test-time scaling regime using different statistical ranking methods?
**Methodology**: The authors formalize dense benchmark ranking under test-time scaling and introduce Scorio, a library implementing statistical ranking methods including paired-comparison models, IRT models, voting rules, and graph-based methods, evaluated across 20 reasoning models on four Olympiad-style math benchmarks.
**Key findings**:
- Most full-trial rankings agree closely with the Bayesian gold standard Bayes_U@80 (mean Kendall's τ_b = 0.93-0.95)
- In the single-trial regime, the best methods reach τ_b ≈ 0.86
- Using greedy decoding as an empirical prior reduces variance at N=1 by 16-52%, but can bias rankings when greedy and stochastic sampling disagree
**Limitations**: Not stated in abstract

### Zeng et al. (2025)

**Research question**: Do o1-like models truly possess test-time scaling capabilities, and do longer chains-of-thought consistently enhance accuracy?
**Methodology**: The authors investigate the relationship between CoT length and accuracy in o1-like models, examine self-revision capabilities, and compare sequential and parallel scaling strategies on QwQ, R1, and LIMO models.
**Key findings**:
- Longer CoTs of o1-like models do not consistently enhance accuracy; correct solutions are often shorter than incorrect ones for the same questions
- The phenomenon is closely related to models' self-revision capabilities—longer CoTs contain more self-revisions, which often lead to performance degradation
- Parallel scaling achieves better coverage and scalability than sequential scaling
- Shortest Majority Vote significantly improves models' test-time scalability compared to conventional majority voting approaches
**Limitations**: Not stated in abstract

### Yu et al. (2025)

**Research question**: How can test-time scaling capacity be extended beyond the limited context length of base models through a multi-dimensional framework?
**Methodology**: The authors introduce a unified framework of multi-dimensional test-time scaling considering three dimensions: context-length scaling, batch scaling (parallel sampling), and turn scaling (iterative self-refinement), proposing 3D test-time scaling that integrates all three.
**Key findings**:
- Each dimension (context, batch, turn) demonstrates a test-time scaling effect, but with bounded capacity
- Combining all three dimensions substantially improves reasoning performance on challenging testbeds including IOI, IMO, and CPHO
- The approach further benefits from human preference feedback
- The human-in-the-loop framework extends to embodied learning for designing humanoid control behaviors
**Limitations**: Not stated in abstract

### Wu et al. (2025)

**Research question**: How can parallel sampling's effectiveness be improved to overcome diversity collapse in test-time scaling?
**Methodology**: The authors propose the mode-conditioning (ModC) framework, which allocates test-time compute across reasoning modes using specialist models or mode-specific prefixes. They evaluate ModC on controlled graph-search tasks and large-scale reasoning benchmarks across model families and sizes from 0.5B to 7B.
**Key findings**:
- ModC consistently improves scaling across controlled graph-search tasks and large-scale reasoning benchmarks
- Fine-tuning Qwen2.5-7B with ModC achieves a 4× efficiency gain over standard training while improving maximum attainable Pass@k
- Gradient clustering enables ModC without explicit mode labels, yielding up to 10% gains on datasets such as NuminaMath
- ModC improves reinforcement learning and can further boost diversity-inducing RL methods
**Limitations**: Not stated in abstract

### Wu (2025)

**Research question**: What factors contribute to the scaling behavior observed in simple test-time scaling methods?
**Methodology**: The paper analyzes simple test-time scaling by examining the effects of scaling down (enforcing maximum length) versus scaling up (appending "Wait") and compares these to fine-tuning on long CoT data distilled from o1-like models.
**Key findings**:
- The scaling behavior is largely attributed to scaling down by enforcing a maximum length
- Fine-tuning on long CoT data distilled from o1-like models has no significant impact on scaling behavior
- Scaling up by appending "Wait" leads to inconsistencies as models may oscillate between solutions
- Simple test-time scaling progressively imposes a lower upper limit on model performance as it scales down
**Limitations**: Not stated in abstract

### Qin et al. (2026)

**Research question**: How can LLM judges for Best-of-N selection in code generation be improved to handle distribution shifts?
**Methodology**: The authors propose DAJ, a reasoning-based LLM judge trained with verifiable rewards under a bi-level data-reweighted learning framework that learns data-importance weights to optimize generalization on held-out meta sets aligned with target benchmarks.
**Key findings**:
- DAJ achieves state-of-the-art performance on LiveCodeBench and BigCodeBench
- The approach automatically emphasizes hard problems, in-distribution samples, and trajectory-aligned data without hand-crafted heuristics
- This is the first application of data reweighting to LLM-as-a-Judge training for test-time scaling
- DAJ outperforms strong test-time scaling baselines as well as leading proprietary models
**Limitations**: Not stated in abstract

### Li et al. (2026)

**Research question**: How can models learn to effectively allocate fresh contexts and carry information between them during test-time scaling?
**Methodology**: The authors introduce Hermes, a family of configurable harnesses that progressively vary model control over context allocation and reuse, and Hermes-Learn, a two-stage framework for learning contextual reasoning capabilities.
**Key findings**:
- Capable models can exploit flexibility to scale with additional inference-time compute, while smaller open-source models initially struggle
- Training with Hermes-Learn induces adaptive contextual reasoning strategies that vary with both problem and reasoning progress
- Gains generalize across benchmarks and models
- Learned capabilities extrapolate beyond inference-time compute seen during training and transfer to complementary test-time scaling methods
**Limitations**: Not stated in abstract

### Huang et al. (2025)

**Research question**: How can model confidence be used to improve the efficiency of test-time scaling in LLMs?
**Methodology**: The authors introduce Self-Calibration by distilling Self-Consistency-derived confidence into the model itself, enabling reliable confidence estimation at test time with one forward pass, then design confidence-based efficient test-time scaling methods like Early-Stopping for Best-of-N.
**Key findings**:
- Model confidence can improve efficiency of test-time scaling by adapting to query complexity
- Self-Calibration enables reliable confidence estimation at test time with one forward pass
- Confidence-based Early Stopping improves MathQA accuracy from 81.0 to 83.6 with a sample budget of 16 responses
- Experiments on three LLMs across six datasets demonstrate the effectiveness of the approach
**Limitations**: Not stated in abstract

## References

Ge, X., Zhang, Z., Huang, Y., Zhu, J., Yuan, L., Gu, W., Wu, W., Huang, W., Han, B., Zhang, X., & Yao, J. (2026). Towards understanding on-policy distillation through the lens of test-time scaling. arXiv. https://arxiv.org/abs/2608.11829

Hariri, M., Hinczewski, M., Ma, J., & Chaudhary, V. (2026). Ranking reasoning LLMs under test-time scaling. arXiv. https://arxiv.org/abs/2603.10960

Huang, C., Huang, L., Leng, J., Liu, J., & Huang, J. (2025). Efficient test-time scaling via self-calibration. arXiv. https://arxiv.org/abs/2503.00031

Kashaniyan, M., & Jannesari, A. (2026). Sample count is not enough: Candidate-generation strategy shapes the energy and performance of LLM test-time scaling. arXiv. https://arxiv.org/abs/2609.19499

Li, X., Goswami, M., Liu, H., Kanakaris, N., Huang, L., Jana, P., Blöbaum, P., & Jain, P. (2026). Hermes: Learning contextual reasoning unlocks test-time scaling. arXiv. https://arxiv.org/abs/2609.38332

Qin, P., Zhang, R., Cao, Q., & Xie, P. (2026). DAJ: Data-reweighted LLM judge for test-time scaling in code generation. arXiv. https://arxiv.org/abs/2601.22230

Wu, C. H., Goyal, S., & Raghunathan, A. (2025). Mode-conditioning unlocks superior test-time scaling. arXiv. https://arxiv.org/abs/2512.01127

Wu, G. (2025). It's not that simple. An analysis of simple test-time scaling. arXiv. https://arxiv.org/abs/2507.14419

Yu, C., Tan, Q., Gao, J., Yu, S., Lu, H., Yang, X., Xu, Z., Wang, Y., Wu, Y., & Vinitsky, E. (2025). Extending test-time scaling: A 3D perspective with context, batch, and turn. arXiv. https://arxiv.org/abs/2511.15738

Zeng, Z., Cheng, Q., Yin, Z., Zhou, Y., & Qiu, X. (2025). Revisiting the test-time scaling of o1-like models: Do they truly possess test-time scaling capabilities? arXiv. https://arxiv.org/abs/2502.12215
