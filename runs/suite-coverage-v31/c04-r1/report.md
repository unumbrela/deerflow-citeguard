# Systematic Literature Review: LLM Mid-Training

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: LLM Mid-Training, cs.CL, published between 2023-10-27 and 2025-10-27
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 arXiv papers on LLM Mid-Training published between October 2023 and October 2025. The surveyed literature reveals mid-training as an emerging critical stage bridging pre-training and post-training in foundation model development. Research converges on defining mid-training as a distinct optimization phase involving data curation, learning-rate scheduling, and capability enhancement. Key themes include systematic capability development (mathematics, coding, reasoning), large-scale data synthesis approaches, and middle-layer representation alignment for cross-lingual transfer. The field demonstrates growing maturity with comprehensive taxonomies, practical frameworks, and empirical validation across multiple benchmarks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM Mid-Training", filtered to category cs.CL, published between 2023-10-27 and 2025-10-27. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Formal Definition and Taxonomy of Mid-Training

The literature establishes mid-training as a formally defined stage in LLM development. Tu et al. (2025) provide the first comprehensive survey that formally defines mid-training and analyzes optimization frameworks encompassing data curation, training strategies, and model architecture. Mo et al. (2025) introduce the first taxonomy spanning data distribution, learning-rate scheduling, and long-context extension, explaining effectiveness through gradient noise scale, information bottleneck, and curriculum learning principles. These foundational works position mid-training as involving multiple annealing-style phases that refine data quality, adapt optimization schedules, and expand model capability in late training, mitigating diminishing returns from noisy tokens while stabilizing convergence.

### Theme 2: Large-Scale Data Synthesis for Capability Enhancement

A significant research direction focuses on synthesizing large-scale, diverse training data for mid-training. Zhang et al. (2025) propose a novel diversified pipeline to synthesize BoostQA, a 100B-token QA dataset that achieves state-of-the-art performance across 12 benchmarks. Their approach curates seed data from heterogeneous sources, utilizes advanced models for STEM-focused multi-grade synthesis, and demonstrates robust scalability with performance improving as model size, data volume, and initial FLOPs scale. Wang et al. (2025) introduce Thinking augmented Pre-Training (TPT), which augments text data with automatically generated thinking trajectories, improving data efficiency by a factor of 3 and enhancing post-training performance by over 10% on challenging reasoning benchmarks for 3B parameter models.

### Theme 3: Middle-Layer Representation and Alignment

Multiple papers investigate middle-layer representations as critical for model capability and transfer. Harada et al. (2025) conduct massive supervised fine-tuning experiments revealing that mid-layer weight changes correlate most strongly with performance gains, with perplexity consistently predicting fine-tuning effectiveness. Liu and Niehues (2025) discover that middle layers exhibit the strongest potential for cross-lingual alignment among internal representations, proposing a middle-layer alignment objective that shows consistent improvements in cross-lingual transfer, especially for lower-resource languages. Bhattacharyya et al. (2025) find that the categorical structure of emotion representations in LLMs appears after the mid-training stage and remains unaffected by different post-training strategies, suggesting mid-training shapes fundamental representational properties.

### Theme 4: Adaptive and Efficient Training Strategies

Research explores adaptive strategies to optimize mid-training efficiency and outcomes. Manvi et al. (2024) demonstrate that LLMs can predict mid-generation whether restarting will yield better responses, enabling adaptive inference-time compute that achieves 74% of improvement from 16 samples using only 1.2 samples on average. This generative self-evaluation scheme allows pruning 50-75% of samples early with minimal performance degradation. Such adaptive approaches complement mid-training by enabling more efficient capability development and resource utilization.

### Theme 5: Multilingual and Cross-Lingual Applications

Mid-training research increasingly addresses multilingual consistency and cross-lingual transfer. Agarwal et al. (2025) propose batch-wise alignment strategies leveraging semantically equivalent multilingual data to reduce performance gaps between high-resource and mid/low-resource languages, improving non-English accuracy by up to 23.9% without compromising English performance. Liu and Niehues (2025) show their middle-layer alignment method is robust to alignment language choice and generalizes to languages unseen during alignment, with separately trained modules mergeable with existing task-specific modules without full re-training.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that mid-training is a distinct and critical stage in LLM development, not merely an extension of pre-training. Multiple papers converge on the importance of data quality and curation over sheer quantity, with systematic data synthesis approaches showing consistent improvements. There is strong agreement that middle-layer representations play a crucial role in capability development and transfer, with multiple independent studies identifying mid-layer changes as correlating with performance gains.

**Disagreements**: The literature shows some tension between approaches focusing on large-scale data synthesis versus those emphasizing architectural or representational interventions. While Zhang et al. (2025) demonstrate success with 100B-token datasets, Wang et al. (2025) achieve substantial gains through thinking augmentation that effectively increases training data volume without requiring massive raw data collection. Additionally, papers differ in their emphasis on domain-specific versus general capability development, with some focusing on specialized domains like mathematics and coding, while others target broader cross-lingual or emotional understanding capabilities.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either insufficient space allocation or under-emphasis on constraint acknowledgment. Second, while multiple papers identify middle-layer importance, there is limited theoretical explanation for why mid-layers specifically (rather than early or late layers) show the strongest alignment potential. Third, the literature lacks comprehensive studies on computational efficiency trade-offs between different mid-training approaches, particularly comparing large-scale data synthesis versus architectural interventions. Fourth, there is limited investigation into how mid-training strategies interact with different model sizes and architectures beyond empirical demonstrations. Finally, the field would benefit from standardized benchmarks specifically designed for evaluating mid-training effectiveness, as current evaluations span disparate tasks and domains.

## Per-Paper Annotations

### Agarwal et al. (2025)

**Research question**: How can performance gaps between high-resource and mid/low-resource languages in LLMs be reduced for enterprise applications?
**Methodology**: The authors propose a batch-wise alignment strategy for fine-tuning LLMs that leverages semantically equivalent multilingual data in each training batch to directly align model outputs across languages, and evaluate its impact on non-English accuracy.
**Key findings**:
- Advanced RAG systems show up to 29% accuracy drop in non-English languages compared to English
- The batch-wise alignment approach improves non-English accuracy by up to 23.9%
- The method does not compromise English performance, model reasoning, or retrieval quality
- The approach is simple to implement, scalable, and integrates seamlessly with existing LLM training and deployment pipelines
**Limitations**: not stated in abstract

### Bhattacharyya et al. (2025)

**Research question**: Do LLMs internalize emotion concepts in a way similar to humans?
**Methodology**: The authors create a benchmark dataset of emotional scenarios spanning 15 emotion categories based on cognitive appraisal theory, then elicit behavioral representations of emotion concepts from both LLMs and humans to study their structural similarity.
**Key findings**:
- LLMs represent emotion concepts more categorically, homogeneously, and determinately than humans
- LLMs represent a single emotion concept with less internal diversity and place different emotions further apart
- The categorical structure of representations in LLMs is robust to contextual variation, including different task framing and demographic personas
- The discretized nature of emotion representations appears after the mid-training stage and is unaffected by different post-training strategies
- LLMs curb the subjectivity inherent to the human experience of emotions
**Limitations**: not stated in abstract

### Harada et al. (2025)

**Research question**: What dataset properties and layer-wise modifications most significantly influence supervised fine-tuning effectiveness for LLM alignment?
**Methodology**: The study trained over 1,000 SFT models across a wide range of base models on various datasets including code generation, mathematical reasoning, and general-domain tasks under controlled conditions. It identified critical dataset properties and examined layer-wise modifications introduced by SFT to determine factors shaping alignment quality.
**Key findings**:
- Some training-task synergies persist across all models while others vary substantially, emphasizing the importance of model-specific strategies
- Perplexity consistently predicts SFT effectiveness, often surpassing superficial similarity between training data and benchmarks
- Mid-layer weight changes correlate most strongly with performance gains
- The study releases 1,000+ SFT models and benchmark results to accelerate further research
**Limitations**: not stated in abstract

### Liu and Niehues (2025)

**Research question**: How can cross-lingual transfer in fine-tuned LLMs be improved, especially for lower-resource languages?
**Methodology**: Through analysis of internal representations from over 1,000+ language pairs, the authors discover that middle layers exhibit the strongest potential for cross-lingual alignment, and propose a middle-layer alignment objective integrated into task-specific training, evaluated on slot filling, machine translation, and structured text generation.
**Key findings**:
- Middle layers exhibit the strongest potential for cross-lingual alignment among LLM internal representations
- The middle-layer alignment method shows consistent improvements in cross-lingual transfer, especially to lower-resource languages
- The method is robust to the choice of alignment languages and generalizes to languages unseen during alignment
- Separately trained alignment modules can be merged with existing task-specific modules, improving cross-lingual capabilities without full re-training
**Limitations**: not stated in abstract

### Manvi et al. (2024)

**Research question**: Can LLMs predict mid-generation whether restarting generation will yield better responses, enabling adaptive and efficient inference-time compute?
**Methodology**: The paper introduces a generative self-evaluation scheme that allows LLMs to predict mid-generation the probability that restarting will yield a better response, without requiring an external reward model. The approach was trained using a dataset constructed with real unfiltered LMSYS user prompts and tested on Llama 3.1 8B.
**Key findings**:
- LLMs can predict mid-generation the probability that restarting generation will yield a better response using a generative reward model formulation
- Llama 3.1 8B's win rate against GPT-4 on AlpacaEval increased from 21% to 34% with 16 samples
- Math performance on GSM8K improved from 84% to 91%
- 74% of the improvement from using 16 samples can be achieved with only 1.2 samples on average through adaptive sampling
- 50-75% of samples can be pruned early in generation with minimal degradation in performance
**Limitations**: not stated in abstract

### Mo et al. (2025)

**Research question**: What is the unified paradigm of LLM mid-training and how can it be taxonomically organized across data distribution, learning-rate scheduling, and long-context extension?
**Methodology**: This paper introduces the first taxonomy of LLM mid-training spanning data distribution, learning-rate scheduling, and long-context extension. It distills practical insights, compiles evaluation benchmarks, and reports gains to enable structured comparisons across models, while identifying open challenges and proposing future research avenues.
**Key findings**:
- Mid-training involves multiple annealing-style phases that refine data quality, adapt optimization schedules, and extend context length
- This stage mitigates diminishing returns from noisy tokens, stabilizes convergence, and expands model capability in late training
- Effectiveness can be explained through gradient noise scale, the information bottleneck, and curriculum learning, which together promote generalization and abstraction
- The paper provides the first unified taxonomy of mid-training as a paradigm
- Practical insights and evaluation benchmarks are compiled to enable structured comparisons across models
**Limitations**: not stated in abstract

### Tu et al. (2025)

**Research question**: How can mid-training for large language models be formally defined and optimized across data curation, training strategies, and model architecture?
**Methodology**: The paper provides a comprehensive survey that formally defines mid-training for LLMs and analyzes optimization frameworks encompassing data curation, training strategies, and model architecture. It examines mainstream model implementations through objective-driven interventions to illustrate mid-training's role in progressive LLM capability development.
**Key findings**:
- Mid-training emerges as a vital stage bridging pre-training and post-training in foundation model development
- Mid-training systematically enhances specified capabilities such as mathematics, coding, reasoning, and long-context extension while maintaining foundational competencies
- The survey offers a comprehensive taxonomy and actionable insights for mid-training optimization frameworks
- Mid-training serves as a distinct and critical stage in the progressive development of LLM capabilities
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can the data efficiency of large language model pre-training be improved given limited high-quality training data?
**Methodology**: The authors propose Thinking augmented Pre-Training (TPT), which augments text data with automatically generated thinking trajectories to make high-quality tokens more learnable through step-by-step reasoning. They evaluate TPT across diverse training configurations up to 100B tokens, including pre-training with constrained and abundant data, and mid-training from strong open-source checkpoints.
**Key findings**:
- TPT substantially improves LLM performance across various model sizes and families
- The method enhances data efficiency of LLM pre-training by a factor of 3
- For a 3B parameter model, TPT improves post-training performance by over 10% on several challenging reasoning benchmarks
- Thinking augmentation effectively increases training data volume and makes high-quality tokens more learnable
**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can large-scale QA data synthesis overcome limitations in scalability and knowledge diversity to improve mid-training for LLMs?
**Methodology**: The authors propose a novel diversified pipeline to synthesize BoostQA, a 100B-token large-scale QA dataset. The framework curates seed data from heterogeneous sources, utilizes DeepSeek-R1 for STEM-focused multi-grade and high-difficulty synthesis, and refines answers via DeepSeek-V3. The dataset is then used in mid-training to optimize domain-specific knowledge acquisition.
**Key findings**:
- BoostQA is a 100B-token large-scale QA dataset synthesized through a novel diversified pipeline
- Llama-3 8B mid-trained on a 40B-token dataset achieved an average improvement of 12.74% on MMLU and CMMLU
- The method established SOTA average performance across 12 benchmarks
- BoostQA demonstrates robust scalability, with performance consistently improving as model size, data volume, and initial FLOPs scale
- The approach addresses challenges in QA data scalability and knowledge diversity, particularly in cross-domain contexts
**Limitations**: not stated in abstract

### Ling et al. (2025)

**Research question**: Is LLM abstention behavior always an expression of genuine uncertainty, or can it be triggered by prompt artifacts?
**Methodology**: The authors conduct ten experimental settings examining LLM abstention behavior, including adding 'Unknown' as an extra option for True/False Questions and replacing it with unrelated random words to test whether abstention is triggered by prompt structure rather than genuine uncertainty.
**Key findings**:
- Abstention Inflation can be triggered by the presence of an extra option, not by genuine uncertainty
- LLMs deny they can answer questions even when they are capable of solving them
- Abstention is a later-layer output override, as reasoning traces and mid-layer representations preserve correct answers
- The phenomenon results from various factors, emerges through instruction tuning, is boosted by higher problem difficulty, and can be mitigated at larger model sizes
- LLMs are trained to imitate the surface pattern of abstention rather than to express genuine uncertainty
**Limitations**: not stated in abstract

## References

Agarwal, A., Meghwani, H., Patel, H. L., Sheng, T., Ravi, S., & Roth, D. (2025). Aligning LLMs for multilingual consistency in enterprise applications. arXiv. https://arxiv.org/abs/2509.23659

Bhattacharyya, S., Kuriabov, E., Craig, L., Dilliraj, T., Adams, R. B., Li, J., & Wang, J. Z. (2025). Too categorical to be human: Emotion concepts in LLMs and humans. arXiv. https://arxiv.org/abs/2508.05880

Harada, Y., Yamauchi, Y., Oda, Y., Oseki, Y., Miyao, Y., & Takagi, Y. (2025). Massive supervised fine-tuning experiments reveal how data, layer, and training factors shape LLM alignment quality. arXiv. https://arxiv.org/abs/2506.14681

Ling, Z., Liu, S., Tang, Y., Yang, J., Fu, S., Son, S., Huang, C., Huang, K., Wan, Y., Hou, Z., & Hu, X. (2025). LLM abstention can be a prompt artifact, in addition to genuine uncertainty. arXiv. https://arxiv.org/abs/2507.16199

Liu, D., & Niehues, J. (2025). Middle-layer representation alignment for cross-lingual transfer in fine-tuned LLMs. arXiv. https://arxiv.org/abs/2502.14830

Manvi, R., Singh, A., & Ermon, S. (2024). Adaptive inference-time compute: LLMs can predict if they can do better, even mid-generation. arXiv. https://arxiv.org/abs/2410.02725

Mo, K., Shi, Y., Weng, W., Zhou, Z., Liu, S., Zhang, H., & Zeng, A. (2025). Mid-training of large language models: A survey. arXiv. https://arxiv.org/abs/2510.06826

Tu, C., Zhang, X., Weng, R., Li, R., Zhang, C., Bai, Y., Yan, H., Wang, J., & Cai, X. (2025). A survey on LLM mid-training. arXiv. https://arxiv.org/abs/2510.23081

Wang, L., Yang, N., Huang, S., Dong, L., & Wei, F. (2025). Thinking augmented pre-training. arXiv. https://arxiv.org/abs/2509.20186

Zhang, X., Tu, C., Ren, C., Weng, R., Yan, H., Wang, J., & Cai, X. (2025). Large-scale diverse synthesis for mid-training. arXiv. https://arxiv.org/abs/2508.01326
