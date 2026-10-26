# Systematic Literature Review: Knowledge Distillation of Language Models

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "knowledge distillation language models", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in knowledge distillation (KD) for language models, focusing on 10 arXiv papers published between late 2024 and 2026. The surveyed literature reveals a field rapidly evolving beyond traditional output-level distillation toward more sophisticated approaches that target intermediate representations, reasoning capabilities, and domain-specific applications. Key developments include symmetric alignment of thought processes through logit lenses, chain-of-thought enhanced distillation for reasoning transfer, and mid-training strategies that favor reasoning over factual recall. The collective work demonstrates that KD can reduce model memorization by over 50% while maintaining 70-95% of teacher capabilities, enabling deployment on resource-constrained platforms across diverse domains including biomedical, energy modeling, and temporal knowledge graph reasoning.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "knowledge distillation language models", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Advanced Distillation Mechanisms Beyond Output Alignment

Traditional knowledge distillation focuses on aligning final output distributions between teacher and student models. Recent work has moved beyond this paradigm to capture richer information from intermediate layers and thought processes. DistillLens introduces symmetric knowledge distillation through logit lenses, projecting intermediate hidden states into vocabulary space and enforcing structural alignment using symmetric divergence objectives (Dhakal et al., 2026). This approach prevents both overconfidence and underconfidence while preserving high-entropy information conduits essential for final deduction. Similarly, Multi-Aspect Knowledge Distillation (MaKD) captures fine-grained information by mimicking self-attention and feed-forward modules in greater depth, rather than focusing only on layer-level knowledge distribution (Liu et al., 2026). Delta Knowledge Distillation addresses the limitation that student and teacher output distributions may not share the same optimal representation space by explicitly preserving the distributional shift introduced during the teacher's supervised finetuning (Cao et al., 2025).

### Theme 2: Reasoning and Chain-of-Thought Enhanced Distillation

A significant thread in recent KD research focuses on transferring reasoning capabilities rather than just factual knowledge. Chain-of-Thought (CoT) prompting has emerged as a critical technique for distilling reasoning from larger to smaller models. Do et al. (2025) demonstrate that CoT prompting improves white-box KD effectiveness for transferring reasoning capability, with distilled models achieving better average performance on BIG-Bench-Hard reasoning and understanding tasks. Building on this, Paredes La Torre et al. (2026) integrate CoT prompting with Group Relative Policy Optimization for coding tasks, achieving up to 93.5% Rouge-L while retaining 70-95% of teacher capabilities across English, Spanish, and code generation tasks. However, He et al. (2026) reveal that the timing of distillation matters critically: forward KL distillation during mid-training favors reasoning gains but slows factual recall acquisition, leading to their Switch Distillation approach that routes based on teacher predictive entropy to achieve 1.61-1.71x reasoning performance while preserving 96.7-96.8% of factual recall.

### Theme 3: Domain-Specific Applications and Specialized Frameworks

Knowledge distillation is increasingly being adapted for domain-specific applications with unique requirements. In the biomedical domain, Xiao et al. (2025) propose a knowledge-driven agentic framework where specialized agents guided by the Medical Subject Headings hierarchy autonomously extract and synthesize high-quality textual data to generate domain-specific question-answer pairs, enabling distilled models to outperform both strong life sciences LLM baselines and advanced proprietary models including GPT-4 with MedPrompt. For temporal knowledge graph reasoning, Xing et al. (2026) leverage LLMs as teachers to transfer both structural and temporal reasoning capabilities to compact student models, achieving favorable trade-offs between reasoning accuracy, computational efficiency, and practical deployability. In sustainability research, Takrouri et al. (2025) employ knowledge distillation for household energy modeling across six countries, generating culturally sensitive, behavior-specific data that captures how cultural, climatic, and behavioral factors converge to shape carbon emissions.

### Theme 4: Memorization and Privacy Dynamics

Understanding what distilled models memorize from their training data has emerged as a critical concern, particularly for privacy implications. Borkar et al. (2026) examine memorization dynamics across the KD pipeline using three LLM families and three datasets, finding that distilled models memorize significantly less training data than standard fine-tuning, reducing memorization by more than 50%. Their work reveals that some examples are inherently easier to memorize and account for over 95% of memorization during distillation, and that student memorization is predictable prior to distillation using features based on zlib entropy, KL divergence, and perplexity. Critically, they find that hard distillation inherits 2.7× more teacher-specific examples than soft distillation, posing greater privacy risk despite similar overall memorization rates. This has important implications for choosing distillation strategies when deploying models in privacy-sensitive contexts.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that traditional output-level distillation is insufficient for capturing the full range of teacher capabilities, particularly for reasoning tasks. Multiple papers converge on the finding that intermediate representation alignment (Dhakal et al., 2026; Liu et al., 2026) and reasoning-focused techniques (Do et al., 2025; Paredes La Torre et al., 2026) significantly improve student performance. There is also broad agreement that domain-specific adaptation and specialized frameworks yield better results than generic distillation approaches (Xiao et al., 2025; Xing et al., 2026; Takrouri et al., 2025).

**Disagreements**: The literature reveals tension around the timing and strategy of distillation. While most work assumes distillation during pre-training or fine-tuning, He et al. (2026) demonstrate that mid-training distillation behaves fundamentally differently, slowing factual recall despite reasoning gains—challenging the assumption that distillation uniformly benefits all capabilities. Additionally, there is disagreement implicit in the choice between hard and soft distillation: Borkar et al. (2026) show hard distillation inherits 2.7× more teacher-specific examples, suggesting soft distillation may be preferable for privacy, while other work does not explicitly address this trade-off.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly state their limitations in the abstract, suggesting a need for more transparent reporting of methodological constraints and boundary conditions. Second, while several papers address reasoning transfer, there is limited work on distilling other specialized capabilities such as creativity, humor, or nuanced social understanding. Third, the privacy implications identified by Borkar et al. (2026) raise questions about optimal distillation strategies for sensitive domains that remain underexplored. Fourth, most work focuses on English or a small set of languages, with only Paredes La Torre et al. (2026) explicitly addressing multilingual distillation—there is a gap in comprehensive cross-lingual KD research. Finally, the environmental and computational costs of different KD approaches are not systematically compared, leaving open questions about the true efficiency gains of various methods.

## Per-Paper Annotations

### Borkar et al. (2026)

**Research question**: How does training data memorization behave in knowledge distillation setups compared to standard fine-tuning?
**Methodology**: The study examines memorization across the KD pipeline using three LLM families (Pythia, OLMo-2, Qwen-3) and three datasets (FineWeb, Wikitext, Nemotron-CC-v2), analyzing factors like zlib entropy, KL divergence, and perplexity to predict memorization.
**Key findings**:
- Distilled models memorize significantly less training data than standard fine-tuning, reducing memorization by more than 50%
- Some examples are inherently easier to memorize and account for over 95% of memorization during distillation
- Student memorization is predictable prior to distillation using features based on zlib entropy, KL divergence, and perplexity
- Hard distillation inherits 2.7× more teacher-specific examples than soft distillation, posing greater privacy risk despite similar overall memorization rates
**Limitations**: not stated in abstract

### Cao et al. (2025)

**Research question**: How can knowledge distillation be improved when student and teacher output distributions do not share the same optimal representation space?
**Methodology**: The authors propose Delta Knowledge Distillation (Delta-KD), an extension of token-level KD that encourages the student to approximate an optimal representation space by explicitly preserving the distributional shift Delta introduced during the teacher's supervised finetuning.
**Key findings**:
- Delta-KD addresses the limitation that prior work assumes student and teacher output distributions share the same optimal representation space
- The method explicitly preserves the distributional shift Delta from the teacher's supervised finetuning
- Empirical results on ROUGE metrics demonstrate Delta-KD substantially improves student performance
- Delta-KD preserves more of the teacher's knowledge compared to standard token-level KD
**Limitations**: not stated in abstract

### Dhakal et al. (2026)

**Research question**: How can knowledge distillation be improved by aligning the intermediate thought processes of student and teacher models rather than only optimizing final outputs?
**Methodology**: The paper introduces DistillLens, a framework that projects intermediate hidden states into vocabulary space via the Logit Lens and enforces structural alignment using a symmetric divergence objective to symmetrically align the evolving thought processes of student and teacher models.
**Key findings**:
- DistillLens symmetrically aligns the evolving thought processes of student and teacher models
- The symmetric divergence constraint imposes a dual-sided penalty, preventing both overconfidence and underconfidence
- The method preserves high-entropy information conduits essential for final deduction
- DistillLens consistently outperforms standard KD and feature-transfer baselines on diverse instruction-following benchmarks across GPT-2 and Llama architectures
**Limitations**: not stated in abstract

### Do et al. (2025)

**Research question**: What is the role and effectiveness of Chain-of-Thought prompting in distilling reasoning capability from larger LLMs to smaller LLMs using white-box knowledge distillation?
**Methodology**: The paper conducts white-box KD experiments using LLMs from the Qwen and Llama2 families, employing CoT data from the CoT-Collection dataset, and evaluates the distilled models on natural language reasoning and understanding tasks from the BIG-Bench-Hard benchmark.
**Key findings**:
- Chain-of-Thought prompting improves white-box KD effectiveness for transferring reasoning capability
- Distilled models achieve better average performance in natural language reasoning tasks from BIG-Bench-Hard
- Distilled models achieve better average performance in natural language understanding tasks from BIG-Bench-Hard
- CoT data from the CoT-Collection dataset enables effective knowledge transfer from larger to smaller LLMs
**Limitations**: not stated in abstract

### He et al. (2026)

**Research question**: How does the effectiveness of logit-based knowledge distillation vary across different training stages, particularly during mid-training versus pre-training?
**Methodology**: Through controlled experiments, the paper investigates forward KL distillation with post-trained teachers during mid-training, traces stage dependence to asymmetry in teacher confidence across data domains, and proposes Switch Distillation that distills on tokens where the teacher is confident using teacher predictive entropy as a routing signal.
**Key findings**:
- Forward KL distillation behaves fundamentally differently during mid-training compared to pre-training
- During mid-training, forward KD slows factual recall acquisition despite continued reasoning gains
- Teachers are more confident on procedural than knowledge-intensive data, while students acquire low-entropy factual knowledge earlier in training
- Switch Distillation achieves 1.61-1.71x reasoning performance and 1.13-1.19x knowledge and commonsense performance relative to standard NTP
- Switch Distillation preserves 96.7-96.8% of factual recall and maintains gains after post-training
**Limitations**: not stated in abstract

### Liu et al. (2026)

**Research question**: How can knowledge distillation capture fine-grained information that existing layer-focused methods may lose during alignment?
**Methodology**: The Multi-aspect Knowledge Distillation (MaKD) method mimics self-attention and feed-forward modules in greater depth to capture rich language knowledge information at different aspects, rather than focusing only on knowledge distribution among layers.
**Key findings**:
- MaKD addresses the issue that existing methods focusing only on layer-level knowledge distribution may cause loss of fine-grained information
- The method captures rich language knowledge at different aspects by mimicking self-attention and feed-forward modules in greater depth
- MaKD achieves competitive performance compared with various strong baselines with the same storage parameter budget
- The method performs well in distilling auto-regressive architecture models
**Limitations**: not stated in abstract

### Paredes La Torre et al. (2026)

**Research question**: Can knowledge distillation combined with chain-of-thought reinforcement learning produce compact, efficient models suitable for resource-constrained deployment?
**Methodology**: The framework uses Qwen 3B as teacher and Qwen 0.5B as student, applying knowledge distillation across English Dolly-15k, Spanish Dolly-15k, and code datasets (BugNet, PyTorrent), with chain-of-thought prompting and Group Relative Policy Optimization for coding tasks, followed by 4-bit weight quantization.
**Key findings**:
- The distilled student retains 70% to 91% of teacher capability in English tasks
- Performance reaches up to 95% in Spanish tasks
- Coding tasks achieve up to 93.5% Rouge-L with chain-of-thought guided reinforcement learning
- Integrating chain-of-thought prompting with Group Relative Policy Optimization improves reasoning coherence and solution correctness compared to knowledge distillation alone
- Post-training 4-bit weight quantization reduces memory footprint and inference latency
**Limitations**: not stated in abstract

### Takrouri et al. (2025)

**Research question**: How can Large Language Models be integrated into energy modeling to generate realistic, culturally sensitive, and behavior-specific data for household energy usage across diverse geographies?
**Methodology**: The study employs and compares five different LLMs to systematically produce family structures, weather patterns, and daily consumption profiles for households in six distinct countries using a four-stage methodology that synthesizes contextual daily data including culturally nuanced activities, realistic weather ranges, HVAC operations, and distinct energy signatures.
**Key findings**:
- LLMs can generate realistic, culturally sensitive, and behavior-specific data for household energy usage across diverse geographies
- The four-stage methodology synthesizes contextual daily data including culturally nuanced activities and realistic weather ranges
- An alternative strategy allows external weather datasets to be directly integrated, bypassing intermediate weather modeling stages
- The resulting dataset provides insights into how cultural, climatic, and behavioral factors converge to shape carbon emissions
- The approach demonstrates how prompt engineering combined with knowledge distillation can advance sustainable energy research
**Limitations**: not stated in abstract

### Xing et al. (2026)

**Research question**: How can knowledge distillation be adapted for temporal knowledge graph reasoning to enable deployment on resource-constrained platforms while maintaining reasoning accuracy?
**Methodology**: The proposed framework leverages large language models as teacher models to guide distillation, integrating large-scale public knowledge with task-specific temporal information to transfer both structural and temporal reasoning capabilities to lightweight student models.
**Key findings**:
- Existing TKG reasoning models rely on large parameter sizes and intensive computation, hindering deployment on resource-constrained platforms
- Most existing compression techniques are designed for static knowledge graphs and fail to capture temporal dependencies
- The framework leverages LLMs as teachers to transfer structural and temporal reasoning capabilities to compact student models
- Extensive experiments on multiple benchmark datasets show the method outperforms strong baselines
- The approach achieves a favorable trade-off between reasoning accuracy, computational efficiency, and practical deployability
**Limitations**: not stated in abstract

### Xiao et al. (2025)

**Research question**: How can a knowledge-driven, agentic framework address the insufficient quantity and quality of open-source annotated scientific corpora for biomedical LLM training?
**Methodology**: The paper proposes a collaborative multi-agent architecture where specialized agents guided by the Medical Subject Headings (MeSH) hierarchy autonomously extract, synthesize, and self-evaluate high-quality textual data from scientific literature to generate domain-specific question-answer pairs.
**Key findings**:
- Language models trained on the multi-agent distilled datasets achieve notable improvements in biomedical question-answering tasks
- The distilled models outperform both strong life sciences LLM baselines and advanced proprietary models
- The AI-Ready dataset enables Llama3-70B to surpass GPT-4 with MedPrompt and Med-PaLM-2 despite their larger scale
- Ablation studies validate the effectiveness and synergy of each agent within the framework
**Limitations**: not stated in abstract

## References

Borkar, J., Chadha, K., Mireshghallah, N., Zhang, Y., Veliche, I.-E., Mitra, A., Smith, D. A., Xu, Z., & Garcia-Olano, D. (2026). Memorization dynamics in knowledge distillation for language models. arXiv. https://arxiv.org/abs/2601.15394

Cao, Y., Kang, Y., Xing, Z., & Jiang, R. (2025). Delta knowledge distillation for large language models. arXiv. https://arxiv.org/abs/2509.14526

Dhakal, M., Jinadu, U., Budathoki, A., Sunderraman, R., & Ding, Y. (2026). DistillLens: Symmetric knowledge distillation through logit lens. arXiv. https://arxiv.org/abs/2602.13567

Do, C.-T., Doddipatla, R., & Knill, K. (2025). Effectiveness of Chain-of-Thought in distilling reasoning capability from large language models. arXiv. https://arxiv.org/abs/2511.05184

He, J., Yen, H., Li, S. S., Li, M., Zeng, H., Xia, Y., Zhang, B., Zhao, Z., Zhang, Q., Koh, P. W., Zettlemoyer, L., & Yih, W.-t. (2026). Knowledge distillation during mid-training favors reasoning over factual recall. arXiv. https://arxiv.org/abs/2609.01532

Liu, Z., Mao, Y., Xu, J., Peng, X., & Huang, K. (2026). Multi-aspect knowledge distillation for language model with low-rank factorization. arXiv. https://arxiv.org/abs/2604.03110

Paredes La Torre, A., Flores, B., & Rodriguez, D. (2026). Knowledge distillation for large language models. arXiv. https://arxiv.org/abs/2603.13765

Takrouri, M., Cuadrado, N. M., & Takáč, M. (2025). Knowledge distillation from large language models for household energy modeling. arXiv. https://arxiv.org/abs/2502.03034

Xing, W., Song, W., Lin, S., Wu, C., Li, Z., & Wang, M. (2026). Knowledge distillation for temporal knowledge graph reasoning with large language models. arXiv. https://arxiv.org/abs/2601.00202

Xiao, M., Cai, X., Long, Q., Wang, C., Zhou, Y., & Zhu, H. (2025). Knowledge-driven agentic scientific corpus distillation framework for biomedical large language models training. arXiv. https://arxiv.org/abs/2504.19565
