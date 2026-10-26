# Systematic Literature Review: Test-Time Scaling of Language Models

**Date:** October 26, 2026  
**Search Parameters:** 10 papers, last 2 years (2024-2026), arXiv category cs.LG  
**Format:** APA Style

---

## Executive Summary

Test-time scaling (TTS) has emerged as a critical paradigm for enhancing language model reasoning capabilities by allocating additional computational resources during inference rather than training. This review synthesizes recent research (2024-2026) examining the mechanisms, limitations, and applications of test-time scaling across language models, vision-language models, and specialized domains. The literature reveals that TTS effectiveness is highly dependent on model architecture, candidate generation strategies, task characteristics, and the specific scaling methods employed.

---

## Annotated Bibliography (APA Format)

### 1. On-Policy Distillation and Test-Time Scaling

Ge, X., Zhang, Z., Huang, Y., Zhu, J., Yuan, L., Gu, W., Wu, W., Huang, W., Han, B., Zhang, X., & Yao, J. (2026). Towards understanding on-policy distillation through the lens of test-time scaling. *arXiv preprint arXiv:2608.11829*. https://arxiv.org/abs/2608.11829v3

**Summary:** This study examines on-policy distillation (OPD) through test-time scaling by varying sampling budgets (K) and evaluating performance with pass@K metrics. The authors identify two distinct patterns: OPD can improve pass@K at both small and large sampling budgets, or improve small-budget performance while reducing large-budget pass@K. They propose the Teacher Advantage Score at K (TAS@K) metric to predict which teacher will yield larger improvements at target sampling budgets, achieving 83.6% agreement across 13 benchmarks.

**Key Contributions:** Introduction of TAS@K for teacher selection; demonstration that OPD improvements are budget-dependent rather than universal.

---

### 2. Test-Time Training for Long Context

Tandon, A., Dalal, K., Li, X., Koceja, D., Rød, M., Buchanan, S., Wang, X., Leskovec, J., Koyejo, S., Hashimoto, T., Guestrin, C., McCaleb, J., Choi, Y., & Sun, Y. (2025). End-to-end test-time training for long context. *arXiv preprint arXiv:2512.23675*. https://arxiv.org/abs/2512.23675v2

**Summary:** The authors reformulate long-context language modeling as continual learning rather than architecture design. Their Test-Time Training End-to-End (TTT-E2E) method uses standard Transformer architecture with sliding-window attention but continues learning at test time via next-token prediction, compressing context into weights. Meta-learning improves initialization for test-time learning. The 3B model trained with 164B tokens scales with context length like full attention Transformers while maintaining constant inference latency (2.7× faster than full attention for 128K context).

**Key Contributions:** Novel TTT-E2E framework combining test-time learning with meta-learning; demonstration of constant-latency long-context modeling.

---

### 3. Beam Search as Test-Time Self-Distillation

Tan, S. E., Ji, X., Tutunov, R., Bou-Ammar, H., & Zimmer, M. (2026). Beam search as test-time self-distillation via counterfactual contexts. *arXiv preprint arXiv:2609.37041*. https://arxiv.org/abs/2609.37041v1

**Summary:** This work proposes test-time self-distillation, a decoding-time method that extracts steering signals from self-distillation frameworks without parameter updates, reward models, or training data. Counterfactual contexts (textual templates priming excellent vs. poor reasoning) substitute for demonstrations. The log-odds ratio under counterfactual conditions defines a reward signal, with optimal KL-regularized policy approximated via beam search. Experiments on MATH500, HumanEval, and GPQA show improvements over standard sampling, low temperature, beam search, and power sampling baselines.

**Key Contributions:** Operationalization of self-distillation at inference time; counterfactual context framework for reward-free steering.

---

### 4. Candidate Generation Strategy and Energy Efficiency

Kashaniyan, M., & Jannesari, A. (2026). Sample count is not enough: Candidate-generation strategy shapes the energy and performance of LLM test-time scaling. *arXiv preprint arXiv:2609.19499*. https://arxiv.org/abs/2609.19499v2

**Summary:** This study demonstrates that candidate count (N) alone inadequately describes test-time scaling costs. Fixing N=8, the authors compare four generation schedules (1×8, 2×4, 4×2, 8×1) on A100 GPUs. Eight serial calls consume 4.64-4.86× more GPU-device energy and have 5.77-6.12× higher P95 latency than one batched call. Accuracy improvements from increasing N (8.4-18.4 percentage points) must be weighed against systems costs.

**Key Contributions:** Systematic analysis of generation schedule impact on energy and latency; recommendation to report generation schedules alongside accuracy metrics.

---

### 5. Efficient Test-Time Scaling for Vision-Language Models

Kaya, M. O., Elliott, D., & Papadopoulos, D. P. (2025). Efficient test-time scaling for small vision-language models. *arXiv preprint arXiv:2510.03574*. https://arxiv.org/abs/2510.03574v2

**Summary:** Addressing the computational demands of existing TTS methods for resource-constrained small Vision-Language Models (VLMs), the authors propose two strategies: (i) Test-Time Augmentation (TTAug) generating multiple augmented inputs with token-level aggregation, and (ii) Test-Time Adaptation (TTAdapt) adapting parameters during inference using consensus-based pseudolabels. Experiments across nine benchmarks demonstrate consistent improvements while maintaining computational efficiency suitable for resource-constrained environments.

**Key Contributions:** TTAug and TTAdapt methods for efficient VLM scaling; demonstration of cross-model and cross-scale generality.

---

### 6. Test-Time Scaling in o1-like Models

Zeng, Z., Cheng, Q., Yin, Z., Zhou, Y., & Qiu, X. (2025). Revisiting the test-time scaling of o1-like models: Do they truly possess test-time scaling capabilities? *arXiv preprint arXiv:2502.12215*. https://arxiv.org/abs/2502.12215v2

**Summary:** This critical examination finds that longer Chain-of-Thought (CoT) in o1-like models (QwQ, DeepSeek-R1, LIMO) does not consistently enhance accuracy; correct solutions are often shorter than incorrect ones. The phenomenon relates to self-revision capabilities—longer CoTs contain more self-revisions leading to performance degradation. Parallel scaling achieves better coverage than sequential scaling. The proposed Shortest Majority Vote method combines parallel scaling with CoT length characteristics, significantly improving test-time scalability over conventional majority voting.

**Key Contributions:** Critical analysis of o1-like model scaling claims; Shortest Majority Vote method; identification of self-revision as scaling limitation.

---

### 7. Stratified Scaling Search for Diffusion Language Models

Bilal, A., Mohsin, M. A., Umer, M., Aali, A., Khanzada, M. U., Rafique, M. U., He, Z., Fox, E., & Hougen, D. F. (2026). S³: Stratified scaling search for test-time in diffusion language models. *arXiv preprint arXiv:2604.06260*. https://arxiv.org/abs/2604.06260v1

**Summary:** The S³ (Stratified Scaling Search) method addresses limitations of naive best-of-K sampling in Diffusion Language Models (DLMs) by reallocating compute during denoising rather than only at output stage. At each denoising step, S³ expands multiple candidate trajectories, evaluates with a lightweight reference-free verifier, and selectively resamples promising candidates while preserving diversity. Experiments with LLaDA-8B-Instruct on MATH-500, GSM8K, ARC-Challenge, and TruthfulQA demonstrate consistent improvements, particularly on mathematical reasoning tasks.

**Key Contributions:** Classical verifier-guided search for DLMs; reward-tilted sampling approximation without model modification.

---

### 8. Recursive Pretraining for Protein Language Models

Jha, S., Liao, Q., Vernon, R., Chandar, S., & Fournier, Q. (2026). recAMPLIFY: Large-scale pretraining of recursive protein language models. *arXiv preprint arXiv:2610.26747*. https://arxiv.org/abs/2610.26747v1

**Summary:** Adapting recursive pretraining to masked protein language models (pLMs), recAMPLIFY uses a weight-tied Transformer core refining residue-aligned hidden states over adjustable cycles. Despite 56% fewer parameters (155M vs. 350M), it improves CASP contact recovery and three of four supervised tasks (22.5% fold accuracy increase). Gated Mixture Recurrence (GMR) decodes proteins from probability-weighted mixtures of hidden states visited during recursion, reducing expected layer depth by up to 37% with learned residual gates controlling update acceptance.

**Key Contributions:** Test-time scaling adaptation for masked encoders; GMR framework unifying halting and gating; biological property tracking via halt depth.

---

### 9. Limits and Gains in Vision-Language Reasoning

Ahmadpour, M., Meighani, A., Taebi, P., Ghahroodi, O., Izadi, A., & Soleymani Baghshah, M. (2025). Limits and gains of test-time scaling in vision-language reasoning. *arXiv preprint arXiv:2512.11109*. https://arxiv.org/abs/2512.11109v1

**Summary:** This systematic empirical study examines inference-time reasoning methods across open-source and closed-source VLMs. Closed-source models consistently benefit from structured reasoning and iterative self-refinement, while open-source VLMs show inconsistent behavior: external verification provides reliable gains, but iterative refinement often degrades performance. TTS effectiveness is dataset-dependent, yielding clear improvements on multi-step reasoning tasks but limited gains on perception-focused benchmarks.

**Key Contributions:** Systematic comparison of open vs. closed-source VLM scaling behavior; identification of task-dependent TTS effectiveness; motivation for adaptive TTS strategies.

---

### 10. Analysis of Simple Test-Time Scaling

Wu, G. (2025). It's not that simple: An analysis of simple test-time scaling. *arXiv preprint arXiv:2507.14419*. https://arxiv.org/abs/2507.14419v1

**Summary:** This analysis finds that simple test-time scaling behavior is largely attributed to scaling down by enforcing maximum length rather than scaling up. Fine-tuning on long CoT data has no significant impact, and scaling up by appending "Wait" leads to inconsistencies with oscillation between solutions. A key distinction exists: o1-like models naturally scale up during reinforcement learning, surpassing peak performance, while simple test-time scaling progressively imposes lower upper limits on performance as it scales down.

**Key Contributions:** Critical distinction between scaling up vs. scaling down; demonstration that simple TTS reproduces appearance rather than unlocking higher performance.

---

## Synthesis and Key Themes

### 1. Scaling Strategies and Mechanisms

The literature reveals diverse TTS approaches:
- **Parallel vs. Sequential Scaling:** Parallel scaling consistently outperforms sequential approaches (Zeng et al., 2025; Kashaniyan & Jannesari, 2026)
- **Candidate Generation:** Batch generation is significantly more energy-efficient than serial calls (Kashaniyan & Jannesari, 2026)
- **Verifier-Guided Search:** Methods like S³ reallocate compute during generation rather than only at output (Bilal et al., 2026)
- **Self-Distillation:** Counterfactual contexts enable training-free steering at inference (Tan et al., 2026)

### 2. Model Architecture Considerations

TTS effectiveness varies by architecture:
- **Autoregressive LLMs:** Benefit from parallel scaling and majority voting variants (Zeng et al., 2025)
- **Diffusion Language Models:** Require specialized search over denoising trajectories (Bilal et al., 2026)
- **Masked Encoders:** Adapt through recursive pretraining rather than generation loops (Jha et al., 2026)
- **Vision-Language Models:** Show divergent behavior between open and closed-source implementations (Ahmadpour et al., 2025; Kaya et al., 2025)

### 3. Task Dependency

TTS gains are not universal:
- **Mathematical Reasoning:** Consistently benefits from TTS across studies (Bilal et al., 2026; Tan et al., 2026)
- **Code Generation:** Shows moderate improvements (Tan et al., 2026)
- **Perception Tasks:** Limited gains from TTS (Ahmadpour et al., 2025)
- **Long-Context Modeling:** Requires specialized test-time training approaches (Tandon et al., 2025)

### 4. Efficiency and Systems Considerations

Multiple studies emphasize cost-benefit analysis:
- Energy consumption varies dramatically by generation schedule (Kashaniyan & Jannesari, 2026)
- Small VLMs require computationally efficient TTS methods (Kaya et al., 2025)
- Constant-latency approaches enable practical long-context modeling (Tandon et al., 2025)
- Recursive methods can reduce expected layer depth (Jha et al., 2026)

### 5. Critical Perspectives

Recent work challenges assumptions about TTS:
- Longer CoT does not guarantee better performance (Zeng et al., 2025)
- Simple TTS may reproduce scaling appearance without unlocking higher performance (Wu, 2025)
- OPD improvements are budget-dependent, not universal (Ge et al., 2026)
- Open-source VLMs show inconsistent TTS behavior (Ahmadpour et al., 2025)

---

## Future Directions

Based on this review, promising research directions include:

1. **Adaptive TTS Strategies:** Developing methods that adjust scaling based on task characteristics and model capabilities (Ahmadpour et al., 2025; Wu, 2025)

2. **Energy-Efficient Scaling:** Optimizing generation schedules and batch sizes for resource-constrained environments (Kashaniyan & Jannesari, 2026; Kaya et al., 2025)

3. **Architecture-Specific Methods:** Tailoring TTS approaches to diffusion models, masked encoders, and multimodal architectures (Bilal et al., 2026; Jha et al., 2026)

4. **Verifier Development:** Creating lightweight, reference-free verifiers for guiding test-time search (Bilal et al., 2026)

5. **Teacher Selection Metrics:** Extending TAS@K and similar metrics for predicting distillation outcomes across sampling budgets (Ge et al., 2026)

---

## References

Ahmadpour, M., Meighani, A., Taebi, P., Ghahroodi, O., Izadi, A., & Soleymani Baghshah, M. (2025). Limits and gains of test-time scaling in vision-language reasoning. *arXiv preprint arXiv:2512.11109*. https://arxiv.org/abs/2512.11109v1

Bilal, A., Mohsin, M. A., Umer, M., Aali, A., Khanzada, M. U., Rafique, M. U., He, Z., Fox, E., & Hougen, D. F. (2026). S³: Stratified scaling search for test-time in diffusion language models. *arXiv preprint arXiv:2604.06260*. https://arxiv.org/abs/2604.06260v1

Ge, X., Zhang, Z., Huang, Y., Zhu, J., Yuan, L., Gu, W., Wu, W., Huang, W., Han, B., Zhang, X., & Yao, J. (2026). Towards understanding on-policy distillation through the lens of test-time scaling. *arXiv preprint arXiv:2608.11829*. https://arxiv.org/abs/2608.11829v3

Jha, S., Liao, Q., Vernon, R., Chandar, S., & Fournier, Q. (2026). recAMPLIFY: Large-scale pretraining of recursive protein language models. *arXiv preprint arXiv:2610.26747*. https://arxiv.org/abs/2610.26747v1

Kashaniyan, M., & Jannesari, A. (2026). Sample count is not enough: Candidate-generation strategy shapes the energy and performance of LLM test-time scaling. *arXiv preprint arXiv:2609.19499*. https://arxiv.org/abs/2609.19499v2

Kaya, M. O., Elliott, D., & Papadopoulos, D. P. (2025). Efficient test-time scaling for small vision-language models. *arXiv preprint arXiv:2510.03574*. https://arxiv.org/abs/2510.03574v2

Tan, S. E., Ji, X., Tutunov, R., Bou-Ammar, H., & Zimmer, M. (2026). Beam search as test-time self-distillation via counterfactual contexts. *arXiv preprint arXiv:2609.37041*. https://arxiv.org/abs/2609.37041v1

Tandon, A., Dalal, K., Li, X., Koceja, D., Rød, M., Buchanan, S., Wang, X., Leskovec, J., Koyejo, S., Hashimoto, T., Guestrin, C., McCaleb, J., Choi, Y., & Sun, Y. (2025). End-to-end test-time training for long context. *arXiv preprint arXiv:2512.23675*. https://arxiv.org/abs/2512.23675v2

Wu, G. (2025). It's not that simple: An analysis of simple test-time scaling. *arXiv preprint arXiv:2507.14419*. https://arxiv.org/abs/2507.14419v1

Zeng, Z., Cheng, Q., Yin, Z., Zhou, Y., & Qiu, X. (2025). Revisiting the test-time scaling of o1-like models: Do they truly possess test-time scaling capabilities? *arXiv preprint arXiv:2502.12215*. https://arxiv.org/abs/2502.12215v2

---

**Review completed:** October 26, 2026
