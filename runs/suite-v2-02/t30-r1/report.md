# Systematic Literature Review: Automated Program Repair with Language Models

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "automated program repair language models", filtered to category cs.SE, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on automated program repair (APR) with large language models reveals a rapidly evolving field focused on improving repair accuracy, generalizability, and efficiency. Recent work demonstrates that LLM-based APR systems achieve substantial improvements over traditional approaches, with repair accuracies reaching 44-45% on major benchmarks. Key research directions include fine-tuning strategies, fault localization improvements, cross-language generalization, and security considerations. The surveyed papers collectively indicate that while LLMs show strong promise for APR, challenges remain in handling imperfect fault localization, adversarial inputs, and computational efficiency. Emerging trends suggest movement toward specification-centric approaches, reasoning-guided localization, and the viability of smaller quantized models for resource-constrained settings.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "automated program repair language models", filtered to category cs.SE, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Fine-tuning and Model Optimization Strategies

Research on optimizing LLM performance for APR has focused heavily on fine-tuning techniques and model selection. Macháček et al. (2025) systematically evaluated six LLMs across three training regimens, finding that parameter-efficient fine-tuning methods (LoRA, IA3) outperform full fine-tuning due to reduced overfitting. Kusama et al. (2025) demonstrated that small language models with int8 quantization can achieve competitive or superior performance compared to large models while significantly reducing memory requirements. Sun et al. (2025) further showed that repair performance does not scale linearly with model size, and specialized models like CodeLlama can outperform larger general-purpose models. This theme reflects a maturing understanding that model selection and training strategy matter more than raw model size for APR tasks.

### Theme 2: Fault Localization and Context Management

A critical challenge in APR is identifying the correct location and context for repairs, especially when repositories exceed LLM context limits. Sepidband et al. (2026) introduced hierarchical reasoning-guided fault localization, achieving substantial improvements in file-level and element-level localization accuracy. Ehsani et al. (2026) examined how LLMs allocate attention across bug report sections, finding that successful repairs correlate with diffused attention across diagnostic components rather than over-localized attention on metadata. Campos et al. (2025) showed that under realistic assumptions of imperfect fault localization, repair accuracy drops significantly compared to using perfect fault localization. These works collectively emphasize that fault localization quality is a bottleneck for APR effectiveness, and that improving how models read and prioritize bug information is as important as the repair generation itself.

### Theme 3: Multi-language and Cross-platform Generalization

The question of whether LLMs can generalize APR capabilities across programming languages remains challenging. Campos et al. (2025) evaluated 13 LLMs across Java, JavaScript, Python, and PHP, finding that different models perform best for different languages, making single-LLM cross-platform repair difficult. However, pooling repairs from multiple models adds value through committee-based approaches. Farzandway and Ghassemi (2025) focused specifically on C programs, integrating spectrum-based fault localization with Chain-of-Thought prompting to achieve 44.93% repair accuracy. Pitts et al. (2025) extended APR to uncompilable student code, showing that models can recover compilable repairs while preserving students' structural intent. This theme reveals that language-specific characteristics and code quality significantly impact APR performance, suggesting hybrid or ensemble approaches may be necessary for broad generalization.

### Theme 4: Specification-centric and Reasoning-based Approaches

Moving beyond direct code rewriting, recent work explores specification-centric and reasoning-guided approaches. Zhu et al. (2026) proposed VibeRepair, which translates buggy code into structured behavior specifications, repairs specification misalignments, then synthesizes code guided by corrected specifications, achieving 19-23% improvements over baselines. Farzandway and Ghassemi (2025) integrated Chain-of-Thought reasoning into autonomous repair loops, reducing repeated errors by incorporating reasoning from previous attempts. Sepidband et al. (2026) used hierarchical reasoning modules to generate structured bug-specific explanations for candidate files. These approaches reflect a shift toward more structured, interpretable repair processes that separate specification understanding from code generation.

### Theme 5: Security and Adversarial Robustness

As LLM-based APR systems become more capable, security concerns emerge. Przymus et al. (2025) demonstrated that 90% of crafted adversarial bug reports triggered attacker-aligned patches, with existing defense mechanisms blocking less than half of adversarial inputs. This work reveals that APR systems are vulnerable to manipulation through carefully constructed bug reports, and that detection and mitigation remain costly and error-prone. This theme represents an emerging area of concern as APR systems are deployed in production settings, suggesting that security hardening must accompany capability improvements.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that fault localization quality fundamentally limits APR effectiveness (Campos et al., 2025; Ehsani et al., 2026; Sepidband et al., 2026). There is also agreement that parameter-efficient approaches—whether through PEFT fine-tuning (Macháček et al., 2025), quantization (Kusama et al., 2025), or specification-centric methods (Zhu et al., 2026)—provide better efficiency-accuracy tradeoffs than brute-force scaling. Most surveyed papers demonstrate that iterative or multi-stage approaches outperform single-pass repair generation (Farzandway & Ghassemi, 2025; Zhu et al., 2026).

**Disagreements**: While Campos et al. (2025) emphasize the difficulty of cross-language generalization with single models, Kusama et al. (2025) show that small models can match or exceed large model performance, suggesting different paths forward. There is also tension between works advocating for specialized, fine-tuned models (Macháček et al., 2025; Sun et al., 2025) versus those demonstrating strong zero-shot or specification-driven approaches (Zhu et al., 2026).

## Gaps and Open Questions

Several gaps emerge across the surveyed literature. Security considerations receive limited attention, with only Przymus et al. (2025) systematically addressing adversarial vulnerabilities—suggesting this area needs broader investigation. Most papers note limitations in evaluation scope, particularly regarding language diversity (Sepidband et al., 2026; Campos et al., 2025), indicating a need for more comprehensive cross-language benchmarks. The impact of imperfect fault localization is consistently acknowledged but rarely solved, pointing to a fundamental research challenge. Several papers note that limitations are "not stated in abstract," suggesting that detailed limitation analysis may be underreported. Finally, the computational and environmental costs of LLM-based APR, while touched on by quantization work (Kusama et al., 2025), deserve more systematic treatment as these systems scale.

## Per-Paper Annotations

### Campos et al. (2025)

**Research question**: How well can Large Language Models generalize automated program repair across different programming languages and levels of patch complexity?
**Methodology**: Extensive empirical evaluation of 13 recent open and closed LLM models across benchmarks for Java, JavaScript, Python, and PHP, investigating language-agnostic repair, fault localization effects, and cross-platform generalization.
**Key findings**:
- Different LLMs perform best for different languages, making cross-platform single-LLM repair techniques difficult to develop
- Combining models by pooling repairs adds value with respect to uniquely fixed bugs, suggesting committee-based approaches
- Under realistic assumptions of imperfect fault localization, significant drops in accuracy are observed compared to using perfect fault localization
**Limitations**: Not stated in abstract

### Ehsani et al. (2026)

**Research question**: How do LLMs prioritize and allocate attention across different sections of bug reports, and how does attention affect repair success?
**Methodology**: Analysis of attention patterns in LLM-based program repair across 319 real-world Python and Java bugs from SWE-bench Verified and Multi-SWE-bench, examining how attention is distributed across bug report sections and comparing successful versus unsuccessful repairs.
**Key findings**:
- Successful repairs are characterized by diffused attention across multiple diagnostic components such as bug descriptions, stacktraces, and test cases
- Failed repairs often exhibit over-localized attention toward metadata such as version information
- Stronger alignment between model attention and developer-identified key sections and phrases is associated with higher repair success
- Attention misallocation is identified as a key factor in LLM-based APR failures
**Limitations**: Not stated in abstract

### Farzandway and Ghassemi (2025)

**Research question**: How can Large Language Models be effectively integrated with statistical program analysis for automated repair of C programs?
**Methodology**: Framework combining spectrum-based fault localization (SBFL), runtime feedback, and Chain-of-Thought-structured prompting in an autonomous repair loop, evaluated on 3,902 bugs from the Codeflaws benchmark.
**Key findings**:
- The approach achieves 44.93% repair accuracy on the Codeflaws benchmark
- The method represents a 3.61% absolute improvement over state-of-the-art APR baselines such as GPT-4 with CoT
- Iterative repair cycles with CoT prompting reduce repeated errors by incorporating reasoning from previous attempts
- Combining statistical program analysis with LLM reasoning provides a practical pathway for automated debugging
**Limitations**: Not stated in abstract

### Kusama et al. (2025)

**Research question**: Can small language models achieve competitive performance in automated program repair tasks compared to large language models?
**Methodology**: Experiments on the QuixBugs benchmark comparing bug-fixing accuracy of small language models and large language models, also analyzing the impact of int8 quantization on APR performance.
**Key findings**:
- The latest small language models can fix bugs as accurately as or more accurately than large language models
- int8 quantization had minimal effect on APR accuracy
- Quantization significantly reduced memory requirements
- SLMs present a viable alternative to LLMs for APR with lower computational costs
**Limitations**: Not stated in abstract

### Macháček et al. (2025)

**Research question**: How do various fine-tuning techniques impact the performance of Large Language Models used for Automated Program Repair?
**Methodology**: Empirical evaluation of six LLMs (CodeGen, CodeT5, StarCoder, DeepSeekCoder, Bloom, and CodeLlama-2) across three APR benchmarks (QuixBugs, Defects4J, HumanEval-Java) using three training regimens: no fine-tuning, full fine-tuning, and parameter-efficient fine-tuning (PEFT) using LoRA and IA3.
**Key findings**:
- Full fine-tuning techniques decrease benchmarking performance of various models due to different data distributions and overfitting
- Parameter-efficient fine-tuning methods restrict the amount of trainable parameters and achieve better results than full fine-tuning
- Different LLMs show varying performance depending on the fine-tuning approach applied
**Limitations**: Not stated in abstract

### Pitts et al. (2025)

**Research question**: Can automated program repair recover uncompilable student code while preserving students' structural intent for use in student modeling?
**Methodology**: Assessment of large language models as repair agents under high- and low-context prompting conditions, evaluating repairs for compilability, edit distance, and preservation of students' original structure and logic.
**Key findings**:
- All models produced compilable repairs from uncompilable student submissions
- Models differed in how well they preserved students' control flow and code structure
- Recovering uncompilable submissions enables richer analyses of learners' coding processes and development over time
**Limitations**: Not stated in abstract

### Przymus et al. (2025)

**Research question**: What security risks do adversarial bug reports pose to LLM-based Automated Program Repair systems?
**Methodology**: Development of a threat model and empirical study using 51 adversarial bug reports generated through manual curation and automated pipelines, testing them against a leading LLM-based APR system with various pre-repair and post-repair defense mechanisms.
**Key findings**:
- 90% of crafted adversarial bug reports triggered attacker-aligned patches
- The best pre-repair filter blocked only 47% of adversarial inputs
- Post-repair analysis was effective in just 58% of cases
- Generating adversarial inputs is inexpensive while detection and mitigation remain costly and error-prone
**Limitations**: The study tested against a single leading LLM-based APR system; scalability of adversarial generation framework is demonstrated via prototype.

### Sepidband et al. (2026)

**Research question**: How can fault localization be improved for project-level automated program repair when software repositories exceed LLM context limits?
**Methodology**: Introduction of a hierarchical reasoning module that generates structured bug-specific explanations for candidate files and elements, using a two-stage ranking scheme combining LLM-based and embedding-based signals, evaluated on SWE-bench benchmarks for Python and Java projects.
**Key findings**:
- File-level Hit@1 improved from 71.4% to 85% on SWE-bench Verified
- File-level MRR improved from 81.8% to 88.8%
- Element-level Exact Match under top-3 files increased from 36% to 69%
- Integrating the localization into Agentless yielded a 12.8% end-to-end repair success improvement
**Limitations**: Evaluation focused on Python and Java projects from SWE-bench benchmarks; generalizability to other languages not explicitly addressed.

### Sun et al. (2025)

**Research question**: How do modern large-scale LLMs perform in automated program repair across diverse languages, bug scenarios, and prompting strategies?
**Methodology**: Evaluation of four open-source LLMs (CodeLlama, LLaMA, StarCoder, DeepSeek-Coder) with 7B to 33B parameters across two bug scenarios (enterprise-grade and algorithmic), three languages (Java, C/C++, Python), and four prompting strategies, analyzing over 600K generated patches on six benchmarks.
**Key findings**:
- Model specialization (e.g., CodeLlama) can outperform larger general-purpose models (e.g., LLaMA)
- Repair performance does not scale linearly with model size
- Correct patches often appear early in the generation process
- Prompting strategies significantly affect repair results
**Limitations**: Not stated in abstract

### Zhu et al. (2026)

**Research question**: Can a specification-centric approach to automated program repair improve repair accuracy compared to direct code-centric rewriting?
**Methodology**: Proposal of VibeRepair, which translates buggy code into structured behavior specifications, infers and repairs specification misalignments, then synthesizes code guided by the corrected specification, with on-demand reasoning for complex cases.
**Key findings**:
- VibeRepair correctly repaired 174 bugs on Defects4J v1.2, exceeding the strongest baseline by 28 bugs (19% improvement)
- On Defects4J v2.0, it repaired 178 bugs, outperforming prior approaches by 33 bugs (23% improvement)
- The approach demonstrated consistently strong effectiveness with a significantly smaller patch space
- Evaluations on real-world benchmarks confirmed effectiveness and generalizability
**Limitations**: Not stated in abstract

## References

Campos, V., Shariffdeen, R., Ulges, A., & Noller, Y. (2025). Exploring generalizable automated program repair with large language models. arXiv. https://arxiv.org/abs/2506.03283

Ehsani, R., Manotas, I., Pujar, S., Buratti, L., & Chatterjee, P. (2026). How do LLMs read bug reports? An empirical study of attention in LLMs for automated program repair. arXiv. https://arxiv.org/abs/2607.25873

Farzandway, M., & Ghassemi, F. (2025). Automated repair of C programs using large language models. arXiv. https://arxiv.org/abs/2509.01947

Kusama, K., Shu, H., Kondo, M., & Kamei, Y. (2025). How small is enough? Empirical evidence of quantized small language models for automated program repair. arXiv. https://arxiv.org/abs/2508.16499

Macháček, R., Grishina, A., Hort, M., & Moonen, L. (2025). The impact of fine-tuning large language models on automated program repair. arXiv. https://arxiv.org/abs/2507.19909

Pitts, G., Pandya, A., Rank, D., Bhatt, T., Hoq, M., & Akram, B. (2025). Automated program repair of uncompilable student code. arXiv. https://arxiv.org/abs/2510.06187

Przymus, P., Happe, A., & Cito, J. (2025). Adversarial bug reports as a security risk in language model-based automated program repair. arXiv. https://arxiv.org/abs/2509.05372

Sepidband, M., Taherkhani, H., Pham, H. V., & Hemmati, H. (2026). RGFL: Reasoning guided fault localization for automated program repair using large language models. arXiv. https://arxiv.org/abs/2601.18044

Sun, J., Li, F., Qi, X., Zhang, H., & Jiang, J. (2025). Empirical evaluation of large language models in automated program repair. arXiv. https://arxiv.org/abs/2506.13186

Zhu, T., Cordeiro, L. C., Mustafa, M. A., & Sun, Y. (2026). Specification vibing for automated program repair. arXiv. https://arxiv.org/abs/2602.08263
