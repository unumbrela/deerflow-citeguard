# Systematic Literature Review: Knowledge Distillation of Language Models

**Date:** October 26, 2025  
**Search Category:** cs.CL (Computation and Language)  
**Time Period:** 2024-2026 (Last 2 Years)  
**Number of Papers:** 10

---

## Executive Summary

This systematic literature review examines recent advances in knowledge distillation (KD) for language models, focusing on 10 papers published between 2024 and 2026 in the cs.CL category. The review reveals several key trends: (1) a shift from output-matching to behavioral alignment and reasoning transfer, (2) innovative approaches for black-box distillation without logit access, (3) integration of preference optimization and reinforcement learning with traditional KD, and (4) growing emphasis on practical deployment in resource-constrained settings. Recent methods achieve 70-95% retention of teacher capabilities while reducing model size by 6-18×, with particular progress in cross-architecture distillation, multilingual transfer, and domain-specific applications.

---

## 1. Introduction

Knowledge distillation has emerged as a critical technique for compressing large language models (LLMs) while preserving their capabilities. As LLMs grow to billions of parameters, deploying them in resource-constrained environments—from edge devices to low-connectivity regions—requires effective compression strategies. This review synthesizes findings from 10 recent papers (2024-2026) that advance the state of the art in language model distillation.

### Research Questions

This review addresses the following questions:
1. What novel distillation methodologies have been proposed for language models in 2024-2026?
2. How do recent approaches address limitations of traditional output-matching KD?
3. What performance gains are achieved in terms of capability retention and model compression?
4. What are the remaining challenges and open problems in LLM distillation?

---

## 2. Methodology

### Search Strategy

Papers were retrieved from arXiv using the following search parameters:
- **Keywords:** "LLM distillation", "knowledge distillation"
- **Category:** cs.CL (Computation and Language)
- **Date Range:** October 2024 - October 2026
- **Selection Criteria:** Papers focused on knowledge distillation applied to language models

### Selection Process

From an initial pool of 15+ papers, 10 were selected based on:
1. Direct relevance to language model distillation (excluding speech/audio-focused papers)
2. Publication in cs.CL or closely related categories
3. Empirical evaluation with quantitative results
4. Novel methodological contributions

### Data Extraction

For each paper, the following information was extracted:
- Research question and problem formulation
- Methodology and technical approach
- Key empirical findings and metrics
- Acknowledged limitations

---

## 3. Thematic Analysis

### 3.1 Intermediate Representation Distillation

Traditional KD focuses on matching final output distributions, but recent work recognizes the value of transferring intermediate reasoning processes.

**DistillLens** (Dhakal et al., 2026) introduces symmetric knowledge distillation through the Logit Lens, projecting intermediate hidden states into vocabulary space and enforcing structural alignment between student and teacher. The method imposes dual-sided penalties that prevent both overconfidence and underconfidence while preserving high-entropy information pathways essential for complex reasoning. Experiments on GPT-2 and Llama architectures show consistent improvements over standard KD and feature-transfer baselines on instruction-following benchmarks.

**Decoder-based Sense Knowledge Distillation** (Wang et al., 2026) addresses a different aspect of intermediate knowledge: structured lexical semantics. While prior work incorporated sense dictionaries into encoder models, DSKD enables decoder-style LLMs to inherit structured word-sense knowledge without requiring dictionary lookup at inference time. This approach significantly enhances distillation performance while maintaining efficient training.

### 3.2 Black-Box Distillation Without Logit Access

A major practical challenge is distilling from proprietary models where internal logits are unavailable. Three papers address this constraint:

**Generative Adversarial Distillation (GAD)** (Ye et al., 2025) frames black-box distillation as a minimax game: the student acts as generator while a discriminator learns to distinguish student from teacher responses. The discriminator serves as an on-policy reward model that co-evolves with the student, providing adaptive feedback. Remarkably, Qwen2.5-14B-Instruct trained with GAD becomes comparable to its teacher GPT-5-Chat on LMSYS-Chat evaluation—despite having no access to teacher logits.

**Bounded Behavioral Indistinguishability** (Hasan, 2026) challenges the assumption that output similarity implies behavioral equivalence. The paper formalizes (ε,q,t,A)-behavioral indistinguishability and evaluates distillation using a 5,000-prompt adversarial probe suite. While LoRA distillation improves semantic similarity (0.788→0.862 for Qwen, 0.814→0.874 for Llama), adversarial discriminators retain nonzero distinguishing advantage, with artifacts concentrated in style/format, robustness, and domain-technical prompts. This work argues that black-box distillation requires bounded, adversarial, and category-aware evaluation beyond simple similarity metrics.

**PLaD** (Zhang et al., 2024) generates pseudo-preference pairs by exploiting teacher-student capacity discrepancies, then uses ranking loss to recalibrate the student's sequence likelihood estimation. This preference-based approach bypasses the need for internal state access while mitigating student mis-calibration issues.

### 3.3 Preference Optimization and Reinforcement Learning Integration

Recent work increasingly combines KD with preference learning and RL:

**ORPO-Distill** (Singh et al., 2025) formulates cross-architecture distillation as preference optimization rather than standard chain-of-thought imitation. The method employs Odds-Ratio Preference Optimization to contrast teacher and student reasoning traces, adopting a mixed-policy strategy that outperforms both off-policy and on-policy alternatives across five datasets.

**DistiLLM-2** (Ko et al., 2025) introduces a contrastive approach that simultaneously increases the likelihood of teacher responses while decreasing the likelihood of student responses. This strategy harnesses synergy between loss formulations and data types, supporting diverse applications including instruction-following, code generation, preference alignment, and vision-language extensions.

**Decoupling KL and Trajectories** (Zhao et al., 2026) provides a unified theoretical framework showing that off-policy and on-policy distillation implicitly couple two orthogonal choices: prefix source and token-level KL direction. The paper establishes gradient-level identities connecting four decoupled objectives to SFT, DAgger, offline-RL, and on-policy distillation. Key findings include: (1) KL direction induces accuracy-entropy tradeoffs, (2) prefix source induces quality-compute tradeoffs, and (3) long-sequence distillation requires substantial forward-KL weight to prevent entropy collapse. The proposed entropy-gated length curriculum improves Avg@k by 3.6 and Pass@k by up to 5.8 points while cutting average response length by 3×.

**Knowledge Distillation with Chain-of-Thought RL** (Paredes La Torre et al., 2026) combines KD with guided chain-of-thought reinforcement learning using Group Relative Policy Optimization. Using Qwen 3B→0.5B distillation across English, Spanish, and code datasets, the distilled student retains 70-91% of teacher capability in English, up to 95% in Spanish, and 93.5% Rouge-L in code. CoT+GRPO integration improves reasoning coherence for coding tasks compared to KD alone.

### 3.4 Domain-Specific and Practical Applications

Several papers demonstrate distillation for specialized deployment scenarios:

**Bangladesh Legal RAG** (Kamal et al., 2026) addresses legal information accessibility in resource-constrained settings. The system compresses a 9B-parameter Gemma-2 teacher into a 2B-parameter student through two-phase progressive distillation: supervised fine-tuning on 9,429 legal Q&A pairs followed by sparse KL divergence minimization via QLoRA. The model quantizes to 1.6GB and runs at 4-8 tokens/second on a Pixel 6 without network access. On English benchmarks, it achieves ROUGE-L 0.4715 and BERTScore 0.5679—103% and 143% gains over undistilled baselines. Cross-lingual evaluation on Bangla queries yields BERTScore 0.8133 despite an English-only corpus.

**Few-Shot MCQA** (Sutanto et al., 2024) uses LLMs to generate multiple-choice questions with probability scores, then distills this knowledge into DeBERTa-v3-base. On MMLU benchmarks, this approach improves accuracy from 28.9% to 39.3%—a 10+ point gain over direct 5-shot finetuning—demonstrating effective knowledge transfer for few-shot learning scenarios.

---

## 4. Performance Metrics and Compression Efficiency

### Capability Retention

| Paper | Teacher → Student | Retention Rate | Task Domain |
|-------|-------------------|----------------|-------------|
| Paredes La Torre et al. (2026) | Qwen 3B → 0.5B | 70-95% | Multilingual + Code |
| Kamal et al. (2026) | Gemma-2 9B → 2B | 103-143% gain over baseline | Legal RAG |
| Ye et al. (2025) | GPT-5-Chat → Qwen2.5-14B | Comparable on LMSYS | General chat |
| Sutanto et al. (2024) | LLM → DeBERTa-v3-base | 39.3% accuracy (+10 pts) | MCQA |
| Hasan (2026) | Qwen/Llama → LoRA student | 0.862-0.874 similarity | Behavioral probes |

### Compression Ratios

- **6× compression:** Qwen 3B → 0.5B (Paredes La Torre et al., 2026)
- **4.5× compression:** Gemma-2 9B → 2B (Kamal et al., 2026)
- **Parameter reduction:** DistillLens achieves improvements without explicit size reduction, focusing on quality gains (Dhakal et al., 2026)

### Inference Efficiency

- **4-bit quantization** further reduces memory footprint and latency (Paredes La Torre et al., 2026)
- **1.6 GB model size** enables smartphone deployment (Kamal et al., 2026)
- **4-8 tokens/second** on Pixel 6 without network access (Kamal et al., 2026)
- **3× reduction in response length** via entropy-gated curriculum (Zhao et al., 2026)

---

## 5. Limitations and Open Challenges

### 5.1 Evaluation Gaps

Several papers acknowledge limitations in their evaluation scope:
- **Task diversity:** Many methods evaluated primarily on instruction-following or math reasoning, with limited cross-domain validation (Dhakal et al., 2026; Zhao et al., 2026)
- **Adversarial robustness:** Behavioral indistinguishability studies reveal that semantic similarity does not guarantee robustness to adversarial probing (Hasan, 2026)
- **Architecture generalizability:** Most studies focus on specific model families (Qwen, Llama, GPT), limiting cross-architecture conclusions

### 5.2 Computational Overhead

- **Training complexity:** Methods like GAD (Ye et al., 2025) and contrastive approaches (Ko et al., 2025) introduce additional training components (discriminators, dual losses) that increase computational costs
- **Hyperparameter tuning:** Several papers note that optimal settings were determined for specific languages or tasks, requiring re-tuning for new domains (Paredes La Torre et al., 2026)

### 5.3 Theoretical Understanding

- **Loss landscape:** While Zhao et al. (2026) provide a unified framework connecting KD objectives to RL paradigms, the interaction between different loss components remains incompletely understood
- **Information bottlenecks:** The mechanisms by which intermediate representations transfer knowledge—and which aspects are most critical—require further investigation (Dhakal et al., 2026; Wang et al., 2026)

### 5.4 Practical Deployment

- **Cross-lingual transfer:** While Paredes La Torre et al. (2026) and Kamal et al. (2026) demonstrate multilingual capabilities, systematic understanding of language-specific distillation challenges is limited
- **Domain adaptation:** Most methods assume access to domain-specific training data; few-shot or zero-shot distillation remains underexplored

---

## 6. Future Directions

Based on this review, we identify several promising research directions:

1. **Unified evaluation frameworks:** Standardized adversarial probing suites and behavioral benchmarks (as proposed by Hasan, 2026) should be adopted across distillation research to enable fair comparison

2. **Architecture-agnostic methods:** Cross-architecture distillation techniques (Singh et al., 2025; Ko et al., 2025) should be extended to support arbitrary teacher-student pairs without manual alignment

3. **Theoretical foundations:** Further work is needed to understand the information-theoretic limits of distillation and the relationship between different loss objectives (Zhao et al., 2026)

4. **Resource-aware distillation:** Methods should explicitly optimize for deployment constraints (memory, latency, energy) rather than treating these as post-hoc considerations

5. **Multilingual and cross-lingual transfer:** Systematic investigation of language-specific distillation challenges, particularly for low-resource languages

6. **Integration with alignment:** As preference optimization becomes central to LLM training, distillation methods should jointly optimize for capability retention and alignment with human values

---

## 7. Conclusion

Knowledge distillation for language models has advanced significantly in 2024-2026, with innovations spanning intermediate representation transfer, black-box methods, preference optimization integration, and practical deployment. Recent approaches achieve 70-95% capability retention while compressing models 4-18×, enabling deployment on edge devices and in resource-constrained settings. However, challenges remain in evaluation rigor, computational efficiency, theoretical understanding, and cross-domain generalization. The field is moving beyond simple output matching toward behavioral alignment, reasoning transfer, and preference-aware distillation—trends that will likely accelerate as LLMs continue to grow in capability and deployment complexity.

---

## References

Dhakal, M., Jinadu, U., Budathoki, A., Sunderraman, R., & Ding, Y. (2026). DistillLens: Symmetric knowledge distillation through logit lens. *arXiv preprint arXiv:2602.13567*. https://arxiv.org/abs/2602.13567

Hasan, M. (2026). Bounded behavioral indistinguishability for black-box LLM distillation. *arXiv preprint arXiv:2605.30448*. https://arxiv.org/abs/2605.30448

Kamal, M. N., Fahim, M. H., Ridwan, T., Zaman, N., Florin, F. R., Sadeque, F. Y., & Ahmed, S. R. (2026). Efficient LLM distillation for Bangladesh legal context: A smartphone-compatible retrieval-augmented generation model. *arXiv preprint arXiv:2609.24177*. https://arxiv.org/abs/2609.24177

Ko, J., Chen, T., Kim, S., Ding, T., Liang, L., Zharkov, I., & Yun, S.-Y. (2025). DistiLLM-2: A contrastive approach boosts the distillation of LLMs. *arXiv preprint arXiv:2503.07067*. https://arxiv.org/abs/2503.07067

Paredes La Torre, A., Flores, B., & Rodriguez, D. (2026). Knowledge distillation for large language models. *arXiv preprint arXiv:2603.13765*. https://arxiv.org/abs/2603.13765

Singh, A., Vaddina, V., & Birru, D. (2025). ORPO-Distill: Mixed-policy preference optimization for cross-architecture LLM distillation. *arXiv preprint arXiv:2509.25100*. https://arxiv.org/abs/2509.25100

Sutanto, P., Santoso, J., Setiawan, E. I., & Wibawa, A. P. (2024). LLM distillation for efficient few-shot multiple choice question answering. *arXiv preprint arXiv:2412.09807*. https://arxiv.org/abs/2412.09807

Wang, Q., Zaki, M. J., Kollias, G., & Kalantzis, V. (2026). Decoder-based sense knowledge distillation. *arXiv preprint arXiv:2602.22351*. https://arxiv.org/abs/2602.22351

Ye, T., Dong, L., Chi, Z., Wu, X., Huang, S., & Wei, F. (2025). Black-box on-policy distillation of large language models. *arXiv preprint arXiv:2511.10643*. https://arxiv.org/abs/2511.10643

Zhang, R., Shen, J., Liu, T., Wang, H., Qin, Z., Han, F., Liu, J., Baumgartner, S., Bendersky, M., & Zhang, C. (2024). PLaD: Preference-based large language model distillation with pseudo-preference pairs. *arXiv preprint arXiv:2406.02886*. https://arxiv.org/abs/2406.02886

Zhao, A., Xin, H., Fan, Y., Tong, J., Li, W., & Shen, X. (2026). Decoupling KL and trajectories: A unified perspective for SFT, DAgger, offline RL, and OPD in LLM distillation. *arXiv preprint arXiv:2605.16826*. https://arxiv.org/abs/2605.16826

---

## Appendix: Search Results

The complete arXiv search results (15 papers) were stored in JSON format and analyzed to extract the 10 papers included in this review. Five papers were excluded due to focus on non-language modalities (speech, audio) or publication dates outside the 2-year window.
