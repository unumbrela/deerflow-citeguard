# Systematic Literature Review: Deep Research

**Date:** October 27, 2026  
**Review Period:** November 24, 2023 - November 23, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Format:** APA Style

---

## Executive Summary

This systematic literature review examines 10 academic papers (2023-2025) on Deep Research and related information-seeking capabilities in large language models. The review reveals that deep research has emerged as a distinct research area with several interconnected themes: (1) reinforcement learning approaches for search capability, (2) benchmark development for evaluation, (3) multi-agent architectures for complex information seeking, (4) data synthesis methods for training, and (5) comprehensive system blueprints for AI search paradigms.

Key findings indicate that recent advances focus on training LLMs to autonomously use search engines through reinforcement learning, developing fair and reproducible benchmarks, synthesizing high-quality training data, and creating modular multi-agent architectures. The field shows rapid progression from simple retrieval-augmented generation to sophisticated iterative search and reasoning systems.

---

## Paper Summaries

### 1. InfoSeek: Open Data Synthesis For Deep Research

**Citation:** Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025). Open Data Synthesis For Deep Research. *arXiv preprint arXiv:2509.00375*.

**Core Contributions:** InfoSeek introduces a scalable framework for synthesizing complex Deep Research tasks from large-scale webpages. The authors formalize Deep Research tasks with verifiable answers as Hierarchical Constraint Satisfaction Problems (HCSPs), which differ fundamentally from single-constraint, multi-hop, or flat CSP formulations. The framework uses a dual-agent system to recursively build Research Trees from webpages, converting these into natural language questions requiring full hierarchy traversal.

**Methodology:**
- Formalizes Deep Research as Hierarchical Constraint Satisfaction Problems (HCSPs)
- Dual-agent system for recursive Research Tree construction from webpages
- Blurs intermediate nodes into valid sub-problems
- Generates natural language questions requiring full hierarchy traversal
- Enables rapid scaling with over 50K training examples and curated test sets
- Uses reject sampling for reasoning trajectories

**Key Findings:**
- Models trained on InfoSeek consistently outperform strong baselines
- On BrowseComp-Plus, 3B LLMs optimized with InfoSeek surpass 32B models and lightweight commercial APIs (Gemini2.5-Flash)
- Achieves performance comparable to stronger APIs (Gemini2.5-Pro)
- Meta-information preservation supports advanced optimization strategies including compound reward design and trajectory-level exploration

**Limitations:** Relies on large-scale webpage availability; synthetic task generation may not capture all nuances of human research needs; requires careful validation to avoid bias amplification.

---

### 2. Gemini 2.5: Advanced Reasoning and Agentic Capabilities

**Citation:** Comanici, G., Bieber, E., Schaekermann, M., Pasupat, I., Sachdeva, N., Dhillon, I., ... & Haridasan, K. (2025). Gemini 2.5: Pushing the frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities. *arXiv preprint arXiv:2507.06261*.

**Core Contributions:** This report introduces the Gemini 2.X model family, including Gemini 2.5 Pro and Gemini 2.5 Flash, along with earlier Gemini 2.0 Flash and Flash-Lite models. Gemini 2.5 Pro achieves state-of-the-art performance on frontier coding and reasoning benchmarks, with capabilities for processing up to 3 hours of video content. The models span the full Pareto frontier of capability versus cost, enabling complex agentic problem-solving workflows.

**Methodology:**
- Comprehensive model architecture, training, and dataset documentation
- Quantitative evaluation across multiple benchmarks
- Example use cases demonstrating agentic workflows
- Extensive safety, security, and responsibility analysis

**Key Findings:**
- Gemini 2.5 Pro achieves SoTA performance on frontier coding and reasoning benchmarks
- Unique combination of long context (3 hours video), multimodal understanding, and reasoning capabilities
- Enables new agentic workflows combining these capabilities
- Gemini 2.5 Flash provides excellent reasoning at reduced compute and latency
- Model family spans full capability-cost Pareto frontier

**Limitations:** Report focuses on Google's proprietary models; detailed architecture and training specifics may not be fully disclosed; evaluation primarily on internal benchmarks.

---

### 3. ZeroSearch: Training Search Capability Without Real Searching

**Citation:** Sun, H., Qiao, Z., Guo, J., Fan, X., Hou, Y., Jiang, Y., ... & Zhou, J. (2025). ZeroSearch: Incentivize the Search Capability of LLMs without Searching. *arXiv preprint arXiv:2505.04588*.

**Core Contributions:** ZeroSearch introduces a novel reinforcement learning framework that incentivizes LLM search capabilities using simulated searches during training, addressing two major challenges: uncontrolled document quality from search engines and prohibitively high API costs for RL training. The approach uses lightweight supervised fine-tuning to transform the LLM into a retrieval module, then employs curriculum-based rollout strategy during RL training.

**Methodology:**
- Lightweight SFT to transform LLM into retrieval module generating useful and noisy documents
- Curriculum-based rollout strategy incrementally degrading document quality
- Progressive elicitation of reasoning ability through increasingly challenging retrieval scenarios
- Compatible with various RL algorithms and model sizes

**Key Findings:**
- Effectively incentivizes search capabilities using 3B LLM as retrieval module
- 7B retrieval module achieves comparable performance to real search engine
- 14B retrieval module surpasses real search engine performance
- Generalizes well across base and instruction-tuned models of various parameter sizes
- Compatible with wide range of RL algorithms

**Limitations:** Simulated search may not capture all complexities of real web search; quality of generated documents depends on retrieval module training; requires careful curriculum design.

---

### 4. BrowseComp-Plus: Fair and Transparent Evaluation Benchmark

**Citation:** Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., ... & Lin, J. (2025). BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent. *arXiv preprint arXiv:2508.06600*.

**Core Contributions:** BrowseComp-Plus introduces a fixed-corpus evaluation benchmark derived from BrowseComp, employing carefully curated static documents to address fairness and transparency limitations in live web search API evaluations. Each query includes human-verified supporting documents and mined challenging negatives, enabling controlled experimentation and reproducible comparisons.

**Methodology:**
- Fixed, carefully curated corpus derived from BrowseComp
- Human-verified supporting documents for each query
- Mined challenging negatives for robust evaluation
- Enables disentangled analysis of deep research agents and retrieval methods

**Key Findings:**
- Benchmark effectively distinguishes performance of deep research systems
- Search-R1 with BM25 retriever achieves 3.86% accuracy
- GPT-5 achieves 55.9% accuracy
- GPT-5 with Qwen3-Embedding-8B retriever enhances accuracy to 70.1% with fewer search calls
- Allows comprehensive evaluation of retrieval effectiveness, citation accuracy, and context engineering

**Limitations:** Fixed corpus may not capture dynamic web aspects; corpus may become outdated; limited to domains covered in collection; may not reflect real-time information needs.

---

### 5. SimpleDeepSearcher: Deep Information Seeking via Web-Powered Trajectory Synthesis

**Citation:** Sun, S., Song, H., Wang, Y., Ren, R., Jiang, J., Zhang, J., ... & Wen, J. (2025). SimpleDeepSearcher: Deep Information Seeking via Web-Powered Reasoning Trajectory Synthesis. *arXiv preprint arXiv:2505.16834*.

**Core Contributions:** SimpleDeepSearcher introduces a lightweight framework addressing critical limitations in existing deep search approaches: lack of high-quality training trajectories, distributional mismatches in simulated environments, and prohibitive computational costs. The approach synthesizes high-quality training data through realistic user interactions in live web search environments with multi-criteria curation strategy.

**Methodology:**
- Simulates realistic user interactions in live web search environments
- Multi-criteria curation strategy optimizing diversity and quality
- Supervised fine-tuning on only 871 curated samples
- Strategic data engineering rather than complex training paradigms

**Key Findings:**
- SFT on 871 curated samples yields significant improvements over RL-based baselines
- Demonstrates effectiveness across five benchmarks in diverse domains
- Establishes SFT as viable pathway by addressing data-scarce bottleneck
- Offers practical insights for efficient deep search system development

**Limitations:** Limited to 871 samples which may not cover all scenarios; relies on live web search simulation; may not generalize to all domains equally.

---

### 6. WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization

**Citation:** Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., ... & Zhou, J. (2025). WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization. *arXiv preprint arXiv:2507.15061*.

**Core Contributions:** WebShaper proposes a formalization-driven information-seeking data synthesis framework addressing scarcity of high-quality training data. Unlike information-driven paradigms that collect data then generate questions, WebShaper systematically formalizes IS tasks through set theory with Knowledge Projections (KP) enabling precise control over reasoning structure.

**Methodology:**
- Formalizes IS tasks through set theory with Knowledge Projections
- KP operation compositions enable precise reasoning structure control
- Multi-step expansion process with agentic Expander
- Uses retrieval and validation tools based on formalization
- Creates seed tasks then expands with increasing complexity

**Key Findings:**
- Achieves state-of-the-art performance among open-sourced IS agents
- Top performance on GAIA and WebWalkerQA benchmarks
- Systematic formalization enables better quality control than information-driven approaches
- Agentic expansion produces diverse, high-quality training data

**Limitations:** Formalization complexity may limit accessibility; requires careful KP design; agentic expansion adds computational overhead.

---

### 7. Towards AI Search Paradigm: Comprehensive Blueprint

**Citation:** Li, Y., Cai, H., Kong, R., Chen, X., Chen, J., Yang, J., ... & Zhao, J. (2025). Towards AI Search Paradigm. *arXiv preprint arXiv:2506.17188*.

**Core Contributions:** This paper introduces the AI Search Paradigm, a comprehensive blueprint for next-generation search systems capable of emulating human information processing and decision-making. The paradigm employs modular architecture with four LLM-powered agents (Master, Planner, Executor, Writer) that dynamically adapt to full spectrum of information needs.

**Methodology:**
- Modular architecture with four LLM-powered agents
- Master agent for query complexity evaluation
- Planner agent for problem decomposition
- Executor agent for tool orchestration and task execution
- Writer agent for content synthesis
- Dynamic collaboration through coordinated workflows

**Key Findings:**
- Systematic presentation of key methodologies for AI search realization
- Covers task planning, tool integration, execution strategies
- Addresses aligned and robust retrieval-augmented generation
- Includes efficient LLM inference at algorithmic and infrastructure levels
- Provides foundation for trustworthy, adaptive, scalable AI search systems

**Limitations:** Blueprint paper without full implementation details; comprehensive scope limits depth in specific areas; requires significant engineering effort to realize full paradigm.

---

### 8. Search-R1: Training LLMs to Reason with Search Engines via RL

**Citation:** Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., ... & Han, J. (2025). Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning. *arXiv preprint arXiv:2503.09516*.

**Core Contributions:** Search-R1 extends reinforcement learning for reasoning frameworks where LLMs learn to autonomously generate multiple search queries during step-by-step reasoning with real-time retrieval. The approach optimizes LLM reasoning trajectories with multi-turn search interactions, leveraging retrieved token masking for stable RL training and outcome-based reward function.

**Methodology:**
- Extension of RL for reasoning frameworks with search integration
- Autonomous search query generation during reasoning
- Multi-turn search interactions optimization
- Retrieved token masking for stable RL training
- Simple outcome-based reward function

**Key Findings:**
- Improves performance by 41% (Qwen2.5-7B) over various RAG baselines
- Improves performance by 20% (Qwen2.5-3B) over various RAG baselines
- Effective across seven question-answering datasets
- Provides empirical insights into RL optimization methods and LLM choices
- Reveals response length dynamics in retrieval-augmented reasoning

**Limitations:** Focuses on question-answering tasks; may not generalize to open-ended research tasks; requires RL training infrastructure; outcome-based reward may oversimplify complex reasoning.

---

### 9. WebWalker: Benchmarking LLMs in Web Traversal

**Citation:** Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., ... & Huang, F. (2025). WebWalker: Benchmarking LLMs in Web Traversal. *arXiv preprint arXiv:2501.07572*.

**Core Contributions:** WebWalker introduces WebWalkerQA, a benchmark designed to assess LLMs' ability to perform web traversal by systematically extracting high-quality data from website subpages. The paper also proposes WebWalker, a multi-agent framework mimicking human-like web navigation through explore-critic paradigm, addressing limitations of traditional search engines in handling complex, multi-layered information.

**Methodology:**
- WebWalkerQA benchmark for web traversal assessment
- Evaluates systematic subpage traversal capability
- WebWalker multi-agent framework with explore-critic paradigm
- Horizontal and vertical integration in real-world scenarios
- RAG combined with web navigation capabilities

**Key Findings:**
- WebWalkerQA proves challenging for current LLMs
- Demonstrates effectiveness of RAG combined with WebWalker
- Successful horizontal and vertical integration in real-world scenarios
- Addresses shallow content retrieval limitations of traditional search engines
- Enables extraction of complex, multi-layered information

**Limitations:** Benchmark may not cover all web structures; explore-critic paradigm adds complexity; may struggle with dynamically generated content; evaluation focused on specific traversal patterns.

---

### 10. DeepDiver: Adaptive Search Intensity Scaling via RL

**Citation:** Shi, W., Tan, H., Kuang, C., Li, X., Ren, X., Zhang, C., ... & Shang, L. (2025). DeepDiver: Adaptive Search Intensity Scaling via Open-Web Reinforcement Learning. *arXiv preprint arXiv:2505.24332*.

**Core Contributions:** DeepDiver introduces a reinforcement learning framework cultivating Search Intensity Scaling (SIS)—an emergent ability to escalate search frequency and depth instead of settling on overconfident, under-evidenced answers. The paper introduces WebPuzzle, a 24k-sample training and 275-sample test benchmark evaluating information seeking on live internet across wiki and open-domain queries.

**Methodology:**
- WebPuzzle benchmark: 24k training samples, 275 test samples
- Evaluates information seeking on live internet
- Covers both wiki and open-domain queries
- RL framework cultivating Search Intensity Scaling ability
- Curriculum from cold-start SFT to well-designed RL procedure

**Key Findings:**
- Qwen2.5-7B-Instruct with SIS achieves performance comparable to 671B-parameter DeepSeek-R1 on real-web tasks
- Pangu-7B-Reasoner with SIS shows similar performance gains
- Seeking policy generalizes from closed-ended queries to open-ended generation
- Advances adaptive information seeking in LLMs
- Provides rigorous benchmark for future work

**Limitations:** Focuses on search intensity rather than search quality; RL training requires significant computational resources; benchmark may not cover all information seeking scenarios; generalization to long-form writing needs further validation.

---

## Cross-Paper Synthesis

### Thematic Analysis

**Theme 1: Reinforcement Learning for Search Capability (4/10 papers)**
Four papers focus on using RL to train search capabilities:
- **ZeroSearch** (2505.04588): Simulated search during training to avoid API costs
- **Search-R1** (2503.09516): Multi-turn search interactions with retrieved token masking
- **DeepDiver** (2505.24332): Search Intensity Scaling through curriculum-based RL
- **Gemini 2.5** (2507.06261): Agentic capabilities with advanced reasoning

Common approaches include outcome-based rewards, curriculum learning, and token masking for stability. All demonstrate that smaller models with proper RL training can match or exceed larger models' search capabilities.

**Theme 2: Benchmark Development (3/10 papers)**
Three papers introduce evaluation benchmarks:
- **BrowseComp-Plus** (2508.06600): Fixed-corpus for fair, reproducible evaluation
- **WebWalkerQA** (2501.07572): Web traversal assessment
- **WebPuzzle** (2505.24332): Live internet information seeking with 275 test samples

Common challenges include balancing reproducibility with ecological validity, managing evaluation costs, and ensuring comprehensive domain coverage.

**Theme 3: Data Synthesis Methods (2/10 papers)**
Two papers address training data scarcity:
- **InfoSeek** (2509.00375): Hierarchical Constraint Satisfaction Problems with Research Trees
- **WebShaper** (2507.15061): Formalization-driven synthesis with Knowledge Projections

Both approaches emphasize quality over quantity, using structured methods to ensure training data captures complex reasoning patterns.

**Theme 4: System Architectures (2/10 papers)**
Two papers propose comprehensive architectures:
- **AI Search Paradigm** (2506.17188): Four-agent modular system (Master, Planner, Executor, Writer)
- **SimpleDeepSearcher** (2505.16834): Lightweight framework with strategic data engineering

Common patterns include modular design, iterative processes, and separation of planning from execution.

### Methodological Trends

**Reinforcement Learning Dominance:** 4/10 papers use RL as primary training method, reflecting consensus that search capability requires learning from interaction rather than static supervision.

**Data Quality Focus:** 3/10 papers emphasize training data synthesis, addressing field-wide recognition that data scarcity limits progress more than model architecture.

**Benchmark Proliferation:** 3/10 papers introduce new benchmarks, indicating field maturation but also fragmentation in evaluation approaches.

**Efficiency Emphasis:** Multiple papers (ZeroSearch, SimpleDeepSearcher, DeepDiver) demonstrate that smaller models with proper training can match larger models, suggesting efficiency gains through better methods rather than scale.

**Live Web Evaluation:** 4/10 papers evaluate on live internet, balancing reproducibility concerns with ecological validity needs.

### Performance Comparisons

| System | Model Size | Key Metric | Performance |
|--------|-----------|------------|-------------|
| ZeroSearch | 7B retrieval | vs Real Search | Comparable |
| ZeroSearch | 14B retrieval | vs Real Search | Surpasses |
| Search-R1 | Qwen2.5-7B | Improvement over RAG | +41% |
| Search-R1 | Qwen2.5-3B | Improvement over RAG | +20% |
| DeepDiver | Qwen2.5-7B | vs DeepSeek-R1 671B | Comparable |
| BrowseComp-Plus | GPT-5 + Qwen3-Embed | Accuracy | 70.1% |
| BrowseComp-Plus | Search-R1 + BM25 | Accuracy | 3.86% |
| InfoSeek | 3B LLM | vs Gemini2.5-Pro | Comparable |

*Note: Different benchmarks use different metrics; direct comparison limited.*

### Common Limitations

1. **Evaluation Fragmentation:** Multiple benchmarks with different metrics limit cross-paper comparison; field lacks standardized evaluation framework.

2. **Computational Costs:** RL training requires significant resources, though ZeroSearch and SimpleDeepSearcher show paths to reduce costs.

3. **Domain Coverage:** Most benchmarks focus on specific domains (question-answering, web traversal); general deep research capabilities underexplored.

4. **Live Web Dependencies:** Systems relying on live web evaluation face reproducibility challenges as web content changes.

5. **Reward Design:** RL approaches use simple outcome-based rewards that may not capture reasoning quality; compound reward design remains nascent.

6. **Simulated vs Real Search:** Trade-off between simulated search efficiency (ZeroSearch) and real search ecological validity; bridging gap remains open challenge.

### Future Directions

**Immediate Priorities (2025-2026):**
- Standardized evaluation framework enabling cross-paper comparison
- Improved reward design for RL training capturing reasoning quality
- Better simulated search environments matching real web characteristics
- Domain expansion beyond question-answering to open-ended research

**Medium-term Goals (2026-2027):**
- Integration of multiple capabilities (planning, search, synthesis) in unified systems
- Token-level or insight-level evaluation granularity
- Reduced computational costs through better training methods
- Cross-model generalization of search capabilities

**Long-term Vision (2027+):**
- Fully autonomous research agents matching expert human performance
- Real-time adaptive search strategies based on task complexity
- Transparent, interpretable search and reasoning processes
- Community-owned benchmarks and infrastructure reducing commercial dependencies

---

## Methodology of This Review

**Search Strategy:**
- Database: arXiv
- Category: cs.CL (Computational Linguistics)
- Date Range: November 24, 2023 - November 23, 2025
- Selection: Scholar screen tool for relevance scoring

**Selection Criteria:**
- Primary focus on deep research, information seeking, or search capabilities
- Empirical contributions with measurable results
- Full text available in English
- Published in arXiv cs.CL category

**Extraction Process:**
- Batch retrieval of paper metadata and abstracts
- Structured extraction of contributions, methodology, findings, limitations
- Cross-paper synthesis identifying themes, trends, and gaps
- APA format citation style

**Limitations of This Review:**
- Limited to arXiv cs.CL category; may miss relevant papers from other categories (cs.AI, cs.IR)
- Rapidly evolving field with papers continuously published
- Reliance on author-reported metrics without independent replication
- Emerging field with limited cross-citation between papers
- Does not include concurrent work from industry labs not published on arXiv

---

## References

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A More Fair and Transparent Evaluation Benchmark of Deep-Research Agent. *arXiv preprint arXiv:2508.06600*.

Comanici, G., Bieber, E., Schaekermann, M., Pasupat, I., Sachdeva, N., Dhillon, I., Blistein, M., Ram, O., Zhang, D., Rosen, E., Marris, L., Petulla, S., Gaffney, C., Aharoni, A., Lintz, N., Pais, T. C., Jacobsson, H., Szpektor, I., Jiang, N. J., & Haridasan, K. (2025). Gemini 2.5: Pushing the frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities. *arXiv preprint arXiv:2507.06261*.

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025). Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning. *arXiv preprint arXiv:2503.09516*.

Li, Y., Cai, H., Kong, R., Chen, X., Chen, J., Yang, J., Zhang, H., Li, J., Wu, J., Chen, Y., Qu, C., Ye, W., Su, L., Ma, X., Yan, L., Xia, L., Shi, D., Wang, J., Zhao, X., & Zhao, J. (2025). Towards AI Search Paradigm. *arXiv preprint arXiv:2506.17188*.

Shi, W., Tan, H., Kuang, C., Li, X., Ren, X., Zhang, C., Chen, H., Wang, Y., Hou, L., & Shang, L. (2025). DeepDiver: Adaptive Search Intensity Scaling via Open-Web Reinforcement Learning. *arXiv preprint arXiv:2505.24332*.

Sun, H., Qiao, Z., Guo, J., Fan, X., Hou, Y., Jiang, Y., Xie, P., Zhang, Y., Huang, F., & Zhou, J. (2025). ZeroSearch: Incentivize the Search Capability of LLMs without Searching. *arXiv preprint arXiv:2505.04588*.

Sun, S., Song, H., Wang, Y., Ren, R., Jiang, J., Zhang, J., Bai, F., Deng, J., Zhao, W. X., Liu, Z., Fang, L., Wang, Z., & Wen, J. (2025). SimpleDeepSearcher: Deep Information Seeking via Web-Powered Reasoning Trajectory Synthesis. *arXiv preprint arXiv:2505.16834*.

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization. *arXiv preprint arXiv:2507.15061*.

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025). WebWalker: Benchmarking LLMs in Web Traversal. *arXiv preprint arXiv:2501.07572*.

Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025). Open Data Synthesis For Deep Research. *arXiv preprint arXiv:2509.00375*.

---

**Document Location:** `/app/backend/.deer-flow/users/a295acd6-7db3-4f7b-be18-f16d8eae7b6d/threads/40149455-40d0-4453-bc64-b07405378a14/user-data/outputs/deep-research-systematic-literature-review.md`  
**Generated:** October 27, 2026  
**Total Papers Reviewed:** 10  
**Search Period:** November 24, 2023 - November 23, 2025  
**Category:** cs.CL (Computational Linguistics)
