# Systematic Literature Review: LLM Mid-Training

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "LLM mid-training", category cs.CL, published between 2023-10-27 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 arXiv papers on LLM mid-training published between late 2023 and late 2025. The surveyed literature reveals mid-training as an emerging paradigm positioned between pre-training and fine-tuning, characterized by multiple annealing-style phases that refine data quality, adapt optimization schedules, and extend model capabilities. Research converges on several key insights: mid-training addresses diminishing returns from noisy tokens, stabilizes convergence in late training stages, and enables more efficient use of high-quality data. However, the literature also reveals significant gaps, particularly in systematic evaluation frameworks and understanding of layer-wise dynamics during mid-training. The field shows active work in data synthesis, cross-lingual adaptation, and efficiency optimization, with practical demonstrations of substantial performance improvements across benchmarks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM mid-training", filtered to category cs.CL, published between 2023-10-27 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search parameters**: The arXiv search was conducted with the following parameters: query="LLM mid-training", category="cs.CL", start_date="2023-10-27", end_date="2026-10-26", max_results=10. The search returned exactly 10 papers across 3 batches.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search returned exactly 10 papers matching the criteria, which limits the breadth of thematic synthesis possible.

## Themes

### Theme 1: Mid-Training as a Distinct Training Paradigm

The literature establishes mid-training as a unified paradigm distinct from both pre-training and fine-tuning. Mo et al. (2025) provide the first comprehensive survey of mid-training practices, introducing a taxonomy that spans data distribution, learning-rate scheduling, and long-context extension. Their work identifies mid-training as an intermediate stage using multiple annealing-style phases to refine data quality and adapt optimization schedules, mitigating diminishing returns from noisy tokens while stabilizing convergence in late training stages. This conceptualization is supported by theoretical frameworks including gradient noise scale, the information bottleneck, and curriculum learning principles.

The effectiveness of mid-training is demonstrated through practical applications. Zhang et al. (2025) show that mid-training with synthesized QA data enables Llama-3 8B to achieve 12.74% average improvement on MMLU and CMMLU benchmarks after processing only 40B tokens. Similarly, Wang et al. (2025) demonstrate that Thinking augmented Pre-Training (TPT) can be applied during mid-training from strong open-source checkpoints, enhancing data efficiency by a factor of 3. These results collectively validate mid-training as a distinct and valuable stage in the LLM development pipeline.

### Theme 2: Data Synthesis and Quality Optimization

A significant research direction focuses on generating and curating high-quality training data for mid-training. Zhang et al. (2025) address data scarcity through a diversified synthesis pipeline that created BoostQA, a 100B-token QA dataset. Their approach uses seed data curation from heterogeneous sources, DeepSeek-R1 for STEM-focused multi-grade synthesis, and DeepSeek-V3 for answer refinement. The resulting dataset demonstrates robust scalability, with performance consistently improving as model size, data volume, and initial FLOPs scale.

Wang et al. (2025) propose an alternative approach through Thinking augmented Pre-Training (TPT), which augments existing text data with automatically generated thinking trajectories. This method makes high-quality tokens more learnable through step-by-step reasoning and decomposition, tested across diverse training configurations up to 100B tokens. The approach substantially improves LLM performance across various model sizes and families, with a 3B parameter model showing over 10% improvement on challenging reasoning benchmarks. Both approaches demonstrate that data quality and diversity are critical factors in mid-training effectiveness.

### Theme 3: Layer-Wise Representation Learning

Research reveals that different layers contribute differently to model capabilities during training, with middle layers playing a particularly important role. Harada et al. (2025) conducted massive supervised fine-tuning experiments across 1,000+ SFT models, discovering that mid-layer weight changes correlate most strongly with performance gains. Their analysis across code generation, mathematical reasoning, and general-domain tasks reveals that perplexity consistently predicts SFT effectiveness, often surpassing superficial similarity between training data and benchmarks.

Liu and Niehues (2025) extend this finding to cross-lingual transfer, discovering through analysis of over 1,000+ language pairs that middle layers exhibit the strongest potential for cross-lingual alignment. They propose a middle-layer alignment objective integrated into task-specific training, showing consistent improvements in cross-lingual transfer on slot filling, machine translation, and structured text generation. The method is robust to the choice of alignment languages and generalizes to languages unseen during alignment. These findings suggest that mid-training interventions targeting middle layers may be particularly effective.

### Theme 4: Cross-Lingual and Multilingual Adaptation

Mid-training techniques show promise for improving multilingual performance, particularly for low-resource languages. Agarwal et al. (2025) address the challenge that non-English languages show up to 29% accuracy drop compared to English even with advanced RAG systems in enterprise applications. Their batch-wise alignment strategy leverages semantically equivalent multilingual data in each training batch to directly align model outputs across languages, improving non-English accuracy by up to 23.9% without compromising English performance.

Remy et al. (2024) focus on low-resource language adaptation through trans-tokenization, a strategy that adapts high-resource monolingual LLMs to unseen target languages by initializing token embeddings using weighted averages of semantically similar token embeddings from the source language. Their approach significantly lowers data and time requirements for training high-quality models for low-resource languages. A Hydra LLM based on TowerInstruct achieved state-of-the-art machine translation for Tatar in a zero-shot manner without parallel data, demonstrating the potential of vocabulary transfer strategies during mid-training.

### Theme 5: Efficiency and Adaptive Training

Research addresses computational efficiency both during training and inference. Manvi et al. (2024) introduce adaptive inference-time compute, enabling LLMs to predict mid-generation whether restarting generation will yield better responses. Their generative self-evaluation scheme using Llama 3.1 8B increases win rate against GPT-4 on AlpacaEval from 21% to 34% with 16 samples, while achieving 74% of the improvement with only 1.2 samples on average by sampling only when beneficial. This approach enables more efficient compute utilization without requiring external reward models.

Wang et al. (2025) address training efficiency through TPT, which enhances data efficiency by a factor of 3. The method can be applied across diverse training configurations including pre-training with constrained and abundant data, as well as mid-training from strong open-source checkpoints. These efficiency-focused approaches demonstrate that mid-training can achieve substantial performance gains while reducing computational costs.

### Theme 6: Post-Training Artifacts and Behavioral Changes

Recent work examines how training choices affect model behavior and outputs, revealing unexpected artifacts. Ling et al. (2025) investigate why LLMs abstain from answering questions they are actually capable of solving, discovering that abstention can be triggered by prompt artifacts rather than genuine uncertainty. Their experiments across ten settings reveal that abstention inflation is a later-layer output override, as reasoning traces and mid-layer representations preserve correct answers. This phenomenon emerges through instruction tuning and is boosted by higher difficulty problems, though it can be mitigated at larger model sizes.

Bhattacharyya et al. (2025) examine emotion concept representation, finding that LLMs represent emotion concepts more categorically, homogeneously, and determinately than humans. This discretized nature of representations appears after mid-training and is unaffected by different post-training strategies. LLMs represent a single emotion concept with less internal diversity and place different emotions further apart, with the categorical structure remaining robust to contextual variation. These findings reveal that mid-training shapes not only task performance but also fundamental representational structures.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key points. Multiple papers agree that mid-training is a distinct and valuable stage between pre-training and fine-tuning (Mo et al., 2025; Zhang et al., 2025; Wang et al., 2025). There is consensus that data quality and diversity are critical factors, with synthesized or augmented data showing substantial benefits (Zhang et al., 2025; Wang et al., 2025). Research also converges on the importance of middle layers in representation learning and transfer (Harada et al., 2025; Liu & Niehues, 2025). Additionally, multiple papers demonstrate that efficiency improvements are achievable without sacrificing performance (Manvi et al., 2024; Wang et al., 2025).

**Disagreements**: The literature shows limited direct disagreement, partly because many papers focus on different aspects of mid-training. However, there are implicit tensions in approach. Some work emphasizes large-scale data synthesis (Zhang et al., 2025), while others focus on augmenting existing data with reasoning trajectories (Wang et al., 2025). The relative merits of these approaches—synthesis versus augmentation—remain unexplored in direct comparison. Additionally, while most papers demonstrate improvements on standard benchmarks, the work on behavioral artifacts (Ling et al., 2025; Bhattacharyya et al., 2025) raises questions about whether performance gains come with unintended representational consequences.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state their limitations in the abstract, suggesting a need for more rigorous self-assessment in the field. Second, while multiple papers demonstrate mid-training effectiveness, there is no systematic evaluation framework for comparing different mid-training approaches—Mo et al. (2025) note this gap and propose evaluation benchmarks, but comprehensive comparisons remain absent.

Third, the theoretical understanding of mid-training lags behind empirical demonstrations. While Mo et al. (2025) provide theoretical frameworks including gradient noise scale and the information bottleneck, deeper mechanistic understanding of why mid-training works remains limited. Fourth, the interaction between mid-training and safety/alignment remains underexplored—Ling et al. (2025) and Bhattacharyya et al. (2025) reveal behavioral artifacts, but systematic study of how mid-training affects model safety properties is absent.

Finally, most work focuses on English or high-resource languages, with limited exploration of mid-training for low-resource contexts beyond the vocabulary transfer approaches (Remy et al., 2024; Agarwal et al., 2025). The scalability of mid-training approaches to diverse linguistic and cultural contexts remains an open question.

## Per-Paper Annotations

### Agarwal et al. (2025)

**Research question**: How can LLMs be improved for reliable multilingual performance in enterprise applications?
**Methodology**: The authors propose a batch-wise alignment strategy for fine-tuning LLMs that leverages semantically equivalent multilingual data in each training batch to directly align model outputs across languages.
**Key findings**:
- Non-English languages show up to 29% accuracy drop compared to English even with advanced RAG systems
- The proposed method improves non-English accuracy by up to 23.9%
- The approach does not compromise English performance, model reasoning, or retrieval quality
- The method is simple to implement, scalable, and integrates seamlessly with existing LLM training and deployment pipelines
**Limitations**: not stated in abstract

### Bhattacharyya et al. (2025)

**Research question**: Do LLMs internalize emotion concepts in a way similar to humans?
**Methodology**: Using cognitive appraisal theory, the authors create a benchmark dataset of emotional scenarios spanning 15 emotion categories, elicit behavioral representations from both LLMs and humans, and study their structural similarity.
**Key findings**:
- LLMs represent emotion concepts more categorically, homogeneously, and determinately than humans
- LLMs represent a single emotion concept with less internal diversity and place different emotions further apart
- The categorical structure is robust to contextual variation including different task framing and demographic personas
- The discretized nature of representations appears after mid-training and is unaffected by different post-training strategies
**Limitations**: not stated in abstract

### Harada et al. (2025)

**Research question**: What dataset properties and training factors most influence supervised fine-tuning (SFT) effectiveness for LLM alignment?
**Methodology**: The authors trained 1,000+ SFT models across various base models and datasets (code generation, mathematical reasoning, general-domain tasks) under controlled conditions, then analyzed dataset properties and layer-wise modifications introduced by SFT.
**Key findings**:
- Some training-task synergies persist across all models while others vary substantially, emphasizing the importance of model-specific strategies
- Perplexity consistently predicts SFT effectiveness, often surpassing superficial similarity between training data and benchmarks
- Mid-layer weight changes correlate most strongly with performance gains
- The authors released 1,000+ SFT models and benchmark results to accelerate further research
- The study reveals that many aspects of SFT remain poorly understood despite its critical role in aligning LLMs with human instructions and values
**Limitations**: not stated in abstract

### Ling et al. (2025)

**Research question**: Why do LLMs abstain from answering questions they are actually capable of solving?
**Methodology**: The authors conduct experiments across ten settings by adding "Unknown" as an extra option for LLMs to choose from, and compare this to replacing "Unknown" with unrelated random words to test whether abstention is triggered by prompt artifacts rather than genuine uncertainty.
**Key findings**:
- Abstention Inflation can be triggered by the presence of an extra option, not by genuine uncertainty
- It makes models deny they can answer even when they can
- It is a later-layer output override, as reasoning traces and mid-layer representations preserve correct answers
- It is not stochastic noise but results from various factors, emerges through instruction tuning, is boosted by higher difficulty problems, and can be mitigated at larger model sizes
**Limitations**: not stated in abstract

### Liu and Niehues (2025)

**Research question**: How can cross-lingual transfer in fine-tuned LLMs be improved, especially for low-resource languages?
**Methodology**: Through analysis of LLM internal representations from over 1,000+ language pairs, the authors discover middle layers exhibit strongest cross-lingual alignment potential, then propose a middle-layer alignment objective integrated into task-specific training.
**Key findings**:
- Middle layers exhibit the strongest potential for cross-lingual alignment
- The method shows consistent improvements in cross-lingual transfer on slot filling, machine translation, and structured text generation
- Improvements are especially notable for lower-resource languages
- The method is robust to the choice of alignment languages and generalizes to languages unseen during alignment
- Separately trained alignment modules can be merged with existing task-specific modules without full re-training
**Limitations**: not stated in abstract

### Manvi et al. (2024)

**Research question**: Can LLMs predict mid-generation whether restarting generation will yield better responses, enabling more efficient inference-time compute?
**Methodology**: The authors introduce a generative self-evaluation scheme using a generative reward model formulation that allows LLMs to predict mid-generation the probability that restarting will yield better responses, trained on real unfiltered LMSYS user prompts and tested with Llama 3.1 8B.
**Key findings**:
- Llama 3.1 8B's win rate against GPT-4 on AlpacaEval increases from 21% to 34% with 16 samples using the proposed method
- Math performance on GSM8K improves from 84% to 91% with the adaptive inference approach
- 74% of the improvement from using 16 samples can be achieved with only 1.2 samples on average by sampling only when beneficial
- 50-75% of samples can be pruned early in generation with minimal degradation in performance
- The method enables more efficient and scalable compute utilization during inference without requiring an external reward model
**Limitations**: not stated in abstract

### Mo et al. (2025)

**Research question**: What is the current state of mid-training as a unified paradigm in LLM development, and how can it be systematically categorized?
**Methodology**: The authors conduct a comprehensive survey of mid-training practices, introducing a taxonomy spanning data distribution, learning-rate scheduling, and long-context extension. They synthesize practical insights from state-of-the-art systems and compile evaluation benchmarks for structured comparisons.
**Key findings**:
- Mid-training is an intermediate stage between pre-training and fine-tuning that uses multiple annealing-style phases to refine data quality, adapt optimization schedules, and extend context length
- This stage mitigates diminishing returns from noisy tokens, stabilizes convergence, and expands model capability in late training
- The effectiveness of mid-training can be explained through gradient noise scale, the information bottleneck, and curriculum learning principles
- Despite widespread use in state-of-the-art systems, there has been no prior survey of mid-training as a unified paradigm until this work
- The authors identify open challenges and propose avenues for future research and practice in mid-training
**Limitations**: not stated in abstract

### Remy et al. (2024)

**Research question**: How can cross-lingual vocabulary transfer strategies enable more efficient language adaptation of large language models for low-resource languages?
**Methodology**: The authors present trans-tokenization, a strategy that adapts a high-resource monolingual LLM to an unseen target language by initializing token embeddings using weighted averages of semantically similar token embeddings from the source language, leveraging translation resources. They validate this with Tweeties (trans-tokenized LLMs) and introduce Hydra LLMs with multiple swappable language modeling heads and embedding tables.
**Key findings**:
- Trans-tokenization enables competitive performance on downstream tasks across a diverse set of low-resource languages
- Hydra LLMs extend trans-tokenization capabilities by supporting multiple swappable language modeling heads
- A Hydra LLM based on TowerInstruct achieved state-of-the-art machine translation for Tatar in a zero-shot manner without parallel data
- The approach significantly lowers data and time requirements for training high-quality models for low-resource languages
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can the data efficiency of LLM pre-training be improved given limited high-quality data availability?
**Methodology**: The authors propose Thinking augmented Pre-Training (TPT), which augments existing text data with automatically generated thinking trajectories to make high-quality tokens more learnable through step-by-step reasoning and decomposition, tested across diverse training configurations up to 100B tokens.
**Key findings**:
- TPT enhances the data efficiency of LLM pre-training by a factor of 3
- For a 3B parameter model, TPT improves post-training performance by over 10% on several challenging reasoning benchmarks
- The method substantially improves LLM performance across various model sizes and families
- TPT can be applied across diverse training configurations including pre-training with constrained and abundant data, as well as mid-training from strong open-source checkpoints
- Augmenting text with thinking trajectories effectively increases training data volume and makes high-quality tokens more learnable
**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can large-scale, knowledge-intensive QA data be synthesized to overcome data scarcity and improve LLM mid-training performance?
**Methodology**: The authors propose a diversified synthesis pipeline to create BoostQA, a 100B-token QA dataset, using seed data curation from heterogeneous sources, DeepSeek-R1 for STEM-focused multi-grade synthesis and high-difficulty synthesis, and DeepSeek-V3 for answer refinement.
**Key findings**:
- BoostQA, a 100B-token large-scale QA dataset synthesized through their pipeline, enables Llama-3 8B mid-trained on 40B tokens to achieve an average improvement of 12.74% on MMLU and CMMLU
- The model established SOTA average performance across 12 benchmarks after mid-training with BoostQA
- The synthesis framework addresses QA data scalability and knowledge diversity challenges, particularly in cross-domain contexts
- BoostQA demonstrates robust scalability, with performance consistently improving as model size, data volume, and initial FLOPs scale
- The discipline and difficulty annotation system helps probe model deficiencies in STEM disciplines and high-difficulty data
**Limitations**: not stated in abstract

## References

Agarwal, A., Meghwani, H., Patel, H. L., Sheng, T., Ravi, S., & Roth, D. (2025). Aligning LLMs for multilingual consistency in enterprise applications. arXiv. https://arxiv.org/abs/2509.23659

Bhattacharyya, S., Kuriabov, E., Craig, L., Dilliraj, T., Adams, R. B., Li, J., & Wang, J. Z. (2025). Too categorical to be human: Emotion concepts in LLMs and humans. arXiv. https://arxiv.org/abs/2508.05880

Harada, Y., Yamauchi, Y., Oda, Y., Oseki, Y., Miyao, Y., & Takagi, Y. (2025). Massive supervised fine-tuning experiments reveal how data, layer, and training factors shape LLM alignment quality. arXiv. https://arxiv.org/abs/2506.14681

Ling, Z., Liu, S., Tang, Y., Yang, J., Fu, S., Son, S., Huang, C., Huang, K., Wan, Y., Hou, Z., & Hu, X. (2025). LLM abstention can be a prompt artifact, in addition to genuine uncertainty. arXiv. https://arxiv.org/abs/2507.16199

Liu, D., & Niehues, J. (2025). Middle-layer representation alignment for cross-lingual transfer in fine-tuned LLMs. arXiv. https://arxiv.org/abs/2502.14830

Manvi, R., Singh, A., & Ermon, S. (2024). Adaptive inference-time compute: LLMs can predict if they can do better, even mid-generation. arXiv. https://arxiv.org/abs/2410.02725

Mo, K., Shi, Y., Weng, W., Zhou, Z., Liu, S., Zhang, H., & Zeng, A. (2025). Mid-training of large language models: A survey. arXiv. https://arxiv.org/abs/2510.06826

Remy, F., Delobelle, P., Avetisyan, H., Khabibullina, A., de Lhoneux, M., & Demeester, T. (2024). Trans-tokenization and cross-lingual vocabulary transfers: Language adaptation of LLMs for low-resource NLP. arXiv. https://arxiv.org/abs/2408.04303

Wang, L., Yang, N., Huang, S., Dong, L., & Wei, F. (2025). Thinking augmented pre-training. arXiv. https://arxiv.org/abs/2509.20186

Zhang, X., Tu, C., Ren, C., Weng, R., Yan, H., Wang, J., & Cai, X. (2025). Large-scale diverse synthesis for mid-training. arXiv. https://arxiv.org/abs/2508.01326
