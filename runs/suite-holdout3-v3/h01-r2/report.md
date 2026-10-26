# Systematic Literature Review: Speculative Decoding for LLM Inference

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "speculative decoding", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in speculative decoding for large language model (LLM) inference, a critical technique for accelerating text generation while preserving output quality. The 10 surveyed papers reveal a rapidly evolving field addressing multiple dimensions: architectural innovations (hybrid models, multi-model hierarchies), novel drafting mechanisms (diffusion-based, retrieval-augmented, quantized drafts), and critical examinations of speculative decoding's limitations (multilingual performance, fairness across tasks, security vulnerabilities). Collectively, the literature demonstrates that speculative decoding has matured beyond simple draft-verify paradigms into sophisticated systems achieving 2-6x speedups through adaptive drafting strategies, block-level parallelism, and multi-level speculation. However, significant challenges remain in ensuring equitable performance across languages and tasks, defending against adversarial attacks, and generalizing acceleration techniques to diverse model architectures.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "speculative decoding", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Innovations in Draft-Verify Systems

Recent work has moved beyond the traditional single draft-single target model paradigm to explore more sophisticated architectural configurations. Component-aware self-speculative decoding exploits internal heterogeneity in hybrid language models, using SSM/linear-attention subgraphs as zero-cost internal drafts (Borobia et al., 2026). However, this approach's effectiveness depends critically on composition patterns: parallel hybrids achieve 18x higher acceptance rates than sequential hybrids, demonstrating that architectural arrangement matters more than component presence alone.

Pyramid Speculative Decoding introduces an intermediate qualifier model between draft and target, creating a three-tier hierarchy that bridges distributional gaps through fuzzy acceptance criteria (Byun et al., 2025). This hierarchical strategy enables significantly smaller draft models while maintaining high acceptance rates, achieving 1.91x speedup over standard speculative decoding. Similarly, DLoop proposes looped speculative decoding that adaptively performs multiple drafting stages before verification, reducing target-model forward passes by 5-41% across diverse methods (Gu et al., 2026).

These architectural innovations share a common insight: the draft-target mismatch is the fundamental bottleneck, and reducing this gap through intermediate representations, adaptive drafting, or internal component exploitation yields substantial acceleration without quality degradation.

### Theme 2: Parallel Drafting via Diffusion Models

A major breakthrough in speculative decoding addresses the sequential drafting bottleneck through diffusion-based parallel token generation. DFlash introduces block diffusion models that generate draft tokens in a single forward pass while conditioning on context features from the target model, achieving over 6x lossless acceleration and 2.5x higher speedup than EAGLE-3 (Chen et al., 2026). This approach fundamentally challenges the assumption that drafting must be sequential, demonstrating that parallel generation can maintain high acceptance rates.

Building on DFlash, DDTree extends block diffusion drafters beyond single trajectory verification by constructing draft trees using a best-first heap algorithm (Ringel & Romano, 2026). The method selects continuations most likely to match the target model under fixed node budgets, verified efficiently in a single forward pass using ancestor-only attention masks. This tree-based approach increases acceptance length while preserving the parallel drafting advantage, positioning itself among leading speculative decoding approaches.

The convergence on diffusion-based drafting across multiple papers suggests this represents a paradigm shift: parallel drafting is not only feasible but superior to sequential approaches when properly implemented with block-level conditioning and tree-based verification.

### Theme 3: Retrieval and Quantization for Plug-and-Play Acceleration

Making speculative decoding practical without requiring extensive pre-training or model alignment has emerged as a critical research direction. RASD integrates retrieval methods with model-based speculative decoding, using tree pruning based on draft model probability distributions and tree fusion via longest prefix matching (Quan et al., 2025). This retrieval augmentation addresses the ineffectiveness of small draft models in out-of-domain scenarios, achieving state-of-the-art acceleration across DocQA, Summary, Code, and In-Domain QA tasks.

ML-SpecQD takes a different approach, using MXFP4 Weight-Only-Quantization models as drafts in a plug-and-play manner, recursively applying speculative decoding to accelerate draft-token generation itself (Georganas et al., 2025). By directly casting BF16 target model weights to MXFP4 without pre-training, this method eliminates draft model alignment requirements while achieving up to 2.72x speedup over BF16 baseline. The multi-level recursive speculation—applying speculation to the drafting process itself—represents a novel meta-acceleration strategy.

Both approaches share the goal of democratizing speculative decoding: making high-performance acceleration accessible without requiring custom draft model training or extensive alignment procedures.

### Theme 4: The Curse of Multilinguality and Fairness Concerns

Critical examinations of speculative decoding reveal significant disparities in performance across languages and tasks. Strong evidence supports that speculative decoding is far less effective for low-resource languages due to limited multilingual capacities of smaller draft models (Paudel et al., 2026). Distillation from larger models generalizes poorly across tasks within the same language, and assembling task-agnostic, representative datasets for low-resource languages proves infeasible. Weaker n-gram models provide moderate speed-ups due to minuscule inference costs but cannot fully address the multilingual gap.

Similarly, speed-up from speculative decoding is not uniformly distributed across tasks, consistently diminishing for under-fit and underrepresented tasks (Sandler et al., 2025). An analytical framework quantifies this unfairness, and a mitigation strategy achieves on average 12% improvement in fairness metrics. The disparate impacts emerge from identifiable factors related to draft model training distributions and task representation.

These papers collectively sound an important caution: speculative decoding's acceleration benefits are not equitably distributed, and addressing this requires intentional intervention in draft model training, task balancing, and fairness-aware optimization.

### Theme 5: Security Vulnerabilities in Speculative Decoding

The drafter-target mismatch that speculative decoding relies upon creates a previously unrecognized attack surface. Mistletoe demonstrates stealthy acceleration-collapse attacks that directly target the acceptance mechanism, jointly optimizing degradation objectives to decrease drafter-target agreement while constraining output distribution through null-space projection (Sun et al., 2026). The attack substantially reduces average accepted length and collapses speedup across various speculative decoding systems while preserving output quality and perplexity, making it difficult to detect.

This work reveals that speculative decoding introduces mechanism-level security vulnerabilities beyond existing output robustness concerns. The attack exploits the fundamental architectural assumption—that drafter and target distributions align sufficiently for efficient verification—by introducing perturbations invisible at the output level but catastrophic at the acceptance mechanism level. This represents a critical challenge for deploying speculative decoding in security-sensitive applications.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that the draft-target distributional mismatch is the fundamental bottleneck limiting speculative decoding efficiency. Multiple approaches—architectural hierarchies (Byun et al., 2025), adaptive looping (Gu et al., 2026), diffusion-based parallel drafting (Chen et al., 2026; Ringel & Romano, 2026), and retrieval augmentation (Quan et al., 2025)—converge on reducing this gap as the primary optimization target. There is also consensus that speculative decoding can achieve 2-6x lossless acceleration when properly implemented, with diffusion-based approaches representing the current state-of-the-art.

**Disagreements**: Papers diverge on whether architectural complexity or architectural simplicity better serves speculative decoding. Component-aware approaches exploit internal model heterogeneity (Borobia et al., 2026), while quantization-based approaches treat models as black boxes (Georganas et al., 2025). Similarly, while diffusion-based drafting shows superior raw performance, questions remain about training costs and deployment complexity compared to simpler quantization or retrieval approaches. The security implications identified by Sun et al. (2026) also raise questions about whether the acceleration benefits justify the introduced vulnerabilities in certain deployment contexts.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature:

1. **Generalization across architectures**: Multiple studies focus on specific model families (hybrid models, diffusion models) without addressing whether findings generalize to other architectural variants or training regimes (Borobia et al., 2026; Chen et al., 2026).

2. **Quantitative fairness metrics**: While fairness disparities are identified (Sandler et al., 2025; Paudel et al., 2026), the abstracts do not specify the exact fairness metrics used, specific tasks tested, or detailed per-language performance metrics, limiting reproducibility and comparison.

3. **Computational overhead**: Multiple papers do not specify computational overhead introduced by their innovations—retrieval components (Quan et al., 2025), diffusion model training (Chen et al., 2026), multi-level recursion (Georganas et al., 2025), or additional drafting stages (Gu et al., 2026)—making it difficult to assess net efficiency gains.

4. **Defense mechanisms**: The security vulnerabilities identified by Sun et al. (2026) are not accompanied by proposed defenses, leaving a critical gap in understanding how to protect speculative decoding systems from acceleration-collapse attacks.

5. **Quality-accuracy trade-offs**: While most papers claim "lossless" acceleration, several note minimal trade-offs with target model quality (Byun et al., 2025) or do not address potential accuracy impacts of quantization (Georganas et al., 2025), suggesting incomplete characterization of quality degradation.

6. **Task-specific performance**: Limited analysis exists comparing performance across different task types, with most evaluations focusing on aggregate metrics rather than task-specific breakdowns beyond broad categories like DocQA or Code (Quan et al., 2025; Chen et al., 2026).

## Per-Paper Annotations

### Borobia et al. (2026)

**Research question**: Can self-speculative decoding be adapted to exploit the internal architectural heterogeneity of hybrid language models?

**Methodology**: The authors introduce component-aware self-speculative decoding, which isolates the SSM/linear-attention subgraph as a zero-cost internal draft. They evaluate this approach on two architecturally distinct hybrid families (Falcon-H1 and Qwen3.5) and compare against a pure Transformer control (Qwen2.5), measuring acceptance rates under greedy decoding at various draft lengths.

**Key findings**:
- Parallel hybrids (Falcon-H1) achieve acceptance rates of α = 0.68 at draft length k=2, while sequential hybrids (Qwen3.5) yield only α = 0.038—an 18x gap.
- The acceptance rate property is scale-invariant: Falcon-H1 at 3B reproduces the rates observed at 0.5B.
- Perplexity degradation from companion ablation predicts speculative viability: a 3.15x ratio maps to α = 0.37 at k=4, while 81.96x maps to α = 0.019.
- For sequential hybrids, generic LayerSkip achieves 12x higher acceptance rates than the component-aware strategy.
- The composition pattern of hybrid models—not merely the presence of alternative components—determines whether component-level self-speculation is viable.

**Limitations**: The study focuses on specific hybrid model families and does not address whether the findings generalize to other architectural variants or training regimes.

### Byun et al. (2025)

**Research question**: How can speculative decoding overcome the trade-off between draft model size and token acceptance rates?

**Methodology**: The authors introduce Pyramid Speculative Decoding (PyramidSD), which inserts an intermediate qualifier model between draft and target models to bridge distributional gaps, using fuzzy acceptance criteria and relaxed divergence thresholds at each stage.

**Key findings**:
- PyramidSD achieves up to 1.91x generation speed over standard speculative decoding.
- The method reaches 124 tokens per second on a consumer GPU (RTX 4090).
- In small-memory settings with 1B draft and 8B target models, PyramidSD minimally trades target model quality for improved throughput.
- The hierarchical strategy enables higher acceptance rates and allows significantly smaller draft models.

**Limitations**: The abstract notes a minimal trade-off with target model quality in small-memory settings, but does not quantify this degradation.

### Chen et al. (2026)

**Research question**: Can diffusion LLMs enable parallel drafting in speculative decoding to overcome sequential drafting limitations?

**Methodology**: The authors introduce DFlash, a speculative decoding framework employing a lightweight block diffusion model for parallel drafting that generates draft tokens in a single forward pass while conditioning on context features from the target model.

**Key findings**:
- DFlash achieves over 6x lossless acceleration across various models and tasks.
- The method delivers up to 2.5x higher speedup than state-of-the-art EAGLE-3.
- Block diffusion enables parallel token generation with high-quality outputs and higher acceptance rates.
- The approach mitigates sequential decoding bottlenecks while maintaining target model performance.

**Limitations**: The abstract does not discuss training requirements for the diffusion model or compare performance across different task types.

### Georganas et al. (2025)

**Research question**: Can speculative decoding be made practical in a plug-and-play fashion without requiring pre-training and alignment of draft models?

**Methodology**: The authors propose ML-SpecQD, which uses MXFP4 Weight-Only-Quantization models as drafts in a plug-and-play manner, recursively applying speculative decoding to accelerate draft-token generation itself through multi-level speculation.

**Key findings**:
- The plug-and-play MXFP4 quantization approach gives speedups up to 2x over BF16 baseline.
- Multi-Level Speculative Decoding with MXFP4 Quantized Drafts yields speedups up to 2.72x over BF16 baseline.
- The method outperforms state-of-the-art speculative decoding approaches.
- MXFP4 quantization merely direct-casts BF16 target model weights, eliminating need for draft model pre-training.

**Limitations**: The abstract does not address potential accuracy impacts of quantization or computational costs of multi-level recursive speculation.

### Gu et al. (2026)

**Research question**: How can speculative decoding reduce unnecessary target-model forward passes when draft models frequently produce fully accepted tokens?

**Methodology**: The authors propose DLoop, a looped speculative decoding approach that adaptively performs multiple drafting stages before verification, combined with loop-aware training that exposes the draft model to its own hidden states for unverified tokens.

**Key findings**:
- DLoop reduces target-model forward passes by continuing drafting while the draft model remains confident.
- DLoop improves wall-clock speedup by 5 to 41 percent across diverse speculative decoding methods including EAGLE-3, DFlash, Domino, DSpark, and multi-token prediction modules.
- The approach preserves lossless decoding while reducing verification overhead.
- Loop-aware training maintains draft model reliability across additional drafting stages.

**Limitations**: The abstract does not specify computational overhead costs or memory requirements for the additional drafting stages.

### Paudel et al. (2026)

**Research question**: Is speculative decoding less effective for low-resource languages due to the limited multilingual capacities of smaller draft models?

**Methodology**: The authors test eleven languages under a standard speculative decoding setup to evaluate the hypothesis. They attempt to improve multilingual capabilities via distillation from larger models and propose using weaker n-gram models as draft models as an alternative approach.

**Key findings**:
- Strong evidence supports the hypothesis that speculative decoding is far less effective for low-resource languages.
- Distillation from larger models generalizes poorly across tasks within the same language.
- Assembling a task-agnostic, fully representative dataset for low-resource languages is infeasible.
- Weaker n-gram models as draft models provide moderate speed-ups due to their minuscule inference cost.
- The curse of multilinguality significantly impacts the effectiveness of speculative decoding across different languages.

**Limitations**: The study covers eleven languages but does not specify which languages were tested or provide detailed per-language performance metrics in the abstract.

### Quan et al. (2025)

**Research question**: How can retrieval methods be integrated to enhance model-based speculative decoding and overcome limitations in out-of-domain scenarios?

**Methodology**: The authors propose RASD, which combines retrieval methods with model-based speculative decoding using tree pruning and tree fusion. They develop a pruning method based on the draft model's probability distribution to construct an optimal retrieval tree, and employ longest prefix matching to merge the draft model tree with the retrieval tree into a unified verification tree.

**Key findings**:
- RASD achieves state-of-the-art inference acceleration across DocQA, Summary, Code, and In-Domain QA tasks.
- Tree pruning based on draft model probability distributions enables construction of optimal retrieval trees.
- Tree fusion via longest prefix matching successfully merges draft and retrieval trees for unified verification.
- RASD exhibits strong scalability, integrating seamlessly with both generation-based and retrieval-based speculative decoding approaches.
- Retrieval augmentation addresses the ineffectiveness of small draft models in out-of-domain scenarios.

**Limitations**: The abstract does not specify computational overhead introduced by the retrieval component or compare latency trade-offs against baseline methods.

### Ringel and Romano (2026)

**Research question**: How can block diffusion drafters be extended beyond single trajectory verification to increase acceptance length in speculative decoding?

**Methodology**: The authors introduce DDTree (Diffusion Draft Tree), which constructs a draft tree from per-position distributions of a block diffusion drafter using a best-first heap algorithm to select continuations most likely to match the target model, verified efficiently with ancestor-only attention masks.

**Key findings**:
- DDTree builds on DFlash, a leading draft model for speculative decoding.
- The method constructs draft trees directly from block diffusion drafter distributions.
- A simple best-first heap algorithm selects optimal continuations under fixed node budgets.
- The resulting tree is verified in a single target model forward pass using ancestor-only attention masks.
- DDTree places itself among leading approaches to speculative decoding.

**Limitations**: The abstract does not provide quantitative speedup metrics or compare acceptance length improvements over vanilla DFlash.

### Sandler et al. (2025)

**Research question**: Does speculative decoding produce disparate speed-up rates across different tasks, and what factors drive this unfairness?

**Methodology**: The authors conduct an analysis of speculative decoding through the lens of disparate speed-up rates across tasks, derive an analytical framework to quantify observed unfairness, and propose a mitigation strategy designed to reduce speed-up disparities, validating the approach across several model pairs.

**Key findings**:
- Speed-up from speculative decoding is not uniformly distributed across tasks.
- Speed-up consistently diminishes for under-fit and often underrepresented tasks.
- The derived analysis successfully quantifies the observed unfairness in speed-up distribution.
- The proposed mitigation strategy achieves on average a 12% improvement in the fairness metric.
- Disparate speed-ups emerge from identifiable factors that can be addressed through targeted interventions.

**Limitations**: The abstract does not specify the fairness metric used, the specific tasks tested, or the model pairs evaluated in the validation.

### Sun et al. (2026)

**Research question**: Can the drafter-target mismatch in speculative decoding be exploited to create stealthy attacks that collapse acceleration while preserving output quality?

**Methodology**: The authors propose Mistletoe, a stealthy attack that directly targets the acceptance mechanism of speculative decoding. The attack jointly optimizes a degradation objective to decrease drafter-target agreement and a semantic-preservation objective to constrain output distribution, using null-space projection to resolve conflicts between these objectives.

**Key findings**:
- Drafter-target mismatch creates a hidden attack surface where small perturbations can reduce draft-token acceptability while preserving visible behavior.
- Mistletoe substantially reduces average accepted length τ and collapses speedup in various speculative decoding systems.
- The attack lowers averaged token throughput while preserving output quality and perplexity.
- Null-space projection successfully suppresses draft acceptance by projecting degradation gradients away from semantic-preserving directions.
- Speculative decoding introduces a mechanism-level attack surface beyond existing output robustness concerns.

**Limitations**: The abstract does not specify the computational cost of mounting the attack or whether defenses against Mistletoe were explored.

## References

Borobia, H., Seguí-Mas, E., & Tormo-Carbó, G. (2026). Component-aware self-speculative decoding in hybrid language models. arXiv. https://arxiv.org/abs/2605.01106

Byun, S., Odema, M., Guack, J. I., Lee, B., Song, J., & Chung, W. S. (2025). 3-Model speculative decoding. arXiv. https://arxiv.org/abs/2510.12966

Chen, J., Liang, Y., & Liu, Z. (2026). DFlash: Block diffusion for flash speculative decoding. arXiv. https://arxiv.org/abs/2602.06036

Georganas, E., Kalamkar, D., Kozlov, A., & Heinecke, A. (2025). ML-SpecQD: Multi-level speculative decoding with quantized drafts. arXiv. https://arxiv.org/abs/2503.13565

Gu, G., Heo, B., Jun, H., Kang, Y., Lee, S., Yun, S., & Han, D. (2026). DLoop: Looped speculative decoding. arXiv. https://arxiv.org/abs/2610.07659

Paudel, N., Ginn, M., De Nardi, L., & Palmer, A. (2026). Speculative decoding and the curse of multilinguality. arXiv. https://arxiv.org/abs/2605.30580

Quan, G., Feng, W., Hao, C., Jiang, G., Zhang, Y., & Wang, H. (2025). RASD: Retrieval-augmented speculative decoding. arXiv. https://arxiv.org/abs/2503.03434

Ringel, L., & Romano, Y. (2026). Accelerating speculative decoding with block diffusion draft trees. arXiv. https://arxiv.org/abs/2604.12989

Sandler, J., Üstün, A., Romanelli, M., Hooker, S., & Fioretto, F. (2025). The disparate impacts of speculative decoding. arXiv. https://arxiv.org/abs/2510.02128

Sun, S., Dai, C., Fang, H., Gao, K., Zhong, X., Sun, Y., Mo, F., Xia, S.-T., & Chen, B. (2026). Mistletoe: Stealthy acceleration-collapse attacks on speculative decoding. arXiv. https://arxiv.org/abs/2605.14005
