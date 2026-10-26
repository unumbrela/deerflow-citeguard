# Systematic Literature Review: Towards Open World Detection

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "open world detection", filtered to category cs.CV, published between 2023-08-22 and 2025-08-22
**Citation format**: APA 7th edition

## Executive Summary

The field of open world detection has evolved significantly between 2023 and 2025, moving from isolated detection frameworks toward unified, language-guided systems capable of handling unknown objects without predefined vocabulary constraints. The surveyed literature reveals a convergence around three major directions: (1) leveraging vision-language models for automatic annotation and captioning, (2) developing prompt-free detection mechanisms that can identify "anything" in images, and (3) creating scalable data engines for continuous self-improvement. Recent work demonstrates that synthetic captions from VLMs can eliminate the need for expensive manual annotation while maintaining or improving detection performance. The field is increasingly focused on practical applications in autonomous driving, aerial imagery, and traffic video analytics, with systems achieving state-of-the-art performance across multiple benchmarks including COCO, LVIS, and domain-specific datasets.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "open world detection", filtered to category cs.CV, published between 2023-08-22 and 2025-08-22. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Vision-Language Model Integration for Automatic Annotation

A dominant trend across the surveyed literature is the integration of vision-language models (VLMs) to enable automatic annotation and reduce dependency on manual labeling. Multiple papers leverage pre-trained VLMs to generate synthetic captions that enrich training data without human intervention. Kong et al. (2024) proposed bootstrapping dense synthetic captions using pre-trained VLMs to provide rich descriptions on different image regions, incorporating these captions to train their HyperLearner detector. Their hyperbolic vision-language learning approach imposes a hierarchy between visual and caption embeddings to mitigate hallucination noise in synthetic captions, achieving consistent improvements over GLIP, GLIPv2, and Grounding DINO.

This theme extends to automated data engines that operate iteratively for continuous self-improvement. Liang et al. (2024) introduced AIDE, which automatically identifies issues, curates data, improves models through auto-labeling, and verifies models through generation of diverse scenarios using vision-language and large language models. Similarly, Wei et al. (2025) presented the OS-W2S Label Engine, centered around an open-source large vision-language model, integrating image-operation-based preprocessing with BERT-based postprocessing to construct MI-OAD, a dataset approximately 40 times larger than comparable remote sensing grounding datasets.

The automation trend reaches its apex in video annotation pipelines. Rocky and Wu (2025) developed SAM2Auto, combining SMART-OD (a robust object detection system using automatic mask generation with open-world object detection) and FLASH (a multi-object real-time video instance segmentation handler) to achieve comparable accuracy to manual annotation while dramatically reducing annotation time and eliminating labor costs.

### Theme 2: Prompt-Free and Universal Object Detection

A second major direction focuses on developing detection systems that operate without user-provided prompts, enabling truly open-world capabilities. Ren et al. (2024) achieved a significant breakthrough with DINO-X, which supports prompt-free open-world detection through a universal object prompt that can detect anything in an image without user input. Their model integrates multiple perception heads to simultaneously support detection, segmentation, pose estimation, object captioning, and object-based QA tasks, achieving 56.0 AP on COCO and 59.8 AP on LVIS-minival zero-shot object detection benchmarks.

This universal detection paradigm is further advanced by Guan et al. (2025) with Prompt-DINO, which introduces an early fusion mechanism unifying text/visual prompts and backbone features at initial encoding, along with order-aligned query selection for DETR-based architectures. Their generative data engine powered by the RAP model synthesizes 0.5B diverse training instances through dual-path cross-verification, reducing label noise by 80.5% compared to conventional approaches and achieving state-of-the-art performance on open-world detection benchmarks.

The conceptual unification of detection approaches reaches its most comprehensive expression in the survey by Bulzan and Cernazanu-Glavan (2025), who propose Open World Detection (OWD) as an umbrella term to unify class-agnostic and generally applicable detection models. They trace the historical development from early saliency detection to modern open world object detection and Vision Large Language Models, identifying convergence patterns across multiple vision subdomains including saliency detection, foreground/background separation, out of distribution detection, zero-shot detection, and VLLMs.

### Theme 3: Geometric and Structural Approaches to Unknown Object Identification

Beyond appearance-based features, several papers explore geometric cues and structural approaches to improve unknown object detection. Yavuz and Güney (2024) proposed grouping known classes into superclasses and identifying unknown classes through an odd-one-out scoring mechanism inspired by human cognition studies. This approach leverages geometric cues in addition to appearance-based features, achieving significant improvements in unknown recall consistently across all tasks without compromising known class performance. Their method demonstrates that better partitioning of the feature space with superclasses prevents the confusion for known classes that noisy pseudo-labels typically introduce.

This structural thinking extends to feature alignment schemes in semi-supervised settings. Mullappilly et al. (2024) introduced SS-OWFormer, utilizing a feature-alignment scheme to better align object query representations between original and augmented images, plus a pseudo-labeling scheme for unknown detection that exploits decoder object queries' capability to capture object-specific information. Their experiments on 4 datasets (MS COCO, PASCAL, Objects365, and DOTA) demonstrate that the approach effectively leverages large unlabeled and few labeled data, though they note that state-of-the-art OWOD detector performance dramatically deteriorates in the semi-supervised setting.

### Theme 4: Domain-Specific Applications and Benchmarks

The surveyed literature demonstrates strong application-driven research across specific domains, particularly autonomous driving, aerial imagery, and traffic video analytics. Liang et al. (2024) established a benchmark for open-world detection on AV datasets to comprehensively evaluate various learning paradigms, addressing the long-tailed distribution problem where rare or unseen object categories pose challenges to deployed perception models. Their AIDE system demonstrates superior performance at reduced cost compared to traditional manual curation and annotation approaches.

In the aerial imagery domain, Wei et al. (2025) constructed MI-OAD with 163,023 images and 2 million image-caption pairs to move beyond vocabulary-level descriptions and meet fine-grained open-world detection demands. Training on MI-OAD lifts Grounding DINO by +31.1 AP50 and +34.7 Recall@10 with sentence-level inputs under zero-shot transfer, yielding state-of-the-art performance on multiple existing open-vocabulary aerial detection and remote sensing visual grounding benchmarks.

Traffic video analytics receives dedicated attention from Yu et al. (2025), who built LAVA, a system accepting natural language queries to retrieve traffic targets across multiple granularity levels. Their video-specific open-world detection module enables flexible querying at arbitrary categories and multiple levels of granularity, overcoming SQL-based constraints. LAVA improves F1-scores for selection queries by 14% compared to baselines, reduces MPAE for aggregation queries by 0.39, achieves top-k precision of 86%, and processes videos 9.6× faster than the most accurate baseline.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong consensus on several key points. First, all papers agree that traditional fixed-vocabulary detection approaches are insufficient for open-world scenarios, necessitating either language-guided systems or prompt-free universal detectors. Second, there is convergence around the value of synthetic or automatically generated annotations—multiple papers (Kong et al., 2024; Liang et al., 2024; Wei et al., 2025; Rocky & Wu, 2025) demonstrate that VLM-generated captions and automatic annotation pipelines can match or exceed manual annotation quality while dramatically reducing costs. Third, there is agreement that geometric cues and structural approaches complement appearance-based features for unknown object identification (Yavuz & Güney, 2024; Mullappilly et al., 2024).

**Disagreements**: The literature reveals tensions around semi-supervised approaches. While Mullappilly et al. (2024) propose semi-supervised open-world detection to reduce annotation costs, they acknowledge that state-of-the-art OWOD detector performance dramatically deteriorates in this setting, suggesting fundamental challenges that remain unresolved. Additionally, there is a methodological divide between papers emphasizing comprehensive unification (Bulzan & Cernazanu-Glavan, 2025; Ren et al., 2024) versus those focusing on domain-specific optimizations (Yu et al., 2025; Wei et al., 2025), with different assumptions about whether general-purpose or specialized systems will dominate future deployments.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly address computational efficiency or real-time deployment constraints, despite the practical applications in autonomous driving and traffic analytics suggesting this is a critical concern. Second, while multiple papers mention mitigating hallucination noise in synthetic captions (Kong et al., 2024) or reducing label noise (Guan et al., 2025), none provide comprehensive analysis of failure modes or systematic error characterization in automatic annotation pipelines.

Third, the semi-supervised setting remains underexplored despite its practical importance—Mullappilly et al. (2024) note performance deterioration but do not offer a complete solution. Fourth, there is limited discussion of ethical considerations, bias propagation from VLMs to detection systems, or privacy implications of universal detection capabilities that can identify "anything" without user prompts.

Finally, while Bulzan and Cernazanu-Glavan (2025) propose OWD as a unifying framework, the surveyed literature lacks systematic comparison studies that evaluate different approaches (hyperbolic learning, geometric cues, early fusion, universal prompts) on common benchmarks to determine which techniques provide complementary versus redundant benefits.

## Per-Paper Annotations

### Bulzan and Cernazanu-Glavan (2025)

**Research question**: How can various class-agnostic and generally applicable detection models in computer vision be unified under a single framework?
**Methodology**: This paper conducts a comprehensive survey tracing the historical development of foundational vision subdomains from early saliency detection to modern open world object detection and Vision Large Language Models. The authors analyze key concepts, methodologies, and datasets across these subdomains to identify convergence patterns.
**Key findings**:
- The paper proposes Open World Detection (OWD) as an umbrella term to unify class-agnostic and generally applicable detection models in the vision domain.
- Multiple vision subdomains including saliency detection, foreground/background separation, out of distribution detection, open world object detection, zero-shot detection, and VLLMs show increasing convergence.
- These subdomains have the potential to unify into a singular perception domain in the future.
**Limitations**: Not stated in abstract.

### Guan et al. (2025)

**Research question**: How can late-stage feature fusion and suboptimal query selection limitations in multimodal vision models be addressed for open-world segmentation?
**Methodology**: The authors propose Prompt-DINO, a text-guided visual Prompt DINO framework with three innovations: an early fusion mechanism unifying text/visual prompts and backbone features at initial encoding, order-aligned query selection for DETR-based architectures optimizing structural alignment between text and visual queries, and a generative data engine powered by the RAP model synthesizing 0.5B diverse training instances through dual-path cross-verification.
**Key findings**:
- Early fusion mechanism enables deeper cross-modal interactions that resolve semantic ambiguities.
- Order-aligned query selection enhances semantic-spatial consistency during decoding.
- The generative data engine reduces label noise by 80.5% compared to conventional approaches.
- Prompt-DINO achieves state-of-the-art performance on open-world detection benchmarks.
- The framework significantly expands semantic coverage beyond fixed-vocabulary constraints.
**Limitations**: Not stated in abstract.

### Kong et al. (2024)

**Research question**: How can open-world detection be improved by transferring knowledge from vision-language models to enrich open-vocabulary descriptions automatically?
**Methodology**: The authors propose bootstrapping dense synthetic captions using pre-trained VLMs to provide rich descriptions on different image regions, and incorporate these captions to train a novel detector called HyperLearner. They introduce a hyperbolic vision-language learning approach to impose a hierarchy between visual and caption embeddings to mitigate hallucination noise in synthetic captions.
**Key findings**:
- The proposed HyperLearner detector consistently outperforms existing state-of-the-art methods including GLIP, GLIPv2, and Grounding DINO when using the same backbone.
- Using synthetic captions from VLMs eliminates the need for expensive large-scale manually annotated caption datasets.
- The hyperbolic learning approach effectively mitigates noise caused by hallucination in synthetic captions.
- The model generalizes well to novel concepts across multiple benchmarks including COCO, LVIS, Object Detection in the Wild, and RefCOCO.
**Limitations**: Not stated in abstract.

### Liang et al. (2024)

**Research question**: How can recent advances in vision-language and large language models be leveraged to automatically improve object detection models for autonomous driving?
**Methodology**: The authors propose AIDE (Automatic Data Engine), a system that automatically identifies issues, efficiently curates data, improves the model through auto-labeling, and verifies the model through generation of diverse scenarios using vision-language and large language models. The process operates iteratively for continuous self-improvement.
**Key findings**:
- AIDE enables continuous self-improvement of perception models through an iterative automatic process.
- The method demonstrates superior performance at reduced cost compared to traditional manual curation and annotation approaches.
- The system addresses the long-tailed distribution problem where rare or unseen object categories pose challenges to deployed perception models.
- A benchmark for open-world detection on AV datasets was established to comprehensively evaluate various learning paradigms.
**Limitations**: Not stated in abstract.

### Mullappilly et al. (2024)

**Research question**: How can open-world object detection be formulated to reduce reliance on human oracles during incremental learning stages while maintaining detection performance?
**Methodology**: The authors introduce a semi-supervised open-world detection (SS-OWOD) formulation that casts incremental learning stages in a semi-supervised manner to reduce annotation costs. They propose SS-OWFormer, a novel detector utilizing a feature-alignment scheme to better align object query representations between original and augmented images, plus a pseudo-labeling scheme for unknown detection that exploits decoder object queries' capability to capture object-specific information.
**Key findings**:
- State-of-the-art OWOD detector performance dramatically deteriorates in the proposed SS-OWOD setting.
- SS-OWFormer's feature-alignment scheme effectively leverages large unlabeled and few labeled data.
- The pseudo-labeling scheme successfully exploits decoder object queries for unknown detection.
- Experiments on 4 datasets (MS COCO, PASCAL, Objects365, and DOTA) demonstrate the effectiveness of the SS-OWOD approach.
- The approach is effective for remote sensing object detection with carefully curated splits and baseline performance evaluations.
**Limitations**: Not stated in abstract.

### Ren et al. (2024)

**Research question**: How can a unified vision model achieve superior open-world object detection and understanding across multiple perception tasks without requiring user-provided prompts?
**Methodology**: The authors developed DINO-X, a unified object-centric vision model using a Transformer-based encoder-decoder architecture that supports text, visual, and customized prompts, including a universal object prompt for prompt-free detection. They constructed Grounding-100M, a large-scale dataset with over 100 million grounding samples, to pre-train the model for enhanced open-vocabulary detection and integrated multiple perception heads for simultaneous task support.
**Key findings**:
- DINO-X achieves 56.0 AP on COCO, 59.8 AP on LVIS-minival, and 52.4 AP on LVIS-val zero-shot object detection benchmarks.
- The model scores 63.3 AP on rare classes of LVIS-minival and 56.5 AP on LVIS-val, improving previous SOTA by 5.8 AP and 5.0 AP respectively.
- DINO-X supports prompt-free open-world detection through a universal object prompt that can detect anything in an image without user input.
- The model integrates multiple perception heads to simultaneously support detection, segmentation, pose estimation, object captioning, and object-based QA tasks.
- Pre-training on the Grounding-100M dataset with over 100 million samples enables foundational object-level representation for open-vocabulary detection.
**Limitations**: Not stated in abstract.

### Rocky and Wu (2025)

**Research question**: How can automated video annotation pipelines address the scarcity of annotated datasets for Vision-Language Models without requiring human intervention or dataset-specific training?
**Methodology**: The authors introduce SAM2Auto, a fully automated annotation pipeline combining SMART-OD (a robust object detection system using automatic mask generation with open-world object detection) and FLASH (a multi-object real-time video instance segmentation handler that maintains consistent object identification across frames). The system employs statistical approaches to minimize detection errors and ensure consistent object tracking throughout video sequences.
**Key findings**:
- SAM2Auto achieves comparable accuracy to manual annotation while dramatically reducing annotation time and eliminating labor costs.
- The system successfully handles diverse datasets without requiring retraining or extensive parameter adjustments.
- SMART-OD overcomes limitations of existing open-world detection methods that require frame-specific hyperparameter tuning and suffer from numerous false positives.
- FLASH maintains consistent object identification across video frames even with intermittent detection gaps.
- The work establishes a new baseline for automated video annotation and provides a pathway for accelerating VLM development.
**Limitations**: Not stated in abstract.

### Wei et al. (2025)

**Research question**: How can large-scale language-guided open-set aerial detection datasets be constructed to move beyond vocabulary-level descriptions and meet fine-grained open-world detection demands?
**Methodology**: The authors present the OS-W2S Label Engine, an automatic annotation pipeline centered around an open-source large vision-language model, integrating image-operation-based preprocessing with BERT-based postprocessing. The engine handles diverse scene annotations across three levels of language guidance (words, phrases, sentences). Using this engine, they constructed MI-OAD, a novel benchmark dataset with 163,023 images and 2 million image-caption pairs.
**Key findings**:
- MI-OAD is approximately 40 times larger than comparable remote sensing grounding datasets.
- Training on MI-OAD lifts Grounding DINO by +31.1 AP50 and +34.7 Recall@10 with sentence-level inputs under zero-shot transfer.
- Using MI-OAD for pre-training yields state-of-the-art performance on multiple existing open-vocabulary aerial detection and remote sensing visual grounding benchmarks.
- The OS-W2S annotations are validated as high quality through effectiveness on three representative tasks.
- The dataset addresses limitations of current remote sensing grounding data and enables effective language-guided open-set aerial detection.
**Limitations**: Not stated in abstract.

### Yavuz and Güney (2024)

**Research question**: How can geometric cues and class grouping strategies improve unknown object detection without compromising known class performance in open-world settings?
**Methodology**: The authors propose grouping known classes into superclasses and identifying unknown classes through an odd-one-out scoring mechanism inspired by human cognition studies. This approach leverages geometric cues in addition to appearance-based features and achieves better partitioning of the feature space.
**Key findings**:
- Geometric cues improve unknown recall in open-world object detection.
- Grouping known classes into superclasses enables identification of unknown objects through an odd-one-out scoring mechanism.
- The approach achieves significant improvements in unknown recall consistently across all tasks without compromising known class performance.
- Better partitioning of the feature space with superclasses prevents the confusion for known classes that noisy pseudo-labels typically introduce.
**Limitations**: Not stated in abstract.

### Yu et al. (2025)

**Research question**: How can language-driven video analytics enable flexible and efficient querying of high-volume traffic video data beyond the constraints of rigid SQL-based paradigms?
**Methodology**: The authors build LAVA, a system accepting natural language queries to retrieve traffic targets across multiple granularity levels. It comprises three components: (1) a multi-armed bandit-based efficient sampling method for video segment-level localization, (2) a video-specific open-world detection module for object-level retrieval, and (3) a long-term object trajectory extraction scheme for temporal object association. A novel benchmark with diverse natural language predicates and fine-grained annotations was developed for evaluation.
**Key findings**:
- LAVA improves F1-scores for selection queries by 14% compared to baselines.
- The system reduces MPAE for aggregation queries by 0.39.
- LAVA achieves top-k precision of 86%.
- Videos are processed 9.6× faster than the most accurate baseline.
- The language-driven paradigm enables flexible querying at arbitrary categories and multiple levels of granularity, overcoming SQL-based constraints.
**Limitations**: Not stated in abstract.

## References

Bulzan, A.-S., & Cernazanu-Glavan, C. (2025). Towards open world detection: A survey. arXiv. https://arxiv.org/abs/2508.16527

Guan, Y., Sun, C., Fu, C., Huang, Z., Yuan, C., & Li, C. (2025). Text-guided visual prompt DINO for generic segmentation. arXiv. https://arxiv.org/abs/2508.06146

Kong, F., Chen, Y., Cai, J., & Modolo, D. (2024). Hyperbolic learning with synthetic captions for open-world detection. arXiv. https://arxiv.org/abs/2404.05016

Liang, M., Su, J.-C., Schulter, S., Garg, S., Zhao, S., Wu, Y., & Chandraker, M. (2024). AIDE: An automatic data engine for object detection in autonomous driving. arXiv. https://arxiv.org/abs/2403.17373

Mullappilly, S. S., Gehlot, A. S., Anwer, R. M., Khan, F. S., & Cholakkal, H. (2024). Semi-supervised open-world object detection. arXiv. https://arxiv.org/abs/2402.16013

Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., & Zhang, L. (2024). DINO-X: A unified vision model for open-world object detection and understanding. arXiv. https://arxiv.org/abs/2411.14347

Rocky, A., & Wu, Q. M. J. (2025). SAM2Auto: Auto annotation using FLASH. arXiv. https://arxiv.org/abs/2506.07850

Wei, G., Liu, Y., Yuan, X., Xue, X., Guo, L., Yang, Y., Zhao, C., Bai, Z., Zhang, H., & Xiao, R. (2025). OS-W2S: An automatic labeling engine for language-guided open-set aerial object detection. arXiv. https://arxiv.org/abs/2505.03334

Yavuz, M., & Güney, F. (2024). O1O: Grouping of known classes to identify unknown objects as odd-one-out. arXiv. https://arxiv.org/abs/2410.07514

Yu, Y., Zhou, T., Sun, J., Qiao, L., Ding, L., Yuan, Y., & Wang, G. (2025). LAVA: Language driven scalable and versatile traffic video analytics. arXiv. https://arxiv.org/abs/2507.19821
