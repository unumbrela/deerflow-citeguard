# Systematic Literature Review: Planning with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "LLM planning", published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on planning with large language models reveals a rapidly evolving field characterized by diverse methodological approaches and a tension between pure neural planning and hybrid neuro-symbolic systems. The surveyed papers collectively demonstrate that while LLMs show promising planning capabilities, significant challenges remain in cost-awareness, optimality, and robustness across domains. Recent work has shifted from simply demonstrating that LLMs can plan toward understanding the underlying cognitive mechanisms that enable planning, developing systematic evaluation frameworks, and integrating LLMs with classical planning formalisms. A notable finding across multiple studies is that reasoning quality often matters more than model scale, and that structured approaches ( Means-Ends Analysis, tree-search algorithms, symbolic grounding) consistently outperform end-to-end neural planning on complex tasks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query `LLM planning`, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, the search was not restricted to a specific arXiv category, resulting in papers from cs.AI, cs.LG, cs.MA, and cs.CL.

## Themes

### Theme 1: Search Algorithms and Tree-Based Planning

A substantial portion of recent work focuses on integrating LLMs with classical search algorithms to improve planning efficiency and optimality. Zhang et al. (2025) conducted a systematic study of tree-search LLM planners, comparing depth-first search, breadth-first search, Monte Carlo Tree Search, and bidirectional search. Their findings reveal that existing tree-based planners often struggle to find cost-optimal plans, and that additional search computation does not reliably improve optimality. Notably, bidirectional search achieved the best overall efficiency and success rate, while MCTS achieved the highest optimality on short-horizon tasks. This suggests that improving LLM planning under resource constraints will likely require new search algorithms rather than solely scaling inference-time compute.

Huang et al. (2026) extended this line of work by applying multidimensional item response theory to uncover the latent competency structure underlying LLM planning, identifying two principal dimensions: operational reasoning (evaluating local action applicability) and structural enumeration (reasoning about goal reachability). Their work reveals that operational reasoning improves under model scaling and longer reasoning traces, while structural enumeration remains comparatively insensitive to scaling and reasoning time.

### Theme 2: Hybrid Neuro-Symbolic Approaches

Several papers advocate for combining LLMs with symbolic planning formalisms to overcome the limitations of pure neural planning. Göbel et al. (2026) developed PyPDDLEngine, a PDDL simulation engine that exposes planning operations as LLM tool calls through an MCP interface, allowing the LLM to act as an interactive search policy selecting one action at a time with state observation and reset/retry capability. Their evaluation on 102 IPC Blocksworld instances showed that agentic LLM planning achieved 66.7% success compared to 63.7% for direct LLM planning, though at 5.7× higher token cost per solution.

Zhang et al. (2025) presented SPIRAL, which embeds a cognitive architecture of three specialized LLM agents (Planner, Simulator, Critic) into a Monte Carlo Tree Search loop, transforming MCTS from brute-force search into a guided, self-correcting reasoning process with dense reward signals. SPIRAL achieved 83.6% overall accuracy on DailyLifeAPIs, improving over 16 percentage points against the next-best search framework.

Kang (2025) introduced NL2Flow, a fully automated pipeline for generating and evaluating workflow planning problems parametrically in a structured intermediate representation, translating them into both natural language and formal PDDL. Their findings showed that translating natural language problems into structured JSON representation prior to symbolic planning significantly improved success rates, demonstrating measurable benefits of neuro-symbolic integration.

### Theme 3: Reasoning Capabilities and Model Scaling

A critical question in LLM planning is whether reasoning quality or model scale matters more. Anjum (2025) benchmarked a distilled 1.5B parameter reasoning model (DeepSeek-R1) against several state-of-the-art non-reasoning LLMs within a generator-discriminator LLM planning framework for text-to-SQL tasks. Surprisingly, the 1.5B reasoning model achieved up to 87% higher F1 and 3.7% better discrimination accuracy than CodeLlama-7B, and 3.7% higher execution accuracy than CodeLlama-13B despite having significantly fewer parameters. This demonstrates that reasoning capabilities can beat scale in certain planning contexts.

However, Anjum (2025) also identified a limit to the logical capabilities of reasoning models—more context or compute budget alone does not improve discrimination performance. Additionally, reasoning models find generation more challenging than discrimination and may underperform as generators compared to smaller non-reasoning LLMs.

Li and Kingsford (2026) explored whether classical Means-Ends Analysis techniques can improve LLM planning performance in continuous-state domains where actions cannot be enumerated. They developed Medaka, a structured prompting framework based on Means-Ends Analysis that encourages recursive goal decomposition, algebraic derivation, and per-step state tracking. Their evaluation on Liquidworld, a new testbed for liquid mixing tasks, showed that Medaka improves performance across model families, demonstrating that classical means-ends analysis elicits LLM-native reasoning abilities helpful for continuous-state planning.

### Theme 4: Evaluation Frameworks and Benchmarks

The field has recognized the need for systematic evaluation frameworks to compare different LLM planning approaches. Wei et al. (2025) presented PlanGenLLMs, a modern survey that examines representative LLM planning works across six key performance criteria: completeness, executability, optimality, representation, generalization, and efficiency. Their analysis revealed that many LLM planning systems are tailored to specific problems, making comparison difficult, and identified a lack of clear and consistent evaluation criteria in the field.

Huang et al. (2024) developed an end-to-end LLM planner and employed diverse metrics to reassess recent strategies including fine-tuning, Chain-of-Thought, and reinforcement learning with a novel 'Longest Contiguous Common Subsequence' reward. Their evaluation on out-of-distribution test sets showed that fine-tuning LLMs on planning corpora does not lead to robust planning skills on out-of-distribution test sets, though various strategies including Chain-of-Thought enhance the probability of a plan being executable.

### Theme 5: Multi-Agent Planning Systems

Recent work has explored coordinating multiple LLM agents for complex planning tasks. Geng and Chang (2025) presented ALAS, a stateful, disruption-aware framework that separates planning from non-circular validation, records versioned execution logs for grounded checks and restore points, and performs localized repair that preserves work in progress. Their evaluation on job-shop scheduling suites across five classical benchmarks showed that ALAS achieves 83.7% success rate, reduces token usage by 60% compared to baselines, and runs 1.82 times faster under comparable settings.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that structured approaches outperform pure end-to-end neural planning. Both Zhang et al. (2025) and Göbel et al. (2026) demonstrate that integrating search algorithms with LLMs yields better performance than direct LLM planning. Similarly, Kang (2025) and Zhang et al. (2025) both show that neuro-symbolic integration provides measurable benefits. There is also agreement across papers that evaluation frameworks need standardization, as noted by Wei et al. (2025) and Huang et al. (2024).

**Disagreements**: While most papers advocate for hybrid approaches, there is disagreement about the cost-benefit tradeoff. Göbel et al. (2026) report that agentic LLM planning shows only a modest three-percentage-point advantage at 5.7× higher token cost per solution, raising questions about practical efficiency. In contrast, Geng and Chang (2025) claim their multi-agent approach reduces token usage by 60% while improving performance. Additionally, while Anjum (2025) shows that smaller reasoning models can outperform larger non-reasoning models in discrimination tasks, this finding may not generalize to all planning domains, as the study focuses specifically on text-to-SQL tasks.

## Gaps and Open Questions

The collective literature reveals several gaps:

1. **Limited generalizability**: Multiple studies note that their findings may not generalize beyond specific domains (text-to-SQL, Blocksworld, job-shop scheduling), suggesting a need for cross-domain evaluation benchmarks.

2. **Token efficiency concerns**: While several papers report high token costs for agentic approaches, systematic optimization of token usage remains underexplored.

3. **Plan validity vs. executability**: Huang et al. (2024) note that while progress exists in plan executability, plan validity remains a challenge, indicating future strategies need to address both aspects.

4. **Structural enumeration limitations**: Huang et al. (2026) identify that structural enumeration remains insensitive to scaling and reasoning time, suggesting fundamental architectural limitations that current approaches do not address.

5. **Reproducibility**: Geng and Chang (2025) note that code and seeds were not yet released at the time of publication, limiting immediate reproducibility—a common issue in the field.

6. **Continuous-state domains**: Li and Kingsford (2026) highlight that traditional LLM planning frameworks assume enumerable actions, which breaks down in continuous-state domains, indicating a significant gap in current approaches.

## Per-Paper Annotations

### Anjum (2025)

**Research question**: How do reasoning models compare to non-reasoning LLMs as discriminators in generator-discriminator planning frameworks for text-to-SQL tasks?

**Methodology**: The study benchmarks a distilled 1.5B parameter reasoning model (DeepSeek-R1) against several state-of-the-art non-reasoning LLMs within a generator-discriminator LLM planning framework, introducing a novel method for extracting soft scores from chain-of-thought outputs to enable fine-grained candidate ranking.

**Key findings**:
- Distilled DeepSeek-R1-1.5B achieves up to 87% higher F1 and 3.7% better discrimination accuracy than CodeLlama-7B
- DeepSeek-R1-1.5B achieves 3.7% higher execution accuracy than CodeLlama-13B despite having significantly fewer parameters
- There is a limit to the logical capabilities of reasoning models—more context or compute budget alone does not improve discrimination performance
- Reasoning models find generation more challenging than discrimination and may underperform as generators compared to smaller non-reasoning LLMs

**Limitations**: The study focuses on text-to-SQL tasks and the generator-discriminator framework, which may limit generalizability to other planning domains.

### Geng and Chang (2025)

**Research question**: How can multi-agent LLM planning frameworks be made more robust and efficient by addressing verification circularity, state tracking, and fault recovery?

**Methodology**: The authors present ALAS, a stateful, disruption-aware framework that separates planning from non-circular validation, records versioned execution logs for grounded checks and restore points, and performs localized repair that preserves work in progress, evaluated on job-shop scheduling suites across five classical benchmarks.

**Key findings**:
- ALAS achieves 83.7% success rate on job-shop scheduling benchmarks
- ALAS reduces token usage by 60% compared to baselines
- ALAS runs 1.82 times faster under comparable settings
- The validator detects injected structural faults with low overhead
- Localized repair contains runtime perturbations with bounded edit radius and less makespan degradation than global recompute

**Limitations**: Code and seeds were not yet released at the time of publication, limiting immediate reproducibility.

### Göbel et al. (2026)

**Research question**: Can large language models serve as viable planners alongside classical symbolic methods when given interactive step-wise feedback through a PDDL simulation engine?

**Methodology**: The authors developed PyPDDLEngine, a PDDL simulation engine exposing planning operations as LLM tool calls through an MCP interface, allowing the LLM to act as an interactive search policy selecting one action at a time with state observation and reset/retry capability. They evaluated four approaches on 102 IPC Blocksworld instances under a 180-second budget.

**Key findings**:
- Fast Downward achieves 85.3% success rate as a classical baseline
- Direct LLM planning achieves 63.7% success while agentic LLM planning achieves 66.7%
- The agentic approach shows a modest three-percentage-point advantage at 5.7× higher token cost per solution
- Both LLM approaches produce shorter plans than seq-sat-lama-2011 on most co-solved difficulty blocks
- Agentic gains depend on the nature of environmental feedback, with coding agents benefiting more from external signals than self-assessed PDDL feedback

**Limitations**: Not stated in abstract.

### Huang et al. (2024)

**Research question**: Which strategies effectively improve LLM planning capabilities, and do they lead to robust planning skills on out-of-distribution tasks?

**Methodology**: The study develops an end-to-end LLM planner and employs diverse metrics to reassess recent strategies including fine-tuning, Chain-of-Thought, and reinforcement learning with a novel 'Longest Contiguous Common Subsequence' reward, evaluating performance on out-of-distribution test sets.

**Key findings**:
- Fine-tuning LLMs on planning corpora does not lead to robust planning skills on out-of-distribution test sets
- Various strategies including Chain-of-Thought enhance the probability of a plan being executable
- Reinforcement learning with the 'Longest Contiguous Common Subsequence' reward emerged as most effective for both plan validity and executability
- Progress exists in plan executability despite plan validity remaining a challenge

**Limitations**: Plan validity remains a challenge despite improvements in executability, indicating future strategies need to address both aspects.

### Huang et al. (2026)

**Research question**: Do uneven LLM performance patterns across planning tasks reflect distinct latent planning competencies rather than differences along a single ability spectrum?

**Methodology**: The authors evaluated multiple LLM families under varying test-time reasoning budgets on ACPBench-Hard and applied a multidimensional item response theory model to uncover the latent competency structure underlying LLM planning.

**Key findings**:
- Two principal dimensions shape planning performance: operational reasoning and structural enumeration
- Operational reasoning is the ability to evaluate local action applicability and immediate state transitions
- Structural enumeration is the ability to reason about goal reachability and landmark structure
- Operational reasoning improves under model scaling and longer reasoning traces
- Structural enumeration remains comparatively insensitive to scaling and reasoning time

**Limitations**: Not stated in abstract.

### Kang (2025)

**Research question**: How can scalable evaluation data for LLM planning and reasoning be generated to better understand error sources as systems scale to complex tasks?

**Methodology**: NL2Flow is introduced as a fully automated pipeline for generating and evaluating workflow planning problems parametrically in a structured intermediate representation, translating them into both natural language and formal PDDL, then evaluating open-source instruct-tuned LLMs on 2296 generated problems.

**Key findings**:
- The best-performing model achieved 86% success in generating valid plans and 69% in generating optimal plans for solvable problems
- The influence of problem characteristics on plan generation is contingent on both model and prompt design
- Translating natural language problems into structured JSON representation prior to symbolic planning significantly improved success rates
- Neuro-symbolic integration provides measurable benefits for LLM planning

**Limitations**: The study focuses on low-difficulty problems, and findings may not generalize to more complex planning tasks.

### Li and Kingsford (2026)

**Research question**: Can classical Means-Ends Analysis techniques improve LLM planning performance in continuous-state domains where actions cannot be enumerated?

**Methodology**: The authors developed Medaka, a structured prompting framework based on Means-Ends Analysis that encourages recursive goal decomposition, algebraic derivation, and per-step state tracking. They evaluated it on Liquidworld, a new testbed for liquid mixing tasks in continuous-state domains.

**Key findings**:
- Traditional LLM planning frameworks assume enumerable actions, which breaks down in continuous-state domains
- Means-Ends Analysis provides a remedy for planning in continuous-state domains
- Medaka improves performance across model families on the Liquidworld testbed
- Classical means-ends analysis elicits LLM-native reasoning abilities helpful for continuous-state planning

**Limitations**: Not stated in abstract.

### Wei et al. (2025)

**Research question**: What is the current state of LLM planning capabilities and how can they be systematically compared across different approaches and tasks?

**Methodology**: This survey builds on foundational work by Kartam and Wilkins (1990) and examines representative LLM planning works across six key performance criteria: completeness, executability, optimality, representation, generalization, and efficiency.

**Key findings**:
- Many LLM planning systems are tailored to specific problems, making comparison difficult
- There is a lack of clear and consistent evaluation criteria in the field
- The survey provides comprehensive analysis of representative works with their strengths and weaknesses across six criteria
- The paper identifies crucial future directions for LLM planning research
- The survey serves as a resource for practitioners and newcomers interested in LLM planning for agentic workflows

**Limitations**: Not stated in abstract.

### Zhang et al. (2025) [SPIRAL]

**Research question**: How can LLM planning be improved by embedding specialized cognitive architectures into search algorithms to overcome linear reasoning limitations?

**Methodology**: SPIRAL embeds a cognitive architecture of three specialized LLM agents (Planner, Simulator, Critic) into a Monte Carlo Tree Search loop, transforming MCTS from brute-force search into a guided, self-correcting reasoning process with dense reward signals.

**Key findings**:
- SPIRAL achieves 83.6% overall accuracy on DailyLifeAPIs, improving over 16 percentage points against the next-best search framework
- SPIRAL consistently outperforms default Chain-of-Thought planning and other state-of-the-art agents on DailyLifeAPIs and HuggingFace datasets
- The framework demonstrates superior token efficiency compared to competing methods
- Structuring LLM reasoning as guided, reflective, and grounded search yields more robust and efficient autonomous planners

**Limitations**: Not stated in abstract.

### Zhang et al. (2025) [Cost-Awareness]

**Research question**: Are tree-search LLM planners cost-aware and do they efficiently generate budget-feasible plans under resource constraints?

**Methodology**: The authors systematically analyzed tree-search LLM planners using a unified framework comparing depth-first search, breadth-first search, Monte Carlo Tree Search, and bidirectional search, with explicit search trees exposing intermediate decisions and failure modes.

**Key findings**:
- Existing tree-based LLM planners often struggle to find cost-optimal plans
- Additional search computation does not reliably improve optimality
- Bidirectional search achieves the best overall efficiency and success rate
- MCTS achieves the highest optimality on short-horizon tasks
- Improving LLM planning under resource constraints will likely require new search algorithms rather than solely scaling inference-time compute

**Limitations**: Not stated in abstract.

## References

Anjum, M. F. (2025). When reasoning beats scale: A 1.5B reasoning model outranks 13B LLMs as discriminator. arXiv. https://arxiv.org/abs/2505.03786

Geng, L., & Chang, E. Y. (2025). ALAS: Transactional and dynamic multi-agent LLM planning. arXiv. https://arxiv.org/abs/2511.03094

Göbel, K., Lorang, P., Zips, P., & Glück, T. (2026). Agentic LLM planning via step-wise PDDL simulation: An empirical characterisation. arXiv. https://arxiv.org/abs/2603.06064

Huang, S., Cohn, T., & Lipovetzky, N. (2024). Chasing progress, not perfection: Revisiting strategies for end-to-end LLM plan generation. arXiv. https://arxiv.org/abs/2412.10675

Huang, S., Zhang, C., Ke, F., Cai, Z., Rastgoo, N., Haffari, G., & Rezatofighi, H. (2026). What we talk about when we talk about LLM planning: Evidence for two distinct planning abilities. arXiv. https://arxiv.org/abs/2607.11197

Kang, J. (2025). Scaling LLM planning: NL2FLOW for parametric problem generation and rigorous evaluation. arXiv. https://arxiv.org/abs/2507.02253

Li, J., & Kingsford, C. (2026). Means-ends analysis helps LLMs plan in continuous-state domains. arXiv. https://arxiv.org/abs/2610.24928

Wei, H., Zhang, Z., He, S., Xia, T., Pan, S., & Liu, F. (2025). PlanGenLLMs: A modern survey of LLM planning capabilities. arXiv. https://arxiv.org/abs/2502.11221

Zhang, Y., Ganapavarapu, G., Jayaraman, S., Agrawal, B., Patel, D., & Fokoue, A. (2025). SPIRAL: Symbolic LLM planning via grounded and reflective search. arXiv. https://arxiv.org/abs/2512.23167

Zhang, Z., Wei, H., Jiang, K., Pan, S., Kai, S., & Liu, F. (2025). Cost-awareness in tree-search LLM planning: A systematic study. arXiv. https://arxiv.org/abs/2505.14656
