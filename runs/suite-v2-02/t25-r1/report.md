# Systematic Literature Review: End-to-End Autonomous Driving

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "end-to-end autonomous driving", cs.RO, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of end-to-end autonomous driving has witnessed significant advancement over the past two years, with research focusing on improving system robustness, interpretability, and safety. The surveyed literature reveals a clear trend toward incorporating higher-level cognitive processes into end-to-end frameworks, moving beyond pure perception-action mapping to include reasoning, planning, and causal understanding. Key developments include cognitive-hierarchy guided approaches, map-assisted planning, multi-sensor fusion innovations, and knowledge-driven policies. Safety analysis frameworks and data scaling laws have emerged as critical enablers for real-world deployment. The collective body of work demonstrates substantial progress in addressing long-tail scenarios, achieving human-like reasoning, and maintaining system compatibility under perception updates, though challenges remain in standardization and comprehensive safety validation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "end-to-end autonomous driving", filtered to category cs.RO, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Cognitive and Hierarchical Reasoning

A prominent direction in recent end-to-end autonomous driving research involves incorporating human-like cognitive hierarchies and reasoning processes into model architectures. Wang et al. (2025) introduced CogAD, which aligns autonomous driving with human cognitive principles through hierarchical perception and intent-conditioned trajectory generation. Similarly, Lu et al. (2025) proposed ReAL-AD, a three-tier framework based on human cognitive models (Driving Strategy, Driving Decision, Driving Operation) that integrates Vision-Language Models for hierarchical reasoning. These approaches share the insight that pure end-to-end mapping benefits from explicit reasoning layers that mirror human driver cognition, improving both performance and interpretability. The convergence on hierarchical structures suggests the field is recognizing limitations of flat perception-action models in handling complex, long-tail scenarios.

### Theme 2: Multi-Sensor Fusion and Representation Learning

Effective integration of multi-modal sensor data remains a central challenge, with recent work exploring novel representation schemes. Liu et al. (2025) introduced GaussianFusion, which uses 2D Gaussian representations as intermediate carriers to aggregate multi-sensor information, addressing interpretability and computational overhead limitations of traditional fusion approaches. The Gaussian-based representation provides an intuitive and compact approach, with explicit features capturing semantic and spatial information while implicit features provide complementary planning cues. This theme reflects a broader recognition that how sensor data is represented and fused fundamentally impacts downstream planning performance.

### Theme 3: Map and Infrastructure-Assisted Planning

Leveraging external map information and infrastructure-based sensors has emerged as a powerful strategy for improving trajectory planning. Yin et al. (2025) proposed MAP (Map-Assisted Planning), which explicitly integrates segmentation-based map features and ego status through a Plan-enhancing Online Mapping module, achieving a 16.6% reduction in L2 displacement error. Xing et al. (2025) explored RS2AD, which reconstructs vehicle-mounted LiDAR data from roadside sensor observations, reducing dependence on costly vehicle-mounted data collection while improving dataset diversity. These approaches demonstrate that end-to-end systems benefit significantly from incorporating structured external information rather than relying solely on onboard perception.

### Theme 4: Knowledge-Driven and Diffusion-Based Policies

The integration of domain knowledge with generative modeling represents an emerging paradigm. Xu et al. (2025) presented KDP, a knowledge-driven diffusion policy combining generative diffusion modeling with sparse mixture-of-experts routing for adaptive, robust decision-making across diverse scenarios. The approach achieves consistently higher success rates with reduced collision risk through structured expert specialization. This theme reflects growing interest in combining the flexibility of generative models with the reliability of knowledge-based constraints, enabling both adaptability and interpretability.

### Theme 5: Safety Analysis and Risk Management

As end-to-end systems approach deployment, comprehensive safety frameworks have become critical. Kou et al. (2025) proposed UniSTPA, a Unified System Theoretic Process Analysis framework that extends safety analysis from the operational phase to the entire lifecycle including information gathering, data preparation, training, verification, and deployment. The framework uncovers multi-stage hazards including scene design defects, sensor fusion biases, and internal model flaws, enabling construction of safety monitoring and response mechanisms. This work represents a maturation of the field toward systematic safety engineering rather than ad-hoc validation.

### Theme 6: Data Scaling and Generalization

Understanding how data quantity and quality affect model performance has received significant attention. Zheng et al. (2024) conducted extensive analysis of data scaling laws for imitation learning-based end-to-end autonomous driving using approximately 4 million demonstrations from 23 scenario types. Their findings reveal that model performance exhibits a power-law relationship with data amount in open-loop evaluation but not in closed-loop evaluation, indicating that data distribution matters more than mere volume. Small increases in long-tailed data quantity can significantly improve performance for corresponding scenarios, highlighting the importance of strategic data collection.

### Theme 7: Causality and Interaction Modeling

Capturing causal relationships between the ego vehicle and surrounding agents has emerged as crucial for robust trajectory prediction. Moon et al. (2026) proposed CaAD, a Causality-aware end-to-end Autonomous Driving framework with ego-centric joint-causal modeling that learns causal dependencies between the ego vehicle and interaction-relevant agents. The framework addresses causal oversight that leads to inconsistent trajectory predictions in interaction-critical scenarios, achieving strong performance on Bench2Drive and NAVSIM benchmarks. This work reflects growing recognition that correlation-based approaches are insufficient for safety-critical interaction scenarios.

### Theme 8: System Maintenance and Compatibility

Practical deployment challenges around system updates and maintenance have been addressed through novel approaches. Li et al. (2026) formulated the model stitching problem for preserving policy compatibility under perception updates, demonstrating that lightweight latent-space alignment can maintain downstream driving behavior when perception modules are updated. Their approach reduces adaptation time from 22.18 hours to 0.91 hours compared to retraining, providing an efficient alternative for maintaining end-to-end systems. This theme addresses a previously underexplored aspect of real-world deployment: how to efficiently update components without full system retraining.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively demonstrate strong agreement on several points. First, hierarchical or structured approaches consistently outperform flat end-to-end mapping, with Wang et al. (2025), Lu et al. (2025), and Xu et al. (2025) all showing benefits of multi-level architectures. Second, incorporating external information—whether maps (Yin et al., 2025), infrastructure sensors (Xing et al., 2025), or causal models (Moon et al., 2026)—improves robustness and generalization. Third, all papers report strong benchmark performance, suggesting the field has matured to the point where novel architectures reliably achieve state-of-the-art results on standard benchmarks like Bench2Drive and NAVSIM.

**Disagreements**: The literature shows less direct disagreement, partly because papers focus on different aspects of the end-to-end driving problem. However, there is an implicit tension between approaches emphasizing data scaling (Zheng et al., 2024) versus those emphasizing architectural innovation (Wang et al., 2025; Lu et al., 2025). Zheng et al. (2024) find that data distribution matters more than volume in closed-loop evaluation, suggesting architectural changes alone may not suffice without appropriate data. Meanwhile, cognitive and reasoning-based approaches assume architectural sophistication is the primary bottleneck. This tension remains unresolved in the current literature.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, which may indicate insufficient self-critique or space constraints. Second, while safety is addressed by Kou et al. (2025), most papers focus on benchmark performance rather than comprehensive safety validation in real-world deployment scenarios. Third, the inconsistency between open-loop and closed-loop evaluation metrics (Zheng et al., 2024) suggests the field lacks reliable evaluation protocols that predict real-world performance. Fourth, computational efficiency and real-time constraints are rarely discussed despite their importance for deployment. Finally, the heavy reliance on simulation benchmarks (Bench2Drive, NAVSIM) raises questions about real-world generalization that remain inadequately addressed.

## Per-Paper Annotations

### Li et al. (2026)

**Research question**: Can policy compatibility in end-to-end autonomous driving systems be preserved through lightweight latent-space alignment when perception models are updated?
**Methodology**: The authors formulate the model stitching problem and test low-complexity model stitching methods including linear and convolutional stitchers for restoring compatibility between updated perception modules and frozen downstream policy modules.
**Key findings**:
- Stitching effectively preserves downstream driving behavior under diverse perception updates including changes in random initialization, sensor configuration, and training domain
- In the cross-domain setting from nuScenes to CARLA, convolutional stitching retains over 91% of the no-shift driving score
- Stitching reduces adaptation time from 22.18 hours to 0.91 hours compared to retraining or fine-tuning
- Model stitching provides an effective and computationally efficient alternative to retraining for maintaining end-to-end autonomous driving systems
**Limitations**: not stated in abstract

### Liu et al. (2025)

**Research question**: How can multi-sensor fusion be improved for end-to-end autonomous driving to address limitations in interpretability and computational overhead?
**Methodology**: The authors introduce GaussianFusion, a framework using 2D Gaussian representations as intermediate carriers to aggregate multi-sensor information, with explicit and implicit features refined through a cascade planning head, evaluated on NAVSIM and Bench2Drive benchmarks.
**Key findings**:
- Gaussian-based representation provides an intuitive and compact approach for multi-sensor fusion
- Explicit features capture rich semantic and spatial information about the traffic scene
- Implicit features provide complementary cues beneficial for trajectory planning
- The cascade planning head effectively exploits spatial and semantic information through iterative refinement
- The framework demonstrates effectiveness and robustness on NAVSIM and Bench2Drive benchmarks
**Limitations**: not stated in abstract

### Lu et al. (2025)

**Research question**: How can hierarchical reasoning processes similar to human drivers be incorporated into end-to-end autonomous driving systems?
**Methodology**: The authors propose ReAL-AD, a Reasoning-Augmented Learning framework based on a three-tier human cognitive model (Driving Strategy, Driving Decision, Driving Operation) incorporating Vision-Language Models, with a Strategic Reasoning Injector, Tactical Reasoning Integrator, and Hierarchical Trajectory Decoder.
**Key findings**:
- Integrating the ReAL-AD framework improves planning accuracy and safety by over 30%
- The Strategic Reasoning Injector formulates high-level driving strategies from VLM-generated insights about complex traffic contexts
- The Tactical Reasoning Integrator refines strategic intent into interpretable tactical choices such as lane changes, overtaking, and speed adjustments
- The Hierarchical Trajectory Decoder translates tactical decisions into precise control actions for smooth and human-like trajectory execution
- The framework makes end-to-end autonomous driving more interpretable and aligned with human-like hierarchical reasoning
**Limitations**: not stated in abstract

### Moon et al. (2026)

**Research question**: How can causal inter-dependencies between the ego vehicle and surrounding agents be captured to improve trajectory prediction in end-to-end autonomous driving?
**Methodology**: The authors propose CaAD, a Causality-aware end-to-end Autonomous Driving framework with an ego-centric joint-causal modeling module that learns causal dependencies between the ego vehicle and interaction-relevant agents, and a causality-aware policy alignment stage with joint-mode embeddings for closed-loop feedback.
**Key findings**:
- CaAD achieves a Driving Score of 87.53 on the Bench2Drive benchmark
- CaAD achieves a Success Rate of 71.81 on Bench2Drive
- CaAD achieves a PDMS of 91.1 on the NAVSIM benchmark
- The framework addresses causal oversight that leads to inconsistent trajectory predictions in interaction-critical scenarios
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can end-to-end autonomous driving be improved by aligning with human cognitive principles in perception and planning?
**Methodology**: The authors propose CogAD, a hierarchical cognition-based model with dual mechanisms: global-to-local context processing for perception and intent-conditioned multi-mode trajectory generation for planning, evaluated on nuScenes and Bench2Drive benchmarks.
**Key findings**:
- CogAD achieves state-of-the-art performance in end-to-end planning on nuScenes and Bench2Drive benchmarks
- The model demonstrates comprehensive environmental understanding through hierarchical perception
- Robust planning exploration is enabled by multi-level planning mechanisms
- Diverse yet reasonable multi-modal trajectory generation is facilitated by dual-level uncertainty modeling
- The approach shows particular superiority in long-tail scenarios and robust generalization to complex real-world conditions
**Limitations**: not stated in abstract

### Xing et al. (2025)

**Research question**: How can vehicle-mounted LiDAR data be reconstructed and synthesized from roadside sensor observations to reduce data acquisition costs and improve dataset diversity?
**Methodology**: The authors propose RS2AD, a framework that transforms roadside LiDAR point clouds into the vehicle-mounted LiDAR coordinate system using the target vehicle's relative pose, then synthesizes high-fidelity vehicle-mounted LiDAR data through virtual LiDAR modeling, point cloud classification, and resampling techniques.
**Key findings**:
- This is the first approach to reconstruct vehicle-mounted LiDAR data from roadside sensor inputs
- Incorporating RS2AD-generated data (RS2V-L dataset) as a supplement to KITTI significantly enhances 3D object detection accuracy
- The method greatly improves the efficiency of end-to-end autonomous driving data generation
- The framework reduces dependence on costly vehicle-mounted data collection while improving model robustness
**Limitations**: not stated in abstract

### Xu et al. (2025)

**Research question**: How can end-to-end autonomous driving achieve adaptive, robust, and interpretable decision-making across diverse scenarios?
**Methodology**: The authors present KDP, a knowledge-driven diffusion policy combining generative diffusion modeling with sparse mixture-of-experts routing to generate temporally coherent actions while enabling modular knowledge composition through specialized expert activation.
**Key findings**:
- KDP achieves consistently higher success rates compared to prevailing paradigms
- The method reduces collision risk and produces smoother control
- Sparse expert activation proves effective according to ablation studies
- Activation analyses reveal structured specialization and cross-scenario reuse of experts
- Diffusion with expert routing establishes a scalable and interpretable paradigm for knowledge-driven autonomous driving
**Limitations**: not stated in abstract

### Yin et al. (2025)

**Research question**: How can online mapping module information be better utilized to enhance trajectory planning in end-to-end autonomous driving?
**Methodology**: The authors propose MAP (Map-Assisted Planning), a framework that explicitly integrates segmentation-based map features and ego status through a Plan-enhancing Online Mapping module, Ego-status-guided Planning module, and Weight Adapter, evaluated on the DAIR-V2X-seq-SPD dataset.
**Key findings**:
- MAP achieves a 16.6% reduction in L2 displacement error compared to the UniV2X baseline
- The method reduces off-road rate by 56.2% without post-processing
- Overall score improved by 44.5% compared to the baseline
- The model achieved top ranking in Track 2 of the End-to-End Autonomous Driving through V2X Cooperation Challenge, outperforming the second-best model by 39.5%
- Explicitly leveraging semantic map features in planning proves effective for improving end-to-end autonomous driving systems
**Limitations**: not stated in abstract

### Zheng et al. (2024)

**Research question**: What are the scaling laws associated with imitation learning-based end-to-end autonomous driving when trained on large-scale real-world data?
**Methodology**: The authors collected approximately 4 million demonstrations from 23 scenario types (over 30,000 hours) and conducted extensive open-loop and closed-loop evaluations on 1,400 diverse driving demonstrations to study data scaling laws.
**Key findings**:
- Model performance exhibits a power-law relationship with data amount in open-loop evaluation, but not in closed-loop evaluation
- The inconsistency between open-loop and closed-loop assessments indicates data distribution matters more than mere volume expansion
- Small increases in long-tailed data quantity can significantly improve performance for corresponding scenarios
- Appropriate data scaling enables models to achieve combinatorial generalization in novel scenes and actions
- Data scaling plays a critical role in improving model generalizability across diverse autonomous driving scenarios
**Limitations**: not stated in abstract

### Kou et al. (2025)

**Research question**: How can safety risks in end-to-end autonomous driving systems be comprehensively identified across the entire development and deployment lifecycle?
**Methodology**: The authors propose the Unified System Theoretic Process Analysis (UniSTPA) framework, which extends STPA from the operational phase to the entire lifecycle including information gathering, data preparation, closed loop training, verification, and deployment, with hazard analysis at both component level and within model internal layers.
**Key findings**:
- UniSTPA uncovers multi-stage hazards overlooked by conventional approaches, including scene design defects, sensor fusion biases, and internal model flaws
- The framework traces hazards to deeper issues such as data quality, network architecture, and optimisation objectives through multi-level causal analysis
- UniSTPA enables construction of safety monitoring and safety response mechanisms supporting continuous improvement from hazard identification to system optimisation
- The framework provides both theoretical and practical guidance for safe development and deployment of end-to-end autonomous driving systems
**Limitations**: not stated in abstract

## References

Kou, H., Lyu, Z., Wang, Z., Wang, C., & Zhang, Y. (2025). UniSTPA: A safety analysis framework for end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2505.15005

Li, Y., Xiao, Y., Jiang, M., Zuo, X., Zhang, S., & Yang, M. (2026). A stitch in time saves nine: Preserving policy compatibility under perception updates in end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2606.21509

Liu, S., Liang, Q., Li, Z., Li, B., & Huang, K. (2025). GaussianFusion: Gaussian-based multi-sensor fusion for end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2506.00034

Lu, Y., Tu, J., Ma, Y., & Zhu, X. (2025). ReAL-AD: Towards human-like reasoning in end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2507.12499

Moon, S., Lee, M., Seo, J., Kim, J., & Lee, J. (2026). Causality-aware end-to-end autonomous driving via ego-centric joint scene modeling. arXiv. https://arxiv.org/abs/2605.13646

Wang, Z., Teng, J., Xiang, C., Chen, K., Pan, X., Deng, L., & Gu, W. (2025). CogAD: Cognitive-hierarchy guided end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2505.21581

Xing, R., Huang, R., Xu, Q., & He, L. (2025). RS2AD: End-to-end autonomous driving data generation from roadside sensor observations. arXiv. https://arxiv.org/abs/2503.07085

Xu, C., Liu, J., Guo, Y., Hang, P., & Sun, J. (2025). A knowledge-driven diffusion policy for end-to-end autonomous driving based on expert routing. arXiv. https://arxiv.org/abs/2509.04853

Yin, H., Kan, Y., & Watzenig, D. (2025). MAP: End-to-end autonomous driving with map-assisted planning. arXiv. https://arxiv.org/abs/2509.13926

Zheng, Y., Yang, P., Xia, Z., Zhang, Q., Zheng, Y., Gu, S., Jin, B., Zhang, T., Lu, B., Han, C., Lang, X., & Zhao, D. (2024). Data scaling laws for imitation learning-based end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2412.02689
