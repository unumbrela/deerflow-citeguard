# Systematic Literature Review: Tool Use in Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "tool use", filtered to category cs.AI, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on tool use in large language models has rapidly evolved over the past two years, with research converging on several critical fronts: benchmarking and evaluation methodologies, training strategies for improving tool use capabilities, and understanding the internal mechanisms governing tool-use decisions. The surveyed papers collectively reveal that while tool-augmented LLMs have demonstrated significant capabilities, current models exhibit substantial limitations including poor constraint adherence (no model exceeds 20% completion under strict constraints), various failure modes (tool-skipping, result-ignoring, output-fabrication), and inefficient tool invocation patterns. A notable tension exists in the literature between approaches advocating for enhanced tool use training and those finding that excessive tool use can be counterproductive, suggesting that adaptive, context-aware tool selection rather than frequent invocation may be the key to effective agentic systems.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query `tool use`, filtered to category cs.AI, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmarking and Evaluation Frameworks

A dominant theme across the surveyed literature is the development of comprehensive benchmarks for evaluating tool use capabilities. Four papers specifically focus on creating diagnostic frameworks that move beyond simple accuracy metrics. Soni (2026) introduced ToolFailBench, which evaluates tool-use failures across 1,000 tasks in finance, medicine, law, cybersecurity, and real estate, categorizing failures into Tool-Skip, Result-Ignore, Output-Fabrication, and Unnecessary-Tool-Use. The benchmark revealed that the best model achieves only 86.33% Clean Tool-Use Rate, with models of similar aggregate scores failing in fundamentally different ways.

He et al. (2025) developed TRAJECT-Bench, which evaluates not just final answers but the entire tool usage trajectory, including tool selection, parameterization, and ordering correctness. Their analysis revealed failure modes such as similar tool confusion and parameter-blind selection, with a particular bottleneck identified in transitioning from short to mid-length trajectories. Ye et al. (2026) introduced CCTU, focusing specifically on tool use under complex constraints, finding that no evaluated model achieves above 20% task completion when strict adherence to all constraints is required.

Most recently, Nam et al. (2026) proposed TURTLE, an unsupervised environment design approach that evolves benchmarks automatically using three LLM agents (proposer, solver, feedback generator), achieving a 165% increase in hard tasks on AppWorld while eliciting broader failure modes than static benchmarks.

### Theme 2: Training Strategies for Enhanced Tool Use

Multiple papers investigate how training methodologies can improve tool use capabilities. Jiang et al. (2026) presented MidTool, demonstrating that dedicated mid-training—rather than relying solely on post-training—significantly improves general tool use capabilities. Their pipeline combines large-scale web, PDF, and code data with synthesized supervision from real-world tool APIs, showing consistent improvements across BFCL, tau2-Bench, and MCP Universe benchmarks when applied to Qwen3 models.

Yin et al. (2024) explored a specialized application in mathematical reasoning, combining tool use with multi-perspective data augmentation. Their MuMath-Code approach integrates external Python interpreters with augmented training data through a two-stage training strategy, achieving state-of-the-art performance among open methods (90.7% on GSM8K, 55.1% on MATH with the 70B model).

Zhang et al. (2026) focused on video deep research, developing AdaVDR with adaptive tool use and reflection capabilities. Their approach uses model-conditioned tool necessity filtering and NASA-GRPO, a necessity-aware segment-guided credit assignment method, outperforming base models by 15.20-29.00 percentage points on video deep research benchmarks.

### Theme 3: Tool Use Efficiency and Adaptive Selection

A critical emerging theme concerns not whether to use tools, but when and how frequently. Kim et al. (2026) identified a "tool-use collapse phenomenon" in visual chain-of-thought agents, where models progressively stop using tools while still achieving higher task accuracy. Their research revealed a striking asymmetry: completely eliminating tool use degrades performance, yet incentivizing tool use yields only marginal gains despite substantially increasing usage. They propose viewing tools as scaffolding, where broader exploration over language generation and visual tool invocation improves reasoning despite declining tool usage frequency.

This efficiency perspective is echoed in AdaVDR (Zhang et al., 2026), which specifically addresses unnecessary video tool calls that incur additional costs and failure risk. Their model-conditioned tool necessity filtering removes tools that can be bypassed using video understanding and internal model knowledge, suggesting that intelligent tool selection rather than maximal tool invocation is key to effective agentic systems.

### Theme 4: Internal Mechanisms and Causal Control

Understanding the internal representations underlying tool-use decisions represents a more theoretical but crucial direction. Chen et al. (2026) investigated whether tool-use decisions have stable internal representations that can be manipulated for causal control. They demonstrated that steering vectors extracted from heading-anchor positions exert bidirectional causal control over tool-invocation behavior across five open-source models and three domains.

However, their geometric analysis revealed unexpected complexity: tool-invocation steps exhibit diffuse, bimodal alignment with suppression vectors rather than the clean linear structure predicted by linear encoding accounts. Different tool types recruit largely distinct internal signatures with low cross-tool feature overlap, suggesting that the non-parametric nature of tools distinguishes them from parametrically grounded concepts. This work opens fundamental questions about how LLMs internally represent and reason about external tools.

### Theme 5: Domain-Specific Applications and Generalization

The literature spans diverse application domains, revealing both specialized solutions and generalization challenges. Mathematical reasoning (Yin et al., 2024), visual reasoning (Kim et al., 2026; Zhang et al., 2026), robotics (Akbulut et al., 2026), and general agentic systems (Jiang et al., 2026; Nam et al., 2026) each present unique tool use requirements.

Akbulut et al. (2026) explored creative robot tool use through counterfactual reasoning, proposing a causal framework where robots identify tools for uses beyond their primary objectives. Their approach grounds tool use in physics through dynamics models and VLM-based feature suggestion, demonstrating successful transfer across novel objects in reaching, scooping, and stepping tasks.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. All papers affirm that tool use is critical for advancing LLM agent capabilities beyond parametric knowledge. There is consensus that current models exhibit significant limitations, with evaluation papers consistently revealing low performance under rigorous testing (Soni, 2026; Ye et al., 2026; He et al., 2025). Multiple papers converge on the insight that evaluation must move beyond final accuracy to measure trajectory quality, failure modes, and constraint adherence (He et al., 2025; Soni, 2026; Nam et al., 2026). Additionally, there is agreement that training specifically targeted at tool use capabilities yields improvements over generic training approaches (Jiang et al., 2026; Yin et al., 2024; Zhang et al., 2026).

**Disagreements**: A notable tension exists regarding optimal tool use frequency. While MidTool (Jiang et al., 2026) and MuMath-Code (Yin et al., 2024) advocate for enhanced tool use capabilities through dedicated training, Kim et al. (2026) found that incentivizing tool use yields only marginal gains and that tools function better as scaffolding for exploration rather than frequently invoked components. This suggests the field has not yet resolved when tool use should be encouraged versus when models should rely on internal reasoning. Additionally, while most papers assume more tool use is desirable, the activation steering work (Chen et al., 2026) shows that suppressing unnecessary tool use is most effective in domains where parametric reasoning suffices, indicating domain-dependent optimal strategies.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, **generalization across architectures** remains limited—most studies evaluate only specific model families (Qwen3 in Jiang et al., 2026; Llama in Yin et al., 2024; Gemma 4 in Nam et al., 2026), leaving open whether findings transfer broadly. Second, **self-refinement capabilities** are consistently identified as a bottleneck, with Ye et al. (2026) noting that LLMs demonstrate limited capacity for self-refinement even after receiving detailed feedback on constraint violations.

Third, the **internal mechanisms of tool-use decisions** remain poorly understood. While Chen et al. (2026) made initial progress, they explicitly note that the relationship between geometric irregularity in internal representations and observed causal effectiveness remains an open question. Fourth, most work focuses on **domain-specific applications** (mathematics, vision, robotics), with limited investigation of truly general tool use capabilities that transfer across domains.

Finally, there is a gap in understanding **long-horizon tool use** in real-world deployments. While TURTLE (Nam et al., 2026) and TRAJECT-Bench (He et al., 2025) begin addressing trajectory length, the literature lacks studies of tool use over extended interactions with accumulated context, error recovery, and evolving user intent.

## Per-Paper Annotations

### Akbulut et al. (2026)

**Research question**: How can robots identify and creatively use tools for tasks beyond their primary intended objectives?
**Methodology**: The authors propose a causal reasoning framework that discovers causal relationships between tools and tasks through simulated experiments in a dynamics model, decoupling causal discovery into VLM-based feature suggestion and counterfactual tool generation via targeted geometric and physical feature perturbations, with skill transfer via keypoint matching.
**Key findings**:
- Identifying causal features and grounding them in physical tool properties leads to more reliable tool selection
- The approach successfully demonstrates creative tool use in diverse scenarios: reaching with different sticks, scooping with various items, and using boxes as stepping platforms
- Counterfactual reasoning enables stronger skill keypoint transfer across novel objects
- Reconstructing tasks in a dynamics model grounds tool use in the physics of the problem
**Limitations**: The approach requires a dynamics model for simulation; evaluation is limited to specific tool-use scenarios (reaching, scooping, stepping) and may not generalize to all robotic manipulation tasks.

### Chen et al. (2026)

**Research question**: Do tool-use decisions in large language models have stable internal representations that can be extracted and manipulated for causal control?
**Methodology**: The researchers extracted steering vectors from heading-anchor positions and tested their bidirectional causal control over tool-invocation behavior across five open-source models and three domains, complemented by geometric analysis of the internal representations.
**Key findings**:
- Steering vectors extracted from heading-anchors exert bidirectional causal control over tool-invocation behavior across multiple models and domains
- Tool use suppression is most effective in domains where parametric reasoning suffices
- Tool-invocation steps exhibit diffuse, bimodal alignment with the suppression vector rather than clean linear structure
- Different tool types recruit largely distinct internal signatures with low cross-tool feature overlap
**Limitations**: The geometric irregularity's relationship to observed causal effectiveness remains an open question; the non-parametric nature of tools distinguishes them from parametrically grounded concepts, limiting generalizability.

### He et al. (2025)

**Research question**: How can we comprehensively evaluate LLMs' tool use capability beyond final answers by considering the detailed tool usage trajectory?
**Methodology**: TRAJECT-Bench pairs high-fidelity executable tools across practical domains with production-style API-grounded tasks, synthesizes trajectories varying in breadth (parallel calls) and depth (interdependent chains), and reports trajectory-level diagnostics including tool selection, argument correctness, and dependency/order satisfaction.
**Key findings**:
- Analyses reveal failure modes including similar tool confusion and parameter-blind selection
- Scaling behavior shows a bottleneck when transitioning from short to mid-length trajectories
- Trajectory-level diagnostics provide actionable guidance beyond final accuracy metrics
- Tool diversity and trajectory length significantly impact LLM performance
**Limitations**: The benchmark focuses on specific practical domains and production-style APIs; evaluation may not capture all real-world tool-use scenarios or generalize to non-API-based tools.

### Jiang et al. (2026)

**Research question**: Can dedicated mid-training improve general tool use capabilities in large language models rather than relying entirely on post-training?
**Methodology**: The authors present MidTool, an open corpus construction pipeline combining large-scale web, PDF, and code data with synthesized supervision from real-world tool APIs, MCP skills, and document-grounded workflows, then mid-trained Qwen3-4B-Base and Qwen3-8B-Base followed by SFT and RL post-training.
**Key findings**:
- MidTool-Mix consistently improves downstream performance under both supervised fine-tuning and reinforcement learning
- Improvements are observed across BFCL, tau2-Bench, and MCP Universe benchmarks
- General tool use benefits from dedicated mid-training rather than being left entirely to post-training
- The pipeline teaches models to recognize tool affordances, ground arguments from context, compose tool call workflows, and recover from incomplete information
**Limitations**: Evaluation was limited to Qwen3 models (4B and 8B base variants); results may not generalize to other model architectures or sizes without additional validation.

### Kim et al. (2026)

**Research question**: What is the role of visual tools in complex visual reasoning tasks beyond simple visual search, and how does tool usage relate to reasoning performance?
**Methodology**: The authors investigate tool use in challenging tasks including 3D spatial reasoning and medical visual question answering, identify a tool-use collapse phenomenon, and add an entropy regularization term to encourage diverse rollout exploration during training.
**Key findings**:
- Tool-use collapse phenomenon: models progressively stop using tools while still achieving higher task accuracy
- Clear asymmetry exists: eliminating tool use degrades performance, but incentivizing tool use yields only marginal gains despite substantially increasing usage
- Both vanilla training and tool-use encouragement reduce rollout diversity
- Entropy regularization achieves best performance despite gradually declining tool usage
- Tools function better as scaffolding for broader exploration rather than frequently invoked components
**Limitations**: The study focuses on specific visual reasoning tasks (3D spatial reasoning, medical VQA); findings may not generalize to non-visual domains or other tool-use paradigms.

### Nam et al. (2026)

**Research question**: How can tool use benchmark data generation be scaled without relying on human supervision or domain-specific constraints?
**Methodology**: The authors propose TURTLE, an Unsupervised Environment Design approach that evolves existing tasks using three LLM agents (proposer, solver, feedback generator), where the proposer is rewarded for generating difficult yet solvable tasks based on the solver's empirical performance.
**Key findings**:
- TURTLE achieved a 165% increase in the percentage of hard tasks on AppWorld
- Evolved tasks increase diversity in terms of reasoning requirements and simultaneous tool interactions
- The approach elicits a broader range of failure modes than original benchmark tasks
- TURTLE produces self-tuning test suites adaptable to different environment requirements including user simulators, document retrieval, and multi-app interactions
**Limitations**: Empirical results were demonstrated primarily on Gemma 4 31B-it; the approach may require tuning for different model architectures and the quality of evolved tasks depends on the proposer and feedback generator capabilities.

### Soni (2026)

**Research question**: How do LLM agents fail when using tools, and what failure modes are hidden by aggregate benchmark scores?
**Methodology**: ToolFailBench is introduced as a diagnostic benchmark with 1,000 tasks across finance, medicine, law, cybersecurity, and real estate; each trace is labeled with failure types (Tool-Skip, Result-Ignore, Output-Fabrication, Unnecessary-Tool-Use) using a rule classifier and two LLM judges aggregated by majority vote.
**Key findings**:
- The best model reaches only 86.33% Clean Tool-Use Rate, showing faithful tool use is not saturated
- Models with similar aggregate scores fail in fundamentally different ways
- Llama-3.1 models exhibit an Always-Call pattern, calling tools unnecessarily
- At the same parameter scale, Llama-3.1-70B and Qwen2.5-72B differ by 89 percentage points on control-task accuracy
- Tool-use evaluation should measure not only whether agents call tools, but whether they use outputs correctly and avoid tools when unnecessary
**Limitations**: Evaluation is limited to 19 headline models across five specific domains; the benchmark may not capture all failure modes or generalize to other task domains.

### Ye et al. (2026)

**Research question**: How well do large language models perform tool use when required to follow explicit complex constraints?
**Methodology**: The authors introduce CCTU, a benchmark with 200 test cases across 12 constraint categories spanning four dimensions (resource, behavior, toolset, response), and develop an executable constraint validation module for step-level validation during multi-turn interactions.
**Key findings**:
- No evaluated model achieves a task completion rate above 20% when strict adherence to all constraints is required
- Models violate constraints in over 50% of cases, particularly in the resource and response dimensions
- LLMs demonstrate limited capacity for self-refinement even after receiving detailed feedback on constraint violations
- Each test case involves an average of seven constraint types with prompts exceeding 4,700 tokens
**Limitations**: The benchmark evaluated only nine LLMs and may not cover all possible constraint types; the constraint validation module requires executable environments which may limit applicability.

### Yin et al. (2024)

**Research question**: How can tool-use LLMs with Python interpreters be effectively integrated with data augmentation methods to enhance mathematical reasoning capabilities?
**Methodology**: The authors augment math questions via multi-perspective data augmentation, synthesize code-nested solutions, and employ a two-stage training strategy: first fine-tuning Llama-2 on pure CoT data, then training on code-nested data to produce MuMath-Code models that interact with external Python interpreters during inference.
**Key findings**:
- MuMath-Code-7B achieves 83.8% on GSM8K and 52.4% on MATH benchmarks
- MuMath-Code-70B achieves state-of-the-art performance among open methods with 90.7% on GSM8K and 55.1% on MATH
- The two-stage training strategy effectively leverages augmented data for improved performance
- Combining tool use with data augmentation outperforms either approach alone
**Limitations**: The approach is evaluated primarily on Llama-2 models and standard math benchmarks (GSM8K, MATH); generalization to other model architectures or reasoning domains is not explored.

### Zhang et al. (2026)

**Research question**: How can video deep research agents reduce unnecessary video tool calls while maintaining performance on tasks requiring both video understanding and external knowledge retrieval?
**Methodology**: The authors develop AdaVDR with adaptive tool use and reflection capabilities, using model-conditioned tool necessity filtering to remove bypassable tools and NASA-GRPO, a necessity-aware segment-guided credit assignment method for constructing normalized tool-level rewards during training.
**Key findings**:
- AdaVDR outperforms the base model by 15.20 percentage points on the VDR-EE benchmark
- AdaVDR outperforms the base model by 29.00 percentage points on the existing VideoDR benchmark
- Model-conditioned tool necessity filtering effectively removes tools that can be bypassed using video understanding and internal model knowledge
- NASA-GRPO's segment-guided evidence contribution and tool necessity evaluation improves adaptive tool selection capabilities
**Limitations**: The approach requires specialized training data construction with adaptive trajectories; generalization to non-video domains or tasks without clear segment boundaries may require additional adaptation.

## References

Akbulut, M. T., Satheesh, V., Jaafar, A., Ahmetoglu, A., Parr, S., Ganeshan, A., Vats, S., & Konidaris, G. (2026). Creative robot tool use by counterfactual reasoning. arXiv. https://arxiv.org/abs/2605.05411

Chen, Y., Siu, V., Liu, Y., Song, D., & Wang, C. (2026). Controlling tool use with heading-specific activation steering. arXiv. https://arxiv.org/abs/2607.05790

He, P., Dai, Z., He, B., Liu, H., Tang, X., Lu, H., Li, J., Ding, J., Mukherjee, S., Wang, S., Xing, Y., Tang, J., & Dumoulin, B. (2025). TRAJECT-Bench: A trajectory-aware benchmark for evaluating agentic tool use. arXiv. https://arxiv.org/abs/2510.04550

Jiang, F., Wang, Y., Liu, B., Wang, Z., Xu, C., Yao, Z., Poovendran, R., & He, Y. (2026). MidTool: Mid-training data synthesis for agentic tool use. arXiv. https://arxiv.org/abs/2608.20314

Kim, D.-H., Tan, R., & Kim, D. (2026). Diversity over frequency: Rethinking tool use in visual chain-of-thought agents. arXiv. https://arxiv.org/abs/2606.00096

Nam, H. A., Dennis, M., Jaques, N., & Chang, M. (2026). Evolving self-tuning benchmarks for long-horizon tool use. arXiv. https://arxiv.org/abs/2610.27307

Soni, H. (2026). ToolFailBench: Diagnosing tool-use failures in LLM agents. arXiv. https://arxiv.org/abs/2607.04686

Ye, J., Zhang, G., Fu, W., Li, Z., Gui, T., Zhang, Q., & Huang, X. (2026). CCTU: A benchmark for tool use under complex constraints. arXiv. https://arxiv.org/abs/2603.15309

Yin, S., You, W., Ji, Z., Zhong, G., & Bai, J. (2024). MuMath-Code: Combining tool-use large language models with multi-perspective data augmentation for mathematical reasoning. arXiv. https://arxiv.org/abs/2405.07551

Zhang, X., Fan, X., Yan, S., He, E., Liu, Z., Zou, Z., Zhang, G., Wu, Y., Gao, Z., & Xue, H. (2026). AdaVDR: Adaptive tool use and reflection for video deep research. arXiv. https://arxiv.org/abs/2608.25559
