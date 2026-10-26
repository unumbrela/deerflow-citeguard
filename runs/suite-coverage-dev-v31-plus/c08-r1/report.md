# Systematic Literature Review: Advances in GRPO for Generation Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "GRPO generation models", category cs.LG, published between 2024-02-21 and 2026-02-20
**Citation format**: APA 7th edition

## Executive Summary

Group Relative Policy Optimization (GRPO) has emerged as a significant reinforcement learning approach for fine-tuning generation models, particularly large language models and flow-based generative systems. The ten papers surveyed reveal a rapidly evolving field focused on addressing GRPO's core limitations: credit assignment, exploration diversity, training efficiency, and generalization bounds. Recent advances span multi-layer architectures for self-correction, transformation-augmented exploration, fine-grained preference alignment for flow models, and divergence-based theoretical frameworks. Collectively, these works demonstrate that GRPO's effectiveness depends critically on the alignment between pretrained model biases and target tasks, with substantial gains achievable through targeted modifications to the optimization process. The field is moving toward more sophisticated credit assignment mechanisms and hybrid approaches that combine on-policy RL with off-policy supervision.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "GRPO generation models", filtered to category cs.LG, published between 2024-02-21 and 2026-02-20. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Credit Assignment and Reward Optimization

A central challenge in GRPO is assigning credit to individual tokens or steps within generated sequences, particularly for complex reasoning tasks. Multiple papers address this through novel mechanisms that provide finer-grained supervision without requiring explicit reward or critic models. Parthasarathi et al. (2025) introduced GRPO-λ, which approximates λ-return using eligibility traces with token-level log-probabilities and a critic-free temporal-difference error approximation, achieving 30-40% improved performance over standard GRPO. Zhou et al. (2025) extended this to flow models with Granular-GRPO, employing Singular Stochastic Sampling for step-wise exploration and Multi-Granularity Advantage Integration across diffusion scales. Ekbate et al. (2025) tackled multi-turn code generation with MURPHY, which constructs feedback-conditioned rollout trees and propagates rewards backward using Max Reward and Mean Reward strategies. These approaches share a common insight: effective credit assignment requires temporal decomposition of the generation process and reward signal propagation across multiple granularities.

### Theme 2: Exploration and Diversity Enhancement

GRPO suffers from gradient vanishing and diversity collapse, limiting exploration on challenging prompts. Two papers propose complementary solutions to this problem. Le et al. (2026) developed Transformation-Augmented GRPO (TA-GRPO), which generates problem-equivalent rephrasings of training questions and jointly computes advantages over the expanded response set, improving pass@32 by 4.97 points on Qwen3-1.7B. Bamba et al. (2025) introduced XRPO, featuring a mathematically grounded rollout allocator that adaptively prioritizes uncertain prompts, in-context seeding for zero-reward prompts, and novelty-aware advantage sharpening. Both approaches demonstrate that expanding the exploration space—whether through question rephrasing or adaptive rollout allocation—significantly improves performance on competition-level benchmarks while accelerating training convergence by up to 2.7×.

### Theme 3: Multi-Layer and Self-Correction Architectures

Moving beyond single-pass optimization, recent work explores hierarchical architectures that enable self-correction and iterative refinement. Ding et al. (2025) proposed Multi-Layer GRPO (MGRPO), a two-layer approach where the first layer generates an initial response and the second layer identifies and corrects errors, creating a self-correction loop that provides implicit process-level supervision. This architecture significantly outperforms standard GRPO on mathematical reasoning benchmarks without requiring an explicit reward model. Similarly, Ekbate et al. (2025) extended GRPO to multi-turn agentic settings where models iteratively refine solutions in response to environmental feedback, achieving up to 6% absolute pass@1 gains on code generation benchmarks. These works suggest that GRPO's effectiveness increases when the optimization process incorporates intermediate supervision and iterative refinement mechanisms.

### Theme 4: Theoretical Foundations and Generalization Bounds

A critical theoretical question concerns GRPO's ability to generalize beyond the pretrained model's distribution. Ni et al. (2025) provided a theoretical analysis proving that GRPO is a conservative reweighting scheme bounded by the base model's distribution, unable to discover completely novel solutions. Their controlled studies training transformers from scratch revealed that out-of-distribution improvement emerges only when the target task aligns with pretrained biases, and in-distribution gains diminish as performance saturates. This work reframes GRPO as a tool that sharpens pretraining biases rather than a universal reasoning enhancer. Haldar et al. (2026) extended this theoretical perspective by introducing f-GRPO, showing that preference alignment objectives can be interpreted as f-divergence estimators between aligned and unaligned distributions, with proven expected reward improvement after alignment. These theoretical contributions provide crucial guidance for when and how to apply GRPO effectively.

### Theme 5: Efficiency and Scaling Laws

As GRPO is applied to increasingly large models, computational efficiency becomes paramount. Nimmaturi et al. (2025) derived empirical scaling laws for GRPO training based on model size, initial performance, and training progress, identifying three consistent phases: slow start, rapid improvement, and plateau. Their experiments on Llama and Qwen models (3B-8B) revealed that training beyond a certain epoch offers diminishing returns, suggesting earlier stopping can reduce compute without sacrificing performance. This work provides a practical guide for efficient GRPO-based fine-tuning that generalizes across model types. The efficiency theme also appears in XRPO (Bamba et al., 2025), which accelerates training convergence by up to 2.7× through targeted exploration and exploitation strategies.

### Theme 6: Generalization Beyond Language Models

GRPO's applicability extends beyond traditional language models to other generative architectures. Xu et al. (2025) demonstrated that GRPO can be generalized to representation learning models through GRPO-RM, which establishes a predefined output set to replace token sequence sampling and employs a specialized reward function for representation models. Zhou et al. (2025) applied GRPO to flow-based generative models with Granular-GRPO, addressing the unique challenges of sparse and narrow reward feedback in diffusion-based systems. Haldar et al. (2026) extended the divergence-based view to general LLM alignment with scalar reward feedback, introducing hybrid f-HAL that combines on-policy reward optimization with off-policy preference supervision. These works collectively demonstrate GRPO's versatility across different generative model architectures.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the insight that standard GRPO requires augmentation to address its core limitations. There is broad agreement that credit assignment benefits from temporal decomposition and multi-granularity evaluation (Parthasarathi et al., 2025; Zhou et al., 2025; Ekbate et al., 2025). The surveyed papers also agree that exploration diversity is critical for performance on challenging reasoning tasks, with multiple approaches demonstrating significant gains through expanded search spaces (Le et al., 2026; Bamba et al., 2025). Additionally, there is consensus that GRPO's effectiveness is bounded by the pretrained model's capabilities and biases (Ni et al., 2025; Haldar et al., 2026).

**Disagreements**: A notable tension exists between works that propose architectural extensions (multi-layer, multi-turn) versus those that focus on theoretical bounds. While Ding et al. (2025) and Ekbate et al. (2025) demonstrate substantial gains through hierarchical architectures, Ni et al. (2025) caution that such improvements are fundamentally limited by the base model's distribution. This suggests a potential ceiling on GRPO's effectiveness that architectural modifications alone cannot overcome. Additionally, there is disagreement about the necessity of explicit reward models: while some approaches successfully operate without them (Ding et al., 2025; Parthasarathi et al., 2025), others incorporate hybrid supervision (Haldar et al., 2026).

## Gaps and Open Questions

The surveyed literature reveals several notable gaps. First, none of the papers explicitly discuss computational costs or resource requirements in detail, despite the focus on efficiency—this limits practical deployment guidance. Second, while theoretical analyses establish GRPO's conservative nature (Ni et al., 2025; Haldar et al., 2026), there is limited guidance on how to identify when pretrained biases align with target tasks in practice. Third, most evaluations focus on mathematical reasoning and code generation benchmarks, with limited exploration of other domains such as creative generation, dialogue, or multimodal tasks. Fourth, the interaction between GRPO and different model architectures (beyond transformers and flow models) remains underexplored. Finally, long-term stability and catastrophic forgetting during GRPO fine-tuning are not addressed in the surveyed papers, representing a critical gap for practical deployment.

## Per-Paper Annotations

### Bamba et al. (2025)

**Research question**: How can GRPO be improved to address limited exploration on challenging prompts and underexploited feedback signals?
**Methodology**: The authors present XRPO, a framework with a mathematically grounded rollout allocator that adaptively prioritizes uncertain prompts, an in-context seeding strategy for zero-reward prompts, and a group-relative novelty-aware advantage sharpening mechanism.
**Key findings**:
- XRPO adaptively allocates rollouts to prompts with higher potential for uncertainty reduction
- In-context seeding strategy injects curated exemplars to steer models into more difficult reasoning trajectories on zero-reward prompts
- Novelty-aware advantage sharpening amplifies low-probability yet correct responses using sequence likelihoods
- XRPO outperforms GRPO and GSPO by up to 4% pass@1 and 6% cons@32 on math and coding benchmarks
- XRPO accelerates training convergence by up to 2.7X
**Limitations**: not stated in abstract

### Ding et al. (2025)

**Research question**: How can the lack of intermediate supervision in GRPO be addressed to improve exploration dynamics and training stability in LLM reasoning?
**Methodology**: The authors propose MGRPO (Multi-layer GRPO), a two-layer approach where the first layer employs standard GRPO to generate an initial response, and the second layer is trained to identify and correct errors in the initial response, creating a self-correction loop that provides implicit process-level supervision.
**Key findings**:
- MGRPO significantly outperforms standard GRPO on mathematical reasoning benchmarks
- The two-layer architecture creates a self-correction loop that identifies and corrects errors in initial responses
- The mechanism provides implicit process-level supervision by rewarding successful error correction without requiring an explicit reward model
- MGRPO fosters both reasoning and self-correction abilities, achieving superior performance
**Limitations**: not stated in abstract

### Chanakya Ekbate et al. (2025)

**Research question**: How can GRPO be extended to handle multi-turn agentic settings where models must iteratively refine solutions in response to environmental feedback?
**Methodology**: The authors introduce MURPHY, a multi-turn extension of GRPO that constructs feedback-conditioned rollout trees where failed candidate solutions are paired with executor feedback and expanded into subsequent turns, with rewards propagated backward through the tree using Max Reward (MARS) and Mean Reward (MERS) strategies.
**Key findings**:
- MURPHY delivers up to 6% absolute pass@1 gains over the strongest prior multi-turn execution-feedback methods across three code generation benchmarks
- Gains are largest on Medium/Hard subsets (+4.38/+4.20 at Iter-5), where iterative self-correction matters more
- Two propagation strategies (MARS and MERS) are studied with post-rollout pruning mechanisms that reduce multi-turn optimization cost
- The method works across two model families (Qwen3-1.7B/4B, OLMo-2-7B) on HumanEval, MBPP, and LiveCodeBench-v6 benchmarks
**Limitations**: not stated in abstract

### Haldar et al. (2026)

**Research question**: How can the divergence-based view of preference alignment be extended to general LLM alignment with scalar reward feedback?
**Methodology**: The authors introduce f-GRPO (a class of on-policy RL objectives) and f-HAL (combining on-policy reward optimization with off-policy preference supervision), showing these estimate f-divergences between reward-aligned and reward-unaligned distributions and proving expected reward improvement after alignment.
**Key findings**:
- Preference alignment objectives can be interpreted as divergence estimators between aligned and unaligned distributions
- f-GRPO improves over GRPO on math-reasoning RLVR tasks
- Hybrid f-HAL mitigates reward hacking in on-policy safety alignment when verifiable rewards are unavailable
- The divergence-based view extends to general LLM alignment including RLVR with scalar reward feedback
**Limitations**: not stated in abstract

### Le et al. (2026)

**Research question**: How can GRPO's gradient vanishing and diversity collapse problems be addressed to improve exploration in LLM reasoning?
**Methodology**: The authors propose TA-GRPO, which generates multiple problem-equivalent rephrasings of training questions that alter wording, format, and information order while preserving meaning, then jointly computes advantages over the expanded response set pooled across original and rephrased questions.
**Key findings**:
- TA-GRPO consistently improves pass@k on competition-level benchmarks (AMC, OlympiadBench, AIME24, AIME25) and out-of-distribution benchmarks (Minerva, GPQA-Diamond)
- TA-GRPO improves the average pass@32 of Qwen3-1.7B and Qwen3-4B by 4.97 and 4.34 points respectively
- The method matches the exploration quality of baselines trained on up to 2.5× more data
- TA-GRPO addresses both gradient vanishing and diversity collapse through question rephrasing
**Limitations**: not stated in abstract

### Ni et al. (2025)

**Research question**: Under what conditions does GRPO improve reasoning and generalize out-of-distribution?
**Methodology**: The authors theoretically prove that GRPO is a conservative reweighting scheme bounded by the base model's distribution, and validate this through controlled studies training transformers from scratch while evaluating generalization across reasoning depth, input length, token representation, and compositionality.
**Key findings**:
- GRPO is a conservative reweighting scheme bounded by the base model's distribution and cannot discover completely novel solutions
- Out-of-distribution improvement emerges only when the target task aligns with the model's pretrained biases
- Gains on in-distribution tasks diminish as performance saturates
- GRPO should be reframed as a tool that sharpens pretraining biases rather than a universal reasoning enhancer
**Limitations**: not stated in abstract

### Nimmaturi et al. (2025)

**Research question**: How can GRPO training be optimized to reduce computational costs while maintaining performance?
**Methodology**: The authors conducted experiments on Llama and Qwen models (3B-8B) to derive an empirical scaling law based on model size, initial performance, and training progress, modeling reward trajectories across three training phases.
**Key findings**:
- Training dynamics follow three consistent phases: slow start, rapid improvement, and plateau
- Training beyond a certain epoch offers little gain, suggesting earlier stopping can reduce compute without sacrificing performance
- The approach generalizes across model types, providing a practical guide for efficient GRPO-based fine-tuning
- An empirical scaling law can predict reward trajectories based on model size, initial performance, and training progress
**Limitations**: not stated in abstract

### Parthasarathi et al. (2025)

**Research question**: How can fine-grained credit assignment be improved in GRPO for complex reasoning tasks without using an explicit reward or critic model?
**Methodology**: The authors present GRPO-λ, which enhances credit assignment by approximating learning from λ-return using a reformulation of eligibility traces with token-level log-probabilities and a novel critic-free approximation of temporal-difference error applied after each sequence generation.
**Key findings**:
- GRPO-λ demonstrates 30-40% improved performance during RL training compared to GRPO on both LLaMA-3.1 and Qwen-2.5 architectures
- Average performance on AIME24, Math500, OlympiadMath, MinervaMath, and AMC improves over GRPO by over 3 points
- A 4.5 points improvement is achieved on the 7B model
- All variations of λ-return weighting provide significant gains over standard GRPO
**Limitations**: not stated in abstract

### Xu et al. (2025)

**Research question**: Can Group Relative Policy Optimization (GRPO), a reinforcement learning method for fine-tuning LLMs, be generalized to representation learning models?
**Methodology**: The authors propose GRPO-RM, which establishes a predefined output set to replace token sequence sampling in LLMs, generating an output group for probability-driven optimization. A specialized reward function is designed to accommodate the properties of representation models.
**Key findings**:
- GRPO can be successfully generalized from LLMs to representation learning models through the GRPO-RM framework
- A predefined output set functionally replaces token sequence sampling to generate output groups essential for GRPO optimization
- A specialized reward function accommodates the unique properties of representation models
- Extensive experiments on various real-world datasets validate the effectiveness of the proposed method
**Limitations**: not stated in abstract

### Zhou et al. (2025)

**Research question**: How can flow-based generative models better align with human preferences despite sparse and narrow reward feedback?
**Methodology**: The authors introduce Granular-GRPO (G²RPO) with a Singular Stochastic Sampling mechanism for step-wise stochastic exploration and a Multi-Granularity Advantage Integration module that aggregates advantages across multiple diffusion scales.
**Key findings**:
- Current flow-based RL approaches struggle with preference alignment due to sparse and narrow reward feedback
- G²RPO enables fine-grained and comprehensive evaluation of sampling directions in RL training of flow models
- Singular Stochastic Sampling ensures strong correlation between injected noise and reward signals for accurate credit assignment
- Multi-Granularity Advantage Integration provides more robust assessment of sampling trajectories by aggregating across diffusion scales
- G²RPO outperforms existing flow-based GRPO baselines on both in-domain and out-of-domain settings
**Limitations**: not stated in abstract

## References

Bamba, U., Fang, M., Yu, Y., Zheng, H., & Lai, F. (2025). XRPO: Pushing the limits of GRPO with Targeted Exploration and Exploitation. arXiv. https://arxiv.org/abs/2510.06672

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-Layer GRPO: Enhancing Reasoning and Self-Correction in Large Language Models. arXiv. https://arxiv.org/abs/2506.04746

Ekbate, C., Lingam, V., Sanghavi, S., Huan, J., Omidvar-Tehrani, B., Deoras, A., & Soatto, S. (2025). MURPHY: Feedback-Aware GRPO with Retrospective Credit Assignment for Multi-Turn Code Generation. arXiv. https://arxiv.org/abs/2511.07833

Haldar, R., Mei, L., Lin, G., Xing, Y., & Song, Q. (2026). f-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment. arXiv. https://arxiv.org/abs/2602.05946

Le, K., Nguyen, P., Mroueh, Y., Lin, C.-H., Gao, S., Hua, T., & Chawla, N. V. (2026). Transformation-Augmented GRPO for Enhancing Exploration in Reasoning of Large Language Models. arXiv. https://arxiv.org/abs/2601.22478

Ni, K., Tan, Z., Liu, Z., Li, P., & Chen, T. (2025). Can GRPO Help LLMs Transcend Their Pretraining Origin? arXiv. https://arxiv.org/abs/2510.15990

Nimmaturi, D., Bhargava, V., Ghosh, R., George, J., & Dutta, D. (2025). Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models. arXiv. https://arxiv.org/abs/2507.18014

Parthasarathi, P., Reymond, M., Chen, B., Cui, Y., & Chandar, S. (2025). GRPO-λ: Credit Assignment improves LLM Reasoning. arXiv. https://arxiv.org/abs/2510.00194

Xu, Y., Jiao, Z., Zhang, H., & Li, X. (2025). GRPO-RM: Fine-Tuning Representation Models via GRPO-Driven Reinforcement Learning. arXiv. https://arxiv.org/abs/2511.15256

Zhou, Y., Ling, P., Bu, J., Wang, Y., Zang, Y., Wang, J., Niu, L., & Zhai, G. (2025). Fine-Grained GRPO for Precise Preference Alignment in Flow Models. arXiv. https://arxiv.org/abs/2510.01982
