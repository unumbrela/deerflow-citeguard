# Systematic Literature Review: Mixture of Experts

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "mixture of experts", category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on Mixture of Experts (MoE) reveals a rapidly evolving field focused on improving efficiency, robustness, and interpretability of sparse expert architectures. Recent work demonstrates that MoE models offer significant advantages over dense networks in terms of parameter efficiency, noise robustness, and task-specific routing capabilities. Key advances include novel routing mechanisms that enable better expert specialization, theoretical frameworks for hyperparameter transfer across scales, and applications to vision and multimodal learning. The collective evidence suggests that sparse MoE architectures are maturing beyond mere parameter scaling to address fundamental questions about representation learning, generalization, and deployment efficiency.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "mixture of experts", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Routing Mechanisms and Expert Specialization

A central challenge in MoE architectures is designing routing mechanisms that effectively assign inputs to appropriate experts while maintaining balanced utilization. Recent work has made significant progress in understanding and improving routing behavior. Avinash (2026) introduced routing signatures as vector representations that capture expert activation patterns, demonstrating that prompts from the same task category induce highly similar routing signatures with 92.5% classification accuracy. This finding reveals that MoE routing exhibits meaningful task-conditioned structure rather than random assignment.

Badjie et al. (2025) proposed the DFCP-MoE framework, which combines feature-level clustering with pseudo-labeling to improve expert specialization on well-labeled, clustered inputs. Their conditional end-to-end joint training method reduces the impact of noise and outliers during training. Similarly, Kowsher et al. (2026) introduced LiME, which achieves expert specialization through lightweight modulation using a single shared PEFT module with expert vectors, eliminating the need for separate adapters per expert and reducing trainable parameters by up to 4x.

### Theme 2: Robustness and Generalization

Multiple papers investigate why MoE models outperform dense networks, particularly under challenging conditions. Sun et al. (2026) provided theoretical and empirical evidence that sparse expert activation acts as a noise filter, achieving lower generalization error under feature noise compared to dense estimators. Their analysis reveals that MoEs demonstrate improved robustness to perturbations and faster convergence speed, explaining benefits beyond mere parameter scaling.

Rokah et al. (2026) compared dense, SoftMoE, and SparseMoE classifier heads on CIFAR10, finding that both MoE variants achieve slightly higher validation accuracy than dense baselines while maintaining balanced expert utilization through regularization. However, they noted that SoftMoE exhibits higher sharpness by Hessian-based metrics, and naively implemented conditional routing does not yield inference speedups on modern hardware at this scale.

### Theme 3: Efficiency and Scalability

Practical deployment of MoE models requires addressing efficiency challenges across quality, memory, and latency dimensions. Huber et al. (2025) evaluated MoE architectures at on-device scale, demonstrating that MoE models outperform FLOP-aligned dense models in fair evaluation. Their introduction of weight-decomposed experts further improves performance while significantly enhancing model offloading efficiency and reducing inference latency.

Małaśnicki et al. (2025) addressed hyperparameter tuning costs by deriving a μ-Parameterization for MoE architectures with theoretical guarantees for feature learning across model widths. Their approach enables optimal learning rates to transfer reliably across model sizes, establishing a foundation for efficient hyperparameter tuning in large-scale MoE models. This work fills a critical gap, as existing μTransfer research had primarily focused on dense LLMs.

### Theme 4: Theoretical Foundations and Representation Learning

Recent work has deepened theoretical understanding of MoE behavior and representation properties. Chaudhari et al. (2025) investigated mechanistic properties like sparsity and superposition, finding that network sparsity (ratio of active to total experts) better characterizes MoE behavior than feature-level metrics. Their results show that models with greater network sparsity exhibit greater monosemanticity, suggesting that MoEs may enable more interpretable models without sacrificing performance.

Do et al. (2024) proposed Vector-Quantized Mixture of Experts (VQMoE), which uses discrete representations learned through vector quantization to address routing inconsistencies and representation collapse. Their approach achieves 28% improvement in robustness compared to other SMoE routing methods, providing theoretical support for using indirection in expert assignment rather than fixing the router directly.

### Theme 5: Uncertainty Estimation and Calibration

As MoE models are deployed in critical applications, calibrated uncertainty estimation becomes essential. Dialameh et al. (2025) applied structured Laplace approximation to the second linear layer of each expert using Kronecker-factored low-rank approximations to model curvature. Their approach improves expected calibration error and negative log-likelihood over baselines without modifying the original training procedure or introducing new parameters, leveraging the modular MoE design for tractable block-wise posterior estimation.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively demonstrate that sparse MoE architectures offer advantages beyond parameter scaling, including improved robustness to noise (Sun et al., 2026; Do et al., 2024), better task-specific routing (Avinash, 2026), and enhanced efficiency at deployment scale (Huber et al., 2025; Kowsher et al., 2026). Multiple papers agree that balanced expert utilization requires careful regularization or architectural design to avoid expert collapse (Rokah et al., 2026; Badjie et al., 2025).

**Disagreements**: While Rokah et al. (2026) found that naively implemented conditional routing does not yield inference speedups at their scale, Kowsher et al. (2026) demonstrated up to 29% faster training with their optimized routing approach, suggesting that implementation details and architectural choices significantly impact practical efficiency. Additionally, the question of whether feature sparsity or network sparsity better characterizes MoE behavior remains open, with Chaudhari et al. (2025) arguing for network-level metrics while others focus on feature-level analyses.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the surveyed papers explicitly discuss limitations in their abstracts, suggesting a need for more critical self-evaluation of MoE approaches. Second, while several papers address efficiency at different scales (on-device, large-scale training), there is limited work on systematic comparisons across the full spectrum of model sizes. Third, the theoretical understanding of why certain routing mechanisms work better than others remains incomplete, with most papers proposing new methods without fully explaining the underlying principles. Finally, the relationship between MoE architectures and interpretability, while hinted at by Chaudhari et al. (2025), requires more systematic investigation.

## Per-Paper Annotations

### Avinash (2026)

**Research question**: Does MoE routing exhibit task-conditioned structure, and can routing signatures capture whether expert activation patterns vary systematically by task category?
**Methodology**: Introduced routing signatures as vector representations summarizing expert activation patterns across layers. Used OLMoE-1B-7B-0125-Instruct to measure within-category vs across-category similarity, trained logistic regression on routing signatures for task classification, and introduced permutation and load-balancing baselines.
**Key findings**:
- Prompts from the same task category induce highly similar routing signatures
- Within-category routing similarity (0.8435 ± 0.0879) significantly exceeds across-category similarity (0.6225 ± 0.1687), with Cohen's d = 1.44
- Logistic regression classifier trained on routing signatures achieves 92.5% ± 6.1% cross-validated accuracy on four-way task classification
- Task structure becomes increasingly apparent in deeper layers
- Observed separation is not explained by sparsity or balancing constraints alone
**Limitations**: not stated in abstract

### Badjie et al. (2025)

**Research question**: How can the Mixture of Experts model's performance in image classification be improved by reducing the impact of noise and outliers in the input space?
**Methodology**: The paper introduces the DFCP-MoE framework, which combines input feature extraction, feature-level clustering, and a pseudo-labeling strategy that leverages a small subset of labeled data. A conditional end-to-end joint training method is proposed to improve expert specialization on well-labeled, clustered inputs.
**Key findings**:
- The DFCP-MoE framework reduces the impact of noise and outliers in MoE training
- The approach leverages a small subset of labeled data to label a large portion of unlabeled inputs
- The proposed joint training method improves expert specialization
- The framework effectively captures input space diversity, leading to competitive inference results
- The approach was validated on three benchmark datasets for multi-class classification tasks
**Limitations**: not stated in abstract

### Chaudhari et al. (2025)

**Research question**: How do mechanistic properties like sparsity and superposition differ between MoE models and dense networks, and what characterizes MoE behavior?
**Methodology**: The study develops new metrics for measuring superposition across experts and analyzes the relationship between network sparsity and monosemanticity, proposing a new definition of expert specialization based on monosemantic feature representation.
**Key findings**:
- Neither feature sparsity nor feature importance cause discontinuous phase changes in MoE models
- Network sparsity (ratio of active to total experts) better characterizes MoE behavior than feature-level metrics
- Models with greater network sparsity exhibit greater monosemanticity
- Experts naturally organize around coherent feature combinations when initialized appropriately
- Network sparsity in MoEs may enable more interpretable models without sacrificing performance
**Limitations**: not stated in abstract

### Dialameh et al. (2025)

**Research question**: How can calibrated uncertainty estimation be applied to fine-tuned MoE large language models without modifying the original training procedure or introducing new parameters?
**Methodology**: Applied structured Laplace approximation to the second linear layer of each expert using Kronecker-factored low-rank approximations to model curvature. Evaluated on common-sense reasoning benchmarks with Qwen1.5-MoE and DeepSeek-MoE.
**Key findings**:
- Improves expected calibration error (ECE) over baselines
- Improves negative log-likelihood (NLL) over baselines
- Enables calibrated uncertainty estimation without modifying original training procedure or introducing new parameters
- Leverages modular MoE design for tractable block-wise posterior estimation
- Directly targets expert pathways already present in MoE models rather than added adapter modules
**Limitations**: not stated in abstract

### Do et al. (2024)

**Research question**: Can discrete representation via vector quantization address routing inconsistencies and representation collapse issues in sparse mixture of experts?
**Methodology**: Proposed Vector-Quantized Mixture of Experts (VQMoE) that assigns experts to input via indirection using discrete representations learned through vector quantization. Provided theoretical support and evaluated on large language models and vision tasks for pre-training and fine-tuning.
**Key findings**:
- VQMoE achieves 28% improvement in robustness compared to other SMoE routing methods
- Maintains strong performance in fine-tuning tasks
- Overcomes routing inconsistencies and representation collapse challenges present in traditional routers
- Discrete representations via vector quantization provide an alternative to fixing the router directly
**Limitations**: not stated in abstract

### Huber et al. (2025)

**Research question**: How can Compact Sparse Mixture of Experts be enabled for on-device inference across quality, memory, and latency dimensions?
**Methodology**: Evaluated MoE architectures against FLOP-aligned dense models at on-device scale under fair evaluation conditions. Introduced weight-decomposed experts and improved model offloading efficiency.
**Key findings**:
- MoE architectures outperform FLOP-aligned dense models at on-device scale in fair evaluation
- Weight-decomposed experts further improve MoE model performance
- Significantly improved model offloading efficiency
- Reduced model inference latency
**Limitations**: not stated in abstract

### Kowsher et al. (2026)

**Research question**: How can MoE-PEFT methods achieve expert specialization without requiring separate adapters per expert, which causes trainable parameters to scale linearly with expert count?
**Methodology**: The paper proposes LiME, which uses a single shared PEFT module with lightweight expert vectors for output modulation instead of separate adapters, introduces zero-parameter routing, and incorporates n-gram windowed routing and adaptive expert selection.
**Key findings**:
- LiME achieves expert specialization through lightweight modulation rather than adapter replication
- The approach reduces expert parameters while generalizing to any PEFT method
- LiME introduces zero-parameter routing by leveraging existing frozen and adapted representations
- Theoretical proofs show that more experts preserve more task-relevant information and modulation approximates full expert-specific PEFT with bounded error
- On the MMT-47 benchmark, LiME achieves competitive or superior performance with up to 4x fewer trainable parameters and up to 29% faster training compared to MoE-PEFT baselines
**Limitations**: not stated in abstract

### Małaśnicki et al. (2025)

**Research question**: How can optimal hyperparameters be transferred across model scales for Mixture of Experts architectures to reduce tuning costs?
**Methodology**: The work derives a μ-Parameterization for MoE architectures, providing theoretical guarantees for feature learning across model widths, and validates through experiments demonstrating reliable learning rate transfer across model sizes.
**Key findings**:
- A μ-Parameterization for MoE architectures is derived with theoretical guarantees for feature learning across model widths
- The optimal learning rate reliably transfers across model sizes
- The approach establishes a foundation for efficient hyperparameter tuning in large-scale MoE models
- The work addresses the gap in existing μTransfer research which has primarily focused on dense LLMs
**Limitations**: not stated in abstract

### Rokah et al. (2026)

**Research question**: How do Mixture-of-Experts architectures behave in image classification settings regarding predictive performance, expert utilization, and generalization?
**Methodology**: Compared dense, SoftMoE, and SparseMoE classifier heads on CIFAR10 under comparable model capacity. Computed Hessian-based sharpness metrics including largest eigenvalue and trace of the loss Hessian on training and test data, plus loss surface perturbation analyses.
**Key findings**:
- Both MoE variants achieve slightly higher validation accuracy than the dense baseline
- Balanced expert utilization is maintained through regularization, avoiding expert collapse
- SoftMoE exhibits higher sharpness by Hessian-based metrics compared to Dense and SparseMoE
- Dense and SparseMoE lie in a similar curvature regime despite comparable generalization performance
- Naively implemented conditional routing does not yield inference speedups on modern hardware at this scale
**Limitations**: not stated in abstract

### Sun et al. (2026)

**Research question**: Why do Mixture of Experts models outperform dense networks beyond parameter scaling, particularly under feature noise conditions?
**Methodology**: The study analyzes an iso-parameter regime where inputs exhibit latent modular structure corrupted by feature noise, using theoretical analysis and empirical validation on synthetic data and real-world language tasks.
**Key findings**:
- Sparse expert activation acts as a noise filter compared to dense estimators
- MoEs achieve lower generalization error under feature noise
- MoEs demonstrate improved robustness to perturbations
- MoEs show faster convergence speed
- Empirical results on synthetic and real-world language tasks corroborate the theoretical insights
**Limitations**: not stated in abstract

## References

Avinash, M. S. R. (2026). Task-conditioned routing signatures in sparse mixture-of-experts transformers. arXiv. https://arxiv.org/abs/2603.11114

Badjie, B., Cecílio, J., & Casimiro, A. (2025). Double-stage feature-level clustering-based mixture of experts framework. arXiv. https://arxiv.org/abs/2503.09504

Chaudhari, M., Nuer, J., & Thorstenson, R. (2025). Sparsity and superposition in mixture of experts. arXiv. https://arxiv.org/abs/2510.23671

Dialameh, M., Rajabzadeh, H., Zhang, W., Ahmed, W., & Kwon, H. J. (2025). Bayesian mixture of experts for large language models. arXiv. https://arxiv.org/abs/2511.08968

Do, G., Pham, K., Le, H., & Tran, T. (2024). On the role of discrete representation in sparse mixture of experts. arXiv. https://arxiv.org/abs/2411.19402

Huber, P., Shrivastava, A., Chang, E., Sankar, C., Aly, A., & Sagar, A. (2025). CoSMoEs: Compact sparse mixture of experts. arXiv. https://arxiv.org/abs/2503.00245

Kowsher, M., Mansoor, H., Prottasha, N. J., Garibay, O., Zhu, V., Ji, Z., & Chen, C. (2026). LiME: Lightweight mixture of experts for efficient multimodal multi-task learning. arXiv. https://arxiv.org/abs/2604.02338

Małaśnicki, J., Ciebiera, K., Boruń, M., Pióro, M., Ludziejewski, J., Stefaniak, M., Krutul, M., Jaszczur, S., Cygan, M., Adamczewski, K., & Krajewski, J. (2025). μ-Parametrization for mixture of experts. arXiv. https://arxiv.org/abs/2508.09752

Rokah, A., Veress, D., Caulk, C., & Sharan, S. (2026). Mixture-of-experts models in vision: Routing, optimization, and generalization. arXiv. https://arxiv.org/abs/2601.15021

Sun, D., Nittala, R., & Burkholz, R. (2026). Robustness of mixtures of experts to feature noise. arXiv. https://arxiv.org/abs/2601.14792
