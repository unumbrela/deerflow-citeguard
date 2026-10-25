# Systematic Literature Review: Low-Resource Machine Translation

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "low-resource machine translation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of low-resource machine translation has seen significant advances in the past two years, with research focusing on data-centric approaches, transfer learning strategies, and innovative training methodologies. The surveyed literature reveals a strong emphasis on leveraging typologically similar languages, pivot languages, and synthetic data generation to overcome the scarcity of parallel training data. Recent work demonstrates that quality improvements can be achieved through round-trip reinforcement learning, cross-linguistic transfer, and terminology-aware post-editing without requiring model fine-tuning. A notable trend is the shift toward community-driven translation services that prioritize actual user needs over corpus availability, particularly for underrepresented languages in Africa and Southeast Asia.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "low-resource machine translation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Data-Centric Approaches and Corpus Quality

A dominant theme across the surveyed literature is the recognition that data quality and curation are as critical as model architecture improvements. Several papers emphasize that disciplined corpus hygiene and strategic data selection can yield substantial performance gains without requiring architectural innovations.

Thakkar et al. (2026) demonstrate that corpus-level deduplication is the single largest preprocessing contributor to downstream translation quality, with removal of deduplication reducing performance by 1.17 BLEU and 2.21 chrF++ points. Their BhashaSetu dataset comprises 2.78 million sentence pairs across diverse domains including news, politics, healthcare, literature, and culture for English-Marathi translation.

Similarly, Gritta et al. (2026) introduce unified quality-estimation filtering that removes up to 96% of training tokens without degrading quality for 19 Sub-Saharan African languages. Their filtered synthetic data dominates the quality-efficiency Pareto frontier, enabling small language models (as few as 0.8B parameters) to outperform larger systems including TranslateGemma-27B and Qwen3.5-122B-A10B.

Nguepi Nguefack et al. (2025) further support this theme by showing that pretraining on multiple languages using both monolingual and parallel data significantly enhances translation quality, helping bridge the performance gap between high-resource and low-resource languages.

### Theme 2: Transfer Learning and Cross-Linguistic Strategies

Transfer learning from high-resource to low-resource languages emerges as a consistently effective strategy across multiple studies. The key insight is that linguistic similarity can enable efficient adaptation, reducing the need for extensive training data.

Boujkian (2024) conducted experiments on five typologically diverse language pairs (Semitic, Bantu, Romance, Slavic, and language isolate), finding that transfer learning consistently improves translation quality across all language pairs, including beyond closely related languages. The study reveals that moderate batch sizes (e.g., 32) are often optimal for similar language pairs, while smaller batch sizes benefit less similar language pairs.

Talwar and Laasri (2025) explore the use of Hindi as a pivot language for Nepali-to-English translation, achieving a SacreBLEU score of 14.2 on the devtest set. Their Transfer Method improves the baseline fully supervised score by 6.6 points, demonstrating that strategically chosen pivot languages can serve as effective bridges between low-resource and high-resource languages.

Borisov et al. (2025) extend this approach to code-switched language pairs, presenting the first code-switching Kazakh-Russian parallel corpus and achieving 16.48 BLEU score using synthetic data generation without labeled data.

### Theme 3: Self-Supervised and Reinforcement Learning Methods

Recent work demonstrates the potential of self-supervised approaches that do not require additional labeled data for improvement. These methods leverage the model's own outputs to create training signals.

Attia and Aji (2026) introduce round-trip reinforcement learning fine-tuning with NLLB models (600M and 1.3B parameters), translating English to target languages and back, using chrF++ and BLEU as reward functions on reconstructed English sentences. Their method shows consistent improvements across Central Aymara, Friulian, Wolof, Dyula, Bhojpuri and Russian, with qualitative analysis showing increased fluency and semantic fidelity in translation outputs. The method benefits from model scale, enabling continued self-improvement.

### Theme 4: In-Context Learning and Scaling Strategies

The application of in-context learning to low-resource translation reveals both opportunities and limitations in scaling approaches.

Salim et al. (2026) scale in-context token budget to 1M tokens on Javanese and Sundanese, comparing monolingual unsupervised data, instruction-style data, and parallel data. Their findings challenge simple scaling assumptions: gains from additional context saturate quickly and can degrade near maximum context window. The scaling behavior is strongly dependent on corpus type, with some forms of monolingual supervision being competitive with parallel data. Larger context windows do not necessarily yield proportional quality gains.

### Theme 5: User-Centric and Community-Driven Translation

A critical theme emerging from recent literature is the importance of aligning translation systems with actual community needs rather than corpus availability.

Merx et al. (2024) conducted an observational study analyzing 100,000 translation requests from tetun.org, a specialized MT service for Tetun language in Timor-Leste. They found that users, many students on mobile devices, typically translate from high-resource languages into Tetun, with translation domains including science, healthcare, and daily life—not just news. However, available Tetun corpora are dominated by news articles on government and social issues, mismatching user needs. The study recommends that MT systems should prioritize accuracy on educational domain content in the high-resource to low-resource direction.

Building on this user-centric approach, Merx et al. (2025) propose Tulun, combining neural MT with LLM-based post-editing guided by glossaries and translation memories. On medical and disaster relief translation for Tetun and Bislama, the system achieves 16.90-22.41 ChrF++ improvements over baseline MT. Across six low-resource languages on FLORES dataset, Tulun outperforms both standalone MT and LLM approaches, achieving an average improvement of 2.8 ChrF points over NLLB-54B. The platform enables collaborative human-machine translation without requiring model fine-tuning.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. Multiple studies converge on the finding that data quality and curation are paramount—Thakkar et al. (2026), Gritta et al. (2026), and Nguepi Nguefack et al. (2025) all demonstrate that careful data selection and preprocessing yield substantial improvements. There is also consensus that transfer learning from high-resource languages consistently improves translation quality across diverse language families (Boujkian, 2024; Talwar & Laasri, 2025). Additionally, multiple papers agree that user needs should drive system design rather than corpus availability (Merx et al., 2024; Merx et al., 2025).

**Disagreements**: The literature reveals tension around scaling strategies. While Attia and Aji (2026) find that their reinforcement learning method benefits from model scale, enabling continued self-improvement, Salim et al. (2026) caution that larger context windows do not necessarily yield proportional quality gains and can even degrade performance near maximum context limits. This suggests that the relationship between scale and performance is more nuanced than simple "bigger is better" assumptions. Additionally, while Talwar and Laasri (2025) achieve improvements using pivot languages, their approach performs slightly below semi-supervised baselines, suggesting that pivot language strategies may be context-dependent rather than universally superior.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Limited explicit limitations reporting**: Most surveyed papers do not explicitly state limitations in their abstracts, making it difficult to assess the boundaries of applicability for proposed methods.

2. **Evaluation beyond BLEU and chrF++**: While multiple metrics are used, there is limited discussion of human evaluation methodologies and real-world deployment challenges beyond controlled experimental settings.

3. **Long-term maintenance and sustainability**: The user-centric studies (Merx et al., 2024; Merx et al., 2025) raise questions about how translation services can be sustainably maintained for low-resource languages, but concrete solutions for long-term support are not addressed.

4. **Cross-domain generalization**: While several papers demonstrate improvements on specific language pairs or domains, there is limited systematic investigation of how methods generalize across different domains within the same language.

5. **Resource efficiency trade-offs**: While Gritta et al. (2026) demonstrate that small models can outperform larger systems, the broader literature lacks systematic analysis of computational costs versus quality trade-offs across different approaches.

## Per-Paper Annotations

### Attia and Aji (2026)

**Research question**: Can self-supervised reinforcement learning with round-trip bootstrapping improve translation quality in low-resource language settings?

**Methodology**: The study uses round-trip reinforcement learning fine-tuning with NLLB models (600M and 1.3B parameters), translating English to target languages and back, using chrF++ and BLEU as reward functions on reconstructed English sentences.

**Key findings**:
- Consistent improvements observed across Central Aymara, Friulian, Wolof, Dyula, Bhojpuri and Russian
- Qualitative analysis shows increased fluency and semantic fidelity in translation outputs
- The method benefits from model scale, enabling continued self-improvement

**Limitations**: Not stated in abstract

### Boujkian (2024)

**Research question**: Does linguistic similarity enable efficient adaptation in transfer learning for low-resource machine translation, reducing the need for extensive training data?

**Methodology**: Experiments conducted on five typologically diverse language pairs (Semitic, Bantu, Romance, Slavic, and language isolate) with hyperparameter variation including learning rate, batch size, epochs, and weight decay.

**Key findings**:
- Transfer learning consistently improves translation quality across all language pairs, including beyond closely related languages
- Moderate batch sizes (e.g., 32) are often optimal for similar language pairs
- Smaller batch sizes benefit less similar language pairs
- Excessively high learning rates can destabilize training

**Limitations**: Not stated in abstract

### Borisov, Kozhirbayev, and Malykh (2025)

**Research question**: How can machine translation be built for code-switched Kazakh-Russian language pairs without labeled data?

**Methodology**: The paper proposes a method using synthetic data generation to build a machine translation model for code-switched Kazakh-Russian without labeled data, and presents the first code-switching Kazakh-Russian parallel corpus.

**Key findings**:
- The proposed method achieves 16.48 BLEU score
- The model almost reaches an existing commercial system's performance
- Human evaluation shows the model beats the commercial system
- The first code-switching Kazakh-Russian parallel corpus is presented

**Limitations**: Not stated in abstract

### Gritta, Lambert, Back, and Nazir (2026)

**Research question**: How can high-quality parallel data and small language models be scaled for underrepresented African languages?

**Methodology**: The paper introduces TranslatePsy-AfriSLM, a collection of MT resources for 19 Sub-Saharan African languages including curated parallel data, African-specialized synthetic data, and fine-tuned SLMs, using unified quality-estimation filtering.

**Key findings**:
- Unified quality-estimation filtering removes up to 96% of training tokens without degrading quality
- Filtered synthetic data dominates the quality-efficiency Pareto frontier
- TranslatePsy-AfriSLMs outperform larger systems including TranslateGemma-27B and Qwen3.5-122B-A10B with as few as 0.8B parameters
- The collection addresses the digital divide limiting AI adoption on the African continent

**Limitations**: Not stated in abstract

### Merx, Correia, Suominen, and Vylomova (2024)

**Research question**: What are the actual community needs and usage patterns for low-resource machine translation, specifically for the Tetun language?

**Methodology**: Observational study analyzing 100,000 translation requests from tetun.org, a specialized MT service for Tetun language in Timor-Leste, comparing usage patterns with existing corpus assumptions.

**Key findings**:
- Users, many students on mobile devices, typically translate from high-resource languages into Tetun
- Translation domains include science, healthcare, and daily life, not just news
- Available Tetun corpora are dominated by news articles on government and social issues, mismatching user needs
- MT systems should prioritize accuracy on educational domain content in high-resource to low-resource direction

**Limitations**: Not stated in abstract

### Merx, Suominen, Hong, Thieberger, Cohn, and Vylomova (2025)

**Research question**: How can terminology-aware translation be achieved for low-resource languages without requiring model fine-tuning?

**Methodology**: The paper proposes Tulun, combining neural MT with LLM-based post-editing guided by glossaries and translation memories, implemented as an open-source web-based platform enabling users to create and leverage terminology resources.

**Key findings**:
- On medical and disaster relief translation for Tetun and Bislama, the system achieves 16.90-22.41 ChrF++ improvements over baseline MT
- Across six low-resource languages on FLORES dataset, Tulun outperforms both standalone MT and LLM approaches
- Tulun achieves an average improvement of 2.8 ChrF points over NLLB-54B
- The platform enables collaborative human-machine translation without requiring model fine-tuning

**Limitations**: Not stated in abstract

### Nguepi Nguefack, Finkelstein, and Sakayo (2025)

**Research question**: What pretraining strategies are most effective for developing machine translation models for low-resource languages?

**Methodology**: Comprehensive experiments exploring different pretraining methodologies including integration of multiple languages and use of both monolingual and parallel data during pretraining, building on Reid and Artetxe (2021) approach for Lingala.

**Key findings**:
- Pretraining on multiple languages significantly enhances translation quality
- Leveraging both monolingual and parallel data during pretraining improves performance
- The approach helps bridge the performance gap between high-resource and low-resource languages

**Limitations**: Not stated in abstract

### Salim, Carlin, Morinvil, Ai, and Ku (2026)

**Research question**: Can scaling in-context learning beyond few-shot to thousands of examples with long-context models improve low-resource machine translation?

**Methodology**: Study scales in-context token budget to 1M tokens on Javanese and Sundanese, comparing three corpus types: monolingual unsupervised data, instruction-style data, and parallel data (English-target and Indonesian-target).

**Key findings**:
- Gains from additional context saturate quickly and can degrade near maximum context window
- Scaling behavior is strongly dependent on corpus type
- Some forms of monolingual supervision can be competitive with parallel data
- Larger context windows do not necessarily yield proportional quality gains

**Limitations**: Not stated in abstract

### Talwar and Laasri (2025)

**Research question**: How can Hindi be used as a pivot language to improve Nepali-to-English translation in low-resource settings?

**Methodology**: The paper uses two approaches: the Transfer Method (fully supervised) and Backtranslation (semi-supervised) to translate Nepali into English using Hindi as a pivot language.

**Key findings**:
- Using Hindi as a pivot language achieves a SacreBLEU score of 14.2 on devtest set
- The Transfer Method improves the baseline fully supervised score by 6.6 points
- The approach performs slightly below the semi-supervised baseline score of 15.1
- Hindi is identified as a good candidate for pivot language in this translation pair

**Limitations**: The paper acknowledges under-performance compared to semi-supervised baseline and discusses potential causes, with scope identified for future work.

### Thakkar, Yadav, Tiemann, Mehta, Bhasin, and Khedkar (2026)

**Research question**: How can a linguistically enriched parallel dataset improve English-Marathi neural machine translation in low-resource settings?

**Methodology**: The paper presents BhashaSetu, a 2.78 million sentence pair English-Marathi dataset from heterogeneous sources with stemmed and lemmatized representations, benchmarked using multiple translation models and parameter-efficient fine-tuning of NLLB-200-distilled-600M using LoRA.

**Key findings**:
- The dataset comprises 2.78 million sentence pairs across diverse domains including news, politics, healthcare, literature, and culture
- Corpus-level deduplication is the single largest preprocessing contributor to downstream quality
- Removing deduplication reduces performance by 1.17 BLEU and 2.21 chrF++
- Disciplined cross-source corpus hygiene is a low-cost, high-impact intervention for low-resource, morphologically rich languages

**Limitations**: Not stated in abstract

## References

Attia, A., & Aji, A. F. (2026). Improving low-resource machine translation via round-trip reinforcement learning. arXiv. https://arxiv.org/abs/2601.12535

Borisov, M., Kozhirbayev, Z., & Malykh, V. (2025). Low-resource machine translation for code-switched Kazakh-Russian language pair. arXiv. https://arxiv.org/abs/2503.20007

Boujkian, S. (2024). Improving low-resource machine translation via cross-linguistic transfer from typologically similar high-resource languages. arXiv. https://arxiv.org/abs/2501.00045

Gritta, M., Lambert, P., Back, J., & Nazir, A. (2026). TranslatePsy-AfriSLM: High-quality data scaling for low-resource machine translation. arXiv. https://arxiv.org/abs/2608.18655

Merx, R., Correia, A. J. G., Suominen, H., & Vylomova, E. (2024). Low-resource machine translation: what for? who for? An observational study on a dedicated Tetun language translation service. arXiv. https://arxiv.org/abs/2411.12262

Merx, R., Suominen, H., Hong, L., Thieberger, N., Cohn, T., & Vylomova, E. (2025). TULUN: Transparent and adaptable low-resource machine translation. arXiv. https://arxiv.org/abs/2505.18683

Nguepi Nguefack, I., Finkelstein, M., & Sakayo, T. S. (2025). Pretraining strategies using monolingual and parallel data for low-resource machine translation. arXiv. https://arxiv.org/abs/2510.25116

Salim, L. F., Carlin, E., Morinvil, A., Ai, X., & Ku, L.-W. (2026). Beyond many-shot translation: Scaling in-context demonstrations for low-resource machine translation. arXiv. https://arxiv.org/abs/2602.04764

Talwar, A., & Laasri, J. (2025). Pivot language for low-resource machine translation. arXiv. https://arxiv.org/abs/2505.14553

Thakkar, P., Yadav, A., Tiemann, M., Mehta, A., Bhasin, A., & Khedkar, S. (2026). BhashaSetu: A data-centric approach to low-resource machine translation. arXiv. https://arxiv.org/abs/2605.27050
