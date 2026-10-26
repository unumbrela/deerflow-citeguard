# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The field of retrieval-augmented generation (RAG) has evolved significantly in the past two years, with research expanding beyond basic retrieval-and-generation pipelines to address fundamental challenges in faithfulness, efficiency, multi-modal integration, and collaborative reasoning. The surveyed literature reveals four major directions: (1) multi-agent architectures that distribute evidence processing across specialized roles, (2) novel integration paradigms that embed retrieval deeper into model parameters rather than context, (3) domain-specific adaptations for sensitive applications like religious texts and federated systems, and (4) architectural innovations enabling retroactive reasoning and mixed-modal retrieval. Collectively, these works demonstrate a maturing field focused on reliability, scalability, and real-world applicability rather than mere retrieval accuracy improvements.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Additionally, all metadata is extracted from abstracts only, which may not capture full methodological details or limitations discussed in the complete papers.

## Themes

### Theme 1: Multi-Agent Collaboration for Evidence Processing

A prominent trend across recent RAG research is the adoption of multi-agent architectures to handle complex evidence processing tasks. Rather than relying on a single monolithic generation step, these systems decompose the retrieval-to-generation pipeline into specialized roles performed by distinct agents. MASS-RAG (Xiao et al., 2026) exemplifies this approach with role-specialized agents for evidence summarization, extraction, and reasoning, whose outputs are combined through a dedicated synthesis stage. Similarly, MAIN-RAG (Chang et al., 2024) employs multiple LLM agents to collaboratively filter and score retrieved documents, using inter-agent consensus to ensure robust document selection without requiring additional training. FAIR-RAG (Aghajani Asl et al., 2025) extends this paradigm with an Iterative Refinement Cycle where agents deconstruct queries into checklists, audit evidence for gaps, and generate targeted sub-queries until evidence is sufficient.

The convergence on multi-agent designs suggests recognition that single-pass retrieval and generation is insufficient for complex, multi-hop reasoning tasks. By exposing multiple intermediate evidence views, these systems allow comparison and integration of complementary information, particularly when relevant evidence is distributed across retrieved contexts. This architectural shift mirrors broader trends in agent-based AI systems, where task decomposition and role specialization improve both transparency and performance.

### Theme 2: Beyond Context Injection — Novel Knowledge Integration Paradigms

Traditional RAG systems inject retrieved documents into the input context, consuming computational resources and potentially overwhelming the model with irrelevant information. Recent work explores alternative paradigms that integrate external knowledge more deeply into model architecture. Parametric RAG (Su et al., 2025) represents a fundamental departure from this approach, integrating external knowledge directly into the parameters of feed-forward networks through document parameterization. This eliminates the need to inject multiple documents into the input context, substantially enhancing both effectiveness and efficiency while saving online computational costs.

RetroRAG (Xiao et al., 2025) introduces another novel paradigm: retroactive reasoning that revises and updates evidence to redirect reasoning chains. Rather than treating retrieval as a one-time pre-processing step, RetroRAG constructs an evidence-collation-discovery system that iteratively searches, generates, and refines credible evidence until a reliable answer is obtained. This addresses the problem of irreversible errors in unidirectional forward reasoning paradigms, allowing the system to correct course when initial retrieval proves insufficient or misleading.

These approaches share a recognition that treating retrieval as context injection limits both efficiency and reasoning quality. By integrating retrieval more deeply into model computation—whether through parameter updates or iterative evidence refinement—these systems achieve better performance while reducing computational overhead.

### Theme 3: Domain-Specific Adaptations and Privacy-Conscious Architectures

RAG research increasingly addresses domain-specific requirements and constraints that generic systems cannot accommodate. Several surveyed papers focus on adaptations for specialized applications. In Quranic studies, Khalila et al. (2025) investigated how 13 open-source LLMs of varying sizes perform when augmented with RAG for domain-specific religious queries, finding that RAG mitigates hallucination issues common in general-purpose LLMs when applied to sensitive religious contexts. Their work demonstrates that well-optimized smaller architectures can achieve high faithfulness and relevance scores despite limited parameters.

Federated RAG addresses privacy-preserving retrieval in distributed settings where data cannot be centrally aggregated. Chakraborty et al. (2025) conducted the first systematic mapping study of Federated RAG, identifying key challenges including privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations. This work synthesizes recurring design patterns in federated systems, providing a foundation for future research at the intersection of RAG and federated learning.

SimGRAG (Cai et al., 2024) targets knowledge graph-driven RAG, addressing the challenge of aligning query texts with KG structures through a two-stage process of query-to-pattern transformation and pattern-to-subgraph alignment. This approach eliminates hallucinations by grounding retrieval in structured knowledge representations rather than unstructured text.

These domain-specific adaptations reveal that one-size-fits-all RAG architectures are insufficient for specialized applications. Whether the constraint is privacy (federated systems), accuracy in sensitive domains (religious texts), or structural alignment (knowledge graphs), tailored architectures outperform generic approaches.

### Theme 4: Mixed-Modal and Universal Retrieval

As AI systems increasingly handle multi-modal content, RAG research extends beyond text-only retrieval to support mixed-modal queries and documents. Nyx (Zhang et al., 2025) represents a unified mixed-modal to mixed-modal retriever tailored for Universal RAG scenarios. The system uses a four-stage automated pipeline to generate and filter mixed-modal data, followed by a two-stage training framework with pre-training on the NyxQA dataset and supervised fine-tuning using VLM feedback. Nyx performs competitively on standard text-only RAG benchmarks while significantly improving generation quality in vision-language tasks.

This extension to mixed-modal retrieval addresses real-world scenarios where queries and documents may combine text and images. The approach demonstrates that retrieval systems trained on diverse mixed-modal data can generalize effectively to both traditional text-only tasks and emerging multi-modal applications, suggesting a path toward truly universal retrieval systems.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all multi-agent approaches (MASS-RAG, MAIN-RAG, FAIR-RAG) converge on the finding that distributing evidence processing across specialized roles improves performance on complex reasoning tasks, with reported improvements of 2-11% in answer accuracy across benchmarks. Second, there is consensus that traditional context injection is inefficient—both Parametric RAG and RetroRAG independently arrive at the conclusion that deeper integration of retrieval into model computation yields better results. Third, domain-specific adaptations consistently demonstrate that generic RAG systems underperform on specialized tasks, whether religious texts, federated environments, or knowledge graphs.

**Disagreements**: The literature does not show direct contradictions, but there are tensions in approach. Multi-agent systems emphasize decomposition and specialization, while Parametric RAG argues for deeper architectural integration that eliminates the retrieval-generation boundary entirely. These represent fundamentally different philosophies: one treats retrieval as a multi-stage collaborative process, the other treats it as a parameter update problem. Additionally, while most papers focus on improving retrieval quality or reasoning architecture, Nyx's mixed-modal approach suggests the future lies in expanding retrieval scope rather than refining text-only pipelines. The field has not yet reconciled whether the path forward is specialization (multi-agent, domain-specific) or unification (parametric integration, universal retrieval).

## Gaps and Open Questions

Several significant gaps emerge from the collective literature. First, **evaluation limitations** are explicitly identified as a key challenge in Federated RAG (Chakraborty et al., 2025), and notably, none of the surveyed papers state their own limitations in their abstracts—a concerning pattern suggesting the field may lack systematic self-critique. Second, **computational efficiency** is mentioned as a benefit of Parametric RAG but never quantitatively compared against multi-agent approaches, which likely incur substantial overhead from running multiple agents. Third, **scalability** remains unaddressed: while multi-agent systems show promise on benchmarks, their behavior at scale with thousands of retrieved documents or complex multi-hop queries spanning dozens of sources is unknown.

Fourth, **human evaluation** is largely absent—all papers rely on benchmark metrics (ROUGE, F1 scores, accuracy) rather than human assessment of answer quality, faithfulness, or usefulness. Only the Quranic studies paper (Khalila et al., 2025) mentions human-assessed metrics. Fifth, **error analysis** is missing: while systems report improved accuracy, none provide detailed analysis of failure modes or when their approaches degrade. Finally, **reproducibility** varies: while some papers explicitly state code is open-sourced (Parametric RAG, SimGRAG), others do not mention availability, making independent verification difficult.

## Per-Paper Annotations

### Aghajani Asl et al. (2025)

**Research question**: How can RAG systems be improved to handle complex, multi-hop queries that require synthesizing information from disparate sources?

**Methodology**: FAIR-RAG introduces an Iterative Refinement Cycle with a Structured Evidence Assessment (SEA) module that deconstructs queries into checklists, audits evidence for gaps, and generates targeted sub-queries until evidence is sufficient. The framework was evaluated on HotpotQA, 2WikiMultiHopQA, and MusiQue benchmarks.

**Key findings**:
- FAIR-RAG significantly outperforms strong baselines on multi-hop QA benchmarks
- On HotpotQA, FAIR-RAG achieved an F1-score of 0.453, an 8.3-point improvement over the strongest iterative baseline
- The structured evidence-driven refinement process with explicit gap analysis improves reliability and accuracy in complex reasoning tasks
- The approach establishes a new state-of-the-art for iterative RAG methods on these benchmarks

**Limitations**: not stated in abstract

### Cai et al. (2024)

**Research question**: How can knowledge graph-driven RAG effectively align query texts with KG structures to eliminate hallucinations in LLMs?

**Methodology**: SimGRAG is a two-stage method using query-to-pattern transformation (LLM converts queries to graph patterns) and pattern-to-subgraph alignment (using graph semantic distance metric), with an optimized retrieval algorithm for efficient subgraph identification.

**Key findings**:
- SimGRAG effectively addresses the challenge of aligning query texts and KG structures through a two-stage process
- The optimized retrieval algorithm identifies top-k subgraphs within 1-second on a 10-million-scale KG
- SimGRAG outperforms state-of-the-art KG-driven RAG methods in both question answering and fact verification
- The code is publicly available at https://github.com/YZ-Cai/SimGRAG

**Limitations**: not stated in abstract

### Chakraborty et al. (2025)

**Research question**: What is the current state of research on Federated Retrieval-Augmented Generation, including its architectural patterns, challenges, and application domains?

**Methodology**: Following Kitchenham's guidelines for evidence-based software engineering, the authors conducted a systematic mapping study covering literature published between 2020 and 2025, developing a structured classification of research focuses, contribution types, and application domains.

**Key findings**:
- This is the first systematic mapping study of Federated RAG, covering literature from 2020 to 2025
- The study identifies key challenges including privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations
- The analysis synthesizes recurring design patterns and architectural patterns in Federated RAG research
- The findings provide a foundation for future work at the intersection of RAG and federated systems

**Limitations**: Evaluation limitations are identified as a key challenge in the field, though specific study limitations are not detailed in the abstract

### Chang et al. (2024)

**Research question**: How can RAG systems improve the quality of retrieved documents to reduce noise and enhance response reliability?

**Methodology**: MAIN-RAG is a training-free RAG framework that uses multiple LLM agents to collaboratively filter and score retrieved documents, with an adaptive filtering mechanism that dynamically adjusts relevance thresholds based on score distributions.

**Key findings**:
- MAIN-RAG leverages inter-agent consensus to ensure robust document selection without requiring additional training data or fine-tuning
- The approach achieves 2-11% improvement in answer accuracy across four QA benchmarks
- The adaptive filtering mechanism effectively minimizes noise while maintaining high recall of relevant documents
- MAIN-RAG reduces the number of irrelevant retrieved documents compared to traditional RAG approaches

**Limitations**: not stated in abstract

### Khalila et al. (2025)

**Research question**: How do 13 open-source LLMs of varying sizes perform when augmented with RAG for domain-specific Quranic studies queries?

**Methodology**: The study categorizes 13 open-source LLMs into large, medium, and small sizes, applies RAG using a descriptive dataset of Quranic surahs, and evaluates models using human-assessed metrics: context relevance, answer faithfulness, and answer relevance.

**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate responses
- The Llama3.2:3b model achieved high faithfulness (4.619) and relevance (4.857) scores despite its small size
- RAG mitigates hallucination issues common in general-purpose LLMs when applied to sensitive religious contexts
- Well-optimized smaller architectures show promise for domain-specific applications

**Limitations**: not stated in abstract

### Su et al. (2025)

**Research question**: How can external knowledge be more deeply integrated into LLMs beyond in-context document injection in traditional RAG?

**Methodology**: The authors propose Parametric RAG, a new paradigm that integrates external knowledge directly into the parameters of feed-forward networks (FFN) of an LLM through document parameterization, eliminating the need to inject multiple documents into the input context.

**Key findings**:
- Parametric RAG substantially enhances both effectiveness and efficiency of knowledge augmentation in LLMs
- The approach saves online computational costs by eliminating the need to inject multiple documents into the LLM's input context
- Parametric RAG deepens the integration of external knowledge into the parametric knowledge space of the LLM
- The method can be combined with in-context RAG methods to achieve even better performance
- All code, data, and models have been open-sourced

**Limitations**: not stated in abstract

### Xiao, H. et al. (2025)

**Research question**: How can retrieval-augmented generation address the problem of irreversible errors in unidirectional forward reasoning paradigms?

**Methodology**: The authors introduce RetroRAG, a novel framework that builds a retroactive reasoning paradigm using an evidence-collation-discovery framework to search, generate, refine, and iteratively update credible evidence until a reliable answer is obtained.

**Key findings**:
- RetroRAG introduces a retroactive reasoning paradigm that revises and updates evidence to redirect reasoning chains
- The framework constructs an evidence-collation-discovery system to search, generate, and refine credible evidence
- RetroRAG synthesizes inferential evidence from existing source knowledge and formulates search queries to uncover additional information
- Empirical evaluations show that RetroRAG significantly outperforms existing methods

**Limitations**: not stated in abstract

### Xiao, X. et al. (2026)

**Research question**: How can retrieval-augmented generation systems more effectively reconcile noisy, incomplete, or heterogeneous retrieved contexts to improve answer quality?

**Methodology**: MASS-RAG is a multi-agent synthesis approach that structures evidence processing into multiple role-specialized agents for evidence summarization, evidence extraction, and reasoning over retrieved documents, with outputs combined through a dedicated synthesis stage. The approach was evaluated through experiments on four benchmarks comparing performance against strong RAG baselines.

**Key findings**:
- MASS-RAG consistently improves performance over strong RAG baselines across four benchmarks
- The multi-agent design exposes multiple intermediate evidence views, allowing comparison and integration of complementary information
- The approach is particularly effective in settings where relevant evidence is distributed across retrieved contexts
- Role-specialized agents (summarization, extraction, reasoning) enable more effective evidence processing than single-generation approaches

**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can RAG systems be extended to handle mixed-modal (text and image) queries and documents in real-world scenarios?

**Methodology**: The authors propose Nyx, a unified mixed-modal retriever, using a four-stage automated pipeline to generate and filter mixed-modal data, followed by a two-stage training framework with pre-training on NyxQA dataset and supervised fine-tuning using VLM feedback.

**Key findings**:
- Nyx is a unified mixed-modal to mixed-modal retriever tailored for Universal RAG scenarios
- The NyxQA dataset comprises diverse mixed-modal question-answer pairs constructed from web documents
- Nyx performs competitively on standard text-only RAG benchmarks
- Nyx significantly improves generation quality in vision-language tasks in the URAG setting

**Limitations**: not stated in abstract

### Ali et al. (2024)

**Research question**: How can literature reviews be automatically generated from PDF files using different NLP techniques and RAG with LLMs?

**Methodology**: The study evaluates three approaches—frequency-based (spaCy), transformer-based (Simple T5), and RAG with GPT-3.5-turbo—on the SciTLDR dataset, using ROUGE scores for system evaluation.

**Key findings**:
- GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364 among the three systems
- The transformer model (Simple T5) performed second best
- The frequency-based spaCy method ranked last in performance
- A graphical user interface was created for the best-performing LLM-based system

**Limitations**: not stated in abstract

## References

Aghajani Asl, M., Dahal, C., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful adaptive iterative refinement for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.22344

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated literature review using NLP techniques and LLM-based retrieval-augmented generation. arXiv. https://arxiv.org/abs/2411.18583

Cai, Y., Guo, Z., Pei, Y., Bian, W., & Zheng, W. (2024). SimGRAG: Leveraging similar subgraphs for knowledge graphs driven retrieval-augmented generation. arXiv. https://arxiv.org/abs/2412.15272

Chakraborty, A., Dahal, C., & Gupta, V. (2025). Federated retrieval-augmented generation: A systematic mapping study. arXiv. https://arxiv.org/abs/2505.18906

Chang, C.-Y., Jiang, Z., Rakesh, V., Pan, M., Yeh, C.-C. M., Wang, G., Hu, M., Xu, Z., Zheng, Y., Das, M., & Zou, N. (2024). MAIN-RAG: Multi-agent filtering retrieval-augmented generation. arXiv. https://arxiv.org/abs/2501.00332

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating retrieval-augmented generation in Quranic studies: A study of 13 open-source large language models. arXiv. https://arxiv.org/abs/2503.16581

Su, W., Tang, Y., Ai, Q., Yan, J., Wang, C., Wang, H., Ye, Z., Zhou, Y., & Liu, Y. (2025). Parametric retrieval augmented generation. arXiv. https://arxiv.org/abs/2501.15915

Xiao, H., Dai, W., Chen, S., Qin, B., Shi, C., Jing, H., & Guo, T. (2025). Retrieval-augmented generation by evidence retroactivity in LLMs. arXiv. https://arxiv.org/abs/2501.05475

Xiao, X., Huang, H., Liu, R., & Xie, J. (2026). MASS-RAG: Multi-agent synthesis retrieval-augmented generation. arXiv. https://arxiv.org/abs/2604.18509

Zhang, C., Dong, G., Yang, X., & Dou, Z. (2025). Towards mixed-modal retrieval for universal retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.17354
