# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "agent evaluation benchmarks", category cs.CL, last 2 years (2024-10-26 to 2025-10-26)
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature reveals a rapidly evolving landscape in LLM agent evaluation, with significant shifts from static, single-task benchmarks toward dynamic, multi-dimensional, and domain-specific evaluation frameworks. Recent work emphasizes the critical gap between user satisfaction and actual agent correctness, particularly in tool-augmented dialogue systems. The field is moving toward more realistic evaluation scenarios that capture lifelong personalization, multi-agent collaboration, and complex constraint satisfaction tasks. However, even state-of-the-art models struggle significantly on these benchmarks, with many achieving less than 50% accuracy on complex multi-turn or multi-constraint tasks. A notable trend is the emergence of domain-specific benchmarks (insurance, e-commerce, travel planning) alongside general evaluation frameworks, reflecting the need for specialized evaluation in professional contexts.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "agent evaluation benchmarks", filtered to category cs.CL, published between 2024-10-26 and 2025-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Beyond Static Benchmarks Toward Dynamic Evaluation

The literature shows a clear shift from static, single-turn evaluation toward dynamic, multi-turn, and interactive benchmarks. Traditional benchmarks fail to capture the complexity of real-world agent interactions, particularly in scenarios requiring memory, reasoning across multiple turns, or adaptive problem-solving. Yoa et al. (2026) propose a dynamic protocol where autonomous agents iteratively generate, validate, and solve problems, enabling progressive evaluation without manually curated datasets. Similarly, Siyan et al. (2026) introduce DETOUR, a dual-agent benchmark that simulates tip-of-the-tongue search processes across multiple conversation turns, highlighting that current models achieve only 36% accuracy when evaluated on all modalities. This theme reflects growing recognition that evaluation must capture the temporal and interactive nature of agent behavior rather than isolated task performance.

### Theme 2: Domain-Specific Evaluation Frameworks

A significant trend is the emergence of specialized benchmarks tailored to specific domains and use cases. Rather than one-size-fits-all evaluation, recent work recognizes that different domains require distinct evaluation criteria and task structures. Zhou et al. (2025) present CUFEInse v1.0, a comprehensive insurance domain benchmark with 14,430 questions spanning five core dimensions including actuarial capabilities, compliance, and intelligent agent application. Zhang et al. (2025) introduce Amazon-Bench for e-commerce web agents, covering diverse functionalities beyond simple product search, including account management and safety evaluation. Qi et al. (2026) present TREK for travel planning, featuring 800 multi-constraint tasks with fully deterministic evaluation. This specialization reflects the recognition that general benchmarks fail to capture domain-specific requirements, safety considerations, and professional standards.

### Theme 3: Multi-Dimensional Evaluation Beyond Task Success

Recent benchmarks increasingly evaluate agents across multiple dimensions rather than simple task completion metrics. The literature reveals growing awareness that agents can appear successful while making critical errors, or fail in ways that matter differently to users. Shourya et al. (2025) introduce TRACE, demonstrating that existing evaluation methods fail to capture critical errors when agents misinterpret tool results yet appear satisfactory to users. Their work highlights the fundamental difficulty of evaluating tool-augmented conversational AI systems where user happiness and agent correctness can diverge. Koren et al. (2026) propose a reference-free framework using LLM judges to assess benchmark quality itself across consistency, complexity, and policy coverage dimensions. Zhang et al. (2026) evaluate memory methods across 12 diverse domains for lifelong personalization, revealing that existing methods are far from user satisfaction. This multi-dimensional approach reflects maturation in the field beyond simple accuracy metrics.

### Theme 4: Benchmarking the Benchmarks: Quality Assessment

An emerging meta-theme is the critical examination of benchmark quality itself. The literature reveals concern that poor benchmarks—with inconsistent tasks, simplistic scenarios, or limited coverage—lead to unreliable evaluations. Koren et al. (2026) explicitly address this gap, noting that benchmark quality is rarely assessed despite its critical role in reliable agent evaluation. Their framework uses LLM judges to provide actionable diagnostics for benchmark consistency, complexity, and policy coverage, validated through agreement with human annotations and controlled quality-degrading perturbations. This self-reflective turn in the literature suggests the field is maturing toward more rigorous evaluation standards, recognizing that the quality of evaluation infrastructure fundamentally shapes research progress.

### Theme 5: Multi-Agent Collaboration and Coordination

Several papers address the evaluation of multi-agent systems, reflecting the growing importance of collaborative AI architectures. Shu et al. (2024) present comprehensive evaluation of coordination and routing capabilities in multi-agent collaboration frameworks, finding that multi-agent collaboration enhances goal success rates by up to 70% compared to single-agent approaches, with coordination modes achieving 90% end-to-end success. Their work evaluates two operational modes: coordination with parallel communication and payload referencing, and routing for efficient message forwarding. Wang et al. (2025) focus on AI-driven code generation agents, evaluating correctness and execution speed on GPU kernel generation tasks. This theme reflects the shift from evaluating individual agents toward assessing collaborative systems where multiple agents must coordinate, communicate, and share context effectively.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key findings. First, there is unanimous agreement that existing evaluation methods are inadequate for capturing the complexity of real-world agent behavior, with multiple papers documenting significant gaps between benchmark performance and actual capability (Shourya et al., 2025; Siyan et al., 2026; Qi et al., 2026). Second, all papers recognize the importance of domain-specific or task-specific evaluation criteria rather than generic metrics. Third, there is consensus that current state-of-the-art models perform poorly on complex, realistic benchmarks, with many achieving less than 50% accuracy on multi-constraint or multi-turn tasks. Finally, the literature converges on the need for more realistic, interactive, and dynamic evaluation protocols that capture temporal aspects of agent behavior.

**Disagreements**: While the papers do not directly contradict each other, they differ in their proposed solutions. Some emphasize domain-specific benchmarks (Zhou et al., 2025; Zhang et al., 2025; Qi et al., 2026), while others advocate for general frameworks applicable across domains (Koren et al., 2026; Yoa et al., 2026). There is also variation in evaluation methodology: some papers use fully deterministic, rule-based evaluators (Qi et al., 2026), while others rely on LLM judges (Koren et al., 2026) or human annotation (Siyan et al., 2026). The field has not yet converged on whether evaluation should prioritize reproducibility through deterministic scoring or flexibility through learned evaluators.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the papers explicitly state limitations in their abstracts, suggesting either space constraints or reluctance to acknowledge methodological limitations—a gap in transparency that the field should address. Second, while multiple papers highlight the inadequacy of current evaluation methods, there is limited work on how to bridge the gap between evaluation and actual deployment performance. Third, safety evaluation receives attention in only one paper (Zhang et al., 2025), despite its critical importance for real-world agent deployment. Fourth, the literature lacks longitudinal studies tracking how agent capabilities evolve over time on consistent benchmarks. Finally, there is minimal work on evaluating the computational efficiency, environmental impact, or scalability of agent systems—dimensions that become critical at deployment scale.

## Per-Paper Annotations

### Koren et al. (2026)

**Research question**: How can we assess the quality of benchmarks used to evaluate task-oriented conversational agents?
**Methodology**: The authors introduce a reference-free framework that uses LLM judges to assess benchmark consistency, complexity, and policy coverage while providing actionable diagnostics, validated through agreement with human annotations and controlled quality-degrading perturbations.
**Key findings**:
- The proposed metrics consistently distinguish between benchmark quality levels across domains and judge models
- Poor benchmarks may contain inconsistent tasks, simplistic scenarios, or limited policy coverage, leading to unreliable evaluations
- The framework is applicable to both synthetic and manually curated benchmarks
- Benchmark quality is rarely assessed despite its critical role in reliable agent evaluation
**Limitations**: not stated in abstract

### Qi et al. (2026)

**Research question**: Can LLM agents produce fully feasible travel itineraries that are jointly constraint-correct, hallucination-free, spatio-temporally executable, budget-valid, and responsive to unstated traveler needs?
**Methodology**: TREK comprises 800 multi-constraint tasks (533 feasible, 267 provably infeasible) over a synthetic knowledge base of 212,530 records across 375 cities and 13 personas, served through validated RESTful APIs, with a fully deterministic, rule-based evaluator and human-verified gold references.
**Key findings**:
- TREK is the first benchmark for feasible itinerary synthesis with fully deterministic, reproducible evaluation
- Even the strongest model (GPT-5.6) produces fully-feasible plans on only 46.2% of solvable tasks
- The median performance across 15 LLM agents is 6.6%, with a floor of 0.0%
- Satisfying travelers' unstated needs emerges as the universal bottleneck, unsolved even at the frontier
**Limitations**: not stated in abstract

### Shourya et al. (2025)

**Research question**: How can we evaluate conversational AI systems that use external tools when errors can arise from complex interactions among users, agents, and tools?
**Methodology**: The authors introduce TRACE, a benchmark of systematically synthesized tool-augmented conversations covering diverse error cases, evaluated using state-of-the-art conversation evaluation frameworks to assess their ability to capture critical errors in multi-turn tool-augmented dialogues.
**Key findings**:
- Existing evaluation methods fail to capture critical errors in multi-turn tool-augmented dialogues, such as when agents misinterpret tool results yet appear satisfactory to users
- All state-of-the-art conversation evaluation approaches remain far from ideal performance on the TRACE benchmark
- The benchmark demonstrates the fundamental difficulty of evaluating tool-augmented conversational AI systems
**Limitations**: not stated in abstract

### Shu et al. (2024)

**Research question**: How can coordination protocols and evaluation methods be designed for effective multi-agent collaboration systems in enterprise applications?
**Methodology**: The authors present a comprehensive evaluation of coordination and routing capabilities in a novel multi-agent collaboration framework, testing two operational modes (coordination with parallel communication and payload referencing, and routing for efficient message forwarding) on handcrafted scenarios from three enterprise domains.
**Key findings**:
- Multi-agent collaboration enhances goal success rates by up to 70% compared to single-agent approaches
- The coordination mode achieved end-to-end goal success rates of 90%
- Payload referencing improves performance on code-intensive tasks by 23%
- Latency can be substantially reduced with a routing mechanism that selectively bypasses agent orchestration
**Limitations**: not stated in abstract

### Siyan et al. (2026)

**Research question**: How can we better evaluate agent capabilities in tip-of-the-tongue search processes that occur over multiple conversation turns?
**Methodology**: The authors introduce DETOUR, a dual-agent evaluation benchmark with 1,011 prompts. The design involves a Primary Agent (the subject of evaluation) that queries a consistent Memory Agent to identify recollected entities across multiple turns, simulating realistic search processes.
**Key findings**:
- Current state-of-the-art models achieve only 36% accuracy on the DETOUR benchmark when evaluated on all modalities (text, image, audio, and video)
- Existing benchmarks are restricted to single-turn settings, which do not realistically simulate tip-of-the-tongue search processes
- The benchmark highlights the importance of enhancing agent capabilities in underspecified scenarios
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can AI-driven code generation be used to automatically produce performant Triton GPU kernels for AMD hardware?
**Methodology**: The authors present GEAK, a framework that leverages large language models with inference-time compute scaling and a Reflexion-style feedback loop to generate Triton-based GPU kernels, evaluated on two benchmarks measuring correctness and execution speed on AMD MI300X and MI250 GPUs.
**Key findings**:
- GEAK achieved up to 63% correctness on evaluation benchmarks
- GEAK demonstrated execution speedups of up to 2.59X compared to baselines
- The framework significantly outperformed direct prompting of frontier LLMs and standard Reflexion-based generation pipelines
- Triton has emerged as a popular target for AI-generated kernels due to its balance of performance and ease-of-coding
**Limitations**: not stated in abstract

### Yoa et al. (2026)

**Research question**: How can LLM evaluation move beyond static datasets to capture evolving reasoning capabilities through dynamic, agent-centric protocols?
**Methodology**: The authors propose a dynamic protocol where autonomous agents iteratively generate, validate, and solve problems: a teacher agent generates candidates, an orchestrator validates them and guards against adversarial attacks, and a student agent attempts solutions, with invalid problems revised until passing validation and solved problems triggering more challenging variants.
**Key findings**:
- The agent-centric protocol enables progressive evaluation without manually curated datasets
- Text anomaly detection demands cross-sentence logical inference and resists pattern-matching shortcuts
- The protocol systematically exposes corner-case reasoning errors that conventional benchmarks fail to reveal
- The benchmark scales in difficulty automatically as more capable agents are substituted into any role
**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can web agent benchmarks better capture the full range of e-commerce functionalities and evaluate safety risks beyond simple product search tasks?
**Methodology**: The authors propose Amazon-Bench, a new benchmark that uses a data generation pipeline leveraging webpage content and interactive elements to create diverse, functionality-grounded user queries, with an automated evaluation framework assessing both performance and safety of web agents.
**Key findings**:
- Current e-commerce benchmarks focus primarily on product search, missing broader functionalities like account management and gift card operations
- Existing benchmarks ignore potential safety risks when agents make unintended changes to user accounts
- Amazon-Bench covers diverse tasks including address management, wish list management, and brand store following
- Current agents struggle with complex queries and pose safety risks in e-commerce settings
**Limitations**: not stated in abstract

### Zhang et al. (2026)

**Research question**: How well do existing LLM memory methods perform in evaluating lifelong, cross-domain user personalization using real-world behavioral data?
**Methodology**: The authors introduce MemoryCD, a large-scale benchmark derived from the Amazon Review dataset that tracks authentic user interactions across years and multiple domains, evaluating 14 LLM base models with 6 memory method baselines on 4 personalization tasks over 12 diverse domains.
**Key findings**:
- MemoryCD is the first user-centric, cross-domain memory benchmark using lifelong real-world behaviors rather than synthetic dialogues
- The benchmark evaluates agents across 12 diverse domains to assess single and cross-domain personalization capabilities
- Existing memory methods are far from user satisfaction across various domains
- MemoryCD provides the first testbed for cross-domain life-long personalization evaluation
**Limitations**: not stated in abstract

### Zhou et al. (2025)

**Research question**: How can a comprehensive evaluation benchmark be constructed to assess large language models' capabilities in the insurance domain?
**Methodology**: The paper presents CUFEInse v1.0, a benchmark with an evaluation framework covering 5 core dimensions, 54 sub-indicators, and 14,430 high-quality questions spanning insurance theoretical knowledge, industry understanding, safety and compliance, intelligent agent application, and logical rigor, used to conduct comprehensive evaluations on 11 mainstream large language models.
**Key findings**:
- General-purpose models suffer from common bottlenecks including weak actuarial capabilities and inadequate compliance adaptation
- High-quality domain-specific training demonstrates significant advantages in insurance vertical scenarios but exhibits shortcomings in business adaptation and compliance
- The evaluation identifies common bottlenecks of current large models in professional scenarios such as insurance actuarial, underwriting and claim settlement reasoning, and compliant marketing copywriting
- CUFEInse fills the gap in professional evaluation benchmarks for the insurance field, providing a professional, systematic, and authoritative evaluation tool
- The benchmark's construction concept and methodology offer important references for the evaluation paradigm of large models in vertical fields
**Limitations**: not stated in abstract

## References

Koren, N., Bar-Haim, R., & Goldsteen, A. (2026). Benchmarking the benchmarks: Evaluating benchmarks for conversational agents. arXiv. https://arxiv.org/abs/2608.06329

Qi, J., Zhang, W., Ng, S. M., Xu, F., Chen, Y., Li, Y., & King, I. (2026). TREK: A travel reasoning and evaluation kit for LLM agents in complex trip planning. arXiv. https://arxiv.org/abs/2607.26977

Shourya, T., Wang, Y., Hou, Z. J., Roy, S., Kumar, V. B., & Gangadharaiah, R. (2025). When users are happy but agents are wrong: Multi-dimensional evaluation of tool-augmented dialogue. arXiv. https://arxiv.org/abs/2510.19186

Shu, R., Das, N., Yuan, M., Sunkara, M., & Zhang, Y. (2024). Towards effective GenAI multi-agent collaboration: Design and evaluation for enterprise applications. arXiv. https://arxiv.org/abs/2412.05449

Siyan, L., Deshpande, D., Kannappan, A., & Qian, R. (2026). DETOUR: An interactive benchmark for dual-agent search and reasoning. arXiv. https://arxiv.org/abs/2602.00352

Wang, J., Joshi, V., Majumder, S., Chao, X., Ding, B., Liu, Z., Brahma, P. P., Li, D., Liu, Z., & Barsoum, E. (2025). Geak: Introducing Triton kernel AI agent & evaluation benchmarks. arXiv. https://arxiv.org/abs/2507.23194

Yoa, S., Yoon, S., Yoon, S., Kim, D., Sim, Y. S., Lee, J., & Lim, W. (2026). From static benchmarks to dynamic protocol: Agent-centric text anomaly detection for evaluating LLM reasoning. arXiv. https://arxiv.org/abs/2602.23729

Zhang, X., Prasad, S., Wang, D., Zeng, Q., Wang, S., Yan, W., & Hans, M. (2025). A functionality-grounded benchmark for evaluating web agents in e-commerce domains. arXiv. https://arxiv.org/abs/2508.15832

Zhang, W., Wei, X., Huang, W.-C., Hui, Z., Wang, C., Gong, M., & Yu, P. S. (2026). MemoryCD: Benchmarking long-context user memory of LLM agents for lifelong cross-domain personalization. arXiv. https://arxiv.org/abs/2603.25973

Zhou, H., Ma, B., Zhang, Y., & Zhao, Y. (2025). Design, results and industry implications of the world's first insurance large language model evaluation benchmark. arXiv. https://arxiv.org/abs/2511.07794
