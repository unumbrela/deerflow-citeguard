# Systematic Literature Review: Conversational Recommender Systems

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: "conversational recommender systems", cs.IR, last 2 years (2024-10-26 to 2026-10-26)
**Citation format**: APA 7th edition

## Executive Summary

The field of conversational recommender systems (CRS) has matured significantly over the past two years, with research converging on three critical fronts: evaluation methodologies, data efficiency, and architectural innovation. The surveyed literature reveals a field in transition—from rule-based systems to large language model (LLM)-driven architectures, from isolated metrics to holistic user-centric evaluation frameworks. A dominant theme is the recognition that CRS evaluation must capture both recommendation accuracy and dialogue quality simultaneously, leading to novel simulation-based and crowdsourced benchmarking approaches. Simultaneously, researchers are addressing fundamental challenges in data sparsity through knowledge-guided augmentation and synthetic data bootstrapping. The integration of LLMs with collaborative filtering and retrieval-augmented generation represents a paradigm shift toward more flexible, context-aware recommendation systems that can handle real-world conversational complexity.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "conversational recommender systems", filtered to category cs.IR, published between 2024-10-26 and 2026-10-26. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation and Benchmarking Frameworks

The surveyed literature demonstrates a strong consensus that CRS evaluation requires multi-dimensional assessment beyond traditional accuracy metrics. Bernard et al. (2024) introduced CRS Arena, a crowdsourced platform enabling pairwise battles between anonymous CRS systems, collecting 474 conversations with user feedback and establishing rankings via the Elo rating system. This work established that both open and closed crowdsourcing platforms produce highly correlated rankings, validating crowdsourcing as a viable evaluation method.

Building on simulation-based evaluation, Bernard and Balog (2025) presented UserSimCRS v2, upgrading the toolkit with large language model-based simulators alongside traditional agenda-based simulators, plus new LLM-as-a-judge evaluation utilities. This addresses the scarcity of resources for simulation-based CRS evaluation and enables automated assessment at scale.

Chen et al. (2025) proposed CoRE (Conversational Recommendation Evaluator), a user-centric framework that summarizes 12 key user experience factors and uses a multi-agent debate mechanism (common user, domain expert, linguist, and HCI expert) to synthesize these into a unified performance score. CoRE demonstrates significantly better alignment with human feedback than existing rule-based metrics, addressing the fundamental challenge of evaluating both recommendation accuracy and dialogue management quality with a single metric.

Li et al. (2026) identified a critical gap in existing user simulators: the lack of realistic decision-making behavior. Their Hesitator framework introduces a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions, reproducing established behavioral patterns from psychological economics. Most existing simulation frameworks do not explicitly model the internal decision process, and LLM-based simulators often exhibit unrealistically strong information-processing capabilities without showing hesitation.

### Theme 2: Addressing Data Sparsity and Bootstrapping

Data sparsity remains a fundamental challenge in CRS, particularly in dialogue and entity spaces. Zhang et al. (2025) proposed DACRS, a framework addressing severe data sparsity through three modules: Dialogue Augmentation (a two-stage pipeline enriching dialogue contexts), Knowledge-Guided Entity Modeling (leveraging knowledge graphs through entity substitution and similarity constraints), and Dialogue-Entity Matching (integrating dialogue representations with entity embeddings via attention aggregation). DACRS consistently outperforms state-of-the-art CRS on two public benchmark datasets.

Surana et al. (2025) explored whether CRS can be bootstrapped using synthetic data generated from non-conversational signals without any in-domain dialogue corpus. Their systematic empirical study compared two information-theoretic selection strategies (Jensen-Shannon diversity and Fisher information) across domain signals, model architectures, datasets, and fine-tuning paradigms. Key findings show that domain-grounded synthetic data consistently outperforms zero-shot prompting and naive synthetic baselines, active selection improves data efficiency over random sampling, and in low-resource settings, synthetic data can outperform scarce real dialogues while further complementing them. This establishes non-conversational domain signals as a viable path toward building CRS without conversational training data.

### Theme 3: LLM Integration and Architectural Innovation

The integration of large language models with traditional recommendation approaches represents the most active research direction. Zhu et al. (2025) proposed CRAG (Collaborative Retrieval Augmented Generation), the first approach combining LLMs with collaborative filtering for conversational recommendations. Experiments on Reddit-v2 and Redial datasets demonstrate superior item coverage and recommendation performance compared to several CRS baselines, with improvements mainly due to better accuracy on recently released movies.

Yang and Fang (2025) addressed hallucination in retrieval-augmented generation for CRS through ReGeS, a reciprocal Retrieval-Generation Synergy framework. ReGeS unifies generation-augmented retrieval to distill user intent from conversations and retrieval-augmented generation to differentiate subtle item features, eliminating the need for extra annotations. The framework achieves state-of-the-art performance in recommendation accuracy on multiple CRS benchmarks while simplifying continuous updates through reciprocal synergy between retrieval and generation.

Yuan et al. (2026) tackled the challenge of handling longer and more heterogeneous inputs in CRS through STARCRS, which integrates two complementary text understanding modes: a screen-reading pathway encoding auxiliary textual information as visual tokens, and an LLM-based textual pathway for fine-grained reasoning. A knowledge-anchored fusion framework combines contrastive alignment, cross-attention interaction, and adaptive gating. This approach addresses practical issues such as input length constraints, text style inconsistency, and irrelevant textual noise, consistently improving both recommendation accuracy and generated response quality.

Zhang et al. (2026) proposed a fully generative CRS that represents items as discrete semantic IDs and integrates them directly into the generation process. A structured generation paradigm factorizes conversational recommendation into a sequence of interdependent decisions: response intent, recommendation target, then response generation. This unified autoregressive framework enables joint prediction of items and responses via next-token modeling, achieving gains of up to 29% on Recall@1 over strong baselines while maintaining competitive dialogue quality.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong agreement on several points. First, all evaluation-focused papers (Bernard et al., 2024; Bernard & Balog, 2025; Chen et al., 2025; Li et al., 2026) converge on the necessity of multi-dimensional evaluation capturing both recommendation accuracy and dialogue quality. Second, there is consensus that LLMs must be augmented with external knowledge or collaborative signals rather than used in isolation (Zhu et al., 2025; Yang & Fang, 2025; Yuan et al., 2026). Third, all papers addressing data sparsity agree that synthetic or augmented data can meaningfully improve performance in low-resource settings (Zhang et al., 2025; Surana et al., 2025).

**Disagreements**: The literature shows limited direct disagreement, reflecting the field's relatively coherent trajectory. However, there is an implicit tension between simulation-based evaluation (Bernard & Balog, 2025; Li et al., 2026) and crowdsourced human evaluation (Bernard et al., 2024) regarding which provides more reliable assessment. Additionally, while most architectural papers assume LLMs as the foundation, the generative approach (Zhang et al., 2026) diverges from retrieval-augmented approaches (Zhu et al., 2025; Yang & Fang, 2025; Yuan et al., 2026) in whether items should be generated directly or retrieved from a candidate pool.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are addressed only in full text or that the field lacks systematic self-critique. Second, while evaluation frameworks are well-developed, there is limited work on longitudinal user studies tracking CRS performance over extended interaction periods. Third, the tension between simulation-based and human-based evaluation remains unresolved—crowdsourced evaluation (Bernard et al., 2024) and simulation-based approaches (Bernard & Balog, 2025; Li et al., 2026) have not been directly compared on the same systems. Fourth, while data augmentation and synthetic bootstrapping show promise, the quality ceiling of synthetic data versus real human conversations remains unclear. Finally, the generative CRS approach (Zhang et al., 2026) raises questions about scalability to large item catalogs that remain unaddressed.

## Per-Paper Annotations

### Bernard et al. (2024)

**Research question**: How can conversational recommender systems be benchmarked at scale using human feedback through crowdsourced platforms?
**Methodology**: The authors developed CRS Arena, a platform that displays pairwise battles between anonymous conversational recommender systems where users interact with systems sequentially before declaring a winner or draw. Experiments were conducted on both open and closed crowdsourcing platforms, collecting 474 conversations with user feedback and ranking systems using the Elo rating system.
**Key findings**:
- Both open and closed crowdsourcing platforms produce highly correlated rankings of conversational recommender systems
- Conversations from both platform setups exhibit similar characteristics
- The platform successfully collected 474 conversations with corresponding user feedback
- A preliminary ranking of systems was established using the Elo rating system
**Limitations**: Not stated in abstract

### Chen et al. (2025)

**Research question**: How can conversational recommender systems be evaluated using a single metric that authentically reflects user experience across both recommendation accuracy and dialogue management quality?
**Methodology**: The authors propose CoRE (Conversational Recommendation Evaluator), a user-centric framework with two components: LLM-As-Evaluator (summarizes 12 key user experience factors and uses LLM to score each) and Multi-Agent Debater (four distinct roles debate to synthesize factors into a unified overall performance score).
**Key findings**:
- CoRE summarizes 12 key factors influencing user experience in conversational recommender systems
- The multi-agent debate framework uses four roles: common user, domain expert, linguist, and HCI expert
- CoRE aligns well with human evaluation across most of the 12 factors and overall assessment
- CoRE's overall evaluation scores demonstrate significantly better alignment with human feedback than existing rule-based metrics
**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can data sparsity in both dialogue and entity spaces be mitigated in conversational recommender systems?
**Methodology**: The authors propose DACRS, a framework with three modules: Dialogue Augmentation (two-stage pipeline to enrich dialogue contexts), Knowledge-Guided Entity Modeling (leverages knowledge graphs through entity substitution and similarity constraints), and Dialogue-Entity Matching (integrates dialogue representations with entity embeddings via attention aggregation).
**Key findings**:
- DACRS addresses severe data sparsity in dialogue and entity spaces simultaneously
- The Dialogue Augmentation module improves robustness to linguistic variation through two-stage augmentation
- Knowledge-Guided Entity Modeling enhances representation learning for sparsely supervised and unseen entities
- DACRS consistently outperforms state-of-the-art conversational recommender systems on two public benchmark datasets
**Limitations**: Not stated in abstract

### Zhu et al. (2025)

**Research question**: How can large language models be enhanced to leverage behavioral data for conversational recommendations using collaborative filtering approaches?
**Methodology**: The authors propose CRAG (Collaborative Retrieval Augmented Generation), combining state-of-the-art LLMs with collaborative filtering for conversational recommendations. Experiments were conducted on two publicly available movie conversational recommendation datasets: Reddit-v2 and Redial.
**Key findings**:
- CRAG demonstrates superior item coverage and recommendation performance compared to several CRS baselines
- Improvements are mainly due to better recommendation accuracy on recently released movies
- CRAG is the first approach that combines LLMs with collaborative filtering for conversational recommendations
- The code and data are publicly available at https://github.com/yaochenzhu/CRAG
**Limitations**: Not stated in abstract

### Surana et al. (2025)

**Research question**: Can conversational recommender systems be bootstrapped using synthetic data generated from non-conversational signals without any in-domain dialogue corpus?
**Methodology**: A systematic empirical study comparing two information-theoretic selection strategies (Jensen-Shannon diversity and Fisher information) across domain signals, model architectures, datasets, and fine-tuning paradigms for generating synthetic conversational supervision from item reviews, metadata, and user-item interactions.
**Key findings**:
- Domain-grounded synthetic data consistently outperforms zero-shot prompting and naive synthetic baselines
- Active selection improves data efficiency over random sampling
- Metadata and collaborative filtering signals each improve selection quality
- In low-resource settings, synthetic data can outperform scarce real dialogues while further complementing them
- Non-conversational domain signals provide a viable path toward building CRS without conversational training data
**Limitations**: Not stated in abstract

### Yang and Fang (2025)

**Research question**: How can retrieval-augmented generation be adapted for conversational recommender systems to reduce hallucination while avoiding domain-specific engineering?
**Methodology**: The authors propose ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval to distill user intent from conversations and retrieval-augmented generation to differentiate subtle item features, eliminating the need for extra annotations.
**Key findings**:
- ReGeS addresses noisy dialogues that weaken retrieval and overlooked nuances among similar items
- The framework obviates the need for extra annotations while reducing hallucinations
- ReGeS simplifies continuous updates through reciprocal synergy between retrieval and generation
- ReGeS achieves state-of-the-art performance in recommendation accuracy on multiple CRS benchmarks
**Limitations**: Not stated in abstract

### Bernard and Balog (2025)

**Research question**: How can simulation-based evaluation resources for conversational recommender systems be improved to align with state-of-the-art research?
**Methodology**: The authors present UserSimCRS v2, an upgraded toolkit featuring an enhanced agenda-based user simulator, large language model-based simulators, integration for a wider range of CRSs and datasets, and new LLM-as-a-judge evaluation utilities, demonstrated through a case study.
**Key findings**:
- UserSimCRS v2 addresses the scarcity of resources for simulation-based CRS evaluation
- The toolkit now includes large language model-based simulators alongside agenda-based simulators
- Integration supports a wider range of conversational recommender systems and datasets
- New LLM-as-a-judge evaluation utilities enable automated assessment
**Limitations**: Not stated in abstract

### Yuan et al. (2026)

**Research question**: How can conversational recommender systems better handle longer and more heterogeneous inputs while maintaining strong language understanding capabilities?
**Methodology**: The authors propose STARCRS, which integrates two complementary text understanding modes: a screen-reading pathway encoding auxiliary textual information as visual tokens, and an LLM-based textual pathway for fine-grained reasoning. A knowledge-anchored fusion framework combines contrastive alignment, cross-attention interaction, and adaptive gating.
**Key findings**:
- STARCRS consistently improves both recommendation accuracy and generated response quality
- The approach addresses practical issues such as input length constraints, text style inconsistency, and irrelevant textual noise
- Two complementary text understanding modes improve preference modeling and response generation
- Extensive experiments on two widely used benchmarks demonstrate consistent improvements
**Limitations**: Not stated in abstract

### Li et al. (2026)

**Research question**: How can user simulators for conversational recommender systems better model human decision-making behavior, including hesitation and decision deferral?
**Methodology**: The authors propose Hesitator, a theory-grounded user simulation framework with a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions. Experiments were conducted across multiple user simulation frameworks, domains, sales modes, and LLM backbones.
**Key findings**:
- Integrating the Decision Module consistently mitigates unrealistic behaviors under increasing overload conditions
- Hesitator reproduces established behavioral patterns from psychological economics
- Most existing simulation frameworks do not explicitly model the internal decision process
- LLM-based simulators often exhibit unrealistically strong information-processing capabilities and rarely show hesitation
- The framework demonstrates ability to model human decision behavior under choice overload
**Limitations**: Not stated in abstract

### Zhang et al. (2026)

**Research question**: How can recommendation and dialog generation be unified within a single autoregressive framework for conversational recommender systems?
**Methodology**: The authors propose a fully generative conversational recommender system that represents items as discrete semantic IDs and integrates them directly into the generation process. A structured generation paradigm factorizes conversational recommendation into a sequence of interdependent decisions: response intent, recommendation target, then response generation.
**Key findings**:
- The method achieves gains of up to 29% on Recall@1 over strong baselines
- The approach maintains competitive dialog quality while improving recommendation performance
- End-to-end optimization enables more coherent dependency structure
- Constrained decoding supports faithful item generation
- Unified autoregressive framework enables joint prediction of items and responses via next-token modeling
**Limitations**: Not stated in abstract

## References

Bernard, N., & Balog, K. (2025). UserSimCRS v2: Simulation-based evaluation for conversational recommender systems. arXiv. https://arxiv.org/abs/2512.04588

Bernard, N., Joko, H., Hasibi, F., & Balog, K. (2024). CRS Arena: Crowdsourced benchmarking of conversational recommender systems. arXiv. https://arxiv.org/abs/2412.10514

Chen, N., Dai, Q., Dong, X., Wang, P., Jia, Q., Du, Z., Dong, Z., & Wu, X.-M. (2025). Evaluating conversational recommender systems via large language models: A user-centric framework. arXiv. https://arxiv.org/abs/2501.09493

Li, Y.-C., Chen, L.-C., Wu, S.-Y., Tsai, Y.-C., & Lin, S.-D. (2026). Decision-aware user simulation agent for evaluating conversational recommender systems. arXiv. https://arxiv.org/abs/2605.05250

Surana, R., Wu, J., Xie, Z., Xia, Y., Kallus, N., & McAuley, J. (2025). An empirical study on zero-data bootstrapping for conversational recommender systems. arXiv. https://arxiv.org/abs/2504.15476

Yang, D., & Fang, H. (2025). ReGeS: Reciprocal retrieval-generation synergy for conversational recommender systems. arXiv. https://arxiv.org/abs/2509.21371

Yuan, W., Qiao, S., Chen, T., Nguyen, Q. V. H., Huang, Z., & Yin, H. (2026). Integrating vision-centric text understanding for conversational recommender systems. arXiv. https://arxiv.org/abs/2601.13505

Zhang, S., & Liu, M., & Long, C. (2026). Generative conversational recommender system. arXiv. https://arxiv.org/abs/2605.21987

Zhang, S., Liu, M., Yuan, W., Yin, H., & Long, C. (2025). On mitigating data sparsity in conversational recommender systems. arXiv. https://arxiv.org/abs/2507.00479

Zhu, Y., Wan, C., Steck, H., Liang, D., Feng, Y., Kallus, N., & Li, J. (2025). Collaborative retrieval for large language model-based conversational recommender systems. arXiv. https://arxiv.org/abs/2502.14137
