# Systematic Literature Review: Towards Open World Detection

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "open world detection", filtered to category cs.CV, published between 2023-08-22 and 2025-08-21
**Citation format**: APA 7th edition

## Executive Summary

The field of open world detection has undergone significant transformation between 2023 and 2025, with research shifting from traditional open-set recognition approaches toward leveraging foundation models and vision-language pre-training. The ten surveyed papers reveal a clear trend: modern open world detection systems increasingly rely on large-scale pre-trained models like CLIP and vision-language architectures to achieve zero-shot generalization to unseen categories. Key advances include real-time open-vocabulary detection capabilities, improved region-text alignment strategies, and the integration of generative capabilities alongside detection. However, challenges remain in handling unknown object recognition without label bias, achieving efficient deployment at the edge, and establishing benchmarks that properly evaluate foundation model-based approaches.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "open world detection", filtered to category cs.CV, published between 2023-08-22 and 2025-08-21. Papers were sorted by co-citation relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening results**: The search identified 50 papers by keyword matching, with an additional 129 papers added through citation expansion from the candidate pool. From a shortlist of 30 papers, 10 were selected based on centrality to the open world detection topic, with 7 of these coming from the citation expansion phase.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. All metadata is derived solely from abstract content, which may not capture full methodological details or limitations.

## Themes

### Theme 1: Vision-Language Pre-training for Open-Vocabulary Detection

A dominant direction in open world detection research involves leveraging vision-language pre-trained models, particularly CLIP, to enable detection of objects beyond predefined categories. This approach addresses the fundamental limitation of traditional detectors that can only recognize classes seen during training.

Cheng et al. (2024) introduced YOLO-World, which integrates a Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) with region-text contrastive loss to facilitate interaction between visual and linguistic information. Their approach achieves 35.4 AP with 52.0 FPS on the LVIS dataset, demonstrating that YOLO detectors can be enhanced with open-vocabulary capabilities while maintaining real-time performance. Similarly, Pham et al. (2023) proposed LP-OVOD, which uses joint text-image embeddings from CLIP to assign box proposals to their closest text label through linear probing, achieving 40.5 AP_novel on COCO without requiring external datasets.

Shi and Yang (2023) identified a critical limitation in existing CLIP-based approaches: using object-level alignment results in overfitting to base categories, particularly harming performance on novel categories similar to base categories. Their Early Dense Alignment (EDA) approach addresses this by learning dense-level rather than object-level alignment, improving novel box AP50 by 8.4% on COCO.

### Theme 2: Real-Time and Edge Deployment

As open-vocabulary detection models grow more sophisticated, a significant research thread focuses on making these systems practical for real-world deployment through optimization for speed and efficiency.

Zhao et al. (2024) analyzed limitations of transformer-based models like OmDet and Grounding-DINO, introducing OmDet-Turbo with an Efficient Fusion Head (EFH) module to alleviate computational bottlenecks. Using TensorRT and language cache techniques, their model achieves 100.2 FPS while maintaining near state-of-the-art performance, establishing new benchmarks on ODinW (AP of 30.1) and OVDEval (NMS-AP of 26.86).

Ren et al. (2024) developed a dual-strategy approach with Grounding DINO 1.5, offering both a Pro model scaled up for maximum performance (54.3 AP on COCO, 55.7 AP on LVIS-minival zero-shot) and an Edge model optimized for efficiency (75.2 FPS with TensorRT while maintaining 36.2 AP on LVIS-minival). This suite provides options for both high-performance and edge computing scenarios, acknowledging that different deployment contexts require different trade-offs.

### Theme 3: Enhanced Region-Text Alignment Strategies

Improving how visual regions align with textual descriptions emerges as a critical challenge across multiple papers, with various strategies proposed to overcome limitations in existing alignment mechanisms.

Ma et al. (2023) reformulated region-word alignment as a co-occurring object discovery problem rather than relying on pre-aligned vision-language models. Their CoDet approach groups images that mention shared concepts in captions and leverages visual similarities to discover co-occurring objects, achieving 37.0 AP^m_novel and 44.7 AP^m_all on OV-LVIS—surpassing previous state-of-the-art by 4.2 and 9.8 AP respectively.

Jiang et al. (2024) introduced T-Rex2, which synergizes text and visual prompts within a single model through contrastive learning. This approach addresses data scarcity and descriptive limitations of text-only methods while conveying abstract concepts better than visual-only methods, enabling the model to handle different scenarios by switching between prompt modalities.

### Theme 4: Foundation Models and Benchmark Evolution

The advent of foundation models has fundamentally challenged existing benchmark definitions and evaluation protocols for open world detection, requiring new approaches to both methodology and assessment.

Zohar et al. (2023) demonstrated that existing OWD benchmarks are insufficient for evaluating foundation model-based methods, as naive integration of foundation models nearly saturates them. They curated a new benchmark with five real-world application-driven datasets including aerial and surgical images, and introduced FOMO (Foundation Object detection Model for the Open world) that identifies unknown objects based on shared attributes with base known objects, achieving approximately 3x unknown object mAP compared to baselines.

Yao et al. (2024) extended open-vocabulary detectors beyond detection to generation, introducing DetCLIPv3 with a caption head for hierarchical label generation. Their auto-annotation pipeline uses visual large language models for rich multi-granular labels, achieving 47.0 zero-shot fixed AP on LVIS minival—outperforming GLIPv2, GroundingDINO, and DetCLIPv2 by 18.0, 19.6, and 6.6 AP respectively.

### Theme 5: Unsupervised Unknown Object Recognition

A persistent challenge in open world detection is recognizing truly unknown objects without label bias, where models tend to classify dissimilar regions as background rather than as unknown objects.

Fang et al. (2023) proposed an unsupervised discriminative model that learns to recognize true unknown objects from raw pseudo labels generated by unsupervised region proposal methods. Their classification-free self-training method iteratively extends pseudo unknown objects to unlabeled regions, significantly outperforming prior state-of-the-art in detecting unknown objects on MS COCO while maintaining competitive performance for known classes and achieving better generalization on LVIS and Objects365 datasets.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively demonstrate strong agreement on several points. First, all approaches acknowledge that traditional closed-set detection paradigms are fundamentally inadequate for open world scenarios. Second, there is consensus that vision-language pre-training, particularly using CLIP-style embeddings, provides a crucial foundation for zero-shot generalization (Cheng et al., 2024; Pham et al., 2023; Shi & Yang, 2023). Third, multiple papers converge on the importance of region-text alignment quality as a determining factor for open-vocabulary detection performance (Ma et al., 2023; Jiang et al., 2024; Shi & Yang, 2023). Finally, there is agreement that real-world deployment requires careful attention to computational efficiency, not just accuracy (Zhao et al., 2024; Ren et al., 2024).

**Disagreements**: The literature reveals tensions in how to best leverage foundation models. Zohar et al. (2023) argue that existing benchmarks must be fundamentally redefined to properly evaluate foundation model-based methods, while other papers continue to report results on traditional benchmarks like COCO and LVIS without questioning their validity. Additionally, there is disagreement about the role of external training data: Pham et al. (2023) emphasize achieving strong results "without requiring external datasets," while Yao et al. (2024) and Ren et al. (2024) leverage large-scale training datasets with over 20 million images. The optimal balance between dataset scale and methodological innovation remains unresolved.

## Gaps and Open Questions

Several critical gaps emerge from the collective limitations of the surveyed literature:

**Evaluation methodology**: Zohar et al. (2023) highlight that current benchmarks fail to properly evaluate foundation model capabilities, yet no consensus exists on what constitutes appropriate evaluation protocols for open world detection in the foundation model era.

**Unknown object handling**: While Fang et al. (2023) address label bias in unknown object recognition, none of the surveyed papers provide comprehensive solutions for distinguishing between unknown objects that should be detected versus background clutter that should be ignored—a critical requirement for real-world deployment.

**Computational efficiency trade-offs**: Although multiple papers address real-time performance (Zhao et al., 2024; Ren et al., 2024; Cheng et al., 2024), the abstracts do not specify the computational resources required for training these models, leaving unclear whether the efficiency gains at inference time come at the cost of prohibitive training requirements.

**Generalization limits**: None of the papers explicitly address the fundamental limits of open world detection—what categories or object types remain inherently undetectable even with foundation models, and what theoretical boundaries exist for zero-shot generalization.

**Integration with downstream tasks**: While Yao et al. (2024) begin to address generation capabilities, the literature largely treats detection as an end goal rather than considering how open world detection integrates with downstream reasoning, planning, or decision-making systems.

## Per-Paper Annotations

### Cheng et al. (2024)

**Research question**: How can YOLO detectors be enhanced with open-vocabulary detection capabilities to detect objects beyond predefined categories?

**Methodology**: The authors propose a Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) and region-text contrastive loss to facilitate interaction between visual and linguistic information, pre-trained on large-scale datasets.

**Key findings**:
- YOLO-World achieves 35.4 AP with 52.0 FPS on V100 on the LVIS dataset
- The method outperforms many state-of-the-art methods in both accuracy and speed
- Fine-tuned YOLO-World achieves remarkable performance on object detection and open-vocabulary instance segmentation tasks
- The approach enables zero-shot detection of a wide range of objects with high efficiency

**Limitations**: Not stated in abstract

### Fang et al. (2023)

**Research question**: How can the label bias problem in open-world object detection be eliminated, where models tend to detect dissimilar regions as background rather than unknown objects?

**Methodology**: The authors propose an unsupervised discriminative model that learns to recognize true unknown objects from raw pseudo labels generated by unsupervised region proposal methods, followed by a classification-free self-training method that iteratively extends pseudo unknown objects to unlabeled regions.

**Key findings**:
- The method significantly outperforms prior state-of-the-art in detecting unknown objects on MS COCO dataset
- The approach maintains competitive performance for detecting known object classes
- The method achieves better generalization ability on LVIS and Objects365 datasets
- The approach eliminates label bias that causes models to detect dissimilar regions as background

**Limitations**: Not stated in abstract

### Jiang et al. (2024)

**Research question**: How can text and visual prompts be synergized to overcome their individual limitations and enable generic object detection across diverse scenarios?

**Methodology**: The authors introduce T-Rex2 that synergizes text and visual prompts within a single model through contrastive learning, accepting inputs in diverse formats including text prompts, visual prompts, and combinations of both.

**Key findings**:
- T-Rex2 exhibits remarkable zero-shot object detection capabilities across a wide spectrum of scenarios
- Text prompts and visual prompts benefit from each other within the synergy
- The model can handle different scenarios by switching between text and visual prompt modalities
- The approach addresses data scarcity and descriptive limitations of text-only methods while conveying abstract concepts better than visual-only methods

**Limitations**: Not stated in abstract

### Ma et al. (2023)

**Research question**: How can reliable region-word alignment be achieved for open-vocabulary object detection without relying on pre-aligned vision-language models?

**Methodology**: The authors reformulate region-word alignment as a co-occurring object discovery problem, grouping images that mention shared concepts in captions and leveraging visual similarities to discover co-occurring objects and align them with shared concepts.

**Key findings**:
- CoDet achieves 37.0 AP^m_novel and 44.7 AP^m_all on OV-LVIS by scaling up the visual backbone
- Surpasses previous state-of-the-art by 4.2 AP^m_novel and 9.8 AP^m_all
- The approach demonstrates superior performance and compelling scalability in open-vocabulary detection
- The method overcomes limitations in localization accuracy and generalization capabilities of existing approaches

**Limitations**: Not stated in abstract

### Pham et al. (2023)

**Research question**: How can open-vocabulary object detection be improved to handle low-quality box proposals that have similar similarity scores as high-quality boxes in CLIP-based embeddings?

**Methodology**: The authors propose LP-OVOD, a method that trains a sigmoid linear classifier on pseudo labels retrieved from top relevant region proposals to novel text, which discards low-quality boxes. The approach uses joint text-image embeddings of CLIP to assign box proposals to their closest text label.

**Key findings**:
- LP-OVOD achieves 40.5 in AP_novel on COCO dataset using ResNet50 as backbone
- The method outperforms state-of-the-art approaches without requiring external datasets
- The approach does not need knowledge of novel classes during training
- The method successfully discards low-quality boxes (over- and under-covered-object boxes)

**Limitations**: Not stated in abstract

### Ren et al. (2024)

**Research question**: How can open-set object detection models be advanced to achieve both stronger generalization capability and faster speed for edge deployment?

**Methodology**: The authors develop two models: Grounding DINO 1.5 Pro with scaled-up architecture and enhanced vision backbone trained on over 20 million images, and Grounding DINO 1.5 Edge optimized for efficiency with reduced feature scales but trained on the same comprehensive dataset.

**Key findings**:
- Grounding DINO 1.5 Pro achieves 54.3 AP on COCO detection benchmark
- Grounding DINO 1.5 Pro achieves 55.7 AP on LVIS-minival zero-shot transfer benchmark, setting new records
- Grounding DINO 1.5 Edge achieves 75.2 FPS with TensorRT optimization while maintaining 36.2 AP on LVIS-minival
- The suite provides options for both high-performance and edge computing scenarios

**Limitations**: Not stated in abstract

### Shi and Yang (2023)

**Research question**: How can open-vocabulary object detection avoid overfitting to base categories and improve base-to-novel generalization?

**Methodology**: The authors identify that loss of fine-grained local image semantics hinders generalization and propose Early Dense Alignment (EDA), which uses object-level supervision to learn dense-level rather than object-level alignment to maintain local fine-grained semantics.

**Key findings**:
- Using CLIP for object-level alignment results in overfitting to base categories
- Novel categories similar to base categories have particularly poor performance with existing methods
- EDA improves novel box AP50 by +8.4% on COCO dataset
- EDA improves rare mask AP by +3.9% on LVIS dataset without external training resources

**Limitations**: Not stated in abstract

### Yao et al. (2024)

**Research question**: How can open-vocabulary object detectors be extended to not only detect but also generate hierarchical labels for detected objects?

**Methodology**: The authors introduce a versatile model architecture integrating a caption head for generation ability, an auto-annotation pipeline using visual large language models for rich multi-granular labels, and an efficient two-stage training strategy with low-resolution pre-training followed by high-resolution fine-tuning.

**Key findings**:
- DetCLIPv3 achieves 47.0 zero-shot fixed AP on LVIS minival benchmark with Swin-T backbone
- Outperforms GLIPv2, GroundingDINO, and DetCLIPv2 by 18.0/19.6/6.6 AP respectively
- Achieves state-of-the-art 19.7 AP in dense captioning task on VG dataset
- The model demonstrates both superior open-vocabulary detection and strong generative capability

**Limitations**: Not stated in abstract

### Zhao et al. (2024)

**Research question**: How can transformer-based open-vocabulary detectors be optimized for real-time applications while maintaining competitive performance?

**Methodology**: The authors analyze limitations of OmDet and Grounding-DINO models and introduce OmDet-Turbo with an Efficient Fusion Head (EFH) module to alleviate computational bottlenecks, using TensorRT and language cache techniques to achieve real-time inference speeds.

**Key findings**:
- OmDet-Turbo-Base achieves 100.2 FPS with TensorRT and language cache techniques
- The model achieves near state-of-the-art performance in zero-shot scenarios on COCO and LVIS datasets
- New state-of-the-art benchmarks established on ODinW (AP of 30.1) and OVDEval (NMS-AP of 26.86)
- The approach demonstrates practical viability for industrial real-time object detection applications

**Limitations**: Not stated in abstract

### Zohar et al. (2023)

**Research question**: How can pre-trained foundation models be utilized in open world object detection when existing benchmark definitions prohibit their use?

**Methodology**: The authors relax existing OWD benchmark and task definitions to enable foundation model utilization, curate a new benchmark with five real-world application-driven datasets (including aerial and surgical images), and introduce FOMO (Foundation Object detection Model for the Open world) that identifies unknown objects based on shared attributes with base known objects.

**Key findings**:
- Existing benchmarks are insufficient for evaluating foundation model-based methods as naive integration nearly saturates them
- FOMO achieves approximately 3x unknown object mAP compared to baselines on the new benchmark
- The new benchmark includes challenging domains such as aerial and surgical images
- Results indicate significant room for improvement in scaling object detection to real-world domains

**Limitations**: Not stated in abstract

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
