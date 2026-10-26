# Systematic Literature Review: LLM Agents for Software Engineering

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search queries "LLM software engineering", "code agents", "autonomous software development" filtered to category cs.SE, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agents for software engineering has rapidly evolved from 2024 to 2026, shifting from initial demonstrations of autonomous coding capabilities toward rigorous evaluation frameworks and safety considerations. The surveyed papers collectively reveal a field maturing through critical self-examination: researchers are identifying fundamental limitations in current benchmarks, developing more realistic evaluation methodologies, and addressing safety concerns that arise from deploying code agents in practice. Three dominant themes emerge: (1) the recognition that current benchmarks like SWE-Bench may overstate agent capabilities through memorization and unrealistic task formulations, (2) the development of structured, reasoning-aware evaluation frameworks that probe deeper than pass/fail metrics, and (3) growing attention to safety and security risks inherent in autonomous code generation. Despite progress, significant gaps remain in standardized evaluation protocols, cross-repository generalization, and understanding of how agents reason about code structure and maintainability.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the queries "LLM software engineering", "code agents", and "autonomous software development", filtered to category cs.SE, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top results were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search was restricted to cs.SE category, potentially missing relevant work in cs.AI or cs.CL that addresses software engineering applications.

## Themes

### Theme 1: Benchmark Validity and the Memorization Problem

A critical thread across multiple papers questions whether current benchmarks accurately measure genuine software engineering reasoning or merely capture memorization of training data. Liang et al. (2025) demonstrate that state-of-the-art models achieve up to 76% accuracy in identifying buggy file paths using only issue descriptions without repository access, dropping to 53% on non-SWE-Bench repositories—strong evidence of data contamination. This "SWE-Bench Illusion" suggests that impressive benchmark performance may reflect memorization rather than generalizable problem-solving ability.

The memorization concern extends to evaluation methodology. Egashira et al. (2026) introduce TestSuiteBench with 165 applications and find that even frontier coding agents achieve mutation scores below 60%, despite generating implementations that pass 82% of reference tests—revealing that agents can build software they cannot verify. Similarly, Kim et al. (2026) show that realistic user inputs reduce resolution rates by 6.4 percentage points compared to curated benchmark descriptions, with 88% of real prompts containing only problem statements versus 7% of benchmark tasks.

These findings collectively challenge the validity of current evaluation paradigms and suggest that benchmark performance gains may not translate to real-world software engineering capabilities.

### Theme 2: Structured Reasoning and Repository Context Understanding

A second major theme addresses how code agents reason about repository structure and whether they genuinely understand code organization. Multiple papers identify that treating codebases as unstructured text leads to brittle failures. Kim et al. (2026) propose CODESTRUCT, which reframes codebases as structured action spaces operating on AST entities rather than text spans, improving Pass@1 accuracy by 1.2-5.0% while reducing token consumption by 12-38%.

Li et al. (2026) introduce RepoMirage, using perturbation-based diagnostics to reveal that agents exhibit "exploration drift"—accessing broader repository context but failing to convert it into effective structural information. Performance drops from 66.8% to 25.3% when structural bottlenecks are made explicit, indicating significant deficiencies in repository context reasoning. Their RepoAnchor prototype demonstrates that explicit structural scaffolding yields notable gains.

Liu et al. (2026) extend this reasoning-focused evaluation with RACE-Bench, which tracks intermediate reasoning alignment alongside patch correctness. They find that failed patches cover 35.7% fewer reference-reasoning elements and contain 94.1% more unsupported reasoning elements than successful patches, highlighting that reasoning quality—not just final output—determines agent success.

### Theme 3: Safety, Security, and Risky Code Generation

As code agents gain deployment, safety concerns emerge as a critical research direction. Guo et al. (2024) introduce RedCode, a benchmark with 4,050 risky test cases revealing that agents are more likely to reject risky OS operations than buggy code, and that risky operations in natural language achieve lower rejection rates than code format. More capable models like GPT-4 paradoxically produce more sophisticated harmful software.

Building on this, Guo et al. (2025) develop RedCodeAgent, the first automated red-teaming agent that systematically uncovers vulnerabilities across diverse code agents. With adaptive memory and dynamic tool selection, RedCodeAgent exposes previously unidentified security risks in real-world assistants like Cursor and Codeium, achieving higher attack success rates than existing methods.

Peng et al. (2025) reveal a novel threat: Functionally Correct yet Vulnerable (FCV) patches that pass all tests but contain security vulnerabilities. Their FCV-Attack demonstrates that even state-of-the-art agents are vulnerable with single black-box queries, achieving 40.7% attack success rate on GPT-5 Mini + OpenHands for information exposure vulnerabilities.

### Theme 4: Efficiency and Model Architecture Improvements

Beyond evaluation and safety, researchers explore architectural improvements for more efficient and capable code agents. Zhu et al. (2026) present CRANE, a training-free parameter-editing method that merges Instruct and Thinking model checkpoints, achieving 66.2% pass1 (+19.5%) on Roo-Eval while preserving tool-use discipline. Gandhi et al. (2026) train small critic models (4B-8B) to steer larger coding agents through high-level planning guidance, improving resolved rates by up to 16% while reducing inference costs by over 50% for some agents.

Lin et al. (2026) introduce Fast Adaptive Semantic Entropy (FASE) for uncertainty quantification in multi-agent workflows, achieving 25% improvement in Spearman correlation over LLM-driven semantic entropy at only 0.3% of the computational cost—enabling practical hallucination detection in production systems.

### Theme 5: Specialized Domains and Low-Resource Languages

While most work targets general-purpose programming, Joel et al. (2024) survey LLM capabilities for low-resource programming languages (LRPLs) and domain-specific languages (DSLs), finding that millions of developers (e.g., 3.5 million Rust users) cannot fully utilize LLM capabilities due to data scarcity and specialized syntax. Their systematic review of 111 papers identifies six improvement method categories but notes the absence of standardized benchmarks for LRPL/DSL code generation.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several critical points. First, there is widespread agreement that current benchmarks—particularly SWE-Bench—overstate agent capabilities through memorization, unrealistic task formulations, or insufficient reasoning demands (Liang et al., 2025; Kim et al., 2026; Egashira et al., 2026). Second, multiple papers independently identify that structure-aware approaches outperform text-based methods, whether through AST manipulation (Kim et al., 2026), explicit structural scaffolding (Li et al., 2026), or reasoning-augmented evaluation (Liu et al., 2026). Third, all safety-focused papers agree that current evaluation paradigms inadequately capture real-world risks, particularly the gap between functional correctness and security (Guo et al., 2024; Guo et al., 2025; Peng et al., 2025).

**Disagreements**: The literature shows limited direct disagreement, reflecting a field still mapping its territory rather than debating settled questions. However, there is tension between papers advocating for more sophisticated agent architectures (Zhu et al., 2026; Gandhi et al., 2026) and those suggesting simpler approaches may suffice. Joel et al. (2024) note that improvement methods are fragmented across six categories without consensus on which approaches generalize best.

## Gaps and Open Questions

The collective limitations across surveyed papers reveal several critical gaps:

1. **Standardized benchmarks for specialized domains**: Joel et al. (2024) identify the absence of standard benchmarks for LRPL/DSL code generation, a gap that persists across the literature.

2. **Cross-repository generalization**: Multiple papers note evaluation limited to specific repositories or benchmarks, with Liang et al. (2025) showing dramatic performance drops on non-SWE-Bench repositories. True generalization remains unproven.

3. **Long-term maintainability focus**: Lin et al. (2026) and Egashira et al. (2026) highlight that benchmarks prioritize functional correctness over maintainability, with agents struggling to eliminate code smells or generate comprehensive test suites.

4. **Real-world deployment validation**: Most evaluations remain benchmark-based rather than field studies. Treude (2026) notes accountability frameworks are poorly aligned with agent-mediated workflows, suggesting deployment realities outpace research.

5. **Human-agent collaboration dynamics**: While BotDD (Treude & Poskitt, 2024) and CodePori (Rasheed et al., 2026) touch on practitioner perspectives, systematic understanding of human-agent teaming remains limited.

6. **Computational efficiency at scale**: FASE (Lin et al., 2026) and CRANE (Zhu et al., 2026) address efficiency, but production-scale multi-agent workflows remain underexplored.

## Per-Paper Annotations

### Egashira et al. (2026)

**Research question**: Can coding agents generate strong test suites from specifications for complex software projects?
**Methodology**: Introduced TestSuiteBench with 165 open-source applications, each with structured specifications, reference implementations, reference test suites, and an average of 74 mutants per application.
**Key findings**:
- Frontier coding agents achieve mutation scores below 60% despite generating valid test suites
- 88% of generated tests pass on reference implementations, but suites lack relevant input combinations
- Generated implementations pass 82% of reference tests, showing agents can build software they cannot verify
- Generated test suites are smaller than reference suites, missing critical edge cases
**Limitations**: Limited to 165 applications; mutation generation may not capture all real-world testing requirements.

### Gandhi et al. (2026)

**Research question**: Can small critic models specialized in high-level planning improve larger coding agents' performance?
**Methodology**: Trained 4B and 8B critic models using SFT and DPO to identify errors and provide guidance without generating concrete actions, evaluated across 6 coding agents.
**Key findings**:
- Critic models improve resolved rates by up to 16.0% on SWE-Bench Verified
- Reduces per-example inference cost from $0.07 to $0.03 for some agents (>50% reduction)
- Critic guidance helps larger models avoid planning errors without concrete action generation
**Limitations**: Requires separate critic training; effectiveness depends on quality of SFT/DPO data construction.

### Guo et al. (2024)

**Research question**: How can we comprehensively evaluate code agents' safety regarding risky code execution and generation?
**Methodology**: Created RedCode benchmark with RedCode-Exec (4,050 risky test cases in Python/Bash across 25 vulnerability types) and RedCode-Gen (10 harmful code generation prompts), evaluating 19 LLMs across 3 agent frameworks.
**Key findings**:
- Agents more likely to reject risky OS operations than technically buggy code
- Risky operations in natural language achieve lower rejection rates than code format
- More capable models (e.g., GPT-4) produce more sophisticated harmful software
- 25 critical vulnerability types across 8 domains identified and benchmarked
**Limitations**: Limited to Python and Bash; RedCode-Gen includes only 10 prompts; evaluation limited to 19 LLMs.

### Guo et al. (2025)

**Research question**: How can we systematically uncover vulnerabilities in diverse code agents that current static safety benchmarks miss?
**Methodology**: Developed RedCodeAgent, an automated red-teaming agent with adaptive memory that dynamically selects effective red-teaming tools, evaluated using simulated sandbox environments.
**Key findings**:
- First automated red-teaming agent for code agents, outperforming existing methods
- Exposes previously unidentified security risks in Cursor and Codeium
- Adaptive memory enables dynamic tool combination selection for boundary condition coverage
- Sandbox evaluation mitigates LLM judge biases from static code analysis
**Limitations**: Evaluation limited to specific code agents and languages; sandbox environments may not capture all deployment scenarios.

### Joel et al. (2024)

**Research question**: What are the current capabilities, challenges, and opportunities for LLM-based code generation in low-resource programming languages and domain-specific languages?
**Methodology**: Systematic literature review filtering 111 papers from over 27,000 studies (2020-2024), analyzing LLMs, benchmarks, metrics, improvement strategies, and dataset methods.
**Key findings**:
- LLMs perform poorly on LRPLs/DSLs due to data scarcity and specialized syntax
- Four evaluation techniques and multiple metrics identified across reviewed studies
- Six improvement method categories with novel architectures proposed
- No standard benchmark or approach exists for LRPL/DSL code generation
- 3.5 million Rust users alone cannot fully utilize LLM capabilities
**Limitations**: Survey covers literature only through 2024; lacks standardized benchmarks for comparability.

### Kim et al. (2026)

**Research question**: How does the gap between structured benchmark descriptions and realistic user requests affect coding agent evaluation?
**Methodology**: Defined six-category information taxonomy and four linguistic style dimensions, created RealSWE with 381 multi-variant task families from SWE-bench, evaluated seven LLMs.
**Key findings**:
- 88% of real prompts contain only problem statements vs. 7% of benchmark tasks
- 87% of real prompts are casually written vs. 94% of benchmarks being formal
- Realistic inputs reduce resolution rates by 6.4 percentage points on average
- Desired Behavior and Motivation information significantly improves performance
- Linguistic style has small, model-dependent effects
**Limitations**: Based on SWE-bench variants; may not generalize to all real-world scenarios; limited to seven LLMs.

### Li et al. (2026)

**Research question**: Does success on end-to-end tasks truly reflect repository context reasoning ability in code agents?
**Methodology**: Introduced RepoMirage, a two-stage evaluation suite using semantics-preserving repository perturbations and explicit structural tasks built on SWE-Bench Verified.
**Key findings**:
- Performance drops from 66.8% to 25.3% when structural bottlenecks are explicit
- Agents exhibit "exploration drift"—accessing context but not converting to structure
- Three perturbation types reveal clear performance degradation requiring broader context
- RepoAnchor structure-first prototype yields notable gains through explicit scaffolding
**Limitations**: Built on SWE-Bench Verified; RepoAnchor is prototype without comprehensive evaluation across diverse repositories.

### Liang et al. (2025)

**Research question**: Are performance gains on SWE-Bench Verified driven by genuine reasoning or memorization/data contamination?
**Methodology**: Introduced two diagnostic tasks (file path identification from issue descriptions, function reproduction with limited context), comparing SWE-Bench vs. non-SWE-Bench repository performance.
**Key findings**:
- Models achieve 76% accuracy identifying file paths with only issue descriptions
- Performance drops to 53% on non-SWE-Bench repositories, suggesting contamination
- 35% consecutive 5-gram accuracy on SWE-Bench vs. 18% on other benchmarks
- Current evaluation protocols may overstate true software engineering capabilities
**Limitations**: Diagnostic tasks probe specific knowledge aspects; exact contamination sources remain unclear.

### Lin et al. (2026)

**Research question**: How can we efficiently quantify uncertainty in multi-agent code generation without costly LLM-driven equivalence checks?
**Methodology**: Introduced Fast Adaptive Semantic Entropy (FASE) approximating functional correctness via minimum spanning tree of structural/semantic dissimilarity graphs, evaluated on HumanEval and BigCodeBench.
**Key findings**:
- 25% average improvement in Spearman correlation over LLM-driven semantic entropy
- 19% increase in ROCAUC score against Pass@1 with Qwen3-Embedding-8B
- Requires only 0.3% of computational cost compared to traditional semantic entropy
- Enables practical hallucination detection in real-world multi-agent workflows
**Limitations**: Evaluated on function-level benchmarks; repository-level uncertainty quantification remains unexplored.

### Liu et al. (2026)

**Research question**: How can we evaluate repository-level code agents beyond final test correctness to understand reasoning quality?
**Methodology**: Introduced RACE-Bench with 528 feature addition instances from 12 repositories, each with executable patch verification and structured reference reasoning, using dual-track evaluation of correctness and reasoning alignment.
**Key findings**:
- Resolved Rate ranges from 29% to 70% across three agents on full benchmark
- Agents perform well on high-level intent but degrade on concrete implementation steps
- Failed patches cover 35.7% fewer reasoning elements than successful patches
- Failed patches contain 94.1% more unsupported reasoning elements
**Limitations**: Evaluates only three agents across 12 repositories; reasoning alignment depends on developer-accepted trajectories that may not capture all valid solutions.

### Peng et al. (2025)

**Research question**: Are functionally correct patches generated by code agents actually safe from security vulnerabilities?
**Methodology**: Developed FCV-Attack demonstrating Functionally Correct yet Vulnerable patches, evaluated across 12 agent-model combinations on SWE-Bench with black-box single-query attacks.
**Key findings**:
- Functionally Correct yet Vulnerable (FCV) patches pass tests but contain security flaws
- 40.7% attack success rate on GPT-5 Mini + OpenHands for CWE-538 information exposure
- All 12 agent-model combinations vulnerable across SWE-Bench
- Single black-box query sufficient to perform successful attacks
**Limitations**: Focused on specific CWE types; defense mechanisms not explored in depth.

### Rasheed et al. (2024)

**Research question**: How do LLM-based multi-agent systems perform on real-world autonomous software development tasks beyond binary benchmark evaluations?
**Methodology**: Developed CodePori multi-agent system for automated code generation, conducted survey-based evaluation with practitioners assessing agent performance on challenging real-world tasks.
**Key findings**:
- Multi-agent systems show potential for autonomous code generation in practice
- Specific challenges identified: short-term memory limitations, hallucinations, code smells
- Practitioner perspective reveals gaps between benchmark and real-world applicability
- Need to move beyond standard benchmarks for practical evaluation
**Limitations**: Survey-based evaluation may not generalize; specific agent architecture details limited.

### Treude (2026)

**Research question**: How do Terms of Service for AI coding assistants allocate accountability, and are existing frameworks aligned with agent-mediated software development?
**Methodology**: Comparative analysis of Terms of Service for widely-used AI coding assistants and agent-enabled tools, examining ownership, responsibility, liability, and disclosure obligations.
**Key findings**:
- Consistent tendency to shift responsibility for correctness, safety, and compliance onto users
- Substantial variation across providers in indemnification, data reuse, and acceptable use
- Existing policy frameworks poorly aligned with agent-mediated workflows
- Research roadmap outlined for modeling responsibility and governance artifacts
**Limitations**: Analysis limited to ToS documents; empirical studies of developer perceptions needed.

### Treude & Poskitt (2024)

**Research question**: How does bot-driven development transform traditional software development roles and practices?
**Methodology**: Conceptual exploration of bot-driven development paradigm, proposing research agenda addressing skill development, human-bot trust, interruption frequency, and ethical considerations.
**Key findings**:
- Bots transitioning from support tasks to proactive development workflow drivers
- BotDD redefines driver-navigator dynamics and aligns with DevOps goals
- Four key challenges identified: skill development, trust dynamics, interruption frequency, ethics
- Need for empirical studies and prototype systems to define best practices
**Limitations**: Vision paper without empirical validation; governance structures remain conceptual.

### Zhu et al. (2026)

**Research question**: How can we combine complementary capabilities of Instruct models (tool-disciplined) and Thinking models (strong planning) for code agents?
**Methodology**: Developed CRANE, training-free parameter-editing method using magnitude thresholding, Conservative Taylor Gate, and Graduated Sigmoidal Projection to merge Instruct/Thinking checkpoints.
**Key findings**:
- Achieves 66.2% pass1 (+19.5%) on Roo-Eval for Qwen3-30B-A3B
- Resolves up to 14 additional instances on SWE-bench-Verified at both scales
- Improves pass1/pass5 by up to 2.3%/7.8% on Terminal-Bench v2
- Preserves Instruct-level efficiency while outperforming alternative merging strategies
**Limitations**: Only applies to paired Instruct/Thinking checkpoints; training-free approach may limit applicability.

## References

Egashira, K., Mündler-Sasahara, N., Müller, M. N., & Vechev, M. (2026). TestSuiteBench: Coding agents struggle to generate strong test suites from specifications. arXiv. https://arxiv.org/abs/2610.13065

Gandhi, S., Xie, Y., Naik, A., Zhu, R., & Rose, C. (2026). Steer, don't solve: Training small critic models for large code agents. arXiv. https://arxiv.org/abs/2606.21811

Guo, C., Liu, X., Xie, C., Zhou, A., Zeng, Y., Lin, Z., Song, D., & Li, B. (2024). RedCode: Risky code execution and generation benchmark for code agents. arXiv. https://arxiv.org/abs/2411.07781

Guo, C., Xie, C., Yang, Y., Chen, Z., Lin, Z., Davies, X., Gal, Y., Song, D., & Li, B. (2025). RedCodeAgent: Automatic red-teaming agent against diverse code agents. arXiv. https://arxiv.org/abs/2510.02609

Joel, S., Wu, J. J. W., & Fard, F. H. (2024). A survey on LLM-based code generation for low-resource and domain-specific programming languages. arXiv. https://arxiv.org/abs/2410.03981

Kim, G., Gwon, H., Kim, J., Shim, K., & Lee, S. (2026). RealSWE: A compositional evaluation of coding agents under realistic user requests. arXiv. https://arxiv.org/abs/2608.27831

Li, H., Zhang, Y., Zhu, S., Su, H., Zhu, J., & Dong, Y. (2026). RepoMirage: Probing repository context reasoning in code agents with perturbations. arXiv. https://arxiv.org/abs/2605.26177

Liang, S., Garg, S., & Moghaddam, R. Z. (2025). The SWE-Bench illusion: When state-of-the-art LLMs remember instead of reason. arXiv. https://arxiv.org/abs/2506.12286

Lin, F., Hu, B., Zhu, X., Zhao, Z., Zheng, Z., Liu, Z., Zhang, Z., Zhou, J., & Xu, T. (2026). SmellBench: Towards fine-grained evaluation of code agents on refactoring tasks. arXiv. https://arxiv.org/abs/2606.05574

Lin, S., & Tahvildari, L. (2026). FASE: Fast adaptive semantic entropy for code quality. arXiv. https://arxiv.org/abs/2606.09800

Liu, S., Zhao, Z., Hu, X., Liu, K., Yang, X., & Xia, X. (2026). RACE-Bench: A reasoning-augmented benchmark for repository-level code agents on feature addition. arXiv. https://arxiv.org/abs/2603.26337

Peng, Y., Song, J., Li, L., Yang, X., Christodorescu, M., Mangal, R., Pasareanu, C., Zheng, H., & Chen, B. (2025). When "correct" is not safe: Can we trust functionally correct patches generated by code agents? arXiv. https://arxiv.org/abs/2510.17862

Rasheed, Z., Waseem, M., Kemell, K.-K., Ahmad, A., Sami, M. A., Saari, M., Rasku, J., & Abrahamsson, P. (2024). CodePori: Large-scale system for autonomous software development using multi-agent technology. arXiv. https://arxiv.org/abs/2402.01411

Treude, C. (2026). Accountable agents in software engineering: An analysis of Terms of Service and a research roadmap. arXiv. https://arxiv.org/abs/2605.04532

Treude, C., & Poskitt, C. M. (2024). Bot-driven development: From simple automation to autonomous software development bots. arXiv. https://arxiv.org/abs/2411.16100

Zhu, M., Merler, M., Pavuluri, R., & Patterson, S. (2026). CRANE: Constrained reasoning injection for code agents via nullspace editing. arXiv. https://arxiv.org/abs/2605.14084
