# Systematic Literature Review: Goal-Driven Root Cause Analysis

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "root cause analysis" in cs.SE category, published between 2023-10-22 and 2025-10-21
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in automated root cause analysis (RCA) for software systems, particularly cloud infrastructure, microservices, and distributed systems. The surveyed literature reveals a field undergoing rapid transformation driven by large language models (LLMs) and autonomous agents, moving from traditional statistical and causal inference methods toward LLM-augmented diagnostic frameworks. Ten papers published between October 2023 and March 2025 demonstrate consistent progress in automating failure diagnosis through tool-augmented agents, Bayesian change point detection, causal inference, and log-based analysis. The collective work indicates that while significant advances have been made in accuracy and automation, challenges remain in handling incomplete information, achieving robustness across diverse system architectures, and reducing dependency on manual workflows.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "root cause analysis", filtered to category cs.SE, published between 2023-10-22 and 2025-10-21. Papers were identified through arXiv search with citation expansion, screened for relevance to goal-driven and systematic approaches to root cause analysis, and the top 10 were included based on co-citation centrality scores. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening flow**: 50 papers identified by search, 69 added from reference expansion, 30 shortlisted, 30 screened, 10 included (4 from references).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review focuses on software engineering applications and may not capture RCA advances in adjacent fields.

## Themes

### Theme 1: LLM-Based Autonomous Agents for Root Cause Analysis

A dominant trend in recent RCA research is the integration of large language models as autonomous agents capable of tool-augmented reasoning and decision-making. Wang et al. (2023) introduced RCAgent, a framework that enhances LLMs with self-consistency mechanisms, context management, and domain knowledge integration to perform cloud root cause analysis without relying on manual workflows. Their approach demonstrated consistent superiority over ReAct baselines across all RCA dimensions and has been deployed in Alibaba Cloud's Real-time Compute Platform for Apache Flink.

Building on this foundation, Roy et al. (2024) empirically evaluated ReAct agents equipped with retrieval tools on production incidents from Microsoft, finding that agents achieve highly increased factual accuracy while performing competitively with strong retrieval and reasoning baselines. The work explored whether incorporating incident discussions as additional inputs would improve performance, though results showed no significant gains. These papers collectively establish that LLM-based agents can overcome limitations of prior RCA approaches by dynamically collecting diagnostic information through tool access, enabling free-form data collection while maintaining comprehensive analysis capabilities.

### Theme 2: Log-Based Failure Diagnosis and Information Extraction

Multiple papers address the challenge of extracting actionable diagnostic information from system logs, recognizing that logs are often the most accessible diagnostic artifact for engineers. Huang et al. (2024) developed LoFI, a two-stage approach that performs coarse-grained filtering followed by fine-grained extraction of fault-indicating descriptions and parameters using pre-trained language models with novel prompt-based tuning. Their method achieved substantial improvements over baselines, including a 25.8-37.9 F1 point advantage over ChatGPT, and has been successfully deployed at CloudA.

Jiang et al. (2025) extended log-based diagnosis to the specialized domain of large-scale LLM training failures, conducting an empirical study of 428 failures and identifying three distinct log patterns: cross-job, spatial, and temporal. Their L4 framework automatically extracts failure-indicating information from training logs, outperforming existing approaches in identifying failure-indicating logs and localizing faulty nodes. Shan et al. (2024) focused specifically on configuration errors, proposing an LLM-based two-stage strategy that enables end-users without source code access to localize root-cause configuration properties using logs alone, achieving 99.91% accuracy on Hadoop. These works demonstrate that logs, when properly processed with modern language models, can provide highly accurate diagnostic information accessible to diverse user populations.

### Theme 3: Causal Inference and Statistical Methods for Microservices

Traditional statistical and causal inference methods remain important for RCA, particularly in microservice architectures where component interactions create complex dependency graphs. Pham et al. (2024a) proposed BARO, which integrates anomaly detection with root cause analysis using Multivariate Bayesian Online Change Point Detection to model dependencies in multivariate time-series metrics. Their approach is notably less sensitive to anomaly detection accuracy compared to existing works and consistently outperforms state-of-the-art methods on benchmark microservice systems.

In a comprehensive evaluation of the field, Pham et al. (2024b) assessed nine causal discovery methods and twenty-one RCA methods, finding that no single method performs optimally across all situations, with each approach falling short in either effectiveness, efficiency, or parameter sensitivity. Ding et al. (2023) introduced TraceDiag, which uses reinforcement learning to learn an interpretable pruning policy for service dependency graphs, eliminating redundant components before applying causal-based root cause identification. This framework, integrated into Microsoft M365 Exchange, significantly reduces human effort while improving RCA efficiency and accuracy. These papers collectively indicate that while causal inference methods face challenges in generalizability, innovations in pruning strategies and Bayesian approaches continue to advance the state of the art.

### Theme 4: Knowledge-Enhanced and Context-Aware Diagnosis

Recent work emphasizes the importance of incorporating additional knowledge sources and execution context to improve RCA accuracy, particularly when diagnostic information is incomplete or ambiguous. Li et al. (2025) proposed COCA, which extracts relevant code snippets and reconstructs execution paths from issue reports to provide comprehensive execution context for LLMs. By constructing prompts that combine historical issue reports with profiled code knowledge, COCA enables LLMs to generate detailed root cause summaries and localize responsible components, achieving 28.3% improvement in root cause localization and 22.0% improvement in summarization over existing methods.

This knowledge-enhancement approach addresses a critical limitation identified across multiple papers: the challenge of handling incomplete or ambiguous information in failure reports. By providing LLMs with structured code knowledge and execution context, these methods enable more accurate diagnosis even when surface-level diagnostic signals are insufficient. The robust generalizability of COCA across various large language models suggests that knowledge-enhancement strategies may be broadly applicable across different system architectures and failure types.

### Theme 5: Comprehensive Surveys and Field Assessment

The maturation of the RCA field is evidenced by comprehensive surveys that synthesize existing work and identify future directions. Zhang et al. (2024) conducted an exhaustive survey reviewing 98 scientific papers from 2003 to present, examining fundamental concepts, system architecture, and problem statements in microservice failure diagnosis. Their work compiles publicly available datasets, toolkits, and evaluation metrics while providing in-depth discussion of best practices and future research directions, highlighting that cascading failures in microservice systems present unique challenges due to independent deployment and dynamic interactions.

This survey tradition serves both to consolidate field knowledge and to identify gaps where further research is needed. The comprehensive nature of these surveys, spanning two decades of research, provides valuable context for understanding how recent LLM-based approaches build upon and diverge from earlier statistical and rule-based methods.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the conclusion that automation through LLM-based agents and tool-augmented reasoning represents a significant advance over manual or semi-automated RCA workflows. There is broad agreement that logs constitute a critical diagnostic artifact, with successful deployments reported across industry settings (Alibaba Cloud, Microsoft, CloudA, Platform-X). The surveyed papers consistently demonstrate that integrating domain knowledge—whether through code snippets, historical issue reports, or system metrics—substantially improves diagnostic accuracy. All deployed systems report positive outcomes from industry integration, suggesting practical viability of the proposed approaches.

**Disagreements**: The literature reveals tension between LLM-based approaches and traditional causal inference methods. While Pham et al. (2024b) found that no single causal inference method performs optimally and that performance on synthetic datasets does not reflect real-system performance, LLM-based papers report consistently high accuracy without extensively comparing to causal baselines. Roy et al. (2024) found that incorporating incident discussions did not yield significant improvements, suggesting that additional context does not always translate to better performance—a finding that contrasts with the knowledge-enhancement philosophy underlying COCA. The field has not yet reached consensus on optimal evaluation metrics or benchmark datasets, with papers reporting accuracy, F1 scores, and deployment success using different measurement frameworks.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are addressed only in full papers or that the field lacks systematic discussion of failure modes and boundary conditions. Second, while multiple papers report successful industry deployments, there is limited discussion of generalizability across different organizational contexts, system scales, or failure types beyond those studied. Third, the comparative effectiveness of LLM-based versus causal inference approaches remains unclear, as papers typically evaluate against limited baselines rather than conducting comprehensive comparisons across methodological families.

The reliance on arXiv preprints means that peer-reviewed validation of claims is pending for many recent contributions. Additionally, while surveys compile available datasets and metrics, the field would benefit from standardized benchmarks that enable direct comparison of LLM-based, statistical, and hybrid approaches. Finally, the computational cost and latency of LLM-based approaches compared to traditional methods is not systematically addressed, representing a practical consideration for production deployment that warrants further investigation.

## Per-Paper Annotations

### Ding et al. (2023)

**Research question**: How can root cause analysis be made more efficient and accurate for large-scale microservice systems with hundreds of components?

**Methodology**: The authors propose TraceDiag, an end-to-end RCA framework using reinforcement learning to learn an interpretable pruning policy for service dependency graphs, which eliminates redundant components before applying a causal-based method for root cause identification.

**Key findings**:
- TraceDiag significantly improves RCA efficiency by automatically pruning redundant components from service dependency graphs.
- The learned pruning policy is interpretable and fully adaptive to new RCA instances.
- TraceDiag demonstrates superior performance compared to state-of-the-art RCA approaches on real data from Microsoft Exchange.
- Integration into Microsoft M365 Exchange resulted in significant reliability improvements.
- The framework considerably reduces human effort required for root cause analysis.

**Limitations**: Not stated in abstract.

### Huang et al. (2024)

**Research question**: How can fault-indicating information be automatically extracted from logs to reduce the labor-intensive manual investigation required for failure diagnosis?

**Methodology**: The authors developed LoFI, a two-stage approach that first performs coarse-grained filtering to collect fault-related logs based on semantic similarity, then leverages a pre-trained language model with a novel prompt-based tuning method to extract fine-grained fault-indicating descriptions and parameters.

**Key findings**:
- LoFI outperforms all baseline methods by a significant margin with an absolute improvement of 25.8-37.9 in F1 over the best baseline (ChatGPT).
- Engineers typically prioritize fault-indicating descriptions (abnormal system events) and fault-indicating parameters (associated entities) for diagnosis.
- The approach has been successfully deployed at CloudA with positive user study results.
- The method effectively recognizes fault-indicating information from extensive runtime log data.

**Limitations**: Not stated in abstract.

### Jiang et al. (2025)

**Research question**: How can automated log analysis effectively diagnose failures in large-scale LLM training to reduce resource and time waste?

**Methodology**: The authors conducted an empirical study of 428 LLM training failures from Platform-X (May 2023–April 2024), identifying three distinct log patterns (cross-job, spatial, temporal). They then developed L4, a log-based framework that automatically extracts failure-indicating information from training logs.

**Key findings**:
- Hardware and user faults are the predominant root causes of LLM training failures.
- Existing log-based diagnostic methods are inadequate for handling LLM training logs.
- LLM training logs exhibit three distinct patterns: cross-job, spatial, and temporal.
- L4 outperforms existing approaches in identifying failure-indicating logs and localizing faulty nodes.
- L4 has been successfully deployed in Platform-X, demonstrating effectiveness in accurate and efficient failure diagnosis.

**Limitations**: Not stated in abstract.

### Li et al. (2025)

**Research question**: How can root cause analysis for distributed system failures be improved when issue reports contain incomplete or ambiguous information?

**Methodology**: The authors propose COCA, a code knowledge enhanced root cause analysis approach that extracts relevant code snippets and reconstructs execution paths from issue reports to provide comprehensive execution context. COCA constructs prompts combining historical issue reports with profiled code knowledge to enable LLMs to generate detailed root cause summaries and localize responsible components.

**Key findings**:
- COCA significantly outperforms existing methods on datasets from five real-world distributed systems.
- COCA achieves a 28.3% improvement in root cause localization compared to existing methods.
- COCA achieves a 22.0% improvement in root cause summarization compared to existing methods.
- COCA demonstrates robust generalizability across various large language models.

**Limitations**: Not stated in abstract.

### Pham et al. (2024a)

**Research question**: How can root cause analysis for microservices be made robust to inaccurate anomaly detection results?

**Methodology**: The authors propose BARO, an end-to-end approach integrating anomaly detection and root cause analysis that uses Multivariate Bayesian Online Change Point Detection to model dependencies in multivariate time-series metrics data, combined with a novel nonparametric statistical hypothesis testing technique for identifying root causes.

**Key findings**:
- BARO consistently outperforms state-of-the-art approaches in both anomaly detection and root cause analysis.
- The approach is less sensitive to the accuracy of anomaly detection compared to existing works.
- Multivariate Bayesian Online Change Point Detection enables more accurate anomaly detection by modeling dependencies within time-series metrics.
- The method was validated on three popular benchmark microservice systems.

**Limitations**: Not stated in abstract.

### Pham et al. (2024b)

**Research question**: What is the current effectiveness and efficiency of causal inference-based root cause analysis methods for microservice systems?

**Methodology**: The authors conducted a comprehensive evaluation of nine causal discovery methods and twenty-one root cause analysis methods to assess their effectiveness, efficiency, and sensitivity to parameters.

**Key findings**:
- No single method performs optimally across all situations.
- Each method tends to fall short in either effectiveness, efficiency, or shows sensitivity to specific parameters.
- Performance on synthetic datasets does not accurately reflect performance in real systems.
- There remains significant room for improvement in causal inference-based root cause analysis.
- The study identifies possible future work directions based on experimental findings.

**Limitations**: Not stated in abstract.

### Roy et al. (2024)

**Research question**: Can LLM-based agents equipped with retrieval tools overcome the limitations of prior RCA approaches by dynamically collecting diagnostic information?

**Methodology**: The authors conducted empirical evaluation of a ReAct agent with retrieval tools on an out-of-distribution dataset of production incidents from Microsoft, then extended the evaluation by incorporating incident discussions and conducted a case study equipping the agent with tools for external diagnostic services.

**Key findings**:
- ReAct agents perform competitively with strong retrieval and reasoning baselines while achieving highly increased factual accuracy.
- Incorporating discussions associated with incident reports as additional inputs does not yield significant performance improvements.
- Agents can overcome limitations of prior work by accessing external diagnostic services through tools.
- The approach enables dynamic collection of diagnostic information such as logs, metrics, and databases.

**Limitations**: Not stated in abstract.

### Shan et al. (2024)

**Research question**: How can end-users without source code access localize configuration error root causes using logs and Large Language Models?

**Methodology**: The authors conducted a preliminary study on challenges and opportunities of log-based configuration error localization, then proposed an LLM-based two-stage strategy and implemented LogConfigLocalizer tool, evaluated on Hadoop with comparison to variants and baseline tools.

**Key findings**:
- This is the first work to localize root-cause configuration properties for end-users using LLMs and logs.
- LogConfigLocalizer achieves an average accuracy of 99.91% on Hadoop.
- Logs are easily accessible to most end-users, making them valuable for configuration error diagnosis.
- Different phases of the methodology demonstrate effectiveness and necessity compared to variants.
- A practical case study validates the methodology's effectiveness and feasibility.

**Limitations**: Not stated in abstract.

### Wang et al. (2023)

**Research question**: How can large language models be enhanced with tool-augmentation and autonomous agent capabilities to improve cloud root cause analysis without relying on manual workflows?

**Methodology**: The authors developed RCAgent, a tool-augmented LLM autonomous agent framework that runs on an internally deployed model. The framework incorporates Self-Consistency for action trajectories, context management, stabilization methods, and domain knowledge integration, then evaluated it against ReAct across multiple RCA tasks using both automated metrics and human evaluations.

**Key findings**:
- RCAgent demonstrates consistent superiority over ReAct across all aspects of root cause analysis including predicting root causes, solutions, evidence, and responsibilities.
- The framework performs well on both tasks covered and uncovered by current rules.
- RCAgent enables free-form data collection and comprehensive analysis with tools while maintaining privacy awareness.
- The system has been successfully integrated into Alibaba Cloud's Real-time Compute Platform for Apache Flink diagnosis workflow.

**Limitations**: Not stated in abstract.

### Zhang et al. (2024)

**Research question**: What are the fundamental concepts, current best practices, and future directions in failure diagnosis for microservice systems?

**Methodology**: The authors conducted an exhaustive survey reviewing 98 scientific papers from 2003 to present, examining fundamental concepts, system architecture, problem statements, and providing qualitative analysis of dimensions, best practices, and future directions.

**Key findings**:
- Microservice systems present unique failure diagnosis challenges due to independent deployment and dynamic interactions.
- Cascading failures can negatively impact operational efficiency and user experience.
- The survey compiles publicly available datasets, toolkits, and evaluation metrics for practitioners.
- Extensive research has achieved significant results in fault diagnosis for microservice stability and reliability.
- The work provides in-depth discussion of current best practices and future research directions.

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
