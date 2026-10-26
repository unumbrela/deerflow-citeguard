# Systematic Literature Review: Conversational Recommender Systems

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "conversational recommender systems", cs.IR, last 2 years (2024-10-26 to 2026-10-26)
**Citation format**: APA 7th edition

## Executive Summary

The field of conversational recommender systems (CRS) has evolved significantly over the past two years, with research focusing on three primary challenges: evaluation methodologies, data sparsity mitigation, and integration of advanced retrieval-generation architectures. The surveyed literature reveals a maturing field moving beyond proof-of-concept systems toward rigorous benchmarking frameworks and scalable solutions. Recent work emphasizes the critical role of large language models in both recommendation accuracy and dialogue quality, while addressing fundamental limitations around hallucination, data efficiency, and realistic user simulation. A notable trend is the shift toward unified generative frameworks that treat recommendation and dialogue generation as interdependent processes rather than decoupled tasks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "conversational recommender systems", filtered to category cs.IR, published between 2024-10-26 and 2026-10-26. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation and Benchmarking Frameworks

A significant portion of recent CRS research addresses the fundamental challenge of how to evaluate these systems reliably and at scale. Traditional metrics focused on recommendation accuracy fail to capture the multi-turn dialogue quality and user experience factors that define successful conversational interactions. Bernard et al. (2024) introduced CRS Arena, a crowdsourced platform that collects pairwise battles between anonymous CRSs, enabling large-scale human feedback collection and reliable system ranking using Elo ratings. This work addresses a critical gap in the field: the lack of standardized benchmarks with authentic user feedback.

Complementing crowdsourced evaluation, simulation-based approaches have gained traction as a scalable alternative. Bernard and Balog (2025) presented UserSimCRS v2, which significantly extends the original toolkit with LLM-based simulators and LLM-as-a-judge evaluation utilities. However, Chen et al. (2025) argued that existing evaluation metrics lack authenticity in reflecting user experience, proposing CoRE—a user-centric framework that summarizes 12 key user experience factors and uses multi-agent debate to synthesize them into a unified score. The convergence across these works suggests that the field is moving toward hybrid evaluation approaches that combine human feedback, simulation, and LLM-based assessment.

### Theme 2: Mitigating Data Sparsity and Bootstrapping

Data sparsity remains a fundamental challenge in CRS, affecting both dialogue contexts and entity representations. Zhang et al. (2025) proposed DACRS, a framework with three modules: Dialogue Augmentation to enrich dialogue contexts, Knowledge-Guided Entity Modeling leveraging knowledge graphs, and Dialogue-Entity Matching integrating dialogue representations with entity embeddings. This work addresses the severe data sparsity that plagues open-ended dialogues where linguistic variation and unseen entities degrade system performance.

Surana et al. (2025) tackled an even more extreme scenario: bootstrapping CRS without any in-domain dialogue corpus. Their empirical study demonstrated that synthetic data generated from non-conversational signals (item reviews, metadata, user-item interactions) can outperform scarce real dialogues in low-resource settings. The key insight is that domain-grounded synthetic data, selected using information-theoretic strategies (Jensen-Shannon diversity and Fisher information), provides viable supervisory signals when conversational training data is unavailable. This line of work suggests a promising direction for deploying CRS in domains where conversational datasets do not yet exist.

### Theme 3: Retrieval-Generation Synergy and Architectural Innovation

The integration of retrieval and generation capabilities has emerged as a central architectural challenge in CRS design. Yang and Fang (2025) proposed ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval for distilling user intent and retrieval-augmented generation for differentiating item features. This approach addresses the problem that noisy dialogues weaken retrieval while overlooked nuances among similar items degrade recommendation quality, all without requiring extra annotations.

Zhu et al. (2025) extended this direction by proposing CRAG (Collaborative Retrieval Augmented Generation), which combines state-of-the-art LLMs with collaborative filtering for conversational recommendations. Their work is notable for demonstrating superior item coverage and recommendation performance, particularly on recently released movies—a challenging scenario where collaborative signals are sparse. Yuan et al. (2026) further expanded the input modality with STARCRS, integrating vision-centric text understanding to handle longer and more heterogeneous inputs through dual pathways: screen-reading for auxiliary textual information and LLM-based reasoning for fine-grained analysis.

### Theme 4: Unified Generative Frameworks

A paradigm shift is emerging toward treating CRS as fully generative systems rather than retrieval-based pipelines. Zhang et al. (2026) proposed a generative CRS that represents items as discrete semantic IDs and integrates them directly into the autoregressive generation process. Their structured generation paradigm factorizes conversational recommendation into interdependent decisions (response intent, recommendation target, then response generation) with constrained decoding. This approach achieved gains of up to 29% on Recall@1 over strong baselines while maintaining competitive dialogue quality, suggesting that end-to-end optimization enables more coherent dependency structures and faithful item generation.

This generative approach addresses limitations inherent in decoupled architectures where recommendation and dialogue generation are optimized separately. By unifying both tasks within a single autoregressive framework, the system can learn dependencies that retrieval-based pipelines inherently miss, such as how response intent should condition item selection and vice versa.

### Theme 5: Realistic User Simulation and Decision Modeling

As simulation-based evaluation gains adoption, ensuring that user simulators exhibit realistic decision-making behavior has become critical. Li et al. (2026) identified that existing LLM-based simulators exhibit unrealistically strong information-processing capabilities and rarely show hesitation or decision deferral under choice overload conditions. They proposed Hesitator, a theory-grounded framework with a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions.

This work draws from psychological economics to reproduce established behavioral patterns, demonstrating that integrating decision-aware modules consistently mitigates unrealistic behaviors under increasing overload conditions. The framework addresses a fundamental gap in current simulation approaches: the assumption that users process information and make decisions optimally, when behavioral economics research consistently shows otherwise.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. First, there is broad agreement that traditional evaluation metrics are insufficient for CRS, with multiple works proposing comprehensive frameworks incorporating dialogue quality, user experience factors, and recommendation accuracy (Bernard et al., 2024; Chen et al., 2025; Bernard & Balog, 2025). Second, the literature consistently identifies data sparsity as a fundamental challenge, whether in dialogue contexts, entity representations, or training data availability (Zhang et al., 2025; Surana et al., 2025). Third, there is convergence on the value of combining LLMs with structured retrieval or collaborative filtering signals rather than relying on LLMs alone (Zhu et al., 2025; Yang & Fang, 2025; Yuan et al., 2026).

**Disagreements**: The literature shows less direct disagreement but reveals tension between different architectural philosophies. The retrieval-augmented generation approach (Yang & Fang, 2025; Zhu et al., 2025) assumes that external knowledge sources and collaborative signals are essential for accurate recommendation, while the fully generative approach (Zhang et al., 2026) suggests that end-to-end optimization within a unified autoregressive framework can subsume these benefits. This tension remains unresolved, as the works do not directly compare these architectural paradigms on identical benchmarks.

## Gaps and Open Questions

Several gaps emerge from the collective limitations of the surveyed literature. First, none of the papers explicitly address the computational cost or latency implications of their proposed frameworks, which is critical for real-world deployment of CRS at scale. Second, while evaluation frameworks are proposed, there is no standardized benchmark that all works adopt, making direct comparison difficult. Third, the literature focuses primarily on movie and entertainment domains, with limited exploration of CRS in other domains such as e-commerce, healthcare, or education. Fourth, privacy and ethical considerations around user data collection and dialogue history are not addressed in any of the surveyed papers. Finally, while user simulation is advanced, the gap between simulated and authentic user behavior remains unquantified in terms of how well simulation-based evaluation predicts real-world system performance.

## Per-Paper Annotations

### Bernard et al. (2024)

**Research question**: How can Conversational Recommender Systems be benchmarked at scale using human feedback?
**Methodology**: The authors introduce CRS Arena, a crowdsourced platform that displays pairwise battles between anonymous CRSs where users interact with systems sequentially and declare winners or draws. They conducted experiments on both open and closed crowdsourcing platforms and released the CRSArena-Dial dataset with 474 conversations and user feedback.
**Key findings**:
- Both open and closed crowdsourcing setups produce highly correlated rankings of CRSs
- Conversations from both setups have similar characteristics
- The platform successfully collects conversations and user feedback for reliable CRS evaluation and ranking
- A preliminary ranking of systems was established using the Elo rating system
- The CRSArena-Dial dataset of 474 conversations with corresponding user feedback was released
**Limitations**: not stated in abstract

### Bernard and Balog (2025)

**Research question**: How can simulation-based evaluation resources for Conversational Recommender Systems be improved to align with state-of-the-art research?
**Methodology**: The authors present UserSimCRS v2, a significant upgrade to the UserSimCRS toolkit that includes an enhanced agenda-based user simulator, introduction of LLM-based simulators, integration for a wider range of CRSs and datasets, and new LLM-as-a-judge evaluation utilities, demonstrated through a case study.
**Key findings**:
- UserSimCRS v2 addresses the scarcity of resources for simulation-based CRS evaluation
- The toolkit now includes large language model-based simulators alongside agenda-based simulators
- Integration supports a wider range of CRSs and datasets than the original version
- New LLM-as-a-judge evaluation utilities are introduced
- The extensions were demonstrated in a case study
**Limitations**: not stated in abstract

### Chen et al. (2025)

**Research question**: How can Conversational Recommender Systems be evaluated using a single metric that authentically reflects user experience across both recommendation accuracy and dialogue management?
**Methodology**: The authors propose CoRE (Conversational Recommendation Evaluator), a user-centric LLM-based evaluation framework with two components: LLM-As-Evaluator (summarizing 12 key user experience factors and using LLM to score each) and Multi-Agent Debater (four distinct roles debating to synthesize factors into a unified overall score).
**Key findings**:
- CoRE aligns well with human evaluation in most of the 12 factors and overall assessment
- CoRE's overall evaluation scores demonstrate significantly better alignment with human feedback compared to existing rule-based metrics
- The framework was applied to evaluate four CRSs on two benchmark datasets
- 12 key factors influencing user experience in CRSs were comprehensively summarized
- The multi-agent debate framework uses four roles: common user, domain expert, linguist, and HCI expert
**Limitations**: not stated in abstract

### Li et al. (2026)

**Research question**: How can user simulators for conversational recommender systems better model human decision-making behavior under choice overload?
**Methodology**: The authors propose Hesitator, a theory-grounded user simulation framework with a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions. Experiments were conducted across multiple user simulation frameworks, domains, sales modes, and LLM backbones.
**Key findings**:
- Integrating the Decision Module consistently mitigates unrealistic behaviors under increasing overload conditions
- Hesitator reproduces established behavioral patterns from psychological economics
- Existing LLM-based simulators exhibit unrealistically strong information-processing capabilities and rarely show hesitation or decision deferral
- The framework demonstrates ability to model human decision behavior with more realistic acceptance probabilities
**Limitations**: not stated in abstract

### Surana et al. (2025)

**Research question**: Can conversational recommender systems be bootstrapped using synthetic data generated from non-conversational signals without any in-domain dialogue corpus?
**Methodology**: A systematic empirical study comparing two information-theoretic selection strategies (Jensen-Shannon diversity and Fisher information) across domain signals, model architectures, datasets, and fine-tuning paradigms for generating synthetic conversational supervision from item reviews, metadata, and user-item interactions.
**Key findings**:
- Domain-grounded synthetic data consistently outperforms zero-shot prompting and naive synthetic baselines
- Active selection improves data efficiency over random sampling
- Metadata and collaborative filtering signals each improve selection quality
- In low-resource settings, synthetic data can outperform scarce real dialogues while further complementing them
- Non-conversational domain signals provide a viable path toward building CRS without conversational training data
**Limitations**: not stated in abstract

### Yang and Fang (2025)

**Research question**: How can retrieval and generation be synergistically combined in Conversational Recommender Systems to connect conversations with external domain knowledge while avoiding hallucinations?
**Methodology**: The authors propose ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval to distill informative user intent from conversations and retrieval-augmented generation to differentiate subtle item features, without requiring extra annotations.
**Key findings**:
- ReGeS achieves state-of-the-art performance in recommendation accuracy on multiple CRS benchmarks
- The reciprocal synergy obviates the need for extra annotations
- The framework reduces hallucinations compared to LLM-only approaches
- The approach simplifies continuous updates to the system
- The framework addresses noisy dialogues that weaken retrieval and overlooked nuances among similar items
**Limitations**: not stated in abstract

### Yuan et al. (2026)

**Research question**: How can vision-centric text understanding improve preference modeling in conversational recommender systems with longer and more heterogeneous inputs?
**Methodology**: The authors propose STARCRS, which integrates two complementary text understanding modes: a screen-reading pathway encoding auxiliary textual information as visual tokens, and an LLM-based textual pathway for fine-grained reasoning. A knowledge-anchored fusion framework combines contrastive alignment, cross-attention interaction, and adaptive gating.
**Key findings**:
- STARCRS consistently improves both recommendation accuracy and generated response quality
- The dual-pathway approach addresses practical issues such as input length constraints, text style inconsistency, and irrelevant textual noise
- Extensive experiments on two widely used benchmarks demonstrate the effectiveness of the approach
**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can data sparsity in both dialogue and entity spaces be mitigated in Conversational Recommender Systems?
**Methodology**: The authors propose DACRS, a novel CRS framework with three modules: Dialogue Augmentation (two-stage pipeline to enrich dialogue contexts), Knowledge-Guided Entity Modeling (leveraging knowledge graphs through entity substitution and similarity constraints), and Dialogue-Entity Matching (integrating dialogue representations with entity embeddings via attention aggregation).
**Key findings**:
- DACRS consistently outperforms state-of-the-art conversational recommender systems on two public benchmark datasets
- The Dialogue Augmentation module improves robustness to linguistic variation in open-ended dialogues
- Knowledge-Guided Entity Modeling enhances representation learning for sparsely supervised and unseen entities
- Dialogue-Entity Matching yields user representations capturing both explicit and implicit preferences
- The framework addresses severe data sparsity in both dialogue and entity spaces
**Limitations**: not stated in abstract

### Zhang et al. (2026)

**Research question**: Can recommendation and dialog generation be unified within a single autoregressive framework for conversational recommender systems?
**Methodology**: The authors propose a fully generative conversational recommender system that represents items as discrete semantic IDs and integrates them directly into the generation process. A structured generation paradigm factorizes conversational recommendation into a sequence of interdependent decisions (response intent, recommendation target, then response generation) with constrained decoding.
**Key findings**:
- The method achieves gains of up to 29% on Recall@1 over strong baselines
- The approach maintains competitive dialog quality while improving recommendation performance
- End-to-end optimization enables more coherent dependency structure and faithful item generation
- The unified autoregressive framework overcomes limitations of decoupled or retrieval-based pipelines
**Limitations**: not stated in abstract

### Zhu et al. (2025)

**Research question**: How can large language models be combined with collaborative filtering to improve conversational recommendation systems?
**Methodology**: The authors propose CRAG (Collaborative Retrieval Augmented Generation), an approach that combines state-of-the-art LLMs with collaborative filtering for conversational recommendations. Experiments were conducted on two movie conversational recommendation datasets (Reddit-v2 and Redial) comparing CRAG against several CRS baselines.
**Key findings**:
- CRAG demonstrates superior item coverage and recommendation performance compared to several CRS baselines
- Improvements are mainly due to better recommendation accuracy on recently released movies
- CRAG is the first approach that combines state-of-the-art LLMs with collaborative filtering for conversational recommendations
**Limitations**: not stated in abstract

## References

Bernard, N., & Balog, K. (2025). UserSimCRS v2: Simulation-based evaluation for conversational recommender systems. arXiv. https://arxiv.org/abs/2512.04588

Bernard, N., Joko, H., Hasibi, F., & Balog, K. (2024). CRS Arena: Crowdsourced benchmarking of conversational recommender systems. arXiv. https://arxiv.org/abs/2412.10514

Chen, N., Dai, Q., Dong, X., Wang, P., Jia, Q., Du, Z., Dong, Z., & Wu, X.-M. (2025). Evaluating conversational recommender systems via large language models: A user-centric framework. arXiv. https://arxiv.org/abs/2501.09493

Li, Y.-C., Chen, L.-C., Wu, S.-Y., Tsai, Y.-C., & Lin, S.-D. (2026). Decision-aware user simulation agent for evaluating conversational recommender systems. arXiv. https://arxiv.org/abs/2605.05250

Surana, R., Wu, J., Xie, Z., Xia, Y., Kallus, N., & McAuley, J. (2025). An empirical study on zero-data bootstrapping for conversational recommender systems. arXiv. https://arxiv.org/abs/2504.15476

Yang, D., & Fang, H. (2025). ReGeS: Reciprocal retrieval-generation synergy for conversational recommender systems. arXiv. https://arxiv.org/abs/2509.21371

Yuan, W., Qiao, S., Chen, T., Nguyen, Q. V. H., Huang, Z., & Yin, H. (2026). Integrating vision-centric text understanding for conversational recommender systems. arXiv. https://arxiv.org/abs/2601.13505

Zhang, S., Liu, M., & Long, C. (2026). Generative conversational recommender system. arXiv. https://arxiv.org/abs/2605.21987

Zhang, S., Liu, M., Yuan, W., Yin, H., & Long, C. (2025). On mitigating data sparsity in conversational recommender systems. arXiv. https://arxiv.org/abs/2507.00479

Zhu, Y., Wan, C., Steck, H., Liang, D., Feng, Y., Kallus, N., & Li, J. (2025). Collaborative retrieval for large language model-based conversational recommender systems. arXiv. https://arxiv.org/abs/2502.14137
