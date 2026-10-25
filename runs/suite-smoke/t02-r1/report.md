# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "retrieval-augmented generation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Retrieval-Augmented Generation (RAG) has emerged as a dominant paradigm for enhancing large language models with external knowledge, addressing critical challenges of hallucination, knowledge staleness, and domain-specific accuracy. The 10 surveyed papers from 2024-2026 reveal a field rapidly evolving along multiple dimensions: architectural innovations for complex reasoning tasks, security and privacy concerns, multimodal extensions, personalization strategies, and practical optimization of retrieval components. Recent work demonstrates significant progress in multi-hop query handling through iterative refinement frameworks, while novel approaches leveraging knowledge graphs, hybrid data stores, and collaborative filtering are pushing retrieval effectiveness beyond traditional vector search. However, the literature also exposes growing concerns about RAG system vulnerabilities, particularly membership inference attacks that can stealthily compromise datastore privacy. The field is maturing from basic retrieve-then-generate pipelines toward sophisticated, evidence-driven reasoning systems capable of handling complex, domain-specific tasks while maintaining faithfulness and computational efficiency.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "retrieval-augmented generation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Advanced Architectures for Complex Reasoning

The literature shows a clear trajectory from basic RAG pipelines toward sophisticated architectures designed for complex, multi-hop reasoning tasks. Traditional RAG systems struggle when queries require synthesizing information from disparate sources, often propagating noise or failing to gather comprehensive context. FAIR-RAG addresses this through an Iterative Refinement Cycle governed by Structured Evidence Assessment, which deconstructs queries into checklists and systematically identifies evidence gaps before generating responses (Aghajani Asl et al., 2025). This approach achieved state-of-the-art performance on HotpotQA with an F1-score of 0.453, demonstrating that structured, evidence-driven refinement is crucial for reliable reasoning. Similarly, TagRAG introduces a tag-guided hierarchical knowledge graph framework that enables efficient global reasoning while supporting scalable graph maintenance, achieving a 78.36% winning rate against baselines with 14.6x construction efficiency improvements over GraphRAG (Tao et al., 2025). These works collectively indicate that the field is moving beyond simple retrieve-then-generate paradigms toward agentic, reasoning-capable systems.

### Theme 2: Retrieval Optimization and Component Design

A significant thread in recent RAG research focuses on optimizing the retrieval component itself, recognizing that retrieval quality fundamentally constrains generation quality. Two papers specifically investigate document chunking strategies, examining how segmentation granularity affects system performance. Garrido-Lestache Belinchon and Garrido-Lestache Belinchon (2026) explore the trade-offs between chunk sizes ranging from individual sentences to entire chapters, finding that smaller chunks enable precise retrieval but limit contextual coherence, while larger chunks provide broader information but introduce noise and computational overhead. Kreileder et al. (2026) evaluate cluster-based semantic chunking against fixed-size and recursive strategies on academic theses, surprisingly finding that simpler approaches outperformed cluster-based methods under their tested configuration, with RAGAs faithfulness metrics showing limited reliability. Beyond chunking, HetaRAG proposes unifying heterogeneous retrieval paradigms—vector indices, knowledge graphs, full-text engines, and structured databases—into a single retrieval plane that dynamically routes and fuses evidence to maximize recall, precision, and contextual fidelity (Yan et al., 2025). These works highlight that retrieval optimization remains an open challenge with significant impact on downstream generation quality.

### Theme 3: Personalization and Collaborative Approaches

Personalization represents an emerging direction in RAG research, recognizing that different users have distinct information needs and contextual requirements. ClusterRAG introduces cluster-based collaborative filtering for personalized RAG, representing users through profile documents and organizing them into semantically coherent clusters using density-based clustering (Nkhata et al., 2026). The system performs retrieval at both cluster and document levels, leveraging collaborative signals from similar users to enhance personalized generation. Experiments on the LaMP benchmark demonstrate that jointly using the target user's profile and profiles from similar users consistently yields the best performance across diverse tasks, integrating seamlessly with different retrievers and rankers while remaining effective with both fine-tuned and zero-shot language models. This collaborative filtering approach addresses both high retrieval costs and the oversight of user similarity signals in existing personalized RAG systems, suggesting that personalization will be increasingly important as RAG systems deploy in user-facing applications.

### Theme 4: Security and Privacy Vulnerabilities

As RAG systems gain adoption, the literature reveals growing concerns about security and privacy vulnerabilities inherent in the retrieve-then-generate architecture. Naseh et al. (2025) present Interrogation Attack, a stealthy membership inference technique that crafts natural-text queries answerable only with the target document's presence in the RAG datastore. The attack achieves successful inference with just 30 queries while remaining undetectable—existing detectors identify adversarial prompts from prior methods up to 76 times more frequently than Interrogation Attack queries. The attack demonstrates a 2x improvement in true positive rate at 1% false positive rate across diverse RAG configurations while costing less than $0.02 per document inference. This work exposes a critical vulnerability: while RAG avoids weight tuning that could leak training data, the retrieved documents in the model's context create new attack surfaces for membership inference. The stealthy nature of these attacks suggests that query rewriting and straightforward detection mechanisms are insufficient defenses, pointing to an urgent need for more robust security frameworks in RAG systems.

### Theme 5: Multimodal and Domain-Specific Extensions

RAG research is expanding beyond text-only retrieval toward multimodal and domain-specific applications. Mei et al. (2025) survey Multimodal RAG (MRAG), which integrates text, images, and videos into retrieval and generation processes, overcoming limitations of text-only RAG. Their survey indicates that MRAG outperforms traditional RAG, especially in scenarios requiring both visual and textual understanding, by grounding responses in factual multimodal knowledge and reducing hallucinations. In the domain-specific arena, Khalila et al. (2025) investigate RAG for Quranic studies, evaluating 13 open-source LLMs across size categories on a dataset of Quranic surahs including meanings, historical context, and qualities. Their findings reveal that while large models consistently outperform smaller ones, well-optimized small models like Llama3.2:3b can achieve exceptional faithfulness scores (4.619) and relevance scores (4.857), demonstrating that RAG enables effective domain-specific applications even with resource-constrained architectures. These extensions highlight RAG's versatility and the importance of adapting retrieval and generation strategies to specific modalities and domains.

### Theme 6: Automation and Practical Deployment

The literature also addresses practical aspects of RAG deployment, including automation of literature review processes and system implementation considerations. Ali et al. (2024) evaluate automated literature review generation using three approaches—frequency-based methods (spaCy), transformer models (Simple T5), and RAG with GPT-3.5-turbo—finding that the LLM-based RAG approach achieved the highest ROUGE-1 score of 0.364 on the SciTLDR dataset. This work demonstrates RAG's utility not just as a research topic but as a practical tool for automating knowledge-intensive tasks. The development of partial implementations with publicly available code, such as HetaRAG's GitHub repository, indicates the field's maturation toward deployable systems rather than purely theoretical frameworks. These practical considerations—evaluation metrics, implementation availability, and automation capabilities—are increasingly important as RAG transitions from research prototypes to production systems.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that basic retrieve-then-generate pipelines are insufficient for complex tasks, with FAIR-RAG, TagRAG, and HetaRAG all proposing more sophisticated architectures incorporating iterative refinement, knowledge graphs, or hybrid retrieval. There is broad agreement that retrieval quality fundamentally constrains generation quality, motivating extensive work on chunking optimization and retrieval strategy evaluation. The literature consistently demonstrates that RAG reduces hallucinations and improves faithfulness across diverse domains, from general QA benchmarks to sensitive religious contexts.

**Disagreements**: The chunking strategy literature reveals disagreement about optimal approaches—while Garrido-Lestache Belinchon and Garrido-Lestache Belinchon (2026) suggest chunk size significantly impacts performance and requires careful evaluation, Kreileder et al. (2026) found that cluster-based semantic chunking did not outperform simpler fixed-size or recursive strategies under their tested configuration. This suggests that optimal chunking may be highly dependent on document structure, domain, and evaluation metrics, with no universally superior approach. Additionally, while most papers emphasize architectural sophistication for improved performance, the strong results from well-optimized small models in domain-specific contexts (Khalila et al., 2025) suggest that model size and optimization may sometimes matter more than architectural complexity.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, security research is nascent—while Naseh et al. (2025) demonstrate effective membership inference attacks, comprehensive defense mechanisms and broader security threat models remain underexplored. Second, evaluation metrics show limitations—RAGAs faithfulness demonstrated limited reliability in Kreileder et al.'s (2026) setup, suggesting the field lacks robust, universally applicable evaluation frameworks. Third, computational overhead and latency analysis is often absent—FAIR-RAG's iterative refinement and HetaRAG's hybrid retrieval likely incur significant costs that are not thoroughly analyzed. Fourth, most evaluations focus on English-language benchmarks, with limited exploration of multilingual RAG systems despite global deployment needs. Fifth, real-world deployment considerations—scalability to large document collections, incremental updates, and integration with existing infrastructure—receive limited attention beyond technical reports like HetaRAG. Finally, the literature lacks longitudinal studies examining how RAG systems perform as knowledge bases evolve and models age, raising questions about long-term maintenance and update strategies.

## Per-Paper Annotations

### Ali et al. (2024)

**Research question**: How can literature review generation be automated from PDF files using Natural Language Processing techniques and Large Language Models?

**Methodology**: Evaluated three distinct systems on the SciTLDR dataset: a frequency-based method (spaCy), a transformer model (Simple T5), and retrieval-augmented generation with GPT-3.5-turbo, using ROUGE scores for comparative evaluation.

**Key findings**:
- GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364, outperforming other approaches
- The transformer model (Simple T5) ranked second in performance
- The spaCy frequency-based method performed worst among the three systems
- A graphical user interface was developed for the best-performing LLM-based system

**Limitations**: Evaluation was limited to the SciTLDR dataset only; ROUGE scores indicate moderate performance with significant room for improvement in automated literature review quality.

### Naseh et al. (2025)

**Research question**: Can membership inference attacks be performed against RAG datastores stealthily without triggering detection mechanisms?

**Methodology**: Developed the Interrogation Attack (IA) that crafts natural-text queries answerable only with the target document's presence, testing across diverse RAG configurations while measuring detection rates and inference costs.

**Key findings**:
- Successful membership inference achieved with only 30 queries per document
- Existing detectors identify adversarial prompts from prior methods up to 76x more frequently than IA-generated queries
- 2x improvement in TPR@1%FPR over prior inference attacks across diverse RAG configurations
- Attack costs less than $0.02 per document inference
- Natural-text queries remain stealthy against straightforward detection mechanisms

**Limitations**: Focuses specifically on membership inference rather than broader RAG security threats; effectiveness may vary against more sophisticated query rewriting or defense mechanisms not evaluated in the study.

### Aghajani Asl et al. (2025)

**Research question**: How can RAG systems be improved to handle complex multi-hop queries that require synthesizing information from disparate sources?

**Methodology**: Introduced FAIR-RAG, an agentic framework with an Iterative Refinement Cycle governed by Structured Evidence Assessment (SEA) that deconstructs queries into checklists, audits evidence for gaps, and generates targeted sub-queries until evidence is sufficient.

**Key findings**:
- Achieved F1-score of 0.453 on HotpotQA, an absolute improvement of 8.3 points over the strongest iterative baseline
- Established new state-of-the-art for iterative RAG methods on HotpotQA benchmark
- Significantly outperformed strong baselines on 2WikiMultiHopQA and MusiQue benchmarks
- Structured evidence-driven refinement with explicit gap analysis proves crucial for reliable reasoning
- The SEA gating mechanism effectively identifies both confirmed facts and explicit informational gaps

**Limitations**: Evaluation limited to multi-hop QA benchmarks; computational overhead and latency of iterative refinement cycles not thoroughly analyzed; may not generalize to non-QA knowledge-intensive tasks.

### Khalila et al. (2025)

**Research question**: How do different LLM sizes perform with RAG in domain-specific religious contexts where response faithfulness and accuracy are critical?

**Methodology**: Evaluated 13 open-source LLMs categorized by size (large, medium, small) with RAG on a descriptive Quranic surahs dataset, using human evaluators to assess context relevance, answer faithfulness, and answer relevance.

**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate responses
- Llama3.2:3b achieved exceptional faithfulness score of 4.619 despite being a small model
- Llama3.2:3b achieved relevance score of 4.857, demonstrating promise of well-optimized smaller architectures
- RAG effectively mitigates hallucination problems across all model sizes in religious contexts
- Clear trade-offs exist between model size, computational efficiency, and response quality in domain-specific applications

**Limitations**: Study focused exclusively on Quranic studies domain with 114 surahs dataset; human evaluation metrics introduce potential subjectivity; findings may not generalize to other religious or sensitive domains.

### Mei et al. (2025)

**Research question**: What is the current state of Multimodal RAG systems that integrate text, images, and videos beyond traditional text-only RAG?

**Methodology**: Comprehensive survey reviewing MRAG's essential components, datasets, evaluation methods, and limitations, comparing MRAG against traditional RAG and identifying challenges and future research directions.

**Key findings**:
- MRAG outperforms traditional text-only RAG, especially in scenarios requiring both visual and textual understanding
- Multimodal retrieval reduces hallucinations by grounding responses in factual multimodal knowledge
- MRAG extends RAG framework to leverage contextual information from diverse data types (text, images, videos)
- Survey identifies key challenges in MRAG construction and improvement across components and evaluation
- MRAG shows potential to revolutionize multimodal information retrieval and generation paradigms

**Limitations**: As a survey paper, provides no original experimental validation; identified challenges and future directions remain speculative without empirical testing; rapid field evolution may quickly date certain findings.

### Yan et al. (2025)

**Research question**: How can heterogeneous retrieval paradigms (vector search, knowledge graphs, full-text indexes, and relational databases) be fused to overcome the trade-offs inherent in single-modality RAG systems?

**Methodology**: HetaRAG proposes a hybrid framework that unifies vector indices, knowledge graphs, full-text engines, and structured databases into a single retrieval plane, dynamically routing and fusing evidence from heterogeneous data stores to maximize recall, precision, and contextual fidelity.

**Key findings**:
- Vector search captures semantic similarity but loses global context, while knowledge graphs excel at relational precision but struggle with recall
- Full-text indexes provide fast and exact matching but are semantically blind, while relational engines offer strong transactional guarantees but no semantic understanding
- These heterogeneous retrieval paradigms are complementary and can be orchestrated synergistically to mitigate individual modality weaknesses
- The framework includes a partial implementation with code available at https://github.com/KnowledgeXLab/HetaRAG

**Limitations**: This is a technical report providing a brief overview with preliminary explorations and an initial RAG pipeline; comprehensive experimental validation and quantitative performance benchmarks are not yet presented in this report.

### Tao et al. (2025)

**Research question**: How can RAG systems overcome the limitations of fragment-level retrieval and GraphRAG's inefficiencies in information extraction, resource consumption, and adaptability to incremental updates?

**Methodology**: TagRAG introduces a tag-guided hierarchical knowledge graph framework with two components: (1) Tag Knowledge Graph Construction that extracts object tags and relationships organized into hierarchical domain tag chains, and (2) Tag-Guided Retrieval that retrieves domain-centric tag chains to localize and synthesize relevant knowledge during inference.

**Key findings**:
- TagRAG achieves an average winning rate of 78.36% against baseline methods across UltraDomain datasets
- The framework demonstrates approximately 14.6x improvement in construction efficiency compared to GraphRAG
- Retrieval efficiency is improved by approximately 1.9x compared to GraphRAG
- The design significantly adapts to smaller language models while improving retrieval granularity
- The hierarchical tag chain structure supports efficient knowledge increment and scalable graph maintenance

**Limitations**: Evaluation was conducted on UltraDomain datasets spanning Agriculture, Computer Science, Law, and cross-domain settings; performance on other domains or highly specialized technical fields may require additional validation.

### Nkhata et al. (2026)

**Research question**: Can collaborative signals from similar users enhance personalized RAG performance while reducing the high retrieval costs of existing personalized RAG approaches?

**Methodology**: ClusterRAG represents users through their profile documents, organizes users into semantically coherent clusters using density-based clustering, and performs retrieval at both cluster and document levels via cluster-level similarity and fine-grained ranking.

**Key findings**:
- Jointly leveraging the target user's profile and profiles from top similar users consistently yields the best performance across diverse tasks
- ClusterRAG integrates seamlessly with different dense retrievers and rankers without requiring architectural modifications
- The approach remains effective when paired with both fine-tuned and zero-shot language models
- Cluster-based collaborative filtering addresses both high retrieval costs and the oversight of collaborative signals in existing personalized RAG approaches
- Experiments on the LaMP benchmark demonstrate consistent performance improvements across multiple personalized generation tasks

**Limitations**: Evaluation was conducted on the LaMP benchmark; performance on other personalized RAG datasets, real-world user profiles with varying quality, and scalability to very large user bases may require additional investigation.

### Garrido-Lestache Belinchon and Garrido-Lestache Belinchon (2026)

**Research question**: How does text chunk size and the number of retrieved segments influence generation quality, retrieval effectiveness, and computational efficiency in Retrieval-Augmented Generation systems?

**Methodology**: The study compares different chunk size configurations ranging from individual sentences to entire chapters, evaluating their impact on generation quality, contextual correctness, retrieval precision, and computational cost across various RAG system configurations.

**Key findings**:
- Smaller chunks (e.g., individual sentences) enable more precise retrieval by narrowing focus but contain less information, potentially limiting response coherence
- Larger chunks (e.g., entire chapters) provide broader contextual information that may improve correctness but introduce noise and increase computational costs
- The number of chunks returned to the model must be considered alongside chunk size, as larger chunks contain more information per segment
- Chunk size is often selected without proper evaluation of its impact on generation quality, representing an under-explored component of RAG systems

**Limitations**: The abstract indicates this is an exploratory study seeking to better understand document segmentation effects; specific quantitative results and domain-specific performance variations are not detailed in the provided abstract.

### Kreileder et al. (2026)

**Research question**: Does cluster-based semantic chunking improve retrieval and answer quality compared to fixed-size and recursive chunking strategies when applied to long, structured academic texts?

**Methodology**: The researchers evaluated different chunking strategies on academic theses using the Retrieval Augmented Generation Assessment (RAGAs) framework, comparing cluster-based semantic chunking against fixed-size and recursive chunking approaches.

**Key findings**:
- RAGAs-based faithfulness metrics showed limited reliability in evaluating chunking strategies on long academic texts
- Performance varied substantially between fixed questions versus document-specific questions, likely related to document formatting and preprocessing
- Under the tested configuration, cluster-based semantic chunking did not outperform simpler fixed-size or recursive chunking strategies
- Document structure and preprocessing significantly impact chunking strategy effectiveness on academic texts

**Limitations**: The RAGAs faithfulness metric demonstrated limited reliability in this setup, and performance variations suggest that results may be highly dependent on document formatting, preprocessing choices, and specific configuration parameters tested.

## References

Aghajani Asl, M., Asgari-Bidhendi, M., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful adaptive iterative refinement for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.22344

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated literature review using NLP techniques and LLM-based retrieval-augmented generation. arXiv. https://arxiv.org/abs/2411.18583

Garrido-Lestache Belinchon, G., & Garrido-Lestache Belinchon, H. (2026). The effect of text chunk size on retrieval-augmented generation performance. arXiv. https://arxiv.org/abs/2607.24767

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating retrieval-augmented generation in Quranic studies: A study of 13 open-source large language models. arXiv. https://arxiv.org/abs/2503.16581

Kreileder, V. J. J., Reisinger, J., & Fischer, A. (2026). Evaluating chunking strategies for retrieval-augmented generation on academic texts. arXiv. https://arxiv.org/abs/2607.01852

Mei, L., Mo, S., Yang, Z., & Chen, C. (2025). A survey of multimodal retrieval-augmented generation. arXiv. https://arxiv.org/abs/2504.08748

Naseh, A., Peng, Y., Suri, A., Chaudhari, H., Oprea, A., & Houmansadr, A. (2025). Riddle me this! Stealthy membership inference for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2502.00306

Nkhata, G., Oyshi, U. A., Mai, Q., & Gauch, S. (2026). ClusterRAG: Cluster-based collaborative filtering for personalized retrieval-augmented generation. arXiv. https://arxiv.org/abs/2605.18769

Tao, W., Li, X., Lan, Y., & Qian, W. (2025). TagRAG: Tag-guided hierarchical knowledge graph retrieval-augmented generation. arXiv. https://arxiv.org/abs/2601.05254

Yan, G., Zhang, Y., Cai, P., Wang, D., Mao, S., Zhang, H., Zhang, Y., Zhang, H., Cai, X., & Shi, B. (2025). HetaRAG: Hybrid deep retrieval-augmented generation across heterogeneous data stores. arXiv. https://arxiv.org/abs/2509.21336
