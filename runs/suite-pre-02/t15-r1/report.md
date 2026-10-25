# Systematic Literature Review: Promptable Image Segmentation Foundation Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "promptable segmentation", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on promptable image segmentation foundation models has evolved rapidly over the past two years, with the Segment Anything Model (SAM) family establishing a dominant paradigm for interactive, generalizable segmentation. The surveyed papers reveal a field focused on three primary directions: extending SAM's capabilities to new modalities (3D, multi-view, audio-visual, PET imaging), reducing annotation and prompt requirements through innovative training strategies, and critically evaluating what these models actually understand versus what they merely approximate. Collectively, the literature demonstrates that while promptable segmentation models achieve impressive mask quality, they often rely on visually salient cues rather than faithful semantic grounding, revealing a significant gap between localization accuracy and conceptual understanding. The field is increasingly moving toward training-free or minimal-data approaches that leverage pre-trained foundation models rather than requiring extensive supervised training.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "promptable segmentation", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search query may not capture all relevant work using alternative terminology such as "interactive segmentation" or "Segment Anything."

## Themes

### Theme 1: Medical Imaging Adaptation and Minimal-Data Training

A significant portion of recent work focuses on adapting promptable segmentation models to medical imaging domains, where annotation costs are prohibitively high and data exhibits fundamentally different characteristics than natural images. Multiple papers address this challenge through different strategies: leveraging existing sparse annotations, training on large-scale domain-specific datasets, or achieving strong performance with minimal curated data.

Church et al. (2026) introduced the concept of "Opportunistic Promptable Segmentation," extracting routine radiological annotations (line measurements and arrows) stored in PACS as GSPS objects and converting them into 3D segmentations using SAM2CT, a model that extends SAM2's prompt encoder to support these annotation types. Their approach achieved clinically acceptable segmentations in 87% of cases without requiring new manual annotations, demonstrating that historical clinical data represents an underutilized resource for training data generation.

Zhang et al. (2025) took a different approach with SegAnyPET, training a universal promptable segmentation foundation model on 10,000+ PET scans covering multiple organs and tracers. Unlike structural imaging modalities, PET images contain functional rather than anatomical information, requiring the model to learn segmentation cues from radio-tracer distribution patterns. Their model achieved state-of-the-art performance on multi-organ segmentation with strong zero-shot generalization to unseen organs and tracers.

Karam et al. (2025) demonstrated that promptable segmentation can be achieved with remarkably minimal data—only 24 fully-segmented images plus 8 weakly-labeled images for prostate cancer segmentation. Their method uses two classifiers (one weakly-supervised, one fully-supervised) to refine segmentation through a guided search process initiated by a single-point prompt, outperforming existing promptable methods while using up to 100× less annotated data than typical approaches.

These three papers collectively demonstrate that medical imaging applications of promptable segmentation can succeed through different data strategies: mining existing annotations, training on large domain-specific datasets, or achieving strong performance with minimal carefully-curated data.

### Theme 2: Cross-Modal and 3D Extensions

Beyond medical imaging, substantial research effort has focused on extending promptable segmentation beyond 2D images into multi-view, 3D, and cross-modal domains. The central challenge in this theme is maintaining consistency across views or modalities while preserving the interactive efficiency that makes promptable segmentation attractive.

Jeong et al. (2026) introduced MV-SAM for multi-view segmentation, achieving 3D consistency using pointmaps—3D points reconstructed from unposed images by visual geometry models. By lifting image embeddings from SAM's pretrained encoder into 3D point embeddings and decoding them with cross-attention to 3D prompt embeddings, MV-SAM eliminates the need for explicit 3D networks or annotated 3D data while outperforming SAM2-Video and matching per-scene optimization baselines across multiple benchmarks.

Rukhman et al. (2026) explored training-free open-vocabulary 3D detection for autonomous vehicles by querying SAM3 with class names as text prompts to generate instance masks from surround-view cameras, then converting masks to metric 3D boxes using scene geometry. Their training-free approach achieved 0.298 mAP using raw LiDAR points within SAM3 masks at zero labeling cost, revealing that the primary performance deficit lies in measurement precision rather than 2D detection capability.

Liu et al. (2025) extended promptable segmentation into the audio-visual domain with AuralSAM2, integrating audio into SAM2 while preserving its interactive efficiency. Their AuralFuser module addresses the "audio prompt dilution" problem where audio signals weaken as they propagate through network layers, using pyramid audio-visual feature prompting and an audio-guided contrastive loss to achieve notable accuracy gains with minimal impact on interactive efficiency.

These extensions share a common strategy: leveraging pre-trained foundation models and augmenting them with modality-specific components rather than training from scratch, enabling cross-modal capabilities while preserving the interactive promptable paradigm.

### Theme 3: Prompt Engineering and Automation

Reducing manual prompt dependency while improving prompt quality represents another major research direction. These works aim to make promptable segmentation more automated and robust to natural prompt variations that occur in real-world usage.

Hu et al. (2025) addressed task-generic promptable segmentation, where a single task description should segment diverse samples without instance-specific prompts. Their INT method introduces instance-specific negative mining that adaptively reduces irrelevant prior knowledge while increasing plausible prior knowledge through higher-contrast negative mining, validated across six datasets including camouflaged objects and medical images.

In earlier work, Hu et al. (2024) proposed ProMaC, which leverages MLLM hallucinations constructively rather than eliminating them. Their iterative Prompt-Mask Cycle uses multi-scale chain-of-thought prompting to initially explore hallucinations for extracting contextual knowledge, then reduces hallucinations to formulate precise instance-specific prompts. The generated masks iteratively refine the prompt generation process, demonstrating effectiveness across five benchmarks.

Moskalenko et al. (2026) critically examined prompt robustness with BREPS, revealing that SAM-like models are highly sensitive to natural bounding box prompt noise. Their user study collected thousands of real bounding box annotations, showing substantial variability in segmentation quality across users for the same model and instance. They reformulated robustness evaluation as a white-box optimization problem, generating adversarial bounding boxes that reveal model vulnerabilities while maintaining naturalness constraints.

These papers collectively reveal that prompt quality and robustness remain critical bottlenecks, with successful approaches either automating prompt generation through iterative refinement or explicitly evaluating and improving robustness to natural prompt variations.

### Theme 4: Conceptual Understanding and Semantic Grounding

The most critical theme emerging from recent literature questions whether promptable segmentation models truly understand what they segment or merely exploit visually salient shortcuts. This theme represents a maturation of the field from asking "does it work?" to "why does it work?"

Liang et al. (2026) introduced CAFE (Counterfactual Attribute Factuality Evaluation), a benchmark with 2,146 paired test samples built on attribute-level counterfactual manipulation. Their evaluation revealed a systematic gap between localization quality and concept discrimination: models often generate accurate masks even for misleading prompts, suggesting strong mask prediction does not imply faithful semantic grounding. This finding challenges the assumption that promptable segmentation models ground high-level textual concepts rather than relying on superficial visual cues.

This theme connects to broader questions about foundation model understanding raised across multiple papers. Rukhman et al. (2026) noted that SAM3 finds 84% of in-range objects with correctly named masks, but failures occur on misnamed or geometrically challenging classes rather than truly unseen objects. Moskalenko et al. (2026) demonstrated that models are highly sensitive to natural prompt variations, suggesting brittle rather than robust understanding of segmentation tasks.

The converging evidence suggests that while promptable segmentation models achieve impressive practical performance, their semantic grounding remains incomplete, relying on visually salient cues that can fail under counterfactual or adversarial conditions.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that promptable segmentation foundation models, particularly the SAM family, provide a powerful base for diverse applications but require domain-specific adaptation or augmentation. Multiple papers converge on the strategy of extending pre-trained models rather than training from scratch (Church et al., 2026; Jeong et al., 2026; Liu et al., 2025; Rukhman et al., 2026). There is also broad agreement that annotation costs remain a primary bottleneck, particularly in medical imaging, motivating approaches that leverage existing annotations or minimize required labeled data (Church et al., 2026; Karam et al., 2025; Zhang et al., 2025).

**Disagreements**: The literature reveals tension between approaches that assume promptable segmentation models have meaningful semantic understanding versus those that treat them as pattern-matching systems requiring careful constraint. Hu et al. (2024, 2025) assume MLLMs can generate meaningful instance-specific prompts from task-generic descriptions, while Liang et al. (2026) demonstrate that models fail to faithfully ground queried concepts under counterfactual evaluation. This disagreement reflects a deeper question about whether improving prompt generation (Hu et al.'s approach) or improving model understanding (the implicit goal of CAFE evaluation) represents the more promising research direction.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature:

1. **Semantic grounding mechanisms**: Despite impressive mask quality, models rely on visually salient shortcuts rather than faithful concept grounding (Liang et al., 2026). The field lacks approaches that explicitly train for semantic faithfulness rather than mask accuracy alone.

2. **Cross-domain generalization limits**: While multiple papers demonstrate zero-shot generalization to unseen organs, tracers, or object classes (Rukhman et al., 2026; Zhang et al., 2025), the boundaries of this generalization remain poorly understood. Karam et al. (2025) demonstrated their approach only on prostate cancer, leaving open whether minimal-data strategies generalize to other cancer types.

3. **Real-world prompt robustness**: BREPS revealed high sensitivity to natural bounding box variations (Moskalenko et al., 2026), but practical solutions remain limited. The field needs training strategies or inference-time methods that improve robustness without sacrificing the interactive efficiency that makes promptable segmentation attractive.

4. **Measurement precision in 3D applications**: Rukhman et al. (2026) identified measurement precision as the primary bottleneck in training-free 3D detection, not 2D segmentation quality. Bridging this gap requires either better geometry estimation from images or more effective fusion with sparse depth sensors.

5. **Audio-visual integration depth**: AuralSAM2 addresses audio prompt dilution (Liu et al., 2025), but the broader question of how to achieve deep multimodal understanding rather than shallow feature fusion remains open across all cross-modal extensions.

## Per-Paper Annotations

### Church et al. (2026)

**Research question**: Can sparse radiologist annotations (line measurements and arrows) stored in PACS as GSPS objects be extracted and converted into 3D segmentations using promptable segmentation models?

**Methodology**: SAM2CT extends SAM2 by modifying the prompt encoder to support arrow and line inputs, and introduces Memory-Conditioned Memories (MCM), a memory encoding strategy specifically tailored for 3D medical volumes to convert routine radiological annotations into 3D segmentations.

**Key findings**:
- Achieves Dice similarity coefficients of 0.649 for arrow prompts and 0.757 for line prompts on public lesion segmentation benchmarks
- Outperforms existing promptable segmentation models and similarly trained baselines
- 87% of 3D segmentations generated from 60 clinical PACS GSPS annotations were clinically acceptable or required only minor adjustments
- Demonstrates strong zero-shot performance on select Emergency Department findings
- Large-scale mining of historical GSPS annotations represents a promising and scalable approach for generating 3D CT segmentation datasets

**Limitations**: 13% of cases required more than minor adjustments, indicating the method is not universally applicable; zero-shot performance was only demonstrated on select Emergency Department findings rather than comprehensively.

### Hu et al. (2024)

**Research question**: Can MLLM hallucinations be leveraged constructively to reduce manual prompt dependency in task-generic promptable segmentation rather than being eliminated?

**Methodology**: ProMaC introduces an iterative Prompt-Mask Cycle generation framework with a prompt generator using multi-scale chain of thought prompting to initially explore hallucinations for extracting extended contextual knowledge, then reduces hallucinations to formulate precise instance-specific prompts, while a mask generator produces semantically aligned masks that iteratively refine the prompt generation process.

**Key findings**:
- MLLM hallucinations can reveal valuable contextual insights representing pre-trained large-scale knowledge beyond individual images when leveraged correctly
- The iterative cycle between prompt and mask generation progressively focuses on task-relevant image areas while reducing irrelevant hallucinations
- Multi-scale chain of thought prompting effectively extracts extended contextual knowledge from test images
- Experiments on 5 benchmarks demonstrate the effectiveness of the ProMaC framework
- The approach successfully reduces manual prompt dependency while improving segmentation accuracy

**Limitations**: The effectiveness depends on the quality of initial hallucinations and the MLLM's reasoning capabilities; the iterative process may increase computational overhead compared to single-pass methods.

### Hu et al. (2025)

**Research question**: How can we improve instance-specific prompt generation for task-generic promptable segmentation when Vision-Language Models struggle to generalize to certain image instances?

**Methodology**: INT introduces instance-specific negative mining that adaptively reduces the influence of irrelevant prior knowledge while increasing the use of plausible prior knowledge through higher-contrast negative mining. The approach consists of two components: instance-specific prompt generation that progressively filters incorrect information, and semantic mask generation that ensures segmentation matches the semantics of instance-specific prompts.

**Key findings**:
- INT effectively addresses poor instance-specific prompt prediction when VLMs struggle to generalize to certain image instances
- The negative mining approach successfully increases contrast to select more plausible prior knowledge
- Validated across six diverse datasets including camouflaged objects and medical images
- Demonstrates strong effectiveness, robustness, and scalability in task-generic promptable segmentation

**Limitations**: The abstract does not explicitly acknowledge limitations; the approach's effectiveness depends on the underlying VLM's ability to generate meaningful prompts even with negative mining.

### Jeong et al. (2026)

**Research question**: How can multi-view segmentation achieve 3D consistency without requiring costly per-scene optimization or explicit 3D networks and annotated 3D data?

**Methodology**: Introduces MV-SAM that leverages pointmaps (3D points reconstructed from unposed images by visual geometry models) to lift image embeddings from SAM's pretrained encoder into 3D point embeddings, decoded by a transformer using cross-attention with 3D prompt embeddings and 3D positional embeddings for implicit cross-view consistency.

**Key findings**:
- Achieves 3D consistency using pointmaps without explicit 3D networks or annotated 3D data
- Outperforms SAM2-Video on multi-view segmentation benchmarks
- Achieves comparable performance with per-scene optimization baselines on NVOS, SPIn-NeRF, ScanNet++, uCo3D, and DL3DV benchmarks
- Trained on SA-1B dataset, the method generalizes well across different domains
- Eliminates the need for costly per-scene optimization to enforce 3D consistency

**Limitations**: Relies on pointmaps from recent visual geometry models which may have their own accuracy limitations; the approach requires pixel-point one-to-one correspondence from pointmaps, which may not be available or reliable in all scenarios.

### Karam et al. (2025)

**Research question**: Can promptable segmentation for cancer on medical images be achieved with minimal expert-curated annotations while maintaining performance comparable to fully-supervised methods?

**Methodology**: Proposes a novel approach using only 24 fully-segmented images supplemented by 8 weakly-labeled images for training, leveraging two classifiers (one weakly-supervised and one fully-supervised) to refine segmentation through a guided search process initiated by a single-point prompt.

**Key findings**:
- Outperforms existing promptable segmentation methods on prostate cancer segmentation
- Performs comparably with fully-supervised methods while using up to 100× less annotated data
- Requires only 24 fully-segmented images plus 8 weakly-labeled images for training
- Enables promptable segmentation with minimal labeled data that can be curated to very high standards
- Mitigates issues with cost and inter-observer variability in obtaining expert annotations

**Limitations**: Demonstrated only on prostate cancer segmentation task; the approach requires careful curation of minimal data to high standards, and generalization to other cancer types or medical imaging modalities remains unverified.

### Liang et al. (2026)

**Research question**: Do promptable segmentation models faithfully ground queried concepts or instead rely on visually salient but semantically misleading cues when generating masks?

**Methodology**: Introduces CAFE (Counterfactual Attribute Factuality Evaluation), a benchmark built on attribute-level counterfactual manipulation where target regions and ground-truth masks are preserved while attributes like surface appearance, context, or material composition are modified, containing 2,146 paired test samples across three counterfactual categories: Superficial Mimicry, Context Conflict, and Ontological Conflict.

**Key findings**:
- Reveals a systematic gap between localization quality and concept discrimination in promptable segmentation models
- Models often generate accurate masks even for misleading prompts, suggesting strong mask prediction does not imply faithful semantic grounding
- Models rely on visually salient but semantically misleading cues rather than faithfully grounding queried concepts
- The CAFE benchmark provides controlled evaluation across three counterfactual categories (SM, CC, OC) with 2,146 paired test samples
- Various model types and sizes all exhibit the concept-faithful grounding problem to varying degrees

**Limitations**: The benchmark focuses on three specific counterfactual categories which may not capture all forms of semantic misunderstanding; evaluation is limited to concept-faithful grounding and does not assess other aspects of segmentation model understanding or real-world application performance.

### Liu et al. (2025)

**Research question**: How can audio be integrated into SAM2 for promptable segmentation in video clips while preserving interactive efficiency and avoiding audio prompt dilution?

**Methodology**: Proposes AuralSAM2 with an AuralFuser module that fuses audio and visual features to generate sparse and dense prompts guided by audio and built upon SAM2's feature pyramid, plus an audio-guided contrastive loss that emphasizes auditory relevance in dominant visual features to align modalities.

**Key findings**:
- Integrates audio into SAM2 while largely preserving its promptable segmentation capability
- Addresses audio prompt dilution problem where audio signal weakens as it propagates through the network
- Achieves notable accuracy gains on public benchmarks
- Has only minimal impact on the interactive efficiency of promptable segmentation
- Avoids increased inference overhead compared to adapter-based audio-visual fusion methods

**Limitations**: Audio-visual integration still faces challenges with audio prompt dilution through network layers; the method's performance across diverse audio-visual scenarios and its robustness to varying audio quality conditions require further investigation.

### Moskalenko et al. (2026)

**Research question**: How robust are promptable segmentation models like SAM to natural variations in bounding box prompts that occur in real-world usage?

**Methodology**: The authors conducted a controlled user study collecting thousands of real bounding box annotations to analyze variability, then reformulated robustness evaluation as a white-box optimization problem over the bounding box prompt space to generate adversarial bounding boxes that minimize or maximize segmentation error while maintaining naturalness constraints.

**Key findings**:
- SAM-like models are highly sensitive to natural prompt noise, with substantial variability in segmentation quality across users for the same model and instance
- Current training and evaluation protocols using synthetic prompts generated through simple heuristics offer limited insight into real-world robustness
- BREPS successfully generates adversarial bounding boxes that reveal model vulnerabilities while adhering to naturalness constraints
- State-of-the-art models were benchmarked across 10 datasets spanning everyday scenes to medical imaging, revealing consistent robustness concerns

**Limitations**: Exhaustive testing of all possible user inputs is computationally prohibitive, necessitating the optimization-based approach; the method focuses on bounding boxes rather than other prompt types like points or text.

### Rukhman et al. (2026)

**Research question**: Can 3D object detection for autonomous vehicles be solved training-free and open-vocabulary without relying on fixed category lists from human-annotated training data?

**Methodology**: Uses SAM3 (a promptable segmentation model) queried with class names as text prompts to supply instance masks from six surround-view cameras, then converts masks to metric 3D boxes using scene geometry through a controlled three-stage comparison on nuScenes where 2D detection is held fixed and only the 3D geometry source changes.

**Key findings**:
- Geometry predicted from images alone reaches 0.183 mAP under the official nuScenes protocol
- Training-free box fitting from raw LiDAR points inside SAM3 masks achieves 0.298 mAP / 0.348 NDS at zero labeling cost
- Borrowing supervised box geometry at inference time lifts performance to 0.413 mAP / 0.555 NDS, revealing the pipeline's largest deficit is in measurement precision rather than 2D detection
- A three-state camera-witness rule built from SAM3 masks improves a supervised LiDAR-only detector from 0.596 to 0.630 mAP (roughly half the gain of fully supervised camera fusion) with no training
- SAM3 finds 84% of in-range objects with correctly named masks; failures occur on misnamed or geometrically unforgiving classes, not unseen objects

**Limitations**: The main performance deficit lies in measurement precision rather than 2D detection, and class confusion and confidence calibration issues persist even when substituting better geometry; the approach fails on classes that are misnamed or geometrically challenging rather than truly unseen.

### Zhang et al. (2025)

**Research question**: Can a universal promptable segmentation foundation model be developed for PET images that overcomes the limitations of insufficient annotation data and varying annotation levels in existing methods?

**Methodology**: SegAnyPET is trained on a large-scale PET dataset with 10,000+ scans covering multiple organs and tracers, employing a promptable segmentation architecture that supports multiple prompt types including points, boxes, and masks to achieve universal segmentation capabilities for PET imaging.

**Key findings**:
- SegAnyPET achieves state-of-the-art performance on multi-organ segmentation tasks in PET imaging
- The model exhibits strong zero-shot generalization to unseen organs and tracers
- Training on 10,000+ PET scans provides sufficient diversity to overcome annotation data limitations
- The promptable architecture successfully adapts segmentation foundation models to molecular PET images with functional rather than structural information
- Supports multiple prompt types (points, boxes, masks) for versatile clinical application

**Limitations**: PET images contain functional information rather than detailed physiological structural information, which may limit applicability compared to structural imaging modalities; the abstract does not address performance on rare organs or tracers not represented in the training dataset.

## References

Church, S., Warner, J. D., Maqbool, D., Tie, X., Hu, J., Lubner, M. G., & Bradshaw, T. J. (2026). Opportunistic promptable segmentation: Leveraging routine radiological annotations to guide 3D CT lesion segmentation. arXiv. https://arxiv.org/abs/2602.00309

Hu, J., Lin, J., Yan, J., & Gong, S. (2024). Leveraging hallucinations to reduce manual prompt dependency in promptable segmentation. arXiv. https://arxiv.org/abs/2408.15205

Hu, J., Cheng, Z., & Gong, S. (2025). INT: Instance-specific negative mining for task-generic promptable segmentation. arXiv. https://arxiv.org/abs/2501.18753

Jeong, Y., Sun, C., Wang, Y.-C. F., Cho, M., & Choe, J. (2026). MV-SAM: Multi-view promptable segmentation using pointmap guidance. arXiv. https://arxiv.org/abs/2601.17866

Karam, L., Wang, Y., Kasivisvanathan, V., Rusu, M., Hu, Y., & Saeed, S. U. (2025). Promptable cancer segmentation using minimal expert-curated data. arXiv. https://arxiv.org/abs/2505.17915

Liang, S., Wang, Z., Li, Y., Liu, X., & Wang, H. (2026). From pixels to concepts: Do segmentation models understand what they segment? arXiv. https://arxiv.org/abs/2605.09591

Liu, Y., Chen, Y., Wang, C., Han, J., Wu, J., Peng, C., Chen, J., Tian, Y., & Carneiro, G. (2025). AuralSAM2: Enabling SAM2 hear through pyramid audio-visual feature prompting. arXiv. https://arxiv.org/abs/2506.01015

Moskalenko, A., Kuznetsov, D., Dudko, I., Iasakova, A., Boldyrev, N., Shepelev, D., Spiridonov, A., Kuznetsov, A., & Shakhuro, V. (2026). BREPS: Bounding-box robustness evaluation of promptable segmentation. arXiv. https://arxiv.org/abs/2601.15123

Rukhman, D., Ezhov, V., Wong, T., Sommer, J. A., Ghanem, R., & Cremers, D. (2026). Training-free open-vocabulary 3D detection with promptable segmentation. arXiv. https://arxiv.org/abs/2609.19358

Zhang, Y., Xue, L., Zhang, W., Li, L., Liu, Y., Jiang, C., Cheng, Y., & Qi, Y. (2025). SegAnyPET: Universal promptable segmentation from Positron Emission Tomography images. arXiv. https://arxiv.org/abs/2502.14351
