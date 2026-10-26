# Systematic Literature Review: Conversational Recommender Systems

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "conversational recommender", filtered to category cs.IR, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Conversational recommender systems (CRS) have evolved significantly over the past two years, with research focusing on six major directions: unifying recommendation and dialog generation through generative architectures, enriching contextual understanding through multi-modal and multi-source information, protecting user privacy through federated learning, developing robust evaluation platforms and methodologies, incorporating emotional intelligence into recommendations, and addressing data sparsity challenges. The literature reveals a field transitioning from modular, retrieval-based pipelines toward integrated, generative frameworks that leverage large language models and knowledge graphs. Collective findings demonstrate that modern CRS approaches achieve substantial improvements in recommendation accuracy (up to 29% gains) while increasingly addressing practical concerns including privacy, emotional engagement, evaluation scalability, and robustness to linguistic variation. However, significant gaps remain in real-world deployment validation, computational efficiency, and handling of evolving user preferences in dynamic environments.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "conversational recommender", filtered to category cs.IR, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Generative and Unified Architectures

A prominent direction in recent CRS research involves moving away from decoupled recommendation and dialog generation pipelines toward unified, generative frameworks. Zhang et al. (2026) propose a fully generative conversational recommender that represents items as discrete semantic IDs and integrates them directly into autoregressive generation, achieving up to 29% improvement on Recall@1 over baselines. This structured generation paradigm factorizes conversational recommendation into interdependent decisions—first predicting response intent and recommendation target, then generating the response conditioned on them—enabling end-to-end optimization and faithful item generation via constrained decoding. This represents a fundamental shift from retrieval-based approaches that treat recommendation and response generation as separate stages, instead treating both as joint next-token prediction tasks within a single language model framework.

### Theme 2: Context Enrichment and Multi-Modal Understanding

Multiple papers address the challenge of enriching conversational context to improve preference modeling. Zou et al. (2025) introduce MCCRS, a mixture-of-experts architecture that fuses multi-type contextual information including structured knowledge graphs, unstructured conversation history, and item reviews, with each expert specialized in one context type coordinated by a ChairBot. Yuan et al. (2026) propose STARCRS, which integrates two complementary text understanding modes: a screen-reading pathway encoding auxiliary text as visual tokens (mimicking human skim-reading) and an LLM-based textual pathway for fine-grained reasoning on critical content. Both approaches recognize that single-source context is insufficient for accurate preference inference, but differ in their fusion strategies—MCCRS uses expert coordination while STARCRS employs knowledge-anchored fusion with contrastive alignment, cross-attention, and adaptive gating. These methods address practical challenges including input length constraints, text style inconsistency, and irrelevant textual noise that arise from context enrichment.

### Theme 3: Privacy and Federated Learning

As CRS systems collect increasingly fine-grained, human-interpretable user preferences through natural language interactions, privacy concerns have become prominent. Lin et al. (2025) address this by proposing a federated conversational recommendation framework that de-centralizes both historical interests estimation and interactive preference elicitation stages, enforcing user-level differential privacy with carefully selected privacy budgets. Their approach recognizes that explicitly-communicated preferences in CRS can reveal sensitive information (financial status, political stands, health information) if breached, and demonstrates that competitive recommendation performance can be achieved even under strict privacy constraints. This represents an important counterbalance to the trend toward more expressive, context-rich models, ensuring that privacy protection does not require sacrificing recommendation quality.

### Theme 4: Evaluation and Benchmarking

A cluster of papers addresses the critical need for scalable, reliable CRS evaluation. Bernard et al. (2024) introduce CRS Arena, a crowdsourced platform for benchmarking CRS based on human feedback through pairwise battles between anonymous systems, releasing CRSArena-Dial with 474 conversations and Elo-based rankings. Bernard and Balog (2025) present UserSimCRS v2, upgrading simulation-based evaluation with enhanced agenda-based simulators, LLM-based simulators, and LLM-as-a-judge utilities for automated evaluation. Bernard and Balog (2024) also present a methodology for systematically identifying conversational breakdowns using user simulation as a diagnostic and development tool. Together, these works establish a multi-faceted evaluation ecosystem combining human feedback (CRS Arena), automated simulation (UserSimCRS v2), and systematic breakdown detection, addressing the field's historical reliance on static datasets and offline metrics that poorly correlate with real-world user satisfaction.

### Theme 5: Emotional and User-Centric Design

Recognizing that benchmark datasets may not reflect real user emotional needs, Zhang et al. (2024) introduce empathy into CRS through the ECR framework with emotion-aware item recommendation and emotion-aligned response generation modules. Their approach employs retrieval-augmented prompts to fine-tune language models for emotional alignment while mitigating hallucination, and enlarges training data using LLM-annotated emotion labels and external emotional reviews. This work challenges the assumption that standard benchmark items and responses are optimal, noting that users may express negative emotions with standard recommendations and feel disengaged by non-emotional responses. By refining preference modeling using user emotions and generating human-like emotional responses, ECR enhances both recommendation accuracy and user satisfaction on the ReDial dataset, suggesting that emotional alignment is not merely a superficial enhancement but fundamental to effective recommendation.

### Theme 6: Data Efficiency and Robustness

Two papers address fundamental data challenges in CRS training and deployment. Zhang et al. (2025) propose DACRS to mitigate severe data sparsity in both dialogue space (linguistically diverse expressions) and entity space (under-trained entities in knowledge graphs) through dialogue augmentation, knowledge-guided entity modeling with entity substitution and similarity constraints, and dialogue-entity matching. Zhang et al. (2024) introduce TCRS, reformulating CRS as tri-phase offline policy learning that reduces dependency on oversimplified user simulators by integrating model-based offline learning with controllable user simulation that dynamically aligns with evolving user preferences. Both approaches recognize that training data limitations—whether sparsity, linguistic variation, or simulator oversimplification—lead to models that perform well in controlled settings but fail in real deployment, and propose architectural solutions to improve generalization and robustness.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key points. First, all papers agree that traditional CRS architectures with decoupled recommendation and dialog components are insufficient, whether proposing generative unification (Zhang et al., 2026), multi-expert fusion (Zou et al., 2025), or offline policy learning (Zhang et al., 2024). Second, there is consensus that evaluation must move beyond static datasets toward dynamic, human-in-the-loop approaches, evidenced by three independent works on evaluation platforms and simulation (Bernard et al., 2024; Bernard & Balog, 2024; Bernard & Balog, 2025). Third, all papers employing knowledge graphs or external context agree that enrichment improves performance but introduces challenges (noise, length constraints, sparsity) requiring architectural solutions rather than simple concatenation. Finally, there is convergence on using LLMs not merely as response generators but as annotation tools (Zhang et al., 2024), evaluation judges (Bernard & Balog, 2025), and simulation agents (Bernard & Balog, 2025), suggesting a shift toward LLM-augmented development pipelines.

**Disagreements**: The literature reveals tensions in architectural philosophy. Generative unified approaches (Zhang et al., 2026) treat recommendation as token generation, while context-enrichment approaches (Zou et al., 2025; Yuan et al., 2026) maintain separation between understanding and generation stages, integrating context through fusion mechanisms rather than unified generation. There is also divergence in evaluation philosophy: crowdsourced human feedback (Bernard et al., 2024) prioritizes real user preferences but scales poorly, while LLM-as-a-judge (Bernard & Balog, 2025) scales well but may inherit model biases. Privacy-focused approaches (Lin et al., 2025) introduce constraints that may conflict with context-enrichment goals, as federated learning limits the types and granularity of context that can be centrally processed.

## Gaps and Open Questions

Several gaps emerge from the collective limitations acknowledged across the surveyed papers. First, **real-world deployment validation** remains limited—most papers evaluate on benchmark datasets (ReDial, two unnamed public datasets) rather than live deployment, with only CRS Arena (Bernard et al., 2024) collecting real user interactions, and even that in controlled crowdsourcing rather than organic usage. Second, **computational efficiency** is consistently unaddressed: generative architectures (Zhang et al., 2026), mixture-of-experts (Zou et al., 2025), vision-centric encoding (Yuan et al., 2026), and federated learning (Lin et al., 2025) all introduce substantial overhead without discussion of latency, memory, or cost implications for production systems. Third, **domain generalization** is rarely tested—most approaches assume availability of large knowledge graphs or domain-specific training data, leaving open questions about performance in low-resource domains or cold-start scenarios. Fourth, **long-term user modeling** is absent—all papers focus on single-session or short-term interactions, neglecting how CRS should model evolving preferences across weeks or months of interaction. Fifth, **multilingual and cross-cultural** considerations are entirely absent from the surveyed literature, with all approaches implicitly assuming English-language, Western cultural contexts. Finally, several papers acknowledge that their evaluation depends on the quality of LLM-annotated data (Zhang et al., 2024; Bernard & Balog, 2025), introducing potential annotation bias that is neither measured nor mitigated.

## Per-Paper Annotations

### Bernard and Balog (2024)

**Research question**: How can conversational recommender systems be systematically tested to identify and characterize conversational breakdowns?
**Methodology**: Presents a methodology to systematically test CRS by examining conversations between the system and simulated users for pre-defined breakdown types, extracting responsible conversational paths, and characterizing them by underlying dialogue intents.
**Key findings**:
- User simulation offers simplicity, cost-effectiveness, and time efficiency for obtaining breakdown-identifying conversations
- The methodology can serve as both a diagnostic tool and a development tool to improve CRS
- With just a few iterations, the system can be made more robust to conversational breakdowns
- Case study demonstrates practical applicability with existing CRS and user simulator
**Limitations**: User simulation may not capture all real-world user behaviors and breakdown scenarios; methodology is limited to pre-defined breakdown types which may not cover all failure modes.

### Bernard et al. (2024)

**Research question**: How can conversational recommender systems be benchmarked at scale based on human feedback?
**Methodology**: Introduces CRS Arena, a research platform that displays pairwise battles between anonymous CRSs where users interact with systems sequentially before declaring a winner or draw, collecting conversations and feedback for Elo-based ranking.
**Key findings**:
- Both open and closed crowdsourcing platforms produce highly correlated CRS rankings
- Conversations from both setups have similar characteristics
- Released CRSArena-Dial dataset containing 474 conversations with corresponding user feedback
- Platform is publicly accessible at https://iai-group-crsarena.hf.space/
**Limitations**: Dataset size is limited (474 conversations); rankings are preliminary and based on Elo rating system which may require more data for stable rankings.

### Bernard and Balog (2025)

**Research question**: How can simulation-based evaluation resources for CRS be upgraded to align with state-of-the-art research given the scarcity of such resources?
**Methodology**: Present UserSimCRS v2 with four key extensions: enhanced agenda-based user simulator, LLM-based simulators, integration support for wider range of CRSs and datasets, and new LLM-as-a-judge evaluation utilities, demonstrated through a case study.
**Key findings**:
- Enhanced agenda-based user simulator provides more realistic and structured user interaction patterns
- LLM-based simulators offer more flexible and natural conversation patterns compared to rule-based approaches
- Expanded integration enables evaluation across a wider range of CRS models and datasets
- LLM-as-a-judge utilities enable automated, scalable evaluation of conversation quality without human annotators
**Limitations**: This is primarily a toolkit upgrade rather than novel algorithmic research, with validation limited to a case study rather than comprehensive comparative evaluation. The LLM-as-a-judge approach may inherit biases from the underlying language models used for evaluation.

### Lin et al. (2025)

**Research question**: How can user privacy be protected in conversational recommender systems that collect and store explicitly-communicated fine-grained user preferences?
**Methodology**: Proposes a federated CRS framework that de-centralizes both historical interests estimation and interactive preference elicitation stages, enforcing user-level differential privacy with carefully selected privacy budgets based on defined privacy protection guidelines.
**Key findings**:
- Framework satisfies the defined user privacy protection guidelines for CRS
- Achieves competitive recommendation performance compared to state-of-the-art non-private approaches
- Effectively reduces risk of exposing sensitive user information (financial status, political stands, health information)
- User-level differential privacy can be enforced without severely degrading recommendation quality
**Limitations**: Privacy budget selection involves trade-offs between privacy protection and recommendation performance; federated learning introduces communication overhead and coordination complexity compared to centralized approaches.

### Zhang et al. (2024)

**Research question**: How can CRS training reduce dependency on oversimplified user simulators that focus on static attributes and neglect evolving user preferences, causing models to fail in real deployment?
**Methodology**: Introduce TCRS (Tri-Phase Offline Policy Learning-based CRS) that integrates model-based offline learning strategy with controllable user simulation that dynamically aligns with personalized and evolving user preferences, reducing dependency on real-time interactions.
**Key findings**:
- Tri-phase offline policy learning significantly reduces dependency on real-time user interactions during training
- Controllable user simulation better captures personalized and evolving user preferences compared to static simulators
- Model-based offline learning strategy effectively mitigates overfitting issues prevalent in traditional approaches
- TCRS demonstrates enhanced robustness and adaptability across diverse user scenarios
**Limitations**: The offline learning approach may not fully capture real-time interaction dynamics and emergent user behaviors. The effectiveness depends heavily on the quality and controllability of the user simulation, which may still not perfectly match real-world user complexity.

### Zhang et al. (2024)

**Research question**: How can conversational recommender systems better address user emotional needs rather than just replicating dataset logic that overlooks negative emotions and emotional engagement?
**Methodology**: Propose an Empathetic Conversational Recommender (ECR) framework with two modules: emotion-aware item recommendation and emotion-aligned response generation, employing retrieval-augmented prompts to fine-tune a pre-trained language model and enlarging empathetic data using LLM-annotated emotion labels and external emotional reviews.
**Key findings**:
- User emotions can effectively refine preference modeling to produce more accurate recommendations
- Retrieval-augmented prompts enable generation of human-like emotional responses while mitigating hallucination
- LLM-annotated emotion labels and external emotional reviews successfully address insufficient supervision
- Novel evaluation metrics better capture user satisfaction in real-world CRS scenarios compared to standard benchmarks
**Limitations**: The evaluation is limited to the ReDial dataset, and the approach depends on the quality of LLM-annotated emotion labels which may introduce annotation bias.

### Zhang et al. (2025)

**Research question**: How can CRS models overcome severe data sparsity in both dialogue space (linguistically diverse expressions) and entity space (under-trained entities in knowledge graphs)?
**Methodology**: Propose DACRS with three modules: Dialogue Augmentation (two-stage pipeline for enriching dialogue contexts), Knowledge-Guided Entity Modeling (entity substitution and similarity constraints for sparse/unseen entities), and Dialogue-Entity Matching (dialogue-guided attention aggregation for user representations).
**Key findings**:
- Two-stage dialogue augmentation significantly improves robustness to linguistic variation in open-ended conversations
- Entity substitution leveraging knowledge graphs enhances representation learning for sparsely supervised entities
- Entity similarity constraints enable effective handling of entirely unseen entities at inference time
- DACRS consistently outperforms state-of-the-art CRS models across two public benchmark datasets
**Limitations**: The approach relies on large knowledge graphs which may not be available or comprehensive for all domains. Evaluation is limited to two public benchmark datasets, and the effectiveness may vary for domains with different entity distributions.

### Zhang et al. (2026)

**Research question**: How can recommendation and dialog generation be better integrated in conversational recommender systems rather than being decoupled or relying on retrieval-based pipelines?
**Methodology**: Proposes a fully generative CRS that unifies recommendation and dialog generation within a single autoregressive framework, representing items as discrete semantic IDs and introducing a structured generation paradigm that factorizes recommendation into interdependent decisions.
**Key findings**:
- Achieves up to 29% improvement on Recall@1 over strong baselines
- Maintains competitive dialog quality while improving recommendation performance
- Structured generation enables end-to-end optimization with coherent dependency structure
- Constrained decoding supports faithful item generation
**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include computational complexity of autoregressive generation and generalization to unseen item domains.

### Yuan et al. (2026)

**Research question**: How can CRS models handle longer and more heterogeneous conversational contexts while addressing practical issues like input length constraints, text style inconsistency, and irrelevant textual noise?
**Methodology**: Propose STARCRS (Screen-Text-AwaRe CRS) with two complementary pathways: screen-reading (encoding auxiliary text as visual tokens mimicking skim reading) and LLM-based textual pathway (fine-grained reasoning on critical content), integrated through knowledge-anchored fusion with contrastive alignment, cross-attention, and adaptive gating.
**Key findings**:
- Screen-reading pathway effectively encodes auxiliary textual information as visual tokens, mimicking human skim-reading behavior
- LLM-based textual pathway enables focused fine-grained reasoning on limited critical content
- Knowledge-anchored fusion framework successfully integrates both pathways through contrastive alignment and cross-attention
- STARCRS consistently improves both recommendation accuracy and generated response quality on two widely used benchmarks
**Limitations**: The vision-centric approach requires additional computational resources for visual token encoding and processing. The method's effectiveness depends on the quality and relevance of auxiliary textual information.

### Zou et al. (2025)

**Research question**: How can different types of contextual information (structured and unstructured) be effectively combined to improve conversational recommender systems?
**Methodology**: Proposes MCCRS that fuses multi-type contextual information (knowledge graph, conversation history, item reviews) via a mixture-of-experts architecture where each expert specializes in one context type, coordinated by a ChairBot to generate final results.
**Key findings**:
- Significantly higher performance compared to existing baselines
- Mixture-of-experts approach breaks the model bottleneck on single contextual information
- Successfully integrates both structured (knowledge graph) and unstructured (conversation history, item reviews) information
- ChairBot coordination effectively combines specialized expert outputs
**Limitations**: The abstract does not explicitly state limitations; potential concerns include complexity of coordinating multiple experts and scalability with increasing context types.

## References

Bernard, N., & Balog, K. (2024). Identifying breakdowns in conversational recommender systems using user simulation. arXiv. https://arxiv.org/abs/2405.14249

Bernard, N., & Balog, K. (2025). UserSimCRS v2: Simulation-based evaluation for conversational recommender systems. arXiv. https://arxiv.org/abs/2512.04588

Bernard, N., Joko, H., Hasibi, F., & Balog, K. (2024). CRS Arena: Crowdsourced benchmarking of conversational recommender systems. arXiv. https://arxiv.org/abs/2412.10514

Lin, A., Wang, J., Zhu, Z., & Caverlee, J. (2025). Federated conversational recommender system. arXiv. https://arxiv.org/abs/2503.00999

Yuan, W., Qiao, S., Chen, T., Nguyen, Q. V. H., Huang, Z., & Yin, H. (2026). Integrating vision-centric text understanding for conversational recommender systems. arXiv. https://arxiv.org/abs/2601.13505

Zhang, G., Gao, C., Pan, H., Teng, R., & Li, R. (2024). Reformulating conversational recommender systems as tri-phase offline policy learning. arXiv. https://arxiv.org/abs/2408.06809

Zhang, S., Liu, M., Yuan, W., Yin, H., & Long, C. (2025). On mitigating data sparsity in conversational recommender systems. arXiv. https://arxiv.org/abs/2507.00479

Zhang, S., Liu, M., & Long, C. (2026). Generative conversational recommender system. arXiv. https://arxiv.org/abs/2605.21987

Zhang, X., Xie, R., Lyu, Y., Xin, X., Ren, P., Liang, M., Zhang, B., Kang, Z., de Rijke, M., & Ren, Z. (2024). Towards empathetic conversational recommender systems. arXiv. https://arxiv.org/abs/2409.10527

Zou, J., Lin, C., Guo, W., Wang, Z., Wei, J., Yang, Y., & Shen, H. T. (2025). Multi-type context-aware conversational recommender systems via mixture-of-experts. arXiv. https://arxiv.org/abs/2504.13655
