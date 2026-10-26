# A Goal-Driven Survey on Root Cause Analysis: Systematic Literature Review

**Search Parameters:**
- **Category:** cs.SE (Software Engineering)
- **Publication Period:** October 22, 2023 – October 21, 2025
- **Total Papers:** 10

---

## Annotated Bibliography (APA Format)

### 1. Causal Inference Methods for Microservices

Pham, L., Ha, H., & Zhang, H. (2024). Root cause analysis for microservice system based on causal inference: How far are we? *arXiv preprint arXiv:2408.13729*. https://arxiv.org/abs/2408.13729v2

**Summary:** This paper presents a comprehensive evaluation of nine causal discovery methods and twenty-one root cause analysis methods for microservice systems. The authors found that no single method excels across all situations, with each approach showing limitations in effectiveness, efficiency, or parameter sensitivity. Notably, performance on synthetic datasets does not accurately reflect real-world performance, indicating significant room for improvement in causal inference-based RCA techniques.

**Key Contributions:** Systematic evaluation framework, identification of gaps between synthetic and real-world performance, recommendations for future research directions.

---

### 2. Integrated Anomaly Detection and RCA

Pham, L., Ha, H., & Zhang, H. (2024). BARO: Robust root cause analysis for microservices via multivariate Bayesian online change point detection. *arXiv preprint arXiv:2405.09330*. https://arxiv.org/abs/2405.09330v1

**Summary:** BARO addresses the challenge that existing RCA methods depend on accurate anomaly detection, which is not guaranteed. The approach integrates anomaly detection and root cause analysis using Multivariate Bayesian Online Change Point Detection to model dependencies in multivariate time-series metrics. A novel nonparametric statistical hypothesis testing technique enables robust root cause identification that is less sensitive to anomaly detection accuracy.

**Key Contributions:** End-to-end pipeline integrating anomaly detection with RCA, reduced sensitivity to detection accuracy, demonstrated superiority over state-of-the-art approaches on three benchmark systems.

---

### 3. Causal Graph-Based System Diagnostics

Tonon, A., Zhang, M., Caglayan, B., Shen, F., Gui, T., Wang, M., & Zhou, R. (2025). RADICE: Causal graph based root cause analysis for system performance diagnostic. *arXiv preprint arXiv:2501.11545*. https://arxiv.org/abs/2501.11545v1

**Summary:** RADICE introduces a novel causal domain knowledge model that allows domain experts to contribute partial knowledge for RCA. The algorithm performs causal graph discovery, enhancement, refinement, and subtraction to output a root cause causal sub-graph showing relationships between affected system components. This approach overcomes limitations of correlation-based methods and systems requiring full domain expertise.

**Key Contributions:** Partial domain knowledge integration, causal graph refinement processes, superior performance over baseline causal discovery and correlation-based approaches.

---

### 4. Serverless Application RCA

Huang, J., Chen, P., Yu, G., Wang, Y., Huang, H., & He, Z. (2024). FaaSRCA: Full lifecycle root cause analysis for serverless applications. *arXiv preprint arXiv:2412.02239*. https://arxiv.org/abs/2412.02239v1

**Summary:** FaaSRCA addresses the unique challenges of serverless applications, which exhibit highly dynamic behavior with short lifecycles and instantaneous pulse-like data. Unlike existing microservice RCA methods, FaaSRCA covers the entire lifecycle of serverless functions using multi-modal observability data integrated through a Global Call Graph. A Graph Attention Network-based auto-encoder computes reconstruction scores to determine root causes at lifecycle stage granularity.

**Key Contributions:** Full lifecycle coverage for serverless, multi-modal data integration, 21.25% to 81.63% top-k precision improvement over baselines.

---

### 5. Autonomous Driving Accident Analysis

Feng, S., Ye, Y., Shi, Q., Cheng, Z., Xu, X., Cheng, S., Choi, H., & Zhang, X. (2024). ROCAS: Root cause analysis of autonomous driving accidents via cyber-physical co-mutation. *arXiv preprint arXiv:2409.07774*. https://arxiv.org/abs/2409.07774v2

**Summary:** ROCAS fills a critical gap in post-accident analysis for autonomous driving systems (ADS). Existing cyber-physical system RCA techniques designed for drones cannot handle the complex physical environments and deep learning models in ADS. The framework features cyber-physical co-mutation to precisely identify accident-trigger entities and pinpoint ADS misconfigurations, with differential analysis to reduce search space.

**Key Contributions:** Formal definition of ADS RCA problem, cyber-physical co-mutation technique, demonstrated effectiveness across 12 accident categories with detailed case studies.

---

### 6. Code-Enhanced Generative RCA

Li, Y., Wu, Y., Liu, J., Jiang, Z., Chen, Z., Yu, G., & Lyu, M. R. (2025). COCA: Generative root cause analysis for distributed systems with code knowledge. *arXiv preprint arXiv:2503.23051*. https://arxiv.org/abs/2503.23051v1

**Summary:** COCA addresses the limitation that prevailing RCA approaches require comprehensive runtime monitoring data, often unavailable in issue platforms like GitHub or JIRA. The approach extracts relevant code snippets and reconstructs execution paths to supplement data-limited issue reports. By combining historical issue reports with profiled code knowledge, COCA enables LLMs to generate detailed root cause summaries and localize responsible components.

**Key Contributions:** Code knowledge extraction for data-limited scenarios, 28.3% improvement in root cause localization, 22.0% improvement in summarization, robust generalizability across various LLMs.

---

### 7. Comprehensive Microservices RCA Survey

Wang, T., & Qi, G. (2024). A comprehensive survey on root cause analysis in (micro) services: Methodologies, challenges, and trends. *arXiv preprint arXiv:2408.00803*. https://arxiv.org/abs/2408.00803v1

**Summary:** This survey provides a structured review of RCA techniques within microservices, exploring methodologies that include metrics, traces, logs, and multi-model data. The authors examine the complex dependencies and propagative faults inherent in microservices architectures and discuss methodologies, challenges, and future trends. Positioned at the forefront of AI and automation advancements, it offers guidance for future research directions.

**Key Contributions:** Comprehensive taxonomy of RCA methodologies, identification of key challenges in microservice RCA, roadmap for future research integrating AI and automation.

---

### 8. DSL-Based Automated RCA Platform

Demarne, M., Cilimdzic, M., Falkowski, T., Johnson, T., Gramling, J., Kuang, W., Hou, H., Aryan, A., Subramaniam, G., Lee, K., Mejia, M., Liu, L., & Vermareddy, D. (2024). Automated root cause analysis system for complex data products. *arXiv preprint arXiv:2412.15374*. https://arxiv.org/abs/2412.15374v1

**Summary:** ARCAS presents a diagnostic platform based on a Domain Specific Language (DSL) designed for fast diagnostic implementation with a low learning curve. The system comprises automated troubleshooting guides (Auto-TSGs) that execute in parallel to detect issues using product telemetry and apply near-real-time mitigation. An LLM prioritizes Auto-TSG outputs, reducing the need to understand general system behavior and contrasting with monitoring-focused platforms like Datadog and New Relic.

**Key Contributions:** DSL for rapid diagnostic development, parallel Auto-TSG execution, LLM-based prioritization, successful deployment across Azure Synapse Analytics and Microsoft Fabric.

---

### 9. Standardized RCA Benchmark

Pham, L., Zhang, H., Ha, H., Salim, F., & Zhang, X. (2024). RCAEval: A benchmark for root cause analysis of microservice systems with telemetry data. *arXiv preprint arXiv:2412.17015*. https://arxiv.org/abs/2412.17015v5

**Summary:** RCAEval addresses the absence of standard benchmarks for microservice RCA by providing an open-source benchmark with large-scale datasets and comprehensive evaluation environments. The benchmark includes three datasets comprising 735 failure cases from three microservice systems, covering various real-world fault types. A comprehensive evaluation framework includes fifteen reproducible baselines covering diverse RCA approaches for both coarse-grained and fine-grained evaluation.

**Key Contributions:** First standardized large-scale RCA benchmark, 735 real-world failure cases, fifteen reproducible baselines, ready-to-use evaluation framework for researchers and practitioners.

---

### 10. LLM-Based Agents for RCA

Roy, D., Zhang, X., Bhave, R., Bansal, C., Las-Casas, P., Fonseca, R., & Rajmohan, S. (2024). Exploring LLM-based agents for root cause analysis. *arXiv preprint arXiv:2403.04123*. https://arxiv.org/abs/2403.04123v1

**Summary:** This work explores LLM-based agents for RCA to address the limitation that existing approaches cannot dynamically collect additional diagnostic information. A ReAct agent equipped with retrieval tools was evaluated on production incidents from Microsoft, showing competitive performance with strong baselines but significantly higher factual accuracy. A case study equipped the agent with external diagnostic service tools, demonstrating practical considerations for implementing such systems.

**Key Contributions:** ReAct agent with retrieval tools for RCA, increased factual accuracy over baselines, integration with external diagnostic services, practical implementation insights from Microsoft deployment.

---

## Thematic Analysis

### Research Trends (2023-2025)

**1. Causal Inference Dominance**
Four papers (Pham et al., 2024a; Pham et al., 2024b; Tonon et al., 2025; Wang & Qi, 2024) emphasize causal inference methods, reflecting a shift from correlation-based to causation-based approaches. The recognition that correlation does not imply causation has driven development of causal graph discovery and Bayesian methods.

**2. LLM Integration**
Three papers (Li et al., 2025; Demarne et al., 2024; Roy et al., 2024) leverage large language models, representing an emerging trend toward generative and agent-based RCA. COCA's code knowledge enhancement and the ReAct agent's dynamic information collection demonstrate LLMs' potential to overcome data limitations.

**3. Domain-Specific Solutions**
Research has diversified beyond generic microservice RCA to address specific domains:
- Serverless applications (Huang et al., 2024)
- Autonomous driving systems (Feng et al., 2024)
- Complex data products (Demarne et al., 2024)

**4. Benchmarking and Evaluation**
The introduction of RCAEval (Pham et al., 2024c) addresses a critical gap in standardized evaluation, enabling reproducible research and fair comparison of approaches.

**5. Integration and Automation**
Multiple works emphasize end-to-end automation, integrating anomaly detection with RCA (BARO), or combining diagnosis with mitigation (ARCAS), reducing manual intervention and time-to-resolution.

### Key Challenges Identified

1. **Synthetic vs. Real-World Performance Gap:** Methods performing well on synthetic datasets often fail in production environments (Pham et al., 2024a)

2. **Data Availability:** Comprehensive monitoring data is often unavailable in issue tracking platforms (Li et al., 2025)

3. **Domain Knowledge Requirements:** Full system knowledge is infeasible for complex, real-time systems (Tonon et al., 2025)

4. **Dynamic System Behavior:** Serverless and highly dynamic systems challenge traditional RCA methods (Huang et al., 2024)

5. **Anomaly Detection Dependency:** RCA accuracy depends on preceding anomaly detection quality (Pham et al., 2024b)

### Future Research Directions

Based on the surveyed literature, promising directions include:

1. **Hybrid Approaches:** Combining causal inference with LLM-based reasoning to leverage both structured and unstructured information

2. **Partial Knowledge Systems:** Developing methods that work with incomplete domain knowledge rather than requiring full system understanding

3. **Cross-Domain Adaptation:** Adapting successful techniques from microservices to emerging paradigms like serverless and autonomous systems

4. **Real-World Validation:** Emphasizing production deployment and real-world evaluation over synthetic benchmarks

5. **Automated Mitigation:** Extending RCA systems to not only identify but also resolve root causes automatically

---

## References

Demarne, M., Cilimdzic, M., Falkowski, T., Johnson, T., Gramling, J., Kuang, W., Hou, H., Aryan, A., Subramaniam, G., Lee, K., Mejia, M., Liu, L., & Vermareddy, D. (2024). Automated root cause analysis system for complex data products. *arXiv preprint arXiv:2412.15374*. https://arxiv.org/abs/2412.15374v1

Feng, S., Ye, Y., Shi, Q., Cheng, Z., Xu, X., Cheng, S., Choi, H., & Zhang, X. (2024). ROCAS: Root cause analysis of autonomous driving accidents via cyber-physical co-mutation. *arXiv preprint arXiv:2409.07774*. https://arxiv.org/abs/2409.07774v2

Huang, J., Chen, P., Yu, G., Wang, Y., Huang, H., & He, Z. (2024). FaaSRCA: Full lifecycle root cause analysis for serverless applications. *arXiv preprint arXiv:2412.02239*. https://arxiv.org/abs/2412.02239v1

Li, Y., Wu, Y., Liu, J., Jiang, Z., Chen, Z., Yu, G., & Lyu, M. R. (2025). COCA: Generative root cause analysis for distributed systems with code knowledge. *arXiv preprint arXiv:2503.23051*. https://arxiv.org/abs/2503.23051v1

Pham, L., Ha, H., & Zhang, H. (2024). BARO: Robust root cause analysis for microservices via multivariate Bayesian online change point detection. *arXiv preprint arXiv:2405.09330*. https://arxiv.org/abs/2405.09330v1

Pham, L., Ha, H., & Zhang, H. (2024). Root cause analysis for microservice system based on causal inference: How far are we? *arXiv preprint arXiv:2408.13729*. https://arxiv.org/abs/2408.13729v2

Pham, L., Zhang, H., Ha, H., Salim, F., & Zhang, X. (2024). RCAEval: A benchmark for root cause analysis of microservice systems with telemetry data. *arXiv preprint arXiv:2412.17015*. https://arxiv.org/abs/2412.17015v5

Roy, D., Zhang, X., Bhave, R., Bansal, C., Las-Casas, P., Fonseca, R., & Rajmohan, S. (2024). Exploring LLM-based agents for root cause analysis. *arXiv preprint arXiv:2403.04123*. https://arxiv.org/abs/2403.04123v1

Tonon, A., Zhang, M., Caglayan, B., Shen, F., Gui, T., Wang, M., & Zhou, R. (2025). RADICE: Causal graph based root cause analysis for system performance diagnostic. *arXiv preprint arXiv:2501.11545*. https://arxiv.org/abs/2501.11545v1

Wang, T., & Qi, G. (2024). A comprehensive survey on root cause analysis in (micro) services: Methodologies, challenges, and trends. *arXiv preprint arXiv:2408.00803*. https://arxiv.org/abs/2408.00803v1

---

*Report generated on October 26, 2026*
