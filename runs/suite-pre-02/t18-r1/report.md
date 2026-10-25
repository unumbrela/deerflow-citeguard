# Systematic Literature Review: Mixture of Experts

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "mixture of experts", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on Mixture of Experts (MoE) reveals a field experiencing rapid diversification across theoretical foundations, architectural innovations, and domain-specific applications. Recent work demonstrates strong convergence on MoE's effectiveness for scaling models efficiently, with particular emphasis on routing mechanisms, expert specialization, and deployment optimization. Theoretical advances in convergence analysis and identifiability conditions provide mathematical grounding for empirical successes, while practical innovations in heterogeneous architectures and pruning techniques address real-world deployment constraints. Security vulnerabilities and efficiency gaps highlight critical challenges requiring attention as MoE architectures scale further.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "mixture of experts", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Routing Mechanisms and Expert Selection

The routing mechanism — determining which experts process which inputs — emerges as a central research focus with both theoretical and empirical dimensions. Avinash (2026) demonstrates that routing in sparse transformers is not merely a load-balancing mechanism but exhibits task-conditioned structure, with prompts from the same task category inducing highly similar routing signatures (within-category similarity 0.8435 vs. across-category 0.6225, Cohen's d = 1.44). A logistic regression classifier achieved 92.5% accuracy on four-way task classification using only routing signatures, suggesting routing encodes meaningful task structure.

Theoretical work by Nguyen et al. (2025) provides convergence rate analysis for softmax gating mechanisms, showing that experts satisfying strong identifiability conditions require polynomially many data points for estimation, while those violating these conditions (such as linear experts) require exponentially many data points due to intrinsic parameter interactions expressible via partial differential equations. This theoretical foundation helps explain why certain routing architectures succeed while others fail.

Empirical studies reveal gaps between theoretical efficiency and practical performance. Rokah et al. (2026) found that naively implemented conditional routing does not yield inference speedups on modern hardware at CIFAR10 scale, highlighting the implementation challenge of realizing MoE's theoretical efficiency benefits.

### Theme 2: Architectural Innovations and Heterogeneity

Moving beyond homogeneous expert architectures, recent work explores heterogeneous designs where experts differ in capacity and specialization. Wang et al. (2024) proposed Heterogeneous MoE (HMoE), where experts vary in size to handle tokens of differing complexity. Their novel training objective encourages frequent activation of smaller experts, achieving lower loss with fewer activated parameters and outperforming homogeneous MoE on pre-training benchmarks.

Lu et al. (2024) addressed deployment efficiency through post-training expert pruning and skipping techniques, demonstrating that plug-and-play sparsification can simultaneously reduce model sizes and increase inference speed while maintaining performance across tasks. This work represents a practical approach to MoE optimization without requiring specialized hardware.

The multi-level MoE architecture proposed by Hu et al. (2025) applies mixture of experts at both intra-level and inter-level granularities for multimodal entity linking, using switch mechanisms to dynamically select features from relevant information regions. This hierarchical approach outperformed state-of-the-art methods, suggesting that MoE benefits compound when applied at multiple architectural levels.

### Theme 3: Domain-Specific Applications

MoE architectures demonstrate strong performance across diverse application domains. In multimodal settings, Hu et al. (2025) leveraged MoE for entity linking across text and images, while Shaabana et al. (2024) applied sparsely-gated MoE to video relationship detection, identifying language triplets in <subject, predicate, object> format. Their MoE-VRD approach employed multiple small expert models specializing in visual relationship learning, achieving superior performance compared to monolithic networks without increasing computational complexity.

Rokah et al. (2026) specifically investigated MoE behavior in image classification, comparing dense, SoftMoE, and SparseMoE heads on CIFAR10. Both MoE variants achieved slightly higher validation accuracy than dense baselines while maintaining balanced expert utilization through regularization, though SoftMoE exhibited higher sharpness in Hessian-based metrics.

### Theme 4: Theoretical Foundations and Convergence Analysis

Two papers provide rigorous theoretical foundations for MoE architectures. Nguyen and Ho (2025) analyzed parameter estimation in deviated Gaussian mixture of experts, constructing novel Voronoi-based loss functions that capture convergence rates of maximum likelihood estimation more accurately than generalized Wasserstein loss. Their framework addresses goodness-of-fit testing between null hypothesis (known function only) and alternative hypothesis (full mixture distribution).

Rushing (2024) offered a philosophical and theoretical perspective, proving that MoE possesses greater functional capacity than equivalent Bayesian methods in the limiting case, explaining MoE's empirical superiority despite Bayesian methods' stronger inductive guarantees. The work frames MoE as a form of abductive reasoning in the Peircian sense of hypothesis construction, bridging machine learning practice with philosophical foundations.

### Theme 5: Security and Vulnerability Analysis

As MoE architectures scale for production deployment, security considerations become critical. Hayes et al. (2024) identified a vulnerability in expert routing strategies with cross-batch dependencies, demonstrating that malicious queries can affect model outputs on benign queries when grouped in the same batch. Their proof-of-concept attack in a toy experimental setting reveals a "buffer overflow" vulnerability specific to MoE architectures, highlighting the need for routing strategies without cross-batch dependencies in production systems.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on MoE's effectiveness for conditional computation and scaling efficiency. Lu et al. (2024), Wang et al. (2024), and Hu et al. (2025) all demonstrate that expert specialization — whether through pruning, heterogeneity, or multi-level architectures — improves performance-efficiency tradeoffs. Theoretical analyses by Nguyen et al. (2025) and Nguyen and Ho (2024) both emphasize the importance of identifiability conditions and algebraic structure in determining convergence rates.

**Disagreements**: A notable tension exists between theoretical efficiency claims and empirical realization. While MoE architectures promise computational efficiency through conditional computation, Rokah et al. (2026) found that naive implementations do not yield inference speedups on modern hardware at CIFAR10 scale. This suggests that efficiency benefits may only materialize at larger scales or with optimized implementations, creating a gap between theoretical motivation and practical deployment.

## Gaps and Open Questions

Several critical gaps emerge across the surveyed literature:

1. **Scalability and Implementation**: Multiple papers acknowledge that theoretical efficiency benefits require optimized implementations not yet realized on modern hardware (Rokah et al., 2026). The conditions under which MoE provides practical speedups remain unclear.

2. **Security and Robustness**: Only one paper (Hayes et al., 2024) addresses security vulnerabilities, yet the identified cross-batch dependency vulnerability likely affects many production MoE systems. Systematic analysis of attack surfaces and mitigation strategies is needed.

3. **Expert Specialization Mechanisms**: While heterogeneous architectures show promise (Wang et al., 2024), principled methods for determining expert count, size distribution, and specialization criteria remain underexplored.

4. **Cross-Domain Generalization**: Most application-specific papers focus on single domains (vision, language, multimodal). Systematic comparison of MoE behavior across domains would clarify which benefits transfer and which are domain-specific.

5. **Training Dynamics**: Several papers note challenges in balancing expert activation and training heterogeneous experts, but comprehensive analysis of training dynamics, convergence behavior, and optimization landscapes is limited.

## Per-Paper Annotations

### Avinash (2026)

**Research question**: Does MoE routing exhibit task-conditioned structure, or is it merely a load-balancing mechanism?
**Methodology**: Introduced routing signatures as vector representations of expert activation patterns across layers, analyzed using OLMoE-1B-7B-0125-Instruct with permutation and load-balancing baselines for statistical validation.
**Key findings**:
- Within-category routing similarity (0.8435 ± 0.0879) significantly exceeds across-category similarity (0.6225 ± 0.1687), Cohen's d = 1.44
- Logistic regression achieves 92.5% ± 6.1% accuracy on four-way task classification using only routing signatures
- Task structure becomes increasingly apparent in deeper layers
- Routing is a measurable task-sensitive component, not merely a balancing mechanism
**Limitations**: Analysis limited to single model architecture (OLMoE-1B-7B-0125-Instruct); generalizability to other MoE architectures and task domains requires further investigation.

### Hayes et al. (2024)

**Research question**: Are expert routing strategies with cross-batch dependencies vulnerable to adversarial attacks where malicious queries can affect model outputs on benign queries?
**Methodology**: Demonstrated a proof-of-concept attack in a toy experimental setting showing that malicious queries sent to MoE models can affect outputs on benign queries when grouped in the same batch due to cross-batch dependencies in routing strategies.
**Key findings**:
- Expert routing strategies with cross-batch dependencies create security vulnerabilities in MoE models
- Malicious queries can influence model behavior on benign queries through batch-level routing interactions
- The vulnerability represents a form of buffer overflow attack specific to MoE architectures
- Proof-of-concept demonstration confirms theoretical vulnerability in experimental toy setting
**Limitations**: The attack is demonstrated only in a toy experimental setting, not on production-scale models. The practical impact on real-world MoE deployments and potential mitigation strategies are not explored.

### Hu et al. (2025)

**Research question**: How can Multimodal Entity Linking address mention ambiguity (lack of semantic content in textual context) and dynamic selection of relevant modal content?
**Methodology**: Proposed MMoE model with four components: description-aware mention enhancement using LLMs to identify WikiData descriptions, multimodal feature extraction encoders, and intra-level and inter-level mixture of experts modules with switch mechanism to dynamically select features from relevant information regions.
**Key findings**:
- MMoE effectively mitigates mention ambiguity by leveraging LLMs to identify matching WikiData descriptions for mentions
- The switch mixture of experts mechanism enables adaptive selection of features from relevant information regions
- Multi-level MoE architecture (intra-level and inter-level) improves multi-grained semantic matching
- Extensive experiments demonstrate MMoE outperforms state-of-the-art MEL approaches
**Limitations**: The abstract does not explicitly discuss computational overhead of incorporating LLMs for description enhancement or scalability concerns. No discussion of performance on low-resource languages or domains beyond WikiData.

### Lu et al. (2024)

**Research question**: How can deployment efficiency of MoE LLMs be enhanced through expert-level sparsification techniques without requiring specialized hardware?
**Methodology**: Proposed novel post-training approaches for both task-agnostic and task-specific expert pruning and skipping of MoE LLMs, designed as plug-and-play techniques to improve deployment efficiency.
**Key findings**:
- Expert pruning and skipping methods simultaneously reduce model sizes and increase inference speed
- Performance is maintained across a wide range of tasks despite parameter reduction
- Post-training sparsification approaches work without requiring specifically designed hardware
- Both task-agnostic and task-specific pruning strategies are viable for MoE optimization
**Limitations**: Abstract does not explicitly acknowledge limitations; deployment challenges for immense parameter sizes remain a fundamental constraint even with pruning techniques.

### Nguyen and Ho (2024)

**Research question**: How can parameter estimation in deviated Gaussian mixture of experts be accurately performed for goodness-of-fit testing when data may come from either a known function or a mixture distribution?
**Methodology**: Constructed novel Voronoi-based loss functions based on algebraic structure of expert functions and distinguishability between the known function g0 and mixture part to capture convergence rates of maximum likelihood estimation for deviated Gaussian mixture of experts models.
**Key findings**:
- Voronoi-based loss functions capture convergence rates of MLE more accurately than existing approaches
- The proposed loss functions characterize local convergence rates of parameter estimation more precisely than generalized Wasserstein loss
- The algebraic structure of expert functions and distinguishability properties enable theoretical analysis of estimation convergence
- The framework addresses goodness-of-fit testing between null hypothesis (g0 only) and alternative hypothesis (full mixture)
**Limitations**: The work is primarily theoretical with focus on convergence rate analysis. The abstract does not discuss practical implementation, computational complexity of the Voronoi-based approach, or empirical validation on real-world datasets.

### Nguyen et al. (2025)

**Research question**: What are the convergence rates for parameter and expert estimation in MoE models equipped with softmax gating mechanisms?
**Methodology**: Performed theoretical convergence analysis of parameter estimation and expert estimation under standard softmax gating and its variants, including dense-to-sparse and hierarchical softmax gating.
**Key findings**:
- Experts satisfying strong identifiability conditions (e.g., two-layer feed-forward networks) require polynomially many data points for estimation
- Linear experts violating strong identifiability require exponentially many data points due to intrinsic parameter interactions
- Parameter interactions can be expressed in the language of partial differential equations
- Theoretical results provide insights into sample-efficient expert structure design
**Limitations**: Theoretical analysis requires rigorous guarantee substantiation; practical implications for real-world MoE deployment need empirical validation.

### Rokah et al. (2026)

**Research question**: How do MoE architectures behave in image classification settings regarding predictive performance, expert utilization, and generalization compared to dense models?
**Methodology**: Compared dense, SoftMoE, and SparseMoE classifier heads on CIFAR10 under comparable model capacity, using Hessian-based sharpness metrics and loss surface perturbation analyses to evaluate generalization.
**Key findings**:
- Both MoE variants achieve slightly higher validation accuracy than dense baseline while maintaining balanced expert utilization
- SoftMoE exhibits higher sharpness (largest eigenvalue and trace of loss Hessian) compared to Dense and SparseMoE
- All models achieve comparable generalization performance despite curvature differences
- Naively implemented conditional routing does not yield inference speedups on modern hardware at this scale
- Qualitative differences exist in non-local behavior under finite parameter perturbations between dense and MoE models
**Limitations**: Gap between theoretical and realized efficiency in sparse MoE models; conditional routing benefits not realized on modern hardware without optimized implementation.

### Rushing (2024)

**Research question**: Why do MoE methods outperform Bayesian methods despite Bayesian approaches having stronger inductive guarantees?
**Methodology**: Proved that MoE has greater functional capacity than equivalent Bayesian methods in the limiting case, then validated through experiments on non-limiting cases.
**Key findings**:
- MoE demonstrates greater functional capacity than equivalent Bayesian methods in the limiting case
- Experimental results on non-limiting cases vouchsafe the theoretical proof
- MoE operates as a type of abductive reasoning in the Peircian sense of hypothesis construction
- Greater functional capacity explains MoE's superior performance despite weaker inductive guarantees
**Limitations**: Theoretical proof applies to limiting case while experiments conducted on non-limiting cases; connection between capacity and abductive reasoning requires further philosophical and empirical exploration.

### Shaabana et al. (2024)

**Research question**: How can visual relationship detection overcome the computational/inference gap in connecting vision and language while improving model stability and generalization beyond monolithic neural networks?
**Methodology**: Introduced MoE-VRD that identifies language triplets in <subject, predicate, object> format using multiple small expert models specializing in visual relationship learning and object tagging, with sparsely-gated mixture of experts enabling conditional computation without increasing computational complexity.
**Key findings**:
- Multiple specialized experts outperform single monolithic networks in visual relationship detection
- Sparsely-gated MoE enables conditional computation, enhancing neural network capacity without additional computational complexity
- The approach effectively addresses action recognition requirements for establishing subject-object relationships
- MoE-VRD demonstrates superior performance compared to state-of-the-art visual relationship detection methods
**Limitations**: The abstract does not specify the number of experts used or criteria for expert specialization. No discussion of training complexity, convergence behavior, or performance on rare relationship types.

### Wang et al. (2024)

**Research question**: Can heterogeneous experts with varying sizes and capacities improve upon homogeneous MoE models for handling input data with varying complexity?
**Methodology**: Proposed Heterogeneous MoE (HMoE) where experts differ in size and capacity, with a novel training objective that encourages frequent activation of smaller experts to enhance computational efficiency and parameter utilization while addressing expert activation imbalance.
**Key findings**:
- Heterogeneous experts with diverse capacities handle varying token complexity more effectively than homogeneous experts
- The proposed training objective successfully encourages frequent activation of smaller experts
- HMoE achieves lower loss with fewer activated parameters compared to conventional homogeneous MoE
- HMoE outperforms homogeneous MoE models on various pre-training evaluation benchmarks
**Limitations**: Code release is pending acceptance, limiting reproducibility. The abstract does not discuss training overhead, expert size selection criteria, or potential challenges in balancing heterogeneous expert training.

## References

Avinash, M. S. R. (2026). Task-conditioned routing signatures in sparse mixture-of-experts transformers. arXiv. https://arxiv.org/abs/2603.11114

Hayes, J., Shumailov, I., & Yona, I. (2024). Buffer overflow in mixture of experts. arXiv. https://arxiv.org/abs/2402.05526

Hu, Z., Gutiérrez-Basulto, V., Xiang, Z., Li, R., & Pan, J. Z. (2025). Multi-level mixture of experts for multimodal entity linking. arXiv. https://arxiv.org/abs/2507.07108

Lu, X., Liu, Q., Xu, Y., Zhou, A., Huang, S., Zhang, B., Yan, J., & Li, H. (2024). Not all experts are equal: Efficient expert pruning and skipping for mixture-of-experts large language models. arXiv. https://arxiv.org/abs/2402.14800

Nguyen, H., & Ho, N. (2024). On parameter estimation in deviated Gaussian mixture of experts. arXiv. https://arxiv.org/abs/2402.05220

Nguyen, H., Ho, N., & Rinaldo, A. (2025). Convergence rates for softmax gating mixture of experts. arXiv. https://arxiv.org/abs/2503.03213

Rokah, A., Veress, D., Caulk, C., & Sharan, S. (2026). Mixture-of-experts models in vision: Routing, optimization, and generalization. arXiv. https://arxiv.org/abs/2601.15021

Rushing, B. (2024). Peirce in the machine: How mixture of experts models perform hypothesis construction. arXiv. https://arxiv.org/abs/2406.17150

Shaabana, A., Gharaee, Z., & Fieguth, P. (2024). Video relationship detection using mixture of experts. arXiv. https://arxiv.org/abs/2403.03994

Wang, A., Sun, X., Xie, R., Li, S., Zhu, J., Yang, Z., Zhao, P., Han, J. N., Kang, Z., Wang, D., Okazaki, N., & Xu, C.-Z. (2024). HMoE: Heterogeneous mixture of experts for language modeling. arXiv. https://arxiv.org/abs/2408.10681
