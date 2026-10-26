# Systematic Literature Review: Deep Research Agents (2023-2025)

## Abstract

This systematic literature review examines ten peer-reviewed papers on deep research agents published between November 24, 2023, and November 23, 2025, focusing on works primarily categorized under computer science - computation and language (cs.CL). The rapid advancement of large language models has enabled autonomous agents capable of conducting complex information synthesis tasks across diverse web sources. This review synthesizes current approaches, benchmarks, evaluation methodologies, and emerging challenges in the field of deep research agent development. Key themes include framework architecture design, benchmark standardization, personalization capabilities, enterprise applications, efficiency optimization, and formal task characterization.

## Introduction

Deep research represents a paradigm shift in how AI systems approach complex information synthesis tasks. Unlike traditional search or question-answering systems, deep research agents autonomously plan investigations, execute multi-step web exploration, synthesize evidence from heterogeneous sources, and generate comprehensive analytical reports grounded in factual information. This systematic review analyzes recent scholarly contributions that define, evaluate, and advance this emerging field.

The selection criteria for this review encompassed papers published within a two-year window (November 24, 2023 - November 23, 2025) with primary categorization in computational linguistics and related fields. Ten relevant papers were identified through systematic arXiv search, representing diverse aspects of deep research including system architectures, benchmark creation, evaluation frameworks, efficiency improvements, and domain-specific adaptations.

## Methodology

This review employed a systematic search strategy using arXiv's academic database with keyword queries focused on "deep research" combined with temporal filtering. Papers were screened based on publication date, primary category relevance, and substantive contribution to the deep research field. All selected papers underwent qualitative synthesis following established systematic review protocols.

## Thematic Analysis

### 1. Framework Architecture and Human-Centric Design

**WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research** (Li et al., 2025) introduces a dual-agent framework addressing critical limitations in existing open-ended deep research approaches. The authors identify two fundamental problems: static research pipelines that decouple planning from evidence acquisition, and monolithic generation paradigms prone to hallucination and citation inaccuracies.

WebWeaver's innovative approach mimics human research methodology through iterative cycles. The planner agent dynamically interleaves evidence acquisition with outline optimization, creating a comprehensive citation-grounded outline linked to a memory bank of evidence. The writer agent then executes hierarchical retrieval, composing reports section-by-section while targeting only necessary evidence via citations. This approach effectively mitigates long-context issues and citation hallucinations.

Experimental validation demonstrates state-of-the-art performance across major benchmarks including DeepResearch Bench, DeepConsult, and DeepResearchGym. These results establish that adaptive planning and focused synthesis are crucial for producing comprehensive, trusted, and well-structured reports.

**Universal Deep Research: Bring Your Own Model and Strategy** (Belcak & Molchanov, 2025) addresses the rigidity observed in current deep research implementations. The authors note that each introduced deep research agent is hard-coded to employ specific research strategies using fixed tool choices, limiting adaptability and customization.

Universal Deep Research (UDR) presents a generalist agentic system that wraps around any language model, enabling users to create, edit, and refine custom deep research strategies without additional training or fine-tuning requirements. The system includes example minimal, expansive, and intensive research strategies, along with a user interface facilitating experimentation. This democratization of strategy development represents a significant step toward accessible and customizable deep research capabilities.

### 2. Benchmark Development and Formal Characterization

**Characterizing Deep Research: A Benchmark and Formal Definition** (Java et al., 2025) addresses a critical gap in the field: the undefined scope of deep research tasks and poor understanding of their distinction from other reasoning-intensive problems. Despite growing interest in deep research terminology, the authors argue that core defining features remain unclear.

The paper proposes a formal characterization arguing that deep research's core feature is not lengthy report-style outputs, but rather high fan-out over concepts during the search process—representing broad and reasoning-intensive exploration. To enable objective evaluation, the authors define deep research using an intermediate output representation encoding key claims uncovered during search, separating the reasoning challenge from surface-level report generation.

Based on this formulation, LiveDRBench was developed—a diverse, challenging benchmark with 100 tasks covering scientific topics (datasets, materials discovery, prior art search) and public interest events (flight incidents, movie awards). Evaluation reveals F1 scores ranging from 0.02 to 0.72 across sub-categories for state-of-the-art deep research systems. OpenAI's model achieved the best overall F1 score of 0.55. Analysis of reasoning traces provided insights into source referencing distributions, branching patterns, and backtracking events, motivating future directions for improving search mechanisms and grounding capabilities.

**BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent** (Chen et al., 2025) addresses notable limitations in current benchmark evaluations like BrowseComp, which rely on black-box live web search APIs. The authors identify three critical problems: (1) fairness issues due to dynamic and opaque web APIs hindering fair comparisons and reproducibility; (2) transparency deficits from lack of control over document corpora preventing isolation of retriever contributions; and (3) inability to conduct well-controlled experiments providing insights into underlying deep research LLM capabilities.

BrowseComp-Plus derives from BrowseComp but employs a fixed, carefully curated corpus. Each query includes human-verified supporting documents and mined challenging negatives, enabling controlled experimentation. The benchmark effectively distinguishes deep research system performance—for instance, Search-R1 with BM25 retriever achieves 3.86% accuracy versus GPT-5 achieving 55.9%. Integrating GPT-5 with Qwen3-Embedding-8B retriever further enhances accuracy to 70.1% with fewer search calls. This benchmark enables comprehensive evaluation and disentangled analysis of deep research agents and retrieval methods, fostering insights into retrieval effectiveness, citation accuracy, and context engineering.

**Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics** (Prabhakar et al., 2025) addresses enterprise-specific challenges where information grows exponentially and organizations must transform unstructured data into coherent, actionable insights. While autonomous agents show promise, they struggle with domain-specific nuances, intent alignment, and enterprise integration.

Enterprise Deep Research (EDR) integrates five components: (1) a Master Planning Agent for adaptive query decomposition; (2) four specialized search agents (General, Academic, GitHub, LinkedIn); (3) an extensible MCP-based tool ecosystem supporting NL2SQL, file analysis, and enterprise workflows; (4) a Visualization Agent for data-driven insights; and (5) a reflection mechanism detecting knowledge gaps and updating research direction with optional human-in-the-loop steering guidance. These components enable automated report generation, real-time streaming, and seamless enterprise deployment validated on internal datasets.

On open-ended benchmarks including DeepResearch Bench and DeepConsult, EDR outperforms state-of-the-art agentic systems without human steering. The framework and benchmark trajectories are released publicly to advance research on multi-agent reasoning applications.

### 3. Personalization and User-Centric Approaches

**Towards Personalized Deep Research: Benchmarks and Evaluations** (Liang et al., 2025) addresses a significant gap: existing evaluations mostly rely on close-ended benchmarks, while open-ended deep research benchmarks remain scarce and typically neglect personalized scenarios. Deep Research Agents demonstrate strong real-world potential but lack evaluation frameworks accounting for individual user preferences and contexts.

The authors introduce Personalized Deep Research Bench (PDR-Bench), the first benchmark specifically evaluating personalization in Deep Research Agents. It pairs 50 diverse research tasks across 10 domains with 25 authentic user profiles combining structured persona attributes with dynamic real-world contexts, yielding 250 realistic user-task queries.

To assess system performance, the PQR Evaluation Framework jointly measures three dimensions: Personalization Alignment, Content Quality, and Factual Reliability. Experiments across various systems highlight current capabilities and limitations in handling personalized deep research. This work establishes a rigorous foundation for developing and evaluating the next generation of truly personalized AI research assistants.

### 4. Efficiency and Resource Optimization

**Efficient Tree-Structured Deep Research with Adaptive Resource Allocation** (Nie et al., 2025) addresses critical constraints in deep research agents' sequential nature of reasoning. This bottleneck results in high latency, poor runtime adaptability, and inefficient resource allocation, making today's deep research systems impractical for interactive applications.

ParallelResearch introduces a novel framework transforming sequential processing into parallel, runtime orchestration by dynamically decomposing complex queries into tree-structured sub-tasks. Core contributions include: (1) an adaptive planner dynamically allocating computational resources based on query complexity; (2) a runtime orchestration layer pruning redundant paths to reallocate resources and enabling speculative execution; and (3) a fully-asynchronous execution infrastructure enabling concurrency across both research breadth and depth.

Experiments on two benchmarks demonstrate up to 5x speedups with comparable final report quality, and consistent quality improvements within the same time budgets. This work significantly advances the practical viability of deep research systems for real-time applications.

### 5. Private Data and Enterprise Integration

**IoDResearch: Deep Research on Private Heterogeneous Data via the Internet of Data** (Shi et al., 2025) addresses limitations in traditional deep research efforts focusing primarily on web search while overlooking local private data. Existing frameworks exhibit low retrieval efficiency for private data and fail to comply with FAIR (Findable, Accessible, Interoperable, Reusable) principles, resulting in inefficiency and limited reusability.

IoDResearch operationalizes the Internet of Data paradigm as a private data-centric Deep Research framework. The system encapsulates heterogeneous resources as FAIR-compliant digital objects, refining them into atomic knowledge units and knowledge graphs, forming a heterogeneous graph index for multi-granularity retrieval. On top of this representation, a multi-agent system supports both reliable question answering and structured scientific report generation.

The authors also establish the IoD DeepResearch Benchmark to systematically evaluate both data representation and Deep Research capabilities in IoD scenarios. Experimental results on retrieval, QA, and report-writing tasks show IoDResearch consistently surpasses representative RAG and Deep Research baselines. This work demonstrates the feasibility of private-data-centric Deep Research under the Internet of Data paradigm, paving the way toward more trustworthy, reusable, and automated scientific discovery.

### 6. Evaluation Platforms and Comparative Analysis

**Deep Research Comparator: A Platform For Fine-grained Human Annotations of Deep Research Agents** (Chandrahasan et al., 2025) addresses the major challenge of effectively evaluating deep research agents that autonomously search the web, analyze information, and generate reports—particularly when assessing long reports and providing detailed feedback on intermediate steps.

The platform offers a holistic framework for: (1) deep research agent hosting; (2) side-by-side comparison; (3) fine-grained human feedback collection; and (4) ranking calculation. Given a user query, the platform displays final reports from two different agents along with their intermediate steps during generation. Annotators can evaluate overall quality through side-by-side comparison and provide detailed feedback by assessing intermediate steps or specific text spans within the final report.

Additionally, the authors develop Simple Deepresearch, an end-to-end agent scaffold serving as a baseline facilitating easy integration of various large language models to transform them into deep research agents for evaluation. Real user preference data was collected from 17 annotators on three deep research agents, demonstrating the platform's utility for deep research agent development.

### 7. Survey and Roadmap Contributions

**Deep Research: A Survey of Autonomous Research Agents** (Zhang et al., 2025) provides a systematic overview of the deep research pipeline comprising four core stages: planning, question developing, web exploration, and report generation. For each stage, the survey analyzes key technical challenges and categorizes representative methods developed to address them.

The survey summarizes recent advances in optimization techniques and benchmarks tailored for deep research. Importantly, it discusses open challenges and promising research directions, aiming to chart a roadmap toward building more capable and trustworthy deep research agents. As one of the few comprehensive surveys in this rapidly evolving field, this work provides essential contextual grounding for understanding the state-of-the-art and future directions.

## Cross-Paper Synthesis

### Evolutionary Trends

Analysis across the ten papers reveals several evolutionary trends in deep research agent development:

1. **From Monolithic to Modular Architectures**: Early approaches emphasized integrated systems, while recent work favors modular, multi-agent designs with specialized components (Li et al., 2025; Prabhakar et al., 2025; Shi et al., 2025).

2. **From Fixed Strategies to Adaptive Systems**: Initial implementations used hardcoded research strategies, progressing toward flexible, user-configurable approaches (Belcak & Molchanov, 2025; Nie et al., 2025).

3. **From Generic to Context-Aware Evaluation**: Benchmarks evolved from general-purpose tests to personalized, domain-specific, and enterprise-oriented evaluation frameworks (Liang et al., 2025; Java et al., 2025; Chen et al., 2025).

4. **From Public Web to Private Data Integration**: Recent developments extend deep research beyond public web sources to incorporate private, heterogeneous data repositories (Shi et al., 2025).

### Common Challenges Across Studies

Despite methodological diversity, several persistent challenges emerge:

1. **Hallucination and Citation Accuracy**: Multiple studies address fact-checking and grounding issues inherent in generative systems (Li et al., 2025; Chen et al., 2025).

2. **Evaluation Standardization**: The field lacks universally accepted benchmarks, leading to fragmented evaluation practices requiring careful cross-validation (Java et al., 2025; Chandrahasan et al., 2025).

3. **Efficiency and Latency**: Sequential processing bottlenecks remain problematic for real-time applications (Nie et al., 2025).

4. **Personalization and Intent Alignment**: Balancing automation with user-specific preferences and organizational context proves challenging (Liang et al., 2025; Prabhakar et al., 2025).

### Emerging Research Directions

Based on identified gaps and stated future work, several promising research directions emerge:

1. **Human-in-the-Loop Steering**: Integrating human oversight while maintaining automation benefits (Prabhakar et al., 2025).

2. **Cross-Modal Research Capabilities**: Extending beyond text-based research to incorporate multimodal data sources.

3. **Federated and Privacy-Preserving Deep Research**: Enabling collaborative research across organizational boundaries while preserving data privacy.

4. **Automated Strategy Generation**: Moving beyond manual strategy design toward ML-driven automatic strategy optimization.

## Limitations of Current Literature

This review identifies several limitations in the current body of work:

1. **Temporal Concentration**: Most papers cluster in mid-to-late 2025, suggesting either recent emergence or concentration of submissions. Earlier foundational work may be underrepresented.

2. **Category Narrowness**: While cs.CL dominates, important contributions in computer science - information retrieval (cs.IR) and distributed computing (cs.DC) categories exist, indicating interdisciplinary nature potentially underexplored.

3. **Benchmark Fragmentation**: Multiple competing benchmarks (LiveDRBench, BrowseComp-Plus, PDR-Bench, DeepResearch Bench) complicate comparative analysis and progress tracking.

4. **Limited Longitudinal Studies**: Absence of longitudinal assessments limits understanding of system evolution and sustained performance over extended periods.

## Practical Implications

The reviewed research carries significant implications for practice:

1. **Enterprise Deployment**: Frameworks like EDR demonstrate viable pathways for organizational adoption of deep research agents with proper integration support (Prabhakar et al., 2025).

2. **Customization Accessibility**: Universal approaches lower barriers to entry, enabling organizations to tailor deep research systems to specific needs without extensive ML expertise (Belcak & Molchanov, 2025).

3. **Performance Optimization**: Efficiency improvements through parallelization make interactive deep research applications practically feasible (Nie et al., 2025).

4. **Privacy Compliance**: Internet of Data frameworks address critical concerns about private data handling in research contexts (Shi et al., 2025).

## Conclusion

This systematic literature review synthesizes ten significant contributions to deep research agent development published between late 2023 and late 2025. The field demonstrates rapid maturation from conceptual foundations to practical, enterprise-ready systems. Key advances include human-centric dual-agent frameworks, formal task characterizations enabling objective evaluation, personalized research capabilities, efficiency optimizations enabling real-time applications, and privacy-preserving architectures for private data research.

Critical challenges remain regarding benchmark standardization, hallucination mitigation, and balancing automation with human oversight. Future research should address these challenges while exploring cross-modal capabilities, federated research paradigms, and automated strategy optimization.

The reviewed work collectively establishes deep research as a distinct and important paradigm in AI-assisted knowledge synthesis, with growing practical significance for enterprises, researchers, and information workers facing increasing complexity in navigating vast information landscapes.

## References

Belcak, P., & Molchanov, P. (2025). Universal Deep Research: Bring Your Own Model and Strategy. *arXiv preprint arXiv:2509.00244*. https://arxiv.org/abs/2509.00244v1

Chandrahasan, P., Jin, J., Zhang, Z., Wang, T., Tang, A., Mo, L., Ziyadi, M., Ribeiro, L. F. R., Qiu, Z., Dreyer, M., Asai, A., & Xiong, C. (2025). Deep Research Comparator: A Platform For Fine-grained Human Annotations of Deep Research Agents. *arXiv preprint arXiv:2507.05495*. https://arxiv.org/abs/2507.05495v2

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent. *arXiv preprint arXiv:2508.06600*. https://arxiv.org/abs/2508.06600v1

Java, A., Khandelwal, A., Midigeshi, S., Halfaker, A., Deshpande, A., Goyal, N., Gupta, A., Natarajan, N., & Sharma, A. (2025). Characterizing Deep Research: A Benchmark and Formal Definition. *arXiv preprint arXiv:2508.04183*. https://arxiv.org/abs/2508.04183v1

Liang, Y., Li, J., Wang, Y., Wang, P., Tian, M., Liu, P., Qiao, S., Fang, R., Zhu, H., Zhang, G., Liu, M., Jiang, Y. E., Zhang, N., & Zhou, W. (2025). Towards Personalized Deep Research: Benchmarks and Evaluations. *arXiv preprint arXiv:2509.25106*. https://arxiv.org/abs/2509.25106v3

Li, Z., Guan, X., Zhang, B., Huang, S., Zhou, H., Lai, S., Yan, M., Jiang, Y., Xie, P., Huang, F., Zhang, J., & Zhou, J. (2025). WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research. *arXiv preprint arXiv:2509.13312*. https://arxiv.org/abs/2509.13312v3

Nie, L., Lipka, N., Rossi, R. A., & Chaudhuri, S. (2025). Efficient Tree-Structured Deep Research with Adaptive Resource Allocation. *arXiv preprint arXiv:2510.05145*. https://arxiv.org/abs/2510.05145v2

Prabhakar, A., Ram, R., Chen, Z., Savarese, S., Wang, F., Xiong, C., Wang, H., & Yao, W. (2025). Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics. *arXiv preprint arXiv:2510.17797*. https://arxiv.org/abs/2510.17797v2

Shi, Z., Guo, Z., Ma, X., Huang, G., Ma, Y., & Jing, X. (2025). IoDResearch: Deep Research on Private Heterogeneous Data via the Internet of Data. *arXiv preprint arXiv:2510.01553*. https://arxiv.org/abs/2510.01553v3

Zhang, W., Li, X., Zhang, Y., Jia, P., Wang, Y., Guo, H., Liu, Y., & Zhao, X. (2025). Deep Research: A Survey of Autonomous Research Agents. *arXiv preprint arXiv:2508.12752*. https://arxiv.org/abs/2508.12752v1

---

*Systematic Literature Review conducted on October 26, 2026*  
*Search parameters: 10 papers, 2023-11-24 to 2025-11-23, cs.CL primary category*
