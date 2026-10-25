# Systematic Literature Review: Speculative Decoding for LLM Inference

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: "speculative decoding", cs.CL category, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Speculative decoding has emerged as a critical acceleration technique for large language model (LLM) inference, with recent research focusing on diverse approaches to improve draft token generation and acceptance rates. The surveyed literature reveals a field rapidly evolving along multiple axes: architectural innovations (hybrid models, multi-model pyramids), parallel generation strategies (block diffusion), quantization techniques, and adaptive verification mechanisms. While most approaches report substantial speedups ranging from 1.91x to over 6x, emerging concerns about fairness across tasks, multilingual limitations, and security vulnerabilities highlight the technique's immaturity. The collective literature demonstrates that speculative decoding is not a monolithic solution but rather a design space requiring careful consideration of model architecture, task characteristics, and deployment constraints.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "speculative decoding", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Innovations in Draft Model Design

Recent work has moved beyond the traditional small-draft, large-target paradigm to explore more sophisticated architectural arrangements. Borobia et al. (2026) investigate component-aware self-speculative decoding in hybrid language models, exploiting internal architectural heterogeneity by isolating SSM/linear-attention subgraphs as zero-cost internal drafts. Their work reveals that parallel hybrids (Falcon-H1) achieve acceptance rates of α=0.68 at k=2, while sequential hybrids (Qwen3.5) yield only α=0.038—an 18x gap determined by composition patterns rather than mere component presence.

Byun et al. (2025) introduce Pyramid Speculative Decoding (PyramidSD), inserting an intermediate qualifier model between draft and target to bridge distributional gaps. This three-model architecture achieves up to 1.91x generation speed over standard speculative decoding and reaches 124 tokens per second on consumer GPUs. The hierarchical decoding strategy with fuzzy acceptance criteria enables the use of significantly smaller draft models without sacrificing performance, addressing the fundamental trade-off between draft model size and token acceptance.

### Theme 2: Parallel Drafting with Block Diffusion

A significant departure from sequential drafting has emerged through diffusion-based approaches. Chen et al. (2026) introduce DFlash, employing a lightweight block diffusion model for parallel drafting that generates draft tokens in a single forward pass. This approach achieves over 6x lossless acceleration across models and tasks, delivering up to 2.5x higher speedup than the state-of-the-art EAGLE-3 method.

Building on DFlash, Ringel and Romano (2026) propose DDTree (Diffusion Draft Tree), which constructs draft trees directly from per-position distributions of a block diffusion drafter. Their best-first heap algorithm under fixed node budget selects continuations most likely to match the target model, verified efficiently with ancestor-only attention mask. This work addresses DFlash's limitation of verifying only a single drafted trajectory per round, positioning DDTree among leading speculative decoding approaches.

### Theme 3: Adaptive Verification and Looped Decoding

As draft models become increasingly capable, traditional per-stage verification becomes inefficient. Gu et al. (2026) propose DLoop, a looped form of speculative decoding that adaptively performs multiple drafting stages before verification. When target models frequently accept all tokens from capable draft models, DLoop reduces unnecessary target-model forward passes by continuing drafting while the draft model remains confident and verifying all accumulated tokens together.

DLoop improves wall-clock speedup by 5% to 41% across diverse speculative decoding methods including EAGLE-3, DFlash, Domino, DSpark, and multi-token prediction, while preserving lossless decoding. The loop-aware training exposes the draft model to its own hidden states for unverified draft tokens, maintaining reliability across multiple drafting stages.

### Theme 4: Quantization and Plug-and-Play Draft Models

Practical deployment concerns have motivated research into quantization-based approaches that eliminate the need for separate draft model training. Georganas et al. (2025) propose ML-SpecQD, using MXFP4 Weight-Only-Quantized models as plug-and-play drafts since MXFP4 merely direct-casts BF16 target model weights. This approach recursively applies speculation for accelerating draft-token generation through multi-level speculative decoding.

The quantization approach achieves speedups up to 2x over BF16 baseline for the plug-and-play solution, while multi-level speculative decoding with quantized drafts yields speedups up to 2.72x. This method outperforms state-of-the-art speculative decoding techniques without requiring pre-training or alignment, addressing a key practical barrier to adoption.

### Theme 5: Retrieval Augmentation and Hybrid Approaches

Integration with retrieval mechanisms has emerged as a strategy to enhance speculative decoding effectiveness, particularly in out-of-domain scenarios. Quan et al. (2025) propose RASD (Retrieval-Augmented Speculative Decoding), introducing tree pruning based on the draft model's probability distribution and tree fusion using longest prefix matching to merge draft model trees with retrieval trees.

RASD achieves state-of-the-art inference acceleration across DocQA, Summary, Code, and In-Domain QA tasks, exhibiting strong scalability by seamlessly integrating with both generation-based and retrieval-based speculative decoding methods. This approach addresses the limitation that model-based speculative decoding frequently becomes less effective in out-of-domain scenarios due to draft model size and limited training data.

### Theme 6: Fairness, Multilinguality, and Security Concerns

As speculative decoding matures, researchers have begun examining its broader implications beyond raw acceleration. Sandler et al. (2025) analyze speculative decoding through the lens of disparate speed-up rates across tasks, finding that speed-up is not uniformly distributed and consistently diminishes for under-fit and often underrepresented tasks. Their mitigation strategy achieves on average a 12% improvement in fairness metrics across several model pairs.

Paudel et al. (2026) examine multilingual limitations, testing eleven languages under standard speculative decoding setups. They find speculative decoding is far less effective for low-resource languages due to limited multilingual capacities of smaller draft models. Distillation generalizes poorly across tasks in the same language, and weaker n-gram models as draft alternatives provide only moderate speed-ups due to their minuscule inference cost.

Security concerns emerge in Sun et al. (2026), who propose Mistletoe, a stealthy attack exploiting drafter-target mismatch as a hidden attack surface. The attack jointly optimizes a degradation objective to decrease drafter-target agreement and a semantic-preservation objective using null-space projection. Mistletoe substantially reduces average accepted length τ, collapses speedup, and lowers token throughput while preserving output quality and perplexity, revealing a mechanism-level attack surface beyond existing output robustness.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key findings. First, all papers demonstrate that speculative decoding can achieve substantial acceleration, with reported speedups ranging from 1.91x to over 6x depending on the approach. Second, there is consensus that the traditional small-draft, large-target paradigm is evolving toward more sophisticated architectures, whether through multi-model arrangements (Byun et al., 2025), architectural exploitation (Borobia et al., 2026), or quantization strategies (Georganas et al., 2025). Third, parallel drafting through diffusion models represents a promising direction, with both Chen et al. (2026) and Ringel and Romano (2026) reporting superior performance over sequential approaches.

**Disagreements**: The literature reveals tensions regarding optimal draft model design. While Borobia et al. (2026) find that component-aware self-speculation works well for parallel hybrids but poorly for sequential ones, Byun et al. (2025) demonstrate that intermediate qualifier models can bridge distributional gaps regardless of architecture. Additionally, Paudel et al. (2026) find distillation ineffective for multilingual scenarios, contrasting with the general assumption in other papers that model alignment is achievable. The security analysis by Sun et al. (2026) challenges the field's focus on acceleration without considering adversarial vulnerabilities.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly discuss limitations in their abstracts, suggesting either limited self-reflection or space constraints—a concerning pattern for a rapidly deploying technology. Second, while multiple papers address multilingual and fairness concerns (Paudel et al., 2026; Sandler et al., 2025), the proposed solutions remain modest (n-gram models, 12% fairness improvements), indicating the field lacks fundamental approaches to these challenges.

Third, the security vulnerability identified by Sun et al. (2026) raises questions about the robustness of speculative decoding in production environments, yet no paper proposes defensive mechanisms. Fourth, the reliance on arXiv preprints means many techniques lack peer review and real-world deployment validation. Finally, the focus on speedup metrics may obscure other important considerations such as energy efficiency, memory footprint, and integration costs with existing inference pipelines.

## Per-Paper Annotations

### Borobia et al. (2026)

**Research question**: Can self-speculative decoding be adapted to exploit the internal architectural heterogeneity of hybrid language models?

**Methodology**: The authors introduce component-aware self-speculative decoding that isolates the SSM/linear-attention subgraph as a zero-cost internal draft, then evaluate it on two hybrid families (Falcon-H1 and Qwen3.5) compared to a pure Transformer control.

**Key findings**:
- Parallel hybrids (Falcon-H1) achieve acceptance rates of α=0.68 at k=2, while sequential hybrids (Qwen3.5) yield only α=0.038—an 18x gap
- The property is scale-invariant: Falcon-H1 at 3B reproduces the rates observed at 0.5B
- Perplexity degradation from companion ablation predicts speculative viability without running speculative decoding
- For sequential hybrids, generic LayerSkip achieves 12x higher acceptance rates than the component-aware strategy
- The composition pattern of hybrid models—not merely the presence of alternative components—determines whether component-level self-speculation is viable

**Limitations**: Not stated in abstract

### Byun et al. (2025)

**Research question**: How can the throughput limitations of speculative decoding caused by the trade-off between draft model size and token acceptance be overcome?

**Methodology**: Introduces Pyramid Speculative Decoding (PyramidSD) that inserts an intermediate qualifier model between draft and target to bridge distributional gaps. Uses fuzzy acceptance criteria and hierarchical decoding strategy to improve alignment across models.

**Key findings**:
- Achieves up to 1.91x generation speed over standard speculative decoding
- Reaches 124 tokens per second on a consumer GPU (RTX 4090)
- Enables use of significantly smaller draft models without sacrificing overall performance
- In small-memory settings with 1B-parameter draft and 8B target model, minimally trades target model quality for improved throughput
- Can be readily applied to existing inference pipelines

**Limitations**: Not stated in abstract

### Chen et al. (2026)

**Research question**: How can the sequential drafting bottleneck in speculative decoding be addressed using parallel generation capabilities of diffusion models?

**Methodology**: Introduces DFlash, a speculative decoding framework that employs a lightweight block diffusion model for parallel drafting. Generates draft tokens in a single forward pass while conditioning on context features extracted from the target model.

**Key findings**:
- Achieves over 6x lossless acceleration across a range of models and tasks
- Delivers up to 2.5x higher speedup than the state-of-the-art EAGLE-3 method
- Block diffusion model enables parallel drafting with high-quality outputs and higher acceptance rates
- Generates draft tokens in a single forward pass, eliminating sequential drafting limitations

**Limitations**: Not stated in abstract

### Georganas et al. (2025)

**Research question**: How can speculative decoding be made more practical and efficient without requiring pre-training and alignment of draft models to target models?

**Methodology**: Proposes using MXFP4 Weight-Only-Quantized models as plug-and-play drafts since MXFP4 merely direct-casts BF16 target model weights. Recursively applies speculation for accelerating draft-token generation through Multi-Level Speculative Decoding with Quantized Drafts.

**Key findings**:
- MXFP4 quantization provides plug-and-play solution without requiring pre-training or alignment
- Plug-and-play solution achieves speedups up to 2x over BF16 baseline
- Multi-level speculative decoding with quantized drafts yields speedups up to 2.72x over BF16 baseline
- Outperforms state-of-the-art speculative decoding methods

**Limitations**: Not stated in abstract

### Gu et al. (2026)

**Research question**: How can speculative decoding be improved when draft models are increasingly capable and the target model frequently accepts all draft tokens, making per-stage verification unnecessary?

**Methodology**: Proposes DLoop, a looped form of speculative decoding that adaptively performs multiple drafting stages before verification. Uses loop-aware training that exposes the draft model to its own hidden states for unverified draft tokens to maintain reliability.

**Key findings**:
- Target models frequently accept all tokens from capable draft models, resulting in unnecessary target-model forward passes with traditional verification
- DLoop reduces target-model forward passes by continuing drafting while the draft model remains confident and verifying all accumulated tokens together
- Improves wall-clock speedup by 5 to 41 percent across diverse speculative decoding methods including EAGLE-3, DFlash, Domino, DSpark, and multi-token prediction
- Preserves lossless decoding while improving efficiency

**Limitations**: Not stated in abstract

### Paudel et al. (2026)

**Research question**: Is speculative decoding less effective for low-resource languages due to the limited multilingual capacities of smaller draft models?

**Methodology**: The authors test eleven languages under a standard speculative decoding setup, then attempt to improve multilingual capabilities via distillation from the larger model, and finally propose weaker n-gram models as draft alternatives.

**Key findings**:
- Speculative decoding is far less effective for low-resource languages due to limited multilingual capacities of smaller models
- Distillation generalizes poorly across tasks in the same language
- Assembling a task-agnostic, fully representative dataset is infeasible for low-resource languages
- Weaker n-gram models as draft models provide moderate speed-ups due to their minuscule inference cost

**Limitations**: Not stated in abstract

### Quan et al. (2025)

**Research question**: How can retrieval methods enhance model-based speculative decoding to improve effectiveness in out-of-domain scenarios?

**Methodology**: The authors propose RASD, which introduces tree pruning based on the draft model's probability distribution and tree fusion using longest prefix matching to merge the draft model tree with a retrieval tree.

**Key findings**:
- RASD achieves state-of-the-art inference acceleration across DocQA, Summary, Code, and In-Domain QA tasks
- Model-based speculative decoding frequently becomes less effective in out-of-domain scenarios due to draft model size and limited training data
- The time cost of the drafting phase results in a low upper limit on acceptance length during verification
- RASD exhibits strong scalability, seamlessly integrating with both generation-based and retrieval-based speculative decoding methods

**Limitations**: Not stated in abstract

### Ringel and Romano (2026)

**Research question**: How can DFlash's acceptance length be improved beyond verifying only a single drafted trajectory per round?

**Methodology**: Introduces DDTree (Diffusion Draft Tree) that constructs a draft tree directly from per-position distributions of a block diffusion drafter. Uses a best-first heap algorithm under fixed node budget to select continuations most likely to match the target model, verified efficiently with ancestor-only attention mask.

**Key findings**:
- Constructs draft trees directly from block diffusion drafter's per-position distributions
- Uses ancestor-only attention mask for efficient single target model forward pass verification
- Best-first heap algorithm selects continuations most likely to match target model according to draft model surrogate
- Builds on DFlash to place DDTree among leading approaches to speculative decoding

**Limitations**: Not stated in abstract

### Sandler et al. (2025)

**Research question**: Does speculative decoding produce disparate speed-up rates across different tasks, and what factors drive this unfairness?

**Methodology**: The authors analyze speculative decoding through the lens of disparate speed-up rates across tasks, derive an analysis to quantify the observed unfairness, and propose a mitigation strategy validated across several model pairs.

**Key findings**:
- Speed-up from speculative decoding is not uniformly distributed across tasks
- Speed-up consistently diminishes for under-fit and often underrepresented tasks
- The authors derive an analysis quantifying the factors motivating disparate speed-ups
- The proposed mitigation strategy achieves on average a 12% improvement in the fairness metric across several model pairs

**Limitations**: Not stated in abstract

### Sun et al. (2026)

**Research question**: Can the drafter-target mismatch in speculative decoding be exploited as a hidden attack surface to reduce draft-token acceptability while preserving target model behavior?

**Methodology**: The authors propose Mistletoe, a stealthy attack that jointly optimizes a degradation objective to decrease drafter-target agreement and a semantic-preservation objective, using null-space projection to resolve conflicts between these objectives.

**Key findings**:
- Drafter-target approximation mismatch creates a hidden attack surface where small perturbations can reduce draft-token acceptability
- Mistletoe directly targets the acceptance mechanism of speculative decoding
- Null-space projection suppresses draft acceptance while minimizing semantic drift
- Mistletoe substantially reduces average accepted length τ, collapses speedup, and lowers token throughput while preserving output quality and perplexity
- Speculative decoding introduces a mechanism-level attack surface beyond existing output robustness

**Limitations**: Not stated in abstract

## References

Borobia, H., Seguí-Mas, E., & Tormo-Carbó, G. (2026). Component-aware self-speculative decoding in hybrid language models. arXiv. https://arxiv.org/abs/2605.01106

Byun, S., Odema, M., Guack, J. I., Lee, B., Song, J., & Chung, W. S. (2025). 3-model speculative decoding. arXiv. https://arxiv.org/abs/2510.12966

Chen, J., Liang, Y., & Liu, Z. (2026). DFlash: Block diffusion for flash speculative decoding. arXiv. https://arxiv.org/abs/2602.06036

Georganas, E., Kalamkar, D., Kozlov, A., & Heinecke, A. (2025). ML-SpecQD: Multi-level speculative decoding with quantized drafts. arXiv. https://arxiv.org/abs/2503.13565

Gu, G., Heo, B., Jun, H., Kang, Y., Lee, S., Yun, S., & Han, D. (2026). DLoop: Looped speculative decoding. arXiv. https://arxiv.org/abs/2610.07659

Paudel, N., Ginn, M., De Nardi, L., & Palmer, A. (2026). Speculative decoding and the curse of multilinguality. arXiv. https://arxiv.org/abs/2605.30580

Quan, G., Feng, W., Hao, C., Jiang, G., Zhang, Y., & Wang, H. (2025). RASD: Retrieval-augmented speculative decoding. arXiv. https://arxiv.org/abs/2503.03434

Ringel, L., & Romano, Y. (2026). Accelerating speculative decoding with block diffusion draft trees. arXiv. https://arxiv.org/abs/2604.12989

Sandler, J., Üstün, A., Romanelli, M., Hooker, S., & Fioretto, F. (2025). The disparate impacts of speculative decoding. arXiv. https://arxiv.org/abs/2510.02128

Sun, S., Dai, C., Fang, H., Gao, K., Zhong, X., Sun, Y., Mo, F., Xia, S.-T., & Chen, B. (2026). Mistletoe: Stealthy acceleration-collapse attacks on speculative decoding. arXiv. https://arxiv.org/abs/2605.14005
