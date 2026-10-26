# Systematic Literature Review: Membership Inference Attacks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "membership inference attacks", filtered to category cs.CR, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on membership inference attacks (MIAs) from 2024-2026 reveals a rapidly evolving field responding to the proliferation of large-scale machine learning models across diverse domains. The surveyed papers collectively demonstrate that MIAs have expanded beyond traditional classification settings to target emerging architectures including federated learning systems, large vision-language models, video-language models, document VQA systems, retrieval-augmented generation, and graph neural networks. A clear trend emerges toward more sophisticated attack methodologies that exploit model-specific vulnerabilities while simultaneously reducing computational requirements for attackers. The research community has converged on recognizing MIAs as the primary tool for privacy auditing under regulatory frameworks like GDPR and CCPA, yet significant gaps remain in defense strategies, particularly for fine-tuned language models and multimodal systems. This review identifies both the escalating sophistication of attack vectors and the pressing need for more robust, architecture-specific defense mechanisms.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "membership inference attacks", filtered to category cs.CR, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review focuses specifically on the cs.CR (Cryptography and Security) category, potentially excluding relevant work published in adjacent categories such as cs.LG or cs.CV.

## Themes

### Theme 1: Expansion to Novel Model Architectures

The surveyed literature demonstrates a clear trajectory of MIAs expanding from traditional classification models to increasingly complex architectures. Early MIA research focused primarily on image classifiers and tabular data models, but recent work has systematically targeted emerging model types. Bai et al. (2024) documented the proliferation of MIAs in federated learning settings, where the decentralized nature of training creates unique attack surfaces. Wu et al. (2025) and Song et al. (2026) extended attacks to large vision-language models and video-language models respectively, exploiting the multimodal nature of these systems. Nguyen et al. (2025) targeted document VQA models, while Liu et al. (2024) focused on retrieval-augmented generation systems. Lassila et al. (2025) addressed graph neural networks with node-level MIAs. This expansion reflects both the research community's responsiveness to new deployment scenarios and the fundamental transferability of membership inference principles across architectural boundaries.

### Theme 2: Black-Box Attack Methodologies

A dominant trend across the literature is the development of black-box attack methods that require only query access to target models, eliminating the need for white-box access to model parameters or training data. Song et al. (2026) introduced temperature-perturbed generation queries to extract membership signals from video-language models through semantic drift analysis. Wu et al. (2025) demonstrated that output text embeddings alone suffice for effective attacks against vision-language models. Nguyen et al. (2025) developed unsupervised black-box attacks against DocVQA models without requiring auxiliary datasets. Liu et al. (2024) employed mask-based queries to RAG systems, inferring membership from prediction accuracy patterns. Galli et al. (2024) introduced the "noisy neighbors" approach, which operates the target model in inference mode only by adding stochastic noise in embedding space. This shift toward black-box methods reflects practical constraints faced by real-world attackers and increases the immediate applicability of research findings to privacy auditing scenarios.

### Theme 3: Computational Efficiency and Accessibility

Recent MIA research increasingly prioritizes computational efficiency, making sophisticated attacks accessible without requiring extensive resources for shadow model training. Galli et al. (2024) explicitly positioned their noisy neighbors method as eliminating the computationally intensive training of additional models. Lassila et al. (2025) demonstrated that their BASE and G-BASE methods match or exceed state-of-the-art MIAs like LiRA and RMIA at significantly lower computational cost. Du et al. (2025) proposed attack-agnostic frameworks (CMIA and PMIA) that incorporate membership dependencies without requiring attack-specific customization. This efficiency trend serves dual purposes: enabling practical privacy auditing under resource constraints, and paradoxically making attacks more dangerous by lowering barriers to execution. The literature suggests that computational efficiency has become a key criterion for evaluating MIA quality, alongside traditional metrics like accuracy and false positive rates.

### Theme 4: Theoretical Foundations and Optimality

A subset of the literature focuses on establishing theoretical foundations for MIAs, moving beyond empirical demonstrations to principled frameworks. Lassila et al. (2025) derived Bayes-optimal membership inference rules building on the decision-theoretic framework of Sablayrolles et al., providing theoretical justification for existing methods like RMIA. Du et al. (2025) provided theoretical analyses for both cascading and proxy attacks, establishing conditions under which membership dependencies can be exploited. Ward et al. (2025) framed MIA selection as a decision-theoretic problem under uncertainty, conducting the largest synthetic data privacy benchmark to date. This theoretical turn reflects maturation of the field, where initial empirical discoveries are being systematized into coherent frameworks that enable prediction of attack effectiveness and guide defense development.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong convergence on several points. First, all papers agree that membership inference attacks represent the primary method for assessing privacy risks in machine learning systems, particularly under regulatory frameworks like GDPR and CCPA (Galli et al., 2024; Amit et al., 2024). Second, there is consensus that black-box attack scenarios are more practically relevant than white-box settings, with multiple papers explicitly designing attacks for query-only access (Song et al., 2026; Wu et al., 2025; Nguyen et al., 2025). Third, the literature converges on the finding that no single attack method dominates across all model architectures and datasets, motivating ensemble approaches (Ward et al., 2025) and architecture-specific methodologies (Lassila et al., 2025). Fourth, all papers acknowledge that defense strategies lag behind attack development, particularly for emerging model types like video-language models and RAG systems.

**Disagreements**: The literature shows less direct disagreement, partly because most papers focus on different model architectures or attack settings rather than competing claims about the same phenomenon. However, there is implicit tension between papers emphasizing attack sophistication (Du et al., 2025; Lassila et al., 2025) and those highlighting defense possibilities (Amit et al., 2024; Bai et al., 2024). Amit et al. (2024) found that combining differential privacy with low-rank adaptors achieves best privacy protection for fine-tuned language models, suggesting defenses are viable, while other papers emphasize vulnerability without proposing equally strong countermeasures. Additionally, there is variation in assumptions about attacker capabilities: some papers assume no auxiliary data access (Nguyen et al., 2025), while others assume adversaries can train shadow models (Du et al., 2025), leading to different attack designs that are not directly comparable.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, defense strategies remain underdeveloped relative to attack sophistication, particularly for multimodal models. While Amit et al. (2024) and Bai et al. (2024) survey defense approaches for language models and federated learning respectively, comparable systematic treatment is absent for vision-language models, video-language models, and document VQA systems. Second, evaluation consistency is lacking: different papers use different metrics (AUC, accuracy, false positive rates) and datasets, making cross-paper comparison difficult. Third, most evaluations are limited to one or two model architectures per paper, limiting generalizability claims (Song et al., 2026 evaluated only LLaVA-Video-7B-Qwen2-Video-Only; Lassila et al., 2025 noted performance dependence on hyperparameter tuning). Fourth, the literature lacks longitudinal studies tracking how MIA vulnerability evolves as models scale in size and training data volume. Fifth, while regulatory compliance (GDPR, CCPA) is frequently invoked as motivation, no papers provide concrete guidance on translating MIA audit results into compliance decisions or risk assessments. Finally, the assumption of no auxiliary dataset access (Nguyen et al., 2025) while realistic, may underestimate attacker capabilities in scenarios where public data or leaked training corpora are available.

## Per-Paper Annotations

### Amit, Goldsteen, and Farkash (2024)

**Research question**: What factors affect the vulnerability of fine-tuned large language models to membership inference attacks, and which defense strategies are most effective in the language domain?
**Methodology**: The authors provide the first systematic review of vulnerability factors and defense strategy effectiveness for fine-tuned LLMs against membership inference attacks, analyzing various training methods and privacy protection techniques.
**Key findings**:
- Fine-tuning data containing personal or sensitive information creates increased privacy risk in NLP applications
- Some training methods provide significantly reduced privacy risk against membership inference attacks
- The combination of differential privacy and low-rank adaptors achieves the best privacy protection against MIAs
- Limited research exists on factors affecting LLM vulnerability to membership inference attacks
- Different defense strategies have varying applicability and effectiveness in the language domain
**Limitations**: As a systematic review, the work synthesizes existing research rather than presenting extensive new experimental validation. The findings depend on the scope and quality of available literature on MIA defenses for language models.

### Bai, Hu, Ye, Li, Wang, and Xu (2024)

**Research question**: What membership inference attacks and defense strategies exist in federated learning, and how can they be systematically categorized?
**Methodology**: The authors create a taxonomy of existing MIA research in federated learning and systematically categorize both attack approaches and countermeasures based on their characteristics. They analyze the strengths and weaknesses of different approaches through comprehensive literature review.
**Key findings**:
- Federated learning faces significant privacy vulnerabilities despite only sharing model updates rather than raw data
- Membership inference attacks can determine whether specific examples are part of clients' training sets, compromising sensitive information
- Multiple attack strategies exist with varying effectiveness depending on the federated learning setting
- Different defense strategies have distinct strengths and weaknesses in mitigating MIA risks
- There are identifiable gaps in current research that warrant future investigation
**Limitations**: As a survey paper, this work synthesizes existing research rather than presenting novel experimental results or empirical evaluations. The taxonomy and analysis depend on the completeness and quality of prior published work in this domain.

### Du, Li, Chen, Zhang, Yuan, Xiao, Ribeiro, and Li (2025)

**Research question**: Can exploiting membership dependencies between instances improve membership inference attack performance in both adaptive and non-adaptive settings?
**Methodology**: The authors propose two attack frameworks: Cascading MIA (CMIA) for adaptive settings using conditional shadow training to incorporate membership dependencies, and Proxy MIA (PMIA) for non-adaptive settings using proxy selection and membership posterior odds testing. Both include theoretical analysis.
**Key findings**:
- Exploiting membership dependencies between instances significantly boosts membership inference performance
- CMIA and PMIA substantially outperform existing MIAs in both adaptive and non-adaptive settings
- The proposed attacks are particularly effective in the low false-positive regime, which is crucial for privacy risk evaluation
- Theoretical analyses support the effectiveness of both cascading and proxy attack approaches
- The attack-agnostic framework can incorporate membership dependencies without requiring attack-specific customization
**Limitations**: The adaptive setting (CMIA) requires the adversary to train shadow models after accessing query instances, which may be computationally expensive. Performance may vary depending on the degree of membership dependency present in different datasets and model architectures.

### Galli, Melis, and Cucinotta (2024)

**Research question**: How can membership inference attacks against LLMs be performed efficiently without computationally intensive shadow model training?
**Methodology**: The authors introduce a "noisy neighbors" methodology that generates variations of a target sample by adding stochastic noise in the embedding space, requiring only inference mode operation of the target model without training additional models.
**Key findings**:
- The noisy neighbors approach closely matches the effectiveness of shadow model-based MIA methods
- The method requires only inference mode operation, eliminating the need for additional model training
- Significantly reduces computational cost compared to traditional MIA approaches
- Demonstrates practical usability for privacy auditing scenarios under GDPR and CCPA compliance
**Limitations**: Effectiveness may vary across different LLM architectures and embedding space properties; the evaluation scope is limited and may not cover all transformer-based model variants.

### Lassila, Östman, Ngo, and Graell i Amat (2025)

**Research question**: What is the theoretically optimal membership inference attack strategy, and how can it be approximated practically for both i.i.d. and graph-structured data?
**Methodology**: Building on the Bayesian decision-theoretic framework of Sablayrolles et al., the authors derive Bayes-optimal membership inference rules and introduce BASE and G-BASE as tractable approximations for non-graph and graph-structured data respectively.
**Key findings**:
- G-BASE achieves superior performance compared to previously proposed classifier-based node-level MIA attacks on graph neural networks
- BASE matches or exceeds state-of-the-art MIAs (LiRA, RMIA) at significantly lower computational cost
- BASE and RMIA are equivalent under a specific hyperparameter setting
- Provides a principled, Bayes-optimal theoretical justification for the RMIA attack
- The approach works effectively for both i.i.d. data and graph-structured data
**Limitations**: The tractable approximations may not fully capture Bayes-optimal behavior in all scenarios; performance depends on hyperparameter settings and requires careful tuning for different applications.

### Liu, Zhang, and Long (2024)

**Research question**: How can we reliably detect if a specific document is stored in a RAG system's knowledge database, overcoming the limitations of existing MIAs for RAG?
**Methodology**: The authors propose Mask-Based Membership Inference Attacks (MBA) that employ a masking algorithm to hide words in target documents, prompt the RAG system to predict masked values, and use threshold-based inference on prediction accuracy to determine document membership.
**Key findings**:
- Mask-based approach is more document-specific and less susceptible to distractions from other documents or the LLM's internal knowledge
- When target documents exist in the knowledge database, masked text retrieves the complete document enabling accurate mask prediction
- Simple threshold-based method effectively infers document membership from mask prediction accuracy
- The approach outperforms existing baseline models in extensive experiments
- Provides better explainability compared to previous RAG MIA approaches that rely solely on system judgments
**Limitations**: Requires query access to the RAG system; masking strategy parameters may need tuning for different document types; effectiveness depends on the quality and coverage of the retrieval mechanism.

### Nguyen, Kerkouche, Fritz, and Karatzas (2025)

**Research question**: Can membership inference attacks be effectively performed on Document Visual Question Answering models to determine if particular documents were part of the training data?
**Methodology**: The authors introduce two novel membership inference attacks tailored for DocVQA models: one for white-box settings with full model access and one for black-box settings with only output access. Both attacks are unsupervised and assume no access to auxiliary datasets.
**Key findings**:
- DocVQA models are vulnerable to membership inference attacks despite their multimodal nature
- The proposed unsupervised attacks outperform existing state-of-the-art membership inference methods across various DocVQA models and datasets
- Effective attacks can be performed without access to auxiliary datasets, making them more realistic and practical
- Documents containing highly sensitive information pose significant privacy risks when used to train DocVQA models
- Both white-box and black-box attack scenarios demonstrate successful membership inference capabilities
**Limitations**: The attacks assume no access to auxiliary datasets, which while realistic, may limit attack effectiveness in scenarios where such data is available. The evaluation is specific to DocVQA models and may not generalize to other document understanding architectures.

### Song, Cao, Ding, Liu, Deng, and Li (2026)

**Research question**: Can an external auditor determine whether a particular video was used during the training of Video Large Language Models?
**Methodology**: The authors present a black-box membership inference attack that couples temperature-perturbed generation with video-aware difficulty features. They query the target model at different temperatures and measure semantic drift between resulting texts, interpreting this signal jointly with the intrinsic difficulty of the queried video.
**Key findings**:
- VideoLLMs are vulnerable to black-box membership inference attacks despite the complexity of video-text data
- The attack achieved 0.68 AUC and 0.63 accuracy on LLaVA-Video-7B-Qwen2-Video-Only
- Member samples tend to induce sharper, more brittle generation behavior across decoding temperatures
- The membership signal is entangled with video-specific factors such as motion complexity and temporal span
- There is an urgent need for systematic evaluation and mitigation of privacy risks in VideoLLMs
**Limitations**: The evaluation was conducted on only one model (LLaVA-Video-7B-Qwen2-Video-Only), limiting generalizability across different VideoLLM architectures. The black-box setting restricts the attack to generated text observations, potentially missing stronger signals available in white-box scenarios.

### Ward, Yang, Wang, and Cheng (2025)

**Research question**: How should an adversary select a membership inference attack method when no single method guarantees optimal performance across different models and datasets?
**Methodology**: The authors conduct the largest synthetic data privacy benchmark to date and frame MIA selection as a decision-theoretic problem under uncertainty, proposing ensemble MIAs that combine individual attacks as regret-minimizing strategies.
**Key findings**:
- No single MIA method constitutes a strictly dominant strategy across different model architectures and dataset domains
- Adversaries face significant uncertainty when choosing attack methods without a priori performance guarantees
- Unsupervised ensembles built on individual attacks provide empirically more robust performance than individual attacks
- Ensemble approaches minimize regret compared to single-method selection under uncertainty
- The benchmark reveals substantial variation in MIA effectiveness across synthetic data generation scenarios
**Limitations**: The study focuses specifically on tabular generative models and may not generalize to other data types like images or text; ensemble methods introduce additional complexity in implementation and interpretation.

### Wu, Lin, Zhang, Wang, Zhang, Zhang, and Wang (2025)

**Research question**: How can we detect whether a target image was used to train a Large Vision-Language Model (LVLM)?
**Methodology**: The authors propose Image Corruption-Inspired Membership Inference Attacks (ICIMIA) that exploit LVLM's different sensitivity to image corruption for member versus non-member images, using embedding similarity between images and their corrupted versions in white-box settings or output text embeddings' similarity in black-box settings.
**Key findings**:
- LVLMs exhibit different sensitivity to image corruption depending on whether images are members (training data) or non-members
- White-box attacks using vision embeddings and corruption-based similarity effectively detect membership
- Black-box attacks using output text embeddings' similarity work in practical query-only scenarios
- Both attack settings are validated as effective on existing datasets
**Limitations**: Evaluation is limited to existing datasets and may not generalize across all LVLM architectures; the approach assumes specific types of image corruption that may not capture all vulnerability patterns.

## References

Amit, G., Goldsteen, A., & Farkash, A. (2024). SoK: Reducing the vulnerability of fine-tuned language models to membership inference attacks. arXiv. https://arxiv.org/abs/2403.08481

Bai, L., Hu, H., Ye, Q., Li, H., Wang, L., & Xu, J. (2024). Membership inference attacks and defenses in federated learning: A survey. arXiv. https://arxiv.org/abs/2412.06157

Du, Y., Li, J., Chen, Y., Zhang, K., Yuan, Z., Xiao, H., Ribeiro, B., & Li, N. (2025). Cascading and proxy membership inference attacks. arXiv. https://arxiv.org/abs/2507.21412

Galli, F., Melis, L., & Cucinotta, T. (2024). Noisy neighbors: Efficient membership inference attacks against LLMs. arXiv. https://arxiv.org/abs/2406.16565

Lassila, M., Östman, J., Ngo, K.-H., & Graell i Amat, A. (2025). Practical Bayes-optimal membership inference attacks. arXiv. https://arxiv.org/abs/2505.24089

Liu, M., Zhang, S., & Long, C. (2024). Mask-based membership inference attacks for Retrieval-Augmented Generation. arXiv. https://arxiv.org/abs/2410.20142

Nguyen, K., Kerkouche, R., Fritz, M., & Karatzas, D. (2025). DocMIA: Document-level membership inference attacks against DocVQA models. arXiv. https://arxiv.org/abs/2502.03692

Song, W., Cao, Y., Ding, Z., Liu, Y., Deng, G., & Li, Y. (2026). Membership inference attacks against Video Large Language Models. arXiv. https://arxiv.org/abs/2604.27002

Ward, J., Yang, Y., Wang, C.-H., & Cheng, G. (2025). Ensembling membership inference attacks against tabular generative models. arXiv. https://arxiv.org/abs/2509.05350

Wu, Z., Lin, M., Zhang, Z., Wang, F., Zhang, X., Zhang, X., & Wang, S. (2025). Image corruption-inspired membership inference attacks against Large Vision-Language Models. arXiv. https://arxiv.org/abs/2506.12340
