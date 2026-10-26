# Systematic Literature Review: Parallel Reasoning in Large Language Models

**Search Parameters:**
- **Database:** arXiv
- **Category:** cs.CL (Computational Linguistics)
- **Publication Window:** October 14, 2023 – October 13, 2025
- **Search Query:** "Parallel Reasoning"
- **Results:** 10 papers

**Retrieval Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in parallel reasoning approaches for large language models (LLMs). The reviewed literature reveals a rapidly evolving field focused on improving reasoning efficiency, accuracy, and scalability through parallel computation strategies. Key themes include: (1) parallel scaling methods for test-time inference, (2) efficiency optimization through pruning and speculative decoding, (3) hybrid approaches combining sequential and parallel reasoning, and (4) novel training methodologies for parallel reasoning capabilities.

---

## Annotated Bibliography (APA Format)

### 1. Adaptive Termination for Multi-round Parallel Reasoning

Xu, Z., Qiu, Z., Huang, G., Li, K., Li, S., Zhang, C., Li, K., Yi, Q., Jiang, Y., Zhou, B., Lian, F., & Kang, Z. (2025). Adaptive termination for multi-round parallel reasoning: An universal semantic entropy-guided framework. *arXiv preprint arXiv:2507.06829*. https://arxiv.org/abs/2507.06829v1

**Summary:** This paper addresses fundamental limitations in both sequential and parallel reasoning paradigms. The authors introduce semantic entropy (SE) as an intrinsic quality metric that quantifies semantic diversity of parallel model responses, serving as a robust indicator of reasoning quality due to its strong negative correlation with accuracy. The framework enables dynamic control and early termination of reasoning traces, exploiting complementary strengths of both sequential and parallel reasoning paradigms through collaborative inference.

**Key Contributions:** Universal semantic entropy-guided framework for adaptive termination; dynamic control mechanism for collaborative inference.

---

### 2. Distributional Reasoning in LLMs

Shalev, Y., Feder, A., & Goldstein, A. (2024). Distributional reasoning in LLMs: Parallel reasoning processes in multi-hop reasoning. *arXiv preprint arXiv:2406.13858*. https://arxiv.org/abs/2406.13858v1

**Summary:** This study presents a novel interpretable analysis of internal multi-hop reasoning processes in LLMs. The authors demonstrate that prediction processes for compositional reasoning questions can be modeled using linear transformations between semantic category spaces. Statistical analyses reveal that middle layers generate highly interpretable embeddings representing potential intermediate answers, with corresponding token subsets activated in the output, implying the existence of parallel reasoning paths even when models lack necessary knowledge.

**Key Contributions:** Interpretable analysis of internal reasoning processes; evidence of parallel reasoning paths in LLM hidden layers; cognitive modeling implications.

---

### 3. DeepPrune: Parallel Scaling without Inter-trace Redundancy

Tu, S., Li, Y., Bai, Y., Hou, L., & Li, J. (2025). DeepPrune: Parallel scaling without inter-trace redundancy. *arXiv preprint arXiv:2510.08483*. https://arxiv.org/abs/2510.08483v2

**Summary:** This work addresses computational inefficiency in parallel scaling caused by inter-trace redundancy, with analysis revealing over 80% of parallel reasoning traces yield identical final answers. DeepPrune features a specialized judge model trained with out-of-distribution data using oversampling techniques to predict answer equivalence from partial reasoning traces (achieving 0.7072 AUROC), combined with an online greedy clustering algorithm for dynamic pruning. Evaluations demonstrate 65.73%–88.50% token reduction while maintaining accuracy within 3 percentage points.

**Key Contributions:** Dynamic pruning framework for efficient parallel scaling; specialized judge model for answer equivalence prediction; substantial computational efficiency gains.

---

### 4. Accelerate Parallelizable Reasoning via Parallel Decoding

Yu, Y. (2025). Accelerate parallelizable reasoning via parallel decoding within one sequence. *arXiv preprint arXiv:2503.20533*. https://arxiv.org/abs/2503.20533v4

**Summary:** This paper leverages inherent parallelizability of certain tasks to accelerate reasoning processes. The method decodes multiple tokens per forward pass via a tree-like attention mask within a single sequence, avoiding additional memory usage. Experimental results demonstrate up to nearly 100% speedup in decoding while maintaining answer quality.

**Key Contributions:** Tree-like attention mask for parallel decoding; single-sequence parallel token generation; significant speedup without memory overhead.

---

### 5. Speculative Decoding for Multi-Sample Inference

Li, Y., Shi, J., Feng, S., Yuan, P., Wang, X., Zhang, Y., Zhang, J., Tan, C., Pan, B., Hu, Y., & Li, K. (2025). Speculative decoding for multi-sample reasoning. *arXiv preprint arXiv:2503.05330*. https://arxiv.org/abs/2503.05330v1

**Summary:** This work proposes a novel speculative decoding method for multi-sample reasoning scenarios such as self-consistency and Best-of-N sampling. The method exploits intrinsic consensus of parallel generation paths to synthesize high-quality draft tokens without requiring auxiliary models or external databases. By dynamically analyzing structural patterns through probabilistic aggregation, it identifies consensus token sequences aligning with decoding distribution. Evaluations show substantial improvement in draft acceptance rates while reducing latency.

**Key Contributions:** Consensus-based speculative decoding for multi-sample inference; probabilistic aggregation mechanism; paradigm shift for efficient sampling-based reasoning.

---

### 6. Training LLMs to Reason in Parallel with Global Forking Tokens

Jia, S., Wang, X., & Kasiviswanathan, S. P. (2025). Training large language models to reason in parallel with global forking tokens. *arXiv preprint arXiv:2510.05132*. https://arxiv.org/abs/2510.05132v3

**Summary:** This paper addresses the challenge that forking tokens triggering diverse yet correct reasoning modes are typically deep in the sampling tree, causing temperature scaling to encounter worsened diversity-accuracy trade-offs. The authors treat parallel reasoning as a set-of-next-token-prediction problem and incorporate set-based global loss into Supervised Fine-Tuning using bipartite matching. Set Supervised Fine-Tuning (SSFT) preserves unique reasoning modes and produces emergent global forking tokens, while Global Forking Policy Optimization (GFPO) leverages these tokens to incentivize complex reasoning, outperforming SFT counterparts on math and code generation benchmarks.

**Key Contributions:** Set Supervised Fine-Tuning (SSFT) methodology; Global Forking Policy Optimization (GFPO); emergent global forking tokens for parallel reasoning.

---

### 7. Large Language Models as an Indirect Reasoner

Zhang, Y., Sun, Y., Zhan, Y., Tao, D., Tao, D., & Gong, C. (2024). Large language models as an indirect reasoner: Contrapositive and contradiction for automated reasoning. *arXiv preprint arXiv:2402.03667*. https://arxiv.org/abs/2402.03667v2

**Summary:** This work addresses the neglect of Indirect Reasoning (IR) in favor of Direct Reasoning (DR) in existing methods. The proposed Direct-Indirect Reasoning (DIR) method considers DR and IR as multiple parallel reasoning paths merged to derive final answers. Prompt templates incorporating contrapositive and contradiction principles stimulate LLMs to implement IR by assuming negation of conclusions. Experimental results on four datasets demonstrate significant outperformance over original methods when combined with various Chain-of-Thought variants.

**Key Contributions:** Direct-Indirect Reasoning (DIR) framework; parallel reasoning path integration; contrapositive and contradiction-based prompt engineering.

---

### 8. Division-of-Thoughts: Hybrid Language Model Synergy

Shao, C., Hu, X., Lin, Y., & Xu, F. (2025). Division-of-Thoughts: Harnessing hybrid language model synergy for efficient on-device agents. *arXiv preprint arXiv:2502.04392*. https://arxiv.org/abs/2502.04392v1

**Summary:** This paper proposes Division-of-Thoughts (DoT), a collaborative reasoning framework leveraging synergy between locally deployed Smaller-scale Language Models (SLMs) and cloud-based LLMs. DoT employs a Task Decomposer to break queries into sub-tasks, a Task Scheduler to create dependency graphs facilitating parallel reasoning, and a Plug-and-Play Adapter for model allocation. Self-reinforced training relies solely on task execution feedback. Experiments demonstrate 66.12% reduction in reasoning time and 83.57% reduction in API costs while maintaining competitive accuracy.

**Key Contributions:** Hybrid SLM-LLM collaborative framework; task decomposition and parallel scheduling; efficient on-device agent deployment.

---

### 9. STOC-TOT: Stochastic Tree-of-Thought

Bi, Z., Hajialigol, D., Sun, Z., Hao, J., & Wang, X. (2024). STOC-TOT: Stochastic tree-of-thought with constrained decoding for complex reasoning in multi-hop question answering. *arXiv preprint arXiv:2407.03687*. https://arxiv.org/abs/2407.03687v1

**Summary:** This work addresses complexities in multi-hop question answering requiring fine-grained prompting for different question and reasoning types. STOC-TOT constructs tree-like reasoning structures by breaking original questions into smaller sub-questions forming different reasoning paths, with probability estimation at each step. Constrained decoding generates more grounded answers and reduces hallucination. Experiments across two datasets and five LLMs show significant outperformance over other reasoning prompts.

**Key Contributions:** Stochastic tree-of-thought prompting; probability-guided reasoning path selection; constrained decoding for multi-hop QA.

---

### 10. Parallel Test-Time Scaling for Latent Reasoning Models

You, R., Li, Y., Liu, M., Wang, W., Nie, L., & Li, W. (2025). Parallel test-time scaling for latent reasoning models. *arXiv preprint arXiv:2510.07745*. https://arxiv.org/abs/2510.07745v4

**Summary:** This paper enables parallel test-time scaling for latent reasoning models where intermediate reasoning unfolds in continuous vector spaces. Two uncertainty-inspired stochastic sampling strategies are introduced: Monte Carlo Dropout and Additive Gaussian Noise. A Latent Reward Model (LatentRM) trained with step-wise contrastive objective scores and guides latent reasoning. Experiments show both sampling strategies scale effectively with compute and exhibit distinct exploration dynamics, while LatentRM enables effective trajectory selection.

**Key Contributions:** Parallel TTS for continuous-space latent reasoning; uncertainty-inspired sampling strategies; Latent Reward Model for trajectory aggregation.

---

## Thematic Analysis

### Theme 1: Efficiency Optimization in Parallel Reasoning

Multiple papers address computational efficiency challenges in parallel reasoning. Tu et al. (2025) identify inter-trace redundancy as a critical bottleneck, with DeepPrune achieving 65-88% token reduction. Yu (2025) demonstrates nearly 100% speedup through parallel decoding within single sequences. Li et al. (2025) reduce latency through consensus-based speculative decoding. Shao et al. (2025) achieve 66% time reduction through hybrid model collaboration.

### Theme 2: Training Methodologies for Parallel Reasoning

Jia et al. (2025) introduce Set Supervised Fine-Tuning and Global Forking Policy Optimization to preserve diverse reasoning modes during training. Zhang et al. (2024) propose Direct-Indirect Reasoning frameworks treating different reasoning approaches as parallel paths.

### Theme 3: Adaptive Control and Termination

Xu et al. (2025) develop semantic entropy-guided adaptive termination for collaborative inference, addressing arbitrary token budget limitations in sequential scaling and coordination challenges in parallel scaling.

### Theme 4: Latent and Continuous Space Reasoning

You et al. (2025) extend parallel reasoning to continuous vector spaces, introducing sampling strategies and reward models for latent reasoning models, representing a paradigm shift from token-based approaches.

### Theme 5: Internal Mechanism Analysis

Shalev et al. (2024) provide interpretable analysis revealing parallel reasoning paths exist in LLM hidden layers even without explicit documentation, offering insights into emergent reasoning capabilities.

---

## Research Gaps and Future Directions

1. **Coordination Mechanisms:** While parallel scaling shows promise, coordination among parallel branches remains challenging (Xu et al., 2025).

2. **Diversity-Accuracy Trade-off:** Maintaining diverse yet accurate reasoning paths requires novel training approaches beyond temperature scaling (Jia et al., 2025).

3. **Continuous Space Reasoning:** Latent reasoning in vector spaces opens new directions but requires further exploration of sampling and aggregation strategies (You et al., 2025).

4. **Resource-Constrained Deployment:** Hybrid approaches balancing local and cloud computation need further optimization for edge devices (Shao et al., 2025).

5. **Interpretability:** Understanding internal parallel reasoning processes remains limited, requiring more interpretable analysis methods (Shalev et al., 2024).

---

## Conclusion

The literature from 2023-2025 reveals parallel reasoning as a rapidly maturing field addressing fundamental challenges in LLM inference efficiency and capability. Key advances include efficiency optimization through pruning and speculative decoding, novel training methodologies preserving reasoning diversity, adaptive control mechanisms, and extension to continuous latent spaces. Future research should focus on improving coordination mechanisms, resolving diversity-accuracy trade-offs, and enhancing interpretability of parallel reasoning processes.

---

## References

Bi, Z., Hajialigol, D., Sun, Z., Hao, J., & Wang, X. (2024). STOC-TOT: Stochastic tree-of-thought with constrained decoding for complex reasoning in multi-hop question answering. *arXiv preprint arXiv:2407.03687*. https://arxiv.org/abs/2407.03687v1

Jia, S., Wang, X., & Kasiviswanathan, S. P. (2025). Training large language models to reason in parallel with global forking tokens. *arXiv preprint arXiv:2510.05132*. https://arxiv.org/abs/2510.05132v3

Li, Y., Shi, J., Feng, S., Yuan, P., Wang, X., Zhang, Y., Zhang, J., Tan, C., Pan, B., Hu, Y., & Li, K. (2025). Speculative decoding for multi-sample reasoning. *arXiv preprint arXiv:2503.05330*. https://arxiv.org/abs/2503.05330v1

Shalev, Y., Feder, A., & Goldstein, A. (2024). Distributional reasoning in LLMs: Parallel reasoning processes in multi-hop reasoning. *arXiv preprint arXiv:2406.13858*. https://arxiv.org/abs/2406.13858v1

Shao, C., Hu, X., Lin, Y., & Xu, F. (2025). Division-of-Thoughts: Harnessing hybrid language model synergy for efficient on-device agents. *arXiv preprint arXiv:2502.04392*. https://arxiv.org/abs/2502.04392v1

Tu, S., Li, Y., Bai, Y., Hou, L., & Li, J. (2025). DeepPrune: Parallel scaling without inter-trace redundancy. *arXiv preprint arXiv:2510.08483*. https://arxiv.org/abs/2510.08483v2

Xu, Z., Qiu, Z., Huang, G., Li, K., Li, S., Zhang, C., Li, K., Yi, Q., Jiang, Y., Zhou, B., Lian, F., & Kang, Z. (2025). Adaptive termination for multi-round parallel reasoning: An universal semantic entropy-guided framework. *arXiv preprint arXiv:2507.06829*. https://arxiv.org/abs/2507.06829v1

You, R., Li, Y., Liu, M., Wang, W., Nie, L., & Li, W. (2025). Parallel test-time scaling for latent reasoning models. *arXiv preprint arXiv:2510.07745*. https://arxiv.org/abs/2510.07745v4

Yu, Y. (2025). Accelerate parallelizable reasoning via parallel decoding within one sequence. *arXiv preprint arXiv:2503.20533*. https://arxiv.org/abs/2503.20533v4

Zhang, Y., Sun, Y., Zhan, Y., Tao, D., Tao, D., & Gong, C. (2024). Large language models as an indirect reasoner: Contrapositive and contradiction for automated reasoning. *arXiv preprint arXiv:2402.03667*. https://arxiv.org/abs/2402.03667v2

---

**Document prepared:** October 26, 2026  
**Format:** APA 7th Edition  
**Total papers reviewed:** 10
