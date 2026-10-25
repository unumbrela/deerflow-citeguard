# Systematic Literature Review: Graph Neural Networks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "graph neural networks", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The surveyed literature on graph neural networks (GNNs) reveals a rapidly evolving field with diverse theoretical and applied advances. Recent work spans foundational theoretical connections between GNNs and other architectures (particularly Transformers), novel mathematical frameworks incorporating differential geometry and spectral theory, and practical applications across domains including power systems, epidemiology, and quantum computing. The field demonstrates strong convergence on the versatility of GNN architectures while exploring innovations in robustness, uncertainty quantification, interpretability, and computational efficiency. Several papers address fundamental limitations of existing GNN approaches, proposing solutions for handling noisy graph structures, distributional shifts, and the computational costs of message passing.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "graph neural networks", filtered to primary category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Foundations and Architectural Connections

Recent work has deepened the theoretical understanding of GNNs by establishing connections to other prominent architectures and mathematical frameworks. Joshi (2025) demonstrated that Transformers can be viewed as message passing GNNs operating on fully connected graphs, where self-attention captures token relationships and positional encodings provide structural information. This theoretical insight reveals that Transformers are essentially GNNs that leverage dense matrix operations for hardware efficiency. Roddenberry and Baraniuk (2026) extended GNN theory by proving that discrete estimates of the Finsler Laplacian on point clouds converge to the true operator on manifolds, defining Finslerian GNNs that can express non-isotropic operators beyond the limitations of traditional Laplacian-based architectures. These theoretical advances expand the mathematical foundations of GNNs and open pathways for architectures that overcome isotropic operator limitations.

### Theme 2: Robustness and Uncertainty Quantification

A significant research direction addresses GNN robustness under distributional shifts and structural noise. Goel and Kanniainen (2026) introduced Topology-Aware Gaussian Repair (TAGR), which constructs sparse feature-neighborhood graphs using adaptive Gaussian kernels combined with topology-aware residual correction, achieving robustness against noisy and missing edges without requiring dense graph structure learning. Tolloso and Bacciu (2025) developed credal graph neural networks (CGNNs) that output set-valued predictions in the form of credal sets, delivering more reliable representations of epistemic uncertainty and achieving state-of-the-art performance under distributional shift on heterophilic graphs. These approaches recognize that real-world graphs often contain structural imperfections and that GNNs must provide reliable uncertainty estimates when operating outside their training distribution.

### Theme 3: Computational Efficiency and Optimization

Several works focus on improving the computational efficiency of GNNs without sacrificing performance. Bessone (2025) presented a spectral theory-based approach for dynamic edge pruning in Asynchronous Recurrent Graph Neural Networks, leveraging eigenvalue analysis of the graph Laplacian to identify and remove computationally unnecessary edges. Knyazhitskiy and Di Francesco (2026) explored early-exiting strategies that enable GNNs to terminate inference at intermediate layers without auxiliary losses, improving inference speed on link prediction tasks while maintaining or even gaining prediction quality. These efficiency-focused approaches address the computational burden of message passing, particularly for large-scale graphs where full propagation through all edges and layers is prohibitively expensive.

### Theme 4: Domain-Specific Applications

GNNs continue to demonstrate strong performance across diverse application domains. De Jong et al. (2025) applied GNNs to transmission grid topology control, identifying the busbar information asymmetry problem in homogeneous graph representations and proposing heterogeneous graph representations that resolve this issue for power grid applications. Han et al. (2025) developed a Causal Spatiotemporal Graph Neural Network (CSTGNN) for epidemic forecasting that integrates physics-based SIR models with GNNs to capture spatiotemporal propagation of diseases, validated on provincial-level data from China and state-level data from Germany. These applications showcase GNNs' ability to model complex relational structures inherent in power grids and disease transmission networks.

### Theme 5: Interpretability and Explainability

As GNNs are deployed in critical applications, interpretability has emerged as a crucial research direction. Jena et al. (2025) introduced QuantumGraphLIME (QGraphLIME), a model-agnostic post-hoc framework for explaining quantum graph neural networks that treats explanations as distributions over local surrogates with finite-sample guarantees, providing uncertainty-aware node and edge importance rankings. Tanis et al. (2024) provided a comprehensive introduction to GNNs through the encoder-decoder framework, emphasizing important phenomena such as oversmoothing and oversquashing that affect GNN behavior and interpretability. These works address the black-box nature of GNNs, enabling practitioners to understand and trust model predictions.

## Convergences and Disagreements

**Convergences**: Most surveyed papers agree on the fundamental versatility of GNN architectures across diverse domains and problem settings. There is strong consensus that graph structure plays a critical role in GNN performance, with multiple papers emphasizing the importance of appropriate graph representations (de Jong et al., 2025; Goel & Kanniainen, 2026). The literature also converges on the need for efficiency improvements, with several works proposing complementary approaches to reduce computational costs (Bessone, 2025; Knyazhitskiy & Di Francesco, 2026). Additionally, there is agreement that uncertainty quantification and robustness under distributional shift are essential for practical deployment (Tolloso & Bacciu, 2025).

**Disagreements**: The literature shows some tension between architectural complexity and efficiency. While Roddenberry and Baraniuk (2026) advocate for mathematically sophisticated Finslerian architectures to capture non-isotropic operators, efficiency-focused works like Bessone (2025) and Knyazhitskiy and Di Francesco (2026) prioritize pruning and early-exiting to reduce computational burden. There is also disagreement on graph representation strategies: de Jong et al. (2025) advocate for heterogeneous representations in power grid applications, while Goel and Kanniainen (2026) demonstrate effectiveness with sparse feature-neighborhood graphs combined with residual correction. The role of auxiliary losses in early-exiting strategies remains debated, with Knyazhitskiy and Di Francesco (2026) showing that early exiting can emerge implicitly without explicit auxiliary supervision.

## Gaps and Open Questions

The collective literature reveals several important gaps. First, none of the surveyed papers explicitly stated limitations in their abstracts, suggesting a potential gap in critical self-assessment of proposed methods. Second, while multiple papers address robustness and uncertainty, there is limited integration of these concerns—future work could combine TAGR's structural robustness with CGNNs' uncertainty quantification for comprehensive reliability. Third, the theoretical connections between Transformers and GNNs (Joshi, 2025) suggest opportunities for cross-pollination of techniques that remain underexplored. Fourth, domain-specific applications focus on individual domains without systematic comparison of GNN architectures across domains, limiting generalizable insights. Finally, while efficiency methods are proposed, there is no unified framework for comparing pruning, early-exiting, and architectural innovations on common benchmarks.

## Per-Paper Annotations

### Bessone (2025)

**Research question**: How can edge pruning be applied to Asynchronous Recurrent Graph Neural Networks to enhance computational efficiency without compromising performance?
**Methodology**: The paper presents a dynamic pruning method based on graph spectral theory that leverages the imaginary component of the eigenvalues of the network graph's Laplacian to identify and remove unnecessary edges in ARGNNs.
**Key findings**:
- A spectral theory-based approach can be used for dynamic edge pruning in Asynchronous Recurrent Graph Neural Networks
- The method leverages eigenvalue analysis of the graph Laplacian to identify computationally unnecessary edges
**Limitations**: Not stated in abstract

### de Jong, Viebahn, and Shapovalova (2025)

**Research question**: How does graph representation affect GNN effectiveness for transmission grid topology control?
**Methodology**: The study identifies the busbar information asymmetry problem in homogeneous graph representations and proposes a heterogeneous graph representation to resolve it, then applies GNNs with both representations and an FCNN baseline on an imitation learning task, evaluating by classification accuracy and grid operation ability.
**Key findings**:
- Heterogeneous GNNs perform best on in-distribution network configurations
- FCNNs perform second best, followed by homogeneous GNNs on in-distribution configurations
- Both GNN types generalize better to out-of-distribution network configurations than FCNNs
- Busbar information asymmetry is a problem inherent to popular homogeneous graph representations
- Heterogeneous graph representation resolves the busbar information asymmetry problem
**Limitations**: Not stated in abstract

### Goel and Kanniainen (2026)

**Research question**: How can graph neural networks achieve robustness against noisy and missing edges in graph topology without relying on dense graph structure learning?
**Methodology**: The authors propose Topology-Aware Gaussian Repair (TAGR), which constructs a sparse feature-neighborhood graph using an adaptive Gaussian kernel and combines it with topology-aware residual correction of the observed graph, evaluated through extensive experiments on benchmark citation networks under noisy-edge and missing-edge settings.
**Key findings**:
- TAGR improves the robustness of GNNs under both noisy-edge and missing-edge settings on benchmark citation networks
- Gaussian feature-neighborhood repair provides the main robustness gain
- Topology-aware residual correction improves stability when the observed graph is incomplete
- Effective graph robustness can be achieved through lightweight sparse graph repair rather than dense graph structure learning
**Limitations**: Not stated in abstract

### Han, Stelz, Sokolowski, Zhou, and Stöcker (2025)

**Research question**: How can physics-based and data-driven modeling be unified for interpretable epidemic forecasting?
**Methodology**: The paper proposes a Causal Spatiotemporal Graph Neural Network (CSTGNN) that integrates a Spatio-Contact SIR model with GNNs, employing an adaptive static connectivity graph for stable human mobility components and a temporal dynamics model for fluctuations, validated on provincial-level data from China and state-level data from Germany.
**Key findings**:
- The CSTGNN framework effectively models spatiotemporal dynamics of infectious diseases
- The method provides a valuable tool for epidemic forecasting and intervention strategies
- Analysis of learned parameters offers insights into disease transmission mechanisms
- The approach enhances interpretability and practical applicability compared to traditional methods
- The model successfully captures both spatial and temporal propagation of epidemics
**Limitations**: Not stated in abstract

### Jena, Shivottam, and Mishra (2025)

**Research question**: How can quantum graph neural networks be explained in a way that accounts for measurement-induced stochasticity and provides uncertainty-aware explanations?
**Methodology**: The authors introduce QuantumGraphLIME (QGraphLIME), a model-agnostic post-hoc framework that treats explanations as distributions over local surrogates fit on structure-preserving perturbations, with Dvoretzky-Kiefer-Wolfowitz bounds providing finite-sample guarantees, evaluated on controlled synthetic graphs with known ground truth.
**Key findings**:
- QGraphLIME yields uncertainty-aware node and edge importance rankings for quantum graph models
- The framework provides distribution-free, finite-sample guarantees on surrogate ensemble size with uniform approximation accuracy
- Empirical studies demonstrate accurate and stable explanations on synthetic graphs with known ground truth
- Nonlinear surrogate modeling and careful perturbation design provide clear benefits for explanation quality
**Limitations**: Not stated in abstract

### Joshi (2025)

**Research question**: What is the relationship between Transformer architecture and Graph Neural Networks?
**Methodology**: The paper establishes theoretical connections by analyzing how Transformers can be viewed as message passing GNNs operating on fully connected graphs, where self-attention captures token relationships and positional encodings provide structural information.
**Key findings**:
- Transformers can be viewed as message passing GNNs operating on fully connected graphs of tokens
- Self-attention mechanisms capture the relative importance of all tokens with respect to each other
- Positional encodings provide hints about sequential ordering or structure
- Transformers are implemented via dense matrix operations that are more efficient on modern hardware than sparse message passing
- Transformers are GNNs that are currently winning the hardware lottery
**Limitations**: Not stated in abstract

### Knyazhitskiy and Di Francesco (2026)

**Research question**: Can early-exiting strategies improve the inference speed of Graph Neural Networks for link prediction while maintaining prediction quality?
**Methodology**: The authors explore early-exiting strategies applied to GNNs without using auxiliary losses, allowing early exiting to emerge as an implicit property of the architecture, evaluated on the HeaRT benchmark for GCN and SAS-GNN backbones.
**Key findings**:
- The method enables early exiting in several setups, moving the Pareto frontier on the HeaRT benchmark
- Inference speed of GNNs on link-prediction problems can be improved while losing little or even gaining in prediction quality
- Early exiting can emerge as an implicit property without enforcing it through auxiliary losses
**Limitations**: Not stated in abstract

### Roddenberry and Baraniuk (2026)

**Research question**: Can Finsler Laplacian estimates on point clouds be expressed as graph neural network layers for modeling non-isotropic operators?
**Methodology**: The paper proves that discrete estimates of the Finsler Laplacian on point clouds sampled from a manifold converge to the true operator as samples grow, shows this operator can be expressed as a GNN layer, and defines a family of Finslerian GNNs constrained to express Finsler geometry.
**Key findings**:
- GNN architectures based on graph Laplacian approximate the Laplace-Beltrami operator, limiting them to isotropic operators
- Discrete estimates of the Finsler Laplacian converge to the true operator on the manifold as point samples grow
- The Finsler Laplacian operator can be expressed as a graph neural network layer
- Finslerian GNNs recover the geometry underlying nonlinear diffusion equations in practice
**Limitations**: Not stated in abstract

### Tanis, Giannella, Mariano, and Meerzaman (2024)

**Research question**: How can graph neural networks be introduced and explained to machine learning engineers through practical frameworks and examples?
**Methodology**: This survey introduces GNNs through the encoder-decoder framework, provides decoder examples for various graph analytic tasks, and uses theory and experiments on homogeneous graphs to illustrate GNN behavior under different training sizes and graph complexity degrees.
**Key findings**:
- GNNs are deep neural networks designed for graphs with attributes attached to nodes or edges
- The encoder-decoder framework provides an effective introduction to GNNs
- The paper illustrates GNN behavior under different training sizes and degrees of graph complexity
- Oversmoothing and oversquashing are emphasized as important phenomena in GNN behavior
- The number of research papers on GNNs is growing rapidly due to impressive performance on diverse tasks
**Limitations**: Not stated in abstract

### Tolloso and Bacciu (2025)

**Research question**: How can credal learning be extended to graph neural networks to provide reliable uncertainty quantification under out-of-distribution conditions?
**Methodology**: The authors introduce credal graph neural networks (CGNNs) that train GNNs to output set-valued predictions in the form of credal sets, leveraging layer-wise information propagation specific to message passing in GNNs, assessed on uncertainty quantification in node classification under out-of-distribution conditions.
**Key findings**:
- CGNNs deliver more reliable representations of epistemic uncertainty
- CGNNs achieve state-of-the-art performance under distributional shift on heterophilic graphs
- Graph homophily assumption plays a critical role in shaping the effectiveness of uncertainty estimates
**Limitations**: Not stated in abstract

## References

Bessone, N. (2025). Spectral theory for edge pruning in asynchronous recurrent graph neural networks. arXiv. https://arxiv.org/abs/2502.17522

de Jong, M., Viebahn, J., & Shapovalova, Y. (2025). Graph neural networks for transmission grid topology control: Busbar information asymmetry and heterogeneous representations. arXiv. https://arxiv.org/abs/2501.07186

Goel, A., & Kanniainen, J. (2026). Topology-aware Gaussian graph repair for robust graph neural networks. arXiv. https://arxiv.org/abs/2606.03462

Han, S., Stelz, L., Sokolowski, T. R., Zhou, K., & Stöcker, H. (2025). Unifying physics- and data-driven modeling via novel causal spatiotemporal graph neural network for interpretable epidemic forecasting. arXiv. https://arxiv.org/abs/2504.05140

Jena, H., Shivottam, J., & Mishra, S. (2025). QGraphLIME - Explaining quantum graph neural networks. arXiv. https://arxiv.org/abs/2510.05683

Joshi, C. K. (2025). Transformers are graph neural networks. arXiv. https://arxiv.org/abs/2506.22084

Knyazhitskiy, R., & Di Francesco, A. G. (2026). Early-exit graph neural networks for link prediction. arXiv. https://arxiv.org/abs/2606.22167

Roddenberry, T. M., & Baraniuk, R. G. (2026). Finsler geometry, graph neural networks, and you. arXiv. https://arxiv.org/abs/2606.17185

Tanis, J. H., Giannella, C., Mariano, A. V., & Meerzaman, D. (2024). Introduction to graph neural networks for machine learning engineers. arXiv. https://arxiv.org/abs/2412.19419

Tolloso, M., & Bacciu, D. (2025). Credal graph neural networks. arXiv. https://arxiv.org/abs/2512.02722
