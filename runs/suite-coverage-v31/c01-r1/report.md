# Systematic Literature Review: Parallel Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "parallel reasoning", category cs.CL, published between 2023-10-14 and 2025-10-14
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent papers on parallel reasoning in Large Language Models, revealing a rapidly evolving field focused on improving reasoning efficiency, robustness, and scalability. The surveyed literature demonstrates that parallel reasoning has emerged as a distinct inference paradigm that complements traditional sequential Chain-of-Thought approaches by concurrently exploring multiple reasoning paths before converging on final answers. Key advances include formal taxonomies organizing parallel reasoning techniques, efficiency-focused methods that reduce computational redundancy, and novel training strategies that enable LLMs to generate diverse yet accurate parallel reasoning traces. The field shows strong convergence around the value of semantic entropy for quality assessment and dynamic control, while open questions remain around optimal termination criteria and the balance between parallel exploration and computational cost.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "parallel reasoning", filtered to category cs.CL, published between 2023-10-14 and 2025-10-14. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Formal Taxonomies and Definitions of Parallel Reasoning

A foundational thread across the literature involves establishing clear definitions and taxonomies for parallel reasoning as a distinct paradigm. Wang et al. (2025) provide the most comprehensive treatment, offering a formal definition of parallel reasoning and clarifying its distinction from related concepts like Chain-of-Thought. Their taxonomy organizes advanced techniques into three categories: non-interactive reasoning, interactive reasoning, and efficiency-focused decoding strategies. This formal grounding is crucial for the field's maturation, as it enables researchers to precisely position their contributions and identify gaps in the existing landscape. The survey reveals that parallel reasoning has various application scenarios including solving complex problems and enhancing the reliability of LLM outputs, with core challenges identified and potential directions suggested for future research.

### Theme 2: Efficiency Optimization and Computational Cost Reduction

A dominant theme across multiple papers addresses the computational inefficiency inherent in parallel reasoning approaches. Tu et al. (2025) identify that over 80% of parallel reasoning traces yield identical final answers, representing substantial wasted computation. Their DeepPrune framework achieves token reduction of 65.73%–88.50% compared to conventional consensus sampling while maintaining competitive accuracy within 3 percentage points. Similarly, Yu (2025) proposes decoding multiple tokens per forward pass via a tree-like attention mask within a single sequence, achieving up to nearly 100% speedup in decoding while maintaining answer quality. Li et al. (2025) exploit intrinsic consensus across parallel generation paths using a probabilistic aggregation mechanism to synthesize high-quality draft tokens, achieving substantial improvement in draft acceptance rates on mathematical reasoning benchmarks. Shao et al. (2025) take a different approach with their Division-of-Thoughts framework, leveraging collaboration between locally deployed smaller-scale language models and cloud-based LLMs to reduce reasoning time by 66.12% and API costs by 83.57%.

### Theme 3: Dynamic Control and Termination Criteria

Several papers address the challenge of determining when to terminate parallel reasoning processes efficiently. Xu et al. (2025) introduce semantic entropy as an intrinsic quality metric to assess model responses during collaborative inference, quantifying the semantic diversity of parallel model responses to enable dynamic control and early termination of reasoning traces. Their key insight is that semantic entropy has a strong negative correlation with accuracy, making it suitable for dynamic control of reasoning processes. This addresses a critical limitation they identify: sequential scaling typically relies on arbitrary token budgets for termination, leading to inefficiency or premature cutoff, while parallel scaling often lacks coordination among parallel branches and requires intrusive fine-tuning to perform effectively.

### Theme 4: Training Strategies for Parallel Reasoning

A distinct thread focuses on training methodologies that enable LLMs to generate effective parallel reasoning traces. Jia et al. (2025) treat parallel reasoning as a set-of-next-token-prediction problem and incorporate a set-based global loss into Supervised Fine-Tuning using bipartite matching between global forking tokens and unique reasoning traces. Their Set Supervised Fine-Tuning (SSFT) preserves unique reasoning modes that naive fine-tuning with multiple reasoning traces collapses, and produces emergent global forking tokens that enable diverse yet correct reasoning. They follow this with Global Forking Policy Optimization (GFPO) to leverage these tokens for incentivizing complex reasoning, with models consistently outperforming SFT counterparts with GRPO on math reasoning and execution-based code generation benchmarks.

### Theme 5: Internal Reasoning Processes and Interpretability

Several papers investigate what occurs within LLMs during parallel reasoning, focusing on interpretability and internal mechanisms. Shalev et al. (2024) introduce a novel interpretable analysis of internal multi-hop reasoning processes, demonstrating that prediction for compositional reasoning questions can be modeled using linear transformation between semantic category spaces. Their statistical analyses show that during inference, middle layers of the network generate highly interpretable embeddings representing potential intermediate answers for multi-hop questions, with corresponding subsets of tokens activated in the model's output, implying the existence of parallel reasoning paths. These observations hold true even when the model lacks the necessary knowledge to solve the task.

### Theme 6: Hybrid Reasoning Approaches

A final theme involves combining parallel reasoning with other reasoning paradigms to leverage complementary strengths. Zhang et al. (2024) propose a Direct-Indirect Reasoning (DIR) method that considers Direct Reasoning and Indirect Reasoning as multiple parallel reasoning paths merged to derive the final answer. Their approach stimulates LLMs to implement Indirect Reasoning by crafting prompt templates incorporating contrapositive and contradiction principles. Bi et al. (2024) propose STOC-TOT, a stochastic tree-of-thought reasoning prompting method with constrained decoding for multi-hop question answering that addresses complexities in question types (bridge vs. comparison) and reasoning types (sequential vs. parallel).

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. Multiple papers converge on the finding that parallel reasoning offers significant advantages over purely sequential approaches for complex reasoning tasks (Wang et al., 2025; Xu et al., 2025). There is consensus that computational efficiency is a critical challenge, with multiple independent approaches demonstrating substantial token or time reduction while maintaining accuracy (Tu et al., 2025; Yu, 2025; Li et al., 2025; Shao et al., 2025). The literature also converges on the value of semantic or structural analysis for quality assessment, with both Xu et al. (2025) and Li et al. (2025) independently developing methods that analyze consensus or diversity across parallel traces.

**Disagreements**: The literature shows less direct disagreement, likely because many papers focus on different aspects of parallel reasoning rather than competing claims. However, there is an implicit tension between approaches that focus on training-time modifications (Jia et al., 2025) versus those that focus on inference-time optimizations (Tu et al., 2025; Yu, 2025). The former requires model fine-tuning but may produce more fundamentally capable reasoning systems, while the latter offers immediate applicability to existing models but may be limited by architectural constraints. Additionally, while some papers focus on parallel reasoning within a single model (Yu, 2025; Tu et al., 2025), others advocate for hybrid approaches combining multiple models of different scales (Shao et al., 2025), reflecting different philosophies about the optimal architecture for parallel reasoning systems.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state their limitations in the abstract, suggesting a need for more transparent reporting of constraints and failure modes. Second, while multiple papers address efficiency, there is limited discussion of the trade-offs between parallel exploration breadth and computational cost—what is the optimal number of parallel traces for different task types? Third, the interpretability work by Shalev et al. (2024) raises questions about whether parallel reasoning paths observed in internal representations align with the explicit parallel traces generated by prompting methods—this connection remains unexplored. Fourth, while training methods show promise (Jia et al., 2025), there is limited investigation of how these methods generalize across different reasoning domains beyond mathematics and code generation. Finally, the literature lacks systematic comparison between different parallel reasoning approaches on standardized benchmarks, making it difficult to assess relative merits of competing methods.

## Per-Paper Annotations

### Bi et al. (2024)

**Research question**: How can prompting methods be improved for multi-hop question answering under zero-shot settings given the complexities in question types and reasoning types?
**Methodology**: The authors propose STOC-TOT, a stochastic tree-of-thought reasoning prompting method with constrained decoding for MHQA. They construct a tree-like reasoning structure by prompting the model to break down original questions into smaller sub-questions forming different reasoning paths, prompt the model to provide probability estimation for each reasoning path at each step, and conduct constrained decoding at answer time to generate more grounded answers and reduce hallucination.
**Key findings**:
- STOC-TOT outperforms other reasoning prompts by a significant margin on two MHQA datasets across five large language models.
- The framework addresses complexities in question types (bridge vs. comparison) and reasoning types (sequential vs. parallel).
- Constrained decoding reduces hallucination and generates more grounded answers.
- The stochastic tree-of-thought approach with probability estimation enables fine-grained prompting for zero-shot MHQA settings.
**Limitations**: not stated in abstract

### Jia et al. (2025)

**Research question**: How can LLMs be trained to generate diverse yet accurate parallel reasoning paths for challenging problems where forking tokens are typically deep in the sampling tree?
**Methodology**: The authors treat parallel reasoning as a set-of-next-token-prediction problem and incorporate a set-based global loss into Supervised Fine-Tuning using bipartite matching between global forking tokens and unique reasoning traces. They propose Set Supervised Fine-Tuning (SSFT) to preserve unique reasoning modes and produce emergent global forking tokens, followed by Global Forking Policy Optimization (GFPO) to leverage these tokens for incentivizing complex reasoning.
**Key findings**:
- SSFT preserves unique reasoning modes that naive fine-tuning with multiple reasoning traces collapses.
- SSFT produces emergent global forking tokens that enable diverse yet correct reasoning.
- GFPO leverages maximally steerable tokens to incentivize complex reasoning.
- Models trained with this method consistently outperform SFT counterparts with GRPO on math reasoning and execution-based code generation benchmarks.
**Limitations**: not stated in abstract

### Li et al. (2025)

**Research question**: How can speculative decoding be improved for multi-sample reasoning scenarios such as self-consistency and Best-of-N sampling?
**Methodology**: The authors propose a novel speculative decoding method that exploits intrinsic consensus across parallel generation paths using a probabilistic aggregation mechanism to synthesize high-quality draft tokens without auxiliary models or external databases. The method dynamically analyzes structural patterns across parallel reasoning paths to identify consensus token sequences that align with the decoding distribution.
**Key findings**:
- The proposed method achieves substantial improvement in draft acceptance rates over baselines on mathematical reasoning benchmarks.
- The approach reduces latency in draft token construction compared to existing methods.
- The method enables seamless integration of speculative decoding with sampling-based reasoning techniques.
- The probabilistic aggregation mechanism successfully identifies consensus token sequences without requiring auxiliary models.
**Limitations**: not stated in abstract

### Shalev et al. (2024)

**Research question**: What processes occur within the hidden layers of LLMs during multi-hop reasoning when no explicit thought process is documented?
**Methodology**: The paper introduces a novel interpretable analysis of internal multi-hop reasoning processes, demonstrating that prediction for compositional reasoning questions can be modeled using linear transformation between semantic category spaces, with statistical analyses showing parallel reasoning paths.
**Key findings**:
- The prediction process for compositional reasoning questions can be modeled using a simple linear transformation between two semantic category spaces.
- During inference, middle layers of the network generate highly interpretable embeddings representing potential intermediate answers for multi-hop questions.
- Statistical analyses show that a corresponding subset of tokens is activated in the model's output, implying the existence of parallel reasoning paths.
- These observations hold true even when the model lacks the necessary knowledge to solve the task.
**Limitations**: not stated in abstract

### Shao et al. (2025)

**Research question**: How can on-device AI assistants leverage hybrid language model collaboration to reduce costs while maintaining competitive reasoning accuracy for complex online tasks?
**Methodology**: The authors propose Division-of-Thoughts (DoT), a collaborative reasoning framework leveraging synergy between locally deployed Smaller-scale Language Models and cloud-based LLMs. DoT uses a Task Decomposer to decompose user queries into smaller sub-tasks, a Task Scheduler to analyze pair-wise dependencies and create dependency graphs for parallel reasoning, and a Plug-and-Play Adapter attached to the SLM for task allocation based on sub-task difficulty using self-reinforced training.
**Key findings**:
- DoT reduces average reasoning time by 66.12% compared to baseline methods.
- DoT reduces API costs by 83.57% while maintaining competitive reasoning accuracy.
- The self-reinforced training method for the adapter relies solely on task execution feedback without altering SLM parameters.
- The framework achieves comparable reasoning accuracy with the best baseline methods while significantly reducing costs.
**Limitations**: not stated in abstract

### Tu et al. (2025)

**Research question**: How can we address the computational inefficiency caused by inter-trace redundancy in parallel scaling for Large Language Models?
**Methodology**: The paper proposes DeepPrune, a framework featuring a specialized judge model trained with out-of-distribution data using oversampling techniques to predict answer equivalence from partial reasoning traces, combined with an online greedy clustering algorithm for dynamic pruning of redundant paths.
**Key findings**:
- Over 80% of parallel reasoning traces yield identical final answers, representing substantial wasted computation.
- DeepPrune achieves 0.7072 AUROC on unseen reasoning models for predicting answer equivalence from partial traces.
- DeepPrune achieves token reduction of 65.73%--88.50% compared to conventional consensus sampling.
- The framework maintains competitive accuracy within 3 percentage points while significantly reducing computational cost.
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: What are the current progress, techniques, applications, and challenges of parallel reasoning in Large Language Models?
**Methodology**: The paper conducts a comprehensive survey of parallel reasoning literature, presenting a formal definition and a novel taxonomy to organize advanced techniques into non-interactive reasoning, interactive reasoning, and efficiency-focused decoding strategies.
**Key findings**:
- Parallel reasoning has emerged as a new inference paradigm that enhances reasoning robustness by concurrently exploring multiple lines of thought before converging on a final answer.
- The paper provides a formal definition of parallel reasoning and clarifies its distinction from related concepts like Chain-of-Thought.
- Advanced techniques are organized into three categories: non-interactive reasoning, interactive reasoning, and efficiency-focused decoding strategies.
- Parallel reasoning has various application scenarios including solving complex problems and enhancing the reliability of LLM outputs.
- Core challenges of parallel reasoning are identified with potential directions suggested for future research.
**Limitations**: not stated in abstract

### Xu et al. (2025)

**Research question**: How can we design a flexible test-time collaborative inference framework that exploits the complementary strengths of sequential and parallel reasoning paradigms with efficient dynamic control and early termination?
**Methodology**: The paper introduces semantic entropy (SE) as an intrinsic quality metric to assess model responses during collaborative inference, quantifying the semantic diversity of parallel model responses to enable dynamic control and early termination of reasoning traces.
**Key findings**:
- Sequential scaling typically relies on arbitrary token budgets for termination, leading to inefficiency or premature cutoff.
- Parallel scaling often lacks coordination among parallel branches and requires intrusive fine-tuning to perform effectively.
- Semantic entropy quantifies the semantic diversity of parallel model responses and serves as a robust indicator of reasoning quality.
- Semantic entropy has a strong negative correlation with accuracy, making it suitable for dynamic control of reasoning processes.
**Limitations**: not stated in abstract

### Yu (2025)

**Research question**: How can we accelerate the reasoning process in LLMs by leveraging the inherent parallelizability of certain tasks?
**Methodology**: The paper proposes decoding multiple tokens per forward pass via a tree-like attention mask within a single sequence when multiple parallel reasoning steps exist, avoiding additional memory usage.
**Key findings**:
- Generating lengthy reasoning sequences is computationally expensive and time-consuming.
- The method leverages inherent parallelizability of certain tasks to accelerate reasoning processes.
- The approach achieves up to nearly 100% speedup in decoding.
- The method maintains answer quality while achieving significant speedup.
**Limitations**: not stated in abstract

### Zhang et al. (2024)

**Research question**: How can Large Language Models be improved to perform Indirect Reasoning tasks that are often encountered in real-world scenarios but overlooked by existing methods?
**Methodology**: The authors propose a Direct-Indirect Reasoning (DIR) method that considers Direct Reasoning and Indirect Reasoning as multiple parallel reasoning paths merged to derive the final answer. They stimulate LLMs to implement Indirect Reasoning by crafting prompt templates incorporating contrapositive and contradiction principles, triggering LLMs to assume the negation of the conclusion as true and combine it with premises to deduce a conclusion.
**Key findings**:
- The DIR method significantly outperforms original baseline methods when combined with various CoT variants on logical reasoning and mathematic proof datasets.
- Most existing methods resort to Direct Reasoning and disregard Indirect Reasoning, making LLMs difficult to solve IR tasks.
- The DIR method is simple yet effective and can be straightforwardly integrated with existing CoT method variants.
- Prompt templates incorporating contrapositive and contradiction principles enhance LLMs' comprehension of rules used in reasoning processes.
**Limitations**: not stated in abstract

## References

Bi, Z., Hajialigol, D., Sun, Z., Hao, J., & Wang, X. (2024). STOC-TOT: Stochastic tree-of-thought with constrained decoding for complex reasoning in multi-hop question answering. arXiv. https://arxiv.org/abs/2407.03687

Jia, S., Wang, X., & Kasiviswanathan, S. P. (2025). Training large language models to reason in parallel with global forking tokens. arXiv. https://arxiv.org/abs/2510.05132

Li, Y., Shi, J., Feng, S., Yuan, P., Wang, X., Zhang, Y., Zhang, J., Tan, C., Pan, B., Hu, Y., & Li, K. (2025). Speculative decoding for multi-sample inference. arXiv. https://arxiv.org/abs/2503.05330

Shalev, Y., Feder, A., & Goldstein, A. (2024). Distributional reasoning in LLMs: Parallel reasoning processes in multi-hop reasoning. arXiv. https://arxiv.org/abs/2406.13858

Shao, C., Hu, X., Lin, Y., & Xu, F. (2025). Division-of-thoughts: Harnessing hybrid language model synergy for efficient on-device agents. arXiv. https://arxiv.org/abs/2502.04392

Tu, S., Li, Y., Bai, Y., Hou, L., & Li, J. (2025). DeepPrune: Parallel scaling without inter-trace redundancy. arXiv. https://arxiv.org/abs/2510.08483

Wang, Z., Niu, B., Gao, Z., Zheng, Z., Xu, T., Meng, L., Li, Z., Liu, J., Chen, Y., Zhu, C., Wu, H., Wang, H., & Chen, E. (2025). A survey on parallel reasoning. arXiv. https://arxiv.org/abs/2510.12164

Xu, Z., Qiu, Z., Huang, G., Li, K., Li, S., Zhang, C., Li, K., Yi, Q., Jiang, Y., Zhou, B., Lian, F., & Kang, Z. (2025). Adaptive termination for multi-round parallel reasoning: An universal semantic entropy-guided framework. arXiv. https://arxiv.org/abs/2507.06829

Yu, Y. (2025). Accelerate parallelizable reasoning via parallel decoding within one sequence. arXiv. https://arxiv.org/abs/2503.20533

Zhang, Y., Sun, Y., Zhan, Y., Tao, D., Tao, D., & Gong, C. (2024). Large language models as an indirect reasoner: Contrapositive and contradiction for automated reasoning. arXiv. https://arxiv.org/abs/2402.03667
