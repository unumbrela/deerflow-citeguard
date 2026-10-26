# Systematic Literature Review: Parallel Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: Query "parallel reasoning", category cs.CL, published between 2023-10-14 and 2025-10-13
**Citation format**: APA 7th edition

## Executive Summary

The literature on parallel reasoning in computational linguistics reveals a rapidly evolving field focused on improving reasoning capabilities in large language models through multiple complementary approaches. Recent work has shifted from purely sequential reasoning toward parallel computation strategies that leverage reinforcement learning, test-time scaling, and multi-sample methods. The surveyed papers collectively demonstrate that reasoning performance can be significantly enhanced through parallel thinking mechanisms, efficient resource allocation, and emergent reasoning patterns developed through pure reinforcement learning. Key advances include parallel decoding systems achieving 1.21x-1.93x speedups, reinforcement learning frameworks yielding 8.4% accuracy improvements, and test-time scaling methods exceeding proprietary model performance on mathematical reasoning benchmarks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "parallel reasoning", filtered to category cs.CL, published between 2023-10-14 and 2025-10-13. Papers were selected through citation-based screening from a pool of 50 arXiv matches plus 90 papers from citation expansion, with 30 shortlisted and 10最终 included based on centrality to the topic. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening flow**: Identified by search: 50; Added from references: 90; Shortlisted: 30; Screened: 30; Included: 10 (9 from citation expansion). Score distribution: 0 (8 papers), 1 (19 papers), 2 (1 paper), 3 (2 papers).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Reinforcement Learning for Reasoning Development

A dominant approach in recent work involves using reinforcement learning to incentivize reasoning capabilities without human-labeled demonstrations. DeepSeek-R1 (DeepSeek-AI et al., 2025) demonstrates that pure RL frameworks can facilitate emergent development of advanced reasoning patterns including self-reflection, verification, and dynamic strategy adaptation. Parallel-R1 (Zheng et al., 2025) extends this by employing a progressive curriculum that first uses supervised fine-tuning on easier tasks, then transitions to RL for exploration and generalization on harder problems, achieving 8.4% accuracy improvements over sequential thinking models. This theme represents a fundamental shift from supervised learning approaches toward self-discovered reasoning strategies, with multiple papers reporting superior performance compared to models trained on human demonstrations.

### Theme 2: Test-Time Scaling and Compute Efficiency

Managing computational resources during inference has emerged as a critical challenge, particularly for o1-like models that exhibit overthinking on simple problems. Chen et al. (2024) introduce efficiency metrics from outcome and process perspectives to evaluate rational use of computational resources, proposing self-training strategies that reduce computational overhead while preserving accuracy across varying difficulty levels. Muennighoff et al. (2025) develop budget forcing to control test-time compute by forcefully terminating or lengthening the model's thinking process, enabling extrapolation from 50% to 57% on AIME24. Yang et al. (2025) integrate a thinking budget mechanism in Qwen3 that allows adaptive allocation of computational resources based on task complexity. These approaches collectively address the challenge of intelligently scaling computation during testing rather than applying uniform resource allocation.

### Theme 3: Parallel Decoding and Semantic Independence

Direct parallel computation approaches focus on identifying and exploiting semantic independence in language model decoding. Jin et al. (2025) present PASTA, a learning-based system with PASTA-LANG annotation language and interpreter that orchestrates parallel decoding at inference time. Through two-stage finetuning, LLMs learn to generate annotations that optimize both response quality and decoding speed, achieving Pareto-dominance over existing methods with geometric mean speedups ranging from 1.21x to 1.93x. This represents a departure from hand-crafted heuristics toward learned systems that can identify parallel decoding opportunities, fundamentally changing how sequential generation is conceptualized.

### Theme 4: Self-Consistency and Multi-Sample Methods

Leveraging multiple samples for improved reasoning performance forms another significant research direction. Chen et al. (2023) propose Universal Self-Consistency (USC), which extends traditional self-consistency methods to free-form answers by using LLMs themselves to select the most consistent answer among multiple candidates. The approach effectively utilizes multiple samples across diverse benchmarks including mathematical reasoning, code generation, long-context summarization, and open-ended question answering. Without access to execution results, USC matches execution-based voting performance on code generation tasks, demonstrating the viability of consistency-based selection for open-ended generation where traditional answer extraction is not applicable.

### Theme 5: Efficient Training and Generalization

The question of how much training data is necessary for sophisticated reasoning has been challenged by recent work demonstrating strong performance with minimal datasets. Ye et al. (2025) propose LIMO, which achieves 63.3% accuracy on AIME24 and 95.6% on MATH500 using only 1% of training data required by prior approaches through strategic demonstration design serving as cognitive templates. Shao et al. (2024) introduce DeepSeekMath 7B, continuing pre-training with 120B math-related tokens using engineered data selection and Group Relative Policy Optimization, achieving 51.7% on the MATH benchmark without external toolkits. Qin et al. (2023) extend reasoning across languages through cross-lingual prompting with alignment and self-consistent mechanisms, significantly outperforming existing single-language prompting methods.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that reinforcement learning can develop reasoning capabilities without human-labeled demonstrations (DeepSeek-AI et al., 2025; Zheng et al., 2025). There is broad agreement that test-time compute should be adaptively allocated based on task complexity rather than uniformly applied (Chen et al., 2024; Muennighoff et al., 2025; Yang et al., 2025). The surveyed literature also converges on the effectiveness of multi-sample approaches for improving reasoning performance across diverse benchmarks.

**Disagreements**: The literature presents different perspectives on the data requirements for reasoning development. While Ye et al. (2025) demonstrate that sophisticated reasoning can emerge with minimal training data (1% of typical requirements), Shao et al. (2024) achieve strong results through large-scale pre-training with 120B tokens. This tension between "less is more" and "more data is better" approaches remains unresolved, potentially reflecting different optimal strategies for different model architectures or reasoning domains.

## Gaps and Open Questions

The collective literature reveals several notable gaps. None of the surveyed papers explicitly state limitations in their abstracts, suggesting potential underreporting of methodological constraints or failure modes. The focus on mathematical reasoning benchmarks (MATH, AIME, AMC) raises questions about generalizability to other reasoning domains such as logical reasoning, causal inference, or real-world decision making. The temporal concentration of papers (2024-2025) indicates this is an emerging field, with limited longitudinal analysis of how parallel reasoning approaches evolve over time. Cross-lingual reasoning remains underexplored, with only Qin et al. (2023) addressing multilingual contexts despite the global applicability of reasoning systems.

## Per-Paper Annotations

### Chen et al. (2023)

**Research question**: How can self-consistency methods be extended to work with free-form answers where traditional answer extraction and aggregation processes are not applicable?

**Methodology**: The authors propose Universal Self-Consistency (USC), which leverages LLMs themselves to select the most consistent answer among multiple candidates. They evaluate USC across diverse benchmarks including mathematical reasoning, code generation, long-context summarization, and open-ended question answering.

**Key findings**:
- USC effectively utilizes multiple samples and improves performance on open-ended generation tasks where the original self-consistency method is not applicable
- For mathematical reasoning, USC matches standard self-consistency performance without requiring similar answer formats
- Without access to execution results, USC matches execution-based voting performance on code generation tasks

**Limitations**: not stated in abstract

### Jin et al. (2025)

**Research question**: How can parallel decoding of LLMs be improved beyond hand-crafted heuristics by teaching models to identify semantic independence and express parallel decoding opportunities?

**Methodology**: The authors present PASTA, a learning-based system with PASTA-LANG (an annotation language for expressing semantic independence) and a language interpreter that orchestrates parallel decoding at inference time. They train LLMs through a two-stage finetuning process to generate PASTA-LANG annotations that optimize both response quality and decoding speed.

**Key findings**:
- PASTA Pareto-dominates existing methods in terms of decoding speed and response quality on the AlpacaEval instruction following benchmark
- The approach achieves geometric mean speedups ranging from 1.21x to 1.93x
- Quality changes range from +2.2% to -7.1%, measured by length-controlled win rates against sequential decoding baseline

**Limitations**: not stated in abstract

### Zheng et al. (2025)

**Research question**: How can parallel thinking capabilities be activated in LLMs through training methods that encourage exploration and generalization rather than teacher-forced imitation?

**Methodology**: The authors propose Parallel-R1, the first reinforcement learning framework for parallel thinking, employing a progressive curriculum that first uses SFT on prompt-generated trajectories from easier tasks, then transitions to RL to explore and generalize on harder problems.

**Key findings**:
- Parallel-R1 achieves 8.4% accuracy improvements over sequential thinking models trained directly on challenging tasks with RL on math benchmarks including MATH, AMC23, and AIME
- The model's thinking behavior shifts from using parallel thinking as exploration strategy early on to multi-perspective verification in later stages
- Parallel thinking as a mid-training exploration scaffold yields a 42.9% improvement over baseline on AIME25

**Limitations**: not stated in abstract

### Shao et al. (2024)

**Research question**: How can mathematical reasoning capabilities in open language models be improved to approach the performance of proprietary models like Gemini-Ultra and GPT-4?

**Methodology**: The authors introduce DeepSeekMath 7B by continuing pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens from Common Crawl, using a meticulously engineered data selection pipeline and introducing Group Relative Policy Optimization (GRPO), a variant of PPO.

**Key findings**:
- DeepSeekMath 7B achieves 51.7% on the competition-level MATH benchmark without external toolkits and voting techniques, approaching Gemini-Ultra and GPT-4 performance
- Self-consistency over 64 samples from DeepSeekMath 7B achieves 60.9% on MATH
- The model's capability is attributed to harnessing publicly available web data through engineered data selection and GRPO for enhanced reasoning with optimized memory usage

**Limitations**: not stated in abstract

### Muennighoff et al. (2025)

**Research question**: What is the simplest approach to achieve test-time scaling and strong reasoning performance comparable to proprietary models like OpenAI's o1?

**Methodology**: The authors curate s1K, a small dataset of 1,000 questions with reasoning traces based on difficulty, diversity, and quality criteria, and develop budget forcing to control test-time compute by forcefully terminating or lengthening the model's thinking process. They supervised finetune Qwen2.5-32B-Instruct on s1K and equip it with budget forcing.

**Key findings**:
- s1-32B exceeds o1-preview on competition math questions by up to 27% on MATH and AIME24
- Scaling s1-32B with budget forcing allows extrapolating from 50% to 57% on AIME24
- Budget forcing can lead the model to double-check answers, often fixing incorrect reasoning steps

**Limitations**: not stated in abstract

### DeepSeek-AI et al. (2025)

**Research question**: How can reasoning abilities of LLMs be incentivized without human-labeled reasoning trajectories?

**Methodology**: Pure reinforcement learning (RL) framework that facilitates emergent development of advanced reasoning patterns like self-reflection, verification, and dynamic strategy adaptation.

**Key findings**:
- Reasoning abilities can be incentivized through pure RL without human-annotated demonstrations
- The RL framework enables emergent reasoning patterns including self-reflection, verification, and dynamic strategy adaptation
- Trained model achieves superior performance on mathematics, coding competitions, and STEM fields compared to supervised learning on human demonstrations
- Emergent reasoning patterns can be harnessed to enhance reasoning capabilities of smaller models

**Limitations**: Not stated in abstract

### Chen et al. (2024)

**Research question**: How can computational resources be intelligently and efficiently scaled during testing for o1-like models that exhibit overthinking on simple problems?

**Methodology**: Introduces efficiency metrics from outcome and process perspectives, and uses self-training paradigm to propose strategies that mitigate overthinking while preserving accuracy.

**Key findings**:
- o1-like models allocate excessive computational resources for simple problems with minimal benefit (overthinking phenomenon)
- Novel efficiency metrics from outcome and process perspectives can evaluate rational use of computational resources
- Self-training approach successfully reduces computational overhead while preserving model performance
- Approach works across testsets with varying difficulty levels (GSM8K, MATH500, GPQA, AIME)

**Limitations**: Not stated in abstract

### Yang et al. (2025)

**Research question**: How can large language models be designed to advance performance, efficiency, and multilingual capabilities while integrating both thinking and non-thinking modes?

**Methodology**: Development of Qwen3 series with both dense and Mixture-of-Expert architectures, integrating thinking mode and non-thinking mode in unified framework with thinking budget mechanism.

**Key findings**:
- Qwen3 achieves state-of-the-art results across diverse benchmarks including code generation, mathematical reasoning, and agent tasks
- Integration of thinking and non-thinking modes eliminates need to switch between different models
- Thinking budget mechanism allows adaptive allocation of computational resources based on task complexity
- Multilingual support expanded from 29 to 119 languages and dialects
- Smaller-scale models achieve competitive performance using knowledge from flagship models

**Limitations**: Not stated in abstract

### Ye et al. (2025)

**Research question**: Can sophisticated reasoning in LLMs emerge with minimal training data rather than requiring massive datasets?

**Methodology**: Simple supervised fine-tuning with strategically designed demonstrations serving as cognitive templates, using only 1% of training data required by prior approaches.

**Key findings**:
- LIMO achieves 63.3% accuracy on AIME24 and 95.6% on MATH500 using only 1% of training data
- Outperforms previous fine-tuned models (6.5% on AIME24, 59.2% on MATH500)
- Exhibits strong out-of-distribution generalization with 45.8% absolute improvement across diverse benchmarks
- Outperforms models trained on 100x more data
- Proposes Less-Is-More Reasoning Hypothesis about cognitive templates guiding reasoning

**Limitations**: Not stated in abstract

### Qin et al. (2023)

**Research question**: How can zero-shot chain-of-thought reasoning be generalized across multiple languages beyond single-language prompting techniques?

**Methodology**: Introduces cross-lingual prompting (CLP) with two components: cross-lingual alignment prompting for aligning representations across languages, and task-specific solver prompting for generating chains of thought; also introduces cross-lingual self-consistent prompting (CLSP) for ensembling reasoning paths.

**Key findings**:
- Existing zero-shot prompting techniques are limited to single language, hindering global development
- CLP and CLSP significantly outperform existing prompting methods
- Achieves state-of-the-art performance on several benchmarks
- Cross-lingual alignment prompting successfully aligns representations across different languages
- Cross-lingual self-consistent prompting effectively ensembles different reasoning paths across languages

**Limitations**: Not stated in abstract

## References

Chen, X., Aksitov, R., Alon, U., Ren, J., Xiao, K., Yin, P., Prakash, S., Sutton, C., Wang, X., & Zhou, D. (2023). Universal self-consistency for large language model generation. arXiv. https://arxiv.org/abs/2311.17311

Chen, X., Xu, J., Liang, T., He, Z., Pang, J., Yu, D., Song, L., Liu, Q., Zhou, M., Zhang, Z., Wang, R., Tu, Z., Mi, H., & Yu, D. (2024). Do NOT think that much for 2+3=? On the overthinking of o1-like LLMs. arXiv. https://arxiv.org/abs/2412.21187

DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., Zhu, Q., Xu, R., Zhang, R., Ma, S., Bi, X., Zhang, X., Yu, X., Wu, Y., Wu, Z. F., Gou, Z., Shao, Z., Li, Z., Gao, Z., Liu, A., et al. (2025). DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. arXiv. https://arxiv.org/abs/2501.12948

Jin, T., Cheng, E. Y., Ankner, Z., Saunshi, N., Elias, B. M., Yazdanbakhsh, A., Ragan-Kelley, J., Subramanian, S., & Carbin, M. (2025). Learning to keep a promise: Scaling language model decoding parallelism with learned asynchronous decoding. arXiv. https://arxiv.org/abs/2502.11517

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. arXiv. https://arxiv.org/abs/2501.19393

Qin, L., Chen, Q., Wei, F., Huang, S., & Che, W. (2023). Cross-lingual prompting: Improving zero-shot chain-of-thought reasoning across languages. arXiv. https://arxiv.org/abs/2310.14799

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024). DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. arXiv. https://arxiv.org/abs/2402.03300

Yang, A., Li, A., Yang, B., Zhang, B., Hui, B., Zheng, B., Yu, B., Gao, C., Huang, C., Lv, C., Zheng, C., Liu, D., Zhou, F., Huang, F., Zheng, F., Ge, H., Wei, H., Lin, H., Tang, J., Yang, J., et al. (2025). Qwen3 technical report. arXiv. https://arxiv.org/abs/2505.09388

Ye, Y., Huang, Z., Xiao, Y., Chern, E., Xia, S., & Liu, P. (2025). LIMO: Less is more for reasoning. arXiv. https://arxiv.org/abs/2502.03387

Zheng, T., Zhang, H., Yu, W., Wang, X., Dai, R., Liu, R., Huang, H., Huang, C., Bao, H., & Yu, D. (2025). Parallel-R1: Towards parallel thinking via reinforcement learning. arXiv. https://arxiv.org/abs/2509.07980
