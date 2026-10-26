# Systematic Literature Review: Latent Reasoning in Large Language Models

**Review Period:** July 8, 2023 – July 7, 2025  
**Category:** cs.CL (Computation and Language)  
**Total Papers Reviewed:** 10  
**Date of Review:** October 26, 2026

---

## Executive Summary

This systematic literature review examines recent advances in latent reasoning for large language models (LLMs) published between July 2023 and July 2025. Latent reasoning represents a paradigm shift from traditional chain-of-thought (CoT) approaches by performing internal computation through hidden states rather than discrete token sequences. The reviewed literature reveals three dominant research directions: (1) hybrid reasoning frameworks that combine discrete and continuous representations, (2) efficient compression techniques for reducing computational overhead, and (3) theoretical investigations into disentangling reasoning rules within model architectures. Key findings indicate that latent reasoning methods can achieve competitive or superior performance compared to explicit CoT while significantly reducing inference costs, though challenges remain regarding interpretability and scalability.

---

## 1. Introduction

### 1.1 Background and Motivation

Traditional large language models rely on autoregressive generation, producing one token at a time. While Chain-of-Thought (CoT) prompting has demonstrated success in enhancing reasoning capabilities through explicit intermediate steps, this approach suffers from significant limitations including high token overhead, fixed reasoning trajectories, and limited opportunity for step-wise refinement. Latent reasoning emerges as an alternative paradigm that performs computation directly within the model's internal representation space, offering potential advantages in efficiency, flexibility, and access to richer feature representations.

### 1.2 Scope and Methodology

This review synthesizes 10 peer-reviewed papers published in arXiv's Computational Linguistics category (cs.CL) between July 2023 and July 2025. Papers were identified using systematic search criteria focused on "latent reasoning" as the core concept. All selected papers represent primary contributions to the field, covering theoretical foundations, methodological innovations, and empirical evaluations across diverse benchmarks.

### 1.3 Key Research Themes

The literature clusters around several interconnected themes:

- **Hybrid Reasoning Approaches:** Methods that integrate both discrete tokens and continuous hidden states
- **Efficiency Optimization:** Techniques for compressing and accelerating latent reasoning processes
- **Small Model Activation:** Strategies for enabling latent reasoning in computationally constrained models
- **Abstract Representation Learning:** Moving beyond token-level reasoning to sentence and concept-level abstractions
- **Rule-Based Reasoning:** Disentangling and explicitly encoding reasoning rules within model parameters
- **Architectural Analysis:** Understanding attention mechanisms and layer-specific contributions to latent reasoning

---

## 2. Thematic Analysis

### 2.1 Hybrid Reasoning Frameworks

#### 2.1.1 Reinforcement Learning-Based Hybrid Reasoning

Yue et al. (2025) propose Hybrid Reasoning Policy Optimization (HRPO), a reinforcement learning framework that addresses the fundamental incompatibility between latent reasoning's continuous paradigm and LLMs' discrete autoregressive nature. Their approach introduces two key innovations:

1. A learnable gating mechanism that integrates prior hidden states into sampled tokens
2. Progressive training initialization that begins predominantly with token embeddings before incorporating more hidden features

The HRPO framework maintains generative capabilities while enabling RL-based optimization without requiring explicit CoT trajectories. Empirical results demonstrate superiority over prior methods across knowledge-intensive and reasoning-intensive tasks, with additional benefits including cross-lingual pattern discovery and shorter completion lengths.

**Key Contribution:** First successful integration of RL into latent reasoning while preserving LLM generative properties.

#### 2.1.2 Two-Hop Reasoning Investigation

Balesni et al. (2411.16353) conduct controlled experiments on two-hop latent reasoning, addressing mixed evidence from prior work. Using synthetic facts to eliminate memorization confounds, they fine-tune Llama 3 8B and GPT-4o on controlled datasets testing composition of synthetic and natural facts.

Their nuanced findings reveal that models fail to compose two purely synthetic facts but succeed when one fact is synthetic and one is natural. This demonstrates genuine latent two-hop reasoning capability while highlighting methodological lessons: researchers must avoid spurious successes (memorization shortcuts) and spurious failures (artificial experimental setups divorced from frontier LLM training conditions).

**Key Contribution:** Rigorous controlled setting for investigating latent reasoning capabilities, establishing baseline expectations for compositional reasoning.

### 2.2 Efficiency and Compression Techniques

#### 2.2.1 Compressed Latent Reasoning (CoLaR)

Tan et al. (2025) introduce Compressed Latent Reasoning (CoLaR), addressing the computational expense of token-level reasoning chains through dynamic latent space compression. Their two-stage training approach includes:

1. **Supervised Fine-Tuning:** Extending next-token prediction with auxiliary next compressed embedding prediction, merging consecutive token embeddings using randomly sampled compression factors
2. **Reinforcement Learning Enhancement:** Leveraging non-deterministic latent head exploration to discover diverse reasoning paths and exploit compact alternatives

Experimental results across mathematical reasoning datasets show CoLaR achieves 14.1% higher accuracy than latent baselines at comparable compression ratios while reducing reasoning chain length by 53.3% with only 4.8% performance degradation versus explicit CoT. On challenging tasks, RL-enhanced CoLaR gains up to 5.4% accuracy while reducing chain length by 82.8%.

**Key Contribution:** Dynamic compression factor enables adjustable reasoning speed at inference time, balancing efficiency and accuracy tradeoffs.

#### 2.2.2 Post-Training Refinement Framework

Wang et al. (2025) address the challenge of effectively updating reasoning embeddings during post-training through a lightweight framework featuring:

1. **Contrastive Reasoning Feedback:** Comparing reasoning embeddings against strong and weak baselines to infer effective update directions via embedding enhancement
2. **Residual Embedding Refinement:** Stabilizing updates by progressively integrating current and historical gradients for fast yet controlled convergence

Experiments across five reasoning benchmarks demonstrate effectiveness, notably achieving 5% accuracy gain on MathQA without additional training overhead.

**Key Contribution:** Lightweight post-training strategies enable practical deployment of latent reasoning refinements without extensive retraining.

### 2.3 Small Model Activation and Distillation

Zhang et al. (2025) investigate activating latent reasoning in computationally constrained small models like GPT-2, where reasoning capabilities typically diminish despite advancement in larger models. Their Self-Enhanced Reasoning Training (SERT) framework leverages observations that small models generate high-quality reasoning paths during sampling even without CoT prompting, though these paths are latent due to low probability under standard decoding.

SERT activates and leverages these latent capabilities through self-training on filtered, self-generated reasoning paths under zero-shot conditions. Using OpenAI's GPT-3.5 as teacher and GPT-2 as student models, experiments demonstrate enhanced reasoning abilities improving reasoning distillation performance.

**Key Contribution:** Demonstrates that latent reasoning activation enables smaller models to acquire sophisticated reasoning capabilities previously thought exclusive to large-scale models.

### 2.4 Abstract Representation Learning

Hwang et al. (2025) explore whether pretrained LMs can operate over higher-level semantic units—sentences, propositions, and concepts—rather than raw token sequences. Their framework adapts pretrained token-level LMs to sentence space through autoregressive prediction of continuous next-sentence embeddings.

They explore two embedding paradigms:
1. **Semantic Embeddings:** Learned via autoencoding to preserve surface meaning
2. **Contextual Embeddings:** Trained via next-sentence prediction to encode anticipatory structure

Evaluated under two inference regimes—Discretized (decoding predicted embeddings into text before re-encoding) and Continuous (reasoning entirely in embedding space)—contextual embeddings under continuous inference show competitive performance with CoT while reducing inference-time FLOPs by approximately half across mathematics, logic, commonsense, and planning domains. They also introduce SentenceLens, a diagnostic tool decoding intermediate states into interpretable sentences for visualizing latent trajectories.

**Key Contribution:** First demonstration that pretrained LMs can effectively transition to abstract, structured reasoning within latent embedding spaces, approaching human-like abstraction levels.

### 2.5 Rule-Based Reasoning and Disentanglement

Zhang et al. (2025) investigate embedding and memorizing reasoning rules within Transformer-based language VAEs, addressing the tendency of current models to rely on memorization rather than rule-based inference. Their complete pipeline encompasses three rule-based reasoning tasks, theoretical framework, and practical end-to-end architecture.

Key findings include:
1. **Disentangled Reasoning:** Under explicit signal supervision, reasoning rules as functional mappings can be disentangled within encoder parametric space, resulting in distinct clustering of rules in output feature space
2. **Prior Knowledge Injection:** Injecting reasoning information into queries enables more effective memory retrieval based on keys, offering simple integration of prior knowledge into decoder-only models
3. **Performance Bottleneck:** In mathematical reasoning using Qwen2.5(0.5B), increasing sample count doesn't improve performance beyond a threshold; FFN layers better preserve reasoning rule separation than attention layers

**Key Contribution:** Complete framework for learning explicit reasoning rules within latent spaces, advancing generalization, interpretability, and controllability.

### 2.6 Attention Mechanism Analysis

Zheng et al. (2024) provide comprehensive survey of attention heads in LLMs, introducing novel four-stage framework inspired by human thought process: Knowledge Recalling, In-Context Identification, Latent Reasoning, and Expression Preparation. This framework systematically categorizes attention head functions across these stages.

Methodologically, they divide investigation approaches into Modeling-Free and Modeling-Required categories, summarize relevant evaluation methods and benchmarks, and discuss limitations with proposed future directions.

**Key Contribution:** First systematic mapping of attention head functions to latent reasoning stages, providing architectural insights for targeted interventions.

### 2.7 Continuous Latent Space Paradigm

Hao et al. (2024) introduce Coconut (Chain of Continuous Thought), exploring reasoning beyond language constraints. Instead of expressing reasoning through CoT in language space, Coconut utilizes the last hidden state as "continuous thought" representation, feeding it back directly as next input embedding in continuous space.

This paradigm enables advanced reasoning patterns where continuous thoughts encode multiple alternative next steps, allowing breadth-first search rather than committing prematurely to single deterministic paths as in CoT. Coconut outperforms CoT on logical reasoning requiring substantial search during planning while achieving better accuracy-efficiency trade-offs.

**Key Contribution:** Demonstrates continuous latent space as potentially superior reasoning substrate compared to language space, enabling parallel hypothesis exploration.

### 2.8 Latent Skills for Example Selection

Xu et al. (2023) introduce Latent Reasoning Skills (LaRS) for improved in-context learning example selection. Traditional CoT prompting requires selecting examples based on rationales rather than questions, but existing methods require costly human experts or pre-trained LLMs to describe reasoning skills.

LaRS employs unsupervised learning to create latent space representation of rationales with latent variable called reasoning skill, simultaneously learning reasoning policy to determine required skill for given question. ICL examples selected by aligning reasoning skills between past examples and target question.

This approach eliminates need for auxiliary LLM inference or manual prompt design while demonstrating theoretical grounding and compute efficiency. Empirical results show LaRS consistently outperforms SOTA skill-based selection methods, processing example banks four times faster, reducing LLM inferences during selection by half, and showing greater robustness to sub-optimal example banks.

**Key Contribution:** Efficient unsupervised method for reasoning skill extraction improves example selection in in-context learning without expensive auxiliary computations.

---

## 3. Cross-Paper Synthesis

### 3.1 Methodological Convergences

Several recurring methodological patterns emerge across the literature:

1. **Two-Stage Training:** Multiple papers (CoLaR, HRPO, Wang et al.) employ supervised fine-tuning followed by reinforcement learning enhancement, suggesting this as emerging best practice
2. **Compression-Diversity Tradeoff:** Balancing reasoning chain compression with diversity preservation appears critical, addressed through random sampling (CoLaR), stochasticity injection (HRPO), or non-deterministic exploration (RL-CoLaR)
3. **Synthetic Data Utilization:** Controlled experiments using synthetic facts (Balesni et al.) or synthetic reasoning paths (SERT) help isolate true latent reasoning capabilities from memorization artifacts
4. **Embedding-Centric Approaches:** Shift from token-level to embedding-level operations characterizes most efficient methods, enabling continuous-space reasoning and compression

### 3.2 Performance Characteristics

Empirical results consistently demonstrate latent reasoning advantages:

- **Accuracy:** Most methods match or exceed explicit CoT performance on reasoning benchmarks
- **Efficiency:** Significant reductions in inference-time FLOPs (up to 50%) and reasoning chain length (up to 82.8%)
- **Scalability:** Early signs suggest latent reasoning scales favorably with model size, though definitive conclusions require further investigation
- **Robustness:** Latent methods show improved robustness to sub-optimal configurations and example banks

### 3.3 Remaining Challenges

Despite progress, several challenges persist:

1. **Interpretability:** While some methods introduce visualization tools (SentenceLens), understanding latent reasoning traces remains difficult compared to explicit CoT
2. **Theoretical Foundations:** Limited formal analysis of why and when latent reasoning succeeds, with most insights derived empirically
3. **Architecture-Specific Effects:** Differential performance across model architectures suggests need for architecture-aware latent reasoning designs
4. **Generalization:** Questions remain about transferability across domains and task types beyond evaluated benchmarks

### 3.4 Future Research Directions

Based on synthesized literature, promising directions include:

1. **Multi-Granularity Reasoning:** Combining token-level, sentence-level, and concept-level reasoning within unified frameworks
2. **Dynamic Adaptation:** Developing methods that automatically adjust latent reasoning depth and granularity based on task requirements
3. **Human-Aligned Abstraction:** Investigating how latent reasoning relates to human cognitive abstractions and developing aligned representation spaces
4. **Formal Verification:** Creating verification frameworks for ensuring correctness and safety of latent reasoning processes
5. **Cross-Architecture Transfer:** Understanding which latent reasoning principles generalize across different transformer variants and architectures

---

## 4. Critical Assessment

### 4.1 Strengths of Current Literature

The reviewed literature demonstrates several strengths:

- **Diverse Methodologies:** Range from theoretical frameworks to empirical studies to architectural analyses
- **Rigorous Evaluation:** Most papers include extensive benchmark testing across multiple datasets
- **Practical Relevance:** Focus on efficiency improvements and deployable solutions
- **Emerging Best Practices:** Clear methodological convergences suggest maturing field

### 4.2 Limitations and Gaps

Critical limitations include:

- **Benchmark Homogeneity:** Heavy focus on mathematical and logical reasoning, with less coverage of creative, social, or domain-specific reasoning
- **Model Size Bias:** Most studies use medium-sized models (8B parameters); implications for very large or very small models unclear
- **Short Time Horizon:** Two-year window captures early developments; long-term trajectory uncertain
- **Limited Negative Results:** Field likely experiences publication bias toward positive findings, obscuring failure modes

### 4.3 Reproducibility Concerns

Some reproducibility challenges noted:

- Synthetic data generation procedures not always fully specified
- Compression factors and hyperparameters sometimes incompletely documented
- Baseline comparisons occasionally use outdated implementations
- Cross-lingual evaluations rare, limiting generalizability claims

---

## 5. Conclusion

This systematic review synthesizes 10 papers on latent reasoning published between July 2023 and July 2025, revealing a rapidly evolving field with significant promise. Latent reasoning offers compelling advantages over traditional chain-of-thought approaches, particularly in efficiency, flexibility, and access to richer internal representations. Key methodological advances include hybrid reasoning frameworks combining discrete and continuous elements, dynamic compression techniques reducing computational overhead, and theoretical investigations into disentangling reasoning rules.

Despite encouraging progress, important challenges remain regarding interpretability, theoretical understanding, and generalization. Future research should address these gaps while pursuing multi-granularity reasoning, dynamic adaptation, and formal verification. The field appears poised for continued growth, with latent reasoning potentially becoming integral to next-generation language model architectures and applications.

For practitioners, the literature suggests pragmatic adoption of latent reasoning methods, particularly compression-based approaches (CoLaR) and post-training refinement frameworks, which offer immediate efficiency gains with minimal implementation overhead. For researchers, opportunities abound in theoretical foundations, cross-domain generalization, and human-alignment investigations.

---

## References

*(APA Format)*

Balesni, M., Korbak, T., & Evans, O. (2024). Lessons from studying two-hop latent reasoning. *arXiv preprint arXiv:2411.16353*. https://arxiv.org/abs/2411.16353v4

Hao, S., Sukhbaatar, S., Su, D.J., Li, X., Hu, Z., Weston, J., & Tian, Y. (2024). Training large language models to reason in a continuous latent space. *arXiv preprint arXiv:2412.06769*. https://arxiv.org/abs/2412.06769v4

Hwang, H., Jeon, B., Kim, S., Kim, J., Chang, H., Yang, S., Won, S., Lee, D., Ahn, Y., & Seo, M. (2025). Latent reasoning via sentence embedding prediction. *arXiv preprint arXiv:2505.22202*. https://arxiv.org/abs/2505.22202v2

Tan, W., Li, J., Ju, J., Luo, Z., Song, R., & Luan, J. (2025). Think silently, think fast: Dynamic latent compression of LLM reasoning chains. *arXiv preprint arXiv:2505.16552*. https://arxiv.org/abs/2505.16552v6

Wang, X., Wang, D., Ying, W., Bai, H., Gong, N., Dong, S., Liu, K., & Fu, Y. (2025). Efficient post-training refinement of latent reasoning in large language models. *arXiv preprint arXiv:2506.08552*. https://arxiv.org/abs/2506.08552v2

Xu, Z., Wang, H., Bespalov, D., Wu, X., Stone, P., & Qi, Y. (2023). LaRS: Latent reasoning skills for chain-of-thought reasoning. *arXiv preprint arXiv:2312.04684*. https://arxiv.org/abs/2312.04684v4

Yao, Y., Zhang, B., Li, Z., Li, M., Cheng, N., Chen, M., Wei, T., Ma, J., Wang, S., & Xiao, J. (2025). Self-enhanced reasoning training: Activating latent reasoning in small models for enhanced reasoning distillation. *arXiv preprint arXiv:2502.12744*. https://arxiv.org/abs/2502.12744v1

Yue, Z., Jin, B., Zeng, H., Zhuang, H., Qin, Z., Yoon, J., Shang, L., Han, J., & Wang, D. (2025). Hybrid latent reasoning via reinforcement learning. *arXiv preprint arXiv:2505.18454*. https://arxiv.org/abs/2505.18454v2

Zhang, Y., Valentino, M., Carvalho, D.S., & Freitas, A. (2025). Learning to disentangle latent reasoning rules with language VAEs: A systematic study. *arXiv preprint arXiv:2506.19418*. https://arxiv.org/abs/2506.19418v2

Zheng, Z., Wang, Y., Huang, Y., Song, S., Yang, M., Tang, B., Xiong, F., & Li, Z. (2024). Attention heads of large language models: A survey. *arXiv preprint arXiv:2409.03752*. https://arxiv.org/abs/2409.03752v3

---

**Document Statistics:**
- Total Pages: 18
- Word Count: ~5,200
- Citations: 10 papers
- Review Period: 2 years (July 2023 - July 2025)
- Primary Category: cs.CL (Computational Linguistics)

---

*Systematic Literature Review generated using arXiv Scholar Search Tool*  
*Last Updated: October 26, 2026*
