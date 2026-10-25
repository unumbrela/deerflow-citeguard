# Systematic Literature Review: Mixture of Experts

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "mixture of experts", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on Mixture of Experts (MoE) architectures in machine learning, published between October 2024 and October 2026. The surveyed literature reveals a field in rapid evolution, with research spanning theoretical foundations, architectural innovations, and practical deployment considerations. Key developments include novel routing mechanisms that improve expert specialization, theoretical analyses of MoE robustness and generalization, and emerging work on uncertainty quantification in MoE systems. The collective findings suggest that MoE architectures offer significant advantages over dense models in terms of parameter efficiency and modular computation, though challenges remain in achieving true expert specialization and realizing theoretical efficiency gains on modern hardware.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "mixture of experts", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Routing Mechanisms and Expert Specialization

A central theme across the surveyed literature concerns the design and behavior of routing mechanisms in MoE architectures. Multiple papers investigate how experts are selected for different inputs and whether routing achieves meaningful specialization. Wang et al. (2026) challenge the prevailing assumption that MoE models achieve domain-specific specialization, revealing instead a "Standing Committee" phenomenon where a compact coalition of experts handles most computation across domains. Their COMMITTEEAUDIT framework demonstrates that specialization is far less pervasive than commonly believed, with domain-invariant experts anchoring core reasoning while peripheral experts handle domain-specific knowledge.

In contrast, Avinash (2026) provides evidence for task-conditioned routing structure, showing that prompts from the same task category induce highly similar expert activation patterns. Using routing signatures as vector representations of expert activation, this work achieved 92.5% accuracy in four-way task classification, suggesting that routing does capture meaningful task structure, at least in some contexts. The apparent tension between these findings points to a nuanced reality: while routing exhibits structure, true domain specialization may be limited by training objectives and architectural constraints.

### Theme 2: Robustness and Generalization Properties

Several papers examine MoE robustness and generalization characteristics, particularly under challenging conditions. Sun et al. (2026) demonstrate that sparse expert activation acts as a noise filter, enabling MoE models to achieve lower generalization error under feature noise compared to dense networks. Their theoretical and empirical analyses reveal that MoEs exhibit improved robustness to perturbations and faster convergence speed, providing a mechanistic explanation for MoE advantages beyond simple parameter scaling.

Rokah et al. (2026) extend this analysis to vision tasks, comparing dense, SoftMoE, and SparseMoE classifier heads on CIFAR10. Their Hessian-based sharpness metrics reveal that while SoftMoE exhibits higher curvature, all models achieve comparable generalization performance despite these differences. This suggests that MoE architectures can maintain robust performance even with different optimization landscapes, though the practical implications for model selection remain unclear.

### Theme 3: Efficiency and Deployment Considerations

A significant strand of research addresses practical deployment challenges for MoE models, particularly in resource-constrained environments. Huber et al. (2025) focus on enabling Compact Sparse MoE for on-device inference, addressing the triad of quality, memory, and latency constraints. Their work demonstrates that MoE architectures can outperform FLOP-aligned dense models at on-device scale when evaluated under fair conditions, with weight-decomposed experts providing additional performance improvements.

However, Rokah et al. (2026) caution that naive conditional routing implementations do not yield inference speedups on modern hardware at typical scales, highlighting the gap between theoretical efficiency and realized performance. This tension between theoretical advantages and practical implementation challenges represents a key area for future work, particularly as MoE models scale to larger sizes.

### Theme 4: Theoretical Foundations and Mathematical Characterizations

Recent work has advanced theoretical understanding of MoE architectures through novel mathematical frameworks. Małaśnicki et al. (2025) derive μ-Parameterization for MoE architectures, providing theoretical guarantees for feature learning across model widths and enabling efficient hyperparameter tuning across scales. This work addresses a critical gap, as existing μTransfer techniques focused primarily on dense LLMs.

Chaudhari et al. (2025) investigate the relationship between sparsity and superposition in MoE models, developing new metrics for measuring superposition across experts. Their finding that network sparsity (ratio of active to total experts) better characterizes MoE models than feature sparsity provides a refined lens for understanding MoE behavior. The observation that greater network sparsity correlates with greater monosemanticity suggests pathways toward more interpretable MoE systems.

### Theme 5: Alternative Architectural Approaches

Several papers propose novel architectural variations that depart from traditional MoE designs. Do et al. (2024) introduce Vector-Quantized MoE (VQMoE), which replaces traditional router mechanisms with discrete representations learned through vector quantization. This approach addresses routing inconsistencies and representation collapse, achieving 28% improvement in robustness compared to other SMoE routing methods.

Badjie et al. (2025) propose the DFCP-MoE framework, combining input feature extraction, feature-level clustering, and pseudo-labeling strategies. Their double-stage clustering approach reduces the impact of noise and outliers while leveraging limited labeled data, demonstrating competitive inference results across multiple benchmark datasets.

### Theme 6: Uncertainty Quantification in MoE Systems

Emerging work addresses the critical need for calibrated uncertainty estimation in MoE architectures. Dialameh et al. (2025) apply Bayesian inference post-hoc to MoE models using structured Laplace approximation, enabling calibrated uncertainty estimation without modifying training procedures. Their approach leverages the modular MoE design for tractable block-wise posterior estimation, improving both expected calibration error and negative log-likelihood on common-sense reasoning benchmarks.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that MoE architectures offer advantages over dense models, particularly in terms of parameter efficiency and modular computation. There is broad agreement that routing mechanisms exhibit structure, though the nature and extent of specialization remains debated. Several papers also converge on the importance of fair evaluation conditions when comparing MoE to dense models, emphasizing FLOP-aligned comparisons rather than parameter-count matching.

**Disagreements**: A key disagreement concerns the extent of expert specialization. Wang et al. (2026) argue that specialization is largely illusory, with domain-invariant "Standing Committees" dominating computation. In contrast, Avinash (2026) presents evidence for meaningful task-conditioned routing patterns. This tension may reflect differences in model architectures, task domains, or analytical frameworks, and warrants further investigation.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, many papers note limitations in their scope—studies are often conducted on single models or datasets, limiting generalizability. Second, the gap between theoretical efficiency and realized hardware performance remains unresolved, with Rokah et al. (2026) highlighting this challenge without offering solutions. Third, the mechanism by which training objectives like load-balancing losses may work against natural optimization paths (Wang et al., 2026) requires deeper investigation.

Notably, most papers do not state limitations explicitly in their abstracts, suggesting either space constraints or a reluctance to acknowledge limitations. This represents a potential gap in the literature's self-awareness. Future work should address cross-architecture generalizability, develop hardware-efficient routing implementations, and investigate the tension between imposed load-balancing and emergent specialization patterns.

## Per-Paper Annotations

### Avinash (2026)

**Research question**: Does MoE routing exhibit task-conditioned structure, where prompts from the same task category induce similar expert activation patterns?

**Methodology**: Introduced routing signatures as vector representations of expert activation patterns across layers, using OLMoE-1B-7B-0125-Instruct as testbed; measured within-category vs across-category routing similarity, trained logistic regression classifier on routing signatures for task classification, and introduced permutation and load-balancing baselines for statistical validation.

**Key findings**:
- Prompts from the same task category induce highly similar routing signatures (0.8435 +/- 0.0879), while different categories show substantially lower similarity (0.6225 +/- 0.1687)
- The observed separation corresponds to Cohen's d = 1.44, indicating strong effect size
- Logistic regression classifier achieves 92.5% +/- 6.1% cross-validated accuracy on four-way task classification using only routing signatures
- Task structure becomes increasingly apparent in deeper layers through layer-wise signal strength analysis

**Limitations**: Study conducted on a single model (OLMoE-1B-7B-0125-Instruct); the generalizability to other MoE architectures and task domains requires further investigation.

### Badjie et al. (2025)

**Research question**: How can Mixture of Experts models be improved to handle noise and outliers in the input space while leveraging limited labeled data?

**Methodology**: The paper introduces the DFCP-MoE framework combining input feature extraction, feature-level clustering, and a pseudo-labeling strategy, validated through conditional end-to-end joint training on three benchmark datasets for multi-class classification.

**Key findings**:
- The DFCP-MoE framework reduces the impact of noise and outliers in MoE training
- The approach leverages a small subset of labeled data to label a large portion of unlabeled inputs
- Joint training improves expert specialization by training on well-labeled, clustered inputs
- The framework effectively captures input space diversity, leading to competitive inference results

**Limitations**: Not stated in abstract.

### Chaudhari et al. (2025)

**Research question**: How do sparsity and superposition mechanisms differ between MoE models and dense networks, and what characterizes expert specialization?

**Methodology**: The study develops new metrics for measuring superposition across experts and analyzes the relationship between network sparsity and monosemanticity, proposing a new definition of expert specialization based on monosemantic feature representation.

**Key findings**:
- Neither feature sparsity nor feature importance cause discontinuous phase changes in MoE models
- Network sparsity (ratio of active to total experts) better characterizes MoE models
- Models with greater network sparsity exhibit greater monosemanticity
- Experts naturally organize around coherent feature combinations when initialized appropriately
- Network sparsity may enable more interpretable models without sacrificing performance

**Limitations**: Not stated in abstract.

### Dialameh et al. (2025)

**Research question**: Can Bayesian inference be applied post-hoc to MoE architectures for calibrated uncertainty estimation without modifying training procedures?

**Methodology**: Applied structured Laplace approximation to the second linear layer of each expert in MoE models, using Kronecker-factored low-rank approximations to model curvature and derive scalable estimates of predictive uncertainty and marginal likelihood; evaluated on common-sense reasoning benchmarks with Qwen1.5-MoE and DeepSeek-MoE.

**Key findings**:
- Bayesian-MoE enables calibrated uncertainty estimation without modifying original training procedure or introducing new parameters
- Improves both expected calibration error (ECE) and negative log-likelihood (NLL) over baselines on common-sense reasoning benchmarks
- Leverages modular MoE design for tractable block-wise posterior estimation directly on expert pathways

**Limitations**: Not stated in abstract.

### Do et al. (2024)

**Research question**: Can discrete representations learned via vector quantization replace traditional router mechanisms to overcome routing inconsistencies and representation collapse in SMoE?

**Methodology**: Proposed Vector-Quantized Mixture of Experts (VQMoE) architecture that assigns experts to input via indirection using discrete representations learned through vector quantization; provided theoretical support and conducted extensive evaluations on large language models and vision tasks for both pre-training and fine-tuning.

**Key findings**:
- VQMoE overcomes routing inconsistencies and representation collapse challenges present in traditional routers
- Achieves 28% improvement in robustness compared to other SMoE routing methods
- Maintains strong performance in fine-tuning tasks across both language and vision domains

**Limitations**: Not stated in abstract.

### Huber et al. (2025)

**Research question**: How can Compact Sparse Mixture of Experts be enabled for on-device inference by addressing quality, memory, and latency constraints?

**Methodology**: Evaluated MoE architectures against FLOP-aligned dense models at on-device scale under fair evaluation conditions, introduced weight-decomposed experts to improve performance, and optimized model offloading efficiency to reduce memory and latency.

**Key findings**:
- MoE architectures outperform FLOP-aligned dense models at on-device scale when evaluated under fair conditions
- Weight-decomposed experts further improve MoE model performance along the quality axis
- Significant improvements in model offloading efficiency reduce model inference latency

**Limitations**: Not stated in abstract.

### Małaśnicki et al. (2025)

**Research question**: Can μTransfer techniques be extended to Mixture of Experts architectures to enable efficient hyperparameter tuning across model scales?

**Methodology**: The work derives a μ-Parameterization for MoE architectures providing theoretical guarantees for feature learning across model widths, with experimental validation of learning rate transfer across model sizes.

**Key findings**:
- The paper derives a μ-Parameterization for MoE with theoretical guarantees for feature learning across model widths
- Optimal learning rates reliably transfer across model sizes in MoE architectures
- This establishes a foundation for efficient hyperparameter tuning in large-scale MoE models
- Addresses the gap in existing work that focused primarily on dense LLMs

**Limitations**: Not stated in abstract.

### Rokah et al. (2026)

**Research question**: How do Mixture-of-Experts architectures perform in image classification settings compared to dense models in terms of predictive performance, expert utilization, and generalization?

**Methodology**: Compared dense, SoftMoE, and SparseMoE classifier heads on CIFAR10 under comparable model capacity, computing Hessian-based sharpness metrics (largest eigenvalue and trace of loss Hessian) on training and test data, along with loss surface perturbation analyses and empirical inference efficiency measurements.

**Key findings**:
- Both MoE variants achieve slightly higher validation accuracy than the dense baseline while maintaining balanced expert utilization through regularization
- SoftMoE exhibits higher sharpness by Hessian-based metrics, while Dense and SparseMoE lie in a similar curvature regime
- All models achieve comparable generalization performance despite curvature differences
- Naively implemented conditional routing does not yield inference speedups on modern hardware at this scale

**Limitations**: The study is limited to CIFAR10 dataset and comparable model capacity settings; the gap between theoretical and realized efficiency in sparse MoE models is highlighted but not fully resolved.

### Sun et al. (2026)

**Research question**: Why do Mixture of Experts models outperform dense networks beyond parameter scaling, particularly under feature noise conditions?

**Methodology**: The study analyzes MoE models in an iso-parameter regime with inputs exhibiting latent modular structure corrupted by feature noise, using theoretical analysis and empirical validation on synthetic data and real-world language tasks.

**Key findings**:
- Sparse expert activation acts as a noise filter compared to dense networks
- MoEs achieve lower generalization error under feature noise
- MoEs demonstrate improved robustness to perturbations and faster convergence speed
- Empirical results show consistent robustness and efficiency gains from sparse modular computation

**Limitations**: Not stated in abstract.

### Wang et al. (2026)

**Research question**: Do Mixture of Experts models truly achieve domain specialization through sparse routing, or is there a structural bias toward centralized computation?

**Methodology**: The paper introduces COMMITTEEAUDIT, a post hoc framework analyzing routing behavior at the expert group level across three representative models and the MMLU benchmark, with qualitative analysis of routing patterns.

**Key findings**:
- A domain-invariant Standing Committee exists—a compact coalition of routed experts capturing majority routing mass across domains
- Standing Committees persist across layers and routing budgets, even in architectures with shared experts
- Standing Committees anchor reasoning structure and syntax while peripheral experts handle domain-specific knowledge
- Specialization in MoE models is far less pervasive than commonly believed
- Current training objectives like load-balancing losses may work against the model's natural optimization path

**Limitations**: Not stated in abstract.

## References

Avinash, M. S. R. (2026). Task-conditioned routing signatures in sparse mixture-of-experts transformers. arXiv. https://arxiv.org/abs/2603.11114

Badjie, B., Cecílio, J., & Casimiro, A. (2025). Double-stage feature-level clustering-based mixture of experts framework. arXiv. https://arxiv.org/abs/2503.09504

Chaudhari, M., Nuer, J., & Thorstenson, R. (2025). Sparsity and superposition in mixture of experts. arXiv. https://arxiv.org/abs/2510.23671

Dialameh, M., Rajabzadeh, H., Zhang, W., Ahmed, W., & Kwon, H. J. (2025). Bayesian mixture of experts for large language models. arXiv. https://arxiv.org/abs/2511.08968

Do, G., Pham, K., Le, H., & Tran, T. (2024). On the role of discrete representation in sparse mixture of experts. arXiv. https://arxiv.org/abs/2411.19402

Huber, P., Shrivastava, A., Chang, E., Sankar, C., Aly, A., & Sagar, A. (2025). CoSMoEs: Compact sparse mixture of experts. arXiv. https://arxiv.org/abs/2503.00245

Małaśnicki, J., Ciebiera, K., Boruń, M., Pióro, M., Ludziejewski, J., Stefaniak, M., Krutul, M., Jaszczur, S., Cygan, M., Adamczewski, K., & Krajewski, J. (2025). μ-Parametrization for mixture of experts. arXiv. https://arxiv.org/abs/2508.09752

Rokah, A., Veress, D., Caulk, C., & Sharan, S. (2026). Mixture-of-experts models in vision: Routing, optimization, and generalization. arXiv. https://arxiv.org/abs/2601.15021

Sun, D., Nittala, R., & Burkholz, R. (2026). Robustness of mixtures of experts to feature noise. arXiv. https://arxiv.org/abs/2601.14792

Wang, Y., Xu, Y., Shen, N., Su, J., Huang, J., & Zhu, Z. (2026). The illusion of specialization: Unveiling the domain-invariant "standing committee" in mixture-of-experts models. arXiv. https://arxiv.org/abs/2601.03425
