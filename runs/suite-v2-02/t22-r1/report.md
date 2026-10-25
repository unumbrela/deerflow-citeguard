# Systematic Literature Review: Tool Use in Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "tool use large language models", category cs.AI, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on tool use in large language models has rapidly evolved toward addressing critical challenges in agent reliability, authorization safety, orchestration efficiency, and scalable training. Recent work demonstrates a shift from simple tool invocation toward sophisticated systems that handle error propagation, replay-resistant authorization, utility-guided decision making, and hierarchical tool representation. The surveyed papers collectively reveal that successful tool-using agents require not just capable language models, but carefully designed infrastructure for evaluation, authorization management, orchestration policies, and training efficiency. Key advances include frameworks for auditing agent execution (Gurram, 2026), durable authorization systems (Xu et al., 2026; Wang et al., 2026), utility-guided orchestration (Liu et al., 2026), scalable tool encoding (Fang et al., 2026), and data-efficient training methods (Ye et al., 2026; Wang et al., 2026).

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "tool use large language models", filtered to category cs.AI, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search query may not capture all relevant work on tool use, as some papers may use alternative terminology such as "agent", "function calling", or "API integration".

## Themes

### Theme 1: Reliability and Error Propagation in Tool-Using Agents

A critical challenge in tool-using LLM agents is ensuring reliable execution and accurate evaluation. Gurram (2026) presents AgentProp-Bench, a comprehensive diagnostic benchmark of 14,750 execution traces from thirteen LLM agents across four domains, revealing that automated evaluation methods often fail to match human annotation quality. The study found that substring-heuristic judging agrees with human annotation only at chance level (kappa = 0.049), while even a single GPT-4o-mini judge achieves stronger agreement (kappa = 0.567). More concerning, parameter-level errors propagate to wrong final answers with probability approximately 0.62 across both proprietary and open-weight models, and several agents fabricate tool executions, asserting tool-derived results never obtained. This theme highlights the gap between apparent agent performance and actual reliability, emphasizing the need for robust evaluation frameworks and runtime mitigation strategies.

### Theme 2: Authorization and Security in Agent Actions

As LLM agents gain access to external tools and systems, ensuring secure and replay-resistant authorization becomes paramount. Two papers address this challenge from complementary angles. Xu et al. (2026) introduce CapLease, an authorization-consumption layer that binds authenticated user confirmation to a canonical action and enforces transactional Issue-Prepare-Commit transitions. Their work demonstrates that identifier-local token consumption cannot prevent fresh semantic reissuance unless the issuer retains monotonic durable state over the authorized action, establishing that durable authorization state—rather than token representation alone—is the systems requirement for replay-resistant agent execution. Wang et al. (2026) propose the Authorization-Closure-Graph (ACG) framework, which represents authorization and dependencies as an evolving, versioned state that selectively invalidates only affected authority when user instructions change. Together, these papers establish that secure tool use requires sophisticated state management beyond simple token-based approaches, particularly in scenarios involving replanning, retry, delegation, and crash recovery.

### Theme 3: Orchestration and Decision-Making Policies

Effective tool use requires intelligent orchestration—deciding when to invoke tools, when to respond directly, and how to balance quality against cost. Liu et al. (2026) propose a utility-guided orchestration policy that formulates agent orchestration as an explicit decision problem, selecting among actions (respond, retrieve, tool call, verify, stop) by balancing estimated gain, step cost, uncertainty, and redundancy. Their work demonstrates that explicit orchestration signals substantially affect agent behavior compared to fixed workflows and free-form methods like ReAct, providing a controllable and analyzable framework for studying quality-cost trade-offs. This theme represents a shift from heuristic-based agent behavior toward principled decision-making frameworks that enable systematic optimization of agent performance.

### Theme 4: Scalable Tool Representation and Learning

As the number of available tools grows, representing and learning tool usage patterns becomes increasingly challenging. Fang et al. (2026) introduce ToolWeaver, a generative tool learning framework that encodes tools into hierarchical sequences using a novel tokenization process combining intrinsic semantics with extrinsic co-usage patterns. Their approach makes vocabulary expansion logarithmic to the number of tools rather than linear, enabling learning collaborative patterns from dense co-occurrence of shared codes rather than sparse co-occurrence of monolithic tool IDs. Evaluation with nearly 47,000 tools shows ToolWeaver significantly outperforms state-of-the-art methods, providing a more scalable, generalizable, and semantically-aware foundation for tool-augmented agents. This theme addresses the fundamental scalability challenge in tool use, moving beyond individual tool learning toward understanding collaborative tool patterns.

### Theme 5: Efficient Training and Data Frameworks for Agentic LLMs

Training tool-using agents efficiently remains a significant challenge, particularly under resource constraints. Two papers address this from different angles. Wang et al. (2026) introduce Cooperative Parameter-subspace Evolution Strategy (CoPES), a cooperative coevolutionary method that decomposes the full parameter space into lower-dimensional subspaces and searches over them cooperatively. CoPES recovers 92% of GRPO's validation-accuracy gain under the same GPU-hour budget (versus 67% for standard ES) with less than one-eighth the GPU memory requirement. Zhang et al. (2025) present ActionStudio, a lightweight framework that unifies diverse agent trajectories using a Unified Format 2.0, achieving up to 9x higher throughput compared to existing agentic training frameworks. Ye et al. (2026) propose In-Context Reinforcement Learning (ICRL), an RL-only framework that eliminates supervised fine-tuning by leveraging few-shot prompting during rollout, gradually reducing in-context examples until the model learns zero-shot tool invocation. Together, these works demonstrate that efficient agent training requires novel algorithms, unified data formats, and data-efficient learning paradigms.

### Theme 6: Domain-Specific Applications and Evaluation Benchmarks

Tool use in LLMs extends beyond general-purpose agents to domain-specific applications requiring specialized evaluation. Kim and Wang (2025) propose a clinical decision support system for mental health diagnosis that combines LLMs with constraint logic programming to ensure both accuracy and interpretability, addressing ethical concerns about direct use of patient data in LLMs. Manakina et al. (2026) develop a multi-agent micro-benchmark inspired by the Stanford marshmallow experiment, analyzing 19,200 agent trajectories to study how social context, personas, and metacognitive policy affect multi-agent LLM system behavior over extended interactions. These papers illustrate that tool use research must account for domain-specific requirements—interpretability in healthcare, social dynamics in multi-agent systems—and develop appropriate benchmarks for evaluation.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that simple heuristic approaches are insufficient for reliable tool use. Gurram (2026), Xu et al. (2026), and Liu et al. (2026) all demonstrate that naive approaches (substring-heuristic evaluation, identifier-local tokens, fixed workflows) fail to provide the reliability, security, or efficiency required for production agent systems. There is also broad agreement that explicit, structured frameworks—whether for evaluation (AgentProp-Bench), authorization (CapLease, ACG), orchestration (utility-guided policies), or tool representation (ToolWeaver)—significantly outperform heuristic or free-form approaches. The surveyed papers collectively emphasize that tool use requires systematic infrastructure design rather than relying solely on model capabilities.

**Disagreements**: The literature shows some tension between different approaches to improving agent performance. While Wang et al. (2026) and Zhang et al. (2025) focus on training efficiency through evolutionary strategies and unified frameworks, Ye et al. (2026) argues for eliminating supervised fine-tuning entirely in favor of in-context reinforcement learning. Additionally, Manakina et al. (2026) find that mandatory metacognitive tool use (must-use self-questioning policy) actually increases risk compared to optional tool use, suggesting that more tool invocation is not always better—a finding that contrasts with the general assumption in other papers that enhanced tool capabilities improve agent performance.

## Gaps and Open Questions

Several gaps emerge from the collective limitations identified in the surveyed papers:

1. **Evaluation scope**: Most papers acknowledge limited evaluation domains—Gurram (2026) covers thirteen agents across four domains, Wang et al. (2026) evaluates on three LLMs in two tasks, and Wang et al. (2026) focuses on math and question-answering tasks. Broader cross-domain evaluation is needed to establish generalizability.

2. **Authorization generality**: Xu et al. (2026) and Wang et al. (2026) focus on specific authorization scenarios but do not address how their frameworks scale to complex multi-party authorization or cross-system coordination.

3. **Orchestration optimality**: Liu et al. (2026) explicitly state their goal is not to claim universally best task performance but to provide a controllable framework, leaving open the question of optimal orchestration policies for specific domains.

4. **Training-transfer gap**: Wang et al. (2026), Zhang et al. (2025), and Ye et al. (2026) all demonstrate training improvements but do not extensively evaluate transfer to unseen tool sets or domains.

5. **Ethical and safety considerations**: While Kim and Wang (2025) address ethical concerns in mental health applications, most papers do not systematically address safety, bias, or ethical implications of deploying tool-using agents in sensitive domains.

6. **Human-agent collaboration**: None of the surveyed papers extensively address how tool-using agents should collaborate with human users, particularly in scenarios where human oversight or intervention is required.

## Per-Paper Annotations

### Fang et al. (2026)

**Research question**: How can we address the scalability and semantic limitations of existing retrieval-based and generative tool-use pipelines for large language models?
**Methodology**: The authors propose ToolWeaver, a generative tool learning framework that encodes tools into hierarchical sequences using a novel tokenization process that combines intrinsic semantics with extrinsic co-usage patterns, integrated into LLMs through generative alignment with fine-tuning.
**Key findings**:
- ToolWeaver makes vocabulary expansion logarithmic to the number of tools rather than linear
- Hierarchical encoding enables learning collaborative patterns from dense co-occurrence of shared codes rather than sparse co-occurrence of monolithic tool IDs
- Evaluation with nearly 47,000 tools shows ToolWeaver significantly outperforms state-of-the-art methods
- The approach provides a more scalable, generalizable, and semantically-aware foundation for tool-augmented agents
**Limitations**: The abstract does not explicitly state limitations of the ToolWeaver framework.

### Gurram (2026)

**Research question**: How reliable are automated evaluation methods for tool-using LLM agents compared to human annotation, and how do errors propagate through agent execution?
**Methodology**: The paper presents AgentProp-Bench, a diagnostic benchmark of 14,750 execution traces from thirteen LLM agents across four domains, using it to audit automated evaluation reliability, error propagation, and runtime mitigation through human annotation comparison and statistical analysis.
**Key findings**:
- Substring-heuristic judging agrees with human annotation only at chance level (kappa = 0.049), while a single GPT-4o-mini judge achieves stronger agreement (kappa = 0.567)
- Under validated judging, parameter-level errors propagate to wrong final answers with probability approximately 0.62 across both proprietary and open-weight models
- Several agents fabricate tool executions, asserting tool-derived results never obtained, with a lightweight runtime interceptor reducing hallucination by up to 24 percentage points
- A model's ability to reject corrupted inputs and recover from them are statistically independent capabilities
**Limitations**: The abstract does not explicitly state limitations of the study; the benchmark covers thirteen LLM agents across four domains but scope constraints are not detailed.

### Kim and Wang (2025)

**Research question**: How can we develop a clinical decision support system for mental health diagnosis that combines large language models with constraint logic programming to ensure both accuracy and interpretability?
**Methodology**: The authors propose a CDSS that uses an LLM to translate diagnostic manuals into logic programs, which are then solved using a constraint logic programming engine, comparing their hybrid approach against LLM-only diagnosis and LLM-generated logic programs without expert inspection.
**Key findings**:
- LLMs are extremely useful in generating candidate logic programs for mental health diagnosis
- Expert inspection and modification of LLM-generated logic programs are required to guarantee faithfulness to official diagnostic manuals
- Direct use of patient data in LLMs raises ethical concerns, underscoring the need for a safer hybrid approach
- The proposed hybrid CDSS ensures diagnoses are both accurate and interpretable
**Limitations**: The abstract does not explicitly state limitations of the proposed approach.

### Liu, Zhao, and Xu (2026)

**Research question**: How can agent orchestration be formulated as an explicit decision problem to balance answer quality and execution cost in tool-using LLM agents?
**Methodology**: The paper proposes a utility-guided orchestration policy that selects among actions (respond, retrieve, tool call, verify, stop) by balancing estimated gain, step cost, uncertainty, and redundancy, treating orchestration as a controllable decision problem rather than prompt-level behavior.
**Key findings**:
- Explicit orchestration signals substantially affect agent behavior compared to fixed workflows and free-form methods like ReAct
- Lightweight utility design provides a defensible and practical mechanism for agent control in quality-cost trade-offs
- The policy framework enables controllable and analyzable decisions balancing gain, cost, uncertainty, and redundancy
- Analyses on cost definitions, workflow fairness, and redundancy control demonstrate practical applicability of the approach
**Limitations**: The paper explicitly states its goal is not to claim universally best task performance but to provide a controllable framework for studying quality-cost trade-offs.

### Manakina, Bogdanov, and Lung (2026)

**Research question**: How do social context, personas, and metacognitive policy affect the behavior and survival of multi-agent LLM systems over extended interactions?
**Methodology**: The authors develop a multi-agent micro-benchmark inspired by the Stanford marshmallow experiment, where ReAct agents operate with a 'raise a question' tool under per-step budgets while manipulating social context (broadcast vs. isolated), personas (age, hedonic drive), and metacognitive policy (mandatory vs. optional tool use), analyzing 19,200 agent trajectories using Kaplan-Meier survival curves and discrete-time hazard models.
**Key findings**:
- Behavior shows a sharp early 'eat' impulse, with only 75.9% of agents persisting to the end
- Isolation reduces per-minute risk relative to broadcast conditions
- A must-use self-questioning policy increases risk compared to optional tool use
- Removing hedonic drive and/or persona age increases survival and completion rates, with combined ablation approaching 100% completion
- The delay-of-gratification paradigm effectively captures social contagion and tool-use dynamics in LLM agents
**Limitations**: The abstract does not explicitly state limitations, though the benchmark is characterized as a 'micro-benchmark' which may limit generalizability.

### Wang et al. (2026) [Authorization Closure Graph]

**Research question**: How can tool-using LLM agents selectively update prior authorization when only part of a user instruction changes, without invalidating unaffected portions of the authorization state?
**Methodology**: The paper proposes an Authorization-Closure-Graph (ACG) framework that represents authorization and dependencies as an evolving, versioned state, selectively invalidating only affected authority while computing minimal repairs for missing evidence or authority required for execution.
**Key findings**:
- ACG enables agents to adapt to revised instructions while avoiding stale authority and unnecessary authorization requests
- The framework consistently improves action safety rate and task success rate across three advanced LLMs in two natural tasks
- ACG computes minimal repairs that identify only the missing evidence or authority required for execution after instruction revisions
**Limitations**: The abstract does not specify limitations; evaluation was conducted across three LLMs in two tasks but broader applicability constraints are not stated.

### Wang et al. (2026) [Cooperative Coevolution]

**Research question**: How can evolution strategies be optimized for resource-constrained post-training of tool-using LLM agents to reduce GPU-hour requirements while maintaining performance?
**Methodology**: The paper introduces Cooperative Parameter-subspace Evolution Strategy (CoPES), a cooperative coevolutionary method that decomposes the full parameter space into lower-dimensional subspaces and searches over them cooperatively, evaluated on a Qwen3.5-4B tool-using agent for math tasks across five benchmarks.
**Key findings**:
- CoPES recovers 92% of GRPO's validation-accuracy gain under the same GPU-hour budget, versus 67% for standard ES
- CoPES theoretical GPU memory requirement is less than one-eighth that of full-parameter GRPO
- CoPES consistently outperforms standard ES and LoRA-based GRPO on all evaluated pass@k metrics across five benchmarks
- The approach demonstrates improved trade-off between memory requirements and training time for agentic LLM post-training under resource constraints
- Additional experiments show CoPES advantage on question-answering tasks beyond math
**Limitations**: The abstract does not explicitly state limitations; evaluation focuses on math and question-answering tasks with a Qwen3.5-4B model.

### Xu et al. (2026)

**Research question**: How can LLM agents prevent semantic replay attacks where one user authorization is executed multiple times under freshly issued token identifiers during replanning, retry, or recovery scenarios?
**Methodology**: The paper introduces CapLease, an authorization-consumption layer that binds authenticated user confirmation to a canonical action and enforces transactional Issue-Prepare-Commit transitions, comparing it against identifier-local token approaches across multiple agent scenarios.
**Key findings**:
- Identifier-local token consumption cannot prevent fresh semantic reissuance unless the issuer retains monotonic durable state over the authorized action
- CapLease and an equally stateful Server Ledger prevent duplicate admission and, with an idempotent sink, duplicate external effects
- Durable authorization state, rather than token representation alone, is the systems requirement for replay-resistant agent execution
- The approach addresses replanning, retry, delegation, concurrency, confirmation-replay, and crash-recovery scenarios
**Limitations**: The abstract does not explicitly state limitations; the focus is on demonstrating the necessity of durable authorization state across various agent scenarios.

### Ye et al. (2026)

**Research question**: How can we enable LLMs to effectively use external tools without requiring expensive supervised fine-tuning data?
**Methodology**: The authors propose In-Context Reinforcement Learning (ICRL), an RL-only framework that eliminates supervised fine-tuning by leveraging few-shot prompting during the rollout stage, gradually reducing in-context examples during training until the model learns to call tools independently in a zero-shot setting.
**Key findings**:
- ICRL achieves state-of-the-art performance across reasoning and tool-use benchmarks
- The framework eliminates the need for expensive supervised fine-tuning data
- Gradual reduction of in-context examples enables transition from few-shot to zero-shot tool invocation
- ICRL demonstrates effectiveness as a scalable, data-efficient alternative to traditional SFT-based pipelines
**Limitations**: The abstract does not explicitly state limitations of the ICRL framework.

### Zhang et al. (2025)

**Research question**: How can we create a lightweight and extensible framework for training large action models that addresses the challenges of diverse agent environments and noisy agentic data?
**Methodology**: The authors introduce ActionStudio, a framework that unifies diverse agent trajectories using a Unified Format 2.0, supports multi-node distributed training workflows, and integrates preprocessing and real-time verification tools, demonstrating performance through throughput comparisons and benchmark evaluations.
**Key findings**:
- ActionStudio achieves up to 9x higher throughput compared to existing agentic training frameworks
- The Unified Format 2.0 successfully unifies diverse agent trajectories for standardized processing
- Trained models using ActionStudio yield top performances across public and realistic agent benchmarks
- The framework supports scalable, agent-specific fine-tuning with optimized multi-node distributed setup
**Limitations**: The abstract does not explicitly state limitations of the ActionStudio framework.

## References

Fang, B., Ye, W., Su, Y., Zhang, J., Liu, Q., Liu, Y., Sun, X., Wu, S., Yang, J., Wei, B., & Wang, L. (2026). ToolWeaver: Weaving collaborative semantics for scalable tool use in large language models. arXiv. https://arxiv.org/abs/2601.21947

Gurram, B. (2026). Auditing automated evaluation, error propagation, and runtime mitigation in tool-using language agents. arXiv. https://arxiv.org/abs/2604.16706

Kim, B. H., & Wang, C. (2025). Large language models for interpretable mental health diagnosis. arXiv. https://arxiv.org/abs/2501.07653

Liu, B., Zhao, G., & Xu, H. (2026). Utility-guided agent orchestration for efficient LLM tool use. arXiv. https://arxiv.org/abs/2603.19896

Manakina, O., Bogdanov, I., & Lung, C.-H. (2026). Delay-of-gratification as a multi-agent survival micro-benchmark for long-horizon LLMs: Social exposure, personas, and tool use budgets. arXiv. https://arxiv.org/abs/2609.29509

Wang, Q., Wang, C., Meng, J., Qin, R., Peng, K., Wei, Z., & Shen, W. (2026). Authorization closure graph: Minimal repair for LLM agents with evolving user instructions. arXiv. https://arxiv.org/abs/2609.32428

Wang, Z., Liu, S., Wu, J., Lu, N., Ouyang, H., Zhang, S., Lv, H., & Tang, K. (2026). Cooperative coevolution for resource-constrained agentic LLM post-training. arXiv. https://arxiv.org/abs/2608.02391

Xu, J., Fan, L., Wang, Z., Li, X., & Liu, H. (2026). Beyond single-use tokens: Durable authorization state for replay-resistant LLM agent actions. arXiv. https://arxiv.org/abs/2608.01710

Ye, Y., Zhao, Y., Duan, K., Zheng, Z., Kawaguchi, K., Xie, C., & Shieh, M. Q. (2026). In-context reinforcement learning for tool use in large language models. arXiv. https://arxiv.org/abs/2603.08068

Zhang, J., Hoang, T., Zhu, M., Liu, Z., Wang, S., Awalgaonkar, T., Prabhakar, A., Chen, H., Yao, W., Liu, Z., Tan, J., Niebles, J. C., Heinecke, S., Wang, H., Savarese, S., & Xiong, C. (2025). ActionStudio: A lightweight framework for data and training of large action models. arXiv. https://arxiv.org/abs/2503.22673
