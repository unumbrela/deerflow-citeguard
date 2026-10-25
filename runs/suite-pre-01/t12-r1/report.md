# Systematic Literature Review: Vision-Language Models

**Date**: 2026-10-25  
**Papers surveyed**: 10  
**Scope**: "vision language models", cs.CV category, 2024-01-01 to 2026-10-25  
**Citation format**: APA 7th edition

## Executive Summary

The vision-language model (VLM) literature from 2024-2026 reveals a field rapidly maturing from capability demonstration toward reliability, safety, and domain-specific deployment. Recent work addresses critical challenges including hallucination reduction, adversarial robustness, explainability, and the gap between expert and lay communication in medical applications. Researchers are developing training-free correction frameworks, lightweight models for resource-constrained settings, and internet-augmented architectures to overcome temporal knowledge limitations. Security vulnerabilities—particularly frequency-domain perturbations and text prompt injection—expose significant reliability concerns for deployed systems. The literature converges on the need for robust evaluation frameworks and domain-adapted solutions, while open questions remain around computational efficiency, cross-modal generalization, and regulatory frameworks for high-stakes applications.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "vision language models", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Reliability and Hallucination Mitigation

A central concern across multiple papers is the reliability of VLM outputs, particularly hallucination—generating plausible but incorrect claims about image content. Sanogo and Ardiccioni (2025) demonstrated that training-free self-correction frameworks can reduce hallucination rates by 9.8 percentage points through uncertainty-guided visual re-attention, operating entirely on frozen pretrained models. Their approach combines multidimensional uncertainty quantification (token entropy, attention dispersion, semantic consistency, claim confidence) with attention-guided cropping of under-explored regions, achieving improved object existence accuracy on adversarial splits without requiring gradient updates.

Complementary work by Vice et al. (2025) exposed critical vulnerabilities in VLM reliability under adversarial frequency-domain perturbations. Their experiments across five state-of-the-art VLMs (including Qwen2/2.5 and BLIP models) revealed that visually imperceptible frequency transformations can systematically undermine both DeepFake detection and automated image captioning. The perturbation injection method generalized across architectures and datasets, challenging the reliability of VLMs deployed for authenticity detection under realistic black-box constraints.

Most recently, Arokiaraj et al. (2026) uncovered a mechanistic explanation for VLM robustness through the "train/inference gap"—a dissociation where adversarial perturbations drive training loss to near zero yet models still generate correct outputs during free generation. Using logit lens analysis on Qwen2.5-VL-7B-Instruct, they localized this gap to the language decoder's differential arbitration: the visual encoder corrupts all images comparably, but the language decoder amplifies corrupted signals for susceptible images while actively suppressing them for resistant ones. This finding suggests adversarial robustness is substantially a property of the language decoder's prior, not the visual encoder, with direct implications for defense strategies.

### Theme 2: Explainability and Cross-Modal Attribution

Understanding where VLMs direct visual attention during reasoning has emerged as essential for interpreting model behavior. Shen (2025) introduced GLIMPSE (Gradient-Layer Importance Mapping for Prompted Visual Saliency Explanation), a lightweight model-agnostic framework that jointly attributes LVLM outputs to relevant visual evidence and textual signals. By fusing gradient-weighted attention, adaptive layer propagation, and relevance-weighted token aggregation, GLIMPSE produces holistic response-level heat maps that outperform prior methods in faithfulness and achieve state-of-the-art human-attention alignment. The framework enables fine-grained analysis of cross-modal attribution, reasoning dynamics, and systematic misalignment diagnosis.

The explainability theme intersects with reliability: understanding attention patterns helps diagnose hallucination and bias. However, as Arokiaraj et al. (2026) noted, even when internal representations are corrupted, models may produce correct outputs through decoder arbitration—suggesting that post-hoc explainability methods must account for this dissociation between internal states and generated outputs.

### Theme 3: Domain-Specific Adaptation and the Expert-Lay Gap

Medical VLMs represent a critical domain where reliability and communication effectiveness have direct clinical consequences. Jang et al. (2026) introduced MedLayXPlain, the first large-scale multimodal benchmark evaluating the "Expert-Lay Gap"—the ability of medical VLMs to generate patient-accessible descriptions mandated by the 21st Century Cures Act. Their benchmark of 33 VLMs on 122,789 samples across 8 imaging modalities revealed a systematic gap: medical VLMs achieve strong expert-level captioning but suffer significant lay-register degradation, while general-purpose VLMs produce more accessible language yet lack clinical precision. Neither paradigm currently serves patient-facing communication adequately.

Kalpelbe et al. (2025) provided a comprehensive survey of Med-VLMs, highlighting transformative impacts on clinical practice, education, and patient care alongside persistent challenges: data scarcity, narrow task generalization, interpretability issues, and ethical concerns around fairness, accountability, and privacy. They emphasized that limitations are exacerbated by uneven dataset distribution, computational demands, and regulatory hurdles, calling for rigorous evaluation methods and robust regulatory frameworks before safe clinical integration.

### Theme 4: Lightweight and Sustainable Deployment

Addressing computational and privacy concerns, recent work explores lightweight VLM alternatives to massive closed-source models. Bir et al. (2026) demonstrated that carefully adapted open-source VLMs with up to 7B parameters can provide sustainable, private, high-performing alternatives for document OCR-to-structured-JSON extraction in heritage digitization. Their comparative study across three university heritage collections showed that hyperparameter optimization, classical image preprocessing (illumination flattening, denoising, CLAHE), and multi-stage training each provide independent performance improvements. Joint multi-dataset training enables one model to operate across collections, though with performance trade-offs between datasets.

This theme reflects growing awareness of the environmental footprint and recurring costs of hyperscale computing, particularly for institutional archives with data autonomy concerns. Lightweight VLMs enable schema-compliant extraction with automatic validation, offering institution-controlled alternatives to commercial black-box systems.

### Theme 5: Temporal Knowledge and Internet-Augmented Generation

VLMs trained on static datasets lack knowledge of events occurring after their training cutoff. Li et al. (2024) addressed this through SearchLVLMs, a plug-and-play framework augmenting existing LVLMs with up-to-date internet knowledge during inference. Their hierarchical filtering model efficiently identifies the most helpful content from search engine results, trained on automatically generated news-related VQA samples (UDK-VQA dataset) with multi-model voting for labeling. SearchLVLMs outperformed GPT-4V by approximately 25% in accuracy on up-to-date knowledge tasks, demonstrating that internet-augmented generation can be implemented without model retraining.

This approach mirrors retrieval-augmented generation (RAG) patterns from text-only LLMs, adapted for multimodal inputs. The framework's effectiveness suggests a promising direction for maintaining VLM relevance without frequent costly updates.

### Theme 6: Security Vulnerabilities and Attack Surfaces

Beyond frequency-domain attacks, VLMs face simpler but effective text prompt injection threats. Zhu (2025) demonstrated that text prompt injection—a computationally efficient attack method—can effectively mislead large vision-language models. Compared to other attack approaches requiring substantial computational resources, text prompt injection offers particular effectiveness against large models with minimal resource demands. This finding underscores the need for input sanitization and defensive prompting strategies in deployed VLM systems.

The convergence of security findings across multiple papers—frequency perturbations (Vice et al., 2025), text injection (Zhu, 2025), and internal representation corruption (Arokiaraj et al., 2026)—paints a picture of VLMs as vulnerable to diverse attack vectors, necessitating multi-layered defense strategies.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the need for robust evaluation frameworks and domain-adapted solutions. Both medical VLM studies (Jang et al., 2026; Kalpelbe et al., 2025) emphasize that current paradigms inadequately serve their intended use cases—whether patient communication or clinical integration. Reliability papers converge on the finding that VLMs exhibit systematic vulnerabilities: hallucination (Sanogo & Ardiccioni, 2025), frequency perturbations (Vice et al., 2025), and internal corruption (Arokiaraj et al., 2026) all reveal gaps between apparent capability and actual robustness. Lightweight deployment work (Bir et al., 2026) and medical surveys (Kalpelbe et al., 2025) both highlight computational efficiency and data autonomy as critical deployment considerations.

**Disagreements**: The literature shows limited direct disagreement, reflecting the survey's focus on complementary rather than competing approaches. However, implicit tensions exist: internet-augmented generation (Li et al., 2024) assumes external knowledge improves VLM performance, while security work (Vice et al., 2025; Zhu, 2025) suggests external inputs introduce attack surfaces. Similarly, lightweight models (Bir et al., 2026) trade absolute performance for sustainability, while medical benchmarks (Jang et al., 2026) reveal that neither lightweight nor massive models currently bridge the expert-lay gap—suggesting architectural innovation beyond scaling is needed.

## Gaps and Open Questions

The collective literature reveals several critical gaps:

1. **Defensive mechanisms**: While multiple papers expose vulnerabilities (frequency perturbations, prompt injection, hallucination), few propose comprehensive defense strategies. Sanogo and Ardiccioni (2025) offer a training-free correction framework, but Arokiaraj et al. (2026) note that decoder-based robustness remains poorly understood and unexploited for defense.

2. **Cross-domain generalization**: Lightweight VLM success in heritage documents (Bir et al., 2026) and medical VLM limitations (Jang et al., 2026; Kalpelbe et al., 2025) both highlight that domain adaptation remains ad hoc. Systematic methods for transferring VLM capabilities across domains without catastrophic forgetting are absent.

3. **Evaluation standardization**: Medical VLM papers (Jang et al., 2026; Kalpelbe et al., 2025) emphasize poor correlation between standard NLG metrics and clinical judgment, calling for domain-specific evaluators. This gap likely extends to other domains—general-purpose metrics may not capture task-relevant quality.

4. **Regulatory frameworks**: Kalpelbe et al. (2025) note that regulatory hurdles exacerbate Med-VLM limitations, yet no paper proposes concrete regulatory pathways. As VLMs enter high-stakes domains (medicine, heritage, authenticity detection), this gap becomes increasingly urgent.

5. **Computational cost transparency**: While lightweight models (Bir et al., 2026) and training-free methods (Sanogo & Ardiccioni, 2025) address efficiency, most papers lack detailed computational cost analysis. Resource sustainability claims remain qualitative rather than quantitative.

6. **Multilingual and cross-cultural considerations**: None of the surveyed papers address VLM performance across languages or cultural contexts beyond English. This gap limits global deployment and raises equity concerns.

## Per-Paper Annotations

### Arokiaraj et al. (2026)

**Research question**: Why do vision-language models exhibit a dissociation between near-zero adversarial training loss and correct free generation outputs?  
**Methodology**: Conducted controlled two-stage PGD attack on Qwen2.5-VL-7B-Instruct using 200 held-out COCO images; applied logit lens analysis to localize the train/inference gap; tracked target-token rank across all 28 LLM decoder layers; trained linear probe on merger hidden state.  
**Key findings**:
- Image-level pixel statistics have essentially no predictive power over which images are corrupted (best predictor r=-0.050, p=0.484)
- Target token rank is fixed at exactly 3,488 out of 152,064 vocabulary entries for every image with zero variance, localized to a single autoregressive step
- Visual encoder corrupts all images comparably, but language decoder differentially arbitrates—amplifying corrupted signals for susceptible images and suppressing them for resistant ones
- Linear probe on merger hidden state separates outcomes with AUC=0.858
- Adversarial robustness is substantially a property of the language decoder's prior, not the visual encoder  
**Limitations**: Study conducted on single model (Qwen2.5-VL-7B-Instruct) limiting generalizability; circularity concern flagged in AUC estimate; 200-image sample may not capture full diversity of VLM behavior.

### Bir et al. (2026)

**Research question**: Can open-source lightweight VLMs (≤7B parameters) provide a sustainable, private, high-performing alternative to commercial APIs for document OCR-to-structured-JSON extraction in heritage digitization?  
**Methodology**: Comparative study of eight open-source lightweight VLMs (up to 7B parameters) across three university heritage collections; evaluated under constraint-aware protocol across zero-shot, few-shot, and fine-tuning settings using CER, ANLS*, and mAP-F1 metrics; tested impact of hyperparameter optimization, classical image preprocessing, and multi-stage training.  
**Key findings**:
- Carefully adapted VLMs with up to 7B parameters can provide sustainable, private, high-performing alternative to manual transcription or commercial black-box systems
- Joint multi-dataset training enables one model to operate across collections but can shift performance between datasets
- Hyperparameter optimization, classical image preprocessing (illumination flattening, denoising, CLAHE), and multi-stage training each provide independent performance improvements
- Lightweight VLMs enable schema-compliant JSON extraction with automatic validation for downstream use  
**Limitations**: Evaluation limited to models up to 7B parameters which may not match largest commercial systems; heritage documents with historical handwriting and domain-specific terminology may not generalize to other document types; joint training creates performance trade-offs between datasets.

### Jang et al. (2026)

**Research question**: Can medical vision-language models generate patient-accessible descriptions that bridge the expert-lay communication gap mandated by the 21st Century Cures Act?  
**Methodology**: Introduced MedLayXPlain-122K benchmark with 122,789 region-grounded samples across 8 imaging modalities using HOVER pipeline for lay caption generation and MedLayEval 3B evaluator for expert-lay alignment scoring.  
**Key findings**:
- Medical VLMs achieve strong expert-level captioning but suffer significant lay-register degradation
- General-purpose VLMs produce more accessible language but lack clinical precision
- Neither current paradigm adequately serves patient-facing communication needs
- Standard NLG metrics show poor correlation with clinical judgment for medical language evaluation
- Systematic Expert-Lay Gap exists across 33 benchmarked VLMs  
**Limitations**: Neither medical nor general-purpose VLM paradigms currently bridge the expert-lay gap; benchmark focuses on publicly available datasets which may not represent all clinical scenarios.

### Kalpelbe et al. (2025)

**Research question**: What are the current advancements, applications, challenges, and future directions of Medical Vision-Language Models (Med-VLMs) in healthcare?  
**Methodology**: Comprehensive survey reviewing recent Med-VLM literature; discussed foundational technology, adaptation of general models for medical tasks, applications in healthcare, challenges, and future directions including federated learning and EHR integration.  
**Key findings**:
- Med-VLMs integrate visual and textual data to enhance healthcare outcomes across clinical practice, education, and patient care
- Key challenges include data scarcity, narrow task generalization, interpretability issues, and ethical concerns (fairness, accountability, privacy)
- Limitations are exacerbated by uneven dataset distribution, computational demands, and regulatory hurdles
- Future directions include leveraging large-scale diverse datasets, improving cross-modal generalization, federated learning, lightweight architectures, and Electronic Health Record integration  
**Limitations**: As a survey paper, presents no original experimental results; challenges around uneven dataset distribution and regulatory frameworks remain unresolved; rigorous evaluation methods and robust regulatory frameworks still needed for safe clinical integration.

### Li et al. (2024)

**Research question**: How can existing Large Vision-Language Models (LVLMs) be augmented with up-to-date internet knowledge during inference to overcome their temporal knowledge limitations?  
**Methodology**: Proposed SearchLVLMs, a plug-and-play framework with a hierarchical filtering model trained to find the most helpful content from search engine results to prompt LVLMs; automatically generated news-related VQA samples (UDK-VQA dataset) with multi-model voting to label website/content usefulness.  
**Key findings**:
- SearchLVLMs framework outperforms GPT-4V by approximately 25% in accuracy on up-to-date knowledge VQA tasks
- Hierarchical filtering model effectively and efficiently identifies the most helpful web content for augmenting LVLM responses
- Multi-model voting mechanism enables reliable labeling of training data for website/content usefulness
- Internet-augmented generation (IAG) can be implemented as a plug-and-play solution for existing LVLMs without model retraining  
**Limitations**: Evaluation focused on news-related VQA samples which may not generalize to all up-to-date knowledge domains; the specific mechanics underlying commercial IAG systems (like GPT-4V) remain unexplained and were not directly compared in detail.

### Sanogo and Ardiccioni (2025)

**Research question**: How can hallucinations in vision-language models be reduced without requiring additional training or model modifications?  
**Methodology**: Proposed training-free self-correction framework combining multidimensional uncertainty quantification (token entropy, attention dispersion, semantic consistency, claim confidence) with attention-guided cropping of under-explored regions on frozen pretrained VLMs.  
**Key findings**:
- Framework reduces hallucination rates by 9.8 percentage points compared to baseline
- Object existence accuracy improves by 4.7 points on adversarial splits
- Uncertainty-guided re-attention successfully grounds corrections in visual evidence
- Method operates entirely with frozen pretrained VLMs requiring no gradient updates
- Standard decoding fails where uncertainty-guided visual re-attention succeeds  
**Limitations**: Validation currently limited to Qwen2.5-VL-7B architecture; plans to extend across diverse architectures in future work; training-free approach may have ceiling on improvement potential.

### Shen (2025)

**Research question**: How can we interpret where large vision-language models direct their visual attention during visual question answering and open-ended generation?  
**Methodology**: Introduced GLIMPSE framework fusing gradient-weighted attention, adaptive layer propagation, and relevance-weighted token aggregation to produce holistic response-level heat maps for cross-modal reasoning attribution.  
**Key findings**:
- GLIMPSE produces holistic response-level heat maps attributing outputs to relevant visual and textual evidence
- Framework outperforms prior methods in faithfulness metrics
- Achieves state-of-the-art performance in human-attention alignment
- Enables fine-grained analysis of cross-modal attribution and reasoning dynamics
- Framework can diagnose hallucination, bias, and systematic misalignment in LVLMs  
**Limitations**: Framework is lightweight and model-agnostic but specific computational overhead not detailed; interpretability methods inherently provide post-hoc explanations rather than improving model behavior directly.

### Sapkota and Karkee (2025)

**Research question**: How can large vision-language models (LVLMs) enhance object detection capabilities beyond traditional deep learning architectures?  
**Methodology**: Systematic three-step research review process examining LVLM architectures, training paradigms, and visual-textual integration approaches for object detection and localization.  
**Key findings**:
- LVLMs enhance adaptability, contextual reasoning, and generalization beyond traditional object detection architectures
- Recent LVLMs achieve advanced contextual understanding through novel architectural innovations and training paradigms
- Comprehensive visualizations demonstrate LVLM effectiveness in diverse scenarios including localization and segmentation
- LVLMs are expected to meet or surpass conventional method performance in object detection
- LVLMs will have transformative impact on object detection and robotic applications  
**Limitations**: Current LVLM modes have identified major limitations requiring solutions; the review proposes a roadmap for future advancement but specific technical constraints are not detailed in the abstract.

### Vice et al. (2025)

**Research question**: How vulnerable are vision-language models to subtle, structured perturbations in the frequency domain when performing authenticity detection and image captioning?  
**Methodology**: Designed targeted frequency-domain image transformations and tested across five state-of-the-art VLMs (Qwen2/2.5 and BLIP models) on ten real and generated image datasets under black-box constraints.  
**Key findings**:
- VLMs exhibit critical vulnerability to visually imperceptible frequency-domain perturbations
- Perturbation injection method generalizes across five different state-of-the-art VLM architectures
- VLM judgments are sensitive to frequency-based cues and may not align with semantic content
- Frequency transformations undermine both DeepFake detection and automated image captioning tasks
- Findings challenge the reliability of VLMs deployed for automated authenticity detection under realistic conditions  
**Limitations**: Study conducted under black-box constraints; findings underscore need for robust multimodal perception systems but specific defense mechanisms are not proposed.

### Zhu (2025)

**Research question**: How effective and efficient is text prompt injection as an attack method for misleading large vision-language models compared to other attack approaches?  
**Methodology**: Developed algorithm for text prompt injection attacks on vision-language models; conducted experiments to demonstrate effectiveness and efficiency compared to other attack methods.  
**Key findings**:
- Text prompt injection is a simple yet effective method for misleading large vision-language models
- Approach is particularly effective for large models without high demand for computational resources
- Text prompt injection attacks offer advantages in efficiency compared to other attack methods  
**Limitations**: Abstract provides limited detail on experimental scope, model architectures tested, and quantitative metrics; defensive countermeasures and mitigation strategies not addressed; unclear which specific VLMs were evaluated.

## References

Arokiaraj, A. J., Wu, Z., & Koshiyama, A. (2026). Corrupted but correct: Why vision-language models lie to themselves internally. arXiv. https://arxiv.org/abs/2610.03445

Bir, U. B., Christlein, V., Maier, A., & Zinnen, M. (2026). From pixels to structure: Lightweight vision-language models for document OCR and structured JSON extraction. arXiv. https://arxiv.org/abs/2610.11818

Jang, H., Lee, J., Kim, S., Lim, C. Y., Goh, H., Eum, H., & Choi, K. S. (2026). MEDLAYXPLAIN: Benchmarking the expert-lay gap in medical vision-language models. arXiv. https://arxiv.org/abs/2606.21194

Kalpelbe, B. C., Adaambiik, A. G., & Peng, W. (2025). Vision language models in medicine. arXiv. https://arxiv.org/abs/2503.01863

Li, C., Li, Z., Jing, C., Liu, S., Shao, W., Wu, Y., Luo, P., Qiao, Y., & Zhang, K. (2024). SearchLVLMs: A plug-and-play framework for augmenting large vision-language models by searching up-to-date internet knowledge. arXiv. https://arxiv.org/abs/2405.14554

Sanogo, K., & Ardiccioni, R. (2025). Toward more reliable artificial intelligence: Reducing hallucinations in vision-language models. arXiv. https://arxiv.org/abs/2512.07564

Sapkota, R., & Karkee, M. (2025). Object detection with multimodal large vision-language models: An in-depth review. arXiv. https://arxiv.org/abs/2508.19294

Shen, G. (2025). GLIMPSE: Holistic cross-modal explainability for large vision-language models. arXiv. https://arxiv.org/abs/2506.18985

Vice, J., Akhtar, N., Gao, Y., Hartley, R., & Mian, A. (2025). On the reliability of vision-language models under adversarial frequency-domain perturbations. arXiv. https://arxiv.org/abs/2507.22398

Zhu, R. (2025). Text prompt injection of vision language models. arXiv. https://arxiv.org/abs/2510.09849
