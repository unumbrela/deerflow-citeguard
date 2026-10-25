# Systematic Literature Review: Dense Retrieval

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv query "dense retrieval", category cs.IR, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on dense retrieval published between 2024 and 2026. The surveyed literature reveals a field rapidly evolving along multiple dimensions: scaling strategies leveraging large language models, domain adaptation techniques for specialized applications, multi-hop reasoning capabilities, and critical considerations around privacy and robustness. Collectively, these papers demonstrate that dense retrieval has matured beyond basic dual-encoder architectures, with researchers addressing practical deployment challenges including computational efficiency, domain generalization, and security vulnerabilities. The field shows strong convergence on the effectiveness of contrastive learning approaches, while diverging on optimal strategies for scaling, adaptation, and balancing performance with practical constraints.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "dense retrieval", filtered to category cs.IR, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Scaling Laws and Large Language Model Integration

A prominent research direction involves understanding and exploiting scaling relationships in dense retrieval. Fang et al. (2024) established that dense retrieval performance follows precise power-law scaling with both model size and training data volume, providing a theoretical foundation for resource allocation decisions. Building on this insight, Huang et al. (2024) proposed ScalingNote, a two-stage approach that trains dual towers from LLMs then distills only the query tower to maintain online efficiency while preserving scaling benefits. These works collectively suggest that the field is transitioning from architecture-centric innovations to systematic scaling strategies that leverage LLM capabilities while managing computational costs. The convergence on distillation as a key technique reflects practical deployment constraints in industrial settings.

### Theme 2: Domain Adaptation and Flexible Deployment

Multiple papers address the challenge of adapting dense retrieval models to new domains without expensive retraining. Li and Gaussier (2024) combined query generation with self-supervised pseudo-relevance labeling using T5-3B, achieving improvements over adversarial learning approaches. Su et al. (2026) introduced Dynamic Dense Retrieval (DDR), which uses prefix tuning modules combined through dynamic routing, enabling flexible domain adaptation with only 2% of training parameters. Pandey (2026) demonstrated a practical blueprint for domain-adaptive retrieval in e-commerce, fine-tuning on Amazon Reviews with FAISS HNSW indexing for efficient serving. These approaches share a commitment to reducing the cost and complexity of domain adaptation, though they differ in their reliance on large models versus modular architectures.

### Theme 3: Multi-Hop and Complex Reasoning

Extending dense retrieval beyond single-hop queries represents another active research frontier. Erker et al. (2025) introduced GRITHopper-7B, a decomposition-free multi-hop retrieval model combining generative and representational instruction tuning with causal language modeling. By incorporating post-retrieval language modeling with elements like final answers during training, the model achieves state-of-the-art performance on both in-distribution and out-of-distribution benchmarks while maintaining end-to-end differentiability. This work addresses a critical limitation of decomposition-based methods that rely on autoregressive steps, positioning multi-hop retrieval as an increasingly important capability for complex information-seeking tasks.

### Theme 4: Theoretical Understanding and Model Interpretation

Several papers seek deeper theoretical understanding of dense retrieval mechanisms. Wu et al. (2024) demonstrated that generative retrieval can be understood as a special case of multi-vector dense retrieval, with both computing relevance as sums of products of query and document vectors with alignment matrices. This theoretical bridge reveals commonalities in term matching between seemingly distinct paradigms. Such foundational work enables more principled model design and suggests that apparent architectural differences may mask underlying similarities in how retrieval systems measure relevance.

### Theme 5: Knowledge Distillation and Training Strategies

Improving dense retrieval through advanced training methodologies is a recurring theme. Huang and Chen (2024) introduced PairDistill, which leverages pairwise reranking rather than pointwise approaches for knowledge distillation, achieving state-of-the-art results by providing fine-grained distinctions between similarly relevant documents. This addresses inconsistent comparison challenges in existing distillation methods. The success of pairwise approaches suggests that the quality of training signals, not just model architecture, critically determines retrieval performance.

### Theme 6: Privacy, Security, and Robustness

As dense retrieval systems see wider deployment, privacy and robustness concerns have emerged as important research directions. Zhuang et al. (2024) investigated the Vec2Text threat—embedding inversion attacks that can reconstruct original text—and analyzed factors affecting recoverability including distance metrics, pooling functions, and embedding quantization. They proposed an embedding transformation that maintains ranking effectiveness while mitigating recoverability risk. Chen et al. (2024) addressed robustness through counterfactual contrastive learning, training models to be sensitive to fine-grained relevance signals while resisting adversarial attacks. These papers collectively highlight that deployment-ready dense retrieval systems must balance effectiveness with security and explainability considerations.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the effectiveness of contrastive learning approaches for training dense retrieval models (Pandey, 2026; Fang et al., 2024; Chen et al., 2024). There is also broad agreement that scaling model size and training data improves performance, though optimal strategies for managing computational costs remain debated. All surveyed papers acknowledge the importance of balancing retrieval effectiveness with practical deployment constraints including latency, model size, and training costs.

**Disagreements**: The literature shows divergence on optimal scaling strategies. While Fang et al. (2024) and Huang et al. (2024) advocate for LLM-based scaling with distillation, Su et al. (2026) demonstrate that parameter-efficient prefix tuning can achieve strong results with minimal training overhead. Similarly, while Erker et al. (2025) pursue larger generative models for multi-hop reasoning, other work emphasizes efficiency through quantization and indexing optimization (Pandey, 2026). The field has not yet converged on whether future gains will come from scaling, architectural innovation, or training methodology improvements.

## Gaps and Open Questions

Several gaps emerge from the collective limitations acknowledged across the surveyed papers:

1. **Generalization across domains**: Multiple papers note that their approaches may not generalize well to all domains or query types (Li & Gaussier, 2024; Chen et al., 2024; Huang et al., 2024). Systematic evaluation across diverse domains remains limited.

2. **Computational cost analysis**: Several papers acknowledge high computational costs from large models (T5-3B in Li & Gaussier, 2024; 7B parameters in Erker et al., 2025) without detailed cost-benefit comparisons to alternative approaches.

3. **Production-scale evaluation**: While some papers report production metrics (Pandey, 2026; Huang et al., 2024), many evaluations remain at benchmark scale without concurrent load testing or real-world latency measurements.

4. **Privacy-robustness trade-offs**: Zhuang et al. (2024) identify effective mitigations for Vec2Text attacks, but the broader landscape of privacy threats and their interactions with retrieval effectiveness requires further exploration.

5. **Annotation quality and scaling**: Fang et al. (2024) examine data augmentation impacts, but the field lacks comprehensive understanding of how annotation quality interacts with scaling laws across different retrieval tasks.

## Per-Paper Annotations

### Chen et al. (2024)

**Research question**: How can dense retrieval models be made more robust and explainable by improving their sensitivity to fine-grained relevance signals without requiring passage-level annotations?
**Methodology**: Proposed counterfactual regularization methods based on game theory and unsupervised learning with counterfactual passages, training models to exhibit high variance when key relevance-determining passages are modified while maintaining low variance for irrelevant changes.
**Key findings**:
- The method can extract key passages without reliance on passage-level relevance annotations
- Regularized dense retrieval models exhibit heightened robustness against adversarial attacks
- The approach surpasses state-of-the-art anti-attack methods
- Counterfactual analysis improves model explainability by identifying which document parts are relevant to queries
**Limitations**: Computational cost of generating counterfactual passages during training is not fully characterized; generalization across different domains and query types requires further validation.

### Erker et al. (2025)

**Research question**: How can multi-hop dense retrieval achieve strong performance on longer queries and out-of-distribution data without the computational cost and non-differentiability of decomposition-based methods?
**Methodology**: Developed GRITHopper-7B combining generative and representational instruction tuning by integrating causal language modeling with dense retrieval training, leveraging post-retrieval language modeling with elements like final answers during training.
**Key findings**:
- Achieves state-of-the-art performance on both in-distribution and out-of-distribution benchmarks
- Post-retrieval language modeling enhances dense retrieval performance
- Better generalization to longer multi-hop problems than existing decomposition-free methods
- Maintains end-to-end differentiability unlike decomposition-based approaches
**Limitations**: 7B parameter model size may be prohibitive for resource-constrained deployments; computational cost of generative approach not fully compared to decomposition methods.

### Fang et al. (2024)

**Research question**: Does the performance of dense retrieval models follow predictable scaling laws correlated with model size and training data, similar to other neural models?
**Methodology**: Proposed contrastive log-likelihood as evaluation metric and conducted extensive experiments with dense retrieval models varying in parameter count and training annotation volume to identify power-law relationships.
**Key findings**:
- Dense retrieval performance follows precise power-law scaling with model size and number of annotations
- Scaling laws enable optimal resource allocation strategy under budget constraints
- Examined impact of annotation quality through prevalent data augmentation methods
**Limitations**: Scaling laws may not generalize across all retrieval tasks and metrics; discrete nature of retrieval metrics complicates scaling analysis; findings specific to their experimental settings.

### Huang and Chen (2024)

**Research question**: How can knowledge distillation techniques for dense retrieval be improved by addressing the challenges of inconsistent comparisons in pointwise reranking approaches?
**Methodology**: Introduced Pairwise Relevance Distillation (PairDistill), which leverages pairwise reranking to offer fine-grained distinctions between similarly relevant documents, enriching the training of dense retrieval models beyond pointwise approaches.
**Key findings**:
- PairDistill outperforms existing knowledge distillation methods
- Achieves new state-of-the-art results across multiple benchmarks
- Pairwise reranking provides more fine-grained distinctions than pointwise approaches
- Source code and trained models are publicly released for reproducibility
**Limitations**: Computational overhead of pairwise comparisons during training not fully characterized; dependency on quality of cross-encoder rerankers for distillation.

### Huang et al. (2024)

**Research question**: How can we leverage the scaling potential of Large Language Models for dense retrieval while maintaining acceptable online query latency for real-world deployment?
**Methodology**: ScalingNote employs a two-stage approach: first training dual towers initialized from the same LLM to unlock scaling potential, then distilling only the query tower using mean squared error loss and cosine similarity to reduce online costs while preserving performance.
**Key findings**:
- ScalingNote outperforms end-to-end models in both offline and online experiments
- The two-stage scaling method verifies the scaling law of dense retrieval with LLMs in industrial scenarios
- Online deployment incorporating ScalingNote significantly enhances relevance between retrieved documents and queries
- Knowledge distillation successfully reduces online query latency while maintaining LLM benefits
**Limitations**: Complexity of two-stage training process; potential information loss during distillation; generalization across different LLM architectures and scales requires further validation.

### Li and Gaussier (2024)

**Research question**: How can dense retrieval models be improved to generalize to target domains with different distributions, where prior adversarial learning and query generation approaches showed limited success?
**Methodology**: Combined query-generation with self-supervision using T5-3B for pseudo-positive labeling and meticulous hard negative selection; extended to conversational retrieval with query-rewriting module for conversational query labeling.
**Key findings**:
- Pseudo-relevance labeling on target domain enables effective domain adaptation
- Approach improves over baseline models for both standard and conversational dense retrieval
- Outperforms prior adversarial learning and query generation approaches
- Query-rewriting module enhances conversational dense retrieval performance
**Limitations**: Relies on large T5-3B model for pseudo-labeling, which is computationally expensive; effectiveness may vary across different target domains; hard negative selection process requires careful tuning.

### Pandey (2026)

**Research question**: How can e-commerce recommendation systems overcome vocabulary mismatch when user intent has limited lexical overlap with product metadata?
**Methodology**: Built a two-tower bi-encoder dense retrieval system fine-tuned on Amazon Reviews 2023 (Fashion) using supervised contrastive learning with Multiple Negatives Ranking Loss, combined with FAISS HNSW indexing and ONNX Runtime with INT8 dynamic quantization for efficient CPU serving.
**Key findings**:
- Improved Recall@10 from 0.26 (BM25 baseline) to 0.66 on review-to-title benchmark
- Achieved 6.1 ms median CPU inference latency at batch size 1
- Reduced model size by 4x through INT8 quantization
- Successfully scaled to 826,402 catalog items
**Limitations**: Evaluated only on Fashion subset of Amazon Reviews; CPU latency measurements may not reflect production-scale concurrent load; training limited to 50,000 sampled interactions.

### Su et al. (2026)

**Research question**: How can we address the limitations of fine-tuning dense retrieval models for new tasks, particularly when training data is limited or models need frequent updates?
**Methodology**: Proposed Dynamic Dense Retrieval (DDR), which uses prefix tuning as domain-specialized modules that can be compositionally combined with a dynamic routing strategy for flexible domain adaptation.
**Key findings**:
- DDR surpasses traditional dense retrieval while utilizing only 2% of training parameters
- The modular approach enables highly flexible domain adaptation in retrieval
- Specialized modules can be dynamically combined for different domains
- Extensive evaluation on six zero-shot downstream tasks validates the approach
**Limitations**: Complexity of managing multiple modules and routing strategies; evaluation limited to zero-shot scenarios without testing on tasks requiring substantial training data.

### Wu et al. (2024)

**Research question**: What is the theoretical relationship between generative retrieval and multi-vector dense retrieval, particularly regarding how they measure query-document relevance?
**Methodology**: Analyzed attention layers and prediction heads of generative retrieval to demonstrate it as a special case of multi-vector dense retrieval, examining how both compute relevance through query-document vector products and alignment matrices.
**Key findings**:
- Generative retrieval and multi-vector dense retrieval share the same relevance measurement framework
- Both compute relevance as sum of products of query and document vectors with alignment matrix
- Both paradigms exhibit commonalities in term matching within their alignment matrices
- Bridges understanding between generative and dense retrieval paradigms
**Limitations**: Primarily theoretical analysis that may not capture all practical implementation differences; experimental validation scope not fully detailed.

### Zhuang et al. (2024)

**Research question**: What factors influence text recoverability via Vec2Text in dense retrieval systems, and how can privacy risks be mitigated while maintaining retrieval effectiveness?
**Methodology**: Comprehensively analyzed factors affecting text recoverability (distance metrics, pooling functions, bottleneck pre-training, noise addition, quantization, embedding dimensions) and proposed a simple embedding transformation that maintains ranking effectiveness while mitigating recoverability risk.
**Key findings**:
- Vec2Text poses a genuine threat to current dense retrieval systems using embeddings from providers like OpenAI and Cohere
- Multiple embedding model factors significantly impact text recoverability
- The proposed embedding transformation guarantees equal ranking effectiveness while mitigating recoverability risk
- Provides insights for practitioners designing privacy-aware dense retrieval systems
**Limitations**: Proposed fix may require implementation changes to existing systems; analysis focuses on specific embedding models and attack scenarios that may not cover all Vec2Text variants.

## References

Chen, H., Ai, Q., Wang, X., Liu, Y., Lin, F., & Liu, Q. (2024). Unsupervised dense retrieval with counterfactual contrastive learning. arXiv. https://arxiv.org/abs/2412.20756

Erker, J.-J., Reimers, N., & Gurevych, I. (2025). GRITHopper: Decomposition-free multi-hop dense retrieval. arXiv. https://arxiv.org/abs/2503.07519

Fang, Y., Zhan, J., Ai, Q., Mao, J., Su, W., Chen, J., & Liu, Y. (2024). Scaling laws for dense retrieval. arXiv. https://arxiv.org/abs/2403.18684

Huang, C.-W., & Chen, Y.-N. (2024). PairDistill: Pairwise relevance distillation for dense retrieval. arXiv. https://arxiv.org/abs/2410.01383

Huang, S., Zhang, C., Wu, Y., Zhang, H., Wang, Y., Wang, M., Cao, S., Xu, T., Zhao, X., Qin, Z., Gao, Y., Bai, Y., Fan, J., Hu, Y., & Chen, E. (2024). ScalingNote: Scaling up retrievers with large language models for real-world dense retrieval. arXiv. https://arxiv.org/abs/2411.15766

Li, M., & Gaussier, E. (2024). Domain adaptation for dense retrieval and conversational dense retrieval through self-supervision by meticulous pseudo-relevance labeling. arXiv. https://arxiv.org/abs/2403.08970

Pandey, M. (2026). Domain-adaptive and scalable dense retrieval for content-based recommendation. arXiv. https://arxiv.org/abs/2602.00899

Su, Z., Mo, F., Zhang, J., Hui, Y., Sun, J. A., Wen, B., & Nie, J.-Y. (2026). Towards dynamic dense retrieval with routing strategy. arXiv. https://arxiv.org/abs/2602.22547

Wu, S., Wei, W., Zhang, M., Chen, Z., Ma, J., Ren, Z., de Rijke, M., & Ren, P. (2024). Generative retrieval as multi-vector dense retrieval. arXiv. https://arxiv.org/abs/2404.00684

Zhuang, S., Koopman, B., Chu, X., & Zuccon, G. (2024). Understanding and mitigating the threat of Vec2Text to dense retrieval systems. arXiv. https://arxiv.org/abs/2402.12784
