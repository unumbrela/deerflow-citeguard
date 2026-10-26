# Systematic Literature Review: Knowledge Distillation of Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "knowledge distillation language models", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on knowledge distillation (KD) for language models, revealing a rapidly evolving field focused on improving efficiency, reasoning capabilities, and domain-specific applications. The surveyed literature demonstrates that KD has matured beyond simple output matching to encompass sophisticated techniques including intermediate representation alignment, chain-of-thought reasoning transfer, and distributional shift preservation. Key advances include methods that reduce memorization and privacy risks (Borkar et al., 2026), enhance reasoning over factual recall (He et al., 2026), and enable deployment in resource-constrained settings (Paredes La Torre et al., 2026). The field shows strong convergence around the importance of capturing teacher model reasoning processes rather than just final outputs, while open questions remain about optimal distillation strategies across different training stages and domains.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "knowledge distillation language models", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Reasoning-Capability Distillation

A prominent research direction focuses on distilling reasoning capabilities from large teacher models to compact students, particularly through chain-of-thought (CoT) prompting. Do et al. (2025) demonstrated that CoT significantly improves white-box KD effectiveness for transferring reasoning skills, with distilled models achieving better performance on natural language reasoning tasks from BIG-Bench-Hard. This approach addresses a critical challenge for smaller models in handling complex reasoning tasks. Paredes La Torre et al. (2026) extended this work by combining CoT with Group Relative Policy Optimization (GRPO) for coding tasks, achieving up to 93.5% Rouge-L performance retention. He et al. (2026) revealed a nuanced finding: mid-training distillation favors reasoning over factual recall, with teachers showing higher confidence on procedural than knowledge-intensive data. Their Switch Distillation method achieved 1.61-1.71x reasoning performance improvements by routing based on teacher predictive entropy.

### Theme 2: Intermediate Representation Alignment

Moving beyond output-level distillation, recent work emphasizes aligning intermediate representations and thought processes between teacher and student models. Dhakal et al. (2026) introduced DistillLens, which projects intermediate hidden states into vocabulary space via the Logit Lens and enforces structural alignment using symmetric divergence objectives. This method symmetrically aligns evolving thought processes, preventing both overconfidence and underconfidence while preserving high-entropy information conduits essential for final deduction. Liu et al. (2026) proposed Multi-aspect Knowledge Distillation (MaKD), which mimics self-attention and feed-forward modules at greater depth to capture rich language knowledge at different aspects, combined with low-rank factorization for compression. These approaches recognize that layer-level alignment alone loses fine-grained information critical for student performance.

### Theme 3: Distributional Shift and Representation Space Preservation

Several papers address the fundamental limitation that student and teacher output distributions may not share the same optimal representation space. Cao et al. (2025) proposed Delta Knowledge Distillation (Delta-KD), which explicitly preserves the distributional shift (Delta) introduced during the teacher's supervised finetuning. This method substantially improves student performance on ROUGE metrics by encouraging the student to approximate an optimal representation space rather than simply matching teacher outputs. This represents a conceptual advance in understanding KD as representation-space transfer rather than mere output matching.

### Theme 4: Memorization and Privacy Dynamics

A critical line of inquiry examines memorization behavior and privacy implications in KD setups. Borkar et al. (2026) found that distilled models memorize significantly less training data than standard fine-tuning, reducing memorization by more than 50%. Their analysis revealed that some examples are inherently easier to memorize, accounting for over 95% of memorization during distillation, and that student memorization is predictable prior to distillation using features like zlib entropy, KL divergence, and perplexity. Importantly, hard distillation inherits 2.7× more teacher-specific examples than soft distillation, posing greater privacy risk. This work provides actionable insights for privacy-conscious KD deployment.

### Theme 5: Domain-Specific Applications

KD research increasingly targets specialized domains requiring tailored approaches. Xiao et al. (2025) developed a knowledge-driven agentic framework for biomedical LLM training, using a collaborative multi-agent architecture guided by the Medical Subject Headings (MeSH) hierarchy to extract and synthesize high-quality textual data from scientific literature. Their approach enabled Llama3-70B to surpass GPT-4 with MedPrompt and Med-PaLM-2 despite larger scale. Takrouri et al. (2025) applied KD to household energy modeling, using LLMs to generate realistic, culturally sensitive, and behavior-specific data across six countries. Xing et al. (2026) adapted KD for temporal knowledge graph reasoning, integrating large-scale public knowledge with task-specific temporal information to transfer both structural and temporal reasoning capabilities to compact student models.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, most papers converge on the finding that intermediate representation alignment outperforms simple output matching (Dhakal et al., 2026; Liu et al., 2026; Cao et al., 2025). Second, there is consensus that chain-of-thought prompting enhances reasoning transfer in KD settings (Do et al., 2025; Paredes La Torre et al., 2026; He et al., 2026). Third, multiple studies confirm that KD can achieve substantial compression while retaining 70-95% of teacher capability across diverse tasks (Paredes La Torre et al., 2026; Xiao et al., 2025). Fourth, the literature agrees that domain-specific knowledge integration is critical for specialized applications (Xiao et al., 2025; Takrouri et al., 2025; Xing et al., 2026).

**Disagreements**: A notable tension exists regarding the effectiveness of distillation across training stages. He et al. (2026) found that forward KL distillation behaves fundamentally differently during mid-training compared to pre-training, slowing factual recall acquisition despite reasoning gains. This contrasts with implicit assumptions in other work that distillation benefits are stage-invariant. Additionally, while most papers focus on logit-based or representation-based distillation, the optimal choice between hard and soft distillation remains contested—Borkar et al. (2026) show hard distillation poses greater privacy risks, yet other work does not address this trade-off.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either space constraints or insufficient critical self-reflection on methodological boundaries. Second, while domain-specific applications are emerging (biomedical, energy, temporal knowledge graphs), there is limited work on cross-domain transfer—whether KD techniques developed for one domain generalize to others. Third, the temporal dynamics of distillation remain underexplored; He et al. (2026) provide initial insights on mid-training versus pre-training, but systematic understanding of stage-dependent effects is nascent. Fourth, privacy implications identified by Borkar et al. (2026) are not addressed by other papers, despite KD's increasing deployment in sensitive applications. Fifth, the surveyed work focuses predominantly on English-language tasks, with limited attention to multilingual distillation challenges beyond Paredes La Torre et al. (2026)'s Spanish evaluation. Finally, computational efficiency metrics are inconsistently reported—while several papers mention reduced memory footprint or latency, standardized benchmarks for KD efficiency are absent.

## Per-Paper Annotations

### Cao et al. (2025)

**Research question**: How can knowledge distillation be improved by accounting for distributional shifts between teacher and student output representations?
**Methodology**: The authors propose Delta Knowledge Distillation (Delta-KD), a novel extension of token-level KD that encourages the student to approximate an optimal representation space by explicitly preserving the distributional shift (Delta) introduced during the teacher's supervised finetuning.
**Key findings**:
- Delta-KD addresses the limitation that student and teacher output distributions may not share the same optimal representation space
- The method substantially improves student performance on ROUGE metrics
- Delta-KD preserves more of the teacher's knowledge compared to standard token-level KD
**Limitations**: not stated in abstract

### Dhakal et al. (2026)

**Research question**: How can knowledge distillation be improved by aligning the intermediate thought processes of student and teacher models rather than just optimizing final outputs?
**Methodology**: The paper introduces DistillLens, which projects intermediate hidden states into vocabulary space via the Logit Lens and enforces structural alignment using a symmetric divergence objective to symmetrically align the evolving thought processes of student and teacher models.
**Key findings**:
- DistillLens symmetrically aligns the evolving thought processes of student and teacher models
- The symmetric divergence constraint imposes a dual-sided penalty, preventing both overconfidence and underconfidence
- The method preserves high-entropy information conduits essential for final deduction
- DistillLens consistently outperforms standard KD and feature-transfer baselines on diverse instruction-following benchmarks
- The framework is demonstrated on GPT-2 and Llama architectures
**Limitations**: not stated in abstract

### Do et al. (2025)

**Research question**: What is the role and effectiveness of Chain-of-Thought prompting in distilling reasoning capability from larger LLMs to smaller LLMs using white-box knowledge distillation?
**Methodology**: The paper conducts white-box KD experiments using LLMs from the Qwen and Llama2 families, employing CoT data from the CoT-Collection dataset, and evaluates the distilled models on natural language reasoning and understanding tasks from the BIG-Bench-Hard benchmark.
**Key findings**:
- Chain-of-Thought improves white-box KD effectiveness for distilling reasoning capability
- Distilled models achieve better average performance in natural language reasoning and understanding tasks from BBH
- CoT is leveraged to transfer reasoning capability from larger LLMs to smaller LLMs
- The approach addresses complex challenges for smaller LLMs in reasoning tasks
- Experimental results demonstrate the role of CoT in improving distilled model performance
**Limitations**: not stated in abstract

### He et al. (2026)

**Research question**: How does the effectiveness of logit-based knowledge distillation vary across different training stages, particularly during mid-training versus pre-training?
**Methodology**: Through controlled experiments, the paper investigates forward KL distillation with post-trained teachers during mid-training, traces stage dependence to asymmetry in teacher confidence across data domains, and proposes Switch Distillation that distills on tokens where the teacher is confident using teacher predictive entropy as a routing signal.
**Key findings**:
- Forward KL distillation behaves fundamentally differently during mid-training compared to pre-training
- During mid-training, forward KD slows factual recall acquisition despite continued reasoning gains
- Teachers are more confident on procedural than knowledge-intensive data, while students acquire low-entropy factual knowledge earlier in training
- Switch Distillation achieves 1.61-1.71x reasoning performance and 1.13-1.19x knowledge and commonsense performance relative to standard NTP
- Benefits persist after post-training, closing the factual recall gap while maintaining gains in reasoning and knowledge
**Limitations**: not stated in abstract

### Liu et al. (2026)

**Research question**: How can knowledge distillation capture fine-grained information beyond layer-level knowledge distribution alignment?
**Methodology**: The authors introduce Multi-aspect Knowledge Distillation (MaKD), which mimics self-attention and feed-forward modules in greater depth to capture rich language knowledge information at different aspects, combined with low-rank factorization for compression.
**Key findings**:
- MaKD achieves competitive performance compared with various strong baselines with the same storage parameter budget
- The method captures fine-grained information that existing layer-focused methods may lose
- MaKD performs well in distilling auto-regressive architecture models
**Limitations**: not stated in abstract

### Paredes La Torre et al. (2026)

**Research question**: Can knowledge distillation combined with chain-of-thought reinforcement learning produce compact, efficient language models suitable for resource-constrained settings?
**Methodology**: The authors propose a resource-efficient framework using Qwen 3B as teacher and Qwen 0.5B as student, applying knowledge distillation across English Dolly-15k, Spanish Dolly-15k, and code datasets (BugNet, PyTorrent), with chain-of-thought prompting and Group Relative Policy Optimization for coding tasks, followed by 4-bit weight quantization.
**Key findings**:
- The distilled student retains 70% to 91% of teacher capability in English tasks
- Spanish tasks show retention up to 95% of teacher capability
- Coding tasks achieve up to 93.5% Rouge-L performance
- Chain-of-thought prompting with GRPO improves reasoning coherence and solution correctness compared to KD alone
- 4-bit weight quantization reduces memory footprint and inference latency
**Limitations**: not stated in abstract

### Takrouri et al. (2025)

**Research question**: How can Large Language Models be integrated into energy modeling to generate realistic, culturally sensitive, and behavior-specific data for household energy usage?
**Methodology**: The study employs and compares five different LLMs to systematically produce family structures, weather patterns, and daily consumption profiles for households in six distinct countries using a four-stage methodology that synthesizes contextual daily data including culturally nuanced activities, realistic weather ranges, HVAC operations, and distinct energy signatures.
**Key findings**:
- LLMs can generate realistic, culturally sensitive, and behavior-specific data for household energy usage across diverse geographies
- The four-stage methodology synthesizes contextual daily data including culturally nuanced activities and realistic weather ranges
- An alternative strategy allows direct integration of external weather datasets, bypassing intermediate weather modeling stages
- The resulting dataset provides insights into how cultural, climatic, and behavioral factors converge to shape carbon emissions
- The approach offers a cost-effective avenue for scenario-based energy optimization
**Limitations**: not stated in abstract

### Xiao et al. (2025)

**Research question**: How can a knowledge-driven, agentic framework improve scientific corpus distillation for training biomedical large language models?
**Methodology**: The paper proposes a collaborative multi-agent architecture guided by the Medical Subject Headings (MeSH) hierarchy, where specialized agents autonomously extract, synthesize, and self-evaluate high-quality textual data from scientific literature to generate domain-specific question-answer pairs.
**Key findings**:
- Language models trained on the multi-agent distilled datasets achieve notable improvements in biomedical question-answering tasks
- The approach outperforms both strong life sciences LLM baselines and advanced proprietary models
- The AI-Ready dataset enables Llama3-70B to surpass GPT-4 with MedPrompt and Med-PaLM-2 despite their larger scale
- Ablation studies validate the effectiveness and synergy of each agent within the framework
- The framework minimizes manual involvement while ensuring comprehensive coverage and consistency with biomedical ontologies
**Limitations**: not stated in abstract

### Xing et al. (2026)

**Research question**: How can knowledge distillation be adapted for temporal knowledge graph reasoning to enable deployment on resource-constrained platforms while maintaining reasoning accuracy?
**Methodology**: The authors propose a distillation framework using large language models as teachers to guide lightweight student models, integrating large-scale public knowledge with task-specific temporal information to transfer both structural and temporal reasoning capabilities.
**Key findings**:
- The framework enables effective transfer of structural and temporal reasoning capabilities to compact student models
- The method consistently outperforms strong baselines on multiple publicly available benchmark datasets
- The approach achieves a favorable trade-off between reasoning accuracy, computational efficiency, and practical deployability
- Existing model compression techniques fail to adequately capture temporal dependencies in TKGs
**Limitations**: not stated in abstract

### Borkar et al. (2026)

**Research question**: How does training data memorization behave in knowledge distillation setups compared to standard fine-tuning?
**Methodology**: The study examines memorization across the KD pipeline using three LLM families (Pythia, OLMo-2, Qwen-3) and three datasets (FineWeb, Wikitext, Nemotron-CC-v2), analyzing memorization rates and predictability using features like zlib entropy, KL divergence, and perplexity.
**Key findings**:
- Distilled models memorize significantly less training data than standard fine-tuning, reducing memorization by more than 50%
- Some examples are inherently easier to memorize and account for over 95% of memorization during distillation
- Student memorization is predictable prior to distillation using features based on zlib entropy, KL divergence, and perplexity
- Hard distillation inherits 2.7× more teacher-specific examples than soft distillation, posing greater privacy risk
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

Xiao, M., Cai, X., Long, Q., Wang, C., Zhou, Y., & Zhu, H. (2025). Knowledge-driven agentic scientific corpus distillation framework for biomedical large language models training. arXiv. https://arxiv.org/abs/2504.19565

Xing, W., Song, W., Lin, S., Wu, C., Li, Z., & Wang, M. (2026). Knowledge distillation for temporal knowledge graph reasoning with large language models. arXiv. https://arxiv.org/abs/2601.00202
