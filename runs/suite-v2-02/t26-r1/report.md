# Systematic Literature Review: Jailbreak Attacks on Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: "jailbreak attacks large language models", cs.CR, last 2 years (2024-10-25 to 2026-10-25)
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on jailbreak attacks against large language models (LLMs) published between late 2024 and mid-2026. The surveyed literature reveals a rapidly evolving adversarial landscape where attackers are developing increasingly sophisticated methods to bypass safety alignment in LLMs, while defenders are responding with novel detection and robustness techniques. Key trends include the shift from single-turn to multi-turn adaptive attacks, expansion into multimodal domains (vision and audio), and the emergence of evidence-based evaluation frameworks. The field demonstrates growing maturity with systematic taxonomies, standardized benchmarks, and latent-space analysis for both attack and defense mechanisms.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "jailbreak attacks large language models", filtered to category cs.CR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Adaptive and Multi-Turn Attack Strategies

Recent jailbreak research has moved beyond single-prompt attacks toward adaptive, iterative strategies that refine queries based on model responses. Narula et al. (2025) introduced HarmNet, a framework that systematically explores the adversarial space through hierarchical semantic networks and feedback-driven simulation, achieving 99.4% attack success rate on Mistral-7B. Similarly, Cheng et al. (2024) developed PBI-Attack, which uses bidirectional cross-modal interaction optimization to iteratively enhance malicious features in vision-language models. This trend reflects a recognition that static jailbreak prompts are increasingly ineffective against aligned models, necessitating dynamic, context-aware attack strategies that adapt in real-time.

### Theme 2: Multimodal Jailbreak Expansion

The attack surface has expanded beyond text-only models to encompass multimodal systems. Chen et al. (2025) demonstrated that traditional text jailbreaks cannot be directly ported to large audio-language models (LALMs) via text-to-speech, prompting their development of AudioJailbreak with suffixal jailbreak audios that operate asynchronously from user prompts. Yin et al. (2025) addressed multimodal large language models (MLLMs), showing that adversarial perturbations can be generated through contrastive embedding attacks across multiple modalities. Cheng et al. (2024) also targeted large vision-language models (LVLMs) with prior-guided bimodal attacks. This expansion reflects the growing deployment of multimodal AI systems and their unique vulnerabilities arising from cross-modal interactions.

### Theme 3: Evaluation Framework Standardization

A maturing field requires rigorous evaluation standards, and recent work has focused on developing evidence-based assessment frameworks. Huang et al. (2026) proposed JailMeter, an Information Bottleneck-inspired framework that achieves 97.27% accuracy in evaluating jailbreak attacks by filtering noise while preserving malicious intent signals. Xu et al. (2026) introduced the Security Cube, a multi-dimensional evaluation framework that moves beyond narrow metrics like attack success rate to capture the full landscape of LLM security. These frameworks address a critical gap in the literature: inconsistent and inadequate evaluation practices that hinder comparison across studies and obscure true progress.

### Theme 4: Latent-Space Analysis and Detection

Understanding jailbreak attacks through internal model representations has emerged as a promising research direction. Kadali and Papalexakis (2026) conducted systematic layer-wise analysis across multiple architectures (GPT-J, LLaMA, Mistral, Mamba), identifying consistent latent-space patterns associated with harmful inputs and proposing a tensor-based detection framework that blocks 78% of jailbreak attempts. Yi et al. (2025) developed LATPC, which dynamically identifies safety-critical latent dimensions through contrastive analysis of harmful and benign inputs, enabling targeted defense with minimal over-defense. This latent-space perspective offers advantages over surface-level text analysis, providing model-internal signals that may generalize across attack types.

### Theme 5: Evolutionary and Optimization-Based Attacks

Biological inspiration and combinatorial optimization have informed novel attack methodologies. Yu et al. (2024) proposed LLM-Virus, treating jailbreak as an evolutionary process where LLMs serve as heuristic operators within an evolutionary algorithm framework, achieving high transferability and transparency compared to opaque optimization techniques. Zhou et al. (2025) formulated CCJA as a combinatorial optimization problem balancing attack success with semantic coherence in the embedding space. These approaches address limitations of gradient-based methods in black-box settings while maintaining attack effectiveness and interpretability.

### Theme 6: Defense Mechanisms and Robustness

Parallel to attack development, significant research has focused on improving model robustness. Yin et al. (2025) introduced SafeMLLM, an adversarial training framework that alternates between generating perturbations and updating model parameters to neutralize attack effects. Yi et al. (2025) proposed embedding-level calibration mechanisms that minimize over-defense behaviors. Xu et al. (2026) conducted benchmark studies on 13 attacks and 5 defenses, establishing a comprehensive view of the defense landscape. These defensive approaches share a common goal: maintaining model utility on benign inputs while effectively blocking malicious queries.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that traditional single-turn, text-only jailbreak methods are insufficient against modern aligned models. Narula et al. (2025), Cheng et al. (2024), and Zhou et al. (2025) all demonstrate that adaptive, iterative approaches significantly outperform static baselines. There is also broad agreement that evaluation practices need standardization, with Huang et al. (2026) and Xu et al. (2026) independently proposing comprehensive frameworks. The surveyed papers consistently report that multimodal systems introduce unique vulnerabilities not present in text-only models.

**Disagreements**: While most papers focus on either attack or defense, there is implicit tension between the arms race dynamics: attack methods continuously evolve to bypass defenses, while defensive techniques must balance safety with utility. The literature does not yet resolve whether latent-space interventions (Kadali & Papalexakis, 2026; Yi et al., 2025) or adversarial training approaches (Yin et al., 2025) offer superior long-term robustness. Additionally, the transferability of attacks across model architectures remains incompletely understood, with Yu et al. (2024) claiming high transferability for evolutionary approaches while others focus on model-specific optimizations.

## Gaps and Open Questions

The surveyed literature reveals several notable gaps. None of the papers explicitly stated limitations in their abstracts, suggesting a need for more transparent discussion of methodological constraints. Several open questions emerge:

1. **Long-term effectiveness**: Most evaluations measure immediate attack success rates, but the durability of attacks against continuously updated models remains unclear.
2. **Real-world deployment**: Laboratory benchmarks may not capture the complexity of production systems with additional safeguards and monitoring.
3. **Cross-model generalization**: While some papers claim transferability, systematic studies of how attacks generalize across architectures, sizes, and training data are limited.
4. **Human evaluation**: Automated judges (including LLM-based evaluators) may not align with human judgments of harmfulness, creating evaluation blind spots.
5. **Ethical considerations**: The dual-use nature of jailbreak research raises questions about responsible disclosure and publication that the literature does not adequately address.

## Per-Paper Annotations

### Chen et al. (2025)

**Research question**: How can jailbreak attacks be effectively executed against end-to-end large audio-language models, particularly in scenarios where adversaries cannot fully manipulate user prompts?
**Methodology**: The authors first evaluate existing text jailbreak attacks ported to LALMs via TTS, then propose AUDIOJAILBREAK featuring asynchrony, universality, stealthiness, and over-the-air robustness through suffixal jailbreak audios and intent concealment strategies.
**Key findings**:
- Advanced text jailbreak attacks cannot be easily ported to end-to-end LALMs via text-to-speech techniques
- AUDIOJAILBREAK achieves asynchrony by crafting suffixal jailbreak audios that don't need to align with user prompts in the time axis
- The attack demonstrates universality with a single jailbreak perturbation effective for different prompts
- AUDIOJAILBREAK can jailbreak OpenAI's GPT-4o-Audio and bypass Meta's Llama-Guard-3 safeguard in the weak adversary scenario
- The jailbreak audios remain effective when played over the air by incorporating reverberation into perturbation generation
**Limitations**: Not stated in abstract

### Cheng et al. (2024)

**Research question**: How can jailbreak attacks on Large Vision Language Models be effective in black-box scenarios without requiring model gradients?
**Methodology**: The authors propose PBI-Attack, which extracts malicious features from a harmful corpus using an alternative LVLM, embeds these features into a benign image as prior information, and enhances them through bidirectional cross-modal interaction optimization using greedy search to maximize toxicity. Toxicity levels are quantified using a trained evaluation model.
**Key findings**:
- PBI-Attack achieves an average attack success rate of 92.5% across three open-source LVLMs
- PBI-Attack achieves around 67.3% attack success rate on three closed-source LVLMs
- The method outperforms previous state-of-the-art jailbreak methods
- Bidirectional cross-modal interaction optimization effectively enhances malicious features
**Limitations**: Not stated in abstract

### Huang et al. (2026)

**Research question**: How can jailbreak attack evaluation against large language models be made more reliable and consistent?
**Methodology**: The authors propose JailMeter, an evidence-based evaluation framework inspired by Information Bottleneck theory that applies dual-feedback optimization to filter jailbreak noise while preserving content relevant to the original malicious question. They evaluate it on JailMeter-Eva, a benchmark with 330 human-labeled jailbreak instances, and distill it into a small language model for large-scale evaluation.
**Key findings**:
- JailMeter achieves an accuracy of 97.27% on the JailMeter-Eva benchmark
- JailMeter substantially outperforms existing evaluation methods
- The distilled JailMeter_SLM maintains comparable reliability with significantly reduced computational costs
- The framework validates attacks only when responses capture malicious intent and deliver complete answers
**Limitations**: Not stated in abstract

### Kadali and Papalexakis (2026)

**Research question**: How do internal representations in large language models differ between jailbreak and benign prompts, and can these differences be used for jailbreak detection?
**Methodology**: The authors conduct a systematic layer-wise analysis across multiple open-source models (GPT-J, LLaMA, Mistral, Mamba) to identify latent-space patterns associated with harmful inputs, then propose a tensor-based latent representation framework for lightweight jailbreak detection without fine-tuning.
**Key findings**:
- Consistent latent-space patterns associated with harmful inputs were identified across multiple models including GPT-J, LLaMA, Mistral, and Mamba
- The proposed tensor-based framework enables lightweight jailbreak detection without requiring model fine-tuning or auxiliary LLM-based detectors
- Selectively bypassing high-susceptibility layers blocks 78% of jailbreak attempts while preserving benign behavior on 94% of benign prompts
- The intervention operates entirely at inference time with minimal overhead
**Limitations**: Not stated in abstract

### Narula et al. (2025)

**Research question**: How can multi-turn jailbreak attacks on Large Language Models be made more adaptive and effective?
**Methodology**: The authors introduce HarmNet, a modular framework with three components: ThoughtNet (a hierarchical semantic network), a feedback-driven Simulator for iterative query refinement, and a Network Traverser for real-time adaptive attack execution. Experiments were conducted across closed-source and open-source LLMs to measure attack success rates.
**Key findings**:
- HarmNet systematically explores and refines the adversarial space to uncover stealthy, high-success attack paths
- HarmNet outperforms state-of-the-art methods in attack success rates
- On Mistral-7B, HarmNet achieves a 99.4% attack success rate, 13.9% higher than the best baseline
**Limitations**: Not stated in abstract

### Xu et al. (2026)

**Research question**: What is the current landscape of jailbreak attacks and defenses in large language models, and how can they be comprehensively evaluated beyond narrow metrics like attack success rate?
**Methodology**: The authors present a systematic taxonomy of jailbreak attacks and defenses, introduce the Security Cube framework for multi-dimensional evaluation, and conduct benchmark studies on 13 representative attacks and 5 defenses.
**Key findings**:
- Existing evaluation practices are inadequate, often relying on narrow metrics like attack success rate that fail to capture the multidimensional nature of LLM security
- The Security Cube provides a unified, multi-dimensional framework for comprehensive evaluation of jailbreak techniques
- Benchmark studies on 13 attacks and 5 defenses establish a clear view of the current landscape encompassing jailbreak attacks, defenses, automated judges, and LLM vulnerabilities
- The analysis identifies unresolved problems and outlines promising research directions for enhancing LLM robustness
**Limitations**: Not stated in abstract

### Yi et al. (2025)

**Research question**: How can latent-space adversarial training with post-aware calibration defend against jailbreak attacks while minimizing over-defense behavior in large language models?
**Methodology**: The authors introduce LATPC, a framework that dynamically identifies safety-critical latent dimensions by contrasting harmful and benign inputs, enabling targeted refusal feature removal attacks, and employs an embedding-level calibration mechanism during inference to minimize over-defense.
**Key findings**:
- LATPC dynamically identifies safety-critical latent dimensions by contrasting harmful and benign inputs
- The framework achieves a superior balance between safety and utility compared to existing defense frameworks across five types of disguise-based jailbreak attacks
- The embedding-level calibration mechanism minimizes over-defense behaviors with negligible computational overhead
- Leveraging safety-critical dimensions is effective for developing robust defense methods against jailbreak attacks
**Limitations**: Not stated in abstract

### Yin et al. (2025)

**Research question**: How can adversarial training improve the robustness of multimodal large language models against jailbreak attacks without relying on external inference steps or safety alignment training?
**Methodology**: The authors introduce SafeMLLM, an adversarial training framework that alternates between generating adversarial perturbations through a contrastive embedding attack (CoE-Attack) and updating model parameters to neutralize perturbation effects while preserving utility on benign inputs.
**Key findings**:
- SafeMLLM generates adversarial perturbations through a newly proposed contrastive embedding attack (CoE-Attack) that optimizes token embeddings under a contrastive objective
- The framework effectively defends against diverse attacks across six MLLMs and six jailbreak methods spanning multiple modalities
- SafeMLLM maintains robust performance and utilities on benign inputs while neutralizing perturbation effects
**Limitations**: Not stated in abstract

### Yu et al. (2024)

**Research question**: How can jailbreak attacks on LLMs be made more transparent, transferable, and computationally efficient compared to existing opaque optimization techniques?
**Methodology**: The authors propose LLM-Virus, inspired by biological virus evolution and infection processes, which treats jailbreak attacks as both an evolutionary and transfer learning problem. The method uses LLMs as heuristic evolutionary operators within an evolutionary algorithm framework to ensure high attack efficiency, transferability, and low time cost.
**Key findings**:
- LLM-Virus achieves competitive or superior performance compared to existing attack methods on multiple safety benchmarks
- The evolutionary algorithm approach provides better transparency than opaque optimization techniques
- The method demonstrates high transferability across different models
- Using LLMs as heuristic evolutionary operators ensures low computational cost
**Limitations**: Not stated in abstract

### Zhou et al. (2025)

**Research question**: How can jailbreak attacks on open-source LLMs leverage access to model parameters and gradient information while maintaining semantic coherence?
**Methodology**: The authors define jailbreak attacks as an optimization problem within the embedding space of masked language models and use combinatorial optimization to balance attack success rate with semantic coherence. They also integrate semantically coherent jailbreak prompts into black-box methodologies targeting closed-source commercial LLMs.
**Key findings**:
- CCJA maintains semantic consistency while surpassing state-of-the-art baselines in attack effectiveness
- Integrating CCJA-generated prompts into black-box methodologies enhances their success rates against closed-source commercial LLMs
- Open-source LLMs pose a security threat to commercial counterparts through this approach
**Limitations**: Not stated in abstract

## References

Chen, G., Song, F., Zhao, Z., Jia, X., Liu, Y., Qiao, Y., Zhang, W., Tu, W., Yang, Y., & Du, B. (2025). AudioJailbreak: Jailbreak attacks against end-to-end large audio-language models. arXiv. https://arxiv.org/abs/2505.14103

Cheng, R., Ding, Y., Cao, S., Duan, R., Jia, X., Yuan, S., Qin, S., Wang, Z., & Jia, X. (2024). PBI-Attack: Prior-guided bimodal interactive black-box jailbreak attack for toxicity maximization. arXiv. https://arxiv.org/abs/2412.05892

Huang, Q., Zhang, J., Wu, J., Li, Y., Zhang, W., Rong, Y., Yao, J., Zhang, S., & Jia, X. (2026). JailMeter: An evidence-based evaluation framework for jailbreak attacks on large language models. arXiv. https://arxiv.org/abs/2607.19424

Kadali, S. D. S. S., & Papalexakis, E. E. (2026). Jailbreaking leaves a trace: Understanding and detecting jailbreak attacks from internal representations of large language models. arXiv. https://arxiv.org/abs/2602.11495

Narula, S., Rafiei Asl, J., Ghasemigol, M., Blanco, E., & Takabi, D. (2025). HarmNet: A framework for adaptive multi-turn jailbreak attacks on large language models. arXiv. https://arxiv.org/abs/2510.18728

Xu, F., Hu, H., He, C., Hang, S., Hu, H., Liu, X., Zhao, Y., Zhou, Z., Zhu, B. B., Sun, S.-F., Gu, D., & Wang, S. (2026). SoK: Robustness in large language models against jailbreak attacks. arXiv. https://arxiv.org/abs/2605.05058

Yi, X., Li, Y., Shi, D., Wang, L., Wang, X., & He, L. (2025). Latent-space adversarial training with post-aware calibration for defending large language models against jailbreak attacks. arXiv. https://arxiv.org/abs/2501.10639

Yin, Z., Cao, Y., Liu, H., Wang, T., Chen, J., & Ma, F. (2025). Towards robust multimodal large language models against jailbreak attacks. arXiv. https://arxiv.org/abs/2502.00653

Yu, M., Fang, J., Zhou, Y., Fan, X., Wang, K., Pan, S., & Wen, Q. (2024). LLM-Virus: Evolutionary jailbreak attack on large language models. arXiv. https://arxiv.org/abs/2501.00055

Zhou, G., Qiu, P., Fan, M., Chen, C., Chu, M., Zhang, X., & Zhou, J. (2025). CCJA: Context-coherent jailbreak attack for aligned large language models. arXiv. https://arxiv.org/abs/2502.11379
