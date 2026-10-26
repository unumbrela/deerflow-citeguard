# Systematic Literature Review: Secure Retrieval-Augmented Generation

**Review Period:** April 9, 2024 – April 8, 2026  
**Category:** cs.CR (Cryptography and Security)  
**Search Date:** October 26, 2026  
**Total Papers:** 10

---

## Executive Summary

This systematic literature review examines recent advances in secure Retrieval-Augmented Generation (RAG) systems. The reviewed papers, published between April 2024 and April 2026, address critical security challenges including data poisoning attacks, privacy preservation, adversarial vulnerabilities, and secure code generation. The literature reveals a rapidly evolving field with contributions spanning theoretical security frameworks, practical defense mechanisms, and comprehensive benchmarking efforts.

Key themes emerging from this review include:
- **Poisoning attack defenses** through detection frameworks and filtering mechanisms
- **Provably secure architectures** with formal security guarantees
- **Federated and decentralized approaches** for collaborative secure RAG
- **Security-focused code generation** leveraging RAG for vulnerability reduction
- **Comprehensive threat taxonomies** and benchmarking frameworks

---

## Annotated Bibliography (APA Format)

### 1. Cheng, Z., Sun, J., Gao, A., Quan, Y., Liu, Z., Hu, X., & Fang, M. (2025). Secure Retrieval-Augmented Generation against Poisoning Attacks. *arXiv preprint arXiv:2510.25025*.

**Published:** October 28, 2025

This paper introduces RAGuard, a detection framework designed to identify and mitigate poisoned texts in RAG systems. The authors address the critical vulnerability of data poisoning attacks, where adversaries inject malicious content into knowledge databases to manipulate system outputs. RAGuard employs a three-pronged approach: (1) expanding retrieval scope to increase clean text proportion, (2) chunk-wise perplexity filtering to detect abnormal variations, and (3) text similarity filtering to flag highly similar suspicious texts. The non-parametric nature of this approach enhances adaptability against evolving attack strategies. Experimental validation on large-scale datasets demonstrates effectiveness against both standard and adaptive poisoning attacks, establishing RAGuard as a significant contribution to RAG security defenses.

**Key Contributions:** Non-parametric poisoning detection, multi-layered filtering strategy, adaptive attack resistance

---

### 2. Zhou, P., Feng, Y., & Yang, Z. (2025). Provably Secure Retrieval-Augmented Generation. *arXiv preprint arXiv:2508.01084*.

**Published:** August 1, 2025

This groundbreaking work proposes the first provably secure framework for RAG systems, addressing the lack of formal security guarantees in existing defense strategies. The authors introduce a pre-storage full-encryption scheme that ensures dual protection of both retrieved content and vector embeddings, guaranteeing that only authorized entities can access sensitive data. Through rigorous formal security proofs, the framework verifies confidentiality and integrity under a computational security model. The approach overcomes limitations of heuristic filtering methods that suffer from limited interpretability and vulnerability to adaptive attacks. Extensive experiments across multiple benchmark datasets demonstrate effective resistance against state-of-the-art attacks. This work establishes a theoretical foundation for verifiably secure RAG systems, advancing AI-powered services toward formally guaranteed security.

**Key Contributions:** First provably secure RAG framework, formal security proofs, full-encryption scheme for content and embeddings

---

### 3. Zhao, D. (2024). FRAG: Toward Federated Vector Database Management for Collaborative and Secure Retrieval-Augmented Generation. *arXiv preprint arXiv:2410.13272*.

**Published:** October 17, 2024

This paper introduces Federated Retrieval-Augmented Generation (FRAG), a novel database management paradigm enabling mutually-distrusted parties to collaboratively perform Approximate k-Nearest Neighbor (ANN) searches on encrypted query vectors and encrypted data stored in distributed vector databases. FRAG addresses two critical challenges: ensuring strong security guarantees (IND-CPA) under practical assumptions without relying on non-collusion assumptions, and maintaining performance overheads comparable to traditional non-federated RAG systems. The framework employs a single-key homomorphic encryption protocol that simplifies key management across distrusted parties, along with a multiplicative caching technique for efficient floating-point encryption. Rigorous security proofs using standard cryptographic reductions validate the approach, while extensive experiments demonstrate practical scalability on both benchmark and real-world datasets.

**Key Contributions:** Federated RAG paradigm, homomorphic encryption for vector databases, multiplicative caching technique

---

### 4. Mu, Y., Hu, H., Li, F., Yuan, Q., Wu, J., Liu, Z., Liu, P., Wang, M., Zhou, H., & Liu, Y. (2026). Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks. *arXiv preprint arXiv:2603.21654*.

**Published:** March 23, 2026

This comprehensive survey presents the first end-to-end review dedicated exclusively to RAG system security. The authors systematically analyze vulnerability mechanisms across the RAG workflow and categorize core threat vectors including data poisoning, adversarial attacks, and membership inference attacks. The taxonomy of defense technologies spans both input and output stages: input-side protections include dynamic access control, homomorphic encryption retrieval, and adversarial pre-filtering; output-side techniques encompass federated learning isolation, differential privacy perturbation, and lightweight data sanitization. The paper consolidates authoritative test datasets, security standards, and evaluation frameworks to establish unified benchmarks for future research. By mapping the entire pipeline from threats to defenses to evaluation, this work provides foundational insights for developing robust and trustworthy next-generation RAG systems.

**Key Contributions:** First comprehensive RAG security survey, dual-perspective defense taxonomy, unified benchmark framework

---

### 5. Shih, Y.-K., & Kang, Y.-K. (2025). Design and Implementation of a Secure RAG-Enhanced AI Chatbot for Smart Tourism Customer Service: Defending Against Prompt Injection Attacks – A Case Study of Hsinchu, Taiwan. *arXiv preprint arXiv:2509.21367*.

**Published:** September 22, 2025

This case study presents the design and implementation of a secure RAG-enhanced chatbot for smart tourism services in Hsinchu, Taiwan. The system addresses prompt injection attacks through multi-layered defenses including API function calls, linguistic analysis across lexical, semantic, and pragmatic levels, and guardrails against injection attempts. Key architectural features include a tiered response strategy, RAG-driven knowledge grounding, intent decomposition, and reverse RAG text prioritization for verified data. Evaluation with 674 adversarial prompts and 223 benign queries demonstrated over 95% accuracy on benign tasks with substantial injection attack detection. Benchmarking against GPT-5 (released August 2025) revealed approximately 85% attack blocking rate, highlighting the necessity for layered defense strategies beyond base model robustness. The work contributes practical insights for sustainable tourism applications, multilingual accessibility, and ethical AI deployment.

**Key Contributions:** Real-world RAG security implementation, multi-layered prompt injection defense, smart tourism case study

---

### 6. Shi, J., & Zhang, T. (2025). RESCUE: Retrieval Augmented Secure Code Generation. *arXiv preprint arXiv:2510.18204*.

**Published:** October 21, 2025

RESCUE addresses the challenge of generating secure code using LLMs through a novel RAG framework with two key innovations. First, a hybrid knowledge base construction method combines LLM-assisted cluster-then-summarize distillation with program slicing, producing both high-level security guidelines and concise, security-focused code examples. Second, hierarchical multi-faceted retrieval traverses the constructed knowledge base from top to bottom, integrating multiple security-critical facts at each level to ensure comprehensive and accurate retrieval. Evaluation across four benchmarks with six LLMs demonstrates that RESCUE improves the SecurePass@1 metric by an average of 4.8 points, establishing new state-of-the-art performance for security. In-depth analysis and ablation studies rigorously validate the effectiveness of individual components, providing actionable insights for secure code generation systems.

**Key Contributions:** Hybrid knowledge base construction, hierarchical multi-faceted retrieval, state-of-the-art secure code generation

---

### 7. Lin, B., Wang, S., Qin, Y., Chen, L., & Mao, X. (2025). Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection. *arXiv preprint arXiv:2504.16429*.

**Published:** April 23, 2025

CodeGuarder presents a security-hardening framework for Retrieval-Augmented Code Generation (RACG) systems that shifts the paradigm from retrieving only functional code examples to incorporating both functional code and security knowledge. The framework constructs a security knowledge base from real-world vulnerability databases, including secure code samples and root cause annotations. For each code generation query, a retriever decomposes the query into fine-grained sub-tasks and fetches relevant security knowledge. A re-ranking and filtering mechanism leverages LLMs' susceptibility to different vulnerability types to prioritize critical security guidance. Evaluation demonstrates significant improvements: average security rate increases of 20.12% in standard RACG, and 31.53% and 21.91% under two distinct poisoning scenarios, without compromising functional correctness. Strong generalization is shown even when targeted language security knowledge is lacking.

**Key Contributions:** Security knowledge injection paradigm, vulnerability-aware re-ranking, poisoning-resistant code generation

---

### 8. Sriram, V., Pandita, S., Lakshmanan, A., Shamraj, A., & Saha, S. (2026). Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback. *arXiv preprint arXiv:2601.00509*.

**Published:** January 1, 2026

This work proposes a retrieval-augmented, multi-tool repair workflow for secure code generation. A single code-generating LLM iteratively refines outputs using compiler diagnostics, CodeQL security scanning, and KLEE symbolic execution feedback. A lightweight embedding model performs semantic retrieval of previously successful repairs, providing security-focused examples that guide generation. Evaluation on 3,242 programs generated by DeepSeek-Coder-1.3B and CodeLlama-7B demonstrates significant robustness improvements: 96% reduction in security vulnerabilities for DeepSeek, and critical security defect rate decrease from 58.55% to 22.19% for CodeLlama. The results highlight the efficacy of tool-assisted self-repair even on models resistant to conventional improvement methods, establishing a practical approach for iterative security enhancement.

**Key Contributions:** Multi-tool feedback integration, iterative self-repair workflow, embedding-based security example retrieval

---

### 9. Lu, Y., Tang, W., Johnson, M., Jung, T., & Jiang, M. (2025). A Decentralized Retrieval Augmented Generation System with Source Reliabilities Secured on Blockchain. *arXiv preprint arXiv:2511.07577*.

**Published:** November 10, 2025

This paper addresses the limitations of centralized RAG architectures through a decentralized system with blockchain-secured source reliability scoring. The novel reliability mechanism dynamically evaluates each data source based on response quality contributions and prioritizes high-quality sources during retrieval. Blockchain-based smart contracts ensure transparent and tamper-proof reliability records without central authority dependence. Evaluation with Llama models (3B and 8B) in simulated environments with varying source reliability demonstrates +10.7% performance improvement over centralized counterparts in unreliable data environments, approaching upper-bound centralized performance under ideal conditions. The decentralized infrastructure achieves approximately 56% marginal cost savings through batched update operations while enabling secure, trustworthy scoring management. The open-source system provides a foundation for privacy-preserving, cost-effective RAG deployments.

**Key Contributions:** Decentralized RAG architecture, blockchain-based reliability scoring, cost-efficient batched operations

---

### 10. Liang, X., Niu, S., Li, Z., Zhang, S., Wang, H., Xiong, F., Fan, Z., Tang, B., Song, S., Wang, M., & Yang, J. (2025). SafeRAG: Benchmarking Security in Retrieval-Augmented Generation of Large Language Model. *arXiv preprint arXiv:2501.18636*.

**Published:** January 28, 2025

SafeRAG introduces a comprehensive benchmark for evaluating RAG security across multiple attack vectors. The authors classify attack tasks into four categories: silver noise, inter-context conflict, soft ad, and white Denial-of-Service. A manually constructed SafeRAG dataset simulates various attack scenarios that RAG systems may encounter. Experiments conducted on 14 representative RAG components reveal significant vulnerabilities: even the most apparent attack tasks can easily bypass existing retrievers, filters, and advanced LLMs, resulting in degraded service quality. The benchmark provides a standardized evaluation framework for assessing RAG security posture and comparing defense mechanisms. By exposing systematic vulnerabilities across the RAG pipeline, this work motivates the development of more robust security measures and establishes baseline metrics for future improvements.

**Key Contributions:** Comprehensive RAG security benchmark, four-category attack taxonomy, systematic vulnerability assessment

---

## Thematic Analysis

### Defense Mechanisms

The reviewed literature reveals diverse defense strategies spanning multiple layers:

**Detection-Based Approaches:** RAGuard (Cheng et al., 2025) and CodeGuarder (Lin et al., 2025) employ sophisticated detection mechanisms using perplexity analysis, similarity filtering, and vulnerability-aware re-ranking to identify and mitigate threats before they impact generation.

**Encryption-Based Approaches:** Zhou et al. (2025) and Zhao (2024) establish formal security guarantees through cryptographic methods, with full-encryption schemes and homomorphic encryption enabling provably secure retrieval operations.

**Architecture-Based Approaches:** Decentralized systems (Lu et al., 2025) and federated frameworks (Zhao, 2024) redistribute trust assumptions, reducing single points of failure and enabling collaborative security.

### Code Security Applications

Four papers specifically address secure code generation (Shi & Zhang, 2025; Lin et al., 2025; Sriram et al., 2026), reflecting the critical importance of this application domain. Common strategies include:
- Hybrid knowledge bases combining guidelines and examples
- Multi-tool feedback integration (compiler, static analysis, symbolic execution)
- Hierarchical retrieval from abstract principles to concrete implementations
- Iterative refinement through security-focused feedback loops

### Benchmarking and Evaluation

The emergence of comprehensive benchmarks (Mu et al., 2026; Liang et al., 2025) indicates field maturation. SafeRAG's systematic vulnerability assessment reveals concerning gaps in current defenses, while Mu et al.'s unified framework consolidates evaluation standards across threat models, defense mechanisms, and performance metrics.

### Real-World Deployment

Shih and Kang's (2025) smart tourism case study demonstrates practical security considerations in production systems, highlighting the gap between theoretical robustness and real-world attack resistance. The 85% attack blocking rate of GPT-5 underscores the necessity for layered defense strategies beyond base model capabilities.

---

## Research Gaps and Future Directions

Based on this systematic review, several research gaps emerge:

1. **Adaptive Attack Evaluation:** While several papers claim resistance to adaptive attacks, comprehensive evaluation against truly adaptive adversaries remains limited.

2. **Cross-Domain Generalization:** Most defenses are evaluated in specific domains (code generation, tourism); transferability across application areas requires further investigation.

3. **Performance-Security Tradeoffs:** Quantitative analysis of security overhead versus system performance remains underexplored, particularly for encryption-based approaches.

4. **Human-in-the-Loop Security:** The role of human oversight and intervention in secure RAG systems receives limited attention despite its practical importance.

5. **Long-Term Reliability:** Blockchain-based reliability scoring (Lu et al., 2025) introduces novel mechanisms, but long-term stability and game-theoretic properties require deeper analysis.

---

## Conclusion

The literature on secure Retrieval-Augmented Generation from April 2024 to April 2026 demonstrates rapid advancement across theoretical foundations, practical defenses, and evaluation frameworks. The field has progressed from ad-hoc security measures to provably secure architectures with formal guarantees. Key trends include the integration of cryptographic methods, federated and decentralized approaches, and comprehensive benchmarking efforts.

However, significant challenges remain. The SafeRAG benchmark reveals persistent vulnerabilities across the RAG pipeline, while real-world deployments continue to struggle with sophisticated attack vectors. Future research should prioritize adaptive attack resistance, cross-domain generalization, and quantitative performance-security analysis to advance the state of secure RAG systems.

The convergence of security-focused code generation techniques, comprehensive threat taxonomies, and unified evaluation frameworks establishes a strong foundation for developing robust, trustworthy RAG systems capable of resisting evolving threats while maintaining practical utility.

---

## References

Cheng, Z., Sun, J., Gao, A., Quan, Y., Liu, Z., Hu, X., & Fang, M. (2025). Secure Retrieval-Augmented Generation against Poisoning Attacks. *arXiv preprint arXiv:2510.25025*. https://arxiv.org/abs/2510.25025v2

Liang, X., Niu, S., Li, Z., Zhang, S., Wang, H., Xiong, F., Fan, Z., Tang, B., Song, S., Wang, M., & Yang, J. (2025). SafeRAG: Benchmarking Security in Retrieval-Augmented Generation of Large Language Model. *arXiv preprint arXiv:2501.18636*. https://arxiv.org/abs/2501.18636v2

Lin, B., Wang, S., Qin, Y., Chen, L., & Mao, X. (2025). Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection. *arXiv preprint arXiv:2504.16429*. https://arxiv.org/abs/2504.16429v1

Lu, Y., Tang, W., Johnson, M., Jung, T., & Jiang, M. (2025). A Decentralized Retrieval Augmented Generation System with Source Reliabilities Secured on Blockchain. *arXiv preprint arXiv:2511.07577*. https://arxiv.org/abs/2511.07577v1

Mu, Y., Hu, H., Li, F., Yuan, Q., Wu, J., Liu, Z., Liu, P., Wang, M., Zhou, H., & Liu, Y. (2026). Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks. *arXiv preprint arXiv:2603.21654*. https://arxiv.org/abs/2603.21654v1

Shi, J., & Zhang, T. (2025). RESCUE: Retrieval Augmented Secure Code Generation. *arXiv preprint arXiv:2510.18204*. https://arxiv.org/abs/2510.18204v2

Shih, Y.-K., & Kang, Y.-K. (2025). Design and Implementation of a Secure RAG-Enhanced AI Chatbot for Smart Tourism Customer Service: Defending Against Prompt Injection Attacks – A Case Study of Hsinchu, Taiwan. *arXiv preprint arXiv:2509.21367*. https://arxiv.org/abs/2509.21367v1

Sriram, V., Pandita, S., Lakshmanan, A., Shamraj, A., & Saha, S. (2026). Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback. *arXiv preprint arXiv:2601.00509*. https://arxiv.org/abs/2601.00509v1

Zhao, D. (2024). FRAG: Toward Federated Vector Database Management for Collaborative and Secure Retrieval-Augmented Generation. *arXiv preprint arXiv:2410.13272*. https://arxiv.org/abs/2410.13272v1

Zhou, P., Feng, Y., & Yang, Z. (2025). Provably Secure Retrieval-Augmented Generation. *arXiv preprint arXiv:2508.01084*. https://arxiv.org/abs/2508.01084v1

---

**Review Completed:** October 26, 2026  
**Format:** APA 7th Edition  
**Total Papers Reviewed:** 10  
**Date Range:** April 9, 2024 – April 8, 2026  
**Category:** cs.CR (Cryptography and Security)
