# Systematic Literature Review: Code Generation with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "code generation", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on code generation with large language models published between October 2024 and October 2026. The surveyed literature reveals a field rapidly advancing along multiple dimensions: multimodal integration (combining visual design inputs with textual instructions), constraint satisfaction and controlled generation, iterative self-improvement through self-training and distillation, and novel decoding strategies to address repetition problems. Research demonstrates that modern code generation systems are moving beyond simple text-to-code translation toward sophisticated pipelines incorporating debugging agents, constraint-aware inference, narrative reformulation for structured reasoning, and causal analysis of prompt modalities. Performance improvements are substantial, with some models achieving GPT-4-comparable results and multi-agent approaches reaching 95.4% Pass@1 scores on specialized benchmarks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query `code generation`, filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Multi-Agent and Iterative Refinement Approaches

A prominent direction in recent code generation research involves multi-agent architectures and iterative self-improvement cycles. Rather than relying on single-pass generation, these systems employ multiple specialized agents or iterative refinement loops to improve code quality. Sorokin et al. (2025) demonstrated that iterative self-training with reinforced re-ranking enables a 13.4B parameter model to outperform a 33B model while being three times faster, achieving GPT-4-comparable performance. Saadi et al. (2025) achieved first place in the BLP-2025 Shared Task with a two-agent pipeline where a code-generation agent produces initial solutions and a debugger agent analyzes error traces to generate revisions, reaching 95.4% Pass@1. Zhang et al. (2026) showed that simple self-distillation using only the model's own raw outputs can improve pass@1 from 42.4% to 55.3% on LiveCodeBench v6, with gains concentrating on harder problems. These convergent findings suggest that iterative refinement and multi-agent collaboration are more effective than simply scaling model size.

### Theme 2: Multimodal and Multilingual Integration

Recent work increasingly integrates multiple input modalities and supports diverse programming languages. Chai et al. (2025) introduced MM-Coder, which integrates visual workflow inputs (UML diagrams and flowcharts) with textual instructions, supported by the MMc-Instruct multimodal dataset and evaluated on the MMEval benchmark. Their work reveals that current models face significant challenges in precise visual information capture and instruction following across modalities. Yang et al. (2025) presented IFEvalCode, a multilingual benchmark with 1.6K test samples across seven programming languages (Python, Java, JavaScript, TypeScript, Shell, C++, and C#) with Chinese and English queries, using decoupled evaluation metrics for correctness and instruction-following. Their findings indicate a significant gap between models' ability to generate correct code versus code that precisely follows instructions, with closed-source models outperforming open-source alternatives. Gupta et al. (2025) applied causal analysis to understand how different prompt modalities affect code generation, revealing that input-output examples significantly influence code generation beyond natural language instructions.

### Theme 3: Constraint Satisfaction and Controlled Generation

Ensuring that generated code satisfies constraints—whether functional, security-related, or syntactic—has emerged as a critical research direction. Shao et al. (2026) introduced Constrained Diffusion for Code (CDC), a training-free neurosymbolic inference framework that integrates constraint satisfaction directly into the reverse denoising process of discrete diffusion models. CDC uses constraint-aware denoising operators combining mathematical optimization with program analysis, consistently improving constraint satisfaction in functional correctness, security, and syntax while requiring less corrective computation than autoregressive baselines. Yang et al. (2025) emphasized that code LLMs need improvement in following detailed constraints beyond mere code correctness, proposing forward and backward constraint generation methods. This theme reflects a maturation of the field from "can it generate code?" to "can it generate code that satisfies specific requirements?"

### Theme 4: Addressing Structural Repetition and Decoding Challenges

The problem of repetition in LLM-generated code has received focused attention, with researchers distinguishing between content repetition and the more prevalent structural repetition. Dong et al. (2025) formally defined structural repetition and proposed RPG (Repetition Penalization based on Grammar), a decoding approach that uses grammar rules to identify repetition and strategically decays the likelihood of critical tokens contributing to repetitions. Their CodeRepetEval dataset was constructed to comprehensively evaluate approaches for mitigating repetition problems, and RPG substantially outperformed baselines on CodeRepetEval, HumanEval, and MBPP benchmarks. This work highlights that decoding strategies, not just model architecture or training data, play a crucial role in code generation quality.

### Theme 5: Narrative and Structured Reasoning Reformulation

Recent research has explored reformulating code generation problems to guide models toward better reasoning. Jang et al. (2026) proposed StoryCoder, a narrative reformulation framework that transforms code generation questions into three-component narratives (task overview, constraints, and example test cases) guided by selected algorithm and genre. Their approach achieved an average gain of 18.7% in zero-shot pass@10 across 11 models on HumanEval, LiveCodeBench, and CodeForces benchmarks, with benefits depending on narrative coherence and genre alignment. This theme suggests that how problems are presented to models—structuring the reasoning task—can be as important as the model's underlying capabilities.

### Theme 6: Comparative Architecture Studies

Foundational comparative work continues to inform the field's understanding of architectural choices. Das et al. (2024) conducted a comparative study on transformer architectures for automated C++ code generation, evaluating models based on architecture complexities and capability to handle diverse problem sets from basic arithmetic to complex computations. While their abstract provides limited detail on specific findings, this work addresses the need to systematically compare transformer architectures for code generation tasks, providing baseline understanding for more specialized approaches.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that iterative refinement and multi-agent approaches outperform single-pass generation (Sorokin et al., 2025; Saadi et al., 2025; Zhang et al., 2026). There is broad agreement that constraint satisfaction and instruction-following represent critical challenges distinct from mere code correctness (Yang et al., 2025; Shao et al., 2026). The literature consistently shows that closed-source models outperform open-source alternatives in controllable code generation (Yang et al., 2025), and that multimodal integration remains challenging despite promising approaches (Chai et al., 2025).

**Disagreements**: The surveyed papers do not present direct contradictions, as they address different aspects of code generation rather than competing claims. However, there is an implicit tension between approaches that emphasize architectural innovation (multi-agent systems, diffusion models) versus those that focus on presentation reformulation (narrative restructuring) or decoding strategies (repetition penalization). The field has not yet established which approach yields the most generalizable improvements.

## Gaps and Open Questions

Several gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations are addressed only in full paper text or that the field has not yet developed standardized practices for articulating constraints. Second, while multimodal integration is proposed (Chai et al., 2025), the MMEval benchmark reveals "significant challenges" that remain unaddressed. Third, the causal analysis work (Gupta et al., 2025) identifies that input-output examples influence code generation, but does not provide prescriptive guidance for optimal example selection. Fourth, there is limited discussion of security implications beyond CDC's mention of security constraints (Shao et al., 2026). Finally, the focus on English and Chinese queries (Yang et al., 2025) suggests underrepresentation of other natural languages in code generation research.

## Per-Paper Annotations

### Chai et al. (2025)

**Research question**: How can code generation be improved by integrating visual design inputs like diagrams and flowcharts alongside textual instructions?
**Methodology**: The authors introduce MM-Coder, which integrates visual workflow inputs (UML diagrams and flowcharts) with textual instructions, supported by the MMc-Instruct multimodal instruction-tuning dataset and evaluated using the new MMEval benchmark.
**Key findings**:
- MM-Coder integrates visual design inputs (UML diagrams and flowcharts) with textual instructions for enhanced code generation.
- The MMc-Instruct dataset provides diverse multimodal instruction-tuning data including visual-workflow-based code generation.
- MMEval benchmark reveals significant challenges in models' precise visual information capture, instruction following, and advanced programming knowledge.
- Current models face remaining challenges in multimodal code generation despite the proposed approach.
**Limitations**: not stated in abstract

### Das et al. (2024)

**Research question**: How do transformer architectures compare in their performance for automated C++ code generation across different model complexities and problem sets?
**Methodology**: The authors introduce a Transformer-based model using NLP methodologies to automatically generate C++ source code and perform a comparative study evaluating transformer-based models based on their architecture complexities and capability to handle diverse problem sets from basic arithmetic to complex computations.
**Key findings**:
- The study evaluates the robustness of transformer-based models based on architecture complexities.
- The models are assessed on their capability to handle diverse problem sets.
- The approach addresses the need to compare transformer architectures for code generation tasks.
**Limitations**: not stated in abstract

### Dong et al. (2025)

**Research question**: How can structural repetition in code generation be formally defined and mitigated beyond the narrower focus on content repetition?
**Methodology**: The paper formally defines structural repetition and proposes RPG (Repetition Penalization based on Grammar), a decoding approach that uses grammar rules to identify repetition and strategically decays the likelihood of critical tokens contributing to repetitions, evaluated on the new CodeRepetEval dataset.
**Key findings**:
- Structural repetition is more prevalent and challenging than content repetition, with repeated code appearing in various patterns but possessing fixed structures reflected in grammar.
- RPG leverages grammar rules to identify repetition problems during code generation.
- RPG strategically decays the likelihood of critical tokens that contribute to repetitions.
- RPG substantially outperforms baselines on CodeRepetEval, HumanEval, and MBPP benchmarks.
- The CodeRepetEval dataset was constructed to comprehensively evaluate approaches for mitigating repetition problems.
**Limitations**: not stated in abstract

### Gupta et al. (2025)

**Research question**: What are the causal effects of different prompt modalities on multi-modal code generation using LLMs?
**Methodology**: CodeSCM is proposed as a Structural Causal Model that applies interventions to measure causal effects of prompt modalities, using latent mediator variables to separate code and natural language semantics and applying Causal Mediation Analysis to quantify direct effects.
**Key findings**:
- CodeSCM introduces latent mediator variables to separate code and natural language semantics in multi-modal prompts.
- Causal Mediation Analysis quantifies direct effects representing the model's spurious leanings.
- Input-output examples significantly influence code generation in addition to natural language instructions.
**Limitations**: not stated in abstract

### Jang et al. (2026)

**Research question**: Can transforming code generation questions into coherent natural language narratives improve LLM code generation performance by providing richer contextual structure?
**Methodology**: The authors propose StoryCoder, a narrative reformulation framework that transforms code generation questions into three-component narratives (task overview, constraints, and example test cases) guided by selected algorithm and genre. Experiments were conducted across 11 models on HumanEval, LiveCodeBench, and CodeForces benchmarks.
**Key findings**:
- Narrative reformulation achieves an average gain of 18.7% in zero-shot pass@10 across 11 models.
- The approach guides models toward correct algorithmic strategies.
- Narrative reformulation reduces implementation errors and induces more modular code structure.
- Benefits depend on narrative coherence and genre alignment.
**Limitations**: not stated in abstract

### Saadi et al. (2025)

**Research question**: How can a multi-agent approach improve code generation from Bangla instructions?
**Methodology**: A two-agent pipeline where a code-generation agent produces initial solutions, and only failing test cases are forwarded to a debugger agent that analyzes error traces and generates revised solutions conditioned on error messages, tests, and current code.
**Key findings**:
- The multi-agent approach achieved first place in the BLP-2025 Shared Task with a Pass@1 score of 95.4.
- Only failing test cases are forwarded to the debugger agent, reducing unnecessary processing.
- The debugger agent conditions on error traces, test cases, and the current program to generate revisions.
- The system code has been made publicly available.
**Limitations**: not stated in abstract

### Shao et al. (2026)

**Research question**: How can constraint satisfaction be integrated into discrete diffusion models for code generation to enforce program-level functionality and security constraints?
**Methodology**: The authors introduce Constrained Diffusion for Code (CDC), a training-free neurosymbolic inference framework that integrates constraint satisfaction directly into the reverse denoising process using constraint-aware denoising operators that combine mathematical optimization with program analysis. The approach was evaluated across code generation benchmarks.
**Key findings**:
- CDC consistently improves constraint satisfaction in functional correctness, security, and syntax.
- CDC outperforms discrete diffusion and autoregressive baselines.
- The approach requires less corrective computation and produces more localized edits.
- The framework enables natural intervention points for enforcing constraints before final code is committed.
**Limitations**: not stated in abstract

### Sorokin et al. (2025)

**Research question**: How can we improve code generation quality by developing a robust reranking model using iterative self-training with Proximal Policy Optimization?
**Methodology**: The authors propose a novel iterative self-training approach that uses PPO to develop a reranking model, which iteratively refines the training dataset by re-evaluating outputs, identifying high-scoring negative examples, and incorporating them into the training loop. The method was evaluated on the MultiPL-E dataset.
**Key findings**:
- The 13.4B parameter model outperforms a 33B model in code generation quality while being three times faster.
- The model achieves performance comparable to GPT-4.
- The model surpasses GPT-4 in one programming language.
- The iterative self-training approach improves both reranking accuracy and overall code generation process.
**Limitations**: not stated in abstract

### Yang et al. (2025)

**Research question**: How can code LLMs be improved to better follow detailed constraints beyond mere code correctness?
**Methodology**: The paper introduces forward and backward constraints generation methods and presents IFEvalCode, a multilingual benchmark with 1.6K test samples across seven programming languages, using decoupled evaluation metrics for correctness and instruction-following.
**Key findings**:
- IFEvalCode provides 1.6K test samples across Python, Java, JavaScript, TypeScript, Shell, C++, and C# with Chinese and English queries.
- Evaluation is decoupled into correctness (Corr.) and instruction-following (Instr.) metrics for nuanced assessment.
- Closed-source models outperform open-source models in controllable code generation.
- There is a significant gap between models' ability to generate correct code versus code that precisely follows instructions.
**Limitations**: not stated in abstract

### Zhang et al. (2026)

**Research question**: Can a large language model improve at code generation using only its own raw outputs through simple self-distillation without external verifiers, teacher models, or reinforcement learning?
**Methodology**: The authors propose simple self-distillation (SSD), which samples solutions from the model with certain temperature and truncation configurations, then fine-tunes on those samples with standard supervised fine-tuning. The method was tested across Qwen and Llama models at 4B, 8B, and 30B scale on LiveCodeBench v6.
**Key findings**:
- SSD improves Qwen3-30B-Instruct from 42.4% to 55.3% pass@1 on LiveCodeBench v6.
- Gains concentrate on harder problems.
- The method generalizes across Qwen and Llama models at 4B, 8B, and 30B scale, including both instruct and thinking variants.
- SSD reshapes token distributions in a context-dependent way, suppressing distractor tails where precision matters while preserving useful diversity where exploration matters.
**Limitations**: not stated in abstract

## References

Chai, L., Yang, J., Liu, S., Zhang, W., Wang, L., Jin, K., Sun, T., Liu, C., Zhang, C., Zhu, H., Liu, J., Wu, X., Zhang, G., Liu, T., & Li, Z. (2025). Multilingual multimodal software developer for code generation. arXiv. https://arxiv.org/abs/2507.08719

Das, N., Panta, R., Karki, N., Manandhar, R., & Kshatri, D. B. (2024). A comparative study on code generation with transformers. arXiv. https://arxiv.org/abs/2412.05749

Dong, Y., Liu, Y., Jiang, X., Jin, Z., & Li, G. (2025). Rethinking repetition problems of LLMs in code generation. arXiv. https://arxiv.org/abs/2505.10402

Gupta, M., Bhatt, N., & Jana, S. (2025). CodeSCM: Causal analysis for multi-modal code generation. arXiv. https://arxiv.org/abs/2502.05150

Jang, G., Han, D., & Yoo, Y. (2026). StoryCoder: Narrative reformulation for structured reasoning in LLM code generation. arXiv. https://arxiv.org/abs/2604.14631

Saadi, H. S., Alam, F., Sanz-Guerrero, M., Bui, M. D., Mager, M., & von der Wense, K. (2025). NALA_MAINZ at BLP-2025 Task 2: A multi-agent approach for Bangla instruction to Python code generation. arXiv. https://arxiv.org/abs/2511.16787

Shao, L., Cardei, M., Xie, Z., Fioretto, F., & Wang, W. (2026). Constrained code generation with discrete diffusion. arXiv. https://arxiv.org/abs/2605.16829

Sorokin, N., Sedykh, I., & Malykh, V. (2025). Iterative self-training for code generation via reinforced re-ranking. arXiv. https://arxiv.org/abs/2504.09643

Yang, J., Zhang, W., Liu, S., Chai, L., Tan, Y., Liu, J., Zhang, G., Zhou, W., Niu, G., Li, Z., Hui, B., & Lin, J. (2025). IFEvalCode: Controlled code generation. arXiv. https://arxiv.org/abs/2507.22462

Zhang, R., Bai, R. H., Zheng, H., Jaitly, N., Collobert, R., & Zhang, Y. (2026). Embarrassingly simple self-distillation improves code generation. arXiv. https://arxiv.org/abs/2604.01193
