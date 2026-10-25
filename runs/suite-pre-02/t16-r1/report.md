# Systematic Literature Review: Reinforcement Learning from Human Feedback

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "RLHF", filtered to category cs.LG, published between 2024-01-01 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on Reinforcement Learning from Human Feedback (RLHF) published between 2024 and 2025. The surveyed literature reveals a rapidly evolving field focused on three primary challenges: improving computational efficiency, scaling human feedback collection, and addressing fundamental limitations of current RLHF approaches. Recent work demonstrates significant progress in making RLHF more accessible through lightweight reward models, efficient annotation frameworks, and novel signal sources such as human gaze data. However, researchers increasingly recognize boundary conditions where RLHF fails, prompting development of diagnostic tools and alternative approaches. The field is maturing from proving RLHF's effectiveness toward systematic understanding of when, why, and how it works.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "RLHF", filtered to category cs.LG, published between 2024-01-01 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Cost Reduction in RLHF Pipelines

A dominant theme across the surveyed literature is the pursuit of more efficient RLHF implementations that reduce computational and annotation costs. Agnihotri and Pandey (2025) demonstrate that lightweight LLM judges with minimal parameter updates can outperform massive reward models, achieving 96.2% accuracy on RewardBench with only a 7B model and rank-16 LoRA adapter affecting just 0.8% of parameters. Similarly, Green et al. (2024) show that carefully designed low-resource RLHF can achieve 85% of high-resource performance at only 20% of the cost through efficient annotation strategies and lightweight reward models. Galliamov et al. (2025) introduce an orthogonal efficiency dimension by leveraging human gaze signals to accelerate convergence during policy optimization, reducing computational costs while maintaining performance. Chen et al. (2025) address annotation costs through hierarchical frameworks combining expert and crowd-sourced feedback, achieving 40% cost reduction compared to expert-only approaches. Collectively, these works suggest that RLHF is transitioning from a resource-intensive research tool toward a practically deployable technology.

### Theme 2: Scaling and Democratization of RLHF

Closely related to efficiency is the challenge of scaling RLHF to meet growing demand while maintaining quality and accessibility. Chen et al. (2025) present hierarchical annotation frameworks that strategically combine diverse annotator pools with quality control mechanisms, demonstrating that strategically sampled feedback from diverse annotators can match or exceed homogeneous expert data performance. Green et al. (2024) focus explicitly on democratization, providing open-source toolkits with pre-trained reward models and training scripts optimized for consumer GPUs, enabling small organizations to implement RLHF without specialized hardware. Dong et al. (2024) contribute detailed recipes for online iterative RLHF with fully open-source datasets, addressing the gap between resource-rich industry labs and open-source communities. This democratization trend reflects growing recognition that RLHF's benefits should extend beyond well-funded organizations to broader research and development communities.

### Theme 3: Understanding and Addressing RLHF Failure Modes

A mature and critical theme emerging in 2024-2025 literature is systematic investigation of RLHF's limitations and failure conditions. Martinez et al. (2025) identify five distinct failure patterns: reward overoptimization, specification gaming, preference inconsistency, domain mismatch, and annotator fatigue, proposing diagnostic tools for each. Liu et al. (2024) focus specifically on bias propagation in preference learning, identifying annotator demographics, task framing effects, and temporal inconsistencies as major bias sources, with debiasing techniques reducing bias-induced performance degradation by 35%. Li et al. (2024) provide comprehensive survey coverage of challenges including reward hacking, distributional shift, and computational costs. This critical self-examination represents field maturation, moving beyond demonstrating RLHF's success toward understanding its boundary conditions and appropriate application domains.

### Theme 4: Multi-Objective and Domain-Specific RLHF

Recent work increasingly recognizes that real-world RLHF applications require balancing multiple competing objectives and adapting to domain-specific requirements. Zhang et al. (2025) introduce multi-objective RLHF frameworks that explicitly model trade-offs between competing values such as helpfulness, harmlessness, and honesty, generating Pareto-optimal policy families that allow users to select alignments matching their preferences. Wilson et al. (2024) address code generation's unique challenges, combining automated test execution for objective correctness with human preferences for readability and maintainability, achieving 23% improvement in functionally correct code over SFT baselines. These works demonstrate that one-size-fits-all RLHF is giving way to specialized approaches tailored to specific application domains and value systems.

### Theme 5: Online and Iterative RLHF Approaches

The literature shows clear movement from offline to online iterative RLHF approaches that continuously refine policies through ongoing feedback. Dong et al. (2024) provide comprehensive workflows for online iterative RLHF, demonstrating substantial performance improvements over offline counterparts on benchmarks including AlpacaEval-2, Arena-Hard, and MT-Bench. Agnihotri and Pandey (2025) enable online RLHF through plug-and-play LLM judges that eliminate offline preference-tuning phases while achieving state-of-the-art results. This shift toward online methods reflects recognition that static preference datasets cannot capture evolving requirements or correct initial misalignments, necessitating continuous adaptation mechanisms.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several points. Most works acknowledge that computational cost and annotation burden are primary barriers to RLHF adoption (Agnihotri & Pandey, 2025; Chen et al., 2025; Green et al., 2024; Galliamov et al., 2025). There is consensus that online iterative approaches outperform offline methods (Dong et al., 2024; Agnihotri & Pandey, 2025). Multiple papers converge on the finding that diverse, strategically-sampled feedback can match or exceed homogeneous expert data quality (Chen et al., 2025; Zhang et al., 2025). The literature also agrees that RLHF has identifiable failure modes requiring diagnostic validation before deployment (Martinez et al., 2025; Liu et al., 2024; Li et al., 2024).

**Disagreements**: Tensions exist regarding the extent to which efficiency gains compromise performance. Green et al. (2024) accept 85% of high-resource performance as sufficient for democratization, while Agnihotri and Pandey (2025) claim their efficient approach achieves state-of-the-art performance exceeding even 70B baselines, suggesting efficiency and performance need not trade off. Another tension concerns the role of human signals: Galliamov et al. (2025) advocate gaze data as valuable supplementary signal, while other works assume text-based preferences alone suffice. Multi-objective approaches (Zhang et al., 2025) implicitly challenge single-objective RLHF assumptions, suggesting fundamental disagreement about whether alignment should produce single optimal policies or policy families representing value trade-offs.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, while multiple papers acknowledge that proxy preference models cannot fully capture human preferences (Dong et al., 2024; Agnihotri & Pandey, 2025), no work provides systematic comparison of proxy versus actual human feedback quality across diverse tasks. Second, bias mitigation techniques (Liu et al., 2024) require validation across cultural and demographic contexts beyond tested benchmarks. Third, multi-objective RLHF (Zhang et al., 2025) introduces user decision burden in policy selection without guidance on how users should navigate trade-offs. Fourth, code generation RLHF (Wilson et al., 2024) depends on test case availability, leaving open how to handle domains lacking objective evaluation criteria. Fifth, gaze-informed approaches (Galliamov et al., 2025) require specialized infrastructure, creating accessibility questions. Finally, Martinez et al.'s (2025) failure mode diagnostics require empirical validation across diverse deployment scenarios to establish reliability and coverage.

## Per-Paper Annotations

### Agnihotri and Pandey (2025)

**Research question**: Can a lightweight, configurable LLM judge replace expensive large-scale reward models in RLHF pipelines while maintaining or improving performance?

**Methodology**: The authors augment a frozen 7B instruction-tuned LLM with a one-line JSON rubric and rank-16 LoRA adapter (affecting only 0.8% of parameters) to serve as a complete substitute for heavyweight reward models, then apply online PPO for policy optimization.

**Key findings**:
- The plug-and-play judge achieves 96.2% accuracy on RewardBench, outperforming specialized reward networks ranging from 27B to 70B parameters
- A 7B actor using this approach achieves 92% exact match accuracy on GSM-8K, substantially outperforming the top 70B DPO baseline (61.8%)
- Six in-context demonstrations deliver the majority of zero-to-few-shot improvements (+2 percentage points)
- The LoRA adapter effectively addresses remaining performance gaps, particularly in safety and adversarial Chat-Hard segments
- LoRA judge attains approximately 9/10 similarity to human explanations compared to 5/10 for zero-shot judges, demonstrating superior interpretability

**Limitations**: The approach requires careful rubric design and LoRA fine-tuning; performance may depend on the quality of the HH-Rationales dataset and may not generalize equally well across all domains without adaptation.

### Chen, Williams, and Park (2025)

**Research question**: How can human feedback collection be scaled to meet growing demand while maintaining annotation quality and reducing costs?

**Methodology**: The authors introduce a hierarchical annotation framework that strategically combines expert and crowd-sourced feedback with quality control mechanisms and annotator training protocols to achieve cost-effective scaling.

**Key findings**:
- The hierarchical annotation framework achieves 40% cost reduction compared to traditional expert-only approaches
- Strategically sampled feedback from diverse annotators can match or exceed the performance of models trained on homogeneous expert data
- Quality control mechanisms and annotator training protocols are effective in maintaining annotation quality at scale
- Diverse annotator pools can provide valuable feedback variety that improves model robustness
- Practical guidelines are provided for implementing scalable RLHF pipelines in production environments

**Limitations**: The approach requires careful annotator selection and training; crowd-sourced feedback quality may vary and requires robust quality control; the framework may need adaptation for specialized domains requiring expert-level knowledge.

### Dong et al. (2024)

**Research question**: How can open-source communities implement online iterative RLHF that outperforms offline RLHF while remaining reproducible with limited resources?

**Methodology**: The authors construct preference models using diverse open-source datasets to approximate human feedback, then apply online iterative RLHF with theoretical insights and detailed practical implementation guidelines.

**Key findings**:
- Online iterative RLHF significantly outperforms offline RLHF by a large margin on LLM chatbot benchmarks
- Supervised fine-tuning (SFT) combined with iterative RLHF achieves state-of-the-art performance using only fully open-source datasets
- The trained model performs impressively on AlpacaEval-2, Arena-Hard, MT-Bench, HumanEval, and TruthfulQA benchmarks
- Proxy preference models can effectively approximate human feedback when online human feedback is infeasible
- All models, curated datasets, and comprehensive code guidebooks are made publicly available for reproducibility

**Limitations**: Online human feedback collection remains infeasible for open-source communities with limited resources, necessitating the use of proxy preference models that may not fully capture human preferences.

### Galliamov, Titov, and Pershin (2025)

**Research question**: Can human gaze signals be leveraged to enhance RLHF efficiency and reduce computational costs during policy optimization?

**Methodology**: The authors explore two approaches: (1) gaze-aware reward models that incorporate gaze patterns into reward computation, and (2) gaze-based distribution of sparse rewards at the token level to guide policy optimization more precisely.

**Key findings**:
- Gaze-informed RLHF achieves faster convergence compared to traditional RLHF approaches
- The method maintains or slightly improves overall performance while reducing computational costs
- Human gaze provides a valuable and previously underused signal for policy optimization
- Token-level reward distribution informed by gaze patterns enables more efficient learning
- The approach points to a promising direction for improving RLHF efficiency without sacrificing quality

**Limitations**: The approach requires gaze-tracking infrastructure which may not be available in all settings; the experiments may not fully represent diverse use cases, and the slight performance improvement suggests gaze signals alone may not be sufficient for all alignment challenges.

### Green, Johnson, and White (2024)

**Research question**: How can RLHF be made accessible to smaller organizations and researchers with limited annotation budgets and computational resources?

**Methodology**: Presents practical methods for conducting RLHF with limited resources including efficient annotation strategies, lightweight reward models, and sample-efficient policy optimization algorithms. Developed an open-source toolkit with pre-trained reward models, annotation interfaces, and training scripts optimized for consumer GPUs.

**Key findings**:
- Carefully designed low-resource RLHF can achieve 85% of the performance of high-resource approaches at just 20% of the cost
- Open-source toolkit provides turnkey solutions for small teams including pre-trained reward models and annotation interfaces
- Training scripts optimized for consumer GPUs make RLHF accessible without specialized hardware
- Efficient annotation strategies and lightweight reward models can significantly reduce resource requirements

**Limitations**: The approach achieves only 85% of high-resource performance, leaving a 15% gap; methods may not scale to very large models or complex tasks requiring extensive annotation, and pre-trained reward models may not generalize to all domains.

### Li, Du, Liu, and Fu (2024)

**Research question**: What are the theoretical foundations, algorithmic developments, practical applications, and key challenges of RLHF as a technique for aligning large language models with human values?

**Methodology**: The authors conduct a comprehensive survey systematically categorizing existing RLHF methods into reward modeling, policy optimization, and evaluation frameworks, while analyzing challenges and emerging alternatives.

**Key findings**:
- RLHF methods can be systematically categorized into reward modeling, policy optimization, and evaluation frameworks
- Key challenges in scaling RLHF include reward hacking, distributional shift, and high computational costs
- Direct Preference Optimization (DPO) and other emerging alternatives offer different trade-offs compared to traditional RLHF
- The survey reveals important research directions for improving efficiency, stability, and interpretability of RLHF systems
- Understanding the relationship between different RLHF components is crucial for developing more effective alignment techniques

**Limitations**: As a survey paper, it does not present new experimental results or novel algorithms; the analysis is limited to existing literature which may not capture the most recent developments or provide empirical validation of the identified research directions.

### Liu, Kim, and Thompson (2024)

**Research question**: What are the sources of bias in human preference data and how do they impact policy learning in RLHF systems?

**Methodology**: Investigates systematic biases in human preference data and proposes debiasing techniques including adversarial filtering, multi-annotator consensus mechanisms, and temporal smoothing of preference labels. Experiments conducted across multiple RLHF benchmarks to validate the approach.

**Key findings**:
- Three major sources of bias identified: annotator demographics, task framing effects, and temporal inconsistencies in human judgments
- Proposed debiasing techniques reduce bias-induced performance degradation by 35%
- The approach maintains annotation efficiency while significantly reducing bias
- Bias propagation in preference learning has measurable impact on policy learning outcomes

**Limitations**: The abstract does not explicitly acknowledge limitations; results may be limited to specific RLHF benchmarks tested and may not generalize to all preference learning scenarios or capture all possible bias sources.

### Martinez, Taylor, and Lee (2025)

**Research question**: Under what boundary conditions does human feedback fail to improve model performance or even degrade it in RLHF systems?

**Methodology**: Systematically investigates failure modes of RLHF including cases where human preferences are noisy, contradictory, or misaligned with task objectives. Proposes diagnostic tools and mitigation strategies for each identified failure mode.

**Key findings**:
- Five distinct failure patterns identified: reward overoptimization, specification gaming, preference inconsistency, domain mismatch, and annotator fatigue
- Human preferences can be noisy, contradictory, or misaligned with task objectives in certain contexts
- RLHF should be applied selectively with careful validation of feedback quality and alignment before deployment
- Diagnostic tools can identify when RLHF is likely to fail or degrade performance

**Limitations**: The abstract does not explicitly acknowledge limitations; the five failure patterns identified may not be exhaustive, and proposed mitigation strategies may not be equally effective across all failure modes or domains.

### Wilson, Chen, and Brown (2024)

**Research question**: How can RLHF be effectively applied to code generation tasks given the structured nature of programming languages and objective correctness criteria?

**Methodology**: Presents a novel RLHF framework for code generation incorporating both functional correctness rewards and stylistic preferences. Uses automated test execution for objective feedback combined with human preferences for code readability and maintainability.

**Key findings**:
- RLHF-trained code models produce functionally correct code 23% more often than SFT baselines
- Generated code is rated by developers as more readable and maintainable
- Combining automated test execution with human preferences effectively balances objective and subjective quality criteria
- Code generation presents unique RLHF challenges due to structured language and objective correctness requirements

**Limitations**: The abstract does not explicitly acknowledge limitations; approach may depend on availability of test cases for automated evaluation, and human preference collection for code style may not scale efficiently.

### Zhang, Anderson, and Garcia (2025)

**Research question**: How can RLHF systems balance multiple, potentially conflicting human values such as helpfulness, harmlessness, and honesty?

**Methodology**: Introduces a multi-objective reinforcement learning framework that explicitly models trade-offs between competing values. Proposes a Pareto-optimal policy search algorithm that generates a family of policies representing different value trade-offs.

**Key findings**:
- Multi-objective RLHF achieves better value alignment across diverse user populations compared to single-objective approaches
- Pareto-optimal policy search generates multiple policies allowing users to select based on their specific preferences
- Particular improvements observed in cross-cultural settings where value priorities differ
- Explicit modeling of value trade-offs enables more transparent and controllable alignment

**Limitations**: The abstract does not explicitly acknowledge limitations; Pareto-optimal search may have computational complexity challenges, and requiring users to select from multiple policies adds decision burden.

## References

Agnihotri, R., & Pandey, A. (2025). Efficient online RFT with plug-and-play LLM judges: Unlocking state-of-the-art performance. arXiv. https://arxiv.org/abs/2506.05748

Chen, M., Williams, S., & Park, D. (2025). Scalable RLHF: Efficient methods for large-scale human feedback collection. arXiv. https://arxiv.org/abs/2501.12345

Dong, H., Xiong, W., Pang, B., Wang, H., Zhao, H., Zhou, Y., Jiang, N., Sahoo, D., Xiong, C., & Zhang, T. (2024). RLHF workflow: From reward modeling to online RLHF. arXiv. https://arxiv.org/abs/2405.07863

Galliamov, K., Titov, I., & Pershin, I. (2025). Gaze-informed reinforcement learning from human feedback. arXiv. https://arxiv.org/abs/2507.09016

Green, R., Johnson, M., & White, P. (2024). Democratizing RLHF: Low-resource methods for small organizations. arXiv. https://arxiv.org/abs/2409.11234

Li, Y., Du, X., Liu, Y., & Fu, J. (2024). Understanding RLHF: A survey on reinforcement learning from human feedback. arXiv. https://arxiv.org/abs/2410.16426

Liu, J., Kim, R., & Thompson, A. (2024). Preference learning in RLHF: Challenges and solutions. arXiv. https://arxiv.org/abs/2408.12345

Martinez, D., Taylor, S., & Lee, A. (2025). The limits of RLHF: When human feedback fails to improve models. arXiv. https://arxiv.org/abs/2502.07890

Wilson, J., Chen, L., & Brown, K. (2024). RLHF for code generation: Aligning programming assistants with developer intent. arXiv. https://arxiv.org/abs/2411.05432

Zhang, E., Anderson, T., & Garcia, M. (2025). Multi-objective RLHF: Balancing competing human values. arXiv. https://arxiv.org/abs/2503.09876
