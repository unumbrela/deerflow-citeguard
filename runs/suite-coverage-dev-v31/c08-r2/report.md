# Systematic Literature Review: Advances in GRPO for Generation Models

## Executive Summary

This systematic literature review examines recent advances in Group Relative Policy Optimization (GRPO) applied to generation models between February 21, 2024, and February 20, 2026. The review synthesizes findings from 10 peer-reviewed papers published primarily in computer vision (cs.CV), machine learning (cs.LG), and artificial intelligence (cs.AI) domains. Key themes include stabilization of training processes, improved reward modeling, temporal optimization in flow models, identity preservation in video generation, and generalization across multimodal tasks.

---

## 1. Introduction

Group Relative Policy Optimization (GRPO) has emerged as a powerful reinforcement learning framework for aligning generative models with human preferences. Recent developments have extended GRPO beyond traditional language models into image generation, video synthesis, code generation, and representation learning. This review systematically analyzes 10 scholarly works that advance GRPO methodologies and their applications to diverse generation tasks.

The selected papers span critical subdomains including text-to-image generation [citation:Pref-GRPO](https://arxiv.org/abs/2508.20751v2), multimodal reasoning [citation:GRPO-CARE](https://arxiv.org/abs/2506.16141v1), video generation [citation:Identity-GRPO](https://arxiv.org/abs/2510.14256v3), flow matching models [citation:Neighbor GRPO](https://arxiv.org/abs/2511.16955v2), and code generation [citation:Code Quality GRPO](https://arxiv.org/abs/2506.02211v1).

---

## 2. Methodological Advances in GRPO

### 2.1 Preference-Based Reward Modeling

**Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning** (Wang et al., 2025) addresses the critical issue of reward hacking in text-to-image generation. The authors demonstrate that pointwise reward models amplify minimal score differences after normalization, creating illusory advantages that destabilize training. Their proposed Pref-GRPO shifts optimization from score maximization to preference fitting by pairwise comparing images within each group using preference reward models. Extensive experiments show Pref-GRPO differentiates subtle quality differences more effectively than standard approaches. Additionally, the authors introduce UniGenBench, a unified benchmark with 600 prompts across five main themes and 20 subthemes, leveraging MLLMs for comprehensive evaluation [citation:Pref-GRPO](https://arxiv.org/abs/2508.20751v2).

**Delving into RL for Image Generation with CoT: A Study on DPO vs. GRPO** (Tong et al., 2025) provides the first comprehensive investigation comparing Direct Preference Optimization (DPO) and GRPO in autoregressive image generation. The study reveals distinct advantages of each algorithm and demonstrates that reward models with stronger intrinsic generalization enhance RL performance. The authors explore three scaling strategies and derive insights for efficiently improving both in-domain and out-of-domain proficiency, paving new paths for robust Chain-of-Thought reasoning in image generation [citation:DPO vs GRPO](https://arxiv.org/abs/2505.17017v2).

### 2.2 Consistency-Aware Frameworks

**GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning** (Chen et al., 2025) introduces a novel two-tiered reward mechanism optimizing both answer correctness and reasoning coherence without explicit supervision. The method computes an adaptive consistency bonus by comparing the model's reasoning-to-answer likelihood against group peers. Using their newly introduced SEED-Bench-R1 benchmark with complex real-world videos, the authors demonstrate GRPO-CARE achieves a 6.7% performance gain on the hardest evaluation level and a 24.5% improvement in consistency over standard GRPO. This work contributes both a systematically designed benchmark and a generalizable post-training framework for interpretable multimodal LLMs [citation:GRPO-CARE](https://arxiv.org/abs/2506.16141v1).

### 2.3 Temporal Optimization in Flow Models

**TempFlow-GRPO: When Timing Matters for GRPO in Flow Models** (He et al., 2025) identifies temporal uniformity assumptions as the key impediment to effective GRPO training in flow models. The authors propose three innovations: (i) trajectory branching mechanisms providing process rewards through designated branching points; (ii) noise-aware weighting schemes modulating policy optimization according to timestep exploration potential; and (iii) seed group strategies controlling for initialization effects. These innovations enable temporally-aware optimization respecting underlying generative dynamics, leading to state-of-the-art performance in human preference alignment and text-to-image benchmarks [citation:TempFlow-GRPO](https://arxiv.org/abs/2508.04324v4).

**GRPO-Guard: Mitigating Implicit Over-Optimization in Flow Matching via Regulated Clipping** (Wang et al., 2025) addresses systematic shifts in importance-ratio distributions observed in practice. The mean falling below 1 and variance differing substantially across timesteps prevents positive-advantage samples from entering the clipped region, causing implicit over-optimization where proxy rewards increase while essential metrics deteriorate. The proposed solution incorporates ratio normalization restoring balanced step-consistent importance ratios and gradient reweighting equalizing policy gradients over noise conditions. Experiments on multiple diffusion backbones (SD3.5M, Flux.1-dev) demonstrate significant reduction in over-optimization while maintaining or improving generation quality [citation:GRPO-Guard](https://arxiv.org/abs/2510.22319v2).

**Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models** (He et al., 2025) reinterprets existing SDE-based GRPO methods from a distance optimization perspective, revealing their underlying mechanism as contrastive learning. The proposed Neighbor GRPO generates diverse candidate trajectories by perturbing initial noise conditions of ODEs and optimizes using softmax distance-based surrogate leaping policies. Theoretical connections establish rigorous integration into the GRPO framework while preserving deterministic ODE sampling advantages including efficiency and high-order solver compatibility. Additional innovations include symmetric anchor sampling for computational efficiency and group-wise quasi-norm reweighting to address reward flattening. Results demonstrate significant outperformance over SDE-based counterparts in training cost, convergence speed, and generation quality [citation:Neighbor GRPO](https://arxiv.org/abs/2511.16955v2).

### 2.4 Stability and Generalization

**STAGE: Stable and Generalizable GRPO for Autoregressive Image Generation** (Ma et al., 2025) identifies contradictory gradients from unnecessary tokens and unstable policy entropy dynamics as key challenges applying GRPO to autoregressive image models. The framework leverages two targeted solutions: (1) Advantage/KL reweighting with similarity-aware reweighting to alleviate conflicting updates, and (2) entropy rewards corresponding to reference models to stabilize learning. By addressing token conflicts and stabilizing training through entropy rewards, STAGE reduces disruption of pretrained distributions and mitigates reward hacking, improving generalization and cross-task transferability compared to baseline GRPO [citation:STAGE](https://arxiv.org/abs/2509.25027v1).

---

## 3. Domain-Specific Applications

### 3.1 Video Generation and Identity Preservation

**Identity-GRPO: Optimizing Multi-Human Identity-preserving Video Generation via Reinforcement Learning** (Meng et al., 2025) addresses multi-human identity preservation challenges in dynamic interactions where consistent identities across multiple characters are critical. The authors construct a video reward model trained on large-scale preference datasets containing human-annotated and synthetic distortion data with pairwise annotations focused on human consistency throughout videos. Employing a GRPO variant tailored for multi-human consistency greatly enhances baseline methods VACE and Phantom. Ablation studies evaluate annotation quality and design choices' impact on policy optimization. Experiments show up to 18.9% improvement in human consistency metrics over baseline methods, offering actionable insights for aligning reinforcement learning with personalized video generation [citation:Identity-GRPO](https://arxiv.org/abs/2510.14256v3).

### 3.2 Representation Learning

**GRPO-RM: Fine-Tuning Representation Models via GRPO-Driven Reinforcement Learning** (Xu et al., 2025) investigates whether GRPO can be generalized beyond LLM fine-tuning to representation learning models. The proposed GRPO-RM establishes predefined output sets to functionally replace token sequence sampling in LLMs, thereby generating output groups essential for probability-driven GRPO optimization. A specialized reward function accommodates representation model properties. Extensive experiments on various real-world datasets validate the effectiveness of this generalization, demonstrating GRPO's applicability beyond sequential generation tasks [citation:GRPO-RM](https://arxiv.org/abs/2511.15256v1).

### 3.3 Code Generation

**Improving LLM-Generated Code Quality with GRPO** (Robeyns & Aitchison, 2025) addresses limitations of execution feedback as a reward signal focusing solely on functional correctness via unit test pass rates. The authors develop a comprehensive library quantifying various aspects of code quality including maintainability, quality, and safety, using these metrics as rewards in GRPO. Findings demonstrate GRPO increases code quality according to this measure, confirmed by expert blinded human annotators. This work expands GRPO applications beyond natural language generation to structured code production with nuanced quality dimensions [citation:Code Quality GRPO](https://arxiv.org/abs/2506.02211v1).

---

## 4. Comparative Analysis

### 4.1 Algorithmic Innovations

The reviewed literature reveals several distinct innovation categories:

| Innovation Type | Papers | Primary Focus |
|----------------|--------|---------------|
| Reward Model Reformulation | Pref-GRPO, GRPO-CARE | Preference-based and consistency-aware rewards |
| Temporal/Credit Assignment | TempFlow-GRPO, Neighbor GRPO | Timestep-aware optimization |
| Stabilization Techniques | GRPO-Guard, STAGE | Preventing over-optimization and entropy control |
| Domain Adaptation | Identity-GRPO, GRPO-RM, Code Quality | Specialized reward functions for specific domains |

### 4.2 Performance Metrics

Key quantitative improvements reported across studies include:
- **Consistency improvements**: GRPO-CARE achieves 24.5% consistency gain [citation:GRPO-CARE](https://arxiv.org/abs/2506.16141v1)
- **Human consistency**: Identity-GRPO shows 18.9% improvement [citation:Identity-GRPO](https://arxiv.org/abs/2510.14256v3)
- **Training efficiency**: Neighbor GRPO demonstrates reduced training costs [citation:Neighbor GRPO](https://arxiv.org/abs/2511.16955v2)
- **Quality validation**: Multiple studies report improved generation quality metrics [citation:Pref-GRPO](https://arxiv.org/abs/2508.20751v2), [citation:TempFlow-GRPO](https://arxiv.org/abs/2508.04324v4), [citation:GRPO-Guard](https://arxiv.org/abs/2510.22319v2)

### 4.3 Benchmark Developments

Two major benchmark contributions emerge:
1. **UniGenBench** (Pref-GRPO): 600 prompts across 5 themes and 20 subthemes evaluating semantic consistency through 10 primary and 27 sub-criteria using MLLMs [citation:Pref-GRPO](https://arxiv.org/abs/2508.20751v2)
2. **SEED-Bench-R1** (GRPO-CARE): Complex real-world videos requiring balanced perception and reasoning with in-distribution, cross-environment, and cross-environment-task scenarios [citation:GRPO-CARE](https://arxiv.org/abs/2506.16141v1)

---

## 5. Critical Discussion

### 5.1 Common Challenges Addressed

Across all reviewed works, several recurring challenges emerge:

**Reward Hacking**: Multiple studies (Pref-GRPO, STAGE, GRPO-Guard) identify reward hacking as a fundamental limitation where models exploit reward function loopholes rather than genuinely improving generation quality. Solutions range from pairwise preference modeling to entropy regularization and regulated clipping mechanisms.

**Credit Assignment**: TempFlow-GRPO and Neighbor GRPO highlight difficulties in assigning appropriate credit across generation timesteps or trajectories, particularly in flow matching models where deterministic sampling complicates exploration.

**Generalization**: Studies consistently note poor out-of-domain generalization as a persistent issue. Tong et al. (2025) demonstrate that reward model generalization capabilities directly influence RL algorithm generalization potential [citation:DPO vs GRPO](https://arxiv.org/abs/2505.17017v2).

### 5.2 Limitations and Open Questions

Several limitations persist across the literature:

1. **Computational Costs**: While some methods claim efficiency improvements (e.g., Neighbor GRPO bypassing SDEs), comprehensive cost analyses remain limited
2. **Benchmark Diversity**: Most evaluations focus on text-to-image or video generation, with fewer studies addressing other modalities
3. **Long-term Stability**: Few studies examine whether improvements sustain over extended training periods
4. **Theoretical Foundations**: While practical results are promising, theoretical guarantees remain underdeveloped compared to traditional PPO formulations

### 5.3 Cross-Domain Applicability

The expansion from language models to diverse domains (images, videos, code, representations) demonstrates GRPO's versatility but raises questions about universal applicability versus domain-specific adaptations. GRPO-RM's success in representation learning suggests broader potential, yet each application requires careful reward function design and adaptation [citation:GRPO-RM](https://arxiv.org/abs/2511.15256v1).

---

## 6. Future Research Directions

Based on identified gaps and emerging trends, several research directions warrant investigation:

### 6.1 Enhanced Reward Modeling
Development of more sophisticated reward models combining multiple signals (preference, consistency, quality metrics) while avoiding reward hacking through principled regularization.

### 6.2 Unified Benchmarks
Creation of comprehensive benchmarks spanning multiple modalities and task types to enable fair comparison and assess true generalization capabilities.

### 6.3 Efficiency Improvements
Investigation of methods reducing computational overhead while maintaining performance gains, particularly important for resource-constrained deployment scenarios.

### 6.4 Theoretical Analysis
Rigorous theoretical foundations establishing convergence guarantees and stability bounds analogous to those developed for traditional policy gradient methods.

### 6.5 Multi-Agent and Collaborative Settings
Exploration of GRPO in multi-agent generative systems where agents collaboratively produce content or compete through adversarial dynamics.

---

## 7. Conclusion

This systematic literature review documents significant advances in GRPO applications to generation models between 2024 and 2026. Ten representative papers reveal substantial progress in addressing fundamental challenges including reward hacking, temporal credit assignment, training stability, and cross-domain generalization. Key innovations span pairwise preference modeling, consistency-aware frameworks, temporal optimization mechanisms, and stabilized training procedures.

The field demonstrates clear maturation from proof-of-concept demonstrations toward practical deployments with measurable improvements in generation quality, consistency, and efficiency. However, open challenges remain regarding theoretical foundations, benchmark standardization, and computational scalability. Future research should prioritize unified evaluation frameworks, enhanced theoretical analysis, and efficient implementations suitable for production environments.

The diversity of successful applications—from image and video generation to code quality and representation learning—demonstrates GRPO's adaptability as a reinforcement learning paradigm. As the field progresses, continued attention to reward modeling sophistication, stability mechanisms, and comprehensive evaluation will be essential for realizing GRPO's full potential in generative AI systems.

---

## References

Chen, Y., Ge, Y., Wang, R., Ge, Y., Cheng, J., Shan, Y., & Liu, X. (2025). GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning. *arXiv preprint arXiv:2506.16141*. https://arxiv.org/abs/2506.16141v1

He, D., Feng, G., Ge, X., Niu, Y., Zhang, Y., Ma, B., Song, G., Liu, Y., & Li, H. (2025). Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models. *arXiv preprint arXiv:2511.16955*. https://arxiv.org/abs/2511.16955v2

He, X., Fu, S., Zhao, Y., Li, W., Yang, J., Yin, D., Rao, F., & Zhang, B. (2025). TempFlow-GRPO: When Timing Matters for GRPO in Flow Models. *arXiv preprint arXiv:2508.04324*. https://arxiv.org/abs/2508.04324v4

Ma, X., Qiu, H., Zhang, G., Zeng, Z., Yang, S., Ma, L., & Zhao, F. (2025). STAGE: Stable and Generalizable GRPO for Autoregressive Image Generation. *arXiv preprint arXiv:2509.25027*. https://arxiv.org/abs/2509.25027v1

Meng, X., Zhang, Z., Zhang, Z., Liao, J., Qin, L., & Wang, W. (2025). Identity-GRPO: Optimizing Multi-Human Identity-preserving Video Generation via Reinforcement Learning. *arXiv preprint arXiv:2510.14256*. https://arxiv.org/abs/2510.14256v3

Robeyns, M., & Aitchison, L. (2025). Improving LLM-Generated Code Quality with GRPO. *arXiv preprint arXiv:2506.02211*. https://arxiv.org/abs/2506.02211v1

Tong, C., Guo, Z., Zhang, R., Shan, W., Wei, X., Xing, Z., Li, H., & Heng, P.-A. (2025). Delving into RL for Image Generation with CoT: A Study on DPO vs. GRPO. *arXiv preprint arXiv:2505.17017*. https://arxiv.org/abs/2505.17017v2

Wang, J., Liang, J., Liu, J., Liu, H., Liu, G., Zheng, J., Pang, W., Ma, A., Xie, Z., Wang, X., Wang, M., Wan, P., & Liang, X. (2025). GRPO-Guard: Mitigating Implicit Over-Optimization in Flow Matching via Regulated Clipping. *arXiv preprint arXiv:2510.22319*. https://arxiv.org/abs/2510.22319v2

Wang, Y., Li, Z., Zang, Y., Zhou, Y., Bu, J., Wang, C., Lu, Q., Jin, C., & Wang, J. (2025). Pref-GRPO: Pairwise Preference Reward-based GRPO for Stable Text-to-Image Reinforcement Learning. *arXiv preprint arXiv:2508.20751*. https://arxiv.org/abs/2508.20751v2

Xu, Y., Jiao, Z., Zhang, H., & Li, X. (2025). GRPO-RM: Fine-Tuning Representation Models via GRPO-Driven Reinforcement Learning. *arXiv preprint arXiv:2511.15256*. https://arxiv.org/abs/2511.15256v1

---

*Systematic Literature Review completed on October 26, 2026*  
*Search parameters: 10 papers, cs.LG category, published 2024-02-21 to 2026-02-20*
