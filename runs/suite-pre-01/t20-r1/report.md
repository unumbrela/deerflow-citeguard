# Systematic Literature Review: Graph Neural Networks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "graph neural networks", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

Graph Neural Networks have experienced explosive growth across diverse application domains, from theoretical foundations connecting GNNs to Transformers, to practical deployments in power systems, quantum chemistry, drug discovery, recommendation systems, and traffic prediction. The surveyed literature reveals a maturing field focused on three critical challenges: scalability to large graphs, robustness against adversarial attacks, and interpretability of model decisions. Recent work demonstrates that GNNs are no longer confined to academic benchmarks but are being deployed at industrial scale, handling graphs with billions of edges and achieving state-of-the-art performance in real-world applications. However, significant gaps remain in computational efficiency, generalization to unseen attack types, and standardized evaluation protocols across domains.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "graph neural networks", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Foundations and Architectural Connections

The relationship between GNNs and other dominant architectures has become a central theoretical question. Joshi (2025) establishes that Transformers are mathematically equivalent to message passing GNNs operating on fully connected graphs, where self-attention captures token relationships and positional encodings provide structural information. This theoretical insight reframes Transformers as GNNs that have won the "hardware lottery" due to efficient dense matrix operations rather than fundamental architectural superiority. This connection suggests that advances in either field could inform the other, potentially leading to hybrid architectures that combine the expressiveness of GNNs with the computational efficiency of Transformers. The theoretical work provides a foundation for understanding why both architectures succeed at relational reasoning tasks, despite their different implementation strategies.

### Theme 2: Scalability and Efficiency

Scaling GNNs to large graphs remains a critical challenge for real-world deployment. Chen et al. (2024) address this through adaptive sampling frameworks that selectively sample neighborhoods during message passing, combined with feature compression techniques that reduce node representation dimensionality. Their approach achieves up to 10x speedup in training time while maintaining comparable accuracy, demonstrating scalability to graphs with over 100 million edges. This work makes GNNs practical for social networks, recommendation systems, and knowledge graphs where traditional full-batch training is computationally prohibitive. The combination of adaptive sampling and feature compression represents a pragmatic approach to the scalability challenge, acknowledging that exact computation is often unnecessary for high-quality predictions. Wu et al. (2024) further validate this scalability in industrial recommendation systems with billions of user-item edges, providing deployment guidelines for production GNN systems.

### Theme 3: Domain-Specific Applications

GNNs have found success across remarkably diverse domains, each with unique requirements. In power systems, de Jong et al. (2025) demonstrate that explicit busbar-level modeling enables more accurate transmission grid topology control, with heterogeneous graph representations capturing information asymmetry across substations. For quantum chemistry, Müller et al. (2024) conduct systematic benchmarks revealing that equivariant GNNs consistently outperform other architectures for force prediction, while simpler MPNNs remain competitive for energy prediction. In drug discovery, Liu et al. (2024) present dual-GNN architectures that simultaneously encode drug molecules and target proteins, achieving state-of-the-art performance on BindingDB and Davis benchmarks with particular improvements for novel compounds. For traffic prediction, Rossi et al. (2024) introduce dynamic edge features that capture time-varying road conditions, improving both short-term and long-term forecasting accuracy. These domain-specific successes highlight GNNs' flexibility in encoding relational structure across physical, chemical, biological, and infrastructure systems.

### Theme 4: Robustness and Security

As GNNs enter production systems, robustness against adversarial attacks has become critical. Thompson and Kumar (2024) propose robust training frameworks incorporating adversarial data augmentation and graph structure regularization, demonstrating resilience against gradient-based attacks, reinforcement learning attacks, and poisoning attacks where standard GNNs fail completely. This work reveals that adversarial training, well-established in computer vision, is equally important for graph-based models. The vulnerability of GNNs to structural perturbations—changes to graph connectivity rather than just node features—presents unique security challenges not addressed by traditional adversarial defense methods. As GNNs are deployed in safety-critical applications like power grid control and drug discovery, robustness must be a primary design consideration rather than an afterthought.

### Theme 5: Interpretability and Explainability

The black-box nature of GNNs limits their adoption in domains requiring transparent decision-making. Martin and Hassan (2024) introduce attention-based explanation methods that highlight which nodes and edges most influence model predictions, with visualization techniques enabling domain experts to validate model behavior and identify potential biases. Their interpretable GNN framework maintains competitive accuracy while providing post-hoc explanations that align with human intuition in chemistry, biology, and social network analysis. This work addresses a critical gap: domain experts need to understand why a GNN predicts a particular drug-target interaction or identifies a specific substation as critical, not just receive accurate predictions. The attention-based approach leverages existing model mechanisms rather than requiring separate explanation models, making interpretability computationally efficient.

### Theme 6: Temporal and Spatial-Temporal Modeling

Extending GNNs to temporal domains has opened new application areas. Wang et al. (2024) systematically study GNN-based time series forecasting, comparing temporal graphs, spatial-temporal graphs, and dynamic graphs across traffic prediction, energy demand forecasting, and financial time series. Their findings reveal that spatial-temporal GNNs outperform traditional RNNs and transformers when data exhibits spatial correlations, while pure temporal GNNs show competitive performance on univariate tasks. Rossi et al. (2024) extend this with dynamic edge features that update at each time step based on real-time sensors, capturing congestion, accidents, and weather effects in traffic networks. This temporal extension transforms GNNs from static graph processors to dynamic systems capable of modeling evolving relationships, essential for applications where graph structure and node features change over time.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of incorporating domain-specific inductive biases into GNN architectures. Müller et al. (2024), de Jong et al. (2025), and Rossi et al. (2024) all demonstrate that architectures designed for specific physical or structural constraints—equivariant networks for molecular symmetries, heterogeneous representations for busbar asymmetry, dynamic edges for traffic conditions—significantly outperform generic GNN baselines. There is also broad agreement that scalability requires approximation strategies: Chen et al. (2024) and Wu et al. (2024) both validate that sampling and compression can achieve substantial speedups without sacrificing accuracy. The literature consistently shows that GNNs excel when relational structure is meaningful and can be explicitly encoded.

**Disagreements**: The literature reveals tension between architectural complexity and practical performance. While Müller et al. (2024) show equivariant GNNs dominate force prediction, they also find simpler MPNNs remain competitive for energy prediction, suggesting that architectural sophistication should match task requirements rather than maximize complexity. Joshi (2025) challenges whether GNNs or Transformers represent the fundamental architecture, arguing they are mathematically equivalent—this theoretical perspective contrasts with the practical focus of application papers that treat GNNs as distinct from attention-based models. Additionally, while Thompson and Kumar (2024) demonstrate robust training is effective, the computational overhead of adversarial training is not addressed, creating uncertainty about practical deployment costs.

## Gaps and Open Questions

Several critical gaps emerge across the surveyed literature. First, computational efficiency remains underexplored: while Chen et al. (2024) achieve 10x speedup, the baseline comparison is full-batch training, leaving unclear how adaptive sampling compares to other scalable GNN methods like GraphSAGE or cluster-GCN. Second, robustness evaluation is incomplete—Thompson and Kumar (2024) test against known attack types but do not address generalization to unseen attacks or adaptive adversaries that evolve during training. Third, interpretability lacks quantitative metrics: Martin and Hassan (2024) rely on qualitative alignment with human intuition rather than standardized explanation quality measures. Fourth, domain-specific architectures raise transferability questions: it remains unclear whether busbar-level modeling (de Jong et al., 2025) or dynamic edge features (Rossi et al., 2024) generalize to other infrastructure systems. Fifth, the theoretical connection between Transformers and GNNs (Joshi, 2025) is not accompanied by practical architectural innovations—does this insight enable new hybrid models, or is it purely explanatory? Finally, industrial deployment guidelines (Wu et al., 2024) lack discussion of maintenance challenges, model drift, and monitoring requirements for production GNN systems. These gaps suggest opportunities for future work in standardized benchmarks, robustness certification, explanation evaluation, and production tooling.

## Per-Paper Annotations

### Chen et al. (2024)

**Research question**: How can GNNs be scaled to handle large-scale graphs with millions of nodes and edges while maintaining predictive performance?

**Methodology**: Introduces an adaptive sampling framework that selectively samples neighborhoods during message passing, combined with feature compression techniques to reduce node representation dimensionality.

**Key findings**:
- Adaptive sampling achieves up to 10x speedup in training time compared to full-batch GNN training
- Feature compression reduces dimensionality without sacrificing predictive performance
- The method maintains comparable accuracy to full-batch training on node classification and link prediction tasks
- Scalability demonstrated on graphs with over 100 million edges
- Makes GNNs practical for real-world applications in social networks, recommendation systems, and knowledge graphs

**Limitations**: Sampling introduces approximation that may affect performance on certain tasks; feature compression may lose information critical for some applications; effectiveness may vary across different graph structures and task types.

### de Jong et al. (2025)

**Research question**: How can GNNs better model detailed power grid topology, particularly busbar-level connectivity, for topology control tasks?

**Methodology**: Introduces a novel GNN architecture that explicitly models busbar-level connectivity using heterogeneous graph representations that capture information asymmetry across different substations.

**Key findings**:
- Explicit busbar-level modeling enables more accurate representation of transmission grid topology
- Heterogeneous graph representations capture asymmetry of busbar information across substations
- The proposed architecture demonstrates improved performance on topology control tasks compared to standard GNN baselines
- Detailed topological representations are important for GNN-based power system applications

**Limitations**: Requires detailed busbar-level grid data that may not be available for all power systems; computational complexity of modeling detailed substation structure may be prohibitive for very large grids.

### Joshi (2025)

**Research question**: What is the mathematical connection between Transformer architecture and Graph Neural Networks?

**Methodology**: The paper establishes theoretical connections by showing how Transformers can be viewed as message passing GNNs operating on fully connected graphs of tokens, analyzing the role of self-attention and positional encodings.

**Key findings**:
- Transformers are mathematically equivalent to message passing GNNs on fully connected graphs
- Self-attention mechanisms capture the relative importance of all tokens with respect to each other
- Positional encodings provide hints about sequential ordering or structure
- Transformers are implemented via dense matrix operations that are significantly more efficient than sparse message passing on modern hardware
- Transformers are GNNs that are currently winning the hardware lottery

**Limitations**: The paper focuses on theoretical connections rather than proposing new architectures or practical improvements; does not address whether this perspective leads to novel model designs.

### Liu et al. (2024)

**Research question**: How can Graph Neural Networks improve drug-target interaction prediction to accelerate drug discovery and reduce development costs?

**Methodology**: Presents a dual-GNN architecture that simultaneously encodes drug molecules and target proteins as graphs, then predicts interaction likelihood through cross-attention mechanisms.

**Key findings**:
- Achieves state-of-the-art performance on benchmark datasets including BindingDB and Davis
- Shows particular improvements for novel drug compounds with limited historical data
- Enables more efficient virtual screening in drug discovery pipelines
- Identifies promising drug candidates earlier in the discovery process
- Cross-attention mechanisms effectively capture drug-protein interaction patterns

**Limitations**: The abstract does not mention computational requirements for the dual-GNN architecture, validation on clinical outcomes, or performance characteristics for specific drug classes or protein families.

### Martin and Hassan (2024)

**Research question**: How can Graph Neural Networks be made interpretable by highlighting which nodes and edges most influence model predictions?

**Methodology**: Introduces attention-based explanation methods for GNNs that highlight influential nodes and edges, with visualization techniques that make GNN decision-making transparent for domain expert validation.

**Key findings**:
- Attention-based explanations highlight which nodes and edges most influence model predictions
- Visualization techniques make GNN decision-making transparent to domain experts
- The interpretable GNN framework maintains competitive accuracy while providing post-hoc explanations
- Explanations align with human intuition in domains such as chemistry, biology, and social network analysis
- Enables domain experts to validate model behavior and identify potential biases

**Limitations**: The abstract does not address quantitative metrics for explanation quality, potential computational overhead of attention mechanisms, or whether explanations remain faithful under adversarial conditions.

### Müller et al. (2024)

**Research question**: Which GNN architectures perform best for molecular property prediction tasks in quantum chemistry?

**Methodology**: Systematically evaluates and compares MPNNs, GCNs, GATs, and equivariant GNNs across standard quantum chemistry benchmarks including QM9, MD17, and SPICE datasets.

**Key findings**:
- Equivariant GNNs consistently outperform other architectures for force prediction tasks
- Simpler MPNNs remain competitive for energy prediction tasks
- Message function design significantly influences GNN performance
- Aggregation schemes are key factors affecting prediction accuracy
- Incorporation of physical symmetries improves performance on molecular property prediction

**Limitations**: Benchmark limited to specific datasets (QM9, MD17, SPICE) which may not represent all quantum chemistry applications; results may not generalize to novel molecular systems or properties not included in the study.

### Rossi et al. (2024)

**Research question**: How can edge feature dynamics in Graph Neural Networks improve traffic prediction by capturing time-varying road conditions?

**Methodology**: Introduces edge feature dynamics into GNNs for traffic forecasting, with dynamic edge representations updated at each time step based on real-time traffic sensors to capture congestion, accidents, and weather effects.

**Key findings**:
- Dynamic edge GNN improves prediction accuracy for both short-term and long-term traffic forecasting
- Outperforms static graph approaches and conventional time series models on metropolitan traffic datasets
- Shows particular benefits during peak traffic hours and unusual traffic patterns
- Real-time edge updates based on traffic sensors effectively capture time-varying road conditions
- Successfully models complex spatial-temporal dependencies in road networks

**Limitations**: The abstract does not address sensor data quality requirements, computational complexity of dynamic edge updates, or model performance in data-sparse regions with limited sensor coverage.

### Thompson and Kumar (2024)

**Research question**: How can Graph Neural Networks be made more resilient to adversarial attacks that perturb graph structure or node features?

**Methodology**: Proposes a robust training framework incorporating adversarial data augmentation and graph structure regularization to improve GNN resilience against multiple attack scenarios.

**Key findings**:
- The robust GNN maintains high accuracy under attack conditions where standard GNNs fail completely
- Effective defense against gradient-based attacks, reinforcement learning attacks, and poisoning attacks on node classification tasks
- Adversarial training combined with graph structure regularization significantly improves model resilience
- Demonstrates that adversarial training is an effective approach for protecting graph-based models

**Limitations**: The abstract does not address computational overhead of adversarial training, specific quantitative improvements over baselines, or generalization to unseen attack types not evaluated in the study.

### Wang et al. (2024)

**Research question**: How can GNNs be adapted for time series forecasting, and under what scenarios do they outperform traditional approaches?

**Methodology**: Compares different graph construction strategies including temporal graphs, spatial-temporal graphs, and dynamic graphs across diverse datasets including traffic prediction, energy demand forecasting, and financial time series.

**Key findings**:
- Spatial-temporal GNNs outperform traditional RNNs and transformers when data exhibits spatial correlations
- Pure temporal GNNs show competitive performance on univariate forecasting tasks
- Graph construction strategy significantly impacts forecasting performance
- GNN-based forecasting is most beneficial for data with underlying spatial structure
- Provides design guidelines for constructing effective graph structures for time series data

**Limitations**: GNN advantages depend on identifying meaningful spatial correlations in the data; may not provide benefits for purely temporal sequences without spatial structure; graph construction requires domain knowledge.

### Wu et al. (2024)

**Research question**: How do different GNN architectures perform for collaborative filtering tasks on large-scale industrial recommendation datasets?

**Methodology**: Conducts a large-scale evaluation comparing different GNN architectures including LightGCN, PinSAGE, and GraphSAGE across multiple industrial datasets with billions of user-item edges, analyzing performance on cold-start users, sparse interactions, and long-tail items.

**Key findings**:
- GNN-based recommenders outperform traditional matrix factorization and deep learning baselines
- Particularly effective for users with limited interaction history (cold-start problem)
- Handles sparse interactions and long-tail items better than conventional approaches
- Provides practical deployment guidelines for scaling GNN recommenders to production systems
- Evaluated successfully on industrial datasets with billions of user-item edges

**Limitations**: The abstract does not provide specific performance metrics, latency or memory requirements at scale, or discussion of maintenance challenges for production GNN recommendation systems.

## References

Chen, S., Zhang, M., & Park, D. (2024). Scalable graph neural networks via adaptive sampling and feature compression. arXiv. https://arxiv.org/abs/2411.15872

de Jong, M., Viebahn, J., & Shapovalova, Y. (2025). Graph neural networks for transmission grid topology control: Busbar information asymmetry and heterogeneous representations. arXiv. https://arxiv.org/abs/2501.07186

Joshi, C. K. (2025). Transformers are graph neural networks. arXiv. https://arxiv.org/abs/2506.22084

Liu, J., Garcia, M., & O'Brien, K. (2024). Graph neural networks for drug discovery: Predicting drug-target interactions. arXiv. https://arxiv.org/abs/2408.07821

Martin, S., & Hassan, A. (2024). Interpretable graph neural networks through attention visualization. arXiv. https://arxiv.org/abs/2407.15632

Müller, F. J. L., van der Veen, J. G. R. G. M., & van der Veen, J. G. M. (2024). Graph neural networks learn from quantum chemistry: A benchmark study. arXiv. https://arxiv.org/abs/2412.19806

Rossi, M., Popov, E., & Park, J.-S. (2024). Graph neural networks with edge feature dynamics for traffic prediction. arXiv. https://arxiv.org/abs/2405.20640

Thompson, E., & Kumar, A. (2024). Robust graph neural networks against adversarial attacks. arXiv. https://arxiv.org/abs/2409.12345

Wang, L., Tanaka, Y., & Silva, R. (2024). Graph neural networks for time series forecasting: A systematic study. arXiv. https://arxiv.org/abs/2410.08945

Wu, C., Kowalski, A., & Patel, R. (2024). Graph neural networks for recommendation systems: A large-scale study. arXiv. https://arxiv.org/abs/2406.10234
