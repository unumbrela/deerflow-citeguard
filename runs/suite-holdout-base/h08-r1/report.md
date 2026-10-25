# Systematic Literature Review: LLM Agents for Software Engineering

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "LLM agents" query, filtered to category cs.SE, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agents for software engineering has rapidly evolved over the past two years, with research focusing on three major dimensions: architectural foundations, practical applications, and reliability challenges. Surveyed papers reveal a field in transition from standalone models to agent systems embedded in external infrastructure, with growing emphasis on debugging, evaluation, and security considerations. While LLM agents demonstrate promising capabilities in code generation, repository deployment, and vulnerability analysis, significant gaps remain in handling complex multi-component systems and ensuring reliable autonomous operation. The collective literature points toward a maturing discipline that increasingly views agents not as isolated models but as components within larger cognitive and operational ecosystems.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "LLM agents", filtered to category cs.SE, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Externalization and Architectural Foundations

A central theme across the literature is the shift from parametric model capabilities to externalized cognitive infrastructure. Zhou et al. (2026) frame this as a progression from weights to context to harness, arguing that memory externalizes state across time, skills externalize procedural expertise, and protocols externalize interaction structure. This architectural perspective is echoed in Ke's (2026) Quine system, which grounds agent abstraction in the OS process model rather than application-layer orchestration, inheriting kernel-level isolation and resource control directly. The EDDOps framework by Xia et al. (2024) extends this systems view by embedding evaluation as a continuous, governing function throughout the agent lifecycle, unifying offline and online evaluation within a closed feedback loop. Together, these papers suggest that practical agent progress increasingly depends not only on stronger models but on better external cognitive infrastructure.

### Theme 2: Debugging and Reliability Challenges

Multiple papers address the emerging challenge of debugging and understanding failures in LLM agent systems. Islam et al. (2026a) present the first comprehensive study of bug types, root causes, and effects in LLM agent-based software, analyzing 1,268 bug-related posts across seven widely used frameworks. Their subsequent work introduces SelfHeal, a multi-agent system with fix and critic ReAct agents that outperforms baseline approaches in bug repair (Islam et al., 2026b). The BugReAct agent, equipped with Gemini 2.5 Flash, achieved remarkable performance in automated bug annotation at an average cost of $0.01 per post. This body of work highlights that as the field grows, developers face new challenges in debugging complex agent systems, and automated tooling is both feasible and cost-effective.

### Theme 3: Security and Privilege Management

Security considerations emerge as a critical concern in agent deployment. Yang et al. (2026) investigate over-privileged tool selection, finding that mainstream LLM agents commonly select or escalate to higher-privilege tools despite sufficient lower-privilege alternatives. This tendency is amplified by transient failures, and general safety alignment does not reliably transfer to least-privilege tool choice. Their privilege-aware post-training defense substantially reduces unnecessary high-privilege tool use while preserving general capabilities. Liu et al. (2025) similarly highlight security gaps in automated web vulnerability reproduction, where agents achieve reasonable success on simple library-based vulnerabilities but consistently fail on complex service-based vulnerabilities requiring multi-component environments. These findings underscore the need for advances in environmental adaptation and autonomous security-aware problem-solving.

### Theme 4: Benchmarking and Evaluation Frameworks

The literature demonstrates growing sophistication in benchmarking agent capabilities across different domains. CSR-Bench by Xiao et al. (2025) assesses LLM agents in deploying computer science research repositories, showing that agents can significantly enhance repository deployment workflows. Yellin (2025) proposes a difficulty metric for microservice-based application specifications, finding that agents using strong LLMs perform well on medium difficulty specifications but poorly on higher difficulty levels involving intricate business logic and database integration. The EDDOps approach by Xia et al. (2024) argues that traditional evaluation methods built around fixed benchmarks fail to capture emergent behaviors, advocating for continuous evaluation driving both runtime adaptation and governed redevelopment. These works collectively emphasize that evaluation must evolve alongside agent capabilities.

### Theme 5: Personal and Domain-Specific Applications

Research extends LLM agents to specialized domains beyond general software engineering. Li et al. (2024) survey Personal LLM Agents, envisioning them as a major software paradigm deeply integrated with personal data and devices. They identify key challenges in user intent understanding, task planning, tool use, and personal data management. The surveyed papers reveal a tension between general-purpose agent frameworks and domain-specific optimizations: while agents show promise across vulnerability reproduction (Liu et al., 2025), research repository deployment (Xiao et al., 2025), and microservice generation (Yellin, 2025), each domain presents unique challenges requiring tailored approaches.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the view that LLM agents are transitioning from model-centric to infrastructure-centric designs. Zhou et al. (2026), Ke (2026), and Xia et al. (2024) all emphasize that agent capabilities emerge from system-level architecture rather than model weights alone. There is also broad agreement on the importance of continuous evaluation and adaptation: Islam et al. (2026a, 2026b), Yang et al. (2026), and Xia et al. (2024) all demonstrate that static benchmarks are insufficient for capturing agent behavior over time. Finally, multiple studies highlight the gap between current capabilities and real-world demands, particularly for complex, multi-component systems (Liu et al., 2025; Yellin, 2025).

**Disagreements**: The literature shows limited direct disagreement, reflecting the field's early stage. However, there is tension between architectural approaches: Ke's (2026) Quine advocates for OS-level process abstraction, while Zhou et al. (2026) propose a higher-level harness engineering framework. These represent different levels of abstraction rather than contradictory claims, but they point to unresolved questions about the appropriate foundation for agent systems. Additionally, while some papers emphasize automated debugging solutions (Islam et al., 2026b), others focus on prevention through evaluation frameworks (Xia et al., 2024), suggesting different philosophies about whether to prioritize detection or prevention of agent failures.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, evaluation frameworks remain nascent: Xia et al. (2024) note that their EDDOps approach requires empirical validation in production settings, and Yang et al. (2026) acknowledge their ToolPrivBench may not cover all privilege escalation patterns in real-world deployments. Second, the AgentDefect benchmark contains only 37 runtime buggy instances, limiting generalizability (Islam et al., 2026b). Third, CSR-Bench focuses on NLP/CV/AI/ML/DM topics and may not generalize to other research domains (Xiao et al., 2025). Fourth, there is limited understanding of how agents handle long-running tasks with evolving context, as Quine's analysis points toward needed extensions for "task-relative worlds and revisable time" (Ke, 2026). Finally, the trade-off between parametric and externalized capability requires further investigation, particularly regarding governance and the co-evolution of models and infrastructure (Zhou et al., 2026).

## Per-Paper Annotations

### Islam et al. (2026a)

**Research question**: What types of bugs, root causes, and effects occur in LLM agent-based software, and can bug identification be automated effectively?
**Methodology**: Collects and analyzes 1,268 bug-related posts and code snippets from Stack Overflow, GitHub, and Hugging Face forums focused on LLM agents built with seven widely used LLM frameworks and custom implementations; builds BugReAct, a ReAct agent with external tools to automatically detect and annotate bugs.
**Key findings**:
- First comprehensive study of bug types, root causes, and effects in LLM agent-based software
- Analysis covers bugs across seven widely used LLM frameworks as well as custom implementations
- BugReAct equipped with Gemini 2.5 Flash achieved remarkable performance in annotating bug characteristics
- Automated bug annotation achieved an average cost of $0.01 USD per post/code snippet
**Limitations**: The field of LLM agent debugging is still in its early stages and the community is underdeveloped, making debugging difficult and costly; the study focuses on seven frameworks which may not represent all LLM agent development practices.

### Islam et al. (2026b)

**Research question**: What are the bug fix patterns in LLM agents, and can an automated multi-agent system effectively repair bugs in LLM agent code?
**Methodology**: Conducts empirical study of buggy posts and code snippets from Stack Overflow, GitHub, and HuggingFace Forums to examine fix patterns, components, languages and frameworks; introduces AgentDefect benchmark with 37 runtime buggy instances; proposes SelfHeal, a multi-agent system with fix and critic ReAct agents using internal fix rules and external web search.
**Key findings**:
- First empirical study on bug fix patterns in LLM agents across multiple platforms
- AgentDefect is the first benchmark dataset for bugs in LLM agents, containing 37 runtime buggy instances with fixed code and test files
- SelfHeal with Gemini 3 Pro as backbone LLM outperforms both baseline and state-of-the-art approaches by a significant margin
- The system leverages two independent ReAct agents (fix agent and critic agent) with tools providing internal knowledge and external web search
**Limitations**: The AgentDefect benchmark contains only 37 runtime buggy instances, which may limit generalizability; the field of LLM agent debugging is still in early stages with an underdeveloped community.

### Ke (2026)

**Research question**: Can LLM agents be realized as native POSIX processes instead of relying on application-layer orchestration frameworks?
**Methodology**: Presented Quine runtime architecture that explicitly maps agent identity to PID, interface to standard streams and exit status, state to memory/filesystem/environment, and lifecycle to fork/exec/exit; implemented as a single executable that recursively spawns fresh instances of itself.
**Key findings**:
- Grounding agent abstraction in OS process model inherits kernel-level isolation, composition, and resource control
- Naturally supports recursive delegation, context renewal via exec, and shell-native composition
- POSIX process model provides robust substrate for execution but not complete runtime model for cognition
- Analysis identifies need for two extensions beyond process semantics: task-relative worlds and revisable time
**Limitations**: POSIX process model does not provide a complete runtime model for cognition; requires extensions for task-relative worlds and revisable time to fully support agent cognition.

### Li et al. (2024)

**Research question**: What are the key architectural components, capabilities, efficiency considerations, and security challenges for Personal LLM Agents that integrate with personal data and devices?
**Methodology**: Surveys the field of Personal LLM Agents by summarizing key components and design choices in architecture, conducting in-depth analysis of opinions from domain experts, and comprehensively surveying representative solutions to address identified challenges.
**Key findings**:
- Personal LLM Agents are envisioned to become a major software paradigm for end-users in the upcoming era
- Key architecture components include user intent understanding, task planning, tool using, and personal data management
- LLMs enable intelligent agents to solve complex problems autonomously with powerful semantic understanding and reasoning
- Key challenges exist in achieving intelligent, efficient, and secure Personal LLM Agents
**Limitations**: Several key challenges remain to achieve intelligent, efficient and secure Personal LLM Agents; existing IPAs still have limited practicality and scalability due to lack of capabilities in user intent understanding, task planning, tool using, and personal data management.

### Liu et al. (2025)

**Research question**: Can current state-of-the-art LLM agents reliably reproduce web vulnerabilities from vulnerability reports in real-world scenarios?
**Methodology**: Systematically assesses 20 agents from software engineering, cybersecurity, and general domains across 16 dimensions on 3 representative web vulnerabilities, then evaluates top 3 agents (OpenHands, SWE-agent, CAI) on a benchmark of 80 real-world CVEs spanning 7 vulnerability types and 6 web technologies.
**Key findings**:
- LLM agents achieve reasonable success on simple library-based vulnerabilities but consistently fail on complex service-based vulnerabilities requiring multi-component environments
- Complex environment configurations and authentication barriers create a gap where agents can execute exploit code but fail to trigger actual vulnerabilities
- Performance degrades by over 33% under incomplete authentication information, showing high sensitivity to input guidance
- There is a significant gap between current LLM agent capabilities and the demands of reliable automated vulnerability reproduction
**Limitations**: The study reveals that current agents struggle with complex service-based vulnerabilities requiring multi-component environments; the evaluation is limited to 80 CVEs across 7 vulnerability types, and results show high sensitivity to input completeness.

### Xia et al. (2024)

**Research question**: How can evaluation be embedded as a continuous, governing function throughout the LLM agent lifecycle rather than as a terminal checkpoint?
**Methodology**: Conducted multivocal literature review (MLR) synthesizing academic and industrial evaluation practices; developed two empirically derived artifacts: a process model and reference architecture for evaluation-driven development and operations (EDDOps) that unifies offline and online evaluation within a closed feedback loop.
**Key findings**:
- Traditional evaluation methods built around fixed benchmarks and static test suites fail to capture emergent behaviors
- EDDOps unifies offline (development-time) and online (runtime) evaluation within a closed feedback loop
- Evaluation evidence drives both runtime adaptation and governed redevelopment
- Approach supports safer, more traceable evolution of LLM agents
**Limitations**: Based on literature review synthesis; specific implementation details may vary across different agent architectures and organizational contexts; requires empirical validation in production settings.

### Xiao et al. (2025)

**Research question**: How effective are LLM agents at deploying computer science research code repositories and setting up experimental environments?
**Methodology**: Created CSR-Bench benchmark assessing accuracy, efficiency, and deployment script quality across NLP/CV/AI/ML/DM topics; introduced CSR-Agents framework using multiple LLM agents to automate GitHub repository deployment by interpreting markdown instructions and repository structures to generate and iteratively improve bash commands.
**Key findings**:
- LLM agents can significantly enhance the workflow of repository deployment
- Agents can automatically set up experimental environments and deploy code to conduct research tasks
- The framework boosts developer productivity in research settings
- Improves management of developmental workflows through automated deployment
**Limitations**: Results are preliminary; benchmark focuses on NLP/CV/AI/ML/DM topics and may not generalize to other research domains or more complex multi-repository setups.

### Yang et al. (2026)

**Research question**: Do LLM agents unnecessarily select or escalate to higher-privilege tools when lower-privilege alternatives would suffice?
**Methodology**: Introduced ToolPrivBench to evaluate agent tool selection across 8 domains and 5 risk patterns, measuring both initial selection and escalation behavior after transient tool failures.
**Key findings**:
- Over-privileged tool selection is common among mainstream LLM agents
- Transient failures amplify the tendency to select higher-privilege tools
- General safety alignment does not reliably transfer to least-privilege tool choice
- Prompt-level controls provide only limited mitigation under transient failures
**Limitations**: Focus is on tool selection scenarios in benchmark settings; may not cover all privilege escalation patterns that occur in real-world deployments with more complex tool ecosystems.

### Yellin (2025)

**Research question**: How well do LLM agents perform at generating code for microservice-based applications across different specification complexity levels?
**Methodology**: Defined standard template for specifying microservice applications; proposed metric for scoring specification difficulty; evaluated agents using strong LLMs (like GPT-3o-mini) across different difficulty levels; analyzed errors in synthesized code to identify key challenges.
**Key findings**:
- Agents using strong LLMs perform fairly well on medium difficulty specifications
- Performance drops significantly on higher difficulty specifications
- Higher difficulty involves intricate business logic, greater use of external services, database integration, and non-functional capabilities like authentication
- Fine-grained approach to code generation improves correctness of synthesized code
**Limitations**: Focus is specifically on microservice architecture; the difficulty metric may not capture all dimensions of specification complexity; results depend on the specific LLMs tested.

### Zhou et al. (2026)

**Research question**: How does externalizing capabilities into memory, skills, protocols, and harness infrastructure transform LLM agent architecture and performance compared to relying on internal model weights?
**Methodology**: Reviews the historical progression from weights to context to harness through the lens of cognitive artifacts, analyzing memory, skills, and protocols as three distinct but coupled forms of externalization within a systems-level framework.
**Key findings**:
- Memory externalizes state across time, skills externalize procedural expertise, and protocols externalize interaction structure
- Harness engineering serves as the unification layer that coordinates externalized modules into governed execution
- Agent infrastructure matters because it transforms hard cognitive burdens into forms that the model can solve more reliably
- Practical agent progress increasingly depends on better external cognitive infrastructure, not just stronger models
**Limitations**: Open challenges remain in evaluation, governance, and understanding the long-term co-evolution of models and external infrastructure; the trade-off between parametric and externalized capability requires further investigation.

## References

Islam, N., Ayon, R. S., Thomas, D. G., Ahmed, S., & Wardat, M. (2026). When agents fail: A comprehensive study of bugs in LLM agents with automated labeling. arXiv. https://arxiv.org/abs/2601.15232

Islam, N., Raza, M. A., & Wardat, M. (2026). SelfHeal: Empirical fix pattern analysis and bug repair in LLM agents. arXiv. https://arxiv.org/abs/2604.17699

Ke, H. (2026). Quine: Realizing LLM agents as native POSIX processes. arXiv. https://arxiv.org/abs/2603.18030

Li, Y., Wen, H., Wang, W., Li, X., Yuan, Y., Liu, G., Liu, J., Xu, W., Wang, X., Sun, Y., Kong, R., Wang, Y., Geng, H., Luan, J., Jin, X., Ye, Z., Xiong, G., Zhang, F., Li, X., Xu, M., Li, Z., Li, P., Liu, Y., Zhang, Y.-Q., & Liu, Y. (2024). Personal LLM agents: Insights and survey about the capability, efficiency and security. arXiv. https://arxiv.org/abs/2401.05459

Liu, B., Zhao, Y., Xu, G., & Wang, H. (2025). LLM agents for automated web vulnerability reproduction: Are we there yet? arXiv. https://arxiv.org/abs/2510.14700

Xia, B., Lu, Q., Zhu, L., Xing, Z., Zhao, D., & Zhang, H. (2024). Evaluation-driven development and operations of LLM agents: A process model and reference architecture. arXiv. https://arxiv.org/abs/2411.13768

Xiao, Y., Wang, R., Kong, L., Golac, D., & Wang, W. (2025). CSR-Bench: Benchmarking LLM agents in deployment of computer science research repositories. arXiv. https://arxiv.org/abs/2502.06111

Yang, K., Bu, Y., Yi, J., Wang, Y., Zhou, B., Dai, J., Hu, S., & Yang, Y. (2026). When lower privileges suffice: Investigating over-privileged tool selection in LLM agents. arXiv. https://arxiv.org/abs/2606.20023

Yellin, D. M. (2025). LLM agents for generating microservice-based applications: how complex is your specification? arXiv. https://arxiv.org/abs/2508.20119

Zhou, C., Chai, H., Chen, W., Guo, Z., Shan, R., Song, Y., Xu, T., Yang, Y., Yu, A., Zhang, W., Zheng, C., Zhu, J., Zheng, Z., Zhang, Z., Lou, X., Zhang, C., Fu, Z., Wang, J., Liu, W., Lin, J., & Zhang, W. (2026). Externalization in LLM agents: A unified review of memory, skills, protocols and harness engineering. arXiv. https://arxiv.org/abs/2604.08224
