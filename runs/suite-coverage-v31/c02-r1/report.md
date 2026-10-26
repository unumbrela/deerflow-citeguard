# Systematic Literature Review: Latent Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv search query "latent reasoning", category cs.CL, published between 2023-07-08 and 2025-07-08
**Citation format**: APA 7th edition

## Executive Summary

Latent reasoning has emerged as a critical research direction in Large Language Models, focusing on performing multi-step inference within continuous hidden states rather than through explicit token-level reasoning. The surveyed literature reveals a rapidly evolving field with diverse methodological approaches, including reinforcement learning-based hybrid reasoning, embedding prediction frameworks, and compression techniques that balance efficiency with performance. Collectively, these papers demonstrate that latent reasoning can achieve competitive performance with traditional Chain-of-Thought approaches while significantly reducing computational costs. However, fundamental questions remain about scalability, the mechanisms underlying latent reasoning capabilities, and how to effectively activate and refine these capabilities in smaller models.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "latent reasoning", filtered to category cs.CL, published between 2023-07-08 and 2025-07-08. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Compression of Reasoning Chains

A dominant theme across the surveyed literature is the pursuit of more efficient latent reasoning that reduces computational overhead while maintaining or improving performance. CoLaR (Tan et al., 2025) achieves a 53.3% reduction in reasoning chain length with only 4.8% performance degradation compared to explicit Chain-of-Thought, and demonstrates up to 82.8% reduction on more difficult tasks. Similarly, Hwang et al. (2025) show that contextual embeddings under continuous inference reduce inference-time FLOPs by half while maintaining competitive performance with Chain-of-Thought on mathematics, logic, commonsense, and planning tasks. Wang et al. (2025) introduce a lightweight post-training framework that achieves a 5% accuracy gain on MathQA without additional training through contrastive reasoning feedback and residual embedding refinement. These convergent findings suggest that latent reasoning compression is not only feasible but can yield substantial efficiency gains.

### Theme 2: Hybrid and Multi-Modal Reasoning Approaches

Several papers explore hybrid approaches that combine discrete and continuous representations to leverage the strengths of both. Yue et al. (2025) introduce Hybrid Reasoning Policy Optimization (HRPO), an RL-based approach that integrates prior hidden states into sampled tokens with a learnable gating mechanism. This hybrid approach maintains LLMs' generative capabilities while incentivizing reasoning using both discrete and continuous representations, outperforming prior methods on knowledge- and reasoning-intensive tasks. Zhang et al. (2025) demonstrate that reasoning rules can be disentangled within encoder parametric space under explicit signal supervision, with FFN layers showing superior capability over attention layers at preserving separation of reasoning rules. These hybrid approaches represent a middle ground between purely latent and purely explicit reasoning paradigms.

### Theme 3: Activation and Refinement of Latent Reasoning Capabilities

A significant research direction focuses on activating and refining latent reasoning capabilities, particularly in smaller models. Zhang et al. (2025) show that small models can generate high-quality reasoning paths during sampling even without Chain-of-Thought prompting, though these paths remain latent due to low probability under standard decoding. Their Self-Enhanced Reasoning Training (SERT) approach activates these capabilities through self-training on filtered, self-generated reasoning paths. Xu et al. (2023) introduce LaRS, which employs unsupervised learning to create latent space representations of reasoning rationales, eliminating the need for auxiliary LLM inference while processing example banks four times faster than existing methods. Wang et al. (2025) similarly focus on post-training refinement, using contrastive feedback to guide models toward more accurate solutions.

### Theme 4: Foundational Capabilities and Theoretical Understanding

Several papers address fundamental questions about the nature and limits of latent reasoning capabilities. Balesni et al. (2024) provide definitive evidence that LLMs are capable of latent two-hop reasoning, though they note that it remains unclear how this ability scales with model size. Their work emphasizes the importance of avoiding both spurious successes from memorization and spurious failures from artificial experimental setups. Zhu et al. (2025) provide a comprehensive survey examining foundational neural network layers as computational substrates, exploring diverse methodologies including activation-based recurrence and hidden state propagation, and discussing advanced paradigms like infinite-depth latent reasoning via masked diffusion models. Zheng et al. (2024) introduce a four-stage framework (Knowledge Recalling, In-Context Identification, Latent Reasoning, and Expression Preparation) to systematically categorize attention head functions, providing theoretical grounding for understanding how attention mechanisms support latent reasoning.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that latent reasoning can achieve competitive performance with explicit Chain-of-Thought while offering substantial efficiency gains. Multiple papers demonstrate that latent reasoning reduces computational costs—whether through FLOPs reduction (Hwang et al., 2025), chain length compression (Tan et al., 2025), or elimination of auxiliary inference (Xu et al., 2023). There is also convergence on the finding that latent reasoning capabilities exist in models of various sizes but may require specific training or activation strategies to manifest effectively.

**Disagreements**: The literature shows some tension regarding the mechanisms underlying latent reasoning. While Zhu et al. (2025) emphasize neural network layers as the primary computational substrate, Zhang et al. (2025) find that FFN layers are superior to attention layers at preserving reasoning rule separation, suggesting different architectural components may play varying roles. Additionally, while Balesni et al. (2024) establish that LLMs are capable of latent two-hop reasoning, they explicitly note uncertainty about how this capability scales with model size—a question that other papers address through different methodologies but do not conclusively resolve.

## Gaps and Open Questions

Several significant gaps emerge from the surveyed literature:

1. **Scalability uncertainty**: Balesni et al. (2024) explicitly note that it remains unclear how latent two-hop reasoning ability scales with model size. This represents a fundamental gap in understanding the relationship between model capacity and latent reasoning capabilities.

2. **Post-training refinement limits**: While Wang et al. (2025) demonstrate effective post-training refinement, Zhang et al. (2025) find that in mathematical reasoning tasks, increasing sample count does not improve performance beyond a certain point, suggesting there may be fundamental limits to refinement approaches.

3. **Architectural mechanisms**: The relative roles of different architectural components (attention layers vs. FFN layers) in supporting latent reasoning remain incompletely understood, with different papers emphasizing different mechanisms.

4. **Generalization across domains**: While several papers evaluate across multiple domains (mathematics, logic, commonsense, planning), systematic understanding of how latent reasoning capabilities transfer across fundamentally different reasoning domains remains limited.

5. **Interpretability**: While Yue et al. (2025) note that HRPO-trained LLMs remain interpretable and exhibit cross-lingual patterns, the broader question of how to interpret and debug latent reasoning processes remains largely unaddressed.

## Per-Paper Annotations

### Balesni et al. (2024)

**Research question**: Are LLMs fundamentally capable of latent two-hop reasoning, and what experimental conditions provide definitive evidence?
**Methodology**: The authors fine-tune LLMs (including Llama 3 8B and GPT-4o) on synthetic facts and test two-hop reasoning over these facts, using synthetic facts to rule out memorization and reasoning shortcuts as explanations for two-hop performance.
**Key findings**:
- Models fail to compose two synthetic facts but can succeed when one fact is synthetic and the other is natural
- LLMs are undeniably capable of latent two-hop reasoning, though it remains unclear how this ability scales with model size
- Researchers must avoid both spurious successes from memorization/reasoning shortcuts and spurious failures from artificial experimental setups
- Previous work on the gap between latent and externalized two-hop reasoning produced mixed evidence with inconclusive results
**Limitations**: It remains unclear how latent two-hop reasoning ability scales with model size.

### Hwang et al. (2025)

**Research question**: Can pretrained language models learn to reason over structured semantic units like sentences rather than raw token sequences?
**Methodology**: The framework adapts pretrained token-level LMs to operate in sentence space by autoregressively predicting continuous embeddings of next sentences, exploring semantic embeddings (autoencoding for surface meaning) and contextual embeddings (next-sentence prediction for anticipatory structure) under discretized and continuous inference regimes.
**Key findings**:
- Contextual embeddings under continuous inference show competitive performance with Chain-of-Thought while reducing inference-time FLOPs by half on average
- The approach was evaluated across four domains: mathematics, logic, commonsense, and planning
- The method demonstrates early signs of scalability and modular adaptation
- SentenceLens diagnostic tool was introduced to visualize latent trajectories by decoding intermediate model states into interpretable sentences
- Pretrained LMs can effectively transition to abstract, structured reasoning within latent embedding spaces
**Limitations**: not stated in abstract

### Tan et al. (2025)

**Research question**: How can chain-of-thought reasoning in large language models be compressed in latent space to reduce computational cost while maintaining performance?
**Methodology**: CoLaR uses a two-stage training approach: supervised fine-tuning with auxiliary next compressed embedding prediction that merges consecutive token embeddings using randomly sampled compression factors, followed by reinforcement learning that leverages the latent head's non-deterministic nature to explore diverse and compact reasoning paths.
**Key findings**:
- CoLaR achieves 14.1% higher accuracy than latent-based baseline methods at comparable compression ratios
- The method reduces reasoning chain length by 53.3% with only 4.8% performance degradation compared to explicit CoT
- RL-enhanced CoLaR demonstrates performance gains of up to 5.4% on challenging mathematical reasoning tasks
- The approach dramatically reduces latent reasoning chain length by 82.8% on more difficult tasks
- CoLaR enables dynamic adjustment of reasoning speed at inference time by prompting the desired compression factor
**Limitations**: not stated in abstract

### Wang et al. (2025)

**Research question**: How can reasoning embeddings be effectively updated during post-training to guide LLMs toward more accurate solutions in latent reasoning?
**Methodology**: The authors propose a lightweight post-training framework that refines latent reasoning trajectories using two novel strategies: contrastive reasoning feedback that compares embeddings against strong and weak baselines, and residual embedding refinement that stabilizes updates by progressively integrating current and historical gradients.
**Key findings**:
- The framework achieves a 5% accuracy gain on MathQA without additional training
- Contrastive reasoning feedback infers effective update directions via embedding enhancement by comparing reasoning embeddings against strong and weak baselines
- Residual embedding refinement stabilizes updates by progressively integrating current and historical gradients, enabling fast yet controlled convergence
- Extensive experiments and case studies were conducted on five reasoning benchmarks to demonstrate effectiveness
**Limitations**: not stated in abstract

### Yue et al. (2025)

**Research question**: How can latent reasoning be made compatible with LLMs' discrete autoregressive generation while leveraging their intrinsic reasoning capabilities?
**Methodology**: The authors introduce hybrid reasoning policy optimization (HRPO), an RL-based approach that integrates prior hidden states into sampled tokens with a learnable gating mechanism and initializes training with predominantly token embeddings while progressively incorporating more hidden features.
**Key findings**:
- HRPO outperforms prior methods in both knowledge- and reasoning-intensive tasks across diverse benchmarks
- The hybrid approach maintains LLMs' generative capabilities while incentivizing hybrid reasoning using both discrete and continuous representations
- HRPO introduces stochasticity into latent reasoning via token sampling, enabling RL-based optimization without requiring CoT trajectories
- HRPO-trained LLMs remain interpretable and exhibit cross-lingual patterns and shorter completion lengths
**Limitations**: not stated in abstract

### Zhang, Y. et al. (2025)

**Research question**: How can reasoning rules be explicitly embedded and memorised within Transformer-based language models through Language Variational Autoencoders?
**Methodology**: The study proposes a complete pipeline for learning reasoning rules within Transformer-based language VAEs, encompassing three rule-based reasoning tasks, a supporting theoretical framework, and a practical end-to-end architecture. Experiments examine disentangled reasoning under explicit signal supervision, prior knowledge injection into Query mechanisms, and performance bottlenecks in mathematical reasoning tasks using Qwen2.5(0.5B).
**Key findings**:
- Reasoning rules can be disentangled within the encoder's parametric space under explicit signal supervision, resulting in distinct clustering of rules in the output feature space
- Injecting reasoning information into the Query enables more effective retrieval of stored values from memory based on Key, offering a simple method for integrating prior knowledge into decoder-only language models
- In mathematical reasoning tasks using Qwen2.5(0.5B), increasing sample count does not improve performance beyond a certain point
- FFN layers are better than attention layers at preserving the separation of reasoning rules in the model's parameters
**Limitations**: not stated in abstract

### Zhang, Y. et al. (2025) [Self-Enhanced Reasoning Training]

**Research question**: Can latent reasoning capabilities in small models be activated and leveraged through self-training to improve reasoning distillation from teacher models?
**Methodology**: SERT activates and leverages latent reasoning capabilities in small models through self-training on filtered, self-generated reasoning paths under zero-shot conditions, using GPT-3.5 as teacher and GPT-2 models as students.
**Key findings**:
- Small models can generate high-quality reasoning paths during sampling even without chain-of-thought prompting, though these paths are latent due to low probability under standard decoding
- SERT enhances the reasoning abilities of small models through self-training on filtered self-generated reasoning paths
- The approach improves small model performance in reasoning distillation from teacher models
- The method addresses the limitation that existing reasoning distillation methods focus primarily on improving teacher-generated reasoning paths
**Limitations**: not stated in abstract

### Zheng et al. (2024)

**Research question**: What are the roles and mechanisms of attention heads in Large Language Models, and how do they contribute to the internal reasoning processes?
**Methodology**: The survey introduces a novel four-stage framework inspired by human thought processes (Knowledge Recalling, In-Context Identification, Latent Reasoning, and Expression Preparation) to systematically categorize attention head functions. It analyzes experimental methodologies used to discover special heads, dividing them into Modeling-Free and Modeling-Required methods, and summarizes relevant evaluation methods and benchmarks.
**Key findings**:
- Attention heads have emerged as a focal point for investigating the underlying mechanics and reasoning bottlenecks of Large Language Models
- A four-stage framework (Knowledge Recalling, In-Context Identification, Latent Reasoning, and Expression Preparation) can be used to identify and categorize the functions of specific attention heads
- Experimental methodologies for discovering special attention heads can be categorized into Modeling-Free and Modeling-Required methods
- Current research on attention heads has limitations that suggest several potential future directions for investigation
**Limitations**: not stated in abstract

### Zhu et al. (2025)

**Research question**: What is the current state of latent reasoning research in Large Language Models and what are the key methodologies and future directions?
**Methodology**: This paper provides a comprehensive survey of latent reasoning by examining foundational neural network layers as computational substrates, exploring diverse methodologies including activation-based recurrence and hidden state propagation, and discussing advanced paradigms like infinite-depth latent reasoning via masked diffusion models.
**Key findings**:
- Latent reasoning performs multi-step inference entirely in the model's continuous hidden state, eliminating token-level supervision
- Neural network layers serve as the computational substrate for reasoning, with hierarchical representations supporting complex transformations
- Diverse latent reasoning methodologies include activation-based recurrence, hidden state propagation, and fine-tuning strategies that compress or internalize explicit reasoning traces
- Advanced paradigms such as infinite-depth latent reasoning via masked diffusion models enable globally consistent and reversible reasoning processes
**Limitations**: not stated in abstract

### Xu et al. (2023)

**Research question**: How can in-context learning examples for chain-of-thought prompting be selected based on reasoning rationales rather than questions without requiring costly human expertise or auxiliary LLM inference?
**Methodology**: LaRS employs unsupervised learning to create a latent space representation of rationales with a reasoning skill latent variable, and learns a reasoning policy to determine required reasoning skills for given questions, then selects ICL examples by aligning reasoning skills between past examples and the question.
**Key findings**:
- LaRS eliminates the need for auxiliary LLM inference or manual prompt design while being theoretically grounded and compute-efficient
- LaRS consistently outperforms state-of-the-art skill-based selection methods
- The approach processes example banks four times faster than existing methods
- LaRS reduces LLM inferences during the selection stage by half
- The method shows greater robustness to sub-optimal example banks
**Limitations**: not stated in abstract

## References

Balesni, M., Korbak, T., & Evans, O. (2024). Lessons from studying two-hop latent reasoning. arXiv. https://arxiv.org/abs/2411.16353

Hwang, H., Jeon, B., Kim, S., Kim, J., Chang, H., Yang, S., Won, S., Lee, D., Ahn, Y., & Seo, M. (2025). Latent reasoning via sentence embedding prediction. arXiv. https://arxiv.org/abs/2505.22202

Tan, W., Li, J., Ju, J., Luo, Z., Song, R., & Luan, J. (2025). Think silently, think fast: Dynamic latent compression of LLM reasoning chains. arXiv. https://arxiv.org/abs/2505.16552

Wang, X., Wang, D., Ying, W., Bai, H., Gong, N., Dong, S., Liu, K., & Fu, Y. (2025). Efficient post-training refinement of latent reasoning in large language models. arXiv. https://arxiv.org/abs/2506.08552

Xu, Z., Wang, H., Bespalov, D., Wu, X., Stone, P., & Qi, Y. (2023). LaRS: Latent reasoning skills for chain-of-thought reasoning. arXiv. https://arxiv.org/abs/2312.04684

Yue, Z., Jin, B., Zeng, H., Zhuang, H., Qin, Z., Yoon, J., Shang, L., Han, J., & Wang, D. (2025). Hybrid latent reasoning via reinforcement learning. arXiv. https://arxiv.org/abs/2505.18454

Zhang, Y., Valentino, M., Carvalho, D. S., & Freitas, A. (2025). Learning to disentangle latent reasoning rules with language VAEs: A systematic study. arXiv. https://arxiv.org/abs/2506.19418

Zhang, Y., Zhang, B., Li, Z., Li, M., Cheng, N., Chen, M., Wei, T., Ma, J., Wang, S., & Xiao, J. (2025). Self-enhanced reasoning training: Activating latent reasoning in small models for enhanced reasoning distillation. arXiv. https://arxiv.org/abs/2502.12744

Zheng, Z., Wang, Y., Huang, Y., Song, S., Yang, M., Tang, B., Xiong, F., & Li, Z. (2024). Attention heads of large language models: A survey. arXiv. https://arxiv.org/abs/2409.03752

Zhu, R.-J., Peng, T., Cheng, T., Qu, X., Huang, J., Zhu, D., Wang, H., Xue, K., Zhang, X., Shan, Y., Cai, T., Kergan, T., Kembay, A., Smith, A., Lin, C., Nguyen, B., Pan, Y., Chou, Y., Cai, Z., & Wu, Z. (2025). A survey on latent reasoning. arXiv. https://arxiv.org/abs/2507.06203
