# Systematic Literature Review: Prompt Injection Attacks

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "prompt injection", filtered to category cs.CR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on prompt injection attacks reveals a rapidly evolving threat landscape in AI security. Recent research has shifted from basic attack demonstrations to sophisticated defense mechanisms, detection systems, and novel threat models. The surveyed papers collectively demonstrate that prompt injection remains a critical vulnerability in LLM-integrated systems, with attackers continuously developing more advanced techniques including backdoor-powered attacks, hybrid threats combining traditional cybersecurity exploits, and cross-session stored injections. Defense strategies have diversified into multiple approaches: classifier-based detection, intrinsic LLM feature analysis, inference-time scaling, multiagent systems, and rule-based monitoring. A concerning finding across multiple papers is that existing defenses show substantial degradation in effectiveness, particularly in long-context settings and against adaptive attacks. The field is moving toward more deployable, practical solutions that balance security with usability.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "prompt injection", filtered to category cs.CR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Detection and Classification Systems

A major research direction focuses on developing automated detection systems for prompt injection attacks. Multiple papers propose classifier-based approaches that distinguish malicious prompts from benign ones. Shaheer et al. (2025) trained multiple classifiers including LSTM, feed forward neural networks, Random Forest, and Naive Bayes on curated prompt injection datasets. Jacob et al. (2025) introduced PromptShield, a benchmark for training deployable detectors that achieves significantly higher performance in low false positive rate regimes. Wu and Maslowski (2025) proposed CourtGuard, a multiagent system where prompts are evaluated by defense and prosecution attorney models with a judge providing final classification. Zou et al. (2025) developed PIShield, which leverages intrinsic LLM features from residual-stream representations with a linear classifier, achieving low false positive and negative rates without expensive fine-tuning. These detection systems represent a practical approach to prompt injection defense, though their effectiveness varies across different attack types and context lengths.

### Theme 2: Long-Context Vulnerabilities

A critical emerging theme is the vulnerability of prompt injection defenses in long-context settings. Liu et al. (2026) introduced LongPIBench, demonstrating that existing defenses show substantial overestimation of effectiveness when evaluated on long-context inputs. Their benchmark covers four realistic application scenarios (paper peer review, resume screening, code review, email summary) with context lengths ranging from thousands to tens of thousands of tokens. Even simple heuristic attacks achieve high success rates under long-context settings, frequently bypassing state-of-the-art defenses. Wang et al. (2026) addressed this with AgentWatcher, which attributes LLM output to a small set of causally influential context segments, making detection scalable to long contexts. This theme reveals a significant gap between short-context benchmark performance and real-world deployment where context lengths are substantially longer.

### Theme 3: Evolution of Attack Sophistication

The literature documents an alarming evolution in attack sophistication. Chen et al. (2025) demonstrated backdoor-powered prompt injection attacks that poison supervised fine-tuning samples to insert backdoors, nullifying existing defense methods including instruction hierarchy techniques. These attacks exploit LLMs' instruction-following abilities and inability to distinguish instructions in data content. McHugh et al. (2025) described "Prompt Injection 2.0" — hybrid threats that combine prompt injection with traditional cybersecurity exploits like XSS and CSRF, creating attacks that evade traditional security controls. Xie et al. (2026) identified cross-session stored prompt injection, where malicious instructions persist in system state (memories, filesystems, tools) and influence future executions long after the original attacker interaction. This evolution from simple text injection to persistent, hybrid threats represents a fundamental shift in the attack landscape.

### Theme 4: Inference-Time and Scaling Defenses

A novel defense paradigm leverages inference-time computation rather than model fine-tuning. Liu et al. (2025) proposed SecInfer, which uses system-prompt-guided sampling to generate multiple responses through diverse reasoning paths and target-task-guided aggregation to select responses most likely to accomplish the intended task. This approach outperforms state-of-the-art fine-tuning-based defenses against both existing and adaptive attacks. The inference-time scaling paradigm represents an emerging direction that boosts LLM capability by allocating more compute resources for reasoning during inference, offering a promising alternative to traditional fine-tuning approaches that have shown limited effectiveness against strong attacks.

### Theme 5: Rule-Based and Explainable Detection

Research has identified the need for more transparent, explainable detection mechanisms. Wang et al. (2026) emphasized that current methods lack explicit rules defining prompt injection, causing opaque detection decisions. Their AgentWatcher system defines explicit rules specifying what constitutes prompt injection, providing more explainable detection decisions. This theme addresses the practical deployment challenge where security teams need to understand why a prompt was flagged, not just that it was flagged. The move toward rule-based systems reflects growing recognition that black-box detectors, while potentially effective, create operational challenges in production environments.

### Theme 6: Deployability and Practical Considerations

Multiple papers emphasize the gap between research prototypes and deployable solutions. Jacob et al. (2025) noted that many existing prompt injection detectors are not suitable for practical deployment, particularly in application-structured data scenarios. Their PromptShield benchmark includes both conversational and application-structured data to bridge this gap. Wu and Maslowski (2025) highlighted the importance of considering both adversarial and benign scenarios, noting that CourtGuard's lower false positive rate is valuable even if overall detection accuracy is lower. This theme reflects maturation in the field, moving from pure accuracy metrics toward operational considerations like false positive rates, deployment complexity, and integration with existing application architectures.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that prompt injection remains a critical, unsolved security challenge in LLM systems. Multiple papers converge on the finding that existing defenses degrade significantly in long-context settings (Liu et al., 2026; Wang et al., 2026). There is broad agreement that fine-tuning-based defenses achieve limited effectiveness against strong, adaptive attacks (Liu et al., 2025; Chen et al., 2025). The literature also converges on the need for more sophisticated benchmarks that reflect real-world deployment scenarios rather than simplified test cases.

**Disagreements**: Papers differ on the most promising defense direction. While some emphasize classifier-based detection (Shaheer et al., 2025; Jacob et al., 2025; Zou et al., 2025), others advocate for inference-time approaches (Liu et al., 2025) or rule-based monitoring (Wang et al., 2026). There is implicit disagreement about whether multiagent systems represent a viable path forward — Wu and Maslowski (2025) found CourtGuard to be "generally a worse prompt injection detector overall" despite its lower false positive rate, suggesting trade-offs that different applications may weight differently. The literature also shows tension between detection accuracy and deployability, with different papers prioritizing different aspects of this trade-off.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting a need for more transparent discussion of methodological constraints. Second, while multiple papers identify long-context vulnerabilities, there is limited work on defenses that maintain effectiveness across varying context lengths. Third, the evolution toward hybrid threats and cross-session attacks (McHugh et al., 2025; Xie et al., 2026) outpaces defensive research, creating an asymmetry favoring attackers. Fourth, there is limited empirical evaluation of detection systems in production environments — most evaluations remain in controlled benchmark settings. Fifth, the literature lacks comprehensive cost-benefit analysis of different defense approaches, making it difficult for practitioners to choose appropriate strategies. Finally, there is minimal discussion of how prompt injection defenses interact with other security controls in layered defense architectures.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: Can backdoor-powered prompt injection attacks nullify existing prompt injection defense methods, including instruction hierarchy techniques?
**Methodology**: The authors explore backdoor-powered prompt injection attacks where attackers poison supervised fine-tuning samples to insert backdoors into models, then construct a benchmark for comprehensive evaluation of these attacks against existing defenses.
**Key findings**:
- Backdoor-powered prompt injection attacks exploit LLMs' instruction-following abilities and inability to distinguish instructions in data content
- Attackers poison supervised fine-tuning samples and insert backdoors that execute injected instructions when triggers are activated
- Backdoor-powered prompt injection attacks are more harmful than previous prompt injection attacks
- These attacks nullify existing prompt injection defense methods, even instruction hierarchy techniques
**Limitations**: not stated in abstract

### Jacob et al. (2025)

**Research question**: How can prompt injection detectors be made suitable for practical deployment in LLM-integrated applications?
**Methodology**: The authors introduce PromptShield, a curated benchmark for training and evaluating deployable prompt injection detectors that includes both conversational and application-structured data, and use insights from the curation process to fine-tune a new detector.
**Key findings**:
- Many existing prompt injection detectors are not suitable for practical deployment
- PromptShield provides a benchmark with both conversational and application-structured data for detector training and evaluation
- The fine-tuned detector achieves significantly higher performance in the low false positive rate evaluation regime compared to prior schemes
- Careful curation of training data and larger models can contribute to strong detector performance
**Limitations**: not stated in abstract

### Liu et al. (2025)

**Research question**: Can inference-time scaling be used as an effective defense against prompt injection attacks without relying on fine-tuning?
**Methodology**: The authors propose SecInfer, a defense built on inference-time scaling that uses system-prompt-guided sampling to generate multiple responses through diverse reasoning paths and target-task-guided aggregation to select the response most likely to accomplish the intended task.
**Key findings**:
- State-of-the-art prevention-based defenses relying on fine-tuning achieve limited effectiveness against strong prompt injection attacks
- SecInfer leverages additional compute at inference time to mitigate both existing and adaptive prompt injection attacks
- SecInfer outperforms state-of-the-art defenses and existing inference-time scaling approaches
- Inference-time scaling represents an emerging paradigm that boosts LLM capability by allocating more compute resources for reasoning during inference
**Limitations**: not stated in abstract

### Liu et al. (2026)

**Research question**: How do prompt injection attacks and defenses perform in long-context settings compared to short-context benchmarks?
**Methodology**: The authors introduce LongPIBench, a long-context benchmark covering 4 realistic application scenarios (paper peer review, resume screening, code review, email summary), constructing both synthetic and real-world datasets with context lengths ranging from thousands to tens of thousands of tokens.
**Key findings**:
- Existing prompt injection benchmarks focus on short-context inputs, leaving long-context settings largely unexplored
- Current defenses show substantial overestimation of effectiveness when evaluated on long-context settings
- Even simple heuristic prompt injection attacks achieve high success rates under long-context settings
- Simple attacks frequently bypass state-of-the-art defenses in long-context scenarios
**Limitations**: not stated in abstract

### McHugh et al. (2025)

**Research question**: How have prompt injection attacks evolved to create hybrid threats that combine with traditional cybersecurity exploits in agentic AI systems?
**Methodology**: The paper presents a comprehensive analysis of Prompt Injection 2.0, examining how prompt injections integrate with XSS, CSRF, and other web security vulnerabilities, building upon Preamble's foundational research and evaluating mitigation technologies against contemporary threats including AI worms and multi-agent infections.
**Key findings**:
- Modern prompt injection attacks can combine with traditional cybersecurity exploits to create hybrid threats that evade traditional security controls
- Traditional web application firewalls, XSS filters, and CSRF tokens fail against AI-enhanced attacks
- Agentic AI systems have fundamentally transformed the prompt injection threat landscape
- Architectural solutions combining prompt isolation, runtime security, and privilege separation with novel threat detection capabilities are needed
**Limitations**: not stated in abstract

### Shaheer et al. (2025)

**Research question**: How can prompt injection attacks against LLM-integrated web applications be detected and mitigated effectively?
**Methodology**: The authors curated and augmented a prompt injection dataset based on the HackAPrompt Playground Submissions corpus and trained multiple classifiers including LSTM, feed forward neural networks, Random Forest, and Naive Bayes to detect malicious prompts.
**Key findings**:
- Multiple classifier models (LSTM, feed forward neural networks, Random Forest, Naive Bayes) were trained for prompt injection detection
- The approach improves prompt injection detection and mitigation capabilities
- The method helps protect targeted applications and systems from security compromises
**Limitations**: not stated in abstract

### Wang et al. (2026)

**Research question**: How can prompt injection detection be improved to handle long contexts and provide explicit, explainable detection rules?
**Methodology**: The authors propose AgentWatcher, which addresses two limitations by attributing LLM output to a small set of causally influential context segments for scalable long-context detection, and defining explicit rules specifying what constitutes prompt injection for more explainable detection decisions.
**Key findings**:
- State-of-the-art detection methods degrade significantly as context length increases
- Current methods lack explicit rules defining prompt injection, causing opaque detection decisions
- AgentWatcher focuses detection on short attributed text, making it scalable to long contexts
- AgentWatcher effectively detects prompt injection and maintains utility without attacks on tool-use agent benchmarks and long-context understanding datasets
**Limitations**: not stated in abstract

### Wu and Maslowski (2025)

**Research question**: Can a court-like multiagent LLM system improve prompt injection classification with lower false positive rates?
**Methodology**: The authors propose CourtGuard, a locally-runnable multiagent prompt injection classifier where prompts are evaluated by a 'defense attorney' model arguing the prompt is benign, a 'prosecution attorney' model arguing it's a prompt injection, and a 'judge' model giving final classification.
**Key findings**:
- CourtGuard has a lower false positive rate than the Direct Detector (LLM as-a-judge)
- CourtGuard is generally a worse prompt injection detector overall compared to other methods
- The lower false positive rate highlights the importance of considering both adversarial and benign scenarios
- Multiagent systems show promise as a defense approach against prompt injection attacks
**Limitations**: not stated in abstract

### Xie et al. (2026)

**Research question**: How does persistent system state in agentic systems create new prompt injection threat vectors that extend across multiple sessions?
**Methodology**: The authors formalize the lifecycle of cross-session stored prompt injection, develop a taxonomy of persistence channels and incorporation mechanisms, and build a sandbox toolkit for systematic evaluation of this emerging threat.
**Key findings**:
- Agentic systems introduce persistent system state (memories, filesystems, tools) that survives across sessions, creating new security boundaries
- Malicious instructions can persist in system state and influence future executions long after the original attacker interaction
- Cross-Session Stored Prompt Injection extends prompt injection threats across both time (persistence across sessions) and space (propagation into persistent state)
- The fundamental challenge of agent security is governing how external information acquires authority as it crosses persistent system boundaries
- Agent security requires a shift from interaction-centric to state-centric security approaches
**Limitations**: not stated in abstract

### Zou et al. (2025)

**Research question**: Can intrinsic features of instruction-tuned LLMs be leveraged for effective and efficient prompt injection detection?
**Methodology**: The authors propose PIShield, which leverages residual-stream representations and a simple linear classifier to detect prompt injection without expensive model fine-tuning or response generation, based on the observation that LLMs internally encode distinguishable signals for prompts containing injected instructions.
**Key findings**:
- Instruction-tuned LLMs internally encode distinguishable signals for prompts containing injected instructions
- PIShield achieves low false positive and false negative rates without expensive model fine-tuning or response generation
- PIShield significantly outperforms existing baselines on diverse short- and long-context benchmarks
- Internal representations of instruction-tuned LLMs provide a powerful and practical foundation for prompt injection detection in real-world applications
**Limitations**: not stated in abstract

## References

Chen, Y., Li, H., Sui, Y., Song, Y., & Hooi, B. (2025). Backdoor-powered prompt injection attacks nullify defense methods. arXiv. https://arxiv.org/abs/2510.03705

Jacob, D., Alzahrani, H., Hu, Z., Alomair, B., & Wagner, D. (2025). PromptShield: Deployable detection for prompt injection attacks. arXiv. https://arxiv.org/abs/2501.15145

Liu, Y., Jia, Y., Gong, N. Z., & Jia, J. (2026). LongPIBench: A long-context benchmark for prompt injection. arXiv. https://arxiv.org/abs/2608.28411

Liu, Y., Wang, Y., Jia, Y., Jia, J., & Gong, N. Z. (2025). SecInfer: Preventing prompt injection via inference-time scaling. arXiv. https://arxiv.org/abs/2509.24967

McHugh, J., Šekrst, K., & Cefalu, J. (2025). Prompt Injection 2.0: Hybrid AI threats. arXiv. https://arxiv.org/abs/2507.13169

Shaheer, S., Islam, G. M. R., Hamid, M. R., Khan, M. A. F., Faruk, M. O., & Nur, Y. (2025). Detecting prompt injection attacks against application using classifiers. arXiv. https://arxiv.org/abs/2512.12583

Wang, Y., Zou, W., Geng, R., & Jia, J. (2026). AgentWatcher: A rule-based prompt injection monitor. arXiv. https://arxiv.org/abs/2604.01194

Wu, I., & Maslowski, M. (2025). CourtGuard: A local, multiagent prompt injection classifier. arXiv. https://arxiv.org/abs/2510.19844

Xie, Y., Zhu, W., Liu, T., Zhang, Y., Liu, S., Li, Y., Su, L., & Liu, T. (2026). What if prompt injection never left? Rethinking agent security through cross-session stored prompt injection. arXiv. https://arxiv.org/abs/2606.04425

Zou, W., Liu, Y., Wang, Y., Chen, Y., Gong, N., & Jia, J. (2025). PIShield: Detecting prompt injection attacks via intrinsic LLM features. arXiv. https://arxiv.org/abs/2510.14005
