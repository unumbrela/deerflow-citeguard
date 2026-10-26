# Systematic Literature Review: LLM Agents for Software Engineering

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "LLM agents software engineering", filtered to category cs.SE, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agents for software engineering reveals a rapidly evolving field focused on three critical dimensions: evaluation methodologies, multi-agent system architectures, and practical applications in software development workflows. Recent research emphasizes the need for reproducible and explainable evaluation frameworks, with multiple papers identifying gaps in current benchmarking practices. Multi-agent systems are emerging as a dominant paradigm, offering improved performance in tasks ranging from code generation to documentation summarization. The field is simultaneously addressing foundational questions about how software engineering itself must adapt to AI-mediated development, proposing new conceptual models and diagnostic frameworks for understanding the expanding scope of engineering artifacts.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM agents software engineering", filtered to category cs.SE, published between 2024-10-26 and 2026-10-26. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation Frameworks and Benchmarking

A significant portion of recent research focuses on establishing rigorous, reproducible evaluation methodologies for LLM agents in software engineering contexts. Li and Storhaug (2026) conducted a systematic analysis of 18 papers from top SE conferences, revealing that current evaluations often lack sufficient detail to enable reproduction. They propose making Thought-Action-Result (TAR) trajectories publicly accessible to support systematic comparisons across approaches. Similarly, Popescu (2026) argues that existing evaluation techniques provide distorted projections of true model capabilities, calling for contamination-aware and trajectory-aware benchmarks that capture realistic coding contexts and human-aligned behavior.

This evaluation focus extends to domain-specific benchmarks. Xiang et al. (2026) introduced Rust-SWE-bench, a repository-level benchmark of 500 real-world Rust issues, demonstrating that language-specific challenges require tailored evaluation approaches. Their work shows that general-purpose agents struggle with Rust's strict type system and trait semantics, highlighting the importance of domain-aware benchmarking.

### Theme 2: Multi-Agent System Architectures

Multi-agent systems are emerging as a preferred architecture for complex software engineering tasks. Oliveira et al. (2026) conducted a mixed-method evaluation of open-source multi-agent frameworks, finding that while fundamental components are well-covered, advanced features like agent telemetry remain underdeveloped. Their empirical comparison across frameworks revealed no significant differences in output quality for summarization tasks, suggesting that framework selection should prioritize developer experience over performance metrics.

The Teacher-Student architecture represents one promising multi-agent pattern. Nguyen et al. (2026) demonstrated that Metagente, a system employing collaborating LLM agents in a Teacher-Student configuration, outperforms baseline approaches in software documentation summarization. The collaborative architecture enhances both relevance and precision of generated summaries, particularly for requirements analysis and technical documentation.

CAPRA (Becattini et al., 2026) exemplifies another multi-agent approach, coordinating specialized agents to provide automated feedback on software architecture deliverables. The system achieved 88.8% satisfaction of evaluation criteria under strict aggregation rules, demonstrating that multi-agent coordination can scale expert feedback in educational contexts.

### Theme 3: Externalization and Cognitive Infrastructure

A conceptual thread running through recent work examines how LLM agent capabilities are increasingly externalized into infrastructure rather than embedded in model weights. Zhou et al. (2026) present a unified review arguing that memory externalizes state across time, skills externalize procedural expertise, protocols externalize interaction structure, and harness engineering coordinates these elements into governed execution. Their analysis suggests that practical agent progress increasingly depends on better external cognitive infrastructure, not only stronger models.

This externalization perspective reframes how we understand agent capabilities, positioning infrastructure design as a first-class research concern rather than an implementation detail.

### Theme 4: Expanding Scope of Software Engineering

The integration of LLM agents is fundamentally expanding what constitutes software engineering work. Feldt et al. (2026) propose the Semi-Executable Stack, a six-ring diagnostic model for reasoning about how engineering artifacts extend beyond executable code to include natural language, tools, workflows, control mechanisms, and organizational routines. Their framework helps locate where contributions, bottlenecks, or organizational transitions primarily sit and their dependencies.

Treude and Storey (2025) argue this represents a paradigm shift for empirical software engineering research itself. They examine how foundational constructs such as "developer," "artifact," and "interaction" are being reshaped as humans and AI agents co-create, blurring boundaries between social and technical actors. Reproducibility becomes contingent on model updates and prompt contexts, requiring new validity frameworks for AI-mediated research environments.

### Theme 5: Practical Applications and Automation

Beyond conceptual frameworks, researchers are demonstrating concrete applications of LLM agents in software engineering workflows. Kikuta et al. (2025) developed ChaosEater, a system that fully automates the chaos engineering cycle using LLMs through predefined agentic workflows. Their case studies on Kubernetes systems show that automated chaos engineering can be completed with significantly low time and monetary costs, enabling broader adoption of resilience testing practices.

These practical demonstrations validate the feasibility of agent-driven automation across diverse software engineering tasks, from testing to documentation to architectural review.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the need for more rigorous, reproducible evaluation methodologies (Li & Storhaug, 2026; Popescu, 2026; Xiang et al., 2026). There is broad agreement that multi-agent architectures outperform single-agent approaches for complex tasks (Nguyen et al., 2026; Becattini et al., 2026; Oliveira et al., 2026). The literature also converges on the view that LLM agents are fundamentally expanding the scope of software engineering work beyond traditional code-centric activities (Feldt et al., 2026; Treude & Storey, 2025).

**Disagreements**: While Oliveira et al. (2026) found no significant performance differences across multi-agent frameworks for summarization tasks, Nguyen et al. (2026) demonstrated clear superiority of their Metagente architecture over baselines, suggesting that architectural choices may matter more for some tasks than others. Additionally, there is tension between papers emphasizing infrastructure externalization (Zhou et al., 2026) and those focusing on model-specific improvements (Xiang et al., 2026), reflecting different perspectives on where innovation should be directed.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, multiple papers note limitations in their empirical scope, with evaluations often restricted to single use cases or specific programming languages (Oliveira et al., 2026; Xiang et al., 2026), suggesting a need for broader cross-domain validation. Second, the conceptual papers (Feldt et al., 2026; Zhou et al., 2026) lack quantitative validation, pointing to a gap between theoretical frameworks and empirical evidence. Third, several papers note that advanced features like agent telemetry remain underdeveloped (Oliveira et al., 2026), indicating infrastructure gaps that limit production deployment.

A critical open question concerns how to balance automation with human oversight. While CAPRA achieved high automated assessment accuracy, Becattini et al. (2026) emphasize that human oversight remains essential for subjective dimensions. The literature has not yet established clear guidelines for determining which tasks can be fully automated versus which require human-in-the-loop approaches.

Finally, the paradigm shift described by Treude and Storey (2025) raises fundamental questions about research validity in AI-mediated environments that the field has only begun to address.

## Per-Paper Annotations

### Becattini et al. (2026)

**Research question**: How can automated assessment of software architecture deliverables be achieved with accurate, reliable technical feedback for students?
**Methodology**: The authors present CAPRA, a multi-agent LLM system that coordinates specialized agents and employs a Python-based microservice for multi-modal document extraction using PyMuPDF and vision-enabled LLMs to parse text and UML diagrams.
**Key findings**:
- CAPRA satisfied 88.8% of evaluated criteria under a strict two-rater aggregation rule
- The system achieved moderate inter-rater agreement with human evaluators (kappa = 0.582)
- Each report was processed in slightly over 4 minutes
- Human oversight remains essential for subjective assessment dimensions
**Limitations**: not stated in abstract

### Feldt et al. (2026)

**Research question**: How should software engineering adapt to the rise of AI-based systems and agentic harnesses that expand engineering beyond executable code?
**Methodology**: This conceptual paper introduces the Semi-Executable Stack, a six-ring diagnostic reference model for reasoning about the expansion of software engineering artifacts, developed through three worked cases and a preserve-versus-purify heuristic.
**Key findings**:
- The shift in software engineering is toward expanding beyond executable code to semi-executable artifacts
- Semi-executable artifacts include combinations of natural language, tools, workflows, control mechanisms, and organizational routines
- The six-ring model spans executable artifacts, instructional artifacts, orchestrated execution, controls, operating logic, and societal/institutional fit
- The model helps locate where contributions, bottlenecks, or organizational transitions primarily sit and their dependencies
**Limitations**: This is a conceptual keynote paper that is diagnostic and agenda-setting rather than empirical, lacking quantitative validation of the proposed model.

### Kikuta et al. (2025)

**Research question**: How can Large Language Models be leveraged to fully automate the chaos engineering cycle to enable anyone to build resilient software systems at low cost?
**Methodology**: The authors propose ChaosEater, a system that automates the entire chaos engineering cycle using LLMs through a predefined agentic workflow with subdivided processes assigned to LLMs, evaluated through case studies on Kubernetes systems.
**Key findings**:
- ChaosEater consistently completes reasonable chaos engineering cycles with significantly low time and monetary costs
- The system targets chaos engineering for software systems built on Kubernetes
- LLMs in ChaosEater complete CE cycles through software engineering tasks including requirement definition, code generation, testing, and debugging
- The cycles are qualitatively validated by both human engineers and LLMs
**Limitations**: not stated in abstract

### Li and Storhaug (2026)

**Research question**: How can evaluations of Agentic AI in software engineering be made more reproducible, explainable, and effective?
**Methodology**: The study analyzes 18 papers on Agentic AI in software engineering published or accepted at top SE conferences to identify prevailing evaluation approaches and their limitations, proposing guidelines demonstrated through a proof-of-concept case study using TAR trajectories.
**Key findings**:
- Current Agentic AI evaluations often lack sufficient information in evaluation design descriptions, making reproduction of results infeasible
- LLMs underlying Agentic AI systems function as black boxes, making it difficult to justify superiority over baselines
- Making TAR trajectories and LLM interaction data publicly accessible enables more effective analysis of different Agentic AI approaches
- A proof-of-concept case study demonstrates that TAR trajectories can support systematic comparisons across approaches
**Limitations**: The study focuses on papers from five specific SE conferences in 2025-2026, which may not represent all Agentic AI evaluation practices in the broader research community.

### Nguyen et al. (2026)

**Research question**: Can an LLM-based multi-agent system improve the quality of automated summarization for software documentation?
**Methodology**: The paper presents Metagente, an LLM-based multi-agent system using a Teacher-Student architecture where multiple LLM agents collaborate to generate summaries, empirically evaluated on real-world datasets.
**Key findings**:
- Metagente effectively generates concise and accurate summaries of software documentation
- The Teacher-Student architecture with collaborating LLM agents enhances relevance and precision of produced summaries
- Metagente outperforms baseline approaches in summarization tasks
- The system improves summarization specifically for requirements analysis and technical documentation
**Limitations**: not stated in abstract

### Oliveira et al. (2026)

**Research question**: What are the capabilities, challenges, and differences among existing open-source frameworks for implementing multi-agent systems in software engineering?
**Methodology**: The paper uses a mixed-method approach combining quantitative analysis of open-source multi-agent system frameworks with qualitative evaluation by implementing a common use case (README.MD summarization) across selected frameworks.
**Key findings**:
- Selected multi-agent system frameworks provide good coverage of fundamental MAS components
- Advanced features such as telemetry of agents are still missing from current frameworks
- There is no significant difference in ROUGE scores among frameworks for the summarization task
- Developers face challenges in selecting appropriate technology, devising coordination rules, and designing specific agent roles
**Limitations**: The empirical evaluation focuses on a single use case (README.MD summarization), which may not generalize to other multi-agent system applications in software engineering.

### Popescu (2026)

**Research question**: How can evaluation techniques for LLM-powered software engineering agents be improved to better reflect true model capabilities in real-world development practice?
**Methodology**: The research proposes a comprehensive evaluation methodology grounded in real-world software development practice, focusing on contamination-awareness, in-the-wild agentic behavior assessment, and trajectory-aware benchmarks and metrics.
**Key findings**:
- Existing evaluation techniques are limited by fragmented nature and distorted projection of true model capabilities
- Current evaluations often rely on hypothetical syntactic scenarios rather than real-world practice
- The proposed approach emphasizes contamination-awareness and trajectory-aware benchmarks
- Evaluation should capture realistic coding contexts and human-aligned behavior
**Limitations**: not stated in abstract

### Treude and Storey (2025)

**Research question**: How does the integration of Large Language Models and autonomous agents into software engineering disrupt established empirical research paradigms?
**Methodology**: This vision paper examines the impact of LLM integration on software engineering research by discussing how it transforms research phenomena, methods, theories, data analysis, and validity threats in AI-mediated environments.
**Key findings**:
- The adoption of LLMs and autonomous agents marks an enduring paradigm shift in software engineering
- Traditional empirical methods remain central but AI introduces new data modalities and alters causal assumptions
- Foundational constructs such as 'developer', 'artifact', and 'interaction' are fundamentally reshaped
- As humans and AI agents co-create, boundaries between social and technical actors blur
- Reproducibility becomes contingent on model updates and prompt contexts
**Limitations**: not stated in abstract

### Xiang et al. (2026)

**Research question**: How can LLM-based agents be improved to resolve real-world Rust repository issues given the language's steep learning curve and strict semantics?
**Methodology**: The authors introduce Rust-SWE-bench, a benchmark of 500 real-world repository-level tasks from 34 Rust repositories, and conduct a comprehensive study evaluating four representative agents and four state-of-the-art LLMs, proposing RUSTFORGER as a novel agentic approach.
**Key findings**:
- ReAct-style agents resolve up to 21.2% of Rust issues but struggle with repository-wide code structure comprehension and Rust's strict type/trait semantics
- Issue reproduction is critical for successful task resolution
- RUSTFORGER using Claude-Sonnet-3.7 resolves 28.6% of tasks, a 34.9% improvement over the strongest baseline
- RUSTFORGER uniquely solves 46 tasks that no other agent could solve across all adopted advanced LLMs
**Limitations**: not stated in abstract

### Zhou et al. (2026)

**Research question**: How does externalization of capabilities into memory, skills, protocols, and harness engineering transform LLM agent infrastructure and performance?
**Methodology**: The paper presents a unified review through the lens of externalization, drawing on cognitive artifacts theory to analyze how agent infrastructure transforms cognitive burdens into more reliably solvable forms, tracing historical progression from weights to context to harness.
**Key findings**:
- LLM agent capabilities are increasingly externalized into memory stores, reusable skills, interaction protocols, and harness engineering rather than changing model weights
- Memory externalizes state across time, skills externalize procedural expertise, protocols externalize interaction structure, and harness engineering coordinates them into governed execution
- Agent infrastructure matters because it transforms hard cognitive burdens into forms the model can solve more reliably
- Practical agent progress increasingly depends on better external cognitive infrastructure, not only stronger models
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
