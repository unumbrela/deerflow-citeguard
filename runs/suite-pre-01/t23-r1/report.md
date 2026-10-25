# Systematic Literature Review: Planning with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "LLM planning", category cs.AI, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on planning with large language models has evolved rapidly from 2024 to 2026, revealing a field in transition from proof-of-concept demonstrations to rigorous empirical evaluation. The surveyed papers collectively demonstrate that LLM planning capabilities are more nuanced than initially assumed, with distinct competencies emerging for different planning paradigms. Research has shifted toward understanding when and why planning methods succeed or fail, rather than simply reporting performance metrics. Key findings indicate that while LLMs show promise for planning tasks, significant challenges remain in cost-awareness, continuous-state domains, and out-of-distribution generalization. The field is converging on hybrid neuro-symbolic approaches and structured evaluation frameworks as promising directions for future work.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "LLM planning", filtered to category cs.AI, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Search-Based Planning Methods and Their Limitations

A substantial body of work has investigated the application of classical search algorithms to LLM planning, seeking to understand when tree search and related methods provide genuine benefits over simpler approaches. Chen et al. (2024) conducted a comprehensive analysis of advanced planning methods including iterative correction and tree search, finding that these methods require discriminators with at least 90% accuracy to achieve significant improvements over simple re-ranking. Their experiments on text-to-SQL parsing and mathematical reasoning revealed that tree search is 10-20 times slower than alternatives while yielding negligible performance gains when using LLM-based discriminators.

Zhang et al. (2025) extended this analysis to cost-awareness in tree-search LLM planning, systematically evaluating DFS, BFS, MCTS, and bidirectional search within a unified framework. Their findings indicate that existing tree-based LLM planners often struggle to find cost-optimal plans, and additional search computation does not reliably improve optimality. Among the methods evaluated, bidirectional search achieved the best overall efficiency and success rate, while MCTS achieved the highest optimality on short-horizon tasks. The authors conclude that improving LLM planning under resource constraints will likely require new search algorithms rather than solely scaling inference-time compute.

Zhang et al. (2025) also introduced SPIRAL, a framework that embeds three specialized LLM agents (Planner, Simulator, Critic) into an MCTS loop, transforming brute-force search into guided, self-correcting reasoning with dense reward signals. SPIRAL achieved 83.6% overall accuracy on DailyLifeAPIs, improving over 16 percentage points against the next-best search framework, demonstrating that the key to effective search-based planning lies not in the search algorithm itself but in the quality of guidance signals provided to the search process.

### Theme 2: Evaluation Frameworks and Benchmark Development

The rapid growth of LLM planning research has exposed a critical need for standardized evaluation frameworks and benchmarks. Wei et al. (2025) conducted a comprehensive survey examining six key performance criteria: completeness, executability, optimality, representation, generalization, and efficiency. Their analysis revealed that many LLM planning systems are tailored to specific problems, making comparison and approach selection challenging, and the field lacks clear and consistent evaluation criteria.

Kang (2025) addressed the scarcity of scalable evaluation data by introducing NL2Flow, a fully automated pipeline that parametrically generates workflow planning problems in structured intermediate representation, translating them into both natural language and formal PDDL. Evaluation of several open-source instruct-tuned LLMs on 2,296 low-difficulty problems showed that the best-performing model achieved 86% success in generating valid plans and 69% in generating optimal plans. Importantly, translating natural language problems into structured JSON representation prior to symbolic planning significantly improved success rates, suggesting benefits from neuro-symbolic integration.

Huang et al. (2026) applied multidimensional item response theory to uncover the latent competency structure underlying LLM planning on ACPBench-Hard. Their analysis revealed two principal dimensions: operational reasoning (the ability to evaluate local action applicability and immediate state transitions) and structural enumeration (the ability to reason about goal reachability and landmark structure). Operational reasoning improves under model scaling and longer reasoning traces, while structural enumeration remains comparatively insensitive. These findings motivate competency-level evaluation of LLM planning, shifting focus from overall improvement to which planning competencies improve under what conditions and why.

### Theme 3: Agentic and Interactive Planning Approaches

Recent work has explored agentic approaches where LLMs interact with environments step-by-step rather than generating complete plans upfront. Göbel et al. (2026) developed PyPDDLEngine, an open-source PDDL simulation engine with MCP interface exposing planning operations as LLM tool calls. Evaluation on 102 IPC Blocksworld instances showed that agentic LLM planning achieved 66.7% success rate compared to 63.7% for direct LLM planning and 85.3% for the classical Fast Downward baseline. While the agentic approach showed a modest 3 percentage-point advantage over direct planning, it came at 5.7× higher token cost per solution. The authors note that agentic gains depend on the nature of environmental feedback: coding agents benefit from externally grounded signals such as compiler errors and test failures, whereas PDDL step feedback is self-assessed, leaving the agent to evaluate its own progress without external verification.

Jia et al. (2026) presented WeaveData, a multimodal data analysis system with self-critiquing and self-evolving LLM plans. The system generates typed logical plans for each question and critiques them step-by-step before execution, then checks executed results against the question afterwards. When plans fail or miss the question, WeaveData diagnoses the failure with actual data, reuses results that remain valid, and accumulates planning experience for later questions. The system grounds planning in a metadata knowledge graph of all modalities, clarifies ambiguous questions with users, and backs every model judgment with evidence in an interactive notebook.

### Theme 4: Continuous vs. Discrete State Planning

Most LLM planning research has focused on discrete-state domains where actions form a finite, enumerable set. Li and Kingsford (2026) addressed the challenge of continuous-state domains where actions form a continuum and cannot be enumerated. They developed Medaka, a Means-Ends Analysis-inspired structured prompting framework that encourages recursive goal decomposition, algebraic derivation, and per-step state tracking. Evaluation on Liquidworld, a systematic testbed on liquid mixing, showed that Medaka improves performance across model families, suggesting that classical means-ends analysis elicits LLM-native reasoning abilities helpful for continuous-state planning.

### Theme 5: Cost and Efficiency Considerations

Several papers have highlighted the importance of computational efficiency and token costs in LLM planning. Zhang et al. (2025) noted that agentic LLM planning costs 5.7× more tokens per solution than direct planning for modest gains. Chen et al. (2024) found that tree search is 10-20 times slower than alternatives with negligible performance gains. Zhang et al. (2025) demonstrated that SPIRAL achieves superior token efficiency compared to baseline methods while maintaining high accuracy. Huang et al. (2024) found that reinforcement learning with a novel "Longest Contiguous Common Subsequence" reward emerged as the most effective strategy for both plan validity and executability, suggesting that careful reward design can improve efficiency without sacrificing performance.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that simple approaches often outperform or match more complex methods when evaluated rigorously. Chen et al. (2024), Zhang et al. (2025), and Göbel et al. (2026) all report that advanced planning methods provide modest or negligible improvements over simpler baselines when evaluated under realistic constraints. There is also broad agreement that current LLM planning systems struggle with out-of-distribution generalization (Huang et al., 2024; Kang, 2025) and that evaluation frameworks remain inconsistent across the field (Wei et al., 2025).

**Disagreements**: While Huang et al. (2024) found that fine-tuning LLMs on planning corpora does not produce robust planning skills, Kang (2025) showed that translating problems into structured intermediate representations prior to planning significantly improves success rates, suggesting that the form of representation matters more than fine-tuning alone. Additionally, while Chen et al. (2024) concluded that tree search provides negligible benefits, Zhang et al. (2025) demonstrated that SPIRAL's guided MCTS approach achieves substantial improvements, indicating that the effectiveness of search depends critically on the quality of guidance signals rather than the search algorithm itself.

## Gaps and Open Questions

Several consistent gaps emerge across the surveyed literature. First, evaluation remains limited to specific domains: Blocksworld (Göbel et al., 2026), liquid mixing (Li & Kingsford, 2026), DailyLifeAPIs and HuggingFace datasets (Zhang et al., 2025), and text-to-SQL/mathematical reasoning (Chen et al., 2024). Generalizability across domains remains untested, and as Huang et al. (2024) demonstrated, fine-tuned models perform poorly on out-of-distribution test sets.

Second, computational efficiency and token costs are acknowledged but rarely addressed systematically. Multiple papers note high token costs for agentic approaches (Göbel et al., 2026) and tree search methods (Chen et al., 2024), but few propose solutions beyond SPIRAL's guided search approach (Zhang et al., 2025).

Third, the distinction between plan executability and plan validity remains underexplored. Huang et al. (2024) found that various strategies enhance plan executability without directly improving validity rates, suggesting that current evaluation metrics may conflate distinct capabilities.

Fourth, continuous-state planning remains nascent, with only Li and Kingsford (2026) addressing this challenge. As LLMs are deployed in real-world settings requiring continuous control, this gap becomes increasingly critical.

Finally, the role of external verification and grounding signals remains unclear. Göbel et al. (2026) suggest that agentic gains depend on externally grounded feedback, but many planning domains lack such signals. Understanding how to provide effective feedback in self-assessed domains remains an open challenge.

## Per-Paper Annotations

### Chen et al. (2024)

**Research question**: Under what conditions do advanced planning methods like iterative correction and tree search provide practical utility for LLM agents solving multi-step problems?
**Methodology**: Comprehensive analysis of how discriminator accuracy affects overall agent performance when using iterative correction, tree search, or re-ranking on text-to-SQL parsing and mathematical reasoning tasks.
**Key findings**:
- Advanced planning methods require discriminators with at least 90% accuracy to achieve significant improvements over simple re-ranking
- Current LLMs' discrimination abilities have not met the threshold needed for advanced planning methods to show benefits
- Tree search is 10-20 times slower than alternatives but yields negligible performance gains when using LLM-based discriminators
- Advanced methods struggle to adequately balance accuracy and efficiency in practical deployments
**Limitations**: Analysis limited to text-to-SQL and mathematical reasoning tasks; does not explore alternative discriminator architectures or training approaches that might reach the 90% accuracy threshold.

### Göbel et al. (2026)

**Research question**: Can LLMs serve as viable planners alongside classical symbolic methods for task planning in autonomous robotic systems?
**Methodology**: Developed PyPDDLEngine, an open-source PDDL simulation engine with MCP interface exposing planning operations as LLM tool calls; evaluated four approaches on 102 IPC Blocksworld instances under uniform 180-second budget.
**Key findings**:
- Fast Downward achieves 85.3% success rate as classical baseline
- Direct LLM planning achieves 63.7% success rate
- Agentic LLM planning achieves 66.7% success rate, a modest 3 percentage-point advantage over direct approach
- Agentic approach costs 5.7× higher tokens per solution than direct LLM planning
- Both LLM approaches produce shorter plans than seq-sat-lama-2011 on co-solved instances despite its iterative quality improvement
- Agentic gains depend on environmental feedback nature; PDDL step feedback is self-assessed without external verification, unlike coding agents with compiler errors and test failures
**Limitations**: Evaluation limited to Blocksworld domain; agentic advantage is modest relative to significantly higher token cost; results may not generalize to domains with externally grounded feedback signals.

### Huang et al. (2024)

**Research question**: Do current strategies for boosting LLM reasoning skills actually lead to robust planning capabilities, or are reported successes misleading?
**Methodology**: Develops an end-to-end LLM planner employing diverse evaluation metrics to reassess strategies including fine-tuning on planning corpora, Chain-of-Thought, and reinforcement learning with novel reward functions.
**Key findings**:
- Fine-tuning LLMs on planning corpora does not produce robust planning skills, as shown by poor out-of-distribution performance
- Chain-of-Thought and similar strategies enhance plan executability probability but do not directly improve final validity rates
- Reinforcement learning with "Longest Contiguous Common Subsequence" reward emerged as most effective for both plan validity and executability
- Incremental progress exists in plan executability despite validity remaining a significant challenge
**Limitations**: Plan validity rates remain poor even with best strategies; out-of-distribution generalization is weak, suggesting fundamental gaps in current approaches.

### Huang et al. (2026)

**Research question**: Do uneven LLM planning performances across tasks reflect distinct latent planning competencies rather than differences along a single ability spectrum?
**Methodology**: Evaluated multiple LLM families on ACPBench-Hard under varying test-time reasoning budgets and applied multidimensional item response theory model to uncover latent competency structure underlying LLM planning.
**Key findings**:
- Two principal dimensions shape planning performance: operational reasoning and structural enumeration
- Operational reasoning is the ability to evaluate local action applicability and immediate state transitions
- Structural enumeration is the ability to reason about goal reachability and landmark structure
- Operational reasoning improves under model scaling and longer reasoning traces
- Structural enumeration remains comparatively insensitive to scaling and reasoning budget
- Findings motivate competency-level evaluation, shifting focus from overall improvement to which planning competencies improve, under what conditions, and why
**Limitations**: Study focused on ACPBench-Hard benchmark; findings may not generalize to all planning benchmarks or task domains; multidimensional IRT model assumptions may not capture all latent competencies.

### Jia et al. (2026)

**Research question**: How can LLM-generated plans for multimodal data analysis be made more reliable when they are prone to silently computing incorrect results, failing during execution, or missing the question?
**Methodology**: Presents WeaveData system featuring self-critiquing (step-by-step plan critique before execution, result validation after), self-evolving (failure diagnosis with actual data, valid result reuse, experience accumulation), and grounding in multimodal metadata knowledge graph.
**Key findings**:
- Pre-execution step-by-step critique and post-execution result checking against the question reduces silent failures
- Plan evolution through failure diagnosis with actual data enables reuse of valid intermediate results
- Grounding planning in metadata knowledge graph of all modalities improves plan grounding and evidence tracking
- Interactive notebook interface backs every model judgment with evidence and clarifies ambiguous questions with users
- System successfully demonstrated on two public multimodal datasets combining relational tables, text, and images
**Limitations**: Demonstration limited to two public datasets; interactive user clarification and notebook-based evidence tracking may face scalability challenges in high-volume or fully automated settings.

### Kang (2025)

**Research question**: How can we generate scalable evaluation data to overcome the scarcity hindering progress in LLM planning and workflow composition research?
**Methodology**: Introduces NL2Flow, a fully automated pipeline that parametrically generates workflow planning problems in structured intermediate representation, translating them into both natural language and formal PDDL for evaluation.
**Key findings**:
- Best-performing model achieved 86% success in generating valid plans and 69% in generating optimal plans on 2,296 low-difficulty problems
- Translating natural language problems into structured JSON representation prior to symbolic planning significantly improved success rates
- Problem characteristics' influence on plan generation is contingent on both model architecture and prompt design
- Neuro-symbolic integration shows measurable benefits for LLM planning at scale
**Limitations**: Evaluation restricted to low-difficulty problems and open-source instruct-tuned models; does not address how error sources shift as problems scale to higher complexity.

### Li and Kingsford (2026)

**Research question**: How can LLMs effectively plan in continuous-state domains where actions form a continuum and cannot be enumerated?
**Methodology**: Developed Medaka, an MEA-inspired structured prompting framework that encourages recursive goal decomposition, algebraic derivation, and per-step state tracking; evaluated on Liquidworld, a systematic testbed on liquid mixing.
**Key findings**:
- Traditional LLM planning frameworks assume enumerable actions, which breaks down in continuous-state domains
- Means-Ends Analysis from human psychology provides a remedy for continuous-state planning challenges
- Medaka improves performance across model families on the Liquidworld testbed
- Classical means-ends analysis elicits LLM-native reasoning abilities helpful for continuous-state planning
**Limitations**: Evaluation limited to liquid mixing domain; unclear generalizability to other continuous-state domains beyond Liquidworld.

### Wei et al. (2025)

**Research question**: How can we provide a comprehensive overview of current LLM planners with clear and consistent evaluation criteria to enable comparison across systems?
**Methodology**: Survey building on foundational work by Kartam and Wilkins (1990), examining six key performance criteria: completeness, executability, optimality, representation, generalization, and efficiency through thorough analysis of representative works.
**Key findings**:
- Many LLM planning systems are tailored to specific problems, making comparison and approach selection challenging
- The field lacks clear and consistent evaluation criteria for LLM planners
- Survey provides thorough analysis of representative works highlighting strengths and weaknesses for each of six criteria
- Identifies crucial future directions for LLM planning research
- Serves as valuable resource for both practitioners and newcomers interested in leveraging LLM planning for agentic workflows
**Limitations**: As a survey paper, synthesizes existing work rather than presenting new empirical findings; comprehensive coverage may become outdated as the rapidly evolving field produces new approaches.

### Zhang et al. (2025)

**Research question**: Are tree-search LLM planners cost-aware and can they efficiently generate budget-feasible plans under resource constraints?
**Methodology**: Systematic analysis of DFS, BFS, MCTS, and bidirectional search within a unified framework using explicit search trees to expose intermediate decisions, node evaluations, and failure modes for controlled ablations.
**Key findings**:
- Existing tree-based LLM planners often struggle to find cost-optimal plans
- Additional search computation does not reliably improve optimality
- Bidirectional search achieves the best overall efficiency and success rate among evaluated methods
- MCTS achieves the highest optimality on short-horizon tasks
- Improving LLM planning under resource constraints requires new search algorithms rather than solely scaling inference-time compute
**Limitations**: Study focused on specific search algorithms within a unified framework; findings may not generalize to all planning scenarios or newer algorithms developed after the study.

### Zhang et al. (2025)

**Research question**: How can LLMs be improved at complex planning tasks that require exploration and self-correction when their linear reasoning struggles to recover from early mistakes?
**Methodology**: Introduces SPIRAL framework that embeds three specialized LLM agents (Planner, Simulator, Critic) into a Monte Carlo Tree Search loop, transforming MCTS from brute-force search into guided, self-correcting reasoning with dense reward signals.
**Key findings**:
- SPIRAL achieves 83.6% overall accuracy on DailyLifeAPIs, improving over 16 percentage points against the next-best search framework
- Consistently outperforms Chain-of-Thought planning and other state-of-the-art agents on both DailyLifeAPIs and HuggingFace datasets
- The Planner-Simulator-Critic synergy provides dense rewards and grounded predictions that enable more robust autonomous planning
- Demonstrates superior token efficiency compared to baseline methods
**Limitations**: Evaluation limited to DailyLifeAPIs and HuggingFace datasets; generalizability to broader planning domains and real-world applications remains untested.

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
