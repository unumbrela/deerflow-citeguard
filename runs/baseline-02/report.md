# Systematic Literature Review: LLM Agent Evaluation Benchmarks

**Date**: October 25, 2026  
**Topic**: LLM Agent Evaluation Benchmarks  
**Scope**: 10 papers from 2024-2026 (including seminal 2023 works published in 2024 venues)  
**Category**: cs.CL (Computation and Language)  
**Format**: APA

---

## Executive Summary

This systematic literature review synthesizes 10 recent papers on LLM agent evaluation benchmarks published between 2023-2025. The review reveals a rapidly evolving field transitioning from single-agent, task-specific benchmarks toward multi-dimensional, enterprise-ready evaluation frameworks. Key findings indicate significant performance gaps between current agents and human baselines (e.g., 14.41% vs 78.24% on WebArena), with emerging focus on multi-agent coordination, security vulnerabilities, visual grounding, and real-world consequential tasks. Two comprehensive surveys establish foundational taxonomies for the field, while eight benchmark papers introduce novel evaluation methodologies across diverse domains.

---

## 1. Introduction

The emergence of LLM-based agents represents a paradigm shift in AI capabilities, enabling autonomous systems that plan, reason, use tools, and interact with dynamic environments [citation:Survey on Evaluation](https://arxiv.org/abs/2503.16416). However, evaluating these agents presents unique challenges beyond traditional LLM assessment, requiring frameworks that capture multi-turn interactions, tool coordination, long-horizon planning, and real-world deployment readiness.

This review addresses the following research questions:
1. What evaluation methodologies and benchmarks exist for LLM agents?
2. What are the key dimensions and metrics used in agent evaluation?
3. What performance gaps exist between current agents and human baselines?
4. What limitations and future directions characterize the field?

---

## 2. Methodology

This systematic literature review follows a structured approach:
- **Search Strategy**: Targeted searches for arXiv papers in cs.CL category focusing on LLM agent evaluation benchmarks
- **Inclusion Criteria**: Papers published 2024-2026 (including seminal 2023 works with 2024 venue publications), English language, peer-reviewed or preprint with substantial evaluation methodology
- **Selection**: 10 papers comprising 2 comprehensive surveys and 8 benchmark/introduction papers
- **Analysis**: Thematic synthesis across evaluation dimensions, methodologies, findings, and limitations
- **Citation Format**: APA 7th edition

---

## 3. Paper Summaries

### 3.1 Survey Papers

#### 3.1.1 Mohammadi, M., & Li, Y. (2025). Survey on Evaluation of LLM-based Agents. *arXiv preprint arXiv:2503.16416*.

**Research Question**: What are the current evaluation methods for LLM-based agents, and what trends, limitations, and future directions exist?

**Methodology**: First comprehensive survey analyzing LLM agent evaluation across five perspectives: core LLM capabilities, application-specific benchmarks, generalist agents, evaluation protocols, and emerging trends.

**Key Findings**:
- LLM-based agents require new evaluation paradigms beyond traditional LLM assessment due to planning, reasoning, tool use, and memory requirements
- Current evaluation approaches are fragmented across capability assessment, domain-specific benchmarks, and generalist agent evaluation
- Most evaluations use static, isolated testing with predefined prompts rather than live interaction or dynamic multi-turn evaluation
- Critical gaps exist in evaluating agent reliability, reproducibility, and real-world deployment readiness

**Limitations**: As the first comprehensive survey, it captures a rapidly evolving landscape that may quickly become outdated; analysis is primarily descriptive rather than prescriptive.

---

#### 3.1.2 Mohammadi, M., Li, Y., Lo, J., & Yip, W. (2025). Evaluation and Benchmarking of LLM Agents: A Survey. *arXiv preprint arXiv:2507.21504*.

**Research Question**: How can the fragmented landscape of LLM agent evaluation be systematically organized for real-world enterprise deployment?

**Methodology**: Introduction of a comprehensive two-dimensional taxonomy for LLM agent evaluation, categorizing assessment along capability, behavior, and safety dimensions while integrating enterprise-specific considerations.

**Key Findings**:
- Current LLM agent evaluation lacks systematic frameworks and comprehensive taxonomies needed for enterprise deployment
- Enterprise-specific challenges (role-based data access, reliability guarantees, dynamic long-horizon interactions, compliance requirements) are largely overlooked
- Agents can produce diverse, well-formed text creating the appearance of active discussion, but substance is often absent
- Structured taxonomy integrating objective performance metrics with protocol-driven methodologies is essential
- Existing benchmarks fail to address real-world enterprise constraints including data access controls and regulatory compliance

**Limitations**: Focus primarily on enterprise contexts; taxonomy requires validation through practical implementation across diverse scenarios.

---

#### 3.1.3 Hou, X., Yan, Y., Li, Y., Xing, Z., Xu, X., Lu, Q., Zhu, L., & Wang, C. (2024). From LLMs to LLM-based Agents for Software Engineering: A Comprehensive Survey. *arXiv preprint arXiv:2408.02479*.

**Research Question**: What are the key differences between LLMs and LLM-based agents in software engineering, and how have evaluation methodologies evolved?

**Methodology**: Comprehensive survey reviewing LLMs vs LLM-based agents across six software engineering topics (requirement engineering, code generation, autonomous learning, software design, test generation, maintenance), analyzing differences in tasks, benchmarks, and evaluation metrics.

**Key Findings**:
- LLM-based agents focus on collaboration and decision-making capabilities using multi-dimensional evaluation metrics
- Clear trend transitioning from standalone LLMs to agent-based systems in software engineering research
- Key benchmarks include SWE-Bench, HumanEval, HumanEvalFix, and AgentBench, each targeting different aspects
- Interface design is critical for enabling effective autonomous software engineering (12.5% on SWE-bench, 87.7% on HumanEvalFix with tailored interfaces)
- Field lacks unified standards and benchmarking to qualify an LLM solution as an LLM-based agent

**Limitations**: Survey synthesizes existing work rather than presenting novel empirical findings; rapidly evolving field means findings may become outdated quickly; broad coverage limits depth in any single area.

---

### 3.2 Benchmark Papers

#### 3.2.1 Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., Gu, Y., Ding, H., Men, K., Yang, K., Zhang, S., Deng, X., Zeng, A., Du, Z., Dong, Y., & Tang, J. (2023). AgentBench: Evaluating LLMs as Agents. *arXiv preprint arXiv:2308.03688*.

**Research Question**: How can we quantitatively evaluate LLMs as agents on challenging tasks in interactive environments?

**Methodology**: Multi-dimensional benchmark consisting of 8 distinct interactive environments (Operating System, Database, Knowledge Graph, Digital Card Game, Lateral Thinking Puzzles, House-Holding, Web Shopping, Configuration Text) assessing 29 API-based and open-source LLMs.

**Key Findings**:
- GPT-4 leads with overall score of 4.01, dominating in 6 out of 8 environments
- Significant performance gap between commercial and open-source LLMs (best OSS model CodeLlama-34B achieves only 0.96)
- Code training improves performance on code-grounded tasks but shows limited transfer to other environments
- Top commercial LLMs demonstrate strong agent capabilities in complex environments
- Performance varies significantly across different environment types, revealing specific capability gaps

**Limitations**: Focus on English-language tasks; 8 environments represent only a subset of potential agent application domains.

---

#### 3.2.2 Zhou, S., Xu, F. F., Zhu, H., Zhou, X., Lo, R., Sridhar, A., Cheng, X., Ou, T., Bisk, Y., Fried, D., Alon, U., & Neubig, G. (2023). WebArena: A Realistic Web Environment for Independent Language-guided Agents. *arXiv preprint arXiv:2307.13854*.

**Research Question**: How can we build a realistic and reproducible environment to evaluate autonomous language-guided agents on real-world web tasks?

**Methodology**: WebArena, a highly realistic and reproducible web environment supporting three website types (e-commerce, social networking, content management) with 812 diverse long-horizon tasks, using programmatically validated functional correctness measures.

**Key Findings**:
- Best GPT-4-based agent achieves only 14.41% success rate compared to humans at 78.24% (64-point gap)
- Agents frequently fail by falsely declaring tasks impossible rather than attempting complex multi-step solutions
- WebArena provides contamination-resistant benchmark with fully functional, self-hosted websites deployable via Docker
- Benchmark reveals fundamental limitations in current agents' ability to handle long-horizon tasks requiring sustained planning
- Task success varies significantly across different website domains

**Limitations**: Requires significant infrastructure to deploy (Docker containers); focuses on web navigation tasks; human baseline of 78.24% suggests some tasks may have ambiguous success criteria.

---

#### 3.2.3 Koh, J. Y., Lo, R., Jang, L., Duvvur, V., Lim, M. C., Huang, P.-Y., Neubig, G., Zhou, S., Salakhutdinov, R., & Fried, D. (2024). VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks. *arXiv preprint arXiv:2401.13649*.

**Research Question**: How can we evaluate multimodal agents on realistic web tasks requiring visual information, and what are the limitations of current agents?

**Methodology**: VisualWebArena extends WebArena with 910 diverse web-based tasks requiring visual grounding, comparing text-only agents with caption augmentation against true multimodal models through quantitative and qualitative analysis.

**Key Findings**:
- Text-only LLM agents fundamentally struggle with web tasks requiring visual information
- Multimodal models show significant improvement (Gemini-Pro: 3.85% caption-augmented vs 6.04% multimodal success rate)
- Current state-of-the-art multimodal agents still have substantial capability gaps on realistic visual web tasks
- Visual grounding is essential for effective web agent performance
- Visual information plays crucial role in task completion for web-based autonomous agents

**Limitations**: Even multimodal agents achieve low absolute success rates, indicating fundamental limitations; focuses on web-based tasks, may not capture other domains requiring visual understanding.

---

#### 3.2.4 Xu, F. F., Song, Y., Li, B., Tang, Y., Jain, K., Bao, M., Wang, Z. Z., Zhou, X., Guo, Z., Cao, M., Yang, M., Lu, H. Y., Martin, A., Su, Z., Maben, L., Mehta, R., Chi, W., Jang, L., Xie, Y., Zhou, S., & Neubig, G. (2024). TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks. *arXiv preprint arXiv:2412.14161*.

**Research Question**: How well can LLM agents perform consequential real-world tasks typically completed by multiple job roles in a software company?

**Methodology**: TheAgentCompany benchmark simulating realistic software company environment with 135 tasks spanning multiple job roles requiring planning, tool use, and long-horizon execution, employing checkpoint-based scoring with partial credit.

**Key Findings**:
- Most competitive agent (Gemini 2.5 Pro) achieved only 30.3% autonomous task completion rate
- Top-performing agents achieved 39.3% partial completion scores
- Agent performance required average of 27.2 LLM calls and $4.20 per task
- Common agent mistakes were surprising and typically not made by humans, revealing fundamental reasoning gaps
- Current LLM agents struggle with multi-step professional tasks requiring sustained planning and tool coordination

**Limitations**: Focused on software company tasks, may not generalize to other industries; simulated environment cannot fully capture complexity of actual workplace dynamics.

---

#### 3.2.5 Zhu, K., Du, H., Hong, Z., Yang, X., Guo, S., Wang, Z., Wang, Z., Qian, C., Tang, X., Ji, H., & You, J. (2025). MultiAgentBench: Evaluating the Collaboration and Competition of LLM-based Multi-Agent Systems. *arXiv preprint arXiv:2503.01935*.

**Research Question**: How can we effectively evaluate LLM-based multi-agent systems across diverse interactive scenarios capturing collaboration and competition dynamics?

**Methodology**: MultiAgentBench with 210 tasks across diverse interactive scenarios, along with MARBLE framework (Multi-agent CooRdination Backbone with LLM Engine) supporting various communication topologies (star, chain, tree, graph-based), using novel milestone-based KPIs.

**Key Findings**:
- Existing benchmarks focus on single-agent tasks or narrow domains, failing to capture multi-agent coordination dynamics
- Milestone-based KPIs provide more nuanced evaluation than binary success metrics
- MARBLE framework's support for multiple communication topologies enables systematic evaluation of coordination structures
- Multi-agent systems exhibit emergent behaviors in collaborative/competitive scenarios unpredictable from single-agent evaluations
- Benchmark reveals significant performance gaps between different LLM backbones in multi-agent coordination

**Limitations**: Limited to simulated interactive scenarios; evaluation focuses on specific communication patterns that may not represent all possible multi-agent interaction modes.

---

#### 3.2.6 Yang, J., Jimenez, C. E., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. R. (2025). SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? *arXiv preprint arXiv:2509.16941*.

**Research Question**: Can AI agents solve realistic, complex, enterprise-level software engineering tasks requiring long-horizon planning and multi-file modifications?

**Methodology**: SWE-Bench Pro with 1,865 problems sourced from 41 actively maintained repositories spanning business applications, B2B services, and developer tools, designed to be contamination-resistant using copyleft-licensed and private/commercial repositories.

**Key Findings**:
- Tasks require substantial code modifications (averaging 107.4 changed lines across 4.1 files per task)
- Current frontier models solve only approximately 25-44% of tasks on public benchmark set
- Benchmark successfully captures enterprise-level complexity beyond simpler single-file fixes
- Contamination-resistant design using diverse repository sources prevents models from memorizing training data
- Performance gaps reveal AI remains far from replacing professional engineers for long-horizon, enterprise-grade development

**Limitations**: Focus on Python, Go, TypeScript, and JavaScript repositories; held-out test set prevents full public evaluation; enterprise-level tasks may not represent all software engineering scenarios.

---

#### 3.2.7 Zhan, Q., Liang, Z., Ying, Z., & Kang, D. (2024). InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Using LLM Agents. *arXiv preprint arXiv:2403.02691*.

**Research Question**: How vulnerable are tool-integrated LLM agents to indirect prompt injection attacks when using external tools?

**Methodology**: InjecAgent benchmark assessing vulnerability of tool-integrated LLM agents to indirect prompt injection (IPI) attacks, evaluating 30 different LLM agents including both prompted (ReAct framework) and fine-tuned agents across open-source and commercial models.

**Key Findings**:
- ReAct-prompted GPT-4 vulnerable to indirect prompt injection attacks 24% of the time
- Fine-tuned agents demonstrate significantly better resilience (GPT-4: 7.1% attack success rate, GPT-3.5: 8.4%)
- Benchmark reveals fundamental security vulnerabilities in current LLM agent architectures
- Attack success varies significantly across different agent types, with prompted agents showing higher vulnerability
- Results demonstrate significant risks in current deployments of tool-integrated LLM agents in production

**Limitations**: Focuses on specific class of attacks (indirect prompt injections); 17 user tools evaluated represent only subset of possible tool integrations; defensive strategies beyond fine-tuning not comprehensively explored.

---

## 4. Thematic Synthesis

### 4.1 Evaluation Dimensions

Across the 10 papers, five key evaluation dimensions emerge:

1. **Capability Assessment**: Core agent abilities including planning, reasoning, tool use, memory, and multi-step execution [citation:Survey on Evaluation](https://arxiv.org/abs/2503.16416)
2. **Domain-Specific Performance**: Task success rates in specific domains (web navigation, software engineering, multi-agent coordination) [citation:WebArena](https://arxiv.org/abs/2307.13854)
3. **Behavioral Quality**: Not just task completion, but quality of collaboration, communication, and decision-making processes [citation:MultiAgentBench](https://arxiv.org/abs/2503.01935)
4. **Safety and Security**: Vulnerability to attacks, compliance with constraints, reliability under adversarial conditions [citation:InjecAgent](https://arxiv.org/abs/2403.02691)
5. **Enterprise Readiness**: Scalability, cost-efficiency, data access controls, regulatory compliance [citation:Evaluation and Benchmarking](https://arxiv.org/abs/2507.21504)

### 4.2 Performance Gaps

A consistent finding across benchmarks is the substantial gap between current LLM agents and human performance:

| Benchmark | Agent Performance | Human Baseline | Gap |
|-----------|------------------|----------------|-----|
| WebArena | 14.41% (GPT-4) | 78.24% | 64 points |
| TheAgentCompany | 30.3% (Gemini 2.5 Pro) | N/A | ~70% failure rate |
| VisualWebArena | 6.04% (Gemini-Pro multimodal) | N/A | >90% failure rate |
| SWE-Bench Pro | 25-44% (frontier models) | N/A | 56-75% failure rate |

These gaps reveal fundamental limitations in current agent architectures, particularly in long-horizon planning, multi-step coordination, and handling complex real-world scenarios.

### 4.3 Evaluation Methodologies

The papers employ diverse evaluation methodologies:

**Static Benchmarks**: Predefined tasks with fixed success criteria (AgentBench, WebArena, VisualWebArena)
- Advantages: Reproducible, contamination-resistant, programmatically validated
- Limitations: May not capture dynamic real-world interactions

**Interactive Environments**: Self-hosted, fully functional environments (WebArena's Docker containers, TheAgentCompany's simulated company)
- Advantages: Realistic, support long-horizon tasks
- Limitations: Infrastructure requirements, deployment complexity

**Milestone-Based Assessment**: Partial credit for intermediate progress (MultiAgentBench, TheAgentCompany)
- Advantages: More nuanced than binary success/failure
- Limitations: Requires careful milestone definition

**Security-Focused Testing**: Adversarial evaluation under attack conditions (InjecAgent)
- Advantages: Reveals vulnerabilities not apparent in standard testing
- Limitations: Focuses on specific threat models

### 4.4 Emerging Trends

Several trends emerge from the 2024-2025 literature:

1. **Multi-Agent Focus**: Shift from single-agent to multi-agent evaluation, capturing collaboration and competition dynamics [citation:MultiAgentBench](https://arxiv.org/abs/2503.01935)

2. **Multimodal Integration**: Recognition that visual grounding is essential for many real-world tasks [citation:VisualWebArena](https://arxiv.org/abs/2401.13649)

3. **Enterprise Readiness**: Growing emphasis on real-world deployment considerations including cost, reliability, and compliance [citation:Evaluation and Benchmarking](https://arxiv.org/abs/2507.21504)

4. **Security Awareness**: Increased attention to vulnerabilities, particularly prompt injection attacks [citation:InjecAgent](https://arxiv.org/abs/2403.02691)

5. **Contamination Resistance**: Design of benchmarks resistant to training data memorization through diverse, private, or copyleft-licensed sources [citation:SWE-Bench Pro](https://arxiv.org/abs/2509.16941)

6. **Taxonomy Development**: Efforts to establish systematic frameworks for organizing evaluation approaches [citation:Survey on Evaluation](https://arxiv.org/abs/2503.16416)

---

## 5. Limitations and Future Directions

### 5.1 Current Limitations

The reviewed papers acknowledge several limitations:

**Narrow Domain Focus**: Most benchmarks target specific domains (web navigation, software engineering) and may not generalize to other application areas.

**Simulated Environments**: Even "realistic" benchmarks are simulated and cannot fully capture the complexity and unpredictability of actual deployment scenarios.

**English-Centric**: Most benchmarks focus on English-language tasks, limiting applicability to multilingual contexts.

**Infrastructure Requirements**: Many benchmarks require significant infrastructure (Docker containers, self-hosted websites) limiting accessibility.

**Rapid Obsolescence**: The field is evolving so quickly that surveys and benchmarks may become outdated within months.

**Lack of Unified Standards**: No consensus on what constitutes an "LLM agent" or standardized evaluation protocols.

### 5.2 Future Research Directions

Based on the synthesis, several promising directions emerge:

1. **Unified Evaluation Frameworks**: Development of comprehensive, standardized frameworks that integrate multiple evaluation dimensions [citation:Evaluation and Benchmarking](https://arxiv.org/abs/2507.21504)

2. **Dynamic Multi-Turn Evaluation**: Moving beyond static, isolated testing to live, interactive evaluation protocols [citation:Survey on Evaluation](https://arxiv.org/abs/2503.16416)

3. **Enterprise-Specific Benchmarks**: Benchmarks addressing real-world enterprise constraints including data access controls, compliance requirements, and reliability guarantees [citation:Evaluation and Benchmarking](https://arxiv.org/abs/2507.21504)

4. **Multimodal Agent Evaluation**: Expanded benchmarks for agents requiring visual, auditory, and other sensory modalities [citation:VisualWebArena](https://arxiv.org/abs/2401.13649)

5. **Security and Robustness**: Comprehensive evaluation of agent resilience under adversarial conditions and diverse attack vectors [citation:InjecAgent](https://arxiv.org/abs/2403.02691)

6. **Cost-Effectiveness Metrics**: Evaluation frameworks that consider computational cost, latency, and economic viability alongside performance [citation:TheAgentCompany](https://arxiv.org/abs/2412.14161)

7. **Cross-Domain Generalization**: Benchmarks testing agent adaptability across diverse domains and task types [citation:AgentBench](https://arxiv.org/abs/2308.03688)

8. **Human-Agent Collaboration**: Evaluation of agents working alongside humans rather than purely autonomous performance [citation:TheAgentCompany](https://arxiv.org/abs/2412.14161)

---

## 6. Conclusion

This systematic literature review of 10 papers on LLM agent evaluation benchmarks reveals a field in rapid transition. Two comprehensive surveys establish foundational taxonomies and identify critical gaps in current evaluation approaches. Eight benchmark papers introduce novel evaluation methodologies across diverse domains, from web navigation and software engineering to multi-agent coordination and security testing.

Consistent findings include substantial performance gaps between current agents and human baselines (ranging from 14-44% agent success rates), the importance of multimodal capabilities for real-world tasks, emerging security vulnerabilities in tool-integrated agents, and the need for enterprise-ready evaluation frameworks.

The field is evolving from single-agent, task-specific benchmarks toward multi-dimensional, contamination-resistant frameworks that capture long-horizon planning, multi-agent coordination, visual grounding, security resilience, and real-world deployment considerations. However, significant challenges remain, including the lack of unified standards, narrow domain focus, infrastructure requirements, and rapid obsolescence.

Future research should prioritize unified evaluation frameworks, dynamic multi-turn protocols, enterprise-specific benchmarks, comprehensive security testing, and cost-effectiveness metrics. As LLM agents continue to advance, robust evaluation methodologies will be essential for assessing real-world readiness and guiding development toward practical, reliable, and safe deployment.

---

## References

Fried, D., Alon, U., Bisk, Y., Cheng, X., Fried, D., Neubig, G., Ou, T., Sridhar, A., Zhou, S., Zhou, X., Zhu, H., & Xu, F. F. (2023). WebArena: A realistic web environment for independent language-guided agents. *arXiv preprint arXiv:2307.13854*. https://arxiv.org/abs/2307.13854

Hou, X., Yan, Y., Li, Y., Xing, Z., Xu, X., Lu, Q., Zhu, L., & Wang, C. (2024). From LLMs to LLM-based agents for software engineering: A comprehensive survey. *arXiv preprint arXiv:2408.02479*. https://arxiv.org/abs/2408.02479

Koh, J. Y., Lo, R., Jang, L., Duvvur, V., Lim, M. C., Huang, P.-Y., Neubig, G., Zhou, S., Salakhutdinov, R., & Fried, D. (2024). VisualWebArena: Evaluating multimodal agents on realistic visual web tasks. *arXiv preprint arXiv:2401.13649*. https://arxiv.org/abs/2401.13649

Liu, X., Yu, H., Zhang, H., Xu, Y., Lei, X., Lai, H., Gu, Y., Ding, H., Men, K., Yang, K., Zhang, S., Deng, X., Zeng, A., Du, Z., Dong, Y., & Tang, J. (2023). AgentBench: Evaluating LLMs as agents. *arXiv preprint arXiv:2308.03688*. https://arxiv.org/abs/2308.03688

Mohammadi, M., & Li, Y. (2025). Survey on evaluation of LLM-based agents. *arXiv preprint arXiv:2503.16416*. https://arxiv.org/abs/2503.16416

Mohammadi, M., Li, Y., Lo, J., & Yip, W. (2025). Evaluation and benchmarking of LLM agents: A survey. *arXiv preprint arXiv:2507.21504*. https://arxiv.org/abs/2507.21504

Xu, F. F., Song, Y., Li, B., Tang, Y., Jain, K., Bao, M., Wang, Z. Z., Zhou, X., Guo, Z., Cao, M., Yang, M., Lu, H. Y., Martin, A., Su, Z., Maben, L., Mehta, R., Chi, W., Jang, L., Xie, Y., Zhou, S., & Neubig, G. (2024). TheAgentCompany: Benchmarking LLM agents on consequential real world tasks. *arXiv preprint arXiv:2412.14161*. https://arxiv.org/abs/2412.14161

Yang, J., Jimenez, C. E., Wettig, A., Yao, S., Pei, K., Press, O., & Narasimhan, K. R. (2025). SWE-Bench Pro: Can AI agents solve long-horizon software engineering tasks? *arXiv preprint arXiv:2509.16941*. https://arxiv.org/abs/2509.16941

Zhan, Q., Liang, Z., Ying, Z., & Kang, D. (2024). InjecAgent: Benchmarking indirect prompt injections in tool-using LLM agents. *arXiv preprint arXiv:2403.02691*. https://arxiv.org/abs/2403.02691

Zhu, K., Du, H., Hong, Z., Yang, X., Guo, S., Wang, Z., Wang, Z., Qian, C., Tang, X., Ji, H., & You, J. (2025). MultiAgentBench: Evaluating the collaboration and competition of LLM-based multi-agent systems. *arXiv preprint arXiv:2503.01935*. https://arxiv.org/abs/2503.01935

---

## Appendix: Paper Summary Table

| Paper | Type | Key Contribution | Performance Gap | Limitations |
|-------|------|------------------|-----------------|-------------|
| Mohammadi & Li (2025) - Survey | Survey | First comprehensive survey of LLM agent evaluation methods | N/A | Descriptive, rapidly evolving field |
| Mohammadi et al. (2025) - Enterprise | Survey | Two-dimensional taxonomy for enterprise evaluation | N/A | Enterprise-focused, requires validation |
| Hou et al. (2024) | Survey | LLM vs LLM-agent differentiation in SE | N/A | Broad coverage limits depth |
| Liu et al. (2023) - AgentBench | Benchmark | 8-environment multi-dimensional benchmark | GPT-4: 4.01, OSS: 0.96 (4x gap) | English-only, 8 environments |
| Zhou et al. (2023) - WebArena | Benchmark | Realistic web environment with 812 tasks | 14.41% vs 78.24% human (64 pts) | Infrastructure requirements |
| Koh et al. (2024) - VisualWebArena | Benchmark | Multimodal web tasks with visual grounding | 6.04% multimodal vs 3.85% text-only | Low absolute success rates |
| Xu et al. (2024) - TheAgentCompany | Benchmark | 135 real-world company tasks | 30.3% autonomous completion | Software company focus |
| Zhu et al. (2025) - MultiAgentBench | Benchmark | 210 multi-agent tasks, MARBLE framework | Varies by LLM backbone | Simulated scenarios |
| Yang et al. (2025) - SWE-Bench Pro | Benchmark | 1,865 enterprise-level SE tasks | 25-44% frontier model success | Held-out test set |
| Zhan et al. (2024) - InjecAgent | Benchmark | Security benchmark for prompt injections | 24% (prompted) vs 7-8% (fine-tuned) | Specific attack class |

---

**Generated**: October 25, 2026  
**Total Papers**: 10  
**Time Range**: 2023-2025 (published 2024-2026)  
**Category**: cs.CL (Computation and Language)
