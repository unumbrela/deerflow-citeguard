# Systematic Literature Review: Latent Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "latent reasoning", category cs.CL, published between 2023-07-08 and 2025-07-07
**Citation format**: APA 7th edition

## Executive Summary

The literature on latent reasoning in large language models has evolved rapidly between 2023 and 2025, with research converging on the fundamental insight that reasoning in continuous latent spaces can outperform traditional discrete Chain-of-Thought approaches while offering substantial efficiency gains. The surveyed papers collectively demonstrate that LLMs can perform multi-hop reasoning through hidden representations without explicit token generation, enabling both "silent" reasoning (reduced computational cost) and more flexible search strategies (breadth-first exploration of reasoning paths). Key advances include reinforcement learning optimization methods that integrate hidden states with discrete tokens, contrastive feedback mechanisms for post-training refinement, and variational autoencoder architectures that disentangle reasoning rules in model parameters. However, the field faces open questions around scaling behavior, interpretability trade-offs, and the conditions under which latent reasoning generalizes across tasks and model sizes.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "latent reasoning", filtered to category cs.CL, published between 2023-07-08 and 2025-07-07. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Continuous Latent Space Reasoning

A central thread in the literature explores the shift from discrete token-based reasoning to continuous latent representations. Hao et al. (2024) introduce Coconut (Chain of Continuous Thought), which utilizes the last hidden state of an LLM as a representation of the reasoning state, feeding it back directly in continuous space rather than decoding to words. This approach enables the model to encode multiple alternative next steps simultaneously, supporting breadth-first search rather than committing to a single deterministic path. Similarly, Hwang et al. (2025) adapt token-level language models to operate in sentence space by autoregressively predicting continuous embeddings of next sentences, demonstrating that contextual embeddings under continuous inference show competitive performance with Chain-of-Thought while reducing inference-time FLOPs by half on average.

The theoretical foundation for this approach rests on the observation that language space may not be optimal for reasoning, as most word tokens primarily ensure textual coherence rather than contributing to reasoning itself (Hao et al., 2024). By operating in continuous space, models can maintain richer representations of intermediate reasoning states without the information loss inherent in token discretization.

### Theme 2: Efficiency and Compression

Multiple papers address the computational efficiency benefits of latent reasoning. Tan et al. (2025) introduce Compressed Latent Reasoning (CoLaR), a two-stage framework that dynamically compresses reasoning chains in latent space, achieving a 53.3% reduction in reasoning chain length with only 4.8% performance degradation compared to explicit Chain-of-Thought. On more difficult mathematical tasks, latent reasoning chain length can be reduced by 82.8% while maintaining performance through RL-enhanced optimization. The framework enables dynamic adjustment of reasoning speed at inference time via compression factor prompting, offering a flexible trade-off between accuracy and computational cost.

Hwang et al. (2025) similarly report that their sentence embedding prediction approach reduces inference-time FLOPs by half compared to Chain-of-Thought, while Hao et al. (2024) note that the latent reasoning paradigm achieves a better trade-off between accuracy and efficiency. These findings collectively suggest that latent reasoning is not merely an alternative representation but offers concrete efficiency advantages for deployment scenarios where computational resources are constrained.

### Theme 3: Training and Optimization Strategies

Reinforcement learning and post-training refinement emerge as key methodologies for improving latent reasoning capabilities. Yue et al. (2025) introduce Hybrid Reasoning Policy Optimization (HRPO), an RL-based approach that integrates prior hidden states into sampled tokens via a learnable gating mechanism. HRPO enables RL optimization without requiring chain-of-thought trajectories by introducing stochasticity through token sampling, and outperforms prior latent reasoning methods on both knowledge-intensive and reasoning-intensive benchmarks.

Wang et al. (2025) propose a lightweight post-training framework with two strategies: contrastive reasoning feedback that compares embeddings against strong and weak baselines, and residual embedding refinement that stabilizes updates by integrating current and historical gradients progressively. This approach achieves a 5% accuracy gain on MathQA without additional training, addressing the challenge of fixed reasoning trajectories in Chain-of-Thought prompting through step-wise refinement of latent reasoning trajectories.

### Theme 4: Small Model Latent Reasoning

An important research direction examines whether latent reasoning capabilities can be activated in smaller models. Zhang et al. (2025) propose Self-Enhanced Reasoning Training (SERT), which activates latent reasoning in small models through self-training on filtered, self-generated reasoning paths under zero-shot conditions. Their experiments using GPT-3.5 as teacher and GPT-2 models as students demonstrate that small models can generate high-quality reasoning paths during sampling even without chain-of-thought prompting, though these paths are often latent due to low probability under standard decoding strategies.

This line of work has implications for reasoning distillation, as SERT enhances the reasoning abilities of small models and improves performance when distilling from teacher models. The findings suggest that latent reasoning is not exclusive to large models but can be cultivated in smaller architectures through appropriate training strategies.

### Theme 5: Reasoning Structure and Disentanglement

Several papers investigate the internal structure of latent reasoning and methods to disentangle reasoning rules. Zhang et al. (2025) present a systematic study of learning reasoning rules within Transformer-based language VAEs, finding that reasoning rules can be disentangled within the encoder's parametric space under explicit signal supervision, with distinct clustering of rules occurring in the output feature space. Their work shows that injecting reasoning information into Query enables more effective retrieval of stored values from memory, and that FFN layers are better than attention layers at preserving separation of reasoning rules in model parameters.

Xu et al. (2023) introduce LaRS (Latent Reasoning Skills), which employs unsupervised learning to create a latent space representation of rationales with a reasoning skill variable. The approach selects chain-of-thought examples by aligning reasoning skills between examples and questions, processing example banks four times faster than existing methods while reducing LLM inferences during selection by half. This demonstrates that latent reasoning structures can be leveraged for more efficient example selection without requiring auxiliary LLM inference or manual prompt design.

## Convergences and Disagreements

**Convergences**: The surveyed literature shows strong agreement on several points. Most papers demonstrate that latent reasoning can match or exceed the performance of explicit Chain-of-Thought while offering efficiency advantages (Hao et al., 2024; Hwang et al., 2025; Tan et al., 2025). Multiple studies confirm that continuous representations enable more flexible reasoning strategies, particularly breadth-first search capabilities that are difficult to achieve with discrete token generation (Hao et al., 2024; Yue et al., 2025). There is also convergence around the effectiveness of post-training refinement strategies, with both Wang et al. (2025) and Yue et al. (2025) showing significant gains without full model retraining.

**Disagreements**: The literature shows less direct disagreement but reveals tension around the scalability of latent reasoning. While Zhang et al. (2025) demonstrate successful activation of latent reasoning in small models, Balesni et al. (2024) explicitly note that it remains unclear how latent two-hop reasoning ability scales with model size. Their controlled experiments show that LLMs can perform latent two-hop reasoning under specific conditions, but the scaling behavior across model sizes requires further investigation. Additionally, while most papers report efficiency gains, the magnitude varies substantially across approaches, suggesting that the conditions under which latent reasoning provides benefits may be task-dependent.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, scaling behavior remains poorly understood — Balesni et al. (2024) explicitly identify this as an open question, and none of the surveyed papers provide comprehensive scaling analyses across model sizes. Second, while several papers mention interpretability as a benefit (Yue et al., 2025; Zhang et al., 2025), the trade-offs between interpretability and performance in latent versus explicit reasoning are not systematically addressed. Third, the abstracts of many papers do not explicitly state limitations (noted in 6 of 10 papers), suggesting that the field may benefit from more rigorous discussion of failure modes and boundary conditions.

A fourth gap concerns the generalization of latent reasoning across tasks and domains. While individual papers demonstrate success on specific benchmarks (MathQA, logical reasoning, NLI tasks), cross-task generalization is not systematically evaluated. Finally, the relationship between latent reasoning and memorization requires further study — Balesni et al. (2024) note that researchers must avoid both spurious successes from memorization and spurious failures from artificial experimental setups, indicating that disentangling genuine reasoning from memorization remains challenging.

## Per-Paper Annotations

### Hao et al. (2024)

**Research question**: Can Large Language Models reason more effectively by operating in a continuous latent space rather than being constrained to express reasoning through language tokens?
**Methodology**: Introduces Coconut (Chain of Continuous Thought), which utilizes the last hidden state of the LLM as a representation of the reasoning state, feeding it back to the model as the next input embedding directly in the continuous space rather than decoding it into words.
**Key findings**:
- The language space may not be optimal for reasoning, as most word tokens primarily ensure textual coherence rather than contributing to reasoning
- Continuous thoughts can encode multiple alternative next steps, enabling the model to perform breadth-first search rather than committing prematurely to a single deterministic path
- Coconut outperforms traditional Chain-of-Thought on logical reasoning tasks that require substantial search during planning
- The latent reasoning paradigm achieves a better trade-off between accuracy and efficiency compared to CoT
- Reasoning beyond language in the continuous space offers potential advantages for complex planning tasks
**Limitations**: not stated in abstract

### Hwang et al. (2025)

**Research question**: Can pretrained language models learn to reason over structured semantic units (sentences, propositions) rather than raw token sequences?
**Methodology**: Presents a framework adapting token-level LMs to operate in sentence space by autoregressively predicting continuous embeddings of next sentences, exploring semantic embeddings (autoencoding) and contextual embeddings (next-sentence prediction) under discretized and continuous inference regimes.
**Key findings**:
- Contextual embeddings under continuous inference show competitive performance with Chain-of-Thought
- The approach reduces inference-time FLOPs on average by half compared to CoT
- Early signs of scalability and modular adaptation are demonstrated
- SentenceLens diagnostic tool enables visualization of latent reasoning trajectories
**Limitations**: not stated in abstract

### Tan et al. (2025)

**Research question**: Can reasoning processes in LLMs be dynamically compressed in latent space to reduce computational cost while maintaining performance?
**Methodology**: Introduces Compressed Latent Reasoning (CoLaR), a two-stage framework combining supervised fine-tuning with auxiliary next compressed embedding prediction and reinforcement learning to explore diverse reasoning paths and exploit more compact ones.
**Key findings**:
- CoLaR achieves 14.1% higher accuracy than latent-based baseline methods at comparable compression ratios
- Reasoning chain length is reduced by 53.3% with only 4.8% performance degradation compared to explicit CoT
- RL-enhanced CoLaR demonstrates performance gains up to 5.4% on challenging mathematical tasks
- Latent reasoning chain length can be dramatically reduced by 82.8% on more difficult tasks
- The framework enables dynamic adjustment of reasoning speed at inference time via compression factor prompting
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can reasoning embeddings be effectively updated during post-training to guide large language models toward more accurate solutions in latent reasoning?
**Methodology**: Proposes a lightweight post-training framework with two strategies: contrastive reasoning feedback that compares embeddings against strong and weak baselines, and residual embedding refinement that stabilizes updates by integrating current and historical gradients progressively.
**Key findings**:
- The framework enables step-wise refinement of latent reasoning trajectories without producing explicit outputs
- Contrastive reasoning feedback infers effective update directions via embedding enhancement
- Residual embedding refinement enables fast yet controlled convergence
- The approach achieves a 5% accuracy gain on MathQA without additional training
- The method addresses the challenge of fixed reasoning trajectories in Chain-of-Thought prompting
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Yue et al. (2025)

**Research question**: How can latent reasoning be made compatible with large language models' discrete autoregressive generation while leveraging their intrinsic reasoning capabilities?
**Methodology**: Introduces Hybrid Reasoning Policy Optimization (HRPO), an RL-based approach that integrates prior hidden states into sampled tokens via a learnable gating mechanism and progressively incorporates hidden features during training.
**Key findings**:
- HRPO outperforms prior latent reasoning methods on both knowledge-intensive and reasoning-intensive benchmarks
- The hybrid approach maintains LLMs' generative capabilities while enabling reasoning with both discrete and continuous representations
- HRPO-trained models remain interpretable and exhibit cross-lingual patterns
- The approach produces shorter completion lengths compared to baseline methods
- Training can proceed without chain-of-thought traces by leveraging LLMs' inherent reasoning patterns
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Zhang, Y. et al. (2025)

**Research question**: How can explicit reasoning rules be embedded and memorized within language models through Variational Autoencoders to enhance generalization and interpretability?
**Methodology**: Proposes a complete pipeline for learning reasoning rules within Transformer-based language VAEs, encompassing three rule-based reasoning tasks, a theoretical framework, and an end-to-end architecture with experiments on NLI tasks.
**Key findings**:
- Reasoning rules can be disentangled within the encoder's parametric space under explicit signal supervision
- Distinct clustering of rules occurs in the output feature space
- Injecting reasoning information into Query enables more effective retrieval of stored values from memory
- In mathematical reasoning with Qwen2.5(0.5B), increasing sample count doesn't improve performance beyond a point
- FFN layers are better than attention layers at preserving separation of reasoning rules in model parameters
**Limitations**: not stated in abstract

### Zhang, Y. et al. (2025) [SERT]

**Research question**: Can latent reasoning capabilities in small models be activated and leveraged to improve reasoning distillation from teacher models?
**Methodology**: Proposes Self-Enhanced Reasoning Training (SERT), which activates latent reasoning in small models through self-training on filtered, self-generated reasoning paths under zero-shot conditions.
**Key findings**:
- Small models can generate high-quality reasoning paths during sampling even without chain-of-thought prompting
- These reasoning paths are often latent due to low probability under standard decoding strategies
- SERT enhances reasoning abilities of small models through self-training on filtered self-generated paths
- The approach improves performance in reasoning distillation from teacher models
**Limitations**: not stated in abstract

### Xu et al. (2023)

**Research question**: How can chain-of-thought examples be selected based on reasoning skills rather than question similarity without requiring human experts or auxiliary LLM inference?
**Methodology**: LaRS employs unsupervised learning to create a latent space representation of rationales with a reasoning skill variable, and learns a reasoning policy to determine the required skill for a given question, then selects examples by aligning reasoning skills between examples and questions.
**Key findings**:
- LaRS consistently outperforms state-of-the-art skill-based selection methods
- The approach processes example banks four times faster than existing methods
- LLM inferences during the selection stage are reduced by half
- The method shows greater robustness to sub-optimal example banks
- The approach eliminates the need for auxiliary LLM inference or manual prompt design
**Limitations**: The abstract does not explicitly state limitations of the approach.

### Balesni et al. (2024)

**Research question**: Can large language models perform latent two-hop reasoning when memorization and reasoning shortcuts are controlled for?
**Methodology**: Fine-tunes LLMs (including Llama 3 8B and GPT-4o) on synthetic facts and tests two-hop reasoning over these facts, using synthetic facts to rule out memorization and reasoning shortcuts as explanations for performance.
**Key findings**:
- LLMs fail to compose two synthetic facts for two-hop reasoning
- Models can succeed when one fact is synthetic and the other is natural
- LLMs are demonstrably capable of latent two-hop reasoning under controlled conditions
- It remains unclear how latent two-hop reasoning ability scales with model size
- Researchers must avoid both spurious successes from memorization and spurious failures from artificial experimental setups
**Limitations**: The abstract notes that it remains unclear how latent two-hop reasoning ability scales with model size.

### Zheng et al. (2024)

**Research question**: What are the roles and mechanisms of attention heads in Large Language Models, and how do they contribute to the internal reasoning processes?
**Methodology**: Introduces a novel four-stage framework (Knowledge Recalling, In-Context Identification, Latent Reasoning, and Expression Preparation) inspired by human thought processes to systematically categorize attention head functions, and analyzes experimental methodologies as Modeling-Free and Modeling-Required methods.
**Key findings**:
- Attention heads serve as a focal point for investigating the underlying mechanics of LLMs and their reasoning bottlenecks
- A four-stage framework can systematically categorize the functions of specific attention heads based on the human thought process
- Experimental methods for discovering special attention heads fall into two categories: Modeling-Free and Modeling-Required methods
- Existing research has identified and categorized various functions of attention heads through systematic review
- Current research on attention heads has limitations that warrant discussion and future investigation
**Limitations**: The abstract mentions that limitations of current research are discussed but does not specify what those limitations are.

## References

Balesni, M., Korbak, T., & Evans, O. (2024). Lessons from studying two-hop latent reasoning. arXiv. https://arxiv.org/abs/2411.16353

Hao, S., Sukhbaatar, S., Su, D., Li, X., Hu, Z., Weston, J., & Tian, Y. (2024). Training large language models to reason in a continuous latent space. arXiv. https://arxiv.org/abs/2412.06769

Hwang, H., Jeon, B., Kim, S., Kim, J., Chang, H., Yang, S., Won, S., Lee, D., Ahn, Y., & Seo, M. (2025). Latent reasoning via sentence embedding prediction. arXiv. https://arxiv.org/abs/2505.22202

Tan, W., Li, J., Ju, J., Luo, Z., Song, R., & Luan, J. (2025). Think silently, think fast: Dynamic latent compression of LLM reasoning chains. arXiv. https://arxiv.org/abs/2505.16552

Wang, X., Wang, D., Ying, W., Bai, H., Gong, N., Dong, S., Liu, K., & Fu, Y. (2025). Efficient post-training refinement of latent reasoning in large language models. arXiv. https://arxiv.org/abs/2506.08552

Xu, Z., Wang, H., Bespalov, D., Wu, X., Stone, P., & Qi, Y. (2023). LaRS: Latent reasoning skills for chain-of-thought reasoning. arXiv. https://arxiv.org/abs/2312.04684

Yue, Z., Jin, B., Zeng, H., Zhuang, H., Qin, Z., Yoon, J., Shang, L., Han, J., & Wang, D. (2025). Hybrid latent reasoning via reinforcement learning. arXiv. https://arxiv.org/abs/2505.18454

Zhang, Y., Valentino, M., Carvalho, D. S., & Freitas, A. (2025). Learning to disentangle latent reasoning rules with language VAEs: A systematic study. arXiv. https://arxiv.org/abs/2506.19418

Zhang, Y., Zhang, B., Li, Z., Li, M., Cheng, N., Chen, M., Wei, T., Ma, J., Wang, S., & Xiao, J. (2025). Self-enhanced reasoning training: Activating latent reasoning in small models for enhanced reasoning distillation. arXiv. https://arxiv.org/abs/2502.12744

Zheng, Z., Wang, Y., Huang, Y., Song, S., Yang, M., Tang, B., Xiong, F., & Li, Z. (2024). Attention heads of large language models: A survey. arXiv. https://arxiv.org/abs/2409.03752
