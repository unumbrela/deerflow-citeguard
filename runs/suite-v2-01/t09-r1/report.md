# Systematic Literature Review: Multilingual Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "multilingual large language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on multilingual large language models (MLLMs) reveals a field increasingly focused on interpretability, fairness, and cross-lingual capability enhancement. Recent research has moved beyond simply building larger multilingual models toward understanding how these models encode language-specific and culture-specific knowledge at the neuron level. Several papers investigate methods to identify, isolate, and manipulate language-specific neurons, enabling more precise control over multilingual behavior. Concurrent work addresses critical challenges in evaluation bias, tokenization equity, and in-context learning optimization. The collective findings suggest that while MLLMs have made significant progress, fundamental challenges remain in achieving true cross-lingual understanding, equitable representation across languages, and mitigation of annotation and cultural biases.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "multilingual large language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Neuron-Level Interpretability and Language-Specific Components

A significant research direction focuses on understanding how multilingual LLMs encode language-specific and culture-specific knowledge at the neuron level. Multiple studies propose methods to identify and isolate neurons responsible for particular languages or cultural knowledge, enabling targeted interventions without affecting other capabilities.

Namazifard & Galke Poech (2025) introduced MUREL, a dataset and methodology for isolating culture neurons distinct from language-specific neurons, demonstrating that cultural knowledge can be selectively modulated in upper layers of multilingual models. Kim et al. (2026) proposed Distribution-aware Language Neuron selection, which uses pairwise relationships between per-language activation distributions to more effectively identify language-specific neurons than entropy-based approaches, achieving up to 4.9× higher on-target language damage per neuron while preserving off-target performance. Le & Li (2026) developed CRANE, a causal relevance analysis framework that identifies language-specific neurons through functional necessity rather than activation magnitude, showing that masking relevant neurons selectively degrades performance on the target language while preserving others.

### Theme 2: Cross-Lingual Representation Alignment and Capability Enhancement

Another prominent theme addresses methods to bridge performance gaps across languages through representation-level alignment rather than extensive fine-tuning on multilingual corpora.

Bu et al. (2025) proposed AlignX, a two-stage framework that aligns multilingual representations through semantic alignment and language feature integration, followed by multilingual instruction fine-tuning. Their approach brings multilingual representations closer together and improves cross-lingual generation capabilities compared to existing fine-tuning approaches. Kaneko et al. (2025) addressed example selection in multilingual in-context learning through balanced multi-factor ICL (BMF-ICL), which optimally balances semantic similarity, linguistic alignment, and language-specific performance, outperforming existing methods across multiple benchmarks and models.

### Theme 3: Bias Detection, Annotation Quality, and Cultural Fairness

Several papers address critical challenges related to bias in multilingual model development, evaluation, and deployment, particularly concerning annotation practices and cultural representation.

Cui et al. (2025) provided a comprehensive framework for detecting and mitigating annotation bias in multilingual LLM development, distinguishing among instruction bias, annotator bias, and contextual/cultural bias. Their work reviews detection methods including inter-annotator agreement, model disagreement, and metadata analysis, while proposing mitigation strategies such as diverse annotator recruitment and iterative guideline refinement. Valentini et al. (2026) investigated translationese in MLLM-generated text across five languages, using high-accuracy classification models and human annotations to distinguish MLLM-produced translationese from human translation artifacts.

### Theme 4: Tokenization Equity and Efficiency Trade-offs

Research on tokenization reveals growing attention to the structural biases embedded in tokenizer design and their impact on underrepresented languages.

Lee et al. (2026) conducted a systematic comparison of equitable tokenizers across 11 Southeast Asian languages, demonstrating that state-of-the-art multilingual LLMs use Byte-level BPE tokenizers that structurally favor high-resource languages and Latin scripts. Their work shows that parity-aware BPE achieves strong compression parity at competitive cost, while Morphology-Driven Byte Encoding delivers superior semantic reasoning performance through morphologically richer representations, albeit at higher computational expense. The findings suggest that cross-lingual fairness and tokenization efficiency are not fundamentally at odds.

### Theme 5: Evaluation Benchmarks and Cross-Lingual Semantic Understanding

Recent work highlights significant limitations in current multilingual models' ability to handle cross-lingual semantic disambiguation and reveals biases toward high-resource languages.

Cahyawijaya et al. (2024) introduced StingrayBench, a novel benchmark for cross-lingual sense disambiguation using false friends across four language pairs. Their findings reveal that multilingual LLMs tend to be biased toward higher-resource languages when disambiguating false friends and cannot reliably distinguish the use of false friends in context, highlighting limitations in cross-lingual semantic evaluation beyond English.

### Theme 6: Comprehensive Survey and Application Domains

The field has also seen efforts to comprehensively survey the state of multilingual LLM research and document real-world applications.

Zhu et al. (2024) provided a comprehensive survey covering MLLM architecture, pre-training objectives, dataset construction, evaluation benchmarks, interpretability analysis, and applications across biology, medicine, computer science, mathematics, and law. Their work emphasizes that data quality and diversity are crucial for enhancing MLLM performance, while evaluation must cover cross-lingual knowledge, reasoning, alignment with human values, safety, and interpretability.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that multilingual LLMs encode language-specific and culture-specific knowledge in distinct, identifiable neuron populations that can be selectively modulated (Namazifard & Galke Poech, 2025; Kim et al., 2026; Le & Li, 2026). There is also broad agreement that current MLLMs exhibit systematic biases toward high-resource languages in tokenization (Lee et al., 2026), in-context learning example selection (Kaneko et al., 2025), and cross-lingual semantic disambiguation (Cahyawijaya et al., 2024). The surveyed literature collectively emphasizes that annotation bias and cultural bias significantly impact model outputs, requiring systematic detection and mitigation approaches (Cui et al., 2025).

**Disagreements**: While there is convergence on the existence of language-specific neurons, different studies propose competing methodologies for their identification—entropy-based measures (Kim et al., 2026) versus causal relevance analysis (Le & Li, 2026) versus culture-versus-language disentanglement (Namazifard & Galke Poech, 2025). On tokenization, Lee et al. (2026) find that Morphology-Driven Byte Encoding delivers superior semantic performance at higher cost, while parity-aware BPE offers a more balanced trade-off—suggesting disagreement on the optimal approach depending on the use case. The literature does not resolve whether representation-level alignment (Bu et al., 2025) or extensive multilingual fine-tuning is more effective for capability enhancement.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Limited explicit limitations reporting**: None of the surveyed papers explicitly stated limitations in their abstracts, suggesting either under-reporting of methodological constraints or space limitations in abstracts.

2. **Scalability of neuron-level interventions**: While multiple studies demonstrate successful isolation and manipulation of language-specific neurons, none address the computational cost or scalability of these approaches to production-scale models with hundreds of billions of parameters.

3. **Cross-lingual transfer mechanisms**: Despite progress in representation alignment, the fundamental mechanisms enabling cross-lingual transfer remain incompletely understood, particularly for low-resource languages.

4. **Cultural versus linguistic disentanglement**: The relationship between culture-specific and language-specific neurons requires further investigation, particularly for languages spoken across multiple cultural contexts.

5. **Evaluation beyond English-centric benchmarks**: Current evaluation practices remain biased toward English and high-resource languages, with limited benchmarks for truly low-resource language capabilities (Cahyawijaya et al., 2024; Lee et al., 2026).

6. **Long-term impact of annotation bias**: While annotation bias detection methods are proposed (Cui et al., 2025), longitudinal studies on the cumulative impact of biased training data on model behavior across languages are absent.

## Per-Paper Annotations

### Bu et al. (2025)

**Research question**: How can multilingual performance gaps in pre-trained LLMs be bridged through representation-level alignment rather than fine-tuning on large-scale multilingual corpora?
**Methodology**: The authors propose AlignX, a two-stage representation-level framework: (1) aligning multilingual representations with multilingual semantic alignment and language feature integration, and (2) stimulating multilingual capability via multilingual instruction fine-tuning, evaluated on several pre-trained LLMs.
**Key findings**:
- AlignX enhances LLMs' multilingual general and cross-lingual generation capability
- The approach brings multilingual representations closer together
- AlignX improves cross-lingual alignment compared to existing fine-tuning approaches
**Limitations**: not stated in abstract

### Cahyawijaya et al. (2024)

**Research question**: Can multilingual LLMs reliably disambiguate cross-lingual word sense, particularly for false friends across language pairs?
**Methodology**: The paper introduces StingrayBench, a novel benchmark for cross-lingual sense disambiguation using false friends (orthographically similar words with different meanings) across four language pairs: Indonesian-Malay, Indonesian-Tagalog, Chinese-Japanese, and English-German.
**Key findings**:
- Multilingual LLMs tend to be biased toward higher-resource languages when disambiguating false friends
- Current multilingual LLMs cannot reliably distinguish the use of false friends in context
- New metrics are proposed for quantifying cross-lingual sense bias and comprehension
- The work highlights limitations in cross-lingual semantic evaluation beyond English
**Limitations**: not stated in abstract

### Cui et al. (2025)

**Research question**: How can annotation bias in NLP datasets be detected and mitigated in multilingual LLM development?
**Methodology**: The paper proposes a comprehensive framework that distinguishes among instruction bias, annotator bias, and contextual/cultural bias, and reviews detection methods including inter-annotator agreement, model disagreement, and metadata analysis.
**Key findings**:
- Annotation bias stems from task framing, annotator subjectivity, and cultural mismatches that distort model outputs
- Detection methods include inter-annotator agreement, model disagreement, metadata analysis, multilingual model divergence, and cultural inference
- Mitigation strategies include diverse annotator recruitment, iterative guideline refinement, and post-hoc model adjustments
- The paper provides a typology of annotation bias, synthesis of detection metrics, ensemble-based bias mitigation approach, and ethical analysis
**Limitations**: not stated in abstract

### Kaneko et al. (2025)

**Research question**: How can example selection in multilingual in-context learning be optimized by explicitly disentangling and balancing the combined impact of semantic similarity, linguistic alignment, and language-specific performance?
**Methodology**: The authors propose balanced multi-factor ICL (BMF-ICL), a method that quantifies and optimally balances three key factors (semantic similarity, linguistic alignment, and language-specific performance) for improved example selection, evaluated on mCSQA and TYDI benchmarks across four MLLMs.
**Key findings**:
- BMF-ICL outperforms existing methods on mCSQA and TYDI benchmarks across four MLLMs
- Incorporating all three factors (semantic similarity, linguistic alignment, language-specific performance) is important for optimal performance
- Selecting examples from multiple languages improves in-context learning effectiveness
**Limitations**: not stated in abstract

### Kim et al. (2026)

**Research question**: Can language specificity in multilingual LLMs be more effectively captured by leveraging pairwise relationships between per-language activation distributions rather than using entropy-based measures?
**Methodology**: The authors propose Distribution-aware Language Neuron selection, which quantifies language specificity by clustering languages using pairwise overlap coefficients between their activation distributions over the full activation range (including negative values), evaluated across two mLLMs and two held-out corpora.
**Key findings**:
- The distribution-aware identifier more effectively isolates language-specific causal effects than entropy-based approaches
- The method yields up to 4.9× higher on-target language damage per neuron
- The approach preserves off-target language performance while isolating language-specific neurons
**Limitations**: not stated in abstract

### Le & Li (2026)

**Research question**: How can language-specific neurons in multilingual LLMs be identified based on functional necessity rather than activation magnitude?
**Methodology**: The paper proposes CRANE, a relevance-based analysis framework that identifies language-specific neurons through targeted neuron-level interventions, characterizing specialization by contribution to language-conditioned predictions rather than activation magnitude.
**Key findings**:
- Masking neurons relevant to a target language selectively degrades performance on that language while preserving performance on others
- CRANE isolates language-specific components more precisely than activation-based methods
- Language-selective but non-exclusive neuron specializations exist in multilingual LLMs
- Experiments on English, Chinese, and Vietnamese across multiple benchmarks validate the approach
**Limitations**: not stated in abstract

### Lee et al. (2026)

**Research question**: How do different tokenizer designs balance compression efficiency and cross-lingual equity for underrepresented Southeast Asian languages?
**Methodology**: The paper presents a systematic comparison of equitable tokenizers on a unified benchmark spanning 11 Southeast Asian languages, with downstream task performance assessed through controlled 1.5B-parameter language model training using the same training data.
**Key findings**:
- State-of-the-art multilingual LLMs use Byte-level BPE tokenizers that structurally favor high-resource languages and Latin scripts
- Parity-aware BPE achieves strong compression parity at competitive cost on the efficiency-equity trade-off
- Morphology-Driven Byte Encoding delivers the best semantic reasoning performance through morphologically richer representations, at higher computational expense
- Byte Latent Transformer underperforms on downstream tasks due to architectural misalignment with limited low-resource training data
- Cross-lingual fairness and tokenization efficiency are not fundamentally at odds
**Limitations**: not stated in abstract

### Namazifard & Galke Poech (2025)

**Research question**: How and where do multilingual large language models encode culture, and can culture-specific neurons be isolated and modulated independently of language-specific neurons?
**Methodology**: The authors introduce MUREL, a curated dataset of 85.2 million tokens spanning six cultures, and apply localization and intervention experiments to identify and isolate culture-specific neurons in multilingual LLMs, disentangling them from language-specific neurons.
**Key findings**:
- LLMs encode different cultures in distinct neuron populations, predominantly in upper layers
- Culture-specific neurons can be modulated largely independently of language-specific neurons
- Culture neurons can be modulated largely independently of neurons specific to other cultures
- Cultural knowledge and propensities in multilingual language models can be selectively isolated and edited
**Limitations**: not stated in abstract

### Valentini et al. (2026)

**Research question**: Does text generated by multilingual large language models resemble translationese, and how does MLLM-produced translationese differ from translationese produced through direct human translation?
**Methodology**: The authors leverage established indicators of translated text to evaluate MLLM-generated text in five languages, comparing to non-translated and human-written baselines, using high-accuracy classification models, variance analyses on linguistic features, and human annotations in German and Spanish.
**Key findings**:
- The study assesses translationese content in MLLM generations across five languages
- High-accuracy classification models can distinguish MLLM-generated text from typical translation-related interference
- Human annotations in German and Spanish help identify key features distinguishing MLLM-generated translationese
**Limitations**: not stated in abstract

### Zhu et al. (2024)

**Research question**: What are the key architectures, datasets, evaluation methods, and applications of multilingual large language models?
**Methodology**: The paper provides a comprehensive survey covering MLLM architecture and pre-training objectives, dataset construction, evaluation benchmarks and taxonomies, interpretability analysis, and real-world applications across diverse domains.
**Key findings**:
- MLLMs represent an important advancement in AI with capabilities to understand and generate language across linguistic boundaries
- Data quality and diversity are crucial for enhancing MLLM performance
- Evaluation covers cross-lingual knowledge, reasoning, alignment with human values, safety, interpretability, and specialized applications
- MLLMs have driven innovation in biology, medicine, computer science, mathematics, and law
- Challenges and opportunities exist in deploying MLLMs within diverse language communities
**Limitations**: not stated in abstract

## References

Bu, M., Zhang, S., He, Z., Wu, H., & Feng, Y. (2025). AlignX: Advancing multilingual large language models with multilingual representation alignment. arXiv. https://arxiv.org/abs/2509.24338

Cahyawijaya, S., Zhang, R., Lovenia, H., Cruz, J. C. B., Gilbert, E., Nomoto, H., & Aji, A. F. (2024). Thank you, Stingray: Multilingual large language models can not (yet) disambiguate cross-lingual word sense. arXiv. https://arxiv.org/abs/2410.21573

Cui, X., Huang, Z., & Adel, N. (2025). Bias in, bias out: Annotation bias in multilingual large language models. arXiv. https://arxiv.org/abs/2511.14662

Kaneko, M., Aji, A. F., & Baldwin, T. (2025). Balanced multi-factor in-context learning for multilingual large language models. arXiv. https://arxiv.org/abs/2502.11495

Kim, M., Won, I., Yuk, J., Kim, D., Kim, J., & Lim, K. T. (2026). Distribution-aware language neuron identification in multilingual large language models. arXiv. https://arxiv.org/abs/2609.10993

Le, Y., & Li, Y. (2026). CRANE: Causal relevance analysis of language-specific neurons in multilingual large language models. arXiv. https://arxiv.org/abs/2601.04664

Lee, K. S. J. W., Qorib, M. R., Soegeng, A. I., & Ng, H. T. (2026). Equity with efficiency: An empirical study of tokenizers for multilingual large language models. arXiv. https://arxiv.org/abs/2606.15044

Namazifard, D., & Galke Poech, L. (2025). Isolating culture neurons in multilingual large language models. arXiv. https://arxiv.org/abs/2508.02241

Valentini, M., Wright, T., Granados, J., Colunga, E., & von der Wense, K. (2026). An investigation of translationese in the generations of multilingual large language models. arXiv. https://arxiv.org/abs/2608.17399

Zhu, S., Supryadi, Xu, S., Sun, H., Pan, L., Cui, M., Du, J., Jin, R., Branco, A., & Xiong, D. (2024). Multilingual large language models: A systematic survey. arXiv. https://arxiv.org/abs/2411.11072
