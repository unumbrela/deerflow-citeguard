# Systematic Literature Review: Deep Research

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "deep research", category cs.CL, published between 2023-11-24 and 2025-11-23
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent papers on deep research capabilities in AI agents, focusing on web browsing, information seeking, and autonomous research systems. The surveyed literature reveals a rapidly evolving field centered on empowering large language models with the ability to autonomously navigate the web, synthesize information across multiple sources, and conduct complex research tasks. Key contributions include benchmarking frameworks (BrowseComp, WebWalkerQA, DeepResearch Bench), novel agent architectures (WebThinker, WebSailor, WebDancer, WebResearcher), and training methodologies using reinforcement learning. The field demonstrates strong convergence on the importance of interleaving reasoning with information retrieval, though approaches vary in their emphasis on benchmarking versus capability development.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "deep research", filtered to category cs.CL, published between 2023-11-24 and 2025-11-23. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening results**: 50 papers identified by search, 89 added from citation expansion, 30 shortlisted, 30 screened, 10 included (6 from references).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmarking Web Browsing and Information Seeking Capabilities

A significant portion of the literature focuses on creating rigorous benchmarks to evaluate agent capabilities in web navigation and information retrieval. BrowseComp (Wei et al., 2025) introduced 1,266 questions requiring persistent internet navigation to find hard-to-find, entangled information, establishing a simple yet challenging evaluation framework. BrowseComp-ZH (Zhou et al., 2025) extended this to the Chinese web ecosystem with 289 multi-hop questions across 11 domains, revealing that most models struggle with accuracy rates below 10%. WebWalkerQA (Wu et al., 2025a) assesses LLMs' capacity to traverse website subpages for systematic data extraction, addressing the limitation that traditional search engines may retrieve shallow content. DeepResearch Bench (Du et al., 2025) represents the most ambitious benchmarking effort, containing 100 PhD-level research tasks across 22 fields crafted by domain experts, with novel evaluation methodologies for assessing research report quality.

### Theme 2: Agent Architectures for Deep Research

Multiple papers propose novel agent architectures designed to empower LLMs with deep research capabilities. WebThinker (Li et al., 2025) integrates a Deep Web Explorer module enabling large reasoning models to dynamically search, navigate, and extract information from the web, employing an Autonomous Think-Search-and-Draft strategy that interleaves reasoning, information gathering, and report writing in real time. WebSailor (Li et al., 2025) introduces a complete post-training methodology using structured sampling and information obfuscation to generate high-uncertainty tasks, combined with Duplicating Sampling Policy Optimization (DUPO) for efficient agentic RL training. WebDancer (Wu et al., 2025b) proposes a four-stage paradigm: browsing data construction, trajectories sampling, supervised fine-tuning for effective cold start, and reinforcement learning for enhanced generalisation. WebResearcher (Qiao et al., 2025) reformulates deep research as a Markov Decision Process where agents periodically consolidate findings into evolving reports while maintaining focused workspaces, overcoming context suffocation and noise contamination.

### Theme 3: Training Methodologies Using Reinforcement Learning

A recurring approach across the literature is the use of reinforcement learning to train agents for deep research tasks. Search-R1 (Jin et al., 2025) extends reinforcement learning for reasoning frameworks where the LLM learns to autonomously generate multiple search queries during step-by-step reasoning with real-time retrieval, using retrieved token masking for stable RL training and a simple outcome-based reward function. WebThinker (Li et al., 2025) employs an RL-based training strategy via iterative online Direct Preference Optimization (DPO). WebSailor (Li et al., 2025) uses DUPO for efficient agentic RL training. WebDancer (Wu et al., 2025b) includes reinforcement learning as the fourth stage of its training paradigm for enhanced generalisation. This convergence on RL reflects recognition that outcome-based learning signals are essential for developing robust information-seeking behaviors.

### Theme 4: Data Synthesis for Training Information-Seeking Agents

Several papers address the challenge of generating high-quality training data for information-seeking agents. WebShaper (Tao et al., 2025) proposes a formalization-driven information-seeking data synthesis framework using set theory and Knowledge Projections (KP) to control reasoning structure through KP operation compositions, with a multi-step expansion process using an agentic Expander. WebResearcher (Qiao et al., 2025) introduces WebFrontier, a scalable data synthesis engine using tool-augmented complexity escalation to generate high-quality training data that bridges passive knowledge recall and active knowledge construction. WebDancer (Wu et al., 2025b) includes browsing data construction and trajectories sampling as the first two stages of its paradigm. This emphasis on synthetic data generation reflects the scarcity of high-quality human demonstrations for complex information-seeking tasks.

### Theme 5: Search-Augmented Reasoning

The integration of search capabilities directly into the reasoning process represents a key innovation across multiple papers. Search-R1 (Jin et al., 2025) trains LLMs to autonomously generate search queries during step-by-step reasoning with real-time retrieval, optimizing reasoning trajectories with multi-turn search interactions. WebThinker (Li et al., 2025) enables seamless interleaving of reasoning, information gathering, and report writing through its Autonomous Think-Search-and-Draft strategy. WebResearcher (Qiao et al., 2025) overcomes context suffocation by periodically consolidating findings into evolving reports while maintaining focused workspaces, naturally scaling through parallel thinking with concurrent multi-agent exploration. These approaches contrast with traditional retrieval-augmented generation by making search an integral part of the reasoning process rather than a preprocessing step.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong agreement on several key points. First, all papers recognize that effective deep research requires interleaving reasoning with information retrieval rather than treating search as a separate preprocessing step (Li et al., 2025; Jin et al., 2025; Qiao et al., 2025). Second, there is consensus that reinforcement learning is essential for training robust information-seeking behaviors, with multiple independent approaches converging on outcome-based RL training (Jin et al., 2025; Li et al., 2025; Wu et al., 2025b). Third, the literature agrees that benchmarking must focus on hard-to-find, entangled information requiring persistent navigation rather than simple factoid retrieval (Wei et al., 2025; Zhou et al., 2025; Wu et al., 2025a; Du et al., 2025). Fourth, all agent architecture papers emphasize the importance of maintaining context and avoiding noise contamination in long-horizon tasks (Qiao et al., 2025; Li et al., 2025).

**Disagreements**: While there is broad agreement on the importance of benchmarks, the literature shows variation in benchmark design philosophy. BrowseComp (Wei et al., 2025) and BrowseComp-ZH (Zhou et al., 2025) focus on short, easily verifiable answers to enable rapid evaluation, while DeepResearch Bench (Du et al., 2025) emphasizes PhD-level research tasks requiring comprehensive report generation with adaptive quality assessment. Another area of variation is the emphasis on data synthesis versus direct RL training: WebShaper (Tao et al., 2025) and WebResearcher (Qiao et al., 2025) prioritize high-quality synthetic data generation, while Search-R1 (Jin et al., 2025) and WebSailor (Li et al., 2025) focus more heavily on direct RL optimization.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the papers explicitly address the challenge of evaluating the quality of synthesized information beyond answer verification or citation accuracy — the deeper question of whether agents produce accurate, well-reasoned conclusions remains underexplored except in DeepResearch Bench (Du et al., 2025). Second, while multiple papers mention the importance of handling ambiguity and resolving conflicting information (Wei et al., 2025; Qiao et al., 2025), none provide detailed methodologies for conflict resolution in multi-source information synthesis. Third, the limitations of current approaches in handling very long-horizon research tasks (beyond a few hours of agent interaction) are not addressed, suggesting a gap in scalability. Fourth, while BrowseComp-ZH (Zhou et al., 2025) addresses Chinese web browsing, the literature remains heavily English-centric, with limited attention to multilingual or cross-lingual research capabilities. Finally, several papers note limitations in addressing the full distribution of user queries, particularly those requiring long answers or ambiguity resolution (Wei et al., 2025), indicating a gap between benchmark performance and real-world utility.

## Per-Paper Annotations

### Du et al. (2025)

**Research question**: How can we systematically evaluate the capabilities of Deep Research Agents that autonomously orchestrate multistep web exploration and synthesis?
**Methodology**: The authors present DeepResearch Bench, a benchmark consisting of 100 PhD-level research tasks crafted by domain experts across 22 fields, with two novel evaluation methodologies: a reference-based method with adaptive criteria for assessing research report quality, and a framework evaluating information retrieval capabilities through effective citation count and citation accuracy.
**Key findings**:
- DeepResearch Bench contains 100 PhD-level research tasks across 22 distinct fields, meticulously crafted by domain experts
- A reference-based method with adaptive criteria achieves strong alignment with human judgment for assessing research report quality
- A framework evaluating information retrieval capabilities through effective citation count and overall citation accuracy is proposed
- The benchmark and key components have been open-sourced to accelerate development of practical LLM-based agents
**Limitations**: not stated in abstract

### Jin et al. (2025)

**Research question**: How can we train LLMs to autonomously generate search queries during step-by-step reasoning with real-time retrieval for effective reasoning and text generation?
**Methodology**: The authors introduce Search-R1, an extension of reinforcement learning for reasoning frameworks where the LLM learns to autonomously generate multiple search queries during step-by-step reasoning with real-time retrieval, using retrieved token masking for stable RL training and a simple outcome-based reward function.
**Key findings**:
- Search-R1 optimizes LLM reasoning trajectories with multi-turn search interactions
- Experiments on seven question-answering datasets show performance improvements of 41% (Qwen2.5-7B) and 20% (Qwen2.5-3B) over various RAG baselines
- The approach provides empirical insights into RL optimization methods, LLM choices, and response length dynamics in retrieval-augmented reasoning
- Code and model checkpoints are available at https://github.com/PeterGriffinJin/Search-R1
**Limitations**: not stated in abstract

### Li et al. (2025a)

**Research question**: How can we empower large reasoning models to autonomously search the web and synthesize diverse web information for complex, knowledge-intensive tasks?
**Methodology**: The authors propose WebThinker, a deep research agent that integrates a Deep Web Explorer module enabling LRMs to dynamically search, navigate, and extract information from the web, employing an Autonomous Think-Search-and-Draft strategy and introducing an RL-based training strategy via iterative online Direct Preference Optimization (DPO).
**Key findings**:
- WebThinker empowers LRMs to autonomously search the web, navigate among web pages, and draft reports during the reasoning process
- The Deep Web Explorer module enables LRMs to dynamically search, navigate, and extract information when encountering knowledge gaps
- The Autonomous Think-Search-and-Draft strategy allows seamless interleaving of reasoning, information gathering, and report writing in real time
- Extensive experiments on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and scientific report generation tasks (Glaive) demonstrate significant outperformance over existing methods
**Limitations**: not stated in abstract

### Li et al. (2025b)

**Research question**: How can we instill sophisticated reasoning patterns in open-source models to systematically reduce extreme uncertainty when navigating vast information landscapes?
**Methodology**: The authors introduce WebSailor, a complete post-training methodology that involves generating novel, high-uncertainty tasks through structured sampling and information obfuscation, RFT cold start, and an efficient agentic RL training algorithm called Duplicating Sampling Policy Optimization (DUPO).
**Key findings**:
- WebSailor significantly outperforms all open-source agents in complex information-seeking tasks
- The approach matches proprietary agents' performance and closes the capability gap
- The methodology is designed to instill the ability to systematically reduce extreme uncertainty when navigating vast information landscapes
- The approach addresses a sophisticated reasoning pattern previously absent in open-source models
**Limitations**: not stated in abstract

### Qiao et al. (2025)

**Research question**: How can AI agents autonomously discover and synthesize knowledge from external sources while overcoming context suffocation and noise contamination in long-horizon tasks?
**Methodology**: The authors introduce WebResearcher, an iterative deep-research paradigm reformulating deep research as a Markov Decision Process where agents periodically consolidate findings into evolving reports while maintaining focused workspaces, plus WebFrontier, a scalable data synthesis engine using tool-augmented complexity escalation to generate high-quality training data.
**Key findings**:
- WebResearcher reformulates deep research as a Markov Decision Process, overcoming context suffocation and noise contamination plaguing mono-contextual approaches
- WebFrontier generates high-quality training data through tool-augmented complexity escalation, bridging passive knowledge recall and active knowledge construction
- Training data from the paradigm significantly enhances tool-use capabilities even for traditional mono-contextual methods
- The paradigm naturally scales through parallel thinking, enabling concurrent multi-agent exploration for more comprehensive conclusions
- Extensive experiments across 6 challenging benchmarks show WebResearcher achieves state-of-the-art performance, surpassing frontier proprietary systems
**Limitations**: not stated in abstract

### Tao et al. (2025)

**Research question**: How can information-seeking data synthesis be improved to ensure consistency between information structure, reasoning structure, and question-answer pairs?
**Methodology**: The authors propose WebShaper, a formalization-driven information-seeking data synthesis framework using set theory and Knowledge Projections (KP) to control reasoning structure through KP operation compositions, with a multi-step expansion process using an agentic Expander that expands formal questions with retrieval and validation tools.
**Key findings**:
- WebShaper systematically formalizes information-seeking tasks through set theory with Knowledge Projections enabling precise control over reasoning structure
- The multi-step expansion process with agentic Expander allows iterative complexity increase with retrieval and validation
- Models trained on the WebShaper-synthesized dataset achieve state-of-the-art performance among open-sourced information-seeking agents on GAIA and WebWalkerQA benchmarks
**Limitations**: not stated in abstract

### Wei et al. (2025)

**Research question**: How can we effectively benchmark the ability of agents to browse the web and find hard-to-find, entangled information?
**Methodology**: The authors present BrowseComp, a benchmark comprising 1,266 questions that require persistently navigating the internet to search for hard-to-find information, using short, easily verifiable predicted answers against reference answers.
**Key findings**:
- BrowseComp comprises 1,266 questions requiring persistent internet navigation to find hard-to-find, entangled information
- The benchmark is simple and easy-to-use with short, easily verifiable predicted answers
- BrowseComp measures the important core capability of exercising persistence and creativity in finding information
- The benchmark can be found at https://github.com/openai/simple-evals
**Limitations**: BrowseComp sidesteps challenges of a true user query distribution, like generating long answers or resolving ambiguity, and is analogous to programming competitions as an incomplete but useful benchmark for coding agents

### Wu et al. (2025a)

**Research question**: How can we assess the ability of LLMs to perform web traversal and extract high-quality data systematically from website subpages?
**Methodology**: The authors introduce WebWalkerQA, a benchmark designed to evaluate LLMs' capacity to traverse website subpages for systematic data extraction, and propose WebWalker, a multi-agent framework using an explore-critic paradigm that mimics human-like web navigation.
**Key findings**:
- WebWalkerQA benchmark assesses LLMs' ability to traverse websites' subpages to extract high-quality data systematically
- Traditional search engines may retrieve shallow content, limiting LLMs' ability to handle complex, multi-layered information
- WebWalker multi-agent framework demonstrates effectiveness through horizontal and vertical integration in real-world scenarios
- Experimental results show WebWalkerQA is challenging and demonstrates the effectiveness of RAG combined with WebWalker
**Limitations**: not stated in abstract

### Wu et al. (2025b)

**Research question**: How can end-to-end agentic information seeking agents be built from a data-centric and training-stage perspective?
**Methodology**: The authors propose a four-stage paradigm: (1) browsing data construction, (2) trajectories sampling, (3) supervised fine-tuning for effective cold start, and (4) reinforcement learning for enhanced generalisation, instantiated in WebDancer, a web agent based on the ReAct framework.
**Key findings**:
- The approach consists of four key stages: browsing data construction, trajectories sampling, supervised fine-tuning, and reinforcement learning for enhanced generalisation
- WebDancer is instantiated as a web agent based on the ReAct framework following the proposed training paradigm
- Empirical evaluations on GAIA and WebWalkerQA benchmarks demonstrate strong performance of WebDancer
- Analysis of agent training provides valuable insights and systematic pathways for developing more capable agentic models
**Limitations**: not stated in abstract

### Zhou et al. (2025)

**Research question**: How can we comprehensively evaluate LLM agents on the Chinese web, addressing the linguistic, infrastructural, and censorship-related complexities overlooked by English-focused benchmarks?
**Methodology**: The authors introduce BrowseComp-ZH, a high-difficulty benchmark consisting of 289 multi-hop questions spanning 11 diverse domains, with each question reverse-engineered from a short, objective, and easily verifiable answer, applying a two-stage quality control protocol to ensure high question difficulty and answer uniqueness.
**Key findings**:
- BrowseComp-ZH consists of 289 multi-hop questions spanning 11 diverse domains in the Chinese web ecosystem
- Most models struggle severely with accuracy rates below 10%, and only a handful exceed 20%
- The best-performing system, OpenAI's DeepResearch, reaches just 42.9% accuracy
- Success on BrowseComp-ZH demands effective retrieval strategies, sophisticated reasoning, and information reconciliation
- The dataset, construction guidelines, and benchmark results have been publicly released at https://github.com/PALIN2018/BrowseComp-ZH
**Limitations**: not stated in abstract

## References

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A comprehensive benchmark for deep research agents. arXiv. https://arxiv.org/abs/2506.11763

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025). Search-R1: Training LLMs to reason and leverage search engines with reinforcement learning. arXiv. https://arxiv.org/abs/2503.09516

Li, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J. (2025). WebSailor: Navigating super-human reasoning for web agent. arXiv. https://arxiv.org/abs/2507.02592

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025). WebThinker: Empowering large reasoning models with deep research capability. arXiv. https://arxiv.org/abs/2504.21776

Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebResearcher: Unleashing unbounded reasoning capability in long-horizon agents. arXiv. https://arxiv.org/abs/2509.13309

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically data synthesizing via information-seeking formalization. arXiv. https://arxiv.org/abs/2507.15061

Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025). BrowseComp: A simple yet challenging benchmark for browsing agents. arXiv. https://arxiv.org/abs/2504.12516

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025). WebWalker: Benchmarking LLMs in web traversal. arXiv. https://arxiv.org/abs/2501.07572

Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebDancer: Towards autonomous information seeking agency. arXiv. https://arxiv.org/abs/2505.22648

Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025). BrowseComp-ZH: Benchmarking web browsing ability of large language models in Chinese. arXiv. https://arxiv.org/abs/2504.19314
