# Systematic Literature Review: Deep Research

**Date:** October 26, 2026  
**Search Period:** November 24, 2023 – November 23, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Total Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in deep research capabilities for large language models and autonomous agents. The reviewed papers span from January 2025 to September 2025, reflecting the rapid emergence of this research area. Key themes include benchmarking web browsing capabilities, training methodologies for search-augmented reasoning, and frameworks for autonomous information-seeking agents.

---

## Reviewed Papers (APA Format)

### 1. Benchmarking Web Browsing Capabilities

**Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025).** BrowseComp: A simple yet challenging benchmark for browsing agents. *arXiv preprint arXiv:2504.12516*. https://arxiv.org/abs/2504.12516v1

This paper introduces BrowseComp, a benchmark comprising 1,266 questions requiring persistent web navigation to find hard-to-find, entangled information. The benchmark is designed to measure core browsing capabilities through short, easily verifiable answers. Despite sidestepping challenges like generating long answers or resolving ambiguity, BrowseComp effectively exercises persistence and creativity in information finding, analogous to programming competitions for coding agents.

**Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025).** BrowseComp-ZH: Benchmarking web browsing ability of large language models in Chinese. *arXiv preprint arXiv:2504.19314*. https://arxiv.org/abs/2504.19314v2

Addressing the English-centric limitation of existing benchmarks, BrowseComp-ZH evaluates LLM agents on the Chinese web with 289 multi-hop questions across 11 domains. Using a two-stage quality control protocol, the benchmark achieves high difficulty: most models score below 10% accuracy, and even the best-performing system (OpenAI's DeepResearch) reaches only 42.9%. The benchmark reveals that success requires effective retrieval strategies, sophisticated reasoning, and information reconciliation—capabilities current models still struggle to master.

**Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025).** WebWalker: Benchmarking LLMs in web traversal. *arXiv preprint arXiv:2501.07572*. https://arxiv.org/abs/2501.07572v3

WebWalkerQA assesses LLMs' ability to systematically traverse website subpages to extract high-quality data, addressing limitations of traditional search engines that retrieve shallow content. The accompanying WebWalker framework employs a multi-agent explore-critic paradigm mimicking human-like web navigation. Experimental results demonstrate both the challenge of the benchmark and the effectiveness of combining retrieval-augmented generation with structured web traversal.

**Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025).** DeepResearch Bench: A comprehensive benchmark for deep research agents. *arXiv preprint arXiv:2506.11763*. https://arxiv.org/abs/2506.11763v1

This work presents the first comprehensive benchmark specifically for Deep Research Agents, consisting of 100 PhD-level research tasks across 22 fields. The authors propose two novel evaluation methodologies: a reference-based method with adaptive criteria for assessing research report quality, and a framework evaluating information retrieval capabilities through effective citation count and accuracy. This benchmark addresses the critical gap in systematically evaluating agents that transform online information into analyst-grade, citation-rich reports.

---

### 2. Training Methodologies for Search-Augmented Reasoning

**Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025).** Search-R1: Training LLMs to reason and leverage search engines with reinforcement learning. *arXiv preprint arXiv:2503.09516*. https://arxiv.org/abs/2503.09516v5

Search-R1 extends reinforcement learning frameworks to teach LLMs autonomous search query generation during step-by-step reasoning with real-time retrieval. The approach optimizes reasoning trajectories with multi-turn search interactions, employing retrieved token masking for stable training and an outcome-based reward function. Experiments on seven question-answering datasets show 41% improvement (Qwen2.5-7B) and 20% improvement (Qwen2.5-3B) over various RAG baselines, providing empirical insights into RL optimization, LLM choices, and response length dynamics in retrieval-augmented reasoning.

**Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025).** WebThinker: Empowering large reasoning models with deep research capability. *arXiv preprint arXiv:2504.21776*. https://arxiv.org/abs/2504.21776v2

WebThinker addresses the limitation of large reasoning models' reliance on static internal knowledge by integrating a Deep Web Explorer module for dynamic web information extraction. The framework employs an Autonomous Think-Search-and-Draft strategy, seamlessly interleaving reasoning, information gathering, and report writing. An RL-based training strategy via iterative online Direct Preference Optimization enhances tool utilization. Experiments on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and scientific report generation tasks (Glaive) demonstrate significant outperformance over existing methods and strong proprietary systems.

---

### 3. Autonomous Information-Seeking Agents

**Li, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J. (2025).** WebSailor: Navigating super-human reasoning for web agent. *arXiv preprint arXiv:2507.02592*. https://arxiv.org/abs/2507.02592v1

Addressing the success of proprietary systems like DeepResearch on complex benchmarks, WebSailor introduces a post-training methodology instilling the capability to systematically reduce extreme uncertainty in vast information landscapes. The approach generates novel high-uncertainty tasks through structured sampling and information obfuscation, RFT cold start, and Duplicating Sampling Policy Optimization (DUPO) for agentic RL training. WebSailor significantly outperforms all open-source agents in complex information-seeking tasks, matching proprietary agents' performance and closing the capability gap.

**Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025).** WebDancer: Towards autonomous information seeking agency. *arXiv preprint arXiv:2505.22648*. https://arxiv.org/abs/2505.22648v3

WebDancer presents a cohesive four-stage paradigm for building end-to-end agentic information seeking agents: (1) browsing data construction, (2) trajectory sampling, (3) supervised fine-tuning for effective cold start, and (4) reinforcement learning for enhanced generalization. Instantiated on the ReAct framework, WebDancer achieves considerable results on GAIA and WebWalkerQA benchmarks. The work provides actionable, systematic pathways for developing more capable agentic models through a data-centric and training-stage perspective.

**Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025).** WebShaper: Agentically data synthesizing via information-seeking formalization. *arXiv preprint arXiv:2507.15061*. https://arxiv.org/abs/2507.15061v1

Addressing the scarcity of high-quality training data for information-seeking agents, WebShaper proposes a formalization-driven data synthesis framework using set theory. The central concept of Knowledge Projections enables precise control over reasoning structure through KP operation compositions. Starting from seed tasks, a multi-step expansion process uses an agentic Expander with retrieval and validation tools. Models trained on the synthesized dataset achieve state-of-the-art performance among open-sourced IS agents on GAIA and WebWalkerQA benchmarks.

**Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025).** WebResearcher: Unleashing unbounded reasoning capability in long-horizon agents. *arXiv preprint arXiv:2509.13309*. https://arxiv.org/abs/2509.13309v2

WebResearcher reformulates deep research as a Markov Decision Process, where agents periodically consolidate findings into evolving reports while maintaining focused workspaces, overcoming context suffocation and noise contamination in mono-contextual approaches. The framework includes WebFrontier, a scalable data synthesis engine generating high-quality training data through tool-augmented complexity escalation. The paradigm naturally scales through parallel thinking for concurrent multi-agent exploration. Extensive experiments across six challenging benchmarks demonstrate state-of-the-art performance, surpassing frontier proprietary systems.

---

## Thematic Analysis

### Benchmarking Trends

Four papers focus on benchmarking deep research capabilities, revealing a clear progression in evaluation complexity. BrowseComp established the foundation with verifiable short-answer questions requiring persistent web navigation. BrowseComp-ZH extended this to non-English contexts, revealing significant performance gaps in Chinese web browsing. WebWalkerQA introduced the dimension of systematic website traversal beyond shallow retrieval. DeepResearch Bench represents the most comprehensive evaluation, targeting PhD-level research tasks with citation-rich report generation.

### Training Paradigm Evolution

The reviewed papers demonstrate convergence on several key training principles:

1. **Reinforcement Learning**: Search-R1, WebThinker, WebSailor, and WebDancer all employ RL-based approaches, with outcome-based rewards and preference optimization emerging as effective strategies.

2. **Data Synthesis**: WebShaper and WebResearcher address training data scarcity through formalized synthesis frameworks, moving beyond information-driven collection to structured task generation.

3. **Interleaved Reasoning and Search**: WebThinker's Think-Search-and-Draft strategy and WebResearcher's iterative consolidation represent a shift from sequential to integrated reasoning-search workflows.

4. **Uncertainty Reduction**: WebSailor identifies systematic uncertainty reduction in vast information landscapes as the key capability distinguishing superhuman from human-level performance.

### Capability Gaps

Despite rapid progress, significant gaps remain:

- **Language Coverage**: BrowseComp-ZH reveals severe limitations in non-English web browsing, with even top systems achieving only 42.9% accuracy.
- **Open vs. Proprietary**: WebSailor and WebResearcher demonstrate that open-source approaches can match proprietary systems, but the gap remains substantial in complex information-seeking tasks.
- **Context Management**: WebResearcher identifies context suffocation and noise contamination as critical limitations in mono-contextual approaches.
- **Research-Level Tasks**: DeepResearch Bench's PhD-level tasks represent a frontier where current agents still require significant improvement.

---

## Methodology

**Search Strategy**: Papers were identified through arXiv search in the cs.CL category with publication dates between November 24, 2023, and November 23, 2025. The search query "deep research" was used to identify relevant papers.

**Screening Process**: From an initial pool of 50 papers, 89 additional papers were identified through citation expansion, resulting in 30 shortlisted papers. Papers were screened based on relevance to deep research methodologies, automated research systems, literature review automation, and research assistance tools.

**Selection Criteria**: The final 10 papers were selected based on:
- Direct relevance to deep research capabilities
- Focus on benchmarking, training, or agent frameworks
- Publication in the cs.CL category
- Empirical evaluation with quantitative results

---

## Conclusion

The deep research field has experienced rapid maturation in 2025, with significant advances in benchmarking, training methodologies, and autonomous agent frameworks. The convergence on reinforcement learning, data synthesis, and interleaved reasoning-search workflows suggests emerging best practices. However, challenges remain in language coverage, context management, and research-level task performance. The release of comprehensive benchmarks like DeepResearch Bench and open-source frameworks like WebResearcher and WebSailor indicate a trajectory toward democratizing deep research capabilities previously limited to proprietary systems.

Future research directions include:
- Multilingual and cross-lingual deep research capabilities
- Improved context management for long-horizon tasks
- Integration of domain-specific knowledge and tools
- Human-agent collaboration frameworks for research tasks
- Evaluation of citation quality and report coherence

---

## References

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A comprehensive benchmark for deep research agents. *arXiv preprint arXiv:2506.11763*. https://arxiv.org/abs/2506.11763v1

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025). Search-R1: Training LLMs to reason and leverage search engines with reinforcement learning. *arXiv preprint arXiv:2503.09516*. https://arxiv.org/abs/2503.09516v5

Li, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J. (2025). WebSailor: Navigating super-human reasoning for web agent. *arXiv preprint arXiv:2507.02592*. https://arxiv.org/abs/2507.02592v1

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025). WebThinker: Empowering large reasoning models with deep research capability. *arXiv preprint arXiv:2504.21776*. https://arxiv.org/abs/2504.21776v2

Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebResearcher: Unleashing unbounded reasoning capability in long-horizon agents. *arXiv preprint arXiv:2509.13309*. https://arxiv.org/abs/2509.13309v2

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically data synthesizing via information-seeking formalization. *arXiv preprint arXiv:2507.15061*. https://arxiv.org/abs/2507.15061v1

Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025). BrowseComp: A simple yet challenging benchmark for browsing agents. *arXiv preprint arXiv:2504.12516*. https://arxiv.org/abs/2504.12516v1

Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebDancer: Towards autonomous information seeking agency. *arXiv preprint arXiv:2505.22648*. https://arxiv.org/abs/2505.22648v3

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025). WebWalker: Benchmarking LLMs in web traversal. *arXiv preprint arXiv:2501.07572*. https://arxiv.org/abs/2501.07572v3

Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025). BrowseComp-ZH: Benchmarking web browsing ability of large language models in Chinese. *arXiv preprint arXiv:2504.19314*. https://arxiv.org/abs/2504.19314v2
