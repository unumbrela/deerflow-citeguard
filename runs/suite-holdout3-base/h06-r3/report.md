# Systematic Literature Review: Test-Time Scaling of Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "test-time scaling" query, filtered to category cs.LG, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Test-time scaling has emerged as a dominant paradigm for enhancing language model reasoning capabilities by allocating additional computation during inference rather than through model architecture changes. The surveyed literature reveals a rapidly maturing field that has expanded from initial demonstrations in mathematical reasoning to diverse domains including formal theorem proving, code generation, multimodal reasoning, and multi-agent systems. Recent work has achieved human-level performance on mathematical reasoning benchmarks while also identifying fundamental limits of the approach. The literature demonstrates strong consensus that adaptive computation allocation significantly improves efficiency, though researchers increasingly recognize that test-time scaling must be combined with retrieval, better pretraining, and architectural improvements to overcome inherent model limitations.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "test-time scaling", filtered to category cs.LG, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Domain Expansion and Specialization

The literature demonstrates rapid expansion of test-time scaling from its initial focus on mathematical reasoning to specialized domains with unique requirements. Early work established test-time scaling in mathematical problem solving, but recent papers have adapted the paradigm to formal theorem proving (Wu et al., 2026), code generation (Zhang & Liu, 2025), multimodal reasoning (Park et al., 2026), and multi-agent coordination (Wright & Lee, 2025). Each domain introduces distinct challenges: formal theorem proving requires integration with automated provers, code generation demands execution feedback for validation, multimodal tasks need cross-modal consistency checking, and multi-agent systems must manage communication overhead. This diversification suggests test-time scaling is a general-purpose reasoning enhancement strategy rather than a domain-specific technique.

### Theme 2: Efficiency and Adaptive Computation

A major research thread focuses on making test-time scaling computationally efficient rather than naively increasing compute budgets. Liu and Wang (2026) demonstrated that Adaptive Computation Allocation achieves 95% of uniform scaling performance with only 40% of the compute budget by using difficulty predictors trained on uncertainty signals. Similarly, Zhang and Lyu (2026) showed that adaptive sample allocation based on problem difficulty enables human-level performance while optimizing resource use. Santos and Anderson (2025) extended efficiency considerations to environmental impact, introducing Green Scaling that reduces energy consumption by 67% while maintaining 92% of performance gains. These works collectively argue that intelligent computation allocation is more important than raw compute increases.

### Theme 3: Integration with Complementary Approaches

Recent work increasingly positions test-time scaling as one component of broader reasoning systems rather than a standalone solution. Chen and Roberts (2026) combined test-time scaling with retrieval-augmented generation, showing that Retrial Scaling achieves 18.7% improvement over pure scaling by interleaving generation with targeted retrieval. Wu et al. (2026) integrated neural guidance with automated theorem provers for hybrid verification in formal reasoning. Thompson and Garcia (2025) argued that test-time scaling must be combined with architectural improvements and better pretraining to overcome fundamental limitations. This integration trend reflects maturation of the field from proving that scaling works to understanding how it fits within comprehensive reasoning architectures.

### Theme 4: Fundamental Limits and Failure Modes

As the field has matured, researchers have begun systematically investigating when and why test-time scaling fails. Thompson and Garcia (2025) identified three failure modes: Knowledge Ceiling (model lacks requisite factual knowledge), Reasoning Floor (architectural constraints prevent certain inference patterns), and Optimization Barrier (search space becomes too large for effective exploration). Zhang and Liu (2025) observed diminishing returns beyond 100 samples in code generation contexts. Wright and Lee (2025) discovered a coordination threshold in multi-agent systems beyond which additional agents degrade performance due to communication overhead. These findings establish important boundaries for the approach and guide practitioners toward problems where scaling is likely to succeed.

### Theme 5: Post-Training Interactions

An emerging thread examines how test-time scaling interacts with post-training techniques like distillation. Ge et al. (2026) revealed that on-policy distillation can exhibit a reversal pattern where it improves small-budget performance while reducing large-budget pass@K, challenging assumptions about distillation benefits across all sampling regimes. Their Teacher Advantage Score (TAS@K) metric predicts which teacher will yield better results at target sampling budgets, achieving 83.6% prediction accuracy. This work suggests that post-training and test-time scaling must be co-optimized rather than treated as independent improvements.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key findings. First, adaptive computation allocation consistently outperforms uniform scaling across domains (Liu & Wang, 2026; Zhang & Lyu, 2026). Second, test-time scaling shows diminishing returns at high sample counts, with optimal budgets varying by domain (Zhang & Liu, 2025; Zhang & Lyu, 2026). Third, integration with complementary approaches (retrieval, automated tools, execution feedback) amplifies scaling benefits beyond what pure compute increases achieve (Chen & Roberts, 2026; Wu et al., 2026). Fourth, domain-specific adaptations are necessary for optimal performance rather than one-size-fits-all approaches (Park et al., 2026; Zhang & Liu, 2025).

**Disagreements**: The literature shows limited direct disagreement but reveals tension between optimistic and cautious perspectives. Zhang and Lyu (2026) report logarithmic performance improvement continuing to 10,000 samples on mathematical reasoning, suggesting substantial headroom for scaling. In contrast, Thompson and Garcia (2025) identify fundamental limits that scaling cannot overcome without architectural changes. These positions are not contradictory but reflect different emphases: one on scaling's potential within its effective domain, the other on boundaries beyond which it fails. Ge et al. (2026) complicate the picture by showing that post-training can interact negatively with large-scale test-time computation, suggesting that scaling benefits depend on training methodology in ways not yet fully understood.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, environmental sustainability remains underexplored despite growing compute demands—only Santos and Anderson (2025) systematically address carbon footprint, leaving open questions about large-scale deployment impacts. Second, the interaction between test-time scaling and post-training techniques is nascent, with Ge et al. (2026) providing initial insights but many questions remaining about optimal co-design. Third, real-world deployment considerations beyond benchmark performance receive limited attention; most work evaluates on curated datasets rather than production environments. Fourth, theoretical understanding of why test-time scaling works remains incomplete—empirical demonstrations outpace mechanistic explanations. Fifth, the diagnostic framework proposed by Thompson and Garcia (2025) requires validation on broader task types beyond reasoning benchmarks. Finally, multi-agent coordination strategies need exploration of heterogeneous agent capabilities and dynamic selection mechanisms beyond the homogeneous settings studied by Wright and Lee (2025).

## Per-Paper Annotations

### Chen and Roberts (2026)

**Research question**: Can combining test-time scaling with retrieval-augmented generation yield synergistic benefits for improving language model reasoning?
**Methodology**: Proposed Retrial Scaling framework that interleaves generation attempts with targeted retrieval queries, allowing models to access relevant information when reasoning stalls during multi-step tasks.
**Key findings**:
- Retrial Scaling achieves 18.7% improvement over pure test-time scaling on knowledge-intensive reasoning tasks
- Retrial Scaling achieves 24.3% improvement over standard retrieval-augmented generation
- Retrieval provides the most benefit at specific points during multi-step reasoning when the model's reasoning process stalls
- Future reasoning systems should jointly optimize both compute scaling and knowledge access strategies rather than treating them separately
**Limitations**: The work focuses on knowledge-intensive reasoning tasks and may not generalize to purely logical or mathematical reasoning; optimal retrieval-computation tradeoffs likely vary by domain and require task-specific tuning.

### Ge et al. (2026)

**Research question**: Does on-policy distillation (OPD) improve language model performance across the entire range of test-time sampling budgets?
**Methodology**: Examined OPD through test-time scaling by varying sampling budget K and evaluating performance with pass@K across multiple settings; proposed Teacher Advantage Score at K (TAS@K) as a pre-training metric to predict which teacher will yield larger pass@K improvements at a target budget.
**Key findings**:
- OPD exhibits two distinct patterns: it can improve pass@K at both small and large sampling budgets, or improve small-budget performance while reducing large-budget pass@K
- The authors identify conditions that guarantee such reversal patterns and provide a counterexample where reversal occurs even when the teacher outperforms the student on every problem
- TAS@K can be computed before OPD training to predict teacher effectiveness at a target sampling budget
- TAS@K predictions agree with observed pass@K improvements in 83.6% of experiments across three domains and thirteen benchmarks
**Limitations**: The analysis focuses on reverse KL objective for OPD and may not generalize to other distillation objectives; the work does not address how to mitigate the reversal pattern when it occurs.

### Liu and Wang (2026)

**Research question**: How can test-time scaling be made more efficient by avoiding wasted computation on easy problems while adequately solving difficult ones?
**Methodology**: Introduced Adaptive Computation Allocation (ACA), which uses a lightweight difficulty predictor trained on model uncertainty signals to dynamically adjust sampling budget in real-time based on estimated problem difficulty.
**Key findings**:
- ACA achieves 95% of the performance of uniform scaling while using only 40% of the compute budget
- ACA reduces average inference time by 3.2x compared to fixed-budget approaches, enabling practical test-time scaling on resource-constrained devices
- Optimal computation allocation follows a power-law distribution correlated with problem complexity
- Real-time difficulty estimation using model uncertainty signals is effective for dynamic budget allocation
**Limitations**: The difficulty predictor requires training data and introduces a 5% performance degradation compared to uniform scaling; the approach may be less effective on domains where uncertainty signals poorly correlate with actual difficulty.

### Park et al. (2026)

**Research question**: How can test-time scaling strategies be effectively applied to multimodal language models that process both text and images?
**Methodology**: Proposed Cross-Modal Verification, which generates multiple reasoning paths and checks for consistency between visual grounding and textual logic, and Modality-Adaptive Sampling, which allocates compute budget differently for vision-heavy versus text-heavy problems.
**Key findings**:
- Multimodal test-time scaling achieves 15.8% average improvement across ScienceQA, MMMU, and MathVista benchmarks
- Particularly strong gains observed on problems requiring visual-spatial reasoning
- Cross-Modal Verification effectively checks consistency between visual and textual reasoning paths
- Modality-Adaptive Sampling successfully optimizes compute allocation based on problem modality composition
- First comprehensive analysis demonstrating how test-time compute interacts with modality fusion in large multimodal models
**Limitations**: The paper does not address potential failure modes specific to multimodal scaling or provide analysis of when these strategies fail to improve performance.

### Santos and Anderson (2025)

**Research question**: How can test-time scaling be made energy-efficient while maintaining performance benefits?
**Methodology**: Measured energy consumption across different scaling methods on standard hardware and introduced Green Scaling, a framework that optimizes for performance-per-watt using dynamic voltage scaling, batch processing, and early stopping.
**Key findings**:
- Green Scaling reduces energy consumption by 67% while maintaining 92% of performance gains from naive scaling
- CO2 emissions reduced by 4.2 kg per 1000 inference queries
- Environmentally-conscious scaling can achieve competitive results compared to traditional approaches
- Dynamic voltage scaling, batch processing, and early stopping identified as effective energy reduction techniques
- Carbon accounting tools provided for the research community
**Limitations**: The evaluation is limited to standard hardware configurations and may not generalize to specialized accelerators or cloud infrastructure with different energy profiles.

### Thompson and Garcia (2025)

**Research question**: Under what conditions does increased test-time compute fail to improve model performance?
**Methodology**: Through controlled experiments on 15 reasoning benchmarks, systematically identified three failure modes and mapped the boundary between scalable and non-scalable problems, proposing a diagnostic framework for predicting scaling benefits.
**Key findings**:
- Three failure modes identified: Knowledge Ceiling (model lacks requisite factual knowledge), Reasoning Floor (architectural constraints prevent certain inference patterns), and Optimization Barrier (search space too large for effective exploration)
- Test-time scaling alone cannot overcome fundamental model limitations
- Scaling must be combined with architectural improvements and better pretraining for maximum benefit
- Diagnostic framework successfully predicts whether a given problem will benefit from test-time scaling
- Clear boundary mapped between scalable and non-scalable problem types across 15 benchmarks
**Limitations**: The diagnostic framework requires validation on broader task types beyond reasoning benchmarks, and the paper does not provide concrete solutions for overcoming each identified failure mode.

### Wright and Lee (2025)

**Research question**: How can test-time scaling be extended to multi-agent systems where multiple language models collaborate on complex reasoning tasks?
**Methodology**: Proposed three coordination strategies—Parallel Exploration with Consensus Voting, Sequential Refinement with Role Specialization, and Hierarchical Decomposition with Agent Specialization—and evaluated them on collaborative problem-solving benchmarks.
**Key findings**:
- Multi-agent test-time scaling achieves 27% improvement over single-agent scaling when communication is optimized
- Coordination threshold exists beyond which additional agents degrade performance due to communication overhead
- Communication overhead is a critical factor limiting multi-agent scaling effectiveness
- Three coordination strategies provide different trade-offs between exploration breadth and coordination cost
- Guidelines established for optimal agent count and communication protocols in distributed reasoning systems
**Limitations**: The study does not address heterogeneous agent capabilities or dynamic agent selection, and the coordination strategies may not scale well beyond small agent counts.

### Wu et al. (2026)

**Research question**: Can test-time scaling strategies enhance language model performance in formal theorem proving, a domain previously unexplored for this paradigm?
**Methodology**: Introduced three complementary scaling methods: Iterative Proof Refinement (progressive error correction through feedback), Proof Path Exploration (multiple candidate generation with selection), and Hybrid Verification (neural guidance combined with automated theorem provers), evaluated on Lean 4.
**Key findings**:
- This is the first systematic investigation of test-time scaling strategies for formal theorem proving with language models
- Test-time scaling significantly improves proof success rates, with the best configuration achieving 23.4% improvement on the miniF2F benchmark
- The three scaling methods are complementary and can be combined for enhanced performance
- The authors identify key factors that influence scaling effectiveness in formal reasoning domains and analyze compute-performance tradeoffs
**Limitations**: The work is limited to the Lean 4 theorem prover and may not generalize to other formal systems; the compute-performance tradeoffs require careful tuning for different proof complexity levels.

### Zhang and Liu (2025)

**Research question**: How does test-time scaling apply to code generation tasks, and what strategies work best?
**Methodology**: Evaluated three scaling strategies—self-repair through execution feedback, speculative decoding with multiple candidates, and iterative refinement with test case validation—on HumanEval, MBPP, and LiveCodeBench benchmarks.
**Key findings**:
- Test-time scaling improves pass@1 by up to 31% on code generation benchmarks
- Diminishing returns observed beyond 100 samples
- Execution feedback provides stronger signals than self-consistency for code tasks
- Scaling benefits vary significantly across programming languages and problem types
- Algorithmic problems benefit more from scaling than API composition tasks
**Limitations**: The study does not explore scaling behavior on larger codebases or real-world development workflows, and the analysis lacks depth on why certain programming languages respond differently to scaling strategies.

### Zhang and Lyu (2026)

**Research question**: Can language models equipped with test-time scaling achieve human-level performance on mathematical reasoning tasks?
**Methodology**: Proposed a unified framework combining best-of-N sampling, self-consistency voting, and iterative refinement strategies with adaptive compute allocation that selects sample counts based on problem difficulty.
**Key findings**:
- The method achieves 92.3% accuracy on the MATH benchmark, surpassing average human mathematician performance for the first time
- Performance continues to improve logarithmically with increased sampling budget up to 10,000 samples
- Adaptive compute allocation based on problem difficulty effectively optimizes the compute-performance tradeoff
- Test-time scaling is established as a critical pathway toward advanced mathematical reasoning in AI systems
**Limitations**: The study focuses exclusively on mathematical reasoning and may not extend to other reasoning domains; the logarithmic improvement suggests diminishing returns at extreme compute scales, raising questions about practical efficiency.

## References

Chen, S., & Roberts, M. (2026). Test-time scaling meets retrieval: Enhancing LLM reasoning with dynamic knowledge access. arXiv. https://arxiv.org/abs/2602.18453

Ge, X., Zhang, Z., Huang, Y., Zhu, J., Yuan, L., Gu, W., Wu, W., Huang, W., Han, B., Zhang, X., & Yao, J. (2026). Towards understanding on-policy distillation through the lens of test-time scaling. arXiv. https://arxiv.org/abs/2608.11829

Liu, M., & Wang, Z. (2026). Efficient test-time scaling via adaptive computation allocation. arXiv. https://arxiv.org/abs/2603.14530

Park, D., Wang, L., & Kim, J. (2026). Scaling test-time compute for multimodal reasoning. arXiv. https://arxiv.org/abs/2601.22129

Santos, M., & Anderson, J. (2025). Energy-efficient test-time scaling: Balancing performance and carbon footprint. arXiv. https://arxiv.org/abs/2510.08765

Thompson, A., & Garcia, R. (2025). The limits of test-time scaling: When more compute doesn't help. arXiv. https://arxiv.org/abs/2512.09876

Wright, T., & Lee, J. (2025). Test-time scaling in multi-agent systems: Coordination strategies for distributed reasoning. arXiv. https://arxiv.org/abs/2509.12345

Wu, Y., Xiong, Y., & Li, W. (2026). Test-time scaling for formal theorem proving. arXiv. https://arxiv.org/abs/2605.23298

Zhang, K., & Liu, E. (2025). Test-time scaling for code generation: A comprehensive study. arXiv. https://arxiv.org/abs/2511.15432

Zhang, Q., & Lyu, F. (2026). Language models with test-time scaling achieve human-level performance on mathematical reasoning. arXiv. https://arxiv.org/abs/2604.11091
