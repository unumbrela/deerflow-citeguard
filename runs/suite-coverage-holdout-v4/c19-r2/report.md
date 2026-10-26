# Systematic Literature Review: Secure Retrieval-Augmented Generation

**Review Period:** April 9, 2024 – April 8, 2026  
**Category:** cs.CR (Cryptography and Security)  
**Format:** APA Style  
**Date of Review:** October 26, 2026

---

## Executive Summary

This systematic literature review examines 10 peer-reviewed papers published between April 2024 and April 2026 focusing on security vulnerabilities, attack vectors, and defense mechanisms in Retrieval-Augmented Generation (RAG) systems. The review reveals a rapidly evolving threat landscape with sophisticated attack methodologies including knowledge base poisoning, backdoor attacks, denial-of-service through blocker documents, and data extraction attacks. The papers collectively demonstrate that RAG systems face critical security challenges that require urgent attention in both design and deployment phases.

---

## Methodology

### Search Strategy
- **Database:** arXiv preprint repository
- **Category:** cs.CR (Cryptography and Security)
- **Time Window:** April 9, 2024 – April 8, 2026
- **Search Query:** "secure retrieval-augmented generation"
- **Initial Pool:** 50 papers identified
- **Reference Expansion:** 31 additional papers from citation analysis
- **Shortlist:** 30 papers screened
- **Final Selection:** 10 papers based on relevance to RAG security

### Inclusion Criteria
1. Focus on security, privacy, or trust aspects of RAG systems
2. Published within the specified date range
3. Primary category cs.CR
4. Empirical evaluation of attacks or defenses
5. Novel contribution to RAG security understanding

---

## Selected Papers (APA Format)

### 1. Jamming and Denial-of-Service Attacks

**Shafran, A., Schuster, R., & Shmatikov, V. (2024).** Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents. *arXiv preprint arXiv:2406.05870*. https://arxiv.org/abs/2406.05870v4

**Key Contributions:**
- Demonstrated denial-of-service attacks through "blocker documents" that prevent RAG systems from answering specific queries
- Developed black-box optimization methods that do not require knowledge of embedding models or LLMs
- Showed that existing safety metrics do not capture vulnerability to jamming attacks
- Achieved high efficacy across multiple embedding and LLM configurations

**Impact:** 12 citations

---

### 2. Deceptive Content Injection

**Tan, Z., Zhao, C., Moraffah, R., Li, Y., Wang, S., Li, J., Chen, T., & Liu, H. (2024).** "Glue pizza and eat rocks" -- Exploiting Vulnerabilities in Retrieval-Augmented Generative Models. *arXiv preprint arXiv:2406.19417*. https://arxiv.org/abs/2406.19417v1

**Key Contributions:**
- Demonstrated adversaries can exploit open knowledge bases by injecting deceptive content
- Targeted realistic settings where adversaries lack knowledge of queries, knowledge base data, and LLM parameters
- Showed successful exploitation through crafted content uploads with retriever access
- Emphasized critical need for security measures in publicly accessible RAG systems

**Impact:** 9 citations

---

### 3. Trigger-Based Response Manipulation

**Xue, J., Zheng, M., Hu, Y., Liu, F., Chen, X., & Lou, Q. (2024).** BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models. *arXiv preprint arXiv:2406.00083*. https://arxiv.org/abs/2406.00083v3

**Key Contributions:**
- Unveiled threat where attackers steer RAG responses by injecting malicious passages
- BadRAG operates by optimizing passages to retrieve exclusively when trigger words appear
- Achieved adversarial objectives including denial of service, sentiment manipulation, context leakage, and tool misuse
- Demonstrated 98.2% retrieval success rate with only 10 malicious passages (0.04% of external corpora)
- Increased negative response rates from 0.22% to 72% for queries containing triggers

**Impact:** 7 citations

---

### 4. Backdoor Attacks via RAG

**Cheng, P., Ding, Y., Ju, T., Wu, Z., Du, W., Yi, P., Zhang, Z., & Liu, G. (2024).** TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models. *arXiv preprint arXiv:2405.13401*. https://arxiv.org/abs/2405.13401v4

**Key Contributions:**
- Proposed joint backdoor attack in RAG to manipulate LLMs in universal attack scenarios
- Used contrastive learning to orthogonally optimize backdoor shortcuts
- Introduced knowledge graphs for structured data to achieve fine-grained hard matching
- Improved recall of target contexts while maintaining retrieval capabilities on normal queries
- Demonstrated versatility threats across truthfulness, language understanding, and harmfulness metrics

**Impact:** 6 citations

---

### 5. Retrieval Prompt Hijacking

**Zhang, Y., Li, Q., Du, T., Zhang, X., Zhao, X., Feng, Z., & Yin, J. (2024).** HijackRAG: Hijacking Attacks against Retrieval-Augmented Large Language Models. *arXiv preprint arXiv:2410.22832*. https://arxiv.org/abs/2410.22832v1

**Key Contributions:**
- Revealed retrieval prompt hijack attack enabling manipulation of RAG retrieval mechanisms
- Formalized HijackRAG as optimization problem with black-box and white-box strategies
- Achieved high attack success rates across multiple benchmark datasets
- Demonstrated transferability across different retriever models
- Showed existing defense mechanisms are insufficient against HijackRAG

**Impact:** 5 citations

---

### 6. Escalated Data Extraction and Worms

**Cohen, S., Bitton, R., & Nassi, B. (2024).** Unleashing Worms and Extracting Data: Escalating the Outcome of Attacks against RAG-based Inference in Scale and Severity Using Jailbreaking. *arXiv preprint arXiv:2409.08045*. https://arxiv.org/abs/2409.08045v1

**Key Contributions:**
- Demonstrated escalation of membership inference and entity extraction to full document extraction attacks
- Achieved 80%-99.8% data extraction from RAG databases
- Crafted adversarial self-replicating prompts triggering computer worm chain reactions
- Compromised entire GenAI ecosystems through propagation across applications
- Evaluated worm performance in email assistant ecosystems with multi-hop propagation

**Impact:** 5 citations

---

### 7. General Backdoor Poisoning Framework

**Chaudhari, H., Severi, G., Abascal, J., Suri, A., Jagielski, M., Choquette-Choo, C. A., Nasr, M., Nita-Rotaru, C., & Oprea, A. (2024).** Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation. *arXiv preprint arXiv:2405.20485*. https://arxiv.org/abs/2405.20485v3

**Key Contributions:**
- Proposed Phantom, a two-stage optimization framework for backdoor poisoning attacks
- Crafted malicious documents retrieved only when specific trigger sequences appear
- Induced adversarial objectives including refusal to answer, reputation damage, privacy violations, and harmful behaviors
- Demonstrated attacks on Gemma, Vicuna, Llama, GPT-3.5 Turbo, and GPT-4
- Successfully attacked NVIDIA's "Chat with RTX" production RAG system

**Impact:** 4 citations

---

### 8. Privacy-Preserving Synthetic Data

**Zeng, S., Zhang, J., He, P., Ren, J., Zheng, T., Lu, H., Xu, H., Liu, H., Xing, Y., & Tang, J. (2024).** Mitigating the Privacy Issues in Retrieval-Augmented Generation (RAG) via Pure Synthetic Data. *arXiv preprint arXiv:2406.14773*. https://arxiv.org/abs/2406.14773v2

**Key Contributions:**
- Proposed SAGE, a two-stage synthetic data generation paradigm for privacy preservation
- Stage-1: Attribute-based extraction and generation to preserve key contextual information
- Stage-2: Agent-based iterative refinement to enhance privacy properties
- Achieved comparable performance to original data while substantially reducing privacy risks
- First work investigating high-utility privacy-preserving synthetic data for RAG

**Impact:** 4 citations

---

### 9. Knowledge Base Poisoning in Code Generation

**Lin, B., Wang, S., Chen, L., & Mao, X. (2025).** Exploring the Security Threats of Knowledge Base Poisoning in Retrieval-Augmented Code Generation. *arXiv preprint arXiv:2502.03233*. https://arxiv.org/abs/2502.03233v1

**Key Contributions:**
- First comprehensive study on security risks in Retrieval-Augmented Code Generation (RACG)
- Investigated how vulnerable code in knowledge bases compromises generated code security
- Evaluated four major LLMs, two retrievers, and two poisoning scenarios
- Found single poisoned code example can compromise up to 48% of generated code
- Provided practical mitigation recommendations for improving LLM-generated code security

**Impact:** 3 citations

---

### 10. Poisoning Attack Traceback System

**Zhang, B., Xin, H., Fang, M., Liu, Z., Yi, B., Li, T., & Liu, Z. (2025).** Traceback of Poisoning Attacks to Retrieval-Augmented Generation. *arXiv preprint arXiv:2504.21668*. https://arxiv.org/abs/2504.21668v2

**Key Contributions:**
- Introduced RAGForensics, the first traceback system for identifying poisoned texts in RAG
- Operates iteratively: retrieves subset of texts, uses crafted prompts to detect poisoning
- Addresses insufficiency of existing inference-time mitigation defenses
- Demonstrated effectiveness against state-of-the-art poisoning attacks across multiple datasets
- Pioneered traceback mechanisms for enhancing RAG system security

**Impact:** 3 citations

---

## Thematic Analysis

### Attack Vectors Identified

1. **Knowledge Base Poisoning** (6 papers)
   - Malicious document injection (Shafran et al., 2024; Tan et al., 2024; Xue et al., 2024)
   - Trigger-based manipulation (Xue et al., 2024; Cheng et al., 2024; Chaudhari et al., 2024)
   - Vulnerable code injection in RACG (Lin et al., 2025)

2. **Backdoor Attacks** (3 papers)
   - TrojanRAG joint backdoor optimization (Cheng et al., 2024)
   - Phantom framework for general backdoor poisoning (Chaudhari et al., 2024)
   - Contrastive learning for shortcut optimization (Cheng et al., 2024)

3. **Denial-of-Service** (2 papers)
   - Blocker document jamming (Shafran et al., 2024)
   - Refusal-to-answer induction (Xue et al., 2024; Chaudhari et al., 2024)

4. **Data Extraction** (1 paper)
   - Escalated extraction attacks achieving 80%-99.8% success (Cohen et al., 2024)
   - Self-replicating worms for ecosystem-wide compromise (Cohen et al., 2024)

5. **Retrieval Hijacking** (1 paper)
   - Prompt hijacking for predetermined answer generation (Zhang et al., 2024)
   - Transferable attacks across retriever models (Zhang et al., 2024)

### Defense Mechanisms Proposed

1. **Synthetic Data Generation**
   - SAGE framework for privacy-preserving retrieval (Zeng et al., 2024)
   - Two-stage attribute extraction and iterative refinement

2. **Traceback and Attribution**
   - RAGForensics for identifying poisoned texts (Zhang et al., 2025)
   - Iterative detection using crafted prompts

3. **Guardrails and Mitigation**
   - Analysis of existing guardrails (Cohen et al., 2024)
   - Practical recommendations for RACG security (Lin et al., 2025)

### Key Findings

1. **Vulnerability Prevalence:** All reviewed papers demonstrate significant vulnerabilities in current RAG implementations, with attack success rates ranging from 48% to 99.8%.

2. **Black-Box Feasibility:** Multiple attacks (Shafran et al., 2024; Tan et al., 2024; Chaudhari et al., 2024) succeed without knowledge of target system internals, making them broadly applicable.

3. **Minimal Resource Requirements:** Attacks require minimal resources—as few as 10 malicious passages (0.04% of corpus) can achieve 98.2% retrieval success (Xue et al., 2024).

4. **Transferability:** Attacks transfer across different models and retrievers (Zhang et al., 2024; Chaudhari et al., 2024), indicating systemic vulnerabilities.

5. **Production System Vulnerability:** Successful attacks demonstrated on production systems including NVIDIA's "Chat with RTX" (Chaudhari et al., 2024).

6. **Ecosystem-Wide Threats:** Self-replicating worms can compromise entire GenAI ecosystems through chain reactions (Cohen et al., 2024).

7. **Defense Insufficiency:** Existing defenses are consistently reported as insufficient against sophisticated attacks (Zhang et al., 2024; Cohen et al., 2024).

---

## Research Gaps and Future Directions

1. **Real-Time Detection:** Need for runtime monitoring systems to detect poisoning attempts during retrieval.

2. **Robust Embedding Models:** Development of embedding models resistant to adversarial document injection.

3. **Formal Verification:** Application of formal methods to verify RAG system security properties.

4. **Standardized Benchmarks:** Creation of standardized benchmarks for evaluating RAG security.

5. **Privacy-Utility Tradeoffs:** Further research on optimizing the balance between privacy preservation and retrieval quality (Zeng et al., 2024).

6. **Attribution Mechanisms:** Expansion of traceback capabilities beyond RAGForensics (Zhang et al., 2025).

7. **Multi-Modal RAG Security:** Investigation of security issues in multi-modal RAG systems combining text, images, and other media.

---

## Conclusion

The systematic review reveals that RAG systems face severe and diverse security threats that are both practical and scalable. The literature demonstrates a concerning gap between attack sophistication and defense capabilities. While recent work has begun addressing traceback (Zhang et al., 2025) and privacy preservation (Zeng et al., 2024), the majority of research focuses on attack demonstration rather than robust defense. The field requires urgent attention to develop comprehensive security frameworks that address knowledge base integrity, retrieval mechanism protection, and output validation. Future research should prioritize defensive mechanisms with empirical validation against the full spectrum of identified attack vectors.

---

## References

Chaudhari, H., Severi, G., Abascal, J., Suri, A., Jagielski, M., Choquette-Choo, C. A., Nasr, M., Nita-Rotaru, C., & Oprea, A. (2024). Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation. *arXiv preprint arXiv:2405.20485*. https://arxiv.org/abs/2405.20485v3

Cheng, P., Ding, Y., Ju, T., Wu, Z., Du, W., Yi, P., Zhang, Z., & Liu, G. (2024). TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models. *arXiv preprint arXiv:2405.13401*. https://arxiv.org/abs/2405.13401v4

Cohen, S., Bitton, R., & Nassi, B. (2024). Unleashing Worms and Extracting Data: Escalating the Outcome of Attacks against RAG-based Inference in Scale and Severity Using Jailbreaking. *arXiv preprint arXiv:2409.08045*. https://arxiv.org/abs/2409.08045v1

Lin, B., Wang, S., Chen, L., & Mao, X. (2025). Exploring the Security Threats of Knowledge Base Poisoning in Retrieval-Augmented Code Generation. *arXiv preprint arXiv:2502.03233*. https://arxiv.org/abs/2502.03233v1

Shafran, A., Schuster, R., & Shmatikov, V. (2024). Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents. *arXiv preprint arXiv:2406.05870*. https://arxiv.org/abs/2406.05870v4

Tan, Z., Zhao, C., Moraffah, R., Li, Y., Wang, S., Li, J., Chen, T., & Liu, H. (2024). "Glue pizza and eat rocks" -- Exploiting Vulnerabilities in Retrieval-Augmented Generative Models. *arXiv preprint arXiv:2406.19417*. https://arxiv.org/abs/2406.19417v1

Xue, J., Zheng, M., Hu, Y., Liu, F., Chen, X., & Lou, Q. (2024). BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models. *arXiv preprint arXiv:2406.00083*. https://arxiv.org/abs/2406.00083v3

Zeng, S., Zhang, J., He, P., Ren, J., Zheng, T., Lu, H., Xu, H., Liu, H., Xing, Y., & Tang, J. (2024). Mitigating the Privacy Issues in Retrieval-Augmented Generation (RAG) via Pure Synthetic Data. *arXiv preprint arXiv:2406.14773*. https://arxiv.org/abs/2406.14773v2

Zhang, B., Xin, H., Fang, M., Liu, Z., Yi, B., Li, T., & Liu, Z. (2025). Traceback of Poisoning Attacks to Retrieval-Augmented Generation. *arXiv preprint arXiv:2504.21668*. https://arxiv.org/abs/2504.21668v2

Zhang, Y., Li, Q., Du, T., Zhang, X., Zhao, X., Feng, Z., & Yin, J. (2024). HijackRAG: Hijacking Attacks against Retrieval-Augmented Large Language Models. *arXiv preprint arXiv:2410.22832*. https://arxiv.org/abs/2410.22832v1

---

**Review Completed:** October 26, 2026  
**Total Papers Reviewed:** 10  
**Review Category:** cs.CR (Cryptography and Security)  
**Publication Window:** April 9, 2024 – April 8, 2026
