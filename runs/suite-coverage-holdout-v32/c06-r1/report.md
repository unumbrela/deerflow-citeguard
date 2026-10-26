# Systematic Literature Review: AI Scientists

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "AI scientists", category cs.AI, published between 2023-10-27 and 2025-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on AI Scientists reveals a rapidly evolving field focused on automating scientific discovery through agentic systems. The surveyed papers collectively demonstrate significant progress: AI-generated research papers have successfully passed peer review at ICLR 2025 workshops, marking a historic milestone. However, critical bottlenecks remain, particularly in implementation capability, verification procedures, and potential failure modes that could undermine research integrity. The field is transitioning from proof-of-concept demonstrations to addressing scalability, standardization, and trustworthiness concerns.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "AI scientists", filtered to category cs.AI, published between 2023-10-27 and 2025-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Automated Scientific Discovery Systems

The core thread across the literature is the development of fully automated AI Scientist systems capable of conducting end-to-end scientific research. The foundational work by Lu et al. (2024) introduced "The AI Scientist," demonstrating that frontier LLMs could generate novel research ideas, write code, execute experiments, and produce full scientific papers at minimal cost. Building on this, Yamada et al. (2025) developed "The AI Scientist-v2," which eliminated reliance on human-authored code templates and achieved the first fully AI-generated paper to pass peer review at an ICLR workshop.

These systems employ agentic architectures with progressive tree-search methodologies, experiment managers, and enhanced AI reviewer components integrating vision-language models for iterative refinement. The progression from template-dependent to fully autonomous systems marks a critical evolution in the field.

### Theme 2: Benchmarking and Evaluation Frameworks

A second major theme is the development of rigorous benchmarks to assess AI Scientist capabilities. Yin (2024) proposed seven "Turing Tests" inspired by historical scientific discoveries, requiring AI agents to make groundbreaking discoveries without access to prior human knowledge about the targets. These tests span domains from inferring heliocentric models to discovering Huffman coding.

Luo et al. (2025) introduced BAISBench, specifically targeting biological discovery from omics data, comprising cell type annotation across 15 expert-labeled datasets and 193 multiple-choice questions from published studies. This benchmark provides human performance baselines and addresses the gap in existing benchmarks that fail to reflect realistic data-driven biological research.

### Theme 3: Implementation Capability Bottlenecks

Multiple papers converge on identifying implementation capability as the fundamental bottleneck. Zhu et al. (2025) provide quantitative evidence that current AI Scientists lack the execution capabilities needed for rigorous experiments, despite generating research reports accepted at ICLR 2025 workshops and ACL 2025. Their systematic evaluation of 28 papers from five advanced AI Scientist systems reveals that verification procedures remain the critical limiting factor.

Xie et al. (2025) echo this concern in their prospect-driven survey, mapping current achievements while identifying key bottlenecks preventing AI Scientists from producing ground-breaking discoveries comparable to automated scientific tools in other domains.

### Theme 4: Platform Standardization and Democratization

The literature shows growing emphasis on standardization and accessibility. Gao et al. (2025) present ToolUniverse, an open platform standardizing AI-tool interaction through natural language declarations and typed schemas across 2,700+ scientific tools and 130+ research skills. This platform enables any language or reasoning model to function as an AI Scientist, democratizing access to automated research capabilities.

Zhang et al. (2025) address the dissemination challenge with aiXiv, a next-generation open-access ecosystem enabling research proposals and papers to be submitted, reviewed, and iteratively refined by both human and AI scientists. Their experiments demonstrate significant quality enhancement through iterative revising and reviewing.

### Theme 5: Failure Modes and Trustworthiness

A critical emerging theme concerns hidden pitfalls and failure modes. Luo et al. (2025) identify four potential failure modes: inappropriate benchmark selection, data leakage, metric misuse, and post-hoc selection bias. Their controlled experiments assessing two prominent open-source AI Scientist systems reveal failures across a spectrum of severity that can be easily overlooked without close scrutiny of internal workflows.

This work advocates for mandatory submission of workflow artifacts alongside AI-generated papers to ensure transparency, accountability, and reproducibility—a policy recommendation gaining traction as AI-generated research proliferates.

### Theme 6: Theory Agreement and Convergence

Fu et al. (2025) investigate a foundational question: when two AI models are trained on the same scientific task, do they learn the same theory or different theories? Using Hamiltonian-Lagrangian neural networks as AI Scientists, they find that AI scientists tend to converge on theories as more systems are provided in training data, but sometimes form distinct groups corresponding to different theoretical frameworks. This work reveals strong seed dependence in training dynamics and theory switching behavior when problem complexity increases.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key findings. First, AI Scientists have achieved demonstrable progress, with papers accepted at ICLR 2025 workshops and ACL 2025 (Yamada et al., 2025; Zhu et al., 2025; Xie et al., 2025). Second, implementation capability and verification procedures represent the fundamental bottleneck preventing groundbreaking achievements (Zhu et al., 2025; Xie et al., 2025). Third, current benchmarks inadequately reflect realistic research scenarios, necessitating new evaluation frameworks (Yin, 2024; Luo et al., 2025).

**Disagreements**: The literature shows limited direct disagreement, reflecting the field's early stage. However, there is implicit tension between optimism about AI Scientists' potential (Lu et al., 2024; Yamada et al., 2025) and cautionary findings about failure modes and limitations (Luo et al., 2025; Zhu et al., 2025). While some papers emphasize breakthrough achievements, others highlight systemic vulnerabilities requiring attention before widespread deployment.

## Gaps and Open Questions

The collective literature reveals several unaddressed gaps:

1. **Limited domain diversity**: Most AI Scientist systems focus on machine learning research; few address other scientific domains beyond biology (Luo et al., 2025).

2. **Long-term autonomy**: Current systems demonstrate single-paper generation but lack evidence of sustained, open-ended research programs building cumulative knowledge.

3. **Human-AI collaboration**: While platforms like ToolUniverse and aiXiv support hybrid workflows, systematic studies of optimal human-AI scientist collaboration patterns remain absent.

4. **Ethical and safety considerations**: None of the surveyed papers extensively address ethical implications of autonomous research generation or potential misuse.

5. **Reproducibility infrastructure**: While Luo et al. (2025) advocate for workflow artifact submission, no standardized infrastructure exists for archiving and verifying AI-generated research processes.

6. **Theory convergence mechanisms**: Fu et al. (2025) identify theory switching behavior but do not provide mechanisms for ensuring AI Scientists converge on correct rather than merely consistent theories.

## Per-Paper Annotations

### Fu et al. (2025)

**Research question**: When two AI models are trained on the same scientific task, do they learn the same theory or different theories?
**Methodology**: The authors propose MASS and use Hamiltonian-Lagrangian neural networks as AI Scientists, trained on standard physics problems across many seeds to simulate different AI scientist configurations. They mechanistically interpret and quantify theory agreement using these neural networks.
**Key findings**:
- AI scientists tend to converge in the theories they learn as more systems are provided in training data
- AI scientists sometimes form distinct groups corresponding to different theories
- AI scientists switch from learning a Hamiltonian theory in simple setups to a Lagrangian formulation when more complex systems are introduced
- Strong seed dependence of training dynamics and final learned weights controls the rise and fall of relevant theories
- The neural networks can aid interpretability and can be applied to higher dimensional problems
**Limitations**: Not stated in abstract

### Gao et al. (2025)

**Research question**: How can AI scientists be made more accessible and standardized across different models and workflows?
**Methodology**: The authors present ToolUniverse, an open platform that standardizes AI-tool interaction through natural language declarations, typed schemas, and backend-agnostic invocation formats across 2,700+ scientific tools and 130+ research skills. They demonstrate the platform through case studies in target assessment, chemical strategy, and clinical-trial safety.
**Key findings**:
- ToolUniverse standardizes how AI scientists identify and call tools through an AI-tool interaction standard
- The platform applies its standard to more than 2,700 scientific tools and over 130 research skills
- It automatically refines tool interfaces, generates new tools from natural language, optimizes tool specifications, and composes tools into agentic workflows
- Case studies demonstrate ToolUniverse was used to create AI scientists that carried out end-to-end analyses in target assessment, chemical strategy, and clinical-trial safety
- The platform works across any language or reasoning model, including open- and closed-weight models
**Limitations**: Not stated in abstract

### Luo, E. et al. (2025)

**Research question**: To what extent can AI scientists extract meaningful biological insights from real experimental omics data?
**Methodology**: The authors introduce BAISBench, a benchmark comprising cell type annotation across 15 expert-labeled datasets and 193 multiple-choice questions derived from 41 published single-cell studies. They evaluated several AI scientists and compared against a human baseline of six graduate-level bioinformaticians.
**Key findings**:
- Current AI scientists fall short of fully autonomous biological discovery
- AI scientists already demonstrate substantial potential in supporting data-driven biological research
- BAISBench serves as a practical benchmark for characterizing current capabilities and limitations of AI scientists in biological research
- The benchmark provides a human performance baseline for comparison
- Existing benchmarks fail to reflect realistic, data-driven biological research, which BAISBench addresses
**Limitations**: Not stated in abstract

### Luo, Z. et al. (2025)

**Research question**: What are the potential failure modes in contemporary AI scientist systems that could undermine the integrity, reliability, and trustworthiness of their research outputs?
**Methodology**: Identification of four potential failure modes and design of controlled experiments to isolate each failure mode, followed by assessment of two prominent open-source AI scientist systems to examine risks in their internal workflows.
**Key findings**:
- Four potential failure modes identified: inappropriate benchmark selection, data leakage, metric misuse, and post-hoc selection bias
- Assessment of two prominent open-source AI scientist systems reveals presence of several failures across a spectrum of severity
- These failures can be easily overlooked in practice without close scrutiny of internal workflows
- Access to trace logs and code from the full automated workflow enables far more effective detection of failures than examining the final paper alone
- Journals and conferences should mandate submission of workflow artifacts alongside AI-generated papers to ensure transparency, accountability, and reproducibility
**Limitations**: Not stated in abstract

### Lu et al. (2024)

**Research question**: Can frontier large language models be developed into agents capable of conducting fully automated scientific research and discovering new knowledge independently?
**Methodology**: The authors present a comprehensive framework for fully automatic scientific discovery, introducing The AI Scientist system that generates novel research ideas, writes code, executes experiments, visualizes results, writes full scientific papers, and runs a simulated review process for evaluation. The system was applied to three distinct subfields of machine learning: diffusion modeling, transformer-based language modeling, and learning dynamics.
**Key findings**:
- The AI Scientist can generate novel research ideas and develop them into full papers at a cost of less than $15 per paper
- An automated reviewer was designed and validated, achieving near-human performance in evaluating paper scores
- The system can produce papers that exceed the acceptance threshold at a top machine learning conference as judged by the automated reviewer
- The approach can be repeated to iteratively develop ideas in an open-ended fashion, acting like the human scientific community
- The code is open-sourced to enable further development of automated scientific discovery
**Limitations**: Not stated in abstract

### Yin (2024)

**Research question**: Can an AI agent conduct scientific research independently and make groundbreaking discoveries without relying on human-generated knowledge?
**Methodology**: Proposal of seven benchmark "Turing tests" inspired by historical scientific developments, evaluating AI agents' ability to make discoveries in various domains using interactive libraries or datasets without access to prior human knowledge about the target discoveries.
**Key findings**:
- Seven benchmark tests are proposed: inferring heliocentric model, discovering laws of motion, deriving differential equations for vibrating strings, inferring Maxwell's equations, inventing numerical methods for initial value problems, discovering Huffman coding, and developing efficient sorting algorithms
- Tests ensure validity by providing domain-specific interactive libraries or datasets without access to human knowledge containing information about target discoveries
- Passing the majority of these seven tests would indicate significant progress towards building an AI scientist
- The tests serve as intermediate milestones assessing AI agent's ability to make discoveries that were groundbreaking in their time
**Limitations**: Not stated in abstract

### Yamada et al. (2025)

**Research question**: Can an agentic AI system autonomously conduct end-to-end scientific discovery and produce peer-review-accepted workshop papers without human-authored code templates?
**Methodology**: The authors developed The AI Scientist-v2, an end-to-end agentic system using progressive agentic tree-search methodology managed by a dedicated experiment manager agent. The system iteratively formulates hypotheses, designs and executes experiments, analyzes and visualizes data, and authors scientific manuscripts, with an enhanced AI reviewer component integrating a Vision-Language Model feedback loop.
**Key findings**:
- The AI Scientist-v2 eliminates reliance on human-authored code templates and generalizes effectively across diverse machine learning domains
- Three fully autonomous manuscripts were submitted to a peer-reviewed ICLR workshop
- One manuscript achieved scores exceeding the average human acceptance threshold, marking the first fully AI-generated paper to successfully navigate peer review
- The system enhances the AI reviewer component by integrating a VLM feedback loop for iterative refinement of figures
- The code has been open-sourced to foster future development of autonomous scientific discovery technologies
**Limitations**: Not stated in abstract

### Xie et al. (2025)

**Research question**: How far are AI scientists from changing the world and reshaping the scientific research paradigm?
**Methodology**: A prospect-driven survey review that comprehensively analyzes current achievements of AI Scientist systems, identifying key bottlenecks and critical components required for scientific agents capable of producing ground-breaking discoveries.
**Key findings**:
- LLM-based AI Scientist systems are now taking the lead in scientific research
- AI-generated research papers have been accepted at the ICLR 2025 workshop
- Current AI Scientist systems have identifiable limitations and bottlenecks
- The survey maps where we are, what is missing, and what the ultimate goals for scientific AI should be
**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can we address the challenges of disseminating AI-generated research content in a fragmented and closed publication ecosystem?
**Methodology**: Introduction and experimental evaluation of aiXiv, a next-generation open-access platform with multi-agent architecture that enables research proposals and papers to be submitted, reviewed, and iteratively refined by both human and AI scientists.
**Key findings**:
- Traditional journals and conferences rely on human peer review, making them difficult to scale for AI-generated research
- Existing preprint servers like arXiv lack rigorous quality-control mechanisms
- aiXiv provides API and MCP interfaces for seamless integration of heterogeneous human and AI scientists
- Experiments demonstrate aiXiv significantly enhances the quality of AI-generated research proposals and papers after iterative revising and reviewing
- The platform lays groundwork for a next-generation open-access ecosystem for AI scientists
**Limitations**: Not stated in abstract

### Zhu et al. (2025)

**Research question**: What is the fundamental bottleneck preventing AI Scientists from producing groundbreaking achievements in computer science?
**Methodology**: The authors conducted extensive quantitative evidence from existing benchmarks in complex engineering tasks and systematically evaluated 28 research papers generated by five advanced AI Scientist systems to identify the implementation gap.
**Key findings**:
- The fundamental bottleneck for AI Scientists lies in their capability to execute requisite verification procedures
- Current AI Scientist systems lack the execution capabilities needed to execute rigorous experiments and produce high-quality scientific papers
- Despite progress, AI Scientist has yet to produce a groundbreaking achievement in computer science on par with automated scientific tools
- Generated research reports have gained acceptance at ICLR 2025 workshop and ACL 2025, suggesting substantial progress
- The paper calls for the community to bridge the implementation gap
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

Zhu, M., Xie, Q., Weng, Y., Wu, J., Lin, Z., Yang, L., & Zhang, Y. (2025). AI scientists fail without strong implementation capability. arXiv. https://arxiv.org/abs/2506.01372
