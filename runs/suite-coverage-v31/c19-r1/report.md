# Systematic Literature Review: Secure Retrieval-Augmented Generation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "secure retrieval augmented generation", filtered to category cs.CR, published between 2024-04-09 and 2026-04-09
**Citation format**: APA 7th edition

## Executive Summary

The literature on Secure Retrieval-Augmented Generation (RAG) has rapidly evolved between 2024 and 2026, reflecting growing recognition that RAG systems introduce distinct security vulnerabilities beyond inherent model flaws. The surveyed papers collectively reveal a field organizing around three core challenges: protecting RAG systems from poisoning attacks, establishing formal security guarantees through cryptographic methods, and building comprehensive taxonomies to categorize threats and defenses. Researchers have proposed diverse solutions ranging from non-parametric detection frameworks and encryption-based approaches to federated architectures and blockchain-secured decentralized systems. A notable trend is the emergence of benchmarking initiatives like SafeRAG, which systematically evaluate RAG vulnerabilities across multiple attack categories. The field demonstrates strong convergence on the need for multi-layered defenses, though significant gaps remain in standardized evaluation methodologies and real-world deployment validation.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "secure retrieval augmented generation", filtered to category cs.CR, published between 2024-04-09 and 2026-04-09. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Defense Against Poisoning and Adversarial Attacks

A dominant research direction focuses on protecting RAG systems from data poisoning attacks, where adversaries inject malicious content into knowledge databases to manipulate system outputs. Cheng et al. (2025) introduced RAGuard, a non-parametric detection framework that expands retrieval scope to increase the proportion of clean text, then applies chunk-wise perplexity filtering and text similarity filtering to identify poisoned content. Their approach demonstrates effectiveness even against strong adaptive attacks, suggesting that detection-based methods can provide robust protection without requiring model retraining.

Complementing this, Shih and Kang (2025) implemented a secure RAG chatbot for smart tourism that defends against prompt injection attacks through multi-layered linguistic analysis and guardrails including system norms, gatekeepers for intent judgment, and reverse RAG text. Their system achieved over 95% accuracy on benign tasks while demonstrating substantial detection of prompt injection attacks, highlighting the practical viability of layered defense strategies in real-world applications.

### Theme 2: Cryptographic and Formal Security Guarantees

Another significant thread emphasizes establishing provable security guarantees through cryptographic techniques. Zhou et al. (2025) proposed the first provably secure framework for RAG systems (SAG) using pre-storage full-encryption to protect both retrieved content and vector embeddings, with formal security proofs under a computational security model. This work establishes a theoretical foundation for verifiably secure RAG systems, moving beyond empirical defenses to mathematically verifiable security properties.

Zhao (2024) extended cryptographic approaches to federated environments with FRAG, which enables mutually-distrusted parties to collaboratively perform approximate nearest neighbor searches on encrypted vectors using single-key homomorphic encryption. The framework achieves IND-CPA security under practical assumptions without requiring non-collusion assumptions, demonstrating that strong security guarantees can be maintained in distributed, multi-party RAG deployments.

### Theme 3: Comprehensive Taxonomies and Survey Frameworks

The emergence of comprehensive survey papers indicates field maturation and the need for systematic organization of rapidly growing literature. Xu et al. (2026) curated 135 works on RAG security, organizing them using the SLOT taxonomy (Surface, Layer, Objective, Target scope) and mapping studies onto an external knowledge-access pipeline. Their analysis identified three critical mismatches: target mismatch (T2 attacks outpace defenses), stage mismatch (S1 attacks outnumber defenses), and signal mismatch (sophisticated attacks challenge anomaly-based defenses).

Mu et al. (2026) conducted the first end-to-end survey dedicated exclusively to RAG system security, analyzing vulnerability mechanisms guided by the RAG workflow and constructing a taxonomy of defense technologies from input and output stage perspectives. Their work systematically categorizes threat vectors including data poisoning, adversarial attacks, and membership inference attacks, providing a unified framework for understanding the security landscape.

### Theme 4: Secure Code Generation Applications

A specialized application domain receiving significant attention is secure code generation, where RAG systems retrieve security documentation and code examples to assist developers. Shi and Zhang (2025) proposed RESCUE, which improves secure code generation through hybrid knowledge base construction combining LLM-assisted cluster-then-summarize distillation with program slicing, and hierarchical multi-faceted retrieval. Their framework improved the SecurePass@1 metric by an average of 4.8 points over existing methods, establishing new state-of-the-art performance.

Sriram et al. (2026) enhanced this direction with a retrieval-augmented, multi-tool repair workflow that iteratively refines code outputs using compiler diagnostics, CodeQL security scanning, and KLEE symbolic execution. For DeepSeek-Coder-1.3B, security vulnerabilities were reduced by 96%, while for CodeLlama-7B, the critical security defect rate decreased from 58.55% to 22.19%, demonstrating that tool-assisted self-repair proves effective even on larger models.

### Theme 5: Decentralized and Blockchain-Secured Architectures

Emerging research explores decentralized architectures that eliminate single points of failure and enable data owners to maintain control. Lu et al. (2025) developed a decentralized RAG system with a novel reliability scoring mechanism that dynamically evaluates each source based on response quality, managed through blockchain-based smart contracts for transparency and trust. The system achieved a +10.7% performance improvement over centralized counterparts in unreliable data environments, suggesting that decentralization can provide both security and performance benefits.

### Theme 6: Benchmarking and Systematic Evaluation

The field has recognized the need for standardized benchmarking to evaluate RAG security systematically. Liang et al. (2025) introduced SafeRAG, a benchmark that classifies attack tasks into four categories: silver noise, inter-context conflict, soft ad, and white Denial-of-Service. Their experiments on 14 representative RAG components revealed that RAG exhibits significant vulnerability to all classified attack tasks, with even apparent attacks easily bypassing existing retrievers, filters, or advanced LLMs. This work provides critical infrastructure for comparing defense mechanisms and tracking field progress.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong agreement on several fundamental points. First, there is consensus that RAG systems require multi-layered defenses rather than single-point solutions (Cheng et al., 2025; Shih & Kang, 2025; Mu et al., 2026). Second, researchers converge on the view that RAG security vulnerabilities are distinct from inherent model flaws and require dedicated attention to the external knowledge-access pipeline (Xu et al., 2026; Mu et al., 2026). Third, there is agreement that cryptographic methods can provide strong security guarantees, though practical deployment remains challenging (Zhou et al., 2025; Zhao, 2024).

**Disagreements**: While not explicit contradictions, tensions exist between different philosophical approaches. Detection-based methods (Cheng et al., 2025; Shih & Kang, 2025) assume attacks will occur and focus on identification and mitigation, whereas prevention-based cryptographic approaches (Zhou et al., 2025; Zhao, 2024) aim to make attacks impossible through encryption. The field has not yet resolved which approach offers better practical trade-offs between security, performance, and usability. Additionally, centralized architectures with strong defenses compete against decentralized approaches (Lu et al., 2025), with unresolved questions about which model better serves different deployment scenarios.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature:

1. **Limited empirical validation**: Most proposed frameworks are evaluated on benchmark datasets or simulated environments, with limited real-world deployment validation. The abstract-level limitations (not stated in abstract for most papers) suggest that practical deployment challenges remain underexplored.

2. **Standardized evaluation metrics**: While SafeRAG (Liang et al., 2025) provides a benchmark, the field lacks universally accepted metrics for comparing defense mechanisms across different threat models and deployment contexts.

3. **Performance-security trade-offs**: Cryptographic approaches (Zhou et al., 2025; Zhao, 2024) acknowledge performance overheads but provide limited analysis of practical trade-offs in production environments.

4. **Adaptive attack evaluation**: While Cheng et al. (2025) test against adaptive attacks, systematic evaluation of how defenses perform against evolving, adaptive adversaries remains limited.

5. **Integration challenges**: The literature treats different security mechanisms in isolation, with limited work on how to integrate detection-based, cryptographic, and architectural defenses into cohesive systems.

6. **Human factors**: None of the surveyed papers address how security mechanisms affect user experience, developer workflows, or adoption barriers, representing a significant gap for practical deployment.

## Per-Paper Annotations

### Cheng et al. (2025)

**Research question**: How can Retrieval-Augmented Generation systems be protected against data poisoning attacks that inject malicious texts into knowledge databases?

**Methodology**: The authors propose RAGuard, a non-parametric detection framework that expands retrieval scope to increase clean text proportion, then applies chunk-wise perplexity filtering and text similarity filtering to identify poisoned content.

**Key findings**:
- RAGuard effectively detects and mitigates poisoning attacks in RAG systems
- Expanding retrieval scope reduces the likelihood of retrieving poisoned content
- Chunk-wise perplexity filtering detects abnormal variations in retrieved texts
- Text similarity filtering flags highly similar suspicious texts
- The framework remains effective against strong adaptive attacks

**Limitations**: Not stated in abstract

### Zhou et al. (2025)

**Research question**: How can RAG systems achieve formal security guarantees against privacy and security risks such as data leakage and data poisoning?

**Methodology**: The authors propose the first provably secure framework for RAG systems (SAG) using pre-storage full-encryption to protect both retrieved content and vector embeddings, with formal security proofs under a computational security model.

**Key findings**:
- The SAG framework provides dual protection for retrieved content and vector embeddings through full-encryption
- Only authorized entities can access encrypted data
- Formal security proofs verify confidentiality and integrity
- The framework effectively resists state-of-the-art attacks across multiple benchmark datasets
- Establishes theoretical foundation for verifiably secure RAG systems

**Limitations**: Not stated in abstract

### Xu et al. (2026)

**Research question**: What are the security risks, attack vectors, and defense mechanisms in Retrieval-Augmented Generation systems, and how can they be systematically categorized?

**Methodology**: The authors conducted a systematic search and curated 135 works on RAG security, organizing them using SLOT taxonomy (Surface, Layer, Objective, Target scope) and mapping studies onto an external knowledge-access pipeline to identify mismatches.

**Key findings**:
- Secure RAG is framed as securing external knowledge access paths distinct from inherent model flaws
- Three mismatches identified: target mismatch (T2 attacks outpace defenses), stage mismatch (S1 attacks outnumber defenses), and signal mismatch (sophisticated attacks challenge anomaly-based defenses)
- 135 works were curated and categorized by attack surface and defense layer
- T2 attacks are more prevalent than T2 defenses and evaluation methods
- Machine-readable SLOT labels and selected-paper metadata are publicly released

**Limitations**: Not stated in abstract

### Mu et al. (2026)

**Research question**: What are the system-level security vulnerabilities in RAG architectures, and how can threats and defenses be comprehensively categorized across the RAG pipeline?

**Methodology**: The paper analyzes vulnerability mechanisms guided by the RAG workflow, systematically categorizes threat vectors (data poisoning, adversarial attacks, membership inference), and constructs a taxonomy of defense technologies from input and output stage perspectives.

**Key findings**:
- Multi-module RAG architecture introduces complex system-level security vulnerabilities
- Core threats include data poisoning, adversarial attacks, and membership inference attacks
- Input-side defenses include dynamic access control, homomorphic encryption retrieval, and adversarial pre-filtering
- Output-side techniques include federated learning isolation, differential privacy perturbation, and data sanitization
- This is the first end-to-end survey dedicated to RAG system security with unified threat-defense-evaluation analysis

**Limitations**: Not stated in abstract

### Zhao (2024)

**Research question**: How can mutually-distrusted parties collaboratively perform ANN searches on encrypted vectors in distributed databases while maintaining strong security guarantees?

**Methodology**: The authors introduce FRAG, a federated RAG paradigm using single-key homomorphic encryption for simplified key management and multiplicative caching technique for efficient encryption of floating-point numbers, with security proofs via standard cryptographic reductions.

**Key findings**:
- FRAG enables collaborative ANN searches on encrypted query vectors and data without exposing information to any party
- Single-key homomorphic encryption simplifies key management across mutually-distrusted parties
- Multiplicative caching technique significantly improves computational performance for large-scale federated environments
- Achieves IND-CPA security under practical assumptions without requiring non-collusion assumptions
- Performance overheads remain comparable to traditional non-federated RAG systems

**Limitations**: Not stated in abstract

### Shih and Kang (2025)

**Research question**: How can a RAG-enhanced AI chatbot for smart tourism be designed to defend against prompt injection attacks while maintaining high contextual awareness?

**Methodology**: The authors designed and implemented a secure RAG chatbot integrating API function calls, multi-layered linguistic analysis (lexical, semantic, pragmatic), and guardrails including system norms, gatekeepers for intent judgment, and reverse RAG text. The system was evaluated using 674 adversarial prompts and 223 benign queries, with a GPT-5 variant benchmarked for inherent robustness.

**Key findings**:
- The secure RAG chatbot achieved over 95% accuracy on benign tasks
- The system demonstrated substantial detection of prompt injection attacks
- GPT-5 blocked approximately 85% of attacks, showing progress but highlighting the need for layered defenses
- Key security features include tiered response strategy, RAG-driven knowledge grounding, and intent decomposition across multiple linguistic levels
- The work contributes to sustainable tourism, multilingual accessibility, and ethical AI deployment

**Limitations**: Not stated in abstract

### Shi and Zhang (2025)

**Research question**: How can retrieval-augmented generation be improved to enhance LLM-based secure code generation by addressing noise in security documents and overlooked security semantics in task descriptions?

**Methodology**: The authors propose RESCUE, a RAG framework with two innovations: (1) hybrid knowledge base construction combining LLM-assisted cluster-then-summarize distillation with program slicing to produce security guidelines and focused code examples, and (2) hierarchical multi-faceted retrieval that traverses the knowledge base top-to-bottom while integrating multiple security-critical facts at each level. The framework was evaluated on four benchmarks comparing five state-of-the-art methods across six LLMs.

**Key findings**:
- RESCUE improves the SecurePass@1 metric by an average of 4.8 points over existing methods
- The framework establishes a new state-of-the-art performance for secure code generation
- Hybrid knowledge base construction effectively distills high-level security guidelines and concise, security-focused code examples
- Hierarchical multi-faceted retrieval ensures comprehensive and accurate retrieval of security-critical information
- Ablation studies validated the effectiveness of individual RESCUE components

**Limitations**: Not stated in abstract

### Lu et al. (2025)

**Research question**: How can a decentralized RAG system address varying source reliability while enabling data owners to maintain full control over their sources without relying on centralized architecture?

**Methodology**: The authors developed a decentralized RAG system with a novel reliability scoring mechanism that dynamically evaluates each source based on response quality and prioritizes high-quality sources during retrieval. The scoring process is managed through blockchain-based smart contracts for transparency and trust. The system was evaluated using two Llama models (3B and 8B) in two simulated environments with six data sources of varying reliability levels.

**Key findings**:
- The decentralized system achieves a +10.7% performance improvement over centralized counterparts in unreliable data environments
- Performance approaches the upper-bound of centralized systems under ideally reliable data conditions
- Blockchain-based scoring management enables secure and trustworthy reliability records without central authority
- The system achieves approximately 56% marginal cost savings through batched update operations
- The infrastructure enables data owners to maintain full control while foundation models utilize information directly from sources

**Limitations**: Not stated in abstract

### Sriram et al. (2026)

**Research question**: How can retrieval-augmented generation combined with multi-tool feedback improve LLM-assisted code generation to reduce security vulnerabilities, logical inconsistencies, and compilation errors?

**Methodology**: The authors propose a retrieval-augmented, multi-tool repair workflow where a single code-generating LLM iteratively refines outputs using compiler diagnostics, CodeQL security scanning, and KLEE symbolic execution. A lightweight embedding model performs semantic retrieval of previously successful repairs to provide security-focused examples. The system was evaluated on 3,242 programs generated by DeepSeek-Coder-1.3B and CodeLlama-7B.

**Key findings**:
- For DeepSeek-Coder-1.3B, security vulnerabilities were reduced by 96%
- For CodeLlama-7B, the critical security defect rate decreased from 58.55% to 22.19%
- Tool-assisted self-repair proves effective even on 'stubborn' larger models
- Semantic retrieval of successful repairs provides effective security-focused guidance for generation
- The multi-tool feedback approach (compiler, CodeQL, KLEE) significantly improves code robustness

**Limitations**: Not stated in abstract

### Liang et al. (2025)

**Research question**: How vulnerable is retrieval-augmented generation to various attack tasks when incorporating external and unverified knowledge, and how can RAG security be systematically benchmarked?

**Methodology**: The authors introduced SafeRAG, a benchmark that classifies attack tasks into four categories (silver noise, inter-context conflict, soft ad, and white Denial-of-Service) and constructed a primarily manual RAG security evaluation dataset for each task. The SafeRAG dataset was used to simulate various attack scenarios, and experiments were conducted on 14 representative RAG components to evaluate vulnerability.

**Key findings**:
- RAG exhibits significant vulnerability to all classified attack tasks
- Even the most apparent attack tasks can easily bypass existing retrievers, filters, or advanced LLMs
- Attack manipulation of knowledge results in degradation of RAG service quality
- The SafeRAG benchmark successfully simulates various attack scenarios RAG systems may encounter
- Four attack task categories were identified: silver noise, inter-context conflict, soft ad, and white Denial-of-Service

**Limitations**: Not stated in abstract

## References

Cheng, Z., Sun, J., Gao, A., Quan, Y., Liu, Z., Hu, X., & Fang, M. (2025). Secure retrieval-augmented generation against poisoning attacks. arXiv. https://arxiv.org/abs/2510.25025

Liang, X., Niu, S., Li, Z., Zhang, Z., Wang, H., Xiong, F., Fan, Z., Tang, B., Song, S., Wang, M., & Yang, J. (2025). SafeRAG: Benchmarking security in retrieval-augmented generation of large language model. arXiv. https://arxiv.org/abs/2501.18636

Lu, Y., Tang, W., Johnson, M., Jung, T., & Jiang, M. (2025). A decentralized retrieval augmented generation system with source reliabilities secured on blockchain. arXiv. https://arxiv.org/abs/2511.07577

Mu, Y., Hu, H., Li, F., Yuan, Q., Wu, J., Liu, Z., Liu, P., Wang, M., Zhou, H., & Liu, Y. (2026). Towards secure retrieval-augmented generation: A comprehensive review of threats, defenses and benchmarks. arXiv. https://arxiv.org/abs/2603.21654

Shi, J., & Zhang, T. (2025). RESCUE: Retrieval augmented secure code generation. arXiv. https://arxiv.org/abs/2510.18204

Shih, Y.-K., & Kang, Y.-K. (2025). Design and implementation of a secure RAG-enhanced AI chatbot for smart tourism customer service: Defending against prompt injection attacks -- A case study of Hsinchu, Taiwan. arXiv. https://arxiv.org/abs/2509.21367

Sriram, V., Pandita, S., Lakshmanan, A., Shamraj, A., & Saha, S. (2026). Improving LLM-assisted secure code generation through retrieval-augmented-generation and multi-tool feedback. arXiv. https://arxiv.org/abs/2601.00509

Xu, Y., Zhang, M., Ge, Z., Li, H., Hu, N., Zhang, Y., Wen, Z., Zhang, J. C., Li, Q., & Chen, L. (2026). A survey of secure retrieval-augmented generation. arXiv. https://arxiv.org/abs/2604.08304

Zhao, D. (2024). FRAG: Toward federated vector database management for collaborative and secure retrieval-augmented generation. arXiv. https://arxiv.org/abs/2410.13272

Zhou, P., Feng, Y., & Yang, Z. (2025). Provably secure retrieval-augmented generation. arXiv. https://arxiv.org/abs/2508.01084
