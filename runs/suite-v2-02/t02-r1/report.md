# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2026-10-25  
**Papers surveyed**: 10  
**Scope**: arXiv search query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25  
**Citation format**: APA 7th edition

## Executive Summary

Retrieval-Augmented Generation (RAG) has evolved significantly in the past two years, with research expanding beyond basic retrieval-and-generation pipelines to address fundamental challenges in evidence quality, reasoning paradigms, and architectural innovation. The surveyed literature reveals a field maturing through diversification: researchers are tackling multi-hop query complexity through iterative refinement cycles, exploring parametric knowledge integration as an alternative to in-context retrieval, and extending RAG to mixed-modal and domain-specific applications. A prominent trend is the emergence of multi-agent architectures that distribute evidence processing across specialized agents, alongside novel reasoning paradigms that enable retroactive evidence revision. Despite these advances, common limitations persist around evaluation rigor, privacy-preserving retrieval in federated settings, and the challenge of aligning retrieved structures with query semantics—particularly in knowledge graph-driven approaches.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Agent Architectures for Evidence Processing

A significant trend in recent RAG research is the decomposition of evidence processing across multiple specialized agents. Rather than relying on a single monolithic pipeline, these systems distribute tasks such as filtering, summarization, extraction, and reasoning across distinct agents that collaborate to produce final answers. Chang et al. (2024) introduced MAIN-RAG, which uses multiple LLM agents to collaboratively filter and score retrieved documents with adaptive thresholding, achieving 2-11% accuracy improvements across QA benchmarks. Similarly, Xiao et al. (2026) proposed MASS-RAG, which structures evidence processing into role-specialized agents for summarization, extraction, and reasoning, with a dedicated synthesis stage that enables comparison and integration of complementary information. These approaches address the fundamental challenge of noisy or incomplete retrieved contexts by leveraging inter-agent consensus and structured evidence reconciliation. The convergence on multi-agent designs suggests that complex RAG tasks benefit from explicit decomposition of cognitive labor, mirroring successful patterns in broader agent-based systems research.

### Theme 2: Iterative and Retroactive Reasoning Paradigms

Traditional RAG systems follow a forward reasoning paradigm: retrieve documents, then generate answers. Recent work challenges this unidirectional flow by introducing iterative refinement and retroactive reasoning capabilities. Aghajani Asl et al. (2025) developed FAIR-RAG, which implements an Iterative Refinement Cycle with Structured Evidence Assessment (SEA) that deconstructs complex queries into checklists, audits evidence for gaps, and generates targeted sub-queries until sufficient evidence is gathered. This approach achieved an F1-score of 0.453 on HotpotQA, an 8.3-point improvement over the strongest iterative baseline. More radically, Xiao et al. (2025) introduced RetroRAG, which builds a retroactive reasoning paradigm using an evidence-collation-discovery framework that searches, generates, and refines credible evidence. The system synthesizes inferential evidence from existing source knowledge, formulates search queries, and iteratively updates evidence until a reliable answer is obtained. These approaches recognize that complex multi-hop queries cannot be satisfied by single-pass retrieval and require dynamic evidence accumulation with explicit gap detection.

### Theme 3: Parametric and Structural Knowledge Integration

Beyond in-context document injection, researchers are exploring deeper integration of external knowledge into model parameters and structured representations. Su et al. (2025) proposed Parametric RAG, which integrates external knowledge directly into the parameters of feed-forward networks through document parameterization rather than appending documents to input context. This eliminates the computational cost of injecting multiple documents during inference and enables deeper integration into the LLM's parametric knowledge space. In parallel, knowledge graph-driven approaches address the challenge of aligning query texts with structured knowledge. Cai et al. (2024) introduced SimGRAG, which uses a two-stage process: query-to-pattern transforms queries into graph patterns using an LLM, and pattern-to-subgraph quantifies alignment using a graph semantic distance metric. Their optimized retrieval algorithm identifies top-k subgraphs within 1 second on a 10-million-scale knowledge graph. These approaches represent complementary strategies: parametric integration for efficiency and structural alignment for semantic precision.

### Theme 4: Domain-Specific and Mixed-Modal Extensions

RAG research is expanding beyond general-purpose text QA to address domain-specific requirements and mixed-modal information needs. Khalila et al. (2025) investigated RAG applications in Quranic studies, evaluating 13 open-source LLMs on context relevance, answer faithfulness, and relevance metrics. Their work demonstrates that RAG effectively mitigates hallucination issues in domain-specific religious contexts, with large models consistently outperforming smaller ones, though some small models like Llama3.2:3b achieved strong faithfulness scores. Extending RAG beyond unimodal text, Zhang et al. (2025) proposed Nyx, a unified mixed-modal to mixed-modal retriever for Universal RAG scenarios involving both text and images. They created the NyxQA dataset through a four-stage automated pipeline and trained Nyx using pre-training on diverse datasets followed by supervised fine-tuning with vision-language model feedback. Nyx performs competitively on standard text-only RAG benchmarks while significantly improving generation quality in vision-language tasks. These domain-specific and mixed-modal extensions demonstrate RAG's adaptability to diverse information structures and user needs.

### Theme 5: Privacy-Preserving and Federated RAG

As RAG systems encounter privacy-sensitive applications, researchers are exploring federated learning paradigms that enable knowledge-intensive NLP without centralized data aggregation. Chakraborty et al. (2025) conducted the first systematic mapping study of Federated RAG covering 2020-2025 literature, following Kitchenham's guidelines for evidence-based software engineering. Their analysis identifies key challenges including privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations. Federated RAG offers a promising framework for secure, knowledge-intensive NLP in privacy-sensitive domains, but requires novel approaches to retrieval that respect data locality constraints. The study identifies recurring design patterns and synthesizes the rapidly evolving research body, providing a foundation for future work at the intersection of RAG and federated systems. This emerging direction addresses critical deployment barriers in healthcare, finance, and other regulated domains where data cannot be centrally aggregated.

### Theme 6: Automation and Meta-Analysis of Literature Review

Ironically, RAG technology is being applied to automate the literature review process itself. Ali et al. (2024) implemented and compared three systems for auto-generating literature reviews from PDF research articles: a frequency-based approach using spaCy, a transformer model using Simple T5, and retrieval-augmented generation using GPT-3.5-turbo. Evaluated on the SciTLDR dataset using ROUGE scores, the GPT-3.5-turbo approach achieved the highest ROUGE-1 score of 0.364. This meta-application demonstrates RAG's utility in research workflows while providing empirical validation of RAG's effectiveness for summarization tasks. The work also highlights the progressive improvement from frequency-based to transformer-based to LLM-based approaches, mirroring broader trends in NLP capability evolution.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. First, all multi-agent approaches converge on the principle that distributing evidence processing across specialized agents improves accuracy and consistency compared to monolithic pipelines (Chang et al., 2024; Xiao et al., 2026). Second, iterative refinement is consistently shown to outperform single-pass retrieval for complex queries, with multiple papers demonstrating substantial gains on multi-hop QA benchmarks (Aghajani Asl et al., 2025; Xiao et al., 2025). Third, domain-specific applications benefit from RAG's ability to ground responses in authoritative sources, reducing hallucination across diverse contexts from religious texts to mixed-modal queries (Khalila et al., 2025; Zhang et al., 2025). Fourth, structural alignment between queries and retrieved knowledge—whether through knowledge graphs or parametric integration—improves both efficiency and accuracy (Su et al., 2025; Cai et al., 2024).

**Disagreements**: The literature reveals tension between parametric and in-context knowledge integration strategies. Su et al. (2025) argue that parametric integration eliminates online computational costs and enables deeper knowledge fusion, while the multi-agent and iterative approaches implicitly assume in-context retrieval remains necessary for flexibility and traceability. Additionally, there is implicit disagreement about the role of model size: Khalila et al. (2025) found large models consistently outperform smaller ones, yet noted that Llama3.2:3b (a small model) achieved strong faithfulness and relevance scores, suggesting that RAG may partially compensate for model capacity limitations—a question requiring further investigation.

## Gaps and Open Questions

Several critical gaps emerge across the surveyed literature:

1. **Evaluation limitations**: None of the surveyed papers explicitly state limitations in their abstracts, which itself suggests a gap in critical self-assessment. Chakraborty et al. (2025) identify evaluation limitations as a key challenge in Federated RAG, but this concern likely extends to centralized RAG systems as well.

2. **Privacy-preserving retrieval**: While federated RAG addresses data locality, the specific challenge of privacy-preserving retrieval mechanisms remains underexplored. How can relevance scoring and document selection occur without exposing query or document contents?

3. **Cross-client heterogeneity**: In federated settings, the heterogeneity of client data distributions and retrieval indices poses unresolved challenges for consistent RAG performance (Chakraborty et al., 2025).

4. **Efficiency-accuracy trade-offs**: Parametric RAG claims efficiency gains (Su et al., 2025), but comprehensive comparisons of computational costs across different RAG paradigms (multi-agent, iterative, parametric, structural) are lacking.

5. **Scalability of multi-agent approaches**: While multi-agent systems show accuracy improvements, the computational overhead of coordinating multiple agents and the scalability to large document corpora remain unaddressed.

6. **Mixed-modal retrieval generalization**: Nyx demonstrates strong performance on mixed-modal tasks (Zhang et al., 2025), but whether the approach generalizes to other modalities (audio, video, 3D structures) is unknown.

7. **Knowledge graph alignment at scale**: SimGRAG achieves sub-second retrieval on 10-million-scale graphs (Cai et al., 2024), but real-world knowledge graphs often exceed this scale by orders of magnitude, requiring further optimization.

## Per-Paper Annotations

### Aghajani Asl et al. (2025)

**Research question**: How can retrieval-augmented generation systems be improved to handle complex multi-hop queries that require synthesizing information from disparate sources?  
**Methodology**: The authors introduce FAIR-RAG, an agentic framework featuring an Iterative Refinement Cycle with Structured Evidence Assessment (SEA) that deconstructs queries into checklists, audits evidence for gaps, and generates targeted sub-queries until sufficient evidence is gathered. Experiments were conducted on HotpotQA, 2WikiMultiHopQA, and MusiQue benchmarks.  
**Key findings**:
- FAIR-RAG achieved an F1-score of 0.453 on HotpotQA, an 8.3-point improvement over the strongest iterative baseline
- The framework establishes a new state-of-the-art for iterative RAG methods on multi-hop QA benchmarks
- Structured Evidence Assessment effectively identifies both confirmed facts and explicit informational gaps
- The iterative refinement cycle ensures comprehensive context before final generation  
**Limitations**: not stated in abstract

### Ali et al. (2024)

**Research question**: How can literature reviews be automatically generated from PDF research articles using Natural Language Processing techniques?  
**Methodology**: The research implements and compares three systems for auto-generating literature reviews: a frequency-based approach using spaCy, a transformer model using Simple T5, and retrieval-augmented generation using GPT-3.5-turbo. All systems are evaluated on the SciTLDR dataset using ROUGE scores.  
**Key findings**:
- GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364 among all three approaches
- The transformer model (Simple T5) performed second best in the evaluation
- The frequency-based spaCy approach ranked last in performance
- A graphical user interface was developed for the best-performing LLM-based system  
**Limitations**: not stated in abstract

### Cai et al. (2024)

**Research question**: How can knowledge graphs be effectively leveraged in RAG systems to align query texts with KG structures?  
**Methodology**: The paper proposes SimGRAG, which uses a two-stage process: query-to-pattern transforms queries into graph patterns using an LLM, and pattern-to-subgraph quantifies alignment using a graph semantic distance metric. An optimized retrieval algorithm identifies top-k subgraphs efficiently on large-scale knowledge graphs.  
**Key findings**:
- SimGRAG effectively addresses the challenge of aligning query texts and KG structures through a two-stage process
- The graph semantic distance metric quantifies alignment between query patterns and candidate subgraphs
- The optimized retrieval algorithm identifies top-k subgraphs within 1 second on a 10-million-scale knowledge graph
- SimGRAG outperforms state-of-the-art KG-driven RAG methods in question answering and fact verification tasks  
**Limitations**: not stated in abstract

### Chakraborty et al. (2025)

**Research question**: What is the current state of research at the intersection of Federated Learning and Retrieval-Augmented Generation, and what are the key patterns, challenges, and open questions in this emerging field?  
**Methodology**: This systematic mapping study follows Kitchenham's guidelines for evidence-based software engineering, analyzing Federated RAG literature published between 2020 and 2025. The research develops a structured classification of research focuses, contribution types, and application domains while analyzing architectural patterns and temporal trends.  
**Key findings**:
- This is the first systematic mapping study of Federated RAG covering 2020-2025 literature
- Federated RAG offers a promising framework for secure, knowledge-intensive NLP in privacy-sensitive domains
- Key challenges include privacy-preserving retrieval, cross-client heterogeneity, and evaluation limitations
- The study identifies recurring design patterns and synthesizes the rapidly evolving research body
- The work provides a foundation for future research at the intersection of RAG and federated systems  
**Limitations**: not stated in abstract

### Chang et al. (2024)

**Research question**: How can RAG systems improve the quality of retrieved documents to reduce noise and enhance response reliability?  
**Methodology**: The paper proposes MAIN-RAG, a training-free RAG framework that uses multiple LLM agents to collaboratively filter and score retrieved documents. It introduces an adaptive filtering mechanism that dynamically adjusts relevance thresholds based on score distributions and leverages inter-agent consensus for robust document selection.  
**Key findings**:
- MAIN-RAG achieves a 2-11% improvement in answer accuracy over traditional RAG approaches across four QA benchmarks
- The adaptive filtering mechanism effectively minimizes noise while maintaining high recall of relevant documents
- The approach reduces the number of irrelevant retrieved documents, lowering computational overhead
- MAIN-RAG achieves superior response consistency and answer accuracy compared to baseline methods without requiring additional training data  
**Limitations**: not stated in abstract

### Khalila et al. (2025)

**Research question**: How do different open-source large language models perform when applied to Quranic studies using retrieval-augmented generation to ensure accurate and contextually faithful responses?  
**Methodology**: The study investigates 13 open-source LLMs categorized by size (large, medium, small) using a RAG framework with a descriptive dataset of Quranic surahs. Models are evaluated by human evaluators on context relevance, answer faithfulness, and answer relevance metrics.  
**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate responses
- Llama3.2:3b, despite being a small model, achieved strong faithfulness (4.619) and relevance (4.857) scores
- RAG effectively mitigates hallucination issues when applying LLMs to domain-specific religious contexts
- There are trade-offs between model size, computational efficiency, and response quality  
**Limitations**: not stated in abstract

### Su et al. (2025)

**Research question**: How can external knowledge be more effectively integrated into large language models beyond the limitations of in-context knowledge injection in traditional RAG approaches?  
**Methodology**: The authors propose Parametric RAG, a new paradigm that integrates external knowledge directly into the parameters of feed-forward networks of LLMs through document parameterization, rather than appending documents to the input context. The approach is experimentally evaluated for effectiveness and efficiency.  
**Key findings**:
- Parametric RAG substantially enhances both effectiveness and efficiency of knowledge augmentation in LLMs
- The approach eliminates the need to inject multiple documents into the input context, reducing online computational costs
- External knowledge is more deeply integrated into the parametric knowledge space of the LLM
- Parametric RAG can be combined with in-context RAG methods to achieve even better performance
- All code, data, and models have been open-sourced  
**Limitations**: not stated in abstract

### Xiao et al. (2025)

**Research question**: How can retrieval-augmented generation systems address the problem of irreversible errors in forward reasoning paradigms?  
**Methodology**: The paper introduces RetroRAG, a framework that builds a retroactive reasoning paradigm using an evidence-collation-discovery framework to search, generate, and refine credible evidence. The system synthesizes inferential evidence from existing source knowledge, formulates search queries, and iteratively updates evidence until a reliable answer is obtained.  
**Key findings**:
- RetroRAG introduces a novel retroactive reasoning paradigm that revises and updates evidence to redirect reasoning chains
- The framework constructs an evidence-collation-discovery system that synthesizes inferential evidence related to key entities
- RetroRAG continually updates and organizes new evidence as it is found, enhancing its ability to locate further necessary information
- Empirical evaluations demonstrate that RetroRAG significantly outperforms existing methods  
**Limitations**: not stated in abstract

### Xiao et al. (2026)

**Research question**: How can multi-agent architectures improve evidence reconciliation in RAG systems when retrieved contexts are noisy or incomplete?  
**Methodology**: The paper proposes MASS-RAG, which structures evidence processing into multiple role-specialized agents for summarization, extraction, and reasoning over retrieved documents, with outputs combined through a dedicated synthesis stage to produce the final answer.  
**Key findings**:
- MASS-RAG applies distinct agents for evidence summarization, extraction, and reasoning over retrieved documents
- The synthesis stage combines intermediate evidence views, allowing comparison and integration of complementary information before answer generation
- MASS-RAG consistently improves performance over strong RAG baselines on four benchmarks
- The approach is particularly effective when relevant evidence is distributed across retrieved contexts  
**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: How can RAG systems be extended to handle mixed-modal queries and documents beyond unimodal text?  
**Methodology**: The paper proposes Nyx, a unified mixed-modal to mixed-modal retriever for Universal RAG. The authors created NyxQA, a dataset of diverse mixed-modal question-answer pairs using a four-stage automated pipeline, and trained Nyx using a two-stage framework: pre-training on NyxQA and open-source datasets, followed by supervised fine-tuning with feedback from vision-language models.  
**Key findings**:
- Nyx is a unified mixed-modal retriever tailored for universal RAG scenarios involving both text and images
- The NyxQA dataset provides diverse mixed-modal question-answer pairs that better reflect real-world information needs
- Nyx performs competitively on standard text-only RAG benchmarks
- Nyx significantly improves generation quality in vision-language tasks in the universal RAG setting  
**Limitations**: not stated in abstract

## References

Aghajani Asl, M., Asgari-Bidhendi, M., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful adaptive iterative refinement for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.22344

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated literature review using NLP techniques and LLM-based retrieval-augmented generation. arXiv. https://arxiv.org/abs/2411.18583

Cai, Y., Guo, Z., Pei, Y., Bian, W., & Zheng, W. (2024). SimGRAG: Leveraging similar subgraphs for knowledge graphs driven retrieval-augmented generation. arXiv. https://arxiv.org/abs/2412.15272

Chakraborty, A., Dahal, C., & Gupta, V. (2025). Federated retrieval-augmented generation: A systematic mapping study. arXiv. https://arxiv.org/abs/2505.18906

Chang, C.-Y., Jiang, Z., Rakesh, V., Pan, M., Yeh, C.-C. M., Wang, G., Hu, M., Xu, Z., Zheng, Y., Das, M., & Zou, N. (2024). MAIN-RAG: Multi-agent filtering retrieval-augmented generation. arXiv. https://arxiv.org/abs/2501.00332

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating retrieval-augmented generation in Quranic studies: A study of 13 open-source large language models. arXiv. https://arxiv.org/abs/2503.16581

Su, W., Tang, Y., Ai, Q., Yan, J., Wang, C., Wang, H., Ye, Z., Zhou, Y., & Liu, Y. (2025). Parametric retrieval augmented generation. arXiv. https://arxiv.org/abs/2501.15915

Xiao, L., Dai, W., Chen, S., Qin, B., Shi, C., Jing, H., & Guo, T. (2025). Retrieval-augmented generation by evidence retroactivity in LLMs. arXiv. https://arxiv.org/abs/2501.05475

Xiao, X., Huang, H., Liu, R., & Xie, J. (2026). MASS-RAG: Multi-agent synthesis retrieval-augmented generation. arXiv. https://arxiv.org/abs/2604.18509

Zhang, C., Dong, G., Yang, X., & Dou, Z. (2025). Towards mixed-modal retrieval for universal retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.17354
