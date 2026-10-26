# Systematic Literature Review: Membership Inference Attacks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "membership inference attacks", category cs.CR, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on membership inference attacks (MIAs) in the cryptography and security domain (cs.CR) from the past two years. The literature reveals MIAs as an evolving privacy threat across diverse machine learning paradigms, including federated learning, retrieval-augmented generation, video-language models, fine-tuned language models, and chat agent memory systems. While earlier work primarily attributed MIA vulnerability to model overfitting, recent research demonstrates that privacy leakage persists even in non-overfitted models and extends to novel architectures. A critical strand of literature questions the effectiveness of MIAs as privacy metrics under realistic conditions, suggesting potential overestimation of risks. The field is simultaneously advancing more sophisticated attack methodologies—including cascading attacks, proxy attacks, and ensemble approaches—while identifying targeted defense strategies that preserve model utility.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "membership inference attacks", filtered to category cs.CR (Cryptography and Security), published between 2024-10-26 and 2026-10-26. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: MIA Vulnerabilities Across Novel ML Architectures

Recent literature demonstrates that membership inference attacks extend beyond traditional supervised learning to emerging ML paradigms. Bai et al. (2024) survey MIA vulnerabilities in federated learning, where privacy risks persist despite only sharing model updates rather than raw training data. The attack surface has expanded to retrieval-augmented generation systems, with Liu et al. (2024) and Kulkarni et al. (2026) developing mask-based and prefix-based attacks respectively for RAG and in-context learning systems. Video-language models are not immune: Song et al. (2026) demonstrate black-box MIAs against VideoLLMs by exploiting temperature-perturbed generation patterns. Most recently, Chen et al. (2026) introduce attacks targeting chat agent memory systems, revealing privacy risks in user-agent interactions and retrieved facts. This theme illustrates that MIA threats evolve alongside ML architectural innovation, requiring continuous reassessment of privacy guarantees.

### Theme 2: Exploiting Membership Dependencies and Ensemble Methods

A significant methodological advance involves exploiting structural relationships between data instances and combining multiple attack signals. Du et al. (2025) propose cascading and proxy membership inference attacks that leverage membership dependencies between instances, substantially outperforming existing attacks in both adaptive and non-adaptive settings. Their CMIA incorporates conditional shadow training, while PMIA employs proxy selection based on behavioral similarity. Ward et al. (2025) conduct the largest synthetic data privacy benchmark to date, demonstrating that no single MIA method dominates across diverse model architectures and datasets. They propose ensemble MIAs as regret-minimizing strategies, revealing that different MIA methods exploit distinct privacy leakage signals. This theme reflects a maturation of MIA methodology from single-metric attacks to sophisticated, multi-signal approaches.

### Theme 3: MIA Risks in Parameter-Efficient Fine-Tuning

The security implications of parameter-efficient fine-tuning techniques have received focused attention. Ran et al. (2025) introduce LoRA-Leak, a holistic evaluation framework testing fifteen membership inference attacks against LoRA fine-tuned language models. Despite LoRA tuning only a small proportion of parameters, their findings reveal significant vulnerability (0.775 AUC under conservative settings). Critically, they demonstrate that utilizing the pre-trained model as reference induces more information leakage than previously recognized, making MIA a more severe risk for LoRA-based models than anticipated. This theme highlights that parameter efficiency does not inherently confer privacy protection, and that pre-trained model access substantially amplifies attack capabilities.

### Theme 4: Beyond Overfitting – Fundamental Vulnerability Sources

Recent work challenges the traditional attribution of MIA vulnerability solely to overfitting. Khalil et al. (2025) empirically analyze non-overfitted models and find they can still leak information about a small subset of training data. Their analysis reveals that vulnerable samples are often outliers within their classes—noisy or hard-to-classify instances. This finding decouples MIA risk from overfitting as the exclusive cause, pointing to more fundamental sources of privacy leakage inherent in model training dynamics. The identification of targeted defensive strategies for vulnerable samples suggests that privacy protection may benefit from sample-level rather than model-level interventions.

### Theme 5: Critical Evaluation of MIA Effectiveness as Privacy Metrics

A critical strand of literature questions whether MIAs constitute genuine privacy threats under realistic conditions. Jebreel et al. (2026) propose an evaluation framework defining conditions under which MIAs represent authentic privacy threats, then review representative MIAs against this framework. Their findings suggest that under realistic conditions, MIAs represent weak privacy threats, and relying on them as privacy metrics can lead to risk overestimation. This critique warns that current MIA-based privacy assessment may cause unnecessary sacrifices in model utility through overly strong defenses. This theme introduces important nuance to the field, urging careful calibration of privacy defenses to actual threat levels rather than worst-case attack scenarios.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that membership inference attacks remain effective across diverse ML architectures and settings (Bai et al., 2024; Du et al., 2025; Ran et al., 2025). There is broad agreement that exploiting structural properties—whether membership dependencies between instances (Du et al., 2025), ensemble signals (Ward et al., 2025), or pre-trained model access (Ran et al., 2025)—substantially improves attack performance. The literature also converges on the finding that vulnerable samples often exhibit distinctive characteristics, such as being outliers or hard-to-classify instances (Khalil et al., 2025).

**Disagreements**: A notable tension exists between the predominant attack-focused literature and the critical evaluation perspective. While most surveyed papers demonstrate and quantify MIA effectiveness, Jebreel et al. (2026) argue that under realistic conditions, MIAs represent weak privacy threats and may lead to risk overestimation. This disagreement reflects a fundamental question about whether MIA success rates translate to genuine privacy harms, and whether current evaluation frameworks appropriately calibrate threat models to realistic adversary capabilities and constraints.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Scalability and computational costs**: Multiple papers note that their abstracts do not specify computational overhead or scalability constraints of proposed methods (Du et al., 2025; Ward et al., 2025), leaving practical deployment considerations unclear.

2. **Generalization across architectures**: Several attacks are evaluated on single models or limited architectures (Song et al., 2026; Kulkarni et al., 2026), raising questions about generalizability to other model families.

3. **Defense specificity**: While attacks are often thoroughly evaluated, defense discussions remain high-level, with limited empirical validation of proposed countermeasures' effectiveness-utility tradeoffs (Bai et al., 2024; Liu et al., 2024).

4. **Realistic threat modeling**: The critical review by Jebreel et al. (2026) highlights that many MIA evaluations may not reflect realistic adversary capabilities, suggesting a need for more grounded threat models that account for practical constraints.

5. **Sample-level defenses**: The finding that vulnerable samples are often outliers (Khalil et al., 2025) suggests potential for targeted, sample-level defenses, but this direction remains underexplored in the surveyed literature.

## Per-Paper Annotations

### Bai et al. (2024)

**Research question**: What are the membership inference attacks and corresponding defense strategies in federated learning, and how can they be systematically categorized?

**Methodology**: This paper conducts a comprehensive survey by categorizing and summarizing membership inference attacks and defense strategies based on their characteristics in federated learning settings. The authors introduce a taxonomy of existing attack research and provide a systematic overview of various countermeasures.

**Key findings**:
- Federated learning faces privacy vulnerabilities despite only sharing model updates rather than raw training data.
- Membership inference attacks can determine whether specific examples are part of the training set, compromising sensitive information.
- The survey categorizes attacks and defenses based on their characteristics in the federated learning setting.
- Different approaches have distinct strengths and weaknesses that are analyzed in the paper.
- Key future research directions are identified for advancing the field.

**Limitations**: As a survey paper, it synthesizes existing research rather than presenting novel empirical results; specific limitations of surveyed approaches are discussed but not exhaustively enumerated in the abstract.

### Chen et al. (2026)

**Research question**: Can membership inference attacks be effectively performed against chat agent memory systems?

**Methodology**: The authors propose Multi-Recall Memory MIA (MRMMIA), a unified attack utilizing multiple recall probes to extract membership signals across black-box, gray-box, and white-box settings.

**Key findings**:
- Chat agent memory is vulnerable to membership inference attacks.
- MRMMIA consistently outperforms baseline attacks.
- Agent memory containing sensitive user-agent interactions, retrieved facts, and user preferences poses privacy risks.
- The work provides an initial evaluation framework for membership leakage in chat-agent memory systems.

**Limitations**: Not stated in abstract.

### Du et al. (2025)

**Research question**: How can membership inference attacks be improved by exploiting membership dependencies between instances in adaptive and non-adaptive settings?

**Methodology**: The authors propose two attacks: Cascading Membership Inference Attack (CMIA) for the adaptive setting, which incorporates membership dependencies via conditional shadow training, and Proxy Membership Inference Attack (PMIA) for the non-adaptive setting, which employs a proxy selection strategy to identify samples with similar behaviors to query instances. Both attacks include theoretical analyses.

**Key findings**:
- CMIA and PMIA substantially outperform existing membership inference attacks in both adaptive and non-adaptive settings.
- Exploiting membership dependencies between instances improves attack performance.
- The attacks are particularly effective in the low false-positive regime, which is crucial for evaluating privacy risks.
- The framework is attack-agnostic, allowing incorporation of membership dependencies regardless of the base attack method.
- Proxy selection using behavioral similarity enables effective membership inference without access to query instances during shadow model training.

**Limitations**: The abstract does not specify computational costs or scalability constraints of the proposed methods; practical deployment considerations are not discussed.

### Jebreel et al. (2026)

**Research question**: Under what conditions do membership inference attacks constitute a genuine privacy threat in machine learning?

**Methodology**: The authors propose an evaluation framework defining conditions under which MIAs constitute genuine privacy threats, then review representative MIAs against this framework.

**Key findings**:
- Under realistic conditions defined in the proposed framework, MIAs represent weak privacy threats.
- Relying on MIAs as a privacy metric can lead to overestimation of risk.
- Current MIA-based privacy assessment may cause unnecessary sacrifices in model utility through overly strong defenses.

**Limitations**: Not stated in abstract.

### Khalil et al. (2025)

**Research question**: What are the root causes of membership inference vulnerabilities in machine learning models beyond traditional overfitting?

**Methodology**: The authors empirically analyze characteristics of training data samples vulnerable to MIAs in non-overfitted models and propose defensive strategies to protect vulnerable samples.

**Key findings**:
- Non-overfitted ML models can still leak information about a small subset of their training data.
- Vulnerable samples in non-overfitted models are often outliers within their classes (noisy or hard to classify).
- Targeted defensive strategies can protect vulnerable samples and enhance privacy-preserving capabilities.
- Model overfitting is not the sole factor contributing to membership inference vulnerabilities.

**Limitations**: Not stated in abstract.

### Kulkarni et al. (2026)

**Research question**: Can remotely hosted applications using retrieval-based in-context learning be vulnerable to membership inference attacks when the service provider and users are separate parties?

**Methodology**: The authors propose two black-box membership inference attacks that exploit query text prefixes to distinguish member from non-member inputs. The first uses a reference model to estimate loss metrics, while the second uses a novel weighted-averaging scheme without requiring a reference model.

**Key findings**:
- Remotely hosted applications with retrieval-based in-context learning are vulnerable to membership inference attacks even with separate service providers and users.
- The proposed attacks exhibit resilience to paraphrasing of query text.
- The attacks outperform three prior attacks in many cases with small numbers of prefixes.
- An existing ensemble prompting defense substantially mitigates privacy leakage from the second attack.

**Limitations**: Not stated in abstract.

### Liu et al. (2024)

**Research question**: How can membership inference attacks be improved for Retrieval-Augmented Generation systems to reliably detect if a specific target document is stored in the RAG knowledge database?

**Methodology**: The authors propose a Mask-Based Membership Inference Attack (MBA) framework that employs a masking algorithm to mask words in the target document, then prompts the RAG system to predict the masked values. A threshold-based method analyzes mask prediction accuracy to infer document membership.

**Key findings**:
- The mask-based approach is more document-specific, making RAG system generation less susceptible to distractions from other documents or the LLM's internal knowledge.
- If the target document appears in the knowledge database, masked text retrieves the complete document as context, enabling accurate mask prediction.
- The approach addresses limitations of previous methods that relied solely on RAG system judgment or were easily influenced by other documents.
- Extensive experiments demonstrate the effectiveness of the approach compared to existing baseline models.
- The method provides better explainability than previous membership inference attacks for RAG systems.

**Limitations**: The abstract does not discuss the sensitivity of the approach to the masking algorithm design or threshold selection; performance on documents with varying lengths or domains is not specified.

### Ran et al. (2025)

**Research question**: Are LoRA fine-tuned language models vulnerable to membership inference attacks despite the small proportion of tuned parameters?

**Methodology**: The authors introduce LoRA-Leak, a holistic evaluation framework incorporating fifteen membership inference attacks (ten existing and five improved attacks leveraging the pre-trained model as reference), tested on three advanced language models across three NLP tasks.

**Key findings**:
- LoRA-based fine-tuned language models remain vulnerable to membership inference attacks (e.g., 0.775 AUC under conservative fine-tuning settings).
- Utilizing the pre-trained model induces more information leakage than previously recognized.
- Only dropout and excluding specific LM layers during fine-tuning effectively mitigate MIA risks while maintaining utility.
- The existence of the pre-trained model makes MIA a more severe risk for LoRA-based language models.

**Limitations**: Not stated in abstract.

### Song et al. (2026)

**Research question**: Can an external auditor determine whether a particular video was used during training of Video Large Language Models?

**Methodology**: The authors present a black-box membership inference attack targeting VideoLLMs that couples temperature-perturbed generation with video-aware difficulty features. They query the target model at low and high temperatures and measure semantic drift between resulting texts, interpreting this signal jointly with the intrinsic difficulty of the queried video.

**Key findings**:
- VideoLLMs are vulnerable to black-box membership inference attacks.
- Member samples tend to induce sharper, more brittle generation behavior across decoding temperatures.
- The attack achieves a member inference AUC of 0.68 and accuracy of 0.63 against LLaVA-Video-7B-Qwen2-Video-Only.
- The membership signal is entangled with video-specific factors such as motion complexity and temporal span.
- There is an urgent need for the community to systematically evaluate and mitigate privacy risks in VideoLLMs.

**Limitations**: The attack is evaluated on a single model (LLaVA-Video-7B-Qwen2-Video-Only), and the moderate AUC of 0.68 suggests the attack has limited effectiveness; the abstract does not discuss generalization to other VideoLLM architectures.

### Ward et al. (2025)

**Research question**: How can adversaries robustly choose membership inference attack methods when no single method dominates across different model architectures and dataset domains?

**Methodology**: The authors conduct the largest synthetic data privacy benchmark to date, studying membership inference attacks as a decision-theoretic problem under uncertainty. They propose ensemble membership inference attacks built on individual attacks and evaluate them across various model architectures and dataset domains.

**Key findings**:
- No single membership inference attack constitutes a strictly dominant strategy across diverse model architectures and dataset domains.
- Unsupervised ensembles built on individual attacks offer empirically more robust, regret-minimizing strategies than individual attacks.
- Different MIA methods exploit different privacy leakage signals, creating uncertainty for adversaries in method selection.
- The benchmark reveals significant variation in attack performance depending on the target model and data characteristics.
- Ensemble approaches mitigate the risk of choosing suboptimal attack methods in realistic threat scenarios.

**Limitations**: The abstract does not specify the computational overhead of ensemble methods or discuss potential diminishing returns when combining highly correlated attack signals.

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
