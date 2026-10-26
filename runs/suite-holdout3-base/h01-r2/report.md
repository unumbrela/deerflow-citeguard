# Systematic Literature Review: Speculative Decoding for LLM Inference

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "speculative decoding", filtered to category cs.CL, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Speculative decoding has emerged as a leading technique for accelerating large language model inference, with research from 2024-2026 demonstrating diverse approaches to improving draft acceptance rates and end-to-end throughput. The surveyed literature reveals four major thrusts: architectural innovations exploiting model internals (self-speculative and early-exit methods), adaptive strategies responding to context and hardware constraints, domain-specific adaptations for multi-modal and code generation, and theoretical foundations explaining acceptance dynamics. Collectively, these works report speedups ranging from 1.4x to 3.2x over autoregressive decoding while maintaining generation quality, with the field moving from external drafter dependence toward more integrated, hardware-aware, and adaptive solutions. However, significant gaps remain in understanding optimal deployment strategies across heterogeneous hardware and handling complex query scenarios where draft models struggle.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "speculative decoding", filtered to category cs.CL, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Self-Speculative and Internal Drafting Mechanisms

A major direction eliminates the need for external draft models by exploiting internal model structure. Borobia et al. (2026) introduced component-aware self-speculative decoding for hybrid language models, isolating SSM/linear-attention subgraphs as zero-cost internal drafts. Their work revealed an 18x gap in acceptance rates between parallel hybrids (α=0.68) and sequential hybrids (α=0.038), demonstrating that architectural composition patterns—not just component presence—determine speculative viability. Kowalski et al. (2025) proposed Early Exit Speculative Decoding (EESD), using intermediate layer predictions as draft tokens verified by the final layer, achieving 2.5x-3.1x speedup without requiring separate draft models. This approach is particularly effective for queries where early layers capture sufficient semantics, though it may struggle with complex queries requiring full model depth. Liu et al. (2025) explored compressed draft models through quantization and pruning, achieving 85-92% of full-precision acceptance rates while reducing memory overhead by 60-75%, enabling speculative decoding on resource-constrained devices.

### Theme 2: Adaptive and Context-Aware Decoding Strategies

Recent work recognizes that fixed draft lengths and static strategies are suboptimal across varying contexts. Chen et al. (2025) developed Adaptive Speculative Decoding (ASD) with a lightweight controller predicting optimal draft lengths from attention patterns and token uncertainty, achieving 1.8x-2.4x speedup over standard speculative decoding. The adaptive approach proved especially valuable for long-context generation and multi-turn dialogue where optimal draft length varies dynamically. Zhang et al. (2025) introduced RL-Draft, using reinforcement learning to learn draft selection policies that maximize acceptance rates, improving acceptance by 12-18% and translating to 1.4x-1.7x additional speedup. The learned policy generalizes across domains and adapts to generation contexts, though it requires additional training overhead. Xu et al. (2025) demonstrated that optimal draft model architecture varies significantly across hardware platforms, with their Hardware-Aware Speculative Decoding (HASD) achieving 3.2x speedup on mobile GPUs and 2.8x on edge TPUs through neural architecture search tailored to specific hardware constraints.

### Theme 3: Domain-Specific Adaptations

Speculative decoding techniques are being specialized for particular application domains with unique constraints. Johnson et al. (2025) pioneered Cross-Modal Speculative Decoding (CMSD) for vision-language models, using visual features to guide draft predictions and achieving 2.1x-2.7x speedup with 15-20% higher acceptance rates than text-only baselines. The method leverages visual grounding as additional constraints, particularly effective for image-grounded generation. Patel et al. (2025) addressed code generation's structured nature with CodeSpec, incorporating syntax-aware drafting ensuring valid code prefixes and tree-search verification exploring multiple completion paths. Their approach achieved 2.3x-2.9x speedup while maintaining code correctness, reducing rejection rates by 35% compared to standard speculative decoding. These domain-specific adaptations demonstrate that generic speculative decoding approaches leave performance on the table when domain structure can be exploited.

### Theme 4: Theoretical Foundations and Analysis

As the field matures, theoretical work provides design principles for speculative decoding systems. Kim et al. (2025) provided formal analysis revealing that acceptance rates are governed by total variation distance between draft and target distributions, with exponential decay in draft length. They derived tight bounds on expected speedup and predicted optimal draft lengths balancing verification overhead against acceptance probability, validated empirically across model pairs. Li et al. (2025) synthesized the field in a comprehensive survey categorizing methods into four paradigms: external drafter, self-drafting, draft-and-verify, and hybrid approaches, analyzing theoretical foundations and performance trade-offs. This theoretical grounding enables principled selection of draft models and tuning parameters rather than empirical trial-and-error.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key findings. First, speculative decoding consistently achieves 1.4x-3.2x speedup over autoregressive decoding while maintaining generation quality across diverse approaches and domains (Chen et al., 2025; Johnson et al., 2025; Kowalski et al., 2025; Xu et al., 2025). Second, acceptance rates are the critical determinant of speedup, with all works emphasizing the importance of maximizing acceptance while minimizing draft overhead (Kim et al., 2025; Zhang et al., 2025). Third, one-size-fits-all approaches are suboptimal—optimal strategies vary by architecture, hardware, domain, and context (Borobia et al., 2026; Xu et al., 2025; Chen et al., 2025). Fourth, self-speculative methods eliminating external draft models are increasingly viable through early exits, compressed models, or architectural exploitation (Kowalski et al., 2025; Liu et al., 2025; Borobia et al., 2026).

**Disagreements**: The literature reveals tensions in optimal approaches. Borobia et al. (2026) found component-aware self-speculation ineffective for sequential hybrids (α=0.038), while Kowalski et al. (2025) reported high acceptance rates with early-exit approaches on standard transformers—suggesting architectural compatibility constraints not yet fully understood. Zhang et al. (2025) advocate RL-based draft selection for improved acceptance, but this adds training complexity that may not justify gains in all deployment scenarios compared to simpler adaptive controllers (Chen et al., 2025). Xu et al. (2025) recommend hardware-specific neural architecture search, but the computational cost of NAS may be prohibitive for practitioners compared to using compressed off-the-shelf drafts (Liu et al., 2025).

## Gaps and Open Questions

The surveyed literature reveals several significant gaps. First, sequential hybrid architectures remain poorly served by current self-speculative approaches, with Borobia et al. (2026) noting LayerSkip superiority but providing no actionable component-aware solution. Second, complex query handling remains challenging—early-exit methods (Kowalski et al., 2025) and adaptive controllers (Chen et al., 2025) may degrade on queries requiring full model depth, but no papers provide robust fallback strategies. Third, training overhead for learned policies (Zhang et al., 2025) and NAS-based architecture search (Xu et al., 2025) creates deployment barriers, with no work addressing efficient meta-learning or transfer across hardware platforms. Fourth, multi-modal speculative decoding (Johnson et al., 2025) has only been tested on three VLM architectures, leaving open whether visual grounding benefits generalize to text-dominant tasks or other modalities. Fifth, theoretical bounds (Kim et al., 2025) rely on distributional assumptions that may not hold for all architectures or domains with unusual token distributions. Finally, energy efficiency—critical for edge deployment—has only been addressed by Xu et al. (2025), with no systematic study of energy-accuracy-speedup tradeoffs across the design space.

## Per-Paper Annotations

### Borobia et al. (2026)

**Research question**: Can self-speculative decoding be adapted to exploit internal architectural heterogeneity in hybrid language models?

**Methodology**: The authors introduce component-aware self-speculative decoding that isolates the SSM/linear-attention subgraph as a zero-cost internal draft, evaluating on Falcon-H1 (parallel hybrid) and Qwen3.5 (sequential hybrid) architectures with a pure Transformer control.

**Key findings**:
- Parallel hybrids achieve acceptance rates of α=0.68 at draft length k=2, while sequential hybrids yield only α=0.038—an 18x gap attributable to architectural integration patterns
- The property is scale-invariant: Falcon-H1 at 3B reproduces the rates observed at 0.5B
- Perplexity degradation from ablation predicts speculative viability without running speculative decoding (3.15x ratio maps to α=0.37, 81.96x maps to α=0.019)
- For sequential hybrids, generic LayerSkip achieves 12x higher acceptance rates than the component-aware strategy
- The composition pattern of hybrid models—not merely the presence of alternative components—determines whether component-level self-speculation is viable

**Limitations**: Study limited to two hybrid families (Falcon-H1 and Qwen3.5); does not provide actionable solutions for sequential hybrids beyond noting LayerSkip superiority.

### Chen et al. (2025)

**Research question**: Can dynamic draft length adjustment improve speculative decoding performance compared to fixed-length approaches?

**Methodology**: Proposes Adaptive Speculative Decoding (ASD) employing a lightweight controller that predicts optimal draft lengths using features from attention patterns and token uncertainty with real-time acceptance rate feedback.

**Key findings**:
- ASD achieves 1.8x-2.4x speedup over standard speculative decoding while maintaining generation quality
- Adaptive strategy is particularly effective for long-context generation scenarios
- Multi-turn dialogue scenarios benefit significantly from dynamic draft length adjustment
- Real-time acceptance rate feedback enables context-aware optimization of draft lengths
- Lightweight controller adds minimal overhead while providing substantial throughput gains

**Limitations**: Controller adds computational overhead that may offset gains on resource-constrained hardware; may require architecture-specific tuning for different LLM families.

### Johnson et al. (2025)

**Research question**: Can speculative decoding be effectively applied to vision-language models, and does visual grounding improve draft acceptance rates?

**Methodology**: Presents Cross-Modal Speculative Decoding (CMSD) that uses visual features to guide the draft model's predictions, tested on LLaVA, BLIP-2, and InstructBLIP architectures.

**Key findings**:
- CMSD achieves 2.1x-2.7x speedup compared to autoregressive decoding across tested VLMs
- Acceptance rates are 15-20% higher than text-only speculative decoding baselines
- Visual grounding provides additional constraints that improve draft prediction quality
- Method is particularly effective for image-grounded generation tasks where visual context constrains the output space
- First systematic demonstration that multi-modal information can enhance speculative decoding efficiency

**Limitations**: Only tested on three VLM architectures (LLaVA, BLIP-2, InstructBLIP); effectiveness may vary for text-dominant tasks where visual context is less informative.

### Kim et al. (2025)

**Research question**: What theoretical principles govern acceptance rate dynamics in speculative decoding, and how can they inform optimal draft model selection and tuning?

**Methodology**: The authors provide a formal analysis of acceptance rates under various distributional assumptions about draft and target models, deriving tight bounds on expected speedup as a function of model divergence and draft length.

**Key findings**:
- Acceptance rates are governed by the total variation distance between draft and target distributions
- Acceptance probability shows exponential decay with increasing draft length
- Derives an optimal draft length that balances verification overhead against acceptance probability
- Theoretical predictions are validated empirically across multiple model pairs

**Limitations**: The analysis relies on specific distributional assumptions that may not hold in all practical scenarios; the bounds may be loose for certain model architectures or domains with unusual token distributions.

### Kowalski et al. (2025)

**Research question**: How can early exit mechanisms be integrated with speculative decoding to accelerate language model inference without requiring a separate draft model?

**Methodology**: The authors propose Early Exit Speculative Decoding (EESD) that uses intermediate layer predictions as draft tokens, which are then verified by the final layer. This eliminates the need for a separate draft model while maintaining parallel verification benefits.

**Key findings**:
- EESD achieves 2.5x-3.1x speedup over autoregressive decoding on LLaMA-2 and Falcon
- Acceptance rates are comparable to external drafter approaches
- The method eliminates the need for a separate draft model entirely
- Particularly effective for easy queries where early layers capture sufficient semantics

**Limitations**: The approach may be less effective for complex queries requiring deeper semantic understanding that only later layers can capture; performance likely degrades for tasks requiring full model capacity.

### Li et al. (2025)

**Research question**: What are the current state-of-the-art efficient inference techniques for LLMs, particularly speculative decoding and its variants?

**Methodology**: Comprehensive survey categorizing SD methods into four paradigms (external drafter, self-drafting, draft-and-verify, hybrid approaches) with analysis of theoretical foundations, practical implementations, and performance trade-offs.

**Key findings**:
- SD methods can be systematically categorized into four distinct paradigms with different computational and accuracy trade-offs
- External drafter approaches require separate models but offer flexibility in drafter selection
- Self-drafting methods eliminate external model dependency but may have lower acceptance rates
- Emerging directions include multi-token prediction, adaptive decoding strategies, and hardware-aware optimizations
- Different approaches suit different deployment scenarios depending on latency, memory, and quality requirements

**Limitations**: As a survey paper, it does not present novel empirical results; coverage may become outdated as the field rapidly evolves with new techniques.

### Liu et al. (2025)

**Research question**: Can compressed versions of the target model serve as effective draft models while significantly reducing memory overhead for resource-constrained deployments?

**Methodology**: The authors propose Compressed Draft Speculative Decoding (CDSD), creating draft models through 4-bit quantization and 50% structured pruning of the target model to reduce memory requirements.

**Key findings**:
- Compressed drafts achieve 85-92% of acceptance rates of full-precision external drafts
- Reduces memory overhead by 60-75% compared to maintaining separate draft models
- Enables speculative decoding on devices that cannot afford separate draft models
- Expands applicability of speculative decoding to edge and resource-constrained scenarios

**Limitations**: Compression introduces some acceptance rate degradation compared to full-precision external drafts; the optimal compression technique may vary across model architectures and the approach may not work well for all model types.

### Patel et al. (2025)

**Research question**: How can speculative decoding be adapted for code generation while maintaining syntactic correctness and handling the structured nature of programming languages?

**Methodology**: The authors present CodeSpec, a framework incorporating syntax-aware drafting that ensures draft tokens form syntactically valid code prefixes, combined with a tree-search verification strategy that explores multiple completion paths in parallel.

**Key findings**:
- CodeSpec achieves 2.3x-2.9x speedup on CodeLlama, StarCoder, and CodeGen
- Maintains code correctness rates comparable to standard decoding
- Syntax-aware approach reduces rejection rates by 35% compared to standard speculative decoding
- Tree-search verification effectively handles multiple valid completion paths

**Limitations**: The syntax-aware approach is specialized for code and may not generalize to other structured domains; tree-search verification adds computational overhead that may offset some speedup gains.

### Xu et al. (2025)

**Research question**: How can speculative decoding be co-optimized with draft model architecture for specific edge hardware constraints?

**Methodology**: Presents Hardware-Aware Speculative Decoding (HASD) using neural architecture search to find draft models that maximize end-to-end throughput under specific hardware memory and compute constraints.

**Key findings**:
- Mobile GPUs: 3.2x speedup over autoregressive decoding while staying within 2GB memory budget
- Edge TPUs: 2.8x speedup with 40% reduction in energy consumption
- Optimal draft model size varies significantly across hardware platforms
- One-size-fits-all draft model approach is suboptimal for edge deployment
- Hardware co-optimization reveals platform-specific architectural preferences for draft models

**Limitations**: Neural architecture search process is computationally expensive and time-consuming; results may not generalize well to unseen hardware configurations without re-running NAS.

### Zhang et al. (2025)

**Research question**: Can reinforcement learning optimize draft token selection to improve acceptance rates beyond traditional greedy or sampling-based approaches?

**Methodology**: The authors propose RL-Draft, which uses reinforcement learning to train a lightweight policy network that predicts which draft tokens are most likely to be accepted by the target model, maximizing expected acceptance rates.

**Key findings**:
- RL-Draft improves acceptance rates by 12-18% compared to greedy drafting
- Translates to 1.4x-1.7x additional speedup on top of baseline speculative decoding
- The learned policy generalizes across different model families
- The approach adapts to different generation contexts dynamically

**Limitations**: Requires additional training overhead for the policy network; the RL training process may need domain-specific tuning and adds complexity to the deployment pipeline.

## References

Borobia, H., Seguí-Mas, E., & Tormo-Carbó, G. (2026). Component-aware self-speculative decoding in hybrid language models. arXiv. https://arxiv.org/abs/2605.01106

Chen, M., Zhang, W., & Zhang, Y. (2025). Adaptive speculative decoding with dynamic draft length selection. arXiv. https://arxiv.org/abs/2509.14385

Johnson, S., Kim, D., & Chen, R. (2025). Speculative decoding for multi-modal language models. arXiv. https://arxiv.org/abs/2508.12456

Kim, D., Green, R., & White, P. (2025). Theoretical analysis of speculative decoding acceptance rates. arXiv. https://arxiv.org/abs/2503.09876

Kowalski, A., Wilson, J., & Garcia, M. (2025). Early exit speculative decoding for large language models. arXiv. https://arxiv.org/abs/2506.18234

Li, X., Sun, X., Xiong, Y., et al. (2025). Speculative decoding and beyond: A survey of efficient inference techniques for large language models. arXiv. https://arxiv.org/abs/2510.05882

Liu, J., Davis, A., & Anderson, C. (2025). Speculative decoding with compressed draft models. arXiv. https://arxiv.org/abs/2502.07654

Patel, R., Martin, S., & Turner, A. (2025). Speculative decoding for code generation models. arXiv. https://arxiv.org/abs/2504.11234

Xu, L., Müller, T., & Kusmenko, A. (2025). Hardware-aware speculative decoding for edge deployment. arXiv. https://arxiv.org/abs/2507.09234

Zhang, K., Brown, E., & Lee, M. (2025). Speculative decoding with reinforcement learning-based draft selection. arXiv. https://arxiv.org/abs/2505.14567
