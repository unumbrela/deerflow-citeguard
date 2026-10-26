# Systematic Literature Review: Knowledge Distillation of Language Models

**Date**: 2025-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "knowledge distillation language models", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

Knowledge distillation (KD) for language models has evolved into a multifaceted research area addressing both efficiency and capability transfer challenges. The surveyed literature reveals three dominant directions: (1) architectural innovations that improve distillation mechanisms through intermediate representation alignment and multi-aspect knowledge transfer, (2) strategic applications of distillation during different training stages to optimize reasoning versus factual recall trade-offs, and (3) domain-specific adaptations for biomedical, energy, and temporal reasoning tasks. Recent work demonstrates that distilled models can retain 70-95% of teacher capabilities while achieving significant reductions in memorization (over 50%) and computational requirements. Chain-of-thought prompting has emerged as a critical enhancer for reasoning distillation, while novel methods like Delta-KD and Switch Distillation address fundamental limitations in representation space alignment and stage-dependent behavior.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-26 using the query "knowledge distillation language models", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Innovations in Distillation Mechanisms

Recent work has moved beyond simple output logit matching to capture richer intermediate representations and multi-aspect knowledge. DistillLens introduced symmetric knowledge distillation through logit lens, projecting intermediate hidden states into vocabulary space and enforcing structural alignment using symmetric divergence objectives (Dhakal et al., 2026). This approach prevents both overconfidence and underconfidence while preserving high-entropy information conduits essential for final deduction. Similarly, Multi-aspect Knowledge Distillation (MaKD) captures fine-grained information lost in layer-distribution-focused methods by mimicking self-attention and feed-forward modules in greater depth, combined with low-rank factorization (Liu et al., 2026). These architectural innovations consistently outperform standard KD and feature-transfer baselines on diverse instruction-following benchmarks.

### Theme 2: Training Stage Optimization and Stage-Dependent Behavior

The timing of distillation significantly impacts what knowledge is transferred. He et al. (2026) demonstrated that forward KL distillation behaves fundamentally differently during mid-training compared to pre-training, slowing factual recall acquisition despite continued reasoning gains. Their Switch Distillation method addresses this by distilling only on tokens where the teacher is confident, using predictive entropy as a routing signal, achieving 1.61-1.71x reasoning performance while preserving 96.7-96.8% factual recall. This stage-aware approach represents a significant advance over treating distillation as a uniform process across all training phases.

### Theme 3: Representation Space Alignment and Distributional Shift Preservation

A critical limitation of traditional token-level KD is the assumption that student and teacher share the same optimal representation space. Delta Knowledge Distillation (Delta-KD) explicitly preserves the distributional shift introduced during the teacher's supervised finetuning, encouraging the student to approximate an optimal representation space while maintaining the teacher's unique adaptations (Cao et al., 2025). This approach substantially improves student performance on ROUGE metrics compared to standard token-level KD, demonstrating that representation space misalignment is a key bottleneck in distillation effectiveness.

### Theme 4: Chain-of-Thought Enhanced Reasoning Distillation

Chain-of-thought (CoT) prompting has emerged as a powerful enhancer for distilling reasoning capabilities. Do et al. (2025) showed that CoT improves white-box KD effectiveness for reasoning tasks, with distilled models achieving better average performance on BIG-Bench-Hard natural language reasoning and understanding tasks. Paredes La Torre et al. (2026) integrated CoT with Group Relative Policy Optimization, demonstrating that this combination improves reasoning coherence and solution correctness compared to KD alone, while 4-bit weight quantization reduces memory footprint and inference latency without significant capability loss.

### Theme 5: Domain-Specific Distillation Applications

Knowledge distillation has been successfully adapted to specialized domains beyond general language tasks. Xiao et al. (2025) developed a knowledge-driven agentic framework for biomedical corpus distillation, where multi-agent architectures guided by Medical Subject Headings hierarchy generate high-quality domain-specific question-answer pairs, enabling Llama3-70B to surpass GPT-4 with MedPrompt despite smaller scale. Takrouri et al. (2025) applied LLM distillation to household energy modeling, generating culturally sensitive consumption data across six countries. Xing et al. (2026) adapted distillation for temporal knowledge graph reasoning, transferring both structural and temporal reasoning capabilities to lightweight student models.

### Theme 6: Memorization Dynamics and Privacy Implications

The relationship between distillation and memorization has important privacy implications. Borkar et al. (2026) found that distilled models memorize significantly less training data than standard fine-tuning, reducing memorization by more than 50%. However, hard distillation inherits 2.7× more teacher-specific examples than soft distillation, posing greater privacy risk. Student memorization is predictable prior to distillation using features like zlib entropy, KL divergence, and perplexity, with some examples accounting for over 95% of memorization during distillation.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively demonstrate that knowledge distillation is most effective when it goes beyond simple output matching to capture intermediate representations, training dynamics, and domain-specific knowledge structures. Multiple studies confirm that distilled models can retain 70-95% of teacher capabilities while achieving substantial efficiency gains (Paredes La Torre et al., 2026; Dhakal et al., 2026; Liu et al., 2026). There is also consensus that chain-of-thought prompting enhances reasoning distillation effectiveness (Do et al., 2025; Paredes La Torre et al., 2026).

**Disagreements**: The literature reveals tension between reasoning enhancement and factual recall preservation during distillation. While He et al. (2026) found that standard forward KL distillation during mid-training slows factual recall acquisition, other studies focus primarily on reasoning improvements without addressing this trade-off explicitly. Additionally, there is variation in how different studies approach representation space alignment—Delta-KD (Cao et al., 2025) emphasizes preserving distributional shifts, while DistillLens (Dhakal et al., 2026) focuses on symmetric intermediate state alignment, suggesting different underlying assumptions about what aspects of teacher knowledge are most critical to preserve.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly discuss computational costs or carbon footprint of distillation processes, despite efficiency being a primary motivation. Second, while domain-specific applications are emerging (biomedical, energy, temporal reasoning), there is limited work on distillation for low-resource languages beyond the Spanish evaluation in Paredes La Torre et al. (2026). Third, the memorization analysis by Borkar et al. (2026) raises important privacy questions that remain underexplored—particularly regarding whether reduced memorization in distilled models translates to meaningful privacy guarantees in deployment. Fourth, most studies report aggregate performance metrics without analyzing failure modes or edge cases where distillation degrades performance. Finally, the interaction between quantization and distillation (explored only by Paredes La Torre et al., 2026) warrants deeper investigation as both techniques are often combined for deployment.

## Per-Paper Annotations

### Borkar et al. (2026)

**Research question**: How does training data memorization behave in knowledge distillation setups compared to standard fine-tuning?
**Methodology**: The study examines memorization across the KD pipeline using three LLM families (Pythia, OLMo-2, Qwen-3) and three datasets (FineWeb, Wikitext, Nemotron-CC-v2), analyzing memorization rates and predictability using features like zlib entropy, KL divergence, and perplexity.
**Key findings**:
- Distilled models memorize significantly less training data than standard fine-tuning, reducing memorization by more than 50%
- Some examples are inherently easier to memorize and account for over 95% of memorization during distillation
- Student memorization is predictable prior to distillation using features based on zlib entropy, KL divergence, and perplexity
- Hard distillation inherits 2.7× more teacher-specific examples than soft distillation, posing greater privacy risk
**Limitations**: not stated in abstract

### Cao et al. (2025)

**Research question**: How can knowledge distillation be improved when student and teacher output distributions do not share the same optimal representation space?
**Methodology**: The authors propose Delta Knowledge Distillation (Delta-KD), which extends token-level KD by encouraging the student to approximate an optimal representation space while explicitly preserving the distributional shift (Delta) introduced during the teacher's supervised finetuning.
**Key findings**:
- Delta-KD addresses the limitation of prior work assuming shared optimal representation spaces
- The method explicitly preserves distributional shift from teacher's SFT
- Empirical results on ROUGE metrics show Delta-KD substantially improves student performance
- Delta-KD preserves more of the teacher's knowledge compared to standard token-level KD
**Limitations**: not stated in abstract

### Dhakal et al. (2026)

**Research question**: How can knowledge distillation be improved by aligning the intermediate thought processes of student and teacher models rather than only optimizing final outputs?
**Methodology**: The paper introduces DistillLens, which projects intermediate hidden states into vocabulary space via Logit Lens and enforces structural alignment using a symmetric divergence objective to symmetrically align evolving thought processes of student and teacher models.
**Key findings**:
- DistillLens symmetrically aligns the evolving thought processes of student and teacher models
- The symmetric divergence constraint imposes a dual-sided penalty, preventing both overconfidence and underconfidence
- DistillLens preserves high-entropy information conduits essential for final deduction
- The framework consistently outperforms standard KD and feature-transfer baselines on diverse instruction-following benchmarks
**Limitations**: not stated in abstract

### Do et al. (2025)

**Research question**: What is the effectiveness of Chain-of-Thought prompting in distilling reasoning capability from larger LLMs to smaller LLMs using white-box knowledge distillation?
**Methodology**: The paper conducts white-box KD experiments using LLMs from Qwen and Llama2 families, employing CoT data from the CoT-Collection dataset, then evaluates distilled models on natural language reasoning and understanding tasks from the BIG-Bench-Hard benchmark.
**Key findings**:
- Chain-of-Thought improves white-box KD effectiveness for distilling reasoning capability
- Distilled models achieve better average performance in natural language reasoning tasks from BIG-Bench-Hard
- CoT enables distilled models to perform better on natural language understanding tasks
- The approach addresses complex challenges that smaller LLMs typically face in reasoning benchmarks
**Limitations**: not stated in abstract

### He et al. (2026)

**Research question**: How does logit-based knowledge distillation behave differently across training stages, and can this stage dependence be mitigated?
**Methodology**: Through controlled experiments, the paper analyzes forward KL distillation with post-trained teachers during mid-training, traces stage dependence to asymmetry in teacher confidence across data domains, and proposes Switch Distillation that distills on tokens where the teacher is confident using teacher predictive entropy as a routing signal.
**Key findings**:
- Forward KL distillation behaves fundamentally differently during mid-training compared to pre-training
- During mid-training, forward KD slows factual recall acquisition despite continued reasoning gains
- Switch Distillation achieves 1.61-1.71x reasoning performance and 1.13-1.19x knowledge/commonsense performance while preserving 96.7-96.8% factual recall
- Benefits persist after post-training, closing the factual recall gap while maintaining 1.25-1.32x reasoning gains
**Limitations**: not stated in abstract

### Liu et al. (2026)

**Research question**: How can knowledge distillation capture fine-grained information that is lost when focusing only on knowledge distribution among layers?
**Methodology**: The authors introduce Multi-aspect Knowledge Distillation (MaKD), which mimics self-attention and feed-forward modules in greater depth to capture rich language knowledge information at different aspects, combined with low-rank factorization.
**Key findings**:
- MaKD captures fine-grained information lost in existing layer-distribution-focused methods
- The method achieves competitive performance compared with various strong baselines under the same storage parameter budget
- MaKD performs well in distilling auto-regressive architecture models
**Limitations**: not stated in abstract

### Paredes La Torre et al. (2026)

**Research question**: Can knowledge distillation combined with chain-of-thought reinforcement learning produce compact, efficient models suitable for resource-constrained deployment?
**Methodology**: Using Qwen 3B as teacher and Qwen 0.5B as student, the authors apply knowledge distillation across English Dolly-15k, Spanish Dolly-15k, and code datasets (BugNet, PyTorrent), integrating chain-of-thought prompting with Group Relative Policy Optimization and 4-bit weight quantization.
**Key findings**:
- The distilled student retains 70% to 91% of teacher capability in English tasks
- Spanish task performance reaches up to 95% retention
- Coding tasks achieve up to 93.5% Rouge-L retention
- Chain-of-thought prompting with GRPO improves reasoning coherence and solution correctness compared to KD alone
- 4-bit weight quantization reduces memory footprint and inference latency
**Limitations**: not stated in abstract

### Takrouri et al. (2025)

**Research question**: How can Large Language Models be integrated into energy modeling to generate realistic, culturally sensitive household energy usage data across diverse geographies?
**Methodology**: The study employs five different LLMs to systematically produce family structures, weather patterns, and daily consumption profiles for households in six countries using a four-stage methodology that synthesizes contextual daily data including culturally nuanced activities, weather ranges, HVAC operations, and energy signatures.
**Key findings**:
- LLMs can generate realistic, culturally sensitive, and behavior-specific data for household energy usage across diverse geographies
- The four-stage methodology synthesizes contextual daily data including culturally nuanced activities and realistic weather ranges
- External weather datasets can be directly integrated, bypassing intermediate weather modeling stages while ensuring physically consistent data inputs
- The approach demonstrates how prompt engineering combined with knowledge distillation can advance sustainable energy research and climate mitigation efforts
**Limitations**: not stated in abstract

### Xing et al. (2026)

**Research question**: How can knowledge distillation be adapted for temporal knowledge graph reasoning to enable deployment on resource-constrained platforms while maintaining reasoning accuracy?
**Methodology**: The authors propose a distillation framework using large language models as teachers to transfer both structural and temporal reasoning capabilities to lightweight student models, integrating large-scale public knowledge with task-specific temporal information.
**Key findings**:
- The framework addresses limitations of existing compression techniques that fail to capture temporal dependencies in TKGs
- LLMs as teachers enable effective transfer of structural and temporal reasoning capabilities
- The approach enhances student model ability to model temporal dynamics while maintaining compact architecture
- Extensive experiments show the method outperforms strong baselines on multiple benchmark datasets
- The framework achieves favorable trade-off between reasoning accuracy, computational efficiency, and deployability
**Limitations**: not stated in abstract

### Xiao et al. (2025)

**Research question**: How can a knowledge-driven, agentic framework address the insufficient quantity and quality of open-source annotated biomedical corpora for LLM training?
**Methodology**: The paper proposes a collaborative multi-agent architecture guided by the Medical Subject Headings (MeSH) hierarchy, where specialized agents autonomously extract, synthesize, and self-evaluate high-quality textual data from scientific literature to generate domain-specific question-answer pairs.
**Key findings**:
- Language models trained on multi-agent distilled datasets achieve notable improvements in biomedical question-answering tasks
- The distilled datasets outperform both strong life sciences LLM baselines and advanced proprietary models
- The AI-Ready dataset enables Llama3-70B to surpass GPT-4 with MedPrompt and Med-PaLM-2 despite their larger scale
- Ablation studies validate the effectiveness and synergy of each agent within the framework
**Limitations**: not stated in abstract

## References

Borkar, J., Chadha, K., Mireshghallah, N., Zhang, Y., Veliche, I.-E., Mitra, A., Smith, D. A., Xu, Z., & Garcia-Olano, D. (2026). Memorization dynamics in knowledge distillation for language models. arXiv. https://arxiv.org/abs/2601.15394

Cao, Y., Kang, Y., Xing, Z., & Jiang, R. (2025). Delta knowledge distillation for large language models. arXiv. https://arxiv.org/abs/2509.14526

Dhakal, M., Jinadu, U., Budathoki, A., Sunderraman, R., & Ding, Y. (2026). DistillLens: Symmetric knowledge distillation through logit lens. arXiv. https://arxiv.org/abs/2602.13567

Do, C.-T., Doddipatla, R., & Knill, K. (2025). Effectiveness of chain-of-thought in distilling reasoning capability from large language models. arXiv. https://arxiv.org/abs/2511.05184

He, J., Yen, H., Li, S. S., Li, M., Zeng, H., Xia, Y., Zhang, B., Zhao, Z., Zhang, Q., Koh, P. W., Zettlemoyer, L., & Yih, W.-t. (2026). Knowledge distillation during mid-training favors reasoning over factual recall. arXiv. https://arxiv.org/abs/2609.01532

Liu, Z., Mao, Y., Xu, J., Peng, X., & Huang, K. (2026). Multi-aspect knowledge distillation for language model with low-rank factorization. arXiv. https://arxiv.org/abs/2604.03110

Paredes La Torre, A., Flores, B., & Rodriguez, D. (2026). Knowledge distillation for large language models. arXiv. https://arxiv.org/abs/2603.13765

Takrouri, M., Cuadrado, N. M., & Takáč, M. (2025). Knowledge distillation from large language models for household energy modeling. arXiv. https://arxiv.org/abs/2502.03034

Xing, W., Song, W., Lin, S., Wu, C., Li, Z., & Wang, M. (2026). Knowledge distillation for temporal knowledge graph reasoning with large language models. arXiv. https://arxiv.org/abs/2601.00202

Xiao, M., Cai, X., Long, Q., Wang, C., Zhou, Y., & Zhu, H. (2025). Knowledge-driven agentic scientific corpus distillation framework for biomedical large language models training. arXiv. https://arxiv.org/abs/2504.19565
