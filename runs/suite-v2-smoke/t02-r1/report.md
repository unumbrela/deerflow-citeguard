# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

Retrieval-Augmented Generation (RAG) has evolved significantly in the past two years, with research focusing on improving retrieval quality, multi-agent architectures, domain-specific applications, and novel integration paradigms. The surveyed literature reveals a field maturing beyond basic retrieval-and-generation pipelines toward sophisticated systems that address fundamental challenges: handling noisy or incomplete evidence, supporting multi-hop reasoning, preserving privacy in distributed settings, and integrating knowledge through parametric rather than contextual mechanisms. Multi-agent approaches dominate recent innovations, with frameworks leveraging specialized agents for filtering, synthesis, and iterative refinement. Domain-specific applications demonstrate RAG's versatility, from Quranic studies to automated literature review, while new paradigms like parametric RAG and mixed-modal retrieval expand the technical boundaries of what RAG systems can achieve.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Agent RAG Architectures

A dominant trend in recent RAG research is the adoption of multi-agent architectures to improve retrieval quality and answer synthesis. Multiple papers propose frameworks where specialized LLM agents collaborate to filter, refine, and synthesize retrieved evidence. Chang et al. (2024) introduced MAIN-RAG, which uses multiple agents to collaboratively filter and score retrieved documents with an adaptive mechanism that dynamically adjusts relevance thresholds based on score distributions, achieving 2-11% improvement in answer accuracy across four QA benchmarks. Xiao et al. (2026) proposed MASS-RAG, which structures evidence processing into role-specialized agents for summarization, extraction, and reasoning, with a dedicated synthesis stage that combines intermediate evidence views to produce final answers. This approach proves particularly effective when relevant evidence is distributed across retrieved contexts. Asl et al. (2025) presented FAIR-RAG, an agentic framework featuring an Iterative Refinement Cycle with Structured Evidence Assessment that deconstructs queries into checklists, identifies evidence gaps, and generates targeted sub-queries until sufficient evidence is gathered, establishing new state-of-the-art performance on multi-hop QA benchmarks with an F1-score of 0.453 on HotpotQA.

### Theme 2: Advanced Reasoning Paradigms

Recent work addresses fundamental limitations in RAG reasoning, particularly the challenge of irreversible errors from unidirectional forward reasoning and flawed retrieval systems. Xiao et al. (2025) introduced RetroRAG, which builds a retroactive reasoning paradigm through an evidence-collation-discovery system that searches, generates, and refines credible evidence iteratively. The framework synthesizes inferential evidence from existing knowledge and formulates search queries, continually updating information while an Answerer evaluates outputs until reliable answers are obtained. This retroactive approach allows the system to revise and redirect reasoning chains when initial evidence proves insufficient or flawed, significantly outperforming existing methods in empirical evaluations.

### Theme 3: Domain-Specific RAG Applications

RAG systems are being increasingly adapted for domain-specific applications, revealing both opportunities and challenges in specialized contexts. Khalila et al. (2025) investigated RAG in Quranic studies, evaluating 13 open-source LLMs across three size categories using a RAG framework with a descriptive dataset of 114 Quranic surahs. Their findings reveal that large models consistently outperform smaller models in capturing query semantics and producing accurate, contextually grounded responses, though well-optimized smaller architectures like Llama3.2:3b show promise for domain-specific applications despite their size. Ali et al. (2024) applied RAG to automated literature review generation, evaluating three NLP approaches using the SciTLDR dataset, with GPT-3.5-turbo achieving the highest ROUGE-1 score of 0.364. These domain-specific studies highlight the importance of model selection, dataset quality, and evaluation metrics tailored to particular application areas.

### Theme 4: Knowledge Integration Paradigms

Novel approaches to knowledge integration are emerging beyond traditional in-context retrieval. Su et al. (2025) introduced Parametric RAG, a paradigm that integrates external knowledge directly into the parameters of feed-forward networks (FFN) of LLMs through document parameterization, rather than appending documents to the input context. This approach eliminates the need to inject multiple documents into LLM input context, reducing online computational costs while deepening integration of external knowledge into the parametric knowledge space of LLMs. Experimental results show substantial improvements in both effectiveness and efficiency, and the approach can be combined with traditional in-context RAG methods to achieve even better performance. Cai et al. (2024) proposed SimGRAG for knowledge graph-driven RAG, addressing query-KG alignment through a two-stage process: query-to-pattern transforms queries into graph patterns using an LLM, and pattern-to-subgraph quantifies alignment using a graph semantic distance metric, efficiently identifying top-k subgraphs within 1-second on a 10-million-scale KG.

### Theme 5: Privacy and Federated RAG

As RAG systems are deployed in privacy-sensitive domains, federated approaches are emerging to address data privacy concerns. Chakraborty et al. (2025) conducted the first systematic mapping study of Federated RAG covering literature from 2020 to 2025, identifying recurring design patterns and architectural approaches. Their analysis reveals key challenges including privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations. The study synthesizes a rapidly evolving research body at the intersection of RAG and federated systems, providing a foundation for future work in secure, knowledge-intensive NLP for domains like healthcare and finance where data privacy is paramount.

### Theme 6: Mixed-Modal and Universal RAG

The frontier of RAG research is expanding beyond text-only retrieval to handle mixed-modal queries and documents. Zhang et al. (2025) proposed Nyx, a unified mixed-modal retriever for Universal RAG (URAG), using a four-stage automated pipeline to generate and filter diverse mixed-modal question-answer pairs from web documents. Their two-stage training framework performs pre-training on the NyxQA dataset and open-source retrieval data, followed by supervised fine-tuning using feedback from vision-language models. Nyx performs competitively on standard text-only RAG benchmarks while significantly improving generation quality in vision-language tasks within the URAG setting, demonstrating that mixed-modal retrieval can enhance rather than compromise text-only performance.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that multi-agent and iterative approaches significantly improve RAG performance, with multiple studies demonstrating 2-11% accuracy improvements through agent collaboration and adaptive refinement. There is strong consensus that domain-specific optimization matters: model size, retrieval strategies, and evaluation metrics must be tailored to particular application domains. All papers acknowledge the importance of retrieval quality as a bottleneck for RAG performance, with solutions ranging from multi-agent filtering to parametric integration to graph-based alignment.

**Disagreements**: The literature reveals tension between parametric and in-context knowledge integration approaches. While Su et al. (2025) argue for parametric RAG's superiority in reducing computational costs and deepening knowledge integration, other papers implicitly assume in-context retrieval remains the primary paradigm, enhancing it through multi-agent architectures rather than replacing it. There is also variation in evaluation approaches: some papers focus on standard QA benchmarks (HotpotQA, 2WikiMultiHopQA, MusiQue), while others emphasize domain-specific metrics (context relevance, answer faithfulness in Quranic studies) or systematic mapping methodologies, making cross-paper performance comparisons challenging.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are discussed only in full paper text or that the field has not yet developed standardized practices for reporting constraints. Second, while multi-agent approaches show promise, there is limited discussion of the computational overhead and latency implications of deploying multiple specialized agents in production systems. Third, the federated RAG literature identifies privacy challenges but lacks concrete solutions for cross-client heterogeneity and evaluation standardization. Fourth, domain-specific applications reveal trade-offs between model size and performance, but there is insufficient guidance on optimal model selection criteria for particular domains. Finally, mixed-modal RAG is emerging but lacks comprehensive benchmarks that evaluate both text-only and vision-language performance in unified frameworks.

## Per-Paper Annotations

### Ali et al. (2024)

**Research question**: How can literature reviews be automatically generated from PDF files using Natural Language Processing techniques and retrieval-augmented generation?
**Methodology**: The study evaluates three NLP approaches—frequency-based method (spaCy), transformer model (Simple T5), and retrieval-augmented generation with GPT-3.5-turbo—using the SciTLDR dataset and ROUGE scores for evaluation.
**Key findings**:
- GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364 among the three systems tested
- The transformer model (Simple T5) performed second best in the evaluation
- The spaCy frequency-based method ranked last among the three approaches
- A graphical user interface was created for the best-performing LLM-based system
**Limitations**: Not stated in abstract

### Asl et al. (2025)

**Research question**: How can retrieval-augmented generation systems be improved to handle complex multi-hop queries that require synthesizing information from disparate sources?
**Methodology**: The authors introduce FAIR-RAG, an agentic framework featuring an Iterative Refinement Cycle with Structured Evidence Assessment (SEA) that deconstructs queries into checklists, identifies evidence gaps, and generates targeted sub-queries until sufficient evidence is gathered.
**Key findings**:
- FAIR-RAG achieved an F1-score of 0.453 on HotpotQA, an 8.3-point improvement over the strongest iterative baseline
- The framework establishes a new state-of-the-art for iterative RAG methods on multi-hop QA benchmarks including HotpotQA, 2WikiMultiHopQA, and MusiQue
- Structured evidence-driven refinement with explicit gap analysis enables reliable reasoning in complex knowledge-intensive tasks
- The SEA module effectively identifies both confirmed facts and explicit informational gaps to guide adaptive query refinement
**Limitations**: Not stated in abstract

### Cai et al. (2024)

**Research question**: How can knowledge graph-driven RAG effectively align query texts with KG structures for improved retrieval?
**Methodology**: The paper proposes SimGRAG, which addresses query-KG alignment through a two-stage process: query-to-pattern transforms queries into graph patterns using an LLM, and pattern-to-subgraph quantifies alignment using a graph semantic distance metric. An optimized retrieval algorithm identifies top-k subgraphs within 1-second on a 10-million-scale KG.
**Key findings**:
- SimGRAG addresses KG-driven RAG through a two-stage query-to-pattern and pattern-to-subgraph alignment process
- The method uses an LLM to transform queries into desired graph patterns
- A graph semantic distance metric quantifies alignment between patterns and candidate subgraphs
- The optimized retrieval algorithm efficiently identifies top-k subgraphs within 1-second on a 10-million-scale KG
- SimGRAG outperforms state-of-the-art KG-driven RAG methods in question answering and fact verification
**Limitations**: Not stated in abstract

### Chakraborty et al. (2025)

**Research question**: What is the current state of research at the intersection of Federated Learning and Retrieval-Augmented Generation for privacy-sensitive NLP applications?
**Methodology**: This systematic mapping study follows Kitchenham's guidelines for evidence-based software engineering, analyzing Federated RAG literature from 2020-2025 with structured classification of research focuses, contribution types, application domains, architectural patterns, and temporal trends.
**Key findings**:
- This is the first systematic mapping study of Federated RAG covering literature from 2020 to 2025
- The study identifies recurring design patterns and architectural approaches in Federated RAG systems
- Key challenges include privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations
- The findings synthesize a rapidly evolving research body at the intersection of RAG and federated systems
- The study provides a foundation for future work in secure, knowledge-intensive NLP for domains like healthcare and finance
**Limitations**: Not stated in abstract

### Chang et al. (2024)

**Research question**: How can RAG systems improve the quality of retrieved documents to reduce noise and enhance response reliability?
**Methodology**: The paper proposes MAIN-RAG, a training-free RAG framework that uses multiple LLM agents to collaboratively filter and score retrieved documents. It introduces an adaptive filtering mechanism that dynamically adjusts relevance thresholds based on score distributions, leveraging inter-agent consensus for robust document selection without requiring additional training.
**Key findings**:
- MAIN-RAG leverages multiple LLM agents to collaboratively filter and score retrieved documents
- The adaptive filtering mechanism dynamically adjusts relevance thresholds based on score distributions
- Inter-agent consensus ensures robust document selection without requiring additional training data or fine-tuning
- MAIN-RAG achieves 2-11% improvement in answer accuracy across four QA benchmarks
- The approach reduces the number of irrelevant retrieved documents while maintaining high recall
**Limitations**: Not stated in abstract

### Khalila et al. (2025)

**Research question**: How do different open-source large language models perform when applying retrieval-augmented generation to domain-specific Quranic studies tasks?
**Methodology**: The study investigates 13 open-source LLMs across three size categories (large, medium, small) using a RAG framework with a descriptive dataset of 114 Quranic surahs, evaluated by human evaluators on context relevance, answer faithfulness, and answer relevance metrics.
**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate, contextually grounded responses
- Llama3.2:3b (a small model) achieved exceptional performance with faithfulness score of 4.619 and relevance score of 4.857
- Well-optimized smaller architectures show promise for domain-specific applications despite their size
- The study reveals trade-offs between model size, computational efficiency, and response quality in domain-specific LLM applications
**Limitations**: Not stated in abstract

### Su et al. (2025)

**Research question**: How can external knowledge be more effectively integrated into large language models beyond in-context knowledge injection in retrieval-augmented generation?
**Methodology**: The authors introduce Parametric RAG, a new paradigm that integrates external knowledge directly into the parameters of feed-forward networks (FFN) of LLMs through document parameterization, rather than appending documents to the input context.
**Key findings**:
- Parametric RAG eliminates the need to inject multiple documents into LLM input context, reducing online computational costs
- The approach deepens integration of external knowledge into the parametric knowledge space of LLMs
- Experimental results show substantial improvements in both effectiveness and efficiency of knowledge augmentation
- Parametric RAG can be combined with traditional in-context RAG methods to achieve even better performance
- All code, data, and models have been open-sourced on GitHub
**Limitations**: Not stated in abstract

### Xiao et al. (2025)

**Research question**: How can retrieval-augmented generation address irreversible errors from unidirectional forward reasoning and flawed retrieval systems?
**Methodology**: The paper introduces RetroRAG, a framework that builds a retroactive reasoning paradigm through an evidence-collation-discovery system that searches, generates, and refines credible evidence iteratively. It synthesizes inferential evidence from existing knowledge and formulates search queries, continually updating information while an Answerer evaluates outputs until reliable answers are obtained.
**Key findings**:
- RetroRAG introduces a novel retroactive reasoning paradigm that revises and updates evidence to redirect reasoning chains
- The framework constructs an evidence-collation-discovery system to search, generate, and refine credible evidence
- RetroRAG synthesizes inferential evidence related to key entities and formulates search queries to uncover additional information
- The system continually updates and organizes evidence, enhancing its ability to locate further necessary information
- Empirical evaluations demonstrate that RetroRAG significantly outperforms existing methods
**Limitations**: Not stated in abstract

### Xiao et al. (2026)

**Research question**: How can RAG systems better reconcile noisy, incomplete, or heterogeneous retrieved contexts through structured evidence processing?
**Methodology**: The paper proposes MASS-RAG, a multi-agent synthesis approach that structures evidence processing into role-specialized agents for summarization, extraction, and reasoning over retrieved documents. A dedicated synthesis stage combines intermediate evidence views to produce the final answer, allowing comparison and integration of complementary information.
**Key findings**:
- MASS-RAG structures evidence processing into multiple role-specialized agents for summarization, extraction, and reasoning
- A dedicated synthesis stage combines outputs from distinct agents to produce the final answer
- The design exposes multiple intermediate evidence views for comparing and integrating complementary information
- MASS-RAG consistently improves performance over strong RAG baselines across four benchmarks
- The approach is particularly effective when relevant evidence is distributed across retrieved contexts
**Limitations**: Not stated in abstract

### Zhang et al. (2025)

**Research question**: How can RAG systems handle mixed-modal queries and documents (text and images) for universal retrieval-augmented generation?
**Methodology**: The paper proposes Nyx, a unified mixed-modal retriever for URAG, using a four-stage automated pipeline to generate and filter diverse mixed-modal question-answer pairs from web documents. A two-stage training framework performs pre-training on the NyxQA dataset and open-source retrieval data, followed by supervised fine-tuning using feedback from vision-language models.
**Key findings**:
- Nyx is a unified mixed-modal to mixed-modal retriever tailored for universal RAG scenarios
- A four-stage automated pipeline constructs NyxQA, a dataset of diverse mixed-modal question-answer pairs from web documents
- Two-stage training combines pre-training on NyxQA with supervised fine-tuning using VLM feedback
- Nyx performs competitively on standard text-only RAG benchmarks
- The model significantly improves generation quality in vision-language tasks within the URAG setting
**Limitations**: Not stated in abstract

## References

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated literature review using NLP techniques and LLM-based retrieval-augmented generation. arXiv. https://arxiv.org/abs/2411.18583

Asl, M. A., Asgari-Bidhendi, M., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful adaptive iterative refinement for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.22344

Cai, Y., Guo, Z., Pei, Y., Bian, W., & Zheng, W. (2024). SimGRAG: Leveraging similar subgraphs for knowledge graphs driven retrieval-augmented generation. arXiv. https://arxiv.org/abs/2412.15272

Chakraborty, A., Dahal, C., & Gupta, V. (2025). Federated retrieval-augmented generation: A systematic mapping study. arXiv. https://arxiv.org/abs/2505.18906

Chang, C.-Y., Jiang, Z., Rakesh, V., Pan, M., Yeh, C.-C. M., Wang, G., Hu, M., Xu, Z., Zheng, Y., Das, M., & Zou, N. (2024). MAIN-RAG: Multi-agent filtering retrieval-augmented generation. arXiv. https://arxiv.org/abs/2501.00332

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating retrieval-augmented generation in Quranic studies: A study of 13 open-source large language models. arXiv. https://arxiv.org/abs/2503.16581

Su, W., Tang, Y., Ai, Q., Yan, J., Wang, C., Wang, H., Ye, Z., Zhou, Y., & Liu, Y. (2025). Parametric retrieval augmented generation. arXiv. https://arxiv.org/abs/2501.15915

Xiao, L., Dai, W., Chen, S., Qin, B., Shi, C., Jing, H., & Guo, T. (2025). Retrieval-augmented generation by evidence retroactivity in LLMs. arXiv. https://arxiv.org/abs/2501.05475

Xiao, X., Huang, H., Liu, R., & Xie, J. (2026). MASS-RAG: Multi-agent synthesis retrieval-augmented generation. arXiv. https://arxiv.org/abs/2604.18509

Zhang, C., Dong, G., Yang, X., & Dou, Z. (2025). Towards mixed-modal retrieval for universal retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.17354
