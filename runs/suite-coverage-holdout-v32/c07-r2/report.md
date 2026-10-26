# Systematic Literature Review: LLM/Agent-as-Data-Analyst

**Search Parameters:**
- **Database:** arXiv
- **Category:** cs.AI (primary)
- **Publication Window:** September 28, 2023 – September 27, 2025
- **Papers Reviewed:** 10

---

## Annotated Bibliography (APA Format)

### 1. Interactive Data Analysis Benchmarks

Li, J., Huo, N., Gao, Y., Shi, J., Zhao, Y., Qu, G., Wu, Y., Ma, C., Lou, J.-G., & Cheng, R. (2024). *Tapilot-Crossing: Benchmarking and Evolving LLMs Towards Interactive Data Analysis Agents*. arXiv. https://arxiv.org/abs/2403.05307v1

**Summary:** This paper introduces Tapilot-Crossing, a benchmark with 1,024 interactions across 4 practical scenarios (Normal, Action, Private, Private Action) for evaluating LLM agents in interactive data analysis. The benchmark is constructed using an economical multi-agent environment called "Decision Company" with minimal human effort. The authors propose Adaptive Interaction Reflection (AIR), a self-generated reflection strategy that guides LLM agents to learn from successful history, achieving up to 44.5% relative performance improvement.

**Key Contributions:** Benchmark creation methodology, AIR strategy for agent evolution, evaluation of popular LLM agents on interactive data analysis tasks.

---

### 2. Human-LLM Interaction Protocols

Mestha, H., Bania, K., Sathyanarayana, S. V., Liu, S., & Srinivasan, A. (2024). *Multi-Turn Human-LLM Interaction Through the Lens of a Two-Way Intelligibility Protocol*. arXiv. https://arxiv.org/abs/2410.20600v4

**Summary:** This work investigates structured human-LLM interaction for data analysis tasks using a "two-way intelligibility" protocol modeled by communicating finite-state machines. The implementation was empirically validated in radiology and drug design domains through controlled experiments with human proxies and uncontrolled experiments with human subjects. Results support the protocol's capability to capture one- and two-way intelligibility in human-LLM interaction.

**Key Contributions:** Formal protocol for human-LLM interaction, empirical validation in scientific domains, evidence for two-way intelligibility in human-machine systems.

---

### 3. Data Science Agent Evaluation

Zhang, Y., Jiang, Q., Han, X., Chen, N., Yang, Y., & Ren, K. (2024). *Benchmarking Data Science Agents*. arXiv. https://arxiv.org/abs/2402.17168v1

**Summary:** This paper introduces DSEval, a novel evaluation paradigm and benchmark suite for assessing LLM-based data science agents throughout the entire data science lifecycle. The authors incorporate a bootstrapped annotation method that streamlines dataset preparation, improves evaluation coverage, and expands benchmarking comprehensiveness. Findings reveal prevalent obstacles in current data science agents and provide critical insights for future advancements.

**Key Contributions:** DSEval evaluation framework, bootstrapped annotation method, comprehensive benchmarks for data science lifecycle.

---

### 4. GUI Agents Survey

Zhang, C., He, S., Qian, J., Li, B., Li, L., Qin, S., Kang, Y., Ma, M., Liu, G., Lin, Q., Rajmohan, S., Zhang, D., & Zhang, Q. (2024). *Large Language Model-Brained GUI Agents: A Survey*. arXiv. https://arxiv.org/abs/2411.18279v12

**Summary:** This comprehensive survey explores LLM-brained GUI agents capable of interpreting complex GUI elements and autonomously executing actions based on natural language instructions. The paper covers historical evolution, core components, advanced techniques, existing frameworks, data collection for training, large action models, and evaluation metrics. Applications span web navigation, mobile app interactions, and desktop automation.

**Key Contributions:** Structured taxonomy of GUI agents, research roadmap, identification of key research gaps, consolidation of foundational knowledge and state-of-the-art developments.

---

### 5. Financial Analysis Agent

Han, S., Zhang, J., Shen, Y., Yan, K., & Li, H. (2025). *FinSphere, a Real-Time Stock Analysis Agent Powered by Instruction-Tuned LLMs and Domain Tools*. arXiv. https://arxiv.org/abs/2501.12399v2

**Summary:** This paper addresses two critical limitations of financial LLMs: absence of objective evaluation metrics and lack of depth in stock analysis. The authors introduce FinSphere with three contributions: (1) AnalyScore evaluation framework, (2) Stocksis dataset curated by industry experts, and (3) FinSphere agent that generates high-quality stock analysis reports. The integrated framework combines real-time data feeds, quantitative tools, and instruction-tuned LLMs.

**Key Contributions:** AnalyScore framework, Stocksis dataset, FinSphere agent architecture, superior performance over general and domain-specific LLMs.

---

### 6. Scientific Data Analysis Agent

Xiao, Y., Liu, J., Zheng, Y., Xie, X., Hao, J., Li, M., Wang, R., Ni, F., Li, Y., Luo, J., Jiao, S., & Peng, J. (2024). *CellAgent: An LLM-driven Multi-Agent Framework for Automated Single-cell Data Analysis*. arXiv. https://arxiv.org/abs/2407.09811v1

**Summary:** CellAgent is an LLM-driven multi-agent framework for automated single-cell RNA sequencing data analysis. The framework constructs three LLM-driven biological expert roles (planner, executor, evaluator) with specific responsibilities, coordinated through a hierarchical decision-making mechanism. A self-iterative optimization mechanism enables autonomous evaluation and optimization of solutions. Evaluation on comprehensive benchmark datasets shows CellAgent effectively identifies suitable tools and hyperparameters.

**Key Contributions:** Multi-agent framework for scientific data analysis, hierarchical decision-making, self-iterative optimization, "Agent for Science" paradigm.

---

### 7. Urban Mobility Agent

Wang, J., Jiang, R., Yang, C., Wu, Z., Onizuka, M., Shibasaki, R., Koshizuka, N., & Xiao, C. (2024). *Large Language Models as Urban Residents: An LLM Agent Framework for Personal Mobility Generation*. arXiv. https://arxiv.org/abs/2402.14744v3

**Summary:** This pioneering work designs an LLM agent framework for activity generation based on real-world human activity data. The framework addresses three research questions: aligning LLMs with real-world urban mobility data, developing reliable activity generation strategies, and exploring LLM applications in urban mobility. Key technical contributions include a self-consistency approach for alignment and a retrieval-augmented strategy for interpretable activity generation.

**Key Contributions:** LLM agent framework for urban mobility, self-consistency alignment approach, retrieval-augmented generation for personal mobility.

---

### 8. Cloud-Native Systems Analysis

Zhang, X., Wang, Q., Li, M., Yuan, Y., Xiao, M., Zhuang, F., & Yu, D. (2025). *TAMO: Fine-Grained Root Cause Analysis via Tool-Assisted LLM Agent with Multi-Modality Observation Data in Cloud-Native Systems*. arXiv. https://arxiv.org/abs/2504.20462v5

**Summary:** TAMO addresses three key challenges in LLM-driven root cause analysis for cloud-native systems: multi-modality input constraint, context window limitation, and dynamic dependence graph. The tool-assisted LLM agent includes multimodality alignment tool, root cause localization tool, and fault types classification tool. TAMO unifies multi-modal observation data into time-aligned representations and overcomes LLM limitations in processing real-time raw observational data.

**Key Contributions:** Tool-assisted LLM agent architecture, multi-modality alignment, structured prompt design for system context, superior performance on benchmark datasets.

---

### 9. Structured Reasoning Agent

Sundar, S., Satheesan, P., & Avadhanam, U. (2025). *I2I-STRADA -- Information to Insights via Structured Reasoning Agent for Data Analysis*. arXiv. https://arxiv.org/abs/2507.17874v1

**Summary:** I2I-STRADA addresses the oversight of structured reasoning processes in existing agentic systems for data analysis. While current systems manage query translation, data transformation, and visualization, they lack consistent cognitive workflows. I2I-STRADA formalizes the reasoning process through modular sub-tasks reflecting analytical thinking: interpreting vague goals, grounding in contextual knowledge, constructing abstract plans, and adapting execution based on intermediate outcomes.

**Key Contributions:** Structured cognitive workflow formalization, modular sub-task architecture, superior performance on DABstep and DABench benchmarks in planning coherence and insight alignment.

---

### 10. Semiconductor Failure Analysis Agent

Dobrovsky, A., Schekotihin, K., & Burmer, C. (2025). *Intelligent Assistants for the Semiconductor Failure Analysis with LLM-Based Planning Agents*. arXiv. https://arxiv.org/abs/2506.15567v3

**Summary:** This paper investigates agentic AI systems for semiconductor failure analysis using LLM-based Planning Agents (LPA). The LPA integrates LLMs with advanced planning capabilities and external tool utilization, enabling autonomous processing of complex queries, retrieval of relevant data from external systems, and generation of human-readable responses. The system orchestrates multiple AI components into cohesive workflows that seamlessly integrate with the failure analysis process.

**Key Contributions:** LPA architecture for failure analysis, orchestration of multiple AI components, operational effectiveness in knowledge-intensive processes.

---

## Synthesis and Thematic Analysis

### Emerging Themes

**1. Benchmarking and Evaluation Frameworks**
Three papers focus on creating evaluation frameworks: Tapilot-Crossing (Li et al., 2024), DSEval (Zhang et al., 2024), and AnalyScore (Han et al., 2025). This indicates the field's maturation from proof-of-concept to systematic evaluation, with emphasis on interactive scenarios, complete data science lifecycles, and domain-specific quality metrics.

**2. Multi-Agent Architectures**
Multiple papers employ multi-agent frameworks with specialized roles: CellAgent's planner-executor-evaluator triad (Xiao et al., 2024), Decision Company's multi-agent environment (Li et al., 2024), and I2I-STRADA's modular sub-tasks (Sundar et al., 2025). This reflects recognition that complex data analysis requires decomposed expertise rather than monolithic agents.

**3. Domain Specialization**
Papers target specific domains: finance (FinSphere), biology (CellAgent), urban planning (Wang et al.), cloud operations (TAMO), and semiconductor manufacturing (Dobrovsky et al.). This specialization addresses the gap between general-purpose LLMs and domain-specific analytical requirements.

**4. Human-Agent Interaction**
Mestha et al. (2024) and Zhang et al. (2024) emphasize structured interaction protocols and GUI-based interfaces, recognizing that effective data analysis requires seamless human-LLM collaboration rather than full automation.

**5. Self-Improvement Mechanisms**
Adaptive Interaction Reflection (Li et al., 2024), self-iterative optimization (Xiao et al., 2024), and self-consistency approaches (Wang et al., 2024) demonstrate the field's focus on agents that learn and improve from their own execution history.

### Research Gaps Identified

1. **Standardized Evaluation:** Despite multiple benchmarks, no unified evaluation framework exists across domains
2. **Real-Time Processing:** Limited work on streaming data and real-time analytical scenarios
3. **Explainability:** Most papers focus on performance over interpretability of agent decisions
4. **Long-Horizon Planning:** Current agents handle multi-step tasks but struggle with extended analytical workflows
5. **Cross-Domain Transfer:** Domain-specific agents show limited generalization capabilities

### Temporal Trends (2024-2025)

- **2024:** Foundation year with benchmark creation and framework proposals
- **2025:** Shift toward specialized applications and structured reasoning mechanisms

The field evolved from establishing evaluation baselines to developing sophisticated, domain-specific agents with formalized reasoning processes.

---

## Conclusion

The literature from September 2023 to September 2025 reveals a rapidly maturing field transitioning from conceptual frameworks to production-ready systems. Key advances include standardized benchmarks, multi-agent architectures, domain specialization, and structured reasoning processes. Future research should address evaluation standardization, real-time processing, explainability, and cross-domain generalization to realize the full potential of LLM/Agent-as-Data-Analyst systems.

---

**Report Generated:** October 26, 2026  
**Search Database:** arXiv  
**Total Papers:** 10  
**Format:** APA Style
