# Systematic Literature Review: Jailbreak Attacks on Large Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search for "jailbreak attacks" in category cs.CR, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on jailbreak attacks against large language models (LLMs) has evolved rapidly over the past two years, with research focusing on three primary directions: systematic benchmarking and taxonomy development, novel attack vector discovery, and defense mechanism innovation. The surveyed papers collectively reveal that while jailbreak attacks remain a significant threat to LLM safety, the field is maturing toward standardized evaluation frameworks and more sophisticated defense strategies. A notable trend is the shift from studying attacks in isolation to comprehensive, large-scale evaluations that consider multiple attack types, defense mechanisms, and evaluation metrics. However, significant gaps remain in cross-lingual robustness, computational efficiency of defenses, and standardized benchmarking practices.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "jailbreak attacks" in category cs.CR, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search was restricted to the cs.CR (Security and Cryptography) category, potentially missing relevant papers in cs.AI or cs.CL categories.

## Themes

### Theme 1: Standardized Benchmarking and Taxonomy Development

A significant thread across the surveyed literature is the recognition that jailbreak research has been conducted in fragmented, isolated studies without standardized evaluation frameworks. Xu et al. (2024) introduced JailTrickBench to evaluate eight key factors of jailbreak attacks from both target-level and attack-level perspectives, conducting approximately 354 experiments across six defense methods. Their work highlights that previous studies primarily overlooked diverse attack factors, concentrating mainly on LLM vulnerabilities without exploring defense-enhanced models. Similarly, Chu et al. (2024) developed JailbreakRadar, collecting 17 representative jailbreak attacks and establishing a comprehensive taxonomy evaluated across nine aligned LLMs on 160 forbidden questions from 16 violation categories. The most recent systematization by Xu et al. (2026) introduced Security Cube, a unified multi-dimensional framework addressing the inadequacy of existing evaluation practices that rely on narrow metrics like attack success rate. Lu et al. (2024) employed directed acyclic graphs to systematically map dependency relationships across all attack surfaces, proposing AutoAttack, AutoDefense, and AutoEvaluation frameworks. This convergence toward standardized benchmarking reflects the field's maturation and recognition that meaningful progress requires reproducible, comprehensive evaluation methodologies.

### Theme 2: Novel Attack Vector Discovery

Beyond benchmarking, several papers focus on discovering and exploiting previously overlooked attack vectors. Zhou et al. (2024) introduced Virtual Context, which leverages special tokens—previously ignored in LLM security research—to enhance jailbreak attack success rates by approximately 40% across various LLMs. Their approach requires minimal background knowledge about the target model, making it particularly effective in black-box settings. Doumbouya et al. (2024) developed h4rm3l, a domain-specific language that formally expresses jailbreak attacks as compositions of parameterized string transformation primitives, enabling program synthesis methods to explore large compositional attack spaces. Their synthesizer generated 2,656 novel attacks targeting six state-of-the-art LLMs, with success rates exceeding 90%—significantly outperforming existing attacks in the literature. Li et al. (2024) investigated multilingual jailbreak attacks, where malicious questions are translated into various languages to evade safety filters, revealing that translation-based attacks can effectively bypass multilingual safety mechanisms. These works collectively demonstrate that attack surface expansion through novel vectors—special tokens, compositional synthesis, and cross-language exploitation—represents a critical threat vector requiring immediate attention in red-teaming efforts.

### Theme 3: Defense Mechanism Innovation

In response to evolving attack sophistication, the literature shows substantial innovation in defense mechanisms operating at different stages of the LLM inference pipeline. Xu et al. (2024) proposed SafeDecoding, a safety-aware decoding strategy that manipulates token probabilities during generation by identifying and amplifying safety disclaimers while attenuating harmful token sequences. Their experiments across five LLMs showed significant reduction in attack success rates without compromising response helpfulness, outperforming six existing defense methods. Zeng et al. (2024) developed AutoDefense, a multi-agent framework where different LLM agents collaborate to filter harmful responses, demonstrating that smaller open-source models can effectively defend larger victim models—reducing attack success rate on GPT-3.5 from 55.74% to 7.95% using LLaMA-2-13b with a three-agent system. Qian et al. (2024) introduced Hidden State Filtering (HSF), a pre-inference defense mechanism that leverages clustering patterns in LLM hidden state representations to proactively identify and reject adversarial inputs before inference begins, achieving defense with negligible computational overhead. These defense approaches reflect a diversification strategy: rather than relying on a single defense mechanism, the literature suggests layered defenses operating at different stages (pre-inference, during decoding, post-generation) provide more robust protection against diverse attack vectors.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several key points. First, all papers acknowledge that existing jailbreak research has been conducted in isolation without standardized benchmarks, creating reproducibility and comparability challenges (Xu et al., 2024; Chu et al., 2024; Xu et al., 2026). Second, there is consensus that defense-enhanced LLMs remain vulnerable to sophisticated attacks, necessitating continuous innovation in both attack and defense methodologies. Third, multiple papers converge on the finding that computational efficiency is a critical constraint for practical defense deployment—methods requiring extensive GPU hours or inference overhead are impractical for real-world applications (Xu et al., 2024; Qian et al., 2024). Finally, there is agreement that black-box attack scenarios, where attackers have minimal knowledge of the target model, represent the most realistic and concerning threat model (Zhou et al., 2024; Doumbouya et al., 2024).

**Disagreements**: While the literature shows more convergence than disagreement, subtle tensions exist in evaluation philosophy. Xu et al. (2026) argue that narrow metrics like attack success rate fail to capture the multidimensional nature of LLM security, advocating for comprehensive multi-dimensional frameworks. However, other papers continue to primarily report attack success rate as the primary metric, suggesting the field has not yet fully adopted the proposed comprehensive evaluation frameworks. Additionally, there is implicit disagreement about the optimal defense strategy: Xu et al. (2024) advocate for decoding-time interventions, Qian et al. (2024) argue for pre-inference filtering, and Zeng et al. (2024) propose post-generation multi-agent filtering—each approach has different computational trade-offs and effectiveness profiles that remain incompletely resolved.

## Gaps and Open Questions

The collective literature reveals several critical gaps requiring future research attention. First, computational resource requirements pose a significant barrier: Xu et al. (2024) noted their comprehensive evaluation required approximately 55,000 GPU hours on A800-80G, making replication and extension difficult for most research groups. Second, several papers acknowledge that their defenses require access to model internals—token probabilities (Xu et al., 2024), hidden states (Qian et al., 2024), or multi-agent querying (Zeng et al., 2024)—which may not be available in deployed API-based LLM services, creating an deployment gap between research and practice. Third, while Li et al. (2024) addressed multilingual attacks, their mitigation strategy requires fine-tuning resources and may not generalize to all languages, leaving non-English languages underprotected. Fourth, the h4rm3l framework (Doumbouya et al., 2024) requires an automated harmful behavior classifier strongly aligned with human judgment, but the generalizability of such classifiers across cultural and linguistic contexts remains unaddressed. Finally, as Xu et al. (2026) note, the Security Cube framework requires community adoption for standardized evaluation, but no mechanism for such adoption is proposed, leaving the field fragmented despite recognition of the problem.

## Per-Paper Annotations

### Chu et al. (2024)

**Research question**: What patterns and insights emerge when systematically comparing jailbreak attacks across multiple aligned LLMs and defense mechanisms?

**Methodology**: Collected 17 representative jailbreak attacks, established a novel taxonomy, and conducted comprehensive measurement and ablation studies across nine aligned LLMs on 160 forbidden questions from 16 violation categories, plus testing under eight advanced defenses.

**Key findings**:
- Heuristic-based attacks achieve high success rates but are easily mitigated by defenses, resulting in low practicality
- Previous research studied jailbreak attacks in isolation with unaligned settings or limited method comparisons
- The proposed taxonomy enables systematic comparison and understanding of attack characteristics
- Comprehensive evaluation across multiple LLMs reveals important patterns for future research
- The work serves as an effective benchmark tool to help the community avoid incremental work

**Limitations**: Limited to 160 forbidden questions which may not cover all possible attack surfaces; focuses on aligned LLMs which may not represent all deployment scenarios in practice.

### Doumbouya et al. (2024)

**Research question**: Can a formal composable domain-specific language for jailbreak attacks enable exploration of larger attack spaces through program synthesis methods?

**Methodology**: Developed h4rm3l, a human-readable DSL expressing jailbreak attacks as compositions of parameterized string transformation primitives, with a synthesizer using bandit algorithms and a red-teaming toolkit; synthesized 2,656 novel attacks targeting 6 SOTA LLMs.

**Key findings**:
- Synthesized attacks achieve success rates exceeding 90% on state-of-the-art LLMs
- h4rm3l-generated attacks are more diverse and successful than existing jailbreak attacks in literature
- The composable DSL enables efficient exploration of large compositional attack spaces
- The automated harmful behavior classifier is strongly aligned with human judgment
- Program synthesis methods can effectively generate novel jailbreak attacks for black-box LLMs

**Limitations**: Requires an automated harmful behavior classifier that must be strongly aligned with human judgment; the DSL may not capture all possible attack vectors outside its compositional primitives; benchmarking against a subset of synthesized attacks may not represent full attack space.

### Li et al. (2024)

**Research question**: How do multilingual jailbreak attacks evade safety filters, and what mitigation strategies are effective against them?

**Methodology**: Developed a semantic-preserving algorithm to create a multilingual jailbreak dataset, conducted exhaustive evaluation on open-source and commercial LLMs including GPT-4 and LLaMa, performed interpretability analysis, and implemented a fine-tuning mitigation method.

**Key findings**:
- Multilingual jailbreak attacks can effectively evade safety filters by translating malicious questions into various languages
- Comprehensive empirical study reveals vulnerabilities across both open-source and commercial LLMs
- Interpretability analysis uncovered distinct patterns in how multilingual jailbreak attacks operate
- Fine-tuning mitigation strategy significantly enhances model defense, reducing attack success rate by 96.2%
- First comprehensive empirical study specifically addressing the multilingual jailbreak threat

**Limitations**: Focuses on translation-based multilingual attacks; the fine-tuning mitigation requires additional training resources and may not generalize to all languages or attack types.

### Lu et al. (2024)

**Research question**: How can we systematically analyze and optimize jailbreak attacks and defenses through dependency relationships across all attack surfaces?

**Methodology**: Employed directed acyclic graphs (DAGs) to position and analyze dependency relationships in jailbreak techniques, proposing three frameworks: AutoAttack (genetic algorithm and adversarial-generation attacks), AutoDefense (mixture-of-defenders approach), and AutoEvaluation (novel evaluation method).

**Key findings**:
- Current jailbreak strategies focus on local optimization within specific algorithmic frameworks, resulting in ineffective optimization and limited scalability
- Dependency relationships can be generalized and mapped across all possible attack surfaces using DAGs
- AutoAttack investigates dependencies in two optimization strategies and proposes an ensemble jailbreak attack to exploit these dependencies
- AutoDefense offers a mixture-of-defenders approach leveraging dependencies in pre-generative and post-generative defense strategies
- AutoEvaluation introduces a novel evaluation method that distinguishes attack and defense effectiveness more comprehensively

**Limitations**: The dependency-based approach may be complex to implement and generalize; the abstract was truncated in available sources, limiting full understanding of AutoEvaluation's contributions and empirical results.

### Qian et al. (2024)

**Research question**: How can we design a pre-inference defense method that resists diverse jailbreak prompts without requiring costly LLM inference?

**Methodology**: Proposed Hidden State Filter (HSF), a lossless architectural defense mechanism that leverages clustering patterns in LLM hidden state representations to proactively identify and reject adversarial inputs before inference, activated through an additional plugin module framing defense as classification.

**Key findings**:
- Jailbreak attacks, safe queries, and harmful queries exhibit distinct clustering patterns within LLM hidden state representation space
- HSF significantly enhances resilience against six cutting-edge jailbreak attacks across three different LLMs
- Significantly reduces jailbreak attack success rate while minimally impacting responses to benign user queries
- Achieves defense with negligible inference overhead compared to output control and detection methods
- Outperforms existing defense baselines that focus on prompt rewriting or output detection

**Limitations**: Requires access to model hidden states and an additional plugin module; evaluation was conducted on specific benchmark datasets which may not capture all attack variations.

### Xu et al. (2024) [JailTrickBench]

**Research question**: How do various attack settings and key factors impact the effectiveness of jailbreak attacks on LLMs, particularly defense-enhanced models?

**Methodology**: Introduced JailTrickBench to evaluate eight key factors of jailbreak attacks from target-level and attack-level perspectives, conducting seven representative attacks on six defense methods across two datasets with approximately 354 experiments.

**Key findings**:
- Different attack settings significantly impact jailbreak effectiveness on LLMs
- Defense-enhanced LLMs require standardized evaluation frameworks for proper assessment
- Eight key factors were identified from both target-level and attack-level perspectives
- Previous studies primarily overlooked diverse key factors, focusing mainly on LLM vulnerabilities
- Standardized benchmarking is necessary to properly evaluate attacks on defense-enhanced LLMs

**Limitations**: The study requires substantial computational resources (55,000 GPU hours on A800-80G), making replication difficult; primarily focuses on evaluation framework rather than proposing novel attack or defense methods.

### Xu et al. (2024) [SafeDecoding]

**Research question**: Can safety-aware decoding strategies defend against jailbreak attacks by manipulating token probabilities without compromising response helpfulness?

**Methodology**: Introduced SafeDecoding, a safety-aware decoding strategy that identifies safety disclaimers among top probability tokens and amplifies their probabilities while attenuating token sequences aligned with jailbreak objectives; evaluated on five LLMs with six state-of-the-art attacks across four benchmark datasets.

**Key findings**:
- Safety disclaimers appear among top tokens even when harmful content tokens have higher probabilities
- SafeDecoding significantly reduces attack success rates and harmfulness of jailbreak attacks
- The defense maintains helpfulness of responses to benign user queries
- SafeDecoding outperforms six existing defense methods in experimental evaluations
- Token probability manipulation during decoding can effectively mitigate jailbreak attacks

**Limitations**: Requires access to token probabilities during the decoding process, which may not be available in all deployment scenarios; effectiveness against all types of jailbreak attacks, especially adaptive ones, needs further investigation.

### Xu et al. (2026)

**Research question**: How can we comprehensively evaluate jailbreak attack and defense techniques beyond narrow metrics like attack success rate?

**Methodology**: Presented a systematic taxonomy of jailbreak attacks and defenses, introduced Security Cube as a unified multi-dimensional evaluation framework, and conducted benchmark studies on 13 representative attacks and 5 defenses with detailed comparison tables.

**Key findings**:
- Existing evaluation practices are inadequate, relying on narrow metrics that fail to capture the multidimensional nature of LLM security
- Security Cube provides a unified framework for comprehensive evaluation encompassing attacks, defenses, automated judges, and vulnerabilities
- Benchmark studies establish a clear view of the current landscape across 13 attacks and 5 defenses
- Detailed comparison tables highlight key insights and open challenges across the literature
- Analysis distills critical findings, identifies unresolved problems, and outlines promising research directions for enhancing LLM robustness

**Limitations**: As a systematization of knowledge paper, it does not propose novel attack or defense techniques; the Security Cube framework requires community adoption for standardized evaluation.

### Zeng et al. (2024)

**Research question**: How can we defend large language models against jailbreak attacks that bypass moral alignment pre-training?

**Methodology**: Proposed AutoDefense, a multi-agent defense framework that assigns different roles to LLM agents to collaboratively filter harmful responses using a response-filtering mechanism, enabling small open-source models to defend larger victim models.

**Key findings**:
- AutoDefense is robust against different jailbreak attack prompts and can defend different victim models
- Small open-source LMs can serve as agents to defend larger models against jailbreak attacks
- Reduced attack success rate on GPT-3.5 from 55.74% to 7.95% using LLaMA-2-13b with a 3-agent system
- Maintains performance on normal user requests while filtering harmful content
- Task division among agents enhances instruction-following and enables integration of other defense components as tools

**Limitations**: The abstract does not explicitly acknowledge limitations; the multi-agent approach may introduce computational overhead from querying multiple LLM agents for each response.

### Zhou et al. (2024)

**Research question**: Can special tokens previously overlooked in LLM security be leveraged to improve jailbreak attack success rates with minimal resource requirements?

**Methodology**: Introduced Virtual Context that leverages special tokens to enhance existing jailbreak methods, requiring minimal background knowledge about the target model; comprehensively evaluated across various LLMs with four widely used jailbreak methods.

**Key findings**:
- Virtual Context improves success rates of existing jailbreak methods by approximately 40% across various LLMs
- The approach requires minimal background knowledge about the target model, enhancing black-box effectiveness
- Special tokens represent an overlooked threat vector in LLM security that should be included in red-teaming
- Applying Virtual Context to original malicious behaviors still achieves notable jailbreak effects
- The method enhances attack effectiveness without additional computational overhead

**Limitations**: Effectiveness depends on the availability and behavior of special tokens in target models; primarily evaluated by enhancing existing jailbreak methods rather than demonstrating entirely novel attack vectors.

## References

Chu, J., Liu, Y., Yang, Z., Shen, X., Backes, M., & Zhang, Y. (2024). JailbreakRadar: Comprehensive assessment of jailbreak attacks against LLMs. arXiv. https://arxiv.org/abs/2402.05668

Doumbouya, M. K. B., Nandi, A., Poesia, G., Ghilardi, D., Goldie, A., Bianchi, F., Jurafsky, D., & Manning, C. D. (2024). h4rm3l: A language for composable jailbreak attack synthesis. arXiv. https://arxiv.org/abs/2408.04811

Li, J., Liu, Y., Liu, C., Shi, L., Ren, X., Zheng, Y., Liu, Y., & Xue, Y. (2024). A cross-language investigation into jailbreak attacks in large language models. arXiv. https://arxiv.org/abs/2401.16765

Lu, L., Yan, H., Yuan, Z., Shi, J., Wei, W., Chen, P.-Y., & Zhou, P. (2024). AutoJailbreak: Exploring jailbreak attacks and defenses through a dependency lens. arXiv. https://arxiv.org/abs/2406.03805

Qian, C., Zhang, H., Sha, L., & Zheng, Z. (2024). HSF: Defending against jailbreak attacks with hidden state filtering. arXiv. https://arxiv.org/abs/2409.03788

Xu, F., Hu, H., He, C., Hang, S., Hu, H., Liu, X., Zhao, Y., Zhou, Z., Zhu, B. B., Sun, S.-F., Gu, D., & Wang, S. (2026). SoK: Robustness in large language models against jailbreak attacks. arXiv. https://arxiv.org/abs/2605.05058

Xu, Z., Jiang, F., Niu, L., Jia, J., Lin, B. Y., & Poovendran, R. (2024). SafeDecoding: Defending against jailbreak attacks via safety-aware decoding. arXiv. https://arxiv.org/abs/2402.08983

Xu, Z., Liu, F., & Liu, H. (2024). Bag of tricks: Benchmarking of jailbreak attacks on LLMs. arXiv. https://arxiv.org/abs/2406.09324

Zeng, Y., Wu, Y., Zhang, X., Wang, H., & Wu, Q. (2024). AutoDefense: Multi-agent LLM defense against jailbreak attacks. arXiv. https://arxiv.org/abs/2403.04783

Zhou, Y., Lu, L., Sun, H., Zhou, P., & Sun, L. (2024). Virtual context: Enhancing jailbreak attacks with special token injection. arXiv. https://arxiv.org/abs/2406.19845
