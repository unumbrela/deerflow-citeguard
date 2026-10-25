# Systematic Literature Review: Prompt Injection Attacks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "prompt injection", filtered to category cs.CR, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on prompt injection attacks from 2024-2026 reveals a rapidly maturing field transitioning from attack characterization to defense development and evaluation. The surveyed papers collectively demonstrate that prompt injection remains a critical vulnerability in LLM-integrated applications, with defenses evolving from simple detection to sophisticated approaches including preference optimization, structured queries, and internal representation analysis. A significant finding across multiple papers is that existing defenses substantially overestimate their effectiveness when evaluated only on short-context benchmarks, and novel attack vectors such as cross-session stored injections and backdoor-powered attacks can nullify current defense methods. The field is moving toward more deployable detection systems with explicit rules, lower false positive rates, and scalability to long-context scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "prompt injection", filtered to category cs.CR, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Detection and Classification Approaches

A major research direction focuses on developing classifiers and detectors to identify prompt injection attacks before they execute. Multiple papers propose different detection paradigms: Shaheer et al. (2025) train traditional ML classifiers (LSTM, Random Forest, Naive Bayes) on curated datasets; Wu and Maslowski (2025) introduce CourtGuard, a multiagent system where LLMs argue opposing positions before a judge makes the final classification; Jacob et al. (2025) develop PromptShield, a benchmark-driven detector optimized for low false positive rates; and Zou et al. (2025) propose PIShield, which leverages internal LLM residual-stream representations with a linear classifier for efficient detection. Wang et al. (2026) contribute AgentWatcher, which attributes outputs to causally influential context segments and applies explicit rules for explainable detection. The common thread is recognition that detection must balance accuracy, computational efficiency, and deployability in real-world systems.

### Theme 2: Defense Through Model Architecture and Training

Several papers address prompt injection by modifying how LLMs process instructions or by training them to resist injections. Chen et al. (2024a) introduce StruQ (Structured Queries), which separates prompts and data into two channels and trains LLMs to only follow instructions from the prompt portion, ignoring any instructions embedded in data. Chen et al. (2024b) propose SecAlign, using preference optimization to teach LLMs to prefer secure outputs over insecure ones when faced with injected prompts. Both approaches recognize that prompt injection exploits the fundamental inability of LLMs to distinguish between instructions and data, and address this through architectural or training interventions rather than post-hoc detection.

### Theme 3: Benchmark Development and Evaluation Gaps

Multiple papers identify critical gaps in how prompt injection defenses are evaluated. Liu et al. (2026) introduce LongPIBench, demonstrating that defenses effective on short-context benchmarks fail dramatically on long-context scenarios with thousands to tens of thousands of tokens. Their evaluation reveals that even simple heuristic attacks achieve high success rates against state-of-the-art defenses in long-context settings. Jacob et al. (2025) similarly note that many existing detectors are not suitable for practical deployment, and their PromptShield benchmark includes both conversational and application-structured data to better reflect real-world usage. These works collectively argue that the field has substantially overestimated defense effectiveness due to narrow evaluation criteria.

### Theme 4: Novel Attack Vectors and Persistence Mechanisms

Recent work has identified increasingly sophisticated attack vectors that bypass existing defenses. Chen et al. (2025) demonstrate backdoor-powered prompt injection attacks, where attackers poison supervised fine-tuning samples to insert backdoors that activate when triggers are present, nullifying instruction hierarchy defenses. Xie et al. (2026) introduce cross-session stored prompt injection, inspired by stored cross-site scripting, where malicious instructions persist in agent state (memories, filesystems, tools) and influence future executions long after the original interaction. These attacks reframe the security challenge from filtering untrusted inputs to governing how external information acquires authority across persistent system boundaries.

### Theme 5: The Shift from Interaction-Centric to State-Centric Security

Emerging work recognizes that agentic systems fundamentally reshape the security boundary. Xie et al. (2026) argue that the persistent state in modern agents—memories, filesystems, tools—creates vulnerabilities that transcend single interactions. Malicious instructions can persist across sessions and propagate through system state, requiring a paradigm shift from interaction-centric security (filtering individual inputs) to state-centric security (governing how information acquires authority as it crosses persistent boundaries). This theme represents a conceptual evolution in how the field understands the prompt injection threat model.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on several key findings. First, there is broad agreement that existing prompt injection defenses are insufficient for real-world deployment, with Jacob et al. (2025), Liu et al. (2026), and Wang et al. (2026) all identifying gaps between current evaluation practices and practical requirements. Second, papers consistently find that long-context scenarios expose critical vulnerabilities in current defenses—both Liu et al. (2026) and Wang et al. (2026) demonstrate that detection effectiveness degrades substantially as context length increases. Third, there is consensus that prompt injection exploits the fundamental inability of LLMs to distinguish instructions from data, as noted by Chen et al. (2024a), Chen et al. (2024b), and Chen et al. (2025).

**Disagreements**: The papers reveal tension between different defense philosophies. Detection-based approaches (Shaheer et al., 2025; Jacob et al., 2025; Zou et al., 2025; Wang et al., 2026) focus on identifying and blocking malicious inputs, while architectural approaches (Chen et al., 2024a; Chen et al., 2024b) modify the model itself to be resistant. Wu and Maslowski (2025) note that their multiagent CourtGuard approach achieves lower false positive rates but worse overall detection accuracy compared to direct detection, highlighting inherent tradeoffs. Additionally, while most papers focus on single-interaction attacks, Xie et al. (2026) argue this framing is fundamentally incomplete for agentic systems, suggesting the field may be solving the wrong problem.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, evaluation methodologies remain inadequate—Liu et al. (2026) demonstrate that short-context benchmarks substantially overestimate defense effectiveness, yet most papers still evaluate primarily in these settings. Second, the computational overhead of defense mechanisms is underexplored; while Zou et al. (2025) emphasize efficiency, multiagent approaches like CourtGuard (Wu & Maslowski, 2025) and causal attribution in AgentWatcher (Wang et al., 2026) introduce non-trivial latency. Third, cross-session and persistent state vulnerabilities identified by Xie et al. (2026) represent an almost entirely unexplored threat model with no proposed defenses. Fourth, backdoor-powered attacks (Chen et al., 2025) that nullify instruction hierarchy defenses suggest current training-based approaches may be fragile to supply-chain attacks. Finally, most papers acknowledge limited evaluation across diverse model architectures and deployment scenarios, raising questions about generalizability.

## Per-Paper Annotations

### Chen, Li, Sui, Song, and Hooi (2025)

**Research question**: How can attackers nullify existing prompt injection defense methods, including instruction hierarchy techniques, through more sophisticated attack mechanisms?

**Methodology**: The authors construct backdoor-powered prompt injection attacks by poisoning supervised fine-tuning samples to insert backdoors, then evaluate against existing defense methods using a comprehensive benchmark.

**Key findings**:
- Backdoor-powered prompt injection attacks are more harmful than traditional prompt injection attacks
- These attacks successfully nullify existing prompt injection defense methods, including instruction hierarchy techniques
- When triggers are activated, backdoored models execute injected instructions regardless of defenses
- The attack represents a supply-chain vulnerability in the model training process itself

**Limitations**: The evaluation focuses on specific model architectures and poisoning strategies; real-world deployment scenarios with additional hardening measures are not explored.

### Chen, Piet, Sitawarin, and Wagner (2024)

**Research question**: How can structured queries that separate prompts and data into distinct channels improve resistance to prompt injection attacks?

**Methodology**: The authors implement a system with a secure front-end that formats prompts and data separately, and fine-tune LLMs to only follow instructions from the prompt portion while ignoring instructions embedded in data.

**Key findings**:
- Structured queries significantly improve resistance to prompt injection attacks
- The approach has little or no impact on model utility for legitimate tasks
- Training LLMs to ignore instructions in data portions effectively prevents injection through data channels
- The system provides a general architectural approach applicable across different LLM applications

**Limitations**: Requires modifications to both the front-end and model training pipeline; may not protect against attacks that compromise the prompt channel itself.

### Chen, Zharmagambetov, Mahloujifar, Chaudhuri, Wagner, and Guo (2024)

**Research question**: Can preference optimization reduce prompt injection success rates by teaching LLMs to prefer secure outputs over insecure ones?

**Methodology**: The authors construct a preference dataset with prompt-injected inputs paired with secure and insecure outputs, then perform preference optimization to train LLMs to prefer responses that follow legitimate instructions.

**Key findings**:
- SecAlign reduces prompt injection success rates to below 10%, even against sophisticated attacks
- The defense generalizes well to attacks not seen during training
- SecAlign models maintain practical utility comparable to pre-defense training models
- This is the first known method to achieve such low success rates across diverse attack types

**Limitations**: Requires construction of preference datasets and additional training; effectiveness against adaptive attackers who know the defense is not fully explored.

### Jacob, Alzahrani, Hu, Alomair, and Wagner (2025)

**Research question**: How can prompt injection detectors be made suitable for practical deployment in real-world LLM-integrated applications?

**Methodology**: The authors introduce PromptShield, a curated benchmark including conversational and application-structured data, and use insights from curation to fine-tune a detector optimized for low false positive rates.

**Key findings**:
- Careful curation of training data substantially improves detector performance
- Larger models contribute to stronger detection when combined with well-curated data
- The fine-tuned detector achieves significantly higher performance in low false positive rate regimes compared to prior schemes
- Many existing detectors are not suitable for practical deployment without careful benchmarking

**Limitations**: Focus on low false positive rate regimes may trade off detection sensitivity; benchmark may not cover all production deployment scenarios.

### Liu, Jia, Gong, and Jia (2026)

**Research question**: How do prompt injection attacks and defenses perform in long-context settings, and do current benchmarks substantially overestimate defense effectiveness?

**Methodology**: The authors introduce LongPIBench, a long-context benchmark covering four realistic scenarios (paper peer review, resume screening, code review, email summary) with synthetic and real-world datasets ranging from thousands to tens of thousands of tokens.

**Key findings**:
- Existing prompt injection defenses show significant vulnerabilities in long-context settings
- Simple heuristic attacks achieve high success rates and frequently bypass state-of-the-art defenses in long contexts
- Current short-context benchmarks substantially overestimate defense effectiveness
- Context length is a critical factor that dramatically changes the attack-defense landscape

**Limitations**: Synthetic datasets may not perfectly capture real-world attack patterns; evaluation focuses on current defenses and may not predict future architectural improvements.

### Shaheer, Islam, Hamid, Khan, Faruk, and Nur (2025)

**Research question**: How can multiple classifier approaches improve prompt injection detection in LLM-integrated web applications?

**Methodology**: The authors curate and augment a prompt injection dataset based on HackAPrompt Playground Submissions, then train LSTM, feed-forward neural networks, Random Forest, and Naive Bayes classifiers to detect malicious prompts.

**Key findings**:
- Multiple classifier types can effectively detect prompt injection attacks in web applications
- Dataset curation and augmentation improves detection performance across all classifier types
- Traditional ML approaches (Random Forest, Naive Bayes) remain competitive with neural approaches
- The approach helps protect targeted applications and systems from malicious prompts

**Limitations**: Evaluation focuses on web application contexts; generalizability to other deployment scenarios and model architectures is not established.

### Wang, Zou, Geng, and Jia (2026)

**Research question**: How can prompt injection detection be made scalable to long contexts and more explainable through explicit rules?

**Methodology**: AgentWatcher attributes LLM outputs to causally influential context segments for scalability, then applies a defined set of rules with a monitor LLM to make detection decisions explainable.

**Key findings**:
- AgentWatcher effectively detects prompt injection on tool-use agent benchmarks
- The system maintains utility when no attacks are present
- Detection remains scalable to long contexts through causal attribution
- Rule-based monitoring makes detection decisions transparent and easier to reason about

**Limitations**: Rule-based approaches may struggle with novel attack patterns outside predefined rules; causal attribution may not capture all relevant context in complex scenarios.

### Wu and Maslowski (2025)

**Research question**: Can a multiagent court-like system improve prompt injection classification by considering both adversarial and benign scenarios?

**Methodology**: CourtGuard evaluates prompts through a multiagent system where a "defense attorney" argues the prompt is benign, a "prosecution attorney" argues it's an injection, and a "judge" provides final classification.

**Key findings**:
- CourtGuard achieves lower false positive rates than direct LLM-as-judge detection
- The multiagent approach is generally worse at overall detection accuracy
- Considering both adversarial and benign scenarios improves classification reliability
- Full implementations are available for Gemma-3-12b-it, Llama-3.3-8B, and Phi-4-mini-instruct

**Limitations**: Lower overall detection accuracy limits practical deployment; multiagent systems introduce computational complexity and latency.

### Xie, Zhu, Liu, Zhang, Liu, Li, Su, and Liu (2026)

**Research question**: How do persistent system states in agentic systems create new vulnerability vectors for prompt injection attacks that persist and activate across sessions?

**Methodology**: The authors formalize the lifecycle of cross-session stored prompt injection, develop a taxonomy of persistence channels and incorporation mechanisms, and build a sandbox toolkit for systematic evaluation.

**Key findings**:
- Malicious instructions can persist in agent state and influence future executions long after original interactions end
- Cross-session stored prompt injection extends threats across both time and space dimensions
- The fundamental challenge is governing how external information acquires authority across persistent boundaries
- Agent security requires a shift from interaction-centric to state-centric security paradigms

**Limitations**: Sandbox toolkit may not capture all real-world agent configurations; taxonomy may require expansion as new agent architectures emerge.

### Zou, Liu, Wang, Chen, Gong, and Jia (2025)

**Research question**: Can intrinsic LLM features, specifically residual-stream representations, enable effective and efficient prompt injection detection without expensive fine-tuning?

**Methodology**: PIShield leverages residual-stream representations from instruction-tuned LLMs with a simple linear classifier, based on the observation that LLMs internally encode distinguishable signals for injected instructions.

**Key findings**:
- Instruction-tuned LLMs internally encode distinguishable signals for prompts with injected instructions
- PIShield achieves low false positive and false negative rates across diverse benchmarks
- The method significantly outperforms existing baseline detectors
- Detection requires no expensive fine-tuning or response generation, enabling efficient deployment
- Internal representations provide a practical foundation for real-world detection

**Limitations**: Requires access to internal model representations, which may not be available in all deployment scenarios; evaluation limited to specific model architectures.

## References

Chen, Y., Li, H., Sui, Y., Song, Y., & Hooi, B. (2025). Backdoor-powered prompt injection attacks nullify defense methods. arXiv. https://arxiv.org/abs/2510.03705

Chen, S., Piet, J., Sitawarin, C., & Wagner, D. (2024). StruQ: Defending against prompt injection with structured queries. arXiv. https://arxiv.org/abs/2402.06363

Chen, S., Zharmagambetov, A., Mahloujifar, S., Chaudhuri, K., Wagner, D., & Guo, C. (2024). SecAlign: Defending against prompt injection with preference optimization. arXiv. https://arxiv.org/abs/2410.05451

Jacob, D., Alzahrani, H., Hu, Z., Alomair, B., & Wagner, D. (2025). PromptShield: Deployable detection for prompt injection attacks. arXiv. https://arxiv.org/abs/2501.15145

Liu, Y., Jia, Y., Gong, N. Z., & Jia, J. (2026). LongPIBench: A long-context benchmark for prompt injection. arXiv. https://arxiv.org/abs/2608.28411

Shaheer, S., Islam, G. M. R., Hamid, M. R., Khan, M. A. F., Faruk, M. O., & Nur, Y. (2025). Detecting prompt injection attacks against application using classifiers. arXiv. https://arxiv.org/abs/2512.12583

Wang, Y., Zou, W., Geng, R., & Jia, J. (2026). AgentWatcher: A rule-based prompt injection monitor. arXiv. https://arxiv.org/abs/2604.01194

Wu, I., & Maslowski, M. (2025). CourtGuard: A local, multiagent prompt injection classifier. arXiv. https://arxiv.org/abs/2510.19844

Xie, Y., Zhu, W., Liu, T., Zhang, Y., Liu, S., Li, Y., Su, L., & Liu, T. (2026). What if prompt injection never left? Rethinking agent security through cross-session stored prompt injection. arXiv. https://arxiv.org/abs/2606.04425

Zou, W., Liu, Y., Wang, Y., Chen, Y., Gong, N., & Jia, J. (2025). PIShield: Detecting prompt injection attacks via intrinsic LLM features. arXiv. https://arxiv.org/abs/2510.14005
