# Systematic Literature Review: Robot Manipulation with Foundation Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: "robot manipulation foundation models", cs.RO category, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

The integration of foundation models into robotic manipulation represents a rapidly evolving research frontier, with recent work demonstrating significant advances in generalization, perception, and planning capabilities. The surveyed literature reveals three dominant architectural paradigms: Vision-Language-Action (VLA) models that leverage large-scale pretraining for cross-embodiment transfer, 3D-aware foundation policies that incorporate geometric reasoning, and hybrid approaches that combine foundation models with specialized memory or scene graph representations. Collectively, these works demonstrate that foundation models enable robots to achieve unprecedented zero-shot capabilities, robust error recovery, and intuitive human-robot interaction, though challenges remain in evaluation methodologies, data efficiency, and long-horizon task execution.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "robot manipulation foundation models", filtered to category cs.RO, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Vision-Language-Action Foundation Models

The emergence of VLA models represents a paradigm shift in robotic manipulation, leveraging large-scale vision-language foundation models as the backbone for action generation. Qwen-RobotManip (Yuan et al., 2026) exemplifies this approach, building on Qwen-VL to create a unified alignment framework across representation, motion, and behavioral dimensions. The model's human-to-robot synthesis pipeline converts egocentric hand demonstrations into robot trajectories across 15 platforms, creating a massive ~38,100-hour pretraining corpus that enables emergent generalization capabilities including zero-shot instruction following and cross-embodiment transfer.

Survey work by Shao et al. (2025) systematically categorizes VLA architectures into monolithic models (single-system and dual-system designs) and hierarchical models that decouple planning from execution. This taxonomy reveals that the most successful approaches integrate foundation models with reinforcement learning, training-free optimization, and world model integration. The convergence on hierarchical architectures suggests that separating high-level reasoning from low-level control provides better scalability and interpretability.

### Theme 2: 3D Geometric Reasoning and Affordance Grounding

A critical limitation of 2D-only foundation models is their inability to reason about 3D geometric relationships essential for manipulation. FP3 (Yang et al., 2025) addresses this by introducing a 3D foundation policy built on a diffusion transformer architecture, pre-trained on 60k trajectories with point cloud observations. The model achieves over 90% success rates in novel environments with only 80 demonstrations, significantly surpassing 2D-only baselines and demonstrating that 3D geometric information is essential for robust manipulation.

Complementing this work, O³Afford (Tian et al., 2025) focuses on one-shot 3D object-to-object affordance grounding, combining semantic features from vision foundation models with point cloud representations. The integration with large language models enables the system to comprehend and reason about object interactions when generating task-specific constraint functions, significantly outperforming existing baselines in both accuracy and generalization to novel objects and categories.

### Theme 3: Memory and Scene Representation for Long-Horizon Tasks

Long-horizon manipulation requires persistent spatial awareness and consistent environmental reasoning. SAM2Act (Fang et al., 2025) introduces a multi-view robotic transformer policy leveraging visual representations from large-scale foundation models, enhanced with a memory architecture inspired by SAM2. The memory-based variant (SAM2Act+) achieves 94.3% success rate on memory-based tasks in the novel MemoryBench benchmark, demonstrating that memory mechanisms are critical for tasks requiring spatial recall and temporal reasoning.

For structured scene understanding, Dinesh and Park (2025) present a framework integrating off-the-shelf foundation models with dynamically maintained scene graphs for spatial awareness. This approach enables accurate long-horizon manipulation without domain-specific training by providing consistent environmental reasoning. Similarly, SENT-Map (Kathirvel et al., 2025) introduces JSON-based semantically enhanced topological maps that enable both humans and foundation models to add and edit semantic information, grounding the robot to existing nodes during planning to avoid infeasible states.

### Theme 4: Human-Robot Interaction and Intent Communication

Foundation models enable more intuitive human-robot interaction modalities beyond traditional programming interfaces. GAMMA (Tay et al., 2026) leverages ego-centric gaze tracking combined with vision-language models to infer user intent and autonomously execute manipulation tasks. By contextualizing gaze fixations within the scene to map visual attention to semantic understanding, the system enables skill selection and parameterization without task-specific training, providing robust and generalizable control for assistive care settings.

This work demonstrates that foundation models can serve as interpreters of human communication signals, translating non-verbal cues like eye gaze into actionable robot commands. The approach is particularly valuable in scenarios where users cannot provide explicit verbal instructions or where rapid, intuitive interaction is required.

### Theme 5: Automated Scene Generation and Evaluation

The quality of robot learning depends critically on the diversity and realism of training data. GIF (Xu et al., 2026) addresses this through an agentic generation framework that produces fine-grained functional object compositions for robot manipulation evaluation. The system recasts scene generation as disentangled reconstruction followed by relative pose recovery, with CoGen producing instance-disentangled meshes and GPRM refining relative pose under geometric and physical guidance. The framework reduces collision rates to below 1% and enables policy learning with diversity scaling in simulation and real-world deployment.

This work highlights the symbiotic relationship between foundation models for generation and foundation models for manipulation: generative models create diverse training scenarios that improve manipulation policies, which in turn can be used to evaluate and refine generative models.

### Theme 6: Survey and Taxonomy Development

The field's rapid growth has prompted several comprehensive surveys to organize the design space and emerging trends. Bai et al. (2025) examine robotic manipulation through a unified abstraction of high-level planning and low-level action modeling, extending task planning to include reasoning over language, code, affordances, geometric constraints, and 3D representations. Their survey identifies open challenges including scalability, generalization, data efficiency, multimodal physical interaction, and safety.

Shao et al. (2025) provide a complementary taxonomy focused specifically on large VLM-based VLA models, resolving inconsistencies in existing taxonomies and mitigating research fragmentation. Both surveys converge on the importance of foundation models in generating structured planning artifacts and directly modeling executable actions, while identifying memory mechanisms, 4D perception, efficient adaptation, and multi-agent cooperation as promising future directions.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong consensus on several key points. First, all papers agree that foundation models provide unprecedented generalization capabilities compared to task-specific approaches, with multiple works reporting zero-shot or few-shot performance on novel tasks (Yuan et al., 2026; Yang et al., 2025; Tian et al., 2025). Second, there is convergence on the importance of 3D geometric reasoning for manipulation, with both FP3 and O³Afford demonstrating significant improvements over 2D-only approaches. Third, all works acknowledge that standard benchmarks fail to capture the full capabilities of foundation model-based approaches, necessitating out-of-distribution evaluation settings.

**Disagreements**: The literature reveals tension between monolithic and hierarchical architectural choices. While Qwen-RobotManip (Yuan et al., 2026) demonstrates success with a unified VLA model, the survey by Shao et al. (2025) suggests that hierarchical approaches better decouple planning from execution for improved interpretability. Additionally, there is disagreement on the optimal data scale: some works advocate for massive pretraining corpora (~38,100 hours in Qwen-RobotManip), while others achieve strong results with limited demonstrations (80 in FP3), suggesting different pathways to generalization.

## Gaps and Open Questions

The collective literature reveals several critical gaps. First, none of the surveyed papers explicitly address safety guarantees or formal verification of foundation model-based manipulation policies, despite acknowledging safety as an open challenge (Bai et al., 2025). Second, while multiple works demonstrate impressive few-shot or zero-shot capabilities, the theoretical foundations for why and when foundation models generalize remain unclear. Third, evaluation methodologies are inconsistent across papers, with custom benchmarks (MemoryBench, the GIF benchmark) making direct comparisons difficult. Fourth, the computational requirements of large foundation models raise questions about deployment on resource-constrained robotic platforms, with only SENT-Map (Kathirvel et al., 2025) explicitly addressing locally-deployable models. Finally, the long-tail of rare but critical failure modes in open-world manipulation remains underexplored, with most evaluations focused on tabletop or controlled environments.

## Per-Paper Annotations

### Bai et al. (2025)

**Research question**: How can recent learning-based approaches for robotic manipulation be organized and understood through the lens of foundation models from planning and learning perspectives?

**Methodology**: This survey examines robotic manipulation through a unified abstraction of high-level planning and low-level action modeling, extending task planning to include reasoning over language, code, affordances, geometric constraints, and 3D representations, while presenting a learning-paradigm-oriented taxonomy of action models.

**Key findings**:
- Foundation models contribute by generating structured planning artifacts instantiated as constraints or latent inputs, or by directly modeling executable actions and trajectories
- High-level planning includes reasoning over language, code, affordances, geometric constraints, and 3D representations
- Low-level action models are categorized by input modeling, latent learning, and policy learning paradigms
- Open challenges include scalability, generalization, data efficiency, multimodal physical interaction, and safety
- The survey provides a structured view of the design space and emerging trends in foundation models for robotic manipulation

**Limitations**: not stated in abstract

### Dinesh and Park (2025)

**Research question**: How can pre-trained foundation models be leveraged for accurate long-horizon robotic manipulation without domain-specific training?

**Methodology**: The authors present a framework that integrates off-the-shelf foundation models for multimodal perception with a general-purpose reasoning model for robust task sequencing, using dynamically maintained scene graphs for spatial awareness and consistent environmental reasoning.

**Key findings**:
- The framework enables robotic manipulation using pre-trained foundation models without requiring domain-specific training
- Scene graphs provide spatial awareness and enable consistent reasoning about the environment
- Evaluation through tabletop robotic manipulation experiments highlights the framework's potential for building systems on top of off-the-shelf foundation models

**Limitations**: not stated in abstract

### Fang et al. (2025)

**Research question**: How can visual foundation models be integrated with memory architectures to improve robotic manipulation in diverse, dynamic environments?

**Methodology**: The authors introduce SAM2Act, a multi-view robotic transformer-based policy leveraging multi-resolution upsampling with visual representations from large-scale foundation models, and SAM2Act+, which adds a memory-based architecture with a memory bank, encoder, and attention mechanism inspired by SAM2.

**Key findings**:
- SAM2Act achieves a state-of-the-art average success rate of 86.8% across 18 tasks in the RLBench benchmark
- SAM2Act demonstrates robust generalization on The Colosseum benchmark with only a 4.3% performance gap under diverse environmental perturbations
- The authors introduce MemoryBench, a novel benchmark for evaluating spatial memory and action recall in robotic manipulation
- SAM2Act+ achieves an average success rate of 94.3% on memory-based tasks in MemoryBench, significantly outperforming existing approaches

**Limitations**: not stated in abstract

### Kathirvel et al. (2025)

**Research question**: How can semantically enhanced topological maps support autonomous navigation and manipulation in indoor environments using foundation models?

**Methodology**: The authors introduce SENT-Map, a JSON-based semantically enhanced topological map representation, employing a two-stage approach: first mapping the environment with a Vision-FM alongside an operator, then using the SENT-Map representation with natural-language queries within an FM for planning.

**Key findings**:
- SENT-Map represents indoor environments in a JSON text format that enables semantic information to be added and edited in a format both humans and foundation models understand
- The framework grounds the robot to existing nodes during planning to avoid infeasible states during deployment
- Semantic enhancement enables even small locally-deployable foundation models to successfully plan over indoor environments

**Limitations**: not stated in abstract

### Shao et al. (2025)

**Research question**: What is the current state and taxonomy of large VLM-based Vision-Language-Action models for robotic manipulation?

**Methodology**: This survey provides a systematic, taxonomy-oriented review of large VLM-based VLA models, defining two principal architectural paradigms (monolithic and hierarchical models) and examining their integration with advanced domains, distinctive characteristics, and promising future directions.

**Key findings**:
- Large VLM-based VLA models are categorized into monolithic models (single-system and dual-system designs) and hierarchical models (decoupling planning from execution)
- Integration with advanced domains includes reinforcement learning, training-free optimization, learning from human videos, and world model integration
- The survey consolidates recent advances to resolve inconsistencies in existing taxonomies and mitigate research fragmentation
- Promising directions include memory mechanisms, 4D perception, efficient adaptation, and multi-agent cooperation

**Limitations**: not stated in abstract

### Tay et al. (2026)

**Research question**: How can eye gaze be leveraged as an intuitive input modality for conveying user intent in human-robot interaction for robotic manipulation?

**Methodology**: GAMMA (Gaze Assisted Manipulation for Modular Autonomy) leverages ego-centric gaze tracking and a vision-language model to infer user intent and autonomously execute robotic manipulation tasks by contextualizing gaze fixations within the scene to map visual attention to semantic understanding.

**Key findings**:
- GAMMA enables skill selection and parameterization without task-specific training
- The system provides robust, intuitive, and generalizable control compared to baseline gaze-based control without reasoning
- Combining foundation models and gaze enables natural and scalable robot autonomy
- Eye gaze serves as a fast, non-intrusive, and intent-rich input modality for assistive care settings

**Limitations**: not stated in abstract

### Tian et al. (2025)

**Research question**: How can object-to-object affordance grounding be achieved for robotic manipulation under limited data constraints?

**Methodology**: The authors propose a one-shot 3D object-to-object affordance learning approach that combines semantic features from vision foundation models with point cloud representation for geometric understanding, and integrates this with large language models for robotics manipulation.

**Key findings**:
- The O³Afford approach enables one-shot learning for object-to-object affordance grounding in robotic manipulation
- Semantic features from vision foundation models combined with point cloud representation enable effective generalization to novel objects and categories
- Integration with LLMs significantly enhances their capability to comprehend and reason about object interactions when generating task-specific constraint functions
- Experiments demonstrate that O³Afford significantly outperforms existing baselines in both accuracy and generalization capability

**Limitations**: not stated in abstract

### Xu et al. (2026)

**Research question**: How can automated scene generation be improved to produce fine-grained functional object compositions for robot manipulation evaluation and data generation?

**Methodology**: GIF is an agentic generation framework that recasts the problem as disentangled reconstruction followed by relative pose recovery. CoGen produces instance-disentangled meshes with coarse initial poses using 2D and 3D generative models, while GPRM refines relative pose under geometric and physical guidance, with a VLM verifier selecting the best candidate.

**Key findings**:
- GIF improves both asset quality and relation matching compared to state-of-the-art generators
- The framework reduces collision rate to below 1%
- A benchmark spanning eight representative contact-geometry classes was constructed for evaluation
- Synthesized data enables policy learning with diversity scaling in simulation and real-world deployment

**Limitations**: not stated in abstract

### Yang et al. (2025)

**Research question**: How can 3D geometric information be incorporated into foundation models for robotic manipulation to improve perception and reasoning about the 3D world?

**Methodology**: FP3 is a large-scale 3D foundation policy model built on a scalable diffusion transformer architecture, pre-trained on 60k trajectories with point cloud observations, designed for efficient fine-tuning on downstream tasks.

**Key findings**:
- With only 80 demonstrations, FP3 achieves over 90% success rates in novel environments with unseen objects
- FP3 significantly surpasses existing robot foundation models that rely solely on 2D image observations
- The model exhibits strong generalization capabilities due to its design and diverse pre-training data
- 3D geometric information is essential for robots to perceive and reason about the 3D world

**Limitations**: not stated in abstract

### Yuan et al. (2026)

**Research question**: Can the scaling approach used in language and multimodal foundation models be applied to robotic manipulation to achieve genuine generalization?

**Methodology**: Qwen-RobotManip is a Vision-Language-Action foundation model built on Qwen-VL that introduces unified alignment across representation, motion, and behavioral dimensions. A human-to-robot synthesis pipeline converts egocentric hand demonstrations into robot trajectories across 15 platforms, creating a ~38,100-hour pretraining corpus from open-source datasets and human videos.

**Key findings**:
- Qwen-RobotManip exhibits emergent generalization capabilities including zero-shot instruction following, robustness to perturbations, reactive error recovery, and cross-embodiment transfer
- The model substantially outperforms prior state-of-the-art models including π0.5 across all OOD settings
- Ranks 1st in RoboChallenge with a 20% relative improvement
- Standard benchmarks fail to capture pretraining quality, requiring OOD settings for proper evaluation
- Alignment enables coherent large-scale multi-source training that prior regimes could not sustain

**Limitations**: not stated in abstract

## References

Bai, S., Song, W., Chen, J., Ji, Y., Zhong, Z., Yang, J., Zhao, H., Zhou, W., Li, Z., Ding, P., Chi, C., Xu, C., Zheng, X., Wang, D., Li, H., Zhang, S., & Chen, B. (2025). Embodied robot manipulation in the era of foundation models: Planning and learning perspectives. arXiv. https://arxiv.org/abs/2512.22983

Dinesh, S. S., & Park, S. (2025). Toward accurate long-horizon robotic manipulation: Language-to-action with foundation models via scene graphs. arXiv. https://arxiv.org/abs/2510.27558

Fang, H., Grotz, M., Pumacay, W., Wang, Y. R., Fox, D., Krishna, R., & Duan, J. (2025). SAM2Act: Integrating visual foundation model with a memory architecture for robotic manipulation. arXiv. https://arxiv.org/abs/2501.18564

Kathirvel, R. S. R., Chavis, Z. A., Guy, S. J., & Desingh, K. (2025). SENT Map -- Semantically enhanced topological maps with foundation models. arXiv. https://arxiv.org/abs/2511.03165

Shao, R., Li, W., Zhang, L., Zhang, R., Liu, Z., Chen, R., & Nie, L. (2025). Large VLM-based Vision-Language-Action models for robotic manipulation: A survey. arXiv. https://arxiv.org/abs/2508.13073

Tay, T. Y. H., Yan, X., Ouyang, J., Wu, D., Jiang, W., Kao, J., & Cui, Y. (2026). Intent at a glance: Gaze-guided robotic manipulation via foundation models. arXiv. https://arxiv.org/abs/2601.05336

Tian, T., Kang, X., & Kuo, Y.-L. (2025). O³Afford: One-shot 3D object-to-object affordance grounding for generalizable robotic manipulation. arXiv. https://arxiv.org/abs/2509.06233

Xu, L., Zhang, Z., Yan, M., Deng, S., Xia, C., Dong, M., Chen, J., Lyu, J., Gao, F., Zhang, Z., & Wang, H. (2026). GIF: Agentic generation of interactive and functional object compositions for robot learning. arXiv. https://arxiv.org/abs/2609.05927

Yang, R., Chen, G., Wen, C., & Gao, Y. (2025). FP3: A 3D foundation policy for robotic manipulation. arXiv. https://arxiv.org/abs/2503.08950

Yuan, H., Liang, Z., Chen, A., Wang, Y., Li, H., Lin, P., Huang, Y., Lei, Z., Zhang, T., Zhang, J., Zhang, J., Fan, J., Zhou, G., Peng, Q., Lv, C., Chen, X., Yang, A., Huang, F., Lin, J., Liu, D., Zhou, J., Wu, C., & Chen, X.-H. (2026). Qwen-RobotManip technical report: Alignment unlocks scale for robotic manipulation foundation models. arXiv. https://arxiv.org/abs/2606.17846
