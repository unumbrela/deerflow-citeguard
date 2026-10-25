# Systematic Literature Review: Multilingual Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "multilingual large language models", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on multilingual large language models (MLLMs) from the past two years reveals a field maturing from capability demonstrations toward deeper scientific understanding and targeted improvements. Research has shifted from asking "can MLLMs work across languages?" to investigating how multilingual capabilities are internally organized, why performance gaps persist across languages, and how to systematically improve cross-lingual consistency and fairness. A dominant theme is interpretability at the neuron level, with multiple studies isolating language-specific and culture-specific neurons through causal interventions. Another major thread addresses evaluation gaps, demonstrating that standard metrics overestimate cross-lingual consistency and that MLLMs struggle with fundamental challenges like word sense disambiguation. Methodological advances focus on representation alignment and in-context learning optimization rather than brute-force scaling of multilingual corpora.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "multilingual large language models", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The time window captures recent work but may miss influential older papers that continue to shape the field.

## Themes

### Theme 1: Neuron-Level Interpretability and Causal Analysis

A significant cluster of research investigates how multilingual capabilities are organized at the neuron level within transformer architectures. Rather than treating MLLMs as black boxes, these studies employ causal intervention methodologies to identify which neurons are functionally necessary for specific languages or cultural knowledge. Namazifard and Poech (2025) localized culture-specific neurons in upper layers, demonstrating they can be modulated independently from language-specific neurons. Kim et al. (2026) improved upon entropy-based language neuron identification by proposing distribution-aware selection that considers pairwise activation overlaps, achieving 4.9× higher on-target damage while preserving off-target performance. Le and Li (2026) introduced CRANE, which redefines language specificity through functional necessity rather than activation magnitude, revealing asymmetric patterns where masking language-relevant neurons selectively degrades that language while preserving others. Collectively, these studies suggest that multilingual knowledge is not uniformly distributed but rather encoded in partially separable neuron populations that can be selectively targeted for editing or debugging.

### Theme 2: Cross-Lingual Representation Alignment

Multiple papers address the persistent performance gap between dominant and non-dominant languages in MLLMs through representation-level interventions. Bu et al. (2025) proposed AlignX, a two-stage framework that first aligns multilingual representations through semantic alignment and feature integration, then stimulates multilingual capabilities via instruction fine-tuning, demonstrating improvements over brute-force corpus scaling. This approach reflects a broader shift from data-centric solutions (collect more multilingual data) to architecture- and representation-centric solutions (align existing representations more precisely). The underlying hypothesis is that imprecise alignment, not lack of data, limits cross-lingual transfer, and that bringing multilingual representations closer in latent space improves generalization without requiring massive retraining.

### Theme 3: Evaluation Gaps and Hidden Inconsistencies

A critical thread in recent literature exposes fundamental limitations in how MLLL capabilities are evaluated across languages. Sun et al. (2026) demonstrated that standard embedding-based similarity metrics systematically overstate cross-lingual consistency in reasoning traces, with 52.1%–67.3% of examples rated as highly similar holistically failing to show structural similarity. Their bilingual annotation studies revealed that human judgments align with structural similarity rather than holistic embeddings, suggesting that answer-level evaluations mask substantial divergence in supporting evidence across languages. Cahyawijaya et al. (2024) introduced StingrayBench, showing that MLLMs fail to disambiguate false friends across languages and exhibit bias toward higher-resource languages. Valentini et al. (2026) found that MLLM-generated text exhibits translationese characteristics distinguishable from non-translated baselines, raising questions about whether MLLMs are genuinely generating in target languages or performing implicit translation. These studies collectively argue for more granular, trace-level evaluation methodologies that capture not just what answers MLLMs produce, but how they arrive at them.

### Theme 4: In-Context Learning and Example Selection

Research on improving MLLM performance without parameter updates has focused on optimizing in-context learning through better example selection. Kaneko et al. (2025) proposed BMF-ICL, which balances three factors—semantic similarity, linguistic alignment, and language-specific performance—demonstrating that existing approaches treating these factors independently leave performance gains unrealized. Their findings highlight the importance of selecting examples from multiple languages rather than monolingual contexts, suggesting that cross-lingual knowledge transfer in ICL is sensitive to how examples are curated. This line of work is particularly relevant for low-resource settings where fine-tuning is impractical and practitioners must rely on prompting strategies.

### Theme 5: Annotation Bias and Cultural Fairness

As MLLMs are deployed in culturally diverse settings, attention has turned to biases introduced during dataset annotation. Cui et al. (2025) proposed a comprehensive framework distinguishing instruction bias, annotator bias, and contextual/cultural bias, synthesizing detection methods and outlining mitigation strategies including diverse annotator recruitment and iterative guideline refinement. Their work emphasizes that annotation pipelines themselves can perpetuate cultural mismatches that distort model outputs, particularly in multilingual contexts where annotator subjectivity interacts with cultural differences. This theme intersects with neuron-level interpretability: if cultural knowledge is encoded in identifiable neurons (Namazifard & Poech, 2025), then annotation biases may become entrenched in specific model components that are difficult to correct post-hoc.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that multilingual capabilities in LLMs are not uniformly distributed but rather organized in partially separable components—whether neurons (Namazifard & Poech, 2025; Kim et al., 2026; Le & Li, 2026) or representations (Bu et al., 2025). There is broad agreement that standard evaluation methodologies overestimate cross-lingual consistency (Sun et al., 2026; Cahyawijaya et al., 2024). All intervention studies acknowledge that current approaches are limited to specific languages or language families, with generalizability to low-resource or typologically distant languages remaining unproven.

**Disagreements**: While neuron-level studies agree on the existence of language-specific components, they differ on identification methodology: activation-based approaches (implicitly critiqued by Kim et al., 2026 and Le & Li, 2026) versus distribution-aware or relevance-based frameworks. The field has not resolved whether representation alignment (Bu et al., 2025) or in-context learning optimization (Kaneko et al., 2025) offers better returns for improving low-resource language performance, as no direct comparisons exist. On translationese, Valentini et al. (2026) establish its presence but do not explain mechanisms, leaving open whether it stems from training data composition or architectural biases.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. First, language coverage remains narrow: most studies focus on high-resource languages (English, Chinese, German, Spanish), with only a few including Vietnamese, Indonesian, or Tagalog, and almost none addressing African or Indigenous languages. Second, while neuron-level interventions demonstrate causal effects, no study has shown that editing identified neurons improves real-world performance on downstream tasks without degrading other capabilities. Third, the relationship between annotation bias (Cui et al., 2025) and model-internal representations (culture neurons, language neurons) remains unexplored—does biased annotation create biased neurons, or do pre-existing model biases interact with annotation processes? Fourth, trace-level divergence (Sun et al., 2026) raises safety concerns: if users in different languages receive different reasoning for the same answer, auditing and verification become language-dependent, yet no mitigation strategies are proposed. Finally, the systematic survey by Zhu et al. (2024) documents applications across domains, but none of the intervention studies validate their methods on domain-specific tasks, leaving open whether laboratory findings generalize to production settings.

## Per-Paper Annotations

### Bu et al. (2025)

**Research question**: How can the multilingual performance gap in pre-trained LLMs be bridged through representation-level alignment rather than large-scale multilingual corpus fine-tuning?

**Methodology**: AlignX employs a two-stage representation-level framework: first aligning multilingual representations through semantic alignment and language feature integration, then stimulating multilingual capability via multilingual instruction fine-tuning.

**Key findings**:
- AlignX enhances multilingual general and cross-lingual generation capabilities across several pre-trained LLMs
- The approach brings multilingual representations closer together
- Cross-lingual alignment is improved compared to fine-tuning on large-scale multilingual corpora alone
- Two-stage representation alignment is more effective than imprecise alignment from corpus fine-tuning

**Limitations**: The approach requires a two-stage training process, and its effectiveness on extremely low-resource languages or languages with very different typological features from dominant languages is not thoroughly examined.

### Cahyawijaya et al. (2024)

**Research question**: Can multilingual LLMs reliably disambiguate cross-lingual word senses, particularly for false friends (words orthographically similar but with different meanings across languages)?

**Methodology**: The authors introduce StingrayBench, a novel benchmark for cross-lingual sense disambiguation using false friends across four language pairs (Indonesian-Malay, Indonesian-Tagalog, Chinese-Japanese, English-German), and propose new metrics for quantifying cross-lingual sense bias and comprehension.

**Key findings**:
- Multilingual LLMs struggle with cross-lingual word sense disambiguation, particularly when confronted with false friends
- Models exhibit bias toward higher-resource languages when processing cross-lingual semantic tasks
- False friends serve as an effective approach to pinpoint limitations in cross-lingual sense disambiguation capabilities
- New metrics are proposed for quantifying cross-lingual sense bias and comprehension based on the StingrayBench benchmark
- The work highlights the need for more diverse and inclusive language modeling to promote fairer access for the wider multilingual community

**Limitations**: The study is limited to four language pairs which may not capture the full diversity of cross-lingual challenges; the focus on false friends, while effective, may not represent all types of cross-lingual semantic ambiguity.

### Cui et al. (2025)

**Research question**: What types of annotation bias exist in multilingual LLM datasets and how can they be detected and mitigated in culturally diverse settings?

**Methodology**: The authors propose a comprehensive framework for understanding annotation bias by distinguishing among instruction bias, annotator bias, and contextual/cultural bias, then review detection methods and outline proactive and reactive mitigation strategies.

**Key findings**:
- Annotation bias in NLP datasets remains a major challenge for multilingual LLMs, particularly in culturally diverse settings where bias from task framing, annotator subjectivity, and cultural mismatches can distort model outputs
- Three distinct types of annotation bias are identified: instruction bias, annotator bias, and contextual/cultural bias
- Detection methods include inter-annotator agreement, model disagreement, metadata analysis, multilingual model divergence, and cultural inference
- Mitigation strategies span diverse annotator recruitment, iterative guideline refinement, and post-hoc model adjustments
- An ensemble-based bias mitigation approach adapted for multilingual settings is proposed alongside ethical analysis of annotation processes

**Limitations**: This appears to be a framework and synthesis paper rather than empirical validation; the abstract does not report experimental results or quantify the effectiveness of proposed mitigation strategies.

### Kaneko et al. (2025)

**Research question**: How can example selection in multilingual in-context learning be optimized by balancing semantic similarity, linguistic alignment, and language-specific performance factors?

**Methodology**: The authors propose BMF-ICL, a method that quantifies and optimally balances three key factors (semantic similarity, linguistic alignment, and language-specific performance) for improved example selection, evaluated on mCSQA and TYDI benchmarks across four MLLMs.

**Key findings**:
- BMF-ICL outperforms existing methods on mCSQA and TYDI benchmarks across four MLLMs
- All three factors (semantic, linguistic, and language-specific performance) are important for optimal example selection
- Selecting examples from multiple languages improves performance
- Existing approaches that address factors independently leave optimal example selection underexplored

**Limitations**: The evaluation is limited to four MLLMs and two benchmarks (mCSQA and TYDI), and the approach's effectiveness on other tasks or low-resource languages remains to be validated.

### Kim et al. (2026)

**Research question**: Can language specificity in multilingual LLMs be better captured by leveraging pairwise relationships between per-language activation distributions rather than entropy-based measures?

**Methodology**: The authors propose Distribution-aware Language Neuron (DLN) selection, which quantifies language specificity by clustering languages using pairwise overlap coefficients between per-language activation distributions over the full activation range, including negative values.

**Key findings**:
- DLN more effectively isolates language-specific causal effects compared to entropy-based approaches
- The method yields up to 4.9× higher on-target language damage per neuron
- Off-target language performance is preserved while improving isolation
- Distributional relationships between languages provide richer information than entropy measures alone

**Limitations**: The evaluation is conducted on only two mLLMs and two held-out corpora, limiting claims about generalizability across diverse model architectures and language families.

### Le and Li (2026)

**Research question**: How are language capabilities organized at the neuron level in multilingual LLMs, and can language-specific neurons be identified through functional necessity rather than activation patterns?

**Methodology**: The authors propose CRANE, a relevance-based analysis framework that identifies language-specific neurons through targeted neuron-level interventions, characterizing neuron specialization by their contribution to language-conditioned predictions rather than activation magnitude.

**Key findings**:
- Masking neurons relevant to a target language selectively degrades performance on that language while substantially preserving performance on other languages
- Language-specific neurons exhibit language-selective but non-exclusive specializations, revealing an asymmetric pattern
- CRANE isolates language-specific components more precisely than activation-based methods that conflate language preference with functional importance
- Experiments conducted on English, Chinese, and Vietnamese across multiple benchmarks validate the approach
- A dedicated relevance-based metric and base-to-chat model transfer analysis support the framework's effectiveness

**Limitations**: The implementation is noted as "will be made publicly available" suggesting it was not yet released; the study is limited to three languages (English, Chinese, Vietnamese) which may not generalize to all language families.

### Namazifard and Poech (2025)

**Research question**: How and where do multilingual large language models encode culture, and can culture-specific neurons be isolated independently from language-specific neurons?

**Methodology**: The authors build on established methodology for identifying language-specific neurons to localize culture-specific neurons, introducing MUREL, a curated dataset of 85.2 million tokens spanning six cultures, and conducting localization and intervention experiments to disentangle culture from language neurons.

**Key findings**:
- LLMs encode different cultures in distinct neuron populations, predominantly in upper layers
- Culture neurons can be modulated largely independently of language-specific neurons
- Culture neurons can be edited independently from those specific to other cultures
- Cultural knowledge and propensities in multilingual language models can be selectively isolated

**Limitations**: The study is limited to six cultures in the MUREL dataset, and the methodology's generalizability to other cultures or model architectures beyond those tested remains unexplored.

### Sun et al. (2026)

**Research question**: Do multilingual LLMs provide comparable reasoning traces across languages, or do standard evaluations overestimate consistency by only measuring final-answer agreement?

**Methodology**: The authors introduce a trace-level divergence framework that compares visible reasoning traces as structured sequences, decomposing agreement into structural similarity, order consistency, and holistic similarity with pair-specific calibration, evaluated across three reasoning benchmarks, seven languages, and six frontier LLMs.

**Key findings**:
- Standard embedding-based similarity systematically overstates agreement between multilingual reasoning traces
- 52.1%–67.3% of examples in the top quartile of holistic similarity are not in the top quartile of structural similarity, revealing substantial dissociation
- Human judgments from blind bilingual annotation studies align with structural similarity rather than the holistic baseline
- Divergence is language-specific: English traces for paraphrases of the same question agree more closely than English traces with counterparts in other languages
- Answer-level and holistic evaluations can substantially overestimate the consistency of multilingual explanatory artifacts, motivating trace-level evaluation for reliable multilingual deployment

**Limitations**: The study covers seven languages but may not generalize to all languages, particularly low-resource ones; the focus on reasoning benchmarks may not capture divergence patterns in other task types such as creative or conversational contexts.

### Valentini et al. (2026)

**Research question**: Does text generated by multilingual large language models resemble translationese, and how does MLLM-produced translationese differ from translationese produced through direct human or machine translation?

**Methodology**: The authors leverage established indicators of translated text to evaluate MLLM-generated text in five languages, using high-accuracy classification models, variance analyses on linguistic features, and human annotations (for German and Spanish) to compare against non-translated and human-written baselines.

**Key findings**:
- MLLM generations do exhibit translationese characteristics distinguishable from non-translated text
- MLLM-produced translationese differs in key linguistic features from direct translation-produced translationese
- High-accuracy classification models can detect translationese patterns in MLLM outputs
- Human annotations confirm the presence of translation-related interference in MLLM generations

**Limitations**: Human annotations were collected for only two languages (German and Spanish), limiting cross-linguistic generalization, and the study does not fully explain the mechanisms causing MLLMs to produce translationese.

### Zhu et al. (2024)

**Research question**: What is the current state of research on multilingual LLMs including their architectures, training methodologies, evaluation benchmarks, interpretability, and real-world applications?

**Methodology**: This is a comprehensive survey paper that systematically reviews and synthesizes existing research on MLLMs, covering architecture and pre-training objectives, multilingual dataset construction, evaluation benchmarks and methodologies, interpretability analysis, and applications across diverse domains.

**Key findings**:
- MLLMs represent an important advancement in AI capable of understanding and generating language across linguistic boundaries
- A detailed taxonomy and roadmap is provided for evaluating MLLMs across cross-lingual knowledge, reasoning, alignment with human values, safety, interpretability, and specialized applications
- The survey extensively discusses multilingual evaluation benchmarks and datasets, including the use of LLMs themselves as multilingual evaluators
- Interpretability of multilingual capabilities, cross-lingual transfer, and language bias within MLLMs are addressed to enhance models from black to white boxes
- Real-world applications are reviewed across biology, medicine, computer science, mathematics, and law, showcasing innovation while highlighting challenges and opportunities in diverse language communities

**Limitations**: As a survey paper, it synthesizes existing work rather than presenting new empirical findings; the companion GitHub repository may not capture all recent developments given the rapid pace of MLLM research.

## References

Bu, M., Zhang, S., He, Z., Wu, H., & Feng, Y. (2025). AlignX: Advancing multilingual large language models with multilingual representation alignment. arXiv. https://arxiv.org/abs/2509.24338

Cahyawijaya, S., Zhang, R., Lovenia, H., Cruz, J. C. B., Gilbert, E., Nomoto, H., & Aji, A. F. (2024). Thank you, Stingray: Multilingual large language models can not (yet) disambiguate cross-lingual word sense. arXiv. https://arxiv.org/abs/2410.21573

Cui, X., Huang, Z., & Adel, N. (2025). Bias in, bias out: Annotation bias in multilingual large language models. arXiv. https://arxiv.org/abs/2511.14662

Kaneko, M., Aji, A. F., & Baldwin, T. (2025). Balanced multi-factor in-context learning for multilingual large language models. arXiv. https://arxiv.org/abs/2502.11495

Kim, M., Won, I., Yuk, J., Kim, D., Kim, J., & Lim, K. T. (2026). Distribution-aware language neuron identification in multilingual large language models. arXiv. https://arxiv.org/abs/2609.10993

Le, Y., & Li, Y. (2026). CRANE: Causal relevance analysis of language-specific neurons in multilingual large language models. arXiv. https://arxiv.org/abs/2601.04664

Namazifard, D., & Poech, L. G. (2025). Isolating culture neurons in multilingual large language models. arXiv. https://arxiv.org/abs/2508.02241

Sun, R., Mei, P., Cheng, X., Chen, K., Li, T., Yu, Z., & Chandrasekaran, V. (2026). Same answer, different reasons: Trace-level divergence in multilingual large language models. arXiv. https://arxiv.org/abs/2610.29092

Valentini, M., Wright, T., Granados, J., Colunga, E., & von der Wense, K. (2026). An investigation of translationese in the generations of multilingual large language models. arXiv. https://arxiv.org/abs/2608.17399

Zhu, S., Supryadi, Xu, S., Sun, H., Pan, L., Cui, M., Du, J., Jin, R., Branco, A., & Xiong, D. (2024). Multilingual large language models: A systematic survey. arXiv. https://arxiv.org/abs/2411.11072
