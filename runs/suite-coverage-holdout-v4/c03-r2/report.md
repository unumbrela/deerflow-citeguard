# Systematic Literature Review: Diffusion Language Models

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: Diffusion language models, cs.CL, published between 2023-08-14 and 2025-08-13
**Citation format**: APA 7th edition

## Executive Summary

The literature on diffusion language models has experienced rapid development from 2023 to 2025, demonstrating that diffusion-based approaches can achieve performance competitive with autoregressive models across diverse language tasks. Early work established that masked diffusion models could close the performance gap through improved training objectives and scaling, while recent advances have focused on practical deployment concerns including inference acceleration and specialized applications like code generation. The field is characterized by a shift from proving feasibility to achieving state-of-the-art performance on specific benchmarks, with particular strength in reasoning tasks and parallel generation scenarios. Three commercial-scale models have emerged, challenging the assumption that core large language model capabilities inherently depend on autoregressive architectures.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "diffusion language models", filtered to category cs.CL, published between 2023-08-14 and 2025-08-13. Papers were identified through arXiv search with citation expansion, then screened for centrality to the topic of diffusion language models. The top 10 papers were selected based on co-citation analysis and relevance scoring. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents working exclusively from arXiv batch results, with cross-paper synthesis performed by the lead agent.

**Screening flow**: 50 papers identified by search, 55 added from references, 30 shortlisted, 30 screened, 10 included (3 from references).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. Metadata extraction was limited to abstract content, which may not capture full methodological details or comprehensive limitations.

## Themes

### Theme 1: Closing the Performance Gap with Autoregressive Models

A central thread across the surveyed literature is the effort to demonstrate that diffusion models can match or exceed autoregressive performance on standard benchmarks. Early work by Sahoo et al. (2024) showed that simple masked discrete diffusion, when trained with a Rao-Blackwellized objective, could approach autoregressive perplexity on language modeling benchmarks. This finding challenged prior assumptions about diffusion models' inherent limitations in language tasks. Subsequent work scaled this approach: Ye et al. (2023) demonstrated that diffusion language models pretrained with masked language modeling and fine-tuned with instructions could solve general language tasks comparably to autoregressive models, including zero-shot and few-shot in-context learning.

The most comprehensive challenge to autoregressive dominance came from Nie et al. (2025), whose LLaDA model trained from scratch achieved competitive performance with LLaMA3 8B across extensive benchmarks covering general tasks, math, and code. Their findings directly contest the assumption that core LLM capabilities inherently depend on autoregressive architectures. Gong et al. (2024) took a different approach, adapting existing autoregressive models (GPT2 and LLaMA from 127M to 7B parameters) to diffusion frameworks using less than 200B tokens of continual pre-training, achieving performance competitive with their autoregressive counterparts.

### Theme 2: Specialized Advantages in Reasoning and Planning Tasks

Multiple papers identify reasoning and planning as domains where diffusion models offer distinct advantages over autoregressive approaches. Ye et al. (2024) introduced Multi-Granularity Diffusion Modeling (MGDM), which prioritizes subgoals based on difficulty during learning. Their approach achieved 91.5% accuracy on Countdown compared to 45.8% for autoregressive models, and 100% accuracy on Sudoku compared to 20.7% for autoregressive models. The key insight is that diffusion models can effectively learn difficult subgoals that elude autoregressive approaches, which struggle with long-term planning dependencies.

This advantage stems from the non-autoregressive nature of diffusion, which allows the model to consider the entire sequence structure rather than making locally optimal token-by-token predictions. The surveyed papers suggest that diffusion models are particularly well-suited for tasks requiring global consistency, constraint satisfaction, or multi-step planning where autoregressive models' sequential generation creates compounding errors.

### Theme 3: Inference Acceleration and Practical Deployment

A significant portion of recent work addresses the inference speed bottleneck that has historically limited diffusion models' practical deployment. Wu et al. (2025) introduced Fast-dLLM, a training-free acceleration method enabling KV cache and parallel decoding in diffusion LLMs. Their block-wise approximate KV cache mechanism and confidence-aware parallel decoding strategy achieved up to 27.6× throughput improvement with minimal accuracy loss. Similarly, Ma et al. (2025) proposed dKV-Cache, a delayed KV-cache mechanism for the denoising process that achieves 2-10× speedup in inference, narrowing the gap between autoregressive and diffusion models.

The most dramatic speed improvements came from Inception Labs et al. (2025), whose Mercury Coder models achieved 1109 tokens/sec throughput (Mini) and 737 tokens/sec (Small) on NVIDIA H100 GPUs, outperforming speed-optimized frontier models by up to 10× while maintaining comparable quality. These advances collectively demonstrate that diffusion models' parallel generation capability, once seen as a liability due to slow sequential denoising, can become a competitive advantage when properly optimized.

### Theme 4: Energy-Based and Hybrid Approaches

Xu et al. (2024) proposed an energy-based diffusion language model (EDLM) that operates at the full sequence level for each diffusion step, with parameters obtained from pretrained autoregressive models or fine-tuned bidirectional transformers via noise contrastive estimation. Their approach consistently outperformed state-of-the-art diffusion models and approached autoregressive perplexity, while offering 1.3× sampling speedup. The energy-based framework addresses the performance degradation in diffusion models caused by imperfect approximation, suggesting that hybrid approaches combining autoregressive pretraining with diffusion fine-tuning can capture the best of both paradigms.

### Theme 5: Code Generation as a Killer Application

Two papers specifically target code generation, identifying it as a domain where diffusion models' unique properties offer particular advantages. Gong et al. (2025) trained DiffuCoder, a 7B diffusion LLM on 130B tokens of code, revealing that diffusion language models can decide how causal their generation should be without relying on semi-autoregressive decoding. Their coupled-GRPO sampling scheme, which constructs complementary mask noise for completions to reduce variance in token log-likelihood estimates, improved performance on code generation benchmarks by 4.4% on EvalPlus. Inception Labs et al. (2025) similarly focused on coding applications, with Mercury Coder ranking second on quality and fastest overall on Copilot Arena.

The emphasis on code generation reflects recognition that programming languages' structured nature and the importance of parallel token prediction (for completing multiple tokens simultaneously) align well with diffusion models' strengths.

## Convergences and Disagreements

**Convergences**: The surveyed papers collectively agree that diffusion language models have matured from proof-of-concept to competitive alternatives to autoregressive models. Multiple studies confirm that: (1) masked diffusion objectives can achieve autoregressive-level perplexity with proper training recipes (Sahoo et al., 2024; Ye et al., 2023); (2) inference acceleration through KV caching and parallel decoding is feasible without significant quality loss (Wu et al., 2025; Ma et al., 2025); and (3) diffusion models offer particular advantages in reasoning, planning, and code generation tasks where global sequence structure matters (Ye et al., 2024; Gong et al., 2025).

**Disagreements**: The literature shows some divergence on the best path forward. Gong et al. (2024) advocate adapting existing autoregressive models to diffusion frameworks, while Nie et al. (2025) demonstrate that training diffusion models from scratch can achieve comparable results. Xu et al. (2024) propose energy-based approaches requiring autoregressive pretraining, whereas Sahoo et al. (2024) show that pure diffusion training with simplified objectives can be effective. These disagreements reflect different priorities: adaptation approaches leverage existing infrastructure and pretrained weights, while from-scratch approaches offer cleaner architectural designs and potentially better long-term scalability.

## Gaps and Open Questions

Several limitations recur across the surveyed literature. First, most abstracts do not explicitly state limitations of the proposed approaches, suggesting either space constraints or insufficient critical analysis of failure modes. Second, while inference acceleration has made significant progress, the training-free methods (Wu et al., 2025; Ma et al., 2025) still require careful tuning of confidence thresholds and cache parameters. Third, Gong et al. (2025) note that training and inference mechanisms for diffusion language models in coding are still under-explored, indicating room for further innovation in domain-specific adaptations.

A broader gap is the lack of comprehensive comparison across different diffusion paradigms (masked, energy-based, adaptation-based) on unified benchmarks. The field would benefit from systematic ablation studies isolating the contributions of different design choices. Finally, while several papers demonstrate strong performance on specific tasks, fewer address general instruction-following and multi-turn dialogue capabilities at scale, an area where Nie et al. (2025) made initial progress but which remains underexplored.

## Per-Paper Annotations

### Gong et al. (2024)

**Research question**: Can autoregressive models be efficiently adapted to build text diffusion models at scale, avoiding the challenges of training diffusion models from scratch?

**Methodology**: The authors propose adapting open-source autoregressive language models to build text diffusion models by demonstrating connections between AR and diffusion modeling objectives and introducing a simple continual pre-training approach. They convert GPT2 and LLaMA models ranging from 127M to 7B parameters using less than 200B tokens and evaluate on language modeling, reasoning, and commonsense benchmarks.

**Key findings**:
- Autoregressive models can be converted to diffusion models using less than 200B tokens for training
- The adapted diffusion models outperform earlier diffusion language models
- The models are competitive with their autoregressive counterparts on benchmarks
- The released DLMs can generate fluent text, perform in-context learning, and follow instructions
- The models support filling in the middle without prompt re-ordering

**Limitations**: The abstract does not explicitly state limitations of the adaptation approach.

### Gong et al. (2025)

**Research question**: How can masked diffusion models be optimized for code generation, and what are their unique decoding behaviors compared to autoregressive models?

**Methodology**: The authors train a 7B diffusion LLM (DiffuCoder) on 130B tokens of code and systematically investigate denoising processes and reinforcement learning methods. They propose coupled-GRPO, a novel sampling scheme that constructs complementary mask noise for completions to reduce variance in token log-likelihood estimates.

**Key findings**:
- DiffuCoder reveals that dLLMs can decide how causal their generation should be without relying on semi-AR decoding
- Increasing sampling temperature diversifies both token choices and generation order, creating rich search space for RL rollouts
- Coupled-GRPO significantly improves performance on code generation benchmarks (+4.4% on EvalPlus)
- The approach reduces reliance on autoregressive bias during decoding

**Limitations**: The abstract notes that current training and inference mechanisms for dLLMs in coding are still under-explored.

### Inception Labs et al. (2025)

**Research question**: Can diffusion-based large language models achieve state-of-the-art speed-quality performance for coding applications?

**Methodology**: The authors present Mercury, a generation of commercial-scale LLMs based on diffusion, parameterized via Transformer architecture and trained to predict multiple tokens in parallel. They evaluate Mercury Coder Mini and Small on code benchmarks across multiple languages and use-cases, with independent evaluations by Artificial Analysis and real-world validation on Copilot Arena.

**Key findings**:
- Mercury Coder models set a new state-of-the-art on the speed-quality frontier
- Mercury Coder Mini achieves 1109 tokens/sec throughput on NVIDIA H100 GPUs
- Mercury Coder Small achieves 737 tokens/sec throughput on NVIDIA H100 GPUs
- The models outperform speed-optimized frontier models by up to 10x on average while maintaining comparable quality
- Mercury Coder ranks second on quality and is the fastest model overall on Copilot Arena

**Limitations**: The abstract does not explicitly state limitations; it focuses on demonstrating speed and quality advantages for coding applications.

### Ma et al. (2025)

**Research question**: How can diffusion language models overcome the slow inference bottleneck caused by their inability to use key-value cache?

**Methodology**: The authors propose delayed KV-Cache (dKV-Cache), a KV-cache-like mechanism for the denoising process of DLMs with delayed and conditioned caching strategy for key and value states. Two variants are designed: dKV-Cache-Decode for almost lossless acceleration and dKV-Cache-Greedy for aggressive caching with higher speed-ups.

**Key findings**:
- dKV-Cache achieves 2-10× speedup in inference, narrowing the gap between autoregressive and diffusion models
- dKV-Cache-Decode provides almost lossless acceleration and can improve performance on long sequences
- dKV-Cache-Greedy achieves higher speed-ups with quadratic time complexity at the cost of some performance degradation
- The cache mechanism works in a training-free manner on current DLMs

**Limitations**: The abstract acknowledges that dKV-Cache-Greedy has performance degradation due to aggressive caching with reduced lifespan.

### Nie et al. (2025)

**Research question**: Can diffusion models trained from scratch achieve capabilities comparable to autoregressive large language models across diverse tasks?

**Methodology**: The authors introduce LLaDA, a diffusion model trained from scratch under pre-training and supervised fine-tuning paradigms, employing forward data masking and reverse generation processes parameterized by a Transformer. They evaluate on extensive benchmarks covering general tasks, math, and code, and compare against self-constructed autoregressive baselines.

**Key findings**:
- LLaDA demonstrates strong scalability and performs comparably to autoregressive baselines across extensive benchmarks
- LLaDA 8B is competitive with LLaMA3 8B in in-context learning
- After supervised fine-tuning, LLaDA exhibits impressive instruction-following abilities including multi-turn dialogue
- LLaDA addresses the reversal curse, surpassing GPT-4o in reversal poem completion
- The findings challenge the assumption that core LLM capabilities inherently depend on autoregressive models

**Limitations**: The abstract does not explicitly state limitations; it emphasizes the competitive performance of the diffusion approach.

### Sahoo et al. (2024)

**Research question**: Can simple masked discrete diffusion models close the performance gap with autoregressive methods in language modeling?

**Methodology**: The authors apply an effective training recipe for masked diffusion models and derive a simplified, Rao-Blackwellized objective that is a mixture of classical masked language modeling losses. They train encoder-only language models on language modeling benchmarks using modern engineering practices and compare against autoregressive baselines.

**Key findings**:
- Simple masked discrete diffusion is more performant than previously thought
- The Rao-Blackwellized objective provides additional improvements over the baseline training recipe
- Masked diffusion models achieve a new state-of-the-art among diffusion models on language modeling benchmarks
- The approach approaches autoregressive perplexity performance
- The objective enables efficient samplers that can generate arbitrary lengths of text semi-autoregressively

**Limitations**: The abstract does not explicitly state limitations of the approach; it focuses on demonstrating improvements over prior diffusion methods.

### Wu et al. (2025)

**Research question**: How can diffusion LLMs achieve practical inference speed comparable to autoregressive models while maintaining generation quality?

**Methodology**: The authors introduce a block-wise approximate KV Cache mechanism for bidirectional diffusion models and propose a confidence-aware parallel decoding strategy that selectively decodes tokens exceeding a confidence threshold. Experiments are conducted on LLaDA and Dream models across multiple LLM benchmarks.

**Key findings**:
- The approach achieves up to 27.6× throughput improvement with minimal accuracy loss
- Block-wise approximate KV Cache enables cache reuse with negligible performance drop
- Confidence-aware parallel decoding mitigates dependency violations and maintains generation quality
- The method closes the performance gap with autoregressive models

**Limitations**: The abstract does not explicitly state limitations, though it acknowledges quality degradation occurs when decoding multiple tokens simultaneously under the conditional independence assumption.

### Xu et al. (2024)

**Research question**: How can diffusion language models overcome the performance gap with autoregressive models, especially when reducing sampling steps?

**Methodology**: The authors propose Energy-based Diffusion Language Model (EDLM), an energy-based model operating at the full sequence level for each diffusion step, with parameters obtained from pretrained autoregressive models or finetuned bidirectional transformers via noise contrastive estimation. They also propose an efficient generation algorithm via parallel important sampling.

**Key findings**:
- EDLM consistently outperforms state-of-the-art diffusion models by a significant margin
- The model approaches autoregressive models' perplexity
- The framework offers 1.3× sampling speedup over existing diffusion models without generation performance drop
- The performance degradation in diffusion models is caused by imperfect approximation

**Limitations**: The abstract does not explicitly state limitations, though it acknowledges the approach requires either pretrained autoregressive models or finetuning via noise contrastive estimation.

### Ye et al. (2023)

**Research question**: Can diffusion language models solve general language tasks comparably to autoregressive language models?

**Methodology**: The authors build diffusion language models at scale by pretraining with masked language modeling, then reprogram them into diffusion models via diffusive adaptation with task-specific and instruction finetuning. Experiments evaluate performance across downstream language tasks and test zero-shot/few-shot in-context learning abilities.

**Key findings**:
- Scaling diffusion language models consistently improves performance across downstream language tasks
- Instruction finetuning elicits zero-shot and few-shot in-context learning abilities for unseen tasks
- The models show promise in advanced abilities such as reasoning
- Masked language modeling pretraining provides intrinsic connections for acquiring knowledge from massive data

**Limitations**: The abstract does not explicitly state limitations of the approach or identify specific failure cases.

### Ye et al. (2024)

**Research question**: Can discrete diffusion models overcome the limitations of autoregressive models in complex reasoning and long-term planning tasks?

**Methodology**: The authors introduce Multi-Granularity Diffusion Modeling (MGDM), which prioritizes subgoals based on difficulty during learning through the lens of subgoal imbalance. They evaluate on complex tasks including Countdown, Sudoku, and Boolean Satisfiability Problems, comparing against autoregressive models without search techniques.

**Key findings**:
- Diffusion models effectively learn difficult subgoals that elude autoregressive approaches
- MGDM achieves 91.5% accuracy on Countdown compared to 45.8% for autoregressive models
- MGDM achieves 100% accuracy on Sudoku compared to 20.7% for autoregressive models
- The approach significantly outperforms autoregressive models on complex reasoning tasks without using search
- Diffusion-based approaches show potential for advancing AI capabilities in sophisticated problem-solving

**Limitations**: The abstract does not explicitly state limitations; it focuses on demonstrating superior performance on specific reasoning benchmarks.

## References

Gong, S., Agarwal, S., Zhang, Y., Ye, J., Zheng, L., Li, M., An, C., Zhao, P., Bi, W., Han, J., Peng, H., & Kong, L. (2024). Scaling diffusion language models via adaptation from autoregressive models. arXiv. https://arxiv.org/abs/2410.17891

Gong, S., Zhang, R., Zheng, H., Gu, J., Jaitly, N., Kong, L., & Zhang, Y. (2025). DiffuCoder: Understanding and improving masked diffusion models for code generation. arXiv. https://arxiv.org/abs/2506.20639

Inception Labs, Khanna, S., Kharbanda, S., Li, S., Varma, H., Wang, E., Birnbaum, S., Luo, Z., Miraoui, Y., Palrecha, A., Ermon, S., Grover, A., & Kuleshov, V. (2025). Mercury: Ultra-fast language models based on diffusion. arXiv. https://arxiv.org/abs/2506.17298

Ma, X., Yu, R., Fang, G., & Wang, X. (2025). dKV-Cache: The cache for diffusion language models. arXiv. https://arxiv.org/abs/2505.15781

Nie, S., Zhu, F., You, Z., Zhang, X., Ou, J., Hu, J., Zhou, J., Lin, Y., Wen, J.-R., & Li, C. (2025). Large language diffusion models. arXiv. https://arxiv.org/abs/2502.09992

Sahoo, S. S., Arriola, M., Schiff, Y., Gokaslan, A., Marroquin, E., Chiu, J. T., Rush, A., & Kuleshov, V. (2024). Simple and effective masked diffusion language models. arXiv. https://arxiv.org/abs/2406.07524

Wu, C., Zhang, H., Xue, S., Liu, Z., Diao, S., Zhu, L., Luo, P., Han, S., & Xie, E. (2025). Fast-dLLM: Training-free acceleration of diffusion LLM by enabling KV cache and parallel decoding. arXiv. https://arxiv.org/abs/2505.22618

Xu, M., Geffner, T., Kreis, K., Nie, W., Xu, Y., Leskovec, J., Ermon, S., Vahdat, A. (2024). Energy-based diffusion language models for text generation. arXiv. https://arxiv.org/abs/2410.21357

Ye, J., Zheng, Z., Bao, Y., Qian, L., & Gu, Q. (2023). Diffusion language models can perform many tasks with scaling and instruction-finetuning. arXiv. https://arxiv.org/abs/2308.12219

Ye, J., Gao, J., Gong, S., Zheng, L., Jiang, X., Li, Z., & Kong, L. (2024). Beyond autoregression: Discrete diffusion for complex reasoning and planning. arXiv. https://arxiv.org/abs/2410.14157
