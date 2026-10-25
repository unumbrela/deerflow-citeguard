# Systematic Literature Review: Multi-Agent Collaboration with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "multi-agent collaboration" in cs.AI, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of multi-agent collaboration with large language models has evolved rapidly over the past two years, with research increasingly focused on understanding when and how collaboration provides genuine value. The surveyed literature reveals a maturing field that has moved beyond demonstrating that multi-agent systems can work together, toward critically examining the conditions under which collaboration outperforms single-agent approaches. Key findings suggest that multi-agent collaboration excels in specialized domains requiring heterogeneous expertise (medical decision-making, multimodal sensing) and tasks benefiting from diverse perspectives (brainstorming), but does not universally outperform advanced single LLMs. Privacy constraints, safety concerns, and coordination overhead emerge as significant challenges that can substantially degrade collaboration performance. The literature collectively points to a nuanced understanding: more agents do not necessarily make a system more intelligent, and the benefits of collaboration are bounded by task structure rather than being universal.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "multi-agent collaboration", filtered to category cs.AI, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: When Does Collaboration Add Value?

A central question across the surveyed literature is identifying the specific conditions under which multi-agent collaboration provides systematic benefits over single-agent alternatives. Yuan et al. (2026) directly challenge the assumption that scaling agent pools or deepening recursion levels consistently improves outcomes, demonstrating that multi-agent superiority is bounded by task structure. Their work shows that collaboration confers benefits specifically in long-horizon tasks with sparse dependencies, while single-agent harnesses remain superior in tightly coupled, sequential workflows. This finding is echoed by Zhu et al. (2025), who found that multi-agent collaboration does not consistently outperform advanced single LLMs in textual medical QA, though it demonstrates benefits in specific scenarios such as enhancing task completeness in clinical workflow automation.

The literature converges on a critical insight: collaboration overhead must be carefully weighed against tangible performance gains. Chen et al. (2025) note that specialized conventional methods generally maintain better performance in medical VQA and EHR-based prediction tasks compared to multi-agent approaches, suggesting that the inherent complexity of multi-agent systems is not always justified.

### Theme 2: Specialized Domain Applications

Multiple papers demonstrate how multi-agent collaboration excels when applied to specialized domains requiring heterogeneous expertise or multimodal reasoning. Yoon et al. (2026) introduce ConSensus, a framework that decomposes multimodal sensing tasks into specialized modality-aware agents, achieving 7.1% accuracy improvement over single-agent baselines. Their approach demonstrates that single monolithic LLMs often fail to reason coherently across modalities, leading to incomplete interpretations and prior-knowledge bias.

In the medical domain, Chen et al. (2025) propose MedOrch, a mediator-guided framework enabling multiple VLM-based expert agents to exchange and reflect on outputs, surpassing the capabilities of any individual agent without requiring model training. Zhou et al. (2026) extend this to antimicrobial peptide design with MAC-AMP, a closed-loop system that balances multiple objectives while remaining interpretable rather than operating as a black box. These works collectively demonstrate that multi-agent collaboration provides particular value in domains where heterogeneous expertise must be integrated.

### Theme 3: Privacy and Safety Constraints

A significant thread of research addresses the challenges of maintaining privacy and safety in multi-agent collaborations. Park et al. (2026) present PAC-Bench, revealing that privacy constraints substantially degrade collaboration performance and make outcomes depend more on the initiating agent than the partner. Their work identifies privacy-induced hallucinations and overly conservative abstraction as recurring coordination breakdown patterns.

Zhou et al. (2025) address safety concerns such as hallucination amplification and error propagation with GUARDIAN, which models multi-agent collaboration as a discrete-time temporal attributed graph. Their unsupervised encoder-decoder architecture achieves state-of-the-art accuracy in detecting and mitigating safety vulnerabilities, effectively capturing propagation dynamics of hallucinations and errors. These works highlight that as multi-agent systems scale, safeguarding against error propagation and privacy violations becomes increasingly critical.

### Theme 4: Coordination Mechanisms and Communication

Several papers focus on improving coordination mechanisms to enhance collaboration effectiveness. Straub et al. (2025) explore persona-based agent selection for brainstorming, finding that persona choice shapes idea domains and that collaboration mode shifts diversity of idea generation. Their work demonstrates that multi-agent persona-driven brainstorming produces idea depth and cross-domain coverage.

Garrido-Lestache Belinchon and Kedziora (2025) introduce Team-Attention-Actor-Critic (TAAC), incorporating multi-headed attention mechanisms to facilitate dynamic inter-agent communication and explicit querying among teammates. Their attention-based design exhibits superior performance compared to benchmark algorithms, demonstrating enhanced collaborative behaviors across multiple metrics. Xu et al. (2025) propose AnchorRAG, using a multi-agent framework with independent retriever agents for parallel multi-hop explorations and a supervisor agent to formulate retrieval strategies, significantly outperforming existing baselines on knowledge graph reasoning tasks.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key findings. Most papers agree that multi-agent collaboration does not universally outperform single-agent approaches, with benefits being task-dependent (Yuan et al., 2026; Zhu et al., 2025; Chen et al., 2025). There is consensus that specialized domains requiring heterogeneous expertise or multimodal reasoning particularly benefit from collaboration (Yoon et al., 2026; Chen et al., 2025; Zhou et al., 2026). Additionally, multiple papers identify coordination overhead and communication challenges as significant factors affecting collaboration performance (Park et al., 2026; Straub et al., 2025).

**Disagreements**: The literature shows some tension regarding the relative value of multi-agent approaches in medical domains. While Chen et al. (2025) find that specialized conventional methods generally maintain better performance in medical VQA and EHR-based prediction, Chen et al. (2025) demonstrate that mediator-guided multi-agent collaboration can surpass individual agent capabilities in medical decision-making. This suggests that the specific implementation and coordination mechanism may be more important than the mere presence of multiple agents.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting a need for more transparent discussion of methodological constraints and failure modes. Second, while multiple papers identify that collaboration benefits are task-dependent, there is limited prescriptive guidance on how to determine a priori whether a given task will benefit from multi-agent collaboration. Third, the literature focuses heavily on performance metrics without充分 exploration of the computational and resource costs of multi-agent systems compared to single-agent alternatives. Finally, while privacy and safety concerns are identified as significant challenges, the proposed solutions (PAC-Bench, GUARDIAN) are primarily detection-focused rather than prevention-focused, indicating a need for work on designing inherently privacy-preserving and safe multi-agent architectures.

## Per-Paper Annotations

### Chen et al. (2025) - Mediator-Guided Multi-Agent Collaboration

**Research question**: How can multi-agent systems be designed to effectively support cooperative workflows in multimodal medical decision-making scenarios?
**Methodology**: Proposes MedOrch, a mediator-guided multi-agent collaboration framework employing an LLM-based mediator agent to enable multiple VLM-based expert agents to exchange and reflect on outputs, validated on five medical vision question answering benchmarks without model training.
**Key findings**:
- Collaboration within distinct VLM-based agents can surpass the capabilities of any individual agent
- MedOrch demonstrates superior collaboration performance without requiring model training
- The mediator-guided approach enables effective information exchange and reflection among VLM agents
- Using heterogeneous open-source VLMs reveals strength in multi-agent collaboration for medical decision-making
**Limitations**: Not stated in abstract

### Chen et al. (2025) - MedAgentBoard Benchmarking

**Research question**: What are the practical advantages of multi-agent collaboration approaches compared to single-LLM and conventional methods across diverse medical tasks?
**Methodology**: Introduces MedAgentBoard, a comprehensive benchmark encompassing four diverse medical task categories (medical VQA, lay summary generation, EHR predictive modeling, clinical workflow automation) across text, medical images, and structured EHR data.
**Key findings**:
- Multi-agent collaboration demonstrates benefits in specific scenarios such as enhancing task completeness in clinical workflow automation
- Multi-agent collaboration does not consistently outperform advanced single LLMs in textual medical QA
- Specialized conventional methods generally maintain better performance in medical VQA and EHR-based prediction tasks
- Existing evaluations often lack generalizability and fail to cover diverse tasks reflective of real-world clinical practice
- The inherent complexity and overhead of multi-agent collaboration must be carefully weighed against tangible performance gains
**Limitations**: Not stated in abstract

### Garrido-Lestache Belinchon and Kedziora (2025)

**Research question**: How can reinforcement learning algorithms be designed to enhance multi-agent collaboration in cooperative environments with efficient management of joint-action spaces?
**Methodology**: Introduces Team-Attention-Actor-Critic (TAAC), a reinforcement learning algorithm with Centralized Training/Centralized Execution scheme incorporating multi-headed attention mechanisms in both actor and critic, evaluated in a simulated soccer environment.
**Key findings**:
- TAAC exhibits superior performance compared to benchmark algorithms including PPO and Multi-Agent Actor-Attention-Critic
- The attention-based design facilitates dynamic inter-agent communication and explicit querying among teammates
- TAAC demonstrates enhanced collaborative behaviors across multiple metrics including win rates, goal differentials, and Elo ratings
- The approach efficiently manages exponential growth of joint-action spaces while ensuring high collaboration
**Limitations**: Not stated in abstract

### Park et al. (2026)

**Research question**: What are the dynamics of multi-agent collaboration under privacy constraints and how do privacy constraints affect collaboration performance?
**Methodology**: Presents PAC-Bench, a benchmark for systematic evaluation of multi-agent collaboration under privacy constraints, with experiments analyzing how privacy constraints impact collaboration performance and coordination.
**Key findings**:
- Privacy constraints substantially degrade collaboration performance
- Privacy constraints make outcomes depend more on the initiating agent than the partner
- Degradation is driven by early-stage privacy violations
- Overly conservative abstraction contributes to coordination breakdowns
- Privacy-induced hallucinations are a recurring coordination breakdown pattern
**Limitations**: Not stated in abstract

### Straub et al. (2025)

**Research question**: How does persona-based agent selection and curation improve brainstorming outcomes in multi-agent collaboration?
**Methodology**: Proposes a framework for persona-based agent selection, evaluating brainstorming outputs across different persona pairings and A2A dynamics using multiple experimental setups.
**Key findings**:
- Persona choice shapes idea domains
- Collaboration mode shifts diversity of idea generation
- Multi-agent persona-driven brainstorming produces idea depth and cross-domain coverage
- Persona domain curation can improve brainstorming outcomes
- Persona-based multi-agents brainstorming is important for both diverse topics and subject matter ideation
**Limitations**: Not stated in abstract

### Xu et al. (2025)

**Research question**: How can Retrieval-Augmented Generation on Knowledge Graphs be made robust in open-world settings where accurate linking between user queries and KG entities is unreliable?
**Methodology**: Proposes AnchorRAG, a multi-agent collaboration framework using a predictor agent to identify candidate anchor entities, independent retriever agents for parallel multi-hop explorations, and a supervisor agent to formulate retrieval strategies and synthesize knowledge paths.
**Key findings**:
- AnchorRAG significantly outperforms existing baselines on four public benchmarks
- The multi-agent framework improves retrieval robustness and mitigates impact of ambiguous or erroneous anchors
- The approach establishes new state-of-the-art results on real-world reasoning tasks
- Parallel multi-hop explorations from multiple candidate anchors enhance open-world RAG performance
**Limitations**: Not stated in abstract

### Yoon et al. (2026)

**Research question**: How can multi-agent collaboration improve the interpretation of heterogeneous multimodal sensor data compared to single monolithic LLMs?
**Methodology**: Introduces ConSensus, a training-free multi-agent collaboration framework that decomposes multimodal sensing tasks into specialized modality-aware agents with a hybrid fusion mechanism balancing semantic aggregation and statistical consensus.
**Key findings**:
- Single monolithic LLMs often fail to reason coherently across modalities, leading to incomplete interpretations and prior-knowledge bias
- ConSensus achieves an average accuracy improvement of 7.1% over the single-agent baseline across five diverse multimodal sensing benchmarks
- ConSensus matches or exceeds the performance of iterative multi-agent debate methods
- ConSensus achieves a 12.7 times reduction in average fusion token cost through a single-round hybrid fusion protocol
- The combination of semantic aggregation and statistical consensus enables reliable inference under sensor noise and missing data
**Limitations**: Not stated in abstract

### Yuan et al. (2026)

**Research question**: When does multi-agent collaboration offer genuine value compared to single-agent alternatives as individual agent capabilities continue to scale?
**Methodology**: Conducts systematic analysis to delineate capability boundaries of multi-agent collaboration relative to single-agent alternatives, then proposes SAIGE, a lightweight multi-agent collaboration mechanism modeling collaboration as a dynamically evolving graph with agent instances spawned on demand.
**Key findings**:
- Multi-agent collaboration confers systematic benefits specifically in long-horizon tasks with sparse dependencies
- Single-agent harnesses remain superior in tightly coupled, sequential workflows
- Scaling the agent pool or deepening the recursion level does not consistently improve outcomes
- Multi-agent superiority is bounded by task structure rather than universal
- More agents do not necessarily make a system more intelligent
**Limitations**: Not stated in abstract

### Zhou et al. (2025) - GUARDIAN

**Research question**: How can safety concerns such as hallucination amplification and error propagation be detected and mitigated in LLM multi-agent collaboration systems?
**Methodology**: GUARDIAN models multi-agent collaboration as a discrete-time temporal attributed graph using an unsupervised encoder-decoder architecture with incremental training to reconstruct node attributes and graph structures, introducing a graph abstraction mechanism based on Information Bottleneck Theory.
**Key findings**:
- GUARDIAN achieves state-of-the-art accuracy in detecting and mitigating safety vulnerabilities in multi-agent collaborations
- The temporal graph modeling approach effectively captures propagation dynamics of hallucinations and errors
- The unsupervised architecture enables identification of anomalous nodes and edges with high precision
- The method demonstrates efficient resource utilization while safeguarding LLM multi-agent collaborations
**Limitations**: Not stated in abstract

### Zhou et al. (2026) - MAC-AMP

**Research question**: How can multi-agent LLM collaboration systems be designed to balance multiple objectives in antimicrobial peptide design while remaining interpretable?
**Methodology**: Implements MAC-AMP, a closed-loop multi-agent collaboration system with an autonomous simulated peer review-adaptive reinforcement learning framework requiring only a task description and example dataset, supporting multi-objective optimization and remaining explainable.
**Key findings**:
- MAC-AMP outperforms other AMP generative models in optimizing multiple key molecular properties
- The system achieves exceptional results in antibacterial activity, AMP likeliness, toxicity compliance, and structural reliability
- The closed-loop multi-agent approach provides explainability in contrast to black-box models
- The system demonstrates cross-domain transferability for multi-objective optimization
**Limitations**: Not stated in abstract

## References

Chen, K., Liu, M., Zong, D., Ding, C., Rui, S., Jiang, Y., Zhou, M., & Wang, X. (2025). Mediator-guided multi-agent collaboration among open-source models for medical decision-making. arXiv. https://arxiv.org/abs/2508.05996

Garrido-Lestache Belinchon, H., & Kedziora, J. (2025). Enhancing multi-agent collaboration with attention-based actor-critic policies. arXiv. https://arxiv.org/abs/2507.22782

Park, M., Kim, D., Ju, H., Lim, S., Choi, D., Kwon, T., Kim, M., & Yeo, J. (2026). PAC-BENCH: Evaluating multi-agent collaboration under privacy constraints. arXiv. https://arxiv.org/abs/2604.11523

Straub, N., Khan, S., Jay, K., Cabral, B., & Linde, O. (2025). Persona-based multi-agent collaboration for brainstorming. arXiv. https://arxiv.org/abs/2512.04488

Xu, J., Li, M., Tang, Y., Wang, P., & Zhang, W. (2025). Towards open-world retrieval-augmented generation on knowledge graph: A multi-agent collaboration framework. arXiv. https://arxiv.org/abs/2509.01238

Yoon, H., Malekzadeh, M., Lee, S.-J., Kawsar, F., & Qendro, L. (2026). ConSensus: Multi-agent collaboration for multimodal sensing. arXiv. https://arxiv.org/abs/2601.06453

Yuan, Y., Wu, Y., Zhang, Y., Sun, M., Li, S., Ma, X., Li, Y., & Liu, J. (2026). Rethinking multi-agent collaboration: When more is less. arXiv. https://arxiv.org/abs/2609.19759

Zhou, G., Janarthanan, S., Chen, L., & Hu, P. (2026). MAC-AMP: A closed-loop multi-agent collaboration system for multi-objective antimicrobial peptide design. arXiv. https://arxiv.org/abs/2602.14926

Zhou, J., Wang, L., & Yang, X. (2025). GUARDIAN: Safeguarding LLM multi-agent collaborations with temporal graph modeling. arXiv. https://arxiv.org/abs/2505.19234

Zhu, Y., He, Z., Hu, H., Zheng, X., Zhang, X., Wang, Z., Gao, J., Ma, L., & Yu, L. (2025). MedAgentBoard: Benchmarking multi-agent collaboration with conventional methods for diverse medical tasks. arXiv. https://arxiv.org/abs/2505.12371
