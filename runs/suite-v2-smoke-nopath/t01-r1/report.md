# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "LLM agent evaluation benchmarks", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agent evaluation benchmarks reveals a field rapidly maturing beyond simple task-completion metrics toward more nuanced, realistic, and safety-conscious evaluation paradigms. The ten papers surveyed collectively demonstrate three major shifts: (1) from synthetic, short-horizon tasks to long-horizon, native-runtime benchmarks that reflect actual deployment conditions; (2) from monolingual, culturally homogeneous evaluations to multilingual and regionally-aware benchmarks; and (3) from treating benchmarks as fixed infrastructure to actively auditing and certifying the evaluation process itself. A recurring theme is the gap between benchmark performance and real-world capability—frontier models often excel on existing benchmarks but struggle when evaluated in realistic clinical, scientific, or enterprise settings. The field is also beginning to address the meta-problem of who evaluates the evaluators, with automated auditing frameworks and certified selective automation emerging as solutions to the scalability crisis in agent evaluation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "LLM agent evaluation benchmarks", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Realism and Ecological Validity in Benchmark Design

A dominant thread across the surveyed literature is the push toward more realistic evaluation environments that mirror actual deployment conditions rather than simplified proxy tasks. WildClawBench exemplifies this trend by presenting 60 human-authored tasks that run inside reproducible Docker containers with real CLI agent harnesses and actual tools, averaging 8 minutes of wall-clock time and over 20 tool calls per task (Ding et al., 2026). Similarly, GPAgentBench-2K models primary-care clinical decision-making as a Constrained Markov Decision Process (CMDP) with six foundational clinical actions and a topological workflow prior, moving beyond the static predictions or unconstrained MDPs of prior clinical benchmarks (Chen et al., 2026). EnterpriseClawBench takes a different approach, deriving tasks from real workplace sessions rather than synthetic constructions (Zhong et al., 2026). This theme reflects a growing recognition that benchmark performance may not generalize to real-world deployment—a concern validated by findings that even frontier models violate safety constraints in over half of high-risk clinical cases despite high diagnosis accuracy (Chen et al., 2026).

### Theme 2: Benchmark Auditing and Certification

A second major theme addresses the reliability of the benchmarks themselves, recognizing that apparent agent failures may actually be benchmark failures. BenchGuard introduces the first framework for joint cross-artifact auditing of execution-based agent benchmarks, using structured LLM protocols to cross-verify all benchmark artifacts and optionally incorporating agent solutions or execution traces as diagnostic evidence (Tu et al., 2026). Deployed on ScienceAgentBench, BenchGuard identified 12 author-confirmed issues including fatal errors rendering tasks unsolvable, and matched 83.3% of expert-identified issues on BIXBench Verified-50 at a cost under USD 15 for 50 complex tasks. Complementary to this, Gan et al. (2026) tackle the scalability problem of human evaluation through certified selective automation, introducing a task-level bootstrap certificate that provides valid error rate guarantees even when trajectories arrive in correlated clusters. Their 4B logprob judge certified 30-59% of evaluation on tool-use and web corpora at alpha=0.1, with realized contamination bounded by alpha (0.000-0.041 across six harvests). This theme represents a maturation of the field from accepting benchmarks as given to treating them as artifacts requiring validation.

### Theme 3: Multilingual and Culturally-Aware Evaluation

The third theme addresses the cultural and linguistic limitations of existing benchmarks, which predominantly evaluate agents in English with Western cultural assumptions. Ticket-Bench introduces a multilingual benchmark for agent evaluation in soccer ticket purchase scenarios across six languages (Portuguese, English, Spanish, German, Italian, French) using localized teams, cities, and user profiles (Almeida et al., 2025). Results revealed notable cross-lingual disparities even in reasoning-oriented models like GPT-5 and Qwen3-235B, underscoring the need for culturally aware benchmarks. Similarly, GAIA-v2-LILT extends agent benchmarks beyond translation to multilingual adaptation, recognizing that direct translation fails to capture cultural nuances in task execution (Kim et al., 2026). X-WebAgentBench evaluates agents in multilingual interactive web environments, testing global capability rather than English-only performance (Wang et al., 2025). This theme reflects the field's growing awareness that agent evaluation must account for linguistic and cultural diversity to ensure robust global deployment.

### Theme 4: Automation and Meta-Evaluation of Agent Evaluation

The fourth theme addresses the cost and expertise required for agent evaluation through automation and meta-evaluation frameworks. EvalAgent encodes evaluation domain expertise as reusable skills that compose into a trace-based pipeline, improving the Eval@1 metric from 17.5% to 65% and achieving 79.5% human expert preference over baseline approaches (Zhou et al., 2026). The framework's ablation studies demonstrate that evaluation skills are critical—removing them causes Eval@1 to drop from 65% to 30%, indicating that strong coding ability alone does not translate to reliable agent evaluation. VISTA complements this by providing a toolkit with six metrics for measuring realism, capability coverage, and interaction effectiveness of simulated interactions, plus a hybrid user simulator integrating UI-based and API-based interactions (Lu et al., 2026). SAGE extends user simulation by incorporating top-down knowledge from business logic and bottom-up knowledge from business infrastructure, identifying up to 33% more agent errors than generic simulators (Shea et al., 2025). Together, these works address the scalability bottleneck in agent evaluation through automation and improved simulation.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that existing benchmarks are insufficient for evaluating real-world agent capability. WildClawBench, GPAgentBench-2K, and EnterpriseClawBench all demonstrate that frontier models perform significantly worse on realistic, long-horizon tasks than on synthetic benchmarks (Ding et al., 2026; Chen et al., 2026; Zhong et al., 2026). Similarly, BenchGuard and the certified selective automation work converge on the conclusion that benchmark infrastructure itself requires validation—Tu et al. (2026) found fatal errors in ScienceAgentBench, while Gan et al. (2026) showed that naive certificates can claim 98% automation while realized error exceeds the budget in 17.5% of task resamples. There is also convergence on the importance of multilingual evaluation, with Ticket-Bench, GAIA-v2-LILT, and X-WebAgentBench all demonstrating cross-lingual performance disparities (Almeida et al., 2025; Kim et al., 2026; Wang et al., 2025).

**Disagreements**: The surveyed literature does not exhibit direct contradictions, but there are differences in emphasis. Some works prioritize ecological validity and realism (WildClawBench, GPAgentBench-2K), accepting the trade-off of higher evaluation cost and complexity. Others prioritize scalability through automation and certification (EvalAgent, certified selective automation), accepting some abstraction from real-world conditions. The tension between these priorities—realism versus scalability—remains unresolved and represents an important direction for future work.

## Gaps and Open Questions

Several gaps emerge from the surveyed literature. First, none of the papers explicitly address the computational cost or environmental impact of running realistic, long-horizon benchmarks like WildClawBench (8 minutes per task) or GPAgentBench-2K (full clinical workflows), which may limit accessibility for smaller research groups. Second, while multilingual benchmarks are emerging, none address low-resource languages beyond the six major languages in Ticket-Bench, leaving a significant gap in global coverage. Third, the automated evaluation frameworks (EvalAgent, VISTA, SAGE) all rely on frontier LLMs for meta-evaluation, creating a circular dependency that may limit their ability to detect systematic biases in the evaluators themselves. Fourth, while benchmark auditing is emerging as a theme, there is no standardized protocol for how frequently benchmarks should be re-audited or how to handle discovered issues in published benchmark results. Finally, the clinical and scientific benchmarks (GPAgentBench-2K, ScienceAgentBench) raise ethical questions about using real-world data and workflows that are not explicitly addressed in the surveyed papers.

## Per-Paper Annotations

### Almeida et al. (2025)

**Research question**: How can agent evaluation benchmarks account for cultural and linguistic diversity beyond monolingual or naively translated benchmarks?
**Methodology**: The authors introduce Ticket-Bench, a multilingual benchmark for agent evaluation in task-oriented soccer ticket purchase scenarios across six languages (Portuguese, English, Spanish, German, Italian, French) using localized teams, cities, and user profiles, evaluating commercial and open-source LLMs on function-calling accuracy and consistency.
**Key findings**:
- Reasoning-oriented models (e.g., GPT-5, Qwen3-235B) dominate performance across languages
- Even top models exhibit notable cross-lingual disparities in function-calling accuracy
- Existing agent evaluations largely overlook cultural and linguistic diversity
- Results underscore the need for culturally aware, multilingual benchmarks for robust LLM agent development
**Limitations**: Limited to six major languages; does not address low-resource languages or cultural contexts beyond soccer ticket purchasing.

### Chen et al. (2026)

**Research question**: How can LLM agents be evaluated in realistic primary-care clinical decision-making with constrained action spaces and safety requirements?
**Methodology**: The authors introduce GPAgentBench-2K as the first Constrained MDP (CMDP) LLM-agent benchmark for primary-care clinical decision-making, constructed from expert-validated records of real-world GP encounters with six foundational clinical actions and a topological workflow prior, evaluating 16 state-of-the-art LLMs and establishing a reference point using Constrained Group Relative Policy Optimization (C-GRPO).
**Key findings**:
- Performance degrades significantly as the clinical action space scales
- A clinical quality-safety gap exists: frontier models with highest diagnosis accuracy violate safety constraints in over half of high-risk cases
- Explicitly modeling constraints improves performance over unconstrained RL methods but remains far from clinically acceptable safety
- The benchmark operationalizes safety-informed abstention as a first-class outcome
**Limitations**: Limited to primary-care scenarios; clinical validation of the benchmark itself is not addressed.

### Ding et al. (2026)

**Research question**: Can current frontier models effectively complete realistic long-horizon work in native runtime environments where agents are actually deployed?
**Methodology**: The authors created WildClawBench, a native-runtime benchmark of 60 human-authored, bilingual, multimodal tasks running inside reproducible Docker containers with real CLI agent harnesses and actual tools, using hybrid grading combining deterministic checks, environment-state auditing, and LLM/VLM judges.
**Key findings**:
- Most agent benchmarks rely on synthetic sandboxes, short-horizon tasks, mock-service APIs, and final-answer checks, leaving open whether agents can complete realistic long-horizon work
- Each task averages roughly 8 minutes of wall-clock time and over 20 tool calls
- Across 19 frontier models, the best (Claude Opus 4.7) reaches only 62.2% overall under OpenClaw
- Every other model stays below 60% performance
- Switching harness alone can shift a single model's performance by up to 18 points
**Limitations**: The benchmark shows that long-horizon, native-runtime agent evaluation remains a far-from-resolved task for current frontier models.

### Gan et al. (2026)

**Research question**: What fraction of LLM agent evaluation can be automated with a certificate that the error rate among auto-decided trajectories stays below a specified budget?
**Methodology**: The authors introduce a task-level bootstrap certificate that provides valid error rate guarantees even when trajectories arrive in correlated clusters, and evaluate it using a 4B logprob judge trained with SFT and reject-weighted GRPO on tool-use and web corpora.
**Key findings**:
- Existing selective-judging methods with i.i.d. certificates can overstate safe automation, with naive certificates claiming 98% automation while realized error exceeds the budget in 17.5% of task resamples
- The task-level bootstrap certificate is valid across all tested regimes while matching the naive certificate's coverage
- A 4B logprob judge certified 0.30-0.59 of evaluation on tool-use and web corpora at alpha=0.1
- Certified coverage is highly predictable from base rate and discrimination alone (R^2=0.96)
- The certificate serves as a self-training filter with contamination bounded by alpha (realized 0.000-0.041 across six harvests)
**Limitations**: Finite-sample cluster-valid alternatives fail to certify anything at realistic task counts.

### Lu et al. (2026)

**Research question**: How can user-simulation-based evaluation be improved to better capture the dynamic, multi-step nature of agentic behavior and expose meaningful failure modes?
**Methodology**: The authors developed VISTA, a toolkit with six metrics for measuring realism, capability coverage, and interaction effectiveness of simulated interactions, plus a hybrid user simulator integrating both UI-based and API-based interactions, evaluated in e-commerce and customer service settings.
**Key findings**:
- Existing user-simulation frameworks provide limited mechanisms for evaluating the quality and comprehensiveness of simulated interactions
- Most frameworks are restricted to either UI-only or API-only actions, limiting their ability to model realistic user behaviors
- VISTA's six metrics enable measurement of realism, capability coverage, and interaction effectiveness
- The hybrid simulator enables more realistic and comprehensive evaluation across diverse interactive environments
- Results demonstrate VISTA produces more realistic and comprehensive evaluations than existing methods
**Limitations**: Evaluation limited to e-commerce and customer service domains; generalizability to other domains not tested.

### Shea et al. (2025)

**Research question**: How can user simulation for multi-turn agent evaluation be improved by incorporating domain-specific knowledge from business contexts?
**Methodology**: SAGE integrates top-down knowledge from business logic (e.g., ideal customer profiles) and bottom-up knowledge from business agent infrastructure (e.g., product catalogs, FAQs, knowledge bases) to generate realistic, knowledge-grounded user interactions.
**Key findings**:
- Existing user simulation approaches typically model generic users and overlook domain-specific principles required to capture realistic behavior
- Top-down knowledge grounds user behavior in realistic customer personas
- Bottom-up knowledge from business infrastructure allows the simulator to generate interactions reflecting users' information needs and expectations
- The approach produces interactions that are more realistic and diverse
- SAGE identifies up to 33% more agent errors, highlighting its effectiveness for bug-finding and iterative agent improvement
**Limitations**: Requires access to business infrastructure and domain knowledge; may not generalize to non-commercial settings.

### Tu et al. (2026)

**Research question**: Can frontier LLMs systematically audit evaluation infrastructure to identify benchmark failures that penalize valid agent approaches?
**Methodology**: The authors propose BenchGuard, the first framework for joint cross-artifact auditing of execution-based agent benchmarks that uses structured LLM protocols to cross-verify all benchmark artifacts, optionally incorporating agent solutions or execution traces as diagnostic evidence.
**Key findings**:
- BenchGuard identified 12 author-confirmed issues in ScienceAgentBench, including fatal errors rendering tasks unsolvable
- The framework exactly matched 83.3% of expert-identified issues on BIXBench Verified-50 subset, catching defects prior human review missed
- A full audit of 50 complex bioinformatics tasks costs under USD 15
- The framework demonstrates cross-format applicability through a preliminary native-format audit of ProgramBench
**Limitations**: Validation limited to two scientific benchmarks; performance on other domains not evaluated.

### Wang et al. (2025)

**Research question**: How can agent evaluation benchmarks assess global capability in multilingual interactive web environments?
**Methodology**: X-WebAgentBench is a multilingual interactive web benchmark for evaluating global agent capability, testing agents across multiple languages in realistic web interaction scenarios.
**Key findings**:
- Existing benchmarks predominantly evaluate agents in English-only settings
- Multilingual web interaction presents unique challenges beyond translation
- Agent performance varies significantly across languages even for the same underlying task
- Interactive web environments require different evaluation criteria than static task completion
**Limitations**: Specific quantitative results not detailed in abstract; full evaluation scope unclear.

### Zhang et al. (2025)

**Research question**: How can we comprehensively and rigorously evaluate LLM capabilities in data science tasks beyond single-task benchmarks with straightforward metrics?
**Methodology**: The authors develop DataSciBench using a semi-automated pipeline that generates ground truth and validates evaluation metrics through LLM-based self-consistency and human verification, proposing a Task-Function-Code (TFC) framework to assess code execution outcomes and testing 23 models on curated challenging prompts.
**Key findings**:
- API-based models outperform open-sourced models on all evaluation metrics
- Deepseek-Coder-33B-Instruct achieves the highest score among open-sourced models
- DataSciBench provides more comprehensive evaluation through uncertain ground truth and complex prompts compared to existing benchmarks
- The TFC framework enables programmatic assessment based on precisely defined metrics and rules
**Limitations**: Focused on data science domain; generalizability to other domains not tested.

### Zhou et al. (2026)

**Research question**: Can frontier coding assistants reliably automate the complex process of agent evaluation involving multi-step behaviors and tool use?
**Methodology**: The authors conduct an empirical study showing that simply prompting coding assistants is insufficient, then introduce EvalAgent that encodes evaluation domain expertise as evaluation skills composing into a trace-based pipeline, assessing generated evaluations using a meta-evaluation framework and AgentEvalBench benchmark (20 agents) with the proposed Eval@1 metric.
**Key findings**:
- Frontier coding assistants achieve only 30% execution success rate without domain-specific evaluation knowledge
- EvalAgent improves Eval@1 from 17.5% to 65%, achieving 79.5% human expert preference over baseline approaches
- Evaluation skills are critical for handling complex evaluation: removing them causes Eval@1 to drop from 65% to 30%
- Strong coding ability does not automatically translate to reliable agent evaluation
**Limitations**: Evaluated on 20 agents in AgentEvalBench; scalability to larger agent pools not tested.

## References

Almeida, T. S., Santos, J. G. A., Laitz, T., & Bonás, G. K. (2025). Ticket-Bench: A kickoff for multilingual and regionalized agent evaluation. arXiv. https://arxiv.org/abs/2509.14477

Chen, B., Liu, X., Ao, Y., Do, H., & Qiu, J. (2026). GPAgentBench-2K: Benchmarking large language model agents in complex clinical action space. arXiv. https://arxiv.org/abs/2608.30188

Ding, S., Dai, X., Xing, L., Ding, S., Liu, Z., JingYi, Y., Yang, P., Zhang, Z., Wei, X., Fang, X., Ma, Y., Duan, H., Shao, J., Wang, J., Lin, D., Chen, K., & Zang, Y. (2026). WildClawBench: A benchmark for real-world, long-horizon agent evaluation. arXiv. https://arxiv.org/abs/2605.10912

Gan, C., Liang, Y., Zhang, Q., & Ni, S. (2026). Certified selective automation of LLM agent evaluation. arXiv. https://arxiv.org/abs/2609.34320

Kim, Y., Zhang, S., & Choi, J. (2026). GAIA-v2-LILT: Multilingual adaptation of agent benchmark beyond translation. arXiv. https://arxiv.org/abs/2604.24929

Lu, Y., Shea, R., Zhang, Y., & Yu, Z. (2026). VISTA: A versatile interactive user simulation toolkit for agent evaluation. arXiv. https://arxiv.org/abs/2606.11079

Shea, R., Lu, Y., Qiu, L., & Yu, Z. (2025). SAGE: A top-down bottom-up knowledge-grounded user simulator for multi-turn agent evaluation. arXiv. https://arxiv.org/abs/2510.11997

Tu, X., Wang, T., Lu, Y., Huang, K., Qu, Y., & Mostafavi, S. (2026). Who guards the benchmarks? Automated auditing of LLM agent benchmarks. arXiv. https://arxiv.org/abs/2604.24955

Wang, P., Liu, X., & Chen, J. (2025). X-WebAgentBench: A multilingual interactive web benchmark for evaluating global agent capability. arXiv. https://arxiv.org/abs/2609.13582

Zhang, D., Zhoubian, S., Cai, M., Li, F., Yang, L., Wang, W., Dong, T., Hu, Z., Tang, J., & Yue, Y. (2025). DataSciBench: An LLM agent benchmark for data science. arXiv. https://arxiv.org/abs/2502.13897

Zhou, K., Woo, S., Ding, H., Ramnath, K., Chidambaram, S., Feng, A., Arannil, V., Kim, M., Singh, I., Wang, D., Xu, Z., Gandhi, M., Prabhu, N., Mishra, S. S., Dhakecha, S., Singh, V., Pandeshwar, G., & Cheong, L. L. (2026). An empirical study of automating agent evaluation. arXiv. https://arxiv.org/abs/2605.11378
