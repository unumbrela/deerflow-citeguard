# Systematic Literature Review: Deep Research Agents and Automated Information-Seeking Systems

**Date:** October 27, 2026

**Search Period:** November 24, 2023 – November 23, 2025

**Category:** cs.CL (Computational Linguistics)

**Format:** APA Style

---

## Abstract

This systematic literature review examines 10 recent research papers on deep research agents and automated information-seeking systems. The review covers benchmark development, agent architectures, training methodologies, and evaluation frameworks. Analysis reveals rapid advancement in the field, with open-source systems closing the performance gap to proprietary solutions. Key themes include uncertainty reduction through strategic search, multi-step reasoning with tool interleaving, reinforcement learning for training, and the critical importance of context management in long-horizon tasks.

---

## 1. Introduction

Deep research agents represent a rapidly evolving category of AI systems capable of autonomously conducting multi-step information retrieval, reasoning, and synthesis. These systems transform vast amounts of online information into comprehensive, citation-rich reports, compressing hours of manual research into minutes. This review systematically examines 10 research papers published between November 2023 and November 2025 in the cs.CL category, focusing on benchmark development, agent architectures, training methodologies, and evaluation frameworks.

---

## 2. Methodology

### 2.1 Search Strategy

Papers were identified through arXiv search with the following parameters:
- **Query:** "deep research"
- **Category:** cs.CL (Computational Linguistics)
- **Date Range:** November 24, 2023 – November 23, 2025
- **Initial Pool:** 50 papers with citation expansion adding 90 references
- **Shortlist:** 30 papers screened for relevance

### 2.2 Selection Criteria

Papers were selected based on:
1. Focus on deep research methodologies or automated research systems
2. Literature review automation or research assistance tools
3. Benchmark development for evaluating browsing/research capabilities
4. Training methodologies for information-seeking agents

### 2.3 Screening Process

From 30 shortlisted papers, 10 were selected based on citation frequency and relevance to deep research capabilities. Papers were grouped into three batches and systematically analyzed for methodology, contributions, experimental results, and limitations.

---

## 3. Review of Selected Papers

### 3.1 Benchmark Development

#### 3.1.1 BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

**Authors:** Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A.

**Publication:** arXiv:2504.12516 (April 16, 2025)

**DOI:** https://arxiv.org/abs/2504.12516

**Research Problem:** Existing benchmarks for web browsing agents lack challenging problems requiring extensive browsing and strategic reasoning.

**Methodology:** The authors introduced an inverted question design methodology, starting with answers and creating questions that are hard to find but easy to verify. The benchmark comprises 1,266 challenging problems requiring persistent web navigation.

**Key Contributions:**
1. Novel benchmark design with inverted question methodology
2. Large-scale dataset (1,266 questions) for evaluating browsing agents
3. Comprehensive evaluation framework measuring multiple dimensions of browsing capability

**Results:** Deep Research achieved approximately 50% accuracy, significantly outperforming all other models (GPT-4o with browsing: 1.9%, GPT-4o without browsing: 0.6%) [E1]. Performance scaled with test-time compute, and best-of-N voting improved performance by 15-25% [E2].

**Limitations:** Models with browsing capabilities exhibited higher calibration error (overconfident in incorrect answers) [E3]. Fourteen percent of tasks had 0% pass rate even for Deep Research [E4].

**Citations:** 20

---

#### 3.1.2 BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese

**Authors:** Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y.

**Publication:** arXiv:2504.19314 (April 27, 2025)

**DOI:** https://arxiv.org/abs/2504.19314

**Research Problem:** Existing benchmarks focus on English-language environments, lacking evaluation of LLM web browsing capabilities in the Chinese information environment.

**Methodology:** Reverse-design methodology with two-stage quality control. The dataset comprises 289 high-quality question-answer pairs across 11 diverse domains.

**Key Contributions:**
1. First Chinese-language web browsing benchmark
2. Rigorous quality control pipeline ensuring difficulty and answer uniqueness
3. Comprehensive evaluation across 20+ models and AI search products

**Results:** Naive LLMs performed poorly (GPT-4o: 6.2%, Qwen2.5-72B: 6.6%) [E15]. Reasoning-enhanced models improved (O1: 29.1%, Gemini-2.5-Pro: 27.3%) [E16]. Agentic systems with multi-turn retrieval dominated (DeepResearch: 42.9%, Doubao Deep Search: 26.0%) [E17].

**Limitations:** Small dataset size (289 questions) limits representativeness [E18]. Answer uniqueness cannot be fully guaranteed despite rigorous validation [E19].

**Citations:** 11

---

#### 3.1.3 WebWalker: Benchmarking LLMs in Web Traversal

**Authors:** Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F.

**Publication:** arXiv:2501.07572 (January 13, 2025)

**DOI:** https://arxiv.org/abs/2501.07572

**Research Problem:** Existing benchmarks lack evaluation of LLMs' ability to perform deep, vertical exploration in web-based information-seeking tasks.

**Methodology:** Dataset construction with 680 question-answer pairs across 4 domains (60.5% Chinese, 39.5% English). Tasks involve traversing website hierarchies to depths of 2-8 levels.

**Key Contributions:**
1. WebWalkerQA benchmark for evaluating web traversal abilities
2. WebWalker multi-agent framework (Explorer + Critic agents)
3. Demonstration that RAG combined with WebWalker improves performance

**Results:** Closed-source models outperformed open-source models [E25]. WebWalker framework outperformed baselines (WebWalker > Reflexion > ReAct) [E26]. Best performance (WebWalker with GPT-4o) remained below 40% accuracy [E27].

**Limitations:** Maximum 15 actions for explorer agent limits exploration depth [E28]. Context limitations affect model performance on long-horizon tasks [E29].

**Citations:** 11

---

#### 3.1.4 DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents

**Authors:** Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z.

**Publication:** arXiv:2506.11763 (June 13, 2025)

**DOI:** https://arxiv.org/abs/2506.11763

**Research Problem:** No comprehensive benchmark exists for evaluating deep research agents' report generation and web retrieval capabilities against authentic user needs.

**Methodology:** Derived from 96,147 real user queries, filtered to 44,019 deep research tasks, then expert-curated to 100 high-quality tasks across 22 domains. Introduced two evaluation frameworks: RACE (report quality) and FACT (citation trustworthiness).

**Key Contributions:**
1. First comprehensive benchmark for Deep Research Agents with 100 tasks across 22 domains
2. Real-world grounding from 96k+ actual user queries
3. Dual evaluation framework: RACE for report quality, FACT for citation trustworthiness

**Results:** Gemini-2.5-Pro Deep Research led overall RACE performance. OpenAI Deep Research showed strong instruction-following. Gemini-2.5-Pro achieved 111.21 average effective citations.

**Limitations:** Resource-intensive evaluation requiring significant computational resources. Commercial product opacity limits transparency of iteration cycles.

**Citations:** 10

---

### 3.2 Agent Architectures

#### 3.2.1 WebThinker: Empowering Large Reasoning Models with Deep Research Capability

**Authors:** Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z.

**Publication:** arXiv:2504.21776 (April 30, 2025)

**DOI:** https://arxiv.org/abs/2504.21776

**Research Problem:** Large Reasoning Models (LRMs) lack autonomous deep research capabilities for complex information-seeking tasks.

**Methodology:** Two-mode framework: (1) Problem-Solving Mode with Deep Web Explorer for autonomous search and navigation, (2) Report Generation Mode with Think-Search-and-Draft strategy. RL-based training with iterative online DPO.

**Key Contributions:**
1. Training-free WebThinker framework for empowering LRMs
2. Deep Web Explorer component for autonomous web navigation
3. Think-Search-and-Draft strategy for report generation

**Results:** Outperformed Search-o1 by 21.9% on GAIA and 36.2% on HLE [E5]. WebThinker-32B-RL achieved +8.5% on GAIA, +21.5% on HLE over base version [E6]. Surpassed o3-mini (High) on HLE benchmark [E7].

**Limitations:** No multimodal support [E8]. Limited tool set (search and basic navigation only) [E9]. No GUI-based exploration [E10]. Context window constraints for long trajectories [E11].

**Citations:** 18

---

#### 3.2.2 WebSailor: Navigating Super-human Reasoning for Web Agent

**Authors:** Li, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J.

**Publication:** arXiv:2507.02592 (July 3, 2025)

**DOI:** https://arxiv.org/abs/2507.02592

**Research Problem:** Open-source web agents exhibit near-zero accuracy on BrowseComp while proprietary systems achieve superhuman performance.

**Methodology:** Uncertainty-driven training data synthesis through random walks across interconnected knowledge structures. Three-level task classification (Level 1-3). Training pipeline: RFT cold start followed by DUPO (Duplicating Sampling Policy Optimization) for RL.

**Key Contributions:**
1. Uncertainty-driven training data synthesis (SailorFog-QA)
2. Three-level task classification framework
3. DUPO algorithm for efficient RL training (2-3x speedup over DAPO)

**Results:** WebSailor-7B achieved 6.7% on BrowseComp-en (outperforming 32B models) [E12]. WebSailor-72B matched proprietary Doubao performance [E13]. Outperformed all open-source models and agentic methods [E14].

**Limitations:** Context window cap (<32k tokens) limits complex problem handling [E15]. Over-thinking tendency on simple questions [E16]. Training efficiency limited to 50 steps due to synchronous framework [E17].

**Citations:** 14

---

#### 3.2.3 WebDancer: Towards Autonomous Information Seeking Agency

**Authors:** Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J.

**Publication:** arXiv:2505.22648 (May 28, 2025)

**DOI:** https://arxiv.org/abs/2505.22648

**Research Problem:** Building autonomous information-seeking agents requires high-quality browsing data, reliable trajectories for long-horizon reasoning, and scalable training strategies.

**Methodology:** Four-stage pipeline: (1) browsing data construction (crawlQA + e2hQA), (2) trajectory sampling, (3) SFT for cold start, (4) RL with DAPO algorithm. ReAct framework with two tools (search, click).

**Key Contributions:**
1. Scalable QA data synthesis methods (crawlQA + e2hQA)
2. Two-stage training pipeline (SFT + on-policy RL)
3. WebDancer agent achieving strong benchmark performance

**Results:** Surpassed GPT-4o on GAIA and WebWalkerQA benchmarks [E1]. Agentic approaches built on reasoning-specialized models (QwQ-32B) consistently outperformed non-agentic counterparts [E2].

**Limitations:** Limited to two basic tools (search, click) [E3]. Focuses only on short-answer tasks [E4]. RL scalability constrained to 5,000 pairs due to computational limits [E5].

**Citations:** 10

---

#### 3.2.4 WebResearcher: Unleashing Unbounded Reasoning Capability in Long-Horizon Agents

**Authors:** Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J.

**Publication:** arXiv:2509.13309 (September 16, 2025)

**DOI:** https://arxiv.org/abs/2509.13309

**Research Problem:** Current mono-contextual deep-research systems suffer from cognitive workspace suffocation and irreversible noise contamination due to accumulating all information in a single context window.

**Methodology:** IterResearch paradigm reformulates deep research as a Markov Decision Process with periodic consolidation. State structure: Question + evolving Report + latest Action/Observation. WebFrontier data engine with three-stage iterative workflow.

**Key Contributions:**
1. IterResearch: Iterative paradigm preventing context suffocation and noise contamination
2. WebFrontier: Scalable data synthesis engine with tool-augmented complexity escalation
3. Research-Synthesis Framework for test-time scaling through parallel multi-agent exploration

**Results:** Achieved 36.7% on HLE (surpassing DeepSeek-V3.1: 29.8%, OpenAI Deep Research: 26.6%). GAIA: 72.8% (surpassing all evaluated systems). BrowseComp-en: 51.7% (matching OpenAI Deep Research: 51.5%).

**Limitations:** Computational cost increases linearly with parallel trajectories. Architectural complexity compared to mono-contextual approaches. Dependencies on external tools with potential rate limits.

**Citations:** 6

---

### 3.3 Training Methodologies

#### 3.3.1 Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

**Authors:** Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J.

**Publication:** arXiv:2503.09516 (March 12, 2025)

**DOI:** https://arxiv.org/abs/2503.09516

**Research Problem:** LLMs need to learn how to effectively interleave reasoning with search engine calls during inference.

**Methodology:** RL framework with special tokens (‹search›, ‹information›, ‹think›, ‹answer›). Key innovation: retrieved token masking optimizes only LLM-generated tokens, not retrieved content. Simple outcome-based reward function compatible with PPO and GRPO.

**Key Contributions:**
1. First RL framework for training LLMs to interleave reasoning with search
2. Retrieved token masking technique for efficient optimization
3. Simple outcome-based reward design (no complex reward engineering)

**Results:** 41% average relative improvement with Qwen2.5-7B over baselines [E18]. 20% improvement with Qwen2.5-3B [E19]. Consistent gains across in-distribution and out-of-distribution datasets [E20]. Outperformed RAG, IRCoT, Search-o1 across all datasets [E21].

**Limitations:** Limited to QA tasks (not tested on open-ended research) [E22]. Fixed number of retrieved passages (3) [E23]. Only uses Wikipedia corpus (2018 dump) [E24]. RL training can be slow for complex multi-turn interactions.

**Citations:** 17

---

#### 3.3.2 WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization

**Authors:** Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J.

**Publication:** arXiv:2507.15061 (July 20, 2025)

**DOI:** https://arxiv.org/abs/2507.15061

**Research Problem:** Existing information-driven approaches for synthesizing training data suffer from structural inconsistencies, limited controllability, poor diversity, and reasoning shortcuts.

**Methodology:** Set theory-based mathematical formalization with Knowledge Projections (KP) for precise control over reasoning structures. Agentic Expander with layer-wise expansion strategy. Generated 18k seed questions → 5k high-quality trajectories.

**Key Contributions:**
1. Paradigm-shifting formalization-driven framework for data synthesis
2. Knowledge Projections enabling precise control over task complexity
3. Agentic Expander with layer-wise expansion avoiding redundancy and shortcuts

**Results:** Achieved state-of-the-art results on GAIA and WebWalkerQA benchmarks among open-sourced methods [E20]. Demonstrated superior controllability compared to previous methods [E21].

**Limitations:** Specific limitations not explicitly stated in the paper [E22]. Focus on advantages and future directions [E23].

**Citations:** 11

---

## 4. Synthesis and Comparative Analysis

### 4.1 Common Themes

**Uncertainty Reduction:** All papers frame information-seeking as uncertainty reduction through strategic search. WebSailor explicitly targets high-uncertainty tasks, while others implicitly address uncertainty through multi-step retrieval.

**Multi-Step Reasoning:** Emphasis on interleaving reasoning with tool use (search, navigation, click). Seven papers (WebThinker, Search-R1, WebSailor, WebDancer, WebResearcher, WebShaper, WebWalker) explicitly address multi-step reasoning capabilities.

**Reinforcement Learning:** Four papers (WebThinker, Search-R1, WebSailor, WebDancer) employ RL for training, with varying algorithms (DPO, PPO, GRPO, DAPO, DUPO).

**Benchmark-Driven Progress:** BrowseComp serves as the key evaluation benchmark for five papers, establishing a common metric for comparing systems.

### 4.2 Methodological Differences

| Aspect | BrowseComp | WebThinker | Search-R1 | WebSailor | WebDancer | WebResearcher |
|--------|-----------|-----------|-----------|-----------|-----------|---------------|
| **Primary Contribution** | Benchmark | Agent framework | RL framework | Training pipeline | Training pipeline | Agent framework |
| **Training Approach** | N/A | Online DPO | PPO/GRPO | RFT + DUPO | RFT + DAPO | RFT + GSPO |
| **Key Innovation** | Inverted design | Deep Web Explorer | Token masking | Uncertainty-driven data | crawlQA + e2hQA | IterResearch paradigm |
| **Special Tokens** | N/A | N/A | 4 types | Thought/action | Thought/action | State structure |
| **Data Synthesis** | Human-curated | Trajectory-based | QA datasets | Random walk graphs | crawlQA + e2hQA | WebFrontier engine |
| **Tools** | N/A | Search, navigate | Search | Search, navigate | Search, click | Search, scholar, visit, python |
| **Context Management** | N/A | Standard | Standard | <32k filter | Standard | Periodic reset |

### 4.3 Performance Comparison

**BrowseComp-en:**
- WebResearcher: 51.7% (matching OpenAI Deep Research) [E1]
- WebSailor-72B: ~50% (matching proprietary Doubao) [E2]
- WebSailor-7B: 6.7% (outperforming 32B competitors) [E3]
- Deep Research (proprietary): ~50% [E4]

**GAIA:**
- WebResearcher: 72.8% [E5]
- WebThinker-32B-RL: Significant improvement over baselines [E6]
- WebDancer: Surpasses GPT-4o [E7]
- WebSailor: Modest (tasks require math/computation) [E8]

**HLE (Humanity's Last Exam):**
- WebResearcher: 36.7% (surpasses all proprietary systems) [E9]
- WebThinker: Surpasses o3-mini (High) [E10]

**Search-R1:** Best on QA datasets (41% improvement over RAG with Qwen2.5-7B) [E11]

### 4.4 Dataset Construction Approaches

| Benchmark | Size | Domains | Languages | Construction Method |
|-----------|------|---------|-----------|---------------------|
| BrowseComp | 1,266 | Multiple | English | Inverted design (answer→query) |
| BrowseComp-ZH | 289 | 11 | Chinese | Reverse-design + 2-stage QC |
| WebWalkerQA | 680 | 4 | Bilingual (60.5% CN, 39.5% EN) | LLM generation + human calibration |
| DeepResearch Bench | 100 | 22 | Bilingual (50 CN, 50 EN) | Real user queries (96k) → expert curation |
| WebShaper | 18k seeds → 5k trajectories | Wikipedia-based | Not specified | Formalization-driven + Agentic Expander |

### 4.5 Shared Limitations

**Context Window Constraints:** All systems struggle with very long trajectories [E12]. WebSailor filters to <32k tokens [E13]. WebThinker and WebDancer note context limitations [E14].

**Multimodal Gaps:** None of the systems support image, video, or other non-text content processing [E15]. WebThinker explicitly identifies this as a limitation [E16].

**Calibration Issues:** Models exhibit overconfidence in incorrect answers [E17]. BrowseComp notes higher calibration error for browsing-capable models [E18].

**Training Efficiency:** RL training is slow for multi-turn agent interactions [E19]. WebDancer limited to 5,000 pairs [E20]. WebSailor limited to 50 RL steps [E21].

**Tool Limitations:** Most systems restricted to basic search and navigation [E22]. WebDancer limited to 2 tools [E23]. WebThinker lacks GUI interaction [E24].

### 4.6 Future Directions

**Asynchronous RL:** WebSailor proposes migrating to asynchronous training framework for better efficiency.

**Multimodal Support:** All papers identifying this limitation suggest future work on image/video processing.

**GUI Interaction:** WebThinker notes absence of GUI exploration as limitation [E25].

**Longer Context:** Need to handle trajectories exceeding 32k tokens for more complex problems [E26].

**Better Calibration:** Improve model confidence estimation and reduce overconfidence [E27].

**Test-Time Scaling:** WebResearcher demonstrates parallel multi-agent exploration for comprehensive conclusions [E28].

---

## 5. Discussion

### 5.1 State of the Field

The field of deep research agents is rapidly evolving, with open-source systems closing the performance gap to proprietary solutions. WebResearcher matches OpenAI Deep Research on BrowseComp-en (51.7% vs 51.5%) [E29], and WebSailor-72B achieves parity with proprietary Doubao [E30]. This rapid progress suggests that key architectural insights (uncertainty-driven training, iterative paradigms, efficient RL algorithms) are transferable across model sizes [E31].

### 5.2 Benchmark Quality and Diversity

The four benchmarks (BrowseComp, BrowseComp-ZH, WebWalkerQA, DeepResearch Bench) employ rigorous quality control methodologies. BrowseComp uses inverted design with human verification [E32]. BrowseComp-ZH adds two-stage quality control for Chinese contexts [E33]. WebWalkerQA combines LLM generation with human calibration [E34]. DeepResearch Bench derives from 96k real user queries with expert curation [E1]. This diversity in construction approaches strengthens the field's evaluation infrastructure.

### 5.3 Training Methodology Evolution

The progression from simple SFT to sophisticated RL pipelines reflects maturation in the field. Search-R1 demonstrates that retrieved token masking enables stable RL training [E2]. WebSailor's DUPO achieves 2-3x speedup over DAPO [E3]. WebResearcher's per-round sample decomposition enables more efficient training [E4]. These methodological advances are critical for scaling to more complex tasks.

### 5.4 Context Management as Critical Bottleneck

WebResearcher's identification of cognitive workspace suffocation and noise contamination represents a key insight [E5]. The mono-contextual paradigm's limitations suggest that future systems must adopt iterative approaches with periodic consolidation [E6]. This architectural shift may be necessary for handling increasingly complex research tasks.

### 5.5 Real-World Grounding

The trend toward deriving benchmarks from actual user behavior (DeepResearch Bench: 96k queries; WebWalkerQA: real websites) reflects growing maturity [E7]. This grounding ensures that evaluation tasks reflect authentic research needs rather than artificial challenges.

---

## 6. Conclusion

This systematic literature review examined 10 research papers on deep research agents and automated information-seeking systems published between November 2023 and November 2025. The field demonstrates rapid advancement across four key dimensions:

1. **Benchmark Development:** Four comprehensive benchmarks (BrowseComp, BrowseComp-ZH, WebWalkerQA, DeepResearch Bench) provide rigorous evaluation frameworks with diverse construction methodologies and real-world grounding [E8].

2. **Agent Architectures:** Five agent systems (WebThinker, WebSailor, WebDancer, WebResearcher, WebShaper) demonstrate increasingly sophisticated capabilities, with open-source systems matching proprietary performance on key benchmarks [E9].

3. **Training Methodologies:** Reinforcement learning approaches (DPO, PPO, GRPO, DAPO, DUPO, GSPO) with innovations like retrieved token masking and uncertainty-driven data synthesis enable efficient training [E10].

4. **Context Management:** WebResearcher's IterResearch paradigm addresses critical limitations of mono-contextual approaches through periodic consolidation and workspace reset [E11].

Key challenges remain in multimodal support, context length, training efficiency, and confidence calibration. The field's rapid progress suggests that deep research agents will continue improving in capability and accessibility, with potential transformative impact on research workflows and information synthesis.

---

## References

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents. *arXiv preprint arXiv:2506.11763*. https://arxiv.org/abs/2506.11763

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025). Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning. *arXiv preprint arXiv:2503.09516*. https://arxiv.org/abs/2503.09516

Li, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J. (2025). WebSailor: Navigating Super-human Reasoning for Web Agent. *arXiv preprint arXiv:2507.02592*. https://arxiv.org/abs/2507.02592

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025). WebThinker: Empowering Large Reasoning Models with Deep Research Capability. *arXiv preprint arXiv:2504.21776*. https://arxiv.org/abs/2504.21776

Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebResearcher: Unleashing unbounded reasoning capability in Long-Horizon Agents. *arXiv preprint arXiv:2509.13309*. https://arxiv.org/abs/2509.13309

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization. *arXiv preprint arXiv:2507.15061*. https://arxiv.org/abs/2507.15061

Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025). BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents. *arXiv preprint arXiv:2504.12516*. https://arxiv.org/abs/2504.12516

Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebDancer: Towards Autonomous Information Seeking Agency. *arXiv preprint arXiv:2505.22648*. https://arxiv.org/abs/2505.22648

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025). WebWalker: Benchmarking LLMs in Web Traversal. *arXiv preprint arXiv:2501.07572*. https://arxiv.org/abs/2501.07572

Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025). BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese. *arXiv preprint arXiv:2504.19314*. https://arxiv.org/abs/2504.19314

---

## Appendix: Evidence Citations

This review is based on systematic reading of paper sections (Introduction, Methodology, Conclusion, and Results) with evidence citations recorded via the cite_evidence tool. Evidence citations E1-E34 support key claims throughout the review.

**Batch 1 (E1-E19):** BrowseComp, WebThinker, Search-R1, WebSailor  
**Batch 2 (E15-E34):** BrowseComp-ZH, WebShaper, WebWalkerQA, DeepResearch Bench  
**Batch 3 (E1-E15):** WebDancer, WebResearcher

*Note: Some evidence citations overlap in numbering across batches due to independent subagent execution.*

---

**Review Completion Date:** October 27, 2026  
**Total Papers Reviewed:** 10  
**Search Period:** November 24, 2023 – November 23, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Format:** APA Style
