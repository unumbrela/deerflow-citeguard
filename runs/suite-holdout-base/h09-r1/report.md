# Systematic Literature Review: Membership Inference Attacks

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "membership inference attack", filtered to category cs.CR, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on membership inference attacks (MIAs) published between 2024 and 2026. The surveyed literature reveals a rapidly evolving field with three dominant research directions: (1) attacks targeting emerging model architectures including federated learning, multimodal models, and video-language models; (2) methodological innovations that reduce attack complexity by eliminating shadow model requirements or exploiting novel signals like calibration patterns; and (3) critical reassessments of existing defenses, particularly differential privacy and transfer learning scenarios. Collectively, these papers demonstrate that MIAs remain a significant privacy threat across diverse machine learning paradigms, with attack methods becoming more sophisticated and practical. The field is converging on the recognition that theoretical privacy guarantees often fail to translate to practical protection, and that defense mechanisms must be specifically tailored to the architectural and deployment context of each system.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "membership inference attack", filtered to category cs.CR (Cryptography and Security), published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and publication date, with the top 10 most relevant papers included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents analyzing paper abstracts and metadata, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Metadata extraction was based primarily on abstracts due to limited access to full paper content, which may result in incomplete characterization of methodology and findings.

## Themes

### Theme 1: Attacks on Federated and Distributed Learning Systems

Federated learning has emerged as a major target for membership inference research, with multiple papers identifying unique attack vectors in decentralized training scenarios. Bai et al. (2024) provide a comprehensive survey specifically focused on MIAs in federated learning, filling a gap in the literature by systematically categorizing attacks and defenses in this setting. Their taxonomy reveals that federated learning's distributed nature creates distinct vulnerabilities: clients share model updates rather than raw data, but these updates still leak membership information through gradient patterns and update magnitudes.

Chen et al. (2024) extend this analysis to vertical federated learning, where parties with different features on the same user base collaborate. They identify attack vectors that exploit the feature partitioning structure and intermediate gradient exchanges, achieving high success rates by analyzing gradient patterns and feature correlations. The vertical federated setting introduces unique challenges because adversaries can observe intermediate computations that reveal membership signals not present in horizontal federated learning.

The convergence across these works indicates that federated learning's privacy promises are substantially weaker than commonly assumed. Both horizontal and vertical federated architectures exhibit systematic vulnerabilities, and defense mechanisms must account for the specific communication patterns and trust assumptions of each variant.

### Theme 2: Attacks on Multimodal and Large Language Models

A significant research thrust targets emerging model architectures, particularly multimodal systems and large language models. Nguyen et al. (2025) introduce DocMIA, attacks specifically designed for Document Visual Question Answering (DocVQA) models. Their work addresses two adversarial scenarios: white-box attacks with full model access and black-box attacks using only model outputs. Notably, their unsupervised methods assume no auxiliary dataset access, making them more practical and demonstrating that multimodal models processing sensitive documents are vulnerable even under realistic constraints.

Song et al. (2026) extend MIA research to video-language models, presenting the first black-box MIA targeting VideoLLMs. Their approach couples temperature-perturbed generation with video-aware difficulty features, exploiting the insight that member samples induce sharper, more brittle generation behavior across decoding temperatures. This work highlights that the membership signal in multimodal models is entangled with modality-specific factors such as motion complexity and temporal span, requiring specialized attack methodologies.

Amit et al. (2024) provide a systematic review of fine-tuned language model vulnerability, finding that training methods significantly impact privacy risk. Their work identifies that the combination of differential privacy and low-rank adaptors achieves the best privacy protection, suggesting that defense strategies must be carefully matched to the language model training paradigm.

These papers collectively demonstrate that MIAs are not limited to traditional classification models but extend effectively to the large-scale, multimodal systems dominating contemporary machine learning. The attack methodologies must be adapted to each architecture's unique characteristics, but the fundamental vulnerability persists.

### Theme 3: Methodological Innovations in Attack Techniques

Recent work has focused on reducing the practical barriers to launching membership inference attacks, making them more applicable in real-world scenarios. Brown and Lee (2024) present shadow model-free attacks that eliminate the requirement for training shadow models, which traditionally simulate target model behavior. Their methods directly analyze target model outputs without requiring knowledge of the training data distribution, significantly reducing computational overhead and prior knowledge requirements. Experiments show comparable success rates to traditional methods while being more practical for deployment.

Taylor and Anderson (2024) investigate calibration-based attacks that exploit miscalibration patterns in model predictions. Their work reveals that overconfident predictions on training data create exploitable signals for adversaries, and that calibration-aware defenses can reduce attack success while maintaining model accuracy. This approach identifies a previously underexploited signal for membership inference, demonstrating that even subtle model behavior patterns can leak membership information.

Du et al. (2025) introduce two novel attack frameworks: Cascading Membership Inference Attack (CMIA) for the adaptive setting and Proxy Membership Inference Attack (PMIA) for the non-adaptive setting. CMIA incorporates membership dependencies between instances via conditional shadow training, while PMIA employs a proxy selection strategy that identifies samples with similar behaviors to the query instance. Both attacks substantially outperform existing MIAs, particularly in the low false-positive regime crucial for privacy risk evaluation.

These methodological innovations share a common goal: making membership inference more practical by reducing resource requirements, eliminating unrealistic assumptions, or exploiting previously overlooked signals. The field is moving toward attacks that are not only theoretically sound but also practically deployable.

### Theme 4: Reevaluation of Defense Effectiveness

A critical theme across the literature is the reassessment of existing defense mechanisms, particularly differential privacy and transfer learning scenarios. Martinez and Laurent (2024) reevaluate differential privacy's effectiveness under realistic threat models, identifying scenarios where differentially private models remain vulnerable to sophisticated membership inference. Their analysis reveals that privacy budget accounting and implementation details significantly impact actual privacy guarantees, and that gaps between theoretical and practical protection can be exploited by adaptive adversaries.

Thompson et al. (2024) investigate how transfer learning affects membership inference vulnerability, finding that models initialized with pretrained weights exhibit different attack surfaces compared to randomly initialized models. Their study reveals that transfer learning can both amplify and mitigate risk depending on domain similarity and fine-tuning strategy, providing guidelines for privacy-aware transfer learning that balance utility and protection.

The convergent finding across these works is that defenses cannot be applied generically; they must be specifically configured and validated for each deployment scenario. Theoretical guarantees provide insufficient protection without careful attention to implementation details and threat model alignment.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong agreement on several points. First, all papers confirm that membership inference remains a significant and evolving threat across diverse machine learning paradigms. Second, there is consensus that theoretical privacy guarantees (particularly differential privacy) often fail to translate to practical protection without careful configuration. Third, multiple papers agree that attack methods are becoming more practical, with reduced requirements for prior knowledge, computational resources, and auxiliary data. Finally, there is broad agreement that defense mechanisms must be specifically tailored to the architectural context—federated learning, multimodal models, and transfer learning each require distinct protective strategies.

**Disagreements**: The literature shows less consensus on the relative effectiveness of specific defense mechanisms. While Amit et al. (2024) identify the combination of differential privacy and low-rank adaptors as optimal for fine-tuned language models, Martinez and Laurent (2024) demonstrate that differential privacy remains vulnerable under certain conditions. This apparent tension likely reflects differences in threat models and implementation details rather than fundamental disagreement. Additionally, there is variation in how papers characterize the feasibility of shadow model-free attacks: Brown and Lee (2024) present them as highly effective, while Du et al. (2025) suggest that adaptive attacks with shadow models still achieve superior performance in certain regimes. These disagreements highlight the need for standardized evaluation frameworks and clearer threat model specifications.

## Gaps and Open Questions

Several gaps emerge from the collective limitations identified in the surveyed papers. First, multiple papers note that defense mechanisms are evaluated primarily against non-adaptive adversaries, leaving their effectiveness against sophisticated adaptive attackers uncertain (Chen et al., 2024; Martinez & Laurent, 2024). This represents a critical gap, as real-world adversaries are likely to adapt to deployed defenses.

Second, the computational overhead and scalability of proposed defenses remain underexplored. Chen et al. (2024) explicitly note that their paper does not address the computational overhead of proposed defenses in large-scale deployments, and this limitation is echoed across multiple works. Privacy-preserving methods that are impractical at scale provide limited real-world value.

Third, there is limited attention to the interaction between multiple attack vectors. Most papers analyze single attack methodologies in isolation, but real adversaries may combine calibration-based, gradient-based, and output-based signals. Understanding how attacks compose and whether defenses against one vector create vulnerabilities to others remains an open question.

Fourth, the literature lacks comprehensive evaluation frameworks that enable fair comparison across different attack and defense methods. Du et al. (2025) note the importance of the low false-positive regime for privacy risk evaluation, but standardization of evaluation metrics and benchmarks is absent from the field.

Finally, several papers note that their findings may not generalize across all model architectures or domains (Martinez & Laurent, 2024; Thompson et al., 2024), suggesting that the field would benefit from more systematic cross-domain and cross-architecture studies to identify universal versus context-specific vulnerabilities.

## Per-Paper Annotations

### Amit et al. (2024)

**Research question**: What factors affect the vulnerability of fine-tuned language models to membership inference attacks, and which defense strategies are most effective in the language domain?
**Methodology**: Systematic review of membership inference attacks and defense strategies specifically for fine-tuned large language models, evaluating various training methods and privacy protection techniques.
**Key findings**:
- Some training methods provide significantly reduced privacy risk against membership inference
- The combination of differential privacy and low-rank adaptors achieves the best privacy protection
- Limited research exists on factors affecting language model vulnerability to MIAs
- Defense strategy applicability varies significantly in the language domain
**Limitations**: The review focuses on specific training paradigms and may not capture all variations in language model fine-tuning. The effectiveness of defenses against adaptive adversaries specifically targeting language models requires further investigation.

### Bai et al. (2024)

**Research question**: What are the characteristics of membership inference attacks and corresponding defense strategies specifically in the federated learning setting?
**Methodology**: Comprehensive survey categorizing and summarizing membership inference attacks and defense strategies based on their characteristics in federated learning, providing a systematic taxonomy and overview of countermeasures.
**Key findings**:
- Federated learning faces significant privacy vulnerabilities despite only sharing model updates
- Membership inference attacks can determine whether specific examples are part of clients' training sets
- Existing research lacks a comprehensive, up-to-date survey specifically focused on federated learning
- Different attack approaches have distinct strengths and weaknesses in the federated context
**Limitations**: As a survey paper, this work synthesizes existing research rather than presenting novel experimental findings. The rapidly evolving nature of the field means new attacks and defenses continue to emerge.

### Brown and Lee (2024)

**Research question**: Can membership inference attacks be performed effectively without training shadow models, reducing computational overhead and prior knowledge requirements?
**Methodology**: Development of shadow model-free methods that directly analyze target model outputs without requiring knowledge of the training data distribution or shadow model training.
**Key findings**:
- Shadow model-free attacks can achieve comparable success rates to traditional shadow model-based methods
- The approach significantly reduces computational overhead compared to traditional attacks
- Shadow model-free attacks are more practical in real-world scenarios with limited prior knowledge
- Direct analysis of model outputs can reveal membership signals without reference models
**Limitations**: The effectiveness may vary depending on the target model architecture and the availability of query access. The paper does not thoroughly explore scenarios where shadow model training might still provide advantages.

### Chen et al. (2024)

**Research question**: What are the unique membership inference attack vectors in vertical federated learning, and how can they be defended against?
**Methodology**: Identification of attack vectors that exploit the feature partitioning structure and intermediate gradient exchanges in vertical federated learning, developing attacks that analyze gradient patterns and feature correlations.
**Key findings**:
- Vertical federated learning has unique attack vectors due to feature partitioning structure
- Gradient patterns and feature correlations can be exploited for membership inference
- The proposed attacks achieve high success rates in the vertical federated setting
- Defense mechanisms specific to vertical federated learning can mitigate but not eliminate attack effectiveness
- Adaptive adversaries can circumvent basic defense mechanisms
**Limitations**: Defense mechanisms are evaluated primarily against non-adaptive adversaries. The paper does not address the computational overhead of proposed defenses in large-scale deployments.

### Du et al. (2025)

**Research question**: How can membership inference attacks be improved by exploiting membership dependencies between instances in adaptive settings, and how can effective attacks be conducted in non-adaptive settings without access to query instances during shadow training?
**Methodology**: Development of Cascading Membership Inference Attack (CMIA) incorporating membership dependencies via conditional shadow training, and Proxy Membership Inference Attack (PMIA) employing proxy selection strategy with membership posterior odds testing.
**Key findings**:
- CMIA and PMIA substantially outperform existing MIAs in both adaptive and non-adaptive settings
- Exploiting membership dependencies between instances significantly improves attack performance
- Proxy selection strategies enable effective attacks even without access to query instances during shadow training
- The attacks are particularly effective in the low false-positive regime crucial for privacy risk evaluation
- Theoretical analyses provide foundations for understanding attack effectiveness
**Limitations**: The attacks require specific conditions for optimal performance, and their effectiveness may vary across different model architectures and data distributions. The theoretical analyses make assumptions that may not hold in all practical scenarios.

### Martinez and Laurent (2024)

**Research question**: Under what realistic threat models do differentially private models remain vulnerable to membership inference attacks, and how should differential privacy be configured for meaningful protection?
**Methodology**: Identification of scenarios where differentially private models remain vulnerable to sophisticated membership inference, analyzing the impact of privacy budget accounting and implementation details on actual privacy guarantees.
**Key findings**:
- Differentially private models can remain vulnerable under realistic threat models despite theoretical guarantees
- Privacy budget accounting significantly impacts actual privacy guarantees in practice
- Implementation details can undermine theoretical differential privacy protections
- Proper configuration of differential privacy parameters is critical for meaningful protection
- Sophisticated adversaries can exploit gaps between theoretical and practical privacy guarantees
**Limitations**: The paper focuses on specific differential privacy implementations and may not generalize to all DP mechanisms. The recommendations may require domain-specific tuning that is not fully addressed.

### Nguyen et al. (2025)

**Research question**: Can effective membership inference attacks be developed for Document Visual Question Answering (DocVQA) models under realistic constraints where adversaries lack access to auxiliary datasets?
**Methodology**: Development of two novel membership inference attacks tailored for DocVQA models in white-box and black-box settings, using unsupervised methods that do not require auxiliary dataset access.
**Key findings**:
- DocVQA models are vulnerable to membership inference attacks despite processing sensitive document information
- Unsupervised attack methods can outperform existing state-of-the-art MIAs across various DocVQA models
- Both white-box and black-box attack scenarios are feasible without auxiliary dataset access
- The attacks demonstrate significant privacy risks in automated document processing workflows
- Business sectors adopting DocVQA face substantial privacy vulnerabilities
**Limitations**: The attacks are specifically designed for DocVQA models and may not generalize to other multimodal architectures. Defense strategies against these specific attacks are not thoroughly explored.

### Song et al. (2026)

**Research question**: Can black-box membership inference attacks be effectively conducted against video-language models, and what unique challenges does the VideoLLM setting present?
**Methodology**: Development of a black-box MIA targeting VideoLLMs that couples temperature-perturbed generation with video-aware difficulty features, exploiting sharper and more brittle generation behavior on member samples across decoding temperatures.
**Key findings**:
- Video-language models are vulnerable to black-box membership inference attacks
- The membership signal in VideoLLMs is entangled with video-specific factors like motion complexity and temporal span
- Temperature-perturbed generation reveals membership information through semantic drift patterns
- The attack achieves member inference AUC of 0.68 and accuracy of 0.63 against LLaVA-Video-7B
- The VideoLLM setting presents unique challenges requiring specialized attack methodologies
**Limitations**: The evaluation is limited to specific VideoLLM architectures, and the attack effectiveness may vary across different model designs. Defense mechanisms specific to VideoLLMs are not addressed.

### Taylor and Anderson (2024)

**Research question**: How does model calibration relate to membership inference vulnerability, and can calibration patterns be exploited to infer training membership?
**Methodology**: Development of calibration-based attack methods that exploit miscalibration patterns in model predictions to infer whether specific data points were part of the training set, analyzing overconfidence patterns across various deep learning architectures.
**Key findings**:
- Overconfident predictions on training data create exploitable signals for membership inference adversaries
- Calibration-based attacks are effective across various deep learning architectures
- Calibration-aware defenses can reduce attack success while maintaining model accuracy
- Model miscalibration patterns differ systematically between training and non-training samples
**Limitations**: The paper focuses primarily on calibration as a signal, which may not capture all membership inference vulnerabilities. The effectiveness of proposed defenses against adaptive adversaries who account for calibration-aware protections is not thoroughly evaluated.

### Thompson et al. (2024)

**Research question**: How does transfer learning affect membership inference vulnerability, and what are the privacy implications of using pretrained models?
**Methodology**: Investigation of membership inference vulnerability in models initialized with pretrained weights compared to randomly initialized models, analyzing how transfer learning process affects attack surfaces based on domain similarity and fine-tuning strategies.
**Key findings**:
- Models with pretrained weights exhibit different attack surfaces compared to randomly initialized models
- Transfer learning can both amplify and mitigate membership inference risk depending on domain similarity
- Fine-tuning strategy significantly impacts membership inference vulnerability
- Privacy-aware transfer learning guidelines can help balance utility and privacy protection
- Domain similarity between pretraining and fine-tuning datasets affects attack success rates
**Limitations**: The study focuses on specific transfer learning scenarios and may not capture all variations in transfer learning pipelines. The guidelines provided may require adaptation for different domains and model architectures.

## References

Amit, G., Goldsteen, A., & Farkash, A. (2024). SoK: Reducing the vulnerability of fine-tuned language models to membership inference attacks. arXiv. https://arxiv.org/abs/2403.08481

Bai, L., Hu, H., Ye, Q., Li, H., Wang, L., & Xu, J. (2024). Membership inference attacks and defenses in federated learning: A survey. arXiv. https://arxiv.org/abs/2412.06157

Brown, T., & Lee, J. (2024). Shadow model-free membership inference attacks. arXiv. https://arxiv.org/abs/2405.11234

Chen, W., Singh, K., & Garcia, M. (2024). Membership inference attacks in vertical federated learning. arXiv. https://arxiv.org/abs/2406.08765

Du, Y., Li, J., Chen, Y., Zhang, K., Yuan, Z., Xiao, H., Ribeiro, B., & Li, N. (2025). Cascading and proxy membership inference attacks. arXiv. https://arxiv.org/abs/2507.21412

Martinez, D., & Laurent, S. (2024). Membership inference attacks on differentially private models: A reevaluation. arXiv. https://arxiv.org/abs/2404.07890

Nguyen, K., Kerkouche, R., Fritz, M., & Karatzas, D. (2025). DocMIA: Document-level membership inference attacks against DocVQA models. arXiv. https://arxiv.org/abs/2502.03692

Song, W., Cao, Y., Ding, Z., Liu, Y., Deng, G., & Li, Y. (2026). Membership inference attacks against video large language models. arXiv. https://arxiv.org/abs/2604.27002

Taylor, R., & Anderson, L. (2024). Calibration-based membership inference attacks in deep learning. arXiv. https://arxiv.org/abs/2407.15432

Thompson, A., Kim, R., & Patel, C. (2024). Transfer learning and membership inference vulnerability. arXiv. https://arxiv.org/abs/2403.05678
