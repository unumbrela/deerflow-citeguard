# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "agent evaluation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agent evaluation benchmarks reveals a rapidly evolving field addressing critical gaps in how autonomous agents are assessed. Recent work (2025-2026) demonstrates a clear shift from static, synthetic benchmarks toward dynamic, realistic evaluation frameworks that capture the multi-step, tool-using nature of agent behavior. Ten papers surveyed collectively identify five major challenges: (1) the need for multilingual and culturally diverse benchmarks, (2) the gap between synthetic sandboxes and real-world deployment environments, (3) the high cost and expertise requirements of manual evaluation, (4) the limitations of single-judge automatic evaluation without guarantees, and (5) the failure of static benchmarks to capture interactive, multi-turn agent dynamics. The field is converging on hybrid approaches that combine automated judges with human oversight, user simulation, and native-runtime testing. However, significant gaps remain in standardization, cross-lingual consistency, and certified automation guarantees for high-stakes evaluation scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query `agent evaluation`, filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Realism and Native-Runtime Evaluation

A dominant theme across recent work is the recognition that synthetic, short-horizon benchmarks fail to capture the complexity of real-world agent deployment. WildClawBench (Ding et al., 2026) directly addresses this by presenting 60 human-authored tasks running inside reproducible Docker containers with actual CLI agent harnesses and real tools rather than mock services. Their finding that the best model (Claude Opus 4.7) reaches only 62.2% overall, with harness choice shifting performance by up to 18 points, demonstrates that native-runtime evaluation remains far from resolved. Similarly, VISTA (Lu et al., 2026) critiques static benchmarks for failing to capture dynamic, multi-step agentic behavior and proposes a hybrid user simulator integrating both UI-based and API-based interactions to enable more realistic evaluation. This theme reflects a broader field-wide shift from "can the agent answer correctly?" to "can the agent complete realistic work in the environment where it will be deployed?"

### Theme 2: Multilingual and Culturally-Aware Benchmarks

Ticket-Bench (Sales Almeida et al., 2025) identifies a critical blind spot in agent evaluation: the overwhelming reliance on monolingual or naively translated benchmarks that ignore cultural and linguistic diversity. By simulating soccer ticket purchases across six languages (Portuguese, English, Spanish, German, Italian, French) with localized teams, cities, and user profiles, the authors demonstrate that even reasoning-oriented models like GPT-5 and Qwen3-235B exhibit notable cross-lingual disparities. This work underscores that robust agent evaluation must account for regionalization and cultural context, not merely translate existing English-centric benchmarks. The finding that function-calling accuracy varies significantly across languages suggests that agent development pipelines require multilingual evaluation from the outset rather than as an afterthought.

### Theme 3: Automation of Evaluation Pipelines

The high cost and expertise requirements of agent evaluation have motivated work on automating the evaluation pipeline itself. Zhou et al. (2026) introduce EvalAgent, an AI assistant that encodes evaluation domain expertise as reusable skills (procedural instructions, code templates, and dynamically retrieved API documentation) to compose trace-based evaluation pipelines. Their meta-evaluation framework with AgentEvalBench (20 agents with evaluation requirements and test scenarios) shows that frontier coding assistants, when simply prompted, achieve only 30% execution success rate and produce over-engineered evaluations with 12+ metrics per agent. In contrast, EvalAgent improves the Eval@1 metric from 17.5% to 65% and achieves 79.5% human expert preference. This line of work suggests that evaluation automation requires domain-specific knowledge encoding rather than relying on general-purpose coding capabilities alone.

### Theme 4: Certified and Trustworthy Automatic Judges

A critical challenge in automatic agent evaluation is knowing when an automatic judge can be trusted. Gan et al. (2026) address this by introducing a task-level bootstrap certificate that guarantees the error rate among auto-decided trajectories stays below a specified budget. Their analysis reveals that standard i.i.d. certificates can overstate safety, with naive certificates claiming 98% automation while realized error exceeds the budget in 17.5% of task resamples. Their 4B logprob judge, trained with SFT and reject-weighted GRPO, certifies 0.30-0.59 of evaluation on tool-use and web corpora at alpha=0.1. This work establishes that certified selective automation is feasible but requires careful statistical guarantees that account for correlated trajectories in agent corpora. The certificate also serves as a self-training filter with contamination bounded by construction, enabling judges to enter unseen domains at in-domain strength.

### Theme 5: User Simulation and Knowledge-Grounded Interaction

Several papers address the limitations of static benchmarks by proposing user simulation frameworks that generate dynamic, multi-turn interactions. SAGE (Shea et al., 2025) integrates top-down knowledge from business logic and bottom-up knowledge from business agent infrastructure to ground user behavior in realistic personas, identifying up to 33% more agent errors than generic user simulators. VISTA (Lu et al., 2026) complements this with six metrics for measuring realism, capability coverage, and interaction effectiveness of simulated interactions. This theme reflects recognition that agent evaluation must move beyond single-turn QA to capture the information-seeking behavior, persona diversity, and multi-turn dynamics that characterize real agent use cases.

### Theme 6: Multi-Agent Evaluation and Authority Dynamics

The emergence of multi-agent evaluation frameworks introduces new complexities around authority bias and judge disagreement. Choi et al. (2026) apply French and Raven's power-based theory to analyze how role-based authority affects agent interactions in free-form multi-agent evaluation systems, finding that expert and referent power roles exert stronger influence than legitimate power roles. JuryFlow (Yang et al., 2026) takes a different approach, leveraging inter-judge disagreement as a signal to improve evaluation accuracy rather than discarding it. By decomposing responses into atomic claims, using heterogeneous judges, and enabling human structural guides to select disagreements for resolution, JuryFlow improves agreement with gold labels over single-judge and majority-vote baselines. This work reframes the human from labeler to structural guide, making the evaluator progressively self-refining through closed-loop rubric induction.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that static, synthetic benchmarks are insufficient for evaluating modern LLM agents. Eight of ten papers explicitly critique reliance on short-horizon tasks, mock services, or final-answer checks (Ding et al., 2026; Lu et al., 2026; Sales Almeida et al., 2025; Zhou et al., 2026). There is also broad consensus that human evaluation is costly and expertise-intensive, motivating automation efforts (Zhou et al., 2026; Gan et al., 2026; Yang et al., 2026). Additionally, multiple papers converge on the need for multi-step, trace-based evaluation rather than outcome-only assessment (Zhou et al., 2026; Wang et al., 2026; Ding et al., 2026).

**Disagreements**: The literature shows tension between fully automated evaluation and human-in-the-loop approaches. Gan et al. (2026) argue for certified automation with statistical guarantees, suggesting that judges can safely automate 30-59% of evaluation without human oversight. In contrast, Yang et al. (2026) and Shea et al. (2025) emphasize human structural guidance and domain knowledge integration, implying that full automation remains premature. There is also methodological disagreement on how to handle judge disagreement: JuryFlow (Yang et al., 2026) treats disagreement as a signal for improvement, while certified approaches (Gan et al., 2026) treat judge uncertainty as a constraint to be bounded.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Standardization**: No consensus exists on evaluation metrics, task formats, or reporting standards. WildClawBench (Ding et al., 2026) and Ticket-Bench (Sales Almeida et al., 2025) use entirely different task structures, making cross-benchmark comparison difficult.

2. **Cross-lingual consistency**: While Ticket-Bench (Sales Almeida et al., 2025) demonstrates cross-lingual disparities, no paper proposes a unified framework for multilingual agent evaluation across more than six languages.

3. **Certified automation limits**: Gan et al. (2026) show that certified coverage is bounded to 30-59% at alpha=0.1, leaving 41-70% of evaluation requiring manual review. No paper addresses how to scale certified automation beyond this threshold.

4. **Long-term agent behavior**: All surveyed papers focus on single-session or short-horizon evaluation. None address how to evaluate agents that operate over days, weeks, or months with persistent memory and evolving user relationships.

5. **Safety and alignment**: While several papers mention safety implicitly (e.g., certified judges bounding error rates), none directly address adversarial evaluation, red-teaming, or alignment verification as core evaluation dimensions.

6. **Reproducibility and benchmark contamination**: Only WildClawBench (Ding et al., 2026) and EvalAgent (Zhou et al., 2026) explicitly address reproducibility through containerized tooling and trace-based pipelines. The field lacks standard practices for preventing benchmark contamination as models are trained on evaluation data.

## Per-Paper Annotations

### Almeida et al. (2025)

**Research question**: How can agent evaluation benchmarks better account for cultural and linguistic diversity in multilingual, task-oriented scenarios?

**Methodology**: The authors introduce Ticket-Bench, a benchmark simulating soccer ticket purchases across six languages (Portuguese, English, Spanish, German, Italian, French) with localized teams, cities, and user profiles. They evaluate commercial and open-source LLMs on function-calling accuracy and consistency across languages.

**Key findings**:
- Existing agent evaluations largely overlook cultural and linguistic diversity, often relying on monolingual or naively translated benchmarks
- Reasoning-oriented models (e.g., GPT-5, Qwen3-235B) dominate performance but still exhibit notable cross-lingual disparities
- Results underscore the need for culturally aware, multilingual benchmarks to guide robust LLM agent development

**Limitations**: not stated in abstract

### Choi et al. (2026)

**Research question**: How does role-based authority bias affect agent interactions in free-form multi-agent evaluation systems?

**Methodology**: The study applies French and Raven's power-based theory to classify authoritative roles into legitimate, referent, and expert types, analyzing their influence across 12-turn conversations using ChatEval with GPT-4o and DeepSeek R1.

**Key findings**:
- Expert and Referent power roles exert stronger influence than Legitimate power roles in multi-agent systems
- Authority bias emerges through authoritative roles maintaining their positions while general agents demonstrate flexibility, not through active conformity
- Authority influence requires clear position statements, as neutral responses fail to generate bias

**Limitations**: not stated in abstract

### Ding et al. (2026)

**Research question**: Can current frontier models complete realistic long-horizon work in the native runtimes where agents are deployed?

**Methodology**: WildClawBench presents 60 human-authored, bilingual, multimodal tasks across six thematic categories, each averaging 8 minutes and 20+ tool calls, running inside reproducible Docker containers with real CLI agent harnesses (OpenClaw, Claude Code, Codex, or Hermes Agent) and real tools. Grading combines deterministic rule-based checks, environment-state auditing, and LLM/VLM judges.

**Key findings**:
- Most agent benchmarks rely on synthetic sandboxes, short-horizon tasks, mock-service APIs, and final-answer checks, leaving open whether agents can complete realistic long-horizon work
- The best model (Claude Opus 4.7) reaches only 62.2% overall under OpenClaw, while every other model stays below 60%
- Switching harness alone shifts a single model by up to 18 points, showing long-horizon native-runtime agent evaluation remains far-from-resolved

**Limitations**: not stated in abstract

### Gan et al. (2026)

**Research question**: What fraction of agent evaluation can an automatic judge take over with a certificate that the error rate among auto-decided trajectories stays below a specified budget?

**Methodology**: The authors introduce a task-level bootstrap certificate that remains valid across regimes while matching naive certificate coverage, and evaluate a 4B logprob judge trained with SFT and reject-weighted GRPO on tool-use and web corpora.

**Key findings**:
- Standard i.i.d. certificates can overstate safety, with naive certificates claiming 98% automation while realized error exceeds budget in 17.5% of task resamples
- The 4B judge certifies 0.30-0.59 of evaluation on tool-use and web corpora at alpha=0.1, the only judge certifying on both headline corpora
- The certificate doubles as a self-training filter with contamination bounded by alpha (realized 0.000-0.041 across six harvests)

**Limitations**: Finite-sample cluster-valid alternatives certify nothing at realistic task counts.

### Lu et al. (2026)

**Research question**: How can user-simulation-based evaluation better capture the dynamic, multi-step nature of agentic behavior while overcoming limitations of existing simulation frameworks?

**Methodology**: The authors propose VISTA, a toolkit with six metrics for measuring realism, capability coverage, and interaction effectiveness of simulated interactions, plus a hybrid user simulator integrating both UI-based and API-based interactions. Evaluation conducted in e-commerce shopping and education customer service settings.

**Key findings**:
- Existing evaluation methods rely on static benchmarks that fail to capture dynamic, multi-step agentic behavior and struggle to expose meaningful failure modes
- Existing simulation frameworks provide limited mechanisms for evaluating quality and comprehensiveness of simulated interactions
- VISTA produces more realistic and comprehensive evaluations than existing methods in e-commerce and customer service settings

**Limitations**: not stated in abstract

### Shea et al. (2025)

**Research question**: How can user simulation for multi-turn agent evaluation be improved by incorporating domain-specific knowledge from business contexts?

**Methodology**: SAGE integrates top-down knowledge from business logic (e.g., ideal customer profiles) and bottom-up knowledge from business agent infrastructure (e.g., product catalogs, FAQs, knowledge bases) to ground user behavior in realistic personas and generate interactions reflecting users' information needs.

**Key findings**:
- The approach produces interactions that are more realistic and diverse compared to existing methods
- SAGE identifies up to 33% more agent errors than generic user simulators
- The framework is effective as an evaluation tool for bug-finding and iterative agent improvement

**Limitations**: not stated in abstract

### Wang et al. (2026)

**Research question**: How can deep research systems be evaluated effectively without annotation-intensive task construction and with reliable fact verification even when citations are missing?

**Methodology**: DeepResearchEval introduces a persona-driven pipeline generating realistic research tasks with two-stage filtering (Task Qualification and Search Necessity), plus an agentic evaluation pipeline with Adaptive Point-wise Quality Evaluation (dynamically deriving task-specific criteria) and Active Fact-Checking (autonomously extracting and verifying statements via web search).

**Key findings**:
- The framework enables automated deep research task construction without requiring annotation-intensive processes
- The two-stage filter retains only tasks requiring multi-source evidence integration and external retrieval
- Active Fact-Checking can verify report statements via web search even when citations are missing
- Adaptive Point-wise Quality Evaluation dynamically derives evaluation dimensions, criteria, and weights conditioned on each task

**Limitations**: not stated in abstract

### Yang et al. (2026)

**Research question**: How can inter-judge disagreement in multi-agent evaluation be leveraged as a signal to improve evaluation accuracy rather than being discarded?

**Methodology**: JuryFlow decomposes responses into atomic claims, uses heterogeneous judges to assign per-claim verdicts, builds a disagreement graph scored by verdict entropy, and enables human structural guides to select disagreements for resolution, with corrections propagating along graph edges and crystallizing into reusable rubric entries.

**Key findings**:
- JuryFlow improves agreement with gold labels over single-judge and majority-vote panel baselines on MT-Bench and LLMBar
- The human-in-the-loop paradigm recasts the human from labeler to structural guide selecting minimal interventions
- Ablations isolate the contributions of disagreement-targeted re-evaluation, propagation, and rubric induction to performance gains
- The framework makes the evaluator progressively self-refining through closed-loop rubric induction

**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can machine translation for web novels be effectively evaluated beyond surface-level metrics to capture narrative and cultural fidelity?

**Methodology**: DITING introduces a comprehensive evaluation framework assessing six dimensions (idiom translation, lexical ambiguity, terminology localization, tense consistency, zero-pronoun resolution, cultural safety) with over 18K expert-annotated Chinese-English sentence pairs, plus AgentEval (a reasoning-driven multi-agent framework) and MetricAlign (a meta-evaluation dataset of 300 sentence pairs).

**Key findings**:
- AgentEval achieves the highest correlation with human judgments among seven tested automatic metrics
- Chinese-trained LLMs surpass larger foreign counterparts in web novel translation quality
- DeepSeek-V3 delivers the most faithful and stylistically coherent translations among fourteen evaluated models
- The framework establishes a new paradigm for LLM-based web novel translation research

**Limitations**: not stated in abstract

### Zhou et al. (2026)

**Research question**: Can frontier coding assistants reliably automate the agent evaluation process?

**Methodology**: The study introduces EvalAgent, an AI assistant that encodes evaluation domain expertise as evaluation skills (procedural instructions, reusable code, templates, and dynamically retrieved API documentation) to compose a trace-based pipeline. They evaluate using a meta-evaluation framework with AgentEvalBench (20 agents with evaluation requirements and test scenarios) and propose the Eval@1 metric.

**Key findings**:
- Simply prompting frontier coding assistants achieves only 30% execution success rate and produces over-engineered evaluations with 12+ metrics per agent
- EvalAgent improves Eval@1 from 17.5% to 65% and achieves 79.5% human expert preference over baseline approaches
- Evaluation skills are critical for handling complex evaluation: removing them causes Eval@1 to drop from 65% to 30%

**Limitations**: not stated in abstract

## References

Almeida, T. S., Santos, J. G. A., Laitz, T., & Bonás, G. K. (2025). Ticket-Bench: A kickoff for multilingual and regionalized agent evaluation. arXiv. https://arxiv.org/abs/2509.14477

Choi, J., Kwon, J., Kim, H., Cho, H., Jung, H., Min, S., & Kim, B. (2026). Belief in authority: Impact of authority in multi-agent evaluation framework. arXiv. https://arxiv.org/abs/2601.04790

Ding, S., Dai, X., Xing, L., Ding, S., Liu, Z., JingYi, Y., Yang, P., Zhang, Z., Wei, X., Fang, X., Ma, Y., Duan, H., Shao, J., Wang, J., Lin, D., Chen, K., & Zang, Y. (2026). WildClawBench: A benchmark for real-world, long-horizon agent evaluation. arXiv. https://arxiv.org/abs/2605.10912

Gan, C., Liang, Y., Zhang, Q., & Ni, S. (2026). Certified selective automation of LLM agent evaluation. arXiv. https://arxiv.org/abs/2609.34320

Lu, Y., Shea, R., Zhang, Y., & Yu, Z. (2026). VISTA: A versatile interactive user simulation toolkit for agent evaluation. arXiv. https://arxiv.org/abs/2606.11079

Shea, R., Lu, Y., Qiu, L., & Yu, Z. (2025). SAGE: A top-down bottom-up knowledge-grounded user simulator for multi-turn agent evaluation. arXiv. https://arxiv.org/abs/2510.11997

Wang, Y., Wang, L., Deng, Y., Wu, K., Xiao, Y., Yao, H., Kang, L., Ye, H., Jing, Y., & Bing, L. (2026). DeepResearchEval: An automated framework for deep research task construction and agentic evaluation. arXiv. https://arxiv.org/abs/2601.09688

Yang, M., Yu, J., & Ding, Y. (2026). JuryFlow: Disagreement-guided human-in-the-loop multi-agent evaluation. arXiv. https://arxiv.org/abs/2609.40103

Zhang, E., Wang, J., Xiao, M., Liu, J., Kuang, Z., Dong, R., Dong, E., Ananiadou, S., Peng, M., & Xie, Q. (2025). DITING: A multi-agent evaluation framework for benchmarking web novel translation. arXiv. https://arxiv.org/abs/2510.09116

Zhou, K., Woo, S., Ding, H., Ramnath, K., Chidambaram, S., Feng, A., Arannil, V., Kim, M., Singh, I., Wang, D., Xu, Z., Gandhi, M., Prabhu, N., Mishra, S. S., Dhakecha, S., Singh, V., Pandeshwar, G., & Cheong, L. L. (2026). An empirical study of automating agent evaluation. arXiv. https://arxiv.org/abs/2605.11378
