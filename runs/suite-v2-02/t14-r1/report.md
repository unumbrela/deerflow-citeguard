# Systematic Literature Review: Video Understanding with Multimodal Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: "video understanding multimodal", cs.CV, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on video understanding with multimodal models, revealing a rapidly evolving field focused on benchmarking, efficiency, and reasoning capabilities. The surveyed literature demonstrates a critical shift from single-turn evaluation to multi-turn interactive dialogue systems, alongside growing emphasis on model efficiency and temporal reasoning. A recurring theme is the recognition that current benchmarks suffer from inflated leaderboard scores that do not reflect real-world capabilities, prompting the development of more rigorous evaluation frameworks. The field is also witnessing significant advances in synthetic-to-real learning paradigms and specialized domain applications, particularly in clinical and surgical contexts.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "video understanding multimodal", filtered to category cs.CV, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmark Evolution and Multi-Turn Evaluation

The surveyed literature reveals a fundamental shift in how video understanding benchmarks are designed and evaluated. Early benchmarks focused on single-turn question answering, but recent work emphasizes multi-turn interactive dialogues that better reflect real-world usage scenarios. Pan et al. (2025) introduced MT-Video-Bench to address this gap, creating 1,000 curated multi-turn dialogues across diverse domains that assess six core competencies in perceptivity and interactivity. Their evaluation revealed significant performance discrepancies in current multimodal large language models (MLLMs) when handling interactive video dialogues.

This evolution extends to benchmark complexity hierarchies. Fu et al. (2026) created Video-MME-v2 with a progressive tri-level hierarchy encompassing multi-point visual aggregation, temporal dynamics modeling, and complex multimodal reasoning. Their work highlights a critical discrepancy between inflated leaderboard scores and actual model capabilities in real-world applications. Similarly, Shi and Zhang (2026) introduced HAVEN with a fully granular dataset architecture spanning frame, shot, and video levels, addressing the fragmentation of supervision across isolated granularities in existing benchmarks.

Song et al. (2025) expanded the benchmarking scope to multi-discipline lecture understanding with Video-MMLU, testing over 90 models ranging from 0.5B to 40B parameters. Their findings indicate that current models struggle particularly with tasks requiring both perception and reasoning, with performance influenced by the number of visual tokens and the choice of large language models.

### Theme 2: Model Efficiency and Scalability

A significant research direction focuses on developing efficient video understanding models that require fewer computational resources while maintaining performance. Zhang et al. (2025) developed TinyLLaVA-Video, a 3.6B parameter model that challenges the prevailing assumption that effective video understanding requires models with over 7B parameters. Their video-level group resampler effectively mitigates redundancy while enhancing temporal comprehension, requiring only one day of training on 8 A100-40G GPUs while surpassing several existing 7B-parameter models on multiple benchmarks.

Complementary to efficiency in model architecture is efficiency in data acquisition. Rahman et al. (2026) proposed SynMulti, demonstrating that synthetic data pipelines can serve as scalable alternatives to expensive real-world annotation. Their unified synthetic data generation pipeline automatically produces unlimited multimodal video data, with models trained predominantly on synthetic data generalizing effectively to real-world datasets and often outperforming traditionally trained counterparts.

### Theme 3: Reasoning Consistency and Visual Grounding

The literature consistently identifies a critical challenge: current models' reasoning often relies heavily on linguistic priors rather than visual content. Maaz et al. (2025) formalized two diagnostic metrics—Think Answer Consistency (TAC) and Video Attention Score (VAS)—to measure this phenomenon. TAC measures alignment between reasoning and answers, while VAS captures the extent to which reasoning depends on visual versus textual cues. Their Video-R2 model combines timestamp-aware supervised fine-tuning with Group Relative Policy Optimization guided by a Temporal Alignment Reward, achieving consistently higher TAC, VAS, and accuracy across 11 video reasoning benchmarks.

This theme connects to findings about modality imbalance. Ma et al. (2025) proposed Multimodal Mixup (MM) and Balanced Multimodal Mixup (B-MM) to address overfitting to strong modalities during training. Their approach applies mixup at the aggregated multimodal feature level, with B-MM dynamically adjusting mixing ratios for each modality based on their relative contributions to the learning objective, demonstrating effectiveness across several datasets in improving generalization and multimodal robustness.

### Theme 4: Domain-Specialized Applications

The surveyed literature shows growing specialization of multimodal video understanding for specific domains, particularly clinical and surgical applications. Amprimo et al. (2025) created EHWGesture, a multimodal dataset with over 1,100 recordings of five clinically relevant gestures captured using two RGB-Depth cameras and an event camera. All devices are spatially calibrated and synchronized for cross-modal alignment, with recordings organized by execution speed classes that mirror clinical evaluations of hand dexterity. Their baseline experiments demonstrate the dataset's potential for gesture classification, trigger detection, and action quality assessment.

Chen et al. (2025) proposed SurgLLM, a versatile large multimodal model specifically designed for surgical video understanding with enhanced spatial focus and temporal awareness. Their framework incorporates Surgical Context-aware Multimodal Pretraining for spatial focus, Temporal-aware Multimodal Tuning for temporal reasoning, and a Surgical Task Dynamic Ensemble to handle various understanding tasks without conflicts. The model demonstrates significant improvements over state-of-the-art approaches across diverse surgical video understanding tasks, including captioning, general VQA, and temporal VQA.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that current evaluation benchmarks are insufficient for capturing real-world model capabilities. Pan et al. (2025), Fu et al. (2026), and Shi and Zhang (2026) all identify the gap between leaderboard performance and practical utility as a critical issue. There is also agreement across papers that temporal reasoning and visual grounding remain significant challenges, with Maaz et al. (2025), Song et al. (2025), and Chen et al. (2025) all emphasizing the importance of temporal awareness in video understanding models.

**Disagreements**: The literature shows some tension regarding the role of synthetic versus real data. While Rahman et al. (2026) demonstrate that synthetic training can outperform traditional approaches, the clinical gesture work by Amprimo et al. (2025) emphasizes the irreplaceable value of precisely calibrated real-world multimodal capture with ground-truth tracking. Additionally, there is implicit disagreement about model scale requirements: Zhang et al. (2025) show that smaller models can be effective, while Song et al. (2025) evaluate models up to 40B parameters, suggesting the field has not reached consensus on optimal model size.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly state their own limitations in their abstracts, suggesting a potential gap in critical self-assessment or space constraints in arXiv submissions. Second, while multiple papers address benchmark design and model architecture, there is limited discussion of computational efficiency during inference, which is critical for real-world deployment. Third, the literature shows a gap in cross-domain generalization studies—while domain-specialized models are emerging, there is limited work on how models trained on one domain (e.g., surgical videos) transfer to others.

Additionally, Fu et al. (2026) note that thinking-based reasoning is highly dependent on textual cues, improving with subtitles but sometimes degrading in purely visual settings, indicating a gap in purely visual reasoning capabilities. The literature also lacks discussion of user interaction design and how multimodal video understanding systems should be integrated into practical workflows, particularly in clinical settings where Amprimo et al. (2025) and Chen et al. (2025) focus on technical capabilities without addressing deployment considerations.

## Per-Paper Annotations

### Amprimo et al. (2025)

**Research question**: How can a multimodal dataset be created to advance clinical gesture understanding with precise tracking and action quality assessment?

**Methodology**: The authors collected EHWGesture, a multimodal dataset with over 1,100 recordings (6 hours) of five clinically relevant gestures from 25 subjects using two RGB-Depth cameras and an event camera. A motion capture system provided ground-truth hand landmark tracking, and recordings were organized by execution speed classes.

**Key findings**:
- Existing datasets often lack multimodal and multi-view diversity, precise ground-truth tracking, and action quality components
- EHWGesture includes five clinically relevant gestures with multimodal capture
- All devices are spatially calibrated and synchronized for cross-modal alignment
- Recordings are organized by execution speed classes that mirror clinical evaluations of hand dexterity
- Baseline experiments demonstrate the dataset's potential for gesture classification, trigger detection, and action quality assessment

**Limitations**: Not stated in abstract.

### Chen et al. (2025)

**Research question**: How can large multimodal models be improved for versatile surgical video understanding with enhanced spatial focus and temporal awareness?

**Methodology**: The authors propose SurgLLM framework with Surgical Context-aware Multimodal Pretraining for spatial focus, Temporal-aware Multimodal Tuning for temporal reasoning, and a Surgical Task Dynamic Ensemble to handle various understanding tasks without conflicts.

**Key findings**:
- SurgLLM demonstrates significant improvements over state-of-the-art approaches across diverse surgical video understanding tasks
- The framework effectively handles captioning, general VQA, and temporal VQA tasks
- Instrument-centric Masked Video Reconstruction and multimodal alignment enhance spatial perception
- Interleaved multimodal embeddings improve temporal reasoning capabilities

**Limitations**: Not stated in abstract.

### Fu et al. (2026)

**Research question**: How can video understanding benchmarks be designed to rigorously evaluate model robustness and faithfulness beyond saturated leaderboard scores?

**Methodology**: The authors created Video-MME-v2 with a progressive tri-level hierarchy (multi-point visual aggregation, temporal dynamics modeling, complex multimodal reasoning) and a group-based non-linear evaluation strategy. The benchmark was constructed through a controlled human annotation pipeline involving 12 annotators and 50 reviewers over 3,300 human-hours with up to 5 rounds of quality assurance.

**Key findings**:
- Existing benchmarks show a critical discrepancy between inflated leaderboard scores and real-world model capabilities
- The progressive tri-level hierarchy incrementally increases video comprehension complexity
- Group-based non-linear evaluation enforces consistency across related queries and coherence in multi-step reasoning
- There is a substantial gap between the best model (Gemini-3-Pro) and human experts
- Thinking-based reasoning is highly dependent on textual cues, improving with subtitles but sometimes degrading in purely visual settings

**Limitations**: Not stated in abstract.

### Ma et al. (2025)

**Research question**: How can multimodal mixup strategies address the problem of modality imbalance and overfitting in multimodal video understanding models?

**Methodology**: The authors propose Multimodal Mixup (MM) applying Mixup at the aggregated multimodal feature level, and Balanced Multimodal Mixup (B-MM) which dynamically adjusts mixing ratios for each modality based on their relative contributions to the learning objective.

**Key findings**:
- Multimodal Mixup effectively improves generalization by mitigating overfitting to strong modalities
- Balanced Multimodal Mixup accounts for modality imbalance during training
- Both methods demonstrate effectiveness across several datasets in improving generalization and multimodal robustness

**Limitations**: Not stated in abstract.

### Maaz et al. (2025)

**Research question**: How can multimodal language models be improved to generate reasoning that is logically consistent and grounded in visual evidence rather than linguistic priors?

**Methodology**: The authors formalized two diagnostic metrics (Think Answer Consistency and Video Attention Score) and proposed a reinforcement learning approach combining timestamp-aware supervised fine-tuning with Group Relative Policy Optimization guided by a Temporal Alignment Reward. The approach was evaluated across 11 video reasoning benchmarks.

**Key findings**:
- Current models' reasoning often relies heavily on linguistic priors rather than visual content
- Think Answer Consistency measures alignment between reasoning and answers
- Video Attention Score captures the extent to which reasoning depends on visual versus textual cues
- The Video-R2 model achieves consistently higher TAC, VAS, and accuracy across multiple benchmarks
- Improvements in temporal alignment and reasoning coherence lead to more accurate and trustworthy video understanding

**Limitations**: Not stated in abstract.

### Pan et al. (2025)

**Research question**: How can Multimodal Large Language Models be evaluated on multi-turn video dialogue capabilities that reflect real-world interactive scenarios?

**Methodology**: The authors created MT-Video-Bench, a benchmark with 1,000 curated multi-turn dialogues across diverse domains that assess 6 core competencies in perceptivity and interactivity. They evaluated various state-of-the-art open-source and closed-source MLLMs on this benchmark.

**Key findings**:
- Existing evaluation benchmarks are limited to single-turn question answering and do not capture multi-turn dialogue complexity
- MT-Video-Bench assesses 6 core competencies focused on perceptivity and interactivity
- The benchmark includes applications like interactive sports analysis and multi-turn video-based intelligent tutoring
- Evaluation revealed significant performance discrepancies and limitations in current MLLMs for handling multi-turn video dialogues

**Limitations**: Not stated in abstract.

### Rahman et al. (2026)

**Research question**: Can synthetic data pipelines serve as a scalable alternative to expensive real-world annotation for training multimodal video understanding models?

**Methodology**: The authors propose SynMulti dataset and a unified synthetic data generation pipeline capable of automatically producing unlimited multimodal video data, along with a VQA-based fine-tuning strategy to enhance reasoning ability, evaluated on video object counting, VQA, and object segmentation tasks.

**Key findings**:
- Models trained predominantly on synthetic data generalize effectively to real-world datasets
- Synthetic training often outperforms traditionally trained counterparts
- Unified synthetic data pipelines enable scalable and consistent data creation across multiple task formats
- VQA-based fine-tuning encourages deeper visual grounding and reasoning

**Limitations**: Not stated in abstract.

### Shi and Zhang (2026)

**Research question**: How can multimodal large language models be better evaluated for summarizing and reasoning over complex video narratives?

**Methodology**: The authors introduce HAVEN, a hierarchically aligned multimodal benchmark with fully granular (frame, shot, and video levels) and fully multimodal (video and text) dataset architecture, along with a comprehensive evaluation suite spanning summarization, temporal reasoning, multimodal grounding, and saliency ranking.

**Key findings**:
- Existing benchmarks fragment supervision across isolated granularities, failing to capture hierarchical cross-modal alignment
- Benchmarking of state-of-the-art MLLMs reveals a gap between surface-level textual fluency and grounded multimodal understanding
- HAVEN provides a rigorous, standardized testbed for interpretable, hierarchical video understanding

**Limitations**: Not stated in abstract.

### Song et al. (2025)

**Research question**: What are the capabilities of language multimodal models (LMMs) in understanding multi-discipline lectures?

**Methodology**: The authors introduce Video-MMLU, a massive benchmark to evaluate LMMs on multi-discipline lecture understanding, and test over 90 open-source and proprietary models ranging from 0.5B to 40B parameters.

**Key findings**:
- Current models show limitations in addressing cognitive challenges presented by multi-discipline lectures
- Models struggle particularly with tasks requiring both perception and reasoning
- The number of visual tokens and the choice of large language models influence performance

**Limitations**: The abstract notes limitations of current models but does not explicitly state limitations of this study.

### Zhang et al. (2025)

**Research question**: How can lightweight video understanding models be designed to effectively process long visual sequences and temporal understanding while requiring fewer resources?

**Methodology**: The authors developed TinyLLaVA-Video, a 3.6B parameter model featuring a video-level group resampler that reduces visual tokens at the video level. The model was trained for one day on 8 A100-40G GPUs and evaluated on multiple benchmarks.

**Key findings**:
- Most existing open-source video understanding models require over 7B parameters and large-scale datasets
- The video-level group resampler effectively mitigates redundancy while enhancing temporal comprehension
- TinyLLaVA-Video requires only one day of training on 8 A100-40G GPUs
- The model surpasses several existing 7B-parameter models on multiple benchmarks

**Limitations**: Not stated in abstract.

## References

Amprimo, G., Ancilotto, A., Savino, A., Quazzolo, F., Ferraris, C., Olmo, G., Farella, E., & Di Carlo, S. (2025). EHWGesture -- A dataset for multimodal understanding of clinical gestures. arXiv. https://arxiv.org/abs/2509.07525

Chen, Z., Luo, X., Yuan, K., Wu, J., Chan, D. T. M., Navab, N., Liu, H., Lei, Z., & Luo, J. (2025). SurgLLM: A versatile large multimodal model with spatial focus and temporal awareness for surgical video understanding. arXiv. https://arxiv.org/abs/2509.00357

Fu, C., Yuan, H., Dong, Y., Zhang, Y.-F., Shen, Y., Hu, X., Li, X., Su, J., Long, C., Xie, X., Xie, Y., Zheng, X., Yang, X., Cao, H., Wu, Y., Liu, Z., Sun, X., Shan, C., & He, R. (2026). Video-MME-v2: Towards the next stage in benchmarks for comprehensive video understanding. arXiv. https://arxiv.org/abs/2604.05015

Ma, X., Ding, D., & Chen, H. (2025). Mixup helps understanding multimodal video better. arXiv. https://arxiv.org/abs/2510.10986

Maaz, M., Rasheed, H., Khan, F. S., & Khan, S. (2025). Video-R2: Reinforcing consistent and grounded reasoning in multimodal language models. arXiv. https://arxiv.org/abs/2511.23478

Pan, Y., Xie, Q., Zhang, G., Wang, Z., Wen, Y., Zhang, Y., Hu, H., Pan, Z., Huang, Y., Gan, Z., Lin, Y., Ping, A., Li, S., Wang, Y., & Peng, T. (2025). MT-Video-Bench: A holistic video understanding benchmark for evaluating multimodal LLMs in multi-turn dialogues. arXiv. https://arxiv.org/abs/2510.17722

Rahman, T., Liao, R., & Sigal, L. (2026). SynMulti: Synthetic-to-real learning for multimodal video understanding. arXiv. https://arxiv.org/abs/2604.12335

Shi, M., & Zhang, H. (2026). HAVEN: Hierarchically aligned multimodal benchmark for unified video understanding. arXiv. https://arxiv.org/abs/2605.19223

Song, E., Chai, W., Xu, W., Xie, J., Liu, Y., & Wang, G. (2025). Video-MMLU: A massive multi-discipline lecture understanding benchmark. arXiv. https://arxiv.org/abs/2504.14693

Zhang, X., Weng, X., Yue, Y., Fan, Z., Wu, W., & Huang, L. (2025). TinyLLaVA-Video: Towards smaller LMMs for video understanding with group resampler. arXiv. https://arxiv.org/abs/2501.15513
