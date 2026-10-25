# Systematic Literature Review: End-to-End Autonomous Driving

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "end-to-end autonomous driving", filtered to category cs.RO, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on end-to-end autonomous driving in the robotics category (cs.RO) from the past two years. The surveyed literature reveals a field rapidly evolving along multiple dimensions: cognitive and human-like reasoning architectures, multi-sensor fusion strategies, safety analysis frameworks, data scaling methodologies, and novel neural computing paradigms. Collectively, these papers demonstrate a shift from purely data-driven approaches toward systems that incorporate structured reasoning, causal understanding, and interpretability. Several works address the critical challenge of generalization to long-tail scenarios through hierarchical cognition, knowledge-driven policies, and map-assisted planning. The field also shows growing attention to practical deployment concerns, including computational efficiency (spike-driven neural networks), safety throughout the development lifecycle, and cost-effective data generation from infrastructure-based sensors.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "end-to-end autonomous driving", filtered to category cs.RO, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Human-Like Cognitive Architectures

A prominent direction in recent end-to-end autonomous driving research involves mimicking human cognitive processes to achieve more robust and interpretable decision-making. Wang et al. (2025) proposed CogAD, which implements a hierarchical cognition model with global-to-local context processing for perception and intent-conditioned multi-mode trajectory generation for planning. Similarly, Lu et al. (2025) introduced ReAL-AD, based on a three-tier human cognitive model (Driving Strategy, Driving Decision, and Driving Operation) that uses Vision-Language Models to capture hierarchical reasoning. Both approaches share the insight that human drivers naturally employ multi-level reasoning, from high-level strategic thinking to low-level operational control. These cognitive architectures aim to address the brittleness of purely end-to-end neural networks in long-tail scenarios by incorporating structured reasoning processes that mirror human driving behavior.

### Theme 2: Causal and Knowledge-Driven Reasoning

Beyond mimicking human cognition structure, several works explicitly incorporate causal reasoning and knowledge-driven approaches to improve robustness and interpretability. Moon et al. (2026) developed CaAD, which captures causal inter-dependencies between the ego vehicle and surrounding agents through ego-centric joint scene modeling, addressing causal oversight that leads to inconsistent trajectory predictions in interaction-critical scenarios. Xu et al. (2025) presented KDP, a knowledge-driven diffusion policy that integrates generative diffusion modeling with sparse mixture-of-experts routing, where specialized experts are activated according to context. These approaches recognize that correlation-based learning alone is insufficient for safe autonomous driving; understanding causal relationships and leveraging structured knowledge enables more reliable decision-making in complex multi-agent interactions.

### Theme 3: Multi-Sensor Fusion and Map Integration

Effective perception and planning in autonomous driving requires integrating information from multiple sensors and map sources. Liu et al. (2025) introduced GaussianFusion, which employs 2D Gaussian representations as intermediate carriers to aggregate information from diverse sensors, providing intuitive and compact multi-sensor fusion with reduced computational overhead. Yin et al. (2025) proposed MAP, which explicitly integrates segmentation-based map features and ego status through a Plan-enhancing Online Mapping module, achieving a 16.6% reduction in L2 displacement error compared to baseline. Both approaches demonstrate that thoughtful architectural design for sensor and map integration—rather than naive concatenation of features—significantly improves planning performance and reduces off-road driving.

### Theme 4: Data Scaling and Generation Strategies

The role of data in end-to-end autonomous driving has received substantial attention, with multiple papers examining how to efficiently collect, scale, and generate training data. Zheng et al. (2024) conducted an extensive study of data scaling laws using approximately 4 million demonstrations from 23 different scenario types (over 30,000 hours of driving), finding that model performance exhibits a power-law relationship with data amount in open-loop evaluation but not in closed-loop evaluation, indicating that data distribution matters more than mere volume. Xing et al. (2025) introduced RS2AD, the first approach to reconstruct vehicle-mounted LiDAR data from roadside sensor observations, reducing dependence on costly vehicle-mounted data collection while improving model generalization. These works collectively suggest that smart data strategies—focusing on distribution quality, long-tail scenario coverage, and infrastructure-based data generation—are more important than raw data volume alone.

### Theme 5: Safety Analysis and Verification

As end-to-end autonomous driving systems move toward deployment, ensuring safety throughout the development lifecycle has become critical. Kou et al. (2025) proposed UniSTPA, which extends System Theoretic Process Analysis (STPA) from the operational phase to the entire lifecycle of end-to-end autonomous driving systems, performing hazard analysis at both component level and within the model's internal layers through multi-level causal analysis. This framework uncovers multi-stage hazards overlooked by conventional approaches, including scene design defects, sensor fusion biases, and internal model flaws. The growing attention to safety analysis frameworks reflects the field's maturation from purely performance-driven research toward systems that can be rigorously verified and validated for real-world deployment.

### Theme 6: Energy-Efficient Neural Computing

Addressing the computational and energy efficiency of autonomous driving systems, Zhang et al. (2026) presented SDPAD, a fully spike-driven end-to-end planning pipeline that converts pre-trained ANN perception stacks into integer-spike form via quantized ANN2SNN conversion. SDPAD achieves planning accuracy comparable to strong ANN planners (average L2 error of 0.40m, collision rate of 0.12% on nuScenes) while consuming only 69.9mJ—less than 2% of recent ANN baselines. This work demonstrates that spiking neural networks can achieve competitive performance in end-to-end autonomous driving while offering orders-of-magnitude improvements in energy efficiency, opening new possibilities for deployment on resource-constrained platforms.

## Convergences and Disagreements

**Convergences**: Multiple surveyed papers converge on the importance of structured reasoning and interpretability in end-to-end autonomous driving. Wang et al. (2025), Lu et al. (2025), Moon et al. (2026), and Xu et al. (2025) all emphasize that purely black-box neural networks are insufficient for safe, robust autonomous driving; instead, systems should incorporate hierarchical reasoning, causal understanding, or knowledge-driven mechanisms. Additionally, several papers agree that generalization to long-tail scenarios remains a critical challenge, addressed through diverse strategies including cognitive hierarchies, expert routing, and targeted data scaling (Zheng et al., 2024; Wang et al., 2025).

**Disagreements**: The surveyed literature does not show fundamental disagreements, as papers focus on different aspects of the problem. However, there is an implicit tension between approaches that emphasize large-scale data collection and scaling (Zheng et al., 2024) versus those that prioritize architectural innovations for reasoning and efficiency (Zhang et al., 2026; Moon et al., 2026). The field has not yet resolved whether performance gains will come primarily from more data or from better architectures—likely both are necessary.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Closed-loop evaluation inconsistency**: Zheng et al. (2024) found that data scaling laws differ between open-loop and closed-loop evaluation, suggesting that current evaluation protocols may not accurately predict real-world performance. More standardized closed-loop benchmarks are needed.

2. **Limited limitation reporting**: None of the surveyed papers explicitly discussed limitations in their abstracts, making it difficult to assess the boundaries of each approach's applicability.

3. **Integration challenges**: While individual papers propose cognitive architectures, causal reasoning, multi-sensor fusion, and safety analysis, no surveyed work integrates all these dimensions into a unified system. How to combine these complementary approaches remains open.

4. **Real-world deployment evidence**: Most papers report results on simulation benchmarks (nuScenes, Bench2Drive, NAVSIM); evidence from real-world deployment is limited, particularly for novel architectures like spike-driven networks.

5. **Computational efficiency trade-offs**: Except for SDPAD (Zhang et al., 2026), most papers do not report computational costs or energy consumption, making it difficult to assess practical deployment feasibility.

## Per-Paper Annotations

### Moon et al. (2026)

**Research question**: How can causal inter-dependencies between the ego vehicle and surrounding agents be captured to improve trajectory prediction in end-to-end autonomous driving?

**Methodology**: The authors propose CaAD, a Causality-aware end-to-end Autonomous Driving framework with two components: an ego-centric joint-causal modeling module that learns causal dependencies between the ego vehicle and interaction-relevant agents, and a causality-aware policy alignment stage with joint-mode embeddings to align the stochastic ego policy with planning-oriented closed-loop feedback.

**Key findings**:
- CaAD achieves a Driving Score of 87.53 and Success Rate of 71.81 on the Bench2Drive benchmark
- CaAD achieves a PDMS of 91.1 on the NAVSIM benchmark
- The framework addresses causal oversight that leads to inconsistent and unreliable trajectory predictions in interaction-critical scenarios
- The ego-centric joint-causal modeling module builds on the marginal prediction branch to learn causal dependencies

**Limitations**: not stated in abstract

### Kou et al. (2025)

**Research question**: How can safety risks in end-to-end autonomous driving systems be comprehensively identified and analyzed throughout the entire development lifecycle?

**Methodology**: The authors propose the Unified System Theoretic Process Analysis (UniSTPA) framework, which extends STPA from the operational phase to the entire lifecycle of end-to-end autonomous driving systems, performing hazard analysis at both component level and within the model's internal layers through multi-level causal analysis.

**Key findings**:
- UniSTPA uncovers multi-stage hazards overlooked by conventional approaches, including scene design defects, sensor fusion biases, and internal model flaws
- The framework traces hazards to deeper issues such as data quality, network architecture, and optimisation objectives
- The analysis results are used to construct a safety monitoring and safety response mechanism supporting continuous improvement from hazard identification to system optimisation
- UniSTPA enables fine-grained assessment of inter and intra module interactions within the model's internal layers

**Limitations**: not stated in abstract

### Lu et al. (2025)

**Research question**: How can end-to-end autonomous driving systems capture the hierarchical reasoning process that human drivers naturally employ?

**Methodology**: The authors propose ReAL-AD, a Reasoning-Augmented Learning framework based on the three-tier human cognitive model (Driving Strategy, Driving Decision, and Driving Operation), incorporating Vision-Language Models with three components: Strategic Reasoning Injector, Tactical Reasoning Integrator, and Hierarchical Trajectory Decoder.

**Key findings**:
- Integrating the ReAL-AD framework improves planning accuracy and safety by over 30%
- The Strategic Reasoning Injector formulates high-level driving strategies by interpreting complex traffic contexts from VLM-generated insights
- The Tactical Reasoning Integrator refines strategic intent into interpretable tactical choices such as lane changes, overtaking, and speed adjustments
- The Hierarchical Trajectory Decoder progressively translates tactical decisions into precise control actions for smooth and human-like trajectory execution
- The framework makes end-to-end autonomous driving more interpretable and aligned with human-like hierarchical reasoning

**Limitations**: not stated in abstract

### Xing et al. (2025)

**Research question**: How can vehicle-mounted LiDAR data be reconstructed and synthesized from roadside sensor observations to reduce data acquisition costs and improve model generalization in autonomous driving?

**Methodology**: The authors introduce RS2AD, a framework that transforms roadside LiDAR point clouds into the vehicle-mounted LiDAR coordinate system by leveraging the target vehicle's relative pose, then synthesizes high-fidelity vehicle-mounted LiDAR data through virtual LiDAR modeling, point cloud classification, and resampling techniques.

**Key findings**:
- This is the first approach to reconstruct vehicle-mounted LiDAR data from roadside sensor inputs
- Incorporating RS2AD-generated data (RS2V-L dataset) as a supplement to the KITTI dataset significantly enhances the accuracy of 3D object detection
- The method greatly improves the efficiency of end-to-end autonomous driving data generation
- The approach reduces dependence on costly vehicle-mounted data collection while improving the robustness of autonomous driving models

**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can end-to-end autonomous driving be better aligned with human cognitive principles in perception and planning?

**Methodology**: The authors propose CogAD, a hierarchical cognition model implementing global-to-local context processing for perception and intent-conditioned multi-mode trajectory generation for planning, with dual-level uncertainty modeling.

**Key findings**:
- CogAD achieves state-of-the-art performance in end-to-end planning on nuScenes and Bench2Drive benchmarks
- The model demonstrates comprehensive environmental understanding through hierarchical perception
- Multi-level planning enables robust planning exploration
- Dual-level uncertainty modeling facilitates diverse yet reasonable multi-modal trajectory generation
- The approach shows particular superiority in long-tail scenarios and robust generalization to complex real-world driving conditions

**Limitations**: not stated in abstract

### Zhang et al. (2026)

**Research question**: Can spiking neural networks achieve planning accuracy comparable to artificial neural networks in end-to-end autonomous driving while consuming significantly less energy?

**Methodology**: The authors present SDPAD, a fully spike-driven end-to-end planning pipeline that converts a pre-trained ANN perception stack into integer-spike form via quantized ANN2SNN conversion, lifts multi-view images into BEV space with spike-driven-max depth distribution, and plans through Spike-QFormer with ego, agent, and map queries fused by learnable waypoint queries via cross-attention.

**Key findings**:
- SDPAD achieves an average L2 error of 0.40m and a collision rate of 0.12% on the nuScenes open-loop benchmark, on par with strong ANN planners
- SDPAD consumes 69.9mJ, less than 2% of recent ANN baselines
- In closed-loop evaluation on NAVSIM navtest split, SDPAD reaches 86.3 PDMS, surpassing the previous SNN planner SAD by 4.3 points and matching mainstream ANN planners
- SDPAD is the first fully spike-driven planner evaluated in end-to-end autonomous driving
- Every operation is gated by integer spikes with inference as a single feed-forward pass without temporal simulation loops

**Limitations**: not stated in abstract

### Xu et al. (2025)

**Research question**: How can end-to-end autonomous driving achieve adaptive, robust, and interpretable decision-making across diverse scenarios?

**Methodology**: The authors present KDP, a knowledge-driven diffusion policy that integrates generative diffusion modeling with a sparse mixture-of-experts routing mechanism, where the diffusion component generates temporally coherent action sequences and expert routing activates specialized experts according to context.

**Key findings**:
- KDP achieves consistently higher success rates compared to prevailing paradigms across representative driving scenarios
- The method reduces collision risk and produces smoother control
- Sparse expert activation and the Transformer backbone are effective according to ablation studies
- Activation analyses reveal structured specialization and cross-scenario reuse of experts
- Diffusion with expert routing establishes a scalable and interpretable paradigm for knowledge-driven end-to-end autonomous driving

**Limitations**: not stated in abstract

### Liu et al. (2025)

**Research question**: How can multi-sensor fusion be improved for end-to-end autonomous driving with better interpretability and reduced computational overhead?

**Methodology**: The authors introduce GaussianFusion, a Gaussian-based multi-sensor fusion framework that employs 2D Gaussian representations as intermediate carriers to aggregate information from diverse sensors, with explicit and implicit features refined through multi-modal integration and a cascade planning head for trajectory prediction.

**Key findings**:
- Gaussian representations provide intuitive and compact intermediate carriers for multi-sensor information aggregation
- Explicit features capture rich semantic and spatial information about the traffic scene
- Implicit features provide complementary cues beneficial for trajectory planning
- The cascade planning head effectively exploits spatial and semantic information in Gaussians through iterative trajectory refinement
- The framework demonstrates effectiveness and robustness on NAVSIM and Bench2Drive benchmarks

**Limitations**: not stated in abstract

### Yin et al. (2025)

**Research question**: How can online mapping modules be better utilized to enhance trajectory planning in end-to-end autonomous driving?

**Methodology**: The authors propose MAP (Map-Assisted Planning), a framework that explicitly integrates segmentation-based map features and ego status through a Plan-enhancing Online Mapping module, Ego-status-guided Planning module, and Weight Adapter.

**Key findings**:
- MAP achieves a 16.6% reduction in L2 displacement error compared to the UniV2X baseline
- The method reduces off-road rate by 56.2%
- Overall score improves by 44.5% compared to baseline, even without post-processing
- The approach achieved top ranking in Track 2 of the End-to-End Autonomous Driving through V2X Cooperation Challenge at CVPR2025 MEIS Workshop, outperforming the second-best model by 39.5%
- Explicitly leveraging semantic map features in planning suggests new directions for improving structure design in end-to-end autonomous driving systems

**Limitations**: not stated in abstract

### Zheng et al. (2024)

**Research question**: What are the scaling laws associated with end-to-end autonomous driving when using imitation learning with large-scale real-world data?

**Methodology**: The authors collected approximately 4 million demonstrations from 23 different scenario types (over 30,000 hours of driving) and conducted extensive open-loop and closed-loop evaluations on 1,400 diverse driving demonstrations to study scaling laws.

**Key findings**:
- Model performance exhibits a power-law relationship with data amount in open-loop evaluation, but not in closed-loop evaluation
- The inconsistency between open-loop and closed-loop assessments indicates that data distribution matters more than mere volume expansion
- Small increases in long-tailed data quantities can significantly improve performance for corresponding scenarios
- Appropriate data scaling enables models to achieve combinatorial generalization in novel scenes and actions
- Data scaling plays a critical role in improving model generalizability across diverse autonomous driving scenarios

**Limitations**: not stated in abstract

## References

Kou, H., Lyu, Z., Wang, Z., Wang, C., & Zhang, Y. (2025). UniSTPA: A safety analysis framework for end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2505.15005

Liu, S., Liang, Q., Li, Z., Li, B., & Huang, K. (2025). GaussianFusion: Gaussian-based multi-sensor fusion for end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2506.00034

Lu, Y., Tu, J., Ma, Y., & Zhu, X. (2025). ReAL-AD: Towards human-like reasoning in end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2507.12499

Moon, S., Lee, M., Seo, J., Kim, J., & Lee, J. (2026). Causality-aware end-to-end autonomous driving via ego-centric joint scene modeling. arXiv. https://arxiv.org/abs/2605.13646

Wang, Z., Teng, J., Xiang, C., Chen, K., Pan, X., Deng, L., & Gu, W. (2025). CogAD: Cognitive-hierarchy guided end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2505.21581

Xing, R., Huang, R., Xu, Q., & He, L. (2025). RS2AD: End-to-end autonomous driving data generation from roadside sensor observations. arXiv. https://arxiv.org/abs/2503.07085

Xu, C., Liu, J., Guo, Y., Hang, P., & Sun, J. (2025). A knowledge-driven diffusion policy for end-to-end autonomous driving based on expert routing. arXiv. https://arxiv.org/abs/2509.04853

Yin, H., Kan, Y., & Watzenig, D. (2025). MAP: End-to-end autonomous driving with map-assisted planning. arXiv. https://arxiv.org/abs/2509.13926

Zhang, C., Zhang, Y., Yang, J., & Sawan, M. (2026). SDPAD: A fully spike-driven pipeline for end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2610.11583

Zheng, Y., Yang, P., Xia, Z., Zhang, Q., Zheng, Y., Gu, S., Jin, B., Zhang, T., Lu, B., Han, C., Lang, X., & Zhao, D. (2024). Data scaling laws for imitation learning-based end-to-end autonomous driving. arXiv. https://arxiv.org/abs/2412.02689
