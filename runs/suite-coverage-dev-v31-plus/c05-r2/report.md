# Systematic Literature Review: Deep Research

**Date:** October 26, 2026  
**Search Period:** November 24, 2023 – November 23, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Number of Papers:** 10

---

## Executive Summary

This systematic literature review examines recent advances in Deep Research systems—autonomous AI agents capable of conducting complex investigations and generating comprehensive reports. The reviewed literature, published between November 2023 and November 2025, reveals several key themes: (1) formal characterization and benchmarking of deep research tasks, (2) novel architectural frameworks for multi-agent systems, (3) personalization and enterprise applications, and (4) evaluation methodologies. The field demonstrates rapid maturation with increasing focus on reproducibility, transparency, and real-world applicability.

---

## Introduction

Deep Research has emerged as a critical capability in AI systems, requiring agents to decompose complex questions, coordinate multi-step reasoning, and synthesize evidence from diverse sources. This review systematically examines 10 peer-reviewed papers from arXiv's cs.CL category that contribute to the theoretical foundations, architectural innovations, and evaluation frameworks for Deep Research systems.

---

## Methodology

### Search Strategy

A systematic search was conducted on arXiv for papers with the following criteria:
- **Keywords:** "Deep Research"
- **Category:** cs.CL (Computational Linguistics)
- **Publication Date Range:** November 24, 2023 – November 23, 2025
- **Result Count:** 10 papers

### Selection Criteria

Papers were included if they:
1. Addressed deep research systems, benchmarks, or methodologies
2. Were published in the cs.CL category
3. Fell within the specified date range
4. Provided empirical evaluation or theoretical contributions

---

## Review of Selected Papers

### 1. WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research

**Authors:** Li, Z., Guan, X., Zhang, B., Huang, S., Zhou, H., Lai, S., Yan, M., Jiang, Y., Xie, P., Huang, F., Zhang, J., & Zhou, J. (2025).

**Publication Date:** September 16, 2025  
**URL:** https://arxiv.org/abs/2509.13312v3

**Summary:**  
This paper addresses open-ended deep research (OEDR), where AI agents must synthesize vast web-scale information into insightful reports. The authors identify two key limitations in current approaches: static research pipelines that decouple planning from evidence acquisition, and monolithic generation paradigms that include redundant, irrelevant evidence. They introduce WebWeaver, a dual-agent framework emulating human research processes. The planner operates in a dynamic cycle, iteratively interleaving evidence acquisition with outline optimization, while the writer executes hierarchical retrieval and writing. WebWeaver achieves state-of-the-art results on DeepResearch Bench, DeepConsult, and DeepResearchGym benchmarks.

**Key Contributions:**
- Dynamic outline optimization interleaved with evidence acquisition
- Dual-agent architecture separating planning and writing
- Mitigation of long-context issues and citation hallucinations
- State-of-the-art performance on major OEDR benchmarks

---

### 2. Towards Personalized Deep Research: Benchmarks and Evaluations

**Authors:** Liang, Y., Li, J., Wang, Y., Wang, P., Tian, M., Liu, P., Qiao, S., Fang, R., Zhu, H., Zhang, G., Liu, M., Jiang, Y. E., Zhang, N., & Zhou, W. (2025).

**Publication Date:** September 29, 2025  
**URL:** https://arxiv.org/abs/2509.25106v3

**Summary:**  
This work addresses the gap in personalized deep research evaluation. The authors introduce Personalized Deep Research Bench (PDR-Bench), the first benchmark for evaluating personalization in Deep Research Agents (DRAs). PDR-Bench comprises 50 diverse research tasks across 10 domains paired with 25 authentic user profiles combining structured persona attributes with dynamic real-world contexts, yielding 250 realistic user-task queries. The PQR Evaluation Framework jointly measures Personalization Alignment, Content Quality, and Factual Reliability. Experiments reveal current capabilities and limitations in handling personalized deep research.

**Key Contributions:**
- First benchmark for personalized deep research (PDR-Bench)
- PQR Evaluation Framework (Personalization, Quality, Reliability)
- 250 realistic user-task queries with authentic user profiles
- Comprehensive evaluation of existing systems on personalization

---

### 3. Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics

**Authors:** Prabhakar, A., Ram, R., Chen, Z., Savarese, S., Wang, F., Xiong, C., Wang, H., & Yao, W. (2025).

**Publication Date:** October 20, 2025  
**URL:** https://arxiv.org/abs/2510.17797v2

**Summary:**  
This paper presents Enterprise Deep Research (EDR), a multi-agent system designed for enterprise analytics. EDR integrates five components: (1) a Master Planning Agent for adaptive query decomposition, (2) four specialized search agents (General, Academic, GitHub, LinkedIn), (3) an extensible MCP-based tool ecosystem supporting NL2SQL, file analysis, and enterprise workflows, (4) a Visualization Agent for data-driven insights, and (5) a reflection mechanism with optional human-in-the-loop steering. EDR outperforms state-of-the-art agentic systems on DeepResearch Bench and DeepConsult without human steering.

**Key Contributions:**
- Multi-agent architecture with specialized search agents
- MCP-based extensible tool ecosystem for enterprise integration
- Human-in-the-loop steering capability
- Real-time streaming and automated report generation

---

### 4. Characterizing Deep Research: A Benchmark and Formal Definition

**Authors:** Java, A., Khandelwal, A., Midigeshi, S., Halfaker, A., Deshpande, A., Goyal, N., Gupta, A., Natarajan, N., & Sharma, A. (2025).

**Publication Date:** August 6, 2025  
**URL:** https://arxiv.org/abs/2508.04183v1

**Summary:**  
This foundational work proposes a formal characterization of deep research tasks and introduces LiveDRBench, a benchmark for evaluation. The authors argue that the core defining feature of deep research is not lengthy report outputs, but rather the high fan-out over concepts required during search—broad and reasoning-intensive exploration. They define DR using an intermediate output representation encoding key claims, separating reasoning from surface-level report generation. LiveDRBench includes 100 challenging tasks over scientific topics and public interest events. Evaluation of state-of-the-art systems reveals F1 scores ranging from 0.02 to 0.72, with OpenAI's model achieving the best overall F1 of 0.55.

**Key Contributions:**
- Formal definition of deep research tasks
- LiveDRBench with 100 challenging tasks
- Intermediate output representation separating reasoning from generation
- Comprehensive analysis of current system limitations

---

### 5. BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent

**Authors:** Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025).

**Publication Date:** August 8, 2025  
**URL:** https://arxiv.org/abs/2508.06600v1

**Summary:**  
This paper addresses limitations in current deep research benchmarks, particularly BrowseComp's reliance on black-box live web search APIs. The authors introduce BrowseComp-Plus, employing a fixed, carefully curated corpus with human-verified supporting documents and mined challenging negatives. This enables controlled experimentation and fair comparisons. The benchmark effectively distinguishes system performance: Search-R1 with BM25 achieves 3.86% accuracy, while GPT-5 achieves 55.9%, and GPT-5 with Qwen3-Embedding-8B retriever reaches 70.1% with fewer search calls.

**Key Contributions:**
- Fixed corpus enabling fair and reproducible comparisons
- Human-verified supporting documents with challenging negatives
- Disentangled analysis of retrieval and reasoning components
- Significant performance differentiation across systems

---

### 6. Open Data Synthesis For Deep Research

**Authors:** Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025).

**Publication Date:** August 30, 2025  
**URL:** https://arxiv.org/abs/2509.00375v1

**Summary:**  
This work formalizes Deep Research tasks with verifiable answers as Hierarchical Constraint Satisfaction Problems (HCSPs), fundamentally different from single-constraint or flat CSP formulations. The authors introduce InfoSeek, a scalable framework for synthesizing complex Deep Research tasks using a dual-agent system that recursively builds Research Trees from webpages. InfoSeek generates over 50K training examples and reasoning trajectories via reject sampling. Models trained on InfoSeek consistently outperform baselines: 3B LLMs optimized with InfoSeek surpass 32B models and commercial APIs on BrowseComp-Plus.

**Key Contributions:**
- Formalization of Deep Research as Hierarchical CSPs
- InfoSeek framework for scalable data synthesis
- Research Tree construction from web-scale data
- Superior performance with significantly smaller models

---

### 7. DRBench: A Realistic Benchmark for Enterprise Deep Research

**Authors:** Abaskohi, A., Chen, T., Muñoz-Mármol, M., Fox, C., Ramesh, A. V., Marcotte, É., Lù, X. H., Chapados, N., Gella, S., West, P., Carenini, G., Pal, C., Drouin, A., & Laradji, I. H. (2025).

**Publication Date:** September 30, 2025  
**URL:** https://arxiv.org/abs/2510.00172v2

**Summary:**  
DRBench evaluates AI agents on complex, open-ended deep research tasks in enterprise settings. Unlike prior benchmarks focusing on simple questions or web-only queries, DRBench evaluates multi-step queries requiring facts from both public web and private company knowledge bases. Tasks span heterogeneous search spaces including productivity software, cloud file systems, emails, chat conversations, and the open web. The benchmark includes 100 tasks across 10 domains (Sales, Cybersecurity, Compliance) with human-in-the-loop verification. Agents are evaluated on insight recall, factual accuracy, and coherent report production.

**Key Contributions:**
- Enterprise-focused benchmark with private and public knowledge integration
- 100 tasks across 10 enterprise domains
- Realistic user personas and enterprise context
- Comprehensive evaluation of open and closed-source models

---

### 8. Deep Researcher with Test-Time Diffusion

**Authors:** Han, R., Chen, Y., CuiZhu, Z., Miculicich, L., Sun, G., Bi, Y., Wen, W., Wan, H., Wen, C., Maître, S., Lee, G., Tirumalashetty, V., Xue, E., Zhang, Z., Haykal, S., Gokturk, B., Pfister, T., & Lee, C.-Y. (2025).

**Publication Date:** July 21, 2025  
**URL:** https://arxiv.org/abs/2507.16075v1

**Summary:**  
This paper proposes Test-Time Diffusion Deep Researcher (TTD-DR), conceptualizing research report generation as a diffusion process. TTD-DR initiates with a preliminary draft—an updatable skeleton guiding research direction—then iteratively refines through a "denoising" process dynamically informed by retrieval at each step. A self-evolutionary algorithm enhances each component of the agentic workflow. This draft-centric design improves timeliness and coherence while reducing information loss. TTD-DR achieves state-of-the-art results on benchmarks requiring intensive search and multi-hop reasoning.

**Key Contributions:**
- Novel diffusion-based framework for report generation
- Iterative draft refinement with retrieval-informed denoising
- Self-evolutionary algorithm for component optimization
- State-of-the-art performance on multi-hop reasoning benchmarks

---

### 9. A Vision for Geo-Temporal Deep Research Systems: Towards Comprehensive, Transparent, and Reproducible Geo-Temporal Information Synthesis

**Authors:** Martins, B., Szymański, P., & Gramacki, P. (2025).

**Publication Date:** June 17, 2025  
**URL:** https://arxiv.org/abs/2506.14345v1

**Summary:**  
This vision paper identifies critical gaps in current deep research systems: lack of geo-temporal capabilities essential for context-rich questions in domains like public health, environmental science, and socio-economic analysis. The authors outline technical, infrastructural, and evaluative challenges in integrating geo-temporal reasoning into deep research pipelines. They argue for augmenting retrieval and synthesis with geo-temporal constraint handling, supported by open and reproducible infrastructures and rigorous evaluation protocols.

**Key Contributions:**
- Vision for geo-temporal deep research systems
- Identification of technical and infrastructural challenges
- Framework for geo-temporal constraint handling
- Call for open and reproducible evaluation protocols

---

### 10. Evaluation Sheet for Deep Research: A Use Case for Academic Survey Writing

**Authors:** Azime, I. A., Belay, T. D., & Tonja, A. L. (2025).

**Publication Date:** September 30, 2025  
**URL:** https://arxiv.org/abs/2510.01283v1

**Summary:**  
This work introduces an evaluation sheet for assessing Deep Research tools, using academic survey writing as a use case. The authors evaluated OpenAI's Deep Search and Google's Deep Search, revealing significant gaps between search engines and standalone Deep Research tools, particularly in representing targeted areas. Findings emphasize the need for carefully crafted evaluation standards to ensure comprehensive and accurate deep research outputs.

**Key Contributions:**
- Structured evaluation sheet for Deep Research tools
- Academic survey writing as evaluation use case
- Comparative analysis of commercial deep research systems
- Identification of evaluation standard requirements

---

## Thematic Analysis

### Theme 1: Formal Characterization and Definition

Two papers address foundational definitions of deep research. Java et al. (2025) propose that deep research's core feature is high fan-out over concepts during search, not report length. Xia et al. (2025) formalize deep research as Hierarchical Constraint Satisfaction Problems, providing theoretical grounding for task complexity.

### Theme 2: Benchmark Development

Five papers introduce benchmarks addressing different aspects:
- **LiveDRBench** (Java et al., 2025): General deep research with intermediate representations
- **BrowseComp-Plus** (Chen et al., 2025): Fair evaluation with fixed corpus
- **PDR-Bench** (Liang et al., 2025): Personalized deep research
- **DRBench** (Abaskohi et al., 2025): Enterprise-focused tasks
- **InfoSeek** (Xia et al., 2025): Training data synthesis

### Theme 3: Architectural Innovations

Three papers propose novel architectures:
- **WebWeaver** (Li et al., 2025): Dual-agent with dynamic outlines
- **Enterprise Deep Research** (Prabhakar et al., 2025): Multi-agent with specialized searchers
- **TTD-DR** (Han et al., 2025): Diffusion-based report generation

### Theme 4: Specialized Capabilities

Two papers address specialized domains:
- **Geo-Temporal Systems** (Martins et al., 2025): Vision for spatial-temporal reasoning
- **Enterprise Analytics** (Prabhakar et al., 2025; Abaskohi et al., 2025): Integration with private knowledge bases

### Theme 5: Evaluation Methodologies

Azime et al. (2025) and Liang et al. (2025) emphasize rigorous evaluation frameworks, with the PQR framework measuring personalization, quality, and reliability jointly.

---

## Critical Analysis

### Strengths of Current Research

1. **Rapid Benchmark Development:** The field shows maturation through diverse benchmarks addressing personalization, enterprise needs, and fairness.

2. **Architectural Innovation:** Novel frameworks like WebWeaver's dual-agent approach and TTD-DR's diffusion process demonstrate creative solutions to core challenges.

3. **Formal Foundations:** Theoretical work on HCSPs and intermediate representations provides rigorous grounding for future research.

4. **Real-World Applicability:** Enterprise-focused research (EDR, DRBench) bridges academic research and practical deployment.

### Limitations and Gaps

1. **Geo-Temporal Gap:** Only one paper (Martins et al., 2025) addresses geo-temporal reasoning, despite its importance in many domains.

2. **Reproducibility Concerns:** While BrowseComp-Plus addresses this, many benchmarks still rely on dynamic web APIs limiting reproducibility.

3. **Performance Gaps:** Java et al. (2025) report F1 scores as low as 0.02 for some subcategories, indicating significant room for improvement.

4. **Evaluation Standardization:** Azime et al. (2025) highlight the lack of standardized evaluation criteria across studies.

---

## Future Directions

Based on the reviewed literature, several promising directions emerge:

1. **Geo-Temporal Integration:** Developing systems with native geo-temporal reasoning capabilities as envisioned by Martins et al. (2025).

2. **Personalization Advances:** Building on PDR-Bench to create truly personalized research assistants adapting to individual user contexts.

3. **Enterprise Integration:** Expanding MCP-based ecosystems for seamless enterprise workflow integration.

4. **Evaluation Standards:** Establishing unified evaluation frameworks combining personalization, quality, and reliability metrics.

5. **Efficiency Improvements:** Leveraging insights from InfoSeek to achieve strong performance with smaller models.

6. **Transparency and Reproducibility:** Following BrowseComp-Plus's approach with fixed corpora for fair comparisons.

---

## Conclusion

The deep research field demonstrates rapid advancement with significant progress in formal characterization, benchmark development, architectural innovation, and evaluation methodologies. The 10 reviewed papers collectively establish foundations for autonomous agents capable of conducting complex investigations across diverse domains. Key challenges remain in geo-temporal reasoning, reproducibility, and standardization, but the trajectory suggests continued maturation toward practical, reliable deep research systems.

The convergence of dual-agent architectures, diffusion-based generation, hierarchical task formalization, and comprehensive benchmarks positions deep research as a critical capability in AI systems. Future work should prioritize geo-temporal integration, personalization, enterprise applicability, and standardized evaluation to realize the full potential of autonomous research agents.

---

## References

Abaskohi, A., Chen, T., Muñoz-Mármol, M., Fox, C., Ramesh, A. V., Marcotte, É., Lù, X. H., Chapados, N., Gella, S., West, P., Carenini, G., Pal, C., Drouin, A., & Laradji, I. H. (2025). DRBench: A Realistic Benchmark for Enterprise Deep Research. *arXiv preprint arXiv:2510.00172*. https://arxiv.org/abs/2510.00172v2

Azime, I. A., Belay, T. D., & Tonja, A. L. (2025). Evaluation Sheet for Deep Research: A Use Case for Academic Survey Writing. *arXiv preprint arXiv:2510.01283*. https://arxiv.org/abs/2510.01283v1

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent. *arXiv preprint arXiv:2508.06600*. https://arxiv.org/abs/2508.06600v1

Han, R., Chen, Y., CuiZhu, Z., Miculicich, L., Sun, G., Bi, Y., Wen, W., Wan, H., Wen, C., Maître, S., Lee, G., Tirumalashetty, V., Xue, E., Zhang, Z., Haykal, S., Gokturk, B., Pfister, T., & Lee, C.-Y. (2025). Deep Researcher with Test-Time Diffusion. *arXiv preprint arXiv:2507.16075*. https://arxiv.org/abs/2507.16075v1

Java, A., Khandelwal, A., Midigeshi, S., Halfaker, A., Deshpande, A., Goyal, N., Gupta, A., Natarajan, N., & Sharma, A. (2025). Characterizing Deep Research: A Benchmark and Formal Definition. *arXiv preprint arXiv:2508.04183*. https://arxiv.org/abs/2508.04183v1

Li, Z., Guan, X., Zhang, B., Huang, S., Zhou, H., Lai, S., Yan, M., Jiang, Y., Xie, P., Huang, F., Zhang, J., & Zhou, J. (2025). WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research. *arXiv preprint arXiv:2509.13312*. https://arxiv.org/abs/2509.13312v3

Liang, Y., Li, J., Wang, Y., Wang, P., Tian, M., Liu, P., Qiao, S., Fang, R., Zhu, H., Zhang, G., Liu, M., Jiang, Y. E., Zhang, N., & Zhou, W. (2025). Towards Personalized Deep Research: Benchmarks and Evaluations. *arXiv preprint arXiv:2509.25106*. https://arxiv.org/abs/2509.25106v3

Martins, B., Szymański, P., & Gramacki, P. (2025). A Vision for Geo-Temporal Deep Research Systems: Towards Comprehensive, Transparent, and Reproducible Geo-Temporal Information Synthesis. *arXiv preprint arXiv:2506.14345*. https://arxiv.org/abs/2506.14345v1

Prabhakar, A., Ram, R., Chen, Z., Savarese, S., Wang, F., Xiong, C., Wang, H., & Yao, W. (2025). Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics. *arXiv preprint arXiv:2510.17797*. https://arxiv.org/abs/2510.17797v2

Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025). Open Data Synthesis For Deep Research. *arXiv preprint arXiv:2509.00375*. https://arxiv.org/abs/2509.00375v1

---

## Appendix: Search Methodology Details

**Database:** arXiv  
**Search Query:** "Deep Research"  
**Category Filter:** cs.CL (Computational Linguistics)  
**Date Range:** 2023-11-24 to 2025-11-23  
**Total Results:** 10 papers  
**Retrieval Date:** October 26, 2026

All papers were retrieved through systematic arXiv search with exact phrase matching for "Deep Research" in the cs.CL category within the specified publication window.
