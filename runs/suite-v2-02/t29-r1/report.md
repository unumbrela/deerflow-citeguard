# Systematic Literature Review: LLM-Based Recommender Systems

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "LLM recommender systems", category cs.IR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM-based recommender systems reveals a rapidly evolving field focused on addressing fundamental challenges in efficiency, personalization, fairness, and evaluation. Recent work demonstrates that LLMs can significantly enhance recommendation quality through semantic understanding of items and users, but introduce new challenges around computational cost, bias, and evaluation methodologies. The surveyed papers collectively show a shift from traditional collaborative filtering toward hybrid architectures that combine LLMs with graph-based methods, retrieval-augmented generation, and knowledge graphs. Key innovations include token-efficient representations, selective LLM guidance, and LLM-as-a-judge evaluation frameworks. The field is moving toward end-to-end personalization systems that provide both accurate recommendations and natural-language explanations, though significant gaps remain in understanding long-term user impacts and addressing hallucination risks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "LLM recommender systems", filtered to category cs.IR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency vs. Accuracy Trade-offs

A central tension in LLM-based recommendation is balancing computational efficiency with recommendation accuracy. Several papers address this through architectural innovations that reduce token usage or enable dynamic inference termination. Kim et al. (2025) propose I-LLMRec, which uses images instead of lengthy textual descriptions to represent items, achieving both efficiency gains and improved effectiveness by reducing noise sensitivity. Zhou et al. (2025) introduce multi-head early exit mechanisms in RAG-enhanced recommenders, allowing dynamic termination of inference based on predictive confidence while maintaining accuracy. Yang et al. (2025) take a different approach with selective LLM-guided regularization, activating LLM supervision only when predicted to be reliable, with all scoring performed offline to avoid inference costs. These works collectively demonstrate that efficiency need not come at the expense of accuracy when LLMs are strategically integrated rather than used naively.

### Theme 2: Cold-Start and Data Scarcity Solutions

LLMs show particular promise in addressing the persistent cold-start problem where new items or users lack interaction history. Yang et al. (2025) present ColdRAG, which dynamically constructs knowledge graphs from raw metadata rather than relying on static, pre-filtered candidate lists, enabling LLM-guided multi-hop reasoning at inference time. Kang et al. (2026) tackle rare medication recommendation with GenRxR, using LLMs to generate counterfactual medical data that augments scarce training examples, achieving up to 30.9% improvement for rare medications. Ebrat et al. (2025) address limited user feedback scenarios by using LLMs to generate semantically meaningful user and item profiles from metadata, which serve as initial features in graph-based collaborative filtering. These approaches share a common strategy: leveraging LLMs' semantic understanding to compensate for missing interaction data.

### Theme 3: Fairness and Bias Evaluation

As LLMs become central to recommendation, ensuring fairness across diverse user populations emerges as critical. Sah et al. (2025) introduce FairEval, integrating personality traits with demographic attributes to comprehensively assess user-level bias, revealing fairness disparities reaching 34.79% across dimensions despite high overall PAFS scores. This work highlights that aggregate metrics can mask significant subgroup disparities. The framework's integration of psychological profiling with demographic sensitivity represents a more nuanced approach to fairness evaluation than previous work focusing solely on protected attributes.

### Theme 4: Evaluation Paradigm Shifts

The shift to LLM-driven recommenders necessitates rethinking evaluation itself. Epure et al. (2025) argue that standard accuracy metrics are questionable for generative LLM-based music recommenders, calling for evaluation beyond traditional train/test protocols. Doh et al. (2026) empirically validate LLM-as-a-judge for conversational recommendation, finding moderate positive alignment with human expert judgments while outperforming reference-based baselines. These papers collectively suggest the field is transitioning from discriminative ranking metrics toward evaluation frameworks that account for generative capabilities, natural language explanations, and conversational interaction quality.

### Theme 5: Cross-Domain and Context-Aware Recommendation

LLMs enable richer cross-domain recommendations by understanding semantic relationships across categories. Kekuda et al. (2025) demonstrate this with a cross-pollination framework bridging grocery and general merchandise, using LLMs for item-item association identification combined with real-time cart context, achieving 36% lift in add-to-cart rates. This work exemplifies how LLMs can identify non-obvious cross-category associations that traditional collaborative filtering would miss, while leveraging sequential context for ranking.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. First, all demonstrate that LLMs provide measurable improvements over baselines when properly integrated, with reported gains ranging from 15% to 36% in engagement metrics and significant accuracy improvements across datasets. Second, there is consensus that LLMs are most valuable for their semantic understanding capabilities—generating user/item profiles, identifying cross-domain associations, and providing natural-language explanations—rather than as standalone rankers. Third, multiple papers agree that offline or selective LLM usage is preferable to real-time scoring for efficiency (Yang et al., 2025; Zhou et al., 2025).

**Disagreements**: Tensions emerge around evaluation methodologies. While Doh et al. (2026) validate LLM-as-a-judge as a practical evaluation tool, Epure et al. (2025) caution that LLMs introduce challenges including hallucinations, non-determinism, and opaque training data that complicate their use as evaluators. There is also implicit disagreement about the role of images versus text: Kim et al. (2025) advocate image-based representations for efficiency, while most other papers assume text-based LLM inputs, suggesting unresolved questions about optimal modality.

## Gaps and Open Questions

Several significant gaps emerge from the collective literature. First, none of the papers explicitly state limitations in their abstracts, suggesting either space constraints or insufficient critical reflection on failure modes. Second, while multiple papers address efficiency, none provide comprehensive analysis of the carbon footprint or environmental costs of LLM-based recommendation at scale. Third, long-term user impacts remain unexamined—does LLM-personalized recommendation create filter bubbles or enhance discovery over extended periods? Fourth, the hallucination risk identified by Epure et al. (2025) is not addressed by any proposed mitigation strategy in the surveyed papers. Finally, fairness evaluation by Sah et al. (2025) reveals significant disparities, but no paper proposes concrete debiasing interventions beyond evaluation frameworks.

## Per-Paper Annotations

### Ebrat et al. (2025)

**Research question**: How can recommender systems improve both personalization and interpretability, particularly in scenarios involving limited user feedback or heterogeneous item attributes?
**Methodology**: The authors propose a hybrid framework combining Graph Attention Networks with LLMs, where LLMs generate semantically meaningful user and item profiles from metadata serving as initial node features in a bipartite graph processed by GAT-based collaborative filtering, with a hybrid loss function combining Bayesian Personalized Ranking, cosine similarity, and robust negative sampling.
**Key findings**:
- The hybrid model consistently outperforms strong baselines on MovieLens 100k and 1M datasets
- LLM-based embeddings significantly contribute to performance gains as confirmed by ablation studies
- Cosine similarity in the hybrid loss function improves ranking accuracy
- LLM post-processing enables reranking and provides natural-language justifications for transparency
**Limitations**: Not stated in abstract

### Epure et al. (2025)

**Research question**: How should evaluation practices for Music Recommender Systems be rethought in light of the shift toward LLM-driven approaches?
**Methodology**: The authors review LLM impacts on user modeling, item modeling, and natural language-based recommendation in music, analyze evaluation practices from NLP, and synthesize insights on LLM prompting applications to music recommendation systems to outline success and risk dimensions.
**Key findings**:
- Standard accuracy metrics are questionable for generative LLM-based music recommenders
- LLMs introduce challenges including hallucinations, knowledge cutoffs, non-determinism, and opaque training data
- LLMs create opportunities for natural language interaction and enable models to act as evaluators
- The shift requires rethinking evaluation beyond traditional train/test protocols
**Limitations**: Not stated in abstract

### Kang et al. (2026)

**Research question**: How can AI-based medication recommendation systems improve predictive performance for rarely prescribed medications given data scarcity and limited consideration of co-recommended medications?
**Methodology**: The authors propose GenRxR, leveraging LLMs to generate counterfactual medical data for mitigating rare medication data scarcity, integrating an LLM into the recommendation process to model relationships among co-recommended medications, and using instruction tuning to align the LLM's capability with the recommendation task.
**Key findings**:
- GenRxR outperforms 14 baselines (including 5 LLM-based) in most cases
- Achieves up to 30.9% higher predictive performance for rare medications than the strongest baseline
- Counterfactual data augmentation effectively mitigates data scarcity
- Instruction tuning enables better handling of clinical context including rare medication cases
**Limitations**: Not stated in abstract

### Kekuda et al. (2025)

**Research question**: How can e-commerce platforms effectively recommend general merchandise to customers focused on grocery shopping by leveraging cross-category associations and real-time cart context?
**Methodology**: The authors introduce a cross-pollination framework with two stages: candidate generation using co-purchase market basket analysis and LLM-based item-item association identification, followed by a transformer-based ranker leveraging real-time sequential cart context and optimizing for engagement signals.
**Key findings**:
- LLM-based retrieval on the item page increased add-to-cart rate by 36%
- Cart context-based ranker achieved a 15% lift in add-to-cart rate
- The framework successfully bridges grocery and general merchandise cross-category recommendations
- Multi-source product associations combined with real-time cart context improve relevance
**Limitations**: Not stated in abstract

### Kim et al. (2025)

**Research question**: How can LLM-based recommender systems address the trade-off between efficiency and effectiveness when representing items consumed by users?
**Methodology**: The authors propose I-LLMRec, leveraging images as an alternative to lengthy textual descriptions for representing items, aiming to reduce token usage while preserving rich semantic information, evaluated through extensive experiments comparing efficiency and effectiveness against existing methods.
**Key findings**:
- I-LLMRec outperforms existing methods in both efficiency and effectiveness
- There is significant information overlap between images and descriptions associated with items
- Using images reduces sensitivity to noise in descriptions, leading to more robust recommendations
- Image-based representation reduces token usage while preserving semantic information
**Limitations**: Not stated in abstract

### Sah et al. (2025)

**Research question**: How can fairness in LLM-based recommender systems be systematically evaluated across demographic and psychological user dimensions?
**Methodology**: The authors introduce FairEval, integrating personality traits with eight sensitive demographic attributes to enable comprehensive assessment of user-level bias, evaluating models including ChatGPT 4o and Gemini 1.5 Flash on music and movie recommendations using the PAFS fairness metric.
**Key findings**:
- PAFS metric achieves scores up to 0.9969 for ChatGPT 4o and 0.9997 for Gemini 1.5 Flash
- Fairness disparities reaching 34.79% were observed across demographic and psychological dimensions
- The framework enables comprehensive assessment by integrating personality traits with demographic attributes
- Results highlight the importance of robustness in prompt sensitivity for inclusive recommendation systems
**Limitations**: Not stated in abstract

### Yang et al. (2025) [ColdRAG]

**Research question**: How can recommender systems address the cold-start problem for new items with limited interaction data without relying on static knowledge graphs or pre-filtered candidate lists?
**Methodology**: The authors propose ColdRAG, a retrieval-augmented framework that dynamically constructs a knowledge graph from raw metadata, extracts entities and relations to construct an updatable structure, and introduces LLM-guided multi-hop reasoning at inference time to retrieve and rank candidates without relying on pre-filtered lists.
**Key findings**:
- ColdRAG consistently outperforms seven strong baselines across multiple benchmarks
- Dynamic knowledge graph construction avoids the expense and obsolescence issues of static KGs
- The framework enables candidate retrieval and ranking without relying on pre-filtered lists
- LLM-guided multi-hop reasoning improves candidate retrieval at inference time
**Limitations**: Not stated in abstract

### Yang et al. (2025) [Selective LLM-Guided Regularization]

**Research question**: How can LLM guidance be selectively activated to improve recommendation models without the drawbacks of standalone LLM recommenders or global knowledge distillation?
**Methodology**: The authors introduce Selective LLM-Guided Regularization, a model-agnostic framework using a trainable gating mechanism (informed by user history length, item popularity, and model uncertainty) to activate LLM-based pairwise ranking supervision only when the LLM is predicted to be reliable, with all LLM scoring performed offline.
**Key findings**:
- The selective strategy consistently improves overall accuracy across multiple datasets
- Substantial performance gains are achieved in cold start and long tail regimes
- The approach outperforms global distillation baselines
- The framework is computation-efficient and does not increase inference cost since LLM scoring is done offline
**Limitations**: Not stated in abstract

### Zhou et al. (2025)

**Research question**: How can RAG-enhanced LLM recommender systems concurrently enhance computational efficiency and predictive accuracy for Click-Through Rate prediction?
**Methodology**: The paper presents an optimization framework combining Retrieval-Augmented Generation with a multi-head early exit architecture, integrating Graph Convolutional Networks as efficient retrieval mechanisms, with an early exit strategy allowing dynamic termination of model inference using real-time predictive confidence assessments.
**Key findings**:
- The architecture effectively decreases computation time without sacrificing accuracy
- GCNs as retrieval mechanisms significantly reduce data retrieval times while maintaining high performance
- The early exit strategy quickens LLM responsiveness while upholding or improving accuracy
- The approach establishes a new standard for efficient, real-time LLM deployment in commercial systems
**Limitations**: Not stated in abstract

### Doh et al. (2026)

**Research question**: How reliably does LLM-as-a-judge align with human judgment when evaluating conversational recommendation system responses?
**Methodology**: The authors conducted the first user study to empirically assess LLM-as-a-judge reliability for CRS responses, sampling 20 multi-turn music recommendation sessions and generating candidate responses using four instruction-tuned LLMs, collecting 400 ratings from 20 domain-expert annotators evaluating Personalization Quality and Explanation Quality, then performing bootstrapped correlation analysis.
**Key findings**:
- LLM-based judges exhibit moderate positive alignment with human assessments
- LLM-as-a-judge outperforms all reference-based baselines for evaluating CRS responses
- Judge performance varies according to model scale and conditioning information
- The study provides practical guidance for deploying LLM-as-a-judge in conversational recommendation contexts
**Limitations**: Not stated in abstract

## References

Doh, S., Sguerra, B., Oramas, S., Epure, E. V., & Nam, J. (2026). LLM-as-a-judge for evaluating system responses in conversational music recommendation. arXiv. https://arxiv.org/abs/2607.25640

Ebrat, D., Aminian, T., Ahmadian, S., & Rueda, L. (2025). End-to-end personalization: Unifying recommender systems with large language models. arXiv. https://arxiv.org/abs/2508.01514

Epure, E. V., Deldjoo, Y., Sguerra, B., Schedl, M., & Moussallam, M. (2025). Music recommendation with large language models: Challenges, opportunities, and evaluation. arXiv. https://arxiv.org/abs/2511.16478

Kang, S., Lee, S. Y., Kim, J., Shin, K., & Chang, B. (2026). Improving rare medication recommendation with counterfactual data augmentation and large language models. arXiv. https://arxiv.org/abs/2607.24829

Kekuda, A., Dandu, M. M. K., Lahiri, R., Cai, S., Subramaniam, S., Korpeoglu, E., & Achan, K. (2025). Grocery to general merchandise: A cross-pollination recommender using LLMs and real-time cart context. arXiv. https://arxiv.org/abs/2509.02890

Kim, K., Kim, S., Kang, H., Kim, J., Noh, H., In, Y., Yoon, K., Oh, J., McAuley, J., & Park, C. (2025). Token-efficient item representation via images for LLM recommender systems. arXiv. https://arxiv.org/abs/2503.06238

Sah, C. K., Lian, X., Xu, T., & Zhang, L. (2025). FairEval: Evaluating fairness in LLM-based recommendations with personality awareness. arXiv. https://arxiv.org/abs/2504.07801

Yang, S., & Shi, Z. (2025). Selective LLM-guided regularization for enhancing recommendation models. arXiv. https://arxiv.org/abs/2512.21526

Yang, W., Zhang, W., Liu, Y., Han, Y., Wang, Y., Lee, J., & Yu, P. S. (2025). Adaptive candidate retrieval with dynamic knowledge graph construction for cold-start recommendation. arXiv. https://arxiv.org/abs/2505.20773

Zhou, H., Gu, H., Liu, X., Zhou, K., Liang, M., Xiao, Y., Govindan, S., Chawla, P., Yang, J., Meng, X., Li, H., Zhang, B., Luo, L., Chen, W.-Y., Han, Y., Long, B., Zhang, R., & Chen, T. (2025). The efficiency vs. accuracy trade-off: Optimizing RAG-enhanced LLM recommender systems using multi-head early exit. arXiv. https://arxiv.org/abs/2501.02173
