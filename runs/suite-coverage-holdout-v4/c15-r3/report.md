# Systematic Literature Review: Code Generation with LLM-based Agents

**Date:** October 26, 2026  
**Search Period:** July 31, 2023 – July 30, 2025  
**Category:** cs.SE (Software Engineering)  
**Format:** APA Style

---

## Executive Summary

This systematic literature review examines 10 key papers on code generation with LLM-based agents published between July 2023 and July 2025. The review reveals a rapidly evolving field where autonomous agents are transforming software engineering practices, from simple code completion to complex repository-level development tasks. Key themes include agent-computer interfaces, multi-agent collaboration, tool integration, autonomous program repair, and the emulation of established software process models.

---

## Methodology

### Search Strategy
- **Database:** arXiv preprint repository
- **Primary Category:** cs.SE (Software Engineering)
- **Time Window:** July 31, 2023 – July 30, 2025
- **Search Query:** "code generation agents"
- **Initial Pool:** 50 papers identified
- **Reference Expansion:** 54 additional papers from citations
- **Shortlist:** 30 papers screened
- **Final Selection:** 10 papers based on relevance to LLM-based code generation agents

### Selection Criteria
Papers were selected based on their focus on:
- Code generation using LLM-based agents
- Multi-agent systems for software development
- Autonomous coding agents
- Agent-driven code synthesis and program improvement
- Tool-integrated agent frameworks

---

## Selected Papers (APA Format)

### 1. Agent-Computer Interfaces

**Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024).** SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. *arXiv preprint arXiv:2405.15793*. https://arxiv.org/abs/2405.15793v3

**Key Contributions:**
- Introduces the concept of Agent-Computer Interfaces (ACI) specifically designed for LM agents
- Achieves state-of-the-art performance on SWE-bench (12.5% pass@1) and HumanEvalFix (87.7% pass@1)
- Demonstrates that specially-built interfaces significantly enhance agent performance in code creation, repository navigation, and test execution
- Shows non-interactive LMs are outperformed by interactive agent systems with proper interfaces

**Significance:** This paper establishes that LLM agents, like human developers, benefit from specialized interfaces, fundamentally shifting how we design agent systems for software engineering tasks.

---

### 2. Tool-Integrated Agent Systems

**Zhang, K., Li, J., Ge, L., Shi, X., & Jin, Z. (2024).** CodeAgent: Enhancing Code Generation with Tool-Integrated Agent Systems for Real-World Repo-level Coding Challenges. *arXiv preprint arXiv:2401.07339*. https://arxiv.org/abs/2401.07339v2

**Key Contributions:**
- Introduces CodeAgentBench, a manually curated benchmark with 101 samples across 5 Python projects for repo-level code generation
- Integrates 5 programming tools for information retrieval, code symbol navigation, and code testing
- Implements 4 agent strategies to optimize tool usage
- Achieves 18.1% to 250% performance improvement over baseline LLMs
- Outperforms GitHub Copilot in accuracy and efficiency

**Significance:** Addresses the gap between simple code unit generation and real-world repository-level challenges, demonstrating that tool integration is essential for practical code generation.

---

### 3. Autonomous Program Improvement

**Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024).** AutoCodeRover: Autonomous Program Improvement. *arXiv preprint arXiv:2404.05427*. https://arxiv.org/abs/2404.05427v3

**Key Contributions:**
- Proposes automated approach for solving GitHub issues to achieve program improvement
- Uses abstract syntax tree (AST) representation rather than treating projects as file collections
- Exploits program structure (classes/methods) for enhanced issue understanding
- Achieves 19% efficacy on SWE-bench-lite, exceeding SWE-agent
- Operates at significantly lower cost ($0.43 USD average per issue)

**Significance:** Demonstrates that software engineering-oriented approaches using program structure outperform generic agent methods, with practical cost efficiency.

---

### 4. Simplicity vs. Complexity Debate

**Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2024).** Agentless: Demystifying LLM-based Software Engineering Agents. *arXiv preprint arXiv:2407.01489*. https://arxiv.org/abs/2407.01489v2

**Key Contributions:**
- Questions the necessity of complex autonomous agents
- Proposes simplistic three-phase process: localization, repair, and validation
- Achieves 32.00% (96 correct fixes) on SWE-bench Lite with low cost ($0.70)
- Outperforms all existing open-source software agents
- Constructs SWE-bench Lite-S for more rigorous evaluation by excluding problematic issues

**Significance:** Challenges the field's trend toward increasingly complex agent architectures, demonstrating that simple, interpretable techniques can achieve superior results.

---

### 5. Autonomous Program Repair

**Bouzenia, I., Devanbu, P., & Pradel, M. (2024).** RepairAgent: An Autonomous, LLM-Based Agent for Program Repair. *arXiv preprint arXiv:2403.17134*. https://arxiv.org/abs/2403.17134v2

**Key Contributions:**
- First autonomous LLM-based agent specifically for program repair
- Treats LLM as an agent capable of autonomously planning and executing actions
- Freely interleaves information gathering, repair ingredient collection, and fix validation
- Repairs 164 bugs on Defects4J dataset, including 39 not fixed by prior techniques
- Average cost: 270,000 tokens per bug (14 cents USD with GPT-3.5)

**Significance:** Pioneers agent-based program repair, moving beyond fixed-prompt approaches to dynamic, tool-invoking autonomous agents.

---

### 6. Open Platform for AI Developers

**Wang, X., Li, B., Song, Y., Xu, F. F., Tang, X., Zhuge, M., Pan, J., Song, Y., Li, B., Singh, J., Tran, H. H., Li, F., Ma, R., Zheng, M., Qian, B., Shao, Y., Muennighoff, N., Zhang, Y., Hui, B., & Lin, J. (2024).** OpenHands: An Open Platform for AI Software Developers as Generalist Agents. *arXiv preprint arXiv:2407.16741*. https://arxiv.org/abs/2407.16741v3

**Key Contributions:**
- Introduces OpenHands (formerly OpenDevin), an open platform for AI software developers
- Enables agents to write code, interact with command line, and browse the web
- Supports implementation of new agents, safe sandboxed environments, and multi-agent coordination
- Evaluates agents across 15 challenging tasks including SWE-BENCH and WEBARENA
- Community project with 2.1K+ contributions from 188+ contributors under MIT license

**Significance:** Provides a flexible, open infrastructure for developing generalist AI software developers, fostering community collaboration and standardization.

---

### 7. Benchmarking Code Generation

**Zhuo, T. Y., Vu, M. C., Chim, J., Hu, H., Yu, W., Widyasari, R., Yusuf, I. N. B., Zhan, H., He, J., Paul, I., Brunner, S., Gong, C., Hoang, T., Zebaye, A. R., Hong, X., Li, W.-D., Kaddour, J., Xu, M., Zhang, Z., & Yadav, P. (2024).** BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions. *arXiv preprint arXiv:2406.15877*. https://arxiv.org/abs/2406.15877v4

**Key Contributions:**
- Introduces BigCodeBench with 1,140 fine-grained tasks requiring multiple function calls from 139 libraries across 7 domains
- Each task includes 5.6 test cases with 99% average branch coverage
- Proposes BigCodeBench-Instruct with natural-language-oriented variant
- Evaluates 60 LLMs, revealing maximum scores of 60% vs. human performance of 97%
- Identifies significant gap in LLMs' ability to follow complex instructions for precise function call usage

**Significance:** Establishes rigorous benchmarking for practical code generation tasks, revealing current limitations in compositional reasoning and tool usage.

---

### 8. Multi-Agent Frameworks

**Ishibashi, Y., & Nishimura, Y. (2024).** Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization. *arXiv preprint arXiv:2404.02183*. https://arxiv.org/abs/2404.02183v1

**Key Contributions:**
- Proposes Self-Organized multi-Agent framework (SoA) for scalable code generation
- Agents operate independently while collaborating to construct overall codebase
- Automatically multiplies agents based on problem complexity for dynamic scalability
- Each agent manages constant code amount while overall code volume increases indefinitely
- Surpasses single-agent baseline by 5% in Pass@1 accuracy on HumanEval

**Significance:** Addresses context length limitations in single-agent approaches through self-organizing multi-agent collaboration, enabling ultra large-scale code generation.

---

### 9. Software Process Model Emulation

**Lin, F., Kim, D. J., Tse-Husn, & Chen. (2024).** SOEN-101: Code Generation by Emulating Software Process Models Using Large Language Model Agents. *arXiv preprint arXiv:2403.15852*. https://arxiv.org/abs/2403.15852v2

**Key Contributions:**
- Introduces FlowGen framework emulating three software process models: Waterfall, TDD, and Scrum
- Assigns LLM agents to roles: requirement engineer, architect, developer, tester, and scrum master
- FlowGenScrum achieves Pass@1 of 75.2 (HumanEval), 65.5 (HumanEval-ET), 82.5 (MBPP), 56.7 (MBPP-ET)
- Average 15% improvement over RawGPT baseline
- Integrating CodeT into FlowGenScrum achieves highest Pass@1 scores
- Development activities impact code smell and exception handling differently

**Significance:** Demonstrates that emulating established software engineering processes with multi-agent systems significantly improves code quality and stability.

---

### 10. AI-Aided Software Development

**Zhang, S., Wang, J., Dong, G., Sun, J., Zhang, Y., & Pu, G. (2024).** Experimenting a New Programming Practice with LLMs. *arXiv preprint arXiv:2401.01062*. https://arxiv.org/abs/2401.01062v1

**Key Contributions:**
- Develops AISD (AI-aided Software Development) prototype
- Takes high-level, potentially vague user requirements as inputs
- Generates detailed use cases, prototype system designs, and system implementation
- Keeps user in the loop through iterative feedback on use cases, designs, and implementations
- Evaluated on novel benchmark of non-trivial software projects
- Suggests future where software engineering reduces to requirement engineering and system testing

**Significance:** Proposes transformative programming practice where LLMs handle implementation while humans focus on high-level requirements and validation.

---

## Thematic Analysis

### Theme 1: Agent Architecture and Interfaces

The literature reveals a fundamental tension between complexity and simplicity in agent design. **Yang et al. (2024)** demonstrate that specialized Agent-Computer Interfaces dramatically improve performance, suggesting agents need tailored interaction mechanisms. Conversely, **Xia et al. (2024)** challenge this trend, showing that a simple three-phase process without autonomous decision-making outperforms complex agent architectures. This debate highlights the field's maturation as researchers question assumptions about agent complexity.

### Theme 2: Tool Integration and Repository-Level Challenges

A consistent finding across multiple papers is that real-world code generation requires tool integration beyond language modeling. **Zhang et al. (2024)** show 18.1%-250% improvements through tool integration, while **Bouzenia et al. (2024)** demonstrate autonomous tool invocation for program repair. **Zhuo et al. (2024)** reveal that current LLMs struggle with complex function calls, scoring only 60% compared to human 97% performance, indicating significant room for improvement in tool usage capabilities.

### Theme 3: Multi-Agent Collaboration

Three papers explore multi-agent approaches from different angles. **Ishibashi & Nishimura (2024)** propose self-organizing agents for scalability, **Lin et al. (2024)** emulate software process models with role-based agents, and **Wang et al. (2024)** provide infrastructure for multi-agent coordination. The consistent finding is that multi-agent systems outperform single agents, particularly for complex tasks requiring division of labor.

### Theme 4: Program Understanding and Structure

**Zhang et al. (2024)** emphasize using abstract syntax trees rather than treating code as text, achieving better results at lower cost. This software engineering-oriented approach contrasts with purely language-based methods, suggesting that incorporating program structure understanding is crucial for effective code generation and repair.

### Theme 5: Benchmarking and Evaluation

The field shows rapid advancement in benchmarking sophistication. From **HumanEval** and **SWE-bench** to **CodeAgentBench**, **BigCodeBench**, and **SWE-bench Lite-S**, researchers are creating increasingly realistic and challenging evaluation scenarios. The progression from algorithmic tasks to repository-level challenges reflects the field's maturation toward practical applications.

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Human-Agent Collaboration:** While **Zhang et al. (2024)** propose keeping humans in the loop, most papers focus on full automation. The optimal division of labor between humans and agents remains underexplored.

2. **Long-Term Maintenance:** Current research focuses on initial code generation and repair. Long-term code evolution, refactoring, and maintenance by autonomous agents need further investigation.

3. **Security and Safety:** None of the reviewed papers extensively address security implications of autonomous code generation, including vulnerability introduction or malicious code prevention.

4. **Cost-Performance Tradeoffs:** While some papers report costs (**Zhang et al., 2024**: $0.43; **Bouzenia et al., 2024**: $0.14; **Xia et al., 2024**: $0.70), systematic analysis of cost-performance tradeoffs across different approaches is lacking.

5. **Domain Specialization:** Most benchmarks focus on general Python programming. Domain-specific code generation (e.g., embedded systems, safety-critical software) requires specialized investigation.

### Future Research Directions

1. **Hybrid Approaches:** Combining the simplicity of **Agentless** with the interface sophistication of **SWE-agent** may yield optimal performance-cost ratios.

2. **Process Model Optimization:** **Lin et al. (2024)** show Scrum outperforms Waterfall and TDD. Further research into optimal process models for different task types could enhance performance.

3. **Tool Learning:** Given **Zhuo et al. (2024)** findings on function call limitations, research into improving LLMs' tool usage capabilities is critical.

4. **Scalable Multi-Agent Systems:** **Ishibashi & Nishimura (2024)** demonstrate automatic agent multiplication. Extending this to dynamic agent specialization and communication optimization presents fertile ground.

5. **Real-World Deployment:** Moving from benchmarks to production deployment requires addressing integration, monitoring, and failure recovery in live systems.

---

## Conclusion

The systematic review of 10 papers reveals a field in rapid transition. LLM-based agents for code generation have evolved from simple code completion to sophisticated systems capable of repository-level development, autonomous repair, and multi-agent collaboration. Key findings include:

- **Specialized interfaces** significantly outperform generic approaches
- **Tool integration** is essential for real-world applications
- **Multi-agent systems** enable scalability and role specialization
- **Process model emulation** improves code quality and stability
- **Simplicity** can outperform complexity in certain contexts
- **Program structure understanding** enhances repair and generation

The field faces the fundamental challenge of balancing automation with human oversight, complexity with interpretability, and benchmark performance with practical deployment. As **Zhang et al. (2024)** envision, the future may see software engineering reduced to requirement engineering and system testing, with LLM agents handling implementation. However, achieving this vision requires addressing identified gaps in security, long-term maintenance, and domain specialization.

The reviewed papers collectively demonstrate that LLM-based agents are not merely incremental improvements to code completion tools but represent a paradigm shift in how software is developed, maintained, and evolved. The next phase of research must bridge the gap between impressive benchmark results and reliable, production-ready autonomous software engineering systems.

---

## References

Bouzenia, I., Devanbu, P., & Pradel, M. (2024). RepairAgent: An autonomous, LLM-based agent for program repair. *arXiv preprint arXiv:2403.17134*. https://arxiv.org/abs/2403.17134v2

Ishibashi, Y., & Nishimura, Y. (2024). Self-organized agents: A LLM multi-agent framework toward ultra large-scale code generation and optimization. *arXiv preprint arXiv:2404.02183*. https://arxiv.org/abs/2404.02183v1

Lin, F., Kim, D. J., Tse-Husn, & Chen. (2024). SOEN-101: Code generation by emulating software process models using large language model agents. *arXiv preprint arXiv:2403.15852*. https://arxiv.org/abs/2403.15852v2

Wang, X., Li, B., Song, Y., Xu, F. F., Tang, X., Zhuge, M., Pan, J., Song, Y., Li, B., Singh, J., Tran, H. H., Li, F., Ma, R., Zheng, M., Qian, B., Shao, Y., Muennighoff, N., Zhang, Y., Hui, B., & Lin, J. (2024). OpenHands: An open platform for AI software developers as generalist agents. *arXiv preprint arXiv:2407.16741*. https://arxiv.org/abs/2407.16741v3

Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2024). Agentless: Demystifying LLM-based software engineering agents. *arXiv preprint arXiv:2407.01489*. https://arxiv.org/abs/2407.01489v2

Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-computer interfaces enable automated software engineering. *arXiv preprint arXiv:2405.15793*. https://arxiv.org/abs/2405.15793v3

Zhang, K., Li, J., Ge, L., Shi, X., & Jin, Z. (2024). CodeAgent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges. *arXiv preprint arXiv:2401.07339*. https://arxiv.org/abs/2401.07339v2

Zhang, S., Wang, J., Dong, G., Sun, J., Zhang, Y., & Pu, G. (2024). Experimenting a new programming practice with LLMs. *arXiv preprint arXiv:2401.01062*. https://arxiv.org/abs/2401.01062v1

Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). AutoCodeRover: Autonomous program improvement. *arXiv preprint arXiv:2404.05427*. https://arxiv.org/abs/2404.05427v3

Zhuo, T. Y., Vu, M. C., Chim, J., Hu, H., Yu, W., Widyasari, R., Yusuf, I. N. B., Zhan, H., He, J., Paul, I., Brunner, S., Gong, C., Hoang, T., Zebaye, A. R., Hong, X., Li, W.-D., Kaddour, J., Xu, M., Zhang, Z., & Yadav, P. (2024). BigCodeBench: Benchmarking code generation with diverse function calls and complex instructions. *arXiv preprint arXiv:2406.15877*. https://arxiv.org/abs/2406.15877v4

---

## Appendix: Screening Statistics

- **Initial Search Results:** 50 papers
- **Reference Expansion:** 54 papers added from citations
- **Total Pool:** 104 papers
- **Shortlisted:** 30 papers
- **Screening Scores:**
  - Score 0: 2 papers
  - Score 1: 13 papers
  - Score 2: 4 papers
  - Score 3: 11 papers
- **Final Selection:** 10 papers (7 from reference expansion, 3 from initial search)
- **Inclusion Rate:** 33.3% of shortlisted papers
