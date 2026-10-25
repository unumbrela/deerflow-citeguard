# Systematic Literature Review: LLM-Based Recommender Systems

**Date**: 2026-10-25
**Papers surveyed**: 3
**Scope**: arXiv search query "LLM recommender systems", category cs.IR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examined 3 recent arXiv papers on LLM-based recommender systems within the cs.IR (Information Retrieval) category. The surveyed literature reveals a field focused on addressing fundamental challenges in deploying LLMs for recommendation tasks, particularly the tension between computational efficiency and recommendation accuracy. Recent work emphasizes novel architectures that leverage multimodal representations, retrieval-augmented generation, and dynamic knowledge structures to improve both performance and practicality of LLM-based recommenders. The limited number of papers in this specific category suggests this is an emerging research direction with substantial room for growth.

## Methodology

This review surveyed 3 arXiv papers retrieved on 2026-10-25 using the query "LLM recommender systems", filtered to category cs.IR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and all matching results were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented. The search returned only 3 papers, suggesting either the intersection of "LLM" and "recommender systems" in cs.IR is narrow, or related work may be categorized under adjacent categories such as cs.AI, cs.LG, or cs.CL.

## Themes

### Theme 1: Efficiency vs. Accuracy Trade-offs

A central concern across the surveyed literature is balancing computational efficiency with recommendation accuracy. LLMs are computationally expensive, particularly when processing lengthy item descriptions or user histories. Kim et al. (2025) address this by proposing image-based item representations that reduce token consumption while preserving semantic richness. Zhou et al. (2025) tackle the same challenge through architectural innovations that enable early termination of inference when confidence thresholds are met. Both approaches recognize that practical deployment of LLM recommenders requires careful optimization of resource usage without sacrificing predictive quality.

### Theme 2: Retrieval-Augmented Generation for Recommendations

Two of the three surveyed papers employ retrieval-augmented generation (RAG) architectures, indicating this is a dominant paradigm in LLM-based recommendation. Zhou et al. (2025) integrate RAG with multi-head early exit mechanisms to accelerate click-through rate prediction. Yang et al. (2025) extend RAG to cold-start scenarios by dynamically constructing knowledge graphs at inference time. The convergence on RAG suggests that augmenting LLMs with external retrieval mechanisms is viewed as essential for grounding recommendations in up-to-date, context-specific information rather than relying solely on parametric knowledge.

### Theme 3: Multimodal and Dynamic Representations

The literature shows movement toward richer, more adaptive item representations. Kim et al. (2025) demonstrate that images can serve as token-efficient alternatives to textual descriptions, leveraging the information overlap between visual and textual modalities. Yang et al. (2025) propose dynamic knowledge graph construction that adapts to new items without requiring expensive pre-computation. These approaches reflect recognition that static, text-only representations are insufficient for capturing the full semantic landscape needed for effective recommendation.

## Convergences and Disagreements

**Convergences**: All surveyed papers agree that efficiency is a critical bottleneck in LLM-based recommendation systems. Both Kim et al. (2025) and Zhou et al. (2025) explicitly frame their contributions as solutions to the efficiency-accuracy trade-off. Additionally, there is consensus that retrieval mechanisms are necessary for practical LLM recommender deployment, as evidenced by the RAG-based approaches in Zhou et al. (2025) and Yang et al. (2025).

**Disagreements**: The surveyed papers do not directly contradict one another, as they address different sub-problems within LLM-based recommendation. However, there is a methodological divergence: Kim et al. (2025) focus on modality substitution (images vs. text), while Zhou et al. (2025) and Yang et al. (2025) focus on architectural optimization and retrieval strategies. Whether multimodal representation or architectural refinement offers greater gains remains an open empirical question.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the abstracts explicitly state limitations, suggesting either that limitations were not discussed or that they focus on implementation details rather than fundamental constraints. Second, all papers are from 2025, indicating this is a very recent research direction — longitudinal studies tracking the evolution of these approaches are absent. Third, the small number of papers in cs.IR suggests related work may be scattered across adjacent categories, making comprehensive synthesis challenging. Finally, while all papers claim improved performance over baselines, the abstracts do not specify whether evaluations were conducted on common benchmarks, making cross-paper comparison difficult.

## Per-Paper Annotations

### Kim et al. (2025)

**Research question**: How can LLM-based recommender systems address the trade-off between efficiency and effectiveness when representing items consumed by users?

**Methodology**: The authors propose I-LLMRec, a method that leverages images as an alternative to lengthy textual descriptions for representing items, aiming to reduce token usage while preserving rich semantic information. The approach is based on the observation that there is significant information overlap between images and descriptions associated with items.

**Key findings**:
- I-LLMRec outperforms existing methods in both efficiency and effectiveness by leveraging images
- The method reduces token usage while preserving the rich semantic information of item descriptions
- I-LLMRec demonstrates ability to reduce sensitivity to noise in descriptions, leading to more robust recommendations

**Limitations**: not stated in abstract

### Zhou et al. (2025)

**Research question**: How can LLM-based recommender systems for click-through rate prediction balance computational efficiency and predictive accuracy?

**Methodology**: The paper presents an optimization framework combining Retrieval-Augmented Generation (RAG) with a multi-head early exit architecture. The approach integrates Graph Convolutional Networks as efficient retrieval mechanisms and employs an early exit strategy that allows dynamic termination of model inference using real-time predictive confidence assessments across multiple heads.

**Key findings**:
- The architecture significantly reduces data retrieval times while maintaining high model performance
- The early exit strategy quickens responsiveness of LLMs while upholding or improving accuracy
- The method effectively decreases computation time without sacrificing accuracy needed for reliable recommendation delivery
- The approach establishes a new standard for efficient, real-time LLM deployment in commercial systems

**Limitations**: not stated in abstract

### Yang et al. (2025)

**Research question**: How can recommender systems address the cold-start problem for new items with limited interaction data while overcoming limitations of static knowledge graphs and LLM-based methods?

**Methodology**: The authors propose ColdRAG, a retrieval-augmented framework that dynamically constructs a knowledge graph from raw metadata, extracts entities and relations to build an updatable structure, and introduces LLM-guided multi-hop reasoning at inference time to retrieve and rank candidates without relying on pre-filtered lists.

**Key findings**:
- ColdRAG dynamically constructs knowledge graphs from raw metadata, avoiding the expense and obsolescence of static KGs
- The framework extracts entities and relations to construct an updatable structure
- LLM-guided multi-hop reasoning enables candidate retrieval and ranking without pre-filtered lists
- ColdRAG consistently outperforms seven strong baselines across multiple benchmarks

**Limitations**: not stated in abstract

## References

Kim, K., Kim, S., Kang, H., Kim, J., Noh, H., In, Y., Yoon, K., Oh, J., McAuley, J., & Park, C. (2025). Token-efficient item representation via images for LLM recommender systems. arXiv. https://arxiv.org/abs/2503.06238

Yang, W., Zhang, W., Liu, Y., Han, Y., Wang, Y., Lee, J., & Yu, P. S. (2025). Adaptive candidate retrieval with dynamic knowledge graph construction for cold-start recommendation. arXiv. https://arxiv.org/abs/2505.20773

Zhou, H., Gu, H., Liu, X., Zhou, K., Liang, M., Xiao, Y., Govindan, S., Chawla, P., Yang, J., Meng, X., Li, H., Zhang, B., Luo, L., Chen, W.-Y., Han, Y., Long, B., Zhang, R., & Chen, T. (2025). The efficiency vs. accuracy trade-off: Optimizing RAG-enhanced LLM recommender systems using multi-head early exit. arXiv. https://arxiv.org/abs/2501.02173
