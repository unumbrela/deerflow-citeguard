# Systematic Literature Review: Graph Neural Networks

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "graph neural networks", category cs.LG, published between 2024-10-25 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on graph neural networks (GNNs) published within the last two years in the cs.LG category. The surveyed literature reveals a field rapidly expanding along multiple dimensions: theoretical foundations connecting GNNs to other architectures (transformers, Finsler geometry), robustness and uncertainty quantification methods, efficiency optimizations through pruning and early-exiting, and novel applications spanning power grid control to epidemic forecasting. A notable trend is the increasing sophistication in handling graph structure itself—whether through heterogeneous representations, topology-aware repair mechanisms, or spectral-based edge pruning. The field demonstrates strong convergence on the importance of interpretability, robustness under distributional shift, and computational efficiency, while beginning to explore emerging frontiers such as quantum graph neural networks.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "graph neural networks", filtered to category cs.LG, published between 2024-10-25 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Foundations and Architectural Connections

Recent work has deepened the theoretical understanding of GNNs by establishing connections to other prominent architectures and mathematical frameworks. Joshi (2025) demonstrates that Transformers can be viewed as message passing GNNs operating on fully connected graphs of tokens, revealing that self-attention mechanisms capture relative token importance through dense matrix operations more efficient than sparse message passing on modern hardware. This positions Transformers as GNNs that are "winning the hardware lottery."

Complementing this, Roddenberry and Baraniuk (2026) extend GNN theory through Finsler geometry, showing that discrete estimates of the Finsler Laplacian on point clouds converge to the true operator and can be expressed as GNN layers. This provides a nonlinear alternative to traditional Laplacian-based GNNs, which are limited to isotropic operators. Together, these papers illustrate how GNNs are being situated within broader mathematical and architectural frameworks, enriching theoretical foundations while explaining empirical successes of seemingly distinct architectures.

### Theme 2: Robustness and Uncertainty Quantification

A significant research direction addresses GNN robustness to noisy or incomplete graph structure and uncertainty under distributional shift. Goel and Kanniainen (2026) propose Topology-Aware Gaussian Repair (TAGR), which constructs sparse feature-neighborhood graphs using adaptive Gaussian kernels combined with topology-aware residual correction. Their experiments show that lightweight sparse graph repair achieves effective robustness under both noisy-edge and missing-edge settings without requiring dense graph structure learning.

Tolloso and Bacciu (2025) introduce credal graph neural networks (CGNNs) that output set-valued predictions as credal sets, delivering more reliable epistemic uncertainty representations. Their approach achieves state-of-the-art performance under distributional shift on heterophilic graphs, highlighting how graph homophily assumptions critically shape uncertainty estimate effectiveness. These works converge on the insight that robustness requires explicit modeling of structural uncertainty rather than assuming observed graphs are complete or accurate.

### Theme 3: Efficiency Through Structural Optimization

Several papers address computational efficiency by optimizing graph structure during inference. Bessone (2025) presents a spectral theory-based dynamic pruning method for Asynchronous Recurrent Graph Neural Networks (ARGNNs), leveraging the imaginary component of eigenvalues from the network graph's Laplacian to identify and remove unnecessary edges. This approach enhances efficiency without compromising performance.

Knyazhitskiy and Di Francesco (2026) explore early-exiting strategies for GNNs in link prediction tasks, allowing early exiting to emerge as an implicit architectural property without auxiliary losses. Their method moves the Pareto frontier on the HeaRT benchmark, improving inference speed while maintaining or even gaining prediction quality. Both approaches demonstrate that structural optimization—whether through edge pruning or adaptive computation depth—can yield substantial efficiency gains.

### Theme 4: Heterogeneous and Domain-Specific Representations

The literature emphasizes that graph representation choices fundamentally impact GNN effectiveness, particularly in domain-specific applications. De Jong et al. (2025) identify a busbar information asymmetry problem in homogeneous graph representations for transmission grid topology control and propose heterogeneous graph representations to resolve it. Their heterogeneous GNNs perform best on in-distribution network configurations and generalize better to out-of-distribution configurations than fully connected neural networks.

Han et al. (2025) develop a Causal Spatiotemporal Graph Neural Network (CSTGNN) for epidemic forecasting that integrates physics-based Spatio-Contact SIR models with data-driven GNNs. Their approach uses adaptive static connectivity graphs for stable human mobility components and temporal dynamics models for fluctuations, enhancing both interpretability and practical applicability. These papers demonstrate that domain knowledge must inform graph construction—whether through heterogeneous node types or physics-informed connectivity—to achieve optimal performance and interpretability.

### Theme 5: Interpretability and Explainability

As GNNs are deployed in high-stakes domains, interpretability has become increasingly critical. Jena et al. (2025) introduce QuantumGraphLIME (QGraphLIME), a model-agnostic post-hoc framework for explaining quantum graph neural networks. The method treats explanations as distributions over local surrogates fit on structure-preserving perturbations, aggregating surrogate attributions with their dispersion. It provides Dvoretzky-Kiefer-Wolfowitz bounds for finite-sample guarantees on surrogate ensemble size, yielding uncertainty-aware node and edge importance rankings.

Tanis et al. (2024) provide an introductory framework for understanding GNN behavior through the encoder-decoder paradigm, emphasizing the importance of understanding oversmoothing and oversquashing phenomena. Their experimental analysis illustrates how GNNs behave under different training sizes and graph complexity levels, offering practical guidance for machine learning engineers. Both works highlight that interpretability mechanisms must account for the unique structural properties of graphs while providing actionable insights for practitioners.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the importance of explicitly modeling graph structure rather than treating it as fixed or given. Goel and Kanniainen (2026), De Jong et al. (2025), and Han et al. (2025) all demonstrate that structural choices—whether through repair mechanisms, heterogeneous representations, or physics-informed connectivity—fundamentally determine GNN effectiveness. Additionally, there is strong agreement on the need for uncertainty quantification and robustness under distributional shift, with Tolloso and Bacciu (2025) and Goel and Kanniainen (2026) both addressing reliability under out-of-distribution conditions.

**Disagreements**: The literature shows tension between architectural generality and domain specificity. Joshi (2025) argues for the universality of GNN-like mechanisms (positioning Transformers as GNNs), while Roddenberry and Baraniuk (2026) advocate for specialized geometric frameworks (Finsler geometry) beyond standard Laplacian-based approaches. Similarly, efficiency-focused papers differ on whether optimization should target structure (Bessone, 2025, pruning edges) or computation depth (Knyazhitskiy & Di Francesco, 2026, early-exiting), suggesting context-dependent optimal strategies rather than universal solutions.

## Gaps and Open Questions

The collective literature reveals several notable gaps. First, none of the surveyed papers explicitly address scalability to very large graphs (millions of nodes), focusing instead on benchmark datasets or domain-specific moderate-scale applications. Second, while robustness and uncertainty are well-studied, the interaction between these properties—how uncertainty estimates degrade under structural perturbations—remains unexplored. Third, the emerging area of quantum graph neural networks (Jena et al., 2025) lacks theoretical foundations connecting quantum and classical GNN frameworks. Finally, several papers note limitations "not stated in abstract," suggesting that detailed limitations and failure modes may be underreported in the literature, limiting practitioners' ability to assess when GNNs may fail.

## Per-Paper Annotations

### Bessone (2025)

**Research question**: How can unnecessary edges be pruned in Asynchronous Recurrent Graph Neural Networks to enhance efficiency without compromising performance?

**Methodology**: Presents a dynamic pruning method based on graph spectral theory, leveraging the imaginary component of the eigenvalues of the network graph's Laplacian for edge pruning in ARGNNs.

**Key findings**:
- Proposes a spectral theory-based approach for edge pruning in ARGNNs
- Leverages eigenvalues of the network graph's Laplacian to identify unnecessary edges

**Limitations**: Not stated in abstract.

### De Jong, Viebahn, and Shapovalova (2025)

**Research question**: How does graph representation affect GNN effectiveness for transmission grid topology control?

**Methodology**: Investigates the effect of graph representation on GNN effectiveness by identifying the busbar information asymmetry problem in homogeneous graph representations and proposing a heterogeneous graph representation. Models are evaluated using classification accuracy and grid operation ability on an imitation learning task.

**Key findings**:
- Busbar information asymmetry is a problem inherent to homogeneous graph representations
- Heterogeneous graph representation resolves the busbar information asymmetry problem
- Heterogeneous GNNs perform best on in-distribution network configurations
- FCNNs perform better than homogeneous GNNs on in-distribution configurations
- Both GNN types generalize better to out-of-distribution network configurations than FCNNs

**Limitations**: Not stated in abstract.

### Goel and Kanniainen (2026)

**Research question**: How can graph neural networks be made more robust to noisy and missing edges in real-world graph topology?

**Methodology**: Propose Topology-Aware Gaussian Repair (TAGR), which constructs a sparse feature-neighborhood graph using an adaptive Gaussian kernel and combines it with topology-aware residual correction of the observed graph. Evaluated through extensive experiments on benchmark citation networks under noisy-edge and missing-edge settings.

**Key findings**:
- TAGR improves the robustness of GNNs under both noisy-edge and missing-edge settings on benchmark citation networks
- Gaussian feature-neighborhood repair provides the main robustness gain
- Topology-aware residual correction improves stability when the observed graph is incomplete
- Effective graph robustness can be achieved through lightweight sparse graph repair rather than dense graph structure learning

**Limitations**: Not stated in abstract.

### Han, Stelz, Sokolowski, Zhou, and Stöcker (2025)

**Research question**: How can physics-based and data-driven modeling be unified for interpretable epidemic forecasting?

**Methodology**: Proposes a Causal Spatiotemporal Graph Neural Network (CSTGNN) that integrates a Spatio-Contact SIR model with GNNs. Uses an adaptive static connectivity graph for stable human mobility components, a temporal dynamics model for fluctuations, and a temporal decomposition model for temporal dependence, validated on provincial-level data from China and state-level data from Germany.

**Key findings**:
- CSTGNN effectively models spatiotemporal dynamics of infectious diseases
- The method provides a valuable tool for epidemic forecasting and intervention strategies
- Analysis of learned parameters offers insights into disease transmission mechanisms
- The approach enhances interpretability and practical applicability of epidemic models
- The hybrid framework addresses limitations of both traditional compartmental models and deep learning models

**Limitations**: Not stated in abstract.

### Jena, Shivottam, and Mishra (2025)

**Research question**: How can quantum graph neural networks be explained despite measurement-induced stochasticity and the combinatorial nature of graph structure?

**Methodology**: Introduce QuantumGraphLIME (QGraphLIME), a model-agnostic post-hoc framework that treats model explanations as distributions over local surrogates fit on structure-preserving perturbations of a graph, aggregating surrogate attributions with their dispersion. Provides a Dvoretzky-Kiefer-Wolfowitz bound for finite-sample guarantees on surrogate ensemble size.

**Key findings**:
- QGraphLIME yields uncertainty-aware node and edge importance rankings for quantum graph models
- Empirical studies on synthetic graphs with known ground truth demonstrate accurate and stable explanations
- Ablations show clear benefits of nonlinear surrogate modeling and highlight sensitivity to perturbation design
- The framework provides distribution-free, finite-sample guarantees on surrogate ensemble size

**Limitations**: Not stated in abstract.

### Joshi (2025)

**Research question**: What is the relationship between Transformer architectures and Graph Neural Networks?

**Methodology**: Analyzes the Transformer architecture and shows how it can be viewed as message passing GNNs operating on fully connected graphs of tokens.

**Key findings**:
- Transformers can be viewed as message passing GNNs operating on fully connected graphs of tokens
- Self-attention mechanisms capture the relative importance of all tokens with respect to each other
- Positional encodings provide hints about sequential ordering or structure
- Transformers are implemented via dense matrix operations that are more efficient on modern hardware than sparse message passing
- Transformers are GNNs that are currently winning the hardware lottery

**Limitations**: Not stated in abstract.

### Knyazhitskiy and Di Francesco (2026)

**Research question**: How can early-exiting strategies improve the speed/quality tradeoff in Graph Neural Networks for link prediction?

**Methodology**: Explore early-exiting strategies applied to Graph Neural Networks without using auxiliary losses to enforce early exiting, allowing it to emerge as an implicit property of the architecture. Evaluated on the HeaRT benchmark for GCN and SAS-GNN backbones.

**Key findings**:
- The method enables early exiting in several setups, moving the Pareto frontier on the HeaRT benchmark
- Inference speed of GNNs on many link-prediction problems can be improved while losing little or even gaining in prediction quality
- Early exiting can emerge as an implicit property of the architecture without auxiliary losses

**Limitations**: Not stated in abstract.

### Roddenberry and Baraniuk (2026)

**Research question**: Can Finsler geometry be expressed through graph neural network architectures as a nonlinear alternative to Laplacian-based GNNs?

**Methodology**: Consider estimates of the Finsler Laplacian on point clouds sampled from a manifold and prove convergence to the true operator. Show this operator can be expressed as a GNN layer and use it to define Finslerian graph neural networks constrained to express Finsler geometry.

**Key findings**:
- GNN architectures based on graph Laplacian approximate the Laplace-Beltrami operator, limiting them to isotropic operators
- Discrete estimates of the Finsler Laplacian converge to the true operator as point samples grow
- The Finsler Laplacian operator can be expressed as a graph neural network layer
- Finslerian graph neural networks recover the geometry underlying nonlinear diffusion equations in practice

**Limitations**: Not stated in abstract.

### Tanis, Giannella, Mariano, and Meerzaman (2024)

**Research question**: How can graph neural networks be introduced and explained to machine learning engineers through practical examples and analysis?

**Methodology**: This survey introduces GNNs through the encoder-decoder framework, provides decoder examples for various graph analytic tasks, and uses theory and experiments on homogeneous graphs to illustrate GNN behavior under different training sizes and graph complexity levels.

**Key findings**:
- GNNs are deep neural networks designed for graphs with attributes on nodes or edges
- Research on GNNs is growing rapidly due to impressive performance on diverse tasks
- The encoder-decoder framework provides a useful introduction to GNNs
- The paper illustrates GNN behavior under different training sizes and graph complexity
- The survey emphasizes understanding oversmoothing and oversquashing phenomena

**Limitations**: Not stated in abstract.

### Tolloso and Bacciu (2025)

**Research question**: How can uncertainty quantification be improved in Graph Neural Networks for reliable deployment under out-of-distribution conditions?

**Methodology**: Introduce credal graph neural networks (CGNNs) that extend credal learning to the graph domain by training GNNs to output set-valued predictions in the form of credal sets, leveraging layer-wise information propagation. Assessed on uncertainty quantification in node classification under out-of-distribution conditions.

**Key findings**:
- CGNNs deliver more reliable representations of epistemic uncertainty
- CGNNs achieve state-of-the-art performance under distributional shift on heterophilic graphs
- Graph homophily assumption plays a critical role in shaping the effectiveness of uncertainty estimates

**Limitations**: Not stated in abstract.

## References

Bessone, N. (2025). Spectral theory for edge pruning in asynchronous recurrent graph neural networks. arXiv. https://arxiv.org/abs/2502.17522

De Jong, M., Viebahn, J., & Shapovalova, Y. (2025). Graph neural networks for transmission grid topology control: Busbar information asymmetry and heterogeneous representations. arXiv. https://arxiv.org/abs/2501.07186

Goel, A., & Kanniainen, J. (2026). Topology-aware Gaussian graph repair for robust graph neural networks. arXiv. https://arxiv.org/abs/2606.03462

Han, S., Stelz, L., Sokolowski, T. R., Zhou, K., & Stöcker, H. (2025). Unifying physics- and data-driven modeling via novel causal spatiotemporal graph neural network for interpretable epidemic forecasting. arXiv. https://arxiv.org/abs/2504.05140

Jena, H., Shivottam, J., & Mishra, S. (2025). QGraphLIME - Explaining quantum graph neural networks. arXiv. https://arxiv.org/abs/2510.05683

Joshi, C. K. (2025). Transformers are graph neural networks. arXiv. https://arxiv.org/abs/2506.22084

Knyazhitskiy, R., & Di Francesco, A. G. (2026). Early-exit graph neural networks for link prediction. arXiv. https://arxiv.org/abs/2606.22167

Roddenberry, T. M., & Baraniuk, R. G. (2026). Finsler geometry, graph neural networks, and you. arXiv. https://arxiv.org/abs/2606.17185

Tanis, J. H., Giannella, C., Mariano, A. V., & Meerzaman, D. (2024). Introduction to graph neural networks for machine learning engineers. arXiv. https://arxiv.org/abs/2412.19419

Tolloso, M., & Bacciu, D. (2025). Credal graph neural networks. arXiv. https://arxiv.org/abs/2512.02722
