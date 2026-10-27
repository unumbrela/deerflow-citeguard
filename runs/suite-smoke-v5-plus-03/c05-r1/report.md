# Systematic Literature Review: Deep Research

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: deep research, cs.CL, published between 2023-11-24 and 2025-11-23
**Citation format**: APA 7th edition

## Executive Summary

The literature on deep research agents reveals a rapidly evolving field focused on empowering large language models with autonomous web browsing and information-seeking capabilities. Recent work emphasizes benchmarking agent performance on challenging multi-hop retrieval tasks, developing training methodologies using reinforcement learning, and creating frameworks for systematic evaluation. The surveyed papers collectively demonstrate that deep research agents significantly outperform standard retrieval-augmented generation and direct reasoning approaches, with performance scaling predictably with test-time compute. However, challenges remain in confidence calibration, multimodal processing, and handling long-horizon reasoning tasks without context degradation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query `deep research`, filtered to category cs.CL, published between 2023-11-24 and 2025-11-23. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; 0 papers had only an abstract), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Screening flow**: Identified by search: 50 papers; added from references: 89 papers; shortlisted: 30 papers; screened: 30 papers; included: 10 papers (6 from reference expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmarking Deep Research Capabilities

A dominant thread in recent literature focuses on creating challenging benchmarks to evaluate deep research agents. Four papers introduce benchmarks specifically designed to test multi-hop web browsing and information retrieval capabilities. Wei et al. (2025) present BrowseComp, a benchmark of 1,266 questions requiring persistent web navigation to find hard-to-find, deeply entangled information [E23]. Zhou et al. (2025) extend this work to Chinese with BrowseComp-ZH, containing 289 multi-hop questions across 11 domains [E7]. Wu et al. (2025a) introduce WebWalkerQA for benchmarking LLMs in web traversal tasks [E15]. Du et al. (2025) propose DeepResearch Bench with 100 PhD-level research tasks across 22 fields, along with RACE and FACT evaluation frameworks [E19]. These benchmarks consistently reveal that even state-of-the-art agents struggle with complex multi-hop retrieval, with accuracy often below 50% on the most challenging tasks.

### Theme 2: Reinforcement Learning for Training Deep Research Agents

Multiple papers demonstrate that reinforcement learning is crucial for training effective deep research agents. Jin et al. (2025) introduce Search-R1, an RL framework enabling LLMs to interleave self-reasoning with real-time search engine interactions, achieving 24% and 20% average relative improvement on 7B and 3B models respectively [E31]. Li et al. (2025) train WebThinker using RL-based iterative online DPO, with the RL-trained WebThinker-32B-RL achieving state-of-the-art among 32B models on all benchmarks [E27]. Wu et al. (2025b) propose WebSailor with Duplicating Sampling Policy Optimization (DUPO) for efficient RL training, achieving performance on par with top-tier proprietary agents. Wu et al. (2025c) use a four-stage approach including supervised fine-tuning and on-policy RL for WebDancer, showing substantial gains over vanilla ReAct baselines [E1]. Qiao et al. (2025) employ RL in their WebResearcher system, demonstrating state-of-the-art performance across diverse deep-research benchmarks [E6]. The consensus across these works is that RL training provides significant improvements over supervised fine-tuning alone.

### Theme 3: Test-Time Compute and Performance Scaling

A key finding across multiple papers is that deep research performance scales predictably with test-time compute. Wei et al. (2025) demonstrate that BrowseComp performance scales smoothly as a function of test-time compute used [E24], with best-of-N and voting methods improving Deep Research performance by 15% to 25% compared to single attempts [E26]. This scaling relationship suggests that investing more computational resources at inference time yields predictable improvements in agent performance on complex information-seeking tasks.

### Theme 4: Architecture and Training Methodologies

Recent work explores diverse architectural approaches and training methodologies for deep research agents. Li et al. (2025) propose WebThinker with a Deep Web Explorer module and Autonomous Think-Search-and-Draft strategy, finding that WebThinker consistently outperforms direct reasoning and standard RAG across all model sizes [E29]. Tao et al. (2025) introduce WebShaper, a formalization-driven data synthesis framework using set theory and Knowledge Projections for precise control over reasoning structure, achieving state-of-the-art performance on GAIA and WebWalkerQA [E11], and demonstrating that reinforcement learning training provides significant performance improvements over SFT alone [E13]. Qiao et al. (2025) reformulate deep research as a Markov Decision Process with periodic consolidation to address context suffocation and noise contamination [E5]. These architectural innovations consistently outperform baseline approaches, with formalization-based methods showing particular promise for generating high-quality training data.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that deep research agents with browsing capabilities significantly outperform standard retrieval-augmented generation and direct reasoning approaches, with Li et al. (2025) showing WebThinker consistently outperforms direct reasoning and standard RAG across all model sizes [E29]. There is strong agreement that reinforcement learning is essential for training effective agents, with RL-trained models consistently outperforming supervised-only baselines, as Tao et al. (2025) demonstrate that reinforcement learning training provides significant performance improvements over SFT alone [E13]. The literature also agrees that multi-round retrieval systems achieve significantly higher accuracy than single-retrieval systems, with Zhou et al. (2025) finding multi-round retrieval systems achieve significantly higher accuracy than single-retrieval systems [E8], and that models with reasoning capabilities show substantial performance gains over those without [E9].

**Disagreements**: An interesting tension exists regarding the value of search capabilities for certain models. Zhou et al. (2025) report that enabling search for DeepSeek-R1 causes performance decline from 23.2% to 7.6% [E10], suggesting that search integration may harm performance for some model architectures. This contrasts with the generally positive findings about search integration in other papers. Additionally, Wei et al. (2025) find that models with browsing capabilities exhibit higher calibration error, suggesting web tools may increase confidence in incorrect answers [E25], raising questions about the trade-offs between capability and reliability.

## Gaps and Open Questions

The collective literature reveals several important gaps. Multiple papers note limitations in multimodal processing: Li et al. (2025) explicitly state that WebThinker cannot process multimodal information such as images and videos [E30], and currently supports only a limited set of tools. Wei et al. (2025) highlight that Deep Research struggles with confidence calibration and often fails to convey uncertainty accurately [E25]. Qiao et al. (2025) address the problem of context suffocation in long-horizon agents, noting that mono-contextual systems suffer from progressive degradation due to context bloat [E5]. Wu et al. (2025b) identify that filtering training trajectories to under 32k tokens may cap the model's ability to tackle more complex problems, and that RL processes are limited due to inefficiency of synchronous RL frameworks [E37]. The literature also notes that even best-performing agents do not surpass 40% accuracy on the most challenging benchmarks [E17], indicating substantial room for improvement.

## Per-Paper Annotations

### Wei et al. (2025)

**Research question**: How well can AI agents persistently browse the internet to search for hard-to-find, deeply entangled information?
**Methodology**: The authors present BrowseComp, a benchmark of 1,266 questions requiring persistent web navigation to find hard-to-find information. They evaluated multiple OpenAI models with and without browsing capabilities and analyzed performance scaling with test-time compute.
**Key findings**:
- Deep Research significantly outperforms all other models on BrowseComp, solving around half of the problems [E23]
- BrowseComp performance scales smoothly as a function of test-time compute used [E24]
- Models with browsing capabilities exhibit higher calibration error, suggesting web tools may increase confidence in incorrect answers [E25]
- Best-of-N and voting methods improve Deep Research performance by 15% to 25% compared to single attempt [E26]
**Limitations**: Models with browsing capabilities exhibit higher calibration error and struggle to convey uncertainty accurately; Deep Research struggles with confidence calibration and often fails to convey uncertainty accurately at present.

### Li et al. (2025)

**Research question**: How can large reasoning models be empowered to autonomously search the web, navigate among web pages, and draft comprehensive research reports?
**Methodology**: The authors propose WebThinker, a deep research agent with a Deep Web Explorer module and Autonomous Think-Search-and-Draft strategy, trained with RL-based iterative online DPO. They evaluated on complex reasoning benchmarks (GPQA, GAIA, WebWalkerQA, HLE) and scientific report generation tasks (Glaive).
**Key findings**:
- RL-trained WebThinker-32B-RL achieves state-of-the-art among 32B models on all benchmarks [E27]
- WebThinker achieves top overall score on scientific report generation, surpassing RAG baselines and Gemini-Deep Research [E28]
- WebThinker consistently outperforms direct reasoning and standard RAG across all model sizes [E29]
- WebThinker cannot process multimodal information such as images and videos [E30]
**Limitations**: WebThinker cannot process multimodal information such as images and videos; it currently supports only a limited set of tools; extending to support GUI-based web exploration would enable handling more complex interactive tasks.

### Jin et al. (2025)

**Research question**: How can LLMs be trained to autonomously generate search queries during step-by-step reasoning with real-time retrieval?
**Methodology**: The authors introduce Search-R1, an RL framework that enables LLMs to interleave self-reasoning with real-time search engine interactions, using retrieved token masking for stable training and outcome-based rewards. They evaluated on seven QA datasets.
**Key findings**:
- Search-R1 consistently outperforms baseline methods with 24% and 20% average relative improvement on 7B and 3B models [E31]
- Search-R1 surpasses RL-based training without retrieval by incorporating search into LLM reasoning [E32]
- Larger models are better at learning search, with 7B model showing much larger performance gap than 3B model [E33]
**Limitations**: Future work can explore expanding Search-R1 to support broader search strategies, including more sophisticated reward mechanisms, dynamic retrieval adjustments based on uncertainty, and integration with diverse information sources beyond search.

### Wu et al. (2025b)

**Research question**: How can open-source web agents be trained to achieve superhuman reasoning capabilities for navigating vast information landscapes with extreme uncertainty?
**Methodology**: The authors propose WebSailor, a post-training methodology using structured sampling for high-uncertainty tasks, RFT cold start, and Duplicating Sampling Policy Optimization (DUPO) for efficient RL training. They evaluated on BrowseComp-en/zh, GAIA, and XbenchDeepSearch.
**Key findings**:
- WebSailor-7B achieves 6.7 accuracy on BrowseComp-en, outperforming agents built on larger 32B models [E34]
- WebSailor-72B achieves performance on par with Doubao, a top-tier proprietary agent, on BrowseComp-zh [E35]
- RL training brings notable improvements across all benchmarks, with most significant gains on BrowseComp-en/zh [E36]
- RFT cold start yields significantly superior final converged performance compared to direct RL training [E37]
**Limitations**: Filtering training trajectories to under 32k tokens may cap the model's ability to tackle more complex problems; WebSailor can exhibit over-thinking on simple questions; RL process is limited to 50 steps due to inefficiency of synchronous RL framework.

### Zhou et al. (2025)

**Research question**: How well do large language models and AI search systems perform on web browsing and reasoning tasks in the Chinese information environment?
**Methodology**: Created BrowseComp-ZH, a benchmark with 289 multi-hop questions across 11 domains, reverse-engineered from verifiable answers with two-stage quality control. Evaluated over 20 models and AI search products.
**Key findings**:
- OpenAI's DeepResearch achieved the highest accuracy (42.9%) on BrowseComp-ZH, followed by O1 (29.1%) and Gemini-2.5-Pro (27.3%) [E7]
- Multi-round retrieval systems achieve significantly higher accuracy than single-retrieval systems [E8]
- Models with reasoning capabilities show substantial performance gains over those without [E9]
- Enabling search for DeepSeek-R1 causes performance decline from 23.2% to 7.6% [E10]
**Limitations**: The dataset is relatively small; answer uniqueness cannot be fully guaranteed due to the dynamic nature of the web.

### Tao et al. (2025)

**Research question**: How can high-quality training data for information-seeking agents be synthesized to address structural inconsistencies in existing information-driven approaches?
**Methodology**: Proposed WebShaper, a formalization-driven IS data synthesis framework using set theory and Knowledge Projections for precise control over reasoning structure, with agentic Expander for multi-step expansion.
**Key findings**:
- WebShaper achieves state-of-the-art performance on GAIA and WebWalkerQA among open-sourced methods [E11]
- WebShaper-enabled models significantly outperform baseline datasets across all backbone architectures [E12]
- Reinforcement learning training provides significant performance improvements over SFT alone [E13]
- Formalization language excels natural language in data synthesis across all backbones [E14]
**Limitations**: Not stated.

### Wu et al. (2025a)

**Research question**: How well can large language models traverse websites to extract high-quality data for complex, multi-layered information-seeking tasks?
**Methodology**: Introduced WebWalkerQA benchmark and WebWalker, a multi-agent framework using explore-critic paradigm to mimic human-like web navigation. Evaluated nine models including closed-source and open-source LLMs.
**Key findings**:
- WebWalker framework outperforms Reflexion and ReAct baselines [E15]
- Closed-source models outperform open-source models in performance and efficiency [E16]
- Even best-performing WebWalker with GPT-4o does not surpass 40% accuracy [E17]
- Larger model sizes lead to enhanced long-range information-seeking ability [E18]
**Limitations**: Not stated.

### Du et al. (2025)

**Research question**: How can deep research agents be systematically evaluated for their report generation and web retrieval capabilities?
**Methodology**: Created DeepResearch Bench with 100 PhD-level research tasks across 22 fields, and proposed RACE (reference-based) and FACT (citation-based) evaluation frameworks validated against human expert judgments.
**Key findings**:
- Gemini-2.5-Pro Deep Research demonstrates leading overall performance on RACE framework [E19]
- Deep Research Agents include more Effective Citations than LLMs with Search Tools [E20]
- RACE framework exhibits strongest human consistency, outperforming vanilla baseline [E21]
- Gemini 2.5 Pro Preview achieves best performance as Judge LLM with competitive cost [E22]
**Limitations**: Not stated.

### Wu et al. (2025c)

**Research question**: How to build end-to-end agentic information seeking agents from a data-centric and training-stage perspective?
**Methodology**: Four-stage approach: browsing data construction, trajectories sampling, supervised fine-tuning for cold start, and reinforcement learning for enhanced generalisation, instantiated in ReAct-based WebDancer agent.
**Key findings**:
- WebDancer shows substantial gains over vanilla ReAct baseline across different model scales and surpasses GPT-4o in best-case scenario [E1]
- The two-stage training pipeline combining SFT and on-policy RL achieves strong performance on GAIA and WebWalkerQA benchmarks [E2]
**Limitations**: Currently integrates only two basic information-seeking tools; experiments focus on short-answer tasks; RL stage can only utilize small subset due to computational constraints; RL phase incurs substantial computational and time overhead; hallucinations may occur in tool invocation and over-action may arise during reasoning.

### Qiao et al. (2025)

**Research question**: How to build deep-research agents that overcome context suffocation and noise contamination in mono-contextual approaches?
**Methodology**: Two key components: IterResearch paradigm reformulating deep research as Markov Decision Process with periodic consolidation, and WebFrontier scalable data synthesis engine generating training data through tool-augmented complexity escalation.
**Key findings**:
- WebResearcher demonstrates state-of-the-art performance across diverse deep-research benchmarks, significantly outperforming both larger models and existing deep-research systems [E6]
- On Humanity's Last Exam (HLE), WebResearcher-heavy achieves 36.7% accuracy, dramatically outperforming all systems including DeepSeek-V3.1 (29.8%), OpenAI Deep Research (26.6%), and Gemini Deep Research (26.9%) [E3]
- On BrowseComp-en, WebResearcher-heavy achieves 51.7% accuracy, matching OpenAI's Deep Research (51.5%) while vastly exceeding all open-source alternatives [E4]
- By periodically reconstructing the workspace and synthesizing findings, WebResearcher maintains consistent reasoning quality throughout extended research processes, whereas mono-contextual systems suffer from progressive degradation due to context bloat [E5]
**Limitations**: Not stated.

## References

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A comprehensive benchmark for deep research agents. arXiv. https://arxiv.org/abs/2506.11763

Jin, B., Zeng, H., Yue, Z., Yoon, J., Arik, S., Wang, D., Zamani, H., & Han, J. (2025). Search-R1: Training LLMs to reason and leverage search engines with reinforcement learning. arXiv. https://arxiv.org/abs/2503.09516

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025). WebThinker: Empowering large reasoning models with deep research capability. arXiv. https://arxiv.org/abs/2504.21776

Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebResearcher: Unleashing unbounded reasoning capability in long-horizon agents. arXiv. https://arxiv.org/abs/2509.13309

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically data synthesizing via information-seeking formalization. arXiv. https://arxiv.org/abs/2507.15061

Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025). BrowseComp: A simple yet challenging benchmark for browsing agents. arXiv. https://arxiv.org/abs/2504.12516

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025a). WebWalker: Benchmarking LLMs in web traversal. arXiv. https://arxiv.org/abs/2501.07572

Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025c). WebDancer: Towards autonomous information seeking agency. arXiv. https://arxiv.org/abs/2505.22648

Wu, K., Zhang, Z., Yin, H., Zhang, L., Ou, L., Wu, J., Yin, W., Li, B., Tao, Z., Wang, X., Shen, W., Zhang, J., Zhang, D., Wu, X., Jiang, Y., Yan, M., Xie, P., Huang, F., & Zhou, J. (2025b). WebSailor: Navigating super-human reasoning for web agent. arXiv. https://arxiv.org/abs/2507.02592

Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025). BrowseComp-ZH: Benchmarking web browsing ability of large language models in Chinese. arXiv. https://arxiv.org/abs/2504.19314
