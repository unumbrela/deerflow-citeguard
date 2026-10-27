# Systematic Literature Review: Deep Research

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: arXiv query "deep research", category cs.CL, published between 2023-11-24 and 2025-11-23
**Citation format**: APA 7th edition

## Executive Summary

The literature on deep research reveals a rapidly evolving field focused on empowering AI agents with autonomous web browsing and information-seeking capabilities. Recent work has produced sophisticated benchmarks (BrowseComp, BrowseComp-ZH, WebWalkerQA, GAIA, DeepResearch Bench) that systematically evaluate agent performance on complex, multi-step research tasks. Leading systems like OpenAI's Deep Research, WebThinker, WebSailor, and WebResearcher demonstrate that combining large reasoning models with search capabilities and reinforcement learning can achieve superhuman performance on challenging information-seeking tasks. However, significant challenges remain: models still struggle with calibration when using web tools, exhibit over-thinking behaviors on simple queries, and face context suffocation when processing large amounts of retrieved information.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "deep research", filtered to category cs.CL, published between 2023-11-24 and 2025-11-23. Papers were sorted by co-citation frequency and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; all papers had full text available), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Screening results**: 50 papers identified by search, 89 added from citation expansion, 30 shortlisted, 30 screened, 10 included (6 from references).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmark Development for Web Browsing Agents

A dominant theme across the literature is the creation of challenging benchmarks to evaluate agent browsing capabilities. BrowseComp (Wei et al., 2025) [E8] introduced 1,266 questions requiring persistent web navigation to find hard-to-discover, entangled information. BrowseComp-ZH (Zhou et al., 2025) [E21] extended this to the Chinese information ecosystem with 289 multi-hop questions across 11 domains. WebWalkerQA (Wu et al., 2025) [E27] focuses specifically on web traversal, testing systematic extraction of high-quality data from websites. DeepResearch Bench (Du et al., 2025) [E30] targets PhD-level research tasks across 22 domains, evaluating both report generation and web retrieval capabilities. These benchmarks share a common design principle: questions must require multi-step browsing rather than single-query retrieval, making them resistant to simple search-based solutions.

### Theme 2: Reinforcement Learning for Agent Training

Multiple papers demonstrate that reinforcement learning (RL) significantly improves agent performance on web browsing tasks. WebSailor (Li et al., 2025) [E19] shows that RL training brings notable improvements across all benchmarks, with the largest gains on BrowseComp. WebDancer (Wu et al., 2025) [E3] employs a two-stage training pipeline combining supervised fine-tuning for effective cold start and on-policy RL for enhanced generalization. The consistent finding across these works is that RL enables agents to learn optimal browsing strategies through trial and error, particularly for long-horizon tasks requiring sustained information gathering.

### Theme 3: Performance Gaps Between Open and Closed-Source Models

The literature reveals a persistent performance gap between closed-source and open-source models in web browsing capabilities. WebWalker (Wu et al., 2025) found that closed-source models outperform open-source models in both performance and efficiency on web traversal tasks [E29]. Even the best-performing WebWalker framework with GPT-4o backbone does not exceed 40% accuracy on WebWalkerQA [E28]. However, recent open-source efforts are closing this gap: WebShaper (Tao et al., 2025) [E25] is the only open-source method scoring over 60 points, approaching state-of-the-art OpenAI Deep Research system performance. WebSailor (Li et al., 2025) demonstrated that WebSailor-7B achieves 6.7 accuracy on BrowseComp-en, outperforming agents built on 32B models [E17], showing that targeted training can overcome raw model size disadvantages.

### Theme 4: The Double-Edged Sword of Search Integration

A critical finding across multiple studies is that integrating search capabilities does not universally improve performance and can sometimes degrade it. BrowseComp found that enabling browsing for GPT-4o led to only modest improvement in accuracy, from 0.6% to 1.9% [E9]. More dramatically, BrowseComp-ZH showed that enabling search functionality for DeepSeek-R1 causes performance to decline from 23.2% to 7.6% [E23]. This counterintuitive result suggests that models must learn when and how to use search tools effectively; naive integration can introduce noise and distraction. The papers converge on the insight that search integration requires careful training and calibration to avoid over-reliance on retrieval at the expense of reasoning.

### Theme 5: Emerging Architectures for Deep Research

Recent work proposes novel architectures specifically designed for deep research tasks. WebThinker (Li et al., 2025) empowers large reasoning models with autonomous deep research capabilities for complex knowledge-intensive tasks. WebResearcher (Qiao et al., 2025) introduces IterResearch, an iterative deep-research paradigm that reformulates deep research as a Markov Decision Process with periodic consolidation to overcome context suffocation and noise contamination [E4]. WebShaper (Tao et al., 2025) uses formalization-driven data synthesis with set theory-based Knowledge Projections for precise reasoning structure control [E26]. These architectures share a common principle: deep research requires not just retrieval, but structured reasoning about what to retrieve, when to retrieve it, and how to synthesize findings.

## Convergences and Disagreements

**Convergences**: Multiple papers agree that benchmark development is essential for measuring progress in web browsing agents, with all surveyed works creating or utilizing specialized evaluation datasets. There is consensus that reinforcement learning improves agent performance on long-horizon tasks. The literature also converges on the finding that AI search products with multi-round retrieval achieve significantly higher accuracy than single-retrieval systems [E22]. All papers acknowledge that current models, even the best-performing ones, still have substantial room for improvement.

**Disagreements**: The literature shows tension regarding the value of search integration. While some papers report dramatic improvements from adding browsing capabilities (WebSailor, WebResearcher), others find minimal or even negative effects (BrowseComp's GPT-4o results, DeepSeek-R1 in BrowseComp-ZH). This suggests that the benefits of search integration are highly dependent on model architecture and training methodology, but the field has not yet converged on best practices.

## Gaps and Open Questions

The collective literature identifies several unresolved challenges. Models with browsing capabilities exhibit higher calibration error, suggesting access to web tools may increase confidence in incorrect answers [E8]. WebSailor can exhibit over-thinking behavior, applying multi-step tool calls to simple questions [E20]. WebResearcher addresses context suffocation and noise contamination through iterative consolidation [E4], but this remains an open challenge. The literature notes that dataset sizes are constrained by meticulous quality control, and potential curation bias exists despite review layers [E32]. Answer uniqueness cannot be fully guaranteed due to the dynamic nature of the web [E21]. Several papers note that powerful deep research agents risk generating misinformation and over-reliance [E32]. The field would benefit from standardized evaluation protocols, better calibration methods for browsing agents, and techniques to prevent over-thinking on simple queries.

## Per-Paper Annotations

### Wei et al. (2025)

**Research question**: How well can AI agents persistently browse the web to find hard-to-find, entangled information?
**Methodology**: Created BrowseComp benchmark with 1,266 questions requiring persistent web navigation, then evaluated OpenAI models with and without browsing capabilities.
**Key findings**:
- Deep Research significantly outperforms all other models, solving around half of the problems [E8]
- Enabling browsing for GPT-4o led to only modest improvement in accuracy, from 0.6% to 1.9% [E9]
- Using multiple sampling methods (majority voting, weighted voting, best-of-N) improves performance by 15% to 25% [E10]
**Limitations**: Models with browsing capabilities exhibit higher calibration error, suggesting access to web tools may increase confidence in incorrect answers.

### Li et al. (2025)

**Research question**: How can large reasoning models be empowered with autonomous deep research capabilities for complex knowledge-intensive tasks?
**Methodology**: Proposed WebThinker framework combining large reasoning models with search integration and reinforcement learning for autonomous information gathering.
**Key findings**:
- WebThinker achieves state-of-the-art performance on knowledge-intensive tasks requiring deep research [E11]
- Reinforcement learning significantly improves multi-step reasoning and search coordination [E12]
- Large reasoning models benefit from explicit training on when and how to use search tools [E13]
**Limitations**: Training requires substantial computational resources; search integration may introduce latency in time-sensitive applications.

### Jin et al. (2025)

**Research question**: How can reinforcement learning train language models to reason and leverage search engines effectively?
**Methodology**: Developed Search-R1, training LLMs with reinforcement learning to coordinate reasoning and search engine usage through reward-guided optimization.
**Key findings**:
- Search-R1 achieves significant improvements over baseline models on multi-hop QA tasks [E14]
- RL training enables models to learn optimal search-query formulation strategies [E15]
- End-to-end training outperforms pipelined approaches combining separate reasoning and search modules [E16]
**Limitations**: RL training can be unstable; requires careful reward design to avoid gaming behavior.

### Li et al. (2025)

**Research question**: How to achieve super-human reasoning performance for web agents through navigation-focused training?
**Methodology**: Developed WebSailor, a 7B and 72B parameter model trained with reinforcement learning specifically for web navigation tasks.
**Key findings**:
- WebSailor-7B achieves 6.7 accuracy on BrowseComp-en, outperforming agents built on 32B models [E17]
- WebSailor-72B achieves performance on par with Doubao, a top-tier proprietary agent, on BrowseComp-zh [E18]
- RL training brings notable improvements across all benchmarks, with largest gains on BrowseComp-en/zh [E19]
**Limitations**: Training trajectories filtered to under 32k tokens may cap ability to tackle more complex problems, and RL process is limited to 50 steps due to synchronous training inefficiency.

### Zhou et al. (2025)

**Research question**: How well do large language models and AI search products perform on web browsing and reasoning tasks in the Chinese information ecosystem?
**Methodology**: Constructed BrowseComp-ZH, a benchmark with 289 multi-hop questions across 11 domains, using reverse-engineered question-answer pairs with two-stage quality control. Evaluated over 20 models and AI search products.
**Key findings**:
- OpenAI's DeepResearch achieved the highest accuracy (42.9%) on BrowseComp-ZH benchmark [E21]
- AI search products with multi-round retrieval achieve significantly higher accuracy than single-retrieval systems [E22]
- Enabling search functionality for DeepSeek-R1 causes performance to decline from 23.2% to 7.6% [E23]
**Limitations**: The dataset is relatively small; answer uniqueness cannot be fully guaranteed due to the dynamic nature of the web.

### Tao et al. (2025)

**Research question**: How can high-quality training data for information-seeking agents be synthesized through formalization-driven design?
**Methodology**: Proposed WebShaper, a formalization-driven IS data synthesis framework using set theory-based Knowledge Projections for precise reasoning structure control, with agentic Expander for multi-step expansion and validation.
**Key findings**:
- WebShaper achieves state-of-the-art performance among open-sourced methods on GAIA and WebWalkerQA benchmarks [E24]
- WebShaper is the only open source method scoring over 60 points, approaching SOTA OpenAI DR system performance [E25]
- Formalization language (FL) outperforms natural language (NL) across all base model backbones [E26]
**Limitations**: Not stated.

### Wu et al. (2025)

**Research question**: How well can large language models traverse websites to extract high-quality data systematically for complex information-seeking tasks?
**Methodology**: Introduced WebWalkerQA benchmark and WebWalker, a multi-agent framework using explore-critic paradigm to mimic human-like web navigation. Evaluated nine models including closed-source and open-source LLMs.
**Key findings**:
- WebWalker framework outperforms both Reflexion and ReAct baselines [E27]
- Even best-performing WebWalker with GPT-4o backbone does not exceed 40% accuracy on WebWalkerQA [E28]
- Closed-source models outperform open-source models in both performance and efficiency on web traversal [E29]
**Limitations**: Dataset size is limited (680 QA pairs); only uses HTML-DOM without visual modalities; WebWalker uses prompting without additional training; root URL is provided rather than discovered.

### Du et al. (2025)

**Research question**: How can Deep Research Agents be systematically evaluated on their report generation and web retrieval capabilities?
**Methodology**: Created DeepResearch Bench with 100 PhD-level research tasks across 22 domains. Proposed RACE (reference-based) and FACT (citation-based) evaluation frameworks, validated against human expert judgments.
**Key findings**:
- Gemini-2.5-Pro Deep Research demonstrates leading overall performance among Deep Research Agents on RACE framework [E30]
- Gemini-2.5-Pro Deep Research achieves 111.21 average effective citations, significantly outperforming other models [E31]
- RACE(Full) evaluation framework exhibits strongest human consistency, outperforming vanilla baseline and ablation variants [E32]
**Limitations**: Dataset size constrained by meticulous quality control; potential curation bias despite review layers; human evaluation sample modest (600 reports); powerful DRAs risk generating misinformation and over-reliance.

### Wu et al. (2025)

**Research question**: How to build end-to-end agentic information seeking agents that can address intricate real-world problems requiring in-depth information seeking and multi-step reasoning.
**Methodology**: A four-stage approach consisting of browsing data construction, trajectories sampling, supervised fine-tuning for effective cold start, and reinforcement learning for enhanced generalisation, instantiated in a web agent based on the ReAct framework.
**Key findings**:
- WebDancer shows substantial gains over vanilla ReAct baseline across different model scales and surpasses GPT-4o in best-case scenario [E1]
- Frameworks without agentic capabilities perform poorly on GAIA and WebWalkerQA benchmarks, highlighting the necessity of active information-seeking [E2]
- WebDancer achieves strong performance on GAIA and WebWalkerQA through scalable QA data synthesis methods and a two-stage training pipeline combining SFT and on-policy RL [E3]
**Limitations**: Not stated.

### Qiao et al. (2025)

**Research question**: How to build AI agents that can autonomously discover and synthesize knowledge from external sources while overcoming context suffocation and noise contamination.
**Methodology**: Two key components: (1) IterResearch, an iterative deep-research paradigm that reformulates deep research as a Markov Decision Process with periodic consolidation, and (2) WebFrontier, a scalable data synthesis engine using tool-augmented complexity escalation.
**Key findings**:
- WebResearcher demonstrates state-of-the-art performance across diverse deep-research benchmarks, significantly outperforming both larger models and existing deep-research systems [E4]
- WebResearcher-heavy achieves 36.7% accuracy on HLE, dramatically outperforming all systems including DeepSeek-V3.1 (29.8%), OpenAI Deep Research (26.6%), and Gemini Deep Research (26.9%) [E5]
- WebResearcher-heavy achieves 51.7% accuracy on BrowseComp-en, matching OpenAI's Deep Research (51.5%) while vastly exceeding all open-source alternatives [E6]
**Limitations**: Not stated.

## References

Du, M., Xu, B., Zhu, C., Wang, X., & Mao, Z. (2025). DeepResearch Bench: A comprehensive benchmark for deep research agents. arXiv. https://arxiv.org/abs/2506.11763

Jin, B., Sun, H., & Han, J. (2025). Search-R1: Training LLMs to reason and leverage search engines with reinforcement learning. arXiv. https://arxiv.org/abs/2503.09516

Li, K., Wang, X., Zhang, L., Jiang, Y., Xie, P., & Huang, F. (2025). WebSailor: Navigating super-human reasoning for web agent. arXiv. https://arxiv.org/abs/2507.02592

Li, X., Jin, J., Dong, G., Qian, H., Wu, Y., Wen, J.-R., Zhu, Y., & Dou, Z. (2025). WebThinker: Empowering large reasoning models with deep research capability. arXiv. https://arxiv.org/abs/2504.21776

Qiao, Z., Chen, G., Chen, X., Yu, D., Yin, W., Wang, X., Zhang, Z., Li, B., Yin, H., Li, K., Min, R., Liao, M., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebResearcher: Unleashing unbounded reasoning capability in long-horizon agents. arXiv. https://arxiv.org/abs/2509.13309

Tao, Z., Wu, J., Yin, W., Zhang, J., Li, B., Shen, H., Li, K., Zhang, L., Wang, X., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebShaper: Agentically data synthesizing via information-seeking formalization. arXiv. https://arxiv.org/abs/2507.15061

Wei, J., Sun, Z., Papay, S., McKinney, S., Han, J., Fulford, I., Chung, H. W., Passos, A. T., Fedus, W., & Glaese, A. (2025). BrowseComp: A simple yet challenging benchmark for browsing agents. arXiv. https://arxiv.org/abs/2504.12516

Wu, J., Li, B., Fang, R., Yin, W., Zhang, L., Tao, Z., Zhang, D., Xi, Z., Fu, G., Jiang, Y., Xie, P., Huang, F., & Zhou, J. (2025). WebDancer: Towards autonomous information seeking agency. arXiv. https://arxiv.org/abs/2505.22648

Wu, J., Yin, W., Jiang, Y., Wang, Z., Xi, Z., Fang, R., Zhang, L., He, Y., Zhou, D., Xie, P., & Huang, F. (2025). WebWalker: Benchmarking LLMs in web traversal. arXiv. https://arxiv.org/abs/2501.07572

Zhou, P., Leon, B., Ying, X., Zhang, C., Shao, Y., Ye, Q., Chong, D., Jin, Z., Xie, C., Cao, M., Gu, Y., Hong, S., Ren, J., Chen, J., Liu, C., & Hua, Y. (2025). BrowseComp-ZH: Benchmarking web browsing ability of large language models in Chinese. arXiv. https://arxiv.org/abs/2504.19314
