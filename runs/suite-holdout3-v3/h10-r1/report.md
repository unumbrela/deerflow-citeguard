# Systematic Literature Review: Conversational Recommender Systems

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "conversational recommender systems", category cs.IR, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Conversational Recommender Systems (CRS) represent a rapidly evolving research area that combines natural language dialogue with personalized recommendation capabilities. The surveyed literature from the past two years reveals a field maturing along multiple dimensions: evaluation methodologies, data efficiency, architectural innovations leveraging large language models, and user behavior modeling. Researchers are increasingly focused on addressing fundamental challenges including data sparsity, evaluation reliability, hallucination reduction, and realistic user simulation. The collective work demonstrates a shift toward more sophisticated integration of LLMs with traditional collaborative filtering, enhanced retrieval-generation synergy, and systematic benchmarking frameworks that better reflect real-world user experience.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "conversational recommender systems", filtered to category cs.IR, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation and Benchmarking Frameworks

A significant portion of recent CRS research focuses on developing robust evaluation methodologies that authentically capture user experience. Traditional metrics have proven insufficient for capturing the nuanced quality of conversational interactions, leading to novel frameworks that leverage both crowdsourcing and LLM-based assessment.

Bernard et al. (2024) introduced CRS Arena, a crowdsourced benchmarking platform that enables pairwise comparison of anonymous CRS systems through sequential user interactions. Their approach validates that both open and closed crowdsourcing platforms produce highly correlated rankings, establishing a foundation for reliable CRS evaluation. The released CRSArena-Dial dataset containing 474 conversations provides a valuable community resource.

Building on simulation-based evaluation, Bernard and Balog (2025) presented UserSimCRS v2, which upgrades previous toolkits with enhanced agenda-based simulators and LLM-based simulation capabilities. This work addresses the need for evaluation resources that align with state-of-the-art research, integrating support for a wider range of CRSs and datasets.

Chen et al. (2025) proposed CoRE, a user-centric evaluation framework that identifies 12 key factors influencing user experience and uses LLM-as-evaluator combined with multi-agent debate to synthesize these into unified performance scores. Their approach demonstrates significantly better alignment with human feedback compared to existing rule-based metrics, addressing the critical gap in authentic user experience reflection.

### Theme 2: Addressing Data Sparsity and Bootstrapping Challenges

Data sparsity remains a fundamental challenge in CRS development, with multiple papers proposing innovative solutions for learning from limited dialogue and entity supervision.

Zhang et al. (2025) developed DACRS, a comprehensive framework addressing both dialogue and entity sparsity through three modules: Dialogue Augmentation with a two-stage pipeline for enriching contexts, Knowledge-Guided Entity Modeling leveraging knowledge graphs, and Dialogue-Entity Matching integrating representations through attention. Their approach consistently outperforms state-of-the-art CRSs on public benchmarks.

Surana et al. (2025) explored whether CRS can be bootstrapped without any in-domain dialogue corpus through zero-data approaches. Their systematic empirical study demonstrates that domain-grounded synthetic data from non-conversational signals (item reviews, metadata, user-item interactions) consistently outperforms zero-shot prompting. Active selection strategies using Jensen-Shannon diversity and Fisher information improve data efficiency, with synthetic data outperforming scarce real dialogues in low-resource settings.

### Theme 3: LLM Integration and Architectural Innovations

The integration of large language models with traditional recommendation approaches represents a dominant research direction, with papers exploring various architectural strategies for combining LLM capabilities with collaborative filtering and retrieval mechanisms.

Zhu et al. (2025) introduced CRAG, the first approach combining state-of-the-art LLMs with collaborative filtering for conversational recommendations. Their method demonstrates superior item coverage and recommendation performance, particularly on recently released movies, addressing LLMs' historical struggle to leverage behavioral data important for classical collaborative filtering.

Yang and Fang (2025) proposed ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval and retrieval-augmented generation. This approach reduces hallucinations compared to LLM-only methods while achieving state-of-the-art performance on multiple CRS benchmarks, eliminating the need for extra annotations.

Yuan et al. (2026) addressed the challenge of handling longer and more heterogeneous inputs through STARCRS, which integrates vision-centric text understanding with LLM-based textual reasoning. Their screen-reading pathway encodes auxiliary information as visual tokens while the textual pathway focuses on critical content, demonstrating consistent improvements in both recommendation accuracy and response quality.

Zhang et al. (2026) presented a fully generative CRS that represents items as discrete semantic IDs within a single autoregressive framework. Their structured generation paradigm factorizes conversational recommendation into interdependent decisions, achieving gains of up to 29% on Recall@1 over strong baselines while maintaining competitive dialogue quality.

### Theme 4: User Simulation and Decision Modeling

Realistic user simulation is critical for both evaluation and training of CRS, with recent work focusing on better modeling of human decision-making behavior including psychological factors.

Li et al. (2026) proposed Hesitator, a theory-grounded user simulation framework that explicitly models the internal decision process including hesitation and decision deferral. Their modular Decision Module separates utility-based item selection from overload-aware commitment decisions, reproducing established behavioral patterns from psychological economics. The framework consistently mitigates unrealistic behaviors under increasing overload conditions, addressing the tendency of LLM-based simulators to exhibit unrealistically strong information-processing capabilities.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. Multiple works emphasize the insufficiency of traditional evaluation metrics and the need for more authentic user-centric assessment (Bernard et al., 2024; Chen et al., 2025; Bernard & Balog, 2025). There is broad agreement that data sparsity remains a critical bottleneck requiring innovative augmentation strategies (Zhang et al., 2025; Surana et al., 2025). The literature consistently demonstrates that hybrid approaches combining LLMs with traditional recommendation techniques outperform purely LLM-based or purely traditional methods (Zhu et al., 2025; Yang & Fang, 2025; Zhang et al., 2026).

**Disagreements**: The literature shows less disagreement on fundamental conclusions than on methodological approaches. Some papers emphasize simulation-based evaluation (Bernard & Balog, 2025; Li et al., 2026) while others prioritize crowdsourced human feedback (Bernard et al., 2024) or LLM-as-judge approaches (Chen et al., 2025). The relative emphasis on retrieval-augmented versus generation-augmented strategies varies, though Yang and Fang (2025) argue for their reciprocal synergy rather than choosing between them.

## Gaps and Open Questions

Several notable gaps emerge from the collective literature. None of the surveyed papers explicitly address long-term user relationship building or multi-session conversation continuity, focusing instead on single-session interactions. Cross-domain recommendation capabilities in conversational settings receive limited attention, with most work confined to specific domains like movies. The psychological and emotional dimensions of conversational recommendations remain underexplored, despite their importance in real-world recommendation scenarios. Privacy considerations in conversational data collection and usage are not addressed in the surveyed papers. Additionally, while multiple papers mention reducing hallucinations, none provide comprehensive analysis of hallucination types or systematic mitigation strategies beyond architectural improvements.

## Per-Paper Annotations

### Bernard et al. (2024)

**Research question**: How can crowdsourced platforms provide scalable and reliable benchmarking of Conversational Recommender Systems through human feedback?

**Methodology**: The authors developed CRS Arena, a platform that displays pairwise battles between anonymous CRSs where users interact with systems sequentially before declaring a winner or draw. Experiments were conducted on both open and closed crowdsourcing platforms to validate ranking correlations.

**Key findings**:
- Both open and closed crowdsourcing platforms produce highly correlated rankings of CRSs
- Conversations collected across different platforms show similar characteristics
- CRSArena-Dial dataset was released containing 474 conversations with corresponding user feedback
- A preliminary ranking of systems was established using the Elo rating system
- The platform provides a foundation for reliable evaluation and ranking of CRSs

**Limitations**: Not stated in abstract

### Bernard and Balog (2025)

**Research question**: How can simulation-based evaluation resources for Conversational Recommender Systems be improved to align with state-of-the-art research?

**Methodology**: The authors present UserSimCRS v2, an upgraded toolkit featuring an enhanced agenda-based user simulator, introduction of LLM-based simulators, integration for a wider range of CRSs and datasets, and new LLM-as-a-judge evaluation utilities, demonstrated through a case study.

**Key findings**:
- UserSimCRS v2 provides significant upgrades aligning the toolkit with state-of-the-art research
- Enhanced agenda-based user simulator improves simulation capabilities
- LLM-based simulators are introduced as a new feature
- Integration supports a wider range of CRSs and datasets
- New LLM-as-a-judge evaluation utilities are added

**Limitations**: Not stated in abstract

### Chen et al. (2025)

**Research question**: How can Conversational Recommender Systems be evaluated using a single metric that authentically reflects user experience across both recommendation accuracy and dialogue management quality?

**Methodology**: The authors propose CoRE (Conversational Recommendation Evaluator), a user-centric framework with two components: LLM-As-Evaluator (summarizing 12 key factors influencing user experience and using LLM to score each factor) and Multi-Agent Debater (four distinct roles debating to synthesize factors into a unified overall performance score).

**Key findings**:
- CoRE identifies 12 key factors influencing user experience in CRSs
- LLM-As-Evaluator component directly leverages LLM to assign scores to each factor
- Multi-Agent Debater uses four roles (common user, domain expert, linguist, HCI expert) to synthesize evaluation factors
- CoRE aligns well with human evaluation in most of the 12 factors and overall assessment
- CoRE's overall evaluation scores demonstrate significantly better alignment with human feedback compared to existing rule-based metrics

**Limitations**: Not stated in abstract

### Li et al. (2026)

**Research question**: How can user simulators for conversational recommender systems better model human decision-making behavior including hesitation and decision deferral?

**Methodology**: The authors propose Hesitator, a theory-grounded user simulation framework with a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions. Experiments were conducted across multiple user simulation frameworks, domains, sales modes, and LLM backbones.

**Key findings**:
- Integrating the Decision Module consistently mitigates unrealistic behaviors under increasing overload conditions
- Most existing simulation frameworks do not explicitly model the internal decision process
- LLM-based simulators often exhibit unrealistically strong information-processing capabilities and rarely show hesitation
- Hesitator reproduces established behavioral patterns from psychological economics
- The framework demonstrates ability to model human decision behavior under choice overload

**Limitations**: Not stated in abstract

### Surana et al. (2025)

**Research question**: Can conversational recommender systems be bootstrapped using synthetic conversational supervision from non-conversational signals without any in-domain dialogue corpus?

**Methodology**: The authors conducted a systematic empirical study comparing two information-theoretic selection strategies (Jensen-Shannon diversity and Fisher information) across domain signals, model architectures, datasets, and fine-tuning paradigms for generating synthetic conversational supervision from item reviews, metadata, and user-item interactions.

**Key findings**:
- Domain-grounded synthetic data consistently outperforms zero-shot prompting and naive synthetic baselines
- Active selection improves data efficiency over random sampling
- Metadata and collaborative filtering signals each improve selection quality
- In low-resource settings, synthetic data can outperform scarce real dialogues while further complementing them
- Non-conversational domain signals provide a viable path toward building CRS without conversational training data

**Limitations**: Not stated in abstract

### Yang and Fang (2025)

**Research question**: How can retrieval-augmented generation be improved for Conversational Recommender Systems to reduce hallucination and handle noisy dialogues?

**Methodology**: The authors propose ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval (to distill informative user intent from conversations) and retrieval-augmented generation (to differentiate subtle item features), eliminating the need for extra annotations.

**Key findings**:
- ReGeS unifies generation-augmented retrieval and retrieval-augmented generation in a reciprocal synergy
- The framework obviates the need for extra annotations
- ReGeS reduces hallucinations compared to approaches relying solely on LLMs
- The framework simplifies continuous updates
- Experiments on multiple CRS benchmarks show ReGeS achieves state-of-the-art performance in recommendation accuracy

**Limitations**: Not stated in abstract

### Yuan et al. (2026)

**Research question**: How can conversational recommender systems better handle longer and more heterogeneous inputs from expanded conversational context while maintaining strong language understanding?

**Methodology**: The authors propose STARCRS, which integrates two complementary text understanding modes: a screen-reading pathway that encodes auxiliary textual information as visual tokens, and an LLM-based textual pathway for fine-grained reasoning. A knowledge-anchored fusion framework combines contrastive alignment, cross-attention interaction, and adaptive gating.

**Key findings**:
- STARCRS consistently improves both recommendation accuracy and generated response quality
- The screen-reading pathway mimics skim reading on a screen by encoding auxiliary text as visual tokens
- The LLM-based textual pathway focuses on limited critical content for fine-grained reasoning
- Context enrichment introduces practical issues such as input length constraints, text style inconsistency, and irrelevant textual noise
- Extensive experiments on two widely used benchmarks demonstrate consistent improvements

**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can data sparsity in both dialogue and entity spaces be mitigated in Conversational Recommender Systems?

**Methodology**: The authors propose DACRS, a framework with three modules: Dialogue Augmentation (two-stage augmentation pipeline to enrich dialogue contexts), Knowledge-Guided Entity Modeling (leveraging knowledge graphs through entity substitution and similarity constraints), and Dialogue-Entity Matching (integrating dialogue representations with entity embeddings via attention aggregation).

**Key findings**:
- DACRS addresses dialogue data sparsity through a two-stage augmentation pipeline that improves robustness to linguistic variation
- Knowledge-Guided Entity Modeling enhances representation learning for sparsely supervised and unseen entities
- Dialogue-Entity Matching yields user representations capturing both explicit and implicit preferences
- Extensive experiments on two public benchmark datasets show DACRS consistently outperforms state-of-the-art CRSs

**Limitations**: Not stated in abstract

### Zhang et al. (2026)

**Research question**: How can recommendation and dialog generation be unified within a single autoregressive framework for conversational recommender systems?

**Methodology**: The authors propose a fully generative conversational recommender system that represents items as discrete semantic IDs integrated directly into the generation process. A structured generation paradigm factorizes conversational recommendation into interdependent decisions: predicting response intent and recommendation target, then generating the response conditioned on them.

**Key findings**:
- The method achieves gains of up to 29% on Recall@1 over strong baselines
- The approach maintains competitive dialog quality while improving recommendation performance
- Representing items as discrete semantic IDs enables joint prediction of items and responses via next-token modeling
- Structured generation enables end-to-end optimization and enforces more coherent dependency structure
- Constrained decoding supports faithful item generation

**Limitations**: Not stated in abstract

### Zhu et al. (2025)

**Research question**: How can large language models be combined with collaborative filtering to improve conversational recommendation performance?

**Methodology**: The authors propose CRAG (Collaborative Retrieval Augmented Generation), which combines state-of-the-art LLMs with collaborative filtering for conversational recommendations. Experiments were conducted on two movie conversational recommendation datasets: Reddit-v2 and Redial.

**Key findings**:
- CRAG demonstrates superior item coverage and recommendation performance compared to several CRS baselines
- CRAG is the first approach that combines state-of-the-art LLMs with collaborative filtering for conversational recommendations
- Improvements are mainly due to better recommendation accuracy on recently released movies
- The approach addresses LLMs' struggle to leverage behavioral data important for classical collaborative filtering

**Limitations**: Not stated in abstract

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
