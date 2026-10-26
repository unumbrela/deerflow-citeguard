# Systematic Literature Review: Code Generation with LLM-based Agents

**Date:** October 26, 2026  
**Search Period:** July 31, 2023 – July 30, 2025  
**Category:** cs.SE (Software Engineering)  
**Format:** APA Style

---

## Executive Summary

This systematic literature review examines 10 peer-reviewed papers on code generation with LLM-based agents published between July 2023 and July 2025 in the cs.SE (Software Engineering) category. The review reveals a rapidly evolving field focused on autonomous software engineering agents, with emphasis on agent-computer interfaces, multi-agent collaboration, tool integration, and autonomous program repair. Key findings demonstrate that LLM-based agents can achieve state-of-the-art performance on software engineering benchmarks while raising important questions about complexity versus simplicity in agent design.

---

## Methodology

### Search Strategy

A systematic search was conducted on arXiv for papers matching the query "code generation LLM agents" with the following criteria:
- **Publication Date Range:** July 31, 2023 – July 30, 2025
- **Primary Category:** cs.SE (Software Engineering)
- **Initial Pool:** 50 papers identified
- **Reference Expansion:** 65 additional papers from citations
- **Shortlist:** 30 papers screened
- **Final Selection:** 10 papers based on centrality to code generation with LLM-based agents

### Selection Criteria

Papers were selected based on:
1. Focus on code generation using LLM-based agents
2. Publication within the specified date range
3. Primary classification in software engineering (cs.SE)
4. Contribution to autonomous software engineering capabilities

---

## Selected Papers (APA Format)

### 1. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). *SWE-agent: Agent-Computer interfaces enable automated software engineering*. arXiv preprint arXiv:2405.15793. https://arxiv.org/abs/2405.15793v3

**Key Contributions:** Introduces SWE-agent with custom agent-computer interface (ACI) that enhances LM agents' ability to create/edit code files, navigate repositories, and execute tests. Achieves state-of-the-art performance on SWE-bench (12.5% pass@1) and HumanEvalFix (87.7% pass@1).

**Methodology:** Designed specialized ACI for LM agents, evaluating interface design impact on agent performance through automated software engineering tasks.

---

### 2. RepairAgent: An Autonomous, LLM-Based Agent for Program Repair

Bouzenia, I., Devanbu, P., & Pradel, M. (2024). *RepairAgent: An autonomous, LLM-based agent for program repair*. arXiv preprint arXiv:2403.17134. https://arxiv.org/abs/2403.17134v2

**Key Contributions:** First autonomous LLM-based agent for program repair. Treats LLM as agent capable of autonomously planning and executing actions by invoking tools. Repairs 164 bugs on Defects4J, including 39 previously unfixed bugs.

**Methodology:** Implements dynamically updated prompt format, finite state machine for tool invocation, and interleaved information gathering, repair ingredient collection, and fix validation.

---

### 3. AutoCodeRover: Autonomous Program Improvement

Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). *AutoCodeRover: Autonomous program improvement*. arXiv preprint arXiv:2404.05427. https://arxiv.org/abs/2404.05427v3

**Key Contributions:** Combines LLMs with sophisticated code search using abstract syntax trees and spectrum-based fault localization. Achieves 19% success rate on SWE-bench-lite at $0.43 average cost, exceeding SWE-agent's efficacy with lower cost.

**Methodology:** Works on program representation (AST) rather than file collections, exploits program structure for code search, and uses iterative context retrieval with test-based fault localization.

---

### 4. OpenCodeInterpreter: Integrating Code Generation with Execution and Refinement

Zheng, T., Zhang, G., Shen, T., Liu, X., Lin, B. Y., Fu, J., Chen, W., & Yue, X. (2024). *OpenCodeInterpreter: Integrating code generation with execution and refinement*. arXiv preprint arXiv:2402.14658. https://arxiv.org/abs/2402.14658v3

**Key Contributions:** Introduces open-source code system integrating code generation, execution, and iterative refinement. Supported by Code-Feedback dataset (68K multi-turn interactions). OpenCodeInterpreter-33B achieves 83.2 accuracy on HumanEval/MBPP, rivaling GPT-4's 84.2.

**Methodology:** Integrates execution and human feedback for dynamic code refinement, evaluated on HumanEval, MBPP, and EvalPlus benchmarks.

---

### 5. OpenHands: An Open Platform for AI Software Developers as Generalist Agents

Wang, X., Li, B., Song, Y., Xu, F. F., Tang, X., Zhuge, M., Pan, J., Song, Y., Li, B., Singh, J., Tran, H. H., Li, F., Ma, R., Zheng, M., Qian, B., Shao, Y., Muennighoff, N., Zhang, Y., Hui, B., & Lin, J. (2024). *OpenHands: An open platform for AI software developers as generalist agents*. arXiv preprint arXiv:2407.16741. https://arxiv.org/abs/2407.16741v3

**Key Contributions:** Open platform for AI software developers as generalist agents that write code, interact with command line, and browse web. Supports new agent implementation, sandboxed code execution, multi-agent coordination, and benchmark integration. Evaluated across 15 challenging tasks including SWE-BENCH and WEBARENA.

**Methodology:** Community-driven platform with 2.1K+ contributions from 188+ contributors, released under MIT license.

---

### 6. Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization

Ishibashi, Y., & Nishimura, Y. (2024). *Self-organized agents: A LLM multi-agent framework toward ultra large-scale code generation and optimization*. arXiv preprint arXiv:2404.02183. https://arxiv.org/abs/2404.02183v1

**Key Contributions:** Proposes Self-Organized multi-Agent framework (SoA) for scalable generation of large-scale code. Agents automatically multiply based on problem complexity, enabling indefinite code volume increase while maintaining constant per-agent code management. Surpasses single-agent baseline by 5% in Pass@1 accuracy on HumanEval.

**Methodology:** Multi-agent framework where self-organized agents operate independently on code components while collaborating to construct overall codebase, addressing context length limitations.

---

### 7. CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges

Zhang, K., Li, J., Li, G., Shi, X., & Jin, Z. (2024). *CodeAgent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges*. arXiv preprint arXiv:2401.07339. https://arxiv.org/abs/2401.07339v2

**Key Contributions:** Introduces CodeAgentBench (101 samples from 5 Python projects) for repo-level code generation evaluation. CodeAgent integrates 5 programming tools for information retrieval, code navigation, and testing. Enhances LLM performance by 18.1% to 250%, outperforming GitHub Copilot.

**Methodology:** Implements tool-integrated agent framework with four agent strategies for optimizing tool usage in real-world repository-level coding challenges.

---

### 8. Agentless: Demystifying LLM-based Software Engineering Agents

Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2024). *Agentless: Demystifying LLM-based software engineering agents*. arXiv preprint arXiv:2407.01489. https://arxiv.org/abs/2407.01489v2

**Key Contributions:** Challenges complex agent-based approaches with simplistic three-phase process (localization, repair, validation). Achieves highest performance (32.00%, 96 correct fixes) on SWE-bench Lite at $0.70 cost among all open-source software agents. Questions necessity of complex autonomous agents.

**Methodology:** Employs simple technique without LLM-decided future actions or complex tools, highlighting overlooked potential of interpretable, non-agent approaches.

---

### 9. MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution

Tao, W., Zhou, Y., Wang, Y., Zhang, W., Zhang, H., & Cheng, Y. (2024). *MAGIS: LLM-based multi-agent framework for GitHub issue resolution*. arXiv preprint arXiv:2403.17927. https://arxiv.org/abs/2403.17927v2

**Key Contributions:** Multi-agent framework with four customized agents (Manager, Repository Custodian, Developer, Quality Assurance Engineer) for GitHub issue resolution. Resolves 13.94% of GitHub issues on SWE-bench, eight-fold increase over direct GPT-4 application.

**Methodology:** Empirical study of LLM failure factors in GitHub issue resolution, followed by multi-agent collaboration framework for planning and coding processes.

---

### 10. AgentFL: Scaling LLM-based Fault Localization to Project-Level Context

Qin, Y., Wang, S., Lou, Y., Dong, J., Wang, K., Li, X., & Mao, X. (2024). *AgentFL: Scaling LLM-based fault localization to project-level context*. arXiv preprint arXiv:2403.16362. https://arxiv.org/abs/2403.16362v2

**Key Contributions:** Multi-agent system for automated fault localization at project-level scale. Localizes 157 out of 395 bugs within Top-1 on Defects4J-V1.2.0, outperforming other LLM-based approaches. Costs average $0.074 and 97 seconds per bug.

**Methodology:** Models fault localization as three-step process (comprehension, navigation, confirmation) with specialized agents and auxiliary strategies including Test Behavior Tracking, Document-Guided Search, and Multi-Round Dialogue.

---

## Thematic Analysis

### Theme 1: Agent-Computer Interfaces and Tool Integration

Five papers emphasize the importance of specialized interfaces and tool integration for LLM agents. SWE-agent [1] demonstrates that custom agent-computer interfaces significantly enhance performance. CodeAgent [7] integrates five programming tools for repository-level tasks. OpenCodeInterpreter [4] combines generation with execution capabilities. RepairAgent [2] and AutoCodeRover [3] similarly leverage tool integration for autonomous operation.

### Theme 2: Multi-Agent Collaboration

Four papers explore multi-agent frameworks for complex software engineering tasks. MAGIS [9] employs four specialized agents for GitHub issue resolution. AgentFL [10] uses multi-agent systems for fault localization. Self-Organized Agents [6] enables dynamic agent multiplication based on problem complexity. OpenHands [5] supports coordination between multiple agents.

### Theme 3: Autonomous Program Repair and Improvement

Three papers focus specifically on autonomous program repair. RepairAgent [2] addresses bug fixing through autonomous LLM agents. AutoCodeRover [3] targets program improvement for software maintenance and evolution. AgentFL [10] scales fault localization to project-level contexts.

### Theme 4: Simplicity versus Complexity

A critical debate emerges regarding agent complexity. Agentless [8] challenges the necessity of complex agent architectures, demonstrating that a simple three-phase process can achieve state-of-the-art results. This contrasts with the sophisticated multi-agent frameworks proposed by MAGIS [9], Self-Organized Agents [6], and AgentFL [10].

### Theme 5: Benchmark Performance and Evaluation

All papers employ rigorous benchmark evaluation. SWE-bench appears in five studies [1, 3, 5, 8, 9], HumanEval in four studies [1, 4, 5, 6], and Defects4J in two studies [2, 10]. Performance ranges from 12.5% to 32% on SWE-bench, reflecting diverse approaches and evaluation settings.

---

## Key Findings

### Performance Achievements

1. **Highest SWE-bench Performance:** Agentless achieves 32.00% (96 correct fixes) [8], followed by AutoCodeRover at 19% [3] and SWE-agent at 12.5% [1].

2. **Cost Efficiency:** AgentFL demonstrates lowest cost at $0.074 per bug [10], while AutoCodeRover achieves $0.43 per task [3] and Agentless at $0.70 [8].

3. **Code Generation Accuracy:** OpenCodeInterpreter-33B reaches 83.2 on HumanEval/MBPP, closely rivaling GPT-4's 84.2 [4]. Self-Organized Agents surpasses single-agent baseline by 5% [6].

### Methodological Innovations

1. **Interface Design:** Custom agent-computer interfaces significantly impact agent capabilities [1].

2. **Multi-Agent Architecture:** Specialized agents with distinct roles improve performance on complex tasks [6, 9, 10].

3. **Tool Integration:** Programming tools for navigation, testing, and information retrieval enhance LLM performance by 18.1% to 250% [7].

4. **Program Representation:** Working with AST rather than file collections improves code understanding [3].

### Open Challenges

1. **Context Limitations:** Single agents face context length constraints for large-scale code [6].

2. **Complexity Trade-offs:** Debate continues on whether complex agent architectures are necessary [8].

3. **Repository-Level Tasks:** LLMs show declined performance on real-world repository-level challenges [7].

4. **Cost Considerations:** Token costs range from $0.074 to $0.70 per task, raising scalability questions [2, 3, 8, 10].

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Long-Term Maintenance:** Limited research on agent capabilities for long-term software maintenance beyond initial repair.

2. **Human-Agent Collaboration:** Insufficient exploration of effective human-agent collaboration patterns in software development.

3. **Security Implications:** Minimal attention to security vulnerabilities in agent-generated code.

4. **Cross-Language Generalization:** Most evaluations focus on Python; generalization to other programming languages requires investigation.

### Future Research Directions

1. **Hybrid Approaches:** Combining simple and complex agent strategies based on task requirements.

2. **Learning from Feedback:** Enhanced mechanisms for agents to learn from execution failures and human feedback.

3. **Scalable Evaluation:** Development of more comprehensive benchmarks reflecting real-world software engineering complexity.

4. **Ethical Considerations:** Examination of ethical implications of autonomous code generation and modification.

---

## Conclusion

This systematic review reveals a rapidly maturing field of LLM-based agents for code generation and software engineering. The 10 selected papers demonstrate significant progress in autonomous program repair, multi-agent collaboration, and tool-integrated systems. Key achievements include state-of-the-art benchmark performance, cost-effective solutions, and novel architectural approaches.

However, fundamental questions remain regarding the optimal balance between agent complexity and performance, the scalability of current approaches to industrial-scale software systems, and the long-term implications of autonomous code generation. The field appears poised for continued growth, with opportunities for hybrid approaches, improved evaluation methodologies, and deeper integration with software development workflows.

The tension between sophisticated multi-agent frameworks and the surprisingly effective simple approaches exemplified by Agentless suggests that the field is still exploring the design space. Future research should focus on understanding when complexity is warranted and when simplicity suffices, guided by rigorous empirical evaluation across diverse software engineering tasks.

---

## References

Bouzenia, I., Devanbu, P., & Pradel, M. (2024). RepairAgent: An autonomous, LLM-based agent for program repair. *arXiv preprint arXiv:2403.17134*. https://arxiv.org/abs/2403.17134v2

Ishibashi, Y., & Nishimura, Y. (2024). Self-organized agents: A LLM multi-agent framework toward ultra large-scale code generation and optimization. *arXiv preprint arXiv:2404.02183*. https://arxiv.org/abs/2404.02183v1

Qin, Y., Wang, S., Lou, Y., Dong, J., Wang, K., Li, X., & Mao, X. (2024). AgentFL: Scaling LLM-based fault localization to project-level context. *arXiv preprint arXiv:2403.16362*. https://arxiv.org/abs/2403.16362v2

Tao, W., Zhou, Y., Wang, Y., Zhang, W., Zhang, H., & Cheng, Y. (2024). MAGIS: LLM-based multi-agent framework for GitHub issue resolution. *arXiv preprint arXiv:2403.17927*. https://arxiv.org/abs/2403.17927v2

Wang, X., Li, B., Song, Y., Xu, F. F., Tang, X., Zhuge, M., Pan, J., Song, Y., Li, B., Singh, J., Tran, H. H., Li, F., Ma, R., Zheng, M., Qian, B., Shao, Y., Muennighoff, N., Zhang, Y., Hui, B., & Lin, J. (2024). OpenHands: An open platform for AI software developers as generalist agents. *arXiv preprint arXiv:2407.16741*. https://arxiv.org/abs/2407.16741v3

Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2024). Agentless: Demystifying LLM-based software engineering agents. *arXiv preprint arXiv:2407.01489*. https://arxiv.org/abs/2407.01489v2

Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-Computer interfaces enable automated software engineering. *arXiv preprint arXiv:2405.15793*. https://arxiv.org/abs/2405.15793v3

Zhang, K., Li, J., Li, G., Shi, X., & Jin, Z. (2024). CodeAgent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges. *arXiv preprint arXiv:2401.07339*. https://arxiv.org/abs/2401.07339v2

Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). AutoCodeRover: Autonomous program improvement. *arXiv preprint arXiv:2404.05427*. https://arxiv.org/abs/2404.05427v3

Zheng, T., Zhang, G., Shen, T., Liu, X., Lin, B. Y., Fu, J., Chen, W., & Yue, X. (2024). OpenCodeInterpreter: Integrating code generation with execution and refinement. *arXiv preprint arXiv:2402.14658*. https://arxiv.org/abs/2402.14658v3

---

## Appendix: Search Methodology Details

**Search Query:** "code generation LLM agents"  
**Database:** arXiv  
**Date Range:** July 31, 2023 – July 30, 2025  
**Category:** cs.SE (Software Engineering)  
**Initial Results:** 50 papers  
**Reference Expansion:** 65 additional papers  
**Shortlist:** 30 papers  
**Final Selection:** 10 papers  
**Screening Method:** Co-citation analysis and centrality scoring  
**Format:** APA 7th Edition
