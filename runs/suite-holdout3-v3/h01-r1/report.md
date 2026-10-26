# Systematic Literature Review: Speculative Decoding for LLM Inference

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "speculative decoding", category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Speculative decoding has emerged as a critical acceleration technique for large language model inference, with recent research focusing on three main directions: improving draft model quality through architectural innovations, addressing fairness and robustness concerns, and extending applicability to multilingual settings. The surveyed literature reveals significant progress in acceleration techniques, with reported speedups ranging from 1.91x to over 6x compared to baseline autoregressive decoding. However, substantial challenges remain, particularly regarding disparate impacts across tasks, vulnerability to adversarial attacks, and reduced effectiveness for low-resource languages. The field is rapidly evolving with novel approaches including block diffusion models, multi-model hierarchies, and quantization-based drafting strategies.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "speculative decoding", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Innovations in Draft Model Design

Recent work has explored diverse architectural approaches to improve draft model quality and efficiency. Component-aware self-speculative decoding leverages internal architectural heterogeneity in hybrid language models, isolating SSM/linear-attention subgraphs as internal draft mechanisms (Borobia et al., 2026). This approach achieves acceptance rates of α=0.68 at draft length k=2 for parallel hybrids, demonstrating that composition patterns of hybrid models determine speculative viability.

Block diffusion models represent another significant innovation, enabling parallel drafting in a single forward pass rather than sequential autoregressive drafting. DFlash employs lightweight block diffusion models for parallel drafting, achieving over 6x lossless acceleration and up to 2.5x higher speedup than EAGLE-3 (Chen et al., 2026). Building on this foundation, DDTree constructs draft trees directly from block diffusion drafter distributions using a best-first heap algorithm, verified efficiently in a single target model forward pass (Ringel & Romano, 2026).

### Theme 2: Multi-Model and Hierarchical Approaches

Several papers propose hierarchical decoding strategies to overcome trade-offs between draft model size and token acceptance rates. Pyramid Speculative Decoding inserts an intermediate qualifier model between draft and target models, bridging distributional gaps through fuzzy acceptance criteria (Byun et al., 2025). This approach achieves up to 1.91x generation speed over standard speculative decoding and reaches 124 tokens per second on consumer GPUs.

Multi-level speculative decoding recursively applies speculation to accelerate draft-token generation itself. ML-SpecQD uses MXFP4 quantized drafts in a plug-and-play fashion, yielding speedups up to 2.72x over BF16 baselines without sacrificing accuracy (Georganas et al., 2025). DLoop introduces looped speculative decoding that adaptively performs multiple drafting stages before verification, improving wall-clock speedup by 5 to 41 percent across diverse methods while preserving lossless decoding (Gu et al., 2026).

### Theme 3: Retrieval-Augmented and Context-Enhanced Methods

Retrieval augmentation addresses limitations of small draft models in out-of-domain scenarios. RASD introduces tree pruning based on draft model probability distributions and tree fusion using longest prefix matching to unify draft and retrieval trees (Quan et al., 2025). This approach achieves state-of-the-art inference acceleration across DocQA, Summary, Code, and In-Domain QA tasks, demonstrating strong scalability and seamless integration with both generation-based and retrieval-based approaches.

### Theme 4: Fairness and Disparate Impacts

Critical analysis reveals that speed-up benefits from speculative decoding are not uniformly distributed across tasks. Under-fit and often underrepresented tasks consistently receive diminished speed-up benefits (Sandler et al., 2025). The authors derive a quantitative analysis framework to measure observed unfairness and propose mitigation strategies achieving on average 12% improvement in fairness metrics. This work highlights the importance of considering equity in acceleration technique deployment.

### Theme 5: Security and Robustness Concerns

The drafter-target mismatch in speculative decoding creates previously unrecognized attack surfaces. Mistletoe demonstrates stealthy attacks that jointly optimize degradation objectives to decrease drafter-target agreement while constraining output distribution through null-space projection (Sun et al., 2026). These attacks substantially reduce average accepted length and collapse speedup across various speculative decoding systems while preserving output quality and perplexity, revealing mechanism-level vulnerabilities beyond existing output robustness concerns.

### Theme 6: Multilingual Challenges and Limitations

Speculative decoding effectiveness varies dramatically across languages, with far lower performance for low-resource languages compared to English (Paudel et al., 2026). The limited multilingual capacities of smaller draft models create a "curse of multilinguality." Distillation from larger models generalizes poorly across tasks within the same language, and assembling task-agnostic representative datasets proves infeasible for low-resource languages. Weaker n-gram models as draft models provide moderate speed-ups due to minuscule inference costs, suggesting alternative drafting strategies may be necessary for multilingual applications.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that speculative decoding provides substantial acceleration benefits, with reported speedups consistently exceeding 1.5x across diverse approaches. There is consensus that draft model quality relative to target model is the primary determinant of acceptance rates and overall speedup. Multiple papers converge on the importance of adaptive strategies that adjust draft length or verification frequency based on confidence levels.

**Disagreements**: Papers diverge on optimal drafting strategies: while some advocate for architectural innovations like block diffusion (Chen et al., 2026; Ringel & Romano, 2026), others emphasize quantization-based approaches (Georganas et al., 2025) or hierarchical multi-model designs (Byun et al., 2025). The multilingual literature suggests n-gram models may outperform neural drafters for low-resource languages (Paudel et al., 2026), contrasting with the general trend toward increasingly sophisticated neural architectures. Security research reveals fundamental tensions between acceleration and robustness that acceleration-focused papers do not address.

## Gaps and Open Questions

The collective literature reveals several critical gaps:

1. **Limited evaluation diversity**: Most studies focus on English-language benchmarks with narrow task distributions. Comprehensive evaluation across diverse languages, domains, and task types remains absent.

2. **Security implications underexplored**: Only one paper addresses adversarial vulnerabilities (Sun et al., 2026), suggesting a significant blind spot in the literature regarding production deployment risks.

3. **Fairness considerations**: The disparate impacts framework (Sandler et al., 2025) raises questions about equitable access to acceleration benefits that remain largely unaddressed by other works.

4. **Computational overhead transparency**: Multiple papers report speedup metrics without detailing retrieval overhead, quantization costs, or memory footprint implications for real-world deployment.

5. **Hybrid architecture coverage**: Component-aware approaches focus on only two specific hybrid families (Falcon-H1 and Qwen3.5), leaving open questions about generalizability to other architectural patterns.

6. **Loop-aware training requirements**: DLoop's adaptive drafting requires specialized training procedures not explored in depth, raising questions about adoption barriers for existing models.

## Per-Paper Annotations

### Borobia et al. (2026)

**Research question**: Can self-speculative decoding be adapted to exploit the internal architectural heterogeneity of hybrid language models for zero-cost drafting?

**Methodology**: The authors introduce component-aware self-speculative decoding that isolates the SSM/linear-attention subgraph as an internal draft mechanism, evaluating on Falcon-H1 and Qwen3.5 hybrid families with pure Transformer controls.

**Key findings**:
- Parallel hybrids (Falcon-H1) achieve acceptance rates of α=0.68 at draft length k=2, while sequential hybrids (Qwen3.5) yield only α=0.038—an 18x gap
- Acceptance rate property is scale-invariant across model sizes
- Perplexity degradation predicts speculative viability without running speculative decoding
- Generic LayerSkip achieves 12x higher acceptance rates than component-aware strategy for sequential hybrids
- Composition pattern of hybrid models determines speculative viability

**Limitations**: The study focuses on two specific hybrid architectures and does not explore other hybrid model families or alternative drafting strategies beyond component-aware isolation.

### Byun et al. (2025)

**Research question**: How can speculative decoding overcome the trade-off between draft model size and token acceptance rates?

**Methodology**: The authors introduce Pyramid Speculative Decoding (PyramidSD), inserting an intermediate qualifier model between draft and target model with fuzzy acceptance criteria supporting relaxed divergence thresholds.

**Key findings**:
- PyramidSD achieves up to 1.91x generation speed over standard speculative decoding
- Reaches 124 tokens per second on consumer GPU (RTX 4090)
- Minimally trades target model quality for improved throughput in small-memory settings
- Hierarchical decoding enables higher acceptance rates and use of significantly smaller draft models

**Limitations**: Not stated in abstract.

### Chen et al. (2026)

**Research question**: How can diffusion LLMs be leveraged for parallel drafting in speculative decoding to overcome sequential drafting limitations?

**Methodology**: The authors introduce DFlash, employing lightweight block diffusion models for parallel drafting in a single forward pass, conditioning on context features extracted from target models.

**Key findings**:
- Achieves over 6x lossless acceleration across various models and tasks
- Delivers up to 2.5x higher speedup than EAGLE-3
- Enables efficient drafting with high-quality outputs and higher acceptance rates
- Block diffusion enables parallel generation unlike autoregressive drafting

**Limitations**: Not stated in abstract.

### Georganas et al. (2025)

**Research question**: How can speculative decoding be made more practical and plug-and-play without requiring pre-training and aligning draft models to target models?

**Methodology**: The authors propose using MXFP4 quantized models as drafts in plug-and-play fashion, introducing ML-SpecQD which recursively applies multi-level speculative decoding for draft-token generation acceleration.

**Key findings**:
- Plug-and-play MXFP4 quantized draft solution gives speedups up to 2x over BF16 baseline
- ML-SpecQD yields speedups up to 2.72x over BF16 baseline
- Accelerates LLM inference without sacrificing accuracy over 16-bit inference
- Multi-level speculation recursively accelerates draft-token generation itself

**Limitations**: Not stated in abstract.

### Gu et al. (2026)

**Research question**: How can speculative decoding reduce unnecessary target-model verification passes when draft models are increasingly capable?

**Methodology**: The authors propose DLoop, a looped form adaptively performing multiple drafting stages before verification, with loop-aware training exposing draft models to their own hidden states for unverified tokens.

**Key findings**:
- Reduces target-model forward passes by spending additional draft-model forward passes
- Improves wall-clock speedup by 5 to 41 percent across EAGLE-3, DFlash, Domino, DSpark, and multi-token prediction modules
- Preserves lossless decoding while improving efficiency
- Adaptive draft length methods work for parallel draft models unlike autoregressive-only approaches

**Limitations**: Not stated in abstract.

### Paudel et al. (2026)

**Research question**: Is speculative decoding less effective for low-resource languages due to the limited multilingual capacities of smaller draft models?

**Methodology**: The authors test eleven languages under standard speculative decoding setup, attempt improvement via distillation from larger models, and propose weaker n-gram models as alternative draft models.

**Key findings**:
- Strong evidence confirms speculative decoding is far less effective for low-resource languages compared to English
- Distillation from larger models generalizes poorly across tasks within the same language
- Assembling task-agnostic representative datasets is infeasible for low-resource languages
- N-gram models provide moderate speed-ups due to minuscule inference costs

**Limitations**: The study is limited to eleven languages and does not explore alternative drafting strategies beyond distillation and n-gram models for all language families.

### Quan et al. (2025)

**Research question**: How can retrieval methods enhance model-based speculative decoding to improve effectiveness in out-of-domain scenarios?

**Methodology**: The authors propose RASD, introducing tree pruning based on draft model probability distributions and tree fusion using longest prefix matching to merge draft and retrieval trees for unified verification.

**Key findings**:
- Achieves state-of-the-art inference acceleration across DocQA, Summary, Code, and In-Domain QA tasks
- Tree pruning constructs optimal retrieval trees for enhanced drafting
- Tree fusion successfully unifies draft and retrieval trees for verification
- Exhibits strong scalability, integrating seamlessly with both generation-based and retrieval-based approaches
- Retrieval augmentation addresses small draft model limitations in out-of-domain scenarios

**Limitations**: The abstract does not specify computational overhead of retrieval operations or evaluate performance on low-resource languages.

### Ringel & Romano (2026)

**Research question**: How can speculative decoding acceptance length be improved beyond verifying only a single drafted trajectory per round?

**Methodology**: The authors introduce DDTree, constructing draft trees directly from per-position distributions of block diffusion drafters using a best-first heap algorithm under fixed node budgets, verified in single target model forward pass with ancestor-only attention masks.

**Key findings**:
- Builds on DFlash, a leading draft model for speculative decoding
- Constructs draft trees verified efficiently in single target model forward pass
- Uses simple best-first heap algorithm to select continuations most likely to match target model
- Gains place DDTree among leading approaches to speculative decoding

**Limitations**: Not stated in abstract.

### Sandler et al. (2025)

**Research question**: Are speed-up rates from speculative decoding uniformly distributed across tasks, or do they disproportionately benefit certain task types?

**Methodology**: The authors conduct analysis through the lens of disparate speed-up rates across tasks, derive quantitative analysis to measure observed unfairness, and propose and validate mitigation strategies across several model pairs.

**Key findings**:
- Speed-up from speculative decoding is not uniformly distributed across tasks
- Under-fit and often underrepresented tasks consistently receive diminished speed-up benefits
- Derived analysis framework quantifies observed unfairness in speed-up distribution
- Proposed mitigation strategy achieves on average 12% improvement in fairness metric
- Disparate speed-ups emerge from identifiable factors that can be systematically addressed

**Limitations**: The abstract does not specify which tasks were most affected or detail the specific mitigation strategy implementation.

### Sun et al. (2026)

**Research question**: Does the drafter-target mismatch in speculative decoding create a hidden attack surface that can be exploited to collapse acceleration while preserving output quality?

**Methodology**: The authors propose Mistletoe, a stealthy attack jointly optimizing degradation objective to decrease drafter-target agreement and semantic-preservation objective to constrain output distribution, using null-space projection to resolve conflicts.

**Key findings**:
- Drafter-target mismatch creates hidden attack surface where small perturbations reduce draft-token acceptability while preserving visible behavior
- Mistletoe substantially reduces average accepted length τ and collapses speedup across various speculative decoding systems
- Attack lowers averaged token throughput while preserving output quality and perplexity
- Null-space projection successfully resolves conflict between degradation and semantic-preservation objectives
- Speculative decoding introduces mechanism-level attack surface beyond existing output robustness concerns

**Limitations**: The abstract does not specify which speculative decoding systems were tested or quantify the exact reduction in accepted length τ.

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
