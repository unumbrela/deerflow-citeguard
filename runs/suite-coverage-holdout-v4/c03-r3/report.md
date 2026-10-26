# Systematic Literature Review: Diffusion Language Models

**Date:** October 26, 2026  
**Review Period:** August 14, 2023 – August 13, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Format:** APA Style

---

## Executive Summary

This systematic literature review examines 10 key papers on Diffusion Language Models (DLMs) published between August 2023 and August 2025. The review reveals rapid advancement in diffusion-based approaches to language modeling, challenging the long-held assumption that autoregressive models are inherently superior for language tasks. Key themes include: (1) demonstrating competitive performance with autoregressive models, (2) scaling diffusion models to large language model sizes, (3) improving inference speed through novel caching mechanisms, (4) applying diffusion models to complex reasoning and code generation tasks, and (5) integrating reinforcement learning for enhanced reasoning capabilities.

---

## Methodology

**Search Strategy:** Papers were identified through arXiv search in the cs.CL (Computational Linguistics) category with the query "diffusion language models." The search included papers published between August 14, 2023, and August 13, 2025.

**Selection Criteria:** Papers were screened based on their focus on diffusion models applied to language modeling tasks. The screening process identified 30 shortlisted papers from a pool of 50, with the 10 most central papers selected for this review based on citation impact and relevance to core DLM research.

**Screening Results:** 
- Initial pool: 50 papers
- After citation expansion: 105 papers (55 added from references)
- Shortlisted: 30 papers
- Final selection: 10 papers
- Inclusion rate: 33.3% of shortlisted papers

---

## Annotated Bibliography

### 1. Sahoo, S. S., Arriola, M., Schiff, Y., Gokaslan, A., Marroquin, E., Chiu, J. T., Rush, A., & Kuleshov, V. (2024). Simple and effective masked diffusion language models. *arXiv preprint arXiv:2406.07524*. https://arxiv.org/abs/2406.07524v2

**Summary:** This foundational work demonstrates that simple masked discrete diffusion models can achieve performance comparable to autoregressive models when trained with modern engineering practices. The authors introduce a Rao-Blackwellized objective that simplifies the training process to a mixture of classical masked language modeling losses. Their approach enables encoder-only language models with efficient samplers capable of generating arbitrary-length text semi-autoregressively.

**Key Contributions:** 
- Simplified training objective for masked diffusion models
- State-of-the-art performance among diffusion models on language modeling benchmarks
- Approaches autoregressive perplexity levels
- Open-source implementation with comprehensive documentation

**Citation Impact:** 18 citations (highest in the selected set)

---

### 2. Nie, S., Zhu, F., You, Z., Zhang, X., Ou, J., Hu, J., Zhou, J., Lin, Y., Wen, J.-R., & Li, C. (2025). Large language diffusion models. *arXiv preprint arXiv:2502.09992*. https://arxiv.org/abs/2502.09992v3

**Summary:** This paper introduces LLaDA, a diffusion model trained from scratch under pre-training and supervised fine-tuning paradigms, challenging the notion that large language model capabilities inherently depend on autoregressive architectures. LLaDA employs a forward data masking process and reverse generation process parameterized by a Transformer. The 8B model demonstrates competitive performance with LLaMA3 8B in in-context learning and exhibits strong instruction-following abilities after SFT.

**Key Contributions:**
- First diffusion model trained from scratch at scale (8B parameters)
- Addresses the reversal curse, surpassing GPT-4o in reversal poem completion
- Demonstrates scalability across general tasks, math, and code
- Challenges the assumption that core LLM capabilities require autoregressive models

**Citation Impact:** 12 citations

---

### 3. Gong, S., Agarwal, S., Zhang, Y., Ye, J., Zheng, L., Li, M., An, C., Zhao, P., Bi, W., Han, J., Peng, H., & Kong, L. (2024). Scaling diffusion language models via adaptation from autoregressive models. *arXiv preprint arXiv:2410.17891*. https://arxiv.org/abs/2410.17891v3

**Summary:** This work addresses the challenge of training diffusion models at scale by proposing adaptation from existing autoregressive models. The authors demonstrate connections between AR and diffusion modeling objectives and introduce a continual pre-training approach. They successfully convert AR models (GPT2 and LLaMA) ranging from 127M to 7B parameters into diffusion models using less than 200B tokens.

**Key Contributions:**
- Novel adaptation approach from AR to diffusion models
- Systematic evaluation showing competitive performance with AR counterparts
- Release of DiffuGPT and DiffuLLaMA model suite (127M-355M-7B)
- Capabilities include in-context learning, fill-in-the-middle, and instruction following

**Citation Impact:** 7 citations

---

### 4. Ye, J., Gao, J., Gong, S., Zheng, L., Jiang, X., Li, Z., & Kong, L. (2024). Beyond autoregression: Discrete diffusion for complex reasoning and planning. *arXiv preprint arXiv:2410.14157*. https://arxiv.org/abs/2410.14157v3

**Summary:** This paper identifies limitations of autoregressive models in complex reasoning and long-term planning tasks, proposing discrete diffusion models as a solution. Through the lens of subgoal imbalance, the authors demonstrate how diffusion models effectively learn difficult subgoals. They introduce Multi-Granularity Diffusion Modeling (MGDM), which prioritizes subgoals based on difficulty during learning.

**Key Contributions:**
- MGDM framework for complex reasoning tasks
- Significant outperformance of AR models without search: 91.5% vs 45.8% on Countdown, 100% vs 20.7% on Sudoku
- Demonstrates diffusion models' superiority for sophisticated problem-solving
- Open-source implementation available

**Citation Impact:** 6 citations

---

### 5. Inception Labs, Khanna, S., Kharbanda, S., Li, S., Varma, H., Wang, E., Birnbaum, S., Luo, Z., Miraoui, Y., Palrecha, A., Ermon, S., Grover, A., & Kuleshov, V. (2025). Mercury: Ultra-fast language models based on diffusion. *arXiv preprint arXiv:2506.17298*. https://arxiv.org/abs/2506.17298v1

**Summary:** This industry report presents Mercury, a commercial-scale diffusion LLM family designed for coding applications. Mercury Coder models achieve state-of-the-art speed-quality performance, with Mini and Small variants reaching 1109 and 737 tokens/sec respectively on NVIDIA H100 GPUs—outperforming speed-optimized frontier models by up to 10x while maintaining comparable quality.

**Key Contributions:**
- First commercial-scale diffusion LLMs for production use
- Unprecedented inference speeds (10x faster than optimized AR models)
- Real-world validation through Copilot Arena (second on quality, fastest overall)
- Public API and playground deployment

**Citation Impact:** 5 citations

---

### 6. Xu, M., Geffner, T., Kreis, K., Nie, W., Xu, Y., Leskovec, J., Ermon, S., & Vahdat, A. (2024). Energy-based diffusion language models for text generation. *arXiv preprint arXiv:2410.21357*. https://arxiv.org/abs/2410.21357v4

**Summary:** This work addresses the performance gap between diffusion and autoregressive models, particularly when reducing sampling steps. The authors propose Energy-based Diffusion Language Model (EDLM), operating at the full sequence level for each diffusion step. The energy-based model is introduced in residual form, leveraging pretrained autoregressive models or finetuning bidirectional transformers via noise contrastive estimation.

**Key Contributions:**
- EDLM framework with sequence-level energy-based modeling
- Consistent outperformance of state-of-the-art diffusion models
- Approaches autoregressive perplexity levels
- 1.3× sampling speedup without performance degradation

**Citation Impact:** 4 citations

---

### 7. Wu, C., Zhang, H., Xue, S., Liu, Z., Diao, S., Zhu, L., Luo, P., Han, S., & Xie, E. (2025). Fast-dLLM: Training-free acceleration of diffusion LLM by enabling KV cache and parallel decoding. *arXiv preprint arXiv:2505.22618*. https://arxiv.org/abs/2505.22618v3

**Summary:** This paper addresses the practical inference speed limitations of diffusion LLMs compared to autoregressive models. The authors introduce a block-wise approximate KV Cache mechanism for bidirectional diffusion models and identify token dependency disruption as the root cause of quality degradation in parallel decoding. They propose confidence-aware parallel decoding to selectively decode tokens exceeding confidence thresholds.

**Key Contributions:**
- Novel KV Cache mechanism for diffusion models (training-free)
- Up to 27.6× throughput improvement with minimal accuracy loss
- Confidence-aware parallel decoding strategy
- Closes performance gap with autoregressive models for practical deployment

**Citation Impact:** 4 citations

---

### 8. Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The cache for diffusion language models. *arXiv preprint arXiv:2505.15781*. https://arxiv.org/abs/2505.15781v1

**Summary:** This work tackles the inference speed bottleneck in diffusion language models caused by their non-autoregressive architecture and bidirectional attention, which preclude traditional key-value caching. The authors propose delayed KV-Cache (dKV-Cache), motivated by the observation that different tokens have distinct representation dynamics throughout the diffusion process.

**Key Contributions:**
- dKV-Cache-Decode: Lossless acceleration with improved long-sequence performance
- dKV-Cache-Greedy: Aggressive caching with 2-10× speedup
- Training-free implementation compatible with existing DLMs
- Demonstrates that caching is viable for diffusion language models

**Citation Impact:** 3 citations

---

### 9. Gong, S., Zhang, R., Zheng, H., Gu, J., Jaitly, N., Kong, L., & Zhang, Y. (2025). DiffuCoder: Understanding and improving masked diffusion models for code generation. *arXiv preprint arXiv:2506.20639*. https://arxiv.org/abs/2506.20639v2

**Summary:** This systematic investigation examines the denoising processes and reinforcement learning methods for diffusion large language models in code generation. The authors train DiffuCoder, a 7B dLLM on 130B tokens of code, revealing unique decoding behaviors: dLLMs can decide generation causality without semi-AR decoding, and temperature increases diversify both token choices and generation order.

**Key Contributions:**
- Comprehensive analysis of dLLM decoding behavior in code generation
- Coupled-GRPO: Novel sampling scheme for RL training reducing variance
- 7B DiffuCoder model trained on 130B code tokens
- +4.4% improvement on EvalPlus benchmark with reduced AR bias reliance

**Citation Impact:** 3 citations

---

### 10. Zhao, S., Gupta, D., Zheng, Q., & Grover, A. (2025). d1: Scaling reasoning in diffusion large language models via reinforcement learning. *arXiv preprint arXiv:2504.12216*. https://arxiv.org/abs/2504.12216v2

**Summary:** This paper explores whether diffusion-based LLMs can leverage recent advances in LLM reasoning through online reinforcement learning, a capability previously demonstrated primarily in autoregressive models. The authors propose d1, a framework adapting pretrained masked dLLMs into reasoning models through masked SFT for knowledge distillation and diffu-GRPO, a critic-free policy-gradient RL algorithm.

**Key Contributions:**
- First integration of policy gradient methods to masked dLLMs
- Masked SFT technique for knowledge distillation and self-improvement
- Diffu-GRPO: Novel critic-free RL algorithm for diffusion models
- Significant performance improvements on mathematical and planning benchmarks

**Citation Impact:** 3 citations

---

## Thematic Analysis

### Theme 1: Performance Parity with Autoregressive Models

Multiple studies demonstrate that diffusion language models can achieve performance comparable to autoregressive models when properly trained. Sahoo et al. (2024) showed that simple masked diffusion approaches with modern engineering practices approach AR perplexity. Nie et al. (2025) provided stronger evidence with LLaDA 8B, competitive with LLaMA3 8B. Gong et al. (2024) further validated this through adaptation approaches, showing DLMs can match their AR counterparts across language modeling, reasoning, and commonsense benchmarks.

### Theme 2: Scaling and Training Efficiency

The field has made significant progress in scaling diffusion models. Two primary approaches have emerged: training from scratch (Nie et al., 2025) and adaptation from existing AR models (Gong et al., 2024). The adaptation approach proves particularly efficient, requiring less than 200B tokens to convert AR models up to 7B parameters. This addresses the historical challenge of training diffusion models at scale.

### Theme 3: Inference Speed Optimization

A critical bottleneck for DLMs has been inference speed. Three papers address this through caching mechanisms: Wu et al. (2025) introduced block-wise approximate KV Cache achieving 27.6× throughput improvement; Ma et al. (2025) proposed dKV-Cache with 2-10× speedup; and Inception Labs (2025) demonstrated commercial viability with Mercury achieving 10× speedup over optimized AR models. These advances largely close the speed gap that previously hindered practical deployment.

### Theme 4: Specialized Applications

Diffusion models show particular promise in specialized domains. For complex reasoning, Ye et al. (2024) demonstrated superiority over AR models in tasks like Countdown (91.5% vs 45.8%) and Sudoku (100% vs 20.7%). For code generation, Gong et al. (2025) trained DiffuCoder on 130B tokens, revealing unique capabilities in global planning and iterative refinement. The reinforcement learning integration by Zhao et al. (2025) further enhances reasoning capabilities through diffu-GRPO.

### Theme 5: Novel Training Paradigms

Energy-based approaches (Xu et al., 2024) and reinforcement learning integration (Gong et al., 2025; Zhao et al., 2025) represent novel training paradigms specific to diffusion models. These approaches leverage the unique characteristics of diffusion processes, such as coarse-to-fine generation and diverse generation orders, to achieve capabilities beyond what AR models can offer.

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Multilingual Capabilities:** None of the reviewed papers extensively evaluate DLMs on multilingual tasks, leaving open questions about cross-lingual transfer and non-English language performance.

2. **Long-Context Understanding:** While caching mechanisms improve speed, systematic evaluation of DLMs on long-context tasks (10K+ tokens) remains limited.

3. **Theoretical Foundations:** The theoretical understanding of why diffusion models excel at certain reasoning tasks (Ye et al., 2024) requires deeper investigation.

4. **Energy Efficiency:** Despite speed improvements, comprehensive analysis of computational efficiency and environmental impact compared to AR models is absent.

### Future Research Directions

1. **Hybrid Architectures:** Combining autoregressive and diffusion approaches may leverage strengths of both paradigms.

2. **Domain-Specific DLMs:** Specialized models for scientific, legal, or medical domains could benefit from diffusion's iterative refinement capabilities.

3. **Real-Time Applications:** With speed improvements, exploring real-time applications like conversational AI and interactive code completion warrants investigation.

4. **Theoretical Analysis:** Deeper theoretical work on the relationship between diffusion processes and reasoning capabilities could guide future model design.

---

## Conclusion

The systematic review of diffusion language models from 2023-2025 reveals a rapidly maturing field that has overcome initial performance limitations to achieve parity with autoregressive models. Key advances include:

- **Performance:** DLMs now match AR models on standard benchmarks while excelling at complex reasoning tasks
- **Scale:** Successful training and adaptation of models up to 8B parameters
- **Speed:** Inference acceleration through novel caching mechanisms enables practical deployment
- **Applications:** Superior performance in code generation, mathematical reasoning, and planning tasks
- **Training:** Novel paradigms including energy-based modeling and reinforcement learning integration

The field has transitioned from proving feasibility to demonstrating practical utility, with commercial deployments like Mercury Coder validating real-world applicability. Future research should address identified gaps in multilingual capabilities, long-context understanding, and theoretical foundations while exploring hybrid architectures and domain-specific applications.

Diffusion language models represent not merely an alternative to autoregressive models but a complementary paradigm with distinct advantages for specific task categories, particularly those requiring global planning, iterative refinement, and complex reasoning.

---

## References

Gong, S., Agarwal, S., Zhang, Y., Ye, J., Zheng, L., Li, M., An, C., Zhao, P., Bi, W., Han, J., Peng, H., & Kong, L. (2024). Scaling diffusion language models via adaptation from autoregressive models. *arXiv preprint arXiv:2410.17891*. https://arxiv.org/abs/2410.17891v3

Gong, S., Zhang, R., Zheng, H., Gu, J., Jaitly, N., Kong, L., & Zhang, Y. (2025). DiffuCoder: Understanding and improving masked diffusion models for code generation. *arXiv preprint arXiv:2506.20639*. https://arxiv.org/abs/2506.20639v2

Inception Labs, Khanna, S., Kharbanda, S., Li, S., Varma, H., Wang, E., Birnbaum, S., Luo, Z., Miraoui, Y., Palrecha, A., Ermon, S., Grover, A., & Kuleshov, V. (2025). Mercury: Ultra-fast language models based on diffusion. *arXiv preprint arXiv:2506.17298*. https://arxiv.org/abs/2506.17298v1

Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The cache for diffusion language models. *arXiv preprint arXiv:2505.15781*. https://arxiv.org/abs/2505.15781v1

Nie, S., Zhu, F., You, Z., Zhang, X., Ou, J., Hu, J., Zhou, J., Lin, Y., Wen, J.-R., & Li, C. (2025). Large language diffusion models. *arXiv preprint arXiv:2502.09992*. https://arxiv.org/abs/2502.09992v3

Sahoo, S. S., Arriola, M., Schiff, Y., Gokaslan, A., Marroquin, E., Chiu, J. T., Rush, A., & Kuleshov, V. (2024). Simple and effective masked diffusion language models. *arXiv preprint arXiv:2406.07524*. https://arxiv.org/abs/2406.07524v2

Wu, C., Zhang, H., Xue, S., Liu, Z., Diao, S., Zhu, L., Luo, P., Han, S., & Xie, E. (2025). Fast-dLLM: Training-free acceleration of diffusion LLM by enabling KV cache and parallel decoding. *arXiv preprint arXiv:2505.22618*. https://arxiv.org/abs/2505.22618v3

Xu, M., Geffner, T., Kreis, K., Nie, W., Xu, Y., Leskovec, J., Ermon, S., & Vahdat, A. (2024). Energy-based diffusion language models for text generation. *arXiv preprint arXiv:2410.21357*. https://arxiv.org/abs/2410.21357v4

Ye, J., Gao, J., Gong, S., Zheng, L., Jiang, X., Li, Z., & Kong, L. (2024). Beyond autoregression: Discrete diffusion for complex reasoning and planning. *arXiv preprint arXiv:2410.14157*. https://arxiv.org/abs/2410.14157v3

Zhao, S., Gupta, D., Zheng, Q., & Grover, A. (2025). d1: Scaling reasoning in diffusion large language models via reinforcement learning. *arXiv preprint arXiv:2504.12216*. https://arxiv.org/abs/2504.12216v2

---

**Review Statistics:**
- Total papers screened: 30
- Papers included: 10
- Date range: August 14, 2023 – August 13, 2025
- Primary category: cs.CL
- Average citations per paper: 6.5
- Total citations: 65
