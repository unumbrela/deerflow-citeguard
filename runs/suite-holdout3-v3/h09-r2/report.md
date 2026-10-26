# Systematic Literature Review: Membership Inference Attacks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "membership inference attacks", category cs.CR, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers (2024-2026) on membership inference attacks (MIAs) in the security and privacy domain (cs.CR). The surveyed literature reveals that MIAs have evolved beyond traditional overfitting-based attacks to target emerging AI paradigms including federated learning, retrieval-augmented generation, video-language models, LoRA fine-tuning, and chat agent memory systems. A critical tension emerges in the field: while attack methodologies have grown increasingly sophisticated and domain-specific, recent work questions whether MIAs constitute genuine privacy threats under realistic conditions. The literature demonstrates that membership vulnerabilities persist even in non-overfitted models, driven by factors such as outlier samples and model architecture choices, necessitating targeted defensive strategies beyond conventional approaches.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "membership inference attacks", filtered to category cs.CR, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: MIAs Targeting Emerging AI Architectures

The surveyed literature demonstrates a clear trend toward attacking novel AI system architectures rather than traditional standalone models. Researchers have extended membership inference methodologies to federated learning systems (Bai et al., 2024), retrieval-augmented generation (Liu et al., 2024; Kulkarni et al., 2026), video large language models (Song et al., 2026), LoRA fine-tuned language models (Ran et al., 2025), and chat agent memory systems (Chen et al., 2026). This architectural diversification reflects the field's response to the rapid deployment of AI systems in production environments, where privacy vulnerabilities may differ substantially from classical machine learning settings. Each domain introduces unique attack surfaces: federated learning's distributed training paradigm, RAG systems' document retrieval mechanisms, VideoLLMs' multimodal generation patterns, and chat agents' persistent memory stores all create distinct membership signals that attackers can exploit.

### Theme 2: Attack Methodology Innovation

Recent work has introduced sophisticated attack frameworks that move beyond simple confidence-score or loss-based heuristics. Du et al. (2025) proposed Cascading Membership Inference Attack (CMIA) and Proxy Membership Inference Attack (PMIA), which exploit membership dependencies between instances through conditional shadow training and proxy selection strategies. Liu et al. (2024) developed a mask-based approach for RAG systems that employs word masking and prediction accuracy analysis to determine membership. Song et al. (2026) introduced temperature-perturbed generation coupled with video-aware difficulty features for VideoLLM attacks. Kulkarni et al. (2026) proposed a weighted-averaging attack scheme that operates without requiring a reference model. Ran et al. (2025) demonstrated that leveraging pre-trained models as references significantly increases information leakage in LoRA fine-tuned models. Chen et al. (2026) developed Multi-Recall Memory MIA (MRMMIA) utilizing multiple recall probes across black-box, gray-box, and white-box settings. These methodological advances reflect a maturing field where attackers systematically analyze the unique properties of each target system.

### Theme 3: Privacy Risk Assessment and Critique

A critical counter-narrative emerges in the literature questioning the actual privacy threat posed by MIAs under realistic conditions. Jebreel et al. (2026) conducted a critical review proposing an evaluation framework that defines conditions under which MIAs constitute genuine privacy threats, concluding that under realistic conditions, MIAs represent weak privacy threats. They argue that relying on MIAs as a privacy metric can lead to overestimation of privacy risk and unnecessary sacrifices in model utility from employing overly strong defenses. Khalil et al. (2025) similarly found that even non-overfitted models can leak information about only a small subset of training data, typically outliers within their classes. This critical perspective challenges the field to reconsider whether the substantial research investment in MIA development corresponds to proportionate actual privacy risks, or whether the community has conflated attack success metrics with meaningful privacy breaches.

### Theme 4: Ensemble and Benchmark Approaches

Recognizing that no single attack method dominates across different architectures and domains, recent work has adopted ensemble and comprehensive benchmarking strategies. Ward et al. (2025) conducted the largest synthetic data privacy benchmark to date, studying membership inference attacks as a decision-theoretic problem under uncertainty. Their key finding that no MIA constitutes a strictly dominant strategy led to the proposal of ensemble MIAs built on individual attacks, which offer empirically more robust, regret-minimizing strategies. Bai et al. (2024) similarly took a survey approach in federated learning, systematically categorizing attacks and defenses to provide a comprehensive taxonomy. Ran et al. (2025) introduced LoRA-Leak, a holistic evaluation framework incorporating fifteen membership inference attacks to comprehensively assess LoRA fine-tuned model vulnerabilities. This shift toward ensemble and benchmark methodologies reflects the field's recognition that privacy assessment requires multi-faceted evaluation rather than reliance on any single attack vector.

### Theme 5: Defensive Strategies and Mitigation

The literature identifies several defensive strategies that show promise in mitigating membership inference risks. Ran et al. (2025) found that only dropout and excluding specific language model layers during fine-tuning effectively mitigate MIA risks while maintaining utility in LoRA settings. Kulkarni et al. (2026) demonstrated that an existing ensemble prompting defense substantially mitigates privacy leakage from their proposed weighted-averaging attack. Khalil et al. (2025) proposed targeted defensive strategies to protect vulnerable samples (often outliers) and enhance privacy-preserving capabilities. Bai et al. (2024) provided a systematic overview of various countermeasures in federated learning. However, the critical review by Jebreel et al. (2026) cautions against overly strong defenses that sacrifice model utility based on inflated privacy risk estimates from MIA metrics. This tension between effective defense and practical utility remains a central challenge in the field.

## Convergences and Disagreements

**Convergences**: Multiple papers agree that membership inference vulnerabilities persist beyond traditional overfitting scenarios (Khalil et al., 2025; Ran et al., 2025). There is consensus that emerging AI architectures introduce novel attack surfaces requiring domain-specific methodologies (Bai et al., 2024; Liu et al., 2024; Song et al., 2026; Chen et al., 2026). The literature converges on the finding that no single attack method dominates across different settings, necessitating ensemble or adaptive approaches (Ward et al., 2025; Du et al., 2025).

**Disagreements**: A significant tension exists between papers emphasizing the severity of MIA privacy threats and those questioning their practical impact. While most papers frame MIAs as serious privacy concerns requiring mitigation, Jebreel et al. (2026) argue that MIAs represent weak privacy threats under realistic conditions and that the community may be overestimating risks. This disagreement reflects a fundamental question about whether attack success metrics (AUC, accuracy) translate to meaningful privacy breaches in production systems. Additionally, there is implicit disagreement about the appropriate strength of defensive responses: some papers advocate for robust defenses (Ran et al., 2025; Khalil et al., 2025), while Jebreel et al. (2026) caution against unnecessary utility sacrifices from overly strong defenses.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, many papers do not explicitly state limitations in their abstracts (Kulkarni et al., 2026; Ran et al., 2025; Jebreel et al., 2026; Khalil et al., 2025; Chen et al., 2026), suggesting a need for more transparent discussion of methodological constraints. Second, the critical review by Jebreel et al. (2026) highlights that the field lacks consensus on what constitutes a meaningful privacy threat versus a successful attack metric — this conceptual gap requires resolution. Third, several attacks achieve only moderate accuracy (e.g., Song et al., 2026 report 0.63 accuracy), raising questions about practical exploitability that are not fully addressed. Fourth, computational overhead and scalability of advanced attacks (CMIA's conditional shadow training, ensemble methods) are not detailed, limiting understanding of real-world feasibility. Fifth, the literature focuses heavily on attack development with less emphasis on systematically validated defensive frameworks that balance privacy and utility. Finally, as a survey-based review, this synthesis relies on abstract-level metadata; full-paper analysis would be needed to extract more nuanced methodological details and experimental validation.

## Per-Paper Annotations

### Bai et al. (2024)

**Research question**: What membership inference attacks and defense strategies exist in federated learning, and how can they be systematically categorized?

**Methodology**: The paper conducts a comprehensive survey by categorizing and summarizing membership inference attacks and their corresponding defense strategies based on their characteristics in the federated learning setting, introducing a taxonomy of existing attack research with systematic overview of countermeasures.

**Key findings**:
- Federated learning faces privacy vulnerabilities despite only sharing model updates rather than raw training data
- Membership inference attacks can determine whether a specific example is part of the training set, compromising sensitive information
- The survey categorizes membership inference attacks and defense strategies based on their characteristics in federated learning
- A unique taxonomy of existing attack research is introduced with systematic overview of countermeasures
- The paper identifies key future research directions for advancing the field

**Limitations**: As a survey paper, it synthesizes existing research rather than presenting new experimental results; specific limitations of the surveyed approaches are analyzed but not empirically validated.

### Song et al. (2026)

**Research question**: Can an external auditor determine whether a particular video was used during training of Video Large Language Models through black-box membership inference attacks?

**Methodology**: The paper presents a black-box membership inference attack targeting VideoLLMs that couples temperature-perturbed generation with video-aware difficulty features, querying the target model at low and high temperatures and measuring semantic drift between resulting texts to detect membership signals.

**Key findings**:
- VideoLLMs are vulnerable to black-box membership inference attacks despite the challenge that auditors observe only generated text
- Member samples tend to induce sharper, more brittle generation behavior across decoding temperatures
- The attack achieves a member inference AUC of 0.68 and accuracy of 0.63 against LLaVA-Video-7B-Qwen2-Video-Only
- The membership signal is entangled with video-specific factors such as motion complexity and temporal span
- There is an urgent need for the community to systematically evaluate and mitigate privacy risks in VideoLLMs

**Limitations**: The attack achieves moderate accuracy (0.63) and AUC (0.68), indicating the challenge of extracting membership signals from video-specific factors; evaluation is limited to one model architecture.

### Du et al. (2025)

**Research question**: How can membership inference attacks be improved by exploiting membership dependencies between instances in adaptive and non-adaptive settings?

**Methodology**: The paper proposes two attack frameworks: Cascading Membership Inference Attack (CMIA) for the adaptive setting that incorporates membership dependencies via conditional shadow training, and Proxy Membership Inference Attack (PMIA) for the non-adaptive setting that employs a proxy selection strategy to identify samples with similar behaviors to the query instance, with theoretical analyses for both attacks.

**Key findings**:
- Exploiting membership dependencies between instances can boost membership inference performance in the adaptive setting
- CMIA incorporates membership dependencies via conditional shadow training to improve attack effectiveness
- PMIA employs proxy selection to identify samples with similar behaviors and uses their behaviors in shadow models for membership posterior odds testing
- Both CMIA and PMIA substantially outperform existing MIAs, particularly in the low false-positive regime
- The low false-positive regime is crucial for evaluating privacy risks in machine learning models

**Limitations**: The paper provides theoretical analyses and experimental validation, but specific limitations regarding computational overhead of conditional shadow training or proxy selection are not detailed in the abstract.

### Ward et al. (2025)

**Research question**: How can adversaries choose effective membership inference attack methods when no single method dominates across different model architectures and dataset domains?

**Methodology**: The paper conducts the largest synthetic data privacy benchmark to date, studying membership inference attacks as a decision theoretic problem under uncertainty, and based on findings that no MIA constitutes a strictly dominant strategy, proposes ensemble MIAs built on individual attacks.

**Key findings**:
- No membership inference attack constitutes a strictly dominant strategy across various model architectures and dataset domains
- In realistic threat scenarios, adversaries must choose a single method without guarantee it will be the empirically highest performing option
- Unsupervised ensembles built on individual attacks offer empirically more robust, regret-minimizing strategies than individual attacks
- Many diverse MIA methods have been proposed that each exploit different privacy leakage signals in tabular generative models
- The study represents the largest synthetic data privacy benchmark conducted to date

**Limitations**: The ensemble approach requires combining multiple attack methods, which may increase computational cost; the abstract does not specify the overhead or scalability constraints of the ensemble methods.

### Liu et al. (2024)

**Research question**: How can membership inference attacks for RAG systems be improved to be more document-specific and less susceptible to distractions from other documents or the LLM's internal knowledge?

**Methodology**: The paper proposes a Mask-Based Membership Inference Attacks (MBA) framework that employs a masking algorithm to mask words in the target document, prompts the RAG system with the masked text to predict mask values, and uses a threshold-based method to infer membership by analyzing mask prediction accuracy.

**Key findings**:
- Previous MIAs for RAG systems are insufficient as they rely solely on the RAG system's judgment or are easily influenced by other documents or the LLM's internal knowledge
- The mask-based approach is more document-specific, making the RAG system's generation less susceptible to distractions
- If the target document appears in the knowledge database, the masked text retrieves the complete document as context, enabling accurate mask prediction
- A simple threshold-based method effectively infers membership by analyzing mask prediction accuracy
- Extensive experiments demonstrate the effectiveness of the mask-based approach compared to existing baseline models

**Limitations**: The approach requires the RAG system to support mask prediction tasks; the optimal number of words to mask and threshold selection criteria are not specified in the abstract.

### Kulkarni et al. (2026)

**Research question**: Can remotely hosted applications employing retrieval-based in-context learning be vulnerable to membership inference attacks even when the service provider and users are separate parties?

**Methodology**: The authors propose two black-box membership inference attacks that exploit query text prefixes to distinguish member from non-member inputs: one using a reference model to estimate loss metrics, and another using a novel weighted-averaging scheme without a reference model, with comprehensive empirical evaluations testing these attacks with paraphrased query texts against three prior attacks.

**Key findings**:
- Remotely hosted applications with retrieval-based in-context learning are vulnerable to membership inference attacks even with separated service providers and users
- The proposed weighted-averaging attack outperforms three prior attacks in many cases with small numbers of prefixes
- Both attacks exhibit resilience to paraphrasing of query texts
- An existing ensemble prompting defense substantially mitigates privacy leakage from the second attack

**Limitations**: Not stated in abstract.

### Ran et al. (2025)

**Research question**: Are LoRA fine-tuned language models vulnerable to membership inference attacks, and does the pre-trained model contribute to information leakage?

**Methodology**: The authors introduce LoRA-Leak, a holistic evaluation framework incorporating fifteen membership inference attacks (ten existing and five improved attacks leveraging the pre-trained model as reference), applying it to three advanced language models across three NLP tasks under various fine-tuning settings and exploring four defense mechanisms.

**Key findings**:
- LoRA-based fine-tuned language models remain vulnerable to membership inference attacks (e.g., 0.775 AUC under conservative fine-tuning settings)
- Utilizing the pre-trained model induces more information leakage than previously recognized
- Only dropout and excluding specific LM layers during fine-tuning effectively mitigate MIA risks while maintaining utility
- The existence of the pre-trained model makes MIA a more severe risk for LoRA-based language models under the pre-training and fine-tuning paradigm

**Limitations**: Not stated in abstract.

### Jebreel et al. (2026)

**Research question**: Under what conditions do membership inference attacks constitute a genuine privacy threat in machine learning?

**Methodology**: The authors propose an evaluation framework defining conditions under which MIAs constitute genuine privacy threats, then review representative MIAs against this framework to assess their effectiveness as privacy metrics.

**Key findings**:
- Under realistic conditions defined in the proposed framework, MIAs represent weak privacy threats
- Relying on MIAs as a privacy metric can lead to overestimation of privacy risk
- Using MIAs as privacy metrics may result in unnecessary sacrifices in model utility from employing overly strong defenses

**Limitations**: Not stated in abstract.

### Khalil et al. (2025)

**Research question**: What are the root causes of membership inference vulnerabilities in machine learning models beyond traditional overfitting?

**Methodology**: The authors empirically analyze characteristics of training data samples vulnerable to MIAs in models that are not overfitted, then propose targeted defensive strategies to protect vulnerable samples and enhance privacy-preserving capabilities.

**Key findings**:
- Model overfitting is not the sole cause of membership inference vulnerabilities
- Training samples vulnerable to MIAs in non-overfitted models are often outliers within their classes (e.g., noisy or hard to classify)
- Even non-overfitted ML models can leak information about a small subset of their training data
- Targeted defensive strategies can protect vulnerable samples and enhance privacy preservation

**Limitations**: Not stated in abstract.

### Chen et al. (2026)

**Research question**: Can membership inference attacks be effective against chat agent memory stores containing sensitive user-agent interactions?

**Methodology**: The authors propose Multi-Recall Memory MIA (MRMMIA), a unified attack utilizing multiple recall probes to extract membership signals across black-box, gray-box, and white-box settings, with experiments demonstrating MRMMIA's performance against baselines in chat agent memory systems.

**Key findings**:
- Chat agent memory is vulnerable to membership inference attacks
- MRMMIA consistently outperforms baseline attacks across different settings
- The proposed unified attack works effectively across black-box, gray-box, and white-box settings
- Agent memory containing sensitive user interactions, retrieved facts, and preferences presents privacy risks

**Limitations**: Not stated in abstract.

## References

Bai, L., Hu, H., Ye, Q., Li, H., Wang, L., & Xu, J. (2024). Membership inference attacks and defenses in federated learning: A survey. arXiv. https://arxiv.org/abs/2412.06157

Chen, K., Pang, Y., & Wang, T. (2026). MRMMIA: Membership inference attacks on memory in chat agents. arXiv. https://arxiv.org/abs/2605.27825

Du, Y., Li, J., Chen, Y., Zhang, K., Yuan, Z., Xiao, H., Ribeiro, B., & Li, N. (2025). Cascading and proxy membership inference attacks. arXiv. https://arxiv.org/abs/2507.21412

Jebreel, N., Sánchez, D., & Domingo-Ferrer, J. (2026). A critical review on the effectiveness and privacy threats of membership inference attacks. arXiv. https://arxiv.org/abs/2603.22987

Khalil, M., Blanco-Justicia, A., Jebreel, N., & Domingo-Ferrer, J. (2025). Membership inference attacks beyond overfitting. arXiv. https://arxiv.org/abs/2511.16792

Kulkarni, T., Koskela, A., & Zumot, L. (2026). Membership inference attacks for retrieval based in-context learning for document question answering. arXiv. https://arxiv.org/abs/2605.04116

Liu, M., Zhang, S., & Long, C. (2024). Mask-based membership inference attacks for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2410.20142

Ran, D., He, X., Cong, T., Wang, A., Li, Q., & Wang, X. (2025). LoRA-Leak: Membership inference attacks against LoRA fine-tuned language models. arXiv. https://arxiv.org/abs/2507.18302

Song, W., Cao, Y., Ding, Z., Liu, Y., Deng, G., & Li, Y. (2026). Membership inference attacks against video large language models. arXiv. https://arxiv.org/abs/2604.27002

Ward, J., Yang, Y., Wang, C.-H., & Cheng, G. (2025). Ensembling membership inference attacks against tabular generative models. arXiv. https://arxiv.org/abs/2509.05350
