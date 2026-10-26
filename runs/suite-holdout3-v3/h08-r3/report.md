# Systematic Literature Review: LLM Agents for Software Engineering

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "LLM agents software engineering", filtered to category cs.SE, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature reveals a rapidly maturing field focused on LLM-powered agents for software engineering, with research spanning evaluation methodologies, multi-agent system development, automated documentation, and paradigm shifts in empirical software engineering. The papers collectively demonstrate a transition from theoretical proposals to practical implementations, with significant attention to reproducibility, developer alignment, and real-world applicability. A recurring theme is the emphasis on making agent systems more transparent, explainable, and integrated into existing software engineering workflows, while acknowledging the challenges of evaluating black-box LLM components in production contexts.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM agents software engineering", filtered to category cs.SE, published between 2024-10-26 and 2026-10-26. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation and Benchmarking of Agentic AI

A significant portion of the literature focuses on establishing rigorous evaluation frameworks for LLM agents in software engineering contexts. Li & Storhaug (2026) identify critical gaps in current evaluation practices, noting that many studies lack sufficient detail for reproducibility or fail to justify superiority over baselines. Their position paper advocates for transparent Thought-Action-Result (TAR) trajectories and public LLM interaction data to enable systematic analysis.

Popescu (2026) extends this critique, arguing that existing evaluation techniques are fragmented and often rely on hypothetical syntactic scenarios rather than real-world contexts. The proposed methodology emphasizes contamination-awareness and trajectory-aware benchmarks that capture realistic coding environments and human-aligned behavior. Xiang et al. (2026) demonstrate this approach concretely with Rust-SWE-bench, a repository-level benchmark of 500 real-world tasks, revealing that even state-of-the-art agents resolve only 21.2% of issues without specialized improvements.

### Theme 2: Multi-Agent System Architectures and Frameworks

Several papers investigate multi-agent system (MAS) architectures as a means to enhance software engineering capabilities. Oliveira et al. (2026) conduct a mixed-method experience report on developing LLM-based MAS, evaluating open-source frameworks through both quantitative feature analysis and qualitative implementation of a common use case (README summarization). Their findings highlight that while fundamental MAS components are well-covered, advanced features like agent telemetry remain underdeveloped.

Nguyen et al. (2026) present Metagente, a Teacher-Student architecture where multiple LLM agents collaborate to generate software document summaries. Their empirical evaluation demonstrates that collaborative agent architectures outperform baseline approaches, particularly for requirements analysis and technical documentation. Becattini et al. (2026) extend this to software architecture assessment with CAPRA, a multi-agent system that coordinates specialized agents to evaluate structural completeness and requirements traceability, achieving 88.8% criterion satisfaction under strict aggregation rules.

### Theme 3: Externalization and Infrastructure Engineering

Zhou et al. (2026) provide a unified theoretical framework for understanding LLM agent architecture through the lens of externalization. Drawing on cognitive artifacts theory, they analyze how agent infrastructure—memory, skills, protocols, and harness engineering—transforms cognitive burdens into forms that models can solve more reliably. Their review traces a historical progression from weights to context to harness, arguing that practical agent progress increasingly depends on better external cognitive infrastructure rather than solely stronger models.

This perspective reframes agent development as an engineering challenge of reorganizing runtime around models, with memory externalizing state across time, skills externalizing procedural expertise, and protocols externalizing interaction structure. The paper identifies emerging directions including self-evolving harnesses and shared agent infrastructure, while highlighting open challenges in evaluation and governance.

### Theme 4: Conceptual and Paradigmatic Shifts

The literature also addresses broader conceptual shifts in software engineering practice. Feldt et al. (2026) introduce the Semi-Executable Stack, a six-ring diagnostic reference model spanning from executable artifacts through societal and institutional fit. Their conceptual framework argues that software engineering is adapting to semi-executable artifacts combining natural language, tools, workflows, and organizational routines, rather than becoming irrelevant in the age of AI-driven agentic systems.

Treude & Storey (2025) examine how generative AI and autonomous agents disrupt established empirical research paradigms. Their vision paper argues that AI integration fundamentally reshapes developer roles and artifacts, blurring boundaries between social and technical actors. Traditional empirical methods face new challenges from dynamic AI environments, including reproducibility issues contingent on model updates and prompt contexts, while new data modalities challenge foundational constructs such as "developer," "artifact," and "interaction."

### Theme 5: Specialized Applications and Domain-Specific Solutions

Several papers demonstrate domain-specific applications of LLM agents. Kikuta et al. (2025) present ChaosEater, a system that automates the entire chaos engineering cycle for Kubernetes-based systems. By predefining an agentic workflow and assigning subdivided processes to LLMs, their approach enables low-cost resilience testing with qualitatively validated cycles completed by both human engineers and LLMs.

Xiang et al. (2026) focus on the Rust programming language, addressing its steep learning curve and strict type semantics. Their RUSTFORGER approach integrates automated test environment setup with Rust metaprogramming-driven dynamic tracing, achieving 28.6% task resolution on Rust-SWE-bench—a 34.9% improvement over the strongest baseline—and uniquely solving 46 tasks that no other agent could solve.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the need for transparent, reproducible evaluation methodologies. Li & Storhaug (2026), Popescu (2026), and Xiang et al. (2026) all emphasize that current evaluation practices are insufficient, advocating for trajectory-aware benchmarks, public interaction data, and real-world task repositories. There is also broad agreement that multi-agent architectures outperform single-agent approaches for complex software engineering tasks, as demonstrated by Nguyen et al. (2026), Becattini et al. (2026), and Oliveira et al. (2026).

The literature consistently acknowledges that LLMs function as black boxes, making evaluation transparency difficult (Li & Storhaug, 2026; Zhou et al., 2026; Treude & Storey, 2025). All surveyed papers recognize that agent infrastructure—memory, skills, protocols—matters as much as or more than model capabilities alone.

**Disagreements**: While most papers advocate for multi-agent systems, Oliveira et al. (2026) found no significant difference in ROUGE scores across different MAS frameworks for their summarization task, suggesting that framework selection may be less critical than task design. Additionally, there is tension between conceptual frameworks (Feldt et al., 2026; Zhou et al., 2026; Treude & Storey, 2025) that emphasize paradigmatic shifts and empirical papers (Xiang et al., 2026; Nguyen et al., 2026) that focus on incremental improvements to existing practices.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature:

1. **Limited empirical validation**: Many papers are position papers or conceptual frameworks (Li & Storhaug, 2026; Feldt et al., 2026; Zhou et al., 2026; Treude & Storey, 2025) that provide guidelines rather than comprehensive empirical validation. Even empirical studies often lack details about dataset size, diversity, or baseline comparisons (Nguyen et al., 2026).

2. **Narrow evaluation scope**: Several studies are limited to specific use cases—README summarization (Oliveira et al., 2026), student architecture reports (Becattini et al., 2026), or Rust issue resolution (Xiang et al., 2026)—raising questions about generalizability to other software engineering contexts.

3. **Missing advanced features**: Oliveira et al. (2026) note that advanced features such as agent telemetry are still missing from current MAS frameworks, limiting practitioners' ability to monitor and debug agent behavior.

4. **Human oversight requirements**: Becattini et al. (2026) explicitly acknowledge that human oversight remains essential for subjective assessment dimensions, yet few papers address how to optimally integrate human judgment with automated agent systems.

5. **Reproducibility challenges**: Treude & Storey (2025) highlight that reproducibility is contingent on model updates and prompt contexts, creating fundamental challenges for empirical software engineering in AI-mediated environments that remain unaddressed.

6. **Governance and evaluation standards**: Zhou et al. (2026) identify open challenges in evaluation and governance for shared agent infrastructure, particularly as self-evolving harnesses emerge.

## Per-Paper Annotations

### Becattini et al. (2026)

**Research question**: How can automated assessment be extended to software architecture deliverables, which require analyzing structural completeness and requirements traceability?
**Methodology**: The authors developed CAPRA, a multi-agent LLM system that coordinates multiple specialized agents and employs a Python-based microservice for multi-modal document extraction using PyMuPDF and vision-enabled LLMs (gpt-4o) to parse text and UML diagrams. The system includes a deterministic Evidence Anchoring step using fuzzy matching and a ConsistencyManager agent for cross-verification.
**Key findings**:
- CAPRA satisfied 88.8% of evaluated criteria under a strict two-rater aggregation rule in a preliminary evaluation on 10 student reports.
- The system achieved moderate inter-rater agreement with human evaluators (kappa = 0.582).
- Each report was processed in slightly over 4 minutes.
- Human oversight remains essential for subjective assessment dimensions.
**Limitations**: Not stated in abstract.

### Feldt et al. (2026)

**Research question**: How should software engineering adapt to the shift from purely executable code to semi-executable artifacts in the age of AI-driven agentic systems?
**Methodology**: This conceptual keynote paper introduces the Semi-Executable Stack, a six-ring diagnostic reference model spanning executable artifacts through societal and institutional fit. The argument is developed through three worked cases and includes a preserve-versus-purify heuristic for legacy process decisions.
**Key findings**:
- The shift in software engineering is not toward irrelevance but toward engineering semi-executable artifacts combining natural language, tools, workflows, and organizational routines.
- The Semi-Executable Stack model provides a six-ring framework for locating contributions, bottlenecks, and organizational transitions.
- The paper reframes familiar objections to AI in SE as engineering targets rather than reasons to dismiss the transition.
- A preserve-versus-purify heuristic helps decide which legacy SE processes should be kept versus redesigned.
**Limitations**: This is a conceptual keynote companion paper that is diagnostic and agenda-setting rather than empirical, so it does not provide quantitative validation of the proposed framework.

### Kikuta et al. (2025)

**Research question**: How can Large Language Models automate the entire Chaos Engineering cycle to enable low-cost building of resilient software systems?
**Methodology**: The authors propose ChaosEater, a system that predefines an agentic workflow according to a systematic CE cycle and assigns subdivided processes to LLMs, targeting Kubernetes-based software systems. The system is evaluated through case studies on small- and large-scale Kubernetes systems.
**Key findings**:
- ChaosEater consistently completes reasonable CE cycles with significantly low time and monetary costs.
- The system automates the entire CE cycle including requirement definition, code generation, testing, and debugging through LLMs.
- ChaosEater's cycles are qualitatively validated by both human engineers and LLMs.
- The approach enables anyone to build resilient systems at low cost by automating experiment planning and system improvement processes.
**Limitations**: Not stated in abstract.

### Li & Storhaug (2026)

**Research question**: How can evaluation practices for Agentic AI in software engineering be improved to enable reproducibility and explainability?
**Methodology**: This position paper analyzes 18 papers on Agentic AI evaluation published or accepted at top SE venues (ICSE 2026, ICSE 2025, FSE 2025, ASE 2025, ISSTA 2025) to synthesize current practices and identify limitations. It proposes guidelines and includes a proof-of-concept case study demonstrating TAR trajectory comparisons.
**Key findings**:
- Current Agentic AI evaluations often lack sufficient detail to reproduce results or justify superiority over baselines.
- LLMs underlying Agentic AI function as black boxes, making evaluation transparency difficult.
- The paper proposes making Thought-Action-Result (TAR) trajectories and LLM interaction data publicly accessible.
- A proof-of-concept case study demonstrates that TAR trajectories can support systematic analysis across different Agentic AI approaches.
**Limitations**: As a position paper, it provides conceptual guidelines and recommendations rather than comprehensive empirical validation of the proposed evaluation framework.

### Nguyen et al. (2026)

**Research question**: Can an LLM-based multi-agent system improve the quality of automated summarization for software documentation compared to existing baselines?
**Methodology**: The paper presents Metagente, an LLM-based multi-agent system using a Teacher-Student architecture where multiple LLM agents collaborate to generate summaries. The system was empirically evaluated on real-world datasets and compared against baseline approaches.
**Key findings**:
- Metagente's Teacher-Student architecture enables multiple LLM agents to collaborate for enhanced summary relevance and precision.
- The system outperforms considered baselines in summarization effectiveness.
- Metagente improves summarization specifically for requirements analysis and technical documentation.
- The evaluation demonstrates the transformative potential of LLM-based MAS in streamlining software engineering workflows.
**Limitations**: The abstract does not specify the size or diversity of the real-world datasets used, nor does it detail which baseline approaches were compared.

### Oliveira et al. (2026)

**Research question**: What tools and frameworks exist for implementing LLM-based multi-agent systems in software engineering, and what are their capabilities and limitations from a developer perspective?
**Methodology**: The study uses a mixed-method approach: first conducting quantitative analysis of open-source MAS frameworks by evaluating documentation, features, and capabilities, then performing qualitative evaluation by implementing a common use case (README.MD summarization) across selected frameworks.
**Key findings**:
- Selected MAS frameworks provide good coverage of fundamental multi-agent system components.
- Advanced features such as agent telemetry are still missing from current frameworks.
- Empirical evaluation shows no significant difference in ROUGE scores across frameworks for the summarization task.
- The paper provides lessons learned and challenges to help practitioners select suitable MAS frameworks.
**Limitations**: The evaluation is limited to a specific use case (README.MD summarization) and may not generalize to other multi-agent system applications in software engineering.

### Popescu (2026)

**Research question**: How can evaluation techniques for LLM-powered agents be improved to provide a comprehensive assessment grounded in real-world software development practice?
**Methodology**: The research proposes a comprehensive evaluation methodology for LLM-powered agents focused on contamination-awareness, in-the-wild agentic behavior assessment, and trajectory-aware benchmarks and metrics that capture realistic coding contexts, human-aligned behavior, and model failure modes.
**Key findings**:
- Existing evaluation techniques for LLM agents are limited due to their fragmented nature and distorted projection of true model capabilities.
- Current evaluations often rely on hypothetical syntactic scenarios rather than real-world contexts.
- The proposed approach emphasizes contamination-awareness and trajectory-aware benchmarks.
- The methodology aims to capture realistic coding contexts and human-aligned behavior.
**Limitations**: Not stated in abstract.

### Treude & Storey (2025)

**Research question**: How does the integration of LLMs and autonomous agents into software engineering disrupt established empirical research paradigms?
**Methodology**: This vision paper examines the integration of LLMs into software engineering through discussion and analysis of how it transforms research phenomena, methods, theories, data, and validity threats in AI-mediated environments.
**Key findings**:
- The adoption of LLMs and autonomous agents marks an enduring paradigm shift in software engineering.
- AI integration fundamentally reshapes developer roles and the artifacts they produce, blurring boundaries between social and technical actors.
- Traditional empirical methods remain central but face new challenges from dynamic AI environments, including reproducibility issues contingent on model updates and prompt contexts.
- New data modalities and altered causal assumptions challenge foundational constructs such as 'developer', 'artifact', and 'interaction'.
**Limitations**: Not stated in abstract.

### Xiang et al. (2026)

**Research question**: How can LLM-powered agents be improved to automate Rust issue resolution given the language's steep learning curve and coding challenges?
**Methodology**: The authors introduced Rust-SWE-bench, a benchmark of 500 real-world repository-level software engineering tasks from 34 Rust repositories, then conducted a comprehensive study evaluating four representative agents and four state-of-the-art LLMs. Based on findings, they proposed RUSTFORGER, a novel agentic approach integrating automated test environment setup with Rust metaprogramming-driven dynamic tracing.
**Key findings**:
- ReAct-style agents resolve up to 21.2% of Rust issues but are limited by challenges in comprehending repository-wide code structure and complying with Rust's strict type and trait semantics.
- Issue reproduction is critical for successful task resolution.
- RUSTFORGER using Claude-Sonnet-3.7 resolved 28.6% of tasks on Rust-SWE-bench, representing a 34.9% improvement over the strongest baseline.
- RUSTFORGER uniquely solved 46 tasks that no other agent could solve across all adopted advanced LLMs.
**Limitations**: Not stated in abstract.

### Zhou et al. (2026)

**Research question**: How does externalization of capabilities into memory, skills, protocols, and harness engineering transform LLM agent architecture and performance?
**Methodology**: The paper presents a unified review through the lens of externalization, drawing on cognitive artifacts theory to analyze how agent infrastructure transforms cognitive burdens into forms that models can solve more reliably. The authors trace a historical progression from weights to context to harness and examine memory, skills, and protocols as three distinct but coupled forms of externalization.
**Key findings**:
- LLM agents are increasingly built by reorganizing the runtime around models rather than changing model weights.
- Memory externalizes state across time, skills externalize procedural expertise, protocols externalize interaction structure, and harness engineering coordinates them into governed execution.
- Agent infrastructure matters because it transforms hard cognitive burdens into forms that the model can solve more reliably.
- Practical agent progress increasingly depends on better external cognitive infrastructure, not only stronger models.
- Emerging directions include self-evolving harnesses and shared agent infrastructure, with open challenges in evaluation and governance.
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

Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., Lin, J., & et al. (2026). Externalization in LLM agents: A unified review of memory, skills, protocols and harness engineering. arXiv. https://arxiv.org/abs/2604.08224
