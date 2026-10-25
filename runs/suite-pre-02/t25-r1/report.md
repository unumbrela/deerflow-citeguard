# Systematic Literature Review: End-to-End Autonomous Driving

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "end-to-end driving", filtered to category cs.RO, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

End-to-end autonomous driving has experienced rapid advancement in the past two years, with research focusing on addressing fundamental challenges in interpretability, training efficiency, and closed-loop deployment. The surveyed literature reveals a field maturing from pure architecture design toward nuanced considerations of data quality, reasoning capabilities, and safety evaluation. A dominant theme is bridging the gap between open-loop training and closed-loop performance, with multiple approaches including post-training refinement, trajectory optimization, and self-play scaling. Vision-language models and chain-of-thought reasoning represent emerging directions for improving decision-making transparency. Safety evaluation under rare but critical scenarios has gained attention, with new frameworks for generating photorealistic test scenarios. Collectively, these works demonstrate that end-to-end driving systems are achieving competitive performance on benchmarks while grappling with real-world deployment challenges.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "end-to-end driving", filtered to category cs.RO, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review focuses on cs.RO category, potentially missing relevant work in cs.CV or other categories.

## Themes

### Theme 1: Interpretability and Reasoning in End-to-End Systems

A significant challenge in end-to-end driving is the lack of interpretability and controllability in driving decisions, which hinders real-world deployment. Two papers address this by integrating reasoning capabilities into end-to-end architectures. Wang et al. (2024) introduced DriveCoT, which collects chain-of-thought labels alongside sensor data and control decisions in the CARLA simulator, enabling the model to generate interpretable reasoning before making driving decisions. Their DriveCoT-Agent demonstrated strong performance in both open-loop and closed-loop evaluations, validating that CoT integration does not sacrifice performance.

Extending this concept, Tan et al. (2025) proposed LCDrive, which represents chain-of-thought reasoning in a latent action-aligned space rather than natural language. The model interleaves action-proposal tokens with world model tokens that capture predicted future outcomes, enabling more efficient reasoning. LCDrive achieved faster inference and better trajectory quality compared to both non-reasoning and text-reasoning baselines, with larger improvements from interactive reinforcement learning. The key insight is that latent representations can capture reasoning more efficiently than natural language while maintaining action alignment.

### Theme 2: Dataset Quality and Learner-Expert Alignment

The quality and composition of training datasets significantly impact end-to-end driving performance, yet this factor is often overlooked in favor of architecture design. Zimmerlin et al. (2024) systematically analyzed training dataset factors and discovered that expert driving style significantly affects downstream policy performance, and that frame weighting based on simplistic criteria like class frequencies is ineffective for complex datasets. Instead, estimating frame importance by whether it changes target labels compared to previous frames can reduce dataset size without losing critical information. These insights enabled their model to achieve 1st and 2nd place on the 2024 CARLA Challenge.

Nguyen et al. (2025) extended this analysis by studying the misalignment between privileged expert demonstrations and sensor-based student observations in imitation learning. They identified that experts have significantly higher visibility (ignoring occlusions) and far lower uncertainty (knowing other vehicles' actions) than students, making them difficult to imitate reliably. After implementing modifications to narrow these learner-expert asymmetries, their TransFuser v6 achieved 95 DS on Bench2Drive and more than doubled prior performances on Longest6 v2 and Town13 benchmarks. The work demonstrates that careful attention to data alignment can yield larger improvements than architecture changes alone.

### Theme 3: Bridging the Open-Loop to Closed-Loop Gap

A fundamental challenge in end-to-end driving is that policies trained through open-loop behavior cloning must ultimately operate in closed-loop deployment, creating a performance gap. Multiple papers address this mismatch through different strategies. Zhang et al. (2026) identified that waypoint-based supervision creates physically incoherent intermediate trajectories, and introduced Endpoint-Constrained Optimization (ECO), a lightweight postprocessing layer that preserves predicted endpoints while reshaping intermediate waypoints for controller feasibility. ECO requires no additional training and improved VaVAM from 18.1 to 31.0 HD-Score (+71%) on HUGSIM, achieving 1st place on the HUGSIM Closed-Loop Driving Challenge.

Da Col et al. (2026) proposed OPTED, which decouples reinforcement learning from end-to-end policy post-training. A privileged teacher trained via RL on vectorized inputs provides supervision to pre-trained camera-based students during closed-loop post-training using neural reconstructions of real driving logs. OPTED increased driving scores by factors of 1.6× and 9.5× for TransFuser and VaVAM respectively, while requiring approximately 1000× fewer simulator interactions than direct RL post-training. This approach demonstrates that efficient closed-loop adaptation is possible without the computational cost of direct reinforcement learning on sensor inputs.

### Theme 4: Scaling Training Through Self-Play and Efficient Generation

Scaling training data and computation is critical for improving end-to-end driving performance, but traditional approaches face diminishing returns. Rowe et al. (2026) introduced Gigapixel, a high-throughput batched driving simulator achieving 50k agent steps per second with simplified bounding-box rendering that preserves essential scene structure. They proposed self-play DAgger training, where pixel-based policies are trained via on-policy distillation from a privileged RL teacher, followed by lightweight perception adaptation for sim-to-real transfer. Policies trained without any human trajectory supervision achieved competitive performance on HUGSIM and NAVSIM-v2 benchmarks, with scaling self-play training yielding proportional gains.

Chai et al. (2025) addressed the computational cost of generative models for multi-modal planning by proposing AnchDrive, which bootstraps diffusion policies with hybrid trajectory anchors. Rather than denoising from pure noise, AnchDrive initializes its planner with anchors derived from static driving priors and dynamic context-aware trajectories decoded by a Transformer. The diffusion model then refines these anchors by predicting trajectory offset distributions, enabling efficient generation of diverse, high-quality trajectories. AnchDrive set a new state-of-the-art on the NAVSIM benchmark, demonstrating that anchor-based bootstrapping significantly reduces computational costs while maintaining trajectory quality.

### Theme 5: Vision-Language Models for End-to-End Driving

The integration of large language models, particularly vision-language models, represents an emerging direction for end-to-end autonomous driving. Guo et al. (2025) demonstrated that combining end-to-end architectural design with knowledgeable VLMs yields impressive performance on driving tasks. Their method, which achieved 2nd place in the CVPR2024 E2E Challenge, uses only a single camera and was the best camera-only solution across the leaderboard. This work establishes that VLMs can successfully contribute to autonomous driving decision-making despite being originally designed for language tasks, and that vision-based driving approaches have significant potential for end-to-end autonomous driving.

### Theme 6: Safety Evaluation Under Critical Scenarios

Evaluating end-to-end driving systems under rare but safety-critical scenarios is essential for real-world deployment, yet generating such scenarios is challenging. Liu et al. (2026) presented ControlPed, a framework that combines trajectory-level conflict synthesis with 3D Gaussian Splatting to generate photorealistic, motion-controllable safety-critical pedestrian scenarios. Built on the HazardPed dataset of 10,352 traffic videos with 422 conflict trajectories, ControlPed generates conflict trajectories, lifts them into 3D human motion sequences via text-conditioned motion diffusion, and renders multi-view sensor observations using animatable 3DGS avatars. Safety evaluation in 88 rendered scenarios revealed that seven leading end-to-end driving models suffered severe performance drops, with mean HDScore plunging from 88.8 to 47.4, exposing major failure modes under dangerous pedestrian behaviors.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of addressing the open-loop to closed-loop gap as a fundamental challenge in end-to-end driving (Zhang et al., 2026; Da Col et al., 2026; Nguyen et al., 2025). There is also consensus that dataset quality and composition significantly impact performance, often more than architecture design choices (Zimmerlin et al., 2024; Nguyen et al., 2025). The surveyed literature agrees that simulation-based training and evaluation remain essential, but sim-to-real transfer techniques are necessary for real-world deployment.

**Disagreements**: While most papers focus on improving performance through better training strategies, there is divergence on the role of interpretability. Wang et al. (2024) and Tan et al. (2025) prioritize interpretable reasoning, whereas other works prioritize performance gains through latent representations or postprocessing without explicit interpretability. There is also variation in the emphasis on human supervision: some works achieve competitive results without human trajectory supervision through self-play (Rowe et al., 2026), while others rely heavily on carefully curated human demonstrations (Zimmerlin et al., 2024; Nguyen et al., 2025).

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, most papers rely on simulation environments (CARLA, HUGSIM, AlpaSim, NAVSIM), with limited discussion of real-world deployment results. The sim-to-real gap remains a significant challenge, with only a few papers addressing perception adaptation for transfer (Rowe et al., 2026; Da Col et al., 2026). Second, safety evaluation is underexplored relative to performance optimization, with only one paper (Liu et al., 2026) focusing specifically on generating safety-critical scenarios. Third, the computational cost of training and deployment is mentioned but not systematically addressed across papers, with only AnchDrive (Chai et al., 2025) and OPTED (Da Col et al., 2026) explicitly targeting efficiency improvements.

The reliance on privileged information (HD-maps, bounding boxes, expert knowledge) in several approaches (Da Col et al., 2026; Nguyen et al., 2025; Rowe et al., 2026) raises questions about deployment in environments where such information is unavailable. Additionally, while vision-language models show promise (Guo et al., 2025), their computational requirements and latency for real-time deployment are not thoroughly addressed. Finally, the literature lacks long-term studies of deployment reliability and failure mode analysis in real-world conditions.

## Per-Paper Annotations

### Chai et al. (2025)

**Research question**: How can diffusion policies for end-to-end driving be bootstrapped to reduce the high computational cost of traditional generative models?
**Methodology**: AnchDrive initializes its planner with hybrid trajectory anchors derived from both static driving priors and dynamic context-aware trajectories decoded by a Transformer, then uses diffusion to refine these anchors by predicting trajectory offset distributions.
**Key findings**:
- Anchor-based bootstrapping enables efficient generation of diverse, high-quality trajectories compared to traditional diffusion from pure noise
- Hybrid anchors combining static priors and dynamic context-aware trajectories provide rich initialization
- AnchDrive sets a new state-of-the-art on the NAVSIM benchmark
- The framework demonstrates strong generalizability across driving scenarios
**Limitations**: The approach depends on the quality of both static priors and the Transformer that generates dynamic anchors; evaluation is primarily demonstrated on NAVSIM benchmark with limited discussion of performance on other datasets or real-world deployment.

### Da Col et al. (2026)

**Research question**: How can closed-loop post-training for end-to-end driving policies be performed efficiently without costly simulation requirements for sensor-based policies?
**Methodology**: OPTED decouples reinforcement learning from policy post-training: a privileged teacher trained via RL on vectorized inputs provides supervision to pre-trained camera-based students during closed-loop post-training using neural reconstructions (3DGS) of real driving logs.
**Key findings**:
- Closed-loop post-training mitigates compounding errors that occur when vehicles operate outside the training data distribution
- OPTED applied to TransFuser and VaVAM increased driving scores by factors of 1.6× and 9.5× respectively
- OPTED matches closed-loop performance with approximately 1000× fewer simulator interactions than direct RL post-training
- The approach stays closer to the human prior compared to direct reinforcement learning methods
**Limitations**: The method requires a privileged teacher with access to HD-map and bounding box information, and relies on neural reconstructions of driving logs which may not perfectly capture real-world complexity.

### Guo et al. (2025)

**Research question**: Can powerful large language models, particularly multi-modality Vision Language Models, benefit end-to-end autonomous driving tasks?
**Methodology**: Combined end-to-end architectural design with knowledgeable Vision Language Models (VLMs), implementing a camera-only solution that leverages VLM capabilities for driving task execution.
**Key findings**:
- Combining end-to-end architecture with VLMs yields impressive performance on driving tasks
- The method achieved the best camera-only solution across the CVPR2024 E2E Challenge leaderboard
- A single camera input is sufficient for competitive end-to-end driving when paired with VLMs
- Large language models can successfully contribute to autonomous driving decision-making
**Limitations**: The camera-only approach may not match the robustness of multi-sensor fusion systems in adverse conditions, and the evaluation was specific to the CVPR challenge environment.

### Liu et al. (2026)

**Research question**: How can photorealistic, controllable safety-critical pedestrian scenarios be generated to evaluate end-to-end driving systems under rare vehicle-pedestrian interactions?
**Methodology**: ControlPed combines trajectory-level conflict synthesis with 3D Gaussian Splatting, generating conflict trajectories from the HazardPed dataset, lifting them into 3D human motion sequences via text-conditioned motion diffusion, and rendering multi-view sensor observations using animatable 3DGS avatars.
**Key findings**:
- Seven leading end-to-end driving models suffer severe performance drops in safety-critical pedestrian scenarios, with mean HDScore plunging from 88.8 to 47.4
- The framework successfully generates photorealistic, motion-controllable safety-critical scenarios
- HazardPed dataset comprises 10,352 traffic videos with 422 conflict trajectories and 857 annotated 3D human motions
- Safety evaluation in 88 rendered scenarios exposes major failure modes under dangerous pedestrian behaviors
**Limitations**: Safety evaluation was conducted on only 88 rendered scenarios which may not cover the full space of dangerous pedestrian behaviors; the framework is specifically focused on vehicle-pedestrian interactions.

### Nguyen et al. (2025)

**Research question**: How does misalignment between privileged expert demonstrations and sensor-based student observations limit imitation learning effectiveness in autonomous driving?
**Methodology**: Empirically studied visibility and uncertainty asymmetries between experts and students in CARLA simulation, then implemented modifications to TransFuser v6 to narrow these gaps through improved student-expert alignment and better navigational intent specification.
**Key findings**:
- Experts have significantly higher visibility and far lower uncertainty than students, making them difficult to imitate reliably
- Navigational intent is under-specified in student models at test time when provided via only a single target point
- TransFuser v6 achieves 95 DS on Bench2Drive after addressing learner-expert asymmetries
- Performance more than doubles on Longest6 v2 and Town13 benchmarks
- Integration of perception supervision shows consistent gains on NAVSIM and Waymo benchmarks
**Limitations**: The work primarily focuses on simulation (CARLA) and requires sim-to-real transfer techniques for real-world deployment; the interventions are specific to the TransFuser architecture.

### Rowe et al. (2026)

**Research question**: Can large-scale self-play training from pixel observations in simulation overcome the limitations of offline human demonstration datasets for end-to-end driving?
**Methodology**: Introduced Gigapixel, a high-throughput batched driving simulator with perspective rendering at 50k agent steps per second, and proposed self-play DAgger training where pixel-based policies are trained via on-policy distillation from a privileged RL teacher.
**Key findings**:
- Policies trained via self-play achieve competitive performance on HUGSIM and NAVSIM-v2 benchmarks without any human trajectory supervision
- Scaling self-play training yields proportional gains in policy performance
- Simplified bounding-box rendering preserves essential scene structure while achieving high throughput
- Self-play DAgger training addresses the sample inefficiency of direct pixel-space self-play RL
**Limitations**: The approach relies on simulation with simplified rendering that may not capture all real-world visual complexity; the sim-to-real gap still requires perception adaptation techniques.

### Tan et al. (2025)

**Research question**: Can latent representations rather than natural language provide more efficient chain-of-thought reasoning for autonomous driving decisions?
**Methodology**: LCDrive represents CoT reasoning in an action-aligned latent space using interleaved action-proposal tokens and world model tokens grounded in a learned latent world model, with cold-start supervision from ground-truth future rollouts followed by closed-loop reinforcement learning.
**Key findings**:
- Latent language representations capture possible outcomes of driving actions more efficiently than natural language text
- LCDrive achieves faster inference compared to both non-reasoning and text-reasoning baselines
- The model produces better trajectory quality than baseline approaches
- Interactive reinforcement learning yields larger improvements for LCDrive
**Limitations**: The latent CoT representations are less interpretable than natural language reasoning; the approach requires ground-truth future rollouts for cold-start supervision which may be expensive to obtain.

### Wang et al. (2024)

**Research question**: How can interpretability and controllability be improved in end-to-end driving systems to enable real-world deployment?
**Methodology**: Created a comprehensive end-to-end driving dataset (DriveCoT) using the CARLA simulator with sensor data, control decisions, and chain-of-thought labels; proposed a rule-based expert policy to generate ground truth reasoning labels and a baseline model trained on this dataset.
**Key findings**:
- End-to-end driving systems lack interpretability and controllability, hindering real-world deployment
- Chain-of-thought reasoning can be successfully integrated with end-to-end driving architectures
- The DriveCoT dataset enables evaluation of accuracy across different reasoning aspects and final driving decisions
- DriveCoT-Agent demonstrates strong performance in both open-loop and closed-loop evaluations
**Limitations**: The dataset relies on CARLA simulator data rather than real-world driving scenarios, and the rule-based expert policy may not fully capture the nuances of human driving behavior.

### Zhang et al. (2026)

**Research question**: How can the open-loop/closed-loop performance gap in end-to-end driving models be addressed, particularly regarding trajectory physical feasibility?
**Methodology**: Identified that waypoint-based supervision creates physically incoherent intermediate trajectories; introduced Endpoint-Constrained Optimization (ECO), a lightweight postprocessing layer that preserves predicted endpoints while reshaping intermediate waypoints for controller feasibility.
**Key findings**:
- Waypoint-based supervision does not ensure physically coherent or controller-trackable intermediate trajectories
- Trajectory inconsistencies concentrate primarily at intermediate waypoints while predicted endpoints remain comparatively reliable
- ECO requires no additional training and can be inserted between various waypoint-emitting policies and controllers
- ECO improved VaVAM from 18.1 to 31.0 HD-Score (+71%) on HUGSIM, achieving 1st place on the HUGSIM Closed-Loop Driving Challenge
**Limitations**: ECO is a postprocessing solution that addresses symptoms rather than root causes of the open-loop/closed-loop gap; evaluation was conducted in simulation environments.

### Zimmerlin et al. (2024)

**Research question**: How does training dataset quality and composition impact end-to-end driving performance on the challenging CARLA Leaderboard 2.0?
**Methodology**: Systematically analyzed training dataset factors including expert style, frame weighting strategies, and data reduction techniques; applied findings to achieve top rankings on the 2024 CARLA Challenge and Bench2Drive test routes.
**Key findings**:
- Expert driving style significantly affects downstream policy performance
- Frame weighting based on simplistic criteria like class frequencies is ineffective for complex datasets
- Estimating frame importance by label changes can reduce dataset size without losing important information
- Incorporating these dataset insights achieved 1st and 2nd place on the 2024 CARLA Challenge
- Current evaluation metrics contain design flaws that the authors propose modifications to address
**Limitations**: The analysis focuses primarily on CARLA simulator environments, and findings may not fully generalize to real-world autonomous driving scenarios.

## References

Chai, J., Jiang, A., Jiang, H., Mu, S., Gu, Z., Sun, H., & Xu, S. (2025). AnchDrive: Bootstrapping diffusion policies with hybrid trajectory anchors for end-to-end driving. arXiv. https://arxiv.org/abs/2509.20253

Da Col, D., Igl, M., Karkus, P., Chitta, K., Ivanovic, B., Pavone, M., Schindler, K., & Sakaridis, C. (2026). OPTED: On-policy fine-tuning for end-to-end driving using a render-free teacher. arXiv. https://arxiv.org/abs/2609.20756

Guo, Z., Luo, Y., Sha, L., Wang, D., Wang, P., Xu, C., & Yang, Y. (2025). 2nd Place Solution for CVPR2024 E2E Challenge: End-to-end autonomous driving using Vision Language Model. arXiv. https://arxiv.org/abs/2509.02659

Liu, S., Li, M., Yu, H., Lin, H., Zhou, Q., Nie, B., & Zhao, D. (2026). Controllable and photorealistic pedestrian risky motion generation for end-to-end driving safety evaluation. arXiv. https://arxiv.org/abs/2610.06171

Nguyen, L., Fauth, M., Jaeger, B., Dauner, D., Igl, M., Geiger, A., & Chitta, K. (2025). LEAD: Minimizing learner-expert asymmetry in end-to-end driving. arXiv. https://arxiv.org/abs/2512.20563

Rowe, L., Girgis, R., de Schaetzen, R., Cornelisse, D., Grandhi, A., Heide, F., Vinitsky, E., Pal, C., & Paull, L. (2026). Scaling self-play for end-to-end driving. arXiv. https://arxiv.org/abs/2606.19641

Tan, S., Chitta, K., Chen, Y., Tian, R., You, Y., Wang, Y., Luo, W., Cao, Y., Krahenbuhl, P., Pavone, M., & Ivanovic, B. (2025). Latent chain-of-thought world modeling for end-to-end driving. arXiv. https://arxiv.org/abs/2512.10226

Wang, T., Xie, E., Chu, R., Li, Z., & Luo, P. (2024). DriveCoT: Integrating chain-of-thought reasoning with end-to-end driving. arXiv. https://arxiv.org/abs/2403.16996

Zhang, B., Golchoubian, M., Gilitschenski, I., Ivanovic, B., & Chitta, K. (2026). Guiding end-to-end driving models with endpoint-constrained trajectory optimization. arXiv. https://arxiv.org/abs/2609.31383

Zimmerlin, J., Beißwenger, J., Jaeger, B., Geiger, A., & Chitta, K. (2024). Hidden biases of end-to-end driving datasets. arXiv. https://arxiv.org/abs/2412.09602
