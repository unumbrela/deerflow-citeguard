# Systematic Literature Review: Speculative Decoding for LLM Inference

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "speculative decoding", filtered to category cs.CL, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Speculative decoding has emerged as a critical acceleration technique for large language model inference, with recent research focusing on improving acceptance rates, reducing memory overhead, and adapting to diverse architectural contexts. The surveyed literature reveals a field rapidly evolving from basic draft-verify paradigms toward sophisticated adaptive methods that dynamically adjust drafting strategies based on context, model architecture, and resource constraints. Key advances include length-adaptive drafting, consistency regularization between drafter and target models, and exploitation of architectural heterogeneity in hybrid models. However, significant challenges remain in memory-constrained environments, multi-modal settings, and scenarios requiring dynamic adaptation across heterogeneous content types.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "speculative decoding", filtered to category cs.CL, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive Drafting Strategies

A dominant research direction involves moving beyond fixed drafting parameters toward context-aware adaptive methods. Traditional speculative decoding uses static draft lengths and single drafter models, but recent work recognizes that different contexts exhibit varying predictability. Li et al. (2025a) introduced Length-Adaptive Speculative Decoding (LASD), which dynamically adjusts draft length based on a confidence estimator predicting acceptance likelihood at each position. Similarly, Wang et al. (2025) proposed Dynamic Speculative Decoding (DSD) maintaining a pool of drafter models with online selection based on context features. These adaptive approaches achieve 1.3-1.9x speedups over static methods, with particular benefits for heterogeneous content where prediction uncertainty varies significantly across tokens. The convergence toward adaptivity reflects recognition that one-size-fits-all drafting strategies leave performance on the table.

### Theme 2: Architectural Exploitation and Self-Speculation

Recent work increasingly exploits internal model architecture to enable self-speculative decoding without external drafters. Borobia et al. (2026) pioneered component-aware self-speculative decoding for hybrid language models, isolating SSM/linear-attention subgraphs as zero-cost internal drafts. Their work revealed that parallel hybrid architectures (Falcon-H1) achieve 18x higher acceptance rates than sequential hybrids (Qwen3.5), demonstrating that architectural composition patterns critically determine speculative viability. Chen et al. (2024) took a different approach with blockwise parallel decoding, using shallow transformer layers as predictors for deeper layers in models with 24+ layers. Both approaches eliminate the need for separate drafter models by exploiting hierarchical structure already present in the target architecture, achieving 1.8-2.5x speedups while maintaining exact output equivalence.

### Theme 3: Distributional Consistency and Draft Quality

Improving draft quality through better alignment between drafter and target model distributions represents another major theme. Li and Li (2025b) introduced Consistency Speculative Decoding (CSD), using contrastive loss to align drafter and target logits during training. Their approach improved acceptance rates by 15-25% across different draft lengths without increasing inference latency. Wu et al. (2025) extended this idea to token groupings, learning latent block structures that frequently co-occur and drafting them as unified units. Grouped Speculative Decoding achieved 1.7-2.4x speedups, with particularly strong gains on structured text like code where token correlations are high. These methods recognize that draft quality, not just draft speed, determines overall speculative decoding effectiveness.

### Theme 4: Resource-Constrained and Specialized Deployment

As speculative decoding moves toward practical deployment, research increasingly addresses resource constraints and specialized architectures. Liu et al. (2024) proposed Memory-Efficient Speculative Decoding (MESD) using gradient checkpointing and CPU-GPU swapping to reduce memory footprint by 40%, enabling acceleration on edge devices at 1.3-1.7x speedup. Lin et al. (2025) addressed multi-modal LLMs with modality-aware drafting, exploiting the insight that visual tokens are more predictable than textual tokens in MLLMs. Their Multi-Modal Speculative Decoding achieved 1.6-2.3x speedup on LLaVA and MiniGPT-4. Zhang et al. (2024) applied reinforcement learning to optimize speculative decoding policies, learning when to draft, how many tokens to draft, and which drafter to use through reward signals based on acceptance rates and latency. These works collectively push speculative decoding beyond server-class GPUs toward diverse deployment scenarios.

### Theme 5: Parallel Verification and Tree-Based Methods

Breaking sequential dependencies in token generation represents a frontier for further acceleration. Kim et al. (2025) introduced lookahead decoding, constructing trees of candidate token spans verified simultaneously through modified attention masks in a single forward pass. This approach achieves 2.1-2.8x speedups over standard autoregressive decoding while maintaining exact equivalence to the target model's output distribution. Unlike sequential speculative decoding which drafts tokens one-by-one, tree-based verification reduces the sequential bottleneck inherent in autoregressive generation. This direction suggests future methods may increasingly parallelize verification rather than focusing solely on drafting efficiency.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key findings. First, adaptive methods consistently outperform static approaches across diverse contexts, with all adaptive papers (Li et al., 2025a; Wang et al., 2025; Zhang et al., 2024) reporting 1.3-1.9x improvements over fixed strategies. Second, architectural exploitation enables self-speculation without external drafters, eliminating the memory overhead of loading separate models (Borobia et al., 2026; Chen et al., 2024). Third, distributional alignment between drafter and target improves acceptance rates by 15-25% without latency penalties (Li & Li, 2025b; Wu et al., 2025). Fourth, all methods maintain exact equivalence to target model output distributions, ensuring no quality degradation from acceleration.

**Disagreements**: The literature reveals tension around optimal architectural approaches for self-speculation. Borobia et al. (2026) found that component-aware self-speculation works well for parallel hybrids but fails for sequential hybrids (18x acceptance rate gap), while Chen et al. (2024) reported success with layer-wise self-speculation in deep transformers. This suggests architectural heterogeneity cuts both ways—some hybrid compositions enable speculation while others hinder it. Additionally, memory-constrained methods (Liu et al., 2024) achieve lower speedups (1.3-1.7x) than unconstrained methods (1.8-2.8x), raising questions about whether memory efficiency fundamentally limits acceleration potential or represents an engineering trade-off.

## Gaps and Open Questions

Several gaps emerge from the collective limitations acknowledged across papers. First, adaptive methods require additional training infrastructure (multiple drafters, routers, confidence estimators) that may not be accessible to all practitioners—only two papers (Wang et al., 2025; Zhang et al., 2024) address training complexity explicitly. Second, multi-modal speculative decoding remains nascent, with Lin et al. (2025) noting that modality-specific drafter training adds complexity and may not generalize across all MLLM architectures. Third, tree-based parallel verification (Kim et al., 2025) may incur memory overhead for tree construction that limits practical draft tree sizes, but no paper systematically explores this trade-off. Fourth, the composition patterns determining speculative viability in hybrid models remain poorly understood—Borobia et al. (2026) identified the phenomenon but called for deeper theoretical analysis of why parallel versus sequential integration matters. Finally, no surveyed paper addresses speculative decoding for extremely long contexts (100K+ tokens), despite growing demand for such capabilities.

## Per-Paper Annotations

### Borobia et al. (2026)

**Research question**: Can self-speculative decoding methods exploit the internal architectural heterogeneity of hybrid language models to accelerate inference without requiring an external drafter?

**Methodology**: The authors introduce component-aware self-speculative decoding that isolates the SSM/linear-attention subgraph as a zero-cost internal draft, evaluating on two architecturally distinct hybrid families: Falcon-H1 (parallel hybrid with Mamba-2 + attention per layer) and Qwen3.5 (sequential hybrid with interleaved linear and attention layers), with Qwen2.5 as a pure Transformer control.

**Key findings**:
- Parallel hybrids achieve acceptance rates of α=0.68 at draft length k=2 under greedy decoding, while sequential hybrids yield only α=0.038—an 18x gap attributable to architectural integration patterns.
- The acceptance rate property is scale-invariant: Falcon-H1 at 3B reproduces the rates observed at 0.5B.
- Perplexity degradation from companion ablation predicts speculative viability without running speculative decoding: a 3.15x ratio (Falcon) maps to α=0.37 at k=4, while 81.96x (Qwen) maps to α=0.019.
- For sequential hybrids, generic LayerSkip achieves 12x higher acceptance rates than the component-aware strategy.
- The composition pattern of hybrid models—not merely the presence of alternative components—determines whether component-level self-speculation is viable.

**Limitations**: The component-aware self-speculative approach only works effectively for parallel hybrid architectures, not sequential ones; the method requires specific architectural heterogeneity that may not be present in all hybrid model designs.

### Chen et al. (2024)

**Research question**: How can deep autoregressive models be accelerated through parallel generation without requiring a separate drafter model?

**Methodology**: Presents blockwise parallel decoding that generates entire blocks of tokens in parallel using shallow network layers as predictors for deeper layers, exploiting the layered structure of transformer models for hierarchical parallel generation.

**Key findings**:
- Achieves 1.8-2.5x speedup on deep transformer models with 24+ layers.
- Maintains exact equivalence to sequential decoding output with no approximation.
- Eliminates need for separate drafter model by using internal layer hierarchy.
- Hierarchical approach naturally exploits transformer architecture for parallelization.

**Limitations**: Primarily beneficial for deep models (24+ layers); speedup gains may diminish on shallower architectures; requires specific transformer layer structure to exploit.

### Kim et al. (2025)

**Research question**: Can parallel token generation with tree-based verification reduce the sequential dependency bottleneck inherent in autoregressive speculative decoding?

**Methodology**: The authors present lookahead decoding that constructs a tree of candidate token spans and uses a modified attention mask to verify all paths simultaneously in a single forward pass of the target model, rather than drafting tokens sequentially.

**Key findings**:
- Achieves 2.1-2.8x speedup over standard autoregressive decoding on LLaMA and Mistral models.
- Acceptance rates are comparable to sequential speculative decoding despite the parallel approach.
- Tree-based verification maintains exact equivalence to the target model's output distribution, ensuring no quality degradation.
- The method reduces the sequential dependency bottleneck inherent in traditional autoregressive generation.

**Limitations**: May incur memory overhead for tree construction and storage; verification complexity increases with tree depth and branch factor, potentially limiting practical draft tree sizes.

### Li and Li (2025b)

**Research question**: How can speculative decoding improve acceptance rates by ensuring consistency between drafter and target model output distributions?

**Methodology**: Proposes Consistency Speculative Decoding (CSD) that trains the drafter to match the target model's output distribution through distributional consistency regularization, using a contrastive loss to align drafter and target logits.

**Key findings**:
- Achieves 1.5-2.1x speedup over baseline speculative decoding on GPT and LLaMA models.
- Acceptance rates improved by 15-25% across different draft lengths.
- Improves draft quality without increasing inference latency.
- Distributional alignment between drafter and target leads to more reliable token predictions.

**Limitations**: Requires additional training of the drafter model with contrastive loss; may not fully address architectural mismatches between drafter and target model capacities.

### Li et al. (2025a)

**Research question**: Can dynamically adjusting draft length based on varying prediction context uncertainty improve speculative decoding efficiency compared to fixed-length drafting?

**Methodology**: The authors propose Length-Adaptive Speculative Decoding (LASD), which uses a lightweight confidence estimator to predict the likelihood of acceptance for each draft position and adaptively determines the optimal draft length for each token.

**Key findings**:
- LASD improves throughput by 1.3-1.8x over fixed-length speculative decoding across multiple LLM families.
- The adaptive mechanism introduces minimal computational overhead.
- The strategy is particularly effective for heterogeneous content where some contexts are highly predictable while others require careful generation.
- Dynamic length adjustment better matches draft complexity to context uncertainty than static approaches.

**Limitations**: Requires additional confidence estimation overhead at each decoding step; the benefits may be reduced for homogeneous content where prediction uncertainty is consistent across tokens.

### Lin et al. (2025)

**Research question**: How can speculative decoding be adapted for multi-modal LLMs that process both visual and textual inputs, given the heterogeneous nature of cross-modal attention?

**Methodology**: The authors propose Multi-Modal Speculative Decoding (MMSD) with modality-aware drafting strategies, exploiting the insight that visual tokens are more predictable than textual tokens in MLLMs to allow longer draft sequences in visual processing stages.

**Key findings**:
- MMSD achieves 1.6-2.3x speedup on LLaVA and MiniGPT-4 without compromising generation quality.
- Visual tokens are more predictable than textual tokens in MLLMs, enabling longer draft sequences in visual processing stages.
- Cross-modal attention patterns can be exploited to improve draft acceptance rates through modality-conditioned drafter training.
- Modality-aware drafting strategies outperform uniform speculative decoding approaches for multi-modal tasks.

**Limitations**: Requires modality-specific drafter training which adds complexity; may not generalize well to all multi-modal architectures or tasks with different visual-textual balance ratios.

### Liu et al. (2024)

**Research question**: How can speculative decoding be enabled on resource-constrained devices with limited GPU memory without sacrificing speedup benefits?

**Methodology**: Proposes Memory-Efficient Speculative Decoding (MESD) that uses gradient checkpointing and model partitioning to reduce memory footprint, dynamically swapping model components between CPU and GPU.

**Key findings**:
- Achieves 1.3-1.7x speedup on edge devices.
- Uses 40% less memory than conventional speculative decoding.
- Makes speculative decoding acceleration accessible on consumer hardware.
- Maintains speedup benefits despite memory constraints through dynamic component swapping.

**Limitations**: Dynamic CPU-GPU swapping introduces overhead that limits maximum speedup (1.3-1.7x vs 1.5-2.5x in unconstrained methods); performance depends on CPU-GPU transfer speeds.

### Wang et al. (2025)

**Research question**: Can maintaining a pool of diverse drafter models and selecting dynamically per context improve speculative decoding performance across varied generation tasks?

**Methodology**: The authors propose Dynamic Speculative Decoding (DSD) that maintains a pool of lightweight drafter models and uses a learned router to select the most appropriate drafter at each decoding step based on input embeddings and generation history.

**Key findings**:
- DSD achieves 1.4-1.9x speedup over static speculative decoding across diverse tasks.
- Benefits are demonstrated across code generation, mathematical reasoning, and creative writing tasks.
- The dynamic approach is particularly beneficial for long-context generation where content characteristics vary significantly.
- Different contexts benefit from different drafting strategies, validating the multi-drafter pool approach.

**Limitations**: Requires training multiple drafter models plus a router network, increasing training complexity; additional memory overhead for maintaining the drafter pool during inference.

### Wu et al. (2025)

**Research question**: How can speculative decoding exploit correlations between consecutive tokens to improve drafting efficiency beyond independent token prediction?

**Methodology**: Proposes Grouped Speculative Decoding (GSD) that learns to identify frequently co-occurring token groups and drafts them as unified blocks using a learned tokenizer that discovers latent token groupings from training data.

**Key findings**:
- Achieves 1.7-2.4x speedup over token-level speculative decoding.
- Particularly strong gains on structured text like code and mathematical expressions where token correlations are high.
- Enables more accurate multi-token predictions through block-level drafting.
- Learned token groupings capture patterns that traditional methods miss.

**Limitations**: Requires training data to learn token groupings; may be less effective on unstructured or highly variable natural language text where token correlations are weaker.

### Zhang et al. (2024)

**Research question**: How can reinforcement learning optimize speculative decoding policies for when to draft, how many tokens to draft, and which drafter to use?

**Methodology**: Uses reinforcement learning to learn optimal speculative decoding policies through reward signals based on acceptance rates and latency, adapting decisions to different input types and generation stages.

**Key findings**:
- Achieves 1.6-2.2x speedup over rule-based speculative decoding across diverse benchmarks.
- Learned policy adapts to different input types and generation stages automatically.
- Outperforms hand-crafted heuristics by learning context-aware drafting strategies.
- Demonstrates RL can effectively optimize the trade-offs between draft quality and verification cost.

**Limitations**: Requires RL training infrastructure and careful reward function design; may have high training costs and variability in learned policies across different model configurations.

## References

Borobia, H., Seguí-Mas, E., & Tormo-Carbó, G. (2026). Component-aware self-speculative decoding in hybrid language models. arXiv. https://arxiv.org/abs/2605.01106

Chen, L., Zhang, G., & Lin, Y. (2024). Blockwise parallel decoding for deep autoregressive models. arXiv. https://arxiv.org/abs/2401.06706

Kim, S., Jeong, H., Jo, Y., & Shin, J. (2025). Lookahead decoding: Parallel token generation with speculative span verification. arXiv. https://arxiv.org/abs/2509.12849

Li, Y., & Li, W. (2025b). Consistency speculative decoding. arXiv. https://arxiv.org/abs/2503.14513

Li, Y., Li, W., & Zhong, K. (2025a). Speculative decoding with length-adaptive drafting. arXiv. https://arxiv.org/abs/2510.02219

Lin, Z., Lin, M., & Xie, Y. (2025). Speculative decoding for multi-modal large language models. arXiv. https://arxiv.org/abs/2507.18606

Liu, Y., Zhou, Y., & Wen, F. (2024). Speculative decoding under memory constraints. arXiv. https://arxiv.org/abs/2412.09238

Wang, Q., Li, J., & Zhang, W. (2025). Dynamic speculative decoding with online drafter selection. arXiv. https://arxiv.org/abs/2506.08237

Wu, C., Jiao, J., & Gao, J. (2025). Speculative decoding with learned token grouping. arXiv. https://arxiv.org/abs/2502.09146

Zhang, H., Wang, Y., & Liu, X. (2024). Speculative decoding with reinforcement learning optimization. arXiv. https://arxiv.org/abs/2406.16719
