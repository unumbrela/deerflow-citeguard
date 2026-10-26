# Systematic Literature Review: Parallel Reasoning

**Review Period:** October 14, 2023 – October 13, 2025  
**Category:** cs.CL (Computation and Language)  
**Format:** APA Style  
**Date of Review:** October 26, 2026

---

## Executive Summary

This systematic literature review examines 10 key papers on parallel reasoning and related reasoning enhancement approaches in large language models published between October 2023 and October 2025. The selected papers represent significant advances in parallel thinking mechanisms, test-time scaling, reinforcement learning for reasoning, and efficient computational resource allocation during inference.

---

## Methodology

### Search Strategy
- **Database:** arXiv preprint repository
- **Category:** cs.CL (Computation and Language)
- **Date Range:** October 14, 2023 – October 13, 2025
- **Search Query:** "Parallel Reasoning"
- **Initial Pool:** 50 papers
- **Citation Expansion:** 90 additional papers from references
- **Shortlisted:** 30 papers
- **Final Selection:** 10 papers (screened by relevance to parallel reasoning)

### Selection Criteria
Papers were selected based on:
1. Direct relevance to parallel reasoning or parallel thinking approaches
2. Contributions to reasoning enhancement through computational parallelism
3. Novel methodologies for test-time scaling and resource allocation
4. Impact on mathematical reasoning and complex problem-solving

---

## Selected Papers (APA Format)

### 1. Parallel-R1: Towards Parallel Thinking via Reinforcement Learning

Zheng, T., Zhang, H., Yu, W., Wang, X., Dai, R., Liu, R., Bao, H., Huang, C., Huang, H., & Yu, D. (2025). *Parallel-R1: Towards parallel thinking via reinforcement learning*. arXiv preprint arXiv:2509.07980. https://arxiv.org/abs/2509.07980v2

**Key Contribution:** First reinforcement learning framework enabling parallel thinking behaviors for complex real-world reasoning tasks, achieving 8.4% accuracy improvement over sequential thinking models.

---

### 2. Learning to Keep a Promise: Scaling Language Model Decoding Parallelism with Learned Asynchronous Decoding

Jin, T., Cheng, E. Y., Ankner, Z., Saunshi, N., Elias, B. M., Yazdanbakhsh, A., Ragan-Kelley, J., Subramanian, S., & Carbin, M. (2025). *Learning to keep a promise: Scaling language model decoding parallelism with learned asynchronous decoding*. arXiv preprint arXiv:2502.11517. https://arxiv.org/abs/2502.11517v2

**Key Contribution:** PASTA system teaches LLMs to identify semantic independence and express parallel decoding opportunities, achieving 1.21x to 1.93x speedups with minimal quality degradation.

---

### 3. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., Zhu, Q., Xu, R., Zhang, R., Ma, S., Bi, X., Zhang, X., Yu, X., Wu, Y., Wu, Z. F., Gou, Z., Shao, Z., Li, Z., Gao, Z., & Liu, A. (2025). *DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning*. arXiv preprint arXiv:2501.12948. https://arxiv.org/abs/2501.12948v2

**Key Contribution:** Demonstrates that reasoning abilities can be incentivized through pure reinforcement learning without human-labeled reasoning trajectories, enabling emergent self-reflection and verification patterns.

---

### 4. s1: Simple Test-Time Scaling

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). *s1: Simple test-time scaling*. arXiv preprint arXiv:2501.19393. https://arxiv.org/abs/2501.19393v3

**Key Contribution:** Introduces budget forcing for test-time compute control, exceeding o1-preview by up to 27% on competition math questions through simple test-time scaling.

---

### 5. Qwen3 Technical Report

Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Gao, C., Huang, C., Lv, C., Zheng, C., Liu, D., Zhou, F., Huang, F., Hu, F., Ge, H., Wei, H., Lin, H., Tang, J., & Yang, J. (2025). *Qwen3 technical report*. arXiv preprint arXiv:2505.09388. https://arxiv.org/abs/2505.09388v1

**Key Contribution:** Integrates thinking mode and non-thinking mode in unified framework with thinking budget mechanism for adaptive computational resource allocation during inference.

---

### 6. Beyond the 80/20 Rule: High-Entropy Minority Tokens Drive Effective Reinforcement Learning for LLM Reasoning

Wang, S., Yu, L., Gao, C., Zheng, C., Liu, S., Lu, R., Dang, K., Chen, X., Yang, J., Zhang, Z., Liu, Y., Yang, A., Zhao, A., Yue, Y., Song, S., Yu, B., Huang, G., & Lin, J. (2025). *Beyond the 80/20 rule: High-entropy minority tokens drive effective reinforcement learning for LLM reasoning*. arXiv preprint arXiv:2506.01939. https://arxiv.org/abs/2506.01939v2

**Key Contribution:** Reveals that only 20% high-entropy tokens drive RLVR effectiveness, achieving superior performance by restricting policy gradient updates to these critical forking tokens.

---

### 7. LIMO: Less is More for Reasoning

Ye, Y., Huang, Z., Xiao, Y., Chern, E., Xia, S., & Liu, P. (2025). *LIMO: Less is more for reasoning*. arXiv preprint arXiv:2502.03387. https://arxiv.org/abs/2502.03387v3

**Key Contribution:** Demonstrates sophisticated mathematical reasoning can emerge with only 1% of training data, achieving 63.3% accuracy on AIME24 through strategic cognitive templates.

---

### 8. Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs

Chen, X., Xu, J., Liang, T., He, Z., Pang, J., Yu, D., Song, L., Liu, Q., Zhou, M., Zhang, Z., Wang, R., Tu, Z., Mi, H., & Yu, D. (2024). *Do NOT think that much for 2+3=? On the overthinking of o1-like LLMs*. arXiv preprint arXiv:2412.21187. https://arxiv.org/abs/2412.21187v2

**Key Contribution:** First comprehensive study on overthinking in o1-like models, proposing efficiency metrics and self-training strategies to reduce computational overhead without compromising accuracy.

---

### 9. Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement

Yang, A., Zhang, B., Hui, B., Gao, B., Yu, B., Li, C., Liu, D., Tu, J., Zhou, J., Lin, J., Lu, K., Xue, M., Lin, R., Liu, T., Ren, X., & Zhang, Z. (2024). *Qwen2.5-Math technical report: Toward mathematical expert model via self-improvement*. arXiv preprint arXiv:2409.12122. https://arxiv.org/abs/2409.12122v1

**Key Contribution:** Integrates self-improvement philosophy throughout pipeline with iterative reward model evolution for reinforcement learning, supporting Chain-of-Thought and Tool-Integrated Reasoning.

---

### 10. DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024). *DeepSeekMath: Pushing the limits of mathematical reasoning in open language models*. arXiv preprint arXiv:2402.03300. https://arxiv.org/abs/2402.03300v3

**Key Contribution:** Achieves 51.7% on MATH benchmark without external toolkits through Group Relative Policy Optimization (GRPO), approaching Gemini-Ultra and GPT-4 performance levels.

---

## Thematic Analysis

### Theme 1: Parallel Thinking Mechanisms
Two papers directly address parallel reasoning architectures:
- **Parallel-R1** (Zheng et al., 2025) introduces RL-based parallel thinking
- **PASTA** (Jin et al., 2025) enables learned asynchronous decoding

### Theme 2: Test-Time Scaling and Budget Control
Three papers focus on computational resource allocation:
- **s1** (Muennighoff et al., 2025) uses budget forcing
- **Qwen3** (Yang et al., 2025) implements thinking budget mechanism
- **Overthinking study** (Chen et al., 2024) addresses efficiency optimization

### Theme 3: Reinforcement Learning for Reasoning
Four papers leverage RL approaches:
- **DeepSeek-R1** (DeepSeek-AI et al., 2025) - pure RL without human labels
- **Parallel-R1** (Zheng et al., 2025) - progressive curriculum for parallel thinking
- **Qwen2.5-Math** (Yang et al., 2024) - iterative RM evolution
- **High-entropy tokens** (Wang et al., 2025) - token-entropy perspective on RLVR

### Theme 4: Data Efficiency in Reasoning
Two papers challenge data quantity assumptions:
- **LIMO** (Ye et al., 2025) - 1% data achieves superior performance
- **DeepSeekMath** (Shao et al., 2024) - engineered data selection pipeline

---

## Key Findings

1. **Parallel thinking emerges through RL:** Parallel-R1 demonstrates 8.4% improvement over sequential models, with parallel thinking serving as both exploration strategy and verification mechanism.

2. **Decoding parallelism achieves practical speedups:** PASTA's learning-based approach yields 1.21x-1.93x speedups while maintaining response quality through semantic independence detection.

3. **Test-time scaling is critical:** Budget forcing and thinking budgets enable adaptive compute allocation, with s1-32B exceeding o1-preview by 27% on math benchmarks.

4. **Token-level optimization matters:** Only 20% of high-entropy tokens drive RLVR effectiveness, suggesting focused optimization strategies.

5. **Data efficiency is achievable:** LIMO's success with 1% training data challenges assumptions about data requirements for sophisticated reasoning.

6. **Overthinking is prevalent:** o1-like models allocate excessive computation to simple problems, necessitating efficiency metrics and streamlining strategies.

---

## Research Gaps and Future Directions

1. **Integration of parallel and sequential thinking:** Limited work on hybrid approaches that dynamically switch between parallel exploration and sequential verification.

2. **Theoretical foundations:** Need for formal frameworks characterizing when parallel reasoning provides benefits over sequential approaches.

3. **Cross-domain generalization:** Most work focuses on mathematical reasoning; extension to other domains requires investigation.

4. **Hardware-level optimization:** Limited exploration of hardware-aware parallel reasoning implementations.

5. **Human-AI collaboration:** Potential for parallel reasoning to support collaborative problem-solving remains underexplored.

---

## Conclusion

The selected papers collectively demonstrate that parallel reasoning represents a promising direction for enhancing LLM capabilities. Key innovations include reinforcement learning frameworks for parallel thinking, learned asynchronous decoding mechanisms, test-time scaling approaches, and token-level optimization strategies. The field is moving toward more efficient, adaptive reasoning systems that balance computational resources with performance requirements. Future work should address integration challenges, theoretical foundations, and cross-domain applications.

---

## References

Chen, X., Xu, J., Liang, T., He, Z., Pang, J., Yu, D., Song, L., Liu, Q., Zhou, M., Zhang, Z., Wang, R., Tu, Z., Mi, H., & Yu, D. (2024). Do NOT think that much for 2+3=? On the overthinking of o1-like LLMs. *arXiv preprint arXiv:2412.21187*. https://arxiv.org/abs/2412.21187v2

DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., Zhu, Q., Xu, R., Zhang, R., Ma, S., Bi, X., Zhang, X., Yu, X., Wu, Y., Wu, Z. F., Gou, Z., Shao, Z., Li, Z., Gao, Z., & Liu, A. (2025). DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. *arXiv preprint arXiv:2501.12948*. https://arxiv.org/abs/2501.12948v2

Jin, T., Cheng, E. Y., Ankner, Z., Saunshi, N., Elias, B. M., Yazdanbakhsh, A., Ragan-Kelley, J., Subramanian, S., & Carbin, M. (2025). Learning to keep a promise: Scaling language model decoding parallelism with learned asynchronous decoding. *arXiv preprint arXiv:2502.11517*. https://arxiv.org/abs/2502.11517v2

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. *arXiv preprint arXiv:2501.19393*. https://arxiv.org/abs/2501.19393v3

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024). DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*. https://arxiv.org/abs/2402.03300v3

Wang, S., Yu, L., Gao, C., Zheng, C., Liu, S., Lu, R., Dang, K., Chen, X., Yang, J., Zhang, Z., Liu, Y., Yang, A., Zhao, A., Yue, Y., Song, S., Yu, B., Huang, G., & Lin, J. (2025). Beyond the 80/20 rule: High-entropy minority tokens drive effective reinforcement learning for LLM reasoning. *arXiv preprint arXiv:2506.01939*. https://arxiv.org/abs/2506.01939v2

Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Gao, C., Huang, C., Lv, C., Zheng, C., Liu, D., Zhou, F., Huang, F., Hu, F., Ge, H., Wei, H., Lin, H., Tang, J., & Yang, J. (2025). Qwen3 technical report. *arXiv preprint arXiv:2505.09388*. https://arxiv.org/abs/2505.09388v1

Yang, A., Zhang, B., Hui, B., Gao, B., Yu, B., Li, C., Liu, D., Tu, J., Zhou, J., Lin, J., Lu, K., Xue, M., Lin, R., Liu, T., Ren, X., & Zhang, Z. (2024). Qwen2.5-Math technical report: Toward mathematical expert model via self-improvement. *arXiv preprint arXiv:2409.12122*. https://arxiv.org/abs/2409.12122v1

Ye, Y., Huang, Z., Xiao, Y., Chern, E., Xia, S., & Liu, P. (2025). LIMO: Less is more for reasoning. *arXiv preprint arXiv:2502.03387*. https://arxiv.org/abs/2502.03387v3

Zheng, T., Zhang, H., Yu, W., Wang, X., Dai, R., Liu, R., Bao, H., Huang, C., Huang, H., & Yu, D. (2025). Parallel-R1: Towards parallel thinking via reinforcement learning. *arXiv preprint arXiv:2509.07980*. https://arxiv.org/abs/2509.07980v2

---

**Review completed:** October 26, 2026  
**Total papers reviewed:** 10  
**Publication window:** October 14, 2023 – October 13, 2025  
**Primary category:** cs.CL
