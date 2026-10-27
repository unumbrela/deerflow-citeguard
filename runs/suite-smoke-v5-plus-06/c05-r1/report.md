# Systematic Literature Review: Deep Research

**Date:** October 27, 2026

**Search Period:** November 24, 2023 – November 23, 2025

**Category:** cs.CL (Computational Linguistics)

**Format:** APA

---

## Executive Summary

This systematic literature review examines ten recent papers (2023-2025) on Deep Research, focusing on AI-powered autonomous research agents, web browsing capabilities, and information-seeking systems. The reviewed literature reveals rapid advancements in deep research agents that can autonomously orchestrate multi-step web exploration, targeted retrieval, and higher-order synthesis to transform vast online information into analyst-grade, citation-rich reports [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763). Key themes include benchmark development, training methodologies, reinforcement learning approaches, and evaluation frameworks for assessing deep research capabilities.

---

## 1. Introduction

Deep Research Agents represent a prominent category of LLM-based agents that autonomously orchestrate multistep web exploration, targeted retrieval, and higher-order synthesis [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763). These systems compress hours of manual desk research into minutes, transforming vast amounts of online information into comprehensive, citation-rich reports. Recent proprietary systems like OpenAI's Deep Research and ChatGPT Deep Research have demonstrated strong information-seeking capabilities through end-to-end reinforcement learning training [citation:Wu et al., 2025a](https://arxiv.org/abs/2505.22648).

This review synthesizes findings from 10 papers published between November 2023 and November 2025 in the cs.CL category, examining benchmarking approaches, training methodologies, agent architectures, and evaluation frameworks for deep research systems.

---

## 2. Methodology

### 2.1 Search Strategy

A systematic search was conducted on arXiv for papers matching the query "Deep Research" with the following criteria:
- **Category:** cs.CL (Computational Linguistics)
- **Publication Date:** November 24, 2023 – November 23, 2025
- **Selection:** Top 10 papers ranked by centrality to the topic and citation frequency

### 2.2 Selection Criteria

Papers were included if they:
1. Focused on deep research methodologies or automated research systems
2. Addressed AI-assisted research or comprehensive research frameworks
3. Presented benchmarks, training methods, or evaluation frameworks for research agents
4. Were published in the cs.CL category within the specified date range

### 2.3 Data Extraction

For each paper, key findings were extracted from abstracts, introductions, methodology sections, experiments, and conclusions. Evidence was recorded with exact quotes and paragraph identifiers for verification.

---

## 3. Review of Selected Papers

### 3.1 Benchmarking Deep Research Capabilities

#### 3.1.1 BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents

**Wei et al. (2025)** [citation:Wei et al., 2025](https://arxiv.org/abs/2504.12516)

Wei et al. (2025) introduced BrowseComp, a benchmark comprising 1,266 challenging problems that require browsing a large number of websites to solve [citation:Wei et al., 2025](https://arxiv.org/abs/2504.12516) [E11]. The benchmark is designed to measure the ability of agents to persistently navigate the internet in search of hard-to-find, entangled information. Key findings include:

- OpenAI's Deep Research significantly outperforms all other models, solving around half of the problems [citation:Wei et al., 2025](https://arxiv.org/abs/2504.12516) [E12]
- BrowseComp performance scales smoothly with increased test-time compute (browsing effort) [citation:Wei et al., 2025](https://arxiv.org/abs/2504.12516) [E13]
- Models with browsing capabilities exhibit higher calibration error, suggesting that access to web tools may increase the model's confidence in incorrect answers [citation:Wei et al., 2025](https://arxiv.org/abs/2504.12516) [E14]

The benchmark can be seen as analogous to programming competitions for coding agents—simple and useful despite being an incomplete representation of true user query distribution [citation:Wei et al., 2025](https://arxiv.org/abs/2504.12516).

#### 3.1.2 BrowseComp-ZH: Benchmarking Web Browsing Ability in Chinese

**Zhou et al. (2025)** [citation:Zhou et al., 2025](https://arxiv.org/abs/2504.19314)

Zhou et al. (2025) addressed the gap in non-English benchmarks by introducing BrowseComp-ZH, a high-difficulty benchmark for evaluating LLM agents on the Chinese web [citation:Zhou et al., 2025](https://arxiv.org/abs/2504.19314). The benchmark consists of 289 multi-hop questions spanning 11 diverse domains, with each question reverse-engineered from a short, objective, and easily verifiable answer.

Key contributions:
- OpenAI's DeepResearch achieved the highest accuracy at 42.9%, demonstrating that AI search products with multi-turn retrieval outperform standalone LLMs [citation:Zhou et al., 2025](https://arxiv.org/abs/2504.19314) [E27]
- BrowseComp-ZH reveals that even advanced models struggle with Chinese web navigation, highlighting the need for specialized training and evaluation [citation:Zhou et al., 2025](https://arxiv.org/abs/2504.19314) [E28]
- A two-stage quality control protocol ensures answer uniqueness and high question difficulty through human-in-the-loop verification [citation:Zhou et al., 2025](https://arxiv.org/abs/2504.19314) [E29]
- Benchmark results show AI search products with retrieval mechanisms significantly outperform closed-source APIs and open-source models [citation:Zhou et al., 2025](https://arxiv.org/abs/2504.19314) [E30]

The results demonstrate that success on BrowseComp-ZH demands not only effective retrieval strategies but also sophisticated reasoning and information reconciliation—capabilities that current models still struggle to master [citation:Zhou et al., 2025](https://arxiv.org/abs/2504.19314).

#### 3.1.3 WebWalker: Benchmarking LLMs in Web Traversal

**Wu et al. (2025b)** [citation:Wu et al., 2025b](https://arxiv.org/abs/2501.07572)

Wu et al. (2025b) introduced WebWalkerQA, a benchmark designed to assess the ability of LLMs to perform web traversal by systematically navigating website subpages to extract high-quality data [citation:Wu et al., 2025b](https://arxiv.org/abs/2501.07572). The benchmark addresses limitations of traditional search engines that may retrieve shallow content, limiting the ability of LLMs to handle complex, multi-layered information.

Key findings:
- WebWalkerQA is highly challenging, with even the best WebWalker implementation using GPT-4o achieving less than 40% accuracy [citation:Wu et al., 2025b](https://arxiv.org/abs/2501.07572) [E34]
- The benchmark includes both multi-source and single-source QA types to simulate different human information-seeking behaviors [citation:Wu et al., 2025b](https://arxiv.org/abs/2501.07572) [E35]
- WebWalker is a multi-agent framework with explorer and critic agents that mimics human-like web navigation through an explore-critic paradigm [citation:Wu et al., 2025b](https://arxiv.org/abs/2501.07572) [E36]

The benchmark demonstrates the effectiveness of RAG combined with WebWalker through horizontal and vertical integration in real-world scenarios [citation:Wu et al., 2025b](https://arxiv.org/abs/2501.07572) [E43].

#### 3.1.4 DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents

**Du et al. (2025)** [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763)

Du et al. (2025) presented DeepResearch Bench, the first specialized benchmark for Deep Research Agents, consisting of 100 PhD-level research tasks across 22 distinct domains crafted by domain experts [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763). The benchmark addresses the absence of comprehensive evaluation frameworks for systematically assessing deep research agent capabilities.

Key innovations:
- **RACE Framework:** A reference-based method with adaptive criteria and dynamic weighting to assess the quality of generated research reports [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763) [E37]
- **FACT Framework:** Evaluates information retrieval and collection capabilities by assessing effective citation count and overall citation accuracy [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763) [E38]
- Evaluation results show Gemini-2.5-Pro Deep Research leads in overall RACE scores while OpenAI Deep Research excels in Instruction-Following [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763) [E39]

Tasks are proposed by PhD-level experts or senior practitioners with 5+ years experience and undergo rigorous manual screening for quality and complexity [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763) [E40]. The benchmark addresses the absence of comprehensive evaluation frameworks for systematically assessing deep research agent capabilities [citation:Du et al., 2025](https://arxiv.org/abs/2506.11763) [E41].

### 3.2 Training Methodologies for Deep Research Agents

#### 3.2.1 WebThinker: Empowering Large Reasoning Models with Deep Research Capability

**Li et al. (2025b)** [citation:Li et al., 2025b](https://arxiv.org/abs/2504.21776)

Li et al. (2025b) proposed WebThinker, a deep research agent that empowers large reasoning models (LRMs) to autonomously search the web, navigate among web pages, and draft reports during the reasoning process [citation:Li et al., 2025b](https://arxiv.org/abs/2504.21776). The approach addresses the limitation that LRMs' reliance on static internal knowledge limits their performance on complex, knowledge-intensive tasks.

Key components:
- **Deep Web Explorer Module:** Enables LRMs to dynamically search, navigate via interactive elements (like links or buttons), and extract relevant information from the web [citation:Li et al., 2025b](https://arxiv.org/abs/2504.21776) [E15]
- **Autonomous Think-Search-and-Draft Strategy:** Allows the model to seamlessly interleave reasoning, information gathering, and report writing in real time [citation:Li et al., 2025b](https://arxiv.org/abs/2504.21776) [E16]
- **RL-based Training Strategy:** Uses iterative online Direct Preference Optimization (DPO) to optimize end-to-end task performance [citation:Li et al., 2025b](https://arxiv.org/abs/2504.21776) [E17]

The RL-trained WebThinker-32B-RL achieves state-of-the-art performance among 32B models on all benchmarks, substantially improving over its Base version (e.g., +8.5% on GAIA and +21.5% on HLE) [citation:Li et al., 2025b](https://arxiv.org/abs/2504.21776) [E18].

#### 3.2.2 Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning

**Jin et al. (2025)** [citation:Jin et al., 2025](https://arxiv.org/abs/2503.09516)

Jin et al. (2025) introduced Search-R1, an extension of reinforcement learning for reasoning frameworks where the LLM learns to autonomously generate multiple search queries during step-by-step reasoning with real-time retrieval [citation:Jin et al., 2025](https://arxiv.org/abs/2503.09516). The approach addresses the suboptimal performance of prompting advanced LLMs to use search engines during inference.

Key innovations:
- **Retrieved Token Masking:** Ensures stable RL training by computing the policy gradient objective only over LLM-generated tokens, excluding retrieved content from optimization [citation:Jin et al., 2025](https://arxiv.org/abs/2503.09516) [E19]
- **Outcome-based Reward Function:** Employs a simple reward design for training retrieval-augmented reasoning [citation:Jin et al., 2025](https://arxiv.org/abs/2503.09516) [E20]
- **Multi-turn Search Interactions:** Optimizes LLM reasoning trajectories with multiple search interactions [citation:Jin et al., 2025](https://arxiv.org/abs/2503.09516) [E21]

Experiments on seven question-answering datasets show Search-R1 achieves 24% and 20% average relative improvement with Qwen2.5-7B and Qwen2.5-3B, respectively, over various RAG baselines [citation:Jin et al., 2025](https://arxiv.org/abs/2503.09516) [E26].

#### 3.2.3 WebSailor: Navigating Super-human Reasoning for Web Agent

**Li et al. (2025a)** [citation:Li et al., 2025a](https://arxiv.org/abs/2507.02592)

Li et al. (2025a) introduced WebSailor, a complete post-training methodology designed to instill superhuman reasoning capabilities for systematically reducing extreme uncertainty when navigating vast information landscapes [citation:Li et al., 2025a](https://arxiv.org/abs/2507.02592). The work focuses on Level 3 tasks characterized by both high uncertainty and high difficulty in uncertainty reduction.

Key contributions:
- **Information Obfuscation:** Deliberately introduces ambiguity through structured sampling to increase task difficulty and initial uncertainty [citation:Li et al., 2025a](https://arxiv.org/abs/2507.02592) [E22]
- **DUPO Algorithm:** Duplicating Sampling Policy Optimization achieves approximately 2-3 times speedup compared to DAPO's dynamic sampling [citation:Li et al., 2025a](https://arxiv.org/abs/2507.02592) [E23]
- **RFT Cold Start:** Uses reinforcement fine-tuning with cold start initialization for efficient agentic RL training [citation:Li et al., 2025a](https://arxiv.org/abs/2507.02592) [E24]

On BrowseComp-zh, WebSailor-72B achieves performance on par with Doubao, a top-tier proprietary agent, significantly outperforming all open-source agents in complex information-seeking tasks [citation:Li et al., 2025a](https://arxiv.org/abs/2507.02592) [E25].

#### 3.2.4 WebDancer: Towards Autonomous Information Seeking Agency

**Wu et al. (2025a)** [citation:Wu et al., 2025a](https://arxiv.org/abs/2505.22648)

Wu et al. (2025a) presented a cohesive paradigm for building end-to-end agentic information seeking agents from a data-centric and training-stage perspective [citation:Wu et al., 2025a](https://arxiv.org/abs/2505.22648). The approach consists of four key stages: browsing data construction, trajectories sampling, supervised fine-tuning for effective cold start, and reinforcement learning for enhanced generalization.

Key components:
- **Two Dataset Synthesis Methods:** crawlQA from crawled web pages and e2hQA for easy-to-hard question transformation to create complex, multi-step QA pairs [citation:Wu et al., 2025a](https://arxiv.org/abs/2505.22648) [E1]
- **Two-stage Training Pipeline:** SFT for cold start followed by RL for generalization [citation:Wu et al., 2025a](https://arxiv.org/abs/2505.22648) [E2]
- **DAPO Algorithm:** Uses Decoupled Clip and Dynamic Sampling Policy Optimization in the RL stage to optimize the policy model's Thought-Action-Observation interleaving capability [citation:Wu et al., 2025a](https://arxiv.org/abs/2505.22648) [E3]

Empirical evaluations on GAIA and WebWalkerQA demonstrate that WebDancer achieves performance that surpasses GPT-4o in best-case scenarios, highlighting the efficacy of the training paradigm [citation:Wu et al., 2025a](https://arxiv.org/abs/2505.22648) [E4]. The work establishes a foundation for building autonomous information seeking agents through systematic data construction and training methodologies [citation:Wu et al., 2025a](https://arxiv.org/abs/2505.22648) [E5].

#### 3.2.5 WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization

**Tao et al. (2025)** [citation:Tao et al., 2025](https://arxiv.org/abs/2507.15061)

Tao et al. (2025) proposed WebShaper, a formalization-driven information-seeking data synthesis framework that systematically formalizes IS tasks through set theory [citation:Tao et al., 2025](https://arxiv.org/abs/2507.15061). The approach addresses inconsistencies between information structure and reasoning structure in existing information-driven paradigms.

Key innovations:
- **Knowledge Projections (KP):** A set theory-based formalization that serves as the basic unit for controlling reasoning structure in information-seeking tasks [citation:Tao et al., 2025](https://arxiv.org/abs/2507.15061) [E31]
- **Agentic Expander:** Employs Layer-wise Expansion Strategy to systematically expand formalized tasks while minimizing redundancy and preventing reasoning shortcuts [citation:Tao et al., 2025](https://arxiv.org/abs/2507.15061) [E32]
- **Multi-step Expansion Process:** Uses retrieval and validation tools based on formalization to construct datasets [citation:Tao et al., 2025](https://arxiv.org/abs/2507.15061) [E33]

WebShaper achieves state-of-the-art performance among open-source methods on GAIA and WebWalkerQA benchmarks, scoring over 60 points and approaching OpenAI's DeepResearch system performance [citation:Tao et al., 2025](https://arxiv.org/abs/2507.15061) [E42].

#### 3.2.6 WebResearcher: Unleashing Unbounded Reasoning Capability

**Qiao et al. (2025)** [citation:Qiao et al., 2025](https://arxiv.org/abs/2509.13309)

Qiao et al. (2025) introduced WebResearcher, a novel framework addressing fundamental limitations of mono-contextual approaches in deep research agents [citation:Qiao et al., 2025](https://arxiv.org/abs/2509.13309). The work identifies that the mono-contextual paradigm with linear accumulation fundamentally constrains deep-research agent potential.

Key contributions:
- **IterResearch Paradigm:** Reformulates deep research as a Markov Decision Process with periodic state reconstruction, operating through discrete rounds with focused workspaces to overcome context suffocation and noise contamination [citation:Qiao et al., 2025](https://arxiv.org/abs/2509.13309) [E6]
- **Context Suffocation Paradox:** Mono-contextual architecture creates a paradox where gathering more information makes agents increasingly ineffective at processing it due to irreversible noise contamination [citation:Qiao et al., 2025](https://arxiv.org/abs/2509.13309) [E7]
- **WebFrontier Data Engine:** Uses a three-stage workflow—seed data generation, iterative complexity escalation, and quality control—to generate high-quality training data [citation:Qiao et al., 2025](https://arxiv.org/abs/2509.13309) [E8]

Extensive experiments across 6 challenging benchmarks demonstrate that WebResearcher achieves state-of-the-art performance, even surpassing frontier proprietary systems [citation:Qiao et al., 2025](https://arxiv.org/abs/2509.13309) [E9]. The paradigm naturally scales through parallel thinking, enabling concurrent multi-agent exploration for more comprehensive conclusions [citation:Qiao et al., 2025](https://arxiv.org/abs/2509.13309) [E10].

---

## 4. Synthesis and Discussion

### 4.1 Benchmarking Trends

The reviewed literature reveals a strong emphasis on benchmark development for evaluating deep research capabilities. Four major benchmarks emerged:

1. **BrowseComp** (Wei et al., 2025) focuses on challenging web browsing questions requiring persistent navigation
2. **BrowseComp-ZH** (Zhou et al., 2025) extends benchmarking to the Chinese web ecosystem
3. **WebWalkerQA** (Wu et al., 2025b) evaluates systematic web traversal abilities
4. **DeepResearch Bench** (Du et al., 2025) provides PhD-level research tasks across 22 domains

All benchmarks demonstrate that current deep research systems, while impressive, still face significant challenges. Even the best-performing systems achieve accuracy rates below 50% on the most difficult tasks, indicating substantial room for improvement.

### 4.2 Training Methodologies

Reinforcement learning emerges as the dominant training paradigm across all reviewed papers. Key RL approaches include:

- **Direct Preference Optimization (DPO)** in WebThinker (Li et al., 2025b)
- **Outcome-based rewards** in Search-R1 (Jin et al., 2025)
- **DUPO (Duplicating Sampling Policy Optimization)** in WebSailor (Li et al., 2025a)
- **DAPO (Decoupled Clip and Dynamic Sampling)** in WebDancer (Wu et al., 2025a)

A consistent pattern is the two-stage training pipeline: supervised fine-tuning for cold start followed by reinforcement learning for generalization. This approach enables models to first acquire basic capabilities before optimizing for complex, multi-step reasoning.

### 4.3 Architectural Innovations

Several architectural innovations address fundamental limitations of existing approaches:

- **Deep Web Explorer modules** enable dynamic search, navigation, and extraction (Li et al., 2025b)
- **Multi-agent frameworks** with explorer-critic paradigms improve memory management (Wu et al., 2025b)
- **Iterative paradigms** with periodic state reconstruction overcome context suffocation (Qiao et al., 2025)
- **Formalization-driven synthesis** provides precise control over reasoning structures (Tao et al., 2025)

The shift from mono-contextual to iterative, multi-workspace architectures represents a significant advancement in addressing the cognitive limitations of linear context accumulation.

### 4.4 Performance Comparisons

Proprietary systems consistently outperform open-source alternatives across benchmarks:

- **OpenAI Deep Research:** ~50% on BrowseComp (Wei et al., 2025), 42.9% on BrowseComp-ZH (Zhou et al., 2025)
- **Gemini-2.5-Pro Deep Research:** Leads in overall RACE scores on DeepResearch Bench (Du et al., 2025)
- **Doubao:** Top-tier proprietary agent performance on BrowseComp-zh (Li et al., 2025a)

However, recent open-source systems like WebSailor-72B (Li et al., 2025a) and WebResearcher (Qiao et al., 2025) have begun matching or surpassing proprietary system performance, indicating rapid progress in the open-source community.

### 4.5 Challenges and Limitations

Several persistent challenges emerge across the literature:

1. **Calibration Issues:** Models with browsing capabilities exhibit higher calibration error, suggesting overconfidence in incorrect answers (Wei et al., 2025)
2. **Context Suffocation:** Linear context accumulation makes agents increasingly ineffective as information grows (Qiao et al., 2025)
3. **Information Obfuscation:** High-uncertainty tasks require sophisticated techniques to increase initial ambiguity (Li et al., 2025a)
4. **Evaluation Complexity:** Assessing deep research agents requires novel methodologies beyond traditional accuracy metrics (Du et al., 2025)

---

## 5. Conclusion

This systematic literature review reveals that deep research agents represent a rapidly evolving field with significant progress in benchmarking, training methodologies, and architectural innovations. The reviewed papers demonstrate that:

1. **Benchmarks are maturing** from simple QA tasks to PhD-level research challenges requiring sophisticated reasoning and information synthesis
2. **Reinforcement learning is essential** for developing autonomous deep research capabilities, with various optimization algorithms showing promise
3. **Architectural innovations** addressing context management and iterative processing are crucial for overcoming fundamental limitations
4. **Proprietary systems lead** but open-source alternatives are rapidly closing the gap

Future research directions include improving calibration and uncertainty estimation, developing more efficient context management strategies, creating multilingual benchmarks beyond English and Chinese, and establishing standardized evaluation frameworks that capture the full spectrum of deep research capabilities.

The field is moving toward increasingly autonomous systems capable of compressing hours of manual research into minutes while maintaining analyst-grade quality. As these systems mature, they promise to transform how researchers, analysts, and knowledge workers access and synthesize information.

---

## References

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents. *arXiv preprint arXiv:2506.11763*. https://arxiv.org/abs/2506.11763

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025). Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning. *arXiv preprint arXiv:2503.09516*. https://arxiv.org/abs/2503.09516

Li, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J. (2025a). WebSailor: Navigating Super-human Reasoning for Web Agent. *arXiv preprint arXiv:2507.02592*. https://arxiv.org/abs/2507.02592

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025b). WebThinker: Empowering Large Reasoning Models with Deep Research Capability. *arXiv preprint arXiv:2504.21776*. https://arxiv.org/abs/2504.21776

Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebResearcher: Unleashing unbounded reasoning capability in Long-Horizon Agents. *arXiv preprint arXiv:2509.13309*. https://arxiv.org/abs/2509.13309

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization. *arXiv preprint arXiv:2507.15061*. https://arxiv.org/abs/2507.15061

Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025). BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents. *arXiv preprint arXiv:2504.12516*. https://arxiv.org/abs/2504.12516

Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025a). WebDancer: Towards Autonomous Information Seeking Agency. *arXiv preprint arXiv:2505.22648*. https://arxiv.org/abs/2505.22648

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025b). WebWalker: Benchmarking LLMs in Web Traversal. *arXiv preprint arXiv:2501.07572*. https://arxiv.org/abs/2501.07572

Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025). BrowseComp-ZH: Benchmarking Web Browsing Ability of Large Language Models in Chinese. *arXiv preprint arXiv:2504.19314*. https://arxiv.org/abs/2504.19314

---

## Sources

### Primary Sources (arXiv Papers)
- [BrowseComp](https://arxiv.org/abs/2504.12516) - Benchmark for web browsing agents
- [BrowseComp-ZH](https://arxiv.org/abs/2504.19314) - Chinese web browsing benchmark
- [DeepResearch Bench](https://arxiv.org/abs/2506.11763) - Comprehensive benchmark for deep research agents
- [Search-R1](https://arxiv.org/abs/2503.09516) - RL-based search engine integration
- [WebDancer](https://arxiv.org/abs/2505.22648) - Autonomous information seeking agent
- [WebResearcher](https://arxiv.org/abs/2509.13309) - Iterative deep research paradigm
- [WebSailor](https://arxiv.org/abs/2507.02592) - Super-human reasoning for web agents
- [WebShaper](https://arxiv.org/abs/2507.15061) - Information-seeking formalization
- [WebThinker](https://arxiv.org/abs/2504.21776) - Deep research capability for LRMs
- [WebWalker](https://arxiv.org/abs/2501.07572) - Web traversal benchmark

---

**Evidence Receipts:** [r3] [r4] [r5] [r6] [r7] [r8] [r9] [r10] [r11] [r12] [r13] [r14]

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E11 | arXiv:2504.12516 | [1 Introduction](https://arxiv.org/html/2504.12516#S1.p2) | “Here we introduce a new benchmark called BrowseComp, which stands for 'Browsing Competition' and comprises 1,266 challenging problems that require browsing a large number of websites to solve.” |
| E12 | arXiv:2504.12516 | [4.1 Performance of OpenAI models](https://arxiv.org/html/2504.12516#S4.SS1.p3) | “Deep Research significantly outperforms all other models, solving around half of the problems.” |
| E13 | arXiv:2504.12516 | [4.3 Test-time compute scaling](https://arxiv.org/html/2504.12516#S4.SS3.p1) | “As shown in Figure 1, each point is a full evaluation run with a different browsing effort, and we see that performance scales smoothly as a function of the amount of test-time compute used.” |
| E14 | arXiv:2504.12516 | [4.2 Calibration Analysis](https://arxiv.org/html/2504.12516#S4.SS2.p1) | “We found models with browsing capabilities such as GPT-4o w/ browsing and Deep Research exhibit higher calibration error, suggesting that access to web tools may increase the model's confidence in incorrect answers.” |
| E27 | arXiv:2504.19314 | [5 Conclusion and Discussion](https://arxiv.org/html/2504.19314#S5.p2) | “AI search products employing multi-turn retrieval, including DeepResearch (42.9%) and Doubao (Deep Search) (26.0%), further outperform purely parametric models, illustrating the effectiveness of test-time scaling through iterative retrieval.” |
| E28 | arXiv:2504.19314 | [3.1 Dataset Construction](https://arxiv.org/html/2504.19314#S3.SS1.p1) | “Inspired by Wei et al. (2025), we adopt a reverse construction strategy: each task begins with a factual answer, from which an elaborate, multi-constraint query is crafted to make direct retrieval non-trivial.” |
| E29 | arXiv:2504.19314 | [Stage 2: Answer Uniqueness Validation](https://arxiv.org/html/2504.19314#S3.SS2.SSS0.Px2.p1) | “This stage focuses on ensuring the uniqueness of the answers, meaning that there is only one correct and unambiguous answer that satisfies all the constraints of each question.” |
| E30 | arXiv:2504.19314 | [4.4 Performance](https://arxiv.org/html/2504.19314#S4.SS4.p1) | “Overall, AI search products equipped with retrieval mechanisms outperformed other categories, followed by closed-source APIs, while open-source models performed the worst on this challenging benchmark.” |
| E34 | arXiv:2501.07572 | [1 Introduction](https://arxiv.org/html/2501.07572#S1.p3) | “WebWalkerQA focuses on text-based reasoning abilities, using a Question-Answer format to evaluate traversal and problem-solving capabilities in web scenarios. We constrain actions to 'click' to evaluate the agent's navigation and information-seeking capabilities.” |
| E35 | arXiv:2501.07572 | [5.2 Main Results](https://arxiv.org/html/2501.07572#S5.SS2.p1) | “Even the best-performing WebWalker using GPT-4o as its backbone does not surpass 40%, highlighting the challenge posed by WebWalkerQA. It can be observed that as the depth increases or the number of sources required increases, the difficulty of acquiring the information needed to resolve the query becomes greater.” |
| E36 | arXiv:2501.07572 | [LLM-based Annotation](https://arxiv.org/html/2501.07572#S3.SS1.SSS0.Px1.p2) | “As illustrated in Figure 2 (b), our dataset construction includes both multi-source and single-source types, corresponding to two types of human information-seeking behaviours within web pages.” |
| E43 | arXiv:2501.07572 | [4 WebWalker](https://arxiv.org/html/2501.07572#S4.p1) | “We introduce WebWalker, a multi-agent framework designed to interact with web environments to answer queries. The WebWalker framework consists of two agents: an explorer agent and a critic agent.” |
| E37 | arXiv:2506.11763 | [1 Introduction](https://arxiv.org/html/2506.11763#S1.p4) | “To fill this gap in evaluating end-to-end research agents, we introduce DeepResearch Bench, a 100-task benchmark spanning 22 domains, with each task meticulously crafted and iteratively refined by domain experts.” |
| E38 | arXiv:2506.11763 | [1 Introduction](https://arxiv.org/html/2506.11763#S1.p5) | “The first one is a Reference-based and Adaptive Criteria-driven Evaluation framework with Dynamic Weighting (denoted as RACE for ease of subsequent reference), which targets the assessment of report generation quality.” |
| E39 | arXiv:2506.11763 | [3.2 FACT: A Framework for Web Retrieval Evaluation](https://arxiv.org/html/2506.11763#S3.SS2.p1) | “To assess the factual grounding of report content and the agent's effectiveness in retrieving and utilizing web-based information, we introduce the framework for Factual Abundance and Citation Trustworthiness(FACT).” |
| E40 | arXiv:2506.11763 | [4.2.1 Evaluation on RACE Framework](https://arxiv.org/html/2506.11763#S4.SS2.SSS1.p1) | “As shown in Table 1, within the DRA category, Gemini-2.5-Pro Deep Research demonstrates leading overall performance on the RACE framework. OpenAI Deep Research also exhibits strong capabilities, surpassing Gemini-2.5-Pro Deep Research in the Instruction-Following dimension.” |
| E41 | arXiv:2506.11763 | [2.2 Benchmark Task Collection](https://arxiv.org/html/2506.11763#S2.SS2.p2) | “We invite Ph.D. or senior practitioners with more than five years of relevant domain experience to propose candidate tasks, as shown in Figure 4. All submissions undergo a manual screening by our team to verify their quality, clarity, complexity, and alignment with our definition of deep research.” |
| E15 | arXiv:2504.21776 | [1 Introduction](https://arxiv.org/html/2504.21776#S1.p4) | “It enables LRMs to autonomously conduct web searches and web page navigation to acquire external knowledge during the reasoning process, facilitating complex real-world problem solving.” |
| E16 | arXiv:2504.21776 | [1 Introduction](https://arxiv.org/html/2504.21776#S1.p5) | “To empower LRMs with the capability to deeply explore web information, we design a Deep Web Explorer module that enables LRMs to search, navigate pages by clicking interactive elements (like links or buttons), and extract relevant information.” |
| E17 | arXiv:2504.21776 | [1 Introduction](https://arxiv.org/html/2504.21776#S1.p7) | “To further unlock the deep research potential of LRM backbones, we develop RL-based training strategies to optimize end-to-end task performance.” |
| E18 | arXiv:2504.21776 | [Main Results.](https://arxiv.org/html/2504.21776#S4.I1.i4.p1) | “RL-trained WebThinker-32B-RL achieves SOTA among 32B models on all benchmarks, substantially improving over its Base version (e.g., +8.5% on GAIA and +21.5% on HLE, respectively).” |
| E19 | arXiv:2503.09516 | [Abstract](https://arxiv.org/html/2503.09516#abstract) | “This paper introduces Search-R1, an extension of reinforcement learning (RL) for reasoning frameworks where the LLM learns to autonomously generate (multiple) search queries during step-by-step reasoning with real-time retrieval.” |
| E20 | arXiv:2503.09516 | [Loss Masking for Retrieved Tokens.](https://arxiv.org/html/2503.09516#S3.SS1.SSS0.Px1.p1) | “To address this, we introduce loss masking for retrieved tokens, ensuring the policy gradient objective is computed only over LLM-generated tokens, excluding retrieved content from the optimization process.” |
| E21 | arXiv:2503.09516 | [3 Search-R1](https://arxiv.org/html/2503.09516#S3.p1) | “In the following sections, we present the detailed design for training methods of Search-R1, covering (1) extending RL to utilize search engines; (2) text generation with an interleaved multi-turn search engine call; (3) the training template; and (4) reward model design.” |
| E26 | arXiv:2503.09516 | [4.4 Performance](https://arxiv.org/html/2503.09516#S4.SS4.p1) | “We achieve 24% and 20% average relative improvement with Qwen2.5-7B and Qwen2.5-3B, respectively.” |
| E22 | arXiv:2507.02592 | [3.1 SailorFog-QA: Scalable Graph-Synthesized QA](https://arxiv.org/html/2507.02592#S3.I1.i3.p1) | “Level 3: the focus of our work, involves problems with both high uncertainty and high difficulty in its reduction.” |
| E23 | arXiv:2507.02592 | [Generating High-Uncertainty Questions via Subgraph Sampling and Obfuscation](https://arxiv.org/html/2507.02592#S3.SS1.SSS0.Px2.p1) | “Critically, we introduce ambiguity through deliberate information obfuscation.” |
| E24 | arXiv:2507.02592 | [4.2 Duplicating Sampling Policy Optimization](https://arxiv.org/html/2507.02592#S4.SS2.p3) | “Compared to DAPO's dynamic sampling, this approach achieves approximately 2–3 times speedup.” |
| E25 | arXiv:2507.02592 | [Achieving Parity with Proprietary Systems](https://arxiv.org/html/2507.02592#S5.SS2.SSS0.Px4.p1) | “On BrowseComp-zh, WebSailor-72B achieves performance on par with Doubao, a top-tier proprietary agent.” |
| E1 | arXiv:2505.22648 | [1 Introduction](https://arxiv.org/html/2505.22648#S1.p1) | “Recent systems, such as ChatGPT Deep Research OpenAI (2025a) and Grok DeepSearch x.ai (2025), have demonstrated strong deep information-seeking capabilities through end-to-end reinforcement learning (RL) training.” |
| E2 | arXiv:2505.22648 | [1 Introduction](https://arxiv.org/html/2505.22648#S1.p5) | “We synthesise the datasets in two ways: 1). By crawling web pages to construct deep queries, referred to as crawlQA, enabling the acquisition of web information through click actions. 2). By enhancing easy-to-hard QA pairs synthesis to incentivize the progression from weak-to-strong agency, transforming simple questions into complex ones, termed e2hQA.” |
| E3 | arXiv:2505.22648 | [3 Multi-Step Multi-Tool Agent Learning](https://arxiv.org/html/2505.22648#S3.p1) | “We first train a policy model π_θ via agent SFT for cold start, followed by agent RL for generalization.” |
| E4 | arXiv:2505.22648 | [3.2 Agent Reinforcement Learning](https://arxiv.org/html/2505.22648#S3.SS2.p1) | “Building on the SFT stage, RL employs Decoupled Clip and Dynamic Sampling Policy Optimization algorithm to refine and incentivize the policy model π_θ's ability to interleave Thought-Action-Observation sequences.” |
| E5 | arXiv:2505.22648 | [4.2 Experimental Results](https://arxiv.org/html/2505.22648#S4.SS2.p1) | “Notably, it even surpasses the performance of GPT-4o in the best-case scenario.” |
| E31 | arXiv:2507.15061 | [1 Introduction](https://arxiv.org/html/2507.15061#S1.p4) | “Unlike prior approaches, we first formalize information-seeking tasks and then systematically guide data synthesis through this formalization. During generation, information collection is explicitly controlled by formal task requirements.” |
| E32 | arXiv:2507.15061 | [4.2 Main Results](https://arxiv.org/html/2507.15061#S4.SS2.p2) | “WebShaper is currently the only open source method with a score of more than 60 points, which is close to the SOTA OpenAI DR system. WebShaper is implemented fully under open-sourced LLMs, demonstrating that high-quality IS data can deeply stimulate the ability of DR Agents.” |
| E33 | arXiv:2507.15061 | [3.2 Agentic Expansion](https://arxiv.org/html/2507.15061#S3.SS2.p2) | “Therefore, we establish an Agentic Expansion. We first introduce the KP representation, which enables clear comprehension of our IS formalization. Then, we propose the Layer-wise Expansion Strategy to mitigate the limitations of redundant and reasoning shortcuts.” |
| E42 | arXiv:2507.15061 | [2 Information-Seeking Formalization](https://arxiv.org/html/2507.15061#S2.p5) | “For a subset V\subseteq{\mathcal{E}} and a sub-space R , define a Knowledge Projection (KP): For example, when R denotes entity pairs of relation bornIn, R(\{\textit{90s}\}) represents the set of all people born in 90s.” |
| E6 | arXiv:2509.13309 | [1 Introduction](https://arxiv.org/html/2509.13309#S1.p2) | “While this linear accumulation strategy appears intuitive and has shown initial success, a deeper analysis reveals that it fundamentally constrains the potential of deep-research agents.” |
| E7 | arXiv:2509.13309 | [2 IterResearch: An Iterative Deep-Research Paradigm](https://arxiv.org/html/2509.13309#S2.p1) | “These limitations create a paradox: as agents gather more information to solve complex problems, their mono-contextual architecture becomes increasingly ineffective.” |
| E8 | arXiv:2509.13309 | [2 IterResearch: An Iterative Deep-Research Paradigm](https://arxiv.org/html/2509.13309#S2.p2) | “To overcome these limitations, we propose IterResearch, which reformulates deep research as a Markov Decision Process (MDP) with periodic state reconstruction.” |
| E9 | arXiv:2509.13309 | [3 A Scalable Data Engine for Advancing Agentic Intelligence](https://arxiv.org/html/2509.13309#S3.p1) | “Our engine leverages a collaborative multi-agent framework organized into a three-stage iterative workflow: (1) seed data generation, (2) iterative complexity escalation, and (3) rigorous quality control.” |
| E10 | arXiv:2509.13309 | [8 Conclusion](https://arxiv.org/html/2509.13309#S8.p1) | “Extensive experiments across 6 challenging benchmarks demonstrate that WebResearcher achieves state-of-the-art performance, surpassing even frontier proprietary systems.” |

<!-- /evidence-appendix -->
