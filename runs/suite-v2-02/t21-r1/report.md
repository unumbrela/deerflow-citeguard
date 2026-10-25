# Systematic Literature Review: Multi-Agent Collaboration with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "multi-agent collaboration large language models", filtered to category cs.AI, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on multi-agent collaboration with large language models has rapidly evolved over the past two years, with research focusing on architectural frameworks, collaborative training paradigms, safety mechanisms, and domain-specific applications. The surveyed papers reveal a field maturing from theoretical frameworks toward practical, production-ready systems that address real-world challenges in alignment, evaluation, and task execution. A dominant trend is the emergence of specialized agent roles within collaborative systems, where orchestration mechanisms enable dynamic task decomposition and inter-agent communication. Researchers increasingly recognize that effective collaboration requires explicit mechanisms for coordination, verification, and safety rather than relying solely on innate model capabilities.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "multi-agent collaboration large language models", filtered to category cs.AI, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Frameworks for Multi-Agent Collaboration

A prominent research direction involves designing structured frameworks that organize multiple LLM agents into collaborative systems with clearly defined roles and interaction protocols. ARCANE (Masters et al., 2025) frames alignment as a multi-agent collaboration problem, representing stakeholder preferences as natural-language rubrics that enable configurable trade-offs without retraining. Similarly, APD-Agents (Chen et al., 2025) introduces a five-agent architecture with specialized roles including an OrchestratorAgent that dynamically directs other agents based on user input. The MedOrch framework (Chen et al., 2025a) employs a mediator agent to guide collaboration among vision-language models, demonstrating that structured mediation enables heterogeneous models to exchange and reflect on outputs effectively. These frameworks share a common insight: explicit architectural design with role specialization outperforms ad-hoc multi-agent interactions.

### Theme 2: Collaborative Training and Post-Training Paradigms

Several papers investigate how multi-agent collaboration can be enhanced through specialized training methodologies. MAPoRL (Park et al., 2025) introduces a post-training paradigm where multiple LLMs generate responses independently, engage in multi-turn discussions to collaboratively improve answers, and are optimized through multi-agent reinforcement learning. Their key finding that training individual LLMs alone is insufficient to induce effective collaboration represents a significant contribution to the field. This work demonstrates that collaborative behaviors must be explicitly cultivated through co-training mechanisms that reward corrective and persuasive discussions. The approach generalizes to unseen domains beyond training data, suggesting that collaborative capabilities learned through multi-agent reinforcement learning transfer across contexts.

### Theme 3: Task Decomposition and Dynamic Scheduling

Effective multi-agent systems require mechanisms for breaking complex tasks into manageable sub-tasks and dynamically routing work among agents. Pan and Wu (2025) propose an architecture that converts natural language task descriptions into unified semantic representations using LLMs, then applies modular decomposition to break goals into hierarchical sub-tasks. Their system features dynamic scheduling and routing mechanisms that enable real-time collaboration, with constraint parsing and global consistency mechanisms ensuring coherent connections and balanced workload. The approach achieves better balance between task complexity and communication overhead compared to existing methods, addressing a critical challenge in multi-agent system design: minimizing coordination costs while maintaining task coherence.

### Theme 4: Safety and Alignment in Multi-Agent Systems

As multi-agent collaborations become more sophisticated, ensuring safety and alignment with human preferences has emerged as a critical research area. GUARDIAN (Zhou et al., 2025) addresses hallucination amplification and error propagation by modeling multi-agent collaboration as a discrete-time temporal attributed graph, using an unsupervised encoder-decoder architecture to identify anomalous nodes and edges. The system achieves state-of-the-art accuracy in detecting and mitigating safety concerns while efficiently utilizing resources. ARCANE (Masters et al., 2025) complements this work by focusing on alignment with stakeholder preferences through interpretable reward models, enabling test-time adaptive alignment for complex, long-horizon AI systems. Together, these works highlight the field's growing recognition that safety and alignment require explicit architectural mechanisms rather than emergent properties.

### Theme 5: Domain-Specific Applications and Evaluation Frameworks

The surveyed literature demonstrates multi-agent collaboration being applied to diverse domains with specialized evaluation requirements. In medical decision-making, MedOrch (Chen et al., 2025a) achieves superior collaboration performance on five medical vision question answering benchmarks using multiple open-source vision-language models. For mobile intelligent assistants, Wang et al. (2025) propose a three-tier agent architecture that achieves significant evaluation matching accuracy with human experts while identifying generation defects. In product concept evaluation, Xuan et al. (2026) introduce an interactive multi-agent system with eight virtual agents representing specialized domains that produces evaluation rankings consistent with senior industry experts. These applications reveal that domain-specific multi-agent systems benefit from heterogeneous model ensembles and specialized evaluation criteria tailored to the application context.

### Theme 6: Infrastructure and Scalability for Production Systems

Emerging work addresses the infrastructure challenges of deploying multi-agent systems at production scale. Aethon (Rao et al., 2026) introduces a reference-based replication primitive that enables near-constant-time instantiation of stateful AI agents by shifting from duplication to reference-based representation. This work addresses a critical bottleneck in production deployments where traditional agent instantiation approaches do not scale efficiently. The framework supports lightweight, composable execution identities that can be spawned and specialized at scale, with implications for multi-agent orchestration and enterprise governance. This infrastructure-focused research complements algorithmic advances by addressing practical deployment challenges that emerge when multi-agent systems move from research prototypes to production environments.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key findings. First, all frameworks emphasize that explicit coordination mechanisms are necessary for effective collaboration—innate model capabilities alone are insufficient (Park et al., 2025; Pan & Wu, 2025). Second, role specialization consistently improves system performance, whether through mediator agents (Chen et al., 2025a), orchestrator agents (Chen et al., 2025), or domain-specific agents (Xuan et al., 2026). Third, the literature agrees that interpretability and configurability are critical for production systems, with multiple papers proposing mechanisms for transparent agent behavior and adjustable trade-offs (Masters et al., 2025; Zhou et al., 2025). Finally, all application-focused papers demonstrate that multi-agent collaboration surpasses individual agent capabilities, validating the fundamental premise of the research area.

**Disagreements**: The literature shows limited direct disagreement, likely reflecting the field's emergent state. However, tensions exist between approaches emphasizing training-time interventions (Park et al., 2025) versus those focusing on architectural design without additional training (Chen et al., 2025a; Pan & Wu, 2025). MAPoRL argues that post-training is essential for collaborative behaviors, while other frameworks achieve collaboration through prompt engineering and structured interaction alone. Additionally, some papers emphasize homogeneous agent ensembles (Park et al., 2025) while others advocate heterogeneous model combinations (Chen et al., 2025a), suggesting unresolved questions about optimal agent diversity strategies.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either space constraints or a field-wide tendency toward optimistic framing that may obscure important boundary conditions. Second, while multiple papers demonstrate collaboration benefits, few provide rigorous ablation studies isolating which aspects of multi-agent architectures contribute most to performance gains. Third, the infrastructure challenges of multi-agent systems receive limited attention, with only Aethon (Rao et al., 2026) addressing scalability directly—this represents a significant gap given the computational costs of running multiple LLM agents in production. Fourth, long-term evaluation of multi-agent systems remains underexplored; most benchmarks measure immediate task success rather than sustained collaboration quality over extended interactions. Finally, the literature lacks systematic comparisons between different orchestration strategies, leaving practitioners without evidence-based guidance for selecting among competing architectural approaches.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: How can large language model-driven multi-agent systems automate mobile app page design to reduce time-intensive manual work?
**Methodology**: The authors propose APD-agents, an LLM-driven multi-agent framework with five specialized agents (OrchestratorAgent, SemanticParserAgent, PrimaryLayoutAgent, TemplateRetrievalAgent, and RecursiveComponentAgent) that collaborate to generate page layouts from user descriptions, evaluated on the RICO dataset.
**Key findings**:
- APD-agents achieve state-of-the-art performance on the RICO dataset for automated page design
- The OrchestratorAgent dynamically directs other agents to accomplish design tasks based on user input
- TemplateRetrievalAgent fetches semantically relevant few-shot examples to enhance layout generation quality
- RecursiveComponentAgent decides how to recursively generate fine-grained sub-elements for each layout element
**Limitations**: not stated in abstract

### Chen et al. (2025a)

**Research question**: How can mediator-guided multi-agent collaboration among open-source vision-language models improve medical multimodal decision-making?
**Methodology**: The authors propose MedOrch, a mediator-guided multi-agent collaboration framework that employs an LLM-based mediator agent to enable multiple VLM-based expert agents to exchange and reflect on outputs, validated on five medical vision question answering benchmarks without model training.
**Key findings**:
- Collaboration within distinct VLM-based agents can surpass the capabilities of any individual agent
- MedOrch achieves superior collaboration performance on five medical vision question answering benchmarks
- The mediator agent enables VLM-based expert agents to exchange and reflect on outputs towards collaboration
- Using multiple open-source VLMs reveals the strength of heterogeneous models over costly GPT-series models
**Limitations**: not stated in abstract

### Masters et al. (2025)

**Research question**: How can we maintain alignment of language model agents with stakeholder preferences in long-horizon tasks through interpretable and configurable reward models?
**Methodology**: The authors introduce ARCANE, a framework that frames alignment as a multi-agent collaboration problem, representing stakeholder preferences as natural-language rubrics (weighted sets of verifiable criteria) generated on-the-fly, evaluated on 219 labeled rubrics from the GDPVal benchmark.
**Key findings**:
- Learned rubrics produce compact, legible evaluations of agent behavior
- The framework enables configurable trade-offs (e.g., correctness vs. conciseness) without retraining
- Rubric-based reward models offer a path toward interpretable, test-time adaptive alignment for complex, long-horizon AI systems
- The approach balances interpretability, faithfulness, and computational efficiency
**Limitations**: not stated in abstract

### Pan and Wu (2025)

**Research question**: How can large language models enable effective modular task decomposition and dynamic collaboration in multi-agent systems for complex task execution?
**Methodology**: The authors propose a multi-agent architecture that converts natural language task descriptions into unified semantic representations using large language models, then applies modular decomposition to break goals into hierarchical sub-tasks with dynamic scheduling and routing mechanisms.
**Key findings**:
- The proposed method outperforms existing approaches in task success rate and decomposition efficiency
- The architecture achieves better balance between task complexity and communication overhead
- Dynamic scheduling allows continuous strategy adjustment based on environmental feedback
- Constraint parsing prevents performance degradation from redundant communication or uneven resource allocation
**Limitations**: not stated in abstract

### Park et al. (2025)

**Research question**: Can post-training multiple LLMs together using reinforcement learning elicit better collaborative behaviors than relying on innate capabilities or training individual models?
**Methodology**: The authors introduce MAPoRL, a post-training paradigm where multiple LLMs generate responses independently, engage in multi-turn discussions to collaboratively improve answers, and are evaluated by a verifier that scores both the answer and discussion quality, optimized through multi-agent reinforcement learning.
**Key findings**:
- Training individual LLMs alone is insufficient to induce effective collaboration
- Multi-agent co-training boosts collaboration performance across benchmarks
- The approach generalizes to unseen domains beyond training data
- The verifier rewards corrective and persuasive discussions, encouraging meaningful collaboration
**Limitations**: not stated in abstract

### Rao et al. (2026)

**Research question**: How can AI infrastructure be redesigned to enable lightweight, constant-time instantiation of stateful AI agents at production scale?
**Methodology**: The paper introduces Aethon, a reference-based replication primitive that represents agent instances as compositional views over stable definitions, layered memory, and local contextual overlays, using layered inheritance and copy-on-write semantics.
**Key findings**:
- Aethon enables near-constant-time instantiation by shifting from duplication to reference-based representation
- Reference-based instantiation decouples creation cost from inherited structure
- The approach supports lightweight, composable execution identities that can be spawned and specialized at scale
- Aethon provides a more appropriate systems abstraction for production-scale agentic software
**Limitations**: not stated in abstract

### Salve et al. (2024)

**Research question**: How can multi-agent systems improve Retrieval-Augmented Generation (RAG) performance when handling diverse data sources such as relational databases, document stores, and graph databases?
**Methodology**: The authors propose a multi-agent RAG system where specialized agents, each optimized for a specific data source (relational, NoSQL, document-based), handle query generation collaboratively within a modular framework with query execution delegated to an environment designed for compatibility across various database types.
**Key findings**:
- The distributed approach enhances query efficiency compared to single-agent RAG architectures
- Specialized agents reduce token overhead by focusing on their specific data source type
- The system improves response accuracy through agent specialization
- The modular framework is scalable and adaptable to diverse, dynamic, or private data sources
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can automated multi-modal evaluation frameworks based on LLMs and multi-agent collaboration address the challenges of high manual costs, inconsistent standards, and subjective bias in evaluating mobile intelligent assistants?
**Methodology**: The authors propose a three-tier agent architecture consisting of interaction evaluation agents, semantic verification agents, and experience decision agents, using supervised fine-tuning on the Qwen3-8B model and tested on eight major intelligent agents.
**Key findings**:
- The framework achieves significant evaluation matching accuracy with human experts
- The three-tier architecture effectively predicts users' satisfaction with mobile assistants
- The framework can identify generation defects in assistant responses
- Supervised fine-tuning on Qwen3-8B enables automated evaluation without manual costs
**Limitations**: not stated in abstract

### Xuan et al. (2026)

**Research question**: Can an LLM-based multi-agent system effectively evaluate new product concepts to overcome limitations of traditional expert-led approaches?
**Methodology**: The study proposes an automated approach using an LLM-based multi-agent system with eight virtual agents representing specialized domains (e.g., R&D, marketing), using retrieval-augmented generation (RAG) and real-time search tools, fine-tuned using professional product review data, evaluated through a case study involving display monitor concepts.
**Key findings**:
- The system's evaluation rankings were consistent with those of senior industry experts
- Eight virtual agents representing specialized domains can collaboratively validate product concepts
- Retrieval-augmented generation and real-time search tools enable agents to gather objective evidence
- Fine-tuning with professional product review data enhances agent judgment accuracy
**Limitations**: not stated in abstract

### Zhou et al. (2025)

**Research question**: How can hallucination amplification and error propagation in LLM multi-agent collaborations be detected and mitigated?
**Methodology**: GUARDIAN models the multi-agent collaboration process as a discrete-time temporal attributed graph and uses an unsupervised encoder-decoder architecture with incremental training to identify anomalous nodes and edges, incorporating a graph abstraction mechanism based on Information Bottleneck Theory.
**Key findings**:
- GUARDIAN achieves state-of-the-art accuracy in detecting and mitigating safety concerns in multi-agent collaborations
- Modeling collaboration as a temporal attributed graph explicitly captures hallucination and error propagation dynamics
- The unsupervised encoder-decoder architecture enables identification of anomalous nodes and edges with high precision
- Graph abstraction based on Information Bottleneck Theory compresses interactions while preserving essential patterns
**Limitations**: not stated in abstract

## References

Chen, K., Liu, M., Zong, D., Ding, C., Rui, S., Jiang, Y., Zhou, M., & Wang, X. (2025). Mediator-guided multi-agent collaboration among open-source models for medical decision-making. arXiv. https://arxiv.org/abs/2508.05996

Chen, X., Han, X., Zhang, K., Ren, G., Wang, Y., Cao, W., Zhou, Y., Lu, J., & Song, Z. (2025). APD-agents: A large language model-driven multi-agents collaborative framework for automated page design. arXiv. https://arxiv.org/abs/2511.14101

Masters, C., Grześkiewicz, M., & Albrecht, S. V. (2025). ARCANE: A multi-agent framework for interpretable and configurable alignment. arXiv. https://arxiv.org/abs/2512.06196

Pan, S., & Wu, D. (2025). Modular task decomposition and dynamic collaboration in multi-agent systems driven by large language models. arXiv. https://arxiv.org/abs/2511.01149

Park, C., Han, S., Guo, X., Ozdaglar, A., Zhang, K., & Kim, J.-K. (2025). MAPoRL: Multi-agent post-co-training for collaborative large language models with reinforcement learning. arXiv. https://arxiv.org/abs/2502.18439

Rao, S., Kashalkar, K., Somashekar, P., & Krishnan, P. (2026). Aethon: A reference-based replication primitive for constant-time instantiation of stateful AI agents. arXiv. https://arxiv.org/abs/2604.12129

Salve, A., Attar, S., Deshmukh, M., Shivpuje, S., & Utsab, A. M. (2024). A collaborative multi-agent approach to retrieval-augmented generation across diverse data. arXiv. https://arxiv.org/abs/2412.05838

Wang, M., Zhong, J., Han, R., Kang, L., Shi, Z., Liang, X., Lin, X., Gao, N., & Zhang, H. (2025). An automated multi-modal evaluation framework for mobile intelligent assistants based on large language models and multi-agent collaboration. arXiv. https://arxiv.org/abs/2508.09507

Xuan, B., Ai, R., & Lee, H. (2026). An interactive multi-agent system for evaluation of new product concepts. arXiv. https://arxiv.org/abs/2603.05980

Zhou, J., Wang, L., & Yang, X. (2025). GUARDIAN: Safeguarding LLM multi-agent collaborations with temporal graph modeling. arXiv. https://arxiv.org/abs/2505.19234
