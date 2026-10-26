# Systematic Literature Review: Root Cause Analysis in Software Engineering

**Search Parameters:**
- **Category:** cs.SE (Software Engineering)
- **Publication Period:** October 22, 2023 – October 22, 2025
- **Number of Papers:** 10
- **Retrieval Date:** October 26, 2026

---

## References (APA Format)

1. Demarne, M., Cilimdzic, M., Falkowski, T., Johnson, T., Gramling, J., Kuang, W., Hou, H., Aryan, A., Subramaniam, G., Lee, K., Mejia, M., Liu, L., & Vermareddy, D. (2024). Automated root cause analysis system for complex data products. *arXiv*. https://arxiv.org/abs/2412.15374

2. Fang, A., Yang, H., Dong, H., Lu, Q., Xu, J., & He, P. (2025). A goal-driven survey on root cause analysis. *arXiv*. https://arxiv.org/abs/2510.19593

3. Feng, S., Ye, Y., Shi, Q., Cheng, Z., Xu, X., Cheng, S., Choi, H., & Zhang, X. (2024). ROCAS: Root cause analysis of autonomous driving accidents via cyber-physical co-mutation. *arXiv*. https://arxiv.org/abs/2409.07774

4. Huang, J., Chen, P., Yu, G., Wang, Y., Huang, H., & He, Z. (2024). FaaSRCA: Full lifecycle root cause analysis for serverless applications. *arXiv*. https://arxiv.org/abs/2412.02239

5. Li, Y., Wu, Y., Liu, J., Jiang, Z., Chen, Z., Yu, G., & Lyu, M. R. (2025). COCA: Generative root cause analysis for distributed systems with code knowledge. *arXiv*. https://arxiv.org/abs/2503.23051

6. Pham, L., Ha, H., & Zhang, H. (2024). BARO: Robust root cause analysis for microservices via multivariate Bayesian online change point detection. *arXiv*. https://arxiv.org/abs/2405.09330

7. Pham, L., Ha, H., Zhang, H., Salim, F., & Zhang, X. (2024). RCAEval: A benchmark for root cause analysis of microservice systems with telemetry data. *arXiv*. https://arxiv.org/abs/2412.17015

8. Pham, L., Ha, H., & Zhang, H. (2024). Root cause analysis for microservice system based on causal inference: How far are we? *arXiv*. https://arxiv.org/abs/2408.13729

9. Tonon, A., Zhang, M., Caglayan, B., Shen, F., Gui, T., Wang, M., & Zhou, R. (2025). RADICE: Causal graph based root cause analysis for system performance diagnostic. *arXiv*. https://arxiv.org/abs/2501.11545

10. Wang, T., & Qi, G. (2024). A comprehensive survey on root cause analysis in (micro) services: Methodologies, challenges, and trends. *arXiv*. https://arxiv.org/abs/2408.00803

---

## Thematic Analysis

### Survey Papers (2 papers)

**Fang et al. (2025)** present a goal-driven framework categorizing 135 RCA papers from 2014-2025 based on their underlying objectives rather than input data types. This work addresses a critical gap in previous surveys that grouped disparate objectives together, obscuring true progress. The authors argue that RCA tasks with different goals (e.g., localizing faulty services vs. identifying specific bugs) require fundamentally different approaches.

**Wang & Qi (2024)** provide a comprehensive structured review of RCA techniques in microservices, covering methodologies using metrics, traces, logs, and multi-modal data. The survey positions itself at the forefront of AI and automation advancements, offering guidance for future research directions in this rapidly evolving field.

### Causal Inference Approaches (3 papers)

**Pham et al. (2024)** conducted a comprehensive evaluation of nine causal discovery methods and twenty-one RCA methods for microservice systems. Their findings reveal that no single method excels in all situations, with each showing limitations in effectiveness, efficiency, or parameter sensitivity. Notably, performance on synthetic datasets does not reliably predict real-system performance.

**Pham et al. (2024)** introduced BARO, an end-to-end approach integrating anomaly detection and root cause analysis using Multivariate Bayesian Online Change Point Detection. BARO demonstrates robustness to inaccurate anomaly detection results, outperforming state-of-the-art approaches across three benchmark microservice systems.

**Tonon et al. (2025)** proposed RADICE, a causal graph-based algorithm that allows domain experts to contribute partial knowledge through a novel causal domain knowledge model. The algorithm performs causal graph discovery, enhancement, refinement, and subtraction to output root cause causal sub-graphs, showing superior results over baseline methods.

### Specialized Domain Applications (3 papers)

**Feng et al. (2024)** addressed RCA for autonomous driving systems (ADS) with ROCAS, featuring cyber-physical co-mutation. Existing CPS techniques designed for drones cannot handle ADS's complex physical environments and deep learning models. ROCAS precisely identifies accident-trigger entities and pinpoints misconfigurations through differential analysis.

**Huang et al. (2024)** developed FaaSRCA for serverless applications, addressing their highly dynamic nature and short lifecycles. Unlike microservice RCA methods, FaaSRCA integrates multi-modal observability data using Global Call Graph and Graph Attention Networks, achieving top-k precision improvements of 21.25% to 81.63%.

**Demarne et al. (2024)** presented ARCAS, a diagnostic platform using a Domain Specific Language for fast implementation of automated troubleshooting guides. The system employs LLMs to prioritize outputs and take appropriate actions, successfully deployed across Azure Synapse Analytics and Microsoft Fabric.

### Code-Enhanced and Benchmark Contributions (2 papers)

**Li et al. (2025)** proposed COCA, leveraging code knowledge to enhance RCA for distributed systems when comprehensive monitoring data is unavailable. By extracting relevant code snippets and reconstructing execution paths, COCA achieves 28.3% improvement in root cause localization and 22.0% improvement in summarization across five real-world systems.

**Pham et al. (2024)** introduced RCAEval, an open-source benchmark providing three comprehensive datasets with 735 failure cases and an evaluation framework with fifteen reproducible baselines. This addresses the critical gap of lacking standard benchmarks for RCA research in microservice systems.

---

## Key Findings and Trends

1. **Goal-Driven Categorization:** The field is moving toward understanding RCA tasks based on their underlying goals rather than input data types, recognizing that different objectives require fundamentally different approaches.

2. **Causal Inference Dominance:** Causal inference methods remain prominent, though evaluations reveal significant limitations in current approaches, particularly regarding synthetic vs. real-world performance gaps.

3. **Domain Specialization:** RCA techniques are increasingly specialized for specific domains (serverless, autonomous driving, data products), reflecting the unique challenges each presents.

4. **LLM Integration:** Recent work incorporates Large Language Models for prioritization, summarization, and code knowledge extraction, representing a shift toward generative approaches.

5. **Benchmark Standardization:** The introduction of comprehensive benchmarks like RCAEval addresses a critical gap in the field, enabling more rigorous comparison of approaches.

6. **Full-Lifecycle Consideration:** Modern approaches consider entire application lifecycles rather than just runtime stages, particularly important for serverless and dynamic systems.

---

## Research Gaps and Future Directions

Based on this systematic review, several gaps emerge:

- **Real-World Validation:** Many methods perform well on synthetic data but struggle in production environments
- **Goal-Aware Methods:** Need for RCA techniques explicitly designed for specific goals (triage vs. definitive fix)
- **Partial Knowledge Handling:** Approaches that work with incomplete monitoring data or partial domain knowledge
- **Cross-Domain Transferability:** Limited generalizability of domain-specific solutions
- **Standardized Evaluation:** While RCAEval is a step forward, broader adoption and expansion are needed

---

## Conclusion

This systematic literature review reveals a field in transition, moving from generic RCA approaches toward goal-driven, domain-specialized, and causally-grounded methods. The integration of LLMs and the development of comprehensive benchmarks represent significant advances. However, substantial gaps remain between synthetic evaluations and real-world performance, highlighting the need for more robust, goal-aware approaches that can handle the complexity of modern distributed systems.

---

**Sources:**

All papers retrieved from arXiv primary category cs.SE (Software Engineering), published between October 22, 2023, and October 22, 2025.
