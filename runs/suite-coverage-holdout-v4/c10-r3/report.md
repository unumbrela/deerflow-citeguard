# Systematic Literature Review: Towards Open World Detection

**Review Period:** August 22, 2023 – August 21, 2025  
**Domain:** Computer Vision (cs.CV)  
**Format:** APA Style  
**Date:** October 26, 2026

---

## Executive Summary

This systematic literature review examines 10 pivotal papers on open world detection published between August 2023 and August 2025. The field has witnessed remarkable progress through the integration of vision-language models, foundation models, and real-time detection architectures. Key trends include the shift from closed-set to open-vocabulary detection, the emergence of text-visual prompt synergy, and the development of efficient models suitable for edge deployment. The reviewed papers demonstrate significant advances in zero-shot detection capabilities, with particular emphasis on handling unknown objects, reducing label bias, and improving generalization across diverse domains.

---

## Annotated Bibliography (APA Format)

### 1. YOLO-World: Real-Time Open-Vocabulary Object Detection

**Citation:**  
Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. *arXiv preprint arXiv:2401.17270*. https://arxiv.org/abs/2401.17270v3

**Summary:**  
This paper introduces YOLO-World, which enhances the YOLO detection series with open-vocabulary capabilities through vision-language modeling. The authors propose a Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) and region-text contrastive loss to facilitate vision-language interaction. The method achieves 35.4 AP at 52.0 FPS on the LVIS dataset, outperforming state-of-the-art methods in both accuracy and speed.

**Key Contributions:**
- Novel RepVL-PAN architecture for vision-language fusion
- Region-text contrastive loss for zero-shot detection
- Real-time performance (52.0 FPS) with competitive accuracy (35.4 AP on LVIS)
- Strong performance on downstream tasks including open-vocabulary instance segmentation

**Relevance to Open World Detection:**  
YOLO-World addresses the limitation of predefined categories in traditional YOLO detectors, enabling detection of arbitrary objects through natural language queries. This represents a significant step toward practical open world deployment.

---

### 2. DetCLIPv3: Towards Versatile Generative Open-vocabulary Object Detection

**Citation:**  
Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., & Xu, D. (2024). DetCLIPv3: Towards versatile generative open-vocabulary object detection. *arXiv preprint arXiv:2404.09216*. https://arxiv.org/abs/2404.09216v1

**Summary:**  
DetCLIPv3 introduces a high-performing detector capable of both open-vocabulary object detection and generating hierarchical labels for detected objects. The model features three core designs: versatile architecture with caption head integration, high information density data through auto-annotation pipelines, and an efficient two-stage training strategy. The Swin-T backbone model achieves 47.0 zero-shot fixed AP on LVIS minival, outperforming GLIPv2, GroundingDINO, and DetCLIPv2 by significant margins.

**Key Contributions:**
- Generative capability through integrated caption head
- Auto-annotation pipeline leveraging visual large language models
- Two-stage training: low-resolution pre-training followed by high-resolution fine-tuning
- State-of-the-art 19.7 AP on dense captioning task (VG dataset)

**Relevance to Open World Detection:**  
DetCLIPv3 extends beyond detection to provide rich semantic descriptions, enabling more nuanced understanding of novel objects in open world scenarios.

---

### 3. Grounding DINO 1.5: Advance the "Edge" of Open-Set Object Detection

**Citation:**  
Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., & Zhang, L. (2024). Grounding DINO 1.5: Advance the "edge" of open-set object detection. *arXiv preprint arXiv:2405.10300*. https://arxiv.org/abs/2405.10300v2

**Summary:**  
This paper presents Grounding DINO 1.5 suite with two models: Pro (high-performance) and Edge (efficient). The Pro model features scaled architecture, enhanced vision backbone, and training on over 20 million grounding-annotated images. The Edge model maintains robust detection with reduced feature scales for faster deployment. Grounding DINO 1.5 Pro achieves 54.3 AP on COCO and 55.7 AP on LVIS-minival zero-shot, while the Edge model reaches 75.2 FPS with TensorRT optimization.

**Key Contributions:**
- Dual-model strategy addressing performance and efficiency trade-offs
- Massive training dataset (20M+ images) for rich semantic understanding
- Record-breaking zero-shot performance (55.7 AP on LVIS-minival)
- Edge-optimized deployment with 75.2 FPS inference speed

**Relevance to Open World Detection:**  
Grounding DINO 1.5 demonstrates that scaling model architecture and training data significantly improves open-set generalization, while providing practical deployment options for edge scenarios.

---

### 4. T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy

**Citation:**  
Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., & Zhang, L. (2024). T-Rex2: Towards generic object detection via text-visual prompt synergy. *arXiv preprint arXiv:2403.14610*. https://arxiv.org/abs/2403.14610v1

**Summary:**  
T-Rex2 addresses limitations of text-only and visual-only prompts by synergizing both modalities within a single model through contrastive learning. Text prompts excel at abstract concepts but struggle with rare objects, while visual prompts provide concrete examples but lack abstract representation. T-Rex2 accepts diverse input formats (text, visual, or combined) and switches between modalities based on scenario requirements.

**Key Contributions:**
- Text-visual prompt synergy through contrastive learning
- Flexible input handling for diverse scenarios
- Remarkable zero-shot capabilities across wide spectrum of scenarios
- Complementary strengths addressing data scarcity and descriptive limitations

**Relevance to Open World Detection:**  
T-Rex2's multimodal approach enables more robust detection of novel objects by leveraging both linguistic abstraction and visual concreteness, crucial for open world applications.

---

### 5. Open World Object Detection in the Era of Foundation Models

**Citation:**  
Zohar, O., Lozano, A., Goel, S., Yeung, S., & Wang, K.-C. (2023). Open world object detection in the era of foundation models. *arXiv preprint arXiv:2312.05745*. https://arxiv.org/abs/2312.05745v1

**Summary:**  
This paper examines the utilization of pre-trained foundation models in open world object detection (OWD). The authors demonstrate that existing benchmarks are insufficient for evaluating foundation model-based methods, as naive integration nearly saturates current benchmarks. They introduce a new benchmark with five real-world application-driven datasets (including aerial and surgical images) and propose FOMO (Foundation Object detection Model for the Open world), which identifies unknown objects based on shared attributes with known objects. FOMO achieves ~3× unknown object mAP compared to baselines.

**Key Contributions:**
- Critical analysis of benchmark limitations for foundation models
- New challenging benchmark with five application-driven datasets
- FOMO method leveraging shared attributes for unknown object detection
- ~3× improvement in unknown object mAP over baselines

**Relevance to Open World Detection:**  
This work addresses the critical gap between OWD research and real-world deployment, providing more rigorous evaluation frameworks and demonstrating foundation models' potential for handling novel objects.

---

### 6. Unsupervised Recognition of Unknown Objects for Open-World Object Detection

**Citation:**  
Fang, R., Pang, G., Zhou, L., Bai, X., & Zheng, J. (2023). Unsupervised recognition of unknown objects for open-world object detection. *arXiv preprint arXiv:2308.16527*. https://arxiv.org/abs/2308.16527v1

**Summary:**  
This paper addresses the label bias problem in current OWOD models, which tend to detect dissimilar regions as background. The authors propose learning an unsupervised discriminative model to recognize true unknown objects from raw pseudo labels generated by unsupervised region proposal methods. The model is refined through classification-free self-training that iteratively extends pseudo unknown objects to unlabeled regions. The method significantly outperforms prior SOTA in unknown object detection while maintaining competitive known object performance on MS COCO, with better generalization on LVIS and Objects365.

**Key Contributions:**
- Unsupervised discriminative model for unknown object recognition
- Classification-free self-training for iterative pseudo-label extension
- Elimination of label bias toward known object features
- Superior generalization across multiple datasets (COCO, LVIS, Objects365)

**Relevance to Open World Detection:**  
This work directly addresses the fundamental challenge of unknown object detection without relying on known object supervision, crucial for true open world deployment.

---

### 7. Real-time Transformer-based Open-Vocabulary Detection with Efficient Fusion Head

**Citation:**  
Zhao, T., Liu, P., He, X., Zhang, L., & Lee, K. (2024). Real-time transformer-based open-vocabulary detection with efficient fusion head. *arXiv preprint arXiv:2403.06892*. https://arxiv.org/abs/2403.06892v2

**Summary:**  
This paper introduces OmDet-Turbo, addressing computational bottlenecks in transformer-based open-vocabulary detectors. The innovative Efficient Fusion Head (EFH) module alleviates limitations observed in OmDet and Grounding-DINO. OmDet-Turbo-Base achieves 100.2 FPS with TensorRT and language cache techniques, while maintaining near state-of-the-art zero-shot performance on COCO and LVIS. The model establishes new benchmarks on ODinW (30.1 AP) and OVDEval (26.86 NMS-AP).

**Key Contributions:**
- Efficient Fusion Head (EFH) for real-time transformer-based detection
- 100.2 FPS inference speed with competitive accuracy
- New state-of-the-art on ODinW and OVDEval benchmarks
- Practical industrial applicability through speed-accuracy balance

**Relevance to Open World Detection:**  
OmDet-Turbo demonstrates that real-time performance is achievable for open-vocabulary detection, enabling practical deployment in time-critical applications.

---

### 8. EdaDet: Open-Vocabulary Object Detection Using Early Dense Alignment

**Citation:**  
Shi, C., & Yang, S. (2023). EdaDet: Open-vocabulary object detection using early dense alignment. *arXiv preprint arXiv:2309.01151*. https://arxiv.org/abs/2309.01151v1

**Summary:**  
This paper identifies that using CLIP for object-level alignment results in overfitting to base categories, particularly for novel categories similar to base categories. The authors propose Early Dense Alignment (EDA) to bridge the gap between generalizable local semantics and object-level prediction. EDA uses object-level supervision to learn dense-level rather than object-level alignment, maintaining local fine-grained semantics. The method improves novel box AP50 by +8.4% on COCO and rare mask AP by +3.9% on LVIS without external training resources.

**Key Contributions:**
- Early Dense Alignment (EDA) for preserving fine-grained local semantics
- Dense-level alignment instead of object-level alignment
- Significant improvement in base-to-novel generalization (+8.4% novel AP50 on COCO)
- No external training resources required

**Relevance to Open World Detection:**  
EdaDet addresses the critical challenge of base-to-novel generalization, ensuring that novel objects similar to known categories are not misclassified.

---

### 9. CLIPSelf: Vision Transformer Distills Itself for Open-Vocabulary Dense Prediction

**Citation:**  
Wu, S., Zhang, W., Xu, L., Jin, S., Li, X., Liu, W., & Loy, C. C. (2023). CLIPSelf: Vision transformer distills itself for open-vocabulary dense prediction. *arXiv preprint arXiv:2310.01403*. https://arxiv.org/abs/2310.01403v2

**Summary:**  
This paper analyzes the region-language alignment in CLIP models and identifies domain shift from full images to local image regions as a key limitation. CLIPSelf adapts CLIP ViT's image-level recognition ability to local regions without requiring region-text pairs. The approach empowers ViTs to distill themselves by aligning region representations from dense feature maps with image-level representations of corresponding image crops. CLIPSelf achieves state-of-the-art performance on open-vocabulary object detection, semantic segmentation, and panoptic segmentation across various benchmarks.

**Key Contributions:**
- Self-distillation approach for region-language alignment
- No requirement for region-text pairs
- Domain shift mitigation from image-level to region-level
- State-of-the-art across multiple dense prediction tasks

**Relevance to Open World Detection:**  
CLIPSelf enables transfer of CLIP's powerful vision-language alignment to local regions, essential for detecting novel objects without extensive region-level annotations.

---

### 10. OV-DINO: Unified Open-Vocabulary Detection with Language-Aware Selective Fusion

**Citation:**  
Wang, H., Ren, P., Jie, Z., Dong, X., Feng, C., Qian, Y., Ma, L., Jiang, D., Wang, Y., Lan, X., & Liang, X. (2024). OV-DINO: Unified open-vocabulary detection with language-aware selective fusion. *arXiv preprint arXiv:2407.07844*. https://arxiv.org/abs/2407.07844v2

**Summary:**  
OV-DINO addresses two main challenges in open-vocabulary detection: eliminating data noise from pseudo-labeling and efficiently leveraging language-aware capability for region-level cross-modality fusion. The method introduces Unified Data Integration (UniDI) pipeline for end-to-end training and noise elimination, and Language-Aware Selective Fusion (LASF) module for enhanced cross-modality alignment through language-aware query selection and fusion. OV-DINO achieves 50.6% AP on COCO and 40.1% on LVIS in zero-shot manner, with 58.4% AP when fine-tuned on COCO.

**Key Contributions:**
- Unified Data Integration (UniDI) pipeline for noise elimination
- Language-Aware Selective Fusion (LASF) module
- State-of-the-art zero-shot performance (50.6% AP on COCO, 40.1% on LVIS)
- Strong fine-tuned performance (58.4% AP on COCO)

**Relevance to Open World Detection:**  
OV-DINO's unified framework effectively handles data quality issues and enhances cross-modality alignment, critical for robust open-vocabulary detection in diverse scenarios.

---

## Thematic Analysis

### Theme 1: Vision-Language Model Integration

Six of the ten reviewed papers leverage vision-language models (YOLO-World, DetCLIPv3, Grounding DINO 1.5, T-Rex2, EdaDet, CLIPSelf, OV-DINO) to enable open-vocabulary capabilities. The consistent finding is that pre-trained vision-language models provide strong zero-shot generalization, with CLIP-based approaches being particularly prominent. The key innovation across these works is the adaptation of image-level vision-language alignment to region-level detection tasks.

**Key Insight:** Vision-language pre-training provides the semantic foundation for open world detection, but requires careful adaptation to avoid domain shift and preserve fine-grained local semantics.

### Theme 2: Real-Time Performance and Efficiency

Three papers explicitly address computational efficiency (YOLO-World: 52.0 FPS, Grounding DINO 1.5 Edge: 75.2 FPS, OmDet-Turbo: 100.2 FPS). This represents a significant shift from accuracy-focused research to practical deployment considerations. The Efficient Fusion Head in OmDet-Turbo and the Edge model in Grounding DINO 1.5 demonstrate that real-time performance is achievable without substantial accuracy sacrifice.

**Key Insight:** Real-time open-vocabulary detection is now feasible, enabling deployment in robotics, autonomous systems, and edge computing applications.

### Theme 3: Unknown Object Detection and Label Bias

Two papers directly address the fundamental challenge of unknown object detection (FOMO, Fang et al.). The label bias problem—where models classify dissimilar regions as background—remains a critical limitation. The unsupervised approaches proposed demonstrate significant improvements (~3× mAP for FOMO) by learning discriminative models without known object supervision.

**Key Insight:** True open world detection requires moving beyond known object supervision to unsupervised unknown object recognition.

### Theme 4: Benchmark Evolution and Foundation Models

Zohar et al. critically examine existing benchmarks, demonstrating they are insufficient for evaluating foundation model-based methods. The introduction of application-driven datasets (aerial, surgical images) reflects the field's maturation toward real-world deployment scenarios. This suggests that future research should focus on domain-specific challenges rather than generic benchmarks.

**Key Insight:** Benchmark design must evolve to match the capabilities of foundation models and reflect real-world application requirements.

### Theme 5: Multimodal Prompt Synergy

T-Rex2's text-visual prompt synergy represents an emerging direction recognizing the complementary strengths of different prompt modalities. This approach addresses the limitations of text-only prompts for rare objects and visual-only prompts for abstract concepts.

**Key Insight:** Multimodal prompting enables more flexible and robust open world detection across diverse scenarios.

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Incremental Learning:** While several papers mention incremental learning capabilities, few provide rigorous evaluation of continuous learning scenarios where new objects are discovered and learned over time.

2. **Domain Adaptation:** Most methods are evaluated on COCO and LVIS, with limited investigation of domain shift in real-world applications (medical, aerial, industrial).

3. **Computational Efficiency Trade-offs:** While real-time methods exist, the accuracy-efficiency Pareto frontier is not systematically explored across different model scales.

4. **Unknown Object Characterization:** Current methods detect unknown objects but provide limited semantic understanding or characterization of what makes them "unknown."

5. **Evaluation Metrics:** Existing metrics (AP, zero-shot AP) may not adequately capture open world detection performance, particularly for unknown object discovery and incremental learning.

### Future Research Directions

1. **Unified Frameworks:** Integration of detection, segmentation, and captioning in unified models (as initiated by DetCLIPv3) for comprehensive scene understanding.

2. **Active Learning for Open World:** Developing active learning strategies where models can query human annotation for the most informative unknown objects.

3. **Cross-Modal Reasoning:** Advancing beyond alignment to enable reasoning about relationships between known and unknown objects.

4. **Lifelong Learning:** Addressing catastrophic forgetting in continuous open world deployment scenarios.

5. **Benchmark Standardization:** Establishing comprehensive benchmarks that evaluate both known and unknown object detection, incremental learning, and real-world applicability.

---

## Conclusion

The reviewed literature demonstrates remarkable progress in open world detection from 2023 to 2025. Key advances include:

- **Vision-language integration** enabling zero-shot detection of arbitrary objects
- **Real-time performance** making practical deployment feasible
- **Unsupervised unknown object recognition** addressing fundamental label bias
- **Multimodal prompting** providing flexible detection capabilities
- **Foundation model utilization** leveraging large-scale pre-training

However, significant challenges remain in incremental learning, domain adaptation, and comprehensive evaluation. The field is moving toward unified frameworks that combine detection, segmentation, and semantic understanding, with increasing emphasis on real-world applicability rather than benchmark performance alone.

The convergence of foundation models, efficient architectures, and unsupervised learning techniques suggests that truly practical open world detection systems are within reach, though fundamental research questions around continuous learning and unknown object characterization require further investigation.

---

## References

Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. *arXiv preprint arXiv:2401.17270*. https://arxiv.org/abs/2401.17270v3

Fang, R., Pang, G., Zhou, L., Bai, X., & Zheng, J. (2023). Unsupervised recognition of unknown objects for open-world object detection. *arXiv preprint arXiv:2308.16527*. https://arxiv.org/abs/2308.16527v1

Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., & Zhang, L. (2024). T-Rex2: Towards generic object detection via text-visual prompt synergy. *arXiv preprint arXiv:2403.14610*. https://arxiv.org/abs/2403.14610v1

Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., & Zhang, L. (2024). Grounding DINO 1.5: Advance the "edge" of open-set object detection. *arXiv preprint arXiv:2405.10300*. https://arxiv.org/abs/2405.10300v2

Shi, C., & Yang, S. (2023). EdaDet: Open-vocabulary object detection using early dense alignment. *arXiv preprint arXiv:2309.01151*. https://arxiv.org/abs/2309.01151v1

Wang, H., Ren, P., Jie, Z., Dong, X., Feng, C., Qian, Y., Ma, L., Jiang, D., Wang, Y., Lan, X., & Liang, X. (2024). OV-DINO: Unified open-vocabulary detection with language-aware selective fusion. *arXiv preprint arXiv:2407.07844*. https://arxiv.org/abs/2407.07844v2

Wu, S., Zhang, W., Xu, L., Jin, S., Li, X., Liu, W., & Loy, C. C. (2023). CLIPSelf: Vision transformer distills itself for open-vocabulary dense prediction. *arXiv preprint arXiv:2310.01403*. https://arxiv.org/abs/2310.01403v2

Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., & Xu, D. (2024). DetCLIPv3: Towards versatile generative open-vocabulary object detection. *arXiv preprint arXiv:2404.09216*. https://arxiv.org/abs/2404.09216v1

Zhao, T., Liu, P., He, X., Zhang, L., & Lee, K. (2024). Real-time transformer-based open-vocabulary detection with efficient fusion head. *arXiv preprint arXiv:2403.06892*. https://arxiv.org/abs/2403.06892v2

Zohar, O., Lozano, A., Goel, S., Yeung, S., & Wang, K.-C. (2023). Open world object detection in the era of foundation models. *arXiv preprint arXiv:2312.05745*. https://arxiv.org/abs/2312.05745v1

---

**Review Methodology:**  
Papers were identified through arXiv search in cs.CV category with publication dates between August 22, 2023 and August 21, 2025. The search used the query "open world detection" with citation expansion, resulting in a pool of 50 papers with 129 additional papers from references. Papers were screened for relevance to open world detection, open set recognition, unknown object detection, or novel class detection. The 10 most central papers were selected based on co-citation analysis and relevance scoring.
