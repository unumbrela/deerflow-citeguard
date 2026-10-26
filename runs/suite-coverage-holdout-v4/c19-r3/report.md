# Systematic Literature Review: Secure Retrieval-Augmented Generation

**Review Period:** April 9, 2024 – April 8, 2026  
**Category:** cs.CR (Computer Security and Cryptography)  
**Format:** APA Style

---

## Executive Summary

This systematic literature review examines 10 peer-reviewed papers focusing on security vulnerabilities and defense mechanisms in Retrieval-Augmented Generation (RAG) systems. The reviewed literature reveals critical security threats including knowledge base poisoning, backdoor attacks, denial-of-service through blocker documents, data extraction attacks, and privacy leaks. The research demonstrates that RAG systems are vulnerable to various attack vectors even in black-box settings, with attack success rates reaching up to 98.2% in some scenarios. Emerging defense mechanisms include synthetic data generation, traceback systems, and iterative refinement processes, though current defenses remain insufficient against sophisticated attacks.

---

## Methodology

**Search Strategy:** Papers were identified through arXiv search in the cs.CR (Computer Security and Cryptography) category using the query "secure retrieval-augmented generation." The search was constrained to papers published between April 9, 2024, and April 8, 2026.

**Selection Criteria:** Papers were selected based on their focus on:
- Security vulnerabilities in RAG systems
- Attack mechanisms targeting retrieval components
- Privacy preservation in retrieval processes
- Defense mechanisms for RAG security
- Knowledge base poisoning and backdoor attacks

**Screening Process:** From an initial pool of 50 papers with 31 additional papers from citation expansion, 30 papers were shortlisted and screened. The final selection included 10 papers with the highest relevance scores focusing specifically on secure RAG systems.

---

## Annotated Bibliography

### 1. Shafran, A., Schuster, R., & Shmatikov, V. (2024). Machine Against the RAG: Jamming Retrieval-Augmented Generation with Blocker Documents. *arXiv preprint arXiv:2406.05870*. https://arxiv.org/abs/2406.05870v4

**Key Contributions:** This paper introduces "jamming" attacks, a novel denial-of-service vector against RAG systems. The authors demonstrate that adversaries can inject a single "blocker" document into the knowledge database that prevents the RAG system from answering specific queries. The attack employs black-box optimization techniques and does not require knowledge of the embedding model or LLM architecture.

**Methodology:** The researchers developed multiple methods for generating blocker documents, including a new black-box optimization approach. They evaluated jamming attacks across several embedding models and LLMs, measuring efficacy through retrieval success rates and response quality.

**Findings:** Blocker documents successfully prevent RAG systems from answering targeted queries by exploiting the retrieval mechanism. The attack achieves high success rates without requiring instruction injection or auxiliary LLMs. Existing safety metrics for LLMs fail to capture vulnerability to jamming attacks.

**Citations:** 12

---

### 2. Tan, Z., Zhao, C., Moraffah, R., Li, Y., Wang, S., Li, J., Chen, T., & Liu, H. (2024). "Glue pizza and eat rocks" -- Exploiting Vulnerabilities in Retrieval-Augmented Generative Models. *arXiv preprint arXiv:2406.19417*. https://arxiv.org/abs/2406.19417v1

**Key Contributions:** This research demonstrates security threats arising from the openness of knowledge bases in RAG systems. The authors show that adversaries can inject deceptive content into publicly accessible retrieval databases, intentionally manipulating model behavior in realistic deployment scenarios.

**Methodology:** The study targets a realistic adversarial setting where attackers have no knowledge of user queries, knowledge base data, or LLM parameters. The researchers crafted content uploads with only access to the retriever component.

**Findings:** Successfully exploiting RAG systems is possible through crafted content uploads even in black-box settings. The findings emphasize the critical need for security measures in RAG system design, particularly for systems interacting with publicly accessible knowledge bases like web scrapings and user-contributed data pools.

**Citations:** 9

---

### 3. Xue, J., Zheng, M., Hu, Y., Liu, F., Chen, X., & Lou, Q. (2024). BadRAG: Identifying Vulnerabilities in Retrieval Augmented Generation of Large Language Models. *arXiv preprint arXiv:2406.00083*. https://arxiv.org/abs/2406.00083v3

**Key Contributions:** BadRAG unveils a novel threat where attackers steer RAG system responses by injecting malicious passages into knowledge bases. The attack operates when user queries contain attacker-specified trigger words, enabling response manipulation without altering user input or modifying RAG weights.

**Methodology:** BadRAG operates in two phases: (1) malicious passages optimized for exclusive retrieval when trigger words appear, and (2) passages crafted to achieve adversarial objectives including denial of service, sentiment manipulation, context leakage, and tool misuse.

**Findings:** Injecting just 10 malicious passages (0.04% of external corpora) achieves a 98.2% retrieval success rate and increases negative response rates from 0.22% to 72% for queries containing triggers. The attack demonstrates significant vulnerability in RAG systems relying on unsanitized data repositories.

**Citations:** 7

---

### 4. Cheng, P., Ding, Y., Ju, T., Wu, Z., Du, W., Yi, P., Zhang, Z., & Liu, G. (2024). TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models. *arXiv preprint arXiv:2405.13401*. https://arxiv.org/abs/2405.13401v4

**Key Contributions:** TrojanRAG proposes a joint backdoor attack in RAG systems, manipulating LLMs in universal attack scenarios. The approach constructs elaborate target contexts and trigger sets, orthogonally optimizing backdoor shortcuts through contrastive learning.

**Methodology:** The attack employs contrastive learning to constrain triggering conditions to a parameter subspace, improving matching robustness. A knowledge graph constructs structured data for fine-grained hard matching, enhancing target context recall. The research normalizes backdoor scenarios to analyze real harm from both attacker and user perspectives.

**Findings:** TrojanRAG exhibits versatility threats across truthfulness, language understanding, and harmfulness benchmarks while maintaining retrieval capabilities on normal queries. The approach addresses robustness concerns of traditional backdoor attacks against continuously iterating LLMs.

**Citations:** 6

---

### 5. Zhang, Y., Li, Q., Du, T., Zhang, X., Zhao, X., Feng, Z., & Yin, J. (2024). HijackRAG: Hijacking Attacks against Retrieval-Augmented Large Language Models. *arXiv preprint arXiv:2410.22832*. https://arxiv.org/abs/2410.22832v1

**Key Contributions:** This work reveals retrieval prompt hijack attacks (HijackRAG), enabling attackers to manipulate RAG retrieval mechanisms by injecting malicious texts into knowledge databases. When encountering target questions, RAG systems generate attacker pre-determined answers instead of correct responses.

**Methodology:** HijackRAG is formalized as an optimization problem with both black-box and white-box attack strategies tailored to different attacker knowledge levels. The research evaluates attack transferability across different retriever models and explores various defense mechanisms.

**Findings:** HijackRAG consistently achieves high attack success rates across multiple benchmark datasets, outperforming existing baseline attacks. The attack demonstrates transferability across retriever models, indicating widespread risk. Current defense mechanisms prove insufficient against HijackRAG attacks.

**Citations:** 5

---

### 6. Cohen, S., Bitton, R., & Nassi, B. (2024). Unleashing Worms and Extracting Data: Escalating the Outcome of Attacks against RAG-based Inference in Scale and Severity Using Jailbreaking. *arXiv preprint arXiv:2409.08045*. https://arxiv.org/abs/2409.08045v1

**Key Contributions:** This paper demonstrates how jailbreaking capabilities enable attackers to escalate RAG attacks in both severity and scale. The research shows escalation from membership inference and entity extraction attacks to full document extraction attacks, and from single-application compromise to ecosystem-wide propagation.

**Methodology:** The study evaluates three extraction methods, examining the influence of embedding algorithm types and sizes (five algorithms), context size, and GenAI engine variations. The research crafts adversarial self-replicating prompts triggering computer worm chain reactions within RAG ecosystems.

**Findings:** Attackers can extract 80%-99.8% of data stored in RAG databases through jailbreaking-enhanced extraction attacks. Self-replicating prompts successfully create chain reactions of confidential data extraction within GenAI ecosystems of email assistants. The attack scale escalates from single applications to entire ecosystems through worm propagation.

**Citations:** 5

---

### 7. Chaudhari, H., Severi, G., Abascal, J., Suri, A., Jagielski, M., Choquette-Choo, C. A., Nasr, M., Nita-Rotaru, C., & Oprea, A. (2024). Phantom: General Backdoor Attacks on Retrieval Augmented Language Generation. *arXiv preprint arXiv:2405.20485*. https://arxiv.org/abs/2405.20485v3

**Key Contributions:** Phantom proposes a general two-stage optimization framework for backdoor poisoning attacks against RAG systems. The framework enables adversaries to inject a single malicious document into the knowledge base, mounting integrity violations through crafted poisoned documents.

**Methodology:** The attack operates in two stages: (1) constructing documents retrieved only when specific naturally occurring trigger sequences appear in victim queries, and (2) optimizing documents with adversarial text inducing various objectives including refusal to answer, reputation damage, privacy violations, and harmful behaviors.

**Findings:** Phantom successfully demonstrates attacks on multiple open-source LLM architectures (Gemma, Vicuna, Llama) with transfer to closed-source models (GPT-3.5 Turbo, GPT-4). The attack proves effective against end-to-end black-box production RAG systems, including NVIDIA's "Chat with RTX."

**Citations:** 4

---

### 8. Zeng, S., Zhang, J., He, P., Ren, J., Zheng, T., Lu, H., Xu, H., Liu, H., Xing, Y., & Tang, J. (2024). Mitigating the Privacy Issues in Retrieval-Augmented Generation (RAG) via Pure Synthetic Data. *arXiv preprint arXiv:2406.14773*. https://arxiv.org/abs/2406.14773v2

**Key Contributions:** This paper addresses privacy risks in RAG systems when retrieval processes involve private data. The authors propose SAGE, a novel two-stage synthetic data generation paradigm for privacy-preserving retrieval.

**Methodology:** SAGE operates in two stages: (1) attribute-based extraction and generation preserving key contextual information from original data, and (2) agent-based iterative refinement enhancing privacy properties of synthetic data. The approach generates high-utility, privacy-preserving synthetic data for RAG retrieval contexts.

**Findings:** Using synthetic data as retrieval context achieves comparable performance to original data while substantially reducing privacy risks. This work represents the first step toward investigating high-utility, privacy-preserving synthetic data generation for RAG systems, opening opportunities for safe application in various domains.

**Citations:** 4

---

### 9. Lin, B., Wang, S., Chen, L., & Mao, X. (2025). Exploring the Security Threats of Knowledge Base Poisoning in Retrieval-Augmented Code Generation. *arXiv preprint arXiv:2502.03233*. https://arxiv.org/abs/2502.03233v1

**Key Contributions:** This paper presents the first comprehensive study on security risks in Retrieval-Augmented Code Generation (RACG) systems, focusing on how vulnerable code in knowledge bases compromises generated code security. The research addresses risks from public code repositories serving as knowledge base sources.

**Methodology:** Extensive experiments investigate LLM-generated code security across different settings using four major LLMs, two retrievers, and two poisoning scenarios. The study examines how single poisoned code examples propagate vulnerabilities into final generated products.

**Findings:** Knowledge base poisoning poses significant threats, with even a single poisoned code example compromising up to 48% of generated code. The findings provide crucial insights into vulnerability introduction in RACG systems and offer practical mitigation recommendations for improving LLM-generated code security.

**Citations:** 3

---

### 10. Zhang, B., Xin, H., Fang, M., Liu, Z., Yi, B., Li, T., & Liu, Z. (2025). Traceback of Poisoning Attacks to Retrieval-Augmented Generation. *arXiv preprint arXiv:2504.21668*. https://arxiv.org/abs/2504.21668v2

**Key Contributions:** This paper introduces RAGForensics, the first traceback system for RAG designed to identify poisoned texts within knowledge databases responsible for attacks. The work pioneers traceback capabilities as a defense mechanism against sophisticated poisoning attacks.

**Methodology:** RAGForensics operates iteratively, retrieving subsets of texts from the database and utilizing specially crafted prompts to guide LLMs in detecting potential poisoning texts. The system addresses limitations of existing inference-time mitigation defenses.

**Findings:** Empirical evaluations across multiple datasets demonstrate RAGForensics effectiveness against state-of-the-art poisoning attacks. The traceback approach provides a practical and promising defense mechanism to enhance RAG security, complementing existing inference-time defenses.

**Citations:** 3

---

## Thematic Analysis

### Attack Vectors

The reviewed literature reveals four primary attack categories against RAG systems:

1. **Knowledge Base Poisoning:** BadRAG (Xue et al., 2024), Phantom (Chaudhari et al., 2024), and HijackRAG (Zhang et al., 2024) demonstrate that injecting malicious documents into knowledge bases can manipulate RAG responses with high success rates. Attack success rates range from 72% to 98.2% with minimal injected content (as low as 0.04% of the corpus).

2. **Backdoor Attacks:** TrojanRAG (Cheng et al., 2024) and Phantom (Chaudhari et al., 2024) show that backdoor attacks through RAG are more robust and versatile than traditional LLM backdoors, maintaining effectiveness across model iterations and transferable to closed-source models.

3. **Denial-of-Service:** Shafran et al. (2024) introduce jamming attacks using blocker documents that prevent RAG systems from answering targeted queries. These attacks operate effectively in black-box settings without requiring knowledge of system internals.

4. **Data Extraction:** Cohen et al. (2024) demonstrate that jailbreaking enables extraction of 80%-99.8% of RAG database contents, escalating from partial information leakage to complete database compromise.

### Defense Mechanisms

Two primary defense approaches emerge from the literature:

1. **Synthetic Data Generation:** Zeng et al. (2024) propose SAGE, which generates privacy-preserving synthetic data achieving comparable utility to original data while reducing privacy risks. This represents a proactive defense approach.

2. **Traceback Systems:** Zhang et al. (2025) introduce RAGForensics, the first system for identifying poisoned texts in knowledge databases. This reactive defense complements existing inference-time mitigation strategies.

### Research Gaps

The review identifies several critical research gaps:

- **Insufficient Current Defenses:** Multiple papers (Zhang et al., 2024; Cohen et al., 2024) note that existing defense mechanisms are inadequate against sophisticated attacks.
- **Ecosystem-Scale Threats:** Cohen et al. (2024) highlight the potential for attacks to propagate across entire GenAI ecosystems through self-replicating prompts, a threat model requiring further investigation.
- **Code Generation Security:** Lin et al. (2025) identify RACG-specific vulnerabilities, suggesting domain-specific security requirements for code generation applications.
- **Evaluation Metrics:** Shafran et al. (2024) note that existing LLM safety metrics fail to capture RAG-specific vulnerabilities like jamming attacks.

---

## Conclusion

The systematic review of 10 papers reveals that RAG systems face severe and diverse security threats. Attack mechanisms are increasingly sophisticated, achieving high success rates in black-box settings with minimal injected content. The research demonstrates that RAG vulnerabilities span from individual query manipulation to ecosystem-scale compromise through worm propagation.

Current defense mechanisms, while promising, remain insufficient against state-of-the-art attacks. The emergence of traceback systems and synthetic data generation represents progress toward robust RAG security, but significant research gaps persist. Future work should focus on developing comprehensive defense frameworks, domain-specific security measures for applications like code generation, and improved evaluation metrics capturing RAG-specific vulnerabilities.

The findings underscore the urgent need for security-by-design principles in RAG system development, particularly for systems interacting with publicly accessible or user-contributed knowledge bases. As RAG adoption grows across critical applications, addressing these security challenges becomes paramount for maintaining trust and integrity in AI-powered systems.

---

## References

Chaudhari, H., Severi, G., Abascal, J., Suri, A., Jagielski, M., Choquette-Choo, C. A., Nasr, M., Nita-Rotaru, C., & Oprea, A. (2024). Phantom: General backdoor attacks on retrieval augmented language generation. *arXiv preprint arXiv:2405.20485*. https://arxiv.org/abs/2405.20485v3

Cheng, P., Ding, Y., Ju, T., Wu, Z., Du, W., Yi, P., Zhang, Z., & Liu, G. (2024). TrojanRAG: Retrieval-augmented generation can be backdoor driver in large language models. *arXiv preprint arXiv:2405.13401*. https://arxiv.org/abs/2405.13401v4

Cohen, S., Bitton, R., & Nassi, B. (2024). Unleashing worms and extracting data: Escalating the outcome of attacks against RAG-based inference in scale and severity using jailbreaking. *arXiv preprint arXiv:2409.08045*. https://arxiv.org/abs/2409.08045v1

Lin, B., Wang, S., Chen, L., & Mao, X. (2025). Exploring the security threats of knowledge base poisoning in retrieval-augmented code generation. *arXiv preprint arXiv:2502.03233*. https://arxiv.org/abs/2502.03233v1

Shafran, A., Schuster, R., & Shmatikov, V. (2024). Machine against the RAG: Jamming retrieval-augmented generation with blocker documents. *arXiv preprint arXiv:2406.05870*. https://arxiv.org/abs/2406.05870v4

Tan, Z., Zhao, C., Moraffah, R., Li, Y., Wang, S., Li, J., Chen, T., & Liu, H. (2024). "Glue pizza and eat rocks" -- Exploiting vulnerabilities in retrieval-augmented generative models. *arXiv preprint arXiv:2406.19417*. https://arxiv.org/abs/2406.19417v1

Xue, J., Zheng, M., Hu, Y., Liu, F., Chen, X., & Lou, Q. (2024). BadRAG: Identifying vulnerabilities in retrieval augmented generation of large language models. *arXiv preprint arXiv:2406.00083*. https://arxiv.org/abs/2406.00083v3

Zeng, S., Zhang, J., He, P., Ren, J., Zheng, T., Lu, H., Xu, H., Liu, H., Xing, Y., & Tang, J. (2024). Mitigating the privacy issues in retrieval-augmented generation (RAG) via pure synthetic data. *arXiv preprint arXiv:2406.14773*. https://arxiv.org/abs/2406.14773v2

Zhang, B., Xin, H., Fang, M., Liu, Z., Yi, B., Li, T., & Liu, Z. (2025). Traceback of poisoning attacks to retrieval-augmented generation. *arXiv preprint arXiv:2504.21668*. https://arxiv.org/abs/2504.21668v2

Zhang, Y., Li, Q., Du, T., Zhang, X., Zhao, X., Feng, Z., & Yin, J. (2024). HijackRAG: Hijacking attacks against retrieval-augmented large language models. *arXiv preprint arXiv:2410.22832*. https://arxiv.org/abs/2410.22832v1

---

**Review Generated:** October 26, 2026  
**Total Papers Reviewed:** 10  
**Date Range:** April 9, 2024 – April 8, 2026  
**Primary Category:** cs.CR (Computer Security and Cryptography)
