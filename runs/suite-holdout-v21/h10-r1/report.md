# Systematic Literature Review: Conversational Recommender Systems

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "conversational recommender systems", category cs.IR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of conversational recommender systems (CRS) has evolved significantly over the past two years, with research concentrating on three critical challenges: evaluation methodologies, data sparsity mitigation, and integration of large language models. The surveyed literature reveals a maturing field moving from proof-of-concept systems toward rigorous benchmarking frameworks and simulation-based evaluation. Large language models have emerged as a dominant architectural component, enabling more natural dialogue while raising new challenges around hallucination and evaluation authenticity. Simultaneously, researchers are addressing fundamental limitations in training data availability through synthetic data generation and zero-data bootstrapping approaches.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "conversational recommender systems", filtered to category cs.IR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation Frameworks and Benchmarking

A significant portion of recent CRS research focuses on establishing rigorous evaluation methodologies. Traditional rule-based metrics have proven insufficient for capturing the nuanced user experience in conversational settings. Bernard et al. (2024) introduced CRS Arena, a crowdsourced platform that enables pairwise comparison of CRS systems through human feedback, collecting 474 conversations with the CRSArena-Dial dataset. This approach addresses the scalability challenge in CRS evaluation by leveraging crowdsourcing to generate reliable system rankings.

Building on simulation-based approaches, Bernard and Balog (2025) presented UserSimCRS v2, which enhances user simulation toolkits with large language model-based simulators and LLM-as-a-judge evaluation utilities. Chen et al. (2025) proposed CoRE, a user-centric evaluation framework that identifies 12 key factors influencing user experience and employs multi-agent debate to synthesize these into unified performance scores. Li et al. (2026) extended this line of work with Hesitator, addressing a critical gap in existing simulators: the unrealistic modeling of human decision-making behavior, particularly hesitation and decision deferral under choice overload.

These works collectively demonstrate a shift from purely accuracy-based metrics toward holistic evaluation frameworks that capture dialogue quality, user satisfaction, and behavioral realism.

### Theme 2: Large Language Model Integration

The integration of large language models (LLMs) has transformed CRS architectures, offering unprecedented capabilities in natural language understanding and generation. Zhu et al. (2025) proposed CRAG, the first approach combining LLMs with collaborative filtering for conversational recommendations, demonstrating superior item coverage and performance on recently released movies. This hybrid approach addresses a key limitation of pure LLM-based systems: their inability to leverage collaborative patterns from user-item interaction data.

Yang and Fang (2025) introduced ReGeS, which establishes reciprocal retrieval-generation synergy to connect conversations with external domain knowledge without requiring domain-specific engineering. Their framework distills user intent from conversations while differentiating subtle item features, reducing hallucinations compared to LLM-only approaches. Yuan et al. (2026) extended multimodal capabilities with STARCRS, integrating vision-centric text understanding to handle longer and more heterogeneous inputs through a knowledge-anchored fusion framework.

Zhang et al. (2026) took integration further by proposing a fully generative CRS that represents items as discrete semantic IDs within a single autoregressive framework, achieving up to 29% improvement on Recall@1 while maintaining competitive dialogue quality.

### Theme 3: Data Sparsity and Bootstrapping

Data sparsity remains a fundamental challenge in CRS, affecting both dialogue contexts and entity representations. Zhang et al. (2025) proposed DACRS, a framework addressing sparsity through dialogue augmentation and knowledge-guided entity modeling. Their three-module architecture enriches dialogue contexts, leverages knowledge graphs through entity substitution, and integrates dialogue representations with entity embeddings via attention aggregation.

Surana et al. (2025) explored an alternative approach through zero-data bootstrapping, demonstrating that synthetic supervision from non-conversational signals (item reviews, metadata, user-item interactions) can effectively bootstrap CRS without any in-domain dialogue corpus. Their systematic empirical study showed that domain-grounded synthetic data consistently outperforms zero-shot prompting, and in low-resource settings, synthetic data can outperform scarce real dialogues while further complementing them.

These approaches reflect a growing recognition that CRS performance is fundamentally constrained by data availability, and that creative solutions leveraging external knowledge sources and synthetic generation are essential for practical deployment.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong agreement on several points. First, all papers acknowledge that traditional evaluation metrics are insufficient for CRS, necessitating either human-in-the-loop evaluation (Bernard et al., 2024; Chen et al., 2025) or sophisticated simulation (Bernard & Balog, 2025; Li et al., 2026). Second, there is consensus that LLMs, while powerful, require augmentation with retrieval mechanisms or collaborative filtering to achieve reliable recommendations (Zhu et al., 2025; Yang & Fang, 2025; Yuan et al., 2026). Third, all works addressing data sparsity agree that external knowledge sources (knowledge graphs, reviews, metadata) are essential for overcoming supervision limitations (Zhang et al., 2025; Surana et al., 2025).

**Disagreements**: A notable tension exists between simulation-based and human-based evaluation approaches. While Bernard et al. (2024) demonstrate that crowdsourced evaluation produces reliable rankings, Bernard and Balog (2025) and Chen et al. (2025) argue that LLM-based simulation can approximate human judgment at scale. Li et al. (2026) challenge both positions, showing that existing LLM simulators exhibit unrealistic information-processing capabilities and rarely show hesitation, suggesting that neither pure simulation nor simple crowdsourcing fully captures authentic user behavior.

Additionally, there is divergence in architectural philosophy: Zhang et al. (2026) advocate for fully generative end-to-end systems, while Yang and Fang (2025) and Zhu et al. (2025) maintain that retrieval and generation should remain distinct but synergistic components.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly address long-term user relationship building or multi-session conversation continuity, focusing instead on single-session interactions. Second, while multiple papers mention reducing hallucinations (Yang & Fang, 2025) and improving faithfulness (Zhang et al., 2026), none provide comprehensive solutions for ensuring recommendation explanations are grounded in verifiable evidence.

Third, the limitations sections were notably absent from most abstracts, suggesting either space constraints or insufficient attention to boundary conditions and failure modes. Fourth, only Yuan et al. (2026) address multimodal inputs, indicating a gap in handling visual or audio-based conversational recommendations despite growing user expectations for multimodal interaction.

Finally, while evaluation frameworks are well-represented, there is limited work on real-world deployment challenges including latency, scalability, and integration with production recommendation infrastructure.

## Per-Paper Annotations

### Bernard et al. (2024)

**Research question**: How can we create a scalable platform for benchmarking Conversational Recommender Systems based on human feedback?

**Methodology**: The authors developed CRS Arena, a crowdsourced platform that displays pairwise battles between anonymous CRSs where users interact with systems sequentially before declaring a winner or draw. Experiments were conducted on both open and closed crowdsourcing platforms to validate the approach.

**Key findings**:
- Both open and closed crowdsourcing setups produce highly correlated rankings of CRSs
- Conversations from both setups have similar characteristics
- The platform collected 474 conversations with corresponding user feedback in the CRSArena-Dial dataset
- A preliminary ranking of systems was generated using the Elo rating system

**Limitations**: Not stated in abstract

### Bernard and Balog (2025)

**Research question**: How can we improve simulation-based evaluation resources for Conversational Recommender Systems?

**Methodology**: The authors present UserSimCRS v2, a significant upgrade to the UserSimCRS toolkit with key extensions including an enhanced agenda-based user simulator, large language model-based simulators, integration for a wider range of CRSs and datasets, and new LLM-as-a-judge evaluation utilities.

**Key findings**:
- UserSimCRS v2 aligns the toolkit with state-of-the-art research
- The upgrade includes an enhanced agenda-based user simulator
- Large language model-based simulators have been introduced
- Integration supports a wider range of CRSs and datasets
- New LLM-as-a-judge evaluation utilities have been added

**Limitations**: Not stated in abstract

### Chen et al. (2025)

**Research question**: How can we evaluate both recommendation accuracy and dialogue management quality in CRSs using a unified metric that authentically reflects user experience?

**Methodology**: The authors propose CoRE (Conversational Recommendation Evaluator), a user-centric evaluation framework with two components: LLM-As-Evaluator (summarizes 12 key factors influencing user experience and uses LLM to score each) and Multi-Agent Debater (four distinct roles debate to synthesize factors into a unified overall performance score).

**Key findings**:
- CoRE identifies 12 key factors influencing user experience in CRSs
- LLM-as-evaluator assigns scores to each of the 12 factors
- Multi-agent debate framework uses four roles (common user, domain expert, linguist, HCI expert) to synthesize an overall score
- CoRE aligns well with human evaluation in most of the 12 factors and overall assessment
- CoRE's overall evaluation scores demonstrate significantly better alignment with human feedback compared to existing rule-based metrics

**Limitations**: Not stated in abstract

### Li et al. (2026)

**Research question**: How can user simulators for conversational recommender systems better model human decision-making behavior including hesitation and decision deferral?

**Methodology**: The authors propose Hesitator, a theory-grounded user simulation framework with a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions. Experiments were conducted across multiple user simulation frameworks, domains, sales modes, and LLM backbones.

**Key findings**:
- Integrating the Decision Module consistently mitigates unrealistic behaviors under increasing overload conditions
- Hesitator reproduces established behavioral patterns from psychological economics
- Existing LLM-based simulators exhibit unrealistically strong information-processing capabilities and rarely show hesitation
- The framework demonstrates ability to model human decision behavior under choice overload

**Limitations**: Not stated in abstract

### Surana et al. (2025)

**Research question**: Can conversational recommender systems be bootstrapped using synthetic supervision from non-conversational signals without any in-domain dialogue corpus?

**Methodology**: The authors conduct a systematic empirical study comparing two information-theoretic selection strategies (Jensen-Shannon diversity and Fisher information) across domain signals, model architectures, datasets, and fine-tuning paradigms for generating synthetic conversational supervision from item reviews, metadata, and user-item interactions.

**Key findings**:
- Domain-grounded synthetic data consistently outperforms zero-shot prompting and naive synthetic baselines
- Active selection improves data efficiency over random sampling
- Metadata and collaborative filtering signals each improve selection quality
- In low-resource settings, synthetic data can outperform scarce real dialogues while further complementing them
- Non-conversational domain signals provide a viable path toward building CRS without conversational training data

**Limitations**: Not stated in abstract

### Yang and Fang (2025)

**Research question**: How can we connect conversations with external domain knowledge for CRSs without requiring domain-specific engineering or relying solely on LLMs?

**Methodology**: The authors propose ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval to distill informative user intent from conversations and retrieval-augmented generation to differentiate subtle item features.

**Key findings**:
- ReGeS addresses noisy dialogues that weaken retrieval and overlooked nuances among similar items
- The framework obviates the need for extra annotations
- ReGeS reduces hallucinations compared to LLM-only approaches
- The approach simplifies continuous updates
- Experiments on multiple CRS benchmarks show ReGeS achieves state-of-the-art performance in recommendation accuracy

**Limitations**: Not stated in abstract

### Yuan et al. (2026)

**Research question**: How can vision-centric text understanding be integrated into conversational recommender systems to handle longer and more heterogeneous inputs?

**Methodology**: The authors propose STARCRS, which integrates two complementary text understanding modes: a screen-reading pathway that encodes auxiliary textual information as visual tokens, and an LLM-based textual pathway for fine-grained reasoning. A knowledge-anchored fusion framework combines contrastive alignment, cross-attention interaction, and adaptive gating.

**Key findings**:
- STARCRS consistently improves both recommendation accuracy and generated response quality
- The approach addresses practical issues such as input length constraints, text style inconsistency, and irrelevant textual noise
- Extensive experiments on two widely used benchmarks demonstrate the effectiveness of the approach

**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can we address data sparsity in both dialogue and entity spaces that plagues Conversational Recommender Systems?

**Methodology**: The authors propose DACRS, a novel CRS framework with three modules: Dialogue Augmentation (two-stage pipeline to enrich dialogue contexts), Knowledge-Guided Entity Modeling (leverages knowledge graphs through entity substitution and similarity constraints), and Dialogue-Entity Matching (integrates dialogue representations with entity embeddings via attention aggregation).

**Key findings**:
- DACRS addresses both dialogue data sparsity and entity supervision sparsity simultaneously
- The Dialogue Augmentation module improves robustness to linguistic variation
- Knowledge-Guided Entity Modeling enhances representation learning for sparsely supervised and unseen entities
- Extensive experiments on two public benchmark datasets show DACRS consistently outperforms state-of-the-art CRS models

**Limitations**: Not stated in abstract

### Zhang et al. (2026)

**Research question**: How can recommendation and dialog generation be unified within a single autoregressive framework for conversational recommender systems?

**Methodology**: The authors propose a fully generative conversational recommender system that represents items as discrete semantic IDs and integrates them directly into the generation process. A structured generation paradigm factorizes conversational recommendation into a sequence of interdependent decisions with constrained decoding for faithful item generation.

**Key findings**:
- The method achieves gains of up to 29% on Recall@1 over strong baselines
- The approach maintains competitive dialog quality while improving recommendation performance
- Structured generation enables end-to-end optimization and enforces a more coherent dependency structure
- Constrained decoding supports faithful item generation

**Limitations**: Not stated in abstract

### Zhu et al. (2025)

**Research question**: How can large language models be combined with collaborative filtering to improve conversational recommender systems?

**Methodology**: The authors propose CRAG (Collaborative Retrieval Augmented Generation), which combines state-of-the-art LLMs with collaborative filtering for conversational recommendations. Experiments were conducted on two movie conversational recommendation datasets (Reddit-v2 and Redial) to evaluate item coverage and recommendation performance.

**Key findings**:
- CRAG demonstrates superior item coverage and recommendation performance compared to several CRS baselines
- Improvements are mainly due to better recommendation accuracy on recently released movies
- CRAG is the first approach that combines LLMs with collaborative filtering for conversational recommendations

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
