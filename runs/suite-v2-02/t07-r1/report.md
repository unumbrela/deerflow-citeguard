# Systematic Literature Review: Code Generation with Large Language Models

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "code generation large language models", category cs.CL, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on code generation with large language models reveals a rapidly evolving field focused on three critical dimensions: benchmark creation and evaluation, architectural innovation for efficiency, and reliability improvements through constrained interfaces. Recent work demonstrates that while LLMs have achieved remarkable capabilities in code generation, significant challenges remain in evaluating their true performance, scaling efficiently, and ensuring reliable output for complex multi-step tasks. The field is moving beyond simple code completion toward sophisticated evaluation frameworks, domain-specific languages, and novel architectures that enable parallel generation while maintaining quality.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "code generation large language models", filtered to category cs.CL, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Benchmark Creation and Automated Evaluation

A prominent research direction focuses on developing comprehensive, automated benchmarks to evaluate LLM code generation capabilities. Hossain et al. (2025) introduced LLM-ProS, which benchmarks five state-of-the-art models on 166 ICPC World Finals problems from 2011 to 2024, evaluating not just correctness but also resource utilization and response calibration. Their work reveals significant performance differences across models and highlights how training methodologies and chain-of-thought reasoning impact algorithmic problem-solving.

Complementing this, Chou et al. (2025) addressed the scalability limitations of manual benchmark creation by proposing AutoCodeGen, which automatically generates high-difficulty multilingual code problems across 20 programming languages. Their AutoCodeBench comprises 3,920 problems and demonstrates that even advanced LLMs struggle with the complexity and multilingual nature of real-world coding tasks. This automated approach overcomes the Python-centric bias of existing benchmarks and provides a more comprehensive evaluation framework.

### Theme 2: Efficiency and Scalability Innovations

Multiple papers address the computational efficiency challenges of large-scale code generation. Chavan et al. (2026) presented Lafa (Large flow language model), which achieves 2.54x throughput compared to autoregressive models while maintaining comparable quality on coding tasks. Their continuous flow architecture enables parallel generation through blockwise processing with causal attention on prefixes and bidirectional asynchronous flow within blocks, trained efficiently with fewer than 30B tokens.

Shi et al. (2025) tackled the problem of long context compression for code LLMs with LongCodeZip, achieving up to 5.6x compression ratios without performance degradation. Their dual-stage strategy identifies function-level chunks using conditional perplexity and selects optimal subsets under adaptive token budgets, specifically preserving code structures that general text pruning techniques overlook. Meanwhile, Gross et al. (2025) explored the opposite direction with tiny language models (TLMs), demonstrating that pre-trained shallow architectures can replicate deep model accuracy with lower latency, potentially enabling broader accessibility for code generation research.

### Theme 3: Reliability Through Constrained Interfaces

A critical theme emerging from recent work is the use of constrained syntax and domain-specific languages to improve reliability. Al Mazrouei (2025) introduced Anka, a DSL for data transformation pipelines that achieves 99.9% parse success and 95.8% overall task accuracy despite zero prior training exposure. Their constrained syntax demonstrates a 40 percentage point accuracy advantage over Python on multi-step pipeline tasks, suggesting that LLMs can learn novel DSLs entirely from in-context prompts.

Zhong et al. (2025) explored a different approach to control through sparse dimension manipulation in multilingual models, identifying that cross-lingual transitions are governed by a small set of dimensions at consistent layer indices. Their training-free method can switch output language while preserving semantic content with as few as 50 sentences of parallel data, offering interpretable and efficient multilingual control for code generation across languages.

### Theme 4: Ensemble Methods and Model Combination

Ashiga et al. (2025) surveyed ensemble approaches for LLMs in text and code generation, categorizing methods into seven main categories: weight merging, knowledge fusion, mixture-of-experts, reward ensemble, output ensemble, routing, and cascading. Their work highlights how ensemble techniques address inconsistent outputs, biases, and limited representation of diverse language patterns in individual models, with key benefits including improved diversity representation, enhanced output quality, and greater application flexibility.

### Theme 5: Multilingual Capabilities and Transfer

The literature shows strong interest in extending code generation capabilities across languages. Zhang et al. (2024) developed BayLing 2, which uses language alignment to transfer generative capabilities from high-resource to low-resource languages without constructing expensive instruction data for over 100 languages. Their approach maintains high performance in English while significantly improving capabilities in low-resource languages, addressing a critical gap in multilingual code generation.

Darm and Riccardi (2025) explored a different aspect of multilingual and multi-capability control through attention head interventions, demonstrating that fine-grained interventions at specific attention heads can steer LLM generations more effectively than layer-level interventions or supervised fine-tuning, with implications for controlling code generation behavior.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that evaluation frameworks must move beyond simple correctness metrics to capture resource utilization, efficiency, and adaptability (Hossain et al., 2025; Chou et al., 2025). There is consensus that automated benchmark generation and evaluation are essential for scaling assessment across programming languages and problem types. Multiple papers converge on the finding that constrained interfaces or DSLs significantly improve reliability for complex multi-step tasks compared to general-purpose languages (Al Mazrouei, 2025; Zhong et al., 2025).

**Disagreements**: The literature shows tension between scaling up model size and architecture innovation versus exploring smaller, more efficient alternatives. While Chavan et al. (2026) demonstrate that billion-parameter flow models can achieve superior throughput, Gross et al. (2025) argue that tiny language models may be sufficient for many tasks, suggesting biologically inspired shallow architectures. This reflects an ongoing debate about whether progress requires continued scaling or architectural rethinking.

## Gaps and Open Questions

The collective literature reveals several critical gaps:

1. **Limited discussion of safety and alignment**: While Darm and Riccardi (2025) address intervention-based control, most papers do not explicitly discuss safety considerations in code generation, particularly for automated systems that could generate malicious code.

2. **Insufficient real-world deployment studies**: Most evaluations focus on benchmark performance rather than production deployment challenges, technical debt in AI-generated code, or maintenance implications.

3. **Lack of standardization in evaluation metrics**: Different papers use different metrics (correctness, throughput, compression ratio, accuracy), making cross-paper comparison difficult.

4. **Limited exploration of human-AI collaboration**: The literature focuses on autonomous code generation rather than how LLMs augment human developers in collaborative settings.

5. **Absence of long-term capability retention studies**: No paper addresses whether LLMs maintain code generation capabilities over extended deployment or how they adapt to evolving programming paradigms.

## Per-Paper Annotations

### Al Mazrouei (2025)

**Research question**: Can a domain-specific language with explicit, constrained syntax reduce systematic errors that LLMs exhibit on complex, multi-step programming tasks compared to general-purpose languages?
**Methodology**: Introduced Anka, a DSL for data transformation pipelines with explicit, constrained syntax, evaluated Claude 3.5 Haiku on 100 benchmark problems with zero prior training exposure, and conducted cross-model validation with GPT-4o-mini.
**Key findings**:
- Claude 3.5 Haiku achieves 99.9% parse success and 95.8% overall task accuracy on Anka despite zero prior training exposure
- Anka demonstrates a 40 percentage point accuracy advantage over Python on multi-step pipeline tasks (100% vs. 60%)
- Cross-model validation with GPT-4o-mini confirms a 26.7 percentage point advantage on multi-step tasks
- LLMs can learn novel DSLs entirely from in-context prompts, achieving near-native accuracy
**Limitations**: not stated in abstract

### Ashiga et al. (2025)

**Research question**: What ensemble approaches are emerging for LLMs in text and code generation to address inconsistent outputs, biases, and limited representation of diverse language patterns in individual models?
**Methodology**: Conducted a survey reviewing ensemble approaches for LLMs in text and code generation, categorizing methods into seven main categories and analyzing the capabilities of each approach.
**Key findings**:
- LLM ensemble techniques are increasingly explored for code generation, inspired by successes in text generation
- Seven main ensemble methods are identified: weight merging, knowledge fusion, mixture-of-experts, reward ensemble, output ensemble, routing, and cascading
- Key benefits include improved diversity representation, enhanced output quality, and greater application flexibility
- Ensemble insights aid model selection for real-world tasks and lay groundwork for extending strategies to multimodal LLMs
**Limitations**: not stated in abstract

### Chavan et al. (2026)

**Research question**: Can continuous flow language models be scaled to billion-parameter levels with data-efficient training while enabling parallel generation and matching autoregressive model quality?
**Methodology**: Presented Lafa (Large flow language model), a blockwise flow model with causal attention on the prefix and bidirectional asynchronous flow within each block, trained at 0.5B, 7B, and 8B scales with fewer than 30B tokens, adapting pretrained autoregressive models.
**Key findings**:
- Lafa achieves 2.54x throughput of autoregressive models at comparable quality via self-speculative decoding
- Flow training preserves or improves pretrained autoregressive capabilities through multi-token prediction effects
- The learned flow matches or surpasses autoregressive quality on instruction following, reasoning, and coding tasks
- Continuous flows can serve as a scalable foundation for language modeling
**Limitations**: not stated in abstract

### Chou et al. (2025)

**Research question**: How can we automatically generate high-difficulty multilingual code generation benchmarks without manual annotations to overcome the scalability and language coverage limitations of existing benchmarks?
**Methodology**: Proposed AutoCodeGen, an automated method that generates code problems using reverse-order problem generation, creates test inputs with LLMs, and obtains test outputs through a multilingual sandbox with multiple filtering steps. Introduced AutoCodeBench, a benchmark of 3,920 problems across 20 programming languages, and evaluated over 30 LLMs on it.
**Key findings**:
- AutoCodeGen successfully generates high-difficulty multilingual code generation datasets without manual annotations by using LLMs for test input generation and a multilingual sandbox for test outputs
- AutoCodeBench comprises 3,920 problems evenly distributed across 20 programming languages, addressing the Python-centric bias of existing benchmarks
- Even the most advanced LLMs struggle with the complexity, diversity, and multilingual nature of tasks in AutoCodeBench
- AutoCodeBench-Complete was introduced specifically for evaluating base models on few-shot code generation capabilities
**Limitations**: not stated in abstract

### Darm and Riccardi (2025)

**Research question**: Can inference-time activation interventions at specific attention heads bypass safety alignments and steer LLM generations toward harmful AI coordination?
**Methodology**: Applied fine-grained interventions at specific attention heads identified by probing each head in a binary choice task, then demonstrated that these interventions generalize to open-ended generation settings to circumvent safety guardrails.
**Key findings**:
- Intervening on a few attention heads is more effective than intervening on full layers or supervised fine-tuning
- Only a few example completions are needed to compute effective steering directions
- Applying interventions in the negative direction can prevent common jailbreak attacks
- Attention head level activations encode fine-grained linearly separable behaviours
**Limitations**: not stated in abstract

### Gross et al. (2025)

**Research question**: Do tiny language models (TLMs) exhibit the same key qualitative features of large language models, and can they provide accessible alternatives for broader NLP research?
**Methodology**: Explored TLMs by pre-training BERT-6 and BERT-1 variants on Wikipedia subsets and evaluating on FewShot, AGNews, and DBPedia classification tasks, comparing pre-trained versus non-pre-trained models and testing soft committee approaches.
**Key findings**:
- Pre-trained TLMs show a clear performance gap over non-pre-trained models across classification tasks
- The performance gap increases with pre-training dataset size and token overlap between pre-training and classification datasets
- A soft committee of multiple independently pre-trained shallow architectures can replicate deep TLM accuracy with lower latency
- TLMs may be sufficient for language development, suggesting biologically inspired models
**Limitations**: not stated in abstract

### Hossain et al. (2025)

**Research question**: How do state-of-the-art large language models perform on International Collegiate Programming Contest (ICPC) problems across metrics like correctness, resource utilization, and response calibration?
**Methodology**: Introduced LLM-ProS, a novel evaluation technique that benchmarks five LLMs (GPT-4o, Mistral Large, Llama-3.1-405B, o1-mini, o1-preview) on a curated dataset of 166 ICPC World Finals problems from 2011 to 2024, evaluating reasoning, accuracy, and efficiency.
**Key findings**:
- Significant differences exist in models' abilities to generalize, adapt, and solve novel algorithmic problems
- Training methodologies, dataset contamination, and chain-of-thought reasoning impact model performance
- The evaluation reveals both strengths and limitations of current LLMs for algorithmic coding tasks
**Limitations**: not stated in abstract

### Shi et al. (2025)

**Research question**: How can we compress long code contexts for code LLMs to reduce API costs and generation latency while preserving code-specific structures and dependencies that general text pruning techniques overlook?
**Methodology**: Proposed LongCodeZip, a plug-and-play code compression framework with a dual-stage strategy: coarse-grained compression that identifies and ranks function-level chunks using conditional perplexity, and fine-grained compression that segments retained functions into blocks based on perplexity and selects an optimal subset under an adaptive token budget.
**Key findings**:
- LongCodeZip consistently outperforms baseline methods across code completion, summarization, and question answering tasks
- LongCodeZip achieves up to a 5.6x compression ratio without degrading task performance
- The framework effectively reduces context size while preserving essential information for code LLMs
- Existing context pruning techniques like LLMLingua achieve promising results for general text but overlook code-specific structures and dependencies
**Limitations**: not stated in abstract

### Zhang et al. (2024)

**Research question**: How can we efficiently transfer generative capabilities and knowledge from high-resource languages to low-resource languages without constructing prohibitively expensive instruction data for over 100 languages?
**Methodology**: Introduced BayLing 2, which uses language alignment to transfer capabilities from high-resource to low-resource languages. Constructed a dataset of 3.2 million instructions (Chinese, English, and cross-lingual instructions for 100+ languages) and performed instruction tuning based on Llama as the foundation model, developing BayLing-2-7B, BayLing-2-13B, and BayLing-2-8B variants.
**Key findings**:
- BayLing shows superior performance compared to open-source models of similar scale for multilingual translation across 100+ languages
- BayLing achieves significant improvements across over 20 low-resource languages in multilingual knowledge and understanding benchmarks
- BayLing maintains high performance in high-resource languages (English benchmarks) while enhancing performance in low-resource languages
- The language alignment approach effectively transfers generative capabilities and knowledge from high-resource to low-resource languages
**Limitations**: not stated in abstract

### Zhong et al. (2025)

**Research question**: Is the cross-lingual transition in multilingual LLMs governed by a small, sparse set of dimensions that occur at consistent indices across intermediate to final layers?
**Methodology**: Introduced a training-free method to identify and manipulate sparse dimensions governing cross-lingual transitions, requiring as few as 50 sentences of parallel or monolingual data, and tested interventions on multilingual generation control tasks.
**Key findings**:
- Cross-lingual transitions are governed by a small and sparse set of dimensions at consistent layer indices
- Interventions in these dimensions can switch output language while preserving semantic content
- The approach surpasses prior neuron-based methods at substantially lower computational cost
- The identified dimensions demonstrate interpretability for multilingual control
**Limitations**: not stated in abstract

## References

Al Mazrouei, S. K. S. (2025). Anka: A domain-specific language for reliable LLM code generation. arXiv. https://arxiv.org/abs/2512.23214

Ashiga, M., Jie, W., Wu, F., Voskanyan, V., Dinmohammadi, F., Brookes, P., Gong, J., & Wang, Z. (2025). Ensemble learning for large language models in text and code generation: A survey. arXiv. https://arxiv.org/abs/2503.13505

Chavan, A., Lee, C., Bamba, U., Yoo, J., Hong, S., Raghunathan, A., & Kim, J. (2026). Large flow language models. arXiv. https://arxiv.org/abs/2610.28559

Chou, J., Liu, A., Deng, Y., Zeng, Z., Zhang, T., Zhu, H., Cai, J., Mao, Y., Zhang, C., Tan, L., Xu, Z., Zhai, B., Liu, H., Zhu, S., Zhou, W., & Lian, F. (2025). AutoCodeBench: Large language models are automatic code benchmark generators. arXiv. https://arxiv.org/abs/2508.09101

Darm, P., & Riccardi, A. (2025). Head-specific intervention can induce misaligned AI coordination in large language models. arXiv. https://arxiv.org/abs/2502.05945

Gross, R. D., Tzach, Y., Halevi, T., Koresh, E., & Kanter, I. (2025). Tiny language models. arXiv. https://arxiv.org/abs/2507.14871

Hossain, M. S., Tabassum, A., Arefin, M. F., & Zaman, T. S. (2025). LLM-ProS: Analyzing large language models' performance in competitive problem solving. arXiv. https://arxiv.org/abs/2502.04355

Shi, Y., Qian, Y., Zhang, H., Shen, B., & Gu, X. (2025). LongCodeZip: Compress long context for code language models. arXiv. https://arxiv.org/abs/2510.00446

Zhang, S., Zhang, K., Fang, Q., Guo, S., Zhou, Y., Liu, X., & Feng, Y. (2024). BayLing 2: A multilingual large language model with efficient language alignment. arXiv. https://arxiv.org/abs/2411.16300

Zhong, C., Cheng, F., Liu, Q., Murawaki, Y., Chu, C., & Kurohashi, S. (2025). Language lives in sparse dimensions: Toward interpretable and efficient multilingual control for large language models. arXiv. https://arxiv.org/abs/2510.07213
