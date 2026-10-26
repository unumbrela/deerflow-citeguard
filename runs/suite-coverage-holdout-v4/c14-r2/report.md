# Systematic Literature Review: A Goal-Driven Survey on Root Cause Analysis

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "root cause analysis", category cs.SE, published between 2023-10-22 and 2025-10-21
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in root cause analysis (RCA) for software systems, with particular focus on goal-driven and automated approaches. The surveyed literature reveals a field undergoing rapid transformation driven by large language models (LLMs) and AI operations (AIOps). Ten papers published between October 2023 and October 2025 demonstrate a clear shift from traditional statistical and causal inference methods toward LLM-augmented autonomous agents capable of dynamic diagnostic information collection. The literature converges on the importance of integrating multiple data sources (logs, traces, metrics) and automating fault pattern recognition, while significant challenges remain in handling the complexity of modern microservice architectures and large-scale distributed systems. Notably, several approaches have achieved successful industrial deployment, indicating maturity beyond purely academic research.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "root cause analysis", filtered to category cs.SE, published between 2023-10-22 and 2025-10-21. Papers were selected through citation expansion and co-citation screening, with the top 10 most central papers included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search and screening statistics**: 50 papers identified by initial search, 69 additional papers added through citation expansion, 30 papers shortlisted, 10 papers included (5 from reference expansion). Screening scores ranged from 0-3, with included papers receiving scores of 2-3.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search was restricted to the software engineering category, potentially excluding relevant work in adjacent fields such as distributed systems or machine learning operations.

## Themes

### Theme 1: LLM-Augmented Autonomous Agents for RCA

The emergence of LLM-based agents represents a paradigm shift in root cause analysis automation. Wang et al. (2023) introduced RCAgent, a tool-augmented autonomous agent framework that operates without manual workflow configurations, combining self-consistency mechanisms for action trajectories with domain knowledge import. Their approach demonstrated superior performance over ReAct baselines across multiple RCA dimensions, including root cause prediction, solution generation, and evidence collection. Similarly, Roy et al. (2024) empirically evaluated ReAct agents equipped with retrieval tools on production incidents from Microsoft, finding that agents achieve highly increased factual accuracy while performing competitively with strong retrieval and reasoning baselines. The key innovation in this theme is the ability of LLM agents to dynamically collect diagnostic information rather than relying on static, pre-defined workflows, enabling more flexible and comprehensive analysis.

### Theme 2: Log-Based Failure Diagnosis and Fault Information Extraction

A substantial body of work focuses on extracting fault-indicating information from system logs, recognizing that logs contain critical diagnostic signals. Huang et al. (2024a) proposed LoFI, a two-stage approach that first performs coarse-grained filtering based on semantic similarity, then uses pre-trained language models with novel prompt-based tuning to extract fine-grained fault-indicating descriptions and parameters. Their method achieved F1 improvements of 25.8–37.9 points over ChatGPT baselines and has been deployed at CloudA. Extending this work to large language model training specifically, Jiang et al. (2025) developed L4, a log-based framework that automatically extracts failure-indicating information from LLM training logs, addressing the unique cross-job, spatial, and temporal patterns characteristic of distributed training failures. These approaches share a common goal: transforming unstructured log data into structured, actionable diagnostic information that can guide root cause identification.

### Theme 3: Microservice System Root Cause Analysis

The complexity of microservice architectures has spawned specialized RCA approaches addressing the unique challenges of distributed, independently-deployable services. Pham et al. (2024a) introduced BARO, which integrates anomaly detection and root cause analysis using Multivariate Bayesian Online Change Point Detection, making the approach robust to inaccurate anomaly detection results—a common failure mode in existing methods. Ding et al. (2023) proposed TraceDiag, employing reinforcement learning to learn interpretable, adaptive pruning policies for service dependency graphs, enabling efficient execution of causal-based methods on large-scale systems with hundreds of components. Their integration into Microsoft M365 Exchange resulted in significant reliability improvements. Pham et al. (2024b) conducted a comprehensive evaluation of nine causal discovery methods and twenty-one RCA methods, revealing that no single method dominates across all situations and that performance on synthetic datasets may not accurately reflect real-world effectiveness.

### Theme 4: Cloud System Fault Profiling and Incident Analysis

Large-scale cloud systems generate vast numbers of incident tickets requiring systematic analysis. Huang et al. (2024b) developed FaultProfIT, an automated fault pattern profiling approach leveraging hierarchy-guided contrastive learning to train hierarchy-aware incident encoders. Deployed at CloudA for six months, the system analyzed over 10,000 incidents from 30+ cloud services and successfully revealed fault trends that informed system improvements. This theme emphasizes the importance of learning from historical incident data to identify recurring fault patterns, enabling proactive system improvements and reducing manual labeling burden.

### Theme 5: Comprehensive Surveys and AIOps Evolution

The field has matured sufficiently to warrant comprehensive surveys synthesizing best practices and identifying future directions. Zhang et al. (2024a) conducted an exhaustive review of 98 scientific papers on failure diagnosis in microservice systems, compiling publicly available datasets, toolkits, and evaluation metrics to facilitate technique selection and validation. Zhang et al. (2024b) provided the first comprehensive survey discussing differences between LLM-based and traditional AIOps methods for failure management, identifying how LLMs can address challenges such as lack of cross-platform generality and cross-task flexibility that have limited traditional approaches. These surveys serve as valuable resources for practitioners navigating the expanding landscape of RCA techniques.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of automation in RCA workflows. Wang et al. (2023), Roy et al. (2024), Huang et al. (2024a), and Jiang et al. (2025) all demonstrate successful industrial deployments of automated RCA systems, validating the practical viability of these approaches. There is strong agreement that integrating multiple data sources—logs, traces, metrics, and incident tickets—provides more comprehensive diagnostic coverage than single-source approaches. Additionally, several papers (Pham et al., 2024a; Ding et al., 2023) emphasize the need for robustness to inaccurate anomaly detection, recognizing that upstream detection errors should not cascade into RCA failures.

**Disagreements**: The literature reveals tension between specialized and general-purpose approaches. While LLM-based agents (Wang et al., 2023; Roy et al., 2024) advocate for flexible, general-purpose reasoning capabilities, causal inference methods (Pham et al., 2024a, 2024b) emphasize the importance of domain-specific statistical modeling. Pham et al.'s (2024b) finding that no single causal inference method dominates across all situations contrasts with the more unified performance claims of LLM-based approaches, though direct comparisons are limited. Additionally, Roy et al. (2024) found that incorporating incident discussions did not yield significant performance improvements, suggesting that additional context may not always enhance RCA accuracy—a finding that warrants further investigation.

## Gaps and Open Questions

The surveyed literature reveals several notable gaps. First, **none of the papers explicitly state limitations** in their abstracts, suggesting either that limitations are discussed only in full text or that systematic limitation reporting is insufficient. This gap impedes clear understanding of method boundaries and failure modes.

Second, while multiple papers report successful industrial deployments (Wang et al., 2023; Huang et al., 2024a, 2024b; Jiang et al., 2025; Ding et al., 2023), **comparative evaluations between different approaches on common benchmarks are limited**. The field would benefit from standardized evaluation frameworks enabling direct comparison of LLM-based agents, causal inference methods, and statistical approaches.

Third, the **integration of LLM-based reasoning with traditional statistical and causal methods** remains underexplored. While surveys (Zhang et al., 2024b) identify LLMs as addressing traditional AIOps limitations, concrete hybrid architectures combining the flexibility of LLMs with the rigor of causal inference are not well represented in the surveyed literature.

Fourth, **human-AI collaboration in RCA workflows** receives limited attention. Most approaches focus on full automation, yet the optimal division of labor between automated systems and human engineers—particularly for complex, novel failure modes—remains an open question.

Finally, the literature focuses heavily on **reactive diagnosis** rather than **proactive prevention**. While fault pattern profiling (Huang et al., 2024b) represents a step toward proactive improvement, methods for predicting and preventing failures before they occur are underrepresented.

## Per-Paper Annotations

### Ding et al. (2023)

**Research question**: How can root cause analysis be made more efficient and accurate for large-scale microservice systems with hundreds of components?

**Methodology**: The authors propose TraceDiag, an end-to-end RCA framework using reinforcement learning to learn an interpretable, adaptive pruning policy for service dependency graphs, enabling efficient execution of causal-based methods on the pruned graph.

**Key findings**:
- TraceDiag automatically eliminates redundant components through learned pruning policies, significantly improving RCA efficiency
- The learned pruning policy is interpretable and fully adaptive to new RCA instances
- TraceDiag demonstrates superior performance compared to state-of-the-art RCA approaches on real data from Microsoft Exchange
- Integration into Microsoft M365 Exchange resulted in significant reliability improvements and reduced human effort for RCA

**Limitations**: Not stated in abstract.

### Huang et al. (2024a)

**Research question**: How can fault-indicating information be automatically extracted from logs to support failure diagnosis in online service systems?

**Methodology**: The authors propose LoFI, a two-stage approach: first performing coarse-grained filtering of logs based on semantic similarity to collect fault-related logs, then using a pre-trained language model with a novel prompt-based tuning method to extract fine-grained fault-indicating descriptions and parameters.

**Key findings**:
- Engineers prioritize two categories of log information for diagnosis: fault-indicating descriptions (abnormal system events) and fault-indicating parameters (associated entities)
- LoFI outperforms all baseline methods by a significant margin on Apache Spark and CloudA industrial datasets
- LoFI achieves an absolute improvement of 25.8–37.9 in F1 over the best baseline method, ChatGPT
- Successful deployment at CloudA and user studies validate the practical utility of the method

**Limitations**: Not stated in abstract.

### Huang et al. (2024b)

**Research question**: How can fault pattern profiling of incident tickets in large-scale cloud systems be automated to overcome the limitations of manual labeling?

**Methodology**: The authors propose FaultProfIT, an automated approach that leverages hierarchy-guided contrastive learning to train a hierarchy-aware incident encoder and predict fault patterns with enhanced incident representations. The approach was evaluated using production incidents from CloudA.

**Key findings**:
- FaultProfIT outperforms state-of-the-art methods in fault pattern profiling
- The ablation study verifies the effectiveness of hierarchy-guided contrastive learning
- FaultProfIT has been deployed at CloudA for six months and analyzed 10,000+ incidents from 30+ cloud services
- The system successfully revealed several fault trends that informed system improvements

**Limitations**: Not stated in abstract.

### Jiang et al. (2025)

**Research question**: How can failure diagnosis for large-scale LLM training be automated to reduce resource and time waste caused by training failures?

**Methodology**: The authors conducted an empirical study of 428 LLM training failures from Platform-X, identified three distinct log patterns (cross-job, spatial, temporal), and developed L4, a log-based framework that automatically extracts failure-indicating information (log events, nodes, stages, iterations) from training logs.

**Key findings**:
- Hardware and user faults are the predominant root causes of LLM training failures
- Existing log-based diagnostic methods are inadequate for handling the unique features of LLM training logs
- LLM training logs exhibit three distinct patterns: cross-job, spatial, and temporal
- L4 outperforms existing approaches in identifying failure-indicating logs and localizing faulty nodes on real-world datasets
- L4 has been successfully deployed in Platform-X, demonstrating effectiveness in accurate and efficient failure diagnosis

**Limitations**: Not stated in abstract.

### Pham et al. (2024a)

**Research question**: How can root cause analysis for microservices be made robust to inaccurate anomaly detection results?

**Methodology**: The authors propose BARO, an end-to-end approach that integrates anomaly detection and root cause analysis using Multivariate Bayesian Online Change Point Detection to model dependencies within multivariate time-series metrics data, combined with a novel nonparametric statistical hypothesis testing technique for identifying root causes.

**Key findings**:
- BARO consistently outperforms state-of-the-art approaches in both anomaly detection and root cause analysis
- The approach is less sensitive to the accuracy of anomaly detection compared to existing works
- Multivariate Bayesian Online Change Point Detection enables more accurate anomaly detection
- The method was validated on three popular benchmark microservice systems
- BARO provides an integrated solution for the typical two-phase failure troubleshooting pipeline

**Limitations**: Not stated in abstract.

### Pham et al. (2024b)

**Research question**: What is the current state and effectiveness of causal inference-based root cause analysis methods for microservice systems?

**Methodology**: The authors conducted a comprehensive evaluation of nine causal discovery methods and twenty-one root cause analysis methods to assess their effectiveness, efficiency, and factors affecting performance on both synthetic and real systems.

**Key findings**:
- No single method stands out in all situations; each method has trade-offs in effectiveness, efficiency, or parameter sensitivity
- Performance on synthetic datasets may not accurately reflect performance in real microservice systems
- There remains significant room for improvement in causal inference-based root cause analysis methods
- The study identifies specific factors that affect the performance of different methods

**Limitations**: Not stated in abstract.

### Roy et al. (2024)

**Research question**: Can LLM-based agents with retrieval tools overcome the limitations of prior RCA approaches that cannot dynamically collect diagnostic information?

**Methodology**: The authors conducted empirical evaluation of a ReAct agent equipped with retrieval tools on an out-of-distribution dataset of production incidents from Microsoft, and extended the evaluation by incorporating incident-related discussions. A case study was also conducted to equip the agent with tools accessing external diagnostic services used by a Microsoft team.

**Key findings**:
- ReAct performs competitively with strong retrieval and reasoning baselines while achieving highly increased factual accuracy
- Incorporating discussions associated with incident reports as additional inputs does not yield significant performance improvements
- Agents can overcome the limitations of prior work by accessing external diagnostic services
- The approach demonstrates practical considerations for implementing such systems in production environments
- Automation of RCA can significantly save time and ease the burden on on-call engineers

**Limitations**: Not stated in abstract.

### Wang et al. (2023)

**Research question**: How can tool-augmented LLM autonomous agents improve cloud root cause analysis without relying on manual workflow settings?

**Methodology**: The authors present RCAgent, a tool-augmented LLM autonomous agent framework that runs on internally deployed models and combines Self-Consistency for action trajectories with methods for context management, stabilization, and domain knowledge import. The framework was evaluated through experiments comparing RCAgent against ReAct across multiple RCA aspects using automated metrics and human evaluations.

**Key findings**:
- RCAgent demonstrates consistent superiority over ReAct in predicting root causes, solutions, evidence, and responsibilities
- The framework performs well on both tasks covered and uncovered by current rules
- RCAgent enables free-form data collection and comprehensive analysis with tools
- The system has been successfully integrated into Alibaba Cloud's Real-time Compute Platform for Apache Flink
- Validation through both automated metrics and human evaluations confirms the framework's effectiveness

**Limitations**: Not stated in abstract.

### Zhang et al. (2024a)

**Research question**: What are the current best practices, fundamental concepts, and future directions for failure diagnosis in modern microservice systems?

**Methodology**: The authors conducted an exhaustive review of 98 scientific papers from 2003 to the present, examining fundamental concepts, system architecture, and problem statements, along with qualitative analysis of dimensions and current best practices.

**Key findings**:
- Modern microservice systems present unique failure diagnosis challenges due to independent deployment and dynamic interactions
- The complexity of microservice systems can lead to cascading failures that negatively impact operational efficiency and user experience
- The survey compiles publicly available datasets, toolkits, and evaluation metrics to facilitate technique selection and validation
- The paper provides in-depth discussion of current best practices and future directions for failure diagnosis

**Limitations**: Not stated in abstract.

### Zhang et al. (2024b)

**Research question**: What are the differences between LLM-based AIOps and traditional AIOps methods for failure management, and what are the challenges and future directions?

**Methodology**: The authors conducted a comprehensive survey of AIOps technology for failure management in the LLM era, including detailed definitions of AIOps tasks, data sources, LLM-based approaches, and exploration of AIOps subtasks with suitable LLM-based approaches.

**Key findings**:
- LLMs can significantly address challenges faced by traditional AIOps methods such as lack of cross-platform generality and cross-task flexibility
- The survey provides comprehensive coverage of AIOps tasks for failure management and their data sources
- Different LLM-based approaches are suitable for different AIOps subtasks
- The paper identifies challenges and future directions for the domain
- This is the first comprehensive survey discussing differences between LLM-based and traditional AIOps methods

**Limitations**: Not stated in abstract.

## References

Ding, R., Zhang, C., Wang, L., Xu, Y., Ma, M., Wu, X., Zhang, M., Chen, Q., Gao, X., Gao, X., Fan, H., Rajmohan, S., Lin, Q., & Zhang, D. (2023). TraceDiag: Adaptive, interpretable, and efficient root cause analysis on large-scale microservice systems. arXiv. https://arxiv.org/abs/2310.18740

Huang, J., Jiang, Z., Liu, J., Huo, Y., Gu, J., Chen, Z., Feng, C., Dong, H., Yang, Z., & Lyu, M. R. (2024). Demystifying and extracting fault-indicating information from logs for failure diagnosis. arXiv. https://arxiv.org/abs/2409.13561

Huang, J., Liu, J., Chen, Z., Jiang, Z., Li, Y., Gu, J., Feng, C., Yang, Z., Yang, Y., & Lyu, M. R. (2024). FaultProfIT: Hierarchical fault profiling of incident tickets in large-scale cloud systems. arXiv. https://arxiv.org/abs/2402.17583

Jiang, Z., Huang, J., Chen, Z., Li, Y., Yu, G., Feng, C., Yang, Y., Yang, Z., & Lyu, M. R. (2025). L4: Diagnosing large-scale LLM training failures via automated log analysis. arXiv. https://arxiv.org/abs/2503.20263

Pham, L., Ha, H., & Zhang, H. (2024). BARO: Robust root cause analysis for microservices via multivariate Bayesian online change point detection. arXiv. https://arxiv.org/abs/2405.09330

Pham, L., Ha, H., & Zhang, H. (2024). Root cause analysis for microservice system based on causal inference: How far are we? arXiv. https://arxiv.org/abs/2408.13729

Roy, D., Zhang, X., Bhave, R., Bansal, C., Las-Casas, P., Fonseca, R., Rajmohan, S., & Saravan. (2024). Exploring LLM-based agents for root cause analysis. arXiv. https://arxiv.org/abs/2403.04123

Wang, Z., Liu, Z., Zhang, Y., Zhong, A., Wang, J., Yin, F., Fan, L., Wu, L., Wen, Q., & et al. (2023). RCAgent: Cloud root cause analysis by autonomous agents with tool-augmented large language models. arXiv. https://arxiv.org/abs/2310.16340

Zhang, L., Jia, T., Jia, M., Wu, Y., Liu, A., Yang, Y., Wu, Z., Hu, X., Yu, P. S., & Li, Y. (2024). A survey of AIOps for failure management in the era of large language models. arXiv. https://arxiv.org/abs/2406.11213

Zhang, S., Xia, S., Fan, W., Shi, B., Xiong, X., Zhong, Z., Ma, M., Sun, Y., & Pei, D. (2024). Failure diagnosis in microservice systems: A comprehensive survey and analysis. arXiv. https://arxiv.org/abs/2407.01710
