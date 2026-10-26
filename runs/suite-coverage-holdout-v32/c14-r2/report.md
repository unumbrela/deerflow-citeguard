# A Goal-Driven Survey on Root Cause Analysis: Systematic Literature Review

**Search Parameters:**
- **Category:** cs.SE (Software Engineering)
- **Publication Window:** October 22, 2023 – October 21, 2025
- **Number of Papers:** 10
- **Retrieval Date:** October 26, 2026

---

## Annotated Bibliography (APA Format)

### 1. Causal Inference-Based Methods for Microservices

**Pham, L., Ha, H., & Zhang, H. (2024).** Root Cause Analysis for Microservice System based on Causal Inference: How Far Are We? *arXiv preprint arXiv:2408.13729*. https://arxiv.org/abs/2408.13729v2

This paper presents a comprehensive evaluation of nine causal discovery methods and twenty-one root cause analysis methods for microservice systems. The authors conducted extensive experiments to assess both effectiveness and efficiency of causal inference-based RCA techniques. Key findings indicate that no single method excels in all situations; each approach shows limitations in either effectiveness, efficiency, or parameter sensitivity. Notably, performance on synthetic datasets does not accurately reflect real-system performance, highlighting significant room for improvement in current methodologies.

---

### 2. Integrated Anomaly Detection and RCA

**Pham, L., Ha, H., & Zhang, H. (2024).** BARO: Robust Root Cause Analysis for Microservices via Multivariate Bayesian Online Change Point Detection. *arXiv preprint arXiv:2405.09330*. https://arxiv.org/abs/2405.09330v1

BARO addresses the challenge of inaccurate anomaly detection affecting root cause localization by proposing an end-to-end approach integrating both phases. The method leverages Multivariate Bayesian Online Change Point Detection to model dependencies within multivariate time-series metrics data, enabling more accurate anomaly detection. A novel nonparametric statistical hypothesis testing technique provides robust root cause identification with reduced sensitivity to anomaly detection accuracy. Experiments on three benchmark microservice systems demonstrate BARO's superior performance over state-of-the-art approaches in both anomaly detection and root cause analysis.

---

### 3. Causal Graph-Based System Performance Diagnostics

**Tonon, A., Zhang, M., Caglayan, B., Shen, F., Gui, T., Wang, M., & Zhou, R. (2025).** RADICE: Causal Graph Based Root Cause Analysis for System Performance Diagnostic. *arXiv preprint arXiv:2501.11545*. https://arxiv.org/abs/2501.11545v1

RADICE introduces a novel causal domain knowledge model representing causal relations among system components, allowing domain experts to contribute partial knowledge for RCA. The algorithm employs causal graph discovery, enhancement, refinement, and subtraction processes to output a root cause causal sub-graph showing causal relations between components affected by anomalies. Evaluation with simulated data and real-world use cases demonstrates RADICE's superior performance compared to baseline methods, including causal discovery algorithms and correlation-based approaches. The work emphasizes that correlation does not imply causation, addressing a critical limitation in existing approaches.

---

### 4. Serverless Application RCA

**Huang, J., Chen, P., Yu, G., Wang, Y., Huang, H., & He, Z. (2024).** FaaSRCA: Full Lifecycle Root Cause Analysis for Serverless Applications. *arXiv preprint arXiv:2412.02239*. https://arxiv.org/abs/2412.02239v1

FaaSRCA addresses the unique challenges of serverless applications, which exhibit highly dynamic nature with short lifecycles and instantaneous pulse-like data lacking long-term continuous information. Unlike existing methods focusing solely on the running stage, FaaSRCA provides full lifecycle RCA by integrating multi-modal observability data from platform and application sides using Global Call Graph. A Graph Attention Network (GAT) based graph auto-encoder computes reconstruction scores for nodes, determining root causes at the granularity of lifecycle stages. Experimental evaluation on two serverless benchmarks shows top-k precision improvements ranging from 21.25% to 81.63% over baseline methods.

---

### 5. Autonomous Driving Systems RCA

**Feng, S., Ye, Y., Shi, Q., Cheng, Z., Xu, X., Cheng, S., Choi, H., & Zhang, X. (2024).** ROCAS: Root Cause Analysis of Autonomous Driving Accidents via Cyber-Physical Co-mutation. *arXiv preprint arXiv:2409.07774*. https://arxiv.org/abs/2409.07774v2

ROCAS fills a critical gap in autonomous driving systems (ADS) accident analysis, addressing challenges that existing cyber-physical system RCA techniques (designed for drones) cannot handle due to more complex physical environments and deep learning models in ADS. The framework features cyber-physical co-mutation, leveraging both physical and cyber mutations to precisely identify accident-trigger entities and pinpoint ADS misconfigurations. A differential analysis identifies responsible modules to reduce search space. Study of 12 ADS accident categories demonstrates ROCAS's effectiveness in narrowing search space and pinpointing misconfigurations, with detailed case studies illustrating how identified misconfigurations help understand accident rationales.

---

### 6. Code-Enhanced Generative RCA

**Li, Y., Wu, Y., Liu, J., Jiang, Z., Chen, Z., Yu, G., & Lyu, M. R. (2025).** COCA: Generative Root Cause Analysis for Distributed Systems with Code Knowledge. *arXiv preprint arXiv:2503.23051*. https://arxiv.org/abs/2503.23051v1

COCA addresses the limitation of prevailing automatic RCA approaches that rely on comprehensive runtime monitoring data often unavailable in issue platforms. The approach extracts diagnostic clues from code to supplement data-limited issue reports. COCA intelligently extracts relevant code snippets and reconstructs execution paths, providing comprehensive execution context for RCA. By constructing prompts combining historical issue reports with profiled code knowledge, COCA enables LLMs to generate detailed root cause summaries and localize responsible components. Evaluation on five real-world distributed systems demonstrates 28.3% improvement in root cause localization and 22.0% improvement in root cause summarization over existing methods, with robust generalizability across various LLMs.

---

### 7. Comprehensive Survey of Microservice RCA

**Wang, T., & Qi, G. (2024).** A Comprehensive Survey on Root Cause Analysis in (Micro) Services: Methodologies, Challenges, and Trends. *arXiv preprint arXiv:2408.00803*. https://arxiv.org/abs/2408.00803v1

This survey provides a comprehensive, structured review of RCA techniques within microservices, exploring methodologies that include metrics, traces, logs, and multi-model data. The complex dependencies and propagative faults inherent in microservices, characterized by dense networks of interconnected services, pose significant challenges in identifying underlying causes of issues. The survey delves into methodologies, challenges, and future trends within microservices architectures, positioned at the forefront of AI and automation advancements. It offers guidance for future research directions, emphasizing the crucial need for prompt identification and resolution of disruptive problems to ensure rapid recovery and maintain system stability.

---

### 8. DSL-Based Automated RCA System

**Demarne, M., Cilimdzic, M., Falkowski, T., Johnson, T., Gramling, J., Kuang, W., Hou, H., Aryan, A., Subramaniam, G., Lee, K., Mejia, M., Liu, L., & Vermareddy, D. (2024).** Automated Root Cause Analysis System for Complex Data Products. *arXiv preprint arXiv:2412.15374*. https://arxiv.org/abs/2412.15374v1

ARCAS (Automated Root Cause Analysis System) presents a diagnostic platform based on a Domain Specific Language (DSL) built for fast diagnostic implementation and low learning curve. The system comprises automated troubleshooting guides (Auto-TSGs) that execute in parallel to detect issues using product telemetry and apply mitigation in near-real-time. The DSL enables subject matter experts to deliver highly curated Auto-TSGs quickly without understanding system-wide interactions, reducing time-to-mitigate and saving engineering cycles. ARCAS uses LLMs to prioritize Auto-TSG outputs and take appropriate actions, suppressing the costly requirement of understanding general system behavior. The platform has been successfully deployed across Azure Synapse Analytics and Microsoft Fabric Synapse Data Warehouse products.

---

### 9. RCA Benchmark for Microservices

**Pham, L., Zhang, H., Ha, H., Salim, F., & Zhang, X. (2024).** RCAEval: A Benchmark for Root Cause Analysis of Microservice Systems with Telemetry Data. *arXiv preprint arXiv:2412.17015*. https://arxiv.org/abs/2412.17015v5

RCAEval addresses the absence of standard benchmarks with large-scale datasets and comprehensive evaluation environments for microservice RCA. The open-source benchmark provides three comprehensive datasets comprising 735 failure cases from three microservice systems, covering various fault types observed in real-world failures. A comprehensive evaluation framework includes fifteen reproducible baselines covering a wide range of RCA approaches, with ability to evaluate both coarse-grained and fine-grained RCA. This ready-to-use benchmark enables researchers and practitioners to conduct extensive analysis and paves the way for robust new solutions for microservice RCA.

---

### 10. LLM-Based Agents for RCA

**Roy, D., Zhang, X., Bhave, R., Bansal, C., Las-Casas, P., Fonseca, R., & Rajmohan, S. (2024).** Exploring LLM-based Agents for Root Cause Analysis. *arXiv preprint arXiv:2403.04123*. https://arxiv.org/abs/2403.04123v1

This work explores LLM-based agents for RCA to address limitations of prior approaches unable to dynamically collect additional diagnostic information such as incident-related logs, metrics, or databases. A ReAct agent equipped with retrieval tools was empirically evaluated on an out-of-distribution dataset of production incidents collected at Microsoft. Results show competitive performance with strong retrieval and reasoning baselines, but with highly increased factual accuracy. Incorporating discussions associated with incident reports as additional inputs surprisingly did not yield significant performance improvements. A case study with a Microsoft team equipped the ReAct agent with tools accessing external diagnostic services used for manual RCA, demonstrating practical considerations for implementing such systems.

---

## Thematic Analysis

### Research Trends (2023-2025)

The literature reveals several prominent themes in root cause analysis research:

1. **Causal Inference Dominance:** Multiple papers (Pham et al., 2024a; Pham et al., 2024b; Tonon et al., 2025) emphasize causal inference over correlation-based approaches, recognizing that correlation does not imply causation.

2. **LLM Integration:** Recent work increasingly leverages large language models for RCA (Li et al., 2025; Demarne et al., 2024; Roy et al., 2024), either for generating root cause summaries, prioritizing diagnostic outputs, or as agents with retrieval capabilities.

3. **Domain-Specific Solutions:** Research addresses specific architectural paradigms including microservices (Pham et al., 2024a; Pham et al., 2024b; Wang & Qi, 2024), serverless computing (Huang et al., 2024), autonomous driving systems (Feng et al., 2024), and distributed systems (Li et al., 2025).

4. **Benchmark Development:** The introduction of RCAEval (Pham et al., 2024d) addresses a critical gap in standardized evaluation, providing large-scale datasets and reproducible baselines.

5. **Integration Challenges:** Multiple works highlight the interdependence of anomaly detection and RCA (Pham et al., 2024b), the need for full lifecycle analysis (Huang et al., 2024), and the importance of incorporating code knowledge (Li et al., 2025).

### Key Challenges Identified

- **Synthetic vs. Real Performance:** Methods performing well on synthetic datasets may not translate to real systems (Pham et al., 2024a)
- **Incomplete Monitoring Data:** Runtime monitoring data is often unavailable in issue platforms (Li et al., 2025)
- **Dynamic Nature of Modern Architectures:** Serverless and microservice systems present unique challenges requiring specialized approaches (Huang et al., 2024)
- **Domain Knowledge Requirements:** Full expert knowledge is often infeasible for complex, real-time systems (Tonon et al., 2025)
- **Factual Accuracy:** LLM-based approaches must maintain high factual accuracy while leveraging reasoning capabilities (Roy et al., 2024)

### Future Directions

Based on the surveyed literature, promising research directions include:

1. Hybrid approaches combining causal inference with LLM capabilities
2. Enhanced benchmark datasets covering more diverse failure scenarios
3. Methods robust to incomplete or inaccurate anomaly detection
4. Full lifecycle analysis extending beyond runtime stages
5. Practical deployment considerations for production environments
6. Integration of partial domain knowledge with automated discovery

---

## References

Demarne, M., Cilimdzic, M., Falkowski, T., Johnson, T., Gramling, J., Kuang, W., Hou, H., Aryan, A., Subramaniam, G., Lee, K., Mejia, M., Liu, L., & Vermareddy, D. (2024). Automated Root Cause Analysis System for Complex Data Products. *arXiv preprint arXiv:2412.15374*. https://arxiv.org/abs/2412.15374v1

Feng, S., Ye, Y., Shi, Q., Cheng, Z., Xu, X., Cheng, S., Choi, H., & Zhang, X. (2024). ROCAS: Root Cause Analysis of Autonomous Driving Accidents via Cyber-Physical Co-mutation. *arXiv preprint arXiv:2409.07774*. https://arxiv.org/abs/2409.07774v2

Huang, J., Chen, P., Yu, G., Wang, Y., Huang, H., & He, Z. (2024). FaaSRCA: Full Lifecycle Root Cause Analysis for Serverless Applications. *arXiv preprint arXiv:2412.02239*. https://arxiv.org/abs/2412.02239v1

Li, Y., Wu, Y., Liu, J., Jiang, Z., Chen, Z., Yu, G., & Lyu, M. R. (2025). COCA: Generative Root Cause Analysis for Distributed Systems with Code Knowledge. *arXiv preprint arXiv:2503.23051*. https://arxiv.org/abs/2503.23051v1

Pham, L., Ha, H., & Zhang, H. (2024). BARO: Robust Root Cause Analysis for Microservices via Multivariate Bayesian Online Change Point Detection. *arXiv preprint arXiv:2405.09330*. https://arxiv.org/abs/2405.09330v1

Pham, L., Ha, H., & Zhang, H. (2024). Root Cause Analysis for Microservice System based on Causal Inference: How Far Are We? *arXiv preprint arXiv:2408.13729*. https://arxiv.org/abs/2408.13729v2

Pham, L., Zhang, H., Ha, H., Salim, F., & Zhang, X. (2024). RCAEval: A Benchmark for Root Cause Analysis of Microservice Systems with Telemetry Data. *arXiv preprint arXiv:2412.17015*. https://arxiv.org/abs/2412.17015v5

Roy, D., Zhang, X., Bhave, R., Bansal, C., Las-Casas, P., Fonseca, R., & Rajmohan, S. (2024). Exploring LLM-based Agents for Root Cause Analysis. *arXiv preprint arXiv:2403.04123*. https://arxiv.org/abs/2403.04123v1

Tonon, A., Zhang, M., Caglayan, B., Shen, F., Gui, T., Wang, M., & Zhou, R. (2025). RADICE: Causal Graph Based Root Cause Analysis for System Performance Diagnostic. *arXiv preprint arXiv:2501.11545*. https://arxiv.org/abs/2501.11545v1

Wang, T., & Qi, G. (2024). A Comprehensive Survey on Root Cause Analysis in (Micro) Services: Methodologies, Challenges, and Trends. *arXiv preprint arXiv:2408.00803*. https://arxiv.org/abs/2408.00803v1

---

**Report Generated:** October 26, 2026  
**Total Papers Reviewed:** 10  
**Publication Period:** October 22, 2023 – October 21, 2025  
**Primary Category:** cs.SE (Software Engineering)
