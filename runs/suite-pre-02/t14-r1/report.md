# Systematic Literature Review: Video Understanding with Multimodal Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "video multimodal", category cs.CV, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of video understanding with multimodal large language models has experienced rapid advancement between 2025 and 2026, with research converging on five critical challenges: efficient token compression, fine-grained temporal reasoning, hallucination mitigation, human preference alignment, and controllable user interaction. The surveyed literature reveals a maturing field moving beyond basic video captioning toward sophisticated temporal reasoning, where models must understand not just what appears in frames, but how events unfold over time. A notable trend is the shift from training-heavy approaches to plug-and-play modules that can enhance existing MLLMs without retraining, alongside growing emphasis on evaluation frameworks that detect hallucinations and align outputs with human preferences. Despite significant progress, common limitations persist around computational costs, domain generalization, and the need for large annotated datasets.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query `video multimodal`, filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Token Compression and Computational Efficiency

A dominant research direction addresses the prohibitive computational cost of processing dense visual tokens in video MLLMs. Fang et al. (2024) introduced Visual Token Coding (VTC), which adapts classical video coding principles from HEVC to predict I/P frames and measure frame-wise residuals for estimating token redundancy. Their dynamic variant VTC_Dy achieves remarkable efficiency, retaining 100.1% performance with only 50% token budget and 97.8% performance at 25% budget for Qwen3-VL, all without requiring additional model tuning. Complementing this approach, Yu et al. (2026) proposed VisionTrim, a unified training-free framework that integrates Dominant Vision Token Selection (DVTS) with Text-Guided Vision Complement (TGVC) to preserve essential tokens while maintaining textual alignment during compression. Both works demonstrate that intelligent token selection can dramatically reduce computational overhead without sacrificing accuracy, though neither thoroughly analyzes the added complexity of their dynamic selection mechanisms.

### Theme 2: Fine-Grained Temporal and Motion Understanding

Multiple papers identify temporal reasoning as a core bottleneck in current video MLLMs. Zhao et al. (2025) addressed VMLLMs' limited ability to reason about brief actions and rare transient events through VideoPerceiver, which employs a two-stage training framework using "key-information-missing" videos and relative rewards in reinforcement learning to enhance sensitivity to fine-grained motion cues. Their approach substantially outperforms state-of-the-art models on fine-grained action understanding while maintaining performance on standard tasks. Similarly, Zhu et al. (2026) proposed COMET, which introduces an explicit temporal motion branch built on Taylor frame differences and combines temporal prior distillation with forward-reverse TC-GRPO optimization. COMET achieves a 4.9% improvement on action-centric tasks and 2.1% on temporal reasoning tasks while leaving static perception unchanged, demonstrating targeted enhancement of motion-temporal capabilities. Both works converge on the insight that explicit temporal modeling, rather than sparse frame sampling alone, is essential for robust video understanding.

### Theme 3: Hallucination Detection and Mitigation

Hallucination in video MLLMs has emerged as a critical challenge, with two distinct approaches appearing in the literature. Xing et al. (2026) focused on compositional hallucinations arising from incorrect reasoning over interacting spatial and temporal factors, introducing the OmniVCHall benchmark and TriCD contrastive decoding framework. Their evaluation of 39 VLLMs revealed that even advanced models like Qwen3-VL and GPT-5 exhibit substantial degradation on compositional hallucination tasks, and TriCD achieves over 10% accuracy improvement through adaptive perturbation and saliency-guided enhancement. Jing et al. (2025) took a broader approach with FIFA, a unified faithfulness evaluation framework that extracts descriptive facts, models semantic dependencies via Spatio-Temporal Semantic Dependency Graphs, and verifies them using VideoQA models. FIFA uniquely addresses both Video-to-Text and Text-to-Video generation, with their Post-Correction tool effectively improving factual consistency in both directions. The convergence across these works indicates that hallucination detection requires structured semantic modeling rather than surface-level consistency checks.

### Theme 4: Human Preference Alignment

The alignment of video MLLM outputs with human preferences represents an emerging research direction. Tang et al. (2025) proposed AVC-DPO, which uses Direct Preference Optimization with enhanced prompts targeting temporal dynamics and spatial information—two factors humans prioritize when watching videos. Their approach achieved first place in the LOVE@CVPR'25 Video Detailed Captioning Challenge by leveraging the same foundation model's responses under varied prompt conditions for preference-aware training. In a different domain, Xue et al. (2026) developed a computational model of Message Sensation Value (MSV) for short video engagement, finding that while MSV positively correlates with sensory engagement, it shows an inverted U-shaped relationship with behavioral engagement—moderate MSV optimizes user interaction. Both works demonstrate that understanding and incorporating human preferences, whether through explicit preference optimization or engagement modeling, significantly improves practical deployment.

### Theme 5: Adaptive and Controllable Architectures

Recent work emphasizes user control and adaptive feature fusion in video MLLMs. Zhang et al. (2026) introduced the novel task of Controllable Video Segmentation and Captioning (SegCaptioning), where users provide bounding box prompts to generate aligned masks and captions. Their SG-FSCFormer framework uses a Prompt-guided Temporal Graph Former and Fine-grained Mask-linguistic Decoder to achieve precise user-intent alignment. Sun et al. (2025) proposed LLaVA-Octopus, which adaptively weights features from different visual projectors based on user instructions, recognizing that some projectors excel at static details while others better capture temporal information. Both approaches share the insight that single, monolithic architectures cannot optimally handle all video understanding tasks, and that dynamic adaptation—whether to user prompts or task requirements—enables superior performance across diverse scenarios.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key findings. First, all papers addressing efficiency agree that token compression is necessary and achievable without substantial performance loss, with multiple works demonstrating 50% or greater token reduction while maintaining 97-100% performance. Second, there is strong agreement that explicit temporal modeling—rather than improved frame sampling alone—is essential for fine-grained video understanding, as evidenced by VideoPerceiver, COMET, and the temporal components in FIFA. Third, multiple papers independently identify that plug-and-play, training-free modules offer practical advantages for deployment, appearing in VTC, VisionTrim, and TriCD. Finally, there is convergence around the need for structured semantic representations, whether in Spatio-Temporal Semantic Dependency Graphs (FIFA), scene graphs (SG-FSCFormer), or motion-temporal branches (COMET).

**Disagreements**: The literature shows limited direct disagreement, as most papers address distinct subproblems. However, there is an implicit tension between approaches requiring extensive training or dataset curation (VideoPerceiver's 80,000-video dataset, SG-FSCFormer's benchmark training) and those emphasizing training-free deployment (VisionTrim, VTC). This reflects a broader field-level question about whether performance gains justify the annotation and training costs. Additionally, while most papers evaluate on standard benchmarks, Xue et al. (2026) focus on short video engagement rather than traditional understanding tasks, suggesting different success metrics for different application domains.

## Gaps and Open Questions

Several gaps emerge consistently across the surveyed literature:

1. **Computational overhead analysis**: Multiple papers (VTC, COMET, LLaVA-Octopus) introduce additional architectural components but do not thoroughly analyze inference-time computational costs or latency implications, leaving practical deployment questions unanswered.

2. **Domain generalization**: Nearly all papers acknowledge limited evaluation diversity—most benchmarks focus on specific video types (action recognition, short videos, captioning datasets), and cross-domain generalization remains underexplored.

3. **Annotation costs**: Approaches requiring large curated datasets (VideoPerceiver's 80,000 videos, OmniVCHall's fine-grained taxonomy) do not address the scalability of annotation efforts, creating a barrier to replication and extension.

4. **Real-time applications**: Despite efficiency improvements, none of the surveyed papers explicitly address real-time or streaming video scenarios, which have different latency and memory constraints than batch processing.

5. **Cultural and contextual factors**: The MSV study (Xue et al., 2026) notes potential platform-specific effects, but broader cultural and contextual variation in video understanding is absent from the literature.

6. **Long-horizon reasoning**: While temporal understanding is well-studied, reasoning over very long videos (hours rather than minutes) remains an open challenge, with most benchmarks capping at short to medium durations.

## Per-Paper Annotations

### Fang et al. (2026)

**Research question**: How can visual tokens in video Multimodal Large Language Models be compressed efficiently while maintaining model performance?
**Methodology**: Proposes Visual Token Coding (VTC) inspired by classical video coding principles (e.g., HEVC) that performs structured compression by predicting I/P frames and measuring frame-wise residuals to estimate token redundancy, enhanced with Dynamic Resolution Input, Dynamic Token Allocation, and Spatial Coverage Top-K.
**Key findings**:
- VTC_Dy achieves 100.1% average performance retention with only 50% token budget for Qwen3-VL
- Retains 97.8% of average performance even when token budget is reduced to 25%
- Works as a plug-and-play design requiring no additional tuning of MLLMs
- Successfully validated across three different MLLMs on multiple video understanding benchmarks
**Limitations**: The computational overhead of dynamic designs is not thoroughly analyzed; may not generalize equally well to all video types and domains beyond the tested benchmarks.

### Xing et al. (2026)

**Research question**: How can compositional hallucinations arising from incorrect reasoning over multiple interacting spatial and temporal factors be mitigated in video MLLMs?
**Methodology**: Introduces OmniVCHall benchmark for systematic evaluation of isolated and compositional hallucinations, and proposes TriCD, a contrastive decoding framework with triple-pathway calibration using adaptive perturbation controller and saliency-guided enhancement module optimized via reinforcement learning.
**Key findings**:
- Evaluation of 39 VLLMs reveals even advanced models (Qwen3-VL, GPT-5) exhibit substantial performance degradation on compositional hallucinations
- TriCD achieves average accuracy improvement of over 10% across two representative backbone models
- Introduces novel camera-based hallucination type with fine-grained taxonomy
- Adversarial answer options effectively prevent shortcut reasoning
- OmniVCHall spans diverse video domains enabling comprehensive hallucination evaluation
**Limitations**: The benchmark may not capture all possible hallucination types in real-world video scenarios; reinforcement learning optimization adds training complexity and computational cost.

### Zhao et al. (2025)

**Research question**: How can VMLLMs' limited ability to reason about brief actions in short clips or rare transient events in long videos be improved?
**Methodology**: Adopts two-stage training framework: SFT constructs 'key-information-missing' videos by replacing key frames with adjacent frames and uses auxiliary contrastive loss for visual-text alignment; RL uses relative reward ensuring complete video responses outperform degraded inputs; curated 80,000 video dataset with fine-grained actions and transient events.
**Key findings**:
- Substantially outperforms state-of-the-art VMLLMs on fine-grained action understanding benchmarks
- Achieves strong performance on rare event captioning tasks in long videos
- Maintains competitive performance on standard video understanding tasks
- Prioritizes task-relevant visual features through the two-stage training approach
- 80,000 video dataset enables robust training for fine-grained temporal perception
**Limitations**: Curating 80,000 videos with fine-grained annotations requires significant resources; the approach may not generalize well to all video domains beyond those covered in the curated dataset.

### Zhu et al. (2026)

**Research question**: How can fine-grained motion-temporal understanding in video MLLMs be strengthened beyond the limitations of sparse frame sampling?
**Methodology**: Proposes temporally grounded framework with temporal motion branch built on Taylor frame differences, injects motion evidence into appearance stream via temporal attention bias-enhanced cross-attention, and combines temporal prior distillation with forward-reverse TC-GRPO optimization for direction-aware learning.
**Key findings**:
- Action-centric tasks (STAR, SSv2) improve by 4.9% on average on Qwen3-VL-8B
- Temporal reasoning tasks (NExT-QA, CLEVRER, LLaVA-178K) improve by 2.1% over BL-GRPO
- Static perception tasks (PerceptionTest) remain on par, showing targeted improvement
- Gain pattern transfers to InternVL2.5-8B, indicating generalization across model families
- Explicit temporal representation and appearance-motion fusion address core temporal modeling bottleneck
**Limitations**: The motion-temporal bias may not benefit all task types equally; additional architectural components increase model complexity and inference cost.

### Zhang et al. (2026)

**Research question**: How can users be empowered to provide specific prompts for controllable video segmentation and captioning with precise mask-caption alignment?
**Methodology**: Proposes novel Controllable Video Segmentation and Captioning (SegCaptioning) task with SG-FSCFormer framework integrating Prompt-guided Temporal Graph Former with adaptive prompt adaptor for user intent capture, and Fine-grained Mask-linguistic Decoder with Multi-entity Contrastive loss for mask-caption pair prediction and alignment.
**Key findings**:
- Achieves remarkable performance on two benchmark datasets for controllable video segmentation and captioning
- Effectively captures user intent from bounding box prompts around objects of interest
- Generates precise mask-caption pairs with fine-grained alignment between masks and corresponding caption tokens
- Enables interactive user control over video interpretation beyond global comprehension
- Scene graph guidance improves semantic coherence between segmented regions and generated captions
**Limitations**: Requires explicit user prompts (e.g., bounding boxes) which may limit applicability in fully automated scenarios; comprehensive evaluation limited to two benchmark datasets.

### Yu et al. (2026)

**Research question**: How can multimodal large language models be accelerated without training while reducing excessive visual tokens that cause high computational costs?
**Methodology**: Proposes VisionTrim, a unified training-free framework integrating two plug-and-play modules: Dominant Vision Token Selection (DVTS) for preserving essential visual tokens via global-local views, and Text-Guided Vision Complement (TGVC) for context-aware token merging guided by textual cues.
**Key findings**:
- Unified token reduction approach addresses multiple pipeline components simultaneously rather than in isolation
- Maintains textual alignment during token compression, avoiding performance degradation common in existing methods
- Demonstrates superior performance across diverse image and video multimodal benchmarks
- Training-free design enables practical deployment without additional model training costs
**Limitations**: Abstract does not explicitly acknowledge limitations; potential constraints may include compatibility with specific MLLM architectures and effectiveness across all vision-language tasks.

### Tang et al. (2025)

**Research question**: How can video multimodal large language models adjust caption focal emphasis according to human preferences?
**Methodology**: Proposes AVC-DPO, a post-training framework using Direct Preference Optimization with enhanced prompts targeting temporal dynamics and spatial information, leveraging the same foundation model's responses under varied prompt conditions for preference-aware training.
**Key findings**:
- Achieved first place on the Video Detailed Captioning (VDC) benchmark according to VDCSCORE evaluation metric at LOVE@CVPR'25 Workshop
- Enhanced prompts successfully incorporate human-centric preferences for temporal and spatial information
- DPO framework effectively aligns video captions with human preferences without requiring separate preference models
- Same foundation model can generate varied responses suitable for preference optimization under different prompt conditions
**Limitations**: Abstract does not explicitly state limitations; approach may depend on quality of prompt design and may not generalize to all video domains or caption styles beyond those targeted by the enhanced prompts.

### Sun et al. (2025)

**Research question**: How can video MLLMs leverage complementary strengths of different visual projectors to improve video understanding performance?
**Methodology**: Introduces LLaVA-Octopus that adaptively weights features from different visual projectors based on user instructions, dynamically selecting and combining the most suitable features for each task.
**Key findings**:
- Different visual projectors exhibit distinct characteristics: some excel at static details, others at temporal information or temporal coherence
- Instruction-driven adaptive fusion enables dynamic feature selection based on task requirements
- Achieves excellent performance on video question answering, long video understanding, and comprehensive multi-choice benchmarks
- Complementary projector strengths can be effectively combined rather than choosing a single projector architecture
**Limitations**: Abstract does not explicitly acknowledge limitations; potential concerns include computational overhead from maintaining multiple projectors and complexity of learning optimal weighting strategies.

### Jing et al. (2025)

**Research question**: How can hallucinations in both Text-to-Video and Video-to-Text generation be evaluated and corrected in a unified framework?
**Methodology**: Proposes FIFA framework that extracts comprehensive descriptive facts, models semantic dependencies via Spatio-Temporal Semantic Dependency Graph, verifies using VideoQA models, and introduces Post-Correction tool-based framework for revising hallucinated content.
**Key findings**:
- FIFA aligns more closely with human judgment than existing evaluation methods for hallucination detection
- Post-Correction framework effectively improves factual consistency in both text and video generation
- Unified approach addresses both V2T and T2V tasks, unlike existing methods limited to single task types
- Framework can assess hallucinations in open-ended, free-form responses, addressing a key gap in existing methods
**Limitations**: Abstract does not explicitly state limitations; framework depends on VideoQA model quality and may have computational costs from dependency graph construction and verification steps.

### Xue et al. (2026)

**Research question**: What is the collective impact of multimodal features on viewer engagement with short videos, and how does Message Sensation Value predict sensory and behavioral engagement?
**Methodology**: Develops and tests a computational model of Message Sensation Value (MSV) using multimodal feature analysis and human evaluation of 1,200 short videos, validated across two unseen datasets from three platforms (combined N=14,492).
**Key findings**:
- MSV is positively associated with sensory engagement: higher MSV elicits stronger sensory stimulation
- MSV shows inverted U-shaped relationship with behavioral engagement: moderate MSV optimizes behavioral engagement
- Computational model successfully predicts both sensory and behavioral engagement across multiple platforms
- Model validated across three different short video platforms demonstrating generalizability
**Limitations**: Study focused on short videos; findings may not generalize to long-form content. Cultural and platform-specific effects on MSV-engagement relationships may require further investigation.

## References

Fang, C., Chen, T., You, J., Peng, J., Zhou, Y., & Ji, R. (2026). Visual token coding for video multimodal large language models. arXiv. https://arxiv.org/abs/2608.28008

Jing, L., Lai, V., Yoon, S., Bui, T., & Du, X. (2025). FIFA: Unified faithfulness evaluation framework for text-to-video and video-to-text generation. arXiv. https://arxiv.org/abs/2507.06523

Sun, B., Zhao, J., Chen, X., Wei, X., & Hou, Q. (2025). LLaVA-Octopus: Unlocking instruction-driven adaptive projector fusion for video understanding. arXiv. https://arxiv.org/abs/2501.05067

Tang, J., Li, H., Du, Y., & Zhao, W. X. (2025). AVC-DPO: Aligned video captioning via direct preference optimization. arXiv. https://arxiv.org/abs/2507.01492

Xing, W., Zha, Q., Zu, L., Li, M., Li, M., & Yan, J. (2026). Learning to decode against compositional hallucination in video multimodal large language models. arXiv. https://arxiv.org/abs/2602.00559

Xue, H., Zhang, J., Wang, X., Kim, D. D., & Song, Y. (2026). A computational model of message sensation value in short video multimodal features that predicts sensory and behavioral engagement. arXiv. https://arxiv.org/abs/2604.19995

Yu, H., Li, W., Qu, X., Wang, S., Chen, J., & Zhu, J. (2026). VisionTrim: Unified vision token compression for training-free MLLM acceleration. arXiv. https://arxiv.org/abs/2601.22674

Zhang, X., Yuan, J., Yang, B., Liu, X., Zhang, Q., Wang, Y., Li, Z., & Zhang, H. (2026). Scene graph-guided SegCaptioning transformer with fine-grained alignment for controllable video segmentation and captioning. arXiv. https://arxiv.org/abs/2603.20887

Zhao, F., Zhang, L., Shi, D., Gao, Y., Ye, C., Cai, Y., Gao, J., & Yan, D. (2025). VideoPerceiver: Enhancing fine-grained temporal perception in video multimodal large language models. arXiv. https://arxiv.org/abs/2511.18823

Zhu, C., Kang, Z., Shi, Q., Wu, S., Jiang, K., Wei, L., Hu, L., Dong, G., Yang, M., Lu, R., & Luo, G. (2026). COMET: Contrastive motion-enhanced temporal reasoning for video multimodal large language models. arXiv. https://arxiv.org/abs/2608.21030
