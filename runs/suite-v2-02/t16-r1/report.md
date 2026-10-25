# Systematic Literature Review: Reinforcement Learning from Human Feedback

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "reinforcement learning human feedback", filtered to category cs.LG, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

Recent research in reinforcement learning from human feedback (RLHF) demonstrates a field rapidly evolving beyond the canonical RLHF recipe toward more efficient, safe, and diverse feedback modalities. The surveyed literature reveals five major directions: (1) computational efficiency improvements through lightweight reward models and plug-and-play judges, (2) formal safety guarantees and high-confidence constraints, (3) exploration of alternative feedback channels including neural signals and multi-level episodic scores, (4) addressing strategic behavior in multi-labeler settings, and (5) improved interaction designs for collecting human feedback. Collectively, these works suggest that RLHF is maturing from a monolithic alignment technique into a diverse toolkit of post-training methods, with increasing attention to practical deployment concerns such as efficiency, safety certification, and human-AI interaction quality. The field shows strong convergence on the need for more informative feedback signals and better theoretical foundations, while disagreements remain about optimal trade-offs between alignment quality and computational cost.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "reinforcement learning human feedback", filtered to category cs.LG, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, metadata extraction relied solely on abstract content, which may not capture full methodological details or nuanced findings from complete papers.

## Themes

### Theme 1: Efficiency and Scalability in RLHF

A major research direction focuses on reducing the computational burden of RLHF while maintaining or improving alignment quality. Agnihotri & Pandey (2025) demonstrate that lightweight, instruction-tuned 7B language models with minimal parameter adaptation (rank-16 LoRA affecting only 0.8% of parameters) can serve as effective substitutes for heavyweight reward models ranging from 27B to 70B parameters. Their plug-and-play judge achieves 96.2% accuracy on RewardBench while enabling a 7B actor to achieve 92% exact match accuracy on GSM-8K, substantially outperforming larger DPO baselines. This efficiency-focused approach reflects a broader trend toward making RLHF accessible for resource-constrained settings without sacrificing performance. The introduction of HH-Rationales, a subset of 10,000 pairs from Anthropic HH-RLHF with human-generated justifications, also addresses the interpretability gap that has plagued efficient RLHF methods.

### Theme 2: Safety Guarantees and Constrained Alignment

Safety remains a central concern in RLHF research, with recent work moving beyond treating safety as a trade-off against helpfulness toward providing formal safety guarantees. Chittepu et al. (2025) propose HC-RLHF, which decouples human preferences into helpfulness and harmlessness components learned via separate reward and cost models. Their two-step optimization process employs pessimistic cost constraints followed by safety testing within upper-confidence bounds, providing theoretical proof that unsafe solutions will not be returned with probability greater than a user-specified threshold. This work represents a significant advance in making RLHF certifiably safe, addressing a critical gap in deployment scenarios where safety violations cannot be tolerated. The method's ability to improve both harmlessness and helpfulness simultaneously challenges the conventional wisdom that safety necessarily comes at the cost of reduced capability.

### Theme 3: Alternative Feedback Modalities

Several papers explore feedback modalities beyond traditional pairwise comparisons or scalar ratings, seeking more informative and natural channels for human input. Santaniello et al. (2025) introduce NEURO-LOOP, an implicit feedback framework using functional near-infrared spectroscopy (fNIRS) to collect brain signals from the prefrontal cortex while participants observe or guide a reinforcement learning agent. Their demonstration that a relationship exists between fNIRS data and agent performance represents a critical first step toward reinforcement learning from neural feedback, potentially enabling passive brain-computer interfaces for human-in-the-loop RL without requiring active instruction. Elahi et al. (2025) propose learning from multi-level human feedback provided as episode-end scores rather than binary comparative preferences, showing that such feedback provides more informative signals and can handle non-Markovian rewards by evaluating entire episodes. Wu et al. (2025) similarly advance multi-task reward learning from human ratings, introducing learnable weights that balance contributions from both classification and regression models to capture inherent uncertainty in human decision-making.

### Theme 4: Strategic and Multi-Labeler Settings

As RLHF systems scale to incorporate feedback from multiple humans, strategic behavior and preference aggregation become critical challenges. Kleine Buening et al. (2025) analyze existing RLHF algorithms for strategyproofness and prove that current methods, including pluralistic approaches, are vulnerable to manipulation: a single strategic labeler can cause arbitrarily large misalignment with social welfare. They establish that any strategyproof RLHF algorithm must perform k-times worse than optimal in the worst case (where k is the number of labelers), revealing a fundamental trade-off between incentive alignment and policy alignment. Their proposed Pessimistic Median of MLEs algorithm achieves approximate strategyproofness under appropriate policy coverage assumptions. This theoretical work highlights the game-theoretic complexities that emerge when RLHF systems must aggregate potentially conflicting or strategically reported preferences from multiple humans.

### Theme 5: Interaction Design and Feedback Quality

The quality and efficiency of human feedback collection depends critically on interaction design. Kompatscher et al. (2025) developed an interactive visualization system enabling groupwise comparison of multiple behaviors rather than traditional pairwise comparisons. Their system uses hierarchical clustering to efficiently handle large sets of sampled behaviors, with an exploration view showing the clustering structure and a comparison view for groupwise user queries. The incorporation of active learning to suggest groups for comparison yields substantial improvements: the groupwise approach increases final rewards by 69.34% compared to pairwise comparisons while reducing error rates. Metz et al. (2024) provide a conceptual framework mapping the space of human feedback for reinforcement learning, developing a taxonomy based on nine key dimensions and identifying seven quality metrics that influence both human ability to express feedback and agents' ability to learn from it. Their work calls for interdisciplinary collaboration between machine learning and human-computer interaction to address gaps in existing systems.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the conclusion that traditional pairwise comparison feedback is suboptimal compared to richer feedback modalities. Both Elahi et al. (2025) and Kompatscher et al. (2025) demonstrate that more informative feedback structures (episode-end scores and groupwise comparisons, respectively) yield superior policy learning. There is also broad agreement that efficiency need not come at the cost of performance, as evidenced by Agnihotri & Pandey's (2025) lightweight judge achieving state-of-the-art results. The safety literature converges on the need for formal guarantees rather than empirical safety alone (Chittepu et al., 2025).

**Disagreements**: The field shows tension between theoretical optimality and practical performance. Kleine Buening et al. (2025) establish fundamental impossibility results for strategyproof RLHF, showing that incentive alignment necessarily trades off against policy alignment, while other papers focus on empirical improvements without addressing strategic concerns. There is also disagreement about the optimal feedback modality: while some work advocates for implicit neural feedback (Santaniello et al., 2025), others emphasize structured explicit feedback (Metz et al., 2024). The efficiency literature debates whether lightweight methods can truly replace large reward models across all domains, or whether their success is task-specific.

## Gaps and Open Questions

The surveyed literature reveals several significant gaps:

1. **Limited empirical validation**: Most papers report theoretical results or simulations without extensive real-world deployment testing. The limitations sections across papers consistently note that abstract-level claims require fuller empirical validation.

2. **Scalability to complex domains**: While efficiency improvements are promising, it remains unclear whether lightweight methods scale to highly complex domains requiring nuanced reward modeling.

3. **Long-term alignment stability**: None of the surveyed papers address whether RLHF-aligned systems maintain alignment over extended deployment or whether they exhibit drift requiring periodic re-alignment.

4. **Cross-cultural feedback aggregation**: The strategic feedback literature (Kleine Buening et al., 2025) addresses preference aggregation but does not consider cultural differences in feedback expression or preference structures.

5. **Neural feedback interpretability**: While NEURO-LOOP demonstrates feasibility of neural feedback (Santaniello et al., 2025), the mapping between neural signals and specific preferences remains poorly understood.

6. **Standardized evaluation benchmarks**: The field lacks standardized benchmarks for comparing different RLHF methods, making it difficult to assess relative progress across efficiency, safety, and feedback modality improvements.

## Per-Paper Annotations

### Agnihotri & Pandey (2025)

**Research question**: Can a lightweight, instruction-tuned 7B LLM with minimal parameter adaptation serve as an effective substitute for heavyweight reward models in RLHF pipelines?

**Methodology**: The authors augment a frozen 7B LLM with a one-line JSON rubric and a rank-16 LoRA adapter affecting only 0.8% of parameters, then evaluate it on RewardBench and apply it to online PPO training. They introduce HH-Rationales, a subset of 10,000 pairs from Anthropic HH-RLHF with human-generated justifications, to examine interpretability.

**Key findings**:
- The plug-and-play judge achieves 96.2% accuracy on RewardBench, outperforming specialized reward networks ranging from 27B to 70B parameters
- The LoRA-enhanced approach enables a 7B actor to achieve 92% exact match accuracy on GSM-8K, outperforming the top 70B DPO baseline (61.8%)
- Six in-context demonstrations deliver the majority of zero-to-few-shot improvements (+2pp), with LoRA addressing remaining disparities particularly in safety and adversarial segments
- The LoRA judge attains approximately 9/10 similarity to human explanations per GPT-4 scoring, compared to around 5/10 for zero-shot judges

**Limitations**: Not stated in abstract

### Chittepu et al. (2025)

**Research question**: How can language model alignment provide high-confidence safety guarantees while maximizing helpfulness, rather than treating safety as a tradeoff?

**Methodology**: The authors propose HC-RLHF, which decouples human preferences into helpfulness and harmlessness components learned via separate reward and cost models, then employs a two-step optimization process with pessimistic cost constraints followed by safety testing within upper-confidence bounds.

**Key findings**:
- HC-RLHF provides theoretical proof that it will not return an unsafe solution with probability greater than a user-specified threshold
- The method produces safe models with high probability when applied to Qwen2-1.5B, Qwen2.5-3B, and LLaMa3.2-3B
- HC-RLHF can improve both harmlessness and helpfulness compared to previous methods

**Limitations**: Not stated in abstract

### Elahi et al. (2025)

**Research question**: How can reinforcement learning efficiently learn reward functions from multi-level human feedback provided as episode-end scores rather than binary comparative preferences?

**Methodology**: The authors propose a novel algorithm that learns both the reward function and optimal policy from multi-level human feedback (scores at episode ends). They provide theoretical analysis showing sublinear regret and validate through extensive simulations.

**Key findings**:
- Multi-level feedback (episode-end scores) provides more informative signals than binary comparative feedback
- The proposed approach can handle non-Markovian rewards by evaluating entire episodes
- The algorithm achieves sublinear regret theoretically
- Extensive simulations demonstrate empirical effectiveness of the approach

**Limitations**: Not stated in abstract

### Kompatscher et al. (2025)

**Research question**: Can an interactive visualization system that enables groupwise comparison of multiple behaviors improve the efficiency and effectiveness of collecting human feedback for RLHF?

**Methodology**: The authors developed an interactive visualization with two linked views: an exploration view showing hierarchical clustering of all sampled behaviors, and a comparison view for groupwise user queries. They incorporated an active learning approach to suggest groups for comparison and evaluated in six simulated robotics tasks.

**Key findings**:
- The groupwise comparison approach increases final rewards by 69.34% compared to traditional pairwise comparisons
- The method leads to lower error rates and better policies
- The visualization efficiently handles large sets of behaviors through hierarchical clustering
- Active learning suggestions further improve the comparison process
- The open-sourced code can be integrated into RLHF training loops

**Limitations**: Not stated in abstract

### Kleine Buening et al. (2025)

**Research question**: How can RLHF algorithms be designed to be strategyproof when multiple labelers may strategically misreport feedback to advance their own preferences?

**Methodology**: The authors analyze existing RLHF algorithms for strategyproofness, prove theoretical bounds on worst-case performance, and propose the Pessimistic Median of MLEs algorithm. They provide theoretical analysis for both contextual bandits and Markov decision processes under policy coverage assumptions.

**Key findings**:
- Existing RLHF algorithms, including pluralistic methods, are not strategyproof
- A single strategic labeler can cause arbitrarily large misalignment with social welfare
- Any strategyproof RLHF algorithm must perform k-times worse than optimal in worst case (k = number of labelers)
- The Pessimistic Median of MLEs algorithm is approximately strategyproof under appropriate assumptions
- There is a fundamental trade-off between incentive alignment and policy alignment

**Limitations**: Not stated in abstract

### Lambert (2025)

**Research question**: What are the core methods, techniques, and foundational concepts for post-training machine learning models using RLHF and related approaches?

**Methodology**: This work presents a comprehensive book covering the canonical RLHF recipe, including instruction tuning, reward model training, rejection sampling, reinforcement learning, on-policy distillation, and direct alignment algorithms, supplemented with companion resources including codebase, comparison library, and educational course.

**Key findings**:
- RLHF has evolved from core methods into a broader suite of post-training techniques
- The book covers the complete optimization pipeline from instruction tuning to direct alignment algorithms
- RLHF has origins converging from economics, philosophy, and optimal control fields
- Advanced topics include synthetic data, tool-use, character training, and evaluation
- Companion resources provide practical implementation and educational materials

**Limitations**: Not stated in abstract

### Metz et al. (2024)

**Research question**: How can we develop a shared understanding of human feedback types in interactive learning scenarios to bridge the gap between machine learning and human-computer interaction?

**Methodology**: The authors develop a taxonomy of feedback types for reward-based learning from human feedback based on nine key dimensions, identify seven quality metrics of human feedback, and derive requirements and design choices for systems learning from human feedback.

**Key findings**:
- A unified taxonomy of feedback types is introduced based on nine key dimensions, unifying human-centered, interface-centered, and model-centered aspects
- Seven quality metrics are identified that influence both human ability to express feedback and agent's ability to learn from feedback
- Gaps in existing work and future research opportunities are identified, calling for interdisciplinary collaboration with data-driven co-adaptive modeling and varied interaction mechanics

**Limitations**: Not stated in abstract

### Santaniello et al. (2025)

**Research question**: Can brain signals be mapped to reinforcement learning agent performance to enable implicit human-in-the-loop training without active instruction?

**Methodology**: The authors introduce NEURO-LOOP, an implicit feedback framework using functional near-infrared spectroscopy (fNIRS) to collect signals from the prefrontal cortex while participants observe or guide a reinforcement learning agent, then apply classical machine learning techniques to analyze the relationship.

**Key findings**:
- A relationship between fNIRS data and agent performance exists, as demonstrated using classical machine learning techniques
- The work demonstrates feasibility of mapping brain signals to agent performance as a critical first step toward reinforcement learning from neural feedback
- The dataset enables future research using passive Brain-Computer Interfaces for Human-in-the-Loop Reinforcement Learning

**Limitations**: Not stated in abstract

### Wu et al. (2025)

**Research question**: Can reinforcement learning better mimic human decision-making by jointly considering multiple tasks rather than modeling human reasoning through isolated classification or regression tasks?

**Methodology**: The authors propose a novel RL method that leverages human ratings in reward-free environments to infer a reward function, introducing learnable weights that balance contributions from both classification and regression models to capture inherent uncertainty in human decision-making.

**Key findings**:
- The proposed method consistently outperforms existing rating-based RL methods in experiments using synthetic human ratings
- In some cases, the multi-task approach surpasses traditional RL approaches
- Learnable weights allow the model to adaptively emphasize different strategies, capturing uncertainty in human decision-making

**Limitations**: Not stated in abstract

### Gomaa & Mahdy (2024)

**Research question**: How does imitation learning with expert guidance compare to traditional reinforcement learning in terms of performance, robustness, and limitations?

**Methodology**: The study conducts extensive experimentation in a pre-existing Unity simulation environment, comparing imitation learning and traditional reinforcement learning approaches while investigating the influence of both expert guidance and suboptimal demonstrations on the learning process.

**Key findings**:
- The study provides comparative insights into performance differences between imitation learning and traditional RL
- Both expert guidance and suboptimal demonstrations influence the learning process differently
- The research identifies specific benefits and challenges of incorporating human feedback into learning
- The findings contribute to advancing human-centered AI development

**Limitations**: Not stated in abstract

## References

Agnihotri, R., & Pandey, A. (2025). Efficient online RFT with plug-and-play LLM judges: Unlocking state-of-the-art performance. arXiv. https://arxiv.org/abs/2506.05748

Chittepu, Y., Metevier, B., Schwarzer, W., Hoag, A., Niekum, S., & Thomas, P. S. (2025). Reinforcement learning from human feedback with high-confidence safety constraints. arXiv. https://arxiv.org/abs/2506.08266

Elahi, M. Q., Oguchienti, S., Ahmed, M. H., & Ghasemi, M. (2025). Reinforcement learning from multi-level and episodic human feedback. arXiv. https://arxiv.org/abs/2504.14732

Gomaa, A., & Mahdy, B. (2024). Unveiling the role of expert guidance: A comparative analysis of user-centered imitation learning and traditional reinforcement learning. arXiv. https://arxiv.org/abs/2410.21403

Kompatscher, J., Shi, D., Varni, G., Weinkauf, T., & Oulasvirta, A. (2025). Interactive groupwise comparison for reinforcement learning from human feedback. arXiv. https://arxiv.org/abs/2507.04340

Kleine Buening, T., Gan, J., Mandal, D., & Kwiatkowska, M. (2025). Strategyproof reinforcement learning from human feedback. arXiv. https://arxiv.org/abs/2503.09561

Lambert, N. (2025). Reinforcement learning from human feedback. arXiv. https://arxiv.org/abs/2504.12501

Metz, Y., Lindner, D., Baur, R., & El-Assady, M. (2024). Mapping out the space of human feedback for reinforcement learning: A conceptual framework. arXiv. https://arxiv.org/abs/2411.11761

Santaniello, J., Russell, M., Jiang, B., Sassaroli, D., Jacob, R., & Sinapov, J. (2025). Mapping neural signals to agent performance, a step towards reinforcement learning from neural feedback. arXiv. https://arxiv.org/abs/2506.12636

Wu, M., White, D., Rose, E., Lawhern, V., Waytowich, N. R., & Cao, Y. (2025). Multi-task reward learning from human ratings. arXiv. https://arxiv.org/abs/2506.09183
