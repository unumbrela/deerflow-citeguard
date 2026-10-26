# Systematic Literature Review: Deep Research

**Date**: 2025-11-26
**Papers surveyed**: 10
**Scope**: arXiv query "deep research", category cs.CL, published between 2023-11-24 and 2025-11-24
**Citation format**: APA 7th edition

## Executive Summary

The deep research field has rapidly evolved from a loosely defined concept into a structured research area with formal definitions, specialized benchmarks, and sophisticated agent architectures. The ten surveyed papers collectively reveal a field maturing through three parallel tracks: (1) formal task characterization and benchmarking, (2) architectural innovation in agent systems, and (3) optimization techniques for training and evaluation. A strong consensus emerges that deep research requires high fan-out reasoning-intensive exploration rather than merely generating lengthy outputs. The literature shows significant progress in enterprise applications, personalization, and cost-efficient open models, though challenges remain in evaluation fairness, computational efficiency, and handling dynamic real-world contexts.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-11-26 using the query "deep research", filtered to category cs.CL, published between 2023-11-24 and 2025-11-24. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Formal Definition and Benchmarking of Deep Research

A foundational thread across the surveyed literature is the effort to formally characterize what constitutes "deep research" as distinct from other reasoning-intensive tasks. Java et al. (2025) argue persuasively that the core defining feature is not lengthy report generation but rather high fan-out over concepts during search—broad and reasoning-intensive exploration. This formalization enables objective evaluation through intermediate output representations encoding key claims uncovered during search, separating the reasoning challenge from surface-level report generation.

This definitional clarity has catalyzed benchmark development across multiple dimensions. LiveDRBench (Java et al., 2025) provides 100 challenging tasks over scientific topics and public interest events, revealing that even state-of-the-art systems achieve F1 scores between only 0.02 and 0.72 across sub-categories. BrowseComp-Plus (Chen et al., 2025) addresses fairness and transparency concerns by employing a fixed, curated corpus with human-verified supporting documents, enabling controlled experimentation that disentangles agent capabilities from retriever contributions. The benchmark demonstrates dramatic performance differences: Search-R1 with BM25 achieves only 3.86% accuracy, while GPT-5 with Qwen3-Embedding-8B retriever reaches 70.1%.

Enterprise-specific evaluation receives dedicated attention in DRBench (Abaskohi et al., 2025), which introduces 100 multi-step queries across 10 domains requiring agents to identify supporting facts from both public web and private company knowledge bases. This heterogeneous search space—including productivity software, cloud file systems, emails, and chat conversations—captures realistic enterprise contexts that web-only benchmarks miss.

### Theme 2: Agent Architecture Innovation

The surveyed papers reveal diverse architectural approaches to deep research, ranging from dual-agent frameworks to multi-agent enterprise systems. WebWeaver (Li et al., 2025) introduces a planner-writer dual-agent framework where the planner operates in dynamic cycles, interleaving evidence acquisition with outline optimization to produce citation-grounded outlines linked to a memory bank. The writer then executes hierarchical retrieval and writing section by section, performing targeted retrieval only for necessary evidence. This approach establishes new state-of-the-art results across DeepResearch Bench, DeepConsult, and DeepResearchGym by mitigating long-context issues and citation hallucinations.

Enterprise contexts demand more specialized architectures. Enterprise Deep Research (Prabhakar et al., 2025) integrates five components: a Master Planning Agent for adaptive query decomposition, four specialized search agents (General, Academic, GitHub, LinkedIn), an extensible MCP-based tool ecosystem supporting NL2SQL and file analysis, a Visualization Agent for data-driven insights, and a reflection mechanism with optional human-in-the-loop steering. This multi-agent system outperforms state-of-the-art agentic systems on open-ended benchmarks without human steering, demonstrating the value of domain specialization and enterprise integration.

A different architectural innovation appears in Test-Time Diffusion Deep Researcher (Han et al., 2025), which conceptualizes report generation as a diffusion process. Starting with a preliminary draft skeleton, TTD-DR iteratively refines through a "denoising" process dynamically informed by retrieval mechanisms. This draft-centric design, inspired by human research cycles of searching, reasoning, and revision, achieves state-of-the-art results while reducing information loss during iterative search.

### Theme 3: Training and Optimization Strategies

Training deep research agents presents unique challenges, particularly for open-ended, long-form tasks where traditional reinforcement learning with verifiable rewards falls short. DR Tulu (Shao et al., 2025) addresses this through Reinforcement Learning with Evolving Rubrics (RLER), where rubrics co-evolve with the policy model during training. This allows rubrics to incorporate newly explored information from search and contrasting model responses, enabling better fact checking and more discriminative on-policy feedback. The resulting DR Tulu-8B model substantially outperforms existing open agents by 15.6% over Tongyi DR and matches proprietary agents like OpenAI DR while being 1000x cheaper per query.

Data synthesis for training receives focused attention in InfoSeek (Xia et al., 2025), which formalizes deep research tasks as Hierarchical Constraint Satisfaction Problems fundamentally different from flat CSP formulations. InfoSeek uses a dual-agent system to recursively build Research Trees from large-scale webpages, converting these into natural language questions requiring full hierarchy traversal. The framework yields over 50K training examples, and models trained on InfoSeek consistently outperform strong baselines—3B LLMs optimized with InfoSeek surpass 32B models and lightweight commercial APIs on BrowseComp-Plus.

### Theme 4: Personalization and User-Centric Evaluation

As deep research agents mature, attention shifts toward personalization—adapting research outputs to individual user contexts, preferences, and needs. PDR-Bench (Liang et al., 2025) introduces the first benchmark for evaluating personalization in Deep Research Agents, pairing 50 diverse research tasks across 10 domains with 25 authentic user profiles combining structured persona attributes with dynamic real-world contexts. This yields 250 realistic user-task queries evaluated through the PQR Framework measuring Personalization Alignment, Content Quality, and Factual Reliability. Experiments reveal current capabilities and limitations in handling personalized scenarios, establishing a foundation for developing truly personalized AI research assistants.

This personalization focus complements the broader trend toward user-centric design seen in WebWeaver's human-centric iterative methodology and EDR's optional human-in-the-loop steering, suggesting the field is evolving beyond purely autonomous systems toward collaborative human-AI research partnerships.

### Theme 5: Survey and Synthesis of the Field

The field's rapid growth necessitates comprehensive synthesis to guide future development. Shi et al. (2025) provide a systematic survey formalizing a three-stage roadmap distinguishing deep research from related paradigms, introducing four key components (query planning, information acquisition, memory management, answer generation) with fine-grained sub-taxonomies. The survey consolidates optimization techniques including prompting, supervised fine-tuning, and agentic reinforcement learning, while identifying open challenges in evaluation criteria. This meta-level contribution serves as both a roadmap for newcomers and a reference point for positioning new research.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong agreement on several foundational points. First, there is consensus that deep research is defined by high fan-out reasoning-intensive exploration rather than output length (Java et al., 2025; Shi et al., 2025). Second, multiple papers converge on the necessity of iterative, cyclical processes mirroring human research behavior—whether through WebWeaver's dynamic planning cycles (Li et al., 2025), TTD-DR's diffusion-based revision (Han et al., 2025), or EDR's reflection mechanism (Prabhakar et al., 2025). Third, all benchmark papers agree that current systems have substantial room for improvement, with even the best models achieving only moderate performance on challenging tasks.

**Disagreements**: The literature shows minimal direct disagreement, reflecting the field's early-stage consensus-building phase. However, subtle tensions emerge around evaluation methodology. BrowseComp-Plus (Chen et al., 2025) advocates for fixed corpora enabling controlled experiments, while LiveDRBench (Java et al., 2025) and DRBench (Abaskohi et al., 2025) emphasize real-world dynamic contexts including live web search and private enterprise data. This reflects a broader methodological divide between experimental control and ecological validity that remains unresolved.

## Gaps and Open Questions

Several patterns emerge from the limitations acknowledged across the surveyed papers. First, computational efficiency remains a persistent concern: WebWeaver's dual-agent system incurs overhead from dynamic cycling (Li et al., 2025), TTD-DR's iterative diffusion requires significant resources (Han et al., 2025), and RLER's co-evolving rubrics introduce training complexity (Shao et al., 2025). While DR Tulu demonstrates cost advantages at 1000x cheaper than proprietary systems, the underlying architectural trade-offs between efficiency and capability warrant further investigation.

Second, generalizability limitations appear across multiple papers. Enterprise-focused systems like EDR (Prabhakar et al., 2025) and DRBench (Abaskohi et al., 2025) acknowledge reduced applicability to non-enterprise contexts. Similarly, benchmarks focusing on scientific topics (LiveDRBench) or enterprise domains (DRBench) may not capture consumer-facing or creative research scenarios. The field lacks unified benchmarks that span diverse application domains while maintaining evaluation rigor.

Third, personalization remains underexplored beyond PDR-Bench's initial contribution (Liang et al., 2025). The benchmark's 25 profiles and 50 tasks provide a foundation but may not encompass the full spectrum of personalization scenarios. Dynamic context adaptation—how agents adjust to evolving user needs over extended interactions—receives no dedicated treatment in the surveyed literature.

Fourth, while several papers mention human-in-the-loop capabilities, systematic study of human-AI collaboration patterns in deep research is absent. EDR offers optional steering (Prabhakar et al., 2025), and WebWeaver emulates human processes (Li et al., 2025), but empirical investigation of optimal collaboration points, interface designs, and division of labor remains an open question.

Finally, the rapidly evolving nature of the field is explicitly acknowledged by Shi et al. (2025), who commit to continuous survey updates. This temporal limitation means the current synthesis captures only a snapshot, with likely significant developments emerging beyond the review window.

## Per-Paper Annotations

### Abaskohi et al. (2025)

**Research question**: How can we evaluate AI agents on complex, open-ended deep research tasks in realistic enterprise settings that require both public web and private company knowledge?

**Methodology**: Introduced DRBench with 100 multi-step queries across 10 enterprise domains, grounded in realistic user personas and spanning heterogeneous search spaces including productivity software, cloud file systems, emails, chat conversations, and the open web, with tasks generated through a synthesis pipeline with human-in-the-loop verification.

**Key findings**:
- DRBench evaluates agents on multi-step queries requiring identification of supporting facts from both public web and private company knowledge bases
- The benchmark spans 10 domains including Sales, Cybersecurity, and Compliance, providing diverse enterprise contexts
- Evaluation covers agent ability to recall relevant insights, maintain factual accuracy, and produce coherent, well-structured reports
- The benchmark highlights strengths, weaknesses, and critical paths for advancing enterprise deep research across diverse DR agents and strategies

**Limitations**: The benchmark focuses specifically on enterprise settings, which may not generalize to academic, scientific, or consumer-facing deep research scenarios. The heterogeneous search space including private company data may limit reproducibility for external researchers.

### Chen et al. (2025)

**Research question**: How can we create a fair and transparent benchmark for evaluating deep research agents that addresses the limitations of black-box live web search APIs?

**Methodology**: Introduced BrowseComp-Plus, derived from BrowseComp, employing a fixed and carefully curated corpus where each query includes human-verified supporting documents and mined challenging negatives to enable controlled experimentation and disentangled analysis of deep research agents and retrieval methods.

**Key findings**:
- Search-R1 with BM25 retriever achieves only 3.86% accuracy, while GPT-5 achieves 55.9% accuracy on the benchmark
- Integrating GPT-5 with the Qwen3-Embedding-8B retriever enhances accuracy to 70.1% with fewer search calls
- The benchmark effectively distinguishes the performance of different deep research systems and retrieval methods
- BrowseComp-Plus enables comprehensive evaluation of retrieval effectiveness, citation accuracy, and context engineering in deep research systems

**Limitations**: The benchmark is derived from BrowseComp and may inherit some of its original limitations. The fixed corpus approach, while enabling controlled experiments, may not fully capture the dynamic nature of real-world web search scenarios.

### Han et al. (2025)

**Research question**: How can we improve deep research agents' performance on complex, long-form research report generation beyond the plateau caused by generic test-time scaling algorithms?

**Methodology**: Proposed Test-Time Diffusion Deep Researcher (TTD-DR), which conceptualizes research report generation as a diffusion process starting with a preliminary draft skeleton that is iteratively refined through a denoising process dynamically informed by retrieval mechanisms, enhanced by a self-evolutionary algorithm applied to each component of the agentic LLM workflow.

**Key findings**:
- TTD-DR achieves state-of-the-art results on a wide array of benchmarks requiring intensive search and multi-hop reasoning
- The framework significantly outperforms existing deep research agents on complex report generation tasks
- The draft-centric design makes the report writing process more timely and coherent while reducing information loss during iterative search
- The approach draws inspiration from the iterative nature of human research involving cycles of searching, reasoning, and revision

**Limitations**: The draft-centric diffusion approach may require significant computational resources for iterative refinement. The method's effectiveness depends on the quality of the initial draft skeleton and the retrieval mechanism's ability to inform the denoising process at each step.

### Java et al. (2025)

**Research question**: What is the formal definition of the deep research task and how can it be objectively evaluated separate from lengthy report generation?

**Methodology**: Proposed a formal characterization of deep research based on high fan-out over concepts during search, defined an intermediate output representation encoding key claims uncovered during search, and introduced LiveDRBench with 100 challenging tasks over scientific topics and public interest events.

**Key findings**:
- F1 scores across state-of-the-art DR systems range between 0.02 and 0.72 for any sub-category, indicating significant room for improvement
- OpenAI's model performs best with an overall F1 score of 0.55
- Analysis of reasoning traces reveals the distribution over the number of referenced sources, branching, and backtracking events executed by current DR systems
- The core defining feature of deep research is broad and reasoning-intensive exploration, not the production of lengthy report-style outputs

**Limitations**: The benchmark focuses on scientific topics and public interest events, which may not cover all enterprise or domain-specific deep research scenarios. Current DR systems show limited performance with low F1 scores across sub-categories.

### Li et al. (2025)

**Research question**: How can AI agents synthesize vast web-scale information into insightful reports for open-ended deep research without suffering from hallucination and low citation accuracy?

**Methodology**: WebWeaver is a dual-agent framework where a planner iteratively interleaves evidence acquisition with outline optimization to produce a citation-grounded outline, and a writer executes hierarchical retrieval and writing using a memory bank of evidence.

**Key findings**:
- Establishes new state-of-the-art on DeepResearch Bench, DeepConsult, and DeepResearchGym benchmarks
- Dynamic outline approach effectively mitigates long-context issues and citation hallucinations
- Targeted retrieval from memory bank via citations reduces redundant and irrelevant evidence
- Human-centric iterative methodology produces comprehensive, trusted, and well-structured reports

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include computational overhead from the dual-agent system and dynamic cycling, and scalability of the memory bank for extremely large evidence collections.

### Liang et al. (2025)

**Research question**: How can deep research agents be evaluated for personalization capabilities when existing benchmarks are mostly close-ended and neglect personalized scenarios?

**Methodology**: Introduced PDR-Bench with 50 diverse research tasks across 10 domains paired with 25 authentic user profiles combining structured persona attributes with dynamic real-world contexts, yielding 250 realistic queries, and proposed the PQR Evaluation Framework measuring Personalization Alignment, Content Quality, and Factual Reliability.

**Key findings**:
- First benchmark specifically designed for evaluating personalization in Deep Research Agents
- 250 realistic user-task queries provide diverse evaluation coverage across 10 domains
- PQR Framework enables joint measurement of personalization, quality, and reliability dimensions
- Experiments reveal current capabilities and limitations of existing systems in handling personalized deep research

**Limitations**: The benchmark covers 50 tasks and 25 profiles which may not encompass all personalization scenarios; the evaluation framework may require further refinement as the field evolves; open-ended personalized benchmarks remain scarce beyond this contribution.

### Prabhakar et al. (2025)

**Research question**: How can autonomous agents be adapted for enterprise analytics given challenges with domain-specific nuances, intent alignment, and enterprise integration?

**Methodology**: Presented EDR, a multi-agent system integrating a Master Planning Agent for adaptive query decomposition, four specialized search agents (General, Academic, GitHub, LinkedIn), an extensible MCP-based tool ecosystem, a Visualization Agent, and a reflection mechanism with optional human-in-the-loop steering guidance.

**Key findings**:
- Outperforms state-of-the-art agentic systems on DeepResearch Bench and DeepConsult without human steering
- Enables automated report generation, real-time streaming, and seamless enterprise deployment
- Specialized search agents improve domain coverage across general, academic, code, and professional contexts
- Reflection mechanism effectively detects knowledge gaps and updates research direction
- MCP-based tool ecosystem supports NL2SQL, file analysis, and enterprise workflows

**Limitations**: Validation was primarily conducted on internal datasets which may limit generalizability to external enterprise contexts; enterprise-specific design choices may reduce applicability to non-enterprise scenarios; human-in-the-loop steering is optional and its impact on performance is not fully characterized.

### Shao et al. (2025)

**Research question**: How can reinforcement learning be adapted for open-ended, long-form deep research tasks when existing methods trained on short-form QA do not extend to realistic long-form scenarios?

**Methodology**: Developed Reinforcement Learning with Evolving Rubrics (RLER) where rubrics are constructed and maintained to co-evolve with the policy model during training, incorporating newly explored information from search and contrasting model responses to enable better fact checking and discriminative on-policy feedback.

**Key findings**:
- DR Tulu-8B is the first fully open model directly trained for open-ended, long-form deep research
- Substantially outperforms existing open deep research agents by 15.6% over Tongyi DR on average
- Matches or exceeds proprietary agents (0.7% over OpenAI DR) while being 1000x cheaper per query
- Evolving rubrics enable better fact checking and more discriminative feedback during training
- Strong performance across four benchmarks in science, healthcare, and general domains

**Limitations**: The 8B model size, while cost-effective, may have inherent capability limits compared to larger proprietary models; rubric evolution requires careful design to ensure quality feedback signals; training complexity of co-evolving rubrics and policy may present implementation challenges.

### Shi et al. (2025)

**Research question**: What is the current state of deep research systems that combine LLM reasoning capabilities with external tools, and how can they be systematically categorized and understood?

**Methodology**: Presented a comprehensive survey formalizing a three-stage roadmap, introducing four key components (query planning, information acquisition, memory management, answer generation) with fine-grained sub-taxonomies, summarizing optimization techniques, and consolidating evaluation criteria and open challenges.

**Key findings**:
- Formalizes a three-stage roadmap that distinguishes deep research from related paradigms
- Identifies and categorizes four key components with fine-grained sub-taxonomies for each
- Summarizes optimization techniques including prompting, supervised fine-tuning, and agentic reinforcement learning
- Consolidates evaluation criteria and open challenges to guide future development
- Commits to continuous updates to reflect the rapidly evolving field

**Limitations**: As a survey of a rapidly evolving field, it captures only a snapshot of current progress; the authors acknowledge the need for continuous updates to remain current with latest developments.

### Xia et al. (2025)

**Research question**: How can we synthesize complex deep research tasks that capture hierarchical constraint satisfaction complexity, avoiding the shortcomings of existing benchmarks and synthetic datasets?

**Methodology**: Formalized deep research tasks with verifiable answers as Hierarchical Constraint Satisfaction Problems (HCSPs) and introduced InfoSeek, a scalable dual-agent framework that recursively builds Research Trees from large-scale webpages, blurs intermediate nodes into valid sub-problems, and converts these trees into natural language questions requiring full hierarchy traversal.

**Key findings**:
- InfoSeek enables rapid scaling, yielding over 50K training examples, a curated test set, and reasoning trajectories generated via reject sampling
- On BrowseComp-Plus, 3B LLMs optimized with InfoSeek surpass much larger 32B models and lightweight commercial APIs like Gemini2.5-Flash
- InfoSeek-trained models achieve performance comparable to stronger commercial APIs like Gemini2.5-Pro
- The framework preserves meta-information such as intermediate steps and retrieval labels, supporting advanced optimization strategies including compound reward design and trajectory-level exploration

**Limitations**: Existing synthetic datasets often introduce shortcut reasoning, knowledge leakage, or lack sufficient structural depth, which InfoSeek aims to address but may not fully eliminate. The approach relies on large-scale webpage availability for tree construction.

## References

Abaskohi, A., Chen, T., Muñoz-Mármol, M., Fox, C., Ramesh, A. V., Marcotte, É., Lù, X. H., Chapados, N., Gella, S., West, P., Carenini, G., Pal, C., Drouin, A., & Laradji, I. H. (2025). DRBench: A realistic benchmark for enterprise deep research. arXiv. https://arxiv.org/abs/2510.00172

Chen, Z., Ma, X., Zhuang, S., Nie, P., Zou, K., Liu, A., Green, J., Patel, K., Meng, R., Su, M., Sharifymoghaddam, S., Li, Y., Hong, H., Shi, X., Liu, X., Thakur, N., Zhang, C., Gao, L., Chen, W., & Lin, J. (2025). BrowseComp-Plus: A more fair and transparent evaluation benchmark of deep-research agent. arXiv. https://arxiv.org/abs/2508.06600

Han, R., Chen, Y., CuiZhu, Z., Miculicich, L., Sun, G., Bi, Y., Wen, W., Wan, H., Wen, C., Maître, S., Lee, G., Tirumalashetty, V., Xue, E., Zhang, Z., Haykal, S., Gokturk, B., Pfister, T., & Lee, C.-Y. (2025). Deep researcher with test-time diffusion. arXiv. https://arxiv.org/abs/2507.16075

Java, A., Khandelwal, A., Midigeshi, S., Halfaker, A., Deshpande, A., Goyal, N., Gupta, A., Natarajan, N., & Sharma, A. (2025). Characterizing deep research: A benchmark and formal definition. arXiv. https://arxiv.org/abs/2508.04183

Li, Z., Guan, X., Zhang, B., Huang, S., Zhou, H., Lai, S., Yan, M., Jiang, Y., Xie, P., Huang, F., Zhang, J., & Zhou, J. (2025). WebWeaver: Structuring web-scale evidence with dynamic outlines for open-ended deep research. arXiv. https://arxiv.org/abs/2509.13312

Liang, Y., Li, J., Wang, Y., Wang, P., Tian, M., Liu, P., Qiao, S., Fang, R., Zhu, H., Zhang, G., Liu, M., Jiang, Y. E., Zhang, N., & Zhou, W. (2025). Towards personalized deep research: Benchmarks and evaluations. arXiv. https://arxiv.org/abs/2509.25106

Prabhakar, A., Ram, R., Chen, Z., Savarese, S., Wang, F., Xiong, C., Wang, H., & Yao, W. (2025). Enterprise deep research: Steerable multi-agent deep research for enterprise analytics. arXiv. https://arxiv.org/abs/2510.17797

Shao, R., Asai, A., Shen, S. Z., Ivison, H., Kishore, V., Zhuo, J., Zhao, X., Park, M., Finlayson, S. G., Sontag, D., Murray, T., Min, S., Dasigi, P., Soldaini, L., Brahman, F., Yih, W.-t., Wu, T., Zettlemoyer, L., Kim, Y., & Hajishirzi, H. (2025). DR Tulu: Reinforcement learning with evolving rubrics for deep research. arXiv. https://arxiv.org/abs/2511.19399

Shi, Z., Chen, Y., Li, H., Sun, W., Ni, S., Lyu, Y., Fan, R.-Z., Jin, B., Weng, Y., Zhu, M., Xie, Q., Guo, X., Yang, Q., Wu, J., Zhao, J., Tang, X., Ma, X., Wang, C., Mao, J., & Ai, Q. (2025). Deep research: A systematic survey. arXiv. https://arxiv.org/abs/2512.02038

Xia, Z., Luo, K., Qian, H., & Liu, Z. (2025). Open data synthesis for deep research. arXiv. https://arxiv.org/abs/2509.00375
