# Systematic Literature Review: Self-Supervised Visual Representation Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "self-supervised visual", filtered to category cs.CV, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on self-supervised visual representation learning from the past two years reveals a field rapidly expanding beyond traditional contrastive and masked image modeling approaches. Recent work focuses on three major directions: (1) integrating self-supervised learning with multimodal large language models to address visual reasoning limitations, (2) developing theoretical frameworks that unify disparate SSL methods under common principles, and (3) applying SSL to domain-specific challenges including cross-domain generalization and specialized tasks like writer identification. The surveyed papers collectively demonstrate that self-supervised methods are maturing from generic representation learners to specialized tools that can operate without labels in challenging real-world scenarios, though fundamental questions remain about the necessary and sufficient conditions for effective unsupervised visual learning.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "self-supervised visual", filtered to category cs.CV, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Integration with Multimodal Large Language Models

A prominent direction in recent work is the integration of self-supervised visual learning with multimodal large language models (MLLMs) and vision-language models (VLMs). As MLLMs have demonstrated impressive capabilities in connecting vision and language, their proficiency in fundamental visual reasoning tasks remains limited due to over-reliance on textual supervision (Caffagni et al., 2025). JARVIS addresses this by integrating the I-JEPA learning paradigm into MLLM training, leveraging frozen vision foundation models to learn structural and semantic regularities from images without exclusive language supervision. Similarly, self-supervised visual preference alignment eliminates the need for GPT-4 or human supervision in VLM preference learning by using properly designed image augmentations to generate hard negative responses (Zhu et al., 2024). The dino.txt framework extends this integration by aligning self-supervised visual encoders like DINOv2 with text, achieving CLIP-like capabilities at a fraction of the computational cost while maintaining performance on dense tasks (Jose et al., 2024). This theme reflects a broader recognition that language supervision alone is insufficient for robust visual understanding.

### Theme 2: Theoretical Unification and Foundational Principles

Several papers attempt to formalize the theoretical underpinnings of self-supervised visual learning. Giakoumoglou et al. (2026) argue that effective SSL requires three jointly necessary principles: semantic invariance across augmented views (observation), patch-level spatial prediction, and representational non-degeneracy (regularization). Their theoretical analysis proves that combining observation and prediction without regularization admits degenerate solutions, and that every major SSL method can be expressed as a special case of a unified energy decomposition. This theoretical work provides a framework for understanding why certain methods succeed and others fail. Complementing this, research on latent masked image modeling identifies the specific challenges of learning representations through masked reconstruction in latent space, including representation collapsing and high region correlation (Wei et al., 2024). These theoretical contributions move the field from ad-hoc method development toward principled design.

### Theme 3: Domain-Specific Applications and Cross-Domain Generalization

A significant body of recent work applies self-supervised visual learning to domain-specific challenges, particularly where labeled data is scarce or domain shift is problematic. For road damage detection, self-supervised visual prompting derives defect-aware prompts from unlabeled target data to guide a frozen ViT backbone, achieving robust zero-shot transfer across domains (Xiao et al., 2025). In writer identification, decorrelation-based self-supervised pretraining learns disentangled stroke features, outperforming both contemporary SSL frameworks and several supervised methods (Maitra et al., 2024). Self-supervised visual on-policy distillation constructs learning signals from asymmetric augmented views, improving fine-grained perception benchmarks without ground-truth annotations (Li et al., 2026). These applications demonstrate that SSL is transitioning from generic representation learning to specialized tools that can operate effectively in real-world scenarios with limited or no labels.

### Theme 4: Embodied and Interaction-Based Learning

Emerging work recognizes that self-supervised visual learning can benefit from incorporating action and interaction data. Aubret et al. (2024) explore whether object-related actions can boost SSL by extracting actions performed to transition between ego-centric views from video datasets and introducing a loss function that aligns actions with visual representations. Their method outperforms previous approaches on category recognition by achieving better viewpoint-wise alignment of objects from the same category. This embodied perspective acknowledges that human visual learning occurs through active interaction with the environment, suggesting that SSL methods incorporating action information may achieve more robust and human-like visual representations.

### Theme 5: Understanding Representation Geometry and Failure Modes

Recent work also probes the fundamental properties and limitations of visual encoders. SPOOK investigates the relationship between embedding similarity and human-visible semantics far from the natural-image manifold by applying sparse pixel edits to blank canvases (Gupta et al., 2026). Their findings reveal that sparse edits on visually non-semantic inputs can enter target semantic basins in both language-aligned and self-supervised encoders, identifying a shared off-manifold failure mode. This line of research is critical for understanding when and why visual encoders fail, providing diagnostic tools for evaluating representation quality beyond standard benchmarks.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. First, there is broad agreement that pure language supervision is insufficient for robust visual understanding, motivating the integration of self-supervised objectives into MLLM and VLM training (Caffagni et al., 2025; Zhu et al., 2024; Jose et al., 2024). Second, multiple papers emphasize the importance of augmentation design—whether for creating asymmetric views in distillation (Li et al., 2026), generating hard negatives in preference alignment (Zhu et al., 2024), or structuring latent representations through actions (Aubret et al., 2024). Third, there is consensus that self-supervised methods can match or exceed supervised performance in domain-specific tasks when properly adapted (Maitra et al., 2024; Xiao et al., 2025).

**Disagreements**: The literature reveals tension between theoretical unification and practical specialization. Giakoumoglou et al. (2026) propose that all SSL methods are special cases of a unified framework with three necessary principles, suggesting a path toward general theory. However, the success of highly specialized methods for specific domains—writer identification (Maitra et al., 2024), road damage detection (Xiao et al., 2025), and visual prompting (Li et al., 2026)—suggests that domain-specific inductive biases remain important. Additionally, while some work focuses on improving in-domain performance through better self-supervised objectives (Wei et al., 2024), others prioritize cross-domain generalization through prompting and adaptation (Xiao et al., 2025), reflecting different priorities in the field.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, many methods require careful tuning of augmentation strength or prompt design, yet there is limited theoretical guidance on how to select these hyperparameters without labeled validation data (Li et al., 2026; Zhu et al., 2024). Second, while several papers demonstrate success on specific benchmarks, few provide comprehensive evaluation across diverse tasks and domains, making it difficult to assess generalizability (Caffagni et al., 2025; Maitra et al., 2024). Third, the theoretical framework proposed by Giakoumoglou et al. (2026) focuses on specific architectural assumptions that may not capture all practical SSL variants, leaving open the question of whether their three principles are truly universal. Fourth, embodied SSL methods require action annotations or extractable action data from video clips, limiting their applicability to datasets without such information (Aubret et al., 2024). Finally, the off-manifold failure modes identified by Gupta et al. (2026) suggest that current encoders may have fundamental limitations not captured by standard evaluations, pointing to the need for more robust diagnostic tools.

## Per-Paper Annotations

### Aubret et al. (2024)

**Research question**: Can object-related actions and embodied interactions boost self-supervised visual learning similar to how humans purposefully turn or move around objects during learning?
**Methodology**: The authors extract actions performed to transition between ego-centric views of objects from four video datasets and introduce a new loss function that learns visual and action embeddings by aligning the performed action with representations of two images from the same clip, allowing actions to structure the latent visual representation.
**Key findings**:
- The method consistently outperforms previous methods on downstream category recognition
- Improvement is associated with better viewpoint-wise alignment of different objects from the same category
- Embodied interactions with objects can improve self-supervised learning of object categories
- Performed actions can effectively structure latent visual representations
**Limitations**: The method is evaluated on only four video datasets and may not generalize beyond ego-centric object interaction scenarios; requires action annotations or extractable action data from video clips.

### Caffagni et al. (2025)

**Research question**: How can Multimodal Large Language Models improve their visual reasoning capabilities when they overfit language priors and overlook visual details due to reliance on textual supervision?
**Methodology**: The authors introduce JARVIS, a JEPA-inspired framework that integrates I-JEPA learning into MLLM training by using frozen vision foundation models as context and target encoders while training the LLM's early layers as a predictor to learn structural and semantic regularities from images without exclusive language supervision.
**Key findings**:
- JARVIS consistently improves performance on vision-centric benchmarks across different LLM families
- The approach does not degrade multimodal reasoning abilities
- Addresses the overfitting to language priors that occurs from text-based supervision
- Successfully leverages structural and semantic regularities from images independent of language
**Limitations**: The approach relies on frozen vision foundation models which may limit adaptability; the abstract does not report results on language-only tasks or address potential computational overhead from the additional JEPA training paradigm.

### Giakoumoglou et al. (2026)

**Research question**: What are the necessary and sufficient principles required for learning visual representations without labels?
**Methodology**: The authors formalize three principles (observation, prediction, regularization) and provide theoretical proofs about their necessity, complemented by controlled experiments including patch-retrieval evaluation to assess spatial consequences.
**Key findings**:
- Three non-overlapping objectives are jointly necessary: semantic invariance across augmented views, patch-level spatial prediction, and representational non-degeneracy
- Combining observation and prediction without regularization admits the constant encoder as a global minimizer under negative-free alignment
- The observation and prediction objectives are gradient-complementary and structurally non-conflicting at the encoder output
- Momentum encoder converges to the same fixed point as the online encoder and provides no collapse guarantee at convergence
**Limitations**: The theoretical framework focuses on specific architectural assumptions (negative-free alignment, momentum encoders) that may not capture all practical SSL variants; claims are scale-dependent and may not hold at different training regimes.

### Gupta et al. (2026)

**Research question**: What is the relationship between embedding similarity and human-visible semantics in vision encoders when operating far from the natural-image manifold?
**Methodology**: The authors apply sparse pixel edits to blank canvases using a simple pixel-level hill-climbing procedure, then evaluate whether these optimized inputs can retrieve chosen targets in multimodal contrastive encoders (OpenCLIP) and self-supervised visual encoders (DINOv3) across ImageNet and Flickr30k.
**Key findings**:
- Sparse edits on visually non-semantic blank canvases can enter target semantic basins in both language-aligned and self-supervised representation spaces
- On OpenCLIP, inputs optimized toward class prompts achieve strong top-1 and top-5 targeted retrieval performance
- On DINOv3, inputs optimized toward class prototypes achieve high target alignment and near-top prototype ranks
- The findings identify a shared off-manifold failure mode across modern vision encoders
**Limitations**: Black-box probing approach provides limited insight into internal encoder mechanisms; the sparse pixel edit methodology may not capture all off-manifold behaviors; evaluation limited to specific encoder architectures.

### Jose et al. (2024)

**Research question**: How can self-supervised visual foundation models like DINOv2 be aligned with language to enable open-vocabulary tasks while maintaining performance on dense prediction tasks?
**Methodology**: The authors propose dino.txt, building on the LiT training strategy to align a text encoder with frozen DINOv2, with key improvements including concatenating the [CLS] token with patch average for training and curating data using both text and image modalities to improve performance on both global and dense tasks.
**Key findings**:
- Achieves state-of-the-art results in zero-shot classification
- Achieves state-of-the-art results in open-vocabulary semantic segmentation
- Trains a CLIP-like model with only a fraction of the computational cost compared to CLIP
- Successfully handles both global (image-level) and dense (pixel-level) tasks
**Limitations**: The method relies on frozen DINOv2 vision encoder which limits vision-side adaptability; performance depends on careful data curation using both modalities which may require significant effort.

### Li et al. (2026)

**Research question**: Where can informative asymmetry come from in visual on-policy distillation when no privileged information (larger teacher, ground-truth annotations, or rewards) is available?
**Methodology**: The authors invert the asymmetry source by subtracting information from the student rather than adding privileged info to the teacher, introducing S²VOPD which distills a teacher's distribution on original images into a student's distribution on strongly augmented views of the same image.
**Key findings**:
- Asymmetry matters: all four augmentation families improve performance, while symmetric self-distillation degrades it
- Strength matters: performance peaks at moderate augmentation strength
- The gap must remain task-consistent: augmentations that completely remove question-relevant evidence induce large but uninformative discrepancies
- Improves Qwen3.5-4B from 70.7% to 77.4% across six fine-grained perception benchmarks, surpassing GPT-5.4
**Limitations**: The approach is evaluated primarily on fine-grained perception benchmarks and may not generalize to all visual tasks; the method requires careful tuning of augmentation strength to avoid removing task-relevant information.

### Maitra et al. (2024)

**Research question**: Can decorrelation-based self-supervised learning be effectively applied to learn disentangled stroke features for writer identification?
**Methodology**: The authors propose SWIS, a modified decorrelation-based framework that standardizes features along each dimension, originally designed for signature verification, and adapt it for writer identification tasks.
**Key findings**:
- The proposed SWIS framework outperforms contemporary self-supervised learning frameworks on writer identification benchmarks
- The method outperforms several supervised methods for writer identification
- This represents the first application of self-supervised learning specifically for writer verification tasks
- Decorrelation-based self-supervised pretraining yields performance comparable to supervised and contrastive SSL baselines
**Limitations**: Evaluation is limited to writer identification tasks; the approach may not generalize to other document analysis or biometric recognition domains without modification.

### Wei et al. (2024)

**Research question**: Can masked reconstruction in latent space combine the locality benefits of Masked Image Modeling with high-level semantic targets for self-supervised visual representation learning?
**Methodology**: The authors conduct a thorough analysis of Latent MIM challenges through carefully designed experiments, identifying and sequentially addressing issues including representation collapsing, learning objectives, high region correlation in latent space, and decoding conditioning.
**Key findings**:
- Joint online/target optimization leads to representation collapsing in Latent MIM frameworks
- High region correlation in latent space and decoding conditioning present significant training challenges
- Sequentially addressing identified challenges enables Latent MIM to learn high-level representations
- Latent MIM can retain the locality benefits of traditional MIM while achieving high-level semantic learning
**Limitations**: The framework requires careful handling of multiple training challenges; the solution involves sequential mitigation of several issues which may complicate implementation; further validation across diverse downstream tasks may be needed.

### Xiao et al. (2025)

**Research question**: How can self-supervised learning improve cross-domain generalization for pavement defect detection without requiring costly re-annotation for new environments?
**Methodology**: The authors propose a self-supervised framework with a Self-supervised Prompt Enhancement Module (SPEM) that derives defect-aware prompts from unlabeled target data, and a Domain-Aware Prompt Alignment (DAPA) objective that aligns prompt-conditioned source and target representations.
**Key findings**:
- The framework consistently outperforms strong supervised, self-supervised, and adaptation baselines across four challenging benchmarks
- Achieves robust zero-shot transfer capability to unseen target domains
- Demonstrates improved resilience to domain variations in road damage detection
- Shows high data efficiency in few-shot adaptation scenarios
**Limitations**: Requires access to unlabeled target domain data for prompt enhancement; evaluation is specific to road damage detection and may need adaptation for other visual inspection domains.

### Zhu et al. (2024)

**Research question**: Can unsupervised preference alignment be achieved in Vision-Language Models without relying on GPT-4 or human supervision during the alignment process?
**Methodology**: The authors generate chosen and rejected responses from original and augmented image pairs, then conduct preference alignment using direct preference optimization, where properly designed image augmentations induce the VLM to generate false but hard negative responses that help the model learn more robust answers.
**Key findings**:
- Achieves 90% relative score to GPT-4 on complex reasoning in LLaVA-Bench with only 8k randomly sampled unsupervised data
- Improves LLaVA-7B/13B by 6.7%/5.6% on the complex multi-modal benchmark MM-Vet
- The pipeline requires no GPT-4 or human involvement during alignment
- Highly efficient implementation requiring only a few lines of code
**Limitations**: The approach depends on properly designed augmentations to generate meaningful hard negatives; evaluation is limited to specific benchmarks (LLaVA-Bench, MM-Vet) and may not generalize to all preference alignment scenarios.

## References

Aubret, A., Teulière, C., & Triesch, J. (2024). Self-supervised visual learning from interactions with objects. arXiv. https://arxiv.org/abs/2407.06704

Caffagni, D., Sarto, S., Cornia, M., Baraldi, L., Dovesi, P. L., Roohi, S., Granroth-Wilding, M., & Cucchiara, R. (2025). Seeing beyond words: Self-supervised visual learning for multimodal large language models. arXiv. https://arxiv.org/abs/2512.15885

Giakoumoglou, N., Giakoumoglou, P., & Stathaki, T. (2026). Three necessary principles for self-supervised visual representation learning. arXiv. https://arxiv.org/abs/2608.08309

Gupta, A., Pandya, A., Adami, C., & Dolson, E. (2026). SPOOK: Sparse pixel optimization for off-manifold knowledge in vision encoders. arXiv. https://arxiv.org/abs/2610.32835

Jose, C., Moutakanni, T., Kang, D., Baldassarre, F., Darcet, T., Xu, H., Li, D., Szafraniec, M., Ramamonjisoa, M., Oquab, M., Siméoni, O., Vo, H. V., Labatut, P., & Bojanowski, P. (2024). DINOv2 meets text: A unified framework for image- and pixel-level vision-language alignment. arXiv. https://arxiv.org/abs/2412.16334

Li, Y., Liang, Y., Tian, Y., Wang, B., Zhang, K., Yin, Z., Fu, D., Torr, P., & Vasconcelos, N. (2026). Self-supervised visual on-policy distillation. arXiv. https://arxiv.org/abs/2608.14144

Maitra, A., Mitra, S., Manna, S., Bhattacharya, S., & Pal, U. (2024). Decorrelation-based self-supervised visual representation learning for writer identification. arXiv. https://arxiv.org/abs/2410.01441

Wei, Y., Gupta, A., & Morgado, P. (2024). Towards latent masked image modeling for self-supervised visual representation learning. arXiv. https://arxiv.org/abs/2407.15837

Xiao, X., Wang, Z., Mo, M., Liu, C., Ma, C., Li, Y., Krishnaswamy, S., Wang, X., & Wang, T. (2025). Self-supervised visual prompting for cross-domain road damage detection. arXiv. https://arxiv.org/abs/2511.12410

Zhu, K., Ge, Z., Zhao, L., & Zhang, X. (2024). Self-supervised visual preference alignment. arXiv. https://arxiv.org/abs/2404.10501
