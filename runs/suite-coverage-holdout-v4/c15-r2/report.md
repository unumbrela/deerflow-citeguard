# Systematic Literature Review: Code Generation with LLM-based Agents

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "code generation agents", filtered to category cs.SE, published between 2023-07-31 and 2025-07-30
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM-based agents for code generation reveals a rapidly evolving field focused on autonomous software engineering capabilities. Surveyed papers demonstrate a clear progression from simple code completion to sophisticated multi-agent systems that emulate software development processes. Key findings indicate that agent-computer interface design significantly impacts performance, with some studies showing that simpler, well-structured approaches can outperform complex agent architectures. The field emphasizes both benchmarking (with new benchmarks like BigCodeBench and CodeAgentBench) and practical system development (SWE-agent, CodeAgent, AutoCodeRover, RepairAgent, OpenHands). Multi-agent frameworks address scalability challenges, while survey papers consolidate the growing body of research and identify future directions.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "code generation agents", filtered to category cs.SE, published between 2023-07-31 and 2025-07-30. Papers were sorted by relevance using co-citation analysis, and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search and screening results**: 50 papers identified by search, 54 added from references, 30 shortlisted, 30 screened, 10 included (7 from reference expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Metadata extraction was based solely on abstracts, which may not capture full methodological details or limitations.

## Themes

### Theme 1: Agent-Computer Interface Design and Performance

A central theme across multiple papers is how interface design affects LLM agent performance in software engineering tasks. Yang et al. (2024) demonstrated that custom agent-computer interfaces (ACIs) significantly enhance an agent's ability to create and edit code files, navigate repositories, and execute tests, with SWE-agent achieving 12.5% pass@1 on SWE-bench and 87.7% on HumanEvalFix. This work established that interface design is not merely an implementation detail but a critical factor determining agent capabilities.

Interestingly, Xia et al. (2024) challenged the assumption that complex agent architectures are necessary, showing that Agentless—a simple three-phase process without sophisticated tools—achieved 32.00% on SWE-bench Lite, outperforming all existing open-source software agents at lower cost ($0.70). This suggests that well-designed, interpretable techniques may have been overlooked in the pursuit of increasingly complex agent systems.

### Theme 2: Tool Integration and Repository-Level Code Generation

Several papers address the challenge of integrating LLMs with external tools and handling real-world repository-level complexity. Zhang et al. (2024) introduced CodeAgent, which integrates five programming tools and four agent strategies to tackle repository-level code generation with complex dependencies. Their CodeAgentBench benchmark revealed that real-world repo-level coding involves dependencies and documentation that current LLMs struggle with, yet CodeAgent achieved improvements ranging from 18.1% to 250% over baseline approaches.

The emphasis on tool integration reflects recognition that standalone LLMs are insufficient for practical software engineering. Agents must coordinate multiple capabilities—code search, testing, documentation analysis, and tool invocation—to achieve meaningful improvements in autonomous code generation.

### Theme 3: Autonomous Program Repair and Improvement

A significant research direction focuses on autonomous program repair beyond simple code generation. Bouzenia et al. (2024) introduced RepairAgent, the first autonomous LLM-based agent for program repair, which autonomously repaired 164 bugs on Defects4J, including 39 bugs that prior techniques could not fix. The approach uses a finite state machine to guide tool invocation and interleaves information gathering, repair ingredient collection, and fix validation.

Zhang et al. (2024) proposed AutoCodeRover, which combines LLMs with sophisticated code search using abstract syntax tree representations and spectrum-based fault localization. This approach achieved 19% efficacy on SWE-bench-lite at significantly lower cost ($0.43 USD) compared to other baselines, demonstrating that exploiting program structure enhances understanding of issue root causes and enables autonomous software engineering where auto-generated code can be autonomously improved.

### Theme 4: Multi-Agent Frameworks for Scalability

Addressing context length limitations in large-scale code generation, several papers explore multi-agent architectures. Ishibashi and Nishimura (2024) proposed Self-Organized Agents (SoA), where agents operate independently to generate and modify code components while collaborating to construct overall codebases. The framework automatically multiplies agents based on problem complexity, keeping each agent's code constant while allowing overall code volume to scale indefinitely. SoA surpassed single-agent baselines by 5% in Pass@1 accuracy on HumanEval.

Lin et al. (2024) developed FlowGen, which emulates software process models (Waterfall, TDD, and Scrum) using multiple LLM agents assigned to specific roles (requirement engineer, architect, developer, tester, scrum master). FlowGenScrum achieved the best performance with average Pass@1 scores 15% higher than RawGPT, demonstrating that integrating software engineering process knowledge into agent design improves code quality, exception handling, and reduces code smells.

### Theme 5: Benchmarking and Evaluation

The field has seen significant investment in benchmarking to evaluate LLM-based agents. Zhuo et al. (2024) introduced BigCodeBench, a benchmark with 1,140 fine-grained tasks requiring LLMs to invoke multiple function calls from 139 libraries across 7 domains. Each task includes 5.6 test cases with 99% average branch coverage. Their evaluation of 60 LLMs revealed that models scored up to 60%, significantly lower than human performance of 97%, indicating that LLMs are not yet capable of following complex instructions to use function calls precisely.

The development of specialized benchmarks (BigCodeBench, CodeAgentBench, SWE-bench variants) reflects the field's maturation and recognition that standard benchmarks like HumanEval are insufficient for evaluating repository-level, tool-integrated agent capabilities.

### Theme 6: Open Platforms and Community Development

Wang et al. (2024) introduced OpenHands, an open platform for AI software developers as generalist agents. The platform enables AI agents to write code, interact with command lines, and browse the web, with support for new agent implementation, sandboxed code execution, and multi-agent coordination. Released under the MIT license, the project has attracted over 2.1K contributions from more than 188 contributors, demonstrating strong community interest in open, extensible platforms for AI software development.

## Convergences and Disagreements

**Convergences**: Multiple papers agree that standalone LLMs are insufficient for practical software engineering tasks—agent architectures that integrate tools, exploit program structure, or coordinate multiple agents consistently outperform baseline approaches. There is also consensus that interface design and process structure significantly impact performance, whether through custom agent-computer interfaces (Yang et al., 2024) or software process model emulation (Lin et al., 2024). The field converges on the view that autonomous software engineering requires sophisticated coordination of multiple capabilities beyond simple code generation.

**Disagreements**: A notable tension exists between proponents of complex agent architectures and advocates of simpler approaches. While many papers develop increasingly sophisticated multi-agent systems with elaborate tool integration, Xia et al. (2024) demonstrate that Agentless—a simple three-phase process—outperforms complex agents on SWE-bench Lite. This suggests disagreement about whether complexity or simplicity is the path forward, with implications for cost, interpretability, and practical deployment.

## Gaps and Open Questions

Several gaps emerge from the surveyed literature. First, most papers do not explicitly state limitations in their abstracts, making it difficult to assess boundary conditions and failure modes. Second, cost considerations are mentioned inconsistently—while some papers report token costs (Bouzenia et al., 2024: 270,000 tokens per bug; Zhang et al., 2024: $0.43 USD), others omit economic analysis despite its importance for practical deployment.

Third, the evaluation landscape remains fragmented, with multiple benchmarks (SWE-bench, HumanEval, MBPP, Defects4J, BigCodeBench, CodeAgentBench) making cross-paper comparison challenging. Fourth, most studies focus on Python or single-language contexts, leaving multilingual and cross-language code generation underexplored.

Finally, while multi-agent frameworks show promise for scalability, the optimal coordination mechanisms, communication protocols, and agent role specializations remain open questions. Liu et al. (2024) note that synergy between multiple agents and human interaction offers promise, but the literature has not yet converged on best practices for human-agent collaboration in software engineering workflows.

## Per-Paper Annotations

### Bouzenia et al. (2024)

**Research question**: How can an autonomous LLM-based agent be designed to autonomously plan and execute actions to fix software bugs?

**Methodology**: Introduced RepairAgent, an autonomous agent treating the LLM as capable of planning and executing actions by invoking suitable tools, using a finite state machine to guide tool invocation with dynamically updated prompts and interleaved information gathering, repair ingredient collection, and fix validation.

**Key findings**:
- Repaired 164 bugs autonomously on the Defects4J dataset
- Fixed 39 bugs that prior techniques could not repair
- Average cost per bug is 270,000 tokens (14 cents USD using GPT-3.5)
- First autonomous, LLM-based agent for program repair

**Limitations**: The abstract does not explicitly state limitations, though it notes the token cost per bug (270,000 tokens) which may be a practical consideration.

### Ishibashi and Nishimura (2024)

**Research question**: How can multi-agent frameworks overcome context length limitations to generate and optimize large-scale, complex codebases?

**Methodology**: Proposed Self-Organized multi-Agent framework (SoA), where self-organized agents operate independently to generate and modify code components while collaborating to construct the overall codebase, automatically multiplying agents based on problem complexity.

**Key findings**:
- Enables dynamic scalability by automatically multiplying agents based on problem complexity
- Each agent handles significantly less code than a single-agent system
- Overall generated code is substantially greater than single-agent approaches
- Surpasses powerful single-agent baseline by 5% in Pass@1 accuracy on HumanEval

**Limitations**: Not stated in abstract.

### Lin et al. (2024)

**Research question**: Can emulating software process models using multiple LLM agents improve code generation quality compared to standalone LLM approaches?

**Methodology**: Developed FlowGen, a code generation framework emulating three software process models (Waterfall, TDD, and Scrum) using multiple LLM agents assigned to specific roles (requirement engineer, architect, developer, tester, scrum master), evaluated using GPT-3.5 on four benchmarks.

**Key findings**:
- FlowGenScrum achieved best performance with Pass@1 scores of 75.2 (HumanEval), 65.5 (HumanEval-ET), 82.5 (MBPP), and 56.7 (MBPP-ET), averaging 15% improvement over RawGPT
- Outperformed CodeT on MBPP, with both outperforming Reflexion
- Integrating CodeT into FlowGenScrum resulted in statistically significant improvements
- Design and code review activities increased exception handling and reduced code smells
- Maintained stable Pass@1 scores across GPT-3.5 versions and temperature values

**Limitations**: The study uses GPT-3.5 as the underlying LLM, and results may vary with different model architectures; the evaluation is limited to four specific benchmarks.

### Lin et al. (2024)

**Research question**: What is the current state of research on LLM-based agents applied to Software Engineering, and what are the key challenges and future directions?

**Methodology**: Conducted a comprehensive and systematic survey by collecting 124 papers on LLM-based agents for Software Engineering, categorizing them from both Software Engineering and agent perspectives, and identifying open challenges and future research directions.

**Key findings**:
- LLM-based agents extend standalone LLMs by enhancing capabilities for perceiving and utilizing external resources and tools
- LLM-based agents have shown remarkable effectiveness when applied to Software Engineering tasks
- Synergy between multiple agents and human interaction offers promise for tackling complex real-world SE problems
- Survey collected and categorized 124 papers from two perspectives: SE and agent viewpoints
- Repository of surveyed papers maintained at https://github.com/FudanSELab/Agent4SE-Paper-List

**Limitations**: Not stated in abstract.

### Wang et al. (2024)

**Research question**: How can we build an open platform for developing powerful and flexible AI agents that interact with environments like human developers?

**Methodology**: Introduced OpenHands (formerly OpenDevin), a community platform enabling AI agents to write code, interact with command lines, and browse the web, with support for new agent implementation, sandboxed code execution, multi-agent coordination, and evaluation benchmarks across 15 challenging tasks.

**Key findings**:
- Enables AI agents to interact with environments through code writing, command line interaction, and web browsing
- Supports implementation of new agents and safe sandboxed code execution
- Agents evaluated across 15 challenging tasks including SWE-BENCH and WEBARENA
- Project has over 2.1K contributions from more than 188 contributors
- Released under the permissive MIT license as a community project

**Limitations**: Not stated in abstract.

### Xia et al. (2024)

**Research question**: Do we really need complex autonomous software agents for automating software development tasks, or can simpler approaches suffice?

**Methodology**: Built Agentless, a simplistic three-phase process (localization, repair, and patch validation) without complex tools or autonomous action planning, evaluated on SWE-bench Lite, and constructed SWE-bench Lite-S by excluding problematic issues for more rigorous evaluation.

**Key findings**:
- Achieved highest performance (32.00%, 96 correct fixes) on SWE-bench Lite compared to all existing open-source software agents
- Achieved high performance at low cost ($0.70), demonstrating that simple approaches can outperform complex agent-based methods
- Identified problems with exact ground truth patches or insufficient/misleading issue descriptions in SWE-bench Lite
- Simple, interpretable techniques have overlooked potential in autonomous software development

**Limitations**: Not stated in abstract.

### Yang et al. (2024)

**Research question**: How does interface design affect the performance of language model agents in software engineering tasks?

**Methodology**: Designed and evaluated SWE-agent, a system with a custom agent-computer interface (ACI) enabling language model agents to autonomously use computers for software engineering, evaluated on SWE-bench and HumanEvalFix benchmarks.

**Key findings**:
- Custom agent-computer interface significantly enhances agent's ability to create and edit code files, navigate repositories, and execute tests
- Achieved pass@1 rate of 12.5% on SWE-bench, exceeding previous state-of-the-art performance
- Achieved pass@1 rate of 87.7% on HumanEvalFix, far exceeding previous state-of-the-art
- Design of agent-computer interface can significantly impact agents' behavior and performance

**Limitations**: Not stated in abstract.

### Zhang et al. (2024)

**Research question**: How can automated approaches solve GitHub issues to autonomously achieve program improvement beyond just code generation?

**Methodology**: Proposed AutoCodeRover, combining LLMs with sophisticated code search capabilities using abstract syntax tree representations and spectrum-based fault localization, exploiting program structure to enhance understanding and retrieve context via iterative search.

**Key findings**:
- Achieved 19% efficacy on SWE-bench-lite (300 real-life GitHub issues), higher than SWE-agent
- Achieved efficacy with significantly lower cost (on average $0.43 USD) compared to other baselines
- Using program structure and spectrum-based fault localization enhances LLM's understanding of issue root causes
- Workflow enables autonomous software engineering where auto-generated code can be autonomously improved

**Limitations**: Not stated in abstract.

### Zhang et al. (2024)

**Research question**: How can large language models be improved for real-world repository-level code generation tasks with complex dependencies?

**Methodology**: Introduced CodeAgentBench, a manually curated benchmark with five Python projects and 101 samples for repo-level code generation, then developed CodeAgent, an LLM-based agent framework integrating five programming tools and four agent strategies, evaluated on CodeAgentBench and HumanEval.

**Key findings**:
- CodeAgent significantly enhances LLM performance on repo-level code generation, with improvements ranging from 18.1% to 250%
- Outperforms commercial products like Github Copilot in accuracy and efficiency
- Demonstrates adaptability and efficacy across various code generation tasks beyond repo-level challenges
- Real-world repo-level coding involves complex dependencies and extensive documentation that current LLMs struggle with

**Limitations**: Not stated in abstract.

### Zhuo et al. (2024)

**Research question**: How well can LLMs solve challenging and practical tasks via programs that require invoking multiple function calls and understanding complex instructions?

**Methodology**: Introduced BigCodeBench, a benchmark with 1,140 fine-grained tasks requiring LLMs to invoke multiple function calls from 139 libraries across 7 domains, each task including 5.6 test cases with 99% average branch coverage, and proposed BigCodeBench-Instruct transforming docstrings into short instructions, evaluating 60 LLMs on both variants.

**Key findings**:
- Challenges LLMs to use function calls from 139 libraries across 7 domains
- LLMs scored up to 60% on the benchmark, significantly lower than human performance of 97%
- LLMs are not yet capable of following complex instructions to use function calls precisely
- Benchmark includes 1,140 tasks with rigorous evaluation (5.6 test cases per task, 99% branch coverage)

**Limitations**: Not stated in abstract.

## References

Bouzenia, I., Devanbu, P., & Pradel, M. (2024). RepairAgent: An autonomous, LLM-based agent for program repair. arXiv. https://arxiv.org/abs/2403.17134

Ishibashi, Y., & Nishimura, Y. (2024). Self-organized agents: A LLM multi-agent framework toward ultra large-scale code generation and optimization. arXiv. https://arxiv.org/abs/2404.02183

Lin, F., Kim, D. J., Tse-Husn, & Chen. (2024). SOEN-101: Code generation by emulating software process models using large language model agents. arXiv. https://arxiv.org/abs/2403.15852

Liu, J., Wang, K., Chen, Y., Peng, X., Chen, Z., Zhang, L., & Lou, Y. (2024). Large language model-based agents for software engineering: A survey. arXiv. https://arxiv.org/abs/2409.02977

Wang, X., Li, B., Song, Y., Xu, F. F., Tang, X., Zhuge, M., Pan, J., Song, Y., Li, B., Singh, J., Tran, H. H., Li, F., Ma, R., Zheng, M., Qian, B., Shao, Y., Muennighoff, N., Zhang, Y., Hui, B., Lin, J., et al. (2024). OpenHands: An open platform for AI software developers as generalist agents. arXiv. https://arxiv.org/abs/2407.16741

Xia, C. S., Deng, Y., Dunn, S., & Zhang, L. (2024). Agentless: Demystifying LLM-based software engineering agents. arXiv. https://arxiv.org/abs/2407.01489

Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao, S., Narasimhan, K., & Press, O. (2024). SWE-agent: Agent-computer interfaces enable automated software engineering. arXiv. https://arxiv.org/abs/2405.15793

Zhang, K., Li, J., Li, G., Shi, X., & Jin, Z. (2024). CodeAgent: Enhancing code generation with tool-integrated agent systems for real-world repo-level coding challenges. arXiv. https://arxiv.org/abs/2401.07339

Zhang, Y., Ruan, H., Fan, Z., & Roychoudhury, A. (2024). AutoCodeRover: Autonomous program improvement. arXiv. https://arxiv.org/abs/2404.05427

Zhuo, T. Y., Vu, M. C., Chim, J., Hu, H., Yu, W., Widyasari, R., Yusuf, I. N. B., Zhan, H., He, J., Paul, I., Brunner, S., Gong, C., Hoang, T., Zebaze, A. R., Hong, X., Li, W.-D., Kaddour, J., Xu, M., Zhang, Z., Yadav, P., et al. (2024). BigCodeBench: Benchmarking code generation with diverse function calls and complex instructions. arXiv. https://arxiv.org/abs/2406.15877
