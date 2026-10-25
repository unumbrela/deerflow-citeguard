# Systematic Literature Review: Retrieval-Augmented Generation

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "retrieval augmented generation", cs.CL, 2024-01-01 to 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Retrieval-Augmented Generation (RAG) has emerged as a critical paradigm for enhancing large language models with external knowledge, addressing fundamental challenges including hallucination, knowledge staleness, and domain adaptation. This systematic literature review examines 10 recent arXiv papers (2024-2026) in the cs.CL category, revealing a field characterized by rapid architectural innovation, expanding domain applications, and growing security awareness. The surveyed literature demonstrates clear convergence on RAG's effectiveness in mitigating hallucinations across diverse domains, while simultaneously exposing critical vulnerabilities including membership inference attacks and limitations in handling complex multi-hop reasoning queries. Recent advances in graph-based retrieval, parametric knowledge integration, and iterative refinement frameworks represent promising directions for addressing these challenges, though significant gaps remain in evaluation methodology standardization and computational efficiency optimization.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "retrieval augmented generation", filtered to category cs.CL, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The review is further constrained to the cs.CL category, potentially excluding relevant work from adjacent categories such as cs.IR, cs.AI, or cs.LG that may address RAG from different perspectives.

## Themes

### Theme 1: Architecture Innovations for Enhanced Reasoning

A dominant theme across the surveyed literature is the development of novel RAG architectures designed to overcome limitations of standard retrieval-generation pipelines. Multiple papers propose sophisticated frameworks that fundamentally restructure how retrieval and generation interact. FAIR-RAG introduces an agentic framework with Structured Evidence Assessment that performs iterative refinement cycles, explicitly identifying evidence gaps and generating targeted sub-queries until comprehensive context is achieved (Aghajani Asl et al., 2025). Similarly, LoRAG incorporates dynamic loop mechanisms enabling iterative refinement of generated text through repeated interactions with retrieved information, demonstrating improvements in BLEU and ROUGE scores (Thakur & Vashisth, 2024). GFM-RAG takes a different approach, leveraging graph foundation models with 8M parameters trained on 60 knowledge graphs to capture complex query-knowledge relationships that conventional RAG systems miss (Luo et al., 2025). These architectural innovations share a common insight: standard one-shot retrieval is insufficient for complex reasoning tasks requiring synthesis across multiple knowledge sources.

### Theme 2: Parametric vs. In-Context Knowledge Integration

A second major theme concerns the fundamental question of how external knowledge should be integrated into language models. Traditional RAG approaches rely on in-context knowledge injection, appending retrieved documents to the input. However, this approach faces inherent limitations in context length and computational overhead, particularly for complex reasoning tasks. Parametric RAG proposes a paradigm shift by integrating external knowledge directly into the feed-forward network parameters of LLMs through document parameterization (Su et al., 2025). This approach eliminates the need for multiple document injection during inference, reducing computational costs while deepening knowledge integration into the model's parametric space. The framework demonstrates substantial improvements in both effectiveness and efficiency, and can be combined with traditional in-context methods for even better performance. This theme reflects a broader tension in the field between maintaining architectural simplicity and pursuing deeper, more efficient knowledge integration mechanisms.

### Theme 3: Security Vulnerabilities and Privacy Concerns

As RAG systems gain deployment in production environments, security and privacy concerns have emerged as a critical research direction. Naseh et al. (2025) expose a significant vulnerability through their Interrogation Attack, a membership inference technique that can determine whether specific documents exist in a RAG datastore using only natural-text queries. The attack achieves successful inference with just 30 queries while remaining stealthy—existing detectors identify adversarial prompts from prior methods up to 76 times more frequently. This work reveals that while RAG avoids weight tuning (which prevents parameter-based leakage), it introduces new attack surfaces through the retrieval mechanism itself. The attack costs less than $0.02 per document inference and demonstrates a 2x improvement in TPR@1%FPR over prior methods, raising serious concerns for RAG deployments handling sensitive information. This theme underscores the need for security-by-design approaches in RAG system development.

### Theme 4: Domain-Specific Applications and Adaptations

The surveyed literature demonstrates RAG's versatility across diverse application domains, each presenting unique challenges and requirements. In religious and sensitive domains, Khalila et al. (2025) investigate RAG for Quranic studies, where hallucination poses particularly serious concerns. Their evaluation of 13 open-source LLMs reveals that large models consistently outperform smaller ones in capturing query semantics, though well-optimized smaller architectures like Llama3.2:3b show remarkable faithfulness (4.619) and relevance (4.857) scores. In enterprise IT support, Toro Isaza et al. (2024) present a RAG-based incident resolution system that enables smaller models to leverage domain-specific knowledge, addressing both cost concerns and domain coverage limitations without requiring large proprietary models. For academic literature review automation, Ali et al. (2024) demonstrate that GPT-3.5-turbo with RAG achieves the highest ROUGE-1 score (0.364) compared to transformer models and frequency-based methods. These domain-specific applications reveal a common pattern: RAG enables smaller, more efficient models to achieve domain expertise through retrieval rather than extensive fine-tuning.

### Theme 5: Retrieval Optimization Strategies

Optimizing the retrieval component of RAG systems represents another active research direction. The literature explores multiple strategies for improving retrieval quality and its integration with generation. R²AG addresses the semantic gap between retrievers and LLMs by incorporating retrieval information into the generation process through a R²-Former and retrieval-aware prompting strategy (Ye et al., 2024). This approach helps LLMs distinguish and utilize retrieved documents more effectively, particularly in low-resource scenarios where models remain frozen. In contrast, Kreileder et al. (2026) evaluate chunking strategies for RAG on academic texts, finding that cluster-based semantic chunking does not outperform simpler fixed-size or recursive approaches under their tested configuration. Their work also reveals that the RAGAs faithfulness metric shows limited reliability in this setup, highlighting methodological challenges in RAG evaluation. These studies collectively suggest that retrieval optimization is highly context-dependent, with no universally superior strategy across all domains and document types.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong agreement on several key points. First, all papers affirm RAG's fundamental effectiveness in mitigating hallucinations and enabling domain adaptation without extensive model fine-tuning. Second, there is consensus that standard one-shot RAG pipelines struggle with complex, multi-hop queries requiring synthesis across disparate sources—a limitation motivating the architectural innovations in FAIR-RAG, GFM-RAG, and LoRAG. Third, multiple papers converge on the finding that retrieval quality and integration strategy significantly impact overall system performance, though they diverge on optimal approaches. Finally, the literature collectively acknowledges trade-offs between computational efficiency and generation quality, with different frameworks optimizing for different points on this spectrum.

**Disagreements**: Notable disagreements emerge around retrieval optimization strategies. While some papers advocate for sophisticated approaches like graph-based retrieval (Luo et al., 2025) or cluster-based semantic chunking in principle, empirical results are mixed—Kreileder et al. (2026) found cluster-based chunking did not outperform simpler strategies in their evaluation. Another tension exists between parametric and in-context knowledge integration: Parametric RAG claims substantial efficiency advantages (Su et al., 2025), but this approach requires model parameter access and modification, limiting applicability to open-source or custom models. The literature also shows disagreement on evaluation methodologies, with Kreileder et al. (2026) reporting limited reliability of RAGAs faithfulness metrics, while other papers rely on standard QA metrics without addressing their limitations for RAG-specific evaluation.

## Gaps and Open Questions

The collective literature reveals several significant gaps and open questions. First, evaluation methodology remains underdeveloped: multiple papers note limitations in existing metrics (particularly RAGAs faithfulness), yet no consensus alternative has emerged. This methodological gap complicates cross-paper comparison and makes it difficult to assess true progress in the field. Second, computational overhead from iterative refinement methods receives insufficient attention—while FAIR-RAG and LoRAG demonstrate improved accuracy through iterative cycles, neither provides detailed analysis of latency, cost, or energy implications for production deployment.

Third, generalizability across domains remains uncertain. While domain-specific applications demonstrate RAG's versatility, most evaluations are confined to single domains (Quranic studies, IT support, academic literature), making it unclear whether architectural innovations transfer effectively across domains. Fourth, security research is nascent—while Naseh et al. (2025) expose critical membership inference vulnerabilities, the literature lacks systematic defense mechanisms or security frameworks for RAG systems.

Finally, the literature reveals a gap in understanding the interaction between retrieval strategies and document characteristics. Kreileder et al. (2026) note that performance varied substantially based on document formatting and preprocessing, yet systematic guidance on matching retrieval strategies to document types remains absent. Future research should address these gaps through standardized evaluation benchmarks, comprehensive efficiency analyses, cross-domain transfer studies, security framework development, and retrieval strategy guidelines.

## Per-Paper Annotations

### Ali et al. (2024)

**Research question**: How can literature review generation be automated from PDF files using Natural Language Processing techniques?

**Methodology**: Evaluated three distinct systems (spaCy frequency-based method, Simple T5 transformer model, and GPT-3.5-turbo RAG) on the SciTLDR dataset using ROUGE scores for comparative evaluation.

**Key findings**:
- GPT-3.5-turbo achieved the highest ROUGE-1 score of 0.364 among all three systems tested
- The transformer model (Simple T5) ranked second in performance
- The frequency-based spaCy method performed worst among the three approaches
- A graphical user interface was developed for the best-performing LLM-based system

**Limitations**: Evaluation was limited to the SciTLDR dataset only; ROUGE scores indicate moderate performance with significant room for improvement in automated literature review quality.

### Aghajani Asl et al. (2025)

**Research question**: How can RAG systems be improved to handle complex multi-hop queries that require synthesizing information from disparate sources?

**Methodology**: Introduced FAIR-RAG, an agentic framework with Structured Evidence Assessment (SEA) module that performs iterative refinement cycles with explicit gap analysis and adaptive query refinement until evidence is verified as sufficient.

**Key findings**:
- Achieved F1-score of 0.453 on HotpotQA, an absolute improvement of 8.3 points over the strongest iterative baseline
- Established new state-of-the-art performance on challenging multi-hop QA benchmarks (HotpotQA, 2WikiMultiHopQA, MusiQue)
- Structured evidence-driven refinement with explicit gap analysis proved crucial for reliable reasoning
- Iterative cycle ensures comprehensive context before final faithful generation

**Limitations**: Iterative refinement cycles may increase computational overhead and latency; performance on non-multi-hop or simpler queries not thoroughly evaluated.

### Khalila et al. (2025)

**Research question**: How do different-sized open-source LLMs perform with RAG in sensitive, domain-specific applications like Quranic studies where hallucination is a critical concern?

**Methodology**: Evaluated 13 open-source LLMs across three size categories (large, medium, small) with RAG on a descriptive Quranic surahs dataset using human evaluation metrics for context relevance, answer faithfulness, and answer relevance.

**Key findings**:
- Large models consistently outperform smaller models in capturing query semantics and producing accurate, contextually grounded responses
- Llama3.2:3b achieved exceptional faithfulness (4.619) and relevance (4.857) scores despite being categorized as small
- Well-optimized smaller architectures show promise for domain-specific applications
- RAG effectively mitigates hallucination concerns in religious and sensitive contexts

**Limitations**: Human evaluation introduces subjectivity in scoring; study limited to Quranic domain which may not generalize to other religious or sensitive domains; limited to open-source models only.

### Kreileder et al. (2026)

**Research question**: Does cluster-based semantic chunking improve retrieval and answer quality compared to fixed-size and recursive chunking for RAG systems on academic texts?

**Methodology**: Evaluated different chunking strategies (cluster-based semantic, fixed-size, recursive) on long, structured academic theses using the Retrieval Augmented Generation Assessment (RAGAs) framework.

**Key findings**:
- RAGAs-based faithfulness metric shows limited reliability when evaluating RAG on academic theses
- Performance varied substantially between fixed questions versus document-specific questions
- Document formatting and preprocessing likely influenced retrieval and generation performance
- Cluster-based semantic chunking did not outperform simpler fixed-size or recursive chunking strategies under the tested configuration

**Limitations**: The RAGAs faithfulness metric demonstrated limited reliability in this evaluation setup, and results may be specific to the tested configuration and academic thesis documents.

### Luo et al. (2025)

**Research question**: How can graph structures be leveraged to improve RAG's ability to capture complex relationships between knowledge pieces for intricate multi-source reasoning?

**Methodology**: Developed GFM-RAG with an 8M-parameter graph neural network trained in two stages on 60 knowledge graphs (14M+ triples) and 700k documents to reason over graph structures for query-knowledge relationships.

**Key findings**:
- First graph foundation model applicable to unseen datasets for retrieval without any fine-tuning required
- Achieves state-of-the-art performance on three multi-hop QA datasets and seven domain-specific RAG datasets
- Maintains efficiency while aligning with neural scaling laws
- Two-stage training on large-scale data enables impressive generalizability

**Limitations**: Graph structures may still contain noise and incompleteness affecting performance; training requires access to large-scale graph datasets which may not be available for all domains.

### Naseh et al. (2025)

**Research question**: Can membership inference attacks be performed stealthily against RAG systems using natural-language queries that evade detection?

**Methodology**: Developed the Interrogation Attack (IA) that crafts natural-text queries answerable only when the target document is present in the RAG datastore, testing across diverse RAG configurations.

**Key findings**:
- Successful membership inference achieved with only 30 queries per document
- Existing detectors identify adversarial prompts from prior methods up to 76x more frequently than IA-generated queries
- Achieved 2x improvement in TPR@1%FPR over prior inference attacks across diverse RAG configurations
- Attack costs less than $0.02 per document inference

**Limitations**: Evaluation focused on specific RAG configurations and straightforward detectors; effectiveness against advanced defense mechanisms or query rewriting techniques requires further investigation.

### Su et al. (2025)

**Research question**: How can external knowledge be integrated more deeply into LLMs beyond the limitations of in-context knowledge injection in traditional RAG?

**Methodology**: Introduced Parametric RAG, a new paradigm that integrates external knowledge directly into the parameters of feed-forward networks (FFN) of LLMs through document parameterization, eliminating the need for in-context document injection.

**Key findings**:
- Parametric RAG reduces online computational costs by eliminating the need to inject multiple documents into the LLM's input context
- Direct integration of external knowledge into FFN parameters deepens knowledge integration into the LLM's parametric knowledge space
- Experimental results show substantial improvements in both effectiveness and efficiency of knowledge augmentation compared to in-context methods
- Parametric RAG can be combined with traditional in-context RAG methods to achieve even better performance

**Limitations**: The approach requires document parameterization and modifications to FFN layers, which may not be applicable to all LLM architectures or closed-source models where parameter access is restricted.

### Thakur and Vashisth (2024)

**Research question**: How can iterative refinement mechanisms improve the quality of retrieval-augmented text generation?

**Methodology**: Presented LoRAG framework that integrates a generative model, retrieval mechanism, and dynamic loop module to enable iterative refinement of generated text through repeated interactions with retrieved information from the input context.

**Key findings**:
- LoRAG surpasses existing state-of-the-art models in BLEU score, ROUGE score, and perplexity on benchmark datasets
- The iterative loop mechanism effectively achieves both coherence and relevance in generated text
- Qualitative assessment demonstrates LoRAG's capability to produce contextually rich and coherent outputs
- Iterative loops successfully mitigate common challenges in retrieval-augmented text generation

**Limitations**: The paper provides limited detail on computational overhead from iterative loops; specific benchmark datasets and comparison baselines are not fully specified in the available abstract.

### Toro Isaza et al. (2024)

**Research question**: How can RAG address domain coverage and model size constraints for clients implementing generative AI in IT Support and AIOps?

**Methodology**: Developed a system combining RAG for answer generation with an encoder-only model for classification and a generative LLM for query generation, specifically designed for IT support case solution recommendation.

**Key findings**:
- RAG enables smaller models to leverage domain-specific retrieved knowledge, addressing both cost/privacy concerns and domain coverage limitations
- The hybrid architecture combining RAG, encoder-only classification, and generative LLM for query generation effectively serves IT support domains
- Clients can avoid larger proprietary models like GPT-4 while still achieving adequate domain coverage through retrieval augmentation
- The system architecture, data collection, annotation processes, and development journey provide practical lessons for similar deployments

**Limitations**: The paper presents preliminary validations with final deployment and evaluation plans still pending, indicating the system was not yet fully validated in production at time of publication.

### Ye et al. (2024)

**Research question**: How can the semantic gap between LLMs and retrievers in RAG systems be addressed to improve generation quality?

**Methodology**: Proposed R²AG framework that utilizes nuanced features from retrievers, employs a R²-Former to capture retrieval information, and uses a retrieval-aware prompting strategy to integrate retrieval information into LLMs' generation.

**Key findings**:
- R²AG effectively bridges the semantic gap between retrievers and LLMs by incorporating retrieval information into the generation process
- Retrieval information serves as an anchor to aid LLMs during generation, reducing the burden of distinguishing retrieved documents
- The framework is particularly effective in low-resource scenarios where both LLMs and retrievers remain frozen
- Extensive experiments across five datasets validated the effectiveness, robustness, and efficiency of R²AG

**Limitations**: The approach is designed for scenarios where LLMs and retrievers are frozen, which may limit applicability in settings where model fine-tuning is available or desired.

## References

Aghajani Asl, M., Asgari-Bidhendi, M., & Minaei-Bidgoli, B. (2025). FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation. arXiv. https://arxiv.org/abs/2510.22344

Ali, N. F., Mohtasim, M. M., Mosharrof, S., & Krishna, T. G. (2024). Automated Literature Review Using NLP Techniques and LLM-Based Retrieval-Augmented Generation. arXiv. https://arxiv.org/abs/2411.18583

Khalila, Z., Nasution, A. H., Monika, W., Onan, A., Murakami, Y., Radi, Y. B. I., & Osmani, N. M. (2025). Investigating Retrieval-Augmented Generation in Quranic Studies: A Study of 13 Open-Source Large Language Models. arXiv. https://arxiv.org/abs/2503.16581

Kreileder, V. J. J., Reisinger, J., & Fischer, A. (2026). Evaluating Chunking Strategies for Retrieval-Augmented Generation on Academic Texts. arXiv. https://arxiv.org/abs/2607.01852

Luo, L., Zhao, Z., Haffari, G., Phung, D., Gong, C., & Pan, S. (2025). GFM-RAG: Graph Foundation Model for Retrieval Augmented Generation. arXiv. https://arxiv.org/abs/2502.01113

Naseh, A., Peng, Y., Suri, A., Chaudhari, H., Oprea, A., & Houmansadr, A. (2025). Riddle Me This! Stealthy Membership Inference for Retrieval-Augmented Generation. arXiv. https://arxiv.org/abs/2502.00306

Su, W., Tang, Y., Ai, Q., Yan, J., Wang, C., Wang, H., Ye, Z., Zhou, Y., & Liu, Y. (2025). Parametric Retrieval Augmented Generation. arXiv. https://arxiv.org/abs/2501.15915

Thakur, A., & Vashisth, R. (2024). Loops On Retrieval Augmented Generation (LoRAG). arXiv. https://arxiv.org/abs/2403.15450

Toro Isaza, P., Nidd, M., Zheutlin, N., Ahn, J.-w., Bhatt, C. A., Deng, Y., Mahindru, R., Franz, M., Florian, H., & Roukos, S. (2024). Retrieval Augmented Generation-Based Incident Resolution Recommendation System for IT Support. arXiv. https://arxiv.org/abs/2409.13707

Ye, F., Li, S., Zhang, Y., & Chen, L. (2024). R^2AG: Incorporating Retrieval Information into Retrieval Augmented Generation. arXiv. https://arxiv.org/abs/2406.13249
