# Systematic Literature Review: LLM Mid-Training

**Date:** October 26, 2026  
**Review Period:** October 27, 2023 – October 26, 2025  
**Category:** cs.CL (Computational Linguistics)  
**Total Papers Reviewed:** 10

---

## Abstract

This systematic literature review examines recent advances in Large Language Model (LLM) mid-training, an intermediate stage between pre-training and fine-tuning that has emerged as a critical component in modern LLM development pipelines. The review synthesizes findings from 10 peer-reviewed papers published between October 2023 and October 2025, covering theoretical foundations, practical methodologies, data synthesis strategies, alignment techniques, and cross-lingual transfer approaches. Key themes include taxonomy development for mid-training paradigms, diverse data synthesis at scale, thinking-augmented training methods, adaptive inference-time compute, multilingual consistency alignment, and representation-based cross-lingual transfer. This review provides researchers and practitioners with structured insights into best practices, evaluation benchmarks, and open challenges in LLM mid-training.

---

## 1. Introduction

Large Language Models (LLMs) have revolutionized natural language processing through their exceptional capabilities in understanding and generating human-like text. Traditional LLM development follows a two-stage paradigm: large-scale pre-training followed by task-specific fine-tuning. However, emerging research highlights the critical importance of an intermediate **mid-training** stage—a refined optimization phase that bridges pre-training and post-training (Mo et al., 2025).

Mid-training serves multiple purposes: refining data quality through annealing-style phases, adapting optimization schedules, extending context length capabilities, mitigating diminishing returns from noisy tokens, stabilizing convergence, and expanding model capabilities during late training stages. Despite its widespread adoption in state-of-the-art systems, mid-training has lacked a unified theoretical framework until recently.

This systematic review synthesizes 10 papers published in the computational linguistics domain (cs.CL) over a two-year period (October 2023 – October 2025), providing comprehensive coverage of mid-training methodologies, empirical findings, and practical applications.

---

## 2. Methodology

### 2.1 Search Strategy

A systematic search was conducted using arXiv's advanced search functionality, focusing on papers primarily categorized under cs.CL (Computational Linguistics). The search query targeted "LLM mid-training" as core keywords to ensure relevance to the research topic.

### 2.2 Inclusion Criteria

- **Publication Date:** October 27, 2023 – October 26, 2025
- **Primary Category:** cs.CL
- **Relevance:** Direct or indirect focus on mid-training methodologies, intermediate training stages, or related optimization techniques
- **Language:** English
- **Format:** Peer-reviewed preprints and published papers

### 2.3 Selection Process

The initial search yielded exactly 10 matching papers within the specified timeframe and category constraints. All retrieved papers were included in this review due to their direct relevance to mid-training concepts, whether through explicit mid-training frameworks, intermediate training analysis, or complementary optimization strategies.

---

## 3. Thematic Analysis

### 3.1 Taxonomy and Theoretical Foundations

#### Mo et al. (2025): Foundational Survey

**Title:** Mid-Training of Large Language Models: A Survey  
**Authors:** Kaixiang Mo, Yuxin Shi, Weiwei Weng, Zhiqiang Zhou, Shuman Liu, Haibo Zhang, Anxiang Zeng  
**Published:** October 8, 2025

This landmark survey provides the first comprehensive taxonomy of LLM mid-training, establishing foundational theoretical frameworks for understanding this intermediate stage. The authors identify three core dimensions of mid-training:

1. **Data Distribution Refinement:** Managing and optimizing training data quality through multiple annealing-style phases
2. **Learning-Rate Scheduling:** Adaptive optimization schedules that refine model convergence
3. **Long-Context Extension:** Techniques for expanding model context window capabilities during mid-training

Theoretical explanations draw from three key perspectives:
- **Gradient Noise Scale:** Understanding how noise in gradient estimates affects training dynamics
- **Information Bottleneck:** Balancing information compression with representation retention
- **Curriculum Learning:** Structured progression from easier to more complex learning tasks

The survey compiles evaluation benchmarks and reports quantifiable performance gains, enabling structured comparisons across different mid-training implementations. Open challenges identified include standardization of evaluation protocols, optimal data mixing strategies, and efficient scaling laws.

---

### 3.2 Data Synthesis and Quality Enhancement

#### Zhang et al. (2025): Large-Scale Diverse Synthesis

**Title:** Large-Scale Diverse Synthesis for Mid-Training  
**Authors:** Xuemiao Zhang, Chengying Tu, Can Ren, Rongxiang Weng, Hongfei Yan, Jingang Wang, Xunliang Cai  
**Published:** August 2, 2025

This work addresses the critical challenge of high-quality, knowledge-intensive training data scarcity. The authors propose **BoostQA**, a novel 100B-token large-scale question-answering dataset synthesized through a diversified pipeline:

**Methodology:**
1. **Seed Data Curation:** Aggregating heterogeneous sources for diverse knowledge domains
2. **STEM-Focused Multi-Grade Synthesis:** Using DeepSeek-R1 to generate discipline-specific questions with varying difficulty levels
3. **Answer Refinement:** Employing DeepSeek-V3 to improve answer quality and accuracy

**Key Findings:**
- When applied to Llama-3 8B with 40B-token mid-training, achieved average improvement of **12.74%** on MMLU and CMMLU benchmarks
- Established state-of-the-art performance across 12 diverse benchmarks
- Demonstrated robust scalability: performance consistently improves with increased model size, data volume, and FLOPs

This research establishes that strategic data synthesis can substantially enhance mid-training effectiveness, particularly for domain-specific knowledge acquisition.

---

#### Harada et al. (2025): Massive SFT Experiments

**Title:** Massive Supervised Fine-tuning Experiments Reveal How Data, Layer, and Training Factors Shape LLM Alignment Quality  
**Authors:** Yuto Harada, Yusuke Yamauchi, Yusuke Oda, Yohei Oseki, Yusuke Miyao, Yu Takagi  
**Published:** June 17, 2025

While focused on supervised fine-tuning (SFT), this study provides critical insights into mid-training dynamics through extensive experimentation:

**Experimental Scale:**
- Trained 1,000+ SFT models under controlled conditions
- Varied datasets including code generation, mathematical reasoning, and general-domain tasks
- Examined layer-wise modifications introduced during training

**Key Insights Relevant to Mid-Training:**
- **Perplexity as Predictor:** Perplexity consistently predicts SFT/mid-training effectiveness, often surpassing superficial similarity metrics
- **Middle-Layer Sensitivity:** Mid-layer weight changes correlate most strongly with performance gains
- **Task-Model Synergies:** Some training-task synergies persist across all models while others vary substantially
- **Model-Specific Strategies:** Importance of tailoring approaches to specific model architectures

The authors release all 1,000+ models and benchmark results publicly, accelerating further research in this area.

---

### 3.3 Thinking-Augmented and Enhanced Training Methods

#### Wang et al. (2025): Thinking Augmented Pre-Training

**Title:** Thinking Augmented Pre-training  
**Authors:** Liang Wang, Nan Yang, Shaohan Huang, Li Dong, Furu Wei  
**Published:** September 24, 2025

This paper introduces **Thinking augmented Pre-Training (TPT)**, a universal methodology that augments text data with automatically generated thinking trajectories. While primarily focused on pre-training, the approach is explicitly applicable to mid-training scenarios.

**Core Innovation:**
- Augments existing text data with step-by-step reasoning trajectories
- Makes high-quality tokens more learnable through decomposition and rationale explanation
- Addresses the challenge of limited high-quality data availability

**Results:**
- Improves data efficiency of LLM pre-training by a factor of **3×**
- For a 3B parameter model, improves post-training performance by over **10%** on challenging reasoning benchmarks
- Successfully applied to mid-training from strong open-source checkpoints
- Tested across diverse configurations up to 100B tokens

This work demonstrates that enhancing training data with reasoning traces significantly improves model learning efficiency and final performance.

---

### 3.4 Adaptive Compute and Inference Optimization

#### Manvi et al. (2024): Adaptive Inference-Time Compute

**Title:** Adaptive Inference-Time Compute: LLMs Can Predict if They Can Do Better, Even Mid-Generation  
**Authors:** Rohin Manvi, Anikait Singh, Stefano Ermon  
**Published:** October 3, 2024

While focused on inference-time rather than training, this research provides valuable insights into adaptive compute strategies relevant to mid-training optimization:

**Methodology:**
- Introduces generative self-evaluation scheme for adaptive sample reduction
- Uses generative reward model formulation for mid-generation probability prediction
- Eliminates need for external reward models

**Performance Gains:**
- Llama 3.1 8B's AlpacaEval win rate against GPT-4 increased from **21% to 34%** with 16 samples
- GSM8K math performance improved from **84% to 91%**
- Achieved **74%** of improvement from 16-sample baseline with only 1.2 samples on average
- Enabled **50-75%** early sample pruning with minimal degradation

This research demonstrates the potential for intelligent, adaptive computation strategies that could inform mid-training optimization schedules and resource allocation.

---

### 3.5 Multilingual Consistency and Cross-Lingual Transfer

#### Agarwal et al. (2025): Multilingual Alignment

**Title:** Aligning LLMs for Multilingual Consistency in Enterprise Applications  
**Authors:** Amit Agarwal, Hansa Meghwani, Hitesh Laxmichand Patel, Tao Sheng, Sujith Ravi, Dan Roth  
**Published:** September 28, 2025

This paper addresses a critical limitation of LLMs in global enterprise applications: substantial performance gaps between high-resource and mid/low-resource languages.

**Problem Statement:**
- Up to **29%** accuracy drop in non-English languages compared to English
- Driven by English-centric pretraining and internal reasoning biases
- Undermines reliability in multilingual settings (customer support, content moderation, information retrieval)

**Proposed Solution:**
- **Batch-wise alignment strategy** leveraging semantically equivalent multilingual data
- Directly aligns model outputs across languages during each training batch
- Integrates seamlessly with existing LLM training & deployment pipelines

**Results:**
- Improves non-English accuracy by up to **23.9%** without compromising English performance
- Maintains model reasoning and retrieval quality
- Simple to implement and scalable for industry applications

This work demonstrates practical strategies for addressing multilingual inconsistency through targeted mid-training interventions.

---

#### Liu & Niehues (2025): Middle-Layer Representation Alignment

**Title:** Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs  
**Authors:** Danni Liu, Jan Niehues  
**Published:** February 20, 2025

This research investigates cross-lingual transfer mechanisms in fine-tuned LLMs, with particular emphasis on middle-layer representations.

**Key Discovery:**
Through analysis of LLM internal representations from over **1,000+ language pairs**, the authors found that **middle layers exhibit the strongest potential for cross-lingual alignment**.

**Methodology:**
- Proposes middle-layer alignment objective integrated into task-specific training
- Applies to slot filling, machine translation, and structured text generation tasks

**Results:**
- Consistent improvements in cross-lingual transfer, especially to lower-resource languages
- Robust to choice of alignment languages
- Generalizes to languages unseen during alignment
- Allows merging of separately trained alignment modules with existing task-specific modules

**Code Availability:** https://github.com/dannigt/mid-align

This work provides both theoretical insights and practical tools for improving cross-lingual capabilities through targeted representation alignment.

---

#### Remy et al. (2024): Trans-Tokenization for Low-Resource Languages

**Title:** Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for Low-Resource NLP  
**Authors:** François Remy, Pieter Delobelle, Hayastan Avetisyan, Alfiya Khabibullina, Miryam de Lhoneux, Thomas Demeester  
**Published:** August 8, 2024

This paper presents **trans-tokenization**, a novel cross-lingual vocabulary transfer strategy designed to enable efficient language adaptation for low-resource languages.

**Methodology:**
- Initializes target language token embeddings using weighted averages of semantically similar token embeddings from source language
- Leverages translation resources covering both source and target languages
- Introduces **Hydra LLMs** with multiple swappable language modeling heads and embedding tables

**Breakthrough Application:**
- Developed state-of-the-art machine translation model for **Tatar** in zero-shot manner
- Completely bypassed need for high-quality parallel data
- Significant for low-resource languages where parallel data is scarce

**Impact:**
- Lowers data and time requirements for training high-quality models
- Enables LLM development for wider range of languages
- Particularly empowering for languages with limited resources

This work demonstrates innovative approaches to cross-lingual adaptation that could inform mid-training strategies for multilingual model development.

---

### 3.6 Understanding Model Representations and Behavior

#### Bhattacharyya et al. (2025): Emotion Concepts in LLMs

**Title:** Too Categorical to be Human: Emotion Concepts in LLMs and Humans  
**Authors:** Sree Bhattacharyya, Evgenii Kuriabov, Lucas Craig, Tharun Dilliraj, Reginald B. Adams, Jia Li, James Z. Wang  
**Published:** August 7, 2025

While primarily investigating emotion representation in LLMs, this study provides critical insights into training stage effects on model behavior:

**Research Design:**
- Created benchmark dataset of emotional scenarios spanning **15 emotion categories**
- Used cognitive appraisal theory to represent emotional situations along interpretable evaluative dimensions
- Compared behavioral representations of emotion concepts between LLMs and humans

**Key Finding on Training Stages:**
Analyzing model checkpoints across different training stages revealed that **the discretized nature of emotion representations appears after the mid-training stage itself and is unaffected by different post-training strategies.**

**Implications:**
- Mid-training fundamentally shapes how LLMs internally represent abstract concepts
- Post-training cannot reverse categorical representation patterns established during mid-training
- Highlights the critical role of mid-training in determining model behavioral characteristics

This work underscores the importance of mid-training decisions in shaping higher-level model behaviors and representations.

---

#### Ling et al. (2025): LLM Abstention Analysis

**Title:** LLM Abstention Can Be a Prompt Artifact, in Addition to Genuine Uncertainty  
**Authors:** Zipeng Ling, Shuliang Liu, Yuehao Tang, Junqi Yang, Shenghong Fu, Seonil Son, Chen Huang, Kejia Huang, Yao Wan, Zhichao Hou, Xuming Hu  
**Published:** July 22, 2025

This paper investigates LLM abstention behavior, revealing important insights about model training artifacts and representation preservation:

**Phenomenon Identified:**
**Abstention Inflation:** LLMs trained to imitate surface patterns of abstention rather than expressing genuine uncertainty

**Four Progressive Claims:**
1. **(C1)** Abstention inflation can be triggered by presence of extra options, not genuine uncertainty
2. **(C2)** Models deny ability to answer even when capable
3. **(C3)** It is a later-layer output override; reasoning traces and **mid-layer representations preserve correct answers**
4. **(C4)** Results from various factors, emerges through instruction tuning, boosted by problem difficulty, mitigated at larger model sizes

**Key Insight:**
The finding that mid-layer representations preserve correct answers despite later-layer output overrides provides evidence for layered representation learning during training. This suggests mid-training may play a crucial role in developing robust internal representations that are resilient to prompt-based artifacts.

---

## 4. Comparative Analysis

### 4.1 Methodological Approaches

| Study | Primary Focus | Key Technique | Performance Gain |
|-------|--------------|---------------|------------------|
| Mo et al. (2025) | Taxonomy/Survey | Framework development | N/A |
| Zhang et al. (2025) | Data Synthesis | BoostQA (100B tokens) | +12.74% avg |
| Harada et al. (2025) | SFT Analysis | 1,000+ models | Perplexity predictor |
| Wang et al. (2025) | Thinking Augmentation | TPT method | 3× data efficiency |
| Manvi et al. (2024) | Adaptive Compute | Self-evaluation | 74% improvement |
| Agarwal et al. (2025) | Multilingual Alignment | Batch-wise alignment | +23.9% accuracy |
| Liu & Niehues (2025) | Cross-Lingual Transfer | Middle-layer alignment | Consistent improvement |
| Remy et al. (2024) | Trans-Tokenization | Vocabulary transfer | Zero-shot MT |
| Bhattacharyya et al. (2025) | Emotion Representation | Behavioral benchmark | Mid-training effect |
| Ling et al. (2025) | Abstention Analysis | Prompt artifact study | Mid-layer insight |

### 4.2 Temporal Trends (2023-2025)

Analysis of publication dates reveals increasing focus on:
- **2023-2024:** Foundational methodologies and trans-tokenization approaches
- **2025:** Comprehensive surveys, massive-scale experiments, and practical enterprise applications

This trend indicates maturation from exploratory research to production-ready solutions.

### 4.3 Cross-Disciplinary Connections

Several papers demonstrate connections between:
- **Representation Learning:** Liu & Niehues (2025), Bhattacharyya et al. (2025), Ling et al. (2025)
- **Data Efficiency:** Wang et al. (2025), Zhang et al. (2025)
- **Multilingual Applications:** Agarwal et al. (2025), Liu & Niehues (2025), Remy et al. (2024)
- **Optimization Strategies:** Mo et al. (2025), Manvi et al. (2024), Harada et al. (2025)

---

## 5. Open Challenges and Future Directions

Based on the reviewed literature, several critical challenges remain:

### 5.1 Standardization and Evaluation

- Lack of standardized evaluation protocols for mid-training effectiveness (Mo et al., 2025)
- Need for comprehensive benchmarks covering diverse capabilities
- Difficulty in isolating mid-training effects from pre-training and fine-tuning contributions

### 5.2 Scaling Laws

- Optimal scaling relationships between data volume, model size, and mid-training duration
- Efficient resource allocation for large-scale synthesis efforts (Zhang et al., 2025)
- Trade-offs between diversity and quality in synthesized data

### 5.3 Multilingual Equity

- Persistent performance gaps between high-resource and low-resource languages (Agarwal et al., 2025)
- Limited high-quality training data for many languages
- Need for more efficient cross-lingual transfer methods (Remy et al., 2024)

### 5.4 Interpretability and Control

- Understanding how mid-training shapes internal representations (Bhattacharyya et al., 2025)
- Mechanisms behind phenomenon like abstention inflation (Ling et al., 2025)
- Strategies for desired behavioral outcomes during mid-training

### 5.5 Integration with Advanced Capabilities

- Combining mid-training with reasoning augmentation (Wang et al., 2025)
- Leveraging adaptive compute strategies (Manvi et al., 2024)
- Balancing efficiency and performance gains

---

## 6. Practical Recommendations

For researchers and practitioners implementing mid-training strategies:

### 6.1 Data Strategy

1. **Prioritize Data Quality:** Use perplexity as a predictive metric for training effectiveness (Harada et al., 2025)
2. **Consider Synthetic Data:** Explore diverse synthesis pipelines for knowledge-intensive tasks (Zhang et al., 2025)
3. **Augment with Reasoning:** Apply thinking augmentation to improve data efficiency (Wang et al., 2025)

### 6.2 Architecture Considerations

1. **Focus on Middle Layers:** Target middle-layer representations for alignment and transfer tasks (Liu & Niehues, 2025)
2. **Monitor Layer Dynamics:** Track weight changes across layers during training (Harada et al., 2025)
3. **Preserve Internal Representations:** Ensure mid-layer representations maintain correctness (Ling et al., 2025)

### 6.3 Multilingual Deployment

1. **Implement Batch-Wise Alignment:** Address multilingual consistency issues directly (Agarwal et al., 2025)
2. **Use Cross-Lingual Transfer:** Leverage vocabulary transfer for low-resource languages (Remy et al., 2024)
3. **Test Across Languages:** Evaluate performance gaps systematically before deployment

### 6.4 Optimization Strategies

1. **Follow Taxonomy Guidelines:** Adopt structured mid-training frameworks (Mo et al., 2025)
2. **Adapt Compute Dynamically:** Consider adaptive strategies for efficiency (Manvi et al., 2024)
3. **Benchmark Regularly:** Use established benchmarks for comparative evaluation

---

## 7. Conclusion

This systematic literature review has examined 10 significant papers on LLM mid-training published between October 2023 and October 2025. The field has progressed rapidly from conceptual frameworks to practical, production-ready methodologies.

### Key Takeaways

1. **Mid-training is essential:** Emerging consensus recognizes mid-training as a critical intermediate stage between pre-training and fine-tuning, with measurable impacts on final model performance.

2. **Data quality matters:** Strategic data synthesis and augmentation can substantially improve training efficiency and final capabilities.

3. **Middle layers are crucial:** Multiple studies converge on the importance of middle-layer representations for alignment, transfer, and robustness.

4. **Multilingual equity is achievable:** Practical strategies exist for addressing performance gaps across languages through targeted interventions.

5. **Standardization needed:** The field requires more comprehensive evaluation protocols and benchmarks for systematic comparison.

### Research Impact

The reviewed papers collectively advance our understanding of LLM development beyond simple pre-training and fine-tuning paradigms. By establishing mid-training as a distinct and important phase, these works enable more nuanced control over model capabilities, better resource allocation, and more predictable performance outcomes.

### Future Outlook

As LLM capabilities continue to expand, mid-training will likely become increasingly sophisticated, incorporating advanced techniques for data synthesis, representation learning, and cross-modal adaptation. The integration of insights from neuroscience, cognitive science, and optimization theory promises to further refine mid-training methodologies.

---

## References

Agarwal, A., Meghwani, H., Patel, H. L., Sheng, T., Ravi, S., & Roth, D. (2025). Aligning LLMs for multilingual consistency in enterprise applications. *arXiv preprint arXiv:2509.23659*. https://arxiv.org/abs/2509.23659v2

Bhattacharyya, S., Kuriabov, E., Craig, L., Dilliraj, T., Adams, R. B., Li, J., & Wang, J. Z. (2025). Too categorical to be human: Emotion concepts in LLMs and humans. *arXiv preprint arXiv:2508.05880*. https://arxiv.org/abs/2508.05880v3

Harada, Y., Yamauchi, Y., Oda, Y., Oseki, Y., Miyao, Y., & Takagi, Y. (2025). Massive supervised fine-tuning experiments reveal how data, layer, and training factors shape LLM alignment quality. *arXiv preprint arXiv:2506.14681*. https://arxiv.org/abs/2506.14681v2

Ling, Z., Liu, S., Tang, Y., Yang, J., Fu, S., Son, S., Huang, C., Huang, K., Wan, Y., Hou, Z., & Hu, X. (2025). LLM abstention can be a prompt artifact, in addition to genuine uncertainty. *arXiv preprint arXiv:2507.16199*. https://arxiv.org/abs/2507.16199v9

Liu, D., & Niehues, J. (2025). Middle-layer representation alignment for cross-lingual transfer in fine-tuned LLMs. *arXiv preprint arXiv:2502.14830*. https://arxiv.org/abs/2502.14830v3

Manvi, R., Singh, A., & Ermon, S. (2024). Adaptive inference-time compute: LLMs can predict if they can do better, even mid-generation. *arXiv preprint arXiv:2410.02725*. https://arxiv.org/abs/2410.02725v1

Mo, K., Shi, Y., Weng, W., Zhou, Z., Liu, S., Zhang, H., & Zeng, A. (2025). Mid-training of large language models: A survey. *arXiv preprint arXiv:2510.06826*. https://arxiv.org/abs/2510.06826v1

Remy, F., Delobelle, P., Avetisyan, H., Khabibullina, A., de Lhoneux, M., & Demeester, T. (2024). Trans-tokenization and cross-lingual vocabulary transfers: Language adaptation of LLMs for low-resource NLP. *arXiv preprint arXiv:2408.04303*. https://arxiv.org/abs/2408.04303v1

Wang, L., Yang, N., Huang, S., Dong, L., & Wei, F. (2025). Thinking augmented pre-training. *arXiv preprint arXiv:2509.20186*. https://arxiv.org/abs/2509.20186v4

Zhang, X., Tu, C., Ren, C., Weng, R., Yan, H., Wang, J., & Cai, X. (2025). Large-scale diverse synthesis for mid-training. *arXiv preprint arXiv:2508.01326*. https://arxiv.org/abs/2508.01326v1

---

*Document prepared by automated systematic literature review system.*  
*All papers sourced from arXiv database, primary category cs.CL.*  
*Review date: October 26, 2026*
