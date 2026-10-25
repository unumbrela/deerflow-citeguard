# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2025-10-25
**Papers surveyed**: 3
**Scope**: arXiv search query "retrieval-augmented generation", category cs.CL, last 2 years (2024-10-25 to 2025-10-25)
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines recent advances in Retrieval-Augmented Generation (RAG) within the computational linguistics domain (cs.CL). The three surveyed papers reveal a field rapidly evolving along multiple dimensions: automation of literature review processes, enhancement of multi-hop reasoning capabilities, and domain-specific applications in sensitive contexts. Collectively, these works demonstrate that RAG systems are being adapted to increasingly complex tasks, from synthesizing information across disparate sources to maintaining faithfulness in religious text interpretation. The literature shows strong consensus that RAG mitigates hallucination in large language models, though optimal implementation strategies vary significantly by use case and domain requirements.

## Methodology

This review surveyed 3 arXiv papers retrieved on 2025-10-25 using the query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top results were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search returned only 3 papers with cs.CL as the primary category, suggesting RAG research is more commonly categorized under information retrieval (cs.IR) or artificial intelligence (cs.AI).

## Themes

### Theme 1: RAG for Domain-Specific Applications

The surveyed literature demonstrates RAG's adaptability to specialized domains requiring high accuracy and contextual faithfulness. Ali et al. (2024) applied RAG to automated literature review generation, addressing the challenge of processing ever-increasing research article volumes. Their work shows RAG can automate knowledge synthesis tasks that traditionally require human expertise. Similarly, Khalila et al. (2025) investigated RAG in Quranic studies, where response accuracy and faithfulness to authoritative sources are paramount. This application highlights RAG's potential in sensitive domains where hallucination poses significant risks. Both studies emphasize that domain-specific datasets and careful model selection are critical for success in specialized applications.

### Theme 2: Advanced Reasoning and Multi-Hop Query Handling

A significant research direction focuses on enhancing RAG's capability to handle complex queries requiring information synthesis from multiple sources. Aghajani Asl et al. (2025) introduced FAIR-RAG, which addresses the limitation of existing frameworks in handling multi-hop queries through an iterative refinement cycle with explicit evidence gap analysis. This represents a shift from simple retrieve-then-generate pipelines toward dynamic, evidence-driven reasoning processes. The framework's state-of-the-art performance on multi-hop QA benchmarks demonstrates that structured, iterative approaches can substantially improve RAG's reasoning capabilities for complex knowledge-intensive tasks.

### Theme 3: Evaluation and Performance Optimization

The literature reveals ongoing efforts to optimize RAG systems and establish rigorous evaluation methodologies. Ali et al. (2024) employed ROUGE scores to compare different NLP approaches, finding that LLM-based RAG outperformed both frequency-based and transformer-only methods. Khalila et al. (2025) used human evaluation metrics including context relevance, answer faithfulness, and answer relevance to assess 13 different model sizes. Their findings reveal important trade-offs between model size, computational efficiency, and response quality, with well-optimized smaller models showing competitive performance. This theme underscores the field's maturation toward systematic performance evaluation and optimization strategies.

## Convergences and Disagreements

**Convergences**: All surveyed papers agree that RAG effectively mitigates hallucination in large language models by grounding responses in retrieved evidence. There is consensus that domain-specific retrieval corpora improve response quality for specialized tasks. Multiple papers emphasize that model architecture and size significantly impact performance, though optimal choices depend on the specific application domain. The literature converges on the view that RAG represents a cost-effective alternative to fine-tuning for incorporating external knowledge.

**Disagreements**: The papers differ in their approach to retrieval complexity. While Aghajani Asl et al. (2025) advocate for sophisticated iterative retrieval with explicit gap analysis, Ali et al. (2024) demonstrate that simpler direct RAG with a powerful LLM can achieve strong results for certain tasks. There is also variation in evaluation approaches: some studies prioritize automated metrics like ROUGE scores, while others emphasize human evaluation for domain-specific applications, reflecting ongoing debate about appropriate evaluation methodologies for RAG systems.

## Gaps and Open Questions

The collective literature reveals several notable gaps. None of the surveyed papers explicitly discuss limitations in their abstracts, suggesting potential publication bias toward positive results. The review found limited discussion of computational costs associated with different RAG architectures, despite this being a practical concern for deployment. There is minimal exploration of hybrid approaches combining multiple retrieval strategies, even though real-world applications often require such flexibility. Additionally, the temporal dynamics of knowledge updates in RAG systems—how frequently retrieval corpora should be updated and how to handle conflicting information across versions—remain underexplored. Future research should address scalability concerns, particularly for applications requiring real-time retrieval from large, evolving knowledge bases.

## Per-Paper Annotations

### Aghajani Asl et al. (2025)

**Research question**: How can Retrieval-Augmented Generation frameworks be improved to handle complex, multi-hop queries that require synthesizing information from disparate sources?

**Methodology**: The authors introduce FAIR-RAG, an agentic framework featuring an Iterative Refinement Cycle with a Structured Evidence Assessment (SEA) module that deconstructs queries into checklists and audits evidence to identify gaps. The framework was evaluated on multi-hop QA benchmarks including HotpotQA, 2WikiMultiHopQA, and MusiQue in a unified experimental setup.

**Key findings**:
- FAIR-RAG significantly outperforms strong baselines on challenging multi-hop QA benchmarks
- On HotpotQA, FAIR-RAG achieved an F1-score of 0.453, an 8.3-point improvement over the strongest iterative baseline
- The framework establishes a new state-of-the-art for its class of methods on the evaluated benchmarks
- The Structured Evidence Assessment module successfully identifies both confirmed facts and explicit informational gaps
- The iterative refinement process with explicit gap analysis enables reliable reasoning for complex, knowledge-intensive tasks

**Limitations**: not stated in abstract

### Ali et al. (2024)

**Research question**: How can literature reviews be automatically generated from PDF files using Natural Language Processing techniques and Large Language Models?

**Methodology**: The study evaluates three distinct NLP approaches—frequency-based method (spaCy), transformer model (Simple T5), and retrieval-augmented generation with GPT-3.5-turbo—using the SciTLDR dataset. Performance was measured using ROUGE scores to compare the three systems.

**Key findings**:
- GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364 among the three evaluated systems
- The transformer model (Simple T5) performed second best in the evaluation
- The frequency-based spaCy method ranked last among the three approaches
- A graphical user interface was successfully created for the best-performing LLM-based system

**Limitations**: not stated in abstract

### Khalila et al. (2025)

**Research question**: How do different open-source Large Language Models perform when applying Retrieval-Augmented Generation to Quranic studies, and what are the trade-offs between model size and response quality?

**Methodology**: The study investigates 13 open-source LLMs categorized by size (large, medium, small) using a Retrieval-Augmented Generation approach with a descriptive dataset of Quranic surahs. Models were evaluated by human evaluators on three metrics: context relevance, answer faithfulness, and answer relevance.

**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate, contextually grounded responses
- Llama3.2:3b, despite being a small model, achieved strong scores in faithfulness (4.619) and relevance (4.857)
- RAG helps mitigate hallucination issues that general-purpose LLMs face in religious contexts
- Well-optimized smaller architectures show promise for domain-specific applications
- There are notable trade-offs between model size, computational efficiency, and response quality

**Limitations**: not stated in abstract

## References

Aghajani Asl, M., Asgari-Bidhendi, M., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful adaptive iterative refinement for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.22344

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated literature review using NLP techniques and LLM-based retrieval-augmented generation. arXiv. https://arxiv.org/abs/2411.18583

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating retrieval-augmented generation in Quranic studies: A study of 13 open-source large language models. arXiv. https://arxiv.org/abs/2503.16581
