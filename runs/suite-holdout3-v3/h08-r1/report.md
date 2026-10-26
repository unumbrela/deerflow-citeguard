# Systematic Literature Review: LLM Agents for Software Engineering

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "LLM agents software engineering", filtered to category cs.SE, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on LLM agents for software engineering, revealing a rapidly evolving field focused on evaluation methodologies, multi-agent architectures, and practical applications. The surveyed literature demonstrates a clear paradigm shift toward agentic systems that automate complex software engineering tasks, from issue resolution to chaos engineering. Researchers emphasize the need for reproducible evaluation frameworks, with multiple papers proposing standardized benchmarks and transparent reporting practices. The field shows strong convergence around multi-agent collaboration as a key architectural pattern, though significant gaps remain in long-term empirical validation and developer experience studies.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM agents software engineering", filtered to category cs.SE, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation Methodologies and Benchmarking

A dominant theme across the surveyed literature is the critical need for rigorous, reproducible evaluation frameworks for LLM-powered agents in software engineering. Li and Storhaug (2026) analyze 18 papers from top SE conferences and identify significant limitations in current evaluation practices, particularly the lack of reproducibility due to missing information in evaluation design descriptions. They propose guidelines recommending researchers make Thought-Action-Result (TAR) trajectories and LLM interaction data publicly accessible.

This concern is echoed by Popescu (2026), who argues that existing evaluation techniques suffer from fragmented approaches and distorted projections of true model capabilities, often derived from hypothetical syntactic scenarios rather than real-world practice. The proposed solution emphasizes contamination-awareness, in-the-wild agentic behavior assessment, and trajectory-aware benchmarks. Xiang et al. (2026) contribute Rust-SWE-bench, a benchmark of 500 real-world repository-level tasks from 34 Rust repositories, demonstrating the field's move toward realistic, large-scale evaluation datasets.

### Theme 2: Multi-Agent System Architectures

Multiple papers explore multi-agent collaboration as an architectural pattern for complex software engineering tasks. Oliveira et al. (2026) present a mixed-method experience report on developing LLM-based multi-agent systems, evaluating frameworks across documentation quality, feature coverage, and practical implementation. Their findings reveal that while fundamental multi-agent components are well-supported, advanced features like agent telemetry remain underdeveloped.

Nguyen et al. (2026) introduce Metagente, a Teacher-Student architecture where multiple LLM agents collaborate to generate summaries of software documentation, outperforming baseline methods. Becattini et al. (2026) present CAPRA, a multi-agent system for automated software architecture assessment that coordinates specialized agents with deterministic Evidence Anchoring and cross-verification mechanisms, achieving 88.8% criterion satisfaction under strict evaluation.

### Theme 3: Externalization and Infrastructure Design

A conceptual shift identified in the literature is the move from model-centric to infrastructure-centric agent design. Zhou et al. (2026) review this trend through the lens of "externalization," arguing that practical agent progress increasingly comes from reorganizing runtime infrastructure rather than changing model weights. They analyze memory (externalizing state across time), skills (externalizing procedural expertise), and protocols (externalizing interaction structure) as three coupled forms of externalization.

Feldt et al. (2026) extend this thinking with the "Semi-Executable Stack," a six-ring diagnostic model spanning from executable artifacts to societal and institutional fit. They argue that software engineering must adapt to semi-executable artifacts combining natural language, tools, workflows, and organizational routines, proposing a preserve-versus-purify heuristic for deciding which legacy processes should be kept or redesigned.

### Theme 4: Practical Applications and Domain Specialization

The surveyed papers demonstrate LLM agents applied to diverse software engineering domains. Xiang et al. (2026) focus on repository-level issue resolution in Rust, introducing RUSTFORGER which integrates automated test environment setup with Rust metaprogramming-driven dynamic tracing, achieving 28.6% task resolution compared to 21.2% for baseline agents.

Kikuta et al. (2025) present ChaosEater, a system automating the entire chaos engineering cycle for Kubernetes systems through a predefined agentic workflow. Their case studies show consistent completion of chaos engineering cycles with significantly low time and monetary costs, validated by both human engineers and LLMs.

### Theme 5: Paradigm Shifts in Software Engineering Research

Treude and Storey (2025) argue that LLMs and autonomous agents mark an enduring paradigm shift in software engineering, fundamentally transforming the phenomena studied, methods used, and data analyzed in empirical software engineering. They highlight how boundaries between social and technical actors blur as humans and AI agents co-create, and how reproducibility becomes contingent on model updates and prompt contexts. Foundational constructs such as 'developer', 'artifact', and 'interaction' are being reshaped, requiring new theoretical frameworks.

## Convergences and Disagreements

**Convergences**: The literature shows strong agreement on several points. First, multiple papers converge on the inadequacy of current evaluation practices for LLM agents (Li & Storhaug, 2026; Popescu, 2026; Xiang et al., 2026), with consensus that transparent reporting of agent trajectories and real-world benchmarks are essential. Second, there is widespread agreement that multi-agent architectures provide advantages over single-agent approaches for complex software engineering tasks (Nguyen et al., 2026; Becattini et al., 2026; Oliveira et al., 2026). Third, the literature collectively acknowledges that infrastructure and externalization matter as much as or more than model capabilities (Zhou et al., 2026; Feldt et al., 2026).

**Disagreements**: The surveyed papers show limited direct disagreement, likely because they address different aspects of the field. However, there is tension between the conceptual, agenda-setting work (Feldt et al., 2026; Treude & Storey, 2025) and the empirical, benchmark-focused papers (Xiang et al., 2026; Kikuta et al., 2025). The conceptual papers argue for fundamental reframing of software engineering, while empirical papers focus on incremental improvements within existing paradigms. Additionally, while Oliveira et al. (2026) find no significant difference in ROUGE scores across multi-agent frameworks for summarization tasks, Nguyen et al. (2026) report their multi-agent approach outperforms baselines, suggesting task-dependent effectiveness.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, limitations reporting is notably absent — 8 of 10 papers do not state limitations in their abstracts, suggesting either insufficient critical reflection or space constraints preventing discussion of constraints (Li & Storhaug, 2026; Oliveira et al., 2026; Nguyen et al., 2026; Xiang et al., 2026; Becattini et al., 2026; Popescu, 2026; Zhou et al., 2026; Kikuta et al., 2025).

Second, empirical validation is limited. While several papers present case studies or preliminary evaluations, long-term studies of agent effectiveness in production environments are absent. Becattini et al. (2026) note that human oversight remains essential for subjective assessment dimensions, but do not specify which dimensions or under what conditions agents might operate autonomously.

Third, developer experience and adoption challenges are underexplored. Oliveira et al. (2026) identify challenges in selecting technology, designing coordination rules, and defining agent roles, but the literature lacks systematic studies of how developers actually work with agents in practice.

Fourth, the conceptual papers (Feldt et al., 2026; Treude & Storey, 2025) raise profound questions about the future of software engineering but offer limited concrete guidance for practitioners navigating the transition. The preserve-versus-purify heuristic proposed by Feldt et al. (2026) requires further operationalization.

Finally, evaluation standardization remains incomplete. While multiple papers call for better benchmarks and transparent reporting (Li & Storhaug, 2026; Popescu, 2026; Xiang et al., 2026), the field lacks agreed-upon standards for what constitutes rigorous evaluation of LLM agents in software engineering.

## Per-Paper Annotations

### Becattini et al. (2026)

**Research question**: How can automated assessment of software architecture deliverables be achieved while ensuring technical feedback accuracy and reliability for students?
**Methodology**: CAPRA is a multi-agent LLM system that coordinates multiple specialized agents and employs a Python-based microservice for multi-modal document extraction using PyMuPDF and vision-enabled LLMs (gpt-4o) to parse text and UML diagrams, with deterministic Evidence Anchoring and a ConsistencyManager agent for cross-verification.
**Key findings**:
- CAPRA satisfied 88.8% of evaluated criteria under a strict two-rater aggregation rule in a preliminary evaluation on 10 student reports
- The system achieved moderate inter-rater agreement with human evaluators (kappa = 0.582)
- Each report was processed in slightly over 4 minutes
- Results support viability of LLM-supported architectural feedback while indicating human oversight remains essential
**Limitations**: not stated in abstract

### Feldt et al. (2026)

**Research question**: How should software engineering adapt to the rise of AI-driven agentic systems that expand engineering scope beyond executable code?
**Methodology**: This conceptual paper introduces the Semi-Executable Stack, a six-ring diagnostic reference model, and develops the argument through three worked cases to reframe objections as engineering targets.
**Key findings**:
- The shift in software engineering is toward semi-executable artifacts combining natural language, tools, workflows, and organizational routines
- The Semi-Executable Stack model spans six rings: executable artifacts, instructional artifacts, orchestrated execution, controls, operating logic, and societal/institutional fit
- The model helps locate where contributions, bottlenecks, or organizational transitions primarily sit and their dependencies
- The paper proposes a preserve-versus-purify heuristic for deciding which legacy SE processes should be kept or redesigned
**Limitations**: This is a conceptual keynote companion paper that is diagnostic and agenda-setting rather than empirical

### Kikuta et al. (2025)

**Research question**: How can Large Language Models enable fully automated Chaos Engineering cycles to build resilient software systems at low cost?
**Methodology**: The authors propose ChaosEater, a system that automates the entire Chaos Engineering cycle using LLMs through a predefined agentic workflow with subdivided processes, evaluated through case studies on small- and large-scale Kubernetes systems.
**Key findings**:
- ChaosEater consistently completes reasonable Chaos Engineering cycles with significantly low time and monetary costs
- The system automates the entire CE cycle including requirement definition, code generation, testing, and debugging
- ChaosEater's cycles are qualitatively validated by both human engineers and LLMs
- The approach targets CE for software systems built on Kubernetes
**Limitations**: not stated in abstract

### Li and Storhaug (2026)

**Research question**: How can evaluations of Agentic AI in software engineering be made more reproducible, explainable, and effective?
**Methodology**: The study analyzes 18 papers on Agentic AI in software engineering published or accepted by top SE conferences (ICSE 2026, ICSE 2025, FSE 2025, ASE 2025, ISSTA 2025) to synthesize current evaluation practices and identify their limitations.
**Key findings**:
- Current evaluation practices for Agentic AI in SE have significant limitations in reproducibility and explainability
- Missing information in evaluation design descriptions makes reproduction of results infeasible
- The paper proposes guidelines recommending researchers make Thought-Action-Result (TAR) trajectories and LLM interaction data publicly accessible
- A proof-of-concept case study demonstrates how TAR trajectories can support systematic analysis across different Agentic AI approaches
**Limitations**: not stated in abstract

### Nguyen et al. (2026)

**Research question**: How can LLM-based multi-agent systems improve the automated summarization of software documentation?
**Methodology**: The paper presents Metagente, an LLM-based multi-agent system using a Teacher-Student architecture where multiple LLM agents collaborate to generate summaries, evaluated on real-world datasets against baseline approaches.
**Key findings**:
- Metagente demonstrates effectiveness in streamlining workflows for software document summarization
- The multi-agent approach outperforms considered baseline methods
- The system improves summarization quality for requirements analysis and technical documentation
- LLM-based multi-agent systems show transformative potential in software engineering
**Limitations**: not stated in abstract

### Oliveira et al. (2026)

**Research question**: What are the challenges and capabilities of existing multi-agent system frameworks for software engineering from a developer's perspective?
**Methodology**: The study uses a mixed-method approach: first, a quantitative analysis of open source MAS frameworks evaluating documentation, features, and capabilities; second, a qualitative evaluation implementing a common use case (README.MD summarization) across selected frameworks.
**Key findings**:
- Selected MAS frameworks provide good coverage of fundamental multi-agent system components
- Advanced features such as telemetry of agents are still missing from current frameworks
- No significant difference was found in ROUGE scores across frameworks for the summarization task
- Developers face challenges in selecting appropriate technology, designing coordination rules, and defining agent roles
- The paper provides lessons learned and challenges to help practitioners select suitable MAS frameworks
**Limitations**: not stated in abstract

### Popescu (2026)

**Research question**: How can evaluation techniques for LLM-powered agents be improved to better reflect true model capabilities grounded in real-world software development practice?
**Methodology**: The research proposes a comprehensive evaluation methodology for LLM-powered agents grounded in real-world software development practice, focusing on contamination-awareness, in-the-wild agentic behavior assessment, and trajectory-aware benchmarks and metrics.
**Key findings**:
- Existing evaluation techniques are limited due to their fragmented nature and distorted projection of true model capabilities, often obtained from hypothetical syntactic scenarios
- The proposed approach captures realistic coding contexts, human-aligned behavior, and model failure modes
- The methodology aims to bridge the gap between accelerated agent adoption and adequate evaluation techniques
**Limitations**: not stated in abstract

### Treude and Storey (2025)

**Research question**: How does the integration of Large Language Models and autonomous agents into software engineering disrupt established empirical research paradigms?
**Methodology**: This vision paper examines the paradigm shift caused by LLM integration in software engineering through discussion of transformed phenomena, methods, theories, data modalities, and validity threats in AI-mediated environments.
**Key findings**:
- LLMs and autonomous agents mark an enduring paradigm shift in software engineering
- AI integration transforms the phenomena studied, methods and theories used, and data analyzed in empirical software engineering
- The boundaries between social and technical actors blur as humans and AI agents increasingly co-create
- Reproducibility becomes contingent on model updates and prompt contexts
- Foundational constructs such as 'developer', 'artifact', and 'interaction' are fundamentally reshaped
**Limitations**: not stated in abstract

### Xiang et al. (2026)

**Research question**: How can LLM-powered agents be improved to automate issue resolution in Rust repositories given the language's steep learning curve and strict semantics?
**Methodology**: The authors introduce Rust-SWE-bench, a benchmark of 500 real-world repository-level tasks from 34 Rust repositories, and conduct a comprehensive study evaluating four representative agents and four state-of-the-art LLMs, then propose RUSTFORGER integrating automated test environment setup with Rust metaprogramming-driven dynamic tracing.
**Key findings**:
- ReAct-style agents resolve up to 21.2% of issues but are limited by challenges in comprehending repository-wide code structure and complying with Rust's strict type and trait semantics
- Issue reproduction is critical for task resolution in the Rust ecosystem
- RUSTFORGER using Claude-Sonnet-3.7 resolves 28.6% of tasks on Rust-SWE-bench, representing a 34.9% improvement over the strongest baseline
- RUSTFORGER uniquely solves 46 tasks that no other agent could solve across all adopted advanced LLMs
**Limitations**: not stated in abstract

### Zhou et al. (2026)

**Research question**: Why has practical agent progress increasingly shifted from changing model weights to reorganizing runtime infrastructure through externalization of capabilities?
**Methodology**: This paper reviews the shift toward externalization through the lens of cognitive artifacts, tracing a historical progression from weights to context to harness, and analyzing memory, skills, and protocols as three distinct but coupled forms of externalization within a larger agent system.
**Key findings**:
- LLM agents are increasingly built by reorganizing the runtime around them rather than changing model weights
- Memory externalizes state across time, skills externalize procedural expertise, protocols externalize interaction structure, and harness engineering serves as the unification layer coordinating them into governed execution
- Agent infrastructure matters because it transforms hard cognitive burdens into forms that the model can solve more reliably
- Emerging directions include self-evolving harnesses and shared agent infrastructure, with open challenges in evaluation, governance, and long-term co-evolution of models and external infrastructure
**Limitations**: not stated in abstract

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

Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., Lin, J., et al. (2026). Externalization in LLM agents: A unified review of memory, skills, protocols and harness engineering. arXiv. https://arxiv.org/abs/2604.08224
