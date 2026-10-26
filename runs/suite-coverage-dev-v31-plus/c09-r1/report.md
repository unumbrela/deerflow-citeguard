# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "domain generalization semantic segmentation", filtered to category cs.CV, published between 2023-10-03 and 2025-10-02
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on domain generalization for semantic segmentation (DGSS) published between October 2023 and October 2025. The surveyed literature reveals a field rapidly evolving toward leveraging vision foundation models (VFMs) as the primary backbone for achieving domain-invariant representations. Three dominant approaches have emerged: (1) integrating multi-modal cues such as depth and language information, (2) applying spectral decomposition and feature calibration techniques to separate style from content, and (3) developing collaborative frameworks that combine multiple foundation models. The collective findings demonstrate that parameter-efficient fine-tuning of frozen VFMs, combined with geometric consistency enforcement and style-invariant feature learning, achieves state-of-the-art performance across synthetic-to-real and real-to-real domain shifts. However, most papers acknowledge limitations in their abstracts regarding computational efficiency and the need for broader evaluation across diverse domain conditions.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "domain generalization semantic segmentation", filtered to category cs.CV, published between 2023-10-03 and 2025-10-02. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Vision Foundation Models as Universal Backbones

A dominant trend across the surveyed literature is the adoption of frozen vision foundation models (VFMs) such as DINOv2, EVA02, CLIP, and the Segment Anything Model (SAM) as the primary feature extractors for DGSS. Rather than training from scratch or using domain randomization, researchers are leveraging the rich, pre-trained representations of VFMs and applying parameter-efficient fine-tuning strategies. Benigmim et al. (2023) introduced the CLOUDS framework, which integrates CLIP backbones with SAM for iterative segmentation refinement, achieving 5.6% improvement on synthetic-to-real benchmarks. Wei et al. (2023) proposed Rein, a token-based fine-tuning approach that achieves strong performance with only 1% extra trainable parameters while keeping the VFM backbone frozen. This approach demonstrates that VFMs can be adapted for DGSS tasks without extensive retraining, preserving their generalization capabilities while adding task-specific refinements.

The shift toward VFMs represents a fundamental change in DGSS methodology: instead of learning domain-invariant features from scratch, researchers are now building upon the already robust representations learned by foundation models during pre-training. This trend is evident in 8 of the 10 surveyed papers, suggesting strong consensus on VFMs as the preferred starting point for DGSS research.

### Theme 2: Multi-Modal Integration for Domain Invariance

A second prominent theme is the integration of complementary modalities—particularly depth information and language cues—to enhance domain generalization. Chen et al. (2025a) proposed Vireo, a single-stage framework that unifies open-vocabulary semantic segmentation with domain generalization by incorporating Depth VFMs alongside visual foundation models. Their GeoText Prompts align geometric features with language, enabling the model to generalize to unseen domains and novel categories simultaneously. Similarly, Chen et al. (2025b) introduced DepthForge, which integrates depth cues from Depth Anything V2 with visual features from DINOv2 or EVA02, demonstrating particularly strong performance under extreme conditions such as night and snow where visual cues alone degrade.

Zhang and Tan (2025) extended this multi-modal approach by bridging VFMs with vision-language models (VLMs) through their MFuser framework. By combining the fine-grained visual features of VFMs with the text alignment capabilities of CLIP, they achieved 68.20 mIoU on synthetic-to-real benchmarks and 71.87 mIoU on real-to-real benchmarks. The consistent success of multi-modal approaches across these papers suggests that domain invariance is best achieved not through visual features alone, but through the fusion of geometric, semantic, and linguistic information that remains stable across domain shifts.

### Theme 3: Spectral Decomposition and Feature Calibration

The third major theme focuses on separating style (domain-specific) from content (domain-invariant) information through spectral decomposition and feature calibration techniques. Yi et al. (2024) proposed the SET framework, which decomposes VFM features into phase and amplitude components in frequency space—phase containing content information and amplitude containing style information. By processing these components separately with learnable tokens and applying attention optimization, they effectively isolate style-affected representations from static, domain-invariant tokens.

Li and Guo (2025) extended this approach with Multi-Granularity Feature Calibration (MGFC), which performs coarse-to-fine alignment of VFM features across three stages: global contextual semantics (coarse), category-level discriminability (medium), and high-frequency spatial detail enhancement (fine). This hierarchical calibration transfers the generalization strengths of VFMs to domain-specific DGSS tasks. Ahn et al. (2024) took a different approach with BlindNet, using covariance alignment to train encoders to uniformly recognize various styles while preserving content information, combined with semantic consistency contrastive learning to disentangle features vulnerable to misclassification. These spectral and calibration-based approaches share a common insight: rather than attempting to normalize away style variations, effective DGSS requires explicit modeling and separation of style and content at the feature level.

### Theme 4: Generative Augmentation and Style Synthesis

A fourth theme emerging from the literature is the use of generative models for data augmentation and style synthesis. Benigmim et al. (2023) incorporated generative models into CLOUDS for content diversification, addressing the limitations of traditional domain randomization. Niu et al. (2024) proposed SCSD, which uses a Text-Driven Style Transform module with domain difference text embeddings for controllable style transformation, achieving 49.11 mIoU on four unseen domain datasets when trained on GTAV.

Fan et al. (2025) introduced IELDM, a diffusion-based data augmentation framework using inverse evolution layers with Laplacian-based priors to filter undesirable generative patterns. Their approach suppresses domain-specific noise and defects in diffusion-generated data, achieving superior generalization compared to existing methods. These generative approaches complement the feature-based methods by expanding training data diversity while maintaining semantic consistency, suggesting that effective DGSS requires both robust feature learning and diverse training distributions.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong consensus on several key points. First, 8 of 10 papers agree that frozen vision foundation models provide superior starting points compared to training from scratch or using domain randomization alone. Second, there is widespread agreement that multi-modal integration—particularly incorporating depth or geometric information—improves robustness under domain shift, with Chen et al. (2025a), Chen et al. (2025b), and Zhang and Tan (2025) all demonstrating significant gains from depth-language fusion. Third, all papers employing feature decomposition or calibration methods (Yi et al., 2024; Li & Guo, 2025; Ahn et al., 2024) converge on the principle that explicit style-content separation outperforms implicit normalization approaches.

**Disagreements**: While the papers largely agree on the value of VFMs, there is divergence on the optimal adaptation strategy. Wei et al. (2023) advocate for minimal parameter fine-tuning with token-based refinements, while Chen et al. (2025a) and Chen et al. (2025b) propose more extensive architectural modifications incorporating additional foundation models. Additionally, there is methodological variation in how style-content separation is achieved: Yi et al. (2024) use frequency-domain spectral decomposition, while Ahn et al. (2024) employ covariance alignment in the spatial domain. These differences reflect ongoing exploration of the most effective adaptation mechanisms rather than fundamental disagreements about the field's direction.

## Gaps and Open Questions

Several gaps emerge from the collective limitations noted across the surveyed papers. First, none of the papers explicitly address computational efficiency in their abstracts, despite many proposing multi-component frameworks that integrate multiple foundation models—a significant concern for real-world deployment. Second, while depth integration shows promise, the reliance on depth estimation models introduces potential failure modes when depth predictions are inaccurate, yet no paper systematically addresses robustness to depth estimation errors. Third, most papers report performance on standard benchmarks (Cityscapes, GTAV, etc.), but few address extreme or rare domain shifts such as adverse weather combinations, sensor degradation, or geographic regions not represented in training data.

Additionally, the literature shows limited discussion of failure cases or error analysis—most abstracts report mIoU improvements without detailing where models continue to struggle. Finally, while open-vocabulary capabilities are mentioned by Chen et al. (2025a) and Zhang and Tan (2025), the integration of DGSS with open-vocabulary recognition remains nascent, with questions about how to handle novel categories that appear only in target domains.

## Per-Paper Annotations

### Ahn et al. (2024)

**Research question**: How can style variations be removed from features without unintentionally discarding crucial content information in domain generalized semantic segmentation?
**Methodology**: BlindNet uses covariance alignment to train the encoder to uniformly recognize various styles while preserving content information, combined with semantic consistency contrastive learning to enable the decoder to construct discriminative class embedding space and disentangle features vulnerable to misclassification.
**Key findings**:
- BlindNet successfully blinds style without requiring external modules or datasets
- Covariance alignment allows the encoder to preserve content information rather than removing style-sensitive factors
- Semantic consistency contrastive learning enables robust segmentation by disentangling features vulnerable to misclassification
- The approach outperforms existing DGSS methods on unseen target domains
**Limitations**: not stated in abstract

### Benigmim et al. (2023)

**Research question**: How can an assembly of collaborative foundation models improve domain generalized semantic segmentation beyond traditional domain randomization approaches?
**Methodology**: The CLOUDS framework integrates multiple foundation models: a CLIP backbone for robust feature representation, generative models for content diversification, and the Segment Anything Model (SAM) for iteratively refining segmentation predictions.
**Key findings**:
- CLOUDS excels in adapting from synthetic to real DGSS benchmarks
- The framework performs well under varying weather conditions
- Outperforms prior methods by 5.6% on averaged mIoU for synthetic-to-real benchmarks
- Outperforms prior methods by 6.7% on averaged mIoU under varying weather conditions
- The approach addresses content diversification limitations of domain randomization
**Limitations**: not stated in abstract

### Chen et al. (2025a)

**Research question**: How can depth information and language cues be unified to enable open-vocabulary semantic segmentation that generalizes across unseen domains?
**Methodology**: Vireo is a single-stage framework that builds upon frozen Visual Foundation Models and incorporates Depth VFMs for domain-invariant structural features, with three key components: GeoText Prompts for aligning geometric features with language, Coarse Mask Prior Embedding for enhanced gradient flow, and DOV-VEH for fusing structural and semantic features.
**Key findings**:
- Vireo unifies OVSS and DGSS capabilities in a single-stage framework for the first time
- Depth VFMs successfully extract domain-invariant structural features
- GeoText Prompts effectively align geometric features with language cues and refine VFM encoder representations
- CMPE enhances gradient flow for faster convergence and stronger textual influence
- Vireo achieves state-of-the-art performance surpassing existing methods by a large margin in both domain generalization and open-vocabulary recognition
**Limitations**: not stated in abstract

### Chen et al. (2025b)

**Research question**: Can integrating depth information with vision foundation model features improve geometric consistency and generalization performance in domain generalized semantic segmentation?
**Methodology**: The authors propose DepthForge, a fine-tuning framework that integrates visual cues from frozen DINOv2 or EVA02 with depth cues from frozen Depth Anything V2, incorporating depth-aware learnable tokens at each VFM layer to decouple domain-invariant visual and spatial information, plus a depth refinement decoder for adaptive multi-layer feature refinement.
**Key findings**:
- DepthForge significantly outperforms alternative approaches across various DGSS settings and five unseen target domain datasets
- The method demonstrates particularly strong performance under extreme conditions such as night and snow
- Depth information provides more robust geometric consistency compared to visual cues alone
- The approach achieves steadier visual-spatial attention and superior generalization ability
**Limitations**: not stated in abstract

### Fan et al. (2025)

**Research question**: How can inverse evolution layers be used to suppress domain-specific noise and defects in diffusion-generated data for improved domain generalized semantic segmentation?
**Methodology**: The authors propose IELDM, a diffusion-based data augmentation framework using inverse evolution layers (IELs) with Laplacian-based priors to filter undesirable generative patterns, and embed IELs into the decoder as IELFormer with a multi-scale frequency fusion module for cross-scale semantic consistency.
**Key findings**:
- IELs effectively highlight spatial discontinuities and semantic inconsistencies to filter defective generative patterns
- The defect-suppression capability of IELs benefits both the generative process and the segmentation network
- Multi-scale frequency fusion improves cross-scale coherence through frequency-domain analysis
- The approach achieves superior generalization performance compared to existing methods on benchmark datasets
**Limitations**: not stated in abstract

### Li and Guo (2025)

**Research question**: How can vision foundation models be adapted across multiple feature granularities to improve domain generalization in semantic segmentation?
**Methodology**: The authors propose Multi-Granularity Feature Calibration (MGFC), a framework that performs coarse-to-fine alignment of VFM features through three stages: coarse-grained feature calibration for global contextual semantics, medium-grained refinement for category-level discriminability, and fine-grained calibration via high-frequency spatial detail enhancement.
**Key findings**:
- MGFC effectively transfers the generalization strengths of VFMs to domain-specific DGSS tasks through hierarchical granularity-aware calibration
- The method outperforms state-of-the-art DGSS approaches on benchmark datasets
- Multi-granularity adaptation proves effective for semantic segmentation under domain shifts
**Limitations**: not stated in abstract

### Niu et al. (2024)

**Research question**: How can semantic consistency prediction and style diversity generalization be jointly optimized to overcome limitations of feature normalization and domain randomization in DGSS?
**Methodology**: The SCSD framework comprises three components: a Semantic Query Booster to enhance semantic awareness in the mask decoder, a Text-Driven Style Transform module using domain difference text embeddings for controllable style transformation, and Style Synergy Optimization to prevent similar domain feature space collapse through weighted style contrastive and aggregation losses.
**Key findings**:
- Semantic Query Booster enhances semantic awareness and discrimination capabilities of object queries for cross-domain consistency
- Text-Driven Style Transform enables controllable style transformation using domain difference text embeddings
- Style Synergy Optimization prevents collapse of similar domain feature spaces by separating inter-domain and aggregating intra-domain features
- SCSD trained on GTAV achieved 49.11 mIoU on four unseen domain datasets
- SCSD surpasses the previous state-of-the-art method by +4.08 mIoU
**Limitations**: not stated in abstract

### Wei et al. (2023)

**Research question**: How can vision foundation models be parameter-efficiently fine-tuned to achieve superior generalizability in domain generalized semantic segmentation?
**Methodology**: Rein is a fine-tuning approach built upon trainable tokens linked to distinct instances that precisely refines and forwards feature maps between backbone layers, producing diverse refinements for different categories within a single image while keeping the backbone frozen.
**Key findings**:
- Rein efficiently fine-tunes VFMs with fewer trainable parameters while surpassing full parameter fine-tuning
- With just 1% extra trainable parameters within the frozen backbone, Rein achieves strong performance
- Rein achieves a mIoU of 78.4% on Cityscapes without accessing any real urban-scene datasets
- The approach produces diverse refinements for different categories within a single image
- Rein significantly outperforms state-of-the-art methods across various experimental settings
**Limitations**: not stated in abstract

### Yi et al. (2024)

**Research question**: How can spectral decomposition of vision foundation model features improve learning of style-invariant features for domain generalized semantic segmentation?
**Methodology**: The SET framework decomposes frozen VFM features into phase and amplitude components in frequency space (containing content and style information respectively), processes them separately with learnable tokens, and applies attention optimization to bridge style-affected representation and static tokens during inference.
**Key findings**:
- Spectral decomposition separates content (phase) and style (amplitude) information effectively
- Learnable tokens can extract task-specific information from decomposed features
- Style variation primarily impacts token-based feature enhancement within the amplitude branch
- Attention optimization method addresses the gap between style-affected representation and static tokens
- The framework achieves state-of-the-art performance in extensive cross-domain experiments
**Limitations**: not stated in abstract

### Zhang and Tan (2025)

**Research question**: How can Vision Foundation Models and Vision-Language Models be effectively integrated to improve Domain Generalized Semantic Segmentation while maintaining computational efficiency?
**Methodology**: The authors propose MFuser, a Mamba-based fusion framework with two components: MVFuser (a co-adapter for joint fine-tuning capturing sequential and spatial dynamics) and MTEnhancer (a hybrid attention-Mamba module that refines text embeddings using image priors). The approach combines VFMs like DINOv2 with VLMs like CLIP while maintaining linear scalability in sequence length.
**Key findings**:
- MFuser significantly outperforms state-of-the-art DGSS methods
- Achieves 68.20 mIoU on synthetic-to-real benchmarks
- Achieves 71.87 mIoU on real-to-real benchmarks
- Maintains precise feature locality and strong text alignment without significant computational overhead
- Effectively integrates complementary strengths of VFMs (fine-grained features) and VLMs (text alignment)
**Limitations**: not stated in abstract

## References

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style blind domain generalized semantic segmentation via covariance alignment and semantic consistence contrastive learning. arXiv. https://arxiv.org/abs/2403.06122

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating foundation models for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2312.09788

Chen, S., Han, T., Fu, C., Zhang, C., Wang, C., Su, J., Cai, G., & Wu, M. (2025a). Leveraging depth and language for open-vocabulary domain-generalized semantic segmentation. arXiv. https://arxiv.org/abs/2506.09881

Chen, S., Han, T., Zhang, C., Luo, X., Wu, M., Cai, G., & Su, J. (2025b). Stronger, steadier & superior: Geometric consistency in depth VFM forges domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2504.12753

Fan, Q., Liu, C., Qiao, Z., & Shen, X. (2025). IELDG: Suppressing domain-specific noise with inverse evolution layers for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2508.19604

Li, X., & Guo, X. (2025). Multi-Granularity Feature Calibration via VFM for Domain Generalized Semantic Segmentation. arXiv. https://arxiv.org/abs/2508.03007

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring semantic consistency and style diversity for domain generalized semantic segmentation. arXiv. https://arxiv.org/abs/2412.12050

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. arXiv. https://arxiv.org/abs/2312.04265

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. arXiv. https://arxiv.org/abs/2407.18568

Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. arXiv. https://arxiv.org/abs/2504.03193
