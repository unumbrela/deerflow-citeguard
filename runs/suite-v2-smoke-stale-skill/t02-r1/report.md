# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: "retrieval augmented generation" query, cs.CL category, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Retrieval-Augmented Generation (RAG) has emerged as a critical paradigm for enhancing large language models with external knowledge, addressing fundamental challenges including hallucinations, knowledge staleness, and domain adaptation. The 10 papers surveyed reveal a field rapidly evolving along multiple dimensions: architectural innovations introducing iterative refinement cycles and graph-based reasoning, parametric integration of knowledge directly into model weights, and practical deployments in specialized domains from religious studies to IT operations. Collectively, these works demonstrate that RAG is maturing beyond simple retrieve-then-generate pipelines toward sophisticated agentic systems capable of multi-hop reasoning, while simultaneously confronting emerging security vulnerabilities and optimization challenges in real-world deployments.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "retrieval augmented generation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Architectural Innovations for Complex Reasoning

A dominant research direction involves transforming RAG from a static retrieve-then-generate pipeline into a dynamic, iterative reasoning process. FAIR-RAG introduces an agentic framework with a Structured Evidence Assessment module that deconstructs queries into checklists, audits evidence for gaps, and iteratively refines retrieval until sufficient context is gathered (Aghajani Asl et al., 2025). This approach achieved state-of-the-art performance on multi-hop QA benchmarks with an F1-score of 0.453 on HotpotQA, representing an 8.3-point improvement over prior iterative baselines. Similarly, LoRAG incorporates a dynamic loop mechanism enabling iterative refinement of generated text through interactions with retrieved context, demonstrating improvements in BLEU, ROUGE, and perplexity metrics (Thakur & Vashisth, 2024).

Graph-based approaches represent another architectural innovation, with GFM-RAG introducing a graph foundation model that captures complex relationships between knowledge pieces using an 8M-parameter graph neural network trained on 60 knowledge graphs containing over 14M triples (Luo et al., 2025). This approach enables retrieval from unseen datasets without fine-tuning, achieving state-of-the-art performance across three multi-hop QA datasets and seven domain-specific RAG benchmarks. These works collectively establish that sophisticated architectural designs—iterative cycles, graph reasoning, and evidence-driven refinement—are essential for handling complex, knowledge-intensive tasks that require synthesizing information from disparate sources.

### Theme 2: Parametric vs. In-Context Knowledge Integration

A fundamental tension in RAG research concerns how external knowledge should be integrated into language models. Traditional RAG approaches inject retrieved documents into the input context, but this faces limitations in context length, computational overhead, and performance degradation in complex reasoning scenarios. Parametric RAG proposes a paradigm shift by integrating external knowledge directly into the feed-forward network parameters of an LLM through document parameterization (Su et al., 2025). This approach eliminates the need for in-context document injection, reducing online computational costs while deepening integration of external knowledge into the model's parametric knowledge space.

The contrast between parametric and in-context approaches reveals complementary strengths: parametric methods offer efficiency and deeper knowledge integration, while in-context methods provide flexibility and transparency. Notably, Su et al. (2025) demonstrate that parametric RAG can be combined with traditional in-context RAG to achieve even better performance, suggesting hybrid approaches may represent the optimal path forward. This theme reflects a broader recognition that the simple retrieve-append-generate model is insufficient for many applications, requiring more nuanced integration strategies.

### Theme 3: Bridging the Retriever-Generator Semantic Gap

A critical challenge in RAG systems is the semantic gap between retrievers and generators, arising from differences in their training objectives and architectures. R²AG addresses this misalignment by incorporating retrieval information into the generation process through a R²-Former that captures nuanced features from retrievers, combined with a retrieval-aware prompting strategy (Ye et al., 2024). This approach is particularly effective in low-resource scenarios where both LLMs and retrievers are frozen, as retrieval information serves as an anchor to aid LLMs in distinguishing and utilizing retrieved documents effectively.

The semantic gap problem manifests across multiple papers in this review. GFM-RAG addresses it through graph structures that explicitly model query-knowledge relationships (Luo et al., 2025), while FAIR-RAG uses structured evidence assessment to ensure retrieved context aligns with query requirements (Aghajani Asl et al., 2025). These convergent solutions—graph reasoning, retrieval-aware prompting, and evidence-driven refinement—all aim to ensure that retrieved information is not merely appended but meaningfully integrated into the generation process, reducing the burden on LLMs to passively accept and distinguish retrieved documents using only inherent knowledge.

### Theme 4: Domain-Specific Applications and Practical Deployments

RAG is being actively deployed in specialized domains where accuracy, faithfulness, and domain knowledge are critical. In Quranic studies, a domain requiring exceptional faithfulness to authoritative sources, RAG systems were evaluated across 13 open-source LLMs of varying sizes, revealing that large models consistently outperform smaller ones in capturing query semantics, though well-optimized small models like Llama3.2:3b achieved surprisingly high faithfulness (4.619) and relevance (4.857) scores (Khalila et al., 2025). This work highlights the trade-offs between model size, computational efficiency, and response quality in sensitive, domain-specific applications.

In enterprise IT support and AIOps, RAG addresses domain coverage and model size constraints by enabling smaller models to perform effectively without requiring large proprietary models like GPT-4 (Toro Isaza et al., 2024). A multi-component system combining RAG for answer generation, encoder-only models for classification, and generative LLMs for query generation demonstrates practical deployment considerations including architecture design, data annotation, and deployment planning. Similarly, automated literature review generation using RAG with GPT-3.5-turbo achieved the highest ROUGE-1 score (0.364) compared to frequency-based and transformer-only approaches, demonstrating RAG's utility in academic automation contexts (Ali et al., 2024). These applications collectively validate RAG as a practical solution for domain-specific challenges where general-purpose LLMs struggle with hallucinations and knowledge gaps.

### Theme 5: Security Vulnerabilities in RAG Systems

As RAG systems proliferate, security concerns are emerging as a critical research area. A stealthy membership inference attack called Interrogation Attack (IA) demonstrates that RAG systems are vulnerable to adversaries who can determine whether specific documents exist in the retrieval datastore using only natural-text queries (Naseh et al., 2025). The attack crafts queries answerable only with the target document's presence, achieving successful inference with just 30 queries while remaining undetectable—existing detectors identify adversarial prompts from prior methods up to 76 times more frequently than IA-generated queries.

The attack achieves a 2x improvement in TPR@1%FPR over prior inference attacks across diverse RAG configurations while costing less than $0.02 per document inference. This work reveals a fundamental vulnerability in RAG architectures: while the absence of weight tuning prevents leakage via model parameters, the retrieved documents in the model's context create a new attack surface. The stealthy nature of IA—using natural queries that evade detection—poses significant privacy and security risks for RAG deployments handling sensitive information, highlighting the urgent need for robust defense mechanisms.

### Theme 6: Optimization Strategies and Evaluation Challenges

Practical RAG deployment requires careful optimization of component choices, particularly in document chunking strategies. An evaluation of chunking approaches on academic theses found that cluster-based semantic chunking did not outperform simpler fixed-size or recursive chunking strategies under tested configurations (Kreileder et al., 2026). Performance varied substantially between fixed questions and document-specific questions, with document formatting and preprocessing significantly impacting retrieval and generation quality. Notably, the RAGAs faithfulness metric showed limited reliability in this evaluation setup, raising questions about evaluation methodology in RAG research.

The optimization theme extends beyond chunking to include iterative refinement loops, which improve generation quality but introduce computational overhead and latency concerns (Thakur & Vashisth, 2024). Similarly, FAIR-RAG's iterative refinement cycle achieves superior accuracy but lacks thorough analysis of computational costs (Aghajani Asl et al., 2025). These findings reveal a tension between architectural sophistication and practical deployment constraints, where improvements in accuracy must be balanced against efficiency, latency, and evaluation reliability.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the conclusion that simple retrieve-then-generate pipelines are insufficient for complex tasks. FAIR-RAG, LoRAG, GFM-RAG, and R²AG all demonstrate that iterative, structured, or graph-enhanced approaches outperform baseline RAG on challenging benchmarks (Aghajani Asl et al., 2025; Thakur & Vashisth, 2024; Luo et al., 2025; Ye et al., 2024). There is also broad agreement that domain-specific applications benefit from RAG's ability to ground responses in authoritative sources, as evidenced by successful deployments in Quranic studies, IT support, and literature review automation (Khalila et al., 2025; Toro Isaza et al., 2024; Ali et al., 2024).

**Disagreements**: While most papers advocate for architectural complexity, there is implicit disagreement about the optimal balance between sophistication and simplicity. Kreileder et al. (2026) found that cluster-based semantic chunking—a more sophisticated approach—did not outperform simpler strategies, suggesting that complexity does not always yield benefits. Similarly, the contrast between parametric RAG (Su et al., 2025), which integrates knowledge into model parameters, and iterative approaches like FAIR-RAG (Aghajani Asl et al., 2025), which add retrieval cycles, reflects different philosophies about whether RAG should modify models or augment them externally.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, evaluation methodology remains inconsistent: RAGAs faithfulness showed limited reliability in academic text evaluation (Kreileder et al., 2026), and several papers acknowledge that computational overhead and latency of iterative approaches were not thoroughly analyzed (Aghajani Asl et al., 2025; Thakur & Vashisth, 2024). Second, security research is nascent—only one paper addresses membership inference attacks (Naseh et al., 2025), leaving open questions about other vulnerability classes, defense mechanisms, and real-world attack scenarios.

Third, domain generalization remains underexplored: while domain-specific applications demonstrate RAG's utility, most evaluations focus on single domains (Quranic studies, IT support, academic theses), limiting understanding of cross-domain transferability. Fourth, the parametric vs. in-context debate requires further investigation, particularly regarding scalability of parametric approaches to large corpora and feasibility of parameter modification in deployment scenarios where models are frozen (Su et al., 2025). Finally, practical deployment considerations—including cost, latency, maintenance, and integration with existing systems—receive limited attention despite their critical importance for real-world adoption.

## Per-Paper Annotations

### Aghajani Asl et al. (2025)

**Research question**: How can RAG systems better handle complex multi-hop queries that require synthesizing information from disparate sources?
**Methodology**: Introduced FAIR-RAG, an agentic framework with an Iterative Refinement Cycle governed by a Structured Evidence Assessment (SEA) module that deconstructs queries into checklists, audits evidence for gaps, and generates targeted sub-queries until evidence is sufficient.
**Key findings**:
- Achieved F1-score of 0.453 on HotpotQA, an absolute improvement of 8.3 points over the strongest iterative baseline
- Established new state-of-the-art performance on HotpotQA, 2WikiMultiHopQA, and MusiQue benchmarks
- Structured evidence-driven refinement with explicit gap analysis proved crucial for reliable reasoning
- The SEA module effectively identifies both confirmed facts and explicit informational gaps
**Limitations**: Evaluated only on multi-hop QA benchmarks; computational overhead and latency of the iterative refinement cycle not thoroughly analyzed.

### Ali et al. (2024)

**Research question**: How can literature reviews be automatically generated from PDF files using NLP techniques and retrieval-augmented generation?
**Methodology**: Compared three approaches for automated literature review generation: frequency-based method (spaCy), transformer model (Simple T5), and RAG with LLM (GPT-3.5-turbo), evaluated on the SciTLDR dataset using ROUGE scores.
**Key findings**:
- GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364 among all three systems
- The transformer model (Simple T5) ranked second in performance
- The frequency-based spaCy approach performed worst among the three methods
- A graphical user interface was created for the best-performing LLM-based system
**Limitations**: Evaluation was limited to the SciTLDR dataset only; ROUGE scores may not fully capture the quality and coherence of generated literature reviews.

### Khalila et al. (2025)

**Research question**: How do different sized open-source LLMs perform in RAG systems for domain-specific, sensitive tasks like Quranic studies?
**Methodology**: Investigated 13 open-source LLMs categorized by size (large, medium, small) with RAG on a descriptive Quranic dataset; evaluated using human-assessed metrics for context relevance, answer faithfulness, and answer relevance.
**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate responses
- Llama3.2:3b (small model) performed surprisingly well with faithfulness score of 4.619 and relevance score of 4.857
- Clear trade-offs identified between model size, computational efficiency, and response quality
- Well-optimized smaller architectures show promise for domain-specific applications
**Limitations**: Study limited to Quranic studies domain; human evaluation metrics introduce potential subjectivity; results may not generalize to other domains.

### Kreileder et al. (2026)

**Research question**: Does cluster-based semantic chunking improve retrieval and answer quality compared to fixed-size and recursive chunking in RAG systems for academic texts?
**Methodology**: Evaluated different chunking strategies (cluster-based semantic, fixed-size, recursive) on long, structured academic theses using the RAGAs (Retrieval Augmented Generation Assessment) framework.
**Key findings**:
- RAGAs-based faithfulness metric shows limited reliability when evaluating RAG systems on academic thesis documents
- Performance varied substantially between fixed questions versus document-specific questions
- Document formatting and preprocessing significantly impacted retrieval and generation quality
- Cluster-based semantic chunking did not outperform simpler fixed-size or recursive chunking strategies under the tested configuration
**Limitations**: Evaluation limited to academic theses; RAGAs faithfulness metric reliability concerns; results may be configuration-dependent and not generalize to other document types.

### Luo et al. (2025)

**Research question**: How can graph structures improve RAG systems' ability to capture complex relationships between knowledge pieces for intricate reasoning?
**Methodology**: Introduced GFM-RAG, a graph foundation model powered by an innovative graph neural network (8M parameters) with two-stage training on 60 knowledge graphs (14M+ triples) and 700k documents, enabling application to unseen datasets without fine-tuning.
**Key findings**:
- First graph foundation model applicable to unseen datasets for retrieval without any fine-tuning required
- Achieves state-of-the-art performance on three multi-hop QA datasets and seven domain-specific RAG datasets
- Maintains efficiency while aligning with neural scaling laws
- Demonstrates impressive generalizability across diverse datasets and domains
**Limitations**: Graph construction overhead and scalability for very large knowledge bases not fully addressed; 8M parameter model may still face resource constraints in some deployment scenarios.

### Naseh et al. (2025)

**Research question**: Can membership inference attacks be performed stealthily on RAG systems without triggering detection mechanisms?
**Methodology**: Developed the Interrogation Attack (IA) that crafts natural-text queries answerable only with the target document's presence, tested across diverse RAG configurations to measure inference success and detectability.
**Key findings**:
- Successful membership inference achieved with only 30 queries per document
- Existing detectors identify adversarial prompts from prior methods up to 76x more frequently than IA-generated queries
- 2x improvement in TPR@1%FPR over prior inference attacks across diverse RAG configurations
- Attack costs less than $0.02 per document inference
**Limitations**: Evaluated on specific RAG configurations; effectiveness against advanced query rewriting or other defense mechanisms not fully explored.

### Su et al. (2025)

**Research question**: Can external knowledge be integrated directly into LLM parameters rather than through in-context injection to overcome context length and performance limitations?
**Methodology**: Introduced Parametric RAG that integrates external knowledge directly into the parameters of feed-forward networks (FFN) of an LLM through document parameterization, eliminating the need for in-context document injection.
**Key findings**:
- Parametric RAG saves online computational costs by eliminating the need to inject multiple documents into the LLM input context
- Deeper integration of external knowledge into the parametric knowledge space of the LLM improves performance
- Substantially enhances both effectiveness and efficiency of knowledge augmentation compared to in-context methods
- Can be combined with traditional in-context RAG methods to achieve even better performance
- All code, data, and models have been open-sourced for reproducibility
**Limitations**: Requires modification of LLM parameters which may not be feasible for all deployment scenarios; document parameterization approach may have scalability constraints for very large corpora.

### Thakur and Vashisth (2024)

**Research question**: Can iterative loop mechanisms enhance the quality of retrieval-augmented text generation?
**Methodology**: Developed LoRAG framework that integrates a generative model, retrieval mechanism, and dynamic loop module to allow iterative refinement of generated text through interactions with retrieved information from the input context.
**Key findings**:
- LoRAG surpasses existing state-of-the-art models in BLEU score, ROUGE score, and perplexity on benchmark datasets
- Iterative refinement mechanism achieves both coherence and relevance in generated text
- Qualitative assessment demonstrates capability to produce contextually rich and coherent outputs
- Dynamic loop module effectively mitigates challenges in text generation through iterative retrieval interactions
**Limitations**: Evaluation limited to benchmark datasets; computational overhead from iterative loops not thoroughly analyzed; potential latency implications for real-time applications not discussed.

### Toro Isaza et al. (2024)

**Research question**: How can RAG systems address domain coverage and model size constraints in IT Support and AIOps applications?
**Methodology**: Developed a multi-component system combining RAG for answer generation, an encoder-only model for classification, and a generative LLM for query generation, with comprehensive documentation of architecture, data collection, annotation, and deployment planning.
**Key findings**:
- RAG enables smaller models to perform effectively in specialized domains without requiring large proprietary models
- The approach addresses cost and privacy concerns associated with using larger models like GPT-4
- Multi-component architecture (retrieval, classification, generation) effectively handles IT support case resolution workflows
- Practical lessons learned from development journey provide insights for enterprise AI deployment
**Limitations**: Preliminary validation stage with final evaluation plans still pending; domain-specific to IT support; deployment process not yet completed at time of publication.

### Ye et al. (2024)

**Research question**: How can the semantic gap between retrievers and LLMs in RAG systems be addressed to improve generation quality?
**Methodology**: Proposed R²AG framework that utilizes nuanced features from retrievers, employs a R²-Former to capture retrieval information, and designs a retrieval-aware prompting strategy to integrate retrieval information into LLM generation.
**Key findings**:
- Retrieval information serves as an anchor to aid LLMs in the generation process, filling the semantic gap between retrievers and generators
- R²AG is particularly effective in low-source scenarios where both LLMs and retrievers are frozen
- Extensive experiments across five datasets validated the effectiveness, robustness, and efficiency of the approach
- The framework reduces the burden on LLMs to distinguish retrieved documents using only their inherent knowledge
**Limitations**: Designed for frozen LLM and retriever scenarios; may require additional architectural components (R²-Former); effectiveness in dynamic fine-tuning scenarios not explored.

## References

Aghajani Asl, M., Asgari-Bidhendi, M., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful adaptive iterative refinement for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2510.22344

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated literature review using NLP techniques and LLM-based retrieval-augmented generation. arXiv. https://arxiv.org/abs/2411.18583

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating retrieval-augmented generation in Quranic studies: A study of 13 open-source large language models. arXiv. https://arxiv.org/abs/2503.16581

Kreileder, V. J. J., Reisinger, J., & Fischer, A. (2026). Evaluating chunking strategies for retrieval-augmented generation on academic texts. arXiv. https://arxiv.org/abs/2607.01852

Luo, L., Zhao, Z., Haffari, G., Phung, D., Gong, C., & Pan, S. (2025). GFM-RAG: Graph foundation model for retrieval augmented generation. arXiv. https://arxiv.org/abs/2502.01113

Naseh, A., Peng, Y., Suri, A., Chaudhari, H., Oprea, A., & Houmansadr, A. (2025). Riddle me this! Stealthy membership inference for retrieval-augmented generation. arXiv. https://arxiv.org/abs/2502.00306

Su, W., Tang, Y., Ai, Q., Yan, J., Wang, C., Wang, H., Ye, Z., Zhou, Y., & Liu, Y. (2025). Parametric retrieval augmented generation. arXiv. https://arxiv.org/abs/2501.15915

Thakur, A., & Vashisth, R. (2024). Loops on retrieval augmented generation (LoRAG). arXiv. https://arxiv.org/abs/2403.15450

Toro Isaza, P., Nidd, M., Zheutlin, N., Ahn, J., Bhatt, C. A., Deng, Y., Mahindru, R., Franz, M., Florian, H., & Roukos, S. (2024). Retrieval augmented generation-based incident resolution recommendation system for IT support. arXiv. https://arxiv.org/abs/2409.13707

Ye, F., Li, S., Zhang, Y., & Chen, L. (2024). R^2AG: Incorporating retrieval information into retrieval augmented generation. arXiv. https://arxiv.org/abs/2406.13249
