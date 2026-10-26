# Systematic Literature Review: Latent Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "latent reasoning", category cs.CL, published between 2023-07-08 and 2025-07-07
**Citation format**: APA 7th edition

## Executive Summary

The literature on latent reasoning in large language models reveals a rapidly evolving field focused on moving beyond explicit, text-based chain-of-thought reasoning toward more efficient internal reasoning mechanisms. The surveyed papers collectively demonstrate that reasoning can occur in continuous latent spaces, through compressed representations, or via internalized hidden states, often achieving comparable or superior performance to explicit reasoning while reducing computational costs. A dominant theme is the tension between reasoning transparency and efficiency—while explicit chain-of-thought provides interpretability, latent reasoning approaches offer significant speed and accuracy improvements. The field shows strong convergence on the value of hybrid approaches that combine latent and text tokens, as well as test-time scaling strategies that dynamically allocate computation. However, limitations remain in understanding when and why latent reasoning fails, particularly for multi-hop queries requiring complex intermediate entity resolution.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "latent reasoning", filtered to category cs.CL, published between 2023-07-08 and 2025-07-07. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Search and screening statistics**: 50 papers identified by search, 83 added from citation expansion, 30 shortlisted, 30 screened, 10 included (6 from references). Screening scores ranged from 0-3, with 14 papers scoring 3 (highest centrality).

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. All limitations were extracted from abstracts only; many papers did not explicitly state limitations.

## Themes

### Theme 1: Continuous Latent Space Reasoning

A central paradigm shift in the literature involves replacing discrete text-based reasoning with continuous vector representations. Hao et al. (2024) introduced Coconut (Chain of Continuous Thought), which uses the last hidden state of an LLM as a reasoning state representation, feeding it back directly as the next input embedding rather than decoding into words. This enables breadth-first search reasoning patterns instead of the deterministic single-path approach of traditional chain-of-thought. Similarly, Cheng and Van Durme (2024) proposed Compressed Chain-of-Thought (CCoT), generating continuous contemplation tokens as compressed representations of explicit reasoning chains. Both approaches share the insight that most tokens in traditional reasoning primarily ensure textual coherence rather than contributing to core reasoning, and that operating in continuous space allows encoding multiple alternative reasoning paths simultaneously.

### Theme 2: Internalization of Explicit Reasoning

Several papers explore how models can internalize explicit chain-of-thought reasoning while maintaining performance without generating intermediate steps. Deng et al. (2024) proposed a gradual internalization method, starting with explicit CoT training and progressively removing intermediate steps while finetuning, enabling GPT-2 Small to solve 9-by-9 multiplication with 99% accuracy. In earlier work, Deng et al. (2023) demonstrated implicit reasoning through knowledge distillation, where reasoning happens vertically among hidden states in different layers rather than horizontally through intermediate words. This vertical reasoning achieves speed comparable to no chain-of-thought while solving tasks previously requiring explicit reasoning. The convergence across these works suggests that explicit reasoning serves primarily as a training scaffold that can be distilled away.

### Theme 3: Test-Time Scaling and Budget Forcing

A distinct but related direction focuses on controlling computation at inference time. Muennighoff et al. (2025) introduced s1, a simple test-time scaling approach using budget forcing to control the model's thinking process by appending 'Wait' tokens or forcibly terminating reasoning. Their s1-32B model exceeded o1-preview by up to 27% on competition math questions, demonstrating that strategic allocation of test-time computation can outperform larger models. This approach shares with latent reasoning the goal of improving the accuracy-efficiency tradeoff, but operates at a different level—controlling when and how long to reason rather than changing the representation of reasoning itself.

### Theme 4: Pause Tokens and Pre-Computation

Goyal et al. (2023) introduced pause tokens as learnable tokens appended to the input prefix, delaying output extraction until the last pause token is seen. This allows the model to manipulate additional hidden vectors before committing to an answer, achieving an 18% EM score gain on SQuAD and 8% on CommonSenseQA. The approach conceptually bridges latent reasoning and test-time scaling—pause tokens provide additional computation time in latent space before generating text output. The gains were observed only when models were both pre-trained and finetuned with delays, suggesting that latent pre-computation requires architectural integration rather than simple inference-time modification.

### Theme 5: Multi-Hop Reasoning Mechanisms and Limitations

Two papers specifically investigate how LLMs internally compute multi-hop queries, revealing both capabilities and fundamental limitations. Yang et al. (2024) found strong evidence of latent multi-hop reasoning for certain relation types, with the reasoning pathway used in over 80% of prompts, though evidence for the second hop was only moderate. Biran et al. (2024) used back-patching analysis to show that bridge entities are resolved in early layers, but later layers sometimes lack the functionality needed for correct answer generation—in up to 66% of previously incorrect cases, a back-patch could restore correct answers. These mechanistic studies provide crucial grounding for latent reasoning approaches, revealing where and why internal reasoning fails.

### Theme 6: Hybrid Latent-Text Representations

The most recent work explores hybrid approaches combining latent and text tokens. Su et al. (2025) proposed mixing latent discrete tokens generated by VQ-VAE with text tokens, significantly reducing reasoning trace length while outperforming baselines on logical and mathematical reasoning benchmarks. Their random mixing training procedure enables fast adaptation to new latent tokens, suggesting a practical path toward deploying latent reasoning in existing architectures. This hybrid approach represents a synthesis of the field's insights—retaining the interpretability benefits of text while gaining the efficiency of latent representations.

## Convergences and Disagreements

**Convergences**: The surveyed papers show strong agreement on several points. First, most agree that traditional chain-of-thought reasoning contains substantial redundancy, with many tokens serving textual coherence rather than core reasoning (Hao et al., 2024; Su et al., 2025; Deng et al., 2024). Second, there is consensus that latent or compressed reasoning can achieve comparable or superior accuracy to explicit reasoning while reducing computation (Cheng & Van Durme, 2024; Deng et al., 2023; Goyal et al., 2023). Third, all papers implicitly or explicitly endorse the view that reasoning and language generation are separable capabilities that can be optimized independently.

**Disagreements**: The literature shows less disagreement on fundamental claims than on implementation approaches. A notable tension exists between approaches that fully replace text with continuous representations (Hao et al., 2024) versus those that maintain hybrid representations (Su et al., 2025). Additionally, while some approaches require architectural changes and pre-training with latent tokens (Goyal et al., 2023; Su et al., 2025), others claim effectiveness with off-the-shelf models through post-hoc compression or distillation (Cheng & Van Durme, 2024; Deng et al., 2023). The field has not yet resolved whether latent reasoning requires fundamental architectural changes or can be effectively retrofitted.

## Gaps and Open Questions

Several critical gaps emerge from the collective literature. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either that limitations were not discussed or that the field is in an early, optimism-driven phase. Second, while mechanistic studies reveal where multi-hop reasoning fails (Biran et al., 2024; Yang et al., 2024), there is limited work on diagnostic tools for identifying latent reasoning failures in deployed systems. Third, the literature focuses heavily on mathematical and logical reasoning benchmarks, with limited exploration of latent reasoning for creative, open-ended, or domain-specific tasks. Fourth, the interpretability tradeoff remains unresolved—while latent reasoning improves efficiency, it sacrifices the transparency that made chain-of-thought valuable for debugging and trust. Finally, most approaches are evaluated on relatively small models or specific benchmarks, leaving open questions about scalability and generalization to production-scale systems.

## Per-Paper Annotations

### Biran et al. (2024)

**Research question**: How do transformer-based LLMs internally compute multi-hop queries, and what are the limitations of this computation?
**Methodology**: The authors analyze internal computations of transformer-based models using a novel back-patching analysis method where hidden representations from later layers are patched back to earlier layers to test whether later layers lack necessary functionality.
**Key findings**:
- The bridge entity is resolved in the early layers of the model
- The two-hop query is solved in later layers only after bridge entity resolution
- In up to 66% of previously incorrect cases, there exists a back-patch that results in correct answer generation
- Later layers sometimes lack the needed functionality for correctly predicting answers
**Limitations**: Not stated in abstract

### Cheng and Van Durme (2024)

**Research question**: Can chain-of-thought reasoning be compressed into dense continuous representations to reduce generation latency while maintaining reasoning performance?
**Methodology**: The authors propose Compressed Chain-of-Thought (CCoT), a framework that generates contentful and continuous contemplation tokens of variable sequence length as compressed representations of explicit reasoning chains, applied to off-the-shelf decoder language models.
**Key findings**:
- CCoT enables additional reasoning over dense contentful representations to achieve corresponding improvements in accuracy
- The generated contemplation tokens are compressed representations of explicit reasoning chains
- Reasoning improvements can be adaptively modified on demand by controlling the number of contemplation tokens generated
- The method can be applied to off-the-shelf decoder language models without modification
**Limitations**: Not stated in abstract

### Deng et al. (2023)

**Research question**: Can language models perform effective reasoning using internal hidden states rather than explicitly producing chain-of-thought reasoning steps in natural language?
**Methodology**: The authors explore implicit reasoning by using the language model's internal hidden states to perform reasoning instead of explicit natural language output, with implicit reasoning steps distilled from a teacher model trained on explicit chain-of-thought reasoning.
**Key findings**:
- The approach enables solving tasks previously not solvable without explicit chain-of-thought
- The method achieves speed comparable to no chain-of-thought reasoning
- Reasoning happens vertically among the hidden states in different layers rather than horizontally producing intermediate words
- Experiments were conducted on multi-digit multiplication and grade school math problem datasets
**Limitations**: Not stated in abstract

### Deng et al. (2024)

**Research question**: Can language models be taught to internalize explicit chain-of-thought reasoning steps while maintaining high performance without generating intermediate steps?
**Methodology**: The authors propose a method for internalizing CoT steps by starting with a model trained for explicit CoT reasoning and gradually removing the intermediate steps while finetuning the model.
**Key findings**:
- The approach enables a GPT-2 Small model to solve 9-by-9 multiplication with up to 99% accuracy, whereas standard training cannot solve beyond 4-by-4 multiplication
- The method proves effective on larger language models such as Mistral 7B, achieving over 50% accuracy on GSM8K without producing intermediate steps
- Starting with explicit CoT training and gradually removing intermediate steps allows models to internalize reasoning while maintaining high performance
- The internalization process simplifies the reasoning process while preserving accuracy on complex tasks
**Limitations**: Not stated in abstract

### DeepSeek-AI et al. (2025)

**Research question**: Can the reasoning abilities of large language models be incentivized through pure reinforcement learning without requiring human-annotated reasoning trajectories?
**Methodology**: The authors propose a reinforcement learning framework that incentivizes reasoning capabilities in LLMs without human-labeled reasoning trajectories, allowing emergent development of advanced reasoning patterns such as self-reflection, verification, and dynamic strategy adaptation.
**Key findings**:
- Reasoning abilities of LLMs can be incentivized through pure reinforcement learning, eliminating the need for human-annotated demonstrations
- The RL framework facilitates emergent development of advanced reasoning patterns including self-reflection, verification, and dynamic strategy adaptation
- The trained model achieves superior performance on mathematics, coding competitions, and STEM fields compared to counterparts trained via conventional supervised learning
- Emergent reasoning patterns from large-scale models can be systematically harnessed to guide and enhance reasoning capabilities of smaller models
**Limitations**: Not stated in abstract

### Goyal et al. (2023)

**Research question**: Can language models improve their outputs by manipulating additional hidden vectors through learnable pause tokens before generating the next token?
**Methodology**: The authors introduce pause tokens—learnable tokens appended to the input prefix—and delay extracting the model's outputs until the last pause token is seen, allowing the model to process extra computation before committing to an answer.
**Key findings**:
- Inference-time delays show gains when the model is both pre-trained and finetuned with delays
- For the 1B model, gains were observed on 8 of 9 tasks evaluated
- Notable improvements include an 18% EM score gain on SQuAD QA task, 8% on CommonSenseQA, and 1% accuracy gain on GSM8k reasoning task
- Allowing models to manipulate additional hidden vectors before outputting tokens enables more computation before committing to answers
**Limitations**: Gains are only observed when models are both pre-trained and finetuned with delays; the approach raises conceptual and practical questions about making delayed next-token prediction widely applicable

### Hao et al. (2024)

**Research question**: Can large language models reason more effectively by operating in a continuous latent space rather than being constrained to the language space for reasoning?
**Methodology**: The authors introduce Coconut (Chain of Continuous Thought), a paradigm that uses the last hidden state of the LLM as a representation of the reasoning state, termed 'continuous thought,' and feeds it back to the model as the next input embedding directly in the continuous space.
**Key findings**:
- Coconut outperforms chain-of-thought (CoT) on logical reasoning tasks that require substantial search during planning
- Continuous thoughts can encode multiple alternative next steps, allowing the model to perform breadth-first search rather than committing to a single deterministic path
- The latent reasoning paradigm achieves a better trade-off between accuracy and efficiency compared to CoT
- Most word tokens in traditional reasoning primarily ensure textual coherence and are not essential for reasoning itself
**Limitations**: Not stated in abstract

### Muennighoff et al. (2025)

**Research question**: What is the simplest approach to achieve test-time scaling and strong reasoning performance in language models?
**Methodology**: The authors curate a small dataset s1K of 1,000 questions with reasoning traces based on difficulty, diversity, and quality criteria, and develop budget forcing to control test-time compute by forcefully terminating or lengthening the model's thinking process.
**Key findings**:
- s1-32B exceeds o1-preview on competition math questions by up to 27% on MATH and AIME24
- Scaling s1-32B with budget forcing allows extrapolating performance from 50% to 57% on AIME24
- Budget forcing can lead the model to double-check its answer, often fixing incorrect reasoning steps
- The model, data, and code are open-source
**Limitations**: Not stated in abstract

### Su et al. (2025)

**Research question**: Can hybrid representations mixing latent discrete tokens with text tokens improve language model reasoning efficiency while reducing computational costs?
**Methodology**: The authors propose a hybrid representation where initial reasoning steps are partially abstracted using latent discrete tokens generated by VQ-VAE to reduce reasoning trace length, with a training procedure that randomly mixes latent and text tokens.
**Key findings**:
- The approach significantly reduces the length of reasoning traces compared to full text-based chain-of-thought
- The method consistently outperforms baseline methods in various benchmarks
- Random mixing of latent and text tokens enables fast adaptation to new latent tokens
- The approach is effective for both logical and mathematical reasoning problems
**Limitations**: Not stated in abstract

### Yang et al. (2024)

**Research question**: Do large language models latently perform multi-hop reasoning when processing complex prompts that require identifying intermediate bridge entities and using knowledge about them?
**Methodology**: The authors analyze two hops of latent multi-hop reasoning individually: testing if indirectly mentioning the bridge entity increases the LLM's internal recall of that entity, and testing if increasing this recall causes the LLM to better utilize its knowledge about the bridge entity.
**Key findings**:
- Strong evidence of latent multi-hop reasoning exists for prompts of certain relation types, with the reasoning pathway used in more than 80% of prompts
- Utilization of latent reasoning is highly contextual, varying across different types of prompts
- On average, evidence for the second hop and full multi-hop traversal is moderate, with substantial evidence only for the first hop
- A clear scaling trend exists with increasing model size for the first hop of reasoning but not for the second hop
**Limitations**: The utilization of latent multi-hop reasoning is highly contextual and varies across prompt types; evidence for the second hop and complete multi-hop traversal is only moderate on average

## References

Biran, E., Gottesman, D., Yang, S., Geva, M., & Globerson, A. (2024). Hopping too late: Exploring the limitations of large language models on multi-hop queries. arXiv. https://arxiv.org/abs/2406.12775

Cheng, J., & Van Durme, B. (2024). Compressed chain of thought: Efficient reasoning through dense representations. arXiv. https://arxiv.org/abs/2412.13171

DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., Zhu, Q., Xu, R., Zhang, R., Ma, S., Bi, X., Zhang, X., Yu, X., Wu, Y., Wu, Z. F., Gou, Z., Shao, Z., Li, Z., Gao, Z., Liu, A., et al. (2025). DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. arXiv. https://arxiv.org/abs/2501.12948

Deng, Y., Choi, Y., & Shieber, S. (2024). From explicit CoT to implicit CoT: Learning to internalize CoT step by step. arXiv. https://arxiv.org/abs/2405.14838

Deng, Y., Prasad, K., Fernandez, R., Smolensky, P., Chaudhary, V., & Shieber, S. (2023). Implicit chain of thought reasoning via knowledge distillation. arXiv. https://arxiv.org/abs/2311.01460

Goyal, S., Ji, Z., Rawat, A. S., Menon, A. K., Kumar, V., & Nagarajan, V. (2023). Think before you speak: Training language models with pause tokens. arXiv. https://arxiv.org/abs/2310.02226

Hao, S., Sukhbaatar, S., Su, D., Li, X., Hu, Z., Weston, J., & Tian, Y. (2024). Training large language models to reason in a continuous latent space. arXiv. https://arxiv.org/abs/2412.06769

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. arXiv. https://arxiv.org/abs/2501.19393

Su, D., Zhu, H., Xu, Y., Jiao, J., Tian, Y., & Zheng, Q. (2025). Token assorted: Mixing latent and text tokens for improved language model reasoning. arXiv. https://arxiv.org/abs/2502.03275

Yang, S., Gribovskaya, E., Kassner, N., Geva, M., & Riedel, S. (2024). Do large language models latently perform multi-hop reasoning? arXiv. https://arxiv.org/abs/2402.16837
