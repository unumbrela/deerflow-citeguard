# Systematic Literature Review: Towards Open World Detection

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "open world detection", filtered to category cs.CV, published between 2023-08-22 and 2025-08-21
**Citation format**: APA 7th edition

## Executive Summary

The literature on open world detection has evolved significantly with the emergence of foundation models and vision-language pre-training. Recent work (2023-2025) demonstrates a clear shift from traditional open-set recognition approaches toward open-vocabulary detection paradigms that leverage large-scale vision-language models like CLIP. The surveyed papers collectively indicate that the field is moving beyond detecting predefined unknown categories toward truly generative, versatile detection systems capable of recognizing arbitrary objects through natural language prompts or visual examples. Key advances include real-time performance optimization, improved region-text alignment strategies, and the integration of foundation models for unknown object discovery. However, challenges remain in addressing label bias, maintaining computational efficiency, and establishing robust benchmarks that reflect real-world deployment scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "open world detection", filtered to category cs.CV, published between 2023-08-22 and 2025-08-21. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening Results**: The search identified 50 papers by phrase matching, expanded to 179 papers through citation analysis (129 added from references), shortlisted 30 papers, and screened 30 papers with relevance scores (4 papers scored 0, 6 scored 1, 15 scored 2, 5 scored 3), resulting in 10 included papers (7 from citation expansion).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Vision-Language Integration for Open-Vocabulary Detection

The integration of vision and language modalities has become the dominant paradigm for open-vocabulary object detection. Rather than relying on fixed category sets, these approaches enable detection through natural language queries, fundamentally changing how detectors generalize to novel objects. Cheng et al. (2024) introduced YOLO-World, which incorporates a Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) and region-text contrastive loss to facilitate interaction between visual and linguistic information. This approach enables the detector to recognize objects described by arbitrary text prompts, achieving 35.4 AP with 52.0 FPS on the LVIS dataset.

Similarly, Yao et al. (2024) extended this paradigm with DetCLIPv3, which not only performs open-vocabulary detection but also generates hierarchical labels for detected objects through an integrated caption head. Their auto-annotation pipeline uses visual large language models to produce rich multi-granular labels, achieving 47.0 zero-shot fixed AP on LVIS minival benchmark. The work demonstrates that open-vocabulary detectors can transcend predefined category sets to provide generative, descriptive outputs about detected objects.

Ren et al. (2024) further advanced this theme with Grounding DINO 1.5, scaling up architecture and training on over 20 million images to achieve 55.7 AP on LVIS-minival zero-shot transfer benchmark. The dual-model strategy—offering both a high-performance Pro variant and an efficient Edge variant optimized for deployment (75.2 FPS with TensorRT)—illustrates the maturation of vision-language detection systems toward practical applications.

### Theme 2: Efficient Region-Text Alignment Strategies

A critical technical challenge in open-vocabulary detection is establishing reliable alignment between visual regions and textual descriptions without relying on pre-trained vision-language models that may lack precise localization capabilities. Ma et al. (2023) reformulated region-word alignment as a co-occurrence guided discovery problem in CoDet, grouping images that mention shared concepts in captions and leveraging visual similarities to discover co-occurring objects aligned with those concepts. This approach achieved 37.0 AP^m_novel on OV-LVIS, surpassing previous state-of-the-art by 4.2 AP^m_novel, demonstrating that reliable alignment can be derived without pre-trained vision-language models.

Shi and Yang (2023) identified a different alignment challenge in EdaDet, observing that using CLIP for object-level alignment results in overfitting to base categories, particularly when novel categories are similar to base categories. They proposed Early Dense Alignment (EDA), which uses object-level supervision to learn dense-level rather than object-level alignment to maintain local fine-grained semantics. This approach improved novel box AP50 by +8.4% on COCO and +3.9% rare mask AP on LVIS under strict settings without external training resources, bridging the gap between generalizable local semantics and object-level prediction.

Zhao et al. (2024) addressed computational bottlenecks in transformer-based open-vocabulary detection with OmDet-Turbo, introducing an Efficient Fusion Head (EFH) module that achieves 100.2 FPS with TensorRT and language cache techniques while maintaining performance nearly on par with state-of-the-art supervised models in zero-shot scenarios. This work demonstrates that efficiency optimizations can enable real-time transformer-based detection without significant accuracy trade-offs.

### Theme 3: Foundation Models for Unknown Object Discovery

The integration of foundation models has opened new possibilities for detecting truly unknown objects—those not just unseen during training but entirely outside the predefined category space. Zohar et al. (2023) relaxed existing open world detection benchmark definitions to allow foundation models and curated a new benchmark with five real-world application-driven datasets, including challenging domains such as aerial and surgical images. Their proposed FOMO (Foundation Object detection Model for the Open world) identifies unknown objects based on shared attributes with known base objects, achieving approximately 3x unknown object mAP compared to baselines on the new benchmark. This work highlights that existing OWD benchmarks are insufficient for evaluating foundation model-based methods, as naive integration nearly saturates them.

Fang et al. (2023) addressed a complementary challenge in unknown object recognition: label bias that causes models to detect dissimilar regions as background rather than recognizing true unknown objects. Their unsupervised discriminative model learns to recognize true unknown objects from raw pseudo labels generated by unsupervised region proposal methods, followed by a classification-free self-training method that iteratively extends pseudo unknown objects to unlabeled regions. The method significantly outperformed prior state-of-the-art in detecting unknown objects on MS COCO dataset while maintaining competitive performance on known object classes, achieving better generalization ability on LVIS and Objects365 datasets.

### Theme 4: Prompt Synergy and Multi-Modal Flexibility

Recent work has explored synergizing different prompt modalities to overcome the limitations of single-modality approaches. Jiang et al. (2024) introduced T-Rex2, which combines text and visual prompts within a single model through contrastive learning, accepting inputs in diverse formats including text prompts, visual prompts, and combinations of both. This approach addresses the limitations of text prompts for rare or complex objects and visual prompts for abstract concepts, enabling the model to handle different scenarios by switching between text and visual prompt modalities. The synergy between prompt types allows T-Rex2 to exhibit remarkable zero-shot object detection capabilities across a wide spectrum of scenarios.

### Theme 5: Addressing Quality and Calibration in Open-Vocabulary Detection

Beyond architectural innovations, recent work has focused on improving the quality and calibration of open-vocabulary detection systems. Pham et al. (2023) identified a critical issue in CLIP-based open-vocabulary object detection methods: low-quality box proposals have misleading similarity scores because CLIP lacks exact object location information, resulting in the same similarity scores for low-quality and high-quality boxes. Their LP-OVOD method trains a sigmoid linear classifier on pseudo labels retrieved from top relevant region proposals to novel text, which discards low-quality boxes. This approach achieves 40.5 AP_novel on COCO dataset without requiring external datasets or knowledge of novel classes during training, outperforming state-of-the-art methods through improved proposal quality filtering.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that vision-language pre-training is essential for effective open-vocabulary detection. Multiple papers (Cheng et al., 2024; Yao et al., 2024; Ren et al., 2024) demonstrate that large-scale vision-language training enables zero-shot generalization to novel categories. There is also consensus that computational efficiency must be addressed for practical deployment, with multiple works (Zhao et al., 2024; Ren et al., 2024) achieving real-time performance through architectural optimizations. Additionally, papers agree that existing benchmarks require updating to reflect foundation model capabilities (Zohar et al., 2023).

**Disagreements**: The literature shows divergence in approaches to region-text alignment. Ma et al. (2023) argue that reliable alignment can be achieved without pre-trained vision-language models through co-occurrence guided discovery, while Shi and Yang (2023) demonstrate that CLIP-based alignment can be effective when properly modified with early dense alignment. There is also variation in whether to prioritize single-modality (text-only) prompts versus multi-modal prompt synergy, with Jiang et al. (2024) advocating for combined text-visual prompts while others focus on optimizing text-only approaches.

## Gaps and Open Questions

The collective literature reveals several gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting a need for more transparent discussion of failure modes and boundary conditions. Second, while several papers address efficiency (Zhao et al., 2024; Ren et al., 2024), there is limited work on energy efficiency and edge deployment beyond FPS optimization. Third, the new benchmark proposed by Zohar et al. (2023) includes only five datasets, indicating a need for more comprehensive, diverse evaluation benchmarks that span additional domains. Fourth, while multi-modal prompting shows promise (Jiang et al., 2024), there is limited exploration of how to optimally combine or weight different prompt modalities in various scenarios. Finally, the issue of label bias in unknown object detection (Fang et al., 2023) suggests that fundamental challenges remain in how models conceptualize and represent "unknown" categories versus background.

## Per-Paper Annotations

### Cheng et al. (2024)

**Research question**: How can YOLO detectors be enhanced with open-vocabulary detection capabilities to overcome their reliance on predefined object categories?

**Methodology**: The authors propose a Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) and region-text contrastive loss to facilitate interaction between visual and linguistic information, pre-trained on large-scale datasets.

**Key findings**:
- YOLO-World achieves 35.4 AP with 52.0 FPS on V100 on the LVIS dataset
- The method outperforms many state-of-the-art approaches in both accuracy and speed
- Fine-tuned YOLO-World demonstrates remarkable performance on object detection and open-vocabulary instance segmentation tasks
- The approach enables zero-shot detection of a wide range of objects with high efficiency

**Limitations**: not stated in abstract

### Fang et al. (2023)

**Research question**: How can open-world object detection models overcome label bias that causes them to detect dissimilar regions as background rather than recognizing true unknown objects?

**Methodology**: The authors propose an unsupervised discriminative model that learns to recognize true unknown objects from raw pseudo labels generated by unsupervised region proposal methods, followed by a classification-free self-training method that iteratively extends pseudo unknown objects to unlabeled regions.

**Key findings**:
- Current OWOD models suffer from label bias, tending to detect regions dissimilar to known objects as background
- The proposed method significantly outperforms prior state-of-the-art in detecting unknown objects on MS COCO dataset
- The method maintains competitive performance on known object classes while improving unknown detection
- The approach achieves better generalization ability on LVIS and Objects365 datasets

**Limitations**: not stated in abstract

### Jiang et al. (2024)

**Research question**: How can text and visual prompts be synergized to overcome their respective limitations and enable generic object detection across diverse scenarios?

**Methodology**: The authors introduce T-Rex2 that combines text and visual prompts within a single model through contrastive learning, accepting inputs in diverse formats including text prompts, visual prompts, and combinations of both.

**Key findings**:
- T-Rex2 exhibits remarkable zero-shot object detection capabilities across a wide spectrum of scenarios
- Text prompts and visual prompts benefit from each other within the synergy
- The model can handle different scenarios by switching between text and visual prompt modalities
- The approach addresses limitations of text prompts for rare/complex objects and visual prompts for abstract concepts

**Limitations**: not stated in abstract

### Ma et al. (2023)

**Research question**: How can reliable region-word alignment be derived for open-vocabulary object detection without relying on pre-trained or self-trained vision-language models?

**Methodology**: The authors reformulate region-word alignment as a co-occurring object discovery problem, grouping images that mention shared concepts in captions and leveraging visual similarities to discover co-occurring objects aligned with those concepts.

**Key findings**:
- CoDet achieves 37.0 AP^m_novel on OV-LVIS, surpassing previous SoTA by 4.2 AP^m_novel
- CoDet achieves 44.7 AP^m_all on OV-LVIS, surpassing previous SoTA by 9.8 AP^m_all
- The approach demonstrates superior performance and compelling scalability in open-vocabulary detection
- Performance improves when scaling up the visual backbone

**Limitations**: not stated in abstract

### Pham et al. (2023)

**Research question**: How can open-vocabulary object detection be improved to discard low-quality box proposals that have misleading similarity scores in CLIP-based text-image embeddings?

**Methodology**: The authors propose LP-OVOD, a method that trains a sigmoid linear classifier on pseudo labels retrieved from top relevant region proposals to novel text, which discards low-quality boxes. The approach is evaluated on COCO dataset using ResNet50 backbone without external datasets.

**Key findings**:
- CLIP-based OVOD methods suffer from low-quality boxes having the same similarity scores as high-quality boxes because CLIP lacks exact object location information
- LP-OVOD achieves 40.5 AP_novel on COCO dataset, outperforming state-of-the-art methods
- The method works without requiring external datasets or knowledge of novel classes during training

**Limitations**: not stated in abstract

### Ren et al. (2024)

**Research question**: How can open-set object detection models be advanced to achieve both stronger generalization capability and faster speed for edge deployment?

**Methodology**: The authors develop two models: Grounding DINO 1.5 Pro with scaled-up architecture and enhanced vision backbone trained on over 20 million images, and Grounding DINO 1.5 Edge optimized for efficiency with reduced feature scales but trained on the same comprehensive dataset.

**Key findings**:
- Grounding DINO 1.5 Pro achieves 54.3 AP on COCO detection benchmark
- Grounding DINO 1.5 Pro achieves 55.7 AP on LVIS-minival zero-shot transfer benchmark, setting new records
- Grounding DINO 1.5 Edge achieves 75.2 FPS with TensorRT optimization
- Grounding DINO 1.5 Edge attains 36.2 AP on LVIS-minival zero-shot benchmark

**Limitations**: not stated in abstract

### Shi and Yang (2023)

**Research question**: How can open-vocabulary object detection overcome overfitting to base categories and improve base-to-novel generalization when using CLIP for object-level alignment?

**Methodology**: The authors identify that loss of fine-grained local image semantics hinders generalization, and propose Early Dense Alignment (EDA) that uses object-level supervision to learn dense-level rather than object-level alignment to maintain local fine-grained semantics, evaluated on COCO and LVIS datasets.

**Key findings**:
- Using CLIP for object-level alignment results in overfitting to base categories, with novel categories similar to base categories performing particularly poorly
- Loss of critical fine-grained local image semantics hinders existing methods from attaining strong base-to-novel generalization
- EDA improves novel box AP50 by +8.4% on COCO and +3.9% rare mask AP on LVIS under strict settings without external training resources
- Early dense alignment bridges the gap between generalizable local semantics and object-level prediction

**Limitations**: not stated in abstract

### Yao et al. (2024)

**Research question**: How can open-vocabulary object detectors be extended beyond predefined category sets to also generate hierarchical labels for detected objects?

**Methodology**: The authors introduce a versatile model architecture integrating a caption head for generation, an auto-annotation pipeline using visual large language models for rich multi-granular labels, and an efficient two-stage training strategy with low-resolution pre-training followed by high-resolution fine-tuning.

**Key findings**:
- DetCLIPv3 achieves 47.0 zero-shot fixed AP on LVIS minival benchmark with Swin-T backbone
- Outperforms GLIPv2, GroundingDINO, and DetCLIPv2 by 18.0, 19.6, and 6.6 AP respectively
- Achieves state-of-the-art 19.7 AP in dense captioning task on VG dataset
- Demonstrates strong generative capability alongside open-vocabulary detection performance

**Limitations**: not stated in abstract

### Zhao et al. (2024)

**Research question**: How can transformer-based open-vocabulary detectors be optimized for real-time applications while maintaining competitive performance?

**Methodology**: The authors analyze limitations of OmDet and Grounding-DINO, then introduce OmDet-Turbo with an Efficient Fusion Head (EFH) module to address computational bottlenecks, evaluated with TensorRT and language cache techniques on COCO, LVIS, ODinW, and OVDEval benchmarks.

**Key findings**:
- OmDet-Turbo-Base achieves 100.2 FPS with TensorRT and language cache techniques applied
- The model achieves performance nearly on par with state-of-the-art supervised models in zero-shot scenarios on COCO and LVIS
- OmDet-Turbo establishes new state-of-the-art on ODinW (AP of 30.1) and OVDEval (NMS-AP of 26.86)
- The Efficient Fusion Head module successfully alleviates bottlenecks observed in OmDet and Grounding-DINO

**Limitations**: not stated in abstract

### Zohar et al. (2023)

**Research question**: How can open world object detection benchmarks and methods be adapted to effectively utilize pre-trained foundation models for detecting unknown objects?

**Methodology**: The authors relax existing OWD benchmark definitions to allow foundation models, curate a new benchmark with five real-world application-driven datasets (including aerial and surgical images), and propose FOMO (Foundation Object detection Model for the Open world) that identifies unknown objects based on shared attributes with known base objects.

**Key findings**:
- Existing OWD benchmarks are insufficient for evaluating foundation model-based methods, as naive integration nearly saturates them
- FOMO achieves approximately 3x unknown object mAP compared to baselines on the new benchmark
- The new benchmark includes challenging domains such as aerial and surgical images, establishing more realistic evaluation standards
- Results indicate significant room for improvement in scaling object detection to real-world domains

**Limitations**: not stated in abstract

## References

Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. arXiv. https://arxiv.org/abs/2401.17270

Fang, R., Pang, G., Zhou, L., Bai, X., & Zheng, J. (2023). Unsupervised recognition of unknown objects for open-world object detection. arXiv. https://arxiv.org/abs/2308.16527

Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., & Zhang, L. (2024). T-Rex2: Towards generic object detection via text-visual prompt synergy. arXiv. https://arxiv.org/abs/2403.14610

Ma, C., Jiang, Y., Wen, X., Yuan, Z., & Qi, X. (2023). CoDet: Co-occurrence guided region-word alignment for open-vocabulary object detection. arXiv. https://arxiv.org/abs/2310.16667

Pham, C., Vu, T., & Nguyen, K. (2023). LP-OVOD: Open-vocabulary object detection by linear probing. arXiv. https://arxiv.org/abs/2310.17109

Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., & Zhang, L. (2024). Grounding DINO 1.5: Advance the "edge" of open-set object detection. arXiv. https://arxiv.org/abs/2405.10300

Shi, C., & Yang, S. (2023). EdaDet: Open-vocabulary object detection using early dense alignment. arXiv. https://arxiv.org/abs/2309.01151

Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., & Xu, D. (2024). DetCLIPv3: Towards versatile generative open-vocabulary object detection. arXiv. https://arxiv.org/abs/2404.09216

Zhao, T., Liu, P., He, X., Zhang, L., & Lee, K. (2024). Real-time transformer-based open-vocabulary detection with efficient fusion head. arXiv. https://arxiv.org/abs/2403.06892

Zohar, O., Lozano, A., Goel, S., Yeung, S., & Wang, K.-C. (2023). Open world object detection in the era of foundation models. arXiv. https://arxiv.org/abs/2312.05745
