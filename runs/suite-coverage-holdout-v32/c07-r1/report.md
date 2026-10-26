# Systematic Literature Review: LLM/Agent-as-Data-Analyst

**Date**: 2026-10-26
**Papers surveyed**: 8
**Scope**: arXiv query "agent data analyst", category cs.AI, published between 2023-09-28 and 2025-09-27
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature reveals a rapidly emerging field where LLM-based agents are being deployed as autonomous data analysts across diverse domains including scientific research, business intelligence, journalism, and sports analytics. Eight papers published between late 2023 and 2025 demonstrate that multi-agent architectures consistently outperform single-model approaches, with specialized agent roles (analyst, planner, critic, domain expert) enabling complex analytical workflows that bridge high-level objectives with low-level computational execution. Key achievements include 29.2% accuracy on open-ended biological analysis benchmarks (surpassing GPT-5 by 27%), 83% recall in competitive landscape mapping (exceeding Deep Research and Perplexity), and autonomous completion of hydrologic simulations from natural language prompts. The field shows strong convergence around hierarchical, multi-agent designs with validation loops, though operational deployment remains limited by calibration needs and vulnerability to hallucination in unstructured environments.

## Methodology

This review surveyed 8 arXiv papers retrieved on 2026-10-26 using the query "agent data analyst", filtered to category cs.AI, published between 2023-09-28 and 2025-09-27. Papers were sorted by relevance and the top 8 were included (the search returned fewer than the requested 10 papers under these constraints). Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The requested 10 papers could not be met; only 8 papers matched the constraints, indicating this is an emerging but still niche research area.

## Themes

### Theme 1: Multi-Agent Hierarchical Architectures

A dominant pattern across the surveyed literature is the shift from single-model prompting to hierarchical multi-agent systems with specialized roles. Five of eight papers explicitly employ multi-agent architectures where distinct agents handle planning, execution, domain expertise, literature review, and criticism. Li et al. (2025) introduce K-Dense Analyst with a dual-loop architecture coupling planning with validated execution using specialized agents, achieving 29.2% accuracy on BixBench—nearly 27% improvement over GPT-5's baseline. Saeedi et al. (2025) structure AstroAgents around eight collaborative agents including a data analyst, planner, three domain scientists, accumulator, literature reviewer, and critic for hypothesis generation from mass spectrometry data. Vinogradov et al. (2025) deploy LLM-based agents with a dedicated LLM-as-a-judge agent to filter false positives in drug asset due diligence. Zhang and Elhamod (2025) present modular LLM agents capable of domain detection, concept extraction, multi-perspective analysis, and iterative self-reflection for automated dashboard generation. Yan et al. (2025) use vision-enabled LLMs to autonomously perform hydrologic modeling. This convergence suggests that architectural innovations—not just model improvements—are critical for unlocking autonomous analytical capabilities.

### Theme 2: Domain-Specific Agent Deployment

The literature demonstrates strong domain-specific customization rather than general-purpose analytical agents. Each surveyed system is purpose-built for its target domain: bioinformatics (Li et al., 2025), investigative journalism (Veerbeek & Diakopoulos, 2024), astrobiology and mass spectrometry (Saeedi et al., 2025), enterprise analytics dashboards (Zhang & Elhamod, 2025), pharmaceutical due diligence (Vinogradov et al., 2025), hydrology (Yan et al., 2025), and football tactics analysis (Ide et al., 2025). This specialization extends beyond surface-level prompts to deep integration with domain-specific data formats (mass spectrometry, terrain rasters, tracking data), evaluation metrics (BixBench for biology, recall benchmarks for drug competition), and expert validation workflows (hydrologist evaluation, astrobiology expert assessment). The pattern suggests that successful agent-as-analyst systems require domain-specific scaffolding rather than generic analytical capabilities.

### Theme 3: Benchmarking and Evaluation Frameworks

A significant thread across the literature is the development of domain-specific benchmarks and evaluation frameworks to measure agent performance. Li et al. (2025) evaluate on BixBench, a comprehensive benchmark for open-ended biological analysis. Zeng et al. (2025) introduce FutureX, described as the largest and most diverse live benchmark for future prediction, supporting real-time daily updates with automated pipelines for question gathering and answer collection, evaluating 25 LLM/agent models. Vinogradov et al. (2025) use recall metrics for competitor discovery, achieving 83% recall compared to 65% for OpenAI Deep Research and 60% for Perplexity Labs. Zhang and Elhamod (2025) employ tailored evaluation metrics measuring insightfulness, domain relevance, and analytical depth through both automated metrics and qualitative human assessment. This focus on rigorous, domain-specific benchmarking distinguishes the agent-as-analyst literature from more general LLM evaluation work.

### Theme 4: Bridging High-Level Objectives with Low-Level Execution

A recurring research question across multiple papers is how to bridge the gap between high-level analytical objectives and low-level computational execution. Li et al. (2025) frame this explicitly, asking "How can autonomous systems bridge the gap between high-level scientific objectives and low-level computational execution in bioinformatics analysis?" Their system decomposes complex objectives into executable, verifiable tasks within secure computational environments. Yan et al. (2025) demonstrate autonomous completion of hydrologic simulations from simple natural-language prompts, with the agent retrieving required data, configuring models, running simulations, and generating self-contained PDF reports without manual intervention. Zhang and Elhamod (2025) automate the data-to-dashboard pipeline, simulating the analytical reasoning process of business analysts through modular agents. This theme reflects a fundamental challenge in agent design: translating abstract analytical goals into concrete, executable workflows while maintaining verification and validation throughout the process.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several points. First, multi-agent architectures consistently outperform single-model baselines—Li et al. (2025) report 29.2% vs. 18.3% for the underlying model alone; Vinogradov et al. (2025) achieve 83% recall vs. 65% for Deep Research; Veerbeek and Diakopoulos (2024) find agent-based systems generate more newsworthy and accurate insights than baseline models. Second, all papers emphasize the need for specialized, domain-specific design rather than general-purpose analytical agents. Third, there is consensus that validation loops, self-reflection mechanisms, and expert evaluation are essential components of successful analytical agents.

**Disagreements**: The literature does not show fundamental disagreements, likely reflecting the early-stage nature of the field. However, there is variation in the degree of autonomy claimed: Yan et al. (2025) report fully autonomous hydrologic simulation "without manual intervention," while Saeedi et al. (2025) note that only 36% of generated hypotheses were judged plausible by experts, suggesting significant human oversight remains necessary. Li et al. (2025) achieve 29.2% accuracy on BixBench, indicating substantial room for improvement even in the best-performing systems.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, operational deployment remains limited—Yan et al. (2025) explicitly state "further calibration and validation are still needed for operational deployment" in hydrology. Second, hallucination and false positives remain significant challenges, requiring dedicated LLM-as-a-judge agents (Vinogradov et al., 2025) and expert validation (Saeedi et al., 2025). Third, Zeng et al. (2025) identify vulnerability to fake web pages and temporal validity as significant challenges for agents performing future-oriented reasoning. Fourth, Veerbeek and Diakopoulos (2024) note "variability between different stories," suggesting inconsistent performance across cases that is not yet well understood. Finally, the relatively small number of papers (8 instead of the requested 10) and their concentration in 2025 suggest this is an emerging field where best practices, evaluation standards, and architectural patterns are still crystallizing.

## Per-Paper Annotations

### Ide et al. (2025)

**Research question**: Can low-dimensional, rule-based models using spatiotemporal data effectively capture football tactics for decision-making support?
**Methodology**: The authors defined interpretable state variables for ball-holders and potential pass receivers based on criteria exploring passing options. They trained an XGBoost model using StatsBomb event data and SkillCorner tracking data from the 2023/24 LaLiga season to predict pass success, with key variables identified through discussions with a manager.
**Key findings**:
- Low-dimensional, rule-based models can effectively capture football tactics using interpretable variables
- Distance between the player and the ball is a key factor in determining successful passes
- Player's space score is another critical factor for pass success prediction
- The approach provides practical value as a decision-making support tool for tactical analysis
**Limitations**: not stated in abstract

### Li et al. (2025)

**Research question**: How can autonomous systems bridge the gap between high-level scientific objectives and low-level computational execution in bioinformatics analysis?
**Methodology**: The authors introduce K-Dense Analyst, a hierarchical multi-agent system with a dual-loop architecture that couples planning with validated execution using specialized agents to decompose complex objectives into executable, verifiable tasks within secure computational environments. The system was evaluated on BixBench, a comprehensive benchmark for open-ended biological analysis.
**Key findings**:
- K-Dense Analyst achieves 29.2% accuracy on BixBench, surpassing GPT-5 by 6.3 percentage points (nearly 27% improvement).
- The system achieves this performance using Gemini 2.5 Pro, which attains only 18.3% accuracy when used directly.
- Architectural innovations unlock capabilities far beyond the underlying model's baseline performance.
- Autonomous scientific reasoning requires purpose-built systems that bridge high-level scientific objectives and low-level computational execution.
**Limitations**: not stated in abstract

### Saeedi et al. (2025)

**Research question**: How can multi-agent AI systems analyze mass spectrometry data within the context of existing astrobiology literature and generate plausible hypotheses regarding the emergence of life on Earth?
**Methodology**: The authors introduce AstroAgents, a large language model-based multi-agent AI system structured around eight collaborative agents: a data analyst, a planner, three domain scientists, an accumulator, a literature reviewer, and a critic. The system processes mass spectrometry data alongside user-provided research papers, with an astrobiology expert evaluating the novelty and plausibility of generated hypotheses from eight meteorites and ten soil samples.
**Key findings**:
- Of the hypotheses generated, 36% were identified as plausible by an expert evaluator.
- Among the plausible hypotheses, 66% were novel.
- The system successfully processes mass spectrometry data and generates hypotheses by interpreting data, delegating exploration, collecting and deduplicating hypotheses, reviewing literature, and critically evaluating results.
**Limitations**: not stated in abstract

### Veerbeek and Diakopoulos (2024)

**Research question**: Can generative AI agents collaboratively generate and refine newsworthy tips from datasets for investigative data reporting?
**Methodology**: The authors developed a system employing three specialized agents—an analyst, a reporter, and an editor—to collaboratively generate and refine tips from datasets. The approach was validated using real-world investigative stories.
**Key findings**:
- The agent-based system generally generates more newsworthy and accurate insights compared to a baseline model without agents.
- Some variability was noted between different stories.
- Generative AI has potential to provide leads for investigative data reporting.
**Limitations**: Some variability was noted between different stories, suggesting inconsistent performance across cases.

### Vinogradov et al. (2025)

**Research question**: Can LLM-based AI agents reliably retrieve all competing drug names and extract canonical attributes for competitive landscape mapping in drug asset due diligence?
**Methodology**: The authors describe and benchmark a competitor-discovery component within an agentic AI system for drug asset due diligence. They used LLM-based agents to transform five years of multi-modal, unstructured diligence memos from a private biotech VC fund into a structured evaluation corpus, and introduced a competitor validating LLM-as-a-judge agent to filter false positives. The system was evaluated on recall metrics and deployed in production with a case study at a biotech VC investment fund.
**Key findings**:
- The competitor-discovery agent achieves 83% recall on the benchmark.
- The system exceeds OpenAI Deep Research (65%) and Perplexity Labs (60%) in recall performance.
- In production, analyst turnaround time dropped from 2.5 days to approximately 3 hours (approximately 20x improvement).
- The LLM-as-a-judge agent successfully filters false positives to maximize precision and suppress hallucinations.
**Limitations**: not stated in abstract

### Yan et al. (2025)

**Research question**: Can a vision-enabled language-based agent autonomously perform hydrologic modeling from natural language prompts to produce analyst-ready documentation?
**Methodology**: The authors developed AQUAH, an end-to-end language-based agent that uses vision-enabled large language models to interpret maps and rasters, retrieve terrain/forcing/gauge data, configure and run hydrologic models, and generate PDF reports. Experiments were conducted across multiple U.S. basins with cold-start simulations evaluated by hydrologists.
**Key findings**:
- AQUAH can autonomously complete hydrologic simulations from simple natural-language prompts without manual intervention
- The agent successfully retrieves required data, configures models, runs simulations, and generates self-contained PDF reports
- Hydrologists judged the results as clear, transparent, and physically plausible
- Vision-enabled LLMs can effectively interpret maps and rasters to steer key modeling decisions
**Limitations**: Further calibration and validation are still needed for operational deployment.

### Zeng et al. (2025)

**Research question**: How can LLM agents be evaluated on future prediction tasks given the challenges of real-time updates and timely answer retrieval?
**Methodology**: The authors introduced FutureX, a dynamic live benchmark supporting real-time daily updates with an automated pipeline for question gathering and answer collection. They evaluated 25 LLM/agent models including those with reasoning and search capabilities, analyzing failure modes and performance pitfalls in future-oriented tasks.
**Key findings**:
- FutureX is the largest and most diverse live benchmark for future prediction, eliminating data contamination through automated pipelines
- 25 LLM/agent models were comprehensively evaluated including open-source and closed-source Deep Research models
- Agents show vulnerability to fake web pages in future prediction tasks
- Temporal validity is a significant challenge for agents performing future-oriented reasoning
**Limitations**: not stated in abstract

### Zhang and Elhamod (2025)

**Research question**: How can modular LLM agents automate the data-to-dashboard pipeline while simulating the analytical reasoning process of business analysts?
**Methodology**: The authors present an agentic system that automates the data-to-dashboard pipeline through modular LLM agents capable of domain detection, concept extraction, multi-perspective analysis generation, and iterative self-reflection. The system was evaluated on three datasets across different domains and benchmarked against GPT-4o with a single-prompt baseline.
**Key findings**:
- The approach shows improved insightfulness compared to GPT-4o with a single-prompt baseline.
- The system demonstrates better domain relevance than the baseline.
- The framework achieves greater analytical depth as measured by tailored evaluation metrics and qualitative human assessment.
- The modular pipeline successfully bridges the path from raw data to visualization without relying on closed ontologies or question templates.
**Limitations**: not stated in abstract

## References

Ide, K., Someya, T., Kawaguchi, K., & Fujii, K. (2025). Interpretable low-dimensional modeling of spatiotemporal agent states for decision making in football tactics. arXiv. https://arxiv.org/abs/2506.16696

Li, O., Agarwal, V., Zhou, S., Gopinath, A., & Kassis, T. (2025). K-Dense Analyst: Towards fully automated scientific analysis. arXiv. https://arxiv.org/abs/2508.07043

Saeedi, D., Buckner, D., Aponte, J. C., & Aghazadeh, A. (2025). AstroAgents: A multi-agent AI for hypothesis generation from mass spectrometry data. arXiv. https://arxiv.org/abs/2503.23170

Veerbeek, J., & Diakopoulos, N. (2024). Using generative agents to create tip sheets for investigative data reporting. arXiv. https://arxiv.org/abs/2409.07286

Vinogradov, V., Vinogradova, A., Radkevich, D., Yasny, I., Kobyzev, D., Izmailov, I., Yanchanka, K., Doronin, R., & Doronichev, A. (2025). LLM-Based agents for competitive landscape mapping in drug asset due diligence. arXiv. https://arxiv.org/abs/2508.16571

Yan, S., Li, Z., Zhu, S., Wen, Y., Zhang, M., Chen, M., Cao, J., & Hong, Y. (2025). AQUAH: Automatic quantification and unified agent in hydrology. arXiv. https://arxiv.org/abs/2508.02936

Zeng, Z., Liu, J., Chen, S., He, T., Liao, Y., Tian, Y., Wang, J., Wang, Z., Yang, Y., Yin, L., Yin, M., Zhu, Z., Cai, T., Chen, Z., Chen, J., Du, Y., Gao, X., Guo, J., Hu, L., Jiao, J., et al. (2025). FutureX: An advanced live benchmark for LLM agents in future prediction. arXiv. https://arxiv.org/abs/2508.11987

Zhang, R., & Elhamod, M. (2025). Data-to-Dashboard: Multi-Agent LLM framework for insightful visualization in enterprise analytics. arXiv. https://arxiv.org/abs/2505.23695
