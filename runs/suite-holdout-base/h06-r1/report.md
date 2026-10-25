# Systematic Literature Review: Test-Time Scaling of Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "test-time scaling", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Test-time scaling has emerged as a critical research direction for enhancing language model reasoning capabilities, with the literature revealing multiple complementary approaches spanning efficiency optimization, methodological frameworks, and domain-specific applications. The surveyed papers collectively demonstrate that test-time scaling is not monolithic—researchers have identified at least three distinct dimensions (context, batch, and turn scaling), each with bounded capacity but synergistic when combined. While early work focused on simple parallel sampling and sequential refinement, recent advances have introduced sophisticated techniques including budget forcing, differential analysis, and trajectory replay that achieve superior performance with reduced computational costs. However, fundamental challenges remain around understanding saturation points, optimizing resource allocation, and ensuring that scaling improvements generalize across domains and model architectures.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "test-time scaling", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Dimensional Scaling Frameworks

Recent work has moved beyond viewing test-time scaling as a single-dimensional phenomenon. Yu et al. (2025) introduced a unified 3D framework integrating context scaling (extending reasoning length), batch scaling (parallel sampling), and turn scaling (iterative self-refinement), demonstrating that each dimension exhibits scaling effects with bounded capacity, but their combination yields substantial improvements on challenging benchmarks. This multi-dimensional perspective represents a maturation of the field from simple "more compute = better performance" assumptions toward nuanced understanding of how different scaling axes interact. Wang et al. (2025) similarly analyzed both parallel and sequential scaling paradigms, deriving theoretical saturation points beyond which additional computation yields diminishing returns, with both approaches converging to unified mathematical structures in their upper bounds.

### Theme 2: Efficiency and Resource Optimization

A significant thread focuses on making test-time scaling more computationally efficient. Kashaniyan and Jannesari (2026) demonstrated that candidate count alone is insufficient to describe systems costs—the generation schedule dramatically affects energy consumption and latency, with batched calls using 4.64-4.86x less GPU-device energy than serial calls for the same candidate count. Ding and Zhang (2026) introduced SWE-Replay, which recycles trajectories from prior trials and dynamically chooses between exploration and exploitation, reducing costs by up to 17.4% while maintaining or improving performance. He et al. (2026) presented DiffCodeGen, which performs candidate selection without additional LLM inference calls by using coverage-guided fuzzing and behavioral clustering, achieving competitive performance with a fraction of the token consumption. These works collectively shift focus from "how to scale more" to "how to scale smarter."

### Theme 3: Simple, Open-Source Approaches

In response to proprietary systems like OpenAI's o1 that demonstrated test-time scaling without revealing methodology, researchers have developed simple, open-source alternatives. Muennighoff et al. (2025) introduced s1, which curates a small 1,000-question dataset with reasoning traces and employs budget forcing—forcefully terminating or extending the model's thinking process by appending "Wait" tokens. Their s1-32B model exceeded o1-preview on competition math by up to 27%, demonstrating that sophisticated test-time scaling need not require massive resources or secret techniques. This democratization effort makes advanced reasoning capabilities accessible to the broader research community.

### Theme 4: Domain-Specific Applications

Test-time scaling techniques have been adapted for specific domains with unique constraints. Ge et al. (2026) examined on-policy distillation through the test-time scaling lens, revealing that distillation can improve small-budget performance while reducing large-budget pass@K, and proposed the Teacher Advantage Score to predict which teacher will yield better improvements at target budgets. Ding and Zhang (2026) and He et al. (2026) both focused on software engineering, addressing the computational expense of repeated trajectory sampling and the impracticality of relying on public test cases. Xiao et al. (2025) introduced state tuning for RWKV-7, a state-based approach tailored to RNN architectures that achieves state-of-the-art performance by tuning only the state matrix without altering pre-trained weights.

### Theme 5: Evaluation and Ranking Methodologies

As test-time scaling becomes widespread, rigorous evaluation frameworks have emerged. Hariri et al. (2026) formalized dense benchmark ranking under test-time scaling and introduced Scorio, implementing statistical ranking methods including paired-comparison models, item response theory, and graph-based methods. Their evaluation across 20 reasoning models on Olympiad-style math benchmarks found that most full-trial rankings agree closely with Bayesian gold standards (τ_b = 0.93-0.95), while in single-trial regimes the best methods reach τ_b ≈ 0.86. This work provides essential infrastructure for comparing models fairly in the test-time scaling regime.

### Theme 6: Critical Examination of Scaling Claims

Not all work uncritically accepts test-time scaling benefits. Zeng et al. (2025) questioned whether o1-like models truly possess test-time scaling capabilities, finding that longer chains-of-thought do not consistently enhance accuracy—correct solutions are often shorter than incorrect ones. They attributed this to self-revision patterns, where longer CoTs contain more revisions that often degrade performance. Their proposed Shortest Majority Vote, combining parallel scaling with CoT length characteristics, significantly improved scalability compared to conventional majority voting. This critical perspective ensures the field distinguishes genuine scaling effects from artifacts of specific evaluation protocols.

## Convergences and Disagreements

**Convergences**: The literature converges on several key points. First, test-time scaling exhibits bounded capacity—multiple papers (Wang et al., 2025; Yu et al., 2025) identify saturation points beyond which additional computation yields diminishing returns. Second, parallel scaling generally outperforms sequential scaling in terms of both efficiency and coverage (Zeng et al., 2025; Kashaniyan & Jannesari, 2026). Third, simple, targeted interventions can match or exceed proprietary systems—s1's budget forcing (Muennighoff et al., 2025) and state tuning (Xiao et al., 2025) both demonstrate this principle. Fourth, evaluation must account for computational costs, not just accuracy—multiple papers report energy, latency, or token consumption alongside performance metrics.

**Disagreements**: A notable tension exists around the relationship between reasoning length and accuracy. While early test-time scaling assumed longer reasoning traces would improve performance, Zeng et al. (2025) found the opposite in o1-like models, with correct solutions often shorter than incorrect ones. This contrasts with Yu et al. (2025), who found context scaling (extending reasoning length) improves performance when combined with other dimensions. Additionally, Ge et al. (2026) observed that on-policy distillation can improve small-budget performance while reducing large-budget pass@K, suggesting that scaling benefits are not monotonic and depend critically on the interaction between training objectives and test-time strategies.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, most evaluations focus on competition mathematics (AIME, MATH) or specific benchmarks (GSM8K, SWE-Bench), limiting generalizability claims to broader reasoning domains or real-world applications. Second, while theoretical saturation points are derived (Wang et al., 2025), practical guidance for estimating these thresholds for specific model architectures remains underdeveloped. Third, the interaction between test-time scaling and model size is insufficiently explored—whether smaller models benefit proportionally more or less from scaling remains unclear. Fourth, energy and systems metrics are reported inconsistently, hindering cross-paper comparisons of efficiency claims. Fifth, most work examines English-language reasoning, with limited investigation of multilingual or cross-cultural generalization. Finally, the relationship between test-time scaling and alignment—whether scaled models exhibit different safety or bias characteristics—is largely unexamined.

## Per-Paper Annotations

### Ding and Zhang (2026)

**Research question**: How can test-time scaling be made efficient for software engineering agents without relying on potentially noisy value estimates?

**Methodology**: SWE-Replay optimizes scaling by recycling trajectories from prior trials, dynamically choosing to explore from scratch or exploit archived experience by branching at critical intermediate steps based on repository exploration potential and reasoning significance.

**Key findings**:
- SWE-Replay consistently outperforms naive scaling on SWE-Bench Verified
- Reduces costs by up to 17.4% while maintaining or improving performance by up to 3.8%
- Generalizes successfully to SWE-Bench Pro and Multilingual benchmarks
- First efficient and generalizable test-time scaling technique for modern software engineering agents without value estimate reliance

**Limitations**: Evaluation focused on SWE-Bench datasets which may not represent all software engineering scenarios; intermediate step selection criteria may require tuning for different codebases; approach depends on modern agents that synthesize custom bash scripts as tools.

### Ge et al. (2026)

**Research question**: Does on-policy distillation improve performance across the entire range of test-time sampling budgets, and how can we predict which teacher will yield better improvements at a target budget?

**Methodology**: The authors examine OPD through test-time scaling by varying sampling budget K and evaluating with pass@K, identify conditions for performance reversal, and propose Teacher Advantage Score at K (TAS@K) to predict teacher selection before OPD training.

**Key findings**:
- OPD can improve pass@K at both small and large sampling budgets, but can also improve small-budget performance while reducing large-budget pass@K
- A reversal condition was identified that guarantees this pattern, even occurring under idealized reverse KL when the teacher has higher accuracy on every problem
- TAS@K can be computed before OPD training to predict which teacher will lead to larger pass@K improvement
- TAS@K ordering agrees with observed pass@K improvements in 83.6% of experiments across three domains and thirteen benchmarks

**Limitations**: The TAS@K metric achieves 83.6% agreement, leaving room for improvement in prediction accuracy, and the analysis focuses on specific domains and benchmarks that may not generalize to all OPD scenarios.

### Hariri et al. (2026)

**Research question**: How can we reliably rank reasoning LLMs in the test-time scaling regime, and which statistical methods work best at different trial budgets?

**Methodology**: The authors formalize dense benchmark ranking under test-time scaling and introduce Scorio, a library implementing statistical ranking methods including paired-comparison models, IRT models, voting rules, and graph- and spectral-based methods, evaluated across 20 reasoning models on four Olympiad-style math benchmarks.

**Key findings**:
- Most full-trial rankings agree closely with the Bayesian gold standard Bayes_U@80 (mean Kendall's τ_b = 0.93-0.95)
- Between 19-34 methods recover exactly the same ordering as the gold standard
- In the single-trial regime, the best methods reach τ_b ≈ 0.86
- Using greedy decoding as an empirical prior (Bayes_R0@N) reduces variance at N=1 by 16-52%
- Greedy priors can bias rankings when greedy and stochastic sampling disagree

**Limitations**: The evaluation concentrates on Olympiad-style math benchmarks (AIME, HMMT, BrUMO), and the greedy prior approach risks biasing rankings when greedy and stochastic sampling produce divergent results.

### He et al. (2026)

**Research question**: How can test-time scaling for code generation be made more efficient without relying on public test cases or requiring extensive LLM inference for candidate selection?

**Methodology**: The authors present DiffCodeGen, which generates diverse code candidates using various sampling and prompting strategies, applies coverage-guided fuzzing to synthesize inputs without existing tests, executes all candidates to capture dynamic behavior, clusters by behavioral similarity, and selects the medoid of the largest cluster.

**Key findings**:
- DiffCodeGen performs candidate selection without any extra LLM model calls, incurring little to no additional token consumption
- The method is fully asynchronous and naturally suited to agentic coding workflows
- Evaluated across 4 LLMs, DiffCodeGen demonstrates consistent improvements over baselines
- Compared to state-of-the-art test-time scaling methods, DiffCodeGen achieves competitive or superior performance while using only a fraction of time and tokens
- The approach is model-agnostic and can be combined with reasoning models to further boost performance

**Limitations**: The approach depends on coverage-guided fuzzing to synthesize inputs, which may not be effective for all code generation tasks, and evaluation was conducted on specific benchmarks that may not represent all practical coding scenarios.

### Kashaniyan and Jannesari (2026)

**Research question**: How does the candidate-generation strategy beyond just sample count affect the systems cost and efficiency of test-time scaling in LLMs?

**Methodology**: The authors fix N=8 and compare four generation schedules (1x8, 2x4, 4x2, 8x1) across Phi-3-mini and Qwen2.5-1.5B on 500 GSM8K prompts, measuring latency, throughput, GPU-hours, and GPU-device energy consumption.

**Key findings**:
- Increasing N from 1 to 8 improves accuracy by 8.4 points for Phi-3-mini and 18.4 points for Qwen2.5-1.5B
- Eight serial calls consume 4.64-4.86x more GPU-device energy than one batched call with eight candidates
- Eight serial calls have 5.77-6.12x the P95 latency of one batched call
- The efficiency pattern holds across three independently scheduled A100 nodes and in SciQ/V100 experiments
- Candidate count alone is insufficient to describe the systems cost of multi-candidate test-time scaling

**Limitations**: The experiments focus on specific models (Phi-3-mini, Qwen2.5-1.5B) and benchmarks (GSM8K, SciQ), and findings may not generalize to scenarios where candidates are interdependent or memory is constrained.

### Muennighoff et al. (2025)

**Research question**: What is the simplest approach to achieve test-time scaling and strong reasoning performance in language models?

**Methodology**: The authors curate s1K, a small dataset of 1,000 questions with reasoning traces based on difficulty, diversity, and quality criteria, and develop budget forcing to control test-time compute by terminating or extending the model's thinking process.

**Key findings**:
- s1-32B exceeds o1-preview on competition math questions by up to 27% (MATH and AIME24)
- Budget forcing enables performance extrapolation from 50% to 57% on AIME24
- The three curation criteria (difficulty, diversity, quality) were validated through ablations
- All model, data, and code are released as open-source

**Limitations**: Evaluation focuses primarily on competition mathematics benchmarks; budget forcing mechanism of appending 'Wait' may not generalize well to all reasoning domains; the 1,000-question dataset is relatively small.

### Wang et al. (2025)

**Research question**: What are the practical limits of test-time scaling and how can optimal resource allocation be achieved in large reasoning models?

**Methodology**: The authors introduce the Test-Time Scaling Performance Model (TTSPM) and theoretically analyze parallel and sequential scaling paradigms from a probabilistic modeling perspective to derive saturation points for both strategies.

**Key findings**:
- Saturation points are identified for both parallel and sequential scaling, marking thresholds beyond which additional computation yields diminishing returns
- Despite distinct mechanisms, both paradigms converge to a unified mathematical structure in their upper bounds
- Theoretical findings are empirically validated on AIME, MATH-500, and GPQA benchmarks
- The derived bounds provide practical guidance for test-time resource allocation

**Limitations**: Theoretical model may not capture all practical nuances of real-world deployment; validation limited to specific reasoning benchmarks; saturation point estimation requires careful calibration for different model architectures.

### Xiao et al. (2025)

**Research question**: How can test-time scaling be applied to RNN-based RWKV-7 models to improve performance without altering pre-trained weights?

**Methodology**: The authors develop an observer framework allowing smaller models to replicate RWKV-7 state dynamics, employ kernel methods to dynamically upscale state size, and integrate Decorrelated Backpropagation (DBP) to optimize the upscaled state matrix.

**Key findings**:
- State tuning achieves state-of-the-art performance on the target task by tuning only the state matrix
- A smaller model can outperform larger models using this approach
- The method preserves RWKV-7 architecture efficiency while harnessing test-time scaling power
- Three key innovations enable the approach: observer framework, kernel-based state upscaling, and DBP optimization

**Limitations**: Performance is demonstrated on a specific target task without clear evidence of generalizability to other domains; the method is specifically tailored to RWKV-7 architecture and may not transfer to other model types.

### Yu et al. (2025)

**Research question**: How can test-time scaling be extended beyond context length to maximize reasoning capacity across multiple dimensions?

**Methodology**: The authors propose a unified 3D test-time scaling framework integrating context scaling (reasoning length), batch scaling (parallel sampling), and turn scaling (iterative self-refinement), evaluated on challenging reasoning benchmarks with human preference feedback.

**Key findings**:
- Each dimension (context, batch, turn) demonstrates test-time scaling effect but with bounded capacity
- Combining all three dimensions substantially improves performance on IOI, IMO, and CPHO benchmarks
- The framework benefits from human preference feedback integration
- The human-in-the-loop approach extends to embodied learning for humanoid control behavior design

**Limitations**: Each scaling dimension has bounded capacity limiting maximum gains; human feedback requirement may limit scalability; evaluation concentrated on competitive reasoning benchmarks rather than broader applications.

### Zeng et al. (2025)

**Research question**: Do o1-like models (QwQ, Deepseek-R1, LIMO) genuinely exhibit test-time scaling capabilities, and how does chain-of-thought length affect their reasoning performance?

**Methodology**: The authors analyze whether longer CoTs improve accuracy in o1-like models, investigate the relationship between CoT length and self-revision patterns, compare sequential versus parallel scaling strategies, and propose Shortest Majority Vote combining parallel scaling with CoT length characteristics.

**Key findings**:
- Longer CoTs in o1-like models do not consistently enhance accuracy; correct solutions are often shorter than incorrect ones for the same questions
- The phenomenon is closely related to self-revision capabilities—longer CoTs contain more self-revisions, which often lead to performance degradation
- Parallel scaling achieves better coverage and scalability than sequential scaling on QwQ, R1, and LIMO
- Shortest Majority Vote significantly improves test-time scalability compared to conventional majority voting approaches

**Limitations**: The study concentrates on o1-like models (QwQ, Deepseek-R1, LIMO), and the Shortest Majority Vote approach may not generalize to models with different CoT behaviors or self-revision patterns.

## References

Ding, Y., & Zhang, L. (2026). SWE-Replay: Efficient test-time scaling for software engineering agents. arXiv. https://arxiv.org/abs/2601.22129

Ge, X., Zhang, Z., Huang, Y., Zhu, J., Yuan, L., Gu, W., Wu, W., Huang, W., Han, B., Zhang, X., & Yao, J. (2026). Towards understanding on-policy distillation through the lens of test-time scaling. arXiv. https://arxiv.org/abs/2608.11829

Hariri, M., Hinczewski, M., Ma, J., & Chaudhary, V. (2026). Ranking reasoning LLMs under test-time scaling. arXiv. https://arxiv.org/abs/2603.10960

He, Y., Wang, E., Wang, J., Ouyang, X., & Chen, H. (2026). Code generation by differential test time scaling. arXiv. https://arxiv.org/abs/2605.20473

Kashaniyan, M., & Jannesari, A. (2026). Sample count is not enough: Candidate-generation strategy shapes the energy and performance of LLM test-time scaling. arXiv. https://arxiv.org/abs/2609.19499

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. arXiv. https://arxiv.org/abs/2501.19393

Wang, J., Zhu, B., Leong, C. T., Li, Y., & Li, W. (2025). Scaling over scaling: Exploring test-time scaling plateau in large reasoning models. arXiv. https://arxiv.org/abs/2505.20522

Xiao, L., Zhiyuan, L., & Yueyu, L. (2025). State tuning: State-based test-time scaling on RWKV-7. arXiv. https://arxiv.org/abs/2504.05097

Yu, C., Tan, Q., Gao, J., Yu, S., Lu, H., Yang, X., Xu, Z., Wang, Y., Wu, Y., & Vinitsky, E. (2025). Extending test-time scaling: A 3D perspective with context, batch, and turn. arXiv. https://arxiv.org/abs/2511.15738

Zeng, Z., Cheng, Q., Yin, Z., Zhou, Y., & Qiu, X. (2025). Revisiting the test-time scaling of o1-like models: Do they truly possess test-time scaling capabilities? arXiv. https://arxiv.org/abs/2502.12215
