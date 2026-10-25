# Systematic Literature Review: Video Understanding with Multimodal Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "multimodal video", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in video understanding with multimodal models, surveying 10 arXiv papers from the cs.CV category published within the last two years. The surveyed literature reveals a field rapidly evolving toward more sophisticated integration of multiple modalities—visual content, audio transcripts, text descriptions, and temporal information—to enhance video comprehension. Three dominant research directions emerge: (1) synthetic data generation and training strategies to overcome annotation bottlenecks, (2) intelligent routing and sampling mechanisms to reduce computational overhead while maintaining performance, and (3) novel architectures for temporal grounding and anomaly detection. Collectively, these works demonstrate that multimodal approaches consistently outperform unimodal baselines, though challenges remain in modality imbalance, environmental robustness, and efficient evidence seeking. The field shows strong momentum toward practical, scalable solutions for real-world video understanding tasks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "multimodal video", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Synthetic Data Generation and Training Strategies

A prominent research direction addresses the fundamental challenge of obtaining high-quality annotated video data for training multimodal models. Rahman et al. (2026) introduce SynMulti, a unified synthetic data generation pipeline that automatically produces unlimited multimodal video data with rich supervision across multiple task formats. Their VQA-based fine-tuning strategy trains models to answer structured questions about visual content, enabling models trained predominantly on synthetic data to generalize effectively to real-world datasets—often outperforming traditionally trained counterparts. This theme reflects a broader recognition that synthetic data can provide a scalable alternative to expensive real-world annotation, particularly for complex multimodal tasks requiring expert annotators.

### Theme 2: Intelligent Routing and Computational Efficiency

Multiple works focus on reducing computational overhead while maintaining or improving retrieval and understanding performance. Dela Rosa (2025) presents ModaRoute, an LLM-based intelligent routing system that analyzes query intent and routes queries across ASR (speech), OCR (text), and visual indices, averaging only 1.78 modalities per query versus exhaustive 3.0 modality search—reducing computational overhead by 41% while achieving competitive Recall@5 scores. Similarly, Ma et al. (2025) propose Multimodal Mixup strategies that apply Mixup at the aggregated multimodal feature level to mitigate overfitting and modality imbalance, with their Balanced Multimodal Mixup dynamically adjusting mixing ratios based on modality contributions. Gao et al. (2026) introduce MoRoute, which uses dynamic layer routing to connect hierarchical multimodal representations from pretrained vision-language models to video diffusion transformers, enabling adaptive correspondence between multimodal understanding and video synthesis.

### Theme 3: Temporal Grounding and Frame Sampling

Effective temporal reasoning and frame selection emerge as critical challenges in video understanding. Wang et al. (2025) introduce VideoITG, a framework that adaptively customizes frame sampling strategies based on user instructions, using the VidThinker pipeline to automate annotation by generating instruction-conditioned captions and selecting key frames. Their VideoITG-40K dataset contains 40K videos with 500K temporal grounding annotations, enabling discriminative frame selection using Video-LLMs. This theme reflects the recognition that not all frames contribute equally to understanding, and instruction-aware sampling can significantly improve performance on multimodal video benchmarks.

### Theme 4: Script-Driven and Text-Guided Summarization

The integration of textual information—whether user-provided scripts or generated anomaly descriptions—provides explicit semantic guidance for video understanding tasks. Mylonas et al. (2025) present SD-MVSum, which extends script-driven video summarization by incorporating audio transcript relevance alongside visual content, using a weighted cross-modal attention mechanism that exploits semantic similarity between script-video and script-transcript pairs. Sun et al. (2026) leverage text modality for weakly supervised multimodal video anomaly detection, proposing an in-context learning-based text augmentation mechanism to generate high-quality anomaly text samples and a multi-scale bottleneck Transformer fusion module that progressively integrates information across modalities. Both works demonstrate that text provides explicit semantic information that can enhance characterization and reduce false alarms.

### Theme 5: Evidence Seeking and Misinformation Detection

A novel direction addresses video misinformation detection through active evidence acquisition rather than holistic processing. Zhao et al. (2026) propose SIEVE, a framework where an evidence-seeking agent actively explores multimodal evidence to construct a compact evidence package, which is then used by a verifier to determine veracity. The agent is trained using supervised evidence-seeking trajectories and an evidence-aware reinforcement learning objective. This approach supports reliable verification using compact evidence packages while providing an explicit and inspectable evidence trail, improving transparency and groundedness of multimodal misinformation detection.

### Theme 6: Long-Form Video Understanding and Prompt Engineering

Understanding long-form videos presents unique challenges due to the need for comprehensive content capture and subject-expert annotators. Jahagirdar et al. (2025) explore prompt engineering techniques using LLMs combined with ASR and OCR technologies to capture concise and informative content from entire videos in educational and news domains. Their work advocates for leveraging prompt engineering to comprehend long-form multimodal video datasets comprehensively, addressing the limitations of baseline approaches on extended video content.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively demonstrate that multimodal approaches consistently outperform unimodal baselines across diverse tasks—video object counting, VQA, segmentation, retrieval, and anomaly detection. Multiple works agree that intelligent mechanisms for selecting which modalities or frames to process (Dela Rosa, 2025; Wang et al., 2025; Zhao et al., 2026) can achieve comparable or superior performance to exhaustive processing while significantly reducing computational costs. There is also broad consensus that synthetic or augmented data generation (Rahman et al., 2026; Sun et al., 2026) can effectively supplement or replace expensive real-world annotations.

**Disagreements**: An interesting tension emerges regarding multimodal fusion strategies. While Sun et al. (2026) and Mylonas et al. (2025) demonstrate benefits from sophisticated cross-modal attention mechanisms that integrate multiple modalities, Ma et al. (2026) report that RGB-NIR fusion does not consistently outperform RGB-only input in palm presentation attack detection, revealing architecture-dependent behavior. Similarly, while Dela Rosa (2025) shows that intelligent routing can reduce modality usage by 41%, dense text captions alone can achieve 75.9% Recall@5 but require expensive offline processing—suggesting trade-offs between different efficiency strategies that remain unresolved.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Environmental Robustness**: Ma et al. (2026) reveal substantial architecture-dependent degradation under environmental shift in palm presentation attack detection, yet systematic evaluation of multimodal video models across diverse acquisition environments remains limited.

2. **Modality Imbalance Mechanisms**: While Ma et al. (2025) propose Balanced Multimodal Mixup to address modality imbalance, the fundamental mechanisms causing certain modalities to dominate learning remain under-explored across different task types.

3. **Long-Form Video Benchmarks**: Jahagirdar et al. (2025) note the challenge of obtaining subject-expert annotators for long-form videos, yet comprehensive benchmarks for educational and news video understanding remain scarce.

4. **Transparency in Evidence Seeking**: While Zhao et al. (2026) introduce inspectable evidence trails for misinformation detection, broader adoption of transparent, interpretable multimodal reasoning mechanisms is needed across the field.

5. **Cross-Domain Generalization**: Most papers evaluate on domain-specific benchmarks, but systematic studies of cross-domain generalization—whether models trained on one video domain (e.g., surveillance) transfer to others (e.g., educational content)—are notably absent.

## Per-Paper Annotations

### Dela Rosa (2025)

**Research question**: How can intelligent routing reduce computational overhead in multimodal video retrieval while maintaining competitive effectiveness?

**Methodology**: The author introduces ModaRoute, an LLM-based intelligent routing system that uses GPT-4.1 to analyze query intent and route queries across ASR (speech), OCR (text), and visual indices, averaging 1.78 modalities per query versus exhaustive 3.0 modality search.

**Key findings**:
- ModaRoute reduces computational overhead by 41% while achieving 60.9% Recall@5
- Dense text captions can achieve 75.9% Recall@5 but require expensive offline processing
- 34% of clips contain scene text not captured by ASR
- Intelligent routing provides a practical solution for scaling multimodal retrieval systems

**Limitations**: Not stated in abstract

### Gao et al. (2026)

**Research question**: How can hierarchical multimodal representations from a pretrained vision-language model be effectively connected to a pretrained video diffusion transformer for unified multimodal video generation?

**Methodology**: The authors propose MoRoute, a framework that formulates a frozen VLM and pretrained video DiT as heterogeneous experts connected through dynamic layer routing, where a lightweight block-wise router enables each DiT block to select the most relevant VLM layer for its generation stage.

**Key findings**:
- MoRoute enables adaptive correspondence between multimodal understanding and video synthesis through dynamic layer routing
- The framework incorporates reference images and source videos directly into the DiT token sequence through unified in-context conditioning
- MoRoute outperforms the best competing method on IntelligentVBench, OpenVE-Bench, and RefVIE-Bench
- Average score improvements of 0.15, 0.18, and 0.34 on a 1-5 scale were achieved on the three benchmarks respectively

**Limitations**: Not stated in abstract

### Jahagirdar et al. (2025)

**Research question**: How can prompt engineering techniques be leveraged to comprehend long-form multimodal video datasets in educational and news domains?

**Methodology**: The authors introduce a dataset of long-form lectures and news videos, present baseline approaches to understand their limitations, and advocate for exploring prompt engineering techniques using LLMs combined with ASR and OCR technologies to capture content from entire videos.

**Key findings**:
- Long-form video understanding is challenging due to the need for subject-expert annotators
- LLMs combined with ASR and OCR technologies can capture concise and informative content from entire videos
- Baseline approaches have limitations on long-form multimodal video datasets
- Prompt engineering techniques show promise for comprehending long-form multimodal video datasets comprehensively

**Limitations**: Not stated in abstract

### Ma et al. (2025)

**Research question**: How can multimodal mixup strategies address the problem of modality imbalance and overfitting in multimodal video understanding models?

**Methodology**: The authors propose Multimodal Mixup (MM) which applies Mixup strategy at the aggregated multimodal feature level, and Balanced Multimodal Mixup (B-MM) which dynamically adjusts mixing ratios for each modality based on their relative contributions to the learning objective.

**Key findings**:
- Multimodal models are prone to overfitting strong modalities that can dominate learning and suppress weaker modalities
- Multimodal Mixup (MM) applies Mixup at the aggregated multimodal feature level to generate virtual feature-label pairs and mitigate overfitting
- Balanced Multimodal Mixup (B-MM) dynamically adjusts mixing ratios based on modality contributions
- Extensive experiments demonstrate effectiveness in improving generalization and multimodal robustness across several datasets

**Limitations**: Not stated in abstract

### Ma et al. (2026)

**Research question**: How can a large-scale multimodal video dataset enable systematic evaluation of palm presentation attack detection across environments, modalities, and attack types?

**Methodology**: The authors present GBU-Palm, a large-scale multimodal video dataset with 21,326 videos from 105 subjects across six acquisition environments, construct leakage-controlled protocols separating palm identity and attack lineage, and benchmark four video architectures under environment-matched and held-out settings with detailed model behavior analysis.

**Key findings**:
- GBU-Palm contains 21,326 videos from 105 subjects and 210 palms across six acquisition environments with 6,310 synchronized RGB-NIR samples
- Leakage-controlled protocols separate palm identity and attack lineage for systematic evaluation
- Results reveal substantial architecture-dependent degradation under environmental shift
- RGB-NIR fusion does not consistently outperform RGB-only input
- Detailed analysis through TA/TR/FA/FR decomposition, spectral masking, temporal-order intervention, and frozen-backbone NIR probing reveals distinct failure patterns across architectures

**Limitations**: Not stated in abstract

### Mylonas et al. (2025)

**Research question**: How can script-driven multimodal video summarization leverage both visual content and audio transcripts to identify video segments most relevant to a user-provided script?

**Methodology**: The authors present SD-MVSum, which extends their earlier SD-VSum method by incorporating audio transcript relevance alongside visual content, using a new weighted cross-modal attention mechanism that exploits semantic similarity between script-video and script-transcript pairs.

**Key findings**:
- SD-MVSum considers both visual modality and the relevance of user-provided scripts with spoken content (audio transcripts)
- A new weighted cross-modal attention mechanism models dependence between script-video and script-transcript pairs
- The mechanism promotes video parts with highest relevance to the user-provided script
- Two large-scale datasets (S-VideoXum and MrHiSum) were extended for script-driven multimodal video summarization
- SD-MVSum demonstrates competitiveness against state-of-the-art approaches for script-driven and generic video summarization

**Limitations**: Not stated in abstract

### Rahman et al. (2026)

**Research question**: How can synthetic data generation pipelines provide a scalable alternative to expensive real-world annotation for training multimodal video understanding models?

**Methodology**: The authors propose SynMulti, a unified synthetic data generation pipeline that automatically produces unlimited multimodal video data with rich supervision across multiple task formats. They introduce a VQA-based fine-tuning strategy that trains models to answer structured questions about visual content to enhance reasoning ability.

**Key findings**:
- SynMulti provides a unified synthetic data generation pipeline capable of automatically producing unlimited multimodal video data with diverse supervision
- The VQA-based fine-tuning strategy encourages deeper visual grounding and reasoning by training models to answer structured questions about visual content
- Models trained predominantly on synthetic data generalize effectively to real-world datasets
- Synthetic-trained models often outperform traditionally trained counterparts across video object counting, video-based VQA, and video object segmentation tasks

**Limitations**: Not stated in abstract

### Sun et al. (2026)

**Research question**: How can the under-explored text modality be leveraged to enhance weakly supervised multimodal video anomaly detection?

**Methodology**: The authors propose a text-guided framework featuring an in-context learning-based multi-stage text augmentation mechanism to generate high-quality anomaly text samples, and a multi-scale bottleneck Transformer fusion module that uses compressed bottleneck tokens to progressively integrate information across modalities.

**Key findings**:
- Text provides explicit semantic information that can enhance anomaly characterization and reduce false alarms
- The proposed text augmentation mechanism generates high-quality anomaly text samples for fine-tuning the text feature extractor
- The bottleneck Transformer fusion module mitigates redundancy and imbalance in multimodal fusion
- The framework demonstrates state-of-the-art performance on UCF-Crime and XD-Violence benchmarks

**Limitations**: Not stated in abstract

### Wang et al. (2025)

**Research question**: How can frame sampling strategies be adaptively customized based on user instructions to improve multimodal video understanding and temporal reasoning?

**Methodology**: The authors introduce VideoITG, a framework that uses the VidThinker pipeline to automate annotation by generating instruction-conditioned captions, retrieving relevant video segments, and selecting key frames, building a 40K video dataset with 500K temporal grounding annotations to enable discriminative frame selection using Video-LLMs.

**Key findings**:
- VideoITG adaptively customizes frame sampling strategies based on user instructions
- The VidThinker pipeline enables efficient supervision through automated annotation
- The VideoITG-40K dataset contains 40K videos and 500K temporal grounding annotations
- VideoITG consistently boosts performance on multiple multimodal video understanding benchmarks

**Limitations**: Not stated in abstract

### Zhao et al. (2026)

**Research question**: Can decoupling evidence acquisition from verification improve multimodal video misinformation detection by identifying sparse, decision-relevant clues rather than processing entire videos holistically?

**Methodology**: The authors propose SIEVE, a framework where an evidence-seeking agent actively explores multimodal evidence to construct a compact evidence package, which is then used by a verifier to determine veracity, with the agent trained using supervised evidence-seeking trajectories and an evidence-aware reinforcement learning objective.

**Key findings**:
- SIEVE consistently outperforms evaluated baselines on multiple video misinformation benchmarks
- The framework supports reliable verification using compact evidence packages
- The acquisition process provides an explicit and inspectable evidence trail
- The approach improves transparency and groundedness of multimodal misinformation detection

**Limitations**: Not stated in abstract

## References

Dela Rosa, K. (2025). Smart routing for multimodal video retrieval: When to search what. arXiv. https://arxiv.org/abs/2507.13374

Gao, C., Ma, J., Peng, Z., Wang, C., Wu, H., Liang, J., Li, G., & Li, J. (2026). MoRoute: Dynamic routing for in-context multimodal video generation. arXiv. https://arxiv.org/abs/2607.29545

Jahagirdar, S. S., Saha, J., & Jawahar, C. V. (2025). Prompt2LVideos: Exploring prompts for understanding long-form multimodal videos. arXiv. https://arxiv.org/abs/2503.08335

Ma, X., Ding, D., & Chen, H. (2025). Mixup helps understanding multimodal video better. arXiv. https://arxiv.org/abs/2510.10986

Ma, Y., Yu, Z., Jia, W., Kumar, A., & Shen, L. (2026). GBU-Palm: A multimodal video dataset and benchmark for palm presentation attack detection. arXiv. https://arxiv.org/abs/2608.14389

Mylonas, M., Zerva, C., Apostolidis, E., & Mezaris, V. (2025). SD-MVSum: Script-driven multimodal video summarization method and datasets. arXiv. https://arxiv.org/abs/2510.05652

Rahman, T., Liao, R., & Sigal, L. (2026). SynMulti: Synthetic-to-real learning for multimodal video understanding. arXiv. https://arxiv.org/abs/2604.12335

Sun, S., Hua, J., Feng, J., & Gong, X. (2026). Enhancing weakly supervised multimodal video anomaly detection through text guidance. arXiv. https://arxiv.org/abs/2602.10549

Wang, S., Chen, G., Huang, D.-a., Li, Z., Li, M., Liu, G., Alvarez, J. M., Zhang, L., & Yu, Z. (2025). VideoITG: Multimodal video understanding with instructed temporal grounding. arXiv. https://arxiv.org/abs/2507.13353

Zhao, H., Xu, Y., Lin, X., Xie, D., Lu, J., Qian, Y., Wang, Y., Xu, H., & Gou, G. (2026). Sparse evidence can suffice: Agentic evidence seeking for multimodal video misinformation detection. arXiv. https://arxiv.org/abs/2607.18080
