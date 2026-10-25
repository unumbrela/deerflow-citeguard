# Systematic Literature Review: 3D Gaussian Splatting

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "3D Gaussian splatting", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

3D Gaussian Splatting (3DGS) has emerged as a transformative technique for real-time radiance field rendering, offering superior speed and quality compared to neural implicit representations like NeRF. The surveyed literature from 2024-2026 reveals a rapidly evolving field focused on addressing three core challenges: computational efficiency, memory/storage demands, and domain-specific adaptations. Recent work demonstrates significant progress in optimization techniques (achieving 26-38% reductions in training time and computational costs), compression methods enabling mobile deployment, and specialized applications ranging from human body reconstruction to language-guided scene understanding. The field shows strong convergence around explicit Gaussian representations as a foundation, with divergent approaches to scaling, compression, and semantic integration.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "3D Gaussian splatting", filtered to category cs.CV, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Performance Optimization

A dominant research direction focuses on improving the computational efficiency of 3DGS through both algorithmic and hardware-level optimizations. The work by Vicente (2026) demonstrates that low-level C++/CUDA re-implementation can achieve substantial gains, with a 26.8% reduction in training time and 13.3% fewer Gaussians while maintaining superior visual quality. Similarly, Jo et al. (2024) address the rendering bottleneck by identifying and excluding unnecessary Gaussians through clustering, achieving a 38.3% reduction in rendering computation without sacrificing PSNR. These approaches share a common insight: the explicit nature of 3DGS representations enables targeted optimization strategies that are difficult or impossible with neural implicit methods. The hardware accelerator proposed by Jo et al. (2024) achieves 10.7x speedup over GPU execution, suggesting that custom hardware support could further amplify efficiency gains. Lin (2024) takes a complementary approach, conducting over 2000 experiments to identify optimal configurations across multiple dimensions of the 3DGS pipeline, introducing novel compression techniques that improve training efficiency.

### Theme 2: Compression and Memory Reduction

The high storage and memory demands of 3DGS represent a critical barrier to practical deployment, particularly for mobile devices and VR headsets. Bagdasarian et al. (2024) provide the first comprehensive survey of compression methods, establishing a unified framework that distinguishes between compression (reducing file size) and compaction (minimizing Gaussian count). Their analysis reveals that methods developed in parallel over a short period lacked standardized comparison, making it difficult to assess relative merits. The survey classifies approaches by their optimization target and establishes consistent evaluation metrics across datasets. This work is particularly timely given that 3DGS models, while offering real-time rendering, require significant memory that limits applicability in resource-constrained environments. The distinction between compression and compaction is crucial: some applications prioritize download size and storage (compression), while others benefit more from reduced Gaussian counts that directly impact rendering speed (compaction).

### Theme 3: Domain-Specific Applications

3DGS has proven particularly effective for specialized reconstruction tasks that benefit from explicit geometric representations. Li et al. (2024) adapt 3DGS for dynamic clothed human reconstruction, addressing the challenge of non-rigid deformations through pose-guided deformation fields that associate Gaussians across canonical and observation spaces. Their method achieves state-of-the-art photorealistic rendering while handling complex cloth dynamics. Pan et al. (2025) extend this to the even more challenging problem of hair strand reconstruction, where the explicit Gaussian representation naturally aligns with strand geometry. Their multi-stage pipeline reconstructs individual strands through a differentiable rasterizer, merges segments into coherent strands, and refines under photometric supervision. Notably, they introduce a new evaluation metric for topological accuracy, addressing a gap in existing methods that focus on geometric quality while neglecting strand connectivity. These domain-specific adaptations demonstrate that 3DGS is not merely a general-purpose renderer but provides particular advantages for articulated and deformable objects where explicit geometry matters.

### Theme 4: Self-Supervised and Latent Learning

A promising direction involves learning reusable 3DGS representations without exhaustive supervision. Ren et al. (2026) introduce Gaussian-JEPA, which predicts representations of held-out Gaussian token blocks from visible context using joint-embedding predictive learning. Unlike reconstruction-based methods that tie supervision to specific Gaussian realizations, Gaussian-JEPA operates in latent space, providing more consistent features across different samplings of the same object. The approach uses an online encoder for context processing and a shared exponential-moving-average encoder for multi-scale targets with stop-gradient features. Evaluated on Gaussian resampling, partial observations, and transfer tasks (part segmentation, object classification), Gaussian-JEPA demonstrates superior consistency and stronger frozen features compared to matched reconstruction pretraining. This work suggests that latent prediction objectives may be more effective than direct attribute reconstruction for learning generalizable 3DGS representations, paralleling broader trends in self-supervised learning toward latent-space prediction rather than pixel-level reconstruction.

### Theme 5: Image Quality Enhancement

Real-world deployment of 3DGS requires robustness to imperfections in training data, particularly motion blur, defocus, and camera shake. Lee et al. (2024) address this with a real-time deblurring framework that uses a small MLP to manipulate the covariance of each 3D Gaussian, modeling scene blurriness directly in the representation. Unlike prior deblurring approaches designed for volumetric NeRF rendering, this method maintains 3DGS's real-time rendering advantage while reconstructing sharp details from blurry inputs. The approach handles multiple blur types (lens defocusing, object motion, camera shake) and demonstrates effectiveness on benchmark datasets. This work highlights an important trade-off: while 3DGS achieves superior speed and quality under ideal conditions, practical applications require handling real-world image degradation. The covariance manipulation approach is elegantly matched to the Gaussian representation, suggesting that domain-specific solutions can preserve 3DGS's advantages while extending robustness.

### Theme 6: Language-Guided Scene Understanding

Integrating vision-language capabilities with 3DGS enables semantic scene understanding beyond geometric reconstruction. Ding et al. (2026) identify a critical limitation in existing referring 3DGS methods: restriction to single-target queries, which fails to capture real-world instruction ambiguity. They introduce the Generalized Referring 3D Gaussian Splatting Segmentation (GR3DGS) task, requiring dynamic segmentation of arbitrary target counts (0, 1, or N). Their ZeroSplat approach lifts 2D Vision-Language Model priors into 3D space through multi-view geometric constraints, achieving intrinsic point-level understanding without per-scene optimization or heavy feature storage. The training-free, zero-feature design significantly outperforms state-of-the-art methods in both generalized and single-target scenarios while maintaining exceptional efficiency. This work demonstrates that 3DGS can serve as a foundation for language-guided interaction without sacrificing the efficiency that makes it attractive, and the new benchmarks (GR-LERF, GR-ScanNet) establish evaluation standards for future work.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively affirm that 3DGS's explicit Gaussian representation provides fundamental advantages over neural implicit methods for real-time rendering, editing, and domain-specific adaptation. Multiple papers independently validate that optimization targeting Gaussian primitives directly (whether through pruning, compression, or hardware acceleration) yields substantial efficiency gains without quality degradation. There is also convergence around the need for standardized evaluation frameworks, as evidenced by the introduction of new benchmarks (GR-LERF, GR-ScanNet by Ding et al., 2026; unified compression evaluation by Bagdasarian et al., 2024) and topological metrics (Pan et al., 2025).

**Disagreements**: The literature reveals tension between different optimization strategies. Vicente (2026) advocates for low-level C++/CUDA re-implementation within specific frameworks, achieving substantial gains but at the cost of portability. In contrast, Lin (2024) demonstrates improvements through systematic parameter tuning and compression techniques applicable across implementations. Similarly, efficiency approaches diverge between hardware-specific solutions (Jo et al., 2024 propose custom accelerators) versus algorithmic improvements applicable to existing GPU pipelines. The compression survey by Bagdasarian et al. (2024) notes that methods developed in parallel lack consensus on whether to prioritize file size reduction or Gaussian count minimization, reflecting different application priorities.

## Gaps and Open Questions

Several gaps emerge from the collective limitations identified across papers. First, evaluation remains fragmented: multiple papers note their methods are validated only on specific datasets (Mip-NeRF360 appears frequently) or within particular frameworks (LichtFeld-Studio in Vicente, 2026), limiting generalizability claims. Second, the trade-offs between efficiency gains and quality preservation are not systematically explored across methods—while individual papers report Pareto improvements, cross-method comparison is difficult without standardized benchmarks. Third, domain-specific adaptations (human bodies, hair) demonstrate promise but raise questions about which domains benefit most from 3DGS versus alternative representations. Fourth, self-supervised approaches like Gaussian-JEPA (Ren et al., 2026) show potential but require further validation across broader downstream tasks beyond segmentation and classification. Finally, the integration of language and semantics (Ding et al., 2026) is nascent, with open questions about scaling to complex queries and handling ambiguous or context-dependent instructions. The compression survey (Bagdasarian et al., 2024) explicitly notes the lack of comprehensive comparison across methods due to parallel development timelines, suggesting a need for unified evaluation frameworks.

## Per-Paper Annotations

### Bagdasarian et al. (2024)

**Research question**: How can the significant storage and memory demands of 3D Gaussian Splatting be reduced to make it practical for mobile devices and headsets?
**Methodology**: Comprehensive survey classifying existing methods into compression (reducing file size) and compaction (minimizing Gaussian count) categories, establishing a unified framework for comparing methods based on key performance metrics and datasets.
**Key findings**:
- First comprehensive survey providing unified framework to evaluate 3DGS compression techniques
- Methods clearly classified into compression versus compaction approaches with distinct goals
- Both approaches aim to maintain or improve quality while minimizing their respective attributes
- Establishes consistent comparison framework for methods developed in parallel over a short period
- Provides mathematical concepts, implementation details, and design choices for analyzed methods
**Limitations**: Survey nature means no new method is proposed; methods developed over short time period previously lacked comprehensive comparison, so framework is newly established rather than validated over time.

### Ding et al. (2026)

**Research question**: How can 3D Gaussian Splatting support generalized referring segmentation that handles an arbitrary number of targets (0, 1, or N) rather than being restricted to single-target queries?
**Methodology**: Proposes ZeroSplat, a training-free and zero-feature framework that lifts 2D Vision-Language Model (VLM) priors into 3D space through robust multi-view geometric constraints, enabling intrinsic point-level understanding without additional feature storage.
**Key findings**:
- ZeroSplat enables segmentation of arbitrary numbers of targets (0, 1, or N), overcoming the single-target limitation of existing R3DGS methods
- Achieves intrinsic 3D point-level understanding without requiring per-scene optimization or heavy semantic feature embedding
- Significantly outperforms state-of-the-art methods in both generalized and single-target segmentation scenarios
- Maintains exceptional efficiency through the training-free, zero-feature design
- Two new benchmarks (GR-LERF and GR-ScanNet) were constructed for comprehensive evaluation
**Limitations**: The training-free approach may have limitations in specialized scenarios requiring domain-specific adaptation; reliance on 2D VLM priors may inherit their inherent limitations and biases.

### Jo et al. (2024)

**Research question**: How can unnecessary 3D Gaussians be quickly identified and excluded during rendering in real-time without compromising image quality?
**Methodology**: Offline clustering of 3D Gaussians that are close in distance, followed by projection of these clusters onto 2D image plane during runtime to identify unnecessary Gaussians, plus an efficient hardware accelerator architecture to address GPU bottlenecks.
**Key findings**:
- Excludes 63% of 3D Gaussians on average before 2D image projection on Mip-NeRF360 dataset
- Reduces overall rendering computation by 38.3% without sacrificing PSNR
- Proposed hardware accelerator achieves 10.7x speedup compared to GPU execution
- Technique operates in real-time for current view direction rendering
- Identifies computation bottleneck in GPU execution and provides hardware solution
**Limitations**: Requires offline clustering step before runtime; maximum benefit requires custom hardware accelerator rather than standard GPU implementation.

### Lee et al. (2024)

**Research question**: How can 3D Gaussian Splatting reconstruct sharp, clean images from blurry training data caused by lens defocusing, object motion, and camera shake?
**Methodology**: Proposes a novel real-time deblurring framework using a small Multi-Layer Perceptron (MLP) that manipulates the covariance of each 3D Gaussian to model scene blurriness, enabling clean reconstruction from blurry input images.
**Key findings**:
- The proposed MLP-based approach successfully reconstructs fine and sharp details from blurry training images
- The framework maintains real-time rendering capabilities despite the additional deblurring component
- Effectively handles multiple blur types including lens defocusing, object motion, and camera shake
- Benchmark experiments demonstrate superior performance compared to existing approaches
**Limitations**: Requires an additional small MLP which adds some complexity; the approach is specifically designed for rasterization-based 3DGS and may not generalize to all blur scenarios equally well.

### Li et al. (2024)

**Research question**: How can 3D Gaussian Splatting be adapted for dynamic clothed human reconstruction despite challenges from non-rigid deformations and rich cloth details?
**Methodology**: Proposes GaussianBody with explicit pose-guided deformation to associate dynamic Gaussians across canonical and observation spaces; introduces physically-based prior with regularized transformations, pose refinement strategy for compensating inaccurate initial estimation, and split-with-scale mechanism to enhance point cloud density.
**Key findings**:
- Achieves state-of-the-art photorealistic novel-view rendering for dynamic clothed human bodies with high-quality details
- The pose-guided deformation successfully handles complicated non-rigid deformations in dynamic human reconstruction
- Enables explicit geometry reconstruction alongside high-quality rendering
- Pose refinement strategy effectively compensates for inaccurate initial pose estimation
- Split-with-scale mechanism improves the density and quality of regressed point clouds
**Limitations**: Applying static 3DGS to dynamic scenarios requires significant modifications; reconstruction quality depends on pose estimation accuracy, though the refinement strategy helps mitigate this issue.

### Lin (2024)

**Research question**: How can the training efficiency and performance of 3D Gaussian Splatting be improved to make it more practical for real-world applications?
**Methodology**: Conducts over 2000 experiments testing different components and dimensions of 3DGS to identify performance impacts; introduces integer compression (base 95) and floating-point compression (base 94) with ASCII encoding/decoding mechanisms, followed by systematic fine-tuning.
**Key findings**:
- Multiple dimensions and components of 3DGS significantly impact training efficiency and can be optimized independently
- Novel compression techniques (integer base-95 and floating-point base-94 with ASCII encoding) improve model performance
- Systematic fine-tuning across multiple dimensions yields excellent performance improvements over the original 3DGS
- The project code is released as open source for community use
**Limitations**: The extensive experimental approach may be difficult to reproduce fully; compression techniques may introduce trade-offs between quality and efficiency that are not fully explored.

### Pan et al. (2025)

**Research question**: How can 3D Gaussian Splatting be extended to enable strand-level hair geometry reconstruction from multi-view images while preserving connectivity and topology?
**Methodology**: Multi-stage pipeline that first reconstructs detailed hair geometry using a differentiable Gaussian rasterizer, then merges individual Gaussian segments into coherent strands through a novel merging scheme, and finally refines and grows strands under photometric supervision.
**Key findings**:
- Robustly handles a wide range of hairstyles on both synthetic and real-world datasets
- Achieves efficient reconstruction typically completing within one hour
- New evaluation metric proposed as proxy for assessing topological accuracy in strand reconstruction
- Addresses connectivity and topology of hair strands, which existing methods typically neglect
- Natural alignment between 3DGS explicit representations and hair strand structure
**Limitations**: Existing evaluation methods focus on geometric level rather than strand connectivity; new topological metric serves as proxy rather than direct measurement of strand accuracy.

### Ren et al. (2026)

**Research question**: How can self-supervised learning for 3D Gaussian Splatting create reusable representations that work consistently across different primitive realizations without requiring input-space reconstruction?
**Methodology**: Introduces Gaussian-JEPA that predicts representations of held-out Gaussian token blocks from visible context using an online encoder and a shared exponential-moving-average encoder that supplies stop-gradient features for multi-scale targets, with complementary target projections and feature-space grounding for latent supervision.
**Key findings**:
- More consistent across resampled inputs compared to matched reconstruction pretraining
- Retains more instance information under partial observations
- Provides stronger frozen features for Gaussian completion tasks
- Latent prediction proves effective as an objective for reusable 3D Gaussian representations
- Successfully transfers to part segmentation and object classification tasks
**Limitations**: Requires specific encoder architecture with exponential-moving-average components; evaluation limited to transfer learning on segmentation and classification without broader downstream task assessment.

### Vicente (2026)

**Research question**: How can 3D Gaussian Splatting achieve better balance between reconstruction fidelity and computational efficiency through low-level hardware optimization?
**Methodology**: High-performance C++/CUDA re-implementation within LichtFeld-Studio framework featuring Long-Axis-Split CUDA kernel, custom Laplacian-based importance kernels with Non-Maximum Suppression for edge scores, and adaptive Exponential Scale Scheduler to reduce host-device synchronization and training latency.
**Key findings**:
- 1M-budget variant achieves 26.8% reduction in training time, saving 17 minutes per session
- Uses 13.3% fewer Gaussians while maintaining superior visual quality compared to MCMC baseline
- Full variant demonstrates 1.28 dB PSNR increase over ADC baseline
- 38.4% reduction in parametric complexity achieved
- Establishes new Pareto-optimal front for scene reconstruction on Mip-NeRF360 dataset
**Limitations**: Implementation specific to LichtFeld-Studio framework limiting portability; evaluation conducted only on Mip-NeRF360 dataset without broader dataset validation.

### Wu et al. (2024)

**Research question**: How can we provide a comprehensive survey of 3D Gaussian Splatting methods to help both beginners and experienced researchers understand this rapidly evolving field?
**Methodology**: Literature review classifying 3DGS methods into three functional categories: 3D reconstruction, 3D editing, and downstream applications; also illustrates traditional point-based rendering methods and 3DGS rendering formulation for foundational understanding.
**Key findings**:
- 3DGS uses explicit Gaussian ellipsoids instead of neural implicit representations, enabling significantly faster rendering through rasterization
- The explicit representation facilitates editing tasks including dynamic reconstruction, geometry editing, and physical simulation
- The field is experiencing rapid growth with an increasing number of works across multiple application domains
- 3DGS achieves real-time novel view synthesis while maintaining photorealistic quality
**Limitations**: As a survey paper, it does not present new experimental results or propose novel methods; the rapidly evolving nature of the field means some recent works may not be covered.

## References

Bagdasarian, M. T., Knoll, P., Li, Y.-H., Barthel, F., Hilsmann, A., Eisert, P., & Morgenstern, W. (2024). 3DGS.zip: A survey on 3D Gaussian Splatting compression methods. arXiv. https://arxiv.org/abs/2407.09510

Ding, J., Song, M., Zhang, X., Jin, H., Jin, Y., & Si, X. (2026). ZeroSplat: Generalized referring segmentation in 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2607.18801

Jo, J., Lee, H., & Park, J. (2024). Identifying unnecessary 3D Gaussians using clustering for fast rendering of 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2402.13827

Lee, B., Lee, H., Sun, X., Ali, U., & Park, E. (2024). Deblurring 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2401.00834

Li, M., Yao, S., Xie, Z., & Chen, K. (2024). GaussianBody: Clothed human reconstruction via 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2401.09720

Lin, J. (2024). I3DGS: Improve 3D Gaussian Splatting from multiple dimensions. arXiv. https://arxiv.org/abs/2405.06408

Pan, Y., Nießner, M., & Kirschstein, T. (2025). HairGS: Hair strand reconstruction based on 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2509.07774

Ren, B., Ma, Q., Li, Y., Han, Z., Li, Y., Fu, Y., Anwer, R. M., Gevers, T., Khan, F. S., & Khan, S. (2026). Gaussian-JEPA: Joint-Embedding Predictive Learning for 3D Gaussian Splats. arXiv. https://arxiv.org/abs/2608.15651

Vicente, J. M. (2026). ImprovedGS+: A High-Performance C++/CUDA Re-Implementation Strategy for 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2603.08661

Wu, T., Yuan, Y.-J., Zhang, L.-X., Yang, J., Cao, Y.-P., Yan, L.-Q., & Gao, L. (2024). Recent Advances in 3D Gaussian Splatting. arXiv. https://arxiv.org/abs/2403.11134
