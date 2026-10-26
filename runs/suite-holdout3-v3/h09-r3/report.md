# Systematic Literature Review: Membership Inference Attacks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "membership inference attacks", category cs.CR, last 2 years (2024-10-26 to 2026-10-26)
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on membership inference attacks (MIAs) published between late 2024 and mid-2026 within the computer security category (cs.CR). The surveyed literature reveals a rapidly evolving field where MIAs have expanded beyond traditional machine learning models to target emerging architectures including federated learning systems, video large language models, retrieval-augmented generation systems, LoRA fine-tuned models, and chat agent memory systems. Collectively, these papers demonstrate that MIAs remain a significant privacy threat across diverse model architectures and deployment scenarios, though recent critical work questions whether MIAs represent genuine privacy threats under realistic conditions. The field shows increasing sophistication in attack methodologies, with novel techniques exploiting membership dependencies, ensemble strategies, and temperature-perturbed generation, while defensive research focuses on targeted protection mechanisms and architectural modifications.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "membership inference attacks", filtered to category cs.CR, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Expansion to Novel Model Architectures

The surveyed literature demonstrates a clear trend of extending membership inference attacks beyond traditional machine learning models to emerging architectures. Bai et al. (2024) established the foundation for understanding MIAs in federated learning contexts, where privacy vulnerabilities persist despite the protocol's design of sharing only model updates rather than raw training data. More recent work has pushed further into cutting-edge systems: Song et al. (2026) targeted video large language models (VideoLLMs), Chen et al. (2026) focused on chat agent memory systems, and Kulkarni et al. (2026) examined retrieval-based in-context learning for document question answering. This expansion reflects the field's response to rapidly evolving AI deployment patterns, where each new architecture introduces unique attack surfaces. The progression from federated learning (2024) to VideoLLMs and chat agents (2026) illustrates how MIA research tracks closely with industry adoption of new model types.

### Theme 2: Attack Methodology Sophistication

Recent work shows increasing methodological sophistication in MIA design. Du et al. (2025) introduced cascading and proxy membership inference attacks that exploit membership dependencies between instances, substantially outperforming existing MIAs in both adaptive and non-adaptive settings. Ward et al. (2025) conducted the largest synthetic data privacy benchmark to date, proposing ensemble MIAs as regret-minimizing strategies when no single attack dominates across different architectures. Liu et al. (2024) developed mask-based attacks specifically for retrieval-augmented generation systems, employing masking algorithms to make attacks more document-specific and less susceptible to distractions. Song et al. (2026) coupled temperature-perturbed generation with video-aware difficulty features for attacking VideoLLMs, achieving member inference AUC of 0.68. Ran et al. (2025) introduced LoRA-Leak, a holistic evaluation framework incorporating fifteen membership inference attacks against LoRA fine-tuned language models. This methodological diversification reflects the recognition that different model architectures require tailored attack strategies.

### Theme 3: Critical Assessment of MIA Effectiveness

A notable theme emerging from the 2025-2026 literature is critical self-reflection about whether MIAs constitute genuine privacy threats. Jebreel et al. (2026) proposed an evaluation framework defining conditions under which MIAs represent genuine privacy threats and concluded that under realistic conditions, MIAs represent weak privacy threats. They argue that relying on MIAs as privacy metrics can lead to overestimation of risk and cause unnecessary sacrifices in model utility from employing overly strong defenses. This critical perspective is complemented by Khalil et al. (2025), who demonstrated that non-overfitted models can still leak information about a small subset of their training data, identifying vulnerable samples as often being outliers within their classes. Together, these papers suggest the field is maturing beyond demonstrating attack feasibility toward understanding the actual privacy implications and appropriate evaluation methodologies.

### Theme 4: Targeted Defense Strategies

The surveyed literature reveals a shift from generic defenses to targeted protection mechanisms. Ran et al. (2025) found that only dropout and excluding specific LM layers during fine-tuning effectively mitigate MIA risks while maintaining utility for LoRA-based models. Khalil et al. (2025) proposed targeted defensive strategies to protect vulnerable samples identified as outliers within their classes. Bai et al. (2024) provided a systematic overview of various countermeasures in federated learning with thorough analysis of strengths and weaknesses. Kulkarni et al. (2026) noted that an existing ensemble prompting defense substantially mitigates privacy leakage from their second attack. This trend toward targeted defenses reflects growing recognition that privacy protection must balance security with model utility, and that one-size-fits-all approaches are insufficient.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that membership inference attacks remain viable across diverse model architectures. Bai et al. (2024), Ran et al. (2025), Song et al. (2026), and Chen et al. (2026) all demonstrate successful attacks against their respective target systems, establishing that privacy vulnerabilities persist regardless of architectural innovations. There is also broad agreement that traditional overfitting-based explanations are insufficient: Khalil et al. (2025) explicitly demonstrate vulnerabilities in non-overfitted models, while Du et al. (2025) show that exploiting membership dependencies improves attack performance beyond what overfitting alone would predict.

**Disagreements**: A significant tension exists between papers demonstrating attack effectiveness and those questioning the practical privacy implications. While most surveyed papers present successful attacks with quantitative metrics (e.g., Song et al., 2026: AUC 0.68; Ran et al., 2025: AUC 0.775), Jebreel et al. (2026) argue that under realistic conditions defined in their evaluation framework, MIAs represent weak privacy threats. This disagreement reflects a fundamental question in the field: does demonstrating attack feasibility equate to meaningful privacy risk? The disagreement extends to evaluation methodology, with Jebreel et al. (2026) cautioning that current MIA-based evaluation may cause overestimation of risk.

## Gaps and Open Questions

The surveyed literature reveals several notable gaps. First, none of the papers explicitly state limitations in their abstracts, suggesting either that limitations are not systematically addressed or that space constraints prevent their inclusion in abstracts. Second, while multiple papers propose defenses (Bai et al., 2024; Ran et al., 2025; Khalil et al., 2025), there is limited systematic comparison of defensive effectiveness across different attack types and model architectures. Third, the critical perspective raised by Jebreel et al. (2026) about MIA effectiveness as a privacy metric suggests the field needs standardized evaluation frameworks, but no such framework has achieved consensus. Fourth, Ward et al. (2025) note that adversaries must choose a single attack method without a priori guarantee of optimal performance, highlighting a gap in understanding attack selection under uncertainty. Finally, the rapid expansion to new architectures (VideoLLMs, chat agents, RAG systems) suggests that MIA research is reactive rather than proactive, raising questions about whether the field can anticipate vulnerabilities in future architectures.

## Per-Paper Annotations

### Bai et al. (2024)

**Research question**: What are the membership inference attacks and corresponding defense strategies in federated learning, and how can they be systematically categorized?
**Methodology**: This paper presents a comprehensive survey that categorizes and summarizes membership inference attacks and defense strategies in federated learning based on their characteristics, introducing a taxonomy of existing attack research and providing a systematic overview of various countermeasures.
**Key findings**:
- Federated learning faces privacy vulnerabilities despite only sharing model updates rather than raw training data
- Membership inference attacks can determine whether specific examples are part of the training set, compromising sensitive information
- There was no comprehensive and up-to-date survey specifically focused on membership inference attacks within federated learning prior to this work
- The authors provide a unique taxonomy categorizing existing attack research and defense strategies
- Key future research directions are identified for advancing the field
**Limitations**: Not stated in abstract

### Song et al. (2026)

**Research question**: Can an external auditor determine whether a particular video was used during training of Video Large Language Models?
**Methodology**: The authors present a black-box membership inference attack targeting VideoLLMs that couples temperature-perturbed generation with video-aware difficulty features, querying the target model at low and high temperatures and measuring semantic drift between resulting texts.
**Key findings**:
- VideoLLMs are vulnerable to black-box membership inference attacks despite the challenge that auditors observe only generated text
- Member samples tend to induce sharper, more brittle generation behavior across decoding temperatures
- The attack achieved a member inference AUC of 0.68 and accuracy of 0.63 against LLaVA-Video-7B-Qwen2-Video-Only
- The membership signal is entangled with video-specific factors such as motion complexity and temporal span
- There is an urgent need for the community to systematically evaluate and mitigate privacy risks in VideoLLMs
**Limitations**: Not stated in abstract

### Du et al. (2025)

**Research question**: How can membership inference attacks be improved by exploiting membership dependencies between instances in both adaptive and non-adaptive settings?
**Methodology**: The authors propose two attack frameworks: Cascading Membership Inference Attack (CMIA) for the adaptive setting that incorporates membership dependencies via conditional shadow training, and Proxy Membership Inference Attack (PMIA) for the non-adaptive setting that employs a proxy selection strategy to identify samples with similar behaviors to the query instance.
**Key findings**:
- Membership dependencies between instances can be exploited to boost membership inference performance
- CMIA and PMIA substantially outperform existing MIAs in both adaptive and non-adaptive settings
- The attacks are particularly effective in the low false-positive regime, which is crucial for evaluating privacy risks
- The authors provide theoretical analyses supporting both attack frameworks
- MIAs can be classified into adaptive (adversary trains shadow models after accessing queries) and non-adaptive (shadow models trained before obtaining queries) settings
**Limitations**: Not stated in abstract

### Ward et al. (2025)

**Research question**: How can adversaries choose effective membership inference attack methods when no single method dominates across different model architectures and dataset domains?
**Methodology**: The authors conduct the largest synthetic data privacy benchmark to date, studying MIA selection as a decision theoretic problem under uncertainty and proposing ensemble MIAs built on individual attacks to offer more robust, regret-minimizing strategies.
**Key findings**:
- No membership inference attack constitutes a strictly dominant strategy across various model architectures and dataset domains
- Many diverse MIA methods have been proposed that each exploit different privacy leakage signals
- Unsupervised ensembles built on individual attacks offer empirically more robust strategies than individual attacks
- In realistic threat scenarios, adversaries must choose a single method without a priori guarantee of optimal performance
- This represents the largest synthetic data privacy benchmark conducted to date
**Limitations**: Not stated in abstract

### Liu et al. (2024)

**Research question**: How can membership inference attacks for RAG systems be improved to be more document-specific and less susceptible to distractions from other documents or the LLM's internal knowledge?
**Methodology**: The authors propose a Mask-Based Membership Inference Attacks (MBA) framework that employs a masking algorithm to mask words in the target document, then prompts the RAG system to predict the mask values, using a threshold-based method to analyze mask prediction accuracy to infer membership.
**Key findings**:
- Previous MIAs for RAG systems are insufficient as they rely solely on the RAG system's judgment or are easily influenced by other documents or the LLM's internal knowledge
- The mask-based approach is more document-specific, making generation less susceptible to distractions
- If the target document appears in the knowledge database, masked text retrieves the complete document as context, enabling accurate mask prediction
- Extensive experiments demonstrate the effectiveness of the approach compared to existing baseline models
- RAG systems storing up-to-date or copyrighted data raise concerns about membership inference attacks detecting if specific documents are in the knowledge database
**Limitations**: Not stated in abstract

### Kulkarni et al. (2026)

**Research question**: Can remotely hosted applications using retrieval-based in-context learning be vulnerable to membership inference attacks when the service provider and users are separate parties?
**Methodology**: The authors propose two black-box membership inference attacks that exploit query text prefixes to distinguish member from non-member inputs, with the first attack using a reference model to estimate loss metrics and the second using a novel weighted-averaging scheme without requiring a reference model.
**Key findings**:
- Retrieval-augmented in-context learning applications are vulnerable to membership inference attacks even with separated service providers and users
- The proposed attacks exhibit strong resilience to paraphrasing of query text
- The attacks outperform three prior attacks in many cases with small numbers of prefixes
- An existing ensemble prompting defense substantially mitigates privacy leakage from the second attack
**Limitations**: Not stated in abstract

### Ran et al. (2025)

**Research question**: Are LoRA fine-tuned language models vulnerable to membership inference attacks despite the small proportion of tuned parameters?
**Methodology**: The authors introduce LoRA-Leak, a holistic evaluation framework incorporating fifteen membership inference attacks (ten existing and five improved attacks leveraging pre-trained models as references), tested on three advanced language models across three NLP tasks.
**Key findings**:
- LoRA-based fine-tuned language models remain vulnerable to membership inference attacks (e.g., 0.775 AUC under conservative fine-tuning settings)
- Utilizing the pre-trained model induces more information leakage than previously recognized
- Only dropout and excluding specific LM layers during fine-tuning effectively mitigate MIA risks while maintaining utility
- The existence of pre-trained models makes MIA a more severe risk for LoRA-based language models
**Limitations**: Not stated in abstract

### Jebreel et al. (2026)

**Research question**: Under what conditions do membership inference attacks constitute a genuine privacy threat in machine learning?
**Methodology**: The authors propose an evaluation framework defining conditions under which MIAs represent genuine privacy threats, then review representative MIAs against this framework.
**Key findings**:
- Under realistic conditions defined in the proposed framework, MIAs represent weak privacy threats
- Relying on MIAs as privacy metrics can lead to overestimation of risk
- Current MIA-based evaluation may cause unnecessary sacrifices in model utility from employing overly strong defenses
**Limitations**: Not stated in abstract

### Khalil et al. (2025)

**Research question**: What are the root causes of membership inference vulnerabilities in machine learning models beyond traditional overfitting?
**Methodology**: The authors empirically analyze characteristics of training data samples vulnerable to MIAs in non-overfitted models and propose targeted defensive strategies to protect vulnerable samples.
**Key findings**:
- Non-overfitted models can still leak information about a small subset of their training data
- Vulnerable samples are often outliers within their classes (e.g., noisy or hard to classify)
- Model overfitting is not the sole factor contributing to membership inference vulnerabilities
- Targeted defenses can protect vulnerable samples and enhance privacy-preserving capabilities
**Limitations**: Not stated in abstract

### Chen et al. (2026)

**Research question**: Can membership inference attacks be effective against chat agent memory systems containing sensitive user-agent interactions?
**Methodology**: The authors propose Multi-Recall Memory MIA (MRMMIA), a unified attack utilizing multiple recall probes to extract membership signals across black-box, gray-box, and white-box settings.
**Key findings**:
- Chat agent memory is vulnerable to membership inference attacks
- MRMMIA consistently outperforms baseline attacks
- Agent memory containing sensitive user interactions, retrieved facts, and preferences poses privacy risks
- The work provides an initial evaluation framework for membership leakage in chat-agent memory systems
**Limitations**: Not stated in abstract

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
