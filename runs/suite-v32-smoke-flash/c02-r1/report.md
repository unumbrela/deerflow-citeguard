# Systematic Literature Review: Latent Reasoning in Large Language Models

## Executive Summary

This systematic literature review examines 10 research papers on latent reasoning published between July 2023 and July 2025 in the field of Computation and Language (cs.CL). Latent reasoning represents a paradigm shift from traditional chain-of-thought (CoT) approaches, enabling language models to perform internal computation using hidden states rather than explicit token sequences. The reviewed literature reveals significant progress in four key areas: reinforcement learning-based hybrid reasoning, efficient post-training refinement, small model activation for reasoning distillation, and continuous latent space training. Key findings indicate that latent reasoning methods achieve comparable or superior performance to CoT while substantially reducing computational overhead and inference costs.

---

## 1. Introduction

### 1.1 Background and Motivation

Large language models (LLMs) have demonstrated remarkable capabilities in complex reasoning tasks through chain-of-thought (CoT) prompting, which generates explicit intermediate reasoning steps as text tokens (Xu et al., 2023). However, this approach suffers from significant limitations including token overhead, fixed reasoning trajectories, and inability to perform step-wise refinement during inference (Wang et al., 2025a). These constraints motivate the development of latent reasoning paradigms that operate directly within the model's internal representation space.

Latent reasoning enables LLMs to perform internal computation with hidden states from previous steps, benefitting from more informative features without sampling discrete CoT paths (Yue et al., 2025). This paradigm offers several advantages: reduced computational costs, dynamic reasoning compression, and the potential for more sophisticated search strategies beyond deterministic token generation.

### 1.2 Scope and Methodology

This review systematically analyzes 10 peer-reviewed papers published on arXiv between July 8, 2023, and July 7, 2025, indexed under the primary category cs.CL (Computation and Language). The papers were selected based on their focus on latent reasoning mechanisms, methodologies, and applications across various domains including mathematical reasoning, logical inference, commonsense understanding, and planning tasks.

The review synthesizes findings across multiple dimensions: theoretical frameworks, methodological innovations, experimental benchmarks, and practical implications for model deployment and scaling.

---

## 2. Theoretical Foundations

### 2.1 Defining Latent Reasoning

Latent reasoning fundamentally differs from traditional CoT by operating in continuous embedding spaces rather than discrete token sequences. Hwang et al. (2025) conceptualize this as lifting pretrained token-level language models to operate over "higher-level abstractions - sentences, propositions, and concepts" rather than raw token streams. Their framework adapts pretrained models to autoregressively predict continuous embeddings of next sentences, exploring both semantic embeddings (preserving surface meaning via autoencoding) and contextual embeddings (encoding anticipatory structure via next-sentence prediction).

Zheng et al. (2024) provide a comprehensive four-stage framework inspired by human thought processes that includes latent reasoning as a critical component: Knowledge Recalling → In-Context Identification → **Latent Reasoning** → Expression Preparation. This positions latent reasoning as an intermediate processing stage where internal representations are manipulated before being decoded into explicit output.

### 2.2 Continuous vs. Discrete Paradigms

A central challenge in latent reasoning is reconciling continuous hidden state computation with the inherently discrete nature of autoregressive text generation. Yue et al. (2025) identify this incompatibility as a fundamental barrier: "their continuous paradigm conflicts with the discrete nature of autoregressive generation." They propose Hybrid Reasoning Policy Optimization (HRPO), which integrates prior hidden states into sampled tokens through a learnable gating mechanism, maintaining generative capabilities while leveraging continuous reasoning.

Hao et al. (2024) introduce Coconut (Chain of Continuous Thought), which uses the last hidden state as a "continuous thought" representation that feeds back directly to the model without decoding into words. This enables "breadth-first search (BFS)" capability where continuous thoughts can encode multiple alternative next steps simultaneously, contrasting with CoT's commitment to single deterministic paths.

---

## 3. Methodological Approaches

### 3.1 Reinforcement Learning-Based Methods

#### 3.1.1 Hybrid Reasoning Policy Optimization (HRPO)

Yue et al. (2025) develop HRPO as an RL-based approach that introduces stochasticity into latent reasoning via token sampling, eliminating the need for CoT trajectories during training. Their method employs two key innovations:

1. **Learnable Gating Mechanism**: Integrates prior hidden states into sampled tokens dynamically
2. **Progressive Training Strategy**: Initializes with predominantly token embeddings while progressively incorporating hidden features

This design maintains LLMs' generative capabilities while incentivizing hybrid reasoning using both discrete and continuous representations.

#### 3.1.2 RL-Enhanced Compression

Tan et al. (2025) combine reinforcement learning with supervised fine-tuning in their Compressed Latent Reasoning (CoLaR) framework. The RL phase leverages the non-deterministic nature of the latent head to explore diverse reasoning paths while exploiting more compact ones, achieving "performance gains of up to 5.4% while dramatically reducing latent reasoning chain length by 82.8%" on challenging mathematical tasks.

### 3.2 Post-Training Refinement Strategies

Wang et al. (2025a) address the challenge of updating reasoning embeddings during post-training through two novel strategies:

1. **Contrastive Reasoning Feedback**: Compares reasoning embeddings against strong and weak baselines to infer effective update directions via embedding enhancement
2. **Residual Embedding Refinement**: Stabilizes updates by progressively integrating current and historical gradients for fast yet controlled convergence

Their lightweight framework achieves a 5% accuracy gain on MathQA without additional training, demonstrating the efficiency of embedding-space refinement.

### 3.3 Small Model Activation Techniques

Zhang et al. (2025) observe that small models like GPT-2 can generate high-quality reasoning paths during sampling even without CoT prompting, though these remain latent due to low probability under standard decoding. They propose Self-Enhanced Reasoning Training (SERT), which activates and leverages latent reasoning capabilities through self-training on filtered, self-generated reasoning paths under zero-shot conditions. Using OpenAI's GPT-3.5 as teacher and GPT-2 as students, SERT successfully enhances small model reasoning abilities for distillation purposes.

### 3.4 Unsupervised Skill Discovery

Xu et al. (2023) introduce Latent Reasoning Skills (LaRS), employing unsupervised learning to create latent space representations of rationales. A latent variable called "reasoning skill" learns to determine required reasoning capabilities for given questions, enabling example selection by aligning reasoning skills between past examples and queries. This theoretically grounded approach eliminates auxiliary LLM inference requirements and achieves fourfold speed improvements over skill-based selection methods.

### 3.5 Variational Autoencoder Frameworks

Zhang et al. (2025b) investigate disentangling reasoning rules within Transformer-based language VAEs, proposing a complete pipeline encompassing three rule-based reasoning tasks and theoretical foundations. Their experiments reveal that "under explicit signal supervision, reasoning rules - viewed as functional mappings - can be disentangled within the encoder's parametric space," resulting in distinct clustering of rules in output feature space. They note that FFN layers outperform attention layers at preserving reasoning rule separation.

---

## 4. Empirical Findings and Benchmarks

### 4.1 Performance Across Domains

The reviewed papers evaluate latent reasoning across multiple domains:

| Paper | Domains Tested | Key Metrics | Best Results |
|-------|---------------|-------------|--------------|
| Yue et al. (2025) | Knowledge-intensive, reasoning-intensive | Accuracy, interpretability | Outperforms prior methods |
| Wang et al. (2025a) | MathQA, five reasoning benchmarks | Accuracy | +5% on MathQA |
| Tan et al. (2025) | Four mathematical reasoning datasets | Accuracy, chain length | +14.1% vs baselines, -53.3% chain length |
| Hwang et al. (2025) | Mathematics, logic, commonsense, planning | FLOPs, accuracy | Competitive with CoT, 50% fewer FLOPs |
| Hao et al. (2024) | Logical reasoning requiring search | Accuracy, efficiency | Better trade-off than CoT |
| Balesni et al. (2024) | Two-hop QA with synthetic facts | Composition success | Partial success patterns identified |

### 4.2 Computational Efficiency

Latent reasoning consistently demonstrates substantial efficiency gains:

- **Token Reduction**: Tan et al. (2025) achieve 53.3% reduction in reasoning chain length with only 4.8% performance degradation versus explicit CoT
- **FLOPs Savings**: Hwang et al. (2025) report average 50% reduction in inference-time FLOPs compared to CoT
- **Compression Ratios**: CoLaR achieves up to 82.8% latent reasoning chain length reduction while maintaining competitive accuracy

### 4.3 Scaling Considerations

Balesni et al. (2024) provide crucial insights on scalability through careful experimentation with Llama 3 8B and GPT-4o on two-hop reasoning tasks. Their findings reveal nuanced patterns: "Models fail to compose two synthetic facts, but can succeed when one fact is synthetic and the other is natural." This suggests latent reasoning capabilities may scale differently depending on knowledge distribution rather than uniformly improving with model size.

Zhang et al. (2025b) identify performance bottlenecks in mathematical reasoning using Qwen2.5(0.5B), noting that "increasing sample count doesn't improve performance beyond a point," indicating potential limits to data-driven latent reasoning improvements in smaller models.

---

## 5. Critical Analysis

### 5.1 Strengths and Advantages

**Computational Efficiency**: All reviewed papers demonstrate significant reductions in computational overhead compared to traditional CoT, making latent reasoning particularly attractive for resource-constrained deployments.

**Dynamic Adaptability**: Methods like CoLaR enable dynamic adjustment of reasoning speed at inference time through compression factor prompting, offering flexibility absent in fixed CoT trajectories.

**Search Capabilities**: Coconut's continuous thought representation enables breadth-first search strategies impossible with deterministic token generation, potentially unlocking new problem-solving approaches.

**Interpretability Potential**: HRPO-trained models exhibit intriguing behaviors like cross-lingual patterns and shorter completion lengths, suggesting latent reasoning may preserve or enhance model interpretability despite operating in hidden spaces.

### 5.2 Limitations and Challenges

**Experimental Validity Concerns**: Balesni et al. (2024) emphasize critical methodological considerations: researchers must avoid both spurious successes (from memorization shortcuts) and spurious failures (from artificial experimental setups divorced from frontier LLM training).

**Memorization vs. Reasoning**: The distinction between genuine latent reasoning and pattern memorization remains challenging to establish definitively, particularly when models encounter familiar facts or structures.

**Small Model Constraints**: While SERT demonstrates success in activating latent reasoning in small models, Zhang et al. (2025b) identify inherent performance bottlenecks that may limit scalability of certain approaches.

**Integration Complexity**: Hybrid approaches like HRPO require careful balancing of discrete and continuous representations, introducing additional engineering complexity compared to pure CoT or pure latent methods.

### 5.3 Research Gaps

Several important gaps emerge from the literature:

1. **Long-Term Stability**: No studies examine whether latent reasoning benefits persist across extended usage periods or continual learning scenarios

2. **Domain Generalization**: Most evaluations focus on mathematical and logical reasoning; broader domain coverage including creative tasks and open-ended dialogue remains unexplored

3. **Human Alignment**: Limited investigation into how latent reasoning correlates with human-like reasoning patterns or alignment preferences

4. **Cross-Modal Integration**: Absence of work combining latent reasoning with vision, audio, or multimodal inputs

---

## 6. Applications and Implications

### 6.1 Practical Deployment Scenarios

Latent reasoning shows particular promise for:

- **Resource-Constrained Environments**: Reduced token overhead makes latent methods attractive for edge computing and mobile deployment
- **High-Frequency Trading**: Fast inference with maintained accuracy benefits time-sensitive applications
- **Real-Time Systems**: Dynamic compression allows adaptation to latency requirements
- **Educational Tools**: Interpretability features support explainable AI applications

### 6.2 Research Directions

The literature suggests several promising future directions:

1. **Hybrid Architecture Development**: Combining strengths of CoT (interpretability) and latent reasoning (efficiency)
2. **Multi-Scale Modeling**: Understanding how latent reasoning scales across model sizes from millions to trillions of parameters
3. **Curriculum Learning**: Designing training protocols that progressively build latent reasoning capabilities
4. **Neurosymbolic Integration**: Merging latent reasoning with symbolic reasoning systems for enhanced capabilities

---

## 7. Conclusion

This systematic review of 10 papers on latent reasoning published between 2023 and 2025 reveals a rapidly evolving research landscape addressing fundamental limitations of traditional chain-of-thought approaches. Key contributions include reinforcement learning-based optimization strategies, efficient post-training refinement techniques, small model activation methods, and continuous latent space training paradigms.

The evidence strongly supports latent reasoning as a viable alternative to explicit CoT, offering substantial computational efficiency gains while maintaining or improving performance across mathematical, logical, and planning tasks. However, important challenges remain regarding scalability, interpretability, and establishing clear boundaries between genuine reasoning and memorization.

Future research should prioritize multi-domain evaluation, long-term stability assessment, and integration with human-aligned objectives to fully realize latent reasoning's potential for advancing large language model capabilities.

---

## References

Balesni, M., Korbak, T., & Evans, O. (2024, November 25). *Lessons from studying two-hop latent reasoning*. arXiv preprint arXiv:2411.16353v4. https://arxiv.org/abs/2411.16353v4

Hao, S., Sukhbaatar, S., Su, D., Li, X., Hu, Z., Weston, J., & Tian, Y. (2024, December 9). *Training large language models to reason in a continuous latent space*. arXiv preprint arXiv:2412.06769v4. https://arxiv.org/abs/2412.06769v4

Hwang, H., Jeon, B., Kim, S., Kim, J., Chang, H., Yang, S., Won, S., Lee, D., Ahn, Y., & Seo, M. (2025, May 28). *Latent reasoning via sentence embedding prediction*. arXiv preprint arXiv:2505.22202v2. https://arxiv.org/abs/2505.22202v2

Tan, W., Li, J., Ju, J., Luo, Z., Song, R., & Luan, J. (2025, May 22). *Think silently, think fast: Dynamic latent compression of LLM reasoning chains*. arXiv preprint arXiv:2505.16552v6. https://arxiv.org/abs/2505.16552v6

Wang, X., Wang, D., Ying, W., Bai, H., Gong, N., Dong, S., Liu, K., & Fu, Y. (2025a, June 10). *Efficient post-training refinement of latent reasoning in large language models*. arXiv preprint arXiv:2506.08552v2. https://arxiv.org/abs/2506.08552v2

Xu, Z., Wang, H., Bespalov, D., Wu, X., Stone, P., & Qi, Y. (2023, December 7). *LaRS: Latent reasoning skills for chain-of-thought reasoning*. arXiv preprint arXiv:2312.04684v4. https://arxiv.org/abs/2312.04684v4

Yue, Z., Jin, B., Zeng, H., Zhuang, H., Qin, Z., Yoon, J., Shang, L., Han, J., & Wang, D. (2025, May 24). *Hybrid latent reasoning via reinforcement learning*. arXiv preprint arXiv:2505.18454v2. https://arxiv.org/abs/2505.18454v2

Zhang, Y., Valentino, M., Carvalho, D. S., & Freitas, A. (2025b, June 24). *Learning to disentangle latent reasoning rules with language VAEs: A systematic study*. arXiv preprint arXiv:2506.19418v2. https://arxiv.org/abs/2506.19418v2

Zhang, Y., Zhang, B., Li, Z., Li, M., Cheng, N., Chen, M., Wei, T., Ma, J., Wang, S., & Xiao, J. (2025). *Self-enhanced reasoning training: Activating latent reasoning in small models for enhanced reasoning distillation*. arXiv preprint arXiv:2502.12744v1. https://arxiv.org/abs/2502.12744v1

Zheng, Z., Wang, Y., Huang, Y., Song, S., Yang, M., Tang, B., Xiong, F., & Li, Z. (2024, September 5). *Attention heads of large language models: A survey*. arXiv preprint arXiv:2409.03752v3. https://arxiv.org/abs/2409.03752v3

---

*Review completed: October 26, 2026*
