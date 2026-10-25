# Systematic Literature Review: Low-Resource Machine Translation

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "low-resource machine translation", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines ten recent arXiv papers (2024-2026) addressing low-resource machine translation (MT), revealing a field rapidly evolving through diverse methodological approaches. The surveyed literature demonstrates that effective low-resource MT no longer relies solely on traditional parallel corpus expansion but instead leverages innovative strategies including pivot languages, round-trip reinforcement learning, cross-linguistic transfer from typologically similar languages, sophisticated pretraining regimes, and data-centric curation. Several papers emphasize the critical importance of understanding actual user needs and deployment contexts, challenging the assumption that more data automatically translates to better performance. Collectively, these works show that small, carefully curated datasets combined with targeted adaptation techniques can outperform larger, noisier alternatives, with some systems achieving competitive results using models as small as 0.8B parameters.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "low-resource machine translation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Data-Centric Approaches and Corpus Quality

A prominent theme across multiple papers is the recognition that data quality matters more than quantity for low-resource MT. Thakkar et al. (2026) demonstrate that corpus-level deduplication alone contributes 1.17 BLEU and 2.21 chrF++ improvements, characterizing disciplined cross-source corpus hygiene as a "low-cost, high-impact intervention." Their BhashaSetu dataset for English-Marathi translation comprises 2.78 million sentence pairs from diverse domains with stemmed and lemmatized representations. Similarly, Gritta et al. (2026) show that unified quality-estimation filtering removes up to 96% of training tokens without degrading quality, with filtered synthetic data dominating the quality-efficiency Pareto frontier for 19 Sub-Saharan African languages. This data-centric perspective challenges the prevailing assumption that scaling data volume is the primary path to improvement.

### Theme 2: Transfer Learning and Cross-Linguistic Strategies

Multiple papers explore how knowledge from high-resource languages can be transferred to low-resource settings. Boujkian (2024) systematically demonstrates that transfer learning from typologically similar high-resource languages consistently improves translation quality across five diverse language families (Semitic, Bantu, Romance, Slavic, and language isolates), confirming applicability beyond closely related languages. The work reveals nuanced hyperparameter sensitivities, with moderate batch sizes (e.g., 32) optimal for similar language pairs while smaller batch sizes benefit less similar pairs. Talwar and Laasri (2025) employ Hindi as a pivot language for Nepali-to-English translation, achieving a SacreBLEU score of 14.2 with the Transfer Method—a 6.6-point improvement over baseline. These approaches share the insight that strategic selection of source languages based on linguistic relationships can dramatically reduce the data requirements for effective MT.

### Theme 3: Self-Supervised and Reinforcement Learning Techniques

Recent work increasingly employs self-supervised signals to improve low-resource MT without requiring additional parallel data. Attia and Aji (2026) introduce round-trip reinforcement learning, translating English into target languages and back, using chrF++ and BLEU as reward functions on reconstructed English sentences. Their approach yields consistent improvements across six languages from Central Aymara to Russian, with qualitative inspection showing increased fluency and semantic fidelity. This bootstrapping strategy enables models to leverage pretrained knowledge for self-improvement, particularly valuable when parallel supervision is scarce. The method's scalability suggests that even modest-sized models (600M to 1.3B parameters) can benefit from such self-supervised fine-tuning.

### Theme 4: In-Context Learning and Scaling Behavior

The application of long-context models to low-resource MT reveals complex scaling dynamics. Salim et al. (2026) scale in-context learning to 1M tokens for Javanese and Sundanese translation, comparing monolingual unsupervised data, instruction-style data, and parallel data as in-context supervision. Counterintuitively, they find that gains from additional context saturate quickly and can degrade near the maximum context window, with scaling behavior strongly dependent on corpus type. Some forms of monolingual supervision prove competitive with parallel data despite offering less explicit supervision. These findings caution against naive scaling assumptions and highlight the importance of understanding what types of context actually contribute to translation quality.

### Theme 5: User-Centered Design and Deployment Contexts

Several papers emphasize understanding actual user needs rather than optimizing abstract metrics. Merx et al. (2024) conduct an observational study of 100,000 translation requests from tetun.org, revealing that users—many students on mobile devices—typically translate from high-resource languages into Tetun across diverse domains including science, healthcare, and daily life. Critically, available Tetun corpora are dominated by news articles covering government and social issues, contrasting sharply with actual user needs. This mismatch suggests that MT systems for institutionalized minority languages should prioritize accuracy on domains relevant to educational contexts. Merx et al. (2025) extend this user-centered approach with TULUN, a platform enabling non-technical users to create and leverage terminology resources without model fine-tuning.

### Theme 6: Synthetic Data Generation and Augmentation

When parallel data is unavailable, synthetic data generation emerges as a viable strategy. Borisov et al. (2025) build a machine translation model for code-switched Kazakh-Russian with no labeled data using synthetic data generation, achieving 16.48 BLEU and nearly matching commercial systems. Human evaluation shows their model beats the commercial system, and they present the first code-switching Kazakh-Russian parallel corpus. Gritta et al. (2026) similarly leverage African-specialized synthetic data as part of TranslatePsy-AfriSLM, demonstrating that carefully filtered synthetic data can dominate quality-efficiency frontiers. These works validate synthetic data as a legitimate resource when combined with rigorous quality filtering.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that careful data curation and strategic adaptation outperform naive scaling. Thakkar et al. (2026), Gritta et al. (2026), and Merx et al. (2024) all emphasize that understanding data quality, user needs, and domain relevance matters more than raw corpus size. Similarly, Attia and Aji (2026), Boujkian (2024), and Talwar and Laasri (2025) all demonstrate that leveraging existing pretrained knowledge—whether through reinforcement learning, cross-linguistic transfer, or pivot languages—consistently improves low-resource MT performance. There is broad agreement that small, well-designed interventions can yield substantial gains.

**Disagreements**: Talwar and Laasri (2025) find that their semi-supervised backtranslation approach underperforms compared to baseline (15.1 vs. 14.2 SacreBLEU for the Transfer Method), while Attia and Aji (2026) report consistent improvements from their round-trip reinforcement learning approach. This suggests that not all self-supervised strategies are equally effective, and the specific implementation details matter substantially. Additionally, Salim et al. (2026) find that larger context windows do not necessarily yield proportional quality gains, challenging assumptions underlying many long-context MT approaches.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. First, none of the papers explicitly address computational efficiency or deployment constraints in resource-limited settings, despite the focus on low-resource languages—this represents a significant gap between research and practical deployment. Second, while multiple papers mention domain mismatch between available corpora and actual user needs (Merx et al., 2024; Thakkar et al., 2026), few propose systematic methods for identifying and addressing these mismatches before data collection. Third, the limitations sections are largely unstated in abstracts, suggesting that systematic limitation analysis may be underreported. Fourth, while Gritta et al. (2026) achieve competitive performance with 0.8B parameter models, there is limited exploration of the absolute minimum model size required for different language pairs and domains. Finally, the temporal gap between user-need studies and system development suggests a need for more iterative, user-informed MT development cycles.

## Per-Paper Annotations

### Attia and Aji (2026)

**Research question**: Can self-supervised reinforcement learning fine-tuning with round-trip bootstrapping improve machine translation quality in low-resource language settings?

**Methodology**: The authors translate English into target low-resource languages and back into English using NLLB models (600M and 1.3B parameters), applying chrF++ and BLEU as reward functions on reconstructed English sentences. They evaluate on six languages from the NLLB-MD dataset.

**Key findings**:
- Consistent improvements observed across Central Aymara, Friulian, Wolof, Dyula, Bhojpuri and Russian
- Qualitative inspection shows increased fluency and semantic fidelity in translation outputs
- The method can benefit from scale, enabling models to leverage pretrained knowledge for self-improvement

**Limitations**: Not stated in abstract

### Boujkian (2024)

**Research question**: Does linguistic similarity enable efficient adaptation in transfer learning for low-resource machine translation, reducing the need for extensive training data?

**Methodology**: Experiments conducted on five typologically diverse language pairs (Semitic, Bantu, Romance, Slavic, and language isolate) with fine-tuning models initially trained on typologically similar high-resource languages. Secondary analysis varied hyperparameters including learning rate, batch size, epochs, and weight decay.

**Key findings**:
- Transfer learning consistently improves translation quality across all language pairs, confirming applicability beyond closely related languages
- Moderate batch sizes (e.g., 32) are often optimal for similar language pairs
- Smaller batch sizes benefit less similar language pairs
- Excessively high learning rates can destabilize training

**Limitations**: Not stated in abstract

### Nguepi Nguefack et al. (2025)

**Research question**: What pretraining strategies are most effective for developing machine translation models for low-resource languages?

**Methodology**: Comprehensive experiments exploring different pretraining methodologies including integration of multiple languages and use of both monolingual and parallel data during pretraining, building upon Reid and Artetxe (2021) approach, with focus on Lingala as the target language.

**Key findings**:
- Pretraining on multiple languages significantly enhances translation quality
- Leveraging both monolingual and parallel data during pretraining improves translation quality
- The approach helps bridge the performance gap between high-resource and low-resource languages

**Limitations**: Not stated in abstract

### Salim et al. (2026)

**Research question**: How does scaling in-context learning beyond few-shot to thousands of examples with long-context models affect low-resource machine translation performance?

**Methodology**: Experiments scaling in-context token budget to 1M tokens on Javanese and Sundanese, comparing three types of training corpora as in-context supervision: monolingual unsupervised data, instruction-style data, and parallel data (English-target and Indonesian-target).

**Key findings**:
- Gains from additional context saturate quickly and can degrade near the maximum context window
- Scaling behavior is strongly dependent on corpus type
- Some forms of monolingual supervision can be competitive with parallel data despite offering less supervision
- Larger context windows do not necessarily yield proportional quality gains

**Limitations**: Not stated in abstract

### Merx et al. (2024)

**Research question**: What are the actual usage patterns and community needs for low-resource machine translation, as revealed through observational analysis of a Tetun language translation service?

**Methodology**: Observational study analyzing 100,000 translation requests from tetun.org, a specialized MT service for the Tetun language in Timor-Leste, examining user patterns, device types, translation directions, and domains.

**Key findings**:
- Users, many of them students on mobile devices, typically translate from high-resource languages into Tetun
- Translation spans diverse domains including science, healthcare, and daily life
- Available Tetun corpora are dominated by news articles covering government and social issues, contrasting with actual user needs
- MT systems for institutionalized minority languages should prioritize accuracy on domains relevant to educational contexts

**Limitations**: Not stated in abstract

### Talwar and Laasri (2025)

**Research question**: How can Hindi be used as a pivot language to improve Nepali-to-English translation in the absence of large parallel corpora?

**Methodology**: The paper uses two approaches: the Transfer Method (fully supervised) and Backtranslation (semi-supervised) to translate Nepali into English using Hindi as a pivot language.

**Key findings**:
- Using Hindi as a pivot language achieves a SacreBLEU score of 14.2 with the Transfer Method
- The Transfer Method improves the baseline by 6.6 points compared to Guzman et al. (2019)
- The semi-supervised Backtranslation approach underperforms compared to the baseline score of 15.1
- Hindi is identified as a suitable pivot language for Nepali-English translation

**Limitations**: The semi-supervised approach underperformed compared to the baseline, and the paper discusses potential causes but suggests scope for future work.

### Borisov et al. (2025)

**Research question**: How can machine translation be built for the code-switched Kazakh-Russian language pair without labeled data?

**Methodology**: The method generates synthetic data to build a machine translation model and presents the first code-switching Kazakh-Russian parallel corpus.

**Key findings**:
- A translation model was built with no labeled data using synthetic data generation
- The model achieves 16.48 BLEU score
- The model almost reaches the performance of an existing commercial system
- Human evaluation shows the model beats the commercial system
- The first code-switching Kazakh-Russian parallel corpus was created

**Limitations**: Not stated in abstract

### Thakkar et al. (2026)

**Research question**: How can linguistically enriched parallel datasets improve low-resource neural machine translation for English-Marathi?

**Methodology**: The paper presents BhashaSetu, a 2.78 million sentence pair dataset from diverse domains with stemmed and lemmatized representations, and benchmarks multiple translation models including parameter-efficient fine-tuning of NLLB-200 using LoRA.

**Key findings**:
- Corpus-level deduplication is the single largest preprocessing contributor to downstream quality
- Removing deduplication reduces performance by 1.17 BLEU and 2.21 chrF++
- The dataset comprises 2.78 million sentence pairs from news, politics, healthcare, literature, and culture domains
- Disciplined cross-source corpus hygiene is a low-cost, high-impact intervention for low-resource languages
- The dataset is publicly released for reproducible research

**Limitations**: Not stated in abstract

### Merx et al. (2025)

**Research question**: How can terminology-aware translation be made accessible to non-technical users for low-resource languages without requiring model fine-tuning?

**Methodology**: TULUN combines neural machine translation with LLM-based post-editing guided by existing glossaries and translation memories, implemented as an open-source web-based platform for collaborative human-machine translation.

**Key findings**:
- TULUN achieves improvements of 16.90-22.41 ChrF++ points on medical and disaster relief translation for Tetun and Bislama
- Across six low-resource languages on FLORES dataset, TULUN outperforms standalone MT and LLM approaches
- Average improvement of 2.8 ChrF points over NLLB-54B
- The platform enables users to create, edit, and leverage terminology resources without model fine-tuning
- The approach fosters collaborative human-machine translation while respecting domain expertise

**Limitations**: Not stated in abstract

### Gritta et al. (2026)

**Research question**: How can high-quality parallel data be scaled for African languages to develop competitive small language models for machine translation?

**Methodology**: The paper introduces TranslatePsy-AfriSLM, a collection of MT resources for 19 Sub-Saharan African languages including curated parallel data, African-specialized synthetic data, and fine-tuned SLMs, using unified quality-estimation filtering.

**Key findings**:
- Unified quality-estimation filtering removes up to 96% of training tokens without degrading quality
- Filtered synthetic data dominates the quality-efficiency Pareto frontier
- TranslatePsy-AfriSLMs outperform larger systems including TranslateGemma-27B and Qwen3.5-122B-A10B
- Competitive performance achieved with as few as 0.8B parameters
- The resources cover 19 Sub-Saharan African languages

**Limitations**: Not stated in abstract

## References

Attia, A., & Aji, A. F. (2026). Improving low-resource machine translation via round-trip reinforcement learning. arXiv. https://arxiv.org/abs/2601.12535

Borisov, M., Kozhirbayev, Z., & Malykh, V. (2025). Low-resource machine translation for code-switched Kazakh-Russian language pair. arXiv. https://arxiv.org/abs/2503.20007

Boujkian, S. (2024). Improving low-resource machine translation via cross-linguistic transfer from typologically similar high-resource languages. arXiv. https://arxiv.org/abs/2501.00045

Gritta, M., Lambert, P., Back, J., & Nazir, A. (2026). TranslatePsy-AfriSLM: High-quality data scaling for low-resource machine translation. arXiv. https://arxiv.org/abs/2608.18655

Merx, R., Correia, A. J. G., Suominen, H., & Vylomova, E. (2024). Low-resource machine translation: What for? Who for? An observational study on a dedicated Tetun language translation service. arXiv. https://arxiv.org/abs/2411.12262

Merx, R., Suominen, H., Hong, L., Thieberger, N., Cohn, T., & Vylomova, E. (2025). TULUN: Transparent and adaptable low-resource machine translation. arXiv. https://arxiv.org/abs/2505.18683

Nguepi Nguefack, I., Finkelstein, M., & Sakayo, T. S. (2025). Pretraining strategies using monolingual and parallel data for low-resource machine translation. arXiv. https://arxiv.org/abs/2510.25116

Salim, L. F., Carlin, E., Morinvil, A., Ai, X., & Ku, L.-W. (2026). Beyond many-shot translation: Scaling in-context demonstrations for low-resource machine translation. arXiv. https://arxiv.org/abs/2602.04764

Talwar, A., & Laasri, J. (2025). Pivot language for low-resource machine translation. arXiv. https://arxiv.org/abs/2505.14553

Thakkar, P., Yadav, A., Tiemann, M., Mehta, A., Bhasin, A., & Khedkar, S. (2026). BhashaSetu: A data-centric approach to low-resource machine translation. arXiv. https://arxiv.org/abs/2605.27050
