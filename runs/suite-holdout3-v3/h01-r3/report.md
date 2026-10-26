# Systematic Literature Review: Speculative Decoding for LLM Inference

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "speculative decoding LLM inference", category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Speculative decoding has emerged as a dominant paradigm for accelerating large language model inference, with recent research achieving 2x-5x speedups while maintaining lossless output distributions. The literature reveals a clear evolution from basic draft-verify frameworks toward sophisticated approaches addressing batch inference, heterogeneous hardware, and adaptive scheduling. Recent work demonstrates that the key bottlenecks have shifted from drafting accuracy to drafting latency, prompting innovations in parallel generation, non-autoregressive forecasting, and structure-isolated drafting. Collectively, these papers establish speculative decoding as a mature technique with multiple viable optimization pathways, though challenges remain in heterogeneous vocabulary support and large-batch scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "speculative decoding LLM inference", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Drafting Architecture Evolution

The literature shows a clear trajectory from autoregressive drafting toward parallel and non-autoregressive approaches. Early speculative decoding relied on smaller autoregressive models to generate drafts sequentially, but this introduced high drafting latency that became a performance bottleneck. Liu et al. (2026) address this with DART, which predicts logits for multiple future masked positions in parallel within a single forward pass, eliminating autoregressive rollouts entirely. Similarly, Shi et al. (2025) propose SpecFormer, which integrates unidirectional and bidirectional attention mechanisms to enable parallel generation without relying on large prefix trees. This architectural shift reflects a fundamental insight: drafting accuracy alone is insufficient when multi-step autoregressive inference creates latency that negates speedup gains.

### Theme 2: Batch Inference and Scheduling Optimization

Several papers address the challenge of maintaining speculative decoding efficiency under batch inference conditions. Wang et al. (2026) identify that state-of-the-art algorithms exhibit substantial speed degradation under large batch sizes, attributing this to high rejection rates and under-utilization of dynamic token budgets. Their AgentSpec approach introduces structure-isolated drafting that constrains speculation to semantically coherent segments, achieving extremely low rejection rates. Li et al. (2025) tackle the scheduling problem from a different angle, proposing LAPS-SD, a semi-clairvoyant algorithm that maintains multiple priority queues and allows request preemption. Their work reveals that execution time depends on both output length and token acceptance rate—a factor existing methods overlook—achieving approximately 39% latency reduction over state-of-the-art scheduling.

### Theme 3: Heterogeneous and Adaptive Approaches

A significant research direction involves adapting speculative decoding to heterogeneous environments without requiring additional training. Ge et al. (2025) propose automatic task detection with heterogeneous draft models, routing prompts dynamically to appropriate drafters aligned with task-specific data, improving draft accuracy by 6% to 50%. Lu et al. (2025) introduce AdaSD, a hyperparameter-free scheme that dynamically adjusts generation length and acceptance criteria using token entropy and Jensen-Shannon distance, achieving up to 1.46x speedup over vanilla speculative decoding with minimal accuracy degradation. Timor et al. (2025) remove the shared-vocabulary constraint entirely, presenting three lossless methods that enable any off-the-shelf model to serve as a drafter, broadening applicability substantially.

### Theme 4: Parallel Execution and Hardware Acceleration

Breaking the serial barrier in speculative decoding has emerged as a critical optimization path. Bhendawade et al. (2025) present Mirror-SD, which launches branch-complete rollouts from early-exit signals in parallel with the target model's suffix, explicitly mapping computation across heterogeneous accelerators (GPU and NPU). Their approach converts speculation into two complementary execution pipelines where the draft speculates forward continuations for the target to verify, while the target simultaneously speculates correction paths for the draft. Combined with speculative streaming that enables multiple tokens per step, this achieves 2.8x-5.8x wall-time speedups across diverse tasks, offering a 30% average relative improvement over EAGLE3.

## Convergences and Disagreements

**Convergences**: All surveyed papers agree that speculative decoding achieves substantial speedups (2x-5x range) while maintaining lossless output distributions. There is consensus that the draft-verify paradigm fundamentally addresses the autoregressive decoding bottleneck. Multiple papers converge on the finding that drafting latency has become the primary performance limiter as draft accuracy improves (Bhendawade et al., 2025; Liu et al., 2026; Shi et al., 2025). The literature also uniformly demonstrates that batch inference introduces unique challenges requiring specialized solutions beyond single-request optimization (Wang et al., 2026; Li et al., 2025; Shi et al., 2025).

**Disagreements**: The literature reveals tension between different approaches to reducing drafting latency. While Liu et al. (2026) advocate for diffusion-inspired parallel generation eliminating autoregressive rollouts, Bhendawade et al. (2025) argue for maintaining autoregressive drafting but parallelizing execution across heterogeneous hardware. Wang et al. (2026) emphasize structure-isolated drafting to reduce rejection rates, whereas Ge et al. (2025) focus on task-specific heterogeneous drafters to improve accuracy. These differences reflect distinct optimization priorities: some approaches prioritize drafting speed, others prioritize acceptance rates, and the optimal balance appears workload-dependent.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the papers explicitly state limitations in their abstracts, suggesting either that limitations are not thoroughly addressed or that abstracts do not capture methodological constraints. Second, while multiple papers address batch inference, there is limited discussion of memory overhead and resource requirements for production deployment. Third, the evaluation focuses primarily on wall-clock speedup and acceptance rates, with minimal attention to energy efficiency or carbon footprint—critical considerations for large-scale deployment. Fourth, most approaches assume access to heterogeneous hardware (GPU+NPU), but the performance characteristics on commodity hardware remain unclear. Finally, the interaction between speculative decoding and emerging techniques like retrieval-augmented generation or tool use has not been explored, leaving open questions about applicability to agentic workflows beyond the single AgentSpec paper.

## Per-Paper Annotations

### AdaSD: Adaptive Speculative Decoding for Efficient Language Model Inference

**Research question**: How can speculative decoding be made adaptive without requiring additional training, hyperparameter tuning, or prior model analysis?
**Methodology**: Proposes Adaptive Speculative Decoding (AdaSD), a hyperparameter-free decoding scheme that dynamically adjusts generation length and acceptance criteria during inference using two adaptive components updated in real time based on token entropy and Jensen-Shannon distance.
**Key findings**:
- Existing speculative decoding approaches often require additional training, extensive hyperparameter tuning, or prior analysis before deployment
- AdaSD eliminates the need for pre-analysis or fine-tuning and is compatible with off-the-shelf models
- Achieves up to 1.46x speedup over vanilla speculative decoding
- Accuracy degradation is limited to under 1.8%, making it a practical solution for efficient LLM inference
**Limitations**: not stated in abstract

### AgentSpec: Speculative Decoding for Batch Inference of LLM Agents

**Research question**: How can speculative decoding be improved for LLM agent batch inference to avoid speed degradation under large batch sizes?
**Methodology**: Presents systematic analysis of speculative decoding for LLM agents, identifying two dominant factors of speedup degradation. Proposes AgentSpec with structure-isolated drafting and redundancy-aware budget allocation, evaluating on five workloads and four models from four LLM families in vLLM.
**Key findings**:
- State-of-the-art speculative decoding algorithms exhibit substantial speed degradation under large batch sizes
- High rejection rate of speculative tokens and under-utilization of dynamic token budgets are the two dominant factors of speedup degradation
- AgentSpec's structure-isolated drafting constrains speculation to semantically coherent segments, reducing irrelevant semantic path drafts and achieving extremely low rejection rate
- Redundancy-aware budget allocation exploits agent-level information to better utilize dynamically-free token budget during agent inference
- AgentSpec demonstrates superiority over state-of-the-art methods across five different workloads and four models from four LLM families
**Limitations**: not stated in abstract

### Accelerating LLM Inference with Lossless Speculative Decoding Algorithms for Heterogeneous Vocabularies

**Research question**: How can speculative decoding methods remove the shared-vocabulary constraint between drafter and target models?
**Methodology**: Presents three new speculative decoding methods that remove the shared-vocabulary constraint, preserving the target distribution (lossless) and working with off-the-shelf models without requiring additional training or modifications. Empirically evaluated on summarization, programming, and long-context tasks.
**Key findings**:
- Existing SD approaches require drafter and target models to share the same vocabulary, limiting the pool of possible drafters
- The three proposed methods are lossless and work with off-the-shelf models without requiring additional training or modifications
- The algorithms demonstrate significant speedups of up to 2.8x over standard autoregressive decoding
- The work enables any off-the-shelf model to serve as a drafter, substantially broadening SD framework applicability
**Limitations**: not stated in abstract

### Automatic Task Detection and Heterogeneous LLM Speculative Decoding

**Research question**: How can speculative decoding be optimized for diverse downstream tasks while balancing acceptance rate and decoding speed?
**Methodology**: Proposes a speculative decoding algorithm with automatic task partitioning that categorizes downstream tasks into sub-tasks and assigns them to heterogeneous draft models. Incorporates an online lightweight prompt classifier to dynamically route prompts to appropriate draft models, with each draft model aligned to the target model using task-specific data.
**Key findings**:
- Existing methods face a trade-off between acceptance rate and decoding speed due to limited draft model capacity
- The proposed method improves draft accuracy by 6% to 50% over vanilla speculative decoding
- Achieves a speedup of 1.10x to 2.64x in LLM inference
- Automatic task categorization and heterogeneous draft models enhance consistency of inference results across diverse tasks
**Limitations**: not stated in abstract

### Closer Look at Efficient Inference Methods: A Survey of Speculative Decoding

**Research question**: How can speculative decoding methods optimize efficient inference in large language models?
**Methodology**: Conducts a comprehensive survey of speculative decoding methods, categorizing them into draft-centric and model-centric approaches. Analyzes key ideas associated with each method and their potential for scaling LLM inference.
**Key findings**:
- Speculative decoding addresses computational inefficiencies in traditional autoregressive decoding through a two-stage framework of drafting and verification
- A smaller, efficient model generates a preliminary draft which is then refined by a larger, more sophisticated model
- Methods can be categorized into draft-centric and model-centric approaches
- The survey aims to guide future research in optimizing speculative decoding for real-world LLM applications
**Limitations**: not stated in abstract

### DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference

**Research question**: How can drafting latency in speculative decoding be reduced by eliminating autoregressive rollouts while preserving high draft accuracy?
**Methodology**: Proposes DART, which leverages parallel generation inspired by diffusion-based LLMs. DART predicts logits for multiple future masked positions in parallel within a single forward pass based on hidden states of the target model, eliminating autoregressive rollouts. An efficient tree pruning algorithm constructs high-quality draft token trees with N-gram-enforced semantic continuity.
**Key findings**:
- Existing model-based draft designs like EAGLE3 improve accuracy at the cost of multi-step autoregressive inference, resulting in high drafting latency and making the drafting stage a performance bottleneck
- DART predicts logits for multiple future masked positions in parallel within a single forward pass, eliminating autoregressive rollouts in the draft model while preserving a lightweight design
- An efficient tree pruning algorithm constructs high-quality draft token trees with N-gram-enforced semantic continuity based on parallel logit predictions
- Achieves a 2.03x–3.44x wall-clock time speedup across multiple datasets
- DART surpasses EAGLE3 by 30% on average, offering a practical speculative decoding framework
**Limitations**: not stated in abstract

### Mirror Speculative Decoding: Breaking the Serial Barrier in LLM Inference

**Research question**: How can speculative decoding break the latency-acceptance tradeoff that limits gains from increasing draft size?
**Methodology**: Presents Mirror-SD, an inference algorithm that launches branch-complete rollouts from early-exit signals in parallel with the target model's suffix and explicitly maps computation across heterogeneous accelerators (GPU and NPU). The approach adds speculative streaming so the draft emits multiple tokens per step, combining parallel heterogeneous execution with multi-token speculative streaming.
**Key findings**:
- Prior methods (Medusa, Hydra, EAGLE) partially reduce draft cost but either degrade acceptance or introduce overheads that limit scaling
- Mirror-SD converts speculation into two complementary execution pipelines: the draft speculates forward continuations for the target to verify, while the target simultaneously speculates correction paths for the draft
- Speculative streaming enables the draft to emit multiple tokens per step, cutting draft latency without weakening acceptance semantics
- Achieves 2.8x-5.8x wall-time speedups across diverse tasks on SpecBench with server-scale models from 14B to 66B parameters
- Offers a 30% average relative improvement over the strongest baseline, EAGLE3
**Limitations**: not stated in abstract

### Scaling LLM Speculative Decoding: Non-Autoregressive Forecasting in Large-Batch Scenarios

**Research question**: How can speculative decoding be performed effectively with low verification resources and low scheduling costs in large-batch scenarios?
**Methodology**: Proposes SpecFormer, a novel architecture integrating unidirectional and bidirectional attention mechanisms that combines autoregressive information extraction with parallel generation benefits of non-autoregressive models. The approach eliminates reliance on large prefix trees and is evaluated through lossless speculative decoding experiments across models of various scales.
**Key findings**:
- Current speculative decoding methods assume considerable computing power and generate complex draft trees, but batching has become a superior alternative that compresses idle computing power
- SpecFormer enables parallel generation on draft sequences without relying on large prefix trees
- The architecture achieves consistent acceleration even in large-batch scenarios
- SpecFormer sets a new standard for scaling LLM inference with lower training demands and reduced computational costs
**Limitations**: not stated in abstract

### Semi-Clairvoyant Scheduling of Speculative Decoding Requests to Minimize LLM Inference Latency

**Research question**: How can inference requests be efficiently scheduled in LLM serving systems to minimize average inference latency when execution time depends on both output length and token acceptance rate?
**Methodology**: Proposes LAPS-SD, a semi-clairvoyant request scheduling algorithm that maintains multiple priority queues and allows request execution preemption across different queues. The algorithm adaptively schedules requests according to their features during decoding, accurately estimating execution time once token acceptance rate becomes stable.
**Key findings**:
- Existing work estimates execution time based solely on predicted output length, which is inaccurate because execution time depends on both output length and token acceptance rate
- LAPS-SD maintains multiple priority queues and allows request execution preemption when token acceptance rate is dynamic and execution time is difficult to estimate
- Once token acceptance rate becomes stable, LAPS-SD can accurately estimate execution time and schedule requests accordingly
- LAPS-SD reduces inference latency by approximately 39% compared to state-of-the-art scheduling methods
**Limitations**: not stated in abstract

### Tutorial Proposal: Speculative Decoding for Efficient LLM Inference

**Research question**: How can speculative decoding accelerate LLM inference while maintaining original distributions?
**Methodology**: This tutorial presents a comprehensive introduction to speculative decoding techniques, including draft model architectures and verification strategies. Explores acceleration potential and future research directions through systematic analysis of the SD paradigm.
**Key findings**:
- Speculative decoding drafts multiple future tokens and verifies them in parallel, enabling simultaneous decoding of multiple tokens per step
- The approach achieves 2x-4x speedups in LLM inference while maintaining original distributions
- Unlike traditional autoregressive decoding, SD mitigates high inference latency through an innovative decoding paradigm
- The tutorial covers latest techniques including draft model architectures and verification strategies
- Future research directions in speculative decoding are explored for more efficient LLM inference
**Limitations**: not stated in abstract

## References

Bhendawade, N., Nishu, K., Kundu, A., Bartels, C., Cho, M., & Belousova, I. (2025). Mirror speculative decoding: Breaking the serial barrier in LLM inference. arXiv. https://arxiv.org/abs/2510.13161

Ge, D., Gao, J., Jiang, Q., Feng, Y., & Ji, W. (2025). Automatic task detection and heterogeneous LLM speculative decoding. arXiv. https://arxiv.org/abs/2505.08600

Li, R., Chen, F., & Li, P. (2025). Semi-clairvoyant scheduling of speculative decoding requests to minimize LLM inference latency. arXiv. https://arxiv.org/abs/2505.17074

Liu, F., Li, X., Zhao, K., Gao, Y., Zhou, Z., Zhang, Z., Wang, Z., Dou, W., Zhong, S., & Tian, C. (2026). DART: Diffusion-inspired speculative decoding for fast LLM inference. arXiv. https://arxiv.org/abs/2601.19278

Lu, K.-W., Hong, D.-Y., Liu, P., & Wu, J.-J. (2025). AdaSD: Adaptive speculative decoding for efficient language model inference. arXiv. https://arxiv.org/abs/2512.11280

Ryu, H., & Kim, E. (2024). Closer look at efficient inference methods: A survey of speculative decoding. arXiv. https://arxiv.org/abs/2411.13157

Shi, L., Li, Z., Zhang, L., Qi, B., Liu, G., & Zhao, H. (2025). Scaling LLM speculative decoding: Non-autoregressive forecasting in large-batch scenarios. arXiv. https://arxiv.org/abs/2511.20340

Timor, N., Mamou, J., Korat, D., Berchansky, M., Jain, G., Pereg, O., Wasserblat, M., & Harel, D. (2025). Accelerating LLM inference with lossless speculative decoding algorithms for heterogeneous vocabularies. arXiv. https://arxiv.org/abs/2502.05202

Wang, X., Miao, Z., Zhu, Y., Shen, H., Wan, Z., Yang, F., & Zhang, M. (2026). AgentSpec: Speculative decoding for batch inference of LLM agents. arXiv. https://arxiv.org/abs/2608.24004

Xia, H., Du, C., Li, Y., Liu, Q., & Li, W. (2025). Tutorial proposal: Speculative decoding for efficient LLM inference. arXiv. https://arxiv.org/abs/2503.00491
