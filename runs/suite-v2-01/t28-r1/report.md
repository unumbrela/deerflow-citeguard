# Systematic Literature Review: Dense Retrieval

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search "dense retrieval", category cs.IR, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on dense retrieval in the information retrieval category (cs.IR) from the past two years. The surveyed literature reveals a field rapidly evolving along multiple dimensions: efficiency optimization through model scaling and dimensionality reduction, adaptation to new domains and languages, and novel approaches to training without supervision. A notable trend is the integration of large language models (LLMs) into dense retrieval systems, with papers exploring both training-based and training-free approaches. The research demonstrates significant progress in multi-hop retrieval, multilingual capabilities, and handling complex query structures including Boolean logic. However, challenges remain in annotation requirements, threshold calibration, and computational efficiency for real-world deployment.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "dense retrieval", filtered to category cs.IR, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Efficiency and Scalability Optimization

A major research direction focuses on making dense retrieval more efficient and scalable for real-world deployment. Siciliano et al. (2024) address the computational burden through static pruning using matrix decomposition, reducing embedding dimensionality by over 50% with only a 5% reduction in retrieval effectiveness. Their query-independent approach can be executed offline, avoiding additional computation during query processing.

Huang et al. (2024) tackle the scaling challenge from a different angle, proposing ScalingNote, a two-stage method that exploits the scaling potential of large language models while maintaining acceptable online query latency. By training dual towers initialized from the same LLM and then distilling only the query tower, they achieve cost-effective scaling that outperforms end-to-end models in industrial scenarios.

Erker et al. (2025) contribute to this theme with GRITHopper-7B, which combines generative and representational instruction tuning to create a robust, scalable solution for multi-hop dense retrieval that generalizes well to out-of-distribution data.

### Theme 2: Dynamic and Adaptable Retrieval Systems

Recent work emphasizes the need for dense retrieval systems that can adapt to new domains and evolve over time without prohibitive retraining costs. Su et al. (2026) propose dynamic dense retrieval (DDR) using prefix tuning as domain-specific modules combined with a dynamic routing strategy. Their approach achieves performance surpassing traditional dense retrieval while utilizing only 2% of the training parameters, enabling highly flexible domain adaptation.

This adaptability extends to multilingual contexts, where Huang et al. (2025) focus on boosting data utilization through better negative sample selection and effective mini-batch data efficacy. Their method demonstrates that focusing on data utilization rather than model architecture improvements can enhance retrieval effectiveness across 16 languages on the MIRACL benchmark.

### Theme 3: Training-Free and Unsupervised Approaches

A significant trend is the development of dense retrieval methods that reduce or eliminate the need for supervised training. Jedidi et al. (2026) introduce RICE (Representations from In-Context Examples), a training-free approach that extracts dense representations from LLMs by conditioning on examples that provide shared context for query and document encoding. Their work demonstrates that LLMs can produce effective representations for dense retrieval with only a few in-context examples.

Chen et al. (2024) contribute an unsupervised approach using counterfactual contrastive learning based on game theory. Their method extracts key passages without reliance on passage-level relevance annotations, while enhancing model robustness against adversarial attacks and improving explainability by analyzing which parts of documents are relevant to queries.

### Theme 4: Integration with Generative Models

The boundary between dense retrieval and generative models is increasingly blurred. Yang et al. (2024) explore the performance and computation trade-offs between generative retrieval and sequential dense retrieval for recommendation systems. They propose LIGER, a hybrid model that integrates sequential dense retrieval into generative retrieval, mitigating performance differences and enhancing cold-start item recommendation.

Erker et al. (2025) similarly bridge these paradigms by integrating causal language modeling with dense retrieval training, incorporating post-retrieval language modeling with elements like final answers during training. This combination achieves state-of-the-art performance on both in-distribution and out-of-distribution benchmarks.

### Theme 5: Understanding Retrieval Limitations and Edge Cases

Several papers investigate fundamental limitations and edge cases in current dense retrieval systems. Zhang et al. (2024) formulate the task of Boolean Dense Retrieval and collect the BoolQuestions benchmark dataset, revealing that current dense retrieval systems do not fully understand Boolean logic in language. Their work identifies significant room for improvement and provides a baseline for future research.

Wullach et al. (2026) examine the overlooked role of graded relevance thresholds in multilingual dense retrieval, finding that the optimal threshold varies systematically across languages and tasks. Their analysis demonstrates that proper threshold calibration can improve effectiveness, reduce fine-tuning data requirements, and mitigate annotation noise.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of leveraging large language models for dense retrieval, whether through scaling (Huang et al., 2024), training-free approaches (Jedidi et al., 2026), or hybrid architectures (Erker et al., 2025; Yang et al., 2024). There is also broad agreement that efficiency and adaptability are critical challenges, with several papers proposing methods to reduce computational costs while maintaining effectiveness (Siciliano et al., 2024; Su et al., 2026).

The literature consistently demonstrates that improvements in data utilization and training strategies can yield significant gains without architectural changes (Huang et al., 2025; Chen et al., 2024). Additionally, multiple papers emphasize the importance of handling complex retrieval scenarios, including multi-hop queries (Erker et al., 2025), Boolean logic (Zhang et al., 2024), and multilingual contexts (Wullach et al., 2026; Huang et al., 2025).

**Disagreements**: While not explicit disagreements, the papers reflect different philosophical approaches to the role of training. Some works advocate for sophisticated training strategies and model scaling (Huang et al., 2024; Erker et al., 2025), while others demonstrate that training-free or unsupervised approaches can achieve competitive results (Jedidi et al., 2026; Chen et al., 2024). This tension suggests an ongoing debate about the necessity of extensive supervised training versus leveraging pre-trained LLM capabilities.

The integration of generative and retrieval models also presents different approaches: Yang et al. (2024) focus on recommendation systems with semantic IDs, while Erker et al. (2025) integrate post-retrieval language modeling for multi-hop retrieval, reflecting different priorities in how these paradigms should be combined.

## Gaps and Open Questions

Several gaps emerge from the collective literature:

1. **Annotation Requirements**: Multiple papers acknowledge the challenge of requiring extensive relevance annotations (Chen et al., 2024; Wullach et al., 2026). While unsupervised approaches show promise, the field would benefit from more systematic investigation into minimizing annotation burden.

2. **Threshold Calibration**: Wullach et al. (2026) highlight that graded relevance threshold calibration is often overlooked, yet systematically affects performance across languages and tasks. This suggests a broader need for adaptive calibration methods.

3. **Boolean and Complex Logic Understanding**: Zhang et al. (2024) reveal that dense retrieval systems struggle with Boolean logic, indicating a fundamental gap in semantic understanding that extends beyond simple relevance matching.

4. **Real-World Deployment Challenges**: While several papers address efficiency (Siciliano et al., 2024; Huang et al., 2024), the gap between research prototypes and production systems remains significant, particularly for multilingual and cross-lingual scenarios.

5. **Explainability**: Chen et al. (2024) note that enhanced sensitivity to relevance-determining passages improves explainability, but this remains an underexplored area across the surveyed literature.

6. **Limitations Reporting**: Notably, none of the 10 surveyed papers explicitly stated limitations in their abstracts, suggesting either a gap in self-reflection or space constraints that prevent thorough discussion of methodological limitations.

## Per-Paper Annotations

### Chen et al. (2024)

**Research question**: How can the robustness and explainability of dense retrieval models be improved by enhancing their sensitivity to fine-grained relevance signals?

**Methodology**: The authors propose counterfactual regularization methods based on game theory and unsupervised learning with counterfactual passages to improve model sensitivity to key relevance-determining passages.

**Key findings**:
- The method can extract key passages without reliance on passage-level relevance annotations
- Regularized dense retrieval models exhibit heightened robustness against adversarial attacks
- The approach surpasses state-of-the-art anti-attack methods
- Enhanced sensitivity makes it possible to analyze which parts of documents are relevant to queries, improving explainability

**Limitations**: Not stated in abstract.

### Erker et al. (2025)

**Research question**: How can decomposition-free multi-hop dense retrieval be improved to handle longer multi-hop problems and generalize better to out-of-distribution data?

**Methodology**: The authors introduce GRITHopper-7B, which combines generative and representational instruction tuning by integrating causal language modeling with dense retrieval training, incorporating post-retrieval language modeling with elements like final answers during training.

**Key findings**:
- GRITHopper-7B achieves state-of-the-art performance on both in-distribution and out-of-distribution benchmarks
- Post-retrieval language modeling enhances dense retrieval performance
- Including final answers during training helps the model better contextualize and retrieve relevant information
- The approach provides a robust, scalable, and generalizable solution for multi-hop dense retrieval

**Limitations**: Not stated in abstract.

### Huang et al. (2024)

**Research question**: How can the scaling potential of large language models be exploited for dense retrieval while maintaining acceptable online query latency?

**Methodology**: The authors propose ScalingNote, a two-stage method: first training dual towers initialized from the same LLM, then distilling only the query tower using mean squared error loss and cosine similarity to reduce online costs.

**Key findings**:
- The two-stage scaling method outperforms end-to-end models
- The approach verifies the scaling law of dense retrieval with LLMs in industrial scenarios
- The method enables cost-effective scaling of dense retrieval systems
- Online incorporation of ScalingNote significantly enhances relevance between retrieved documents and queries

**Limitations**: Not stated in abstract.

### Huang et al. (2025)

**Research question**: How can data utilization be improved for multilingual dense retrieval through better negative sample selection and mini-batch data efficacy?

**Methodology**: Proposed method to obtain high-quality hard negative samples and effective mini-batch data, evaluated on the MIRACL multilingual retrieval benchmark with 16 languages.

**Key findings**:
- The method outperforms several existing strong baselines on the MIRACL benchmark
- Focus on data utilization rather than model architecture improvements can enhance retrieval effectiveness
- High-quality hard negative samples improve contrastive learning for multilingual dense retrieval
- Effective mini-batch data selection contributes to better cross-lingual representation alignment

**Limitations**: Not stated in abstract.

### Jedidi et al. (2026)

**Research question**: Can large language models produce effective dense representations for retrieval using only in-context examples without training?

**Methodology**: Introduced RICE (Representations from In-Context Examples), a training-free approach that extracts dense representations from LLMs by conditioning on examples that provide shared context for query and document encoding.

**Key findings**:
- RICE embeddings can substantially improve the accuracy of prompt-based LLM embeddings
- LLMs can be prompted to produce effective representations for dense retrieval with only a few in-context examples
- The approach establishes a simple method to build LLM-based dense retrievers without training
- The code is publicly released at https://github.com/nourj98/RICE

**Limitations**: Not stated in abstract.

### Siciliano et al. (2024)

**Research question**: How can embedding dimensionality be reduced in dense retrieval using a query-independent method that can be executed offline without impacting retrieval efficiency?

**Methodology**: The authors present a novel static pruning method using Principal Components Analysis to reduce embedding dimensionality in a query-independent manner that can be executed offline.

**Key findings**:
- The method reduces dimensionality of document representations by over 50%
- The reduction comes with up to only 5% reduction in NDCG@10 for different dense retrieval models
- The approach leads to significant boost in dense retrieval efficiency with negligible impact on effectiveness
- Unlike query-dependent methods, this approach does not require additional computations during query processing

**Limitations**: Not stated in abstract.

### Su et al. (2026)

**Research question**: How can dense retrieval be adapted more flexibly to new domains and updated frequently without the prohibitive expense of training from scratch?

**Methodology**: The authors propose dynamic dense retrieval (DDR) using prefix tuning as domain-specific modules that can be compositionally combined with a dynamic routing strategy for flexible domain adaptation.

**Key findings**:
- DDR can surpass traditional dense retrieval while utilizing only 2% of the training parameters
- The approach enables highly flexible domain adaptation in the retrieval component
- Extensive evaluation on six zero-shot downstream tasks demonstrates the effectiveness of the method
- The paradigm offers a promising direction for applying dense retrieval to various tasks

**Limitations**: Not stated in abstract.

### Wullach et al. (2026)

**Research question**: How do graded relevance scores and the threshold used to convert them into binary labels affect multilingual dense retrieval performance?

**Methodology**: Analysis using a multilingual dataset with LLM-annotated relevance scores across monolingual, multilingual mixture, and cross-lingual retrieval scenarios.

**Key findings**:
- The optimal threshold varies systematically across languages and tasks, often reflecting differences in resource level
- A well-chosen threshold can improve effectiveness and reduce the amount of fine-tuning data required
- Proper threshold calibration can mitigate annotation noise
- A poorly chosen threshold can degrade performance
- Graded relevance is a valuable but underutilized signal for dense retrieval

**Limitations**: Not stated in abstract.

### Yang et al. (2024)

**Research question**: What are the performance and computation trade-offs between generative retrieval and sequential dense retrieval, and can they be combined for improved recommendation?

**Methodology**: Comparison of generative retrieval and sequential dense retrieval under controlled conditions on academic benchmarks, plus proposal of LIGER, a hybrid model combining both approaches.

**Key findings**:
- Sequential dense retrieval requires significant memory as item representations grow
- Generative retrieval offers a promising alternative by directly predicting item indices using semantic IDs
- LIGER integrates sequential dense retrieval into generative retrieval, mitigating performance differences
- The hybrid approach enhances cold-start item recommendation in the evaluated datasets
- The approach provides insights into efficiency and effectiveness trade-offs for recommendation systems

**Limitations**: Not stated in abstract.

### Zhang et al. (2024)

**Research question**: Do current dense retrieval systems comprehend the Boolean logic implied in language?

**Methodology**: Formulated the task of Boolean Dense Retrieval and collected a benchmark dataset (BoolQuestions) covering complex queries with Boolean logic and annotated passages; explored contrastive continual training method as a baseline.

**Key findings**:
- Current dense retrieval systems do not fully understand Boolean logic in language
- Existing training objectives overlook Boolean logic inherent in language
- There is significant room for improvement in dense retrieval systems' Boolean logic comprehension
- Boolean operation on decomposed query with contrastive continual training serves as a strong baseline
- The BoolQuestions benchmark dataset promotes further research on Boolean logic understanding

**Limitations**: Not stated in abstract.

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
