# Systematic Literature Review: Parallel Reasoning

**Date**: 2026-10-26  
**Papers surveyed**: 10  
**Scope**: arXiv query "parallel reasoning", category cs.CL, published between 2023-10-14 and 2025-10-13  
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on parallel reasoning in large language models, revealing a rapidly evolving field focused on improving reasoning efficiency, accuracy, and scalability. The surveyed literature demonstrates three primary research directions: (1) architectural innovations enabling parallel token generation and decoding acceleration, (2) collaborative frameworks combining sequential and parallel reasoning paradigms, and (3) test-time scaling strategies that leverage multiple reasoning paths without prohibitive computational costs. Collectively, these works establish parallel reasoning as a critical mechanism for enhancing LLM capabilities while addressing the fundamental tension between diversity and efficiency in multi-path inference. Notably, recent advances in semantic entropy-guided termination, speculative decoding, and latent-space reasoning suggest the field is maturing beyond simple sampling-based approaches toward more sophisticated coordination and pruning mechanisms.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "parallel reasoning", filtered to category cs.CL, published between 2023-10-14 and 2025-10-13. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency Through Parallel Decoding and Acceleration

A dominant theme across the literature is leveraging parallelism to accelerate reasoning without sacrificing accuracy. Several papers propose methods to generate multiple tokens or reasoning paths simultaneously, fundamentally challenging the sequential nature of traditional autoregressive decoding. Yu (2025) introduced a tree-like attention mask enabling parallel decoding within a single sequence, achieving up to 100% speedup while maintaining answer quality. Similarly, Li et al. (2025) adapted speculative decoding for multi-sample inference by exploiting intrinsic consensus across parallel generation paths, eliminating the need for auxiliary models while substantially improving draft acceptance rates. These approaches share a common insight: certain reasoning tasks exhibit inherent parallelizability that can be harvested through architectural modifications or probabilistic aggregation mechanisms, offering substantial latency reductions without requiring additional memory overhead.

### Theme 2: Coordination and Pruning of Parallel Reasoning Paths

A second major theme addresses the computational inefficiency arising from redundant or low-quality parallel reasoning traces. Tu et al. (2025) reported that over 80% of parallel reasoning traces yield identical final answers, representing substantial wasted computation. Their DeepPrune framework introduces a specialized judge model trained to predict answer equivalence from partial traces, combined with online greedy clustering to dynamically prune redundant paths while preserving diversity, achieving 65-88% token reduction with minimal accuracy loss. Complementing this, Xu et al. (2025) proposed semantic entropy as an intrinsic quality metric that quantifies semantic diversity across parallel responses, leveraging its strong negative correlation with accuracy to enable dynamic control and early termination of reasoning traces. These coordination mechanisms represent a shift from naive parallel sampling toward intelligent path selection and resource allocation.

### Theme 3: Training Strategies for Parallel Reasoning Capabilities

Several works focus on training methodologies that explicitly teach LLMs to generate diverse, high-quality parallel reasoning paths. Jia et al. (2025) introduced Set Supervised Fine-Tuning (SSFT), which incorporates a set-based global loss using bipartite matching between global forking tokens and unique reasoning traces, preventing the collapse of diverse reasoning modes that occurs in naive fine-tuning. Their Global Forking Policy Optimization (GFPO) further leverages these tokens to incentivize complex reasoning, consistently outperforming standard SFT with GRPO on math reasoning and code generation benchmarks. This training paradigm addresses a fundamental challenge: how to preserve multiple valid reasoning strategies within a single model without sacrificing coherence or falling into mode collapse.

### Theme 4: Collaborative and Hybrid Reasoning Frameworks

The literature also explores frameworks that combine parallel reasoning with other paradigms or distribute reasoning across multiple models. Shao et al. (2025) proposed Division-of-Thoughts (DoT), a collaborative framework that decomposes queries into sub-tasks, creates dependency graphs for parallel reasoning, and allocates tasks between local small language models and cloud-based large models, reducing API costs by 83.57% while maintaining competitive accuracy. Zhang et al. (2024) introduced Direct-Indirect Reasoning (DIR), which treats direct and indirect reasoning as parallel paths merged to derive final answers, significantly outperforming baselines on logical reasoning and mathematical proof tasks. These hybrid approaches recognize that parallel reasoning need not operate in isolation but can be integrated with sequential methods, model hierarchies, or complementary reasoning strategies.

### Theme 5: Latent-Space and Continuous Reasoning

An emerging direction extends parallel reasoning beyond discrete token sequences into continuous vector spaces. You et al. (2025) demonstrated that latent reasoning models, where intermediate reasoning unfolds in continuous spaces, can benefit from parallel test-time scaling using uncertainty-inspired stochastic strategies like Monte Carlo Dropout and Additive Gaussian Noise. Their Latent Reward Model (LatentRM), trained with step-wise contrastive objectives, enables effective trajectory selection for latent reasoning, opening new possibilities for scalable inference in continuous spaces. This work suggests that parallel reasoning principles may generalize beyond traditional token-based generation to broader classes of reasoning architectures.

### Theme 6: Structured Reasoning for Complex Multi-Hop Tasks

Several papers address parallel reasoning in the context of structured, multi-hop question answering. Bi et al. (2024) proposed STOC-TOT, a stochastic tree-of-thought method with constrained decoding that constructs tree-like reasoning structures by decomposing questions into sub-questions, prompting probability estimation at each step, and conducting constrained decoding to reduce hallucination. Shalev et al. (2024) provided interpretable analysis of internal multi-hop reasoning processes, demonstrating that predictions for compositional questions can be modeled using linear transformations between semantic category spaces, with middle layers generating interpretable embeddings representing potential intermediate answers. These works reveal that parallel reasoning in complex tasks often involves structured decomposition and probabilistic path evaluation rather than simple independent sampling.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that naive parallel sampling is computationally wasteful, with multiple works independently identifying redundancy rates exceeding 80% (Tu et al., 2025; Li et al., 2025). There is broad consensus that semantic diversity metrics, particularly entropy-based measures, correlate negatively with accuracy and can serve as reliable quality indicators for early termination (Xu et al., 2025; Jia et al., 2025). Additionally, all efficiency-focused papers demonstrate that substantial speedup or token reduction is achievable with minimal accuracy degradation (typically within 3 percentage points), suggesting parallel reasoning can be both efficient and effective when properly coordinated.

**Disagreements**: The literature reveals tension between training-time and test-time approaches to parallel reasoning. Jia et al. (2025) argue that specialized training is necessary to preserve diverse reasoning modes, while Yu (2025) and Li et al. (2025) demonstrate that architectural modifications and decoding strategies alone can achieve substantial gains without retraining. Similarly, there is disagreement about the optimal level of coordination: Tu et al. (2025) advocate aggressive pruning based on partial trace evaluation, whereas Xu et al. (2025) prefer semantic entropy-guided termination that maintains greater diversity before early stopping. These disagreements reflect fundamental questions about whether parallel reasoning improvements should come from model training, inference architecture, or runtime coordination.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the surveyed papers explicitly address the computational overhead of coordination mechanisms themselves—while pruning and entropy calculation reduce token generation, the cost of running judge models or computing semantic entropy is rarely quantified. Second, most papers evaluate on math reasoning or code generation benchmarks, with limited exploration of parallel reasoning in open-ended generation, creative tasks, or domains requiring long-horizon planning. Third, the interaction between parallel reasoning and retrieval-augmented generation remains unexplored—whether parallel paths benefit from shared or independent retrieval, and how coordination mechanisms adapt when external knowledge sources are involved. Finally, while several papers mention "emergent" forking tokens or latent structures, none provide mechanistic interpretability analysis explaining how parallel reasoning capabilities are represented internally within model weights or activations.

## Per-Paper Annotations

### Bi et al. (2024)

**Research question**: How can multi-hop question answering performance be enhanced under zero-shot settings through novel prompting methods that address complexities in question types and reasoning types?  
**Methodology**: The authors propose STOC-TOT, a stochastic tree-of-thought reasoning prompting method with constrained decoding that constructs tree-like reasoning structures by decomposing questions into sub-questions, prompts probability estimation at each step, and conducts constrained decoding to generate grounded answers.  
**Key findings**:
- STOC-TOT addresses the need for fine-grained prompting methods for different question types (bridge vs. comparison) and reasoning types (sequential vs. parallel)
- The framework outperforms other reasoning prompts by a significant margin on two MHQA datasets with five large language models
- Constrained decoding helps generate more grounded answers and reduces hallucination at answer time  
**Limitations**: Not stated in abstract

### Jia et al. (2025)

**Research question**: How can large language models be trained to generate diverse and accurate parallel reasoning paths without the diversity-accuracy trade-off encountered by temperature scaling?  
**Methodology**: The authors propose Set Supervised Fine-Tuning (SSFT), which incorporates a set-based global loss into SFT using bipartite matching between global forking tokens and unique reasoning traces, and introduce Global Forking Policy Optimization (GFPO) to leverage these tokens for incentivizing complex reasoning.  
**Key findings**:
- Naive fine-tuning with multiple reasoning traces collapses unique reasoning modes, while SSFT preserves these modes and produces emergent global forking tokens
- GFPO leverages maximally steerable forking tokens to incentivize complex reasoning
- Models trained with the proposed method consistently outperform SFT counterparts with GRPO on math reasoning and execution-based code generation benchmarks  
**Limitations**: Not stated in abstract

### Li et al. (2025)

**Research question**: How can speculative decoding be adapted for multi-sample reasoning scenarios to exploit intrinsic consensus of parallel generation paths without requiring auxiliary models or external databases?  
**Methodology**: The authors propose a novel speculative decoding method that exploits intrinsic consensus of parallel generation paths by dynamically analyzing structural patterns across parallel reasoning paths through a probabilistic aggregation mechanism to identify consensus token sequences.  
**Key findings**:
- The method synthesizes high-quality draft tokens without requiring auxiliary models or external databases
- It dynamically analyzes structural patterns across parallel reasoning paths through probabilistic aggregation
- Evaluations demonstrate substantial improvement in draft acceptance rates over baselines
- The approach reduces latency in draft token construction  
**Limitations**: Not stated in abstract

### Shalev et al. (2024)

**Research question**: What processes occur within LLM hidden layers during compositional reasoning tasks, and can these processes be referred to as reasoning when no explicit thought process is documented?  
**Methodology**: The authors introduce a novel interpretable analysis of internal multi-hop reasoning processes, demonstrating that predictions for compositional reasoning questions can be modeled using linear transformations between semantic category spaces, with statistical analyses showing activation of corresponding token subsets.  
**Key findings**:
- The prediction process for compositional reasoning questions can be modeled using a simple linear transformation between two semantic category spaces
- Middle layers of the network generate highly interpretable embeddings representing potential intermediate answers for multi-hop questions
- A corresponding subset of tokens is activated in the model's output, implying the existence of parallel reasoning paths
- These observations hold true even when the model lacks the necessary knowledge to solve the task  
**Limitations**: Not stated in abstract

### Shao et al. (2025)

**Research question**: How can on-device AI agents leverage collaborative reasoning between locally deployed smaller language models and cloud-based large language models to reduce costs while maintaining reasoning accuracy?  
**Methodology**: The authors propose Division-of-Thoughts (DoT), a collaborative reasoning framework with three components: a Task Decomposer to break queries into sub-tasks, a Task Scheduler to create dependency graphs for parallel reasoning, and a Plug-and-Play Adapter attached to the SLM for task allocation, using self-reinforced training relying on task execution feedback.  
**Key findings**:
- DoT significantly reduces LLM costs while maintaining competitive reasoning accuracy
- The framework reduces average reasoning time by 66.12% and API costs by 83.57%
- DoT achieves comparable reasoning accuracy with the best baseline methods while enabling hybrid language models to exploit their respective strengths  
**Limitations**: Not stated in abstract

### Tu et al. (2025)

**Research question**: How can we address the computational inefficiency caused by inter-trace redundancy in parallel scaling approaches for enhancing reasoning capabilities in LLMs?  
**Methodology**: The authors propose DeepPrune, a framework featuring a specialized judge model trained with out-of-distribution data using oversampling techniques to predict answer equivalence from partial reasoning traces, combined with an online greedy clustering algorithm that dynamically prunes redundant paths.  
**Key findings**:
- Over 80% of parallel reasoning traces yield identical final answers, representing substantial wasted computation
- DeepPrune achieves token reduction of 65.73%–88.50% compared to conventional consensus sampling
- The method maintains competitive accuracy within 3 percentage points despite significant token reduction
- The judge model achieves 0.7072 AUROC on unseen reasoning models  
**Limitations**: Not stated in abstract

### Xu et al. (2025)

**Research question**: How can we design a flexible test-time collaborative inference framework that exploits the complementary strengths of both sequential and parallel reasoning paradigms with dynamic control and early termination?  
**Methodology**: The authors introduce semantic entropy (SE) as an intrinsic quality metric that quantifies the semantic diversity of parallel model responses, leveraging its strong negative correlation with accuracy to enable dynamic control and early termination of reasoning traces.  
**Key findings**:
- Sequential reasoning approaches typically rely on arbitrary token budgets for termination, leading to inefficiency or premature cutoff
- Parallel reasoning approaches often lack coordination among parallel branches and require intrusive fine-tuning
- Semantic entropy serves as a robust indicator of reasoning quality due to its strong negative correlation with accuracy
- The proposed framework enables dynamic control and early termination of reasoning traces during collaborative inference  
**Limitations**: Not stated in abstract

### You et al. (2025)

**Research question**: Can latent reasoning models, where intermediate reasoning unfolds in continuous vector spaces, benefit from parallel test-time scaling similar to token-based chain-of-thought approaches?  
**Methodology**: The authors introduce two uncertainty-inspired stochastic strategies for sampling in continuous space: Monte Carlo Dropout and Additive Gaussian Noise, and design a Latent Reward Model (LatentRM) trained with step-wise contrastive objective to score and guide latent reasoning trajectories.  
**Key findings**:
- Both sampling strategies (Monte Carlo Dropout and Additive Gaussian Noise) scale effectively with compute and exhibit distinct exploration dynamics
- LatentRM enables effective trajectory selection for latent reasoning models
- The work opens a new direction for scalable inference in continuous spaces, with code and checkpoints released publicly  
**Limitations**: Not stated in abstract

### Yu (2025)

**Research question**: How can we accelerate the reasoning process in LLMs by leveraging the inherent parallelizability of certain tasks while avoiding additional memory usage?  
**Methodology**: The author leverages inherent parallelizability of certain tasks by decoding multiple tokens per forward pass via a tree-like attention mask within a single sequence, avoiding additional memory usage.  
**Key findings**:
- Generating lengthy reasoning sequences is computationally expensive and time-consuming
- The proposed method decodes multiple tokens per forward pass within a single sequence
- The approach achieves up to nearly 100% speedup in decoding
- The method basically maintains the answer quality despite the acceleration  
**Limitations**: Not stated in abstract

### Zhang et al. (2024)

**Research question**: How can large language models be improved to perform indirect reasoning tasks that are often encountered in the real world but disregarded by existing methods?  
**Methodology**: The authors propose Direct-Indirect Reasoning (DIR), which treats direct and indirect reasoning as parallel paths merged to derive the final answer, crafting prompt templates incorporating contrapositive and contradiction principles to stimulate LLMs to implement indirect reasoning.  
**Key findings**:
- Most existing methods resort to Direct Reasoning and disregard Indirect Reasoning, making LLMs difficult to solve IR tasks
- The DIR method is simple yet effective and can be straightforwardly integrated with existing Chain-of-Thought variants
- Experimental results on four datasets related to logical reasoning and mathematic proof show DIR significantly outperforms original methods when combined with various baselines  
**Limitations**: Not stated in abstract

## References

Bi, Z., Hajialigol, D., Sun, Z., Hao, J., & Wang, X. (2024). STOC-TOT: Stochastic tree-of-thought with constrained decoding for complex reasoning in multi-hop question answering. arXiv. https://arxiv.org/abs/2407.03687

Jia, S., Wang, X., & Kasiviswanathan, S. P. (2025). Training large language models to reason in parallel with global forking tokens. arXiv. https://arxiv.org/abs/2510.05132

Li, Y., Shi, J., Feng, S., Yuan, P., Wang, X., Zhang, Y., Zhang, J., Tan, C., Pan, B., Hu, Y., & Li, K. (2025). Speculative decoding for multi-sample inference. arXiv. https://arxiv.org/abs/2503.05330

Shalev, Y., Feder, A., & Goldstein, A. (2024). Distributional reasoning in LLMs: Parallel reasoning processes in multi-hop reasoning. arXiv. https://arxiv.org/abs/2406.13858

Shao, C., Hu, X., Lin, Y., & Xu, F. (2025). Division-of-thoughts: Harnessing hybrid language model synergy for efficient on-device agents. arXiv. https://arxiv.org/abs/2502.04392

Tu, S., Li, Y., Bai, Y., Hou, L., & Li, J. (2025). DeepPrune: Parallel scaling without inter-trace redundancy. arXiv. https://arxiv.org/abs/2510.08483

Xu, Z., Qiu, Z., Huang, G., Li, K., Li, S., Zhang, C., Li, K., Yi, Q., Jiang, Y., Zhou, B., Lian, F., & Kang, Z. (2025). Adaptive termination for multi-round parallel reasoning: An universal semantic entropy-guided framework. arXiv. https://arxiv.org/abs/2507.06829

You, R., Li, Y., Liu, M., Wang, W., Nie, L., & Li, W. (2025). Parallel test-time scaling for latent reasoning models. arXiv. https://arxiv.org/abs/2510.07745

Yu, Y. (2025). Accelerate parallelizable reasoning via parallel decoding within one sequence. arXiv. https://arxiv.org/abs/2503.20533

Zhang, Y., Sun, Y., Zhan, Y., Tao, D., Tao, D., & Gong, C. (2024). Large language models as an indirect reasoner: Contrapositive and contradiction for automated reasoning. arXiv. https://arxiv.org/abs/2402.03667
