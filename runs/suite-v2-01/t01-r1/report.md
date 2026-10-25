# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "agent evaluation", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on LLM agent evaluation benchmarks published between late 2024 and late 2026. The field is rapidly evolving, with research concentrated on four key directions: automating evaluation processes, developing user simulation frameworks, designing specialized benchmarks for diverse scenarios, and leveraging multi-agent frameworks for more reliable evaluation. Collectively, these works reveal a maturing recognition that static benchmarks are insufficient for evaluating dynamic, multi-step agentic behavior, prompting a shift toward interactive, realistic, and culturally-aware evaluation methodologies. The literature demonstrates growing sophistication in addressing evaluation challenges including long-horizon task completion, multilingual and regional considerations, and the reliability of automated judges.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query `agent evaluation`, filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Automation of Evaluation Processes

A significant research direction focuses on automating the evaluation process itself, recognizing that manual evaluation is costly and inconsistent. Zhou et al. (2024) introduced EvalAgent, an AI assistant that encodes evaluation domain expertise as evaluation skills including procedural instructions, reusable code, templates, and dynamically retrieved API documentation. Their work demonstrates that simply prompting coding assistants is insufficient for agent evaluation, achieving only 30% execution success rate, while EvalAgent improves performance to 65% Eval@1 with focused evaluations.

Complementing this work, Gan et al. (2026) addressed the question of what fraction of agent evaluation can be safely automated with certified error guarantees. They introduced a task-level bootstrap certificate that remains valid across regimes, addressing the critical issue that correlated trajectory clusters can cause i.i.d. certificates to overstate safe automation. Their 4B parameter judge model, trained with SFT and reject-weighted GRPO, certifies 0.30-0.59 of evaluation on tool-use and web corpora while maintaining error rate guarantees. This work provides theoretical grounding for understanding the limits and possibilities of automated evaluation.

### Theme 2: User Simulation for Evaluation

User simulation has emerged as a powerful paradigm for overcoming the limitations of static benchmarks. Lu et al. (2026) proposed VISTA, a Versatile Interactive User Simulation Toolkit that addresses three critical gaps in existing evaluation methods: reliance on static benchmarks that fail to capture dynamic multi-step agentic behavior, limited mechanisms for evaluating quality and comprehensiveness of simulated interactions, and restriction to either UI-only or API-only actions. VISTA includes six metrics for measuring realism, capability coverage, and interaction effectiveness, plus a hybrid user simulator integrating both UI-based and API-based interactions.

Building on user simulation approaches, Shea et al. (2025) introduced SAGE, a Top-Down Bottom-Up Knowledge-Grounded User Simulator for multi-turn agent evaluation. SAGE integrates top-down knowledge from business logic (ideal customer profiles) and bottom-up knowledge from business infrastructure (product catalogs, FAQs, knowledge bases) to generate realistic user interactions. Their approach produces more realistic and diverse interactions compared to existing approaches and identifies up to 33% more agent errors than baseline methods, demonstrating the value of grounding user simulation in domain-specific knowledge.

### Theme 3: Benchmark Design and Diversity

The literature reveals growing attention to benchmark design that captures real-world complexity and diversity. Almeida et al. (2025) introduced Ticket-Bench, addressing the critical gap that existing agent evaluations largely overlook cultural and linguistic diversity. Ticket-Bench simulates soccer ticket purchases across six languages (Portuguese, English, Spanish, German, Italian, French) with localized teams, cities, and user profiles. Their evaluation of commercial and open-source LLMs reveals that reasoning-oriented models dominate performance but still exhibit notable cross-lingual disparities, demonstrating the need for culturally aware, multilingual benchmarks.

Ding et al. (2026) presented WildClawBench, a native-runtime benchmark addressing the gap that most agent benchmarks rely on synthetic sandboxes, short-horizon tasks, mock-service APIs, and final-answer checks. WildClawBench comprises 60 human-authored, bilingual, multimodal tasks spanning six thematic categories, with each task averaging approximately 8 minutes and 20+ tool calls, running in reproducible Docker containers with real CLI agent harnesses. Their striking finding that the best model (Claude Opus 4.7) reaches only 62.2% overall under OpenClaw, with all other models below 60%, reveals that long-horizon, native-runtime agent evaluation remains a far-from-resolved task for current frontier models.

Wang et al. (2026) contributed DeepResearchEval, an automated framework for deep research task construction and agentic evaluation. Their persona-driven pipeline uses two-stage filtering (Task Qualification and Search Necessity) for task construction, and an agentic evaluation pipeline with Adaptive Point-wise Quality Evaluation and Active Fact-Checking that verifies statements via web search even without citations. This approach addresses gaps in existing benchmarks regarding citation-free verification and generates realistic, complex research tasks anchored in diverse user profiles.

### Theme 4: Multi-Agent Evaluation Frameworks

Multi-agent approaches to evaluation leverage multiple judges or agents to improve reliability and reduce bias. Choi et al. (2026) applied French and Raven's power-based theory to classify authoritative roles into legitimate, referent, and expert types, analyzing their influence across multi-turn conversations using ChatEval with GPT-4o and DeepSeek R1 models. Their finding that expert and referent power roles exert stronger influence than legitimate power roles reveals important dynamics in how authority bias emerges through authoritative roles maintaining positions while general agents show flexibility.

Zhang et al. (2025) developed DITING, a multi-agent evaluation framework for benchmarking web novel translation across six dimensions: idiom translation, lexical ambiguity, terminology localization, tense consistency, zero-pronoun resolution, and cultural safety. Using 18K expert-annotated Chinese-English pairs, their AgentEval multi-agent framework achieves the highest correlation with human judgments among seven tested automatic metrics, demonstrating the effectiveness of multi-agent approaches for nuanced evaluation tasks.

Yang et al. (2026) introduced JuryFlow, which leverages inter-judge disagreement as a signal for improving evaluation reliability rather than discarding it. JuryFlow decomposes responses into atomic claims, assigns per-claim verdicts via heterogeneous judges, builds a disagreement graph scored by verdict entropy, and enables human-guided focal re-evaluation with correction propagation and rubric induction. Their framework improves agreement with gold labels over single-judge and majority-vote panel baselines on MT-Bench and LLMBar, recasting humans from labelers to structural guides selecting which disagreements to resolve.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that static benchmarks are insufficient for evaluating dynamic, multi-step agentic behavior (Lu et al., 2026; Ding et al., 2026; Wang et al., 2026). There is consensus that evaluation must account for real-world complexity, including long-horizon tasks, cultural and linguistic diversity, and interactive behavior. Multiple papers converge on the finding that automated evaluation requires domain-specific knowledge or expertise encoding to achieve reliable results (Zhou et al., 2024; Shea et al., 2025; Zhang et al., 2025).

**Disagreements**: The literature reveals tension between full automation and human-in-the-loop approaches. While Zhou et al. (2024) and Gan et al. (2026) focus on maximizing automation with certified guarantees, Yang et al. (2026) argue for leveraging disagreement to guide human intervention rather than eliminating it. Additionally, there is disagreement about the role of authority in multi-agent evaluation: Choi et al. (2026) find that authority bias can distort evaluation outcomes, while Zhang et al. (2025) and Yang et al. (2026) successfully employ structured multi-agent frameworks with differentiated roles.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, most papers do not explicitly state limitations in their abstracts, suggesting a need for more transparent discussion of methodological constraints. Second, Gan et al. (2026) note that finite-sample cluster-valid alternatives certify nothing at realistic task counts, indicating a fundamental limitation in current certification approaches. Third, while several papers address multilingual evaluation (Almeida et al., 2025; Zhang et al., 2025), comprehensive coverage of low-resource languages remains unaddressed.

The literature also reveals gaps in standardization: different papers use incompatible evaluation metrics and frameworks, making cross-paper comparison difficult. Ding et al. (2026) found that switching harness alone can shift a single model's performance by up to 18 points, highlighting the need for standardized evaluation environments. Finally, the question of how to evaluate evaluation methods themselves—meta-evaluation—receives limited attention despite its importance for establishing trust in automated evaluation systems.

## Per-Paper Annotations

### Almeida et al. (2025)

**Research question**: How can agent evaluation benchmarks better account for cultural and linguistic diversity in multilingual, task-oriented scenarios?

**Methodology**: The authors introduce Ticket-Bench, a benchmark for multilingual agent evaluation simulating soccer ticket purchases across six languages (Portuguese, English, Spanish, German, Italian, French) with localized teams, cities, and user profiles. They evaluate commercial and open-source LLMs measuring function-calling accuracy and consistency across languages.

**Key findings**:
- Existing agent evaluations largely overlook cultural and linguistic diversity, often relying on monolingual or naively translated benchmarks
- Reasoning-oriented models (e.g., GPT-5, Qwen3-235B) dominate performance but still exhibit notable cross-lingual disparities
- The benchmark demonstrates the need for culturally aware, multilingual benchmarks to guide robust LLM agent development

**Limitations**: Not stated in abstract

### Chen et al. (2026)

**Research question**: Benchmarking Large Language Model Agents in Complex Clinical Ac

**Methodology**: GPAgentBench-2K: Benchmarking large language model agents in complex clinical scenarios.

**Key findings**:
- Not stated in abstract

**Limitations**: Not stated in abstract

### Choi et al. (2026)

**Research question**: How does role-based authority bias influence agent interactions in multi-agent evaluation frameworks?

**Methodology**: The study applies French and Raven's power-based theory to classify authoritative roles into legitimate, referent, and expert types, analyzing their influence across 12-turn conversations using ChatEval with GPT-4o and DeepSeek R1 models.

**Key findings**:
- Expert and Referent power roles exert stronger influence than Legitimate power roles
- Authority bias emerges through authoritative roles maintaining positions while general agents show flexibility
- Authority influence requires clear position statements; neutral responses fail to generate bias
- General agents demonstrate flexibility rather than active conformity to authority

**Limitations**: Not stated in abstract

### Ding et al. (2026)

**Research question**: Can current frontier models complete realistic long-horizon work in native CLI runtimes where agents are deployed?

**Methodology**: The authors present WildClawBench, a native-runtime benchmark of 60 human-authored, bilingual, multimodal tasks spanning six thematic categories, with each task averaging ~8 minutes and 20+ tool calls, running in reproducible Docker containers with real CLI agent harnesses. Grading combines deterministic rule-based checks, environment-state auditing, and LLM/VLM judges.

**Key findings**:
- Most agent benchmarks rely on synthetic sandboxes, short-horizon tasks, mock-service APIs, and final-answer checks
- The best model (Claude Opus 4.7) reaches only 62.2% overall under OpenClaw, with all other models below 60%
- Switching harness alone can shift a single model's performance by up to 18 points
- Long-horizon, native-runtime agent evaluation remains a far-from-resolved task for current frontier models

**Limitations**: Not stated in abstract

### Gan et al. (2026)

**Research question**: What fraction of agent evaluation can a judge automate with a certificate guaranteeing the error rate stays below a specified budget?

**Methodology**: The authors introduce a task-level bootstrap certificate that remains valid across regimes while matching naive certificate coverage, addressing the issue that correlated trajectory clusters can cause i.i.d. certificates to overstate safe automation. They train a 4B logprob judge with SFT and reject-weighted GRPO and evaluate on tool-use and web corpora.

**Key findings**:
- Naive certificates can claim 98% automation while realized error exceeds the budget in 17.5% of task resamples
- Under the task-level bootstrap certificate at alpha=0.1, a 4B judge certifies 0.30-0.59 of evaluation on tool-use and web corpora
- Certified coverage is predictable before training from base rate and discrimination alone (leave-one-corpus-out R^2=0.96)
- The certificate serves as a self-training filter with contamination bounded by alpha (realized 0.000-0.041 across six harvests)

**Limitations**: Finite-sample cluster-valid alternatives certify nothing at realistic task counts

### Lu et al. (2026)

**Research question**: How can user-simulation-based evaluation overcome limitations of static benchmarks and existing simulation frameworks for interactive agent development?

**Methodology**: The authors propose VISTA, a toolkit including six metrics for measuring realism, capability coverage, and interaction effectiveness of simulated interactions, plus a hybrid user simulator integrating both UI-based and API-based interactions. They evaluate VISTA in e-commerce shopping and education customer service settings.

**Key findings**:
- Existing evaluation methods rely on static benchmarks that fail to capture dynamic, multi-step agentic behavior
- Existing simulation frameworks provide limited mechanisms for evaluating quality and comprehensiveness of simulated interactions
- Most frameworks are restricted to either UI-only or API-only actions, limiting realistic user behavior modeling
- VISTA produces more realistic and comprehensive evaluations than existing methods in tested settings

**Limitations**: Not stated in abstract

### Shea et al. (2025)

**Research question**: How can user simulation for multi-turn agent evaluation be improved by integrating domain-specific knowledge from business contexts?

**Methodology**: SAGE integrates top-down knowledge from business logic (ideal customer profiles) and bottom-up knowledge from business infrastructure (product catalogs, FAQs, knowledge bases) to generate realistic user interactions. The approach was empirically evaluated to measure interaction realism, diversity, and agent error detection rates.

**Key findings**:
- SAGE produces more realistic and diverse interactions compared to existing approaches
- The framework identifies up to 33% more agent errors than baseline methods
- Top-down knowledge grounds user behavior in realistic customer personas
- Bottom-up knowledge enables interactions that reflect users' information needs in target markets

**Limitations**: Not stated in abstract

### Wang et al. (2026)

**Research question**: How can deep research systems be evaluated automatically without relying on annotation-intensive task construction and static evaluation dimensions?

**Methodology**: DeepResearchEval uses a persona-driven pipeline with two-stage filtering (Task Qualification and Search Necessity) for task construction, and an agentic evaluation pipeline with Adaptive Point-wise Quality Evaluation and Active Fact-Checking that verifies statements via web search even without citations.

**Key findings**:
- The framework generates realistic, complex research tasks anchored in diverse user profiles
- Adaptive Point-wise Quality Evaluation dynamically derives task-specific criteria and weights
- Active Fact-Checking autonomously extracts and verifies report statements via web search
- The approach addresses gaps in existing benchmarks regarding citation-free verification

**Limitations**: Not stated in abstract

### Yang et al. (2026)

**Research question**: How can inter-judge disagreement in multi-agent evaluation be leveraged as a signal for improving evaluation reliability rather than discarded?

**Methodology**: JuryFlow decomposes responses into atomic claims, assigns per-claim verdicts via heterogeneous judges, builds a disagreement graph scored by verdict entropy, and enables human-guided focal re-evaluation with correction propagation and rubric induction for closed-loop refinement.

**Key findings**:
- JuryFlow improves agreement with gold labels over single-judge and majority-vote panel baselines on MT-Bench and LLMBar
- Disagreement-targeted re-evaluation, propagation, and rubric induction each contribute to performance gains
- The framework recasts humans from labelers to structural guides selecting which disagreements to resolve
- Corrections propagate along graph edges and to historically similar cases, crystallizing into reusable rubric entries

**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can machine translation of web novels be evaluated more effectively beyond surface-level metrics?

**Methodology**: DITING assesses translation quality across six dimensions (idiom translation, lexical ambiguity, terminology localization, tense consistency, zero-pronoun resolution, cultural safety) using 18K expert-annotated Chinese-English pairs, with AgentEval multi-agent framework and MetricAlign meta-evaluation dataset for comparison.

**Key findings**:
- AgentEval achieves highest correlation with human judgments among seven tested automatic metrics
- Chinese-trained LLMs surpass larger foreign counterparts in web novel translation
- DeepSeek-V3 delivers the most faithful and stylistically coherent translations
- The framework provides 300 sentence pairs with error labels and scalar quality scores for metric comparison

**Limitations**: Not stated in abstract

### Zhou et al. (2026)

**Research question**: Can frontier coding assistants reliably automate the agent evaluation process?

**Methodology**: The study introduces EvalAgent, an AI assistant that encodes evaluation domain expertise as evaluation skills (procedural instructions, reusable code, templates, and dynamically retrieved API documentation) that compose into a trace-based pipeline. They assess generated evaluations using a meta-evaluation framework with AgentEvalBench (20 agents with evaluation requirements and test scenarios) and propose the Eval@1 metric.

**Key findings**:
- Simply prompting coding assistants is insufficient for agent evaluation, achieving only 30% execution success rate
- Frontier coding assistants produce over-engineered evaluations averaging 12+ metrics per agent without domain-specific knowledge
- EvalAgent improves Eval@1 from 17.5% to 65% with focused evaluations
- EvalAgent achieves 79.5% human expert preference over baseline approaches
- Evaluation skills are critical for handling complex evaluation: removing them causes Eval@1 to drop from 65% to 30%

**Limitations**: Not stated in abstract

## References

Almeida, T. S., Santos, J. G. A., Laitz, T., & Bonás, G. K. (2025). Ticket-Bench: A kickoff for multilingual and regionalized agent evaluation. arXiv. https://arxiv.org/abs/2509.14477

Chen, B. (2026). GPAgentBench-2K: Benchmarking large language model agents in complex clinical ac. arXiv. https://arxiv.org/abs/2608.30188

Choi, J., Kwon, J., Kim, H., Cho, H., Jung, H., Min, S., & Kim, B. (2026). Belief in authority: Impact of authority in multi-agent evaluation framework. arXiv. https://arxiv.org/abs/2601.04790

Ding, S., Dai, X., Xing, L., Ding, S., Liu, Z., Yang, J., Yang, P., Zhang, Z., Wei, X., Fang, X., Ma, Y., Duan, H., Shao, J., Wang, J., Lin, D., Chen, K., & Zang, Y. (2026). WildClawBench: A benchmark for real-world, long-horizon agent evaluation. arXiv. https://arxiv.org/abs/2605.10912

Gan, C., Liang, Y., Zhang, Q., & Ni, S. (2026). Certified selective automation of LLM agent evaluation. arXiv. https://arxiv.org/abs/2609.34320

Lu, Y., Shea, R., Zhang, Y., & Yu, Z. (2026). VISTA: A versatile interactive user simulation toolkit for agent evaluation. arXiv. https://arxiv.org/abs/2606.11079

Shea, R., Lu, Y., Qiu, L., & Yu, Z. (2025). SAGE: A top-down bottom-up knowledge-grounded user simulator for multi-turn agent evaluation. arXiv. https://arxiv.org/abs/2510.11997

Wang, Y., Wang, L., Deng, Y., Wu, K., Xiao, Y., Yao, H., Kang, L., Ye, H., Jing, Y., & Bing, L. (2026). DeepResearchEval: An automated framework for deep research task construction and agentic evaluation. arXiv. https://arxiv.org/abs/2601.09688

Yang, M., Yu, J., & Ding, Y. (2026). JuryFlow: Disagreement-guided human-in-the-loop multi-agent evaluation. arXiv. https://arxiv.org/abs/2609.40103

Zhang, E., Wang, J., Xiao, M., Liu, J., Kuang, Z., Dong, R., Dong, E., Ananiadou, S., Peng, M., & Xie, Q. (2025). DITING: A multi-agent evaluation framework for benchmarking web novel translation. arXiv. https://arxiv.org/abs/2510.09116

Zhou, K., Woo, S., Ding, H., Ramnath, K., Chidambaram, S., Feng, A., Arannil, V., Kim, M., Singh, I., Wang, D., Xu, Z., Gandhi, M., Prabhu, N., Mishra, S. S., Dhakecha, S., Singh, V., Pandeshwar, G., & Cheong, L. L. (2026). An empirical study of automating agent evaluation. arXiv. https://arxiv.org/abs/2605.11378
