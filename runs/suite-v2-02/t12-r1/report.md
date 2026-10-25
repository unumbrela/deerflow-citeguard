# Systematic Literature Review: Vision-Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "vision-language models", category cs.CV, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on vision-language models (VLMs) from the past two years reveals a field rapidly maturing beyond foundational architecture development toward critical concerns of reliability, safety, and domain-specific application. Recent research demonstrates strong consensus that while VLMs have achieved impressive capabilities in multimodal reasoning and cross-modal understanding, significant challenges remain in hallucination reduction, adversarial robustness, and accessibility for non-expert users. The literature spans diverse application domains including medical imaging, document processing, and object detection, with particular emphasis on making VLMs more trustworthy and interpretable. A notable shift is evident from purely performance-driven research toward addressing safety, explainability, and the gap between expert and lay understanding in critical domains like healthcare.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "vision-language models", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Reliability and Hallucination Mitigation

A dominant thread across the surveyed literature concerns the reliability of VLM outputs and the reduction of hallucinations. Multiple papers address the fundamental challenge that VLMs can generate confident but incorrect responses, particularly when reasoning about visual content. Sanogo & Ardiccioni (2025) propose a training-free self-correction framework that reduces hallucination rates by 9.8 percentage points through uncertainty-guided visual re-attention, demonstrating that iterative refinement can ground corrections in visual evidence without requiring model retraining. This work aligns with broader concerns about VLM trustworthiness, as the framework operates entirely with frozen pretrained models, making it immediately applicable to deployed systems.

The reliability theme extends beyond hallucination to internal representation integrity. Arokiaraj et al. (2026) reveal a striking dissociation between corrupted internal representations during training and correct outputs during free generation, showing that adversarial robustness in autoregressive VLMs is substantially a property of the language decoder's prior rather than the visual encoder. This finding challenges conventional wisdom about where robustness should be engineered and suggests that language model priors play a more critical arbitration role than previously recognized.

### Theme 2: Adversarial Vulnerabilities and Robustness

Closely related to reliability concerns, several papers examine VLM vulnerabilities under adversarial conditions. Vice et al. (2025) demonstrate that VLMs exhibit critical vulnerabilities to subtle, structured perturbations in the frequency domain, undermining both authenticity/DeepFake detection and automated image captioning tasks. Their work shows that visually imperceptible spatial frequency transformations expose the fragility of VLMs deployed for automated tasks, with perturbations generalizing across five state-of-the-art models including different-parameter Qwen and BLIP variants.

This vulnerability theme connects to the broader reliability concern: VLMs' sensitivity to frequency-based cues suggests they may not wholly align with semantic content, raising questions about deployment in security-critical applications. The convergence of findings across these papers indicates that robustness remains an open challenge requiring architectural innovations beyond current training paradigms.

### Theme 3: Medical VLMs and the Expert-Lay Gap

A significant application domain in the surveyed literature is medicine, where VLMs face unique challenges in bridging expert and lay understanding. Jang et al. (2026) introduce MedLayXPlain, a large-scale benchmark revealing a systematic Expert-Lay Gap: medical VLMs achieve strong expert captioning but suffer significant lay-register degradation when generating patient-accessible descriptions. Their benchmark of 33 VLMs across 122,789 region-grounded samples spanning 8 imaging modalities confirms that neither medical-specialized nor general-purpose VLMs adequately serve patient-facing communication.

This finding aligns with broader survey work by Kalpelbe et al. (2025), who identify interpretability issues as a key challenge alongside data scarcity and narrow task generalization. The convergence on interpretability as a critical gap suggests that medical VLM development must prioritize accessibility and transparency alongside clinical accuracy, particularly as these systems move toward clinical deployment.

### Theme 4: Explainability and Cross-Modal Attribution

Understanding where and how VLMs direct their visual attention emerges as a distinct research direction. Shen (2025) introduces GLIMPSE, a lightweight model-agnostic framework that jointly attributes VLM outputs to relevant visual evidence and textual signals, producing holistic response-level heat maps for interpreting cross-modal reasoning. This work outperforms prior methods in faithfulness and human-attention alignment, enabling fine-grained insights into VLM reasoning dynamics.

The explainability theme connects to both reliability and safety concerns: by tracing systematic misalignment and diagnosing hallucination and bias, explainability frameworks like GLIMPSE provide tools for ensuring transparency in VLM deployments. The emphasis on model-agnostic approaches suggests the field values interpretability methods applicable across diverse architectures rather than model-specific solutions.

### Theme 5: Domain-Specific Applications and Adaptations

The surveyed literature demonstrates VLM adaptation to specialized domains beyond general-purpose multimodal understanding. Basu Bir et al. (2026) show that carefully adapted lightweight VLMs (up to 7B parameters) can provide sustainable, private alternatives to commercial APIs for OCR-to-structure extraction in heritage digitization, extracting text and generating schema-compliant JSON from document images. Their work addresses data autonomy concerns and environmental footprint of hyperscale computing while maintaining high performance through classical image preprocessing and hyperparameter optimization.

Similarly, Sapkota & Karkee (2025) examine VLMs for object detection, finding that large vision-language models revolutionize the field by enhancing adaptability, contextual reasoning, and generalization beyond traditional architectures. This application-focused research demonstrates VLMs' versatility while highlighting domain-specific challenges in real-time performance and output flexibility.

### Theme 6: Safety-Aware Architectures

A forward-looking theme concerns proactive safety integration rather than reactive mitigation. Poppi et al. (2025) introduce HySAC (Hyperbolic Safety-Aware CLIP), which encodes safe and unsafe content as an entailment hierarchy in hyperbolic space, shifting from unlearning unsafe concepts to awareness-based discrimination. This paradigm enables dynamic redirection of unsafe queries toward safer alternatives while preserving the model's capacity to discern between safe and unsafe content, establishing a more adaptable and interpretable framework for content moderation.

The safety-aware approach represents a conceptual shift from defensive postures toward architectural integration of safety considerations, leveraging hyperbolic geometry's capacity for hierarchical entailment relations that Euclidean embeddings cannot effectively model.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key findings. First, there is broad agreement that VLMs have achieved impressive multimodal capabilities but face critical reliability challenges requiring architectural and methodological innovations. Second, multiple papers confirm that interpretability and explainability remain underdeveloped relative to raw performance capabilities. Third, the literature consistently finds that domain-specific adaptation—whether in medicine, heritage digitization, or object detection—requires careful consideration of trade-offs between generalization and specialization. Fourth, there is consensus that training-free or lightweight interventions can meaningfully improve VLM behavior without requiring full model retraining, suggesting practical pathways for deployment improvement.

**Disagreements**: The surveyed literature shows limited direct disagreement, likely reflecting the early stage of many research directions. However, implicit tensions exist between specialization and generalization approaches: medical VLM research (Jang et al., 2026; Kalpelbe et al., 2025) emphasizes domain-specific adaptation, while explainability work (Shen, 2025) and reliability frameworks (Sanogo & Ardiccioni, 2025) pursue model-agnostic solutions applicable across architectures. The field has not yet resolved whether optimal VLM development prioritizes domain specialization or general-purpose adaptability with targeted interventions.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, the Expert-Lay Gap in medical VLMs (Jang et al., 2026) highlights a broader challenge: VLMs' inability to adapt their output register for different audiences, a capability critical for democratizing AI access. Second, while multiple papers identify adversarial vulnerabilities (Vice et al., 2025; Arokiaraj et al., 2026), the literature lacks consensus on robust architectural solutions beyond detection and mitigation. Third, explainability methods (Shen, 2025) demonstrate feasibility but require broader validation across diverse VLM architectures and tasks. Fourth, safety-aware architectures (Poppi et al., 2025) remain nascent, with limited empirical validation of their effectiveness in real-world deployment scenarios. Finally, the reliance on arXiv preprints means many findings await peer-reviewed validation, and the rapid pace of VLM development risks obsolescence of specific architectural recommendations.

## Per-Paper Annotations

### Arokiaraj et al. (2026)

**Research question**: Why do vision-language models show a dissociation between corrupted internal representations during training and correct outputs during free generation?
**Methodology**: The authors conducted a controlled two-stage PGD attack on 200 held-out COCO images using Qwen2.5-VL-7B-Instruct, analyzing image-level pixel statistics, using the logit lens to localize the train/inference gap, and tracking target-token rank across all 28 LLM decoder layers.
**Key findings**:
- Image-level pixel statistics have essentially no predictive power over which images are corrupted (best predictor r=-0.050, ridge regression R^2=0.069).
- The train/inference gap localizes to a single autoregressive step where the target token rank is fixed at exactly 3,488 out of 152,064 vocabulary entries for every image with zero variance.
- The visual encoder corrupts every image's representation by a comparable margin, but the language model decoder differentially arbitrates by amplifying or suppressing the corrupted signal.
- A linear probe on the merger hidden state separates susceptible and resistant outcomes with AUC=0.858.
- Adversarial robustness in autoregressive VLMs is substantially a property of the language decoder's prior, not the visual encoder.
**Limitations**: The linear probe AUC estimate has a flagged circularity concern that needs further investigation.

### Basu Bir et al. (2026)

**Research question**: Can open-source lightweight vision-language models provide a sustainable, private alternative to commercial APIs for OCR-to-structure extraction in heritage digitization?
**Methodology**: The authors present a comparative study of eight open-source lightweight VLMs (up to 7B parameters) for OCR-to-structure across three university heritage collections, evaluating models under a constraint-aware protocol across zero-shot, few-shot, and fine-tuning settings using CER, ANLS*, and mAP-F1 metrics, while testing the impact of hyperparameter optimization, classical image preprocessing, and multi-stage training.
**Key findings**:
- Carefully adapted VLMs with up to 7B parameters can provide a sustainable, private, high-performing alternative to manual transcription or commercial black-box systems.
- Models can extract text and generate schema-compliant JSON from document images, enabling automatic validation and downstream use.
- Joint training enables one model to operate across collections but can shift performance between datasets.
- Classical image preprocessing techniques (illumination flattening, denoising, CLAHE) and hyperparameter optimization independently impact extraction quality.
- The approach addresses data autonomy concerns, recurring costs, and environmental footprint of hyperscale computing in heritage digitization.
**Limitations**: Not stated in abstract

### Jang et al. (2026)

**Research question**: Can medical vision-language models (Med-VLMs) generate patient-accessible descriptions that bridge the Expert-Lay Gap in medical communication?
**Methodology**: The paper introduces MedLayXPlain, a large-scale multimodal benchmark with 122,789 region-grounded samples across 8 imaging modalities, using a Hierarchical Ontology-Verified Refinement (HOVER) pipeline combining patient-centric vocabulary mapping, LLM-based constrained rewriting, and cross-model visual verification. The study also introduces MedLayEval, a 3B evaluator distilled from a 27B verifier to score expert-lay alignment across five clinically grounded attributes, and benchmarks 33 VLMs on the dataset.
**Key findings**:
- Medical VLMs achieve strong expert-level performance but their ability to generate patient-accessible descriptions remains underexplored.
- There is a systematic Expert-Lay Gap: medical VLMs achieve strong expert captioning but suffer significant lay-register degradation.
- General-purpose VLMs produce more accessible language yet lack clinical precision.
- Neither current paradigm (medical VLMs nor general-purpose VLMs) adequately serves patient-facing communication.
- The benchmark spans 7 semantic groups, 43 semantic types, and 2,411 medical concepts across 12 publicly available source datasets.
**Limitations**: The study confirms that neither current VLM paradigm adequately serves patient-facing communication, indicating a gap in existing approaches.

### Kalpelbe et al. (2025)

**Research question**: What are the current advancements, applications, challenges, and future directions of Medical Vision-Language Models in healthcare?
**Methodology**: This survey provides an extensive review of recent advancements in Medical Vision-Language Models, discussing foundational technology, illustrating how general models are adapted for complex medical tasks, and examining their applications in healthcare through a comprehensive literature review.
**Key findings**:
- Med-VLMs integrate visual and textual data to enhance healthcare outcomes across clinical practice, education, and patient care.
- Key challenges include data scarcity, narrow task generalization, interpretability issues, and ethical concerns like fairness, accountability, and privacy.
- Limitations are exacerbated by uneven dataset distribution, computational demands, and regulatory hurdles.
- Future directions include leveraging large-scale diverse datasets, improving cross-modal generalization, and enhancing interpretability.
- Innovations like federated learning, lightweight architectures, and EHR integration are pathways to democratize access and improve clinical relevance.
**Limitations**: The survey identifies that rigorous evaluation methods and robust regulatory frameworks are essential for safe integration into healthcare workflows, indicating current gaps in these areas.

### Poppi et al. (2025)

**Research question**: How can hyperbolic space be leveraged to create safety-aware vision-language models that discern between safe and unsafe content rather than simply unlearning unsafe concepts?
**Methodology**: The authors introduce HySAC (Hyperbolic Safety-Aware CLIP), which encodes safe and unsafe content as an entailment hierarchy in different regions of hyperbolic space using entailment loss functions to model hierarchical and asymmetrical relations between safe and unsafe image-text pairs.
**Key findings**:
- The hyperbolic space approach enables modeling of entailment hierarchies that is ineffective in standard vision-language models due to their reliance on Euclidean embeddings.
- HySAC serves as both a multimodal unsafe classifier and a flexible content retriever.
- The model can dynamically redirect unsafe queries toward safer alternatives or retain the original output.
- The approach enhances safety recognition while establishing a more adaptable and interpretable framework for content moderation.
- The paradigm shifts from unlearning to awareness, preserving the model's capacity to discern between safe and unsafe content.
**Limitations**: Not stated in abstract

### Sanogo & Ardiccioni (2025)

**Research question**: How can hallucinations in vision-language models (VLMs) be reduced without requiring model retraining?
**Methodology**: The paper proposes a training-free self-correction framework enabling VLMs to iteratively refine responses through uncertainty-guided visual re-attention, combining multidimensional uncertainty quantification (token entropy, attention dispersion, semantic consistency, claim confidence) with attention-guided cropping of under-explored regions. The approach operates entirely with frozen, pretrained VLMs without gradient updates and is validated on POPE and MMHAL BENCH benchmarks using Qwen2.5-VL-7B.
**Key findings**:
- The proposed method reduces hallucination rates by 9.8 percentage points compared to the baseline.
- Object existence accuracy improves by 4.7 points on adversarial splits.
- Uncertainty-guided re-attention successfully grounds corrections in visual evidence where standard decoding fails.
- The framework operates entirely with frozen, pretrained VLMs requiring no gradient updates.
- Qualitative analysis confirms the method's effectiveness in reducing hallucinated content.
**Limitations**: Validation is currently limited to Qwen2.5-VL-7B architecture, with plans to extend validation across diverse architectures in future versions.

### Sapkota & Karkee (2025)

**Research question**: How do large vision-language models (LVLMs) enhance object detection compared to traditional deep learning architectures?
**Methodology**: This paper presents a structured three-step research review process examining the state-of-the-art in LVLMs for object detection, including analysis of architectural innovations, training paradigms, and output flexibility. The review includes comprehensive visualizations and comparative analysis of real-time performance, adaptability, and complexity against traditional systems.
**Key findings**:
- LVLMs revolutionize object detection by enhancing adaptability, contextual reasoning, and generalization beyond traditional architectures.
- LVLMs integrate visual and textual information to achieve advanced contextual understanding for object detection and localization.
- LVLMs demonstrate effectiveness in diverse scenarios including localization and segmentation tasks.
- LVLMs are expected to meet or surpass the performance of conventional methods in object detection.
- Current LVLM modes have identified limitations, and the paper proposes solutions and a roadmap for future advancement.
**Limitations**: The review identifies major limitations of current LVLM modes but specific details are not elaborated in the abstract.

### Shen (2025)

**Research question**: How can we interpret where large vision-language models (LVLMs) direct their visual attention to understand model behavior in visual question answering?
**Methodology**: The paper introduces GLIMPSE, a lightweight, model-agnostic framework that jointly attributes LVLM outputs to the most relevant visual evidence and textual signals using gradient-weighted attention, adaptive layer propagation, and relevance-weighted token aggregation to produce holistic response-level heat maps for interpreting cross-modal reasoning.
**Key findings**:
- GLIMPSE produces holistic response-level heat maps for interpreting cross-modal reasoning in LVLMs.
- The framework outperforms prior methods in faithfulness and pushes the state-of-the-art in human-attention alignment.
- GLIMPSE enables fine-grained insights into LVLM cross-modal attribution and reasoning dynamics.
- The method can trace systematic misalignment, diagnose hallucination and bias, and ensure transparency.
- GLIMPSE is a lightweight, model-agnostic framework applicable to open-ended generation tasks.
**Limitations**: Not stated in abstract

### Vice et al. (2025)

**Research question**: How vulnerable are vision-language models (VLMs) to subtle, structured perturbations in the frequency domain when performing visual content reasoning tasks?
**Methodology**: The study designs targeted image transformations operating in the frequency domain to systematically adjust VLM outputs when exposed to frequency-perturbed real and synthetic images, testing generalization across five state-of-the-art VLMs including Qwen2/2.5 and BLIP models. Experiments were conducted across ten real and generated image datasets under realistic, black-box constraints.
**Key findings**:
- VLMs exhibit critical vulnerabilities when exposed to subtle, structured perturbations in the frequency domain.
- Feature transformations in the frequency domain undermine authenticity/DeepFake detection and automated image captioning tasks.
- The perturbation injection method generalizes across five state-of-the-art VLMs including different-parameter Qwen2/2.5 and BLIP models.
- VLM judgments are sensitive to frequency-based cues and may not wholly align with semantic content.
- Visually-imperceptible spatial frequency transformations expose the fragility of VLMs deployed for automated image captioning and authenticity detection tasks.
**Limitations**: The study operates under realistic, black-box constraints, but specific limitations of the methodology are not stated in the abstract.

### Ye et al. (2025)

**Research question**: What is the color vision capacity of large vision-language models, and how can their performance on color vision tests be improved?
**Methodology**: The authors defined a color vision testing task for large vision-language models and constructed a dataset covering multiple categories of test questions and tasks of varying difficulty levels, then analyzed error types and proposed fine-tuning strategies to enhance performance.
**Key findings**:
- The color vision abilities of large vision-language models have not been thoroughly explored prior to this work.
- A comprehensive color vision test dataset was constructed with multiple categories and varying difficulty levels.
- Error analysis reveals specific types of mistakes made by large vision-language models in color vision tasks.
- Fine-tuning strategies can enhance model performance in color vision tests.
**Limitations**: Not stated in abstract

## References

Arokiaraj, A. J., Wu, Z., & Koshiyama, A. (2026). Corrupted but correct: Why vision-language models lie to themselves internally. arXiv. https://arxiv.org/abs/2610.03445

Basu Bir, U., Christlein, V., Maier, A., & Zinnen, M. (2026). From pixels to structure: Lightweight vision-language models for document OCR and structured JSON extraction. arXiv. https://arxiv.org/abs/2610.11818

Jang, H., Lee, J., Kim, S., Lim, C. Y., Goh, H., Eum, H., & Choi, K. S. (2026). MedLayXPlain: Benchmarking the expert-lay gap in medical vision-language models. arXiv. https://arxiv.org/abs/2606.21194

Kalpelbe, B. C., Adaambiik, A. G., & Peng, W. (2025). Vision language models in medicine. arXiv. https://arxiv.org/abs/2503.01863

Poppi, T., Kasarla, T., Mettes, P., Baraldi, L., & Cucchiara, R. (2025). Hyperbolic safety-aware vision-language models. arXiv. https://arxiv.org/abs/2503.12127

Sanogo, K., & Ardiccioni, R. (2025). Toward more reliable artificial intelligence: Reducing hallucinations in vision-language models. arXiv. https://arxiv.org/abs/2512.07564

Sapkota, R., & Karkee, M. (2025). Object detection with multimodal large vision-language models: An in-depth review. arXiv. https://arxiv.org/abs/2508.19294

Shen, G. (2025). GLIMPSE: Holistic cross-modal explainability for large vision-language models. arXiv. https://arxiv.org/abs/2506.18985

Vice, J., Akhtar, N., Gao, Y., Hartley, R., & Mian, A. (2025). On the reliability of vision-language models under adversarial frequency-domain perturbations. arXiv. https://arxiv.org/abs/2507.22398

Ye, H., Chen, B., Liu, W., Zhang, Y., Li, Z., Ni, D., & Chen, H. (2025). Assessing color vision test in large vision-language models. arXiv. https://arxiv.org/abs/2507.11153
