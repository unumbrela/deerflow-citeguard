# Systematic Literature Review: Latent Reasoning in Language Models (2023-2025)

## Executive Summary

This systematic literature review examines 10 peer-reviewed papers published between July 8, 2023, and July 7, 2025, focusing on latent reasoning mechanisms in language models within the computer science - Computation and Language (cs.CL) category. The reviewed research explores diverse approaches to latent reasoning, including continuous latent spaces, implicit chain-of-thought methods, compression techniques, and test-time scaling strategies. Key findings indicate that latent reasoning paradigms can significantly improve reasoning accuracy while reducing computational overhead compared to traditional explicit chain-of-thought approaches.

---

## Introduction

Reasoning capabilities in large language models (LLMs) represent one of the most critical frontiers in artificial intelligence research. Traditional approaches rely heavily on explicit chain-of-thought (CoT) prompting, where models generate step-by-step textual reasoning before arriving at final answers. However, recent scholarship suggests that natural language may not always be optimal for reasoning processes, as many word tokens primarily ensure textual coherence rather than contributing essential reasoning information.

This review synthesizes advances in latent reasoning—approaches that enable models to perform reasoning computations through internal representations, continuous spaces, or compressed discrete tokens rather than explicit text generation. The selected papers span from October 2023 to February 2025, capturing the rapid evolution of this field during its formative period.

### Search Methodology

The systematic search was conducted using arXiv's scholarly database with the following parameters:
- **Query**: "Latent Reasoning" (phrase matching with all terms)
- **Category**: cs.CL (Computation and Language)
- **Date Range**: July 8, 2023 – July 7, 2025
- **Selection Criteria**: Papers must focus on latent reasoning mechanisms in language models or related cognitive architectures
- **Screening Process**: Initial pool of 50 papers expanded to 133 total candidates through citation expansion; 30 shortlisted based on relevance; 10 finally selected based on centrality scores and co-citation frequency

---

## Thematic Analysis

### Theme 1: Continuous Latent Space Reasoning

#### Coconut: Chain of Continuous Thought

Hao et al. (2024) introduced Coconut (Chain of Continuous Thought), a paradigm-shifting approach that leverages the last hidden state of LLMs as a representation of reasoning state in continuous space. Unlike traditional CoT, which decodes reasoning into discrete word tokens, Coconut feeds the continuous thought state directly back to the model as the next input embedding.

**Key Contributions:**
- Enables breadth-first search (BFS) reasoning patterns by encoding multiple alternative next steps simultaneously
- Outperforms explicit CoT on logical reasoning tasks requiring substantial planning search
- Achieves better accuracy-efficiency trade-offs

**Methodology:** The authors trained LLMs to reason entirely in continuous latent space, avoiding tokenization bottlenecks. Their experiments demonstrated that continuous thoughts can maintain rich reasoning states without the verbosity and constraints of natural language.

#### Token Assorted: Hybrid Latent-Text Representations

Su et al. (2025) extended latent reasoning concepts through Token Assorted, which mixes latent discrete tokens with traditional text tokens to create hybrid reasoning representations. Using VQ-VAE-generated latent tokens, their approach abstracts initial reasoning steps while maintaining interpretable text for later stages.

**Key Findings:**
- Significantly reduces reasoning trace length while preserving accuracy
- Random mixing training procedure enables fast adaptation to new latent tokens
- Outperformed baseline methods across logical and mathematical reasoning benchmarks

### Theme 2: Implicit Chain-of-Thought Through Knowledge Distillation

#### Implicit CoT via Vertical Reasoning

Deng et al. (2023a) explored implicit chain-of-thought reasoning through knowledge distillation, where intermediate reasoning happens "vertically" among hidden states across different layers rather than "horizontally" through sequential word generation.

**Innovations:**
- Distilled reasoning from explicit CoT-trained teacher models
- Enabled solving previously unsolvable tasks without explicit CoT
- Maintained speed comparable to no-chain-of-thought baselines
- Demonstrated on multi-digit multiplication and grade school math datasets

#### Internalizing CoT Step-by-Step

Building on this work, Deng et al. (2024) developed a progressive method for internalizing CoT steps through gradual removal of intermediate outputs during fine-tuning. Starting with explicitly CoT-trained models, they incrementally removed intermediate steps while maintaining performance.

**Results:**
- GPT-2 Small achieved 99% accuracy on 9×9 multiplication (vs. 4×4 limit with standard training)
- Mistral 7B exceeded 50% GSM8K accuracy without producing intermediate steps
- Preserved high performance while eliminating reasoning trace generation overhead

### Theme 3: Computational Delays and Pause Mechanisms

#### Think Before You Speak: Pause Tokens

Goyal et al. (2023) introduced learnable pause tokens that allow models to manipulate additional hidden vectors before committing to output tokens. This operationalizes the intuition that delayed prediction enables deeper computation.

**Empirical Findings:**
- 1B model showed gains on 8 of 9 evaluated tasks
- SQuAD EM score improved by 18%
- CommonSenseQA gained 8%
- GSM8k reasoning task improved by 1%
- Benefits require both pre-training and fine-tuning with delays

This work established the conceptual foundation for inference-time computation delays as a viable reasoning enhancement strategy.

### Theme 4: Compressed Contemplation Tokens

#### Compressed Chain-of-Thought (CCoT)

Cheng and Van Durme (2024) proposed CCoT, generating contentful continuous contemplation tokens of variable sequence length as compressed representations of explicit reasoning chains. Their framework applies to off-the-shelf decoder language models without architectural modifications.

**Advantages:**
- Enables adaptive reasoning improvements by controlling token count
- Combines efficiency of compression with effectiveness of explicit reasoning
- Provides flexible trade-off between latency and accuracy

### Theme 5: Multi-Hop Reasoning Architecture

#### Latent Multi-Hop Reasoning Investigation

Yang et al. (2024) conducted empirical investigation into whether LLMs latently perform multi-hop reasoning with complex prompts. They examined evidence of latent pathways where models identify bridge entities and utilize相关知识 to complete queries.

**Key Insights:**
- Strong evidence of latent multi-hop reasoning for certain relation types (>80% usage)
- Utilization highly contextual, varying across prompt types
- Clear scaling trend for first hop but not second hop
- Average evidence for second hop and full traversal moderate despite substantial first-hop evidence

#### Hopping Too Late: Layer-Based Limitations

Biran et al. (2024) discovered that bridge entity resolution occurs in early transformer layers, while two-hop query solving happens in later layers. This temporal separation creates potential limitations when later layers lack necessary knowledge.

**Novel Contribution:** Back-patching analysis method revealed that up to 66% of incorrect cases could be corrected by patching later-layer representations to earlier layers, demonstrating that some failures stem from late-layer knowledge gaps rather than early-stage reasoning errors.

### Theme 6: Test-Time Scaling Strategies

#### DeepSeek-R1: RL-Incentivized Reasoning

DeepSeek-AI et al. (2025) demonstrated that pure reinforcement learning can incentivize advanced reasoning capabilities without human-labeled trajectories. Their framework facilitates emergent development of self-reflection, verification, and dynamic strategy adaptation.

**Performance Highlights:**
- Surpasses counterparts trained via conventional supervised learning
- Superior performance on verifiable tasks (mathematics, coding competitions, STEM)
- Emergent patterns guide smaller model enhancement

#### s1: Simple Test-Time Scaling

Muennighoff et al. (2025) developed minimalist test-time scaling through budget forcing—forcefully terminating or extending thinking processes by appending "Wait" tokens. Their Qwen2.5-32B-Instruct model (s1-32B) exceeded o1-preview on competition math by up to 27%.

**Core Innovations:**
- Small curated dataset (s1K) of 1,000 questions with quality reasoning traces
- Budget forcing controls test-time compute dynamically
- Open-source implementation enables reproducibility

---

## Comparative Analysis

### Performance Metrics Across Approaches

| Approach | Accuracy Improvement | Efficiency Gain | Primary Use Case |
|----------|---------------------|-----------------|------------------|
| Coconut (continuous) | Substantial on planning tasks | Better trade-off | Complex logical reasoning |
| Implicit CoT (vertical) | Solves previously unsolvable tasks | Comparable to no-CoT | Math problems |
| Pause Tokens | Up to 18% on QA tasks | Moderate overhead | General reasoning |
| Compressed CoT | Adaptive based on token count | Significant reduction | Latency-sensitive applications |
| Token Assorted | Consistent outperformance | Reduced trace length | Mixed interpretability needs |
| Test-Time Scaling | Up to 27% on competition math | Variable | High-stakes reasoning |

### Convergence Patterns

Several convergent themes emerge across these works:

1. **Internal Computation Over External Generation**: Multiple studies demonstrate that reasoning performed internally (through hidden states, continuous representations, or compressed tokens) often outperforms explicit text-based reasoning.

2. **Compression Without Sacrifice**: Techniques like CCoT and Token Assorted achieve significant compression while maintaining or improving accuracy, suggesting redundancy in explicit CoT.

3. **Test-Time Compute Flexibility**: Both pause tokens and budget forcing demonstrate that allocating additional computation during inference improves outcomes, challenging fixed-compute assumptions.

4. **Layer-Specific Reasoning Roles**: Research on multi-hop reasoning reveals distinct computational roles across transformer layers, informing future architecture design.

---

## Critical Evaluation

### Strengths

**Methodological Rigor**: Selected papers employ diverse evaluation methodologies including ablation studies, comparative benchmarks, and novel analysis techniques like back-patching.

**Practical Impact**: Many approaches show tangible improvements on real-world tasks (GSM8K, SQuAD, AIME competition math), demonstrating applicability beyond toy problems.

**Open Science Commitment**: Notable open-source contributions (s1, Coconut variants) facilitate community replication and extension.

### Limitations

**Task Scope**: Many evaluations focus predominantly on mathematical and logical reasoning, with less emphasis on creative or ambiguous reasoning domains.

**Scalability Questions**: While impressive on medium-scale models (7B-32B), extrapolation to massive models requires further investigation.

**Interpretability Trade-offs**: Continuous and compressed representations sacrifice some interpretability compared to explicit CoT, creating tension between efficiency and explainability.

### Unresolved Questions

1. What determines optimal latent vs. explicit reasoning boundaries for different task types?
2. How do latent reasoning capabilities transfer across domains and modalities?
3. Can latent reasoning approaches be combined effectively, or do they compete?
4. What are the safety implications of reasoning processes that are difficult to inspect?

---

## Future Directions

Based on current trends, several promising research avenues emerge:

### Architectural Innovations
- Hybrid models combining latent and explicit reasoning components
- Layer-adaptive reasoning allocation based on task complexity
- Cross-modal latent reasoning extensions

### Training Paradigms
- Self-supervised latent reasoning discovery
- Curriculum learning for progressive internalization
- Multi-objective optimization balancing accuracy, efficiency, and interpretability

### Evaluation Frameworks
- Standardized benchmarks for latent reasoning capabilities
- Diagnostic tools for analyzing internal reasoning states
- Longitudinal studies tracking reasoning capability emergence

### Application Domains
- Scientific discovery and hypothesis generation
- Complex planning and decision-making systems
- Educational AI tutors with transparent reasoning

---

## Conclusion

The ten papers reviewed here collectively establish latent reasoning as a robust and multifaceted research domain with significant practical implications. From continuous latent spaces to compressed contemplation tokens, from vertical hidden-state reasoning to test-time scaling, these approaches demonstrate that reasoning need not be confined to explicit textual generation.

The convergence toward internal computation strategies suggests fundamental insights about how language models process information. Rather than viewing CoT as merely a prompting technique, emerging evidence positions it as one option among many for allocating computational resources across time and representation spaces.

As the field progresses, key challenges remain around establishing theoretical foundations, developing unified frameworks, and ensuring that efficiency gains do not come at the cost of reliability or interpretability. Nevertheless, the trajectory is clear: latent reasoning represents a crucial pathway toward more capable, efficient, and ultimately more human-like machine intelligence.

---

## References

Biran, E., Gottesman, D., Yang, S., Geva, M., & Globerson, A. (2024). Hopping too late: Exploring the limitations of large language models on multi-hop queries. *arXiv preprint arXiv:2406.12775*. https://arxiv.org/abs/2406.12775v2

Cheng, J., & Van Durme, B. (2024). Compressed chain of thought: Efficient reasoning through dense representations. *arXiv preprint arXiv:2412.13171*. https://arxiv.org/abs/2412.13171v1

DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., ... Liu, A. (2025). DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. *arXiv preprint arXiv:2501.12948*. https://arxiv.org/abs/2501.12948v2

Deng, Y., Prasad, K., Fernandez, R., Smolensky, P., Chaudhary, V., & Shieber, S. (2023a). Implicit chain of thought reasoning via knowledge distillation. *arXiv preprint arXiv:2311.01460*. https://arxiv.org/abs/2311.01460v1

Deng, Y., Choi, Y., & Shieber, S. (2024). From explicit CoT to implicit CoT: Learning to internalize CoT step by step. *arXiv preprint arXiv:2405.14838*. https://arxiv.org/abs/2405.14838v1

Goyal, S., Ji, Z., Rawat, A. K., Menon, A. K., Kumar, S., & Nagarajan, V. (2023). Think before you speak: Training language models with pause tokens. *arXiv preprint arXiv:2310.02226*. https://arxiv.org/abs/2310.02226v3

Hao, S., Sukhbaatar, S., Su, D., Li, X., Hu, Z., Weston, J., & Tian, Y. (2024). Training large language models to reason in a continuous latent space. *arXiv preprint arXiv:2412.06769*. https://arxiv.org/abs/2412.06769v4

Muennighoff, N., Yang, Z., Shi, W., Li, X. L., Fei-Fei, L., Hajishirzi, H., Zettlemoyer, L., Liang, P., Candès, E., & Hashimoto, T. (2025). s1: Simple test-time scaling. *arXiv preprint arXiv:2501.19393*. https://arxiv.org/abs/2501.19393v3

Su, D., Zhu, H., Xu, Y., Jiao, J., Tian, Y., & Zheng, Q. (2025). Token assorted: Mixing latent and text tokens for improved language model reasoning. *arXiv preprint arXiv:2502.03275*. https://arxiv.org/abs/2502.03275v2

Yang, S., Gribovskaya, E., Kassner, N., Geva, M., & Riedel, S. (2024). Do large language models latently perform multi-hop reasoning? *arXiv preprint arXiv:2402.16837*. https://arxiv.org/abs/2402.16837v2

---

## Appendix: Screening Statistics

- **Initial Pool Identified**: 50 papers
- **Added from Citation Expansion**: 83 papers  
- **Shortlisted Candidates**: 30 papers
- **Final Selection**: 10 papers
- **Included from References**: 6 papers

**Score Distribution During Screening:**
- Score 0 (lowest relevance): 3 papers
- Score 1: 5 papers
- Score 2: 4 papers
- Score 3 (highest relevance): 18 papers

---

*Review completed on October 26, 2026*
*Systematic literature review following PRISMA-inspired methodology*
