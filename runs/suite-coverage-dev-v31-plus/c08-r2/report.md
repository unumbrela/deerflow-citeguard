# Systematic Literature Review: Advances in GRPO for Generation Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "GRPO generation models", filtered to category cs.LG, published between 2024-02-21 and 2026-02-20
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in Group Relative Policy Optimization (GRPO) for generation models, surveying 10 arXiv papers published between February 2024 and February 2026. The literature reveals a rapidly evolving field where researchers are addressing GRPO's fundamental limitations—particularly in credit assignment, exploration diversity, and theoretical understanding—while extending its applicability beyond language models to representation learning and flow-based generative models. A notable tension emerges in the literature: while most papers demonstrate empirical improvements through various GRPO enhancements, recent theoretical work cautions that GRPO operates as a conservative reweighting scheme bounded by the base model's pretraining distribution, suggesting its gains reflect sharpened pretraining biases rather than discovery of novel solutions. The field is converging on multi-turn, feedback-aware extensions and divergence-based theoretical frameworks as promising directions for future research.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "GRPO generation models", filtered to category cs.LG, published between 2024-02-21 and 2026-02-20. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, all extracted metadata comes from abstracts only, which may not capture full methodological details or limitations discussed in the complete papers.

## Themes

### Theme 1: Credit Assignment Improvements

A dominant research direction addresses GRPO's inability to assign fine-grained credit across token sequences, particularly critical for complex reasoning and multi-turn generation tasks. Parthasarathi et al. (2025) introduce GRPO-λ, which approximates learning from λ-return using eligibility traces with token-level log-probabilities applied after sequence generation, achieving 30-40% improved performance during RL training and over 3-point average improvement on mathematical reasoning benchmarks. Extending this to multi-turn settings, Ekbate et al. (2025) propose MURPHY, which constructs feedback-conditioned rollout trees where rewards propagate backward through failed solutions, delivering up to 6% absolute pass@1 gains on code generation tasks. For flow-based generative models, Zhou et al. (2025) develop Granular-GRPO (G²RPO) with Singular Stochastic Sampling and Multi-Granularity Advantage Integration, enabling step-wise stochastic exploration and aggregation across multiple diffusion scales to overcome sparse reward feedback. These works collectively demonstrate that fine-grained credit assignment—whether through temporal-difference approximations, backward propagation in multi-turn trees, or multi-scale advantage integration—consistently improves GRPO performance across diverse generation tasks.

### Theme 2: Exploration Enhancement and Diversity

GRPO's tendency toward gradient vanishing and diversity collapse has motivated several approaches to enhance exploration. Le et al. (2026) propose Transformation-Augmented GRPO (TA-GRPO), which generates problem-equivalent rephrasings of training questions to pool responses across original and transformed variants, computing advantages over the expanded set. This approach improves pass@k on competition-level benchmarks (AMC, OlympiadBench, AIME24, AIME25) and out-of-distribution benchmarks (Minerva, GPQA-Diamond), matching exploration quality of baselines trained on 2.5× more data. Bamba et al. (2025) present XRPO with three components: a mathematically grounded rollout allocator for adaptive prompt prioritization, in-context seeding for zero-reward prompts, and novelty-aware advantage sharpening that amplifies low-probability correct responses. XRPO outperforms GRPO and GSPO by up to 4% pass@1 and 6% cons@32 while accelerating training convergence by 2.7×. Both approaches share the insight that expanding the response space—through question rephrasing or adaptive prompt allocation—mitigates GRPO's exploration limitations without requiring additional training data.

### Theme 3: Theoretical Understanding and Fundamental Limits

Recent work has begun examining GRPO's theoretical foundations and inherent limitations. Ni et al. (2025) prove that GRPO operates as a conservative reweighting scheme bounded by the base model's distribution, unable to discover completely novel solutions beyond pretraining biases. Their controlled studies training transformers from scratch reveal that out-of-distribution improvement emerges only when target tasks align with pretrained biases, and gains on in-distribution tasks diminish as performance saturates. This theoretical perspective reframes GRPO as a tool that sharpens pretraining biases rather than a universal reasoning enhancer. Complementing this analysis, Haldar et al. (2026) introduce f-GRPO and f-Hybrid Alignment Loss (f-HAL), showing these objectives estimate f-divergences between reward-aligned and reward-unaligned distributions while proving expected reward improvement after alignment. Their divergence-based view provides a principled framework for designing alignment losses beyond preference-based supervision, with f-GRPO improving over standard GRPO on math-reasoning RLVR tasks and hybrid f-HAL mitigating reward hacking in on-policy safety alignment. These theoretical contributions caution against viewing GRPO as a panacea while offering principled extensions for broader alignment contexts.

### Theme 4: Multi-Turn and Self-Correction Mechanisms

Extending GRPO to multi-turn agentic settings where models must iteratively refine solutions has emerged as a significant research direction. Ekbate et al. (2025) develop MURPHY with feedback-conditioned rollout trees and backward reward propagation, achieving largest gains on Medium/Hard subsets (+4.38/+4.20 at Iter-5) where iterative self-correction matters most. Ding et al. (2025) propose Multi-Layer GRPO (MGRPO), a two-layer approach where the first layer employs standard GRPO for initial response generation and the second layer identifies and corrects errors, creating a self-correction loop with implicit process-level supervision without requiring explicit reward models. MGRPO significantly outperforms standard GRPO on mathematical reasoning benchmarks by rewarding error correction without densely-annotated reward models. Both approaches recognize that multi-turn generation requires different credit assignment mechanisms than single-turn tasks, with feedback propagation and self-correction loops providing implicit supervision signals that compensate for the absence of dense rewards.

### Theme 5: Efficiency and Scaling Laws

As GRPO training becomes more widespread, understanding its scaling behavior and optimizing resource usage has gained attention. Nimmaturi et al. (2025) derive empirical scaling laws based on model size, initial performance, and training progress that predict reward trajectories across Llama and Qwen models (3B-8B), identifying three consistent training phases: slow start, rapid improvement, and plateau. Their findings suggest training beyond a certain epoch offers little gain, enabling earlier stopping to reduce compute without sacrificing performance. Xu et al. (2025) extend GRPO beyond language models to representation learning with GRPO-RM, establishing a predefined output set to replace token sequence sampling and designing specialized reward functions for representation model properties. Their extensive experiments on real-world datasets validate GRPO's generalizability beyond LLM fine-tuning. These works provide practical guidance for efficient GRPO deployment: predictive scaling laws enable resource optimization, while GRPO-RM demonstrates the algorithm's applicability to non-language generation tasks.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several findings. First, all empirical papers report performance improvements over standard GRPO on their respective benchmarks, suggesting GRPO provides a solid foundation for RL-based fine-tuning across diverse generation tasks. Second, multiple papers independently identify credit assignment as GRPO's core limitation—whether through temporal-difference approximations (Parthasarathi et al., 2025), multi-turn backward propagation (Ekbate et al., 2025), or multi-scale advantage integration (Zhou et al., 2025). Third, exploration enhancement through response space expansion—via question rephrasing (Le et al., 2026) or adaptive prompt allocation (Bamba et al., 2025)—consistently improves performance without requiring additional training data.

**Disagreements**: A notable tension exists between empirical demonstrations of GRPO improvements and theoretical analysis of its fundamental limits. While most papers present GRPO enhancements as enabling new capabilities, Ni et al. (2025) caution that GRPO cannot transcend the base model's pretraining distribution, framing gains as sharpened biases rather than novel solution discovery. This theoretical perspective suggests empirical improvements may reflect better exploitation of existing capabilities rather than genuine capability expansion—a distinction with important implications for when GRPO fine-tuning is appropriate versus when architectural changes or different pretraining strategies may be necessary.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either limited self-critical analysis or space constraints in abstracts—full papers may contain more nuanced limitation discussions. Second, while theoretical work (Ni et al., 2025; Haldar et al., 2026) provides important foundations, the field lacks comprehensive theoretical frameworks explaining why specific GRPO variants work, under what conditions they fail, and how different enhancements interact. Third, most papers evaluate on mathematical reasoning or code generation benchmarks, with limited exploration of GRPO applications to creative generation, dialogue, or multimodal tasks. Fourth, the computational cost of GRPO variants—particularly multi-turn extensions and transformation-augmented approaches—receives limited attention despite practical deployment concerns. Finally, the relationship between GRPO fine-tuning and catastrophic forgetting of pretraining knowledge remains unexplored across the surveyed literature.

## Per-Paper Annotations

### Bamba et al. (2025)

**Research question**: How can GRPO be improved to address limited exploration on challenging prompts and underexploited feedback signals?
**Methodology**: XRPO (eXplore-eXploit GRPO) with a mathematically grounded rollout allocator for adaptive prompt prioritization, in-context seeding for zero-reward prompts, and a group-relative novelty-aware advantage sharpening mechanism.
**Key findings**:
- XRPO adaptively prioritizes prompts with higher potential for uncertainty reduction through a rollout allocator
- In-context seeding injects curated exemplars to steer models into more difficult reasoning trajectories on zero-reward prompts
- Novelty-aware advantage sharpening amplifies low-probability yet correct responses to extend policy reach beyond sparse rewards
- XRPO outperforms GRPO and GSPO by up to 4% pass@1 and 6% cons@32 across diverse math and coding benchmarks
- XRPO accelerates training convergence by up to 2.7X
**Limitations**: Not stated in abstract

### Ding et al. (2025)

**Research question**: How can the inefficient exploration dynamics and training instability caused by lack of intermediate supervision in GRPO be addressed?
**Methodology**: MGRPO (Multi-layer GRPO), a two-layer approach where the first layer employs standard GRPO to generate an initial response, and the second layer identifies and corrects errors in the initial response, creating a self-correction loop.
**Key findings**:
- MGRPO significantly outperforms standard GRPO on mathematical reasoning benchmarks
- The two-layer self-correction mechanism provides implicit process-level supervision
- Error correction is rewarded without requiring densely-annotated reward models
- The approach fosters both reasoning and self-correction abilities in LLMs
**Limitations**: Not stated in abstract

### Ekbate et al. (2025)

**Research question**: How can GRPO be extended to handle multi-turn agentic settings where models must iteratively refine solutions in response to environmental feedback?
**Methodology**: MURPHY, a multi-turn extension of GRPO that constructs feedback-conditioned rollout trees where failed solutions are paired with executor feedback and expanded into subsequent turns, with rewards propagated backward through the tree.
**Key findings**:
- MURPHY delivers up to 6% absolute pass@1 gains over prior multi-turn execution-feedback methods
- Gains are largest on Medium/Hard subsets (+4.38/+4.20 at Iter-5) where iterative self-correction matters more
- Backward reward propagation credits earlier attempts that surfaced informative feedback
- Post-rollout pruning mechanisms reduce multi-turn optimization cost
**Limitations**: Not stated in abstract

### Haldar et al. (2026)

**Research question**: How can preference alignment objectives be extended from preference-based supervision to general LLM alignment with scalar rewards?
**Methodology**: f-Group Relative Policy Optimization (f-GRPO) and f-Hybrid Alignment Loss (f-HAL), showing these objectives estimate f-divergences between reward-aligned and reward-unaligned distributions and prove expected reward improvement after alignment.
**Key findings**:
- Preference alignment objectives can be interpreted as divergence estimators between aligned and unaligned distributions
- f-GRPO improves over GRPO on math-reasoning RLVR tasks
- Hybrid f-HAL mitigates reward hacking in on-policy safety alignment when verifiable rewards are unavailable
- The divergence-based view provides a principled recipe for designing alignment losses beyond preference-based supervision
**Limitations**: Not stated in abstract

### Le et al. (2026)

**Research question**: How can GRPO's gradient vanishing and diversity collapse problems be addressed to improve exploration in reasoning tasks?
**Methodology**: TA-GRPO generates multiple problem-equivalent rephrasings of training questions that alter wording, format, and information order while preserving meaning, with responses pooled across original and rephrased questions to yield mixed rewards and diverse reasoning paths.
**Key findings**:
- TA-GRPO consistently improves pass@k on competition-level benchmarks (AMC, OlympiadBench, AIME24, AIME25)
- The method also improves out-of-distribution benchmark performance (Minerva, GPQA-Diamond)
- Average pass@32 of Qwen3-1.7B and Qwen3-4B improves by 4.97 and 4.34 points respectively
- TA-GRPO matches exploration quality of baselines trained on up to 2.5× more data
**Limitations**: Not stated in abstract

### Ni et al. (2025)

**Research question**: Under what conditions does GRPO improve reasoning and generalize out-of-distribution?
**Methodology**: Theoretical proof that GRPO is a conservative reweighting scheme bounded by the base model's distribution, validated through controlled studies training transformers from scratch across reasoning depth, input length, token representation, and compositionality.
**Key findings**:
- GRPO is a conservative reweighting scheme unable to discover completely novel solutions beyond the base model's distribution
- Out-of-distribution improvement emerges only when the target task aligns with the model's pretrained biases
- Gains on in-distribution tasks diminish as performance saturates
- GRPO should be viewed as a tool that sharpens pretraining biases rather than a universal reasoning enhancer
**Limitations**: Not stated in abstract

### Nimmaturi et al. (2025)

**Research question**: How can training dynamics be modeled to optimize resource usage in GRPO-based fine-tuning of large language models?
**Methodology**: Experiments on Llama and Qwen models (3B-8B) to derive an empirical scaling law based on model size, initial performance, and training progress that predicts reward trajectories and identifies three training phases.
**Key findings**:
- Training dynamics follow three consistent phases: slow start, rapid improvement, and plateau
- Training beyond a certain epoch offers little gain, suggesting earlier stopping can reduce compute without sacrificing performance
- The predictive approach generalizes across model types, providing a practical guide for efficient GRPO-based fine-tuning
**Limitations**: Not stated in abstract

### Parthasarathi et al. (2025)

**Research question**: How can GRPO's inability to assign fine-grained credit across token sequences be improved for complex reasoning tasks?
**Methodology**: GRPO-λ approximates learning from λ-return using a reformulation of eligibility traces with token-level log-probabilities applied after sequence generation, plus a novel critic-free approximation of temporal-difference error.
**Key findings**:
- GRPO-λ achieves 30-40% improved performance during RL training on LLaMA-3.1 and Qwen-2.5 architectures
- Average performance on AIME24, Math500, OlympiadMath, MinervaMath, and AMC improves over GRPO by over 3 points
- The 7B model shows a 4.5 points improvement on benchmark performance
- All variations of the method provide significant gains over standard GRPO
**Limitations**: Not stated in abstract

### Xu et al. (2025)

**Research question**: Can Group Relative Policy Optimization (GRPO), successful for fine-tuning large language models, be generalized to representation learning models?
**Methodology**: GRPO-RM establishes a predefined output set to replace token sequence sampling in LLMs, generating an output group for probability-driven optimization, with a specialized reward function designed for representation model properties.
**Key findings**:
- GRPO can be successfully adapted from LLM fine-tuning to representation model post-training
- A predefined output set functionally replaces token sequence sampling to generate output groups
- A specialized reward function accommodates representation model properties
- Extensive experiments on various real-world datasets validate the method's effectiveness
**Limitations**: Not stated in abstract

### Zhou et al. (2025)

**Research question**: How can flow-based generative models better align with human preferences despite sparse and narrow reward feedback?
**Methodology**: Granular-GRPO (G²RPO) with a Singular Stochastic Sampling mechanism for step-wise stochastic exploration and a Multi-Granularity Advantage Integration module that aggregates advantages across multiple diffusion scales.
**Key findings**:
- G²RPO enables fine-grained and comprehensive evaluation of sampling directions in RL training of flow models
- Singular Stochastic Sampling ensures strong correlation between injected noise and reward signals for accurate credit assignment
- Multi-Granularity Advantage Integration mitigates bias from fixed-granularity denoising for more robust trajectory assessment
- G²RPO outperforms existing flow-based GRPO baselines in both in-domain and out-of-domain settings
**Limitations**: Not stated in abstract

## References

Bamba, U., Fang, M., Yu, Y., Zheng, H., & Lai, F. (2025). XRPO: Pushing the limits of GRPO with Targeted Exploration and Exploitation. arXiv. https://arxiv.org/abs/2510.06672

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-Layer GRPO: Enhancing Reasoning and Self-Correction in Large Language Models. arXiv. https://arxiv.org/abs/2506.04746

Chanakya Ekbate, Lingam, V., Sanghavi, S., Huan, J., Omidvar-Tehrani, B., Deoras, A., & Soatto, S. (2025). MURPHY: Feedback-Aware GRPO with Retrospective Credit Assignment for Multi-Turn Code Generation. arXiv. https://arxiv.org/abs/2511.07833

Haldar, R., Mei, L., Lin, G., Xing, Y., & Song, Q. (2026). f-GRPO and Beyond: Divergence-Based Reinforcement Learning Algorithms for General LLM Alignment. arXiv. https://arxiv.org/abs/2602.05946

Le, K., Nguyen, P., Mroueh, Y., Lin, C.-H., Gao, S., Hua, T., & Chawla, N. V. (2026). Transformation-Augmented GRPO for Enhancing Exploration in Reasoning of Large Language Models. arXiv. https://arxiv.org/abs/2601.22478

Ni, K., Tan, Z., Liu, Z., Li, P., & Chen, T. (2025). Can GRPO Help LLMs Transcend Their Pretraining Origin? arXiv. https://arxiv.org/abs/2510.15990

Nimmaturi, D., Bhargava, V., Ghosh, R., George, J., & Dutta, D. (2025). Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models. arXiv. https://arxiv.org/abs/2507.18014

Parthasarathi, P., Reymond, M., Chen, B., Cui, Y., & Chandar, S. (2025). GRPO-$λ$: Credit Assignment improves LLM Reasoning. arXiv. https://arxiv.org/abs/2510.00194

Xu, Y., Jiao, Z., Zhang, H., & Li, X. (2025). GRPO-RM: Fine-Tuning Representation Models via GRPO-Driven Reinforcement Learning. arXiv. https://arxiv.org/abs/2511.15256

Zhou, Y., Ling, P., Bu, J., Wang, Y., Zang, Y., Wang, J., Niu, L., & Zhai, G. (2025). Fine-Grained GRPO for Precise Preference Alignment in Flow Models. arXiv. https://arxiv.org/abs/2510.01982
