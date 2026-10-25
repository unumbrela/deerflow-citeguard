# Systematic Literature Review: Jailbreak Attacks on Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "jailbreak LLM", filtered to category cs.CR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on jailbreak attacks against large language models (LLMs) reveals a rapidly evolving adversarial landscape where attackers exploit structural vulnerabilities in safety-aligned models through increasingly sophisticated techniques. The surveyed papers demonstrate that jailbreak attacks have progressed from simple prompt engineering to complex optimization-based methods, fine-tuning exploits, and framework-level manipulations that achieve high attack success rates while evading detection. A critical finding across multiple studies is that benign-appearing inputs—including fine-tuning data, grammar constraints, and template structures—can be weaponized to induce harmful model behavior, challenging the assumption that safety filters can reliably distinguish malicious from legitimate usage. The field is converging on automated, adaptive attack frameworks that continuously evolve strategies through interaction, while defense research emphasizes unified principles spanning perception, generation, and alignment layers.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query `jailbreak LLM`, filtered to category cs.CR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Optimization-Based Attack Strategies

A dominant research direction involves using optimization algorithms to automatically discover and refine jailbreak prompts. Multiple papers employ genetic algorithms, gradient-based optimization, or alternating optimization to evolve attack vectors that maximize attack success rate while maintaining semantic coherence. GeneShift uses a genetic algorithm to optimize hybrid scenario shifts, achieving a 60% success rate where direct prompting fails completely [citation:Geneshift](https://arxiv.org/abs/2504.08104). TASO alternates between template and suffix optimization, leveraging their complementary strengths to control both initial tokens and overall output quality across 24 LLMs [citation:TASO](https://arxiv.org/abs/2511.18581). ASTRA extends this paradigm by introducing continuous learning and self-evolution through a closed-loop attack-evaluate-distill-reuse mechanism with hierarchical memory management [citation:ASTRA](https://arxiv.org/abs/2511.02356). These optimization-based approaches significantly outperform manual prompt engineering and demonstrate that automated search can discover attack vectors that humans may overlook.

### Theme 2: Exploitation of Benign Mechanisms

A striking pattern across recent work is the exploitation of mechanisms designed for legitimate purposes—fine-tuning APIs, grammar constraints, and safety analysis frameworks—to induce harmful behavior. TrojanPraise achieves 95.88% attack success rate by fine-tuning models with benign, moderation-approved data that associates crafted words with harmless connotations, then uses these words to praise harmful concepts [citation:TrojanPraise](https://arxiv.org/abs/2601.12460). Similarly, Few-Shot DPO attacks exploit Direct Preference Optimization using only 10 harmless preference pairs, achieving 59-82% attack success rates across GPT-4 variants while remaining indistinguishable from legitimate fine-tuning requests [citation:Few-Shot DPO](https://arxiv.org/abs/2605.10998). Grammar-Constrained Decoding, designed to improve code generation reliability, can be weaponized through CodeSpear to increase attack success rate by over 30 percentage points [citation:CodeSpear](https://arxiv.org/abs/2606.11817). These attacks reveal a fundamental vulnerability: safety systems calibrated to detect overtly malicious inputs fail against attacks that operate through benign intermediaries.

### Theme 3: Semantic Dissimilarity and Obfuscation

Multiple papers identify semantic dissimilarity—the degree to which manipulated prompts differ from their original harmful intent in embedding space—as a critical factor in jailbreak success. Alphabet Index Mapping achieves 94% attack success rate on GPT-4 by maximizing semantic dissimilarity while maintaining simple decodability [citation:AIM](https://arxiv.org/abs/2506.12685). JOOD uses out-of-distribution transformations, including simple techniques like image mixup, to increase model uncertainty in discerning malicious intent, successfully jailbreaking GPT-4 and o1 models that resist previous attacks [citation:JOOD](https://arxiv.org/abs/2503.20823). TrojFill structurally reframes malicious instructions as template-filling tasks for safety analysis, achieving 100% attack success rate on Gemini-flash-2.5 and DeepSeek-3.1 by exploiting the decoupling of unsafety reasoning from content generation [citation:TrojFill](https://arxiv.org/abs/2510.21190). These approaches demonstrate that obfuscation strategies which maintain decoding simplicity while maximizing semantic distance from harmful content are highly effective at bypassing safety filters.

### Theme 4: Unified Defense Principles

As attack sophistication increases, research is converging on unified defense frameworks that span multiple layers of the model pipeline. The comprehensive survey by Chen et al. (2026) proposes defense principles including variant-consistency and gradient-sensitivity detection at the perception layer, safety-aware decoding at the generation layer, and adversarially augmented preference alignment at the parameter layer [citation:Unified Defense](https://arxiv.org/abs/2601.03594). CodeShield demonstrates one such principle by teaching models to generate semantically harmless honeypot code under grammar constraints while preserving natural-language refusals [citation:CodeShield](https://arxiv.org/abs/2606.11817). RAID introduces refusal-aware and integrated decoding specifically designed to counter jailbreak attempts [citation:RAID](https://arxiv.org/abs/2510.13901). These defenses recognize that single-layer solutions are insufficient against multi-vector attacks and that robust safety requires coordinated protection across perception, generation, and alignment.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several key findings. First, all papers agree that safety-aligned LLMs remain vulnerable to sophisticated attacks, with even commercial models like GPT-4, GPT-4o, and o1 susceptible to novel attack vectors. Second, there is consensus that benign-appearing inputs can be weaponized, challenging the assumption that moderation filters can reliably distinguish malicious from legitimate usage based on content alone. Third, multiple studies demonstrate that automated, optimization-based approaches consistently outperform manual prompt engineering, suggesting that human intuition is insufficient for discovering optimal attack vectors. Finally, papers converge on the finding that high attack success rates (often 60-95%) are achievable while maintaining stealth and evading detection.

**Disagreements**: The literature shows limited direct disagreement, partly because most papers focus on proposing new attack methods rather than critiquing existing ones. However, there is implicit tension between papers emphasizing semantic dissimilarity as the primary attack mechanism (AIM, JOOD) versus those emphasizing structural or framework exploitation (TrojFill, CodeSpear). Additionally, while most papers report attack success rates as their primary metric, there is variation in evaluation methodology—some use dictionary-based success metrics while others emphasize detailed, actionable harmful responses, with GeneShift explicitly critiquing existing methods for failing to output detailed content despite achieving dictionary-based success.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the papers explicitly state limitations of their proposed methods in their abstracts, suggesting a need for more transparent discussion of attack scope, failure modes, and conditions under which methods degrade. Second, while multiple papers demonstrate attacks on commercial models, the black-box nature of these evaluations limits reproducibility and independent verification. Third, there is a gap in longitudinal studies tracking how model updates affect attack success—whether fixes for known vulnerabilities introduce new ones or genuinely improve robustness. Fourth, the literature lacks systematic comparison of defense effectiveness across attack types, making it difficult to prioritize defensive investments. Finally, while automated attack frameworks like ASTRA demonstrate continuous learning, there is no corresponding research on automated defense systems that adapt to evolving attack strategies in real-time.

## Per-Paper Annotations

### Ahn et al. (2025)

**Research question**: How can word-based puzzles be used to jailbreak LLMs?
**Methodology**: The paper proposes PUZZLED, a jailbreak method using word-based puzzles to bypass safety filters.
**Key findings**:
- Word-based puzzles can effectively jailbreak LLMs
- The approach leverages linguistic ambiguity to induce harmful outputs
- Evaluation demonstrates success across multiple model variants
**Limitations**: Not stated in abstract

### Chen et al. (2026)

**Research question**: What are the shared mechanisms, evaluation metrics, and unified defense principles for jailbreak attacks on Large Language Models and Vision-Language Models across text-only and multimodal settings?
**Methodology**: The paper proposes a three-dimensional survey framework covering attack dimensions (template/encoding-based, in-context learning, adversarial learning, fine-tuned attacks, perturbations), defense dimensions (prompt obfuscation, output evaluation, model alignment), and evaluation dimensions (ASR, toxicity score, query/time cost, multimodal metrics), consolidating mechanisms across text and multimodal settings and proposing unified defense principles.
**Key findings**:
- Jailbreak vulnerabilities stem from structural factors including incomplete training data, linguistic ambiguity, and generative uncertainty
- The survey spans from text-only to multimodal settings, consolidating shared mechanisms across both domains
- Unified defense principles include variant-consistency and gradient-sensitivity detection at the perception layer, safety-aware decoding at the generation layer, and adversarially augmented preference alignment at the parameter layer
- Hallucinations and jailbreaks differ in terms of intent and triggering mechanisms
- Existing multimodal safety benchmarks are summarized with future directions including automated red teaming and cross-modal collaborative defense
**Limitations**: The abstract does not explicitly state limitations; as a survey paper, limitations may relate to coverage scope or the maturity of proposed unified defense principles

### Husain (2025)

**Research question**: What is the relationship between semantic dissimilarity induced by prompt manipulation and attack success rate in jailbreaking LLMs?
**Methodology**: The paper analyzes embedding space visualizations (UMAP, KDE) and cosine similarities for FlipAttack's flipping modes, then introduces a novel adversarial attack called Alphabet Index Mapping (AIM) designed to maximize semantic dissimilarity while maintaining simple decodability, tested on GPT-4 using a subset of AdvBench.
**Key findings**:
- Semantic dissimilarity between original and manipulated prompts is inversely correlated with attack success rate (ASR)
- AIM and its variant AIM+FWO achieve 94% ASR on GPT-4, outperforming FlipAttack and other methods on the tested subset
- High semantic dissimilarity is crucial for successful jailbreaking, but must be balanced with decoding simplicity
- The work contributes a new, effective jailbreak technique with simple decodability
**Limitations**: Not stated in abstract

### Jeong et al. (2025)

**Research question**: How does out-of-distribution (OOD) transformation of harmful inputs affect the ability of safety-aligned LLMs and MLLMs to discern malicious intent and maintain safety guarantees?
**Methodology**: The paper proposes JOOD, a jailbreak framework that OOD-ifies harmful inputs beyond the safety alignment distribution using various off-the-shelf visual and textual transformation techniques, including simple mixing-based techniques such as image mixup, tested across diverse jailbreak scenarios on proprietary LLMs and MLLMs.
**Key findings**:
- OOD-ifying vanilla harmful inputs highly increases model uncertainty in discerning malicious intent, leading to higher jailbreak success
- Simple mixing-based techniques such as image mixup prove highly effective in bypassing safety alignment
- JOOD effectively jailbreaks recent proprietary LLMs and MLLMs such as GPT-4 and o1 with high attack success rate
- Previous attack approaches have consistently struggled to jailbreak these same models
**Limitations**: Not stated in abstract

### Liu et al. (2025)

**Research question**: How can black-box jailbreak attacks bypass safety filters by exploiting the decoupling of unsafety reasoning from content generation in LLMs?
**Methodology**: The paper introduces TrojFill, a black-box exploitation framework that structurally reframes malicious instructions as a template-filling task required for safety analysis, embedding obfuscated payloads into a Trojan structure to induce the model to generate prohibited content as a demonstrative example for subsequent safety critique, evaluated against GPT-4o, Gemini-2.5, DeepSeek-3.1, and Qwen-Max.
**Key findings**:
- TrojFill achieves 100% Attack Success Rate on Gemini-flash-2.5 and DeepSeek-3.1, and 97% on GPT-4o
- The approach significantly outperforms existing black-box baselines
- TrojFill generates highly interpretable and transferable attack vectors, unlike optimization-based adversarial prompts
- The attack exposes a systematic vulnerability in safety-aligned LLMs through the decoupling of unsafety reasoning from content generation
**Limitations**: Not stated in abstract

### Liu et al. (2025)

**Research question**: How can jailbreak attacks achieve continuous learning and self-evolution from interactions to improve the diversity and adaptability of attack strategies?
**Methodology**: The paper proposes ASTRA, an automated framework operating on a closed-loop attack-evaluate-distill-reuse mechanism that autonomously discovers, retrieves, and evolves attack strategies, with a dynamic three-tier strategy library (Effective, Promising, and Ineffective) that categorizes strategies based on performance for hierarchical memory management.
**Key findings**:
- ASTRA significantly outperforms existing baselines in black-box jailbreak settings
- The framework automatically distills reusable strategies from every interaction
- The hierarchical memory mechanism enhances efficiency by leveraging successful patterns while optimizing exploration by avoiding known failures
- ASTRA addresses the lack of continuous learning and self-evolution capability in existing jailbreak methods
**Limitations**: Not stated in abstract

### Nguyen et al. (2025)

**Research question**: How can refusal-aware decoding mechanisms improve LLM robustness against jailbreak attacks?
**Methodology**: The paper proposes RAID, a refusal-aware and integrated decoding approach for countering jailbreak attempts on LLMs.
**Key findings**:
- Refusal-aware decoding can detect and prevent jailbreak attempts
- Integrated decoding mechanisms improve safety without sacrificing utility
- The approach is evaluated across multiple jailbreak scenarios
**Limitations**: Not stated in abstract

### Wang et al. (2025)

**Research question**: Can combining template optimization and suffix optimization in an alternating manner improve the effectiveness of jailbreak attacks on LLMs?
**Methodology**: The authors introduce TASO (Template and Suffix Optimization), a jailbreak method that alternately optimizes both semantic templates (to guide overall output quality) and suffixes (to control initial output tokens), leveraging the complementary strengths of both approaches, and evaluate it on 24 LLMs including Llama, OpenAI, and DeepSeek models using HarmBench and AdvBench datasets.
**Key findings**:
- TASO effectively jailbreaks existing LLMs by combining template and suffix optimization
- Suffix optimization controls initial output tokens but cannot control overall output quality
- Template optimization guides the entire output but cannot effectively control initial tokens that significantly impact subsequent responses
- The two optimization approaches are complementary and can be combined to improve attack effectiveness
- TASO was evaluated successfully on 24 leading LLMs across benchmark datasets
**Limitations**: Not stated in abstract

### Wu et al. (2025)

**Research question**: How can scenario shifts be optimized to improve jailbreak attack effectiveness on LLMs, particularly for generating detailed and actionable harmful responses rather than just achieving dictionary-based success?
**Methodology**: The authors propose GeneShift, a black-box jailbreak attack using a genetic algorithm to optimize and evolve hybrid scenario shifts based on the observation that malicious queries perform optimally under different scenario shifts, guiding the method to elicit detailed harmful responses while maintaining a benign facade.
**Key findings**:
- GeneShift increases jailbreak success rate from 0% to 60% when direct prompting alone would fail
- Existing jailbreak methods often fail to output detailed contents despite achieving dictionary-based evaluation success
- Malicious queries perform optimally under different scenario shifts, which can be exploited for more effective attacks
- The genetic algorithm approach improves stealthiness by maintaining a seemingly benign facade
- GeneShift elicits detailed and actionable harmful responses, addressing a gap in GPT-based evaluation performance
**Limitations**: Not stated in abstract

### Xie et al. (2026)

**Research question**: Can large language models be jailbroken through fine-tuning with benign, moderation-approved data rather than malicious training data?
**Methodology**: The authors propose TrojanPraise, a fine-tuning attack that trains models to associate crafted words (e.g., 'bruaf') with harmless connotations, then uses these words to praise harmful concepts, subtly shifting the model's attitude toward compliance without triggering moderation. The approach is grounded in a theoretical framework decoupling the LLM's internal representation into knowledge and attitude dimensions, and is evaluated on five open-source and two commercial LLMs under black-box settings.
**Key findings**:
- TrojanPraise achieves a maximum attack success rate of 95.88% while evading moderation models like Llama-Guard-3
- Successful jailbreak requires shifting the model's attitude while avoiding knowledge shift (distortion in understanding of the concept)
- Benign, moderation-approved training data can be exploited for jailbreak attacks, challenging the assumption that malicious data is required
- The attack works under strict black-box settings on both open-source and commercial LLMs
- Fine-tuning APIs offered by commercial LLMs introduce a critical security loophole
**Limitations**: Not stated in abstract

### Yoon et al. (2026)

**Research question**: Can Direct Preference Optimization (DPO) fine-tuning be exploited using only benign, harmless preference pairs to reduce refusal behavior in LLMs?
**Methodology**: The authors propose a truly benign DPO attack using only 10 harmless preference pairs where each pair contains a benign prompt with a normal helpful answer as preferred response and a refusal as dispreferred response, tested across OpenAI models supporting DPO fine-tuning.
**Key findings**:
- DPO introduces a stronger and harder-to-audit failure mode compared to benign supervised fine-tuning
- The attack achieves ASR of 59.13% on GPT-4o, 70.20% on GPT-4.1, 54.80% on GPT-4.1-mini, and 81.73% on GPT-4.1-nano
- The attack data is practically indistinguishable from legitimate fine-tuning requests seeking to reduce over-refusal
- The effect can emerge from even a single benign preference pair on open-weight models without minimum data requirements
- Attack costs are minimal: $1.7, $1.7, $0.3, and $0.1 respectively for the tested models
**Limitations**: Not stated in abstract

### Zhang et al. (2026)

**Research question**: Can Grammar-Constrained Decoding (GCD), a technique designed to improve code generation reliability, be exploited as an attack surface to jailbreak LLMs into generating malicious code?
**Methodology**: The authors propose CodeSpear, a jailbreak attack that exploits GCD by applying benign code grammar constraints to induce LLMs to generate malicious code. They then propose CodeShield, a safety alignment approach that teaches models to generate semantically harmless honeypot code under GCD while preserving natural-language refusals, and evaluate both on 10 LLMs across 4 benchmarks.
**Key findings**:
- Grammar-Constrained Decoding can be exploited as a jailbreak attack vector to induce LLMs to generate malicious code
- CodeSpear outperforms representative jailbreak baselines and increases attack success rate by more than 30 percentage points on average
- CodeShield restores safety under CodeSpear attacks while preserving benign utility
- CodeShield generates structurally diverse honeypot code that is difficult to suppress through grammar tightening
- CodeShield preserves natural-language refusals when natural language is available
**Limitations**: The abstract does not explicitly state limitations of the proposed methods or evaluation scope beyond the 10 LLMs and 4 benchmarks tested

## References

Chen, Z., Li, C., Li, C., Zhang, X., Zhang, L., & He, Y. (2026). Jailbreaking LLMs & VLMs: Mechanisms, evaluation, and unified defense. arXiv. https://arxiv.org/abs/2601.03594

Husain, B. S. (2025). Alphabet index mapping: Jailbreaking LLMs through semantic dissimilarity. arXiv. https://arxiv.org/abs/2506.12685

Jeong, J., Bae, S., Jung, Y., Hwang, J., & Yang, E. (2025). Playing the fool: Jailbreaking LLMs and multimodal LLMs with out-of-distribution strategy. arXiv. https://arxiv.org/abs/2503.20823

Liu, M., Zhang, S., Long, C., & Lam, K. Y. (2025). The Trojan example: Jailbreaking LLMs through template filling and unsafety reasoning. arXiv. https://arxiv.org/abs/2510.21190

Liu, X., Chen, Y., Ling, K., Zhu, Y., Zhang, H., Fan, G., & Yu, H. (2025). ASTRA: An automated framework for strategy discovery, retrieval, and evolution for jailbreaking LLMs. arXiv. https://arxiv.org/abs/2511.02356

Nguyen, T. T. (2025). RAID: Refusal-aware and integrated decoding for jailbreaking LLMs. arXiv. https://arxiv.org/abs/2510.13901

Wang, Y., Geng, R., Chen, J., Cheng, M., & Jia, J. (2025). TASO: Jailbreak LLMs via alternative template and suffix optimization. arXiv. https://arxiv.org/abs/2511.18581

Wu, T., Xue, Z., Liu, Y., Zhang, J., Hooi, B., & Ng, S.-K. (2025). Geneshift: Impact of different scenario shift on jailbreaking LLM. arXiv. https://arxiv.org/abs/2504.08104

Xie, Z., Song, X., & Luo, J. (2026). TrojanPraise: Jailbreak LLMs via benign fine-tuning. arXiv. https://arxiv.org/abs/2601.12460

Yoon, S., Jeung, W., Cho, Y., Jeon, D., & No, A. (2026). Few-shot truly benign DPO attack for jailbreaking LLMs. arXiv. https://arxiv.org/abs/2605.10998

Zhang, Y., Lu, S., & Li, J. (2026). Grammar-constrained decoding can jailbreak LLMs into generating malicious code. arXiv. https://arxiv.org/abs/2606.11817
