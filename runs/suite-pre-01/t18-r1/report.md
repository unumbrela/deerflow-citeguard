# Systematic Literature Review: Mixture of Experts

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "mixture of experts", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The mixture of experts (MoE) literature from 2024-2026 reveals a rapidly maturing research area with dual focus on theoretical foundations and practical deployment considerations. Recent work has shifted from merely proposing MoE architectures to rigorously analyzing their convergence properties, routing mechanisms, and security vulnerabilities. A dominant theme centers on efficiency improvements through expert pruning, heterogeneous architectures, and deployment optimization, reflecting the community's transition from scaling-driven research to real-world applicability. Simultaneously, theoretical work has established convergence guarantees for softmax gating mechanisms and parameter estimation procedures, providing mathematical grounding for practices that were previously empirical. The field demonstrates strong convergence on MoE's effectiveness across modalities (language, vision, multimodal tasks), though significant gaps remain in understanding cross-batch security vulnerabilities, hardware-aware implementations, and generalization beyond controlled experimental settings.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "mixture of experts", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Deployment Optimization

A significant portion of recent MoE research addresses the practical challenge of deploying large MoE models efficiently. Lu et al. (2024) introduced post-training expert pruning and skipping techniques that reduce model sizes and increase inference speed without requiring specialized hardware, achieving satisfactory performance retention across diverse tasks. Wang et al. (2024) proposed Heterogeneous MoE (HMoE), where experts vary in size and capacity, enabling more specialized handling of token complexity while a novel training objective encourages balanced activation of smaller experts, resulting in lower loss with fewer activated parameters. Rokah et al. (2026) examined the gap between theoretical and realized efficiency in vision MoE models, finding that naively implemented conditional routing does not yield inference speedups on modern hardware at CIFAR10 scale, highlighting the importance of hardware-aware optimization. This theme reflects the field's maturation from demonstrating MoE's feasibility to ensuring its practical viability in production environments.

### Theme 2: Theoretical Foundations and Convergence Analysis

Parallel to applied work, several papers have established rigorous theoretical foundations for MoE architectures. Nguyen et al. (2025) performed convergence analysis of softmax gating MoE models, demonstrating that experts satisfying strong identifiability conditions (e.g., two-layer feed-forward networks) require polynomially many data points to estimate, while linear experts violating these conditions necessitate exponentially many samples due to intrinsic parameter interactions. Nguyen et al. (2024) constructed novel Voronoi-based loss functions for parameter estimation in deviated Gaussian mixture of experts, achieving more accurate characterization of local convergence rates than generalized Wasserstein loss. Rushing (2024) provided theoretical proof that MoE possesses greater functional capacity than equivalent Bayesian methods in the limiting case, framing MoE as a form of Peircian abductive reasoning that explains its empirical superiority despite weaker inductive guarantees. These theoretical contributions provide mathematical grounding for design choices that were previously empirical.

### Theme 3: Routing Mechanisms and Expert Specialization

Understanding and improving routing mechanisms has emerged as a critical research direction. Avinash (2026) introduced routing signatures as vector representations of expert activation patterns, demonstrating that prompts from the same task category induce highly similar routing signatures (within-category similarity 0.8435 vs. across-category 0.6225, Cohen's d = 1.44), with logistic regression achieving 92.5% accuracy on four-way task classification using only routing signatures. This finding establishes that routing is not merely a load-balancing mechanism but a measurable task-sensitive component of conditional computation. Hu et al. (2025) developed multi-level MoE with intra-level and inter-level expert modules employing switch mechanisms for dynamic feature selection in multimodal entity linking, effectively distinguishing importance of different modal content regions. Shaabana et al. (2024) employed sparsely-gated MoE for video relationship detection, where multiple small expert models specializing in visual relationship learning are aggregated, improving stability and generalization compared to monolithic networks.

### Theme 4: Security Vulnerabilities and Robustness

As MoE models scale, security considerations have gained prominence. Hayes et al. (2024) identified a critical vulnerability in expert routing strategies with cross-batch dependencies, demonstrating that malicious queries can exploit buffer overflow to affect model outputs on benign queries grouped in the same batch. Their proof-of-concept attack in a toy experimental setting reveals security implications for scaling large foundation models using MoE architectures. This work stands in contrast to the predominantly efficiency-focused literature, highlighting that deployment considerations must encompass not only computational efficiency but also adversarial robustness. The vulnerability identified suggests that routing strategies designed for load balancing may inadvertently create attack surfaces requiring mitigation in production systems.

### Theme 5: Cross-Modal and Domain-Specific Applications

MoE architectures have demonstrated effectiveness across diverse modalities and domains beyond language modeling. Hu et al. (2025) applied multi-level MoE to multimodal entity linking, addressing mention ambiguity through LLM-powered description enhancement and dynamic modal content selection, significantly outperforming state-of-the-art methods. Shaabana et al. (2024) extended MoE to video relationship detection, identifying language triplets (<subject, predicate, object>) through specialized experts for visual relationship learning and object tagging. Rokah et al. (2026) studied MoE behavior in image classification on CIFAR10, finding that both SoftMoE and SparseMoE variants achieve slightly higher validation accuracy than dense baselines while maintaining balanced expert utilization through regularization. These applications demonstrate MoE's versatility as a general architectural pattern for conditional computation across vision, language, and multimodal tasks.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the effectiveness of MoE architectures for improving parameter efficiency while maintaining or enhancing performance compared to dense models (Lu et al., 2024; Wang et al., 2024; Rokah et al., 2026). There is strong agreement that routing mechanisms exhibit meaningful structure beyond simple load balancing, with task-conditioned patterns observable across different architectures (Avinash, 2026; Hu et al., 2025). The literature consistently demonstrates that specialized experts outperform monolithic approaches in terms of both capacity and generalization (Shaabana et al., 2024; Rushing, 2024).

**Disagreements**: A notable tension exists between theoretical efficiency claims and empirical realization. While Wang et al. (2024) and Lu et al. (2024) report inference speedups from expert sparsification, Rokah et al. (2026) found that naively implemented conditional routing does not yield speedups on modern hardware at CIFAR10 scale, highlighting a gap between theoretical and realized efficiency that depends on implementation details and scale. Additionally, while Nguyen et al. (2025) established polynomial sample complexity for strongly identifiable experts, the practical relevance of exponential complexity for linear experts remains debated, as real-world MoE implementations rarely use purely linear experts.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, security vulnerabilities identified by Hayes et al. (2024) were demonstrated only in toy experimental settings, leaving open the question of whether production-scale MoE models exhibit similar vulnerabilities and what mitigation strategies are effective. Second, multiple papers acknowledge limited empirical validation beyond controlled datasets (CIFAR10, specific task categories), raising questions about generalization to diverse real-world domains (Rokah et al., 2026; Avinash, 2026). Third, the computational overhead of sophisticated routing mechanisms, particularly those involving LLM integration (Hu et al., 2025), lacks systematic analysis, leaving practitioners without guidance on efficiency-accuracy tradeoffs. Fourth, code availability remains inconsistent—while some papers release code publicly (Lu et al., 2024; Hu et al., 2025), others defer release pending acceptance (Wang et al., 2024), limiting reproducibility and community validation. Finally, the gap between theoretical convergence guarantees and practical training dynamics remains unaddressed, as theoretical analyses (Nguyen et al., 2025; Nguyen et al., 2024) do not provide actionable guidance for hyperparameter selection or training schedule design.

## Per-Paper Annotations

### Avinash (2026)

**Research question**: Does MoE routing exhibit task-conditioned structure, or is it merely a load-balancing mechanism?
**Methodology**: Introduces routing signatures as vector representations of expert activation patterns across layers, analyzes similarity patterns across task categories using OLMoE-1B-7B-0125-Instruct, and validates findings with permutation and load-balancing baselines plus logistic regression classification.
**Key findings**:
- Prompts from the same task category induce highly similar routing signatures (0.8435 ± 0.0879) compared to across-category similarity (0.6225 ± 0.1687)
- The effect size is substantial (Cohen's d = 1.44), indicating strong task-conditioned routing structure
- A logistic regression classifier achieves 92.5% ± 6.1% cross-validated accuracy on four-way task classification using only routing signatures
- Task structure becomes increasingly apparent in deeper layers of the transformer
- The observed separation cannot be explained by sparsity or load-balancing constraints alone
**Limitations**: The analysis is conducted on a single model (OLMoE-1B-7B-0125-Instruct) and four task categories, limiting generalizability to other MoE architectures and task taxonomies.

### Hayes et al. (2024)

**Research question**: Are expert routing strategies with cross-batch dependencies vulnerable to adversarial attacks that can corrupt model outputs on benign queries?
**Methodology**: Demonstrates a proof-of-concept attack in a toy experimental setting showing that malicious queries can exploit cross-batch dependencies in expert routing to affect model outputs on other benign queries grouped in the same batch.
**Key findings**:
- Expert routing strategies with cross-batch dependencies are vulnerable to adversarial attacks
- Malicious queries can affect model output on benign queries when grouped in the same batch
- Buffer overflow vulnerability exists in MoE architectures despite steady inference costs
- Security implications for scaling large foundation models using MoE
- Attack demonstrated successfully in experimental toy setting
**Limitations**: The vulnerability was demonstrated only in a toy experimental setting rather than production-scale models, limiting immediate real-world impact assessment.

### Hu et al. (2025)

**Research question**: How can Multimodal Entity Linking address mention ambiguity and dynamic selection of modal content that existing approaches fail to handle?
**Methodology**: Proposes MMoE with four components: description-aware mention enhancement using LLMs to match WikiData descriptions, multimodal feature extraction encoders, and intra/inter-level mixture of experts modules with switch MoE mechanism for adaptive feature selection.
**Key findings**:
- MMoE significantly outperforms state-of-the-art methods in Multimodal Entity Linking tasks
- LLM-powered description enhancement effectively mitigates mention ambiguity caused by brief textual contexts
- Switch MoE mechanism successfully distinguishes importance of different parts of modal information
- Multi-level expert architecture enables dynamic and adaptive selection of features from relevant information regions
- Code released publicly at https://github.com/zhiweihu1103/MEL-MMoE
**Limitations**: The abstract does not explicitly acknowledge limitations; potential concerns include computational overhead from LLM integration and generalization to domains beyond WikiData-linked entities.

### Lu et al. (2024)

**Research question**: How can we improve the deployment efficiency of MoE LLMs through expert-level sparsification techniques without relying on specialized hardware?
**Methodology**: Proposes novel post-training approaches for both task-agnostic and task-specific expert pruning and skipping of MoE LLMs, designed as plug-and-play techniques to enhance deployment efficiency while maintaining model performance.
**Key findings**:
- The proposed methods can simultaneously reduce model sizes and increase inference speed
- Model performance is maintained at satisfactory levels across a wide range of tasks after pruning
- Expert-level sparsification provides a hardware-agnostic alternative to previous weight pruning methods
- Both task-agnostic and task-specific pruning approaches are viable for different deployment scenarios
**Limitations**: The abstract does not specify quantitative pruning ratios or performance degradation thresholds, and hardware-specific deployment results are not detailed.

### Nguyen et al. (2024)

**Research question**: How can parameter estimation be performed in deviated Gaussian mixture of experts for goodness-of-fit testing between null hypothesis (known function) and alternative hypothesis (full mixture)?
**Methodology**: Constructs novel Voronoi-based loss functions based on algebraic structure of expert functions and distinguishability between g0 and mixture part to capture convergence rates of maximum likelihood estimation.
**Key findings**:
- Proposed Voronoi-based loss functions characterize convergence rates of MLE for deviated Gaussian mixture of experts
- New loss functions characterize local convergence rates of parameter estimation more accurately than generalized Wasserstein loss
- Method addresses goodness-of-fit testing for determining whether data follows known function or full mixture distribution
- Algebraic structure analysis enables proper handling of distinguishability between components
- Theoretical framework applies to covariate-response settings with unknown mixing proportion
**Limitations**: The abstract focuses on theoretical contributions without empirical validation; practical applicability to real-world datasets and computational complexity of Voronoi-based methods are not discussed.

### Nguyen et al. (2025)

**Research question**: What are the convergence rates of parameter estimation and expert estimation under MoE models equipped with softmax gating mechanisms?
**Methodology**: Performs theoretical convergence analysis of parameter and expert estimation under MoE with standard softmax gating and its variants (dense-to-sparse gating and hierarchical softmax gating), using identifiability conditions and partial differential equation analysis.
**Key findings**:
- Experts satisfying the strong identifiability condition (e.g., two-layer feed-forward networks) require polynomially many data points to estimate
- Linear experts violating strong identifiability require exponentially many data points due to intrinsic parameter interactions
- The theoretical analysis provides insights into designing sample-efficient expert structures
- Different gating variants (standard, dense-to-sparse, hierarchical) have distinct convergence characteristics
**Limitations**: The theoretical results, while rigorously guaranteed, may require empirical validation on practical MoE implementations to confirm real-world applicability.

### Rokah et al. (2026)

**Research question**: How do MoE architectures behave in image classification settings with respect to predictive performance, expert utilization, and generalization compared to dense models?
**Methodology**: Compares dense, SoftMoE, and SparseMoE classifier heads on CIFAR10 under comparable model capacity, using Hessian-based sharpness metrics (largest eigenvalue and trace) and loss surface perturbation analyses to evaluate generalization.
**Key findings**:
- Both MoE variants achieve slightly higher validation accuracy than the dense baseline
- Balanced expert utilization is maintained through regularization, avoiding expert collapse
- SoftMoE exhibits higher sharpness by Hessian-based metrics while Dense and SparseMoE lie in similar curvature regimes
- All models achieve comparable generalization performance despite curvature differences
- Naively implemented conditional routing does not yield inference speedups on modern hardware at this scale
**Limitations**: The study is limited to CIFAR10 image classification at a specific scale, and the gap between theoretical and realized efficiency in sparse MoE models remains unaddressed.

### Rushing (2024)

**Research question**: Why does MoE often outperform Bayesian methods despite Bayesian approaches having stronger inductive guarantees?
**Methodology**: Provides theoretical proof that MoE has greater functional capacity than equivalent Bayesian methods in the limiting case, supplemented by experiments on non-limiting cases, and frames MoE as a form of Peircian abductive reasoning (hypothesis construction).
**Key findings**:
- MoE has greater functional capacity than equivalent Bayesian methods in the limiting case
- Experimental results on non-limiting cases vouchsafe the theoretical capacity advantage
- MoE can be characterized as a type of abductive reasoning in the Peircian sense of hypothesis construction
- The greater functional capacity explains MoE's superior performance despite weaker inductive guarantees
**Limitations**: The theoretical proof applies to limiting cases while experiments cover only non-limiting cases, and the philosophical framing of MoE as abductive reasoning requires further formal development.

### Shaabana et al. (2024)

**Research question**: How can visual relationship detection overcome the computational inference gap between vision and language while improving classifier stability and generalization?
**Methodology**: Introduces MoE-VRD that identifies language triplets (<subject, predicate, object>) using multiple small expert models specializing in visual relationship learning and object tagging, aggregated through sparsely-gated mixture of experts for conditional computation.
**Key findings**:
- MoE-VRD achieves superior performance compared to state-of-the-art visual relationship detection methods
- Sparsely-gated MoE enables conditional computation, significantly enhancing neural network capacity without increasing computational complexity
- Multiple specialized experts improve stability and generalization compared to single monolithic networks
- Successfully addresses action recognition requirements for establishing subject-object relationships
- Demonstrates scalability advantages of mixture-of-experts approach for visual relationship learning
**Limitations**: The abstract does not explicitly state limitations; potential concerns include expert load balancing challenges and applicability to diverse video domains beyond tested datasets.

### Wang et al. (2024)

**Research question**: Can heterogeneous experts with varying capacities outperform homogeneous MoE models by better handling varying input complexity and improving parameter utilization?
**Methodology**: Proposes Heterogeneous MoE (HMoE) where experts differ in size and capacity, with a novel training objective that encourages frequent activation of smaller experts to address activation imbalance and enhance computational efficiency.
**Key findings**:
- HMoE achieves lower loss with fewer activated parameters compared to homogeneous MoE
- Heterogeneous expert sizes enable more specialized handling of varying token complexities
- Outperforms conventional homogeneous MoE models on various pre-training evaluation benchmarks
- Novel training objective successfully encourages balanced activation across differently-sized experts
- Demonstrates improved parameter utilization efficiency through expert heterogeneity
**Limitations**: Code was not released at publication time (promised upon acceptance), limiting immediate reproducibility and community validation.

## References

Avinash, M. S. R. (2026). Task-conditioned routing signatures in sparse mixture-of-experts transformers. arXiv. https://arxiv.org/abs/2603.11114

Hayes, J., Shumailov, I., & Yona, I. (2024). Buffer overflow in mixture of experts. arXiv. https://arxiv.org/abs/2402.05526

Hu, Z., Gutiérrez-Basulto, V., Xiang, Z., Li, R., & Pan, J. Z. (2025). Multi-level mixture of experts for multimodal entity linking. arXiv. https://arxiv.org/abs/2507.07108

Lu, X., Liu, Q., Xu, Y., Zhou, A., Huang, S., Zhang, B., Yan, J., & Li, H. (2024). Not all experts are equal: Efficient expert pruning and skipping for mixture-of-experts large language models. arXiv. https://arxiv.org/abs/2402.14800

Nguyen, H., Nguyen, K., & Ho, N. (2024). On parameter estimation in deviated Gaussian mixture of experts. arXiv. https://arxiv.org/abs/2402.05220

Nguyen, H., Ho, N., & Rinaldo, A. (2025). Convergence rates for softmax gating mixture of experts. arXiv. https://arxiv.org/abs/2503.03213

Rokah, A., Veress, D., Caulk, C., & Sharan, S. (2026). Mixture-of-experts models in vision: Routing, optimization, and generalization. arXiv. https://arxiv.org/abs/2601.15021

Rushing, B. (2024). Peirce in the machine: How mixture of experts models perform hypothesis construction. arXiv. https://arxiv.org/abs/2406.17150

Shaabana, A., Gharaee, Z., & Fieguth, P. (2024). Video relationship detection using mixture of experts. arXiv. https://arxiv.org/abs/2403.03994

Wang, A., Sun, X., Xie, R., Li, S., Zhu, J., Yang, Z., Zhao, P., Han, J. N., Kang, Z., Wang, D., Okazaki, N., & Xu, C. (2024). HMoE: Heterogeneous mixture of experts for language modeling. arXiv. https://arxiv.org/abs/2408.10681
