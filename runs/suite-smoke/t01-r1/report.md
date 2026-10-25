# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "agent evaluation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature reveals a rapidly maturing field focused on addressing fundamental challenges in LLM agent evaluation. Collectively, these papers demonstrate that traditional static benchmarks are inadequate for evaluating complex, multi-step agent behaviors, leading to the development of sophisticated evaluation frameworks that emphasize realism, multilingual coverage, and certified automation. The field is shifting from simple task completion metrics toward comprehensive infrastructure that captures dynamic interactions, long-horizon performance, and real-world deployment scenarios. Key trends include the emergence of hybrid evaluation approaches combining automated judges with human oversight, the recognition of cultural and linguistic diversity gaps, and the development of specialized benchmarks for domain-specific applications such as web navigation, software engineering, and translation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "agent evaluation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Automation of Agent Evaluation

A significant body of work focuses on automating the agent evaluation process itself, recognizing that manual evaluation is costly and expertise-intensive. Zhou et al. (2026) demonstrated that simply prompting frontier coding assistants achieves only 30% execution success rate and produces over-engineered evaluations, leading them to develop EvalAgent which encodes domain expertise as evaluation skills and improves first-run success from 17.5% to 65%. Similarly, Gan et al. (2026) addressed the fundamental challenge that automatic judges lack guarantees on error rates, introducing a task-level bootstrap certificate that can safely automate 30-59% of evaluation with bounded error. This theme reflects the field's recognition that scalable agent development requires scalable evaluation, but that automation must be carefully designed with domain-specific knowledge rather than relying on general-purpose coding capabilities.

### Theme 2: Realistic and Long-Horizon Evaluation

Multiple papers emphasize the inadequacy of synthetic, short-horizon benchmarks for evaluating agents deployed in real-world settings. Ding et al. (2026) introduced WildClawBench, a native-runtime benchmark with 60 human-authored tasks averaging 8 minutes and 20+ tool calls, revealing that even the best model (Claude Opus 4.7) achieves only 62.2% success. Li et al. (2026) extended this focus to software development with LoopsBench, which evaluates sustained execution through dependency DAGs across 112 tasks, finding that the strongest configuration resolves only 25% of tasks. These findings collectively demonstrate that current frontier models struggle significantly with long-horizon, realistic tasks, suggesting that benchmark design must prioritize ecological validity over task simplicity.

### Theme 3: Infrastructure and Standardization

The field is developing comprehensive infrastructure to standardize agent evaluation practices. Kapoor et al. (2025) introduced the Holistic Agent Leaderboard (HAL), which orchestrates parallel evaluations across hundreds of VMs, reducing evaluation time from weeks to hours while conducting 21,730 agent rollouts at a cost of approximately $40,000. Their three-dimensional analysis spanning models, scaffolds, and benchmarks revealed counterintuitive findings such as higher reasoning effort reducing accuracy in most runs. This infrastructure-focused work aims to shift the field from agents that excel on benchmarks to agents that work reliably in practice, addressing common implementation bugs and enabling large-scale comparative studies.

### Theme 4: User Simulation for Interactive Evaluation

For interactive agents, user simulation has emerged as a critical evaluation paradigm. Lu et al. (2026) developed VISTA, a toolkit with six metrics for measuring simulation quality and a hybrid simulator integrating UI and API interactions, demonstrating more realistic evaluations in e-commerce and customer service settings. Shea et al. (2025) introduced SAGE, which incorporates both top-down business logic knowledge and bottom-up infrastructure knowledge to simulate realistic customer personas, identifying up to 33% more agent errors than generic simulators. These approaches address the limitations of static benchmarks by capturing the dynamic, multi-turn nature of agent-user interactions.

### Theme 5: Multilingual and Cultural Considerations

The literature increasingly recognizes that agent evaluation must account for linguistic and cultural diversity. Almeida et al. (2025) introduced Ticket-Bench for multilingual agent evaluation across six languages (Portuguese, English, Spanish, German, Italian, French), revealing that even reasoning-oriented models like GPT-5 exhibit notable cross-lingual disparities despite dominating overall performance. This work highlights the inadequacy of monolingual or naively translated benchmarks and underscores the need for culturally aware evaluation frameworks that reflect the global deployment contexts of LLM agents.

### Theme 6: Domain-Specific Evaluation Frameworks

Several papers develop evaluation frameworks tailored to specific application domains. Zhang et al. (2025) created DITING for web novel translation, assessing six dimensions including idiom translation, cultural safety, and zero-pronoun resolution across 18K expert-annotated sentence pairs, finding that Chinese-trained LLMs outperform larger foreign models. Choi et al. (2026) examined authority bias in multi-agent evaluation frameworks, applying French and Raven's power-based theory to analyze how Expert and Referent power roles exert stronger influence than Legitimate roles. These domain-specific approaches recognize that evaluation criteria must align with the unique requirements and failure modes of particular application areas.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that static, synthetic benchmarks are inadequate for evaluating modern LLM agents. Multiple studies demonstrate that realistic, long-horizon evaluation reveals significant performance gaps not captured by simpler benchmarks (Ding et al., 2026; Li et al., 2026; Kapoor et al., 2025). There is also strong consensus that automation of evaluation requires domain-specific knowledge rather than general-purpose capabilities (Zhou et al., 2026; Gan et al., 2026). The literature uniformly emphasizes the need for more comprehensive infrastructure to support scalable, reproducible evaluation.

**Disagreements**: The papers differ in their approaches to balancing automation with reliability. Zhou et al. (2026) advocate for encoding domain expertise as explicit evaluation skills, while Gan et al. (2026) focus on statistical certificates that bound error rates without requiring explicit domain knowledge encoding. Additionally, there is tension between the push for standardized infrastructure (Kapoor et al., 2025) and the development of specialized, domain-specific frameworks (Zhang et al., 2025; Choi et al., 2026), reflecting unresolved questions about whether the field should prioritize general-purpose or specialized evaluation tools.

## Gaps and Open Questions

Several critical gaps emerge from the collective limitations identified in the surveyed literature. First, generalizability remains a persistent concern: most benchmarks are evaluated in limited domains (e-commerce, customer service, soccer tickets) with unclear applicability to other contexts (Lu et al., 2026; Almeida et al., 2025; Zhou et al., 2026). Second, the computational and financial cost of comprehensive evaluation is substantial—Kapoor et al. (2025) report approximately $40,000 for their study, raising questions about accessibility for smaller research groups. Third, certified automation approaches currently cover only 30-59% of evaluation tasks (Gan et al., 2026), leaving the majority of evaluation still requiring human judgment. Fourth, while multilingual benchmarks address an important gap, coverage is limited to six major languages, excluding many global languages (Almeida et al., 2025). Finally, the field lacks consensus on evaluation metrics, with different papers proposing Eval@1, function-calling accuracy, certification coverage, and other measures, complicating cross-study comparisons.

## Per-Paper Annotations

### Almeida et al. (2025)

**Research question**: How can we evaluate LLM agents under realistic, multilingual conditions that account for cultural and linguistic diversity?

**Methodology**: The authors introduced Ticket-Bench, a benchmark simulating soccer ticket purchases across six major languages using localized teams, cities, and user profiles, evaluating commercial and open-source LLMs on function-calling accuracy and consistency.

**Key findings**:
- Existing agent evaluations largely overlook cultural and linguistic diversity, often relying on monolingual or naively translated benchmarks
- Reasoning-oriented models (e.g., GPT-5, Qwen3-235B) dominate performance on the benchmark
- Even top-performing models exhibit notable cross-lingual disparities in function-calling accuracy
- Localized content provides higher realism compared to translated benchmarks
- Results underscore the need for culturally aware, multilingual benchmarks

**Limitations**: The benchmark is limited to the soccer ticket purchase domain and six languages, which may not represent the full spectrum of multilingual and regionalized agent evaluation scenarios.

### Choi et al. (2026)

**Research question**: How does role-based authority bias impact agent interactions in multi-agent evaluation frameworks?

**Methodology**: The authors conducted the first systematic analysis of authority bias in free-form multi-agent evaluation using ChatEval, applying French and Raven's power-based theory to classify authoritative roles into legitimate, referent, and expert types across 12-turn conversations with GPT-4o and DeepSeek R1.

**Key findings**:
- Expert and Referent power roles exert stronger influence than Legitimate power roles
- Authority bias emerges not through active conformity by general agents, but through authoritative roles consistently maintaining positions while general agents demonstrate flexibility
- Authority influence requires clear position statements, as neutral responses fail to generate bias
- This is the first systematic analysis of role-based authority bias in multi-agent evaluation
- Findings provide key insights for designing multi-agent frameworks with asymmetric interaction patterns

**Limitations**: The study focuses on specific models (GPT-4o, DeepSeek R1) and the ChatEval framework, limiting generalizability to other multi-agent systems and model architectures.

### Ding et al. (2026)

**Research question**: Can current LLM agents complete realistic long-horizon work in the native runtimes where they are deployed?

**Methodology**: The authors created WildClawBench, a native-runtime benchmark of 60 human-authored, bilingual, multimodal tasks averaging 8 minutes and 20+ tool calls, running in reproducible Docker containers with real CLI agent harnesses and hybrid grading combining rule-based checks, environment-state auditing, and LLM/VLM judges.

**Key findings**:
- The best model (Claude Opus 4.7) reaches only 62.2% overall under OpenClaw, while every other model stays below 60%
- Switching harness alone shifts a single model's performance by up to 18 points
- Long-horizon, native-runtime agent evaluation remains a far-from-resolved task for current frontier models
- Most existing benchmarks rely on synthetic sandboxes, short-horizon tasks, and mock services, leaving open questions about real-world performance
- Hybrid grading combining deterministic checks and semantic verification provides more comprehensive evaluation

**Limitations**: The benchmark focuses on CLI-based agents and may not generalize to other interaction modalities; the 60 tasks, while human-authored, may not cover all real-world deployment scenarios.

### Gan et al. (2026)

**Research question**: What fraction of agent evaluation can a judge automate with a certificate guaranteeing the error rate among auto-decided trajectories stays below a specified budget?

**Methodology**: The authors introduced a task-level bootstrap certificate valid under correlated trajectory clusters and trained a 4B logprob judge using SFT and reject-weighted GRPO, testing on tool-use and web corpora to measure certified coverage at various error budgets.

**Key findings**:
- Naive i.i.d. certificates can overstate safety—claiming 98% automation while realized error exceeds budget in 17.5% of task resamples
- A 4B logprob judge certifies 0.30-0.59 of evaluation on tool-use and web corpora at alpha=0.1
- Certified coverage is predictable before training from base rate and discrimination alone (leave-one-corpus-out R²=0.96)
- The certificate doubles as a self-training filter with pseudo-label contamination bounded by alpha (realized 0.000-0.041)
- This enables judges to enter unseen domains at in-domain strength with zero target training labels

**Limitations**: Certified automation coverage remains limited to 30-59% even with the best judge, and the approach requires training a specialized judge model rather than working with off-the-shelf frontier models.

### Kapoor et al. (2025)

**Research question**: How can we address the many challenges undermining our understanding of how well AI agents really work?

**Methodology**: The authors introduced the Holistic Agent Leaderboard (HAL) with a standardized evaluation harness orchestrating parallel evaluations across hundreds of VMs, conducting 21,730 agent rollouts across 9 models and 9 benchmarks with LLM-aided log inspection.

**Key findings**:
- Standardized evaluation harness reduces evaluation time from weeks to hours while eliminating common implementation bugs
- Three-dimensional analysis reveals surprising insights, such as higher reasoning effort reducing accuracy in the majority of runs
- LLM-aided log inspection uncovered previously unreported behaviors, including agents searching for benchmarks on HuggingFace instead of solving tasks
- The project shared all agent logs comprising 2.5B tokens of language model calls
- The work aims to shift focus from agents that ace benchmarks to agents that work reliably in the real world

**Limitations**: The evaluation infrastructure required substantial cost (~$40,000 for the study), and while covering 9 models and 9 benchmarks, it may not encompass all agent types, scaffolds, and real-world task domains.

### Li et al. (2026)

**Research question**: How can we evaluate coding agents on sustained long-horizon software development rather than localized tasks or end-state outcomes?

**Methodology**: The authors introduced LoopsBench, a long-horizon benchmark where each task is a dependency DAG over separately testable development units, comprising 112 tasks from authentic sources across 8 programming languages with flow-aware runtime releasing tests along the ready frontier.

**Key findings**:
- The strongest configuration (Opus-4.7 with Claude Code and outer continuation) resolves only 25.00% of tasks
- Recorded plans recover only part of the source-recovered prerequisite DAG
- Regression events remain visible across evaluated loop profiles
- Coding agent infrastructure is shifting from harness engineering toward loop engineering
- The benchmark includes more than 5,300 development units and executable tests

**Limitations**: The benchmark focuses specifically on coding agents and software development tasks, with unclear applicability to other agent domains; the 25% success rate suggests the tasks may be extremely challenging even for frontier models.

### Lu et al. (2026)

**Research question**: How can we evaluate interactive agents beyond static benchmarks to capture dynamic, multi-step behavior and expose meaningful failure modes?

**Methodology**: The authors developed VISTA, a toolkit with six metrics for measuring realism, capability coverage, and interaction effectiveness, and created a hybrid user simulator integrating both UI-based and API-based interactions, evaluated in e-commerce and education customer service settings.

**Key findings**:
- Existing evaluation methods relying on static benchmarks fail to capture dynamic, multi-step agentic behavior
- Existing simulation frameworks provide limited mechanisms for evaluating quality and comprehensiveness of simulated interactions
- Most frameworks are restricted to either UI-only or API-only actions, limiting realistic user behavior modeling
- VISTA's hybrid simulator enables more realistic and comprehensive evaluation across diverse interactive environments
- VISTA produces more realistic and comprehensive evaluations than existing methods in evaluated settings

**Limitations**: The toolkit was evaluated only in e-commerce shopping and education customer service settings; generalizability to other interactive domains and the computational cost of running comprehensive simulations are not addressed.

### Shea et al. (2025)

**Research question**: How can we improve user simulation for multi-turn interactive agent evaluation by incorporating domain-specific knowledge?

**Methodology**: The authors proposed SAGE, a user simulation framework integrating top-down knowledge from business logic (ideal customer profiles) and bottom-up knowledge from business infrastructure (product catalogs, FAQs, knowledge bases) to generate realistic customer personas and interactions.

**Key findings**:
- This approach produces interactions that are more realistic and diverse than generic user simulators
- SAGE identifies up to 33% more agent errors, highlighting its effectiveness as an evaluation tool
- Existing approaches typically model generic users and overlook domain-specific principles required for realistic behavior
- The framework supports bug-finding and iterative agent improvement
- Knowledge-grounded simulation better captures users' information needs and expectations in target markets

**Limitations**: The framework requires access to business-specific knowledge infrastructure, which may not be available for all evaluation scenarios; the approach was validated in specific business contexts with unclear generalizability.

### Zhang et al. (2025)

**Research question**: How can we evaluate LLM-based web novel translation beyond surface-level metrics to capture narrative and cultural fidelity?

**Methodology**: The authors introduced DITING, assessing six dimensions (idiom translation, lexical ambiguity, terminology localization, tense consistency, zero-pronoun resolution, cultural safety) across 18K expert-annotated Chinese-English sentence pairs, and proposed AgentEval, a multi-agent evaluation framework simulating expert deliberation.

**Key findings**:
- Chinese-trained LLMs surpass larger foreign counterparts in web novel translation
- DeepSeek-V3 delivers the most faithful and stylistically coherent translations
- AgentEval achieves the highest correlation with human judgments among seven tested automatic metrics
- Existing benchmarks relying on surface-level metrics fail to capture distinctive traits of web novel genre
- The work establishes a new paradigm for exploring LLM-based web novel translation

**Limitations**: The framework focuses specifically on Chinese-English web novel translation, limiting applicability to other language pairs and translation domains; the 300 sentence pairs in MetricAlign may be insufficient for comprehensive metric comparison.

### Zhou et al. (2026)

**Research question**: Can frontier coding assistants reliably automate the agent evaluation process?

**Methodology**: The authors studied coding assistants' performance on agent evaluation tasks and introduced EvalAgent, an AI assistant encoding evaluation domain expertise as evaluation skills (procedural instructions, reusable code, templates, dynamically retrieved API documentation), creating a meta-evaluation framework and AgentEvalBench with 20 agents.

**Key findings**:
- Frontier coding assistants achieve only 30% execution success rate without domain-specific evaluation knowledge
- Coding assistants produce over-engineered evaluations averaging 12+ metrics per agent
- EvalAgent improves Eval@1 metric from 17.5% to 65%, producing focused evaluations
- EvalAgent achieves 79.5% human expert preference over baseline approaches
- Evaluation skills are critical—removing them causes Eval@1 to drop from 65% to 30%

**Limitations**: The study focuses specifically on coding assistants and their custom benchmark; generalizability to other evaluation domains and agent types beyond the 20 agents in AgentEvalBench remains untested.

## References

Almeida, T. S., Santos, J. G. A., Laitz, T., & Bonás, G. K. (2025). Ticket-Bench: A kickoff for multilingual and regionalized agent evaluation. arXiv. https://arxiv.org/abs/2509.14477

Choi, J., Kwon, J., Kim, H., Cho, H., Jung, H., Min, S., & Kim, B. (2026). Belief in authority: Impact of authority in multi-agent evaluation framework. arXiv. https://arxiv.org/abs/2601.04790

Ding, S., Dai, X., Xing, L., Ding, S., Liu, Z., JingYi, Y., Yang, P., Zhang, Z., Wei, X., Fang, X., Ma, Y., Duan, H., Shao, J., Wang, J., Lin, D., Chen, K., & Zang, Y. (2026). WildClawBench: A benchmark for real-world, long-horizon agent evaluation. arXiv. https://arxiv.org/abs/2605.10912

Gan, C., Liang, Y., Zhang, Q., & Ni, S. (2026). Certified selective automation of LLM agent evaluation. arXiv. https://arxiv.org/abs/2609.34320

Kapoor, S., Stroebl, B., Kirgis, P., Nadgir, N., Siegel, Z. S., Wei, B., Xue, T., Chen, Z., Chen, F., Utpala, S., Ndzomga, F., Oruganty, D., Luskin, S., Liu, K., Yu, B., Arora, A., Hahm, D., Trivedi, H., Sun, H., Lee, J., Jin, T., Mai, Y., Zhou, Y., Zhu, Y., Bommasani, R., Kang, D., Song, D., Henderson, P., Su, Y., Liang, P., & Narayanan, A. (2025). Holistic Agent Leaderboard: The missing infrastructure for AI agent evaluation. arXiv. https://arxiv.org/abs/2510.11977

Li, H., Fang, Z., Feng, R., Zhao, Y., Liu, J., Gao, P., Ye, H., Lin, D., Lin, Q., Rajmohan, S., & Zhang, D. (2026). LoopsBench: From harness engineering to loop engineering in coding agent evaluation. arXiv. https://arxiv.org/abs/2608.00267

Lu, Y., Shea, R., Zhang, Y., & Yu, Z. (2026). VISTA: A versatile interactive user simulation toolkit for agent evaluation. arXiv. https://arxiv.org/abs/2606.11079

Shea, R., Lu, Y., Qiu, L., & Yu, Z. (2025). SAGE: A top-down bottom-up knowledge-grounded user simulator for multi-turn agent evaluation. arXiv. https://arxiv.org/abs/2510.11997

Zhang, E., Wang, J., Xiao, M., Liu, J., Kuang, Z., Dong, R., Dong, E., Ananiadou, S., Peng, M., & Xie, Q. (2025). DITING: A multi-agent evaluation framework for benchmarking web novel translation. arXiv. https://arxiv.org/abs/2510.09116

Zhou, K., Woo, S., Ding, H., Ramnath, K., Chidambaram, S., Feng, A., Arannil, V., Kim, M., Singh, I., Wang, D., Xu, Z., Gandhi, M., Prabhu, N., Mishra, S. S., Dhakecha, S., Singh, V., Pandeshwar, G., & Cheong, L. L. (2026). An empirical study of automating agent evaluation. arXiv. https://arxiv.org/abs/2605.11378
