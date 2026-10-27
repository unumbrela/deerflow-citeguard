# Systematic Literature Review: Mid-Training Techniques for Large Language Models

**Date:** October 27, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Time Period:** October 27, 2023 – October 26, 2025

---

## Abstract

Mid-training has emerged as a critical phase in large language model development, positioned between initial pre-training and final fine-tuning. This systematic literature review examines 10 influential papers published between 2023-2025 that investigate mid-training strategies, data curation methods, and training schedules for enhancing LLM capabilities. We identify five key themes: (1) multi-stage training processes with evolving data mixtures, (2) data quality prioritization over quantity, (3) domain-specific continual pre-training, (4) learning rate scheduling strategies, and (5) mid-training's impact on downstream reinforcement learning performance. Our analysis reveals that successful mid-training approaches emphasize instance-level data optimization, performance-driven interventions, and careful alignment between mid-training data distributions and downstream task requirements. We discuss limitations and future research directions for advancing mid-training methodologies.

**Keywords:** mid-training, large language models, continual pre-training, data curation, reinforcement learning

---

## 1. Introduction

The rapid advancement of large language models (LLMs) has fundamentally transformed natural language processing capabilities. As models scale in size and training data expands, researchers have identified a critical intermediate phase—mid-training—that bridges initial pre-training and task-specific fine-tuning. Mid-training encompasses various strategies including continual pre-training on domain-specific corpora, multi-stage training with evolving data mixtures, and targeted interventions to address capability bottlenecks.

This systematic literature review synthesizes recent research on LLM mid-training techniques, focusing on papers published between October 2023 and October 2025 in the cs.CL category. We analyze 10 influential studies that collectively advance understanding of how mid-training strategies impact model performance across reasoning, coding, multilingual capabilities, and context extension.

Our review addresses three research questions:
1. **RQ1:** What are the predominant mid-training strategies employed across recent LLM development?
2. **RQ2:** How do data curation and mixing approaches during mid-training affect downstream capabilities?
3. **RQ3:** What is the relationship between mid-training and subsequent reinforcement learning performance?

---

## 2. Methods

### 2.1 Search Strategy

We conducted a systematic search of arXiv preprints in the cs.CL (Computational Linguistics) category for papers published between October 27, 2023 and October 26, 2025. The search query "LLM mid-training" identified 32 papers, with an additional 104 papers collected from reference citations. After shortlisting and screening based on relevance to mid-training techniques, methods, and analysis, 10 papers were included for final review.

### 2.2 Inclusion Criteria

Papers were included if they:
- Explicitly discussed mid-training, continual pre-training, or multi-stage training strategies
- Provided empirical evaluation of training methodologies
- Focused on large language models (≥1B parameters)
- Were published in the cs.CL category within the specified time window

### 2.3 Data Extraction and Synthesis

For each included paper, we extracted information on: model architectures, training data composition, training schedules, learning rate strategies, evaluation benchmarks, and key findings. Papers were analyzed for common patterns, divergent approaches, and methodological innovations in mid-training.

---

## 3. Results

### 3.1 Included Studies Overview

The 10 included papers span various model families and focus areas:

| Paper | Model | Training Tokens | Key Contribution |
|-------|-------|-----------------|------------------|
| OctoThinker (2506.20512) | Llama-3.2-1B/3B | 220B | Two-stage "Stable-then-Decay" strategy |
| DeepSeekMath (2402.03300) | DeepSeek-LLM 7B | 120B | Iterative math corpus collection |
| SmolLM2 (2502.02737) | SmolLM2-1.7B | 11T | Performance-driven 4-stage training |
| Qwen2.5 (2412.15115) | Qwen2.5 series | 18T | LLM-filtered data quality improvements |
| Qwen3 (2505.09388) | Qwen3 series | 36T | Instance-level data optimization |
| Tower (2402.17733) | TowerBase-7B/13B | 20B | Multilingual parallel sentence integration |
| LLaMAX (2407.05975) | LLaMA-2 variants | Varies | Vocabulary expansion for multilingual |
| Magicoder (2312.02120) | CodeLlama-7B | 75K synthetic | OSS-Instruct code generation |
| Phi-3 (2404.14219) | Phi-3-mini | 3.3T | Quality-filtered two-phase training |
| MATES (2406.06046) | LLaMA-2-410M/1B | Varies | Model-aware data selection with influence models |

### 3.2 Theme 1: Multi-Stage Training with Evolving Data Mixtures

Four studies explicitly employed multi-stage training approaches where data mixtures evolved across phases:

**OctoThinker** introduced a two-stage "Stable-then-Decay" mid-training strategy. In the Stable stage, models train on high-quality web corpora (MegaMath-Web-Pro-Max, DCLM-Baselines) with constant learning rate for 200B tokens. The Decay stage branches into three variants (Long/Short/Hybrid reasoning) with cosine learning rate decay [citation:OctoThinker](https://arxiv.org/abs/2506.20512).

**SmolLM2** implemented four training phases across 11 trillion tokens with performance-driven interventions. Stage 1 (0-6T) used 60% FineWeb-Edu/40% DCLM with 10% code; Stage 2 (6-8T) added 5% math and increased code to 20%; Stage 3 (8-10T) incorporated 10% math and adjusted web ratios; Stage 4 (10-11T) featured 14% math, 24% code, and 58% English web during the final 10% learning rate decay [citation:SmolLM2](https://arxiv.org/abs/2502.02737).

**Qwen3** employed three distinct stages: General Stage (30T+ tokens, 4k sequence length), Reasoning Stage (5T higher-quality STEM/coding/synthetic data with accelerated learning rate decay), and Long Context Stage (hundreds of billions of tokens, 32k sequence length with RoPE base frequency 1M) [citation:Qwen3](https://arxiv.org/abs/2505.09388).

**Phi-3** trained on 3.3T tokens in two disjoint sequential phases: Phase-1 comprised web sources for general knowledge and language understanding, while Phase-2 merged heavily filtered webdata with synthetic data for logical reasoning and niche skills [E5][citation:Phi-3](https://arxiv.org/abs/2404.14219).

### 3.3 Theme 2: Data Quality Over Quantity

Multiple studies emphasized data quality curation over raw token volume:

**OctoThinker** developed MegaMath-Web-Pro-Max using a two-stage curation process: fastText classifier recall followed by Llama-3.1-70B-instruct refinement, resulting in 5.5× more tokens than MegaMath-Web-Pro while maintaining comparable quality [citation:OctoThinker](https://arxiv.org/abs/2506.20512).

**Qwen2.5** expanded from 7T to 18T tokens using Qwen2-Instruct models as multi-dimensional quality filters, specialized math/code data integration from Qwen2.5-Math and Qwen2.5-Coder, and synthetic data with reward model filtering [citation:Qwen2.5](https://arxiv.org/abs/2412.15115).

**Qwen3** introduced instance-level data optimization through a multilingual annotation system across 30T tokens, evaluating educational value, fields, domains, and safety. This approach optimizes mixtures at the instance level via proxy model ablations, contrasting with prior source-level or domain-level optimization [citation:Qwen3](https://arxiv.org/abs/2505.09388).

**DeepSeekMath** employed an iterative corpus collection pipeline using fastText classifiers trained on seed corpora (OpenWebMath), expanding through 4 iterations to 120B tokens from Common Crawl [citation:DeepSeekMath](https://arxiv.org/abs/2402.03300).

**Tower** extended LLaMA-2's training on 20 billion tokens for 10 languages, mixing parallel sentences (one-third) with monolingual data (two-thirds) and applying quality thresholds [citation:Tower](https://arxiv.org/abs/2402.17733).

**Phi-3** deviated from standard scaling laws by filtering publicly available web data for "educational level" and calibrating training data to the "data optimal regime" for small models [citation:Phi-3](https://arxiv.org/abs/2404.14219).

**MATES** introduced model-aware data selection using data influence models to estimate each training example's contribution to model performance, enabling efficient pretraining by selecting high-influence data points [E3][citation:MATES](https://arxiv.org/abs/2406.06046).

### 3.4 Theme 3: Domain-Specific Continual Pre-Training

Several studies focused on continual pre-training for specialized capabilities:

**DeepSeekMath** allocated 56% DeepSeekMath Corpus, 4% AlgebraicStack, 10% arXiv, 20% GitHub code, and 10% natural language. The model outperformed Minerva 540B (77× larger) on MATH dataset by 10%+ absolute and led all open-source base models across 8 math benchmarks [citation:DeepSeekMath](https://arxiv.org/abs/2402.03300).

**Magicoder** used OSS-Instruct to generate 75K synthetic samples from open source code snippets, then continued finetuning with evol-codealpaca-v1 (110K samples). Magicoder-CL-7B outperformed WizardCoder-SC-15B and closely matched DeepSeek-Coder-Instruct-33B despite having 5× fewer parameters [E4][citation:Magicoder](https://arxiv.org/abs/2312.02120).

**LLaMAX** adapted pre-trained LLMs to new languages through vocabulary expansion, continual pre-training on multilingual corpora covering 102 languages with over 64 billion tokens, and instruction tuning [E1][citation:LLaMAX](https://arxiv.org/abs/2407.05975).

**Tower** achieved multilingual extension by mixing parallel sentences (one-third) with monolingual data (two-thirds), finding this ratio optimal for translation tasks [E2][citation:Tower](https://arxiv.org/abs/2402.17733).

### 3.5 Theme 4: Learning Rate Scheduling Strategies

Learning rate scheduling emerged as a critical mid-training component:

**OctoThinker** employed cosine learning rate without warmup (peak 3e-5, minimum one-tenth of peak) during the Stable stage, then applied cosine decay during the branching Decay stage [citation:OctoThinker](https://arxiv.org/abs/2506.20512).

**SmolLM2** used Warmup Stable Decay (WSD) schedule with 2,000-step warmup, peak learning rate 5.0×10⁻⁴ during stable phase, transitioning to decay phase reducing learning rate to zero over 10% of total training steps [citation:SmolLM2](https://arxiv.org/abs/2502.02737).

**DeepSeekMath** applied multi-step learning rate: peak after 2,000 warmup steps, 31.6% after 80% of training, 10% after 90% of training, with maximum learning rate 5.3e-4 [citation:DeepSeekMath](https://arxiv.org/abs/2402.03300).

**Qwen3** accelerated learning rate decay during the Reasoning Stage (5T tokens) to prioritize higher-quality STEM/coding/synthetic data [citation:Qwen3](https://arxiv.org/abs/2505.09388).

**Phi-3** and **SmolLM2** both reserved the final 10% of training for learning rate decay, using this annealing phase to maximize impact of upsampled high-quality math and code data [citation:Phi-3](https://arxiv.org/abs/2404.14219) [citation:SmolLM2](https://arxiv.org/abs/2502.02737).

### 3.6 Theme 5: Mid-Training Impact on Reinforcement Learning

**OctoThinker** provided the most comprehensive analysis of mid-training's effect on downstream RL performance:

- Models mid-trained on math web corpora showed improved RL performance, with MegaMath-Web-Pro and MegaMath-Web-Pro-Max bringing significant gains while FineMath-4plus yielded only marginal improvements
- Incorporating short-CoT data during mid-training showed no RL improvements compared to web-only mid-training, attributed to data distribution gaps
- Long-CoT data brought significant RL performance gains but introduced training instability with sudden performance drops and sharp response length increases
- 30% QA data ratio achieved optimal performance with diminishing returns beyond this threshold
- OctoThinker-Long-3B-Base reached performance parity with Qwen2.5-3B-Base during RL, despite starting from Llama-3.2-3B-Base, demonstrating mid-training's ability to close performance gaps between model families [citation:OctoThinker](https://arxiv.org/abs/2506.20512)

### 3.7 Optimal Data Mixing Ratios

Multiple studies identified specific optimal mixing ratios:

- **OctoThinker**: 30% QA data ratio optimal, with diminishing returns beyond this point [citation:OctoThinker](https://arxiv.org/abs/2506.20512)
- **SmolLM2**: 10-14% math data across stages, 20-24% code data in later stages [citation:SmolLM2](https://arxiv.org/abs/2502.02737)
- **Tower**: One-third parallel sentences, two-thirds monolingual data for optimal multilingual performance [citation:Tower](https://arxiv.org/abs/2402.17733)
- **DeepSeekMath**: 56% domain corpus, 20% code, 10% arXiv, 10% natural language, 4% algebraic code [citation:DeepSeekMath](https://arxiv.org/abs/2402.03300)

### 3.8 Context Length Extension Strategies

Three studies addressed context extension during mid-training:

**SmolLM2** extended context from 2k to 8k tokens using an intermediate checkpoint, training on 40% long-context documents (8k+ tokens) with RoPE base frequency 130k [citation:SmolLM2](https://arxiv.org/abs/2502.02737).

**Qwen2.5** employed two-phase context training: 4,096 tokens initially, extended to 32,768 (or 262,144 for Turbo) using YARN and Dual Chunk Attention with RoPE base frequency increased to 1,000,000 using ABF technique [citation:Qwen2.5](https://arxiv.org/abs/2412.15115).

**Qwen3** dedicated an entire third stage to long-context training with hundreds of billions of tokens at 32k sequence length, using RoPE base frequency 1M with ABF, YARN, and DCA [citation:Qwen3](https://arxiv.org/abs/2505.09388).

---

## 4. Discussion

### 4.1 Synthesis of Findings

Our systematic review reveals that mid-training has evolved from simple continual pre-training to sophisticated multi-stage processes with performance-driven interventions. Five key insights emerge:

**First**, successful mid-training requires adaptive data mixtures that evolve based on benchmark monitoring. SmolLM2's "online" approach exemplifies this, adjusting ratios across four stages to address capability bottlenecks [citation:SmolLM2](https://arxiv.org/abs/2502.02737).

**Second**, data quality curation has shifted from domain-level filtering to instance-level optimization. Qwen3's multilingual annotation system across 30T tokens represents the state-of-the-art, optimizing at granular instance level rather than coarse source level [citation:Qwen3](https://arxiv.org/abs/2505.09388).

**Third**, mid-training data distribution must align with downstream task requirements. OctoThinker's finding that short-CoT mid-training provided no RL benefits due to distribution gaps highlights this critical consideration [citation:OctoThinker](https://arxiv.org/abs/2506.20512).

**Fourth**, learning rate scheduling interacts with data mixture timing. All multi-stage approaches reserve the final 10% of training for decay, strategically upsampling high-quality data during this annealing phase [citation:SmolLM2](https://arxiv.org/abs/2502.02737) [citation:Phi-3](https://arxiv.org/abs/2404.14219).

**Fifth**, mid-training can bridge performance gaps between model families. OctoThinker-Long-3B-Base achieved parity with Qwen2.5-3B-Base during RL despite starting from the weaker Llama-3.2-3B-Base, demonstrating mid-training's potential to overcome architectural limitations [citation:OctoThinker](https://arxiv.org/abs/2506.20512).

### 4.2 Limitations

Several limitations characterize current mid-training research:

**Computational Cost**: Multi-stage training with performance monitoring requires substantial resources. SmolLM2's training cost approximately $250,000 USD, limiting exploration of alternative mixing schedules [citation:SmolLM2](https://arxiv.org/abs/2502.02737).

**Incomplete Reporting**: Some papers provided limited mid-training details. MATES was only available as abstract due to access issues, and Magicoder's concurrent work (DeepSeek-Coder) lacked publicly available data and instruction tuning details at time of writing [citation:Magicoder](https://arxiv.org/abs/2312.02120).

**Narrow Benchmark Focus**: Most evaluations emphasize math and coding benchmarks (MATH, GSM8K, HumanEval, MBPP), with limited assessment of broader capabilities such as creativity, reasoning transfer, or real-world task performance.

**RL Instability**: OctoThinker identified training instability when incorporating long-CoT data, with sudden performance drops and response length explosions. Stabilization methods require further investigation [citation:OctoThinker](https://arxiv.org/abs/2506.20512).

### 4.3 Future Research Directions

Based on our synthesis, we identify five promising directions:

1. **Automated Data Mixture Optimization**: Current approaches rely on manual monitoring and intervention. Future work should explore automated systems that dynamically adjust mixtures based on real-time benchmark performance.

2. **Instance-Level Selection at Scale**: Qwen3's instance-level optimization shows promise but requires 30T tokens of annotations. Research into efficient proxy models or automated annotation could democratize this approach.

3. **RL Stability Mechanisms**: The instability observed when mid-training with long-CoT data necessitates investigation into stabilization techniques, potentially through curriculum learning or gradient clipping strategies.

4. **Cross-Domain Transfer**: Current mid-training focuses on math/code domains. Research should explore mid-training for other capabilities such as scientific reasoning, legal analysis, or creative writing.

5. **Efficiency-Performance Tradeoffs**: Most studies prioritize performance over efficiency. Systematic investigation of compute-optimal mid-training strategies could reduce costs while maintaining gains.

---

## 5. Conclusion

This systematic literature review synthesizes 10 influential studies on LLM mid-training techniques published between 2023-2025. We identified five predominant themes: multi-stage training with evolving data mixtures, data quality prioritization, domain-specific continual pre-training, learning rate scheduling strategies, and mid-training's impact on reinforcement learning.

Key findings demonstrate that successful mid-training requires performance-driven interventions, instance-level data optimization, alignment between mid-training distributions and downstream tasks, and strategic learning rate scheduling. Mid-training has proven capable of bridging performance gaps between model families, with OctoThinker achieving parity with stronger base models through targeted 200B+ token mid-training.

Limitations include high computational costs, incomplete reporting in some studies, narrow benchmark focus, and RL instability with certain data types. Future research should prioritize automated mixture optimization, efficient instance-level selection, RL stability mechanisms, cross-domain transfer, and efficiency-performance tradeoffs.

As LLM development continues to advance, mid-training will remain a critical lever for enhancing model capabilities without requiring complete retraining from scratch. The methodologies and insights reviewed here provide a foundation for systematic mid-training research and development.

---

## References

1. Wang, Z., Zhou, F., Li, X., & Liu, P. (2025). OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling. *arXiv preprint arXiv:2506.20512*. https://arxiv.org/abs/2506.20512

2. Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024). DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models. *arXiv preprint arXiv:2402.03300*. https://arxiv.org/abs/2402.03300

3. Ben Allal, L., Lozhkov, A., Bakouch, E., Blázquez, G. M., Penedo, G., Tunstall, L., Marafioti, A., Kydlíček, H., Lajarín, A. P., Srivastav, V., Lochner, J., Fahlgren, C., Nguyen, X. S., Fourrier, C., Burtenshaw, B., Larcher, H., Zhao, H., Zakka, C., Morlon, M., & Raffel, C. (2025). SmolLM2: When Smol Goes Big -- Data-Centric Training of a Small Language Model. *arXiv preprint arXiv:2502.02737*. https://arxiv.org/abs/2502.02737

4. Qwen, Yang, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Li, C., Liu, D., Huang, F., Wei, H., Lin, H., Yang, J., Tu, J., Zhang, J., Yang, J., Yang, J., Zhou, J., & Lin, J. (2024). Qwen2.5 Technical Report. *arXiv preprint arXiv:2412.15115*. https://arxiv.org/abs/2412.15115

5. Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Gao, C., Huang, C., Lv, C., Zheng, C., Liu, D., Zhou, F., Huang, F., Hu, F., Ge, H., Wei, H., Lin, H., Tang, J., & Yang, J. (2025). Qwen3 Technical Report. *arXiv preprint arXiv:2505.09388*. https://arxiv.org/abs/2505.09388

6. Alves, D. M., Pombal, J., Guerreiro, N. M., Martins, P. H., Alves, J., Farajian, A., Peters, B., Rei, R., Fernandes, P., Agrawal, S., Colombo, P., de Souza, J. G. C., & Martins, A. F. T. (2024). Tower: An Open Multilingual Large Language Model for Translation-Related Tasks. *arXiv preprint arXiv:2402.17733*. https://arxiv.org/abs/2402.17733

7. Lu, Y., Zhu, W., Li, L., Qiao, Y., & Yuan, F. (2024). LLaMAX: Scaling Linguistic Horizons of LLM by Enhancing Translation Capabilities Beyond 100 Languages. *arXiv preprint arXiv:2407.05975*. https://arxiv.org/abs/2407.05975

8. Wei, Y., Wang, Z., Liu, J., Ding, Y., & Zhang, L. (2023). Magicoder: Empowering Code Generation with OSS-Instruct. *arXiv preprint arXiv:2312.02120*. https://arxiv.org/abs/2312.02120

9. Abdin, M., Aneja, J., Awadalla, H., Awadallah, A., Awan, A. A., Bach, N., Bahree, A., Bakhtiari, A., Bao, J., Behl, H., Benhaim, A., Bilenko, M., Bjorck, J., Bubeck, S., Cai, M., Cai, Q., Chaudhary, V., Chen, D., Chen, D., & Chen, W. (2024). Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone. *arXiv preprint arXiv:2404.14219*. https://arxiv.org/abs/2404.14219

10. Yu, Z., Das, S., & Xiong, C. (2024). MATES: Model-Aware Data Selection for Efficient Pretraining with Data Influence Models. *arXiv preprint arXiv:2406.06046*. https://arxiv.org/abs/2406.06046

---

## Sources

### Primary Sources (Included Papers)
- [OctoThinker](https://arxiv.org/abs/2506.20512) - Two-stage mid-training with RL scaling analysis
- [DeepSeekMath](https://arxiv.org/abs/2402.03300) - Iterative math corpus collection and continual pre-training
- [SmolLM2](https://arxiv.org/abs/2502.02737) - Performance-driven multi-stage training with evolving mixtures
- [Qwen2.5](https://arxiv.org/abs/2412.15115) - Scaled pre-training with LLM-filtered data quality
- [Qwen3](https://arxiv.org/abs/2505.09388) - Instance-level data optimization across three stages
- [Tower](https://arxiv.org/abs/2402.17733) - Multilingual continual pre-training with parallel sentences
- [LLaMAX](https://arxiv.org/abs/2407.05975) - Vocabulary expansion for multilingual adaptation
- [Magicoder](https://arxiv.org/abs/2312.02120) - OSS-Instruct code generation from open source
- [Phi-3](https://arxiv.org/abs/2404.14219) - Quality-filtered two-phase pre-training
- [MATES](https://arxiv.org/abs/2406.06046) - Model-aware data selection with influence models

<!-- evidence-appendix: generated by the citation gate from checked quotes; edits here are overwritten -->

## Evidence

Each [E#] in the text points to a quote below. Code checked on 2026-10-27 that every quote appears word for word in the paper's arXiv HTML (case, punctuation and in-text citations ignored). Whether a quote supports the sentence citing it was not checked by code.

| Id | Paper | Location | Quote |
|---|---|---|---|
| E5 | arXiv:2404.14219 | [Training Methodology.](https://arxiv.org/html/2404.14219#S2.SS0.SSS0.Px2.p1) | “Pre-training is performed in two disjoint and sequential phases; phase-1 comprises mostly of web sources aimed at teaching the model general knowledge and language understanding. Phase-2 merges even more heavily filtered webdata (a subset used in Phase-1) with some synthetic data that teach the model logical reasoning and various niche skills.” |
| E3 | arXiv:2406.06046 | [3.1 Model-aware data selection framework](https://arxiv.org/html/2406.06046#S3.SS1.p1) | “MATES selects the most effective data for pretraining a language model, aiming to maximize its final target performance, as illustrated in Figure 2.” |
| E4 | arXiv:2312.02120 | [3 Evaluation](https://arxiv.org/html/2312.02120#S3.p1) | “To derive Magicoder series, we first finetune them on 75K synthetic data generated through OSS-Instruct. We then obtain Magicoder \mathcal{S} by continuing finetuning Magicoder with the evol-codealpaca-v1 dataset, an open-source Evol-Instruct implementation containing about 110K samples.” |
| E1 | arXiv:2407.05975 | [3.1 Components of Training Data](https://arxiv.org/html/2407.05975#S3.SS1.p1) | “During the continual pertaining stage, the collected training data covering 102 languages (refer to A , which are all languages supported by Flores-101), mainly consists of two parts: monolingual ( \mathcal{D}_{\mathrm{mono}}^{A} ) and parallel ( \mathcal{D}_{\mathrm{para}}^{A} ) data.” |
| E2 | arXiv:2402.17733 | [2.1 TowerBase: Extending the multilingual capabilities of LLaMA-2](https://arxiv.org/html/2402.17733#S2.SS1.p1) | “We extend LLaMA-2's training on a highly-multilingual dataset comprising 20 billion tokens — measured with the model's tokenizer — for 10 languages: English (en), German (de), French (fr), Dutch (nl), Italian (it), Spanish (es), Portuguese (pt), Korean (ko), Russian (ru), and Chinese (zh).” |

<!-- /evidence-appendix -->
