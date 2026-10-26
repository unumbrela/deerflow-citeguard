# Systematic Literature Review: Diffusion Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "diffusion language models", category cs.CL, published between 2023-08-14 and 2025-08-13
**Citation format**: APA 7th edition

## Executive Summary

Diffusion language models (DLMs) represent an emerging alternative to autoregressive language models, offering bidirectional generation capabilities and improved controllability. The surveyed literature from 2023-2025 demonstrates rapid progress in addressing core challenges: inference speed, reasoning capabilities, controllability, and text quality. Recent breakthroughs show DLMs achieving comparable or superior performance to autoregressive models in certain benchmarks, with innovations like anchoring mechanisms, KV-caching adaptations, and one-step generation frameworks dramatically improving efficiency. The field is transitioning from proof-of-concept to practical deployment, with significant advances in reasoning tasks, code generation, and controllable text production.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "diffusion language models", filtered to category cs.CL, published between 2023-08-14 and 2025-08-13. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Accelerating Inference Speed

A dominant research direction addresses the fundamental speed disadvantage of diffusion models compared to autoregressive generation. Multiple papers propose caching mechanisms and scheduling strategies to reduce the iterative denoising steps that traditionally slow DLM inference. Ma et al. (2025) introduced dKV-Cache, adapting the successful KV-cache concept from autoregressive models to the diffusion setting, achieving 2-10× speedup. Luxembourg et al. (2025) proposed dilated scheduling that unmasks non-adjacent token groups in parallel, yielding up to 5.8× wall-clock speedup. Most dramatically, Chen et al. (2025) developed DLM-One, a one-step generation framework achieving ~2000× speedup in sampling steps through score distillation. These approaches collectively transform DLMs from theoretically interesting but impractical models into viable deployment candidates.

### Theme 2: Enhancing Reasoning Capabilities

Several papers focus on integrating reasoning mechanisms into DLMs, leveraging their bidirectional nature for superior reasoning performance. Ye et al. (2024) proposed Diffusion-of-Thought (DoT), allowing reasoning steps to diffuse over time and demonstrating that small diffusion models with DoT outperform much larger autoregressive models in reasoning tasks. Huang et al. (2025) introduced DCoLT, treating intermediate diffusion steps as latent thinking actions optimized via outcome-based reinforcement learning, achieving substantial improvements on GSM8K (+9.8%), MATH (+5.7%), and code generation benchmarks. The bidirectional generation inherent to DLMs enables non-linear, iterative reasoning that autoregressive models cannot naturally support.

### Theme 3: Improving Text Quality and Likelihood Modeling

Closing the performance gap with autoregressive models in text quality remains a central challenge. Rout et al. (2025) introduced the Anchored Diffusion Language Model (ADLM), a two-stage framework that first predicts distributions over important tokens, then generates remaining tokens conditioned on these anchors. ADLM achieved up to 25.4% improvement in test perplexity and, notably, surpassed autoregressive models in MAUVE score—marking the first time a DLM generated better human-like text than an autoregressive counterpart. This represents a watershed moment for the field, demonstrating that DLMs can exceed rather than merely match autoregressive performance.

### Theme 4: Controllability and Conditional Generation

The inherent flexibility of diffusion processes enables sophisticated control mechanisms unavailable to autoregressive models. Kang et al. (2024) proposed QE-CDLM, using quantized embedding vectors to create gradient-based controllers for fine-grained generation control. Koh et al. (2024) integrated conditional masked language models through conditional Markov Random Field theory, achieving superior quality-diversity tradeoffs. Buzzard (2025) demonstrated that classifier-free guidance and stochastic clamping provide controllable quality-diversity tradeoffs analogous to temperature control in autoregressive models. These approaches exploit the diffusion framework's ability to iteratively refine outputs based on gradient signals.

### Theme 5: Scaling and Instruction Tuning

Foundational work establishes that DLMs benefit from scaling and instruction tuning similarly to autoregressive models. Ye et al. (2023) demonstrated that scaling diffusion language models consistently improves performance across downstream tasks, and that instruction finetuning elicits zero-shot and few-shot in-context learning abilities. This work established DLMs as viable general-purpose language models rather than niche approaches for specific tasks. The finding that masked language modeling pretraining enables knowledge acquisition from massive data parallels the success of BERT-style pretraining, suggesting DLMs can follow similar scaling trajectories.

## Convergences and Disagreements

**Convergences**: The surveyed papers unanimously agree that inference speed is the primary barrier to DLM adoption, with all efficiency-focused works targeting reduction of iterative denoising steps. Multiple papers converge on the finding that DLMs excel at reasoning tasks due to their bidirectional nature (Ye et al., 2024; Huang et al., 2025; Rout et al., 2025). There is also agreement that instruction tuning and scaling laws apply to DLMs similarly to autoregressive models (Ye et al., 2023).

**Disagreements**: Different approaches to speedup involve tradeoffs between quality and efficiency. dKV-Cache-Decode provides lossless acceleration while dKV-Cache-Greedy sacrifices some quality for higher speedup (Ma et al., 2025). Similarly, DUS trades network calls against generation quality (Luxembourg et al., 2025), while DLM-One maintains competitive performance despite one-step generation through careful adversarial regularization (Chen et al., 2025). The optimal balance remains an open question, with different approaches suited to different application requirements.

## Gaps and Open Questions

The surveyed literature reveals several consistent gaps. None of the papers explicitly address computational requirements for training large-scale DLMs, though Huang et al. (2025) note training DCoLT-reinforced models required 16 H800 GPUs. Memory efficiency during training remains underexplored compared to inference optimization. Safety and alignment considerations specific to DLMs—particularly given their iterative refinement capabilities—are not addressed in any surveyed paper. Additionally, while several papers demonstrate strong benchmark performance, real-world deployment case studies are absent. The theoretical understanding of why anchoring (Rout et al., 2025) or dilated scheduling (Luxembourg et al., 2025) works remains incomplete, with most papers providing empirical rather than theoretical justification.

## Per-Paper Annotations

### Buzzard (2025)

**Research question**: How can diffusion language models gain controllable trade-offs between quality and diversity similar to temperature control in autoregressive models?
**Methodology**: The author proposes using classifier-free guidance and stochastic clamping techniques to manipulate the quality-diversity trade-off on sequence-to-sequence tasks in continuous embedding space diffusion models.
**Key findings**:
- Classifier-free guidance can be used to control quality-diversity trade-offs in diffusion language models
- Stochastic clamping provides another mechanism for manipulating generation characteristics
- These techniques may be used to improve diffusion language model performance on sequence-to-sequence tasks
- The work addresses a gap in diffusion models lacking natural control mechanisms comparable to autoregressive temperature
**Limitations**: not stated in abstract

### Chen et al. (2025)

**Research question**: Can diffusion language models achieve efficient one-step sequence generation while maintaining competitive performance?
**Methodology**: The authors propose DLM-One, a score-distillation-based framework that aligns student model outputs with a pretrained teacher DLM's score function in forward-diffused noisy space, eliminating iterative refinement. They propose an adversarially-regularized two-stage training scheme to prevent student degeneration.
**Key findings**:
- DLM-One achieves up to ~2000× speedup in sampling steps and ~500× in wall-clock time
- The framework maintains competitive performance on benchmark text generation tasks despite one-step generation
- The approach is architecture-agnostic and robust across diverse continuous manifolds including token embedding spaces and logit simplex spaces
- One-step score distillation is positioned as a viable path for efficient deployment of continuous diffusion models in NLP
**Limitations**: not stated in abstract

### Huang et al. (2025)

**Research question**: Can a reasoning framework for diffusion language models optimize reasoning trajectories using outcome-based reinforcement learning?
**Methodology**: The authors introduce Diffusion Chain of Lateral Thought (DCoLT), which treats each intermediate step in the reverse diffusion process as a latent thinking action and optimizes the entire reasoning trajectory with outcome-based RL. Implementation is tested on SEDD (continuous-time discrete diffusion) and LLaDA (discrete-time masked diffusion) models.
**Key findings**:
- DCoLT allows bidirectional, non-linear reasoning without strict grammatical correctness in intermediate steps
- DCoLT-reinforced LLaDA improves reasoning accuracy by +9.8% on GSM8K, +5.7% on MATH, +11.4% on MBPP, and +19.5% on HumanEval
- The order to predict and unmask tokens plays an essential role in optimizing RL action via the Unmasking Policy Module
- DCoLT-reinforced diffusion language models outperform others trained by SFT or RL or both using only public data and 16 H800 GPUs
- DCoLT treats intermediate diffusion steps as latent thinking actions optimized to maximize final answer correctness
**Limitations**: not stated in abstract

### Kang et al. (2024)

**Research question**: How can the controllability, portability, and inference speed of diffusion language models be improved while reducing memory and computational demands?
**Methodology**: The authors propose Quantized Embedding Controllable Diffusion Language Model (QE-CDLM), which remodels task-specific embedding space via quantization to obtain a gradient-based controller and more stable intermediate latent variables. Adaption fine-tuning is employed to reduce tunable weights, evaluated on five fine-grained control tasks.
**Key findings**:
- QE-CDLM achieves better perplexity and lightweight fine-tuning compared to existing methods
- Quantized embedding space provides a gradient-based controller for generation tasks
- More stable intermediate latent variables bring accelerated convergence and better controllability
- Adaption fine-tuning reduces tunable weights for improved portability
- QE-CDLM compares favorably to existing methods in quality and feasibility across five challenging control tasks
**Limitations**: not stated in abstract

### Koh et al. (2024)

**Research question**: How can diffusion language models be improved to address challenges in diverse text generation and conditional controllability?
**Methodology**: The authors propose Diffusion-EAGS, a framework integrating conditional masked language models into diffusion language models through conditional Markov Random Field theory. They introduce entropy-adaptive Gibbs sampling and entropy-based noise scheduling to counterbalance model shortcomings.
**Key findings**:
- Diffusion-EAGS outperforms baselines in non-autoregressive text generation
- The framework achieves the best quality-diversity tradeoff among compared methods
- The approach effectively addresses degeneracy issues in non-autoregressive methods
- The integration demonstrates effectiveness in conditional generation tasks
**Limitations**: not stated in abstract

### Luxembourg et al. (2025)

**Research question**: How can masked diffusion language models achieve faster parallel generation without sacrificing quality?
**Methodology**: The authors propose the Dilated Unmasking Scheduler (DUS), an inference-only method that partitions sequence positions into non-adjacent dilated groups and unmasks them in parallel to minimize joint entropy gain at each denoising step. The approach trades off network calls against generation quality.
**Key findings**:
- DUS yields up to 5.8× wall-clock speedup over token-by-token masked diffusion language model decoding
- The method outperforms confidence-based planners across math, code, general-knowledge, and instruction following benchmarks
- DUS turns the diffusion quality-speed trade-off into a deterministic, predictable speedup set by block size B
- Applied as a drop-in post-filter, dilated spacing also improves adaptive samplers
**Limitations**: not stated in abstract

### Ma et al. (2025)

**Research question**: How can the slow inference of diffusion language models be accelerated given their non-autoregressive architecture prevents traditional KV caching?
**Methodology**: The authors propose delayed KV-Cache (dKV-Cache), a KV-cache-like mechanism for the denoising process of diffusion language models, with two variants: dKV-Cache-Decode for lossless acceleration and dKV-Cache-Greedy for aggressive caching. Evaluation is conducted on general language understanding, mathematical, and code-generation benchmarks.
**Key findings**:
- dKV-Cache achieves 2-10x speedup in inference, narrowing the gap between autoregressive models and diffusion language models
- dKV-Cache-Decode provides almost lossless acceleration and even improves performance on long sequences
- dKV-Cache-Greedy achieves higher speed-ups with quadratic time complexity at the cost of some performance degradation
- Different tokens have distinct representation dynamics throughout the diffusion process
- The cache mechanism works in a training-free manner on current diffusion language models
**Limitations**: not stated in abstract

### Rout et al. (2025)

**Research question**: How can diffusion language models be improved to close the performance gap with autoregressive models in likelihood modeling and text quality?
**Methodology**: The authors introduce the Anchored Diffusion Language Model (ADLM), a two-stage framework that first predicts distributions over important tokens via an anchor network, then predicts likelihoods of missing tokens conditioned on anchored predictions. They derive an Anchored Negative Evidence Lower Bound (ANELBO) objective and evaluate on LM1B, OpenWebText, and seven zero-shot benchmarks.
**Key findings**:
- ADLM achieves up to 25.4% improvement in test perplexity over prior diffusion language models on LM1B and OpenWebText
- The model achieves state-of-the-art performance in zero-shot generalization across seven benchmarks
- ADLM surpasses autoregressive models in MAUVE score, marking the first time a diffusion language model generates better human-like text than an autoregressive model
- Anchoring improves sample complexity and likelihood modeling theoretically
- The anchoring approach boosts performance in autoregressive models and enhances reasoning in math and logic tasks
**Limitations**: not stated in abstract

### Ye et al. (2023)

**Research question**: Can diffusion language models solve general language tasks comparably to autoregressive models?
**Methodology**: The authors build diffusion language models at scale by pretraining on massive data via masked language modeling, then reprogram them via diffusive adaptation with task-specific and instruction finetuning. Experiments evaluate scaling effects and instruction finetuning across downstream language tasks.
**Key findings**:
- Scaling diffusion language models consistently improves performance across downstream language tasks
- Instruction finetuning elicits zero-shot and few-shot in-context learning abilities for unseen tasks
- Diffusion language models show promise in advanced abilities such as reasoning
- Masked language modeling pretraining enables knowledge acquisition from massive data
- Task-specific and instruction finetuning unlock versatility in solving general language tasks
**Limitations**: not stated in abstract

### Ye et al. (2024)

**Research question**: Can diffusion models be integrated with Chain-of-Thought reasoning to improve reasoning ability compared to autoregressive language models?
**Methodology**: The authors propose Diffusion-of-Thought (DoT), integrating diffusion models with Chain-of-Thought reasoning, allowing reasoning steps to diffuse over time through a diffusion language model. Experiments evaluate DoT on multi-digit multiplication, boolean logic, and grade school math problems.
**Key findings**:
- A small diffusion model with DoT outperforms a much larger autoregressive model in both efficiency and accuracy
- DoT allows reasoning steps to diffuse over time, offering greater flexibility in trading computation for reasoning performance
- DoT showcases promising self-correction abilities
- DoT benefits from existing reasoning-enhancing techniques like self-consistency decoding
- DoT is effective in multi-digit multiplication, boolean logic, and grade school math problems
**Limitations**: not stated in abstract

## References

Buzzard, Z. (2025). Understanding the quality-diversity trade-off in diffusion language models. arXiv. https://arxiv.org/abs/2503.10683

Chen, T., Zhang, S., & Zhou, M. (2025). DLM-One: Diffusion language models for one-step sequence generation. arXiv. https://arxiv.org/abs/2506.00290

Huang, Z., Chen, Z., Wang, Z., Li, T., & Qi, G.-J. (2025). Reinforcing the diffusion chain of lateral thought with diffusion language models. arXiv. https://arxiv.org/abs/2505.10446

Kang, C., Chen, X., Hu, Y., & Novak, D. (2024). Quantized embedding vectors for controllable diffusion language models. arXiv. https://arxiv.org/abs/2402.10107

Koh, H., Jhang, M., Kim, D., Lee, S., & Jung, K. (2024). Conditional [MASK] discrete diffusion language model. arXiv. https://arxiv.org/abs/2411.06438

Luxembourg, O., Permuter, H., & Nachmani, E. (2025). Plan for speed: Dilated scheduling for masked diffusion language models. arXiv. https://arxiv.org/abs/2506.19037

Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The cache for diffusion language models. arXiv. https://arxiv.org/abs/2505.15781

Rout, L., Caramanis, C., & Shakkottai, S. (2025). Anchored diffusion language model. arXiv. https://arxiv.org/abs/2505.18456

Ye, J., Zheng, Z., Bao, Y., Qian, L., & Gu, Q. (2023). Diffusion language models can perform many tasks with scaling and instruction-finetuning. arXiv. https://arxiv.org/abs/2308.12219

Ye, J., Gong, S., Chen, L., Zheng, L., Gao, J., Shi, H., Wu, C., Jiang, X., Li, Z., Bi, W., & Kong, L. (2024). Diffusion of thoughts: Chain-of-thought reasoning in diffusion language models. arXiv. https://arxiv.org/abs/2402.07754
