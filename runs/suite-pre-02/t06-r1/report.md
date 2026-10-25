# Systematic Literature Review: Low-Resource Machine Translation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "low-resource machine translation" query, cs.CL category, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Low-resource machine translation has emerged as a critical research area addressing the needs of billions of speakers of under-resourced languages. The surveyed literature from 2024-2026 reveals a field rapidly evolving through multiple complementary approaches: leveraging large language models for knowledge distillation, developing novel pretraining strategies with monolingual and parallel data, exploring cross-linguistic transfer from typologically similar languages, and implementing innovative reinforcement learning techniques. A significant shift toward data-centric approaches emphasizes corpus quality, deduplication, and domain alignment with actual user needs. Recent work demonstrates that larger context windows and more data do not automatically yield proportional gains, highlighting the importance of strategic data selection and corpus hygiene over brute-force scaling.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "low-resource machine translation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Large Language Models as Enablers for Low-Resource MT

The emergence of powerful large language models has transformed low-resource machine translation by providing new pathways for knowledge transfer and synthetic data generation. Enis & Hopkins (2024) demonstrated that Claude 3 Opus exhibits superior translation competence and remarkable resource efficiency compared to other LLMs, with translation quality less dependent on language pair resource levels. Their work showed that LLM translation capabilities can be distilled into traditional NMT models, advancing state-of-the-art in Yoruba-English translation to meet or surpass NLLB-54B and Google Translate. This theme reflects a broader trend of leveraging LLMs not just as direct translation systems but as knowledge sources for training specialized models.

The in-context learning paradigm offers another avenue for adapting LLMs to low-resource settings. Salim et al. (2026) explored scaling in-context demonstrations to thousands of examples with 1M token context windows, revealing that gains saturate quickly and can degrade near maximum context capacity. Their experiments on Javanese and Sundanese showed that some forms of monolingual supervision can be competitive with parallel data, challenging assumptions about the necessity of explicit translation pairs. This work characterizes the effective limits of long-context ICL, highlighting that larger context windows do not necessarily yield proportional quality gains.

### Theme 2: Pretraining and Transfer Learning Strategies

A substantial body of recent work focuses on effective pretraining strategies that leverage available data more efficiently. Nguepi Nguefack et al. (2025) examined pretraining methodologies for Lingala, an under-resourced African language, finding that pretraining on multiple languages and leveraging both monolingual and parallel data significantly enhances translation quality. Their approach builds on methods originally designed for high-resource languages but adapts them to bridge the performance gap for marginalized communities.

Cross-linguistic transfer from typologically similar high-resource languages represents another promising direction. Boujkian (2024) conducted experiments across five typologically diverse language pairs spanning Semitic, Bantu, Romance, Slavic, and language isolate families, demonstrating that transfer learning consistently improves translation quality beyond closely related languages. The study provided practical guidance on hyperparameter tuning, finding that moderate batch sizes optimize similar pairs while smaller sizes benefit less similar pairs, and excessively high learning rates destabilize training.

### Theme 3: Reinforcement Learning and Self-Supervised Approaches

Reinforcement learning has emerged as a powerful technique for improving low-resource MT without requiring additional labeled data. Attia & Aji (2026) investigated self-supervised reinforcement learning fine-tuning using round-trip bootstrapping with NLLB models, translating English to target low-resource languages and back while using chrF++ and BLEU as reward functions. Their approach yielded consistent improvements across Central Aymara, Friulian, Wolof, Dyula, Bhojpuri, and Russian, with qualitative inspection showing increased fluency and semantic fidelity. The method's scalability suggests models can increasingly leverage pretrained knowledge for continued self-improvement.

### Theme 4: Pivot Languages and Synthetic Data Generation

When direct parallel corpora are unavailable, pivot languages and synthetic data generation offer viable alternatives. Talwar & Laasri (2025) used Hindi as a pivot language to translate Nepali into English, comparing the Transfer Method (fully supervised) and Backtranslation (semi-supervised). Their Transfer Method achieved a SacreBLEU score of 14.2, improving the baseline by 6.6 points, though slightly below semi-supervised baselines. Borisov et al. (2025) tackled the even more challenging code-switched Kazakh-Russian language pair with no labeled data, proposing synthetic data generation that achieved 16.48 BLEU, nearly reaching commercial system performance and beating it in human evaluation.

### Theme 5: Data-Centric Approaches and Corpus Quality

A significant shift toward data-centric approaches emphasizes that corpus quality and hygiene can be more impactful than model architecture changes. Thakkar et al. (2026) presented BhashaSetu, a linguistically enriched English-Marathi parallel dataset of 2.78 million sentence pairs with stemmed and lemmatized representations. Their ablation study revealed corpus-level deduplication as the single largest preprocessing contributor to downstream quality, with removal reducing performance by 1.17 BLEU and 2.21 chrF++. This demonstrates that disciplined cross-source corpus hygiene is a low-cost, high-impact intervention for low-resource, morphologically rich languages.

### Theme 6: Community Needs and Usage-Driven Development

Understanding actual community needs has emerged as critical for effective low-resource MT development. Merx et al. (2024) conducted an observational study of 100,000 translation requests from tetun.org, revealing patterns that challenge assumptions based on existing corpora. Users, predominantly students on mobile devices, typically translate from high-resource languages into Tetun across diverse domains including science, healthcare, and daily life, contrasting sharply with available corpora dominated by news articles. This work demonstrates that MT systems for institutionalized minority languages should prioritize accuracy on domains relevant to educational contexts, grounding research in practical community needs rather than researcher assumptions.

### Theme 7: Federated Learning and Interpretability

Federated learning approaches offer new possibilities for leveraging heterogeneous data while maintaining interpretability. Moskvoretskii et al. (2024) presented MeritOpt, based on Personalized Federated Learning, evaluated on South East Asian and Finno-Ugric languages. Their approach is highly interpretable, tracking the impact of each language used for training, revealing that target dataset size affects weight distribution across auxiliary languages, unrelated languages do not interfere with training, and auxiliary optimizer parameters have minimal impact. The method's ease of application with a few lines of code makes it accessible for practical deployment.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key findings. First, multiple papers demonstrate that strategic data use outperforms brute-force scaling—whether through deduplication (Thakkar et al., 2026), typologically-informed transfer (Boujkian, 2024), or domain alignment with user needs (Merx et al., 2024). Second, there is consensus that LLMs and large pre-trained models provide valuable foundations for low-resource MT, whether through direct use (Enis & Hopkins, 2024), knowledge distillation (Enis & Hopkins, 2024), or as starting points for fine-tuning (Attia & Aji, 2026; Nguepi Nguefack et al., 2025). Third, multiple studies confirm that monolingual data and synthetic data can be competitive with or substitute for parallel data in various contexts (Salim et al., 2026; Borisov et al., 2025).

**Disagreements**: The literature shows some tension around optimal scaling strategies. While Salim et al. (2026) found that context scaling saturates quickly and can degrade performance, Attia & Aji (2026) argue their method benefits from scale, enabling models to leverage pretrained knowledge for continued improvement. This apparent disagreement may reflect different scaling dimensions—context window size versus model size and training iterations. Additionally, Talwar & Laasri (2025) found their pivot language approach underperformed semi-supervised baselines, while Borisov et al. (2025) achieved near-commercial performance with synthetic data, suggesting pivot language effectiveness may depend heavily on specific language relationships and data availability.

## Gaps and Open Questions

The collective literature reveals several critical gaps. First, evaluation remains limited to specific language families—South East Asian, Finno-Ugric, African languages, and European languages dominate, with limited representation from other language families. Second, most studies focus on translation into or from English, with limited work on direct low-resource-to-low-resource translation. Third, the observational study by Merx et al. (2024) highlights a significant gap between available corpora and actual user needs, suggesting many low-resource MT systems may be optimized for the wrong use cases. Fourth, while several papers note the importance of domain alignment, systematic methods for identifying and prioritizing domains based on community needs remain underdeveloped. Finally, the reproducibility challenge noted by Nguepi Nguefack et al. (2025)—where datasets may become inaccessible due to changes in public availability—points to a broader need for sustainable, maintained resources for low-resource language communities.

## Per-Paper Annotations

### Attia & Aji (2026)

**Research question**: Can self-supervised reinforcement learning fine-tuning with round-trip bootstrapping improve low-resource machine translation performance?
**Methodology**: The authors investigate round-trip bootstrapping with NLLB models, translating English to target low-resource languages and back, using a combination of chrF++ and BLEU as the reward function on reconstructed English sentences.
**Key findings**:
- Consistent improvements observed across Central Aymara, Friulian, Wolof, Dyula, Bhojpuri, and Russian
- Qualitative inspection shows increased fluency and semantic fidelity in translation outputs
- Both 600M and 1.3B parameter NLLB models benefit from the approach
- The method can further benefit from scale, enabling models to leverage pretrained knowledge
- Self-improvement through round-trip reinforcement learning is feasible in low-resource settings
**Limitations**: The approach is evaluated on only 6 specific languages and relies on the NLLB family of models. The qualitative improvements noted may not fully correlate with quantitative metric gains across all language pairs.

### Borisov, Kozhirbayev, & Malykh (2025)

**Research question**: How can machine translation models be built for code-switched low-resource language pairs when no labeled training data exists?
**Methodology**: The authors propose a method based on synthetic data generation to build an MT model for code-switched Kazakh-Russian without labeled data, and present the first code-switching Kazakh-Russian parallel corpus for evaluation.
**Key findings**:
- The model achieved 16.48 BLEU score on the code-switched translation task
- Performance nearly reaches that of an existing commercial system
- The model beats the commercial system in human evaluation
- First code-switching Kazakh-Russian parallel corpus was created and released
- Synthetic data generation is viable for code-switched low-resource MT without labeled data
**Limitations**: Relies entirely on synthetic data generation which may not capture all natural code-switching patterns; evaluation scope is limited to the created corpus.

### Boujkian (2024)

**Research question**: Does transfer learning from typologically similar high-resource languages improve low-resource machine translation when limited target language data is available?
**Methodology**: The author conducts experiments on five typologically diverse language pairs (Semitic, Bantu, Romance, Slavic, and a language isolate), fine-tuning models initially trained on typologically similar high-resource languages with limited target language data, while varying key hyperparameters.
**Key findings**:
- Transfer learning consistently improves translation quality across all five language pairs
- The approach is applicable beyond closely related languages, confirming generalizability across language families
- Moderate batch sizes (e.g., 32) are often optimal for typologically similar pairs
- Smaller batch sizes benefit less similar language pairs
- Excessively high learning rates can destabilize training
**Limitations**: Only five language pairs were tested, which may not represent all possible language family combinations. While minimal tuning is required, some hyperparameter optimization is still necessary to achieve optimal results for different language pair characteristics.

### Enis & Hopkins (2024)

**Research question**: Can Claude 3 Opus outperform other LLMs for low-resource machine translation, and can its translation knowledge be distilled into traditional NMT models?
**Methodology**: The authors evaluate Claude 3 Opus on curated benchmarks to assess translation competence and resource efficiency, then use Claude to generate synthetic data for knowledge distillation into NMT models, specifically tested on Yoruba-English translation.
**Key findings**:
- Claude 3 Opus exhibits stronger machine translation competence than other LLMs
- Claude demonstrates remarkable resource efficiency, with translation quality less dependent on language pair resource levels
- Knowledge distillation from Claude advances state-of-the-art in Yoruba-English translation
- The distilled NMT model meets or surpasses strong baselines including NLLB-54B and Google Translate
- LLM translation advancements can be successfully compressed into traditional NMT architectures
**Limitations**: Evidence of data contamination was found on FLORES-200 benchmark, requiring curation of new benchmarks. The study focuses primarily on translation into English, and Yoruba-English represents only one language pair for knowledge distillation validation.

### Merx, Correia, Suominen, & Vylomova (2024)

**Research question**: What are the actual usage patterns and community needs for low-resource machine translation services, and how do they differ from assumptions based on existing corpora?
**Methodology**: The authors conducted an observational study analyzing 100,000 translation requests from tetun.org, a specialized MT service for Tetun (the lingua franca in Timor-Leste), examining actual usage patterns rather than relying on surveys or focus groups.
**Key findings**:
- Users, predominantly students on mobile devices, typically translate from high-resource languages into Tetun (not the reverse)
- Translation requests span diverse domains including science, healthcare, and daily life
- Available Tetun corpora are dominated by news articles covering government and social issues, creating a mismatch with actual user needs
- MT systems for institutionalized minority languages should prioritize accuracy on domains relevant to educational contexts
- Observational analysis of actual usage better informs low-resource language technology development than surveys alone
**Limitations**: Study focuses on a single language (Tetun) and one platform (tetun.org); findings may not generalize to all low-resource language communities.

### Moskvoretskii, Tupitsa, Biemann, Horváth, Gorbunov, & Nikishina (2024)

**Research question**: How can Personalized Federated Learning be applied to improve low-resource machine translation with heterogeneous data?
**Methodology**: The authors present MeritOpt, a new approach based on the Personalized Federated Learning algorithm MeritFed, evaluated on low-resource machine translation tasks using datasets from South East Asian and Finno-Ugric languages.
**Key findings**:
- Target dataset size affects weight distribution across auxiliary languages
- Unrelated languages do not interfere with the training process
- Auxiliary optimizer parameters have minimal impact on performance
- The approach is highly interpretable, allowing tracking of each language's impact on training
- MeritOpt is easy to apply with just a few lines of code
**Limitations**: Evaluation is limited to South East Asian and Finno-Ugric language families, which may not generalize to other typologically distinct languages. The approach's effectiveness across broader language families remains untested.

### Nguepi Nguefack, Finkelstein, & Sakayo (2025)

**Research question**: What pretraining strategies are most effective for developing machine translation models tailored to low-resource languages?
**Methodology**: Building on the pretraining approach by Reid and Artetxe (2021), the authors explore different pretraining methodologies including integration of multiple languages and use of both monolingual and parallel data, with the translation model specifically developed for Lingala.
**Key findings**:
- Pretraining on multiple languages significantly enhances translation quality
- Leveraging both monolingual and parallel data during pretraining improves performance
- The approach helps bridge the performance gap between high-resource and low-resource languages
- The methodology contributes to developing more inclusive NLP models for marginalized communities
- Results offer practical insights for effective pretraining strategies in low-resource settings
**Limitations**: The translation model is specifically developed for Lingala, limiting generalizability claims to other low-resource languages. Some datasets used may no longer be accessible due to changes in public availability, affecting reproducibility. The approach builds on a method originally designed for high-resource languages.

### Salim, Carlin, Morinvil, Ai, & Ku (2026)

**Research question**: How can in-context learning be effectively scaled beyond few-shot settings to thousands of examples for low-resource machine translation using long-context models?
**Methodology**: The authors scale in-context token budget to 1M tokens and compare three types of training corpora used as in-context supervision: monolingual unsupervised data, instruction-style data, and parallel data (English-target and Indonesian-target), experimenting on Javanese and Sundanese languages.
**Key findings**:
- Gains from additional context saturate quickly rather than continuing to improve with more examples
- Performance can degrade near the maximum context window (1M tokens)
- Scaling behavior is strongly dependent on corpus type
- Some forms of monolingual supervision can be competitive with parallel data despite lacking explicit translation pairs
- Larger context windows do not necessarily yield proportional quality gains
**Limitations**: Study limited to only two languages (Javanese and Sundanese); results characterize effective limits but don't provide solutions for overcoming the saturation problem.

### Talwar & Laasri (2025)

**Research question**: How can pivot languages be leveraged to overcome the lack of large, diverse parallel corpora for low-resource language pairs?
**Methodology**: The authors use Hindi as a pivot language to translate Nepali into English, comparing two approaches: the Transfer Method (fully supervised) and Backtranslation (semi-supervised), and analyze what makes Hindi a suitable pivot candidate.
**Key findings**:
- Transfer Method achieved a devtest SacreBLEU score of 14.2
- This improves the baseline fully supervised score by 6.6 points over prior work (Guzman et al., 2019)
- Hindi serves as an effective pivot due to linguistic and geographical proximity to Nepali
- Performance was slightly below the semi-supervised baseline score of 15.1
- Pivot language approaches offer a viable path when direct parallel corpora are unavailable
**Limitations**: The approach underperformed compared to semi-supervised baselines; the paper acknowledges scope for future work to understand and address this gap.

### Thakkar, Yadav, Tiemann, Mehta, Bhasin, & Khedkar (2026)

**Research question**: How can linguistically enriched, data-centric approaches address persistent data quality limitations in low-resource neural machine translation for morphologically rich languages?
**Methodology**: The authors created BhashaSetu, a 2.78 million sentence-pair English-Marathi parallel dataset from heterogeneous sources with stemmed and lemmatized representations, benchmarked multiple state-of-the-art models, and conducted parameter-efficient fine-tuning of NLLB-200 using LoRA with ablation studies on preprocessing.
**Key findings**:
- Corpus-level deduplication is the single largest preprocessing contributor to downstream quality
- Removing deduplication reduces performance by 1.17 BLEU and 2.21 chrF++
- Disciplined cross-source corpus hygiene is a low-cost, high-impact intervention for low-resource, morphologically rich languages
- Dataset spans diverse domains including news, politics, healthcare, literature, and culture
- Dataset publicly released to promote reproducible and linguistically informed low-resource NMT research
**Limitations**: Focused only on English-Marathi language pair; findings on preprocessing may not fully generalize to other morphologically rich languages without validation.

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
