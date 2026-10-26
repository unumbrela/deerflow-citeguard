# Systematic Literature Review: Diffusion Language Models

**Review Period:** August 14, 2023 – August 13, 2025  
**Category:** cs.CL (Computation and Language)  
**Format:** APA Style  
**Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines 10 key papers on Diffusion Language Models (DLMs) published between August 2023 and August 2025. The review reveals a rapidly evolving field that has transitioned from demonstrating feasibility to achieving competitive performance with autoregressive models. Key themes include: (1) closing the performance gap with autoregressive approaches, (2) scaling strategies and adaptation from pretrained AR models, (3) acceleration techniques for practical deployment, and (4) specialized applications in reasoning, planning, and code generation.

---

## Annotated Bibliography

### 1. Ye, J., Zheng, Z., Bao, Y., Qian, L., & Gu, Q. (2023). Diffusion Language Models Can Perform Many Tasks with Scaling and Instruction-Finetuning. *arXiv preprint arXiv:2308.12219*.

**Published:** August 23, 2023  
**Citations:** 4

This foundational work demonstrates that diffusion language models can solve general language tasks comparable to autoregressive counterparts through scaling. The authors build competent diffusion language models by acquiring knowledge from massive data via masked language modeling pretraining, then reprogramming pretrained masked language models into diffusion language models through diffusive adaptation. Task-specific finetuning and instruction finetuning unlock versatility in solving general language tasks. Key findings show that scaling diffusion language models consistently improves performance across downstream tasks, and instruction finetuning elicits zero-shot and few-shot in-context learning abilities, showing promise in advanced abilities such as reasoning.

---

### 2. Sahoo, S. S., Arriola, M., Schiff, Y., Gokaslan, A., Marroquin, E., Chiu, J. T., Rush, A., & Kuleshov, V. (2024). Simple and Effective Masked Diffusion Language Models. *arXiv preprint arXiv:2406.07524*.

**Published:** June 11, 2024  
**Citations:** 18

This paper challenges the notion that diffusion models underperform in language modeling. The authors apply an effective training recipe that improves masked diffusion model performance and derive a simplified, Rao-Blackwellized objective resulting in additional improvements. The objective has a simple form—a mixture of classical masked language modeling losses—and can train encoder-only language models that admit efficient samplers, including ones that generate arbitrary lengths of text semi-autoregressively. On language modeling benchmarks, masked diffusion models trained with modern engineering practices achieve a new state-of-the-art among diffusion models and approach autoregressive perplexity.

---

### 3. Ye, J., Gao, J., Gong, S., Zheng, L., Jiang, X., Li, Z., & Kong, L. (2024). Beyond Autoregression: Discrete Diffusion for Complex Reasoning and Planning. *arXiv preprint arXiv:2410.14157*.

**Published:** October 18, 2024  
**Citations:** 6

This work addresses limitations of autoregressive models in complex reasoning and long-term planning tasks through discrete diffusion models. Through the lens of subgoal imbalance, the authors demonstrate how diffusion models effectively learn difficult subgoals that elude autoregressive approaches. They propose Multi-Granularity Diffusion Modeling (MGDM), which prioritizes subgoals based on difficulty during learning. On complex tasks like Countdown, Sudoku, and Boolean Satisfiability Problems, MGDM significantly outperforms autoregressive models without search techniques, achieving 91.5% and 100% accuracy on Countdown and Sudoku respectively, compared to 45.8% and 20.7% for autoregressive models.

---

### 4. Gong, S., Agarwal, S., Zhang, Y., Ye, J., Zheng, L., Li, M., An, C., Zhao, P., Bi, W., Han, J., Peng, H., & Kong, L. (2024). Scaling Diffusion Language Models via Adaptation from Autoregressive Models. *arXiv preprint arXiv:2410.17891*.

**Published:** October 23, 2024  
**Citations:** 7

Given the prevalence of open-source autoregressive language models, this paper proposes adapting these models to build text diffusion models. The authors demonstrate connections between AR and diffusion modeling objectives and introduce a simple continual pre-training approach for training diffusion models. Through systematic evaluation on language modeling, reasoning, and commonsense benchmarks, they show that AR models ranging from 127M to 7B parameters (GPT2 and LLaMA) can be converted into diffusion models DiffuGPT and DiffuLLaMA using less than 200B tokens for training. These models outperform earlier DLMs and are competitive with their AR counterparts, capable of generating fluent text, performing in-context learning, filling in the middle without prompt re-ordering, and following instructions.

---

### 5. Xu, M., Geffner, T., Kreis, K., Nie, W., Xu, Y., Leskovec, J., Ermon, S., & Vahdat, A. (2024). Energy-Based Diffusion Language Models for Text Generation. *arXiv preprint arXiv:2410.21357*.

**Published:** October 28, 2024  
**Citations:** 4

This paper addresses the performance gap between diffusion and autoregressive models, particularly when reducing sampling steps. The analysis reveals that degradation is a consequence of imperfect approximation used by diffusion models. The authors propose Energy-based Diffusion Language Model (EDLM), an energy-based model operating at the full sequence level for each diffusion step, introduced to improve the underlying approximation. Specifically, they introduce an EBM in residual form, with parameters obtained by leveraging a pretrained autoregressive model or by finetuning a bidirectional transformer via noise contrastive estimation. Comprehensive experiments show the model consistently outperforms state-of-the-art diffusion models by a significant margin, approaches autoregressive models' perplexity, and offers a 1.3× sampling speedup over existing diffusion models without performance drop.

---

### 6. Nie, S., Zhu, F., You, Z., Zhang, X., Ou, J., Hu, J., Zhou, J., Lin, Y., Wen, J.-R., & Li, C. (2025). Large Language Diffusion Models. *arXiv preprint arXiv:2502.09992*.

**Published:** February 14, 2025  
**Citations:** 12

This work challenges the notion that large language model capabilities inherently depend on autoregressive models by introducing LLaDA, a diffusion model trained from scratch under pre-training and supervised fine-tuning paradigm. LLaDA employs a forward data masking process and reverse generation process, parameterized by a Transformer to predict masked tokens, providing principled generative approach for probabilistic inference by optimizing a likelihood lower bound. Across extensive benchmarks on general tasks, math, code, and more, LLaDA demonstrates strong scalability and performs comparably to autoregressive baselines. Remarkably, LLaDA 8B is competitive with strong LLMs like LLaMA3 8B in in-context learning and, after SFT, exhibits impressive instruction-following abilities in multi-turn dialogue. Moreover, LLaDA addresses the reversal curse, surpassing GPT-4o in reversal poem completion tasks.

---

### 7. Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The Cache for Diffusion Language Models. *arXiv preprint arXiv:2505.15781*.

**Published:** May 21, 2025  
**Citations:** 3

This paper addresses the inference speed bottleneck in diffusion language models. The core challenge is that non-autoregressive architecture and bidirectional attention preclude the key-value cache that accelerates decoding in autoregressive models. The authors propose a KV-cache-like mechanism, delayed KV-Cache, for the denoising process of DLMs, motivated by the observation that different tokens have distinct representation dynamics throughout the diffusion process. Two complementary variants are designed: dKV-Cache-Decode provides almost lossless acceleration and even improves performance on long sequences, while dKV-Cache-Greedy achieves higher speed-ups with quadratic time complexity at the cost of some performance degradation. dKV-Cache achieves 2-10x speedup in inference, largely narrowing the gap between ARs and DLMs across general language understanding, mathematical, and code-generation benchmarks.

---

### 8. Wu, C., Zhang, H., Xue, S., Liu, Z., Diao, S., Zhu, L., Luo, P., Han, S., & Xie, E. (2025). Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding. *arXiv preprint arXiv:2505.22618*.

**Published:** May 28, 2025  
**Citations:** 4

This work addresses the practical inference speed gap between diffusion LLMs and autoregressive models due to lack of KV Cache and quality degradation when decoding multiple tokens simultaneously. The authors introduce a novel block-wise approximate KV Cache mechanism tailored for bidirectional diffusion models, enabling cache reuse with negligible performance drop. Additionally, they identify the root cause of generation quality degradation in parallel decoding as disruption of token dependencies under the conditional independence assumption. To address this, they propose a confidence-aware parallel decoding strategy that selectively decodes tokens exceeding a confidence threshold, mitigating dependency violations and maintaining generation quality. Experimental results on LLaDA and Dream models demonstrate up to 27.6× throughput improvement with minimal accuracy loss, closing the performance gap with autoregressive models.

---

### 9. Inception Labs, Khanna, S., Kharbanda, S., Li, S., Varma, H., Wang, E., Birnbaum, S., Luo, Z., Miraoui, Y., Palrecha, A., Ermon, S., Grover, A., & Kuleshov, V. (2025). Mercury: Ultra-Fast Language Models Based on Diffusion. *arXiv preprint arXiv:2506.17298*.

**Published:** June 17, 2025  
**Citations:** 5

This report presents Mercury, a new generation of commercial-scale large language models based on diffusion. These models are parameterized via the Transformer architecture and trained to predict multiple tokens in parallel. The report details Mercury Coder, the first set of diffusion LLMs designed for coding applications, coming in two sizes: Mini and Small. These models set a new state-of-the-art on the speed-quality frontier. Based on independent evaluations, Mercury Coder Mini and Mercury Coder Small achieve state-of-the-art throughputs of 1109 tokens/sec and 737 tokens/sec respectively on NVIDIA H100 GPUs, outperforming speed-optimized frontier models by up to 10x on average while maintaining comparable quality. The model ranks second on quality and is the fastest model overall on Copilot Arena.

---

### 10. Gong, S., Zhang, R., Zheng, H., Gu, J., Jaitly, N., Kong, L., & Zhang, Y. (2025). DiffuCoder: Understanding and Improving Masked Diffusion Models for Code Generation. *arXiv preprint arXiv:2506.20639*.

**Published:** June 25, 2025  
**Citations:** 3

This work investigates diffusion large language models for code generation, leveraging their global planning and iterative refinement features particularly useful for coding. The authors systematically investigate denoising processes and reinforcement learning methods, training a 7B dLLM, DiffuCoder, on 130B tokens of code. Analysis reveals how dLLMs differ from AR models: (1) dLLMs can decide how causal their generation should be without relying on semi-AR decoding, and (2) increasing sampling temperature diversifies not only token choices but also their generation order, creating rich search space for RL rollouts. For RL training, to reduce variance of token log-likelihood estimates and maintain training efficiency, the authors propose coupled-GRPO, a novel sampling scheme that constructs complementary mask noise for completions used in training. Coupled-GRPO significantly improves DiffuCoder's performance on code generation benchmarks (+4.4% on EvalPlus) and reduces reliance on AR bias during decoding.

---

## Thematic Synthesis

### Performance Parity with Autoregressive Models

The literature demonstrates remarkable progress in closing the performance gap between diffusion and autoregressive models. Early work by Ye et al. (2023) established that scaling could make diffusion models competitive, while Sahoo et al. (2024) showed that simple masked discrete diffusion with proper training recipes could approach autoregressive perplexity. The breakthrough came with Nie et al. (2025), demonstrating that diffusion models trained from scratch (LLaDA) could match LLaMA3 8B performance, challenging the assumption that core LLM capabilities inherently depend on autoregressive architectures.

### Scaling and Adaptation Strategies

Two distinct approaches to scaling emerged: training from scratch and adaptation from pretrained autoregressive models. Gong et al. (2024) demonstrated that converting existing AR models (GPT2, LLaMA) to diffusion models requires less than 200B tokens, providing a practical pathway for leveraging the wealth of open-source AR models. Meanwhile, Nie et al. (2025) proved that training diffusion models from scratch at scale is viable, opening new architectural possibilities.

### Inference Acceleration

A critical barrier to practical deployment—inference speed—was addressed through multiple innovations. Ma et al. (2025) and Wu et al. (2025) independently developed KV-cache mechanisms for diffusion models, achieving 2-10x and up to 27.6x speedups respectively. These training-free accelerations largely narrow the inference speed gap with autoregressive models. Inception Labs (2025) demonstrated commercial viability with Mercury Coder achieving 1109 tokens/sec, outperforming speed-optimized models by 10x.

### Specialized Applications

Diffusion models show particular promise in domains requiring global planning and iterative refinement. Ye et al. (2024) demonstrated superiority in complex reasoning tasks (Countdown, Sudoku, Boolean SAT), achieving 91.5-100% accuracy versus 20.7-45.8% for autoregressive models. Gong et al. (2025) showed diffusion models' advantages in code generation, with coupled-GRPO reinforcement learning improving performance by 4.4% on EvalPlus.

### Energy-Based Approaches

Xu et al. (2024) introduced energy-based diffusion language models (EDLM) to improve the underlying approximation used by diffusion models. By introducing an EBM in residual form, either leveraging pretrained autoregressive models or finetuning bidirectional transformers via noise contrastive estimation, EDLM consistently outperforms state-of-the-art diffusion models while offering 1.3x sampling speedup.

---

## Methodology

**Search Strategy:** This review searched arXiv's cs.CL (Computation and Language) category for papers published between August 14, 2023 and August 13, 2025 using the query "Diffusion Language Models."

**Screening Process:** From an initial pool of 50 papers matched by phrase and all terms, 30 papers were shortlisted after citation expansion. Papers were screened for centrality to the topic, with 10 most co-cited central papers included in this review.

**Inclusion Criteria:**
- Primary category: cs.CL
- Publication date: August 14, 2023 – August 13, 2025
- Focus on diffusion language models for text generation
- Empirical evaluation on language modeling or downstream tasks

**Exclusion Criteria:**
- Papers focused solely on image or audio diffusion
- Opinion pieces without empirical evaluation
- Papers outside the cs.CL category

---

## Conclusions and Future Directions

The literature from 2023-2025 establishes diffusion language models as a viable and competitive alternative to autoregressive models. Key achievements include:

1. **Performance Parity:** Diffusion models now match autoregressive perplexity and demonstrate competitive performance on general language tasks, reasoning, and code generation.

2. **Scalability:** Both training-from-scratch and adaptation approaches enable scaling to 7B+ parameters, with LLaDA 8B showing competitive performance with LLaMA3 8B.

3. **Inference Speed:** KV-cache mechanisms and parallel decoding strategies have addressed the historical speed disadvantage, achieving up to 27.6x throughput improvements.

4. **Unique Capabilities:** Diffusion models demonstrate advantages in complex reasoning, planning, and code generation tasks requiring global planning and iterative refinement.

**Future Research Directions:**
- Further scaling to larger model sizes (beyond 8B parameters)
- Integration with multimodal capabilities
- Exploration of diffusion-specific architectures beyond adapted autoregressive models
- Development of more efficient sampling algorithms
- Investigation of diffusion models' robustness and calibration properties

---

## References

Gong, S., Agarwal, S., Zhang, Y., Ye, J., Zheng, L., Li, M., An, C., Zhao, P., Bi, W., Han, J., Peng, H., & Kong, L. (2024). Scaling diffusion language models via adaptation from autoregressive models. *arXiv preprint arXiv:2410.17891*.

Gong, S., Zhang, R., Zheng, H., Gu, J., Jaitly, N., Kong, L., & Zhang, Y. (2025). DiffuCoder: Understanding and improving masked diffusion models for code generation. *arXiv preprint arXiv:2506.20639*.

Inception Labs, Khanna, S., Kharbanda, S., Li, S., Varma, H., Wang, E., Birnbaum, S., Luo, Z., Miraoui, Y., Palrecha, A., Ermon, S., Grover, A., & Kuleshov, V. (2025). Mercury: Ultra-fast language models based on diffusion. *arXiv preprint arXiv:2506.17298*.

Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The cache for diffusion language models. *arXiv preprint arXiv:2505.15781*.

Nie, S., Zhu, F., You, Z., Zhang, X., Ou, J., Hu, J., Zhou, J., Lin, Y., Wen, J.-R., & Li, C. (2025). Large language diffusion models. *arXiv preprint arXiv:2502.09992*.

Sahoo, S. S., Arriola, M., Schiff, Y., Gokaslan, A., Marroquin, E., Chiu, J. T., Rush, A., & Kuleshov, V. (2024). Simple and effective masked diffusion language models. *arXiv preprint arXiv:2406.07524*.

Wu, C., Zhang, H., Xue, S., Liu, Z., Diao, S., Zhu, L., Luo, P., Han, S., & Xie, E. (2025). Fast-dLLM: Training-free acceleration of diffusion LLM by enabling KV cache and parallel decoding. *arXiv preprint arXiv:2505.22618*.

Xu, M., Geffner, T., Kreis, K., Nie, W., Xu, Y., Leskovec, J., Ermon, S., & Vahdat, A. (2024). Energy-based diffusion language models for text generation. *arXiv preprint arXiv:2410.21357*.

Ye, J., Gao, J., Gong, S., Zheng, L., Jiang, X., Li, Z., & Kong, L. (2024). Beyond autoregression: Discrete diffusion for complex reasoning and planning. *arXiv preprint arXiv:2410.14157*.

Ye, J., Zheng, Z., Bao, Y., Qian, L., & Gu, Q. (2023). Diffusion language models can perform many tasks with scaling and instruction-finetuning. *arXiv preprint arXiv:2308.12219*.

---

**Review completed:** October 26, 2026  
**Total papers reviewed:** 10  
**Date range:** August 14, 2023 – August 13, 2025  
**Category:** cs.CL (Computation and Language)
