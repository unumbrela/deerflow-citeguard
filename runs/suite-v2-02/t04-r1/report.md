# Systematic Literature Review: Hallucination Detection in Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "hallucination detection large language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review synthesizes findings from 10 recent arXiv papers (2024-2026) on hallucination detection in large language models within the cs.CL category. The surveyed literature reveals a rapidly evolving field characterized by diverse methodological approaches ranging from lightweight CPU-feasible detectors to sophisticated sparse auto-encoder frameworks. A prominent trend is the shift toward unified benchmarks and standardized evaluation pipelines, enabling consistent comparison across detection methods. Research increasingly focuses on efficiency, with adaptive sampling strategies and small language model ensembles achieving competitive performance while reducing computational costs. However, significant challenges remain, particularly in detecting localized hallucinations in summarization tasks and extending detection capabilities across multilingual contexts beyond English-centric benchmarks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "hallucination detection large language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmark Standardization and Unified Evaluation Frameworks

A dominant theme across the surveyed literature is the push toward standardized evaluation pipelines for hallucination detection. Multiple papers recognize that inconsistent inference configurations and limited domain coverage have hampered reproducible comparisons across detection methods. Li et al. (2026) introduce OpenHalDet, a unified benchmark that standardizes the entire evaluation pipeline from prompt construction through detector scoring and metric computation, supporting heterogeneous detector families under black-box, gray-box, and white-box access settings. Similarly, Zhang et al. (2025) present Poly-FEVER, a large-scale multilingual fact verification benchmark comprising 77,973 labeled factual claims across 11 languages, addressing the critical gap of English-centric evaluation. These works collectively emphasize that meaningful progress in hallucination detection requires shared infrastructure enabling controlled comparison of diverse tasks, models, and detectors within a unified framework.

### Theme 2: Efficiency-Oriented Detection Methods

Computational efficiency emerges as a central concern across multiple papers, with researchers developing adaptive and lightweight approaches that maintain detection quality while reducing resource requirements. Sun et al. (2026) propose an Adaptive Bayesian Estimation framework for Semantic Entropy that dynamically adjusts sampling requirements using variance-based thresholds, achieving comparable detection performance with approximately 50% fewer samples in low-budget scenarios. Cheung (2025) demonstrates that multiple small language models can effectively verify LLM responses, achieving a 10% improvement in F1 scores while providing a scalable solution for both academic and practical applications. Faujdar and Kadvani (2026) systematically benchmark lightweight, CPU-feasible detectors including ROUGE-L, semantic similarity, BERTScore, and NLI-based methods, showing that ensemble approaches can achieve F1 = 0.792 on QA tasks without GPU acceleration. This efficiency focus reflects growing recognition that hallucination detection must be deployable in resource-constrained environments.

### Theme 3: Geometric and Latent Space Approaches

A sophisticated thread of research leverages the geometric structure of token embeddings and latent dynamics to detect hallucinations. Oblovatny et al. (2025) introduce a method based on estimating probabilistic distances between distributions of prompt token embeddings and response token embeddings, examining the geometric structure of token hidden states to extract factuality signals in a fully unsupervised manner. Chen et al. (2026) propose HalluSAE, a phase transition-inspired framework using sparse auto-encoders and a geometric potential energy metric to model hallucination as a critical shift in the model's latent dynamics. These approaches share the insight that hallucination manifests as detectable structural changes in the model's internal representations, offering a more principled alternative to surface-level text comparison methods.

### Theme 4: Architecture-Specific Detection Strategies

Recent work increasingly tailors detection methods to specific model architectures rather than applying one-size-fits-all approaches. Chang et al. (2025) develop TraceDet specifically for diffusion large language models (D-LLMs), recognizing that existing methods designed for auto-regressive LLMs are ill-suited for the multi-step denoising process characteristic of diffusion models. Their framework models the denoising process as an action trace and identifies sub-traces maximally informative to hallucinated responses, achieving an average AUROC gain of 15.2% compared to baselines. Zhang et al. (2025) integrate the HHEM framework, a lightweight classification-based approach independent of LLM-based judgments, and conduct comparative analysis across various LLM sizes, finding that larger models (7B-9B parameters) generally exhibit fewer hallucinations while intermediate-sized models show higher instability. This architecture-aware trend reflects maturation in the field as researchers recognize that different generation paradigms require specialized detection strategies.

### Theme 5: Comprehensive Taxonomy and Integrated Detection-Correction Systems

Several papers move beyond binary detection toward comprehensive taxonomies and integrated systems that combine detection, identification, and correction. Xu et al. (2025) introduce a comprehensive hallucination taxonomy with 11 categories across various natural language generation tasks and propose HAD models that integrate hallucination detection, span-level identification, and correction into a single inference process. Their models, trained on approximately 90K synthetic samples, achieve state-of-the-art results on HaluEval, FactCHD, and FaithBench benchmarks, confirming robustness and versatility across tasks. This integrated approach reflects recognition that practical deployment requires not just detecting hallucinations but also identifying their precise locations and generating corrected outputs within a unified pipeline.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, multiple papers converge on the necessity of standardized benchmarks and evaluation pipelines for meaningful comparison across detection methods (Li et al., 2026; Zhang et al., 2025). Second, there is consensus that efficiency matters: adaptive sampling, lightweight models, and CPU-feasible methods can achieve competitive performance without prohibitive computational costs (Sun et al., 2026; Cheung, 2025; Faujdar & Kadvani, 2026). Third, papers consistently find that summarization tasks present unique challenges for hallucination detection, with multiple works reporting near-chance performance on summarization benchmarks and requiring specialized techniques like segment-based retrieval to improve detection (Zhang et al., 2025; Faujdar & Kadvani, 2026).

**Disagreements**: While the surveyed papers do not exhibit direct contradictions, they reflect different philosophical approaches to the detection problem. The geometric/latent space approaches (Oblovatny et al., 2025; Chen et al., 2026) assume hallucination manifests as detectable structural changes in internal representations, while benchmark-focused works (Li et al., 2026; Zhang et al., 2025) prioritize standardized evaluation over theoretical grounding. Additionally, there is tension between architecture-specific methods optimized for particular model families (Chang et al., 2025) versus general-purpose detectors applicable across architectures (Xu et al., 2025).

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, multilingual coverage remains limited: while Poly-FEVER (Zhang et al., 2025) addresses this partially, most detection methods are developed and evaluated primarily on English datasets, leaving open the question of cross-lingual generalization. Second, summarization consistently emerges as the hardest task, with lightweight methods performing near chance levels even with improvements like sentence-level chunk aggregation (Faujdar & Kadvari, 2026; Zhang et al., 2025). Third, several papers note limitations in detecting localized hallucinations—errors confined to specific text segments—requiring specialized segment-based verification strategies that are not yet widely adopted. Fourth, most abstracts do not explicitly state limitations, suggesting either space constraints or insufficient critical reflection on method boundaries. Finally, the dynamic nature of hallucinations and their underlying mechanisms remain understudied, with most existing methods treating hallucination as a static property rather than a process emerging during generation (Chen et al., 2026).

## Per-Paper Annotations

### Chang et al. (2025)

**Research question**: How can hallucination detection be improved for diffusion large language models (D-LLMs) where hallucination signals emerge throughout the multi-step denoising process?

**Methodology**: The authors propose TraceDet, a framework that models the denoising process as an action trace with each action defined as the model's prediction over the cleaned response conditioned on the previous intermediate output, identifying the sub-trace maximally informative to hallucinated responses.

**Key findings**:
- Existing hallucination detection methods designed for auto-regressive LLMs are ill-suited for D-LLMs
- TraceDet consistently improves hallucination detection across various open source D-LLMs
- The framework achieves an average gain in AUROC of 15.2% compared to baselines
- Hallucination signals in D-LLMs emerge throughout the multi-step denoising process rather than in single-step generation

**Limitations**: Not stated in abstract.

### Chen et al. (2026)

**Research question**: How can hallucination detection leverage the dynamic nature and underlying mechanisms of hallucinations in large language models?

**Methodology**: The authors propose HalluSAE, a phase transition-inspired framework that models hallucination as a critical shift in the model's latent dynamics using sparse auto-encoders and a geometric potential energy metric, consisting of three stages: potential energy empowered phase zone localization, hallucination-related sparse feature attribution using contrastive logit attribution, and probing-based causal hallucination detection through linear probes on disentangled features.

**Key findings**:
- HalluSAE models hallucination as a critical shift in the model's latent dynamics
- The framework identifies critical transition zones and attributes factual errors to specific high-energy sparse features
- HalluSAE achieves state-of-the-art hallucination detection performance on Gemma-2-9B
- Most existing hallucination detection methods overlook the dynamic nature and underlying mechanisms of hallucinations

**Limitations**: Not stated in abstract.

### Cheung (2025)

**Research question**: How can hallucinations in LLM responses be detected without ground truth in retrieval-augmented generation scenarios?

**Methodology**: The paper proposes a framework integrating multiple small language models to verify LLM responses by breaking responses into individual sentences and using the probability of generating 'Yes' tokens from multiple models for questions, responses, and retrieved context.

**Key findings**:
- The framework was validated on real datasets with over 100 sets of questions, answers, and contexts
- The method achieved a 10% improvement in F1 scores for detecting correct responses compared to hallucinations
- Multiple small language models can be effectively employed for answer verification
- The approach provides a scalable and efficient solution for both academic and practical applications

**Limitations**: Not stated in abstract.

### Faujdar and Kadvani (2026)

**Research question**: How well can hallucination detection perform using only lightweight, CPU-feasible methods built on public models for resource-constrained researchers and practitioners?

**Methodology**: The authors benchmarked four lightweight detectors (ROUGE-L, semantic similarity, BERTScore, and an NLI detector based on a FEVER-trained DeBERTa model) plus a score-level ensemble across all three tasks of the HaluEval benchmark: question answering, dialogue, and summarisation, calibrating on a held-out validation split and evaluating on 2,000 test instances per task with bootstrap confidence intervals.

**Key findings**:
- The similarity-NLI ensemble is the most consistent method across tasks
- On QA, the ensemble achieves F1 = 0.792 and AUC-ROC = 0.873
- On dialogue, the ensemble achieves F1 = 0.694 and AUC-ROC = 0.749
- On summarisation, every method performs near chance (AUC-ROC between 0.469 and 0.574)
- Raising premise budget and using sentence-level chunk aggregation improves summarisation AUC-ROC from 0.567 to 0.683 on CPU

**Limitations**: The study focuses on lightweight, CPU-feasible methods which may not capture the full potential of GPU-intensive approaches; summarisation remains the hardest task even with improvements.

### Li et al. (2026)

**Research question**: How can hallucination detection evaluations be standardized to enable consistent comparison, reproduction, and generalization across different domains and tasks?

**Methodology**: The paper introduces OpenHalDet, a unified benchmark that standardizes the evaluation pipeline from prompt construction and response generation to truthfulness annotation, detector scoring, and metric computation, supporting heterogeneous detector families under black-box, gray-box, and white-box access settings.

**Key findings**:
- Existing evaluations face challenges in inconsistent inference configuration and limited coverage of downstream domains
- OpenHalDet enables controlled comparison of diverse tasks, models, and detectors within a shared framework
- The benchmark provides a systematic view of how different detection paradigms behave in LLM applications
- The codebase is released as open and extensible to facilitate reproducible evaluation

**Limitations**: Not stated in abstract.

### Oblovatny et al. (2025)

**Research question**: How can hallucination detection methods be specifically designed for RAG systems to overcome limitations of existing approaches?

**Methodology**: The paper introduces a hallucination detection method based on estimating distances between distributions of prompt token embeddings and language model response token embeddings, examining the geometric structure of token hidden states to extract factuality signals.

**Key findings**:
- The method achieves state-of-the-art or competitive performance in extensive experiments
- The approach is friendly to long sequences
- The method has transferability from NLI tasks to hallucination detection tasks
- It is a fully unsupervised and efficient method with competitive performance

**Limitations**: Not stated in abstract.

### Sun et al. (2026)

**Research question**: How can hallucination detection methods adapt sampling requirements based on query complexity to improve computational efficiency?

**Methodology**: The paper proposes an Adaptive Bayesian Estimation framework for Semantic Entropy with Guided Semantic Exploration that dynamically adjusts sampling requirements using a hierarchical Bayesian framework with variance-based thresholds and a perturbation-based importance sampling strategy.

**Key findings**:
- The method achieves superior hallucination detection performance with significant efficiency gains
- In low-budget scenarios, the approach requires about 50% fewer samples to achieve comparable detection performance
- The method delivers an average AUROC improvement of 12.6% under the same sampling budget
- Experiments were conducted on four QA datasets

**Limitations**: Not stated in abstract.

### Xu et al. (2025)

**Research question**: How can hallucination detection, span-level identification, and correction be integrated into a single inference process for natural language generation models?

**Methodology**: The authors introduce a comprehensive hallucination taxonomy with 11 categories across various NLG tasks and propose HAD models that integrate hallucination detection, span-level identification, and correction into a single inference process, training on a synthetic dataset of about 90K samples and evaluating on both in-domain and out-of-domain test sets.

**Key findings**:
- HAD models outperform existing baselines on HaluEval, FactCHD, and FaithBench benchmarks
- The models achieve state-of-the-art results confirming their robustness and versatility
- HAD models can be applied to various NLG tasks due to their versatile design
- The comprehensive hallucination taxonomy with 11 categories covers various NLG tasks

**Limitations**: Not stated in abstract.

### Zhang et al. (2025) [Poly-FEVER]

**Research question**: How can hallucination detection in large language models be evaluated across diverse linguistic contexts rather than just English and a few widely spoken languages?

**Methodology**: The authors created Poly-FEVER, a large-scale multilingual fact verification benchmark comprising 77,973 labeled factual claims spanning 11 languages, sourced from FEVER, Climate-FEVER, and SciFact, conducting systematic evaluation of LLMs including ChatGPT and the LLaMA series and analyzing how topic distribution and web resource availability influence hallucination frequency.

**Key findings**:
- Topic distribution and web resource availability influence hallucination frequency in LLMs
- Language-specific biases impact model accuracy in hallucination detection
- Poly-FEVER enables cross-linguistic comparisons of hallucination detection across 11 languages
- The benchmark facilitates development of more reliable, language-inclusive AI systems

**Limitations**: Not stated in abstract.

### Zhang et al. (2025) [HHEM]

**Research question**: How can hallucination evaluation methods balance computational efficiency with robust factual validation across different LLMs?

**Methodology**: The paper integrates the HHEM framework, a lightweight classification-based approach independent of LLM-based judgments, and conducts comparative analysis across various LLMs evaluating TPR, TNR, and Accuracy on QA and summarization tasks, introducing segment-based retrieval for localized hallucinations.

**Key findings**:
- HHEM reduces evaluation time from 8 hours to 10 minutes while maintaining high detection accuracy
- HHEM with non-fabrication checking achieves 82.2% accuracy and 78.9% TPR
- HHEM struggles with localized hallucinations in summarization tasks
- Segment-based retrieval improves detection by verifying smaller text components
- Larger models (7B-9B parameters) generally exhibit fewer hallucinations while intermediate-sized models show higher instability

**Limitations**: HHEM struggles with localized hallucinations in summarization tasks, requiring segment-based retrieval to address this limitation.

## References

Chang, S., Yu, J., Wang, W., Chen, Y., Yu, J., Torr, P., & Gu, J. (2025). TraceDet: Hallucination detection from the decoding trace of diffusion large language models. arXiv. https://arxiv.org/abs/2510.01274

Chen, B., Fan, Z., Wang, K., Leng, Z., Wu, F., Zheng, H., Sun, Y., & Wu, W. (2026). HalluSAE: Detecting hallucinations in large language models via sparse auto-encoders. arXiv. https://arxiv.org/abs/2604.16430

Cheung, M. (2025). Hallucination detection with small language models. arXiv. https://arxiv.org/abs/2506.22486

Faujdar, K., & Kadvani, S. (2026). How far can you get without a GPU? A systematic benchmark of lightweight hallucination detection across question answering, dialogue, and summarisation. arXiv. https://arxiv.org/abs/2606.29809

Li, X., Fang, Z., Deng, Y., Luo, J., Ma, H., Oh, C., Shi, Z., Ye, S., Wang, H., Chen, S.-L., Luo, Y., Yang, M., Du, S., Li, S., & Chen, L. (2026). OpenHalDet: A unified benchmark for hallucination detection across diverse generation scenarios. arXiv. https://arxiv.org/abs/2606.06959

Oblovatny, R., Kuleshova, A., Polev, K., & Zaytsev, A. (2025). Probabilistic distances-based hallucination detection in LLMs with RAG. arXiv. https://arxiv.org/abs/2506.09886

Sun, Q., Li, X., He, X., Cheng, A., Ji, X., Lu, H., Huang, R., & Hu, Q. (2026). Efficient hallucination detection: Adaptive Bayesian estimation of semantic entropy with guided semantic exploration. arXiv. https://arxiv.org/abs/2603.22812

Xu, F., Hu, X., Yu, Z., Lin, L., Zhang, X., Zhang, Y., Zhou, W., Gu, J., & Wan, X. (2025). HAD: HAllucination detection language models based on a comprehensive hallucination taxonomy. arXiv. https://arxiv.org/abs/2510.19318

Zhang, C., Wang, H., & Meng, H. (2025). Hallucination detection and evaluation of large language model. arXiv. https://arxiv.org/abs/2512.22416

Zhang, H., Anjum, S., Fan, H., Zheng, W., Huang, Y., & Feng, Y. (2025). Poly-FEVER: A multilingual fact verification benchmark for hallucination detection in large language models. arXiv. https://arxiv.org/abs/2503.16541
