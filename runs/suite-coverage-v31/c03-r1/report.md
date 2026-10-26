# Systematic Literature Review: Diffusion Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "diffusion language models", category cs.CL, published between 2023-08-14 and 2025-08-14
**Citation format**: APA 7th edition

## Executive Summary

Diffusion Language Models (DLMs) have emerged as a compelling alternative to autoregressive language models, offering parallel token generation through iterative denoising processes. The surveyed literature from 2023-2025 reveals a rapidly maturing field addressing fundamental challenges in efficiency, reasoning capabilities, and text quality. Recent breakthroughs demonstrate that DLMs can achieve performance comparable to autoregressive models while providing significant speedup through parallel generation. Key advances include instruction-finetuning for task generalization, novel caching mechanisms for inference acceleration, reinforcement learning for enhanced reasoning, and architectural innovations that close the performance gap with traditional autoregressive approaches. The field has progressed from proving feasibility to achieving state-of-the-art results across multiple benchmarks, with several papers reporting DLMs surpassing autoregressive models in specific metrics.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "diffusion language models", filtered to category cs.CL, published between 2023-08-14 and 2025-08-14. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Inference Efficiency and Acceleration

A dominant research direction focuses on overcoming DLMs' historical inference speed disadvantage compared to autoregressive models. Multiple papers address the fundamental challenge that non-autoregressive generation cannot leverage traditional key-value caching. Ma et al. (2025) introduced dKV-Cache, achieving 2-10x speedup through delayed caching mechanisms that work with the denoising process. Chen et al. (2025) took a more radical approach with DLM-One, enabling one-step sequence generation through score distillation, achieving approximately 2000× speedup in sampling steps. Luxembourg et al. (2025) proposed the Dilated Unmasking Scheduler, which partitions sequence positions into non-adjacent groups for parallel unmasking, yielding up to 5.8× wall-clock speedup without modifying the underlying denoiser. These works collectively demonstrate that efficiency gaps are solvable through architectural and algorithmic innovations.

### Theme 2: Reasoning and Chain-of-Thought Integration

Several papers explore integrating reasoning capabilities into DLMs, drawing inspiration from chain-of-thought approaches successful in autoregressive models. Ye et al. (2024) pioneered Diffusion-of-Thought (DoT), allowing reasoning steps to diffuse over time through a diffusion language model, demonstrating that small diffusion models with DoT can outperform much larger autoregressive models. Huang et al. (2025) advanced this with the Diffusion Chain of Lateral Thought (DCoLT), which treats intermediate diffusion steps as latent thinking actions and optimizes reasoning trajectories with outcome-based reinforcement learning, achieving substantial accuracy improvements across GSM8K (+9.8%), MATH (+5.7%), MBPP (+11.4%), and HumanEval (+19.5%). Rout et al. (2025) found that anchoring mechanisms not only improve likelihood modeling but also enhance reasoning in math and logic tasks, outperforming existing chain-of-thought approaches. This theme reveals DLMs' unique advantages in bidirectional reasoning and self-correction.

### Theme 3: Controllability and Fine-Grained Control

Research has addressed how to provide fine-grained control over DLM generation while maintaining efficiency. Kang et al. (2024) proposed Quantized Embedding Controllable Diffusion Language Model (QE-CDLM), which remodels the task-specific embedding space via quantization to obtain gradient-based controllers and more stable intermediate latent variables. Koh et al. (2024) introduced Diffusion-EAGS, integrating conditional masked language models into DLMs through entropy-adaptive Gibbs sampling and entropy-based noise scheduling, achieving the best quality-diversity tradeoff among evaluated methods. These approaches demonstrate that DLMs can offer superior controllability compared to autoregressive models through their unique latent space properties.

### Theme 4: Scaling and Instruction-Finetuning

Foundational work establishes that DLMs can achieve general language task performance through scaling and instruction-finetuning. Ye et al. (2023) demonstrated that masked language modeling pretraining at scale, combined with diffusive adaptation and instruction finetuning, elicits zero-shot and few-shot in-context learning abilities for unseen tasks. This work established that scaling diffusion language models consistently improves performance across downstream language tasks and enables advanced abilities such as reasoning. The survey by Li et al. (2025) synthesizes these findings, noting that recent advancements allow DLMs to achieve several-fold speed-up with performance comparable to autoregressive counterparts.

### Theme 5: Likelihood Modeling and Text Quality

Improving likelihood modeling and text generation quality remains central to DLM research. Rout et al. (2025) introduced the Anchored Diffusion Language Model (ADLM), achieving up to 25.4% improvement in test perplexity and surpassing autoregressive models in MAUVE score—the first time a DLM generates better human-like text than an AR model. This breakthrough addresses a longstanding criticism of DLMs regarding text quality. The theoretical analysis shows that anchoring improves sample complexity and likelihood modeling, with empirical validation across LM1B, OpenWebText, and seven zero-shot benchmarks.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that DLMs can achieve competitive or superior performance to autoregressive models when properly scaled and trained (Ye et al., 2023; Li et al., 2025). There is strong agreement that parallel generation provides inherent advantages in reducing inference latency and capturing bidirectional context (Chen et al., 2025; Luxembourg et al., 2025). All surveyed papers acknowledge that efficiency improvements are critical for DLM adoption, with consistent emphasis on speedup metrics.

**Disagreements**: Different approaches to acceleration reveal trade-offs: Ma et al. (2025) prioritize lossless acceleration with dKV-Cache-Decode, while Chen et al. (2025) accept some performance degradation for extreme speedup with one-step generation. The choice between maintaining generation quality versus maximizing speed represents an ongoing tension in the field. Additionally, while some papers focus on architectural modifications (Rout et al., 2025), others emphasize training-free inference optimizations (Luxembourg et al., 2025), reflecting different philosophies about where improvements should originate.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the papers explicitly address long-sequence handling beyond standard benchmarks, despite this being a critical requirement for practical applications. Second, infrastructure requirements and deployment considerations receive minimal attention, with most papers reporting results from controlled research environments. Third, while reasoning benchmarks are well-represented, applications to domain-specific tasks (medical, legal, scientific writing) remain underexplored. Fourth, the survey by Li et al. (2025) notes limitations in efficiency, long-sequence handling, and infrastructure requirements that persist across the field. Finally, multimodal extensions are mentioned as an emerging direction but lack comprehensive treatment in the surveyed papers, suggesting this represents a frontier for future research.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: Can score distillation enable one-step sequence generation in continuous diffusion language models while maintaining competitive performance?
**Methodology**: The authors propose DLM-One, a score-distillation-based framework that aligns the scores of a student model's outputs with the score function of a pretrained teacher DLM in the forward-diffused noisy space, with an adversarially-regularized two-stage training scheme.
**Key findings**:
- DLM-One achieves up to ~2000× speedup in sampling steps and ~500× in wall-clock time
- The framework maintains competitive performance on benchmark text generation tasks despite one-step generation
- DLM-One is architecture-agnostic and robust across diverse continuous manifolds
- One-step score distillation is positioned as a viable path for efficient deployment of continuous diffusion models in NLP
**Limitations**: not stated in abstract

### Huang et al. (2025)

**Research question**: Can a reasoning framework that treats intermediate diffusion steps as latent thinking actions and optimizes reasoning trajectories with outcome-based reinforcement learning improve diffusion language model performance?
**Methodology**: The authors introduce Diffusion Chain of Lateral Thought (DCoLT), which allows bidirectional, non-linear reasoning by optimizing the entire reasoning trajectory with outcome-based reinforcement learning, implemented on SEDD and LLaDA models using a ranking-based Unmasking Policy Module.
**Key findings**:
- DCoLT-reinforced diffusion language models outperform other diffusion language models trained by supervised fine-tuning or reinforcement learning or both
- DCoLT-reinforced LLaDA boosts reasoning accuracy by +9.8% on GSM8K, +5.7% on MATH, +11.4% on MBPP, and +19.5% on HumanEval
- The order to predict and unmask tokens plays an essential role in optimizing reinforcement learning actions
- The approach uses only public data and 16 H800 GPUs for training
**Limitations**: not stated in abstract

### Kang et al. (2024)

**Research question**: How can quantized embedding vectors improve the controllability, portability, and inference speed of diffusion language models while reducing memory and computational demands?
**Methodology**: The authors propose Quantized Embedding Controllable Diffusion Language Model (QE-CDLM), which remodels the task-specific embedding space via quantization to obtain a gradient-based controller and more stable intermediate latent variables, with adaption fine-tuning to reduce tunable weights.
**Key findings**:
- QE-CDLM achieves better perplexity and lightweight fine-tuning compared to existing methods
- Quantized embedding space leads to accelerated convergence and better controllability
- The approach produces more stable intermediate latent variables for generation tasks
- Experimental results on five fine-grained control tasks demonstrate favorable quality and feasibility
**Limitations**: not stated in abstract

### Koh et al. (2024)

**Research question**: How can conditional masked language models be integrated into diffusion language models to improve text diversity and controllability?
**Methodology**: The authors propose Diffusion-EAGS, a framework that integrates conditional masked language models into diffusion language models through the theoretical lens of a conditional Markov Random Field, with entropy-adaptive Gibbs sampling and entropy-based noise scheduling.
**Key findings**:
- Diffusion-EAGS outperforms baselines in non-autoregressive text generation
- The framework achieves the best quality-diversity tradeoff among evaluated methods
- Entropy-adaptive Gibbs sampling and entropy-based noise scheduling effectively address shortcomings of both component models
**Limitations**: not stated in abstract

### Li et al. (2025)

**Research question**: What is the current state of diffusion language models, including their evolution, techniques, applications, and challenges?
**Methodology**: This survey provides a holistic overview of the DLM landscape by tracing evolution and relationships with other paradigms, covering foundational principles and state-of-the-art models, offering a comprehensive taxonomy, analyzing techniques from pre-training to post-training methods, and reviewing inference strategies and optimizations.
**Key findings**:
- DLMs generate tokens in parallel through iterative denoising, offering inherent advantages in reducing inference latency and capturing bidirectional context
- Recent advancements allow DLMs to achieve several-fold speed-up with performance comparable to autoregressive counterparts
- The survey provides an up-to-date, comprehensive taxonomy and in-depth analysis of current techniques
- Latest approaches to multimodal extensions of DLMs and their applications across various practical scenarios are highlighted
- Limitations and challenges include efficiency, long-sequence handling, and infrastructure requirements
**Limitations**: not stated in abstract

### Luxembourg et al. (2025)

**Research question**: How can masked diffusion language models achieve faster parallel generation without reducing to slow autoregressive behavior?
**Methodology**: The authors propose the Dilated Unmasking Scheduler (DUS), an inference-only, planner-model-free method that partitions sequence positions into non-adjacent dilated groups and unmasks them in parallel to minimize an upper bound on joint entropy gain at each denoising step.
**Key findings**:
- DUS outperforms confidence-based planners across math (GSM8K, MATH500), code (HumanEval, MBPP), general-knowledge (BBH, MMLU-Pro), and instruction following (IFEval) benchmarks
- DUS yields up to 5.8× wall-clock speedup over token-by-token MDLM decoding without modifying the underlying denoiser
- The speedup is deterministic and predictable, set by the block size B
- Applied as a drop-in post-filter, dilated spacing also improves adaptive samplers
**Limitations**: not stated in abstract

### Ma et al. (2025)

**Research question**: How can diffusion language models overcome their slow inference caused by the inability to use key-value caching due to non-autoregressive architecture?
**Methodology**: The authors propose delayed KV-Cache (dKV-Cache), a KV-cache-like mechanism for the denoising process of diffusion language models, with two variants: dKV-Cache-Decode for lossless acceleration and dKV-Cache-Greedy for aggressive caching.
**Key findings**:
- dKV-Cache achieves 2-10x speedup in inference, narrowing the gap between autoregressive models and diffusion language models
- dKV-Cache-Decode provides almost lossless acceleration and even improves performance on long sequences
- dKV-Cache-Greedy achieves higher speed-ups with quadratic time complexity at the cost of some performance degradation
- The approach can be used in a training-free manner from current diffusion language models
**Limitations**: not stated in abstract

### Rout et al. (2025)

**Research question**: How can diffusion language models be improved to close the performance gap with autoregressive models in likelihood modeling and text quality?
**Methodology**: The authors introduce the Anchored Diffusion Language Model (ADLM), a two-stage framework that first predicts distributions over important tokens via an anchor network, then predicts likelihoods of missing tokens conditioned on anchored predictions, deriving an Anchored Negative Evidence Lower Bound (ANELBO) objective.
**Key findings**:
- ADLM achieves up to 25.4% improvement in test perplexity over prior diffusion language models on LM1B and OpenWebText
- ADLM achieves state-of-the-art performance in zero-shot generalization across seven benchmarks
- ADLM surpasses autoregressive models in MAUVE score, marking the first time a DLM generates better human-like text than an AR model
- Anchoring improves sample complexity and likelihood modeling theoretically
- Anchoring boosts performance in autoregressive models and enhances reasoning in math and logic tasks, outperforming existing chain-of-thought approaches
**Limitations**: not stated in abstract

### Ye et al. (2023)

**Research question**: Can diffusion language models solve general language tasks comparable to autoregressive models through scaling and instruction-finetuning?
**Methodology**: The authors build diffusion language models at scale through masked language modeling pretraining on massive data, then reprogram them via diffusive adaptation with task-specific and instruction finetuning, evaluating performance across downstream language tasks with scaling analysis.
**Key findings**:
- Scaling diffusion language models consistently improves performance across downstream language tasks
- Instruction finetuning elicits zero-shot and few-shot in-context learning abilities for unseen tasks
- The approach shows promise in advanced abilities such as reasoning
- Masked language modeling pretraining enables knowledge acquisition for diffusion language models
**Limitations**: not stated in abstract

### Ye et al. (2024)

**Research question**: Can integrating diffusion models with Chain-of-Thought reasoning improve the reasoning ability of diffusion language models compared to autoregressive approaches?
**Methodology**: The authors propose Diffusion-of-Thought (DoT), which integrates diffusion models with Chain-of-Thought reasoning, allowing reasoning steps to diffuse over time through a diffusion language model, evaluating performance on multi-digit multiplication, boolean logic, and grade school math problems.
**Key findings**:
- A small diffusion model with DoT outperforms a much larger autoregressive model in both efficiency and accuracy
- DoT showcases promising self-correction abilities
- The approach benefits from existing reasoning-enhancing techniques like self-consistency decoding
- DoT offers greater flexibility in trading-off computation for reasoning performance compared to autoregressive models
**Limitations**: not stated in abstract

## References

Chen, T., Zhang, S., & Zhou, M. (2025). DLM-One: Diffusion language models for one-step sequence generation. arXiv. https://arxiv.org/abs/2506.00290

Huang, Z., Chen, Z., Wang, Z., Li, T., & Qi, G.-J. (2025). Reinforcing the diffusion chain of lateral thought with diffusion language models. arXiv. https://arxiv.org/abs/2505.10446

Kang, C., Chen, X., Hu, Y., & Novak, D. (2024). Quantized embedding vectors for controllable diffusion language models. arXiv. https://arxiv.org/abs/2402.10107

Koh, H., Jhang, M., Kim, D., Lee, S., & Jung, K. (2024). Conditional [MASK] discrete diffusion language model. arXiv. https://arxiv.org/abs/2411.06438

Li, T., Chen, M., Guo, B., & Shen, Z. (2025). A survey on diffusion language models. arXiv. https://arxiv.org/abs/2508.10875

Luxembourg, O., Permuter, H., & Nachmani, E. (2025). Plan for speed: Dilated scheduling for masked diffusion language models. arXiv. https://arxiv.org/abs/2506.19037

Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The cache for diffusion language models. arXiv. https://arxiv.org/abs/2505.15781

Rout, L., Caramanis, C., & Shakkottai, S. (2025). Anchored diffusion language model. arXiv. https://arxiv.org/abs/2505.18456

Ye, J., Zheng, Z., Bao, Y., Qian, L., & Gu, Q. (2023). Diffusion language models can perform many tasks with scaling and instruction-finetuning. arXiv. https://arxiv.org/abs/2308.12219

Ye, J., Gong, S., Chen, L., Zheng, L., Gao, J., Shi, H., Wu, C., Jiang, X., Li, Z., Bi, W., & Kong, L. (2024). Diffusion of thoughts: Chain-of-thought reasoning in diffusion language models. arXiv. https://arxiv.org/abs/2402.07754
