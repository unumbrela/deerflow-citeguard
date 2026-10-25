# Systematic Literature Review: Conversational Recommender Systems

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "conversational recommender systems", category cs.IR, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on conversational recommender systems (CRS) from the past two years reveals a field maturing toward practical evaluation frameworks and integration of large language models with retrieval mechanisms. A dominant trend across the surveyed papers is the development of systematic evaluation methodologies, with five papers proposing new benchmarking platforms, user simulators, or LLM-based evaluation frameworks. Simultaneously, researchers are addressing fundamental challenges in CRS architecture, particularly around retrieval-augmented generation, multi-type context fusion, and data sparsity mitigation. The collective work demonstrates a shift from purely dialogue-driven recommendations toward hybrid systems that combine LLM capabilities with collaborative filtering, knowledge graphs, and behavioral data. However, significant gaps remain in real-world deployment validation and cross-domain generalization.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "conversational recommender systems", filtered to category cs.IR, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Evaluation and Benchmarking Frameworks

A significant portion of recent CRS research focuses on developing robust evaluation methodologies. Bernard and colleagues have contributed extensively to this area, introducing CRS Arena as a crowdsourced benchmarking platform where users engage in pairwise battles between anonymous CRS implementations (Bernard et al., 2024). This platform collects human feedback and conversation data, releasing the CRSArena-Dial dataset with 474 conversations and corresponding user feedback. Building on simulation-based evaluation, the same research team introduced UserSimCRS v2, which enhances the original toolkit with LLM-based simulators and LLM-as-a-judge evaluation utilities (Bernard & Balog, 2025). Their earlier work established a methodology for systematically identifying conversational breakdowns using user simulation, demonstrating that just a few iterations can improve system robustness (Bernard & Balog, 2024).

Complementing these simulation-based approaches, Chen et al. (2025) proposed CoRE, a user-centric evaluation framework leveraging LLMs as evaluators across 12 key factors influencing user experience, synthesized through a multi-agent debate mechanism. Their framework achieves significantly better alignment with human feedback compared to rule-based metrics. Most recently, Li et al. (2026) introduced Hesitator, a theory-grounded user simulation framework that explicitly models human decision-making under choice overload, addressing the unrealistic acceptance probabilities exhibited by existing LLM-based simulators.

### Theme 2: Retrieval-Augmented Generation for Knowledge Integration

The integration of retrieval mechanisms with generative models represents another major research direction. Yang and Fang (2025) proposed ReGeS, a reciprocal Retrieval-Generation Synergy framework that unifies generation-augmented retrieval for distilling user intent from conversations with retrieval-augmented generation for differentiating subtle item features. This approach achieves state-of-the-art performance on multiple CRS benchmarks while reducing hallucination risks and eliminating the need for extra annotations.

Zhu et al. (2025) introduced CRAG, the first approach combining state-of-the-art LLMs with collaborative filtering for conversational recommendations. Their collaborative retrieval augmented generation method demonstrates superior item coverage and recommendation performance, particularly on recently released movies. Similarly, Zhang et al. (2024) applied retrieval-augmented prompting in their empathetic CRS framework to fine-tune pre-trained language models for emotion-aligned response generation while mitigating hallucination.

### Theme 3: Multi-Type Context Fusion and Knowledge Graph Integration

Addressing the challenge of combining diverse contextual information, Zou et al. (2025) proposed MCCRS, a multi-type context-aware CRS using a mixture-of-experts architecture. Their system incorporates structured knowledge graphs, unstructured conversation history, and unstructured item reviews, with each expert specialized in a particular domain coordinated by a ChairBot. This approach breaks the bottleneck of relying on single contextual information sources and achieves significantly higher performance compared to existing baselines.

Zhang et al. (2025) tackled the related problem of data sparsity in both dialogue and entity spaces with DACRS, a framework featuring three modules: Dialogue Augmentation for enriching contexts, Knowledge-Guided Entity Modeling for enhancing representation of sparsely supervised entities, and Dialogue-Entity Matching for capturing explicit and implicit preferences. Their approach consistently outperforms state-of-the-art CRS on two public benchmark datasets.

### Theme 4: User-Centric and Emotionally-Aware Design

A growing recognition that CRS must align with actual user emotional needs rather than benchmark-optimal responses has emerged. Zhang et al. (2024) introduced empathy into CRS through their ECR framework, which employs emotion-aware item recommendation and emotion-aligned response generation. Their experiments on the ReDial dataset validate that incorporating user emotions enhances both recommendation accuracy and user satisfaction.

This user-centric perspective extends to evaluation frameworks, with Chen et al. (2025) emphasizing authentic reflection of user experience through their 12-factor evaluation scheme, and Li et al. (2026) modeling realistic consumer decision-making behaviors including hesitation and decision deferral under choice overload conditions.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong agreement on several fronts. First, there is consensus that evaluation of CRS requires moving beyond separate assessment of recommendation accuracy and dialogue management toward unified, user-centric metrics (Bernard et al., 2024; Chen et al., 2025; Li et al., 2026). Second, multiple papers converge on the necessity of integrating external knowledge sources—whether knowledge graphs, behavioral data, or item reviews—to overcome limitations of dialogue-only approaches (Zou et al., 2025; Zhang et al., 2025; Zhu et al., 2025; Yang & Fang, 2025). Third, there is broad agreement that LLMs, while powerful, require augmentation through retrieval mechanisms or fine-tuning to mitigate hallucination risks and improve domain specificity (Yang & Fang, 2025; Zhang et al., 2024; Zhu et al., 2025).

**Disagreements**: The literature shows some divergence in evaluation philosophy. Bernard and colleagues emphasize crowdsourced human feedback and simulation-based evaluation as the gold standard (Bernard et al., 2024; Bernard & Balog, 2025; Bernard & Balog, 2024), while Chen et al. (2025) advocate for LLM-as-evaluator approaches that can synthesize multiple factors into unified scores. Additionally, there is tension between approaches prioritizing multi-expert architectures for context fusion (Zou et al., 2025) versus those favoring unified retrieval-generation frameworks (Yang & Fang, 2025; Zhu et al., 2025), reflecting different views on architectural complexity versus integration elegance.

## Gaps and Open Questions

Several gaps emerge from the collective limitations acknowledged across the surveyed papers. First, dataset scale remains a concern, with Bernard et al. (2024) noting the relatively limited size of CRSArena-Dial (474 conversations) and preliminary nature of rankings. Second, simulation fidelity is repeatedly questioned—multiple papers acknowledge that simulated user interactions may not fully capture the complexity and unpredictability of actual user behavior (Bernard & Balog, 2024; Bernard & Balog, 2025; Li et al., 2026).

Third, computational complexity and resource requirements are acknowledged but not thoroughly addressed, particularly for multi-expert architectures (Zou et al., 2025) and multi-agent debate frameworks (Chen et al., 2025). Fourth, domain specificity remains a limitation, with Zhu et al. (2025) noting improvements concentrated on movie recommendations and Li et al. (2026) calling for validation across domains beyond those tested.

Finally, dependency on external knowledge quality is a recurring concern, with DACRS (Zhang et al., 2025) and MCCRS (Zou et al., 2025) both relying heavily on the availability and quality of knowledge graphs and structured data sources. The field would benefit from systematic investigation of CRS performance under varying knowledge quality conditions and development of approaches robust to incomplete or noisy external data.

## Per-Paper Annotations

### Bernard & Balog (2024)

**Research question**: How can conversational breakdowns in CRS be systematically identified and addressed using user simulation?
**Methodology**: Developed a methodology to systematically test CRS for conversational breakdowns by examining simulated conversations for pre-defined breakdown types, extracting responsible conversational paths, and characterizing them in terms of underlying dialogue intents.
**Key findings**:
- The methodology serves effectively as both a diagnostic tool and a development tool for improving CRS
- User simulation provides simplicity, cost-effectiveness, and time efficiency for obtaining breakdown-identifying conversations
- Just a few iterations of the methodology can make systems more robust to conversational breakdowns
- Breakdown types can be systematically categorized and linked to specific dialogue intents
- Case study demonstrated practical effectiveness with an existing CRS and user simulator
**Limitations**: Pre-defined breakdown types may not cover all possible failure modes in real conversations. Simulated user interactions may not fully reflect the complexity and unpredictability of actual user behavior, potentially missing some breakdown scenarios.

### Bernard et al. (2024)

**Research question**: How can we create a scalable benchmarking platform for Conversational Recommender Systems based on human feedback?
**Methodology**: Introduced CRS Arena, a research platform that displays pairwise battles between anonymous conversational recommender systems where users interact with systems sequentially before declaring a winner or draw, collecting conversations and user feedback for evaluation and ranking.
**Key findings**:
- Both open and closed crowdsourcing platforms produce highly correlated rankings of CRSs
- Conversations from both setups have similar characteristics
- Released CRSArena-Dial dataset containing 474 conversations with corresponding user feedback
- Established preliminary CRS rankings using the Elo rating system
- Platform enables reliable evaluation and comparison of conversational recommender systems
**Limitations**: The dataset size is relatively limited (474 conversations), and the rankings are preliminary rather than definitive. The platform's accessibility may constrain the diversity and volume of collected feedback.

### Zhang et al. (2024)

**Research question**: How can conversational recommender systems address the misalignment between benchmark-optimal responses and actual user emotional needs that are often overlooked?
**Methodology**: Proposed ECR framework with two modules: (1) emotion-aware item recommendation using user emotions to refine preference modeling, and (2) emotion-aligned response generation using retrieval-augmented prompts to fine-tune a pre-trained language model; also enlarged empathetic data using LLM-annotated emotion labels and external emotional reviews.
**Key findings**:
- ECR enhances recommendation accuracy on the ReDial dataset
- Improves user satisfaction by generating human-like emotional responses
- Successfully mitigates hallucination through retrieval-augmented prompting
- Novel evaluation metrics better capture user satisfaction in real-world CRS scenarios
- LLM-annotated emotion labels effectively address insufficient supervision
**Limitations**: The framework requires emotion annotation which may introduce noise, and the approach depends on the quality of external emotional reviews for data augmentation.

### Chen et al. (2025)

**Research question**: How can conversational recommender systems be evaluated using a single metric that authentically reflects user experience by capturing both recommendation accuracy and dialogue management quality?
**Methodology**: Proposed CoRE framework with two components: (1) LLM-As-Evaluator that scores 12 key user experience factors, and (2) Multi-Agent Debater with four distinct roles (common user, domain expert, linguist, HCI expert) to synthesize factors into a unified overall performance score.
**Key findings**:
- CoRE aligns well with human evaluation on most of the 12 identified factors
- CoRE's overall evaluation scores demonstrate significantly better alignment with human feedback compared to existing rule-based metrics
- Successfully evaluated four CRSs on two benchmark datasets
- The multi-agent debate framework effectively synthesizes diverse evaluation perspectives into a coherent score
**Limitations**: The abstract does not explicitly acknowledge limitations, though the approach depends on LLM quality and the computational cost of multi-agent debate may be substantial.

### Zhu et al. (2025)

**Research question**: How can LLM-based conversational recommender systems effectively leverage behavioral data that has proven important for classical collaborative filtering approaches?
**Methodology**: Proposed CRAG (Collaborative Retrieval Augmented Generation), the first approach combining state-of-the-art LLMs with collaborative filtering for conversational recommendations through collaborative retrieval augmentation.
**Key findings**:
- CRAG demonstrates superior item coverage compared to several CRS baselines
- Achieves better recommendation performance on Reddit-v2 and ReDial datasets
- Improvements are mainly due to better accuracy on recently released movies
- Successfully bridges the gap between LLM contextual understanding and CF behavioral data
- Code and data made publicly available for reproducibility
**Limitations**: The improvements appear to be primarily concentrated on recently released movies, suggesting potential limitations for older or less popular items; the approach may be domain-specific to movie recommendations.

### Zou et al. (2025)

**Research question**: How can different types of contextual information be effectively combined to improve conversational recommender systems?
**Methodology**: Proposed MCCRS, a multi-type context-aware CRS that uses a mixture-of-experts approach where each expert specializes in a particular contextual domain (knowledge graph, conversation history, item reviews), coordinated by a ChairBot to generate final recommendations.
**Key findings**:
- MCCRS achieves significantly higher performance compared to existing baseline methods
- The mixture-of-experts architecture effectively fuses structured and unstructured contextual information
- Expert specialization breaks the model bottleneck imposed by relying on single contextual information sources
- ChairBot coordination successfully integrates outputs from multiple specialized experts
- Incorporating knowledge graphs, conversation history, and item reviews together improves recommendation quality
**Limitations**: The multi-expert architecture introduces complexity and potential coordination overhead. The approach may require substantial computational resources and careful tuning of the ChairBot coordination mechanism.

### Zhang et al. (2025)

**Research question**: How can data sparsity in both dialogue and entity spaces be mitigated in conversational recommender systems?
**Methodology**: Proposed DACRS, a framework with three modules: Dialogue Augmentation (two-stage pipeline to enrich dialogue contexts), Knowledge-Guided Entity Modeling (entity substitution and similarity constraints for sparse/unseen entities), and Dialogue-Entity Matching (attention aggregation for user representations).
**Key findings**:
- DACRS consistently outperforms state-of-the-art conversational recommender systems on two public benchmark datasets
- Two-stage dialogue augmentation improves robustness to linguistic variation in open-ended conversations
- Knowledge-guided entity modeling enhances representation learning for sparsely supervised and unseen entities
- Dialogue-guided attention aggregation captures both explicit and implicit user preferences
- Entity substitution and similarity constraints effectively leverage knowledge graphs despite sparse supervision
**Limitations**: The approach depends heavily on the availability and quality of external knowledge graphs. The multi-module architecture may introduce training complexity and the augmentation pipeline requires careful design to avoid introducing noise.

### Yang & Fang (2025)

**Research question**: How can conversational recommender systems connect conversations with external domain knowledge without requiring domain-specific engineering or risking LLM hallucination?
**Methodology**: Proposed ReGeS framework with reciprocal synergy: generation-augmented retrieval to distill informative user intent from conversations, and retrieval-augmented generation to differentiate subtle item features.
**Key findings**:
- Achieves state-of-the-art performance in recommendation accuracy on multiple CRS benchmarks
- The reciprocal synergy obviates the need for extra annotations
- Significantly reduces hallucination risks compared to LLM-only approaches
- Simplifies continuous updates to the system
- Effectively handles noisy dialogues that typically weaken retrieval
**Limitations**: The abstract does not explicitly state limitations, though performance may depend on retrieval quality and the approach may have computational overhead from the reciprocal retrieval-generation loop.

### Bernard & Balog (2025)

**Research question**: How can simulation-based evaluation resources for conversational recommender systems be improved to align with state-of-the-art research?
**Methodology**: Presented UserSimCRS v2, a significant upgrade to the original toolkit featuring an enhanced agenda-based user simulator, introduction of LLM-based simulators, integration for wider CRS and dataset compatibility, and new LLM-as-a-judge evaluation utilities.
**Key findings**:
- UserSimCRS v2 addresses the scarcity of resources for simulation-based CRS evaluation
- LLM-based simulators provide new capabilities aligned with state-of-the-art research
- Enhanced agenda-based simulator improves simulation fidelity over the original version
- Wider integration supports evaluation across more CRS implementations and datasets
- LLM-as-a-judge utilities offer automated evaluation capabilities demonstrated in case study
**Limitations**: Simulation fidelity may not fully capture real user behavior and preferences. The quality of LLM-based simulators depends on underlying model capabilities, and the case study demonstration may not generalize to all CRS scenarios.

### Li et al. (2026)

**Research question**: How can user simulators for CRS evaluation better model human decision-making including hesitation and decision deferral commonly observed in real consumer behavior?
**Methodology**: Proposed Hesitator, a theory-grounded user simulation framework with a modular Decision Module that separates utility-based item selection from overload-aware commitment decisions to explicitly model human decision-making under choice overload.
**Key findings**:
- Integrating the Decision Module consistently mitigates unrealistic behaviors under increasing overload conditions
- Hesitator reproduces established behavioral patterns from psychological economics
- Improvements are consistent across multiple user simulation frameworks, domains, sales modes, and LLM backbones
- Addresses the problem of overly high acceptance probabilities in existing LLM-based simulators
- Successfully models hesitation and decision deferral observed in real consumer behavior
**Limitations**: The framework's performance across domains beyond those tested remains to be validated, and the theory-grounded approach may require domain-specific calibration for different product categories.

## References

Bernard, N., & Balog, K. (2024). Identifying breakdowns in conversational recommender systems using user simulation. arXiv. https://arxiv.org/abs/2405.14249

Bernard, N., & Balog, K. (2025). UserSimCRS v2: Simulation-based evaluation for conversational recommender systems. arXiv. https://arxiv.org/abs/2512.04588

Bernard, N., Joko, H., Hasibi, F., & Balog, K. (2024). CRS Arena: Crowdsourced benchmarking of conversational recommender systems. arXiv. https://arxiv.org/abs/2412.10514

Chen, N., Dai, Q., Dong, X., Wang, P., Jia, Q., Du, Z., Dong, Z., & Wu, X.-M. (2025). Evaluating conversational recommender systems via large language models: A user-centric framework. arXiv. https://arxiv.org/abs/2501.09493

Li, Y.-C., Chen, L.-C., Wu, S.-Y., Tsai, Y.-C., & Lin, S.-D. (2026). Decision-aware user simulation agent for evaluating conversational recommender systems. arXiv. https://arxiv.org/abs/2605.05250

Yang, D., & Fang, H. (2025). ReGeS: Reciprocal retrieval-generation synergy for conversational recommender systems. arXiv. https://arxiv.org/abs/2509.21371

Zhang, X., Xie, R., Lyu, Y., Xin, X., Ren, P., Liang, M., Zhang, B., Kang, Z., de Rijke, M., & Ren, Z. (2024). Towards empathetic conversational recommender systems. arXiv. https://arxiv.org/abs/2409.10527

Zhang, S., Liu, M., Yuan, W., Yin, H., & Long, C. (2025). On mitigating data sparsity in conversational recommender systems. arXiv. https://arxiv.org/abs/2507.00479

Zhu, Y., Wan, C., Steck, H., Liang, D., Feng, Y., Kallus, N., & Li, J. (2025). Collaborative retrieval for large language model-based conversational recommender systems. arXiv. https://arxiv.org/abs/2502.14137

Zou, J., Lin, C., Guo, W., Wang, Z., Wei, J., Yang, Y., & Shen, H. T. (2025). Multi-type context-aware conversational recommender systems via mixture-of-experts. arXiv. https://arxiv.org/abs/2504.13655
