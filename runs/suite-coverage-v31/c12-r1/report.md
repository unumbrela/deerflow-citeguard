# Systematic Literature Review: Negative Sampling Techniques in Information Retrieval

**Review Period:** January 9, 2024 – January 9, 2026  
**Category:** cs.IR (Information Retrieval)  
**Total Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in negative sampling techniques for information retrieval and recommendation systems published between January 2024 and January 2026. The review reveals significant progress in several key areas: (1) comprehensive surveys synthesizing the field, (2) LLM-driven synthetic negative generation, (3) domain-specific hard negative mining, (4) theoretical analyses of loss functions, and (5) multi-modal negative sampling approaches. The literature demonstrates a clear trend toward more sophisticated, semantically-aware sampling strategies that balance computational efficiency with retrieval effectiveness.

---

## Annotated Bibliography (APA Format)

### 1. Comprehensive Surveys

**Ma, H., Xie, R., Meng, L., Feng, F., Du, X., Sun, X., Kang, Z., & Meng, X. (2024).** Negative Sampling in Recommendation: A Survey and Future Directions. *arXiv preprint arXiv:2409.07237*. https://arxiv.org/abs/2409.07237

This comprehensive survey addresses the often-overlooked role of negative feedback in recommender systems. The authors classify existing negative sampling strategies into five categories based on their techniques and analyze challenges including information cocoons, interaction sparsity, and cold-start problems. The review covers tailored strategies for diverse RS scenarios and outlines prospective research directions, emphasizing the inescapable role of negative sampling in revealing genuine negative aspects of user behaviors.

**Wischounig, L., Abdallah, A., & Jatowt, A. (2026).** Negative Sampling Techniques in Information Retrieval: A Survey. *arXiv preprint arXiv:2603.18005*. https://arxiv.org/abs/2603.18005

Synthesizing 35 seminal papers, this up-to-date survey focuses on negative sampling techniques in dense retrieval with unique emphasis on modern NLP applications and LLM-driven methods. The authors propose a taxonomy categorizing techniques into random, static/dynamically mined, and synthetic datasets. The survey analyzes trade-offs between effectiveness, computational cost, and implementation difficulty, concluding with challenges and future directions for LLM-generated synthetic data—an area absent in prior reviews.

### 2. LLM-Driven Synthetic Negative Generation

**Li, X., Li, X., Zhang, H., Du, Z., Jia, P., Wang, Y., Zhao, X., Guo, H., & Tang, R. (2024).** SyNeg: LLM-Driven Synthetic Hard-Negatives for Dense Retrieval. *arXiv preprint arXiv:2412.17250*. https://arxiv.org/abs/2412.17250

This work addresses limitations of traditional negative sampling methods that either fail to capture accurate boundaries between positive and negative samples or suffer from false negatives. The authors present a framework harnessing LLMs to synthesize high-quality hard negative samples using a multi-attribute self-reflection prompting strategy. A hybrid sampling strategy integrates synthetic negatives with traditionally retrieved negatives, stabilizing training and improving retrieval performance. Extensive experiments on five benchmark datasets demonstrate the approach's efficacy.

**Singh, K., Kaur, S., & Smiley, C. (2024).** FinQAPT: Empowering Financial Decisions with End-to-End LLM-driven Question Answering Pipeline. *arXiv preprint arXiv:2410.13959*. https://arxiv.org/abs/2410.13959

While primarily focused on financial question answering, this paper introduces a novel clustering-based negative sampling technique to enhance context extraction in financial document retrieval. The pipeline achieved state-of-the-art accuracy of 80.6% on the FinQA dataset at the module level. The clustering-based approach optimizes context extraction by identifying relevant financial reports, though pipeline-level performance revealed challenges in extracting relevant context from complex financial documents.

### 3. Domain-Specific Hard Negative Mining

**Meghwani, H., Agarwal, A., Pattnayak, P., Patel, H. L., & Panda, S. (2025).** Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems. *arXiv preprint arXiv:2505.18366*. https://arxiv.org/abs/2505.18366

Addressing semantic mismatches in enterprise search systems, this paper proposes a scalable hard-negative mining framework tailored for domain-specific enterprise data. The approach dynamically selects semantically challenging but contextually irrelevant documents to enhance deployed re-ranking models. The method integrates diverse embedding models, performs dimensionality reduction, and uniquely selects hard negatives ensuring computational efficiency and semantic precision. Evaluation demonstrated substantial improvements of 15% in MRR@3 and 19% in MRR@10 compared to state-of-the-art baselines on proprietary enterprise corpus, with validation on public datasets (FiQA, Climate Fever, TechQA) confirming generalizability.

### 4. Semantic-Aware and Multi-Modal Approaches

**Xing, H., Matsuyama, K., Deng, H., Hu, J., Zhang, Y., & Zeng, X. (2025).** ESANS: Effective and Semantic-Aware Negative Sampling for Large-Scale Retrieval Systems. *arXiv preprint arXiv:2502.16077*. https://arxiv.org/abs/2502.16077

This work addresses limitations in industrial recommendation systems including false negatives, high computational costs, and semantic information deficiency. The authors propose ESANS, integrating two key components: (1) Effective Dense Interpolation Strategy (EDIS) generating virtual samples within low-dimensional embedding space to improve diversity and density while minimizing computational costs, and (2) Multimodal Semantic-Aware Clustering (MSAC) refining negative sampling distribution by hierarchically clustering item representations based on multimodal information (visual, textual, behavioral). Extensive offline and online experiments demonstrate superior efficiency and performance.

**Ji, Y., Luo, D., Liu, C., Wu, S., Tong, J., He, Q., Ji, D., Lu, H., & Ding, Y. (2025).** Generating Negative Samples for Multi-Modal Recommendation. *arXiv preprint arXiv:2501.15183*. https://arxiv.org/abs/2501.15183

Addressing two key challenges in negative sampling for multi-modal recommender systems—producing cohesive negative samples and maintaining balanced influence across modalities—this paper proposes NegGen. The framework utilizes multi-modal large language models (MLLMs) to generate balanced and contrastive negative samples through three different prompt templates analyzing and manipulating item attributes across multiple modalities. A causal learning module disentangles the effect of intervened key features and irrelevant item attributes, enabling fine-grained learning of user preferences. Extensive experiments on real-world datasets demonstrate superior performance compared to state-of-the-art methods.

### 5. Theoretical Analyses

**Di Teodoro, G., Siciliano, F., Tonellotto, N., & Silvestri, F. (2024).** A Theoretical Analysis of Recommendation Loss Functions under Negative Sampling. *arXiv preprint arXiv:2411.07770*. https://arxiv.org/abs/2411.07770

This theoretical work provides mathematical explanations for why Categorical Cross Entropy (CCE) outperforms Binary Cross Entropy (BCE) and Bayesian Personalized Ranking (BPR) when using full negative item sets, proving CCE offers the tightest lower bound on ranking metrics like NDCG and MRR. Under negative sampling, the authors reveal that BPR and CCE are equivalent when a single negative sample is drawn, and all three losses converge to the same global minimum. The sampled losses remain lower bounds for NDCG and MRR in a probabilistic sense, with worst-case analysis showing BCE offers the strongest bound. Experiments on five datasets and four models empirically support these findings.

### 6. Content-Based and Specialized Applications

**Rebelo, M. Â., Vinagre, J., Pereira, I., & Figueira, Á. (2024).** Rethinking negative sampling in content-based news recommendation. *arXiv preprint arXiv:2411.08700*. https://arxiv.org/abs/2411.08700

Addressing the brief lifespan and rapid relevance decay of news articles, this study posits that careful sampling of negative examples significantly impacts model outcomes in content-based neural news recommendation. The authors devise a negative sampling technique that improves model accuracy while facilitating decentralization of the recommendation system. Experimental results on the MIND dataset demonstrate that the method competes with state-of-the-art models while reducing model complexity and accelerating training. The paper discusses how decentralized models can improve privacy and scalability.

**Yang, Z., Shao, Z., Dong, Y., & Tang, J. (2024).** TriSampler: A Better Negative Sampling Principle for Dense Retrieval. *arXiv preprint arXiv:2402.11855*. https://arxiv.org/abs/2402.11855

This work provides theoretical analysis of negative sampling in dense retrieval, unveiling the quasi-triangular principle—a novel framework elucidating the triangular-like interplay between query, positive document, and negative document. Based on this guiding principle, the authors introduce TriSampler, a straightforward yet highly effective method that selectively samples more informative negatives within a prescribed constrained region. Experimental evaluation shows TriSampler consistently attains superior retrieval performance across diverse representative retrieval models, addressing the lack of comprehensive guiding principles for constructing negative candidates and designing sampling distributions.

---

## Thematic Analysis

### 1. Evolution Toward LLM-Driven Approaches

A prominent trend in 2024-2026 is the emergence of LLM-driven synthetic negative generation. Two papers (Li et al., 2024; Ji et al., 2025) leverage large language models to generate contextually rich negative samples, addressing limitations of traditional methods in capturing accurate decision boundaries. This represents a paradigm shift from mining existing negatives to synthesizing new ones.

### 2. Domain Specialization

Research increasingly focuses on domain-specific challenges. Meghwani et al. (2025) address enterprise systems, while Singh et al. (2024) tackle financial documents, and Rebelo et al. (2024) focus on news recommendation. This specialization acknowledges that generic negative sampling strategies may not address unique domain characteristics.

### 3. Theoretical Foundations

The field is maturing with stronger theoretical grounding. Di Teodoro et al. (2024) provide rigorous analysis of loss functions under negative sampling, while Yang et al. (2024) introduce the quasi-triangular principle. These theoretical contributions offer principled guidance for designing sampling strategies.

### 4. Multi-Modal Integration

With the rise of multi-modal recommender systems, negative sampling techniques are evolving to handle multiple data types. Ji et al. (2025) and Xing et al. (2025) propose methods that balance information across modalities, ensuring negative samples are informative across visual, textual, and behavioral dimensions.

### 5. Efficiency-Effectiveness Trade-offs

Multiple papers address the computational challenges of negative sampling at scale. ESANS (Xing et al., 2025) and the enterprise framework (Meghwani et al., 2025) explicitly optimize for both computational efficiency and semantic precision, reflecting practical deployment constraints.

---

## Methodological Trends

### Sampling Strategies

The literature reveals diverse sampling strategies:
- **Random/Naive Sampling**: Baseline approach, often insufficient for complex tasks
- **Hard Negative Mining**: Dynamically selecting challenging negatives (Meghwani et al., 2025)
- **Synthetic Generation**: LLM-driven creation of negatives (Li et al., 2024; Ji et al., 2025)
- **Semantic-Aware Clustering**: Using multimodal information for clustering (Xing et al., 2025)
- **Principle-Guided Sampling**: Following theoretical principles like quasi-triangular (Yang et al., 2024)

### Evaluation Metrics

Common evaluation metrics include:
- **MRR@K**: Mean Reciprocal Rank at various cutoffs
- **NDCG**: Normalized Discounted Cumulative Gain
- **Accuracy**: Task-specific accuracy measures
- **Computational Efficiency**: Training time and resource consumption

### Datasets

The reviewed papers utilize both proprietary and public datasets:
- **Enterprise corpora** (cloud services domain)
- **FiQA, Climate Fever, TechQA** (domain-specific retrieval)
- **MIND** (news recommendation)
- **FinQA** (financial question answering)
- **Five benchmark datasets** for dense retrieval (Li et al., 2024)

---

## Challenges and Future Directions

### Current Challenges

1. **False Negatives**: Multiple papers identify false negatives as a persistent problem leading to performance degradation and training instability (Li et al., 2024; Xing et al., 2025)

2. **Computational Cost**: Ensuring sampling quality often incurs high computational costs, particularly at scale (Xing et al., 2025)

3. **Semantic Information Deficiency**: Traditional methods may lack semantic awareness, producing less informative negatives (Xing et al., 2025)

4. **Multi-Modal Balance**: Maintaining balanced influence across different modalities remains challenging (Ji et al., 2025)

5. **Domain Adaptation**: Generic strategies may not transfer well across domains (Meghwani et al., 2025)

### Future Directions

Based on the surveyed literature, promising research directions include:

1. **LLM-Generated Synthetic Data**: Wischounig et al. (2026) identify this as an area absent in prior reviews with significant potential

2. **Hybrid Approaches**: Combining synthetic negatives with traditionally retrieved negatives (Li et al., 2024)

3. **Theoretical Principles**: Developing more guiding principles like the quasi-triangular principle (Yang et al., 2024)

4. **Decentralized Systems**: Exploring privacy-preserving decentralized recommendation (Rebelo et al., 2024)

5. **Fine-Grained Preference Learning**: Using causal learning to disentangle features (Ji et al., 2025)

---

## Conclusion

The literature from 2024-2026 demonstrates significant advancement in negative sampling techniques for information retrieval. The field is characterized by: (1) comprehensive surveys synthesizing accumulated knowledge, (2) innovative LLM-driven approaches, (3) stronger theoretical foundations, (4) domain-specific adaptations, and (5) multi-modal integration. 

Key contributions include the quasi-triangular principle providing theoretical guidance, LLM-based synthetic negative generation offering new possibilities, and semantic-aware clustering improving sampling quality. The trend toward hybrid approaches combining multiple strategies suggests future systems will leverage complementary strengths of different techniques.

Practical considerations around computational efficiency, false negative reduction, and domain adaptation remain central concerns. The emergence of decentralized approaches points to growing attention to privacy and scalability. Overall, the literature indicates a maturing field with both theoretical depth and practical applicability.

---

## References

Di Teodoro, G., Siciliano, F., Tonellotto, N., & Silvestri, F. (2024). A Theoretical Analysis of Recommendation Loss Functions under Negative Sampling. *arXiv preprint arXiv:2411.07770*. https://arxiv.org/abs/2411.07770

Ji, Y., Luo, D., Liu, C., Wu, S., Tong, J., He, Q., Ji, D., Lu, H., & Ding, Y. (2025). Generating Negative Samples for Multi-Modal Recommendation. *arXiv preprint arXiv:2501.15183*. https://arxiv.org/abs/2501.15183

Li, X., Li, X., Zhang, H., Du, Z., Jia, P., Wang, Y., Zhao, X., Guo, H., & Tang, R. (2024). SyNeg: LLM-Driven Synthetic Hard-Negatives for Dense Retrieval. *arXiv preprint arXiv:2412.17250*. https://arxiv.org/abs/2412.17250

Ma, H., Xie, R., Meng, L., Feng, F., Du, X., Sun, X., Kang, Z., & Meng, X. (2024). Negative Sampling in Recommendation: A Survey and Future Directions. *arXiv preprint arXiv:2409.07237*. https://arxiv.org/abs/2409.07237

Meghwani, H., Agarwal, A., Pattnayak, P., Patel, H. L., & Panda, S. (2025). Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems. *arXiv preprint arXiv:2505.18366*. https://arxiv.org/abs/2505.18366

Rebelo, M. Â., Vinagre, J., Pereira, I., & Figueira, Á. (2024). Rethinking negative sampling in content-based news recommendation. *arXiv preprint arXiv:2411.08700*. https://arxiv.org/abs/2411.08700

Singh, K., Kaur, S., & Smiley, C. (2024). FinQAPT: Empowering Financial Decisions with End-to-End LLM-driven Question Answering Pipeline. *arXiv preprint arXiv:2410.13959*. https://arxiv.org/abs/2410.13959

Wischounig, L., Abdallah, A., & Jatowt, A. (2026). Negative Sampling Techniques in Information Retrieval: A Survey. *arXiv preprint arXiv:2603.18005*. https://arxiv.org/abs/2603.18005

Xing, H., Matsuyama, K., Deng, H., Hu, J., Zhang, Y., & Zeng, X. (2025). ESANS: Effective and Semantic-Aware Negative Sampling for Large-Scale Retrieval Systems. *arXiv preprint arXiv:2502.16077*. https://arxiv.org/abs/2502.16077

Yang, Z., Shao, Z., Dong, Y., & Tang, J. (2024). TriSampler: A Better Negative Sampling Principle for Dense Retrieval. *arXiv preprint arXiv:2402.11855*. https://arxiv.org/abs/2402.11855

---

**Review Completed:** October 26, 2026  
**Search Category:** cs.IR  
**Publication Window:** January 9, 2024 – January 9, 2026  
**Total Papers:** 10
