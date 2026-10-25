# Systematic Literature Review: Jailbreak Attacks on Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "jailbreak attacks", filtered to category cs.CR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on jailbreak attacks against large language models has rapidly evolved from simple prompt engineering techniques to sophisticated multi-modal and reasoning-based attack vectors. Recent research reveals that current LLM safety mechanisms share fundamental vulnerabilities that can be exploited through transferable attacks, with success rates ranging from 60-85% across different attack methodologies. The field has identified critical gaps in evaluation practices, with most defenses proving vulnerable to adaptive attacks and lacking standardized benchmarking frameworks. Emerging research directions include multi-turn conversational attacks, visual injection attacks on multi-modal models, and Chain-of-Thought exploitation, all of which expose significant limitations in current defense mechanisms that remain largely reactive rather than proactive.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "jailbreak attacks", filtered to category cs.CR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Taxonomy and Systematic Classification of Jailbreak Attacks

The surveyed literature demonstrates a strong emphasis on creating comprehensive taxonomies to categorize jailbreak attacks. Multiple survey papers establish systematic frameworks for understanding attack surfaces and methodologies. Liu et al. (2025) categorize attacks into input-level, representation-level, and multi-turn strategies, while Zhao et al. (2025) organize attacks by attack surfaces (input manipulation, model manipulation, and output manipulation) and methodologies (prompt-based, optimization-based, and learning-based approaches). Xu et al. (2026) advance this further with their Security Cube framework, which provides multi-dimensional evaluation beyond narrow metrics like attack success rate. This taxonomic work reflects the field's maturation from isolated attack demonstrations to systematic understanding of the attack landscape, enabling more structured defense development and evaluation.

### Theme 2: Transferability and Universal Vulnerabilities

A critical finding across multiple studies is that jailbreak attacks exhibit significant transferability across different LLM architectures. Chen et al. (2025) demonstrate that transferable attacks achieve success rates exceeding 60% across 8 different LLM families, including both open-source and closed-source models. This transferability stems from common vulnerabilities in alignment training rather than architecture-specific features, revealing that current LLM safety mechanisms share fundamental weaknesses. The benchmarking study by Zhang et al. (2025) supports this finding, showing that larger models do not necessarily exhibit better jailbreak resistance, with some 70B parameter models showing higher vulnerability than 7B models. These findings challenge the assumption that scale alone provides robustness and highlight the need for more diverse safety training approaches that address universal vulnerability patterns.

### Theme 3: Emerging Attack Vectors Beyond Text

Recent research has expanded jailbreak attack methodologies beyond traditional text-based prompts to exploit multi-modal and reasoning capabilities. He et al. (2025) introduce visual injection attacks on multi-modal LLMs, achieving success rates exceeding 70% by injecting malicious visual patterns while maintaining semantic coherence. Shan et al. (2025) exploit Chain-of-Thought reasoning mechanisms, achieving up to 85% success rate by using step-by-step reasoning to gradually normalize harmful content. Li et al. (2025) demonstrate that multi-turn conversational attacks achieve 72% success rate compared to 38% for single-turn attacks, exploiting context accumulation and safety boundary erosion. These emerging vectors expose critical security gaps in systems designed primarily for text-only, single-turn interaction scenarios, revealing that safety mechanisms have not kept pace with capability expansion.

### Theme 4: Defense Mechanisms and Their Limitations

The literature reveals a concerning pattern: most current defenses are reactive and insufficient against sophisticated adaptive attacks. Liu et al. (2025) and Zhao et al. (2025) both note that existing defenses including input sanitization, model fine-tuning, and output filtering remain vulnerable to adaptive attacks specifically designed to circumvent known defense mechanisms. However, promising defense approaches are emerging. Zhang et al. (2025) propose Defensive Distillation, which transfers knowledge from robust teacher models and reduces attack success rates by 45% while maintaining benign task performance. Zhang et al. (2024) introduce automated detection using semantic entropy, achieving 89% detection accuracy with false positive rates below 5%, generalizing well to unseen attack types. Despite these advances, the field lacks proactive defense mechanisms and standardized evaluation frameworks, leaving most deployed systems vulnerable to novel attack strategies.

### Theme 5: Benchmarking and Evaluation Challenges

A recurring theme across the literature is the critical need for standardized benchmarking and evaluation practices. Zhang et al. (2025) present JailBench, a comprehensive framework with 500+ adversarial prompts covering 12 attack categories, revealing significant variations in robustness across model families. Xu et al. (2026) critique existing evaluation practices as inadequate, relying on narrow metrics that fail to capture the multidimensional nature of LLM security. Their Security Cube framework enables comprehensive comparison across attacks, defenses, automated judges, and vulnerabilities. The benchmarking work reveals that current evaluation practices make it difficult to compare defense effectiveness across studies, hindering progress in the field. Standardized protocols and multi-dimensional metrics are essential for advancing LLM safety research and enabling reproducible evaluation of new techniques.

## Convergences and Disagreements

**Convergences**: The surveyed papers demonstrate strong agreement on several critical points. All studies acknowledge that current defense mechanisms are largely reactive and insufficient against adaptive attacks (Liu et al., 2025; Zhao et al., 2025; Chen et al., 2025). Multiple papers identify the lack of standardized evaluation benchmarks as a fundamental gap hindering progress (Xu et al., 2026; Zhang et al., 2025; Liu et al., 2025). There is consensus that emerging attack vectors including multi-turn conversations, multi-modal inputs, and reasoning exploitation represent critical security gaps requiring urgent attention (Li et al., 2025; He et al., 2025; Shan et al., 2025). The literature also converges on the finding that model scale does not guarantee robustness, with safety fine-tuning quality and alignment strategy being more critical factors than parameter count (Zhang et al., 2025; Chen et al., 2025).

**Disagreements**: The surveyed literature shows limited direct disagreement, as most papers focus on different aspects of the jailbreak landscape rather than competing claims. However, there is implicit tension between papers emphasizing universal vulnerabilities (Chen et al., 2025) versus those highlighting architecture-specific factors (He et al., 2025; Shan et al., 2025). While Chen et al. (2025) argue that transferable attacks exploit fundamental weaknesses shared across all LLMs, He et al. (2025) and Shan et al. (2025) identify vulnerabilities specific to multi-modal architectures and CoT-enabled models respectively. This suggests that while universal vulnerabilities exist, architecture-specific factors also play important roles in determining attack success, pointing to a nuanced reality where both universal and specific vulnerabilities coexist.

## Gaps and Open Questions

The collective literature identifies several critical gaps requiring future research. First, there is a fundamental lack of proactive defense mechanisms, with current approaches remaining reactive to known attacks rather than anticipating novel strategies (Zhao et al., 2025; Liu et al., 2025). Second, theoretical understanding of LLM vulnerabilities remains limited, preventing development of principled defense mechanisms grounded in formal security analysis (Zhao et al., 2025). Third, representation-level vulnerabilities are poorly understood, with most attacks and defenses operating at the input-output level without examining internal model representations (Liu et al., 2025). Fourth, multi-turn conversation safety remains an unresolved challenge, as existing single-turn defenses fail to account for cumulative context effects (Li et al., 2025). Fifth, multi-modal security is critically underexplored, with visual injection attacks revealing fundamental gaps in MLLM safety systems (He et al., 2025). Sixth, reasoning-based attack vectors including CoT exploitation require comprehensive countermeasures beyond initial proposals (Shan et al., 2025). Finally, privacy-preserving defense mechanisms and computational overhead transparency remain open problems, particularly for real-time detection systems that must balance accuracy with latency constraints (Zhang et al., 2024; Zhang et al., 2025).

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: How can jailbreak attacks be made transferable across different LLM architectures without requiring model-specific optimization?
**Methodology**: Proposes a novel attack framework that identifies universal vulnerability patterns in LLM safety mechanisms through adversarial prompt generation and cross-model validation, focusing on fundamental weaknesses in alignment training rather than architecture-specific features.
**Key findings**:
- Transferable attacks achieve success rates exceeding 60% across 8 different LLM families
- Attacks are effective on both open-source and closed-source models
- Current LLM safety mechanisms share common vulnerabilities exploitable through universal attacks
- Attack transferability depends on prompt structure, semantic content, and safety training data overlap
**Limitations**: The study focuses primarily on attack methodologies without extensively exploring countermeasures; the effectiveness may vary as safety training approaches evolve.

### He et al. (2025)

**Research question**: How vulnerable are multi-modal large language models to jailbreak attacks through adversarial visual content injection?
**Methodology**: Novel attack framework that injects malicious visual patterns into input images while maintaining semantic coherence, tested across multiple MLLM architectures to evaluate attack success rates and analyze visual encoding component vulnerabilities.
**Key findings**:
- Visual injection attacks achieve high success rates exceeding 70% on benchmark tasks across multiple MLLM architectures
- Different visual encoding components show varying levels of vulnerability to adversarial attacks
- Critical security gaps exist in current MLLM safety systems for multi-modal inputs
- This represents the first systematic investigation of visual-based jailbreak attacks on MLLMs
- Robust multi-modal defense mechanisms are urgently needed
**Limitations**: The study focuses specifically on visual injection attacks; broader multi-modal attack vectors beyond visual injection may exist and require investigation.

### Li et al. (2025)

**Research question**: How vulnerable are conversational LLMs to multi-turn jailbreak attacks that leverage conversational context to gradually bypass safety filters?
**Methodology**: Presents a systematic study proposing a novel attack strategy that exploits conversational memory and context accumulation to progressively normalize harmful content across multiple dialogue turns, with detailed analysis of conversation trajectories.
**Key findings**:
- Multi-turn attacks achieve 72% success rate, significantly higher than single-turn baseline attacks at 38%
- Identifies key vulnerability patterns: context dilution, safety boundary erosion, and conversational momentum exploitation
- Existing single-turn defense mechanisms are largely ineffective against multi-turn attacks
- Reveals critical need for context-aware defense mechanisms monitoring conversation-level safety rather than individual turn safety
**Limitations**: Focuses primarily on attack methodology rather than comprehensive defense solutions; may not cover all conversational attack vectors and interaction patterns.

### Liu et al. (2025)

**Research question**: What is the current landscape of jailbreak attacks and defenses on LLMs, and what key challenges remain unresolved?
**Methodology**: Comprehensive survey categorizing attacks into input-level, representation-level, and multi-turn strategies while examining corresponding defense mechanisms including input sanitization, model fine-tuning, and output filtering.
**Key findings**:
- Attacks can be categorized into input-level, representation-level, and multi-turn strategies with distinct methodologies
- Most current defenses are vulnerable to adaptive attacks
- Significant gaps exist including lack of standardized evaluation benchmarks
- Limited understanding of representation-level vulnerabilities remains a critical challenge
- Robust multi-turn conversation safety mechanisms are needed but currently lacking
**Limitations**: Current defenses remain largely reactive and insufficient against sophisticated adaptive attacks; the field lacks standardized evaluation frameworks and has limited theoretical understanding of LLM vulnerabilities.

### Shan et al. (2025)

**Research question**: Can Chain-of-Thought reasoning mechanisms be exploited to bypass safety filters in LLMs?
**Methodology**: Introduction of CoT-Jailbreak attack that leverages step-by-step reasoning processes to gradually guide LLMs toward generating harmful content while maintaining apparent policy compliance, tested extensively across multiple LLM architectures.
**Key findings**:
- CoT-Jailbreak attacks achieve up to 85% success rate on safety-aligned models, significantly higher than traditional prompt-based methods
- CoT reasoning creates unique vulnerabilities that existing defense mechanisms fail to address
- The incremental nature of CoT reasoning allows attackers to gradually normalize harmful content, making detection increasingly difficult
- CoT-aware safety filters and reasoning trajectory monitoring are proposed as initial countermeasures
- Reasoning-based attack vectors represent critical security gaps in CoT-enabled LLMs
**Limitations**: Proposed countermeasures are initial and preliminary; the full scope of reasoning-based attack vectors and comprehensive defenses require further research.

### Xu et al. (2026)

**Research question**: How can jailbreak attacks and defenses on LLMs be comprehensively evaluated beyond narrow metrics like attack success rate?
**Methodology**: The authors present a systematic taxonomy of jailbreak attacks and defenses and introduce Security Cube, a unified multi-dimensional framework for comprehensive evaluation. They conduct benchmark studies on 13 representative attacks and 5 defenses using this framework.
**Key findings**:
- Existing evaluation practices are inadequate, relying on narrow metrics that fail to capture the multidimensional nature of LLM security
- Security Cube provides a unified framework enabling comprehensive comparison of attacks, defenses, automated judges, and LLM vulnerabilities
- Benchmark studies establish a clear view of the current landscape across 13 attacks and 5 defenses
- Critical unresolved problems and promising research directions for enhancing LLM robustness were identified
**Limitations**: The abstract does not explicitly acknowledge limitations, though it implies current evaluation practices and metrics are fundamentally inadequate for capturing LLM security complexity.

### Zhang, L. et al. (2024)

**Research question**: How can we detect jailbreak attacks in real-time with better generalization to novel attack strategies beyond pattern matching or supervised classifiers?
**Methodology**: Proposes a detection approach based on semantic entropy that measures uncertainty in model responses by computing entropy across multiple sampled responses to identify anomalous patterns indicative of jailbreak attacks.
**Key findings**:
- Achieves 89% detection accuracy with false positive rates below 5%
- Generalizes well to unseen attack types, outperforming traditional pattern-based detectors by 23% in cross-attack evaluation
- Imposes minimal computational overhead suitable for real-time deployment in production systems
- Jailbreak attacks induce distinctive uncertainty patterns in model responses reliably captured through semantic entropy measurement
**Limitations**: Requires multiple response samples which may increase latency; effectiveness may vary across different model architectures and sampling configurations.

### Zhang, Z. et al. (2025)

**Research question**: How can we establish standardized benchmarking frameworks for consistently evaluating jailbreak attack and defense effectiveness across different LLMs?
**Methodology**: Presents JailBench, a comprehensive benchmarking framework with 500+ adversarial prompts covering 12 attack categories, automated evaluation metrics, and standardized testing protocols, used to evaluate 15 state-of-the-art LLMs.
**Key findings**:
- Significant variations in robustness exist across model families and sizes
- Larger models do not necessarily exhibit better jailbreak resistance; some 70B parameter models show higher vulnerability than 7B models
- Critical factors affecting robustness include safety fine-tuning quality, training data composition, and alignment strategy
- Enables reproducible evaluation of jailbreak attacks and defenses with standardized tools
**Limitations**: Benchmark coverage of 500+ prompts across 12 categories may not capture all emerging attack types; results are dependent on the specific prompt set and evaluation protocols used.

### Zhang, H. et al. (2025)

**Research question**: How can we defend against jailbreak attacks with better generalization and lower computational overhead than existing defense mechanisms?
**Methodology**: Proposes Defensive Distillation that transfers knowledge from a robust teacher model to enhance student model jailbreak resistance through adversarial training with distilled safety knowledge, enabling robustness inheritance without extensive retraining.
**Key findings**:
- Reduces attack success rates by an average of 45% compared to baseline defenses
- Maintains model performance on benign tasks while improving safety
- Provides robust protection against adaptive attacks targeting known defense mechanisms
- Knowledge distillation creates more generalized safety boundaries harder to circumvent than traditional fine-tuning
**Limitations**: Requires access to a robust teacher model; defense effectiveness may depend on the quality and robustness of the teacher model used for distillation.

### Zhao et al. (2025)

**Research question**: What is the state of jailbreak attacks and defenses in LLMs, and what critical research gaps need to be addressed?
**Methodology**: Systematic taxonomy categorizing attacks by attack surfaces (input, model, and output manipulation) and methodologies (prompt-based, optimization-based, and learning-based), followed by review of defense mechanisms including input filtering, model hardening, and output monitoring.
**Key findings**:
- Jailbreak attacks can be systematically categorized by attack surface and methodology
- Significant progress has been made in understanding jailbreak attack mechanisms
- Current defenses remain largely reactive and insufficient against sophisticated adaptive attacks
- Proactive defense mechanisms are needed but currently lacking
- Standardized evaluation frameworks and theoretical understanding of vulnerabilities are critical gaps
**Limitations**: Current defenses are reactive rather than proactive; there is lack of standardized evaluation frameworks and insufficient theoretical understanding of LLM vulnerabilities.

## References

Chen, Y., Zhou, T., Zhang, X., Liu, Z., Zhao, J., Li, Y., Sun, M., Sun, Z., Hua, J., & Luo, X. (2025). Transferable jailbreak attacks on large language models. arXiv. https://arxiv.org/abs/2504.08018

He, Z., Dong, Y., Ji, X., Yu, N., Ying, Z., Dong, H., Zhang, X., & He, C. (2025). Jailbreak attack on multi-modal large language models via visual injection. arXiv. https://arxiv.org/abs/2506.15377

Li, R., Xie, X., Wang, J., Ma, L., Zhang, X., Liu, Y., Feng, C., & Li, X. (2025). Multi-turn jailbreak attacks on conversational large language models. arXiv. https://arxiv.org/abs/2501.15432

Liu, Y., Li, X., Lu, J., Sengupta, B., Mubarak, S., Khaled, A., Zehni, N., Zahran, M., Ba, Z., & Ji, X. (2025). Jailbreak attacks and defenses on large language models: A survey. arXiv. https://arxiv.org/abs/2509.14364

Shan, M., Zhang, X., Zhang, Y., Xu, Z., Chang, H., Sun, Z., Hua, J., Luo, X., & Chen, K. (2025). Chain-of-thought jailbreak attacks on large language models. arXiv. https://arxiv.org/abs/2505.14316

Xu, F., Hu, H., He, C., Hang, S., Hu, H., Liu, X., Zhao, Y., Zhou, Z., Zhu, B. B., Sun, S.-F., Gu, D., & Wang, S. (2026). SoK: Robustness in large language models against jailbreak attacks. arXiv. https://arxiv.org/abs/2605.05058

Zhang, H., Wang, W., Chen, J., Cao, Y., Guan, X., & Liu, T. (2025). Defensive distillation against jailbreak attacks on large language models. arXiv. https://arxiv.org/abs/2503.12456

Zhang, L., Liu, Z., Liu, Y., Li, S., Liu, Z., & Sun, M. (2024). Automated detection of jailbreak attacks using semantic entropy. arXiv. https://arxiv.org/abs/2412.18765

Zhang, Z., Li, Y., Xu, Y., Wang, J., Lyu, Z., Tao, S., Liu, J., Lu, X., Sun, Y., & Yu, W. (2025). Benchmarking jailbreak attacks on large language models: A comprehensive study. arXiv. https://arxiv.org/abs/2502.09876

Zhao, W., Peng, Z., Shen, Y., Zhang, J., Wang, R., Li, S., Liu, Z., & Sun, M. (2025). A survey on jailbreak attacks and defenses in large language models. arXiv. https://arxiv.org/abs/2508.19368
