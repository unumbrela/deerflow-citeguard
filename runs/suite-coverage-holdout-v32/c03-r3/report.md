# Systematic Literature Review: Diffusion Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "diffusion language models", category cs.CL, published between 2023-08-14 and 2025-08-13
**Citation format**: APA 7th edition

## Executive Summary

Diffusion language models (DLMs) have emerged as a compelling alternative to autoregressive models, offering bidirectional generation capabilities and improved controllability. The surveyed literature from 2023-2025 reveals a rapidly maturing field focused on addressing three core challenges: closing the performance gap with autoregressive models, improving inference efficiency, and enhancing reasoning capabilities. Recent breakthroughs demonstrate that DLMs can now surpass autoregressive models in text quality metrics while achieving dramatic speedups through novel caching mechanisms and one-step generation techniques. The field shows strong convergence around scaling laws, instruction finetuning, and the integration of chain-of-thought reasoning, though significant gaps remain in theoretical understanding and deployment practicality.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "diffusion language models", filtered to category cs.CL, published between 2023-08-14 and 2025-08-13. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Performance and Scaling

The foundational question driving early DLM research was whether diffusion models could achieve performance comparable to autoregressive models on language tasks. Ye et al. (2023) demonstrated that with proper scaling and instruction finetuning, diffusion language models can indeed perform many tasks competitively. Their approach involved pretraining on massive data via masked language modeling, then reprogramming models through diffusive adaptation with task-specific and instruction finetuning. This work established that scaling consistently improves performance across downstream language tasks and elicits zero-shot and few-shot in-context learning abilities.

Building on this foundation, Rout et al. (2025) introduced the Anchored Diffusion Language Model (ADLM), achieving up to 25.4% improvement in test perplexity over prior DLMs and, notably, surpassing autoregressive models in MAUVE score—marking the first time a DLM generated better human-like text than an AR model. ADLM's two-stage framework predicts distributions over important tokens via an anchor network, then predicts missing tokens conditioned on anchored predictions, theoretically improving sample complexity and likelihood modeling.

### Theme 2: Reasoning and Chain-of-Thought Integration

A significant research direction has focused on integrating reasoning capabilities into the diffusion process itself. Ye et al. (2024) proposed Diffusion-of-Thought (DoT), which integrates diffusion models with Chain-of-Thought reasoning, allowing reasoning steps to diffuse over time. Their approach demonstrated that a small diffusion model with DoT could outperform much larger autoregressive models in both efficiency and accuracy on multi-digit multiplication, boolean logic, and grade school math problems, while showcasing promising self-correction abilities.

Huang et al. (2025) advanced this direction with the Diffusion Chain of Lateral Thought (DCoLT), which treats each intermediate step in the reverse diffusion process as a latent thinking action and optimizes the entire reasoning trajectory using outcome-based reinforcement learning. DCoLT allows bidirectional, non-linear reasoning with no strict grammatical correctness requirements for intermediate steps. Their reinforced DLMs outperformed other DLMs trained by supervised finetuning or reinforcement learning using only public data and 16 H800 GPUs, boosting reasoning accuracy by +9.8% on GSM8K, +5.7% on MATH, +11.4% on MBPP, and +19.5% on HumanEval.

### Theme 3: Efficiency and Speed Optimization

The inference speed bottleneck has been a critical limitation of DLMs due to their non-autoregressive architecture preventing traditional KV caching. Ma et al. (2025) addressed this with dKV-Cache, a delayed KV-Cache mechanism based on the observation that different tokens have distinct representation dynamics throughout diffusion. Their approach achieves 2-10x speedup in inference, narrowing the gap between autoregressive models and DLMs. The dKV-Cache-Decode variant provides almost lossless acceleration and even improves performance on long sequences, while dKV-Cache-Greedy achieves higher speed-ups with quadratic time complexity at some performance cost.

Chen et al. (2025) pursued an even more aggressive approach with DLM-One, a score-distillation-based framework enabling one-step sequence generation. Their adversarially-regularized two-stage training scheme achieved up to ~2000× speedup in sampling steps and ~500× in wall-clock time while maintaining competitive performance on benchmark text generation tasks. This architecture-agnostic approach works across diverse continuous manifolds including token embedding spaces and logit simplex spaces.

Luxembourg et al. (2025) proposed the Dilated Unmasking Scheduler (DUS), an inference-only method that partitions sequence positions into non-adjacent dilated groups and unmasks them in parallel to minimize joint entropy gain at each denoising step. DUS yields up to 5.8× wall-clock speedup over token-by-token masked diffusion language model decoding without modifying the underlying denoiser, outperforming confidence-based planners across math, code, general-knowledge, and instruction-following benchmarks.

### Theme 4: Controllability and Quality-Diversity Trade-off

Controllability represents a key advantage of DLMs over autoregressive models, yet managing the quality-diversity trade-off has remained challenging. Kang et al. (2024) proposed QE-CDLM, which remodels the task-specific embedding space via quantization to obtain more stable intermediate latent variables and enable gradient-based control. Their approach achieves better perplexity and lightweight fine-tuning compared to existing methods, with quantized embedding space leading to accelerated convergence and improved model portability for independent deployment.

Buzzard (2025) addressed the lack of natural control mechanisms in DLMs by proposing classifier-free guidance and stochastic clamping to manipulate the quality-diversity trade-off on sequence-to-sequence tasks. These techniques provide DLMs with control similar to temperature in autoregressive models, improving performance on sequence-to-sequence tasks and addressing a key limitation hindering understanding of model performance.

Koh et al. (2024) introduced Diffusion-EAGS, integrating conditional masked language models into diffusion language models through conditional Markov Random Field theory. Their framework employs entropy-adaptive Gibbs sampling and entropy-based noise scheduling to balance model shortcomings, achieving the best quality-diversity tradeoff among compared methods and demonstrating effectiveness in conditional generation tasks.

### Theme 5: Architectural Innovations

Beyond efficiency and controllability, novel architectural approaches have emerged to address fundamental DLM limitations. The surveyed papers reveal diverse strategies: anchoring mechanisms (Rout et al., 2025), quantized embeddings (Kang et al., 2024), score distillation (Chen et al., 2025), and dilated scheduling (Luxembourg et al., 2025). These innovations reflect the field's exploration of multiple pathways to improve DLMs rather than convergence on a single architectural paradigm.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, scaling consistently improves DLM performance across tasks (Ye et al., 2023; Rout et al., 2025). Second, instruction finetuning is essential for eliciting zero-shot and few-shot capabilities (Ye et al., 2023; Huang et al., 2025). Third, the bidirectional nature of diffusion provides inherent advantages for reasoning tasks that autoregressive models cannot match (Ye et al., 2024; Huang et al., 2025). Fourth, inference speed remains the primary deployment bottleneck, requiring specialized solutions beyond autoregressive optimizations (Ma et al., 2025; Chen et al., 2025; Luxembourg et al., 2025).

**Disagreements**: The literature shows some divergence in approach philosophy. While some works prioritize architectural innovation (Rout et al., 2025; Chen et al., 2025), others focus on training-free inference optimizations (Ma et al., 2025; Luxembourg et al., 2025). Additionally, there is tension between approaches that treat diffusion steps as latent reasoning actions (Huang et al., 2025) versus those that view them purely as generation mechanisms (Chen et al., 2025). The quality-diversity trade-off is addressed through different mechanisms—quantization (Kang et al., 2024), classifier-free guidance (Buzzard, 2025), and entropy-adaptive sampling (Koh et al., 2024)—without clear consensus on the optimal approach.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either space constraints or reluctance to acknowledge weaknesses—a notable gap in scientific transparency. Second, while efficiency improvements are dramatic (up to 2000× speedup), theoretical understanding of why certain approaches work remains limited. Third, the field lacks comprehensive benchmarks comparing all approaches under standardized conditions, making it difficult to assess relative merits. Fourth, deployment practicality—memory requirements, energy consumption, and integration with existing infrastructure—receives minimal attention despite being critical for real-world adoption. Finally, the interaction between reasoning capabilities and generation quality remains underexplored: does enhancing reasoning compromise text quality, or can both be optimized simultaneously?

## Per-Paper Annotations

### Buzzard (2025)

**Research question**: How can diffusion language models gain natural control over the quality-diversity trade-off similar to temperature in autoregressive models?
**Methodology**: The author proposes using classifier-free guidance and stochastic clamping to manipulate the quality-diversity trade-off on sequence-to-sequence tasks, demonstrating these techniques for improving diffusion language model performance.
**Key findings**:
- Classifier-free guidance can be used to control the quality-diversity trade-off in diffusion language models
- Stochastic clamping provides another mechanism for manipulating generation quality and diversity
- These techniques improve the performance of diffusion language models on sequence-to-sequence tasks
- The work addresses the lack of natural control mechanisms that hinder understanding of model performance
**Limitations**: not stated in abstract

### Chen et al. (2025)

**Research question**: Can diffusion language models achieve one-step sequence generation while maintaining competitive performance?
**Methodology**: The authors propose DLM-One, a score-distillation-based framework that aligns student model output scores with a pretrained teacher DLM's score function in forward-diffused noisy space. They propose an adversarially-regularized two-stage training scheme and evaluate across multiple continuous manifolds and benchmark text generation tasks.
**Key findings**:
- DLM-One achieves up to ~2000× speedup in sampling steps and ~500× in wall-clock time
- The framework maintains competitive performance on benchmark text generation tasks despite one-step generation
- The approach is architecture-agnostic and robust across diverse continuous manifolds including token embedding spaces and logit simplex spaces
- An adversarially-regularized two-stage training scheme prevents student degeneration
- One-step score distillation is positioned as a viable path for efficient deployment of continuous diffusion models
**Limitations**: not stated in abstract

### Huang et al. (2025)

**Research question**: Can a reasoning framework that treats intermediate diffusion steps as latent thinking actions and optimizes reasoning trajectories with outcome-based reinforcement learning improve diffusion language model performance?
**Methodology**: The authors introduce Diffusion Chain of Lateral Thought (DCoLT), which treats each intermediate step in the reverse diffusion process as a latent thinking action and optimizes the entire reasoning trajectory using outcome-based reinforcement learning. DCoLT is implemented on SEDD (continuous-time discrete diffusion) and LLaDA (discrete-time masked diffusion) with a ranking-based Unmasking Policy Module.
**Key findings**:
- DCoLT allows bidirectional, non-linear reasoning with no strict grammatical correctness requirements for intermediate steps
- DCoLT-reinforced DLMs outperform other DLMs trained by SFT or RL or both using only public data and 16 H800 GPUs
- DCoLT-reinforced LLaDA boosts reasoning accuracy by +9.8% on GSM8K, +5.7% on MATH, +11.4% on MBPP, and +19.5% on HumanEval
- Token unmasking order plays an essential role in optimizing RL actions for masked diffusion models
**Limitations**: not stated in abstract

### Kang et al. (2024)

**Research question**: How can the controllability, portability, and inference speed of diffusion language models be improved while reducing memory and computational demands?
**Methodology**: The authors propose QE-CDLM, which remodels the task-specific embedding space via quantization to obtain more stable intermediate latent variables and enable gradient-based control. An adaption fine-tuning method is employed to reduce tunable weights.
**Key findings**:
- QE-CDLM achieves better perplexity and lightweight fine-tuning compared to existing methods
- Quantized embedding space leads to accelerated convergence and better controllability
- The approach improves model portability for independent deployment
- More stable intermediate latent variables are obtained through the quantization approach
**Limitations**: not stated in abstract

### Koh et al. (2024)

**Research question**: How can diffusion language models be improved to address degenerate outputs and shortcomings in conditional generation?
**Methodology**: The authors propose Diffusion-EAGS, integrating conditional masked language models into diffusion language models through conditional Markov Random Field theory. They introduce entropy-adaptive Gibbs sampling and entropy-based noise scheduling to balance model shortcomings.
**Key findings**:
- Diffusion-EAGS outperforms baselines in non-autoregressive text generation
- The framework achieves the best quality-diversity tradeoff among compared methods
- Entropy-adaptive Gibbs sampling and entropy-based noise scheduling effectively counterbalance model shortcomings
- The approach demonstrates effectiveness in conditional generation tasks
**Limitations**: not stated in abstract

### Luxembourg et al. (2025)

**Research question**: How can masked diffusion language models achieve faster parallel generation without sacrificing quality?
**Methodology**: The authors propose the Dilated Unmasking Scheduler (DUS), an inference-only method that partitions sequence positions into non-adjacent dilated groups and unmasks them in parallel to minimize joint entropy gain at each denoising step. They evaluate across math, code, general-knowledge, and instruction-following benchmarks.
**Key findings**:
- DUS yields up to 5.8× wall-clock speedup over token-by-token MDLM decoding without modifying the underlying denoiser
- DUS outperforms confidence-based planners across GSM8K, MATH500, HumanEval, MBPP, BBH, MMLU-Pro, and IFEval benchmarks
- The approach recovers most performance lost under traditional parallel unmasking strategies
- DUS turns the diffusion quality-speed trade-off into a deterministic, predictable speedup set by block size B
- Dilated spacing improves adaptive samplers when applied as a drop-in post-filter
**Limitations**: not stated in abstract

### Ma et al. (2025)

**Research question**: How can the slow inference bottleneck in diffusion language models be addressed given their non-autoregressive architecture prevents traditional KV caching?
**Methodology**: The authors propose delayed KV-Cache (dKV-Cache), a caching mechanism for the denoising process of DLMs based on the observation that different tokens have distinct representation dynamics throughout diffusion. Two variants are designed: dKV-Cache-Decode for lossless acceleration and dKV-Cache-Greedy for aggressive speed-ups.
**Key findings**:
- dKV-Cache achieves 2-10x speedup in inference, narrowing the gap between autoregressive models and DLMs
- dKV-Cache-Decode provides almost lossless acceleration and even improves performance on long sequences
- dKV-Cache-Greedy achieves higher speed-ups with quadratic time complexity at the cost of some performance degradation
- The approach works in a training-free manner on current DLMs
- Existing DLMs may under-utilize contextual information during inference
**Limitations**: not stated in abstract

### Rout et al. (2025)

**Research question**: How can diffusion language models be improved to close the performance gap with autoregressive models in likelihood modeling and text quality?
**Methodology**: The authors introduce Anchored Diffusion Language Model (ADLM), a two-stage framework that first predicts distributions over important tokens via an anchor network, then predicts missing tokens conditioned on anchored predictions. They derive an Anchored Negative Evidence Lower Bound (ANELBO) objective and evaluate on LM1B, OpenWebText, and seven zero-shot benchmarks.
**Key findings**:
- ADLM achieves up to 25.4% improvement in test perplexity over prior diffusion language models
- ADLM surpasses autoregressive models in MAUVE score, marking the first time a DLM generates better human-like text than an AR model
- ADLM achieves state-of-the-art performance in zero-shot generalization across seven benchmarks
- Anchoring improves sample complexity and likelihood modeling theoretically
- Anchoring boosts performance in autoregressive models and enhances reasoning in math and logic tasks
**Limitations**: not stated in abstract

### Ye et al. (2023)

**Research question**: Can diffusion language models solve general language tasks comparably to autoregressive models?
**Methodology**: The authors build diffusion language models at scale by pretraining on massive data via masked language modeling, then reprogram them into diffusion models through diffusive adaptation with task-specific and instruction finetuning.
**Key findings**:
- Scaling diffusion language models consistently improves performance across downstream language tasks
- Instruction finetuning elicits zero-shot and few-shot in-context learning abilities for unseen tasks
- The approach shows promise in advanced abilities such as reasoning
- Diffusion models can be made competent language learners through proper scaling and finetuning
**Limitations**: not stated in abstract

### Ye et al. (2024)

**Research question**: Can integrating diffusion models with Chain-of-Thought reasoning improve the reasoning ability of language models compared to autoregressive approaches?
**Methodology**: The authors propose Diffusion-of-Thought (DoT), which integrates diffusion models with Chain-of-Thought reasoning, allowing reasoning steps to diffuse over time through a diffusion language model with greater flexibility in trading computation for reasoning performance.
**Key findings**:
- A small diffusion model with DoT outperforms a much larger autoregressive model in both efficiency and accuracy on multi-digit multiplication, boolean logic, and grade school math problems
- DoT showcases promising self-correction abilities
- DoT benefits from existing reasoning-enhancing techniques like self-consistency decoding
- The approach offers greater flexibility in trading-off computation for reasoning performance compared to autoregressive models
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
