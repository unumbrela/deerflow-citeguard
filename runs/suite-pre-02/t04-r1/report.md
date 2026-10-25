# Systematic Literature Review: Hallucination Detection in Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "hallucination detection", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on hallucination detection in large language models published within the last two years. The surveyed literature reveals a rapidly evolving field characterized by diverse methodological approaches ranging from theoretical impossibility analyses to practical benchmarking frameworks. Collectively, these papers demonstrate that hallucination detection remains a fundamentally challenging problem, with performance highly dependent on task type, model access level, and computational resources. Recent work emphasizes standardization of evaluation benchmarks, efficiency improvements through adaptive sampling, domain-specific solutions for high-stakes applications like medicine, and theoretical understanding of detection feasibility. The field shows strong convergence on the need for standardized evaluation protocols and the importance of expert-labeled feedback for training effective detectors.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "hallucination detection", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmarking and Standardization

A prominent theme across recent work is the recognition that hallucination detection research suffers from inconsistent evaluation protocols, making cross-method comparisons difficult. Li et al. (2026) directly address this challenge with OpenHalDet, a unified benchmark that standardizes the entire evaluation pipeline from prompt construction through metric computation. Their framework supports heterogeneous detector families under black-box, gray-box, and white-box access settings, enabling systematic comparison of different detection paradigms. Similarly, Faujdar and Kadvani (2026) conduct comprehensive benchmarking of lightweight detection methods across question answering, dialogue, and summarization tasks, revealing that detection performance varies dramatically by task type. These benchmarking efforts collectively highlight that reported detector performance is often difficult to compare, reproduce, and generalize beyond specific experimental settings, and they provide the infrastructure needed for more rigorous evaluation.

### Theme 2: Efficiency and Adaptive Methods

Computational efficiency emerges as a critical concern, particularly for methods relying on multiple sampling passes. Sun et al. (2026) propose an Adaptive Bayesian Estimation framework that dynamically adjusts sampling requirements based on observed uncertainty, achieving comparable detection performance with approximately 50% fewer samples than fixed-budget approaches. Their method delivers an average AUROC improvement of 12.6% under the same sampling budget, demonstrating that intelligent sampling strategies can substantially reduce computational costs without sacrificing accuracy. This efficiency focus reflects growing recognition that hallucination detection methods must be practical for real-world deployment, not just theoretically sound.

### Theme 3: Domain-Specific Solutions

The literature increasingly recognizes that hallucination detection must be tailored to specific domains, particularly high-stakes applications. Lamarche et al. (2025) present MedHal, a large-scale synthetic dataset specifically designed for medical hallucination detection, demonstrating that general-purpose methods face significant limitations when applied to specialized medical domains. Their baseline model trained on MedHal shows improvements over general-purpose approaches, highlighting that domain-specific training data and evaluation benchmarks are essential for reliable detection in critical applications where errors can directly affect patient outcomes.

### Theme 4: Theoretical Foundations

Beyond practical methods, recent work provides important theoretical insights into the fundamental limits of hallucination detection. Karbasi et al. (2025) establish an equivalence between hallucination detection and the classical problem of language identification, proving that automated detection is fundamentally impossible when trained only on positive (correct) examples. However, they show that detection becomes possible for all countable language collections when using expert-labeled feedback with both positive and negative examples. This theoretical work provides rigorous justification for feedback-based methods like reinforcement learning with human feedback (RLHF) and highlights the essential role of expert-labeled negative examples in training effective detectors.

### Theme 5: Model-Internal Approaches

Several papers explore detection methods that leverage access to model internals, achieving state-of-the-art performance through sophisticated analysis of hidden representations. Hu et al. (2025) propose HARP, which decomposes the hidden state space into semantic and reasoning subspaces using singular value decomposition on the Unembedding layer parameters, achieving an AUROC of 92.8% on TriviaQA. Liu et al. (2026) reframe hallucination detection as an out-of-distribution detection problem, treating next-token prediction as classification and applying OOD techniques with modifications for LLM structural differences. These internal approaches demonstrate superior performance but require white-box access to model parameters, limiting their applicability to proprietary or closed-source models.

### Theme 6: Black-Box and Resource-Constrained Methods

Complementing white-box approaches, significant work addresses detection in resource-constrained or black-box settings. Oblovatny et al. (2025) introduce a method based on probabilistic distances between prompt and response token embeddings specifically for RAG systems, achieving competitive performance while remaining unsupervised. Lee et al. (2025) propose sampling future contexts based on the observation that hallucinations tend to persist once introduced, demonstrating improvements across multiple detection methods for black-box generators. Faujdar and Kadvani (2026) systematically evaluate lightweight CPU-feasible methods, finding that ensemble approaches combining semantic similarity and NLI achieve strong performance on QA and dialogue tasks, though summarization remains challenging.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several key points. First, multiple papers emphasize that hallucination detection performance is highly task-dependent, with question answering consistently showing better detection rates than summarization (Faujdar & Kadvani, 2026; Li et al., 2026). Second, there is broad consensus that standardized evaluation frameworks are essential for meaningful progress, with multiple papers calling for or providing benchmarking infrastructure (Li et al., 2026; Faujdar & Kadvani, 2026). Third, papers across methodological approaches agree that computational efficiency is a critical practical concern, particularly for methods requiring multiple sampling passes (Sun et al., 2026; Lee et al., 2025). Finally, the literature converges on the importance of domain-specific solutions, particularly for high-stakes applications like medicine (Lamarche et al., 2025).

**Disagreements**: The literature reveals tension between approaches requiring model access and those designed for black-box settings. White-box methods like HARP (Hu et al., 2025) and OOD-based detection (Liu et al., 2026) achieve superior performance but are inapplicable to proprietary models. In contrast, black-box methods (Lee et al., 2025; Oblovatny et al., 2025) sacrifice some accuracy for broader applicability. Additionally, there is implicit disagreement about the role of synthetic versus real data, with MedHal (Lamarche et al., 2025) advocating synthetic datasets while other work relies on naturally occurring hallucinations. The theoretical impossibility results (Karbasi et al., 2025) also create tension with practical approaches that assume detection is feasible without extensive negative training examples.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, summarization remains a persistent challenge across all detection methods, with even the best lightweight approaches achieving near-chance performance without substantial computational investment (Faujdar & Kadvani, 2026). Second, most methods are evaluated primarily on question answering datasets, with limited validation on dialogue, reasoning, or creative generation tasks. Third, domain-specific detection beyond medicine remains underexplored, despite clear evidence that general-purpose methods struggle in specialized domains. Fourth, the theoretical impossibility results (Karbasi et al., 2025) raise questions about the scalability of methods that rely on limited negative examples. Fifth, most papers acknowledge limitations in their evaluation scope, with few methods tested across diverse model architectures, sizes, or training regimes. Finally, the field lacks longitudinal studies examining how detection methods generalize to future model generations with different architectures or training objectives.

## Per-Paper Annotations

### Cheng et al. (2026)

**Research question**: How can semantic entropy-based hallucination detection be made computationally efficient by adapting sampling budgets to query complexity rather than using fixed sampling?
**Methodology**: Proposes an Adaptive Bayesian Estimation framework for Semantic Entropy with Guided Semantic Exploration that dynamically adjusts sampling requirements based on observed uncertainty using a hierarchical Bayesian framework with variance-based thresholds for termination.
**Key findings**:
- Requires approximately 50% fewer samples to achieve comparable detection performance in low-budget scenarios
- Delivers an average AUROC improvement of 12.6% under the same sampling budget
- Hierarchical Bayesian framework enables dynamic control of sampling iterations
- Perturbation-based importance sampling systematically explores the semantic space
- Extensive experiments on four QA datasets demonstrate superior performance with significant efficiency gains
**Limitations**: The method's effectiveness depends on the quality of Bayesian uncertainty estimates; performance on tasks beyond QA datasets is not addressed.

### Faujdar and Kadvani (2026)

**Research question**: How well can hallucination detection perform using only lightweight, CPU-feasible methods without GPU-intensive inference or proprietary API access?
**Methodology**: Benchmarks four lightweight detectors (ROUGE-L, semantic similarity, BERTScore, and NLI-based detector) plus a score-level ensemble across all three HaluEval tasks with calibration on validation split and bootstrap confidence intervals.
**Key findings**:
- Similarity-NLI ensemble is the most consistent method but performance is highly task-dependent
- Best performance on QA (F1=0.792, AUC-ROC=0.873) and dialogue (F1=0.694, AUC-ROC=0.749)
- All methods perform near chance on summarization with single-pass design
- Increasing premise budget and sentence-level chunk aggregation improves summarization performance
- Summarization remains the hardest task even with optimizations
**Limitations**: Summarization remains challenging; improved sentence-level aggregation comes at approximately 20x inference cost.

### Hu et al. (2025)

**Research question**: How can hallucinations in LLMs be detected by disentangling semantic and reasoning information in the model's hidden states?
**Methodology**: Proposes HARP framework that decomposes the hidden state space into semantic and reasoning subspaces using SVD on Unembedding layer parameters, then projects hidden states onto reasoning subspace basis vectors.
**Key findings**:
- Hidden state space can be decomposed into semantic and reasoning subspaces
- Unembedding layer can disentangle subspaces via SVD to obtain basis vectors
- Feature dimension reduced to approximately 5% of original while filtering noise
- Achieves AUROC of 92.8% on TriviaQA, outperforming previous best by 7.5%
- Demonstrates enhanced robustness across multiple datasets
**Limitations**: Requires access to model internals, limiting applicability to black-box models.

### Karbasi et al. (2025)

**Research question**: Is automated hallucination detection in LLMs theoretically possible under different training regimes?
**Methodology**: Introduces theoretical framework based on Gold-Angluin language identification, establishes equivalence between hallucination detection and language identification, analyzes feasibility under different training conditions.
**Key findings**:
- Hallucination detection is theoretically equivalent to language identification
- Detection is impossible when trained only on positive examples for most language collections
- Detection becomes possible with expert-labeled feedback including negative examples
- Provides theoretical justification for feedback-based methods like RLHF
- Highlights essential role of expert-labeled negative examples
**Limitations**: Theoretical framework assumes countable language collections; practical implementation details not addressed.

### Lamarche et al. (2025)

**Research question**: How can hallucination detection be improved for medical texts where errors can directly affect patient outcomes?
**Methodology**: Presents MedHal, a large-scale synthetic dataset for medical hallucination detection incorporating diverse medical text sources and tasks, then trains and evaluates baseline model.
**Key findings**:
- General-purpose methods face significant limitations in medical domains
- MedHal provides substantial training data for medical hallucination detection
- Baseline model shows improvements over general-purpose approaches
- Dataset covers both intrinsic and extrinsic hallucinations
- Enables efficient evaluation while reducing reliance on expert review
**Limitations**: Synthetic dataset may not fully capture real-world medical hallucination complexity.

### Lee et al. (2025)

**Research question**: How can hallucinations be detected in black-box LLM generators without access to internal model states?
**Methodology**: Proposes sampling future contexts based on observation that hallucinations tend to persist, then integrates sampled contexts with existing sampling-based detection methods.
**Key findings**:
- Hallucinations tend to persist once introduced in generated text
- Sampled future contexts provide valuable clues for detection
- Sampling approach can be integrated with various existing methods
- Demonstrates performance improvements across multiple methods
- Enables detection for black-box generators without model access
**Limitations**: Requires multiple sampling passes increasing computational cost and latency.

### Li et al. (2026)

**Research question**: How can hallucination detection be evaluated consistently and reproducibly across diverse generation scenarios, models, and detector types?
**Methodology**: Introduces OpenHalDet, a unified benchmark standardizing the entire evaluation pipeline from prompt construction through metric computation, supporting heterogeneous detector families.
**Key findings**:
- Existing evaluations face inconsistent configuration and limited domain coverage
- OpenHalDet enables controlled comparison across detector families and access settings
- Provides systematic view of detection paradigm behavior in LLM applications
- Released as open and extensible codebase for reproducible evaluation
- Supports black-box, gray-box, and white-box detection methods
**Limitations**: Benchmark validity depends on truthfulness annotation quality.

### Li et al. (2025)

**Research question**: How can the scarcity of well-labeled datasets for hallucination detection be addressed without additional human annotations?
**Methodology**: Introduces PALE framework using prompt-guided data augmentation to generate truthful and hallucinated training data, with Contrastive Mahalanobis Score for evaluating intermediate embeddings.
**Key findings**:
- Prompt-guided responses can generate training data at low cost
- CM Score captures structure of truthful and hallucinated data distributions
- Framework requires no additional human annotations
- Outperforms competitive baseline by 6.55%
- Demonstrates practicality for real-world applications
**Limitations**: Quality depends on prompt design; may not generalize across all domains.

### Liu et al. (2026)

**Research question**: Can out-of-distribution detection techniques be adapted to improve hallucination detection, particularly for reasoning tasks?
**Methodology**: Reframes hallucination detection as OOD detection by treating next-token prediction as classification, applies OOD techniques with modifications for LLM structural differences.
**Key findings**:
- OOD-based approaches can be adapted for hallucination detection
- Achieves training-free detection without labeled training data
- Operates on single samples rather than requiring multiple generations
- Achieves strong accuracy on reasoning tasks where existing methods struggle
- Reframing provides scalable pathway for language model safety
**Limitations**: Requires structural modifications for LLM differences; performance on non-reasoning tasks may vary.

### Oblovatny et al. (2025)

**Research question**: How can hallucination detection be improved specifically for Retrieval-Augmented Generation systems where most existing methods are not designed?
**Methodology**: Introduces method based on estimating probabilistic distances between prompt and response token embeddings, examining geometric structure of token hidden states.
**Key findings**:
- Achieves state-of-the-art or competitive performance
- Demonstrates transferability from NLI to hallucination detection
- Operates as fully unsupervised and efficient method
- Suitable for long sequences
- Specifically addresses RAG system limitations
**Limitations**: Performance may vary across different RAG architectures and domains.

## References

Cheng, Q., Li, X., He, X., Cheng, A., Ji, X., Lu, H., Huang, R., & Hu, Q. (2026). Efficient hallucination detection: Adaptive Bayesian Estimation of Semantic Entropy with Guided Semantic Exploration. arXiv. https://arxiv.org/abs/2603.22812

Faujdar, K., & Kadvani, S. (2026). How far can you get without a GPU? A systematic benchmark of lightweight hallucination detection across Question Answering, Dialogue, and Summarisation. arXiv. https://arxiv.org/abs/2606.29809

Hu, J., Tu, G., Cheng, S., Li, J., Wang, J., Chen, R., Zhou, Z., & Shan, D. (2025). HARP: Hallucination detection via reasoning subspace projection. arXiv. https://arxiv.org/abs/2509.11536

Karbasi, A., Montasser, O., Sous, J., & Velegkas, G. (2025). (Im)possibility of automated hallucination detection in Large Language Models. arXiv. https://arxiv.org/abs/2504.17004

Lamarche, F., Mehenni, G., Fard, N. E., Rios-Ibacache, O., Wang, L. M., Kildea, J., & Zouaq, A. (2025). MedHal: A synthetic dataset for medical hallucination detection. arXiv. https://arxiv.org/abs/2504.08596

Lee, J., Park, C., Jo, H., Kim, J., Park, J., & Yoo, K. M. (2025). Enhancing hallucination detection via future context. arXiv. https://arxiv.org/abs/2507.20546

Li, W., Zhang, Z., Jiang, D., & Lan, X. (2025). Bolster hallucination detection via prompt-guided data augmentation. arXiv. https://arxiv.org/abs/2510.15977

Li, X., Fang, Z., Deng, Y., Luo, J., Ma, H., Oh, C., Shi, Z., Ye, S., Wang, H., Chen, S.-L., Luo, Y., Yang, M., Du, S., Li, S., & Chen, L. (2026). OpenHalDet: A unified benchmark for hallucination detection across diverse generation scenarios. arXiv. https://arxiv.org/abs/2606.06959

Liu, L., Pourreza, R., Jian, Y., Qin, Y., & Memisevic, R. (2026). From out-of-distribution detection to hallucination detection: A geometric view. arXiv. https://arxiv.org/abs/2602.07253

Oblovatny, R., Kuleshova, A., Polev, K., & Zaytsev, A. (2025). Probabilistic distances-based hallucination detection in LLMs with RAG. arXiv. https://arxiv.org/abs/2506.09886
