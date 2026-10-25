# Systematic Literature Review: Multilingual Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "multilingual large language models", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on multilingual large language models (MLLMs) reveals a field rapidly maturing from basic capability demonstration to nuanced investigation of cultural representation, bias, and equitable design. Recent work has shifted focus toward understanding how MLLMs encode and process multilingual information at the neuron level, with multiple studies identifying language-specific and culture-specific neural populations that can be selectively isolated and manipulated. Concurrently, researchers are addressing critical challenges including annotation bias, translationese artifacts, tokenization inequities, and cross-lingual disambiguation failures. The collective findings suggest that while MLLMs have achieved impressive multilingual capabilities, significant gaps remain in achieving truly equitable and culturally grounded language understanding across diverse linguistic communities.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "multilingual large language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Neural Localization of Language and Culture

A prominent research direction involves identifying and isolating specific neuron populations responsible for language-specific and culture-specific processing in MLLMs. Namazifard and Poech (2025) demonstrated that culture is encoded in distinct neuron populations, predominantly in upper layers, and can be modulated independently from language-specific neurons. Building on this line of inquiry, Kim et al. (2026) introduced a distribution-aware approach to language neuron identification that leverages pairwise relationships between per-language activation distributions, achieving up to 4.9× higher on-target language damage per neuron compared to entropy-based methods. Similarly, Le and Li (2026) proposed CRANE, a causal relevance analysis framework that identifies language-specific neurons through functional necessity rather than activation-based heuristics, enabling more precise isolation of language-selective components. This convergence suggests that interpretability at the neuron level is crucial for understanding and improving MLLM multilingual capabilities.

### Theme 2: Bias Detection and Mitigation in Multilingual Systems

Multiple papers address various forms of bias affecting MLLM performance and fairness. Cui et al. (2025) provided a comprehensive framework for understanding annotation bias, proposing a typology distinguishing instruction bias, annotator bias, and contextual/cultural bias, with detection methods including inter-annotator agreement, model disagreement, and multilingual model divergence. Valentini et al. (2026) investigated translationese in MLLM generations across five languages, revealing that MLLM-produced text exhibits characteristics of translated content that differ from direct human translation. Cahyawijaya et al. (2024) exposed cross-lingual word sense disambiguation failures, showing that MLLMs tend to bias toward higher-resource languages when processing false friends across language pairs. These studies collectively highlight the need for systematic bias detection and mitigation strategies throughout the MLLM development pipeline.

### Theme 3: Equitable Tokenization and Representation

The tension between efficiency and equity in tokenization design has emerged as a critical research area. Lee et al. (2026) conducted a systematic comparison of equitable tokenizers across 11 Southeast Asian languages, finding that parity-aware BPE achieves strong compression parity at competitive cost, while morphology-driven byte encoding delivers superior semantic reasoning at higher computational expense. Their work demonstrates that cross-lingual fairness and tokenization efficiency are not fundamentally at odds. Complementing this work, Bu et al. (2025) proposed AlignX, a two-stage representation-level framework that aligns multilingual representations through semantic alignment and language feature integration, bringing multilingual representations closer together and improving cross-lingual alignment compared to existing fine-tuning approaches.

### Theme 4: Optimized In-Context Learning for Multilingual Tasks

Research on in-context learning has evolved to explicitly balance multiple factors for improved multilingual performance. Kaneko et al. (2025) introduced balanced multi-factor in-context learning (BMF-ICL), which quantifies and optimally balances semantic similarity, linguistic alignment, and language-specific performance for example selection. Their method outperformed existing methods on mCSQA and TYDI datasets across four MLLMs, demonstrating that incorporating all three factors and selecting examples from multiple languages improves results. This work represents a shift from single-factor optimization to holistic, multi-factor approaches in multilingual in-context learning.

### Theme 5: Comprehensive Survey and Taxonomy Development

The field has seen efforts to synthesize and systematize knowledge about MLLMs. Zhu et al. (2024) provided a comprehensive survey covering MLLM architecture, pre-training objectives, multilingual dataset construction, evaluation benchmarks, and applications across diverse domains including biology, medicine, computer science, mathematics, and law. Their taxonomy addresses cross-lingual knowledge, reasoning, alignment, safety, interpretability, and specialized applications, providing a roadmap for assessing MLLM capabilities and identifying areas for future research.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, multiple studies converge on the finding that MLLMs encode language-specific and culture-specific information in separable neural populations that can be selectively manipulated (Namazifard & Poech, 2025; Kim et al., 2026; Le & Li, 2026). Second, there is consensus that current MLLMs exhibit systematic biases toward high-resource languages and Latin scripts, particularly in tokenization and cross-lingual disambiguation (Cahyawijaya et al., 2024; Lee et al., 2026; Cui et al., 2025). Third, the literature agrees that data quality and diversity in multilingual pre-training and alignment datasets are crucial for enhancing MLLM performance (Zhu et al., 2024; Bu et al., 2025).

**Disagreements**: While the surveyed papers do not show fundamental disagreements, they differ in their approaches to addressing multilingual challenges. For instance, Kim et al. (2026) advocate for distribution-aware neuron identification based on activation distributions, while Le and Li (2026) argue for causal relevance analysis based on functional necessity—though both approaches aim to improve upon entropy-based methods. Additionally, there is tension between efficiency-focused approaches like parity-aware BPE (Lee et al., 2026) and performance-focused approaches like morphology-driven encoding, reflecting ongoing debate about optimal trade-offs in multilingual system design.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly stated limitations in their abstracts, suggesting either that limitations are addressed in full text or that this aspect remains underdeveloped in the field. Second, while multiple papers identify bias and inequity issues, few provide comprehensive, deployable mitigation strategies that have been validated in production systems. Third, the focus on neuron-level interpretability, while promising, has not yet been connected to practical interventions for end users or application developers. Fourth, there is limited investigation of low-resource languages beyond Southeast Asian languages, leaving gaps in understanding MLLM behavior across the full spectrum of global linguistic diversity. Finally, the temporal concentration of papers (2024-2026) suggests this is an emerging field where longitudinal studies of MLLM evolution and improvement over time are still needed.

## Per-Paper Annotations

### Bu et al. (2025)

**Research question**: How can the multilingual performance gap in pre-trained LLMs be bridged, particularly for non-dominant languages that lag in performance and cross-lingual alignment?
**Methodology**: The authors propose AlignX, a two-stage representation-level framework: (1) aligning multilingual representations with multilingual semantic alignment and language feature integration, and (2) stimulating multilingual capability via multilingual instruction fine-tuning. Experiments were conducted on several pre-trained LLMs.
**Key findings**:
- AlignX enhances LLMs' multilingual general and cross-lingual generation capability
- The approach brings multilingual representations closer together
- AlignX improves cross-lingual alignment compared to existing fine-tuning approaches
**Limitations**: not stated in abstract

### Cahyawijaya et al. (2024)

**Research question**: Can multilingual LLMs reliably disambiguate cross-lingual word sense, particularly for false friends across different language pairs?
**Methodology**: The study introduces StingrayBench, a novel benchmark for cross-lingual sense disambiguation using false friends (orthographically similar words with different meanings) across four language pairs: Indonesian-Malay, Indonesian-Tagalog, Chinese-Japanese, and English-German.
**Key findings**:
- Multilingual LLMs tend to be biased toward higher-resource languages when disambiguating false friends
- The study collects false friends in four language pairs to challenge LLMs' cross-lingual sense disambiguation capabilities
- New metrics are proposed for quantifying cross-lingual sense bias and comprehension
- Current multilingual LLMs show limitations in distinguishing orthographically similar words with different meanings across languages
- The work contributes to developing more diverse and inclusive language modeling for fairer multilingual community access
**Limitations**: not stated in abstract

### Cui et al. (2025)

**Research question**: How can annotation bias in NLP datasets be understood, detected, and mitigated in multilingual LLM development?
**Methodology**: The paper proposes a comprehensive framework for understanding annotation bias and reviews detection methods including inter-annotator agreement, model disagreement, and metadata analysis, while highlighting emerging techniques such as multilingual model divergence and cultural inference.
**Key findings**:
- Annotation bias stems from task framing, annotator subjectivity, and cultural mismatches, which can distort model outputs and exacerbate social harms
- The authors propose a typology distinguishing instruction bias, annotator bias, and contextual and cultural bias
- Detection methods include inter-annotator agreement, model disagreement, metadata analysis, multilingual model divergence, and cultural inference
- Mitigation strategies include diverse annotator recruitment, iterative guideline refinement, and post-hoc model adjustments
- The work provides an ethical analysis of annotation processes for more equitable and culturally grounded LLM pipelines
**Limitations**: not stated in abstract

### Kaneko et al. (2025)

**Research question**: How can example selection in multilingual in-context learning be optimized by explicitly disentangling and balancing the combined impact of semantic similarity, linguistic alignment, and language-specific performance?
**Methodology**: The authors propose balanced multi-factor ICL (BMF-ICL), a method that quantifies and optimally balances three key factors (semantic similarity, linguistic alignment, and language-specific performance) for improved example selection. Experiments were conducted on mCSQA and TYDI datasets across four MLLMs.
**Key findings**:
- BMF-ICL outperforms existing methods on mCSQA and TYDI across four MLLMs
- Incorporating all three factors (semantic similarity, linguistic alignment, language-specific performance) is important for optimal performance
- Selecting examples from multiple languages improves results
**Limitations**: not stated in abstract

### Kim et al. (2026)

**Research question**: Can language-specific neuron identification in multilingual LLMs be improved by leveraging pairwise relationships between per-language activation distributions rather than using entropy-based measures?
**Methodology**: The authors propose Distribution-aware Language Neuron selection, which leverages pairwise relationships between per-language activation distributions over the full activation range (including negative values). They quantify language specificity by clustering languages using pairwise overlap coefficients between their activation distributions, evaluated across two mLLMs and two held-out corpora.
**Key findings**:
- The proposed identifier more effectively isolates language-specific causal effects compared to existing entropy-based approaches
- The method yields up to 4.9× higher on-target language damage per neuron
- The approach preserves off-target language performance better than existing methods
**Limitations**: not stated in abstract

### Le and Li (2026)

**Research question**: How can language-specific neurons in multilingual LLMs be identified through functional necessity rather than activation-based heuristics?
**Methodology**: The paper proposes CRANE, a relevance-based analysis framework that identifies language-specific neurons through targeted neuron-level interventions, characterizing neuron specialization by their contribution to language-conditioned predictions rather than activation magnitude.
**Key findings**:
- Masking neurons relevant to a target language selectively degrades performance on that language while preserving performance on other languages
- Language-selective but non-exclusive neuron specializations exist in multilingual LLMs
- CRANE isolates language-specific components more precisely than activation-based methods
- Experiments on English, Chinese, and Vietnamese across multiple benchmarks validate the approach
- The framework includes a dedicated relevance-based metric and base-to-chat model transfer analysis
**Limitations**: not stated in abstract

### Lee et al. (2026)

**Research question**: How do different tokenizer designs balance efficiency and equity for multilingual LLMs, particularly for underrepresented Southeast Asian languages?
**Methodology**: The paper presents a systematic comparison of equitable tokenizers on a unified benchmark spanning 11 Southeast Asian languages, including downstream task performance through controlled 1.5B-parameter language model training using the same training data.
**Key findings**:
- State-of-the-art multilingual LLMs often use Byte-level BPE tokenizers that structurally favor high-resource languages and Latin scripts
- Parity-aware BPE achieves strong compression parity at competitive cost, lying on the Pareto frontier of the efficiency-equity trade-off
- Morphology-Driven Byte Encoding delivers the best semantic reasoning performance through morphologically richer representations, albeit at higher computational expense
- Byte Latent Transformer underperforms on downstream tasks, possibly due to misalignment with limited low-resource training data constraints
- Cross-lingual fairness and tokenization efficiency are not fundamentally at odds, offering practical guidance for equitable multilingual model design
**Limitations**: not stated in abstract

### Namazifard and Poech (2025)

**Research question**: How and where do multilingual large language models encode culture, and can culture-specific neurons be isolated and disentangled from language-specific neurons?
**Methodology**: The authors build on established methodology for identifying language-specific neurons to localize and isolate culture-specific neurons, using a curated dataset (MUREL) of 85.2 million tokens spanning six cultures. They conduct localization and intervention experiments to modulate culture neurons independently.
**Key findings**:
- LLMs encode different cultures in distinct neuron populations, predominantly in upper layers
- Culture neurons can be modulated largely independently of language-specific neurons
- Culture neurons can be modulated largely independently of neurons specific to other cultures
- Cultural knowledge and propensities in multilingual language models can be selectively isolated and edited
**Limitations**: not stated in abstract

### Valentini et al. (2026)

**Research question**: Does text generated by multilingual large language models resemble translationese, and how does MLLM-produced translationese differ from translationese produced through direct translation?
**Methodology**: The authors leverage established indicators of translated text to evaluate MLLM-generated text in five languages, comparing to both non-translated and human-written baselines. They use high-accuracy classification models, analyses of variance on individual linguistic features, and human annotations (in German and Spanish) to assess translationese content.
**Key findings**:
- The study assesses the translationese content of MLLM generations across five languages
- The research examines key linguistic features that distinguish MLLM-generated text from typical translation-related interference
- Human annotations were collected in German and Spanish to validate findings
**Limitations**: not stated in abstract

### Zhu et al. (2024)

**Research question**: What are the current architectures, datasets, evaluation methods, and applications of multilingual large language models?
**Methodology**: This paper provides a comprehensive survey covering MLLM architecture and pre-training objectives, multilingual dataset construction, evaluation benchmarks and taxonomies, interpretability analysis, and real-world applications across diverse domains.
**Key findings**:
- MLLMs represent an important advancement in AI with capabilities to understand and generate language across linguistic boundaries
- The survey presents a detailed taxonomy and roadmap for assessing MLLMs' cross-lingual knowledge, reasoning, alignment, safety, interpretability, and specialized applications
- Data quality and diversity in multilingual pre-training and alignment datasets are crucial for enhancing MLLM performance
- The paper addresses interpretability of multilingual capabilities, cross-lingual transfer, and language bias within these models
- MLLMs have driven innovation in specialized fields including biology, medicine, computer science, mathematics, and law
**Limitations**: not stated in abstract

## References

Bu, M., Zhang, S., He, Z., Wu, H., & Feng, Y. (2025). AlignX: Advancing multilingual large language models with multilingual representation alignment. arXiv. https://arxiv.org/abs/2509.24338

Cahyawijaya, S., Zhang, R., Lovenia, H., Cruz, J. C. B., Gilbert, E., Nomoto, H., & Aji, A. F. (2024). Thank you, stingray: Multilingual large language models can not (yet) disambiguate cross-lingual word sense. arXiv. https://arxiv.org/abs/2410.21573

Cui, X., Huang, Z., & Adel, N. (2025). Bias in, bias out: Annotation bias in multilingual large language models. arXiv. https://arxiv.org/abs/2511.14662

Kaneko, M., Aji, A. F., & Baldwin, T. (2025). Balanced multi-factor in-context learning for multilingual large language models. arXiv. https://arxiv.org/abs/2502.11495

Kim, M., Won, I., Yuk, J., Kim, D., Kim, J., & Lim, K. T. (2026). Distribution-aware language neuron identification in multilingual large language models. arXiv. https://arxiv.org/abs/2609.10993

Le, Y., & Li, Y. (2026). CRANE: Causal relevance analysis of language-specific neurons in multilingual large language models. arXiv. https://arxiv.org/abs/2601.04664

Lee, K. S. J. W., Qorib, M. R., Soegeng, A. I., & Ng, H. T. (2026). Equity with efficiency: An empirical study of tokenizers for multilingual large language models. arXiv. https://arxiv.org/abs/2606.15044

Namazifard, D., & Poech, L. G. (2025). Isolating culture neurons in multilingual large language models. arXiv. https://arxiv.org/abs/2508.02241

Valentini, M., Wright, T., Granados, J., Colunga, E., & von der Wense, K. (2026). An investigation of translationese in the generations of multilingual large language models. arXiv. https://arxiv.org/abs/2608.17399

Zhu, S., Supryadi, Xu, S., Sun, H., Pan, L., Cui, M., Du, J., Jin, R., Branco, A., & Xiong, D. (2024). Multilingual large language models: A systematic survey. arXiv. https://arxiv.org/abs/2411.11072
