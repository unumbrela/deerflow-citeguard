# Systematic Literature Review: World Models for Robotic Manipulation

**Review Period:** May 27, 2024 – May 26, 2026  
**Category:** cs.RO (Robotics)  
**Papers Reviewed:** 10  
**Date of Review:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in world models for robotic manipulation, focusing on 10 key papers published between May 2024 and May 2026 in the cs.RO category. The reviewed literature reveals a rapidly evolving field characterized by three major trends: (1) unified frameworks integrating video generation and action prediction, (2) leveraging generative models for scalable policy learning, and (3) novel representations including 3D Gaussian primitives and latent spaces for embodied intelligence.

The papers demonstrate significant progress in addressing core challenges in robotic manipulation, including generalization to novel tasks and environments, efficient use of action-free video data, and bridging the sim-to-real gap. Notable contributions include Unified World Models (UWM), WorldVLA, DreamGen, EnerVerse, and Gaussian World Models (GWM), each offering distinct approaches to learning and representing environmental dynamics for robotic control.

---

## Methodology

### Search Strategy
- **Database:** arXiv preprint server
- **Primary Category:** cs.RO (Robotics)
- **Date Range:** May 27, 2024 – May 26, 2026
- **Search Query:** "world models robotic manipulation"
- **Initial Pool:** 50 papers
- **Citation Expansion:** 95 additional papers from references
- **Shortlist:** 30 papers
- **Final Selection:** 10 papers based on relevance to world models and robotic manipulation

### Inclusion Criteria
1. Focus on world models, model-based learning, or predictive models
2. Application to robotic manipulation tasks
3. Published within the specified date range in cs.RO category
4. Primary contribution related to learning environmental dynamics or future state prediction

### Selection Process
Papers were screened and scored based on centrality to the topic of world models for robotic manipulation. The 10 most co-cited and central papers were selected for this review.

---

## Reviewed Papers

### 1. Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets

**Authors:** Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A.  
**Publication Date:** April 3, 2025  
**Source:** arXiv:2504.02792v3  
**DOI/URL:** https://arxiv.org/abs/2504.02792v3

**Abstract:**  
Imitation learning has emerged as a promising approach towards building generalist robots. However, scaling imitation learning for large robot foundation models remains challenging due to its reliance on high-quality expert demonstrations. Meanwhile, large amounts of video data depicting a wide range of environments and diverse behaviors are readily available. This data provides a rich source of information about real-world dynamics and agent-environment interactions. Leveraging this data directly for imitation learning, however, has proven difficult due to the lack of action annotation. In this work, we present Unified World Models (UWM), a framework that allows for leveraging both video and action data for policy learning. Specifically, a UWM integrates an action diffusion process and a video diffusion process within a unified transformer architecture, where independent diffusion timesteps govern each modality. By controlling each diffusion timestep, UWM can flexibly represent a policy, a forward dynamics, an inverse dynamics, and a video generator. Through simulated and real-world experiments, we show that: (1) UWM enables effective pretraining on large-scale multitask robot datasets with both dynamics and action predictions, resulting in more generalizable and robust policies than imitation learning, (2) UWM naturally facilitates learning from action-free video data through independent control of modality-specific diffusion timesteps, further improving the performance of finetuned policies. Our results suggest that UWM offers a promising step toward harnessing large, heterogeneous datasets for scalable robot learning, and provides a simple unification between the often disparate paradigms of imitation learning and world modeling.

**Key Contributions:**
- Unified transformer architecture integrating action and video diffusion processes
- Independent control of modality-specific diffusion timesteps for flexible representation
- Effective pretraining on large-scale datasets with both video and action data
- Learning from action-free video data to improve policy performance

---

### 2. WorldVLA: Towards Autoregressive Action World Model

**Authors:** Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H.  
**Publication Date:** June 26, 2025  
**Source:** arXiv:2506.21539v1  
**DOI/URL:** https://arxiv.org/abs/2506.21539v1

**Abstract:**  
We present WorldVLA, an autoregressive action world model that unifies action and image understanding and generation. Our WorldVLA integrates Vision-Language-Action (VLA) model and world model in one single framework. The world model predicts future images by leveraging both action and image understanding, with the purpose of learning the underlying physics of the environment to improve action generation. Meanwhile, the action model generates the subsequent actions based on image observations, aiding in visual understanding and in turn helps visual generation of the world model. We demonstrate that WorldVLA outperforms standalone action and world models, highlighting the mutual enhancement between the world model and the action model. In addition, we find that the performance of the action model deteriorates when generating sequences of actions in an autoregressive manner. This phenomenon can be attributed to the model's limited generalization capability for action prediction, leading to the propagation of errors from earlier actions to subsequent ones. To address this issue, we propose an attention mask strategy that selectively masks prior actions during the generation of the current action, which shows significant performance improvement in the action chunk generation task.

**Key Contributions:**
- Integration of Vision-Language-Action (VLA) model with world model in unified framework
- Mutual enhancement between world model (future image prediction) and action model
- Attention mask strategy to address error propagation in autoregressive action generation
- Improved performance over standalone action and world models

---

### 3. Unified Video Action Model

**Authors:** Li, S., Gao, Y., Sadigh, D., & Song, S.  
**Publication Date:** February 28, 2025  
**Source:** arXiv:2503.00200v3  
**DOI/URL:** https://arxiv.org/abs/2503.00200v3

**Abstract:**  
A unified video and action model holds significant promise for robotics, where videos provide rich scene information for action prediction, and actions provide dynamics information for video prediction. However, effectively combining video generation and action prediction remains challenging, and current video generation-based methods struggle to match the performance of direct policy learning in action accuracy and inference speed. To bridge this gap, we introduce the Unified Video Action model (UVA), which jointly optimizes video and action predictions to achieve both high accuracy and efficient action inference. The key lies in learning a joint video-action latent representation and decoupling video-action decoding. The joint latent representation bridges the visual and action domains, effectively modeling the relationship between video and action sequences. Meanwhile, the decoupled decoding, powered by two lightweight diffusion heads, enables high-speed action inference by bypassing video generation during inference. Such a unified framework further enables versatile functionality through masked input training. By selectively masking actions or videos, a single model can tackle diverse tasks beyond policy learning, such as forward and inverse dynamics modeling and video generation. Via an extensive set of experiments, we demonstrate that UVA can serve as a general-purpose solution for a wide range of robotics tasks, such as policy learning, forward/inverse dynamics and video observation prediction, without compromising performance compared to methods tailored for specific applications.

**Key Contributions:**
- Joint video-action latent representation bridging visual and action domains
- Decoupled decoding with lightweight diffusion heads for high-speed inference
- Masked input training enabling versatile functionality across multiple tasks
- General-purpose solution for policy learning, dynamics modeling, and video prediction

---

### 4. DreamGen: Unlocking Generalization in Robot Learning through Video World Models

**Authors:** Jang, J., Ye, S., Lin, Z., Xiang, J., Bjorck, J., Fang, Y., Hu, F., Huang, S., Kundalia, K., Lin, Y.-C., Magne, L., Mandlekar, A., Narayan, A., Tan, Y. L., Wang, G., Wang, J., Wang, Q., Xu, Y., Zeng, X., & Zheng, K.  
**Publication Date:** May 19, 2025  
**Source:** arXiv:2505.12705v2  
**DOI/URL:** https://arxiv.org/abs/2505.12705v2

**Abstract:**  
We introduce DreamGen, a simple yet highly effective 4-stage pipeline for training robot policies that generalize across behaviors and environments through neural trajectories - synthetic robot data generated from video world models. DreamGen leverages state-of-the-art image-to-video generative models, adapting them to the target robot embodiment to produce photorealistic synthetic videos of familiar or novel tasks in diverse environments. Since these models generate only videos, we recover pseudo-action sequences using either a latent action model or an inverse-dynamics model (IDM). Despite its simplicity, DreamGen unlocks strong behavior and environment generalization: a humanoid robot can perform 22 new behaviors in both seen and unseen environments, while requiring teleoperation data from only a single pick-and-place task in one environment. To evaluate the pipeline systematically, we introduce DreamGen Bench, a video generation benchmark that shows a strong correlation between benchmark performance and downstream policy success. Our work establishes a promising new axis for scaling robot learning well beyond manual data collection.

**Key Contributions:**
- 4-stage pipeline for training policies using synthetic video data from world models
- Adaptation of image-to-video generative models for robot embodiment
- Recovery of pseudo-action sequences using latent action or inverse-dynamics models
- Strong generalization with minimal teleoperation data (single task, single environment)
- DreamGen Bench for systematic evaluation of video generation and policy success

---

### 5. EnerVerse: Envisioning Embodied Future Space for Robotics Manipulation

**Authors:** Huang, S., Chen, L., Zhou, P., Chen, S., Jiang, Z., Hu, Y., Liao, Y., Gao, P., Li, H., Yao, M., & Ren, G.  
**Publication Date:** January 3, 2025  
**Source:** arXiv:2501.01895v3  
**DOI/URL:** https://arxiv.org/abs/2501.01895v3

**Abstract:**  
We introduce EnerVerse, a generative robotics foundation model that constructs and interprets embodied spaces. EnerVerse employs a chunk-wise autoregressive video diffusion framework to predict future embodied spaces from instructions, enhanced by a sparse context memory for long-term reasoning. To model the 3D robotics world, we adopt a multi-view video representation, providing rich perspectives to address challenges like motion ambiguity and 3D grounding. Additionally, EnerVerse-D, a data engine pipeline combining generative modeling with 4D Gaussian Splatting, forms a self-reinforcing data loop to reduce the sim-to-real gap. Leveraging these innovations, EnerVerse translates 4D world representations into physical actions via a policy head (EnerVerse-A), achieving state-of-the-art performance in both simulation and real-world tasks. For efficiency, EnerVerse-A reuses features from the first denoising step and predicts action chunks, achieving about 280 ms per 8-step action chunk on a single RTX 4090.

**Key Contributions:**
- Chunk-wise autoregressive video diffusion with sparse context memory
- Multi-view video representation for 3D robotics world modeling
- EnerVerse-D data engine combining generative modeling with 4D Gaussian Splatting
- Self-reinforcing data loop to reduce sim-to-real gap
- Efficient policy head achieving 280 ms per 8-step action chunk

---

### 6. Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation

**Authors:** Tian, Y., Yang, S., Zeng, J., Wang, P., Lin, D., Dong, H., & Pang, J.  
**Publication Date:** December 19, 2024  
**Source:** arXiv:2412.15109v1  
**DOI/URL:** https://arxiv.org/abs/2412.15109v1

**Abstract:**  
Current efforts to learn scalable policies in robotic manipulation primarily fall into two categories: one focuses on "action," which involves behavior cloning from extensive collections of robotic data, while the other emphasizes "vision," enhancing model generalization by pre-training representations or generative models, also referred to as world models, using large-scale visual datasets. This paper presents an end-to-end paradigm that predicts actions using inverse dynamics models conditioned on the robot's forecasted visual states, named Predictive Inverse Dynamics Models (PIDM). By closing the loop between vision and action, the end-to-end PIDM can be a better scalable action learner. In practice, we use Transformers to process both visual states and actions, naming the model Seer. It is initially pre-trained on large-scale robotic datasets, such as DROID, and can be adapted to real-world scenarios with a little fine-tuning data. Thanks to large-scale, end-to-end training and the synergy between vision and action, Seer significantly outperforms previous methods across both simulation and real-world experiments. It achieves improvements of 13% on the LIBERO-LONG benchmark, 21% on CALVIN ABC-D, and 43% in real-world tasks. Notably, Seer sets a new state-of-the-art on CALVIN ABC-D benchmark, achieving an average length of 4.28, and exhibits superior generalization for novel objects, lighting conditions, and environments under high-intensity disturbances on real-world scenarios.

**Key Contributions:**
- End-to-end Predictive Inverse Dynamics Models (PIDM) paradigm
- Transformer-based model (Seer) processing both visual states and actions
- Pre-training on large-scale robotic datasets (e.g., DROID)
- Significant improvements: 13% on LIBERO-LONG, 21% on CALVIN ABC-D, 43% in real-world tasks
- New state-of-the-art on CALVIN ABC-D (average length 4.28)

---

### 7. Gen2Act: Human Video Generation in Novel Scenarios enables Generalizable Robot Manipulation

**Authors:** Bharadhwaj, H., Dwibedi, D., Gupta, A., Tulsiani, S., Doersch, C., Xiao, T., Shah, D., Xia, F., Sadigh, D., & Kirmani, S.  
**Publication Date:** September 24, 2024  
**Source:** arXiv:2409.16283v1  
**DOI/URL:** https://arxiv.org/abs/2409.16283v1

**Abstract:**  
How can robot manipulation policies generalize to novel tasks involving unseen object types and new motions? In this paper, we provide a solution in terms of predicting motion information from web data through human video generation and conditioning a robot policy on the generated video. Instead of attempting to scale robot data collection which is expensive, we show how we can leverage video generation models trained on easily available web data, for enabling generalization. Our approach Gen2Act casts language-conditioned manipulation as zero-shot human video generation followed by execution with a single policy conditioned on the generated video. To train the policy, we use an order of magnitude less robot interaction data compared to what the video prediction model was trained on. Gen2Act doesn't require fine-tuning the video model at all and we directly use a pre-trained model for generating human videos. Our results on diverse real-world scenarios show how Gen2Act enables manipulating unseen object types and performing novel motions for tasks not present in the robot data.

**Key Contributions:**
- Zero-shot human video generation for novel scenarios
- Conditioning robot policy on generated human videos
- Leveraging web data instead of scaling expensive robot data collection
- Order of magnitude less robot interaction data required
- No fine-tuning of video model needed
- Generalization to unseen object types and novel motions

---

### 8. GWM: Towards Scalable Gaussian World Models for Robotic Manipulation

**Authors:** Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S.  
**Publication Date:** August 25, 2025  
**Source:** arXiv:2508.17600v2  
**DOI/URL:** https://arxiv.org/abs/2508.17600v2

**Abstract:**  
Training robot policies within a learned world model is trending due to the inefficiency of real-world interactions. The established image-based world models and policies have shown prior success, but lack robust geometric information that requires consistent spatial and physical understanding of the three-dimensional world, even pre-trained on internet-scale video sources. To this end, we propose a novel branch of world model named Gaussian World Model (GWM) for robotic manipulation, which reconstructs the future state by inferring the propagation of Gaussian primitives under the effect of robot actions. At its core is a latent Diffusion Transformer (DiT) combined with a 3D variational autoencoder, enabling fine-grained scene-level future state reconstruction with Gaussian Splatting. GWM can not only enhance the visual representation for imitation learning agent by self-supervised future prediction training, but can serve as a neural simulator that supports model-based reinforcement learning. Both simulated and real-world experiments depict that GWM can precisely predict future scenes conditioned on diverse robot actions, and can be further utilized to train policies that outperform the state-of-the-art by impressive margins, showcasing the initial data scaling potential of 3D world model.

**Key Contributions:**
- Novel Gaussian World Model (GWM) using Gaussian primitives for 3D representation
- Latent Diffusion Transformer (DiT) combined with 3D variational autoencoder
- Fine-grained scene-level future state reconstruction with Gaussian Splatting
- Dual functionality: visual representation enhancement and neural simulator
- Policies trained in GWM outperform state-of-the-art by significant margins

---

### 9. Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation

**Authors:** Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G.  
**Publication Date:** August 7, 2025  
**Source:** arXiv:2508.05635v3  
**DOI/URL:** https://arxiv.org/abs/2508.05635v3

**Abstract:**  
We introduce Genie Envisioner (GE), a unified world foundation platform for robotic manipulation that integrates policy learning, evaluation, and simulation within a single video-generative framework. At its core, GE-Base is a large-scale, instruction-conditioned video diffusion model that captures the spatial, temporal, and semantic dynamics of real-world robotic interactions in a structured latent space. Built upon this foundation, GE-Act maps latent representations to executable action trajectories through a lightweight, flow-matching decoder, enabling precise and generalizable policy inference across diverse embodiments with minimal supervision. To support scalable evaluation and training, GE-Sim serves as an action-conditioned neural simulator, producing high-fidelity rollouts for closed-loop policy development. The platform is further equipped with EWMBench, a standardized benchmark suite measuring visual fidelity, physical consistency, and instruction-action alignment. Together, these components establish Genie Envisioner as a scalable and practical foundation for instruction-driven, general-purpose embodied intelligence.

**Key Contributions:**
- Unified platform integrating policy learning, evaluation, and simulation
- GE-Base: instruction-conditioned video diffusion model in structured latent space
- GE-Act: lightweight flow-matching decoder for action trajectory mapping
- GE-Sim: action-conditioned neural simulator for closed-loop policy development
- EWMBench: standardized benchmark suite for comprehensive evaluation

---

### 10. EnerVerse-AC: Envisioning Embodied Environments with Action Condition

**Authors:** Jiang, Y., Chen, S., Huang, S., Chen, L., Zhou, P., Liao, Y., He, X., Liu, C., Li, H., Yao, M., & Ren, G.  
**Publication Date:** May 14, 2025  
**Source:** arXiv:2505.09723v1  
**DOI/URL:** https://arxiv.org/abs/2505.09723v1

**Abstract:**  
Robotic imitation learning has advanced from solving static tasks to addressing dynamic interaction scenarios, but testing and evaluation remain costly and challenging due to the need for real-time interaction with dynamic environments. We propose EnerVerse-AC (EVAC), an action-conditional world model that generates future visual observations based on an agent's predicted actions, enabling realistic and controllable robotic inference. Building on prior architectures, EVAC introduces a multi-level action-conditioning mechanism and ray map encoding for dynamic multi-view image generation while expanding training data with diverse failure trajectories to improve generalization. As both a data engine and evaluator, EVAC augments human-collected trajectories into diverse datasets and generates realistic, action-conditioned video observations for policy testing, eliminating the need for physical robots or complex simulations. This approach significantly reduces costs while maintaining high fidelity in robotic manipulation evaluation.

**Key Contributions:**
- Action-conditional world model for generating future visual observations
- Multi-level action-conditioning mechanism and ray map encoding
- Training data augmentation with diverse failure trajectories
- Dual functionality as data engine and evaluator
- Cost reduction by eliminating need for physical robots or complex simulations

---

## Thematic Analysis

### Theme 1: Unified Video-Action Frameworks

Four papers (Zhu et al., 2025; Li et al., 2025; Cen et al., 2025; Liao et al., 2025) propose unified frameworks that integrate video generation and action prediction. These approaches recognize the complementary nature of visual and action information: videos provide rich scene context while actions encode environmental dynamics. Key innovations include:

- **Modality-independent control:** UWM (Zhu et al., 2025) uses independent diffusion timesteps for video and action modalities, enabling flexible representation as policy, forward/inverse dynamics, or video generator.
- **Joint latent representations:** UVA (Li et al., 2025) learns joint video-action latent spaces with decoupled decoding for efficient inference.
- **Mutual enhancement:** WorldVLA (Cen et al., 2025) demonstrates bidirectional benefits between world model and action model components.
- **Structured latent spaces:** Genie Envisioner (Liao et al., 2025) captures spatial, temporal, and semantic dynamics in unified latent representations.

### Theme 2: Generative Models for Scalable Data Synthesis

Three papers (Jang et al., 2025; Bharadhwaj et al., 2024; Jiang et al., 2025) leverage generative models to synthesize training data, addressing the bottleneck of expensive robot data collection:

- **Neural trajectories:** DreamGen (Jang et al., 2025) generates synthetic videos adapted to robot embodiments, recovering pseudo-actions via latent action or inverse dynamics models.
- **Zero-shot human video generation:** Gen2Act (Bharadhwaj et al., 2024) uses pre-trained video generation models on web data, requiring an order of magnitude less robot data.
- **Action-conditional data augmentation:** EnerVerse-AC (Jiang et al., 2025) augments human trajectories with diverse failure cases and generates realistic video observations for policy testing.

### Theme 3: Advanced 3D Representations

Two papers (Huang et al., 2025; Lu et al., 2025) introduce novel 3D representations for more robust geometric understanding:

- **4D Gaussian Splatting:** EnerVerse (Huang et al., 2025) employs multi-view video representation with 4D Gaussian Splatting in a self-reinforcing data loop.
- **Gaussian primitives:** GWM (Lu et al., 2025) reconstructs future states by inferring propagation of Gaussian primitives, enabling fine-grained scene-level prediction with geometric consistency.

### Theme 4: End-to-End Predictive Models

One paper (Tian et al., 2024) presents an end-to-end paradigm closing the vision-action loop:

- **Predictive Inverse Dynamics:** Seer (Tian et al., 2024) predicts actions using inverse dynamics models conditioned on forecasted visual states, achieving state-of-the-art performance on multiple benchmarks.

---

## Comparative Analysis

| Paper | Representation | Key Innovation | Data Efficiency | Generalization |
|-------|---------------|----------------|-----------------|----------------|
| UWM (Zhu et al., 2025) | Video + Action diffusion | Independent modality timesteps | Learns from action-free video | High |
| WorldVLA (Cen et al., 2025) | Autoregressive VLA | Attention mask for action chunks | Moderate | High |
| UVA (Li et al., 2025) | Joint latent representation | Decoupled decoding | High | High |
| DreamGen (Jang et al., 2025) | Synthetic video trajectories | 4-stage pipeline | Very high (1 task, 1 env) | Very high (22 behaviors) |
| EnerVerse (Huang et al., 2025) | 4D Gaussian Splatting | Multi-view + sparse memory | High | High |
| Seer (Tian et al., 2024) | Visual states + actions | End-to-end PIDM | High | Very high |
| Gen2Act (Bharadhwaj et al., 2024) | Human video generation | Zero-shot web data | Very high (10x less robot data) | High |
| GWM (Lu et al., 2025) | Gaussian primitives | 3D DiT + VAE | High | High |
| Genie Envisioner (Liao et al., 2025) | Structured latent space | Unified platform | High | High |
| EnerVerse-AC (Jiang et al., 2025) | Action-conditional video | Multi-level conditioning | High | High |

---

## Key Findings

### 1. Unification is Dominant Trend
The majority of reviewed papers (6 out of 10) propose unified frameworks combining video generation and action prediction. This reflects recognition that world models and policies benefit from shared representations and mutual enhancement.

### 2. Data Efficiency Through Generation
Generative world models enable dramatic improvements in data efficiency. DreamGen requires teleoperation from only one task in one environment yet generalizes to 22 behaviors. Gen2Act uses 10x less robot data by leveraging web-scale video models.

### 3. 3D Representations Emerging
Recent work (2025) shows shift toward 3D representations (Gaussian Splatting, Gaussian primitives) addressing limitations of image-based models in geometric and physical understanding.

### 4. Benchmarks Maturing
Multiple papers introduce dedicated benchmarks (DreamGen Bench, EWMBench) correlating video generation quality with downstream policy success, enabling systematic evaluation.

### 5. Sim-to-Real Gap Addressed
Several approaches (EnerVerse-D's self-reinforcing loop, GWM's neural simulator, EnerVerse-AC's action-conditional evaluation) explicitly target reducing sim-to-real gap through realistic world modeling.

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Physical Consistency:** While visual fidelity has improved, ensuring physical consistency in generated worlds remains challenging. Only GWM (Lu et al., 2025) and Genie Envisioner (Liao et al., 2025) explicitly address physical plausibility.

2. **Long-Horizon Reasoning:** Most approaches focus on short-horizon prediction. EnerVerse's sparse context memory is one of few mechanisms for long-term reasoning.

3. **Multi-Embodiment Generalization:** While several papers claim cross-embodiment capabilities, systematic evaluation across diverse robot morphologies is limited.

4. **Real-Time Performance:** Only EnerVerse-A (280 ms per action chunk) and UVA report inference speeds. Real-time deployment requirements need more attention.

5. **Failure Mode Learning:** EnerVerse-AC is unique in explicitly training on failure trajectories. More work needed on learning from failures.

### Future Directions

1. **Hybrid Representations:** Combining Gaussian primitives with neural radiance fields or explicit physics engines for better geometric and physical reasoning.

2. **World Model Ensembles:** Using multiple specialized world models for different aspects (geometry, dynamics, semantics) rather than monolithic approaches.

3. **Active Data Collection:** World models guiding which data to collect next, optimizing data efficiency through uncertainty-aware exploration.

4. **Human-Robot Collaboration:** Extending world models to predict and reason about human actions in collaborative manipulation scenarios.

5. **Causal World Models:** Moving beyond correlation-based prediction to causal understanding of intervention effects.

---

## Conclusions

This systematic review reveals a field in rapid transition, with world models for robotic manipulation evolving from simple forward dynamics predictors to sophisticated generative frameworks unifying perception, prediction, and action. The 10 reviewed papers demonstrate several converging trends:

- **Integration over separation:** Unified frameworks outperform specialized models by leveraging complementary information across modalities.
- **Generation over collection:** Synthetic data from world models reduces dependence on expensive robot data collection while improving generalization.
- **3D over 2D:** Emerging 3D representations address fundamental limitations of image-based models in spatial and physical reasoning.
- **Platforms over models:** Comprehensive platforms (Genie Envisioner, EnerVerse) integrating learning, simulation, and evaluation are replacing isolated model contributions.

The field has made substantial progress toward general-purpose robotic manipulation, with demonstrated generalization to novel objects, environments, and behaviors. However, challenges remain in physical consistency, long-horizon reasoning, and real-time deployment. Future work addressing these gaps, particularly through hybrid representations and causal modeling, will be critical for deploying world model-based policies in real-world robotic applications.

---

## References

Bharadhwaj, H., Dwibedi, D., Gupta, A., Tulsiani, S., Doersch, C., Xiao, T., Shah, D., Xia, F., Sadigh, D., & Kirmani, S. (2024). Gen2Act: Human video generation in novel scenarios enables generalizable robot manipulation. *arXiv preprint arXiv:2409.16283*. https://arxiv.org/abs/2409.16283v1

Cen, J., Yu, C., Yuan, H., Jiang, Y., Huang, S., Guo, J., Li, X., Song, Y., Luo, H., Wang, F., Zhao, D., & Chen, H. (2025). WorldVLA: Towards autoregressive action world model. *arXiv preprint arXiv:2506.21539*. https://arxiv.org/abs/2506.21539v1

Huang, S., Chen, L., Zhou, P., Chen, S., Jiang, Z., Hu, Y., Liao, Y., Gao, P., Li, H., Yao, M., & Ren, G. (2025). EnerVerse: Envisioning embodied future space for robotics manipulation. *arXiv preprint arXiv:2501.01895*. https://arxiv.org/abs/2501.01895v3

Jang, J., Ye, S., Lin, Z., Xiang, J., Bjorck, J., Fang, Y., Hu, F., Huang, S., Kundalia, K., Lin, Y.-C., Magne, L., Mandlekar, A., Narayan, A., Tan, Y. L., Wang, G., Wang, J., Wang, Q., Xu, Y., Zeng, X., & Zheng, K. (2025). DreamGen: Unlocking generalization in robot learning through video world models. *arXiv preprint arXiv:2505.12705*. https://arxiv.org/abs/2505.12705v2

Jiang, Y., Chen, S., Huang, S., Chen, L., Zhou, P., Liao, Y., He, X., Liu, C., Li, H., Yao, M., & Ren, G. (2025). EnerVerse-AC: Envisioning embodied environments with action condition. *arXiv preprint arXiv:2505.09723*. https://arxiv.org/abs/2505.09723v1

Li, S., Gao, Y., Sadigh, D., & Song, S. (2025). Unified Video Action Model. *arXiv preprint arXiv:2503.00200*. https://arxiv.org/abs/2503.00200v3

Liao, Y., Zhou, P., Huang, S., Yang, D., Chen, S., Jiang, Y., Hu, Y., Cai, J., Liu, S., Luo, J., Chen, L., Yan, S., Yao, M., & Ren, G. (2025). Genie Envisioner: A unified world foundation platform for robotic manipulation. *arXiv preprint arXiv:2508.05635*. https://arxiv.org/abs/2508.05635v3

Lu, G., Jia, B., Li, P., Chen, Y., Wang, Z., Tang, Y., & Huang, S. (2025). GWM: Towards scalable Gaussian world models for robotic manipulation. *arXiv preprint arXiv:2508.17600*. https://arxiv.org/abs/2508.17600v2

Tian, Y., Yang, S., Zeng, J., Wang, P., Lin, D., Dong, H., & Pang, J. (2024). Predictive Inverse Dynamics Models are Scalable Learners for Robotic Manipulation. *arXiv preprint arXiv:2412.15109*. https://arxiv.org/abs/2412.15109v1

Zhu, C., Yu, R., Feng, S., Burchfiel, B., Shah, P., & Gupta, A. (2025). Unified World Models: Coupling video and action diffusion for pretraining on large robotic datasets. *arXiv preprint arXiv:2504.02792*. https://arxiv.org/abs/2504.02792v3

---

## Appendix: Search Methodology Details

### Search Execution
- **Search Date:** October 26, 2026
- **Database:** arXiv API
- **Initial Query:** "world models robotic manipulation"
- **Category Filter:** cs.RO (primary category match)
- **Date Window:** May 27, 2024 – May 26, 2026

### Pool Statistics
- **Initial Matches:** 50 papers
- **Citation Expansion:** 95 papers added from references
- **Total Pool:** 145 papers
- **Shortlisted:** 30 papers
- **Screened:** 30 papers
- **Final Selection:** 10 papers

### Screening Scores Distribution
- Score 6: 1 paper
- Score 14: 1 paper
- Score 9: 1 paper
- Score 5: 7 papers

### Selection Criteria
Papers were scored based on:
1. Centrality to world models for robotic manipulation
2. Novelty of contribution
3. Empirical validation quality
4. Citation impact within the shortlist
5. Relevance to practical robotic applications
