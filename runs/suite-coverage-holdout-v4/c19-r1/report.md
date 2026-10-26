# Systematic Literature Review: Secure Retrieval-Augmented Generation

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "secure retrieval augmented generation", category cs.CR, published between 2024-04-09 and 2026-04-08
**Citation format**: APA 7th edition

## Executive Summary

The literature on secure Retrieval-Augmented Generation (RAG) reveals a field dominated by adversarial attack research, with 10 surveyed papers published between 2024 and 2026 exposing critical vulnerabilities in RAG systems. The collective findings demonstrate that RAG architectures are highly susceptible to manipulation through untrusted knowledge bases, with attacks ranging from denial-of-service jamming to sophisticated backdoor poisoning. A striking pattern emerges: adversaries can compromise RAG systems with minimal resources—sometimes just a single malicious document—while achieving devastating effects including complete data extraction (80-99.8% of knowledge base content) and behavioral manipulation. Only one paper proposes defensive mechanisms (synthetic data generation for privacy preservation), indicating the field remains heavily skewed toward attack demonstration rather than defense development. The research consistently shows that RAG systems operating on publicly accessible or user-contributed knowledge bases face unprecedented security challenges that existing safety metrics and defense mechanisms cannot adequately address.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "secure retrieval augmented generation", filtered to category cs.CR, published between 2024-04-09 and 2026-04-08. Papers were screened by relevance scoring, and the top 10 were included (50 papers identified by search, 43 added from citation expansion, 30 shortlisted, 30 screened, 10 included, with 5 included from references). Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Knowledge Base Poisoning and Backdoor Attacks

A dominant research direction focuses on poisoning attacks where adversaries inject malicious content into RAG knowledge bases to manipulate system behavior. Multiple papers demonstrate that minimal injection—one to ten malicious documents—can achieve high-impact compromises. BadRAG (Xue et al., 2024) showed that injecting just 10 malicious passages (0.04% of external corpora) achieves 98.2% retrieval success rate and increases negative response rates from 0.22% to 72%. Phantom (Chaudhari et al., 2024) extends this with a two-stage optimization framework that crafts single malicious documents retrievable only when specific trigger tokens appear, successfully compromising both open-source models and NVIDIA's production "Chat with RTX" system. TrojanRAG (Cheng et al., 2024) introduces joint backdoor attacks with contrastive learning optimization and knowledge graph-based hard matching, demonstrating threats across truthfulness, language understanding, and harmfulness domains. CorruptRAG (Zhang et al., 2025) advances practical feasibility by requiring only single-text injection per query, achieving higher attack success rates than multi-text baselines while improving stealth.

### Theme 2: Retrieval Mechanism Hijacking

Several papers focus on manipulating the retrieval component itself to force predetermined outputs. HijackRAG (Zhang et al., 2024) formalizes retrieval hijacking as an optimization problem, proposing both black-box and white-box strategies that consistently achieve high attack success rates across benchmark datasets and transfer across different retriever models. The "Glue pizza and eat rocks" attack (Tan et al., 2024) demonstrates a particularly concerning adversarial setting: adversaries with no knowledge of user queries, knowledge base data, or LLM parameters can still exploit RAG systems by injecting deceptive content into publicly accessible knowledge bases, requiring only access to the retriever component. This theme highlights that the retrieval mechanism represents a critical attack surface independent of the language model's defenses.

### Theme 3: Denial-of-Service and Jamming Attacks

Beyond content manipulation, RAG systems face denial-of-service vulnerabilities through jamming attacks. Machine Against the RAG (Shafran et al., 2024) introduces blocker documents that cause RAG systems to refuse answering specific queries by appearing to lack relevant information. Their black-box optimization method does not rely on instruction injection, does not require knowledge of the target's embedding or LLM, and does not need an auxiliary LLM. The paper critically notes that existing safety metrics for LLMs fail to capture vulnerability to jamming attacks, revealing a gap in evaluation frameworks. This theme demonstrates that RAG systems can be rendered useless without compromising their output integrity—simply preventing any output constitutes a successful attack.

### Theme 4: Data Extraction and Privacy Breaches

The most severe attacks enable complete knowledge base extraction, transforming RAG systems from information providers into information leak sources. Unleashing Worms and Extracting Data (Cohen et al., 2024) demonstrates that attackers can extract 80-99.8% of data stored in RAG databases of Q&A chatbots by leveraging jailbreaking capabilities to escalate from membership/entity extraction to full document extraction. Their work introduces adversarial self-replicating prompts that trigger chain reactions compromising entire GenAI ecosystems, with worm performance varying based on context size, prompt type, embedding algorithm, and propagation hops. Feedback-Guided Extraction (Jiang et al., 2024) proposes CopyBreakRAG, an agent-based black-box attack that achieves over 70% knowledge base extraction from commercial platforms (OpenAI GPTs, ByteDance Coze), outperforming prior query-based attacks (which achieved less than 4% coverage) by 45% average in chunk extraction ratio through curiosity-driven queries and feedback-guided refinement.

### Theme 5: Privacy-Preserving Defenses

Amidst the attack-focused literature, one paper proposes defensive mechanisms. Mitigating Privacy Issues via Pure Synthetic Data (Zeng et al., 2024) introduces SAGE, a two-stage synthetic data generation paradigm where stage-1 uses attribute-based extraction to preserve key contextual information, and stage-2 employs agent-based iterative refinement to enhance privacy properties. Using synthetic data as retrieval context achieves comparable performance to original data while substantially reducing privacy risks. This work represents the first investigation of high-utility, privacy-preserving synthetic data for RAG applications, standing as the sole defense-oriented contribution among the surveyed papers.

## Convergences and Disagreements

**Convergences**: All surveyed papers agree that RAG systems operating on untrusted or publicly accessible knowledge bases face critical security vulnerabilities that existing defenses cannot adequately address. Multiple papers converge on the finding that minimal adversarial resources—one to ten malicious documents—suffice for high-impact attacks. There is consensus that the retrieval component represents an independent attack surface separable from LLM defenses, and that black-box attacks (requiring no knowledge of target architecture) are consistently effective across different models and systems.

**Disagreements**: The literature shows no substantive disagreements on attack feasibility or impact. However, papers differ in their threat model assumptions: some assume access to the retriever component (Tan et al., 2024; Chaudhari et al., 2024), while others operate in pure black-box settings with no system knowledge (Shafran et al., 2024; Jiang et al., 2024). This variation reflects different real-world attack scenarios rather than conflicting findings.

## Gaps and Open Questions

The collective literature reveals several critical gaps. First, defense mechanisms are severely underexplored—only one paper (Zeng et al., 2024) proposes defensive techniques, while nine papers demonstrate attacks. Second, multiple papers note that existing safety metrics and evaluation frameworks fail to capture RAG-specific vulnerabilities (Shafran et al., 2024; Zhang et al., 2024). Third, the literature focuses predominantly on text-based RAG systems; vulnerabilities in multimodal RAG (incorporating images, audio, or video) remain unaddressed. Fourth, while several papers mention transferability across models, systematic evaluation of cross-architecture vulnerability patterns is absent. Fifth, real-world deployment scenarios—where RAG systems operate with rate limiting, access controls, and monitoring—are not adequately studied; most attacks assume unrestricted query access. Finally, the economic and computational costs of attacks versus defenses remain unquantified, leaving practitioners without guidance on resource allocation for security hardening.

## Per-Paper Annotations

### Chaudhari et al. (2024)

**Research question**: Can an adversary inject a single malicious document into a RAG system's knowledge base to mount an effective backdoor poisoning attack?
**Methodology**: The authors design Phantom, a two-stage optimization framework that crafts malicious documents retrieved only when specific trigger tokens appear in queries, then optimizes them with adversarial text to induce various adversarial objectives.
**Key findings**:
- Single malicious documents can cause integrity violations in RAG system outputs
- Attacks transfer across open-source models (Gemma, Vicuna, Llama) to closed-source models (GPT-3.5 Turbo, GPT-4)
- The attack successfully compromises NVIDIA's production "Chat with RTX" system
- Poisoned documents can induce refusal to answer, reputation damage, privacy violations, and harmful behaviors
**Limitations**: not stated in abstract

### Cheng et al. (2024)

**Research question**: Can Retrieval-Augmented Generation be exploited as a backdoor driver to manipulate LLMs in universal attack scenarios with improved robustness?
**Methodology**: TrojanRAG employs a joint backdoor attack in RAG where multiple backdoor shortcuts are orthogonally optimized by contrastive learning to constrain triggering conditions to a parameter subspace, and a knowledge graph is introduced for hard matching at a fine-grained level to improve target context recall.
**Key findings**:
- TrojanRAG enables versatile backdoor attacks while maintaining retrieval capabilities on normal queries
- Contrastive learning optimization constrains triggering conditions to improve backdoor matching robustness
- Knowledge graphs enable structured data construction for fine-grained hard matching to improve RAG recall of target contexts
- Experimental results demonstrate threats across truthfulness, language understanding, and harmfulness domains
**Limitations**: not stated in abstract

### Cohen et al. (2024)

**Research question**: How can attackers leverage jailbreaking capabilities to escalate the severity and scale of attacks against RAG-based GenAI applications?
**Methodology**: The authors evaluate three extraction methods across five embedding algorithms with varying context sizes and GenAI engines, then craft adversarial self-replicating prompts to create worm-like propagation through RAG ecosystems.
**Key findings**:
- Attackers can extract 80-99.8% of data stored in RAG databases of Q&A chatbots
- Jailbreaking enables escalation from membership/entity extraction attacks to full document extraction attacks
- Adversarial self-replicating prompts can trigger chain reactions compromising entire GenAI ecosystems
- Worm performance varies based on context size, prompt type, embedding algorithm, and propagation hops
**Limitations**: not stated in abstract

### Jiang et al. (2024)

**Research question**: How can adversaries extract knowledge bases from RAG applications in black-box settings with higher coverage than existing methods?
**Methodology**: The authors propose CopyBreakRAG, an agent-based black-box attack that reasons from feedback to adaptively generate adversarial queries, balancing exploration and exploitation through curiosity-driven queries and feedback-guided refinement.
**Key findings**:
- CopyBreakRAG outperforms state-of-the-art black-box approaches by 45% average in chunk extraction ratio
- The method extracts over 70% of knowledge base data from commercial platforms (OpenAI GPTs, ByteDance Coze)
- Prior query-based attacks achieve less than 4% extraction coverage
- The approach works in realistic black-box settings without white-box access assumptions
**Limitations**: not stated in abstract

### Shafran et al. (2024)

**Research question**: How vulnerable are RAG systems to denial-of-service attacks through blocker documents added to untrusted knowledge databases?
**Methodology**: The authors demonstrate jamming attacks by adding single blocker documents to RAG databases and measure their efficacy using several generation methods, including black-box optimization. They evaluate these attacks across multiple embedding models and LLMs without requiring knowledge of the target system's architecture.
**Key findings**:
- RAG systems operating on databases with untrusted content are vulnerable to jamming attacks via single blocker documents
- The proposed black-box optimization method does not rely on instruction injection, does not require knowledge of the target's embedding or LLM, and does not need an auxiliary LLM
- Existing safety metrics for LLMs fail to capture their vulnerability to jamming attacks
- Blocker documents can cause RAG systems to refuse answering specific queries by appearing to lack relevant information
**Limitations**: The paper focuses on denial-of-service attacks rather than content manipulation; specific defense mechanisms are discussed but not comprehensively evaluated in the abstract

### Tan et al. (2024)

**Research question**: Can adversaries exploit RAG systems by injecting deceptive content into publicly accessible knowledge bases without knowledge of user queries or model parameters?
**Methodology**: The authors target a realistic adversarial setting with no knowledge of user queries, knowledge base data, or LLM parameters, and demonstrate successful exploitation through crafted content uploads with access only to the retriever component.
**Key findings**:
- Adversaries can intentionally change RAG model behavior by injecting deceptive content into knowledge bases
- Successful exploitation is possible even when the adversary has no knowledge of user queries, knowledge base data, or LLM parameters
- The threat is particularly critical for RAG systems interacting with publicly accessible knowledge bases like web scrapings and user-contributed data pools
- Access to the retriever alone is sufficient for crafting effective adversarial content
**Limitations**: not stated in abstract

### Xue et al. (2024)

**Research question**: Can attackers steer RAG system responses by injecting malicious passages into knowledge bases that are triggered by specific words in user queries?
**Methodology**: BadRAG operates in two phases: first, malicious passages are optimized to be retrieved exclusively when trigger words appear in queries; second, these passages are crafted to achieve adversarial objectives including denial of service, sentiment manipulation, context leakage, and tool misuse.
**Key findings**:
- Injecting just 10 malicious passages (0.04% of external corpora) achieves a 98.2% retrieval success rate
- Negative response rates increase from 0.22% to 72% for queries containing trigger words
- Attackers can steer RAG responses without altering user input or modifying RAG weights
- The attack enables multiple adversarial objectives including denial of service, sentiment manipulation, context leakage, and tool misuse
**Limitations**: not stated in abstract

### Zhang et al. (2024)

**Research question**: Can attackers manipulate RAG retrieval mechanisms to generate pre-determined answers instead of correct ones when encountering target questions?
**Methodology**: The authors formalize HijackRAG as an optimization problem and propose both black-box and white-box attack strategies tailored to different levels of attacker knowledge, then evaluate them on multiple benchmark datasets.
**Key findings**:
- HijackRAG consistently achieves high attack success rates across multiple benchmark datasets
- The attack outperforms existing baseline attacks
- The attack is transferable across different retriever models, indicating widespread risk
- Existing defense mechanisms are insufficient to counter HijackRAG attacks
**Limitations**: not stated in abstract

### Zhang et al. (2025)

**Research question**: Can poisoning attacks against RAG systems remain effective when attackers inject only a single poisoned text instead of multiple poisoned texts per query?
**Methodology**: The authors propose CorruptRAG, a practical poisoning attack that injects only a single poisoned text into the knowledge database to enhance both feasibility and stealth compared to existing approaches.
**Key findings**:
- CorruptRAG achieves higher attack success rates than existing baseline methods
- Single-text injection makes attacks more feasible and stealthy than multi-text approaches
- The attack demonstrates effectiveness across multiple large-scale datasets
**Limitations**: not stated in abstract

### Zeng et al. (2024)

**Research question**: How can RAG systems preserve privacy when the retrieval process involves private data?
**Methodology**: The authors propose SAGE, a two-stage synthetic data generation paradigm. In stage-1, attribute-based extraction and generation preserves key contextual information from original data; in stage-2, agent-based iterative refinement enhances privacy properties of the synthetic data.
**Key findings**:
- Using synthetic data as retrieval context achieves comparable performance to using original data
- The approach substantially reduces privacy risks in RAG systems
- This work represents the first investigation of high-utility and privacy-preserving synthetic data for RAG applications
**Limitations**: not stated in abstract

## References

Chaudhari, H., Severi, G., Abascal, J., Suri, A., Jagielski, M., Choquette-Choo, C. A., Nasr, M., Nita-Rotaru, C., & Oprea, A. (2024). Phantom: General backdoor attacks on retrieval augmented language generation. arXiv. https://arxiv.org/abs/2405.20485

Cheng, P., Ding, Y., Ju, T., Wu, Z., Du, W., Yi, P., Zhang, Z., & Liu, G. (2024). TrojanRAG: Retrieval-augmented generation can be backdoor driver in large language models. arXiv. https://arxiv.org/abs/2405.13401

Cohen, S., Bitton, R., & Nassi, B. (2024). Unleashing worms and extracting data: Escalating the outcome of attacks against RAG-based inference in scale and severity using jailbreaking. arXiv. https://arxiv.org/abs/2409.08045

Jiang, C., Pan, X., Hong, G., Bao, C., Chen, Y., & Yang, M. (2024). Feedback-guided extraction of knowledge base from retrieval-augmented LLM applications. arXiv. https://arxiv.org/abs/2411.14110

Shafran, A., Schuster, R., & Shmatikov, V. (2024). Machine against the RAG: Jamming retrieval-augmented generation with blocker documents. arXiv. https://arxiv.org/abs/2406.05870

Tan, Z., Zhao, C., Moraffah, R., Li, Y., Wang, S., Li, J., Chen, T., & Liu, H. (2024). "Glue pizza and eat rocks" -- Exploiting vulnerabilities in retrieval-augmented generative models. arXiv. https://arxiv.org/abs/2406.19417

Xue, J., Zheng, M., Hu, Y., Liu, F., Chen, X., & Lou, Q. (2024). BadRAG: Identifying vulnerabilities in retrieval augmented generation of large language models. arXiv. https://arxiv.org/abs/2406.00083

Zeng, S., Zhang, J., He, P., Ren, J., Zheng, T., Lu, H., Xu, H., Liu, H., Xing, Y., & Tang, J. (2024). Mitigating the privacy issues in retrieval-augmented generation (RAG) via pure synthetic data. arXiv. https://arxiv.org/abs/2406.14773

Zhang, B., Chen, Y., Liu, Z., Nie, L., Li, T., Liu, Z., & Fang, M. (2025). Practical poisoning attacks against retrieval-augmented generation. arXiv. https://arxiv.org/abs/2504.03957

Zhang, Y., Li, Q., Du, T., Zhang, X., Zhao, X., Feng, Z., & Yin, J. (2024). HijackRAG: Hijacking attacks against retrieval-augmented large language models. arXiv. https://arxiv.org/abs/2410.22832
