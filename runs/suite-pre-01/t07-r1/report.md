# Systematic Literature Review: Code Generation with Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "code generation LLM", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on code generation with large language models has evolved from basic capability demonstrations to sophisticated frameworks addressing evaluation, specialization, and verification. The surveyed papers collectively reveal a field maturing beyond "can LLMs generate code?" to "how well, for what purposes, and under what constraints?" Three dominant threads emerge: (1) benchmark development exposing limitations of existing evaluation methods, (2) multi-agent and tool-augmented architectures extending code generation beyond single-pass generation, and (3) verification and constraint enforcement mechanisms ensuring generated code meets formal requirements. The field shows growing recognition that code generation quality depends not just on model scale but on task structure, evaluation rigor, and the integration of symbolic verification layers.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query `"code generation LLM"`, filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmark Development and Evaluation Rigor

A significant portion of recent work focuses on creating more rigorous, comprehensive benchmarks for code generation LLMs. Yadav et al. (2024) identified critical biases in popular benchmarks like HumanEval and MBPP, which concentrate on a narrow set of programming concepts and include too many easy tasks, potentially inflating performance estimates. Their PythonSaga benchmark addresses this with 185 hand-crafted prompts covering 38 programming concepts across diverse difficulty levels, revealing that existing Code-LLMs perform poorly when properly evaluated.

This evaluation focus extends to domain-specific benchmarks. Gramacki et al. (2024) constructed a geospatial code generation benchmark, recognizing that code generation LLMs are typically not evaluated on domain-specific tasks despite their potential utility in specialized fields like spatial data science. Similarly, Chervyakov et al. (2025) introduced MERA Code, addressing the gap in non-English evaluation by creating a comprehensive benchmark for Russian language code generation across 11 tasks and 8 programming languages.

A more theoretical evaluation approach comes from Yoran et al. (2025), who proposed the KoLMogorov-Test, framing compression-as-intelligence where models must generate the shortest program producing a given sequence. This approach provides an essentially infinite supply of test instances with an ungameable metric, though current flagship models like GPT-4o and Llama-3.1-405B perform poorly on both natural and synthetic sequences.

### Theme 2: Multi-Agent and Tool-Augmented Architectures

Recent work increasingly moves beyond single-model code generation to multi-agent frameworks that decompose complex tasks and incorporate verification. Trirat et al. (2024) introduced AutoML-Agent, a multi-agent framework for full-pipeline automated machine learning that coordinates specialized LLM agents through retrieval-augmented planning and multi-stage verification. Their approach demonstrates that decomposing plans into parallel sub-tasks (data preprocessing, neural network design) and verifying executed results significantly improves success rates across diverse domains.

The self-evolution paradigm extends this further. Kar et al. (2026) proposed a hierarchical self-evolving multi-agent framework integrating a Base LLM, operational SLM agent, Code-Generation LLM, and Teacher-LLM to enable continuous post-deployment adaptation. Their framework escalates from tool use to tool synthesis to evolutionary improvement (via Curriculum Learning, Reward-Based Learning, or Genetic Algorithms) when tasks exceed current capabilities, demonstrating that evolved agents consistently outperform their originals.

### Theme 3: Verification and Constraint Enforcement

A critical challenge in code generation is ensuring generated code satisfies constraints beyond mere syntactic correctness. Chen et al. (2026) presented CEDAR, a counterexample-guided framework that grounds natural language instructions as regular languages over environment event traces, representing both skills and specifications as deterministic finite automata. This approach transforms constraints into executable, verifiable objects that can be composed and enforced by construction rather than through repeated prompting. In Minecraft evaluations, CEDAR maintained temporal and spatial constraints that program-generating baselines failed to preserve while reducing cumulative LLM queries through skill amortization.

Assogba and Ren (2024) examined long-range dependency handling in code generation, finding that performance degrades significantly (up to 2x) when functions reference other functions defined later in the prompt, particularly for models using sliding window attention. Their work shows that simple prompt modifications using call graph information can improve multi-step retrieval performance up to 3x, highlighting that code generation quality depends on information organization, not just model capability.

### Theme 4: Efficiency and Practical Deployment

Several papers address the practical question of optimal model selection and deployment strategies. Hassid et al. (2024) challenged the assumption that larger models are always better by comparing code generation LLMs under equal budget constraints. They found that repeated use of smaller models can yield improvements up to 15% when unit-tests are available for output selection, though ranking-based selection without unit-tests falls short of larger model performance. This work highlights the importance of studying output ranking approaches and the critical role of verification mechanisms in realizing efficiency gains.

Li et al. (2026) questioned whether LLMs are necessary for SQL generation, analyzing 376 databases to show that practical SQL query complexity is finite and follows a Power Law distribution where 70% of queries can be covered with just 13% of template types. Their findings suggest that templates could be safer, cheaper, and more auditable than LLMs for database access tasks, operating in a narrow, highly formulaic space where the overhead of LLMs may be unjustified.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the inadequacy of current evaluation practices. Yadav et al. (2024), Gramacki et al. (2024), and Chervyakov et al. (2025) all identify that existing benchmarks focus on narrow task types, neglect domain-specific requirements, or overlook non-English languages. There is also broad agreement that verification mechanisms are essential: whether through unit-tests (Hassid et al., 2024), multi-stage verification (Trirat et al., 2024), or formal automata-based constraints (Chen et al., 2026), all successful systems incorporate explicit correctness checking rather than relying on LLMs to produce correct code in a single pass.

**Disagreements**: The literature shows tension around the role of model scale versus architectural innovation. Hassid et al. (2024) demonstrate that smaller models can outperform larger ones under equal budget constraints with proper verification, while Kar et al. (2026) show that self-evolving architectures can improve agent capabilities post-deployment. However, Yoran et al. (2025) find that even flagship models (GPT-4o, Llama-3.1-405B) perform poorly on their KoLMogorov-Test, suggesting fundamental limitations that cannot be overcome by scale alone. Li et al. (2026) go further, questioning whether LLMs are appropriate for certain code generation tasks at all, arguing that template-based approaches may be superior for formulaic domains like SQL.

## Gaps and Open Questions

Several gaps emerge from the limitations acknowledged across the surveyed papers:

1. **Language generalization**: MERA Code (Chervyakov et al., 2025) focuses on Russian, but the broader challenge of non-English code generation remains underexplored. PythonSaga (Yadav et al., 2024) is limited to Python, and the geospatial benchmark (Gramacki et al., 2024) does not address multilingual requirements.

2. **Synthetic-to-real generalization**: Yoran et al. (2025) explicitly note that gains on synthetic data generalize poorly to real-world data in their KoLMogorov-Test, a limitation echoed in Kar et al.'s (2026) observation that evolution mechanisms may not generalize equally well to all task types.

3. **Context window limitations**: Assogba and Ren (2024) evaluated only up to 8k token contexts, but modern models now support much larger windows. The degradation patterns they observed may worsen or improve at extreme scales.

4. **Production readiness**: Multiple papers (Trirat et al., 2024; Chervyakov et al., 2025) acknowledge gaps in understanding true model capabilities and risks in production environments. The transition from benchmark performance to deployed system reliability remains underexplored.

5. **Verification mechanism comparison**: While all papers agree verification is necessary, there is no systematic comparison of verification approaches (unit-tests, multi-stage verification, automata-based constraints, template matching) to determine which is most effective for different task types.

## Per-Paper Annotations

### Assogba and Ren (2024)

**Research question**: How well do code generation models handle long-range dependencies in large context windows?
**Methodology**: Analyzed code generation models using multi-step key retrieval tasks in context windows up to 8k tokens with progressively increasing difficulty levels.
**Key findings**:
- Performance degrades significantly (up to 2x) when functions reference other functions defined later in the prompt
- Models using sliding window attention mechanisms struggle with references beyond a single window size
- Simple prompt modifications using call graph information can improve multi-step retrieval performance up to 3x
- Long-context performance requires deeper consideration beyond single fact retrieval within documents
**Limitations**: Evaluation limited to 8k token context windows and focused on specific multi-step retrieval task types rather than broader code generation scenarios.

### Chen et al. (2026)

**Research question**: How can we create verifiable, composable interfaces for language-guided embodied agents that preserve user-imposed constraints while the world changes?
**Methodology**: Presented CEDAR, a counterexample-guided framework that grounds instructions as regular languages over environment event traces, using language models for semantic judgments and execution traces for correction, representing both skills and specifications as deterministic finite automata.
**Key findings**:
- Regular languages offer a practical verification layer between natural-language instructions and embodied-agent policies
- CEDAR maintains temporal and spatial constraints that program-generating baselines fail to preserve
- Learned skills can be intersected with specifications, yielding controllers that enforce constraints by construction
- Framework amortizes reuse of learned skills, reducing cumulative LLM queries
- Free-form programs from LLMs provide no stable object to verify, compose, or repair from failing traces
**Limitations**: Evaluation was conducted in Minecraft with specific simulator/API observations, which may limit generalizability to other embodied agent domains. The approach requires adaptation of the automata-based verification framework for different environments and constraint types.

### Chervyakov et al. (2025)

**Research question**: How can code generation LLMs be properly evaluated beyond natural language tasks, particularly for non-English languages and real-world code quality?
**Methodology**: Proposed MERA Code benchmark with 11 evaluation tasks spanning 8 programming languages in Russian, featuring a taxonomy of practical coding skills, open-source codebase, scoring system compatible with existing programming environments, and a leaderboard platform for submissions.
**Key findings**:
- Current evaluations primarily focus on natural language tasks, overlooking code quality and executable performance
- Most benchmarks prioritize high-level reasoning over real-world code performance
- Created comprehensive evaluation framework covering 11 tasks across 8 programming languages
- Evaluated both open LLMs and frontier API models, identifying limitations in non-English coding tasks
- Publicly released benchmark aims to standardize evaluation procedures and guide future research
**Limitations**: The benchmark is specifically focused on Russian language evaluation, which may limit generalizability to other non-English languages. The study reveals gaps in understanding true model capabilities and risks in production environments that require further investigation.

### Gramacki et al. (2024)

**Research question**: How well do code generation LLMs perform on geospatial coding tasks, given that they are typically not evaluated on this domain?
**Methodology**: Constructed an evaluation benchmark by categorizing geospatial tasks based on complexity and required tools, creating a dataset with specific coding problems and test scenarios for automatic correctness checking, then tested existing code generation LLMs on these tasks.
**Key findings**:
- Geospatial domain poses different challenges than general code generation tasks
- Created a publicly available dataset and reproducible evaluation code on GitHub
- Tested multiple existing code generation LLMs specifically on geospatial tasks
- The benchmark can serve as a standard evaluation tool for new LLMs in geospatial applications
- Dataset enables development of coding assistants tailored for geospatial applications
**Limitations**: Code generation LLMs are typically not evaluated on geospatial tasks, and the domain poses unique challenges that require specialized benchmarking. The study acknowledges the need for future models capable of solving geospatial coding tasks with high accuracy.

### Hassid et al. (2024)

**Research question**: Are larger LLMs actually better than smaller ones when both operate under the same compute budget?
**Methodology**: Compared code generation LLMs of various sizes under equal budget constraints (e.g., running a 70B model once versus generating five outputs from a 13B model), using a standard unit-test setup to select correct outputs and evaluating scenarios with and without unit-tests.
**Key findings**:
- Repeated use of smaller models can yield consistent improvements of up to 15% across five tasks when unit-tests are available
- Ranking-based selection of candidates from smaller models falls short of larger model performance when unit-tests are unavailable
- The common belief that larger models are always better does not hold under equal budget constraints
- Unit-test availability is critical for realizing benefits from smaller model repetition
- Approaches for ranking LLM outputs need further study for scenarios without unit-tests
**Limitations**: The benefits of smaller models depend heavily on unit-test availability for output selection. In scenarios without unit-tests, ranking-based approaches cannot match the performance of single outputs from larger models, limiting the practical applicability of budget reallocation strategies.

### Kar et al. (2026)

**Research question**: How can we enable LLM agents to autonomously expand capabilities, generate new tools, and evolve their reasoning after deployment?
**Methodology**: Created a hierarchical self-evolving multi-agent framework integrating Base LLM, operational SLM agent, Code-Generation LLM, and Teacher-LLM; evaluated Curriculum Learning, Reward-Based Learning, and Genetic Algorithm evolution paradigms on the TaskCraft dataset.
**Key findings**:
- Curriculum Learning delivers fast recovery and strong generalization capabilities
- Reward-Based Learning excels on high-difficulty tasks
- Genetic Algorithm offers high behavioral diversity in evolved agents
- Evolved agents outperform their original versions across all experimental settings
- Framework demonstrates robust, autonomous, self-improving agentic evolution
**Limitations**: Evaluation limited to the TaskCraft dataset; evolution mechanisms may not generalize equally well to all task types and real-world scenarios.

### Li et al. (2026)

**Research question**: How complex is SQL query generation in practice, and are LLMs necessary for this task given that query complexity may be bounded?
**Methodology**: Analyzed a sample of 376 databases to study the relationship between database complexity and SQL query complexity, examining template distribution patterns and frequency of query types.
**Key findings**:
- SQL queries have finite practical complexity bounded by real-life utility and human needs
- 70% of tested queries can be covered with just 13% of all template types, following a Power Law-like distribution
- No clear monotonic relationship exists between increases in database table count and SQL query complexity
- The majority of SQL queries are predictable and formulaic
- Templates could be safer, cheaper, and more auditable than LLMs for database access tasks
**Limitations**: The study focuses on practical, utility-bounded queries rather than theoretical maximum complexity. While databases can become unbounded in complexity, the analysis is limited to real-world human needs and may not capture edge cases or highly specialized query patterns.

### Trirat et al. (2024)

**Research question**: How can we create a more usable AutoML system that handles the full pipeline from data retrieval to deployment using LLMs?
**Methodology**: Developed a multi-agent framework with specialized LLM agents, retrieval-augmented planning strategy, parallel sub-task execution, and multi-stage verification to automate the full AutoML pipeline.
**Key findings**:
- AutoML-Agent achieves higher success rate in automating the full AutoML process compared to existing methods
- Retrieval-augmented planning enhances exploration to search for more optimal plans
- Parallel execution of specialized agents for sub-tasks makes the search process more efficient
- Multi-stage verification successfully guides code generation LLMs to implement successful solutions
- System yields good performance across diverse domains (evaluated on 7 downstream tasks using 14 datasets)
**Limitations**: Requires careful coordination between multiple agents and may not handle all edge cases in highly complex or domain-specific pipelines.

### Yadav et al. (2024)

**Research question**: How can we create a better benchmark for evaluating code generation LLMs that addresses bias and difficulty issues in existing benchmarks?
**Methodology**: Conducted large-scale human evaluation of HumanEval and MBPP benchmarks to analyze diversity and difficulty, then created PythonSaga with 185 hand-crafted prompts covering 38 programming concepts across diverse difficulty levels.
**Key findings**:
- Existing benchmarks (HumanEval, MBPP) show critical bias towards a limited set of programming concepts
- Most programming concepts are entirely neglected in current benchmarks
- Easy tasks are prevalent in existing benchmarks, potentially inflating model performance estimates
- PythonSaga demonstrates poor performance of existing Code-LLMs, validating its robustness as a benchmark
**Limitations**: The benchmark is limited to Python programming language and may not generalize to other programming languages or coding paradigms.

### Yoran et al. (2025)

**Research question**: Can code generation models approximate Kolmogorov compression as a measure of intelligence?
**Methodology**: Introduced the KoLMogorov-Test where models generate the shortest program to produce given sequences; evaluated on audio, text, DNA data, and sequences from random synthetic programs.
**Key findings**:
- Current flagship models (GPT4-o and Llama-3.1-405B) perform poorly on both natural and synthetic sequences
- KT provides essentially infinite problem instances with an ungameable evaluation metric (compression)
- Training code generation models on synthetic data achieves lower compression rates than previous approaches
- Gains on synthetic data generalize poorly to real-world data
- New innovations beyond current approaches are necessary for additional gains on KT
**Limitations**: Kolmogorov compression is theoretically uncomputable, and synthetic-to-real data generalization remains a significant challenge requiring new methodological innovations.

## References

Assogba, Y., & Ren, D. (2024). Evaluating long range dependency handling in code generation LLMs. arXiv. https://arxiv.org/abs/2407.21049

Chen, L., Velasquez, A., & Trivedi, A. (2026). CEDAR: Automata as verifiable interfaces for language-guided embodied action. arXiv. https://arxiv.org/abs/2608.27797

Chervyakov, A., Kharitonov, A., Zadorozhny, P., Adamenko, P., Levichev, R., Vorobev, D., Salikhov, D., Valeev, A., Pestova, A., Dziuba, M., Alimova, I., Zavgorodnev, A., Medvedev, A., Moiseev, S., Bruches, E., Grebenkin, D., Derunets, R., Vladimir, V., Emelyanov, A., Babaev, D., Ivanov, V. V., Malykh, V., & Fenogenova, A. (2025). MERA code: A unified framework for evaluating code generation across tasks. arXiv. https://arxiv.org/abs/2507.12284

Gramacki, P., Martins, B., & Szymański, P. (2024). Evaluation of code LLMs on geospatial code generation. arXiv. https://arxiv.org/abs/2410.04617

Hassid, M., Remez, T., Gehring, J., Schwartz, R., & Adi, Y. (2024). The larger the better? Improved LLM code-generation via budget reallocation. arXiv. https://arxiv.org/abs/2404.00725

Kar, I., Zonunpuia, S., & Ralte, Z. (2026). Towards AGI a pragmatic approach towards self evolving agent. arXiv. https://arxiv.org/abs/2601.11658

Li, Y., Mimno, D., & Jo, U. E. S. (2026). Are LLMs overkill for databases?: A study on the finiteness of SQL. arXiv. https://arxiv.org/abs/2603.25568

Trirat, P., Jeong, W., & Hwang, S. J. (2024). AutoML-agent: A multi-agent LLM framework for full-pipeline AutoML. arXiv. https://arxiv.org/abs/2410.02958

Yadav, A., Beniwal, H., & Singh, M. (2024). PythonSaga: Redefining the benchmark to evaluate code generating LLMs. arXiv. https://arxiv.org/abs/2401.03855

Yoran, O., Zheng, K., Gloeckle, F., Gehring, J., Synnaeve, G., & Cohen, T. (2025). The KoLMogorov test: Compression by code generation. arXiv. https://arxiv.org/abs/2503.13992
