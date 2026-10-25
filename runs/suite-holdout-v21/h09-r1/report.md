# Systematic Literature Review: Membership Inference Attacks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "membership inference attacks", filtered to category cs.CR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on membership inference attacks (MIAs) has evolved significantly beyond traditional overfitting-based attacks to encompass diverse machine learning paradigms including federated learning, retrieval-augmented generation, video-language models, and chat agent memory systems. Recent work demonstrates that MIAs remain effective even in non-overfitted models by exploiting outlier training samples, fine-tuning artifacts, and retrieval patterns. The surveyed papers reveal a field maturing toward more sophisticated attack vectors while simultaneously developing robust defense mechanisms and critical frameworks for evaluating when MIAs constitute genuine privacy threats. Notably, ensemble-based attacks and proxy-based methods have emerged as particularly effective approaches that outperform traditional MIAs, especially in low false-positive regimes.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "membership inference attacks", filtered to category cs.CR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: MIAs in Emerging ML Architectures

The literature demonstrates a clear trend of extending membership inference attacks to novel machine learning architectures beyond traditional classification models. Recent work has targeted federated learning systems (Bai et al., 2024), retrieval-augmented generation (RAG) systems (Liu et al., 2024; Kulkarni et al., 2026), video large language models (Song et al., 2026), LoRA fine-tuned language models (Ran et al., 2025), and chat agent memory systems (Chen et al., 2026). This expansion reflects the field's response to the rapid deployment of these technologies in production environments where privacy concerns are paramount. Each architecture presents unique challenges: federated learning shares only model updates rather than raw data, RAG systems retrieve from external knowledge bases, VideoLLMs process multimodal inputs, and chat agents maintain persistent memory across interactions. The common thread is that despite architectural differences, all remain vulnerable to carefully designed membership inference attacks that exploit system-specific behaviors.

### Theme 2: Attack Methodology Evolution

A second prominent theme is the evolution from simple loss-based attacks to more sophisticated methodologies that exploit system-specific characteristics. The mask-based approach for RAG systems (Liu et al., 2024) masks words in target documents and measures prediction accuracy to infer membership, making it more document-specific and less susceptible to distractions. Cascading and proxy attacks (Du et al., 2025) exploit membership dependencies between instances and use proxy selection strategies, substantially outperforming existing methods in low false-positive regimes. The temperature-perturbed generation approach for VideoLLMs (Song et al., 2026) queries models at different temperatures and measures semantic drift, achieving 0.68 AUC. LoRA-Leak (Ran et al., 2025) leverages the pre-trained model as a reference to detect information leakage during fine-tuning. These methodological innovations demonstrate that effective MIAs increasingly require domain-specific adaptations rather than one-size-fits-all approaches.

### Theme 3: Ensemble and Robust Attack Strategies

The literature shows growing recognition that no single MIA method dominates across all scenarios, leading to ensemble-based approaches. Ward et al. (2025) conducted the largest synthetic data privacy benchmark to date, demonstrating that no MIA constitutes a strictly dominant strategy across various model architectures and dataset domains. They propose ensemble MIAs that combine multiple individual attacks, showing that unsupervised ensembles offer more robust, regret-minimizing strategies than individual attacks. This addresses the realistic threat scenario where adversaries must choose a single method without guarantee it will be the highest performing option. The ensemble approach represents a maturation of the field toward more reliable and consistent attack performance across diverse settings.

### Theme 4: Privacy Threats Beyond Overfitting

A critical theme emerging from recent work is that membership inference vulnerabilities extend well beyond the traditional overfitting explanation. Khalil et al. (2025) empirically demonstrate that even non-overfitted ML models can leak information about a small subset of their training data, with vulnerable samples often being outliers within their classes (noisy or hard-to-classify samples). This challenges the conventional wisdom that MIAs primarily exploit overfitting and suggests that privacy risks persist even in well-generalized models. Ran et al. (2025) further show that the pre-trained model in LoRA fine-tuning can induce significant information leakage that existing attacks overlook, indicating that privacy risks can stem from the model development paradigm itself rather than just training dynamics.

### Theme 5: Critical Evaluation and Defense Frameworks

The literature reveals growing sophistication in evaluating when MIAs constitute genuine privacy threats and developing targeted defenses. Jebreel et al. (2026) propose an evaluation framework defining conditions under which MIAs represent genuine privacy threats, concluding that under realistic conditions, MIAs represent weak privacy threats and relying on them as a privacy metric can lead to overestimation of risk. This critical perspective suggests the field may be over-investing in defenses against exaggerated threats. Meanwhile, targeted defensive strategies have shown promise: Ran et al. (2025) found that only dropout and excluding specific LM layers during fine-tuning effectively mitigate MIA risks while maintaining utility. Kulkarni et al. (2026) adapted an ensemble prompting defense that substantially mitigates privacy leakage. Bai et al. (2024) provide systematic analysis of various countermeasures in federated learning, categorizing defenses based on their characteristics.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that membership inference attacks remain effective across diverse ML architectures, from federated learning to chat agents (Bai et al., 2024; Chen et al., 2026; Song et al., 2026). There is broad agreement that domain-specific adaptations outperform generic attack methods (Du et al., 2025; Liu et al., 2024; Ran et al., 2025). The literature also converges on the finding that vulnerable training samples often share specific characteristics, such as being outliers or having unique features that make them distinguishable (Khalil et al., 2025; Ward et al., 2025).

**Disagreements**: A notable tension exists regarding the severity of the privacy threat posed by MIAs. While most papers treat MIAs as serious privacy concerns requiring robust defenses, Jebreel et al. (2026) argue that under realistic conditions, MIAs represent weak privacy threats and that current reliance on MIAs as privacy metrics may result in unnecessary sacrifices in model utility due to overly strong defenses. This critical perspective challenges the field's assumptions about threat severity and suggests a need for more nuanced evaluation frameworks. Additionally, there is implicit disagreement about whether ensemble methods or specialized single-method attacks represent the optimal attack strategy, with Ward et al. (2025) advocating for ensembles while others demonstrate strong results with domain-specific single approaches.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly discuss limitations in their abstracts, suggesting a need for more transparent reporting of attack constraints and failure modes. Second, while several papers propose defenses, there is limited systematic comparison of defense effectiveness across different attack types, making it difficult for practitioners to choose appropriate countermeasures. Third, the critical perspective raised by Jebreel et al. (2026) about overestimation of MIA risks suggests the field needs more rigorous frameworks for evaluating when MIAs constitute genuine privacy threats versus theoretical concerns. Fourth, most attacks focus on specific architectural features, but there is limited work on transferable attack methods that work across multiple ML paradigms. Finally, the literature lacks discussion of regulatory and ethical implications of MIA research, particularly regarding dual-use concerns where attack methodologies could be misused by malicious actors.

## Per-Paper Annotations

### Bai et al. (2024)

**Research question**: What are the membership inference attacks and corresponding defense strategies in federated learning, and how can they be systematically categorized?
**Methodology**: The paper conducts a comprehensive survey by categorizing and summarizing membership inference attacks and defense strategies based on their characteristics in federated learning, introducing a taxonomy of existing attack research and providing systematic analysis of various countermeasures.
**Key findings**:
- Federated learning faces privacy vulnerabilities despite only sharing model updates, not raw training data
- Membership inference attacks can determine whether a specific example is part of the training set, compromising sensitive information
- The survey categorizes attacks and defenses based on their characteristics in the federated learning setting
- Different approaches have distinct strengths and weaknesses that are analyzed systematically
- Key future research directions are identified for advancing the field
**Limitations**: not stated in abstract

### Chen et al. (2026)

**Research question**: How can membership inference attacks be applied to chat agent memory systems to infer whether candidate memory units belong to an agent's memory store?
**Methodology**: The authors propose Multi-Recall Memory MIA (MRMMIA), a unified attack utilizing multiple recall probes to extract membership signals across black-box, gray-box, and white-box settings.
**Key findings**:
- Chat agent memory containing sensitive user-agent interactions, retrieved facts, and user preferences is vulnerable to membership inference attacks
- MRMMIA consistently outperforms baseline attacks across different access settings
- The work provides an initial evaluation framework for membership leakage in chat-agent memory systems
**Limitations**: not stated in abstract

### Du et al. (2025)

**Research question**: How can membership inference attacks be improved by exploiting membership dependencies between instances in adaptive settings and using proxy selection strategies in non-adaptive settings?
**Methodology**: The paper introduces two attacks: Cascading Membership Inference Attack (CMIA) for adaptive settings that incorporates membership dependencies via conditional shadow training, and Proxy Membership Inference Attack (PMIA) for non-adaptive settings that employs proxy selection strategies and membership posterior odds tests.
**Key findings**:
- MIAs are classified into adaptive or non-adaptive depending on whether adversaries can train shadow models on membership queries
- CMIA exploits membership dependencies between instances through conditional shadow training to boost inference performance
- PMIA identifies samples with similar behaviors to query instances and uses their behaviors in shadow models for membership inference
- Both CMIA and PMIA substantially outperform existing MIAs, particularly in the low false-positive regime
- Theoretical analyses are provided for both attacks alongside extensive experimental validation
**Limitations**: not stated in abstract

### Jebreel et al. (2026)

**Research question**: Under what conditions do membership inference attacks constitute a genuine privacy threat in machine learning systems?
**Methodology**: The authors propose an evaluation framework defining conditions under which MIAs represent genuine privacy threats, then review representative MIAs against this framework.
**Key findings**:
- Under realistic conditions defined in the proposed framework, MIAs represent weak privacy threats
- Relying on MIAs as a privacy metric can lead to overestimation of risk
- Current reliance on MIAs may result in unnecessary sacrifices in model utility due to overly strong defenses
**Limitations**: not stated in abstract

### Khalil et al. (2025)

**Research question**: What are the root causes of membership inference vulnerabilities in machine learning models beyond traditional overfitting?
**Methodology**: The authors empirically analyze characteristics of training data samples vulnerable to MIAs in non-overfitted models and propose defensive strategies to protect vulnerable samples.
**Key findings**:
- Even non-overfitted ML models can leak information about a small subset of their training data
- Vulnerable samples in non-overfitted models are often outliers within their classes (e.g., noisy or hard to classify samples)
- Targeted defensive strategies can protect vulnerable samples and enhance privacy-preserving capabilities
- The research code is publicly available at https://github.com/najeebjebreel/mia_analysis
**Limitations**: not stated in abstract

### Kulkarni et al. (2026)

**Research question**: Can membership inference attacks effectively target retrieval-based in-context learning systems for document question answering when the service provider and users are separate parties?
**Methodology**: The authors propose two black-box membership inference attacks that exploit query text prefixes to distinguish member from non-member inputs: one using a reference model to estimate loss metrics, and another using a novel weighted-averaging scheme without requiring a reference model.
**Key findings**:
- Remotely hosted applications using retrieval-based in-context learning are vulnerable to membership inference attacks even with separated service providers and users
- The proposed attacks demonstrate stronger resilience to paraphrasing compared to three prior attacks
- The attacks perform well with a small number of prefixes
- An existing ensemble prompting defense was adapted and shown to substantially mitigate privacy leakage from the second attack
**Limitations**: not stated in abstract

### Liu et al. (2024)

**Research question**: How can mask-based approaches improve membership inference attacks against RAG systems by making them more document-specific and less susceptible to distractions?
**Methodology**: The paper proposes a Mask-Based Membership Inference Attacks (MBA) framework that employs a masking algorithm to mask words in target documents, prompts the RAG system with masked text to predict mask values, and uses threshold-based methods to infer membership based on prediction accuracy.
**Key findings**:
- RAG systems store up-to-date or copyrighted data in knowledge databases, raising membership inference concerns
- Existing MIAs for RAG systems are insufficient, relying solely on system judgment or being easily influenced by other documents
- The mask-based approach masks certain words in target documents and requires the RAG system to predict them
- If the target document is in the knowledge database, masked text retrieves complete context allowing accurate mask prediction
- The mask-based approach is more document-specific and less susceptible to distractions from other documents or LLM internal knowledge
**Limitations**: not stated in abstract

### Ran et al. (2025)

**Research question**: How vulnerable are LoRA fine-tuned language models to membership inference attacks, and what role does the pre-trained model play in information leakage?
**Methodology**: The authors introduce LoRA-Leak, a holistic evaluation framework incorporating fifteen membership inference attacks (ten existing and five improved attacks leveraging the pre-trained model as a reference), applied to three advanced language models across three NLP tasks.
**Key findings**:
- LoRA-based fine-tuned language models remain vulnerable to membership inference attacks (e.g., 0.775 AUC under conservative fine-tuning settings)
- The pre-trained model can induce significant information leakage that existing attacks overlook
- Only dropout and excluding specific LM layers during fine-tuning effectively mitigate MIA risks while maintaining utility among four tested defenses
- The existence of the pre-trained model makes MIA a more severe risk for LoRA-based models under the pre-training and fine-tuning paradigm
**Limitations**: not stated in abstract

### Song et al. (2026)

**Research question**: Can an external auditor determine whether a particular video was used during training of Video Large Language Models through black-box membership inference attacks?
**Methodology**: The paper presents a black-box membership inference attack targeting VideoLLMs that couples temperature-perturbed generation with video-aware difficulty features, querying the target model at low and high temperatures and measuring semantic drift between resulting texts.
**Key findings**:
- VideoLLMs are trained on large-scale video-text corpora from heterogeneous sources, raising privacy concerns
- The VideoLLM setting is challenging because black-box auditors observe only generated text while membership signals are entangled with video-specific factors
- Member samples tend to induce sharper, more brittle generation behavior across decoding temperatures
- The attack achieved a member inference AUC of 0.68 and accuracy of 0.63 against LLaVA-Video-7B-Qwen2-Video-Only
- VideoLLMs are vulnerable to black-box membership inference attacks, highlighting need for systematic evaluation and mitigation
**Limitations**: not stated in abstract

### Ward et al. (2025)

**Research question**: How can ensemble membership inference attacks provide more robust privacy auditing strategies than individual attacks against tabular generative models?
**Methodology**: The paper conducts the largest synthetic data privacy benchmark to date, studying MIA selection as a decision theoretic problem under uncertainty, then proposes ensemble MIAs and demonstrates that unsupervised ensembles built on individual attacks offer more robust strategies.
**Key findings**:
- MIAs have emerged as a principled framework for auditing privacy of synthetic data from tabular generative models
- In realistic threat scenarios, adversaries must choose a single method without guarantee it will be the highest performing option
- No MIA constitutes a strictly dominant strategy across various model architectures and dataset domains
- Ensemble MIAs are proposed to address the challenge of method selection under uncertainty
- Unsupervised ensembles built on individual attacks offer empirically more robust, regret-minimizing strategies than individual attacks
**Limitations**: not stated in abstract

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
