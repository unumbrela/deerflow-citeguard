# Systematic Literature Review: Diffusion Language Models

**Review Period:** August 14, 2023 – August 13, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Total Papers:** 10  
**Retrieval Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in Diffusion Language Models (DLMs) from August 2023 to August 2025. The reviewed papers demonstrate significant progress in addressing core challenges of DLMs, including inference speed, reasoning capabilities, controllability, and quality-diversity trade-offs. Key contributions include novel caching mechanisms (dKV-Cache), reasoning frameworks (Diffusion Chain of Lateral Thought), one-step generation methods (DLM-One), and architectural innovations (Anchored DLMs). The collective research indicates that DLMs are emerging as viable alternatives to autoregressive models, offering parallel generation and bidirectional context while narrowing performance gaps through scaling, instruction fine-tuning, and architectural improvements.

---

## Annotated Bibliography (APA Format)

### 1. Ye, J., Zheng, Z., Bao, Y., Qian, L., & Gu, Q. (2023). Diffusion Language Models Can Perform Many Tasks with Scaling and Instruction-Finetuning. *arXiv preprint arXiv:2308.12219v3*. https://arxiv.org/abs/2308.12219v3

**Summary:** This foundational paper demonstrates that diffusion language models can achieve strong performance across general language tasks through scaling and instruction fine-tuning. The authors propose a two-stage approach: (1) masked language modeling pretraining on massive data, followed by (2) diffusive adaptation with task-specific and instruction fine-tuning. Key findings show that scaling DLMs consistently improves downstream task performance, and instruction fine-tuning elicits zero-shot and few-shot in-context learning abilities. The paper establishes that DLMs can tackle unseen tasks through natural language instructions and shows promise in reasoning capabilities.

**Key Contributions:**
- First comprehensive demonstration of DLMs performing general language tasks comparable to autoregressive models
- Introduced diffusive adaptation framework for reprogramming pretrained masked language models
- Showed instruction fine-tuning enables zero-shot and few-shot learning in DLMs

---

### 2. Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The Cache for Diffusion Language Models. *arXiv preprint arXiv:2505.15781v1*. https://arxiv.org/abs/2505.15781v1

**Summary:** This paper addresses the critical inference speed bottleneck in DLMs by proposing dKV-Cache, a delayed KV-cache mechanism for the denoising process. The approach leverages the observation that different tokens exhibit distinct representation dynamics throughout diffusion. Two variants are introduced: dKV-Cache-Decode (lossless acceleration with improved long-sequence performance) and dKV-Cache-Greedy (aggressive caching with higher speedups). The method achieves 2-10x inference speedup in a training-free manner, significantly narrowing the gap between autoregressive models and DLMs.

**Key Contributions:**
- First KV-cache-like mechanism for diffusion language models
- Training-free acceleration method compatible with existing DLMs
- Demonstrated 2-10x speedup across language understanding, math, and code generation benchmarks

---

### 3. Huang, Z., Chen, Z., Wang, Z., Li, T., & Qi, G.-J. (2025). Reinforcing the Diffusion Chain of Lateral Thought with Diffusion Language Models. *arXiv preprint arXiv:2505.10446v3*. https://arxiv.org/abs/2505.10446v3

**Summary:** The authors introduce the Diffusion Chain of Lateral Thought (DCoLT), a reasoning framework that treats each intermediate step in the reverse diffusion process as a latent "thinking" action optimized via outcome-based reinforcement learning. Unlike traditional linear Chain-of-Thought, DCoLT enables bidirectional, non-linear reasoning without strict grammatical constraints on intermediate steps. Implemented on SEDD and LLaDA models, DCoLT achieved significant improvements: +9.8% on GSM8K, +5.7% on MATH, +11.4% on MBPP, and +19.5% on HumanEval using only public data and 16 H800 GPUs.

**Key Contributions:**
- Novel bidirectional, non-linear reasoning framework for DLMs
- Outcome-based RL optimization over entire diffusion trajectories
- State-of-the-art performance on math and code generation benchmarks

---

### 4. Kang, C., Chen, X., Hu, Y., & Novak, D. (2024). Quantized Embedding Vectors for Controllable Diffusion Language Models. *arXiv preprint arXiv:2402.10107v1*. https://arxiv.org/abs/2402.10107v1

**Summary:** This work proposes QE-CDLM (Quantized Embedding Controllable Diffusion Language Model) to address memory, computational, and portability challenges in DLMs. The approach remodels task-specific embedding spaces via quantization, enabling gradient-based control and more stable intermediate latent variables. The method incorporates adaptation fine-tuning to reduce tunable weights. Experiments on five fine-grained control tasks demonstrate superior perplexity and lightweight fine-tuning compared to existing methods.

**Key Contributions:**
- Novel quantization approach for embedding spaces in DLMs
- Improved controllability, portability, and inference speed
- Better perplexity and stability on fine-grained control tasks

---

### 5. Ye, J., Gong, S., Chen, L., Zheng, L., Gao, J., Shi, H., Wu, C., Jiang, X., Li, Z., Bi, W., & Kong, L. (2024). Diffusion of Thoughts: Chain-of-Thought Reasoning in Diffusion Language Models. *arXiv preprint arXiv:2402.07754v3*. https://arxiv.org/abs/2402.07754v3

**Summary:** This paper introduces Diffusion-of-Thought (DoT), integrating diffusion models with Chain-of-Thought reasoning. Unlike autoregressive models that reason left-to-right, DoT allows reasoning steps to diffuse over time, offering flexible computation-performance trade-offs. A small diffusion model with DoT outperformed much larger autoregressive models in efficiency and accuracy on multi-digit multiplication, boolean logic, and grade school math problems. The approach demonstrates self-correction abilities and benefits from self-consistency decoding.

**Key Contributions:**
- First integration of Chain-of-Thought with diffusion language models
- Flexible computation-performance trade-off through temporal diffusion
- Demonstrated self-correction capabilities and compatibility with reasoning-enhancement techniques

---

### 6. Rout, L., Caramanis, C., & Shakkottai, S. (2025). Anchored Diffusion Language Model. *arXiv preprint arXiv:2505.18456v1*. https://arxiv.org/abs/2505.18456v1

**Summary:** The authors identify that DLM underperformance stems from important tokens (key words, low-frequency words) being masked early in the forward process, limiting contextual information. They propose ADLM (Anchored Diffusion Language Model), a two-stage framework that first predicts distributions over important tokens via an anchor network, then predicts missing tokens conditioned on anchored predictions. ADLM achieved up to 25.4% perplexity gains on LM1B and OpenWebText, state-of-the-art zero-shot generalization across seven benchmarks, and surpassed autoregressive models in MAUVE score—the first DLM to generate better human-like text than AR models.

**Key Contributions:**
- Identified critical limitation in existing DLM architectures (early masking of important tokens)
- Novel two-stage anchoring framework with theoretical ANELBO objective
- First DLM to surpass autoregressive models in human-like text generation (MAUVE score)

---

### 7. Chen, T., Zhang, S., & Zhou, M. (2025). DLM-One: Diffusion Language Models for One-Step Sequence Generation. *arXiv preprint arXiv:2506.00290v2*. https://arxiv.org/abs/2506.00290v2

**Summary:** DLM-One introduces a score-distillation framework for one-step sequence generation with continuous DLMs, eliminating iterative refinement by aligning student model outputs with a pretrained teacher DLM's score function in forward-diffused noisy space. The architecture-agnostic framework works across standard token embedding and logit simplex spaces. Experiments demonstrate up to ~2000× speedup in sampling steps and ~500× in wall-clock time while maintaining competitive benchmark performance. The paper includes analysis of failure modes and proposes an adversarially-regularized two-stage training scheme.

**Key Contributions:**
- First one-step generation framework for continuous diffusion language models
- Architecture-agnostic approach robust across diverse continuous manifolds
- Unprecedented speedups (2000× sampling, 500× wall-clock) with maintained quality

---

### 8. Luxembourg, O., Permuter, H., & Nachmani, E. (2025). Plan for Speed: Dilated Scheduling for Masked Diffusion Language Models. *arXiv preprint arXiv:2506.19037v5*. https://arxiv.org/abs/2506.19037v5

**Summary:** This paper addresses the limitation of existing masked diffusion language model samplers that ignore token interactions when unmasking multiple positions in parallel. The proposed Dilated Unmasking Scheduler (DUS) partitions sequence positions into non-adjacent dilated groups and unmasks them in parallel to minimize joint entropy gain upper bounds at each denoising step. This inference-only, planner-model-free method achieves up to 5.8× wall-clock speedup over token-by-token decoding without modifying the underlying denoiser, while recovering performance lost under traditional parallel unmasking.

**Key Contributions:**
- Novel dilated unmasking strategy minimizing joint entropy gain
- Deterministic, predictable speedup based on block size parameter
- Drop-in post-filter compatible with adaptive samplers

---

### 9. Koh, H., Jhang, M., Kim, D., Lee, S., & Jung, K. (2024). Conditional [MASK] Discrete Diffusion Language Model. *arXiv preprint arXiv:2411.06438v5*. https://arxiv.org/abs/2411.06438v5

**Summary:** Diffusion-EAGS integrates conditional masked language models into diffusion language models through conditional Markov Random Field theory. The framework proposes entropy-adaptive Gibbs sampling and entropy-based noise scheduling to balance model shortcomings. Experimental results demonstrate superior quality-diversity tradeoff compared to baselines, effectively addressing challenges in diverse text generation and controllability that plague autoregressive models.

**Key Contributions:**
- Theoretical integration of conditional MLMs into DLMs via conditional MRF
- Entropy-adaptive Gibbs sampling for improved generation
- Best quality-diversity tradeoff among non-autoregressive methods

---

### 10. Buzzard, Z. (2025). Understanding the Quality-Diversity Trade-off in Diffusion Language Models. *arXiv preprint arXiv:2503.10683v1*. https://arxiv.org/abs/2503.10683v1

**Summary:** This work addresses the lack of natural quality-diversity control in continuous embedding space DLMs. The paper proposes classifier-free guidance and stochastic clamping techniques to manipulate the quality-diversity tradeoff on sequence-to-sequence tasks. These methods enable performance improvements comparable to temperature hyperparameter control in autoregressive models, enhancing both understanding of model performance and generation quality.

**Key Contributions:**
- First systematic approach to quality-diversity control in continuous-space DLMs
- Classifier-free guidance and stochastic clamping techniques
- Improved generation quality through controlled trade-offs

---

## Thematic Analysis

### Theme 1: Inference Speed and Efficiency
Four papers directly address DLM inference speed limitations:
- **dKV-Cache** (Ma et al., 2025): 2-10× speedup via delayed caching
- **DLM-One** (Chen et al., 2025): ~500× wall-clock speedup via one-step generation
- **Dilated Scheduling** (Luxembourg et al., 2025): 5.8× speedup via parallel unmasking
- **QE-CDLM** (Kang et al., 2024): Accelerated convergence via quantized embeddings

### Theme 2: Reasoning Capabilities
Three papers focus on enhancing reasoning:
- **DCoLT** (Huang et al., 2025): Bidirectional, non-linear reasoning with RL optimization
- **DoT** (Ye et al., 2024): Temporal diffusion of reasoning steps
- **ADLM** (Rout et al., 2025): Improved reasoning through anchoring important tokens

### Theme 3: Controllability and Quality
Three papers address generation control:
- **Diffusion-EAGS** (Koh et al., 2024): Entropy-adaptive control for quality-diversity
- **Quality-Diversity Trade-off** (Buzzard, 2025): Classifier-free guidance for control
- **QE-CDLM** (Kang et al., 2024): Gradient-based control via quantization

### Theme 4: Foundational Capabilities
- **Scaling and Instruction-Finetuning** (Ye et al., 2023): Established DLMs as viable general-purpose language learners

---

## Chronological Timeline

| Date | Paper | Key Innovation |
|------|-------|----------------|
| Aug 2023 | Ye et al. | Scaling + instruction fine-tuning for general tasks |
| Feb 2024 | Ye, J. et al. | Diffusion-of-Thought reasoning framework |
| Feb 2024 | Kang et al. | Quantized embeddings for controllability |
| Nov 2024 | Koh et al. | Conditional MRF + entropy-adaptive sampling |
| Mar 2025 | Buzzard | Quality-diversity control mechanisms |
| May 2025 | Huang et al. | DCoLT: RL-optimized lateral thought |
| May 2025 | Ma et al. | dKV-Cache for inference acceleration |
| May 2025 | Rout et al. | Anchored DLM architecture |
| May 2025 | Chen et al. | DLM-One: one-step generation |
| Jun 2025 | Luxembourg et al. | Dilated unmasking scheduler |

---

## Key Findings and Trends

1. **Speed Gap Closing:** Multiple approaches (dKV-Cache, DLM-One, DUS) demonstrate that DLM inference speed can approach or exceed autoregressive models through architectural innovations and caching strategies.

2. **Reasoning Superiority:** DLMs' bidirectional, non-linear reasoning capabilities (DCoLT, DoT) offer advantages over linear autoregressive reasoning, particularly in math and code generation tasks.

3. **Quality Parity:** ADLM (Rout et al., 2025) achieved the first instance of a DLM surpassing autoregressive models in human-like text generation (MAUVE score), marking a significant milestone.

4. **Training-Free Acceleration:** Several methods (dKV-Cache, DUS) provide speedups without model retraining, enabling immediate deployment benefits.

5. **Controllability Advances:** Quantization, entropy-adaptive sampling, and classifier-free guidance provide DLMs with fine-grained control comparable to temperature-based control in autoregressive models.

---

## Research Gaps and Future Directions

1. **Unified Framework:** No single approach combines all advantages (speed, reasoning, quality, controllability) into one framework.

2. **Theoretical Understanding:** Limited theoretical analysis of why diffusion processes excel at certain reasoning tasks compared to autoregressive generation.

3. **Scalability:** Most papers evaluate on models up to billions of parameters; scaling behavior at trillion-parameter scale remains unexplored.

4. **Multilingual Performance:** All benchmarks focus on English; multilingual DLM capabilities are underexamined.

5. **Real-World Deployment:** Limited discussion of production deployment challenges beyond inference speed (memory footprint, energy efficiency, latency guarantees).

---

## Conclusion

The systematic review of 10 papers from August 2023 to August 2025 reveals rapid maturation of Diffusion Language Models as viable alternatives to autoregressive models. Key breakthroughs in inference speed (up to 500× wall-clock acceleration), reasoning capabilities (bidirectional, RL-optimized thought processes), and generation quality (surpassing AR models in MAUVE scores) demonstrate that DLMs are no longer theoretical curiosities but practical solutions for natural language generation. The diversity of approaches—ranging from caching mechanisms and one-step distillation to anchoring architectures and entropy-adaptive sampling—indicates a healthy, rapidly evolving research landscape. Future work should focus on unified frameworks combining these advances, theoretical understanding of diffusion advantages, and production-ready deployments at scale.

---

## References

Buzzard, Z. (2025). Understanding the quality-diversity trade-off in diffusion language models. *arXiv preprint arXiv:2503.10683v1*. https://arxiv.org/abs/2503.10683v1

Chen, T., Zhang, S., & Zhou, M. (2025). DLM-One: Diffusion language models for one-step sequence generation. *arXiv preprint arXiv:2506.00290v2*. https://arxiv.org/abs/2506.00290v2

Huang, Z., Chen, Z., Wang, Z., Li, T., & Qi, G.-J. (2025). Reinforcing the diffusion chain of lateral thought with diffusion language models. *arXiv preprint arXiv:2505.10446v3*. https://arxiv.org/abs/2505.10446v3

Kang, C., Chen, X., Hu, Y., & Novak, D. (2024). Quantized embedding vectors for controllable diffusion language models. *arXiv preprint arXiv:2402.10107v1*. https://arxiv.org/abs/2402.10107v1

Koh, H., Jhang, M., Kim, D., Lee, S., & Jung, K. (2024). Conditional [MASK] discrete diffusion language model. *arXiv preprint arXiv:2411.06438v5*. https://arxiv.org/abs/2411.06438v5

Luxembourg, O., Permuter, H., & Nachmani, E. (2025). Plan for speed: Dilated scheduling for masked diffusion language models. *arXiv preprint arXiv:2506.19037v5*. https://arxiv.org/abs/2506.19037v5

Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The cache for diffusion language models. *arXiv preprint arXiv:2505.15781v1*. https://arxiv.org/abs/2505.15781v1

Rout, L., Caramanis, C., & Shakkottai, S. (2025). Anchored diffusion language model. *arXiv preprint arXiv:2505.18456v1*. https://arxiv.org/abs/2505.18456v1

Ye, J., Gong, S., Chen, L., Zheng, L., Gao, J., Shi, H., Wu, C., Jiang, X., Li, Z., Bi, W., & Kong, L. (2024). Diffusion of thoughts: Chain-of-thought reasoning in diffusion language models. *arXiv preprint arXiv:2402.07754v3*. https://arxiv.org/abs/2402.07754v3

Ye, J., Zheng, Z., Bao, Y., Qian, L., & Gu, Q. (2023). Diffusion language models can perform many tasks with scaling and instruction-finetuning. *arXiv preprint arXiv:2308.12219v3*. https://arxiv.org/abs/2308.12219v3
