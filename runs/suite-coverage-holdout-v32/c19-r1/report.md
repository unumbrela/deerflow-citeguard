# Systematic Literature Review: Secure Retrieval-Augmented Generation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "secure retrieval augmented generation", category cs.CR, published between 2024-04-09 and 2026-04-08
**Citation format**: APA 7th edition

## Executive Summary

The literature on secure Retrieval-Augmented Generation (RAG) has rapidly evolved between 2024-2026, with research concentrated on defending against poisoning attacks, establishing formal security guarantees, and enabling secure deployment in distributed environments. The surveyed papers collectively demonstrate that RAG systems face multifaceted security threats ranging from data poisoning and prompt injection to membership inference attacks. Researchers have responded with diverse defense mechanisms including non-parametric detection frameworks, cryptographic encryption schemes, blockchain-based decentralization, and comprehensive benchmarking initiatives. A notable trend is the shift from reactive defense to proactive security-hardening, with several papers proposing frameworks that integrate security knowledge directly into the retrieval and generation pipeline. The field is maturing toward systematic, end-to-end security analysis rather than isolated vulnerability studies.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "secure retrieval augmented generation", filtered to category cs.CR, published between 2024-04-09 and 2026-04-08. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Poisoning Attack Defense

A dominant research direction addresses data poisoning attacks, where adversaries inject malicious texts into RAG knowledge databases to manipulate model outputs. Cheng et al. (2025) introduced RAGuard, a non-parametric detection framework that expands retrieval scope to increase clean text proportion, then applies chunk-wise perplexity filtering and text similarity filtering to detect poisoned content. Their multi-stage filtering approach demonstrates effectiveness against strong adaptive attacks on large-scale datasets. Similarly, Lin et al. (2025) proposed CodeGuarder, which constructs a security knowledge base from real-world vulnerability databases and uses LLM-based re-ranking to prioritize critical security guidance, improving code security rates by 20.12% in standard RAG settings and up to 31.53% under poisoning scenarios. These works share a common strategy: rather than preventing retrieval of potentially malicious content, they focus on detection and filtering post-retrieval.

### Theme 2: Formal Security Guarantees

Moving beyond empirical defenses, recent work has established theoretically grounded security frameworks for RAG systems. Zhou et al. (2025) proposed SAG, the first provably secure framework employing pre-storage full-encryption for dual protection of retrieved content and vector embeddings. Their formal security proofs verify confidentiality and integrity under a computational security model, providing theoretical guarantees absent in prior empirical approaches. This represents a significant maturation of the field—shifting from ad-hoc defenses to cryptographically rigorous solutions with interpretable security guarantees. The framework's resistance to state-of-the-art attacks across multiple benchmarks demonstrates that formal security need not sacrifice practical effectiveness.

### Theme 3: Secure Code Generation

Several papers focus specifically on security in code generation contexts, recognizing that RAG-enhanced code synthesis introduces unique vulnerabilities. Shi and Zhang (2025) developed RESCUE, which addresses noise in security documents through hybrid knowledge base construction using LLM-assisted cluster-then-summarize distillation combined with program slicing. Their hierarchical multi-faceted retrieval traverses the knowledge base while integrating security-critical facts at each level, improving SecurePass@1 by 4.8 points over existing methods. Sriram et al. (2026) took a complementary approach, combining RAG with multi-tool feedback including compiler diagnostics, CodeQL security scanning, and KLEE symbolic execution, achieving a 96% reduction in security vulnerabilities for DeepSeek-Coder-1.3B. These works demonstrate that secure code generation requires both high-quality security knowledge retrieval and iterative verification through specialized analysis tools.

### Theme 4: Decentralized and Federated Architectures

Recognizing that centralized RAG systems create single points of failure and trust, researchers have explored decentralized alternatives. Zhao (2024) proposed FRAG, enabling mutually-distrusted parties to collaboratively perform approximate nearest neighbor searches on encrypted vectors using single-key homomorphic encryption. The system achieves Indistinguishability under Chosen-Plaintext Attack (IND-CPA) security while maintaining performance comparable to traditional non-federated RAG systems. Lu et al. (2025) developed a blockchain-based decentralized RAG system with a novel reliability scoring mechanism that dynamically evaluates sources based on response quality, achieving 10.7% performance improvement over centralized counterparts in unreliable data environments. These architectures address both security and trust concerns by distributing control and enabling transparent, verifiable operations through smart contracts.

### Theme 5: Comprehensive Security Surveys and Benchmarking

The field has matured to produce systematic surveys and benchmarks that consolidate fragmented knowledge. Mu et al. (2026) conducted the first end-to-end survey dedicated to RAG system security, categorizing core threat vectors (data poisoning, adversarial attacks, membership inference attacks) and constructing a taxonomy of defense technologies from input and output perspectives. Their work consolidates authoritative test datasets and evaluation frameworks, providing a unified reference absent in prior literature that isolated specific vulnerabilities. Liang et al. (2025) introduced SafeRAG, a benchmark classifying attack tasks into four categories: silver noise, inter-context conflict, soft ad, and white Denial-of-Service. Their experiments on 14 representative RAG components revealed that even apparent attack tasks can easily bypass existing retrievers, filters, and advanced LLMs, highlighting the field's vulnerability.

### Theme 6: Application-Specific Secure Deployments

Beyond general frameworks, researchers have demonstrated secure RAG implementations in specific application domains. Shih and Kang (2025) presented a case study of a RAG-enhanced AI chatbot for smart tourism in Hsinchu, Taiwan, integrating multi-layered linguistic analysis (lexical, semantic, pragmatic levels) with guardrails against prompt injection attacks. Their system achieved over 95% accuracy on benign tasks while substantially detecting prompt injection attacks, though even GPT-5 blocked only 85% of attacks, underscoring the need for layered defenses. This work illustrates how domain-specific requirements—such as multilingual accessibility and ethical AI deployment in tourism contexts—shape security architecture decisions.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that layered, multi-stage defenses are necessary for comprehensive RAG security. Both Cheng et al. (2025) and Shih and Kang (2025) employ multi-stage filtering or analysis, reflecting consensus that single-mechanism defenses are insufficient. There is also agreement that expanding retrieval scope or knowledge base quality improves security outcomes, as demonstrated by Cheng et al.'s scope expansion strategy and Lin et al.'s security knowledge injection approach. The literature uniformly recognizes that RAG's multi-module architecture introduces complex system-level vulnerabilities requiring end-to-end analysis rather than component-level fixes.

**Disagreements**: The papers diverge in their approach to trust assumptions. Zhou et al. (2025) and Zhao (2024) assume adversarial environments requiring cryptographic guarantees, while others like Shi and Zhang (2025) focus on improving retrieval quality without formal threat models. There is also tension between centralized optimization (e.g., RAGuard's detection framework) and decentralized architectures (e.g., Lu et al.'s blockchain system), reflecting different philosophies about where trust should reside. Additionally, while Mu et al. (2026) advocate for comprehensive taxonomies, the application-specific approach of Shih and Kang (2025) suggests that domain-tailored solutions may outperform general frameworks.

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. Most papers do not explicitly state limitations in their abstracts, suggesting either space constraints or insufficient critical reflection on approach boundaries. The literature lacks comprehensive evaluation across diverse attack scenarios—most frameworks are tested on specific attack types rather than adversarial ensembles. There is limited discussion of computational overhead: while Zhao (2024) and Lu et al. (2025) mention performance metrics, systematic analysis of security-performance tradeoffs remains absent. The field would benefit from standardized evaluation protocols that enable fair comparison across defense mechanisms. Finally, none of the papers address the human factors dimension—how end users interact with secure RAG systems and whether security measures introduce usability barriers that undermine adoption.

## Per-Paper Annotations

### Cheng et al. (2025)

**Research question**: How can Retrieval-Augmented Generation systems be protected against data poisoning attacks that inject malicious texts into knowledge databases?
**Methodology**: The authors introduce RAGuard, a non-parametric detection framework that expands retrieval scope to increase clean text proportion, then applies chunk-wise perplexity filtering to detect abnormal variations and text similarity filtering to flag highly similar texts.
**Key findings**:
- RAGuard effectively detects poisoned texts in RAG systems through a multi-stage filtering approach
- Expanding retrieval scope reduces the likelihood of retrieving poisoned content by increasing clean text proportion
- Chunk-wise perplexity filtering successfully identifies abnormal variations indicative of poisoned content
- Text similarity filtering effectively flags highly similar texts that may indicate poisoning attacks
- The framework demonstrates effectiveness against strong adaptive attacks on large-scale datasets
**Limitations**: The abstract does not explicitly state limitations of the approach; it focuses on demonstrating effectiveness across datasets and attack types.

### Zhou et al. (2025)

**Research question**: How can RAG systems achieve formal security guarantees with interpretability and resistance to adaptive attacks?
**Methodology**: The paper proposes SAG, the first provably secure framework for RAG systems, employing a pre-storage full-encryption scheme for dual protection of retrieved content and vector embeddings, with formal security proofs verifying confidentiality and integrity under a computational security model.
**Key findings**:
- SAG provides the first formally provable security framework for RAG systems with theoretical guarantees
- Pre-storage full-encryption ensures dual protection of both retrieved content and vector embeddings
- Only authorized entities can access encrypted data, ensuring confidentiality
- Formal security proofs rigorously verify the scheme's confidentiality and integrity
- Experiments across multiple benchmark datasets demonstrate effective resistance against state-of-the-art attacks
**Limitations**: The abstract does not explicitly discuss limitations; it emphasizes the theoretical foundation and practical paradigm established for verifiably secure RAG systems.

### Mu et al. (2026)

**Research question**: What are the comprehensive security vulnerabilities, threat vectors, and defense mechanisms across the entire RAG system pipeline?
**Methodology**: This paper conducts a systematic end-to-end survey analyzing RAG workflow vulnerabilities, categorizing core threat vectors (data poisoning, adversarial attacks, membership inference attacks), and constructing a taxonomy of defense technologies from input and output perspectives, while consolidating authoritative test datasets and evaluation frameworks.
**Key findings**:
- RAG's multi-module architecture introduces complex system-level security vulnerabilities across the entire pipeline
- Core threat vectors include data poisoning, adversarial attacks, and membership inference attacks
- Input-side defenses include dynamic access control, homomorphic encryption retrieval, and adversarial pre-filtering
- Output-side defenses include federated learning isolation, differential privacy perturbation, and lightweight data sanitization
- This is the first end-to-end survey dedicated to RAG system security, systematically mapping threats, defenses, and evaluation benchmarks
**Limitations**: As a comprehensive review paper, the abstract does not state specific limitations; it positions itself as distinct from existing literature that isolates specific vulnerabilities rather than providing unified analysis.

### Zhao (2024)

**Research question**: How can mutually-distrusted parties collaboratively perform ANN searches on encrypted vectors in distributed databases while maintaining strong security guarantees and practical performance?
**Methodology**: FRAG employs a single-key homomorphic encryption protocol to simplify key management across mutually-distrusted parties and introduces multiplicative caching technique to efficiently encrypt floating-point numbers, with rigorous security proofs using standard cryptographic reductions and extensive experiments on benchmark and real-world datasets.
**Key findings**:
- FRAG enables collaborative ANN searches on encrypted query vectors and data without any party gaining knowledge about others' queries or data
- Single-key homomorphic encryption simplifies key management while avoiding overly optimistic assumptions like non-collusion among parties
- Multiplicative caching technique significantly improves computational performance for encrypting floating-point numbers in large-scale federated environments
- Security guarantees include Indistinguishability under Chosen-Plaintext Attack (IND-CPA) under practical assumptions
- Experiments demonstrate practical scalability and efficiency comparable to traditional non-federated RAG systems
**Limitations**: The abstract does not explicitly state limitations; it emphasizes achieving performance overheads comparable to traditional systems while maintaining strong security guarantees.

### Shih and Kang (2025)

**Research question**: How can secure RAG chatbots for smart tourism be designed and implemented to defend against prompt injection attacks while maintaining high contextual awareness?
**Methodology**: The paper presents a case study implementing a secure RAG chatbot for Hsinchu smart tourism that integrates RAG with API function calls, multi-layered linguistic analysis (lexical, semantic, pragmatic levels), and guardrails against injections, with defense mechanisms including system norms, gatekeepers for intent judgment, and reverse RAG text prioritization, benchmarked against a GPT-5 variant.
**Key findings**:
- The system achieves over 95% accuracy on benign tasks while substantially detecting prompt injection attacks
- Multi-layered linguistic analysis across lexical, semantic, and pragmatic levels enables high contextual awareness
- Tiered response strategy with RAG-driven knowledge grounding and intent decomposition enhances security
- GPT-5 blocked approximately 85% of attacks, showing progress but highlighting the need for layered defenses
- The framework contributes to sustainable tourism, multilingual accessibility, and ethical AI deployment in smart tourism contexts
**Limitations**: The abstract indicates that even GPT-5's 85% attack blocking rate highlights the need for layered defenses, suggesting that inherent model robustness alone is insufficient for complete protection against prompt injection attacks.

### Shi and Zhang (2025)

**Research question**: How can Retrieval-Augmented Generation be improved to enhance secure code generation by addressing noise in security documents and overlooked security semantics in task descriptions?
**Methodology**: The authors propose RESCUE, a RAG framework with two innovations: (1) hybrid knowledge base construction using LLM-assisted cluster-then-summarize distillation combined with program slicing, and (2) hierarchical multi-faceted retrieval that traverses the knowledge base while integrating security-critical facts at each level. The framework was evaluated on four benchmarks comparing against five state-of-the-art methods across six LLMs.
**Key findings**:
- RESCUE improves the SecurePass@1 metric by an average of 4.8 points over existing methods
- The framework establishes new state-of-the-art performance for secure code generation
- Hybrid knowledge base construction produces both high-level security guidelines and concise, security-focused code examples
- Hierarchical multi-faceted retrieval ensures comprehensive and accurate retrieval of security knowledge
- Ablation studies validated the effectiveness of individual components in the RESCUE framework
**Limitations**: Not stated in abstract.

### Lu et al. (2025)

**Research question**: How can a decentralized RAG system be designed to enable data owners to maintain control over their sources while addressing the challenge of varying source reliability?
**Methodology**: The authors developed a decentralized RAG system with a novel reliability scoring mechanism that dynamically evaluates each source based on response quality and prioritizes high-quality sources during retrieval. The scoring process is managed through blockchain-based smart contracts to ensure transparency and trust. The system was evaluated using two Llama models (3B and 8B) in two simulated environments with six data sources of different reliability levels.
**Key findings**:
- The decentralized system achieves a +10.7% performance improvement over centralized counterparts in unreliable data environments
- Performance approaches the upper-bound of centralized systems under ideally reliable data conditions
- Blockchain-based scoring management achieves approximately 56% marginal cost savings through batched update operations
- The reliability scoring mechanism effectively prioritizes high-quality sources during retrieval
- The system enables secure and trustworthy scoring management without relying on a central authority
**Limitations**: Not stated in abstract.

### Sriram et al. (2026)

**Research question**: How can retrieval-augmented generation combined with multi-tool feedback improve the security and correctness of LLM-generated code?
**Methodology**: The authors propose a retrieval-augmented, multi-tool repair workflow where a single code-generating LLM iteratively refines outputs using compiler diagnostics, CodeQL security scanning, and KLEE symbolic execution. A lightweight embedding model performs semantic retrieval of previously successful repairs to provide security-focused examples. The system was evaluated on 3,242 programs generated by DeepSeek-Coder-1.3B and CodeLlama-7B.
**Key findings**:
- Security vulnerabilities were reduced by 96% for DeepSeek-Coder-1.3B
- For CodeLlama-7B, critical security defect rate decreased from 58.55% to 22.19%
- Tool-assisted self-repair proves effective even on 'stubborn' models
- Semantic retrieval of successful repairs provides effective security-focused guidance
- The combined approach of compiler diagnostics, CodeQL, and KLEE symbolic execution significantly improves robustness
**Limitations**: Not stated in abstract.

### Liang et al. (2025)

**Research question**: How vulnerable is Retrieval-Augmented Generation to various attack tasks that manipulate external knowledge, and how can these vulnerabilities be benchmarked?
**Methodology**: The authors introduce SafeRAG, a benchmark that classifies attack tasks into four categories: silver noise, inter-context conflict, soft ad, and white Denial-of-Service. They constructed a RAG security evaluation dataset primarily manually for each attack task and used it to simulate various attack scenarios. Experiments were conducted on 14 representative RAG components to evaluate vulnerability.
**Key findings**:
- RAG exhibits significant vulnerability to all four attack task categories
- Even the most apparent attack tasks can easily bypass existing retrievers, filters, and advanced LLMs
- Attack tasks result in degradation of RAG service quality
- The SafeRAG dataset provides a comprehensive benchmark for evaluating RAG security
- Incorporation of external and unverified knowledge increases LLM vulnerability to manipulation
**Limitations**: Not stated in abstract.

### Lin et al. (2025)

**Research question**: How can Retrieval-Augmented Code Generation systems be hardened against security threats, particularly malicious code poisoning in knowledge bases?
**Methodology**: The authors propose CodeGuarder, a security-hardening framework that constructs a security knowledge base from real-world vulnerability databases including secure code samples and root cause annotations. For each query, a retriever decomposes it into fine-grained sub-tasks and fetches relevant security knowledge, with a re-ranking and filtering mechanism leveraging LLMs' susceptibility to different vulnerability types to prioritize critical security guidance.
**Key findings**:
- CodeGuarder improves code security rates by 20.12% in standard RACG settings
- Under two distinct poisoning scenarios, improvements of 31.53% and 21.91% were achieved
- The framework maintains functional correctness while improving security
- CodeGuarder demonstrates strong generalization, enhancing security even when targeted language security knowledge is lacking
- Shifting from retrieving only functional code to incorporating security knowledge significantly reduces risks
**Limitations**: Not stated in abstract.

## References

Cheng, Z., Sun, J., Gao, A., Quan, Y., Liu, Z., Hu, X., & Fang, M. (2025). Secure retrieval-augmented generation against poisoning attacks. arXiv. https://arxiv.org/abs/2510.25025

Liang, X., Niu, S., Li, Z., Zhang, Z., Wang, H., Xiong, F., Fan, J. Z., Tang, B., Song, S., Wang, M., & Yang, J. (2025). SafeRAG: Benchmarking security in retrieval-augmented generation of large language model. arXiv. https://arxiv.org/abs/2501.18636

Lin, B., Wang, S., Qin, Y., Chen, L., & Mao, X. (2025). Give LLMs a security course: Securing retrieval-augmented code generation via knowledge injection. arXiv. https://arxiv.org/abs/2504.16429

Lu, Y., Tang, W., Johnson, M., Jung, T., & Jiang, M. (2025). A decentralized retrieval augmented generation system with source reliabilities secured on blockchain. arXiv. https://arxiv.org/abs/2511.07577

Mu, Y., Hu, H., Li, F., Yuan, Q., Wu, J., Liu, Z., Liu, P., Wang, M., Zhou, H., & Liu, Y. (2026). Towards secure retrieval-augmented generation: A comprehensive review of threats, defenses and benchmarks. arXiv. https://arxiv.org/abs/2603.21654

Shi, J., & Zhang, T. (2025). RESCUE: Retrieval augmented secure code generation. arXiv. https://arxiv.org/abs/2510.18204

Shih, Y.-K., & Kang, Y.-K. (2025). Design and implementation of a secure RAG-enhanced AI chatbot for smart tourism customer service: Defending against prompt injection attacks -- A case study of Hsinchu, Taiwan. arXiv. https://arxiv.org/abs/2509.21367

Sriram, V., Pandita, S., Lakshmanan, A., Shamraj, A., & Saha, S. (2026). Improving LLM-assisted secure code generation through retrieval-augmented-generation and multi-tool feedback. arXiv. https://arxiv.org/abs/2601.00509

Zhao, D. (2024). FRAG: Toward federated vector database management for collaborative and secure retrieval-augmented generation. arXiv. https://arxiv.org/abs/2410.13272

Zhou, P., Feng, Y., & Yang, Z. (2025). Provably secure retrieval-augmented generation. arXiv. https://arxiv.org/abs/2508.01084
