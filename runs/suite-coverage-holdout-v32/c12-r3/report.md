# Systematic Literature Review: Negative Sampling Techniques in Information Retrieval

**Review Period:** January 9, 2024 – January 8, 2026  
**Category:** cs.IR (Information Retrieval)  
**Total Papers Reviewed:** 10

---

## Executive Summary

This systematic literature review examines recent advances in negative sampling techniques within information retrieval and recommender systems. The reviewed literature spans from January 2024 to January 2026, revealing significant progress in hard negative mining, semantic-aware sampling, LLM-driven synthetic negative generation, and theoretical foundations. Key themes include: (1) the shift from naive random sampling to sophisticated hard negative mining strategies, (2) integration of large language models for synthetic negative generation, (3) multi-modal considerations in negative sample construction, and (4) theoretical analysis of loss functions under negative sampling constraints.

---

## References (APA Format)

Di Teodoro, G., Siciliano, F., Tonellotto, N., & Silvestri, F. (2024, November 12). A theoretical analysis of recommendation loss functions under negative sampling. *arXiv preprint arXiv:2411.07770*. https://arxiv.org/abs/2411.07770v3

Ji, Y., Luo, D., Liu, C., Wu, S., Tong, J., He, Q., Ji, D., Lu, H., & Ding, Y. (2025, January 25). Generating negative samples for multi-modal recommendation. *arXiv preprint arXiv:2501.15183*. https://arxiv.org/abs/2501.15183v3

Ma, H., Xie, R., Meng, L., Feng, F., Du, X., Sun, X., Kang, Z., & Meng, X. (2024, September 11). Negative sampling in recommendation: A survey and future directions. *arXiv preprint arXiv:2409.07237*. https://arxiv.org/abs/2409.07237v2

Meghwani, H., Agarwal, A., Pattnayak, P., Patel, H. L., & Panda, S. (2025, May 23). Hard negative mining for domain-specific retrieval in enterprise systems. *arXiv preprint arXiv:2505.18366*. https://arxiv.org/abs/2505.18366v1

Rebelo, M. Â., Vinagre, J., Pereira, I., & Figueira, Á. (2024, November 13). Rethinking negative sampling in content-based news recommendation. *arXiv preprint arXiv:2411.08700*. https://arxiv.org/abs/2411.08700v1

Shi, K., Zhang, J., Fang, L., Wang, W., & Jing, B. (2024, March 28). Enhanced Bayesian personalized ranking for robust hard negative sampling in recommender systems. *arXiv preprint arXiv:2403.19276*. https://arxiv.org/abs/2403.19276v1

Singh, K., Kaur, S., & Smiley, C. (2024, October 17). FinQAPT: Empowering financial decisions with end-to-end LLM-driven question answering pipeline. *arXiv preprint arXiv:2410.13959*. https://arxiv.org/abs/2410.13959v2

Xing, H., Matsuyama, K., Deng, H., Hu, J., Zhang, Y., & Zeng, X. (2025, February 22). ESANS: Effective and semantic-aware negative sampling for large-scale retrieval systems. *arXiv preprint arXiv:2502.16077*. https://arxiv.org/abs/2502.16077v1

Yang, Z., Shao, Z., Dong, Y., & Tang, J. (2024, February 19). TriSampler: A better negative sampling principle for dense retrieval. *arXiv preprint arXiv:2402.11855*. https://arxiv.org/abs/2402.11855v1

Li, X., Li, X., Zhang, H., Du, Z., Jia, P., Wang, Y., Zhao, X., Guo, H., & Tang, R. (2024, December 23). SyNeg: LLM-driven synthetic hard-negatives for dense retrieval. *arXiv preprint arXiv:2412.17250*. https://arxiv.org/abs/2412.17250v1

---

## Thematic Analysis

### 1. Hard Negative Mining and Domain-Specific Applications

**Meghwani et al. (2025)** introduced a scalable hard-negative mining framework specifically designed for enterprise search systems. Their approach dynamically selects semantically challenging but contextually irrelevant documents, achieving substantial improvements of 15% in MRR@3 and 19% in MRR@10 compared to state-of-the-art baselines. The method integrates diverse embedding models with dimensionality reduction techniques, ensuring both computational efficiency and semantic precision.

**Shi et al. (2024)** addressed the false negative problem in hard negative sampling by refining the loss function rather than designing sophisticated sampling algorithms. Their Hard-BPR (Enhanced Bayesian Personalized Ranking) objective is specifically crafted for dynamic hard negative sampling, demonstrating effectiveness and robustness across three real-world datasets.

### 2. Semantic-Aware and Multi-Modal Negative Sampling

**Xing et al. (2025)** proposed ESANS (Effective and Semantic-Aware Negative Sampling), which integrates two key components: Effective Dense Interpolation Strategy (EDIS) and Multimodal Semantic-Aware Clustering (MSAC). EDIS generates virtual samples within the low-dimensional embedding space to improve diversity and density, while MSAC refines negative sampling through hierarchical clustering based on multimodal information (visual, textual, behavioral), ensuring semantic consistency and reducing false negatives.

**Ji et al. (2025)** focused on multi-modal recommender systems, identifying two key challenges: producing cohesive negative samples contrasting with positive samples and maintaining balanced influence across different modalities. Their NegGen framework utilizes multi-modal large language models (MLLMs) to generate balanced and contrastive negative samples through three different prompt templates, supplemented by a causal learning module for fine-grained user preference learning.

### 3. LLM-Driven Synthetic Negative Generation

**Li et al. (2024)** presented SyNeg, a framework harnessing large language models to synthesize high-quality hard negative samples for dense retrieval. Their multi-attribute self-reflection prompting strategy directs LLMs in hard negative sample generation, while a hybrid sampling strategy integrates synthetic negatives with traditionally retrieved negatives to stabilize training. Extensive experiments on five benchmark datasets demonstrated the efficacy of this approach.

**Singh et al. (2024)** introduced a clustering-based negative sampling technique within their FinQAPT pipeline for financial question answering. This novel approach enhanced context extraction from financial reports, contributing to state-of-the-art accuracy of 80.6% at the module level on the FinQA dataset.

### 4. Theoretical Foundations and Loss Function Analysis

**Di Teodoro et al. (2024)** provided a theoretical analysis of recommendation loss functions (CCE, BCE, BPR) under negative sampling. They proved that CCE offers the tightest lower bound on ranking metrics like NDCG and MRR when using the full set of negative items. Under negative sampling conditions, they revealed that BPR and CCE are equivalent when a single negative sample is drawn, and all three losses converge to the same global minimum. Their worst-case analysis showed that BCE offers the strongest bound on NDCG and MRR.

**Yang et al. (2024)** conducted theoretical analysis of negative sampling in dense retrieval, unveiling the quasi-triangular principle that elucidates the triangular-like interplay between query, positive document, and negative document. Their TriSampler method selectively samples more informative negatives within a prescribed constrained region, consistently attaining superior retrieval performance across diverse retrieval models.

### 5. Survey and Future Directions

**Ma et al. (2024)** conducted an extensive literature review on negative sampling strategies in recommender systems, classifying existing approaches into five categories based on their techniques. They discussed existing user feedback, the critical role of negative sampling, optimization objectives, and thoroughly analyzed challenges impeding progress. The survey outlined prospective research directions for the community.

### 6. Application-Specific Innovations

**Rebelo et al. (2024)** focused on news recommender systems, where articles undergo rapid relevance decay. Their negative sampling technique improves model accuracy while facilitating decentralization of the recommendation system. Experimental results on the MIND dataset demonstrated that their method can compete with state-of-the-art models while reducing model complexity and accelerating training.

---

## Key Findings and Trends

### Methodological Advances

1. **From Random to Hard Negatives:** The literature demonstrates a clear shift from naive random negative sampling to sophisticated hard negative mining strategies that select semantically challenging samples.

2. **LLM Integration:** Multiple studies (Li et al., 2024; Ji et al., 2025; Singh et al., 2024) leverage large language models for synthetic negative generation, representing a significant methodological innovation.

3. **Multi-Modal Considerations:** Recent work recognizes the importance of incorporating multiple modalities (visual, textual, behavioral) in negative sample construction to ensure semantic consistency.

4. **Theoretical Grounding:** Several papers (Di Teodoro et al., 2024; Yang et al., 2024) provide theoretical foundations explaining why certain negative sampling strategies outperform others.

### Performance Improvements

Reported improvements across studies include:
- 15-19% improvement in MRR metrics (Meghwani et al., 2025)
- 80.6% accuracy on FinQA dataset (Singh et al., 2024)
- Consistent superior performance across diverse retrieval models (Yang et al., 2024)
- Enhanced ability to distinguish false negatives (Shi et al., 2024)

### Open Challenges

1. **False Negative Problem:** Multiple studies (Shi et al., 2024; Xing et al., 2025) highlight the persistent challenge of inadvertently selecting false negatives that provide incorrect training signals.

2. **Computational Efficiency:** Balancing sampling quality with computational cost remains a concern, particularly for large-scale industrial systems (Xing et al., 2025).

3. **Domain Generalization:** While methods show promise on proprietary datasets, generalizability across domains requires further validation (Meghwani et al., 2025).

4. **Multi-Modal Balance:** Maintaining balanced influence across different modalities in negative sample generation presents ongoing challenges (Ji et al., 2025).

---

## Conclusion

The reviewed literature from 2024-2026 demonstrates significant advances in negative sampling techniques for information retrieval and recommender systems. Key trends include the integration of large language models for synthetic negative generation, semantic-aware multi-modal sampling strategies, and stronger theoretical foundations explaining loss function behavior under negative sampling. The field is moving beyond simple random sampling toward sophisticated, domain-aware, and computationally efficient methods that better capture the boundaries between positive and negative samples. Future research directions identified include addressing false negative problems, improving cross-domain generalization, and developing more robust multi-modal negative sampling frameworks.

---

## Appendix: Chronological Timeline

| Date | Paper | Key Contribution |
|------|-------|------------------|
| 2024-02-19 | Yang et al. - TriSampler | Quasi-triangular principle for dense retrieval |
| 2024-03-28 | Shi et al. - Hard-BPR | Enhanced loss function for hard negative sampling |
| 2024-09-11 | Ma et al. - Survey | Comprehensive classification of negative sampling strategies |
| 2024-10-17 | Singh et al. - FinQAPT | Clustering-based negative sampling for financial QA |
| 2024-11-12 | Di Teodoro et al. - Loss Analysis | Theoretical analysis of CCE, BCE, BPR under negative sampling |
| 2024-11-13 | Rebelo et al. - News Recommendation | Decentralized negative sampling for news recommendation |
| 2024-12-23 | Li et al. - SyNeg | LLM-driven synthetic hard-negative generation |
| 2025-01-25 | Ji et al. - NegGen | Multi-modal negative sample generation with MLLMs |
| 2025-02-22 | Xing et al. - ESANS | Semantic-aware negative sampling with multimodal clustering |
| 2025-05-23 | Meghwani et al. - Enterprise Hard Negatives | Domain-specific hard-negative mining for enterprise systems |
