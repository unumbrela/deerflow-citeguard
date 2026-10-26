# Systematic Literature Review: Code Generation with LLM-based Agents

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "code generation LLM agents", category cs.SE, published between 2023-07-31 and 2025-07-31
**Citation format**: APA 7th edition

## Executive Summary

The literature on code generation with LLM-based agents reveals a rapidly evolving field transitioning from single-agent approaches toward sophisticated multi-agent frameworks. The surveyed papers collectively demonstrate that multi-agent collaboration significantly improves code quality, security, and scalability compared to baseline LLM approaches. Key advances include self-reflective architectures, specialized agent roles for different development tasks, and novel evaluation benchmarks addressing communication competence and project-level code generation. The field shows increasing attention to practical engineering challenges including vulnerability reduction, documentation generation, and repository-level code synthesis.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "code generation LLM agents", filtered to category cs.SE, published between 2023-07-31 and 2025-07-31. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Agent Architectures for Code Generation

The surveyed literature overwhelmingly favors multi-agent frameworks over single-agent approaches. Five papers explicitly propose multi-agent systems with specialized roles: AutoSafeCoder employs three agents (Coding, Static Analyzer, and Fuzzing) working iteratively to secure code generation (Nunez et al., 2024). DocAgent introduces five specialized agents (Reader, Searcher, Writer, Verifier, and Orchestrator) for documentation generation (Yang et al., 2025). CodeCoR implements a four-agent framework where agents generate prompts, code, test cases, and repair advice respectively (Pan et al., 2025). Self-Organized Agents (SoA) enables automatic agent multiplication based on problem complexity for dynamic scalability (Ishibashi & Nishimura, 2024). GraphCodeAgent uses an LLM-powered agent guided by dual graphs for retrieval-augmented code generation (Li et al., 2025).

This architectural pattern reflects a fundamental shift from monolithic LLM code generation toward distributed, collaborative approaches where each agent handles a constant amount of context while the overall system scales indefinitely with agent count.

### Theme 2: Security and Quality Assurance in Generated Code

Security emerges as a critical concern in LLM code generation, with multiple papers addressing vulnerability detection and reduction. AutoSafeCoder achieved a 13% reduction in code vulnerabilities by integrating static analysis and mutation-based fuzzing during the generation process (Nunez et al., 2024). The framework demonstrates that security improvements can be achieved without compromising code functionality through continuous collaboration between specialized agents.

GraphCodeAgent addresses a different quality dimension by bridging the gap between natural language requirements and programming implementations through dual graph-guided retrieval (Li et al., 2025). The approach enables retrieval of both implicit and explicit code snippets not directly expressed in requirements, significantly outperforming state-of-the-art baselines on repo-level code generation.

### Theme 3: Benchmarking and Evaluation Frameworks

The literature shows increasing sophistication in evaluation methodologies. HumanEvalComm introduces a new benchmark modified from existing problems with three types of issues (inconsistency, ambiguity, incompleteness) and defines new metrics: Communication Rate and Good Question Rate (Wu & Fard, 2024). This benchmark addresses whether LLMs can demonstrate communication competence by asking clarifying questions when problem descriptions contain issues.

ProjectEval provides automated evaluation on project-level code generation from a user's perspective with explainable results (Liu et al., 2025). The benchmark simulates user interaction for evaluating generated projects through execution and code similarity using existing objective indicators. A multi-agent evaluation framework compares performance across seven different LLMs using the HumanEval benchmark (Rasheed et al., 2024).

### Theme 4: Feedback Loops and Iterative Refinement

Several papers employ iterative refinement mechanisms to improve code quality. CodeCoR implements a self-reflective process where generated code is tested locally, with failing code sent to a repair agent for iterative refinement before returning the code that passes the most test cases (Pan et al., 2025). The framework achieves an average Pass@1 score of 77.13% across four datasets.

Infrastructure as Code generation research investigates a feedback loop that returns errors and warnings to allow iterative code improvement (Palavalli & Santolucito, 2024). However, the effectiveness of the feedback loop decreases exponentially with each iteration and eventually plateaus, revealing a limitation of this approach.

### Theme 5: Survey and Synthesis of the Field

The most recent paper in this review provides a comprehensive survey tracing the developmental trajectory of LLM-based code generation agents (Dong et al., 2025). The survey categorizes core techniques into single-agent and multi-agent architectures and documents applications across the full software development lifecycle. Key findings indicate that the field has evolved from algorithmic innovation toward practical engineering challenges like system reliability and tool integration.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the superiority of multi-agent approaches over single-agent baselines. AutoSafeCoder, DocAgent, CodeCoR, SoA, and GraphCodeAgent all demonstrate performance improvements through specialized agent collaboration. The surveyed papers also agree on the importance of iterative refinement processes and the need for comprehensive evaluation frameworks beyond simple code snippet generation.

**Disagreements**: The literature shows different approaches to scaling. Self-Organized Agents proposes automatic agent multiplication for dynamic scalability (Ishibashi & Nishimura, 2024), while other frameworks maintain fixed agent counts with specialized roles. The effectiveness of feedback loops also shows disagreement: while CodeCoR's iterative refinement achieves strong results (Pan et al., 2025), infrastructure as code research finds feedback loop effectiveness diminishes exponentially until plateauing (Palavalli & Santolucito, 2024).

## Gaps and Open Questions

The collective literature reveals several gaps. First, most papers do not explicitly state limitations regarding computational overhead, scalability to very large codebases, or domain-specific constraints. Second, coordination overhead and communication costs between agents remain underexplored despite being critical for multi-agent systems. Third, the surveyed papers focus primarily on English-language code generation with limited attention to multilingual or cross-cultural programming contexts. Finally, practitioner feedback and real-world deployment studies are largely absent, with most evaluations conducted on benchmark datasets rather than production environments.

## Per-Paper Annotations

### Ishibashi & Nishimura (2024)

**Research question**: How can multi-agent frameworks overcome context length constraints to enable scalable generation and optimization of large-scale codebases?
**Methodology**: The authors propose Self-Organized multi-Agent framework (SoA), where agents operate independently to generate and modify code components while collaborating to construct the overall codebase, with automatic agent multiplication based on problem complexity for dynamic scalability.
**Key findings**:
- SoA enables automatic multiplication of agents based on problem complexity for dynamic scalability
- Each agent manages a constant amount of code while overall code volume increases indefinitely with agent count
- SoA surpasses single-agent baseline by 5% in Pass@1 accuracy on HumanEval benchmark
- Agents in SoA handle significantly less code individually compared to single-agent systems
**Limitations**: The abstract does not specify limitations regarding coordination overhead, communication costs between agents, or constraints on agent interaction complexity.

### Li et al. (2025)

**Research question**: How can retrieval-augmented code generation approaches bridge the gap between natural language requirements and programming implementations in repository-level code generation?
**Methodology**: The authors propose GraphCodeAgent, which constructs two interconnected graphs: a Requirement Graph modeling requirement relations of code snippets, and a Structural-Semantic Code Graph capturing repository code dependencies. An LLM-powered agent performs multi-hop reasoning guided by these graphs to systematically retrieve relevant context code snippets.
**Key findings**:
- GraphCodeAgent significantly outperforms state-of-the-art baselines on repo-level code generation
- The dual graph approach enables retrieval of both implicit and explicit code snippets not directly expressed in requirements
- The approach was evaluated on three advanced LLMs using DevEval and CoderEval benchmarks
- Multi-hop reasoning systematically retrieves all relevant context code snippets
**Limitations**: Not stated in abstract.

### Liu et al. (2025)

**Research question**: How can LLM agents' project-level code generation capabilities be automatically evaluated from a user's perspective with explainable results?
**Methodology**: The authors introduce ProjectEval, a benchmark constructed by LLM with human reviewing that simulates user interaction for evaluating generated projects through execution and code similarity using existing objective indicators, with three different levels of natural language or code skeleton inputs.
**Key findings**:
- Systematic engineering project code is key for LLM agents to achieve practical projects
- Overall understanding of the project is crucial for successful code generation
- Comprehensive analysis capability is essential for LLM agents in real-world production
- The benchmark enables automated evaluation through user interaction simulation
**Limitations**: Not stated in abstract.

### Nunez et al. (2024)

**Research question**: How can multi-agent frameworks improve the security of LLM-generated code by integrating static and dynamic testing during code generation?
**Methodology**: The authors propose AutoSafeCoder, a multi-agent framework with three agents (Coding Agent, Static Analyzer Agent, and Fuzzing Agent) that collaborate iteratively during code generation. The framework was evaluated using the SecurityEval dataset to measure vulnerability reduction compared to baseline LLMs.
**Key findings**:
- AutoSafeCoder achieved a 13% reduction in code vulnerabilities compared to baseline LLMs
- The framework integrates static analysis and mutation-based fuzzing in an iterative process during code generation
- Security improvements were achieved without compromising code functionality
- Three specialized agents collaborate continuously: code generation, vulnerability identification, and dynamic testing
**Limitations**: The abstract does not specify limitations of the approach or potential constraints on scalability and generalizability.

### Palavalli & Santolucito (2024)

**Research question**: Can a feedback loop that returns errors and warnings improve LLM agent performance in generating Infrastructure as Code?
**Methodology**: The authors investigate an LLM agent's ability to construct infrastructure using the Infrastructure as Code paradigm, employing a feedback loop that returns errors and warnings on generated IaC to allow iterative code improvement by the LLM agent.
**Key findings**:
- LLM agents can construct infrastructure using the Infrastructure as Code paradigm
- A feedback loop returning errors and warnings enables the LLM agent to improve generated code
- The effectiveness of the feedback loop decreases exponentially with each iteration
- The feedback loop eventually plateaus at a certain point and becomes ineffective
**Limitations**: The feedback loop's effectiveness diminishes exponentially until it plateaus and becomes ineffective after certain iterations.

### Pan et al. (2025)

**Research question**: How can multi-agent frameworks reduce error propagation in sequential code generation workflows to improve syntactic and semantic correctness of LLM-generated code?
**Methodology**: The authors propose CodeCoR, a four-agent framework where agents generate prompts, code, test cases, and repair advice respectively, with each agent producing multiple outputs and pruning low-quality ones. Generated code is tested locally, with failing code sent to a repair agent for iterative refinement before returning the code that passes the most test cases.
**Key findings**:
- CodeCoR outperforms existing baselines including CodeCoT and MapCoder on code generation tasks
- The framework achieves an average Pass@1 score of 77.13% across four datasets
- Experiments were conducted on HumanEval, HumanEval-ET, MBPP, and MBPP-ET datasets
- The pruning mechanism reduces error propagation in sequential workflows
**Limitations**: Not stated in abstract.

### Rasheed et al. (2024)

**Research question**: How can a multi-agent AI model be designed to evaluate and compare the performance of various Large Language Models in code generation tasks?
**Methodology**: The authors introduce a multi-agent model consisting of eight distinct AI agents that retrieve code from different LLMs (GPT-3.5, GPT-3.5 Turbo, GPT-4, GPT-4 Turbo, Google Bard, LLAMA, and Hugging Face) based on common descriptions, plus a verification agent that evaluates generated code using the HumanEval benchmark.
**Key findings**:
- GPT-3.5 Turbo model's performance is comparatively better than other tested models
- The multi-agent framework enables side-by-side comparison of different LLMs
- The verification agent successfully integrates HumanEval benchmark for code assessment
- The preliminary analysis serves as a benchmark for LLM performance comparison
**Limitations**: The evaluation currently lacks the MBPP benchmark which is planned for future work; practitioner feedback from twenty users is also pending.

### Wu & Fard (2024)

**Research question**: Can LLMs and LLM agents demonstrate communication competence by asking clarifying questions when code generation problem descriptions contain issues?
**Methodology**: The authors created HumanEvalComm, a new benchmark modified from existing problems with three types of issues (inconsistency, ambiguity, incompleteness), and defined new metrics (Communication Rate, Good Question Rate) to evaluate Code LLMs and the Okanagan LLM agent approach.
**Key findings**:
- Top-level software engineers ask clarifying questions to reduce ambiguity, suggesting LLMs should exhibit similar communication behavior
- HumanEvalComm benchmark was created by modifying problem descriptions to include inconsistency, ambiguity, and incompleteness
- New evaluation metrics were defined: Communication Rate and Good Question Rate
- Experiments compared different Code LLMs against the Okanagan LLM agent approach
**Limitations**: The abstract does not specify limitations of the benchmark or the comparative results between Code LLMs and Okanagan.

### Yang et al. (2025)

**Research question**: How can multi-agent collaborative systems improve the quality and reliability of automated code documentation generation?
**Methodology**: The authors introduce DocAgent, a multi-agent system using topological code processing for incremental context building with five specialized agents (Reader, Searcher, Writer, Verifier, Orchestrator), and propose a multi-faceted evaluation framework assessing Completeness, Helpfulness, and Truthfulness.
**Key findings**:
- DocAgent uses topological code processing for incremental context building with specialized collaborative agents
- The system includes five agents: Reader, Searcher, Writer, Verifier, and Orchestrator
- DocAgent significantly outperforms baselines consistently across comprehensive experiments
- Ablation study confirms the vital role of topological processing order
- The multi-faceted evaluation framework assesses Completeness, Helpfulness, and Truthfulness
**Limitations**: The abstract does not specify limitations regarding computational overhead, scalability to very large codebases, or domain-specific constraints.

### Dong et al. (2025)

**Research question**: What is the current state of LLM-based code generation agents, and what are the core techniques, applications, and future research directions in this field?
**Methodology**: This paper presents a systematic survey tracing the developmental trajectory of LLM-based code generation agents, categorizing core techniques including single-agent and multi-agent architectures, and documenting applications across the full software development lifecycle.
**Key findings**:
- Code generation agents are characterized by three core features: autonomy, expanded task scope beyond code snippets, and enhanced engineering practicality
- The field has evolved from algorithmic innovation toward practical engineering challenges like system reliability and tool integration
- The survey categorizes techniques into single-agent and multi-agent architectures
- Applications now span the entire software development lifecycle rather than just code snippet generation
- The paper identifies foundational long-term research directions based on analysis of primary challenges
**Limitations**: The abstract does not explicitly state limitations of the survey methodology or scope constraints.

## References

Dong, Y., Jiang, X., Qian, J., Wang, T., Zhang, K., Jin, Z., & Li, G. (2025). A survey on code generation with LLM-based agents. arXiv. https://arxiv.org/abs/2508.00083

Ishibashi, Y., & Nishimura, Y. (2024). Self-organized agents: A LLM multi-agent framework toward ultra large-scale code generation and optimization. arXiv. https://arxiv.org/abs/2404.02183

Li, J., Shi, X., Zhang, K., Li, G., Jin, Z., Li, L., Zhang, H., Li, J., Liu, F., Zhang, Y., Tao, Z., Dong, Y., Zhu, Y., Tao, C., et al. (2025). GraphCodeAgent: Dual graph-guided LLM agent for retrieval-augmented repo-level code generation. arXiv. https://arxiv.org/abs/2504.10046

Liu, K., Pan, Y., Xiang, Y., He, D., Li, J., Du, Y., & Gao, T. (2025). ProjectEval: A benchmark for programming agents automated evaluation on project-level code generation. arXiv. https://arxiv.org/abs/2503.07010

Nunez, A., Islam, N. T., Jha, S. K., & Najafirad, P. (2024). AutoSafeCoder: A multi-agent framework for securing LLM code generation through static analysis and fuzz testing. arXiv. https://arxiv.org/abs/2409.10737

Palavalli, M. A., & Santolucito, M. (2024). Using a feedback loop for LLM-based infrastructure as code generation. arXiv. https://arxiv.org/abs/2411.19043

Pan, R., Zhang, H., & Liu, C. (2025). CodeCoR: An LLM-based self-reflective multi-agent framework for code generation. arXiv. https://arxiv.org/abs/2501.07811

Rasheed, Z., Waseem, M., Systä, K., & Abrahamsson, P. (2024). Large language model evaluation via multi AI agents: Preliminary results. arXiv. https://arxiv.org/abs/2404.01023

Wu, J. J. W., & Fard, F. H. (2024). HumanEvalComm: Benchmarking the communication competence of code generation for LLMs and LLM agent. arXiv. https://arxiv.org/abs/2406.00215

Yang, D., Simoulin, A., Qian, X., Liu, X., Cao, Y., Teng, Z., & Yang, G. (2025). DocAgent: A multi-agent system for automated code documentation generation. arXiv. https://arxiv.org/abs/2504.08725
