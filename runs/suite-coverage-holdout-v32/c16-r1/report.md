# Systematic Literature Review: World Action Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "world action models", filtered to category cs.RO, published between 2024-06-18 and 2026-06-17
**Citation format**: APA 7th edition

## Executive Summary

World Action Models (WAMs) represent an emerging paradigm in embodied AI that jointly predicts future observations and actions for robotic manipulation. The surveyed literature from mid-2024 to mid-2026 reveals a field rapidly maturing beyond basic future prediction toward sophisticated architectures addressing efficiency, memory, multimodal reasoning, safety, and knowledge transfer. Recent work demonstrates that the primary value of WAMs lies not in generating future observations at test time, but in learning robust latent representations that capture environment dynamics. Key advances include parameter-efficient knowledge transfer achieving near full-fine-tuning performance with only 1.17% trainable parameters, adaptive execution strategies reducing planning calls by up to 74%, and hierarchical memory mechanisms enabling reliable long-horizon manipulation. However, significant challenges remain in ensuring dynamic consistency between imagined futures and actual outcomes, addressing safety vulnerabilities to adversarial attacks, and determining when model imagination should be trusted versus when replanning is necessary.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "world action models", filtered to category cs.RO, published between 2024-06-18 and 2026-06-17. Papers were sorted by submission date and all 10 matching results were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, all extracted limitations fields reported "not stated in abstract," indicating that detailed limitation discussions appear only in full paper texts.

## Themes

### Theme 1: Efficiency Through Adaptive Computation

A dominant thread in recent WAM research focuses on reducing computational overhead while preserving or improving performance. Rather than uniformly applying full denoising or future prediction at every step, newer approaches adaptively modulate computation based on task demands and state conditions.

SANTS (State-Adaptive Noise Trajectory Scheduler) represents a fundamental shift from fixed terminal denoising depth to state-adaptive selection along the video noise trajectory (Sun et al., 2026). By reading the current video-state representation and noise level, SANTS jointly predicts a cumulative stopping hazard and relative noise-progression ratio, achieving 81.7% latency reduction on RoboTwin 2.0 while maintaining 94.4% overall success. This work demonstrates that video refinement reduces action error only up to a state-dependent point, after which gains saturate or reverse.

FFDC-WAM extends this adaptive philosophy to execution control, introducing a lightweight verifier that decides when to continue executing planned actions versus when to replan (Wang et al., 2026). The Future Forward Dynamics Causal Attention mechanism reasons over predicted actions, predicted visual dynamics, real observations, and instruction-conditioned semantics to verify future-reality consistency. This approach reduced WAM planning calls by 69.10% in randomized settings and 74.06% on real-world tasks while improving success rates, demonstrating that adaptive execution control can simultaneously improve efficiency and robustness.

AdaWAM introduces adaptive multimodal reasoning, using a lightweight dynamic router to autonomously trigger textual or visual reasoning as needed during task execution (Tang et al., 2026). Textual reasoning guides high-level action prediction during task transitions, while visual reasoning supports fine-grained manipulation during precise control phases. This contextual modulation of reasoning modes substantially improves inference efficiency while outperforming state-of-the-art embodied policies on both simulated and real-world tasks.

### Theme 2: Memory and Temporal Abstraction for Long-Horizon Tasks

Long-horizon robotic manipulation presents distinctive challenges requiring sustained task-relevant memory and structured temporal abstraction. Recent work addresses these challenges through hierarchical latent representations and boundary-triggered memory mechanisms.

HiMem-WAM introduces a Hierarchical Memory-Gated architecture that integrates motion-centric latent actions, high-level skill latents, and boundary-triggered memory updates (Sun et al., 2026). The approach uses a hierarchical latent action framework jointly learning low-level motion and high-level skill latents, with a boundary-aware memory gate that writes compact task states at predicted skill transitions. This enables causal inference without test-time generation of future video or optical flow estimation, with the memory module providing substantial benefits for memory-dependent long-horizon manipulation on LIBERO, LIBERO-PLUS, RMBench, and real-world tasks.

The privileged foresight distillation work reveals that future information in WAMs acts as an action-conditioned correction rather than merely a regularizer (Fang et al., 2026). By formulating privileged foresight as a residual in the action-denoising direction and transferring this residual from a training-time teacher into a small adapter on a current-only student, PFD achieves consistent improvements on LIBERO and RoboTwin manipulation benchmarks while preserving the current-only inference interface at negligible added latency. This suggests that temporal abstraction benefits can be distilled into efficient architectures without requiring explicit future generation at inference time.

### Theme 3: Structured Representations Beyond Pixels

A significant conceptual advance in the surveyed literature is the recognition that pixel-based future prediction alone provides limited structural and spatial understanding. Multiple papers propose augmenting or replacing pixel representations with more structured alternatives capturing geometry, semantics, or motion.

GeoSem-WAM enhances latent representations through geometric and semantic supervision alongside future RGB prediction (Ma et al., 2026). The framework introduces two auxiliary prediction branches for future geometry and semantic representations, enabling joint capture of scene dynamics, spatial geometry, and semantic context within a unified latent space. This work explicitly identifies that the primary advantage of WAMs lies in learning robust latent representations rather than generating future observations at test time, with structured world supervision consistently improving action prediction accuracy while preserving efficient inference.

JOPAT takes a different approach, proposing that point tracks provide an explicit representation of motion capturing long-horizon dynamics more effectively than pixel appearance alone (Guan et al., 2026). The Joint Pixel-And-Track World-Action Model predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer. Track-based representations remain robust under occlusion or partial out-of-frame motion, with the largest performance gains occurring on long-horizon tasks involving occlusion, object interaction, and off-screen motion. This work demonstrates that motion-centric representations complement appearance-based prediction, particularly for tasks requiring sustained tracking through visual disruptions.

### Theme 4: Safety, Consistency, and Trust Verification

As WAMs deploy in real-world robotic systems, ensuring safety and determining when model predictions can be trusted become critical concerns. The surveyed literature reveals both vulnerabilities and verification mechanisms.

JailWAM presents the first systematic evaluation of safety risks in WAMs when exposed to adversarially designed instructions (Liu et al., 2026). The framework integrates Visual-Trajectory Mapping to transform heterogeneous low-level action outputs into unified visual representations, a Risk Discriminator supervised by three safety levels (Safety Compliance, Motion Failure, Catastrophic Risk), and a Dual-Path Verification Strategy combining rapid risk screening with closed-loop physical simulation. The alarming 84.2% attack success rate on LingBot-VA indicates WAMs may be susceptible to jailbreak attacks inducing unsafe physical behaviors, highlighting an urgent need for safety hardening in embodied AI systems.

The dynamic consistency work identifies action-state consistency as a missing reliability axis for WAMs, examining whether imagined futures are dynamically compatible with the action sequences they claim to model (Ruan et al., 2026). This systematic study across representative joint-prediction and inverse-dynamics models reveals that action-state consistency systematically separates successful and failed rollouts, following similar success-failure trends as learned value estimates. However, background collapse presents an important boundary condition where low-dynamics failed trajectories can become deceptively consistent because static futures are easier to predict. The proposed value-free consensus strategy for test-time selection improves success rates on RoboCasa and RoboTwin 2.0 without additional training or reward modeling, suggesting that consistency captures decision-relevant structure beyond visual realism.

### Theme 5: Parameter-Efficient Knowledge Transfer

As the field develops multiple WAM variants, transferring knowledge across heterogeneous models becomes increasingly important. Recent work addresses the challenge of mismatched latent interfaces and high adaptation costs.

CKT-WAM proposes a parameter-efficient Context Knowledge Transfer framework that transfers teacher WAM knowledge into a student WAM through compact context in the text embedding space rather than output imitation or dense hidden-state matching (Jiang et al., 2026). The approach extracts intermediate teacher hidden states, reduces tokens via learnable-query cross attention, and transforms them through a generalized adapter, lightweight router, and sparsely activated specialized adapters, with the resulting context appended to the student's conditioning textual embeddings. Remarkably, CKT-WAM achieves 86.1% total success rate on LIBERO-Plus benchmark with only 1.17% trainable parameters, approaching full fine-tuning performance while demonstrating strong real-world long-horizon manipulation ability with 83.3% average success rate across four multi-step tasks.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several fundamental points. First, multiple papers converge on the insight that WAMs' primary value lies in learning robust latent representations rather than generating future observations at test time (Fang et al., 2026; Ma et al., 2026; Sun et al., 2026). Second, there is consensus that adaptive computation—whether through state-adaptive scheduling, adaptive multimodal reasoning, or adaptive execution control—can simultaneously improve efficiency and performance (Sun et al., 2026; Tang et al., 2026; Wang et al., 2026). Third, papers addressing long-horizon tasks consistently emphasize the need for structured temporal abstraction and memory mechanisms (Sun et al., 2026; Fang et al., 2026; Guan et al., 2026). Fourth, the literature agrees that structured representations beyond pixels—whether geometric, semantic, or motion-based—provide crucial advantages for complex embodied tasks (Ma et al., 2026; Guan et al., 2026).

**Disagreements**: The literature reveals tension between trusting model imagination versus verifying consistency with reality. FFDC-WAM assumes that imagined futures can be trusted when verified by a lightweight consistency checker, triggering replanning only when validity deteriorates (Wang et al., 2026). In contrast, the dynamic consistency work identifies fundamental limitations in action-state alignment, showing that even visually plausible futures may be dynamically incompatible with claimed action sequences (Ruan et al., 2026). This suggests that verification mechanisms themselves may need verification—a regress not yet addressed in the literature. Additionally, while CKT-WAM demonstrates that knowledge transfer through text embeddings is highly parameter-efficient (Jiang et al., 2026), other work on privileged foresight distillation transfers knowledge through action-denoising residuals (Fang et al., 2026), leaving open the question of which transfer mechanism generalizes better across heterogeneous WAM architectures.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, all surveyed papers report "not stated in abstract" for limitations, suggesting that detailed limitation discussions appear only in full texts—this review cannot assess whether authors adequately acknowledge their methods' boundaries. Second, while JailWAM identifies severe safety vulnerabilities with 84.2% attack success rates (Liu et al., 2026), none of the other surveyed papers address safety considerations, indicating that safety hardening may not yet be integrated into mainstream WAM development. Third, the dynamic consistency work identifies background collapse as a boundary condition where consistency verification fails (Ruan et al., 2026), but no paper proposes a complete solution to this fundamental limitation. Fourth, while parameter-efficient transfer achieves remarkable results (Jiang et al., 2026), the literature does not address whether transferred knowledge preserves safety properties or whether transfer itself introduces new vulnerabilities. Fifth, all evaluations focus on manipulation benchmarks (LIBERO, RoboTwin, RoboCasa) and real-world robotic tasks, but none address deployment in unstructured, open-world environments where distribution shift may be more severe. Finally, the literature does not address computational requirements for training these increasingly sophisticated architectures, raising questions about accessibility and environmental impact.

## Per-Paper Annotations

### Fang et al. (2026)

**Research question**: What role does the future-prediction branch actually play in world action models, and can its benefits be transferred to current-only policies?
**Methodology**: The authors formulate privileged foresight as a residual in the action-denoising direction and introduce Privileged Foresight Distillation (PFD), which transfers this residual from a training-time teacher into a small adapter on a current-only student. The teacher and student share the same backbone and differ only in the attention mask over video tokens.
**Key findings**:
- Future information in world action models acts as an action-conditioned correction rather than merely a regularizer
- PFD transfers the future-conditioned correction from a teacher to a current-only student without generating future video at inference
- PFD achieves consistent improvements on LIBERO and RoboTwin manipulation benchmarks
- The approach preserves the current-only inference interface at negligible added latency
- The gain reflects a genuine future-conditioned correction rather than a side effect of capacity or regularization
**Limitations**: not stated in abstract

### Guan et al. (2026)

**Research question**: How can world-action models for robot policy learning better capture environment dynamics while remaining robust to task-irrelevant visual variation?
**Methodology**: The authors propose JOPAT, a Joint Pixel-And-Track World-Action Model that predicts latent visual observations, 2D point tracks with visibility, and actions in a single denoising diffusion transformer. The approach leverages point tracks as an explicit representation of motion to capture long-horizon dynamics robustly under occlusion or partial out-of-frame motion.
**Key findings**:
- Point tracks provide an explicit representation of motion that captures long-horizon dynamics more effectively than pixel appearance alone
- Track-based representations remain robust under occlusion or partial out-of-frame motion
- JOPAT improves over pixel-based baselines on LIBERO and real-world LeRobot tasks
- The largest performance gains occur on long-horizon tasks involving occlusion, object interaction, and off-screen motion
**Limitations**: not stated in abstract

### Jiang et al. (2026)

**Research question**: How can knowledge be transferred across heterogeneous world action models (WAMs) despite mismatched latent interfaces, high adaptation costs, and rigid conventional distillation objectives?
**Methodology**: The authors propose CKT-WAM, a parameter-efficient Context Knowledge Transfer framework that transfers teacher WAM knowledge into a student WAM through compact context in the text embedding space rather than output imitation or dense hidden-state matching. The approach extracts intermediate teacher hidden states, reduces tokens via learnable-query cross attention (LQCA), and transforms them through a generalized adapter, lightweight router, and sparsely activated specialized adapters, with the resulting context appended to the student's conditioning textual embeddings.
**Key findings**:
- CKT-WAM consistently improves zero-shot generalization across evaluated tasks
- Achieves 86.1% total success rate on LIBERO-Plus benchmark with only 1.17% trainable parameters
- Performance approaches that of full fine-tuning methods
- Demonstrates strong real-world long-horizon manipulation ability with 83.3% average success rate across four multi-step tasks
**Limitations**: not stated in abstract

### Liu et al. (2026)

**Research question**: What safety risks do World Action Models face when exposed to adversarially designed instructions, and how can these risks be systematically evaluated?
**Methodology**: The authors propose JailWAM, the first jailbreak evaluation framework for WAMs, which integrates three innovations: Visual-Trajectory Mapping to transform model-specific actions into unified visual trajectory representations, a Risk Discriminator supervised by three safety levels (Safety Compliance, Motion Failure, Catastrophic Risk), and a Dual-Path Verification Strategy combining rapid risk screening with closed-loop physical simulation. Extensive experiments were conducted in the RoboTwin simulation environment.
**Key findings**:
- JailWAM achieves an 84.2% attack success rate on LingBot-VA, indicating WAMs may be susceptible to jailbreak attacks that induce unsafe physical behaviors
- Visual-Trajectory Mapping enables consistent risk assessment across different WAM architectures by transforming heterogeneous low-level action outputs into unified visual representations
- The severity-aware Risk Discriminator can distinguish different physical outcomes from visual trajectories and support scalable risk screening
- Dual-Path Verification Strategy reduces computational cost by restricting expensive verification to candidates with potential safety risks
**Limitations**: not stated in abstract

### Ma et al. (2026)

**Research question**: Can World Action Models be enhanced through geometric and semantic supervision to improve structural and spatial understanding of complex environments?
**Methodology**: The authors propose a structured world modeling framework that enhances latent representations through geometric and semantic supervision. Alongside future RGB prediction, the model introduces two auxiliary prediction branches for future geometry and semantic representations, enabling joint capture of scene dynamics, spatial geometry, and semantic context within a unified latent space.
**Key findings**:
- The primary advantage of WAMs lies in learning robust latent representations rather than generating future observations at test time
- RGB-based future prediction alone provides limited structural and spatial understanding of complex environments
- Incorporating structured world supervision consistently improves action prediction accuracy
- The approach enhances scene understanding and robustness under challenging embodied scenarios
- The method preserves efficient inference by avoiding explicit future rollout or video generation at test time
**Limitations**: not stated in abstract

### Ruan et al. (2026)

**Research question**: Are the imagined futures generated by World Action Models dynamically compatible with the action sequences they claim to model, beyond being merely visually plausible?
**Methodology**: The authors identify action-state consistency as a missing reliability axis for WAMs and conduct a systematic study across representative joint-prediction and inverse-dynamics models to examine the alignment between predicted actions and induced state transitions. They identify background collapse as a boundary condition and introduce a value-free consensus strategy for test-time selection that ranks candidate rollouts by agreement among predicted futures, evaluated on RoboCasa and RoboTwin 2.0.
**Key findings**:
- Action-state consistency systematically separates successful and failed rollouts across many tasks and follows similar success-failure trends as learned value estimates
- Background collapse is identified as an important boundary condition where low-dynamics failed trajectories can become deceptively consistent because static futures are easier to predict
- A value-free consensus strategy for test-time selection improves success rates on RoboCasa and RoboTwin 2.0 without additional training or reward modeling
- Consistency captures decision-relevant structure beyond visual realism in WAM rollouts
**Limitations**: not stated in abstract

### Sun et al. (2026) [HiMem-WAM]

**Research question**: How can World Action Models be improved to better handle task-relevant memory in long-horizon robotic manipulation?
**Methodology**: The authors present HiMem-WAM, a Hierarchical Memory-Gated WAM that integrates motion-centric latent actions, high-level skill latents, and boundary-triggered memory updates. The approach uses a hierarchical latent action framework that jointly learns low-level motion and high-level skill latents, with a boundary-aware memory gate that writes compact task states at predicted skill transitions.
**Key findings**:
- Hierarchical latent actions provide structured temporal abstraction for robotic manipulation
- The boundary-aware memory gate enables causal inference without test-time generation of future video or optical flow estimation
- Hierarchical latents improve robustness under deployment perturbations
- The memory module substantially benefits memory-dependent long-horizon manipulation
- HiMem-WAM shows improved performance on LIBERO, LIBERO-PLUS, RMBench and real-world tasks
**Limitations**: not stated in abstract

### Sun et al. (2026) [SANTS]

**Research question**: How can World Action Models optimize action generation by adaptively selecting the appropriate denoising depth along the video noise trajectory rather than using a fixed terminal denoising depth?
**Methodology**: The authors introduce State-Adaptive Noise Trajectory Scheduler (SANTS), a lightweight scheduler for video-to-action diffusion policies that reads the current video-state representation and noise level, then jointly predicts a cumulative stopping hazard and a relative noise-progression ratio. SANTS is post-trained with a path-level reward computed after the frozen action branch generates the final action chunk, optimizing the scheduler for downstream action quality while penalizing redundant video-state updates.
**Key findings**:
- SANTS reaches 94.4% overall success on RoboTwin 2.0 and 73.1% average success across seven real-robot tasks
- SANTS reduces latency by 81.7% and 79.0% relative to full video denoising on RoboTwin 2.0 and real-robot tasks, respectively
- Controlled denoising-depth scans show that video refinement can reduce action error up to a state-dependent point, after which the gain may saturate or reverse
- Adaptive selection along the video noise trajectory preserves the control benefits of WAM-style future reasoning while removing much of its redundant inference cost
**Limitations**: not stated in abstract

### Tang et al. (2026)

**Research question**: How can World Action Models be enhanced with adaptive multimodal reasoning to improve effectiveness on long-horizon, complex tasks?
**Methodology**: The authors propose AdaWAM, a world action model with adaptive multimodal reasoning that integrates a lightweight dynamic router to autonomously trigger textual or visual reasoning as needed during task execution. Textual reasoning is used during task transitions for high-level action prediction, while visual reasoning is used during fine-grained manipulation for precise control.
**Key findings**:
- WAMs require different multimodal reasoning modes under different execution contexts
- Textual reasoning is essential during task transitions to guide high-level action prediction
- Visual reasoning is critical during fine-grained manipulation for precise control
- AdaWAM substantially improves inference efficiency while outperforming state-of-the-art embodied policies
- The approach works effectively on both simulated and real-world embodied tasks
**Limitations**: not stated in abstract

### Wang et al. (2026)

**Research question**: How can World Action Models adaptively decide when to continue executing planned actions versus when to replan based on the consistency between imagined futures and reality?
**Methodology**: The authors propose Future Forward Dynamics Causal Attention (FFDC), a lightweight verifier that reasons over predicted actions, predicted visual dynamics, real observations, and instruction-conditioned semantics to verify future-reality consistency. They combine this verification mechanism with Mixture-of-Horizon Training to improve long-horizon trajectory coverage and evaluate on RoboTwin in both clean and randomized settings, as well as on six real-world tasks on a Unitree G1D robot.
**Key findings**:
- FFDC-WAM achieves the highest average success rate among evaluated methods in both clean and randomized settings on RoboTwin
- Under randomization, FFDC-WAM improves success by 2.54 percentage points over Base-Motus while reducing WAM planning calls by 69.10% and completion time by 33.88%
- On six real-world tasks on a Unitree G1D robot, FFDC-WAM improves average success by 9.17% over Base-Motus-LC16 while reducing calls by 74.06% and completion time by 51.31%
- The verifier allows continued execution when plans remain reliable and triggers replanning when validity deteriorates
**Limitations**: not stated in abstract

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
