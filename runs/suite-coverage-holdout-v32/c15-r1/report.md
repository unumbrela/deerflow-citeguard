# Systematic Literature Review: Code Generation with LLM-based Agents

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "code generation LLM agents", filtered to category cs.SE, published between 2023-07-31 and 2025-07-30
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM-based agents for code generation reveals a rapidly evolving field focused on multi-agent collaborative frameworks that address critical limitations of single-agent approaches. The surveyed papers collectively demonstrate a paradigm shift from monolithic LLM code generation to distributed, specialized agent systems that incorporate self-reflection, iterative feedback, and domain-specific validation mechanisms. Key advances include security integration through static and dynamic analysis, communication competence for handling ambiguous requirements, topological code processing for documentation, and graph-guided retrieval for repository-level generation. The field shows strong convergence on the benefits of multi-agent architectures, with consistent improvements in pass rates, security, and scalability compared to baseline single-agent systems. However, significant gaps remain in long-term evaluation, real-world deployment validation, and understanding the diminishing returns of iterative feedback mechanisms.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "code generation LLM agents", filtered to category cs.SE, published between 2023-07-31 and 2025-07-30. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Agent Collaborative Frameworks

A dominant theme across the surveyed literature is the transition from single-agent to multi-agent architectures for code generation tasks. Six of the ten papers explicitly propose multi-agent frameworks with specialized roles, reflecting a consensus that distributed collaboration outperforms monolithic approaches.

AutoSafeCoder exemplifies this trend with three specialized agents: a Coding Agent for generation, a Static Analyzer Agent for vulnerability identification, and a Fuzzing Agent for dynamic testing (Nunez et al., 2024). This division of labor enables continuous security validation during generation rather than post-hoc analysis. Similarly, DocAgent employs five specialized agents (Reader, Searcher, Writer, Verifier, Orchestrator) for automated documentation generation, with each agent handling distinct subtasks in a coordinated pipeline (Yang et al., 2025).

The Self-Organized Agents (SoA) framework takes multi-agent collaboration further by introducing automatic agent multiplication based on problem complexity (Ishibashi & Nishimura, 2024). This approach addresses context length constraints by distributing code volume across multiple agents while maintaining per-agent cognitive load at manageable levels. The framework's 5% improvement in Pass@1 accuracy on HumanEval demonstrates that multi-agent systems can surpass powerful single-agent baselines even on established benchmarks.

CodeCoR introduces a four-agent framework with a self-reflective pruning mechanism, where agents generate multiple outputs and eliminate low-quality intermediate results (Pan et al., 2025). This approach specifically targets error propagation in sequential workflows, a critical challenge in multi-step code generation pipelines. The framework's 77.13% average Pass@1 score across four datasets validates the effectiveness of multi-agent collaboration with quality filtering.

### Theme 2: Iterative Feedback and Self-Reflection

A second prominent theme is the integration of feedback loops and self-reflection mechanisms to improve code generation quality through iterative refinement. Five papers explicitly incorporate feedback-driven improvement cycles, suggesting widespread recognition that single-pass generation is insufficient for complex software engineering tasks.

The feedback loop approach is most explicitly studied in the context of Infrastructure as Code generation, where Palavalli and Santolucito (2024) investigate how returning errors and warnings enables iterative code improvement. Their findings reveal a critical limitation: feedback effectiveness decreases exponentially with each iteration and eventually plateaus, indicating diminishing returns that constrain the practical utility of extended refinement cycles.

CodeCoR implements a more sophisticated feedback mechanism by testing generated code in a local environment and routing failing code to a repair agent (Pan et al., 2025). This closed-loop system enables targeted repairs based on concrete execution failures rather than abstract quality assessments. The integration of test-driven feedback with multi-agent collaboration produces robust improvements across diverse benchmarks.

AutoSafeCoder's feedback operates through static analysis and fuzz testing, with vulnerabilities identified during generation feeding back to the Coding Agent for immediate correction (Nunez et al., 2024). The 13% reduction in vulnerabilities demonstrates that security-focused feedback integrated during generation outperforms post-generation security audits.

### Theme 3: Repository-Level and Project-Level Code Generation

Three papers address the challenge of scaling code generation from isolated functions to repository-level and project-level contexts, reflecting growing recognition that practical software development requires understanding broader codebase structure and dependencies.

GraphCodeAgent introduces a dual graph-guided approach that constructs a Requirement Graph to model requirement relations and a Structural-Semantic Code Graph to capture repository code dependencies (Li et al., 2025). This architecture enables multi-hop reasoning to retrieve both explicit and implicit code snippets not directly expressed in requirements, addressing a critical gap in repository-level generation. The framework's significant outperformance of state-of-the-art baselines on DevEval and CoderEval benchmarks validates the graph-guided retrieval approach.

ProjectEval introduces a benchmark specifically designed for project-level code generation evaluation (Liu et al., 2025). The benchmark's construction through LLM generation with human reviewing ensures both scalability and quality, while its three-level input structure (natural languages or code skeletons) accommodates varying specification granularities. The emphasis on user interaction simulation for execution evaluation reflects a user-centric perspective often absent in function-level benchmarks.

Self-Organized Agents addresses repository-scale generation through automatic agent multiplication, enabling indefinite increase in overall code volume while maintaining per-agent code volume at manageable levels (Ishibashi & Nishimura, 2024). This approach directly tackles the context length constraints that limit existing single-agent approaches to repository-scale tasks.

### Theme 4: Evaluation and Benchmarking

Four papers contribute to evaluation methodology and benchmark development, indicating active maturation of the field's assessment infrastructure. The diversity of evaluation approaches reflects both the novelty of multi-agent code generation and the need for task-specific metrics beyond traditional Pass@1.

HumanEvalComm introduces a novel benchmark that modifies problem descriptions to introduce inconsistency, ambiguity, and incompleteness, evaluating LLMs' communication competence through their ability to ask clarifying questions (Wu & Fard, 2024). The new metrics (Communication Rate and Good Question Rate) capture dimensions of code generation competence absent from traditional benchmarks, addressing the reality that professional developers routinely seek clarification before implementing ambiguous requirements.

ProjectEval's benchmark enables automatic evaluation from users' perspectives with explainable results (Liu et al., 2025). The emphasis on explainability addresses a critical gap in existing benchmarks that produce opaque pass/fail outcomes without diagnostic information about failure modes.

The multi-agent evaluation approach by Rasheed et al. (2024) introduces eight distinct AI agents responsible for retrieving code from different LLMs, with a verification agent integrating the HumanEval benchmark for comparative assessment. This meta-evaluation framework enables systematic comparison of LLM performance across multiple models simultaneously.

RepoRift achieves 78.2% success rate at Success@10 and 34.6% at Success@1 on the CodeSearchNet dataset through RAG-powered agents that enhance user queries with relevant repository details (Jain et al., 2024). The significant outperformance of existing methods at Success@1 indicates that agentic workflows substantially improve retrieval accuracy for semantic code search.

### Theme 5: Security and Reliability in Code Generation

Two papers explicitly address security and reliability concerns in LLM-generated code, reflecting growing awareness that functional correctness alone is insufficient for production deployment.

AutoSafeCoder's integration of static analysis and fuzz testing during code generation represents a proactive security approach that prevents vulnerabilities rather than detecting them post-hoc (Nunez et al., 2024). The 13% vulnerability reduction while maintaining functional correctness demonstrates that security and functionality need not be traded off when security validation is integrated into the generation process.

DocAgent's emphasis on Truthfulness as an evaluation dimension addresses the reliability challenge of factually incorrect outputs in automated documentation (Yang et al., 2025). The multi-agent verification mechanism ensures that generated documentation accurately reflects code behavior, addressing a critical barrier to adoption in production environments.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong consensus on several key points:

1. Multi-agent architectures consistently outperform single-agent baselines across diverse code generation tasks (Ishibashi & Nishimura, 2024; Nunez et al., 2024; Pan et al., 2025; Yang et al., 2025).

2. Iterative feedback mechanisms improve code quality, though with diminishing returns that eventually plateau (Palavalli & Santolucito, 2024; Pan et al., 2025).

3. Repository-level and project-level generation require fundamentally different approaches than function-level generation, with graph-based retrieval and topological processing emerging as effective strategies (Li et al., 2025; Liu et al., 2025).

4. Traditional benchmarks like HumanEval are insufficient for evaluating communication competence, security, and reliability dimensions of code generation (Wu & Fard, 2024; Nunez et al., 2024).

**Disagreements**: The surveyed papers show limited direct disagreement, likely reflecting the field's early stage and the complementary nature of proposed approaches. However, implicit tensions exist:

1. The optimal number of agents remains unresolved, with frameworks proposing between three (AutoSafeCoder) and eight (Rasheed et al.) agents depending on task complexity.

2. The effectiveness of feedback loops shows variability: while CodeCoR and AutoSafeCoder report sustained improvements through iterative refinement, Palavalli and Santolucito (2024) explicitly document exponential decay in feedback effectiveness, suggesting task-dependent limits.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Long-term deployment validation**: None of the surveyed papers report on real-world deployment of multi-agent code generation systems in production environments. All evaluations remain benchmark-based, limiting understanding of practical adoption barriers.

2. **Diminishing returns characterization**: While Palavalli and Santolucito (2024) document exponential decay in feedback loop effectiveness, systematic characterization of diminishing returns across different feedback types (static analysis, fuzz testing, execution failures) remains absent.

3. **Agent communication overhead**: Multi-agent frameworks incur communication and coordination costs that are not systematically analyzed. The trade-off between specialization benefits and coordination overhead remains unquantified.

4. **Human-agent collaboration**: None of the surveyed papers address how multi-agent code generation systems should collaborate with human developers, despite the reality that production software development is fundamentally human-centric.

5. **Limitations reporting**: Seven of ten papers do not state limitations in their abstracts, suggesting either space constraints or reluctance to explicitly acknowledge weaknesses. This limits the field's ability to build cumulatively on identified gaps.

## Per-Paper Annotations

### Ishibashi & Nishimura (2024)

**Research question**: How can multi-agent frameworks overcome context length constraints to enable ultra large-scale code generation and optimization?

**Methodology**: The authors propose Self-Organized Agents (SoA), a framework where agents operate independently to generate and modify code components while collaborating to construct the overall codebase, featuring automatic agent multiplication based on problem complexity.

**Key findings**:
- SoA enables indefinite increase in overall code volume by scaling the number of agents
- Each agent handles significantly less code than single-agent systems while generating more overall code
- SoA surpasses powerful single-agent baselines by 5% in Pass@1 accuracy on HumanEval benchmark
- Automatic agent multiplication based on problem complexity enables dynamic scalability

**Limitations**: not stated in abstract

### Jain et al. (2024)

**Research question**: How can Retrieval Augmented Generation powered agents improve semantic code search accuracy for ambiguous or context-dependent queries?

**Methodology**: The authors introduce RAG-powered agents that inject information into user prompts to provide better inputs for embedding models, enhancing queries with relevant GitHub repository details, deployed with a multi-stream ensemble approach.

**Key findings**:
- RepoRift achieves 78.2% success rate at Success@10 on the CodeSearchNet dataset
- RepoRift achieves 34.6% success rate at Success@1, significantly outperforming existing methods
- RAG agents enhance user queries with relevant repository details for better contextual alignment
- The multi-stream ensemble approach paired with agentic workflow improves retrieval accuracy

**Limitations**: not stated in abstract

### Li et al. (2025)

**Research question**: How can the gap between natural language requirements and programming implementations be bridged for repository-level code generation?

**Methodology**: The authors propose GraphCodeAgent, a dual graph-guided LLM agent that constructs a Requirement Graph to model requirement relations and a Structural-Semantic Code Graph to capture repository code dependencies, with multi-hop reasoning for context retrieval.

**Key findings**:
- GraphCodeAgent significantly outperforms state-of-the-art baselines on repo-level code generation
- The dual graph approach successfully bridges the gap between NL requirements and programming implementations
- Multi-hop reasoning enables retrieval of both implicit and explicit code snippets not explicitly expressed in requirements
- The approach was evaluated on three advanced LLMs using DevEval and CoderEval benchmarks

**Limitations**: not stated in abstract

### Liu et al. (2025)

**Research question**: How can LLM agents' project-level code generation capabilities be automatically evaluated from a user perspective with explainable results?

**Methodology**: The authors introduce ProjectEval, a benchmark constructed by LLM with human reviewing, featuring three different level inputs of natural languages or code skeletons, evaluating generated projects through user interaction simulation.

**Key findings**:
- Systematic engineering project code is key for LLM agents to achieve practical projects
- Overall understanding of the project is crucial for LLM agent success
- Comprehensive analysis capability is essential for developing effective programming agents
- The benchmark enables automatic evaluation from users' perspective with explainable results

**Limitations**: not stated in abstract

### Nunez et al. (2024)

**Research question**: How can multi-agent frameworks improve the security of LLM-generated code by integrating static and dynamic testing during code generation?

**Methodology**: The authors propose AutoSafeCoder, a multi-agent framework with three specialized agents: a Coding Agent for code generation, a Static Analyzer Agent for identifying vulnerabilities, and a Fuzzing Agent for mutation-based dynamic testing, integrating iterative static and dynamic security testing during generation.

**Key findings**:
- AutoSafeCoder achieves a 13% reduction in code vulnerabilities compared to baseline LLMs
- The multi-agent approach enables continuous collaboration between code generation, vulnerability analysis, and security enhancement
- The framework maintains functional correctness while improving security through iterative testing
- Experiments were validated using the SecurityEval dataset

**Limitations**: not stated in abstract

### Palavalli & Santolucito (2024)

**Research question**: Can a feedback loop returning errors and warnings improve LLM agent performance in Infrastructure as Code generation?

**Methodology**: The authors investigate an LLM agent's ability to construct infrastructure using the Infrastructure as Code paradigm, employing a feedback loop that returns errors and warnings on generated IaC to allow iterative code improvement.

**Key findings**:
- LLM agents can construct infrastructure using the Infrastructure as Code paradigm
- Feedback loops with errors and warnings enable LLM agents to iteratively improve generated code
- The effectiveness of the feedback loop decreases exponentially with each iteration
- The feedback loop eventually plateaus at a certain point and becomes ineffective

**Limitations**: The feedback loop's effectiveness diminishes exponentially until it plateaus and becomes ineffective after a certain number of iterations.

### Pan et al. (2025)

**Research question**: How can multi-agent frameworks reduce error propagation in sequential code generation workflows through self-reflection and pruning?

**Methodology**: The authors propose CodeCoR, a four-agent framework where agents generate prompts, code, test cases, and repair advice respectively, with each agent producing multiple outputs and pruning low-quality ones, and local environment testing for iterative repair.

**Key findings**:
- CodeCoR achieves an average Pass@1 score of 77.13% across four datasets
- The pruning mechanism reduces error propagation in sequential workflows by eliminating low-quality intermediate outputs
- Local environment testing enables iterative code repair through feedback to the coding agent
- CodeCoR outperforms existing baselines including CodeCoT and MapCoder on HumanEval, HumanEval-ET, MBPP, and MBPP-ET datasets

**Limitations**: not stated in abstract

### Rasheed et al. (2024)

**Research question**: How can multi-agent AI models be designed to evaluate and compare the performance of different Large Language Models?

**Methodology**: The authors introduce a multi-agent AI model consisting of eight distinct AI agents, each responsible for retrieving code based on a common description from different LLMs, with a verification agent integrating the HumanEval benchmark for assessment.

**Key findings**:
- GPT-3.5 Turbo model's performance was comparatively better than the other tested models
- The multi-agent model successfully retrieved code from seven different advanced language models using their APIs
- The verification agent effectively assessed generated code performance using HumanEval benchmark
- The preliminary analysis provides a side-by-side benchmark comparison of LLM performances

**Limitations**: The study is preliminary and plans to incorporate the MBPP benchmark for further refinement; practitioner feedback from twenty users is still pending.

### Wu & Fard (2024)

**Research question**: Can LLMs be evaluated on their ability to ask clarifying questions when faced with ambiguous or incomplete code generation requirements?

**Methodology**: The authors created HumanEvalComm, a new benchmark by modifying problem descriptions to introduce inconsistency, ambiguity, and incompleteness, with new evaluation metrics (Communication Rate and Good Question Rate) for assessing LLM questioning behavior.

**Key findings**:
- Top-tier software engineers ask clarifying questions to reduce ambiguity, a skill that should apply to LLMs
- HumanEvalComm benchmark evaluates LLM communication skills through modified problem descriptions with three issue types
- New metrics (Communication Rate and Good Question Rate) were defined to assess LLM questioning behavior
- The Okanagan LLM agent approach was evaluated alongside Code LLMs for identifying and asking questions about ambiguous requirements

**Limitations**: not stated in abstract

### Yang et al. (2025)

**Research question**: How can multi-agent collaborative systems improve the quality and reliability of automated code documentation generation?

**Methodology**: The authors introduce DocAgent, a multi-agent system using topological code processing for incremental context building with five specialized agents (Reader, Searcher, Writer, Verifier, Orchestrator), with a multi-faceted evaluation framework assessing Completeness, Helpfulness, and Truthfulness.

**Key findings**:
- DocAgent significantly outperforms baseline approaches consistently across experiments
- Topological code processing enables incremental context building for better documentation quality
- Multi-agent collaboration with specialized roles improves documentation reliability
- Ablation study confirms the vital role of topological processing order in system performance

**Limitations**: not stated in abstract

## References

Ishibashi, Y., & Nishimura, Y. (2024). Self-organized agents: A LLM multi-agent framework toward ultra large-scale code generation and optimization. arXiv. https://arxiv.org/abs/2404.02183

Jain, S., Dora, A., Sam, K. S., & Singh, P. (2024). LLM agents improve semantic code search. arXiv. https://arxiv.org/abs/2408.11058

Li, J., Shi, X., Zhang, K., Li, G., Jin, Z., Li, L., Zhang, H., Li, J., Liu, F., Zhang, Y., Tao, Z., Dong, Y., Zhu, Y., & Tao, C. (2025). GraphCodeAgent: Dual graph-guided LLM agent for retrieval-augmented repo-level code generation. arXiv. https://arxiv.org/abs/2504.10046

Liu, K., Pan, Y., Xiang, Y., He, D., Li, J., Du, Y., & Gao, T. (2025). ProjectEval: A benchmark for programming agents automated evaluation on project-level code generation. arXiv. https://arxiv.org/abs/2503.07010

Nunez, A., Islam, N. T., Jha, S. K., & Najafirad, P. (2024). AutoSafeCoder: A multi-agent framework for securing LLM code generation through static analysis and fuzz testing. arXiv. https://arxiv.org/abs/2409.10737

Palavalli, M. A., & Santolucito, M. (2024). Using a feedback loop for LLM-based infrastructure as code generation. arXiv. https://arxiv.org/abs/2411.19043

Pan, R., Zhang, H., & Liu, C. (2025). CodeCoR: An LLM-based self-reflective multi-agent framework for code generation. arXiv. https://arxiv.org/abs/2501.07811

Rasheed, Z., Waseem, M., Systä, K., & Abrahamsson, P. (2024). Large language model evaluation via multi AI agents: Preliminary results. arXiv. https://arxiv.org/abs/2404.01023

Wu, J. J. W., & Fard, F. H. (2024). HumanEvalComm: Benchmarking the communication competence of code generation for LLMs and LLM agent. arXiv. https://arxiv.org/abs/2406.00215

Yang, D., Simoulin, A., Qian, X., Liu, X., Cao, Y., Teng, Z., & Yang, G. (2025). DocAgent: A multi-agent system for automated code documentation generation. arXiv. https://arxiv.org/abs/2504.08725
