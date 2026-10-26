# Systematic Literature Review: Latent Reasoning

**Date**: 2026-10-26
**Papers surveyed**: 10
**Scope**: arXiv query "latent reasoning", category cs.CL, published between 2023-07-08 and 2025-07-07
**Citation format**: APA 7th edition

## Executive Summary

The literature on latent reasoning in large language models has rapidly evolved between 2023 and 2025, with researchers exploring how reasoning can occur in continuous embedding spaces rather than explicit token sequences. The surveyed papers collectively demonstrate a shift from traditional Chain-of-Thought (CoT) approaches toward more efficient, compressed, and scalable reasoning paradigms. Key innovations include reinforcement learning-based hybrid reasoning, sentence embedding prediction, continuous latent space reasoning, and dynamic compression techniques. The field shows strong convergence around the idea that latent reasoning can reduce computational costs while maintaining or improving accuracy, though questions remain about scalability, interpretability, and optimal training methodologies.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-26 using the query "latent reasoning", filtered to category cs.CL, published between 2023-07-08 and 2025-07-07. Papers were sorted by submission date and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Continuous Latent Space Reasoning

A major research direction involves moving reasoning from discrete token space to continuous embedding representations. Hao et al. (2024) introduced Coconut (Chain of Continuous Thought), which uses the last hidden state of LLMs as continuous thought representations fed back as next input embeddings. This approach enables breadth-first search patterns rather than deterministic chain-of-thought, outperforming traditional CoT on logical reasoning tasks requiring substantial search. Similarly, Hwang et al. (2025) adapted pretrained token-level LMs to operate in sentence space by autoregressively predicting continuous embeddings of next sentences, showing competitive performance with CoT while reducing inference-time FLOPs by half.

### Theme 2: Reinforcement Learning for Latent Reasoning

Multiple papers leverage reinforcement learning to optimize latent reasoning capabilities. Yue et al. (2025) developed hybrid reasoning policy optimization (HRPO), an RL-based approach integrating prior hidden states into sampled tokens with learnable gating mechanisms. Their method maintains LLMs' generative capabilities while incentivizing hybrid reasoning using both discrete and continuous representations. Zhang et al. (2025) proposed Self-Enhanced Reasoning Training (SERT), using self-training on filtered, self-generated reasoning paths under zero-shot conditions to activate latent reasoning in small models for enhanced distillation from larger teachers.

### Theme 3: Compression and Efficiency

Several works focus on compressing reasoning chains to reduce computational overhead. Tan et al. (2025) introduced Compressed Latent Reasoning (CoLaR), a two-stage framework using supervised fine-tuning with auxiliary next compressed embedding prediction, then RL enhancement. CoLaR achieves 14.1% higher accuracy than latent-based baselines at comparable compression ratios, reducing reasoning chain length by 53.3% with only 4.8% performance degradation. Wang et al. (2025) proposed a lightweight post-training framework with contrastive reasoning feedback and residual embedding refinement, achieving 5% accuracy gain on MathQA without additional training.

### Theme 4: Disentangled Reasoning Representations

Research has explored how reasoning rules can be explicitly embedded and disentangled within model architectures. Zhang et al. (2025) investigated Language Variational Autoencoders for learning reasoning rules, finding that under explicit signal supervision, reasoning rules can be disentangled within the encoder's parametric space, with FFN layers better than attention layers at preserving separation of reasoning rules. This work provides theoretical grounding for how reasoning capabilities can be modularly represented within transformer architectures.

### Theme 5: Empirical Studies of Latent Reasoning Capabilities

Foundational work examines the latent reasoning capabilities of existing models. Balesni et al. (2024) studied two-hop latent reasoning in LLMs including Llama 3 8B and GPT-4o, finding that models can succeed at latent two-hop reasoning when one fact is synthetic and one natural, though they fail to compose two synthetic facts. Xu et al. (2023) developed LaRS (Latent Reasoning Skills), employing unsupervised learning to create latent space representations of rationales for chain-of-thought example selection, processing example banks four times faster than existing methods.

### Theme 6: Attention Mechanisms and Latent Reasoning

The relationship between attention mechanisms and latent reasoning has been systematically examined. Zheng et al. (2024) introduced a four-stage framework (Knowledge Recalling, In-Context Identification, Latent Reasoning, Expression Preparation) to categorize attention head functions, providing experimental methodologies for discovering special attention heads that enable reasoning processes.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that latent reasoning offers computational efficiency benefits over explicit Chain-of-Thought approaches. Multiple studies demonstrate that continuous representations can encode alternative reasoning paths, enabling more flexible search strategies (Hao et al., 2024; Hwang et al., 2025). There is consensus that small models possess latent reasoning capabilities that can be activated through appropriate training methodologies (Zhang et al., 2025; Balesni et al., 2024).

**Disagreements**: The optimal approach to latent reasoning remains contested. While some papers advocate for RL-based optimization (Yue et al., 2025; Tan et al., 2025), others demonstrate success with supervised fine-tuning and contrastive learning (Wang et al., 2025; Hwang et al., 2025). The scalability of latent reasoning approaches varies across domains, with some methods showing strong mathematical reasoning performance but limited evaluation on other task types.

## Gaps and Open Questions

Several gaps emerge from the surveyed literature. First, the scalability of latent reasoning with model size remains unclear, as noted by Balesni et al. (2024). Second, most papers do not state limitations explicitly in their abstracts, suggesting a need for more comprehensive evaluation of failure modes. Third, while efficiency gains are demonstrated, the interpretability trade-offs of latent versus explicit reasoning require further investigation. Fourth, the relationship between attention mechanisms and latent reasoning capabilities, while surveyed by Zheng et al. (2024), needs deeper empirical validation. Finally, cross-lingual patterns in latent reasoning, briefly mentioned by Yue et al. (2025), represent an underexplored direction.

## Per-Paper Annotations

### Balesni et al. (2024)

**Research question**: What are the latent two-hop reasoning capabilities of large language models when tested in a controlled setting that rules out memorization and reasoning shortcuts?

**Methodology**: Fine-tuned LLMs (including Llama 3 8B and GPT-4o) on synthetic facts and tested two-hop reasoning over these facts, using synthetic facts to rule out memorization and reasoning shortcuts.

**Key findings**:
- Models fail to compose two synthetic facts but can succeed when one fact is synthetic and the other is natural
- LLMs are undeniably capable of latent two-hop reasoning, though scalability with model size remains unclear
- Researchers must avoid both spurious successes from memorization/reasoning shortcuts and spurious failures from artificial setups

**Limitations**: It remains unclear how latent two-hop reasoning ability scales with model size.

### Hao et al. (2024)

**Research question**: Can large language models reason more effectively by operating in a continuous latent space rather than being constrained to the language space?

**Methodology**: Introduced Coconut (Chain of Continuous Thought), using the last hidden state of LLMs as continuous thought representations fed back as next input embeddings directly in continuous space, enabling breadth-first search patterns.

**Key findings**:
- Language space may not be optimal for reasoning as most word tokens primarily ensure textual coherence
- Continuous thoughts can encode multiple alternative next steps, enabling breadth-first search
- Coconut outperforms traditional CoT on logical reasoning tasks requiring substantial search
- Latent reasoning paradigm achieves better accuracy-efficiency trade-off compared to CoT

**Limitations**: Not stated in abstract.

### Hwang et al. (2025)

**Research question**: Can pretrained language models learn to reason over structured semantic units (sentences) rather than raw token sequences?

**Methodology**: Framework adapting pretrained token-level LMs to operate in sentence space by autoregressively predicting continuous embeddings of next sentences, exploring semantic embeddings (autoencoding) and contextual embeddings (next-sentence prediction).

**Key findings**:
- Contextual embeddings under continuous inference show competitive performance with CoT reasoning
- Approach reduces inference-time FLOPs on average by half compared to traditional CoT
- Pretrained LMs can effectively transition to abstract, structured reasoning within latent embedding spaces
- Framework shows early signs of scalability and modular adaptation

**Limitations**: Not stated in abstract.

### Tan et al. (2025)

**Research question**: Can Chain-of-Thought reasoning processes be dynamically compressed in latent space to reduce computational cost while maintaining performance?

**Methodology**: Introduced Compressed Latent Reasoning (CoLaR), a two-stage framework using supervised fine-tuning with auxiliary next compressed embedding prediction objective, then RL enhancement leveraging latent head's non-deterministic nature.

**Key findings**:
- CoLaR achieves 14.1% higher accuracy than latent-based baseline methods at comparable compression ratios
- Framework reduces reasoning chain length by 53.3% with only 4.8% performance degradation compared to explicit CoT
- RL-enhanced CoLaR demonstrates performance gains up to 5.4% while reducing latent reasoning chain length by 82.8%
- Enables dynamic adjustment of reasoning speed at inference time by prompting desired compression factor

**Limitations**: Not stated in abstract.

### Wang et al. (2025)

**Research question**: How can reasoning embeddings be effectively updated during post-training to guide large language models toward more accurate solutions in latent reasoning?

**Methodology**: Lightweight post-training framework with contrastive reasoning feedback comparing reasoning embeddings against strong and weak baselines, and residual embedding refinement stabilizing updates by progressively integrating current and historical gradients.

**Key findings**:
- Framework refines latent reasoning trajectories using contrastive reasoning feedback and residual embedding refinement
- Extensive experiments on five reasoning benchmarks demonstrate effectiveness
- Achieves 5% accuracy gain on MathQA without additional training
- Addresses challenge of updating reasoning embeddings during post-training without producing explicit outputs

**Limitations**: Not stated in abstract.

### Xu et al. (2023)

**Research question**: How can in-context learning examples be selected for chain-of-thought prompting based on reasoning skills rather than questions, without requiring human experts or pre-trained LLMs?

**Methodology**: LaRS employs unsupervised learning to create latent space representation of rationales with reasoning skill latent variable, learns reasoning policy to determine required reasoning skill, selects ICL examples by aligning reasoning skills.

**Key findings**:
- LaRS consistently outperforms SOTA skill-based selection methods
- Approach processes example banks four times faster than existing methods
- Reduces LLM inferences during selection stage by half
- Shows greater robustness to sub-optimal example banks
- Theoretically grounded and compute-efficient, eliminating need for auxiliary LLM inference or manual prompt design

**Limitations**: Not stated in abstract.

### Yue et al. (2025)

**Research question**: How can latent reasoning be made compatible with large language models while leveraging their intrinsic reasoning capabilities through reinforcement learning?

**Methodology**: Introduced hybrid reasoning policy optimization (HRPO), an RL-based approach integrating prior hidden states into sampled tokens with learnable gating mechanism, initializing training with predominantly token embeddings while progressively incorporating more hidden features.

**Key findings**:
- HRPO outperforms prior methods in both knowledge- and reasoning-intensive tasks across diverse benchmarks
- Maintains LLMs' generative capabilities while incentivizing hybrid reasoning using both discrete and continuous representations
- Introduces stochasticity into latent reasoning via token sampling, enabling RL-based optimization without requiring CoT trajectories
- HRPO-trained LLMs remain interpretable and exhibit cross-lingual patterns and shorter completion lengths

**Limitations**: Not stated in abstract.

### Zhang, Y. et al. (2025)

**Research question**: How can reasoning rules be explicitly embedded and memorised within language models through Language Variational Autoencoders?

**Methodology**: Complete pipeline for learning reasoning rules within Transformer-based language VAEs, encompassing three rule-based reasoning tasks, supporting theoretical framework, and practical end-to-end architecture.

**Key findings**:
- Under explicit signal supervision, reasoning rules can be disentangled within encoder's parametric space
- Injecting reasoning information into Query enables more effective retrieval of stored values from memory
- In mathematical reasoning tasks using Qwen2.5(0.5B), increasing sample count doesn't improve performance beyond a point
- FFN layers are better than attention layers at preserving separation of reasoning rules in model parameters

**Limitations**: Not stated in abstract.

### Zhang, Y. et al. (2025) [SERT]

**Research question**: Can latent reasoning capabilities in small models be activated and leveraged to improve reasoning distillation from larger teacher models?

**Methodology**: Proposed Self-Enhanced Reasoning Training (SERT), using self-training on filtered, self-generated reasoning paths under zero-shot conditions to activate latent reasoning in small models, with GPT-3.5 as teacher and GPT-2 models as students.

**Key findings**:
- Small models can generate high-quality reasoning paths during sampling even without CoT prompting, though paths remain latent due to low probability under standard decoding
- SERT successfully activates and leverages latent reasoning capabilities in small models through self-training
- Approach enhances small models' reasoning abilities and improves performance in reasoning distillation from GPT-3.5

**Limitations**: Not stated in abstract.

### Zheng et al. (2024)

**Research question**: How do attention heads function within large language models to enable reasoning processes?

**Methodology**: Introduced four-stage framework inspired by human thought processes (Knowledge Recalling, In-Context Identification, Latent Reasoning, Expression Preparation) to categorize attention head functions, analyzed Modeling-Free and Modeling-Required experimental methodologies.

**Key findings**:
- Attention heads have emerged as focal point for investigating underlying mechanics and reasoning bottlenecks of LLMs
- Novel four-stage framework systematically categorizes functions of specific attention heads based on human thought processes
- Experimental methodologies for discovering special attention heads fall into two categories: Modeling-Free and Modeling-Required methods
- Survey summarizes relevant evaluation methods and benchmarks for attention head research

**Limitations**: The abstract discusses limitations of current research but does not specify them in detail.

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
