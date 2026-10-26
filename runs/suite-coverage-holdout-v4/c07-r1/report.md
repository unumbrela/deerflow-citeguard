# Systematic Literature Review: LLM/Agent-as-Data-Analyst

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "agent data analyst", category cs.AI, published between 2023-09-28 and 2025-09-27
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM/Agent-as-Data-Analyst reveals a rapidly evolving field focused on developing autonomous AI systems capable of conducting scientific research and data analysis with minimal human intervention. The surveyed papers collectively demonstrate a shift from single-query analytical tools to comprehensive, multi-agent frameworks that can execute entire research pipelines—from hypothesis generation through experimental design, execution, and manuscript preparation. A dominant trend is the specialization of agents for domain-specific tasks, particularly in biology and chemistry, where systems integrate specialized computational tools, knowledge graphs, and validation mechanisms. The field shows strong convergence on the need for hierarchical architectures, iterative refinement processes, and rigorous evaluation benchmarks, though significant gaps remain in generalizability across domains and transparent limitation reporting.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "agent data analyst", filtered to category cs.AI, published between 2023-09-28 and 2025-09-27. Papers were sorted by relevance through citation expansion and co-citation analysis, and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search and screening results**: The initial search identified 8 papers by phrase matching, which was expanded to 22 papers through citation expansion (checking references from the initial pool). After screening for centrality to the topic "LLM/Agent-as-Data-Analyst", 10 papers were included. Notably, 8 of the 10 included papers came from the citation expansion phase, indicating the value of looking beyond direct search matches to capture relevant literature.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, the search was constrained to the cs.AI category, potentially missing relevant work in domain-specific categories such as cs.CL, cs.CV, or q-bio.

## Themes

### Theme 1: Autonomous Scientific Discovery Systems

A major research direction focuses on developing fully autonomous systems that can conduct complete scientific research workflows without human intervention. The AI Scientist framework (Lu et al., 2024) represents a pioneering comprehensive system that generates novel research ideas, writes code, executes experiments, visualizes results, writes full scientific papers, and runs simulated review processes—all at a cost of less than $15 per paper. Similarly, AI-Researcher (Tang et al., 2025) orchestrates the complete research pipeline from literature review through hypothesis generation, algorithm implementation, and manuscript preparation, achieving implementation success rates and paper quality approaching human-level performance.

PROTEUS (Ding et al., 2024) extends this vision to proteomics research, taking datasets as input and producing research objectives, analysis results, and novel biological hypotheses without human intervention. The system generated 191 scientific hypotheses across 12 proteomics datasets, which were validated through both automatic LLM-based scoring and human expert reviews. These systems share a common architecture of hierarchical planning, tool execution, and iterative refinement, suggesting convergence on multi-level abstraction as a key design principle for autonomous scientific discovery.

### Theme 2: Domain-Specific AI Analysts

Rather than general-purpose analysts, many systems are designed for specific scientific domains, particularly biology and chemistry. BioDiscoveryAgent (Roohani et al., 2024) specializes in designing genetic perturbation experiments, achieving 21% average improvement over Bayesian optimization baselines and 46% improvement on the harder task of non-essential gene perturbation. The agent leverages biological knowledge from literature search, code execution, and peer evaluation tools without requiring model training or explicit acquisition functions.

K-Dense Analyst (Li et al., 2025) targets bioinformatics analysis through a hierarchical multi-agent system with dual-loop architecture, achieving 29.2% accuracy on BixBench—surpassing GPT-5 by 6.3 percentage points using only Gemini 2.5 Pro as the underlying model. This demonstrates that architectural innovations can unlock capabilities far beyond baseline model performance. Similarly, SciToolAgent (Ding et al., 2025) automates hundreds of scientific tools across biology, chemistry, and materials science using a scientific tool knowledge graph for intelligent tool selection through graph-based retrieval-augmented generation.

### Theme 3: Benchmark Development for AI Research Capabilities

The field shows strong emphasis on creating comprehensive benchmarks to evaluate AI systems' research and analytical capabilities. LAB-Bench (Laurent et al., 2024) contains over 2,400 multiple choice questions covering practical biology research capabilities including literature recall and reasoning, figure interpretation, database navigation, and DNA/protein sequence manipulation. The benchmark enables direct comparison of frontier language models against human expert biology researchers.

InsightBench (Sahu et al., 2024) focuses on business analytics, providing 100 diverse business datasets with curated insights for evaluating agents' ability to perform end-to-end analytics including question formulation, answer interpretation, and insight generation. The benchmark uses LLaMA-3 as an evaluator and enables comprehensive evaluation beyond single-query resolution. These benchmarks reflect a maturing field moving from proof-of-concept demonstrations to rigorous, standardized evaluation frameworks.

### Theme 4: Multi-Agent and Hierarchical Architectures

A recurring architectural pattern across the surveyed papers is the use of multiple specialized agents working in coordination. The generative agents system for investigative data reporting (Veerbeek & Diakopoulos, 2024) employs three specialized agents—an analyst, a reporter, and an editor—to collaboratively generate and refine tips from datasets, generally producing more newsworthy and accurate insights compared to baseline models without agents.

K-Dense Analyst (Li et al., 2025) uses a dual-loop architecture that couples planning with validated execution using specialized agents to decompose complex objectives into executable, verifiable tasks within secure computational environments. This hierarchical decomposition enables the system to bridge high-level scientific objectives and low-level computational execution. The convergence on multi-agent architectures suggests recognition that single monolithic models cannot adequately handle the diverse subtasks required for complex scientific analysis.

### Theme 5: Tool Integration and Knowledge Graphs

Enhancing LLMs with external tools and structured knowledge representations emerges as a critical theme. SciToolAgent (Ding et al., 2025) leverages a scientific tool knowledge graph enabling intelligent tool selection through graph-based retrieval-augmented generation, combined with a comprehensive safety-checking module for responsible and ethical tool usage. The system was evaluated through case studies in protein engineering, chemical reactivity prediction, chemical synthesis, and metal-organic framework screening.

BioDiscoveryAgent (Roohani et al., 2024) provides access to literature search, code execution, and peer evaluation tools, enabling the agent to navigate hypothesis spaces using biological knowledge without requiring explicit model training. The LLM-based approach for insight generation (Sánchez Pérez et al., 2025) uses a three-component framework with a Hypothesis Generator, Query Agent for SQL generation, and Summarization module, demonstrating that modular tool integration produces more insightful results than monolithic approaches while maintaining correctness.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several key points. First, all systems employ some form of hierarchical planning or multi-level abstraction to manage complexity—from high-level research objectives down to executable computational tasks. Second, there is consensus that domain specialization outperforms general-purpose approaches, particularly in scientific domains requiring specialized knowledge and tools. Third, all papers emphasize the importance of iterative refinement processes, whether through multi-agent collaboration, dual-loop architectures, or simulated review processes. Fourth, the field converges on the necessity of comprehensive benchmarks for rigorous evaluation, with multiple papers introducing new evaluation frameworks rather than relying on existing metrics.

**Disagreements**: While not explicit contradictions, the papers differ in their approach to validation and quality assurance. Systems like The AI Scientist (Lu et al., 2024) and AI-Researcher (Tang et al., 2025) rely heavily on automated review processes and LLM-based evaluation, whereas PROTEUS (Ding et al., 2024) and BioDiscoveryAgent (Roohani et al., 2024) emphasize human expert validation alongside automated scoring. Additionally, there is variation in the degree of automation: some systems aim for fully autonomous operation end-to-end, while others like the investigative reporting system (Veerbeek & Diakopoulos, 2024) position themselves as tools to augment rather than replace human analysts.

## Gaps and Open Questions

Several significant gaps emerge from the collective literature. First, **limitation reporting is notably absent**: 8 of the 10 papers explicitly state "not stated in abstract" or similar for limitations, suggesting a field-wide tendency to emphasize capabilities over constraints. This makes it difficult to assess failure modes, domain boundaries, or appropriate use cases.

Second, **generalizability remains unproven**: while domain-specific systems show impressive performance in their target areas (biology, chemistry, business analytics), there is limited evidence of transferability across domains. The heavy reliance on domain-specific knowledge graphs, tools, and benchmarks raises questions about whether these systems can adapt to new domains without substantial re-engineering.

Third, **computational and resource requirements are under-specified**: none of the papers provide detailed analysis of computational costs beyond The AI Scientist's mention of "$15 per paper," leaving unclear the practical barriers to adoption for resource-constrained researchers.

Fourth, **ethical and safety considerations are mentioned but not deeply addressed**: while SciToolAgent (Ding et al., 2025) mentions a "comprehensive safety-checking module," the abstract provides no details on what this entails or how safety is validated. As these systems become more autonomous, the lack of detailed safety frameworks represents a significant gap.

Finally, **human-AI collaboration models are under-explored**: most systems position themselves as fully autonomous, with limited discussion of optimal human-AI interaction patterns, oversight mechanisms, or scenarios where human intervention is necessary or preferred.

## Per-Paper Annotations

### Laurent et al. (2024)

**Research question**: How can we evaluate language model performance on practical tasks required for biological scientific research?

**Methodology**: The authors introduce LAB-Bench, a dataset of over 2,400 multiple choice questions covering practical biology research capabilities including literature recall and reasoning, figure interpretation, database navigation, and DNA/protein sequence manipulation. They measure performance of several frontier language models against this benchmark and compare results to human expert biology researchers.

**Key findings**:
- LAB-Bench contains over 2,400 multiple choice questions designed to evaluate AI systems on practical biology research capabilities
- The benchmark covers literature recall and reasoning, figure interpretation, database access and navigation, and DNA/protein sequence comprehension and manipulation
- Frontier language models were evaluated against the benchmark with results compared to human expert biology researchers
- A public subset of LAB-Bench is available for community use

**Limitations**: The abstract does not explicitly state limitations of the benchmark or study.

### Ding et al. (2025)

**Research question**: How can Large Language Models be enhanced to seamlessly integrate and orchestrate multiple specialized computational tools for complex scientific workflows?

**Methodology**: The authors present SciToolAgent, an LLM-powered agent that automates hundreds of scientific tools across biology, chemistry, and materials science using a scientific tool knowledge graph for intelligent tool selection through graph-based retrieval-augmented generation, combined with a comprehensive safety-checking module. The system was evaluated on a curated benchmark and tested through case studies in protein engineering, chemical reactivity prediction, chemical synthesis, and metal-organic framework screening.

**Key findings**:
- SciToolAgent automates hundreds of scientific tools across biology, chemistry, and materials science
- The system leverages a scientific tool knowledge graph enabling intelligent tool selection through graph-based retrieval-augmented generation
- A comprehensive safety-checking module ensures responsible and ethical tool usage
- Extensive evaluations demonstrate SciToolAgent significantly outperforms existing approaches
- Case studies demonstrate capability to automate complex workflows in protein engineering, chemical reactivity prediction, chemical synthesis, and metal-organic framework screening

**Limitations**: The abstract does not explicitly state limitations of the approach or system.

### Ding et al. (2024)

**Research question**: Can large language models automate entire exploratory proteomics research processes and generate novel scientific hypotheses without human intervention?

**Methodology**: The authors present PROTEUS, a fully automated system using large language models to perform hierarchical planning, execute specialized bioinformatics tools, and iteratively refine analysis workflows. The system was evaluated on 12 proteomics datasets from various biological samples (immune cells, tumors) and sample types (single-cell and bulk), generating 191 scientific hypotheses that were assessed using automatic LLM-based scoring on 5 metrics and detailed reviews from human experts.

**Key findings**:
- PROTEUS is a fully automated system that takes proteomics datasets as input and produces research objectives, analysis results, and novel biological hypotheses without human intervention
- The system was evaluated on 12 proteomics datasets from various biological samples and sample types
- PROTEUS generated 191 scientific hypotheses that were assessed through both automatic LLM-based scoring and human expert reviews
- Results demonstrate the system consistently produces reliable, logically coherent results that align with existing literature while proposing novel, evaluable hypotheses
- The flexible architecture facilitates seamless integration of diverse analysis tools and adaptation to different proteomics data types

**Limitations**: The abstract does not explicitly state limitations of the system or approach.

### Lu et al. (2024)

**Research question**: Can frontier large language models be developed into agents capable of conducting complete scientific research independently, from idea generation through paper writing and review?

**Methodology**: The authors introduce The AI Scientist, a comprehensive framework enabling frontier LLMs to perform independent research by generating novel research ideas, writing code, executing experiments, visualizing results, writing full scientific papers, and running a simulated review process for evaluation. The system was applied to three distinct machine learning subfields (diffusion modeling, transformer-based language modeling, and learning dynamics), with each idea developed into a full paper at less than $15 cost. An automated reviewer was designed and validated to achieve near-human performance in evaluating paper scores.

**Key findings**:
- The AI Scientist is the first comprehensive framework for fully automatic scientific discovery
- The system generates novel research ideas, writes code, executes experiments, visualizes results, writes full scientific papers, and runs simulated review processes
- Each research idea is implemented and developed into a full paper at a cost of less than $15
- The automated reviewer achieves near-human performance in evaluating paper scores
- The AI Scientist can produce papers that exceed the acceptance threshold at top machine learning conferences as judged by the automated reviewer
- The code is open-sourced and available for community use

**Limitations**: The abstract does not explicitly state limitations of the approach, though it focuses on machine learning subfields as demonstration domains.

### Tang et al. (2025)

**Research question**: How can AI-driven autonomous systems transform scientific research pipelines from literature review to publication-ready manuscript preparation?

**Methodology**: The authors developed AI-Researcher, a fully autonomous research system that orchestrates the complete research pipeline with minimal human intervention. They created Scientist-Bench, a comprehensive benchmark with state-of-the-art papers across AI domains featuring guided innovation and open-ended exploration tasks, and evaluated the system through extensive experiments measuring implementation success rates and paper quality.

**Key findings**:
- AI-Researcher achieves remarkable implementation success rates in autonomous research tasks
- The system produces research papers that approach human-level quality
- The framework seamlessly orchestrates literature review, hypothesis generation, algorithm implementation, and manuscript preparation
- AI-Researcher can systematically explore solution spaces beyond human cognitive limitations

**Limitations**: The abstract does not explicitly state specific limitations of the approach, such as computational requirements, domain constraints, or failure modes.

### Sahu et al. (2024)

**Research question**: How can we evaluate AI agents' ability to perform end-to-end business data analytics including question formulation, answer interpretation, and insight generation?

**Methodology**: The authors created InsightBench, a benchmark dataset with 100 diverse business datasets (finance, incident management, etc.) with curated insights. They implemented a two-way evaluation mechanism using LLaMA-3 as an evaluator and proposed AgentPoirot, a baseline agent for end-to-end analytics. They compared AgentPoirot against existing single-query approaches like Pandas Agent and evaluated both open- and closed-source LLMs.

**Key findings**:
- AgentPoirot outperforms existing single-query approaches such as Pandas Agent on end-to-end analytics tasks
- InsightBench provides 100 datasets representing diverse business use cases with clear goals and meaningful questions
- LLaMA-3 serves as an effective open-source evaluator for assessing agents' insight extraction capabilities
- The benchmark enables comprehensive evaluation of automated data analytics beyond single-query resolution

**Limitations**: The abstract does not explicitly state limitations, though it notes the benchmark focuses on specific business domains and the evaluation relies on planted insights which may not capture all real-world complexity.

### Roohani et al. (2024)

**Research question**: Can LLM-based agents design genetic perturbation experiments to identify genes that produce specific phenotypes when perturbed?

**Methodology**: The authors developed BioDiscoveryAgent, an LLM-based agent that designs experiments, reasons about outcomes, and navigates hypothesis spaces using biological knowledge without requiring model training or explicit acquisition functions. They evaluated the agent using Claude 3.5 Sonnet on six datasets (including one unpublished) for predicting genetic perturbations, comparing against Bayesian optimization baselines and random baselines, with access to literature search, code execution, and peer evaluation tools.

**Key findings**:
- BioDiscoveryAgent achieves 21% average improvement over Bayesian optimization baselines in predicting relevant genetic perturbations across six datasets
- The agent shows 46% improvement on the harder task of non-essential gene perturbation
- BioDiscoveryAgent predicts gene combinations to perturb more than twice as accurately as random baseline
- The approach works on unpublished datasets, demonstrating generalization beyond training data
- The agent is interpretable at every stage of the experimental design process

**Limitations**: The abstract does not explicitly state limitations, though it notes the evaluation was conducted on specific genetic perturbation tasks and the agent's performance may depend on the underlying LLM's biological knowledge.

### Sánchez Pérez et al. (2025)

**Research question**: How can Large Language Models automatically generate concise, text-based insights that reflect interesting patterns in multi-table databases?

**Methodology**: The authors developed a three-component framework: a Hypothesis Generator to formulate domain-relevant questions, a Query Agent to generate SQL queries against databases, and a Summarization module to verbalize insights. They evaluated generated insights using a hybrid model combining human judgment and automated metrics for both correctness and subjective insightfulness, testing on public and enterprise databases.

**Key findings**:
- The LLM-based approach generates more insightful insights than other approaches while maintaining correctness
- The three-module framework effectively produces concise, text-based insights from multi-table databases
- The hybrid evaluation model successfully assesses both correctness and subjective insightfulness
- The approach works on both public and enterprise databases

**Limitations**: The abstract does not explicitly state limitations, though the reliance on human judgment for evaluating subjective insightfulness may introduce variability and the approach may be constrained by the LLM's ability to formulate relevant hypotheses.

### Li et al. (2025)

**Research question**: How can large language models be enhanced to perform autonomous bioinformatics analysis through iterative computation, tool integration, and rigorous validation?

**Methodology**: The authors introduce K-Dense Analyst, a hierarchical multi-agent system with a dual-loop architecture that couples planning with validated execution using specialized agents to decompose complex objectives into executable, verifiable tasks within secure computational environments. The system was evaluated on BixBench, a comprehensive benchmark for open-ended biological analysis.

**Key findings**:
- K-Dense Analyst achieves 29.2% accuracy on BixBench, surpassing GPT-5 by 6.3 percentage points (nearly 27% improvement)
- The system achieves this performance using Gemini 2.5 Pro, which attains only 18.3% accuracy when used directly
- Architectural innovations unlock capabilities far beyond the underlying model's baseline performance
- Autonomous scientific reasoning requires purpose-built systems that bridge high-level scientific objectives and low-level computational execution

**Limitations**: Not stated in abstract.

### Veerbeek & Diakopoulos (2024)

**Research question**: Can generative AI agents collaboratively generate and refine newsworthy tips from datasets for investigative data reporting?

**Methodology**: The authors introduce a system employing three specialized agents—an analyst, a reporter, and an editor—to collaboratively generate and refine tips from datasets. The approach was validated using real-world investigative stories, comparing the agent-based system against a baseline model without agents.

**Key findings**:
- The agent-based system generally generates more newsworthy and accurate insights compared to a baseline model without agents
- Some variability was noted between different stories in the system's performance
- Generative AI has potential to provide leads for investigative data reporting

**Limitations**: Not stated in abstract.

## References

Ding, K., Yu, J., Huang, J., Yang, Y., Zhang, Q., & Chen, H. (2025). SciToolAgent: A knowledge graph-driven scientific agent for multi-tool integration. arXiv. https://arxiv.org/abs/2507.20280

Ding, N., Qu, S., Xie, L., Li, Y., Liu, Z., Zhang, K., Xiong, Y., Zuo, Y., Chen, Z., Hua, E., Lv, X., Sun, Y., Li, Y., Li, D., He, F., & Zhou, B. (2024). Automating exploratory proteomics research via language models. arXiv. https://arxiv.org/abs/2411.03743

Laurent, J. M., Janizek, J. D., Ruzo, M., Hinks, M. M., Hammerling, M. J., Narayanan, S., Ponnapati, M., White, A. D., & Rodriques, S. G. (2024). LAB-Bench: Measuring capabilities of language models for biology research. arXiv. https://arxiv.org/abs/2407.10362

Li, O., Agarwal, V., Zhou, S., Gopinath, A., & Kassis, T. (2025). K-Dense Analyst: Towards fully automated scientific analysis. arXiv. https://arxiv.org/abs/2508.07043

Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. arXiv. https://arxiv.org/abs/2408.06292

Roohani, Y., Lee, A., Huang, Q., Vora, J., Steinhart, Z., Huang, K., Marson, A., Liang, P., & Leskovec, J. (2024). BioDiscoveryAgent: An AI agent for designing genetic perturbation experiments. arXiv. https://arxiv.org/abs/2405.17631

Sahu, G., Puri, A., Rodriguez, J., Abaskohi, A., Chegini, M., Abaskohi, H., Taslakian, P., Zantedeschi, V., Lacoste, A., Vazquez, D., Chapados, N., Pal, C., Mudumba, S. R., & Laradji, I. H. (2024). InsightBench: Evaluating business analytics agents through multi-step insight generation. arXiv. https://arxiv.org/abs/2407.06423

Sánchez Pérez, A., Boukhary, A., Papotti, P., Castejón Lozano, L., & Elwood, A. (2025). An LLM-based approach for insight generation in data analysis. arXiv. https://arxiv.org/abs/2503.11664

Tang, J., Xia, L., Li, Z., & Huang, C. (2025). AI-Researcher: Autonomous scientific innovation. arXiv. https://arxiv.org/abs/2505.18705

Veerbeek, J., & Diakopoulos, N. (2024). Using generative agents to create tip sheets for investigative data reporting. arXiv. https://arxiv.org/abs/2409.07286
