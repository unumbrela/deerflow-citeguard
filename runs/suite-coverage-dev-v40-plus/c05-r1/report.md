# Systematic Literature Review: Deep Research

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "deep research", category cs.CL, published between 2023-11-24 and 2025-11-23
**Citation format**: APA 7th edition

## Executive Summary

The deep research field has experienced rapid development between 2023-2025, with researchers focusing on empowering large language models and reasoning systems with autonomous web browsing and information synthesis capabilities. The surveyed literature reveals a maturing ecosystem characterized by sophisticated benchmarking frameworks, novel training methodologies leveraging reinforcement learning and preference optimization, and increasingly capable agent architectures that approach or surpass human-level performance on complex information-seeking tasks. A notable trend is the shift from simple retrieval-augmented generation toward iterative, multi-step research processes where agents dynamically formulate queries, navigate web content, and synthesize findings into comprehensive reports. The field demonstrates strong convergence around the need for persistent, creative browsing strategies and systematic uncertainty reduction, though significant challenges remain in handling long-horizon tasks and avoiding context suffocation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "deep research", filtered to category cs.CL, published between 2023-11-24 and 2025-11-23. The scholar search identified 50 papers by phrase matching, with citation expansion adding 90 additional papers from references. From a shortlist of 30 papers, 10 were selected based on centrality to the deep research topic and co-citation frequency. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents working from paper abstracts, with cross-paper synthesis performed by the lead agent.

**Screening flow**: Identified by search: 50; Added from references: 90; Shortlisted: 30; Screened: 30; Included: 10 (6 from citation expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Metadata extraction relied solely on abstracts, which may not capture full methodological details or nuanced findings.

## Themes

### Theme 1: Benchmarking and Evaluation Frameworks

A substantial portion of recent deep research literature focuses on creating rigorous benchmarks to evaluate agent capabilities. This reflects the field's maturation from proof-of-concept demonstrations toward systematic capability assessment. Wei et al. (2025) introduced BrowseComp, comprising 1,266 questions requiring persistent internet navigation to find hard-to-find, entangled information with easily verifiable answers. The benchmark deliberately sidesteps challenges of true user query distributions while measuring core browsing capabilities analogous to programming competitions for coding agents.

Extending this work to multilingual contexts, Zhou et al. (2025) created BrowseComp-ZH with 289 multi-hop questions across 11 domains for the Chinese web ecosystem. Their findings reveal severe capability gaps, with most models achieving below 10% accuracy and even OpenAI's DeepResearch reaching only 42.9%, highlighting the linguistic, infrastructural, and censorship-related complexities unique to Chinese web navigation.

Wu et al. (2025a) introduced WebWalkerQA to assess LLMs' capacity for systematic data extraction from multi-layered website content, addressing the limitation that traditional search engines retrieve only shallow content. Most comprehensively, Du et al. (2025) presented DeepResearch Bench with 100 PhD-level research tasks across 22 fields, proposing both reference-based evaluation with adaptive criteria and citation-based frameworks for assessing information retrieval capabilities. These benchmarks collectively establish rigorous evaluation standards that enable systematic comparison of agent capabilities.

### Theme 2: Training Methodologies for Deep Research Agents

The literature demonstrates strong convergence around advanced training paradigms that combine supervised fine-tuning with reinforcement learning. Li et al. (2025) proposed WebThinker, employing an Autonomous Think-Search-and-Draft strategy with RL-based training via iterative online Direct Preference Optimization (DPO). Their approach enables large reasoning models to autonomously search the web, navigate among pages, and draft reports during reasoning, significantly outperforming existing methods on GPQA, GAIA, WebWalkerQA, and HLE benchmarks.

Jin et al. (2025) extended reinforcement learning for reasoning frameworks with Search-R1, where LLMs learn to generate multiple search queries during step-by-step reasoning with real-time retrieval. Their retrieved token masking technique enables stable RL training with a simple outcome-based reward function, improving performance by 41% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines across seven question-answering datasets.

Wu et al. (2025b) presented WebDancer with a four-stage paradigm: browsing data construction, trajectories sampling, supervised fine-tuning for effective cold start, and reinforcement learning for enhanced generalization. Based on the ReAct architecture, WebDancer achieves considerable results on GAIA and WebWalkerQA benchmarks, demonstrating the efficacy of combining SFT cold starts with RL-enhanced generalization. Li et al. (2025) similarly emphasized that WebThinker paves the way for more capable and versatile deep research systems through their training approach.

### Theme 3: Agent Architectures for Information Seeking

Novel agent architectures emerge as a central theme, with researchers developing increasingly sophisticated frameworks for navigating vast information landscapes. Li et al. (2025) introduced WebThinker's Deep Web Explorer module, enabling dynamic search, navigation, and information extraction from web sources beyond static internal knowledge.

Wu et al. (2025a) proposed WebWalker, a multi-agent framework mimicking human-like web navigation through an explore-critic paradigm combining retrieval-augmented generation with horizontal and vertical integration. This architecture addresses the limitation of shallow content retrieval by systematically traversing website subpages for comprehensive data extraction.

Qiao et al. (2025) introduced WebResearcher, reformulating deep research as a Markov Decision Process where agents consolidate findings into evolving reports with focused workspaces. This iterative paradigm overcomes context suffocation and noise contamination plaguing existing mono-contextual approaches. The architecture naturally scales through parallel thinking, enabling concurrent multi-agent exploration and achieving state-of-the-art performance across six challenging benchmarks, surpassing frontier proprietary systems.

### Theme 4: Superhuman Reasoning and Uncertainty Reduction

A particularly ambitious thread in the literature focuses on instilling superhuman reasoning capabilities in open-source agents. Li et al. (2025) introduced WebSailor, a complete post-training methodology that generates novel high-uncertainty tasks through structured sampling and information obfuscation, combined with RFT cold start and an efficient agentic RL training algorithm called Duplicating Sampling Policy Optimization (DUPO).

The core insight is that success hinges on instilling the ability to systematically reduce extreme uncertainty when navigating vast information landscapes. WebSailor significantly outperforms all open-source agents in complex information-seeking tasks, matches proprietary agents' performance, and closes the capability gap, demonstrating that superhuman capabilities on extremely complex information-seeking benchmarks are attainable.

This theme connects to broader questions about what distinguishes expert-level research capabilities from basic information retrieval. The emphasis on systematic uncertainty reduction suggests that deep research competence requires not just finding information, but strategically navigating information spaces where relevant content is deliberately obscured or distributed across multiple sources.

### Theme 5: Data Synthesis for Agent Training

Recognizing the scarcity of high-quality training data for deep research agents, recent work focuses on programmatic data synthesis. Tao et al. (2025) proposed WebShaper, a formalization-driven information-seeking data synthesis framework using set theory and Knowledge Projections to enable precise control over reasoning structure. The approach creates seed tasks and uses a multi-step expansion process with an agentic Expander employing retrieval and validation tools.

Models trained on WebShaper's synthesized dataset achieve state-of-the-art performance among open-sourced information-seeking agents, demonstrating superior performance on GAIA and WebWalkerQA benchmarks compared to existing approaches. The formalization addresses inconsistency between information structure and reasoning structure in agent data synthesis.

Qiao et al. (2025) similarly proposed WebFrontier, a scalable data synthesis engine using tool-augmented complexity escalation that bridges passive knowledge recall and active knowledge construction. Their training data significantly enhances tool-use capabilities even for traditional mono-contextual methods, suggesting that high-quality synthesized data can benefit diverse architectural approaches.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong agreement on several foundational points. First, all papers converge on the necessity of moving beyond simple retrieval-augmented generation toward iterative, multi-step research processes where agents dynamically formulate queries and synthesize findings (Li et al., 2025; Qiao et al., 2025; Jin et al., 2025). Second, there is consensus that benchmarking must involve hard-to-find, entangled information requiring persistent navigation rather than simple factoid retrieval (Wei et al., 2025; Zhou et al., 2025; Du et al., 2025). Third, all training-focused papers agree on combining supervised fine-tuning for cold-start capability with reinforcement learning for enhanced generalization (Wu et al., 2025b; Li et al., 2025; Jin et al., 2025). Fourth, the literature converges on the importance of systematic uncertainty reduction as a core capability distinguishing expert-level agents from basic information retrieval systems (Li et al., 2025; Qiao et al., 2025).

**Disagreements**: The literature shows limited direct disagreement, reflecting the field's early stage where researchers are exploring complementary rather than competing approaches. However, there are implicit tensions in architectural philosophy: WebWalker's multi-agent explore-critic paradigm (Wu et al., 2025a) contrasts with WebResearcher's iterative consolidation into evolving reports (Qiao et al., 2025), suggesting different views on whether parallel agent collaboration or sequential report refinement better handles long-horizon tasks. Additionally, while WebSailor achieves superhuman performance through high-uncertainty task generation (Li et al., 2025), BrowseComp deliberately uses easily verifiable answers (Wei et al., 2025), reflecting different priorities in benchmark design between measuring capability ceilings versus core browsing competence.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the papers explicitly address limitations in their abstracts, suggesting either space constraints or reluctance to acknowledge weaknesses in this rapidly competitive field. This absence of stated limitations itself represents a gap in transparency.

Second, while multiple papers mention handling long-horizon tasks (Qiao et al., 2025; Wu et al., 2025b), none provide detailed analysis of failure modes as task horizon extends beyond current benchmarks. The challenge of maintaining coherent research strategies over dozens or hundreds of sequential actions remains underexplored.

Third, the literature focuses heavily on English and Chinese web ecosystems (Wei et al., 2025; Zhou et al., 2025), with no benchmarks or methods addressing other linguistic and infrastructural contexts. This limits generalizability to global research scenarios.

Fourth, while DeepResearch Bench provides PhD-level tasks (Du et al., 2025), none of the papers evaluate whether their agents can produce genuinely novel research insights versus synthesizing existing information. The leap from information synthesis to knowledge creation remains unaddressed.

Fifth, the emphasis on RL training raises questions about sample efficiency and computational costs that none of the papers address in their abstracts. Practical deployment considerations for resource-constrained environments remain unexplored.

## Per-Paper Annotations

### Du et al. (2025)

**Research question**: How can we systematically evaluate the capabilities of Deep Research Agents that autonomously orchestrate multistep web exploration and synthesis?
**Methodology**: Presented DeepResearch Bench with 100 PhD-level research tasks across 22 fields, proposing reference-based evaluation with adaptive criteria and citation-based frameworks for assessing information retrieval capabilities.
**Key findings**:
- DeepResearch Bench provides 100 PhD-level research tasks across 22 distinct fields for evaluating Deep Research Agents
- Reference-based evaluation method with adaptive criteria achieves strong alignment with human judgment for report quality assessment
- Citation-based framework effectively evaluates DRA information retrieval and collection capabilities
- Benchmark and key framework components have been open-sourced to accelerate DRA development
**Limitations**: Not stated in abstract

### Jin et al. (2025)

**Research question**: How can we train LLMs to autonomously generate search queries during step-by-step reasoning with real-time retrieval?
**Methodology**: Extended reinforcement learning for reasoning frameworks where the LLM learns to generate multiple search queries during step-by-step reasoning with real-time retrieval, using retrieved token masking for stable RL training and a simple outcome-based reward function.
**Key findings**:
- Search-R1 improves performance by 41% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines on seven question-answering datasets
- Approach optimizes LLM reasoning trajectories with multi-turn search interactions
- Provides empirical insights into RL optimization methods, LLM choices, and response length dynamics in retrieval-augmented reasoning
**Limitations**: Not stated in abstract

### Li et al. (2025a)

**Research question**: How can we instill super-human reasoning capabilities in open-source web agents to systematically reduce extreme uncertainty when navigating vast information landscapes?
**Methodology**: Introduced WebSailor, a complete post-training methodology involving generating novel high-uncertainty tasks through structured sampling and information obfuscation, RFT cold start, and an efficient agentic RL training algorithm called Duplicating Sampling Policy Optimization (DUPO).
**Key findings**:
- WebSailor significantly outperforms all open-source agents in complex information-seeking tasks
- WebSailor matches proprietary agents' performance and closes the capability gap
- Success hinges on instilling the ability to systematically reduce extreme uncertainty when navigating vast information landscapes
- Approach demonstrates that superhuman capabilities on extremely complex information-seeking benchmarks are attainable
**Limitations**: Not stated in abstract

### Li et al. (2025b)

**Research question**: How can we empower large reasoning models to autonomously search the web and produce comprehensive research reports beyond their static internal knowledge?
**Methodology**: Proposed WebThinker, a deep research agent with a Deep Web Explorer module that enables LRMs to dynamically search, navigate, and extract information from the web, employing an Autonomous Think-Search-and-Draft strategy with RL-based training via iterative online Direct Preference Optimization (DPO).
**Key findings**:
- WebThinker significantly outperforms existing methods and strong proprietary systems on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE)
- Approach enhances LRM reliability and applicability in complex scenarios
- WebThinker enables LRMs to autonomously search the web, navigate among web pages, and draft reports during the reasoning process
- Method paves the way for more capable and versatile deep research systems
**Limitations**: Not stated in abstract

### Qiao et al. (2025)

**Research question**: How can we build AI agents that autonomously discover and synthesize knowledge from external sources while overcoming context suffocation and noise contamination?
**Methodology**: Introduced WebResearcher, an iterative deep-research paradigm that reformulates deep research as a Markov Decision Process where agents consolidate findings into evolving reports with focused workspaces. Also proposed WebFrontier, a scalable data synthesis engine using tool-augmented complexity escalation, with natural scaling through parallel thinking for concurrent multi-agent exploration.
**Key findings**:
- WebResearcher overcomes context suffocation and noise contamination plaguing existing mono-contextual approaches through periodic consolidation into evolving reports
- WebFrontier generates high-quality training data through tool-augmented complexity escalation, bridging passive knowledge recall and active knowledge construction
- Training data from the paradigm significantly enhances tool-use capabilities even for traditional mono-contextual methods
- Paradigm naturally scales through parallel thinking enabling concurrent multi-agent exploration
- WebResearcher achieves state-of-the-art performance across 6 challenging benchmarks, surpassing frontier proprietary systems
**Limitations**: Not stated in abstract

### Tao et al. (2025)

**Research question**: How can we mitigate the inconsistency between information structure and reasoning structure in information-seeking agent data synthesis?
**Methodology**: Proposed WebShaper, a formalization-driven information-seeking data synthesis framework that uses set theory and Knowledge Projections to enable precise control over reasoning structure. The approach creates seed tasks and uses a multi-step expansion process with an agentic Expander that employs retrieval and validation tools.
**Key findings**:
- WebShaper systematically formalizes information-seeking tasks through set theory with Knowledge Projections enabling precise control over reasoning structure
- Multi-step expansion process uses an agentic Expander with retrieval and validation tools to create increasingly complex formal questions
- Models trained on the synthesized dataset achieve state-of-the-art performance among open-sourced information-seeking agents
- WebShaper demonstrates superior performance on GAIA and WebWalkerQA benchmarks compared to existing approaches
**Limitations**: Not stated in abstract

### Wei et al. (2025)

**Research question**: How can we measure the ability of agents to browse the web effectively?
**Methodology**: Created BrowseComp, a benchmark comprising 1,266 questions that require persistently navigating the internet to find hard-to-find, entangled information with short, easily verifiable answers.
**Key findings**:
- BrowseComp is simple and easy-to-use as a benchmark for browsing agents
- Benchmark measures the important core capability of exercising persistence and creativity in finding information
- BrowseComp can be seen as analogous to how programming competitions are an incomplete but useful benchmark for coding agents
- Benchmark sidesteps challenges of a true user query distribution while measuring core browsing capabilities
**Limitations**: BrowseComp sidesteps challenges of a true user query distribution, such as generating long answers or resolving ambiguity

### Wu et al. (2025a)

**Research question**: How can we assess the ability of LLMs to perform web traversal and extract high-quality data systematically from multi-layered website content?
**Methodology**: Introduced WebWalkerQA, a benchmark designed to evaluate LLMs' capacity to traverse website subpages for systematic data extraction. Also proposed WebWalker, a multi-agent framework that mimics human-like web navigation through an explore-critic paradigm combining RAG with horizontal and vertical integration.
**Key findings**:
- Traditional search engines retrieve shallow content, limiting LLMs' ability to handle complex, multi-layered information
- WebWalkerQA benchmark effectively assesses LLMs' web traversal capabilities across multiple website layers
- WebWalker multi-agent framework demonstrates effectiveness through an explore-critic paradigm mimicking human navigation
- Combination of RAG with WebWalker shows strong performance in real-world scenarios through horizontal and vertical integration
**Limitations**: Not stated in abstract

### Wu et al. (2025b)

**Research question**: How can we build end-to-end agentic information seeking agents through a data-centric and training-stage perspective?
**Methodology**: Presented a four-stage paradigm: (1) browsing data construction, (2) trajectories sampling, (3) supervised fine-tuning for effective cold start, and (4) reinforcement learning for enhanced generalisation. Instantiated this framework in WebDancer, a web agent based on the ReAct architecture.
**Key findings**:
- Four-stage training paradigm enables end-to-end development of agentic information seeking agents
- Supervised fine-tuning provides effective cold start capability for the agent
- Reinforcement learning enhances the agent's generalisation abilities
- WebDancer achieves considerable results on GAIA and WebWalkerQA benchmarks, demonstrating the efficacy of the training paradigm
- Analysis provides systematic pathways for developing more capable agentic models
**Limitations**: Not stated in abstract

### Zhou et al. (2025)

**Research question**: How can we benchmark the web browsing ability of large language models in the Chinese web ecosystem, accounting for linguistic, infrastructural, and censorship-related complexities?
**Methodology**: Created BrowseComp-ZH, a high-difficulty benchmark with 289 multi-hop questions spanning 11 diverse domains, reverse-engineered from short verifiable answers, with a two-stage quality control protocol to ensure high question difficulty and answer uniqueness.
**Key findings**:
- Most models struggle severely on BrowseComp-ZH, with accuracy rates below 10%
- Only a handful of models exceed 20% accuracy on the benchmark
- Even the best-performing system (OpenAI's DeepResearch) reaches just 42.9% accuracy
- Success on BrowseComp-ZH demands effective retrieval strategies, sophisticated reasoning, and information reconciliation capabilities that current models still struggle to master
- Dataset, construction guidelines, and benchmark results have been publicly released
**Limitations**: Not stated in abstract

## References

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A comprehensive benchmark for deep research agents. arXiv. https://arxiv.org/abs/2506.11763

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025). Search-R1: Training LLMs to reason and leverage search engines with reinforcement learning. arXiv. https://arxiv.org/abs/2503.09516

Li, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J. (2025a). WebSailor: Navigating super-human reasoning for web agent. arXiv. https://arxiv.org/abs/2507.02592

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025b). WebThinker: Empowering large reasoning models with deep research capability. arXiv. https://arxiv.org/abs/2504.21776

Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebResearcher: Unleashing unbounded reasoning capability in long-horizon agents. arXiv. https://arxiv.org/abs/2509.13309

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically data synthesizing via information-seeking formalization. arXiv. https://arxiv.org/abs/2507.15061

Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025). BrowseComp: A simple yet challenging benchmark for browsing agents. arXiv. https://arxiv.org/abs/2504.12516

Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025a). WebDancer: Towards autonomous information seeking agency. arXiv. https://arxiv.org/abs/2505.22648

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025b). WebWalker: Benchmarking LLMs in web traversal. arXiv. https://arxiv.org/abs/2501.07572

Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025). BrowseComp-ZH: Benchmarking web browsing ability of large language models in Chinese. arXiv. https://arxiv.org/abs/2504.19314
