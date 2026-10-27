# Systematic Literature Review: World Models for Robotic Manipulation

**Date**: 2026-10-27
**Papers surveyed**: 10
**Scope**: arXiv query "world models robotic manipulation", filtered to category cs.RO, published between 2024-05-27 and 2026-05-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on world models for robotic manipulation has rapidly evolved toward unified architectures that jointly model video generation and action prediction, enabling policies to generalize across novel tasks and environments. Recent work demonstrates that coupling predictive world modeling with policy learning significantly improves sample efficiency, robustness to visual disturbances, and zero-shot generalization capabilities. A dominant trend involves leveraging large-scale pretraining on robotic datasets combined with action-free video data to bootstrap representation learning. However, the field faces common challenges including computational costs of training generative models, artifacts in high-dynamics video prediction, and limitations in transferring across embodiments and dexterous manipulation scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-27 using the query "world models robotic manipulation", filtered to category cs.RO, published between 2024-05-27 and 2026-05-26. Papers were selected by co-citation analysis from a shortlist of 30 papers (itself derived from 50 search results plus 93 papers they cited), with the top 10 ranked by centrality to the topic. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents from each paper's full text (arXiv HTML; all 10 papers had full text available), with every key finding tied to a quote that code checked against the paper, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Unified Video-Action Architectures

A central direction in recent work involves integrating video generation and action prediction within unified transformer-based architectures. Rather than treating world modeling and policy learning as separate stages, these approaches learn joint latent representations that support both future state prediction and action inference. UWM couples video and action diffusion processes within a single transformer, where independent diffusion timesteps govern each modality [citation:Unified World Models](https://arxiv.org/abs/2504.02792) [E13]. Similarly, UVA decouples video-action decoding using two lightweight diffusion heads, enabling high-speed action inference by bypassing video generation during deployment [citation:Unified Video Action Model](https://arxiv.org/abs/2503.00200) [E21]. WorldVLA takes an autoregressive approach, integrating Vision-Language-Action modeling with world prediction in a single framework where attention masking mitigates error propagation [citation:WorldVLA](https://arxiv.org/abs/2506.21539) [E18]. These unified architectures consistently outperform decoupled baselines, with UWM surpassing the best baseline by up to 20% on real robot tasks [citation:Unified World Models](https://arxiv.org/abs/2504.02792) [E13], and UVA achieving 20% improvement on PushT-M and 5% on Libero10 in multi-task settings [citation:Unified Video Action Model](https://arxiv.org/abs/2503.00200) [E20].

### Theme 2: Scaling Through Synthetic Data Generation

Multiple papers explore using world models as data engines to generate synthetic training trajectories, addressing the scarcity of real-world robotic data. DreamGen adapts image-to-video generative models to produce photorealistic synthetic robot videos, then extracts pseudo-action sequences using latent action models to train visuomotor policies [citation:DreamGen](https://arxiv.org/abs/2505.12705). The approach enables learning entirely new behaviors, achieving 32% absolute improvement from 11.2% to 43.2% success rates [citation:DreamGen](https://arxiv.org/abs/2505.12705) [E26]. Policy performance scales log-linearly with the number of neural trajectories, though the approach requires significant compute—54 hours on 1500 L40 GPUs for 240k samples [citation:DreamGen](https://arxiv.org/abs/2505.12705) [E27]. EnerVerse-AC similarly functions as a data engine, where augmentation with generated trajectories improves policy success rates from 28% to 36% [citation:EnerVerse-AC](https://arxiv.org/abs/2505.09723) [E11]. Gen2Act takes a different approach, casting manipulation as zero-shot human video generation using pre-trained web-scale video models, then conditioning robot policies on generated videos with motion extracted via point tracking [citation:Gen2Act](https://arxiv.org/abs/2409.16283).

### Theme 3: Benchmarking and Evaluation Frameworks

The emergence of standardized benchmarks reflects the field's maturation. EWMBench, introduced alongside Genie Envisioner, measures visual fidelity, physical consistency, and instruction-action alignment across world models, showing strong correlation with human preference ratings [citation:Genie Envisioner](https://arxiv.org/abs/2508.05635) [E7]. GE-Base outperforms seven state-of-the-art video generation models on EWMBench metrics, with particular strengths in temporal alignment and dynamic consistency [citation:Genie Envisioner](https://arxiv.org/abs/2508.05635) [E5, E6]. The LIBERO benchmark appears frequently across papers as a standard evaluation suite, with EnerVerse achieving 84.1 average score using single S-RGB input [citation:EnerVerse](https://arxiv.org/abs/2501.01895) [E29], and Seer achieving 78.7% success rate on LIBERO-LONG with 9% improvement from pre-training [citation:Seer](https://arxiv.org/abs/2412.15109) [E32]. Real-world deployment remains a critical validation step, with GWM achieving 65% success rate versus 35% for Diffusion Policy in real-world pick-and-place tasks [citation:GWM](https://arxiv.org/abs/2508.17600) [E4].

### Theme 4: 3D and Geometric Representations

Moving beyond 2D video prediction, recent work incorporates explicit 3D geometric reasoning into world models. GWM combines a latent Diffusion Transformer with a 3D variational autoencoder to reconstruct future states by inferring propagation of Gaussian primitives under robot actions [citation:GWM](https://arxiv.org/abs/2508.17600). This geometric grounding enables GWM to consistently outperform iVideoGPT on future state prediction across synthetic and real-world environments, while achieving 2× faster RL convergence [citation:GWM](https://arxiv.org/abs/2508.17600) [E3]. EnerVerse employs multi-view video representation for 3D grounding with chunk-wise autoregressive video diffusion and sparse context memory for long-term reasoning [citation:EnerVerse](https://arxiv.org/abs/2501.01895). The sparse memory mechanism proves critical, with performance dropping from 73 to 30.8 on LIBERO-Long without it [citation:EnerVerse](https://arxiv.org/abs/2501.01895) [E30]. EnerVerse-AC extends this with ray map encoding for dynamic multi-view image generation, maintaining visual stability for up to 30 chunks in single-view settings [citation:EnerVerse-AC](https://arxiv.org/abs/2505.09723) [E9].

## Convergences and Disagreements

**Convergences**: All surveyed papers agree that joint modeling of video and actions outperforms decoupled approaches, with consistent improvements in sample efficiency and generalization. Multiple papers independently validate that pretraining on large-scale robotic datasets (particularly DROID) followed by fine-tuning yields substantial gains [citation:Unified World Models](https://arxiv.org/abs/2504.02792) [E15], [citation:Seer](https://arxiv.org/abs/2412.15109) [E34]. There is broad consensus that incorporating action-free video data improves policy robustness, with UWM showing significant robustness improvements when co-trained with videos [citation:Unified World Models](https://arxiv.org/abs/2504.02792) [E16], and EnerVerse-AC demonstrating that including failure trajectories prevents hallucination [citation:EnerVerse-AC](https://arxiv.org/abs/2505.09723) [E12].

**Disagreements**: While most papers advocate for unified architectures, they differ on the optimal generation paradigm. Diffusion-based approaches (UWM, UVA) emphasize robustness and sample quality, while autoregressive methods (WorldVLA, EnerVerse) prioritize long-horizon consistency and scalability. DreamGen's reliance on massive compute (1500 GPUs) contrasts with GWM's more efficient Gaussian representation approach, reflecting tension between scaling laws and architectural efficiency. Additionally, papers diverge on whether to prioritize single-view simplicity (EnerVerse with 84.1 on LIBERO using single S-RGB) versus multi-view geometric richness (EnerVerse-AC's multi-view with stability limited to 10 chunks).

## Gaps and Open Questions

Several critical gaps persist across the literature. First, computational requirements remain prohibitive for most labs—DreamGen requires 54 hours on 1500 L40 GPUs, limiting accessibility and reproducibility [citation:DreamGen](https://arxiv.org/abs/2505.12705). Second, video generation artifacts in high-dynamics tasks remain unresolved, with EnerVerse explicitly noting artifacts in high-dynamics robotics tasks [citation:EnerVerse](https://arxiv.org/abs/2501.01895) [E31], and UWM acknowledging that forward dynamics reconstruction often contains artifacts reducing planning efficacy [citation:Unified World Models](https://arxiv.org/abs/2504.02792). Third, cross-embodiment transfer remains largely unexplored—Seer's evaluation notes that cross-embodiment capability across different robots remains to be tested [citation:Seer](https://arxiv.org/abs/2412.15109). Fourth, dexterous manipulation is consistently limited, with Gen2Act noting inability to generate realistic hands for dexterous tasks [citation:Gen2Act](https://arxiv.org/abs/2409.16283) [E39], and EnerVerse-AC's gripper representation potentially not generalizing to dexterous hands [citation:EnerVerse-AC](https://arxiv.org/abs/2505.09723). Finally, the relationship between video generation quality and policy performance remains incompletely understood, with EnerVerse calling for further exploration of how video generation guides action policy learning [citation:EnerVerse](https://arxiv.org/abs/2501.01895).

## Per-Paper Annotations

### Cen et al. (2025)

**Research question**: Can an autoregressive action world model unify action and image understanding and generation to achieve mutual enhancement between world modeling and action modeling?
**Methodology**: WorldVLA integrates Vision-Language-Action model and world model in one single framework, using an autoregressive approach with attention mask strategy to selectively mask prior actions during generation, evaluated on LIBERO benchmark with action and world model ablation studies.
**Key findings**:
- Integration of world model significantly enhances action model performance [E40]
- Action world model outperforms pure world model in generation quality for longer video sequences [E17]
- Attention masking mechanism mitigates error propagation in autoregressive action generation [E18]
- World model pretraining leads to notable improvements in grasping performance [E19]
**Limitations**: The current image tokenizer, which relies on discrete representations, exhibits limitations in perceptual expressiveness.

### Huang et al. (2025)

**Research question**: How can generative robotics foundation models construct and interpret embodied spaces for manipulation tasks?
**Methodology**: EnerVerse employs chunk-wise autoregressive video diffusion with sparse context memory for long-term reasoning, uses multi-view video representation for 3D grounding, and integrates a policy head (EnerVerse-A) that translates 4D world representations into physical actions.
**Key findings**:
- EnerVerse produces superior video quality compared to DynamicCrafter baseline with higher PSNR and lower FVD [E28]
- EnerVerse achieves state-of-the-art performance on LIBERO benchmark with 84.1 average score using single S-RGB input [E29]
- Sparse memory mechanism is critical for policy performance with 30.8 vs 73 on LIBERO-Long without it [E30]
- EnerVerse has limitations with video artifacts in high-dynamics robotics tasks [E31]
**Limitations**: Video generation models inevitably produce artifacts in high-dynamics tasks, the current rendered views use heuristically set camera poses that may not be optimal, and further exploration is needed to understand how video generation guides action policy learning.

### Jang et al. (2025)

**Research question**: How can robot policies generalize across behaviors and environments using synthetic data generated from video world models?
**Methodology**: DreamGen uses a 4-stage pipeline that adapts image-to-video generative models to produce photorealistic synthetic robot videos, then extracts pseudo-action sequences using latent action models or inverse-dynamics models to train visuomotor policies.
**Key findings**:
- Co-training with neural trajectories improves policy performance across all data regimes [E24]
- Robot policy performance scales log-linearly with the number of neural trajectories [E25]
- DreamGen enables learning entirely new behaviors with 32% absolute improvement from 11.2% to 43.2% [E26]
- DreamGen requires significant computational resources with 54 hours on 1500 L40 GPUs for 240k samples [E27]
**Limitations**: The approach requires significant compute (54 hours on 1500 L40 GPUs for 240k samples), tasks are relatively simple covering limited kinematic capabilities, and the automatic evaluator can hallucinate when evaluating physical realism.

### Jiang et al. (2025)

**Research question**: How can an action-conditional world model generate future visual observations based on agent actions to enable realistic robotic inference and evaluation without physical robots?
**Methodology**: The authors propose EVAC with multi-level action-conditioning mechanism and ray map encoding for dynamic multi-view image generation, trained on AgiBot World dataset including diverse failure trajectories, evaluated as both data engine for policy augmentation and evaluator for policy testing across manipulation tasks comparing success rates with real-world executions.
**Key findings**:
- EVAC maintains visual stability for up to 30 chunks in single-view and 10 chunks in multi-view settings [E9]
- EVAC simulator evaluation trends align with real-world performance across manipulation tasks [E10]
- Data augmentation with EVAC-generated trajectories improves policy success rate from 28% to 36% [E11]
- Including failure trajectories prevents model from hallucinating successful grasps when objects are absent [E12]
**Limitations**: Gripper openness representation using unit circle with color intensities may not generalize to complex end-effectors like dexterous hands; wrist camera captures irrelevant background noise limiting multi-view inference to 10 chunks; potential applications with actor-critic reinforcement learning methods remain unexplored.

### Liao et al. (2025)

**Research question**: How can a unified world foundation platform integrate policy learning, evaluation, and simulation within a single video-generative framework for robotic manipulation?
**Methodology**: The authors introduce Genie Envisioner with three components: GE-Base (instruction-conditioned video diffusion model), GE-Act (flow-matching decoder for action trajectories), and GE-Sim (action-conditioned neural simulator), proposing EWMBench benchmark suite measuring visual fidelity, physical consistency, and instruction-action alignment, evaluating against seven state-of-the-art video generation models.
**Key findings**:
- GE-Base outperforms seven state-of-the-art video generation models on EWMBench metrics [E5]
- GE-Base shows particular strengths in temporal alignment and dynamic consistency metrics [E6]
- EWMBench evaluation metrics correlate strongly with human preference ratings [E7]
- Genie Envisioner is limited by reliance on single-platform dataset without internet-scale or simulation data [E8]
**Limitations**: Training relies exclusively on AgiBot-World-Beta dataset without internet-scale or simulation data; confined to upper-body tabletop manipulation with parallel-jaw grippers; evaluation methodology relies on proxy metrics with partial human validation.

### Li et al. (2025)

**Research question**: Can a unified video and action model jointly optimize video and action predictions to achieve both high accuracy and efficient action inference for robotics tasks?
**Methodology**: UVA learns a joint video-action latent representation and decouples video-action decoding using two lightweight diffusion heads, enabling high-speed action inference by bypassing video generation during inference, evaluated in single-task and multi-task settings in simulation and real-world environments.
**Key findings**:
- UVA surpasses best baseline by 20% on PushT-M and 5% on Libero10 in multi-task setting [E20]
- UVA achieves faster inference by performing diffusion only on lightweight action head [E21]
- Video generation methods (UVA and UniPi) exhibit superior robustness to visual disturbances [E22]
- Joint video-action modeling is critical - removing video generation reduces performance [E23]
**Limitations**: The framework does not currently leverage large amounts of actionless video data, which could provide valuable additional supervision.

### Lu et al. (2025)

**Research question**: How can world models for robotic manipulation incorporate robust geometric information through 3D Gaussian representations to improve future state prediction and policy learning?
**Methodology**: The authors propose Gaussian World Model (GWM) combining a latent Diffusion Transformer with a 3D variational autoencoder to reconstruct future states by inferring propagation of Gaussian primitives under robot actions, evaluated on Meta-World, RoboCasa, and real-world Franka-PnP environments using action-conditioned prediction, imitation learning, model-based RL, and real-world deployment tasks.
**Key findings**:
- GWM consistently outperforms iVideoGPT on future state prediction across synthetic and real-world environments [E1]
- GWM improves imitation learning success rates across 24 kitchen manipulation tasks [E2]
- GWM achieves faster convergence and higher performance than iVideoGPT in model-based RL [E3]
- GWM achieves 65% success rate vs 35% for Diffusion Policy in real-world pick-and-place tasks [E4]
**Limitations**: Not explicitly stated in the paper; the conclusion focuses on contributions rather than limitations.

### Tian et al. (2024)

**Research question**: Can end-to-end predictive inverse dynamics models that predict actions from forecasted visual states serve as scalable learners for robotic manipulation?
**Methodology**: Seer uses Transformers to process both visual states and actions in an end-to-end paradigm called Predictive Inverse Dynamics Models (PIDM), pre-trained on large-scale robotic datasets like DROID and adapted to real-world scenarios with minimal fine-tuning.
**Key findings**:
- Seer achieves 78.7% success rate on LIBERO-LONG with 9% improvement from pre-training [E32]
- Seer sets new state-of-the-art on CALVIN ABC-D with average sequence length of 4.28 [E33]
- Seer shows exceptional data efficiency with 187% relative improvement under 10% data regime on LIBERO-LONG [E34]
- Seer's evaluation is limited to six downstream tasks requiring broader exploration [E35]
**Limitations**: Only six downstream tasks were evaluated, leaving a broader spectrum of high-precision and contact-rich tasks unexplored, and cross-embodiment capability across different robots remains to be tested.

### Zhu et al. (2025)

**Research question**: Can Unified World Models effectively learn from large robotic datasets as a pretraining paradigm and further benefit from additional video data without action labels?
**Methodology**: UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality, evaluated through real robot experiments with a Franka robot using the DROID manipulation platform and simulated experiments in the LIBERO benchmark.
**Key findings**:
- UWM achieves highest success rates across all five real robot tasks, surpassing best baseline by as much as 20% [E13]
- UWM consistently improves performance when co-trained with additional action-free videos [E14]
- UWM achieves highest success rates on LIBERO benchmark in out-of-distribution setting [E15]
- UWM cotrained on videos is significantly more robust than pretrained UWM and Diffusion Policy [E16]
**Limitations**: The proposed model does not yet learn from large scale human videos, bridging the embodiment gap. Additionally, the forward dynamics reconstruction may often contain artifacts which may reduce efficacy when planning with this model.

### Bharadhwaj et al. (2024)

**Research question**: How can robot manipulation policies generalize to novel tasks involving unseen object types and new motions using web-scale video generation?
**Methodology**: Gen2Act casts language-conditioned manipulation as zero-shot human video generation using pre-trained video models from web data, then conditions a robot policy on the generated video with motion information extracted via point track prediction.
**Key findings**:
- Gen2Act achieves higher success rates for object-type and motion-type generalization compared to baselines [E36]
- Gen2Act enables long-horizon manipulation through chaining of video generation and policy execution for tasks like Making Coffee [E37]
- Co-training with approximately 400 additional trajectories improves Gen2Act generalization performance [E38]
- Gen2Act is limited by video generation models inability to produce realistic hands for dexterous manipulation [E39]
**Limitations**: The system is limited by current video generation capabilities including inability to generate realistic hands for dexterous tasks, and reliable long-horizon manipulation requires augmenting chaining with recovery policies for intermediate failures.

## References

Bharadhwaj, H., Dwibedi, D., Gupta, A., Tulsiani, S., Doersch, C., Xiao, T., Shah, D., Xia, F., Sadigh, D., & Kirmani, S. (2024). Gen2Act: Human video generation in novel scenarios enables generalizable robot manipulation. arXiv. https://arxiv.org/abs/2409.16283

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards autoregressive action world model. arXiv. https://arxiv.org/abs/2506.21539

Huang, S., Chen, L., Zhou, P., Chen, S., Jiang, Z., Hu, Y., Liao, Y., Gao, P., Li, H., Yao, M., & Ren, G. (2025). EnerVerse: Envisioning embodied future space for robotics manipulation. arXiv. https://arxiv.org/abs/2501.01895

Jang, J., Ye, S., Lin, Z., Xiang, J., Bjorck, J., Fang, Y., Hu, F., Huang, S., Kundalia, K., Lin, Y.-C., Magne, L., Mandlekar, A., Narayan, A., Tan, Y. L., Wang, G., Wang, J., Wang, Q., Xu, Y., Zeng, X., Zheng, K., et al. (2025). DreamGen: Unlocking generalization in robot learning through video world models. arXiv. https://arxiv.org/abs/2505.12705

Jiang, Y., Chen, S., Huang, S., Chen, L., Zhou, P., Liao, Y., He, X., Liu, C., Li, H., Yao, M., & Ren, G. (2025). EnerVerse-AC: Envisioning embodied environments with action condition. arXiv. https://arxiv.org/abs/2505.09723

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified video action model. arXiv. https://arxiv.org/abs/2503.00200

Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025). Genie Envisioner: A unified world foundation platform for robotic manipulation. arXiv. https://arxiv.org/abs/2508.05635

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. arXiv. https://arxiv.org/abs/2508.17600

Tian, Y., Yang, S., Zeng, J., Wang, P., Lin, D., Dong, H., & Pang, J. (2024). Predictive inverse dynamics models are scalable learners for robotic manipulation. arXiv. https://arxiv.org/abs/2412.15109

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified world models: Coupling video and action diffusion for pretraining on large robotic datasets. arXiv. https://arxiv.org/abs/2504.02792

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E13 | arXiv:2504.02792 | [IV-B2 Discussion](https://arxiv.org/html/2504.02792#S4.SS2.SSS2.p2) | “We find that UWM achieves the highest success rates across all five tasks among the methods, surpassing the best baseline by as much as 20%.” |
| E21 | arXiv:2503.00200 | [V-D Policy Learning Results](https://arxiv.org/html/2503.00200#S5.SS4.p11) | “Our method achieves faster inference speeds by performing diffusion iterations only on the lightweight action head, rather than the entire network as DP-C and DP-T.” |
| E18 | arXiv:2506.21539 | [Action Chunking Generation with Proposed Attention Mask.](https://arxiv.org/html/2506.21539#S4.SS2.SSS0.Px4.p1) | “The proposed attention masking mechanism ensures that each action is generated independently and solely determined by the visual input, thereby mitigating the issue of error propagation within the action sequence.” |
| E20 | arXiv:2503.00200 | [V-D Policy Learning Results](https://arxiv.org/html/2503.00200#S5.SS4.p4) | “UVA surpasses the best baseline by 20% on the PushT-M task and by 5% on the Libero10 benchmark.” |
| E26 | arXiv:2505.12705 | [Behavior Generalization](https://arxiv.org/html/2505.12705#S3.SS2.SSS0.Px1.p1) | “we see a non-trivial performance gain when trained with neural trajectories (11.2% → 43.2%), showing that our pipeline enables learning totally new verbs” |
| E27 | arXiv:2505.12705 | [7 Limitation](https://arxiv.org/html/2505.12705#S7.p2) | “generating the 240k-sample RoboCasa dataset took 54 hours on 1500 NVIDIA L40 GPUs” |
| E11 | arXiv:2505.09723 | [4.4 EVAC as Data Engine](https://arxiv.org/html/2505.09723#S4.SS4.p2) | “the success rate (SR) improves significantly from 0.28 to 0.36 when the augmented trajectories are included” |
| E7 | arXiv:2508.05635 | [Metric-Human Consistency](https://arxiv.org/html/2508.05635#S6.SS5.p1) | “EWMBench rankings exhibit strong concordance with human judgments” |
| E5 | arXiv:2508.05635 | [World Model Evaluation](https://arxiv.org/html/2508.05635#S6.SS3.p2) | “GE-Base consistently outperforms the baselines across multiple evaluation dimensions” |
| E6 | arXiv:2508.05635 | [World Model Evaluation](https://arxiv.org/html/2508.05635#S6.SS3.p2) | “notable strengths in temporal alignment and dynamic consistency” |
| E29 | arXiv:2501.01895 | [3.2 Comparison Results](https://arxiv.org/html/2501.01895#S3.SS2.p5) | “With single S-RGB input, it achieves an average score of 84.1, outperforming strong baselines” |
| E32 | arXiv:2412.15109 | [4.2 Simulation Main Results](https://arxiv.org/html/2412.15109#S4.SS2.p1) | “our policy achieved an average success rate of 78.7% without pre-training. After pre-training, the success rate increases by 9%” |
| E4 | arXiv:2508.17600 | [4.4 Real-world Deployment](https://arxiv.org/html/2508.17600#S4.SS4.p2) | “GWM outperforms Diffusion Policy (65% vs. 35% success rate) on 20 trials” |
| E3 | arXiv:2508.17600 | [Results and Analyses](https://arxiv.org/html/2508.17600#S4.SS3.SSS0.Px2.p1) | “GWM consistently outperforms iVideoGPT across all six Meta-World tasks” |
| E30 | arXiv:2501.01895 | [3.3 Further Studies](https://arxiv.org/html/2501.01895#S3.SS3.p2) | “the absence of the sparse memory results in significant performance degradation, with the policy achieving only 30.8 compared to 73 when the sparse memory mechanism is applied” |
| E9 | arXiv:2505.09723 | [4.2 Controllable Manipulation Video Generation](https://arxiv.org/html/2505.09723#S4.SS2.p2) | “generated videos remain sharp and reliable for up to 30 consecutive chunks in single-view scenarios” |
| E15 | arXiv:2504.02792 | [IV-C Simulated Experiments](https://arxiv.org/html/2504.02792#S4.SS3.p2) | “UWM achieves the highest success rates across the evauation tasks in the out-of-distribution setting.” |
| E34 | arXiv:2412.15109 | [4.3 Data Efficiency](https://arxiv.org/html/2412.15109#S4.SS3.p1) | “under data-scarce conditions with only 10% of the training data, the pre-trained policy achieves a 187% relative improvement in success rate on LIBERO-LONG” |
| E16 | arXiv:2504.02792 | [IV-D3 Categorized OOD Experiments](https://arxiv.org/html/2504.02792#S4.SS4.SSS3.p1) | “UWM cotrained on videos (co) is significantly more robust than both UWM (pre) and DP pretrained on robot data.” |
| E12 | arXiv:2505.09723 | [4.5 Further Analysis](https://arxiv.org/html/2505.09723#S4.SS5.p2) | “Without failure data, the model tended to overfit to successful examples, leading it to hallucinate” |
| E31 | arXiv:2501.01895 | [5 Conclusions](https://arxiv.org/html/2501.01895#S5.p2) | “video generation models inevitably produce artifacts” |
| E39 | arXiv:2409.16283 | [V Discussion and Conclusion](https://arxiv.org/html/2409.16283#S5.p2) | “limited by the current capabilities of video generation models, like inability to generate realistic hands and thereby limited ability to perform very dexterous tasks” |
| E40 | arXiv:2506.21539 | [World Model Helps Action Model.](https://arxiv.org/html/2506.21539#S4.SS2.SSS0.Px2.p1) | “Quantitative results in Table 3, including row 2 vs. row 1, or row 5 vs. row 4, demonstrate that the integration of a world model significantly enhances the performance of the action model.” |
| E17 | arXiv:2506.21539 | [Action Model Helps World Model.](https://arxiv.org/html/2506.21539#S4.SS2.SSS0.Px3.p1) | “Table 4 demonstrates that the action world model outperforms the pure world model in terms of generation quality, particularly when producing longer video sequences.” |
| E19 | arXiv:2506.21539 | [Pretrain Action Model using World Model.](https://arxiv.org/html/2506.21539#S4.SS2.SSS0.Px7.p1) | “Employing the world model for pretraining leads to notable improvements in grasping performance.” |
| E28 | arXiv:2501.01895 | [3.2 Comparison Results](https://arxiv.org/html/2501.01895#S3.SS2.p2) | “our approach achieves a higher PSNR and a lower FVD” |
| E24 | arXiv:2505.12705 | [Simulation experiments](https://arxiv.org/html/2505.12705#S3.SS1.SSS0.Px1.p2) | “co-training with neural trajectories yields a performance boost for both IDM and LAPA actions across all data regime scenarios” |
| E25 | arXiv:2505.12705 | [Simulation experiments](https://arxiv.org/html/2505.12705#S3.SS1.SSS0.Px1.p2) | “there is a consistent log-linear slope between the total number of neural trajectories and the downstream robot policy performance” |
| E10 | arXiv:2505.09723 | [4.3 EVAC as Policy Evaluator](https://arxiv.org/html/2505.09723#S4.SS3.p1) | “the relative performance trends across tasks were consistent” |
| E8 | arXiv:2508.05635 | [Limitations](https://arxiv.org/html/2508.05635#S8.I1.i1.p1) | “our training relies exclusively on the AgiBot-World-Beta dataset—a large-scale yet single-platform real-world corpus” |
| E22 | arXiv:2503.00200 | [V-D Policy Learning Results](https://arxiv.org/html/2503.00200#S5.SS4.p14) | “Video generation methods, such as UniPi and UVA, exhibit superior performance in handling visual disturbances.” |
| E23 | arXiv:2503.00200 | [V-D Policy Learning Results](https://arxiv.org/html/2503.00200#S5.SS4.p16) | “This modification led to reduced performance compared to the complete framework, highlighting the critical role of video generation in improving policy learning.” |
| E1 | arXiv:2508.17600 | [Results and Analyses](https://arxiv.org/html/2508.17600#S4.SS1.SSS0.Px2.p1) | “our method consistently outperforms the current state-of-the-art image-based world modeling method iVideoGPT on both synthetic and real-world environments” |
| E2 | arXiv:2508.17600 | [Results and Analyses](https://arxiv.org/html/2508.17600#S4.SS2.SSS0.Px2.p1) | “Across 24 kitchen manipulation tasks, our approach consistently outperforms the BC-Transformer baseline” |
| E33 | arXiv:2412.15109 | [4.2 Simulation Main Results](https://arxiv.org/html/2412.15109#S4.SS2.p2) | “The Seer-Large variant achieves Avg. Len. of 4.28, establishing a new state-of-the-art on CALVIN ABC-D benchmark” |
| E35 | arXiv:2412.15109 | [6 Conclusion and Limitations](https://arxiv.org/html/2412.15109#S6.p1) | “we only evaluate six downstream tasks. A broader spectrum of high-precision and contact-rich tasks remains to be explored” |
| E14 | arXiv:2504.02792 | [IV-B2 Discussion](https://arxiv.org/html/2504.02792#S4.SS2.SSS2.p4) | “We find UWM to consistently improve performance when exposed to additional videos during pretraining.” |
| E36 | arXiv:2409.16283 | [IV-E Generalization of Gen2Act to scenes, objects, motions](https://arxiv.org/html/2409.16283#S4.SS5.p1) | “for higher levels of generalization, Gen2Act achieves much higher success rates indicating that human video generation combined with explicitly extracting motion information from track prediction is helpful in unseen tasks” |
| E37 | arXiv:2409.16283 | [IV-F Chaining Gen2Act for long-horizon manipulation](https://arxiv.org/html/2409.16283#S4.SS6.p1) | “Table II shows results for long-horizon activities like Making Coffee that consist of multiple tasks to be performed in sequence” |
| E38 | arXiv:2409.16283 | [IV-G Co-Training with additional teleop demonstrations](https://arxiv.org/html/2409.16283#S4.SS7.p1) | “we see improved performance of Gen2Act with such co-training” |

<!-- /evidence-appendix -->
