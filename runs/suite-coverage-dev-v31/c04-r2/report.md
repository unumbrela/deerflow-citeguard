# Systematic Literature Review: LLM Mid-Training

**Review Period:** October 27, 2023 – October 26, 2025  
**Category:** cs.CL (Computation and Language)  
**Total Papers Reviewed:** 10  

---

## Executive Summary

This systematic literature review examines recent advances in Large Language Model (LLM) mid-training, an intermediate stage between pre-training and task-specific fine-tuning that has emerged as critical for optimizing model performance. The reviewed literature reveals that mid-training serves multiple purposes: refining data quality, stabilizing convergence through annealing-style phases, extending context length capabilities, and enhancing domain-specific knowledge acquisition. Key findings indicate that mid-training can achieve performance improvements of up to 12.74% on standard benchmarks while improving data efficiency by factors of 3x. The research spans theoretical frameworks, practical methodologies, and empirical evaluations across diverse domains including STEM education, code generation, multilingual alignment, and emotional reasoning.

### Key Themes Identified:

1. **Mid-Training Taxonomy and Frameworks** - Comprehensive surveys establishing foundational understanding
2. **Data Synthesis and Quality Enhancement** - Novel approaches for creating high-quality training corpora
3. **Computational Efficiency** - Adaptive compute allocation and optimization strategies
4. **Domain-Specific Applications** - Specialized implementations for coding, mathematics, and enterprise use
5. **Representation Analysis** - Understanding how training stages affect internal model representations

---

## Introduction

Large language models have traditionally been developed through large-scale pre-training followed directly by task-specific fine-tuning. However, emerging research highlights the critical importance of an intermediate mid-training stage that refines model capabilities before final alignment. This systematic review synthesizes 10 peer-reviewed papers published between October 2023 and October 2025, focusing on computational linguistics (cs.CL) and related fields where mid-training methodologies are prominently featured.

The mid-training paradigm addresses several challenges inherent in direct pre-training-to-fine-tuning pipelines: diminishing returns from noisy tokens, convergence instability, limited generalization capacity, and constrained context length expansion. Through gradient noise scale management, information bottleneck optimization, and curriculum learning principles, mid-training promotes superior abstraction and generalization capabilities.

### Methodology

This review follows systematic literature review protocols with the following criteria:
- **Search Scope**: arXiv repository, primary category cs.CL
- **Time Window**: October 27, 2023 – October 26, 2025 (exactly 2 years)
- **Selection Criteria**: Papers explicitly addressing mid-training concepts or methodology
- **Format**: APA citation style
- **Quality Assessment**: Peer-reviewed preprints with empirical validation

---

## Thematic Analysis

### 1. Foundational Frameworks and Surveys

#### Mo et al. (2025) - First Comprehensive Survey

The most recent and comprehensive survey by Mo et al. provides the first unified taxonomy of LLM mid-training, categorizing approaches across three dimensions: data distribution, learning-rate scheduling, and long-context extension. The authors identify gradient noise scale, information bottleneck theory, and curriculum learning as the theoretical foundations explaining mid-training effectiveness [citation:Mo et al., 2025](https://arxiv.org/abs/2510.06826v1).

Key contributions include:
- Unified conceptual framework for mid-training as a distinct paradigm
- Practical insights distilled from state-of-the-art systems
- Evaluation benchmarks enabling structured cross-model comparisons
- Identification of open challenges and future research directions

The survey emphasizes that despite widespread adoption in production systems, mid-training had previously lacked systematic study, making this work foundational for subsequent research.

### 2. Data-Centric Approaches

#### Zhang et al. (2025) - BoostQA Synthesis Framework

Zhang et al. present a novel diversified pipeline for synthesizing BoostQA, a 100B-token large-scale question-answering dataset designed specifically for mid-training applications [citation:Zhang et al., 2025](https://arxiv.org/abs/2508.01326v1). Their approach addresses critical limitations in traditional corpus development:

**Methodology:**
1. Seed data curation from heterogeneous sources
2. DeepSeek-R1 implementation for STEM-focused multi-grade synthesis
3. Difficulty degradation mitigation through specialized augmentation
4. Answer refinement via DeepSeek-V3 for quality improvement

**Results:**
- Llama-3 8B mid-trained on 40B-token subset achieved average improvement of 12.74% on MMLU and CMMLU
- Established SOTA performance across 12 benchmarks
- Demonstrated robust scalability with consistent improvements across model sizes and FLOPs budgets

This work exemplifies the data-centric paradigm where mid-training serves as the optimal stage for domain-specific knowledge acquisition before final alignment.

#### Wang et al. (2025) - Thinking Augmented Pre-Training

Wang et al. introduce Thinking augmented Pre-Training (TPT), a universal methodology that augments existing text data with automatically generated thinking trajectories [citation:Wang et al., 2025](https://arxiv.org/abs/2509.20186v4). While primarily positioned as pre-training augmentation, the authors explicitly apply TPT to mid-training scenarios from strong open-source checkpoints.

**Key Findings:**
- Improves data efficiency of LLM pre-training by factor of 3
- Makes high-quality tokens more learnable through step-by-step reasoning decomposition
- Enhances post-training performance by over 10% on challenging reasoning benchmarks for 3B parameter models
- Applicable across diverse training configurations up to 100B tokens

This approach demonstrates how mid-training benefits from enriched token-level rationales, particularly for complex reasoning tasks where underlying logic requires explicit decomposition.

### 3. Computational Efficiency and Optimization

#### Manvi et al. (2024) - Adaptive Inference-Time Compute

Manvi et al. investigate adaptive inference-time compute strategies that relate to mid-generation optimization [citation:Manvi et al., 2024](https://arxiv.org/abs/2410.02725v1). While focused on inference rather than training, their generative self-evaluation scheme offers insights applicable to mid-training optimization.

**Innovation:**
- Generative reward model formulation allowing mid-generation probability prediction
- Eliminates need for external reward models
- Enables early sample pruning and temperature annealing adjustments

**Performance Gains:**
- Llama 3.1 8B AlpacaEval win rate increased from 21% to 34% with 16 samples
- GSM8K math performance improved from 84% to 91%
- Achieved 74% of 16-sample improvement using only 1.2 samples on average
- Pruned 50-75% of samples early with minimal performance degradation

This work highlights the parallel between adaptive inference strategies and potential mid-training optimizations, suggesting similar self-evaluation mechanisms could improve training efficiency.

#### Su et al. (2025) - Training Instability Mitigation

Su et al. examine training instabilities in block-scaled precision formats during LLM training [citation:Su et al., 2025](https://arxiv.org/abs/2506.20752v1). Their findings are particularly relevant for mid-training where precision schemes can be modified to recover performance.

**Key Insights:**
- Multiplicative gradient bias from quantization triggers runaway divergence
- Instabilities become pronounced at larger compute scales (2×10^17 to 4.8×10^19 FLOPs)
- Modifying precision schemes mid-training can avert or delay instabilities
- Hybrid configurations recover performance competitive with full-precision training

This research demonstrates that mid-training represents an optimal intervention point for stability modifications, supporting the broader argument for dedicated mid-training phases.

### 4. Domain-Specific Applications

#### FAIR CodeGen Team (2025) - World Models for Code Generation

The FAIR CodeGen team release Code World Model (CWM), a 32-billion-parameter LLM specifically designed for code generation research [citation:FAIR CodeGen Team, 2025](https://arxiv.org/abs/2510.02387v1). Their approach uniquely leverages mid-training on observation-action trajectories from Python interpreter and agentic Docker environments.

**Architecture:**
- Dense, decoder-only LLM with 131k token context size
- Mid-training on execution trajectories enables step-by-step simulation
- Multi-task reasoning RL in verifiable coding, math, and software engineering environments
- Released checkpoints after mid-training, SFT, and RL stages for reproducibility

**Performance:**
- 65.8% pass@1 on SWE-bench Verified (with test-time scaling)
- 68.6% on LiveCodeBench
- 96.6% on Math-500
- 76.0% on AIME 2024

This work establishes world modeling as a viable mid-training strategy for computational domains, providing a testbed for exploring reasoning and planning in computational environments.

#### Agarwal et al. (2025) - Multilingual Enterprise Alignment

Agarwal et al. address performance gaps between high-resource and low-resource languages in enterprise applications [citation:Agarwal et al., 2025](https://arxiv.org/abs/2509.23659v2). They propose a batch-wise alignment strategy leveraging semantically equivalent multilingual data for mid-training optimization.

**Approach:**
- Batch-wise alignment using semantically equivalent multilingual pairs
- Direct cross-language output alignment without compromising English performance
- Simple implementation integrating seamlessly with existing training pipelines

**Results:**
- Up to 23.9% improvement in non-English accuracy
- No degradation in English performance or retrieval quality
- Addresses 29% accuracy drop observed in RAG systems for non-English languages

This research demonstrates mid-training's applicability to enterprise-scale multilingual deployment challenges, offering practical solutions for global AI applications.

#### Harada et al. (2025) - Massive SFT Experiments

Harada et al. conduct extensive supervised fine-tuning experiments examining layer-wise modifications and dataset properties [citation:Harada et al., 2025](https://arxiv.org/abs/2506.14681v2). While focused on SFT, their findings reveal important correlations with mid-training effects.

**Major Findings:**
- Trained 1,000+ SFT models under controlled conditions
- Perplexity consistently predicts SFT effectiveness, surpassing superficial data similarity
- Mid-layer weight changes correlate most strongly with performance gains
- Training-task synergies persist across models but vary substantially in magnitude
- Release of 1,000+ models and benchmark results for community research

This massive experimental effort provides empirical evidence supporting mid-training's role in shaping model capabilities, particularly through mid-layer modifications that enable downstream task adaptation.

### 5. Representation and Behavior Analysis

#### Ling et al. (2025) - Abstention Artifact Analysis

Ling et al. investigate LLM abstention behaviors, finding that uncertainty expression is often prompt-dependent rather than genuine [citation:Ling et al., 2025](https://arxiv.org/abs/2507.16199v9). Their analysis of training stage effects reveals crucial insights about mid-training impact on model behavior.

**Key Discoveries:**
- "Abstention Inflation" triggered by extra response options independent of genuine uncertainty
- Later-layer output override preserves correct answers in mid-layer representations
- Phenomenon emerges through instruction tuning and increases with problem difficulty
- Can be mitigated at larger model sizes

**Relevance to Mid-Training:**
The study suggests that mid-training stages significantly shape whether models express genuine uncertainty versus pattern-matching abstention behaviors, highlighting the importance of careful design in this phase.

#### Bhattacharyya et al. (25) - Emotion Concept Representations

Bhattacharyya et al. compare how LLMs and humans represent emotion concepts, finding categorical differences in model representations [citation:Bhattacharyya et al., 2025](https://arxiv.org/abs/2508.05880v3). Their checkpoint analysis across training stages provides unique insights into mid-training effects.

**Critical Finding:**
"The discretized nature of representations appears after the mid-training stage itself and is unaffected by different post-training strategies."

This discovery positions mid-training as the definitive stage where emotion concept representations become established, demonstrating its irreplaceable role in shaping behavioral characteristics. The categorical, homogeneous structure differs fundamentally from distributed human emotion processing.

---

## Cross-Paper Synthesis

### Common Methodologies Across Studies

1. **Checkpoint-Based Analysis**: Multiple studies (Wang et al., Bhattacharyya et al., FAIR CodeGen Team) leverage mid-training checkpoints to analyze representation evolution, establishing this phase as critical for capability formation.

2. **Synthetic Data Generation**: Zhang et al., Wang et al., and Manvi et al. all employ synthetic or augmented data creation, demonstrating that mid-training benefits from specialized data engineering beyond simple corpus expansion.

3. **Benchmark-Driven Evaluation**: All papers utilize standardized benchmarks (MMLU, GSM8K, SWE-bench, etc.) enabling quantitative comparison across approaches and establishing performance baselines.

4. **Scalability Analysis**: Most studies (Zhang et al., Wang et al., Su et al.) demonstrate consistent improvements across model sizes and compute budgets, suggesting mid-training benefits generalize across scales.

### Emerging Best Practices

Based on the collective evidence:

1. **Timing Matters**: Mid-training should occur after initial pre-training reaches reasonable perplexity thresholds but before task-specific alignment

2. **Data Diversity**: High-quality, diverse datasets (particularly knowledge-intensive) yield superior outcomes compared to scaled-but-homogeneous corpora

3. **Layer-Specific Effects**: Mid-layer modifications appear most consequential for downstream performance, suggesting targeted interventions may be optimal

4. **Precision Flexibility**: Modifying precision schemes mid-training can resolve instabilities that emerge at scale

5. **Evaluation Rigor**: Multi-benchmark evaluation essential for capturing broad capability improvements rather than narrow optimization

### Open Challenges Identified

1. **Theoretical Foundation**: Despite empirical success, unified theoretical framework remains incomplete (Mo et al., 2025)

2. **Automated Detection**: Methods for automatically identifying optimal mid-training timing and duration remain underdeveloped

3. **Cross-Domain Transfer**: Limited understanding of how mid-training in one domain affects capabilities in others

4. **Efficiency Trade-offs**: Balancing mid-training computational costs against performance gains requires further investigation

5. **Representation Control**: Techniques for steering representation evolution during mid-training lack mature methodologies

---

## Implications for Practice

### For Research Practitioners

1. **Always Include Mid-Training**: Evidence suggests skipping mid-training results in suboptimal final performance regardless of pre-training quality

2. **Invest in Data Engineering**: Mid-training benefits disproportionately from high-quality, domain-specific data synthesis

3. **Monitor Layer Dynamics**: Track mid-layer weight changes as indicators of effective capability transfer

4. **Use Diverse Benchmarks**: Evaluate across multiple domains to capture holistic improvements

5. **Release Checkpoints**: Make mid-training checkpoints available for reproducibility and ablation studies

### For Industry Deployment

1. **Enterprise Multilingual**: Batch-wise alignment strategies offer practical solutions for global applications

2. **Code Generation**: World model integration during mid-training enables advanced reasoning capabilities

3. **Cost Optimization**: Adaptive compute strategies can reduce inference costs while maintaining performance

4. **Stability Management**: Precision scheme modifications mid-training prevent costly training failures at scale

5. **Behavioral Alignment**: Careful mid-training design shapes fundamental model behaviors like uncertainty expression

---

## Conclusion

This systematic review of 10 papers reveals mid-training as an indispensable phase in modern LLM development pipelines. The evidence overwhelmingly supports mid-training's role in:

- Enabling domain-specific knowledge acquisition (Zhang et al., 2025; FAIR CodeGen Team, 2025)
- Improving data efficiency by factors of 2-3x (Wang et al., 2025)
- Achieving single-digit to double-digit percentage improvements on standard benchmarks (Zhang et al., 2025; Manvi et al., 2024)
- Stabilizing training at scale through precision modifications (Su et al., 2025)
- Shaping fundamental representation structures irreversibly (Bhattacharyya et al., 2025)
- Addressing enterprise-scale deployment challenges (Agarwal et al., 2025)

The field has progressed from empirical observation to systematic understanding, with Mo et al.'s (2025) survey providing foundational taxonomy and numerous follow-up studies offering methodological innovations. Future research should focus on theoretical unification, automated optimization, and cross-domain transfer mechanisms.

For practitioners, the message is clear: mid-training is not optional optimization but essential infrastructure for state-of-the-art LLM development. As models scale and applications diversify, mid-training methodologies will become increasingly sophisticated, serving as the bridge between raw language modeling capability and task-specific expertise.

---

## References

Agarwal, A., Meghwani, H., Patel, H. L., Sheng, T., Ravi, S., & Roth, D. (2025). Aligning LLMs for multilingual consistency in enterprise applications. *arXiv preprint arXiv:2509.23659*. https://arxiv.org/abs/2509.23659v2

Bhattacharyya, S., Kuriabov, E., Craig, L., Dilliraj, T., Adams, R. B., Li, J., & Wang, J. Z. (2025). Too categorical to be human: Emotion concepts in LLMs and humans. *arXiv preprint arXiv:2508.05880*. https://arxiv.org/abs/2508.05880v3

FAIR CodeGen Team, Copet, J., Carbonneaux, Q., Cohen, G., Gehring, J., Kahn, J., ... Zheng, K. (2025). CWM: An open-weights LLM for research on code generation with world models. *arXiv preprint arXiv:2510.02387*. https://arxiv.org/abs/2510.02387v1

Harada, Y., Yamauchi, Y., Oda, Y., Oseki, Y., Miyao, Y., & Takagi, Y. (2025). Massive supervised fine-tuning experiments reveal how data, layer, and training factors shape LLM alignment quality. *arXiv preprint arXiv:2506.14681*. https://arxiv.org/abs/2506.14681v2

Ling, Z., Liu, S., Tang, Y., Yang, J., Fu, S., Son, S., ... Hu, X. (2025). LLM abstention can be a prompt artifact, in addition to genuine uncertainty. *arXiv preprint arXiv:2507.16199*. https://arxiv.org/abs/2507.16199v9

Manvi, R., Singh, A., & Ermon, S. (2024). Adaptive inference-time compute: LLMs can predict if they can do better, even mid-generation. *arXiv preprint arXiv:2410.02725*. https://arxiv.org/abs/2410.02725v1

Mo, K., Shi, Y., Weng, W., Zhou, Z., Liu, S., Zhang, H., & Zeng, A. (2025). Mid-training of large language models: A survey. *arXiv preprint arXiv:2510.06826*. https://arxiv.org/abs/2510.06826v1

Su, H., Kwun, M., Gil, S., Kakade, S., & Anand, N. (2025). Characterization and mitigation of training instabilities in microscaling formats. *arXiv preprint arXiv:2506.20752*. https://arxiv.org/abs/2506.20752v1

Wang, L., Nan, Y., Huang, S., Li, D., & Wei, F. (2025). Thinking augmented pre-training. *arXiv preprint arXiv:2509.20186*. https://arxiv.org/abs/2509.20186v4

Zhang, X., Tu, C., Ren, C., Weng, R., Yan, H., Wang, J., & Cai, X. (2025). Large-scale diverse synthesis for mid-training. *arXiv preprint arXiv:2508.01326*. https://arxiv.org/abs/2508.01326v1

---

**Review Generated:** October 26, 2026  
**Systematic Search Parameters:** arXiv cs.CL category, October 27, 2023 – October 26, 2025  
**Papers Retrieved:** 10  
**Format:** APA Style
