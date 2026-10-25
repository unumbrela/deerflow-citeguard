# Systematic Literature Review: Multi-Agent Collaboration with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "multi-agent collaboration", filtered to category cs.AI, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Multi-agent collaboration with large language models has emerged as a rapidly evolving research area between 2024 and 2026, with significant focus on practical deployment frameworks, architectural innovations, and systematic evaluation methodologies. The surveyed literature reveals a field maturing from initial enthusiasm about agent scaling toward more nuanced understanding of when and how multi-agent systems provide genuine value. Key convergences include recognition that collaboration benefits are task-structure dependent rather than universal, and that efficiency optimizations are critical for real-world deployment. However, significant gaps remain in understanding privacy-aware collaboration, cross-domain generalization, and standardized evaluation protocols that account for both performance and computational costs.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "multi-agent collaboration", filtered to category cs.AI, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Enterprise and Domain-Specific Applications

A substantial portion of recent work focuses on deploying multi-agent collaboration in specific domains, particularly enterprise applications, healthcare, and embodied AI. Shu et al. (2024) demonstrated that multi-agent collaboration enhances goal success rates by up to 70% compared to single-agent approaches in enterprise scenarios, with payload referencing improving performance on code-intensive tasks by 23%. Similarly, Zhu et al. (2025) introduced MedAgentBoard, a comprehensive benchmark for medical tasks, revealing that multi-agent collaboration shows benefits in clinical workflow automation but does not consistently outperform specialized conventional methods in medical visual question answering or EHR-based prediction.

In embodied AI contexts, Zhang et al. (2024) proposed Reinforced Advantage feedback (ReRead) for efficient LLM grounding in multi-agent collaboration, showing significant reductions in agent interaction steps and LLM query rounds on Overcooked-AI and RoCoBench benchmarks. Yoon et al. (2026) extended multi-agent collaboration to multimodal sensing with ConSensus, achieving 7.1% accuracy improvement over single-agent baselines while reducing token costs by 12.7 times through a single-round hybrid fusion protocol. These domain-specific applications demonstrate that multi-agent collaboration provides tangible benefits when tasks require specialized expertise or multimodal integration, but success depends heavily on appropriate architecture selection for the target domain.

### Theme 2: Collaboration Architecture and Orchestration

The architecture of multi-agent collaboration has received substantial attention, with research exploring both static and dynamic organizational structures. Qian et al. (2024) investigated scaling laws in multi-agent collaboration, organizing over a thousand agents into directed acyclic graphs through their MacNet framework. They identified a collaborative scaling law where performance follows logistic growth as agents scale, with irregular topologies outperforming regular ones and collaborative emergence occurring earlier than traditional neural emergence.

Building on this, Dang et al. (2025) proposed a puppeteer-style paradigm where a centralized orchestrator dynamically directs agents in response to evolving task states. Their reinforcement learning-trained orchestrator achieved superior performance with reduced computational costs, with improvements stemming from the emergence of more compact, cyclic reasoning structures. Yuan et al. (2026) challenged the assumption that more agents always improve performance, proposing SAIGE (Semantic-Aware Incremental Graph Evolution) that models collaboration as a dynamically evolving graph. Their systematic analysis revealed that multi-agent collaboration confers benefits specifically in long-horizon tasks with sparse dependencies, while single-agent harnesses remain superior in tightly coupled, sequential workflows. Straub et al. (2025) explored persona-based collaboration for brainstorming, demonstrating that persona choice shapes idea domains and collaboration mode shifts diversity of idea generation, with multi-agent persona-driven brainstorming producing greater idea depth and cross-domain coverage.

### Theme 3: Efficiency and Optimization

Computational efficiency and resource optimization emerge as critical concerns across the surveyed literature. Multiple papers address the tension between collaboration benefits and computational overhead. Dang et al. (2025) showed that their evolving orchestration approach achieves superior performance with reduced computational costs compared to static collaboration structures. Yoon et al. (2026) demonstrated that ConSensus matches or exceeds iterative multi-agent debate methods while achieving a 12.7 times reduction in average fusion token cost through single-round hybrid fusion.

Zhang et al. (2024) addressed efficiency in embodied multi-agent collaboration, showing that their ReAd framework significantly decreases both agent interaction steps and LLM query rounds compared to methods relying on physical verification or self-reflection. Liu et al. (2026) introduced STORM for state management in collaborative coding, achieving comparable or better cost efficiency than git-worktree-based approaches while outperforming them by +18.7 on Commit0-Lite and +1.4 on PaperBench. These efficiency optimizations are essential for practical deployment, as multi-agent systems must demonstrate not only performance improvements but also computational feasibility for real-world applications.

### Theme 4: Evaluation and Benchmarking

The development of comprehensive benchmarks and evaluation frameworks represents a significant trend in the literature. Zhu et al. (2025) introduced MedAgentBoard encompassing four diverse medical task categories to address the lack of generalizability in existing evaluations, emphasizing the need for rigorous comparisons against both single-LLM and conventional methods. Park et al. (2026) presented PAC-Bench for evaluating multi-agent collaboration under privacy constraints, revealing that privacy constraints substantially degrade collaboration performance and make outcomes depend more on the initiating agent than the partner.

Shu et al. (2024) benchmarked their multi-agent collaboration framework on handcrafted scenarios from three enterprise domains, evaluating coordination and routing capabilities with end-to-end goal success rates of 90%. Liu et al. (2026) evaluated STORM on Commit0 and PaperBench across multiple LLMs, reaching highest scores of 87.6 and 78.2 respectively when combined with single-agent runs. These evaluation efforts reveal a field moving toward more rigorous, domain-specific benchmarking that accounts for task structure, privacy constraints, and comparison against appropriate baselines rather than assuming multi-agent approaches are universally superior.

### Theme 5: Emerging Challenges and Limitations

The literature identifies several critical challenges that remain unresolved. Privacy-aware collaboration emerges as a distinct challenge, with Park et al. (2026) identifying recurring coordination breakdowns including early-stage privacy violations, overly conservative abstraction, and privacy-induced hallucinations. State management in collaborative environments presents another challenge, addressed by Liu et al. (2026) through explicit state management rather than workspace isolation, detecting and resolving conflicts at write time.

Yuan et al. (2026) challenged the assumption of universal multi-agent superiority, showing that scaling the agent pool or deepening recursion level does not consistently improve outcomes and that multi-agent superiority is bounded by task structure. Zhu et al. (2025) emphasized that the inherent complexity and overhead of multi-agent collaboration must be carefully weighed against tangible performance gains, advocating for task-specific, evidence-based approaches to selecting AI solutions. These emerging challenges suggest the field is maturing beyond initial enthusiasm toward more nuanced understanding of when, why, and how multi-agent collaboration provides genuine value.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, multi-agent collaboration benefits are task-structure dependent rather than universal, with multiple papers identifying specific conditions under which collaboration provides advantages (Yuan et al., 2026; Zhu et al., 2025; Shu et al., 2024). Second, efficiency optimizations are critical for practical deployment, with all papers addressing computational costs demonstrating that reduced overhead is achievable without sacrificing performance (Dang et al., 2025; Yoon et al., 2026; Zhang et al., 2024; Liu et al., 2026). Third, domain-specific customization is necessary, as evidenced by specialized frameworks for enterprise applications, medical tasks, embodied AI, and multimodal sensing (Shu et al., 2024; Zhu et al., 2025; Zhang et al., 2024; Yoon et al., 2026).

**Disagreements**: The literature reveals some tension regarding scaling. Qian et al. (2024) identified collaborative scaling laws suggesting performance improvements with increasing agent counts up to over a thousand agents, while Yuan et al. (2026) found that scaling the agent pool does not consistently improve outcomes and that "more agents do not necessarily make a system more intelligent." This apparent disagreement likely reflects different task structures and collaboration architectures, with Qian et al. focusing on irregular topologies in MacNet while Yuan et al. examined scenarios where single-agent harnesses may be superior. Additionally, while most papers demonstrate multi-agent benefits in specific domains, Zhu et al. (2025) notably found that specialized conventional methods generally maintain better performance than multi-agent approaches in medical VQA and EHR-based prediction, challenging assumptions about universal LLM-based multi-agent superiority.

## Gaps and Open Questions

Several significant gaps emerge from the collective literature. First, privacy-aware multi-agent collaboration remains an unresolved challenge, with Park et al. (2026) identifying the problem but not proposing specific coordination mechanisms to address it. The literature identifies privacy-induced performance degradation but lacks concrete solutions for privacy-preserving collaboration protocols.

Second, cross-domain generalization remains insufficiently explored. Most evaluations are limited to specific benchmarks within their target domains, with Zhang et al. (2024) noting that generalization to broader embodied tasks and real-world physical environments remains unverified, and Straub et al. (2025) acknowledging that persona-based brainstorming results may not generalize to all contexts and domains.

Third, computational overhead transparency is inconsistent across papers. While several address efficiency, others do not report comprehensive cost analyses, making it difficult to assess trade-offs between performance gains and resource requirements. Yuan et al. (2026) and Zhu et al. (2025) call for more rigorous cost-benefit analysis, but standardized metrics for evaluating these trade-offs are not yet established.

Fourth, the interaction between agent capabilities and collaboration architecture is not fully understood. While Yuan et al. (2026) delineate capability boundaries relative to single-agent alternatives, the field lacks systematic understanding of how improvements in individual agent capabilities affect the value proposition of multi-agent collaboration over time.

Finally, standardized evaluation protocols are needed. Current benchmarks are domain-specific and use different metrics, making cross-paper comparisons difficult. The field would benefit from unified evaluation frameworks that account for performance, efficiency, robustness, and scalability across diverse task types.

## Per-Paper Annotations

### Dang et al. (2025)

**Research question**: How can multi-agent collaboration among LLMs overcome the limitations of static organizational structures that struggle to adapt as task complexity and agent numbers grow?

**Methodology**: The authors propose a puppeteer-style paradigm where a centralized orchestrator dynamically directs agents, trained via reinforcement learning to adaptively sequence and prioritize agents in response to evolving task states.

**Key findings**:
- The method achieves superior performance with reduced computational costs compared to static collaboration approaches
- Key improvements consistently stem from the emergence of more compact, cyclic reasoning structures under the orchestrator's evolution
- The orchestrator enables flexible and evolvable collective reasoning that adapts to task complexity
- The approach demonstrates effectiveness in both closed- and open-domain scenarios

**Limitations**: The orchestrator requires reinforcement learning training which adds overhead; scalability limits and coordination overhead at very large agent counts are not fully explored.

### Liu et al. (2026)

**Research question**: How can we handle concurrent edits and conflicting changes when multiple agents work on a shared codebase?

**Methodology**: The authors propose STORM (STate-ORiented Management), which manages agent states by mediating interactions with the shared workspace, detecting and resolving conflicts at write time rather than post-hoc merge.

**Key findings**:
- STORM outperforms git-worktree-based multi-agent baseline by +18.7 on Commit0-Lite and +1.4 on PaperBench
- Explicit state management is more effective for multi-agent collaboration than workspace isolation
- Combined with single-agent runs, STORM reaches highest scores of 87.6 on Commit0 and 78.2 on PaperBench
- STORM can be plugged into any multi-agent system seamlessly

**Limitations**: Evaluation is limited to Commit0 and PaperBench benchmarks; may not generalize to all types of collaborative coding scenarios and non-code domains.

### Park et al. (2026)

**Research question**: How do privacy constraints affect the dynamics and performance of multi-agent collaboration?

**Methodology**: The authors present PAC-Bench, a benchmark for systematic evaluation of multi-agent collaboration under privacy constraints, analyzing coordination breakdowns and performance degradation patterns.

**Key findings**:
- Privacy constraints substantially degrade collaboration performance
- Outcomes depend more on the initiating agent than the partner under privacy constraints
- Coordination breakdowns include early-stage privacy violations, overly conservative abstraction, and privacy-induced hallucinations
- Privacy-aware multi-agent collaboration requires new coordination mechanisms beyond existing agent capabilities

**Limitations**: The benchmark identifies problems but does not propose specific solutions; may not cover all privacy scenarios and regulatory frameworks.

### Qian et al. (2024)

**Research question**: Can continuous addition of collaborative agents yield performance benefits similar to neural scaling laws observed in increasing neurons?

**Methodology**: The authors utilize directed acyclic graphs to organize agents into a multi-agent collaboration network (MacNet), upon which interactive reasoning is topologically orchestrated for autonomous task solving.

**Key findings**:
- The framework effectively supports collaboration among over a thousand agents
- Irregular topologies outperform regular ones in multi-agent collaboration
- Overall performance follows a logistic growth pattern as agents scale, identifying a collaborative scaling law
- Collaborative emergence occurs earlier than traditional neural emergence
- Scaling agents catalyzes multidimensional considerations during interactive reflection and refinement, producing more comprehensive artifacts

**Limitations**: The logistic growth pattern suggests diminishing returns at very large scales; computational costs and coordination overhead of scaling to thousands of agents are not fully addressed.

### Shu et al. (2024)

**Research question**: How can we design collaboration protocols and evaluate the effectiveness of multi-agent systems for enterprise applications?

**Methodology**: The authors present a comprehensive evaluation framework with two operational modes (coordination and routing), benchmarking on handcrafted scenarios from three enterprise domains.

**Key findings**:
- Multi-agent collaboration enhances goal success rates by up to 70% compared to single-agent approaches
- Payload referencing improves performance on code-intensive tasks by 23%
- Latency can be substantially reduced with a routing mechanism that selectively bypasses agent orchestration
- End-to-end goal success rates of 90% achieved with inter-agent communication and payload referencing mechanisms

**Limitations**: Evaluation is based on handcrafted scenarios from only three enterprise domains, which may not represent the full spectrum of enterprise use cases.

### Straub et al. (2025)

**Research question**: How does persona-based agent selection and domain curation improve brainstorming outcomes in multi-agent collaboration?

**Methodology**: The authors develop a framework for persona-based agent selection and evaluate brainstorming outputs across different persona pairings and agent-to-agent dynamics (separate, together, separate-then-together) through multiple experimental setups.

**Key findings**:
- Persona choice shapes idea domains, affecting the types of ideas generated
- Collaboration mode shifts the diversity of idea generation
- Multi-agent persona-driven brainstorming produces greater idea depth and cross-domain coverage
- Different persona pairings (e.g., Doctor vs VR Engineer) yield distinct brainstorming outcomes
- A2A dynamics (separate, together, separate-then-together) significantly impact brainstorming results

**Limitations**: Results may not generalize to all brainstorming contexts and domains; persona selection criteria and optimal pairing strategies are not fully specified; evaluation scope limited to experimental setups described.

### Yoon et al. (2026)

**Research question**: How can heterogeneous multimodal sensor data be accurately interpreted when single monolithic LLMs fail to reason coherently across modalities?

**Methodology**: The authors introduce ConSensus, a training-free multi-agent collaboration framework that decomposes multimodal sensing tasks into specialized modality-aware agents, with a hybrid fusion mechanism balancing semantic aggregation for cross-modal reasoning and statistical consensus for robustness across modalities.

**Key findings**:
- ConSensus demonstrates an average accuracy improvement of 7.1% over single-agent baseline across five diverse multimodal sensing benchmarks
- The framework matches or exceeds the performance of iterative multi-agent debate methods
- Achieves a 12.7 times reduction in average fusion token cost through a single-round hybrid fusion protocol
- The combination of semantic aggregation and statistical consensus enables reliable inference under sensor noise and missing data
- Each approach has complementary failure modes, but their combination provides robustness

**Limitations**: The training-free approach may not optimize for specific domains; the fusion mechanism may encounter edge cases with highly conflicting modalities; evaluation limited to five benchmarks.

### Yuan et al. (2026)

**Research question**: When does multi-agent collaboration offer genuine value compared to single-agent alternatives as individual agent capabilities continue to scale?

**Methodology**: Through systematic analysis of capability boundaries, the authors propose SAIGE, a lightweight collaboration mechanism based on Semantic-Aware Incremental Graph Evolution that models collaboration as a dynamically evolving graph with on-demand agent instances.

**Key findings**:
- Multi-agent collaboration confers systematic benefits specifically in long-horizon tasks with sparse dependencies
- Single-agent harnesses remain superior in tightly coupled, sequential workflows
- Scaling the agent pool or deepening recursion level does not consistently improve outcomes
- Multi-agent superiority is bounded by task structure rather than being universal

**Limitations**: SAIGE is a lightweight mechanism that may not capture all collaboration complexities; findings are based on specific long-horizon task benchmarks that may not generalize to all domains.

### Zhang et al. (2024)

**Research question**: How can LLM reasoning be efficiently grounded for embodied multi-agent collaboration tasks without excessive and inefficient querying of LLMs?

**Methodology**: The authors propose a framework introducing Reinforced Advantage feedback (ReAd) for efficient self-refinement of plans, performing critic regression to learn a sequential advantage function from LLM-planned data and treating the LLM planner as an optimizer to maximize the advantage function.

**Key findings**:
- ReAd surpasses baselines in success rate on Overcooked-AI and a difficult variant of RoCoBench
- The method significantly decreases the interaction steps of agents
- Query rounds of LLMs are substantially reduced, demonstrating high efficiency
- The approach endows the LLM with foresight to discern whether actions contribute to accomplishing the final task
- Theoretical analysis extends advantage-weighted regression in reinforcement learning to multi-agent systems

**Limitations**: Evaluation is limited to specific benchmarks (Overcooked-AI and RoCoBench); generalization to broader embodied tasks and real-world physical environments remains unverified.

### Zhu et al. (2025)

**Research question**: What are the practical advantages of multi-agent collaboration approaches for diverse medical tasks compared to single-LLM and conventional methods?

**Methodology**: The authors introduce MedAgentBoard, a comprehensive benchmark covering four medical task categories (medical VQA, lay summary generation, EHR predictive modeling, clinical workflow automation) with comparisons against single-LLM and conventional methods.

**Key findings**:
- Multi-agent collaboration demonstrates benefits in specific scenarios like clinical workflow automation
- Does not consistently outperform advanced single LLMs in textual medical QA
- Specialized conventional methods generally maintain better performance in medical VQA and EHR-based prediction
- Task-specific, evidence-based approach is necessary for selecting AI solutions in medicine

**Limitations**: Benchmark coverage, while diverse, may not encompass all medical applications; results may vary across different healthcare settings and institutional contexts.

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
