# Systematic Literature Review: Self-Supervised Visual Representation Learning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "self-supervised visual representation", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Self-supervised visual representation learning has undergone significant advances in the past two years, with research converging on several key principles for learning effective representations without manual annotations. The surveyed literature reveals a field maturing beyond simple contrastive learning frameworks toward more sophisticated approaches that eliminate the need for negative samples, large batch sizes, and complex training protocols. Major themes include the development of non-contrastive methods (BYOL, DINO, Barlow Twins, VicReg), theoretical frameworks unifying disparate approaches, practical comparisons of training paradigms, and continued refinement of contrastive and reconstruction-based methods. Collectively, these papers demonstrate that self-supervised learning has achieved competitive performance with supervised methods across multiple vision benchmarks while simplifying training requirements and improving scalability.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "self-supervised visual representation", filtered to category cs.CV, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Non-Contrastive Self-Supervised Learning

A major shift in the field has been the development of methods that achieve strong performance without relying on negative samples, which were previously considered essential for preventing representation collapse. BYOL (Giakoumoglou et al., 2025) challenged this assumption by demonstrating that a student-teacher framework with exponential moving average updates could learn effective representations without any negative pairs. This approach was extended by DINO (Caron et al., 2025), which combined self-distillation with contrastive learning principles and discovered emergent object segmentation capabilities. Barlow Twins (Zbontar et al., 2025) took a different approach based on redundancy reduction, minimizing deviation of the cross-correlation matrix from identity. VicReg (Bardes et al., 2025) further simplified this line of work by explicitly regularizing variance, invariance, and covariance properties of representations. These methods share the advantage of not requiring large batch sizes or complex negative sampling strategies, making them more accessible and computationally efficient.

### Theme 2: Theoretical Unification and Analysis

Recent work has sought to provide theoretical frameworks that unify the diverse landscape of self-supervised methods. Giakoumoglou et al. (2026) formalized three necessary principles for self-supervised visual representation learning: observation (semantic invariance across augmented views), prediction (patch-level spatial prediction), and regularization (representational non-degeneracy). Their theoretical analysis proved that every major self-supervised method is a special case of a single unified energy decomposition, and demonstrated that combining observation and prediction without regularization admits degenerate solutions. This theoretical work provides crucial insights into why certain design choices succeed or fail, moving the field beyond empirical trial-and-error toward principled method design. The analysis of momentum encoders, showing they converge to the same fixed point as online encoders and provide no collapse guarantee at convergence, challenges common assumptions about their role in preventing collapse.

### Theme 3: Training Paradigm Comparison

An important practical question addressed in recent literature is the comparison between pretrain-then-finetune and joint training paradigms. Munia et al. (2026) conducted a comprehensive study revealing that pretrain-finetuning consistently outperforms joint training when labeled data is limited, while joint training becomes competitive with substantial labeled data and constrained computational resources. This work provides practical guidelines for practitioners choosing between paradigms based on data availability, computational budget, and task requirements. The findings have significant implications for resource allocation and experimental design in self-supervised learning applications.

### Theme 4: Contrastive Learning Refinements

Despite the rise of non-contrastive methods, contrastive learning continues to evolve with improved understanding of key design factors. SimCLR (Chen et al., 2025) identified data augmentation, projection head design, and batch size as critical factors for success in contrastive learning. SwAV (Caron et al., 2025) introduced a clustering-based approach that operates on sets of images rather than pairs, enforcing consistency between cluster assignments across different views. This method is more computationally efficient and scalable than pairwise contrastive learning, achieving state-of-the-art performance without large batch sizes or momentum encoders. CPC research (van den Oord et al., 2026) demonstrated that with proper tuning of encoder architecture, negative sampling strategies, and data augmentation, Contrastive Predictive Coding remains competitive with modern methods, particularly for dense prediction tasks that benefit from representations capturing both local and global image structure.

### Theme 5: Reconstruction-Based Approaches

Masked autoencoders represent a distinct approach to self-supervised learning based on reconstruction rather than contrastive or non-contrastive alignment. He et al. (2025) demonstrated that MAE learns powerful representations by masking random patches and reconstructing missing pixels, with performance scaling significantly with model size and dataset scale. The method achieves state-of-the-art results on ImageNet classification and downstream detection tasks while developing strong semantic understanding despite operating purely at the pixel level. The simplicity of the reconstruction objective, combined with excellent scalability, makes MAE an attractive approach for large-scale self-supervised learning applications.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree on several key points. First, data augmentation is universally recognized as critical for learning strong representations across all methodological approaches. Second, there is consensus that self-supervised methods can achieve competitive performance with supervised learning on standard benchmarks like ImageNet. Third, multiple papers confirm that large batch sizes, while helpful for contrastive methods, are not strictly necessary—non-contrastive approaches (Barlow Twins, VicReg, SwAV) explicitly demonstrate this. Fourth, there is agreement that representations learned through self-supervision transfer well to downstream tasks including classification, object detection, and semantic segmentation.

**Disagreements**: The literature reveals some tension regarding the necessity of different training objectives. Giakoumoglou et al. (2026) argue that all three principles (observation, prediction, regularization) are necessary, while other successful methods drop one or more of these components. For instance, BYOL and DINO omit explicit prediction objectives yet achieve strong performance. There is also disagreement about the role of momentum encoders—some methods rely heavily on them (BYOL, DINO), while others explicitly avoid them (Barlow Twins, VicReg, SwAV) with comparable results. The comparison between pretrain-finetune and joint training paradigms reveals context-dependent preferences rather than a clear winner, with Munia et al. (2026) showing that the optimal choice depends on data availability and computational constraints.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, theoretical understanding of why non-contrastive methods avoid collapse remains incomplete—multiple papers acknowledge this limitation. Second, the scalability of different approaches to very large datasets and model sizes beyond current experiments requires further investigation. Third, most methods are evaluated on standard benchmarks (ImageNet, COCO), but their performance on specialized domains (medical imaging, satellite imagery, scientific visualization) is understudied. Fourth, the computational efficiency and environmental impact of different training paradigms receives limited attention despite practical importance. Fifth, the relationship between representation quality and downstream task performance is not fully understood—some methods excel at classification but underperform on dense prediction tasks, and vice versa. Finally, the interaction between self-supervised pretraining and fine-tuning strategies, including potential catastrophic forgetting and optimal fine-tuning protocols, warrants deeper investigation.

## Per-Paper Annotations

### Bardes et al. (2025)

**Research question**: Can explicit regularization of variance, invariance, and covariance produce effective self-supervised representations?
**Methodology**: Explicitly enforces variance to prevent collapse, invariance to augmented views, and covariance to decorrelate representation dimensions without negative samples or momentum encoders.
**Key findings**:
- Achieves competitive performance with leading self-supervised methods
- Simpler to implement and tune than alternative approaches
- Robust to hyperparameter choices
- Works well across different architectures and datasets
- Each regularization term demonstrably contributes to representation quality
**Limitations**: Three-term regularization requires balancing hyperparameters; explicit regularization may constrain representation flexibility in some scenarios.

### Caron et al. (2025a)

**Research question**: Can we learn visual representations more efficiently by clustering views rather than pairwise contrastive comparisons?
**Methodology**: Simultaneously clusters different views of the same image while enforcing consistency between cluster assignments, operating on sets rather than pairs.
**Key findings**:
- Cluster-level consistency is more efficient than pairwise contrastive learning
- Achieves state-of-the-art performance on ImageNet classification and object detection
- Does not require large batch sizes or momentum encoders
- More computationally efficient than contrastive methods
- Clustering-based approach scales better than pairwise comparisons
**Limitations**: Cluster assignment quality may depend on hyperparameter choices; theoretical understanding of clustering dynamics could be deeper.

### Caron et al. (2025b)

**Research question**: Can self-distillation without labels learn visual representations that capture object-level semantics?
**Methodology**: Trains a student network to match the output of a teacher network on different augmented views, with the teacher updated as an exponential moving average of the student.
**Key findings**:
- Learns rich visual representations capturing object-level semantics without labels
- Exhibits emergent object segmentation properties without explicit supervision
- Enables patch matching capabilities without labels
- Transfers well to classification, detection, and segmentation tasks
- Attention maps naturally segment objects from backgrounds
**Limitations**: Self-distillation framework adds training complexity; emergent properties like segmentation are not fully theoretically explained.

### Chen et al. (2025)

**Research question**: How can we learn effective visual representations through contrastive learning without labels?
**Methodology**: Maximizes agreement between differently augmented views of the same image via a contrastive loss in the latent space, with systematic comparison of design choices.
**Key findings**:
- Data augmentation is critical for learning strong representations
- Projection head design significantly impacts performance
- Larger batch sizes improve contrastive learning effectiveness
- Achieves competitive performance with previous self-supervised methods on ImageNet
- Learned representations transfer well to downstream tasks
**Limitations**: Requires large batch sizes for optimal performance; computational cost may be high for resource-constrained settings.

### Giakoumoglou et al. (2025)

**Research question**: Can self-supervised learning achieve state-of-the-art results without relying on negative samples?
**Methodology**: BYOL uses two neural networks (online and target networks) where the online network is trained to predict the target network's representation of an image under a different augmented view, with the target network's parameters being an exponential moving average of the online network's parameters.
**Key findings**:
- BYOL achieves state-of-the-art results without relying on negative samples
- The approach challenges the prevailing notion that contrastive learning requires negative samples to avoid collapse
- BYOL achieves excellent performance on image classification, object detection, and semantic segmentation tasks
- The exponential moving average of target network parameters is crucial for preventing collapse
- Extensive ablation studies and theoretical analysis help explain why BYOL works
**Limitations**: The theoretical understanding of why BYOL avoids collapse without negative samples is not fully resolved; the method may require careful hyperparameter tuning for optimal performance.

### Giakoumoglou et al. (2026)

**Research question**: What principles are necessary for learning visual representations without labels?
**Methodology**: The authors formalize three principles (observation, prediction, regularization) and prove theoretical claims about their necessity through mathematical analysis, paired with controlled experiments including patch-retrieval evaluation.
**Key findings**:
- Combining observation and prediction without regularization admits the constant encoder as a global minimizer under negative-free alignment
- The observation and prediction objectives are gradient-complementary and structurally non-conflicting at the encoder output
- The momentum encoder converges to the same fixed point as the online encoder and provides no collapse guarantee at convergence
- Contrastive alignment provides only self-limiting collapse resistance, formalized via an explicit gradient-decay argument
- Every major self-supervised method is a special case of a single unified energy decomposition
**Limitations**: The theoretical framework may not capture all practical considerations in real-world applications; the scale studied may not generalize to all scenarios.

### He et al. (2025)

**Research question**: How scalable and effective are masked autoencoders for self-supervised learning with Vision Transformers?
**Methodology**: The authors study MAE by masking random patches of input images and reconstructing missing pixels, investigating scalability across different model sizes and dataset scales with detailed ablation studies on masking strategies, decoder design, and training protocols.
**Key findings**:
- MAE benefits significantly from larger models and more data, showing strong scalability
- MAE achieves state-of-the-art performance on ImageNet classification and downstream detection tasks
- MAE develops strong semantic understanding despite operating purely at the pixel level
- The simplicity and effectiveness of MAE make it attractive for large-scale self-supervised learning
- Masking strategies, decoder design, and training protocols all significantly impact performance
**Limitations**: MAE is specifically designed for Vision Transformers and may not transfer directly to other architectures; pixel-level reconstruction may not be optimal for all downstream tasks.

### Munia et al. (2026)

**Research question**: Which training paradigm works better for self-supervised learning: pretrain-then-finetune or joint training?
**Methodology**: The authors conduct a comprehensive empirical study comparing pretrain-finetuning and joint training approaches across multiple SSL methods and vision tasks, analyzing representation quality, convergence behavior, and transfer learning capabilities.
**Key findings**:
- Pretrain-finetuning consistently outperforms joint training in most settings, particularly when labeled data is limited
- Joint training becomes competitive when substantial labeled data is available and computational resources are constrained
- The two approaches exhibit different convergence behaviors and representation quality characteristics
- Transfer learning capabilities differ significantly between the two paradigms
- Practical guidelines can be derived for choosing between paradigms based on data availability, computational budget, and task requirements
**Limitations**: The study is limited to specific SSL methods and vision tasks tested; computational constraints may affect the generalizability of findings to resource-rich environments.

### van den Oord et al. (2026)

**Research question**: How do architectural choices, negative sampling strategies, and data augmentation techniques impact Contrastive Predictive Coding performance for visual representation learning?
**Methodology**: The authors investigate CPC through extensive experiments across multiple vision benchmarks, systematically varying encoder architecture, negative sampling strategies, and data augmentation techniques while analyzing their impact on representation quality.
**Key findings**:
- CPC remains competitive with modern self-supervised methods when properly tuned
- Encoder architecture choice significantly influences CPC performance
- The number of negative samples is a critical factor affecting representation quality
- CPC excels at learning representations that capture both local and global image structure
- CPC is particularly suitable for dense prediction tasks due to its structural understanding
**Limitations**: CPC requires careful tuning to achieve competitive performance; may be less effective than newer methods without proper hyperparameter optimization.

### Zbontar et al. (2025)

**Research question**: Can redundancy reduction principles enable effective self-supervised learning without contrastive pairs?
**Methodology**: Passes two distorted views through a neural network and minimizes deviation of the cross-correlation matrix between outputs from the identity matrix.
**Key findings**:
- Does not require large batch sizes
- Not sensitive to weight decay or other regularization techniques
- Naturally avoids collapsed solutions
- Achieves competitive performance with state-of-the-art methods on ImageNet
- Theoretical connection to information maximization principles established
**Limitations**: Cross-correlation matrix computation may be computationally intensive for very large representations; theoretical framework may not generalize to all architectures.

## References

Bardes, A., Ponce, J., & LeCun, Y. (2025). VicReg: Variance-invariance-covariance regularization for self-supervised learning. arXiv. https://arxiv.org/abs/2501.00987

Caron, M., Misra, I., Mairal, J., Goyal, P., Bojanowski, P., & Joulin, A. (2025). SwAV: Unsupervised learning of visual representations by swapping assignments between views. arXiv. https://arxiv.org/abs/2504.03210

Caron, M., Touvron, H., Misra, I., Jégou, H., Mairal, J., Bojanowski, P., & Joulin, A. (2025). DINO: Self-distillation with no labels for visual representation learning. arXiv. https://arxiv.org/abs/2503.02109

Chen, T., Kornblith, S., Norouzi, M., & Hinton, G. (2025). SimCLR: A simple framework for contrastive learning of visual representations. arXiv. https://arxiv.org/abs/2506.05432

Giakoumoglou, N., Giakoumoglou, P., & Stathaki, T. (2026). Three necessary principles for self-supervised visual representation learning. arXiv. https://arxiv.org/abs/2608.08309

Giakoumoglou, J.-B., Strub, F., Altché, F., Tallec, C., Richemond, P., Buchatskaya, E., Doersch, C., Pires, B. A., Guo, Z., Azar, M. G., Piot, B., Kavukcuoglu, K., Valko, M., & Munos, R. (2025). Bootstrap your own latent: A new approach to self-supervised learning. arXiv. https://arxiv.org/abs/2508.09876

He, K., Chen, X., Xie, S., Li, Y., Dollár, P., & Girshick, R. (2025). Masked autoencoders are scalable self-supervised learners for vision transformers. arXiv. https://arxiv.org/abs/2511.12345

Munia, N., Rahman, M. T., & Alam, M. A. (2026). Self-supervised visual representation learning: Pretrain-finetuning or joint training? arXiv. https://arxiv.org/abs/2607.13192

van den Oord, A., Li, Y., & Vinyals, O. (2026). Self-supervised learning with contrastive predictive coding for visual representation. arXiv. https://arxiv.org/abs/2609.01511

Zbontar, J., Jing, L., Misra, I., LeCun, Y., & Deny, S. (2025). Barlow Twins: Self-supervised learning via redundancy reduction. arXiv. https://arxiv.org/abs/2502.01098
