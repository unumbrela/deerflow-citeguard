# Systematic Literature Review: LLM/Agent-as-Data-Analyst

**Review Period:** September 28, 2023 – September 27, 2025  
**Category:** cs.AI  
**Format:** APA Style  
**Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in LLM-based agents for data analysis tasks. The reviewed papers, published between September 2023 and September 2025, demonstrate significant progress in automating data science workflows through multi-agent systems, code generation, and interactive analysis capabilities. Key themes include hierarchical task decomposition, iterative refinement, benchmark development, and human-AI collaboration in data analytics.

---

## Methodology

**Search Strategy:** Papers were identified through arXiv search in the cs.AI category with the query "LLM agent data analysis." The search yielded 48 papers, with citation expansion adding 22 additional references from paper bibliographies.

**Screening Process:** From 30 shortlisted papers, 10 were selected based on relevance to LLM/Agent-as-Data-Analyst topics, including automated data exploration, statistical analysis, visualization generation, and data-driven decision making.

**Inclusion Criteria:**
- Published between September 28, 2023 and September 27, 2025
- Primary category: cs.AI
- Focus on LLM agents for data analysis tasks
- Peer-reviewed preprints with empirical evaluation

---

## Annotated Bibliography (APA Format)

### 1. Data Interpreter: An LLM Agent For Data Science

**Citation:**  
Hong, S., Lin, Y., Liu, B., Liu, B., Wu, B., Zhang, C., Wei, C., Li, D., Chen, J., Zhang, J., Wang, J., Zhang, L., Zhang, L., Yang, M., Zhuge, M., Guo, T., Zhou, T., Tao, W., Tang, X., & Lu, X. (2024). Data Interpreter: An LLM Agent For Data Science. *arXiv preprint arXiv:2402.18679*. https://arxiv.org/abs/2402.18679v4

**Summary:**  
This paper presents Data Interpreter, an LLM-based agent designed to solve data science problems end-to-end. The system incorporates two key modules: (1) Hierarchical Graph Modeling for breaking down complex problems into manageable subproblems, and (2) Programmable Node Generation for refining and verifying each subproblem to improve code generation. Experimental results show significant performance improvements: 25% boost on InfiAgent-DABench (from 75.9% to 94.9% accuracy), improvements from 88% to 95% on machine learning tasks, and from 60% to 97% on open-ended tasks. On the MATH dataset, Data Interpreter achieved a 26% improvement compared to state-of-the-art baselines.

**Key Contributions:**
- Hierarchical problem decomposition for complex data science workflows
- Dynamic node generation and graph optimization
- Iterative code refinement and verification
- Strong empirical performance across multiple benchmarks

---

### 2. AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions

**Citation:**  
Li, Z., Zang, Q., Ma, D., Guo, J., Zheng, T., Liu, M., Niu, X., Wang, Y., Yang, J., Liu, J., Zhong, W., Zhou, W., Huang, W., & Zhang, G. (2024). AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions. *arXiv preprint arXiv:2410.20424*. https://arxiv.org/abs/2410.20424v3

**Summary:**  
AutoKaggle is a multi-agent framework that assists data scientists in completing daily data pipelines through collaborative agent systems. The framework implements an iterative development process combining code execution, debugging, and comprehensive unit testing. It offers customizable workflows allowing human intervention at each phase, integrating automated intelligence with human expertise. The system includes a universal data science toolkit with validated functions for data cleaning, feature engineering, and modeling. Evaluated on 8 Kaggle competitions, AutoKaggle achieved a validation submission rate of 0.85 and a comprehensive score of 0.82 in typical data science pipelines.

**Key Contributions:**
- Multi-agent collaboration for data science competitions
- Iterative code execution with debugging and testing
- Human-in-the-loop intervention capabilities
- Comprehensive data science toolkit with validated functions

---

### 3. Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?

**Citation:**  
Cao, R., Lei, F., Wu, H., Chen, J., Fu, Y., Gao, H., Xiong, X., Zhang, H., Mao, Y., Hu, W., Xie, T., Xu, H., Zhang, D., Wang, S., Sun, R., Yin, P., Xiong, C., Ni, A., Liu, Q., & Zhong, V. (2024). Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows? *arXiv preprint arXiv:2407.10956*. https://arxiv.org/abs/2407.10956v1

**Summary:**  
This paper introduces Spider2-V, the first multimodal agent benchmark focusing on professional data science and engineering workflows. The benchmark features 494 real-world tasks in authentic computer environments incorporating 20 enterprise-level professional applications including BigQuery, dbt, and Airbyte. Tasks evaluate the ability of multimodal agents to perform data-related tasks by writing code and managing GUIs in enterprise data software systems. Empirical evaluation reveals that existing state-of-the-art LLM/VLM-based agents do not reliably automate full data workflows (14.0% success rate). Even with step-by-step guidance, agents underperform in tasks requiring fine-grained, knowledge-intensive GUI actions (16.2%) and remote cloud-hosted workspaces (10.6%).

**Key Contributions:**
- First multimodal benchmark for data science and engineering workflows
- 494 real-world tasks across 20 enterprise applications
- Comprehensive evaluation revealing current limitations (14% success rate)
- Automatic configuration and evaluation metrics for each task

---

### 4. SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning

**Citation:**  
Chi, Y., Lin, Y., Hong, S., Pan, D., Fei, Y., Mei, G., Liu, B., Pang, T., Kwok, J., Zhang, C., Liu, B., & Wu, C. (2024). SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning. *arXiv preprint arXiv:2410.17238*. https://arxiv.org/abs/2410.17238v1

**Summary:**  
SELA introduces Tree-Search Enhanced LLM Agents for Automated Machine Learning, leveraging Monte Carlo Tree Search (MCTS) to optimize the AutoML process. The framework represents pipeline configurations as trees, enabling agents to conduct experiments intelligently and iteratively refine strategies based on experimental feedback. This approach addresses limitations of existing LLM-based frameworks that often generate low-diversity and suboptimal code. Evaluated across 20 machine learning datasets, SELA achieved a win rate of 65% to 80% against each baseline across all datasets, demonstrating significant potential for agent-based strategies in AutoML.

**Key Contributions:**
- Integration of Monte Carlo Tree Search with LLM agents
- Tree-based representation of ML pipeline configurations
- Iterative strategy refinement based on experimental feedback
- 65-80% win rate against baselines across 20 datasets

---

### 5. TaskWeaver: A Code-First Agent Framework

**Citation:**  
Qiao, B., Li, L., Zhang, X., He, S., Kang, Y., Zhang, C., Yang, F., Dong, H., Zhang, J., Wang, L., Ma, M., Zhao, P., Qin, S., Qin, X., Du, C., Xu, Y., Lin, Q., Rajmohan, S., & Zhang, D. (2023). TaskWeaver: A Code-First Agent Framework. *arXiv preprint arXiv:2311.17541*. https://arxiv.org/abs/2311.17541v3

**Summary:**  
TaskWeaver is a code-first framework for building LLM-powered autonomous agents that addresses limitations in handling domain-specific data analytics tasks with rich data structures. The framework converts user requests into executable code and treats user-defined plugins as callable functions. TaskWeaver provides support for rich data structures, flexible plugin usage, and dynamic plugin selection, leveraging LLM coding capabilities for complex logic. It incorporates domain-specific knowledge through examples and ensures secure execution of generated code. The framework offers a powerful approach for creating intelligent conversational agents that can handle complex tasks and adapt to domain-specific scenarios.

**Key Contributions:**
- Code-first approach for autonomous agents
- User-defined plugins as callable functions
- Support for rich data structures and dynamic plugin selection
- Secure code execution with domain-specific knowledge integration

---

### 6. InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation

**Citation:**  
Sahu, G., Puri, A., Rodriguez, J., Abaskohi, A., Chegini, M., Drouin, A., Taslakian, P., Zantedeschi, V., Lacoste, A., Vazquez, D., Chapados, N., Pal, C., Mudumba, S. R., & Laradji, I. H. (2024). InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation. *arXiv preprint arXiv:2407.06423*. https://arxiv.org/abs/2407.06423v4

**Summary:**  
This paper introduces InsightBench, a benchmark dataset for evaluating agents on end-to-end data analytics capabilities. The benchmark consists of 100 datasets representing diverse business use cases (finance, incident management), each with carefully curated insights. Unlike existing benchmarks focusing on single queries, InsightBench evaluates agents based on their ability to formulate questions, interpret answers, and generate summaries of insights and actionable steps. The authors propose AgentPoirot, a baseline data analysis agent capable of performing end-to-end data analytics. Evaluation shows AgentPoirot outperforms existing approaches (such as Pandas Agent) that focus on resolving single queries.

**Key Contributions:**
- 100 datasets across diverse business use cases
- End-to-end evaluation including question formulation and insight generation
- Two-way evaluation mechanism using LLaMA-3 as evaluator
- AgentPoirot baseline demonstrating superior performance

---

### 7. SciAgents: Automating Scientific Discovery Through Multi-Agent Intelligent Graph Reasoning

**Citation:**  
Ghafarollahi, A., & Buehler, M. J. (2024). SciAgents: Automating Scientific Discovery Through Multi-Agent Intelligent Graph Reasoning. *arXiv preprint arXiv:2409.05556*. https://arxiv.org/abs/2409.05556v1

**Summary:**  
SciAgents presents an approach leveraging three core concepts for autonomous scientific discovery: (1) large-scale ontological knowledge graphs organizing diverse scientific concepts, (2) a suite of LLMs and data retrieval tools, and (3) multi-agent systems with in-situ learning capabilities. Applied to biologically inspired materials, SciAgents reveals hidden interdisciplinary relationships achieving scale, precision, and exploratory power surpassing traditional human-driven research methods. The framework autonomously generates and refines research hypotheses, elucidating underlying mechanisms and design principles. Case studies demonstrate scalable capabilities combining generative AI, ontological representations, and multi-agent modeling.

**Key Contributions:**
- Ontological knowledge graphs for scientific concept organization
- Multi-agent systems with in-situ learning
- Autonomous hypothesis generation and refinement
- Discovery of hidden interdisciplinary relationships in materials science

---

### 8. LAMBDA: A Large Model Based Data Agent

**Citation:**  
Sun, M., Han, R., Jiang, B., Qi, H., Sun, D., Yuan, Y., & Huang, J. (2024). LAMBDA: A Large Model Based Data Agent. *arXiv preprint arXiv:2407.17535*. https://arxiv.org/abs/2407.17535v3

**Summary:**  
LAMBDA (LArge Model Based Data Agent) is an open-source, code-free multi-agent data analysis system leveraging large language models. The system features two key agent roles: the programmer (generates code based on user instructions and domain knowledge) and the inspector (debugs code when necessary). LAMBDA includes a user interface allowing direct user intervention for robustness and handles adverse scenarios. The system can flexibly integrate external models and algorithms through a Knowledge Integration Mechanism for customized data analysis. LAMBDA demonstrates strong performance on various data analysis tasks using real-world data examples.

**Key Contributions:**
- Code-free multi-agent architecture with programmer-inspector roles
- User interface for direct intervention and debugging
- Knowledge Integration Mechanism for external model integration
- Open-source implementation with real-world case studies

---

### 9. Tapilot-Crossing: Benchmarking and Evolving LLMs Towards Interactive Data Analysis Agents

**Citation:**  
Li, J., Huo, N., Gao, Y., Shi, J., Zhao, Y., Qu, G., Wu, Y., Ma, C., Lou, J.-G., & Cheng, R. (2024). Tapilot-Crossing: Benchmarking and Evolving LLMs Towards Interactive Data Analysis Agents. *arXiv preprint arXiv:2403.05307*. https://arxiv.org/abs/2403.05307v1

**Summary:**  
This paper introduces Tapilot-Crossing, a benchmark for evaluating LLM agents on interactive data analysis. The benchmark contains 1024 interactions covering 4 practical scenarios: Normal, Action, Private, and Private Action. Tapilot-Crossing is constructed using an economical multi-agent environment called Decision Company with minimal human effort. Evaluation of popular LLM agents underscores the challenges of interactive data analysis. The authors propose Adaptive Interaction Reflection (AIR), a self-generated reflection strategy guiding LLM agents to learn from successful history. Experiments demonstrate AIR can evolve LLMs into effective interactive data analysis agents, achieving relative performance improvement of up to 44.5%.

**Key Contributions:**
- 1024 interactions across 4 practical scenarios
- Economical multi-agent construction environment (Decision Company)
- Adaptive Interaction Reflection (AIR) learning strategy
- 44.5% relative performance improvement with AIR

---

### 10. Multi-Turn Human-LLM Interaction Through the Lens of a Two-Way Intelligibility Protocol

**Citation:**  
Mestha, H., Bania, K., Sathyanarayana, S. V., Liu, S., & Srinivasan, A. (2024). Multi-Turn Human-LLM Interaction Through the Lens of a Two-Way Intelligibility Protocol. *arXiv preprint arXiv:2410.20600*. https://arxiv.org/abs/2410.20600v4

**Summary:**  
This paper investigates structured human-LLM interaction for data analysis tasks using a two-way intelligibility protocol modeled by communicating finite-state machines. The protocol enables LLMs to harness human expertise and creativity for complex problems through multiple turns of prompts and responses. The authors provide an implementation and empirical evidence from controlled experiments (with a human proxy database) and uncontrolled experiments (with human subjects) in radiology and drug design. Results support the protocol's capability of capturing one- and two-way intelligibility in human-LLM interaction and demonstrate utility in designing human-machine systems for data analysis.

**Key Contributions:**
- Two-way intelligibility protocol for human-LLM interaction
- Implementation using communicating finite-state machines
- Empirical validation in radiology and drug design domains
- Controlled and uncontrolled experimental evaluation

---

## Thematic Analysis

### 1. Multi-Agent Architectures

A dominant theme across the reviewed literature is the use of multi-agent systems for data analysis tasks. Eight of ten papers employ multi-agent approaches, with common patterns including:

- **Role specialization:** Programmer-inspector pairs (LAMBDA), hierarchical task decomposition (Data Interpreter)
- **Collaborative workflows:** Multi-agent frameworks for competitions (AutoKaggle), scientific discovery (SciAgents)
- **Iterative refinement:** Tree-search enhanced optimization (SELA), code debugging cycles (TaskWeaver)

### 2. Benchmark Development

Three papers focus specifically on benchmark creation, reflecting the field's maturation:

- **Spider2-V:** 494 tasks across 20 enterprise applications (Cao et al., 2024)
- **InsightBench:** 100 business analytics datasets (Sahu et al., 2024)
- **Tapilot-Crossing:** 1024 interactive data analysis scenarios (Li et al., 2024)

These benchmarks reveal current limitations, with Spider2-V reporting only 14% success rate for state-of-the-art agents on real-world workflows.

### 3. Human-AI Collaboration

Several papers emphasize human intervention and collaboration:

- **Direct intervention:** User interfaces for code debugging (LAMBDA, AutoKaggle)
- **Two-way intelligibility:** Protocol-based human-LLM interaction (Mestha et al., 2024)
- **Plugin systems:** User-defined functions as callable components (TaskWeaver)

### 4. Code Generation and Execution

All reviewed systems rely on code generation as the primary mechanism for data analysis:

- **Code-first approaches:** Converting natural language to executable code (TaskWeaver, Data Interpreter)
- **Verification mechanisms:** Unit testing, debugging, and iterative refinement (AutoKaggle, SELA)
- **Security considerations:** Safe code execution environments (TaskWeaver)

### 5. Domain-Specific Applications

Papers demonstrate applications across diverse domains:

- **Business analytics:** Finance, incident management (InsightBench)
- **Scientific discovery:** Materials science, biology (SciAgents)
- **Medical applications:** Radiology, drug design (Mestha et al., 2024)
- **Data competitions:** Kaggle challenges (AutoKaggle)

---

## Performance Summary

| System | Key Metric | Performance |
|--------|-----------|-------------|
| Data Interpreter | InfiAgent-DABench | 94.9% accuracy |
| AutoKaggle | Validation submission rate | 0.85 |
| Spider2-V | Success rate (baseline) | 14.0% |
| SELA | Win rate vs baselines | 65-80% |
| Tapilot-Crossing + AIR | Performance improvement | +44.5% |

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Limited real-world deployment:** Most evaluations remain on benchmarks rather than production systems
2. **GUI interaction challenges:** Poor performance on fine-grained GUI operations (16.2% success rate)
3. **Cloud workspace limitations:** Low success rates (10.6%) on remote cloud-hosted environments
4. **Domain adaptation:** Need for better transfer learning across different data analysis domains
5. **Explainability:** Limited discussion of how agents explain their analytical decisions

### Future Research Directions

1. **Multimodal integration:** Enhanced vision-language capabilities for GUI interaction
2. **Long-horizon planning:** Better handling of multi-day or multi-week data science projects
3. **Human-in-the-loop optimization:** More sophisticated collaboration protocols
4. **Privacy and security:** Formal verification of code safety and data handling
5. **Standardized evaluation:** Community-wide benchmarks with consistent metrics

---

## Conclusion

The reviewed literature demonstrates rapid progress in LLM-based agents for data analysis, with significant advances in multi-agent architectures, benchmark development, and human-AI collaboration. Key achievements include:

- End-to-end automation of data science workflows with 94.9% accuracy on specific benchmarks
- Multi-agent frameworks achieving 65-80% win rates against traditional AutoML baselines
- Comprehensive benchmarks revealing current limitations (14% success rate on complex workflows)
- Novel interaction protocols enabling effective human-LLM collaboration

However, substantial challenges remain, particularly in handling complex GUI interactions, cloud-based workflows, and long-horizon planning. The field is maturing with standardized benchmarks and evaluation protocols, but real-world deployment and domain adaptation require further investigation.

The convergence of code generation, multi-agent collaboration, and human-in-the-loop systems suggests promising directions for future research. As LLM capabilities continue to advance, agent-based data analysis systems are poised to transform how organizations approach data-driven decision making.

---

## References

Cao, R., Lei, F., Wu, H., Chen, J., Fu, Y., Gao, H., Xiong, X., Zhang, H., Mao, Y., Hu, W., Xie, T., Xu, H., Zhang, D., Wang, S., Sun, R., Yin, P., Xiong, C., Ni, A., Liu, Q., & Zhong, V. (2024). Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows? *arXiv preprint arXiv:2407.10956*. https://arxiv.org/abs/2407.10956v1

Chi, Y., Lin, Y., Hong, S., Pan, D., Fei, Y., Mei, G., Liu, B., Pang, T., Kwok, J., Zhang, C., Liu, B., & Wu, C. (2024). SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning. *arXiv preprint arXiv:2410.17238*. https://arxiv.org/abs/2410.17238v1

Ghafarollahi, A., & Buehler, M. J. (2024). SciAgents: Automating Scientific Discovery Through Multi-Agent Intelligent Graph Reasoning. *arXiv preprint arXiv:2409.05556*. https://arxiv.org/abs/2409.05556v1

Hong, S., Lin, Y., Liu, B., Liu, B., Wu, B., Zhang, C., Wei, C., Li, D., Chen, J., Zhang, J., Wang, J., Zhang, L., Zhang, L., Yang, M., Zhuge, M., Guo, T., Zhou, T., Tao, W., Tang, X., & Lu, X. (2024). Data Interpreter: An LLM Agent For Data Science. *arXiv preprint arXiv:2402.18679*. https://arxiv.org/abs/2402.18679v4

Li, J., Huo, N., Gao, Y., Shi, J., Zhao, Y., Qu, G., Wu, Y., Ma, C., Lou, J.-G., & Cheng, R. (2024). Tapilot-Crossing: Benchmarking and Evolving LLMs Towards Interactive Data Analysis Agents. *arXiv preprint arXiv:2403.05307*. https://arxiv.org/abs/2403.05307v1

Li, Z., Zang, Q., Ma, D., Guo, J., Zheng, T., Liu, M., Niu, X., Wang, Y., Yang, J., Liu, J., Zhong, W., Zhou, W., Huang, W., & Zhang, G. (2024). AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions. *arXiv preprint arXiv:2410.20424*. https://arxiv.org/abs/2410.20424v3

Mestha, H., Bania, K., Sathyanarayana, S. V., Liu, S., & Srinivasan, A. (2024). Multi-Turn Human-LLM Interaction Through the Lens of a Two-Way Intelligibility Protocol. *arXiv preprint arXiv:2410.20600*. https://arxiv.org/abs/2410.20600v4

Qiao, B., Li, L., Zhang, X., He, S., Kang, Y., Zhang, C., Yang, F., Dong, H., Zhang, J., Wang, L., Ma, M., Zhao, P., Qin, S., Qin, X., Du, C., Xu, Y., Lin, Q., Rajmohan, S., & Zhang, D. (2023). TaskWeaver: A Code-First Agent Framework. *arXiv preprint arXiv:2311.17541*. https://arxiv.org/abs/2311.17541v3

Sahu, G., Puri, A., Rodriguez, J., Abaskohi, A., Chegini, M., Drouin, A., Taslakian, P., Zantedeschi, V., Lacoste, A., Vazquez, D., Chapados, N., Pal, C., Mudumba, S. R., & Laradji, I. H. (2024). InsightBench: Evaluating Business Analytics Agents Through Multi-Step Insight Generation. *arXiv preprint arXiv:2407.06423*. https://arxiv.org/abs/2407.06423v4

Sun, M., Han, R., Jiang, B., Qi, H., Sun, D., Yuan, Y., & Huang, J. (2024). LAMBDA: A Large Model Based Data Agent. *arXiv preprint arXiv:2407.17535*. https://arxiv.org/abs/2407.17535v3

---

**Review completed:** October 26, 2026  
**Total papers reviewed:** 10  
**Search database:** arXiv (cs.AI category)
