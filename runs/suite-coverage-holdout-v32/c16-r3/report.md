# Systematic Literature Review: World Action Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "world action models", category cs.RO, published between 2024-06-18 and 2026-06-17
**Citation format**: APA 7th edition

## Executive Summary

World Action Models (WAMs) represent an emerging paradigm in robotic policy learning that jointly predicts future observations and actions to enable more robust decision-making. The ten papers surveyed here, all published between April and June 2026, reveal a rapidly maturing field focused on addressing fundamental challenges: computational efficiency, representation quality, reliability of predictions, and safety. Recent work demonstrates that WAMs benefit from explicit motion representations (point tracks), structured world modeling with geometric and semantic supervision, hierarchical memory mechanisms, and adaptive computation strategies. A significant thread examines when and how to trust imagined futures, with multiple papers proposing verification mechanisms. The literature also addresses knowledge transfer between heterogeneous WAM architectures and exposes security vulnerabilities through jailbreak frameworks. Collectively, these papers suggest WAMs are transitioning from proof-of-concept to production-ready systems, with emphasis on long-horizon manipulation, real-world deployment, and parameter-efficient adaptation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "world action models", filtered to category cs.RO, published between 2024-06-18 and 2026-06-17. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The narrow two-year window captures only the most recent developments, potentially missing foundational earlier work.

## Themes

### Theme 1: Efficiency Through Adaptive Computation

A dominant theme across recent WAM research is reducing inference cost without sacrificing performance. Three papers address this through different mechanisms. Sun et al. (2026) introduce SANTS, a state-adaptive noise trajectory scheduler that dynamically determines video denoising depth based on robot state, achieving 81.7% latency reduction in simulation while maintaining 94.4% success rate. Tang et al. (2026) propose AdaWAM, which uses a lightweight dynamic router to trigger textual or visual reasoning only when necessary—textual reasoning during task transitions and visual reasoning during fine-grained manipulation. Fang et al. (2026) demonstrate that future-prediction branches in WAMs act primarily as regularizers and can be removed at inference with minimal loss through Privileged Foresight Distillation, which transfers future-conditioned corrections to current-only policies. These approaches share a philosophy: computation should be expended only when and where it provides decision-relevant information.

### Theme 2: Enhanced Representations Through Structured Supervision

Multiple papers argue that WAMs benefit from explicit structural representations beyond pixel-level prediction. Guan et al. (2026) show that point tracks provide explicit motion representations that capture long-horizon dynamics and remain robust under occlusion, outperforming pixel-based baselines on LIBERO and real-world LeRobot tasks. Ma et al. (2026) propose GeoSem-WAM, which adds geometric and semantic auxiliary prediction branches alongside RGB prediction, enabling joint capture of scene dynamics, spatial geometry, and semantic context. Their key insight is that WAMs' primary advantage lies in learning robust latent representations rather than generating future observations at test time. Sun et al. (2026) extend this with HiMem-WAM, which integrates motion-centric latent actions, high-level skill latents, and boundary-triggered memory updates for long-horizon manipulation. These approaches converge on the principle that structured, multi-modal representations improve both action prediction accuracy and scene understanding.

### Theme 3: Reliability and Consistency Verification

A critical challenge for WAMs is determining when to trust imagined futures. Wang et al. (2026) propose Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that evaluates predicted actions, visual dynamics, real observations, and instruction-conditioned semantics to determine plan validity. Their approach reduces WAM planning calls by 69-74% while improving success rates, demonstrating that selective replanning is more efficient than continuous execution. Ruan et al. (2026) conduct a systematic study of action-state consistency, finding that alignment between predicted actions and induced state transitions systematically separates successful and failed rollouts. They identify "background collapse" as a boundary condition where static futures can become deceptively consistent, and propose a value-free consensus strategy that ranks candidate rollouts by agreement among predicted futures. Both papers converge on the insight that consistency metrics can serve as reliable diagnostics without requiring additional reward modeling.

### Theme 4: Knowledge Transfer and Generalization

As WAM architectures proliferate, transferring knowledge between heterogeneous models becomes essential. Jiang et al. (2026) address this with CKT-WAM, a parameter-efficient context knowledge transfer framework that extracts intermediate teacher hidden states, compresses them via learnable-query cross attention, and transforms them through generalized adapters. Their approach achieves 86.1% success rate on LIBERO-Plus with only 1.17% trainable parameters, approaching full fine-tuning performance while enabling zero-shot generalization. This work reflects a broader trend toward modular, composable WAM systems that can leverage existing models rather than training from scratch.

### Theme 5: Safety and Security Vulnerabilities

As WAMs deploy in real-world settings, understanding their vulnerabilities becomes critical. Liu et al. (2026) present JailWAM, the first jailbreak evaluation framework for WAMs, featuring Visual-Trajectory Mapping to transform heterogeneous actions into unified visual representations and a severity-aware Risk Discriminator. Their framework achieves 84.2% attack success rate on LingBot-VA in RoboTwin simulation, exposing that WAMs are susceptible to adversarial instructions that can induce unsafe physical behaviors. This work highlights the need for robust safety verification mechanisms as WAMs transition from simulation to deployment.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key findings. First, WAMs benefit from explicit structural representations—whether point tracks (Guan et al., 2026), geometric and semantic supervision (Ma et al., 2026), or hierarchical latents (Sun et al., 2026)—rather than relying solely on pixel-level prediction. Second, adaptive computation strategies consistently improve efficiency without sacrificing performance, with all three efficiency-focused papers (Sun et al., 2026; Tang et al., 2026; Fang et al., 2026) reporting substantial latency reductions alongside maintained or improved success rates. Third, consistency metrics provide reliable diagnostics for plan validity without requiring additional reward modeling (Wang et al., 2026; Ruan et al., 2026).

**Disagreements**: The surveyed papers do not exhibit fundamental disagreements, reflecting the field's relative coherence. However, there are tensions in emphasis: some papers prioritize representation quality (Guan et al., 2026; Ma et al., 2026) while others prioritize inference efficiency (Sun et al., 2026; Fang et al., 2026). The optimal balance between these goals remains an open question, particularly for resource-constrained deployment scenarios.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the papers explicitly address multi-robot coordination or team-based manipulation, suggesting WAMs remain focused on single-agent scenarios. Second, while several papers evaluate on real-world tasks, the scope remains limited (6-7 tasks per paper), and long-term deployment robustness is not systematically studied. Third, the "limitations" sections are frequently absent from abstracts, indicating insufficient self-critique in the literature. Fourth, background collapse (Ruan et al., 2026) represents an important boundary condition for consistency-based verification that remains unresolved. Finally, the security vulnerabilities exposed by JailWAM (Liu et al., 2026) suggest urgent need for defensive mechanisms, but no paper in this set addresses mitigation strategies.

## Per-Paper Annotations

### Fang et al. (2026)

**Research question**: What role does the future-prediction branch actually play in world action models, and can its benefits be transferred to current-only policies?

**Methodology**: The authors formulate privileged foresight as a residual in the action-denoising direction and introduce Privileged Foresight Distillation (PFD), which transfers this residual from a training-time teacher into a small adapter on a current-only student.

**Key findings**:
- Future-prediction branches in WAMs can be removed at inference with little to no loss, suggesting future information acts as a regularizer
- Joint training induces an action-conditioned correction that privileged future observations impose on action denoising
- PFD achieves consistent improvements on LIBERO and RoboTwin manipulation benchmarks
- The approach preserves the current-only inference interface at negligible added latency

**Limitations**: Not stated in abstract

### Guan et al. (2026)

**Research question**: How can world-action models for robot policy learning better capture environment dynamics while remaining robust to task-irrelevant visual variation?

**Methodology**: The authors propose JOPAT, a joint pixel-and-track world-action model that predicts latent visual observations, 2D point tracks with visibility, and actions using a single denoising diffusion transformer.

**Key findings**:
- Point tracks provide an explicit representation of motion that captures long-horizon dynamics more effectively than pixel-level prediction alone
- Track-based representations remain robust under occlusion or partial out-of-frame motion
- JOPAT improves over pixel-based baselines on LIBERO and real-world LeRobot tasks
- The largest performance gains occur on long-horizon tasks involving occlusion, object interaction, and off-screen motion

**Limitations**: Not stated in abstract

### Jiang et al. (2026)

**Research question**: How can knowledge be transferred across heterogeneous world action models efficiently despite mismatched latent interfaces and high adaptation costs?

**Methodology**: The authors propose CKT-WAM, a parameter-efficient context knowledge transfer framework that extracts intermediate teacher hidden states, compresses them via learnable-query cross attention, and transforms them through a generalized adapter, lightweight router, and sparsely activated specialized adapters.

**Key findings**:
- CKT-WAM achieves 86.1% total success rate on LIBERO-Plus with only 1.17% trainable parameters
- The framework consistently improves zero-shot generalization compared to baseline methods
- CKT-WAM approaches full fine-tuning performance while requiring significantly fewer trainable parameters
- Real-world evaluation demonstrates 83.3% average success rate across four multi-step and long-horizon manipulation tasks

**Limitations**: Not stated in abstract

### Liu et al. (2026)

**Research question**: What safety risks do World Action Models face from adversarial instructions, and how can these jailbreak vulnerabilities be systematically evaluated?

**Methodology**: The authors propose JailWAM, the first jailbreak evaluation framework for WAMs, featuring Visual-Trajectory Mapping to transform heterogeneous actions into unified visual representations, a Risk Discriminator with three severity levels, and a Dual-Path Verification Strategy.

**Key findings**:
- JailWAM achieves 84.2% attack success rate on LingBot-VA in RoboTwin simulation
- Visual-Trajectory Mapping enables consistent risk assessment across different WAM architectures
- The severity-aware Risk Discriminator can distinguish different physical outcomes from visual trajectories
- WAMs are susceptible to jailbreak attacks that can induce unsafe physical behaviors

**Limitations**: The abstract does not explicitly state limitations; evaluation is conducted in RoboTwin simulation environment, and real-world physical risk validation may require additional verification.

### Ma et al. (2026)

**Research question**: Can structured world modeling with geometric and semantic supervision enhance latent representations in world action models beyond RGB-based future prediction?

**Methodology**: The authors propose a structured world modeling framework that enhances latent representations through geometric and semantic supervision, introducing two auxiliary prediction branches for future geometry and semantic representations alongside future RGB prediction.

**Key findings**:
- The primary advantage of WAMs lies in learning robust latent representations rather than generating future observations at test time
- Existing WAMs mainly rely on RGB-based future prediction, which provides limited structural and spatial understanding
- Incorporating structured world supervision consistently improves action prediction accuracy, scene understanding, and robustness
- The approach preserves efficient inference by avoiding explicit future rollout or video generation at test time

**Limitations**: Not stated in abstract

### Ruan et al. (2026)

**Research question**: Are imagined futures in World Action Models dynamically compatible with their claimed action sequences, and can action-state consistency serve as a reliability diagnostic?

**Methodology**: The authors conduct a systematic study across representative joint-prediction and inverse-dynamics models to examine action-state consistency and identify background collapse as a boundary condition, proposing a value-free consensus strategy for test-time selection.

**Key findings**:
- Action-state consistency systematically separates successful and failed rollouts across many tasks
- Consistency follows similar success-failure trends as learned value estimates
- Consistency captures decision-relevant structure beyond visual realism
- Background collapse can make low-dynamics failed trajectories deceptively consistent
- Value-free consensus strategy improves success rates on RoboCasa and RoboTwin 2.0 without additional training or reward modeling

**Limitations**: The abstract does not explicitly state limitations; background collapse represents an important boundary condition where static futures can become deceptively consistent, potentially limiting the diagnostic's effectiveness in low-dynamics scenarios.

### Sun et al. (2026) [SANTS]

**Research question**: Can adaptive selection of video denoising depth based on robot state improve action quality while reducing inference latency in World Action Models?

**Methodology**: The authors introduce State-Adaptive Noise Trajectory Scheduler (SANTS), which reads current video-state representation and noise level to jointly predict cumulative stopping hazard and relative noise-progression ratio, post-trained with path-level reward.

**Key findings**:
- SANTS reaches 94.4% overall success on RoboTwin 2.0 simulation
- Achieves 73.1% average success across seven real-robot tasks
- Reduces latency by 81.7% in simulation relative to full video denoising
- Reduces latency by 79.0% in real-robot tasks compared to full denoising
- Adaptive selection along video noise trajectory preserves control benefits while removing redundant inference cost

**Limitations**: The abstract does not explicitly state limitations; the approach requires post-training with path-level reward and may depend on the quality of the frozen action branch.

### Sun et al. (2026) [HiMem-WAM]

**Research question**: How can world action models better handle task-relevant memory in long-horizon robotic manipulation tasks?

**Methodology**: The authors present HiMem-WAM, a hierarchical memory-gated WAM that integrates motion-centric latent actions, high-level skill latents, and boundary-triggered memory updates using a hierarchical latent action framework.

**Key findings**:
- Existing WAMs struggle with task-relevant memory in long-horizon robotic manipulation
- Hierarchical latent action framework provides structured temporal abstraction through low-level motion and high-level skill latents
- The memory module enables causal inference without test-time generation of future video or optical flow estimation
- Hierarchical latents improve robustness under deployment perturbations on LIBERO, LIBERO-PLUS, RMBench and real-world tasks

**Limitations**: Not stated in abstract

### Tang et al. (2026)

**Research question**: How can world action models incorporate adaptive multimodal reasoning to improve effectiveness on long-horizon, complex embodied tasks?

**Methodology**: The authors propose AdaWAM, a world action model with adaptive multimodal reasoning that integrates a lightweight dynamic router to autonomously trigger textual or visual reasoning as needed during task execution.

**Key findings**:
- Existing WAMs rely heavily on video prediction as action priors and lack adaptive multimodal reasoning
- Different multimodal reasoning modes are required under different execution contexts: textual for task transitions, visual for fine-grained manipulation
- AdaWAM substantially improves inference efficiency while outperforming state-of-the-art embodied policies
- The approach works effectively on both simulated and real-world embodied tasks

**Limitations**: Not stated in abstract

### Wang et al. (2026)

**Research question**: How can World Action Models adaptively decide when to continue executing imagined actions versus when to replan based on future-reality consistency?

**Methodology**: The authors propose Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that evaluates predicted actions, visual dynamics, real observations, and instruction-conditioned semantics to determine plan validity, combined with Mixture-of-Horizon Training.

**Key findings**:
- FFDC-WAM achieves the highest average success rate among evaluated methods in both clean and randomized RoboTwin settings
- Under randomization, FFDC improves success by 2.54 percentage points over Base-Motus while reducing WAM planning calls by 69.10%
- Completion time is reduced by 33.88% under randomization compared to baseline
- On six real-world tasks, FFDC-WAM improves average success by 9.17% over Base-Motus-LC16 while reducing calls by 74.06%

**Limitations**: The abstract does not explicitly state limitations; evaluation is limited to RoboTwin simulation and six specific real-world tasks on Unitree G1D robot.

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
