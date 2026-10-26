# Systematic Literature Review: Negative Sampling Techniques in Information Retrieval

## Executive Summary

This systematic literature review examines negative sampling techniques in information retrieval, focusing on papers published between January 9, 2024, and January 8, 2026, in the cs.IR category. The search identified 26 papers through arXiv, with citation expansion adding 42 additional references, resulting in a shortlist of 30 papers. After screening for centrality to negative sampling techniques, **6 papers** were selected for this review. Notably, fewer papers than the requested 10 met the inclusion criteria under the specified constraints, indicating that negative sampling remains a specialized but active research area within information retrieval.

## Methodology

### Search Strategy
- **Database**: arXiv preprint repository
- **Category**: cs.IR (Information Retrieval)
- **Date Range**: January 9, 2024 – January 8, 2026
- **Search Query**: "negative sampling techniques"
- **Inclusion Criteria**: Papers focusing on negative sampling methods, techniques, and approaches specifically in information retrieval contexts
- **Screening Process**: Automated scoring based on co-citation centrality and relevance to the topic

### Screening Results
- Initial pool: 26 papers
- After citation expansion: 68 papers (26 + 42 from references)
- Shortlisted: 30 papers
- Screened and scored: 30 papers
- **Final inclusion: 6 papers**

The screening revealed that while 30 papers were shortlisted, only 6 received high centrality scores (score ≥1), with the majority (24 papers) receiving the lowest score of 0, indicating limited focus on negative sampling as a primary contribution.

---

## Included Studies

### 1. Adaptive Hardness Negative Sampling for Collaborative Filtering

**Citation (APA)**:  
Lai, R., Chen, R., Han, Q., Zhang, C., & Chen, L. (2024). Adaptive hardness negative sampling for collaborative filtering. *arXiv preprint arXiv:2401.05191*. https://arxiv.org/abs/2401.05191v1

**Summary**:  
This paper addresses a critical limitation in existing negative sampling methods for collaborative filtering: the inability to select negative samples at varying hardness levels, leading to false positive and false negative problems. The authors propose Adaptive Hardness Negative Sampling (AHNS), a new paradigm with three key criteria that adaptively selects negative samples with appropriate hardness during training. They present a concrete instantiation, AHNS_{p<0}, and provide theoretical demonstration of its superior performance bounds. Comprehensive experiments show consistent and substantial improvements over state-of-the-art competitors across multiple datasets.

**Key Contributions**:
- Identification of fixed hardness limitation in existing methods
- Theoretical framework for adaptive hardness sampling
- Practical instantiation with provable performance bounds

---

### 2. TriSampler: A Better Negative Sampling Principle for Dense Retrieval

**Citation (APA)**:  
Yang, Z., Shao, Z., Dong, Y., & Tang, J. (2024). TriSampler: A better negative sampling principle for dense retrieval. *arXiv preprint arXiv:2402.11855*. https://arxiv.org/abs/2402.11855v1

**Summary**:  
This work provides theoretical analysis of negative sampling in dense retrieval, introducing the quasi-triangular principle that elucidates the triangular-like interplay between query, positive document, and negative document. Based on this principle, the authors develop TriSampler, a method that selectively samples more informative negatives within a constrained region. Experimental evaluation demonstrates consistently superior retrieval performance across diverse representative retrieval models.

**Key Contributions**:
- Theoretical quasi-triangular principle for negative sampling
- Constrained region sampling for informative negatives
- Empirical validation across multiple retrieval models

---

### 3. Enhancing Retrieval Performance: An Ensemble Approach For Hard Negative Mining

**Citation (APA)**:  
Meghwani, H. (2024). Enhancing retrieval performance: An ensemble approach for hard negative mining. *arXiv preprint arXiv:2411.02404*. https://arxiv.org/abs/2411.02404v1

**Summary**:  
This study focuses on the crucial role of hard negatives in training cross-encoder models, explaining performance gains observed with hard negative sampling compared to random sampling. The author develops a robust hard negative mining technique for efficient training of cross-encoder re-rank models on enterprise datasets with domain-specific context. The approach demonstrates that learning both similarity and dissimilarity simultaneously with cross-encoders improves retrieval system performance, with implications for advanced LLM systems like Retrieval-Augmented Generation (RAG) and Reasoning and Action Agents (ReAct).

**Key Contributions**:
- Explanation of hard negative benefits in cross-encoder training
- Novel ensemble approach for hard negative mining
- Application to enterprise domain-specific contexts
- Connection to RAG and ReAct systems

---

### 4. NV-Retriever: Improving Text Embedding Models with Effective Hard-Negative Mining

**Citation (APA)**:  
Moreira, G. de S. P., Osmulski, R., Xu, M., Ak, R., Schifferer, B., & Oldridge, E. (2024). NV-Retriever: Improving text embedding models with effective hard-negative mining. *arXiv preprint arXiv:2407.15831*. https://arxiv.org/abs/2407.15831v2

**Summary**:  
This paper introduces a family of positive-aware mining methods that use positive relevance scores as anchors for effective false negative removal in text embedding models. The authors provide an ablation study on hard-negative mining methods, exploring different teacher and base model configurations. The proposed methods are demonstrated at scale with the NV-Retriever-v1 model, which achieved 60.9 on the MTEB Retrieval (BEIR) benchmark and ranked 1st upon publication in July 2024.

**Key Contributions**:
- Positive-aware mining methods for false negative removal
- Comprehensive ablation study of mining configurations
- State-of-the-art performance on MTEB Retrieval benchmark
- Faster training with more accurate retrieval models

---

### 5. Understanding the Role of Cross-Entropy Loss in Fairly Evaluating Large Language Model-based Recommendation

**Citation (APA)**:  
Xu, C., Zhu, Z., Wang, J., Wang, J., & Zhang, W. (2024). Understanding the role of cross-entropy loss in fairly evaluating large language model-based recommendation. *arXiv preprint arXiv:2402.06216*. https://arxiv.org/abs/2402.06216v2

**Summary**:  
While primarily focused on evaluation methodology, this paper addresses negative sampling implicitly through its analysis of cross-entropy loss with full softmax versus pointwise/pairwise loss functions in LLM-based recommendation. The authors theoretically justify the superiority of cross-entropy and demonstrate it can be adequately replaced by elementary approximations with necessary modifications. Results across three public datasets show that existing LLM-based methods are not as effective as claimed for next-item recommendation when evaluated objectively.

**Key Contributions**:
- Theoretical analysis of loss functions related to negative sampling
- Fair evaluation framework for LLM-based recommendation
- Empirical demonstration of evaluation biases
- Practical approximations for cross-entropy loss

---

### 6. SCONE: A Novel Stochastic Sampling to Generate Contrastive Views and Hard Negative Samples for Recommendation

**Citation (APA)**:  
Lee, C., Choi, J., Wi, H., Cho, S.-B., & Park, N. (2024). SCONE: A novel stochastic sampling to generate contrastive views and hard negative samples for recommendation. *arXiv preprint arXiv:2405.00287*. https://arxiv.org/abs/2405.00287v2

**Summary**:  
This paper proposes SCONE, a novel stochastic sampling approach for generating both dynamic augmented views and diverse hard negative samples in graph-based collaborative filtering. Based on score-based generative models, SCONE addresses data sparsity and negative sampling challenges through a unified approach. Extensive experiments on 6 benchmark datasets show consistent outperformance of state-of-the-art baselines. The method demonstrates particular efficacy in addressing user sparsity and item popularity issues, enhancing performance for cold-start users and long-tail items while improving recommendation diversity and representation uniformity.

**Key Contributions**:
- Unified stochastic sampling for contrastive views and hard negatives
- Score-based generative model foundation
- Improved performance for cold-start and long-tail scenarios
- Enhanced diversity and uniformity of representations

---

## Thematic Analysis

### Theme 1: Adaptive and Dynamic Sampling Strategies

Three papers emphasize the importance of adaptive sampling strategies that go beyond fixed hardness levels. Lai et al. (2024) introduce AHNS, which adaptively selects negative samples with appropriate hardness during training. Yang et al. (2024) propose TriSampler with constrained region sampling based on the quasi-triangular principle. Lee et al. (2024) develop SCONE with dynamic stochastic sampling. This trend reflects recognition that static negative sampling approaches are insufficient for complex retrieval scenarios.

### Theme 2: Hard Negative Mining

All six papers address hard negative mining to varying degrees, with particular emphasis from Meghwani (2024) and Moreira et al. (2024). The consensus is that hard negatives—samples that are difficult to distinguish from positives—provide more informative training signals than random negatives. Moreira et al. (2024) specifically address false negative removal through positive-aware mining, while Meghwani (2024) focuses on ensemble approaches for cross-encoder training.

### Theme 3: Theoretical Foundations

Several papers provide theoretical underpinnings for their methods. Lai et al. (2024) demonstrate theoretical performance bounds for AHNS_{p<0}. Yang et al. (2024) establish the quasi-triangular principle through theoretical analysis. Xu et al. (2024) provide theoretical justification for cross-entropy loss superiority. This theoretical grounding distinguishes recent work from earlier heuristic approaches.

### Theme 4: Application Domains

The reviewed papers span multiple application domains within information retrieval:
- **Collaborative Filtering**: Lai et al. (2024), Lee et al. (2024)
- **Dense Retrieval**: Yang et al. (2024), Moreira et al. (2024)
- **Cross-Encoder Re-ranking**: Meghwani (2024)
- **LLM-based Recommendation**: Xu et al. (2024)
- **Text Embedding Models**: Moreira et al. (2024)

This diversity demonstrates the cross-cutting importance of negative sampling across IR subdomains.

### Theme 5: Connection to Large Language Models

Three papers explicitly connect negative sampling to LLM applications. Meghwani (2024) discusses implications for RAG and ReAct systems. Moreira et al. (2024) focus on text embedding models for semantic search and QA systems based on RAG. Xu et al. (2024) critically evaluate LLM-based recommendation methods. This reflects the growing integration of negative sampling techniques with LLM-powered retrieval systems.

---

## Research Gaps and Future Directions

### Identified Gaps

1. **Limited Temporal Coverage**: The search identified only 6 highly relevant papers within the specified date range, suggesting either limited research activity or分散ed publication venues outside cs.IR.

2. **Evaluation Standardization**: While multiple papers propose new methods, there is limited discussion of standardized evaluation protocols for comparing negative sampling techniques across different retrieval tasks.

3. **Computational Efficiency**: Most papers focus on effectiveness rather than computational efficiency of negative sampling, which is critical for large-scale deployment.

4. **Cross-Domain Generalization**: Limited investigation of how negative sampling techniques transfer across different domains and application contexts.

### Future Research Directions

1. **Unified Frameworks**: Development of unified theoretical frameworks that can encompass diverse negative sampling approaches across different retrieval paradigms.

2. **Efficiency-Effectiveness Trade-offs**: Systematic investigation of computational costs versus performance gains for different negative sampling strategies.

3. **LLM Integration**: Deeper exploration of negative sampling for training and evaluating LLM-based retrieval systems, particularly for RAG applications.

4. **Adaptive Curriculum Learning**: Extension of adaptive hardness concepts to curriculum learning approaches that progressively increase negative sample difficulty.

5. **Multi-Modal Retrieval**: Application of advanced negative sampling techniques to multi-modal retrieval scenarios involving text, images, and other modalities.

---

## Conclusion

This systematic literature review reveals that negative sampling remains an active and important research area within information retrieval, with significant advances in adaptive sampling strategies, hard negative mining, and theoretical foundations. The six included papers demonstrate consistent themes around dynamic sampling, theoretical grounding, and application to modern LLM-based systems.

However, the limited number of highly central papers (6 out of 30 shortlisted, compared to the requested 10) suggests that negative sampling research may be either: (1) concentrated in a smaller community of specialists, (2) published in venues outside the cs.IR category, or (3) integrated as components of larger systems rather than studied as primary contributions.

The field would benefit from increased standardization of evaluation protocols, greater attention to computational efficiency, and deeper exploration of negative sampling for emerging LLM-based retrieval paradigms. The theoretical foundations established in recent work provide a strong basis for future advances in this critical area of information retrieval.

---

## References

Lai, R., Chen, R., Han, Q., Zhang, C., & Chen, L. (2024). Adaptive hardness negative sampling for collaborative filtering. *arXiv preprint arXiv:2401.05191*. https://arxiv.org/abs/2401.05191v1

Lee, C., Choi, J., Wi, H., Cho, S.-B., & Park, N. (2024). SCONE: A novel stochastic sampling to generate contrastive views and hard negative samples for recommendation. *arXiv preprint arXiv:2405.00287*. https://arxiv.org/abs/2405.00287v2

Meghwani, H. (2024). Enhancing retrieval performance: An ensemble approach for hard negative mining. *arXiv preprint arXiv:2411.02404*. https://arxiv.org/abs/2411.02404v1

Moreira, G. de S. P., Osmulski, R., Xu, M., Ak, R., Schifferer, B., & Oldridge, E. (2024). NV-Retriever: Improving text embedding models with effective hard-negative mining. *arXiv preprint arXiv:2407.15831*. https://arxiv.org/abs/2407.15831v2

Xu, C., Zhu, Z., Wang, J., Wang, J., & Zhang, W. (2024). Understanding the role of cross-entropy loss in fairly evaluating large language model-based recommendation. *arXiv preprint arXiv:2402.06216*. https://arxiv.org/abs/2402.06216v2

Yang, Z., Shao, Z., Dong, Y., & Tang, J. (2024). TriSampler: A better negative sampling principle for dense retrieval. *arXiv preprint arXiv:2402.11855*. https://arxiv.org/abs/2402.11855v1

---

## Appendix: Search Methodology Details

**Search Dates**: Conducted on October 26, 2026  
**Database**: arXiv  
**Category Filter**: cs.IR (primary category only)  
**Date Window**: January 9, 2024 – January 8, 2026  
**Initial Matches**: 26 papers  
**Citation Expansion**: 42 additional papers from references  
**Shortlist**: 30 papers  
**Screening Scores**:  
- Score 24: 3 papers  
- Score 3: 1 paper  
- Score 2: 1 paper  
- Score 1: 1 paper  
- Score 0: 24 papers  

**Final Selection**: 6 papers with scores ≥1

**Note on Paper Count**: The user requested 10 papers, but only 6 papers met the inclusion criteria with sufficient centrality to negative sampling techniques. This shortfall is reported transparently rather than padding with less relevant papers.
