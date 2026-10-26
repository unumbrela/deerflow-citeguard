# Systematic Literature Review: LLM Mid-Training

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: "LLM mid-training", cs.CL category, published between 2024-10-27 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 arXiv papers on LLM mid-training published between late 2024 and late 2026. The surveyed literature reveals mid-training as an emerging paradigm positioned between pre-training and fine-tuning, focused on refining data quality, optimizing learning schedules, and extending model capabilities. Recent work demonstrates that mid-training can substantially improve model performance through diverse data synthesis, layer-wise representation alignment, and thinking-augmented approaches. The field shows convergence around the importance of middle-layer representations for cross-lingual transfer and the value of curated data during intermediate training stages. However, several gaps remain, including limited theoretical understanding of optimal mid-training strategies, insufficient exploration of computational trade-offs, and unclear guidelines for when mid-training provides the greatest benefit.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "LLM mid-training", filtered to category cs.CL, published between 2024-10-27 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Mid-Training as a Distinct Paradigm

The literature establishes mid-training as a unified paradigm distinct from both pre-training and fine-tuning. Mo et al. (2025) provide the first comprehensive taxonomy of mid-training, framing it as an intermediate stage that refines data quality, adapts optimization schedules, and extends context length. Their survey identifies mid-training's role in mitigating diminishing returns from noisy tokens and stabilizing convergence in late training stages. This conceptual framing is supported by theoretical foundations including gradient noise scale, information bottleneck theory, and curriculum learning principles.

The emergence of mid-training as a recognized stage reflects the field's maturation beyond the binary pre-training/fine-tuning dichotomy. Multiple papers implicitly adopt this framing, treating mid-training as a phase where models can be adapted with curated data before task-specific fine-tuning (Zhang et al., 2025; Wang et al., 2025).

### Theme 2: Data Quality and Diverse Synthesis

A major research direction focuses on synthesizing high-quality, diverse training data for mid-training. Zhang et al. (2025) address the scarcity of knowledge-intensive training data by proposing a diversified synthesis pipeline that created BoostQA, a 100B-token QA dataset. Their approach uses DeepSeek-R1 for STEM-focused multi-grade synthesis and achieves state-of-the-art performance across 12 benchmarks, with Llama-3 8B showing 12.74% average improvement on MMLU and CMMLU after mid-training on 40B tokens.

Wang et al. (2025) introduce Thinking augmented Pre-Training (TPT), which augments text with automatically generated thinking trajectories to make high-quality tokens more learnable. Their method improves data efficiency by a factor of 3 and enhances post-training performance by over 10% on challenging reasoning benchmarks for a 3B parameter model. Both approaches emphasize that data quality during mid-training is more critical than sheer quantity.

### Theme 3: Middle-Layer Representation Alignment

Multiple papers identify middle layers as crucial for cross-lingual and cross-domain transfer. Liu and Niehues (2025) analyzed over 1,000 language pairs and found that middle layers exhibit the strongest potential for cross-lingual alignment. Their middle-layer alignment objective, integrated into task-specific training, shows consistent improvements especially for lower-resource languages.

Harada et al. (2025) similarly found that mid-layer weight changes correlate most strongly with performance gains in their massive supervised fine-tuning experiments involving 1,000+ models. Bhattacharyya et al. (2025) discovered that the categorical structure of emotion representations in LLMs appears after the mid-training stage and remains unaffected by different post-training strategies, suggesting mid-training shapes fundamental representational properties.

### Theme 4: Efficiency and Adaptive Compute

Several papers address computational efficiency during training and inference. Manvi et al. (2024) introduce adaptive inference-time compute, enabling LLMs to predict mid-generation whether restarting will yield better responses. Their approach achieves 74% of the improvement from using 16 samples with only 1.2 samples on average, and can prune 50-75% of samples early with minimal performance degradation.

Remy et al. (2024) propose trans-tokenization for efficient language adaptation, bypassing the need for high-quality parallel data. Their approach lowers data and time requirements for training, enabling LLM development for low-resource languages like Tatar where they achieved state-of-the-art machine translation in zero-shot manner.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key findings. First, middle layers play a critical role in model adaptation and cross-lingual transfer (Liu & Niehues, 2025; Harada et al., 2025; Bhattacharyya et al., 2025). Second, data quality during mid-training substantially impacts final performance, with curated or synthesized data outperforming raw scale (Zhang et al., 2025; Wang et al., 2025). Third, mid-training represents a distinct paradigm with unique characteristics requiring specialized strategies (Mo et al., 2025).

**Disagreements**: The literature shows limited direct disagreement, as most papers focus on different aspects of mid-training rather than competing claims. However, there is variation in emphasis: some work prioritizes data synthesis (Zhang et al., 2025), while others focus on architectural interventions (Liu & Niehues, 2025) or efficiency optimizations (Manvi et al., 2024). The relative importance of these approaches remains an open question.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, theoretical understanding of optimal mid-training strategies remains limited—most papers provide empirical results without rigorous theoretical frameworks (Mo et al., 2025; Zhang et al., 2025). Second, computational trade-offs are insufficiently explored; while efficiency gains are reported, the overhead of data synthesis and trajectory generation is rarely quantified (Wang et al., 2025). Third, guidelines for when mid-training provides the greatest benefit are unclear, with limited guidance on model size, data volume, or domain-specific considerations.

Additional gaps include: limited exploration of mid-training's impact on model safety and alignment; insufficient study of how mid-training interacts with different post-training strategies; and sparse investigation of mid-training for multimodal models beyond text-only LLMs. Several papers note limitations "not stated in abstract," suggesting that detailed limitations may be underreported (Ling et al., 2025; Agarwal et al., 2025).

## Per-Paper Annotations

### Agarwal et al. (2025)

**Research question**: How can LLMs be aligned to reduce performance gaps between high-resource and mid/low-resource languages in enterprise applications?
**Methodology**: The authors propose a batch-wise alignment strategy for fine-tuning LLMs, leveraging semantically equivalent multilingual data in each training batch to directly align model outputs across languages.
**Key findings**:
- Advanced RAG systems show up to 29% accuracy drop in non-English languages compared to English
- The batch-wise alignment approach improves non-English accuracy by up to 23.9%
- The method does not compromise English performance, model reasoning, or retrieval quality
- The approach is simple to implement, scalable, and integrates seamlessly with existing LLM training and deployment pipelines
**Limitations**: Not stated in abstract

### Bhattacharyya et al. (2025)

**Research question**: Do LLMs internalize emotion concepts in a way similar to humans?
**Methodology**: Using cognitive appraisal theory, the authors created a benchmark dataset of emotional scenarios spanning 15 emotion categories and elicited behavioral representations of emotion concepts from both LLMs and humans to study their structural similarity.
**Key findings**:
- LLMs represent emotion concepts more categorically, homogeneously, and determinately than humans
- LLMs represent a single emotion concept with less internal diversity and place different emotions further apart
- The categorical structure of representations in LLMs is robust to contextual variation, including different task framing and demographic personas
- The discretized nature of representations appears after the mid-training stage and is unaffected by different post-training strategies
**Limitations**: Not stated in abstract

### Harada et al. (2025)

**Research question**: What dataset properties and layer-wise modifications most significantly influence SFT effectiveness across different LLMs?
**Methodology**: The authors trained 1,000+ SFT models under controlled conditions across various base models and datasets including code generation, mathematical reasoning, and general-domain tasks. They analyzed dataset properties, examined layer-wise modifications, and evaluated perplexity as a predictor of SFT effectiveness.
**Key findings**:
- Some training-task synergies persist across all models while others vary substantially, emphasizing the importance of model-specific strategies
- Perplexity consistently predicts SFT effectiveness, often surpassing superficial similarity between training data and benchmarks
- Mid-layer weight changes correlate most strongly with performance gains
- The study released 1,000+ SFT models and benchmark results to accelerate further research
- Different models respond differently to the same training tasks, requiring model-specific alignment strategies
**Limitations**: The controlled experimental conditions may not capture all real-world SFT scenarios

### Ling et al. (2025)

**Research question**: Can LLM abstention be triggered by prompt artifacts rather than genuine uncertainty?
**Methodology**: The authors conducted experiments across ten settings, adding "Unknown" as an extra option or replacing it with unrelated random words in True/False Questions to test whether abstention is a surface pattern imitation rather than genuine uncertainty expression.
**Key findings**:
- Abstention Inflation can be triggered by the presence of an extra option, not by genuine uncertainty
- LLMs deny they can answer even when they can, due to prompt-induced abstention
- Abstention is a later-layer output override, with reasoning traces and mid-layer representations preserving correct answers
- Abstention results from various factors, emerges through instruction tuning, is boosted by higher problem difficulty, and can be mitigated at larger model sizes
**Limitations**: Not stated in abstract

### Liu and Niehues (2025)

**Research question**: Can middle-layer representation alignment improve cross-lingual transfer in fine-tuned LLMs?
**Methodology**: Through analysis of internal representations from over 1,000+ language pairs, the authors identified middle layers as having the strongest potential for cross-lingual alignment, then proposed a middle-layer alignment objective integrated into task-specific training, tested on slot filling, machine translation, and structured text generation.
**Key findings**:
- Middle layers exhibit the strongest potential for cross-lingual alignment across 1,000+ language pairs
- The middle-layer alignment objective shows consistent improvements in cross-lingual transfer, especially to lower-resource languages
- The method is robust to the choice of alignment languages and generalizes to languages unseen during alignment
- Separately trained alignment modules can be merged with existing task-specific modules, improving cross-lingual capabilities without full re-training
**Limitations**: Not stated in abstract

### Manvi et al. (2024)

**Research question**: Can LLMs predict mid-generation whether restarting generation will yield better responses, enabling adaptive and efficient inference-time compute?
**Methodology**: The authors introduce a generative self-evaluation scheme using a generative reward model formulation that allows LLMs to predict mid-generation the probability that restarting will yield better responses. They trained the model using a dataset constructed with real unfiltered LMSYS user prompts and evaluated on AlpacaEval and GSM8K benchmarks.
**Key findings**:
- Llama 3.1 8B's win rate against GPT-4 on AlpacaEval increased from 21% to 34% with 16 samples
- Math performance on GSM8K improved from 84% to 91%
- 74% of the improvement from using 16 samples can be achieved with only 1.2 samples on average through adaptive sampling
- 50-75% of samples can be pruned early in generation with minimal degradation in performance
- The approach requires no external reward model and is inexpensive, involving generating only a single predefined token
**Limitations**: The training data dependency on LMSYS user prompts and generalization to other domains is not discussed

### Mo et al. (2025)

**Research question**: What is the current state of mid-training as a unified paradigm in LLM development, and how can it be systematically categorized?
**Methodology**: This paper conducts a comprehensive survey of mid-training practices, introducing a taxonomy spanning data distribution, learning-rate scheduling, and long-context extension. The authors synthesize practical insights, compile evaluation benchmarks, and analyze theoretical foundations including gradient noise scale, information bottleneck, and curriculum learning.
**Key findings**:
- Mid-training is an intermediate stage between pre-training and fine-tuning that refines data quality, adapts optimization schedules, and extends context length
- This stage mitigates diminishing returns from noisy tokens and stabilizes convergence in late training
- The effectiveness of mid-training can be explained through gradient noise scale, information bottleneck, and curriculum learning theories
- The paper introduces the first taxonomy of LLM mid-training covering data distribution, learning-rate scheduling, and long-context extension
- The survey compiles evaluation benchmarks and reports gains to enable structured comparisons across models
**Limitations**: The paper identifies open challenges and proposes avenues for future research, though specific limitations of existing mid-training approaches are not detailed in the abstract

### Remy et al. (2024)

**Research question**: How can cross-lingual vocabulary transfer strategies enable more efficient language adaptation of LLMs for low-resource languages?
**Methodology**: The authors propose trans-tokenization, a strategy that adapts a high-resource monolingual LLM to an unseen target language by initializing target language token embeddings using weighted averages of semantically similar source language token embeddings, leveraging translation resources. They validate the method with Tweeties (trans-tokenized LLMs) and introduce Hydra LLMs with multiple swappable language modeling heads.
**Key findings**:
- Trans-tokenization enables competitive performance on downstream tasks across a diverse set of low-resource languages
- Hydra LLMs extend trans-tokenization capabilities by supporting multiple swappable language modeling heads and embedding tables
- A Hydra LLM based on TowerInstruct achieved state-of-the-art machine translation for Tatar in a zero-shot manner
- The approach bypasses the need for high-quality parallel data, which is particularly valuable for languages like Tatar where such data is scarce
- Trans-tokenization lowers data and time requirements for training high-quality models, enabling LLM development for a wider range of languages
**Limitations**: Validation on a small but diverse set of languages suggests limited language coverage in the evaluation; broader scalability and performance across more languages remains to be demonstrated

### Wang et al. (2025)

**Research question**: How can thinking trajectories be used to augment training data and improve the data efficiency of LLM pre-training?
**Methodology**: The authors propose Thinking augmented Pre-Training (TPT), which augments text with automatically generated thinking trajectories to make high-quality tokens more learnable through step-by-step reasoning. They applied TPT across diverse training configurations up to 100B tokens, including pre-training with constrained and abundant data, and mid-training from strong open-source checkpoints.
**Key findings**:
- TPT substantially improves LLM performance across various model sizes and families
- The method enhances data efficiency of LLM pre-training by a factor of 3
- For a 3B parameter model, TPT improves post-training performance by over 10% on several challenging reasoning benchmarks
- Thinking trajectories make high-quality tokens more learnable by decomposing complex reasoning into step-by-step processes
- TPT is a universal methodology applicable across diverse training configurations including mid-training
**Limitations**: The computational overhead of generating thinking trajectories is not discussed

### Zhang et al. (2025)

**Research question**: How can large-scale diverse QA data be synthesized to overcome scarcity of high-quality, knowledge-intensive training data for LLM mid-training?
**Methodology**: The authors propose a diversified synthesis pipeline to create BoostQA, a 100B-token QA dataset. The framework curates seed data from heterogeneous sources, uses DeepSeek-R1 for STEM-focused multi-grade and high-difficulty synthesis, and refines answers via DeepSeek-V3. The dataset is then used in mid-training to optimize domain-specific knowledge acquisition.
**Key findings**:
- BoostQA, a 100B-token synthesized QA dataset, was created using a novel diversified pipeline
- Llama-3 8B mid-trained on a 40B-token dataset achieved an average improvement of 12.74% on MMLU and CMMLU
- The method established SOTA average performance across 12 benchmarks
- BoostQA demonstrates robust scalability, with performance consistently improving as model size, data volume, and initial FLOPs scale
- The approach addresses QA data scalability and knowledge diversity challenges, particularly in cross-domain and STEM contexts
**Limitations**: The abstract does not explicitly state limitations of the synthesis approach or potential biases in the generated data

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
