# Systematic Literature Review: Test-Time Scaling of Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "test-time scaling", filtered to category cs.LG, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Test-time scaling has emerged as a critical research direction in large language models, with recent work exploring multiple dimensions of how computational resources can be allocated during inference to improve reasoning and task performance. The surveyed literature reveals a field rapidly maturing from initial demonstrations of scaling benefits to nuanced investigations of efficiency, ranking methodologies, and practical limits. Key themes include the exploration of multiple scaling dimensions beyond simple sample count, the development of efficient test-time scaling methods that reduce computational overhead, and theoretical frameworks for understanding scaling plateaus. Collectively, these papers establish that test-time scaling is not monolithic but rather a multi-faceted phenomenon requiring careful consideration of candidate generation strategies, ranking methods, and resource allocation trade-offs.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "test-time scaling", filtered to category cs.LG, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Dimensional Scaling Frameworks

The literature reveals a shift from viewing test-time scaling as a single-dimensional phenomenon (simply increasing sample count) to recognizing multiple distinct dimensions that can be scaled independently and in combination. Wang et al. (2025) introduced the 3D test-time scaling framework, integrating context scaling (reasoning length), batch scaling (parallel sampling), and turn scaling (iterative self-refinement). Their work demonstrates that each dimension exhibits scaling effects with bounded capacity, but combining all three dimensions substantially improves performance on challenging reasoning benchmarks including IOI, IMO, and CPHO. This multi-dimensional perspective addresses a fundamental limitation: test-time scaling is constrained by base model context length, which remains orders of magnitude smaller than training token consumption. The 3D framework provides a systematic approach to extending test-time reasoning capacity beyond simple context extension.

Similarly, Wang et al. (2025) theoretically analyzed parallel and sequential scaling paradigms through their Test-Time Scaling Performance Model (TTSPM), deriving saturation points that identify thresholds beyond which additional computation yields diminishing returns. Remarkably, despite their distinct mechanisms, both paradigms converge to a unified mathematical structure in their upper bounds, providing theoretical grounding for understanding scaling limits. These frameworks collectively suggest that future work should consider test-time scaling as a resource allocation problem across multiple dimensions rather than a simple matter of generating more samples.

### Theme 2: Efficiency and Resource Optimization

A prominent theme across recent work is the tension between scaling benefits and computational costs. Kashaniyan and Jannesari (2026) demonstrated that candidate count alone inadequately describes the systems cost of multi-candidate test-time scaling. Their experiments revealed that eight serial generation calls consume 4.64-4.86× as much GPU-device energy and exhibit 5.77-6.12× the P95 latency of a single batched call with eight candidates. This finding has profound implications: when candidates are independent and memory permits, fewer generation calls with larger batch sizes are substantially more efficient. The authors argue that evaluations should report not only candidate count and accuracy, but also generation schedule and GPU-level systems metrics.

Ding and Zhang (2026) addressed efficiency in the software engineering domain with SWE-Replay, which optimizes scaling by recycling trajectories from prior trials rather than repeatedly sampling from scratch. Their approach dynamically chooses between exploration and exploitation by branching at critical intermediate steps based on repository exploration potential and reasoning significance, avoiding reliance on potentially miscalibrated LLM-based value estimates. On SWE-Bench Verified, SWE-Replay reduced costs by up to 17.4% while maintaining or improving performance by up to 3.8%, establishing a robust foundation for efficient test-time scaling of software engineering agents.

He et al. (2026) introduced DiffCodeGen for code generation, which performs candidate selection without additional LLM inference calls by using coverage-guided fuzzing to synthesize inputs and clustering candidates based on behavioral similarity. This approach achieves competitive or superior performance compared to state-of-the-art methods while using only a fraction of time and tokens, demonstrating that intelligent candidate selection can dramatically reduce the token consumption typically associated with test-time scaling.

### Theme 3: Ranking and Evaluation Methodologies

As test-time scaling becomes more prevalent, proper ranking and evaluation of models in this regime has emerged as a critical challenge. Hariri et al. (2026) formalized dense benchmark ranking under test-time scaling and introduced Scorio, an open-source library implementing statistical ranking methods including paired-comparison models, item response theory, voting rules, and graph-based methods. Their evaluation across 20 reasoning models on four Olympiad-style math benchmarks revealed that most full-trial rankings agree closely with the Bayesian gold standard (mean Kendall's τ_b = 0.93-0.95), with 19-34 methods recovering exactly the same ordering. In the single-trial regime, the best methods reach τ_b ≈ 0.86. Using greedy decoding as an empirical prior reduces variance at N=1 by 16-52%, but can bias rankings when greedy and stochastic sampling disagree. This work identifies reliable ranking methods for both high- and low-budget test-time scaling, providing essential infrastructure for fair model comparison.

Zeng et al. (2025) challenged assumptions about test-time scaling capabilities in o1-like models, finding that longer chains-of-thought do not consistently enhance accuracy—correct solutions are often shorter than incorrect ones for the same questions. This phenomenon relates to models' self-revision capabilities: longer CoTs contain more self-revisions, which often lead to performance degradation. Their comparison of sequential and parallel scaling strategies on QwQ, R1, and LIMO found that parallel scaling achieves better coverage and scalability. Based on these insights, they proposed Shortest Majority Vote, which combines parallel scaling with CoT length characteristics, significantly improving test-time scalability compared to conventional majority voting approaches.

### Theme 4: Domain-Specific Applications and Adaptations

Test-time scaling research has expanded beyond general reasoning to domain-specific applications with tailored methodologies. Ge et al. (2026) examined on-policy distillation through the lens of test-time scaling, revealing that OPD improvements do not uniformly extend across all test-time sampling budgets. They observed two distinct patterns: OPD can improve pass@K at both small and large sampling budgets, or improve small-budget performance while reducing large-budget pass@K. Their proposed Teacher Advantage Score at K (TAS@K) can be computed before OPD training to predict which teacher will lead to larger improvements at a target sampling budget, achieving 83.6% agreement with observed improvements across thirteen benchmarks.

Xiao et al. (2025) introduced state tuning for RWKV-7, a novel state-based approach to test-time scaling tailored to RNN architectures. By developing an observer framework for learning state dynamics, employing kernel methods to dynamically upscale state size, and integrating Decorrelated Backpropagation for optimization, they demonstrated that tuning only the state matrix enables smaller models to outperform larger models on target tasks. This work extends test-time scaling beyond transformer architectures, highlighting the potential for architecture-specific scaling strategies.

### Theme 5: Simple and Accessible Approaches

Muennighoff et al. (2025) sought the simplest approach to achieve test-time scaling and strong reasoning performance comparable to proprietary models like o1. Their work introduced s1K, a curated dataset of 1,000 questions paired with reasoning traces validated on difficulty, diversity, and quality criteria, along with budget forcing—a technique to control test-time compute by terminating or lengthening the model's thinking process by appending "Wait" tokens. After supervised finetuning Qwen2.5-32B-Instruct on s1K and equipping it with budget forcing, s1-32B exceeded o1-preview on competition math questions by up to 27% (MATH and AIME24). Budget forcing enabled performance extrapolation from 50% to 57% on AIME24 without additional test-time intervention. This work demonstrates that simple, open approaches can achieve competitive performance with proprietary systems, democratizing access to advanced reasoning capabilities.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that test-time scaling exhibits diminishing returns beyond certain thresholds. Wang et al. (2025) derived theoretical saturation points for both parallel and sequential scaling, while Wang et al. (2025) empirically demonstrated bounded capacity in each of the three scaling dimensions. Kashaniyan and Jannesari (2026) showed that naive scaling (increasing sample count without considering generation strategy) incurs substantial efficiency penalties. There is broad agreement that parallel scaling strategies outperform sequential approaches in terms of both efficiency and coverage (Zeng et al., 2025; Ding & Zhang, 2026).

**Disagreements**: A notable tension exists regarding the relationship between reasoning length and accuracy. Zeng et al. (2025) found that longer CoTs often correlate with worse performance due to self-revision errors, challenging the assumption that more computation time inherently improves results. This contrasts with the 3D scaling framework (Wang et al., 2025), which treats context scaling (increasing reasoning length) as one beneficial dimension, albeit with bounded capacity. The resolution may lie in the quality rather than quantity of reasoning: budget forcing (Muennighoff et al., 2025) can improve performance by prompting models to "double-check" answers, but unstructured length increases may introduce errors faster than corrections.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, most evaluations concentrate on mathematical reasoning benchmarks (AIME, MATH, GPQA), with limited exploration of test-time scaling in other domains such as creative writing, scientific reasoning, or multi-modal tasks. Xiao et al. (2025) evaluated state tuning on a single target task without broader benchmark coverage, and Muennighoff et al. (2025) focused primarily on math competition questions.

Second, the theoretical understanding of why certain scaling strategies work remains incomplete. While Wang et al. (2025) derived unified mathematical structures for scaling bounds, the mechanistic explanations for phenomena like the self-revision degradation observed by Zeng et al. (2025) remain empirical rather than theoretical.

Third, energy and systems-level metrics are underreported in test-time scaling research. Kashaniyan and Jannesari (2026) explicitly call for evaluations to report generation schedules and GPU-level metrics alongside accuracy, suggesting this has been neglected in prior work.

Finally, the generalizability of domain-specific methods remains unclear. SWE-Replay (Ding & Zhang, 2026) is designed specifically for software engineering agents with repository exploration workflows, and DiffCodeGen (He et al., 2026) targets code generation—whether these approaches transfer to other domains requires investigation.

## Per-Paper Annotations

### Ding and Zhang (2026)

**Research question**: How can test-time scaling for software engineering agents be made more efficient without relying on potentially noisy LLM-based value estimates?
**Methodology**: SWE-Replay optimizes scaling by recycling trajectories from prior trials, dynamically choosing to explore from scratch or exploit archived experience by branching at critical intermediate steps based on repository exploration potential and reasoning significance.
**Key findings**:
- Outperforms naive scaling on SWE-Bench Verified while reducing costs by up to 17.4%
- Maintains or improves performance by up to 3.8% compared to standard approaches
- Generalizes successfully to SWE-Bench Pro and Multilingual benchmarks
- Avoids reliance on potentially miscalibrated LLM-based value estimates
**Limitations**: Approach is specifically designed for software engineering agents with repository exploration workflows; effectiveness may vary for different agent architectures or task domains beyond SWE.

### Ge et al. (2026)

**Research question**: Does on-policy distillation (OPD) yield improvements across the entire range of test-time sampling budgets?
**Methodology**: The authors examine OPD through test-time scaling by varying sampling budget K and evaluating performance with pass@K, and propose the Teacher Advantage Score at K (TAS@K) to predict which teacher will lead to larger improvements before OPD training.
**Key findings**:
- OPD can improve pass@K at both small and large sampling budgets, or improve small-budget performance while reducing large-budget pass@K
- Conditions guaranteeing performance reversal are identified with reverse KL counterexamples
- TAS@K can be computed before OPD training to predict teacher selection at target sampling budgets
- TAS@K ordering agrees with observed improvements in 83.6% of experiments across thirteen benchmarks
**Limitations**: TAS@K does not perfectly predict outcomes (only 83.6% agreement rate), and counterexamples demonstrate that even idealized reverse KL cases can exhibit performance reversals.

### Hariri et al. (2026)

**Research question**: How can reasoning LLMs be effectively ranked under test-time scaling regimes?
**Methodology**: The authors formalize dense benchmark ranking under test-time scaling and introduce Scorio, implementing statistical ranking methods including paired-comparison models, item response theory, voting rules, and graph/spectral-based methods, evaluated across 20 reasoning models on four Olympiad-style math benchmarks.
**Key findings**:
- Most full-trial rankings agree closely with Bayesian gold standard Bayes_U@80 (mean Kendall's τ_b = 0.93-0.95)
- 19-34 methods recover exactly the same ordering as the gold standard in full-trial regime
- In single-trial regime, best methods reach τ_b ≈ 0.86
- Using greedy decoding as empirical prior reduces variance at N=1 by 16-52%, but can bias rankings
**Limitations**: Greedy decoding as empirical prior can bias rankings when it disagrees with stochastic sampling; evaluation limited to Olympiad-style math benchmarks which may not generalize to other reasoning domains.

### He et al. (2026)

**Research question**: How can code generation test-time scaling be improved without relying on public test cases or extensive LLM inference for candidate selection?
**Methodology**: DiffCodeGen generates diverse code candidates using various sampling and prompting strategies, applies coverage-guided fuzzing to synthesize inputs without requiring existing tests, clusters candidates based on behavioral similarity, and selects the medoid of the largest cluster.
**Key findings**:
- Achieves competitive or superior performance compared to state-of-the-art methods while using only a fraction of time and tokens
- Candidate selection requires no additional LLM model calls, incurring little to no additional token consumption
- Fully asynchronous, model-agnostic, and naturally suited to agentic coding workflows
- Evaluated across 4 large language models with consistent improvements over baselines
**Limitations**: Relies on coverage-guided fuzzing which may not capture all edge cases; behavioral clustering may not always identify the semantically best solution; effectiveness depends on quality of synthesized test inputs.

### Kashaniyan and Jannesari (2026)

**Research question**: How does candidate-generation strategy (not just candidate count) affect the systems cost and performance of LLM test-time scaling?
**Methodology**: Fixed candidate count N=8 and compared four generation schedules (1x8, 2x4, 4x2, 8x1) measuring latency, throughput, GPU-hours, and GPU-device energy on A100 GPUs using Phi-3-mini and Qwen2.5-1.5B on 500 GSM8K prompts.
**Key findings**:
- Increasing N from 1 to 8 improves accuracy by 8.4 percentage points for Phi-3-mini and 18.4 points for Qwen2.5-1.5B
- Eight serial calls use 4.64-4.86× as much gross GPU-device energy as one batched call
- Eight serial calls have 5.77-6.12× the P95 latency of one batched call
- Fewer generation calls with larger batch sizes are more efficient when candidates are independent
**Limitations**: Experiments limited to A100 and V100 GPUs with independent candidates; memory constraints may limit batch size options in practice.

### Muennighoff et al. (2025)

**Research question**: What is the simplest approach to achieve test-time scaling and strong reasoning performance comparable to proprietary models like o1?
**Methodology**: Curated s1K, a small dataset of 1,000 questions with reasoning traces validated on difficulty, diversity, and quality criteria, and developed budget forcing to control test-time compute by terminating or lengthening the model's thinking process.
**Key findings**:
- s1-32B exceeds o1-preview on competition math questions by up to 27% (MATH and AIME24)
- Budget forcing enables performance extrapolation from 50% to 57% on AIME24
- Three dataset criteria (difficulty, diversity, quality) validated through ablation studies
- Simple supervised finetuning combined with budget forcing achieves strong reasoning performance
**Limitations**: Evaluation concentrated on math competition benchmarks; budget forcing mechanism using "Wait" appending may not transfer effectively to non-mathematical reasoning domains.

### Wang et al. (2025) [3D Perspective]

**Research question**: How can test-time scaling be extended beyond context length limitations to substantially improve reasoning performance?
**Methodology**: Proposed 3D test-time scaling integrating three dimensions: context scaling (reasoning length), batch scaling (parallel sampling for accuracy improvement), and turn scaling (iterative self-refinement for reasoning quality enhancement).
**Key findings**:
- Each dimension demonstrates test-time scaling effects but with bounded individual capacity
- Combining all three dimensions substantially improves performance on IOI, IMO, and CPHO
- Human preference feedback provides additional benefits to combined 3D scaling approach
- Human-in-the-loop framework extends to embodied learning for humanoid control behavior design
**Limitations**: Test-time scaling remains fundamentally constrained by base model context length, orders of magnitude smaller than training token consumption; each dimension has bounded capacity limiting total improvement potential.

### Wang et al. (2025) [Scaling Plateau]

**Research question**: What are the practical limits of test-time scaling and how can optimal resource allocation be achieved for large reasoning models?
**Methodology**: Introduced the Test-Time Scaling Performance Model (TTSPM) and theoretically analyzed parallel and sequential scaling paradigms from a probabilistic modeling perspective to derive saturation points identifying thresholds beyond which additional computation yields diminishing returns.
**Key findings**:
- Both parallel and sequential scaling paradigms converge to unified mathematical structure in upper bounds
- Saturation points identify specific thresholds where additional compute yields diminishing returns
- Theoretical findings empirically validated on AIME, MATH-500, and GPQA benchmarks
- Derived bounds provide practical guidance for cost-benefit trade-offs in resource allocation
**Limitations**: Theoretical model may not capture all practical factors affecting scaling behavior in real-world deployments; validation limited to specific reasoning benchmarks without broader task coverage.

### Xiao et al. (2025)

**Research question**: How can test-time scaling be applied to RNN-based RWKV-7 models to enhance performance without altering pre-trained weights?
**Methodology**: Developed an observer framework enabling smaller models to replicate RWKV-7 state dynamics, employed kernel methods to dynamically upscale state size, and integrated Decorrelated Backpropagation to optimize the upscaled state matrix.
**Key findings**:
- State tuning achieves state-of-the-art performance on target tasks without modifying pre-trained weights
- Smaller models can outperform larger models by tuning only the state matrix
- Method preserves RWKV-7's original efficiency while harnessing test-time scaling benefits
- Three innovations (observer framework, kernel upscaling, DBP) collectively enable effective state tuning
**Limitations**: Approach specifically tailored to RWKV-7 architecture and may not generalize to other model types; evaluation focused on single target task without broader benchmark coverage.

### Zeng et al. (2025)

**Research question**: Do o1-like models (QwQ, Deepseek-R1, LIMO) truly possess test-time scaling capabilities, and does longer chain-of-thought consistently enhance accuracy?
**Methodology**: Analyzed relationship between CoT length and accuracy, examined self-revision patterns in longer CoTs, compared sequential versus parallel scaling strategies on QwQ, R1, and LIMO, and proposed Shortest Majority Vote combining parallel scaling with CoT length characteristics.
**Key findings**:
- Longer CoTs of o1-like models do not consistently enhance accuracy; correct solutions are often shorter than incorrect ones
- Longer CoTs contain more self-revisions, which often lead to performance degradation
- Parallel scaling achieves better coverage and scalability than sequential scaling
- Shortest Majority Vote significantly improves test-time scalability compared to conventional majority voting
**Limitations**: Study focused on specific o1-like models and may not generalize to all reasoning models; self-revision analysis is empirical rather than mechanistic; findings based on specific benchmark datasets.

## References

Ding, Y., & Zhang, L. (2026). SWE-Replay: Efficient test-time scaling for software engineering agents. arXiv. https://arxiv.org/abs/2601.22129

Ge, X., Zhang, Z., Huang, Y., Zhu, J., Yuan, L., Gu, W., Wu, W., Huang, W., Han, B., Zhang, X., & Yao, J. (2026). Towards understanding on-policy distillation through the lens of test-time scaling. arXiv. https://arxiv.org/abs/2608.11829

Hariri, M., Hinczewski, M., Ma, J., & Chaudhary, V. (2026). Ranking reasoning LLMs under test-time scaling. arXiv. https://arxiv.org/abs/2603.10960

He, Y., Wang, E., Wang, J., Ouyang, X., & Chen, H. (2026). Code generation by differential test time scaling. arXiv. https://arxiv.org/abs/2605.20473

Kashaniyan, M., & Jannesari, A. (2026). Sample count is not enough: Candidate-generation strategy shapes the energy and performance of LLM test-time scaling. arXiv. https://arxiv.org/abs/2609.19499

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. arXiv. https://arxiv.org/abs/2501.19393

Wang, J., Zhu, B., Leong, C. T., Li, Y., & Li, W. (2025). Scaling over scaling: Exploring test-time scaling plateau in large reasoning models. arXiv. https://arxiv.org/abs/2505.20522

Wang, C., Tan, Q., Gao, J., Yu, S., Lu, H., Yang, X., Xu, Z., Wang, Y., Wu, Y., & Vinitsky, E. (2025). Extending test-time scaling: A 3D perspective with context, batch, and turn. arXiv. https://arxiv.org/abs/2511.15738

Xiao, L., Zhiyuan, L., & Yueyu, L. (2025). State tuning: State-based test-time scaling on RWKV-7. arXiv. https://arxiv.org/abs/2504.05097

Zeng, Z., Cheng, Q., Yin, Z., Zhou, Y., & Qiu, X. (2025). Revisiting the test-time scaling of o1-like models: Do they truly possess test-time scaling capabilities? arXiv. https://arxiv.org/abs/2502.12215
