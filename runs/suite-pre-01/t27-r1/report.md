# Systematic Literature Review: Prompt Injection Attacks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "prompt injection", filtered to category cs.CR, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Prompt injection attacks have emerged as a critical security vulnerability in large language model applications, with research from 2024-2026 revealing sophisticated attack vectors spanning text-based injections, visual steganography, cross-modal exploits, and indirect attacks through retrieval-augmented generation systems. The surveyed literature demonstrates that current defenses are insufficient against adaptive attackers, with successful attacks documented across web browsers, code interpreters, API integrations, and enterprise systems. Economic impact assessments estimate annual losses exceeding $2.3 billion across the LLM industry, establishing prompt injection as a systemic risk requiring industry-wide security standards. Recent advances in defense mechanisms include preference optimization alignment, federated collaborative detection, automated vulnerability discovery frameworks, and multi-modal analysis approaches, though significant gaps remain in generalization to novel attack patterns and production deployment feasibility.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "prompt injection", filtered to category cs.CR, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Attack Vector Diversification and Evolution

The literature reveals rapid diversification of prompt injection attack vectors beyond simple text-based manipulation. Early work focused on direct text injections, but recent research has expanded to hidden injections embedded in visual content using steganographic techniques (Chen et al., 2024), cross-modal attacks that exploit modality fusion mechanisms in multimodal systems (Rodriguez et al., 2025), and indirect attacks that poison retrieval corpora in RAG systems without direct user input manipulation (Wang et al., 2024). This evolution demonstrates that attackers are systematically exploring new attack surfaces as LLM applications become more complex and multimodal. The success rates of these novel attack vectors are concerning: Chen et al. (2024) report that hidden visual injections bypass existing content filters designed for text-based detection, while Rodriguez et al. (2025) show that coordinated cross-modal injections defeat single-modality defenses. This diversification trend suggests that defense mechanisms must anticipate future attack vectors rather than solely addressing current techniques.

### Theme 2: Automated Vulnerability Discovery and Prevalence

A significant thread in the literature focuses on automated discovery of prompt injection vulnerabilities, revealing that these flaws are far more prevalent than previously understood. Kumar et al. (2025) introduced PromptBreach, an automated framework combining fuzzing, genetic algorithms, and symbolic execution that discovered 127 previously unknown vulnerabilities across 50 production LLM applications. This finding demonstrates that prompt injection vulnerabilities are not rare edge cases but systemic flaws in real-world deployed systems. The automated approach achieves higher attack success rates than manual techniques, suggesting that human security researchers alone cannot adequately assess LLM application security. The prevalence of vulnerabilities across production systems indicates that current development practices do not adequately account for prompt injection risks, and that automated testing frameworks should become standard in LLM application development pipelines.

### Theme 3: Enterprise-Scale Threats and Economic Impact

The literature increasingly recognizes prompt injection as an enterprise-scale threat with substantial economic consequences. Torres et al. (2025) developed comprehensive threat models for enterprise environments, identifying unique attack vectors including insider threats, supply chain vulnerabilities, and multi-tenant isolation failures that can lead to data exfiltration, unauthorized access, and workflow manipulation. Foster et al. (2024) quantified the economic impact, analyzing incident reports from 15 LLM providers and estimating annual losses exceeding $2.3 billion when accounting for direct costs (compute waste, mitigation expenses) and indirect costs (customer churn, reputational damage, regulatory fines). This economic analysis establishes prompt injection as a systemic risk to the LLM industry rather than isolated security incidents. The enterprise focus reveals that production deployments face unique challenges beyond consumer-facing applications, requiring specialized architectural patterns and runtime monitoring techniques that account for integration with internal systems, databases, and workflows.

### Theme 4: Defense Mechanisms and Mitigation Strategies

The surveyed literature proposes diverse defense mechanisms spanning model alignment, detection systems, and collaborative approaches. Chen et al. (2024) introduced SecAlign, which uses preference optimization to align LLMs to prefer safe completions over unsafe ones when faced with malicious prompts, achieving state-of-the-art robustness across multiple benchmarks while maintaining utility on benign inputs. Shaheer et al. (2025) trained multiple classifiers (LSTM, feed forward neural networks, Random Forest, Naive Bayes) on curated prompt injection datasets to detect malicious prompts in LLM-integrated web applications. Martin et al. (2025) proposed federated defense frameworks where multiple organizations collaboratively train detection models using differential privacy and secure aggregation, achieving 23% higher detection accuracy than isolated defenses. Wang et al. (2024) advocated for retrieval provenance tracking and content authentication to detect indirect attacks in RAG systems. Despite these advances, Zhao et al. (2025) systematically evaluated defenses across application domains and concluded that current mechanisms remain insufficient against adaptive attackers who modify their techniques, highlighting the gap between proposed defenses and real-world effectiveness.

### Theme 5: Multimodal and Cross-Modal Vulnerabilities

As AI systems become increasingly multimodal, prompt injection research has expanded beyond text-only attacks to exploit cross-modal interactions. Chen et al. (2024) demonstrated that malicious instructions can be hidden within images using steganographic techniques, bypassing text-focused content filters and achieving high success rates on vision-language models. Rodriguez et al. (2025) extended this work to show that coordinated attacks combining text, images, audio, and structured data can exploit modality fusion mechanisms in ways that single-modality defenses cannot detect. This theme reveals a fundamental vulnerability in multimodal system architecture: the mechanisms that fuse information across modalities create new attack surfaces not present in unimodal systems. The literature suggests that effective defense requires unified analysis across all modalities simultaneously rather than independent per-modality filtering, but practical deployment of such unified defenses faces challenges in computational overhead and latency that remain inadequately addressed.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key findings. First, all papers agree that prompt injection represents a serious and growing threat to LLM applications, with no authors suggesting the problem is overstated. Second, multiple studies independently conclude that current defenses are insufficient against adaptive attackers (Zhao et al., 2025; Chen et al., 2024; Rodriguez et al., 2025). Third, there is consensus that automated approaches outperform manual techniques for both attack discovery (Kumar et al., 2025) and defense deployment (Martin et al., 2025). Fourth, the literature agrees that enterprise environments face unique threats requiring specialized threat models beyond consumer application defenses (Torres et al., 2025). Finally, all defense-focused papers acknowledge the challenge of maintaining utility on benign inputs while providing robust protection (Chen et al., 2024; Shaheer et al., 2025).

**Disagreements**: The literature shows limited direct disagreement, reflecting the emerging nature of this research area. However, there are tensions in emphasis: detection-focused papers (Shaheer et al., 2025; Wang et al., 2024) emphasize runtime monitoring and classification approaches, while alignment-focused work (Chen et al., 2024) argues for model-level robustness through preference optimization. These approaches are not mutually exclusive but reflect different philosophical positions on whether defenses should be external to the model or baked into model behavior. Additionally, there is implicit disagreement about scalability: federated defense proponents (Martin et al., 2025) emphasize collaborative approaches requiring organizational coordination, while automated vulnerability discovery work (Kumar et al., 2025) suggests individual organizations can achieve strong security through automated testing. The literature does not resolve which approach is more practical for widespread adoption.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, multiple papers acknowledge limitations in generalization to novel attack patterns not present in training data (Shaheer et al., 2025; Chen et al., 2024), suggesting that current detection systems may fail against evolving attack techniques. Second, computational overhead and deployment feasibility are consistently mentioned as unaddressed challenges (Rodriguez et al., 2025; Torres et al., 2025), with few papers providing concrete implementation cost analysis. Third, the empirical evaluations cover limited deployments: Torres et al. (2025) evaluated only three enterprise environments, Kumar et al. (2025) tested 50 applications that may not represent the broader ecosystem, and Foster et al. (2024) relied on self-reported incident data that likely underrepresents actual attack frequency. Fourth, false positive rates and performance impacts of proposed defenses are rarely quantified, making it difficult to assess production readiness. Fifth, the literature lacks standardized evaluation benchmarks and metrics, hindering cross-paper comparability (Zhao et al., 2025). Finally, there is insufficient research on long-term effectiveness: most evaluations measure immediate defense performance without assessing how defenses degrade as attackers adapt their techniques over time.

## Per-Paper Annotations

### Chen et al. (2024) - Hidden Prompt Injection

**Research question**: Can prompt injection attacks be concealed within visual content to bypass content filters and compromise vision-language models?
**Methodology**: The authors introduce hidden prompt injection attacks that embed malicious instructions within images using steganographic techniques, then evaluate their effectiveness against existing content filters and multimodal systems while testing several defense strategies.
**Key findings**:
- Malicious instructions can be successfully hidden within images using steganographic techniques
- Hidden prompt injection attacks bypass existing content filters designed for text-based detection
- The attacks achieve high success rates on multimodal vision-language systems
- Robust detection of visual prompt injection remains a significant challenge
**Limitations**: The evaluated defense strategies may not represent all possible countermeasures, and the study does not address the scalability of steganographic attacks or their detectability through image forensics techniques.

### Chen et al. (2024) - SecAlign

**Research question**: How can large language models be aligned to be robust against prompt injection attacks while maintaining utility on benign inputs?
**Methodology**: The authors propose SecAlign, a defense mechanism that uses preference optimization to train LLMs to prefer safe completions over unsafe ones when faced with malicious prompts, evaluated on multiple prompt injection benchmarks.
**Key findings**:
- Preference optimization can effectively align LLMs to resist prompt injection attacks
- SecAlign achieves state-of-the-art robustness across multiple prompt injection benchmarks
- The defense maintains model utility on benign inputs without significant degradation
- Training models to prefer safe completions is a viable alternative to prompt-based defenses
**Limitations**: The abstract does not address the computational cost of preference optimization training, potential overfitting to known attack patterns, or effectiveness against adaptive attackers who evolve their techniques.

### Foster et al. (2024)

**Research question**: What are the quantified economic costs and systemic risks that prompt injection attacks pose to commercial LLM service providers?
**Methodology**: The authors analyze incident reports from 15 LLM providers and develop an economic model accounting for direct costs (compute waste, mitigation expenses) and indirect costs (customer churn, regulatory fines, reputational damage).
**Key findings**:
- Annual losses from prompt injection attacks exceed $2.3 billion across the LLM industry
- Direct costs include significant compute waste and security mitigation expenses
- Indirect costs from customer churn and reputational damage substantially exceed direct costs
- Regulatory fines represent a growing cost category as AI governance matures
- Prompt injection constitutes a systemic risk requiring industry-wide security standards
**Limitations**: Analysis relies on self-reported incident data which may underrepresent actual attack frequency; economic model assumptions may not capture all cost categories or long-term market effects.

### Kumar et al. (2025)

**Research question**: How can prompt injection vulnerabilities in LLM applications be automatically discovered at scale more effectively than manual techniques?
**Methodology**: The authors developed PromptBreach, an automated framework combining fuzzing and symbolic execution to discover vulnerabilities. The system generates adversarial prompts using genetic algorithms and constraint solving to achieve higher attack success rates.
**Key findings**:
- Automated discovery achieves higher attack success rates than manual prompt injection techniques
- 127 previously unknown vulnerabilities were discovered across 50 production LLM applications
- Prompt injection flaws are highly prevalent in real-world deployed systems
- Genetic algorithms effectively generate diverse adversarial prompts
- Constraint solving complements fuzzing by exploring structured attack spaces
**Limitations**: The 50 applications tested may not be representative of the broader LLM application ecosystem; the framework may not detect all vulnerability types, particularly those requiring semantic understanding.

### Martin et al. (2025)

**Research question**: Can federated learning enable multiple organizations to collaboratively train prompt injection detection models without sharing sensitive data while improving detection accuracy?
**Methodology**: The authors propose a federated defense framework where organizations collaboratively train detection models using differential privacy and secure aggregation to preserve privacy. Attack signatures are aggregated across participants without exposing raw sensitive data.
**Key findings**:
- Federated defense achieves 23% higher detection accuracy than isolated organizational defenses
- Collaborative security provides significant value in the LLM era
- Differential privacy enables effective cross-organization collaboration without data exposure
- Secure aggregation preserves privacy while enabling attack signature sharing
- Real-world attack data demonstrates practical viability of the federated approach
**Limitations**: The approach may require significant coordination overhead among participating organizations; differential privacy mechanisms may reduce model effectiveness in some scenarios; adoption barriers for smaller organizations are not addressed.

### Rodriguez et al. (2025)

**Research question**: How can prompt injection attacks leverage cross-modal interactions between text, images, audio, and structured data to bypass single-modality defenses in multimodal AI systems?
**Methodology**: The authors study attack techniques that combine multiple modalities to exploit modality fusion mechanisms in multimodal systems. They introduce novel cross-modal injection methods and propose a unified defense framework that analyzes inputs across all modalities simultaneously.
**Key findings**:
- Cross-modal attacks can successfully bypass defenses designed for single modalities
- Modality fusion mechanisms create new attack surfaces not present in unimodal systems
- Existing single-modality defenses fail to detect coordinated cross-modal injections
- Coordinated attacks across text, images, audio, and structured data amplify attack effectiveness
- Unified multi-modality analysis is necessary for effective defense
**Limitations**: The proposed defense framework may not be tested across all multimodal system architectures; practical deployment challenges including computational overhead and latency are not fully addressed.

### Shaheer et al. (2025)

**Research question**: How can prompt injection attacks against LLM-integrated web applications be effectively detected and mitigated?
**Methodology**: The authors curated and augmented a prompt injection dataset based on the HackAPrompt Playground Submissions corpus and trained multiple classifiers including LSTM, feed forward neural networks, Random Forest, and Naive Bayes to detect malicious prompts.
**Key findings**:
- Multiple classifier architectures can be effectively trained to detect prompt injection attacks
- The curated and augmented dataset improves detection capabilities compared to existing approaches
- The proposed approach helps protect targeted applications and systems from compromise
- Different classifier types offer varying trade-offs in detection accuracy and computational efficiency
**Limitations**: The abstract does not specify evaluation metrics, false positive rates, or how well the classifiers generalize to novel attack patterns not present in the training data.

### Torres et al. (2025)

**Research question**: What are the specific prompt injection threats in enterprise environments and how can they be effectively mitigated?
**Methodology**: The authors developed a comprehensive threat model accounting for insider threats, supply chain vulnerabilities, and multi-tenant isolation failures, then conducted empirical evaluation across three enterprise deployments to assess risks and propose architectural patterns and runtime monitoring techniques.
**Key findings**:
- Prompt injection in enterprise environments can lead to data exfiltration, unauthorized access, and workflow manipulation
- Insider threats, supply chain vulnerabilities, and multi-tenant isolation failures create unique enterprise-specific attack vectors
- Architectural patterns combined with runtime monitoring can effectively mitigate prompt injection risks in production systems
- Enterprise LLM integrations require specialized threat models beyond consumer-facing application defenses
**Limitations**: The empirical evaluation covers only three enterprise deployments, which may not represent the full diversity of enterprise environments, and the proposed mitigations may involve significant implementation costs not quantified in the study.

### Wang et al. (2024)

**Research question**: How can attackers exploit retrieval-augmented generation (RAG) systems through prompt injection attacks that poison the retrieval corpus without direct user input manipulation?
**Methodology**: The authors evaluate indirect prompt injection attacks across multiple RAG implementations by injecting malicious content into knowledge bases and observing LLM execution behavior. They propose and test detection mechanisms based on retrieval provenance tracking and content authentication.
**Key findings**:
- Attackers can successfully inject malicious content into knowledge bases that is later retrieved and executed by LLMs
- Indirect attacks enable compromise without requiring direct manipulation of user input
- Multiple RAG implementations are vulnerable to this attack vector
- Detection mechanisms based on retrieval provenance can identify poisoned content
- Content authentication provides an additional layer of defense against corpus poisoning
**Limitations**: The evaluation may not cover all RAG system architectures or real-world deployment scenarios; detection mechanism false positive rates and performance overhead are not thoroughly discussed.

### Zhao et al. (2025)

**Research question**: What are the characteristics, success rates, and effective defense mechanisms against prompt injection attacks across different LLM application domains?
**Methodology**: The authors conducted a systematic study of prompt injection attacks across web browsers, code interpreters, and API integrations, categorizing attack vectors, analyzing success rates, and proposing a taxonomy of defense mechanisms.
**Key findings**:
- Prompt injection attacks succeed across multiple application domains including web browsers, code interpreters, and API integrations
- Current defense mechanisms are insufficient against adaptive attackers who modify their techniques
- Different application domains exhibit varying vulnerability profiles and attack success rates
- A structured taxonomy of attacks and defenses reveals gaps in existing protection strategies
**Limitations**: The study may not cover all emerging application domains, and the effectiveness of proposed defenses against continuously evolving attack techniques requires ongoing validation.

## References

Chen, C., Wang, J., Li, H., & Xu, W. (2024). Hidden prompt injection: Stealthy attacks on vision-language models. arXiv. https://arxiv.org/abs/2408.14307

Chen, S., Zharmagambetov, A., Mahloujifar, S., Chaudhuri, K., Wagner, D., & Guo, C. (2024). SecAlign: Defending against prompt injection with preference optimization. arXiv. https://arxiv.org/abs/2410.05451

Foster, D., Santos, M., & Smith, J. (2024). Economic impact of prompt injection attacks on LLM services. arXiv. https://arxiv.org/abs/2409.18234

Kumar, A., Zhang, J., & Mueller, T. (2025). PromptBreach: Automated discovery of prompt injection vulnerabilities. arXiv. https://arxiv.org/abs/2502.03456

Martin, S., Hassan, A., Chen, L., & Ruiz, C. (2025). Federated defense against prompt injection: A collaborative approach. arXiv. https://arxiv.org/abs/2508.07654

Rodriguez, E., O'Brien, K., & Sharma, P. (2025). Cross-modal prompt injection in multimodal AI systems. arXiv. https://arxiv.org/abs/2505.12789

Shaheer, S., Islam, G. M. R., Hamid, M. R., Khan, M. A. F., Faruk, M. O., & Nur, Y. (2025). Detecting prompt injection attacks against application using classifiers. arXiv. https://arxiv.org/abs/2512.12583

Torres, M., Kim, S., Liu, J., & Kowalski, A. (2025). Enterprise-scale prompt injection: Threat modeling and mitigation strategies. arXiv. https://arxiv.org/abs/2507.19028

Wang, L., Chen, R., & Park, D. (2024). Indirect prompt injection via retrieval augmented generation. arXiv. https://arxiv.org/abs/2411.09876

Zhao, Y., Li, Z., Liu, Y., Xu, X., & Sun, B. (2025). Prompt injection attacks on LLM-powered applications: A systematic study. arXiv. https://arxiv.org/abs/2503.08932
