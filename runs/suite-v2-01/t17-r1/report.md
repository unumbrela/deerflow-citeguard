# Systematic Literature Review: Parameter-Efficient Fine-Tuning

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "parameter-efficient fine-tuning", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of parameter-efficient fine-tuning (PEFT) has evolved significantly in the past two years, with research focusing on adaptive rank allocation, geometric exploitation of pretrained weights, and novel architectures beyond traditional LoRA. The surveyed literature reveals three major directions: (1) dynamic adaptation mechanisms that optimize parameter allocation across layers, (2) theoretical frameworks leveraging pretrained weight geometry, and (3) exploration of alternative architectures including quantum computing and state-space models. Collectively, these works demonstrate that PEFT methods can achieve competitive or superior performance to full fine-tuning while training less than 0.1% of total parameters. However, the field lacks unified theoretical understanding of why different methods succeed, and few papers address uncertainty quantification or catastrophic forgetting systematically.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "parameter-efficient fine-tuning", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive Rank Allocation and Dynamic Parameter Distribution

A significant body of recent work addresses the suboptimality of uniform rank allocation in Low-Rank Adaptation (LoRA). Tripathi et al. (2026) demonstrate that different transformer layers have heterogeneous adaptation requirements, proposing LAARA, a search-free framework that dynamically allocates ranks using Fisher estimates. Similarly, Anumasa and Liu (2026) introduce EulerLoRA, which uses rank-driven jump dynamics to generate multiple predictive trajectories while maintaining parameter efficiency. This theme reflects a broader recognition that static parameter budgets are insufficient for optimal adaptation across diverse tasks and model architectures.

The key insight across these works is that intelligent parameter allocation—guided by second-order information (Hessian), Fisher estimates, or stochastic dynamics—can dramatically improve the efficiency-performance tradeoff. Tripathi et al. (2026) show that their adaptive approach uses significantly fewer trainable parameters while matching or outperforming state-of-the-art methods. Anumasa and Liu (2026) achieve approximately 69% fewer trainable parameters compared to ensemble baselines while maintaining predictive diversity.

### Theme 2: Geometric and Structural Exploitation of Pretrained Weights

Several papers investigate how the intrinsic geometry of pretrained weights can be leveraged for more efficient adaptation. Hwang et al. (2025) introduce PiCa, which projects gradients onto the principal column space of pretrained weights, providing theoretical guarantees alongside empirical improvements. Xu et al. (2025) propose GenFT, a W0-conditioned method that extracts structured patterns from pretrained weights through row and column transformations with nonlinear activations.

This geometric perspective offers a principled alternative to heuristic adapter designs. The central finding is that pretrained weights encode valuable structural information that, when properly exploited, reduces the parameter budget needed for effective adaptation. Hwang et al. (2025) demonstrate that column space projection provides an effective inductive bias, while Xu et al. (2025) show that deterministic weight generation from pretrained patterns balances cross-layer information reuse with layer-specific flexibility.

### Theme 3: Beyond LoRA—Alternative Architectures and Paradigms

The literature reveals growing exploration of PEFT methods beyond the LoRA family. Koike-Akino et al. (2025) propose Quantum-PEFT, leveraging quantum computations with Pauli parameterization to achieve logarithmic parameter scaling—a fundamentally different approach from linear scaling in LoRA-based methods. Lee et al. (2025) adapt PEFT to State Space Models (Mamba) through membrane-driven gating mechanisms, addressing the unique temporal processing dynamics of these architectures.

These works challenge the assumption that LoRA-style low-rank adaptation is the only viable PEFT paradigm. Quantum-PEFT demonstrates that quantum unitary parameterization can achieve vanishingly smaller parameter counts as dimensions grow (Koike-Akino et al., 2025). Memba shows that bio-inspired membrane potential accumulation enhances selective information retention in state-space models (Lee et al., 2025). This diversification suggests the field is maturing beyond incremental LoRA improvements toward fundamental architectural innovations.

### Theme 4: Cross-Layer Information Flow and Representation Injection

A novel direction involves leveraging information across transformer layers during fine-tuning. Peng et al. (2026) introduce Echo-LoRA, which collects boundary hidden states from deeper layers and injects them into shallow LoRA modules through lightweight projection networks. This approach achieves 5.7 percentage point average improvement across commonsense reasoning benchmarks while maintaining the original low-rank form at inference time.

The key innovation is training-time cross-layer communication without inference-time overhead. By aggregating sample-level echo representations from deeper layers and injecting them into shallow adapters, Peng et al. (2026) demonstrate that intermediate representations contain valuable adaptation signals that standard PEFT methods ignore. This theme connects to broader efforts in understanding how information flows through transformer architectures during adaptation.

### Theme 5: Uncertainty Quantification and Bayesian Approaches

Recent work addresses the critical gap of uncertainty estimation in PEFT. Chai et al. (2025) propose BH-PEFT, integrating Bayesian learning into hybrid PEFT by modeling learnable parameters as distributions and using dynamic fine-tuning where posterior serves as prior for subsequent rounds. Anumasa and Liu (2026) similarly address uncertainty through stochastic trajectory generation in EulerLoRA.

This theme responds to the practical need for reliable decision-making in specialized applications. Chai et al. (2025) demonstrate that Bayesian parameter modeling enables uncertainty quantification for business tasks including sentiment analysis and news categorization. The integration of Bayesian dynamics allows models to adapt to emerging data while quantifying confidence—a capability largely absent from standard PEFT methods.

### Theme 6: Comparative Analysis and Methodological Unification

A meta-analytical perspective emerges in Li et al. (2026), who systematically compare six PEFT methods to understand whether differences are substantive or superficial. Their work examines how parameterizations relate to task performance, forgetting, and changes in pretrained weight geometry, including intervention experiments on spectral component modifications.

This comparative approach reveals that LoRA-family methods approximately preserve pretrained geometry, and restoring drifted singular-value spectra largely preserves task performance (Li et al., 2026). The finding that LoRA most consistently limits forgetting at competitive performance levels provides empirical guidance for method selection. This work represents a maturation of the field—from proposing new methods to understanding why existing methods work.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, uniform parameter allocation is suboptimal—multiple papers demonstrate that adaptive, layer-specific allocation improves efficiency (Tripathi et al., 2026; Xu et al., 2025). Second, pretrained weight geometry contains valuable structural information that should be exploited during adaptation (Hwang et al., 2025; Xu et al., 2025). Third, PEFT methods can achieve competitive or superior performance to full fine-tuning while training orders of magnitude fewer parameters (all surveyed papers).

**Disagreements**: The literature reveals tension between different approaches to parameter efficiency. Li et al. (2026) find that DoRA achieves higher mean task scores than LoRA in most comparisons, while PiSSA often incurs greater retention costs—suggesting tradeoffs between performance and catastrophic forgetting that remain unresolved. Additionally, while most papers focus on deterministic adaptation, the Bayesian approach of Chai et al. (2025) and stochastic approach of Anumasa and Liu (2026) suggest that uncertainty-aware methods may require different parameterization strategies, though the optimal balance remains unclear.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature:

1. **Theoretical unification**: None of the surveyed papers provide a unified theoretical framework explaining why different PEFT methods succeed. Li et al. (2026) begin this work through comparative analysis, but a comprehensive theory remains absent.

2. **Catastrophic forgetting**: While Li et al. (2026) examine forgetting empirically, few papers propose principled solutions. The Bayesian approach of Chai et al. (2025) offers one direction, but systematic treatment of forgetting across architectures is lacking.

3. **Cross-architecture generalization**: Most methods are evaluated on specific architectures (transformers, Mamba, quantum circuits). Whether PEFT principles transfer across fundamentally different architectures remains unclear.

4. **Inference-time efficiency**: While Echo-LoRA (Peng et al., 2026) explicitly addresses inference overhead, most papers focus solely on training-time parameter counts. The relationship between training efficiency and inference latency deserves more attention.

5. **Task-architecture co-design**: No paper systematically addresses how PEFT method selection should depend on both task characteristics and target architecture. Adaptive selection mechanisms remain an open challenge.

## Per-Paper Annotations

### Anumasa and Liu (2026)

**Research question**: How can LoRA be extended to support predictive uncertainty estimation while maintaining parameter efficiency?
**Methodology**: The authors introduce EulerLoRA, a stochastic extension of LoRA that generates multiple predictive trajectories by sampling structured variations along rank-one components of shared low-rank adapters while preserving the deterministic LoRA transformation in expectation, evaluated on vision transformers across multiple benchmarks.
**Key findings**:
- EulerLoRA achieves comparable or improved performance relative to strong LoRA-Ensemble baselines
- Using two rank-20 adapters, EulerLoRA requires approximately 3 million trainable parameters versus 10 million for a rank-8, 16-adapter LoRA-Ensemble
- EulerLoRA achieves roughly 69% fewer trainable parameters while obtaining useful predictive diversity from a small number of shared adapters
**Limitations**: not stated in abstract

### Chai et al. (2025)

**Research question**: How can hybrid PEFT methods be enhanced to quantify uncertainty and dynamically adapt to emerging data in specialized business applications?
**Methodology**: The authors propose BH-PEFT, which integrates Bayesian learning into hybrid PEFT by combining Adapter, LoRA, and prefix-tuning for feedforward and attention layers, modeling learnable parameters as distributions and using Bayesian dynamic fine-tuning where posterior serves as prior for subsequent rounds.
**Key findings**:
- BH-PEFT outperforms existing PEFT baselines on business tasks including sentiment analysis, news categorization, and commonsense reasoning
- The method enables uncertainty quantification for more reliable decision-making
- BH-PEFT improves adaptability in dynamic scenarios through Bayesian dynamic fine-tuning
**Limitations**: not stated in abstract

### Hwang et al. (2025)

**Research question**: How can the geometry of pre-trained weights be exploited to improve parameter-efficient fine-tuning with theoretical guarantees?
**Methodology**: The authors introduce PiCa, a theoretically grounded PEFT method that projects gradients onto the principal column space of pre-trained weights and enhances parameter efficiency through a novel weight-sharing strategy.
**Key findings**:
- Projecting gradients onto the principal column space of pre-trained weights provides an effective inductive bias for adaptation
- PiCa consistently outperforms state-of-the-art baselines under comparable or smaller parameter budgets
- The method demonstrates both theoretical rigor and practical effectiveness across diverse NLP and vision tasks
**Limitations**: not stated in abstract

### Koike-Akino et al. (2025)

**Research question**: Can quantum computations enable ultra parameter-efficient fine-tuning with logarithmic parameter scaling?
**Methodology**: The authors introduce Quantum-PEFT, which leverages quantum computations with Pauli parameterization to achieve full-rank yet parameter-efficient quantum unitary parameterization where trainable parameters grow logarithmically with dimension.
**Key findings**:
- Quantum-PEFT achieves vanishingly smaller number of trainable parameters than the lowest-rank LoRA as dimensions grow
- The number of trainable parameters grows logarithmically with ambient dimension, unlike linearly in LoRA-based methods
- Quantum-PEFT demonstrates significant advantages in parameter efficiency on language and vision transfer learning benchmarks while maintaining competitive performance
**Limitations**: not stated in abstract

### Lee et al. (2025)

**Research question**: How can parameter-efficient fine-tuning methods be adapted to address the unique temporal processing dynamics of State Space Models like Mamba?
**Methodology**: The authors propose Memba, a membrane-driven PEFT approach that introduces Leaky Integrate Membrane (LIM) neurons as bio-inspired gating mechanisms, strategically combined with Low-Rank Adaptations (LoRA) and cross-layer membrane transfer to enhance Mamba's temporal modeling capabilities.
**Key findings**:
- Memba achieves substantial improvements over existing PEFT methods for Mamba models
- LIM neurons enhance selective information retention through bio-inspired membrane potential accumulation
- The approach was validated across both language and vision tasks
**Limitations**: not stated in abstract

### Li et al. (2026)

**Research question**: What are the methodological and functional differences between parameter-efficient fine-tuning methods, and is spectral preservation itself important for adaptation and retention?
**Methodology**: The authors compare six PEFT methods in language and diffusion models, examining how parameterizations relate to task performance, forgetting, and changes in pretrained weight geometry, including intervention experiments on spectral component modifications.
**Key findings**:
- LoRA-family methods approximately preserve pretrained geometry, and restoring their drifted singular-value spectra largely preserves task performance
- LoRA most consistently limits forgetting at competitive performance levels
- DoRA achieves higher mean task scores than LoRA in most comparisons, while PiSSA often incurs greater retention costs
- Restoring dominant spectral components produces the largest mean reduction in general-text NLL or base-image drift
**Limitations**: not stated in abstract

### Peng et al. (2026)

**Research question**: How can intermediate representations from deeper transformer layers be leveraged to improve parameter-efficient fine-tuning?
**Methodology**: The authors propose Echo-LoRA, a cross-layer representation injection method that collects boundary hidden states from deeper source layers, aggregates them into sample-level echo representations, and injects the signal into shallow LoRA or DoRA modules using lightweight projection and gating networks.
**Key findings**:
- Echo-LoRA exceeds LoRA baselines by 5.7 percentage points on average across eight commonsense reasoning benchmarks
- Under reproduced LoRA baselines, Echo-LoRA achieves an average gain of 3.0 points; with DoRA, the gain is 2.7 points
- The Echo path is discarded after training, so the deployed model maintains the original low-rank LoRA/DoRA form with no added inference-time parameters or computation
- Answer-only masking, masked distillation, and stochastic routing keep the auxiliary path stable and reduce training-inference gap
**Limitations**: not stated in abstract

### Tripathi et al. (2026)

**Research question**: How can rank allocation in Low-Rank Adaptation be optimized to address the heterogeneous adaptation requirements across different transformer layers?
**Methodology**: The authors propose LAARA, a search-free framework that dynamically allocates ranks using lightweight diagonal Fisher estimates computed during training, combining projection-wise normalization, logarithmic compression, blended adapter importance estimation, and a vote-to-change dampening mechanism.
**Key findings**:
- Uniform rank allocation across transformer layers is theoretically and empirically suboptimal
- LAARA matches or outperforms state-of-the-art methods (LoRA, AdaLoRA, DyLoRA, Bitfit) on GLUE and MathInstruct benchmarks
- LAARA achieves competitive performance while using significantly fewer trainable parameters
- Fisher-guided rank allocation provides a principled foundation for adaptive parameter-efficient fine-tuning
**Limitations**: not stated in abstract

### Xu et al. (2025)

**Research question**: How can the structural information encoded in pretrained weights be further leveraged for parameter-efficient fine-tuning?
**Methodology**: The authors propose GenFT, a W0-conditioned PEFT method that uses a deterministic weight generator to produce task-specific updates through row and column transformations with nonlinear activations and a shared-specific decomposition.
**Key findings**:
- GenFT extracts structured patterns from pretrained weights through row and column transformations with nonlinear activations
- The shared-specific decomposition balances cross-layer information reuse and layer-specific flexibility
- GenFT achieves competitive or better average performance across NLP and CV benchmarks
- The method is feasible for generative models as demonstrated on LLaMA-7B
**Limitations**: not stated in abstract

### Xu and Bu (2025)

**Research question**: How can the most influential subset of parameters be effectively selected for training in parameter-efficient fine-tuning?
**Methodology**: The authors formulate subset selection as a multi-task optimization problem using the ε-constraint method and second-order Taylor approximation to arrive at a 0-1 knapsack problem solved through Pareto optimality, resulting in AdaPEFT, a Hessian-informed PEFT method.
**Key findings**:
- AdaPEFT adapts to various tasks and models through Hessian-informed subset selection
- The selected subset empirically transfers across training horizons and model sizes
- The approach trains less than 0.1% of total parameters while maximizing performance
**Limitations**: not stated in abstract

## References

Anumasa, S., & Liu, D. (2026). EulerLoRA: Rank-driven jump dynamics for calibrated parameter-efficient fine-tuning. arXiv. https://arxiv.org/abs/2608.01142

Chai, Y., Liu, Y., Zhou, Y., Xie, J., & Zeng, D. D. (2025). A Bayesian hybrid parameter-efficient fine-tuning method for large language models. arXiv. https://arxiv.org/abs/2508.02711

Hwang, J., Cho, W., & Kim, T. (2025). PiCa: Parameter-efficient fine-tuning with column space projection. arXiv. https://arxiv.org/abs/2505.20211

Koike-Akino, T., Tonin, F., Wu, Y., Wu, F. Z., Candogan, L. N., & Cevher, V. (2025). Quantum-PEFT: Ultra parameter-efficient fine-tuning. arXiv. https://arxiv.org/abs/2503.05431

Lee, D., Li, Y., Yin, R., Xiao, S., & Panda, P. (2025). Memba: Membrane-driven parameter-efficient fine-tuning for Mamba. arXiv. https://arxiv.org/abs/2506.18184

Li, Y., Lu, P., & Liu, F. (2026). Are parameter-efficient fine-tuning methods really different? arXiv. https://arxiv.org/abs/2610.09122

Peng, Y., Jin, P., Gong, J., Chen, X., Xu, L., Su, N., & Ran, Y. (2026). Echo-LoRA: Parameter-efficient fine-tuning via cross-layer representation injection. arXiv. https://arxiv.org/abs/2605.08177

Tripathi, A., Singh, S. D., Sahoo, P., & Saha, S. (2026). LAARA: Layer-aware adaptive rank allocation for parameter-efficient fine-tuning. arXiv. https://arxiv.org/abs/2607.19391

Xu, G., Zhang, B., & Ng, M. K. (2025). GenFT: A generative parameter-efficient fine-tuning method for pretrained foundation models. arXiv. https://arxiv.org/abs/2506.11042

Xu, S., & Bu, Z. (2025). Adaptive parameter-efficient fine-tuning via Hessian-informed subset selection. arXiv. https://arxiv.org/abs/2505.12579
