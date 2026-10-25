# Systematic Literature Review: Tool Use in Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 5
**Scope**: arXiv search query "tool use large language models", filtered to category cs.AI, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review surveyed 5 arXiv papers on tool use in large language models published within the last 2 years. The surveyed literature reveals a field maturing beyond basic tool-calling capabilities toward sophisticated concerns around evaluation reliability, authorization safety, orchestration efficiency, and resource-constrained training. Collectively, these papers demonstrate that the research community has shifted from asking "can LLMs use tools?" to "how can we make tool-using agents reliable, safe, and efficient?" Key convergences include the recognition that automated evaluation methods require rigorous auditing, that authorization mechanisms must maintain durable state to prevent replay attacks, and that explicit orchestration policies outperform implicit prompting strategies. The field shows strong momentum toward production-ready agent systems with formal guarantees around safety and efficiency.

## Methodology

This review surveyed 5 arXiv papers retrieved on 2025-10-25 using the query "tool use large language models", filtered to category cs.AI, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were requested, but only 5 papers matched the category filter. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search returned fewer papers than requested (5 instead of 10), indicating either a nascent research area under the specific cs.AI category or the need for broader search terms.

## Themes

### Theme 1: Evaluation and Reliability of Tool-Using Agents

The reliability of automated evaluation methods for tool-using agents has emerged as a critical concern. Gurram (2026) demonstrates that common substring-heuristic judging methods agree with human annotation only at chance level (κ = 0.049), while learned judges like GPT-4o-mini achieve substantially better agreement (κ = 0.567). This finding has profound implications for how the field measures progress: many reported improvements may be artifacts of unreliable evaluation rather than genuine capability gains. The work introduces AgentProp-Bench, a diagnostic benchmark of 14,750 execution traces, revealing that parameter-level errors propagate to incorrect final answers with probability approximately 0.62 across both proprietary and open-weight models. Perhaps most concerning, some agents fabricate tool executions that remain invisible to end-to-end evaluation scores, suggesting that current evaluation practices may miss critical failure modes.

### Theme 2: Authorization and Security in Agent Actions

Two papers address the security challenges of LLM agents executing actions with user authorization. Wang et al. (2026) introduce the Authorization-Closure-Graph (ACG) framework to handle evolving user instructions, selectively invalidating only affected authorization while preserving unaffected portions. This addresses a practical problem: when users modify instructions mid-task, requiring full re-authorization creates friction, but failing to update authorization creates safety risks. Xu et al. (2026) tackle a different attack vector: semantic replay attacks where authorizations are executed multiple times despite single-use token identifiers. Their CapLease system introduces durable authorization state with transactional Issue-Prepare-Commit transitions, demonstrating that token representation alone cannot prevent replay without monotonic durable state over authorized actions. Together, these works establish that authorization for LLM agents requires fundamentally different mechanisms than traditional API authentication.

### Theme 3: Orchestration and Efficiency Optimization

The question of how to orchestrate tool-using agents efficiently receives attention from Liu et al. (2026), who propose utility-guided orchestration policies that explicitly balance answer quality against execution cost. Rather than relying on fixed workflows or free-form multi-step reasoning, their approach selects among actions (respond, retrieve, tool call, verify, stop) by estimating gain, step cost, uncertainty, and redundancy. The key finding is that explicit orchestration signals substantially affect agent behavior compared to implicit approaches, and that lightweight utility design provides a practical mechanism for controllable quality-cost trade-offs. This work represents a shift from "can the agent use tools?" to "how should the agent decide when and which tools to use?"

### Theme 4: Resource-Constrained Agent Training

Wang et al. (2026) address the computational challenges of post-training tool-using agents, introducing Cooperative Parameter-subspace Evolution Strategy (CoPES). This cooperative coevolutionary method decomposes the full parameter space into lower-dimensional subspaces searched cooperatively, recovering 92% of GRPO's validation-accuracy gain under the same GPU-hour budget while requiring less than one-eighth the GPU memory. This work demonstrates that evolution strategies can be made practical for memory-constrained settings, consistently outperforming standard ES and LoRA-based GRPO on pass@k metrics across five benchmarks. The research connects tool-use capabilities to the practical realities of training infrastructure constraints.

## Convergences and Disagreements

**Convergences**: All surveyed papers converge on the recognition that tool-using LLM agents require systems-level thinking beyond model capabilities alone. Gurram (2026), Wang et al. (2026), and Xu et al. (2026) all demonstrate that evaluation, authorization, and security require dedicated infrastructure layers rather than relying on the LLM's implicit reasoning. Liu et al. (2026) and Wang et al. (2026) both emphasize explicit, analyzable mechanisms over implicit prompting strategies. There is broad agreement that parameter-level reliability matters: errors at intermediate steps propagate with high probability to final answers.

**Disagreements**: The surveyed papers do not directly contradict each other, as they address different aspects of tool use (evaluation, authorization, orchestration, training). However, there is an implicit tension between the comprehensive evaluation approach of Gurram (2026), which audits 14,750 execution traces, and the efficiency-focused approaches of Liu et al. (2026) and Wang et al. (2026), which prioritize reducing computational overhead. The field has not yet resolved how to balance thorough evaluation with practical efficiency.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Evaluation standardization**: Gurram (2026) reveals that current evaluation methods are unreliable, but no consensus exists on what constitutes a gold-standard evaluation framework for tool-using agents.

2. **Cross-agent generalization**: Most papers evaluate on specific agent architectures; it remains unclear how findings generalize across different agent designs and tool sets.

3. **Human-agent collaboration**: None of the surveyed papers address how human users interact with tool-using agents in real-time, particularly around authorization decisions and error recovery.

4. **Tool discovery and learning**: The literature assumes fixed tool sets; there is no work on how agents might discover, learn, or adapt to new tools autonomously.

5. **Long-horizon planning**: All papers focus on relatively short execution traces; the challenges of tool use in extended multi-step tasks remain underexplored.

## Per-Paper Annotations

### Gurram (2026)

**Research question**: How reliable are automated evaluation methods for tool-using LLM agents compared to human annotation, and how do errors propagate through agent executions?

**Methodology**: The study presents AgentProp-Bench, a diagnostic benchmark of 14,750 execution traces from thirteen LLM agents across four domains, to audit automated evaluation reliability, error propagation patterns, and runtime mitigation strategies.

**Key findings**:
- Substring-heuristic judging agrees with human annotation only at chance level (κ = 0.049), while GPT-4o-mini judge achieves strongest agreement (κ = 0.567)
- Parameter-level errors propagate to wrong final answers with probability approximately 0.62, replicated across proprietary and open-weight models
- Some agents fabricate tool executions that remain invisible to end-to-end evaluation scores
- A lightweight runtime interceptor reduces hallucination by 24 percentage points at a tunable operating point net-positive on open-weight models

**Limitations**: Not stated in abstract

### Wang, Q. et al. (2026)

**Research question**: How can LLM agents selectively update prior authorization when only part of a user instruction changes without requiring unnecessary re-authorization?

**Methodology**: The authors propose an Authorization-Closure-Graph (ACG) framework that represents authorization and dependencies as an evolving, versioned state, selectively invalidating affected authority while preserving unaffected portions.

**Key findings**:
- ACG selectively invalidates authority affected by instruction revisions while preserving unaffected authorization state
- The framework computes minimal repair identifying only missing evidence or authority required for execution
- ACG consistently improves action safety rate and task success rate across three advanced LLMs in two natural tasks

**Limitations**: Not stated in abstract

### Liu et al. (2026)

**Research question**: How can agent orchestration be explicitly optimized to balance answer quality and execution cost in tool-using LLM agents?

**Methodology**: The study proposes a utility-guided orchestration policy that selects among actions (respond, retrieve, tool call, verify, stop) by balancing estimated gain, step cost, uncertainty, and redundancy through explicit decision-making rather than prompt-level behavior.

**Key findings**:
- Explicit orchestration signals substantially affect agent behavior compared to fixed workflows or free-form multi-step reasoning
- Lightweight utility design provides a defensible and practical mechanism for agent control
- The policy framework enables controllable and analyzable quality-cost trade-offs in tool-using LLM agents
- Additional analyses demonstrate effects of cost definitions, workflow fairness, and redundancy control on agent behavior

**Limitations**: Not stated in abstract

### Xu et al. (2026)

**Research question**: How can LLM agents prevent semantic replay attacks where authorizations are executed multiple times despite single-use token identifiers?

**Methodology**: The authors introduce CapLease, an authorization-consumption layer that binds authenticated user confirmation to a canonical action and enforces transactional Issue-Prepare-Commit transitions with durable state over authorized actions.

**Key findings**:
- Identifier-local token consumption cannot prevent semantic reissuance without monotonic durable state over authorized actions
- CapLease and equally stateful Server Ledger prevent duplicate admission and duplicate external effects with an idempotent sink
- Durable authorization state, rather than token representation alone, is the systems requirement for replay-resistant agent execution

**Limitations**: Not stated in abstract

### Wang, Z. et al. (2026)

**Research question**: How can evolution strategies be made more efficient for memory-constrained post-training of tool-using LLM agents?

**Methodology**: The study introduces Cooperative Parameter-subspace Evolution Strategy (CoPES), a cooperative coevolutionary method that decomposes the full parameter space into lower-dimensional subspaces and searches over them cooperatively to improve optimization efficiency.

**Key findings**:
- CoPES recovers 92% of GRPO's validation-accuracy gain under the same GPU-hour budget, versus 67% for standard ES
- CoPES theoretical GPU memory requirement is less than one-eighth that of full-parameter GRPO
- CoPES consistently outperforms standard ES and LoRA-based GRPO on all evaluated pass@k metrics across five benchmarks
- The method demonstrates improved trade-off between memory requirements and training time for agentic LLM post-training under resource constraints

**Limitations**: Not stated in abstract

## References

Gurram, B. (2026). Auditing automated evaluation, error propagation, and runtime mitigation in tool-using language agents. arXiv. https://arxiv.org/abs/2604.16706

Liu, B., Zhao, G., & Xu, H. (2026). Utility-guided agent orchestration for efficient LLM tool use. arXiv. https://arxiv.org/abs/2603.19896

Wang, Q., Wang, C., Meng, J., Qin, R., Peng, K., Wei, Z., & Shen, W. (2026). Authorization closure graph: Minimal repair for LLM agents with evolving user instructions. arXiv. https://arxiv.org/abs/2609.32428

Wang, Z., Liu, S., Wu, J., Lu, N., Ouyang, H., Zhang, S., Lv, H., & Tang, K. (2026). Cooperative coevolution for resource-constrained agentic LLM post-training. arXiv. https://arxiv.org/abs/2608.02391

Xu, J., Fan, L., Wang, Z., Li, X., & Liu, H. (2026). Beyond single-use tokens: Durable authorization state for replay-resistant LLM agent actions. arXiv. https://arxiv.org/abs/2608.01710
