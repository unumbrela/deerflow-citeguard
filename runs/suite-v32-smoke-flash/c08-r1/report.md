# Systematic Literature Review: Advances in GRPO for Generation Models

## Executive Summary

This systematic literature review examines ten recent advances in Group Relative Policy Optimization (GRPO) for generation models, published between February 21, 2024 and February 20, 2026, within the computer science machine learning category (cs.LG). GRPO has emerged as a leading reinforcement learning approach with verifiable rewards for fine-tuning large language models (LLMs), particularly demonstrated by systems like DeepSeek-R1. This review synthesizes key innovations across five thematic areas: (1) extending GRPO to representation learning and flow models, (2) enhancing multi-turn reasoning and self-correction capabilities, (3) improving credit assignment mechanisms, (4) optimizing training efficiency through scaling laws, and (5) addressing fundamental limitations around exploration and distributional boundaries.

## Introduction

Group Relative Policy Optimization (GRPO) represents a significant advancement in reinforcement learning with verifiable rewards (RLVR) for post-training LLMs. Unlike traditional policy gradient methods that require learned value functions or critics, GRPO employs group-relative advantages computed from multiple sampled responses, eliminating the need for separate critic models while maintaining training stability. The algorithm's effectiveness in reasoning tasks has spurred rapid research innovation, with ten notable papers emerging in the specified timeframe that address various limitations and extend applicability to new domains.

## Thematic Analysis

### 1. Extending GRPO Beyond Language Models

#### GRPO for Representation Learning
Xu et al. (2025) proposed **GRPO-RM**, which adapts GRPO principles to representation models rather than autoregressive language models [citation:GRPO-RM](https://arxiv.org/abs/2511.15256v1). Their key innovation involves establishing a predefined output set to functionally replace token sequence sampling, thereby generating the output groups essential for probability-driven optimization. They designed specialized reward functions accommodating representation model properties, validating their method on various real-world datasets. This work demonstrates GRPO's generalizability beyond sequential generation tasks.

#### Fine-Grained Alignment in Flow Models
Zhou et al. (2025) introduced **Granular-GRPO (G²RPO)** for preference alignment in diffusion and flow-based generative models [citation:Fine-Grained GRPO](https://arxiv.org/abs/2510.01982v3). Their framework addresses the challenge of sparse and narrow reward feedback during RL training of continuous-generation models. Key contributions include:
- **Singular Stochastic Sampling**: Enables step-wise stochastic exploration while maintaining strong correlation between injected noise and reward signals
- **Multi-Granularity Advantage Integration**: Aggregates advantages across multiple diffusion scales for robust trajectory assessment

Their experiments demonstrate G²RPO outperforms existing flow-based GRPO baselines in both in-domain and out-of-domain settings.

#### Divergence-Based Generalization
Haldar et al. (2026) developed **f-GRPO**, interpreting preference alignment objectives as divergence estimators between aligned and unaligned distributions [citation:f-GRPO](https://arxiv.org/abs/2602.05946v3). They extended this view to general LLM alignment including RLVR scenarios where only scalar rewards are available. Their contributions include:
- **f-GRPO**: A class of on-policy RL objectives estimating f-divergences between reward-aligned and unaligned distributions
- **f-Hybrid Alignment Loss (f-HAL)**: Combines on-policy reward optimization with off-policy preference supervision

Theoretical proofs establish expected reward improvement after alignment, while empirical results show improvements on math-reasoning tasks and mitigation of reward hacking in safety alignment.

### 2. Multi-Turn Reasoning and Self-Correction

#### Layered Self-Correction Architecture
Ding et al. (2025) proposed **Multi-Layer GRPO (MGRPO)** to address inefficient exploration dynamics caused by absent intermediate supervision [citation:Multi-Layer GRPO](https://arxiv.org/abs/2506.04746v1). Their two-layer architecture operates as follows:
1. **First layer**: Standard GRPO generates initial response
2. **Second layer**: Trained to identify and correct errors in initial response

This mechanism provides implicit process-level supervision by rewarding successful error correction without requiring densely-annotated reward models. Experimental results on mathematical reasoning benchmarks show MGRPO significantly outperforms standard GRPO by fostering both reasoning and self-correction abilities.

#### Feedback-Aware Multi-Turn Code Generation
Ekbote et al. (2025) introduced **MURPHY**, a multi-turn extension specifically designed for self-correcting code generation [citation:MURPHY](https://arxiv.org/abs/2511.07833v3). Unlike single-turn GRPO variants, MURPHY constructs feedback-conditioned rollout trees where:
- Failed candidate solutions pair with executor feedback
- Expanded into subsequent turns
- Rewards propagate backward so later successful refinements credit earlier attempts that surfaced informative feedback

They studied two propagation strategies—Max Reward (MARS) and Mean Reward (MERS)—and introduced post-rollout pruning mechanisms. Across HumanEval, MBPP, and LiveCodeBench-v6 benchmarks, MURPHY delivered up to 6% absolute pass@1 gains over prior multi-turn execution-feedback methods, with largest gains (+4.38/+4.20 at Iter-5) on Medium/Hard subsets where iterative self-correction matters most.

### 3. Enhanced Credit Assignment Mechanisms

#### Temporal-Difference Error Approximation
Parthasarathi et al. (2025) presented **GRPO-λ**, addressing GRPO's limitation in assigning fine-grained credit across token sequences due to lack of explicit reward or critic models [citation:GRPO-λ](https://arxiv.org/abs/2510.00194v1). Their approach approximates learning from λ-return through:
- Reformulation of eligibility traces using token-level log-probabilities applied after each sequence generation
- Novel critic-free approximation of temporal-difference error

Training plots demonstrated 30-40% improved performance during RL training on both LLaMA-3.1 and Qwen-2.5 architectures. Final evaluation showed average performance improvements over GRPO by over 3 points across AIME24, Math500, OlympiadMath, MinervaMath, and AMC, with 4.5-point improvement on 7B models.

#### Exploration-Exploitation Balance
Bamba et al. (2025) developed **XRPO (eXplore-eXploit GRPO)**, recasting policy optimization through rollout exploration-exploitation lens [citation:XRPo](https://arxiv.org/abs/2510.06672v3). Their unified framework includes:
- **Adaptive Rollout Allocator**: Mathematically grounded allocator prioritizing prompts with higher uncertainty reduction potential
- **In-Context Seeding Strategy**: Injects curated exemplars on zero-reward prompts to steer toward difficult reasoning trajectories
- **Novelty-Aware Advantage Sharpening**: Leverages sequence likelihoods to amplify low-probability yet correct responses

Experiments across diverse math and coding benchmarks demonstrated XRPO outperforming existing advances up to 4% pass@1 and 6% cons@32, while accelerating training convergence by up to 2.7X.

### 4. Training Efficiency and Scaling Laws

#### Predictive Training Dynamics Framework
Nimmaturi et al. (2025) proposed a predictive framework modeling GRPO training dynamics to optimize resource usage [citation:Scaling Laws](https://arxiv.org/abs/2507.18014v3). Through experiments on Llama and Qwen models (3B/8B), they derived an empirical scaling law based on:
- Model size
- Initial performance
- Training progress

Their analysis identified three consistent training phases: slow start, rapid improvement, and plateau. Critically, they found training beyond certain epochs offers little gain, suggesting earlier stopping can significantly reduce compute without sacrificing performance. This approach generalizes across model types, providing practical guidance for efficient GRPO-based fine-tuning.

### 5. Fundamental Limitations and Boundaries

#### Distributional Constraints
Ni et al. (2025) investigated conditions under which GRPO improves reasoning and generalizes out-of-distribution (OOD) [citation:Pretraining Origin](https://arxiv.org/abs/2510.15990v1). Their theoretical proof establishes that GRPO is a conservative reweighting scheme bounded by the base model's distribution, thus unable to discover completely novel solutions. Controlled studies evaluating transformers trained from scratch assessed generalization across:
- Reasoning depth
- Input length
- Token representation
- Compositionality

Results provide principled explanation for GRPO's boundaries: OOD improvement emerges only when target task aligns with model's pretrained biases, while gains on in-distribution tasks diminish as performance saturates. This reframes GRPO not as universal reasoning enhancer but as tool sharpening pretraining biases.

#### Diversity Collapse Mitigation
Le et al. (2026) proposed **Transformation-Augmented GRPO (TA-GRPO)** addressing critical limitations of gradient vanishing and diversity collapse [citation:TA-GRPO](https://arxiv.org/abs/2601.22478v5). When training questions are too easy or too hard, all sampled responses receive identical rewards yielding zero gradients, while models tend to collapse toward single reasoning patterns. TA-GRPO addresses both via question rephrasing:
- Automatically generates multiple problem-equivalent rephrasings altering wording, format, and information order while preserving meaning
- Rephrasings shift model's perceived difficulty
- Pooling responses across original and rephrasings yields mixed rewards and diverse reasoning paths
- Jointly computes advantages over expanded response set, aligning all importance ratios to original question

Experiments on four LLMs (Qwen3-1.7B, Qwen3-4B, Llama-3.2-1B, Llama-3.2-3B) showed TA-GRPO consistently improving pass@$k$ on competition-level benchmarks (AMC, OlympiadBench, AIME24, AIME25) and OOD benchmarks (Minerva, GPQA-Diamond). Notably, it improved average pass@32 of Qwen3-1.7B and Qwen3-4B by 4.97 and 4.34 points respectively, matching exploration quality of baselines trained on up to 2.5× more data.

## Comparative Analysis

| Paper | Key Innovation | Domain | Performance Gain |
|-------|---------------|--------|------------------|
| GRPO-RM (Xu et al., 2025) | Representation model adaptation | Embedding models | Validated on real-world datasets |
| Multi-Layer GRPO (Ding et al., 2025) | Two-layer self-correction | Mathematical reasoning | Superior to standard GRPO |
| MURPHY (Ekbote et al., 2025) | Feedback-conditioned rollout trees | Code generation | +6% pass@1 |
| GRPO-λ (Parthasarathi et al., 2025) | Eligibility traces with TD error | Math reasoning | +3-4.5 points |
| TA-GRPO (Le et al., 2026) | Question rephrasing augmentation | Competition math | +4.97/+4.34 points |
| Pretraining Origin (Ni et al., 2025) | Distributional boundary analysis | General | Theoretical characterization |
| Scaling Laws (Nimmaturi et al., 2025) | Predictive training dynamics | Resource optimization | Earlier stopping viable |
| Fine-Grained GRPO (Zhou et al., 2025) | Step-wise flow model alignment | Diffusion/flow models | Outperforms baselines |
| f-GRPO (Haldar et al., 2026) | Divergence-based alignment | General alignment | Improves RLVR tasks |
| XRPO (Bamba et al., 2025) | Adaptive rollout allocation | Math/coding | +4% pass@1, +6% cons@32 |

## Research Trends and Future Directions

### Emerging Patterns

1. **Domain Expansion**: GRPO is being successfully adapted beyond text generation to representation learning, diffusion models, and flow models, demonstrating algorithmic flexibility.

2. **Temporal Dimension**: Multiple works (MGRPO, MURPHY) address multi-turn interactions, recognizing that real-world applications often involve iterative refinement rather than single-shot generation.

3. **Credit Granularity**: Enhancements like GRPO-λ and XRPO focus on finer-grained credit assignment, acknowledging that token-level or step-level attribution improves learning efficiency.

4. **Efficiency Focus**: Scaling laws research indicates growing maturity of the field, with attention shifting from raw performance to computational optimization.

5. **Fundamental Understanding**: Works examining distributional boundaries reflect maturing theoretical understanding of GRPO's capabilities and limitations.

### Open Challenges

1. **Beyond Pretraining Bias**: As noted by Ni et al. (2025), expanding capabilities beyond pretrained distribution remains unsolved.

2. **Reward Hacking**: While f-HAL mitigates this issue, reward hacking in learned reward models continues to be a concern.

3. **Scalability**: Despite efficiency improvements, GRPO training remains computationally expensive for very large models.

4. **Generalization**: Maintaining performance across diverse domains and prompt distributions requires continued innovation.

## Conclusion

The ten papers reviewed represent significant advances in GRPO methodology for generation models. Key themes include extending GRPO to new model architectures (representation models, flow models), enabling multi-turn reasoning through self-correction mechanisms, improving credit assignment granularity, optimizing training efficiency, and understanding fundamental distributional limitations. Collectively, these advances position GRPO as a versatile and powerful framework for reinforcement learning with verifiable rewards, though challenges remain in pushing beyond pretraining biases and further improving computational efficiency. Future research directions should focus on developing algorithms capable of genuine capability expansion, robust reward model integration, and scalable deployment for next-generation foundation models.

---

## References

Bamba, U., Fang, M., Yu, Y., Zheng, H., & Lai, F. (2025). XRPO: Pushing the limits of GRPO with targeted exploration and exploitation. *arXiv preprint arXiv:2510.06672*. https://arxiv.org/abs/2510.06672v3

Ding, F., Wang, B., Zeng, Z., & Wang, Y. (2025). Multi-Layer GRPO: Enhancing reasoning and self-correction in large language models. *arXiv preprint arXiv:2506.04746*. https://arxiv.org/abs/2506.04746v1

Ekbote, C., Lingam, V., Sanghavi, S., Huan, J., Omidvar-Tehrani, B., Deoras, A., & Soatto, S. (2025). MURPHY: Feedback-aware GRPO with retrospective credit assignment for multi-turn code generation. *arXiv preprint arXiv:2511.07833*. https://arxiv.org/abs/2511.07833v3

Haldar, R., Mei, L., Lin, G., Xing, Y., & Song, Q. (2026). f-GRPO and beyond: Divergence-based reinforcement learning algorithms for general LLM alignment. *arXiv preprint arXiv:2602.05946*. https://arxiv.org/abs/2602.05946v3

Le, K., Nguyen, P., Mroueh, Y., Lin, C.-H., Gao, S., Hua, T., & Chawla, N. V. (2026). Transformation-Augmented GRPO for enhancing exploration in reasoning of large language models. *arXiv preprint arXiv:2601.22478*. https://arxiv.org/abs/2601.22478v5

Ni, K., Tan, Z., Liu, Z., Li, P., & Chen, T. (2025). Can GRPO help LLMs transcend their pretraining origin? *arXiv preprint arXiv:2510.15990*. https://arxiv.org/abs/2510.15990v1

Nimmaturi, D., Bhargava, V., Ghosh, R., George, J., & Dutta, D. (2025). Predictive scaling laws for efficient GRPO training of large reasoning models. *arXiv preprint arXiv:2507.18014*. https://arxiv.org/abs/2507.18014v3

Parthasarathi, P., Reymond, M., Chen, B., Cui, Y., & Chandar, S. (2025). GRPO-$\lambda$: Credit assignment improves LLM reasoning. *arXiv preprint arXiv:2510.00194*. https://arxiv.org/abs/2510.00194v1

Xu, Y., Jiao, Z., Zhang, H., & Li, X. (2025). GRPO-RM: Fine-tuning representation models via GRPO-driven reinforcement learning. *arXiv preprint arXiv:2511.15256*. https://arxiv.org/abs/2511.15256v1

Zhou, Y., Ling, P., Bu, J., Wang, Y., Zang, Y., Wang, J., Niu, L., & Zhai, G. (2025). Fine-Grained GRPO for precise preference alignment in flow models. *arXiv preprint arXiv:2510.01982*. https://arxiv.org/abs/2510.01982v3
