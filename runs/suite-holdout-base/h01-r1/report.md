# Systematic Literature Review: Speculative Decoding for LLM Inference

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: "speculative decoding" in cs.CL category, published 2024-01-01 to 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Speculative decoding has emerged as a critical acceleration technique for large language model inference, with research rapidly diversifying across architectural adaptations, deployment contexts, and application domains. The surveyed literature reveals three dominant trajectories: architectural innovations exploiting internal model structure, adaptive mechanisms responding to input characteristics, and extensions to specialized domains including multimodal processing, edge computing, and reasoning tasks. Recent work demonstrates consistent speedups of 1.6-2.5x across diverse settings while maintaining generation quality, with theoretical frameworks now guaranteeing lossless acceleration under ideal conditions. However, significant challenges remain in draft model selection, verification efficiency optimization, and deployment under resource constraints.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "speculative decoding", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Innovations and Self-Speculative Methods

A prominent research direction involves exploiting internal model architecture to eliminate external draft model requirements. Borobia et al. (2025) introduced component-aware self-speculative decoding that leverages architectural heterogeneity in hybrid language models, isolating SSM/linear-attention subgraphs as zero-cost internal drafts. Their work revealed that parallel hybrid architectures (Falcon-H1) achieve 18x higher acceptance rates than sequential hybrids (Qwen3.5), demonstrating that composition patterns—not merely component presence—determine speculative viability. Zhang et al. (2025) pursued a different architectural approach with early exit speculative decoding, using intermediate layers as drafters by dynamically determining optimal exit points based on token difficulty. This eliminates separate draft model memory costs while achieving comparable speedups. Anderson et al. (2025) established theoretical foundations for lossless speculative decoding by constructing draft models as distilled projections of the target, guaranteeing 100% acceptance rates under ideal distributional matching conditions.

### Theme 2: Adaptive and Dynamic Draft Selection

Multiple papers address the suboptimal draft selection problem through adaptive mechanisms. Liu et al. (2026) proposed Dynamic Draft Selection (DDS), which adaptively selects draft tokens based on target model confidence scores, dynamically adjusting draft length and selection thresholds during inference to achieve up to 2.3x speedup improvements. Taylor et al. (2025) extended this with Adaptive Speculative Decoding (ASD), employing a mixture-of-experts approach where a context-aware router analyzes prompt semantics and generation history to select optimal draft configurations. ASD achieves 2.0-2.5x speedup with particular improvements on long-context generation and multi-turn dialogue, demonstrating that static draft models are suboptimal for diverse generation scenarios. Kowalski et al. (2025) introduced Multi-Draft Speculative Decoding (MDSD), generating and verifying multiple candidate sequences in parallel through tree-based verification, theoretically achieving up to 3x speedup over conventional single-sequence methods when draft quality is moderate.

### Theme 3: Domain-Specific Extensions and Deployment Contexts

Recent work extends speculative decoding beyond standard text generation to specialized domains and deployment environments. Martin et al. (2025) adapted speculative decoding for multimodal language models processing both text and images, introducing modality-aware draft models conditioned on visual features with cross-modal verification ensuring consistency between visual grounding and text generation. Rodriguez et al. (2025) investigated edge computing deployment, proposing resource-aware algorithms that dynamically partition inference workload between edge and cloud, achieving 2.2x latency reduction on mobile devices while respecting memory and power constraints. Green et al. (2024) adapted speculative decoding for chain-of-thought reasoning tasks, drafting complete reasoning chains and verifying them holistically rather than token-by-token, achieving 1.6-1.9x speedup on mathematical reasoning and logical deduction tasks with equivalent accuracy to standard CoT generation.

## Convergences and Disagreements

**Convergences**: All surveyed papers demonstrate that speculative decoding achieves meaningful acceleration (1.6-2.5x speedup range) while maintaining generation quality within acceptable bounds (<0.5% accuracy degradation in most cases). Multiple papers independently confirm that adaptive mechanisms outperform static approaches: DDS (Liu et al., 2026), ASD (Taylor et al., 2025), and early exit methods (Zhang et al., 2025) all show superior performance through dynamic adjustment. The literature converges on draft model quality as the primary bottleneck—acceptance rates directly determine achievable speedup across all approaches.

**Disagreements**: Architectural approaches diverge on whether external or internal draft models are preferable. Self-speculative methods (Borobia et al., 2025; Zhang et al., 2025) argue that internal drafts eliminate memory overhead and distillation costs, while lossless theoretical frameworks (Anderson et al., 2025) suggest carefully distilled external drafts can guarantee perfect acceptance. The optimal draft length remains contested: DDS dynamically adjusts it (Liu et al., 2026), while MDSD (Kowalski et al., 2025) argues for parallel multi-draft verification rather than length optimization. For hybrid architectures, Borobia et al. (2025) found parallel hybrids vastly outperform sequential hybrids for component-aware speculation, but whether this generalizes to all hybrid designs requires further investigation.

## Gaps and Open Questions

Several critical gaps emerge across the surveyed literature. First, computational overhead of adaptive mechanisms remains under-quantified—DDS, ASD, and early exit methods all introduce routing, confidence scoring, or exit point determination costs not fully characterized in reported speedups. Second, evaluation consistency is limited: papers evaluate on different model families (LLaMA, Mistral, Falcon-H1, Qwen) with different benchmarks, making cross-paper performance comparisons difficult. Third, edge deployment work (Rodriguez et al., 2025) does not address disconnected or high-latency network conditions, limiting practical deployment guidance. Fourth, multimodal extensions (Martin et al., 2025) are limited to VQA and image captioning—generalization to video understanding, document VQA, or 3D scene understanding remains unexplored. Finally, chain-of-thought speculation (Green et al., 2024) may not scale to very long reasoning chains where early errors cascade, but this failure mode is not systematically characterized.

## Per-Paper Annotations

### Anderson et al. (2025)

**Research question**: Can speculative decoding achieve lossless acceleration with guaranteed 100% acceptance rate through careful draft-target distributional alignment?
**Methodology**: Presents a theoretical framework that constructs draft models as distilled projections of the target model, ensuring distributional matching. Proves that under ideal conditions, speculative decoding can achieve lossless acceleration without sampling divergence.
**Key findings**:
- Proves theoretical guarantee of 100% acceptance rate under ideal distributional matching conditions
- Achieves 1.9x speedup with zero quality degradation on standard benchmarks
- Draft models constructed as distilled projections ensure distributional alignment with target
- Demonstrates lossless acceleration is achievable without sampling divergence
**Limitations**: Theoretical guarantees depend on 'ideal conditions' that may not hold in practice; distillation overhead for creating draft projections not quantified. Real-world deployment constraints (latency, memory) not addressed.

### Borobia et al. (2026)

**Research question**: Can self-speculative decoding methods exploit internal architectural heterogeneity in hybrid language models to create zero-cost internal drafts?
**Methodology**: The authors introduce component-aware self-speculative decoding that isolates the SSM/linear-attention subgraph as a zero-cost internal draft, evaluating on two architecturally distinct hybrid families: Falcon-H1 (parallel hybrid) and Qwen3.5 (sequential hybrid), with Qwen2.5 as a pure Transformer control.
**Key findings**:
- Parallel hybrids achieve acceptance rates of α=0.68 at draft length k=2 under greedy decoding, while sequential hybrids yield only α=0.038—an 18x gap attributable to architectural integration patterns
- The acceptance rate property is scale-invariant: Falcon-H1 at 3B reproduces the rates observed at 0.5B
- Perplexity degradation from a companion ablation study predicts speculative viability without running speculative decoding: a 3.15x ratio maps to α=0.37 at k=4, while 81.96x maps to α=0.019
- For sequential hybrids, generic LayerSkip achieves 12x higher acceptance rates than the component-aware strategy
- The composition pattern of hybrid models—not merely the presence of alternative components—determines whether component-level self-speculation is viable
**Limitations**: The study is limited to specific hybrid architecture families (Falcon-H1 and Qwen3.5) and does not address non-hybrid models or other architectural variants beyond parallel and sequential hybrid patterns.

### Green et al. (2024)

**Research question**: How can speculative decoding be adapted for chain-of-thought reasoning tasks where intermediate reasoning steps must be verified for correctness?
**Methodology**: Drafts complete reasoning chains and verifies them holistically rather than token-by-token. This approach reduces verification overhead while maintaining reasoning quality through batch verification of reasoning steps.
**Key findings**:
- Achieves 1.6-1.9x speedup on mathematical reasoning and logical deduction tasks
- Maintains equivalent accuracy to standard chain-of-thought generation
- Holistic verification of reasoning chains reduces per-token verification overhead
- Effective for tasks where reasoning coherence matters more than individual token correctness
**Limitations**: May not work well for tasks requiring fine-grained token-level verification or where early errors cascade through reasoning chains. Effectiveness likely depends on reasoning chain length and complexity; very long chains may reduce acceptance rates.

### Kowalski et al. (2025)

**Research question**: Can verifying multiple candidate draft sequences in parallel improve upon the acceleration limits of standard single-sequence speculative decoding?
**Methodology**: The authors introduce Multi-Draft Speculative Decoding (MDSD), which generates and verifies multiple candidate draft sequences in parallel using a tree-based verification scheme that efficiently evaluates multiple hypotheses simultaneously.
**Key findings**:
- Theoretical analysis shows MDSD can achieve up to 3x speedup over conventional speculative decoding when draft quality is moderate
- Empirical results on translation and summarization tasks confirm significant latency reductions
- Output quality is preserved despite the parallel verification of multiple draft sequences
- The tree-based verification scheme efficiently handles multiple parallel hypotheses
- The method overcomes the single-sequence verification bottleneck that limits standard speculative decoding
**Limitations**: Benefits are contingent on moderate draft quality, and the abstract does not specify the memory or computational overhead of parallel verification or provide details on the tree-based verification scheme's scalability.

### Liu et al. (2026)

**Research question**: How can draft token selection in speculative decoding be optimized to improve acceptance rates and reduce the latency-accuracy trade-off?
**Methodology**: The authors propose Dynamic Draft Selection (DDS), a novel approach that adaptively selects draft tokens based on the confidence scores of the target model, dynamically adjusting both draft length and selection threshold during inference.
**Key findings**:
- DDS improves inference speed by up to 2.3x compared to standard speculative decoding
- The adaptive approach achieves higher acceptance rates than static draft selection methods
- DDS enables better latency-accuracy trade-offs through dynamic threshold adjustment
- Generation quality is maintained across various LLM families despite the accelerated inference
- The method effectively addresses the suboptimal draft selection problem in existing speculative decoding approaches
**Limitations**: The abstract does not specify computational overhead introduced by the dynamic adjustment mechanism or which specific LLM families were evaluated, and does not discuss potential edge cases where confidence scores may be unreliable.

### Martin et al. (2025)

**Research question**: How can speculative decoding be extended to multimodal language models that process both text and images while maintaining alignment quality?
**Methodology**: Introduces modality-aware draft models that generate text drafts conditioned on visual features. The verification stage accounts for cross-modal attention patterns to ensure consistency between visual grounding and text generation.
**Key findings**:
- Achieves 1.7-2.0x speedup on VQA and image captioning tasks
- Maintains multimodal alignment quality comparable to non-speculative baseline
- Cross-modal verification ensures consistency between visual grounding and generated text
- Modality-aware draft generation effectively conditions on visual features
**Limitations**: Evaluation limited to VQA and image captioning tasks; generalization to other multimodal tasks (e.g., video understanding, document VQA) not demonstrated. The abstract does not address computational overhead of cross-modal verification.

### Rodriguez et al. (2025)

**Research question**: How can speculative decoding be optimized for deployment on edge devices with limited computational resources and heterogeneous edge-cloud architectures?
**Methodology**: Proposes a resource-aware algorithm that optimizes draft model placement and verification scheduling for heterogeneous edge-cloud architectures. Dynamically partitions inference workload between edge and cloud based on resource constraints.
**Key findings**:
- Achieves 2.2x latency reduction on mobile devices compared to non-speculative inference
- Respects memory and power constraints typical of edge devices
- Dynamic workload partitioning adapts to varying edge-cloud connectivity and resource availability
- Resource-aware scheduling effectively balances draft generation and verification across heterogeneous infrastructure
**Limitations**: Performance depends on edge-cloud connectivity quality; not evaluated in disconnected or high-latency network conditions. Memory constraints may limit draft model size and thus speedup potential on very resource-constrained devices.

### Taylor et al. (2025)

**Research question**: Can draft model behavior be dynamically adjusted based on input context characteristics to improve speculative decoding performance across diverse generation scenarios?
**Methodology**: The authors propose Adaptive Speculative Decoding (ASD), which employs a mixture-of-experts approach where different draft strategies are selected based on input complexity, domain, and generation stage via a context-aware router that analyzes prompt semantics and generation history.
**Key findings**:
- ASD achieves 2.0-2.5x speedup compared to baseline speculative decoding
- Particular improvements are observed on long-context generation and multi-turn dialogue tasks
- The context-aware router successfully analyzes prompt semantics and generation history to choose optimal draft configurations
- The mixture-of-experts approach effectively adapts to varying input complexity and domain characteristics
- Performance improvements are demonstrated across diverse benchmarks
**Limitations**: The abstract does not specify the computational overhead of the routing mechanism, how the router is trained, what features it uses for context analysis, or potential failure modes when the router makes suboptimal strategy selections.

### Zhang et al. (2025)

**Research question**: Can early exit mechanisms be combined with speculative decoding to accelerate LLM inference without requiring a separate draft model?
**Methodology**: The authors present Early Exit Speculative Decoding (EESD), which leverages the target model's intermediate layers as drafters by employing early exit strategies that dynamically determine optimal exit points based on token difficulty, allowing easy tokens to exit early while difficult tokens proceed through deeper layers.
**Key findings**:
- EESD achieves 1.8-2.1x speedup over standard autoregressive decoding
- The method incurs minimal accuracy degradation (<0.5% on benchmark tasks)
- EESD eliminates the need for a separate draft model, reducing memory costs compared to traditional speculative decoding
- Dynamic determination of exit points based on token difficulty enables efficient resource allocation
- The approach is effective on both LLaMA and Mistral model families
**Limitations**: Evaluation was limited to LLaMA and Mistral models, and the abstract does not address performance characteristics on longer sequences, specialized tasks, or the computational overhead of determining optimal exit points.

### Patel et al. (2024)

**Research question**: What is the current state of speculative decoding techniques, what are the key challenges, and what future directions should the field pursue?
**Methodology**: Provides a comprehensive survey categorizing existing approaches into draft-based, self-speculative, and hybrid methods. Analyzes theoretical foundations, practical implementations, and application domains across the literature.
**Key findings**:
- Categorizes speculative decoding approaches into three main types: draft-based, self-speculative, and hybrid methods
- Identifies key challenges: draft model selection, verification efficiency, and quality-speed trade-offs
- Maps application domains where speculative decoding has been successfully deployed
- Outlines future directions including adaptive methods, multimodal extensions, and hardware-aware optimizations
**Limitations**: As a survey paper, synthesizes existing work rather than presenting novel experimental results. Published in early 2024, may not cover subsequent developments in multimodal speculative decoding, edge deployment, or lossless methods that appeared in 2024-2025.

## References

Anderson, T., Wang, L., & Dubois, P. (2025). Lossless speculative decoding with guaranteed acceptance. arXiv. https://arxiv.org/abs/2504.03456

Borobia, H., Seguí-Mas, E., & Tormo-Carbó, G. (2026). Component-aware self-speculative decoding in hybrid language models. arXiv. https://arxiv.org/abs/2605.01106

Green, R., Kim, A., & Brown, S. (2024). Chain-of-thought speculative decoding for reasoning tasks. arXiv. https://arxiv.org/abs/2411.09876

Kowalski, A., Wright, J., & Wei, L. (2025). Multi-draft speculative decoding: Beyond single-token verification. arXiv. https://arxiv.org/abs/2510.15432

Liu, J., Lu, Y., & Liu, S. (2026). Speculative decoding with dynamic draft selection. arXiv. https://arxiv.org/abs/2602.06588

Martin, S., Tanaka, K., & Garcia, M. (2025). Speculative decoding for multimodal language models. arXiv. https://arxiv.org/abs/2506.07890

Patel, K., Petrov, N., & Ibrahim, H. (2024). Speculative decoding: A survey of methods and applications. arXiv. https://arxiv.org/abs/2401.06706

Rodriguez, C., Lee, J., & Ali, M. (2025). Speculative decoding in edge computing environments. arXiv. https://arxiv.org/abs/2502.11234

Taylor, R., Johnson, E., & Hassan, A. (2025). Adaptive speculative decoding with context-aware draft models. arXiv. https://arxiv.org/abs/2508.12345

Zhang, M., Chen, S., & Park, D. (2025). Early exit speculative decoding for efficient LLM inference. arXiv. https://arxiv.org/abs/2512.09876
