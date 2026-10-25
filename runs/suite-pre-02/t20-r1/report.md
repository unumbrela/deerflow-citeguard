# Systematic Literature Review: Graph Neural Networks

**Date**: 2025-10-25
**Papers surveyed**: 10
**Scope**: arXiv search query "graph neural networks", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on graph neural networks published between 2024 and 2025. The surveyed literature reveals a field characterized by diversification across application domains and methodological innovation. Recent work spans theoretical foundations connecting GNNs to other architectures, domain-specific applications in power grids, wireless networks, robotics, and epidemiology, as well as advances in training efficiency and specialized architectures for heterophilous graphs. A notable trend is the integration of GNNs with complementary techniques including reinforcement learning, spiking neural networks, physics-based models, and large language models. While GNNs demonstrate strong performance across diverse tasks, common limitations include evaluation primarily in simulated environments and challenges scaling to large graphs or real-world deployment scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2025-10-25 using the query "graph neural networks", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Theoretical Foundations and Architectural Connections

Recent work has sought to establish deeper theoretical understanding of GNNs and their relationship to other successful architectures. Joshi (2025) demonstrates that Transformers can be mathematically viewed as message passing GNNs operating on fully connected graphs, where self-attention captures token relationships and positional encodings provide structural information. This theoretical framing positions Transformers as GNNs that have succeeded due to efficient dense matrix operations on modern hardware rather than fundamental architectural superiority. This perspective bridges two major deep learning paradigms and suggests that insights from GNN research may inform Transformer development and vice versa.

### Theme 2: Domain-Specific Applications and Adaptations

A dominant trend in recent GNN research is adaptation to specific application domains with custom architectural modifications. Several papers exemplify this pattern:

**Power Systems**: de Jong et al. (2025) address topology control in power transmission grids, identifying a "busbar information asymmetry" problem in homogeneous graph representations and proposing heterogeneous GNNs that better capture grid structure. Their work demonstrates that graph representation choices critically impact GNN effectiveness in engineering applications.

**Wireless Networks**: Zhao et al. (2025) apply GNNs to distributed link scheduling in wireless networks, developing a link sparsification scheme that reduces signaling overhead while maintaining network capacity. Their approach uses GNNs to adjust contention thresholds based on traffic statistics and topology.

**Analog Circuit Design**: Pan et al. (2025) tackle circuit link prediction with GNN-ACLP, which combines the SEAL framework for link prediction with a RAG-enhanced LLM tool for netlist format conversion. Their work addresses data scarcity through the SpiceNetlist dataset of 775 annotated circuits.

**Robotics**: Lai et al. (2025) develop RoboBallet, a GNN policy trained via reinforcement learning for multi-robot coordination, successfully coordinating 8 robots performing 40 tasks in shared workspaces with zero-shot generalization to unseen configurations.

**Epidemiology**: Han et al. (2025) propose CSTGNN, integrating physics-based SIR models with GNNs for interpretable epidemic forecasting that captures spatiotemporal disease dynamics while providing insights into transmission mechanisms.

**Thermodynamics**: Rittig and Mitsos (2024) develop GE-GNNs that ensure thermodynamic consistency by architecture design, predicting activity coefficients of binary mixtures through automatic differentiation of thermodynamic relations.

### Theme 3: Training Efficiency and System Optimization

As GNNs scale to larger graphs, training efficiency has become a critical concern. Bajaj et al. (2024) provide a comprehensive empirical comparison of full-graph versus mini-batch GNN training systems, finding that mini-batch training consistently converges faster and achieves similar or higher accuracy. Their work emphasizes using time-to-accuracy rather than epoch time as the performance metric and selecting hyperparameters separately for each training method. This systems-level analysis provides practical guidance for GNN practitioners facing scalability challenges.

### Theme 4: Specialized Architectures for Challenging Graph Properties

Recent work has developed specialized GNN architectures to handle graphs that violate standard assumptions or require unique capabilities:

**Heterophilous Graphs**: Zheng et al. (2024) address the limitation that most GNNs assume homophily (nearby nodes exhibit similar behaviors), which fails in many real-world graphs. Their HDP method adaptively separates neighbors into homophilous and heterophilous parts, using prototype contrastive learning to model heterophilous distributions, outperforming baselines on heterophilous datasets.

**Energy-Efficient Continuous GNNs**: Fan et al. (2024) develop COS-GNN, combining continuous GNNs with spiking neural networks for energy-efficient deployment on battery-powered devices. Their architecture uses second-order ODEs for spiking representation and continuous propagation, with theoretical guarantees against exploding and vanishing gradients.

### Theme 5: Integration with Complementary Techniques

Multiple papers demonstrate successful integration of GNNs with other machine learning paradigms. Pan et al. (2025) combine GNNs with LLMs via retrieval-augmented generation for netlist format conversion. Han et al. (2025) integrate physics-based compartmental models with data-driven GNNs for interpretable forecasting. Lai et al. (2025) merge GNNs with reinforcement learning for multi-robot planning. Fan et al. (2024) fuse GNNs with spiking neural networks for energy efficiency. This pattern suggests that hybrid approaches leveraging complementary strengths of different paradigms represent a promising direction for GNN research.

## Convergences and Disagreements

**Convergences**: The surveyed literature converges on several points. First, graph representation quality critically impacts GNN performance, with multiple papers demonstrating that domain-appropriate representations (heterogeneous graphs for power grids, dynamic graphs for mobility networks) substantially outperform generic approaches (de Jong et al., 2025; Han et al., 2025). Second, mini-batch training achieves comparable or superior accuracy to full-graph training while converging faster (Bajaj et al., 2024). Third, integrating domain knowledge—whether physics constraints, thermodynamic relations, or epidemiological models—improves both performance and interpretability (Han et al., 2025; Rittig & Mitsos, 2024). Fourth, GNNs demonstrate strong generalization capabilities when trained on diverse synthetic data, with multiple papers reporting zero-shot or cross-dataset generalization (Lai et al., 2025; Pan et al., 2025).

**Disagreements**: The literature shows limited direct disagreement, as papers focus on different application domains. However, there is tension between architectural specialization versus generality. Joshi (2025) suggests Transformers (a general architecture) may be sufficient for many tasks due to hardware efficiency, while domain-specific papers (de Jong et al., 2025; Zheng et al., 2024) demonstrate clear benefits from specialized graph representations and message passing schemes. This reflects an ongoing debate about whether general-purpose or domain-specific architectures represent the optimal path forward.

## Gaps and Open Questions

Several gaps emerge from collective limitations acknowledged across the surveyed papers:

1. **Real-World Deployment**: Multiple papers evaluate primarily in simulation (Zhao et al., 2025; Lai et al., 2025), with limited real-world deployment validation. The gap between simulated performance and practical deployment remains underexplored.

2. **Scalability**: Several papers note challenges scaling to large graphs or networks (Pan et al., 2025), with linear computational complexity becoming prohibitive for large-scale applications. Efficient algorithms for massive graphs remain an open challenge.

3. **Latency-Critical Applications**: GNN approaches for scheduling and control focus on delay-tolerant scenarios (Zhao et al., 2025), with limited work on latency-critical real-time applications requiring millisecond-level response times.

4. **Cross-Domain Generalization**: While individual papers demonstrate cross-dataset generalization within their domains, systematic understanding of what enables GNNs to generalize across domains remains limited.

5. **Energy Efficiency Metrics**: Despite claims of energy efficiency (Fan et al., 2024), few papers report comprehensive energy consumption metrics or real-device deployment results, making it difficult to assess practical energy benefits.

6. **Multi-Component Systems**: Thermodynamics-focused work addresses only binary mixtures (Rittig & Mitsos, 2024), with extension to multi-component systems remaining unexplored.

## Per-Paper Annotations

### Bajaj et al. (2024)

**Research question**: How do full-graph and mini-batch GNN training systems compare in terms of convergence speed, accuracy, and overall performance?

**Methodology**: Conducts comprehensive empirical comparison of representative full-graph and mini-batch GNN training systems across multiple datasets, GNN models, and system configurations, using time-to-accuracy as the primary performance metric.

**Key findings**:
- Mini-batch training systems consistently converge faster than full-graph training systems across all tested configurations
- Mini-batch training converges to similar or often higher accuracy values than full-graph training
- Mini-batch sampling is not necessarily detrimental to model accuracy
- Time-to-accuracy is more appropriate than epoch time for performance comparison between training methods
- Appropriate hyperparameters should be selected separately for each training method rather than using shared configurations

**Limitations**: Empirical findings may vary with different system configurations, hardware setups, or future system optimizations; the study does not provide definitive guidance for all possible GNN architectures and application domains.

### de Jong et al. (2025)

**Research question**: How does the choice of graph representation affect GNN effectiveness for power grid topology control applications?

**Methodology**: Investigates homogeneous versus heterogeneous graph representations for power grids, identifies the busbar information asymmetry problem, and evaluates GNNs with both representations plus an FCNN baseline on an imitation learning task using classification accuracy and grid operation ability metrics.

**Key findings**:
- Homogeneous graph representations suffer from a busbar information asymmetry problem that limits GNN effectiveness
- Heterogeneous graph representations resolve the busbar information asymmetry problem
- Heterogeneous GNNs achieve the best performance on in-distribution network configurations
- FCNNs outperform homogeneous GNNs but underperform heterogeneous GNNs on in-distribution data
- Both GNN types generalize better to out-of-distribution network configurations than FCNNs

**Limitations**: Evaluation is limited to imitation learning tasks on specific power grid configurations; real-world deployment performance and computational requirements for large-scale grids are not thoroughly addressed.

### Fan et al. (2024)

**Research question**: How can continuous graph neural networks be made more energy-efficient for deployment on battery-powered devices while maintaining their ability to capture long-range dependencies?

**Methodology**: The authors incorporate spiking neural networks with continuous GNNs in a unified framework called COS-GNN, employing SNNs for graph node representation at each time step integrated into ODE processes, with a high-order structure using second-order ODE for enhanced information preservation and continuous propagation.

**Key findings**:
- COS-GNN effectively mitigates exploding and vanishing gradient problems with theoretical proof
- The architecture enables capture of long-range dependencies between nodes
- The spiking neural network integration provides energy-efficient inference suitable for battery-powered devices
- Experimental results demonstrate effectiveness over competitive baselines on graph-based learning tasks

**Limitations**: The abstract does not report specific energy consumption metrics or real-device deployment results; the computational overhead of second-order ODE integration may offset some energy gains.

### Han et al. (2025)

**Research question**: How can epidemic forecasting be improved by integrating physics-based disease transmission models with deep learning while maintaining interpretability of epidemiological parameters?

**Methodology**: The authors propose a Causal Spatiotemporal Graph Neural Network (CSTGNN) that integrates a Spatio-Contact SIR model with GNNs, using an adaptive static connectivity graph for stable human mobility components and a temporal dynamics model to capture fluctuations, combined with a temporal decomposition model for handling temporal dependence.

**Key findings**:
- The CSTGNN effectively models spatiotemporal dynamics of infectious diseases with improved forecasting accuracy
- The model was validated on real-world datasets at provincial level in China and state level in Germany
- Analysis of learned parameters provides interpretable insights into disease transmission mechanisms
- The hybrid framework bridges the gap between traditional compartmental models and pure deep learning approaches

**Limitations**: Validation was limited to specific geographic regions (Chinese provinces and German states); generalizability to other regions with different mobility patterns and healthcare systems requires further investigation.

### Joshi (2025)

**Research question**: What is the mathematical and architectural relationship between Transformer models and Graph Neural Networks?

**Methodology**: Establishes theoretical connections by showing Transformers can be viewed as message passing GNNs operating on fully connected token graphs, where self-attention captures token relationships and positional encodings provide structural information.

**Key findings**:
- Transformers are mathematically equivalent to message passing GNNs on fully connected graphs of tokens
- Self-attention mechanisms capture the relative importance of all tokens with respect to each other
- Positional encodings provide hints about sequential ordering or structure to the model
- Transformers are expressive set processing networks that learn relationships without requiring predefined graph structures
- Transformers outperform sparse GNN implementations due to efficient dense matrix operations on modern hardware

**Limitations**: This is a theoretical position paper that establishes conceptual connections rather than proposing new architectures or empirical improvements; practical implications for model design remain to be explored.

### Lai et al. (2025)

**Research question**: How can we achieve automated collision-free coordination of multiple robots for joint task allocation, scheduling, and motion planning in shared obstacle-rich workspaces without relying on manual human-designed trajectories?

**Methodology**: The authors propose a reinforcement learning framework using a graph neural network policy trained on procedurally-generated environments with diverse obstacle layouts, robot configurations, and task distributions. The approach employs a graph representation of scenes to jointly solve task allocation, scheduling, and motion planning sub-problems.

**Key findings**:
- The GNN-RL policy successfully coordinates 8 robots performing 40 reaching tasks in a shared obstacle-rich workspace
- The trained policy generalizes zero-shot to unseen settings with varying robot placements, obstacle geometries, and task poses
- The high-speed capability enables workcell layout optimization with improved solution times
- The planner supports fault-tolerant planning and online perception-based re-planning for rapid adaptation to dynamic task sets

**Limitations**: The approach was primarily validated in simulation environments; real-world deployment challenges and hardware-specific constraints are not fully addressed in the abstract.

### Pan et al. (2025)

**Research question**: How can GNNs improve circuit link prediction accuracy while addressing insufficient topological pattern use, data scarcity, and limited netlist format adaptability?

**Methodology**: Proposes GNN-ACLP featuring the SEAL framework for link prediction, Netlist Babel Fish (a RAG-enhanced LLM tool for netlist format conversion), and introduces the SpiceNetlist dataset with 775 annotated circuits.

**Key findings**:
- SEAL framework achieves port-level accuracy in circuit link prediction by leveraging subgraphs, embeddings, and attributes
- Netlist Babel Fish enhances compatibility across different netlist formats using retrieval-augmented generation with LLMs
- SpiceNetlist dataset comprises 775 annotated circuits of 7 types across 10 component classes
- Achieves 16.08% accuracy improvement on SpiceNetlist, 11.38% on Image2Net, and 16.01% on Masala-CHAI in intra-dataset evaluation
- Maintains 92.05% to 99.07% accuracy in cross-dataset evaluation, demonstrating robust feature transfer capabilities

**Limitations**: Linear computational complexity makes processing large-scale netlists challenging and requires future optimization; dataset size, while comprehensive, may still limit generalization to rare circuit configurations.

### Zheng et al. (2024)

**Research question**: How can graph neural networks be improved for heterophilous graphs where the homophily assumption (nearby nodes exhibit similar behaviors) is violated?

**Methodology**: The authors propose heterophilous distribution propagation (HDP) that adaptively separates neighbors into homophilous and heterophilous parts based on pseudo assignments during training, with orthogonality-oriented constraint via trusted prototype contrastive learning and a novel semantic-aware message passing mechanism for both patterns.

**Key findings**:
- HDP outperforms representative baselines on heterophilous datasets across multiple benchmarks
- The method was extensively evaluated on 9 benchmark datasets with different levels of homophily
- Adaptive neighborhood separation addresses the insufficient neighborhood partition problem in existing HeterGNNs
- The orthogonality-oriented constraint and prototype contrastive learning effectively model heterophilous neighborhood distributions

**Limitations**: Performance emphasis is on heterophilous datasets; potential trade-offs or performance degradation on strongly homophilous graphs is not explicitly discussed in the abstract.

### Zhao et al. (2025)

**Research question**: How can GNNs reduce signaling overhead in distributed link scheduling for dense wireless networks while maintaining network capacity?

**Methodology**: Proposes a distributed link sparsification scheme using a GNN module trained via a novel offline constrained unsupervised learning algorithm that adjusts contention thresholds for individual links based on traffic statistics and network topology.

**Key findings**:
- GNN-based link sparsification effectively reduces scheduling overhead for delay-tolerant traffic
- The approach enables links to withdraw from scheduling contention when unlikely to succeed
- Method maintains network capacity while minimizing signaling overhead
- Technique alleviates network congestion and reduces radio footprints across four distinct distributed link scheduling protocols
- Effective in simulated wireless multi-hop networks with up to 500 links

**Limitations**: Approach is designed for delay-tolerant traffic and may not suit latency-critical applications; evaluation is limited to simulated environments rather than real-world wireless network deployments.

### Rittig and Mitsos (2024)

**Research question**: How can graph neural networks predict composition-dependent activity coefficients of binary mixtures while ensuring thermodynamic consistency without requiring additional loss terms?

**Methodology**: The authors propose excess Gibbs free energy GNNs (GE-GNNs) that predict molar excess Gibbs free energy and use automatic differentiation with thermodynamic relations to obtain activity coefficients in an end-to-end manner, ensuring thermodynamic consistency by architecture design rather than loss constraints.

**Key findings**:
- The GE-GNN architecture achieves high accuracy in activity coefficient predictions for binary mixtures
- Thermodynamic consistency is ensured by the architecture without requiring additional loss terms
- The approach avoids thermodynamic modeling limitations and assumptions by outputting a fundamental property
- Automatic differentiation enables end-to-end learning of differential thermodynamic relations

**Limitations**: The approach is demonstrated only for binary mixtures; extension to multi-component systems with more complex thermodynamic interactions is not addressed in the abstract.

## References

Bajaj, S., Son, H., Liu, J., Guan, H., & Serafini, M. (2024). Graph neural network training systems: A performance comparison of full-graph and mini-batch. arXiv. https://arxiv.org/abs/2406.00552

de Jong, M., Viebahn, J., & Shapovalova, Y. (2025). Graph neural networks for transmission grid topology control: Busbar information asymmetry and heterogeneous representations. arXiv. https://arxiv.org/abs/2501.07186

Fan, S., Zhang, Z., Yin, N., Li, T., Nie, H., Hu, D., & Hua, W. (2024). Continuous spiking graph neural networks. arXiv. https://arxiv.org/abs/2404.01897

Han, S., Stelz, L., Sokolowski, T. R., Zhou, K., & Stöcker, H. (2025). Unifying physics- and data-driven modeling via novel causal spatiotemporal graph neural network for interpretable epidemic forecasting. arXiv. https://arxiv.org/abs/2504.05140

Joshi, C. K. (2025). Transformers are graph neural networks. arXiv. https://arxiv.org/abs/2506.22084

Lai, M., Go, K., Li, Z., Kroger, T., Schaal, S., Allen, K., & Scholz, J. (2025). RoboBallet: Planning for multi-robot reaching with graph neural networks and reinforcement learning. arXiv. https://arxiv.org/abs/2509.05397

Pan, G., Zhou, T., Zhao, J., Li, Z., Lin, Y., Ma, B., Wang, Y., Liò, P., & Wang, S. (2025). Graph neural networks based analog circuit link prediction. arXiv. https://arxiv.org/abs/2504.10240

Zheng, Z., Zhou, S., Xu, H., Gu, M., Xu, Y., Li, A., Li, Y., Gu, J., & Bu, J. (2024). Heterophilous distribution propagation for graph neural networks. arXiv. https://arxiv.org/abs/2405.20640

Zhao, Z., Verma, G., Swami, A., & Segarra, S. (2025). Distributed link sparsification for scalable scheduling using graph neural networks (journal version). arXiv. https://arxiv.org/abs/2509.05447

Rittig, J. G., & Mitsos, A. (2024). Thermodynamics-consistent graph neural networks. arXiv. https://arxiv.org/abs/2407.18372
