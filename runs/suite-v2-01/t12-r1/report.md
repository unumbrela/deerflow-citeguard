# Systematic Literature Review: Vision-Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: "vision-language models", cs.CV category, published between 2025-02-24 and 2026-10-08
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on vision-language models (VLMs) reveals a field rapidly maturing beyond basic multimodal integration toward addressing critical challenges in reliability, safety, interpretability, and domain-specific adaptation. Recent work demonstrates that while VLMs have achieved remarkable capabilities in cross-modal reasoning and contextual understanding, significant vulnerabilities persist—including susceptibility to adversarial perturbations, hallucination tendencies, and gaps between expert and lay communication. The research community is actively developing solutions across multiple fronts: training-free self-correction frameworks, hyperbolic safety-aware architectures, holistic explainability methods, and specialized benchmarks for medical and heritage document applications. Collectively, these papers suggest that the next generation of VLMs must prioritize trustworthiness and domain adaptation alongside raw performance.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "vision-language models", filtered to category cs.CV, published between 2024-10-25 and 2026-10-08. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Reliability and Robustness Under Adversarial Conditions

A prominent concern across recent VLM research is the fragility of these models when exposed to adversarial or perturbed inputs. Vice et al. (2025) demonstrated that VLMs exhibit critical vulnerabilities to subtle, structured frequency-domain perturbations that are visually imperceptible yet systematically undermine authenticity detection and image captioning across multiple state-of-the-art models. Their findings reveal that VLM judgments are sensitive to frequency-based cues and may not wholly align with semantic content, exposing fundamental weaknesses in how these models process visual information.

Complementing this work, Arokiaraj et al. (2026) uncovered a striking dissociation between adversarially corrupted training loss and correct free-generation outputs, showing that adversarial robustness in autoregressive VLMs is substantially a property of the language decoder's prior rather than the visual encoder. Their analysis localized the train/inference gap to a single autoregressive step where the target token rank is fixed at exactly 3,488 out of 152,064 vocabulary entries for every corrupted image, suggesting that the language decoder differentially arbitrates by amplifying or suppressing corrupted signals. These findings collectively indicate that VLM reliability requires deeper architectural scrutiny beyond surface-level performance metrics.

### Theme 2: Hallucination Mitigation and Self-Correction

Addressing the pervasive problem of hallucination in VLMs, Sanogo and Ardiccioni (2025) proposed a training-free self-correction framework that enables VLMs to iteratively refine responses through uncertainty-guided visual re-attention. Their approach combines multidimensional uncertainty quantification with attention-guided cropping, achieving a 9.8 percentage point reduction in hallucination rates and a 4.7 point improvement in object existence accuracy on adversarial splits. This work demonstrates that hallucination mitigation need not require expensive retraining and can instead leverage the model's existing uncertainty signals to ground corrections in visual evidence.

The hallucination problem is further illuminated by explainability research. Shen (2025) introduced GLIMPSE, a lightweight framework that produces holistic response-level heat maps for interpreting cross-modal reasoning, enabling diagnosis of hallucination and bias through fine-grained attribution analysis. By fusing gradient-weighted attention, adaptive layer propagation, and relevance-weighted token aggregation, GLIMPSE outperforms prior methods in faithfulness and human-attention alignment, providing a diagnostic tool for understanding when and why VLMs generate hallucinated content.

### Theme 3: Domain-Specific Adaptation and Specialized Benchmarks

The literature reveals strong momentum toward adapting general-purpose VLMs for specialized domains, particularly medicine and heritage digitization. Jang et al. (2026) introduced MedLayXPlain, a large-scale multimodal benchmark with 122,789 region-grounded samples across 8 imaging modalities, to address the expert-lay gap in medical VLM explanations. Their systematic evaluation of 33 VLMs confirmed that medical VLMs achieve strong expert-level performance but suffer significant lay-register degradation, while general-purpose VLMs produce more accessible language yet lack clinical precision—neither paradigm adequately serves patient-facing communication needs.

In the heritage domain, Basu Bir et al. (2026) demonstrated that lightweight VLMs with up to 7B parameters can provide sustainable, private alternatives to commercial APIs for OCR-to-structure extraction in document digitization. Their comparative study of eight open-source models across three university heritage collections showed that joint training enables one model to operate across collections, though performance trade-offs exist when using multi-dataset checkpoints versus dataset-specific fine-tuning. This work addresses critical concerns about data autonomy, recurring costs, and environmental footprint in institutional archives.

### Theme 4: Safety and Content Moderation

Emerging research is exploring novel architectural approaches to safety in VLMs. Poppi et al. (2025) introduced HySAC (Hyperbolic Safety-Aware CLIP), which leverages hyperbolic space properties to encode safe and unsafe content as an entailment hierarchy, shifting from unlearning to an awareness paradigm. Their approach enables the model to serve as both a multimodal unsafe classifier and flexible content retriever, allowing dynamic redirection of unsafe queries toward safer alternatives. This hierarchical modeling is ineffective in standard VLMs due to their reliance on Euclidean embeddings, demonstrating that geometric representations can fundamentally enhance safety recognition while establishing a more interpretable framework for content moderation.

### Theme 5: Comprehensive Surveys and Future Directions

Broader survey work contextualizes these specialized advances within the field's trajectory. Kalpelbe et al. (2025) provided an extensive review of Medical VLM advancements, identifying key challenges including data scarcity, narrow task generalization, interpretability issues, and ethical concerns such as fairness, accountability, and privacy. They highlighted that limitations are exacerbated by uneven dataset distribution, computational demands, and regulatory hurdles, while proposing future directions including federated learning, lightweight architectures, and EHR integration to democratize access and improve clinical relevance.

Similarly, Sapkota and Karkee (2025) surveyed how large vision-language models have revolutionized object detection by enhancing adaptability, contextual reasoning, and generalization beyond traditional architectures. Their three-step research review process examined architectural innovations, training paradigms, and output flexibility, concluding that LVLMs are expected to meet or surpass conventional methods in object detection while identifying major limitations with proposed solutions for future advancement.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that current VLM architectures, despite impressive capabilities, exhibit systematic vulnerabilities that require architectural rather than superficial fixes. Both adversarial robustness work (Vice et al., 2025; Arokiaraj et al., 2026) and hallucination mitigation research (Sanogo & Ardiccioni, 2025) agree that surface-level performance metrics mask deeper structural issues. Similarly, domain adaptation papers (Jang et al., 2026; Basu Bir et al., 2026; Kalpelbe et al., 2025) converge on the conclusion that general-purpose VLMs require substantial specialization for domain-specific tasks, and that neither purely general nor purely specialized approaches currently suffice.

**Disagreements**: The literature reveals tension between different approaches to VLM improvement. Safety research (Poppi et al., 2025) advocates for architectural innovations in representation geometry, while hallucination work (Sanogo & Ardiccioni, 2025) demonstrates that training-free methods can achieve substantial gains. This suggests disagreement about whether fundamental architectural changes are necessary or whether clever use of existing models can suffice. Additionally, while some papers emphasize lightweight, efficient approaches (Basu Bir et al., 2026; Shen, 2025), others work with large-scale benchmarks and models (Jang et al., 2026), reflecting ongoing debate about the optimal scale for VLM deployment.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Patient-Facing Communication**: Medical VLMs lack adequate capabilities for generating lay-understandable explanations, creating a critical barrier to clinical adoption (Jang et al., 2026).

2. **Architectural Understanding**: The mechanisms by which language decoders arbitrate corrupted visual signals remain poorly understood, with Arokiaraj et al. (2026) noting that linear probe estimates have circularity concerns requiring further investigation.

3. **Cross-Domain Generalization**: While domain-specific adaptation shows promise, the literature lacks clear guidance on when to use joint training versus dataset-specific fine-tuning, with Basu Bir et al. (2026) noting performance trade-offs that remain uncharacterized.

4. **Evaluation Metrics**: Standard NLG metrics show poor correlation with clinical judgment (Jang et al., 2026), and multiple papers note that quantitative performance assessments are incomplete or model-specific, suggesting a need for better evaluation frameworks.

5. **Explainability Limitations**: While GLIMPSE advances explainability, Shen (2025) does not detail limitations in the abstract, and the broader question of how explainability tools translate to practical debugging remains open.

6. **Color Vision and Specialized Capabilities**: Ye et al. (2025) note that color vision abilities of VLMs have not been thoroughly explored, and their abstract lacks specific quantitative results, indicating this is an emerging area requiring further study.

## Per-Paper Annotations

### Arokiaraj et al. (2026)

**Research question**: Why do vision-language models show a dissociation between adversarially corrupted training loss and correct free-generation outputs?
**Methodology**: The authors used a controlled two-stage PGD attack on 200 held-out COCO images with Qwen2.5-VL-7B-Instruct, analyzing image-level pixel statistics, applying logit lens to localize the train/inference gap, and tracking target-token rank across all 28 LLM decoder layers with linear probe analysis.
**Key findings**:
- Image-level pixel statistics including texture-based attackability measures have essentially no predictive power over which images are corrupted (best predictor r=-0.050, ridge regression R^2=0.069)
- The train/inference gap localizes to a single autoregressive step where the target token rank is fixed at exactly 3,488 out of 152,064 vocabulary entries for every image with zero variance
- The visual encoder corrupts every image's representation by comparable margin regardless of outcome, but the language decoder differentially arbitrates by amplifying corrupted signals for susceptible images and suppressing them for resistant ones (p<0.001, rank-biserial r=0.579)
- A linear probe on the merger hidden state separates susceptible and resistant outcomes with AUC=0.858
- Adversarial robustness in autoregressive VLMs is substantially a property of the language decoder's prior rather than the visual encoder
**Limitations**: The linear probe AUC estimate has circularity concerns that the authors flag; the study is conducted on a single model (Qwen2.5-VL-7B-Instruct) with 200 COCO images.

### Basu Bir et al. (2026)

**Research question**: Can open-source lightweight vision-language models (up to 7B parameters) provide a sustainable, private alternative to commercial APIs for OCR-to-structure extraction in heritage document digitization?
**Methodology**: The authors conducted a comparative study of eight open-source lightweight VLMs across three university heritage collections using a constraint-aware protocol evaluating zero-shot, few-shot, and fine-tuning settings with CER, ANLS*, and mAP-F1 metrics, while testing hyperparameter optimization, classical image preprocessing, and multi-stage training approaches.
**Key findings**:
- Lightweight VLMs with up to 7B parameters can provide sustainable, private, high-performing alternatives to manual transcription or commercial black-box systems for heritage institutions
- The study evaluated models on extraction fidelity and structured-output quality using Character Error Rate, Approximate Normalized Levenshtein Similarity, and mean Average Precision F1
- Joint training enables one model to operate across collections but can shift performance between datasets
- Classical image preprocessing techniques (illumination flattening, denoising, CLAHE) and hyperparameter optimization independently impact performance
- The approach addresses data autonomy concerns, recurring costs, and environmental footprint of hyperscale computing in institutional archives
**Limitations**: The study focuses on heritage digitization with domain-specific terminology and non-standard layouts; performance trade-offs exist when using multi-dataset checkpoints versus dataset-specific fine-tuning.

### Jang et al. (2026)

**Research question**: Can medical vision-language models generate patient-accessible descriptions that bridge the gap between expert-level and lay-understandable medical imaging explanations?
**Methodology**: The authors introduce MedLayXPlain, a large-scale multimodal benchmark with 122,789 region-grounded samples across 8 imaging modalities, using Hierarchical Ontology-Verified Refinement (HOVER) for lay caption construction and MedLayEval, a 3B evaluator distilled from a 27B verifier, to benchmark 33 VLMs on expert-lay alignment.
**Key findings**:
- Medical VLMs achieve strong expert-level performance but their ability to generate patient-accessible descriptions remains underexplored.
- A systematic Expert-Lay Gap exists: medical VLMs achieve strong expert captioning but suffer significant lay-register degradation.
- General-purpose VLMs produce more accessible language yet lack clinical precision.
- Neither current paradigm adequately serves patient-facing communication needs.
- Standard NLG metrics show poor correlation with clinical judgment, necessitating specialized evaluation tools.
**Limitations**: The study confirms that neither current medical nor general-purpose VLM paradigm adequately serves patient-facing communication, indicating a significant gap in current capabilities.

### Kalpelbe et al. (2025)

**Research question**: What are the current advancements, applications, challenges, and future directions of Medical Vision-Language Models in healthcare?
**Methodology**: This survey provides an extensive review of recent Med-VLM advancements, discussing foundational technology, adaptation of general models for medical tasks, healthcare applications, and examining challenges through analysis of data scarcity, generalization, interpretability, and ethical concerns.
**Key findings**:
- Med-VLMs integrate visual and textual data to enhance healthcare outcomes across clinical practice, education, and patient care
- Key challenges include data scarcity, narrow task generalization, interpretability issues, and ethical concerns such as fairness, accountability, and privacy
- Limitations are exacerbated by uneven dataset distribution, computational demands, and regulatory hurdles
- Future directions include leveraging large-scale diverse datasets, improving cross-modal generalization, and enhancing interpretability
- Innovations like federated learning, lightweight architectures, and EHR integration are pathways to democratize access and improve clinical relevance
**Limitations**: The survey identifies challenges but the abstract does not provide specific quantitative assessments of current Med-VLM performance gaps or detailed regulatory framework recommendations.

### Poppi et al. (2025)

**Research question**: How can hyperbolic space properties be leveraged to shift from unlearning to an awareness paradigm for unsafe content retrieval in vision-language models like CLIP?
**Methodology**: The authors introduced HySAC (Hyperbolic Safety-Aware CLIP), which encodes safe and unsafe content as an entailment hierarchy in hyperbolic space using entailment loss functions to model hierarchical and asymmetrical relations between safe and unsafe image-text pairs.
**Key findings**:
- The hyperbolic space approach enables encoding safe and unsafe content in different regions as an entailment hierarchy
- The modeling endows the model with awareness of unsafe content, enabling it to serve as both a multimodal unsafe classifier and flexible content retriever
- The approach allows dynamic redirection of unsafe queries toward safer alternatives or retention of original output
- This hierarchical modeling is ineffective in standard vision-language models due to their reliance on Euclidean embeddings
- Extensive experiments show the approach enhances safety recognition while establishing a more adaptable and interpretable framework for content moderation
**Limitations**: The abstract does not specify quantitative performance metrics, dataset details, or computational overhead of the hyperbolic space approach compared to unlearning techniques.

### Sanogo and Ardiccioni (2025)

**Research question**: How can hallucinations in vision-language models be reduced without requiring model retraining?
**Methodology**: The authors propose a training-free self-correction framework that enables VLMs to iteratively refine responses through uncertainty-guided visual re-attention, combining multidimensional uncertainty quantification with attention-guided cropping, validated on POPE and MMHAL BENCH benchmarks using Qwen2.5-VL-7B architecture.
**Key findings**:
- The training-free self-correction framework reduces hallucination rates by 9.8 percentage points compared to baseline.
- Object existence accuracy improves by 4.7 points on adversarial splits.
- Uncertainty-guided re-attention successfully grounds corrections in visual evidence where standard decoding fails.
- The framework operates entirely with frozen, pretrained VLMs requiring no gradient updates.
- Multidimensional uncertainty quantification effectively identifies areas needing visual re-attention.
**Limitations**: Validation was conducted only on Qwen2.5-VL-7B architecture, with plans to extend validation across diverse architectures in future work.

### Sapkota and Karkee (2025)

**Research question**: How have large vision-language models (LVLMs) advanced object detection compared to traditional deep learning architectures?
**Methodology**: The paper presents a structured three-step research review process examining state-of-the-art LVLMs for object detection, including analysis of architectural innovations, training paradigms, and output flexibility. The review includes comprehensive visualizations and comparative analysis of real-time performance, adaptability, and complexity against traditional systems.
**Key findings**:
- LVLMs have revolutionized object detection by enhancing adaptability, contextual reasoning, and generalization beyond traditional architectures.
- Recent LVLMs achieve advanced contextual understanding through novel architectural innovations and training paradigms.
- LVLMs demonstrate effectiveness across diverse scenarios including localization and segmentation.
- LVLMs are expected to meet or surpass the performance of conventional methods in object detection.
- Current LVLM modes have identifiable limitations with proposed solutions and a roadmap for future advancement.
**Limitations**: The review identifies major limitations of current LVLM modes but does not specify them in detail in the abstract.

### Shen (2025)

**Research question**: How can we interpret where large vision-language models direct their visual attention during visual question answering tasks?
**Methodology**: The paper introduces GLIMPSE, a lightweight, model-agnostic framework that jointly attributes LVLM outputs to relevant visual evidence and textual signals by fusing gradient-weighted attention, adaptive layer propagation, and relevance-weighted token aggregation to produce holistic response-level heat maps.
**Key findings**:
- GLIMPSE outperforms prior methods in faithfulness and pushes state-of-the-art in human-attention alignment.
- The framework produces holistic response-level heat maps for interpreting cross-modal reasoning.
- The analytic approach uncovers fine-grained insights into LVLM cross-modal attribution and reasoning dynamics.
- The method enables analysis of systematic misalignment, diagnosis of hallucination and bias, and ensures transparency.
- GLIMPSE is lightweight and model-agnostic, making it broadly applicable across different LVLM architectures.
**Limitations**: Not stated in abstract.

### Vice et al. (2025)

**Research question**: How vulnerable are vision-language models to subtle, structured perturbations in the frequency domain when performing visual content reasoning tasks?
**Methodology**: The authors designed targeted image transformations operating in the frequency domain to systematically adjust VLM outputs when exposed to frequency-perturbed real and synthetic images, testing generalization across five state-of-the-art VLMs including Qwen2/2.5 and BLIP models across ten real and generated image datasets.
**Key findings**:
- VLMs exhibit critical vulnerabilities when exposed to subtle, structured frequency-domain perturbations.
- Feature transformations undermine authenticity/DeepFake detection and automated image captioning tasks.
- The perturbation injection method generalizes across five state-of-the-art VLMs with different parameters.
- Visually-imperceptible spatial frequency transformations expose the fragility of VLMs deployed for automated image captioning and authenticity detection.
- VLM judgments are sensitive to frequency-based cues and may not wholly align with semantic content.
**Limitations**: The findings are demonstrated under realistic, black-box constraints, though specific limitations of the study are not detailed in the abstract.

### Ye et al. (2025)

**Research question**: What is the color vision ability of large vision-language models, and how can their performance on color vision tests be improved?
**Methodology**: The authors defined a color vision testing task for large vision-language models and constructed a dataset covering multiple categories of test questions and varying difficulty levels, then analyzed error types and proposed fine-tuning strategies to enhance performance.
**Key findings**:
- The color vision abilities of large visual-language models have not been thoroughly explored prior to this work
- The authors constructed a dataset covering multiple categories of test questions and tasks of varying difficulty levels
- Analysis of error types made by large vision-language models was conducted
- Fine-tuning strategies were proposed to enhance model performance in color vision tests
**Limitations**: The abstract does not report specific quantitative results, benchmark performance numbers, or details about the dataset size and composition; the fine-tuning strategies and their effectiveness are not detailed.

## References

Arokiaraj, A. J., Wu, Z., & Koshiyama, A. (2026). Corrupted but correct: Why vision-language models lie to themselves internally. arXiv. https://arxiv.org/abs/2610.03445

Basu Bir, U., Christlein, V., Maier, A., & Zinnen, M. (2026). From pixels to structure: Lightweight vision-language models for document OCR and structured JSON extraction. arXiv. https://arxiv.org/abs/2610.11818

Jang, H., Lee, J., Kim, S., Lim, C. Y., Goh, H., Eum, H., & Choi, K. S. (2026). MedLayXPlain: Benchmarking the expert-lay gap in medical vision-language models. arXiv. https://arxiv.org/abs/2606.21194

Kalpelbe, B. C., Adaambiik, A. G., & Peng, W. (2025). Vision language models in medicine. arXiv. https://arxiv.org/abs/2503.01863

Poppi, T., Kasarla, T., Mettes, P., Baraldi, L., & Cucchiara, R. (2025). Hyperbolic safety-aware vision-language models. arXiv. https://arxiv.org/abs/2503.12127

Sanogo, K., & Ardiccioni, R. (2025). Toward more reliable artificial intelligence: Reducing hallucinations in vision-language models. arXiv. https://arxiv.org/abs/2512.07564

Sapkota, R., & Karkee, M. (2025). Object detection with multimodal large vision-language models: An in-depth review. arXiv. https://arxiv.org/abs/2508.19294

Shen, G. (2025). Glimpse: Holistic cross-modal explainability for large vision-language models. arXiv. https://arxiv.org/abs/2506.18985

Vice, J., Akhtar, N., Gao, Y., Hartley, R., & Mian, A. (2025). On the reliability of vision-language models under adversarial frequency-domain perturbations. arXiv. https://arxiv.org/abs/2507.22398

Ye, H., Chen, B., Liu, W., Zhang, Y., Li, Z., Ni, D., & Chen, H. (2025). Assessing color vision test in large vision-language models. arXiv. https://arxiv.org/abs/2507.11153
