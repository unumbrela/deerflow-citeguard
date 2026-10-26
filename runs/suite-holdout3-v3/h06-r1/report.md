# Systematic Literature Review: Test-Time Scaling of Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "test-time scaling", category cs.LG, last 2 years (2024-10-26 to 2026-10-26)
**Citation format**: APA 7th edition

## Executive Summary

The literature on test-time scaling of language models reveals a rapidly evolving field grappling with fundamental questions about how to effectively allocate computational resources during inference. The ten surveyed papers collectively demonstrate that simple scaling approaches—merely increasing sample counts or generation lengths—are insufficient for unlocking improved performance. Instead, researchers are developing sophisticated frameworks that consider multiple dimensions of scaling including context length, batch sampling, iterative refinement, and confidence-based adaptation. A key insight across the literature is that diversity in generation strategies, whether through mode-conditioning, contextual reasoning, or candidate-generation approaches, is critical for achieving meaningful scaling benefits. The field is moving toward more nuanced understanding of when and how test-time compute translates to performance gains, with particular attention to efficiency, calibration, and the role of human feedback.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "test-time scaling", filtered to category cs.LG, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Dimensional Scaling Frameworks

The literature reveals a shift from one-dimensional scaling (simply increasing sample count or generation length) toward multi-dimensional frameworks that consider multiple axes of test-time computation. Yu et al. (2025) introduce a unified 3D perspective encompassing context-length scaling, batch scaling (parallel sampling), and turn scaling (iterative self-refinement), demonstrating that combining all three dimensions substantially improves reasoning performance on challenging benchmarks including IOI, IMO, and CPHO. This framework extends naturally to embodied learning domains for designing humanoid control behaviors. Similarly, Kashaniyan and Jannesari (2026) examine candidate-generation strategy as a critical dimension, showing that eight serial calls use 4.64-4.86x as much GPU-device energy and have 5.77-6.12x the P95 latency of one batched call with eight candidates. The convergent insight is that how compute is allocated matters as much as how much compute is used.

### Theme 2: Diversity as the Key to Scaling

A dominant theme across multiple papers is that diversity collapse fundamentally limits test-time scaling effectiveness. Wu et al. (2025) propose the mode-conditioning (ModC) framework, which allocates test-time compute across reasoning modes using specialist models or mode-specific prefixes, achieving a 4x efficiency gain over standard training on OpenThoughts when fine-tuning Qwen2.5-7B. The core insight is that parallel sampling fails when all samples converge to the same reasoning mode, regardless of sample count. Gradient clustering enables ModC without explicit mode labels, yielding up to 10% gains on datasets such as NuminaMath. This diversity-focused approach aligns with findings from Ge et al. (2026), who show that on-policy distillation can improve pass@K at both small and large sampling budgets, but can also improve small-budget performance while reducing large-budget pass@K—a reversal that depends on the diversity and quality of generated samples.

### Theme 3: Questioning Fundamental Scaling Assumptions

Several papers critically examine whether current approaches to test-time scaling actually deliver on their promises. Zeng et al. (2025) investigate o1-like models (QwQ, Deepseek-R1, LIMO) and find that longer chains of thought do not consistently enhance accuracy—correct solutions are often shorter than incorrect ones for the same questions. This phenomenon is closely related to models' self-revision capabilities, where longer CoTs contain more self-revisions that often lead to performance degradation. Wu (2025) similarly argues that scaling behavior is largely attributed to scaling down by enforcing maximum length, and that fine-tuning on long CoT data distilled from o1-like models has no significant impact on scaling behavior. The critical insight from both papers is that the goal of scaling test-time compute should be to unlock higher performance beyond original capability, not merely reproduce scaling appearance.

### Theme 4: Confidence-Based Efficiency

A promising direction for improving test-time scaling efficiency involves using model confidence to adapt computation to query complexity. Huang et al. (2025) introduce Self-Calibration by distilling Self-Consistency-derived confidence into the model itself for reliable confidence estimation at test time. Their confidence-based Early Stopping applied to Best-of-N improves MathQA accuracy from 81.0 to 83.6 with a sample budget of 16 responses. The key innovation is enabling reliable confidence estimation with one forward pass, allowing the system to handle queries of various difficulty levels without wasting compute on easy problems or under-computing on hard ones. This approach demonstrates that efficiency gains can come from smarter allocation rather than brute-force scaling.

### Theme 5: Contextual Reasoning and Memory Management

Extending test-time scaling beyond the limited context length of base models requires sophisticated approaches to context allocation and reuse. Li et al. (2026) introduce Hermes, a family of configurable harnesses that progressively vary model control over context allocation and reuse, and Hermes-Learn, a two-stage framework for learning contextual reasoning capabilities. Their findings show that capable models can exploit flexibility to scale with additional inference-time compute, and training with Hermes-Learn closes the gap for smaller open-source models that initially struggle. The gains induce adaptive contextual reasoning strategies that vary with both problem and reasoning progress, with benefits that generalize across benchmarks and models, extrapolating beyond inference-time compute seen during training.

### Theme 6: Evaluation and Ranking Under Scaling

As test-time scaling becomes more prevalent, properly evaluating and ranking models in the scaling regime becomes critical. Hariri et al. (2026) formalize dense benchmark ranking under test-time scaling and introduce Scorio, a library implementing statistical ranking methods including paired-comparison models, IRT models, voting rules, and graph- and spectral-based methods. Their evaluation across 20 reasoning models on four Olympiad-style math benchmarks with up to N=80 trials reveals that most full-trial rankings agree closely with Bayesian gold standard (mean Kendall's τ_b = 0.93-0.95), but in the single-trial regime, the best methods reach only τ_b ≈ 0.86. Using greedy decoding as an empirical prior reduces variance at N=1 by 16-52%, but can bias rankings when greedy and stochastic sampling disagree. This work provides essential infrastructure for fair model comparison in the scaling era.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the insight that naive scaling—simply increasing sample count or generation length—is insufficient for meaningful performance gains. Wu et al. (2025), Zeng et al. (2025), and Wu (2025) all demonstrate that longer generation does not guarantee better performance, and can even degrade it through excessive self-revision or mode collapse. There is also broad agreement that diversity in generation strategies is critical, whether through mode-conditioning (Wu et al., 2025), contextual reasoning (Li et al., 2026), or batch-efficient candidate generation (Kashaniyan & Jannesari, 2026). Finally, multiple papers emphasize efficiency as a first-order concern, with approaches like Self-Calibration (Huang et al., 2025) and batch scaling (Kashaniyan & Jannesari, 2026) demonstrating that smarter allocation can achieve better results with less compute.

**Disagreements**: There is some tension between papers that view test-time scaling as fundamentally limited by model architecture and training (Zeng et al., 2025; Wu, 2025) versus those that demonstrate substantial gains are achievable through sophisticated frameworks (Yu et al., 2025; Wu et al., 2025; Li et al., 2026). The former camp argues that o1-like models may not truly possess test-time scaling capabilities in their current form, while the latter demonstrates that with proper frameworks—3D scaling, mode-conditioning, or contextual reasoning—significant improvements are possible. This disagreement may reflect different model classes or task domains rather than fundamental incompatibility, but it highlights the need for more systematic understanding of when and why scaling works.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting a need for more transparent discussion of methodological constraints and boundary conditions. Second, while multiple papers address efficiency, there is limited discussion of environmental impact or carbon footprint of large-scale test-time compute allocation. Third, the relationship between training-time compute and test-time scaling remains underexplored—several papers note that fine-tuning on long CoT data has limited impact (Wu, 2025; Zeng et al., 2025), but the optimal balance between training and inference compute is not well understood. Fourth, human feedback is mentioned as beneficial (Yu et al., 2025) but systematic study of human-in-the-loop scaling approaches is limited. Finally, most papers focus on mathematical or code reasoning benchmarks, with limited exploration of test-time scaling in creative, open-ended, or multi-modal domains.

## Per-Paper Annotations

### Ge et al. (2026)

**Research question**: Do improvements from on-policy distillation extend across the entire range of test-time sampling budgets?
**Methodology**: The authors revisit OPD expectations through test-time scaling by varying sampling budget K and evaluating with pass@K, and propose Teacher Advantage Score at K (TAS@K) to predict which teacher will lead to larger improvement in pass@K.
**Key findings**:
- OPD can improve pass@K at both small and large sampling budgets, but can also improve small-budget performance while reducing large-budget pass@K
- The authors show one condition that guarantees such a reversal and provide an idealized reverse KL counterexample where it occurs even when the teacher has higher accuracy on every problem
- TAS@K ordering agrees with observed pass@K improvements in 83.6% of experiments across three domains and thirteen benchmarks
**Limitations**: not stated in abstract

### Hariri et al. (2026)

**Research question**: How can reasoning LLMs be reliably ranked in the test-time scaling regime?
**Methodology**: The authors formalize dense benchmark ranking under test-time scaling and introduce Scorio, a library implementing statistical ranking methods including paired-comparison models, IRT models, voting rules, and graph- and spectral-based methods, evaluated across 20 reasoning models on four Olympiad-style math benchmarks with up to N=80 trials.
**Key findings**:
- Most full-trial rankings agree closely with Bayesian gold standard Bayes_U@80 (mean Kendall's τ_b = 0.93-0.95)
- 19-34 methods recover exactly the same ordering as the gold standard
- In the single-trial regime, the best methods reach τ_b ≈ 0.86
- Using greedy decoding as an empirical prior reduces variance at N=1 by 16-52%, but can bias rankings when greedy and stochastic sampling disagree
**Limitations**: not stated in abstract

### Huang et al. (2025)

**Research question**: How can model confidence be used to improve the efficiency of test-time scaling by adapting computation to query complexity?
**Methodology**: The authors introduce Self-Calibration by distilling Self-Consistency-derived confidence into the model itself for reliable confidence estimation at test time, then design confidence-based efficient test-time scaling methods including Early-Stopping for Best-of-N and Self-Consistency with calibrated confidence.
**Key findings**:
- Model confidence can improve efficiency of test-time scaling by handling queries of various difficulty
- Self-Calibration enables reliable confidence estimation at test time with one forward pass
- Confidence-based Early Stopping applied to Best-of-N improves MathQA accuracy from 81.0 to 83.6 with sample budget of 16 responses
- Experiments on three LLMs across six datasets demonstrate the effectiveness of the approach
**Limitations**: not stated in abstract

### Kashaniyan and Jannesari (2026)

**Research question**: How does candidate-generation strategy (not just candidate count) affect the systems cost and performance of LLM test-time scaling?
**Methodology**: The study examines the effect of increasing N on reasoning accuracy using Phi-3-mini and Qwen2.5-1.5B on 500 GSM8K prompts, then fixes N=8 and compares four generation schedules (1x8, 2x4, 4x2, 8x1), measuring latency, throughput, GPU-hours, and gross GPU-device energy on A100 GPUs.
**Key findings**:
- Increasing N from 1 to 8 improves accuracy by 8.4 percentage points for Phi-3-mini and 18.4 points for Qwen2.5-1.5B
- Eight serial calls use 4.64-4.86x as much gross GPU-device energy and have 5.77-6.12x the P95 latency of one batched call with eight candidates
- The same pattern appears across three independently scheduled A100 nodes per model and in short-output SciQ/V100 experiments
- When candidates are independent and memory allows it, fewer generation calls with larger batch sizes are more efficient
**Limitations**: not stated in abstract

### Li et al. (2026)

**Research question**: How can models learn to effectively allocate fresh contexts and carry information between them for test-time scaling across multiple context windows?
**Methodology**: The authors introduce Hermes, a family of configurable harnesses that progressively vary model control over context allocation and reuse, and Hermes-Learn, a two-stage framework for learning contextual reasoning capabilities.
**Key findings**:
- Capable models can exploit flexibility to scale with additional inference-time compute
- Training with Hermes-Learn closes the gap for smaller open-source models that initially struggle
- Gains induce adaptive contextual reasoning strategies that vary with both problem and reasoning progress
- Benefits generalize across benchmarks and models, extrapolate beyond inference-time compute seen during training
- Improvements transfer to complementary test-time scaling methods beyond Hermes
**Limitations**: not stated in abstract

### Qin et al. (2026)

**Research question**: How can we train reliable LLM judges for Best-of-N selection in test-time scaling for code generation despite distribution shifts?
**Methodology**: The authors propose DAJ, a reasoning-based LLM judge trained with verifiable rewards under a bi-level data-reweighted learning framework that learns data-importance weights to optimize generalization on held-out meta sets aligned with target benchmarks.
**Key findings**:
- DAJ achieves state-of-the-art performance on LiveCodeBench and BigCodeBench
- The approach automatically emphasizes hard problems, in-distribution samples, and trajectory-aligned data without hand-crafted heuristics
- This is the first application of data reweighting to LLM-as-a-Judge training for test-time scaling
- DAJ outperforms strong test-time scaling baselines as well as leading proprietary models
**Limitations**: not stated in abstract

### Wu (2025)

**Research question**: What are the actual mechanisms behind simple test-time scaling behavior in models distilled from o1-like models?
**Methodology**: The paper analyzes simple test-time scaling by examining scaling down (enforcing maximum length) versus scaling up (appending 'Wait') approaches, and compares fine-tuning on long CoT data against these methods.
**Key findings**:
- Scaling behavior is largely attributed to scaling down by enforcing a maximum length
- Fine-tuning on long CoT data distilled from o1-like models has no significant impact on scaling behavior
- Scaling up by appending 'Wait' leads to inconsistencies as models may oscillate between solutions
- Simple test-time scaling progressively imposes a lower upper limit on model performance as it scales down
- The goal of scaling test-time compute should be to unlock higher performance beyond original capability, not merely reproduce scaling appearance
**Limitations**: not stated in abstract

### Wu et al. (2025)

**Research question**: How can parallel sampling overcome diversity collapse to unlock superior test-time scaling in language models?
**Methodology**: The authors propose the mode-conditioning (ModC) framework, which allocates test-time compute across reasoning modes using specialist models or mode-specific prefixes. They evaluate ModC across controlled graph-search tasks and large-scale reasoning benchmarks with models ranging from 0.5B to 7B parameters.
**Key findings**:
- ModC consistently improves scaling across controlled graph-search tasks and large-scale reasoning benchmarks
- Fine-tuning Qwen2.5-7B with ModC achieves a 4x efficiency gain over standard training on OpenThoughts
- Gradient clustering enables ModC without explicit mode labels, yielding up to 10% gains on datasets such as NuminaMath
- ModC improves reinforcement learning and can further boost diversity-inducing RL methods
**Limitations**: not stated in abstract

### Yu et al. (2025)

**Research question**: How can test-time scaling capacity be extended beyond the limited context length of base models?
**Methodology**: The authors introduce a unified framework of multi-dimensional test-time scaling considering context-length scaling, batch scaling (parallel sampling), and turn scaling (iterative self-refinement), proposing 3D test-time scaling that integrates all three dimensions.
**Key findings**:
- Each dimension demonstrates a test-time scaling effect, but with a bounded capacity
- Combining all three dimensions substantially improves reasoning performance on challenging testbeds including IOI, IMO, and CPHO
- The combined approach further benefits from human preference feedback
- The human-in-the-loop framework naturally extends to embodied learning domain for designing humanoid control behaviors
**Limitations**: not stated in abstract

### Zeng et al. (2025)

**Research question**: Do o1-like models (QwQ, Deepseek-R1, LIMO) truly possess test-time scaling capabilities?
**Methodology**: The study investigates whether longer CoTs enhance accuracy in o1-like models, examines the relationship with self-revision capabilities, and compares sequential and parallel scaling strategies on QwQ, R1 and LIMO.
**Key findings**:
- Longer CoTs of o1-like models do not consistently enhance accuracy; correct solutions are often shorter than incorrect ones for the same questions
- This phenomenon is closely related to models' self-revision capabilities - longer CoTs contain more self-revisions, which often lead to performance degradation
- Parallel scaling achieves better coverage and scalability than sequential scaling
- Shortest Majority Vote method significantly improves models' test-time scalability compared to conventional majority voting approaches
**Limitations**: not stated in abstract

## References

Ge, X., Zhang, Z., Huang, Y., Zhu, J., Yuan, L., Gu, W., Wu, W., Huang, W., Han, B., Zhang, X., & Yao, J. (2026). Towards understanding on-policy distillation through the lens of test-time scaling. arXiv. https://arxiv.org/abs/2608.11829

Hariri, M., Hinczewski, M., Ma, J., & Chaudhary, V. (2026). Ranking reasoning LLMs under test-time scaling. arXiv. https://arxiv.org/abs/2603.10960

Huang, C., Leng, J., Liu, J., & Huang, J. (2025). Efficient test-time scaling via self-calibration. arXiv. https://arxiv.org/abs/2503.00031

Kashaniyan, M., & Jannesari, A. (2026). Sample count is not enough: Candidate-generation strategy shapes the energy and performance of LLM test-time scaling. arXiv. https://arxiv.org/abs/2609.19499

Li, X., Goswami, M., Liu, H., Kanakaris, N., Huang, L., Jana, P., Blöbaum, P., & Jain, P. (2026). Hermes: Learning contextual reasoning unlocks test-time scaling. arXiv. https://arxiv.org/abs/2609.38332

Qin, P., Zhang, R., Cao, Q., & Xie, P. (2026). DAJ: Data-reweighted LLM judge for test-time scaling in code generation. arXiv. https://arxiv.org/abs/2601.22230

Wu, C. H., Goyal, S., & Raghunathan, A. (2025). Mode-conditioning unlocks superior test-time scaling. arXiv. https://arxiv.org/abs/2512.01127

Wu, G. (2025). It's not that simple: An analysis of simple test-time scaling. arXiv. https://arxiv.org/abs/2507.14419

Yu, C., Tan, Q., Gao, J., Yu, S., Lu, H., Yang, X., Xu, Z., Wang, Y., Wu, Y., & Vinitsky, E. (2025). Extending test-time scaling: A 3D perspective with context, batch, and turn. arXiv. https://arxiv.org/abs/2511.15738

Zeng, Z., Cheng, Q., Yin, Z., Zhou, Y., & Qiu, X. (2025). Revisiting the test-time scaling of o1-like models: Do they truly possess test-time scaling capabilities? arXiv. https://arxiv.org/abs/2502.12215
