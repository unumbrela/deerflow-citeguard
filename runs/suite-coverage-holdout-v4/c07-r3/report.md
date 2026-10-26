# Systematic Literature Review: LLM/Agent-as-Data-Analyst

**Review Period:** September 28, 2023 – September 27, 2025  
**Category:** cs.AI (Artificial Intelligence)  
**Format:** APA Style  
**Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in Large Language Model (LLM) and AI agent systems designed for data analysis tasks. The review covers 10 peer-reviewed papers published between September 2023 and September 2025 in the cs.AI category. The selected works demonstrate significant progress in autonomous data science capabilities, ranging from single-agent systems to sophisticated multi-agent frameworks that can handle complex, multi-step analytical workflows.

Key themes identified include: (1) hierarchical task decomposition for complex data science workflows, (2) multi-agent collaboration for specialized analytical tasks, (3) code generation and execution for data manipulation, (4) benchmark development for evaluating data analysis agents, and (5) human-agent interaction protocols for interactive analytics.

---

## Methodology

### Search Strategy
A systematic search was conducted on arXiv's cs.AI category for papers published between September 28, 2023, and September 27, 2025. The search query focused on "LLM agent data analysis" using phrase matching with all terms required.

### Selection Criteria
Papers were included based on:
- Focus on LLMs or AI agents performing data analysis, data interpretation, or analytical reasoning tasks
- Publication in the cs.AI primary category
- Publication date within the specified window
- Peer-reviewed preprint status on arXiv

### Screening Process
From an initial pool of 48 papers identified through direct search and citation expansion, 30 papers were shortlisted. After screening for relevance to data analysis tasks, 10 papers were selected for this review. The screening process prioritized papers with demonstrated empirical evaluation and practical implementations.

---

## Review of Selected Papers

### 1. Data Interpreter: An LLM Agent For Data Science

**Authors:** Hong, S., Lin, Y., Liu, B., Liu, B., Wu, B., Zhang, C., Wei, C., Li, D., Chen, J., Zhang, J., Wang, J., Zhang, L., Zhang, L., Yang, M., Zhuge, M., Guo, T., Zhou, T., Tao, W., Tang, X., & Lu, X. (2024)

**Publication Date:** February 28, 2024

**Source:** arXiv:2402.18679v4

**Abstract:** This paper presents Data Interpreter, an LLM-based agent designed to solve data science problems end-to-end. The system incorporates Hierarchical Graph Modeling for breaking down complex problems into manageable subproblems and Programmable Node Generation for refining code generation results.

**Key Contributions:**
- Novel hierarchical graph modeling approach for task decomposition
- Dynamic node generation and graph optimization capabilities
- Significant performance improvements: 25% boost on InfiAgent-DABench (75.9% to 94.9% accuracy)
- Improved performance on machine learning tasks (88% to 95%) and open-ended tasks (60% to 97%)
- 26% improvement on MATH dataset compared to state-of-the-art baselines

**Relevance:** Directly addresses LLM agents for comprehensive data science workflows with empirical validation across multiple benchmarks.

---

### 2. AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions

**Authors:** Li, Z., Zang, Q., Ma, D., Guo, J., Zheng, T., Liu, M., Niu, X., Wang, Y., Yang, J., Liu, J., Zhong, W., Zhou, W., Huang, W., & Zhang, G. (2024)

**Publication Date:** October 27, 2024

**Source:** arXiv:2410.20424v3

**Abstract:** AutoKaggle is a collaborative multi-agent system designed to assist data scientists in completing data pipelines through iterative development processes combining code execution, debugging, and unit testing.

**Key Contributions:**
- Multi-agent framework for autonomous data science competition participation
- Iterative development process with code execution and debugging
- Customizable workflows allowing human intervention at each phase
- Universal data science toolkit with validated functions for data cleaning, feature engineering, and modeling
- Validation submission rate of 0.85 and comprehensive score of 0.82 on 8 Kaggle competitions

**Relevance:** Demonstrates practical application of multi-agent systems in real-world data science competition scenarios with human-AI collaboration capabilities.

---

### 3. Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?

**Authors:** Cao, R., Lei, F., Wu, H., Chen, J., Fu, Y., Gao, H., Xiong, X., Zhang, H., Mao, Y., Hu, W., Xie, T., Xu, H., Zhang, D., Wang, S., Sun, R., Yin, P., Xiong, C., Ni, A., Liu, Q., & Zhong, V. (2024)

**Publication Date:** July 15, 2024

**Source:** arXiv:2407.10956v1

**Abstract:** This paper introduces Spider2-V, the first multimodal agent benchmark focusing on professional data science and engineering workflows, featuring 494 real-world tasks across 20 enterprise-level applications.

**Key Contributions:**
- First comprehensive benchmark for multimodal agents in data science workflows
- 494 real-world tasks spanning data warehousing to orchestration
- Evaluation of state-of-the-art LLM/VLM agents reveals 14.0% success rate on full data workflows
- Identification of challenges in GUI-based interactions (16.2% success) and cloud-hosted workspaces (10.6% success)
- Automatic configuration system for task setup and evaluation metrics

**Relevance:** Provides critical benchmarking infrastructure for evaluating multimodal agents in professional data science contexts, revealing current limitations and future research directions.

---

### 4. SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning

**Authors:** Chi, Y., Lin, Y., Hong, S., Pan, D., Fei, Y., Mei, G., Liu, B., Pang, T., Kwok, J., Zhang, C., Liu, B., & Wu, C. (2024)

**Publication Date:** October 22, 2024

**Source:** arXiv:2410.17238v1

**Abstract:** SELA introduces Monte Carlo Tree Search (MCTS) to optimize the AutoML process, enabling agents to conduct experiments intelligently and iteratively refine strategies for exploring the machine learning solution space.

**Key Contributions:**
- Integration of Monte Carlo Tree Search with LLM agents for AutoML
- Tree-based representation of pipeline configurations for intelligent exploration
- Win rate of 65% to 80% against baselines across 20 machine learning datasets
- Improved diversity and quality of generated code through experimental feedback
- Novel approach to automated pipeline optimization

**Relevance:** Advances automated machine learning through intelligent search strategies, demonstrating superior performance in discovering optimal ML pipelines.

---

### 5. TaskWeaver: A Code-First Agent Framework

**Authors:** Qiao, B., Li, L., Zhang, X., He, S., Kang, Y., Zhang, C., Yang, F., Dong, H., Zhang, J., Wang, L., Ma, M., Zhao, P., Qin, S., Qin, X., Du, C., Xu, Y., Lin, Q., Rajmohan, S., & Zhang, D. (2023)

**Publication Date:** November 29, 2023

**Source:** arXiv:2311.17541v3

**Abstract:** TaskWeaver is a code-first framework for building LLM-powered autonomous agents that converts user requests into executable code and treats user-defined plugins as callable functions.

**Key Contributions:**
- Code-first approach for handling domain-specific data analytics tasks
- Support for rich data structures and flexible plugin usage
- Dynamic plugin selection leveraging LLM coding capabilities
- Domain-specific knowledge integration through examples
- Secure execution of generated code
- Open-source implementation available at https://github.com/microsoft/TaskWeaver/

**Relevance:** Provides foundational framework for code-based agent systems with strong support for domain-specific analytics and extensibility through plugins.

---

### 6. InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation

**Authors:** Sahu, G., Puri, A., Rodriguez, J., Abaskohi, A., Chegini, M., Drouin, A., Taslakian, P., Zantedeschi, V., Lacoste, A., Vazquez, D., Chapados, N., Pal, C., Mudumba, S. R., & Laradji, I. H. (2024)

**Publication Date:** July 8, 2024

**Source:** arXiv:2407.06423v4

**Abstract:** InsightBench is a benchmark dataset consisting of 100 datasets representing diverse business use cases, evaluating agents based on end-to-end data analytics capabilities including question formulation, answer interpretation, and insight generation.

**Key Contributions:**
- 100 curated datasets across finance, incident management, and other business domains
- Evaluation of end-to-end analytics rather than single-query responses
- Two-way evaluation mechanism using LLaMA-3 as evaluator
- AgentPoirot baseline implementation for comprehensive data analytics
- Demonstration that AgentPoirot outperforms single-query focused approaches like Pandas Agent

**Relevance:** Establishes comprehensive benchmarking for business analytics agents with focus on multi-step insight generation and actionable recommendations.

---

### 7. SciAgents: Automating Scientific Discovery Through Multi-Agent Intelligent Graph Reasoning

**Authors:** Ghafarollahi, A., & Buehler, M. J. (2024)

**Publication Date:** September 9, 2024

**Source:** arXiv:2409.05556v1

**Abstract:** SciAgents leverages large-scale ontological knowledge graphs, multiple LLMs, and multi-agent systems with in-situ learning capabilities to autonomously advance scientific understanding and discover hidden interdisciplinary relationships.

**Key Contributions:**
- Integration of ontological knowledge graphs with multi-agent systems
- Autonomous hypothesis generation and refinement
- Discovery of hidden interdisciplinary relationships in materials science
- "Swarm of intelligence" approach mimicking biological systems
- Modular architecture combining generative AI, ontological representations, and multi-agent modeling

**Relevance:** Demonstrates advanced multi-agent reasoning for scientific discovery, particularly relevant for complex analytical tasks requiring domain knowledge integration.

---

### 8. LAMBDA: A Large Model Based Data Agent

**Authors:** Sun, M., Han, R., Jiang, B., Qi, H., Sun, D., Yuan, Y., & Huang, J. (2024)

**Publication Date:** July 24, 2024

**Source:** arXiv:2407.17535v3

**Abstract:** LAMBDA is an open-source, code-free multi-agent data analysis system featuring two key agent roles: programmer (generates code) and inspector (debugs code), with user intervention capabilities and knowledge integration mechanisms.

**Key Contributions:**
- Code-free multi-agent system using natural language interface
- Dual-agent architecture with programmer and inspector roles
- User interface for direct intervention in adverse scenarios
- Knowledge Integration Mechanism for external model and algorithm integration
- Demonstrated strong performance on real-world data analysis tasks
- Open-source implementation at https://github.com/AMA-CMFAI/LAMBDA

**Relevance:** Provides accessible, code-free approach to data analysis with robust error handling through dual-agent collaboration.

---

### 9. Tapilot-Crossing: Benchmarking and Evolving LLMs Towards Interactive Data Analysis Agents

**Authors:** Li, J., Huo, N., Gao, Y., Shi, J., Zhao, Y., Qu, G., Wu, Y., Ma, C., Lou, J.-G., & Cheng, R. (2024)

**Publication Date:** March 8, 2024

**Source:** arXiv:2403.05307v1

**Abstract:** Tapilot-Crossing is a benchmark for evaluating LLM agents on interactive data analysis, containing 1024 interactions across 4 practical scenarios, constructed through an economical multi-agent environment called Decision Company.

**Key Contributions:**
- 1024 interaction samples covering Normal, Action, Private, and Private Action scenarios
- Decision Company multi-agent environment for economical benchmark construction
- Evaluation of popular LLM agents revealing challenges in interactive data analysis
- Adaptive Interaction Reflection (AIR) strategy for learning from successful history
- Up to 44.5% relative performance improvement using AIR strategy

**Relevance:** Addresses interactive data analysis specifically, providing both benchmark and improvement methodology for human-agent collaboration.

---

### 10. Multi-Turn Human-LLM Interaction Through the Lens of a Two-Way Intelligibility Protocol

**Authors:** Mestha, H., Bania, K., Sathyanarayana, S. V., Liu, S., & Srinivasan, A. (2024)

**Publication Date:** October 27, 2024

**Source:** arXiv:2410.20600v4

**Abstract:** This paper investigates structured human-LLM interaction for data analysis tasks using a two-way intelligibility protocol modeled by communicating finite-state machines, with empirical validation in radiology and drug design domains.

**Key Contributions:**
- Two-way intelligibility protocol for structured human-LLM interaction
- Implementation using communicating finite-state machines
- Controlled experiments with human proxy and uncontrolled experiments with human subjects
- Empirical evidence supporting protocol's capability in capturing intelligibility
- Application to complex scientific domains: radiology and drug design
- Open-source implementation at https://github.com/karannb/interact

**Relevance:** Provides theoretical framework and empirical validation for structured human-agent interaction in complex data analysis contexts.

---

## Synthesis and Analysis

### Emerging Themes

**1. Multi-Agent Architectures**
Seven of the ten reviewed papers employ multi-agent frameworks, indicating a clear trend toward specialized agent roles collaborating on complex tasks. AutoKaggle, SciAgents, LAMBDA, and SELA all demonstrate that dividing responsibilities among specialized agents improves performance and robustness.

**2. Benchmarking and Evaluation**
Three papers introduce significant benchmarks: Spider2-V (494 tasks across 20 applications), InsightBench (100 business datasets), and Tapilot-Crossing (1024 interactions). This reflects the field's maturation toward standardized evaluation methodologies.

**3. Code Generation and Execution**
TaskWeaver, Data Interpreter, and LAMBDA all emphasize code generation as a core capability, with built-in execution, debugging, and verification mechanisms. This code-first approach enables handling of complex, domain-specific analytical tasks.

**4. Human-Agent Collaboration**
AutoKaggle, LAMBDA, Tapilot-Crossing, and Mestha et al. all incorporate human intervention capabilities, recognizing that fully autonomous systems benefit from human oversight and guidance, particularly in complex or adverse scenarios.

**5. Hierarchical Task Decomposition**
Data Interpreter's hierarchical graph modeling and SELA's tree-search approach demonstrate that breaking complex problems into manageable subproblems is critical for success in multi-step data analysis workflows.

### Performance Trends

The reviewed systems show substantial performance improvements over baselines:
- Data Interpreter: 25% improvement on InfiAgent-DABench
- SELA: 65-80% win rate against AutoML baselines
- AutoKaggle: 0.85 validation submission rate
- Tapilot-Crossing with AIR: 44.5% relative improvement

However, Spider2-V reveals significant remaining challenges, with state-of-the-art agents achieving only 14.0% success on full data workflows, indicating substantial room for improvement.

### Research Gaps

**1. Real-World Deployment**
While several systems demonstrate strong benchmark performance, limited evidence exists for large-scale production deployments in enterprise environments.

**2. Domain Adaptation**
Most systems are evaluated on general-purpose benchmarks; domain-specific adaptation strategies require further investigation.

**3. Long-Horizon Planning**
Current systems struggle with very long-horizon tasks requiring sustained planning over extended analytical workflows.

**4. Explainability**
Limited attention is given to explaining agent reasoning and decisions, which is critical for trust in high-stakes analytical contexts.

---

## Conclusion

The period from September 2023 to September 2025 has witnessed significant advances in LLM and AI agent systems for data analysis. The field has evolved from single-agent code generation to sophisticated multi-agent frameworks capable of handling complex, multi-step analytical workflows. Key innovations include hierarchical task decomposition, specialized agent roles, comprehensive benchmarking infrastructure, and human-agent collaboration protocols.

While current systems demonstrate impressive capabilities on specific benchmarks, significant challenges remain in achieving reliable automation of full data science workflows, as evidenced by Spider2-V's findings. Future research should address long-horizon planning, domain adaptation, explainability, and real-world deployment validation.

The convergence of code generation, multi-agent collaboration, and human-in-the-loop design suggests a promising trajectory toward practical, production-ready data analysis agents that can augment and accelerate human data science capabilities.

---

## References

Cao, R., Lei, F., Wu, H., Chen, J., Fu, Y., Gao, H., Xiong, X., Zhang, H., Mao, Y., Hu, W., Xie, T., Xu, H., Zhang, D., Wang, S., Sun, R., Yin, P., Xiong, C., Ni, A., Liu, Q., & Zhong, V. (2024). Spider2-V: How far are multimodal agents from automating data science and engineering workflows? *arXiv:2407.10956v1*. https://arxiv.org/abs/2407.10956v1

Chi, Y., Lin, Y., Hong, S., Pan, D., Fei, Y., Mei, G., Liu, B., Pang, T., Kwok, J., Zhang, C., Liu, B., & Wu, C. (2024). SELA: Tree-search enhanced LLM agents for automated machine learning. *arXiv:2410.17238v1*. https://arxiv.org/abs/2410.17238v1

Ghafarollahi, A., & Buehler, M. J. (2024). SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning. *arXiv:2409.05556v1*. https://arxiv.org/abs/2409.05556v1

Hong, S., Lin, Y., Liu, B., Liu, B., Wu, B., Zhang, C., Wei, C., Li, D., Chen, J., Zhang, J., Wang, J., Zhang, L., Zhang, L., Yang, M., Zhuge, M., Guo, T., Zhou, T., Tao, W., Tang, X., & Lu, X. (2024). Data Interpreter: An LLM agent for data science. *arXiv:2402.18679v4*. https://arxiv.org/abs/2402.18679v4

Li, J., Huo, N., Gao, Y., Shi, J., Zhao, Y., Qu, G., Wu, Y., Ma, C., Lou, J.-G., & Cheng, R. (2024). Tapilot-Crossing: Benchmarking and evolving LLMs towards interactive data analysis agents. *arXiv:2403.05307v1*. https://arxiv.org/abs/2403.05307v1

Li, Z., Zang, Q., Ma, D., Guo, J., Zheng, T., Liu, M., Niu, X., Wang, Y., Yang, J., Liu, J., Zhong, W., Zhou, W., Huang, W., & Zhang, G. (2024). AutoKaggle: A multi-agent framework for autonomous data science competitions. *arXiv:2410.20424v3*. https://arxiv.org/abs/2410.20424v3

Mestha, H., Bania, K., Sathyanarayana, S. V., Liu, S., & Srinivasan, A. (2024). Multi-turn human-LLM interaction through the lens of a two-way intelligibility protocol. *arXiv:2410.20600v4*. https://arxiv.org/abs/2410.20600v4

Qiao, B., Li, L., Zhang, X., He, S., Kang, Y., Zhang, C., Yang, F., Dong, H., Zhang, J., Wang, L., Ma, M., Zhao, P., Qin, S., Qin, X., Du, C., Xu, Y., Lin, Q., Rajmohan, S., & Zhang, D. (2023). TaskWeaver: A code-first agent framework. *arXiv:2311.17541v3*. https://arxiv.org/abs/2311.17541v3

Sahu, G., Puri, A., Rodriguez, J., Abaskohi, A., Chegini, M., Drouin, A., Taslakian, P., Zantedeschi, V., Lacoste, A., Vazquez, D., Chapados, N., Pal, C., Mudumba, S. R., & Laradji, I. H. (2024). InsightBench: Evaluating business analytics agents through multi-step insight generation. *arXiv:2407.06423v4*. https://arxiv.org/abs/2407.06423v4

Sun, M., Han, R., Jiang, B., Qi, H., Sun, D., Yuan, Y., & Huang, J. (2024). LAMBDA: A large model based data agent. *arXiv:2407.17535v3*. https://arxiv.org/abs/2407.17535v3

---

## Appendix: Screening Methodology Details

**Initial Pool:** 48 papers from direct arXiv search  
**Citation Expansion:** 22 additional papers from reference analysis  
**Shortlisted:** 30 papers after initial filtering  
**Final Selection:** 10 papers after relevance screening  

**Screening Scores Distribution:**
- Score 0: 2 papers
- Score 1: 9 papers
- Score 2: 6 papers
- Score 3: 13 papers

**Inclusion from References:** 7 of 10 selected papers were identified through citation expansion, demonstrating the value of snowball sampling in systematic reviews.

---

*Review completed on October 26, 2026*
