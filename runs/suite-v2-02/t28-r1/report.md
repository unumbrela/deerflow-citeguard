# Systematic Literature Review: Dense Retrieval

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "dense retrieval", filtered to category cs.IR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent papers on dense retrieval from the cs.IR category published between late 2024 and 2026. The surveyed literature reveals a field rapidly evolving along multiple dimensions: efficiency optimization through model compression and dynamic architectures, multilingual and cross-lingual retrieval challenges, integration with large language models, and fundamental investigations into retrieval model understanding. Researchers are increasingly focused on making dense retrieval more practical for real-world deployment through parameter-efficient methods, dimensionality reduction, and training-free approaches leveraging in-context learning. At the same time, critical gaps remain in retrieval models' understanding of complex logical reasoning and the systematic handling of graded relevance signals across languages.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "dense retrieval", filtered to category cs.IR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Scalability Optimization

A dominant theme across the surveyed literature is the pursuit of more efficient dense retrieval systems that maintain effectiveness while reducing computational costs. Siciliano et al. (2024) address embedding dimensionality through static pruning using Principal Components Analysis, achieving over 50% dimensionality reduction with only up to 5% reduction in NDCG@10. This query-independent approach can be executed offline, providing significant efficiency gains without the complexity of query-dependent methods. Similarly, Su et al. (2026) propose Dynamic Dense Retrieval (DDR), which uses prefix tuning as specialized modules that can be compositionally combined with dynamic routing, achieving performance surpassing traditional dense retrieval while utilizing only 2% of training parameters. Huang et al. (2024) tackle the challenge of scaling retrievers with Large Language Models through a two-stage method that trains dual towers initialized from the same LLM, then distills only the query tower to reduce online costs while maintaining retrieval quality.

### Theme 2: Multilingual and Cross-Lingual Retrieval

Several papers address the unique challenges of dense retrieval in multilingual settings. Wullach et al. (2026) investigate the overlooked role of graded relevance thresholds, demonstrating that the optimal threshold for converting graded relevance scores to binary labels varies systematically across languages and tasks, often reflecting differences in resource levels. Their work shows that a well-chosen threshold can improve effectiveness, reduce fine-tuning data requirements, and mitigate annotation noise. Huang et al. (2025) focus on boosting data utilization for multilingual dense retrieval by obtaining high-quality hard negative samples and effective mini-batch data, demonstrating effectiveness across 16 languages on the MIRACL benchmark. These works collectively highlight that multilingual retrieval requires careful attention to language-specific characteristics and data quality rather than simply applying monolingual approaches across languages.

### Theme 3: Integration with Generative Approaches and LLMs

The boundary between dense retrieval and generative approaches is increasingly blurred, with several papers exploring hybrid architectures. Erker et al. (2025) introduce GRITHopper-7B, which combines generative and representational instruction tuning by integrating causal language modeling with dense retrieval training for multi-hop retrieval. Their work demonstrates that incorporating post-retrieval language modeling, including elements such as final answers during training, enhances dense retrieval performance. Yang et al. (2024) propose LIGER, a hybrid model unifying generative and dense retrieval for sequential recommendation, integrating sequential dense retrieval into generative retrieval to mitigate performance differences while enhancing cold-start item recommendation. Most recently, Jedidi et al. (2026) introduce RICE (Representations from In-Context Examples), a training-free approach that extracts high-quality dense representations from LLMs by conditioning on examples, establishing a simple method to build LLM-based dense retrievers without requiring training.

### Theme 4: Fundamental Understanding and Reasoning Capabilities

Several papers investigate fundamental limitations in current dense retrieval systems' understanding. Zhang et al. (2024) examine whether dense retrieval systems understand Boolean logic in language, finding that current systems do not fully comprehend Boolean logic despite focusing on optimizing embedding space for text pair relevance. They propose a contrastive continual training method as a baseline for future research. Chen et al. (2024) address robustness and explainability through counterfactual contrastive learning, designing models that exhibit high variance when key passages determining relevance are modified and low variance for changes in irrelevant passages. Their method can extract key passages without reliance on passage-level relevance annotations and provides heightened robustness against adversarial attacks while improving explainability of which document parts are actually relevant to queries.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree that traditional dense retrieval approaches require significant enhancement for practical deployment, with consensus around the need for parameter-efficient methods, better multilingual handling, and integration with LLM capabilities. Multiple papers demonstrate that incorporating additional context or signals beyond basic query-document matching improves retrieval performance (Erker et al., 2025; Chen et al., 2024; Wullach et al., 2026). There is also convergence around the finding that data quality and utilization strategies can be as important as model architecture improvements (Huang et al., 2025; Huang et al., 2024).

**Disagreements**: The literature shows tension between training-intensive approaches and training-free methods. While most papers propose new training methodologies or architectural modifications (Erker et al., 2025; Su et al., 2026; Huang et al., 2024), Jedidi et al. (2026) demonstrate that training-free in-context approaches can produce effective representations, suggesting a fundamentally different path forward. Additionally, there is implicit disagreement about the role of graded relevance: Wullach et al. (2026) argue it is underutilized and valuable, while other papers proceed with binary relevance assumptions without addressing this dimension.

## Gaps and Open Questions

The collective literature reveals several significant gaps. First, none of the surveyed papers explicitly state limitations in their abstracts, suggesting either space constraints or a tendency to emphasize contributions over limitations — this makes it difficult to assess the boundaries of proposed methods. Second, while several papers address multilingual retrieval, there is limited investigation into low-resource languages beyond the 16 languages covered in MIRACL benchmark studies. Third, the Boolean logic understanding gap identified by Zhang et al. (2024) suggests fundamental reasoning capabilities remain underdeveloped, yet few other papers address this dimension. Fourth, the tension between training-intensive and training-free approaches remains unresolved, with insufficient comparative analysis of when each paradigm is preferable. Finally, the practical deployment challenges of integrating these advanced retrieval methods into production systems with strict latency requirements receive limited attention beyond the ScalingNote work (Huang et al., 2024).

## Per-Paper Annotations

### Chen et al. (2024)

**Research question**: How can the robustness and explainability of dense retrieval models be improved by enhancing their sensitivity to fine-grained relevance signals?
**Methodology**: The authors propose counterfactual regularization methods based on game theory and unsupervised learning with counterfactual passages, motivated by causality and counterfactual analysis, designing a model that exhibits high variance when key passages determining relevance are modified and low variance for changes in irrelevant passages.
**Key findings**:
- The method can extract key passages without reliance on passage-level relevance annotations
- Regularized dense retrieval models exhibit heightened robustness against adversarial attacks
- The approach surpasses state-of-the-art anti-attack methods
- The sensitivity makes it possible to analyze which part of a document is actually relevant to a query, improving explainability
**Limitations**: Not stated in abstract

### Erker et al. (2025)

**Research question**: How can decomposition-free multi-hop dense retrieval methods be improved to handle longer multi-hop problems and generalize better to out-of-distribution data?
**Methodology**: The authors introduce GRITHopper-7B, a multi-hop dense retrieval model that combines generative and representational instruction tuning by integrating causal language modeling with dense retrieval training, conducting controlled studies incorporating post-retrieval language modeling, including elements such as final answers during training.
**Key findings**:
- GRITHopper-7B achieves state-of-the-art performance on both in-distribution and out-of-distribution benchmarks
- Incorporating additional context after the retrieval process (post-retrieval language modeling) enhances dense retrieval performance
- Including elements such as final answers during training helps the model learn to better contextualize and retrieve relevant information
- GRITHopper-7B offers a robust, scalable, and generalizable solution for multi-hop dense retrieval
**Limitations**: Not stated in abstract

### Huang et al. (2024)

**Research question**: How can Large Language Models be leveraged to scale up dense retrieval systems while maintaining acceptable online query latency?
**Methodology**: The authors propose ScalingNote, a two-stage method: first training dual towers initialized from the same LLM to unlock LLM potential for dense retrieval, then distilling only the query tower using mean squared error loss and cosine similarity to reduce online costs, validated through theoretical analysis and comprehensive offline and online experiments.
**Key findings**:
- The two-stage scaling method outperforms end-to-end models
- The approach verifies the scaling law of dense retrieval with LLMs in industrial scenarios
- ScalingNote enables cost-effective scaling of dense retrieval systems
- The online method incorporating ScalingNote significantly enhances the relevance between retrieved documents and queries
**Limitations**: Not stated in abstract

### Huang et al. (2025)

**Research question**: How can data utilization be improved for multilingual dense retrieval by obtaining high-quality hard negative samples and effective mini-batch data?
**Methodology**: The authors propose a method to boost data utilization for multilingual dense retrieval by obtaining high-quality hard negative samples and effective mini-batch data, evaluated on the MIRACL benchmark with 16 languages.
**Key findings**:
- The proposed method outperforms several existing strong baselines on the MIRACL multilingual retrieval benchmark
- The approach focuses on data utilization rather than developing sophisticated model architecture
- The method demonstrates effectiveness across 16 different languages
**Limitations**: Not stated in abstract

### Jedidi et al. (2026)

**Research question**: Can large language models produce effective representations for dense retrieval given only a few in-context examples without retriever training?
**Methodology**: The authors introduce RICE (Representations from In-Context Examples), a training-free approach that extracts high-quality dense representations from LLMs by conditioning on examples that provide a shared context for query and document encoding.
**Key findings**:
- RICE embeddings can substantially improve the accuracy of prompt-based LLM embeddings
- RICE establishes a simple method to build LLM-based dense retrievers that do not require training
- LLMs can be prompted to produce effective representations for dense retrieval using only in-context examples
**Limitations**: Not stated in abstract

### Siciliano et al. (2024)

**Research question**: How can embedding dimensionality be reduced in dense retrieval systems offline without sacrificing retrieval effectiveness?
**Methodology**: The authors present a novel static pruning method for reducing embedding dimensionality using Principal Components Analysis, which is query-independent and can be executed offline, experimenting with different dense retrieval models to evaluate the impact on efficiency and effectiveness.
**Key findings**:
- The proposed method reduces the dimensionality of document representations by over 50%
- The reduction comes with up to a 5% reduction in NDCG@10 for different dense retrieval models
- The approach leads to a significant boost in dense retrieval efficiency
- The method has negligible impact on system effectiveness compared to query-dependent pruning methods
**Limitations**: Not stated in abstract

### Su et al. (2026)

**Research question**: How can dense retrieval be made more flexible and cost-effective for domain adaptation and frequent model updates?
**Methodology**: The authors propose dynamic dense retrieval (DDR), which uses prefix tuning as specialized modules for specific domains that can be compositionally combined with a dynamic routing strategy for flexible domain adaptation, evaluating the approach on six zero-shot downstream tasks.
**Key findings**:
- DDR can surpass traditional dense retrieval while utilizing only 2% of the training parameters
- The approach enables highly flexible domain adaptation in the retrieval part
- Prefix tuning modules can be dynamically combined with a routing strategy for efficient updates
- DDR provides a promising direction for applying dense retrieval to various tasks without expensive retraining
**Limitations**: Not stated in abstract

### Wullach et al. (2026)

**Research question**: How do graded relevance scores and the threshold used to convert them into binary labels affect multilingual dense retrieval performance?
**Methodology**: The authors analyze graded relevance scores using a multilingual dataset with LLM-annotated relevance scores, examining monolingual, multilingual mixture, and cross-lingual retrieval scenarios.
**Key findings**:
- The optimal threshold varies systematically across languages and tasks, often reflecting differences in resource level
- A well-chosen threshold can improve effectiveness, reduce the amount of fine-tuning data required, and mitigate annotation noise
- A poorly chosen threshold can degrade performance
- Graded relevance is a valuable but underutilized signal for dense retrieval
**Limitations**: Not stated in abstract

### Yang et al. (2024)

**Research question**: What are the performance and computation trade-offs between generative retrieval and sequential dense retrieval, and can they be combined effectively?
**Methodology**: The authors compare generative retrieval and sequential dense retrieval under controlled conditions on academic benchmarks, then propose LIGER, a hybrid model combining both approaches.
**Key findings**:
- Sequential dense retrieval requires storing unique representations for each item, resulting in significant memory requirements as items grow
- Generative retrieval offers a promising alternative by directly predicting item indices using semantic IDs
- LIGER integrates sequential dense retrieval into generative retrieval, mitigating performance differences
- The hybrid approach enhances cold-start item recommendation in the evaluated datasets
- The approach provides insights into trade-offs between efficiency and effectiveness for recommendation systems
**Limitations**: Not stated in abstract

### Zhang et al. (2024)

**Research question**: Can current dense retrieval systems comprehend the Boolean logic implied in language?
**Methodology**: The authors formulate the task of Boolean Dense Retrieval and collect a benchmark dataset called BoolQuestions covering complex queries with Boolean logic and corresponding annotated passages, then conduct extensive experiments on current retrieval systems.
**Key findings**:
- Current dense retrieval systems do not fully understand Boolean logic in language
- Current systems focus on optimizing the embedding space by attending to relevance of text pairs while overlooking Boolean logic
- The authors propose a contrastive continual training method as a strong baseline for the research community
- There is significant room for improvement in dense retrieval systems' understanding of Boolean logic
**Limitations**: Not stated in abstract

## References

Chen, H., Ai, Q., Wang, X., Liu, Y., Lin, F., & Liu, Q. (2024). Unsupervised dense retrieval with conterfactual contrastive learning. arXiv. https://arxiv.org/abs/2412.20756

Erker, J.-J., Reimers, N., & Gurevych, I. (2025). GRITHopper: Decomposition-free multi-hop dense retrieval. arXiv. https://arxiv.org/abs/2503.07519

Huang, C., Mo, F., Chen, Y., Guan, C., Yue, Z., Wang, X., Xu, J., & Huang, K. (2025). Boosting data utilization for multilingual dense retrieval. arXiv. https://arxiv.org/abs/2509.09459

Huang, S., Zhang, C., Wu, Y., Zhang, H., Wang, Y., Wang, M., Cao, S., Xu, T., Zhao, X., Qin, Z., Gao, Y., Bai, Y., Fan, J., Hu, Y., & Chen, E. (2024). ScalingNote: Scaling up retrievers with large language models for real-world dense retrieval. arXiv. https://arxiv.org/abs/2411.15766

Jedidi, N., Ali, A. B., Li, H., & Lin, J. (2026). Effective dense retrieval using only in-context examples. arXiv. https://arxiv.org/abs/2609.38099

Siciliano, F., Pezzuti, F., Tonellotto, N., & Silvestri, F. (2024). Static pruning in dense retrieval using matrix decomposition. arXiv. https://arxiv.org/abs/2412.09983

Su, Z., Mo, F., Zhang, J., Hui, Y., Sun, J. A., Wen, B., & Nie, J.-Y. (2026). Towards dynamic dense retrieval with routing strategy. arXiv. https://arxiv.org/abs/2602.22547

Wullach, T., Shapira, O., & Cohen, A. D. N. (2026). The overlooked role of graded relevance thresholds in multilingual dense retrieval. arXiv. https://arxiv.org/abs/2601.04395

Yang, L., Paischer, F., Hassani, K., Li, J., Shao, S., Li, Z. G., He, Y., Feng, X., Noorshams, N., Park, S., Long, B., Nowak, R. D., Gao, X., & Eghbalzadeh, H. (2024). Unifying generative and dense retrieval for sequential recommendation. arXiv. https://arxiv.org/abs/2411.18814

Zhang, Z., Zhu, J., Zhou, W., Qi, X., Zhang, P., & Li, H. (2024). BoolQuestions: Does dense retrieval understand Boolean logic in language? arXiv. https://arxiv.org/abs/2411.12235
