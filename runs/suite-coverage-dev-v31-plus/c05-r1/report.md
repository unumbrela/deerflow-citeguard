# Systematic Literature Review: Deep Research

**Date:** October 26, 2026  
**Search Period:** November 24, 2023 – November 23, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Total Papers:** 10

---

## Executive Summary

This systematic literature review examines recent advances in Deep Research systems, focusing on ten peer-reviewed papers published between late 2023 and late 2025 in the computational linguistics category. The reviewed literature reveals a rapidly evolving field characterized by three primary research thrusts: (1) novel architectural frameworks for autonomous research agents, (2) benchmark development for rigorous evaluation, and (3) domain-specific adaptations for enterprise and personalized applications. Key findings indicate that current Deep Research systems achieve moderate performance on standardized benchmarks (F1 scores ranging from 0.02 to 0.72), with significant room for improvement in personalization alignment, geo-temporal reasoning, and citation accuracy.

---

## Methodology

This review follows systematic literature review protocols for computational linguistics research. Papers were retrieved from arXiv's cs.CL category with publication dates constrained to the two-year window from November 24, 2023, through November 23, 2025. The search query "Deep Research" was executed using phrase matching to ensure relevance to the core topic. All ten retrieved papers underwent structured analysis covering methodology, contributions, evaluation approaches, and limitations.

---

## Annotated Bibliography (APA Format)

### 1. WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research

Li, Z., Guan, X., Zhang, B., Huang, S., Zhou, H., Lai, S., Yan, M., Jiang, Y., Xie, P., Huang, F., Zhang, J., & Zhou, J. (2025). WebWeaver: Structuring web-scale evidence with dynamic outlines for open-ended deep research. *arXiv preprint arXiv:2509.13312v3*. https://arxiv.org/abs/2509.13312v3

**Summary:** This paper addresses open-ended deep research (OEDR), where AI agents must synthesize vast web-scale information into insightful reports. The authors identify two critical limitations in current approaches: static research pipelines that decouple planning from evidence acquisition, and monolithic generation paradigms that include redundant evidence, leading to hallucinations and low citation accuracy. WebWeaver introduces a dual-agent framework emulating human research processes, where a planner iteratively interleaves evidence acquisition with outline optimization, and a writer executes hierarchical retrieval and writing. The framework achieves state-of-the-art results on DeepResearch Bench, DeepConsult, and DeepResearchGym benchmarks.

**Key Contributions:**
- Dynamic outline optimization linked to evidence memory bank
- Hierarchical retrieval mitigating long-context issues and citation hallucinations
- Human-centric, iterative methodology for adaptive planning

**Evaluation:** State-of-the-art performance across three major OEDR benchmarks.

---

### 2. Towards Personalized Deep Research: Benchmarks and Evaluations

Liang, Y., Li, J., Wang, Y., Wang, P., Tian, M., Liu, P., Qiao, S., Fang, R., Zhu, H., Zhang, G., Liu, M., Jiang, Y. E., Zhang, N., & Zhou, W. (2025). Towards personalized deep research: Benchmarks and evaluations. *arXiv preprint arXiv:2509.25106v3*. https://arxiv.org/abs/2509.25106v3

**Summary:** This work addresses a critical gap in Deep Research Agent (DRA) evaluation: the lack of personalized scenarios in existing benchmarks. The authors introduce Personalized Deep Research Bench (PDR-Bench), the first benchmark for evaluating personalization in DRAs, comprising 50 diverse research tasks across 10 domains paired with 25 authentic user profiles combining structured persona attributes with dynamic real-world contexts (yielding 250 realistic user-task queries). The PQR Evaluation Framework jointly measures Personalization Alignment, Content Quality, and Factual Reliability.

**Key Contributions:**
- First benchmark specifically designed for personalized deep research evaluation
- PQR Framework for multi-dimensional assessment
- Empirical analysis revealing current system capabilities and limitations in personalization

**Evaluation:** Experiments across multiple systems highlight significant limitations in handling personalized deep research scenarios.

---

### 3. Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics

Prabhakar, A., Ram, R., Chen, Z., Savarese, S., Wang, F., Xiong, C., Wang, H., & Yao, W. (2025). Enterprise deep research: Steerable multi-agent deep research for enterprise analytics. *arXiv preprint arXiv:2510.17797v2*. https://arxiv.org/abs/2510.17797v2

**Summary:** This paper presents Enterprise Deep Research (EDR), a multi-agent system designed to address enterprise-specific challenges in transforming unstructured data into actionable insights. EDR integrates five key components: (1) a Master Planning Agent for adaptive query decomposition, (2) four specialized search agents (General, Academic, GitHub, LinkedIn), (3) an extensible MCP-based tool ecosystem supporting NL2SQL, file analysis, and enterprise workflows, (4) a Visualization Agent for data-driven insights, and (5) a reflection mechanism with optional human-in-the-loop steering. The system outperforms state-of-the-art agentic systems on open-ended benchmarks without human steering.

**Key Contributions:**
- Comprehensive multi-agent architecture for enterprise contexts
- Extensible tool ecosystem with enterprise integration capabilities
- Human-in-the-loop steering mechanism for intent alignment

**Evaluation:** Superior performance on DeepResearch Bench and DeepConsult; validated on internal enterprise datasets. Code and dataset released at https://github.com/SalesforceAIResearch/enterprise-deep-research.

---

### 4. Characterizing Deep Research: A Benchmark and Formal Definition

Java, A., Khandelwal, A., Midigeshi, S., Halfaker, A., Deshpande, A., Goyal, N., Gupta, A., Natarajan, N., & Sharma, A. (2025). Characterizing deep research: A benchmark and formal definition. *arXiv preprint arXiv:2508.04183v1*. https://arxiv.org/abs/2508.04183v1

**Summary:** This foundational work proposes a formal characterization of the deep research task, arguing that its core defining feature is not lengthy report generation but rather the high fan-out over concepts required during search—broad and reasoning-intensive exploration. The authors introduce an intermediate output representation encoding key claims uncovered during search, separating reasoning challenges from surface-level report generation. LiveDRBench comprises 100 challenging tasks over scientific topics and public interest events. Evaluation reveals F1 scores ranging from 0.02 to 0.72 across sub-categories, with OpenAI's model achieving the best overall F1 score of 0.55.

**Key Contributions:**
- Formal definition of deep research based on search fan-out rather than output length
- Intermediate output representation for objective evaluation
- LiveDRBench with 100 challenging, diverse tasks

**Evaluation:** Comprehensive analysis of state-of-the-art DR systems reveals significant performance gaps and motivates future improvements in search mechanisms and grounding capabilities. Benchmark available at https://github.com/microsoft/LiveDRBench.

---

### 5. BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A more fair and transparent evaluation benchmark of deep-research agent. *arXiv preprint arXiv:2508.06600v1*. https://arxiv.org/abs/2508.06600v1

**Summary:** This paper addresses critical limitations in current deep-research evaluation benchmarks, particularly BrowseComp's reliance on black-box live web search APIs, which hinders fairness and transparency. BrowseComp-Plus employs a fixed, carefully curated corpus with human-verified supporting documents and mined challenging negatives, enabling controlled experimentation. The benchmark effectively distinguishes system performance: Search-R1 with BM25 achieves 3.86% accuracy, while GPT-5 achieves 55.9%, and GPT-5 with Qwen3-Embedding-8B retriever reaches 70.1% with fewer search calls.

**Key Contributions:**
- Fixed corpus enabling fair, reproducible comparisons
- Human-verified supporting documents with challenging negatives
- Disentangled analysis of deep research agents and retrieval methods

**Evaluation:** Demonstrates benchmark effectiveness in isolating retriever contributions and evaluating citation accuracy and context engineering.

---

### 6. Open Data Synthesis For Deep Research

Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025). Open data synthesis for deep research. *arXiv preprint arXiv:2509.00375v1*. https://arxiv.org/abs/2509.00375v1

**Summary:** This work formalizes Deep Research tasks with verifiable answers as Hierarchical Constraint Satisfaction Problems (HCSPs), fundamentally different from single-constraint, multi-hop, or flat CSP formulations. The authors introduce InfoSeek, a scalable framework for synthesizing complex Deep Research tasks using a dual-agent system to recursively build Research Trees from large-scale webpages. InfoSeek yields over 50K training examples and enables advanced optimization strategies. Models trained on InfoSeek consistently outperform strong baselines: 3B LLMs optimized with InfoSeek surpass 32B models and lightweight commercial APIs on BrowseComp-Plus.

**Key Contributions:**
- Formal HCSP formulation of Deep Research tasks
- InfoSeek framework for scalable data synthesis
- Demonstration that smaller models can outperform larger ones with proper training data

**Evaluation:** Consistent outperformance of strong baselines; achieves performance comparable to stronger commercial APIs (Gemini2.5-Pro) despite using much smaller models. Code and datasets at https://github.com/VectorSpaceLab/InfoSeek.

---

### 7. DRBench: A Realistic Benchmark for Enterprise Deep Research

Abaskohi, A., Chen, T., Muñoz-Mármol, M., Fox, C., Ramesh, A. V., Marcotte, É., Lù, X. H., Chapados, N., Gella, S., West, P., Carenini, G., Pal, C., Drouin, A., & Laradji, I. H. (2025). DRBench: A realistic benchmark for enterprise deep research. *arXiv preprint arXiv:2510.00172v2*. https://arxiv.org/abs/2510.00172v2

**Summary:** DRBench evaluates AI agents on complex, open-ended deep research tasks in enterprise settings, addressing limitations of prior benchmarks that focus on simple questions or web-only queries. Tasks require identifying supporting facts from both public web and private company knowledge bases, spanning heterogeneous search spaces including productivity software, cloud file systems, emails, chat conversations, and the open web. The benchmark comprises 100 deep research tasks across 10 domains (Sales, Cybersecurity, Compliance, etc.), generated through a synthesis pipeline with human-in-the-loop verification.

**Key Contributions:**
- Realistic enterprise-context tasks requiring multi-source information retrieval
- Heterogeneous search space simulation
- Human-verified task generation pipeline

**Evaluation:** Evaluation across diverse DR agents (GPT, Llama, Qwen) highlights critical paths for advancing enterprise deep research. Code and data at https://github.com/ServiceNow/drbench.

---

### 8. Deep Researcher with Test-Time Diffusion

Han, R., Chen, Y., CuiZhu, Z., Miculicich, L., Sun, G., Bi, Y., Wen, W., Wan, H., Wen, C., Maître, S., Lee, G., Tirumalashetty, V., Xue, E., Zhang, Z., Haykal, S., Gokturk, B., Pfister, T., & Lee, C.-Y. (2025). Deep researcher with test-time diffusion. *arXiv preprint arXiv:2507.16075v1*. https://arxiv.org/abs/2507.16075v1

**Summary:** This paper proposes Test-Time Diffusion Deep Researcher (TTD-DR), conceptualizing research report generation as a diffusion process. TTD-DR initiates with a preliminary draft—an updatable skeleton guiding research direction—then iteratively refines through a "denoising" process dynamically informed by retrieval at each step. A self-evolutionary algorithm enhances each component of the agentic workflow, ensuring high-quality context generation. This draft-centric design improves timeliness and coherence while reducing information loss during iterative search.

**Key Contributions:**
- Novel diffusion-based conceptualization of report generation
- Iterative denoising with dynamic retrieval integration
- Self-evolutionary algorithm for workflow component optimization

**Evaluation:** State-of-the-art results on benchmarks requiring intensive search and multi-hop reasoning, significantly outperforming existing deep research agents.

---

### 9. A Vision for Geo-Temporal Deep Research Systems: Towards Comprehensive, Transparent, and Reproducible Geo-Temporal Information Synthesis

Martins, B., Szymański, P., & Gramacki, P. (2025). A vision for geo-temporal deep research systems: Towards comprehensive, transparent, and reproducible geo-temporal information synthesis. *arXiv preprint arXiv:2506.14345v1*. https://arxiv.org/abs/2506.14345v1

**Summary:** This vision paper identifies a critical gap in current deep research systems: the lack of geo-temporal capabilities essential for context-rich questions in domains like public health, environmental science, and socio-economic analysis. The authors argue for augmenting retrieval and synthesis processes with geo-temporal constraint handling, supported by open, reproducible infrastructures and rigorous evaluation protocols. The paper outlines technical, infrastructural, and evaluative challenges in integrating geo-temporal reasoning into deep research pipelines.

**Key Contributions:**
- Identification of geo-temporal reasoning as a critical unmet need
- Vision framework for next-generation geo-temporally aware systems
- Call for open, reproducible infrastructures and evaluation protocols

**Evaluation:** Conceptual contribution outlining research agenda rather than empirical evaluation.

---

### 10. Evaluation Sheet for Deep Research: A Use Case for Academic Survey Writing

Azime, I. A., Belay, T. D., & Tonja, A. L. (2025). Evaluation sheet for deep research: A use case for academic survey writing. *arXiv preprint arXiv:2510.01283v1*. https://arxiv.org/abs/2510.01283v1

**Summary:** This work introduces an evaluation sheet for assessing Deep Research tool capabilities, using academic survey writing as a use case. The evaluation of OpenAI's Deep Search and Google's Deep Search revealed significant gaps between search engines and standalone Deep Research tools, particularly in representing targeted areas comprehensively. The findings underscore the need for carefully crafted evaluation standards.

**Key Contributions:**
- Structured evaluation sheet for Deep Research capability assessment
- Empirical comparison of commercial Deep Research systems
- Identification of gaps in current system performance

**Evaluation:** Comparative analysis reveals substantial shortcomings in current commercial systems for academic survey generation.

---

## Synthesis and Thematic Analysis

### Architectural Innovation

Three distinct architectural paradigms emerge from the reviewed literature:

1. **Dual-Agent Frameworks:** WebWeaver (Li et al., 2025) and InfoSeek (Xia et al., 2025) both employ dual-agent systems separating planning/research tree construction from evidence synthesis/writing. This separation enables more focused optimization of each component.

2. **Multi-Agent Ecosystems:** EDR (Prabhakar et al., 2025) represents the most complex architecture with five specialized components, reflecting enterprise requirements for domain-specific expertise and tool integration.

3. **Iterative Refinement:** TTD-DR (Han et al., 2025) introduces a diffusion-based approach, conceptualizing report generation as iterative denoising—a fundamentally different paradigm from linear pipeline approaches.

### Benchmark Development

The literature reveals intense focus on benchmark creation, with six papers introducing new evaluation frameworks:

- **PDR-Bench** (Liang et al., 2025): Personalization-focused with 250 user-task queries
- **LiveDRBench** (Java et al., 2025): Formal definition-based with 100 scientific and public interest tasks
- **BrowseComp-Plus** (Chen et al., 2025): Fixed corpus for fair, transparent evaluation
- **InfoSeek** (Xia et al., 2025): Synthetic dataset with 50K+ training examples
- **DRBench** (Abaskohi et al., 2025): Enterprise-context with heterogeneous search spaces
- **Evaluation Sheet** (Azime et al., 2025): Qualitative assessment framework for academic surveys

This proliferation reflects the field's immaturity and lack of consensus on evaluation standards.

### Domain Specialization

Two papers explicitly address domain-specific adaptations:

- **Enterprise Context:** EDR (Prabhakar et al., 2025) and DRBench (Abaskohi et al., 2025) both target enterprise requirements, emphasizing integration with private knowledge bases, specialized search agents, and human-in-the-loop steering.

- **Geo-Temporal Reasoning:** Martins et al. (2025) identify geo-temporal capabilities as a critical gap, particularly relevant for public health, environmental science, and socio-economic analysis.

- **Personalization:** PDR-Bench (Liang et al., 2025) addresses the previously neglected dimension of user personalization in deep research.

### Performance Analysis

Reported performance varies significantly across benchmarks:

- **LiveDRBench:** F1 scores 0.02–0.72; OpenAI leads at 0.55 overall (Java et al., 2025)
- **BrowseComp-Plus:** 3.86% (Search-R1 + BM25) to 70.1% (GPT-5 + Qwen3-Embedding-8B) (Chen et al., 2025)
- **InfoSeek-trained 3B models:** Surpass 32B models and Gemini2.5-Flash; comparable to Gemini2.5-Pro (Xia et al., 2025)

These results indicate substantial headroom for improvement and the critical importance of training data quality over model size alone.

---

## Critical Gaps and Future Directions

### 1. Evaluation Standardization

The field lacks consensus on evaluation protocols. Six different benchmarks introduced in two years suggest fragmentation. Future work should prioritize:
- Standardized metrics enabling cross-benchmark comparison
- Shared test sets for reproducibility
- Clear task taxonomies distinguishing deep research from related capabilities

### 2. Geo-Temporal Reasoning

Martins et al. (2025) identify this as a critical unmet need. Future systems must integrate:
- Geographic constraint handling in retrieval and synthesis
- Temporal reasoning for time-sensitive queries
- Spatiotemporal visualization capabilities

### 3. Personalization

Liang et al. (2025) demonstrate that current systems perform poorly on personalized tasks. Future research should address:
- User modeling and preference learning
- Context-aware adaptation
- Longitudinal personalization across multiple research sessions

### 4. Citation Accuracy and Hallucination Mitigation

Multiple papers (Li et al., 2025; Chen et al., 2025) highlight persistent issues with citation accuracy and hallucination. Promising directions include:
- Evidence-grounded outline generation (WebWeaver)
- Fixed corpus evaluation (BrowseComp-Plus)
- Hierarchical retrieval reducing long-context issues

### 5. Enterprise Integration

EDR (Prabhakar et al., 2025) and DRBench (Abaskohi et al., 2025) reveal enterprise-specific requirements:
- Private knowledge base integration
- Domain-specific tool ecosystems
- Human-in-the-loop steering mechanisms
- Compliance and security considerations

### 6. Training Data Quality

InfoSeek (Xia et al., 2025) demonstrates that training data quality can overcome model size limitations. Future work should explore:
- Automated synthesis of high-quality training data
- Hierarchical constraint satisfaction problem formulations
- Reject sampling and compound reward design

---

## Conclusion

The Deep Research field has advanced rapidly between 2023 and 2025, with significant progress in architectural innovation, benchmark development, and domain specialization. However, performance remains moderate on standardized benchmarks, and critical gaps persist in geo-temporal reasoning, personalization, and citation accuracy. The proliferation of benchmarks reflects both the field's vitality and its immaturity—standardization efforts are urgently needed.

Key takeaways for practitioners:
1. **Architecture matters:** Dual-agent and multi-agent frameworks outperform monolithic approaches
2. **Training data quality exceeds model size:** InfoSeek-trained 3B models outperform 32B models
3. **Domain specialization is critical:** Enterprise and personalized scenarios require tailored approaches
4. **Evaluation rigor is improving:** Fixed corpus benchmarks enable fairer comparisons

The vision articulated by Martins et al. (2025) for geo-temporally aware systems, combined with the formal characterization by Java et al. (2025), provides a roadmap for next-generation Deep Research systems. Continued progress will require sustained attention to evaluation standardization, training data quality, and domain-specific adaptation.

---

## References

Abaskohi, A., Chen, T., Muñoz-Mármol, M., Fox, C., Ramesh, A. V., Marcotte, É., Lù, X. H., Chapados, N., Gella, S., West, P., Carenini, G., Pal, C., Drouin, A., & Laradji, I. H. (2025). DRBench: A realistic benchmark for enterprise deep research. *arXiv preprint arXiv:2510.00172v2*. https://arxiv.org/abs/2510.00172v2

Azime, I. A., Belay, T. D., & Tonja, A. L. (2025). Evaluation sheet for deep research: A use case for academic survey writing. *arXiv preprint arXiv:2510.01283v1*. https://arxiv.org/abs/2510.01283v1

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A more fair and transparent evaluation benchmark of deep-research agent. *arXiv preprint arXiv:2508.06600v1*. https://arxiv.org/abs/2508.06600v1

Han, R., Chen, Y., CuiZhu, Z., Miculicich, L., Sun, G., Bi, Y., Wen, W., Wan, H., Wen, C., Maître, S., Lee, G., Tirumalashetty, V., Xue, E., Zhang, Z., Haykal, S., Gokturk, B., Pfister, T., & Lee, C.-Y. (2025). Deep researcher with test-time diffusion. *arXiv preprint arXiv:2507.16075v1*. https://arxiv.org/abs/2507.16075v1

Java, A., Khandelwal, A., Midigeshi, S., Halfaker, A., Deshpande, A., Goyal, N., Gupta, A., Natarajan, N., & Sharma, A. (2025). Characterizing deep research: A benchmark and formal definition. *arXiv preprint arXiv:2508.04183v1*. https://arxiv.org/abs/2508.04183v1

Li, Z., Guan, X., Zhang, B., Huang, S., Zhou, H., Lai, S., Yan, M., Jiang, Y., Xie, P., Huang, F., Zhang, J., & Zhou, J. (2025). WebWeaver: Structuring web-scale evidence with dynamic outlines for open-ended deep research. *arXiv preprint arXiv:2509.13312v3*. https://arxiv.org/abs/2509.13312v3

Liang, Y., Li, J., Wang, Y., Wang, P., Tian, M., Liu, P., Qiao, S., Fang, R., Zhu, H., Zhang, G., Liu, M., Jiang, Y. E., Zhang, N., & Zhou, W. (2025). Towards personalized deep research: Benchmarks and evaluations. *arXiv preprint arXiv:2509.25106v3*. https://arxiv.org/abs/2509.25106v3

Martins, B., Szymański, P., & Gramacki, P. (2025). A vision for geo-temporal deep research systems: Towards comprehensive, transparent, and reproducible geo-temporal information synthesis. *arXiv preprint arXiv:2506.14345v1*. https://arxiv.org/abs/2506.14345v1

Prabhakar, A., Ram, R., Chen, Z., Savarese, S., Wang, F., Xiong, C., Wang, H., & Yao, W. (2025). Enterprise deep research: Steerable multi-agent deep research for enterprise analytics. *arXiv preprint arXiv:2510.17797v2*. https://arxiv.org/abs/2510.17797v2

Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025). Open data synthesis for deep research. *arXiv preprint arXiv:2509.00375v1*. https://arxiv.org/abs/2509.00375v1

---

**Search Methodology:** This review was conducted using arXiv's scholarly search API with phrase matching for "Deep Research" in category cs.CL, filtered to publications between November 24, 2023, and November 23, 2025. All 10 retrieved papers were included in the final review.
