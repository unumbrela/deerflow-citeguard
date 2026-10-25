# Systematic Literature Review: Low-Resource Machine Translation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "low-resource machine translation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in low-resource machine translation (MT) through analysis of 10 arXiv papers from 2024-2026. The surveyed literature reveals a field rapidly evolving along multiple complementary dimensions: novel training paradigms including federated learning and reinforcement learning, strategic exploitation of cross-linguistic transfer from typologically related languages, innovative pretraining approaches leveraging monolingual data, and critical investigation of real-world usage patterns. Collectively, these works demonstrate that the gap between high-resource and low-resource MT is narrowing through data-centric approaches, parameter-efficient methods, and community-grounded development practices. However, challenges remain in scaling these approaches across diverse language families and ensuring alignment between research outputs and actual community needs.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "low-resource machine translation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Novel Training Paradigms Beyond Standard Supervision

A prominent direction in recent low-resource MT research involves moving beyond conventional supervised training on parallel corpora. Several papers explore alternative learning frameworks that reduce dependence on large-scale annotated data. Moskvoretskii et al. (2024) introduce MeritOpt, a personalized federated learning approach that enables heterogeneous data integration across multiple auxiliary languages while maintaining interpretability about each language's contribution. Attia and Aji (2026) investigate round-trip reinforcement learning, using self-supervised fine-tuning with NLLB models where translations are evaluated through back-translation consistency measured by chrF++ and BLEU rewards. These approaches share a common insight: low-resource settings demand training methodologies that can extract signal from diverse, imperfect, or indirect supervision sources rather than relying solely on high-quality parallel data.

### Theme 2: Cross-Linguistic Transfer and Typological Leverage

Multiple papers demonstrate that strategic exploitation of linguistic relationships can substantially improve low-resource MT performance. Boujkian (2024) provides empirical evidence that transfer learning from typologically similar high-resource languages consistently improves translation quality across five diverse language families, with optimal hyperparameter configurations varying by linguistic similarity. Talwar and Laasri (2025) show that pivot languages can bridge gaps when direct parallel corpora are unavailable, achieving a 6.6-point SacreBLEU improvement for Nepali-English translation using Hindi as an intermediary. These works collectively establish that linguistic typology provides actionable priors for low-resource MT system design, though the degree of benefit depends on careful tuning of transfer parameters.

### Theme 3: Large Language Models as Enablers and Knowledge Sources

The emergence of capable large language models has opened new pathways for low-resource MT. Enis and Hopkins (2024) demonstrate that Claude 3 Opus exhibits remarkable resource efficiency in translation quality, with performance less dependent on language pair resource levels compared to traditional systems. Critically, they show that LLM capabilities can be distilled into smaller NMT models using synthetic data, achieving state-of-the-art Yoruba-English translation that meets or surpasses NLLB-54B and Google Translate. Salim et al. (2026) explore in-context learning with long-context models, finding that while gains from additional context saturate quickly, certain forms of monolingual supervision can compete with parallel data. These findings position LLMs as both direct translation tools and knowledge sources for augmenting traditional MT systems.

### Theme 4: Pretraining Strategies and Data Quality

The importance of pretraining methodology and data curation emerges as a recurring theme. Nguepi Nguefack et al. (2025) demonstrate that pretraining on multiple languages with both monolingual and parallel data significantly enhances translation quality for Lingala, extending approaches originally designed for high-resource languages. Thakkar et al. (2026) present BhashaSetu, a linguistically enriched English-Marathi dataset with 2.78 million sentence pairs, revealing that corpus-level deduplication alone contributes 1.17 BLEU improvement—a low-cost, high-impact intervention. These works emphasize that careful attention to pretraining data composition and hygiene can yield substantial gains independent of model architecture innovations.

### Theme 5: Community Needs and Real-World Usage

Moving beyond technical metrics, recent work increasingly grounds low-resource MT development in actual community usage patterns. Merx et al. (2024) conduct an observational study of 100,000 translation requests on a Tetun language service, revealing that users—predominantly students on mobile devices—translate from high-resource languages into Tetun across science, healthcare, and daily life domains. This contrasts sharply with available Tetun corpora dominated by government and social issue news articles. Their findings challenge the field to prioritize educational domain accuracy and high-resource to low-resource translation direction, demonstrating that observational analysis can reveal misalignments between research assumptions and community needs.

### Theme 6: Specialized Challenges: Code-Switching and Morphological Complexity

Several papers address specialized challenges within low-resource MT. Borisov et al. (2025) tackle code-switched Kazakh-Russian translation with no labeled data, using synthetic data generation to achieve 16.48 BLEU that nearly matches commercial systems and surpasses them in human evaluation. Thakkar et al. (2026) focus on morphology-aware processing for Marathi, a morphologically rich language, showing that stemmed and lemmatized representations support better model learning. These works highlight that low-resource MT is not monolithic—specific language pairs and communities face distinct challenges requiring tailored solutions rather than one-size-fits-all approaches.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers affirm that low-resource MT requires approaches beyond simply scaling data and compute—strategic inductive biases from linguistics, training methodology innovations, or data curation are essential. Second, there is consensus that monolingual data, when properly leveraged through pretraining or in-context learning, provides valuable signal despite lacking direct supervision. Third, multiple papers independently demonstrate that community-grounded development—whether through usage analysis or domain-diverse data collection—produces systems better aligned with real needs.

**Disagreements**: The literature reveals some tension regarding the role of large context windows in in-context learning. Salim et al. (2026) find that gains from scaling in-context demonstrations saturate quickly and can degrade near maximum context windows, suggesting diminishing returns from context expansion alone. This contrasts with the implicit assumption in other works that more data—whether through synthetic generation (Borisov et al., 2025) or large-scale corpus creation (Thakkar et al., 2026)—will yield proportional improvements. Additionally, while Talwar and Laasri (2025) find pivot language approaches promising, their semi-supervised backtranslation underperformed existing baselines, raising questions about when pivot methods are preferable to direct transfer learning approaches explored by Boujkian (2024).

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, evaluation remains limited in linguistic diversity: most papers evaluate on small sets of languages (typically 2-6), with African, South Asian, and Southeast Asian languages well-represented but other regions underexplored. Second, computational cost and accessibility receive minimal attention—while methods like MeritOpt claim ease of implementation, none of the surveyed papers provide detailed analysis of training costs or inference latency that would inform deployment decisions in resource-constrained settings. Third, the literature lacks longitudinal studies tracking whether low-resource MT systems maintain performance as languages evolve or as usage patterns shift over time. Fourth, while several papers release datasets and code, sustainability of these resources is unclear, with Nguepi Nguefack et al. (2025) noting that some data "may no longer be accessible due to changes in public availability." Finally, the field would benefit from standardized evaluation frameworks that assess not only translation quality but also alignment with community needs, domain coverage, and robustness to real-world usage patterns.

## Per-Paper Annotations

### Attia and Aji (2026)

**Research question**: Can self-supervised reinforcement learning fine-tuning with round-trip bootstrapping improve translation quality in low-resource settings?

**Methodology**: The authors investigate a self-supervised reinforcement learning approach using round-trip bootstrapping with NLLB models, translating English to target low-resource languages and back, using chrF++ and BLEU as reward functions on reconstructed English sentences.

**Key findings**:
- Consistent improvements observed across Central Aymara, Friulian, Wolof, Dyula, Bhojpuri, and Russian
- Qualitative inspection shows increased fluency and semantic fidelity in translation outputs
- The method benefits from model scale, enabling models to leverage pretrained knowledge for self-improvement
- Works effectively with both 600M and 1.3B parameter NLLB models

**Limitations**: Evaluation was limited to languages available in the NLLB-MD dataset; the approach requires access to NLLB family models and may not transfer to other model architectures without modification.

### Boujkian (2024)

**Research question**: Does transfer learning from typologically similar high-resource languages improve low-resource machine translation when limited target language data is available?

**Methodology**: The study fine-tunes models initially trained on typologically similar high-resource languages using limited data from target low-resource languages, testing across five typologically diverse language families with hyperparameter variations.

**Key findings**:
- Transfer learning consistently improves translation quality across all five language family pairs tested
- The approach confirms applicability beyond closely related languages, showing generalizability across language families
- Moderate batch sizes (e.g., 32) are often optimal for typologically similar pairs
- Smaller batch sizes benefit less similar language pairs
- Excessively high learning rates can destabilize training

**Limitations**: Only tested on five specific language pairs spanning distinct families; while hyperparameter analysis provides guidance, some tuning effort is still required for optimal results on new language pairs.

### Borisov et al. (2025)

**Research question**: How can we build MT models for code-switched low-resource language pairs without any labeled training data?

**Methodology**: Proposed a method based on synthetic data generation for code-switched Kazakh-Russian translation and created the first code-switching parallel corpus for this language pair.

**Key findings**:
- Achieved 16.48 BLEU score using synthetic data with no labeled training data
- Model performance nearly reaches existing commercial system levels
- Human evaluation showed the model beats the commercial system
- First code-switching Kazakh-Russian parallel corpus was created and released

**Limitations**: No labeled training data available, relying entirely on synthetic data generation which may not capture all natural code-switching patterns and variations.

### Enis and Hopkins (2024)

**Research question**: How does Claude 3 Opus perform on low-resource machine translation, and can its translation capabilities be distilled into traditional NMT models?

**Methodology**: The authors evaluate Claude 3 Opus on curated benchmarks for low-resource translation into English, then use Claude to generate synthetic data for knowledge distillation into traditional NMT models, demonstrated on Yoruba-English translation.

**Key findings**:
- Claude 3 Opus exhibits stronger machine translation competence than other LLMs
- Claude demonstrates remarkable resource efficiency in translation quality relative to language pair resource levels
- Knowledge distillation from Claude achieves state-of-the-art Yoruba-English translation, meeting or surpassing NLLB-54B and Google Translate
- Advancements in LLM translation can be successfully compressed into traditional NMT models

**Limitations**: Evidence of data contamination with Claude on FLORES-200 benchmark required curating new benchmarks; the study focuses primarily on translation into English rather than bidirectional translation capabilities.

### Merx et al. (2024)

**Research question**: What are the actual usage patterns and community needs for low-resource MT services, specifically for the Tetun language?

**Methodology**: Conducted observational analysis of 100,000 translation requests from tetun.org to identify real-world usage patterns and compared them against existing Tetun corpora.

**Key findings**:
- Users, predominantly students on mobile devices, typically translate from high-resource languages into Tetun
- Translation requests span diverse domains including science, healthcare, and daily life
- Available Tetun corpora are dominated by news articles covering government and social issues, misaligned with actual user needs
- MT systems for institutionalized minority languages should prioritize accuracy on educational domains in the high-resource to low-resource direction

**Limitations**: Observational study limited to one language (Tetun) and one translation service; findings may not generalize to other low-resource languages with different community contexts.

### Moskvoretskii et al. (2024)

**Research question**: How can Personalized Federated Learning be applied to improve low-resource machine translation with heterogeneous data?

**Methodology**: The authors present MeritOpt, a new approach based on the Personalized Federated Learning algorithm MeritFed, evaluated on low-resource machine translation tasks using datasets of South East Asian and Finno-Ugric languages.

**Key findings**:
- Target dataset size affects weight distribution across auxiliary languages
- Unrelated languages do not interfere with the training process
- Auxiliary optimizer parameters have minimal impact on performance
- The approach is highly interpretable and can track the impact of each language used for training

**Limitations**: Evaluation was limited to South East Asian and Finno-Ugric language families, which may not generalize to other language groups; the abstract does not discuss computational costs or scalability concerns.

### Nguepi Nguefack et al. (2025)

**Research question**: What pretraining strategies most effectively improve machine translation quality for low-resource languages?

**Methodology**: The authors explore different pretraining methodologies for Lingala, building on Reid and Artetxe (2021), experimenting with integration of multiple languages and use of both monolingual and parallel data during the pretraining phase.

**Key findings**:
- Pretraining on multiple languages significantly enhances translation quality
- Leveraging both monolingual and parallel data during pretraining improves performance
- The approach helps bridge the performance gap between high-resource and low-resource languages
- Results contribute to developing more inclusive NLP models for marginalized communities and underrepresented populations

**Limitations**: Some datasets used may no longer be accessible due to changes in public availability; the study primarily focuses on Lingala as the target language, though several other low-resource languages were considered.

### Salim et al. (2026)

**Research question**: How does scaling in-context learning beyond few-shot to thousands of examples affect low-resource machine translation performance?

**Methodology**: Scaled in-context token budget to 1M tokens and compared three types of training corpora (monolingual unsupervised, instruction-style, and parallel data) for Javanese and Sundanese translation using long-context models.

**Key findings**:
- Gains from additional context saturate quickly and can degrade near the maximum context window
- Scaling behavior strongly depends on corpus type
- Some forms of monolingual supervision can be competitive with parallel data despite offering less direct supervision
- Larger context windows do not necessarily yield proportional quality gains

**Limitations**: Limited evaluation to only Javanese and Sundanese languages; saturation effects and corpus-type sensitivity may vary across other low-resource languages and language families.

### Talwar and Laasri (2025)

**Research question**: Can Hindi serve as an effective pivot language for translating Nepali to English when direct parallel corpora are scarce?

**Methodology**: Used Hindi as a pivot language with two approaches—Transfer Method (fully supervised) and Backtranslation (semi-supervised)—to translate Nepali into English.

**Key findings**:
- Transfer Method achieved 14.2 SacreBLEU, improving the baseline fully supervised score by 6.6 points
- Hindi's linguistic similarity to Nepali makes it a suitable pivot language candidate
- Pivot language approaches can significantly improve translation quality when direct parallel data is unavailable

**Limitations**: Semi-supervised approach underperformed compared to existing baselines with unclear causes; evaluation limited to Nepali-Hindi-English language triplet.

### Thakkar et al. (2026)

**Research question**: How can linguistically enriched parallel datasets improve low-resource NMT for morphologically rich languages like Marathi?

**Methodology**: Created BhashaSetu dataset with 2.78M sentence pairs from diverse sources with stemmed and lemmatized representations; benchmarked multiple models with parameter-efficient fine-tuning using LoRA on NLLB-200.

**Key findings**:
- Corpus-level deduplication is the single largest preprocessing contributor to downstream quality
- Removing deduplication reduces performance by 1.17 BLEU and 2.21 chrF++
- Disciplined cross-source corpus hygiene is a low-cost, high-impact intervention for low-resource, morphologically rich languages
- Dataset covers diverse domains including news, politics, healthcare, literature, and culture

**Limitations**: Focused primarily on English-Marathi language pair; findings about preprocessing importance may not generalize equally to all low-resource languages with different morphological characteristics.

## References

Attia, A., & Aji, A. F. (2026). Improving low-resource machine translation via round-trip reinforcement learning. arXiv. https://arxiv.org/abs/2601.12535

Borisov, M., Kozhirbayev, Z., & Malykh, V. (2025). Low-resource machine translation for code-switched Kazakh-Russian language pair. arXiv. https://arxiv.org/abs/2503.20007

Boujkian, S. (2024). Improving low-resource machine translation via cross-linguistic transfer from typologically similar high-resource languages. arXiv. https://arxiv.org/abs/2501.00045

Enis, M., & Hopkins, M. (2024). From LLM to NMT: Advancing low-resource machine translation with Claude. arXiv. https://arxiv.org/abs/2404.13813

Merx, R., Correia, A. J. G., Suominen, H., & Vylomova, E. (2024). Low-resource machine translation: what for? who for? An observational study on a dedicated Tetun language translation service. arXiv. https://arxiv.org/abs/2411.12262

Moskvoretskii, V., Tupitsa, N., Biemann, C., Horváth, S., Gorbunov, E., & Nikishina, I. (2024). Low-resource machine translation through the lens of personalized federated learning. arXiv. https://arxiv.org/abs/2406.12564

Nguepi Nguefack, I., Finkelstein, M., & Sakayo, T. S. (2025). Pretraining strategies using monolingual and parallel data for low-resource machine translation. arXiv. https://arxiv.org/abs/2510.25116

Salim, L. F., Carlin, E., Morinvil, A., Ai, X., & Ku, L.-W. (2026). Beyond many-shot translation: Scaling in-context demonstrations for low-resource machine translation. arXiv. https://arxiv.org/abs/2602.04764

Talwar, A., & Laasri, J. (2025). Pivot language for low-resource machine translation. arXiv. https://arxiv.org/abs/2505.14553

Thakkar, P., Yadav, A., Tiemann, M., Mehta, A., Bhasin, A., & Khedkar, S. (2026). BhashaSetu: A data-centric approach to low-resource machine translation. arXiv. https://arxiv.org/abs/2605.27050
