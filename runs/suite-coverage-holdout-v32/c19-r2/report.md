# Systematic Literature Review: Secure Retrieval-Augmented Generation

**Review Period:** April 9, 2024 – April 8, 2026  
**Category:** cs.CR (Computer Security and Cryptography)  
**Total Papers Reviewed:** 10  
**Date of Review:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in secure Retrieval-Augmented Generation (RAG) systems. The reviewed literature reveals a rapidly evolving field addressing critical security challenges including data poisoning attacks, privacy preservation, adversarial vulnerabilities, and secure code generation. Research trends indicate a shift from heuristic defenses toward formally verified security guarantees, decentralized architectures, and comprehensive benchmarking frameworks.

---

## Thematic Analysis

### 1. Poisoning Attack Defense Mechanisms

**Cheng et al. (2025)** introduced RAGuard, a detection framework designed to identify poisoned texts in RAG knowledge databases. The system employs a non-parametric approach combining retrieval scope expansion, chunk-wise perplexity filtering, and text similarity filtering. Experimental validation on large-scale datasets demonstrated effectiveness against advanced adaptive attacks.

**Mu et al. (2026)** provided the first end-to-end survey dedicated to RAG security, systematically categorizing threat vectors including data poisoning, adversarial attacks, and membership inference attacks. Their taxonomy organizes defense technologies from dual input-output perspectives, reviewing mechanisms such as dynamic access control, homomorphic encryption retrieval, and differential privacy perturbation.

### 2. Provably Secure Frameworks

**Zhou et al. (2025)** proposed SAG, the first provably secure framework for RAG systems. The framework employs pre-storage full-encryption schemes ensuring dual protection of retrieved content and vector embeddings. Formal security proofs rigorously verify confidentiality and integrity under computational security models, establishing theoretical foundations for verifiably secure RAG systems.

**Zhao (2024)** introduced Federated Retrieval-Augmented Generation (FRAG), enabling mutually-distrusted parties to collaboratively perform Approximate k-Nearest Neighbor searches on encrypted query vectors and data. The system employs single-key homomorphic encryption with multiplicative caching techniques, achieving IND-CPA security guarantees while maintaining performance comparable to traditional RAG systems.

### 3. Secure Code Generation Applications

**Shi & Zhang (2025)** developed RESCUE, a RAG framework for secure code generation featuring hybrid knowledge base construction and hierarchical multi-faceted retrieval. The system combines LLM-assisted cluster-then-summarize distillation with program slicing, improving SecurePass@1 metrics by an average of 4.8 points across four benchmarks.

**Lin et al. (2025)** proposed CodeGuarder, a security-hardening framework that incorporates both functional code and security knowledge into retrieval-augmented code generation. The system constructs security knowledge bases from real-world vulnerability databases, achieving average security rate improvements of 20.12% in standard RACG and 31.53% under poisoning scenarios.

**Sriram et al. (2026)** presented a retrieval-augmented, multi-tool repair workflow integrating compiler diagnostics, CodeQL security scanning, and KLEE symbolic execution. Evaluation on 3,242 programs demonstrated 96% reduction in security vulnerabilities for DeepSeek-Coder and reduction of critical security defect rates from 58.55% to 22.19% for CodeLlama-7B.

### 4. Practical Implementation Case Studies

**Shih & Kang (2025)** documented the design and implementation of a secure RAG-enhanced AI chatbot for smart tourism customer service in Hsinchu, Taiwan. The system integrates multi-layered linguistic analysis, guardrails against prompt injection attacks, and tiered response strategies. Evaluations with 674 adversarial prompts showed over 95% accuracy on benign tasks and substantial detection of injection attacks.

### 5. Decentralized and Blockchain-Secured Architectures

**Lu et al. (2025)** developed a decentralized RAG system with novel reliability scoring mechanisms secured through blockchain-based smart contracts. The system dynamically evaluates source reliability based on response quality, achieving +10.7% performance improvement over centralized counterparts in unreliable data environments with approximately 56% marginal cost savings.

### 6. Security Benchmarking and Evaluation

**Liang et al. (2025)** introduced SafeRAG, a comprehensive benchmark for evaluating RAG security. The framework classifies attack tasks into silver noise, inter-context conflict, soft ad, and white Denial-of-Service categories. Experiments on 14 representative RAG components revealed significant vulnerabilities across all attack categories, with even apparent attacks bypassing existing retrievers, filters, and advanced LLMs.

---

## References (APA Format)

Cheng, Z., Sun, J., Gao, A., Quan, Y., Liu, Z., Hu, X., & Fang, M. (2025). Secure Retrieval-Augmented Generation against Poisoning Attacks. *arXiv preprint arXiv:2510.25025*. https://arxiv.org/abs/2510.25025v2

Zhao, D. (2024). FRAG: Toward Federated Vector Database Management for Collaborative and Secure Retrieval-Augmented Generation. *arXiv preprint arXiv:2410.13272*. https://arxiv.org/abs/2410.13272v1

Liang, X., Niu, S., Li, Z., Zhang, S., Wang, H., Xiong, F., Zhaoxin Fan, J., Tang, B., Song, S., Wang, M., & Yang, J. (2025). SafeRAG: Benchmarking Security in Retrieval-Augmented Generation of Large Language Model. *arXiv preprint arXiv:2501.18636*. https://arxiv.org/abs/2501.18636v2

Lin, B., Wang, S., Qin, Y., Chen, L., & Mao, X. (2025). Give LLMs a Security Course: Securing Retrieval-Augmented Code Generation via Knowledge Injection. *arXiv preprint arXiv:2504.16429*. https://arxiv.org/abs/2504.16429v1

Zhou, P., Feng, Y., & Yang, Z. (2025). Provably Secure Retrieval-Augmented Generation. *arXiv preprint arXiv:2508.01084*. https://arxiv.org/abs/2508.01084v1

Shih, Y.-K., & Kang, Y.-K. (2025). Design and Implementation of a Secure RAG-Enhanced AI Chatbot for Smart Tourism Customer Service: Defending Against Prompt Injection Attacks -- A Case Study of Hsinchu, Taiwan. *arXiv preprint arXiv:2509.21367*. https://arxiv.org/abs/2509.21367v1

Shi, J., & Zhang, T. (2025). RESCUE: Retrieval Augmented Secure Code Generation. *arXiv preprint arXiv:2510.18204*. https://arxiv.org/abs/2510.18204v2

Lu, Y., Tang, W., Johnson, M., Jung, T., & Jiang, M. (2025). A Decentralized Retrieval Augmented Generation System with Source Reliabilities Secured on Blockchain. *arXiv preprint arXiv:2511.07577*. https://arxiv.org/abs/2511.07577v1

Sriram, V., Pandita, S., Lakshmanan, A., Shamraj, A., & Saha, S. (2026). Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback. *arXiv preprint arXiv:2601.00509*. https://arxiv.org/abs/2601.00509v1

Mu, Y., Hu, H., Li, F., Yuan, Q., Wu, J., Liu, Z., Liu, P., Wang, M., Zhou, H., & Liu, Y. (2026). Towards Secure Retrieval-Augmented Generation: A Comprehensive Review of Threats, Defenses and Benchmarks. *arXiv preprint arXiv:2603.21654*. https://arxiv.org/abs/2603.21654v1

---

## Key Findings and Research Gaps

### Consolidated Findings

1. **Security Vulnerability Prevalence**: All reviewed studies confirm that RAG systems exhibit significant vulnerabilities to various attack vectors, particularly data poisoning and prompt injection attacks.

2. **Defense Evolution**: The field is transitioning from heuristic filtering approaches toward formally verified security guarantees with cryptographic foundations.

3. **Application-Specific Solutions**: Secure code generation has emerged as a critical application domain, with multiple specialized frameworks demonstrating substantial security improvements.

4. **Decentralization Benefits**: Blockchain-secured decentralized architectures show promise in addressing privacy concerns and reducing operational costs while improving reliability.

5. **Benchmarking Necessity**: The introduction of SafeRAG and comprehensive surveys highlights the field's maturation toward standardized evaluation frameworks.

### Identified Research Gaps

1. **Real-World Deployment Validation**: Most studies rely on benchmark datasets; longitudinal studies of deployed systems remain limited.

2. **Cross-Domain Generalization**: Security solutions developed for code generation may not transfer effectively to other domains such as healthcare or legal applications.

3. **Adaptive Attack Resistance**: While several frameworks claim resistance to adaptive attacks, comprehensive red-team evaluations are scarce.

4. **Performance-Security Trade-offs**: Quantitative analysis of security overhead impacts on RAG system latency and throughput requires further investigation.

5. **Regulatory Compliance**: Alignment with emerging AI security regulations and standards remains underexplored in the technical literature.

---

## Conclusion

The systematic review reveals a vibrant research community actively addressing critical security challenges in RAG systems. The convergence of cryptographic methods, decentralized architectures, and application-specific solutions indicates a maturing field moving toward production-ready secure RAG deployments. Future research should prioritize real-world validation, cross-domain applicability, and regulatory alignment to ensure trustworthy AI systems at scale.
