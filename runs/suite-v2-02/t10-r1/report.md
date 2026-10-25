# Systematic Literature Review: Text Summarization Evaluation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "text summarization evaluation", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in text summarization evaluation methods and frameworks over the past two years. The surveyed literature reveals a field in transition, moving from traditional metrics like ROUGE toward more sophisticated evaluation approaches including LLM-based assessment, fine-grained content selection protocols, and abstractiveness metrics. A central tension emerges between evaluation quality and practical concerns: metrics that align best with human judgment tend to be computationally expensive and less reproducible. The literature also reflects growing interest in multi-model approaches, domain-specific evaluation (particularly medical), and the evaluation of LLMs themselves as both summarizers and evaluators. Collectively, these papers highlight the need for more robust, standardized evaluation protocols that balance alignment with human judgment, computational efficiency, and reproducibility.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "text summarization evaluation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Reproducibility and Reliability Challenges in Evaluation Metrics

A significant concern across recent work is the reproducibility of evaluation metrics, particularly LLM-based methods. Herserant and Guigue (2025) conducted experiments across six representative summarization evaluation metrics, from classical ROUGE to recent LLM-based methods like G-Eval and SEval-Ex. Their findings reveal significant discrepancies between reported performances in the literature and those observed in controlled experimental settings. They identified a structural trade-off: metrics with the highest alignment with human judgments tend to be computationally intensive and less stable across runs. LLMs used for evaluation exhibit randomness, technical dependencies, and limited reproducibility, raising concerns about their reliability for summarization assessment.

This theme connects to broader concerns about evaluation rigor in the field. As Larionov et al. (2025) note in their comparison of reasoning-enabled LLMs for evaluation tasks, the utility of newer model architectures for evaluating natural language generation remains an open question requiring systematic investigation. Their work provides the first assessment of reasoning LLMs for NLG evaluation, highlighting the need for careful benchmarking across different model architectures.

### Theme 2: Fine-Grained and Systematic Human Evaluation Protocols

Several papers address limitations in existing human evaluation protocols by proposing more systematic, fine-grained alternatives. Zhang et al. (2024) introduced QAPyramid, which improves upon the widely-adopted Pyramid human evaluation protocol for assessing content selection in text summarization. The Pyramid protocol breaks reference summaries into subunits and verifies their presence in system summaries, but suffers from lack of systematicity in defining subunit granularity. QAPyramid decomposes each reference summary into finer-grained question-answer pairs according to the QA-SRL framework, enabling more systematic evaluation while maintaining high inter-annotator agreement without requiring expert annotations.

The collection of 8.9K QA-level annotations across 10 summarization systems demonstrates that automated metrics can achieve higher correlations with QAPyramid than other widely adopted metrics. This work represents a shift toward evaluation protocols that are both more granular and more automatable, addressing long-standing challenges in summarization evaluation.

### Theme 3: Multi-Model and Ensemble Approaches

A recurring theme is the use of multiple models to improve summarization quality and robustness. Fang et al. (2024) proposed a Multi-LLM summarization framework with two strategies: centralized and decentralized. In both approaches, k different LLMs generate diverse summaries, but they differ in evaluation: centralized approaches use a single LLM to evaluate and select the best summary, while decentralized approaches use k LLMs for evaluation. Their results show that multi-LLM approaches significantly outperform single-LLM baselines by up to 3x, indicating the effectiveness of leveraging multiple models for summarization.

Similarly, Alansary and Hamdi (2026) presented a Multi-Model Summarization Framework that integrates multiple fine-tuned transformer-based models with a metric-based selection mechanism. Each model independently generates a candidate summary, and the framework selects the highest-quality summary based on automatic evaluation metrics capturing both lexical similarity and semantic relevance. Their approach achieved the highest BERTScore (88.63%) among compared methods on the CNN/DailyMail dataset, outperforming several LLMs including GPT3-D2, Falcon-7b, and Mpt-7b.

### Theme 4: Domain-Specific Evaluation Challenges

Several papers highlight the unique evaluation challenges posed by domain-specific summarization tasks. Balde et al. (2025) focused on medical text summarization, showing that LLMs exhibit significant performance drops for data points with high concentrations of out-of-vocabulary (OOV) words or high novelty. Their benchmarking study reveals that even Llama-3.1, with approximately 128K tokens in its vocabulary, faces over-fragmentation issues with medical words. They demonstrate that vocabulary adaptation—updating the LLM vocabulary with medical domain words or subwords—helps improve summarization performance in difficult settings. Human evaluation with medical experts confirmed that vocabulary adaptation results in more relevant and faithful summaries.

Aly et al. (2025) similarly found notable performance variations based on dataset properties when evaluating six LLMs across four datasets spanning news, dialog, and scientific domains. Their work shows that LLMs perform competitively on news and dialog tasks, but performance on long scientific documents improves significantly when aided by chunking strategies that enable LLMs with shorter context windows to process extended inputs.

### Theme 5: Abstractiveness and Content Quality Metrics

Beyond traditional surface-level metrics, recent work has developed more principled approaches to measuring abstractiveness in generated summaries. Katwe et al. (2026) introduced Reference Abstraction (RA), Summary Abstraction (SA), and Abstraction Ratio (AR)—heuristic metrics that measure how much a summary diverges from extractive copying of the source text. Their formulation uses the harmonic mean of document lengths modulated by a cubic non-overlap factor, yielding dimensionally consistent, bounded output with non-linear sensitivity to the extractive-abstractive boundary.

Evaluation on 100 XSUM documents across four summarization models demonstrated that these metrics successfully discriminate between extractive models (SA ~ 0.12-0.26) and abstractive models (SA ~ 0.96-1.77). The Abstraction Ratio identifies summaries requiring manual evaluation for potential hallucination, providing a principled approach to quantifying abstractiveness beyond ROUGE-like metrics.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that no single evaluation metric or approach is sufficient for comprehensive summarization assessment. Herserant and Guigue (2025), Aly et al. (2025), and Rehman et al. (2025) all emphasize the importance of using multiple metrics to capture different aspects of summarization quality. There is also broad agreement that domain-specific considerations matter: Balde et al. (2025) and Aly et al. (2025) both demonstrate that summarization performance varies significantly across domains, requiring tailored approaches.

The literature also converges on the value of multi-model approaches. Both Fang et al. (2024) and Alansary and Hamdi (2026) demonstrate that leveraging multiple models improves summarization quality and robustness compared to single-model approaches.

**Disagreements**: The literature reveals tensions around the role of LLMs in evaluation. While Herserant and Guigue (2025) highlight concerns about LLM-based evaluation reliability, randomness, and limited reproducibility, Larionov et al. (2025) explore whether reasoning-enabled LLMs can overcome these limitations. Their findings are mixed: OpenAI o3-mini models show improved performance with increased reasoning on machine translation tasks, but DeepSeek-R1 underperforms compared to its non-reasoning variant except in summarization consistency evaluation. This suggests that the utility of reasoning LLMs for evaluation is architecture and task-dependent, with no clear consensus on their superiority.

## Gaps and Open Questions

Several gaps emerge from the surveyed literature. First, none of the papers explicitly state limitations of their own experimental approaches in their abstracts, suggesting a potential gap in self-critical evaluation within the field. Second, while multiple papers advocate for multi-model approaches, there is limited guidance on how to select which models to include in an ensemble or how to balance diversity against computational cost.

The tension between evaluation quality and computational efficiency remains unresolved. Herserant and Guigue (2025) identify this as a structural trade-off, but no paper offers a satisfactory solution. Similarly, while vocabulary adaptation shows promise for domain-specific summarization (Balde et al., 2025), the optimal strategies for vocabulary expansion and their generalizability across domains remain open questions.

Finally, the field lacks standardized protocols for evaluating summarization in low-resource or high-OOV settings. While Balde et al. (2025) and Aly et al. (2025) address specific aspects of this challenge, a comprehensive framework for evaluating summarization under difficult conditions remains undeveloped.

## Per-Paper Annotations

### Alansary and Hamdi (2026)

**Research question**: How can a multi-model framework improve the robustness and quality of abstractive text summarization compared to single-model approaches?
**Methodology**: The authors developed a Multi-Model Summarization Framework that integrates multiple fine-tuned transformer-based models with a metric-based selection mechanism, evaluated on the CNN/DailyMail dataset.
**Key findings**:
- The framework achieved the highest BERTScore (88.63%) among all compared methods
- Outperformed several LLMs including GPT3-D2, Falcon-7b, and Mpt-7b
- Metric-based selection of the best summary from multiple candidates improves quality and robustness
**Limitations**: Not stated in abstract.

### Aly, Soliman, and AbdelAziz (2025)

**Research question**: How do different large language models perform on text summarization tasks across various domains and datasets when using prompt engineering techniques?
**Methodology**: Systematic evaluation of six LLMs across four datasets (CNN/Daily Mail, NewsRoom, SAMSum, and ArXiv) using zero-shot and in-context learning prompt engineering techniques, with evaluation via ROUGE and BERTScore metrics and inference time analysis.
**Key findings**:
- LLMs perform competitively on news and dialog summarization tasks
- Performance on long scientific documents improves significantly with chunking strategies
- Notable performance variations exist based on model parameters, dataset properties, and prompt design
- Trade-off exists between summarization quality and computational efficiency
**Limitations**: Not stated in abstract.

### Balde et al. (2025)

**Research question**: How do LLMs perform on medical text summarization under difficult settings with high out-of-vocabulary word concentration, and can vocabulary adaptation improve performance?
**Methodology**: Benchmarking study across three medical summarization datasets evaluating multiple vocabulary adaptation strategies and two continual pretraining strategies, with human evaluation by medical experts.
**Key findings**:
- LLMs show significant performance drop for data points with high OOV word concentration or high novelty
- Llama-3.1 faces over-fragmentation issues with medical words despite large vocabulary size
- Vocabulary adaptation improves LLM summarization performance even in difficult settings
- Medical experts found vocabulary adaptation results in more relevant and faithful summaries
**Limitations**: Not stated in abstract.

### Fang et al. (2024)

**Research question**: How can multi-LLM frameworks improve text summarization quality compared to single-LLM approaches?
**Methodology**: Proposed Multi-LLM summarization framework with centralized and decentralized strategies, where k different LLMs generate diverse summaries and evaluation is performed by either a single LLM (centralized) or k LLMs (decentralized).
**Key findings**:
- Multi-LLM approaches significantly outperform single-LLM baselines by up to 3x
- Both centralized and decentralized strategies are effective
- Multi-model generation and evaluation steps improve summarization quality
**Limitations**: Not stated in abstract.

### Herserant and Guigue (2025)

**Research question**: How reproducible are automatic text summarization evaluation metrics, and how do reported performances compare to observed experimental results?
**Methodology**: Experiments across six representative summarization evaluation metrics (ROUGE to LLM-based methods like G-Eval and SEval-Ex) using the SummEval dataset with a unified open-source framework for fair comparison.
**Key findings**:
- Significant discrepancies exist between reported performances in literature and observed experimental results
- Metrics with highest alignment to human judgments tend to be computationally intensive and less stable across runs
- LLMs for evaluation exhibit randomness, technical dependencies, and limited reproducibility
- Structural trade-off exists between alignment quality and computational efficiency/stability
**Limitations**: Not stated in abstract.

### Jayatilleke, Weerasinghe, and Senanayake (2025)

**Research question**: How have advancements in NLP and deep learning enhanced text summarization approaches, and what are the comparative strengths of different summarization techniques?
**Methodology**: Comprehensive survey addressing linguistically diverse categorizations of text summarization approaches, exploring hybrid techniques combining extractive and abstractive methodologies, with comparative analysis of different techniques and metrics.
**Key findings**:
- NLP and deep learning advancements have significantly enhanced summarization effectiveness across technical domains
- Text summarization remains constrained by intricate writing styles and technical complexities
- Hybrid techniques combining extractive and abstractive approaches show promise
- Comparative analysis reveals distinct pros and cons of various approaches
**Limitations**: Not stated in abstract.

### Katwe, Balabantaray, and Vittala (2026)

**Research question**: How can abstractiveness in generated summaries be quantified beyond surface-level metrics like ROUGE?
**Methodology**: Introduced Reference Abstraction (RA), Summary Abstraction (SA), and Abstraction Ratio (AR) metrics using harmonic mean of document lengths modulated by cubic non-overlap factor, evaluated on 100 XSUM documents across four summarization models.
**Key findings**:
- Metrics successfully discriminate between extractive models (SA ~ 0.12-0.26) and abstractive models (SA ~ 0.96-1.77)
- Abstraction Ratio identifies summaries requiring manual evaluation for potential hallucination
- Formulation yields dimensionally consistent, bounded output with non-linear sensitivity
**Limitations**: Not stated in abstract.

### Larionov et al. (2025)

**Research question**: How do reasoning-enabled large language models compare to non-reasoning LLMs for evaluating natural language generation in machine translation and text summarization tasks?
**Methodology**: Systematic comparison of eight models including reasoning models (DeepSeek-R1, OpenAI o3), distilled variants (8B-70B parameters), and equivalent non-reasoning LLMs on WMT23 and SummEval benchmarks using correlation analysis.
**Key findings**:
- OpenAI o3-mini models show improved performance with increased reasoning on machine translation tasks
- DeepSeek-R1 underperforms compared to non-reasoning variant except in summarization consistency evaluation
- Reasoning token usage correlates with evaluation quality only in specific models
- Distillation maintains reasonable performance up to 32B parameters but degrades at 8B scale
**Limitations**: Not stated in abstract.

### Rehman et al. (2025)

**Research question**: How do leading pre-trained and open-source large language models compare in their text summarization capabilities across diverse datasets?
**Methodology**: Evaluation of four models (BART, FLAN-T5, LLaMA-3-8B, and Gemma-7B) across five datasets (CNN/DM, Gigaword, News Summary, XSum, and BBC News) using ROUGE-1, ROUGE-2, ROUGE-L, BERTScore, and METEOR metrics.
**Key findings**:
- Evaluation reveals comparative strengths and limitations of the four models across different text types
- Different models show varying performance across the five diverse datasets
- Multiple automatic metrics provide comprehensive assessment of summarization capabilities
**Limitations**: Not stated in abstract.

### Zhang et al. (2024)

**Research question**: How can the Pyramid human evaluation protocol for text summarization be improved to address its lack of systematicity in defining and granularizing sub-units?
**Methodology**: Proposed QAPyramid, which decomposes reference summaries into finer-grained question-answer pairs using the QA-SRL framework, with collection of QA-SRL annotations for CNN/DM reference summaries and evaluation of 10 summarization systems (8.9K QA-level annotations).
**Key findings**:
- QAPyramid provides more systematic and fine-grained content selection evaluation compared to Pyramid
- Maintains high inter-annotator agreement without requiring expert annotations
- Proposed automated metrics achieve higher correlations with QAPyramid than other widely adopted metrics
- QA-SRL framework enables decomposition into finer-grained evaluative units
**Limitations**: Not stated in abstract.

## References

Alansary, A., & Hamdi, A. (2026). A multi-model metric-based selection framework for abstractive text summarization. arXiv. https://arxiv.org/abs/2606.05494

Aly, W. M., Soliman, T. H. A., & AbdelAziz, A. M. (2025). An evaluation of large language models on text summarization tasks using prompt engineering techniques. arXiv. https://arxiv.org/abs/2507.05123

Balde, G., Roy, S., Mondal, M., & Ganguly, N. (2025). Evaluation of LLMs in medical text summarization: The role of vocabulary adaptation in high OOV settings. arXiv. https://arxiv.org/abs/2505.21242

Fang, J., Liu, C.-T., Kim, J., Bhedaru, Y., Liu, E., Singh, N., Lipka, N., Mathur, P., Ahmed, N. K., Dernoncourt, F., Rossi, R. A., & Deilamsalehy, H. (2024). Multi-LLM text summarization. arXiv. https://arxiv.org/abs/2412.15487

Herserant, T., & Guigue, V. (2025). AllSummedUp: Un framework open-source pour comparer les metriques d'evaluation de resume. arXiv. https://arxiv.org/abs/2508.21389

Jayatilleke, N., Weerasinghe, R., & Senanayake, N. (2025). Advancements in natural language processing for automatic text summarization. arXiv. https://arxiv.org/abs/2502.19773

Katwe, P., Balabantaray, R. C., & Vittala, K. P. (2026). Abstractiveness metrics for evaluating text summarization: A refined formulation with empirical validation. arXiv. https://arxiv.org/abs/2607.10806

Larionov, D., Takeshita, S., Zhang, R., Chen, Y., Leiter, C., Wang, Z., Greisinger, C., & Eger, S. (2025). DeepSeek-R1 vs. o3-mini: How well can reasoning LLMs evaluate MT and summarization? arXiv. https://arxiv.org/abs/2504.08120

Rehman, T., Ghosh, S., Das, K., Bhattacharjee, S., Sanyal, D. K., & Chattopadhyay, S. (2025). Evaluating LLMs and pre-trained models for text summarization across diverse datasets. arXiv. https://arxiv.org/abs/2502.19339

Zhang, S., Wan, D., Cattan, A., Klein, A., Dagan, I., & Bansal, M. (2024). QAPyramid: Fine-grained evaluation of content selection for text summarization. arXiv. https://arxiv.org/abs/2412.07096
