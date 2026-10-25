# Systematic Literature Review: Robot Manipulation with Foundation Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "robot manipulation", filtered to category cs.RO, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of robot manipulation with foundation models is rapidly evolving, with recent work addressing fundamental challenges in sim2real transfer, long-horizon task execution, multi-modal perception, and standardized evaluation. The surveyed literature reveals a field maturing beyond proof-of-concept demonstrations toward rigorous benchmarking and real-world deployment. Key advances include diffusion-based approaches for bridging reality gaps, hierarchical architectures for continual learning, and compact vision-language-action models that achieve competitive performance under tight computational budgets. However, significant challenges remain: semantic generalization struggles despite internet-scale pre-training, long-horizon task success rates collapse beyond 3-4 subgoals, and part-level manipulation remains poorly solved. The literature shows converging agreement on the need for standardized evaluation frameworks and multi-modal representations, while disagreements persist on whether large-scale pre-training or task-specific architectures offer better paths to generalization.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query `robot manipulation`, filtered to category cs.RO, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. One paper (EmbodiedMAE) had truncated metadata in the source material, limiting the depth of analysis for that contribution.

## Themes

### Theme 1: Bridging the Reality Gap Through Generative Models

A central challenge in robot manipulation is the sim2real gap — the discrepancy between simulated training environments and real-world deployment. Recent work has leveraged generative models, particularly diffusion frameworks, to address this challenge through novel paradigms. Liang et al. (2025) propose RealD²iff, which inverts the conventional denoising perspective by learning to synthesize realistic sensor noise from clean simulated depth data. This clean-to-noisy paradigm uses a hierarchical coarse-to-fine diffusion framework that decomposes depth noise into global structural distortions and fine-grained local perturbations, enabling zero-shot sim2real transfer without real-world fine-tuning.

Complementary work by Zhang et al. (2026) addresses cross-embodiment transfer from human videos to robot manipulation. Their Causal-Beam-Guided Subtask Transfer (CBST) framework identifies which contextual conditions and interaction dependencies should be retained when transferring knowledge across morphologically different agents. By grounding manipulation-related representations from human videos in task-level semantic variables using robot demonstrations, CBST enables robots to generate actions from their own observations without requiring direct human-robot motion correspondence. Both approaches share the insight that the key challenge is not acquiring more data, but rather learning the right inductive biases for transferring knowledge across domains — whether sim-to-real or human-to-robot.

### Theme 2: Standardized Evaluation and Benchmarking

The literature reveals strong convergence around the need for rigorous, reproducible evaluation frameworks. Gao et al. (2025) introduce STAR-Gen, a taxonomy structuring generalization evaluation along three dimensions: visual, semantic, and behavioral generalization. Their case studies reveal a critical finding: open-source vision-language-action models struggle with semantic generalization despite internet-scale language pre-training, challenging assumptions about transfer from language foundation models to embodied tasks.

Multiple papers contribute benchmark datasets targeting specific manipulation challenges. Yin et al. (2025) present PartInstruct, the first large-scale benchmark for part-level instruction following, comprising 513 object instances with part-level annotations and 1,302 fine-grained manipulation tasks. Petkov et al. (2026) introduce LADDER, a long-horizon benchmark scaling from 1 to 10 subgoals within the same environment, revealing that low-level policies achieve 85.4% success on single-subgoal tasks but collapse to near zero on extended sequences. Droß et al. (2026) contribute PhyRoGen, a procedural content generation framework for automatically creating solvable physical manipulation puzzles with interlocking dependencies. Collectively, these benchmarks expose specific failure modes — semantic grounding, part-level reasoning, and long-horizon execution — that were previously obscured by heterogeneous evaluation protocols.

### Theme 3: Long-Horizon Task Execution

A recurring challenge across the literature is robust execution of multi-stage manipulation tasks. The LADDER benchmark (Petkov et al., 2026) provides the most comprehensive analysis, demonstrating that orchestration paradigms using tool selection with large language models (GPT-Policy on GPT-6 Astra) achieve ~62% success on long-horizon tasks, substantially outperforming learned-policy methods at ~25%. Critically, the bottleneck is not high-level planning but physical execution errors of low-level policies.

ProgVLA (Kim et al., 2026) addresses this through explicit progress tracking in a compact 0.1B-parameter vision-language-action model. By integrating auxiliary progress heads trained with offline reinforcement learning objectives, ProgVLA maintains an internal estimate of task progress and achieves success rates competitive with substantially larger baselines, particularly on long-horizon and multi-object tasks. Similarly, SPECI (Xu & Nie, 2025) proposes a hierarchical continual imitation learning architecture with high-level skill inference and low-level action execution modules, enabling bidirectional knowledge transfer across tasks through an expandable skill codebook. These approaches converge on hierarchical decomposition as essential for long-horizon success, but differ on whether progress should be explicitly represented (ProgVLA) or implicitly learned through skill hierarchies (SPECI).

### Theme 4: Multi-Modal Perception and Representation

Effective manipulation requires integrating information across visual, depth, proprioceptive, and language modalities. EmbodiedMAE (Dong et al., 2025) proposes a unified 3D multi-modal masked autoencoder that simultaneously learns representations across RGB, depth, and point cloud modalities through stochastic masking and cross-modal fusion. Trained on the enhanced DROID-3D dataset, EmbodiedMAE outperforms state-of-the-art vision foundation models across 70 simulation and 20 real-world tasks, particularly in precise tabletop manipulation where spatial perception is critical.

IronMan (Zhang et al., 2026) applies the information bottleneck principle to video-action learning, imposing constraints that suppress irrelevant visual information while preserving action-relevant dynamics. The framework employs a dynamics-aware bottleneck that distills noisy video features into compact world representations, achieving 99.0% success on LIBERO and 79.4% on RoboTwin, with strong out-of-distribution robustness. Both approaches reject naive fusion of all available sensory inputs in favor of selective, task-relevant representation learning — a principle that echoes findings in biological perception systems.

### Theme 5: Efficiency and Scalability

As foundation models grow larger, several papers investigate whether compact, specialized architectures can match or exceed performance of massive pre-trained models. ProgVLA (Kim et al., 2026) demonstrates that a 0.1B-parameter model with appropriate inductive biases — specifically, progress-aware training and learned context resampling — can exceed substantially larger pretrained baselines on long-horizon and harder task tiers. This challenges the assumption that scale alone drives manipulation capability.

The efficiency theme also appears in procedural data generation. PhyRoGen (Droß et al., 2026) automates synthetic dataset creation for manipulation puzzles, generating 24 unique solvable puzzles through six procedural generators. This addresses the data bottleneck that typically constrains manipulation learning, where collecting diverse real-robot experience is costly and time-consuming. Together, these works suggest that architectural innovation and data efficiency may offer more promising paths to deployment than continued scaling alone.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, hierarchical architectures are essential for long-horizon manipulation — all papers addressing multi-stage tasks employ some form of decomposition, whether through skill hierarchies (Xu & Nie, 2025), progress tracking (Kim et al., 2026), or LLM-based orchestration (Petkov et al., 2026). Second, standardized benchmarking is critical — multiple independent groups developed evaluation frameworks (Gao et al., 2025; Yin et al., 2025; Petkov et al., 2026), reflecting field-wide recognition that heterogeneous evaluation has impeded progress measurement. Third, multi-modal integration must be selective rather than exhaustive — both EmbodiedMAE and IronMan demonstrate that intelligent filtering of sensory information outperforms naive fusion.

**Disagreements**: Tensions exist around the role of large-scale pre-training. While vision-language-action models benefit from internet-scale language data, Gao et al. (2025) find these same models struggle with semantic generalization in manipulation contexts, suggesting embodiment-specific learning cannot be bypassed through language pre-training alone. Additionally, there is disagreement on optimal approaches to long-horizon tasks: Petkov et al. (2026) find LLM-based tool selection orchestration substantially outperforms learned policies, while Kim et al. (2026) and Xu & Nie (2025) demonstrate that compact learned models with appropriate inductive biases can achieve competitive performance without incurring the time and cost budgets of LLM inference.

## Gaps and Open Questions

Several critical gaps emerge from the literature. First, **real-world validation remains limited** — multiple papers acknowledge their approaches were validated primarily in simulation (Droß et al., 2026; Zhang et al., 2026), with real-world experiments restricted to constrained environments like toy kitchens (Kim et al., 2026). The sim2real gap, while addressed by RealD²iff (Liang et al., 2025), requires validation across diverse robotic platforms and deployment scenarios.

Second, **semantic grounding remains unsolved** — despite progress on visual and behavioral generalization, Gao et al. (2025) report that VLA models struggle with semantic generalization even with internet-scale language pre-training. This suggests fundamental gaps in how language concepts ground to physical affordances and task semantics.

Third, **computational overhead transparency is lacking** — while ProgVLA (Kim et al., 2026) explicitly targets tight compute budgets, most papers do not report inference latency, memory footprint, or training costs, making it difficult to assess deployment feasibility. The LLM-based orchestration approach (Petkov et al., 2026) explicitly acknowledges "significant time and cost budget" but does not quantify these costs.

Fourth, **cross-embodiment generalization is underexplored** — while CBST (Zhang et al., 2026) addresses human-to-robot transfer, the literature lacks systematic study of robot-to-robot transfer across different morphologies, actuation schemes, and sensor configurations. This limits the practical utility of learned policies for deployment on heterogeneous robot fleets.

Finally, **lifelong learning remains nascent** — only SPECI (Xu & Nie, 2025) explicitly addresses continual adaptation to evolving tasks and environments. As manipulation systems deploy in dynamic real-world settings, the ability to learn new skills without catastrophic forgetting will become increasingly critical.

## Per-Paper Annotations

### Droß et al. (2026)

**Research question**: How can large training datasets for robot manipulation puzzle solving be generated efficiently without time-consuming manual data collection?
**Methodology**: Proposes PhyRoGen, a procedural content generation framework with six concrete generators for creating physical puzzles with interlocking object dependencies, validated through sampling-based planning algorithms and physical simulation.
**Key findings**:
- Generated 24 physical puzzles across six generator types with interlocking dependencies
- All puzzles solvable in 1-300 seconds using sampling-based planning
- Every puzzle verified as manipulatable using KUKA LBR iiwa robot in simulation
- Provides automated synthetic dataset generation crucial for benchmarking and foundation model development
**Limitations**: Validation performed in physical simulation rather than on real hardware; may not capture all complexities of real-world physics, friction, and sensor noise.

### Gao et al. (2025)

**Research question**: How should we measure progress of robot manipulation policies toward generalization, given the current "Wild West" of heterogeneous, non-reproducible evaluation protocols?
**Methodology**: Proposes STAR-Gen taxonomy structured around visual, semantic, and behavioral generalization, instantiated through two real-world benchmarking case studies using Bridge V2 dataset and bimanual ALOHA 2 platform.
**Key findings**:
- Provides comprehensive taxonomy and reproducible guidelines for measuring generalization
- Open-source vision-language-action models struggle with semantic generalization despite internet-scale language pre-training
- Case studies reveal specific failure modes previously obscured by heterogeneous evaluation
- Addresses reproducibility crisis in robotics generalization research
**Limitations**: Focuses on evaluation framework rather than proposing new algorithms; generalization metrics may not capture all dimensions relevant to real-world deployment.

### Kim et al. (2026)

**Research question**: How can reliable robot manipulation be achieved under tight compute and memory budgets while efficiently processing long multi-modal sequences over extended horizons?
**Methodology**: Presents ProgVLA, a compact 0.1B-parameter VLA with multi-modal encoder using two-stage Perceiver resampling and auxiliary progress heads trained with offline RL for advantage-weighted flow-matching imitation learning.
**Key findings**:
- Achieves success rates competitive with larger baselines on multi-task benchmarks
- Exceeds larger models on long-horizon and harder task tiers despite compact size
- Learned context resampler and task-adaptive visual fine-tuning are largest contributors
- Progress-aware training provides consistent gains on long-horizon and multi-object tasks
- Validated in real-world toy-kitchen environments
**Limitations**: Compact architecture may have capacity limits for extremely complex scenarios; toy-kitchen validation may not represent industrial or highly dexterous manipulation requirements.

### Liang et al. (2025)

**Research question**: How can the visual sim2real gap in depth observations be bridged when simulation depth fails to reflect real sensor noise patterns?
**Methodology**: Proposes RealD²iff, a hierarchical coarse-to-fine diffusion framework using clean-to-noisy paradigm with Frequency-Guided Supervision for global structure and Discrepancy-Guided Optimization for local refinement, integrated into six-stage imitation learning pipeline.
**Key findings**:
- Inverts conventional denoising to synthesize realistic depth sensor noise from clean simulation
- Hierarchical decomposition into global distortions and local perturbations enables progressive learning
- Generates real-world-like depth for clean-noisy paired datasets without manual sensor collection
- Achieves zero-shot sim2real transfer with substantially improved real-world performance without fine-tuning
**Limitations**: Requires simulation environment with known clean depth; may not generalize to novel sensor types or extreme environmental conditions not represented in training distribution.

### Petkov et al. (2026)

**Research question**: How can robot manipulation benchmarks properly isolate and evaluate failures on long-horizon tasks when existing benchmarks have horizons that are too short or entangled with scene/object variations?
**Methodology**: Introduces LADDER benchmark scaling from 1 to 10 subgoals across three suites (SimplerEnv-Long, RobotArena-∞-Long, RoboLab-Long), 145 tasks, eight categories, two embodiments, evaluating text subgoals and tool selection orchestration paradigms.
**Key findings**:
- Low-level policies achieve 85.4% on single-subgoal tasks but collapse to near zero on extended tasks
- Orchestration remedies collapse but achieves only ~25% due to low-level execution errors
- LLM-based tool selection (GPT-Policy on GPT-6 Astra) achieves ~62% but incurs significant time/cost
- Physical execution errors of low-level policies, not high-level planning, are the primary bottleneck
- Real-world experiments confirm low-level policy collapse and orchestration gains
**Limitations**: LLM orchestration incurs significant time and cost budget; reveals fundamental limitations in current low-level policy robustness rather than solving them.

### Xu & Nie (2025)

**Research question**: How can robot manipulation achieve lifelong adaptability to evolving objects, scenes, and tasks in dynamic unstructured environments while overcoming limitations of static training paradigms and rigid skill definitions?
**Methodology**: Proposes SPECI, hierarchical continual imitation learning with multimodal perception/fusion, high-level skill inference via expandable skill codebook with attention-driven selection, and low-level action execution, augmented with mode approximation for task-specific and task-sharing parameters.
**Key findings**:
- Consistently outperforms state-of-the-art CIL methods across all evaluated metrics
- Demonstrates exceptional bidirectional knowledge transfer on skill and task levels
- Expandable skill codebook enables efficient continual implicit skill acquisition and reuse
- Mode approximation enhances task-level knowledge transfer
- Superior performance compared to methods using manually defined rigid skills
**Limitations**: Abstract does not explicitly acknowledge limitations; potential concerns include computational complexity of hierarchical architecture and generalizability to vastly different robot embodiments or task domains.

### Yin et al. (2025)

**Research question**: How can fine-grained robot manipulation with part-level instructions be evaluated when large-scale datasets with part-level annotations and diverse 3D object instances are lacking?
**Methodology**: Introduces PartInstruct benchmark with 513 part-annotated object instances across 14 categories, 1,302 fine-grained tasks in 16 classes, and 10,000+ expert demonstrations in 3D simulator with part-based skill chains and ground-truth 3D part information.
**Key findings**:
- First large-scale benchmark for part-level instruction following in robot manipulation
- Comprehensive test suite evaluates generalizability across states, objects, and tasks
- Current models struggle to robustly ground part concepts
- Models face challenges predicting actions in 3D space
- Long-horizon part manipulation tasks remain difficult for existing approaches
**Limitations**: Simulator-generated demonstrations may not capture real-world execution variability; part-level annotations limited to 14 object categories, may not generalize to novel object types.

### Zhang et al. (2026) [Cross-Embodiment]

**Research question**: What knowledge in human manipulation videos should be transferred across embodiments to robot manipulation, given morphology, action space, and control mechanism differences that make human motions unsuitable as direct supervision?
**Methodology**: Proposes Causal-Beam-Guided Subtask Transfer (CBST) that learns manipulation representations from human videos and grounds them in task-level semantic variables using robot demonstrations, with causal-beam constraints guiding contextual information selection.
**Key findings**:
- Improvements in task success over world-action model baselines on robot manipulation benchmarks
- Enables robot action generation from own observations without human-robot motion correspondence
- Causal-beam constraints successfully identify contextual information for local task effects
- Selected semantic information effectively conditions world-action model for cross-embodiment transfer
- Demonstrates human video knowledge transfer despite morphology and action space differences
**Limitations**: Requires predefined manipulation models and robot demonstrations for grounding; scalability to highly diverse task categories unclear; performance when human and robot capabilities differ substantially not addressed.

### Zhang et al. (2026) [IronMan]

**Research question**: How can video-action models overcome the mismatch between video representations and action generation when excessive visual detail impairs generalization?
**Methodology**: Introduces IronMan framework built on information bottleneck principle with dynamics-aware bottleneck that distills noisy video features into compact world representations, suppressing irrelevant visual information while preserving action-relevant dynamics.
**Key findings**:
- Achieves 99.0% success on LIBERO and 79.4% on RoboTwin clean2clean
- Out-of-distribution success rate of 79.1% on LIBERO-Plus, exceeding strongest baseline by 10.4 percentage points
- Strong in-distribution performance and OOD robustness with efficient inference
- Information constraints effectively suppress irrelevant visual detail while preserving dynamics cues
**Limitations**: Information bottleneck design requires careful tuning of what constitutes "relevant" dynamics; may discard visual information that becomes relevant under distribution shift.

### Dong et al. (2025)

**Research question**: How can unified 3D multi-modal representations overcome domain gaps between training datasets and robot manipulation tasks while effectively incorporating 3D information?
**Methodology**: Proposes EmbodiedMAE, a multi-modal masked autoencoder learning representations across RGB, depth, and point cloud through stochastic masking and cross-modal fusion, trained on enhanced DROID-3D dataset with high-quality depth and point clouds.
**Key findings**:
- Outperforms state-of-the-art vision foundation models across 70 simulation and 20 real-world tasks
- Strong scaling behavior with model size
- Promotes effective policy learning from 3D inputs
- Particularly effective in precise tabletop manipulation requiring spatial perception
- Establishes reliable unified 3D multi-modal VFM for embodied AI systems
**Limitations**: Metadata truncated in source material; full methodological details and limitations require complete paper access. Performance on highly dynamic or deformable object manipulation not reported.

## References

Dong, Z., Ni, F., Yuan, Y., & Li, Y. (2025). EmbodiedMAE: A unified 3D multi-modal representation for robot manipulation. arXiv. https://arxiv.org/abs/2505.10105

Droß, L. J., Orthey, A., & Toussaint, M. (2026). PhyRoGen: Synthetic generation of physical robot manipulation puzzles using procedural content generation. arXiv. https://arxiv.org/abs/2606.06569

Gao, J., Belkhale, S., Dasari, S., Balakrishna, A., Shah, D., & Sadigh, D. (2025). A taxonomy for evaluating generalist robot manipulation policies. arXiv. https://arxiv.org/abs/2503.01238

Kim, S., Choi, J., Baek, S., & Renders, J.-M. (2026). ProgVLA: Progress-aware robot manipulation skill learning. arXiv. https://arxiv.org/abs/2605.28231

Liang, X., Liu, J., Sun, M., He, Q., Lu, C., & Sun, J. (2025). RealD²iff: Bridging real-world gap in robot manipulation via depth diffusion. arXiv. https://arxiv.org/abs/2511.22505

Petkov, P., Albanese, G., Nikolov, N., Van Gool, L., Tremblay, J., & Paudel, D. P. (2026). LADDER: A long-horizon robot manipulation benchmark. arXiv. https://arxiv.org/abs/2610.18053

Xu, J., & Nie, X. (2025). SPECI: Skill prompts based hierarchical continual imitation learning for robot manipulation. arXiv. https://arxiv.org/abs/2504.15561

Yin, Y., Han, Z., Aarya, S., Wang, J., Xu, S., Peng, J., Wang, A., Yuille, A., & Shu, T. (2025). PartInstruct: Part-level instruction following for fine-grained robot manipulation. arXiv. https://arxiv.org/abs/2505.21652

Zhang, X., Li, Y., Guo, P., Hu, J., Zheng, C., & Qiang, W. (2026). Cross-embodiment causal transfer from human videos to robot manipulation. arXiv. https://arxiv.org/abs/2610.21798

Zhang, Y., Zhao, W., Lei, Z., Chen, B., & Chen, S. (2026). IronMan: Information-constrained video-action learning for robot manipulation. arXiv. https://arxiv.org/abs/2610.07961
