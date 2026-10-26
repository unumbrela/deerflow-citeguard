# Systematic Literature Review: Self-Supervised Visual Representation Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "self-supervised visual representation", filtered to category cs.CV, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The field of self-supervised visual representation learning has evolved significantly over the past two years, with research focusing on addressing fundamental challenges in representation collapse, training efficiency, and the integration of multimodal knowledge. The surveyed literature reveals a maturing field moving beyond simple contrastive and non-contrastive methods toward more sophisticated frameworks that incorporate theoretical foundations, latent-space modeling, and cross-modal knowledge transfer. Key advances include theoretical unification of SSL principles, novel approaches to masked image modeling in latent spaces, innovative training paradigms comparing joint versus pretrain-finetune strategies, and exploration of LLM-vision model integration. The collective work demonstrates both incremental improvements to existing methods and paradigm-shifting insights into the nature of self-supervised learning itself.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "self-supervised visual representation", filtered to category cs.CV, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Foundations and Unified Frameworks

Recent work has sought to establish theoretical foundations that unify disparate self-supervised learning approaches under common principles. Giakoumoglou et al. (2026) formalize three necessary principles for SSL—observation (semantic invariance), prediction (spatial understanding), and regularization (non-degeneracy)—proving that omitting any one leads to representation collapse. Their theoretical analysis demonstrates that major SSL methods are special cases of a unified energy decomposition, providing mathematical grounding for why certain architectural choices succeed or fail. Similarly, theoretical work on momentum encoders reveals that they converge to the same fixed point as online encoders and provide no collapse guarantee at convergence, challenging assumptions about their role in preventing collapse. This theoretical turn in SSL research marks a shift from purely empirical discoveries to principled understanding of why methods work.

### Theme 2: Latent-Space and Progressive Learning Approaches

A significant thread in recent literature explores moving beyond pixel-level reconstruction to latent-space modeling and progressive training strategies. Wei et al. (2024) pioneer Latent Masked Image Modeling (Latent MIM), addressing challenges of representation collapse, high region correlation in latent space, and decoding conditioning to enable high-level semantic learning while retaining MIM benefits. Erdogan et al. (2025) introduce LayerLock, which exploits the observation that ViT layers converge in depth order during training, progressively freezing layers to accelerate MAE training and enable latent prediction without collapse. These approaches share a common insight: that operating in learned latent spaces or using progressive training schedules can overcome limitations of direct pixel-level objectives while maintaining the region-aware learning that makes MIM effective.

### Theme 3: Training Paradigm Optimization

The question of how to structure SSL training pipelines has received systematic attention, with work comparing traditional pretrain-then-finetune approaches against joint training paradigms. Munia et al. (2026) conduct comprehensive evaluation across eight SSL methods and diverse domains (natural, medical, crisis response, remote sensing), finding that joint training improves data efficiency and robustness in low-label settings, while pretrain-finetuning remains more reliable in specialized domains. This nuanced finding challenges the dominance of the two-stage paradigm and suggests that optimal training strategy depends critically on task characteristics and data availability. The work establishes a benchmark for hybrid SSL-based semi-supervised learning and provides practical guidance for practitioners selecting training strategies.

### Theme 4: Cross-Modal Knowledge Integration

The integration of language model knowledge into vision models represents an emerging direction in SSL. Kuzucu et al. (2025) introduce LAVIE, which co-adapts Vision Transformers and LLM fusion blocks through joint masked auto-encoding with LoRA adaptation, addressing the modality mismatch between text-pretrained LLMs and vision-centric ViTs. Sharma et al. (2024) explore the inverse direction, demonstrating that LLMs trained on text can generate code-based image representations sufficient to train vision models capable of semantic assessment on natural images. These bidirectional approaches—injecting language knowledge into vision models and extracting visual knowledge from language models—suggest that the boundary between vision and language representations is more permeable than previously assumed.

### Theme 5: Feature Representation and Normalization

Fine-grained investigation of feature representation choices reveals that seemingly standard design decisions have profound effects on learning dynamics. Colton (2025) demonstrates that layer normalization in IJEPA disrupts natural token energy hierarchies where high-energy tokens encode semantically important regions, proposing DynTanh activation as an alternative that preserves token energies and improves ImageNet linear probe accuracy from 38% to 42.7%. Wang et al. (2024) address the neglect of equivariant features in augmentation-based SSL, integrating image reconstruction as an auxiliary task that facilitates equivariant feature learning without additional parameters. These works highlight that careful attention to representation properties—invariant versus equivariant, normalized versus energy-preserving—can yield significant performance gains without architectural complexity.

### Theme 6: Domain-Specific Applications and Probing Methods

SSL methods are being adapted to specialized domains while also being probed for their fundamental limitations. Maitra et al. (2024) apply decorrelation-based SSL to writer identification, proposing SWIS which standardizes features along each dimension and outperforms both contemporary SSL frameworks and supervised methods on writer identification benchmarks. Gupta et al. (2026) probe off-manifold behavior of vision encoders using sparse pixel optimization on blank canvases, revealing that both language-aligned (OpenCLIP) and self-supervised (DINOv3) encoders share failure modes where non-semantic inputs can retrieve target semantic basins. These works demonstrate both the practical utility of SSL in specialized domains and the importance of understanding encoder behavior beyond the natural image manifold.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the insight that standard SSL approaches have fundamental limitations requiring architectural or objective modifications. There is broad agreement that representation collapse remains a central challenge across methods (Giakoumoglou et al., 2026; Wei et al., 2024; Erdogan et al., 2025). Papers also converge on the value of progressive or structured approaches—whether progressive layer freezing, latent-space modeling, or staged training—over naive single-objective optimization. The literature collectively suggests that SSL is moving from simple contrastive/non-contrastive dichotomies toward more nuanced, theoretically-grounded frameworks.

**Disagreements**: The literature reveals tension between unified theoretical frameworks and domain-specific optimization. While Giakoumoglou et al. (2026) argue for universal principles necessary across all SSL methods, Munia et al. (2026) find that optimal training strategies are highly task and domain-dependent, with no universal winner between joint training and pretrain-finetuning. Additionally, there is implicit disagreement about the role of external knowledge: some works advocate pure visual self-supervision (Colton, 2025; Erdogan et al., 2025) while others embrace cross-modal integration with language models (Kuzucu et al., 2025; Sharma et al., 2024).

## Gaps and Open Questions

The collective literature reveals several gaps. First, theoretical claims about necessary principles (Giakoumoglou et al., 2026) are scale-dependent and may not generalize beyond studied model sizes and tasks. Second, latent-space approaches (Wei et al., 2024; Erdogan et al., 2025) require careful hyperparameter tuning and sequential addressing of multiple challenges, suggesting remaining brittleness. Third, cross-modal integration methods (Kuzucu et al., 2025; Sharma et al., 2024) have been validated primarily on standard vision tasks, with limited exploration of genuinely multimodal downstream applications. Fourth, domain-specific adaptations (Maitra et al., 2024; Munia et al., 2026) raise questions about transferability across domains—methods optimized for writer identification or medical imaging may not generalize. Finally, probing studies (Gupta et al., 2026) reveal off-manifold failure modes but do not yet provide solutions for robustifying encoders against such vulnerabilities. The field would benefit from work that bridges theoretical unification with practical robustness across diverse domains and scales.

## Per-Paper Annotations

### Colton (2025)

**Research question**: How does feature normalization (layer normalization) affect the learning dynamics and performance of Image Joint Embedding Predictive Architecture models?
**Methodology**: The author proposes replacing layer normalization with DynTanh activation at the teacher encoder output to preserve natural token energy hierarchy, where high-energy tokens encode semantically important regions.
**Key findings**:
- Layer normalization disrupts the natural energy hierarchy of visual tokens in IJEPA
- High-energy tokens (larger L2 norms) encode semantically important image regions
- Feature layer normalization causes checkerboard-like artifacts in loss maps
- DynTanh activation preserves token energies and eliminates checkerboard artifacts
- The modification improves ImageNet linear probe accuracy from 38% to 42.7% for ViT-Small and reduces RMSE by 0.08 on NYU Depth V2 monocular depth estimation
**Limitations**: The empirical study focuses specifically on IJEPA architecture and may not generalize to other self-supervised learning frameworks; the proposed modification requires validation across broader model scales and tasks.

### Erdogan et al. (2025)

**Research question**: How can we accelerate masked autoencoder training and avoid representation collapse in self-supervised visual representation learning?
**Methodology**: The authors observe that ViT layers converge in order of depth during video MAE training, then exploit this by progressively freezing layers according to an explicit schedule, transitioning from pixel to latent prediction.
**Key findings**:
- Shallower ViT layers converge early while deeper layers converge late during MAE training
- Progressive layer freezing accelerates standard MAE training according to an explicit schedule
- The same freezing schedule enables latent prediction without suffering from representation collapse
- The approach scales to large models up to 4B parameters
- LayerLock surpasses non-latent masked prediction performance on the 4DS perception suite
**Limitations**: The approach is specifically designed for video masked-autoencoding models and may not directly generalize to other architectures or self-supervised learning paradigms without adaptation.

### Giakoumoglou et al. (2026)

**Research question**: What principles are necessary for learning visual representations without labels in self-supervised learning?
**Methodology**: The authors formalize three principles (observation, prediction, regularization) and prove theoretical claims about their necessity through mathematical analysis, paired with controlled experiments including patch-retrieval evaluation.
**Key findings**:
- Combining observation and prediction without regularization admits the constant encoder as a global minimizer under negative-free alignment
- The observation and prediction objectives are gradient-complementary and structurally non-conflicting at the encoder output
- Momentum encoder converges to the same fixed point as the online encoder and provides no collapse guarantee at convergence
- Contrastive alignment provides only self-limiting collapse resistance with explicit gradient-decay
- Every major self-supervised method is a special case of a single unified energy decomposition
**Limitations**: The theoretical framework and proofs may not generalize to all SSL architectures beyond those studied; scale-dependent claims about the necessity of all three principles may not hold at significantly different scales.

### Gupta et al. (2026)

**Research question**: How do modern vision encoders behave when inputs are far from the natural-image manifold, and can sparse pixel edits reveal their representation geometry?
**Methodology**: The authors apply sparse pixel edits to blank canvases using a simple pixel-level hill-climbing procedure to probe whether optimized inputs can retrieve chosen targets in multimodal contrastive and self-supervised visual encoders.
**Key findings**:
- Sparse edits on blank, visually non-semantic inputs can enter target semantic basins in vision encoders
- On OpenCLIP, inputs optimized toward class prompts achieve strong top-1 and top-5 targeted retrieval performance
- On DINOv3, inputs optimized toward class prototypes achieve high target alignment and near-top prototype ranks
- Both language-aligned and self-supervised visual encoders share a common off-manifold failure mode
- Sparse blank-canvas optimization serves as a simple probe of representation geometry
**Limitations**: The black-box probing approach is limited to the tested encoders (OpenCLIP, DINOv3) and evaluation datasets (ImageNet, Flickr30k), and may not generalize to all vision encoder architectures or reveal all failure modes.

### Kuzucu et al. (2025)

**Research question**: How can the modality mismatch between text-pretrained LLMs and vision transformers be bridged for vision-only tasks?
**Methodology**: The authors introduce LAVIE (Language-Adapted Vision Enhancer), which co-adapts a ViT backbone and LLM fusion block by employing MAE to pre-train the ViT and concurrently training LoRA layers within the LLM block using the same MAE objective.
**Key findings**:
- LAVIE significantly improves performance in various downstream vision tasks
- Joint optimization guides the ViT to produce LLM-aligned features
- LoRA enables effective LLM adaptation to interpret visual information
- Frozen LLM knowledge can be effectively leveraged through synergistic pre-training
- The approach offers an effective and efficient way to enhance visual understanding
**Limitations**: Requires careful tuning of LoRA parameters and MAE objectives; may not generalize to all vision-language fusion scenarios or LLM architectures beyond those tested.

### Maitra et al. (2024)

**Research question**: Can decorrelation-based self-supervised learning be effectively applied to learn disentangled stroke features for writer identification?
**Methodology**: The authors propose SWIS, a modified decorrelation-based framework that standardizes features along each dimension on top of the existing framework, originally proposed for signature verification.
**Key findings**:
- SWIS outperforms contemporary self-supervised learning frameworks on writer identification benchmarks
- The proposed framework outperforms several supervised methods as well
- This is the first work to apply self-supervised learning for learning representations for writer verification tasks
- Decorrelation-based self-supervised pretraining yields performance at par with supervised and contrastive SSL baselines
- Disentangled stroke features can be effectively learned through the decorrelation-based paradigm
**Limitations**: Evaluation is limited to writer identification benchmarks and may not generalize to other document analysis or biometric verification tasks; the standardization approach may require tuning for different writing styles or scripts.

### Munia et al. (2026)

**Research question**: Does jointly optimizing self-supervised and supervised objectives during training provide a better alternative to the standard pretraining-then-finetuning pipeline?
**Methodology**: The authors systematically compare pretraining-followed-by-finetuning (PFT) versus joint training (JT) across eight representative SSL methods and diverse computer vision tasks on natural, medical, crisis response, and remote sensing data under varying percentages of labeled data.
**Key findings**:
- The relative effectiveness of PFT and JT depends strongly on the task, labeled data availability, and domain complexity
- Joint training consistently improves data and training efficiency while being robust in low-label settings
- Pretrain-finetuning is more reliable in more specialized domains
- JT shows robustness in low-label settings across diverse tasks
- Different domains show different optimal training strategies
**Limitations**: Results may not generalize to all SSL methods or domains beyond those tested; the optimal strategy is task-dependent, making universal recommendations difficult.

### Sharma et al. (2024)

**Research question**: What visual knowledge do large language models acquire from learning to model relationships between strings?
**Methodology**: The authors systematically evaluate LLMs' abilities to generate and recognize visual concepts of increasing complexity using code to represent images, and demonstrate training a preliminary visual representation learning system using text-only models.
**Key findings**:
- LLM-generated images do not resemble natural images but contain learnable visual concept knowledge
- LLMs can generate and recognize an assortment of visual concepts of increasing complexity
- LLMs demonstrate ability to correct their own generated images
- Images generated with text models can train vision models capable of semantic assessments on natural images
- Precise modeling of strings can teach language models about numerous aspects of the visual world
**Limitations**: LLM-generated images do not look like natural images, and the visual representation learning system trained from text models is preliminary, potentially limiting practical applicability compared to dedicated vision models.

### Wang et al. (2024)

**Research question**: How can augmentation-based self-supervised learning methods learn equivariant features in addition to invariant ones to improve generalizability?
**Methodology**: The authors integrate an image reconstruction task as an auxiliary component using cross-attention to blend features from two augmented views and reconstruct one of them, without adding additional parameters.
**Key findings**:
- Standard augmentation-based SSL methods excel at invariant features but often neglect equivariant ones
- Image reconstruction as an auxiliary task facilitates equivariant feature learning without additional parameters
- Cross-attention mechanism effectively blends features from augmented views for reconstruction
- The method shows significant improvements on both artificial (3DIEBench) and natural (ImageNet) datasets
- The approach excels particularly in scenarios involving combined augmentations, enhancing both invariant and equivariant feature learning
**Limitations**: Evaluation focused on specific benchmarks and datasets; the method may require tuning for different augmentation strategies and downstream tasks beyond those tested.

### Wei et al. (2024)

**Research question**: Can masked reconstruction in latent space combine the locality benefits of MIM with high-level semantic learning?
**Methodology**: Through carefully designed experiments and extensive analysis, the authors identify and sequentially address challenges in Latent MIM including representation collapsing, learning objectives, region correlation in latent space, and decoding conditioning.
**Key findings**:
- Latent MIM can learn high-level representations while retaining the benefits of MIM models
- Representation collapsing occurs with joint online/target optimization
- High region correlation in latent space poses significant training challenges
- Decoding conditioning affects the quality of learned representations
- Sequential addressing of identified issues enables successful Latent MIM training
**Limitations**: Training Latent MIM remains challenging and requires careful handling of multiple issues; the approach may require more hyperparameter tuning than standard pixel-level MIM.

## References

Colton, A. (2025). Elucidating the role of feature normalization in IJEPA. arXiv. https://arxiv.org/abs/2508.02829

Erdogan, G., Parthasarathy, N., Ionescu, C., Hudson, D. A., Lerchner, A., Zisserman, A., Sajjadi, M. S. M., & Carreira, J. (2025). LayerLock: Non-collapsing representation learning with progressive freezing. arXiv. https://arxiv.org/abs/2509.10156

Giakoumoglou, N., Giakoumoglou, P., & Stathaki, T. (2026). Three necessary principles for self-supervised visual representation learning. arXiv. https://arxiv.org/abs/2608.08309

Gupta, A., Pandya, A., Adami, C., & Dolson, E. (2026). SPOOK: Sparse pixel optimization for off-manifold knowledge in vision encoders. arXiv. https://arxiv.org/abs/2610.32835

Kuzucu, S., Naeem, M. F., Kukleva, A., Tombari, F., & Schiele, B. (2025). Enhancing self-supervised visual representation learning via low-rank adapted LLMs. arXiv. https://arxiv.org/abs/2507.00754

Maitra, A., Mitra, S., Manna, S., Bhattacharya, S., & Pal, U. (2024). Decorrelation-based self-supervised visual representation learning for writer identification. arXiv. https://arxiv.org/abs/2410.01441

Munia, N., Ward, T., Nayla, N., Massey, M. A., & Imran, A.-A.-Z. (2026). Self-supervised visual representation learning: Pretrain-finetuning or joint training? arXiv. https://arxiv.org/abs/2607.13192

Sharma, P., Rott Shaham, T., Baradad, M., Fu, S., Rodriguez-Munoz, A., Duggal, S., Isola, P., & Torralba, A. (2024). A vision check-up for language models. arXiv. https://arxiv.org/abs/2401.01862

Wang, Q., Krajsek, K., & Scharr, H. (2024). Equivariant representation learning for augmentation-based self-supervised learning via image reconstruction. arXiv. https://arxiv.org/abs/2412.03314

Wei, Y., Gupta, A., & Morgado, P. (2024). Towards latent masked image modeling for self-supervised visual representation learning. arXiv. https://arxiv.org/abs/2407.15837
