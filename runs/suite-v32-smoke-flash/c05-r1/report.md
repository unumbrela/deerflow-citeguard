# Systematic Literature Review: Deep Research in Language Models

**Review Date:** October 26, 2026  
**Search Period:** November 24, 2023 – November 23, 2025  
**Category:** cs.CL (Computation and Language)  
**Total Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in **Deep Research**—a paradigm where AI agents autonomously conduct complex investigations by decomposing questions into sub-problems, coordinating multi-step reasoning, and synthesizing evidence from diverse sources. The review covers 10 peer-reviewed papers published between November 2023 and November 2025 in the computer science computation and language category (cs.CL).

### Key Findings

1. **Benchmark Development**: Multiple benchmarks have emerged to evaluate deep research capabilities, including Personalized Deep Research Bench (PDR-Bench), Enterprise Deep Research Benchmark (DRBench), BrowseComp-Plus, LiveDRBench, and WebWeaver's evaluation suite [[citation:Personalized Deep Research](https://arxiv.org/abs/2509.25106v3)][[citation:Enterprise Deep Research](https://arxiv.org/abs/2510.17797v2)][[citation:BrowseComp Plus](https://arxiv.org/abs/2508.06600v1)][[citation:Characterizing Deep Research](https://arxiv.org/abs/2508.04183v1)].

2. **Multi-Agent Architectures**: Leading systems employ multi-agent frameworks with specialized roles including planning agents, search agents, writing agents, and visualization agents for enterprise-grade applications [[citation:Enterprise Deep Research](https://arxiv.org/abs/2510.17797v2)][[citation:WebWeaver](https://arxiv.org/abs/2509.13312v3)].

3. **Evaluation Challenges**: Current benchmarks face limitations around fairness, reproducibility, transparency, and domain specificity, particularly in enterprise and personalized contexts [[citation:BrowseComp Plus](https://arxiv.org/abs/2508.06600v1)][[citation:Characterizing Deep Research](https://arxiv.org/abs/2508.04183v1)].

4. **Methodological Innovations**: Novel approaches include diffusion-based report generation, hierarchical constraint satisfaction modeling, test-time optimization, and human-in-the-loop steering mechanisms [[citation:Test-Time Diffusion](https://arxiv.org/abs/2507.16075v1)][[citation:Open Data Synthesis](https://arxiv.org/abs/2509.00375v1)].

---

## Introduction

Deep research represents a significant evolution in AI-assisted information synthesis, moving beyond simple factual queries toward complex, open-ended investigation tasks that require iterative search planning, cross-source reasoning, and coherent report generation. This systematic review synthesizes findings from 10 papers published over a two-year period, examining theoretical foundations, benchmark methodologies, architectural innovations, and evaluation frameworks.

The field has rapidly matured since its conceptualization, with recent work establishing formal definitions, creating diverse benchmark suites, and demonstrating state-of-the-art performance on increasingly challenging tasks. However, significant gaps remain in standardization, reproducibility, and domain-specific applicability.

---

## Methodology

### Search Strategy

A systematic search was conducted using the arXiv database with the following parameters:
- **Query**: "deep research"
- **Primary Category**: cs.CL (Computation and Language)
- **Date Range**: November 24, 2023 – November 23, 2025
- **Selection Criteria**: Peer-reviewed papers directly addressing deep research methodologies, benchmarks, or evaluations

### Inclusion Criteria

Papers were included if they:
1. Were published in the cs.CL primary category
2. Addressed deep research as a core contribution
3. Provided empirical evaluations, benchmarks, or methodological frameworks
4. Were written in English

### Exclusion Criteria

Papers were excluded if they:
1. Focused solely on related but distinct topics (e.g., general question answering, summarization without iterative search)
2. Lacked empirical validation or benchmark contributions
3. Were primarily survey or position papers without novel methodology

---

## Thematic Analysis

### Theme 1: Formal Definitions and Task Characterization

#### Characterizing Deep Research: A Benchmark and Formal Definition

Java et al. (2025) propose the first formal characterization of the deep research task, arguing that its defining feature is not lengthy output but rather **"high fan-out over concepts required during the search process"**—broad and reasoning-intensive exploration [[citation:Characterizing Deep Research](https://arxiv.org/abs/2508.04183v1)].

**Key Contributions:**
- Introduced intermediate output representation encoding key claims uncovered during search
- Separated reasoning challenge from surface-level report generation
- Created LiveDRBench with 100 challenging tasks across scientific topics and public interest events

**Performance Results:**
- OpenAI's model achieved highest F1 score of 0.55
- Overall performance ranged from 0.02 to 0.72 across sub-categories
- Analysis revealed distribution patterns in referenced sources, branching, and backtracking events

**Implications:** This work establishes that deep research should be evaluated based on search breadth and reasoning quality rather than report length alone, fundamentally reframing how success metrics are defined.

### Theme 2: Benchmark Development

#### BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark

Chen et al. (2025) address critical limitations in existing benchmarks like BrowseComp, which rely on black-box live web search APIs, creating issues with fairness and reproducibility [[citation:BrowseComp Plus](https://arxiv.org/abs/2508.06600v1)].

**Innovations:**
- Fixed, curated corpus enabling controlled experimentation
- Human-verified supporting documents and mined challenging negatives
- Disentangled analysis of deep research agents and retrieval methods

**Results:**
- Search-R1 + BM25: 3.86% accuracy
- GPT-5 + BM25: 55.9% accuracy
- GPT-5 + Qwen3-Embedding-8B: 70.1% accuracy

#### DRBench: A Realistic Benchmark for Enterprise Deep Research

Abaskohi et al. (2025) introduced DRBench, specifically designed for enterprise deep research scenarios [[citation:DRBench](https://arxiv.org/abs/2510.00172v2)].

**Unique Features:**
- Multi-step queries requiring both public web and private company knowledge base access
- Heterogeneous search space: productivity software, cloud file systems, emails, chat conversations
- 100 tasks across 10 domains: Sales, Cybersecurity, Compliance, etc.
- Human-in-the-loop verification pipeline

**Significance:** Addresses the gap between academic benchmarks and real-world enterprise needs, providing more realistic evaluation scenarios.

#### PDR-Bench: Personalized Deep Research Benchmark

Liang et al. (2025) created the first benchmark for evaluating personalization in deep research agents [[citation:Personalized Deep Research](https://arxiv.org/abs/2509.25106v3)].

**Components:**
- 50 diverse research tasks across 10 domains
- 25 authentic user profiles combining persona attributes with dynamic contexts
- 250 total user-task queries
- PQR Evaluation Framework measuring Personalization Alignment, Content Quality, and Factual Reliability

**Impact:** Enables evaluation of how well deep research systems adapt to individual user preferences and contexts, a critical capability for practical deployment.

### Theme 3: Multi-Agent Architectures

#### WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines

Li et al. (2025) present a dual-agent framework emulating human research processes [[citation:WebWeaver](https://arxiv.org/abs/2509.13312v3)].

**Architecture:**
1. **Planner Agent**: Iteratively interleaves evidence acquisition with outline optimization
   - Produces citation-grounded outline linked to memory bank
   - Adaptive planning throughout research process
   
2. **Writer Agent**: Hierarchical retrieval and writing
   - Section-by-section composition
   - Targeted evidence retrieval via citations
   - Mitigates long-context issues and citation hallucinations

**Performance:** Establishes state-of-the-art across major benchmarks including DeepResearch Bench, DeepConsult, and DeepResearchGym.

#### Enterprise Deep Research: Steerable Multi-Agent System

Prabhakar et al. (2025) developed Enterprise Deep Research (EDR), a comprehensive multi-agent system for enterprise analytics [[citation:Enterprise Deep Research](https://arxiv.org/abs/2510.17797v2)].

**Five Core Components:**
1. Master Planning Agent for adaptive query decomposition
2. Four specialized search agents (General, Academic, GitHub, LinkedIn)
3. MCP-based tool ecosystem supporting NL2SQL, file analysis, enterprise workflows
4. Visualization Agent for data-driven insights
5. Reflection mechanism with optional human-in-the-loop steering

**Capabilities:**
- Automated report generation
- Real-time streaming
- Seamless enterprise deployment
- Outperforms SOTA agentic systems without human steering

### Theme 4: Methodological Innovations

#### Test-Time Diffusion Deep Researcher (TTD-DR)

Han et al. (2025) introduce a diffusion-based approach to research report generation inspired by iterative human research cycles [[citation:Test-Time Diffusion](https://arxiv.org/abs/2507.16075v1)].

**Core Concept:**
- Research report generation as diffusion process
- Preliminary draft serves as updatable skeleton
- Iterative refinement through "denoising" informed by retrieval mechanism
- Self-evolutionary algorithm optimizes each workflow component

**Advantages:**
- More timely and coherent report writing
- Reduced information loss during iterative search
- State-of-the-art results on intensive search and multi-hop reasoning benchmarks

#### Open Data Synthesis: InfoSeek Framework

Xia et al. (2025) formalize deep research tasks with verifiable answers as Hierarchical Constraint Satisfaction Problems (HCSPs) [[citation:Open Data Synthesis](https://arxiv.org/abs/2509.00375v1)].

**Framework Components:**
- Dual-agent system recursively builds Research Tree from large-scale webpages
- Blurs intermediate nodes into valid sub-problems
- Converts trees into natural language questions requiring full hierarchy traversal
- Generates over 50K training examples

**Results:**
- 3B LLMs trained on InfoSeek surpass larger 32B models
- Competitive with lightweight commercial APIs
- Performance comparable to stronger APIs like Gemini2.5-Pro

**Significance:** Demonstrates scalable data synthesis can overcome limitations of existing benchmarks and enable effective training despite smaller model sizes.

### Theme 5: Domain-Specific Extensions

#### Geo-Temporal Deep Research Systems

Martins et al. (2025) identify the need for geo-temporal capabilities in deep research systems for context-rich questions involving geographic and temporal constraints [[citation:Geo-Temporal Vision](https://arxiv.org/abs/2506.14345v1)].

**Target Domains:**
- Public health
- Environmental science
- Socio-economic analysis

**Proposed Enhancements:**
- Augmented retrieval and synthesis for geo-temporal constraints
- Open and reproducible infrastructures
- Rigorous evaluation protocols

**Vision:** Next-generation systems must handle location-aware and time-sensitive queries, expanding deep research applicability to critical real-world domains.

#### Academic Survey Writing Evaluation

Azime et al. (2025) introduce an evaluation sheet specifically for academic survey writing tasks [[citation:Academic Survey Evaluation](https://arxiv.org/abs/2510.01283v1)].

**Findings:**
- Significant gap between traditional search engines and standalone Deep Research tools
- Current systems show shortcomings in representing targeted research areas
- Need for carefully crafted evaluation standards

**Contribution:** Provides domain-specific evaluation framework for scholarly research assistance applications.

---

## Comparative Analysis

### Benchmark Performance Comparison

| Benchmark | Tasks | Focus Area | Top Performer | Score |
|-----------|-------|------------|---------------|-------|
| LiveDRBench | 100 | Scientific/Public Interest | OpenAI | F1: 0.55 |
| BrowseComp-Plus | Variable | Controlled Corpus | GPT-5 + Embedding | 70.1% |
| PDR-Bench | 250 | Personalized | Various | PQR Framework |
| DRBench | 100 | Enterprise | Various | Domain-dependent |
| DeepResearch Bench | Variable | General | WebWeaver | SOTA |

### Architectural Patterns

**Common Multi-Agent Structures:**
1. **Planning → Execution → Verification** (most common)
2. **Specialized Search Agents** (general, academic, technical, social)
3. **Writer → Citation Manager** pairing
4. **Reflection/Steering Mechanisms** for human intervention

**Emerging Best Practices:**
- Iterative outline development before full report generation
- Memory banks for evidence accumulation and retrieval
- Citation-grounding at multiple stages
- Domain-specific agent specialization

---

## Critical Gaps and Future Directions

### Identified Limitations

1. **Standardization Gap**: Lack of unified evaluation standards across benchmarks
2. **Reproducibility Issues**: Black-box API dependencies hinder fair comparisons
3. **Domain Coverage**: Most benchmarks focus on general knowledge; enterprise and specialized domains underrepresented
4. **Scalability Concerns**: Training data synthesis frameworks exist but limited adoption
5. **Human Alignment**: Personalization and preference handling remain nascent capabilities

### Emerging Research Directions

1. **Interoperable Benchmark Standards**: Need for cross-benchmark compatibility and shared metrics
2. **Hybrid Retrieval Systems**: Combining web search, private databases, and structured knowledge bases
3. **Explainable Reasoning**: Better traceability of multi-hop inference chains
4. **Continual Learning**: Systems that improve through interaction without catastrophic forgetting
5. **Ethical Considerations**: Bias detection, privacy preservation, and transparent sourcing

### Technical Challenges

- **Context Window Management**: Balancing depth vs. breadth in information gathering
- **Citation Accuracy**: Reducing hallucination in source attribution
- **Temporal Awareness**: Handling evolving information and version control
- **Cross-Modal Integration**: Combining text, tables, figures, and multimedia sources

---

## Conclusion

The past two years have witnessed remarkable progress in deep research capabilities, with 10 pivotal papers establishing the field's theoretical foundations, benchmark infrastructure, and architectural paradigms. Key achievements include:

1. **Formal Characterization**: Clear definition separating deep research from related reasoning tasks through high fan-out concept exploration [[citation:Characterizing Deep Research](https://arxiv.org/abs/2508.04183v1)]

2. **Benchmark Ecosystem**: Diverse evaluation suites covering general, enterprise, personalized, and domain-specific scenarios [[citation:DRBench](https://arxiv.org/abs/2510.00172v2)][[citation:Personalized Deep Research](https://arxiv.org/abs/2509.25106v3)][[citation:BrowseComp Plus](https://arxiv.org/abs/2508.06600v1)]

3. **Architectural Maturity**: Multi-agent frameworks achieving state-of-the-art performance with human-centric design principles [[citation:WebWeaver](https://arxiv.org/abs/2509.13312v3)][[citation:Enterprise Deep Research](https://arxiv.org/abs/2510.17797v2)]

4. **Methodological Innovation**: Novel approaches from diffusion-based generation to hierarchical constraint satisfaction modeling [[citation:Test-Time Diffusion](https://arxiv.org/abs/2507.16075v1)][[citation:Open Data Synthesis](https://arxiv.org/abs/2509.00375v1)]

Despite these advances, significant challenges remain in standardization, reproducibility, and domain adaptation. Future work must address interoperability between benchmarks, develop robust evaluation protocols independent of proprietary APIs, and expand coverage to specialized enterprise and scientific domains.

The trajectory suggests deep research will become increasingly integral to knowledge work, academic research, and decision-making processes. Success depends on continued collaboration between academia, industry, and end-users to establish best practices, share evaluation data, and align technical capabilities with practical needs.

---

## References

Azime, I. A., Belay, T. D., & Tonja, A. L. (2025). Evaluation Sheet for Deep Research: A Use Case for Academic Survey Writing. *arXiv preprint arXiv:2510.01283*. https://arxiv.org/abs/2510.01283v1

Abaskohi, A., Chen, T., Muñoz-Mármol, M., Fox, C., Ramesh, A. V., Marcotte, É., ... & Laradji, I. H. (2025). DRBench: A Realistic Benchmark for Enterprise Deep Research. *arXiv preprint arXiv:2510.00172*. https://arxiv.org/abs/2510.00172v2

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., ... & Lin, J. (2025). BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent. *arXiv preprint arXiv:2508.06600*. https://arxiv.org/abs/2508.06600v1

Han, R., Chen, Y., CuiZhu, Z., Miculicich, L., Sun, G., Bi, Y., ... & Lee, C.-Y. (2025). Deep Researcher with Test-Time Diffusion. *arXiv preprint arXiv:2507.16075*. https://arxiv.org/abs/2507.16075v1

Java, A., Khandelwal, A., Midigeshi, S., Halfaker, A., Deshpande, A., Goyal, N., ... & Sharma, A. (2025). Characterizing Deep Research: A Benchmark and Formal Definition. *arXiv preprint arXiv:2508.04183*. https://arxiv.org/abs/2508.04183v1

Liang, Y., Li, J., Wang, Y., Wang, P., Tian, M., Liu, P., ... & Zhou, W. (2025). Towards Personalized Deep Research: Benchmarks and Evaluations. *arXiv preprint arXiv:2509.25106*. https://arxiv.org/abs/2509.25106v3

Li, Z., Guan, X., Zhang, B., Huang, S., Zhou, H., Lai, S., ... & Zhou, J. (2025). WebWeaver: Structuring Web-Scale Evidence with Dynamic Outlines for Open-Ended Deep Research. *arXiv preprint arXiv:2509.13312*. https://arxiv.org/abs/2509.13312v3

Martins, B., Szymański, P., & Gramacki, P. (2025). A Vision for Geo-Temporal Deep Research Systems: Towards Comprehensive, Transparent, and Reproducible Geo-Temporal Information Synthesis. *arXiv preprint arXiv:2506.14345*. https://arxiv.org/abs/2506.14345v1

Prabhakar, A., Ram, R., Chen, Z., Savarese, S., Wang, F., Xiong, C., ... & Yao, W. (2025). Enterprise Deep Research: Steerable Multi-Agent Deep Research for Enterprise Analytics. *arXiv preprint arXiv:2510.17797*. https://arxiv.org/abs/2510.17797v2

Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025). Open Data Synthesis For Deep Research. *arXiv preprint arXiv:2509.00375*. https://arxiv.org/abs/2509.00375v1

---

*Systematic Literature Review completed on October 26, 2026*
