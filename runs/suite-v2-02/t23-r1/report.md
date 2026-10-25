# Systematic Literature Review: Planning with Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "planning large language models", category cs.AI, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on planning with large language models reveals a field in rapid transition, characterized by both optimism about LLM capabilities and sober recognition of fundamental limitations. Recent research demonstrates that while LLMs show remarkable capacity for multi-step reasoning and generalization across domains, they exhibit significant constraints when handling long-horizon planning tasks requiring structured reasoning and explicit state maintenance. The surveyed papers collectively suggest that LLMs are not well-suited as standalone planners, but present enormous opportunity when integrated with traditional planning methods, formal specification languages, or hybrid neuro-symbolic approaches. A recurring finding across multiple studies is that planning performance degrades substantially when tasks require more than 25 moves or steps, suggesting architectural limitations that test-time scaling alone cannot overcome.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "planning large language models", filtered to category cs.AI, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Hybrid Approaches Combining LLMs with Traditional Planning

A dominant theme across the surveyed literature is the recognition that LLMs alone are insufficient for reliable planning, but can significantly enhance planning applications when combined with traditional methods. Multiple papers advocate for hybrid methodologies that leverage LLM flexibility alongside traditional planning rigor (Aghzal et al., 2025; Tantakoun et al., 2025; Puerta-Merino et al., 2025). This approach positions LLMs as tools for formalizing and refining planning specifications to support off-the-shelf automated planners, rather than as standalone planning engines. The integration of neuro-symbolic approaches within automated planning and NLP communities is identified as a promising direction to address LLM planning limitations (Tantakoun et al., 2025).

### Theme 2: Fundamental Limitations in Long-Horizon Planning

Several papers converge on the finding that LLMs exhibit severe limitations in long-horizon planning tasks. Monti et al. (2026) demonstrate that planning performance consistently degrades when more than 25 moves are required, suggesting a fundamental constraint on forward planning capacity in large reasoning models. Schepanowski and Ling (2025) provide even more stark evidence, finding that none of the tested models could solve 8-puzzle tasks even with an external move validator providing only valid moves, due to brittle internal state representations and weak heuristic planning. These findings suggest that inherent architectural limitations might not be overcome by test-time scaling approaches alone (Monti et al., 2026; Schepanowski & Ling, 2025).

### Theme 3: Multi-Agent and Cooperative Frameworks

An emerging research direction explores cooperative multi-agent frameworks to enhance LLM reasoning capabilities for complex multi-step problems. Wang et al. (2024) propose CoPlanner, a framework that separates reasoning steps between a planning agent providing high-level strategic hints and a reasoning agent following those hints, achieving significant performance improvements on reasoning benchmarks. This approach demonstrates that guidance from specialized planning agents and effective cooperation between agents can contribute to superior performance on multi-step reasoning problems. Similarly, Srivastava et al. (2026) introduce GRASP, a strategy-aware multi-stage planning framework that decouples the planning pipeline across specialized modules for generating, revising, and assessing plans.

### Theme 4: Formal Languages and Structured Representations

Several papers explore the use of formal or semi-formal languages to make AI planning more auditable and reliable. Guan et al. (2025) present NormCode, a semi-formal language that enforces data isolation at each inference step and separates semantic operations from syntactic operations, eliminating cross-step contamination by enforcing explicit input passing. This work demonstrates that structured intermediate representations can bridge human intuition and machine rigor while maintaining full transparency. The multi-format ecosystem enables inspection by developers, domain experts, and auditors in formats suited to their needs (Guan et al., 2025).

### Theme 5: Systematic Taxonomies and Survey Frameworks

The field shows maturation through the development of comprehensive taxonomies and systematic survey frameworks. Cao et al. (2025) categorize LLM-based planning methodologies into three principal approaches: External Module Augmented Methods, Finetuning-based Methods, and Searching-based Methods. Aghzal et al. (2025) provide a critical survey examining both successes and shortcomings of LLMs in automated planning. Puerta-Merino et al. (2025) present a taxonomy of integration methods for hierarchical planning and provide standardized benchmark datasets. These survey efforts reflect a field moving toward systematic understanding and evaluation frameworks.

### Theme 6: Inference-Time Planning Behavior and Context Effects

Recent work examines the puzzling gap between LLMs' acquired sequence-level planning abilities and their apparent short-sighted behavior at inference time. Yan et al. (2026) propose a Bayesian account grounding planning behavior in the evolving generative context, demonstrating that accumulated self-generated context drives a planning-shift during inference that creates the appearance of compromised planning behavior. This theoretical work provides empirical evidence through controlled experiments showing how conditioning on self-generated sequences can reduce initial bias and alter planning strength.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key findings. First, there is broad agreement that LLMs demonstrate remarkable capacity for multi-step reasoning and generalization across domains, but have significant limitations in performance when handling intricacies of long-horizon reasoning (Aghzal et al., 2025; Monti et al., 2026; Schepanowski & Ling, 2025). Second, the literature consistently finds that LLMs are not well-suited to serve as standalone planners due to brittle internal state representations and weak heuristic planning capabilities (Schepanowski & Ling, 2025; Tantakoun et al., 2025). Third, there is consensus that hybrid approaches combining LLMs with traditional planning methods, formal specifications, or external tools offer the most promising path forward (Aghzal et al., 2025; Guan et al., 2025; Puerta-Merino et al., 2025; Tantakoun et al., 2025).

**Disagreements**: The surveyed literature shows less disagreement on fundamental claims, reflecting a relatively young field still establishing baseline findings. However, there is variation in optimism about the potential for improvement through different approaches. While Monti et al. (2026) suggest that inherent architectural limitations might not be overcome by test-time scaling alone, Srivastava et al. (2026) demonstrate substantial accuracy gains through their multi-stage framework, suggesting that architectural innovations at the system level can achieve significant improvements even if individual model capabilities remain constrained. Additionally, Yan et al. (2026) focus on characterizing rather than solving the planning behavior gap, offering a theoretical explanation that differs from the more solution-oriented approaches of other papers.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, most papers note limitations "not stated in abstract," suggesting that detailed discussion of limitations may be underrepresented in abstracts or that this is an emerging field still developing critical self-assessment practices. Second, while multiple papers identify fundamental architectural limitations in LLM planning capabilities, few provide concrete pathways for overcoming these constraints beyond general calls for hybrid approaches (Schepanowski & Ling, 2025; Monti et al., 2026). Third, the integration of LLMs into hierarchical planning remains largely unexplored, with Puerta-Merino et al. (2025) noting that LLM planners exhibited only 3% correct plans with none achieving correct hierarchical decomposition. Fourth, there is a gap in understanding how to maintain explicit state and perform structured search within LLM architectures, identified as necessary for further progress (Schepanowski & Ling, 2025). Finally, while several papers propose frameworks and taxonomies, there is limited empirical validation across diverse domains and tasks, suggesting a need for more comprehensive benchmarking and evaluation studies.

## Per-Paper Annotations

### Aghzal et al. (2025)

**Research question**: What are the capabilities and limitations of Large Language Models when applied to automated planning tasks?
**Methodology**: The authors conduct a critical survey investigating existing research on LLMs in automated planning, examining both successes and shortcomings. They analyze LLM performance on long-horizon reasoning tasks and advocate for hybrid approaches combining LLMs with traditional planning methods.
**Key findings**:
- LLMs demonstrate remarkable capacity for multi-step reasoning and generalization across domains
- LLMs have significant limitations in performance when handling intricacies of long-horizon reasoning
- LLMs are not well-suited to serve as standalone planners due to these limitations
- LLMs present enormous opportunity to enhance planning applications when combined with other approaches
- A balanced methodology leveraging LLM flexibility alongside traditional planning rigor is recommended
**Limitations**: not stated in abstract

### Cao et al. (2025)

**Research question**: How can LLM-based planning approaches be systematically categorized and what evaluation frameworks exist for assessing their performance?
**Methodology**: The authors present a comprehensive systematic review structured around theoretical foundations, a taxonomy of LLM-based planning methodologies categorized into three principal approaches (External Module Augmented Methods, Finetuning-based Methods, and Searching-based Methods), and a summary of evaluation frameworks including benchmark datasets and metrics.
**Key findings**:
- LLM-based planning methodologies can be categorized into three principal approaches: External Module Augmented Methods, Finetuning-based Methods, and Searching-based Methods
- External Module Augmented Methods combine LLMs with additional components for planning
- Finetuning-based Methods use trajectory data and feedback signals to adjust LLMs for improved planning abilities
- Searching-based Methods decompose complex tasks and navigate planning space or enhance decoding strategies
- Existing evaluation frameworks include benchmark datasets, evaluation metrics, and performance comparisons between representative methods
**Limitations**: not stated in abstract

### Guan et al. (2025)

**Research question**: How can AI workflows be made auditable by addressing context pollution and implicit data flow in LLM-based multi-step reasoning?
**Methodology**: The authors present NormCode, a semi-formal language that enforces data isolation at each inference step and separates semantic operations (probabilistic LLM reasoning) from syntactic operations (deterministic data flow). A four-phase compilation pipeline transforms natural language intent into executable JSON repositories, with a visual Canvas application for graph visualization and breakpoint debugging.
**Key findings**:
- NormCode eliminates cross-step contamination by enforcing explicit input passing at each inference step
- The multi-format ecosystem (NCDS, NCD, NCN, NCDN files) enables inspection by developers, domain experts, and auditors in formats suited to their needs
- The approach achieved full accuracy on base X addition tasks
- The NormCode compiler was validated through self-hosted execution
- Structured intermediate representations can bridge human intuition and machine rigor while maintaining full transparency
**Limitations**: not stated in abstract

### Monti et al. (2026)

**Research question**: What are the long-horizon planning capabilities of state-of-the-art Large Reasoning Models?
**Methodology**: The study proposes a novel benchmark based on Sokoban puzzles, intentionally simplified to isolate long-horizon planning from state persistence, and systematically assesses planning and long-horizon reasoning capabilities of LRMs.
**Key findings**:
- Planning performance consistently degrades when more than 25 moves are required to reach the solution
- This suggests a fundamental constraint on forward planning capacity in LRMs
- Equipping LRMs with PDDL parsing, validation, and solving tools allows for modest improvements
- Inherent architectural limitations might not be overcome by test-time scaling approaches alone
**Limitations**: The benchmark uses intentionally simplified Sokoban puzzles to isolate long-horizon planning from state persistence

### Puerta-Merino et al. (2025)

**Research question**: How can Large Language Models be integrated into Hierarchical Planning?
**Methodology**: The study presents a taxonomy of integration methods exploring how LLMs can be utilized within the HP life cycle, provides a benchmark with a standardized dataset, and presents initial results for a state-of-the-art HP planner and LLM planner.
**Key findings**:
- The integration of LLMs into Hierarchical Planning remains largely unexplored
- A taxonomy of integration methods was developed to address this gap
- A standardized benchmark dataset was provided for evaluating future LLM-based HP approaches
- The LLM planner exhibited limited performance with only 3% correct plans and none with correct hierarchical decomposition
**Limitations**: The LLM planner baseline shows very limited performance, indicating significant challenges for future approaches

### Schepanowski and Ling (2025)

**Research question**: What is the capacity of large language models for planning and stateful reasoning without external tools?
**Methodology**: The study tests four models under common prompting conditions (Zero-Shot, Chain-of-Thought, Algorithm-of-Thought) and with tiered corrective feedback using the 8-puzzle task, then examines models with an external move validator.
**Key findings**:
- Feedback improves success rates for some model-prompt combinations
- Many successful runs are long, computationally expensive, and indirect
- None of the models solve any puzzles even with an external move validator providing only valid moves
- Models exhibit brittle internal state representations leading to frequent invalid moves
- Models show weak heuristic planning, entering loops or selecting actions that do not reduce distance to the goal
**Limitations**: Current LLMs have substantial limitations in planning without external tools such as code interpreters; further progress may require mechanisms for maintaining explicit state and performing structured search

### Srivastava et al. (2026)

**Research question**: How can high-quality natural language executable plans be generated for complex tasks despite LLM reliability degradation with increasing task complexity?
**Methodology**: The study introduces GRASP, a strategy-aware multi-stage planning framework that decouples the planning pipeline across specialized modules: GenPlan (pre-compiles global macro-guidelines), RevPlan (explores alternative localized strategies), and VerPlan (evaluates trajectories using a multi-criteria discriminator).
**Key findings**:
- GRASP establishes a new state-of-the-art frontier across diverse datasets
- Substantial accuracy gains over direct LLM planners on Natural Plan Calendar Scheduling (~12.4%↑), ZebraLogic (~30.8%↑), and SciBench Math
- GRASP completely flattens the multi-task degradation penalty under multi-task scaling
- In interleaved dual-task environments, GRASP achieves an absolute accuracy gain of up to 16.7% over direct LLM planners
- GRASP outperforms frontier reasoning models (such as GPT-5-mini) by a margin of 14.5%
**Limitations**: not stated in abstract

### Tantakoun et al. (2025)

**Research question**: How can Large Language Models be leveraged to formalize and refine planning specifications to support reliable off-the-shelf automated planning?
**Methodology**: The authors conduct a systematic survey reviewing current research on integrating LLMs with Automated Planning, positioning LLMs as tools for formalizing and refining planning specifications to support traditional AP planners, and analyzing methodologies, challenges, and future directions.
**Key findings**:
- LLMs excel in various natural language tasks but struggle with long-horizon planning problems requiring structured reasoning
- Integrating neuro-symbolic approaches within Automated Planning and NLP communities addresses LLM planning limitations
- LLMs can serve as tools for formalizing and refining planning specifications to support off-the-shelf AP planners
- Identifying optimal AP deployment frameworks introduces new challenges
- The survey highlights methodologies and identifies critical challenges and future directions for joint NLP and Automated Planning research
**Limitations**: not stated in abstract

### Wang et al. (2024)

**Research question**: How can cooperative multi-agent frameworks enhance LLM reasoning capabilities for complex multi-step problems?
**Methodology**: The authors propose CoPlanner, a cooperative multi-agent reasoning framework that separates reasoning steps between a planning agent (providing high-level strategic hints) and a reasoning agent (following hints and inferring answers). The planning agent's policy is trained through interactive reasoning using Proximal Policy Optimization (PPO).
**Key findings**:
- CoPlanner consists of two LLM agents: a planning agent and a reasoning agent with distinct duties
- The planning agent provides high-level strategic hints while the reasoning agent follows these hints to infer answers
- LLaMA-3-8B-based CoPlanner outperforms the previous best method by 9.94% on LogiQA
- CoPlanner outperforms the previous best method by 3.09% on BBH
- Guidance from the planning agent and effective cooperation between agents contribute to superior performance on multi-step reasoning problems
**Limitations**: not stated in abstract

### Yan et al. (2026)

**Research question**: Why does LLM planning behavior at inference time appear short-sighted and inconsistent with their acquired sequence-level planning abilities?
**Methodology**: The study proposes a Bayesian account grounding planning behavior in the evolving generative context and validates it through two controlled experiments: a random-generation task and a Gaussian-sampling task.
**Key findings**:
- Accumulated self-generated context drives a planning-shift during inference
- This creates the appearance of compromised planning behavior
- The random-generation task demonstrates constrained planning under human prompts and increasing planning strength as self-generated context accumulates
- The Gaussian-sampling task shows reduced initial bias when conditioning on self-generated sequences
**Limitations**: The study provides a theoretical explanation and empirical evidence but focuses on characterizing rather than solving the planning behavior gap

## References

Aghzal, M., Plaku, E., Stein, G. J., & Yao, Z. (2025). A survey on large language models for automated planning. arXiv. https://arxiv.org/abs/2502.12435

Cao, P., Men, T., Liu, W., Zhang, J., Li, X., Lin, X., Sui, D., Cao, Y., Liu, K., & Zhao, J. (2025). Large language models for planning: A comprehensive and systematic survey. arXiv. https://arxiv.org/abs/2505.19683

Guan, X., Li, Y., Wu, Z., & Zhang, R. (2025). NormCode: A semi-formal language for auditable AI planning. arXiv. https://arxiv.org/abs/2512.10563

Monti, S., Nicolini, C., Pellegrini, G., Staiano, J., & Lepri, B. (2026). SokoBench: Evaluating long-horizon planning and reasoning in large language models. arXiv. https://arxiv.org/abs/2601.20856

Puerta-Merino, I., Núñez-Molina, C., Mesejo, P., & Fernández-Olivares, J. (2025). A roadmap to guide the integration of LLMs in hierarchical planning. arXiv. https://arxiv.org/abs/2501.08068

Schepanowski, C., & Ling, C. (2025). On the limits of innate planning in large language models. arXiv. https://arxiv.org/abs/2511.21591

Srivastava, A., A., M., Khojastepour, M., Chakradhar, S., & Ulukus, S. (2026). GRASP: Generating, revising, and assessing for strategic planning with agentic AI. arXiv. https://arxiv.org/abs/2609.30147

Tantakoun, M., Zhu, X., & Muise, C. (2025). LLMs as planning formalizers: A survey for leveraging large language models to construct automated planning models. arXiv. https://arxiv.org/abs/2503.18971

Wang, D., Ye, Z., Fang, F., & Li, L. (2024). Cooperative strategic planning enhances reasoning capabilities in large language models. arXiv. https://arxiv.org/abs/2410.20007

Yan, H., Zhu, J.-Q., & Sanborn, A. (2026). Large language models can take false first steps at inference-time planning. arXiv. https://arxiv.org/abs/2602.02991
