# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "retrieval-augmented generation", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on retrieval-augmented generation (RAG) from the past two years reveals a field rapidly evolving along multiple dimensions. Researchers are addressing fundamental limitations of traditional RAG systems through novel paradigms: multi-agent architectures for evidence synthesis and filtering, parametric integration of external knowledge, retroactive reasoning to correct errors, and extensions to mixed-modal and federated settings. The collective work demonstrates strong consensus that RAG effectiveness depends critically on how retrieved evidence is processed, refined, and integrated—not merely on retrieval quality alone. Significant advances include iterative refinement frameworks for multi-hop queries, knowledge graph alignment methods, and domain-specific applications in sensitive contexts like religious texts and privacy-preserving environments.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Agent Architectures for Evidence Processing

A prominent direction in recent RAG research involves deploying multiple specialized agents to handle different stages of evidence processing. Rather than relying on a single monolithic pipeline, these systems distribute responsibilities across agents with distinct roles. MASS-RAG (Xiao et al., 2026) structures evidence processing through role-specialized agents for summarization, extraction, and reasoning, then synthesizes their outputs in a dedicated stage. This design exposes multiple intermediate evidence views, enabling comparison and integration of complementary information before answer generation. Similarly, MAIN-RAG (Chang et al., 2024) employs multiple LLM agents to collaboratively filter and score retrieved documents, using inter-agent consensus for robust document selection without requiring additional training. FAIR-RAG (Aghajani Asl et al., 2025) extends this approach with a Structured Evidence Assessment module that deconstructs queries into checklists, audits evidence for gaps, and iteratively generates targeted sub-queries. The convergence on multi-agent designs suggests growing recognition that complex knowledge-intensive tasks require distributed, specialized processing rather than end-to-end monolithic approaches.

### Theme 2: Iterative and Retroactive Reasoning Paradigms

Traditional RAG systems follow unidirectional forward reasoning: retrieve once, then generate. Recent work challenges this paradigm by introducing iterative refinement and retroactive correction mechanisms. FAIR-RAG (Aghajani Asl et al., 2025) achieves an 8.3-point F1 improvement on HotpotQA through iterative evidence gathering, establishing new state-of-the-art performance on multi-hop QA benchmarks. RetroRAG (Xiao et al., 2025) goes further by introducing retroactive reasoning that can revise and update evidence to redirect reasoning chains when errors are detected. The framework constructs an evidence-collation-discovery system that continually updates and organizes evidence as new information is found. This shift from one-shot retrieval to iterative, self-correcting processes represents a fundamental rethinking of how RAG systems should handle complex queries requiring synthesis across disparate sources.

### Theme 3: Deep Knowledge Integration Beyond Context Injection

A third theme explores moving beyond simple in-context document injection toward deeper integration of external knowledge into LLM parameters. Parametric RAG (Su et al., 2025) introduces a paradigm that integrates external knowledge directly into the parameters of feed-forward networks through document parameterization, rather than appending documents to the input context. This approach saves online computational costs by eliminating the need to inject multiple documents into the context while deepening integration of external knowledge into the parametric knowledge space. The authors note that parametric RAG can be combined with in-context RAG methods for even better performance. SimGRAG (Cai et al., 2024) pursues similar deep integration through knowledge graphs, transforming queries into graph patterns and retrieving aligned subgraphs within 1 second even on 10-million-scale knowledge graphs. These approaches suggest that the future of RAG lies not in choosing between parametric and retrieval-based knowledge, but in finding optimal hybrid architectures.

### Theme 4: Domain-Specific and Privacy-Preserving Applications

RAG research is increasingly addressing domain-specific challenges and privacy constraints. The application of RAG to Quranic studies (Khalila et al., 2025) demonstrates how RAG can mitigate hallucination problems in sensitive religious contexts, with larger models consistently outperforming smaller ones while some small models like Llama3.2:3b achieve surprisingly strong performance. Federated RAG (Chakraborty et al., 2025) addresses privacy-sensitive domains like healthcare and finance by combining federated learning with RAG, enabling secure, knowledge-intensive NLP without centralizing data. The systematic mapping study identifies key challenges including privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations. Nyx (Zhang et al., 2025) extends RAG to mixed-modal scenarios involving both text and images, creating a unified retriever for universal RAG settings. These domain-specific adaptations reveal that RAG is maturing from a general-purpose technique into a family of specialized approaches tailored to particular constraints and modalities.

### Theme 5: Automated RAG System Construction

An emerging meta-theme involves using RAG itself to automate the construction of literature reviews and knowledge systems. Ali et al. (2024) demonstrate this by implementing three systems for automated literature review generation from PDF files, with GPT-3.5-turbo-based RAG achieving the highest ROUGE-1 score of 0.364. This self-referential application—using RAG to survey and synthesize literature including RAG itself—illustrates the technology's growing role in automating knowledge work. The finding that LLM-based RAG outperforms both frequency-based and transformer-only approaches reinforces the broader theme that retrieval augmentation provides unique value beyond what parametric knowledge alone can achieve.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong consensus on several points. First, all multi-agent approaches (Chang et al., 2024; Xiao et al., 2026; Aghajani Asl et al., 2025) agree that distributing responsibilities across specialized agents improves robustness and accuracy compared to monolithic pipelines. Second, there is widespread agreement that iterative refinement—whether through retroactive correction (Xiao et al., 2025) or evidence gap analysis (Aghajani Asl et al., 2025)—significantly outperforms one-shot retrieval on complex queries. Third, all domain-specific applications (Khalila et al., 2025; Chakraborty et al., 2025; Zhang et al., 2025) converge on the finding that RAG must be adapted to particular constraints (privacy, modality, domain sensitivity) rather than applied as a one-size-fits-all solution.

**Disagreements**: The literature reveals tension between parametric and in-context integration approaches. Parametric RAG (Su et al., 2025) argues for deep parameter integration to reduce computational costs, while multi-agent systems (Chang et al., 2024; Xiao et al., 2026) assume in-context processing and focus on optimizing retrieval quality and evidence synthesis. These are not mutually exclusive—the parametric RAG authors explicitly note their approach can combine with in-context methods—but they represent different design priorities. Additionally, there is implicit disagreement about model size requirements: while Quranic studies (Khalila et al., 2025) find large models consistently outperform smaller ones, the strong performance of Llama3.2:3b suggests that task-specific fine-tuning or RAG architecture may matter more than raw model size in certain domains.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are discussed only in full papers or that the field has not yet developed standardized approaches to acknowledging constraints. Second, the Federated RAG mapping study (Chakraborty et al., 2025) identifies evaluation limitations as a key challenge, indicating that the field lacks standardized benchmarks and metrics for privacy-preserving RAG systems. Third, while multi-agent approaches show promise, none of the papers provide detailed analysis of the computational overhead or latency costs introduced by coordinating multiple agents—a critical consideration for production deployment. Fourth, the domain-specific applications (Quranic studies, federated settings, mixed-modal) suggest that general-purpose RAG benchmarks may not adequately capture performance in specialized contexts, yet no paper proposes unified evaluation frameworks that span both general and domain-specific settings. Finally, the automated literature review work (Ali et al., 2024) raises questions about using RAG to survey RAG literature itself: how do we ensure such automated surveys remain current and unbiased as the field evolves?

## Per-Paper Annotations

### Aghajani Asl et al. (2025)

**Research question**: How can retrieval-augmented generation frameworks be improved to handle complex, multi-hop queries that require synthesizing information from disparate sources?

**Methodology**: The authors introduce FAIR-RAG, an agentic framework with a Structured Evidence Assessment module that deconstructs queries into checklists, audits evidence for gaps, and iteratively generates targeted sub-queries until sufficient evidence is gathered for faithful generation.

**Key findings**:
- FAIR-RAG significantly outperforms strong baselines on multi-hop QA benchmarks
- On HotpotQA, FAIR-RAG achieves an F1-score of 0.453, an 8.3-point improvement over the strongest iterative baseline
- The framework establishes a new state-of-the-art for iterative RAG methods on HotpotQA, 2WikiMultiHopQA, and MusiQue
- Structured evidence-driven refinement with explicit gap analysis enables more reliable reasoning in complex knowledge-intensive tasks

**Limitations**: Not stated in abstract

### Ali et al. (2024)

**Research question**: How can literature reviews be automatically generated from PDF files using Natural Language Processing techniques and retrieval-augmented generation?

**Methodology**: The study implements three systems using different NLP approaches: a frequency-based method (spaCy), a transformer model (Simple T5), and retrieval-augmented generation with GPT-3.5-turbo, evaluated on the SciTLDR dataset using ROUGE scores.

**Key findings**:
- GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364 among all three systems
- The transformer model (Simple T5) performed second best
- The frequency-based spaCy method ranked last in performance
- A graphical user interface was created for the best-performing LLM-based system

**Limitations**: Not stated in abstract

### Cai et al. (2024)

**Research question**: How can knowledge graph-driven retrieval-augmented generation effectively align query texts with KG structures?

**Methodology**: The authors propose SimGRAG, which addresses query-KG alignment through a two-stage process: query-to-pattern (using an LLM to transform queries into graph patterns) and pattern-to-subgraph (quantifying alignment using a graph semantic distance metric). They also develop an optimized retrieval algorithm that identifies top-k subgraphs within 1 second on a 10-million-scale KG.

**Key findings**:
- SimGRAG addresses KG-driven RAG by aligning query texts and KG structures through a two-stage process
- The query-to-pattern stage uses an LLM to transform queries into desired graph patterns
- The pattern-to-subgraph stage quantifies alignment between patterns and candidate subgraphs using a graph semantic distance metric
- The optimized retrieval algorithm efficiently identifies top-k subgraphs within 1 second on a 10-million-scale KG
- SimGRAG outperforms state-of-the-art KG-driven RAG methods in both question answering and fact verification

**Limitations**: Not stated in abstract

### Chang et al. (2024)

**Research question**: How can retrieval-augmented generation systems improve the quality of retrieved documents to reduce noise and enhance response reliability?

**Methodology**: The authors propose MAIN-RAG, a training-free RAG framework that uses multiple LLM agents to collaboratively filter and score retrieved documents. It introduces an adaptive filtering mechanism that dynamically adjusts relevance thresholds based on score distributions and leverages inter-agent consensus for robust document selection.

**Key findings**:
- MAIN-RAG leverages multiple LLM agents to collaboratively filter and score retrieved documents
- The adaptive filtering mechanism dynamically adjusts relevance thresholds based on score distributions, minimizing noise while maintaining high recall
- The approach uses inter-agent consensus to ensure robust document selection without requiring additional training data or fine-tuning
- MAIN-RAG achieves 2-11% improvement in answer accuracy across four QA benchmarks compared to traditional RAG approaches
- The approach reduces the number of irrelevant retrieved documents while achieving superior response consistency and answer accuracy

**Limitations**: Not stated in abstract

### Chakraborty et al. (2025)

**Research question**: What is the current state of research at the intersection of Federated Learning and Retrieval-Augmented Generation, and what are the key architectural patterns, challenges, and open questions?

**Methodology**: This systematic mapping study follows Kitchenham's guidelines for evidence-based software engineering, analyzing literature from 2020-2025 to classify research focuses, contribution types, application domains, and architectural patterns in Federated RAG.

**Key findings**:
- This is the first systematic mapping study of Federated RAG covering 2020-2025 literature
- Federated RAG offers a promising framework for secure, knowledge-intensive NLP in privacy-sensitive domains like healthcare and finance
- Key challenges include privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations
- The study identifies recurring design patterns and synthesizes temporal trends in this rapidly evolving research area

**Limitations**: The study identifies evaluation limitations as a key challenge in the Federated RAG literature

### Khalila et al. (2025)

**Research question**: How do different open-source large language models perform when applying retrieval-augmented generation to domain-specific, sensitive tasks like Quranic studies?

**Methodology**: The study evaluates 13 open-source LLMs across large, medium, and small categories using a RAG framework with a descriptive dataset of 114 Quranic surahs, assessed by human evaluators on context relevance, answer faithfulness, and answer relevance.

**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate, contextually grounded responses
- Llama3.2:3b (a small model) achieves strong performance with faithfulness score of 4.619 and relevance score of 4.857
- RAG effectively mitigates hallucination problems when applying LLMs to domain-specific religious contexts
- There are trade-offs between model size, computational efficiency, and response quality in domain-specific applications

**Limitations**: Not stated in abstract

### Su et al. (2025)

**Research question**: How can external knowledge be more deeply integrated into large language models beyond in-context document injection in traditional retrieval-augmented generation?

**Methodology**: The authors introduce Parametric RAG, a new paradigm that integrates external knowledge directly into the parameters of feed-forward networks of an LLM through document parameterization, rather than appending documents to the input context.

**Key findings**:
- Parametric RAG substantially enhances both effectiveness and efficiency of knowledge augmentation in LLMs
- The approach saves online computational costs by eliminating the need to inject multiple documents into the input context
- Parametric RAG deepens integration of external knowledge into the parametric knowledge space of the LLM
- Parametric RAG can be combined with in-context RAG methods to achieve even better performance
- All code, data, and models have been open-sourced

**Limitations**: Not stated in abstract

### Xiao et al. (2025)

**Research question**: How can retrieval-augmented generation address the problem of irreversible errors in unidirectional forward reasoning paradigms?

**Methodology**: The authors propose Retroactive Retrieval-Augmented Generation (RetroRAG), a framework that introduces retroactive reasoning by revising and updating evidence to redirect reasoning chains. It uses an evidence-collation-discovery framework to search, generate, and refine credible evidence iteratively.

**Key findings**:
- RetroRAG introduces a retroactive reasoning paradigm that can revise evidence and redirect reasoning chains to the correct direction
- The framework constructs an evidence-collation-discovery system to search, generate, and refine credible evidence from existing source knowledge
- RetroRAG synthesizes inferential evidence related to key entities and formulates search queries to uncover additional information
- The framework continually updates and organizes evidence as new information is found, enhancing its ability to locate further necessary evidence
- Empirical evaluations show that RetroRAG significantly outperforms existing methods

**Limitations**: Not stated in abstract

### Xiao et al. (2026)

**Research question**: How can retrieval-augmented generation systems effectively reconcile noisy, incomplete, or heterogeneous retrieved contexts?

**Methodology**: The authors propose MASS-RAG, a multi-agent synthesis approach that structures evidence processing into multiple role-specialized agents for summarization, extraction, and reasoning. A dedicated synthesis stage combines outputs from these agents to produce the final answer, exposing multiple intermediate evidence views for comparison and integration.

**Key findings**:
- MASS-RAG structures evidence processing into multiple role-specialized agents for summarization, extraction, and reasoning
- The approach combines agent outputs through a dedicated synthesis stage to produce the final answer
- The design exposes multiple intermediate evidence views, allowing the model to compare and integrate complementary information before answer generation
- MASS-RAG consistently improves performance over strong RAG baselines on four benchmarks
- The approach is particularly effective when relevant evidence is distributed across retrieved contexts

**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can retrieval-augmented generation systems handle mixed-modal queries and documents (text and images) in real-world scenarios?

**Methodology**: The authors propose Nyx, a unified mixed-modal to mixed-modal retriever for Universal RAG. They introduce a four-stage automated pipeline to generate and filter mixed-modal data, creating the NyxQA dataset. Nyx uses a two-stage training framework with pre-training on NyxQA and open-source datasets, followed by supervised fine-tuning using feedback from vision-language models.

**Key findings**:
- Nyx is a unified mixed-modal to mixed-modal retriever tailored for Universal RAG scenarios involving text and images
- The authors created NyxQA, a dataset of diverse mixed-modal question-answer pairs constructed from web documents using a four-stage automated pipeline
- Nyx uses a two-stage training framework: pre-training on NyxQA and open-source retrieval datasets, then supervised fine-tuning with VLM feedback
- Nyx performs competitively on standard text-only RAG benchmarks
- Nyx significantly improves generation quality in vision-language tasks and excels in the URAG setting

**Limitations**: Not stated in abstract

## References

Aghajani Asl, M., Asgari-Bidhendi, M., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful adaptive iterative refinement for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.22344

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated literature review using NLP techniques and LLM-based retrieval-augmented generation. arXiv. https://arxiv.org/abs/2411.18583

Cai, Y., Guo, Z., Pei, Y., Bian, W., & Zheng, W. (2024). SimGRAG: Leveraging similar subgraphs for knowledge graphs driven retrieval-augmented generation. arXiv. https://arxiv.org/abs/2412.15272

Chang, C.-Y., Jiang, Z., Rakesh, V., Pan, M., Yeh, C.-C. M., Wang, G., Hu, M., Xu, Z., Zheng, Y., Das, M., & Zou, N. (2024). MAIN-RAG: Multi-agent filtering retrieval-augmented generation. arXiv. https://arxiv.org/abs/2501.00332

Chakraborty, A., Dahal, C., & Gupta, V. (2025). Federated retrieval-augmented generation: A systematic mapping study. arXiv. https://arxiv.org/abs/2505.18906

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating retrieval-augmented generation in Quranic studies: A study of 13 open-source large language models. arXiv. https://arxiv.org/abs/2503.16581

Su, W., Tang, Y., Ai, Q., Yan, J., Wang, C., Wang, H., Ye, Z., Zhou, Y., & Liu, Y. (2025). Parametric retrieval augmented generation. arXiv. https://arxiv.org/abs/2501.15915

Xiao, L., Dai, W., Chen, S., Qin, B., Shi, C., Jing, H., & Guo, T. (2025). Retrieval-augmented generation by evidence retroactivity in LLMs. arXiv. https://arxiv.org/abs/2501.05475

Xiao, X., Huang, H., Liu, R., & Xie, J. (2026). MASS-RAG: Multi-agent synthesis retrieval-augmented generation. arXiv. https://arxiv.org/abs/2604.18509

Zhang, C., Dong, G., Yang, X., & Dou, Z. (2025). Towards mixed-modal retrieval for universal retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.17354
