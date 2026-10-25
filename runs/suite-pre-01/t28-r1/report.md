# Systematic Literature Review: Dense Retrieval

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: "dense retrieval" query, cs.IR category, published between 2024-10-25 and 2025-10-25
**Citation format**: APA 7th edition

## Executive Summary

The dense retrieval literature from the past two years reveals a field rapidly evolving along multiple dimensions: efficiency optimization for real-world deployment, multilingual and cross-lingual generalization, integration with large language models, and fundamental investigations into retrieval model capabilities and limitations. Recent work demonstrates that dense retrieval systems can achieve substantial performance gains over traditional sparse methods (e.g., 0.26 to 0.66 Recall@10 improvement) while meeting practical latency constraints through techniques like quantization and pruning. However, critical gaps remain in handling complex reasoning tasks such as multi-hop queries and Boolean logic, with current systems showing significant limitations in these areas. The literature also reveals growing attention to deployment considerations including computational efficiency, domain adaptation with minimal training data, and scaling strategies that balance performance with inference costs.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "dense retrieval", filtered to category cs.IR, published between 2024-10-25 and 2025-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Scalability for Real-World Deployment

A prominent thread across recent dense retrieval research focuses on making systems efficient enough for production deployment at scale. Multiple papers address the tension between retrieval effectiveness and computational costs through complementary approaches. Siciliano et al. (2024) propose static pruning using Principal Components Analysis, reducing embedding dimensionality by over 50% with only up to 5% reduction in NDCG@10, enabling query-independent offline processing. Pandey (2026) demonstrates a production-ready system combining FAISS HNSW indexing with ONNX Runtime and INT8 dynamic quantization, achieving 6.1 ms median CPU inference latency and 4x model size reduction while improving Recall@10 from 0.26 to 0.66 on 826,402 catalog items. Huang et al. (2024) introduce ScalingNote, a two-stage approach that first trains dual-tower LLM-based retrievers, then distills only the query tower to maintain online efficiency while capturing LLM scaling benefits. These works collectively establish that efficiency need not come at the cost of effectiveness when appropriate optimization strategies are employed.

### Theme 2: Multilingual and Cross-Lingual Retrieval

Multilingual dense retrieval has emerged as a critical research direction, with multiple papers addressing the challenge of aligning representations across languages in a shared vector space. Wullach et al. (2026) reveal that the optimal threshold for converting graded relevance judgments to binary labels varies systematically across languages and tasks, often reflecting differences in resource levels. Their findings demonstrate that well-chosen thresholds can improve effectiveness, reduce fine-tuning data requirements, and mitigate annotation noise. Huang et al. (2025) focus on data utilization strategies, proposing methods to obtain high-quality hard negative samples and construct more effective mini-batch data for contrastive learning, outperforming strong baselines across 16 languages in the MIRACL benchmark. These works highlight that multilingual retrieval challenges extend beyond architectural innovations to include careful attention to training data quality, relevance threshold calibration, and language-specific considerations.

### Theme 3: Integration with Large Language Models

The integration of dense retrieval with large language models represents a major trend in recent literature. Huang et al. (2024) verify the scaling law of dense retrieval with LLMs in industrial scenarios, demonstrating that LLM-initialized retrievers can outperform traditional dual-tower architectures when combined with appropriate distillation strategies. Erker et al. (2025) introduce GRITHopper-7B, which combines generative and representational instruction tuning by integrating causal language modeling with dense retrieval training, achieving state-of-the-art performance on multi-hop retrieval benchmarks. Their work reveals that incorporating additional context after retrieval through post-retrieval language modeling enhances dense retrieval performance. These papers collectively suggest that LLMs offer substantial potential for dense retrieval when computational costs can be managed through techniques like distillation or hybrid architectures.

### Theme 4: Domain Adaptation and Flexibility

The challenge of adapting dense retrieval systems to new domains with limited training data has received significant attention. Su et al. (2026) propose dynamic dense retrieval (DDR), using prefix tuning modules specialized for specific domains that can be compositionally combined with dynamic routing strategies. Their approach surpasses traditional dense retrieval while utilizing only 2% of training parameters, enabling flexible domain adaptation without expensive retraining from scratch. Pandey (2026) demonstrates domain-adaptive retrieval for e-commerce recommendations, fine-tuning on Amazon Reviews data with supervised contrastive learning. These works address a critical practical limitation: the traditional paradigm of training new models from scratch for each domain is prohibitively expensive for scenarios requiring frequent updates.

### Theme 5: Fundamental Capabilities and Limitations

Several papers investigate fundamental questions about what dense retrieval systems can and cannot do. Zhang et al. (2024) formulate Boolean Dense Retrieval and introduce the BoolQuestions benchmark, revealing that current systems do not fully understand Boolean logic in language despite strong performance on standard retrieval tasks. Their work identifies a significant gap between semantic similarity matching and logical reasoning capabilities. Chen et al. (2024) address robustness and explainability, proposing counterfactual regularization methods that enhance model sensitivity to fine-grained relevance signals, enabling extraction of key passages without passage-level annotations and improving adversarial robustness. These investigations reveal that while dense retrieval excels at semantic matching, critical gaps remain in reasoning, robustness, and interpretability.

### Theme 6: Hybrid and Unified Retrieval Paradigms

Recent work explores combining dense retrieval with complementary approaches to leverage their respective strengths. Yang et al. (2024) propose LIGER, a hybrid model integrating sequential dense retrieval into generative retrieval, mitigating performance differences and enhancing cold-start item recommendation. Their controlled comparison reveals distinct trade-offs: dense retrieval requires storing unique representations for each item (memory-intensive at scale), while generative retrieval directly predicts item indices using semantic IDs. Erker et al. (2025) similarly combine generative and dense approaches in GRITHopper, demonstrating that hybrid architectures can achieve superior performance on complex multi-hop queries. These works suggest that future retrieval systems may increasingly combine multiple paradigms rather than treating them as mutually exclusive.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that dense retrieval can substantially outperform traditional sparse methods (e.g., BM25) when properly optimized, with consistent reports of significant improvements in recall metrics across domains (Chen et al., 2024; Huang et al., 2024; Pandey, 2026). There is also broad agreement that efficiency optimizations—whether through pruning, quantization, or distillation—can be achieved with minimal effectiveness loss when carefully designed (Huang et al., 2024; Siciliano et al., 2024; Pandey, 2026). The literature consistently emphasizes that training data quality and construction strategies matter as much as or more than architectural innovations (Chen et al., 2024; Huang et al., 2025; Wullach et al., 2026).

**Disagreements**: While most papers report positive results on their specific benchmarks, there is implicit disagreement about the generalizability of findings. For instance, Huang et al. (2024) validate scaling laws in industrial scenarios, while Yang et al. (2024) note their hybrid approach was evaluated only on small-scale benchmarks, raising questions about transferability. Similarly, while Su et al. (2026) demonstrate strong zero-shot performance with only 2% of parameters, their evaluation covered only six downstream tasks, leaving open questions about broader applicability. The literature does not contain direct contradictions but reveals varying levels of optimism about generalizability across domains and scales.

## Gaps and Open Questions

Several gaps emerge consistently across the surveyed literature. First, **evaluation scale and diversity** remains limited: multiple papers acknowledge evaluation on small-scale benchmarks (Yang et al., 2024), limited downstream tasks (Su et al., 2026), or single domains (Pandey, 2026), raising questions about generalizability. Second, **computational transparency** is frequently lacking: while efficiency is often claimed, detailed analysis of training costs, carbon footprint, or full deployment requirements is rarely provided. Third, **fundamental reasoning capabilities** remain underexplored: the BoolQuestions benchmark (Zhang et al., 2024) reveals that dense retrieval systems struggle with Boolean logic, suggesting broader gaps in reasoning that may affect complex query understanding. Fourth, **multilingual equity** receives attention but remains unresolved: Wullach et al. (2026) show that optimal thresholds vary by language resource level, potentially exacerbating inequities for low-resource languages without careful calibration. Fifth, **long-term maintenance and updates** are acknowledged as challenges but not fully solved: while DDR (Su et al., 2026) offers a promising direction, the operational complexity of managing multiple prefix modules and routing strategies in production remains unexplored. Finally, **integration with downstream applications** beyond retrieval metrics is underexplored: most papers optimize for retrieval effectiveness (recall, NDCG) rather than end-to-end task performance in applications like question answering or recommendation.

## Per-Paper Annotations

### Chen et al. (2024)

**Research question**: How can dense retrieval models be made more robust against adversarial attacks and more explainable while enhancing sensitivity to fine-grained relevance signals?
**Methodology**: Proposes counterfactual regularization methods based on game theory and unsupervised learning with counterfactual passages, motivated by causality and counterfactual analysis to improve model sensitivity to key relevance-determining passages.
**Key findings**:
- Can extract key passages without reliance on passage-level relevance annotations
- Regularized models exhibit heightened robustness against adversarial attacks
- Surpasses state-of-the-art anti-attack methods in adversarial robustness benchmarks
- Enables analysis of which document passages are actually relevant to queries, improving explainability
- Model exhibits high variance when key passages are modified but low variance for irrelevant changes
**Limitations**: Counterfactual regularization approach may be computationally intensive during training; effectiveness on very large-scale corpora beyond experimental settings not fully demonstrated; game-theoretic foundations add implementation complexity.

### Erker et al. (2025)

**Research question**: How can multi-hop dense retrieval overcome the computational expense and lack of end-to-end differentiability in decomposition-based methods while improving generalization to out-of-distribution data?
**Methodology**: GRITHopper-7B combines generative and representational instruction tuning by integrating causal language modeling with dense retrieval training, incorporating post-retrieval language modeling with elements like final answers during training.
**Key findings**:
- Achieves state-of-the-art performance on both in-distribution and out-of-distribution multi-hop retrieval benchmarks
- Post-retrieval language modeling significantly enhances dense retrieval performance
- Including final answers during training helps the model better contextualize and retrieve relevant information
- Eliminates need for autoregressive decomposition steps, enabling end-to-end differentiability
- Released as an open model for community research on multi-hop reasoning and retrieval
**Limitations**: Current decomposition-free approaches including GRITHopper still struggle with longer multi-hop problems beyond tested benchmarks; the 7B parameter model size may be computationally expensive for resource-constrained deployments.

### Huang et al. (2024)

**Research question**: How can the scaling potential of Large Language Models be exploited for dense retrieval while maintaining acceptable online query latency for real-world industrial deployment?
**Methodology**: Two-stage approach: first trains dual towers both initialized from the same LLM to unlock LLM potential, then distills only the query tower using mean squared error loss and cosine similarity to reduce online inference costs.
**Key findings**:
- Outperforms end-to-end baseline models in both offline and online experiments
- Verifies the scaling law of dense retrieval with LLMs in industrial scenarios
- Enables cost-effective scaling of dense retrieval systems without latency penalties
- Significantly enhances relevance between retrieved documents and queries in production deployment
- Distillation approach maintains retrieval quality while reducing online computational costs
**Limitations**: Still requires significant computational resources for initial LLM-based training; distillation process may lose some capabilities of the full LLM; validation primarily in industrial scenarios may not generalize to all application domains.

### Huang et al. (2025)

**Research question**: How can we improve multilingual dense retrieval by better utilizing training data through improved negative sampling and mini-batch construction?
**Methodology**: The authors propose a method to boost data utilization by obtaining high-quality hard negative samples and constructing more effective mini-batch data for contrastive learning, without developing new model architectures.
**Key findings**:
- Outperforms several existing strong baselines on the MIRACL multilingual retrieval benchmark
- Effective across 16 different languages in the evaluation
- High-quality hard negative samples significantly improve retrieval effectiveness
- Effective mini-batch data construction enhances contrastive learning
- Data utilization improvements can match or exceed architectural innovations
**Limitations**: Evaluation limited to the MIRACL benchmark; the method focuses on data utilization rather than addressing fundamental cross-lingual representation alignment challenges.

### Pandey (2026)

**Research question**: How can e-commerce recommendation systems overcome vocabulary mismatch when user intent has limited lexical overlap with product metadata?
**Methodology**: Presents a scalable dense retrieval system using a two-tower bi-encoder fine-tuned on Amazon Reviews 2023 (Fashion) with supervised contrastive learning (Multiple Negatives Ranking Loss), combining FAISS HNSW indexing with ONNX Runtime inference using INT8 dynamic quantization.
**Key findings**:
- Improved Recall@10 from 0.26 (BM25 baseline) to 0.66 on review-to-title benchmark over 826,402 catalog items
- Achieved 6.1 ms median CPU inference latency at batch size 1, meeting practical serving requirements
- Reduced model size by 4x through INT8 dynamic quantization without significant performance degradation
- Successfully trained on 50,000 sampled review-item pairs with 500 token maximum sequence length
- Provides an end-to-end reproducible blueprint for deploying domain-adapted dense retrieval at catalog scale
**Limitations**: Evaluated only on Amazon Fashion domain, requiring domain-specific fine-tuning for other product categories; the approach depends on availability of review text as query proxies which may not exist in all e-commerce settings.

### Siciliano et al. (2024)

**Research question**: How can we reduce embedding dimensionality in dense retrieval without sacrificing effectiveness while enabling offline, query-independent processing?
**Methodology**: The authors propose a novel static pruning method using Principal Components Analysis (PCA) to reduce embedding dimensionality in a query-independent manner that can be executed offline before query processing.
**Key findings**:
- The method reduces document representation dimensionality by over 50%
- Achieves only up to 5% reduction in NDCG@10, indicating minimal effectiveness loss
- Works across different dense retrieval models
- Enables significant boost in dense retrieval efficiency through offline processing
- Query-independent approach avoids additional computations during query processing
**Limitations**: Some effectiveness loss occurs (up to 5% NDCG@10 reduction); the method may not perform equally well across all retrieval scenarios and query types.

### Su et al. (2026)

**Research question**: How can dense retrieval systems adapt to new domains with limited training data and support frequent model updates without expensive retraining from scratch?
**Methodology**: Proposes dynamic dense retrieval (DDR) using prefix tuning as domain-specialized modules that can be compositionally combined with a dynamic routing strategy for flexible domain adaptation.
**Key findings**:
- Surpasses traditional dense retrieval while utilizing only 2% of training parameters
- Enables highly flexible domain adaptation through compositional combination of prefix tuning modules
- Successfully evaluated on six zero-shot downstream tasks demonstrating strong generalization
- Avoids prohibitive costs of training new models from scratch for frequent updates
- Represents a promising future direction for applying dense retrieval across various tasks
**Limitations**: Evaluated on only six downstream tasks, leaving effectiveness on broader task ranges unverified; the dynamic routing strategy adds architectural complexity that may complicate deployment and maintenance.

### Wullach et al. (2026)

**Research question**: How do graded relevance scores and the thresholds used to convert them into binary labels affect multilingual dense retrieval performance?
**Methodology**: The authors analyze graded relevance scores using a multilingual dataset with LLM-annotated relevance scores, examining monolingual, multilingual mixture, and cross-lingual retrieval scenarios to understand threshold effects.
**Key findings**:
- Optimal relevance threshold varies systematically across languages and tasks
- Threshold differences often reflect variations in language resource levels
- Well-chosen thresholds improve effectiveness and reduce fine-tuning data requirements
- Proper threshold calibration can mitigate annotation noise
- Poorly chosen thresholds can significantly degrade retrieval performance
**Limitations**: Requires careful threshold calibration per language and task; depends on the quality of LLM-annotated relevance scores which may introduce bias.

### Yang et al. (2024)

**Research question**: How do generative retrieval and sequential dense retrieval compare under fair conditions, and can they be combined to leverage their respective strengths?
**Methodology**: The authors compare generative and dense retrieval approaches under controlled conditions on academic benchmarks, then propose LIGER, a hybrid model that integrates sequential dense retrieval into generative retrieval using semantic IDs.
**Key findings**:
- Generative retrieval offers memory efficiency advantages over dense retrieval for large-scale applications
- LIGER hybrid model mitigates performance differences between the two approaches
- The hybrid approach enhances cold-start item recommendation performance
- Comprehensive comparison under fair conditions reveals distinct performance and computation trade-offs
- Semantic IDs encapsulating item semantics enable effective generative retrieval
**Limitations**: Evaluation conducted on small-scale benchmarks only; memory requirements of dense retrieval become more problematic as item catalogs grow to industrial scale.

### Zhang et al. (2024)

**Research question**: Can current dense retrieval systems comprehend and correctly process Boolean logic implicitly contained in natural language queries?
**Methodology**: The authors formulate Boolean Dense Retrieval as a task, collect the BoolQuestions benchmark dataset with complex Boolean queries and annotated passages, and explore a contrastive continual training method with decomposed query operations.
**Key findings**:
- Current dense retrieval systems do not fully understand Boolean logic in language
- BoolQuestions benchmark provides a standardized evaluation framework for Boolean retrieval
- Existing training objectives overlook Boolean logic inherent in language
- Contrastive continual training on decomposed queries serves as a strong baseline
- Significant improvement is needed for dense retrieval systems to handle Boolean reasoning
**Limitations**: The proposed contrastive continual training method is a baseline that still has considerable room for improvement; Boolean logic understanding remains a fundamental gap in current dense retrieval systems.

## References

Chen, H., Ai, Q., Wang, X., Liu, Y., Lin, F., & Liu, Q. (2024). Unsupervised dense retrieval with counterfactual contrastive learning. arXiv. https://arxiv.org/abs/2412.20756

Erker, J.-J., Reimers, N., & Gurevych, I. (2025). GRITHopper: Decomposition-free multi-hop dense retrieval. arXiv. https://arxiv.org/abs/2503.07519

Huang, C., Mo, F., Chen, Y., Guan, C., Yue, Z., Wang, X., Xu, J., & Huang, K. (2025). Boosting data utilization for multilingual dense retrieval. arXiv. https://arxiv.org/abs/2509.09459

Huang, S., Zhang, C., Wu, Y., Zhang, H., Wang, Y., Wang, M., Cao, S., Xu, T., Zhao, X., Qin, Z., Gao, Y., Bai, Y., Fan, J., Hu, Y., & Chen, E. (2024). ScalingNote: Scaling up retrievers with large language models for real-world dense retrieval. arXiv. https://arxiv.org/abs/2411.15766

Pandey, M. (2026). Domain-adaptive and scalable dense retrieval for content-based recommendation. arXiv. https://arxiv.org/abs/2602.00899

Siciliano, F., Pezzuti, F., Tonellotto, N., & Silvestri, F. (2024). Static pruning in dense retrieval using matrix decomposition. arXiv. https://arxiv.org/abs/2412.09983

Su, Z., Mo, F., Zhang, J., Hui, Y., Sun, J. A., Wen, B., & Nie, J.-Y. (2026). Towards dynamic dense retrieval with routing strategy. arXiv. https://arxiv.org/abs/2602.22547

Wullach, T., Shapira, O., & Cohen, A. D. N. (2026). The overlooked role of graded relevance thresholds in multilingual dense retrieval. arXiv. https://arxiv.org/abs/2601.04395

Yang, L., Paischer, F., Hassani, K., Li, J., Shao, S., Li, Z. G., He, Y., Feng, X., Noorshams, N., Park, S., Long, B., Nowak, R. D., Gao, X., & Eghbalzadeh, H. (2024). Unifying generative and dense retrieval for sequential recommendation. arXiv. https://arxiv.org/abs/2411.18814

Zhang, Z., Zhu, J., Zhou, W., Qi, X., Zhang, P., & Li, H. (2024). BoolQuestions: Does dense retrieval understand Boolean logic in language? arXiv. https://arxiv.org/abs/2411.12235
