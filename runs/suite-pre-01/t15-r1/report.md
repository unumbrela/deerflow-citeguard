# Systematic Literature Review: Promptable Image Segmentation Foundation Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "promptable segmentation" query, cs.CV category, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Promptable image segmentation has evolved significantly since the introduction of the Segment Anything Model (SAM), with recent research focusing on three major directions: extending segmentation capabilities to specialized domains (particularly medical imaging), improving prompt generation and robustness, and enabling 3D and multi-view consistency. The surveyed literature from 2024-2026 reveals a field transitioning from general-purpose segmentation toward domain-specific adaptations that address real-world deployment challenges. Medical imaging applications dominate, with multiple papers adapting promptable segmentation for CT, PET, and cancer segmentation tasks using minimal expert-curated data. Simultaneously, researchers are addressing fundamental limitations in prompt quality, robustness to natural variations, and semantic understanding, introducing novel evaluation benchmarks that reveal gaps between mask accuracy and true concept grounding.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "promptable segmentation", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search query may not capture all relevant papers using alternative terminology such as "interactive segmentation" or "Segment Anything."

## Themes

### Theme 1: Medical Imaging Applications and Domain Adaptation

A substantial portion of recent work adapts promptable segmentation foundation models to medical imaging domains, where annotation costs are prohibitive and data availability is limited. Three papers exemplify this trend, each addressing different imaging modalities and clinical workflows.

Church et al. (2026) introduced SAM2CT for converting sparse radiological annotations (line measurements and arrows stored as GSPS objects in PACS systems) into full 3D CT lesion segmentations. Their approach extends SAM2's prompt encoder to support arrow and line inputs and introduces Memory-Conditioned Memories (MCM) tailored to 3D medical volumes, achieving Dice scores of 0.649 for arrow prompts and 0.757 for line prompts on public benchmarks. Similarly, Zhang et al. (2025) developed SegAnyPET for PET image segmentation, incorporating a dual-stream encoder that fuses functional and structural information with cross-attention for prompt-guided refinement, demonstrating superior generalization to unseen organs and imaging protocols.

Karam et al. (2025) took a different approach, showing that promptable cancer segmentation can be achieved with only 24 fully-segmented images plus 8 weakly-labeled images for training—up to 100× less data than conventional methods. Their method leverages two classifiers (weakly-supervised and fully-supervised) to refine segmentation through a guided search initiated by a single-point prompt, performing comparably to fully-supervised methods for prostate cancer segmentation. Collectively, these works demonstrate that promptable segmentation can be adapted to medical domains with minimal annotation burden, enabling scalable dataset generation from historical clinical archives.

### Theme 2: Prompt Generation Optimization and Hallucination Management

Several papers address the fundamental challenge of generating high-quality prompts without manual intervention, particularly for task-generic segmentation where a single prompt must guide segmentation across diverse instances.

Hu et al. (2025) introduced INT (Instance-specific Negative Mining for Task-Generic Promptable Segmentation), which adaptively reduces the influence of irrelevant prior knowledge while amplifying plausible knowledge selected through negative mining with higher contrast. Their approach consists of instance-specific prompt generation that progressively filters incorrect information, and semantic mask generation ensuring alignment between prompts and segmentation semantics, validated across six datasets including camouflaged objects and medical images.

In complementary work, Hu et al. (2024) proposed ProMaC, an iterative Prompt-Mask Cycle framework that leverages MLLM hallucinations rather than eliminating them. Their key insight is that hallucinations represent pre-trained large-scale knowledge beyond individual images; by initially exploring hallucinations through multi-scale chain-of-thought prompting, then reducing them to formulate precise instance-specific prompts, their method achieves better prompts and masks through iterative refinement across five benchmarks. This represents a paradigm shift from hallucination suppression to strategic utilization of MLLM-generated contextual insights.

### Theme 3: 3D and Multi-view Consistency

Extending promptable segmentation from 2D images to 3D scenes and multi-view settings presents unique challenges in maintaining geometric consistency across views without costly per-scene optimization.

Jeong et al. (2026) introduced MV-SAM, which achieves 3D-consistent multi-view segmentation using pointmaps—3D points reconstructed from unposed images by visual geometry models. By lifting image embeddings into 3D point embeddings and decoding them through a transformer with cross-attention to 3D prompt embeddings, MV-SAM eliminates the need for explicit 3D networks or annotated 3D data while outperforming SAM2-Video and matching per-scene optimization baselines across NVOS, SPIn-NeRF, ScanNet++, uCo3D, and DL3DV benchmarks.

For autonomous driving applications, recent work demonstrated training-free open-vocabulary 3D detection by using SAM3 queried with class names as text prompts to supply instance masks from six surround-view cameras, then converting masks to metric 3D boxes using scene geometry (Anonymous, 2026). Their controlled comparison on nuScenes revealed that fitting boxes from raw LiDAR points within SAM3 masks achieves 0.298 mAP at zero labeling cost, while borrowing supervised box geometry at inference lifts performance to 0.413 mAP—locating the pipeline's largest deficit in measurement precision rather than 2D detection.

### Theme 4: Robustness Evaluation and Concept Grounding

As promptable segmentation models mature, researchers are developing sophisticated evaluation frameworks that probe beyond traditional mask accuracy metrics to assess real-world robustness and semantic understanding.

Moskalenko et al. (2026) introduced BREPS (Bounding-Box Robustness Evaluation of Promptable Segmentation) to investigate model sensitivity to natural variations in bounding box prompts. Their user study collecting thousands of real bounding box annotations revealed substantial variability in segmentation quality across users for the same model and instance, indicating high sensitivity to natural prompt noise. BREPS reformulates robustness evaluation as a white-box optimization problem over the bounding box prompt space, generating adversarial boxes that minimize or maximize segmentation error while adhering to naturalness constraints, benchmarked across 10 datasets from everyday scenes to medical imaging.

Liang et al. (2026) introduced CAFE (Counterfactual Attribute Factuality Evaluation), a benchmark probing whether promptable segmentation models faithfully ground queried concepts or rely on visually salient but semantically misleading cues. Built on attribute-level counterfactual manipulation with 2,146 paired test samples across three categories (Superficial Mimicry, Context Conflict, and Ontological Conflict), CAFE reveals a systematic gap between localization quality and concept discrimination: models often generate accurate masks even for misleading prompts, suggesting strong mask prediction does not imply faithful semantic grounding.

### Theme 5: Multimodal Integration

Beyond visual-only prompts, researchers are exploring integration of additional modalities to enhance segmentation capabilities while preserving interactive efficiency.

Liu et al. (2025) proposed AuralSAM2 to integrate audio into SAM2 while preserving its promptable segmentation capability. Their AuralFuser module fuses audio and visual features to generate sparse and dense prompts, propagating auditory cues across visual layers via SAM2's feature pyramid. An audio-guided contrastive loss emphasizes auditory relevance in dominant visual features, achieving notable accuracy gains on public benchmarks with minimal impact on interactive efficiency—addressing the audio prompt dilution problem that plagues adapter-based methods.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key points. First, all medical imaging papers agree that minimal annotation strategies are essential for clinical deployment, with consensus that promptable segmentation can leverage sparse or historical annotations to generate dense segmentations at scale (Church et al., 2026; Karam et al., 2025; Zhang et al., 2025). Second, there is agreement that prompt quality fundamentally limits segmentation performance, motivating multiple approaches to optimize prompt generation without manual intervention (Hu et al., 2024; Hu et al., 2025). Third, researchers consistently find that traditional evaluation metrics (mask accuracy, Dice scores) are insufficient for assessing real-world robustness and semantic understanding, motivating new benchmark frameworks (Liang et al., 2026; Moskalenko et al., 2026).

**Disagreements**: The literature shows limited direct disagreement, as papers focus on different application domains and evaluation criteria. However, there is implicit tension between approaches that seek to eliminate MLLM hallucinations versus those that strategically leverage them: while conventional wisdom treats hallucinations as errors to suppress, Hu et al. (2024) demonstrate they can provide valuable contextual insights when properly managed. Additionally, the 3D detection work suggests measurement precision is the primary bottleneck (Anonymous, 2026), while multi-view segmentation work emphasizes 3D consistency through geometric lifting (Jeong et al., 2026)—these represent different framings of the core challenge in extending promptable segmentation to 3D.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

**Limited cross-domain generalization studies**: While multiple papers demonstrate strong in-domain performance, few systematically evaluate transfer across vastly different domains (e.g., from natural images to medical imaging, or from static images to video). The medical imaging papers each focus on specific modalities (CT, PET, prostate) without unified frameworks for cross-modality adaptation.

**Computational efficiency and deployment considerations**: None of the surveyed papers provide detailed analysis of computational costs, inference latency, or memory requirements—critical factors for clinical or edge deployment. The focus on accuracy improvements leaves open questions about practical deployment constraints.

**Long-tail class performance**: The open-vocabulary 3D detection work notes that failures occur for "misnamed or geometrically unforgiving" classes (Anonymous, 2026), but systematic analysis of long-tail performance across diverse object categories remains absent.

**User interaction modeling**: While BREPS reveals sensitivity to natural prompt variations (Moskalenko et al., 2026), none of the papers incorporate user modeling or adaptive prompt refinement based on user feedback—suggesting a gap in human-in-the-loop optimization.

**Theoretical foundations**: The field lacks theoretical understanding of why certain prompt types (boxes vs. points vs. text) work better for different object classes or domains, relying instead on empirical comparisons.

## Per-Paper Annotations

### Anonymous (2026)

**Research question**: Can open-vocabulary 3D object detection for autonomous vehicles be solved without training, using only promptable segmentation?
**Methodology**: Uses SAM3 prompted with class names as text to generate instance masks from six surround-view cameras, then converts masks to metric 3D boxes using scene geometry, employing controlled three-stage comparison on nuScenes.
**Key findings**:
- Image-only geometry prediction reaches 0.183 mAP under the official protocol
- Training-free LiDAR point fitting within SAM3 masks achieves 0.298 mAP / 0.348 NDS at zero labeling cost
- Borrowing supervised box geometry at inference lifts performance to 0.413 mAP / 0.555 NDS
- A three-state camera-witness rule improves supervised LiDAR-only detector from 0.596 to 0.630 mAP with no training
- SAM3 finds 84% of in-range objects with correctly named masks
**Limitations**: The pipeline's largest deficit lies in measurement precision rather than 2D detection; class confusion and confidence calibration issues persist even when geometry is improved.

### Church, S., Warner, J. D., Maqbool, D., Tie, X., Hu, J., Lubner, M. G., & Bradshaw, T. J. (2026)

**Research question**: Can sparse radiological annotations (line measurements and arrows) stored in PACS be converted into 3D CT segmentations using promptable segmentation models?
**Methodology**: Proposed SAM2CT, extending SAM2's prompt encoder to support arrow and line inputs with Memory-Conditioned Memories (MCM) for 3D medical volumes.
**Key findings**:
- Achieves Dice scores of 0.649 for arrow prompts and 0.757 for line prompts on public benchmarks
- Outperforms existing promptable segmentation models and similarly trained baselines
- Generates clinically acceptable segmentations in 87% of cases from pre-existing GSPS annotations
- Demonstrates strong zero-shot performance on Emergency Department findings
- Enables scalable dataset generation from historical clinical archives
**Limitations**: Clinical validation limited to specific lesion types; generalizability to rare pathologies not demonstrated.

### Hu, J., Cheng, Z., & Gong, S. (2025)

**Research question**: How can task-generic promptable segmentation improve instance-specific prompt generation when VLMs struggle to generalize to certain image instances?
**Methodology**: Introduced INT with two components: instance-specific prompt generation that progressively filters incorrect information, and semantic mask generation ensuring alignment with prompt semantics through negative mining.
**Key findings**:
- Adaptively reduces influence of irrelevant prior knowledge while amplifying plausible knowledge
- Validated on six datasets including camouflaged objects and medical images
- Demonstrates effectiveness, robustness, and scalability across diverse domains
- Improves segmentation quality for challenging instances where VLMs fail
- Enables task-generic prompts to work across diverse image instances
**Limitations**: Performance depends on VLM quality for initial prompt generation; may struggle with entirely novel object categories.

### Hu, J., Lin, J., Yan, J., & Gong, S. (2024)

**Research question**: Can MLLM hallucinations be leveraged strategically to improve promptable segmentation rather than eliminated?
**Methodology**: Proposed ProMaC, an iterative Prompt-Mask Cycle framework using multi-scale chain-of-thought prompting to explore hallucinations for contextual knowledge extraction, then reducing them to precise prompts.
**Key findings**:
- Hallucinations reveal valuable contextual insights representing pre-trained large-scale knowledge
- Iterative refinement produces jointly better prompts and masks
- Multi-scale chain-of-thought prompting extracts extended contextual knowledge
- Mask semantic alignment ensures consistency with task semantics
- Demonstrated effectiveness across five benchmarks
**Limitations**: Requires careful tuning of hallucination exploration-exploitation balance; may introduce computational overhead from iterative cycles.

### Jeong, Y., Sun, C., Wang, Y.-C. F., Cho, M., & Choe, J. (2026)

**Research question**: How can multi-view segmentation achieve 3D consistency without costly per-scene optimization or explicit 3D networks?
**Methodology**: Introduced MV-SAM leveraging pointmaps to lift image embeddings into 3D point embeddings, decoded by transformer with cross-attention to 3D prompt embeddings and positional embeddings.
**Key findings**:
- Trained on SA-1B dataset, generalizes well across domains without per-scene optimization
- Outperforms SAM2-Video on multi-view segmentation benchmarks
- Achieves comparable performance to per-scene optimization baselines across five benchmarks
- Eliminates need for explicit 3D networks or annotated 3D data
- 3D positional embeddings enable implicit learning of consistent masks across views
**Limitations**: Code not yet released at time of publication; depends on external visual geometry models for pointmap generation.

### Karam, L., Wang, Y., Kasivisvanathan, V., Rusu, M., Hu, Y., & Saeed, S. U. (2025)

**Research question**: Can promptable cancer segmentation be achieved with minimal expert-curated annotated data while maintaining high quality standards?
**Methodology**: Proposed approach requiring only 24 fully-segmented and 8 weakly-labeled images, leveraging two classifiers to refine segmentation through guided search initiated by single-point prompt.
**Key findings**:
- Outperforms existing promptable segmentation methods for prostate cancer segmentation
- Performs comparably to fully-supervised methods using up to 100× less annotated data
- Minimal data requirement enables high-quality curation mitigating inter-observer variability
- Single-point prompt initiation makes approach practical for clinical settings
- Enables promptable segmentation with very minimal labeled data
**Limitations**: Evaluation focused on prostate cancer; generalizability to other cancer types or imaging modalities not demonstrated.

### Liang, S., Wang, Z., Li, Y., Liu, X., & Wang, H. (2026)

**Research question**: Do promptable segmentation models faithfully ground queried concepts, or rely on visually salient but semantically misleading cues?
**Methodology**: Introduced CAFE benchmark with 2,146 paired test samples using attribute-level counterfactual manipulation across three categories: Superficial Mimicry, Context Conflict, and Ontological Conflict.
**Key findings**:
- Reveals systematic gap between localization quality and concept discrimination
- Models generate accurate masks even for misleading prompts
- Strong mask prediction does not imply faithful semantic grounding
- Models rely on shortcut-driven mask retrieval rather than true concept understanding
- Provides controlled diagnostic tool for evaluating concept-faithful segmentation
**Limitations**: Benchmark evaluates existing models without proposing solutions; limited to designed counterfactual scenarios.

### Liu, Y., Chen, Y., Wang, C., Han, J., Wu, J., Peng, C., Chen, J., Tian, Y., & Carneiro, G. (2025)

**Research question**: How can audio be integrated into SAM2 for promptable segmentation while avoiding audio prompt dilution and preserving interactive efficiency?
**Methodology**: Proposed AuralSAM2 with AuralFuser module fusing audio and visual features via pyramid-based prompt propagation, with audio-guided contrastive loss for modality alignment.
**Key findings**:
- Achieves notable accuracy gains on public audio-visual segmentation benchmarks
- Preserves SAM2's promptable segmentation capability with minimal impact on interactive efficiency
- Pyramid-based propagation prevents audio prompt dilution plaguing adapter-based methods
- Audio-guided contrastive loss successfully aligns audio and visual modalities
- Code available at https://github.com/yyliu01/AuralSAM2
**Limitations**: Specific benchmark metrics not detailed; may have limited applicability beyond audio-visual scenarios.

### Moskalenko, A., Kuznetsov, D., Dudko, I., Iasakova, A., Boldyrev, N., Shepelev, D., Spiridonov, A., Kuznetsov, A., & Shakhuro, V. (2026)

**Research question**: How robust are promptable segmentation models to natural variations in bounding box prompts?
**Methodology**: Conducted user study collecting thousands of real bounding box annotations, then introduced BREPS reformulating robustness evaluation as white-box optimization over bounding box prompt space.
**Key findings**:
- Substantial variability in segmentation quality across users for same model and instance
- SAM-like models highly sensitive to natural prompt noise
- Bounding boxes outperform points while reducing annotation costs
- Benchmark spans 10 datasets from everyday scenes to medical imaging
- Code available at https://github.com/emb-ai/BREPS
**Limitations**: Exhaustive testing computationally prohibitive; naturalness constraints may not capture all real-world variations.

### Zhang, Y., Xue, L., Zhang, W., Li, L., Liu, Y., Jiang, C., Cheng, Y., & Qi, Y. (2025)

**Research question**: How can promptable segmentation be adapted to PET images with blurred anatomical boundaries and low-resolution functional information?
**Methodology**: Introduced SegAnyPET with dual-stream encoder fusing functional and structural information, cross-attention module for prompt-guided refinement, and multi-scale decoder for precise mask prediction.
**Key findings**:
- Achieves state-of-the-art performance on organ segmentation tasks
- Demonstrates superior generalization to unseen organs and imaging protocols
- Trained on comprehensive multi-organ PET dataset
- Addresses limitations of structural-image-focused medical adaptations
- Enables comprehensive multi-systemic analysis of organ-pathology interactions
**Limitations**: Performance on rare organs or unusual imaging protocols not evaluated; computational requirements for dual-stream encoding not analyzed.

## References

Anonymous. (2026). Training-free open-vocabulary 3D detection from promptable segmentation. arXiv. https://arxiv.org/abs/2609.19358

Church, S., Warner, J. D., Maqbool, D., Tie, X., Hu, J., Lubner, M. G., & Bradshaw, T. J. (2026). Opportunistic promptable segmentation: Leveraging routine radiological annotations to guide 3D CT lesion segmentation. arXiv. https://arxiv.org/abs/2602.00309

Hu, J., Cheng, Z., & Gong, S. (2025). INT: Instance-specific negative mining for task-generic promptable segmentation. arXiv. https://arxiv.org/abs/2501.18753

Hu, J., Lin, J., Yan, J., & Gong, S. (2024). Leveraging hallucinations to reduce manual prompt dependency in promptable segmentation. arXiv. https://arxiv.org/abs/2408.15205

Jeong, Y., Sun, C., Wang, Y.-C. F., Cho, M., & Choe, J. (2026). MV-SAM: Multi-view promptable segmentation using pointmap guidance. arXiv. https://arxiv.org/abs/2601.17866

Karam, L., Wang, Y., Kasivisvanathan, V., Rusu, M., Hu, Y., & Saeed, S. U. (2025). Promptable cancer segmentation using minimal expert-curated data. arXiv. https://arxiv.org/abs/2505.17915

Liang, S., Wang, Z., Li, Y., Liu, X., & Wang, H. (2026). From pixels to concepts: Do segmentation models understand what they segment? arXiv. https://arxiv.org/abs/2605.09591

Liu, Y., Chen, Y., Wang, C., Han, J., Wu, J., Peng, C., Chen, J., Tian, Y., & Carneiro, G. (2025). AuralSAM2: Enabling SAM2 hear through pyramid audio-visual feature prompting. arXiv. https://arxiv.org/abs/2506.01015

Moskalenko, A., Kuznetsov, D., Dudko, I., Iasakova, A., Boldyrev, N., Shepelev, D., Spiridonov, A., Kuznetsov, A., & Shakhuro, V. (2026). BREPS: Bounding-box robustness evaluation of promptable segmentation. arXiv. https://arxiv.org/abs/2601.15123

Zhang, Y., Xue, L., Zhang, W., Li, L., Liu, Y., Jiang, C., Cheng, Y., & Qi, Y. (2025). SegAnyPET: Universal promptable segmentation from positron emission tomography images. arXiv. https://arxiv.org/abs/2502.14351
