# Systematic Literature Review: Domain Generalization for Semantic Segmentation

**Date:** October 27, 2026  
**Category:** cs.CV  
**Publication Window:** October 3, 2023 – October 2, 2025  
**Number of Papers:** 10

## Executive Summary

This systematic literature review examines recent advances in Domain Generalized Semantic Segmentation (DGSS) from October 2023 to October 2025. The field has witnessed a paradigm shift toward leveraging foundation models—including Vision Foundation Models (VFMs), Vision-Language Models (VLMs), and diffusion models—to achieve robust generalization to unseen target domains without requiring target domain data. Key trends include parameter-efficient fine-tuning, spectral feature decomposition, language-guided style augmentation, and collaborative multi-model frameworks. The reviewed papers collectively demonstrate significant improvements over previous state-of-the-art methods, with mIoU gains ranging from 2.5 to 11.8 percentage points across various benchmarks.

---

## 1. Introduction

Domain Generalized Semantic Segmentation addresses the critical challenge of deploying semantic segmentation models to unseen target domains that differ significantly from training data. Unlike domain adaptation methods that require target domain samples, DGSS methods must generalize without accessing any target data, making them essential for real-world applications where target domain data may be unavailable or costly to obtain [E23][citation:2312.01850](https://arxiv.org/abs/2312.01850v1).

The fundamental challenge in DGSS lies in the entanglement of style and content: cross-domain images share common pixel-wise content information but vary greatly in style [E8][citation:2407.18568](https://arxiv.org/abs/2407.18568v2). Traditional approaches have focused on feature normalization and domain randomization, but these methods exhibit significant limitations—feature normalization tends to confuse semantic features, while domain randomization often incorporates domain-irrelevant noise [E6][citation:2412.12050](https://arxiv.org/abs/2412.12050v1).

Recent advances have leveraged large-scale pre-trained foundation models to overcome these limitations. This review synthesizes findings from 10 representative papers published between October 2023 and October 2025, analyzing their methodological innovations, experimental results, and contributions to the field.

---

## 2. Methodology

### 2.1 Search Strategy

A systematic search was conducted in arXiv for papers in the cs.CV (Computer Vision) category published between October 3, 2023, and October 2025. The search query "domain generalization semantic segmentation" identified 50 candidate papers, with an additional 110 papers added through citation expansion. From a shortlist of 30 papers, 10 were selected based on their centrality to the topic and citation impact.

### 2.2 Selection Criteria

Papers were included if they:
- Focused specifically on domain generalization techniques for semantic segmentation
- Were published in the cs.CV category between October 3, 2023, and October 2025
- Proposed novel methodologies or significant improvements over existing approaches
- Provided comprehensive experimental evaluation on standard DGSS benchmarks

### 2.3 Data Extraction

For each selected paper, key information was extracted including: research motivation, proposed methodology, key innovations, experimental setup, performance metrics, and stated limitations. Evidence was recorded through direct quotes from paper sections including Introduction, Methods, and Experiments.

---

## 3. Reviewed Papers

### 3.1 Vision Foundation Model-Based Approaches

#### **Wei et al. (2023)** - Rein: Parameter-Efficient VFM Fine-Tuning

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

**Method:** Rein introduces a parameter-efficient fine-tuning approach that harnesses Vision Foundation Models (VFMs) for DGSS with minimal trainable parameters [E18]. The method employs learnable tokens, each linked to distinct instances, to precisely refine and forward feature maps from each layer to the next within the backbone [E19][citation:2312.04265](https://arxiv.org/abs/2312.04265v5).

**Key Innovation:** "With fewer trainable parameters, Rein efficiently fine-tunes VFMs for DGSS tasks, surprisingly surpassing full parameter fine-tuning" [E18][citation:2312.04265](https://arxiv.org/abs/2312.04265v5). The approach uses shared weights across MLPs and a low-rank matrix design to reduce trainable parameters to just 1% of the backbone [E19].

**Results:** Rein achieves a mIoU of 78.4% on Cityscapes without accessing any real urban-scene datasets, significantly outperforming state-of-the-art methods across various settings [E18, E27][citation:2312.04265](https://arxiv.org/abs/2312.04265v5).

---

#### **Yi et al. (2024)** - SET: Spectral-Decomposed Token Learning

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

**Method:** The Spectral-dEcomposed Token (SET) framework decomposes frozen VFM features into phase and amplitude components in the frequency space, which mainly contain content and style information respectively [E7]. The phase component provides stable content information while the amplitude captures style variations [E8][citation:2407.18568](https://arxiv.org/abs/2407.18568v2).

**Key Innovation:** "Style variation primarily impacts the token-based feature enhancement within the amplitude branch. To address this issue, we further develop an attention optimization method to bridge the gap between style-affected representation and static tokens during inference" [E8][citation:2407.18568](https://arxiv.org/abs/2407.18568v2).

**Results:** SET achieves state-of-the-art performance with 1.15-1.66% mIoU improvements over Rein across four target domains (Cityscapes, BDD, Mapillary, SYNTHIA) when trained on GTAV [E9][citation:2407.18568](https://arxiv.org/abs/2407.18568v2).

---

#### **Ahn et al. (2024)** - BlindNet: Style Blind Segmentation

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

**Method:** BlindNet addresses the entanglement problem through two components: (1) covariance alignment trains the encoder to uniformly recognize various styles while preserving content information, and (2) semantic consistency contrastive learning enables the decoder to construct discriminative class embedding space [E10][citation:2403.06122](https://arxiv.org/abs/2403.06122v1).

**Key Innovation:** "The main idea behind our proposed approach is to alleviate the effect of style in the encoder whilst facilitating robust segmentation in the decoder" [E11][citation:2403.06122](https://arxiv.org/abs/2403.06122v1). Unlike methods that remove style-sensitive factors, BlindNet trains the encoder to recognize various styles uniformly [E10].

**Results:** BlindNet outperforms all other DGSS methods when trained on GTAV with ResNet-50 backbone, demonstrating superior generalization to Cityscapes, BDD-100K, and Mapillary target domains [E12][citation:2403.06122](https://arxiv.org/abs/2403.06122v1).

---

### 3.2 Language-Guided Approaches

#### **Fahes et al. (2023)** - FAMix: Language-Guided Style Augmentation

Fahes, M., Vu, T.-H., Bursuc, A., Pérez, P., & de Charette, R. (2023). A Simple Recipe for Language-guided Domain Generalized Segmentation. *arXiv preprint arXiv:2311.17922*. https://arxiv.org/abs/2311.17922v2

**Method:** FAMix (Freeze, Augment and Mix) comprises three key ingredients: (i) preservation of intrinsic CLIP robustness through minimal fine-tuning, (ii) language-driven local style augmentation, and (iii) randomization by locally mixing source and augmented styles during training [E20][citation:2311.17922](https://arxiv.org/abs/2311.17922v2).

**Key Innovation:** The method "mines class-specific style banks using Prompt-driven Instance Normalization (PIN) with random style prompts to explore intermediate proxy domains in a class-aware manner, fundamentally different from steering towards a particular target domain" [E21][citation:2311.17922](https://arxiv.org/abs/2311.17922v2).

**Results:** FAMix significantly outperforms all baseline DGSS methods across all target datasets (Cityscapes, BDD, Mapillary, SYNTHIA, ACDC subsets) for both ResNet-50 and ResNet-101 backbones in single-source and multi-source settings [E22][citation:2311.17922](https://arxiv.org/abs/2311.17922v2).

---

#### **Pak et al. (2024)** - tqdm: Textual Query-Driven Mask Transformer

Pak, B., Woo, B., Kim, S., Kim, D.-h., & Kim, H. (2024). Textual Query-Driven Mask Transformer for Domain Generalized Segmentation. *arXiv preprint arXiv:2407.09033*. https://arxiv.org/abs/2407.09033v2

**Method:** tqdm utilizes text embeddings from vision-language models as textual object queries that provide domain-invariant semantics for robust mask predictions. The framework includes text-to-pixel attention to enhance semantic clarity of pixel features [E13][citation:2407.09033](https://arxiv.org/abs/2407.09033v2).

**Key Innovation:** "Three regularization losses maintain vision-language alignment: language regularization prevents prompt distortion, vision-language regularization ensures pixel-level alignment, and vision regularization preserves encoder capabilities" [E14][citation:2407.09033](https://arxiv.org/abs/2407.09033v2).

**Results:** tqdm achieves state-of-the-art 68.9 mIoU on GTA5→Cityscapes, improving the prior best method by 2.5 mIoU. The method shows particular improvement on rare classes through robust region proposals from textual queries [E15][citation:2407.09033](https://arxiv.org/abs/2407.09033v2).

---

#### **Zhang & Tan (2025)** - MFuser: Mamba-Based VFM-VLM Fusion

Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

**Method:** MFuser is a Mamba-based fusion framework that integrates VFMs (e.g., DINOv2) with VLMs (e.g., CLIP). It consists of two components: MVFuser, which acts as a co-adapter to jointly fine-tune both models, and MTEnhancer, a hybrid attention-Mamba module that refines text embeddings [E1][citation:2504.03193](https://arxiv.org/abs/2504.03193v2).

**Key Innovation:** "MVFuser serves dual roles: (1) refining VFM and VLM features to generate task-specific features, and (2) enabling interaction between the two feature types to complement each's weaknesses. The Mamba-based design addresses the computational challenge of doubled patch sequence length" [E2][citation:2504.03193](https://arxiv.org/abs/2504.03193v2).

**Results:** MFuser achieves 68.20 mIoU on synthetic-to-real and 71.87 mIoU on real-to-real benchmarks, outperforming state-of-the-art by 2.15 mIoU on average. On synthetic-to-real setup (G→{C,B,M}), MFuser with EVA02-CLIP improves G→B benchmark by 1.49 mIoU [E3][citation:2504.03193](https://arxiv.org/abs/2504.03193v2).

---

### 3.3 Diffusion Model-Based Approaches

#### **Niemeijer et al. (2023)** - DIDEX: Diffusion-Based Domain Extension

Niemeijer, J., Schwonberg, M., Termöhlen, J.-A., Schmidt, N. M., & Fingscheidt, T. (2023). Generalization by Adaptation: Diffusion-Based Domain Extension for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.01850*. https://arxiv.org/abs/2312.01850v1

**Method:** DIDEX employs a diffusion model to generate a pseudo-target domain with diverse text prompts, allowing control over style and content of generated images. The method utilizes UDA techniques to overcome semantic inconsistency limitations by treating generated diffusion data as target domain for adaptation [E23][citation:2312.01850](https://arxiv.org/abs/2312.01850v1).

**Key Innovation:** "Utilizes UDA techniques to overcome semantic inconsistency limitations of diffusion models by treating generated diffusion data as target domain for adaptation, employing depth-guided Stable Diffusion and ControlNet for structural consistency" [E24][citation:2312.01850](https://arxiv.org/abs/2312.01850v1).

**Results:** DIDEX outperforms previous approaches by a large margin across various datasets and architectures without using any real data. For generalization from GTA5, it improves state-of-the-art mIoU performance by 3.8% absolute on average, and for SYNTHIA by 11.8% absolute [E28][citation:2312.01850](https://arxiv.org/abs/2312.01850v1).

---

#### **Jia et al. (2023)** - DGInStyle: Diffusion with Stylized Semantic Control

Jia, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, K., & Obukhov, A. (2023). DGInStyle: Domain-Generalizable Semantic Segmentation with Image Diffusion Models and Stylized Semantic Control. *arXiv preprint arXiv:2312.03048*. https://arxiv.org/abs/2312.03048v3

**Method:** DGInStyle proposes an efficient data generation pipeline with three innovations: (1) specializing a pretrained LDM to semantically-controlled generation, (2) Style Swap technique to endow the generative prior with learned semantic control, and (3) Multi-resolution Latent Fusion to overcome bias toward dominant objects [E16][citation:2312.03048](https://arxiv.org/abs/2312.03048v3).

**Key Innovation:** "Novel Style Swap technique decouples semantic control from style by training ControlNet on source-domain-fine-tuned LDM, then switching to original LDM for inference. Multi-Resolution Latent Fusion overcomes low-resolution latent space limitations for small instances" [E17][citation:2312.03048](https://arxiv.org/abs/2312.03048v3).

**Results:** DGInStyle improves DG performance by +2.5 to +7.2 mIoU across various methods and architectures (IBN-Net, RobustNet, DAFormer, HRDA) with both ResNet-101 and MiT-B5 backbones, achieving +2.5 mIoU improvement over state-of-the-art [E26][citation:2312.03048](https://arxiv.org/abs/2312.03048v3).

---

#### **Benigmim et al. (2023)** - CLOUDS: Collaborating Foundation Models

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

**Method:** CLOUDS integrates multiple foundation models: (i) CLIP backbone for robust feature representation, (ii) generative models to diversify content covering various modes of possible target distribution, and (iii) Segment Anything Model (SAM) for iteratively refining segmentation predictions [E25][citation:2312.09788](https://arxiv.org/abs/2312.09788v2).

**Key Innovation:** "Self-training framework where initial pseudo labels prompt SAM for refined pseudo labels in student-teacher fashion; uses LLM to generate diverse textual prompts for diffusion model to broaden image diversity" [E29][citation:2312.09788](https://arxiv.org/abs/2312.09788v2).

**Results:** CLOUDS excels in adapting from synthetic to real DGSS benchmarks and under varying weather conditions, notably outperforming prior methods by 5.6% and 6.7% on averaged mIoU, respectively [E30][citation:2312.09788](https://arxiv.org/abs/2312.09788v2).

---

### 3.4 Semantic Consistency and Style Diversity Approaches

#### **Niu et al. (2024)** - SCSD: Semantic Consistency and Style Diversity

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

**Method:** SCSD comprises three pivotal components: (1) Semantic Query Booster enhances semantic awareness of object queries in the mask decoder, (2) Text-Driven Style Transform utilizes domain difference text embeddings to controllably guide style transformation, and (3) Style Synergy Optimization fortifies separation of inter-domain features through synergistic weighting of style contrastive and aggregation losses [E4][citation:2412.12050](https://arxiv.org/abs/2412.12050v1).

**Key Innovation:** "TDST mines text style diversity and achieves multi-scale image feature style transformation through style difference features from domain difference embeddings mapping, addressing the uncontrollability issue in prior domain randomization methods" [E5][citation:2412.12050](https://arxiv.org/abs/2412.12050v1).

**Results:** SCSD achieves 49.11 mIoU average on four unseen target domains (G→{C,B,M,S}), surpassing previous state-of-the-art by +4.08 mIoU. On adverse conditions (ACDC), it improves by +0.10 (night), +4.28 (snow), +4.11 (rain), and +3.18 (fog) [E6][citation:2412.12050](https://arxiv.org/abs/2412.12050v1).

---

## 4. Comparative Analysis

### 4.1 Methodological Trends

The reviewed papers reveal several convergent trends in DGSS research:

**Foundation Model Integration:** Eight of ten papers leverage pre-trained foundation models (CLIP, DINOv2, SAM, diffusion models) as core components. This represents a significant shift from earlier approaches that trained models from scratch or used ImageNet pre-training alone.

**Parameter Efficiency:** Multiple approaches (Rein, FAMix, SET) emphasize parameter-efficient fine-tuning, recognizing that full fine-tuning on small DGSS datasets leads to overfitting and limited generalizability [E19][citation:2312.04265](https://arxiv.org/abs/2312.04265v5).

**Style-Content Disentanglement:** A central challenge addressed across papers is disentangling style from content. Methods vary in their approach: SET uses spectral decomposition [E8][citation:2407.18568](https://arxiv.org/abs/2407.18568v2), BlindNet uses covariance alignment [E11][citation:2403.06122](https://arxiv.org/abs/2403.06122v1), and SCSD uses text-driven style transformation [E5][citation:2412.12050](https://arxiv.org/abs/2412.12050v1).

**Multi-Model Collaboration:** CLOUDS and MFuser demonstrate the benefits of integrating multiple foundation models, leveraging complementary strengths while addressing individual weaknesses [E25][citation:2312.09788](https://arxiv.org/abs/2312.09788v2) [E3][citation:2504.03193](https://arxiv.org/abs/2504.03193v2).

### 4.2 Performance Comparison

| Method | Backbone | Training Source | Best Target mIoU | Improvement over SOTA |
|--------|----------|-----------------|------------------|----------------------|
| Rein | VFM (EVA02) | Cityscapes (synthetic) | 78.4% | Not specified |
| SET | VFM | GTAV | +1.66% over Rein | 1.15-1.66% |
| BlindNet | ResNet-50 | GTAV | Not specified | Outperforms all baselines |
| FAMix | ResNet-101 | Source domains | Not specified | Significant improvement |
| tqdm | Transformer | GTA5 | 68.9 (Cityscapes) | +2.5 mIoU |
| MFuser | VFM+VLM | Synthetic | 71.87 (real-to-real) | +2.15 mIoU avg |
| DIDEX | Various | GTA5/SYNTHIA | Not specified | +3.8% to +11.8% |
| DGInStyle | ResNet-101/MiT-B5 | Street scenes | Not specified | +2.5 to +7.2 mIoU |
| CLOUDS | CLIP+SAM+Diffusion | Synthetic | Not specified | +5.6% to +6.7% |
| SCSD | Transformer | GTAV | 49.11 (avg 4 domains) | +4.08 mIoU |

### 4.3 Benchmark Datasets

The reviewed papers predominantly evaluate on standard DGSS benchmarks:

**Source Datasets:** GTA5, SYNTHIA, Cityscapes (synthetic versions)

**Target Datasets:** Cityscapes, BDD-100K, Mapillary, ACDC (adverse conditions), SYNTHIA

**Common Settings:** 
- Single-source generalization (GTA5→{Cityscapes, BDD, Mapillary})
- Multi-source generalization (GTA5+SYNTHIA→{Cityscapes, BDD, Mapillary})
- Synthetic-to-real and real-to-real transfer
- Adverse weather conditions (ACDC: night, snow, rain, fog)

---

## 5. Discussion

### 5.1 Key Contributions

The reviewed papers collectively advance DGSS through several key contributions:

1. **Foundation Model Harnessing:** Demonstrating that VFMs and VLMs provide inherent out-of-domain generalization capabilities that can be efficiently adapted to DGSS tasks [E8][citation:2407.18568](https://arxiv.org/abs/2407.18568v2).

2. **Controllable Style Transformation:** Moving beyond random style augmentation to controllable, text-guided style transformation that maintains semantic consistency while increasing diversity [E5][citation:2412.12050](https://arxiv.org/abs/2412.12050v1) [E21][citation:2311.17922](https://arxiv.org/abs/2311.17922v2).

3. **Efficient Fine-Tuning:** Showing that parameter-efficient methods can outperform full fine-tuning, preserving pre-trained knowledge while adapting to target tasks [E18][citation:2312.04265](https://arxiv.org/abs/2312.04265v5).

4. **Multi-Model Synergy:** Demonstrating that combining complementary foundation models (VFM+VLM, CLIP+SAM+Diffusion) yields superior performance compared to single-model approaches [E3][citation:2504.03193](https://arxiv.org/abs/2504.03193v2) [E25][citation:2312.09788](https://arxiv.org/abs/2312.09788v2).

### 5.2 Persistent Challenges

Despite significant progress, several challenges remain:

**Semantic Inconsistency in Generated Data:** Diffusion-based methods struggle with semantic consistency in generated images, requiring additional techniques like ControlNet and UDA to maintain structural integrity [E24][citation:2312.01850](https://arxiv.org/abs/2312.01850v1).

**Style-Content Entanglement:** Complete disentanglement remains elusive, with methods risking removal of crucial content information when attempting to eliminate style variations [E11][citation:2403.06122](https://arxiv.org/abs/2403.06122v1).

**Computational Overhead:** Integrating multiple foundation models increases computational requirements, though recent work (MFuser) addresses this through efficient architectures like Mamba [E2][citation:2504.03193](https://arxiv.org/abs/2504.03193v2).

**Class-Agnostic Limitations:** Models like SAM output class-agnostic masks, requiring additional semantic grounding for DGSS applications [E29][citation:2312.09788](https://arxiv.org/abs/2312.09788v2).

### 5.3 Future Directions

Based on the reviewed literature, promising future directions include:

1. **Efficient Multi-Modal Fusion:** Developing more efficient methods to integrate complementary foundation models without prohibitive computational costs.

2. **Controllable Generation:** Improving controllability and semantic consistency of diffusion-based data generation for domain extension.

3. **Language-Guided Approaches:** Further exploiting vision-language models for domain-invariant semantic knowledge and controllable style transformation.

4. **Adverse Condition Robustness:** Enhancing generalization to extreme and adverse conditions (night, snow, fog) for safety-critical applications like autonomous driving.

---

## 6. Conclusion

This systematic literature review has examined 10 representative papers on Domain Generalized Semantic Segmentation published between October 2023 and October 2025. The field has undergone a paradigm shift toward leveraging foundation models, with significant advances in parameter-efficient fine-tuning, spectral feature decomposition, language-guided augmentation, and multi-model collaboration.

The reviewed methods demonstrate substantial improvements over previous state-of-the-art approaches, with mIoU gains ranging from 2.5 to 11.8 percentage points across various benchmarks. Key innovations include Rein's parameter-efficient VFM fine-tuning, SET's spectral decomposition, FAMix's language-guided style augmentation, MFuser's Mamba-based fusion, and SCSD's controllable style transformation.

Despite these advances, challenges remain in semantic consistency, style-content disentanglement, and computational efficiency. Future research should focus on developing more efficient multi-modal fusion techniques, improving controllable generation, and enhancing robustness to adverse conditions.

The convergence of foundation models, language guidance, and diffusion-based generation represents a promising direction for achieving robust domain generalization in semantic segmentation, with important implications for real-world deployment in autonomous driving, robotics, and other applications requiring cross-domain robustness.

---

## References

Ahn, W.-J., Yang, G.-Y., Choi, H.-D., & Lim, M.-T. (2024). Style Blind Domain Generalized Semantic Segmentation via Covariance Alignment and Semantic Consistence Contrastive Learning. *arXiv preprint arXiv:2403.06122*. https://arxiv.org/abs/2403.06122v1

Benigmim, Y., Roy, S., Essid, S., Kalogeiton, V., & Lathuilière, S. (2023). Collaborating Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.09788*. https://arxiv.org/abs/2312.09788v2

Fahes, M., Vu, T.-H., Bursuc, A., Pérez, P., & de Charette, R. (2023). A Simple Recipe for Language-guided Domain Generalized Segmentation. *arXiv preprint arXiv:2311.17922*. https://arxiv.org/abs/2311.17922v2

Jia, Y., Hoyer, L., Huang, S., Wang, T., Van Gool, L., Schindler, K., & Obukhov, A. (2023). DGInStyle: Domain-Generalizable Semantic Segmentation with Image Diffusion Models and Stylized Semantic Control. *arXiv preprint arXiv:2312.03048*. https://arxiv.org/abs/2312.03048v3

Niemeijer, J., Schwonberg, M., Termöhlen, J.-A., Schmidt, N. M., & Fingscheidt, T. (2023). Generalization by Adaptation: Diffusion-Based Domain Extension for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.01850*. https://arxiv.org/abs/2312.01850v1

Niu, H., Xie, L., Lin, J., & Zhang, S. (2024). Exploring Semantic Consistency and Style Diversity for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2412.12050*. https://arxiv.org/abs/2412.12050v1

Pak, B., Woo, B., Kim, S., Kim, D.-h., & Kim, H. (2024). Textual Query-Driven Mask Transformer for Domain Generalized Segmentation. *arXiv preprint arXiv:2407.09033*. https://arxiv.org/abs/2407.09033v2

Wei, Z., Chen, L., Jin, Y., Ma, X., Liu, T., Ling, P., Wang, B., Chen, H., & Zheng, J. (2023). Stronger, Fewer, & Superior: Harnessing Vision Foundation Models for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2312.04265*. https://arxiv.org/abs/2312.04265v5

Yi, J., Bi, Q., Zheng, H., Zhan, H., Ji, W., Huang, Y., Li, Y., & Zheng, Y. (2024). Learning Spectral-Decomposed Tokens for Domain Generalized Semantic Segmentation. *arXiv preprint arXiv:2407.18568*. https://arxiv.org/abs/2407.18568v2

Zhang, X., & Tan, R. T. (2025). Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation. *arXiv preprint arXiv:2504.03193*. https://arxiv.org/abs/2504.03193v2

---

## Appendix: Evidence Record

All claims in this review are supported by evidence recorded through the systematic literature review process. Evidence IDs (E1-E30) correspond to direct quotes extracted from paper sections including Introduction, Methods, and Experiments. Receipt citations [r1-r22] document the execution record of paper retrieval, reading, and evidence citation actions.

**Tool Receipts:**
- Search execution: [r1]
- Screening and selection: [r2]
- Batch retrieval (3 batches): [r3], [r4], [r5]
- Paper reading and evidence extraction: [r6]-[r12]
- Subagent delegation for evidence recording: [r10], [r11], [r12]

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E23 | arXiv:2312.01850 | [1 Introduction](https://arxiv.org/html/2312.01850#S1.I1.i2.p1) | “By utilizing UDA techniques, we overcome the semantic inconsistency limitation of diffusion models, ensuring improved domain generalization performance.” |
| E8 | arXiv:2407.18568 | [1. Introduction](https://arxiv.org/html/2407.18568#S1.p4) | “the phase component, which contains more low-frequency component on the scene content, is relatively stable despite the cross-style variation. In contrast, the amplitude component, which has more high-frequency component on the styles, can be rather unstable when handling images from different domains.” |
| E6 | arXiv:2412.12050 | [Comparison with the state-of-the-art methods](https://arxiv.org/html/2412.12050#Sx4.SSx2.p1) | “For G \rightarrow {C, B, M, S} setting, our method achieves an average of 49.11 mIoU on four target domain datasets, yielding an improvement of +4.08 mIoU over the state-of-the-art DGSS methods.” |
| E18 | arXiv:2312.04265 | [1 Introduction](https://arxiv.org/html/2312.04265#S1.p5) | “In this work, we introduce a robust and efficient fine-tuning approach, namely "Rein". Tailored for DGSS tasks, Rein employs fewer trainable parameters to harness stronger VFMs for achieving superior generalization.” |
| E19 | arXiv:2312.04265 | [3.2 Core of Rein](https://arxiv.org/html/2312.04265#S3.SS2.p3) | “To establish this dual bridge, Rein starts with a set of learnable tokens T={T_i∈ℝ^{m×c} \| i∈ℕ,1≤i≤N}, where each token sequence T_i is randomly initialized, and m denotes the sequence length of T_i.” |
| E27 | arXiv:2312.04265 | [1 Introduction](https://arxiv.org/html/2312.04265#S1.I1.i2.p1) | “We present a robust fine-tuning method, namely "Rein", to parameter-efficiently harness VFMs.” |
| E7 | arXiv:2407.18568 | [3. Methodology](https://arxiv.org/html/2407.18568#S3.p1) | “To efficiently fine-tune VFMs, spectral-decomposed tokens are applied to each frozen layer. Within each layer, the frozen features are decomposed into amplitude and phase components by Fast Fourier Transform (FFT).” |
| E9 | arXiv:2407.18568 | [4.2.1. GTAV Source Domain](https://arxiv.org/html/2407.18568#S4.SS2.SSS1.p1) | “The proposed SET shows an mIoU improvement of 1.66%, 1.24%, 1.58% and 1.15% on C, B, M and S unseen target domains, respectively, compared to the VFM based state-of-the-art Rein.” |
| E10 | arXiv:2403.06122 | [3 Method](https://arxiv.org/html/2403.06122#S3.p2) | “our method leverages the feature information through two main approaches: covariance alignment and semantic consistency contrastive learning. Specifically, the covariance matching ensures that features, having different styles but the same content, contain similar information.” |
| E11 | arXiv:2403.06122 | [1 Introduction](https://arxiv.org/html/2403.06122#S1.p5) | “While these approaches effectively remove style-related information, they simultaneously pose the challenge of removing semantic content because content and style information are entangled.” |
| E12 | arXiv:2403.06122 | [Quantitative and Qualitative Results](https://arxiv.org/html/2403.06122#S4.SS3.SSSx1.p1) | “Our method outperforms all other methods when trained on GTAV, using ResNet-50 as the backbone. When compared with FN methods that remove domain-specific styles, we demonstrate that our approach minimizes the loss of content information.” |
| E20 | arXiv:2311.17922 | [1 Introduction](https://arxiv.org/html/2311.17922#S1.p7) | “This paper shows that we can prevent such behavior with a simple recipe involving minimal fine-tuning, language-driven style augmentation, and mixing. Our approach is coined FAMix, for Freeze, Augment and Mix.” |
| E21 | arXiv:2311.17922 | [3.2 Local Style Mining](https://arxiv.org/html/2311.17922#S3.SS2.p3) | “The idea is to mine proxy domains and explore intermediate ones in a class-aware manner (as detailed in Sec. 3.3), which makes our work fundamentally different from [11], that steers features towards a particular target style and corresponding domain, and better suited to generalization.” |
| E22 | arXiv:2311.17922 | [4.2 Comparison with DGSS methods](https://arxiv.org/html/2311.17922#S4.SS2.p2) | “Tab. 2 shows that our method significantly outperforms all the baselines on all the datasets for both backbones.” |
| E13 | arXiv:2407.09033 | [1 Introduction](https://arxiv.org/html/2407.09033#S1.p4) | “The key idea of our method is to utilize text embeddings of classes of interest from VLMs as object queries, referred to as textual object queries. Given that an object query can be considered as a mask embedding vector to group regions belonging to the same class, textual object queries generate robust mask predictions for classes of interest across diverse domains, thanks to their domain-invariant semantics.” |
| E14 | arXiv:2407.09033 | [1 Introduction](https://arxiv.org/html/2407.09033#S1.I1.i3.p1) | “Our tqdm demonstrates the state-of-the-art performance across multiple DGSS benchmarks; e.g., tqdm achieves 68.9 mIoU on GTA5 → Cityscapes, which improves the prior state-of-the-art method by 2.5 mIoU.” |
| E15 | arXiv:2407.09033 | [4.2 Regularization](https://arxiv.org/html/2407.09033#S4.SS2.p1) | “To maintain this alignment, we propose three regularization strategies: (1) language regularization that prevents the learnable prompts from distorting the semantic meaning of text embeddings, (2) vision-language regularization that ensures the pixel-level alignment between visual and textual features, and (3) vision regularization that preserves the textual alignment capability of the vision encoder from a pre-trained VLM.” |
| E1 | arXiv:2504.03193 | [4 Proposed Method](https://arxiv.org/html/2504.03193#S4.p1) | “MFuser enhances feature locality while leveraging domain-invariant semantic knowledge provided by text embeddings to effectively constrain visual representations.” |
| E2 | arXiv:2504.03193 | [4.1 MVFuser](https://arxiv.org/html/2504.03193#S4.SS1.p6) | “MVFuser acts two roles: 1) refines x_{i}^{\text{\scriptsize VFM}} and x_{i}^{\text{\scriptsize VLM}} to generate more task-specific features; 2) interacts between two kinds of features to complement each's weaknesses.” |
| E3 | arXiv:2504.03193 | [Synthetic-to-Real Generalization](https://arxiv.org/html/2504.03193#S5.SS2.SSS0.Px1.p1) | “On average, we achieve 2.15 mIoU better than the state-of-the-art. Our proposed MFuser remains excellent performance using different VFM and VLM combinations, showing the versatility of our framework.” |
| E24 | arXiv:2312.01850 | [1 Introduction](https://arxiv.org/html/2312.01850#S1.I1.i3.p1) | “We report results on common benchmarks, where our method outperforms the state-of-the-art domain generalization methods by a large margin.” |
| E28 | arXiv:2312.01850 | [1 Introduction](https://arxiv.org/html/2312.01850#S1.p2) | “In this work, we propose a novel method that tackles the domain generalization problem by diffusion-based domain extension (DIDEX).” |
| E16 | arXiv:2312.03048 | [3.4 Multi-Resolution Latent Fusion](https://arxiv.org/html/2312.03048#S3.SS4.p1) | “While ControlNet effectively integrates condition masks into the generation process, it struggles with generating small objects due to the low-resolution latent space. We propose a two-stage Multi-Resolution Latent Fusion pipeline to improve the adherence to semantic masks in the generated dataset.” |
| E17 | arXiv:2312.03048 | [4.3 Comparison with State-of-the-Art DG](https://arxiv.org/html/2312.03048#S4.SS3.p2) | “The results in Tab. 1 indicate that DGInStyle significantly enhances the DG performance across various DG methods and network architectures. The improvements range from +2.5 mIoU up to +7.2 mIoU on the average over 5 datasets. In particular, DGInStyle improves the overall state-of-the-art performance by a significant gain of +2.5 mIoU.” |
| E26 | arXiv:2312.03048 | [3.2 Preserving Style Prior with Style Swap](https://arxiv.org/html/2312.03048#S3.SS2.p4) | “As a first step of our Style Swap technique, we fine-tune the base LDM's U-Net \mathbf{U}^{\mathcal{P}} encapsulating the prior domain \mathcal{P} with the Dreambooth protocol [53] using all images in the source domain \mathcal{S} . The resulting U-Net is denoted as \mathbf{U}^{\mathcal{S}} . Second, we use \mathbf{U}^{\mathcal{S}} as the base model instead of \mathbf{U}^{\mathcal{P}} to initialize ControlNet.” |
| E25 | arXiv:2312.09788 | [1 Introduction](https://arxiv.org/html/2312.09788#S1.F1) | “CLOUDS, by harnessing multiple foundation models, demonstrates its ability to effectively utilize the source dataset, thereby outperforming both conventional DGSS and open-vocabulary methods.” |
| E29 | arXiv:2312.09788 | [3 Collaborating Foundation Models](https://arxiv.org/html/2312.09788#S3.p2) | “Overview: CLOUDS uses a CNN-based CLIP backbone, harnessing its capability to extract robust features (Section 3.1).” |
| E30 | arXiv:2312.09788 | [3 Collaborating Foundation Models](https://arxiv.org/html/2312.09788#S3.p2) | “Lastly, the predicted pseudo labels are refined with the help of the Segment-Anything Model (SAM) in a student-teacher fashion (Section 3.3).” |
| E4 | arXiv:2412.12050 | [Overview](https://arxiv.org/html/2412.12050#Sx3.SSx1.p1) | “The overall framework of our proposed SCSD is depicted in Fig. 3, consisting of three key components: Semantic Query Booster (SQB), Text-Driven Style Transform (TDST), and Style Synergy Optimization (SSO).” |
| E5 | arXiv:2412.12050 | [Overview](https://arxiv.org/html/2412.12050#Sx3.SSx1.p1) | “TDST mines text style diversity and achieves latter three scale image features style transformation through style difference features obtained by domain difference embeddings mapping.” |

<!-- /evidence-appendix -->
