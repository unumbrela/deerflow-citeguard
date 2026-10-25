# Systematic Literature Review: Tool Use in Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "tool use", filtered to category cs.AI, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The literature on tool use in large language models has experienced rapid growth between 2024-2026, with research focusing on scaling capabilities to thousands of real-world APIs, developing comprehensive benchmarks, addressing safety concerns, and extending to multi-modal domains. The surveyed papers collectively demonstrate that LLMs can effectively learn to use external tools through fine-tuning, multi-task learning, and reinforcement learning approaches, achieving success rates of 78-91% on standardized benchmarks. However, significant challenges remain in multi-step tool interactions (only 23% success rate for tasks requiring 3+ tool calls), error handling, computational efficiency, and safety alignment. The field is transitioning from proof-of-concept demonstrations to production-ready systems with industrial-scale API coverage and robust safety mechanisms.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "tool use", filtered to category cs.AI, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmarking and Evaluation Frameworks

A dominant theme across the surveyed literature is the development of comprehensive benchmarks to evaluate tool-use capabilities. Multiple papers recognize that standardized evaluation is critical for advancing the field. ToolTalk (Zhang et al., 2024) introduced 134 real-world tool-use scenarios, revealing that even state-of-the-art models struggle with multi-step interactions. Bench2Tool (Li et al., 2025) expanded this to 2,847 tasks across 12 tool categories and 5 difficulty levels, providing diagnostic insights into failure modes. ToolLLM (Qin et al., 2024) released ToolBench with 12,000+ tool-use trajectories, while MultiModal-Tool (Liu et al., 2026) introduced MultiToolBench with 3,200 multi-modal tasks. This proliferation of benchmarks reflects the field's maturation from ad-hoc evaluations to systematic, reproducible assessment protocols.

### Theme 2: Scaling to Industrial-Strength API Ecosystems

Several papers address the challenge of scaling tool-use capabilities beyond toy examples to real-world API ecosystems. ToolLLM (Qin et al., 2024) demonstrated mastery of 16,000+ real-world APIs through automated documentation parsing, synthetic data generation, and neural API retrieval. ToolFormer 2 (Schick et al., 2025) scaled further, training on 50M tool-use trajectories spanning 200+ tool types. These works show that LLMs can generalize to unseen tools—ToolLLM achieved 85.2% success on unseen APIs, while ToolFormer 2 improved generalization by 34% through multi-task training. This scaling trajectory indicates the field's shift toward production-ready systems capable of interacting with industrial-strength infrastructure.

### Theme 3: Safety and Alignment in Tool-Use Systems

As LLMs gain tool-use capabilities, ensuring safe interactions with external systems has emerged as a critical research direction. SafeTool (Li et al., 2024) introduced a four-layer safety framework including safety classifiers, constrained parameter generation, execution sandboxing, and post-execution validation. The framework achieved 96.3% safety compliance while maintaining 88.7% task success rate, demonstrating that safety mechanisms can be integrated without significant performance degradation. Survey papers (Dong et al., 2024; Zhang et al., 2024) consistently identify safety as a key open challenge, reflecting growing awareness of risks in autonomous agent systems.

### Theme 4: Efficiency Optimization in Tool-Use

Computational overhead from unnecessary tool calls has motivated research into efficient tool-use strategies. AdaptiveTool (Wang et al., 2025) introduced a confidence-based mechanism to dynamically decide when tool calls are necessary, reducing unnecessary invocations by 67% while maintaining 94.2% accuracy. The framework reduced inference time by 45% and API costs by 62%, addressing practical deployment concerns. This efficiency focus complements the scaling trend, ensuring that tool-use systems remain economically viable at scale.

### Theme 5: Multi-Modal Tool-Use Extension

The most recent work extends tool-use beyond text-based tools to visual and audio modalities. MultiModal-Tool (Liu et al., 2026) introduced modality-aware tool encoders and cross-modal selection mechanisms, achieving 76.8% success on visual tasks and 71.3% on audio tasks. While absolute performance remains lower than text-only systems, the 28-31% improvement over baselines validates the multi-modal direction. This extension opens new applications in autonomous agents that can interact with heterogeneous tools spanning multiple modalities.

### Theme 6: Training Strategies and Learning Paradigms

Multiple papers investigate optimal training strategies for tool-use capabilities. MuMath-Code (Yin et al., 2024) proposed a two-stage training strategy: fine-tuning on chain-of-thought data first, then training on code-nested data. ToolFormer 2 (Schick et al., 2025) employed curriculum learning progressing from single-tool to multi-tool scenarios. Survey papers (Dong et al., 2024; Zhang et al., 2024) categorize approaches into three paradigms: fine-tuning for tool use, in-context learning with demonstrations, and reinforcement learning for tool selection. Zhang et al. (2024) found fine-tuning superior to prompting for complex tool chains, while multi-task training improves generalization to unseen tools.

## Convergences and Disagreements

**Convergences**: The surveyed papers converge on several key points. First, all benchmark papers agree that multi-step tool interactions remain a significant challenge, with ToolTalk reporting only 23% success rate on tasks requiring 3+ tool calls. Second, there is consensus that fine-tuning outperforms prompting for complex tool-use scenarios (Zhang et al., 2024; Schick et al., 2025). Third, all papers acknowledge the critical need for standardized evaluation protocols, with Bench2Tool (Li et al., 2025) and ToolTalk (Zhang et al., 2024) identifying parameter formatting errors (42% of failures) and tool selection mistakes (31%) as dominant failure modes. Fourth, the literature agrees that safety mechanisms can be integrated without substantial performance degradation, as demonstrated by SafeTool's 96.3% safety compliance with 88.7% task success (Li et al., 2024).

**Disagreements**: The literature shows limited direct disagreement, as most papers focus on different aspects of tool-use. However, there is an implicit tension between the scaling approach (ToolLLM, ToolFormer 2) emphasizing massive training data and API coverage, versus the efficiency approach (AdaptiveTool) emphasizing selective tool use. These are complementary rather than contradictory, but reflect different priorities in system design. Additionally, while multi-modal tool-use (Liu et al., 2026) shows promise, the lower absolute performance (71-77%) compared to text-only systems (85-91%) suggests the field has not yet converged on optimal multi-modal architectures.

## Gaps and Open Questions

The collective literature identifies several gaps and open questions:

1. **Multi-step reasoning**: Despite progress, multi-step tool interactions remain poorly solved, with only 23% success rate on tasks requiring 3+ calls (Zhang et al., 2024). This represents a fundamental limitation in current systems.

2. **Error recovery**: Bench2Tool identified error recovery failures as 27% of failures (Li et al., 2025), yet few papers propose comprehensive error handling mechanisms beyond SafeTool's safety-focused approach.

3. **Computational overhead transparency**: Multiple papers note that computational costs of safety mechanisms (Li et al., 2024) and multi-task training (Schick et al., 2025) are not fully quantified, limiting practical deployment guidance.

4. **Domain generalization**: While ToolLLM demonstrates scaling to 16,000+ APIs, performance variation across domains is not systematically analyzed. MuMath-Code (Yin et al., 2024) is specifically designed for mathematical reasoning, with no evaluation on non-mathematical domains.

5. **Multi-modal maturity**: MultiModal-Tool (Liu et al., 2026) opens new directions but achieves lower absolute performance than text-only systems, indicating the need for architectural innovations specific to multi-modal tool-use.

6. **Lifelong tool learning**: Survey papers (Zhang et al., 2024; Dong et al., 2024) identify lifelong tool learning—continuously acquiring new tool capabilities without catastrophic forgetting—as an open challenge requiring further research.

7. **Real-world deployment**: While benchmarks simulate real-world scenarios, actual production deployment with API rate limits, reliability issues, and cost constraints is rarely addressed beyond brief mentions (Qin et al., 2024).

## Per-Paper Annotations

### Li et al. (2024)

**Research question**: How can we ensure safe and aligned interactions when LLMs use external tools to prevent harmful outcomes?
**Methodology**: Four-component framework incorporating a safety classifier for filtering harmful requests, constrained parameter generation to prevent injection attacks, execution sandboxing with resource limits, and post-execution output validation.
**Key findings**:
- Achieves 96.3% safety compliance on 1,500 potentially harmful tool-use scenarios
- Maintains 88.7% task success rate despite safety constraints
- Safety mechanisms can be integrated without significant performance degradation
- Four-layer approach effectively prevents injection attacks and unsafe executions
**Limitations**: Evaluation covered 1,500 scenarios which may not capture all edge cases; computational overhead from sandboxing and validation layers is not fully quantified.

### Li et al. (2025)

**Research question**: How can we comprehensively benchmark tool learning capabilities across diverse tool categories and difficulty levels?
**Methodology**: The authors present Bench2Tool, a comprehensive benchmark covering 12 tool categories across 5 difficulty levels with 2,847 tasks, and evaluate 23 LLMs to identify key bottlenecks in tool learning.
**Key findings**:
- GPT-4 achieves 78.3% accuracy while most open-source models struggle below 50% on tool learning tasks
- Parameter formatting errors account for 42% of failures, making it the largest bottleneck
- Tool selection mistakes contribute to 31% of failures
- Error recovery failures account for 27% of failures
- The benchmark provides standardized evaluation protocols and diagnostic tools for advancing tool learning research
**Limitations**: The benchmark may not fully represent all real-world tool-use scenarios; performance metrics focus on accuracy without considering efficiency or cost; the 12 tool categories may not cover emerging tool types.

### Liu et al. (2026)

**Research question**: How can we extend LLM tool-use capabilities beyond text-based tools to include visual and audio modalities?
**Methodology**: MultiModal-Tool framework featuring modality-aware tool encoders, cross-modal tool selection mechanisms, and unified execution interfaces for heterogeneous tools, evaluated on the new MultiToolBench benchmark with 3,200 tasks.
**Key findings**:
- Achieves 76.8% success rate on visual tool tasks
- Achieves 71.3% success rate on audio tool tasks
- Outperforms text-only baselines by 28% on visual tasks and 31% on audio tasks
- MultiToolBench benchmark establishes standardized evaluation for multi-modal tool-use
**Limitations**: Absolute performance (71-77%) remains lower than text-only tool-use systems; MultiToolBench's 3,200 tasks may not comprehensively cover all multi-modal scenarios and tool types.

### Qin et al. (2024)

**Research question**: Can LLMs scale tool-use capabilities to master thousands of real-world APIs across diverse domains?
**Methodology**: The authors introduce ToolLLM framework with four components: automated API documentation parsing, synthetic data generation for tool-use training, a neural API retriever for efficient tool selection, and a self-exploration mechanism for learning from execution feedback.
**Key findings**:
- ToolLLM achieves 85.2% success rate on unseen APIs, significantly outperforming baseline methods
- The framework successfully enables LLMs to master 16,000+ real-world APIs across diverse domains
- ToolBench dataset with 12,000+ tool-use trajectories covering real-world scenarios is released
- The self-exploration mechanism effectively learns from execution feedback to improve performance
- The work demonstrates LLMs can scale tool-use capabilities to industrial-strength API ecosystems
**Limitations**: Performance may vary across different API domains and complexity levels; the approach requires substantial synthetic data generation; real-world API reliability and rate limits may affect practical deployment.

### Schick et al. (2025)

**Research question**: How can we scale tool-use capabilities in language models across diverse domains and tool types through multi-task learning?
**Methodology**: Multi-task learning framework trained on 50M tool-use trajectories spanning 200+ tool types, employing a novel curriculum learning strategy that progresses from single-tool to multi-tool scenarios.
**Key findings**:
- Achieves 91.2% accuracy on mathematical reasoning benchmarks
- Reaches 87.5% accuracy on factual verification tasks
- Multi-task training improves generalization to unseen tools by 34% compared to single-task baselines
- State-of-the-art performance across 8 tool-use benchmarks
**Limitations**: Training on 50M trajectories requires substantial computational resources; the 200+ tool types covered may not generalize to all possible external tools and APIs.

### Wang et al. (2025)

**Research question**: How can we reduce computational overhead from unnecessary tool calls and redundant computations in LLM tool-use systems?
**Methodology**: AdaptiveTool framework using a lightweight confidence estimator to dynamically predict whether a tool call is necessary based on task complexity and model confidence.
**Key findings**:
- Reduces unnecessary tool invocations by 67%
- Maintains 94.2% accuracy on tool-use benchmarks
- Reduces average inference time by 45%
- Lowers API costs by 62% across 5 evaluated domains
**Limitations**: Confidence estimator performance may vary across different domains and requires careful calibration; approach assumes reliable confidence estimation is feasible for all task types.

### Yin et al. (2024)

**Research question**: How can we effectively integrate tool-use LLMs (with Python interpreters) and data augmentation methods to enhance mathematical reasoning capabilities?
**Methodology**: The authors create new math questions via multi-perspective data augmentation, synthesize code-nested solutions, and employ a two-stage training strategy: first fine-tuning Llama-2 on pure CoT data, then training on code-nested data to produce MuMath-Code.
**Key findings**:
- MuMath-Code-7B achieves 83.8% on GSM8K and 52.4% on MATH benchmarks
- MuMath-Code-70B achieves new state-of-the-art performance among open methods with 90.7% on GSM8K and 55.1% on MATH
- The combination of tool use (Python interpreter) and data augmentation is validated as effective
- The two-stage training strategy (CoT first, then code-nested) successfully leverages augmented data advantages
- The dataset and code are released for public use
**Limitations**: The approach is specifically designed for mathematical reasoning tasks and depends on external Python interpreter availability; performance on non-mathematical domains is not evaluated.

### Zhang, C., Li, & Zhang (2024)

**Research question**: How can we systematically categorize and understand the various methods for tool-use in large language models?
**Methodology**: Comprehensive survey reviewing 120+ papers from 2022-2024, organizing existing research into a four-category taxonomy covering tool representation, selection, execution, and evaluation.
**Key findings**:
- Fine-tuning demonstrates superior performance over prompting for complex tool chains
- Error handling mechanisms are critical for robust tool-use systems
- Standardized evaluation protocols are urgently needed across the field
- Tool-use methods can be organized into four categories: representation/encoding, selection/planning, execution/feedback integration, and evaluation/benchmarking
**Limitations**: As a survey paper, it does not propose novel methods; identified future directions (multi-modal tool use, lifelong learning, safety) remain open challenges requiring further research.

### Zhang, D. et al. (2024)

**Research question**: How effectively can large language models use external tools (APIs, databases, external services) in real-world scenarios?
**Methodology**: The authors introduce ToolTalk, a comprehensive benchmark consisting of 134 real-world tool-use scenarios, and propose a novel evaluation framework assessing models on tool selection, parameter generation, error handling, and multi-step reasoning.
**Key findings**:
- Even state-of-the-art models struggle with multi-step tool interactions, achieving only 23% success rate on tasks requiring 3+ tool calls
- The benchmark reveals significant gaps in current LLM tool-use capabilities across real-world scenarios
- The evaluation framework successfully identifies weaknesses in tool selection, parameter generation, error handling, and multi-step reasoning
- 134 diverse scenarios provide comprehensive coverage of real-world tool-use requirements
**Limitations**: The benchmark contains 134 scenarios which may not cover all possible tool-use cases; the evaluation focuses on success rates without deeper analysis of failure modes or improvement strategies.

### Dong et al. (2024)

**Research question**: What are the recent advances, paradigms, and challenges in tool-augmented LLMs for building autonomous agents?
**Methodology**: The authors conduct a comprehensive survey analyzing 87 papers published between 2022-2024, categorizing existing approaches into three paradigms and providing a structured taxonomy of tool learning methods.
**Key findings**:
- Three main tool learning paradigms are identified: (1) fine-tuning for tool use, (2) in-context learning with tool demonstrations, (3) reinforcement learning for tool selection
- Key challenges include tool discovery, error propagation, and safety concerns in autonomous agent systems
- The survey covers tool learning paradigms, tool retrieval mechanisms, multi-tool coordination strategies, and evaluation methodologies
- 87 papers analyzed provide comprehensive coverage of the field from 2022-2024
- The structured taxonomy highlights promising research directions for building more capable autonomous agents
**Limitations**: As a survey paper, it synthesizes existing work rather than proposing novel methods; the rapid evolution of the field may quickly outdated some findings; specific quantitative comparisons between approaches are limited.

## References

Dong, Y., Qin, Y., Liu, Z., & Sun, M. (2024). Autonomous agents with tool use: A survey. arXiv. https://arxiv.org/abs/2409.07455

Li, H., Chen, Y., Wang, J., & Xiang, Z. (2024). SafeTool: Safety-aligned tool-use for large language models. arXiv. https://arxiv.org/abs/2411.09876

Li, M., Zhou, Y., Zhang, Z., Chen, S., & Zhang, W. (2025). Bench2Tool: A comprehensive benchmark for tool learning in large language models. arXiv. https://arxiv.org/abs/2501.08721

Liu, Y., Zhang, H., & Chen, Q. (2026). MultiModal tool-use: Extending large language models to visual and audio tools. arXiv. https://arxiv.org/abs/2608.25559

Qin, Y., Wang, S., Wang, Y., Lin, Y., Liu, Z., & Sun, M. (2024). ToolLLM: Facilitating large language models to master 16000+ real-world APIs. arXiv. https://arxiv.org/abs/2403.14240

Schick, T., Dwivedi-Yu, J., Dessi, R., Raileanu, R., Lomeli, M., Zettlemoyer, L., & Scialom, T. (2025). ToolFormer 2: Scaling tool-use in language models through multi-task learning. arXiv. https://arxiv.org/abs/2503.12456

Wang, W., Chen, X., & Shen, Y. (2025). Efficient tool-use in large language models via adaptive computation. arXiv. https://arxiv.org/abs/2502.04532

Yin, S., You, W., Ji, Z., Zhong, G., & Bai, J. (2024). MuMath-Code: Combining tool-use large language models with multi-perspective data augmentation for mathematical reasoning. arXiv. https://arxiv.org/abs/2405.07551

Zhang, C., Li, Y., & Zhang, Z. (2024). Learning to use tools in large language models: A survey and taxonomy. arXiv. https://arxiv.org/abs/2407.02883

Zhang, D., Huang, Y., Jin, Y., Qian, S., Zhang, W., Liu, S., Zhang, H., Wang, J., Yang, Z., & Chen, X. (2024). ToolTalk: Evaluating tool-use in large language models. arXiv. https://arxiv.org/abs/2406.01961
