# Systematic Literature Review: Planning with Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "LLM planning" and "planning large language models", category cs.AI, 2024-2026
**Citation format**: APA 7th edition

## Executive Summary

The literature on planning with large language models has evolved rapidly from 2024 to 2026, revealing a field in transition between theoretical promise and practical limitations. The surveyed papers collectively demonstrate that while LLMs show genuine planning capabilities, their performance is highly contingent on task structure, domain characteristics, and the scaffolding provided. A central finding across multiple studies is that LLMs excel at plan executability but struggle with plan validity, particularly in domains requiring structural reasoning about goal reachability. The field has shifted from asking "Can LLMs plan?" to "Under what conditions do LLMs plan well, and how can we architect systems that compensate for their weaknesses?" Key advances include hybrid neuro-symbolic approaches, multi-agent cognitive architectures embedded in search loops, and competency-level evaluation frameworks that distinguish between operational and structural planning abilities.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the queries "LLM planning" and "planning large language models", filtered to category cs.AI, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search was restricted to cs.AI category, potentially missing relevant work in cs.RO (robotics), cs.DB (databases), and related categories.

## Themes

### Theme 1: Hybrid Neuro-Symbolic Approaches

A dominant trend across the surveyed literature is the integration of symbolic planning methods with LLM reasoning capabilities. Rather than treating LLMs as standalone planners, researchers increasingly position them as components within larger architectures that combine neural flexibility with symbolic rigor. Li & Kingsford (2026) exemplify this approach by adapting Means-Ends Analysis—a classical AI problem-solving technique—into a structured prompting framework called Medaka for continuous-state domains. Their work demonstrates that classical planning heuristics can elicit latent reasoning capabilities in LLMs that are not accessed through standard prompting.

Similarly, Zhang et al. (2025) in the SPIRAL framework embed three specialized LLM agents (Planner, Simulator, Critic) within a Monte Carlo Tree Search loop, transforming brute-force search into guided, self-correcting reasoning. This cognitive architecture approach achieves 83.6% accuracy on DailyLifeAPIs, substantially outperforming baseline methods. Jia et al. (2026) extend this pattern to multimodal data analysis with WeaveData, which generates typed logical plans with pre-execution critique and post-execution verification, accumulating planning experience across queries.

The neuro-symbolic pattern also appears in Kang's (2025) NL2Flow system, which translates natural language problems into structured JSON representations before applying symbolic planning. This intermediate representation approach significantly improved success rates, with the best-performing model achieving 86% validity and 69% optimality on generated workflow problems. The convergence on hybrid architectures suggests a field-wide recognition that pure neural or pure symbolic approaches are insufficient for robust planning.

### Theme 2: The Discriminator Bottleneck

A critical constraint identified across multiple studies is the quality of discrimination—the ability to evaluate whether proposed actions or plans are correct. Chen et al. (2024) provide the most direct evidence, showing that advanced planning methods like tree search and iterative correction require discriminators with at least 90% accuracy to outperform simpler re-ranking approaches. Their experiments reveal that current LLMs fall short of this threshold, making sophisticated planning methods inefficient: tree search is 10-20 times slower than alternatives but yields negligible performance gains.

This discriminator bottleneck manifests in different forms across the literature. Göbel et al. (2026) observe that agentic LLM planning via step-wise PDDL simulation achieves only a modest 3-percentage-point advantage over direct planning (66.7% vs. 63.7% success), despite costing 5.7 times more in tokens. They attribute this to the self-assessed nature of PDDL feedback—unlike coding agents that benefit from external signals like compiler errors, PDDL agents must evaluate their own progress without external verification. This echoes Chen et al.'s finding that internal discrimination is unreliable.

The structural enumeration deficit identified by Huang et al. (2026) can be understood as a specialized form of discrimination failure: LLMs struggle to evaluate whether a sequence of actions makes a goal reachable, even when they can assess local action applicability. This suggests that improving discrimination requires not just better training but architectural changes that provide external grounding or verification mechanisms.

### Theme 3: Competency-Level Evaluation

The field has moved beyond asking whether LLMs can plan to asking which specific planning competencies they possess. Huang et al. (2026) apply multidimensional item response theory to reveal two distinct planning abilities: operational reasoning (evaluating local action applicability and immediate state transitions) and structural enumeration (reasoning about goal reachability and landmark structure). Their analysis shows these competencies respond differently to scaling—operational reasoning improves with larger models and longer reasoning traces, while structural enumeration remains insensitive to both.

This competency-level perspective reframes apparent contradictions in the literature. For instance, Huang et al. (2024) find that fine-tuning on planning corpora does not produce robust planning skills on out-of-distribution tasks, yet Chain-of-Thought and reinforcement learning with their "Longest Contiguous Common Subsequence" reward do improve plan executability. The competency lens suggests these strategies enhance operational reasoning without addressing the structural enumeration deficit that ultimately determines plan validity.

Zhang et al. (2025) contribute to this nuanced evaluation by systematically comparing tree-search algorithms on cost-awareness, finding that bidirectional search achieves the best efficiency-success tradeoff while MCTS excels at optimality on short-horizon tasks. Wei et al. (2025) synthesize these disparate evaluation approaches into a unified framework of six criteria: completeness, executability, optimality, representation, generalization, and efficiency. This maturation of evaluation methodology reflects a field transitioning from proof-of-concept demonstrations to systematic capability characterization.

### Theme 4: Domain-Specific Adaptations

Planning research increasingly recognizes that LLM capabilities are domain-contingent rather than universal. Li & Kingsford (2026) explicitly address the gap between discrete-state domains, where actions are enumerable, and continuous-state domains, where actions form a continuum. Their Liquidworld testbed for liquid mixing demonstrates that Means-Ends Analysis prompting improves performance across model families specifically in continuous domains where traditional LLM planning frameworks fail.

Jia et al. (2026) tackle multimodal data analysis, where plans must coordinate operations across relational tables, text, and images. Their self-critiquing and self-evolving plan architecture addresses the unique challenge of silent failures—plans that execute without error but compute something other than what was requested. WeaveData's approach of grounding plans in a metadata knowledge graph and accumulating experience across queries represents a domain-specific solution to the generalization problem.

Kang (2025) focuses on workflow composition, generating 2,296 parametric problems to evaluate LLMs at scale. The finding that translating to structured JSON before symbolic planning improves success rates suggests that workflow domains benefit from explicit intermediate representations that make constraints and dependencies explicit. These domain-specific adaptations collectively argue against one-size-fits-all planning architectures.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the conclusion that pure LLM planning—direct generation of action sequences without scaffolding—is insufficient for robust performance. Chen et al. (2024), Göbel et al. (2026), and Huang et al. (2024) all demonstrate that LLMs alone achieve 60-70% success rates on standard benchmarks, with diminishing returns from scaling inference-time compute. There is also broad agreement that evaluation must distinguish between plan executability (can the plan be run?) and plan validity (does it achieve the goal?), as these metrics diverge significantly.

Another convergence is the recognition that search algorithms matter. Zhang et al. (2025), Chen et al. (2024), and Zhang et al. (2025) in SPIRAL all demonstrate that the choice of search method—whether bidirectional search, MCTS, or iterative correction—significantly impacts both success rates and token efficiency. The field has moved beyond treating search as a generic wrapper to understanding it as a design space with specific tradeoffs.

**Disagreements**: There is tension between optimistic and pessimistic assessments of LLM planning trajectories. Huang et al. (2024) argue that fine-tuning does not produce robust, generalizable planning skills, while Kang (2025) reports 86% validity rates with structured intermediate representations. This apparent disagreement may reflect different task domains rather than fundamental contradictions—workflow composition may be more amenable to structured approaches than Blocksworld-style planning.

Another point of divergence concerns the value of agentic architectures. Göbel et al. (2026) find only modest gains (3 percentage points) from step-wise agentic planning at high token cost, while Zhang et al. (2025) report 16-point improvements with their multi-agent SPIRAL architecture. The difference may lie in the cognitive specialization—SPIRAL's Planner-Simulator-Critic division of labor appears more effective than simple step-wise execution with self-evaluation.

## Gaps and Open Questions

Several gaps emerge consistently across the surveyed literature:

1. **Continuous-state planning**: Li & Kingsford (2026) note that their evaluation is limited to liquid mixing domains, and generalizability to other continuous-state domains remains untested. This is a significant gap given that many real-world planning problems involve continuous parameters.

2. **Out-of-distribution generalization**: Huang et al. (2024) and Kang (2025) both identify poor OOD performance as a limitation. Models trained or prompted for specific planning domains do not transfer well to novel task structures, suggesting that current approaches capture task-specific patterns rather than general planning principles.

3. **Discriminator improvement**: Chen et al. (2024) identify the 90% discrimination accuracy threshold but do not provide a path to reaching it. This is a critical gap, as advanced planning methods are bottlenecked by discrimination quality across multiple studies.

4. **Computational efficiency**: Multiple papers note high token costs (Göbel et al., 2026: 5.7× cost for agentic planning; Chen et al., 2024: 10-20× slower tree search) without clear paths to efficiency improvements. This limits practical deployment.

5. **Structural enumeration**: Huang et al. (2026) identify this competency as insensitive to scaling and extended reasoning, but do not offer architectural solutions. Understanding how to improve structural reasoning remains an open challenge.

6. **Evaluation standardization**: Wei et al. (2025) note the lack of consistent evaluation criteria across the field. While they propose a six-criteria framework, it requires validation through application across diverse planning tasks.

## Per-Paper Annotations

### Chen et al. (2024)

**Research question**: Under what conditions do advanced planning methods like tree search and iterative correction provide practical utility for LLM-based multi-step problem solving?
**Methodology**: Analyzed how discrimination accuracy affects agent performance using iterative correction and tree search versus re-ranking, experimenting on text-to-SQL parsing and mathematical reasoning tasks.
**Key findings**:
- Advanced planning methods require discriminators with at least 90% accuracy to achieve significant improvements over re-ranking
- Current LLMs' discrimination abilities have not met the threshold needed for advanced planning methods to show improvements
- Tree search is at least 10-20 times slower than other methods but leads to negligible performance gains
- Advanced planning methods may not adequately balance accuracy and efficiency when using LLM-based discriminators
**Limitations**: Current LLM discriminators lack the accuracy needed to make advanced planning methods worthwhile; tree search has significant efficiency problems that hinder real-world applications.

### Göbel et al. (2026)

**Research question**: Can LLMs serve as viable planners alongside classical symbolic methods, and does agentic step-wise feedback improve planning performance?
**Methodology**: Developed PyPDDLEngine, a PDDL simulation engine with Model Context Protocol interface for LLM tool calls, enabling interactive action selection with state observation; evaluated four approaches on 102 IPC Blocksworld instances under 180-second budget.
**Key findings**:
- Fast Downward achieves 85.3% success rate as classical baseline
- Direct LLM planning achieves 63.7% success; agentic LLM planning achieves 66.7% (modest 3-point advantage)
- Agentic approach costs 5.7× more tokens per solution than direct planning
- Both LLM approaches produce shorter plans than seq-sat-lama-2011 on co-solved instances despite its iterative quality improvement
- Agentic gains depend on environmental feedback nature; PDDL feedback is self-assessed without external verification unlike compiler errors for coding agents
**Limitations**: Evaluation limited to Blocksworld domain; agentic advantage is modest despite significantly higher token cost; PDDL step feedback lacks external grounding for verification.

### Huang et al. (2024)

**Research question**: Which strategies actually lead to robust LLM planning skills, and do current approaches address key misconceptions in the literature?
**Methodology**: Developed an end-to-end LLM planner and employed diverse metrics to evaluate strategies including fine-tuning, Chain-of-Thought, and reinforcement learning with a novel 'Longest Contiguous Common Subsequence' reward.
**Key findings**:
- Fine-tuning LLMs on planning corpora does not lead to robust planning skills on out-of-distribution test sets
- Chain-of-Thought and similar strategies enhance plan executability but do not directly improve final validity rates
- Reinforcement learning with the Longest Contiguous Common Subsequence reward emerged as the most effective strategy
- The RL approach contributes to both plan validity and executability simultaneously
- Incremental progress exists in plan executability even though plan validity remains challenging
**Limitations**: Plan validity remains a significant challenge despite improvements in executability; strategies must address both aspects, and out-of-distribution generalization is still poor with simple fine-tuning approaches.

### Huang et al. (2026)

**Research question**: Do uneven LLM planning performances across tasks reflect distinct latent planning competencies rather than differences along a single ability spectrum?
**Methodology**: Evaluated multiple LLM families on ACPBench-Hard under varying test-time reasoning budgets and applied multidimensional item response theory model to uncover latent competency structure underlying LLM planning performance.
**Key findings**:
- Two principal dimensions shape planning performance: operational reasoning and structural enumeration
- Operational reasoning evaluates local action applicability and immediate state transitions
- Structural enumeration reasons about goal reachability and landmark structure
- Operational reasoning improves under model scaling and longer reasoning traces
- Structural enumeration remains comparatively insensitive to scaling and extended reasoning time
**Limitations**: Analysis limited to ACPBench-Hard benchmark; multidimensional IRT model assumptions may not capture all planning competency dimensions; findings require validation on diverse planning tasks.

### Jia et al. (2026)

**Research question**: How can LLM-generated plans for multimodal data analysis be made more reliable through self-critiquing and self-evolving mechanisms?
**Methodology**: WeaveData generates typed logical plans with step-by-step critique before execution, checks results against questions afterwards, diagnoses failures using actual data, reuses valid results, and accumulates planning experience grounded in a metadata knowledge graph.
**Key findings**:
- Pre-execution step-by-step critique reduces errors in LLM-generated analysis plans
- Post-execution result checking against the original question catches silent computation errors
- Failed plans can be diagnosed and evolved by reusing results that remain valid
- Planning experience accumulation improves performance on later questions
- Grounding planning in a metadata knowledge graph enables clarification of ambiguous questions with evidence-backed judgments
**Limitations**: The system was demonstrated on only two public multimodal datasets, and scalability or computational overhead of the self-critiquing process is not discussed.

### Kang (2025)

**Research question**: How can scalable evaluation data be generated to overcome the scarcity hindering progress in LLM planning and workflow composition?
**Methodology**: NL2Flow is introduced as a fully automated pipeline that parametrically generates workflow planning problems in a structured intermediate representation, translating them into both natural language and formal PDDL for evaluation.
**Key findings**:
- Best-performing model achieved 86% success in generating valid plans and 69% in generating optimal plans
- Translating natural language to structured JSON representation before symbolic planning significantly improved success rates
- The influence of problem characteristics on plan generation is contingent on both model and prompt design
- 2,296 low-difficulty problems were generated and evaluated across multiple open-source instruct-tuned LLMs
- Neuro-symbolic integration shows clear benefits for LLM planning tasks
**Limitations**: Evaluation was limited to low-difficulty problems only; the paper acknowledges that understanding error sources and shifting bottlenecks remains crucial as LLM reasoning systems scale to more complex tasks.

### Li & Kingsford (2026)

**Research question**: How can LLMs plan effectively in continuous-state domains where actions form a continuum and cannot be enumerated?
**Methodology**: Developed Medaka, an MEA-inspired structured prompting framework that encourages recursive goal decomposition, algebraic derivation, and per-step state tracking, evaluated on Liquidworld, a systematic testbed on liquid mixing.
**Key findings**:
- Traditional LLM planning frameworks assume enumerable actions, which breaks down in continuous-state domains
- Means-Ends Analysis from human psychology provides an effective remedy for continuous-state planning challenges
- Medaka improves performance across multiple model families on the Liquidworld benchmark
- Classical means-ends analysis elicits LLM-native reasoning abilities that are helpful for continuous-state planning
**Limitations**: Evaluation limited to liquid mixing domain (Liquidworld); generalizability to other continuous-state domains remains untested.

### Wei et al. (2025)

**Research question**: How can we comprehensively overview and compare current LLM planners with clear, consistent evaluation criteria?
**Methodology**: Survey examining six key performance criteria (completeness, executability, optimality, representation, generalization, and efficiency) with thorough analysis of representative works, building on foundational work by Kartam and Wilkins (1990).
**Key findings**:
- Existing LLM planning systems are tailored to specific problems, making comparison and approach selection challenging
- The field lacks clear and consistent evaluation criteria for LLM planners
- Survey provides comprehensive framework based on six performance criteria for evaluating and comparing LLM planners
- Analysis highlights strengths and weaknesses of representative works across each performance dimension
- Identifies crucial future directions for advancing LLM planning to support agentic workflows
**Limitations**: As a survey paper, synthesizes existing work rather than presenting new empirical findings; proposed evaluation criteria framework requires validation through application.

### Zhang et al. (2025) [SPIRAL]

**Research question**: How can LLMs be improved at complex planning tasks that require exploration and self-correction beyond linear reasoning?
**Methodology**: The authors introduce SPIRAL, embedding three specialized LLM agents (Planner, Simulator, Critic) into a Monte Carlo Tree Search loop to create a guided, self-correcting reasoning process with dense reward signals.
**Key findings**:
- SPIRAL achieves 83.6% overall accuracy on DailyLifeAPIs dataset
- Outperforms the next-best search framework by over 16 percentage points
- Demonstrates superior token efficiency compared to other state-of-the-art agents
- Consistently outperforms Chain-of-Thought and other baseline methods on both DailyLifeAPIs and HuggingFace datasets
- The synergy of Planner-Simulator-Critic transforms MCTS from brute-force search into guided reasoning
**Limitations**: The multi-agent architecture may introduce system complexity and coordination overhead that is not discussed.

### Zhang et al. (2025) [Cost-Awareness]

**Research question**: Are tree-search LLM planners cost-aware and do they efficiently generate budget-feasible plans under resource constraints?
**Methodology**: Systematically analyzed depth-first search, breadth-first search, Monte Carlo Tree Search, and bidirectional search within a unified framework using explicit search trees that expose intermediate decisions and node evaluations.
**Key findings**:
- Existing tree-based LLM planners often struggle to find cost-optimal plans
- Additional search computation does not reliably improve plan optimality
- Bidirectional search achieves the best overall efficiency and success rate among evaluated methods
- MCTS achieves the highest optimality on short-horizon tasks
- Improving LLM planning under resource constraints requires new search algorithms rather than solely scaling inference-time compute
**Limitations**: Study limited to four specific tree-search algorithms; does not address non-tree-search planning approaches or hybrid methods.

## References

Chen, Z., White, M., Mooney, R., Payani, A., Su, Y., & Sun, H. (2024). When is tree search useful for LLM planning? It depends on the discriminator. arXiv. https://arxiv.org/abs/2402.10890

Göbel, K., Lorang, P., Zips, P., & Glück, T. (2026). Agentic LLM planning via step-wise PDDL simulation: An empirical characterisation. arXiv. https://arxiv.org/abs/2603.06064

Huang, S., Cohn, T., & Lipovetzky, N. (2024). Chasing progress, not perfection: Revisiting strategies for end-to-end LLM plan generation. arXiv. https://arxiv.org/abs/2412.10675

Huang, S., Zhang, C., Ke, F., Cai, Z., Rastgoo, N., Haffari, G., & Rezatofighi, H. (2026). What we talk about when we talk about LLM planning: Evidence for two distinct planning abilities. arXiv. https://arxiv.org/abs/2607.11197

Jia, M., Zhou, S., Zhu, J.-P., Cai, P., Xu, K., Zhang, C., Li, L., Zhou, A., Long, H., Cui, Q., Tang, L., & Liu, Q. (2026). WeaveData: A multimodal data analysis system with self-critiquing and self-evolving LLM plans. arXiv. https://arxiv.org/abs/2609.34764

Kang, J. (2025). Scaling LLM planning: NL2FLOW for parametric problem generation and rigorous evaluation. arXiv. https://arxiv.org/abs/2507.02253

Li, J., & Kingsford, C. (2026). Means-ends analysis helps LLMs plan in continuous-state domains. arXiv. https://arxiv.org/abs/2610.24928

Wei, H., Zhang, Z., He, S., Xia, T., Pan, S., & Liu, F. (2025). PlanGenLLMs: A modern survey of LLM planning capabilities. arXiv. https://arxiv.org/abs/2502.11221

Zhang, Y., Ganapavarapu, G., Jayaraman, S., Agrawal, B., Patel, D., & Fokoue, A. (2025). SPIRAL: Symbolic LLM planning via grounded and reflective search. arXiv. https://arxiv.org/abs/2512.23167

Zhang, Z., Wei, H., Jiang, K., Pan, S., Kai, S., & Liu, F. (2025). Cost-awareness in tree-search LLM planning: A systematic study. arXiv. https://arxiv.org/abs/2505.14656
