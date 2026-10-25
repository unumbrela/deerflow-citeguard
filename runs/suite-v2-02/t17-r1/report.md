# Systematic Literature Review: Parameter-Efficient Fine-Tuning

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "parameter-efficient fine-tuning", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of parameter-efficient fine-tuning (PEFT) has evolved significantly over the past two years, with research focusing on three primary directions: adaptive rank allocation and dynamic parameter selection, novel architectural mechanisms leveraging pretrained weight structures, and uncertainty quantification through stochastic and Bayesian approaches. The surveyed literature demonstrates a clear trend toward methods that intelligently allocate limited trainable parameters based on layer-specific importance, pretrained geometry, or task-specific requirements. LoRA-based methods remain dominant, but innovations increasingly address their limitations through cross-layer representation injection, quantum-inspired parameterization, and bio-inspired gating mechanisms. Collective findings indicate that parameter efficiency can be dramatically improved—some methods achieving logarithmic rather than linear parameter growth—while maintaining or exceeding the performance of uniform rank allocation approaches.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "parameter-efficient fine-tuning", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive Rank Allocation and Dynamic Parameter Selection

A dominant research direction involves moving beyond uniform rank allocation in Low-Rank Adaptation (LoRA) toward methods that dynamically allocate parameters based on layer-specific importance or task requirements. Tripathi et al. (2026) introduced LAARA, which uses Fisher information estimates to guide rank allocation across transformer layers without requiring expensive search procedures. Similarly, Xu and Bu (2025) proposed AdaPEFT, which frames subset selection as a multi-task optimization problem solved through Hessian-informed parameter selection using Pareto optimality. These approaches share the insight that different layers have heterogeneous adaptation requirements, and uniform parameter allocation is theoretically and empirically suboptimal. The convergence toward second-order information (Fisher matrices, Hessian approximations) as a guide for parameter allocation represents a significant methodological advance, enabling search-free adaptive allocation that matches or outperforms exhaustive search methods while using fewer trainable parameters.

### Theme 2: Exploiting Pretrained Weight Geometry

Another prominent theme involves leveraging the geometric structure of pretrained weights to guide fine-tuning. Hwang et al. (2025) introduced PiCa, which projects gradients onto the principal column space of pretrained weights, providing theoretical grounding for the inductive bias this projection creates. Xu et al. (2025) proposed GenFT, which uses pretrained weights as conditions for a deterministic weight generator that produces task-specific updates through structured transformations. Li et al. (2026) conducted a comparative analysis revealing that LoRA-family methods approximately preserve pretrained geometry, and that restoring drifted singular-value spectra largely preserves task performance. This geometric perspective suggests that successful PEFT methods should respect rather than disrupt the pretrained weight structure, with spectral preservation emerging as an important factor for both adaptation and retention of pretrained knowledge.

### Theme 3: Cross-Layer Representation Injection and Architectural Innovation

Recent work has begun exploring mechanisms beyond weight-space modifications, instead injecting representations across layers or introducing novel architectural components. Peng et al. (2026) proposed Echo-LoRA, which collects boundary hidden states from deeper layers and injects aggregated "echo representations" into shallow LoRA modules via lightweight projection and gating networks. Lee et al. (2025) introduced Memba for State Space Models, incorporating bio-inspired Leaky Integrate Membrane neurons as gating mechanisms that naturally accumulate membrane potentials over time. These approaches recognize that intermediate representations—typically unused in existing LoRA variants—contain valuable information for adaptation. The key innovation is that these architectural additions are discarded after training, preserving the original low-rank form for deployment with no inference-time overhead.

### Theme 4: Uncertainty Quantification and Stochastic Extensions

A emerging direction addresses the limitation that standard PEFT methods provide point estimates without uncertainty quantification. Anumasa and Liu (2026) introduced EulerLoRA, a stochastic extension of LoRA that generates multiple predictive trajectories by sampling structured variations along rank-one components while preserving the deterministic LoRA transformation in expectation. Chai et al. (2025) proposed BH-PEFT, which integrates Bayesian learning into hybrid PEFT by modeling learnable parameters as distributions and using Bayesian dynamic fine-tuning where posterior serves as prior for subsequent rounds. These methods achieve useful predictive diversity from a small number of shared adapters—EulerLoRA using two rank-20 adapters requires approximately 69% fewer trainable parameters than comparable ensemble approaches—demonstrating that uncertainty quantification need not sacrifice parameter efficiency.

### Theme 5: Ultra-Efficient Parameterization Through Novel Computation Paradms

The most radical approach to parameter efficiency involves fundamentally rethinking the parameterization itself. Koike-Akino et al. (2025) introduced Quantum-PEFT, which leverages quantum computations with Pauli parameterization to achieve full-rank quantum unitary parameterization where trainable parameters grow logarithmically with ambient dimension, contrasting sharply with the linear growth in LoRA-based methods. This approach demonstrates that as dimensions grow, Quantum-PEFT achieves a vanishingly smaller number of trainable parameters than even the lowest-rank LoRA while maintaining competitive performance on language and vision transfer learning benchmarks. While requiring quantum computational resources, this work establishes a theoretical upper bound on what parameter efficiency might be achievable through alternative computation paradigms.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that uniform rank allocation in LoRA is suboptimal, with multiple studies providing both theoretical analysis and empirical evidence for this claim (Tripathi et al., 2026; Li et al., 2026). There is also strong convergence around the finding that pretrained weight geometry should be preserved during adaptation, with spectral preservation emerging as important for both task performance and retention of pretrained knowledge (Li et al., 2026; Hwang et al., 2025). Additionally, multiple papers demonstrate that their proposed methods achieve comparable or better performance than standard LoRA while using significantly fewer trainable parameters, suggesting that parameter efficiency and performance are not necessarily trade-offs.

**Disagreements**: While most methods build upon LoRA, there is disagreement about the best direction for innovation. Some approaches focus on adaptive rank allocation within the LoRA framework (Tripathi et al., 2026; Xu & Bu, 2025), while others argue for fundamentally different parameterizations such as quantum unitary transformations (Koike-Akino et al., 2025) or representation injection mechanisms (Peng et al., 2026). Li et al. (2026) found that DoRA achieves higher mean task scores than LoRA in most comparisons, while PiSSA often incurs greater retention costs, suggesting that different LoRA variants have distinct trade-offs that are not yet fully understood. The comparative analysis by Li et al. (2026) also reveals that while LoRA most consistently limits forgetting at competitive performance, the relative performance of different methods varies across tasks and settings, indicating that no single approach dominates universally.

## Gaps and Open Questions

Several important gaps emerge from the collective literature. First, none of the surveyed papers explicitly address the computational overhead of their adaptive methods during training—while methods like LAARA claim to be "search-free," the cost of computing Fisher information estimates or Hessian approximations is not thoroughly analyzed. Second, while several methods demonstrate performance on standard benchmarks (GLUE, MathInstruct, commonsense reasoning), there is limited evaluation on specialized domains such as medical, legal, or scientific text, where PEFT methods are increasingly deployed. Third, the intersection of PEFT with catastrophic forgetting remains underexplored—while Li et al. (2026) examine forgetting across methods, systematic approaches to balancing adaptation with retention are not well-developed. Fourth, most methods are evaluated on language or vision tasks separately, with limited cross-modal evaluation that would reveal whether PEFT innovations transfer across modalities. Finally, while Quantum-PEFT demonstrates theoretical advantages, the practical requirements for quantum computational resources and the feasibility of deployment in classical settings remain open questions.

## Per-Paper Annotations

### Anumasa and Liu (2026)

**Research question**: Can Low-Rank Adaptation be extended to support predictive uncertainty estimation while maintaining parameter efficiency?
**Methodology**: The authors introduce EulerLoRA, a stochastic extension of LoRA that generates multiple predictive trajectories by sampling structured variations along rank-one components of shared low-rank adapters while preserving the deterministic LoRA transformation in expectation, evaluated on vision transformers across multiple benchmarks.
**Key findings**:
- EulerLoRA achieves comparable or improved performance relative to strong LoRA-Ensemble baselines
- Using two rank-20 adapters, EulerLoRA requires approximately 3 million trainable parameters versus 10 million for a rank-8, 16-adapter LoRA-Ensemble
- EulerLoRA achieves roughly 69% fewer trainable parameters than comparable ensemble approaches
- Useful predictive diversity can be obtained from a small number of shared adapters
**Limitations**: Not stated in abstract

### Chai et al. (2025)

**Research question**: How can hybrid PEFT methods be improved to quantify uncertainty and dynamically adapt to emerging data for specialized business applications?
**Methodology**: The authors propose BH-PEFT, which integrates Bayesian learning into hybrid PEFT by combining Adapter, LoRA, and prefix-tuning to fine-tune feedforward and attention layers, modeling learnable parameters as distributions and using Bayesian dynamic fine-tuning where posterior serves as prior for subsequent rounds.
**Key findings**:
- BH-PEFT enables uncertainty quantification by modeling learnable parameters as distributions
- The Bayesian dynamic fine-tuning approach enables effective adaptation to new data
- BH-PEFT outperforms existing PEFT baselines on business tasks including sentiment analysis, news categorization, and commonsense reasoning
- The method supports uncertainty-aware and adaptive decision-making in real-world situations
**Limitations**: Not stated in abstract

### Hwang et al. (2025)

**Research question**: How can the geometry of pre-trained weights be exploited with theoretical grounding to improve parameter-efficient fine-tuning?
**Methodology**: The authors introduce PiCa, a theoretically grounded PEFT method that projects gradients onto the principal column space of pre-trained weights and enhances parameter efficiency through a novel weight-sharing strategy.
**Key findings**:
- Projecting gradients onto the principal column space of pre-trained weights provides an effective inductive bias for adaptation
- PiCa consistently outperforms state-of-the-art baselines across diverse NLP and vision tasks
- The method achieves superior performance under comparable or smaller parameter budgets than existing approaches
- PiCa provides both theoretical rigor and practical effectiveness for parameter-efficient fine-tuning
**Limitations**: Not stated in abstract

### Koike-Akino et al. (2025)

**Research question**: Can quantum computations enable ultra parameter-efficient fine-tuning with logarithmic parameter growth compared to linear growth in LoRA-based methods?
**Methodology**: The authors introduce Quantum-PEFT, which leverages quantum computations with Pauli parameterization to achieve full-rank yet parameter-efficient quantum unitary parameterization where trainable parameters grow logarithmically with ambient dimension.
**Key findings**:
- Quantum-PEFT exploits full-rank quantum unitary parameterization that is surprisingly parameter efficient
- The number of trainable parameters grows logarithmically with ambient dimension, unlike linear growth in LoRA-based methods
- Quantum-PEFT achieves vanishingly smaller number of trainable parameters than the lowest-rank LoRA as dimensions grow
- The method demonstrates significant advantages in parameter efficiency on language and vision transfer learning benchmarks while maintaining competitive performance
**Limitations**: Not stated in abstract

### Lee et al. (2025)

**Research question**: How can parameter-efficient fine-tuning methods be adapted to address the unique temporal processing dynamics of State Space Models like Mamba?
**Methodology**: The authors propose Memba, a membrane-driven PEFT approach that introduces Leaky Integrate Membrane neurons as bio-inspired gating mechanisms, combined with Low-Rank Adaptations and cross-layer membrane transfer to enhance Mamba's temporal modeling capabilities.
**Key findings**:
- Memba introduces LIM neurons that naturally accumulate membrane potentials over time, enhancing selective information retention
- The approach strategically combines LIM neurons with LoRA and cross-layer membrane transfer
- Extensive experiments demonstrate substantial improvements over existing PEFT methods across language and vision tasks
**Limitations**: Not stated in abstract

### Li et al. (2026)

**Research question**: What are the methodological and functional differences between parameter-efficient fine-tuning methods, and is spectral preservation important for adaptation and retention?
**Methodology**: The authors compare six PEFT methods in language and diffusion models, examining how parameterizations relate to task performance, forgetting, and pretrained weight geometry, with intervention experiments on spectral component modifications.
**Key findings**:
- LoRA-family methods approximately preserve pretrained geometry, and restoring their drifted singular-value spectra largely preserves task performance
- LoRA most consistently limits forgetting at competitive performance across settings
- DoRA achieves higher mean task scores than LoRA in most comparisons, while PiSSA often incurs greater retention costs
- Restoring dominant spectral components produces the largest mean reduction in general-text NLL or base-image drift
**Limitations**: Not stated in abstract

### Peng et al. (2026)

**Research question**: How can intermediate representations from deeper layers be leveraged to improve parameter-efficient fine-tuning beyond weight-space modifications?
**Methodology**: The authors propose Echo-LoRA, which collects boundary hidden states from deeper source layers, aggregates them into sample-level echo representations, and injects the signal into shallow LoRA/DoRA modules via lightweight projection and gating networks, using answer-only masking, masked distillation, and stochastic routing for stability.
**Key findings**:
- Echo-LoRA exceeds LoRA baselines by 5.7 percentage points on average across eight commonsense reasoning benchmarks
- Under reproduced baselines in unified implementation, Echo-LoRA achieves 3.0 points average gain; combined with DoRA, the gain is 2.7 points
- The Echo path is discarded after training, so deployed models retain original low-rank LoRA/DoRA form with no inference-time overhead
- Cross-layer representation injection effectively utilizes intermediate representations that are typically unused in existing LoRA variants
**Limitations**: Not stated in abstract

### Tripathi et al. (2026)

**Research question**: How can rank allocation in Low-Rank Adaptation be optimized to address the suboptimality of uniform rank assignment across transformer layers?
**Methodology**: The authors propose LAARA, a search-free framework that dynamically allocates ranks using lightweight diagonal Fisher estimates computed during training, combining projection-wise normalization, logarithmic compression, blended adapter importance estimation, and a vote-to-change dampening mechanism.
**Key findings**:
- Uniform rank allocation in LoRA is theoretically and empirically suboptimal due to heterogeneous adaptation requirements across transformer layers
- LAARA matches or outperforms state-of-the-art methods (LoRA, AdaLoRA, DyLoRA, BitFit) on GLUE and MathInstruct benchmarks
- LAARA achieves comparable or better performance while using significantly fewer trainable parameters
- Fisher-guided rank allocation provides a principled foundation for adaptive parameter-efficient fine-tuning
**Limitations**: Not stated in abstract

### Xu and Bu (2025)

**Research question**: How can the most influential subset of parameters be effectively selected for training in parameter-efficient fine-tuning?
**Methodology**: The authors formulate subset selection as a multi-task optimization problem and leverage ε-constraint method and second-order Taylor approximation to arrive at a 0-1 knapsack problem solved through Pareto optimality, resulting in AdaPEFT, a Hessian-informed PEFT method.
**Key findings**:
- AdaPEFT adapts to various tasks and models through Hessian-informed subset selection
- The selected subset empirically transfers across training horizons and model sizes
- The approach frames PEFT as maximizing performance while minimizing trainable parameters
**Limitations**: Not stated in abstract

### Xu et al. (2025)

**Research question**: How can pretrained weight structures be more effectively leveraged to generate task-specific updates in parameter-efficient fine-tuning?
**Methodology**: The authors propose GenFT, a W0-conditioned PEFT method that uses a deterministic weight generator to produce task-specific updates through row and column transformations with nonlinear activations and shared-specific decomposition.
**Key findings**:
- GenFT extracts structured patterns from pretrained weights through row and column transformations with nonlinear activations
- The shared-specific decomposition balances cross-layer information reuse and layer-specific flexibility
- GenFT achieves competitive or better average performance across NLP and CV benchmarks
- The method is simple and parameter-efficient, with feasibility demonstrated on LLaMA-7B
**Limitations**: Not stated in abstract

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
