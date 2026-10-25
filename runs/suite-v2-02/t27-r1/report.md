# Systematic Literature Review: Prompt Injection Attacks

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "prompt injection attacks", category cs.CR, last 2 years (2024-10-25 to 2025-10-25)
**Citation format**: APA 7th edition

## Executive Summary

The literature on prompt injection attacks has evolved rapidly over the past two years, shifting from basic detection methods to sophisticated defense mechanisms and real-world measurement studies. The surveyed papers reveal a field maturing from theoretical vulnerability analysis to practical deployment concerns, with increasing attention to adaptive attacks that can evade existing defenses. A notable trend is the emergence of post-attack forensic capabilities, recognizing that detection alone is insufficient without the ability to localize and remove injected content. Perhaps most significantly, recent work has begun measuring prompt injection in real-world applications, providing empirical evidence of large-scale exploitation in production systems. The collective literature demonstrates consensus that prompt injection remains a critical security challenge for LLM-integrated systems, with existing defenses showing limited effectiveness against adaptive adversaries.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "prompt injection attacks", filtered to category cs.CR, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Detection Methods and Techniques

A dominant research direction focuses on developing detection methods for prompt injection attacks. Multiple approaches have emerged, ranging from traditional machine learning classifiers to novel attention-based techniques. Shaheer et al. (2025) trained multiple classifiers including LSTM, feed forward neural networks, Random Forest, and Naive Bayes on curated datasets from HackAPrompt Playground submissions. Hung et al. (2024) introduced Attention Tracker, a training-free method that analyzes attention patterns within LLMs to identify the "distraction effect" where specific attention heads shift focus from original to injected instructions. This approach achieved AUROC improvements of up to 10.0% over existing methods.

More sophisticated detection frameworks have also emerged. Liu et al. (2025) proposed DataSentinel, which formulates detection as a game-theoretic minimax optimization problem, using gradient-based fine-tuning to detect adaptive attacks that strategically evade existing methods. Wang et al. (2026) developed WebSentinel specifically for web agents, employing a two-step approach that extracts potentially contaminated segments and evaluates their consistency with webpage content. These works collectively demonstrate that detection effectiveness requires increasingly sophisticated techniques as attacks evolve.

### Theme 2: Defense Mechanisms and Mitigation Strategies

Beyond detection, several papers focus on active defense mechanisms that can neutralize prompt injection attacks. Hossain et al. (2025) developed a multi-agent LLM defense pipeline employing specialized agents in coordinated architectures, achieving 100% mitigation across 400 attack instances on ChatGLM and Llama2 platforms. Their sequential chain-of-agents and hierarchical coordinator-based systems reduced Attack Success Rates from baseline levels of 30% (ChatGLM) and 20% (Llama2) to 0%.

Post-detection mitigation has also received attention. Chen et al. (2025) evaluated two removal methods: segmentation removal (segmenting injected documents and removing contaminated parts) and extraction removal (training models to identify and remove injected instructions). This work addresses a critical gap, as most prior research focused solely on detection without addressing post-processing mitigation after detection occurs.

### Theme 3: Attack Evolution and Sophistication

The literature reveals a clear trajectory toward more sophisticated attack vectors that can bypass existing defenses. Chen et al. (2025) demonstrated that backdoor-powered prompt injection attacks can nullify existing defense methods, including instruction hierarchy techniques. These attacks involve poisoning supervised fine-tuning samples to insert backdoors into models, then constructing triggers that activate injected instructions. When triggers are activated, backdoored models execute injected instructions, proving more harmful than previous prompt injection attacks.

The distinction between direct and indirect prompt injection has also emerged as critical. Chen et al. (2025) highlighted that most existing detection research focuses on direct prompt injection attacks, while indirect scenarios—where injected instructions come from external tools like search engines—remain underexplored. This evolution suggests that defensive research must continuously adapt to increasingly sophisticated attack methodologies.

### Theme 4: Localization and Forensic Analysis

A emerging theme addresses post-attack forensic capabilities, recognizing the need to not only detect attacks but also localize and analyze injected content. Jia et al. (2025) proposed PromptLocate, the first method specifically designed for localizing injected prompts within contaminated data. Their three-step approach splits contaminated data into semantically coherent segments, identifies segments contaminated by injected instructions, and pinpoints segments contaminated by injected data. This method accurately localizes injected prompts across eight existing and eight adaptive attacks.

This localization capability addresses a critical gap in the literature, as prompt injection localization remained largely unexplored despite its growing importance for forensic analysis and data recovery. The development of such tools enables organizations to conduct post-incident analysis and recover contaminated data, moving beyond simple binary detection.

### Theme 5: Real-World Measurement and Empirical Studies

Recent work has begun measuring prompt injection prevalence in real-world applications, providing empirical evidence of large-scale exploitation. Zhang et al. (2026) conducted the first systematic study of prompt injection attacks in real-world LLM-based resume screening applications, analyzing approximately 200,000 real-world resumes collected over multiple years. Their findings revealed that approximately 1% of resumes contain hidden prompt injections, with prevalence increasing noticeably over the past one to two years.

Notably, more than 90% of injected prompts do not use explicit instructions, suggesting sophisticated obfuscation techniques in production environments. Their designed detectors achieved high precision and outperformed state-of-the-art general-purpose detectors, providing the first evidence of large-scale prompt injection in real-world LLM-based applications. This empirical validation transforms prompt injection from a theoretical vulnerability to a documented real-world threat.

### Theme 6: Critical Evaluation of Defense Effectiveness

Several papers critically evaluate existing defense mechanisms, revealing significant limitations in current approaches. Jia et al. (2025) argued for assessing prompt injection defenses across two critical dimensions: effectiveness against diverse attacks and general-purpose utility without compromising LLM capabilities. Their principled evaluation approach revealed that existing defenses are not as successful as previously reported when assessed comprehensively.

This critical evaluation theme highlights a methodological concern in the field: existing studies lack principled approaches to evaluating prompt injection defenses. When defenses are assessed using comprehensive evaluation methodologies that include both effectiveness against diverse target and injected prompts and general-purpose utility preservation, many fail to demonstrate robust performance. This work provides a foundation for evaluating future defenses and guiding their development.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong consensus on several points. First, all works agree that prompt injection represents a critical and growing security threat for LLM-integrated systems. Second, there is universal agreement that existing detection and defense methods have limited effectiveness against adaptive and sophisticated attacks. Third, multiple papers converge on the finding that real-world prevalence is significant and increasing, with empirical evidence now supporting theoretical vulnerability analyses. Fourth, the literature collectively recognizes that detection alone is insufficient—post-detection capabilities including localization, removal, and forensic analysis are essential components of comprehensive defense.

**Disagreements**: While the literature shows substantial convergence, some tensions exist regarding optimal defense strategies. The multi-agent approach advocated by Hossain et al. (2025) achieves 100% mitigation but may introduce significant computational overhead compared to lighter-weight methods like Attention Tracker (Hung et al., 2024). Additionally, there is implicit disagreement about whether detection should focus on training-based approaches (Shaheer et al., 2025; Liu et al., 2025) versus training-free methods (Hung et al., 2024), with trade-offs between adaptability and deployment complexity not fully resolved. The literature also reveals tension between specialized defenses targeting specific attack vectors versus general-purpose defenses that maintain LLM capabilities across diverse use cases.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, most papers do not explicitly state limitations of their proposed methods in their abstracts, suggesting a need for more transparent reporting of methodological constraints and failure modes. Second, while detection and localization have received attention, the computational overhead and latency implications of deploying these defenses in production systems remain underexplored. Third, the literature focuses primarily on English-language prompt injection, with limited attention to multilingual attacks and defenses.

Fourth, while real-world measurement has begun, longitudinal studies tracking attack evolution over extended periods are lacking. Fifth, the interaction between prompt injection and other LLM vulnerabilities (such as training data poisoning or model extraction) remains unexplored. Finally, there is limited work on user-facing interventions and education—how end users can be protected from or educated about prompt injection risks in consumer applications.

## Per-Paper Annotations

### Chen et al. (2025) - Backdoor-Powered Prompt Injection

**Research question**: Can backdoor-powered prompt injection attacks nullify existing prompt injection defense methods, including instruction hierarchy techniques?

**Methodology**: The authors explored backdoor-powered prompt injection attacks where attackers poison supervised fine-tuning samples to insert backdoors into models, then constructed a benchmark for comprehensive evaluation of these attacks against existing defense methods.

**Key findings**:
- Backdoor-powered prompt injection attacks can nullify existing prompt injection defense methods
- Even instruction hierarchy defense techniques are vulnerable to backdoor-powered attacks
- The attacks are more harmful than previous prompt injection attacks
- When triggers are activated, backdoored models execute injected instructions surrounded by the trigger

**Limitations**: Not stated in abstract.

### Chen et al. (2025) - Indirect Prompt Injection Detection

**Research question**: This paper investigates the feasibility of detecting and removing indirect prompt injection attacks in large language models.

**Methodology**: The authors construct a benchmark dataset for evaluation and assess existing LLMs and open-source detection models, while also training detection models using crafted training datasets. They evaluate two removal methods: segmentation removal and extraction removal.

**Key findings**:
- Most existing detection research focuses on direct prompt injection attacks rather than indirect scenarios where injected instructions come from external tools like search engines
- Current works mainly investigate injection detection methods and pay less attention to post-processing mitigation after detection
- The paper evaluates segmentation removal (segmenting injected documents and removing parts containing injected instructions) and extraction removal (training models to identify and remove injected instructions)
- A benchmark dataset was constructed specifically for evaluating indirect prompt injection detection and removal

**Limitations**: The abstract does not explicitly state limitations of the proposed methods or their performance metrics.

### Hossain et al. (2025)

**Research question**: Can a multi-agent defense framework employing specialized LLM agents in coordinated pipelines detect and neutralize prompt injection attacks in real-time?

**Methodology**: The authors developed a multi-agent defense framework with two architectures (sequential chain-of-agents pipeline and hierarchical coordinator-based system) and evaluated it on 55 unique prompt injection attacks across 8 categories totaling 400 attack instances on ChatGLM and Llama2 platforms.

**Key findings**:
- The multi-agent pipeline achieved 100% mitigation, reducing Attack Success Rate to 0% across all tested scenarios
- Baseline Attack Success Rates were 30% for ChatGLM and 20% for Llama2 without defense mechanisms
- The framework demonstrates robustness across multiple attack categories including direct overrides, code execution attempts, data exfiltration, and obfuscation techniques
- Both sequential chain-of-agents and hierarchical coordinator-based architectures were evaluated

**Limitations**: Not stated in abstract.

### Hung et al. (2024)

**Research question**: This paper investigates the underlying mechanisms of prompt injection attacks by analyzing attention patterns within large language models.

**Methodology**: The authors analyze attention patterns within LLMs to identify the 'distraction effect' where specific attention heads shift focus from original to injected instructions, and propose Attention Tracker, a training-free detection method that tracks attention patterns.

**Key findings**:
- Specific attention heads, termed 'important heads', shift focus from the original instruction to the injected instruction during prompt injection attacks
- Attention Tracker is a training-free detection method that does not require additional LLM inference
- The method shows an AUROC improvement of up to 10.0% over existing methods across diverse models, datasets, and attack types
- The approach performs well even on small LLMs and generalizes effectively across different scenarios

**Limitations**: The abstract does not explicitly state limitations of the Attention Tracker method.

### Jia et al. (2025) - Critical Evaluation of Defenses

**Research question**: This paper argues for the need to assess prompt injection defenses across two critical dimensions: effectiveness against diverse attacks and general-purpose utility without compromising LLM capabilities.

**Methodology**: The authors critically evaluate existing defenses using a principled approach that assesses effectiveness against both existing and adaptive prompt injection attacks, and evaluates general-purpose utility to ensure defenses don't compromise foundational LLM capabilities.

**Key findings**:
- Existing studies lack a principled approach to evaluating prompt injection defenses
- When assessed using a comprehensive evaluation methodology, existing defenses are not as successful as previously reported
- Defenses should be evaluated across effectiveness (against diverse target and injected prompts) and general-purpose utility (not compromising LLM capabilities)
- The work provides a foundation for evaluating future defenses and guiding their development

**Limitations**: The abstract does not explicitly state specific limitations beyond noting that existing defenses fail under comprehensive evaluation.

### Jia et al. (2025) - PromptLocate

**Research question**: This paper proposes PromptLocate, the first method for localizing injected prompts within contaminated data for post-attack forensic analysis and data recovery.

**Methodology**: PromptLocate comprises three steps: (1) splitting contaminated data into semantically coherent segments, (2) identifying segments contaminated by injected instructions, and (3) pinpointing segments contaminated by injected data.

**Key findings**:
- Prompt injection localization remains largely unexplored despite its growing importance for forensic analysis and data recovery
- PromptLocate is the first method specifically designed for localizing injected prompts
- The method accurately localizes injected prompts across eight existing and eight adaptive attacks
- The three-step approach effectively segments, identifies, and pinpoints contaminated segments

**Limitations**: The abstract does not explicitly state limitations of the PromptLocate method.

### Liu et al. (2025)

**Research question**: How can prompt injection attacks be detected effectively, including adaptive attacks that evade existing detection methods?

**Methodology**: The authors proposed DataSentinel, a game-theoretic method that formulates detection as a minimax optimization problem and uses a gradient-based approach to fine-tune an LLM by alternating between inner max and outer min problems to detect adaptive attacks.

**Key findings**:
- DataSentinel effectively detects both existing and adaptive prompt injection attacks
- The game-theoretic formulation uses minimax optimization to detect strategically adapted attacks
- The method was evaluated on multiple benchmark datasets and LLMs
- Existing detection methods have limited effectiveness against state-of-the-art and adaptive attacks

**Limitations**: Not stated in abstract.

### Shaheer et al. (2025)

**Research question**: How can prompt injection attacks be detected and mitigated in LLM-integrated web applications?

**Methodology**: The authors curated and augmented a prompt injection dataset based on the HackAPrompt Playground Submissions corpus and trained multiple classifiers including LSTM, feed forward neural networks, Random Forest, and Naive Bayes to detect malicious prompts.

**Key findings**:
- Multiple classifier approaches (LSTM, feed forward neural networks, Random Forest, Naive Bayes) were trained for prompt injection detection
- The dataset was curated and augmented from the HackAPrompt Playground Submissions corpus
- The proposed approach improves prompt injection detection and mitigation capabilities
- The method helps protect targeted applications and systems from compromise

**Limitations**: Not stated in abstract.

### Wang et al. (2026)

**Research question**: How can prompt injection attacks in web agents be detected and localized effectively given the limitations of existing methods?

**Methodology**: The authors proposed WebSentinel, a two-step approach where Step I extracts segments of interest that may be contaminated from a webpage, and Step II evaluates each segment by checking its consistency with the webpage content as context.

**Key findings**:
- WebSentinel is highly effective at detecting and localizing prompt injection attacks in webpages
- The method substantially outperforms baseline methods across multiple datasets
- Existing methods achieve limited effectiveness as their underlying assumptions often do not hold in the web-agent setting
- The code is publicly available at https://github.com/wxl-lxw/WebSentinel

**Limitations**: Not stated in abstract.

### Zhang et al. (2026)

**Research question**: This paper presents the first systematic study of prompt injection attacks in real-world LLM-based resume screening applications.

**Methodology**: The authors analyze approximately 200K real-world resumes collected over multiple years by hireEZ, design tailored methods to detect prompt injection in resumes, and conduct a comprehensive measurement study after validating detector precision on a small-scale dataset.

**Key findings**:
- Approximately 1% of resumes contain hidden prompt injections
- The prevalence of injected resumes has increased noticeably over the past one to two years
- More than 90% of injected prompts do not use explicit instructions
- The designed detectors achieve high precision and outperform state-of-the-art general-purpose detectors
- This provides the first evidence of large-scale prompt injection in real-world LLM-based applications

**Limitations**: The abstract does not explicitly state limitations of the detection methods or measurement study.

## References

Chen, Y., Li, H., Sui, Y., He, Y., Liu, Y., Song, Y., & Hooi, B. (2025). Can indirect prompt injection attacks be detected and removed? arXiv. https://arxiv.org/abs/2502.16580

Chen, Y., Li, H., Sui, Y., Song, Y., & Hooi, B. (2025). Backdoor-powered prompt injection attacks nullify defense methods. arXiv. https://arxiv.org/abs/2510.03705

Hossain, S. M. A., Khan Shayoni, R., Ameen, M. R., Islam, A., Mridha, M. F., & Shin, J. (2025). A multi-agent LLM defense pipeline against prompt injection attacks. arXiv. https://arxiv.org/abs/2509.14285

Hung, K.-H., Ko, C.-Y., Rawat, A., Chung, I.-H., Hsu, W. H., & Chen, P.-Y. (2024). Attention Tracker: Detecting prompt injection attacks in LLMs. arXiv. https://arxiv.org/abs/2411.00348

Jia, Y., Shao, Z., Liu, Y., Jia, J., Song, D., & Gong, N. Z. (2025). A critical evaluation of defenses against prompt injection attacks. arXiv. https://arxiv.org/abs/2505.18333

Jia, Y., Liu, Y., Shao, Z., Jia, J., & Gong, N. (2025). PromptLocate: Localizing prompt injection attacks. arXiv. https://arxiv.org/abs/2510.12252

Liu, Y., Jia, Y., Jia, J., Song, D., & Gong, N. Z. (2025). DataSentinel: A game-theoretic detection of prompt injection attacks. arXiv. https://arxiv.org/abs/2504.11358

Shaheer, S., Islam, G. M. R., Hamid, M. R., Khan, M. A. F., Faruk, M. O., & Nur, Y. (2025). Detecting prompt injection attacks against application using classifiers. arXiv. https://arxiv.org/abs/2512.12583

Wang, X., Liu, Y., Wang, Z., Song, D., & Gong, N. (2026). WebSentinel: Detecting and localizing prompt injection attacks for web agents. arXiv. https://arxiv.org/abs/2602.03792

Zhang, M., Jia, Y., Tan, Z., Jiang, S., Gong, N. Z., Chen, T., & Song, D. (2026). Measuring real-world prompt injection attacks in LLM-based resume screening. arXiv. https://arxiv.org/abs/2605.28999
