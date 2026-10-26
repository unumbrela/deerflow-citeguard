# Systematic Literature Review: Code Generation with LLM-based Agents

**Review Period:** July 31, 2023 – July 30, 2025  
**Category:** cs.SE (Software Engineering)  
**Total Papers Reviewed:** 10  
**Review Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in LLM-based multi-agent frameworks for code generation. The reviewed literature reveals a clear evolution from single-agent code generation toward sophisticated multi-agent systems that incorporate security analysis, self-reflection, iterative refinement, and domain-specific verification. Key themes include security-enhanced code generation, complexity-aware feedback mechanisms, communication competence for requirement clarification, and scalable architectures for large-scale code production.

---

## References (APA Format)

Ishibashi, Y., & Nishimura, Y. (2024). Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization. *arXiv preprint arXiv:2404.02183*. https://arxiv.org/abs/2404.02183v1

Jin, H., Huang, L., Cai, H., Yan, J., Li, B., & Chen, H. (2024). From LLMs to LLM-based Agents for Software Engineering: A Survey of Current, Challenges and Future. *arXiv preprint arXiv:2408.02479*. https://arxiv.org/abs/2408.02479v2

Jin, H., Sun, Z., & Chen, H. (2024). RGD: Multi-LLM Based Agent Debugger via Refinement and Generation Guidance. *arXiv preprint arXiv:2410.01242*. https://arxiv.org/abs/2410.01242v2

Liu, Z., Zeng, R., Wang, D., Peng, G., Wang, J., Liu, Q., Liu, P., & Wang, W. (2024). Agents4PLC: Automating Closed-loop PLC Code Generation and Verification in Industrial Control Systems using LLM-based Agents. *arXiv preprint arXiv:2410.14209*. https://arxiv.org/abs/2410.14209v2

Nunez, A., Islam, N. T., Jha, S. K., & Najafirad, P. (2024). AutoSafeCoder: A Multi-Agent Framework for Securing LLM Code Generation through Static Analysis and Fuzz Testing. *arXiv preprint arXiv:2409.10737*. https://arxiv.org/abs/2409.10737v2

Pan, R., Zhang, H., & Liu, C. (2025). CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation. *arXiv preprint arXiv:2501.07811*. https://arxiv.org/abs/2501.07811v2

Sepidband, M., Taherkhani, H., Wang, S., & Hemmati, H. (2025). Enhancing LLM-Based Code Generation with Complexity Metrics: A Feedback-Driven Approach. *arXiv preprint arXiv:2505.23953*. https://arxiv.org/abs/2505.23953v1

Wang, J., Cao, L., Luo, X., Cao, Y., Li, Z., Xiao, Y., Zhao, M., Jatowt, A., & Cai, Y. (2024). Toward Secure Code Generation: Bridging Correctness and Security via Task-Adaptive Vulnerability Modeling and Execution-Based Benchmarking. *arXiv preprint arXiv:2407.02395*. https://arxiv.org/abs/2407.02395v3

Wang, X., Gao, P., Peng, C., Hu, R., & Gao, C. (2025). CodeVisionary: An Agent-based Framework for Evaluating Large Language Models in Code Generation. *arXiv preprint arXiv:2504.13472*. https://arxiv.org/abs/2504.13472v2

Wu, J. J. W., & Fard, F. H. (2024). HumanEvalComm: Benchmarking the Communication Competence of Code Generation for LLMs and LLM Agent. *arXiv preprint arXiv:2406.00215*. https://arxiv.org/abs/2406.00215v3

---

## Thematic Analysis

### 1. Security-Enhanced Code Generation

**AutoSafeCoder** (Nunez et al., 2024) introduces a three-agent framework integrating static analysis and fuzz testing during code generation. The Coding Agent, Static Analyzer Agent, and Fuzzing Agent collaborate iteratively, achieving a 13% reduction in vulnerabilities on the SecurityEval dataset without compromising functionality.

**SecAwareCoder** (Wang et al., 2024) addresses the security-correctness gap through task-adaptive threat modeling and constraint-aware code generation. The framework introduces CodeSecEval, an execution-based benchmark with 255 Python tasks spanning 77 CWE categories, enabling precise evaluation of secure code generation.

### 2. Self-Reflective Multi-Agent Architectures

**CodeCoR** (Pan et al., 2025) implements a four-agent system with pruning mechanisms to reduce error propagation. Agents generate prompts, code, test cases, and repair advice, with low-quality outputs pruned at each stage. The framework achieves 77.13% average Pass@1 across HumanEval, HumanEval-ET, MBPP, and MBPP-ET datasets, outperforming CodeCoT and MapCoder baselines.

**RGD** (Jin et al., 2024) decomposes code generation into iterative refinement steps using three agents: Guide Agent, Debug Agent, and Feedback Agent. This approach achieves state-of-the-art performance with 9.8% improvement on HumanEval and 16.2% on MBPP compared to traditional prompting methods.

### 3. Scalability and Large-Scale Code Production

**Self-Organized Agents (SoA)** (Ishibashi & Nishimura, 2024) addresses context-length limitations through dynamic agent multiplication based on problem complexity. Each agent manages constant code volume while the overall codebase scales indefinitely. SoA surpasses single-agent baselines by 5% in Pass@1 accuracy on HumanEval.

### 4. Domain-Specific Applications

**Agents4PLC** (Liu et al., 2024) targets industrial control systems with specialized PLC code generation and verification. The framework incorporates Retrieval-Augmented Generation (RAG), advanced prompt engineering, and Chain-of-Thought strategies, establishing a comprehensive benchmark for verifiable PLC code generation.

### 5. Complexity-Aware Feedback Mechanisms

**Complexity Metrics Approach** (Sepidband et al., 2025) investigates correlations between code complexity metrics and LLM success rates. Using logistic regression, the study identifies predictive complexity metrics and implements iterative feedback based on failed outputs. The approach achieves 35.71% Pass@1 improvement on HumanEval with GPT-3.5 Turbo, compared to 12.5% baseline improvement.

### 6. Communication Competence and Requirement Clarification

**HumanEvalComm** (Wu & Fard, 2024) introduces communication skills evaluation for code generation, defining the ability to ask clarifying questions when problem descriptions contain inconsistencies, ambiguities, or incompleteness. New metrics include Communication Rate and Good Question Rate, tested with the Okanagan agent approach.

### 7. Evaluation Frameworks

**CodeVisionary** (Wang et al., 2025) proposes the first agent-based evaluation framework for complex code generation with two stages: requirement-guided multi-dimensional context distillation and fine-grained scoring with summarization. Validated on 363 samples across 37 coding scenarios and 23 programming languages, it outperforms baselines with average improvements of 0.217 (Pearson), 0.163 (Spearman), and 0.141 (Kendall-Tau) correlation coefficients.

### 8. Comprehensive Surveys

**Survey of LLM-based Agents in SE** (Jin et al., 2024) differentiates between LLMs and LLM-based agents across six software engineering topics: requirement engineering, code generation, autonomous decision-making, software design, test generation, and software maintenance. The survey provides comprehensive analysis of models, benchmarks, and evaluation metrics, highlighting the need for unified standards in qualifying LLM solutions as agent-based systems.

---

## Key Findings

1. **Multi-agent frameworks consistently outperform single-agent approaches** across all reviewed studies, with improvements ranging from 5% to 16.2% on standard benchmarks.

2. **Security integration during generation** (not post-hoc) significantly reduces vulnerabilities while maintaining functional correctness.

3. **Iterative refinement with self-reflection** proves more effective than sequential workflows, particularly when low-quality outputs are pruned at each stage.

4. **Dynamic scalability** through agent multiplication addresses context-length limitations for large-scale code production.

5. **Domain-specific adaptations** (e.g., PLC programming) require specialized benchmarks and verification mechanisms beyond general-purpose code generation.

6. **Complexity metrics provide predictive signals** for code correctness and enable targeted feedback for failed generation attempts.

7. **Communication competence** remains underexplored but critical for bridging the gap between LLMs and top-tier software engineering practices.

8. **Evaluation methodologies are evolving** from simple Pass@1 metrics toward multi-dimensional, explainable assessment frameworks.

---

## Research Gaps and Future Directions

1. **Unified benchmarking standards** for LLM-based agents in software engineering remain absent, complicating cross-study comparisons.

2. **Long-term maintenance and evolution** of agent-generated code receives limited attention in current literature.

3. **Human-agent collaboration patterns** warrant deeper investigation, particularly for industrial adoption scenarios.

4. **Energy efficiency and computational costs** of multi-agent frameworks are rarely analyzed despite practical deployment implications.

5. **Cross-language generalization** of agent frameworks requires further validation beyond Python-centric benchmarks.

---

## Conclusion

The literature from 2023-2025 demonstrates rapid maturation of LLM-based multi-agent frameworks for code generation. The field has progressed beyond simple prompt engineering toward sophisticated architectures incorporating security analysis, self-reflection, complexity awareness, and domain-specific verification. Future research should address benchmarking standardization, human-agent collaboration, and practical deployment considerations to realize the full potential of autonomous code generation systems.

---

**Generated:** October 26, 2026  
**Format:** APA 7th Edition  
**Search Window:** July 31, 2023 – July 30, 2025  
**Category:** cs.SE (Software Engineering)  
**Total Papers:** 10
