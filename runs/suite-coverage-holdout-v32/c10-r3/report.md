# Systematic Literature Review: Open World Detection

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "open world detection", category cs.CV, published between 2023-08-22 and 2025-08-21
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on open world detection reveals a rapidly evolving field focused on enabling vision systems to detect and recognize objects beyond fixed, pre-defined vocabularies. The papers collectively demonstrate three major directions: (1) leveraging vision-language models and synthetic data generation to reduce annotation costs, (2) developing novel architectural approaches for unknown object identification, and (3) creating unified models that support multiple perception tasks simultaneously. A strong consensus emerges around the need to move beyond traditional closed-set detection paradigms, with particular emphasis on autonomous driving, aerial imagery, and traffic analytics applications. However, the field still grapples with challenges around hallucination noise in synthetic data, maintaining known-class performance while detecting unknowns, and scaling annotation pipelines efficiently.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "open world detection", filtered to category cs.CV, published between 2023-08-22 and 2025-08-21. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Vision-Language Models for Annotation-Free Detection

A dominant approach across the surveyed literature involves leveraging pre-trained vision-language models to generate synthetic captions and reduce reliance on manual annotation. Kong et al. (2024) introduced HyperLearner, which bootstraps dense synthetic captions using vision-language models and incorporates hyperbolic vision-language learning to impose hierarchy between visual and caption embeddings, effectively mitigating hallucination noise. Similarly, Wei et al. (2025) developed the OS-W2S Label Engine, an automatic annotation pipeline centered around large vision-language models that integrates image-operation-based preprocessing with BERT-based postprocessing to handle diverse scene annotations across words, phrases, and sentences. Their MI-OAD dataset contains 163,023 images and 2 million image-caption pairs, approximately 40 times larger than comparable datasets. Guan et al. (2025) extended this direction with Prompt-DINO, proposing an early fusion mechanism that unifies text and visual prompts with backbone features, alongside a generative data engine (RAP model) that synthesizes 0.5 billion diverse training instances through dual-path cross-verification, reducing label noise by 80.5% compared to conventional approaches.

### Theme 2: Unknown Object Identification Through Geometric and Semantic Cues

Several papers address the fundamental challenge of identifying unknown objects without compromising known-class performance. Yavuz and Güney (2024) proposed the O1O (Odd-One-Out) approach, which groups known classes into superclasses and uses geometric cues with an odd-one-out scoring mechanism to identify unknown classes, drawing inspiration from human cognition studies to better partition the feature space. Their approach achieves significant improvements in unknown recall while maintaining known class performance, avoiding confusion from noisy pseudo-labels. Ren et al. (2024) took a different approach with DINO-X, employing a Transformer-based encoder-decoder architecture that supports text, visual, and customized prompts, including a universal object prompt for prompt-free detection. Pre-trained on Grounding-100M with over 100 million grounding samples, DINO-X achieves 56.0 AP on COCO and improves previous state-of-the-art performance by 5.8 AP on rare class detection benchmarks.

### Theme 3: Semi-Supervised and Active Learning for Real-World Deployment

A critical practical concern involves reducing annotation costs while maintaining detection quality in deployment scenarios. Mullappilly et al. (2024) proposed semi-supervised open-world detection (SS-OWOD), which casts incremental learning stages in a semi-supervised manner. Their SS-OWFormer detector uses feature-alignment to align object query representations between original and augmented images, plus a pseudo-labeling scheme for unknown detection. Experiments across four datasets (MS COCO, PASCAL, Objects365, DOTA) demonstrated that state-of-the-art OWOD detector performance dramatically deteriorates in the semi-supervised setting, highlighting the importance of their feature-alignment approach. Chen et al. (2023) extended active learning to 3D object detection with Open-CRB, proposing Open Label Conciseness (OLC) that mines novel 3D objects with minimal annotation costs. Their framework supports comprehensive reproduction with codebase covering 15 baseline methods, 2 detector types (SECOND and PV-RCNN), and 3 benchmark datasets (KITTI, nuScenes, Waymo), demonstrating superiority in recognizing both novel and known classes with very limited labeling costs.

### Theme 4: Automated Data Engines and Annotation Pipelines

The burden of manual annotation has motivated development of fully automated data curation systems. Liang et al. (2024) designed AIDE (Automatic Data Engine), which leverages vision-language and large language models to automatically identify issues, curate data, improve models through auto-labeling, and verify models through diverse scenario generation in an iterative self-improvement process for autonomous driving perception. Rocky and Wu (2025) introduced SAM2Auto, combining SMART-OD (automatic mask generation with open-world object detection) and FLASH (multi-object real-time video instance segmentation) to create a fully automated annotation pipeline requiring no human intervention or dataset-specific training. SAM2Auto achieves comparable accuracy to manual annotation while dramatically reducing annotation time and eliminating labor costs, successfully handling diverse datasets without requiring retraining or extensive parameter adjustments.

### Theme 5: Domain-Specific Applications in Autonomous Systems

Several papers target specific application domains with tailored solutions. Yu et al. (2025) built LAVA for traffic video analytics, a system with three components: multi-armed bandit-based sampling for video segment-level localization, video-specific open-world detection for object-level retrieval, and long-term object trajectory extraction for temporal association. LAVA processes videos 9.6 times faster than the most accurate baseline while improving F1-scores for selection queries by 14% and achieving top-k precision of 86%. Liang et al. (2024) specifically addressed autonomous driving with AIDE, establishing a benchmark for open-world detection on AV datasets to evaluate various learning paradigms and demonstrating superior performance at reduced cost compared to manual curation approaches.

## Convergences and Disagreements

**Convergences**: The surveyed papers unanimously agree that traditional closed-set detection paradigms are insufficient for real-world deployment, with eight of ten papers explicitly addressing the need to handle unknown or novel objects without extensive manual annotation. There is strong consensus around leveraging pre-trained vision-language models as a foundation, with six papers building upon or extending such models. Multiple papers converge on the importance of reducing annotation costs, whether through synthetic data generation (Kong et al., 2024; Guan et al., 2025), automated pipelines (Liang et al., 2024; Rocky & Wu, 2025; Wei et al., 2025), or semi-supervised learning (Mullappilly et al., 2024; Chen et al., 2023).

**Disagreements**: The papers diverge on the optimal strategy for unknown object identification. Yavuz and Güney (2024) advocate geometric cues and superclass grouping, while Ren et al. (2024) favor unified multi-prompt architectures with massive pre-training. There is also tension between approaches that prioritize known-class performance maintenance (Yavuz & Güney, 2024) versus those that accept some degradation for improved unknown recall. The extent to which synthetic data can replace manual annotation remains contested, with Guan et al. (2025) reporting 80.5% label noise reduction while others note hallucination challenges requiring additional mitigation strategies (Kong et al., 2024).

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either insufficient self-critique or space constraints that prevent honest discussion of failure modes. Second, while multiple papers address annotation cost reduction, there is limited discussion of the computational costs associated with training large vision-language models or running automated pipelines. Third, the temporal dimension of open-world detection—how systems should adapt to objects that appear, disappear, or change over time—receives minimal attention beyond trajectory extraction in LAVA (Yu et al., 2025). Fourth, evaluation benchmarks remain fragmented across different datasets (COCO, LVIS, KITTI, nuScenes, Waymo, aerial imagery), making cross-paper comparison difficult. Finally, the ethical implications of deploying open-world detection systems in safety-critical applications like autonomous driving are not addressed in any of the surveyed papers.

## Per-Paper Annotations

### Chen et al. (2023)

**Research question**: How can active learning for 3D object detection be extended to handle streaming point clouds that may contain unknown or novel objects in real-world open-world deployments?

**Methodology**: The paper proposes Open Label Conciseness (OLC), a strategy that mines novel 3D objects with minimal annotation costs, and integrates it with an active learning method called CRB to form the Open-CRB framework. The approach is evaluated across 15 baseline methods, 2 types of 3D detectors (SECOND and PV-RCNN), and 3 benchmark datasets (KITTI, nuScenes, Waymo) with a single round of selection.

**Key findings**:
- OLC successfully adapts the 3D detection model to open-world scenarios with just one round of selection
- Any generic active learning policy can be integrated with OLC to efficiently address the OWAL-3D problem
- Open-CRB demonstrates superiority and flexibility in recognizing both novel and known classes with very limited labeling costs compared to state-of-the-art baselines
- The framework supports comprehensive reproduction with codebase covering 15 baseline methods, 2 detector types, and 3 benchmark datasets

**Limitations**: Not stated in abstract

### Guan et al. (2025)

**Research question**: How can early fusion and optimized query selection improve multimodal vision models for open-world segmentation beyond fixed-vocabulary constraints?

**Methodology**: The authors propose Prompt-DINO with three innovations: early fusion mechanism unifying text/visual prompts with backbone features, order-aligned query selection for DETR-based architectures, and a generative data engine (RAP model) synthesizing 0.5B diverse training instances through dual-path cross-verification.

**Key findings**:
- Early fusion enables deeper cross-modal interactions, resolving semantic ambiguities in hybrid prompt segmentation
- Order-aligned query selection enhances semantic-spatial consistency between text and visual queries during decoding
- The RAP generative data engine reduces label noise by 80.5% compared to conventional approaches
- Prompt-DINO achieves state-of-the-art performance on open-world detection benchmarks with expanded semantic coverage

**Limitations**: Not stated in abstract

### Kong et al. (2024)

**Research question**: How can vision-language models be leveraged to enrich open-vocabulary descriptions for open-world detection without expensive manual annotation?

**Methodology**: The authors propose HyperLearner, which bootstraps dense synthetic captions using pre-trained vision-language models and incorporates a novel hyperbolic vision-language learning approach to impose hierarchy between visual and caption embeddings, mitigating hallucination noise.

**Key findings**:
- HyperLearner consistently outperforms existing state-of-the-art methods including GLIP, GLIPv2, and Grounding DINO when using the same backbone
- Synthetic captions generated by vision-language models effectively enrich open-vocabulary descriptions without manual annotation
- Hyperbolic vision-language learning mitigates noise caused by hallucination in synthetic captions
- The model generalizes well to novel concepts across multiple benchmarks including COCO, LVIS, Object Detection in the Wild, and RefCOCO

**Limitations**: Not stated in abstract

### Liang et al. (2024)

**Research question**: How can automatic data curation and annotation reduce the human effort required for continuously improving perception models in autonomous driving?

**Methodology**: The authors design AIDE (Automatic Data Engine), which leverages vision-language and large language models to automatically identify issues, curate data, improve models through auto-labeling, and verify models through diverse scenario generation in an iterative self-improvement process.

**Key findings**:
- AIDE enables continuous self-improvement of perception models through an iterative automatic process
- The method demonstrates superior performance at reduced cost compared to manual curation approaches
- The approach addresses the long-tailed distribution of objects encountered in autonomous driving scenarios
- A benchmark for open-world detection on AV datasets was established to evaluate various learning paradigms

**Limitations**: Not stated in abstract

### Mullappilly et al. (2024)

**Research question**: How can open-world object detection be made more realistic for real-world deployment by reducing reliance on human oracles during incremental learning stages?

**Methodology**: The authors propose a semi-supervised open-world detection (SS-OWOD) formulation that casts incremental learning stages in a semi-supervised manner. They introduce SS-OWFormer, a novel detector using feature-alignment to align object query representations between original and augmented images, plus a pseudo-labeling scheme for unknown detection.

**Key findings**:
- State-of-the-art OWOD detector performance dramatically deteriorates in the proposed SS-OWOD setting
- SS-OWFormer's feature-alignment scheme effectively leverages large unlabeled and few labeled data
- The pseudo-labeling scheme exploits decoder object queries' inherent capability to capture object-specific information
- Experiments on 4 datasets (MS COCO, PASCAL, Objects365, DOTA) demonstrate the approach's effectiveness

**Limitations**: Not stated in abstract

### Ren et al. (2024)

**Research question**: How can a unified vision model achieve superior open-world object detection performance while supporting multiple perception and understanding tasks?

**Methodology**: DINO-X employs a Transformer-based encoder-decoder architecture extending input options to support text, visual, and customized prompts, including a universal object prompt for prompt-free detection. The model was pre-trained on Grounding-100M, a dataset with over 100 million grounding samples, and integrates multiple perception heads for simultaneous task support.

**Key findings**:
- DINO-X Pro achieves 56.0 AP on COCO, 59.8 AP on LVIS-minival, and 52.4 AP on LVIS-val zero-shot object detection benchmarks
- Scores 63.3 AP and 56.5 AP on rare classes of LVIS-minival and LVIS-val benchmarks
- Improves previous SOTA performance by 5.8 AP and 5.0 AP on rare class detection
- Supports multiple tasks including detection, segmentation, pose estimation, object captioning, and object-based QA simultaneously
- The universal object prompt enables detecting anything in an image without requiring user prompts

**Limitations**: Not stated in abstract

### Rocky and Wu (2025)

**Research question**: How can automated annotation pipelines eliminate the labor-intensive bottleneck in creating paired visual-textual datasets for vision-language model development?

**Methodology**: The authors introduce SAM2Auto, combining SMART-OD (automatic mask generation with open-world object detection) and FLASH (multi-object real-time video instance segmentation) to create a fully automated annotation pipeline requiring no human intervention or dataset-specific training.

**Key findings**:
- SAM2Auto achieves comparable accuracy to manual annotation while dramatically reducing annotation time and eliminating labor costs
- The system employs statistical approaches to minimize false positives while ensuring consistent object tracking throughout video sequences
- The pipeline successfully handles diverse datasets without requiring retraining or extensive parameter adjustments
- The approach addresses the fundamental dataset bottleneck constraining vision-language model development

**Limitations**: Not stated in abstract

### Wei et al. (2025)

**Research question**: How can large-scale language-guided open-set aerial detection datasets be constructed to support fine-grained open-world detection beyond vocabulary-level descriptions?

**Methodology**: The authors propose the OS-W2S Label Engine, an automatic annotation pipeline centered around an open-source large vision-language model, integrating image-operation-based preprocessing with BERT-based postprocessing to handle diverse scene annotations across three levels: words, phrases, and sentences.

**Key findings**:
- MI-OAD dataset contains 163,023 images and 2 million image-caption pairs, approximately 40 times larger than comparable datasets
- Training on MI-OAD lifts Grounding DINO by +31.1 AP50 and +34.7 Recall@10 with sentence-level inputs under zero-shot transfer
- MI-OAD pre-training yields state-of-the-art performance on multiple existing open-vocabulary aerial detection and remote sensing visual grounding benchmarks
- The dataset addresses limitations of current remote sensing grounding data

**Limitations**: Not stated in abstract

### Yavuz and Güney (2024)

**Research question**: How can geometric cues and class grouping improve unknown object detection without compromising known class performance in open-world settings?

**Methodology**: The authors propose grouping known classes into superclasses and using an odd-one-out scoring mechanism to identify unknown classes, drawing inspiration from human cognition studies to better partition the feature space.

**Key findings**:
- Geometric cues improve unknown recall in open-world object detection
- Grouping known classes into superclasses enables identification of unknown classes through odd-one-out scoring
- The approach achieves significant improvements in unknown recall consistently across all tasks
- Known class performance is maintained without compromise, avoiding confusion from noisy pseudo-labels

**Limitations**: Not stated in abstract

### Yu et al. (2025)

**Research question**: How can natural language-driven video analytics enable flexible and efficient querying of large-scale traffic video databases beyond the constraints of rigid SQL-based patterns?

**Methodology**: The authors build LAVA, a system with three components: (1) multi-armed bandit-based sampling for video segment-level localization, (2) video-specific open-world detection for object-level retrieval, and (3) long-term object trajectory extraction for temporal association. They developed a novel benchmark with diverse natural language predicates and fine-grained annotations.

**Key findings**:
- LAVA improves F1-scores for selection queries by 14% compared to baselines
- Reduces MPAE for aggregation queries by 0.39
- Achieves top-k precision of 86%
- Processes videos 9.6 times faster than the most accurate baseline
- The system supports multiple levels of granularity and arbitrary categories in traffic target retrieval

**Limitations**: Not stated in abstract

## References

Chen, Z., Luo, Y., Wang, Z., Wang, Z., Yu, X., & Huang, Z. (2023). Open-CRB: Towards open world active learning for 3D object detection. arXiv. https://arxiv.org/abs/2310.10391

Guan, Y., Sun, C., Fu, C., Huang, Z., Yuan, C., & Li, C. (2025). Text-guided visual prompt DINO for generic segmentation. arXiv. https://arxiv.org/abs/2508.06146

Kong, F., Chen, Y., Cai, J., & Modolo, D. (2024). Hyperbolic learning with synthetic captions for open-world detection. arXiv. https://arxiv.org/abs/2404.05016

Liang, M., Su, J.-C., Schulter, S., Garg, S., Zhao, S., Wu, Y., & Chandraker, M. (2024). AIDE: An automatic data engine for object detection in autonomous driving. arXiv. https://arxiv.org/abs/2403.17373

Mullappilly, S. S., Gehlot, A. S., Anwer, R. M., Khan, F. S., & Cholakkal, H. (2024). Semi-supervised open-world object detection. arXiv. https://arxiv.org/abs/2402.16013

Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., & Zhang, L. (2024). DINO-X: A unified vision model for open-world object detection and understanding. arXiv. https://arxiv.org/abs/2411.14347

Rocky, A., & Wu, Q. M. J. (2025). SAM2Auto: Auto annotation using FLASH. arXiv. https://arxiv.org/abs/2506.07850

Wei, G., Liu, Y., Yuan, X., Xue, X., Guo, L., Yang, Y., Zhao, C., Bai, Z., Zhang, H., & Xiao, R. (2025). OS-W2S: An automatic labeling engine for language-guided open-set aerial object detection. arXiv. https://arxiv.org/abs/2505.03334

Yavuz, M., & Güney, F. (2024). O1O: Grouping of known classes to identify unknown objects as odd-one-out. arXiv. https://arxiv.org/abs/2410.07514

Yu, Y., Zhou, T., Sun, J., Qiao, L., Ding, L., Yuan, Y., & Wang, G. (2025). LAVA: Language driven scalable and versatile traffic video analytics. arXiv. https://arxiv.org/abs/2507.19821
