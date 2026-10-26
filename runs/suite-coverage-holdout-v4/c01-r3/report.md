# Systematic Literature Review: Parallel Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "parallel reasoning", category cs.CL, published between 2023-10-14 and 2025-10-13
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers (2023-2025) focused on reasoning efficiency and optimization in large language models. The surveyed literature reveals a critical tension in the field: while Chain-of-Thought (CoT) reasoning has dramatically improved LLM performance on complex tasks, particularly mathematical and symbolic reasoning, the verbosity and redundancy of CoT traces create significant challenges for training efficiency, inference costs, and real-world deployment. The papers collectively explore three main directions: (1) methods to compress or accelerate reasoning without sacrificing accuracy, (2) techniques for controlling reasoning length and compute allocation, and (3) fundamental investigations into when CoT is actually necessary. Notably, the field is moving toward more efficient reasoning paradigms that maintain or even improve accuracy while substantially reducing token consumption.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "parallel reasoning", filtered to category cs.CL, published between 2023-10-14 and 2025-10-13. Papers were identified through arXiv search with citation expansion, shortlisted by relevance scoring, and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Screening results**: 50 papers identified by search, 90 added from reference expansion, 30 shortlisted, 10 included (all from reference expansion, indicating these are highly central papers in the field).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Reasoning Efficiency and Compression

A dominant theme across the surveyed literature is the pursuit of more efficient reasoning mechanisms. Multiple papers address the problem that standard CoT reasoning, while effective, generates excessively long traces with redundant content, superficial exploration of multiple paths, and over-analysis of simple problems (Qu et al., 2025). Xu et al. (2025) propose Chain of Draft (CoD), inspired by human cognitive processes, where LLMs generate minimalistic yet informative intermediate reasoning outputs. Their approach matches or surpasses CoT accuracy while using as little as 7.6% of tokens, demonstrating that verbosity is not necessary for effective reasoning. Similarly, Shen et al. (2025) introduce CODI, which compresses natural language CoT into continuous space through self-distillation, achieving a 3.1x compression rate while matching explicit CoT performance at the GPT-2 scale on GSM8k. These approaches challenge the assumption that verbose, step-by-step reasoning in natural language is optimal, showing that reasoning can be compressed into latent continuous space or condensed drafts without performance degradation.

### Theme 2: Test-Time Compute Control and Length Optimization

Another prominent research direction focuses on controlling how long reasoning models think, enabling fine-grained allocation of test-time compute. Aggarwal and Welleck (2025) introduce Length Controlled Policy Optimization (LCPO), a reinforcement learning method that trains models to produce outputs satisfying length constraints given in prompts. Their L1 model enables smooth trade-offs between computational cost and accuracy, with the 1.5B L1 model surpassing GPT-4o at equal reasoning lengths. Yang et al. (2025) address the "overthinking" problem through dynamic early exit, allowing LLMs to self-truncate CoT sequences during generation by monitoring confidence at reasoning transition points. Their method reduces CoT length by 19.1% to 80.1% across 11 reasoning LLMs while actually improving accuracy by 0.3% to 5.0%, requiring no additional training. Muennighoff et al. (2025) develop "budget forcing" to control test-time compute by forcibly terminating or extending the model's thinking process, enabling performance extrapolation from 50% to 57% on AIME24. These works collectively demonstrate that reasoning length is not fixed but can be dynamically controlled to optimize the accuracy-efficiency trade-off.

### Theme 3: When is Chain-of-Thought Necessary?

A critical meta-question emerging from the literature is when CoT prompting actually provides benefits versus when it is unnecessary overhead. Sprague et al. (2024) conduct a quantitative meta-analysis of over 100 papers and find that CoT gives strong performance benefits primarily on tasks involving math or logic, with much smaller gains on other types of tasks. On MMLU, directly generating answers without CoT leads to almost identical accuracy unless the question involves symbolic operations. This finding suggests that CoT should be applied selectively rather than universally, with significant potential for saving inference costs on tasks where it provides minimal benefit. Wang and Zhou (2024) further investigate whether CoT reasoning paths can be elicited without explicit prompting, finding that CoT paths are frequently inherent in top-k alternative token sequences rather than conventional greedy decoding outputs. This suggests that LLMs have intrinsic reasoning capabilities that can be uncovered through altered decoding processes rather than explicit prompting.

### Theme 4: Mathematical Reasoning as a Testbed

Mathematical reasoning emerges as the dominant benchmark domain for evaluating reasoning improvements. Multiple papers use mathematical benchmarks (MATH, GSM8K, AIME, AMC) as primary evaluation targets, reflecting the field's focus on competition-level mathematical problem-solving. Shao et al. (2024) achieve 51.7% on the competition-level MATH benchmark with DeepSeekMath 7B without external toolkits or voting, approaching the performance of Gemini-Ultra and GPT-4. Yang et al. (2024) develop Qwen2.5-Math with self-improvement throughout the pipeline, using reward models to guide iterative evolution during both training and inference. These mathematical reasoning benchmarks serve as rigorous testbeds because they require multi-step logical deduction, symbolic manipulation, and verification—capabilities that stress-test reasoning architectures in ways that natural language tasks may not.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that (1) standard CoT reasoning is often excessively verbose and contains redundant content (Qu et al., 2025; Xu et al., 2025; Yang et al., 2025), (2) reasoning efficiency can be dramatically improved without sacrificing accuracy (Xu et al., 2025; Shen et al., 2025; Yang et al., 2025), and (3) mathematical reasoning represents a critical benchmark domain for evaluating reasoning capabilities (Shao et al., 2024; Yang et al., 2024; Muennighoff et al., 2025). There is also convergence on the finding that test-time compute allocation can be controlled and optimized (Aggarwal & Welleck, 2025; Muennighoff et al., 2025; Yang et al., 2025).

**Disagreements**: While most papers assume CoT is beneficial for complex reasoning, Sprague et al. (2024) challenge this assumption by showing CoT helps mainly on math and symbolic reasoning tasks, with minimal gains elsewhere. This contrasts with the implicit assumption in other papers that CoT-style reasoning is broadly necessary. Additionally, there is a methodological divergence between approaches that maintain natural language reasoning (Xu et al., 2025; Yang et al., 2025) versus those that compress reasoning into continuous latent space (Shen et al., 2025), with different implications for interpretability and debugging.

## Gaps and Open Questions

Several gaps emerge from the collective limitations of the surveyed literature:

1. **Limited theoretical understanding**: None of the papers provide a comprehensive theoretical framework explaining why certain reasoning compression methods work or what the fundamental limits of reasoning efficiency are.

2. **Narrow evaluation domains**: Heavy reliance on mathematical benchmarks may not generalize to other reasoning domains such as scientific reasoning, legal reasoning, or commonsense reasoning.

3. **Lack of human comparison**: While Xu et al. (2025) reference human drafting behavior, systematic comparison of LLM reasoning efficiency to human reasoning efficiency is largely absent.

4. **Training vs. inference trade-offs**: Most methods focus on inference-time efficiency, but the implications for training efficiency and data requirements are less explored.

5. **Interpretability concerns**: Methods that compress reasoning into continuous space (Shen et al., 2025) raise questions about debugging and understanding model failures, which are not adequately addressed.

## Per-Paper Annotations

### Aggarwal and Welleck (2025)

**Research question**: How can the length of chain-of-thought reasoning in language models be controlled to allocate test-time compute for desired performance levels?

**Methodology**: Introduced Length Controlled Policy Optimization (LCPO), a reinforcement learning method that optimizes for accuracy and adherence to user-specified length constraints, used to train L1, a reasoning model that produces outputs satisfying length constraints given in prompts.

**Key findings**:
- L1's length control allows smooth trading off of computational cost and accuracy across a wide range of tasks
- L1 outperforms the state-of-the-art S1 method for length control
- LCPO enables derivation of Short Reasoning Models (SRMs) that exhibit similar reasoning patterns but with CoT lengths comparable to non-reasoning models
- The 1.5B L1 model surpasses GPT-4o at equal reasoning lengths
- LCPO enables precise control over reasoning length for fine-grained allocation of test-time compute and accuracy

**Limitations**: Not stated in abstract

### Muennighoff et al. (2025)

**Research question**: What is the simplest approach to achieve test-time scaling and strong reasoning performance in language models?

**Methodology**: Curated a small dataset s1K of 1,000 questions with reasoning traces based on difficulty, diversity, and quality criteria, and developed budget forcing to control test-time compute by forcibly terminating or extending the model's thinking process.

**Key findings**:
- After supervised finetuning Qwen2.5-32B-Instruct on s1K with budget forcing, s1-32B exceeds o1-preview by up to 27% on MATH and AIME24
- Scaling s1-32B with budget forcing allows performance extrapolation from 50% to 57% on AIME24
- Budget forcing can lead the model to double-check answers, often fixing incorrect reasoning steps
- The approach uses three validated criteria: difficulty, diversity, and quality for dataset curation
- The model, data, and code are open-source

**Limitations**: Not stated in abstract

### Qu et al. (2025)

**Research question**: How can reasoning efficiency be improved in Large Reasoning Models that tend to produce excessively long and redundant Chain-of-Thought traces?

**Methodology**: Comprehensive survey of recent efforts to improve reasoning efficiency in LRMs, examining methods across the LRM lifecycle from pretraining to inference, identifying common patterns of inefficiency and discussing future research directions.

**Key findings**:
- Large Reasoning Models like DeepSeek-R1 and OpenAI o1 demonstrate strong performance by scaling Chain-of-Thought reasoning length during inference
- Excessively long reasoning traces contain redundant content, over-analysis of simple problems, and superficial exploration of multiple reasoning paths
- This inefficiency creates significant challenges for training, inference, and real-world deployment where token economy is critical
- The survey examines methods proposed across the LRM lifecycle from pretraining to inference to address efficiency challenges

**Limitations**: Not stated in abstract

### Shao et al. (2024)

**Research question**: How can language models be improved to achieve competition-level mathematical reasoning performance without relying on external toolkits or voting techniques?

**Methodology**: Continued pre-training DeepSeek-Coder-Base-v1.5 7B with 120B math-related tokens from Common Crawl and introduced Group Relative Policy Optimization (GRPO), a variant of PPO, to enhance mathematical reasoning while optimizing memory usage.

**Key findings**:
- DeepSeekMath 7B achieved 51.7% on the competition-level MATH benchmark without external toolkits or voting
- Self-consistency over 64 samples from DeepSeekMath 7B achieved 60.9% on MATH
- The performance approaches that of Gemini-Ultra and GPT-4
- Success is attributed to a meticulously engineered data selection pipeline for web data
- GRPO enhances mathematical reasoning abilities while optimizing PPO memory usage

**Limitations**: Not stated in abstract

### Shen et al. (2025)

**Research question**: Can natural language Chain-of-Thought be effectively compressed into continuous space while maintaining reasoning performance?

**Methodology**: Introduced CODI, a training framework that compresses natural language CoT into continuous space through self-distillation, jointly training a teacher task (Explicit CoT) and a student task (Implicit CoT), distilling reasoning ability from language into continuous space by aligning hidden states of a designated token.

**Key findings**:
- CODI is the first implicit CoT approach to match the performance of explicit CoT on GSM8k at the GPT-2 scale
- The approach achieves a 3.1x compression rate and outperforms the previous state-of-the-art by 28.2% in accuracy
- CODI demonstrates robustness generalizable to complex datasets and interpretability
- The results validate that LLMs can reason effectively not only in natural language but also in latent continuous space

**Limitations**: Not stated in abstract

### Sprague et al. (2024)

**Research question**: For what kinds of tasks is Chain-of-Thought prompting really helpful compared to direct answer generation?

**Methodology**: Conducted a quantitative meta-analysis covering over 100 papers using CoT and ran their own evaluations of 20 datasets across 14 models, analyzing CoT behavior by separating planning and execution and comparing against tool-augmented LLMs.

**Key findings**:
- Chain-of-Thought gives strong performance benefits primarily on tasks involving math or logic, with much smaller gains on other types of tasks
- On MMLU, directly generating answers without CoT leads to almost identical accuracy unless the question or response contains an equals sign indicating symbolic operations
- Much of CoT's gain comes from improving symbolic execution, but it underperforms relative to using a symbolic solver
- CoT can be applied selectively to maintain performance while saving inference costs

**Limitations**: Not stated in abstract

### Wang and Zhou (2024)

**Research question**: Can Large Language Models reason effectively without manual prompting techniques?

**Methodology**: Investigated whether CoT reasoning paths can be elicited from pre-trained LLMs by altering the decoding process rather than using conventional greedy decoding, examining top-k alternative tokens to uncover inherent CoT paths and assessing LLMs' intrinsic reasoning abilities.

**Key findings**:
- CoT reasoning paths can be elicited from pre-trained LLMs by simply altering the decoding process without prompting
- CoT paths are frequently inherent in top-k alternative token sequences rather than conventional greedy decoding outputs
- The presence of a CoT in the decoding path correlates with higher confidence in the model's decoded answer
- This confidence metric effectively differentiates between CoT and non-CoT paths
- CoT-decoding effectively elicits reasoning capabilities that were previously obscured by standard greedy decoding

**Limitations**: Not stated in abstract

### Xu et al. (2025)

**Research question**: Can LLMs employ a more efficient reasoning strategy by generating concise intermediate thoughts like humans do through drafting?

**Methodology**: Proposed Chain of Draft (CoD), a novel paradigm inspired by human cognitive processes where LLMs generate minimalistic yet informative intermediate reasoning outputs while solving tasks, reducing verbosity and focusing on critical insights.

**Key findings**:
- Chain of Draft matches or surpasses Chain-of-Thought in accuracy while using as little as 7.6% of the tokens
- The approach significantly reduces cost and latency across various reasoning tasks
- Humans typically employ a more efficient strategy than verbose CoT by drafting concise intermediate thoughts that capture only essential information
- CoD focuses on critical insights rather than verbose, step-by-step reasoning

**Limitations**: Not stated in abstract

### Yang et al. (2024)

**Research question**: How can mathematical expert models be developed by integrating self-improvement philosophy throughout the entire pipeline from pre-training to inference?

**Methodology**: Integrated self-improvement throughout the pipeline: using Qwen2-Math-Instruct to generate mathematical data during pre-training, developing a reward model for iterative supervised fine-tuning and reinforcement learning during post-training, and using the RM to guide sampling during inference.

**Key findings**:
- Qwen2.5-Math-Instruct supports both Chinese and English with advanced mathematical reasoning capabilities
- The model supports Chain-of-Thought (CoT) and Tool-Integrated Reasoning (TIR)
- The models were evaluated on 10 mathematics datasets including GSM8K, MATH, GaoKao, AMC23, and AIME24
- The approach covers difficulties ranging from grade school level to math competition problems
- The reward model enables iterative evolution of data in supervised fine-tuning

**Limitations**: Not stated in abstract

### Yang et al. (2025)

**Research question**: How can reasoning language models avoid overthinking in long chain-of-thought generation while maintaining or improving accuracy?

**Methodology**: Proposed a method that allows LLMs to self-truncate CoT sequences by early exit during generation, monitoring model behavior at potential reasoning transition points and dynamically terminating reasoning when the model exhibits high confidence in a trial answer, requiring no additional training.

**Key findings**:
- The method reduces CoT sequence length by an average of 19.1% to 80.1% across 11 reasoning LLMs
- Accuracy improves by 0.3% to 5.0% while reducing reasoning length
- The method requires no additional training and integrates seamlessly into existing o1-like reasoning LLMs
- The approach is effective across 10 reasoning benchmarks including GSM8K, MATH-500, AMC, GPQA, AIME, and LiveCodeBench
- The method addresses overthinking risks including efficiency loss and accuracy degradation from redundant reasoning steps

**Limitations**: Not stated in abstract

## References

Aggarwal, P., & Welleck, S. (2025). L1: Controlling how long a reasoning model thinks with reinforcement learning. arXiv. https://arxiv.org/abs/2503.04697

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. arXiv. https://arxiv.org/abs/2501.19393

Qu, X., Li, Y., Su, Z.-C., Sun, W., Yan, J., Liu, D., Cui, G., Liu, D., Liang, S., He, J., Li, P., Wei, W., Shao, J., Lu, C., Zhang, Y., Hua, X.-S., Zhou, B., & Cheng, Y. (2025). A survey of efficient reasoning for large reasoning models: Language, multimodality, and beyond. arXiv. https://arxiv.org/abs/2503.21614

Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y. K., Wu, Y., & Guo, D. (2024). DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. arXiv. https://arxiv.org/abs/2402.03300

Shen, Z., Yan, H., Zhang, L., Hu, Z., Du, Y., & He, Y. (2025). CODI: Compressing chain-of-thought into continuous space via self-distillation. arXiv. https://arxiv.org/abs/2502.21074

Sprague, Z., Yin, F., Rodriguez, J. D., Jiang, D., Wadhwa, M., Singhal, P., Zhao, X., Ye, X., Mahowald, K., & Durrett, G. (2024). To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning. arXiv. https://arxiv.org/abs/2409.12183

Wang, X., & Zhou, D. (2024). Chain-of-thought reasoning without prompting. arXiv. https://arxiv.org/abs/2402.10200

Xu, S., Xie, W., Zhao, L., & He, P. (2025). Chain of draft: Thinking faster by writing less. arXiv. https://arxiv.org/abs/2502.18600

Yang, A., Zhang, B., Hui, B., Gao, B., Yu, B., Li, C., Liu, D., Tu, J., Zhou, J., Lin, J., Lu, K., Xue, M., Lin, R., Liu, T., Ren, X., & Zhang, Z. (2024). Qwen2.5-Math technical report: Toward mathematical expert model via self-improvement. arXiv. https://arxiv.org/abs/2409.12122

Yang, C., Si, Q., Duan, Y., Zhu, Z., Zhu, C., Li, Q., Chen, M., Lin, Z., & Wang, W. (2025). Dynamic early exit in reasoning models. arXiv. https://arxiv.org/abs/2504.15895
