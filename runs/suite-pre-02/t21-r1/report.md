# Systematic Literature Review: Multi-Agent Collaboration with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "multi-agent collaboration", category cs.AI, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature reveals a rapidly maturing field focused on making multi-agent LLM collaboration more effective, efficient, and task-appropriate. Research clusters around three main directions: (1) architectural innovations for coordination and orchestration, including dynamic graph-based structures and centralized puppeteer models; (2) empirical benchmarking that questions when multi-agent approaches actually outperform single-agent or conventional methods; and (3) specialized applications in domains like healthcare, embodied AI, and multimodal sensing. A critical insight emerging across multiple papers is that multi-agent collaboration is not universally superior—its benefits are bounded by task structure, with long-horizon tasks with sparse dependencies showing the most consistent gains, while tightly coupled workflows may favor single-agent approaches. The field is moving beyond proving that multi-agent systems work toward understanding when, why, and how they should be deployed.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "multi-agent collaboration", filtered to category cs.AI, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search query may miss papers using alternative terminology such as "multi-agent systems" or "collaborative AI" without the exact phrase "multi-agent collaboration."

## Themes

### Theme 1: Architectural Innovations for Dynamic Orchestration

A dominant thread across the literature focuses on moving beyond static multi-agent architectures toward dynamic, adaptive orchestration mechanisms. Several papers propose graph-based or hierarchical structures that evolve in response to task demands. Yuan et al. (2026) introduce SAIGE, which models collaboration as a dynamically evolving graph where agent instances are spawned on-demand and edges encode semantic dependencies established through content-based retrieval. This approach directly addresses the observation that scaling agent pools or deepening recursion does not consistently improve outcomes.

Similarly, Dang et al. (2025) propose a "puppeteer-style" paradigm where a centralized orchestrator, trained via reinforcement learning, dynamically directs agents in response to evolving task states. Their key finding is that the orchestrator's evolution leads to more compact, cyclic reasoning structures, achieving superior performance with reduced computational costs compared to static organizational structures. Qian et al. (2024) take a scaling-focused approach with MacNet, organizing agents into directed acyclic graphs and demonstrating that irregular topologies outperform regular ones, with performance following a logistic growth pattern as agents scale to over 1,000.

These three papers collectively suggest that the future of multi-agent collaboration lies not in adding more agents, but in smarter orchestration—whether through dynamic graphs, learned orchestrators, or topology-aware scaling.

### Theme 2: Empirical Benchmarking and Boundary Conditions

A second major theme involves rigorous empirical evaluation that questions the universal superiority of multi-agent approaches. Multiple papers introduce comprehensive benchmarks to test when multi-agent collaboration actually delivers value. Yuan et al. (2026) systematically delineate capability boundaries, finding that multi-agent collaboration confers benefits specifically in long-horizon tasks with sparse dependencies, while single-agent harnesses remain superior in tightly coupled, sequential workflows.

Zhu et al. (2025) present MedAgentBoard, a benchmark spanning four medical task categories, and find a nuanced landscape: multi-agent collaboration enhances task completeness in clinical workflow automation but does not consistently outperform advanced single LLMs in textual medical QA, and specialized conventional methods generally maintain better performance in medical VQA and EHR-based prediction. Park et al. (2026) introduce PAC-Bench to evaluate collaboration under privacy constraints, finding that privacy substantially degrades performance and introduces coordination breakdowns including early-stage violations and privacy-induced hallucinations.

Shu et al. (2024) benchmark enterprise applications and demonstrate 90% end-to-end goal success rates with their coordination framework, showing up to 70% improvement over single-agent approaches—but crucially, this benefit is demonstrated on handcrafted scenarios from specific enterprise domains, raising questions about generalizability.

### Theme 3: Efficiency and Grounding in Embodied and Multimodal Tasks

A third cluster addresses the challenge of making multi-agent collaboration efficient, particularly in embodied and multimodal domains where LLMs must ground their reasoning in physical or sensor data. Zhang et al. (2024) propose ReAd, a framework that introduces Reinforced Advantage feedback for efficient self-refinement of plans in embodied multi-agent collaboration. Their approach significantly decreases both agent interaction steps and LLM query rounds on Overcooked-AI and RoCoBench, addressing the inefficiency of methods that overly rely on physical verification or self-reflection.

Yoon et al. (2026) tackle multimodal sensing with ConSensus, a training-free framework that decomposes tasks into specialized, modality-aware agents and uses hybrid fusion balancing semantic aggregation with statistical consensus. They achieve 7.1% accuracy improvement over single-agent baselines while reducing fusion token cost by 12.7x compared to iterative multi-agent debate methods.

Liu et al. (2026) address a different efficiency challenge: concurrent editing of shared codebases. Their STORM framework manages agent states by mediating interactions with the shared workspace, detecting and resolving conflicting edits at write time rather than post-hoc. This explicit state management outperforms git-worktree-based isolation by +18.7 on Commit0-Lite, suggesting that workspace isolation defers conflicts to expensive merge steps.

### Theme 4: Specialization Through Personas and Domain Curation

A fourth, smaller but notable theme explores how specialization—whether through persona curation or domain-specific design—improves brainstorming and ideation outcomes. Straub et al. (2025) demonstrate that persona-based multi-agent brainstorming produces greater idea depth and cross-domain coverage compared to generalized collaboration. Their experiments across different persona pairings (e.g., Doctor vs VR Engineer) and collaboration modes show that persona choice shapes idea domains and that collaboration mode shifts diversity of idea generation.

This work connects to the broader theme of moving beyond homogeneous agent pools toward heterogeneous, specialized agents—whether defined by persona, modality expertise, or domain knowledge.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that multi-agent collaboration is not universally superior. Yuan et al. (2026), Zhu et al. (2025), and Park et al. (2026) all demonstrate that benefits are task-dependent, with multi-agent approaches excelling in specific scenarios (long-horizon tasks, workflow automation) but underperforming in others (tightly coupled workflows, medical VQA, privacy-constrained settings). There is also broad agreement that dynamic, adaptive orchestration outperforms static structures (Dang et al., 2025; Yuan et al., 2026; Qian et al., 2024).

**Disagreements**: While most papers report positive results for their proposed methods, there is tension between the scaling optimism of Qian et al. (2024), who find logistic growth up to 1,000+ agents, and the more skeptical findings of Yuan et al. (2026), who show that scaling the agent pool does not consistently improve outcomes. This may reflect differences in task domains or orchestration mechanisms, but highlights an unresolved question about optimal agent pool sizes.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature:

1. **Generalizability**: Multiple papers acknowledge that their benchmarks or frameworks are evaluated on specific domains (enterprise applications, medical tasks, code editing) with limited evidence of cross-domain transfer. Shu et al. (2024) use handcrafted scenarios; Zhu et al. (2025) focus on medical tasks; Liu et al. (2026) evaluate on code benchmarks.

2. **Privacy and Safety**: Park et al. (2026) identify privacy-aware collaboration as "a distinct and unresolved challenge," but none of the other papers address privacy, safety, or alignment concerns in multi-agent settings. This represents a significant gap given the deployment risks of autonomous multi-agent systems.

3. **Human-Agent Collaboration**: None of the surveyed papers examine how multi-agent systems collaborate with humans, focusing exclusively on agent-agent interaction. This limits applicability to real-world settings where humans remain in the loop.

4. **Long-Term Evaluation**: Most evaluations are short-term benchmarks. There is no literature on long-term multi-agent collaboration, learning over time, or adaptation to changing environments.

5. **Cost-Benefit Analysis**: While several papers mention computational costs (Dang et al., 2025; Yoon et al., 2026), none provide comprehensive cost-benefit analyses comparing multi-agent overhead to performance gains across diverse task types.

## Per-Paper Annotations

### Dang et al. (2025)

**Research question**: How can multi-agent LLM collaboration overcome the limitations of static organizational structures that struggle to adapt as task complexity and agent numbers grow?

**Methodology**: The authors propose a puppeteer-style paradigm where a centralized orchestrator dynamically directs agents in response to evolving task states, trained via reinforcement learning to adaptively sequence and prioritize agents.

**Key findings**:
- The puppeteer approach achieves superior performance with reduced computational costs compared to static organizational structures
- Key improvements stem from the emergence of more compact, cyclic reasoning structures under the orchestrator's evolution
- The method demonstrates effectiveness in both closed- and open-domain scenarios

**Limitations**: The centralized orchestrator architecture may introduce a single point of failure, and the approach's effectiveness depends on the quality of reinforcement learning training.

### Liu et al. (2026)

**Research question**: How can we address conflicts and inconsistent views when multiple agents edit a shared codebase concurrently?

**Methodology**: The authors propose STORM (STate-ORiented Management), which manages agent states by mediating interactions with the shared workspace, ensuring consistent views and detecting/resolving conflicting edits at write time.

**Key findings**:
- STORM outperforms git-worktree-based multi-agent baseline by +18.7 on Commit0-Lite and +1.4 on PaperBench
- STORM achieves comparable or better cost efficiency than workspace isolation approaches
- Explicit state management is a more effective foundation for multi-agent collaboration than workspace isolation

**Limitations**: Evaluation focuses on code-related benchmarks; effectiveness may vary for other types of collaborative tasks beyond code editing.

### Park et al. (2026)

**Research question**: How do privacy constraints affect the dynamics and performance of multi-agent collaboration?

**Methodology**: The authors present PAC-Bench, a benchmark for systematic evaluation of multi-agent collaboration under privacy constraints, analyzing coordination breakdowns and performance degradation patterns.

**Key findings**:
- Privacy constraints substantially degrade collaboration performance
- Outcomes depend more on the initiating agent than the partner under privacy constraints
- Coordination breakdowns include early-stage privacy violations, overly conservative abstraction, and privacy-induced hallucinations

**Limitations**: The benchmark may not cover all privacy scenarios and constraint types; findings are specific to the evaluated coordination mechanisms.

### Qian et al. (2024)

**Research question**: Can continuous addition of collaborative agents yield performance benefits similar to neural scaling laws in LLM-based multi-agent systems?

**Methodology**: The authors utilize directed acyclic graphs to organize agents into a multi-agent collaboration network (MacNet), evaluating scaling effects across configurations with up to over a thousand agents.

**Key findings**:
- MacNet effectively supports collaboration among over a thousand agents
- Irregular topologies outperform regular ones in multi-agent collaboration networks
- Performance follows a logistic growth pattern as agents scale, with collaborative emergence occurring earlier than traditional neural emergence

**Limitations**: The logistic growth pattern suggests diminishing returns at very large scales, and coordination overhead may become a concern as agent numbers continue to increase.

### Shu et al. (2024)

**Research question**: How can we design and evaluate multi-agent collaboration frameworks that effectively address complex, multi-faceted problems in enterprise applications?

**Methodology**: The authors present a comprehensive evaluation framework with two operational modes: coordination mode for parallel communication with payload referencing, and routing mode for efficient message forwarding, benchmarked on handcrafted scenarios from three enterprise domains.

**Key findings**:
- Multi-agent collaboration enhances goal success rates by up to 70% compared to single-agent approaches
- Payload referencing improves performance on code-intensive tasks by 23%
- End-to-end goal success rates of 90% achieved with inter-agent communication and payload referencing mechanisms

**Limitations**: Evaluation relies on handcrafted scenarios that may not represent all enterprise use cases; the framework may not generalize to other contexts.

### Straub et al. (2025)

**Research question**: How does persona-based agent selection and domain curation improve brainstorming outcomes compared to generalized multi-agent collaboration?

**Methodology**: The authors develop a framework for persona-based agent selection and evaluate brainstorming outputs across different persona pairings and agent-to-agent dynamics including separate, together, and separate-then-together collaboration modes.

**Key findings**:
- Persona choice shapes idea domains, influencing the types of ideas generated
- Collaboration mode shifts the diversity of idea generation
- Multi-agent persona-driven brainstorming produces greater idea depth and cross-domain coverage

**Limitations**: The effectiveness depends on the quality of persona curation and domain selection, and generalizability beyond the tested experimental setups remains to be demonstrated.

### Yoon et al. (2026)

**Research question**: How can heterogeneous multimodal sensor data be accurately interpreted when single monolithic LLMs fail to reason coherently across modalities?

**Methodology**: The authors introduce ConSensus, a training-free multi-agent collaboration framework that decomposes multimodal sensing tasks into specialized, modality-aware agents with hybrid fusion balancing semantic aggregation and statistical consensus.

**Key findings**:
- ConSensus demonstrates 7.1% average accuracy improvement over single-agent baselines across five multimodal sensing benchmarks
- The framework matches or exceeds iterative multi-agent debate performance with 12.7x reduction in fusion token cost
- The combination of semantic aggregation and statistical consensus enables reliable inference under sensor noise and missing data

**Limitations**: The training-free approach may not optimize for specific domains, and the hybrid fusion mechanism may require careful tuning for different sensor modalities.

### Yuan et al. (2026)

**Research question**: When does multi-agent collaboration offer genuine value compared to increasingly capable single-agent alternatives?

**Methodology**: Through systematic analysis of capability boundaries, the authors propose SAIGE (Semantic-Aware Incremental Graph Evolution), modeling collaboration as a dynamically evolving graph with agent instances spawned on demand.

**Key findings**:
- Multi-agent collaboration confers systematic benefits specifically in long-horizon tasks with sparse dependencies
- Single-agent harnesses remain superior in tightly coupled, sequential workflows
- Scaling the agent pool or deepening recursion level does not consistently improve outcomes

**Limitations**: The analysis focuses on specific task types and may not capture all collaboration scenarios; SAIGE's effectiveness may vary across different domains.

### Zhang et al. (2024)

**Research question**: How can LLM planning for embodied multi-agent collaboration be made more efficient without excessive querying of LLMs for physical verification or self-reflection?

**Methodology**: The authors propose ReAd, a framework that introduces Reinforced Advantage feedback for efficient self-refinement of plans, using critic regression to learn a sequential advantage function from LLM-planned data.

**Key findings**:
- ReAd surpasses baselines in success rate on Overcooked-AI and RoCoBench
- The framework significantly decreases both agent interaction steps and LLM query rounds
- ReAd endows the LLM with foresight to discern whether actions contribute to accomplishing subtasks

**Limitations**: The approach depends on the quality of LLM-planned data for training the critic, and generalizability beyond the tested benchmarks remains to be demonstrated.

### Zhu et al. (2025)

**Research question**: What are the practical advantages of multi-agent collaboration approaches compared to single-LLM and conventional methods across diverse medical tasks?

**Methodology**: The authors introduce MedAgentBoard, a comprehensive benchmark encompassing four medical task categories with rigorous comparisons across multi-agent, single-LLM, and conventional approaches.

**Key findings**:
- Multi-agent collaboration demonstrates benefits in clinical workflow automation but not consistently in textual medical QA
- Specialized conventional methods generally maintain better performance in medical VQA and EHR-based prediction
- Task-specific, evidence-based approach is necessary for selecting AI solutions in medicine

**Limitations**: The benchmark covers specific medical task categories that may not represent all healthcare applications; results may not generalize to all clinical contexts.

## References

Dang, Y., Qian, C., Luo, X., Fan, J., Xie, Z., Shi, R., Chen, W., Yang, C., Che, X., Tian, Y., Xiong, X., Han, L., Liu, Z., & Sun, M. (2025). Multi-agent collaboration via evolving orchestration. arXiv. https://arxiv.org/abs/2505.19591

Liu, M., Chen, T., Xu, Z., Jiang, X., & Dong, Y. (2026). Multi-agent collaboration with state management. arXiv. https://arxiv.org/abs/2605.20563

Park, M., Kim, D., Ju, H., Lim, S., Choi, D., Kwon, T., Kim, M., & Yeo, J. (2026). PAC-BENCH: Evaluating multi-agent collaboration under privacy constraints. arXiv. https://arxiv.org/abs/2604.11523

Qian, C., Xie, Z., Wang, Y., Liu, W., Zhu, K., Xia, H., Dang, Y., Du, Z., Chen, W., Yang, C., Liu, Z., & Sun, M. (2024). Scaling large language model-based multi-agent collaboration. arXiv. https://arxiv.org/abs/2406.07155

Shu, R., Das, N., Yuan, M., Sunkara, M., & Zhang, Y. (2024). Towards effective GenAI multi-agent collaboration: Design and evaluation for enterprise applications. arXiv. https://arxiv.org/abs/2412.05449

Straub, N., Khan, S., Jay, K., Cabral, B., & Linde, O. (2025). Persona-based multi-agent collaboration for brainstorming. arXiv. https://arxiv.org/abs/2512.04488

Yoon, H., Malekzadeh, M., Lee, S.-J., Kawsar, F., & Qendro, L. (2026). ConSensus: Multi-agent collaboration for multimodal sensing. arXiv. https://arxiv.org/abs/2601.06453

Yuan, Y., Wu, Y., Zhang, Y., Sun, M., Li, S., Ma, X., Li, Y., & Liu, J. (2026). Rethinking multi-agent collaboration: When more is less. arXiv. https://arxiv.org/abs/2609.19759

Zhang, Y., Yang, S., Bai, C., Wu, F., Li, X., Wang, Z., & Li, X. (2024). Towards efficient LLM grounding for embodied multi-agent collaboration. arXiv. https://arxiv.org/abs/2405.14314

Zhu, Y., He, Z., Hu, H., Zheng, X., Zhang, X., Wang, Z., Gao, J., Ma, L., & Yu, L. (2025). MedAgentBoard: Benchmarking multi-agent collaboration with conventional methods for diverse medical tasks. arXiv. https://arxiv.org/abs/2505.12371
