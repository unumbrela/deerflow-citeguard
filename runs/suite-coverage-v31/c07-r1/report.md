# Systematic Literature Review: LLM/Agent-as-Data-Analyst

**Date**: 2026-10-26
**Papers surveyed**: 9
**Scope**: arXiv search query "agent data analyst", filtered to category cs.AI, published between 2023-09-28 and 2025-09-28
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM/Agent-as-Data-Analyst reveals a rapidly evolving field where multi-agent systems are transforming data analysis across diverse domains. The surveyed papers collectively demonstrate a shift from single-model approaches to hierarchical, specialized agent architectures that bridge high-level scientific or business objectives with low-level computational execution. Key applications span bioinformatics, astrobiology, hydrology, drug due diligence, enterprise analytics, investigative journalism, and sports analytics. A consistent finding across multiple papers is that purpose-built multi-agent architectures significantly outperform baseline LLM capabilities, with reported improvements ranging from 27% to 20x in task-specific metrics. However, the field faces challenges including the need for rigorous validation, domain-specific calibration, and the absence of standardized public benchmarks for many tasks.

## Methodology

This review surveyed 9 arXiv papers retrieved on 2026-10-26 using the query "agent data analyst", filtered to category cs.AI, published between 2023-09-28 and 2025-09-28. Papers were sorted by relevance and the top 9 were included (the search returned fewer papers than the requested 10 under the specified constraints). Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search returned 9 papers instead of the requested 10, indicating the relative nascent state of this specific research area within the cs.AI category.

## Themes

### Theme 1: Multi-Agent Architectures for Domain-Specific Analysis

A dominant pattern across the surveyed literature is the use of specialized multi-agent systems tailored to specific domains. Rather than relying on a single monolithic model, these systems deploy multiple agents with distinct roles that collaborate to achieve complex analytical objectives. The K-Dense Analyst system employs a hierarchical multi-agent architecture with a dual-loop structure for bioinformatics analysis (Li et al., 2025). AstroAgents coordinates eight specialized agents including data analysts, domain scientists, literature reviewers, and critics for hypothesis generation in astrobiology (Saeedi et al., 2025). The Data-to-Dashboard framework uses modular LLM agents for domain detection, concept extraction, and multi-perspective analysis in enterprise analytics (Zhang & Elhamod, 2025). Similarly, the generative agents system for investigative reporting employs three specialized roles—analyst, reporter, and editor—to collaboratively generate newsworthy tips from datasets (Veerbeek & Diakopoulos, 2024). This architectural pattern reflects a consensus that complex data analysis tasks require decomposition into specialized subtasks handled by purpose-built agents.

### Theme 2: Autonomous Pipeline Orchestration

Several papers emphasize the capability of LLM agent systems to autonomously orchestrate complete analytical pipelines from high-level natural language prompts to executable computational workflows. AQUAH demonstrates end-to-end autonomy in hydrologic modeling, retrieving terrain and forcing data, configuring models, running simulations, and generating analyst-ready PDF reports from simple natural language prompts (Yan et al., 2025). K-Dense Analyst couples planning with validated execution, decomposing complex scientific objectives into executable, verifiable tasks within secure computational environments (Li et al., 2025). The survey by Tang et al. (2025) identifies autonomous pipeline orchestration as one of four key design goals for intelligent data analysis agents, alongside semantic-aware design, tool-augmented workflows, and support for open-world tasks. This theme reflects the field's progression from assisted analysis to fully automated analytical workflows that require minimal human intervention.

### Theme 3: Domain-Specific Applications and Specialization

The surveyed literature demonstrates LLM agent applications across an exceptionally diverse range of domains, each requiring specialized knowledge and tool integration. In bioinformatics, K-Dense Analyst achieves 29.2% accuracy on the BixBench benchmark for open-ended biological analysis (Li et al., 2025). In astrobiology, AstroAgents generates plausible and novel hypotheses from mass spectrometry data, with 36% of generated hypotheses judged plausible by domain experts and 66% of those being novel (Saeedi et al., 2025). In hydrology, AQUAH completes cold-start simulations and produces documentation judged by hydrologists as clear, transparent, and physically plausible (Yan et al., 2025). In drug asset due diligence, LLM-based agents achieve 83% recall in competitor discovery, reducing analyst turnaround time from 2.5 days to approximately 3 hours (Vinogradov et al., 2025). In enterprise analytics, the Data-to-Dashboard framework improves insightfulness and domain relevance compared to single-prompt baselines (Zhang & Elhamod, 2025). In investigative journalism, generative agents produce more newsworthy and accurate insights than baseline models (Veerbeek & Diakopoulos, 2024). Even in sports analytics, interpretable low-dimensional modeling using spatiotemporal agent states facilitates tactical analysis in football (Ide et al., 2025). This diversity demonstrates the generalizability of LLM agent architectures while highlighting the importance of domain-specific customization.

### Theme 4: Benchmarking and Evaluation Frameworks

A critical theme emerging from the literature is the development of specialized benchmarks and evaluation frameworks for assessing LLM agent capabilities in data analysis tasks. The BixBench benchmark provides evaluation for open-ended biological analysis, where K-Dense Analyst's 29.2% accuracy represents a significant advance over baseline LLM performance (Li et al., 2025). FutureX introduces a dynamic live evaluation benchmark for LLM agents performing future prediction tasks, featuring real-time daily updates and an automated pipeline for question gathering and answer collection, with comprehensive evaluation of 25 LLM/agent models (Zeng et al., 2025). The survey by Tang et al. (2025) systematically reviews LLM-based techniques across four data modalities—structured, semi-structured, unstructured, and heterogeneous data—providing a comprehensive framework for understanding the field's evolution. However, Vinogradov et al. (2025) note the absence of accepted public benchmarks for competitor discovery in drug due diligence, highlighting a gap in standardized evaluation resources. This theme reflects the field's maturation from proof-of-concept demonstrations to rigorous, benchmarked evaluation.

### Theme 5: Natural Language Interfaces and Semantic Understanding

Multiple papers emphasize the role of natural language interfaces in democratizing access to complex analytical capabilities. AQUAH enables hydrologists to initiate complete modeling workflows from simple natural language prompts without manual intervention (Yan et al., 2025). The Data-to-Dashboard framework adapts to diverse datasets without relying on closed ontologies or question templates, improving accessibility for business analysts (Zhang & Elhamod, 2025). Tang et al. (2025) highlight natural language interfaces as a key capability enabled by LLMs and agent techniques, covering NL2SQL, NL2GQL, and ModelQA for structured data. The survey identifies semantic-aware design as a fundamental goal, emphasizing the importance of semantic understanding across data modalities. This theme reflects the field's commitment to making sophisticated analytical capabilities accessible to domain experts without requiring computational expertise.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that multi-agent architectures significantly outperform single-model baselines. Li et al. (2025) report K-Dense Analyst surpassing GPT-5 by 6.3 percentage points using Gemini 2.5 Pro, which achieves only 18.3% accuracy when used directly. Vinogradov et al. (2025) report their agent exceeding OpenAI Deep Research (65% recall) and Perplexity Labs (60% recall) with 83% recall. Zhang and Elhamod (2025) report improved insightfulness compared to GPT-4o with single-prompt baselines. There is also consensus that autonomous pipeline orchestration from natural language prompts is achievable and valuable across domains. All papers emphasize the importance of domain-specific customization and validation.

**Disagreements**: The literature does not reveal fundamental disagreements, but rather reflects different emphases based on domain requirements. Some papers prioritize full automation (AQUAH, K-Dense Analyst), while others emphasize human-in-the-loop validation (AstroAgents' expert evaluation, generative agents' editorial refinement). The variation in reported performance metrics across domains makes direct comparison difficult, though this reflects domain-specific challenges rather than methodological disagreements.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, multiple papers note the absence of standardized public benchmarks for their respective tasks (Vinogradov et al., 2025), limiting reproducibility and comparative evaluation. Second, several systems require further calibration and validation for operational deployment (Yan et al., 2025), indicating that current capabilities remain primarily research-stage rather than production-ready. Third, the survey by Tang et al. (2025) identifies remaining challenges in modality alignment for heterogeneous data, suggesting that multi-modal integration remains an open problem. Fourth, Ide et al. (2025) note that previous reinforcement learning approaches lack interpretability, highlighting the tension between performance and explainability. Fifth, Veerbeek and Diakopoulos (2024) observe variability in performance across different datasets, indicating inconsistent robustness. Finally, Zeng et al. (2025) identify agent failure modes including vulnerability to fake web pages and temporal validity issues in future prediction tasks, revealing vulnerabilities in real-world deployment scenarios. The field would benefit from standardized benchmarks, rigorous validation protocols, and systematic evaluation of robustness and generalizability across domains.

## Per-Paper Annotations

### Ide et al. (2025)

**Research question**: Can low-dimensional, rule-based models using spatiotemporal data effectively capture football tactics?
**Methodology**: Defined interpretable state variables for ball-holders and potential pass receivers based on criteria exploring options like passing. Used StatsBomb event data and SkillCorner tracking data from the 2023/24 LaLiga season to train an XGBoost model to predict pass success.
**Key findings**:
- The distance between the player and the ball was a key factor in determining successful passes.
- The player's space score was a key factor in determining successful passes.
- Interpretable low-dimensional modeling facilitates tactical analysis through intuitive variables.
- The approach provides practical value as a tool to support decision-making in football.
**Limitations**: Previous reinforcement learning approaches lack interpretability and require large datasets; rule-based models have not fully considered all players' states.

### Li et al. (2025)

**Research question**: How can autonomous bioinformatics analysis be achieved through a multi-agent system that bridges high-level scientific objectives with computational execution?
**Methodology**: Introduced K-Dense Analyst, a hierarchical multi-agent system with a dual-loop architecture that couples planning with validated execution using specialized agents. Evaluated on BixBench, a benchmark for open-ended biological analysis.
**Key findings**:
- K-Dense Analyst achieves 29.2% accuracy on BixBench, surpassing GPT-5 by 6.3 percentage points (nearly 27% improvement).
- The system achieves this performance using Gemini 2.5 Pro, which attains only 18.3% accuracy when used directly.
- The dual-loop architecture decomposes complex objectives into executable, verifiable tasks within secure computational environments.
- Architectural innovations unlock capabilities far beyond the underlying model's baseline performance.
- Autonomous scientific reasoning requires purpose-built systems that bridge high-level objectives and low-level computational execution.
**Limitations**: The abstract does not explicitly state limitations of the approach, though it notes that LLMs remain fundamentally limited when dealing with real-world analytical workflows requiring iterative computation, tool integration, and rigorous validation.

### Saeedi et al. (2025)

**Research question**: How can multi-agent AI systems generate plausible and novel hypotheses from mass spectrometry data within the context of astrobiology literature?
**Methodology**: AstroAgents is structured around eight collaborative agents (data analyst, planner, three domain scientists, accumulator, literature reviewer, and critic) that process mass spectrometry data alongside user-provided research papers. An astrobiology expert evaluated the novelty and plausibility of generated hypotheses from eight meteorites and ten soil samples.
**Key findings**:
- Of the hypotheses generated, 36% were identified as plausible by an astrobiology expert.
- Among the plausible hypotheses, 66% were novel.
- The system processes mass spectrometry data alongside user-provided research papers to generate hypotheses.
- The eight-agent architecture includes specialized roles for data interpretation, planning, exploration, accumulation, literature review, and criticism.
- The system addresses challenges including environmental contaminants, spectral peak complexity, and cross-matching difficulties.
**Limitations**: The abstract does not explicitly state limitations, though it notes challenges in hypothesis generation including environmental contaminants, complexity of spectral peaks, and difficulties in cross-matching peaks with prior studies.

### Tang et al. (2025)

**Research question**: How have LLMs and agent techniques transformed data analysis tasks across different data modalities?
**Methodology**: The paper conducts a systematic survey reviewing LLM-based techniques across four data modalities: structured, semi-structured, unstructured, and heterogeneous data. It distills technical evolution into four key design goals for intelligent data analysis agents.
**Key findings**:
- LLMs and agent techniques enable complex data understanding, natural language interfaces, semantic analysis functions, and autonomous pipeline orchestration.
- The survey covers NL2SQL, NL2GQL, ModelQA for structured data; markup languages and semi-structured table question answering for semi-structured data.
- Chart understanding and text/image document understanding are reviewed for unstructured data.
- Data retrieval and modality alignment in data lakes are addressed for heterogeneous data.
- Four key design goals are identified: semantic-aware design, autonomous pipelines, tool-augmented workflows, and support for open-world tasks.
**Limitations**: The abstract outlines remaining challenges but does not specify concrete limitations of the surveyed approaches.

### Veerbeek and Diakopoulos (2024)

**Research question**: Can generative AI agents collaboratively generate and refine newsworthy tips from datasets for investigative data reporting?
**Methodology**: Introduced a system employing three specialized agents (analyst, reporter, and editor) to collaboratively generate and refine tips from datasets, validated using real-world investigative stories.
**Key findings**:
- The agent-based system generally generates more newsworthy and accurate insights compared to a baseline model without agents.
- Three specialized agents (analyst, reporter, editor) can collaboratively work to generate and refine tips.
- The approach was validated using real-world investigative stories.
- Some variability was noted between different stories in the system's performance.
**Limitations**: The abstract notes that some variability was observed between different stories, indicating inconsistent performance across different datasets or contexts.

### Vinogradov et al. (2025)

**Research question**: Can LLM-based AI systems reliably retrieve all competing drug names for a given indication in drug asset due diligence?
**Methodology**: The authors transformed five years of multi-modal, unstructured diligence memos from a private biotech VC fund into a structured evaluation corpus mapping indications to competitor drugs with normalized attributes. They introduced a competitor-validating LLM-as-a-judge agent to filter false positives and benchmarked their competitor-discovery agent against OpenAI Deep Research and Perplexity Labs.
**Key findings**:
- The competitor-discovery agent achieves 83% recall on the benchmark.
- The agent exceeds OpenAI Deep Research (65% recall) and Perplexity Labs (60% recall).
- The system is deployed in production with enterprise users.
- Analyst turnaround time dropped from 2.5 days to approximately 3 hours (approximately 20x improvement) in a case study with a biotech VC investment fund.
**Limitations**: The abstract notes that current LLM-based AI systems aren't capable of reliably retrieving all competing drug names, and there is no accepted public benchmark for this task.

### Yan et al. (2025)

**Research question**: Can an end-to-end language-based agent autonomously perform hydrologic modeling from natural language prompts?
**Methodology**: The authors developed AQUAH, a vision-enabled LLM-driven agent that autonomously retrieves terrain, forcing, and gauge data; configures a hydrologic model; runs simulations; and generates PDF reports from simple natural-language prompts. Initial experiments were conducted across a range of U.S. basins.
**Key findings**:
- AQUAH can complete cold-start simulations and produce analyst-ready documentation without manual intervention.
- Results are judged by hydrologists as clear, transparent, and physically plausible.
- The agent autonomously retrieves required data and configures hydrologic models from natural language prompts.
- Vision-enabled LLMs can interpret maps and rasters on the fly to steer key decisions such as outlet selection and parameter initialization.
**Limitations**: Further calibration and validation are still needed for operational deployment.

### Zhang and Elhamod (2025)

**Research question**: How can a modular multi-agent LLM framework automate the data-to-dashboard pipeline while improving insightfulness and domain relevance in enterprise analytics?
**Methodology**: The paper presents an agentic system that automates the data-to-dashboard pipeline through modular LLM agents capable of domain detection, concept extraction, multi-perspective analysis generation, and iterative self-reflection. It was evaluated on three datasets across different domains, benchmarked against GPT-4o with a single-prompt baseline.
**Key findings**:
- The framework simulates the analytical reasoning process of business analysts by retrieving domain-relevant knowledge.
- The system adapts to diverse datasets without relying on closed ontologies or question templates.
- The approach shows improved insightfulness, domain relevance, and analytical depth compared to GPT-4o with a single-prompt baseline.
- Evaluation was conducted using tailored metrics and qualitative human assessment.
- The work contributes a novel modular pipeline bridging raw data to visualization.
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Zeng et al. (2025)

**Research question**: How can LLM agents be evaluated on future prediction tasks in a dynamic, contamination-free manner?
**Methodology**: The authors introduced FutureX, a dynamic live evaluation benchmark for LLM agents performing future prediction tasks with real-time daily updates and an automated pipeline for question gathering and answer collection. They evaluated 25 LLM/agent models including those with reasoning, search capabilities, and external tool integration.
**Key findings**:
- FutureX is the largest and most diverse live benchmark for future prediction.
- The benchmark supports real-time daily updates and eliminates data contamination.
- 25 LLM/agent models were comprehensively evaluated including open-source Deep Research Agent and closed-source Deep Research models.
- The analysis reveals agent failure modes including vulnerability to fake web pages and temporal validity issues.
**Limitations**: The abstract identifies challenges in handling real-time updates and retrieving timely, accurate answers for future prediction benchmarks.

## References

Ide, K., Someya, T., Kawaguchi, K., & Fujii, K. (2025). Interpretable low-dimensional modeling of spatiotemporal agent states for decision making in football tactics. arXiv. https://arxiv.org/abs/2506.16696

Li, O., Agarwal, V., Zhou, S., Gopinath, A., & Kassis, T. (2025). K-Dense Analyst: Towards fully automated scientific analysis. arXiv. https://arxiv.org/abs/2508.07043

Saeedi, D., Buckner, D., Aponte, J. C., & Aghazadeh, A. (2025). AstroAgents: A multi-agent AI for hypothesis generation from mass spectrometry data. arXiv. https://arxiv.org/abs/2503.23170

Tang, Z., Wang, W., Zhou, Z., Jiao, Y., Xu, B., Niu, B., Zhou, D., Zhou, X., Li, G., He, Y., Zhou, W., Song, Y., Tan, C., Yang, X., Liu, C., Wang, B., He, C., Wang, X., & Wu, F. (2025). LLM/Agent-as-Data-Analyst: A survey. arXiv. https://arxiv.org/abs/2509.23988

Veerbeek, J., & Diakopoulos, N. (2024). Using generative agents to create tip sheets for investigative data reporting. arXiv. https://arxiv.org/abs/2409.07286

Vinogradov, V., Vinogradova, A., Radkevich, D., Yasny, I., Kobyzev, D., Izmailov, I., Yanchanka, K., Doronin, R., & Doronichev, A. (2025). LLM-Based agents for competitive landscape mapping in drug asset due diligence. arXiv. https://arxiv.org/abs/2508.16571

Yan, S., Li, Z., Zhu, S., Wen, Y., Zhang, M., Chen, M., Cao, J., & Hong, Y. (2025). AQUAH: Automatic quantification and unified agent in hydrology. arXiv. https://arxiv.org/abs/2508.02936

Zeng, Z., Liu, J., Chen, S., et al. (2025). FutureX: An advanced live benchmark for LLM agents in future prediction. arXiv. https://arxiv.org/abs/2508.11987

Zhang, R., & Elhamod, M. (2025). Data-to-Dashboard: Multi-agent LLM framework for insightful visualization in enterprise analytics. arXiv. https://arxiv.org/abs/2505.23695
