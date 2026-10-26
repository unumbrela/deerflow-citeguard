# Systematic Literature Review: AI Scientists

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "AI scientists", category cs.AI, published between 2023-10-27 and 2025-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on AI Scientists reveals a rapidly evolving field focused on automating scientific discovery through large language models and agentic systems. The surveyed papers collectively demonstrate significant progress toward fully autonomous research capabilities, with recent systems achieving peer-review acceptance at academic venues. However, critical bottlenecks remain in implementation capability, tool integration, and quality assurance mechanisms. The field is characterized by converging efforts to build infrastructure platforms (ToolUniverse, aiXiv), establish benchmarks (BAISBench, Turing Tests), and address fundamental limitations in execution and verification. Despite notable achievements, researchers caution that current AI Scientists have yet to produce groundbreaking discoveries comparable to human experts, and systematic pitfalls in automated workflows pose risks to research integrity.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "AI scientists", filtered to category cs.AI, published between 2023-10-27 and 2025-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Automated Scientific Discovery Systems

A dominant thread across the literature involves building end-to-end systems capable of autonomous scientific research. The foundational work by Lu et al. (2024) introduced "The AI Scientist," demonstrating that frontier LLMs can generate novel research ideas, write code, execute experiments, visualize results, and produce full scientific papers at less than $15 per paper. Building on this, Yamada et al. (2025) developed AI Scientist-v2 using agentic tree search, achieving the first fully AI-generated paper to exceed human acceptance thresholds at an ICLR workshop. These systems represent a shift from human-assisted to fully automated discovery, though Xie et al. (2025) note that despite acceptance at workshops, AI Scientists have yet to produce groundbreaking achievements in computer science.

### Theme 2: Infrastructure and Platform Development

Multiple papers emphasize the need for standardized infrastructure to support AI Scientist development. Gao et al. (2025) present ToolUniverse, an open platform unifying 2,700+ scientific tools and 130+ research skills through natural language declarations and typed schemas. Similarly, Zhang et al. (2025) introduce aiXiv, a next-generation open-access ecosystem enabling research proposals and papers to be submitted, reviewed, and iteratively refined by both human and AI scientists. These platforms address fragmentation in the publication ecosystem and provide API interfaces for seamless integration of heterogeneous AI scientists. The convergence on platform-building reflects recognition that isolated systems cannot scale without shared tooling and quality-control mechanisms.

### Theme 3: Evaluation and Benchmarking

Establishing rigorous evaluation frameworks emerges as a critical research direction. Yin (2024) proposes seven "Turing Tests" for AI Scientists, spanning historical discoveries from heliocentric models to Huffman coding, arguing that passing these would indicate significant progress toward AI scientists surpassing human experts. Luo et al. (2025) introduce BAISBench for evaluating AI scientists on omics data-driven biological discovery, comparing performance against graduate-level bioinformaticians. These benchmarks serve dual purposes: characterizing current capabilities and guiding development toward more capable systems. The emphasis on evaluation reflects growing maturity in the field as researchers move beyond proof-of-concept demonstrations to systematic capability assessment.

### Theme 4: Implementation and Execution Gaps

A recurring concern across the literature involves the gap between research ideation and rigorous implementation. Zhu et al. (2025) identify implementation capability as the fundamental bottleneck, finding that AI Scientists lack execution capabilities needed for rigorous experiments despite progress in paper generation. Their systematic assessment of 28 research papers from five advanced AI Scientist systems reveals a significant gap between current capabilities and human-level scientific discovery. Xie et al. (2025) echo this concern, noting that while LLM-based systems are "taking the lead," identifiable limitations prevent world-changing discoveries. This theme highlights that idea generation alone is insufficient without robust verification and experimental execution.

### Theme 5: Reliability and Quality Assurance

Recent work identifies critical failure modes in AI Scientist systems that threaten research integrity. Luo et al. (2025) document four potential pitfalls: inappropriate benchmark selection, data leakage, metric misuse, and post-hoc selection bias. Their assessment of two prominent open-source systems reveals failures across a spectrum of severity that can be easily overlooked without close examination. They recommend journals and conferences mandate submission of workflow artifacts alongside papers for transparency. Fu et al. (2025) explore theoretical convergence, finding that AI Scientists tend to converge on theories as more systems are provided, but exhibit strong seed dependence in training dynamics. These findings underscore the need for traceability and accountability mechanisms as automation increases.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that AI Scientists have made substantial progress but fall short of fully autonomous, groundbreaking discovery. Multiple papers document acceptance of AI-generated papers at workshops and conferences (Lu et al., 2024; Yamada et al., 2025; Xie et al., 2025), yet all acknowledge significant remaining gaps. There is consensus on the need for standardized platforms and tooling (Gao et al., 2025; Zhang et al., 2025) and rigorous evaluation frameworks (Yin, 2024; Luo et al., 2025).

**Disagreements**: Papers diverge on the primary bottleneck: Zhu et al. (2025) emphasize implementation capability as the fundamental constraint, while others focus on platform infrastructure or evaluation gaps. There is also variation in optimism about timelines: some papers frame AI Scientists as already "taking the lead" (Xie et al., 2025), while others emphasize they "fail without strong implementation capability" (Zhu et al., 2025) or "fall short of fully autonomous biological discovery" (Luo et al., 2025).

## Gaps and Open Questions

The collective literature reveals several unaddressed gaps. First, none of the papers provide detailed analysis of the computational resources required for AI Scientist operations beyond Lu et al.'s (2024) mention of "$15 per paper" — scalability at population level remains unexamined. Second, while multiple papers call for platform development, none address governance questions around AI-authored research, including authorship attribution and intellectual property. Third, the biological domain receives attention (Luo et al., 2025), but other scientific domains beyond machine learning lack dedicated benchmarks. Finally, Luo et al. (2025) note that access to trace logs enables failure detection, but systematic standards for what constitutes adequate transparency remain undeveloped.

## Per-Paper Annotations

### Fu et al. (2025)

**Research question**: When two AI models are trained on the same scientific task, do they learn the same theory or different theories?
**Methodology**: The authors propose MASS, using Hamiltonian-Lagrangian neural networks as AI Scientists trained on standard physics problems, aggregating results across many training seeds to simulate different AI scientist configurations.
**Key findings**:
- AI scientists tend to converge in the theories they learn as more systems are provided in training data
- AI scientists sometimes form distinct groups corresponding to different theories
- AI scientists switch from learning a Hamiltonian theory in simple setups to a Lagrangian formulation when more complex systems are introduced
- Strong seed dependence exists in training dynamics and final learned weights
- The neural networks can aid interpretability and can be applied to higher dimensional problems
**Limitations**: Not stated in abstract

### Gao et al. (2025)

**Research question**: How can AI scientists be built more easily through a shared platform that unifies tools, data, and analyses?
**Methodology**: The authors present ToolUniverse, an open platform that standardizes AI-tool interactions through natural language declarations, typed schemas, and backend-agnostic invocation formats across 2,700+ scientific tools and 130+ research skills, with automatic interface refinement and tool composition capabilities.
**Key findings**:
- ToolUniverse standardizes how AI scientists identify and call tools through an AI-tool interaction standard
- The platform applies its standard to more than 2,700 scientific tools and over 130 research skills spanning machine learning models, datasets, APIs, and scientific packages
- ToolUniverse automatically refines tool interfaces, generates new tools from natural language descriptions, and composes tools into agentic workflows
- Case studies demonstrate ToolUniverse was used to create AI scientists that carried out end-to-end analyses in target assessment, chemical strategy, and clinical-trial safety
- The open-source ToolUniverse is available at https://aiscientist.tools
**Limitations**: Not stated in abstract

### Luo et al. (2025) [BAISBench]

**Research question**: To what extent can AI scientists extract meaningful biological insights from real experimental omics data?
**Methodology**: The authors introduce BAISBench, a benchmark for evaluating AI scientists on real single-cell transcriptomic datasets comprising cell type annotation across 15 expert-labeled datasets and 193 multiple-choice questions derived from 41 published single-cell studies, with comparison to six graduate-level bioinformaticians.
**Key findings**:
- Current AI scientists fall short of fully autonomous biological discovery
- AI scientists already demonstrate substantial potential in supporting data-driven biological research
- BAISBench serves as a practical benchmark for characterizing current capabilities and limitations of AI scientists in biological research
- The benchmark provides a human performance baseline through graduate-level bioinformaticians completing the same tasks
- BAISBench can guide development of more capable AI scientists and help biologists identify AI systems for real-world research workflows
**Limitations**: Not stated in abstract

### Zhu et al. (2025)

**Research question**: What is the fundamental bottleneck preventing AI Scientists from producing groundbreaking achievements in computer science?
**Methodology**: The authors conduct extensive quantitative evaluation using existing benchmarks in complex engineering tasks and systematically assess 28 research papers generated by five advanced AI Scientist systems to identify the implementation gap.
**Key findings**:
- The fundamental bottleneck for AI Scientists lies in their capability to execute the requisite verification procedures
- Current AI Scientist systems lack the execution capabilities needed to execute rigorous experiments and produce high-quality scientific papers
- Despite progress with research reports gaining acceptance at ICLR 2025 workshop and ACL 2025, AI Scientists have yet to produce groundbreaking achievements in computer science
- There is a significant implementation gap between current AI Scientist capabilities and human-level scientific discovery
- The paper calls for the community to bridge the implementation gap
**Limitations**: Not stated in abstract

### Xie et al. (2025)

**Research question**: How far are AI scientists from changing the world and reshaping the scientific research paradigm?
**Methodology**: The paper provides a prospect-driven survey review that comprehensively analyzes current achievements of AI Scientist systems. It identifies key bottlenecks and critical components required for scientific agents capable of producing ground-breaking discoveries.
**Key findings**:
- LLM-based AI Scientist systems are now taking the lead in scientific research
- AI-generated research papers have been accepted at the ICLR 2025 workshop
- Current AI Scientist systems have identifiable limitations that need to be understood
- The survey aims to clarify where we are, what is missing, and what the ultimate goals for scientific AI should be
**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can we address the challenges of disseminating AI-generated research content in a fragmented and closed publication ecosystem?
**Methodology**: The paper introduces aiXiv, a next-generation open-access platform with a multi-agent architecture that allows research proposals and papers to be submitted, reviewed, and iteratively refined by both human and AI scientists. Extensive experiments were conducted to demonstrate the platform's reliability and robustness.
**Key findings**:
- Traditional journals and conferences rely on human peer review, making them difficult to scale for AI-generated research
- Existing preprint servers like arXiv lack rigorous quality-control mechanisms
- aiXiv provides API and MCP interfaces for seamless integration of heterogeneous human and AI scientists
- aiXiv significantly enhances the quality of AI-generated research proposals and papers after iterative revising and reviewing
- The work lays groundwork for a next-generation open-access ecosystem for AI scientists
**Limitations**: Not stated in abstract

### Yin (2024)

**Research question**: Can an AI agent conduct scientific research independently and make groundbreaking discoveries without relying on human-generated knowledge?
**Methodology**: The paper proposes seven benchmark tests inspired by historical scientific developments to evaluate an AI agent's ability to make groundbreaking discoveries in various domains. The AI agent is provided with interactive libraries or datasets specific to each problem without access to human knowledge about the target discoveries.
**Key findings**:
- Seven benchmark tests are proposed: inferring heliocentric model, discovering laws of motion, deriving differential equations for vibrating strings, inferring Maxwell's equations, inventing numerical methods for initial value problems, discovering Huffman coding, and developing efficient sorting algorithms
- These tests serve as intermediate milestones assessing AI's ability to make discoveries that were groundbreaking in their time
- Passing the majority of these seven tests would indicate significant progress toward building an AI scientist
- The ultimate goal is creating an AI scientist capable of making novel and impactful discoveries surpassing the best human experts
**Limitations**: Not stated in abstract

### Luo et al. (2025) [Pitfalls]

**Research question**: What are the potential failure modes in contemporary AI scientist systems that could undermine the integrity and reliability of their research outputs?
**Methodology**: The paper identifies four potential failure modes in AI scientist systems and designs controlled experiments that isolate each failure mode. An assessment of two prominent open-source AI scientist systems was conducted to examine these risks.
**Key findings**:
- Four potential failure modes identified: inappropriate benchmark selection, data leakage, metric misuse, and post-hoc selection bias
- Assessment of two prominent open-source AI scientist systems reveals several failures across a spectrum of severity
- These failures can be easily overlooked in practice without close examination
- Access to trace logs and code from the full automated workflow enables far more effective detection of failures than examining the final paper alone
- The authors recommend journals and conferences mandate submission of workflow artifacts alongside papers for transparency and accountability
**Limitations**: Not stated in abstract

### Yamada et al. (2025)

**Research question**: Can an agentic AI system autonomously produce peer-review-accepted scientific papers through end-to-end automated discovery?
**Methodology**: The system uses progressive agentic tree-search methodology managed by a dedicated experiment manager agent, iteratively formulating hypotheses, designing experiments, analyzing data, and authoring manuscripts. A Vision-Language Model feedback loop refines figure content and aesthetics.
**Key findings**:
- The AI Scientist-v2 eliminates reliance on human-authored code templates and generalizes across diverse ML domains
- Three fully autonomous manuscripts were submitted to an ICLR workshop
- One manuscript exceeded the average human acceptance threshold, marking the first fully AI-generated paper to navigate peer review successfully
- The system iteratively formulates hypotheses, designs/executes experiments, analyzes/visualizes data, and autonomously authors scientific manuscripts
- The code has been open-sourced to foster future development of autonomous scientific discovery technologies
**Limitations**: Not stated in abstract

### Lu et al. (2024)

**Research question**: Can frontier large language models perform independent scientific research and communicate findings through a fully automated discovery framework?
**Methodology**: A comprehensive framework enables frontier LLMs to generate novel research ideas, write code, execute experiments, visualize results, write full scientific papers, and run a simulated review process for evaluation. An automated reviewer achieves near-human performance in evaluating paper scores.
**Key findings**:
- The AI Scientist generates novel research ideas, writes code, executes experiments, visualizes results, and writes full scientific papers
- Each paper is developed at a cost of less than $15 per paper
- The system was applied to three ML subfields: diffusion modeling, transformer-based language modeling, and learning dynamics
- Generated papers can exceed the acceptance threshold at a top ML conference as judged by the automated reviewer
- The automated reviewer achieves near-human performance in evaluating paper scores
**Limitations**: Not stated in abstract

## References

Fu, X., Liu, Z., & Tegmark, M. (2025). Do two AI scientists agree? arXiv. https://arxiv.org/abs/2504.02822

Gao, S., Zhu, R., Sui, P., Kong, Z., Aldogom, S., Huang, Y., Noori, A., Shamji, R., Parvataneni, K., Tsiligkaridis, T., & Zitnik, M. (2025). ToolUniverse: An open platform for democratizing AI scientists. arXiv. https://arxiv.org/abs/2509.23426

Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., & Ha, D. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. arXiv. https://arxiv.org/abs/2408.06292

Luo, E., Jia, J., Xiong, Y., Li, X., Guo, X., Yu, B., Hao, M., Wei, L., & Zhang, X. (2025). Benchmarking AI scientists for omics data driven biological discovery. arXiv. https://arxiv.org/abs/2505.08341

Luo, Z., Kasirzadeh, A., & Shah, N. B. (2025). The more you automate, the less you see: Hidden pitfalls of AI scientist systems. arXiv. https://arxiv.org/abs/2509.08713

Xie, Q., Weng, Y., Zhu, M., Shen, F., Huang, S., Lin, Z., Zhou, J., Mao, Z., Yang, Z., Yang, L., Wu, J., & Zhang, Y. (2025). How far are AI scientists from changing the world? arXiv. https://arxiv.org/abs/2507.23276

Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search. arXiv. https://arxiv.org/abs/2504.08066

Yin, X. (2024). "Turing tests" for an AI scientist. arXiv. https://arxiv.org/abs/2405.13352

Zhang, P., Hu, X., Huang, G., Qi, Y., Zhang, H., Li, X., Song, J., Luo, J., Li, Y., Yin, S., Dai, C., Jiang, E. H., Zhou, X., Yin, Z., Yuan, B., Dong, J., Su, G., Qiao, G., Tang, H., Du, A., et al. (2025). aiXiv: A next-generation open access ecosystem for scientific discovery generated by AI scientists. arXiv. https://arxiv.org/abs/2508.15126

Zhu, M., Weng, Y., Zhu, M., Xie, Q., Lin, Z., Yang, L., & Zhang, Y. (2025). AI scientists fail without strong implementation capability. arXiv. https://arxiv.org/abs/2506.01372
