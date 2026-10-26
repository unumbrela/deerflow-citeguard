# Systematic Literature Review: Deep Research

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "deep research", category cs.CL, published between 2023-11-24 and 2025-11-23
**Citation format**: APA 7th edition

## Executive Summary

The deep research field has rapidly evolved between 2023 and 2025, transitioning from conceptual frameworks to practical systems capable of handling complex, open-ended research tasks. The surveyed literature reveals a field maturing along multiple dimensions: formal characterization of what constitutes deep research, development of comprehensive benchmarks for evaluation, architectural innovations for improved synthesis, and expansion into specialized domains including enterprise analytics and personalized research. A central finding across multiple papers is that deep research is distinguished by high fan-out over concepts during search rather than simply producing lengthy outputs. Despite significant progress, current systems still face challenges with factual reliability, personalization alignment, and geo-temporal reasoning capabilities.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "deep research", filtered to category cs.CL, published between 2023-11-24 and 2025-11-23. Papers were sorted by relevance through co-citation analysis, and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search results**: 50 papers identified by search, 30 shortlisted, 10 screened and included based on centrality scores (9 papers scored 2, 21 papers scored 3).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, semantic scholar citation expansion was unavailable during this search, potentially limiting the candidate pool.

## Themes

### Theme 1: Benchmarking and Evaluation Frameworks

A dominant thread in the literature focuses on establishing rigorous evaluation frameworks for deep research systems. Multiple papers independently recognize that existing benchmarks fail to capture the hierarchical complexity and open-ended nature of real-world deep research tasks. Java et al. (2025) introduce LiveDRBench with 100 challenging tasks, arguing that the core defining feature of deep research is high fan-out over concepts during search. Chen et al. (2025) present BrowseComp-Plus, addressing fairness and transparency issues in evaluation by using a fixed, curated corpus rather than dynamic web APIs that hinder reproducibility.

Abaskohi et al. (2025) extend benchmarking to enterprise contexts with DRBench, spanning 10 domains and requiring agents to search across both public web and private company knowledge. Liang et al. (2025) focus on personalization with PDR-Bench, introducing 250 realistic user-task queries paired with authentic user profiles. These benchmarking efforts collectively reveal that state-of-the-art systems achieve widely varying performance, with F1 scores ranging from 0.02 to 0.72 on challenging tasks (Java et al., 2025), and GPT-5 achieving 55.9% to 70.1% accuracy depending on retrieval integration (Chen et al., 2025).

### Theme 2: Architectural Innovations for Synthesis

Several papers propose novel architectures to improve how deep research systems acquire, organize, and synthesize information. Li et al. (2025) introduce WebWeaver, a dual-agent framework that interleaves evidence acquisition with dynamic outline optimization, establishing new state-of-the-art performance across major benchmarks. The key innovation is maintaining a citation-grounded memory bank that mitigates long-context issues and citation hallucinations through targeted retrieval.

Han et al. (2025) propose Test-Time Diffusion Deep Researcher (TTD-DR), conceptualizing report generation as a diffusion process where an initial skeleton draft is iteratively refined through denoising informed by retrieval. This approach addresses the performance plateau observed when using generic test-time scaling algorithms for complex report generation. Xia et al. (2025) formalize deep research as Hierarchical Constraint Satisfaction Problems and introduce InfoSeek, a dual-agent system that recursively builds Research Trees from webpages, generating over 50K training examples. Their approach enables 3B parameter models to outperform 32B models on BrowseComp-Plus.

### Theme 3: Enterprise and Domain-Specific Applications

The literature shows strong movement toward practical deployment in enterprise settings. Prabhakar et al. (2025) present Enterprise Deep Research (EDR), a multi-agent system with specialized search agents for different sources (General, Academic, GitHub, LinkedIn) and an extensible MCP-based tool ecosystem. The system includes human-in-the-loop steering capabilities and automated report generation with real-time streaming. Their work demonstrates that domain-specific adaptations can outperform general-purpose systems on enterprise analytics tasks without requiring human intervention.

Abaskohi et al. (2025) similarly emphasize the enterprise context, noting that realistic evaluation requires grounding tasks in authentic user personas and accessing heterogeneous knowledge sources including productivity software, cloud file systems, emails, and chat conversations alongside the open web. This theme reflects recognition that deep research value lies not just in web-scale synthesis but in integrating proprietary organizational knowledge.

### Theme 4: Personalization and User Alignment

Emerging work addresses the gap between generic research outputs and personalized user needs. Liang et al. (2025) argue that existing evaluations rely heavily on close-ended benchmarks while open-ended personalized research remains underexplored. Their PQR Evaluation Framework jointly measures Personalization Alignment, Content Quality, and Factual Reliability, recognizing that personalization cannot be evaluated in isolation from accuracy.

This theme connects to broader concerns about intent alignment and steerable systems. Prabhakar et al. (2025) incorporate reflection mechanisms and optional human steering guidance, acknowledging that enterprise users need to guide research direction based on domain expertise. The personalization theme suggests the field is moving beyond "one-size-fits-all" research toward adaptive systems that incorporate user context, preferences, and domain knowledge.

### Theme 5: Formal Characterization and Definition

Several papers attempt to formally characterize what deep research is and how it differs from related tasks. Java et al. (2025) propose that high fan-out over concepts during search—not lengthy report outputs—is the defining feature, distinguishing deep research from single-constraint or flat multi-hop QA tasks. Xia et al. (2025) similarly formalize deep research as Hierarchical Constraint Satisfaction Problems, arguing that existing benchmarks like Natural Questions and HotpotQA fail to capture the required hierarchical complexity.

This theoretical work provides foundations for system design and evaluation. By clarifying what makes deep research distinct, these characterizations help explain why approaches successful on simpler tasks fail when scaled to deep research complexity. The formal definitions also enable more precise benchmark design that targets the actual challenges of deep research rather than proxy tasks.

### Theme 6: Geo-Temporal Reasoning and Contextual Awareness

Martins et al. (2025) identify a critical gap in current systems: lack of geo-temporal capabilities essential for domains like public health, environmental science, and socio-economic analysis. Their vision paper argues that deep research pipelines must augment retrieval and synthesis with geographic and temporal constraint handling. This theme, while represented by a single paper in this set, points to an important dimension where current systems are limited—handling context-rich questions involving "where" and "when" constraints that fundamentally alter information retrieval and synthesis strategies.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key findings. First, there is strong agreement that existing benchmarks are inadequate for evaluating deep research capabilities, with five papers independently proposing new benchmarks (Java et al., 2025; Chen et al., 2025; Abaskohi et al., 2025; Liang et al., 2025; Xia et al., 2025). Second, papers consistently find that current systems struggle with factual reliability and citation accuracy, motivating architectural innovations like WebWeaver's citation-grounded memory bank (Li et al., 2025) and BrowseComp-Plus's fixed corpus approach (Chen et al., 2025). Third, there is consensus that deep research requires hierarchical, multi-step reasoning rather than flat retrieval, formalized through HCSP frameworks (Xia et al., 2025) and fan-out characterizations (Java et al., 2025).

**Disagreements**: The literature shows less disagreement on fundamental claims than on emphasis and approach. Some papers prioritize benchmark design and evaluation (Chen et al., 2025; Java et al., 2025; Abaskohi et al., 2025), while others focus on architectural innovation (Li et al., 2025; Han et al., 2025; Xia et al., 2025). This reflects different views on whether the field's bottleneck is evaluation clarity or system capability. Additionally, while most papers focus on web-scale public information, Martins et al. (2025) argue for geo-temporal reasoning as a critical missing capability, a perspective not emphasized in other surveyed work.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the surveyed papers explicitly state limitations of their approaches in their abstracts, suggesting either space constraints or reluctance to emphasize weaknesses—a gap in transparency that complicates system selection and improvement. Second, while multiple papers address enterprise applications, there is limited discussion of deployment challenges, computational costs, or latency constraints in real-world settings.

Third, geo-temporal reasoning is identified as critical by Martins et al. (2025) but not addressed by other papers, suggesting this capability remains nascent. Fourth, while personalization is recognized as important (Liang et al., 2025; Prabhakar et al., 2025), concrete methods for incorporating user context remain underdeveloped compared to benchmark and architecture work.

Finally, Azime et al. (2025) identify a significant gap between search engines and standalone deep research tools for academic survey writing, noting that current tools show shortcomings in representing targeted areas—suggesting that despite progress, deep research tools have not yet achieved parity with human researchers for complex academic tasks.

## Per-Paper Annotations

### Abaskohi et al. (2025)

**Research question**: How can AI agents be evaluated on complex, open-ended deep research tasks in realistic enterprise settings that require both public web and private company knowledge?
**Methodology**: Introduce DRBench, a benchmark with 100 deep research tasks across 10 enterprise domains, generated through a synthesis pipeline with human-in-the-loop verification. Tasks require agents to identify supporting facts from heterogeneous sources including productivity software, cloud file systems, emails, chat conversations, and the open web.
**Key findings**:
- DRBench evaluates agents on multi-step queries grounded in realistic enterprise user personas and context
- The benchmark spans 10 domains including Sales, Cybersecurity, and Compliance
- Tasks require searching across both public web and private company knowledge bases
- Agents are evaluated on recall of relevant insights, factual accuracy, and coherent report production
- The benchmark highlights strengths, weaknesses, and critical paths for advancing enterprise deep research across diverse models
**Limitations**: Not stated in abstract.

### Azime et al. (2025)

**Research question**: How can we assess the capability of Deep Research tools, and how do existing tools perform on academic survey writing tasks?
**Methodology**: Introduce an evaluation sheet for assessing Deep Research tool capabilities and apply it to evaluate academic survey writing as a use case. Evaluated output reports from OpenAI's Deep Search and Google's Deep Search using their evaluation framework.
**Key findings**:
- Large Language Models with agentic capabilities can perform knowledge-intensive tasks without human involvement through deep research tools
- Carefully crafted evaluation standards are needed for assessing deep research tool capabilities
- There is a significant gap between search engines and standalone Deep Research tools in generating academic surveys
- Current deep research tools show shortcomings in representing the targeted area when generating academic surveys
**Limitations**: Not stated in abstract.

### Chen et al. (2025)

**Research question**: How can deep-research agent evaluation benchmarks be made more fair and transparent by addressing the limitations of black-box live web search APIs?
**Methodology**: Introduce BrowseComp-Plus, a benchmark derived from BrowseComp that employs a fixed, carefully curated corpus with human-verified supporting documents and mined challenging negatives. Evaluate multiple deep research systems including Search-R1 with BM25 retriever and GPT-5 with different retriever configurations.
**Key findings**:
- Current benchmarks like BrowseComp have limitations in fairness due to dynamic, opaque web APIs that hinder reproducibility
- BrowseComp-Plus enables controlled experimentation with a fixed corpus and human-verified supporting documents
- Search-R1 with BM25 retriever achieves only 3.86% accuracy on the benchmark
- GPT-5 achieves 55.9% accuracy, which improves to 70.1% when integrated with Qwen3-Embedding-8B retriever
- The benchmark allows disentangled analysis of deep research agents and retrieval methods
**Limitations**: Not stated in abstract.

### Han et al. (2025)

**Research question**: How can deep research agent performance be improved for generating complex, long-form research reports beyond the plateau of generic test-time scaling algorithms?
**Methodology**: Propose Test-Time Diffusion Deep Researcher (TTD-DR), which conceptualizes research report generation as a diffusion process. The framework uses an updatable skeleton draft that is iteratively refined through a denoising process informed by retrieval mechanisms, enhanced by a self-evolutionary algorithm applied to each component of the agentic workflow.
**Key findings**:
- Deep research agent performance often plateaus when generating complex reports with generic test-time scaling algorithms
- TTD-DR initiates report generation with a preliminary draft serving as an evolving foundation
- The draft is iteratively refined through a denoising process dynamically informed by external retrieval
- A self-evolutionary algorithm enhances each component of the agentic workflow for high-quality context generation
- TTD-DR achieves state-of-the-art results on benchmarks requiring intensive search and multi-hop reasoning
**Limitations**: Not stated in abstract.

### Java et al. (2025)

**Research question**: What is the formal characterization of the deep research task and how does it distinguish from other reasoning-intensive problems?
**Methodology**: Propose a formal characterization of deep research defining its core feature as high fan-out over concepts during search, and introduce LiveDRBench with 100 challenging tasks over scientific topics and public interest events using an intermediate output representation encoding key claims uncovered during search.
**Key findings**:
- The core defining feature of deep research is high fan-out over concepts required during search, not lengthy report outputs
- LiveDRBench contains 100 challenging tasks covering scientific topics and public interest events
- State-of-the-art DR systems achieve F1 scores between 0.02 and 0.72, with OpenAI's model performing best at 0.55
- Analysis reveals distribution over referenced sources, branching, and backtracking events executed by current DR systems
**Limitations**: Not stated in abstract.

### Li et al. (2025)

**Research question**: How can AI agents synthesize vast web-scale information into insightful reports while avoiding hallucination and citation accuracy issues?
**Methodology**: Introduce WebWeaver, a dual-agent framework that emulates human research through iterative interleaving of evidence acquisition with outline optimization. The planner produces citation-grounded outlines linked to a memory bank of evidence, while the writer executes hierarchical retrieval and writing section by section.
**Key findings**:
- WebWeaver establishes new state-of-the-art performance across major OEDR benchmarks including DeepResearch Bench, DeepConsult, and DeepResearchGym
- The dynamic cycle of interleaving evidence acquisition with outline optimization produces comprehensive, citation-grounded reports
- Targeted retrieval from the memory bank via citations effectively mitigates long-context issues and citation hallucinations
- Adaptive planning and focused synthesis are crucial for producing comprehensive, trusted, and well-structured reports
**Limitations**: Not stated in abstract.

### Liang et al. (2025)

**Research question**: How can Deep Research Agents be evaluated for personalization capabilities in realistic user scenarios?
**Methodology**: Introduce PDR-Bench, the first benchmark for evaluating personalization in DRAs, pairing 50 diverse research tasks across 10 domains with 25 authentic user profiles combining structured persona attributes with dynamic real-world contexts. Propose the PQR Evaluation Framework measuring Personalization Alignment, Content Quality, and Factual Reliability.
**Key findings**:
- PDR-Bench yields 250 realistic user-task queries for evaluating personalized deep research
- The PQR Evaluation Framework jointly measures Personalization Alignment, Content Quality, and Factual Reliability
- Experiments on various systems highlight current capabilities and limitations in handling personalized deep research
- Existing evaluations mostly rely on close-ended benchmarks while open-ended deep research benchmarks remain scarce
**Limitations**: Not stated in abstract.

### Martins et al. (2025)

**Research question**: How can deep research systems be augmented with geo-temporal capabilities to handle context-rich questions involving geographic and/or temporal constraints?
**Methodology**: Present a vision paper identifying technical, infrastructural, and evaluative challenges in integrating geo-temporal reasoning into deep research pipelines. Argue for augmenting retrieval and synthesis processes with geo-temporal constraint handling through open infrastructures and rigorous evaluation protocols.
**Key findings**:
- Current deep research systems lack geo-temporal capabilities essential for domains like public health, environmental science, and socio-economic analysis
- Geo-temporal reasoning requires augmenting retrieval and synthesis processes to handle geographic and temporal constraints
- Open and reproducible infrastructures are needed to support geo-temporally aware deep research systems
- Rigorous evaluation protocols are essential for assessing geo-temporal deep research systems
**Limitations**: Not stated in abstract.

### Prabhakar et al. (2025)

**Research question**: How can autonomous agents be adapted to handle domain-specific nuances, intent alignment, and enterprise integration for transforming unstructured data into actionable insights?
**Methodology**: Present Enterprise Deep Research (EDR), a multi-agent system integrating a Master Planning Agent for adaptive query decomposition, four specialized search agents (General, Academic, GitHub, LinkedIn), an extensible MCP-based tool ecosystem, a Visualization Agent, and a reflection mechanism with optional human-in-the-loop steering guidance.
**Key findings**:
- EDR outperforms state-of-the-art agentic systems on open-ended benchmarks including DeepResearch Bench and DeepConsult without human steering
- The system enables automated report generation, real-time streaming, and seamless enterprise deployment
- The reflection mechanism detects knowledge gaps and updates research direction with optional human-in-the-loop steering
- The framework and benchmark trajectories are released to advance research on multi-agent reasoning applications
**Limitations**: Not stated in abstract.

### Xia et al. (2025)

**Research question**: How can complex Deep Research tasks be synthesized at scale to address the gap between existing benchmarks and the hierarchical complexity required for deep research?
**Methodology**: Formalize Deep Research tasks as Hierarchical Constraint Satisfaction Problems (HCSPs) and introduce InfoSeek, a scalable framework using a dual-agent system to recursively build Research Trees from large-scale webpages. The framework generates over 50K training examples with reasoning trajectories via reject sampling.
**Key findings**:
- Deep Research tasks are fundamentally different from single-constraint, multi-hop, or flat CSP formulations
- Existing benchmarks like Natural Questions and HotpotQA fail to capture the hierarchical complexity of deep research
- InfoSeek uses a dual-agent system to build Research Trees and convert them into natural language questions
- Models trained on InfoSeek consistently outperform strong baselines across different model sizes
- 3B LLMs optimized with InfoSeek surpass 32B models and lightweight commercial APIs on BrowseComp-Plus
**Limitations**: Not stated in abstract.

## References

Abaskohi, A., Chen, T., Muñoz-Mármol, M., Fox, C., Ramesh, A. V., Marcotte, É., Lù, X. H., Chapados, N., Gella, S., West, P., Carenini, G., Pal, C., Drouin, A., & Laradji, I. H. (2025). DRBench: A realistic benchmark for enterprise deep research. arXiv. https://arxiv.org/abs/2510.00172

Azime, I. A., Belay, T. D., & Tonja, A. L. (2025). Evaluation sheet for deep research: A use case for academic survey writing. arXiv. https://arxiv.org/abs/2510.01283

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A more fair and transparent evaluation benchmark of deep-research agent. arXiv. https://arxiv.org/abs/2508.06600

Han, R., Chen, Y., CuiZhu, Z., Miculicich, L., Sun, G., Bi, Y., Wen, W., Wan, H., Wen, C., Maître, S., Lee, G., Tirumalashetty, V., Xue, E., Zhang, Z., Haykal, S., Gokturk, B., Pfister, T., & Lee, C.-Y. (2025). Deep researcher with test-time diffusion. arXiv. https://arxiv.org/abs/2507.16075

Java, A., Khandelwal, A., Midigeshi, S., Halfaker, A., Deshpande, A., Goyal, N., Gupta, A., Natarajan, N., & Sharma, A. (2025). Characterizing deep research: A benchmark and formal definition. arXiv. https://arxiv.org/abs/2508.04183

Li, Z., Guan, X., Zhang, B., Huang, S., Zhou, H., Lai, S., Yan, M., Jiang, Y., Xie, P., Huang, F., Zhang, J., & Zhou, J. (2025). WebWeaver: Structuring web-scale evidence with dynamic outlines for open-ended deep research. arXiv. https://arxiv.org/abs/2509.13312

Liang, Y., Li, J., Wang, Y., Wang, P., Tian, M., Liu, P., Qiao, S., Fang, R., Zhu, H., Zhang, G., Liu, M., Jiang, Y. E., Zhang, N., & Zhou, W. (2025). Towards personalized deep research: Benchmarks and evaluations. arXiv. https://arxiv.org/abs/2509.25106

Martins, B., Szymański, P., & Gramacki, P. (2025). A vision for geo-temporal deep research systems: Towards comprehensive, transparent, and reproducible geo-temporal information synthesis. arXiv. https://arxiv.org/abs/2506.14345

Prabhakar, A., Ram, R., Chen, Z., Savarese, S., Wang, F., Xiong, C., Wang, H., & Yao, W. (2025). Enterprise deep research: Steerable multi-agent deep research for enterprise analytics. arXiv. https://arxiv.org/abs/2510.17797

Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025). Open data synthesis for deep research. arXiv. https://arxiv.org/abs/2509.00375
