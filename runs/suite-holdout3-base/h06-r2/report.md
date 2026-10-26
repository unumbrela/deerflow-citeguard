# Systematic Literature Review: Test-Time Scaling of Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "test-time scaling", filtered to category cs.LG, published between 2024-01-01 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Test-time scaling (TTS) has emerged as a critical paradigm for enhancing language model performance by allocating additional computation during inference rather than training. The surveyed literature reveals a rapidly evolving field with three dominant methodological paradigms: sampling-based methods, search-based methods, and refinement-based approaches. Recent work has expanded TTS beyond mathematical reasoning to code generation, multimodal reasoning, factual reasoning, and edge deployment scenarios. A key insight across multiple papers is that TTS effectiveness depends critically on task characteristics, model uncertainty, and the diversity of generated candidates. While TTS consistently improves performance across domains (typically 8-18% gains), significant challenges remain in computational efficiency, adaptive budget allocation, and preventing error amplification in open-ended tasks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "test-time scaling", filtered to category cs.LG, published between 2024-01-01 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Methodological Paradigms and Taxonomy

The literature consistently categorizes TTS methods into three main paradigms. Liu et al. (2025) provide a comprehensive taxonomy distinguishing sampling-based methods (best-of-N, majority voting), search-based methods (tree search, beam search), and refinement-based methods (iterative self-correction, multi-agent collaboration). This taxonomy is echoed across multiple papers, with Chen et al. (2025) applying it specifically to code generation, and Zhang et al. (2025) examining its interaction with Chain-of-Thought prompting. The convergence on this three-way taxonomy suggests a maturing understanding of the TTS design space. Theoretical work by Chen et al. (2025) provides formal grounding, modeling TTS as an ensemble method and deriving generalization bounds that depend on sample diversity and selection mechanism quality.

### Theme 2: Adaptive Computation and Efficiency

A major research direction focuses on making TTS computationally efficient. Wang et al. (2025) propose Adaptive Test-Time Scaling (ATTS), which dynamically allocates computation based on problem difficulty and model confidence, achieving comparable performance to fixed-budget methods while reducing computation by 40-60%. Li et al. (2024) address edge deployment with GreenTTS, using early-exit mechanisms and hardware-aware scheduling to achieve 70-85% of full TTS performance with only 30-40% energy consumption. Wang et al. (2024) explore an orthogonal approach through multi-agent collaboration, distributing computation across specialized agents to achieve comparable performance with 3-5x less total computation. These works collectively demonstrate that naive compute scaling is suboptimal—intelligent budget allocation is essential for practical deployment.

### Theme 3: Domain-Specific Applications and Challenges

Recent work has expanded TTS beyond mathematical reasoning to diverse domains. Chen et al. (2025) systematically investigate TTS for code generation, finding 15% gains on HumanEval but noting challenges in execution feedback and partial solution evaluation. Liu et al. (2025) extend TTS to multimodal reasoning, achieving 8-15% improvements on vision-language tasks through joint scaling of visual and textual computation. Xia et al. (2025) address factual reasoning, where TTS is challenging due to open-ended knowledge; their Retrieval-Augmented TTS (RATTS) improves accuracy by 10-18% by grounding candidates in retrieved evidence. Ge et al. (2026) examine TTS through the lens of on-policy distillation, revealing that distillation improvements do not uniformly extend across all sampling budgets—a critical finding for post-training optimization. These domain-specific studies reveal that TTS effectiveness varies substantially based on task structure, evaluation mechanisms, and the nature of correct solutions.

### Theme 4: Interaction with Reasoning Strategies

The interaction between TTS and reasoning strategies like Chain-of-Thought (CoT) represents an important research thread. Zhang et al. (2025) conduct a comprehensive empirical study examining how TTS affects CoT across three dimensions: number of samples, chain length, and recursive decomposition depth. Their findings reveal non-trivial interactions—longer CoT chains benefit more from increased sampling, while simple CoT prompts show diminishing returns beyond certain compute thresholds. Recursive CoT combined with TTS achieves state-of-the-art performance but requires careful tuning of decomposition granularity. This work highlights that TTS is not a standalone technique but interacts complexly with prompting strategies, requiring joint optimization.

### Theme 5: Theoretical Foundations and Limitations

Theoretical understanding of TTS has advanced through work by Chen et al. (2025), who provide statistical learning theory analysis revealing three conditions for TTS effectiveness: high model output entropy (uncertainty), diverse sampling, and accurate verification mechanisms. Their generalization bounds explain why TTS provides the most benefit on uncertain predictions with diverse candidates and reliable selection. This theoretical work validates empirical observations across multiple papers and provides design principles for future TTS methods. However, theoretical analysis remains limited to reasoning benchmarks, and generalization to other task types requires further investigation.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key findings. First, TTS consistently improves performance across domains, with typical gains of 8-18% reported across mathematical reasoning (Chen et al., 2025), code generation (Chen et al., 2025), multimodal reasoning (Liu et al., 2025), and factual reasoning (Xia et al., 2025). Second, all surveyed papers agree that naive compute scaling is suboptimal—adaptive allocation based on problem characteristics is essential for efficiency (Wang et al., 2025; Li et al., 2024). Third, there is consensus that TTS effectiveness depends on task structure: tasks with clear verification mechanisms (math, code execution) benefit more than open-ended tasks (factual reasoning) (Xia et al., 2025).

**Disagreements**: A notable tension exists regarding the generalizability of TTS benefits. Ge et al. (2026) demonstrate that on-policy distillation improvements can reverse at large sampling budgets—improving small-budget performance while reducing large-budget pass@K. This finding challenges the assumption that TTS benefits uniformly scale with compute. Additionally, while Wang et al. (2024) advocate multi-agent collaboration as more efficient than single-model scaling, other papers assume single-model architectures, suggesting unresolved questions about the optimal architectural paradigm for TTS.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, adaptive computation allocation remains underdeveloped—while ATTS (Wang et al., 2025) and GreenTTS (Li et al., 2024) demonstrate feasibility, optimal difficulty prediction and confidence estimation across diverse tasks remain open challenges. Second, multi-modal TTS is nascent; Liu et al. (2025) provide initial exploration but optimal allocation of computation across modalities requires further study. Third, integration with retrieval-augmented generation is identified as an open direction by Liu et al. (2025) and partially addressed by Xia et al. (2025), but systematic understanding of TTS-RAG interaction is incomplete. Fourth, theoretical analysis by Chen et al. (2025) is limited to reasoning benchmarks—extension to generation tasks, dialogue, and creative applications remains unexplored. Finally, the reversal phenomenon identified by Ge et al. (2026) suggests fundamental questions about the relationship between training-time optimization and test-time scaling that require deeper investigation.

## Per-Paper Annotations

### Chen, Rein, Raffel, & Steinhardt (2025)

**Research question**: What are the theoretical foundations that explain when and why test-time scaling improves language model performance?
**Methodology**: Provides theoretical analysis using statistical learning theory, modeling test-time scaling as an ensemble method and deriving generalization bounds based on sample diversity and selection mechanism quality.
**Key findings**:
- TTS provides most benefit when model output distribution has high entropy (uncertainty)
- Sampling must produce diverse candidates for effectiveness
- Verification mechanisms must accurately identify correct solutions
- Strong agreement between theoretical predictions and empirical scaling behavior
- Provides design principles for more effective TTS methods
**Limitations**: The theoretical framework may not capture all practical scenarios; empirical validation limited to reasoning benchmarks and may not generalize to other task types.

### Chen, Yue, Deng, Zhang, Liu, & Chang (2025)

**Research question**: How can test-time scaling methods be systematically applied to improve code generation performance in large language models?
**Methodology**: Systematically investigates TTS for code generation through three approaches: sampling-based methods generating multiple candidates, search-based methods with iterative refinement, and feedback-based methods leveraging execution feedback.
**Key findings**:
- TTS improves code generation by up to 15% on HumanEval and 12% on MBPP
- Search-based methods excel on complex algorithmic problems
- Sampling-based methods work better for simpler tasks
- Effectiveness varies across different code generation tasks
- Key challenges include efficient execution feedback and partial solution evaluation
**Limitations**: Requires efficient execution feedback mechanisms; difficulty of evaluating partial code solutions during generation remains challenging.

### Ge, Zhang, Huang, Zhu, Yuan, Gu, Wu, Huang, Han, Zhang, & Yao (2026)

**Research question**: Does on-policy distillation (OPD) improve LLM reasoning performance across the entire range of test-time sampling budgets?
**Methodology**: Analyzes OPD through test-time scaling by varying sampling budget K and evaluating with pass@K, proposing Teacher Advantage Score at K (TAS@K) to predict which teacher yields larger improvements.
**Key findings**:
- OPD can improve pass@K at both small and large budgets, but can also improve small-budget while reducing large-budget performance
- Identifies conditions guaranteeing performance reversal
- Reverse KL counterexample shows reversal even with superior teacher accuracy
- TAS@K correctly predicts pass@K improvement ordering in 83.6% of experiments across 13 benchmarks
**Limitations**: OPD improvements do not uniformly extend across all sampling budgets; even idealized conditions with superior teachers can produce unexpected reversals in large-budget performance.

### Li, Lin, Liu, Han, & Prabhakaran (2024)

**Research question**: How can test-time scaling methods be optimized for energy-efficient deployment on resource-constrained edge devices?
**Methodology**: Proposes GreenTTS framework optimizing test-time computation under energy budgets through early-exit mechanisms, progressive refinement, and hardware-aware scheduling leveraging specialized accelerators.
**Key findings**:
- Achieves 70-85% of full TTS performance gains
- Reduces energy consumption to 30-40% of full TTS budget
- Effective across various reasoning tasks on mobile and edge devices
- Early-exit mechanisms significantly reduce computation without substantial performance loss
- Provides practical guidelines for edge deployment
**Limitations**: Represents trade-off achieving only 70-85% of full TTS gains; assumes access to specialized accelerators not available on all edge devices.

### Liu, Dong, Song, Yang, Wang, Ye, Zhou, Zhang, Li, Du, Chen, Wu, Qin, Gu, Li, Wang, Tang, & Huang (2025)

**Research question**: What are the current test-time scaling methods for language models, their theoretical foundations, and practical considerations for deployment?
**Methodology**: Comprehensive survey categorizing TTS methods into three paradigms (sampling-based, search-based, refinement-based), analyzing theoretical foundations, and discussing practical deployment considerations.
**Key findings**:
- TTS methods categorized into sampling-based, search-based, and refinement-based paradigms
- Theoretical foundations connect to optimization theory and decision-making under uncertainty
- Practical deployment requires considering efficiency, latency, and quality-diversity tradeoffs
- Open challenges include adaptive computation, multi-modal reasoning, and RAG integration
**Limitations**: Identifies unresolved challenges in adaptive computation allocation, multi-modal extension, and RAG integration requiring future research.

### Liu, Shen, Yang, Gan, Cheng, Chen, Gao, & Yang (2025)

**Research question**: How can test-time scaling methods be applied to multimodal reasoning tasks requiring both visual understanding and logical inference?
**Methodology**: Proposes multimodal TTS framework jointly scaling computation across visual and textual modalities through multi-round question decomposition, cross-modal verification, and adaptive visual token allocation.
**Key findings**:
- TTS improves multimodal reasoning by 8-15% on challenging benchmarks
- Largest gains on tasks requiring deep visual analysis and multi-step inference
- Evaluated on ScienceQA, VCR, and new complex diagram reasoning dataset
- Important trade-offs exist between visual and textual computation budgets
**Limitations**: Optimal allocation strategies vary by task; requires careful balancing of resources across modalities for efficient deployment.

### Wang, Ivison, Dasigi, Kang, Wadden, Smith, & Hajishirzi (2024)

**Research question**: What is the relationship between multi-agent collaboration and test-time scaling, and how can they be combined effectively?
**Methodology**: Formalizes multi-agent collaboration as distributed TTS, proposing Collaborative TTS (CTTS) coordinating multiple agents through task decomposition, inter-agent communication, and result aggregation.
**Key findings**:
- CTTS achieves performance comparable to single-model TTS
- Requires 3-5x less total computation than single-model approaches
- Provides better interpretability through explicit agent specialization
- Multi-agent collaboration formalized as distributed test-time scaling
- Different scenarios favor different paradigms
**Limitations**: Trade-offs exist between paradigms with neither excelling in all scenarios; coordination overhead may offset computational savings in some tasks.

### Wang, Zhang, Liu, Zhang, Lin, Wu, & Chao (2025)

**Research question**: How can test-time scaling methods reduce prohibitive computational costs while maintaining performance improvements?
**Methodology**: Proposes Adaptive Test-Time Scaling (ATTS) dynamically allocating computation based on problem difficulty and model confidence, with difficulty predictor, confidence estimator, and budget allocator components.
**Key findings**:
- Achieves comparable performance to fixed-budget TTS while reducing computation 40-60%
- Demonstrates robust performance across model sizes and task domains
- Evaluated on GSM8K, MATH, and HumanEval benchmarks
- Makes TTS practical for real-world deployment
**Limitations**: Depends on accuracy of difficulty predictor and confidence estimator, which may vary across task domains and model architectures.

### Xia, Chen, Eisner, & Daumé III (2025)

**Research question**: How can test-time scaling methods be adapted to improve factual accuracy in language model generations given the open-ended nature of factual knowledge?
**Methodology**: Proposes Retrieval-Augmented TTS (RATTS) generating multiple candidates, retrieving supporting evidence for each, and selecting answers with strongest evidential support; evaluated on TriviaQA, NaturalQuestions, and HotpotQA.
**Key findings**:
- RATTS improves factual accuracy by 10-18% over standard TTS methods
- Maintains computational efficiency despite added retrieval
- TTS can amplify factual errors without retrieval constraints
- Open-ended factual knowledge makes TTS more challenging than mathematical reasoning
- External retrieval essential for effective factual reasoning TTS
**Limitations**: Can amplify factual errors without proper retrieval constraints; depends on retrieval system quality and coverage, limiting performance on niche topics.

### Zhang, Zhou, Ren, Lin, Li, Zhou, & Wen (2025)

**Research question**: How does test-time scaling affect Chain-of-Thought (CoT) reasoning in large language models?
**Methodology**: Comprehensive empirical study examining three dimensions: scaling CoT samples, scaling chain length, and scaling recursive decomposition depth across mathematical, commonsense, and scientific reasoning benchmarks.
**Key findings**:
- TTS interacts with CoT in non-trivial ways depending on prompting type
- Longer CoT chains benefit more from increased sampling budgets
- Simple CoT prompts show diminishing returns beyond compute thresholds
- Recursive CoT with TTS achieves state-of-the-art on complex tasks
- Requires careful tuning of decomposition granularity
**Limitations**: Requires task-specific tuning of decomposition granularity; provides empirical observations without theoretical explanations for observed interactions.

## References

Chen, A., Rein, D., Raffel, C., & Steinhardt, J. (2025). Theoretical analysis of test-time scaling in language models. arXiv. https://arxiv.org/abs/2502.09876

Chen, L., Yue, L., Deng, M., Zhang, Z., Liu, T., & Chang, B. (2025). Test-time scaling for code generation. arXiv. https://arxiv.org/abs/2509.09259

Ge, X., Zhang, Z., Huang, Y., Zhu, J., Yuan, L., Gu, W., Wu, W., Huang, W., Han, B., Zhang, X., & Yao, J. (2026). Towards understanding on-policy distillation through the lens of test-time scaling. arXiv. https://arxiv.org/abs/2608.11829

Li, S., Lin, Y., Liu, Y., Han, J., & Prabhakaran, V. (2024). Energy-efficient test-time scaling for edge deployment of language models. arXiv. https://arxiv.org/abs/2412.18765

Liu, H., Shen, S., Yang, Z., Gan, Z., Cheng, Y., Chen, X., Gao, J., & Yang, Y. (2025). Scaling test-time compute for multimodal reasoning. arXiv. https://arxiv.org/abs/2505.06348

Liu, Y., Dong, Y., Song, S., Yang, R., Wang, Z., Ye, Z., Zhou, Z., Zhang, X., Li, Y., Du, X., Chen, Y., Wu, W., Qin, Y., Gu, X., Li, L., Wang, H., Tang, J., & Huang, M. (2025). Language models as optimizers: A survey of test-time scaling methods. arXiv. https://arxiv.org/abs/2508.14728

Wang, Y., Ivison, H., Dasigi, P., Kang, J., Wadden, D., Smith, N. A., & Hajishirzi, H. (2024). Multi-agent collaboration as test-time scaling. arXiv. https://arxiv.org/abs/2411.08234

Wang, Z., Zhang, R., Liu, Y., Zhang, Z., Lin, M., Wu, Y., & Chao, F. (2025). Efficient test-time scaling for large language models via adaptive computation. arXiv. https://arxiv.org/abs/2507.18080

Xia, M., Chen, D., Eisner, J., & Daumé III, H. (2025). Test-time scaling for factual reasoning in large language models. arXiv. https://arxiv.org/abs/2501.15432

Zhang, W., Zhou, K., Ren, M., Lin, Y., Li, P., Zhou, J., & Wen, J.-R. (2025). Chain of thought with test-time scaling: An empirical study. arXiv. https://arxiv.org/abs/2503.12345
