# Systematic Literature Review: Video Understanding with Multimodal Models

**Topic:** Video Understanding with Multimodal Models  
**Search Category:** cs.CV  
**Time Period:** 2024-2026 (last 2 years)  
**Number of Papers:** 10  
**Citation Format:** APA 7th Edition  
**Date:** October 25, 2026

---

## Executive Summary

This systematic literature review examines recent advances in video understanding with multimodal models, analyzing 10 papers published between 2024 and 2026 in the cs.CV category. The review reveals a field rapidly evolving around several critical challenges: data scarcity and annotation costs, modality imbalance and fusion strategies, temporal understanding gaps, and the need for efficient routing and evidence-seeking mechanisms. Key findings indicate that synthetic data generation can match or exceed real-world annotation quality, state-of-the-art models achieve only 38.5% accuracy on fine-grained temporal tasks (revealing a ~30% human-AI gap), and intelligent routing can reduce computational overhead by 41% while maintaining competitive performance. The literature demonstrates growing sophistication in handling multimodal integration, with emerging focus on sparse evidence utilization, dynamic modality selection, and cross-environment robustness.

---

## Thematic Analysis

### Theme 1: Data Generation and Annotation Efficiency

A prominent theme across the literature is addressing the fundamental challenge of data scarcity and annotation costs in multimodal video understanding.

**SynMulti** (Rahman et al., 2026) introduces a unified synthetic data generation pipeline capable of producing unlimited multimodal video data with rich supervision across multiple tasks (object counting, VQA, segmentation). The key innovation is a VQA-based fine-tuning strategy that trains models to answer structured questions about visual content rather than relying solely on captions, encouraging deeper visual grounding and reasoning. Models trained predominantly on synthetic data generalize effectively to real-world datasets, often outperforming traditionally trained counterparts.

**GBU-Palm** (Ma et al., 2026) addresses the opposite end of the data spectrum, presenting a large-scale real-world multimodal video dataset containing 21,326 videos from 105 subjects across six acquisition environments. The dataset features leakage-controlled protocols and synchronized RGB-NIR samples, revealing that RGB-NIR fusion does not consistently outperform RGB-only input—a counterintuitive finding that challenges assumptions about multimodal fusion benefits.

**Prompt2LVideos** (Jahagirdar et al., 2025) tackles long-form video understanding in educational and news domains, where manual annotation by subject experts is prohibitively expensive. The work leverages LLMs combined with ASR and OCR technologies to automatically extract and comprehend content from videos lasting minutes to hours, demonstrating that automated solutions can significantly reduce dependency on expert annotators.

**Convergence:** All three works recognize that data collection and annotation represent fundamental bottlenecks, but propose divergent solutions: synthetic generation, comprehensive real-world benchmarks, and automated extraction from existing content.

### Theme 2: Modality Fusion and Balance

Multiple papers address the challenge of effectively integrating information across modalities without allowing dominant modalities to suppress weaker ones.

**Mixup Helps Understanding Multimodal Video Better** (Ma et al., 2025) identifies that multimodal models are prone to overfitting strong modalities, which can dominate learning and suppress contributions from weaker modalities. The authors propose Multimodal Mixup (MM), applying Mixup strategy at the aggregated multimodal feature level, and Balanced Multimodal Mixup (B-MM), which dynamically adjusts mixing ratios for each modality based on their relative contributions to the learning objective. This work directly addresses modality imbalance—a recurring challenge across the literature.

**SD-MVSum** (Mylonas et al., 2025) extends script-driven video summarization by incorporating both visual and audio modalities through a weighted cross-modal attention mechanism. The method explicitly models semantic similarity between script-video and script-transcript pairs, promoting video segments with highest relevance to user-provided scripts. This represents a more sophisticated approach to multimodal fusion than simple concatenation or early fusion.

**Enhancing Weakly Supervised Multimodal Video Anomaly Detection** (Sun et al., 2026) addresses redundancy and imbalance in multimodal fusion through a multi-scale bottleneck Transformer fusion module that uses compressed bottleneck tokens to progressively integrate information across modalities. The work also introduces an in-context learning-based multi-stage text augmentation mechanism to generate high-quality anomaly text samples, addressing the scarcity of relevant descriptions.

**Convergence:** These works converge on the insight that naive multimodal fusion is insufficient—explicit mechanisms for balancing modality contributions, managing redundancy, and modeling cross-modal relationships are essential for robust performance.

### Theme 3: Temporal Understanding and Reasoning Gaps

A critical finding across the literature is the substantial gap between human and AI capabilities in temporal understanding.

**TemporalBench** (Cai et al., 2024) provides the most stark evidence of this gap, introducing a benchmark with ~10K video question-answer pairs derived from ~2K high-quality human annotations detailing temporal dynamics. State-of-the-art models like GPT-4o achieve only 38.5% question answering accuracy on TemporalBench, demonstrating a ~30% gap between humans and AI in temporal understanding. The work also identifies a critical evaluation pitfall: in multi-choice QA, LLMs can detect subtle changes in negative captions and find centralized descriptions as cues for prediction, leading the authors to propose Multiple Binary Accuracy (MBA) to correct such bias.

**Sparse Evidence Can Suffice** (Zhao et al., 2026) addresses temporal reasoning from a different angle, arguing that real-world misinformation exhibits sparse and compositional evidence structure where reliable decisions depend on only a few coupled clues rather than exhaustive processing. The SIEVE framework employs an evidence-seeking agent that actively explores multimodal evidence and constructs compact evidence packages, trained with supervised trajectories and evidence-aware reinforcement learning. This work challenges the prevailing holistic video-understanding paradigm, suggesting that selective, agentic evidence acquisition may be more effective than exhaustive reasoning.

**Convergence:** Both works reveal limitations in current holistic processing approaches—TemporalBench demonstrates poor fine-grained temporal reasoning, while SIEVE shows that sparse, targeted evidence acquisition can outperform exhaustive processing.

### Theme 4: Efficient Routing and Conditional Processing

Emerging work recognizes that not all queries or inputs require the same computational treatment, motivating intelligent routing mechanisms.

**Smart Routing for Multimodal Video Retrieval** (Dela Rosa, 2025) introduces ModaRoute, an LLM-based intelligent routing system that dynamically selects optimal modalities for multimodal video retrieval. By analyzing query intent and predicting information needs, ModaRoute routes queries across ASR (speech), OCR (text), and visual indices, averaging 1.78 modalities per query versus exhaustive 3.0 modality search. This reduces computational overhead by 41% while achieving 60.9% Recall@5 (compared to 75.9% for exhaustive dense captions, which require expensive offline processing and miss 34% of clips with scene text not captured by ASR).

**MoRoute** (Gao et al., 2026) addresses routing at the architectural level for multimodal video generation, formulating a frozen VLM and pretrained video DiT as heterogeneous experts connected through dynamic layer routing. A lightweight block-wise router enables every DiT block to select the VLM layer most relevant to its generation stage, learning adaptive correspondence between multimodal understanding and video synthesis without joint training. The approach improves average scores by 0.15, 0.18, and 0.34 on a 1-5 scale across three benchmarks.

**Convergence:** Both routing works demonstrate that adaptive, conditional processing—selecting the right modalities or representations for each input—can improve efficiency and performance compared to exhaustive or uniform processing.

---

## Cross-Paper Synthesis

### Methodological Patterns

**Dataset-Centric Approaches (4 papers):** SynMulti, GBU-Palm, Prompt2LVideos, and TemporalBench all prioritize dataset creation or extension, reflecting recognition that data limitations constrain progress. These works collectively argue that benchmark quality and diversity are as important as model architecture innovations.

**Architectural Innovations (4 papers):** SD-MVSum, Mixup, MoRoute, and the text-guided anomaly detection work propose novel architectural mechanisms—cross-modal attention, dynamic mixing, layer routing, and bottleneck fusion—addressing specific challenges in multimodal integration.

**Agentic and Adaptive Systems (2 papers):** SIEVE and ModaRoute represent a shift toward adaptive, agentic approaches that dynamically select what to process rather than processing everything uniformly. This paradigm shift may represent an important direction for scaling multimodal systems.

### Performance Gaps and Limitations

The literature reveals several persistent gaps:

1. **Temporal Understanding Deficit:** The 30% human-AI gap on TemporalBench (Cai et al., 2024) indicates that current models fundamentally lack fine-grained temporal reasoning capabilities, a critical limitation for video understanding.

2. **Modality Imbalance:** Multiple works (Ma et al., 2025; Sun et al., 2026) identify modality imbalance as a core challenge, suggesting that current fusion mechanisms inadequately integrate information across modalities.

3. **Environmental Robustness:** GBU-Palm (Ma et al., 2026) reveals substantial architecture-dependent degradation under environmental shift, indicating poor cross-environment generalization.

4. **Efficiency-Effectiveness Tradeoffs:** ModaRoute (Dela Rosa, 2025) demonstrates a 15% Recall@5 drop (75.9% to 60.9%) for 41% computational savings, highlighting that efficiency gains come with performance costs that must be carefully managed.

### Emerging Directions

Several convergent trends point to promising research directions:

1. **Synthetic Data Viability:** SynMulti's demonstration that synthetic-trained models can match or exceed real-world trained models suggests synthetic data generation may scale more effectively than continued manual annotation efforts.

2. **Sparse Evidence Utilization:** SIEVE's success with compact evidence packages challenges the assumption that more processing always yields better results, suggesting selective, targeted reasoning may be more effective.

3. **Dynamic Routing and Adaptation:** Both ModaRoute and MoRoute demonstrate benefits of adaptive, input-conditioned processing, suggesting future systems should dynamically allocate computational resources rather than applying uniform processing.

4. **Evaluation Methodology Reform:** TemporalBench's identification of multi-choice QA bias and proposal of Multiple Binary Accuracy indicates that evaluation methodologies themselves require refinement to accurately measure capabilities.

---

## Individual Paper Summaries (APA Format)

1. Cai, M., Tan, R., Zhang, J., Zou, B., Zhang, K., Yao, F., Zhu, F., Gu, J., Zhong, Y., Shang, Y., Dou, Y., Park, J., Gao, J., Lee, Y. J., & Yang, J. (2024). TemporalBench: Benchmarking fine-grained temporal understanding for multimodal video models. *arXiv preprint arXiv:2410.10818*. https://arxiv.org/abs/2410.10818

2. Dela Rosa, K. (2025). Smart routing for multimodal video retrieval: When to search what. *arXiv preprint arXiv:2507.13374*. https://arxiv.org/abs/2507.13374

3. Jahagirdar, S. S., Saha, J., & Jawahar, C. V. (2025). Prompt2LVideos: Exploring prompts for understanding long-form multimodal videos. *arXiv preprint arXiv:2503.08335*. https://arxiv.org/abs/2503.08335

4. Ma, X., Ding, D., & Chen, H. (2025). Mixup helps understanding multimodal video better. *arXiv preprint arXiv:2510.10986*. https://arxiv.org/abs/2510.10986

5. Ma, Y., Yu, Z., Jia, W., Kumar, A., & Shen, L. (2026). GBU-Palm: A multimodal video dataset and benchmark for palm presentation attack detection. *arXiv preprint arXiv:2608.14389*. https://arxiv.org/abs/2608.14389

6. Mylonas, M., Zerva, C., Apostolidis, E., & Mezaris, V. (2025). SD-MVSum: Script-driven multimodal video summarization method and datasets. *arXiv preprint arXiv:2510.05652*. https://arxiv.org/abs/2510.05652

7. Rahman, T., Liao, R., & Sigal, L. (2026). SynMulti: Synthetic-to-real learning for multimodal video understanding. *arXiv preprint arXiv:2604.12335*. https://arxiv.org/abs/2604.12335

8. Sun, S., Hua, J., Feng, J., & Gong, X. (2026). Enhancing weakly supervised multimodal video anomaly detection through text guidance. *arXiv preprint arXiv:2602.10549*. https://arxiv.org/abs/2602.10549

9. Zhao, H., Xu, Y., Lin, X., Xie, D., Lu, J., Qian, Y., Wang, Y., Xu, H., & Gou, G. (2026). Sparse evidence can suffice: Agentic evidence seeking for multimodal video misinformation detection. *arXiv preprint arXiv:2607.18080*. https://arxiv.org/abs/2607.18080

10. Gao, C., Ma, J., Peng, Z., Wang, C., Wu, H., Liang, J., Li, G., & Li, J. (2026). MoRoute: Dynamic routing for in-context multimodal video generation. *arXiv preprint arXiv:2607.29545*. https://arxiv.org/abs/2607.29545

---

## Research Gaps and Future Directions

Based on this systematic review, several critical research gaps emerge:

### Gap 1: Temporal Reasoning Mechanisms

The 30% human-AI gap on TemporalBench indicates that current models lack fundamental temporal reasoning capabilities. Future work should investigate:
- Architectural innovations specifically targeting temporal reasoning
- Training objectives that explicitly reward temporal understanding
- Hybrid symbolic-neural approaches that can represent temporal relationships

### Gap 2: Modality-Balanced Learning

Despite recognition of modality imbalance, current solutions (mixup, bottleneck fusion) remain heuristic. Promising directions include:
- Theoretical frameworks for optimal modality weighting
- Adaptive mechanisms that learn modality importance per input
- Causal approaches to identify and correct modality-induced biases

### Gap 3: Cross-Environment Generalization

GBU-Palm's findings on environment-dependent degradation suggest poor robustness. Future research should explore:
- Domain adaptation techniques for multimodal video models
- Environment-invariant representation learning
- Test-time adaptation mechanisms

### Gap 4: Agentic and Selective Processing

The success of SIEVE and ModaRoute suggests that selective, agentic processing may outperform exhaustive approaches. Open questions include:
- How to train evidence-seeking policies that generalize across tasks
- Theoretical bounds on information loss from selective processing
- Integration of agentic selection with end-to-end training

### Gap 5: Synthetic Data Quality and Diversity

While SynMulti demonstrates synthetic data viability, critical questions remain:
- What properties determine synthetic-to-real transfer success?
- How to ensure synthetic data captures real-world edge cases?
- Can synthetic data generation scale indefinitely, or will diminishing returns emerge?

---

## Conclusion

This systematic literature review reveals a field in transition, moving from naive multimodal fusion toward sophisticated mechanisms for balancing, routing, and selectively processing information across modalities. The most striking finding is the substantial human-AI gap in temporal understanding (30% on TemporalBench), indicating that current models fundamentally lack capabilities essential for video comprehension. Concurrently, the emergence of synthetic data generation, agentic evidence-seeking, and dynamic routing suggests promising directions for scaling multimodal systems beyond current limitations.

The literature demonstrates growing recognition that more processing is not always better—sparse evidence can suffice, intelligent routing can reduce overhead by 41%, and synthetic data can match real-world annotation quality. These findings challenge prevailing assumptions and point toward a future where multimodal video understanding systems are more adaptive, efficient, and robust.

Critical gaps remain in temporal reasoning, modality-balanced learning, cross-environment generalization, and synthetic data quality assurance. Addressing these gaps will require both architectural innovations and fundamental rethinking of how multimodal information is integrated, weighted, and utilized for video understanding tasks.

---

## Sources

### Primary Sources (arXiv Papers)
- [TemporalBench](https://arxiv.org/abs/2410.10818) - Fine-grained temporal understanding benchmark revealing 30% human-AI gap
- [SynMulti](https://arxiv.org/abs/2604.12335) - Synthetic-to-real learning for multimodal video understanding
- [GBU-Palm](https://arxiv.org/abs/2608.14389) - Multimodal video dataset for palm presentation attack detection
- [SIEVE](https://arxiv.org/abs/2607.18080) - Agentic evidence seeking for misinformation detection
- [MoRoute](https://arxiv.org/abs/2607.29545) - Dynamic routing for multimodal video generation
- [ModaRoute](https://arxiv.org/abs/2507.13374) - Smart routing for multimodal video retrieval
- [SD-MVSum](https://arxiv.org/abs/2510.05652) - Script-driven multimodal video summarization
- [Mixup](https://arxiv.org/abs/2510.10986) - Multimodal mixup for preventing overfitting
- [Prompt2LVideos](https://arxiv.org/abs/2503.08335) - Long-form multimodal video understanding
- [Text-Guided Anomaly Detection](https://arxiv.org/abs/2602.10549) - Weakly supervised multimodal anomaly detection

### Search Methodology
- Database: arXiv (cs.CV category only)
- Search Query: "multimodal video"
- Date Range: January 1, 2024 - October 25, 2026
- Sort By: Relevance
- Total Papers Analyzed: 10
