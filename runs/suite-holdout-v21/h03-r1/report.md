# Systematic Literature Review: Knowledge Distillation of Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "knowledge distillation language models", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

Knowledge distillation (KD) for language models has evolved significantly in recent years, moving beyond simple teacher-student logit matching to sophisticated frameworks that address architectural, temporal, and domain-specific challenges. The surveyed literature reveals a field maturing along multiple dimensions: novel distillation architectures (DistillLens, Delta-KD, MaKD) that capture finer-grained information transfer; deeper theoretical understanding of memorization dynamics and training-stage effects; integration of reasoning techniques like Chain-of-Thought to preserve complex capabilities; and practical applications spanning biomedical domains, energy modeling, and temporal knowledge graphs. Collectively, these works demonstrate that KD is no longer merely a compression technique but a nuanced transfer mechanism capable of preserving—and in some cases enhancing—specific capabilities while dramatically reducing model size and computational requirements.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "knowledge distillation language models", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Innovations in Knowledge Distillation

Recent work has moved beyond traditional token-level KD to capture richer, multi-aspect information transfer. DistillLens introduces symmetric knowledge distillation through the Logit Lens, projecting intermediate hidden states into vocabulary space and enforcing structural alignment between student and teacher thought processes rather than treating intermediate layers as black boxes (Dhakal et al., 2026). Delta Knowledge Distillation addresses the fundamental limitation that student and teacher output distributions may not share the same optimal representation space by explicitly preserving the distributional shift introduced during the teacher's supervised finetuning (Cao et al., 2025). Multi-aspect Knowledge Distillation (MaKD) captures fine-grained information by mimicking self-attention and feed-forward modules in greater depth, addressing the loss of rich language knowledge when focusing only on knowledge distribution among layers (Liu et al., 2026). These architectural innovations collectively demonstrate that effective KD requires capturing information at multiple levels of abstraction simultaneously.

### Theme 2: Training Dynamics and Memorization

Understanding when and how knowledge is transferred during training has emerged as a critical research direction. He et al. (2026) discovered that forward KL distillation behaves differently during mid-training compared to pre-training, slowing factual recall acquisition despite continued reasoning gains due to teacher confidence asymmetry across data domains. Their Switch Distillation approach uses teacher predictive entropy as a routing signal to achieve 1.61-1.71x reasoning performance while preserving 96.7-96.8% of factual recall. Borkar et al. (2026) examined memorization dynamics across three LLM families and found that distilled models memorize significantly less training data than standard fine-tuning, reducing memorization by more than 50%. These findings reveal that KD is not uniformly beneficial across all training stages and data types, requiring careful orchestration to balance reasoning and factual knowledge acquisition.

### Theme 3: Reasoning and Chain-of-Thought Integration

The integration of Chain-of-Thought (CoT) prompting with KD has emerged as a powerful approach for distilling reasoning capabilities. Do et al. (2025) demonstrated through white-box KD experiments that CoT improves effectiveness for reasoning tasks, with distilled models achieving better average performance on natural language reasoning and understanding tasks from the BIG-Bench-Hard benchmark. Paredes La Torre et al. (2026) combined CoT with Group Relative Policy Optimization for coding tasks, improving reasoning coherence and solution correctness compared to KD alone. Their distilled 0.5B student retained 70-91% of the teacher's capability in English tasks and up to 95% in Spanish tasks. These results suggest that CoT provides a structured intermediate representation that facilitates more effective reasoning transfer than direct logit matching.

### Theme 4: Domain-Specific Applications

KD frameworks are increasingly tailored to specific domains with unique requirements. Xiao et al. (2025) proposed a knowledge-driven agentic framework for biomedical LLM training, using a collaborative multi-agent architecture guided by the Medical Subject Headings hierarchy to generate domain-specific question-answer pairs, enabling Llama3-70B to surpass GPT-4 with MedPrompt despite smaller scale. Takrouri et al. (2025) employed KD from LLMs for household energy modeling, generating culturally sensitive, behavior-specific data across six countries to capture how cultural, climatic, and behavioral factors converge to shape carbon emissions. Xing et al. (2026) developed a distillation framework for temporal knowledge graph reasoning that leverages LLMs as teachers to transfer both structural and temporal reasoning capabilities to lightweight student models. These applications demonstrate KD's versatility beyond general language tasks.

### Theme 5: Efficiency and Deployment Optimization

A consistent thread across the literature is the drive toward practical deployability in resource-constrained settings. Paredes La Torre et al. (2026) integrated post-training 4-bit weight quantization to further reduce memory footprint and inference latency. Xing et al. (2026) emphasized achieving favorable trade-offs between reasoning accuracy, computational efficiency, and practical deployability for temporal knowledge graph models. The biomedical framework by Xiao et al. (2025) minimizes manual involvement while ensuring comprehensive coverage with biomedical ontologies. These works collectively address the gap between research prototypes and production deployment, recognizing that KD's ultimate value lies in enabling real-world applications.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that traditional token-level KD is insufficient for capturing complex capabilities like reasoning and domain-specific knowledge. Multiple works demonstrate that architectural innovations (symmetric alignment, multi-aspect mimicry, distributional shift preservation) consistently outperform standard KD baselines. There is broad consensus that KD reduces memorization risk compared to standard fine-tuning while maintaining or improving task performance. The integration of structured intermediate representations (CoT, Logit Lens projections) emerges as a reliable pattern across successful approaches.

**Disagreements**: The literature reveals tension between reasoning and factual recall during distillation. He et al. (2026) found that forward KL distillation favors reasoning over factual recall during mid-training, suggesting these capabilities compete for model capacity. This contrasts with the implicit assumption in earlier KD work that knowledge transfer is uniformly beneficial. Additionally, while most papers treat KD as a post-training compression technique, He et al. (2026) demonstrate that mid-training distillation exhibits fundamentally different dynamics, challenging the standard pre-training versus fine-tuning dichotomy.

## Gaps and Open Questions

Several limitations recur across the surveyed literature. First, none of the papers explicitly state limitations in their abstracts, suggesting either space constraints or insufficient critical reflection on methodological boundaries. Second, while multiple papers demonstrate improved performance on specific benchmarks, there is limited discussion of failure modes or conditions under which KD approaches degrade. Third, the literature lacks systematic comparison across different KD methods on common benchmarks, making it difficult to determine which architectural innovations provide complementary versus redundant benefits. Fourth, most work focuses on English-language models, with only Paredes La Torre et al. (2026) explicitly addressing multilingual transfer. Finally, the theoretical foundations of why certain KD approaches work remain underexplored—most papers present empirical results without rigorous analysis of the underlying information-theoretic or optimization principles.

## Per-Paper Annotations

### Borkar et al. (2026)

**Research question**: How does training data memorization behave in knowledge distillation setups compared to standard fine-tuning?
**Methodology**: The study examines memorization across the KD pipeline using three LLM families (Pythia, OLMo-2, Qwen-3) and three datasets (FineWeb, Wikitext, Nemotron-CC-v2), analyzing memorization rates and risk factors.
**Key findings**:
- Distilled models memorize significantly less training data than standard fine-tuning, reducing memorization by more than 50%
- Some examples are inherently easier to memorize and account for over 95% of memorization during distillation
- Student memorization is predictable prior to distillation using features based on zlib entropy, KL divergence, and perplexity
- Hard distillation inherits 2.7× more teacher-specific examples than soft distillation, posing greater risk despite similar overall memorization rates
**Limitations**: Not stated in abstract

### Cao et al. (2025)

**Research question**: How can knowledge distillation be improved when student and teacher output distributions do not share the same optimal representation space?
**Methodology**: The authors propose Delta Knowledge Distillation (Delta-KD), a novel extension of token-level KD that encourages the student to approximate an optimal representation space by explicitly preserving the distributional shift Delta introduced during the teacher's supervised finetuning.
**Key findings**:
- Delta-KD addresses the limitation that student and teacher output distributions may not share the same optimal representation space
- The method explicitly preserves the distributional shift Delta introduced during the teacher's supervised finetuning
- Empirical results on ROUGE metrics demonstrate that Delta-KD substantially improves student performance while preserving more of the teacher's knowledge
**Limitations**: Not stated in abstract

### Dhakal et al. (2026)

**Research question**: How can knowledge distillation be improved by symmetrically aligning the evolving thought processes of student and teacher models rather than treating intermediate layers as a black box?
**Methodology**: The paper introduces DistillLens, a framework that projects intermediate hidden states into vocabulary space via the Logit Lens and enforces structural alignment using a symmetric divergence objective to align student and teacher thought processes.
**Key findings**:
- DistillLens consistently outperforms standard KD and feature-transfer baselines on diverse instruction-following benchmarks
- The symmetric divergence constraint imposes a dual-sided penalty preventing both overconfidence and underconfidence
- The approach preserves high-entropy information conduits essential for final deduction
- Experiments were conducted on GPT-2 and Llama architectures
**Limitations**: Not stated in abstract

### Do et al. (2025)

**Research question**: What is the role and effectiveness of Chain-of-Thought prompting in distilling reasoning capability from larger LLMs to smaller LLMs using white-box knowledge distillation?
**Methodology**: The paper conducts white-box KD experiments using LLMs from the Qwen and Llama2 families, employing CoT data from the CoT-Collection dataset, and evaluates distilled models on natural language reasoning and understanding tasks from the BIG-Bench-Hard benchmark.
**Key findings**:
- Chain-of-Thought improves white-box KD effectiveness for reasoning tasks
- Distilled models achieve better average performance in natural language reasoning and understanding tasks from BBH
- CoT helps smaller LLMs handle complex challenges presented by the BBH benchmark
**Limitations**: Not stated in abstract

### He et al. (2026)

**Research question**: How does the effectiveness of logit-based knowledge distillation vary across different training stages, and why does forward KL distillation behave differently during mid-training compared to pre-training?
**Methodology**: Through controlled experiments, the paper analyzes forward KL distillation during mid-training, traces stage dependence to asymmetry in teacher confidence across data domains, and proposes Switch Distillation that distills on tokens where the teacher is confident using teacher predictive entropy as a routing signal.
**Key findings**:
- Forward KL distillation slows factual recall acquisition during mid-training despite continued reasoning gains
- Teachers are more confident on procedural than knowledge-intensive data, while students acquire low-entropy factual knowledge earlier in training
- Switch Distillation achieves 1.61-1.71x reasoning performance and 1.13-1.19x knowledge and commonsense performance relative to standard NTP
- Switch Distillation preserves 96.7-96.8% of factual recall
- Benefits persist after post-training, closing the factual recall gap while maintaining reasoning and knowledge gains
**Limitations**: Not stated in abstract

### Liu et al. (2026)

**Research question**: How can knowledge distillation capture fine-grained information that is lost when focusing only on knowledge distribution among layers?
**Methodology**: The authors introduce Multi-aspect Knowledge Distillation (MaKD), which mimics the self-attention and feed-forward modules in greater depth to capture rich language knowledge information at different aspects.
**Key findings**:
- MaKD addresses the limitation of existing methods that only focus on knowledge distribution among layers
- The method captures rich language knowledge information at different aspects through deeper module mimicry
- MaKD achieves competitive performance compared with various strong baselines with the same storage parameter budget
- The method performs well in distilling auto-regressive architecture models
**Limitations**: Not stated in abstract

### Paredes La Torre et al. (2026)

**Research question**: Can knowledge distillation combined with chain-of-thought guided reinforcement learning produce compact, efficient models suitable for resource-constrained settings?
**Methodology**: The authors propose a resource-efficient framework using Qwen 3B as teacher and Qwen 0.5B as student, applying knowledge distillation across English Dolly-15k, Spanish Dolly-15k, and code datasets, with chain-of-thought prompting and Group Relative Policy Optimization for coding tasks.
**Key findings**:
- The distilled student retains 70% to 91% of the teacher's capability in English tasks
- Performance reaches up to 95% in Spanish tasks and up to 93.5% Rouge-L in code tasks
- Integrating chain-of-thought prompting with Group Relative Policy Optimization improves reasoning coherence and solution correctness compared to knowledge distillation alone
- Post-training 4-bit weight quantization further reduces memory footprint and inference latency
**Limitations**: Not stated in abstract

### Takrouri et al. (2025)

**Research question**: How can Large Language Models be integrated into energy modeling to generate realistic, culturally sensitive, and behavior-specific data for household energy usage across diverse geographies?
**Methodology**: The study employs five different LLMs to systematically produce family structures, weather patterns, and daily consumption profiles for households in six countries using a four-stage methodology that synthesizes contextual daily data including culturally nuanced activities, weather ranges, HVAC operations, and energy signatures.
**Key findings**:
- The approach generates realistic, culturally sensitive, and behavior-specific data for household energy usage
- The methodology captures how cultural, climatic, and behavioral factors converge to shape carbon emissions
- An alternative strategy allows direct integration of external weather datasets while ensuring physically consistent data inputs
- The approach offers a cost-effective avenue for scenario-based energy optimization
- Prompt engineering combined with knowledge distillation can advance sustainable energy research and climate mitigation efforts
**Limitations**: Not stated in abstract

### Xing et al. (2026)

**Research question**: How can temporal knowledge graph reasoning models be compressed for deployment on resource-constrained platforms while maintaining reasoning performance?
**Methodology**: The authors propose a distillation framework tailored for temporal knowledge graph reasoning that leverages large language models as teacher models to guide the transfer of both structural and temporal reasoning capabilities to lightweight student models.
**Key findings**:
- Existing TKG reasoning models rely on large parameter sizes and intensive computation, hindering deployment on resource-constrained platforms
- Most existing compression techniques are designed for static knowledge graphs and fail to capture temporal dependencies
- The proposed framework integrates large-scale public knowledge with task-specific temporal information
- The method consistently outperforms strong baselines on multiple publicly available benchmark datasets
- The approach achieves a favorable trade-off between reasoning accuracy, computational efficiency, and practical deployability
**Limitations**: Not stated in abstract

### Xiao et al. (2025)

**Research question**: How can a knowledge-driven, agentic framework address the challenge of insufficient quantity and quality in open-source annotated scientific corpora for biomedical LLM training?
**Methodology**: The paper proposes a collaborative multi-agent architecture guided by the Medical Subject Headings (MeSH) hierarchy, where specialized agents autonomously extract, synthesize, and self-evaluate high-quality textual data from scientific literature to generate domain-specific question-answer pairs.
**Key findings**:
- Language models trained on the multi-agent distilled datasets achieved notable improvements in biomedical question-answering tasks
- The distilled dataset enabled Llama3-70B to surpass GPT-4 with MedPrompt and Med-PaLM-2 despite their larger scale
- Ablation studies validated the effectiveness and synergy of each agent within the framework
- The approach minimizes manual involvement while ensuring comprehensive coverage and consistency with biomedical ontologies
**Limitations**: Not stated in abstract

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
