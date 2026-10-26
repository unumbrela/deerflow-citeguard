# Systematic Literature Review: Code Generation with LLM-based Agents

**Search Parameters:**
- **Category:** cs.SE (Software Engineering)
- **Publication Period:** July 31, 2023 - July 30, 2025
- **Number of Papers:** 10
- **Review Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in code generation using Large Language Model (LLM)-based agents. The reviewed papers span from 2023 to 2025 and focus on multi-agent frameworks, evaluation benchmarks, and novel methodologies for improving code generation quality, security, and scalability. Key themes include multi-agent collaboration, security enhancement, documentation generation, repository-level code generation, and automated evaluation frameworks.

---

## References (APA Format)

1. Ishibashi, Y., & Nishimura, Y. (2024). Self-Organized Agents: A LLM Multi-Agent Framework toward Ultra Large-Scale Code Generation and Optimization. *arXiv preprint arXiv:2404.02183*. https://arxiv.org/abs/2404.02183v1

2. Jain, S., Dora, A., Sam, K. S., & Singh, P. (2024). LLM Agents Improve Semantic Code Search. *arXiv preprint arXiv:2408.11058*. https://arxiv.org/abs/2408.11058v1

3. Li, J., Shi, X., Zhang, K., Li, G., Jin, Z., Li, L., Zhang, H., Li, J., Liu, F., Zhang, Y., Tao, Z., Dong, Y., Zhu, Y., & Tao, C. (2025). GraphCodeAgent: Dual Graph-Guided LLM Agent for Retrieval-Augmented Repo-Level Code Generation. *arXiv preprint arXiv:2504.10046*. https://arxiv.org/abs/2504.10046v2

4. Liu, K., Pan, Y., Xiang, Y., He, D., Li, J., Du, Y., & Gao, T. (2025). ProjectEval: A Benchmark for Programming Agents Automated Evaluation on Project-Level Code Generation. *arXiv preprint arXiv:2503.07010*. https://arxiv.org/abs/2503.07010v2

5. Nunez, A., Islam, N. T., Jha, S. K., & Najafirad, P. (2024). AutoSafeCoder: A Multi-Agent Framework for Securing LLM Code Generation through Static Analysis and Fuzz Testing. *arXiv preprint arXiv:2409.10737*. https://arxiv.org/abs/2409.10737v2

6. Palavalli, M. A., & Santolucito, M. (2024). Using a Feedback Loop for LLM-based Infrastructure as Code Generation. *arXiv preprint arXiv:2411.19043*. https://arxiv.org/abs/2411.19043v1

7. Pan, R., Zhang, H., & Liu, C. (2025). CodeCoR: An LLM-Based Self-Reflective Multi-Agent Framework for Code Generation. *arXiv preprint arXiv:2501.07811*. https://arxiv.org/abs/2501.07811v2

8. Rasheed, Z., Waseem, M., Systä, K., & Abrahamsson, P. (2024). Large Language Model Evaluation Via Multi AI Agents: Preliminary results. *arXiv preprint arXiv:2404.01023*. https://arxiv.org/abs/2404.01023v1

9. Wu, J. J., & Fard, F. H. (2024). HumanEvalComm: Benchmarking the Communication Competence of Code Generation for LLMs and LLM Agent. *arXiv preprint arXiv:2406.00215*. https://arxiv.org/abs/2406.00215v3

10. Yang, D., Simoulin, A., Qian, X., Liu, X., Cao, Y., Teng, Z., & Yang, G. (2025). DocAgent: A Multi-Agent System for Automated Code Documentation Generation. *arXiv preprint arXiv:2504.08725*. https://arxiv.org/abs/2504.08725v3

---

## Thematic Analysis

### 1. Multi-Agent Frameworks for Code Generation

**Self-Organized Agents (SoA)** - Ishibashi & Nishimura (2024)
- Addresses context length limitations in single-agent approaches
- Enables automatic agent multiplication based on problem complexity
- Achieves 5% improvement in Pass@1 accuracy over single-agent baselines on HumanEval
- Each agent maintains constant code management while overall code volume scales indefinitely

**CodeCoR** - Pan, Zhang, & Liu (2025)
- Implements self-reflective multi-agent framework with four specialized agents
- Prunes low-quality intermediate outputs to reduce error propagation
- Achieves 77.13% average Pass@1 score across HumanEval, HumanEval-ET, MBPP, and MBPP-ET
- Outperforms CodeCoT and MapCoder baselines

**AutoSafeCoder** - Nunez, Islam, Jha, & Najafirad (2024)
- Integrates three agents: Coding, Static Analyzer, and Fuzzing
- Combines static analysis with mutation-based fuzzing for security enhancement
- Demonstrates 13% reduction in code vulnerabilities on SecurityEval dataset
- Maintains functionality while improving security

**DocAgent** - Yang et al. (2025)
- Specialized five-agent system: Reader, Searcher, Writer, Verifier, Orchestrator
- Uses topological code processing for incremental context building
- Evaluates documentation on Completeness, Helpfulness, and Truthfulness dimensions
- Significantly outperforms baseline approaches consistently

### 2. Evaluation Benchmarks and Methodologies

**HumanEvalComm** - Wu & Fard (2024)
- Introduces communication competence benchmarking for code generation
- Modifies problem descriptions with inconsistency, ambiguity, and incompleteness
- Proposes Communication Rate and Good Question Rate metrics
- Evaluates Okanagan agent approach against Code LLMs

**ProjectEval** - Liu et al. (2025)
- First benchmark for project-level code generation automated evaluation
- Simulates user interaction for execution evaluation
- Provides three different input levels: natural language or code skeletons
- Identifies systematic engineering, project understanding, and comprehensive analysis as key success factors

**Multi-Agent LLM Evaluation** - Rasheed, Waseem, Systä, & Abrahamsson (2024)
- Eight-agent system for comparative LLM performance assessment
- Evaluates GPT-3.5, GPT-3.5 Turbo, GPT-4, GPT-4 Turbo, Google Bard, LLAMA, and Hugging Face
- Integrates HumanEval benchmark for verification
- GPT-3.5 Turbo showed superior performance in preliminary results

### 3. Repository-Level and Context-Aware Code Generation

**GraphCodeAgent** - Li et al. (2025)
- Dual graph-guided approach for retrieval-augmented code generation
- Constructs Requirement Graph (RG) and Structural-Semantic Code Graph (SSCG)
- Performs multi-hop reasoning for context retrieval
- Significantly outperforms state-of-the-art baselines on DevEval and CoderEval benchmarks
- Bridges gap between natural language requirements and programming implementations

### 4. Specialized Applications

**Semantic Code Search** - Jain, Dora, Sam, & Singh (2024)
- Applies Retrieval Augmented Generation (RAG) powered agents
- Enhances user queries with repository context
- Multi-stream ensemble approach deployed on repo-rift.com
- Achieves 78.2% Success@10 and 34.6% Success@1 on CodeSearchNet dataset

**Infrastructure as Code (IaC)** - Palavalli & Santolucito (2024)
- Investigates feedback loops for LLM-based IaC generation
- Returns errors and warnings for iterative improvement
- Effectiveness decreases exponentially until plateau
- Addresses infrastructure management challenges in software development

---

## Key Findings

### Methodological Trends

1. **Multi-Agent Collaboration Dominance**: 8 out of 10 papers employ multi-agent architectures, indicating a clear shift from single-agent to collaborative approaches.

2. **Iterative Refinement**: Most frameworks incorporate feedback loops, self-reflection, or iterative testing to improve code quality.

3. **Specialization**: Agents are increasingly specialized for distinct tasks (coding, testing, documentation, security analysis).

4. **Context Management**: Novel approaches address context length limitations through agent multiplication, graph-based retrieval, and topological processing.

### Performance Improvements

- **Security**: AutoSafeCoder achieves 13% vulnerability reduction
- **Accuracy**: CodeCoR reaches 77.13% Pass@1; SoA improves by 5% over single-agent
- **Search**: RepoRift achieves 78.2% Success@10 in semantic code search

### Evaluation Challenges

- Existing benchmarks lack project-level automated evaluation capabilities
- Communication competence remains underexplored
- User perspective simulation is emerging as critical evaluation criterion

---

## Research Gaps and Future Directions

1. **Long-term Maintenance**: Limited research on agent-based code maintenance and evolution over time.

2. **Human-Agent Collaboration**: Insufficient exploration of optimal human-agent interaction patterns in professional settings.

3. **Domain-Specific Optimization**: Need for specialized agents targeting specific programming domains (web, embedded systems, data science).

4. **Scalability Testing**: While SoA addresses scalability, real-world ultra-large-scale validation remains limited.

5. **Feedback Loop Optimization**: Palavalli & Santolucito (2024) identify diminishing returns in iterative feedback; optimal iteration strategies require investigation.

6. **Cross-Repository Learning**: Limited exploration of transfer learning across different codebases and repositories.

---

## Conclusion

The literature from 2023-2025 demonstrates rapid advancement in LLM-based agent systems for code generation. Multi-agent frameworks have emerged as the dominant paradigm, addressing limitations of single-agent approaches in security, scalability, and quality assurance. The introduction of specialized benchmarks like HumanEvalComm, ProjectEval, and multi-agent evaluation systems provides more comprehensive assessment capabilities.

Key innovations include graph-guided retrieval for repository-level generation, topological processing for documentation, and integrated security testing through static and dynamic analysis. However, challenges remain in feedback loop optimization, human-agent collaboration patterns, and long-term codebase maintenance.

The field is moving toward more sophisticated, collaborative, and context-aware systems that better approximate professional software engineering practices. Future research should address identified gaps in maintenance, domain specialization, and optimal human-agent interaction models.

---

## Appendix: Paper Summary Table

| Paper | Framework/Benchmark | Key Innovation | Performance Metric | Dataset/Benchmark |
|-------|-------------------|----------------|-------------------|-------------------|
| Nunez et al. (2024) | AutoSafeCoder | Multi-agent security integration | 13% vulnerability reduction | SecurityEval |
| Wu & Fard (2024) | HumanEvalComm | Communication competence benchmarking | Communication Rate, Good Question Rate | HumanEvalComm |
| Yang et al. (2025) | DocAgent | Topological code processing | Completeness, Helpfulness, Truthfulness | Custom evaluation |
| Ishibashi & Nishimura (2024) | SoA | Automatic agent multiplication | 5% Pass@1 improvement | HumanEval |
| Pan et al. (2025) | CodeCoR | Self-reflective pruning | 77.13% Pass@1 | HumanEval, MBPP |
| Rasheed et al. (2024) | Multi-Agent Evaluator | Eight-agent comparative assessment | Comparative performance | HumanEval |
| Li et al. (2025) | GraphCodeAgent | Dual graph-guided retrieval | Outperforms SOTA | DevEval, CoderEval |
| Liu et al. (2025) | ProjectEval | Project-level automated evaluation | User interaction simulation | ProjectEval |
| Jain et al. (2024) | RepoRift | RAG-powered semantic search | 78.2% Success@10 | CodeSearchNet |
| Palavalli & Santolucito (2024) | Feedback Loop IaC | Iterative error-based improvement | Exponential effectiveness decay | Custom IaC tasks |

---

*This systematic literature review was generated on October 26, 2026, covering papers published between July 31, 2023, and July 30, 2025, in the cs.SE (Software Engineering) category.*
