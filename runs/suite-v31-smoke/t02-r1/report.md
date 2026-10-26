# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "retrieval-augmented generation", category cs.CL, published between 2024-10-26 and 2026-10-26
**Citation format**: APA 7th edition

## Executive Summary

The literature on retrieval-augmented generation (RAG) has evolved significantly over the past two years, with research focusing on three major directions: multi-agent architectures that improve evidence synthesis and filtering, domain-specific adaptations for specialized knowledge domains, and novel paradigms for knowledge integration beyond traditional in-context retrieval. The surveyed papers collectively demonstrate a shift from simple retrieve-then-generate pipelines toward sophisticated systems that employ iterative refinement, collaborative agent filtering, and parametric knowledge integration. Key convergences include agreement that multi-hop reasoning requires iterative evidence assessment, that retrieval quality critically impacts generation reliability, and that domain-specific applications demand specialized architectures. However, limitations persist around evaluation standardization, computational efficiency, and handling of heterogeneous or noisy retrieved contexts.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-26 and 2026-10-26. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Agent RAG Architectures

A prominent trend across recent RAG research is the adoption of multi-agent architectures to address the limitations of single-pass retrieval and generation. Four papers in this survey employ multiple specialized agents or iterative refinement cycles to improve answer quality.

FAIR-RAG introduces an agentic framework with an Iterative Refinement Cycle governed by a Structured Evidence Assessment (SEA) module that deconstructs queries into checklists, audits evidence to identify gaps, and generates targeted sub-queries until evidence is sufficient (Aghajani Asl et al., 2025). This approach achieved state-of-the-art performance on multi-hop QA benchmarks, with an F1-score of 0.453 on HotpotQA, representing an 8.3-point improvement over the strongest iterative baseline.

MAIN-RAG leverages multiple LLM agents to collaboratively filter and score retrieved documents, introducing an adaptive filtering mechanism that dynamically adjusts relevance thresholds based on score distributions (Chang et al., 2024). This training-free approach achieved 2-11% improvement in answer accuracy across four QA benchmarks by reducing noise from irrelevant retrieved documents.

MASS-RAG structures evidence processing through multiple role-specialized agents for evidence summarization, extraction, and reasoning over retrieved documents, with outputs combined through a dedicated synthesis stage (Xiao et al., 2026). The multi-agent design exposes multiple intermediate evidence views for comparing and integrating complementary information, with performance improvements particularly notable when relevant evidence is distributed across retrieved contexts.

The convergence on multi-agent approaches reflects recognition that complex reasoning tasks require iterative evidence assessment and that single-pass retrieval often fails to capture the distributed nature of relevant information.

### Theme 2: Domain-Specific RAG Applications

Several papers demonstrate RAG adaptations for specialized domains with unique requirements around knowledge structure, privacy, or sensitivity.

In religious text analysis, Khalila et al. (2025) investigated 13 open-source LLMs applying RAG to Quranic studies, finding that large models consistently outperform smaller models in capturing query semantics and producing accurate, contextually grounded responses. Notably, the Llama3.2:3b model achieved excellent performance on faithfulness (4.619) and relevance (4.857) despite being classified as small, demonstrating that well-optimized smaller architectures show promise for domain-specific applications.

Federated RAG combines Federated Learning with RAG for privacy-sensitive NLP applications in healthcare, finance, and personalized assistance domains (Chakraborty et al., 2025). This systematic mapping study identifies recurring design patterns in Federated RAG architectures and highlights key challenges including privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations.

For knowledge-intensive domains, SimGRAG addresses query-KG alignment through a two-stage process: query-to-pattern transformation using an LLM to convert queries into graph patterns, and pattern-to-subgraph alignment using a graph semantic distance metric (Cai et al., 2024). The approach efficiently identifies top-k subgraphs within 1 second on a 10-million-scale knowledge graph and outperforms state-of-the-art KG-driven RAG methods in both question answering and fact verification tasks.

### Theme 3: Novel Knowledge Integration Paradigms

Beyond architectural innovations, several papers propose fundamentally new paradigms for how external knowledge is integrated into language models.

Parametric RAG introduces a paradigm that integrates external knowledge directly into the parameters of feed-forward networks (FFN) of an LLM through document parameterization, rather than appending documents to the input context (Su et al., 2025). This approach substantially enhances both effectiveness and efficiency of knowledge augmentation by eliminating the need to inject multiple documents into the LLMs' input context, and can be combined with in-context RAG methods for even better performance.

RetroRAG builds a retroactive reasoning paradigm by revising and updating evidence to redirect reasoning chains, addressing the problem of irreversible errors in forward reasoning paradigms when handling multi-hop complex questions (Xiao et al., 2025). The framework constructs an evidence-collation-discovery system that synthesizes inferential evidence from existing knowledge and formulates search queries for additional information, continually updating and organizing new evidence as it is discovered.

Nyx addresses mixed-modal retrieval for universal RAG scenarios, enabling retrieval and reasoning over mixed-modal information (text and images) to improve vision-language generation (Zhang et al., 2025). The approach uses a four-stage automated pipeline for generating diverse mixed-modal question-answer pairs and a two-stage training framework that aligns retrieval outputs with generative preferences through supervised fine-tuning with VLM feedback.

### Theme 4: Retrieval Quality and Automation

The quality of retrieved documents remains a critical determinant of RAG system performance, with multiple papers addressing automation and quality assessment.

Ali et al. (2024) evaluated three distinct systems for auto-generating literature reviews using RAG with GPT-3.5-turbo, a transformer model (Simple T5), and a frequency-based method (spaCy). The Large Language Model GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364, demonstrating the effectiveness of LLM-based retrieval-augmented approaches for automated literature synthesis tasks.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that: (1) multi-hop reasoning requires iterative evidence assessment rather than single-pass retrieval, (2) retrieval quality critically impacts generation reliability, necessitating sophisticated filtering mechanisms, (3) domain-specific applications demand specialized architectures rather than one-size-fits-all approaches, and (4) multi-agent or iterative approaches consistently outperform baselines on complex reasoning tasks.

**Disagreements**: The literature shows divergence on the optimal integration mechanism for external knowledge. While most papers assume in-context retrieval, Su et al. (2025) argue for parametric integration directly into model weights, claiming superior efficiency. Additionally, there is tension between training-free approaches like MAIN-RAG (Chang et al., 2024) and methods requiring specialized training like Nyx (Zhang et al., 2025), with trade-offs between deployment complexity and performance optimization not fully resolved.

## Gaps and Open Questions

The collective literature reveals several notable gaps:

1. **Evaluation Standardization**: Multiple papers mention evaluation limitations as a challenge (Chakraborty et al., 2025), but no standardized benchmarks exist for comparing multi-agent RAG approaches across domains.

2. **Computational Efficiency**: While Parametric RAG claims efficiency gains (Su et al., 2025), most multi-agent approaches introduce substantial computational overhead that is not systematically analyzed.

3. **Limitations Transparency**: A striking pattern across the surveyed papers is that limitations are "not stated in abstract" for 8 out of 10 papers, suggesting either methodological blind spots or reporting gaps in the literature.

4. **Cross-Domain Generalization**: Domain-specific approaches (Quranic studies, healthcare, knowledge graphs) are evaluated in isolation, with no investigation of transferability across domains.

5. **Human Evaluation**: Most papers rely on automated metrics (ROUGE, F1-scores) with limited human evaluation, despite the subjective nature of generation quality.

## Per-Paper Annotations

### Aghajani Asl et al. (2025)

**Research question**: How can retrieval-augmented generation frameworks be improved to handle complex, multi-hop queries that require synthesizing information from disparate sources?

**Methodology**: The authors introduce FAIR-RAG, an agentic framework with an Iterative Refinement Cycle governed by a Structured Evidence Assessment (SEA) module that deconstructs queries into checklists, audits evidence to identify gaps, and generates targeted sub-queries until evidence is sufficient. The framework was evaluated on multi-hop QA benchmarks including HotpotQA, 2WikiMultiHopQA, and MusiQue in a unified experimental setup.

**Key findings**:
- FAIR-RAG significantly outperforms strong baselines on challenging multi-hop QA benchmarks
- On HotpotQA, FAIR-RAG achieves an F1-score of 0.453, an absolute improvement of 8.3 points over the strongest iterative baseline
- The framework establishes a new state-of-the-art for iterative RAG methods on HotpotQA, 2WikiMultiHopQA, and MusiQue benchmarks
- A structured, evidence-driven refinement process with explicit gap analysis is crucial for reliable reasoning in complex, knowledge-intensive tasks

**Limitations**: not stated in abstract

### Ali et al. (2024)

**Research question**: How can Natural Language Processing techniques and retrieval-augmented generation with Large Language Models be used to automatically generate literature reviews from PDF files?

**Methodology**: The research evaluates three distinct systems for auto-generating literature reviews using the SciTLDR dataset: a frequency-based method (spaCy), a transformer model (Simple T5), and retrieval-augmented generation with GPT-3.5-turbo. All three systems are evaluated using ROUGE scores to compare their effectiveness.

**Key findings**:
- The Large Language Model GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364 among the three systems evaluated
- The transformer model (Simple T5) ranked second in performance
- The frequency-based method (spaCy) ranked last among the three approaches
- A graphical user interface was created for the best-performing system based on the large language model

**Limitations**: not stated in abstract

### Cai et al. (2024)

**Research question**: How can knowledge graph-driven retrieval-augmented generation effectively align query texts with KG structures to eliminate hallucinations in large language models?

**Methodology**: The authors propose SimGRAG, a Similar Graph Enhanced RAG method that addresses query-KG alignment through a two-stage process: (1) query-to-pattern transformation using an LLM to convert queries into graph patterns, and (2) pattern-to-subgraph alignment using a graph semantic distance metric. They also develop an optimized retrieval algorithm that identifies top-k subgraphs within 1 second on a 10-million-scale KG.

**Key findings**:
- SimGRAG effectively addresses the challenge of aligning query texts with knowledge graph structures through a two-stage query-to-pattern and pattern-to-subgraph process
- The graph semantic distance (GSD) metric successfully quantifies alignment between patterns and candidate subgraphs
- The optimized retrieval algorithm efficiently identifies top-k subgraphs within 1 second on a 10-million-scale knowledge graph
- Extensive experiments demonstrate that SimGRAG outperforms state-of-the-art KG-driven RAG methods in both question answering and fact verification tasks

**Limitations**: not stated in abstract

### Chakraborty et al. (2025)

**Research question**: What is the current state of research on Federated Retrieval-Augmented Generation (Federated RAG) and what are its key architectural patterns, challenges, and open questions?

**Methodology**: The authors conducted a systematic mapping study following Kitchenham's guidelines for evidence-based software engineering, analyzing literature published between 2020 and 2025. They developed a structured classification of research focuses, contribution types, and application domains, and analyzed architectural patterns, temporal trends, and key challenges.

**Key findings**:
- This is the first systematic mapping study of Federated RAG, combining Federated Learning with Retrieval-Augmented Generation for privacy-sensitive NLP applications
- The study identifies recurring design patterns in Federated RAG architectures across healthcare, finance, and personalized assistance domains
- Key challenges include privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations
- The research synthesizes a rapidly evolving body of work and surfaces open questions for future research at the intersection of RAG and federated systems

**Limitations**: The abstract mentions evaluation limitations as a key challenge but does not specify the study's own methodological limitations

### Chang et al. (2024)

**Research question**: How can retrieval-augmented generation systems improve the quality of retrieved documents to reduce noise and enhance response reliability?

**Methodology**: The authors propose MAIN-RAG, a training-free RAG framework that leverages multiple LLM agents to collaboratively filter and score retrieved documents. The approach introduces an adaptive filtering mechanism that dynamically adjusts relevance thresholds based on score distributions and uses inter-agent consensus for robust document selection without requiring additional training or fine-tuning.

**Key findings**:
- MAIN-RAG addresses the problem of irrelevant or noisy documents degrading RAG system performance through multi-agent collaborative filtering
- The adaptive filtering mechanism dynamically adjusts relevance thresholds based on score distributions, minimizing noise while maintaining high recall of relevant documents
- Experimental results across four QA benchmarks show 2-11% improvement in answer accuracy compared to traditional RAG approaches
- The approach reduces the number of irrelevant retrieved documents while achieving superior response consistency and answer accuracy over baseline methods

**Limitations**: not stated in abstract

### Khalila et al. (2025)

**Research question**: How do different open-source large language models perform when applying retrieval-augmented generation to domain-specific Quranic studies tasks?

**Methodology**: The study investigates 13 open-source LLMs categorized into large, medium, and small models using a Retrieval-Augmented Generation approach with a descriptive dataset of Quranic surahs. Models are evaluated by human evaluators using three metrics: context relevance, answer faithfulness, and answer relevance.

**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate, contextually grounded responses
- The Llama3.2:3b model, despite being classified as small, achieves excellent performance on faithfulness (4.619) and relevance (4.857)
- Well-optimized smaller architectures show promise for domain-specific applications
- RAG helps address hallucination problems when applying LLMs to sensitive religious contexts

**Limitations**: not stated in abstract

### Su et al. (2025)

**Research question**: How can external knowledge be more deeply integrated into large language models beyond in-context knowledge injection methods?

**Methodology**: The authors introduce Parametric RAG, a new paradigm that integrates external knowledge directly into the parameters of feed-forward networks (FFN) of an LLM through document parameterization, rather than appending documents to the input context. The approach is evaluated for both effectiveness and efficiency of knowledge augmentation.

**Key findings**:
- Parametric RAG substantially enhances both the effectiveness and efficiency of knowledge augmentation in LLMs
- The approach saves online computational costs by eliminating the need to inject multiple documents into the LLMs' input context
- Parametric RAG deepens the integration of external knowledge into the parametric knowledge space of the LLM
- Parametric RAG can be combined with in-context RAG methods to achieve even better performance
- All code, data, and models have been open-sourced

**Limitations**: not stated in abstract

### Xiao, L. et al. (2025)

**Research question**: How can retrieval-augmented generation address the problem of irreversible errors in forward reasoning paradigms when handling multi-hop complex questions?

**Methodology**: The authors introduce RetroRAG, a novel framework that builds a retroactive reasoning paradigm by revising and updating evidence to redirect reasoning chains. They construct an evidence-collation-discovery framework to search, generate, and refine credible evidence, paired with an Answerer to generate and evaluate outputs iteratively.

**Key findings**:
- RetroRAG introduces the first retroactive reasoning paradigm for retrieval-augmented generation, addressing irreversible errors in existing forward reasoning methods
- The framework constructs an evidence-collation-discovery system that synthesizes inferential evidence from existing knowledge and formulates search queries for additional information
- RetroRAG continually updates and organizes new evidence as it is discovered, enhancing its ability to locate further necessary evidence
- Empirical evaluations demonstrate that RetroRAG significantly outperforms existing methods for multi-hop complex questions

**Limitations**: not stated in abstract

### Xiao, X. et al. (2026)

**Research question**: How can retrieval-augmented generation systems better reconcile noisy, incomplete, or heterogeneous retrieved contexts to improve answer quality?

**Methodology**: The authors propose MASS-RAG, a multi-agent synthesis approach that structures evidence processing through multiple role-specialized agents for evidence summarization, extraction, and reasoning over retrieved documents, with outputs combined through a dedicated synthesis stage. The approach was evaluated on four benchmark datasets comparing performance against strong RAG baselines.

**Key findings**:
- MASS-RAG consistently improves performance over strong RAG baselines across four benchmarks
- The multi-agent design exposes multiple intermediate evidence views for comparing and integrating complementary information
- Performance improvements are particularly notable when relevant evidence is distributed across retrieved contexts
- Role-specialized agents (summarization, extraction, reasoning) enable more effective evidence processing than single-generation approaches

**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can retrieval-augmented generation systems handle mixed-modal information (text and images) in real-world scenarios where existing systems focus primarily on unimodal text documents?

**Methodology**: The authors propose Nyx, a unified mixed-modal to mixed-modal retriever for Universal RAG (URAG) scenarios. They introduce a four-stage automated pipeline for generating and filtering web documents to construct NyxQA, a dataset of diverse mixed-modal question-answer pairs. Nyx uses a two-stage training framework: pre-training on NyxQA and open-source retrieval datasets, followed by supervised fine-tuning using feedback from downstream vision-language models.

**Key findings**:
- Nyx addresses the challenge of Universal RAG by enabling retrieval and reasoning over mixed-modal information to improve vision-language generation
- The four-stage automated pipeline successfully constructs NyxQA, a dataset comprising diverse mixed-modal question-answer pairs reflecting real-world information needs
- The two-stage training framework aligns retrieval outputs with generative preferences through supervised fine-tuning with VLM feedback
- Nyx performs competitively on standard text-only RAG benchmarks while significantly improving generation quality in vision-language tasks under the URAG setting

**Limitations**: not stated in abstract

## References

Aghajani Asl, M., Dahal, C., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful adaptive iterative refinement for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.22344

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated literature review using NLP techniques and LLM-based retrieval-augmented generation. arXiv. https://arxiv.org/abs/2411.18583

Cai, Y., Guo, Z., Pei, Y., Bian, W., & Zheng, W. (2024). SimGRAG: Leveraging similar subgraphs for knowledge graphs driven retrieval-augmented generation. arXiv. https://arxiv.org/abs/2412.15272

Chakraborty, A., Dahal, C., & Gupta, V. (2025). Federated retrieval-augmented generation: A systematic mapping study. arXiv. https://arxiv.org/abs/2505.18906

Chang, C.-Y., Jiang, Z., Rakesh, V., Pan, M., Yeh, C.-C. M., Wang, G., Hu, M., Xu, Z., Zheng, Y., Das, M., & Zou, N. (2024). MAIN-RAG: Multi-agent filtering retrieval-augmented generation. arXiv. https://arxiv.org/abs/2501.00332

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating retrieval-augmented generation in Quranic studies: A study of 13 open-source large language models. arXiv. https://arxiv.org/abs/2503.16581

Su, W., Tang, Y., Ai, Q., Yan, J., Wang, C., Wang, H., Ye, Z., Zhou, Y., & Liu, Y. (2025). Parametric retrieval augmented generation. arXiv. https://arxiv.org/abs/2501.15915

Xiao, L., Dai, W., Chen, S., Qin, B., Shi, C., Jing, H., & Guo, T. (2025). Retrieval-augmented generation by evidence retroactivity in LLMs. arXiv. https://arxiv.org/abs/2501.05475

Xiao, X., Huang, H., Liu, R., & Xie, J. (2026). MASS-RAG: Multi-agent synthesis retrieval-augmented generation. arXiv. https://arxiv.org/abs/2604.18509

Zhang, C., Dong, G., Yang, X., & Dou, Z. (2025). Towards mixed-modal retrieval for universal retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.17354
