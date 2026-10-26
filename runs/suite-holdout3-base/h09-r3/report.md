# Systematic Literature Review: Membership Inference Attacks

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search for "membership inference", published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Membership inference attacks (MIAs) have evolved significantly over the past two years, with research expanding beyond traditional black-box settings to address emerging architectures including Retrieval-Augmented Generation (RAG), multimodal large language models, and graph neural networks. The surveyed literature reveals three major trends: (1) attacks are becoming more stealthy and computationally efficient, with new methods requiring less than 5% of prior computational costs while achieving superior performance; (2) researchers are developing more comprehensive privacy measurement frameworks that go beyond exact-match membership to capture range-based and distributional privacy leakage; and (3) theoretical foundations are strengthening, with Bayes-optimal frameworks providing principled justifications for attack design. The field is maturing from empirical demonstrations toward theoretically-grounded, scalable methodologies that can audit privacy risks in large-scale production systems.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "membership inference", sorted by relevance and published between 2024-01-01 and 2026-10-26. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Computational Efficiency and Scalability

A dominant theme across the surveyed literature is the pursuit of more computationally efficient membership inference attacks that maintain or improve attack accuracy. Traditional MIAs require training hundreds of shadow models, creating prohibitive computational overhead for practical privacy auditing.

Du et al. (2025) introduce Imitative Membership Inference Attack (IMIA), which strategically constructs a small number of target-informed imitative models rather than hundreds of independent shadow models, achieving superior performance with less than 5% of the computational cost of state-of-the-art approaches. Similarly, Lassila et al. (2025) develop BASE and G-BASE, tractable approximations of Bayes-optimal membership inference that match or exceed prior state-of-the-art performance at significantly lower computational cost.

Wu et al. (2024) address scalability from a measurement perspective, proposing a discrepancy-based privacy metric that does not require training multiple models and can be applied to large ImageNet classification models in-the-wild. These advances collectively demonstrate that the field is moving toward practical, deployable privacy auditing tools rather than purely academic demonstrations.

### Theme 2: Expanding Attack Surfaces to New Architectures

As machine learning architectures evolve, membership inference research has expanded to address novel attack surfaces including Retrieval-Augmented Generation systems, multimodal models, and self-supervised visual encoders.

Naseh et al. (2025) present the first stealthy membership inference attack targeting RAG datastores, crafting natural-text queries that remain answerable only when the target document is present. Their Interrogation Attack achieves 2x improvement in TPR@1%FPR over prior methods while evading detection mechanisms that identify adversarial prompts up to 76x more frequently.

Emelyanov et al. (2025) extend perturbation-based membership inference to multimodal large language models, addressing the instabilities introduced through multimodal component adaptation and distribution shifts. Their FiMMIA framework demonstrates effective attacks across various fine-tuned multimodal models where prior LLM-focused methods fall short.

Zhu et al. (2025) tackle visual self-supervised models in realistic black-box settings where training paradigms and implementation details are unknown, proposing PartCrop which exploits shared part-aware capabilities across different self-supervised learning approaches.

### Theme 3: Theoretical Foundations and Optimality

Recent work has strengthened the theoretical foundations of membership inference, moving from heuristic approaches toward principled, Bayes-optimal frameworks.

Lassila et al. (2025) derive the Bayes-optimal membership inference rule for node-level attacks against graph neural networks, showing that BASE and the prior RMIA attack are equivalent under specific hyperparameter settings—providing a principled justification for existing methods. This theoretical grounding enables more systematic attack design rather than empirical trial-and-error.

Suri et al. (2024) provide theoretical analysis demonstrating that black-box access is insufficient for optimal membership inference when models are trained with stochastic gradient descent, establishing that white-box access to model parameters is necessary for optimal attacks. Their Inverse Hessian Attack (IHA) explicitly leverages parameter information through inverse-Hessian vector products.

Du et al. (2025) offer theoretical analyses for both their Cascading MIA (adaptive setting) and Proxy MIA (non-adaptive setting), proving performance guarantees particularly in the low false-positive regime crucial for privacy risk evaluation.

### Theme 4: Comprehensive Privacy Measurement Beyond Exact Match

Researchers are recognizing that traditional membership inference—testing exact data point matches—fails to capture the full scope of privacy leakage, prompting development of more comprehensive measurement frameworks.

Tao and Shokri (2024) introduce Range Membership Inference Attacks (RaMIAs) that test whether a model was trained on any data within a specified semantic range, rather than exact matches. Their principled statistical test captures privacy loss more accurately across tabular, image, and language data, enabling more meaningful privacy auditing.

Wu et al. (2024) propose a discrepancy-based metric that upper-bounds the advantage of a family of membership inference attacks, providing theoretical guarantees on privacy leakage without requiring multiple model training. This metric achieves higher advantage than existing methods on models trained with sophisticated training recipes.

### Theme 5: Attack Strategy Innovation

Novel attack strategies continue to emerge, exploiting different information sources and dependencies to improve inference performance.

Galichin et al. (2024) propose GLiRA, exploiting the connection between vulnerability to distillation-based functionality stealing and susceptibility to membership inference. Their knowledge distillation-guided approach significantly improves likelihood ratio tests in black-box settings where target model architecture is unknown.

Du et al. (2025) introduce two complementary innovations: Cascading MIA exploits membership dependencies between query instances through conditional shadow training in adaptive settings, while Proxy MIA employs proxy selection strategies to identify samples with similar behaviors for posterior odds testing in non-adaptive settings.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of computational efficiency for practical deployment. Du et al. (2025), Lassila et al. (2025), and Wu et al. (2024) all demonstrate that their methods achieve superior or comparable performance with dramatically reduced computational requirements. There is also broad agreement that traditional black-box assumptions are insufficient—Suri et al. (2024) prove white-box access is theoretically necessary for optimal inference, while multiple papers develop methods that exploit additional information sources.

**Disagreements**: The literature does not show fundamental disagreements, but rather complementary approaches for different settings. The distinction between adaptive and non-adaptive attack settings (Du et al., 2025) represents different threat models rather than conflicting claims. Similarly, white-box methods (Suri et al., 2024) and black-box methods (Galichin et al., 2024) address different adversary capabilities rather than contradicting each other.

## Gaps and Open Questions

Several gaps emerge from the surveyed literature:

1. **Defense evaluation is limited**: While Zhu et al. (2025) evaluate defenses including early stopping, differential privacy, and shrinking crop scale range, most papers focus on attack development without comprehensive defense analysis. The effectiveness of defenses across different attack types remains underexplored.

2. **Domain generalization**: Most evaluations focus on image classification or specific model types. Galichin et al. (2024) note their evaluation is limited to image classification and may not generalize to NLP or tabular data. Cross-domain robustness of attacks requires further investigation.

3. **Real-world deployment constraints**: Several papers acknowledge their methods were tested on toy encoders or small-scale datasets (Zhu et al., 2025), with scaling studies being relatively recent additions. Practical deployment in production systems with strict latency and resource constraints needs more attention.

4. **Multimodal-specific challenges**: Emelyanov et al. (2025) identify distribution shifts in multimodal datasets affecting MIA performance, but the framework's performance on unseen modalities and sensitivity to perturbation strategies remain open questions.

5. **Parameter access assumptions**: Suri et al. (2024) advocate for white-box methods but acknowledge that parameter access may not be available in many practical scenarios. Bridging the gap between theoretically optimal white-box attacks and practically feasible black-box methods requires further work.

## Per-Paper Annotations

### Du, Chen, Xiao, Ribeiro, and Li (2025) - Cascading and Proxy Membership Inference Attacks

**Research question**: How can membership inference attacks be improved by exploiting membership dependencies between query instances in both adaptive and non-adaptive attack settings?

**Methodology**: The authors propose CMIA (Cascading MIA) for adaptive settings using conditional shadow training to incorporate membership dependencies, and PMIA (Proxy MIA) for non-adaptive settings using a proxy selection strategy with membership posterior odds testing.

**Key findings**:
- CMIA and PMIA substantially outperform existing membership inference attacks in both adaptive and non-adaptive settings
- Both attacks are particularly effective in the low false-positive regime, crucial for privacy risk evaluation
- Theoretical analyses are provided for both attack frameworks
- Exploiting membership dependencies between instances significantly boosts inference performance

**Limitations**: The adaptive setting requires training shadow models after accessing query instances, which may be computationally expensive or impractical in some scenarios.

### Du, Chen, Xiao, Ribeiro, and Li (2025) - Imitative Membership Inference Attack

**Research question**: How can membership inference attacks be performed with significantly reduced computational overhead while maintaining or improving attack accuracy?

**Methodology**: Introduces IMIA (Imitative Membership Inference Attack), which employs a novel imitative training technique to strategically construct a small number of target-informed imitative models that closely replicate the target model's behavior for inference.

**Key findings**:
- IMIA substantially outperforms existing membership inference attacks across various attack settings
- IMIA requires less than 5% of the computational cost of state-of-the-art approaches
- Target-informed imitative models can effectively replicate target model behavior for inference purposes
- The imitative training technique eliminates the need for hundreds of independent shadow models

**Limitations**: Potential concerns include generalizability across different model architectures and the assumption that imitative models can be successfully constructed for various target models.

### Emelyanov, Kudriashov, and Fenogenova (2025) - FiMMIA: scaling semantic perturbation-based membership inference across modalities

**Research question**: How can membership inference attacks be effectively performed on multimodal large language models given the instabilities from multimodal component adaptation and distribution shifts across multiple inputs?

**Methodology**: The authors identify distribution shifts in existing datasets, release an extended baseline pipeline to detect them, and generalize perturbation-based membership inference methods to multimodal LLMs through FiMMIA—a modular framework that trains a neural network to analyze the target model's behavior on perturbed inputs.

**Key findings**:
- Existing MIA methods for LLMs fall short on multimodal LLMs due to instabilities from multimodal component adaptation
- Distribution shifts exist in existing multimodal datasets that affect MIA performance
- FiMMIA's perturbation-based approach effectively captures distributional differences between members and non-members
- Comprehensive evaluations demonstrate effectiveness across various fine-tuned multimodal models

**Limitations**: Potential concerns include the framework's performance on unseen modalities, the computational cost of training the analysis neural network, and possible sensitivity to perturbation strategies.

### Galichin, Pautov, Zhavoronkin, Rogov, and Oseledets (2024) - GLiRA: Black-Box Membership Inference Attack via Knowledge Distillation

**Research question**: How can membership inference attack efficiency be improved in black-box settings where the target model's architecture is unknown to the attacker?

**Methodology**: The authors propose GLiRA, a distillation-guided approach that leverages knowledge distillation to significantly improve the likelihood ratio test used in membership inference attacks on black-box neural networks.

**Key findings**:
- Knowledge distillation significantly improves the efficiency of likelihood ratio membership inference attacks
- GLiRA outperforms current state-of-the-art membership inference attacks in black-box settings
- The method is effective across multiple image classification datasets and model architectures
- The approach exploits the connection between vulnerability to distillation-based functionality stealing and susceptibility to membership inference

**Limitations**: The evaluation is focused on image classification tasks and may not generalize to other domains such as natural language processing or tabular data.

### Lassila, Östman, Ngo, and Graell i Amat (2025) - Practical Bayes-Optimal Membership Inference Attacks

**Research question**: What is the Bayes-optimal membership inference rule for node-level membership inference attacks against graph neural networks, and how can it be made tractable in practice?

**Methodology**: Building on the Bayesian decision-theoretic framework, the authors derive the Bayes-optimal membership inference rule for node-level MIAs against graph neural networks and introduce BASE and G-BASE as tractable approximations.

**Key findings**:
- G-BASE achieves superior performance compared to previously proposed classifier-based node-level MIA attacks on graph data
- BASE (applicable to non-graph data) matches or exceeds the performance of prior state-of-the-art MIAs like LiRA and RMIA
- BASE and G-BASE operate at significantly lower computational cost than existing methods
- BASE and RMIA are equivalent under a specific hyperparameter setting, providing Bayes-optimal justification for RMIA

**Limitations**: Potential concerns include the assumptions required for the Bayesian framework and the specific hyperparameter settings needed for equivalence with existing methods.

### Naseh, Peng, Suri, Chaudhari, Oprea, and Houmansadr (2025) - Riddle Me This! Stealthy Membership Inference for Retrieval-Augmented Generation

**Research question**: How can membership inference attacks be performed on Retrieval-Augmented Generation (RAG) systems in a stealthy manner that evades detection mechanisms?

**Methodology**: The authors present Interrogation Attack (IA), which crafts natural-text queries that are answerable only when the target document is present in the RAG datastore, avoiding unnatural patterns that trigger detection.

**Key findings**:
- Successfully infers document membership with only 30 queries per target document
- Detectors identify adversarial prompts from existing methods up to 76x more frequently than IA-generated queries
- Achieves 2x improvement in TPR@1%FPR over prior inference attacks across diverse RAG configurations
- Costs less than $0.02 per document inference

**Limitations**: The attack is specifically designed for RAG systems and may not generalize to other architectures; the abstract does not explicitly discuss limitations or potential countermeasures.

### Suri, Zhang, and Evans (2024) - Do Parameters Reveal More than Loss for Membership Inference?

**Research question**: Does white-box access to model parameters provide better membership inference capability than black-box access, particularly for models trained with stochastic gradient descent?

**Methodology**: The authors provide theoretical analysis showing that black-box access is insufficient for optimal membership inference with SGD, and develop IHA (Inverse Hessian Attack), a white-box attack that explicitly uses model parameters through inverse-Hessian vector products.

**Key findings**:
- Black-box access is not sufficient for optimal membership inference when models are trained with stochastic gradient descent
- Optimal membership inference requires white-box access to model parameters
- IHA successfully exploits model parameters using inverse-Hessian vector products
- Both privacy auditors and adversaries can benefit from access to model parameters

**Limitations**: The IHA attack requires white-box access which may not be available in many practical scenarios, and computing inverse-Hessian vector products may have computational overhead.

### Tao and Shokri (2024) - Range Membership Inference Attacks

**Research question**: How can privacy risk measurement be improved beyond exact-match membership inference to capture privacy leakage from similar or partially overlapping memorized data?

**Methodology**: The authors introduce Range Membership Inference Attacks (RaMIAs) that test whether a model was trained on any data within a specified semantic range, formulating a principled statistical test for the composite hypotheses involved.

**Key findings**:
- RaMIAs capture privacy loss more accurately and comprehensively than standard membership inference attacks
- The approach works across various data types including tabular, image, and language data
- RaMIAs enable more meaningful privacy auditing of machine learning algorithms
- Similar or partially overlapping memorized data can reveal the same private information as exact matches

**Limitations**: The effectiveness of RaMIAs depends on appropriately defining ranges based on the semantics of privacy for each application domain.

### Wu, Huang, and Chaudhuri (2024) - Better Membership Inference Privacy Measurement through Discrepancy

**Research question**: How can privacy leakage from machine learning models be measured in a scalable way that works on large, well-generalized models without requiring computationally expensive multiple model training?

**Methodology**: Inspired by discrepancy theory, the authors propose a new empirical privacy metric that serves as an upper bound on the advantage of a family of membership inference attacks, which does not require training multiple models.

**Key findings**:
- The proposed discrepancy-based metric does not require training multiple models, enabling scalability
- The metric can be applied to large ImageNet classification models in-the-wild
- The metric achieves higher advantage than existing metrics on models trained with sophisticated training recipes
- The metric provides an upper bound on the advantage of a family of membership inference attacks

**Limitations**: The metric being an upper bound may be loose in some cases, and the approach may have specific assumptions about the model family or training procedures.

### Zhu, Zha, Li, and Wang (2025) - A Unified and Scalable Membership Inference Method for Visual Self-supervised Encoder via Part-aware Capability

**Research question**: How can membership inference be performed on visual self-supervised models when the training method, paradigm, and implementation details are unknown to the adversary?

**Methodology**: The authors propose PartCrop, which exploits the shared part-aware capability among self-supervised models by cropping parts of objects in images and querying responses in the representation space.

**Key findings**:
- PartCrop is effective across different self-supervised paradigms including masked image modeling and contrastive learning
- Successfully attacks models with different training protocols and architectures using three image datasets
- Three defense approaches are effective: early stopping, differential privacy, and shrinking crop scale range
- PartCrop-v2 introduces structural improvements enabling scaling to larger models and datasets

**Limitations**: Initial prototype testing was conducted on toy visual encoders and small-scale image datasets, though the authors do quantitatively study scaling impacts.

## References

Du, Y., Chen, Y., Xiao, H., Ribeiro, B., & Li, N. (2025). Cascading and proxy membership inference attacks. arXiv. https://arxiv.org/abs/2507.21412v3

Du, Y., Chen, Y., Xiao, H., Ribeiro, B., & Li, N. (2025). Imitative membership inference attack. arXiv. https://arxiv.org/abs/2509.06796v3

Emelyanov, A., Kudriashov, S., & Fenogenova, A. (2025). FiMMIA: Scaling semantic perturbation-based membership inference across modalities. arXiv. https://arxiv.org/abs/2512.02786v1

Galichin, A. V., Pautov, M., Zhavoronkin, A., Rogov, O. Y., & Oseledets, I. (2024). GLiRA: Black-box membership inference attack via knowledge distillation. arXiv. https://arxiv.org/abs/2405.07562v1

Lassila, M., Östman, J., Ngo, K.-H., & Graell i Amat, A. (2025). Practical Bayes-optimal membership inference attacks. arXiv. https://arxiv.org/abs/2505.24089v2

Naseh, A., Peng, Y., Suri, A., Chaudhari, H., Oprea, A., & Houmansadr, A. (2025). Riddle me this! Stealthy membership inference for Retrieval-Augmented Generation. arXiv. https://arxiv.org/abs/2502.00306v2

Suri, A., Zhang, X., & Evans, D. (2024). Do parameters reveal more than loss for membership inference? arXiv. https://arxiv.org/abs/2406.11544v4

Tao, J., & Shokri, R. (2024). Range membership inference attacks. arXiv. https://arxiv.org/abs/2408.05131v3

Wu, R., Huang, P., & Chaudhuri, K. (2024). Better membership inference privacy measurement through discrepancy. arXiv. https://arxiv.org/abs/2405.15140v1

Zhu, J., Zha, J., Li, D., & Wang, L. (2025). A unified and scalable membership inference method for visual self-supervised encoder via part-aware capability. arXiv. https://arxiv.org/abs/2505.10351v1
