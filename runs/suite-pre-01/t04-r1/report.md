# Systematic Literature Review: Hallucination Detection in Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "hallucination detection", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Hallucination detection in large language models has emerged as a critical research area for ensuring the reliability and trustworthiness of AI systems. The 10 papers surveyed (2024-2026) reveal a rapidly evolving field characterized by diverse methodological approaches spanning benchmark development, embedding-based detection, semantic entropy methods, lightweight CPU-feasible techniques, domain-specific solutions for medical applications, theoretical feasibility analysis, data augmentation strategies, future context sampling, and multilingual fine-grained detection. Recent work demonstrates significant progress in detection accuracy, with methods achieving AUROC scores up to 92.8% on standard benchmarks, while also addressing practical concerns including computational efficiency, resource constraints, and domain specialization. However, substantial challenges remain in generalizing detection methods across tasks, particularly for summarization, and in developing theoretically grounded approaches that do not rely exclusively on expert-labeled feedback.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "hallucination detection", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmark Development and Standardized Evaluation

A prominent direction in recent hallucination detection research focuses on creating unified benchmarks and standardized evaluation frameworks. Li et al. (2026) introduced OpenHalDet, addressing the critical challenge of inconsistent inference configuration and evaluation across diverse generation scenarios. This benchmark standardizes the entire pipeline from prompt construction to metric computation, supporting heterogeneous detector families under black-box, gray-box, and white-box access settings. Similarly, Faujdar and Kadvani (2026) conducted systematic benchmarking of lightweight detection methods across question answering, dialogue, and summarization tasks using the HaluEval benchmark, revealing significant task-dependent performance variations. These benchmarking efforts enable controlled comparison and provide systematic views of how different detection paradigms behave across diverse LLM applications, addressing reproducibility concerns that have plagued the field.

### Theme 2: Embedding-Based and Internal State Analysis

Multiple papers leverage internal model representations for hallucination detection, examining token embeddings and hidden states to extract factuality signals. Oblovatny et al. (2025) developed a method based on probabilistic distances between distributions of prompt token embeddings and response token embeddings, specifically designed for RAG systems. This approach examines the geometric structure of token hidden states to reliably extract factuality signals while remaining efficient for long sequences. Hu et al. (2025) proposed HARP, which decomposes the hidden state space into semantic and reasoning subspaces using Singular Value Decomposition on Unembedding layer parameters, then projects hidden states onto the reasoning subspace basis vectors as features. By reducing feature dimension to approximately 5% of the original while filtering noise, HARP achieves state-of-the-art performance with AUROC of 92.8% on TriviaQA. Li et al. (2025) similarly modeled distributions of truthful and hallucinated data in the activation space using the Contrastive Mahalanobis Score with matrix decomposition to capture underlying structure.

### Theme 3: Semantic Entropy and Sampling-Based Approaches

Sampling-based methods that quantify semantic inconsistency across multiple generated responses represent another major approach. Sun et al. (2026) addressed computational inefficiency in fixed sampling budget approaches by proposing Adaptive Bayesian Estimation for Semantic Entropy with Guided Semantic Exploration. This framework employs hierarchical Bayesian modeling to dynamically adjust sampling requirements based on observed uncertainty, using variance-based thresholds to terminate generation once sufficient certainty is achieved. Their method requires approximately 50% fewer samples in low-budget scenarios while delivering an average AUROC improvement of 12.6% under the same sampling budget across four QA datasets. Lee et al. (2025) extended sampling-based approaches by introducing future context sampling, leveraging the observation that hallucinations tend to persist once introduced. This framework is particularly valuable for black-box generators where internal states are not accessible, and can be effectively integrated with various existing sampling-based detection methods.

### Theme 4: Lightweight and Resource-Efficient Detection

Addressing practical deployment constraints, several papers investigate hallucination detection methods feasible for resource-constrained environments. Faujdar and Kadvani (2026) systematically benchmarked four lightweight detectors (ROUGE-L, semantic similarity, BERTScore, and NLI based on FEVER-trained DeBERTa) plus an ensemble, using only CPU-feasible computation without GPU-intensive inference or proprietary API access. Their findings reveal that the similarity-NLI ensemble achieves strong performance on QA (F1=0.792, AUC-ROC=0.873) and dialogue (F1=0.694, AUC-ROC=0.749), though summarization remains challenging with all methods performing near chance level in single-pass design. However, they demonstrated that sentence-level chunk aggregation reaches 0.683 AUC-ROC on summarization while remaining on CPU, showing that lightweight detection is not intrinsically unsuited to difficult tasks but requires careful design adjustments. This line of work is essential for democratizing access to hallucination detection capabilities beyond well-resourced institutions.

### Theme 5: Domain-Specific and Multilingual Approaches

Recognition that hallucination detection must be adapted to specific domains and languages has motivated specialized solutions. Lamarche et al. (2025) presented MedHal, a large-scale synthetic dataset specifically designed for medical hallucination detection, addressing the serious risks posed by hallucinations in medical contexts where errors can directly affect patient outcomes. MedHal incorporates diverse medical text sources covering both intrinsic and extrinsic hallucinations, with baseline models trained on this dataset showing improvements over general-purpose approaches. Shen et al. (2024) introduced the first multilingual, fine-grained news headline hallucination detection dataset containing over 11,000 pairs in 5 languages, each annotated with detailed hallucination types by experts. They proposed language-dependent demonstration selection and coarse-to-fine prompting techniques to boost few-shot detection performance, moving beyond oversimplified English-only binary classification schemes. These domain-specific efforts acknowledge that hallucination characteristics and consequences vary substantially across application areas.

### Theme 6: Theoretical Foundations and Data Augmentation

Recent work has begun addressing fundamental theoretical questions about the feasibility of automated hallucination detection while developing practical strategies to overcome data scarcity. Karbasi et al. (2025) established a theoretical framework proving that hallucination detection is equivalent to the classical task of language identification, demonstrating that automated detection is fundamentally impossible when trained using only correct examples from the target language. However, they showed that expert-labeled feedback with both positive and negative examples makes hallucination detection possible for all countable language collections, providing theoretical justification for feedback-based methods like RLHF. Addressing the practical challenge of scarce well-labeled datasets, Li et al. (2025) introduced PALE, a framework leveraging prompt-guided responses from LLMs for data augmentation to generate both truthful and hallucinated training data at low cost without additional human annotations. Their Contrastive Mahalanobis Score achieved superior performance, outperforming competitive baselines by 6.55%.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong agreement on several points. First, all papers recognize hallucination detection as essential for reliable LLM deployment, with particular urgency in high-stakes domains like medicine and critical decision-making. Second, multiple papers converge on the finding that detection performance is highly task-dependent, with question answering consistently showing stronger results than summarization across different methodological approaches (Faujdar & Kadvani, 2026; Sun et al., 2026). Third, there is consensus that internal model signals—whether token embeddings, hidden states, or activation space distributions—provide valuable information for detection when accessible (Oblovatny et al., 2025; Hu et al., 2025; Li et al., 2025). Fourth, the literature agrees that standardized evaluation frameworks are necessary for meaningful comparison and reproducibility (Li et al., 2026; Faujdar & Kadvani, 2026).

**Disagreements**: The literature reveals tension regarding the fundamental feasibility of automated hallucination detection. Karbasi et al. (2025) prove theoretically that detection is impossible without expert-labeled negative examples, while numerous other papers demonstrate strong empirical performance using unsupervised or semi-supervised approaches (Oblovatny et al., 2025; Sun et al., 2026; Lee et al., 2025). This apparent contradiction may reflect differences between worst-case theoretical bounds and average-case empirical performance on specific benchmarks. Additionally, there is disagreement about the viability of lightweight methods for summarization tasks: Faujdar and Kadvani (2026) initially found near-chance performance but demonstrated substantial improvement through sentence-level chunk aggregation, suggesting the limitation is methodological rather than intrinsic, whereas other work implicitly treats summarization as inherently more challenging without proposing such solutions.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, the theoretical impossibility result (Karbasi et al., 2025) raises concerns about the generalizability of empirically successful methods—under what conditions do unsupervised detectors fail catastrophically, and can such failures be anticipated? Second, summarization remains substantially more challenging than QA or dialogue across all evaluated methods, with even the best lightweight approaches requiring twenty times more inference through sentence-level chunk aggregation (Faujdar & Kadvani, 2026); the fundamental sources of this difficulty require deeper investigation. Third, domain specialization is acknowledged as important (Lamarche et al., 2025; Shen et al., 2024), but only medical and news headline domains have dedicated datasets—critical areas like legal, financial, and scientific reasoning lack specialized detection resources. Fourth, multilingual capabilities remain limited to five languages in the largest dataset (Shen et al., 2024), leaving low-resource languages unsupported despite global LLM deployment. Fifth, most methods requiring internal model access cannot be applied to black-box commercial APIs, creating a capability gap between open and closed models. Finally, the reliance on expert-labeled feedback suggested by theoretical analysis (Karbasi et al., 2025) raises practical questions about annotation costs and scalability for real-world deployment.

## Per-Paper Annotations

### Bendersky et al. (2024)

**Research question**: How can fine-grained hallucination types in multilingual news headline generation be detected beyond oversimplified English-only classification schemes?
**Methodology**: Introduced first multilingual fine-grained hallucination detection dataset (11k+ pairs in 5 languages with expert annotations), then tested supervised fine-tuning and in-context learning with novel techniques including language-dependent demonstration selection and coarse-to-fine prompting.
**Key findings**:
- Created first multilingual, fine-grained news headline hallucination dataset with over 11,000 pairs in 5 languages
- Each pair annotated with detailed hallucination types by experts, enabling nuanced detection beyond binary classification
- Language-dependent demonstration selection improves few-shot hallucination detection performance
- Coarse-to-fine prompting technique boosts example-F1 metric in in-context learning settings
- Dataset reveals significant challenges in multilingual fine-grained hallucination detection
**Limitations**: Limited to news headline domain and 5 languages, which may not generalize to other content types or low-resource languages; supervised approaches require substantial labeled data which may be costly to obtain for additional languages.

### Karbasi et al. (2025)

**Research question**: Is automated hallucination detection in LLMs theoretically feasible?
**Methodology**: Introduced a theoretical framework based on the Gold-Angluin framework for language identification, establishing equivalence between hallucination detection and language identification tasks.
**Key findings**:
- Hallucination detection is theoretically equivalent to the classical task of language identification
- Automated hallucination detection is fundamentally impossible when trained using only correct examples from the target language
- Expert-labeled feedback (both positive and negative examples) makes hallucination detection possible for all countable language collections
- Results provide theoretical justification for feedback-based methods like RLHF
- Highlights the essential role of negative examples in training hallucination detectors
**Limitations**: This is a theoretical analysis rather than an empirical study; the framework assumes countable language collections and may not directly address practical implementation challenges in real-world LLM deployment scenarios.

### Lamarche et al. (2025)

**Research question**: How can hallucination detection be improved for medical contexts where errors can directly affect patient outcomes and current methods face significant limitations in specialized domains?
**Methodology**: Presented MedHal, a large-scale synthetic dataset specifically designed for medical hallucination detection, incorporating diverse medical text sources and tasks covering both intrinsic and extrinsic hallucinations, with sufficient volume for training detection models; demonstrates utility by training and evaluating a baseline medical hallucination detection model.
**Key findings**:
- Current hallucination detection methods face significant limitations when applied to specialized domains like medicine
- MedHal addresses this by incorporating diverse medical text sources and tasks with substantial data volume suitable for training
- The baseline model trained on MedHal shows improvements over general-purpose hallucination detection approaches
- The resource enables more efficient evaluation and training of medical text generation systems
- Reduces reliance on costly expert review, potentially accelerating medical AI research development
**Limitations**: As a synthetic dataset, MedHal may not fully capture the complexity and nuances of real-world medical hallucinations that occur in clinical practice; the baseline model demonstration suggests further work is needed to validate performance on authentic medical texts and across diverse medical specialties.

### Li et al. (2025)

**Research question**: How can the scarcity of well-labeled datasets for hallucination detection be addressed without additional human annotations?
**Methodology**: Introduced PALE framework that uses prompt-guided responses from LLMs for data augmentation to generate both truthful and hallucinated data, plus Contrastive Mahalanobis Score (CM Score) with matrix decomposition for evaluating sparse intermediate embeddings.
**Key findings**:
- Prompt-guided data augmentation can generate both truthful and hallucinated training data at relatively low cost
- CM Score based on modeling distributions in activation space effectively evaluates truthfulness of intermediate embeddings
- Matrix decomposition approach accurately captures underlying structure of truthful and hallucinated data distributions
- Framework achieves superior performance without requiring additional human annotations
- Outperforms competitive baseline by 6.55% margin
**Limitations**: The quality of augmented data depends on prompt design effectiveness; the approach assumes LLMs can reliably generate both truthful and hallucinated content under prompt guidance, which may vary across models and domains.

### Lee et al. (2025)

**Research question**: How can hallucinations be detected in black-box LLM generators without access to internal model states?
**Methodology**: Developed a hallucination detection framework for black-box generators by sampling future contexts, leveraging the observation that hallucinations tend to persist once introduced.
**Key findings**:
- Hallucinations, once introduced in LLM outputs, tend to persist in subsequent generated content
- Sampled future contexts provide valuable clues for detecting hallucinations
- The sampling approach can be effectively integrated with various existing sampling-based detection methods
- Demonstrates performance improvements across multiple methods using the proposed sampling approach
- Framework is applicable to black-box models where internal states are not accessible
**Limitations**: Requires multiple sampling passes which increases computational cost and latency; effectiveness depends on the persistence property of hallucinations which may not hold for all types of hallucinated content.

### Hu et al. (2025)

**Research question**: How can hallucinations in LLMs be detected by disentangling semantic and reasoning information in hidden states?
**Methodology**: Proposed HARP framework that decomposes the hidden state space into semantic and reasoning subspaces using SVD on Unembedding layer parameters, then projects hidden states onto reasoning subspace basis vectors as features for detection.
**Key findings**:
- LLM hidden state space can be decomposed into a direct sum of semantic subspace (linguistic expression) and reasoning subspace (internal reasoning processes)
- The Unembedding layer can disentangle these subspaces via Singular Value Decomposition
- Projection onto reasoning subspace reduces feature dimension to approximately 5% of original while filtering noise
- Achieves AUROC of 92.8% on TriviaQA, outperforming previous best method by 7.5%
- Demonstrates enhanced robustness across multiple datasets
**Limitations**: The approach depends on access to model internals (Unembedding layer parameters and hidden states), limiting applicability to black-box models; the theoretical decomposition may not generalize equally across all model architectures.

### Oblovatny et al. (2025)

**Research question**: How can hallucination detection be improved specifically for Retrieval-Augmented Generation (RAG) systems where most existing methods are not specifically designed?
**Methodology**: Introduced a hallucination detection method based on estimating distances between distributions of prompt token embeddings and language model response token embeddings, examining the geometric structure of token hidden states to extract factuality signals while remaining efficient for long sequences.
**Key findings**:
- The method achieves state-of-the-art or competitive performance in extensive experiments
- Demonstrates transferability from solving the Natural Language Inference (NLI) task to the hallucination detection task
- The approach is fully unsupervised and efficient with competitive performance on the final task
- The method remains friendly to long sequences, addressing a practical limitation of many alternatives
**Limitations**: The abstract does not explicitly acknowledge limitations; potential constraints may include performance on very short responses where embedding distributions are less informative, and dependency on quality of token embedding representations across different model architectures.

### Sun et al. (2026)

**Research question**: How can semantic entropy-based hallucination detection be made more computationally efficient by adapting sampling requirements to query complexity rather than using fixed sampling budgets?
**Methodology**: Proposed an Adaptive Bayesian Estimation framework for Semantic Entropy with Guided Semantic Exploration that employs a hierarchical Bayesian framework to model semantic distribution, enabling dynamic control of sampling iterations through variance-based thresholds, combined with a perturbation-based importance sampling strategy to systematically explore the semantic space.
**Key findings**:
- The method achieves superior hallucination detection performance with significant efficiency gains compared to fixed-budget approaches
- In low-budget scenarios, requires about 50% fewer samples to achieve comparable detection performance to existing methods
- Delivers an average AUROC improvement of 12.6% under the same sampling budget
- Extensive experiments demonstrate effectiveness across four QA datasets
- Dynamic adaptation successfully terminates generation once sufficient certainty is achieved
**Limitations**: The method was evaluated only on four QA datasets, which may limit generalizability to other task types such as dialogue, summarization, or creative generation; the Bayesian framework may introduce additional computational overhead per sample despite reducing total sample count.

### Li et al. (2026)

**Research question**: How can hallucination detection be evaluated consistently across diverse generation scenarios given the challenges of inconsistent inference configuration and limited domain coverage in existing evaluations?
**Methodology**: Introduced OpenHalDet, a unified benchmark that standardizes the evaluation pipeline from prompt construction and response generation to truthfulness annotation, detector scoring, and metric computation, supporting heterogeneous detector families under black-box, gray-box, and white-box access settings.
**Key findings**:
- Existing hallucination detection evaluations face two core challenges: inconsistent inference configuration/evaluation and limited coverage of downstream domains and tasks
- OpenHalDet enables controlled comparison of diverse detector families by bringing tasks, models, and detectors into a shared framework
- The benchmark provides a systematic view of how different detection paradigms behave across diverse LLM application scenarios
- OpenHalDet is released as an open and extensible codebase to facilitate reproducible evaluation and future development
**Limitations**: The abstract does not explicitly acknowledge limitations; potential constraints may include the scope of covered tasks and models, dependency on annotation quality for truthfulness labels, and generalizability beyond the benchmark's design choices.

### Faujdar and Kadvani (2026)

**Research question**: How well can hallucination detection perform using only lightweight, CPU-feasible methods without GPU-intensive inference, proprietary API calls, or white-box model access?
**Methodology**: Benchmarked four lightweight detectors (ROUGE-L, semantic similarity, BERTScore, and NLI based on FEVER-trained DeBERTa) plus a score-level ensemble across all three HaluEval benchmark tasks (QA, dialogue, summarisation), with calibration on held-out validation and bootstrap confidence intervals on 2,000 test instances per task.
**Key findings**:
- The similarity-NLI ensemble is the most consistent method across tasks
- Best performance achieved on QA (F1=0.792, AUC-ROC=0.873) and dialogue (F1=0.694, AUC-ROC=0.749), where NLI is the strongest standalone method
- On summarisation, all methods perform near chance level (AUC-ROC between 0.469 and 0.574) in single-pass design
- Raising premise budget from 800 to 1600 characters lifts summarisation AUC-ROC from 0.567 to 0.629
- Sentence-level chunk aggregation reaches 0.683 AUC-ROC on summarisation, demonstrating lightweight detection is not intrinsically unsuited to the task but requires design adjustments
**Limitations**: Summarisation remains by far the hardest task even with improvements; achieving better summarisation performance requires roughly twenty times the NLI inference cost through sentence-level chunk aggregation, which may offset some efficiency benefits of lightweight methods.

## References

Faujdar, K., & Kadvani, S. (2026). How far can you get without a GPU? A systematic benchmark of lightweight hallucination detection across question answering, dialogue, and summarisation. arXiv. https://arxiv.org/abs/2606.29809v2

Hu, J., Tu, G., Cheng, S., Li, J., Wang, J., Chen, R., Zhou, Z., & Shan, D. (2025). HARP: Hallucination detection via reasoning subspace projection. arXiv. https://arxiv.org/abs/2509.11536v2

Karbasi, A., Montasser, O., Sous, J., & Velegkas, G. (2025). (Im)possibility of automated hallucination detection in large language models. arXiv. https://arxiv.org/abs/2504.17004v2

Lamarche, F., Mehenni, G., Fard, N. E., Rios-Ibacache, O., Wang, L. M., Kildea, J., & Zouaq, A. (2025). MedHal: A synthetic dataset for medical hallucination detection. arXiv. https://arxiv.org/abs/2504.08596v4

Lee, J., Park, C., Jo, H., Kim, J., Park, J., & Yoo, K. M. (2025). Enhancing hallucination detection via future context. arXiv. https://arxiv.org/abs/2507.20546v2

Li, W., Zhang, Z., Jiang, D., & Lan, X. (2025). Bolster hallucination detection via prompt-guided data augmentation. arXiv. https://arxiv.org/abs/2510.15977v1

Li, X., Fang, Z., Deng, Y., Luo, J., Ma, H., Oh, C., Shi, Z., Ye, S., Wang, H., Chen, S.-L., Luo, Y., Yang, M., Du, S., Li, S., & Chen, L. (2026). OpenHalDet: A unified benchmark for hallucination detection across diverse generation scenarios. arXiv. https://arxiv.org/abs/2606.06959v1

Oblovatny, R., Kuleshova, A., Polev, K., & Zaytsev, A. (2025). Probabilistic distances-based hallucination detection in LLMs with RAG. arXiv. https://arxiv.org/abs/2506.09886v2

Shen, J., Liu, T., Liu, J., Qin, Z., Pavagadhi, J., Baumgartner, S., & Bendersky, M. (2024). Multilingual fine-grained news headline hallucination detection. arXiv. https://arxiv.org/abs/2407.15975v1

Sun, Q., Li, X., He, X., Cheng, A., Ji, X., Lu, H., Huang, R., & Hu, Q. (2026). Efficient hallucination detection: Adaptive Bayesian estimation of semantic entropy with guided semantic exploration. arXiv. https://arxiv.org/abs/2603.22812v1
