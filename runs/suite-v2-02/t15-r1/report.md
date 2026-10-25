# Systematic Literature Review: Promptable Image Segmentation Foundation Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "promptable image segmentation foundation models", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The field of promptable image segmentation foundation models has experienced rapid expansion beyond general-purpose vision tasks into specialized domains, particularly medical imaging, remote sensing, and video segmentation. The surveyed literature reveals a clear trend toward domain-specific adaptation of the Segment Anything Model (SAM) family, with researchers addressing the substantial performance degradation that occurs when vanilla SAM is applied to specialized imaging modalities. Key advances include parameter-efficient adaptation techniques that preserve the promptable interface while injecting domain-specific knowledge, test-time adaptation frameworks that eliminate the need for extensive annotation, and novel synthetic data generation pipelines that overcome annotation scarcity. The collective findings indicate that successful deployment of promptable segmentation in specialized domains requires full model adaptation rather than simple prompt engineering, with emerging consensus around lightweight adaptation strategies that balance performance gains with computational efficiency.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "promptable image segmentation foundation models", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Domain-Specific Medical Imaging Adaptation

A dominant research direction involves adapting SAM architectures for medical imaging applications, where vanilla models exhibit severe performance degradation due to domain shift. Multiple papers demonstrate that medical images—spanning CT, MRI, PET, and other modalities—require specialized training strategies beyond simple prompt engineering. Jiang et al. (2026) showed that vanilla SAM3 performance degrades substantially on medical data, relying heavily on ground-truth-derived bounding boxes, necessitating full fine-tuning across 33 datasets spanning 10 medical imaging modalities. Similarly, Zhang et al. (2025) constructed PETS-5k, the largest PET segmentation dataset with 5,731 3D whole-body images, to train SegAnyPET with cross-prompting confident learning that handles discrepant annotation quality. Stenhede et al. (2025) took a different approach, training ENSAM from scratch on under 5,000 volumes using a SegResNet-based architecture optimized for 3D medical image interactive segmentation. The convergence across these works indicates that medical imaging demands modality-specific foundation models rather than zero-shot application of general-purpose segmenters.

### Theme 2: Parameter-Efficient Adaptation Strategies

A second prominent theme involves developing lightweight adaptation methods that inject domain knowledge while preserving the core SAM architecture and promptable interface. Malaisree et al. (2026) demonstrated that Low-Rank Adaptation (LoRA) applied to SAM3, updating only 0.121% to 1.341% of parameters, achieved dramatic improvements in structural defect segmentation—with pixel IoU improving from 0.017 to 0.855 on an independent dataset. Their approach introduced hard-negative prompting to prevent model collapse at no annotation cost. Jalilian and Bais (2026) proposed CLIP-Guided SAM, which injects CLIP-derived semantic features through lightweight multi-modal adapters directly into SAM's image encoder, achieving superior performance against SAM+PEFT baselines while remaining parameter-efficient in both training and deployment. These works collectively establish that substantial performance gains can be achieved through targeted architectural modifications rather than full model retraining.

### Theme 3: Synthetic Data and Test-Time Adaptation

Emerging research addresses annotation scarcity through synthetic data generation and test-time adaptation frameworks that eliminate the need for extensive labeled datasets. Pang et al. (2026) introduced HyperSAM, which couples a physics-informed hyperspectral synthesis pipeline with spectral adaptation architecture, generating full-spectrum hyperspectral cubes from SpaceNet multispectral imagery using SAM3-derived pseudo-masks. Their approach demonstrates that high-quality synthetic data can be more effective than simply scaling noisy hyperspectral supervision. Li et al. (2025) developed AutoMiSeg, a zero-shot automatic segmentation pipeline combining vision-language and segmentation foundation models with test-time adaptation using learnable adaptors that align medical inputs with foundation model representations, achieving a 69% relative improvement in Dice Score without requiring ground-truth labels for hyperparameter optimization. These approaches represent a paradigm shift toward annotation-efficient methodologies that reduce barriers to foundation model deployment.

### Theme 4: Extension to Video and Temporal Domains

Recent work extends promptable segmentation from static images to video domains, addressing the challenge of temporally consistent mask propagation in dynamic scenes. Mei et al. (2025) introduced SAM-I2V, which upgrades pre-trained SAM to support promptable video segmentation through an image-to-video feature extraction upgrader, memory filtering strategy, and memory-as-prompt mechanism. Their method achieves over 90% of SAM 2's performance while using only 0.2% of its training cost, presenting a resource-efficient pathway to promptable video segmentation. This work demonstrates that strategic upgrading of image-based foundation models can effectively extend capabilities to temporal domains without prohibitive computational investment.

### Theme 5: Human-Centric Prompting and Model Sensitivity

A critical but underexplored theme involves evaluating how promptable foundation models perform under realistic human-generated prompts versus idealized prompts derived from reference labels. Magg et al. (2026) tested 11 promptable foundation models using human prompts collected through observer studies on musculoskeletal CT segmentation, finding that all models were sensitive to prompt variations and that performance drops significantly when using human prompts compared to ideal prompts. Their work identified Pareto-optimal models (SAM and SAM2.1 in 2D, nnInteractive and Med-SAM2 in 3D) and revealed that localization accuracy and rater consistency vary substantially with anatomical complexity. Chattopadhyay et al. (2025) similarly emphasized that promptable foundation models show potential in bridging domain gaps via smart prompting techniques, but their comprehensive experimental study across 12 datasets highlighted the variability in zero-shot domain generalization capabilities. These findings suggest that reported performance using ideal prompts may substantially overestimate real-world utility in human-driven settings.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that vanilla SAM-family models experience substantial performance degradation when applied directly to specialized domains, particularly medical imaging (Jiang et al., 2026; Zhang et al., 2025; Stenhede et al., 2025). There is also consensus that parameter-efficient adaptation strategies can achieve dramatic improvements while preserving the promptable interface (Malaisree et al., 2026; Jalilian & Bais, 2026). Additionally, several works agree that synthetic data generation and test-time adaptation offer viable pathways to reduce annotation dependency (Pang et al., 2026; Li et al., 2025).

**Disagreements**: While most papers advocate for domain-specific adaptation, there is variation in the recommended adaptation intensity. Some works demonstrate success with full fine-tuning on domain-specific datasets (Jiang et al., 2026; Zhang et al., 2025), while others achieve comparable gains through lightweight parameter-efficient methods updating less than 2% of parameters (Malaisree et al., 2026; Jalilian & Bais, 2026). The field has not yet converged on whether full model adaptation or parameter-efficient fine-tuning represents the optimal strategy for different domain characteristics.

## Gaps and Open Questions

The surveyed literature reveals several notable gaps. First, none of the papers explicitly discuss computational requirements, inference latency, or deployment constraints in their abstracts, despite these factors being critical for clinical or industrial adoption. Second, while multiple papers address medical imaging applications, there is limited discussion of regulatory considerations, clinical validation protocols, or integration with existing medical imaging workflows. Third, the human-centric evaluation of promptable models remains nascent—only Magg et al. (2026) conducted observer studies with human prompts, suggesting that most reported performance metrics may not reflect real-world usability. Fourth, there is no explicit discussion of failure modes, edge cases, or safety considerations when foundation models are deployed in high-stakes domains like medical diagnosis or structural defect detection. Finally, the field lacks standardized benchmarks for comparing promptable segmentation models across domains, making it difficult to assess whether advances in one domain transfer to others.

## Per-Paper Annotations

### Chattopadhyay et al. (2025)

**Research question**: How well do foundation models trained on diverse large-scale data generalize across domains in 3D medical image segmentation without additional training?
**Methodology**: Conducts a comprehensive experimental study examining 6 medical segmentation foundation models across 12 public datasets spanning multiple modalities and anatomies to evaluate their zero-shot domain generalization capabilities.
**Key findings**:
- Promptable foundation models show potential in bridging the domain gap via smart prompting techniques
- Provides valuable insights into the viability of foundation models for domain generalization
- Identifies promising avenues for future research in zero-shot domain generalization
- Study encompasses diverse modalities including CT, MRI, and other imaging protocols
**Limitations**: not stated in abstract

### Jalilian and Bais (2026)

**Research question**: How can promptable segmentation models like SAM be made semantically aware without losing their promptable interface?
**Methodology**: Proposes CLIP-Guided SAM, a framework that injects CLIP-derived text, vision, and similarity features directly into SAM's image encoder through lightweight multi-modal semantic adapters. Supports two operating modes: Manual mode for interactive segmentation with text and spatial prompts, and Semi-Automatic text-only mode for concept-specific segmentation.
**Key findings**:
- Robustness depends on aligning training with the type of prompts used at inference, making train-test prompt consistency an important design principle
- Achieves superior or competitive performance against SAM+PEFT baselines without semantic conditioning, vision-language + SAM pipelines, SAM 3, and strong semi-supervised segmentation methods
- Remains parameter-efficient in both training and deployment
- Applies to both general-domain benchmarks and specialized downstream tasks in low labeled-data settings
**Limitations**: not stated in abstract

### Jiang et al. (2026)

**Research question**: How can SAM3 be adapted to overcome domain shifts and achieve robust prompt-driven medical image segmentation across diverse imaging modalities?
**Methodology**: Medical SAM3 was developed by fully fine-tuning SAM3 on 33 datasets spanning 10 medical imaging modalities with paired segmentation masks and text prompts, enabling the model to acquire domain-specific representations while preserving prompt-driven flexibility for 2D and 3D medical imaging.
**Key findings**:
- Vanilla SAM3 performance degrades substantially on medical data, relying heavily on ground-truth-derived bounding boxes
- Medical SAM3 demonstrates consistent and significant performance gains across organs, imaging modalities, and dimensionalities
- The model excels in challenging scenarios with semantic ambiguity, complex morphology, and long-range 3D context
- Full model adaptation beyond prompt engineering is necessary for robust medical image segmentation
- Medical SAM3 establishes itself as a universal, text-guided segmentation foundation model for medical imaging
**Limitations**: not stated in abstract

### Li et al. (2025)

**Research question**: Can a zero-shot automatic segmentation pipeline combining vision-language and segmentation foundation models achieve competitive performance without requiring extensive annotation or interactive prompts?
**Methodology**: The method uses a grounding model to generate initial bounding boxes from task definitions, followed by visual prompt boosting and promptable segmentation. A test-time adaptation framework with learnable adaptors aligns medical inputs with foundation model representations, with hyperparameters optimized via Bayesian Optimization guided by a proxy validation model without ground-truth labels.
**Key findings**:
- The pipeline achieved a 69% relative improvement in Dice Score (from 42.53 to 71.81) over the previously best-performing method
- The fully automatic pipeline performs competitively with weakly-prompted interactive foundation models
- The approach was evaluated successfully on seven diverse medical imaging datasets
- The method offers an annotation-efficient and scalable solution for zero-shot medical image segmentation
**Limitations**: not stated in abstract

### Magg et al. (2026)

**Research question**: How do different promptable foundation models perform when using human-generated prompts for musculoskeletal CT segmentation?
**Methodology**: Tests 11 promptable foundation models using non-iterative 2D and 3D prompting strategies on private and public datasets focusing on bone and implant segmentation in four anatomical regions, identifies Pareto-optimal models, and further analyzes them using human prompts collected through a dedicated observer study.
**Key findings**:
- Segmentation performance varies significantly between foundation models and prompting strategies
- Pareto-optimal models identified: SAM and SAM2.1 in 2D, nnInteractive and Med-SAM2 in 3D
- Localization accuracy and rater consistency vary with anatomical structures, with higher consistency for simple structures (wrist bones) and lower consistency for complex structures (pelvis, tibia, implants)
- Performance drops using human prompts, suggesting that performance reported on ideal prompts from reference labels might overestimate performance in human-driven settings
- All models were sensitive to prompt variations; while two models demonstrated intra-rater robustness, it did not scale to inter-rater settings
**Limitations**: not stated in abstract

### Malaisree et al. (2026)

**Research question**: How can Low-Rank Adaptation (LoRA) be applied to SAM3 for multi-class structural defect segmentation while addressing failure modes specific to concept-promptable models?
**Methodology**: The study applies LoRA to SAM3 with two methodological contributions: (1) a supervision procedure that trains directly from COCO-style class-labeled instance segmentation using category names as prompts, and (2) exhaustive hard-negative prompting to prevent the model from degenerating into responding to any prompt. Two adapter configurations updating 0.121% and 1.341% of parameters were compared.
**Key findings**:
- On a tunnel lining dataset, pixel IoU improved from 0.017 to 0.338 and instance-level recall from 0.375 to 0.672
- On the independent Structural Defects Dataset, pixel IoU improved from 0.017 to 0.855 and recall from 0.574 to 1.000
- Improvements were consistent across ten metrics on both datasets
- The largest per-category gains occurred where zero-shot competence was absent
- Hard-negative prompting addresses model collapse at no annotation cost
**Limitations**: not stated in abstract

### Mei et al. (2025)

**Research question**: How can SAM's promptable segmentation capabilities be extended to videos with minimal training cost?
**Methodology**: Introduces SAM-I2V, an image-to-video upgradation method with three key innovations: an image-to-video feature extraction upgrader built upon SAM's static image encoder, a memory filtering strategy that selects the most relevant past frames, and a memory-as-prompt mechanism leveraging object memory for temporally consistent mask propagation.
**Key findings**:
- Achieves over 90% of SAM 2's performance while using only 0.2% of its training cost
- Strategically upgrades pre-trained SAM to support promptable video segmentation, significantly reducing training complexity and resource requirements
- Enables spatiotemporal video perception and temporally consistent mask propagation in dynamic scenes
- Presents a resource-efficient pathway to PVS, lowering barriers for further research and broader applications
**Limitations**: not stated in abstract

### Pang et al. (2026)

**Research question**: How can a general-purpose hyperspectral foundation model be constructed despite limited high-resolution annotations and the need to reuse geometric priors from vision foundation models?
**Methodology**: HyperSAM couples a data-centric hyperspectral synthesis pipeline (generating full-spectrum hyperspectral cubes from SpaceNet multispectral imagery via physics-informed abundance-transfer with SAM3-derived pseudo-masks) with a spectral adaptation architecture based on SAM3, featuring a frozen RGB branch, trainable hyperspectral encoder, ControlNet-style feature injection, mixture-of-experts mask refiner, and Cross-modal Sample Selection for noisy-label weighting.
**Key findings**:
- HyperSAM obtains strong generalization on diverse hyperspectral tasks including classification, anomaly detection, change detection, target detection, and airborne oil-spill mapping
- High-quality synthetic data can be more effective than simply scaling noisy hyperspectral supervision
- The approach successfully reuses geometric and interactive priors from modern vision foundation models
- The spectral adaptation architecture with ControlNet-style injection enables effective hyperspectral learning
**Limitations**: not stated in abstract

### Stenhede et al. (2025)

**Research question**: How can we create an efficient 3D medical image segmentation model that performs well under limited data and computational budgets?
**Methodology**: Combines a SegResNet-based encoder with a prompt encoder and mask decoder in a U-Net-style architecture, using latent cross-attention, relative positional encoding, normalized attention, and the Muon optimizer. Trained from scratch on under 5,000 volumes from multiple modalities on a single 32 GB GPU in 6 hours.
**Key findings**:
- Outperforms two previously published baseline models (VISTA3D, SAM-Med3D) and matches the third (SegVol) in challenge evaluation on hidden test set
- Ranks 5th of 10 overall and best among approaches not utilizing pretrained weights in the coreset track
- Relative positional encodings and the Muon optimizer each substantially speed up convergence and improve segmentation quality
- Achieves DSC AUC of 2.404, NSD AUC of 2.266, final DSC of 0.627, and final NSD of 0.597
**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can segmentation foundation models be adapted to overcome insufficient annotation data and weak generalization in PET image segmentation?
**Methodology**: The authors constructed PETS-5k, the largest PET segmentation dataset with 5,731 3D whole-body PET images (over 1.3M 2D images), and developed SegAnyPET, a modality-specific 3D foundation model using cross prompting confident learning (CPCL) with uncertainty-guided self-rectification to learn from both high-quality and noisy labeled data.
**Key findings**:
- SegAnyPET can segment seen and unseen target organs using only one or a few prompt points
- The model outperforms state-of-the-art foundation models and task-specific fully supervised models
- SegAnyPET achieves higher accuracy and strong generalization ability for universal segmentation
- The CPCL strategy effectively handles discrepant annotation quality in PET imaging data
**Limitations**: not stated in abstract

## References

Chattopadhyay, S., Demir, B., & Niethammer, M. (2025). Zero-shot domain generalization of foundational models for 3D medical image segmentation: An experimental study. arXiv. https://arxiv.org/abs/2503.22862

Jalilian, S., & Bais, A. (2026). CLIP-guided SAM: Parameter-efficient semantic conditioning for promptable segmentation. arXiv. https://arxiv.org/abs/2605.24807

Jiang, C., Ding, T., Song, C., Tu, J., Yan, Z., Shao, Y., Wang, Z., Shang, Y., Han, T., & Tian, Y. (2026). Medical SAM3: A foundation model for universal prompt-driven medical image segmentation. arXiv. https://arxiv.org/abs/2601.10880

Li, X., Wu, Q., Ubaradka, A. S., Ding, Y., Que, C., Jiang, R., Xing, J., Wang, T., & Xu, M. (2025). AutoMiSeg: Automatic medical image segmentation via test-time adaptation of foundation models. arXiv. https://arxiv.org/abs/2505.17931

Magg, C., ter Wee, M. A., Dobbe, J. G. G., Streekstra, G. J., Blankevoort, L., Sánchez, C. I., & Kervadec, H. (2026). Prompting with the human-touch: Evaluating model-sensitivity of foundation models for musculoskeletal CT segmentation. arXiv. https://arxiv.org/abs/2603.10541

Malaisree, P., Youwai, S., Janrungautai, S., Amorndechaphon, D., Rojanavasu, P., & Songkitti, W. (2026). SAM3-LoRA: Parameter-efficient adaptation of a concept-promptable foundation model for multi-class structural defect segmentation. arXiv. https://arxiv.org/abs/2609.00469

Mei, H., Zhang, P., & Shou, M. Z. (2025). SAM-I2V: Upgrading SAM to support promptable video segmentation with less than 0.2% training cost. arXiv. https://arxiv.org/abs/2506.01304

Pang, L., Wu, X., Yao, J., Ghamisi, P., Zhou, J., Chen, Z., Meng, D., & Cao, X. (2026). HyperSAM: A promptable foundation model for hyperspectral remote sensing. arXiv. https://arxiv.org/abs/2609.37340

Stenhede, E., Bjørnstad, A. M., & Ranjbar, A. (2025). ENSAM: An efficient foundation model for interactive segmentation of 3D medical images. arXiv. https://arxiv.org/abs/2509.15874

Zhang, Y., Xue, L., Zhang, W., Li, L., Liu, Y., Jiang, C., Cheng, Y., & Qi, Y. (2025). SegAnyPET: Universal promptable segmentation from positron emission tomography images. arXiv. https://arxiv.org/abs/2502.14351
