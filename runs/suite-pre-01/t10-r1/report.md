# Systematic Literature Review: Text Summarization Evaluation

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "text summarization evaluation" and related queries, category cs.CL, 2024-2026
**Citation format**: APA 7th edition

## Executive Summary

The field of text summarization evaluation is undergoing a significant transformation driven by the emergence of large language models (LLMs) as both summarization systems and evaluation tools. The surveyed literature reveals a field grappling with fundamental questions about evaluation reliability, reproducibility, and the alignment between automatic metrics and human judgment. A clear consensus emerges that traditional reference-dependent metrics like ROUGE and BERTScore show poor correlation with human evaluation, while LLM-based evaluators demonstrate substantially better alignment. However, this shift introduces new challenges around computational cost, stability, and reproducibility. The literature also highlights the context-dependent value of evaluation approaches, with Summary Content Units (SCUs) proving most useful for ranking short summaries but less valuable for system-level comparisons. Recent work explores reasoning-enabled LLMs for evaluation, finding architecture-dependent benefits that vary across tasks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using queries for "text summarization evaluation" and "text summarization" filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 evaluation-focused papers were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search yielded only 3 papers with "evaluation" in their focus, so broader queries were used to reach 10 papers, meaning some included papers address evaluation as a secondary contribution rather than primary focus.

## Themes

### Theme 1: The Crisis of Traditional Automatic Metrics

A dominant theme across the literature is the recognition that widely-used automatic evaluation metrics fail to adequately capture summary quality. Nguyen et al. (2024) conducted a comprehensive comparative study of eight automatic metrics against human evaluation and found that ROUGE-2, BERTScore, and SummaC do not align well with human judgments and lack consistency in their assessments. This finding echoes concerns raised by Herserant and Guigue (2025), who discovered significant discrepancies between reported metric performances in the literature and those observed in their experimental settings.

The fundamental problem stems from the reference-dependent nature of these metrics. Traditional approaches require gold-standard reference summaries, which are expensive to create and may not capture the diversity of acceptable summaries. As Alansary and Hamdi (2026) note, relying on single metrics can lead to inconsistent quality assessment across articles with varying structures and topics. The literature suggests that the field is reaching a consensus that automatic metrics, while convenient, cannot be trusted as standalone indicators of summary quality without validation against human judgment.

### Theme 2: LLMs as Evaluators — Promise and Peril

In response to the limitations of traditional metrics, multiple papers propose using large language models as evaluation tools. Nguyen et al. (2024) found that LLM-based evaluation aligns closely with human evaluation, substantially outperforming traditional automatic metrics. Their proposed LLM-powered framework can automatically evaluate and improve text summarization, offering a promising direction for the field. Similarly, Larionov et al. (2025) explored reasoning-enabled LLMs for evaluation, finding that models like OpenAI o3-mini show improved performance with increased reasoning capabilities on certain evaluation tasks.

However, this shift introduces new challenges. Herserant and Guigue (2025) highlight a critical trade-off: metrics with the highest alignment to human judgments tend to be computationally intensive and less stable across runs. Their experiments revealed that LLM-based evaluation exhibits randomness, technical dependencies, and limited reproducibility. The structural trade-off between alignment quality and computational stability presents a fundamental challenge that the field must address. Larionov et al. (2025) further found that the benefits of reasoning LLMs are architecture and task-dependent, with DeepSeek-R1 underperforming compared to its non-reasoning variant except in summarization consistency evaluation.

### Theme 3: Summary Content Units and Fine-Grained Evaluation

A third theme focuses on decomposing summaries into finer-grained units for more precise evaluation. Nawrath et al. (2024) examined Summary Content Units (SCUs), which are concise sentences that decompose a summary into small facts that can be used to judge candidate summary quality. They explored two novel strategies for approximating SCUs: generating approximations from AMR meaning representations (SMUs) and from large language models (SGUs). Their key finding was that SGUs achieve the best approximation quality, outperforming both semantic role triplets (STUs) and SMUs.

However, the value of SCUs is context-dependent. Nawrath et al. (2024) demonstrated through a sentence-decomposition baseline that SCUs and their approximations offer the most value when ranking short summaries, but may not help as much when ranking systems or evaluating longer summaries. This finding suggests that evaluation approaches must be matched to the specific evaluation scenario rather than applied universally.

### Theme 4: Multi-Model and Ensemble Approaches

Several papers advocate for moving beyond single-model approaches to leverage multiple models for more robust evaluation and summarization. Alansary and Hamdi (2026) proposed a Multi-Model Summarization Framework that integrates multiple fine-tuned transformer-based models with a metric-based selection mechanism. Their framework generates candidate summaries from multiple models and selects the highest-quality output based on automatic evaluation metrics capturing both lexical similarity and semantic relevance. The approach achieved a BERTScore of 88.63%, outperforming several large language models including GPT3-D2, Falcon-7b, and Mpt-7b.

This ensemble philosophy extends to evaluation as well. Rehman et al. (2025) evaluated four leading models (BART, FLAN-T5, LLaMA-3-8B, and Gemma-7B) across five diverse datasets using multiple automatic metrics (ROUGE-1, ROUGE-2, ROUGE-L, BERTScore, and METEOR). Their findings revealed that different models exhibit varying strengths depending on text type and dataset characteristics, suggesting that evaluation must be multi-dimensional to capture the full picture of model performance.

### Theme 5: Domain-Specific and Low-Resource Evaluation Challenges

The literature also addresses evaluation challenges in specialized domains and low-resource settings. Sun et al. (2025) focused on medical text summarization, finding that their LongFormer-based model outperformed traditional models on ROUGE metrics and received high expert evaluation scores for information retention and grammatical accuracy. However, they acknowledged limitations in conciseness and readability, with expert evaluators noting redundant information in generated summaries. This highlights the importance of domain-specific evaluation criteria that go beyond generic metrics.

Sinha (2025) tackled the even more challenging problem of abstractive summarization for Sanskrit, a low-resource inflectional language. The work documented challenges at every stage of the development pipeline, from data collection and preprocessing to model training and evaluation. The inflectional nature of Sanskrit and limited training data create unique obstacles that standard evaluation approaches may not adequately address. This work underscores the need for evaluation frameworks that account for linguistic diversity and resource constraints.

### Theme 6: Infrastructure and Tooling for Evaluation Research

Finally, the literature recognizes the importance of infrastructure and tooling to support evaluation research. Syed et al. (2024) created TL;DR Progress, a tool that manually annotated 514 papers on neural text summarization using a comprehensive annotation scheme capturing evaluation metrics, quality dimensions, learning paradigms, challenges addressed, datasets, and document domains. This infrastructure enables fine-grained, faceted search across the literature, helping researchers identify relevant evaluation approaches and compare methodologies.

Jayatilleke et al. (2025) conducted a comprehensive survey exploring extractive, abstractive, and hybrid summarization approaches with comparative analysis of techniques and evaluation metrics. Their work provides technical and mathematical explanations of system architectures, serving as a reference for researchers designing evaluation studies. These infrastructure efforts are essential for advancing the field by enabling systematic comparison and reproducibility.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, there is universal consensus that traditional automatic metrics (ROUGE, BERTScore, SummaC) show poor alignment with human judgment and cannot be relied upon as standalone quality indicators (Nguyen et al., 2024; Herserant & Guigue, 2025). Second, multiple papers converge on the finding that LLM-based evaluators substantially outperform traditional metrics in aligning with human judgments (Nguyen et al., 2024; Larionov et al., 2025). Third, there is agreement that evaluation must be multi-dimensional, using multiple metrics and approaches to capture different aspects of summary quality (Rehman et al., 2025; Alansary & Hamdi, 2026). Finally, the literature converges on the recognition that evaluation approaches must be matched to specific contexts — what works for short summaries may not work for long ones, and domain-specific evaluation criteria are essential (Nawrath et al., 2024; Sun et al., 2025).

**Disagreements**: The literature reveals important disagreements and tensions. Most notably, there is disagreement about the value of reasoning capabilities in LLM evaluators. Larionov et al. (2025) found that reasoning benefits are architecture and task-dependent, with OpenAI o3-mini showing improvements but DeepSeek-R1 underperforming its non-reasoning variant. This suggests that reasoning is not universally beneficial for evaluation, contrary to what might be expected. Additionally, there is tension around the reproducibility of LLM-based evaluation. While Nguyen et al. (2024) advocate for LLM evaluators based on their alignment with human judgment, Herserant and Guigue (2025) raise serious concerns about the stability and reproducibility of these same approaches, highlighting a structural trade-off between alignment and reliability that remains unresolved.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Reproducibility Crisis**: Herserant and Guigue (2025) highlight fundamental reproducibility challenges in evaluation research, with significant discrepancies between reported and observed metric performances. The field lacks standardized protocols and exhaustive documentation practices that would enable reliable comparison across studies.

2. **Domain Generalization**: Most evaluation studies are conducted on specific domains (patents in Nguyen et al., 2024; medical texts in Sun et al., 2025; CNN/DailyMail in Alansary & Hamdi, 2026). There is limited work on cross-domain evaluation frameworks that can generalize across diverse text types and domains.

3. **Computational Cost Analysis**: While multiple papers note that high-alignment metrics are computationally intensive (Herserant & Guigue, 2025), none provide systematic analysis of the trade-offs between computational cost and evaluation quality. This gap limits practical deployment decisions.

4. **Linguistic Diversity**: With the exception of Sinha (2025) on Sanskrit, the literature focuses almost exclusively on English or high-resource languages. Evaluation approaches for low-resource and morphologically rich languages remain underexplored despite their importance for global NLP deployment.

5. **Long-Term Stability**: The stability concerns raised by Herserant and Guigue (2025) regarding LLM-based evaluators point to a deeper gap in understanding how evaluation metrics perform over time as models and data distributions shift. Longitudinal evaluation studies are absent from the literature.

6. **Human-in-the-Loop Frameworks**: While all papers acknowledge the importance of human evaluation as a gold standard, none propose practical frameworks for efficiently combining human and automatic evaluation in production settings. The gap between research evaluation protocols and practical deployment needs remains unaddressed.

## Per-Paper Annotations

### Alansary and Hamdi (2026)

**Research question**: How can we improve the robustness and quality of abstractive text summarization beyond relying on single models that produce inconsistent quality across varying article structures and topics?

**Methodology**: Proposed a Multi-Model Summarization Framework that integrates multiple fine-tuned transformer-based summarization models with a metric-based selection mechanism, where each model generates candidate summaries and the highest-quality summary is selected based on automatic evaluation metrics capturing lexical similarity and semantic relevance.

**Key findings**:
- Framework achieves highest BERTScore (88.63%) among all compared methods
- Outperforms several LLMs including GPT3-D2, Falcon-7b, and Mpt-7b
- Multi-model approach with metric-based selection improves quality and robustness of summarization
- Leveraging multiple transformer-based models addresses inconsistency issues of single-model approaches

**Limitations**: Evaluation conducted only on CNN/DailyMail dataset; framework relies on automatic evaluation metrics which have known limitations in aligning with human judgment as demonstrated by other papers in this collection.

### Herserant and Guigue (2025)

**Research question**: What reproducibility challenges exist in automatic text summarization evaluation, and how do reported metric performances in literature compare to actual experimental results?

**Methodology**: Conducted experiments across six representative metrics ranging from classical approaches (ROUGE) to recent LLM-based methods (G-Eval, SEval-Ex) on the SummEval dataset using a unified open-source framework designed for fair and transparent metric comparison.

**Key findings**:
- Significant discrepancies exist between reported performances in literature and those observed in experimental settings
- Metrics with highest alignment to human judgments tend to be computationally intensive and less stable across runs
- LLM-based evaluation exhibits randomness, technical dependencies, and limited reproducibility
- There is a structural trade-off between alignment quality and computational stability

**Limitations**: Study limited to six metrics on SummEval dataset; highlights inherent structural trade-offs that may be difficult to overcome without methodological standardization and exhaustive documentation.

### Jayatilleke et al. (2025)

**Research question**: What is the current state of automatic text summarization techniques, and how do different approaches compare in addressing the complexities of diverse writing styles across domains?

**Methodology**: Conducted a comprehensive survey exploring extractive, abstractive, and hybrid summarization approaches with linguistically diverse categorizations, comparative analysis of techniques and evaluation metrics, and technical/mathematical explanations of system architectures.

**Key findings**:
- Text summarization techniques are broadly categorized into extractive, abstractive, and hybrid methodologies
- Hybrid techniques combining extractive and abstractive approaches show promise for addressing diverse text complexities
- NLP and deep learning advancements have significantly enhanced summarization effectiveness across technical domains
- Various evaluation techniques and metrics exist for assessing generated summary quality across different language generation models

**Limitations**: The survey acknowledges that summarization remains constrained by intricate writing styles involving technical complexities; as a survey paper, it may not include the most recent developments or provide empirical validation of claims.

### Larionov et al. (2025)

**Research question**: How well do reasoning-enabled large language models perform compared to non-reasoning LLMs for evaluating machine translation and text summarization quality?

**Methodology**: Systematically compared eight models spanning state-of-the-art reasoning models (DeepSeek-R1, OpenAI o3), their distilled variants (8B-70B parameters), and equivalent non-reasoning LLMs on WMT23 and SummEval benchmarks with correlation analysis of reasoning token usage.

**Key findings**:
- OpenAI o3-mini models show improved performance with increased reasoning on machine translation evaluation
- DeepSeek-R1 underperforms compared to its non-reasoning variant except in summarization consistency evaluation
- Reasoning token usage correlates with evaluation quality only in specific models
- Distillation maintains reasonable performance up to 32B parameter models but degrades substantially at 8B scale
- Benefits of reasoning LLMs are architecture and task-dependent

**Limitations**: First assessment of reasoning LLMs for NLG evaluation; performance benefits are architecture and task-dependent, limiting universal applicability of reasoning models for evaluation tasks.

### Nawrath et al. (2024)

**Research question**: Are there better ways to approximate Summary Content Units (SCUs) than semantic role triplets, and under what conditions do SCUs or their approximations offer the most value in evaluation?

**Methodology**: Examined two novel strategies to approximate SCUs: generating SCU approximations from AMR meaning representations (SMUs) and from large language models (SGUs), comparing them against existing semantic role triplet (STU) approach and a sentence-decomposition baseline.

**Key findings**:
- SGUs (LLM-generated approximations) achieve the best approximation quality among all methods
- STUs and SMUs are competitive alternatives for SCU approximation
- SCUs and their approximations offer the most value when ranking short summaries
- SCUs may not help as much when ranking systems or evaluating longer summaries

**Limitations**: The sentence-decomposition baseline reveals that SCUs' value is context-dependent, offering limited benefits for certain evaluation scenarios like system ranking or longer summary assessment.

### Nguyen et al. (2024)

**Research question**: How can we bridge the gap between unreliable reference-dependent automatic metrics and time-consuming human evaluation for text summarization quality assessment?

**Methodology**: Conducted a comparative study evaluating eight automatic metrics, human evaluation, and a proposed LLM-based evaluation method across seven state-of-the-art summarization models on patent document datasets.

**Key findings**:
- LLM-based evaluation aligns closely with human evaluation judgments
- Widely-used automatic metrics (ROUGE-2, BERTScore, SummaC) do not align well with human evaluation
- Traditional automatic metrics lack consistency in their assessments
- Proposed LLM-powered framework can automatically evaluate and improve text summarization

**Limitations**: Evaluation was conducted only on patent document datasets, which may limit generalizability to other domains and summary types.

### Rehman et al. (2025)

**Research question**: How do leading pre-trained and open-source large language models compare in their text summarization capabilities across diverse datasets?

**Methodology**: Evaluated four models (BART, FLAN-T5, LLaMA-3-8B, and Gemma-7B) across five diverse datasets (CNN/DM, Gigaword, News Summary, XSum, and BBC News) using automatic metrics including ROUGE-1, ROUGE-2, ROUGE-L, BERTScore, and METEOR.

**Key findings**:
- Different models exhibit varying strengths and limitations depending on the text type and dataset characteristics
- The evaluation reveals comparative performance patterns across pre-trained versus open-source LLMs
- Automatic metrics provide multi-dimensional assessment of summary coherence and informativeness
- Model performance varies significantly across different domains and text lengths

**Limitations**: The abstract does not explicitly acknowledge limitations; potential gaps include lack of human evaluation and limited model diversity beyond the four tested architectures.

### Sinha (2025)

**Research question**: What are the challenges in developing abstractive text summarization for Sanskrit, a low-resource inflectional language?

**Methodology**: Developed a thesis addressing four thematic sub-questions through literature review, data collection and preprocessing, model training and inference, documenting challenges at every stage of the development pipeline for Sanskrit abstractive summarization.

**Key findings**:
- Initiated a pipeline for Sanskrit abstractive text summarization addressing a low-resource inflectional language
- Data collection and preprocessing present significant challenges for both language model and summarization model training
- Sanskrit's inflectional nature and low-resource status create unique development obstacles
- Research questions across four themes were systematically addressed to answer the key research question

**Limitations**: Sanskrit is a low-resource language with limited training data available; the inflectional nature of Sanskrit adds complexity to model development, and challenges were encountered at every stage of the pipeline.

### Sun et al. (2025)

**Research question**: How can LongFormer's long-range self-attention mechanism address the challenges of information loss and reduced summary quality when processing long medical texts?

**Methodology**: Proposed a LongFormer-based summarization method that introduces long-range self-attention to capture long-range dependencies in medical texts, evaluated against traditional models (RNN, T5, BERT) using ROUGE metrics and expert evaluations.

**Key findings**:
- LongFormer-based model outperforms traditional models (RNN, T5, BERT) on ROUGE automatic evaluation metrics
- The model receives high scores in expert evaluations, particularly for information retention and grammatical accuracy
- Long-range self-attention effectively captures dependencies and retains more key information from long medical texts
- The approach addresses short-term memory limitations of traditional summarization methods

**Limitations**: Generated summaries contain redundant information affecting conciseness; there is room for improvement in readability and fluency, requiring further optimization of the model structure.

### Syed et al. (2024)

**Research question**: How can the neural text summarization literature be systematically organized and explored to enable fine-grained, faceted search across research dimensions?

**Methodology**: Created TL;DR Progress, a tool that manually annotated 514 papers using a comprehensive annotation scheme capturing evaluation metrics, quality dimensions, learning paradigms, challenges addressed, datasets, and document domains, with automatically extracted contextual summaries for each paper.

**Key findings**:
- 514 papers on neural text summarization were successfully organized using a multi-faceted annotation scheme
- The tool enables fine-grained, faceted search across multiple research dimensions
- Each paper includes a succinct indicative summary with automatically extracted contextual factors, issues, and proposed solutions
- The annotation scheme captures diverse aspects including evaluation metrics, quality dimensions, and learning paradigms

**Limitations**: Manual annotation of 514 papers is labor-intensive and may not scale easily; the tool's coverage is limited to papers that have been annotated, potentially missing recent or emerging work.

## References

Alansary, A., & Hamdi, A. (2026). A multi-model metric-based selection framework for abstractive text summarization. arXiv. https://arxiv.org/abs/2606.05494

Herserant, T., & Guigue, V. (2025). AllSummedUp: Un framework open-source pour comparer les metriques d'evaluation de resume. arXiv. https://arxiv.org/abs/2508.21389

Jayatilleke, N., Weerasinghe, R., & Senanayake, N. (2025). Advancements in natural language processing for automatic text summarization. arXiv. https://arxiv.org/abs/2502.19773

Larionov, D., Takeshita, S., Zhang, R., Chen, Y., Leiter, C., Wang, Z., Greisinger, C., & Eger, S. (2025). DeepSeek-R1 vs. o3-mini: How well can reasoning LLMs evaluate MT and summarization? arXiv. https://arxiv.org/abs/2504.08120

Nawrath, M., Nowak, A., Ratz, T., Walenta, D. C., Opitz, J., Ribeiro, L. F. R., Sedoc, J., Deutsch, D., Mille, S., Liu, Y., Zhang, L., Gehrmann, S., Mahamood, S., Clinciu, M., Chandu, K., & Hou, Y. (2024). On the role of summary content units in text summarization evaluation. arXiv. https://arxiv.org/abs/2404.01701

Nguyen, H., Chen, H., Pobbathi, L., & Ding, J. (2024). A comparative study of quality evaluation methods for text summarization. arXiv. https://arxiv.org/abs/2407.00747

Rehman, T., Ghosh, S., Das, K., Bhattacharjee, S., Sanyal, D. K., & Chattopadhyay, S. (2025). Evaluating LLMs and pre-trained models for text summarization across diverse datasets. arXiv. https://arxiv.org/abs/2502.19339

Sinha, S. (2025). Abstractive text summarization for contemporary Sanskrit prose: Issues and challenges. arXiv. https://arxiv.org/abs/2501.01933

Sun, D., He, J., Zhang, H., Qi, Z., Zheng, H., & Wang, X. (2025). A LongFormer-based framework for accurate and efficient medical text summarization. arXiv. https://arxiv.org/abs/2503.06888

Syed, S., Al-Khatib, K., & Potthast, M. (2024). TL;DR Progress: Multi-faceted literature exploration in text summarization. arXiv. https://arxiv.org/abs/2402.06913
