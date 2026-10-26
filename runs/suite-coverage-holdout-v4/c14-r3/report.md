# Systematic Literature Review: Goal-Driven Survey on Root Cause Analysis

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "root cause analysis", filtered to category cs.SE, published between 2023-10-22 and 2025-10-21
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in root cause analysis (RCA) for software engineering systems, with particular attention to goal-driven and autonomous approaches. The surveyed literature reveals a field rapidly evolving toward LLM-augmented autonomous agents that can perform end-to-end diagnosis without relying on manual workflows. A dominant trend is the integration of tool-augmented language models with traditional diagnostic methods, enabling systems to collect diagnostic information dynamically, reason about evidence, and generate actionable root cause summaries. The literature spans cloud infrastructure, microservices, distributed systems, and large-scale ML training platforms, reflecting the growing complexity of modern software systems and the corresponding need for automated, intelligent diagnostic capabilities.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query `root cause analysis`, filtered to category cs.SE, published between 2023-10-22 and 2025-10-21. Papers were sorted by co-citation relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening flow**: 50 papers identified by search, 69 added from citation expansion, 30 shortlisted, 10 included (4 from references).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: LLM-Based Autonomous Agents for Root Cause Analysis

The most prominent theme across the surveyed literature is the emergence of autonomous agents powered by large language models for performing root cause analysis. These systems move beyond traditional rule-based or statistical approaches by enabling free-form reasoning, tool usage, and dynamic information collection. Wang et al. (2023) introduced RCAgent, a tool-augmented LLM framework that demonstrates consistent superiority over ReAct baselines in predicting root causes, solutions, and evidence. The framework has been successfully integrated into Alibaba Cloud's Real-time Compute Platform for Apache Flink diagnosis, demonstrating practical viability.

Building on this foundation, Roy et al. (2024) explored LLM-based agents equipped with retrieval tools for production incident diagnosis at Microsoft. Their work shows that ReAct agents achieve highly increased factual accuracy compared to retrieval and reasoning baselines while maintaining competitive performance. A key insight is that agents equipped with external diagnostic service tools can overcome limitations of prior work that could not collect additional diagnostic information dynamically. This represents a fundamental shift from static analysis to interactive, goal-driven diagnosis where the agent actively seeks out relevant evidence.

### Theme 2: Log-Based Failure Diagnosis and Information Extraction

A second major theme focuses on extracting fault-indicating information from system logs to reduce manual investigation effort. Huang et al. (2024) developed LoFI, a two-stage approach combining coarse-grained semantic filtering with fine-grained extraction using pre-trained language models with prompt-based tuning. The system achieves substantial improvements (25.8-37.9 F1) over baselines including ChatGPT, and has been deployed at CloudA with positive user validation.

Extending log-based diagnosis to the domain of large language model training, Jiang et al. (2025) identified three distinct log patterns (cross-job, spatial, temporal) in 428 LLM training failures from Platform-X. Their L4 framework addresses the unique characteristics of LLM training logs that existing diagnostic methods cannot adequately handle. The work reveals that hardware and user faults are the predominant root causes of training failures, and L4 successfully localizes faulty nodes with superior accuracy. Shan et al. (2024) focused specifically on configuration error localization, proposing LogConfigLocalizer, an LLM-based two-stage strategy that achieves 99.91% accuracy on Hadoop. This work is particularly notable for targeting end-users without source code access, democratizing diagnostic capabilities.

### Theme 3: Causal Inference and Statistical Methods for Microservices

The third theme encompasses causal inference and statistical approaches for root cause analysis in microservice architectures. Pham et al. (2024a) developed BARO, which integrates anomaly detection with root cause analysis using Multivariate Bayesian Online Change Point Detection. The approach models dependencies in multivariate time-series metrics and employs nonparametric statistical hypothesis testing for robust root cause identification. BARO consistently outperforms state-of-the-art approaches across three benchmark systems and is notably less sensitive to anomaly detection accuracy.

In a comprehensive evaluation, Pham et al. (2024b) assessed nine causal discovery methods and twenty-one root cause analysis methods for microservice systems. Their findings reveal that no single method performs optimally across all situations, with each approach exhibiting trade-offs in effectiveness, efficiency, or parameter sensitivity. Critically, performance on synthetic datasets does not accurately reflect real-system performance, highlighting the importance of realistic evaluation. Ding et al. (2023) proposed TraceDiag, using reinforcement learning to learn interpretable, adaptive pruning policies for service dependency graphs. This approach significantly improves RCA efficiency by automatically eliminating redundant components, and has been integrated into Microsoft M365 Exchange.

### Theme 4: Comprehensive Surveys and Best Practices

Zhang et al. (2024) conducted an exhaustive review of 98 scientific papers on failure diagnosis in microservice systems, providing comprehensive coverage of current best practices and future research directions. Their work compiles publicly available resources including datasets, toolkits, and evaluation metrics to facilitate technique selection and validation. The survey emphasizes that microservice systems present unique challenges due to independent deployment and dynamic interactions, with cascading failures negatively impacting operational efficiency and user experience.

### Theme 5: Code Knowledge Integration for Enhanced Diagnosis

Li et al. (2025) introduced COCA, a code knowledge-enhanced root cause analysis approach for distributed systems. The method extracts relevant code snippets and reconstructs execution paths from issue reports to provide comprehensive execution context. COCA achieves 28.3% improvement in root cause localization and 22.0% improvement in summarization compared to existing methods, demonstrating robust generalizability across various large language models. This work addresses the challenge of incomplete or ambiguous information in issue reports by grounding LLM reasoning in concrete code-level evidence.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that LLM-augmented approaches significantly outperform traditional baselines in root cause analysis tasks (Wang et al., 2023; Roy et al., 2024; Huang et al., 2024; Li et al., 2025). There is also broad agreement that integrating multiple diagnostic modalities—logs, metrics, traces, and code knowledge—yields superior results compared to single-source approaches. Several systems have achieved successful production deployment (RCAgent in Alibaba Cloud, LoFI in CloudA, L4 in Platform-X, TraceDiag in Microsoft M365 Exchange), validating practical viability.

**Disagreements**: The literature reveals tension between end-to-end learned approaches and modular, interpretable methods. While BARO (Pham et al., 2024a) and TraceDiag (Ding et al., 2023) emphasize interpretable statistical methods and learned pruning policies, the LLM-based agent approaches prioritize flexible reasoning over explicit interpretability. Additionally, Roy et al. (2024) found that adding incident discussions as inputs did not yield significant performance improvements, suggesting limits to certain information modalities that contrast with the general trend toward multi-modal integration.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, most papers do not explicitly state limitations in their abstracts, making it difficult to assess boundary conditions and failure modes. Second, while multiple systems report successful production deployment, systematic evaluation of long-term operational characteristics—including maintenance burden, false positive rates, and adaptation to system evolution—is largely absent. Third, the evaluation of causal inference methods on synthetic versus real systems reveals a methodological gap: researchers need better benchmarks that capture real-world complexity while remaining reproducible.

Fourth, the literature focuses heavily on cloud infrastructure and microservices, with less attention to edge computing, IoT, or embedded systems contexts. Fifth, while LLM-based approaches show promise, their computational cost, latency, and privacy implications in production settings are not thoroughly addressed. Finally, the human-AI collaboration aspect—how diagnostic systems should present findings to operators, handle uncertainty, and support decision-making—remains underexplored despite clear implications for operational practice.

## Per-Paper Annotations

### Ding et al. (2023)

**Research question**: How can root cause analysis be made more efficient and accurate for large-scale microservice systems with hundreds of components?
**Methodology**: The authors propose TraceDiag, an end-to-end RCA framework using reinforcement learning to learn an interpretable, adaptive pruning policy for service dependency graphs, enabling efficient causal-based analysis on the pruned graph.
**Key findings**:
- TraceDiag significantly improves RCA efficiency by automatically eliminating redundant components through learned pruning policies.
- The framework demonstrates superior performance compared to state-of-the-art RCA approaches on real Microsoft Exchange system data.
- TraceDiag has been integrated into Microsoft M365 Exchange, improving system reliability and reducing human effort.
- The learned pruning policy is both interpretable and adaptive to new RCA instances.
**Limitations**: Not stated in abstract.

### Wang et al. (2023)

**Research question**: How can tool-augmented LLM autonomous agents improve cloud root cause analysis without relying on manual workflows?
**Methodology**: The authors developed RCAgent, a tool-augmented LLM framework running on an internally deployed model, incorporating Self-Consistency for action trajectories and methods for context management, stabilization, and domain knowledge import. The framework was evaluated against ReAct across multiple RCA dimensions using automated metrics and human evaluations.
**Key findings**:
- RCAgent demonstrates consistent superiority over ReAct in predicting root causes, solutions, evidence, and responsibilities.
- The framework performs well on both tasks covered and uncovered by current rules.
- RCAgent has been successfully integrated into Alibaba Cloud's Real-time Compute Platform for Apache Flink diagnosis workflow.
- The approach enables free-form data collection and comprehensive analysis with tools while maintaining privacy awareness.
**Limitations**: The abstract does not explicitly state limitations; evaluation appears to focus on comparison with ReAct and validation within Alibaba Cloud's infrastructure.

### Huang et al. (2024)

**Research question**: How can fault-indicating information be automatically extracted from logs to reduce manual investigation effort in failure diagnosis?
**Methodology**: LoFI uses a two-stage approach: coarse-grained filtering based on semantic similarity to collect fault-related logs, followed by fine-grained extraction using a pre-trained language model with novel prompt-based tuning to identify fault-indicating descriptions and parameters.
**Key findings**:
- LoFI outperforms all baseline methods, achieving a 25.8-37.9 F1 improvement over the best baseline (ChatGPT).
- Engineers prioritize fault-indicating descriptions (abnormal system events) and fault-indicating parameters (associated entities) for diagnosis.
- LoFI has been successfully deployed at CloudA with positive user study validation.
- The prompt-based tuning method effectively extracts fine-grained fault information from collected logs.
**Limitations**: The abstract does not explicitly state limitations; the approach focuses on log-based diagnosis and may not address other diagnostic data sources like metrics or traces.

### Roy et al. (2024)

**Research question**: Can LLM-based agents equipped with retrieval tools improve root cause analysis by dynamically collecting diagnostic information?
**Methodology**: The authors conducted empirical evaluation of a ReAct agent with retrieval tools on production incidents from Microsoft, tested the impact of adding incident discussions as inputs, and performed a case study equipping the agent with external diagnostic service tools.
**Key findings**:
- ReAct agents perform competitively with strong retrieval and reasoning baselines while achieving highly increased factual accuracy.
- Adding incident discussions as additional inputs does not yield significant performance improvements.
- Agents equipped with external diagnostic service tools can overcome limitations of prior work that couldn't collect additional diagnostic information.
- The approach demonstrates practical considerations for implementing LLM-based RCA systems in production environments.
**Limitations**: The abstract suggests that incorporating incident discussions did not significantly improve performance, indicating potential limitations in certain input modalities; specific constraints on tool access or scalability are not detailed.

### Shan et al. (2024)

**Research question**: How can end-users without source code access localize configuration error root causes using logs and LLMs?
**Methodology**: The authors conducted a preliminary study on log-based configuration error diagnosis, then proposed and implemented LogConfigLocalizer, an LLM-based two-stage strategy that localizes root-cause configuration properties through log analysis.
**Key findings**:
- The LLM-based two-stage strategy achieves 99.91% average accuracy in localizing configuration errors on Hadoop.
- This is the first work to localize root-cause configuration properties for end-users using LLMs and logs.
- Different phases of the methodology are demonstrated to be effective and necessary through comparison with variants and baselines.
- The approach is particularly valuable for end-users without access to source code.
**Limitations**: Not stated in abstract.

### Pham et al. (2024a)

**Research question**: How can root cause analysis for microservices be made robust to inaccurate anomaly detection results?
**Methodology**: BARO integrates anomaly detection and root cause analysis using Multivariate Bayesian Online Change Point Detection to model dependencies in multivariate time-series metrics, combined with a novel nonparametric statistical hypothesis testing technique for identifying root causes.
**Key findings**:
- BARO consistently outperforms state-of-the-art approaches in both anomaly detection and root cause analysis across three benchmark microservice systems.
- The approach is less sensitive to anomaly detection accuracy compared to existing works.
- Integrating anomaly detection with root cause analysis in an end-to-end manner improves failure troubleshooting effectiveness.
- The nonparametric statistical hypothesis testing technique provides robust root cause identification.
**Limitations**: The abstract does not explicitly state limitations; the approach is evaluated on three benchmark systems but real-world production deployment challenges are not discussed.

### Zhang et al. (2024)

**Research question**: What are the current best practices, challenges, and future directions in failure diagnosis for microservice systems?
**Methodology**: The authors conducted an exhaustive review of 98 scientific papers from 2003 to present, examining fundamental concepts, system architecture, problem statements, and providing qualitative analysis with compilation of datasets, toolkits, and evaluation metrics.
**Key findings**:
- Microservice systems present unique failure diagnosis challenges due to independent deployment and dynamic interactions.
- The survey provides comprehensive coverage of current best practices and future research directions.
- Cascading failures in microservice systems can negatively impact operational efficiency and user experience.
- The work compiles publicly available resources (datasets, toolkits, metrics) to facilitate technique selection and validation.
**Limitations**: Not stated in abstract.

### Pham et al. (2024b)

**Research question**: What is the current state and effectiveness of causal inference-based root cause analysis methods for microservice systems?
**Methodology**: The authors conducted a comprehensive evaluation of nine causal discovery methods and twenty-one root cause analysis methods to assess their effectiveness, efficiency, and sensitivity to various parameters.
**Key findings**:
- No single method performs optimally across all situations; each method has trade-offs in effectiveness, efficiency, or parameter sensitivity.
- Performance on synthetic datasets does not accurately reflect performance in real systems.
- There remains significant room for improvement in causal inference-based root cause analysis methods.
- The study identifies specific factors that affect the performance of different methods.
**Limitations**: Not stated in abstract.

### Jiang et al. (2025)

**Research question**: How can automated log analysis effectively diagnose failures in large-scale LLM training to reduce resource and time waste?
**Methodology**: The authors conducted an empirical study of 428 LLM training failures from Platform-X (May 2023-April 2024), identifying three distinct log patterns (cross-job, spatial, temporal). They then developed L4, a log-based diagnosis framework that automatically extracts failure-indicating information from training logs.
**Key findings**:
- Hardware and user faults are the predominant root causes of LLM training failures.
- Existing log-based diagnostic methods are inadequate for handling the unique characteristics of LLM training logs.
- L4 successfully identifies failure-indicating logs and localizes faulty nodes, outperforming existing approaches.
- L4 has been deployed in Platform-X and demonstrated effectiveness in enabling accurate and efficient failure diagnosis.
**Limitations**: Not stated in abstract.

### Li et al. (2025)

**Research question**: How can automatic root cause analysis for distributed system failures be improved when issue reports contain incomplete or ambiguous information?
**Methodology**: The authors propose COCA, a code knowledge enhanced root cause analysis approach that extracts relevant code snippets and reconstructs execution paths from issue reports to provide comprehensive execution context. COCA constructs prompts combining historical issue reports with profiled code knowledge to enable LLMs to generate detailed root cause summaries and localize responsible components.
**Key findings**:
- COCA significantly outperforms existing methods on datasets from five real-world distributed systems.
- COCA achieves a 28.3% improvement in root cause localization compared to existing methods.
- COCA achieves a 22.0% improvement in root cause summarization compared to existing methods.
- COCA demonstrates robust generalizability with consistent performance across various large language models.
**Limitations**: Not stated in abstract.

## References

Ding, R., Zhang, C., Wang, L., Xu, Y., Ma, M., Wu, X., Zhang, M., Chen, Q., Gao, X., Gao, X., Fan, H., Rajmohan, S., Lin, Q., & Zhang, D. (2023). TraceDiag: Adaptive, interpretable, and efficient root cause analysis on large-scale microservice systems. arXiv. https://arxiv.org/abs/2310.18740

Huang, J., Jiang, Z., Liu, J., Huo, Y., Gu, J., Chen, Z., Feng, C., Dong, H., Yang, Z., & Lyu, M. R. (2024). Demystifying and extracting fault-indicating information from logs for failure diagnosis. arXiv. https://arxiv.org/abs/2409.13561

Jiang, Z., Huang, J., Chen, Z., Li, Y., Yu, G., Feng, C., Yang, Y., Yang, Z., & Lyu, M. R. (2025). L4: Diagnosing large-scale LLM training failures via automated log analysis. arXiv. https://arxiv.org/abs/2503.20263

Li, Y., Wu, Y., Liu, J., Jiang, Z., Chen, Z., Yu, G., & Lyu, M. R. (2025). COCA: Generative root cause analysis for distributed systems with code knowledge. arXiv. https://arxiv.org/abs/2503.23051

Pham, L., Ha, H., & Zhang, H. (2024a). BARO: Robust root cause analysis for microservices via multivariate Bayesian online change point detection. arXiv. https://arxiv.org/abs/2405.09330

Pham, L., Ha, H., & Zhang, H. (2024b). Root cause analysis for microservice system based on causal inference: How far are we? arXiv. https://arxiv.org/abs/2408.13729

Roy, D., Zhang, X., Bhave, R., Bansal, C., Las-Casas, P., Fonseca, R., & Rajmohan, S. (2024). Exploring LLM-based agents for root cause analysis. arXiv. https://arxiv.org/abs/2403.04123

Shan, S., Huo, Y., Su, Y., Li, Y., Li, D., & Zheng, Z. (2024). Face it yourselves: An LLM-based two-stage strategy to localize configuration errors via logs. arXiv. https://arxiv.org/abs/2404.00640

Wang, Z., Liu, Z., Zhang, Y., Zhong, A., Wang, J., Yin, F., Fan, L., Wu, L., & Wen, Q. (2023). RCAgent: Cloud root cause analysis by autonomous agents with tool-augmented large language models. arXiv. https://arxiv.org/abs/2310.16340

Zhang, S., Xia, S., Fan, W., Shi, B., Xiong, X., Zhong, Z., Ma, M., Sun, Y., & Pei, D. (2024). Failure diagnosis in microservice systems: A comprehensive survey and analysis. arXiv. https://arxiv.org/abs/2407.01710
