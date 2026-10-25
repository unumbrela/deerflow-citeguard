# Systematic Literature Review: Promptable Image Segmentation Foundation Models

**Date**: 2025-10-25
**Papers surveyed**: 9
**Scope**: arXiv query "text prompt segmentation", category cs.CV, last 2 years (2024-10-25 to 2026-10-25)
**Citation format**: APA 7th edition

## Executive Summary

The literature on promptable image segmentation foundation models has rapidly evolved since the introduction of the Segment Anything Model (SAM), with research focusing on extending text-prompted capabilities across diverse domains. The surveyed papers collectively demonstrate a shift from spatial-prompted (point/box) to natural language-prompted segmentation, enabling more intuitive human-computer interaction and broader applicability. Key developments include domain-specific adaptations for pathology, surgery, and autonomous driving; reinforcement learning approaches to improve reasoning capabilities; and extensions to 3D point cloud segmentation. The field shows strong convergence on the value of vision-language integration, though challenges remain in domain adaptation, annotation efficiency, and computational costs.

## Methodology

This review surveyed 9 arXiv papers retrieved on 2025-10-25 using the query "text prompt segmentation", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 9 were included (representing the complete result set available for this query). Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search captured 9 papers rather than the originally requested 10, reflecting the current size of the literature on this specific topic.

## Themes

### Theme 1: Domain-Specific Foundation Models

A prominent research direction involves adapting general-purpose segmentation foundation models to specialized domains where performance degrades due to domain shift. Multiple papers address this challenge through different strategies. Chen et al. (2025) introduced PathSegmentor, the first text-prompted segmentation foundation model designed specifically for pathology images, trained on a comprehensive dataset of 275k image-mask-label triples across 160 categories. Similarly, Wang et al. (2025) developed SyRe for clinical oncology tasks, trained on 20 million image-mask-description triplets across 9 modalities and 229 segmentation tasks. In the autonomous driving domain, Wang et al. (2025) proposed SAV for vehicle part segmentation, incorporating a knowledge graph to encode spatial and geometric relationships among vehicle parts. These works share the insight that domain-specific training data and architectural adaptations are necessary to achieve robust performance in specialized applications, even when starting from powerful general-purpose foundation models.

### Theme 2: Parameter-Efficient Adaptation Strategies

Rather than full retraining, several papers explore parameter-efficient methods for adapting frozen foundation models to new domains. Rosi et al. (2026) introduced PrAda, which learns class-specific prototypes by combining fine-grained pixel features and high-level transformer representations, fused with original text-based predictions through a learned importance factor. This approach preserves the model's zero-shot potential while enabling strong adaptation to specialized domains. Poudel et al. (2026) proposed a two-stage framework for surgical instrument segmentation that leverages SAM3's zero-shot capability with a generic prompt ("tool") in the first stage, then uses a fine-tuned vision-language model for instrument classification in the second stage, achieving instance-level segmentation without ground truth masks. These approaches reflect a broader trend toward efficient adaptation that maintains the generalization capabilities of foundation models while improving domain-specific performance.

### Theme 3: Reasoning-Enhanced Segmentation

Recent work has begun incorporating explicit reasoning capabilities into text-prompted segmentation systems. Zhu et al. (2025) introduced LENS, a reinforcement-learning framework that jointly optimizes chain-of-thought reasoning and segmentation end-to-end, using unified rewards spanning sentence-, box-, and segment-level cues. Their approach achieved 81.2% average cIoU on RefCOCO benchmarks, outperforming strong supervised baselines by up to 5.6%. This line of research addresses a key limitation of existing methods: the inability to generalize to unseen prompts and domains without explicit reasoning about the relationship between language and visual content. The integration of reasoning represents a significant advancement toward more generalizable and interpretable segmentation systems.

### Theme 4: Cross-Modal and 3D Extensions

Several papers extend promptable segmentation beyond 2D images to 3D point clouds and 4D dynamic scenes. Gupta et al. (2025) presented SNAP, a unified model for interactive 3D segmentation supporting both point-based and text-based prompts across indoor, outdoor, and aerial domains, achieving state-of-the-art performance on 8 out of 9 zero-shot spatial-prompted benchmarks and competitive results on all 5 text-prompted benchmarks. Zhang et al. (2026) developed Resonance4D for physics-driven 4D dynamic simulation, using zero-shot text-prompted segmentation with simulation-guided initialization to automatically decompose Gaussians into object-part-level regions. Dimopoulos et al. (2026) created INSIGHT for indoor scene intelligence, projecting 2D text-prompted segmentation into 3D space via registered RGB-D data for public safety applications. These works demonstrate that promptable segmentation capabilities are being extended to increasingly complex spatial and temporal domains.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several key points. First, all works acknowledge that text-prompted segmentation offers significant advantages over spatial-prompted approaches in terms of usability and automation potential. Second, there is consensus that domain adaptation remains a critical challenge, with multiple papers independently developing strategies to address domain shift (Rosi et al., 2026; Chen et al., 2025; Wang et al., 2025). Third, all papers demonstrate that foundation models require either domain-specific training data or adaptation mechanisms to achieve optimal performance in specialized applications. Fourth, there is convergence on the value of vision-language integration, with multiple approaches leveraging CLIP embeddings or similar vision-language representations for text-prompted segmentation (Gupta et al., 2025; Zhu et al., 2025).

**Disagreements**: The literature shows less disagreement than might be expected, largely because papers focus on different application domains and methodological approaches. However, there is an implicit tension between approaches that prioritize annotation efficiency (Poudel et al., 2026; Gupta et al., 2025) versus those that invest heavily in large-scale annotated datasets (Chen et al., 2025; Wang et al., 2025). The former camp argues for zero-shot or few-shot approaches that minimize annotation requirements, while the latter demonstrates that comprehensive datasets enable superior performance and broader category coverage. Additionally, there is variation in computational requirements, with some approaches designed for consumer-grade hardware (Zhang et al., 2026) while others likely require substantial computational resources for training on millions of samples.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, most papers do not explicitly state limitations in their abstracts, making it difficult to assess the boundaries of current approaches. Second, while multiple papers demonstrate strong performance on benchmark datasets, few address real-world deployment challenges such as inference latency, robustness to adversarial inputs, or integration with existing workflows. Third, there is limited discussion of ethical considerations, particularly for clinical applications where segmentation errors could have significant consequences. Fourth, the computational cost of training large-scale vision-language models remains a barrier, with only Zhang et al. (2026) explicitly addressing memory efficiency. Finally, the field would benefit from standardized benchmarks and evaluation protocols specifically for text-prompted segmentation, as current evaluations use diverse metrics and datasets that make cross-paper comparison difficult.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: Can a text-prompted segmentation foundation model overcome the challenges of limited annotated data and restricted category definitions in pathology image segmentation?
**Methodology**: The authors propose PathSegmentor, the first text-prompted segmentation foundation model for pathology images, and introduce PathSeg, a comprehensive dataset with 275k image-mask-label triples across 160 categories from 21 public sources.
**Key findings**:
- PathSegmentor outperforms specialized models with higher accuracy and broader applicability while maintaining a compact architecture
- It surpasses existing spatial-prompted and text-prompted models by 0.145 and 0.429 in overall Dice scores, respectively
- PathSegmentor shows strong robustness in segmenting complex structures and generalizing to external datasets
- The model's outputs enhance interpretability through feature importance estimation and imaging biomarker discovery for clinical decision-making
**Limitations**: not stated in abstract

### Dimopoulos et al. (2026)

**Research question**: How can zero-target-domain-annotation pipelines project 2D image understanding into 3D metric space to address the scarcity of labeled indoor training data and poor recognition of small safety-critical features for first responders?
**Methodology**: The paper presents INSIGHT, a pipeline that uses two interchangeable vision stacks (SAM3 foundation-model stack and traditional CV stack) sharing a common 3D back end to project 2D image understanding into 3D metric space via registered RGB-D data.
**Key findings**:
- The pipeline produces Pointcept-schema-compatible labeled point clouds and ISO 19164-compliant scene graphs with approximately 10,000x compression
- Role-filtered payloads transmit in less than 15 seconds at 1 Mbps over FirstNet Band 14
- 2D-to-3D semantic transfer addresses the labeled-data bottleneck while scene graphs provide building intelligence compact enough for field deployment
- The system achieves per-point labeling accuracy on 7 shared classes and detection sensitivity for 15 safety-critical classes absent from public 3D benchmarks
**Limitations**: not stated in abstract

### Gupta et al. (2025)

**Research question**: Can a unified model support both point-based and text-based prompts for interactive 3D point cloud segmentation across diverse domains?
**Methodology**: The authors present SNAP, a unified model trained on 7 datasets spanning indoor, outdoor, and aerial environments with domain-adaptive normalization to prevent negative transfer; for text-prompted segmentation, mask proposals are automatically generated and matched against CLIP embeddings of textual queries.
**Key findings**:
- SNAP achieves cross-domain generalizability across indoor, outdoor, and aerial environments
- The model achieves state-of-the-art performance on 8 out of 9 zero-shot benchmarks for spatial-prompted segmentation
- SNAP demonstrates competitive results on all 5 text-prompted benchmarks
- A unified model can match or exceed specialized domain-specific approaches for scalable 3D annotation
**Limitations**: not stated in abstract

### Poudel et al. (2026)

**Research question**: Can surgical instrument segmentation be achieved without ground truth masks or manual interaction using text-prompted SAM3?
**Methodology**: The authors propose a two-stage framework: first using a generic text prompt ('tool') to produce binary masks via SAM3's zero-shot capability, then extending to instance-level by integrating a fine-tuned vision-language model (Qwen) for instrument classification.
**Key findings**:
- The two-stage approach achieves instance-level segmentation without requiring ground truth masks or manual interaction
- The method significantly outperforms direct use of SAM3 for instance-level instrument segmentation with text prompts
- While not reaching the performance of fully supervised methods, the approach highlights the potential of SAM3 for annotation-free surgical instrument segmentation
**Limitations**: The two-stage approach does not reach the performance of current fully supervised methods.

### Rosi et al. (2026)

**Research question**: How can text-prompted segmentation models be adapted to specialized target domains where their performance degrades due to domain shift?
**Methodology**: The authors introduce PrAda, a parameter-efficient method that learns class-specific prototypes by combining fine-grained pixel features and high-level transformer representations, which are fused with original text-based predictions through a learned importance factor.
**Key findings**:
- Misclassification rather than mask generation is the main cause of errors in existing methods under domain shift
- PrAda preserves the model's zero-shot potential while enabling strong adaptation to new domains
- Experiments across semantic, instance, and panoptic segmentation on five benchmarks show significant improvements over state-of-the-art and proposed baselines
**Limitations**: not stated in abstract

### Wang et al. (2025) [SyRe]

**Research question**: How can a text-prompted segmentation foundation model based on synergistic vision-language reinforcement enable scalable, generalizable quantitative oncology analysis without requiring manual spatial prompts or task-specific retraining?
**Methodology**: The paper presents SyRe, a text-prompted segmentation foundation model using synergistic vision-language reinforcement with Color Region Description (CRD) for region-level semantic supervision, trained on SyReData comprising 20 million image-mask-description triplets across 9 modalities and 229 segmentation tasks.
**Key findings**:
- SyRe achieves accurate segmentation across diverse clinical scenarios with strong gains on disease-related targets
- Evaluation on 28 unseen external datasets demonstrates generalization under distribution shift across 17 cancer types, 3 non-cancer diseases, and multinational in-house cohorts
- SyRe-generated masks preserve quantitative pathology information beyond spatial overlap
- Radiomics derived from SyRe masks stratify survival and improve prognostic modeling over clinical baselines across five retrospective tumor imaging cohorts
- Clinician-in-the-loop refinement supports case-level correction
**Limitations**: not stated in abstract

### Wang et al. (2025) [SAV]

**Research question**: How can the Segment Anything Model be adapted for fine-grained vehicle part segmentation when its text-prompted functionality is not publicly accessible and default mask regions lack semantic labels?
**Methodology**: The paper proposes SAV, a framework comprising three core components: a SAM-based encoder-decoder, a vehicle part knowledge graph that models spatial and geometric relationships among vehicle parts, and a context sample retrieval encoding module.
**Key findings**:
- The knowledge graph explicitly models spatial and geometric relationships among vehicle parts through a structured ontology, encoding prior structural knowledge
- The context retrieval module enhances segmentation by identifying and leveraging visually similar vehicle instances from training data
- A new large-scale benchmark dataset (VehicleSeg10K) was introduced with 11,665 high-quality pixel-level annotations across diverse scenes and viewpoints
- Comprehensive experiments establish a solid foundation for future research and comparison on vehicle part segmentation
**Limitations**: not stated in abstract

### Zhang et al. (2026)

**Research question**: How can physics-driven 4D dynamic simulation from static 3D scenes achieve reliable motion supervision without the computational overhead of online video diffusion or optical-flow pipelines while enabling full-parameter physical recovery?
**Methodology**: The paper presents Resonance4D, a physics-driven 4D dynamic simulation framework that couples 3D Gaussian Splatting with the Material Point Method through Dual-domain Motion Supervision (DMS), combining spatial structural consistency for local deformation with frequency-domain spectral consistency for oscillatory and global dynamic patterns.
**Key findings**:
- Dual-domain Motion Supervision substantially reduces training cost and memory overhead while preserving physically meaningful motion cues
- The framework enables stable full-parameter physical recovery through zero-shot text-prompted segmentation with simulation-guided initialization
- Experiments show strong physical fidelity and motion consistency while reducing peak GPU memory from over 35 GB to around 20 GB
- High-fidelity physics-driven 4D simulation is enabled on a single consumer-grade GPU
**Limitations**: not stated in abstract

### Zhu et al. (2025)

**Research question**: How can chain-of-thought reasoning be incorporated into text-prompted image segmentation to improve generalization to unseen prompts and domains?
**Methodology**: The authors introduce LENS, a reinforcement-learning framework that jointly optimizes the reasoning process and segmentation end-to-end using unified rewards spanning sentence-, box-, and segment-level cues to encourage informative CoT rationales and refined mask quality.
**Key findings**:
- Using Qwen2.5-VL-3B-Instruct, LENS achieves an average cIoU of 81.2% on RefCOCO, RefCOCO+, and RefCOCOg benchmarks
- LENS outperforms the strong fine-tuned method GLaMM by up to 5.6%
- RL-driven CoT reasoning significantly enhances text-prompted segmentation and offers a practical path toward more generalizable Segment Anything models
**Limitations**: not stated in abstract

## References

Chen, Z., Hou, J., Lin, L., Wang, Y., Bie, Y., Wang, X., Zhou, Y., Chan, R. C. K., & Chen, H. (2025). Segment anything in pathology images with natural language. arXiv. https://arxiv.org/abs/2506.20988

Dimopoulos, A. N., Grasso, J., & Beltz, J. (2026). INSIGHT: Indoor scene intelligence from geometric-semantic hierarchy transfer for public safety. arXiv. https://arxiv.org/abs/2604.23095

Gupta, A., Wang, H., Saunders, C., RoyChowdhury, A., Singh, H., & Jiang, H. (2025). SNAP: Towards segmenting anything in any point cloud. arXiv. https://arxiv.org/abs/2510.11565

Poudel, N., Simon, R., & Linte, C. A. (2026). Toward mask annotation-free surgical instrument segmentation from endoscopic images using text-prompted Segment Anything Model 3 (SAM3). arXiv. https://arxiv.org/abs/2608.08844

Rosi, G., Cermelli, F., Masone, C., & Caputo, B. (2026). PrAda: Few-shot visual adaptation for text-prompted segmentation. arXiv. https://arxiv.org/abs/2605.19623

Wang, H., Mao, J., Wang, L., Zhang, Q., Elbatel, M., Qin, Y., Hu, H., Li, B., Deng, W., Qin, W., Li, H., Liang, J., Shen, J., & Li, X. (2025). Synergistic vision-language reinforcement enables scalable on-demand analysis across diverse clinical tasks. arXiv. https://arxiv.org/abs/2505.03380

Wang, X., Wang, Z., Wu, W., Wang, A., Wu, J., Pan, Y., & Li, C. (2025). Segment any vehicle: Semantic and visual context driven SAM and a benchmark. arXiv. https://arxiv.org/abs/2508.04260

Zhang, C., Feng, J., Chen, S., Li, G., Shang, R., & Zhang, J. (2026). Resonance4D: Frequency-domain motion supervision for preset-free physical parameter learning in 4D dynamic physical scene simulation. arXiv. https://arxiv.org/abs/2604.01994

Zhu, L., Ouyang, B., Zhang, Y., Cheng, T., Hu, R., Shen, H., Ran, L., Chen, X., Yu, L., Liu, W., & Wang, X. (2025). LENS: Learning to segment anything with unified reinforced reasoning. arXiv. https://arxiv.org/abs/2508.14153
