# Systematic Literature Review: Parallel Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "parallel reasoning", category cs.CL, published between 2023-10-14 and 2025-10-13
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent papers on parallel reasoning in large language models, revealing a rapidly evolving field focused on improving efficiency, scalability, and controllability of parallel inference mechanisms. The surveyed literature demonstrates strong convergence around the need to reduce computational redundancy in parallel reasoning traces while maintaining or improving accuracy. Researchers are developing diverse approaches including dynamic termination mechanisms, pruning strategies, speculative decoding, and novel training methods that enable LLMs to generate diverse yet accurate reasoning paths. A notable trend is the shift from naive parallel sampling toward intelligent coordination mechanisms that exploit semantic diversity, consensus patterns, and hybrid sequential-parallel frameworks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "parallel reasoning", filtered to category cs.CL, published between 2023-10-14 and 2025-10-13. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency Optimization in Parallel Reasoning

A dominant theme across the surveyed literature is addressing computational inefficiency in parallel reasoning. Multiple papers identify that naive parallel sampling generates substantial redundancy, with Tu et al. (2025) reporting that over 80% of parallel reasoning traces yield identical final answers, representing wasted computation. Their DeepPrune framework achieves 65.73%–88.50% token reduction through dynamic pruning of redundant paths while preserving answer diversity.

Similarly, Yu (2025) proposes accelerating parallelizable reasoning via parallel decoding within a single sequence using tree-like attention masks, achieving up to nearly 100% speedup without additional memory overhead. Li et al. (2025) adapt speculative decoding for multi-sample inference by exploiting intrinsic consensus among parallel generation paths to synthesize high-quality draft tokens without auxiliary models, substantially improving draft acceptance rates on mathematical reasoning benchmarks.

Shao et al. (2025) take a different approach with Division-of-Thoughts, which decomposes tasks into sub-components and allocates them between local small language models and cloud-based large models based on difficulty, reducing average reasoning time by 66.12% and API costs by 83.57% while maintaining competitive accuracy.

### Theme 2: Training Methods for Parallel Reasoning

Jia et al. (2025) address the fundamental challenge of training LLMs to generate diverse and accurate parallel reasoning paths. They observe that naive fine-tuning with multiple reasoning traces collapses unique reasoning modes, losing diversity. Their Set Supervised Fine-Tuning (SSFT) treats parallel reasoning as a set-of-next-token-prediction problem, incorporating set-based global loss using bipartite matching between global forking tokens and unique reasoning traces.

The authors further introduce Global Forking Policy Optimization (GFPO) to leverage these tokens for incentivizing complex reasoning. Their findings reveal that global forking tokens triggering diverse yet correct reasoning modes typically emerge deep in the sampling tree for challenging problems, and that temperature scaling encounters a worsened trade-off between diversity and accuracy. GFPO-trained models consistently outperform SFT counterparts with GRPO on math reasoning and execution-based code generation benchmarks.

### Theme 3: Dynamic Control and Adaptive Termination

Xu et al. (2025) identify critical limitations in existing parallel reasoning frameworks: sequential reasoning relies on arbitrary token budgets for termination leading to inefficiency or premature cutoff, while parallel reasoning lacks coordination among branches and requires intrusive fine-tuning. They introduce semantic entropy (SE) as an intrinsic quality metric that quantifies semantic diversity of parallel model responses.

Their key insight is that SE serves as a robust indicator of reasoning quality due to its strong negative correlation with accuracy, enabling dynamic control and early termination of reasoning traces. This universal semantic entropy-guided framework provides flexible test-time collaborative inference that exploits complementary strengths of both sequential and parallel reasoning paradigms.

### Theme 4: Internal Reasoning Mechanisms and Latent Processes

Two papers investigate the internal mechanisms underlying parallel reasoning in LLMs. Shalev et al. (2024) introduce novel interpretable analysis of internal multi-hop reasoning processes, demonstrating that predictions for compositional reasoning questions can be modeled using linear transformations between semantic category spaces. Their statistical analyses show that corresponding subsets of tokens are activated in the model's output, implying parallel reasoning paths exist even when the model lacks necessary knowledge to solve the task.

You et al. (2025) explore whether latent reasoning models can benefit from parallel test-time scaling despite the absence of sampling mechanisms in continuous space. They introduce two uncertainty-inspired stochastic sampling strategies for continuous space: Monte Carlo Dropout and Additive Gaussian Noise. Their Latent Reward Model (LatentRM), trained with step-wise contrastive objective, scores and guides latent reasoning trajectories for aggregation, opening new directions for scalable inference in continuous spaces.

### Theme 5: Hybrid and Structured Reasoning Approaches

Several papers propose hybrid approaches that combine parallel reasoning with other strategies. Zhang et al. (2024) propose Direct-Indirect Reasoning (DIR), which considers direct and indirect reasoning as parallel paths merged to derive the final answer. They stimulate indirect reasoning by crafting prompt templates incorporating contrapositive and contradiction principles. DIR can be straightforwardly integrated with existing Chain-of-Thought variants and significantly outperforms original methods on logical reasoning and mathematical proof datasets.

Bi et al. (2024) propose STOC-TOT, a stochastic tree-of-thought reasoning method that constructs tree-like structures by breaking questions into sub-questions to form different reasoning paths. The framework handles complexities in question types (bridge vs. comparison) and reasoning types (sequential vs. parallel), with probability estimation at each reasoning step enabling better trajectory selection and constrained decoding reducing hallucination.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all papers acknowledge that naive parallel sampling is computationally wasteful, with multiple studies reporting substantial redundancy in parallel traces. Second, there is consensus that intelligent coordination mechanisms—whether through pruning, dynamic termination, or speculative decoding—can dramatically reduce computational costs while maintaining accuracy. Third, researchers agree that parallel reasoning benefits from explicit structural mechanisms, whether through tree-based attention masks, task decomposition, or semantic entropy metrics.

**Disagreements**: While not direct contradictions, different papers emphasize different trade-offs. Jia et al. (2025) focus on training-time solutions that preserve diversity through specialized loss functions, while Xu et al. (2025) emphasize test-time control through semantic entropy. Similarly, efficiency-focused papers (Tu et al., 2025; Yu, 2025; Li et al., 2025) prioritize computational speedup, whereas mechanism-focused papers (Shalev et al., 2024; You et al., 2025) prioritize understanding and leveraging internal reasoning processes. The optimal balance between these approaches remains an open question.

## Gaps and Open Questions

Several notable gaps emerge from the surveyed literature. First, none of the abstracts explicitly state limitations of their approaches, suggesting either space constraints or insufficient self-critical analysis. Second, while multiple papers report impressive efficiency gains, few address whether these methods generalize across different model architectures, domains, or reasoning task types beyond mathematical and logical reasoning benchmarks.

Third, the interaction between parallel reasoning and model hallucination receives limited attention, with only Bi et al. (2024) explicitly addressing hallucination through constrained decoding. Fourth, there is limited discussion of how parallel reasoning methods perform on multi-modal tasks or non-text domains. Finally, the relationship between parallel reasoning and emergent capabilities in larger models remains unexplored—whether these methods scale favorably with model size or encounter diminishing returns is an open empirical question.

## Per-Paper Annotations

### Bi et al. (2024)

**Research question**: How can prompting methods be improved to enhance multi-hop question answering performance under zero-shot settings across different question and reasoning types?
**Methodology**: The authors propose STOC-TOT, a stochastic tree-of-thought reasoning method that constructs a tree-like structure by breaking questions into sub-questions to form different reasoning paths, with probability estimation for each path and constrained decoding at answer time.
**Key findings**:
- STOC-TOT outperforms other reasoning prompts by a significant margin on multi-hop question answering datasets
- The framework handles complexities in question types (bridge vs. comparison) and reasoning types (sequential vs. parallel)
- Probability estimation at each reasoning step enables better trajectory selection
- Constrained decoding generates more grounded answers and reduces hallucination
**Limitations**: Not stated in abstract

### Jia et al. (2025)

**Research question**: How can large language models be trained to generate diverse and accurate parallel reasoning paths for challenging problems?
**Methodology**: The authors propose Set Supervised Fine-Tuning (SSFT), which treats parallel reasoning as a set-of-next-token-prediction problem with set-based global loss using bipartite matching, and Global Forking Policy Optimization (GFPO) to leverage global forking tokens for incentivizing complex reasoning.
**Key findings**:
- Naive fine-tuning with multiple reasoning traces collapses unique reasoning modes, while SSFT preserves these modes and produces emergent global forking tokens
- Global forking tokens that trigger diverse yet correct reasoning modes are typically deep in the sampling tree for challenging problems
- Temperature scaling encounters a worsened trade-off between diversity and accuracy for parallel reasoning
- GFPO-trained models consistently outperform SFT counterparts with GRPO on math reasoning and execution-based code generation benchmarks
**Limitations**: Not stated in abstract

### Li et al. (2025)

**Research question**: How can speculative decoding be adapted for multi-sample reasoning scenarios like self-consistency and Best-of-N sampling?
**Methodology**: The method exploits intrinsic consensus of parallel generation paths to synthesize high-quality draft tokens without auxiliary models or external databases, using probabilistic aggregation to identify consensus token sequences that align with the decoding distribution.
**Key findings**:
- The method exploits intrinsic consensus of parallel generation paths for draft token synthesis
- No auxiliary models or external databases are required
- Probabilistic aggregation identifies consensus token sequences aligning with decoding distribution
- Substantial improvement in draft acceptance rates over baselines on mathematical reasoning benchmarks
- Reduces latency in draft token construction while enabling seamless integration with sampling-based techniques
**Limitations**: Not stated in abstract

### Shalev et al. (2024)

**Research question**: What processes occur within LLM hidden layers during multi-hop reasoning, and can these processes be characterized as reasoning?
**Methodology**: The authors introduce novel interpretable analysis of internal multi-hop reasoning processes, demonstrating that predictions for compositional reasoning questions can be modeled using linear transformations between semantic category spaces, with statistical analyses showing corresponding token subsets are activated in the output.
**Key findings**:
- Prediction processes for compositional reasoning can be modeled using simple linear transformations between semantic category spaces
- Middle layers generate highly interpretable embeddings representing potential intermediate answers for multi-hop questions
- Corresponding subsets of tokens are activated in the output, implying existence of parallel reasoning paths
- These observations hold even when the model lacks necessary knowledge to solve the task
**Limitations**: Not stated in abstract

### Shao et al. (2025)

**Research question**: How can on-device AI agents leverage hybrid language model collaboration to reduce costs while maintaining reasoning accuracy?
**Methodology**: The authors propose Division-of-Thoughts (DoT), a collaborative reasoning framework with three components: a Task Decomposer that breaks queries into sub-tasks, a Task Scheduler that creates dependency graphs for parallel reasoning, and a Plug-and-Play Adapter that allocates sub-tasks to either local SLMs or cloud LLMs based on difficulty using self-reinforced training.
**Key findings**:
- DoT reduces average reasoning time by 66.12% and API costs by 83.57% while maintaining competitive reasoning accuracy
- The Plug-and-Play Adapter allocates tasks without altering the SLM's parameters
- Task decomposition allows hybrid language models to exploit their respective strengths based on sub-task difficulty
- Self-reinforced training relies solely on task execution feedback to boost adapter allocation capability
**Limitations**: Not stated in abstract

### Tu et al. (2025)

**Research question**: How can we address the computational inefficiency caused by inter-trace redundancy in parallel scaling for LLM reasoning?
**Methodology**: The authors propose DeepPrune, a framework featuring a specialized judge model trained with out-of-distribution data using oversampling to predict answer equivalence from partial traces, combined with an online greedy clustering algorithm that dynamically prunes redundant paths while preserving answer diversity.
**Key findings**:
- Over 80% of parallel reasoning traces yield identical final answers, representing substantial wasted computation
- DeepPrune's judge model achieves 0.7072 AUROC on unseen reasoning models for predicting answer equivalence
- DeepPrune achieves 65.73%–88.50% token reduction compared to conventional consensus sampling
- Accuracy is maintained within 3 percentage points despite significant token reduction
- Code and data are publicly available at https://deepprune.github.io/
**Limitations**: Not stated in abstract

### Xu et al. (2025)

**Research question**: How can we design a flexible test-time collaborative inference framework that exploits the complementary strengths of both sequential and parallel reasoning paradigms with dynamic control and early termination?
**Methodology**: The authors introduce semantic entropy (SE) as an intrinsic quality metric that quantifies the semantic diversity of parallel model responses, leveraging its strong negative correlation with accuracy to enable dynamic control and early termination of reasoning traces.
**Key findings**:
- Sequential reasoning relies on arbitrary token budgets for termination, leading to inefficiency or premature cutoff
- Parallel reasoning often lacks coordination among parallel branches and requires intrusive fine-tuning
- Semantic entropy quantifies semantic diversity of parallel responses and correlates negatively with accuracy
- SE enables dynamic control and early termination of reasoning traces in collaborative inference
**Limitations**: Not stated in abstract

### Yu (2025)

**Research question**: How can we accelerate the reasoning process in LLMs by leveraging the inherent parallelizability of certain tasks?
**Methodology**: The method decodes multiple tokens per forward pass via a tree-like attention mask within a single sequence when multiple parallel reasoning steps exist, avoiding additional memory usage while maintaining answer quality.
**Key findings**:
- Generating lengthy reasoning sequences is computationally expensive and time-consuming
- The method leverages inherent parallelizability of certain tasks to accelerate reasoning
- Tree-like attention mask enables multiple token decoding per forward pass within one sequence
- The approach achieves up to nearly 100% speedup in decoding while maintaining answer quality
**Limitations**: Not stated in abstract

### You et al. (2025)

**Research question**: Can latent reasoning models benefit from parallel test-time scaling despite the absence of sampling mechanisms in continuous space?
**Methodology**: The authors introduce two uncertainty-inspired stochastic sampling strategies for continuous space: Monte Carlo Dropout and Additive Gaussian Noise, with a Latent Reward Model (LatentRM) trained with step-wise contrastive objective to score and guide latent reasoning trajectories for aggregation.
**Key findings**:
- Both sampling strategies scale effectively with compute and exhibit distinct exploration dynamics
- LatentRM enables effective trajectory selection for latent reasoning models
- The work opens a new direction for scalable inference in continuous spaces
- Code and checkpoints are released to support reproducibility
**Limitations**: Not stated in abstract

### Zhang et al. (2024)

**Research question**: How can large language models be enhanced to perform indirect reasoning tasks that are often encountered in real-world scenarios?
**Methodology**: The authors propose Direct-Indirect Reasoning (DIR), which considers direct and indirect reasoning as parallel paths merged to derive the final answer, stimulating indirect reasoning through prompt templates incorporating contrapositive and contradiction principles where LLMs assume the negation of the conclusion and deduce logical equivalence.
**Key findings**:
- Most existing methods resort to Direct Reasoning and disregard Indirect Reasoning, making LLMs struggle with indirect reasoning tasks
- DIR method can be straightforwardly integrated with existing Chain-of-Thought variants
- When combined with various baseline methods, DIR significantly outperforms all original methods on logical reasoning and mathematical proof datasets
- The approach uses contrapositive and contradiction principles to enhance LLM comprehension of reasoning rules
**Limitations**: Not stated in abstract

## References

Bi, Z., Hajialigol, D., Sun, Z., Hao, J., & Wang, X. (2024). STOC-TOT: Stochastic tree-of-thought with constrained decoding for complex reasoning in multi-hop question answering. arXiv. https://arxiv.org/abs/2407.03687

Jia, S., Wang, X., & Kasiviswanathan, S. P. (2025). Training large language models to reason in parallel with global forking tokens. arXiv. https://arxiv.org/abs/2510.05132

Li, Y., Shi, J., Feng, S., Yuan, P., Wang, X., Zhang, Y., Zhang, J., Tan, C., Pan, B., Hu, Y., & Li, K. (2025). Speculative decoding for multi-sample inference. arXiv. https://arxiv.org/abs/2503.05330

Shalev, Y., Feder, A., & Goldstein, A. (2024). Distributional reasoning in LLMs: Parallel reasoning processes in multi-hop reasoning. arXiv. https://arxiv.org/abs/2406.13858

Shao, C., Hu, X., Lin, Y., & Xu, F. (2025). Division-of-thoughts: Harnessing hybrid language model synergy for efficient on-device agents. arXiv. https://arxiv.org/abs/2502.04392

Tu, S., Li, Y., Bai, Y., Hou, L., & Li, J. (2025). DeepPrune: Parallel scaling without inter-trace redundancy. arXiv. https://arxiv.org/abs/2510.08483

Xu, Z., Qiu, Z., Huang, G., Li, K., Li, S., Zhang, C., Li, K., Yi, Q., Jiang, Y., Zhou, B., Lian, F., & Kang, Z. (2025). Adaptive termination for multi-round parallel reasoning: An universal semantic entropy-guided framework. arXiv. https://arxiv.org/abs/2507.06829

Yu, Y. (2025). Accelerate parallelizable reasoning via parallel decoding within one sequence. arXiv. https://arxiv.org/abs/2503.20533

You, R., Li, Y., Liu, M., Wang, W., Nie, L., & Li, W. (2025). Parallel test-time scaling for latent reasoning models. arXiv. https://arxiv.org/abs/2510.07745

Zhang, Y., Sun, Y., Zhan, Y., Tao, D., Tao, D., & Gong, C. (2024). Large language models as an indirect reasoner: Contrapositive and contradiction for automated reasoning. arXiv. https://arxiv.org/abs/2402.03667
