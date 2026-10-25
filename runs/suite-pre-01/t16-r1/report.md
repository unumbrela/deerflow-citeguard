# Systematic Literature Review: Reinforcement Learning from Human Feedback

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "RLHF", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on Reinforcement Learning from Human Feedback (RLHF) from the past two years reveals a field maturing along multiple dimensions: efficiency and scalability, theoretical foundations, fairness and bias mitigation, and security. The surveyed papers collectively demonstrate that RLHF has become a critical post-training technique for large language models and multimodal systems, yet significant challenges remain in scaling efficiently, capturing diverse human preferences, and ensuring robustness against adversarial manipulation. Research has shifted from establishing RLHF's basic effectiveness to optimizing its computational demands, understanding its theoretical underpinnings, and addressing limitations in bias mitigation and fairness. The field shows growing recognition that uniform reward models fail to capture preference diversity, and that alternative approaches like direct preference optimization (DPO) and negative supervised fine-tuning (nSFT) can match or exceed traditional RLHF in specific contexts.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "RLHF", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search query "RLHF" may miss papers using only the full term "reinforcement learning from human feedback" without the acronym.

## Themes

### Theme 1: Efficiency and Scalability

A dominant thread across the surveyed literature addresses the computational and infrastructural challenges of scaling RLHF to large models and production workloads. Hou et al. (2024) provide a foundational scaling analysis, systematically examining how model size, data composition, and inference budget affect RLHF performance. Their findings reveal that RLHF scales less efficiently than pretraining, with diminishing returns from additional computational resources — larger policy models benefit less from RLHF with a fixed reward model, and more response samples per prompt boost performance only initially before plateauing. This sobering analysis motivates subsequent work on algorithmic and infrastructural optimizations.

Building on the scaling challenge, Yang et al. (2025) propose GRPOVI, a method that accelerates group relative policy optimization (GRPO) training by provably increasing reward variance while preserving relative preferences. Their O(n log n) algorithm solves a nonconvex optimization problem that is NP-hard in general, achieving significant training efficiency improvements. The work also provides an indirect explanation for the empirical success of GRPO with rule-based rewards in DeepSeek-R1.

At the infrastructure level, Wu et al. (2025) introduce G-Core, a scalable RLHF training framework featuring parallel controller programming and dynamic resource placement. G-Core eliminates bottlenecks from centralized controllers and adaptively partitions resources to reduce hardware idle time, successfully training models supporting WeChat product features at scale. Similarly, Wei et al. (2026) present RLHFless, the first serverless computing framework for synchronous RLHF training. By adapting to dynamic resource demands, pre-computing shared prefixes, and using cost-aware actor scaling, RLHFless achieves 1.35x speedup and 44.8% cost reduction compared to serverful baselines.

Collectively, these papers establish that efficient RLHF requires co-design across algorithmic, architectural, and infrastructural dimensions — no single optimization suffices for production-scale deployment.

### Theme 2: Theoretical Foundations and Alternative Approaches

Parallel to efficiency work, researchers have sought to clarify RLHF's theoretical foundations and explore alternative alignment paradigms. Xiao et al. (2025) establish a theoretical connection between RLHF and imitation learning, revealing that RLHF implicitly performs imitation learning on the preference data distribution. Their DIL framework directly optimizes the imitation learning objective, providing a unified perspective that encompasses existing alignment algorithms as special cases while naturally introducing new variants. DIL outperforms existing methods on various benchmarks, suggesting that the imitation learning lens offers practical advantages.

Shi et al. (2025) provide a fine-grained theoretical analysis comparing two-stage RLHF with direct preference optimization (DPO), decomposing the performance gap into explicit and implicit representation gaps. Their analysis reveals that RLHF, DPO, or online DPO can each outperform the others depending on model mis-specification types. Notably, online DPO outperforms both RLHF and standard DPO when reward and policy model classes are isomorphic and both mis-specified. In sparse reward settings, RLHF requires significantly fewer samples than DPO to recover an effective reward model, highlighting a statistical advantage of two-stage learning.

Challenging the necessity of RLHF altogether, Zhu et al. (2024) demonstrate that continual supervised fine-tuning with negative supervision (nSFT) can match multimodal RLHF performance for vision-language models. Their approach extracts the negative supervision signal — the logit of rejected responses — from the RLHF paradigm and applies it through a simple SFT loss. nSFT achieves comparable performance while being more memory efficient, avoiding the requirement for 2-4 large vision-language models simultaneously. This work suggests that RLHF's value may lie primarily in its negative supervision signal rather than its reinforcement learning machinery.

### Theme 3: Fairness, Bias, and Diverse Preferences

A critical limitation of standard RLHF is its treatment of human preferences as homogeneous, inadvertently favoring dominant groups. Mukherjee et al. (2025) address this by introducing SharedRep-RLHF, which learns shared traits in annotations across groups rather than separate reward models per group. They show that the state-of-the-art MaxMin-RLHF is provably suboptimal in learning shared traits and performs poorly when the minimum-reward group is a minority. SharedRep-RLHF achieves up to 20% win rate improvement across diverse natural language tasks, demonstrating that capturing preference diversity requires architectural innovations beyond uniform reward models.

Barnhart et al. (2025) investigate RLHF's effectiveness in mitigating covert and overt biases against African Americans in LLMs. Their experiments applying DPO, ORPO, and RLOO to Llama 3 8B reveal a troubling finding: supervised fine-tuning before RLHF calcifies model biases rather than reducing them. Current alignment techniques prove inadequate for nebulous tasks like mitigating covert biases, highlighting the need for more capable datasets, data curation techniques, and alignment tools. The study extends bias measurement to multimodal models, establishing methodological foundations for future work.

Together, these papers suggest that RLHF's alignment capabilities are fundamentally constrained by dataset quality and reward model expressivity — addressing bias requires interventions at the data curation stage, not just the alignment algorithm stage.

### Theme 4: Security and Trustworthiness

As RLHF platforms become widely adopted for model fine-tuning, their security and trustworthiness remain largely unexplored. Entezami and Naseh (2025) present the first investigation of adversarial attacks on RLHF platforms, demonstrating that an adversarial platform can corrupt the alignment process by selectively manipulating preference dataset samples. When a user's task aligns with the attacker's objective, the platform manipulates related preference samples, corrupting the reward model and ultimately steering the language model toward undesirable behaviors in targeted domains. This attack highlights critical vulnerabilities in publicly available RLHF frameworks and underscores the need for security analysis of alignment infrastructure.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that RLHF exhibits diminishing returns from scaling computational resources (Hou et al., 2024; Yang et al., 2025). There is broad agreement that uniform reward models fail to capture preference diversity (Mukherjee et al., 2025; Barnhart et al., 2025), and that efficiency improvements require co-design across algorithmic and infrastructural dimensions (Wu et al., 2025; Wei et al., 2026). Several papers independently observe that RLHF's value may be extractable through simpler mechanisms — negative supervision (Zhu et al., 2024) or imitation learning objectives (Xiao et al., 2025).

**Disagreements**: The literature shows nuanced disagreements about when RLHF is preferable to alternatives. Shi et al. (2025) demonstrate that RLHF requires fewer samples than DPO in sparse reward settings, while Zhu et al. (2024) show nSFT can match RLHF for multimodal alignment — these findings are not contradictory but highlight context-dependence. Similarly, while Hou et al. (2024) find that larger policy models benefit less from RLHF, Yang et al. (2025) and Wu et al. (2025) demonstrate that algorithmic and infrastructural innovations can restore scaling efficiency.

## Gaps and Open Questions

The surveyed literature reveals several consistent gaps:

1. **Defense mechanisms for RLHF security**: Entezami and Naseh (2025) identify vulnerabilities in RLHF platforms but do not propose defenses. As RLHF becomes production infrastructure, adversarial robustness requires urgent attention.

2. **Bias mitigation beyond data curation**: Barnhart et al. (2025) find that SFT before RLHF calcifies biases, yet offer no algorithmic solution. The field lacks methods for actively debiasing models during alignment rather than relying on dataset curation alone.

3. **Cross-paper comparability**: Efficiency papers report speedups and cost reductions on different benchmarks and infrastructures (Wu et al., 2025; Wei et al., 2026; Yang et al., 2025), making direct comparison difficult. Standardized evaluation protocols are needed.

4. **Theoretical-practical gap**: Theoretical analyses (Shi et al., 2025; Xiao et al., 2025) provide elegant characterizations of when methods excel, but empirical validation is limited to specific constructions. Bridging theory and practice remains challenging.

5. **Generalization beyond tested scenarios**: Multiple papers acknowledge limitations in generalizability — findings from WeChat deployment (Wu et al., 2025), specific model architectures (Barnhart et al., 2025), or simulated clusters (Wei et al., 2026) may not transfer to other contexts.

## Per-Paper Annotations

### Barnhart et al. (2025)

**Research question**: How effective is RLHF in addressing underlying biases, particularly covert and overt biases against African Americans, in large language models?
**Methodology**: Applied various RLHF techniques (DPO, ORPO, and RLOO) to Llama 3 8B and evaluated resulting models using matched-guise probing and explicit bias testing, with additional experiments across different base models and datasets, extending bias measurement tools to multi-modal models.
**Key findings**:
- Supervised fine-tuning (SFT) before RLHF calcifies model biases rather than reducing them
- Current alignment techniques are inadequate for mitigating covert biases
- Different RLHF methods (DPO, ORPO, RLOO) show varying effectiveness on bias reduction
- There is a need for more capable datasets, data curating techniques, and alignment tools
- Bias measurement tools were successfully extended to multi-modal models
**Limitations**: Research focuses primarily on biases against African Americans, so results may not generalize to other bias types or demographic groups; findings are specific to the tested models and may vary with different architectures.

### Entezami and Naseh (2025)

**Research question**: Can adversarial RLHF platforms manipulate the alignment process to cause LLM misalignment in targeted domains?
**Methodology**: The authors propose an attack where an adversarial RLHF platform selectively manipulates data samples in the preference dataset, corrupting the reward model and ultimately steering the language model toward undesirable behaviors.
**Key findings**:
- RLHF platforms' security and reliability remain largely unexplored despite growing adoption
- An adversarial platform can effectively manipulate subsets of preference datasets related to attacker targets
- Such manipulation corrupts the reward model during the alignment process
- The attack successfully steers LLMs toward undesirable behaviors within targeted domains
- Critical vulnerabilities exist in RLHF platforms that can cause misalignment during fine-tuning
**Limitations**: The paper focuses on a specific attack scenario without extensively discussing defense mechanisms or real-world deployment constraints of such attacks.

### Hou et al. (2024)

**Research question**: What are the scaling properties of RLHF in large language models across model size, data composition, and inference budget, and how does RLHF scaling compare to pretraining?
**Methodology**: Systematically analyzes key RLHF components including model size, data diversity and volume, and inference budget to measure their impacts on both reward model performance and policy training outcomes.
**Key findings**:
- Increasing data diversity and volume improves reward model performance and helps process-supervision models scale better
- More response samples per prompt boost policy performance initially but quickly plateau
- Larger reward models provide only modest gains in policy training
- Larger policy models benefit less from RLHF when using a fixed reward model
- RLHF scales less efficiently than pretraining with diminishing returns from additional computational resources
**Limitations**: Study is limited to specific model architectures and datasets; computational constraints may have prevented exploration of extreme scaling regimes that could reveal different patterns.

### Mukherjee et al. (2025)

**Research question**: How can RLHF better capture diverse preferences across sub-populations rather than inadvertently favoring dominant groups?
**Methodology**: The authors introduce SharedRep-RLHF, which learns and leverages shared traits in annotations among various groups rather than learning separate reward models across groups, contrasting with the state-of-the-art MaxMin-RLHF approach.
**Key findings**:
- Uniform-reward RLHF fails to capture diversity of opinions across sub-populations, favoring dominant groups
- MaxMin-RLHF has poor performance when the minimum-reward group is a minority
- SharedRep-RLHF learns shared traits among groups instead of separate reward models
- MaxMin-RLHF is provably suboptimal in learning shared traits
- SharedRep-RLHF achieves up to 20% gain in win rate compared to MaxMin-RLHF across diverse natural language tasks
**Limitations**: The approach assumes identifiable group structures and shared traits among groups; sample complexity analysis is provided but real-world deployment challenges with diverse, overlapping sub-populations are not fully addressed.

### Shi et al. (2025)

**Research question**: What causes the performance gap between two-stage reinforcement learning from human feedback (RLHF) and direct preference optimization (DPO), and under what conditions does each method excel?
**Methodology**: Conducts fine-grained theoretical analysis decomposing the performance gap into explicit representation gap under exact optimization and implicit representation gap under finite samples, with concrete constructions for sparse reward settings to compare sample efficiency.
**Key findings**:
- Performance gap depends on relative capacities of reward and policy model classes
- RLHF, DPO, or online DPO can outperform one another depending on the type of model mis-specifications
- Online DPO outperforms both RLHF and standard DPO when reward and policy model classes are isomorphic and both mis-specified
- RLHF requires significantly fewer samples than DPO to recover effective reward models when ground-truth rewards are sparse
- Two-stage learning provides statistical advantages in certain reward sparsity settings
**Limitations**: Theoretical analysis may not capture all practical considerations encountered in real-world deployments; empirical validation is limited to specific constructions that may not represent the full range of practical scenarios.

### Wei et al. (2026)

**Research question**: How can serverless computing improve the efficiency and cost-effectiveness of synchronous RLHF training given dynamic resource demands?
**Methodology**: The authors present RLHFless, the first scalable training framework for synchronous RLHF built on serverless computing, featuring dynamic resource adaptation, shared prefix pre-computation, and cost-aware actor scaling that accounts for response length variation.
**Key findings**:
- Serverful infrastructures struggle with fine-grained resource variability in RLHF workflows
- RLHFless achieves up to 1.35x speedup compared to state-of-the-art baselines
- RLHFless achieves 44.8% cost reduction compared to state-of-the-art baselines
- The framework reduces intra-function imbalance and idle time through efficient workload assignment
- Cost-aware actor scaling finds optimal trade-offs between cost and speed accounting for response length variation
**Limitations**: Evaluation conducted on specific physical testbeds and simulated clusters may not generalize to all RLHF scenarios; serverless computing introduces its own overhead and cold-start challenges in some cases.

### Wu et al. (2025)

**Research question**: How can RLHF training systems overcome scalability, flexibility, and efficiency challenges when handling multi-modal workflows, diffusion models, and dynamic workloads?
**Methodology**: Proposes G-Core, a new RLHF training framework featuring a parallel controller programming model to eliminate centralized bottlenecks and a dynamic placement schema that adaptively partitions resources and schedules workloads.
**Key findings**:
- Parallel controller architecture eliminates bottlenecks inherent in single centralized controller designs
- Dynamic placement schema significantly reduces hardware idle time and improves utilization under variable training conditions
- Successfully trained models supporting WeChat product features serving large-scale user bases
- Framework handles complex RLHF pipelines including dynamic sampling and generative reward modeling
- Demonstrates robustness and effectiveness in real-world production scenarios
**Limitations**: Focus is primarily on system architecture and infrastructure rather than algorithmic improvements; real-world validation is limited to Tencent/WeChat deployment scenarios which may not generalize to other organizations.

### Xiao et al. (2025)

**Research question**: What is the theoretical relationship between RLHF and imitation learning, and can this connection yield better alignment algorithms?
**Methodology**: The authors establish a theoretical connection showing RLHF implicitly performs imitation learning on the preference data distribution, then propose DIL, a principled framework that directly optimizes the imitation learning objective.
**Key findings**:
- RLHF implicitly performs imitation learning on the preference data distribution
- DIL provides a unified imitation learning perspective on alignment
- DIL encompasses existing alignment algorithms as special cases
- The framework naturally introduces new alignment variants
- DIL outperforms existing methods on various challenging benchmarks
**Limitations**: The theoretical framework may not capture all practical nuances of real-world alignment scenarios; experimental validation is limited to specific benchmarks and may not generalize to all alignment tasks.

### Yang et al. (2025)

**Research question**: How can GRPO-based RLHF training be accelerated while maintaining alignment quality?
**Methodology**: The authors propose a reward adjustment model that provably increases reward variance while preserving relative preferences and reward expectation, with a novel O(n log n) algorithm to solve the resulting nonconvex optimization problem, integrated into GRPO as GRPOVI.
**Key findings**:
- Higher reward variance of the initial policy model leads to faster RLHF training
- The reward adjustment method solves a nonconvex optimization problem by characterizing extreme points of the feasible set
- GRPOVI (GRPO with Reward Variance Increase) significantly improves training efficiency compared to original GRPO
- The method provides an indirect explanation for the empirical effectiveness of GRPO with rule-based reward as demonstrated in DeepSeek-R1
- The O(n log n) algorithm finds a global solution to an otherwise NP-hard problem
**Limitations**: The reward adjustment model inherently poses a nonconvex optimization problem that is NP-hard to solve in general, requiring specialized algorithm design to overcome computational challenges.

### Zhu et al. (2024)

**Research question**: Can continual supervised fine-tuning with negative supervision match or exceed multimodal RLHF performance for vision-language model alignment?
**Methodology**: Proposes negative supervised finetuning (nSFT) that extracts the negative supervision signal from rejected response logits in the RLHF paradigm, then rigorously compares nSFT against various multimodal RLHF approaches across different dataset sources, base VLMs, and evaluation metrics with extensive ablations.
**Key findings**:
- nSFT achieves comparable performance to multimodal RLHF across various benchmarks
- nSFT is more memory efficient than RLHF, avoiding the requirement for 2-4 large VLMs simultaneously
- The inherent value of multimodal RLHF lies primarily in its negative supervision signal
- Approach works consistently across different dataset sources and base vision-language models
- Extensive ablation studies provide strong support for the negative supervision hypothesis
**Limitations**: Focus is on vision-language models and may not generalize to text-only scenarios; the effectiveness of negative supervision extraction may depend heavily on the quality and consistency of rejection labels in the training data.

## References

Barnhart, L., Akbarian Bafghi, R., Becker, S., & Raissi, M. (2025). Aligning to what? Limits to RLHF based alignment. arXiv. https://arxiv.org/abs/2503.09025

Entezami, E., & Naseh, A. (2025). LLM misalignment via adversarial RLHF platforms. arXiv. https://arxiv.org/abs/2503.03039

Hou, Z., Du, P., Niu, Y., Du, Z., Zeng, A., Liu, X., Huang, M., Wang, H., Tang, J., & Dong, Y. (2024). Does RLHF scale? Exploring the impacts from data, model, and method. arXiv. https://arxiv.org/abs/2412.06000

Mukherjee, A., Bullo, M., & Gündüz, D. (2025). SharedRep-RLHF: A shared representation approach to RLHF with diverse preferences. arXiv. https://arxiv.org/abs/2509.03672

Shi, R., Song, M., Zhou, R., Zhang, Z., Fazel, M., & Du, S. S. (2025). Understanding the performance gap in preference learning: A dichotomy of RLHF and DPO. arXiv. https://arxiv.org/abs/2505.19770

Wei, R., Yu, H., Jain, S., Sivakumar, Y., Tiwari, D., Li, J., Park, S.-J., & Wang, H. (2026). RLHFless: Serverless computing for efficient RLHF. arXiv. https://arxiv.org/abs/2602.22718

Wu, J., Chang, W., Liu, X., He, G., Hong, H., Liu, B., Tian, H., Yang, T., Shi, Y., Lin, F., & Yao, T. (2025). G-Core: A simple, scalable and balanced RLHF trainer. arXiv. https://arxiv.org/abs/2507.22789

Xiao, T., Yuan, Y., Li, M., Chen, Z., & Honavar, V. G. (2025). On a connection between imitation learning and RLHF. arXiv. https://arxiv.org/abs/2503.05079

Yang, Z., Gu, Z., Qi, H., & Yuan, Y. (2025). Accelerating RLHF training with reward variance increase. arXiv. https://arxiv.org/abs/2505.23247

Zhu, K., Wang, Y., Sun, Y., Chen, Q., Liu, J., Zhang, G., & Wang, J. (2024). Continual SFT matches multimodal RLHF with negative supervision. arXiv. https://arxiv.org/abs/2411.14797
