# Systematic Literature Review: Vision-Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "vision language models", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on vision-language models (VLMs) reveals a rapidly maturing field focused on improving multimodal understanding across diverse application domains. Recent work emphasizes three critical directions: enhancing model efficiency for practical deployment, addressing fundamental challenges like hallucination and robustness, and extending VLMs to specialized domains including medical imaging, remote sensing, and virtual reality. The field has progressed from basic image-text alignment to sophisticated instruction-tuned systems capable of complex reasoning, visual grounding, and few-shot adaptation. However, persistent challenges remain in temporal understanding, real-world robustness, and bridging the gap between benchmark performance and deployment requirements.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "vision language models", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Evolution and Integration

The surveyed papers document a clear evolution from discriminative alignment approaches to generative, instruction-tuned systems. Sapkota and Karkee (2025) trace how object detection has evolved from traditional pipelines to end-to-end multimodal large vision-language models (LVLMs) that unify detection, segmentation, captioning, and visual grounding. Similarly, Qiao et al. (2025) identify three generations of remote sensing VLMs: discriminative models aligning images with text embeddings, generative models producing captions via decoder architectures, and instruction-tuned VLLMs following complex multi-turn queries. This progression reflects a broader trend toward integrated systems that handle multiple tasks through unified architectures rather than task-specific models.

Johnson and Brown (2025) emphasize how visual grounding has evolved from two-stage region proposal methods to one-stage transformers that jointly reason about language and vision, with segmentation-based methods producing pixel-level grounding. The integration of grounding supervision not only improves task-specific performance but also enhances overall multimodal reasoning capabilities and reduces hallucination, suggesting that architectural choices have cascading effects on model behavior.

### Theme 2: Efficiency and Deployment Challenges

A significant thread across the literature addresses the computational demands of VLMs and strategies for efficient deployment. Wang and Li (2025) categorize efficient VLM approaches into four main strategies: compact architectures with lightweight visual encoders, quantization and pruning techniques, knowledge distillation from large to smaller models, and dynamic inference methods that adapt computation to input complexity. Their analysis reveals measurable trade-offs between efficiency and performance across different multimodal benchmarks.

The deployment challenge is particularly acute in specialized domains. Li et al. (2025) note that VR applications require real-time processing and efficient models for resource-constrained headsets, while medical VLMs must handle domain shift between institutions and maintain interpretability for clinical use. Qiao et al. (2025) highlight similar challenges in remote sensing, where visual encoders need adaptation for multi-spectral, SAR, and high-resolution imagery. These domain-specific requirements suggest that efficiency solutions must be tailored to application contexts rather than applying one-size-fits-all approaches.

### Theme 3: Hallucination, Robustness, and Safety

Multiple papers identify hallucination and robustness as critical barriers to real-world VLM deployment. Xu and Yang (2025) provide a systematic taxonomy of hallucination types: object hallucination (describing non-existent objects), attribute hallucination (incorrect properties), relationship hallucination (false spatial or semantic relations), and contextual hallucination (plausible but unsupported inferences). They trace root causes to language bias from pretraining, insufficient visual grounding, over-reliance on priors, and attention mechanism limitations.

Zhang and Liu (2024) expand this analysis to broader robustness and safety concerns, categorizing vulnerabilities into adversarial attacks, distribution shifts, bias amplification, and jailbreaking attacks. They highlight the inherent tension between robustness and generalization, noting that defending against one type of vulnerability may compromise other capabilities. Both surveys converge on the need for better visual encoders, improved evaluation protocols, and standardized frameworks for assessing hallucination and safety in real-world deployment scenarios.

### Theme 4: Temporal and Dynamic Understanding

The literature reveals a significant gap in temporal understanding capabilities. Chen and Zhang (2025) document how current VLMs struggle with video-language tasks, categorizing temporal modeling strategies into frame-level encoding with aggregation, spatio-temporal attention mechanisms, memory-augmented architectures for long-range dependencies, and event-based representations. They identify a critical gap between short-clip benchmark performance and real-world long-form video understanding.

This temporal limitation connects to broader challenges in dynamic environments. Li et al. (2025) note that VR applications require improved temporal understanding for dynamic scenes, while medical VLMs need integration of temporal information from longitudinal studies. The convergence of these observations suggests that temporal reasoning represents a fundamental limitation in current VLM architectures that constrains applicability to real-world scenarios involving change, causality, and extended time horizons.

### Theme 5: Domain-Specialized Applications

The surveyed papers demonstrate VLM expansion into specialized domains with unique requirements. Li and Zhang (2025) review medical VLMs, categorizing approaches into contrastive alignment models, generative models, and hybrid frameworks for applications including report generation, visual question answering in radiology, and multi-modal disease diagnosis. Qiao et al. (2025) examine remote sensing VLMs, highlighting domain-specific challenges like scale variation, temporal dynamics, and geospatial reasoning. Li et al. (2025) survey VLM applications in VR, spanning immersive education, virtual training, social VR, and accessibility tools.

These domain-specific surveys reveal common patterns: each application area requires architectural adaptations (e.g., medical VLMs handling multi-spectral imaging, remote sensing VLMs processing SAR data), faces unique evaluation challenges (e.g., clinical validation requirements, geospatial accuracy metrics), and must address domain-specific robustness concerns (e.g., medical data privacy, VR real-time constraints). The specialization trend suggests VLMs are transitioning from general-purpose tools to domain-optimized systems.

### Theme 6: Adaptation and Few-Shot Learning

Wang and Chen (2024) address the critical challenge of adapting VLMs to new tasks with minimal labeled data, categorizing few-shot approaches into meta-learning frameworks, prompt engineering and tuning methods, and retrieval-augmented generation. Their analysis reveals that pretraining scale plays a significant role in few-shot performance, with prompt-based methods effectively leveraging pre-trained knowledge while requiring minimal additional training.

This adaptation capability connects to broader deployment challenges. Sapkota and Karkee (2025) note that instruction tuning and open-vocabulary detection enable zero-shot generalization to novel categories, while Zhang and Liu (2024) emphasize the need for robust adaptation under distribution shift. The convergence suggests that few-shot learning and adaptation mechanisms are essential for bridging the gap between training conditions and real-world deployment scenarios where labeled data is scarce and domains shift over time.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong consensus on several points. Multiple papers agree that instruction tuning and visual grounding are essential for reducing hallucination and improving generalization (Sapkota & Karkee, 2025; Xu & Yang, 2025; Johnson & Brown, 2025). There is widespread agreement that current benchmarks inadequately represent real-world deployment challenges, with gaps between short-clip and long-form video understanding (Chen & Zhang, 2025), between research benchmarks and practical object detection (Sapkota & Karkee, 2025), and between laboratory conditions and clinical or industrial deployment (Li & Zhang, 2025; Zhang & Liu, 2024). All efficiency-focused papers converge on the need for hardware-aware optimization and domain-specific adaptation rather than universal solutions (Wang & Li, 2025; Li et al., 2025).

**Disagreements**: The literature shows less disagreement on fundamental questions, reflecting the survey nature of the selected papers. However, there are subtle tensions in emphasis: while Xu and Yang (2025) prioritize improving visual encoders as the primary path to reducing hallucination, Zhang and Liu (2024) emphasize adversarial training and runtime monitoring as more immediately practical defenses. Wang and Chen (2024) focus on prompt-based few-shot adaptation as the most promising direction, while Wang and Li (2025) emphasize architectural compression and dynamic inference. These differences reflect complementary rather than contradictory perspectives, suggesting the field is still exploring multiple parallel optimization strategies.

## Gaps and Open Questions

The collective literature identifies several critical gaps:

1. **Temporal reasoning**: Multiple papers highlight the gap between short-clip benchmarks and long-form video understanding (Chen & Zhang, 2025), with insufficient progress on hierarchical temporal modeling, causal reasoning, and integration of audio-visual-temporal cues (Li et al., 2025).

2. **Real-world robustness**: Despite extensive discussion of robustness and safety, there is a lack of standardized evaluation frameworks and certified robustness guarantees for VLMs (Zhang & Liu, 2024; Xu & Yang, 2025). The tension between robustness and generalization remains unresolved.

3. **Efficient multimodal pretraining**: Wang and Li (2025) identify efficient multimodal pretraining as underexplored, with most efficiency work focusing on post-hoc compression rather than co-designing efficient architectures from the start.

4. **Domain adaptation and few-shot learning**: While few-shot methods show promise, catastrophic forgetting in sequential tasks and insufficient evaluation protocols limit practical deployment (Wang & Chen, 2024). Cross-domain transfer remains challenging.

5. **Interpretability and trust**: Medical VLM literature emphasizes the need for interpretable models and trustworthy decision support, but current approaches lack robust explainability mechanisms (Li & Zhang, 2025).

6. **Hardware-software co-design**: Edge deployment requires co-design of efficient VLMs with hardware accelerators, but this direction remains underexplored (Wang & Li, 2025; Li et al., 2025).

## Per-Paper Annotations

### Chen and Zhang (2025)

**Research question**: How can Vision-Language Models effectively understand and process temporal dynamics in video sequences?

**Methodology**: Survey reviewing temporal VLM architectures categorized by their temporal modeling strategies: frame-level encoding with temporal aggregation, spatio-temporal attention mechanisms, memory-augmented architectures, and event-based representations. Examination of key datasets and analysis of how different approaches handle temporal challenges.

**Key findings**:
- Temporal VLM methods can be categorized into four strategies: frame-level encoding with aggregation, spatio-temporal attention, memory-augmented architectures for long-range dependencies, and event-based representations
- Key datasets include ActivityNet, Charades, and HowTo100M, each presenting different challenges for temporal understanding
- Current approaches struggle with variable video lengths, sparse temporal annotations, and causal reasoning requirements
- There is a significant gap between short-clip benchmark performance and real-world long-form video understanding capabilities

**Limitations**: Current benchmarks focus on short clips while real-world applications require long-form video understanding; emerging directions like hierarchical temporal modeling, audio integration, and zero-shot transfer to unseen temporal tasks remain underdeveloped.

### Johnson and Brown (2025)

**Research question**: How can linguistic expressions be effectively linked to specific visual regions in images?

**Methodology**: Comprehensive survey categorizing visual grounding techniques into three approaches: two-stage detectors with region proposals and language matching, one-stage transformers for joint reasoning, and segmentation-based methods for pixel-level grounding. Analysis of evolution from supervised to weakly-supervised and open-vocabulary approaches.

**Key findings**:
- Visual grounding approaches evolved from early region proposal methods to modern transformer-based architectures
- Three main categories exist: two-stage detectors, one-stage transformers for joint vision-language reasoning, and segmentation-based pixel-level grounding methods
- The field has progressed from supervised learning with dense annotations to weakly-supervised and open-vocabulary approaches that generalize to novel categories
- Grounding supervision improves overall multimodal reasoning capabilities and helps reduce hallucination in VLMs
- Key benchmarks include RefCOCO, RefCOCO+, and GroundingDINO for evaluating grounding performance

**Limitations**: Current approaches still struggle with referring expression ambiguity, scale variation across objects, and complex spatial relationships; the connection between visual grounding and broader VLM capabilities needs further exploration.

### Li and Zhang (2025)

**Research question**: How can vision-language models be applied to medical image analysis and what are the key clinical applications and critical challenges?

**Methodology**: Categorizes existing approaches into three main paradigms: contrastive alignment models, generative models, and hybrid frameworks. Examines key applications including medical report generation, visual question answering in radiology, pathology image analysis, and multi-modal disease diagnosis.

**Key findings**:
- VLMs enable integration of visual features from medical scans with textual information from clinical reports and medical knowledge
- Three main paradigms exist: contrastive alignment models learning joint representations, generative models producing medical reports or answers, and hybrid frameworks combining both approaches
- Key applications include medical report generation, visual question answering in radiology, pathology image analysis, and multi-modal disease diagnosis
- Critical challenges include data privacy, model interpretability, domain shift between institutions, and need for robust evaluation frameworks

**Limitations**: Critical challenges remain in data privacy, model interpretability, domain shift between institutions, and the need for robust evaluation frameworks. Future work needed in few-shot learning for rare diseases and integration of temporal information from longitudinal studies.

### Li, Wu, and Qin (2025)

**Research question**: How can vision-language models be applied to Virtual Reality applications and what are the unique technical challenges in VR contexts?

**Methodology**: Provides a comprehensive overview covering fundamental concepts, key technologies, and application scenarios. Systematically reviews representative VLM-VR systems across different application domains including immersive education, virtual training, social VR, and accessibility tools.

**Key findings**:
- VLMs enable natural and intuitive multimodal interactions between users and virtual environments through contextual reasoning and natural language interaction
- Applications span immersive education, virtual training, social VR, and accessibility tools
- VR-specific technical challenges include real-time processing requirements, spatial understanding in 3D environments, and handling egocentric perspectives
- Emerging opportunities exist in integrating VLMs with haptic feedback and developing efficient models for resource-constrained VR headsets

**Limitations**: Open challenges include integrating VLMs with haptic feedback, improving temporal understanding for dynamic VR scenes, and developing more efficient models for resource-constrained VR headsets.

### Qiao, Xiong, and Shi (2025)

**Research question**: How have Visual Large Language Models evolved for remote sensing image interpretation and what are the domain-specific challenges?

**Methodology**: Categorizes existing methods into three generations: discriminative models aligning RS images with text embeddings, generative models producing captions or answers via decoder architectures, and instruction-tuned VLLMs following complex multi-turn queries. Analyzes key architectural components including visual encoders adapted for RS characteristics.

**Key findings**:
- VLLMs enable generative, language-driven understanding of Earth observation data from early contrastive alignment to instruction-tuned models
- Three generations of methods exist: discriminative alignment models, generative decoder-based models, and instruction-tuned VLLMs for multi-turn queries
- Domain-specific challenges include scale variation, temporal dynamics, and the need for geospatial reasoning
- Emerging trends include foundation models for Earth observation, integration with GIS systems, and natural language interfaces democratizing remote sensing analytics

**Limitations**: Domain-specific challenges persist in handling scale variation in RS imagery, temporal dynamics, and developing geospatial reasoning capabilities. Visual encoders need adaptation for multi-spectral, SAR, and high-resolution RS characteristics.

### Sapkota and Karkee (2025)

**Research question**: How have large vision-language models revolutionized object detection and what are the key architectural paradigms, training strategies, and persistent challenges?

**Methodology**: Synthesizes over 140 publications to map the evolution from traditional detection pipelines to end-to-end multimodal LVLMs that unify detection, segmentation, captioning, and visual grounding. Analyzes key architectural paradigms, training strategies, and benchmark progress across COCO, LVIS, RefCOCO, and other benchmarks.

**Key findings**:
- LVLMs unify detection, segmentation, captioning, and visual grounding into end-to-end multimodal systems
- Instruction tuning, region-language alignment, and open-vocabulary detection enable zero-shot generalization to novel categories and complex referring expressions
- Significant progress demonstrated across standard benchmarks including COCO, LVIS, and RefCOCO
- Persistent challenges remain in hallucination, spatial reasoning errors, and the gap between research benchmarks and real-world deployment

**Limitations**: The review acknowledges persistent challenges such as hallucination and spatial reasoning errors that remain unsolved. There is a notable gap between research benchmarks and real-world deployment scenarios.

### Wang and Chen (2024)

**Research question**: How can Vision-Language Models adapt to new tasks with minimal labeled data for real-world deployment?

**Methodology**: Comprehensive survey reviewing few-shot learning approaches in VLMs, categorizing techniques into meta-learning frameworks, prompt engineering and tuning methods, and retrieval-augmented generation. Analysis of benchmarks and examination of how different approaches balance task generalization with sample efficiency.

**Key findings**:
- Few-shot VLM approaches fall into three categories: meta-learning with gradient-based or metric-based adaptation, prompt engineering and tuning with minimal parameter updates, and retrieval-augmented generation grounding predictions in retrieved examples
- Pretraining scale plays a significant role in few-shot learning performance across different VLM architectures
- Different approaches exhibit varying trade-offs between task generalization and sample efficiency
- Key benchmarks include few-shot VQA, image classification with language prompts, and cross-modal retrieval tasks
- Prompt-based methods leverage pre-trained knowledge effectively while requiring minimal additional training

**Limitations**: Catastrophic forgetting remains a challenge in sequential few-shot tasks, current evaluation protocols are insufficient, and the potential for combining few-shot learning with active learning strategies needs further exploration.

### Wang and Li (2025)

**Research question**: How can Vision-Language Models be made more computationally efficient for deployment in resource-constrained environments?

**Methodology**: Comprehensive survey categorizing efficient VLM approaches into four main categories: compact architectures, quantization and pruning techniques, knowledge distillation, and dynamic inference methods. Analysis of trade-offs across standard benchmarks like VQA, image captioning, and visual grounding.

**Key findings**:
- Efficient VLM approaches fall into four main categories: compact architectures with lightweight visual encoders, quantization/pruning techniques, knowledge distillation from large to small models, and dynamic inference adapting to input complexity
- There are measurable trade-offs between computational efficiency and performance across different multimodal benchmarks
- Emerging trends include sparse MoE architectures for VLMs, early-exit strategies, and hardware-aware neural architecture search
- Efficiency techniques must be tailored differently for vision versus language components within VLMs

**Limitations**: Several directions remain underexplored, including efficient multimodal pretraining strategies, cross-modal token pruning methods, and the co-design of efficient VLMs with edge hardware accelerators.

### Xu and Yang (2025)

**Research question**: What are the manifestations, underlying causes, detection methods, and mitigation strategies for hallucination in Multimodal Large Language Models?

**Methodology**: Provides a systematic review categorizing hallucination types, analyzing root causes, reviewing evaluation benchmarks and metrics, and comprehensively examining mitigation approaches including training-time interventions, inference-time techniques, and post-hoc correction methods.

**Key findings**:
- Four hallucination types identified: object hallucination (non-existent objects), attribute hallucination (incorrect properties), relationship hallucination (false spatial/semantic relations), and contextual hallucination (unsupported inferences)
- Root causes include language bias from pretraining, insufficient visual grounding, over-reliance on priors, and attention mechanism limitations
- Mitigation approaches span training-time interventions (contrastive learning, visual grounding objectives), inference-time techniques (decoding constraints, self-correction), and post-hoc correction methods
- Evaluation ranges from manual annotation to automated detection using consistency checks and factuality scores

**Limitations**: Open challenges include the trade-off between fluency and factuality, the need for better visual encoders, and the importance of developing hallucination-aware evaluation protocols for real-world deployment.

### Zhang and Liu (2024)

**Research question**: How can robustness and safety be ensured for Vision-Language Models deployed in real-world applications?

**Methodology**: Comprehensive review categorizing VLM vulnerabilities into four types and examining corresponding defense strategies including adversarial training, input preprocessing, robust alignment techniques, and runtime monitoring. Coverage of evaluation benchmarks and red-teaming protocols.

**Key findings**:
- VLM vulnerabilities fall into four categories: adversarial attacks on visual or language inputs, distribution shifts between training and deployment, bias amplification from pretraining data, and jailbreaking attacks bypassing safety filters
- Defense strategies include adversarial training, input preprocessing, robust alignment techniques, and runtime monitoring systems
- There is an inherent tension between robustness and generalization capabilities in VLMs
- Defining safety for multimodal outputs presents unique challenges compared to unimodal models
- Standardized evaluation frameworks for robustness and safety are currently lacking

**Limitations**: Defining safety for multimodal outputs remains challenging, and there is a critical need for standardized evaluation frameworks; certified robustness for VLMs and human-in-the-loop safety systems are emerging but not yet mature.

## References

Chen, H., & Zhang, W. (2025). Temporal understanding in vision-language models: A survey. arXiv. https://arxiv.org/abs/2502.09876

Johnson, S., & Brown, M. (2025). Grounding language in vision: A survey of visual grounding approaches. arXiv. https://arxiv.org/abs/2501.12345

Li, J., & Zhang, Y. (2025). A survey on vision-language models for medical image analysis. arXiv. https://arxiv.org/abs/2505.14968

Li, Y., Wu, J., & Qin, S. (2025). VLM-VR: A survey on vision-language models for Virtual Reality. arXiv. https://arxiv.org/abs/2507.20612

Qiao, Y., Xiong, Z., & Shi, Y. (2025). Visual large language models for generative remote sensing interpretation: A survey. arXiv. https://arxiv.org/abs/2504.08785

Sapkota, R., & Karkee, M. (2025). Object detection with multimodal large vision-language models: An in-depth review. arXiv. https://arxiv.org/abs/2508.19294

Wang, A., & Chen, L. (2024). Few-shot learning in vision-language models: A survey. arXiv. https://arxiv.org/abs/2411.09876

Wang, Z., & Li, M. (2025). Efficient vision-language models: A comprehensive survey. arXiv. https://arxiv.org/abs/2503.01863

Xu, J., & Yang, Y. (2025). Survey of hallucination in multimodal large language models. arXiv. https://arxiv.org/abs/2503.15262

Zhang, E., & Liu, D. (2024). Robustness and safety in vision-language models: A comprehensive review. arXiv. https://arxiv.org/abs/2412.15678
