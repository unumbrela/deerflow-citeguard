# Systematic Literature Review: Multilingual Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "multilingual language models", category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on multilingual large language models from 2024-2026 reveals a field grappling with fundamental questions of representation, equity, and safety. The surveyed papers collectively demonstrate that multilingual LMs do not learn unified interlingua representations but instead organize knowledge around surface-form cues like orthography and tokenization, creating systematic disparities across languages and scripts. Research converges on tokenization as a critical source of inequity, with certain writing systems incurring substantial efficiency penalties. Simultaneously, the field is addressing safety concerns through cross-lingual unlearning methods and auditing bias across languages, revealing that larger models encode stereotypes more strongly and that instruction tuning does not consistently mitigate these issues. The shape of the field reflects a maturation from purely performance-driven research to a more nuanced understanding of the trade-offs between efficiency, fairness, and capability in multilingual systems.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "multilingual language models", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Tokenization and Representation Inequity

A dominant theme across the surveyed literature is the critical role of tokenization in shaping multilingual model behavior and creating systematic inequities. Dixit and Dixit (2026) quantify the "script tax" — the efficiency penalty imposed by tokenizers on certain writing systems — finding that higher-fragmentation orthographies incur a 3.4x increase in token fertility and a 16.5x inference slowdown on identical hardware. This work demonstrates that tokenization is not a neutral preprocessing step but a key source of disparity in multilingual NLP.

Complementing this, Dang et al. (2024) compare subword tokenization (mT5) versus character-level tokenization (ByT5), revealing that tokenization strategy directly influences how morphological knowledge is encoded. Their probing analysis across 17 languages shows that languages with more morphological irregularities benefit disproportionately from higher pre-training data shares, suggesting that tokenization interacts with linguistic structure in non-trivial ways.

Verma et al. (2026) extend this line of inquiry by investigating whether multilingual models organize representations around abstract linguistic structure or surface-form cues. Using the Language Activation Probability Entropy (LAPE) metric and Sparse Autoencoders, they find that orthography dominates: romanization induces near-disjoint representations that align with neither native-script inputs nor English. This surface-form dominance fundamentally challenges the assumption that multilingual LMs learn a unified interlingua, with profound implications for cross-lingual transfer.

### Theme 2: Cross-Lingual Transfer and Performance Factors

Beyond tokenization, researchers are identifying the key factors that drive performance disparities across languages in multilingual models. Bagheri Nezhad et al. (2024) move beyond the well-known impacts of pre-training data quantity and model size to identify token similarity and country similarity as pivotal factors. Their analysis across 204 languages using SHAP values reveals that shared cultural and linguistic contexts facilitate cross-lingual transfer, offering guidance for developing more equitable models for underrepresented languages.

Winata et al. (2024) introduce MINERS, a benchmark for evaluating semantic retrieval capabilities across 200+ languages including extremely low-resource settings. Their finding that retrieval of semantically similar embeddings alone yields competitive performance without fine-tuning suggests that multilingual models do learn meaningful cross-lingual representations, at least for retrieval tasks. This work fills a critical gap in understanding how multilingual LMs perform in challenging cross-lingual and code-switching retrieval scenarios.

Ponce and Etchegoyhen (2025) examine whether in-context learning can substitute for instruction tuning in multilingual settings, where high-quality instruction data remains scarce. Their results indicate a persistent gap between ICL and instruction tuning, motivating further research into bridging this divide for resource-constrained multilingual applications.

### Theme 3: Safety, Bias, and Unlearning in Multilingual Contexts

As multilingual models deploy globally, ensuring their safety and fairness across languages has become a critical research direction. Choi et al. (2024) address a previously overlooked vulnerability: unlearning in one language does not transfer to others, making models susceptible to "low-resource language attacks" where sensitive information remains accessible in less dominant languages. Their adaptive unlearning scheme with language-dependent weights offers a solution, selectively erasing information across languages while maintaining performance.

Rowe et al. (2025) introduce EuroGEST, a dataset for measuring gender-stereotypical reasoning across English and 29 European languages. Their evaluation of 24 models from six families reveals disturbing consistency: across all models and languages, the strongest stereotypes associate women with being "beautiful," "empathetic," and "neat," and men with being "leaders," "strong/tough," and "professional." Critically, larger models encode stereotypes more strongly, and instruction finetuning does not consistently reduce them, challenging assumptions about scaling and alignment as solutions to bias.

### Theme 4: Specialized Multilingual Phenomena

Several papers investigate specialized phenomena unique to multilingual contexts. Xie et al. (2025) examine code-switching — alternating between languages within conversations — finding that pre-training mBERT on Spanglish tweets improves performance on POS tagging, sentiment analysis, NER, and language identification. Their latent analysis reveals more homogeneous English and Spanish embeddings, suggesting that code-switched pre-training can better serve globalized, multilingual contexts.

Loyola et al. (2026) probe the geometry of color representations in multilingual models, asking whether they learn perceptually grounded or primarily linguistic color geometries. Their decomposition into perceptual alignment and cross-lingual symmetry axes reveals that perceptual grounding peaks in intermediate layers then collapses toward output layers, while cross-lingual symmetry degrades with depth. Functionally, models achieve 96.7% accuracy on color classification where perceptual alignment peaks, demonstrating that text-only LMs learn universal color-language geometry rather than universal color-perception geometry.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key findings. First, tokenization is a critical determinant of multilingual model behavior, affecting efficiency, representation geometry, and equity across languages (Dixit & Dixit, 2026; Dang et al., 2024; Verma et al., 2026). Second, multilingual models do not learn unified interlingua representations but instead organize knowledge around surface-form cues, with linguistic abstraction emerging gradually if at all (Verma et al., 2026; Loyola et al., 2026). Third, larger models encode biases and stereotypes more strongly, and standard mitigation strategies like instruction finetuning show inconsistent effectiveness (Rowe et al., 2025). Fourth, cross-lingual transfer is facilitated by token similarity and shared cultural-linguistic contexts, not merely by data quantity (Bagheri Nezhad et al., 2024).

**Disagreements**: The literature shows less direct disagreement but reveals tensions in findings. While Winata et al. (2024) demonstrate that multilingual models achieve competitive semantic retrieval performance across 200+ languages without fine-tuning, suggesting robust cross-lingual representations, Verma et al. (2026) find that representations are strongly conditioned on orthography, with romanization inducing near-disjoint representations. These findings may be reconciled by task differences — retrieval may succeed despite surface-form dominance if the retrieval task itself is surface-form sensitive. Additionally, Ponce and Etchegoyhen (2025) find a persistent gap between ICL and instruction tuning, while Xie et al. (2025) show that targeted pre-training on code-switched data can close performance gaps, suggesting different pathways may have different efficacy depending on the specific multilingual challenge.

## Gaps and Open Questions

The collective literature reveals several critical gaps. First, geographic and linguistic coverage remains limited: EuroGEST covers only European languages (Rowe et al., 2025), morphological probing covers 17 languages (Dang et al., 2024), and code-switching research focuses on Spanglish (Xie et al., 2025). The field lacks comprehensive evaluation across the full spectrum of global linguistic diversity, particularly for African, Asian, and Indigenous languages.

Second, the gap between ICL and instruction tuning in multilingual contexts lacks clear solutions (Ponce & Etchegoyhen, 2025). While the problem is identified, methods to reduce this gap — crucial for resource-constrained multilingual deployment — remain undeveloped.

Third, script-aware tokenization and pretraining solutions are motivated but not yet developed and validated (Dixit & Dixit, 2026). The field has identified tokenization as a source of inequity but lacks actionable remedies.

Fourth, perceptual grounding in text-only models is fundamentally limited (Loyola et al., 2026), raising questions about whether truly grounded multilingual understanding requires multimodal training. This gap is particularly relevant for concepts with strong perceptual components beyond color.

Fifth, cross-lingual unlearning methods need validation across broader model families and language sets (Choi et al., 2024). The current approach shows promise but requires testing for generalizability.

Finally, the field lacks methods to achieve unified interlingua representations despite surface-form dominance (Verma et al., 2026). If true cross-lingual transfer requires abstract representations, new architectural or training innovations are needed.

## Per-Paper Annotations

### Bagheri Nezhad et al. (2024)

**Research question**: What factors beyond pre-training data quantity and model size significantly influence the effectiveness of multilingual language models?
**Methodology**: Analyzed geographical, linguistic, and resource-related features using regression models and SHAP values across 204 languages on the SIB-200 classification dataset and Flores-200 machine translation dataset.
**Key findings**:
- Token similarity and country similarity are pivotal factors alongside pre-train data percentage and model size
- Token similarity facilitates cross-lingual transfer between languages
- Country similarity highlights the importance of shared cultural and linguistic contexts in model performance
- Performance disparities exist due to differences in resource availability and linguistic characteristics across languages
- These insights provide guidance for developing more equitable multilingual models for underrepresented languages
**Limitations**: Analysis is limited to two specific datasets (SIB-200 and Flores-200), and findings may not generalize to other tasks or evaluation benchmarks.

### Choi et al. (2024)

**Research question**: How can we selectively erase sensitive information across different languages in multilingual language models while maintaining overall model performance?
**Methodology**: The paper presents an adaptive unlearning scheme that assigns language-dependent weights to address different language performances of multilingual language models, enabling selective knowledge erasure across languages.
**Key findings**:
- Unlearning in one language does not necessarily transfer to other languages in multilingual models
- Models are vulnerable to low-resource language attacks where sensitive information remains accessible in less dominant languages
- The proposed adaptive unlearning framework with language-dependent weights outperforms existing unlearning baselines
- The approach maintains overall model performance while selectively erasing information across different languages
**Limitations**: The abstract does not specify which model families or language sets were tested, and the approach may have limited generalizability to unseen languages or model architectures.

### Dang et al. (2024)

**Research question**: How does tokenization strategy (subword vs. character-level) influence the morphological knowledge encoded in multilingual language models?
**Methodology**: Compared mT5 (subword tokenization) and ByT5 (character-level tokenization) which share identical architecture, training objective, and data, by probing morphological knowledge on four tasks across 17 languages.
**Key findings**:
- Models learn the morphological systems of some languages better than others
- Morphological information is encoded in the middle and late layers of the models
- Languages with more morphological irregularities benefit more from having a higher share of pre-training data
- Tokenization strategy has measurable impact on morphological knowledge encoding despite identical training conditions
**Limitations**: Analysis is limited to two model variants (mT5 and ByT5) and 17 languages, which may not represent the full spectrum of tokenization strategies or linguistic diversity.

### Dixit and Dixit (2026)

**Research question**: Do multilingual language model tokenizers impose systematic efficiency and latency costs on certain writing systems?
**Methodology**: Quantified script tax by comparing two orthographic variants with identical linguistic content across mBERT and XLM-R, measuring fertility, inference speed, and bits per character.
**Key findings**:
- Higher-fragmentation orthography shows ~3.4x increase in fertility (6.73-6.85 vs. 2.10-2.35 tokens/word)
- 16.5x inference slowdown on identical hardware (0.23 vs. 3.8 sentences/second)
- Substantial increase in information cost: +19.7% for mBERT and +47.1% for XLM-R
- Gaps reflect orthography-conditioned processing rather than mapping noise (CER_rt=0.31)
- Tokenization is a key source of inequity in multilingual NLP
**Limitations**: Analysis focused on two orthographic variants; script-aware tokenization and pretraining solutions require further development and validation.

### Loyola et al. (2026)

**Research question**: Do multilingual language models learn a universal internal geometry for color that is perceptually grounded or primarily linguistic?
**Methodology**: Decomposed color representations into two geometric axes (perceptual alignment and cross-lingual symmetry) and analyzed layerwise embeddings across models and multilingual datasets.
**Key findings**:
- Perceptual grounding is weak: alignment to CIE-LAB peaks in intermediate layers then collapses toward output layers
- Cross-lingual symmetry degrades with depth, suggesting later layers encode language-specific structure
- Models achieve 96.7% accuracy on color classification at layers where perceptual alignment peaks
- Perceptual alignment (r=0.70) significantly correlates with downstream task performance
- Text-only LMs learn universal color-language geometry, not universal color-perception geometry
**Limitations**: Analysis limited to text-only language models without visual grounding; findings may differ for multimodal models trained on actual color perception data.

### Ponce and Etchegoyhen (2025)

**Research question**: Can In-Context Learning serve as a substitute for Instruction Tuning in multilingual language models, and how does model scale affect this comparison?
**Methodology**: Compared In-Context Learning against Instruction Tuning across multilingual language models of different scales to evaluate instruction-following capabilities.
**Key findings**:
- A performance gap remains between In-Context Learning and Instruction Tuning
- ICL cannot fully substitute for Instruction Tuning in multilingual scenarios
- Model scale affects the ICL vs. Instruction Tuning comparison
- High-quality instruction data remains challenging to obtain for multilingual contexts
**Limitations**: The gap between ICL and Instruction Tuning persists without clear solutions; research motivates further work but does not provide methods to reduce the gap.

### Rowe et al. (2025)

**Research question**: How do multilingual language models encode gender stereotypes across different languages beyond English-centric benchmarks?
**Methodology**: Introduced EuroGEST dataset measuring gender-stereotypical reasoning across English and 29 European languages using translation tools, quality estimation metrics, and morphological heuristics; evaluated 24 models from 6 model families.
**Key findings**:
- Strongest stereotypes across all models and languages: women are "beautiful", "empathetic", and "neat"; men are "leaders", "strong/tough", and "professional"
- Larger models encode gendered stereotypes more strongly than smaller models
- Instruction finetuning does not consistently reduce gendered stereotypes across models
- Most existing gender bias benchmarks remain English-centric, creating a gap in multilingual fairness evaluation
- The data generation method achieves high accuracy in both translations and gender labels across languages
**Limitations**: The dataset focuses only on European languages (29 languages plus English), limiting generalizability to non-European languages and cultural contexts.

### Verma et al. (2026)

**Research question**: Which linguistic properties—abstract language identity or surface-form cues—shape multilingual representations in language models?
**Methodology**: Analyzed language-associated units across different model families using the Language Activation Probability Entropy (LAPE) metric and decomposed activations with Sparse Autoencoders, testing effects of romanization and word-order shuffling.
**Key findings**:
- Language-associated units are strongly conditioned on orthography rather than abstract linguistic structure
- Romanization induces near-disjoint representations that align with neither native-script inputs nor English
- Word-order shuffling has limited effect on unit identity
- Typological structure becomes increasingly accessible in deeper layers
- Generation is most sensitive to units invariant to surface-form perturbations, not typological alignment
- Multilingual LMs organize representations around surface form, with linguistic abstraction emerging gradually without collapsing into unified interlingua
**Limitations**: Surface-form dominance may limit true cross-lingual transfer; the research does not provide methods to achieve unified interlingua representations.

### Winata et al. (2024)

**Research question**: How effective are multilingual language models' representations for semantic retrieval tasks across diverse languages including low-resource settings?
**Methodology**: Created the MINERS benchmark to evaluate multilingual LMs in semantic retrieval tasks (bitext mining and classification via retrieval-augmented contexts) across over 200 languages including challenging cross-lingual and code-switching settings.
**Key findings**:
- Retrieving semantically similar embeddings alone yields performance competitive with state-of-the-art approaches without requiring fine-tuning
- The framework successfully assesses robustness across 200+ diverse languages including extremely low-resource languages
- Multilingual LMs demonstrate effectiveness in challenging cross-lingual and code-switching retrieval settings
- The benchmark fills a gap in comprehensive exploration of multilingual model representations for semantic retrieval
**Limitations**: Evaluation focuses solely on retrieval without fine-tuning, which may not reflect performance in downstream tasks requiring adaptation; the benchmark may not cover all semantic retrieval scenarios.

### Xie et al. (2025)

**Research question**: Does pre-training Multilingual BERT (mBERT) on code-switched datasets improve the model's performance on critical NLP tasks?
**Methodology**: Pre-trained mBERT on a Spanglish tweets dataset and evaluated the pre-trained model against a baseline model on part-of-speech tagging, sentiment analysis, named entity recognition, and language identification tasks.
**Key findings**:
- The pre-trained mBERT model outperforms or matches the baseline model across all evaluated NLP tasks
- Most significant improvements were observed in part-of-speech tagging
- Latent analysis reveals more homogeneous English and Spanish embeddings for language identification tasks
- Demonstrates potential for adapting multilingual language models for code-switched input data in globalized contexts
**Limitations**: Limited to Spanglish (Spanish-English) code-switching; future work needed to extend to other language pairs, incorporate multiform data, and better understand context-dependent code-switches.

## References

Bagheri Nezhad, S., Agrawal, A., & Pokharel, R. (2024). Beyond data quantity: Key factors driving performance in multilingual language models. arXiv. https://arxiv.org/abs/2412.12500

Choi, M., Min, K., & Choo, J. (2024). Cross-lingual unlearning of selective knowledge in multilingual language models. arXiv. https://arxiv.org/abs/2406.12354

Dang, T. A., Raviv, L., & Galke, L. (2024). Tokenization and morphology in multilingual language models: A comparative analysis of mT5 and ByT5. arXiv. https://arxiv.org/abs/2410.11627

Dixit, A., & Dixit, S. (2026). The script tax: Measuring tokenization-driven efficiency and latency disparities in multilingual language models. arXiv. https://arxiv.org/abs/2602.11174

Loyola, P., Marrese-Taylor, E., & Hoyos-Idrobo, A. (2026). Probing the geometry of color representations in multilingual language models. arXiv. https://arxiv.org/abs/2610.18331

Ponce, D., & Etchegoyhen, T. (2025). In-context learning vs. Instruction tuning: The case of small and multilingual language models. arXiv. https://arxiv.org/abs/2503.01611

Rowe, J., Klimaszewski, M., Guillou, L., Vallor, S., & Birch, A. (2025). EuroGEST: Investigating gender stereotypes in multilingual language models. arXiv. https://arxiv.org/abs/2506.03867

Verma, A. A. K., Chatterjee, A., Gupta, M., & Chakraborty, T. (2026). Multilingual language models encode script over linguistic structure. arXiv. https://arxiv.org/abs/2604.05090

Winata, G. I., Zhang, R., & Adelani, D. I. (2024). MINERS: Multilingual language models as semantic retrievers. arXiv. https://arxiv.org/abs/2406.07424

Xie, K., Babbar, N., Chen, V., & Turura, Y. (2025). Enhancing multilingual language models for code-switched input data. arXiv. https://arxiv.org/abs/2503.07990
