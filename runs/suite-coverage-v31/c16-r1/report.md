# Systematic Literature Review: World Action Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "world action models", filtered to category cs.RO, published between 2024-06-18 and 2026-06-18
**Citation format**: APA 7th edition

## Executive Summary

World Action Models (WAMs) represent an emerging paradigm in robotic policy learning that combines predictive world modeling with action generation. The surveyed literature from 2024-2026 reveals a rapidly maturing field focused on improving the efficiency, robustness, and safety of WAMs for embodied AI tasks. Key trends include moving away from explicit future video generation toward more efficient latent representations, incorporating adaptive reasoning mechanisms, and addressing safety vulnerabilities. The field demonstrates strong convergence around hierarchical temporal abstraction, structured world representations with geometric and semantic supervision, and adaptive execution strategies that verify imagined futures against reality. However, significant gaps remain in understanding long-horizon task failures, safety guarantees under adversarial conditions, and the fundamental trade-offs between representational richness and computational efficiency.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "world action models", filtered to category cs.RO, published between 2024-06-18 and 2026-06-18. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficient Future Prediction Without Explicit Video Generation

A dominant trend across recent WAM research is the shift away from generating explicit future video frames toward more efficient latent representations that preserve only the information necessary for action selection. This theme reflects a growing recognition that full video generation is computationally expensive and often unnecessary for control tasks.

Fang et al. (2026) demonstrate that future video is never needed at inference time through their Privileged Foresight Distillation approach, which transfers future-conditioned corrections from a teacher model to a current-only student. Similarly, Ma et al. (2026) avoid explicit future rollout at test time while still capturing scene dynamics through structured latent representations. Sun et al. (2026) take this further with HiMem-WAM, enabling causal inference without test-time generation of future video or optical flow estimation.

The survey by Shen et al. (2026) identifies this as a consistent design pattern across the field: "WAMs are not simply video generators with action heads, but predictive-action methods with design choices trading representational richness against compute, memory, latency, and action-label cost." The field is moving toward methods that "generate less of the future while preserving what control requires."

### Theme 2: Structured World Representations with Geometric and Semantic Supervision

Multiple papers emphasize the importance of structured world representations that go beyond RGB-based future prediction to capture geometric, semantic, and motion dynamics explicitly.

Ma et al. (2026) introduce GeoSem-WAM, which adds auxiliary prediction branches for future geometry and semantic representations alongside RGB prediction, enabling joint capture of scene dynamics, spatial geometry, and semantic context. Their results show that RGB-based future prediction alone provides "limited structural and spatial understanding of complex environments."

Guan et al. (2026) propose JOPAT, which leverages 2D point tracks as an explicit motion representation that captures long-horizon dynamics and remains robust under occlusion or partial out-of-frame motion. Point tracks provide "greater utility than modeling pixel appearance alone for capturing motion dynamics," with the largest gains on long-horizon tasks involving occlusion and off-screen motion.

Sun et al. (2026) integrate motion-centric latent actions and high-level skill latents in HiMem-WAM, using hierarchical latent action frameworks for structured temporal abstraction. This structured approach improves robustness under deployment perturbations.

### Theme 3: Adaptive Execution and Verification Mechanisms

A third major theme involves adaptive mechanisms that dynamically adjust WAM behavior based on execution context, verifying whether imagined futures remain consistent with reality and triggering replanning when necessary.

Wang et al. (2026) formulate adaptive WAM execution as future-reality verification, proposing FFDC, a lightweight verifier that reasons over predicted actions, predicted visual dynamics, real observations, and instruction-conditioned semantics. Their method reduces planning calls by 69-74% while improving success rates, demonstrating that adaptive execution can substantially improve both efficiency and performance.

Tang et al. (2026) introduce AdaWAM with a lightweight dynamic router that autonomously triggers textual or visual reasoning as needed during task execution. Textual reasoning guides high-level action prediction during task transitions, while visual reasoning supports precise control during fine-grained manipulation, substantially improving inference efficiency.

Sun et al. (2026) address adaptive video denoising depth with SANTS, a scheduler that reads the current video-state representation and noise level to predict an optimal stopping point. This adaptive selection "preserves control benefits while removing much redundant inference cost," reducing latency by 80% while maintaining or improving success rates.

### Theme 4: Safety and Security Vulnerabilities in WAMs

An important emerging theme is the recognition of safety vulnerabilities in WAMs, particularly susceptibility to adversarial attacks that could induce unsafe physical behaviors.

Liu et al. (2026) present JailWAM, the first jailbreak evaluation framework for WAMs, achieving an 84.2% attack success rate on LingBot-VA in simulation. Their work demonstrates that "WAMs may be susceptible to jailbreak attacks that induce unsafe physical behaviors," highlighting the need for systematic safety evaluation frameworks.

The JailWAM framework introduces Visual-Trajectory Mapping for consistent risk assessment across architectures and a Risk Discriminator supervised by three safety levels. This work represents an important first step in understanding and mitigating safety risks in WAM deployments.

### Theme 5: Memory and Long-Horizon Task Handling

Several papers address the challenge of handling long-horizon tasks that require maintaining task-relevant memory over extended execution periods.

Sun et al. (2026) introduce a boundary-aware memory gate in HiMem-WAM that writes compact task states at predicted skill transitions, with the memory module "substantially benefiting memory-dependent long-horizon manipulation."

Guan et al. (2026) find that point tracks provide particular value on "long-horizon tasks involving occlusion, object interaction, and off-screen motion," suggesting that explicit motion representations help maintain continuity over extended task horizons.

Tang et al. (2026) show that different multimodal reasoning modes are required under different execution contexts, with their dynamic router autonomously triggering appropriate modes during long-horizon task execution.

### Theme 6: Diagnostic Tools for WAM Reliability

A final theme involves developing diagnostic tools and metrics for evaluating WAM reliability beyond simple success rates.

Ruan et al. (2026) investigate whether generated futures in WAMs are "dynamically compatible with the action sequences they claim to model, rather than merely visually plausible." They introduce action-state consistency as a diagnostic tool, finding that it "systematically separates successful and failed rollouts across many tasks" and "captures decision-relevant structure beyond visual realism."

Their work identifies "background collapse" as a boundary condition where low-dynamics failed trajectories can become deceptively consistent because static futures are easier to predict. They propose a value-free consensus strategy that improves success rates without additional training or reward modeling.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong convergence on several points. Most papers agree that explicit future video generation is unnecessary at inference time (Fang et al., 2026; Ma et al., 2026; Sun et al., 2026). There is consensus that structured representations incorporating geometric, semantic, or motion information improve performance over RGB-only approaches (Guan et al., 2026; Ma et al., 2026; Sun et al., 2026). Multiple papers converge on the value of adaptive mechanisms that adjust computation based on execution context (Tang et al., 2026; Wang et al., 2026; Sun et al., 2026). The field also agrees that WAMs require evaluation beyond visual plausibility to assess dynamic consistency and action-state alignment (Ruan et al., 2026).

**Disagreements**: The literature shows less disagreement on fundamental questions, reflecting a relatively young field still establishing core principles. However, there is implicit disagreement about the optimal level of abstraction for world representations: Guan et al. (2026) emphasize pixel-and-track joint modeling, while Ma et al. (2026) focus on geometry and semantics, and Sun et al. (2026) prioritize hierarchical latent actions. These differences may reflect task-specific requirements rather than fundamental disagreements. There is also variation in how papers handle memory: some use explicit memory gates (Sun et al., 2026), while others rely on implicit representations through point tracks (Guan et al., 2026) or multimodal reasoning (Tang et al., 2026).

## Gaps and Open Questions

The collective literature reveals several important gaps:

1. **Limited discussion of failure modes**: Most papers report success rates but provide limited analysis of systematic failure patterns. Ruan et al. (2026) identify "background collapse" as one failure mode, but comprehensive failure taxonomies are lacking.

2. **Safety guarantees remain preliminary**: While Liu et al. (2026) demonstrate vulnerability to jailbreak attacks, systematic approaches to building safety guarantees into WAM architectures are not yet developed.

3. **Computational efficiency trade-offs underexplored**: While multiple papers report latency reductions (Wang et al., 2026; Sun et al., 2026), systematic analysis of the trade-offs between representational richness, computational cost, and task performance is limited.

4. **Generalization across task domains**: Most evaluations focus on specific benchmarks (LIBERO, RoboTwin, RoboCasa), but cross-domain generalization capabilities are not thoroughly explored.

5. **Human-robot interaction considerations**: None of the surveyed papers explicitly address WAM deployment in settings requiring human-robot interaction, representing a significant gap for practical applications.

6. **Learning efficiency and data requirements**: The data efficiency of different WAM approaches and sample complexity for training are not systematically compared across methods.

## Per-Paper Annotations

### Fang et al. (2026)

**Research question**: What role does the future-prediction branch actually play in world action models, and can its benefits be transferred to current-only policies?

**Methodology**: The authors formulate privileged foresight as a residual in the action-denoising direction and introduce Privileged Foresight Distillation (PFD), which transfers this residual from a training-time teacher into a small adapter on a current-only student. The teacher and student share the same backbone and differ only in the attention mask over video tokens.

**Key findings**:
- PFD achieves consistent improvements on LIBERO and RoboTwin manipulation benchmarks
- The approach preserves the current-only inference interface at negligible added latency
- Future video is never generated at inference, yet the student captures the future-conditioned correction
- The gain reflects a genuine future-conditioned correction rather than a side effect of capacity or regularization

**Limitations**: Not stated in abstract

### Guan et al. (2026)

**Research question**: How can world-action models for robot policy learning better capture environment dynamics while remaining robust to task-irrelevant visual variations?

**Methodology**: The authors propose JOPAT, a joint pixel-and-track world-action model that predicts latent visual observations, 2D point tracks with visibility, and actions using a single denoising diffusion transformer. The approach leverages point tracks as an explicit motion representation that captures long-horizon dynamics and remains robust under occlusion or partial out-of-frame motion.

**Key findings**:
- JOPAT improves over pixel-based baselines on LIBERO and real-world LeRobot tasks
- Point tracks provide greater utility than modeling pixel appearance alone for capturing motion dynamics
- The largest performance gains occur on long-horizon tasks involving occlusion, object interaction, and off-screen motion
- Tracks remain robust under occlusion or partial out-of-frame motion

**Limitations**: Not stated in abstract

### Liu et al. (2026)

**Research question**: What safety risks do World Action Models face from adversarially designed instructions, and how can these risks be systematically evaluated?

**Methodology**: The authors propose JailWAM, the first jailbreak evaluation framework for WAMs, featuring three innovations: Visual-Trajectory Mapping for consistent risk assessment across architectures, a Risk Discriminator supervised by three safety levels (Safety Compliance, Motion Failure, Catastrophic Risk), and a Dual-Path Verification Strategy combining rapid risk screening with closed-loop physical simulation.

**Key findings**:
- JailWAM achieves an 84.2% attack success rate on LingBot-VA in RoboTwin simulation environment
- WAMs may be susceptible to jailbreak attacks that induce unsafe physical behaviors
- Visual-Trajectory Mapping transforms model-specific actions into unified visual trajectory representations for consistent risk assessment
- The severity-aware Risk Discriminator can distinguish different physical outcomes from visual trajectories

**Limitations**: Not stated in abstract

### Ma et al. (2026)

**Research question**: Can structured world modeling with geometric and semantic supervision enhance latent representations in world action models beyond RGB-based future prediction?

**Methodology**: The authors propose a structured world modeling framework that introduces two auxiliary prediction branches for future geometry and semantic representations alongside future RGB prediction, enabling joint capture of scene dynamics, spatial geometry, and semantic context within a unified latent space while avoiding explicit future rollout at test time.

**Key findings**:
- Incorporating structured world supervision consistently improves action prediction accuracy
- The approach enhances scene understanding and robustness under challenging embodied scenarios
- RGB-based future prediction provides limited structural and spatial understanding of complex environments
- The approach preserves efficient inference by avoiding explicit future rollout or video generation at test time

**Limitations**: Not stated in abstract

### Ruan et al. (2026)

**Research question**: This work investigates whether generated futures in World Action Models are dynamically compatible with the action sequences they claim to model, rather than merely visually plausible.

**Methodology**: The authors conduct a systematic study across representative joint-prediction and inverse-dynamics models to analyze action-state consistency—the alignment between predicted actions and induced state transitions. They introduce a value-free consensus strategy for test-time selection that ranks candidate rollouts by agreement among predicted futures.

**Key findings**:
- Action-state consistency systematically separates successful and failed rollouts across many tasks
- Action-state consistency follows similar success-failure trends as learned value estimates, suggesting it captures decision-relevant structure beyond visual realism
- Background collapse is identified as a boundary condition where low-dynamics failed trajectories can become deceptively consistent because static futures are easier to predict
- The value-free consensus strategy improves success rates on RoboCasa and RoboTwin 2.0 without additional training or reward modeling
- Action-state consistency serves as both a diagnostic tool for evaluating WAM reliability and a practical signal for value-free planning

**Limitations**: Not stated in abstract

### Shen et al. (2026)

**Research question**: How can the rapidly expanding field of World Action Models be organized and clarified to establish common understanding and design patterns?

**Methodology**: The survey clarifies boundaries among world models, video generation models, action-grounded video world models, Vision-Language-Action policies, and WAMs, then organizes existing works through two complementary views: what each method generates (rendered futures, latent futures, video-generation-free action reasoning) and decomposition by predictive substrate, backbone, action coupling, and deployment regime.

**Key findings**:
- WAMs are not simply video generators with action heads, but predictive-action methods with design choices trading representational richness against compute, memory, latency, and action-label cost
- The field is moving toward methods that generate less of the future while preserving what control requires
- Recent WAMs repurpose large video generation models while a parallel line relies on language or vision-language backbones without video-generation core
- A consistent design pattern emerges across interactability, causality, persistence, physical plausibility, and generalization axes

**Limitations**: Not stated in abstract

### Sun et al. (2026) [HiMem-WAM]

**Research question**: How can World Action Models better handle task-relevant memory in long-horizon robotic manipulation tasks?

**Methodology**: The authors present HiMem-WAM, a Hierarchical Memory-Gated WAM that integrates motion-centric latent actions, high-level skill latents, and boundary-triggered memory updates. The approach uses a hierarchical latent action framework for structured temporal abstraction and a boundary-aware memory gate that writes compact task states at predicted skill transitions.

**Key findings**:
- HiMem-WAM enables causal inference without requiring test-time generation of future video or optical flow estimation
- Hierarchical latents improve robustness under deployment perturbations
- The memory module substantially benefits memory-dependent long-horizon manipulation
- The method was evaluated on LIBERO, LIBERO-PLUS, RMBench, and real-world tasks

**Limitations**: Not stated in abstract

### Sun et al. (2026) [SANTS]

**Research question**: What is the optimal video denoising depth for action generation in pixel-space World Action Models, and should it be fixed or state-dependent?

**Methodology**: The authors introduce State-Adaptive Noise Trajectory Scheduler (SANTS), a lightweight scheduler for video-to-action diffusion policies that reads the current video-state representation and noise level, then jointly predicts a cumulative stopping hazard and a relative noise-progression ratio. SANTS is post-trained with a path-level reward optimized for downstream action quality rather than intermediate video fidelity.

**Key findings**:
- SANTS reaches 94.4% overall success on RoboTwin 2.0
- SANTS achieves 73.1% average success across seven real-robot tasks
- The method reduces latency by 81.7% on simulation and 79.0% on real-robot tasks relative to full video denoising
- Adaptive selection along the video noise trajectory preserves control benefits while removing much redundant inference cost
- Video refinement can reduce action error up to a state-dependent point, after which gains saturate or reverse

**Limitations**: Not stated in abstract

### Tang et al. (2026)

**Research question**: How can world action models incorporate adaptive multimodal reasoning to improve effectiveness on long-horizon, complex tasks?

**Methodology**: The authors propose AdaWAM, a world action model with adaptive multimodal reasoning that integrates a lightweight dynamic router to autonomously trigger textual or visual reasoning as needed during task execution. Textual reasoning guides high-level action prediction during task transitions, while visual reasoning supports precise control during fine-grained manipulation.

**Key findings**:
- AdaWAM substantially improves inference efficiency on simulated and real-world embodied tasks
- AdaWAM outperforms state-of-the-art embodied policies
- Different multimodal reasoning modes are required under different execution contexts
- The dynamic router autonomously triggers appropriate reasoning modes during task execution

**Limitations**: Not stated in abstract

### Wang et al. (2026)

**Research question**: When should World Action Models continue executing planned actions versus triggering replanning based on whether imagined futures remain consistent with reality?

**Methodology**: The authors formulate adaptive WAM execution as future-reality verification and propose Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that reasons over predicted actions, predicted visual dynamics, real observations, and instruction-conditioned semantics. They combine verification with Mixture-of-Horizon Training to improve long-horizon trajectory coverage.

**Key findings**:
- FFDC-WAM achieves the highest average success rate among evaluated methods on RoboTwin in both clean and randomized settings
- Under randomization, FFDC-WAM improves success by 2.54 percentage points over Base-Motus while reducing WAM planning calls by 69.10% and completion time by 33.88%
- On six real-robot tasks on a Unitree G1D robot, FFDC-WAM improves average success by 9.17% over Base-Motus-LC16
- The method reduces planning calls by 74.06% and completion time by 51.31% on real-robot tasks

**Limitations**: Not stated in abstract

## References

Fang, P., Chen, H., & Cai, X. (2026). Privileged foresight distillation: Zero-cost future correction for world action models. arXiv. https://arxiv.org/abs/2604.25859

Guan, J., Zhao, W., Pei, Y., Chen, Z., Solin, A., & Kannala, J. (2026). Point tracking improves world action models. arXiv. https://arxiv.org/abs/2605.23856

Liu, H., Wang, S., Long, J., Hou, J., Sun, J., Li, C., Yang, Y., Peng, W., Liu, X., Jiang, T., Mu, Y., & Yao, W. (2026). JailWAM: Jailbreaking world action models in robot control. arXiv. https://arxiv.org/abs/2604.05498

Ma, F., Peng, D., Yue, W., Cao, J., Wang, B., Zhang, Q., & Ma, J. (2026). GeoSem-WAM: Geometry- and semantic-aware world action models. arXiv. https://arxiv.org/abs/2606.03188

Ruan, B.-K., Hsiao, T.-F., Lo, L., & Shuai, H.-H. (2026). Is the future compatible? Diagnosing dynamic consistency in world action models. arXiv. https://arxiv.org/abs/2605.07514

Shen, Q., Zhang, S., Liao, Y., Li, Q., Tan, Z., Wang, S., Yan, S., & Wang, X. (2026). World action models: A survey. arXiv. https://arxiv.org/abs/2606.20781

Sun, X., Zhang, R., Cao, C., Sun, Y., Chen, J., Xu, Z., Chen, B., Chen, H., Yang, Z., Zhu, J., Hong, Y., Xu, J., Pang, J., Yuan, M., & Chen, J. (2026). HiMem-WAM: Hierarchical memory-gated world action models for robotic manipulation. arXiv. https://arxiv.org/abs/2606.10363

Sun, Y., Zhuge, G., Liu, K., Gu, J., Dai, S., Bing, X., Gan, Z., & Tian, C. (2026). SANTS: A state-adaptive scheduler for world action models. arXiv. https://arxiv.org/abs/2605.27947

Tang, Y., Xu, J., Shang, Y., Song, Z., Gao, C., Wu, W., & Li, Y. (2026). Dreaming when necessary: Advancing world action models with adaptive multi-modal reasoning. arXiv. https://arxiv.org/abs/2606.07089

Wang, R., Zhang, Y., Chen, C., Lin, J., Wang, Z., & Qi, X. (2026). When to trust imagination: Adaptive action execution for world action models. arXiv. https://arxiv.org/abs/2605.06222
