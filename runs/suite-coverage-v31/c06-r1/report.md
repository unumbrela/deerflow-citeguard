# Systematic Literature Review: AI Scientists

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "AI scientists", category cs.AI, published between 2023-10-27 and 2025-10-27
**Citation format**: APA 7th edition

## Executive Summary

The literature on AI Scientists represents an emerging and rapidly evolving field focused on automating scientific discovery through autonomous AI systems. The surveyed papers collectively reveal a field in transition: from early benchmark proposals and foundational frameworks (2024) to integrated closed-loop systems capable of producing peer-review-accepted workshop papers (2025). Key developments include the demonstration of fully AI-generated papers passing peer review (Yamada et al., 2025), comprehensive surveys mapping the methodological landscape (Tie et al., 2025; Xie et al., 2025), and critical examinations of failure modes and limitations (Zhu et al., 2025; Luo et al., 2025). The field is characterized by optimism about AI Scientists' potential to reshape scientific research, tempered by recognition of significant implementation gaps, evaluation challenges, and the need for standardized platforms and rigorous quality control mechanisms.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "AI scientists", filtered to category cs.AI, published between 2023-10-27 and 2025-10-27. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Autonomous Scientific Discovery and Closed-Loop Systems

A central thread across the literature is the development of end-to-end AI Scientist systems capable of performing the complete scientific workflow from hypothesis generation to manuscript preparation. The AI Scientist-v2 system represents a significant milestone, producing the first entirely AI-generated peer-review-accepted workshop paper through progressive agentic tree-search methodology (Yamada et al., 2025). This system eliminates reliance on human-authored code templates and generalizes across diverse machine learning domains, demonstrating that autonomous scientific discovery is achievable at the workshop level.

The field has evolved from foundational modules (2022-2023) to integrated closed-loop systems (2024), and now to systems emphasizing scalability, impact, and human-AI collaboration (2025-present) (Tie et al., 2025). This progression reflects increasing sophistication in how AI systems approach scientific tasks, moving from isolated capability demonstrations to comprehensive workflows that emulate human scientific practice.

### Theme 2: Benchmarking and Evaluation Frameworks

Multiple papers address the critical challenge of evaluating AI Scientists' capabilities and limitations. Yin (2024) proposes seven benchmark "Turing tests for an AI scientist" inspired by historical scientific discoveries, including inferring the heliocentric model, discovering laws of motion, and deriving Maxwell's equations. These benchmarks assess whether AI agents can make groundbreaking discoveries without relying on human-generated knowledge, providing a clear bar for measuring progress toward human-level scientific capability.

Luo et al. (2025) introduce BAISBench, a benchmark specifically for omics data-driven biological discovery, evaluating AI scientists on real single-cell transcriptomic datasets through cell type annotation and scientific discovery questions. Their benchmark includes comparison to human performance (six graduate-level bioinformaticians), establishing that current AI scientists fall short of fully autonomous biological discovery but demonstrate substantial potential.

### Theme 3: Implementation Gaps and Failure Modes

A critical theme emerging from the literature is the recognition of significant limitations in current AI Scientist systems. Zhu et al. (2025) identify an "implementation gap" as the fundamental bottleneck, arguing that AI Scientists fail without strong execution capabilities needed to perform rigorous experiments and produce high-quality scientific papers. Despite demonstrating capabilities for independent discovery, current systems lack the execution infrastructure to achieve groundbreaking achievements comparable to automated scientific tools.

Luo et al. (2025) identify four specific failure modes: inappropriate benchmark selection, data leakage, metric misuse, and post-hoc selection bias. Their assessment of two prominent open-source AI scientist systems reveals several failures across a spectrum of severity that can be easily overlooked when examining only final papers. They emphasize that access to trace logs and code from the full automated workflow enables far more effective failure detection than examining the final paper alone.

### Theme 4: Infrastructure and Platform Development

Several papers focus on building infrastructure to support AI Scientists' work. ToolUniverse (Gao et al., 2025) presents an open platform that standardizes AI-tool interaction through declared purposes, typed schemas, and backend-agnostic invocation formats, applied to over 2,700 scientific tools and 130+ research skills. The platform automatically refines tool interfaces, generates new tools from natural language, and composes tools into agentic workflows, working across both open- and closed-weight models.

aiXiv (Zhang et al., 2025) proposes a next-generation open-access ecosystem with a multi-agent architecture enabling both human and AI scientists to submit, review, and iteratively refine research proposals and papers. The platform addresses limitations of traditional journals (difficult to scale, reluctant to accept AI-generated content) and existing preprint servers (lack rigorous quality control), demonstrating through extensive experiments that iterative reviewing and revising significantly enhances AI-generated research quality.

### Theme 5: Consensus and Agreement Among AI Scientists

An intriguing theoretical question explored in the literature is whether AI Scientists converge on similar theories when trained on the same scientific tasks. Fu et al. (2025) investigate this through MASS and Hamiltonian-Lagrangian neural networks trained on standard physics problems, aggregating results across many training seeds. They find that AI scientists tend to converge in theories as training data becomes more complex, though sometimes forming distinct groups corresponding to different theories. Notably, AI scientists switch from learning Hamiltonian theory in simple setups to Lagrangian formulation when more complex systems are introduced, with strong seed dependence in training dynamics controlling the rise and fall of relevant theories.

### Theme 6: Field Surveys and Roadmaps

Two comprehensive surveys map the current state and future directions of AI Scientists. Tie et al. (2025) provide a systematic synthesis introducing a unified six-stage methodological framework (Literature Review, Idea Generation, Experimental Preparation, Experimental Execution, Scientific Writing, and Paper Generation), charting the field's evolution and providing a critical roadmap for overcoming remaining challenges in robustness and governance.

Xie et al. (2025) conduct a prospect-driven survey analyzing current achievements, identifying key bottlenecks, and outlining critical components required for scientific agents capable of producing ground-breaking discoveries. They note that LLM-based AI Scientist systems are taking the lead in scientific research, with AI-generated papers accepted at ICLR 2025 workshops, and suggest that human-level AI Scientists capable of uncovering phenomena previously unknown to humans may soon become reality.

## Convergences and Disagreements

**Convergences**: Multiple papers agree that AI Scientists have made significant progress but face substantial challenges before achieving human-level scientific capability. There is consensus that current systems can perform components of the scientific workflow but struggle with end-to-end autonomous execution, particularly in experimental implementation and verification (Zhu et al., 2025; Xie et al., 2025; Luo et al., 2025). All surveyed papers acknowledge the importance of benchmarking and evaluation, though they propose different approaches. There is also convergence on the need for better infrastructure and platforms to support AI Scientists' work (Gao et al., 2025; Zhang et al., 2025).

**Disagreements**: The literature shows some tension between optimistic assessments of AI Scientists' imminent capabilities (Xie et al., 2025 suggest human-level capability "may soon become reality") and more cautious evaluations emphasizing current limitations (Zhu et al., 2025; Luo et al., 2025). While Yamada et al. (2025) demonstrate successful peer-review acceptance at the workshop level, Luo et al. (2025) caution that such successes may mask underlying failure modes detectable only through workflow trace analysis. There is also implicit disagreement about evaluation approaches: Yin (2024) proposes ambitious historical discovery benchmarks, while Luo et al. (2025) focus on domain-specific benchmarks with human baselines.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are discussed only in full text or that the field has not yet developed standardized practices for acknowledging AI Scientists' constraints. Second, while multiple papers identify implementation gaps and failure modes, there is limited discussion of concrete solutions beyond platform development. Third, the theoretical question of AI Scientists' convergence (Fu et al., 2025) remains underexplored in relation to practical system design. Fourth, while benchmarks are proposed, there is no consensus on standardized evaluation protocols, making cross-system comparison difficult. Finally, ethical and governance considerations are mentioned (Tie et al., 2025) but not deeply explored in the surveyed literature, despite the transformative potential of autonomous scientific discovery systems.

## Per-Paper Annotations

### Fu et al. (2025)

**Research question**: When two AI models are trained on the same scientific task, do they learn the same theory or different theories?

**Methodology**: The authors propose MASS and Hamiltonian-Lagrangian neural networks as AI Scientists, trained on standard physics problems, aggregating results across many training seeds to simulate different AI scientist configurations.

**Key findings**:
- AI scientists tend to converge in theories as training data becomes more complex, though sometimes forming distinct groups corresponding to different theories.
- AI scientists switch from learning Hamiltonian theory in simple setups to Lagrangian formulation when more complex systems are introduced.
- Strong seed dependence exists in training dynamics and final learned weights, controlling the rise and fall of relevant theories.
- Neural networks can aid interpretability and be applied to higher dimensional problems.

**Limitations**: Not stated in abstract.

### Gao et al. (2025)

**Research question**: How can AI scientists be made more accessible and standardized across different models and workflows?

**Methodology**: The authors present ToolUniverse, an open platform that standardizes AI-tool interaction through a declared purpose, typed schema, and backend-agnostic invocation format, applied to over 2,700 scientific tools and 130+ research skills.

**Key findings**:
- ToolUniverse standardizes how AI scientists identify and call tools through an AI-tool interaction standard.
- The platform automatically refines tool interfaces, generates new tools from natural language, and composes tools into agentic workflows.
- Case studies demonstrate ToolUniverse enabling AI scientists to perform end-to-end analyses in target assessment, chemical strategy, and clinical-trial safety.
- The platform works across both open- and closed-weight models.

**Limitations**: Not stated in abstract.

### Luo, E. et al. (2025)

**Research question**: To what extent can AI scientists extract meaningful biological insights from real experimental omics data?

**Methodology**: The authors introduce BAISBench, a benchmark evaluating AI scientists on real single-cell transcriptomic datasets through cell type annotation across 15 datasets and 193 multiple-choice questions derived from 41 published studies, with comparison to six graduate-level bioinformaticians.

**Key findings**:
- Current AI scientists fall short of fully autonomous biological discovery but demonstrate substantial potential in supporting data-driven research.
- BAISBench provides a practical benchmark for characterizing AI scientist capabilities and limitations in biological research.
- The benchmark includes both cell type annotation tasks and scientific discovery questions derived from published conclusions.
- Human performance baseline was established through six graduate-level bioinformaticians completing the same tasks.

**Limitations**: Not stated in abstract.

### Luo, Z. et al. (2025)

**Research question**: What failure modes exist in contemporary AI scientist systems and how can they be detected?

**Methodology**: The authors design controlled experiments that isolate each of four identified failure modes (inappropriate benchmark selection, data leakage, metric misuse, and post-hoc selection bias) while addressing challenges unique to evaluating AI scientist systems. They assess two prominent open-source AI scientist systems to examine these risks.

**Key findings**:
- Four potential failure modes are identified in AI scientist systems: inappropriate benchmark selection, data leakage, metric misuse, and post-hoc selection bias.
- Assessment of two prominent open-source AI scientist systems reveals several failures across a spectrum of severity.
- These failures can be easily overlooked in practice when examining only final papers.
- Access to trace logs and code from the full automated workflow enables far more effective detection of failures than examining the final paper alone.

**Limitations**: Not stated in abstract.

### Tie et al. (2025)

**Research question**: What are the overarching methodological principles and developmental trends in the fragmented field of AI scientists?

**Methodology**: The paper provides a systematic and comprehensive synthesis of the AI scientist domain by introducing a unified six-stage methodological framework that deconstructs the end-to-end scientific process into: Literature Review, Idea Generation, Experimental Preparation, Experimental Execution, Scientific Writing, and Paper Generation. It charts the field's evolution from early Foundational Modules (2022-2023) to integrated Closed-Loop Systems (2024), and finally to the current frontier of Scalability, Impact, and Human-AI Collaboration (2025-present).

**Key findings**:
- Artificial intelligence is transitioning from a computational instrument to an autonomous originator of scientific knowledge.
- The AI scientist paradigm emulates the complete scientific workflow from hypothesis generation to publishable findings.
- The paper introduces a unified six-stage methodological framework for the end-to-end scientific process.
- The field has evolved from Foundational Modules (2022-2023) to Closed-Loop Systems (2024) to current Scalability, Impact, and Human-AI Collaboration (2025-present).
- The survey provides a critical roadmap for overcoming remaining challenges in robustness and governance.

**Limitations**: Not stated in abstract.

### Xie et al. (2025)

**Research question**: How far are AI scientists from changing the world and reshaping the scientific research paradigm?

**Methodology**: The paper conducts a prospect-driven survey review that comprehensively analyzes current achievements of AI Scientist systems. It identifies key bottlenecks and critical components required for scientific agents capable of producing ground-breaking discoveries.

**Key findings**:
- LLM-based AI Scientist systems are now taking the lead in scientific research.
- AI-generated research papers have been accepted at the ICLR 2025 workshop.
- A human-level AI Scientist capable of uncovering phenomena previously unknown to humans may soon become a reality.
- The survey identifies current limitations of AI Scientist systems and clarifies what is missing.
- The work outlines ultimate goals for scientific AI and shows where we currently are.

**Limitations**: Not stated in abstract.

### Yamada et al. (2025)

**Research question**: Can an end-to-end agentic system produce entirely AI-generated peer-review-accepted workshop papers?

**Methodology**: The authors introduce The AI Scientist-v2, an end-to-end agentic system that iteratively formulates hypotheses, designs and executes experiments, analyzes and visualizes data, and autonomously authors scientific manuscripts. The system uses a novel progressive agentic tree-search methodology managed by a dedicated experiment manager agent and eliminates reliance on human-authored code templates. They evaluated the system by submitting three fully autonomous manuscripts to a peer-reviewed ICLR workshop.

**Key findings**:
- The AI Scientist-v2 produced the first entirely AI-generated peer-review-accepted workshop paper.
- One manuscript achieved scores high enough to exceed the average human acceptance threshold, marking the first instance of a fully AI-generated paper successfully navigating peer review.
- The system eliminates reliance on human-authored code templates and generalizes effectively across diverse machine learning domains.
- The AI reviewer component is enhanced by integrating a Vision-Language Model feedback loop for iterative refinement of figures.
- The code has been open-sourced to foster future development of autonomous scientific discovery technologies.

**Limitations**: Not stated in abstract.

### Yin (2024)

**Research question**: Can we establish benchmark tests to assess whether an AI agent can conduct scientific research independently and make groundbreaking discoveries without relying on human-generated knowledge?

**Methodology**: The paper proposes seven benchmark 'Turing tests for an AI scientist' inspired by historical scientific development, evaluating an AI agent's ability to make groundbreaking discoveries in various domains. The AI agent is provided with interactive libraries or datasets specific to each problem without access to human knowledge containing information about target discoveries.

**Key findings**:
- The ability to make scientific discoveries remains a distinct challenge beyond solving math or coding problems.
- Seven benchmark tests are proposed: inferring the heliocentric model, discovering laws of motion, deriving differential equations for vibrating strings, inferring Maxwell's equations, inventing numerical methods for initial value problems, discovering Huffman coding, and developing efficient sorting algorithms.
- The tests assess the AI agent's ability to make discoveries that were groundbreaking in their time.
- Passing the majority of these seven tests would indicate significant progress towards building an AI scientist.
- The ultimate goal is creating an AI scientist capable of making novel and impactful discoveries surpassing the best human experts.

**Limitations**: Not stated in abstract.

### Zhang et al. (2025)

**Research question**: How can we create a scalable open-access platform that enables both human and AI scientists to submit, review, and iteratively refine research proposals and papers?

**Methodology**: The paper introduces aiXiv, a next-generation open-access platform with a multi-agent architecture that allows research proposals and papers to be submitted, reviewed, and iteratively refined by both human and AI scientists. It provides API and MCP interfaces for seamless integration of heterogeneous human and AI scientists, and demonstrates reliability through extensive experiments.

**Key findings**:
- Traditional journals and conferences rely on human peer review, making them difficult to scale and often reluctant to accept AI-generated research content.
- Existing preprint servers like arXiv lack rigorous quality-control mechanisms.
- aiXiv enables both human and AI scientists to submit, review, and iteratively refine research proposals and papers.
- Extensive experiments demonstrate that aiXiv significantly enhances the quality of AI-generated research proposals and papers after iterative revising and reviewing.
- The work lays groundwork for a next-generation open-access ecosystem accelerating publication and dissemination of high-quality AI-generated research.

**Limitations**: Not stated in abstract.

### Zhu et al. (2025)

**Research question**: What is the fundamental bottleneck preventing AI Scientists from achieving groundbreaking achievements in computer science?

**Methodology**: The authors provide extensive quantitative evidence from existing benchmarks in complex engineering tasks and systematically evaluate 28 research papers generated by five advanced AI Scientist systems.

**Key findings**:
- The fundamental bottleneck for AI Scientists lies in their capability to execute requisite verification procedures.
- Current AI Scientist systems lack execution capabilities needed to execute rigorous experiments and produce high-quality scientific papers.
- Despite demonstrating capabilities for independent discovery, AI Scientists have yet to produce groundbreaking achievements comparable to automated scientific tools.
- The paper identifies an 'implementation gap' as the root cause of AI Scientist limitations.

**Limitations**: Not stated in abstract.

## References

Fu, X., Liu, Z., & Tegmark, M. (2025). Do two AI scientists agree? arXiv. https://arxiv.org/abs/2504.02822

Gao, S., Zhu, R., Sui, P., Kong, Z., Aldogom, S., Huang, Y., Noori, A., Shamji, R., Parvataneni, K., Tsiligkaridis, T., & Zitnik, M. (2025). ToolUniverse: An open platform for democratizing AI scientists. arXiv. https://arxiv.org/abs/2509.23426

Luo, E., Jia, J., Xiong, Y., Li, X., Guo, X., Yu, B., Hao, M., Wei, L., & Zhang, X. (2025). Benchmarking AI scientists for omics data driven biological discovery. arXiv. https://arxiv.org/abs/2505.08341

Luo, Z., Kasirzadeh, A., & Shah, N. B. (2025). The more you automate, the less you see: Hidden pitfalls of AI scientist systems. arXiv. https://arxiv.org/abs/2509.08713

Tie, G., Zhou, P., & Sun, L. (2025). A survey of AI scientists. arXiv. https://arxiv.org/abs/2510.23045

Xie, Q., Weng, Y., Zhu, M., Shen, F., Huang, S., Lin, Z., Zhou, J., Mao, Z., Yang, Z., Yang, L., Wu, J., & Zhang, Y. (2025). How far are AI scientists from changing the world? arXiv. https://arxiv.org/abs/2507.23276

Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., Clune, J., & Ha, D. (2025). The AI Scientist-v2: Workshop-level automated scientific discovery via agentic tree search. arXiv. https://arxiv.org/abs/2504.08066

Yin, X. (2024). "Turing tests" for an AI scientist. arXiv. https://arxiv.org/abs/2405.13352

Zhang, P., Hu, X., Huang, G., Qi, Y., Zhang, H., Li, X., Song, J., Luo, J., Li, Y., Yin, S., Dai, C., Jiang, E. H., Zhou, X., Yin, Z., Yuan, B., Dong, J., Su, G., Qiao, G., Tang, H., Du, A., et al. (2025). aiXiv: A next-generation open access ecosystem for scientific discovery generated by AI scientists. arXiv. https://arxiv.org/abs/2508.15126

Zhu, M., Xie, Q., Weng, Y., Wu, J., Lin, Z., Yang, L., & Zhang, Y. (2025). AI scientists fail without strong implementation capability. arXiv. https://arxiv.org/abs/2506.01372
