# Systematic Literature Review: LLM Agents for Software Engineering

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search queries: "LLM software engineering", "autonomous agents code", "AI programming assistant", "code generation agent"; category cs.SE; published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on LLM agents for software engineering reveals a field rapidly maturing from initial code generation capabilities toward more sophisticated concerns including evaluation validity, human factors, security, and ecosystem-level impacts. Surveyed papers collectively demonstrate that while LLM-based coding agents show impressive performance on benchmarks, significant challenges remain: benchmark contamination inflates performance metrics, real-world user requests differ substantially from structured benchmark tasks, and AI assistance introduces hidden biases favoring mainstream technologies over niche ones. Research has expanded beyond pure code generation to address trust calibration, security vulnerabilities, human-centric evaluation frameworks, and the dynamics of developer-AI collaboration. The field acknowledges critical gaps in standardized evaluation for specialized languages, contamination-resistant benchmarks, and longitudinal studies of AI assistant adoption in professional settings.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using multiple queries ("LLM software engineering", "autonomous agents code", "AI programming assistant", "code generation agent"), filtered to category cs.SE, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top results were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search yielded only 3 papers from the initial query, requiring broadened searches to reach 10 papers, which may indicate the specificity of the "LLM agents" framing within cs.SE.

## Themes

### Theme 1: Benchmark Validity and Evaluation Challenges

A significant thread in the literature questions the validity of current benchmark-based evaluation approaches for LLM coding agents. Liang et al. (2025) provide critical evidence that performance gains on SWE-Bench-Verified may be partially driven by memorization rather than genuine problem-solving ability. Their diagnostic tasks reveal that state-of-the-art models achieve up to 76% accuracy identifying buggy file paths using only issue descriptions without repository structure access, but performance drops to 53% on repositories not included in SWE-Bench, suggesting data contamination or memorization.

This concern is complemented by Kim et al. (2026), who demonstrate that realistic user requests differ fundamentally from benchmark tasks. Their analysis shows 88% of real user prompts contain only problem statements with limited context, compared to just 7% of benchmark problems, and realistic inputs reduce resolution rates by 6.4 percentage points on average. These findings collectively suggest that current benchmarks may overstate LLM capabilities and fail to capture real-world usage patterns.

### Theme 2: Human Factors and Trust Dynamics

Multiple papers investigate the human dimensions of AI-assisted programming, moving beyond technical metrics to examine how developers interact with and perceive AI assistants. Shah et al. (2025) tracked the evolution of programmer trust over time, finding that trust in GitHub Copilot increased on average but required calibration to avoid both over-reliance and under-utilization. Their longitudinal study with 71 CS students revealed that trust elevation was driven by observing Copilot's correctness, understanding its context usage, and learning NLP basics.

Heydari (2025) established a human-centered requirements framework for assessing GitHub Copilot output, arguing that existing evaluation frameworks overlook crucial human factors affecting AI assistant integration in software workflows. The framework emphasizes Copilot's ability to adapt explanations and code generation to different user expertise levels, measuring collaborative programming effectiveness rather than pure code correctness.

Rawal et al. (2024) investigated how different hint types affect bug-finding accuracy across program representations, finding that users are surprisingly more accurate when viewing programs in natural text rather than Python code. Their large-scale study with 753 participants suggests next-generation programming tools should provide personalized support adapting modality and hints to user skill level.

### Theme 3: Security and Reliability Concerns

Security vulnerabilities in AI-generated code represent a critical research direction. Kim et al. (2024) present Codexity, a security-focused code generation framework that leverages static analysis tool feedback to mitigate vulnerabilities. Their evaluation on 751 automatically generated vulnerable subjects demonstrates Codexity prevents 60% of vulnerabilities from reaching developers, though 40% still require manual detection.

The security theme connects to broader reliability concerns raised by Liang et al. (2026), who analyze 53.6K real-world developer edits of AI-generated code. Their DECODE dataset reveals that 31% of edit trajectories result in complete removal of AI-generated code, with most edits occurring within 15 minutes of acceptance. This suggests significant reliability issues requiring substantial post-generation correction.

### Theme 4: Ecosystem-Level Impacts and Bias

Recent work examines how AI programming assistants influence broader software ecosystem dynamics beyond individual productivity. Gu et al. (2025) identify a "Matthew Effect" in AI-assisted programming, where mainstream languages and frameworks achieve significantly higher success rates than niche ones. Their large-scale experiments quantifying performance asymmetry suggest a feedback loop where data-rich ecosystems gain superior AI support, introducing hidden bias in software evolution.

This ecosystem perspective connects to Joel et al. (2024), who survey LLM-based code generation for low-resource and domain-specific programming languages. Their analysis of 111 papers reveals that millions of developers (e.g., 3.5M Rust users) cannot fully utilize LLM capabilities due to data scarcity and specialized syntax poorly represented in general-purpose datasets. The lack of standardized benchmarks for specialized languages exacerbates these disparities.

### Theme 5: Multi-Agent Architectures and Advanced Capabilities

Emerging research explores sophisticated multi-agent architectures for complex software engineering tasks. Chen et al. (2026) propose a multi-agent framework for automated exploit generation combining constraint-guided comprehension and reflection mechanisms. Their framework uses specialized agents collaborating to analyze vulnerabilities, generate exploits, and iteratively refine output, achieving higher success rates than single-agent baselines while requiring less human intervention.

This architectural evolution reflects the field's progression from simple code completion toward autonomous agents capable of handling complex, multi-step software engineering tasks requiring deep semantic understanding.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the conclusion that current evaluation approaches are insufficient. Liang et al. (2025), Kim et al. (2026), and Joel et al. (2024) all identify gaps between benchmark performance and real-world capability, calling for more robust, contamination-resistant evaluation methods. The literature also converges on the importance of human factors: Shah et al. (2025), Heydari (2025), and Rawal et al. (2024) all emphasize that successful AI assistant integration requires attention to trust, expertise adaptation, and personalized support.

**Disagreements**: The literature does not show fundamental disagreements but rather reveals tensions between optimization goals. Security-focused work (Kim et al., 2024) prioritizes vulnerability prevention, while productivity-focused research (Liang et al., 2026) emphasizes edit prediction and workflow integration. These represent complementary rather than conflicting priorities, though the field has not yet reconciled how to balance security constraints with development velocity.

## Gaps and Open Questions

The collective literature reveals several critical gaps:

1. **Standardized benchmarks for specialized languages**: Joel et al. (2024) identify the absence of standard approaches and benchmark datasets for evaluating code generation in low-resource and domain-specific languages, limiting comparability across studies and leaving millions of developers underserved.

2. **Contamination-resistant evaluation**: Liang et al. (2025) demonstrate that current benchmarks may measure memorization rather than reasoning, but the field lacks alternative evaluation frameworks that reliably isolate genuine problem-solving ability.

3. **Longitudinal professional studies**: Shah et al. (2025) note their study population was limited to CS students即将 entering the workforce, and the 10-day period may not capture long-term trust evolution. Professional developer populations and longer time scales remain understudied.

4. **Language and framework diversity**: Liang et al. (2026) limited their DECODE dataset to Python, TypeScript, and JavaScript. Other programming languages and their unique editing patterns remain unexplored.

5. **Security coverage gaps**: Kim et al. (2024) achieved 60% vulnerability prevention, leaving 40% undetected. The nature of these remaining vulnerabilities and approaches to address them require further investigation.

6. **Generalizability of findings**: Multiple studies acknowledge limitations in scope—Kim et al. (2026) evaluated only seven LLMs, Rawal et al. (2024) focused on specific hint types, and Chen et al. (2026) did not fully detail their evaluation scope. Broader validation across diverse contexts remains needed.

## Per-Paper Annotations

### Chen et al. (2026)

**Research question**: How can automated exploit generation handle complex vulnerabilities with less human intervention than existing approaches?
**Methodology**: Developed a multi-agent framework combining constraint-guided comprehension and reflection mechanisms, with specialized agents collaborating to analyze vulnerabilities, generate exploits, and iteratively refine output through reflection.
**Key findings**:
- Multi-agent approach achieves higher success rates in generating working exploits compared to single-agent baselines
- Framework requires less human intervention than existing AEG approaches
- Particularly effective for complex vulnerability types requiring deep understanding of program semantics
- Constraint-guided comprehension helps agents understand vulnerability context and constraints
- Reflection mechanism enables continuous improvement of generated exploits
**Limitations**: Evaluation scope on real-world vulnerabilities not fully detailed in abstract; framework complexity may limit practical adoption in resource-constrained environments.

### Gu et al. (2025)

**Research question**: How does AI-assisted programming interact with the software ecosystem and affect the adoption dynamics of different programming languages and frameworks?
**Methodology**: Large-scale experiments on thousands of algorithmic programming tasks and hundreds of framework selection tasks to systematically measure performance asymmetry between mainstream and niche technologies.
**Key findings**:
- Mainstream languages and frameworks achieve significantly higher success rates with AI assistants than niche ones
- Evidence of a Matthew Effect feedback loop where data-rich ecosystems gain superior AI support
- Current LLM models introduce non-negligible productivity friction for niche technologies
- AI assistance represents a hidden bias in software evolution beyond just prompt design and code quality
**Limitations**: AI bias is not the sole driver of technology adoption; the study focuses on performance metrics rather than other factors influencing ecosystem dynamics.

### Heydari (2025)

**Research question**: How well does GitHub Copilot address human needs and adapt its explanations and code generation to different user expertise levels?
**Methodology**: Analyzed GitHub Copilot's chat interface interactions, measured its ability to adapt to user expertise levels, and established a human-centered requirements framework with clear metrics to evaluate these qualities.
**Key findings**:
- Existing evaluation frameworks overlook crucial human factors affecting AI assistant integration in software workflows
- Human-centered framework with clear metrics enables systematic evaluation of Copilot's collaborative qualities
- Copilot's ability to adapt explanations and code generation varies by user expertise level
- Test results provide implications for future analysis of human requirements in automated programming
**Limitations**: Abstract does not specify concrete quantitative results; focuses primarily on framework development rather than extensive empirical validation across diverse user populations.

### Joel et al. (2024)

**Research question**: What are the current capabilities, challenges, and opportunities for LLM-based code generation in Low-Resource Programming Languages (LRPLs) and Domain-Specific Languages (DSLs)?
**Methodology**: Systematically filtered and reviewed 111 papers from over 27,000 published studies between 2020-2024, analyzing LLMs used, benchmarks, evaluation metrics, improvement strategies, and dataset collection methods for LRPLs and DSLs.
**Key findings**:
- LLMs face significant challenges with LRPLs and DSLs due to data scarcity and specialized syntax poorly represented in general-purpose datasets
- Four main evaluation techniques and multiple metrics were identified for assessing code generation in LRPLs and DSLs
- Improvement methods can be categorized into six groups, with several novel architectures proposed by researchers
- No standard approach or benchmark dataset exists for evaluating code generation in LRPLs and DSLs
- Millions of developers (e.g., 3.5M Rust users) cannot fully utilize LLM capabilities for their specialized languages
**Limitations**: The survey synthesizes existing work rather than proposing new solutions; the lack of standardized benchmarks and evaluation approaches limits comparability across studies.

### Kim et al. (2024)

**Research question**: How can security vulnerabilities introduced by AI programming assistants into software codebases be mitigated?
**Methodology**: Developed Codexity, a security-focused code generation framework integrated with five LLMs that leverages feedback from static analysis tools (Infer and CppCheck) to mitigate vulnerabilities in generated code.
**Key findings**:
- Codexity prevents 60% of vulnerabilities from being exposed to software developers
- Static analysis tool feedback effectively reduces security issues in LLM-generated programs
- Framework successfully integrates with multiple LLMs for secure code generation
- Evaluation on 751 automatically generated vulnerable subjects demonstrates practical effectiveness
**Limitations**: 40% of vulnerabilities still reach developers; evaluation limited to a specific benchmark with automatically generated vulnerable subjects.

### Kim et al. (2026)

**Research question**: How do coding agents perform when evaluated on realistic, unstructured user requests compared to structured benchmark tasks from SWE-bench?
**Methodology**: Defined a six-category information taxonomy and four linguistic style dimensions, analyzed real user prompts from SWE-chat versus SWE-bench problems, then created RealSWE with 381 multi-variant task families to evaluate seven contemporary LLMs.
**Key findings**:
- 88% of real user prompts contain only problem statements with limited context, compared to just 7% of benchmark problems
- 87% of real prompts are casually written whereas 94% of benchmark problems use formal language
- Realistic inputs reduce resolution rates by 6.4 percentage points on average and can change model rankings
- Including Desired Behavior and Motivation information significantly improves performance, while Environment Information and Reproduction Steps add tokens without measurable benefit
- Linguistic style has only small, model-dependent effects on performance
**Limitations**: RealSWE variants are derived from SWE-bench, which may not capture all real-world scenarios; evaluation limited to seven LLMs.

### Liang et al. (2025)

**Research question**: Are performance gains on SWE-Bench-Verified driven by genuine problem-solving ability or by memorization and data contamination?
**Methodology**: Introduced two diagnostic tasks: file path identification from issue descriptions alone, and ground truth function reproduction with only current file context and issue description, to probe models' underlying knowledge versus memorization.
**Key findings**:
- State-of-the-art models achieve up to 76% accuracy identifying buggy file paths using only issue descriptions without repository structure access
- Performance drops to merely 53% on tasks from repositories not included in SWE-Bench, suggesting data contamination or memorization
- Verbatim similarity reaches up to 35% consecutive 5-gram accuracy on SWE-Bench Verified and Full, but only 18% on other similar coding benchmarks
- Similar memorization patterns observed in function reproduction tasks
- Current evaluation protocols may overstate LLMs' true software engineering capabilities
**Limitations**: Diagnostic tasks may not fully isolate memorization from reasoning; cannot definitively prove contamination versus genuine pattern recognition; limited to specific benchmark families.

### Liang et al. (2026)

**Research question**: What patterns exist in how developers edit AI-generated code in real-world settings, and can LLMs be trained to predict these edits?
**Methodology**: Introduced DECODE dataset containing 53.6K real-world in-IDE code edits of AI-generated code from 1K+ developers across Python, TypeScript, and JavaScript, then analyzed edit patterns and benchmarked LLM edit prediction capabilities.
**Key findings**:
- Most edits occur within the first 15 minutes after accepting an AI completion
- 31% of edit trajectories result in complete removal of AI-generated code
- Fine-tuning on DECODE enables open-source 3B models to outperform frontier LLMs on code edit prediction tasks
- Manual code edits provide more realistic and granular editing behavior information than Git commits
- Developer-centric machine learning approaches are necessary for future AI programming assistants
**Limitations**: Dataset limited to three languages (Python, TypeScript, JavaScript); in-IDE edits may not capture all editing behaviors; may not generalize across all development contexts and team practices.

### Rawal et al. (2024)

**Research question**: Which types of hints are helpful for bug finding and fixing, and how does this depend on program representation and the user's algorithmic understanding?
**Methodology**: Large-scale crowd-sourced study with 753 participants investigating three hint types (test cases, conceptual, detailed) across two program representations (Python and text-based) and two user groups with different levels of algorithmic understanding.
**Key findings**:
- Program representation significantly influences users' accuracy at finding and fixing bugs
- Users are surprisingly more accurate when viewing programs in natural text rather than Python code
- Hints generally improve accuracy but effectiveness varies by program representation and user understanding
- Different hint types help differently depending on context and user capability
- Findings support personalized programming tools that adapt modality and hints to user skill level
**Limitations**: Study limited to specific hint types and program representations; may not generalize to all programming contexts or more complex debugging scenarios.

### Shah et al. (2025)

**Research question**: How does programmer trust in AI programming assistants like GitHub Copilot evolve over immediate (one hour) and extended (10 days) usage periods?
**Methodology**: Collected survey data from 71 upper-division computer science students working on a legacy code base, quantitatively measuring trust levels and qualitatively analyzing why trust changes over time.
**Key findings**:
- Student trust in Copilot increased on average over the study period
- After completing projects, students recognized that Copilot requires a competent programmer to complete some tasks manually
- Trust elevation was driven by observing Copilot's correctness, understanding how it uses codebase context, and learning NLP basics
- Four pedagogical recommendations emerged: provide challenging SE tasks for trust calibration, teach traditional debugging/testing skills, introduce NLP basics, and demonstrate Copilot's feature range
- Trust is a dynamic attitude that requires calibration to avoid both over-reliance and under-utilization
**Limitations**: Study population limited to CS students即将 entering workforce, may not represent professional developers; 10-day period may not capture long-term trust evolution; reliance on self-reported survey data.

## References

Chen, S., Luo, T., Wu, S., Liu, X., Zhou, Y., Li, Q., & Xu, W. (2026). A multi-agent framework for automated exploit generation with constraint-guided comprehension and reflection. arXiv. https://arxiv.org/abs/2604.05130

Gu, F., Liang, Z., MA, J., & LI, H. (2025). The Matthew effect of AI programming assistants: A hidden bias in software evolution. arXiv. https://arxiv.org/abs/2509.23261

Heydari, S. (2025). A human centric requirements engineering framework for assessing Github Copilot output. arXiv. https://arxiv.org/abs/2508.03922

Joel, S., Wu, J. J. W., & Fard, F. H. (2024). A survey on LLM-based code generation for low-resource and domain-specific programming languages. arXiv. https://arxiv.org/abs/2410.03981

Kim, G., Gwon, H., Kim, J., Shim, K., & Lee, S. (2026). RealSWE: A compositional evaluation of coding agents under realistic user requests. arXiv. https://arxiv.org/abs/2608.27831

Kim, S. Y., Fan, Z., Noller, Y., & Roychoudhury, A. (2024). Codexity: Secure AI-assisted code generation. arXiv. https://arxiv.org/abs/2405.03927

Liang, J. T., Bairathi, M., Chi, W., Talwalkar, A., Subramani, N., & Chen, V. (2026). Learning from 53.6K real-world developer edits of AI-generated code. arXiv. https://arxiv.org/abs/2607.25130

Liang, S., Garg, S., & Moghaddam, R. Z. (2025). The SWE-bench illusion: When state-of-the-art LLMs remember instead of reason. arXiv. https://arxiv.org/abs/2506.12286

Rawal, R., Pădurean, V.-A., Apel, S., Singla, A., & Toneva, M. (2024). Hints help finding and fixing bugs differently in Python and text-based program representations. arXiv. https://arxiv.org/abs/2412.12471

Shah, A., Rexin, T., Tomson, E., Porter, L., Griswold, W. G., & Raj, A. G. S. (2025). Evolution of programmers' trust in generative AI programming assistants. arXiv. https://arxiv.org/abs/2509.13253
