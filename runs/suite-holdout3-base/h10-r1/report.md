# Systematic Literature Review: Conversational Recommender Systems

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "conversational recommender systems", filtered to category cs.IR, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The field of conversational recommender systems (CRS) has rapidly evolved over the past two years, with research focusing on three critical challenges: evaluation methodologies, data efficiency, and architectural innovations. The surveyed papers collectively demonstrate a maturing field that is moving beyond proof-of-concept systems toward rigorous benchmarking, realistic user simulation, and scalable architectures. A dominant theme is the integration of large language models with traditional recommendation techniques, particularly collaborative filtering and knowledge graphs, to balance conversational flexibility with recommendation accuracy. Another significant trend is the development of synthetic data generation and zero-shot bootstrapping methods to address the scarcity of domain-specific dialogue data. Despite these advances, the literature reveals persistent gaps in cross-domain generalization, computational efficiency, and the alignment between automated evaluation metrics and genuine user experience.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "conversational recommender systems", filtered to category cs.IR, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation and Benchmarking Infrastructure

A major focus of recent CRS research is the development of robust evaluation frameworks and benchmarking platforms. Traditional rule-based metrics have proven inadequate for capturing the nuanced user experience in conversational settings, prompting the emergence of LLM-based evaluation and crowdsourced benchmarking. Bernard et al. (2024) introduced CRS Arena, a platform for pairwise battles between anonymous CRSs that collects human feedback to generate Elo-based rankings, demonstrating that both open and closed crowdsourcing setups produce highly correlated system rankings. Building on this, Bernard and Balog (2025) released UserSimCRS v2, which enhances simulation-based evaluation with LLM-based simulators and LLM-as-a-judge utilities to address the scarcity of evaluation resources. Chen et al. (2025) proposed CoRE, a user-centric evaluation framework that uses multi-agent debate among four roles (common user, domain expert, linguist, HCI expert) to synthesize 12 user experience factors into a unified score, achieving significantly better alignment with human feedback than rule-based metrics. Li et al. (2026) addressed the unrealistic behavior of existing simulators by introducing Hesitator, which explicitly models human decision-making under choice overload, reproducing established behavioral patterns from psychological economics. This cluster of work reflects a field-wide recognition that evaluation infrastructure must evolve alongside system capabilities.

### Theme 2: Data Efficiency and Synthetic Data Generation

The scarcity of high-quality dialogue data remains a fundamental bottleneck for CRS development, particularly in new domains. Surana et al. (2025) conducted a systematic empirical study on zero-data bootstrapping, demonstrating that synthetic conversational supervision generated from non-conversational signals (item reviews, metadata, user-item interactions) can outperform zero-shot prompting and even scarce real dialogues in low-resource settings. Their work showed that active selection strategies using Jensen-Shannon diversity and Fisher information improve data efficiency over random sampling, and that metadata and collaborative filtering signals each enhance selection quality. Zhang et al. (2025) documented in their literature review that LLM-based simulation methods have been widely adopted for dataset construction, algorithm enhancement, and system evaluation, though challenges persist including dataset bias and the gap between text semantic space and behavioral semantics. This theme reflects a pragmatic shift toward leveraging readily available non-conversational data rather than waiting for costly dialogue collection.

### Theme 3: Architectural Innovations for Context Integration

Recent architectural advances focus on effectively integrating multiple sources of contextual information to improve recommendation quality. Zou et al. (2025) proposed MCCRS, a mixture-of-experts architecture where each expert specializes in a specific context type (knowledge graph, conversation history, item reviews), coordinated by a ChairBot to generate final recommendations. Their approach breaks the bottleneck of relying on single contextual information sources, achieving significantly higher performance than existing baselines. Yang and Fang (2025) introduced ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval for user intent distillation with retrieval-augmented generation for item feature differentiation, achieving state-of-the-art performance while reducing hallucination risks. Zhu et al. (2025) proposed CRAG, the first approach to combine state-of-the-art LLMs with collaborative filtering for conversational recommendations, demonstrating superior item coverage and recommendation accuracy particularly for recently released movies. Zhang et al. (2025) proposed DACRS to address data sparsity through three modules: Dialogue Augmentation for linguistic robustness, Knowledge-Guided Entity Modeling for unseen entities, and Dialogue-Entity Matching for capturing explicit and implicit preferences. These works collectively demonstrate that hybrid architectures leveraging both neural and symbolic approaches outperform single-paradigm systems.

### Theme 4: Simulation Methods and Human Behavior Modeling

The literature reveals growing sophistication in modeling realistic human behavior for CRS evaluation and training. Zhang et al. (2025) developed a taxonomy categorizing simulation research into dataset construction, algorithm design, system evaluation, and empirical studies, noting that simulation methods play a key role in tackling CRS challenges but face persistent issues including limited output flexibility and the semantic-behavioral gap. Li et al. (2026) specifically addressed the problem that LLM-based simulators exhibit unrealistically strong information-processing capabilities and rarely show hesitation or decision deferral common in real consumer behavior. Their Hesitator framework introduces a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions, consistently mitigating unrealistic behaviors under increasing overload conditions across multiple frameworks, domains, and LLM backbones. This theme reflects recognition that accurate user simulation is critical for both automated evaluation and synthetic data generation.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the inadequacy of traditional rule-based metrics for CRS evaluation. Bernard et al. (2024), Chen et al. (2025), and Bernard and Balog (2025) all demonstrate that human-feedback-based or LLM-based evaluation aligns better with genuine user experience than separate metrics for recommendation accuracy and dialogue management. There is also broad agreement that data scarcity is a fundamental challenge: Surana et al. (2025), Zhang et al. (2025), and Zhang et al. (2025) all propose methods to augment or synthesize training data rather than relying solely on collected dialogues. Finally, multiple papers converge on the value of hybrid architectures: Zou et al. (2025), Yang and Fang (2025), and Zhu et al. (2025) all demonstrate that combining LLMs with structured knowledge or collaborative filtering outperforms pure LLM or pure traditional approaches.

**Disagreements**: The literature shows limited direct disagreement, as most papers focus on different aspects of the CRS pipeline. However, there is an implicit tension between papers advocating for LLM-based evaluation (Chen et al., 2025; Bernard & Balog, 2025) and those noting the limitations of LLM simulators (Li et al., 2026; Zhang et al., 2025). Chen et al. (2025) argue that LLMs can authentically capture user experience, while Li et al. (2026) demonstrate that LLM-based simulators exhibit unrealistic decision-making patterns. This suggests that LLMs may be better suited for evaluation than for simulating realistic user behavior during training. Additionally, while Surana et al. (2025) show synthetic data can outperform scarce real dialogues, Zhang et al. (2025) note that synthetic conversations still face a gap between text semantic space and behavioral semantics, indicating unresolved questions about the fidelity of synthetic data.

## Gaps and Open Questions

The collective literature reveals several persistent gaps:

1. **Cross-domain generalization**: Multiple papers acknowledge limitations in domain generalization. Zhu et al. (2025) evaluated CRAG only on movie datasets, limiting generalizability. Zou et al. (2025) note that performance across diverse recommendation domains remains unestablished. Zhang et al. (2025) observe that knowledge graphs may not be available for all domains.

2. **Computational efficiency**: Several papers acknowledge increased computational complexity. Zou et al. (2025) note that mixture-of-experts architectures increase training costs. Zhang et al. (2025) acknowledge that their three-module framework adds complexity during training and inference. Chen et al. (2025) note that multi-agent debate adds overhead compared to simpler metrics.

3. **Validation against real user behavior**: Li et al. (2026) acknowledge potential concerns about validation against actual human user behavior data. Bernard et al. (2024) released only 474 conversations, suggesting limited data for stable comparisons. The gap between simulated and real behavior remains a fundamental challenge.

4. **LLM bias inheritance**: Chen et al. (2025), Bernard and Balog (2025), and Yang and Fang (2025) all acknowledge that LLM-based evaluation or generation may inherit biases from underlying language models, but none propose mitigation strategies.

5. **Long-term user engagement**: None of the surveyed papers address long-term user engagement, preference evolution, or multi-session interactions. All evaluations focus on single-session performance.

6. **Explainability and transparency**: While multiple papers achieve high recommendation accuracy, none address how CRS systems should explain their recommendations to users or handle transparency requirements.

## Per-Paper Annotations

### Bernard et al. (2024)

**Research question**: How can we create a scalable benchmarking platform for Conversational Recommender Systems that reliably evaluates and ranks CRSs based on human feedback?

**Methodology**: Developed CRS Arena, a platform that displays pairwise battles between anonymous CRSs where users interact with systems sequentially before declaring a winner or draw, collecting conversations and feedback through both open and closed crowdsourcing platforms.

**Key findings**:
- Both open and closed crowdsourcing setups produce highly correlated rankings of CRSs
- Conversations across both platforms exhibit similar characteristics
- Released CRSArena-Dial dataset containing 474 conversations with corresponding user feedback
- Established preliminary CRS rankings using the Elo rating system
- Platform enables scalable, human-feedback-based CRS benchmarking

**Limitations**: The dataset size is relatively limited (474 conversations), and the Elo-based ranking is preliminary, requiring more data for stable, definitive system comparisons.

### Chen et al. (2025)

**Research question**: How can conversational recommender systems be evaluated using a unified metric that authentically reflects user experience across both recommendation accuracy and dialogue management quality?

**Methodology**: Proposed CoRE framework with two components: LLM-As-Evaluator (summarizes 12 user experience factors and scores each using LLM) and Multi-Agent Debater (four roles—common user, domain expert, linguist, HCI expert—synthesize factors into unified overall score).

**Key findings**:
- CoRE aligns well with human evaluation across most of the 12 user experience factors
- Overall evaluation scores demonstrate significantly better alignment with human feedback compared to existing rule-based metrics
- Multi-agent debate framework effectively synthesizes diverse evaluation perspectives into unified scores
- Successfully evaluated four CRSs on two benchmark datasets demonstrating framework applicability
- LLM-based evaluation captures authentic user experience better than separate rule-based metrics for recommendation and dialogue

**Limitations**: LLM-based evaluation may inherit biases from the underlying language models, and the multi-agent debate framework adds computational overhead compared to simpler rule-based metrics.

### Surana et al. (2025)

**Research question**: How can conversational recommender systems be bootstrapped without domain-specific dialogue data by leveraging non-conversational signals?

**Methodology**: Conducts a systematic empirical study comparing two information-theoretic selection strategies (Jensen-Shannon diversity and Fisher information) for generating synthetic conversational supervision from item reviews, metadata, and user-item interactions without any in-domain dialogue corpus.

**Key findings**:
- Domain-grounded synthetic data consistently outperforms zero-shot prompting and naive synthetic baselines
- Active selection improves data efficiency over random sampling
- Metadata and collaborative filtering signals each improve selection quality
- In low-resource settings, synthetic data can outperform scarce real dialogues
- Synthetic data can further complement real dialogues when both are available
- Establishes non-conversational domain signals as a viable path toward building CRS without conversational training data

**Limitations**: Code available through anonymous repository suggests work may be under review; synthetic data generation may require domain-specific tuning; quality of synthetic conversations depends on availability and quality of non-conversational source signals.

### Zou et al. (2025)

**Research question**: How can different types of contextual information (structured and unstructured) be effectively combined to improve conversational recommender systems?

**Methodology**: Proposed MCCRS, a mixture-of-experts architecture where each expert specializes in a specific context type (knowledge graph, conversation history, item reviews), coordinated by a ChairBot to generate final recommendations.

**Key findings**:
- MCCRS achieves significantly higher performance compared to existing baselines
- The multi-expert approach successfully breaks the bottleneck of relying on single contextual information
- Effective fusion of structured knowledge graphs with unstructured conversation history and item reviews
- ChairBot coordination enables specialization while maintaining coherent output
- Different contextual information types provide complementary benefits when properly combined

**Limitations**: The mixture-of-experts architecture may increase computational complexity and training costs, and performance across diverse recommendation domains beyond the tested scenarios remains unestablished.

### Zhu et al. (2025)

**Research question**: How can large language models in conversational recommender systems effectively leverage behavioral data from collaborative filtering approaches?

**Methodology**: Proposes CRAG (Collaborative Retrieval Augmented Generation), the first approach combining state-of-the-art LLMs with collaborative filtering for conversational recommendations.

**Key findings**:
- Demonstrates superior item coverage and recommendation performance compared to several CRS baselines
- Improvements are mainly attributable to better recommendation accuracy on recently released movies
- Successfully bridges LLM contextual understanding with CF behavioral data
- Validated on two publicly available movie conversational recommendation datasets (Reddit-v2 and Redial)
- Code and data made publicly available for reproducibility

**Limitations**: Evaluated only on movie recommendation datasets, which may limit generalizability to other domains; the approach depends on availability of behavioral data for collaborative filtering.

### Yang and Fang (2025)

**Research question**: How can conversational recommender systems connect conversations with external domain knowledge without requiring domain-specific engineering or risking LLM hallucinations?

**Methodology**: Proposes ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval to distill informative user intent from conversations and retrieval-augmented generation to differentiate subtle item features.

**Key findings**:
- Achieves state-of-the-art performance in recommendation accuracy on multiple CRS benchmarks
- The reciprocal synergy obviates the need for extra annotations
- Reduces hallucination risks compared to LLM-only approaches
- Simplifies continuous updates to the recommendation system
- Demonstrates effectiveness for knowledge-intensive CRS tasks

**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include evaluation scope across diverse domains and computational overhead of the reciprocal framework.

### Zhang et al. (2025)

**Research question**: How can data sparsity in both dialogue space (linguistic diversity) and entity space (limited supervision in knowledge graphs) be mitigated in conversational recommender systems?

**Methodology**: Proposed DACRS framework with three modules: Dialogue Augmentation (two-stage pipeline for enriching dialogue contexts), Knowledge-Guided Entity Modeling (entity substitution and similarity constraints), and Dialogue-Entity Matching (attention aggregation for user representations).

**Key findings**:
- DACRS consistently outperforms state-of-the-art CRSs on two public benchmark datasets
- Two-stage dialogue augmentation improves robustness to linguistic variation and open-ended expressions
- Knowledge-guided entity modeling enhances representation learning for sparsely supervised and unseen entities
- Dialogue-guided attention aggregation captures both explicit and implicit user preferences
- Entity substitution and similarity constraints effectively leverage knowledge graphs despite sparse supervision

**Limitations**: The approach relies on large knowledge graphs which may not be available for all recommendation domains, and the three-module framework introduces additional computational complexity during training and inference.

### Bernard and Balog (2025)

**Research question**: How can simulation-based evaluation resources for conversational recommender systems be upgraded to align with state-of-the-art research capabilities?

**Methodology**: Enhanced the UserSimCRS toolkit with an improved agenda-based user simulator, introduced LLM-based simulators, expanded integration for wider CRS and dataset compatibility, and added LLM-as-a-judge evaluation utilities, demonstrated through a case study.

**Key findings**:
- UserSimCRS v2 successfully aligns the toolkit with state-of-the-art CRS research
- LLM-based simulators provide more realistic and diverse user interaction patterns
- Enhanced agenda-based simulator improves simulation fidelity
- Wider CRS and dataset integration increases toolkit applicability
- LLM-as-a-judge utilities enable automated, scalable evaluation of CRS performance

**Limitations**: Simulation-based evaluation inherently cannot fully capture real user behavior and preferences, and LLM-as-judge evaluation may inherit biases from the underlying language models used.

### Zhang et al. (2025)

**Research question**: What is the current research landscape of simulation methods in conversational recommender systems and what are the key challenges and future directions?

**Methodology**: Developed a taxonomy framework to systematically categorize relevant publications into four groups: dataset construction, algorithm design, system evaluation, and empirical studies, providing comprehensive analysis of simulation methods in CRS research.

**Key findings**:
- Simulation methods play a key role in tackling CRS's main challenges
- LLM-based simulation methods have been used for data creation, algorithm enhancement, and system evaluation
- Persistent challenges include dataset bias, limited output flexibility of LLM-based simulations, and gap between text semantic space and behavioral semantics
- Complexity in Human-Computer Interaction of CRSs contributes to ongoing challenges
- Simulation methods hold significant potential for advancing CRS research despite existing challenges

**Limitations**: As a review paper, it identifies challenges rather than solving them; the complexity in HCI of CRSs remains unresolved; findings depend on the scope and selection criteria of the reviewed literature.

### Li et al. (2026)

**Research question**: How can user simulators for CRS evaluation better model realistic human decision-making, including hesitation and decision deferral commonly observed in real consumer behavior?

**Methodology**: Proposes Hesitator, a theory-grounded user simulation framework with a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions.

**Key findings**:
- Integrating the Decision Module consistently mitigates unrealistic behaviors under increasing overload conditions
- Reproduces established behavioral patterns from psychological economics
- Demonstrates ability to model human decision behavior more realistically than existing LLM-based simulators
- Validated across multiple user simulation frameworks, domains, sales modes, and LLM backbones
- Addresses the problem of overly high acceptance probabilities in existing simulators

**Limitations**: The abstract does not explicitly state limitations; potential concerns include validation against actual human user behavior data and applicability across diverse product categories beyond tested domains.

## References

Bernard, N., & Balog, K. (2025). UserSimCRS v2: Simulation-based evaluation for conversational recommender systems. arXiv. https://arxiv.org/abs/2512.04588v3

Bernard, N., Joko, H., Hasibi, F., & Balog, K. (2024). CRS Arena: Crowdsourced benchmarking of conversational recommender systems. arXiv. https://arxiv.org/abs/2412.10514v1

Chen, N., Dai, Q., Dong, X., Wang, P., Jia, Q., Du, Z., Dong, Z., & Wu, X.-M. (2025). Evaluating conversational recommender systems via large language models: A user-centric framework. arXiv. https://arxiv.org/abs/2501.09493v4

Li, Y.-C., Chen, L.-C., Wu, S.-Y., Tsai, Y.-C., & Lin, S.-D. (2026). Decision-aware user simulation agent for evaluating conversational recommender systems. arXiv. https://arxiv.org/abs/2605.05250v1

Surana, R., Wu, J., Xie, Z., Xia, Y., Kallus, N., & McAuley, J. (2025). An empirical study on zero-data bootstrapping for conversational recommender systems. arXiv. https://arxiv.org/abs/2504.15476v2

Yang, D., & Fang, H. (2025). ReGeS: Reciprocal retrieval-generation synergy for conversational recommender systems. arXiv. https://arxiv.org/abs/2509.21371v1

Zhang, H., Zhao, X., Chen, J., & Guo, J. (2025). A literature review on simulation in conversational recommender systems. arXiv. https://arxiv.org/abs/2506.20291v1

Zhang, S., Liu, M., Yuan, W., Yin, H., & Long, C. (2025). On mitigating data sparsity in conversational recommender systems. arXiv. https://arxiv.org/abs/2507.00479v2

Zhu, Y., Wan, C., Steck, H., Liang, D., Feng, Y., Kallus, N., & Li, J. (2025). Collaborative retrieval for large language model-based conversational recommender systems. arXiv. https://arxiv.org/abs/2502.14137v1

Zou, J., Lin, C., Guo, W., Wang, Z., Wei, J., Yang, Y., & Shen, H. T. (2025). Multi-type context-aware conversational recommender systems via mixture-of-experts. arXiv. https://arxiv.org/abs/2504.13655v2
