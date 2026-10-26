# Systematic Literature Review: World Action Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "world action models", category cs.RO, published between 2024-06-18 and 2026-06-17
**Citation format**: APA 7th edition

## Executive Summary

World Action Models (WAMs) represent an emerging paradigm in robotic manipulation that combines future prediction, action generation, and latent world modeling within unified frameworks. The ten papers surveyed here, all published between April and June 2026, reveal a rapidly maturing field focused on improving WAM capabilities across multiple dimensions: enhanced latent representations through geometric and semantic supervision, adaptive multimodal reasoning, hierarchical memory mechanisms, and parameter-efficient knowledge transfer. A strong consensus emerges that the primary value of WAMs lies not in generating photorealistic future observations, but in learning robust latent representations that support effective action prediction. Recent advances address critical limitations including long-horizon task execution, dynamic consistency verification, adaptive execution strategies, and safety vulnerabilities. However, significant gaps remain in systematic safety evaluation, real-world deployment validation, and understanding the fundamental trade-offs between prediction fidelity and control effectiveness.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "world action models", filtered to category cs.RO, published between 2024-06-18 and 2026-06-17. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The narrow 2-year window captures recent advances but may miss foundational earlier work on world models and action prediction.

## Themes

### Theme 1: Enhanced Latent Representations through Structured Supervision

A central challenge in WAMs is learning latent representations that capture task-relevant structure beyond pixel-level prediction. Three papers address this through complementary approaches. GeoSem-WAM introduces geometric and semantic supervision alongside RGB prediction, demonstrating that structured world modeling significantly improves action prediction accuracy while preserving efficient inference (Ma et al., 2026). Similarly, JOPAT leverages point tracks as explicit motion representations, capturing long-horizon dynamics more robustly than pixel-based approaches alone, particularly under occlusion and off-screen motion (Guan et al., 2026). HiMem-WAM extends this line by introducing hierarchical latent actions that jointly learn low-level motion and high-level skill latents, enabling structured temporal abstraction for long-horizon manipulation (Sun et al., 2026). These approaches share a fundamental insight: WAMs benefit from multi-faceted supervision that captures geometry, semantics, and motion structure rather than relying solely on visual prediction.

### Theme 2: Adaptive and Conditional Computation

Multiple papers recognize that uniform computation across all execution contexts is inefficient and propose adaptive mechanisms that condition computation on task demands. AdaWAM introduces a dynamic router that autonomously triggers textual reasoning during task transitions and visual reasoning during fine-grained manipulation, substantially improving inference efficiency while maintaining performance (Tang et al., 2026). FFDC-WAM addresses a different adaptive question: when to trust imagined actions versus when to replan based on future-reality consistency, achieving significant reductions in planning calls and completion time through selective verification (Wang et al., 2026). SANTS takes an adaptive approach to denoising depth, reading current video-state representation to predict optimal stopping points along the noise trajectory, reducing latency by approximately 80% while preserving control quality (Sun et al., 2026). Together, these works establish that adaptive computation is essential for practical WAM deployment.

### Theme 3: Knowledge Transfer and Parameter Efficiency

As WAMs grow in complexity, transferring knowledge between models efficiently becomes critical. CKT-WAM addresses this through a parameter-efficient context knowledge transfer framework that extracts intermediate teacher hidden states, compresses them via learnable-query cross attention, and transforms them through specialized adapters (Jiang et al., 2026). With only 1.17% trainable parameters, CKT-WAM achieves 86.1% success on LIBERO-Plus, approaching full fine-tuning performance. This work demonstrates that heterogeneous WAMs can share knowledge despite mismatched latent interfaces, enabling efficient adaptation without architectural modification. The approach complements Privileged Foresight Distillation, which transfers future-prediction benefits from a teacher to a current-only student through a small adapter, preserving the current-only inference interface with negligible latency (Fang et al., 2026).

### Theme 4: Verification, Consistency, and Dynamic Assessment

Ensuring WAM rollouts produce reliable actions requires mechanisms to assess dynamic consistency beyond visual plausibility. Ruan et al. (2026) systematically analyze action-state consistency as a reliability metric, finding it systematically separates successful and failed rollouts across tasks and captures decision-relevant structure beyond visual realism. Their value-free consensus strategy ranks candidate rollouts by agreement among predicted futures, improving success rates without additional training. This work identifies background collapse as a boundary condition where low-dynamics failed trajectories become deceptively consistent, establishing important limits for consistency-based verification. FFDC-WAM complements this with a lightweight verifier evaluating predicted actions against real observations and instruction-conditioned semantics (Wang et al., 2026).

### Theme 5: Safety and Security Vulnerabilities

The deployment of WAMs in physical robot control introduces safety and security concerns that require systematic evaluation. JailWAM presents the first jailbreak evaluation framework for WAMs, achieving 84.2% attack success rate on LingBot-VA in simulation (Liu et al., 2026). The framework features Visual-Trajectory Mapping to transform heterogeneous actions into unified visual representations, a severity-aware Risk Discriminator distinguishing safety compliance from catastrophic risk, and Dual-Path Verification reducing computational cost. This work reveals that WAMs are susceptible to adversarially designed instructions that can induce unsafe physical behaviors, establishing an important baseline for future safety research.

## Convergences and Disagreements

**Convergences**: Strong consensus emerges across the surveyed literature that WAMs' primary value lies in learning robust latent representations rather than generating photorealistic future observations. Multiple papers independently conclude that structured supervision (geometric, semantic, motion-based) consistently improves action prediction accuracy (Ma et al., 2026; Guan et al., 2026; Sun et al., 2026). All adaptive computation papers agree that context-dependent computation selection preserves control benefits while removing redundant inference cost (Tang et al., 2026; Wang et al., 2026; Sun et al., 2026). There is broad agreement that long-horizon tasks require hierarchical or memory-based mechanisms to maintain task-relevant information across extended sequences (Sun et al., 2026; Jiang et al., 2026).

**Disagreements**: The literature shows limited direct disagreement, reflecting the field's early stage and complementary rather than competing approaches. However, implicit tensions exist between approaches emphasizing explicit structure (geometry, semantics, tracks) versus those relying on learned latent representations. GeoSem-WAM argues for explicit geometric and semantic supervision (Ma et al., 2026), while other work suggests sufficiently powerful latent models can learn structure implicitly. The appropriate balance between prediction fidelity and control effectiveness remains unresolved, with some work prioritizing accurate future prediction and others treating prediction primarily as a representation learning auxiliary.

## Gaps and Open Questions

Several significant gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either space constraints or insufficient critical reflection on methodological boundaries. Second, while JailWAM establishes safety vulnerabilities exist (Liu et al., 2026), no paper proposes comprehensive safety mechanisms or certification frameworks for WAM deployment. Third, real-world evaluation remains limited: most papers report simulation results with brief real-world demonstrations, leaving questions about robustness under real-world variation, sensor noise, and unstructured environments. Fourth, the relationship between prediction fidelity and control effectiveness remains underexplored theoretically—while multiple papers suggest prediction serves representation learning, the precise mechanisms and trade-offs lack formal analysis. Fifth, computational efficiency receives attention (SANTS, AdaWAM, FFDC), but energy efficiency and environmental impact of WAM training and deployment are not addressed. Finally, human-robot interaction aspects, including how WAMs should represent and predict human behavior in shared spaces, remain largely unaddressed.

## Per-Paper Annotations

### Fang et al. (2026)

**Research question**: What role does the future-prediction branch play in world action models, and can its benefits be transferred to current-only policies?
**Methodology**: The authors formulate privileged foresight as a residual in the action-denoising direction and introduce Privileged Foresight Distillation (PFD), which transfers this residual from a training-time teacher into a small adapter on a current-only student. The teacher and student share the same backbone and differ only in the attention mask over video tokens, with no future video generation at inference.
**Key findings**:
- Future-prediction branches in world action models induce an action-conditioned correction that current-only policies capture only partially.
- PFD successfully distills the privileged foresight residual into a small adapter without requiring future video generation at inference.
- PFD achieves consistent improvements on LIBERO and RoboTwin manipulation benchmarks.
- The method preserves the current-only inference interface with negligible added latency.
- Performance gains reflect genuine future-conditioned correction rather than capacity or regularization effects.
**Limitations**: Not stated in abstract.

### Guan et al. (2026)

**Research question**: How can world-action models for robot policy learning better capture environment dynamics while remaining robust to task-irrelevant visual variation?
**Methodology**: The authors propose JOPAT, a joint pixel-and-track world-action model that predicts latent visual observations, 2D point tracks with visibility, and actions using a single denoising diffusion transformer. The approach leverages point tracks as an explicit motion representation to capture long-horizon dynamics robustly under occlusion or partial out-of-frame motion.
**Key findings**:
- Point tracks provide an explicit representation of motion that captures long-horizon dynamics more effectively than pixel-level prediction alone.
- Track-based representations remain robust under occlusion and partial out-of-frame motion, unlike pixel-based approaches.
- JOPAT improves performance over pixel-based baselines on LIBERO and real-world LeRobot tasks.
- The largest performance gains occur on long-horizon tasks involving occlusion, object interaction, and off-screen motion.
**Limitations**: Not stated in abstract.

### Jiang et al. (2026)

**Research question**: How can knowledge be efficiently transferred across heterogeneous world action models (WAMs) despite mismatched latent interfaces and high adaptation costs?
**Methodology**: The authors propose CKT-WAM, a parameter-efficient context knowledge transfer framework that extracts intermediate teacher hidden states, compresses them via learnable-query cross attention, and transforms them through a generalized adapter, lightweight router, and sparsely activated specialized adapters. The resulting context is appended to the student's textual embeddings for knowledge injection with minimal architectural modification.
**Key findings**:
- CKT-WAM achieves 86.1% total success rate on LIBERO-Plus with only 1.17% trainable parameters.
- The framework consistently improves zero-shot generalization compared to baseline methods.
- CKT-WAM approaches full fine-tuning performance while requiring significantly fewer trainable parameters.
- Real-world evaluation shows 83.3% average success rate across four multi-step and long-horizon manipulation tasks.
**Limitations**: Not stated in abstract.

### Liu et al. (2026)

**Research question**: What safety risks do World Action Models face from adversarially designed instructions, and how can these jailbreak attacks be systematically evaluated?
**Methodology**: The authors propose JailWAM, the first jailbreak evaluation framework for WAMs, featuring Visual-Trajectory Mapping to transform heterogeneous actions into unified visual representations, a Risk Discriminator with three severity levels (Safety Compliance, Motion Failure, Catastrophic Risk), and a Dual-Path Verification Strategy combining rapid screening with closed-loop physical simulation. Evaluation is conducted in RoboTwin simulation environment.
**Key findings**:
- JailWAM achieves an 84.2% attack success rate on LingBot-VA in RoboTwin simulation.
- Visual-Trajectory Mapping enables consistent risk assessment across different WAM architectures.
- The severity-aware Risk Discriminator can distinguish different physical safety outcomes from visual trajectories.
- Dual-Path Verification reduces computational cost by restricting expensive verification to high-risk candidates.
- WAMs are susceptible to jailbreak attacks that can induce unsafe physical robot behaviors.
**Limitations**: Not stated in abstract.

### Ma et al. (2026)

**Research question**: Can structured world modeling with geometric and semantic supervision improve the latent representations and effectiveness of world action models?
**Methodology**: The authors propose a structured world modeling framework that enhances latent representations through geometric and semantic supervision. The model introduces two auxiliary prediction branches for future geometry and semantic representations alongside RGB-based future prediction, enabling joint capture of scene dynamics, spatial geometry, and semantic context within a unified latent space without explicit future rollout at test time.
**Key findings**:
- RGB-based future prediction provides limited structural and spatial understanding of complex environments.
- Incorporating geometric and semantic supervision consistently improves action prediction accuracy.
- The structured approach enhances scene understanding and robustness under challenging embodied scenarios.
- The method preserves efficient inference by avoiding explicit future rollout or video generation at test time.
- The primary advantage of world action models lies in learning robust latent representations rather than generating future observations.
**Limitations**: Not stated in abstract.

### Ruan et al. (2026)

**Research question**: Is action-state consistency—the alignment between predicted actions and induced state transitions—a reliable indicator of World Action Model rollout success beyond visual plausibility?
**Methodology**: The authors conduct a systematic study across representative joint-prediction and inverse-dynamics models to analyze action-state consistency as a reliability metric. They identify background collapse as a boundary condition and propose a value-free consensus strategy for test-time selection that ranks candidate rollouts by agreement among predicted futures. Evaluation is performed on RoboCasa and RoboTwin 2.0 without additional training or reward modeling.
**Key findings**:
- Action-state consistency systematically separates successful and failed rollouts across many tasks.
- Consistency follows similar success-failure trends as learned value estimates.
- Consistency captures decision-relevant structure beyond visual realism.
- Background collapse is identified as a boundary condition where low-dynamics failed trajectories can become deceptively consistent.
- Value-free consensus strategy improves success rates on RoboCasa and RoboTwin 2.0 without additional training.
**Limitations**: Not stated in abstract.

### Sun et al. (2026)

**Research question**: How can world action models better handle task-relevant memory in long-horizon robotic manipulation tasks?
**Methodology**: The authors present HiMem-WAM, a hierarchical memory-gated world action model that integrates motion-centric latent actions, high-level skill latents, and boundary-triggered memory updates. The approach uses a hierarchical latent action framework for structured temporal abstraction and a boundary-aware memory gate that writes compact task states at predicted skill transitions for causal inference without test-time generation.
**Key findings**:
- Existing world action models struggle with task-relevant memory in long-horizon robotic manipulation.
- Hierarchical latent actions jointly learning low-level motion and high-level skill latents provide structured temporal abstraction.
- The boundary-aware memory gate enables causal inference without test-time generation of future video or optical flow estimation.
- Hierarchical latents improve robustness under deployment perturbations.
- The memory module substantially benefits memory-dependent long-horizon manipulation on LIBERO, LIBERO-PLUS, RMBench, and real-world tasks.
**Limitations**: Not stated in abstract.

### Sun et al. (2026)

**Research question**: Can adaptive selection of denoising depth along the video noise trajectory improve action generation quality while reducing inference latency in World Action Models?
**Methodology**: The authors introduce State-Adaptive Noise Trajectory Scheduler (SANTS), a lightweight scheduler that reads current video-state representation and noise level to predict a cumulative stopping hazard and relative noise-progression ratio. SANTS is post-trained with path-level reward computed after the frozen action branch generates the final action chunk, optimizing for downstream action quality rather than intermediate video fidelity. Evaluation is performed on RoboTwin 2.0 and seven real-robot tasks.
**Key findings**:
- SANTS reaches 94.4% overall success on RoboTwin 2.0.
- SANTS achieves 73.1% average success across seven real-robot tasks.
- Latency is reduced by 81.7% in simulation relative to full video denoising.
- Latency is reduced by 79.0% on real-robot tasks relative to full video denoising.
- Adaptive selection along the video noise trajectory preserves control benefits while removing redundant inference cost.
**Limitations**: Not stated in abstract.

### Tang et al. (2026)

**Research question**: How can world action models incorporate adaptive multimodal reasoning to improve effectiveness on long-horizon, complex embodied tasks?
**Methodology**: The authors propose AdaWAM, a world action model with adaptive multimodal reasoning that integrates a lightweight dynamic router to autonomously trigger textual or visual reasoning modes based on execution context. Textual reasoning is used during task transitions for high-level action prediction, while visual reasoning supports fine-grained manipulation for precise control.
**Key findings**:
- Different multimodal reasoning modes are required under different execution contexts in world action models.
- Textual reasoning is essential during task transitions to guide high-level action prediction.
- Visual reasoning is critical during fine-grained manipulation for precise control.
- AdaWAM substantially improves inference efficiency while outperforming state-of-the-art embodied policies.
- The approach works effectively on both simulated and real-world embodied tasks.
**Limitations**: Not stated in abstract.

### Wang et al. (2026)

**Research question**: How can World Action Models adaptively decide when to continue executing imagined actions versus when to replan based on future-reality consistency?
**Methodology**: The authors propose Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that evaluates predicted actions, visual dynamics, real observations, and instruction-conditioned semantics to determine execution validity. They combine this with Mixture-of-Horizon Training and evaluate on RoboTwin simulation and real-world Unitree G1D robot tasks.
**Key findings**:
- FFDC-WAM achieves the highest average success rate among evaluated methods in both clean and randomized RoboTwin settings.
- Under randomization, FFDC improves success by 2.54 percentage points over Base-Motus while reducing WAM planning calls by 69.10%.
- Completion time is reduced by 33.88% in simulation under randomization.
- On six real-world Unitree G1D robot tasks, FFDC-WAM improves average success by 9.17% over Base-Motus-LC16.
- Real-world deployment reduces planning calls by 74.06% and completion time by 51.31%.
**Limitations**: Not stated in abstract.

## References

Fang, P., Chen, H., & Cai, X. (2026). Privileged foresight distillation: Zero-cost future correction for world action models. arXiv. https://arxiv.org/abs/2604.25859

Guan, J., Zhao, W., Pei, Y., Chen, Z., Solin, A., & Kannala, J. (2026). Point tracking improves world action models. arXiv. https://arxiv.org/abs/2605.23856

Jiang, Y., Guo, Y., Yang, H., Lei, G., Chen, N., Zhang, Y., Yan, S., Lin, B., Gao, F., & Qi, B. (2026). CKT-WAM: Parameter-efficient context knowledge transfer between world action models. arXiv. https://arxiv.org/abs/2605.06247

Liu, H., Wang, S., Long, J., Hou, J., Sun, J., Li, C., Yang, Y., Peng, W., Liu, X., Jiang, T., Mu, Y., & Yao, W. (2026). JailWAM: Jailbreaking world action models in robot control. arXiv. https://arxiv.org/abs/2604.05498

Ma, F., Peng, D., Yue, W., Cao, J., Wang, B., Zhang, Q., & Ma, J. (2026). GeoSem-WAM: Geometry- and semantic-aware world action models. arXiv. https://arxiv.org/abs/2606.03188

Ruan, B.-K., Hsiao, T.-F., Lo, L., & Shuai, H.-H. (2026). Is the future compatible? Diagnosing dynamic consistency in world action models. arXiv. https://arxiv.org/abs/2605.07514

Sun, X., Zhang, R., Cao, C., Sun, Y., Chen, J., Xu, Z., Chen, B., Chen, H., Yang, Z., Zhu, J., Hong, Y., Xu, J., Pang, J., Yuan, M., & Chen, J. (2026). HiMem-WAM: Hierarchical memory-gated world action models for robotic manipulation. arXiv. https://arxiv.org/abs/2606.10363

Sun, Y., Zhuge, G., Liu, K., Gu, J., Dai, S., Bing, X., Gan, Z., & Tian, C. (2026). SANTS: A state-adaptive scheduler for world action models. arXiv. https://arxiv.org/abs/2605.27947

Tang, Y., Xu, J., Shang, Y., Song, Z., Gao, C., Wu, W., & Li, Y. (2026). Dreaming when necessary: Advancing world action models with adaptive multi-modal reasoning. arXiv. https://arxiv.org/abs/2606.07089

Wang, R., Zhang, Y., Chen, C., Lin, J., Wang, Z., & Qi, X. (2026). When to trust imagination: Adaptive action execution for world action models. arXiv. https://arxiv.org/abs/2605.06222
