# Systematic Literature Review: LLM Agents for Software Engineering

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "LLM agents software engineering", cs.SE, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agents for software engineering reveals a rapidly evolving field transitioning from assistive tools to autonomous contributors in software development workflows. The ten surveyed papers collectively demonstrate that multi-agent architectures are becoming the dominant paradigm for tackling complex software engineering tasks, from issue resolution and code summarization to chaos engineering and architectural assessment. A key insight across the literature is that practical progress increasingly depends not on stronger base models, but on better external cognitive infrastructure—memory systems, skill modules, and coordination protocols that transform hard cognitive burdens into forms that models can solve more reliably. However, the field faces significant challenges in evaluation reproducibility, with current benchmarks often failing to capture realistic development contexts and contamination-aware assessment.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "LLM agents software engineering", filtered to category cs.SE, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Agent System Architectures for Software Engineering Tasks

The surveyed literature demonstrates a clear shift toward multi-agent architectures as the preferred approach for complex software engineering tasks. Rather than relying on single LLM invocations, researchers are designing systems where multiple specialized agents collaborate through structured protocols to achieve higher quality outcomes.

Becattini et al. (2026) present CAPRA, a multi-agent LLM system that coordinates specialized agents with deterministic Evidence Anchoring and a ConsistencyManager agent for cross-verification, achieving 88.8% criterion satisfaction on software architecture deliverables. Similarly, Nguyen et al. (2026) introduce Metagente, employing a Teacher-Student architecture where multiple LLM agents collaborate to generate summaries of software documentation, outperforming baselines in both relevance and precision.

Oliveira et al. (2026) provide a mixed-method evaluation of MAS frameworks, finding that while current frameworks offer good coverage of fundamental multi-agent components, advanced features such as telemetry remain missing. Their empirical evaluation showed no significant difference in ROUGE scores across frameworks for summarization tasks, suggesting that framework selection may matter less than coordination design.

### Theme 2: Evaluation Challenges and Benchmark Development

A second major theme concerns the significant challenges in evaluating LLM agents for software engineering, with multiple papers calling for more rigorous, reproducible, and realistic assessment methodologies.

Li and Storhaug (2026) analyze 18 papers on Agentic AI in software engineering from top venues (ICSE 2025-2026, FSE 2025, ASE 2025, ISSTA 2025), finding that current evaluations suffer from missing information in evaluation design descriptions, making reproduction infeasible. They propose guidelines recommending public accessibility of Thought-Action-Result (TAR) trajectories and LLM interaction data to enable systematic analysis across approaches.

Popescu (2026) argues that existing evaluation techniques are fragmented and provide distorted projections of true model capabilities, often relying on hypothetical syntactic scenarios rather than realistic contexts. The proposed methodology emphasizes contamination-awareness, in-the-wild agentic behavior assessment, and trajectory-aware benchmarks that capture realistic coding contexts and human-aligned behavior.

Xiang et al. (2026) introduce Rust-SWE-bench, a benchmark of 500 real-world repository-level tasks from 34 Rust repositories, addressing the gap in language-specific evaluation. Their comprehensive evaluation reveals that ReAct-style agents resolve only up to 21.2% of issues, limited by challenges in comprehending repository-wide code structure and complying with Rust's strict semantics.

### Theme 3: Externalization and Harness Engineering

The third theme identifies a fundamental shift in how agent capabilities are constructed—moving from model-centric improvements to environment-centric reorganization through externalization of memory, skills, and protocols.

Zhou et al. (2026) provide a unified review of externalization in LLM agents, arguing that agents are increasingly built by reorganizing the runtime environment rather than changing model weights. They identify three distinct but coupled forms of externalization: memory (externalizing state across time), skills (externalizing procedural expertise), and protocols (externalizing interaction structure), with harness engineering serving as the unification layer that coordinates externalized modules into governed execution.

This perspective explains why practical agent progress increasingly depends on better external cognitive infrastructure rather than solely stronger base models. The transformation of hard cognitive burdens into forms that models can solve more reliably represents a systems-level approach to agent design.

### Theme 4: Expanding Scope of Software Engineering in the Agentic Era

Several papers address how software engineering as a discipline must adapt to the shift from purely executable code to semi-executable artifacts in the era of AI-based agentic systems.

Feldt et al. (2026) introduce the Semi-Executable Stack, a six-ring diagnostic reference model spanning executable artifacts, instructional artifacts, orchestrated execution, controls, operating logic, and societal and institutional fit. Their worked cases demonstrate that the important shift in software engineering is not loss of relevance but expansion beyond executable code to semi-executable artifacts, requiring new diagnostic tools and preserve-versus-purify heuristics for legacy process decisions.

Treude and Storey (2025) examine how LLM integration transforms the phenomena studied, methods and theories relied upon, data analyzed, and threats to validity in empirical software engineering. They argue that foundational constructs such as 'developer', 'artifact', and 'interaction' are being fundamentally reshaped as boundaries between social and technical actors blur.

### Theme 5: Automation of Specialized Software Engineering Practices

The literature demonstrates successful application of LLM agents to automate specialized software engineering practices that previously required significant human expertise.

Kikuta et al. (2025) present ChaosEater, a system that automates the entire Chaos Engineering cycle using LLMs by predefining an agentic workflow according to a systematic CE cycle and assigning subdivided processes to LLMs. Their system consistently completes reasonable CE cycles with significantly low time and monetary costs, enabling anyone to build resilient systems by removing the need for manual experiment planning and multi-domain expertise.

Xiang et al. (2026) propose RUSTFORGER, a novel agentic approach with automated test environment setup and dynamic tracing for repository-level Rust issue resolution. Using Claude-Sonnet-3.7, RUSTFORGER resolves 28.6% of tasks, a 34.9% improvement over the strongest baseline, and uniquely solves 46 tasks that no other agent could solve.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that multi-agent architectures outperform single-agent approaches for complex software engineering tasks (Becattini et al., 2026; Nguyen et al., 2026; Oliveira et al., 2026). There is also strong agreement that current evaluation practices are inadequate and require fundamental reform toward transparency, reproducibility, and realistic assessment contexts (Li & Storhaug, 2026; Popescu, 2026; Xiang et al., 2026). The literature collectively emphasizes that external infrastructure—memory, skills, protocols, and harness engineering—is increasingly critical to agent success (Zhou et al., 2026).

**Disagreements**: The literature shows some tension between conceptual and empirical approaches. While Feldt et al. (2026) and Treude and Storey (2025) offer conceptual frameworks for understanding the paradigm shift, empirical papers like Xiang et al. (2026) and Kikuta et al. (2025) focus on specific technical improvements without engaging deeply with the broader implications. Additionally, Oliveira et al. (2026) find no significant difference in performance across MAS frameworks for summarization, suggesting framework choice may be less critical than other papers imply about coordination mechanisms.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Limited empirical validation scope**: Multiple studies acknowledge their evaluations are limited to single use cases or specific domains (README summarization, Rust ecosystem, Kubernetes systems), raising questions about generalizability across programming languages and software engineering tasks (Oliveira et al., 2026; Xiang et al., 2026; Kikuta et al., 2025).

2. **Missing telemetry and monitoring**: Current MAS frameworks lack advanced features such as agent telemetry, making it difficult to understand agent behavior and debug coordination failures (Oliveira et al., 2026).

3. **Human oversight requirements**: Even highly automated systems like CAPRA require human oversight for subjective assessment dimensions, suggesting that full automation remains elusive for tasks requiring judgment (Becattini et al., 2026).

4. **Contamination and reproducibility**: The field lacks standardized approaches to preventing data contamination and ensuring reproducibility in agentic evaluations, with Li and Storhaug (2026) noting that current practices make reproduction infeasible.

5. **Cross-language generalization**: Most empirical work focuses on specific languages (Rust) or platforms (Kubernetes), leaving open whether findings generalize across the diverse software engineering landscape.

## Per-Paper Annotations

### Becattini et al. (2026)

**Research question**: How can automated assessment be extended to software architecture deliverables that require analyzing structural completeness and requirements traceability?
**Methodology**: CAPRA is a multi-agent LLM system that coordinates multiple specialized agents with a Python-based microservice for multi-modal document extraction using PyMuPDF and vision-enabled LLMs, employing deterministic Evidence Anchoring and a ConsistencyManager agent for cross-verification, evaluated on 10 student reports.
**Key findings**:
- CAPRA satisfied 88.8% of evaluated criteria under a strict two-rater aggregation rule
- The system achieved moderate inter-rater agreement with human evaluators (kappa = 0.582)
- Each report was processed in slightly over 4 minutes
- The system generates personalized, template-compliant LaTeX feedback for software architecture deliverables
- Human oversight remains essential for subjective assessment dimensions
**Limitations**: Human oversight remains essential for subjective assessment dimensions, and the evaluation was preliminary with only 10 student reports.

### Feldt et al. (2026)

**Research question**: How should software engineering adapt to the shift from executable code to semi-executable artifacts in the era of AI-based agentic systems?
**Methodology**: This conceptual keynote paper introduces the Semi-Executable Stack, a six-ring diagnostic reference model, and develops the argument through three worked cases and a preserve-versus-purify heuristic for legacy process decisions.
**Key findings**:
- The important shift in software engineering is not loss of relevance but expansion beyond executable code to semi-executable artifacts
- The Semi-Executable Stack model spans six rings: executable artifacts, instructional artifacts, orchestrated execution, controls, operating logic, and societal and institutional fit
- The model helps locate where contributions, bottlenecks, or organizational transitions primarily sit and their dependencies on adjacent rings
- A preserve-versus-purify heuristic aids decisions about which legacy software engineering processes should be kept versus redesigned
**Limitations**: This is a conceptual and diagnostic paper rather than empirical, so findings are based on worked cases and argumentation rather than quantitative evaluation.

### Kikuta et al. (2025)

**Research question**: How can the entire Chaos Engineering cycle be automated using LLMs to enable anyone to build resilient systems at low cost?
**Methodology**: ChaosEater automates the entire CE cycle with LLMs by predefining an agentic workflow according to a systematic CE cycle and assigning subdivided processes to LLMs, targeting Kubernetes-based software systems through software engineering tasks including requirement definition, code generation, testing, and debugging.
**Key findings**:
- ChaosEater consistently completes reasonable CE cycles with significantly low time and monetary costs
- The system automates the entire CE cycle, not just experiment execution
- CE cycles are qualitatively validated by both human engineers and LLMs
- The system enables anyone to build resilient systems by removing the need for manual experiment planning and multi-domain expertise
- ChaosEater targets Kubernetes-based software systems specifically
**Limitations**: Not stated in abstract.

### Li and Storhaug (2026)

**Research question**: How can evaluations of Agentic AI in software engineering be made more reproducible, explainable, and effective?
**Methodology**: The study analyzes 18 papers on Agentic AI in software engineering published or accepted by ICSE 2025-2026, FSE 2025, ASE 2025, and ISSTA 2025 to synthesize current evaluation practices and identify limitations, with a proof-of-concept case study demonstrating how TAR trajectories can support systematic analysis.
**Key findings**:
- Current Agentic AI evaluations in software engineering suffer from missing information in evaluation design descriptions, making reproduction of results infeasible
- Underlying LLMs function as black boxes, making it difficult to justify the superiority of Agentic AI approaches over baselines
- The paper proposes guidelines recommending public accessibility of Thought-Action-Result (TAR) trajectories and LLM interaction data
- Making TAR trajectories publicly accessible enables subsequent studies to more effectively analyze strengths and weaknesses of different Agentic AI approaches
**Limitations**: The study is limited to analyzing papers from specific venues (ICSE 2025-2026, FSE 2025, ASE 2025, ISSTA 2025), which may not represent the full landscape of Agentic AI evaluation practices.

### Nguyen et al. (2026)

**Research question**: Can an LLM-based Multi-Agent System improve the automation and quality of software document summarization?
**Methodology**: Metagente is an LLM-based Multi-Agent System using a Teacher-Student architecture where multiple LLM agents collaborate to generate summaries of software documentation, evaluated on real-world datasets against baselines.
**Key findings**:
- Metagente effectively generates concise and accurate summaries of software documentation
- The Teacher-Student architecture with multiple collaborating LLM agents enhances relevance and precision of produced summaries
- Metagente outperforms baselines in streamlining workflows for requirements analysis and technical documentation summarization
- The evaluation provides evidence that LLM-based MAS can improve summarization for software engineering tasks
**Limitations**: Not stated in abstract.

### Oliveira et al. (2026)

**Research question**: What are the existing tools and frameworks for implementing LLM-based Multi-Agent Systems in software engineering, and what are their capabilities and challenges from a developer perspective?
**Methodology**: The study employs a mixed-method approach: first, a quantitative analysis of open source MAS frameworks evaluating documentation, features, and capabilities from developers' perspective; second, a qualitative evaluation implementing a README summarization use case across selected frameworks.
**Key findings**:
- Selected MAS frameworks provide good coverage of fundamental Multi-Agent System components
- Advanced features such as telemetry of agents are still missing from current frameworks
- Empirical evaluation shows no significant difference in ROUGE scores across frameworks for the summarization task
- Developers face challenges in selecting the right technology, devising coordination rules, and designing specific roles for agents
**Limitations**: The empirical evaluation is limited to a single use case (README.MD summarization), which may not generalize to other MAS application scenarios.

### Popescu (2026)

**Research question**: How can evaluation techniques for LLM-powered agents be improved to better reflect true model capabilities in real-world software development practice?
**Methodology**: The research proposes a comprehensive evaluation methodology for LLM-powered agents grounded in real-world software development practice, focusing on contamination-awareness, in-the-wild agentic behavior assessment, and trajectory-aware benchmarks and metrics.
**Key findings**:
- Existing evaluation techniques are limited due to their fragmented nature and distorted projection of true model capabilities
- Current evaluations often rely on hypothetical syntactic scenarios rather than realistic contexts
- The proposed approach captures realistic coding contexts, human-aligned behavior, and model failure modes
- The methodology addresses the transition of LLMs from assistive companions to autonomous contributors in collaborative development environments
**Limitations**: Not stated in abstract.

### Treude and Storey (2025)

**Research question**: How does the integration of LLMs and autonomous agents into software engineering disrupt established empirical research paradigms?
**Methodology**: This vision paper examines how LLM integration transforms the phenomena studied, methods and theories relied upon, data analyzed, and threats to validity in empirical software engineering, discussing the need for adapting research questions, instruments, and validation standards.
**Key findings**:
- The adoption of LLMs and autonomous agents marks an enduring paradigm shift in software engineering
- Traditional empirical methods remain central but AI introduces new data modalities and alters causal assumptions
- Foundational constructs such as 'developer', 'artifact', and 'interaction' are being fundamentally reshaped
- Boundaries between social and technical actors blur as humans and AI agents co-create
- Reproducibility becomes contingent on model updates and prompt contexts in dynamic AI-mediated environments
**Limitations**: Not stated in abstract.

### Xiang et al. (2026)

**Research question**: How can LLM-based agents be evaluated and improved for automated repository-level Rust issue resolution?
**Methodology**: The study introduces Rust-SWE-bench, a benchmark of 500 real-world repository-level tasks from 34 Rust repositories, then conducts comprehensive evaluation of four agents and four LLMs, leading to the proposal of RUSTFORGER, a novel agentic approach with automated test environment setup and dynamic tracing.
**Key findings**:
- Rust-SWE-bench provides the first large-scale, repository-level benchmark for Rust issue resolution with 500 tasks from 34 repositories
- ReAct-style agents resolve up to 21.2% of issues but are limited by challenges in comprehending repository-wide code structure and complying with Rust's strict type and trait semantics
- Issue reproduction is critical for task resolution in the Rust ecosystem
- RUSTFORGER using Claude-Sonnet-3.7 resolves 28.6% of tasks, a 34.9% improvement over the strongest baseline
- RUSTFORGER uniquely solves 46 tasks that no other agent could solve across all adopted advanced LLMs
**Limitations**: The study focuses specifically on the Rust programming language ecosystem, so findings may not generalize to other programming languages with different characteristics.

### Zhou et al. (2026)

**Research question**: How does the shift toward externalizing capabilities in LLM agent infrastructure transform how agents are built and what explains practical agent progress?
**Methodology**: The paper reviews the shift toward externalization through the lens of cognitive artifacts, tracing a historical progression from weights to context to harness, and analyzing memory, skills, and protocols as three distinct but coupled forms of externalization within a systems-level framework.
**Key findings**:
- LLM agents are increasingly built by reorganizing the runtime environment rather than changing model weights
- Memory externalizes state across time, skills externalize procedural expertise, and protocols externalize interaction structure
- Harness engineering serves as the unification layer that coordinates externalized modules into governed execution
- Agent infrastructure transforms hard cognitive burdens into forms that models can solve more reliably
- Practical agent progress increasingly depends on better external cognitive infrastructure, not only stronger models
**Limitations**: Not stated in abstract.

## References

Becattini, M., Caselli, N., Minin, M., Verdecchia, R., & Vicario, E. (2026). CAPRA: Scaling feedback on software architecture deliverables with a multi-agent LLM system. arXiv. https://arxiv.org/abs/2606.18976

Feldt, R., Lenberg, P., Frattini, J., & Parthasarathy, D. (2026). The semi-executable stack: Agentic software engineering and the expanding scope of SE. arXiv. https://arxiv.org/abs/2604.15468

Kikuta, D., Ikeuchi, H., & Tajiri, K. (2025). LLM-powered fully automated chaos engineering: Towards enabling anyone to build resilient software systems at low cost. arXiv. https://arxiv.org/abs/2511.07865

Li, J., & Storhaug, A. (2026). Reproducible, explainable, and effective evaluations of agentic AI for software engineering. arXiv. https://arxiv.org/abs/2604.01437

Nguyen, D. S. H., Nguyen, M. T., Nguyen, P. T., Di Rocco, J., & Di Ruscio, D. (2026). Automated summarization of software documents: An LLM-based multi-agent approach. arXiv. https://arxiv.org/abs/2606.24689

Oliveira, M. C. S. D., Ibiyo, M. O., Gianrusso, M., Di Sipio, C., Di Ruscio, D., & Nguyen, P. T. (2026). Developing LLM-based multi-agent systems in software engineering: A mixed-method experience report. arXiv. https://arxiv.org/abs/2608.11965

Popescu, R. M. (2026). Reliable and developer-aligned evaluation of agents for software engineering. arXiv. https://arxiv.org/abs/2607.06713

Treude, C., & Storey, M.-A. (2025). Generative AI and empirical software engineering: A paradigm shift. arXiv. https://arxiv.org/abs/2502.08108

Xiang, J., He, W., Wang, X., Tian, H., & Zhang, Y. (2026). Evaluating and improving automated repository-level Rust issue resolution with LLM-based agents. arXiv. https://arxiv.org/abs/2602.22764

Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., Lin, J., & Zhang, W. (2026). Externalization in LLM agents: A unified review of memory, skills, protocols and harness engineering. arXiv. https://arxiv.org/abs/2604.08224
