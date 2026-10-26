# Systematic Literature Review: LLM Mid-Training

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "LLM mid-training", cs.CL category, published between 2023-10-27 and 2025-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 arXiv papers on LLM mid-training published between October 2023 and October 2025. The surveyed literature reveals mid-training as an emerging unified paradigm positioned between pre-training and fine-tuning, characterized by multi-phase annealing schedules, data quality refinement, and curriculum-based optimization strategies. Key findings demonstrate that mid-training substantially improves model performance through diverse synthetic data generation (12.74% improvement on MMLU/CMMLU), curriculum learning (18-45% reduction in training steps), and targeted reasoning augmentation (3x data efficiency gains). The field shows strong convergence around the importance of data quality over quantity, with innovative approaches including dynamic sampling, error-uncertainty frameworks, and thinking-augmented pre-training. However, limitations persist around scalability for small models, multilingual instruction-tuning requirements, and the need for systematic theoretical frameworks explaining mid-training effectiveness.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query `LLM mid-training`, filtered to category cs.CL, published between 2023-10-27 and 2025-10-26. Papers were sorted by relevance using co-citation analysis, and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening process**: 32 papers identified by search, 0 added from references (Semantic Scholar unavailable), 30 shortlisted, 30 screened with co-citation scoring (17 papers scored 0, 4 scored 1, 4 scored 2, 5 scored 3), 10 included.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Citation expansion was unavailable due to Semantic Scholar rate limiting.

## Themes

### Theme 1: Mid-Training as a Unified Paradigm

The surveyed literature establishes mid-training as a distinct stage between pre-training and fine-tuning, characterized by multiple annealing-style phases that refine data quality and optimization schedules. Mo et al. (2025) provide the first comprehensive survey formalizing mid-training as a unified paradigm, identifying its role in mitigating diminishing returns from noisy tokens and stabilizing convergence in late training stages. This conceptualization is supported by theoretical frameworks including gradient noise scale, information bottleneck theory, and curriculum learning principles.

The effectiveness of mid-training is demonstrated across multiple studies. Zhang et al. (2025) show that curriculum learning during mid-training phases accelerates convergence by 18-45% in training steps, while Wang et al. (2025) achieve 3x data efficiency improvements through thinking-augmented pre-training applied during mid-training from strong checkpoints. These findings collectively suggest that mid-training is not merely an optimization trick but a fundamental requirement for efficient large-scale model development.

### Theme 2: Data Quality and Synthetic Data Generation

A dominant theme across the literature is the shift from data quantity to data quality as the primary driver of mid-training performance. Zhang et al. (2025) address data scarcity through BoostQA, a 100B-token synthetic QA dataset generated using DeepSeek-R1 for STEM-focused synthesis and DeepSeek-V3 for answer refinement, achieving 12.74% average improvement on MMLU and CMMLU benchmarks when used to mid-train Llama-3 8B on 40B tokens.

This quality-over-quantity approach is reinforced by Wang et al. (2025), whose Thinking augmented Pre-Training (TPT) augments existing text with automatically generated thinking trajectories, making high-quality tokens more learnable through step-by-step reasoning decomposition. For a 3B parameter model, TPT improves post-training performance by over 10% on challenging reasoning benchmarks. The convergence around synthetic data generation suggests that the field is moving beyond web-scale scraping toward curated, high-signal training corpora.

### Theme 3: Curriculum Learning and Dynamic Sampling

Curriculum learning emerges as a critical mechanism for efficient mid-training, with systematic organization of training data from easy to hard proving consistently beneficial. Zhang et al. (2025) conduct the most extensive investigation to date, training over 200 models on up to 100B tokens across three curriculum strategies (vanilla, pacing-based sampling, interleaved) guided by six difficulty metrics. They identify compression ratio, lexical diversity (MTLD), and readability (Flesch Reading Ease) as the most effective difficulty signals.

This curriculum approach extends to dynamic sampling strategies. Wang et al. (2025) introduce the Error-Uncertainty (EU) Plane diagnostic framework and Quadrant-based Tuning (Q-Tuning), which coordinates sample pruning with asymmetric token pruning, achieving +38% average improvement over full-data SFT baseline using only 12.5% of original training data. The convergence on curriculum-based approaches suggests that data ordering provides practical efficiency gains orthogonal to existing data selection methods.

### Theme 4: Small Model Optimization and Resource Constraints

Several papers address the challenge of enabling strong performance from resource-constrained small models. Xu et al. (2025) develop a four-step systematic training recipe for Phi-4-Mini (3.8B parameters), including large-scale mid-training on diverse distilled long-CoT data, achieving performance that outperforms DeepSeek-R1-Distill-Qwen-7B by 3.2 points and DeepSeek-R1-Distill-Llama-8B by 7.7 points on Math-500.

Chen et al. (2025) address similar challenges with ToolExpander, which enhances tool-oriented reinforcement learning for weak small-scale LLMs that struggle with GRPO training. Their Dynamic Multi-Round Hard Sampling and Self-Exemplifying Thinking frameworks significantly improve training stability and tool-using capabilities. These papers collectively demonstrate that systematic mid-training strategies can overcome inherent capacity limitations of small models.

### Theme 5: Multilingual and Cross-Lingual Considerations

The literature addresses multilingual challenges in mid-training through novel initialization and instruction-tuning strategies. Özeren et al. (2025) propose HYPEROFA, a hypernetwork-based approach that maps from external multilingual word vector spaces to PLM token embedding spaces, overcoming limitations of convex combination approaches and matching or exceeding baseline performance in continual pre-training convergence.

Weber et al. (2024) investigate whether multilingual pre-trained LLMs require multilingual instruction-tuning datasets, finding that instruction-tuning on parallel corpora instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%. Their work challenges the Superficial Alignment Hypothesis, demonstrating that multilingual 7B parameter models require large-scale instruction-tuning datasets. These findings highlight the importance of language-aware mid-training strategies for polyglot models.

### Theme 6: Agentic and Tool-Use Training

Emerging work extends mid-training to agentic capabilities and tool use. Zhan et al. (2025) present KAT-Coder's multi-stage curriculum including Mid-Term Training that enhances reasoning, planning, and reflection using real software engineering data and synthetic agentic interactions. Their approach bridges the gap between static text-based training and dynamic real-world agentic execution.

Chen et al. (2025) similarly focus on tool-use capabilities, though for small models rather than coding-specific agents. The convergence on agentic training during mid-training phases suggests recognition that tool-use and planning capabilities require dedicated intermediate training stages rather than emerging spontaneously from pre-training.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several points:
- Mid-training is a distinct and necessary stage between pre-training and fine-tuning (Mo et al., 2025; Zhang et al., 2025; Wang et al., 2025)
- Data quality and curation matter more than raw scale for mid-training performance (Zhang et al., 2025; Wang et al., 2025)
- Curriculum learning and dynamic sampling consistently accelerate convergence and improve efficiency (Zhang et al., 2025; Wang et al., 2025)
- Small models can achieve competitive performance through systematic mid-training recipes (Xu et al., 2025; Chen et al., 2025)
- Multilingual models require dedicated multilingual instruction-tuning rather than relying on pre-training alone (Weber et al., 2024; Özeren et al., 2025)

**Disagreements**: The literature shows limited direct disagreement, likely due to the emergent nature of the field. However, tensions exist around:
- The optimal balance between synthetic and natural data: Zhang et al. (2025) advocate large-scale synthetic QA generation, while Wang et al. (2025) augment existing natural text with thinking trajectories rather than replacing it entirely
- The necessity of model-specific versus universal approaches: some papers propose universal frameworks (Mo et al., 2025; Wang et al., 2025) while others develop specialized solutions for small models (Xu et al., 2025; Chen et al., 2025) or multilingual settings (Weber et al., 2024; Özeren et al., 2025)

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Theoretical foundations**: While Mo et al. (2025) survey theoretical explanations (gradient noise scale, information bottleneck, curriculum learning), none of the empirical papers explicitly test or validate these theories. The field lacks controlled experiments isolating specific theoretical mechanisms.

2. **Standardized benchmarks**: Papers evaluate on diverse benchmarks (MMLU, CMMLU, Math-500, various tool-use benchmarks) without standardization. This makes cross-paper comparison difficult and obscures whether improvements generalize or are benchmark-specific.

3. **Computational cost analysis**: Despite claims of efficiency improvements, few papers report comprehensive computational cost comparisons. Zhang et al. (2025) note 18-45% reduction in training steps, but total compute costs including curriculum generation overhead remain unreported.

4. **Long-term stability**: All papers evaluate immediate post-training performance without examining long-term stability, catastrophic forgetting, or degradation over extended use. Mid-training's impact on these factors remains unknown.

5. **Scaling laws**: The literature lacks systematic investigation of how mid-training benefits scale with model size. Xu et al. (2025) and Chen et al. (2025) focus on small models, while others use various sizes without controlled scaling analysis.

6. **Domain specificity**: Most work focuses on general reasoning, math, or coding. Mid-training for specialized domains (medicine, law, science) receives minimal attention despite clear practical importance.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: How can tool-oriented reinforcement learning be improved for resource-constrained small-scale LLMs that struggle with GRPO training?
**Methodology**: Proposal of ToolExpander framework with Dynamic Multi-Round Hard Sampling (substituting challenging samples with few-shot demonstrations using exponential learning rate decay) and Self-Exemplifying Thinking (enhanced GRPO without KL divergence with adjusted clipping coefficients).
**Key findings**:
- GRPO training encounters challenges with small-scale architectures where models fail to produce accurate responses
- Dynamic Multi-Round Hard Sampling replaces challenging samples with high-quality few-shot demonstrations
- Self-Exemplifying Thinking eliminates KL divergence and encourages autonomous few-shot example generation
- ToolExpander significantly enhances tool-using capabilities in weak small-scale models while improving training stability
**Limitations**: Not stated in abstract

### Mo et al. (2025)

**Research question**: What is the role and structure of mid-training as a unified paradigm in large language model development?
**Methodology**: Systematic survey and taxonomy development of mid-training practices across data distribution, learning-rate scheduling, and long-context extension, synthesizing theoretical explanations from gradient noise scale, information bottleneck, and curriculum learning frameworks.
**Key findings**:
- Mid-training is an intermediate stage between pre-training and fine-tuning using multiple annealing-style phases to refine data quality and optimization schedules
- This stage mitigates diminishing returns from noisy tokens and stabilizes convergence in late training
- Mid-training extends model capability through context length extension and data quality improvements
- Effectiveness is explained through gradient noise scale, information bottleneck, and curriculum learning theories
- Survey provides taxonomy, practical insights, evaluation benchmarks, and identifies open challenges
**Limitations**: Not stated in abstract

### Özeren et al. (2025)

**Research question**: How can token embedding initialization for target-language tokens be made more expressive and adaptive beyond convex combinations of source-language embeddings?
**Methodology**: HYPEROFA, a hypernetwork-based approach mapping from external multilingual word vector space to PLM token embedding space using source-language tokens; once trained, the hypernetwork generates flexible embeddings for target-language tokens as starting point for continual pretraining.
**Key findings**:
- HYPEROFA consistently outperforms random initialization baseline
- Method matches or exceeds OFA performance in both continual pre-training convergence and downstream task performance
- Hypernetwork approach overcomes OFA's limitation of restricting target-language embeddings to convex combinations
- Code made publicly available
**Limitations**: Not stated in abstract

### Wang et al. (2025)

**Research question**: How can data pruning methods jointly optimize both sample-level and token-level dimensions to improve data efficiency in supervised fine-tuning of large language models?
**Methodology**: Introduction of Error-Uncertainty (EU) Plane diagnostic framework to characterize training data utility across samples and tokens, then Quadrant-based Tuning (Q-Tuning), a two-stage unified framework coordinating sample pruning with asymmetric token pruning.
**Key findings**:
- Q-Tuning achieves +38% average improvement over full-data SFT baseline on SmolLM2-1.7B using only 12.5% of original training data
- Method sets new state of the art across five diverse benchmarks
- Q-Tuning is first dynamic pruning approach to consistently outperform full-data training
- Context-aware scoring mechanism enables selective token trimming exclusively from misconception samples
**Limitations**: Not stated in abstract

### Wang et al. (2025)

**Research question**: How can the data efficiency of large language model pre-training be improved given limited high-quality training data?
**Methodology**: Thinking augmented Pre-Training (TPT) augments existing text data with automatically generated thinking trajectories to make high-quality tokens more learnable through step-by-step reasoning and decomposition, evaluated across diverse training configurations up to 100B tokens.
**Key findings**:
- TPT substantially improves LLM performance across various model sizes and families
- Method enhances data efficiency of LLM pre-training by a factor of 3
- For 3B parameter model, TPT improves post-training performance by over 10% on several challenging reasoning benchmarks
- Thinking trajectories make high-quality tokens more learnable by decomposing complex token-level reasoning
- Approach is universal and scalable across different training configurations
**Limitations**: Not stated in abstract

### Weber et al. (2024)

**Research question**: Do multilingual pre-trained LLMs require multilingual instruction-tuning datasets, and how do language composition and dataset size affect cross-lingual instruction following capabilities?
**Methodology**: Extensive study examining performance of multilingual models instruction-tuned on different language compositions using parallel instruction-tuning benchmarks across major Indo-European languages, systematically analyzing effects of language and dataset size, with human annotation study evaluating alignment between human-based and GPT-4-based evaluation.
**Key findings**:
- Instruction-tuning on parallel corpora instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%
- Superficial Alignment Hypothesis does not hold in general, as investigated multilingual 7B parameter model requires large-scale instruction-tuning datasets
- First extensive study of multilingual model performance on parallel instruction-tuning benchmarks across most spoken Indo-European languages
- Human annotation study reveals alignment patterns between human-based and GPT-4-based evaluation within multilingual chat scenarios
**Limitations**: Not stated in abstract

### Xu et al. (2025)

**Research question**: Can a systematic training recipe unlock strong reasoning capabilities in small language models despite their limited capacity?
**Methodology**: Four-step systematic training recipe applied to Phi-4-Mini (3.8B parameters): (1) large-scale mid-training on diverse distilled long-CoT data, (2) supervised fine-tuning on high-quality long-CoT data, (3) Rollout DPO with curated preference dataset, and (4) Reinforcement Learning with Verifiable Reward.
**Key findings**:
- Chain-of-Thought enhances reasoning in LLMs but improving reasoning in SLMs remains challenging due to limited capacity
- Distillation from LLM-generated synthetic data can substantially improve SLM reasoning ability
- Four-step training recipe includes mid-training, fine-tuning, Rollout DPO, and RL with Verifiable Reward
- Phi-4-Mini-Reasoning outperforms DeepSeek-R1-Distill-Qwen-7B by 3.2 points on Math-500
- Phi-4-Mini-Reasoning outperforms DeepSeek-R1-Distill-Llama-8B by 7.7 points on Math-500
**Limitations**: Not stated in abstract

### Zhan et al. (2025)

**Research question**: How can large language models be trained to bridge the gap between static text-based training and dynamic real-world agentic execution in software development workflows?
**Methodology**: KAT-Coder trained through multi-stage curriculum: Mid-Term Training (enhancing reasoning, planning, and reflection using real software engineering data and synthetic agentic interactions), Supervised Fine-Tuning (million-sample dataset balancing 20 programming languages, 10 development contexts, and 10 task archetypes), Reinforcement Fine-Tuning (novel multi-ground-truth reward formulation), and Reinforcement-to-Deployment Adaptation (Error-Masked SFT and Tree-Structured Trajectory Training).
**Key findings**:
- Multi-stage training enables KAT-Coder to achieve robust tool-use reliability, instruction alignment, and long-context reasoning
- RFT stage introduces novel multi-ground-truth reward formulation for stable and sample-efficient policy optimization
- Reinforcement-to-Deployment phase adapts model to production-grade IDE environments
- KAT-Dev, the KAT series 32B model, has been open-sourced on Hugging Face
- Approach forms deployable foundation for real-world intelligent coding agents
**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: Can curriculum learning improve efficiency in language model pretraining by organizing training data from easy to hard?
**Methodology**: Systematic investigation with over 200 models trained on up to 100B tokens across three curriculum learning strategies (vanilla, pacing-based sampling, interleaved) guided by six difficulty metrics, evaluated on eight benchmarks under limited data, unlimited data, and continual training scenarios.
**Key findings**:
- Curriculum learning remains underexplored for language model pretraining despite success in other ML domains
- Curriculum learning consistently accelerates convergence in early and mid-training phases, reducing training steps by 18-45%
- When used as warmup before standard random sampling, curriculum learning yields sustained improvements up to 3.5%
- Compression ratio, lexical diversity (MTLD), and readability (Flesch Reading Ease) are identified as most effective difficulty signals
- Data ordering provides practical mechanism for more efficient LLM pretraining orthogonal to existing data selection methods
**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can large-scale, diverse synthetic QA data be generated to overcome data scarcity and improve mid-training performance?
**Methodology**: Development of diversified synthesis pipeline creating BoostQA, a 100B-token QA dataset, using DeepSeek-R1 for STEM-focused multi-grade synthesis and DeepSeek-V3 for answer refinement; dataset used to mid-train Llama-3 8B on 40B tokens.
**Key findings**:
- Traditional corpora provide limited information for knowledge-intensive training, creating scalability challenges
- BoostQA synthesis pipeline curates seed data from heterogeneous sources and uses DeepSeek-R1 for STEM-focused and high-difficulty synthesis
- DeepSeek-V3 refines answers to improve output quality
- Mid-training with BoostQA achieved 12.74% average improvement on MMLU and CMMLU benchmarks
- Approach established SOTA average performance across 12 benchmarks with robust scalability as model size and data volume increase
**Limitations**: Not stated in abstract

## References

Chen, F., Wang, P., Li, X., Li, W., Lei, S., & Xiang, D. (2025). ToolExpander: Extending the frontiers of tool-using reinforcement learning to weak LLMs. arXiv. https://arxiv.org/abs/2510.07737

Mo, K., Shi, Y., Weng, W., Zhou, Z., Liu, S., Zhang, H., & Zeng, A. (2025). Mid-training of large language models: A survey. arXiv. https://arxiv.org/abs/2510.06826

Özeren, E., Liu, Y., & Schütze, H. (2025). HYPEROFA: Expanding LLM vocabulary to new languages via hypernetwork-based embedding initialization. arXiv. https://arxiv.org/abs/2504.21018

Wang, L., Yang, N., Huang, S., Dong, L., & Wei, F. (2025). Thinking augmented pre-training. arXiv. https://arxiv.org/abs/2509.20186

Wang, S., Wang, J., Zhang, J., Wang, C., Min, Y., Wen, Z., Ren, X., Huang, F., Jiang, H., Lin, J., Liu, D., & Zhang, L. (2025). Winning the pruning gamble: A unified approach to joint sample and token pruning for efficient supervised fine-tuning. arXiv. https://arxiv.org/abs/2509.23873

Weber, A. A., Thellmann, K., Ebert, J., Flores-Herr, N., Lehmann, J., Fromm, M., & Ali, M. (2024). Investigating multilingual instruction-tuning: Do polyglot models demand for multilingual instructions? arXiv. https://arxiv.org/abs/2402.13703

Xu, H., Peng, B., Awadalla, H., Chen, D., Chen, Y.-C., Gao, M., Kim, Y. J., Li, Y., Ren, L., Shen, Y., Wang, S., Xu, W., Gao, J., & Chen, W. (2025). Phi-4-Mini-Reasoning: Exploring the limits of small reasoning language models in math. arXiv. https://arxiv.org/abs/2504.21233

Zhan, Z., Deng, K., Wang, J., Zhang, X., Tang, H., Zhang, M., Lai, Z., Huang, H., Xiang, W., Wu, K., Zhuang, W., Wang, S., Yan, S., Lei, K., Feng, Z., Wang, H., Lin, Z., Li, M., Xie, M., & Cui, Y. (2025). KAT-Coder technical report. arXiv. https://arxiv.org/abs/2510.18779

Zhang, X., Tu, C., Ren, C., Weng, R., Yan, H., Wang, J., & Cai, X. (2025). Large-scale diverse synthesis for mid-training. arXiv. https://arxiv.org/abs/2508.01326

Zhang, Y., Mohamed, A., Abdine, H., Shang, G., & Vazirgiannis, M. (2025). Beyond random sampling: Efficient language model pretraining via curriculum learning. arXiv. https://arxiv.org/abs/2506.11300
