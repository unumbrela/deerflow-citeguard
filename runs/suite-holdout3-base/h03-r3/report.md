# Systematic Literature Review: Knowledge Distillation of Language Models

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "knowledge distillation", filtered to category cs.CL, published between 2024-10-26 and 2025-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in knowledge distillation (KD) for language models, surveying 10 arXiv papers from the cs.CL category published within the last two years. The literature reveals a field rapidly evolving beyond traditional output-level distillation toward more sophisticated approaches that address intermediate representation alignment, parameter efficiency, and adaptive learning frameworks. Collectively, these papers demonstrate that modern KD methods can retain 70-95% of teacher model capabilities while significantly reducing model size and computational requirements. Key innovations include symmetric alignment of intermediate thought processes, integration with parameter-efficient fine-tuning methods like LoRA, progressive teacher scaling strategies, and domain-specific adaptations for tasks ranging from neural machine translation to energy modeling. The field shows strong convergence on the importance of preserving fine-grained information during distillation, though approaches diverge on whether to focus on architectural modifications, training dynamics, or representation space alignment.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "knowledge distillation", filtered to category cs.CL, published between 2024-10-26 and 2025-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search was restricted to cs.CL category, potentially missing relevant work from cs.LG or cs.AI categories that also addresses language model distillation.

## Themes

### Theme 1: Intermediate Representation Alignment

A prominent research direction focuses on moving beyond output-level distillation to align intermediate representations between teacher and student models. Traditional KD treats the teacher's intermediate layers as black boxes, optimizing only final outputs. DistillLens addresses this by projecting intermediate hidden states into vocabulary space via the Logit Lens and enforcing structural alignment using symmetric divergence objectives (Dhakal et al., 2026). This approach prevents both overconfidence and underconfidence in student models while preserving high-entropy information conduits essential for reasoning. Similarly, Multi-aspect Knowledge Distillation (MaKD) mimics self-attention and feed-forward modules in greater depth using low-rank factorization to capture fine-grained language knowledge at different aspects (Liu et al., 2026). Both approaches share the insight that layer-level or module-level knowledge transfer captures information that would be lost in output-only distillation, achieving competitive performance with the same storage parameter budget.

### Theme 2: Efficiency and Parameter Optimization

Several papers address the computational and parameter efficiency of knowledge distillation. LLM-NEO integrates Low-Rank Adaptation (LoRA) into the KD framework based on the observation that KD and LoRA follow the same underlying paradigm (Yang et al., 2024). This parameter-efficient approach outperforms various baselines on compressing Llama 2 and Llama 3.2 models while providing guidelines for hyperparameter selection. Sparse Logit Sampling tackles a different efficiency challenge: enabling cached teacher logits during pre-training without introducing bias (Anshumann et al., 2025). The authors prove that naive Top-K caching provides biased estimates, and instead propose an importance-sampling-based Random Sampling KD that provides unbiased estimates while requiring storage of significantly sparser logits. This method enables faster training with less than 10% overhead compared to cross-entropy based training while maintaining competitive performance across model sizes from 300M to 3B parameters.

### Theme 3: Progressive and Adaptive Learning Frameworks

Another theme involves making the distillation process itself more adaptive and progressive. Knowledge Distillation with Training Wheels formulates KD as an entropy-regularized value optimization problem where the student learns not only from the teacher during training but also learns when to seek teacher assistance at test-time within specified constraints (Liu et al., 2025). This approach uses constrained reinforcement learning to teach the model to assess relative difficulty and prioritize teacher help, unlocking operating points not available to Speculative Decoding. Evolving Knowledge Distillation takes a different progressive approach, training student models through a sequence of teachers with gradually increasing capacities (Zhang et al., 2026). This addresses the capacity gap problem in neural machine translation, narrowing the gap to the strongest teacher to just 0.08 BLEU on IWSLT-14. Both methods recognize that static teacher-student relationships limit distillation effectiveness and introduce dynamics that adapt during the learning process.

### Theme 4: Specialized Knowledge Integration

Several papers focus on integrating specialized forms of knowledge into the distillation process. Delta Knowledge Distillation addresses a fundamental limitation in token-level KD: the assumption that student and teacher output distributions share the same optimal representation space (Cao et al., 2025). By explicitly preserving the distributional shift (Delta) introduced during the teacher's supervised finetuning, Delta-KD encourages students to approximate optimal representation spaces, substantially improving performance on ROUGE metrics. Decoder-based Sense Knowledge Distillation integrates structured lexical knowledge such as word senses and relationships into decoder-style LLMs without requiring dictionary lookup at inference time (Wang et al., 2026). This enables generative models to inherit structured semantics while maintaining efficient training, significantly enhancing KD performance for decoder models across diverse benchmarks.

### Theme 5: Domain-Specific Applications

The surveyed literature demonstrates KD adaptation to specific domains beyond general language tasks. One paper applies LLM-based knowledge distillation to household energy modeling, using five different LLMs to generate realistic, culturally sensitive data for household energy usage across six countries (Takrouri et al., 2025). This approach addresses privacy-restricted data access in smart-grid research by generating family structures, weather patterns, and consumption profiles that capture unique energy signatures. Another domain-specific application targets neural machine translation, where Evolving Knowledge Distillation progressively trains students through increasingly capable teachers to bridge capacity gaps (Zhang et al., 2026). A third paper combines knowledge distillation with chain-of-thought reinforcement learning for multilingual and code generation tasks, achieving 70-95% retention of teacher capabilities across English, Spanish, and coding benchmarks (Paredes La Torre et al., 2026). These applications demonstrate KD's versatility while highlighting domain-specific challenges such as cultural nuance preservation and reasoning coherence.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that traditional output-level knowledge distillation is insufficient for capturing the full richness of teacher model knowledge. There is strong consensus across DistillLens, MaKD, and LLM-NEO that intermediate representations, parameter-efficient adaptations, or structured knowledge integration are necessary to preserve fine-grained information during distillation. Multiple papers independently demonstrate that their methods maintain competitive performance while significantly reducing computational requirements or model size. The literature also converges on the importance of empirical validation across multiple architectures and benchmarks, with most papers testing on GPT-2, Llama variants, or domain-specific benchmarks.

**Disagreements**: The literature diverges on whether architectural modifications or training dynamics offer the most promising path forward. Papers like LLM-NEO and MaKD focus on architectural changes (LoRA integration, low-rank factorization), while Training Wheels and Evolving KD emphasize adaptive training procedures. There is also tension between methods that require access to teacher internals (DistillLens, MaKD) versus those that work with cached outputs only (Sparse Logit Sampling). The domain-specific papers reveal disagreement about generalizability: some methods are designed specifically for NMT or energy modeling, while others claim broad applicability across language tasks.

## Gaps and Open Questions

Several gaps emerge from the collective limitations acknowledged across the surveyed papers. First, computational overhead remains underexplored: DistillLens does not discuss the cost of logit lens projections, Training Wheels omits details on test-time teacher query overhead, and MaKD may have increased complexity from deeper module mimicry. Second, validation against real-world data is limited: the energy modeling paper does not mention validation against actual consumption records, and several methods lack testing on production deployment scenarios. Third, scalability to very large models is rarely addressed, with most experiments confined to models in the 300M to 3B range. Fourth, cultural and linguistic bias in generated data is acknowledged but not systematically addressed in domain-specific applications. Finally, the generalization of domain-specific methods (particularly NMT-focused approaches) to other NLP domains requires further investigation. The literature would benefit from standardized benchmarks for comparing KD efficiency, systematic studies of computational trade-offs, and more attention to deployment considerations in resource-constrained environments.

## Per-Paper Annotations

### Anshumann et al. (2025)

**Research question**: How can knowledge distillation be efficiently applied to pre-training when teacher logits are cached, without introducing biased estimates from naive sparse approaches?

**Methodology**: Propose Random Sampling Knowledge Distillation using an importance-sampling-based method that provides unbiased estimates of teacher probability distribution while requiring storage of significantly sparser logits.

**Key findings**:
- Naive Top-K caching approaches provide biased estimates leading to suboptimal performance and calibration
- Random Sampling KD provides unbiased estimates and preserves gradients in expectation
- Method enables faster training with marginal overhead (<10%) compared to cross-entropy based training
- Maintains competitive performance compared to full distillation across model sizes from 300M to 3B
- Successfully applies cached logits to pre-training scenarios, which was previously unexplored

**Limitations**: Focus is primarily on pre-training applications; the method's effectiveness in other KD scenarios beyond pre-training remains less explored.

### Cao et al. (2025)

**Research question**: How can knowledge distillation address the problematic assumption that student and teacher output distributions share the same optimal representation space in token-level KD?

**Methodology**: Propose Delta Knowledge Distillation (Delta-KD), a novel extension of token-level KD that encourages the student to approximate an optimal representation space by explicitly preserving the distributional shift Delta introduced during the teacher's supervised finetuning.

**Key findings**:
- Delta-KD substantially improves student model performance compared to standard token-level KD
- The method preserves more of the teacher's knowledge by accounting for distributional shifts
- Empirical results on ROUGE metrics demonstrate the effectiveness of the approach
- Addresses a fundamental limitation in prior KD work regarding representation space assumptions

**Limitations**: Evaluation is limited to ROUGE metrics, which may not capture all aspects of model quality; the approach assumes access to teacher's SFT process information.

### Dhakal et al. (2026)

**Research question**: How can knowledge distillation better align student and teacher models' intermediate thought processes rather than treating them as black boxes?

**Methodology**: The authors introduce DistillLens, which projects intermediate hidden states into vocabulary space via Logit Lens and enforces structural alignment using a symmetric divergence objective that imposes dual-sided penalties on overconfidence and underconfidence.

**Key findings**:
- Symmetric divergence constraint prevents both overconfidence and underconfidence in student models
- Preserves high-entropy information conduits essential for final deduction
- Consistently outperforms standard KD and feature-transfer baselines on instruction-following benchmarks
- Demonstrates effectiveness across both GPT-2 and Llama architectures

**Limitations**: The abstract does not explicitly discuss computational overhead of logit lens projections or scalability to very large models.

### Liu et al. (2025)

**Research question**: How can knowledge distillation be extended to allow student models to learn when to seek teacher assistance at test-time within specified constraints?

**Methodology**: The authors formulate knowledge distillation as an entropy-regularized value optimization problem, adopt Path Consistency Learning with on-policy and off-policy demonstrations, and extend it using constrained reinforcement learning to incorporate test-time teacher reference within rules.

**Key findings**:
- Student models can learn both the learning material and the relative difficulty of different sections
- Model learns to prioritize when to seek teacher help at test-time
- Unlocks operating points not available to popular Speculative Decoding approach
- Demonstrates efficacy on translation and summarization tasks with observable trends in accuracy and teacher use

**Limitations**: The abstract does not detail the computational overhead of test-time teacher queries or how the constraint rules specifying test-time restrictions are determined.

### Liu et al. (2026)

**Research question**: How can fine-grained information loss be prevented in knowledge distillation when existing methods only focus on knowledge distribution among layers?

**Methodology**: Introduce Multi-aspect Knowledge Distillation (MaKD) that mimics self-attention and feed-forward modules in greater depth using low-rank factorization to capture rich language knowledge at different aspects.

**Key findings**:
- MaKD captures fine-grained information that layer-level KD methods miss
- Achieves competitive performance compared to strong baselines with the same storage parameter budget
- Method performs well in distilling auto-regressive architecture models
- Low-rank factorization enables efficient multi-aspect knowledge transfer
- Addresses information loss in the alignment process through deeper module mimicry

**Limitations**: Focus is on layer and module-level knowledge; the method may have increased computational complexity due to deeper module mimicry requirements.

### Paredes La Torre et al. (2026)

**Research question**: How can knowledge distillation combined with chain-of-thought reinforcement learning produce compact, efficient models suitable for resource-constrained deployment?

**Methodology**: The authors apply knowledge distillation from Qwen 3B to Qwen 0.5B across English Dolly-15k, Spanish Dolly-15k, and code datasets, integrate chain-of-thought prompting with Group Relative Policy Optimization on CoT-annotated Codeforces data, and apply post-training 4-bit weight quantization.

**Key findings**:
- Distilled student retains 70% to 91% of teacher capability in English tasks
- Achieves up to 95% retention in Spanish tasks and up to 93.5% Rouge-L in code tasks
- Chain-of-thought with Group Relative Policy Optimization improves reasoning coherence and solution correctness compared to KD alone
- 4-bit weight quantization further reduces memory footprint and inference latency
- Produces compact models suitable for deployment in resource-constrained settings

**Limitations**: The abstract does not specify which tasks show the largest performance gaps between teacher and student, or whether the approach generalizes to non-English code-related tasks.

### Takrouri et al. (2025)

**Research question**: How can LLMs generate realistic, culturally sensitive household energy usage data to overcome privacy-restricted data access in smart-grid research?

**Methodology**: The study employs five different LLMs to systematically produce family structures, weather patterns, and daily consumption profiles for households across six countries using a four-stage methodology, with an alternative strategy that directly integrates external weather datasets.

**Key findings**:
- LLMs can generate culturally nuanced activities and realistic weather ranges for energy modeling
- Creates distinct 'energy signatures' that capture unique household consumption footprints
- Provides insights into how cultural, climatic, and behavioral factors converge to shape carbon emissions
- Offers a cost-effective avenue for scenario-based energy optimization and climate mitigation
- Prompt engineering combined with knowledge distillation can advance sustainable energy research

**Limitations**: The abstract does not mention validation of generated data against real energy consumption records or address potential biases in LLM-generated cultural patterns.

### Wang et al. (2026)

**Research question**: How can structured lexical knowledge such as word senses and relationships be incorporated into decoder-style generative LLMs during knowledge distillation without requiring dictionary lookup at inference?

**Methodology**: The authors introduce Decoder-based Sense Knowledge Distillation (DSKD), a framework that integrates lexical resources into decoder-style LLM training without requiring dictionary lookup at inference time.

**Key findings**:
- DSKD significantly enhances knowledge distillation performance for decoder models
- Enables generative models to inherit structured semantics from lexical resources
- Maintains efficient training without inference-time dictionary overhead
- Demonstrates effectiveness across diverse benchmarks

**Limitations**: The abstract does not specify which lexical resources were used, the computational cost of integration during training, or performance on specific semantic tasks.

### Yang et al. (2024)

**Research question**: How can parameter efficiency be improved in knowledge distillation for LLMs by leveraging insights from Low-Rank Adaptation (LoRA)?

**Methodology**: Propose LLM-NEO, a parameter-efficient KD method that integrates LoRA into the knowledge distillation framework based on the observation that KD and LoRA follow the same paradigm.

**Key findings**:
- KD and LoRA follow the same underlying paradigm, enabling their integration
- LLM-NEO outperforms various baselines on compressing Llama 2 and Llama 3.2 models
- The method demonstrates robustness across variants of LoRA
- Provides valuable guidelines for hyperparameter selection in LLM-NEO
- Code and trained models are publicly available for reproducibility

**Limitations**: Method is tied to LoRA architecture variants; effectiveness may depend on specific model architectures and the provided hyperparameter guidelines.

### Zhang et al. (2026)

**Research question**: How can knowledge distillation effectiveness be maintained when there is a large capacity gap between teacher and student models in Neural Machine Translation?

**Methodology**: Propose Evolving Knowledge Distillation (EKD), a progressive training framework where the student model learns from a sequence of teachers with gradually increasing capacities.

**Key findings**:
- EKD leads to consistent improvements at each training stage across multiple benchmarks
- On IWSLT-14, achieves 34.24 BLEU, narrowing gap to strongest teacher (34.32 BLEU) to just 0.08 BLEU
- Similar performance trends observed on WMT-17 and WMT-23 datasets
- Effectively bridges the capacity gap between compact student and larger teacher models
- Enables lightweight models to achieve performance close to much larger teachers

**Limitations**: Approach is specifically designed for Neural Machine Translation tasks; generalization to other NLP domains beyond NMT requires further investigation.

## References

Anshumann, Zaidi, M. A., Kedia, A., Ahn, J., Kwon, T., Lee, K., Lee, H., & Lee, J. (2025). Sparse logit sampling: Accelerating knowledge distillation in LLMs. arXiv. https://arxiv.org/abs/2503.16870

Cao, Y., Kang, Y., Xing, Z., & Jiang, R. (2025). Delta knowledge distillation for large language models. arXiv. https://arxiv.org/abs/2509.14526

Dhakal, M., Jinadu, U., Budathoki, A., Sunderraman, R., & Ding, Y. (2026). DistillLens: Symmetric knowledge distillation through logit lens. arXiv. https://arxiv.org/abs/2602.13567

Liu, G., Ramachandran, A., Gangwani, T., Fu, Y., & Sethy, A. (2025). Knowledge distillation with training wheels. arXiv. https://arxiv.org/abs/2502.17717

Liu, Z., Mao, Y., Xu, J., Peng, X., & Huang, K. (2026). Multi-aspect knowledge distillation for language model with low-rank factorization. arXiv. https://arxiv.org/abs/2604.03110

Paredes La Torre, A., Flores, B., & Rodriguez, D. (2026). Knowledge distillation for large language models. arXiv. https://arxiv.org/abs/2603.13765

Takrouri, M., Cuadrado, N. M., & Takáč, M. (2025). Knowledge distillation from large language models for household energy modeling. arXiv. https://arxiv.org/abs/2502.03034

Wang, Q., Zaki, M. J., Kollias, G., & Kalantzis, V. (2026). Decoder-based sense knowledge distillation. arXiv. https://arxiv.org/abs/2602.22351

Yang, R., Wu, T., Wang, J., Hu, P., Wu, Y.-C., Wong, N., & Yang, Y. (2024). LLM-NEO: Parameter efficient knowledge distillation for large language models. arXiv. https://arxiv.org/abs/2411.06839

Zhang, X., Zhang, H., & Huang, X. (2026). Evolving knowledge distillation for lightweight neural machine translation. arXiv. https://arxiv.org/abs/2605.09924
