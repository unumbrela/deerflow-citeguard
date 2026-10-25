# Systematic Literature Review: Federated Learning

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "federated learning", cs.LG, 2024-01-01 to 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

The federated learning literature from 2024-2026 reveals a field maturing beyond its initial privacy-preserving premise to address critical challenges in practical deployment. The surveyed papers collectively demonstrate that while FL successfully prevents direct data exchange, significant privacy vulnerabilities persist through gradient leakage and parameter analysis, requiring sophisticated countermeasures including differential privacy and dynamic perturbation techniques. A dominant theme addresses statistical heterogeneity and client participation dynamics, with multiple papers proposing novel aggregation strategies and incentive mechanisms to sustain collaborative learning in real-world cross-silo environments. Emerging directions include quantum federated learning, blockchain-enabled trust architectures, and domain-specific applications in healthcare and industrial settings, indicating FL's expansion into diverse application domains. However, the literature consistently acknowledges trade-offs between privacy, performance, and participation that remain incompletely resolved, particularly for non-IID and small dataset scenarios.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "federated learning", filtered to category cs.LG, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Privacy Threats and Defense Mechanisms

A substantial body of recent FL research focuses on understanding and mitigating privacy vulnerabilities that persist despite the federated architecture. While FL was originally conceived as privacy-preserving by design, recent work demonstrates that training data can still be leaked through gradient analysis and parameter weight inspection. Wei et al. (2024) reveal that gradient updates during federated training can expose training data, requiring careful perturbation strategies before sharing. Their analytical study demonstrates that adding controlled randomized noise to raw gradients can mitigate leakage, but the effectiveness depends critically on determining the proper amount and location of noise injection.

Complementing this work, Hayashitani et al. (2024) provide a comprehensive taxonomy of privacy threats across three FL architectures: horizontal, vertical, and transfer federated learning. Their survey reveals that privacy threats vary significantly by architecture type, with each having both common and unique vulnerabilities requiring specific countermeasures. Banse et al. (2024) empirically demonstrate that differential privacy mechanisms, while providing protection, introduce measurable performance trade-offs that are particularly severe for non-IID and small datasets.

The convergence of these findings suggests that privacy in FL requires multi-layered defense strategies combining gradient perturbation, differential privacy, and architecture-specific countermeasures, with careful calibration to minimize performance degradation.

### Theme 2: Statistical Heterogeneity and Client Selection

Data heterogeneity represents one of the most persistent challenges in FL, with multiple papers proposing innovative solutions to address non-IID data distributions across clients. Németh et al. (2025) characterize statistical heterogeneity through six metrics capturing global and client attribute imbalance, class imbalance, and spurious correlations. Their FEDDIVERSE algorithm addresses this challenge through diversity-driven client selection, promoting collaboration between clients with complementary data distributions. Experiments across seven newly created computer vision datasets demonstrate that this approach enhances performance and robustness of various FL methods while maintaining low communication and computational overhead.

Legler et al. (2024) examine the complementary challenge of integrating new clients into existing FL systems, particularly in production environments where the number of clients is typically smaller than in consumer applications like Gboard. Their work emphasizes that each new client's data becomes increasingly valuable in such settings, requiring effective client selection strategies that balance data diversity benefits against system stability and efficiency concerns.

These papers collectively establish that heterogeneity is not merely a technical obstacle but a fundamental characteristic of real-world FL deployments that must be actively managed through intelligent client selection and aggregation strategies.

### Theme 3: Incentive Mechanisms and Rational Participation

A critical insight emerging from recent literature is that FL clients are rational agents who may prioritize local utility over global model performance, creating participation dilemmas that threaten system sustainability. Yashwanth et al. (2026) introduce FedUCA, a framework formalizing the server's role as an optimizer that maximizes global performance by sustaining client participation through utility-constrained stochastic aggregation. Their extensive experiments demonstrate that prioritizing participation feasibility achieves significantly higher client retention and superior global model performance compared to traditional approaches that assume passive client compliance.

Hewa Kaluannakkage and Buyya (2025) expand this perspective through a comprehensive taxonomy examining how economics and game theory concepts can be applied to FL incentive design, alongside technology-driven solutions including blockchain and deep reinforcement learning. Their analysis reveals that well-designed incentive mechanisms are not optional features but essential components for practical FL success across diverse domains including healthcare, smart infrastructure, vehicular networks, and decentralized systems.

The convergence of these works establishes incentive design as a foundational requirement for sustainable FL ecosystems, particularly in cross-silo environments where clients have autonomy over participation decisions.

### Theme 4: Blockchain-Enabled Trust Architectures

Blockchain technology emerges as a promising solution for addressing trust, privacy, and coordination challenges in collaborative AI systems. Rangwala et al. (2025) provide comprehensive architectural analysis of blockchain-enabled federated learning (BCFL) systems through a four-dimensional taxonomy examining coordination structures, consensus mechanisms, storage architectures, and trust models. Their analysis demonstrates how consensus mechanisms like Proof of Quality and Proof of Federated Learning repurpose computational work from arbitrary cryptographic puzzles to productive machine learning tasks, creating aligned incentives for honest participation.

The TrustMesh framework case study illustrates practical implementation considerations, showing effective collaborative learning across IoT devices with highly non-IID data distributions while maintaining complete transparency and fault tolerance. Real-world deployments across healthcare consortiums, financial services, and IoT security applications validate BCFL's practical viability, achieving performance comparable to centralized approaches while providing enhanced security guarantees and enabling trustless collaborative intelligence.

### Theme 5: Domain-Specific Applications and Specialized Frameworks

Recent FL research increasingly targets domain-specific challenges, with healthcare applications receiving particular attention. Ho (2026) presents the first federated learning framework for automated infant movement analysis and General Movement Assessment using skeletal motion data. The proposed Uncertainty-Aware Federated Averaging (UA-FedAvg) strategy incorporates predictive entropy from Monte Carlo Dropout into the aggregation process, enabling client contributions to be adjusted according to predictive uncertainty. Results demonstrate that FL substantially improves classification performance compared to independently trained local models while approaching centralized training performance.

In emerging computational paradigms, Pokhrel et al. (2024) explore quantum federated learning deployment on cloud platforms. Their data-encoding-driven QFL approach, implemented as a proof-of-concept using genomic datasets on quantum simulators, shows promising results despite quantum intricacies and platform limitations. This work represents an early but significant step toward collaborative quantum model training with local data privacy preservation.

## Convergences and Disagreements

**Convergences**: Multiple papers converge on the finding that non-IID data distributions present the most significant challenge to FL performance and stability. Wei et al. (2024), Banse et al. (2024), Legler et al. (2024), and Németh et al. (2025) all identify data heterogeneity as a primary obstacle requiring active management. There is also broad agreement that privacy in FL requires defense-in-depth strategies rather than relying solely on the federated architecture itself.

The literature consistently demonstrates that client participation cannot be assumed but must be actively sustained through utility-aware aggregation or explicit incentive mechanisms, as shown by both Yashwanth et al. (2026) and Hewa Kaluannakkage and Buyya (2025).

**Disagreements**: The literature shows less consensus on optimal trade-offs between privacy and performance. While Wei et al. (2024) advocate for dynamic model perturbation as simultaneously ensuring privacy, poisoning resilience, and performance, Banse et al. (2024) empirically demonstrate that differential privacy mechanisms inevitably introduce performance degradation, particularly severe for small and non-IID datasets. This tension between theoretical promises of simultaneous optimization and empirical evidence of unavoidable trade-offs remains unresolved.

Additionally, there is divergence in architectural preferences: Rangwala et al. (2025) advocate for blockchain integration for trust and transparency, while other papers achieve robust results through centralized coordination with sophisticated aggregation strategies, suggesting context-dependent optimal architectures rather than universal solutions.

## Gaps and Open Questions

The collective literature reveals several significant gaps:

1. **Quantitative thresholds for privacy-utility trade-offs**: While multiple papers acknowledge trade-offs between privacy mechanisms and model performance, none establish generalizable quantitative thresholds for optimal noise levels or privacy budgets across different domains and data characteristics.

2. **Real-world deployment validation**: Most papers validate their approaches on standard datasets or limited case studies. Wei et al. (2024), Legler et al. (2024), and Németh et al. (2025) all acknowledge limited real-world deployment validation, suggesting a gap between proposed solutions and production-ready implementations.

3. **Scalability to large federated networks**: Several approaches, particularly Ho (2026) with three clients and Legler et al. (2024) focusing on small production environments, are validated in small-scale settings. Scalability to hundreds or thousands of clients remains underexplored.

4. **Domain generalization**: Németh et al. (2025) focus on computer vision datasets, while Ho (2026) addresses healthcare. Cross-domain validation of FL methods, particularly for NLP or tabular data, remains limited.

5. **Quantum FL practical deployment**: Pokhrel et al. (2024) conduct experiments on quantum simulators rather than actual quantum hardware, with cloud platform limitations and quantum network infrastructure remaining significant practical barriers.

6. **Long-term sustainability of incentive mechanisms**: While Hewa Kaluannakkage and Buyya (2025) and Yashwanth et al. (2026) propose incentive frameworks, long-term empirical validation of these mechanisms in sustained FL ecosystems is absent from the literature.

## Per-Paper Annotations

### Banse et al. (2024)

**Research question**: How do the number of clients and differential privacy mechanisms affect federated learning model performance across different data types?
**Methodology**: Empirical benchmark examining the effect of client count and differential privacy mechanisms on model performance across different types of data distributions.
**Key findings**:
- Non-i.i.d datasets experience the highest performance decrease in distributed and differentially private settings
- Small datasets show significant performance degradation when DP mechanisms are applied
- The number of clients impacts model performance in DP-enabled FL
- Private information can still be divulged by analyzing uploaded parameter weights despite FL's privacy-preserving nature
- DP mechanisms introduce measurable performance trade-offs that vary by data characteristics
**Limitations**: This is an empirical benchmark study that identifies performance issues but does not propose solutions to mitigate the performance degradation in non-i.i.d and small dataset scenarios.

### Hayashitani et al. (2024)

**Research question**: How can common and unique privacy threats be systematically categorized and described across different types of federated learning architectures?
**Methodology**: Comprehensive survey approach categorizing privacy threats and countermeasures for three typical FL types: horizontal, vertical, and transfer federated learning.
**Key findings**:
- Federated learning is not inherently privacy-safe despite no direct training data exchange between clients
- Privacy threats vary significantly across horizontal, vertical, and transfer federated learning architectures
- Each FL type has both common and unique privacy vulnerabilities requiring specific countermeasures
- Existing privacy countermeasures have been studied but lack comprehensive categorization by FL type
**Limitations**: As a survey paper, it provides categorization rather than novel empirical validation; specific implementation details of countermeasures may require further investigation.

### Hewa Kaluannakkage and Buyya (2025)

**Research question**: How can incentive mechanisms address the participation dilemma in federated learning to ensure sustainable, fair, and robust FL ecosystems?
**Methodology**: Comprehensive taxonomy development examining economics and game theory concepts, blockchain, and deep reinforcement learning applied to both centralized and decentralized FL architectures.
**Key findings**:
- Participation dilemma is a critical barrier: entities unwilling to contribute without benefits or may free-ride on others' contributions
- Well-designed incentive mechanisms are essential components, not optional features, for practical FL success
- Economics and game theory concepts can be effectively applied alongside technology solutions like blockchain and deep reinforcement learning
- Incentive mechanisms must address diverse application domains including healthcare, smart infrastructure, vehicular networks, and decentralized systems
- Both centralized and decentralized architectures require different incentive design approaches
**Limitations**: Significant challenges remain in building truly sustainable and fair FL ecosystems; practical implementation and validation across diverse industrial applications requires further work.

### Ho (2026)

**Research question**: How can federated learning enable automated infant movement analysis while addressing privacy and data-sharing constraints in clinical settings?
**Methodology**: Presents the first FL framework for automated infant movement analysis using Monte Carlo Dropout for uncertainty estimation and proposes Uncertainty-Aware Federated Averaging (UA-FedAvg) that incorporates predictive entropy into the aggregation process.
**Key findings**:
- Federated learning substantially improves classification performance compared to independently trained local models
- FL performance approaches that of centralized training
- UA-FedAvg generally outperforms conventional FedAvg across evaluated data-split configurations
- UA-FedAvg variant incorporating validation loss shows additional improvements
- First federated learning framework specifically designed for infant movement analysis and General Movement Assessment
**Limitations**: Evaluated on a specific use case (fidgety movement classification) with only three clients, which may limit generalizability to broader clinical settings or larger federated networks.

### Legler et al. (2024)

**Research question**: How can new clients be seamlessly integrated into existing FL systems despite data heterogeneity and varying computational capabilities?
**Methodology**: Analysis of client integration complexities with exploration of data heterogeneity effects, client selection strategies, and practical approaches demonstrated through optical quality inspection image data.
**Key findings**:
- Dynamic incorporation of new clients with diverse data distributions poses significant challenges to FL system stability and efficiency
- Non-IID data distribution among clients critically affects model training, system efficiency, scalability, and stability
- Production environments typically have fewer clients than consumer applications, making information from each new client more valuable
- New client integration presents opportunities to enhance data diversity, improve learning performance, and leverage distributed computational power
- Effective client selection strategies are crucial for ensuring system scalability and stability in production FL deployments
**Limitations**: Focus on optical quality inspection as primary use case may limit generalizability; specific quantitative metrics for client selection effectiveness require further validation across diverse domains.

### Németh et al. (2025)

**Research question**: How can federated learning address statistical data heterogeneity that impacts model generalization, convergence speed, and performance?
**Methodology**: Proposes characterization of statistical heterogeneity through 6 metrics, creates 7 computer vision datasets covering diverse heterogeneity patterns, and introduces FEDDIVERSE, a client selection algorithm promoting collaboration between clients with complementary data distributions.
**Key findings**:
- FEDDIVERSE enhances performance and robustness of various FL methods
- The algorithm has low communication and computational overhead
- Seven new FL datasets were created and shared covering broad range of statistical data heterogeneity
- Six metrics effectively characterize global and client attribute imbalance, class imbalance, and spurious correlations
- Promoting collaboration between clients with complementary distributions improves model generalization
**Limitations**: Focused primarily on computer vision datasets for binary and multiclass image classification; may require validation on other domains such as NLP or tabular data.

### Pokhrel et al. (2024)

**Research question**: What are the challenges of deploying Quantum Federated Learning on cloud platforms, and how can data encoding strategies address quantum network limitations?
**Methodology**: Proof-of-concept implementation using data-encoding-driven QFL with genomic datasets on quantum simulators, with open-source code available on GitHub.
**Key findings**:
- QFL enables collaborative quantum model training while preserving local data privacy over quantum networks
- Cloud platform deployment faces significant quantum intricacies and platform-specific limitations
- Data-encoding-driven approaches show promising results for QFL implementation
- Genomic datasets can be effectively used for QFL proof-of-concept on quantum simulators
**Limitations**: Experiments conducted on quantum simulators rather than actual quantum hardware; cloud platform limitations and quantum network infrastructure remain significant practical barriers.

### Rangwala et al. (2025)

**Research question**: How can blockchain technology address fundamental challenges of trust, privacy, and coordination in collaborative AI systems?
**Methodology**: Provides comprehensive architectural analysis through a systematic four-dimensional taxonomy examining coordination structures, consensus mechanisms, storage architectures, and trust models, including a TrustMesh framework case study.
**Key findings**:
- BCFL systems achieve performance comparable to centralized approaches while providing enhanced security guarantees
- Consensus mechanisms like Proof of Quality and Proof of Federated Learning repurpose computational work from cryptographic puzzles to productive ML tasks
- Multi-tier storage architectures balance blockchain transaction constraints with neural network parameter requirements
- Real-world deployments validated across healthcare consortiums, financial services, and IoT security applications
- Enables new models of trustless collaborative intelligence with complete transparency and fault tolerance
**Limitations**: Design patterns involve trade-offs in scalability, security, and performance that must be carefully balanced; blockchain's transaction constraints pose challenges for large neural network parameters.

### Wei et al. (2024)

**Research question**: What are the privacy intrusion and data poisoning threats in federated learning, and how can they be effectively mitigated while maintaining model performance?
**Methodology**: Analytical study with empirical evidence examining gradient leakage threats, poisoning attacks, and defense strategies including gradient perturbation and dynamic model perturbation techniques.
**Key findings**:
- Training data can be leaked during federated training through gradient updates, requiring careful noise addition to raw gradients before sharing
- The proper amount and location of randomized noise is critical for effective mitigation of gradient leakage threats
- Data poisoning-induced model Trojan attacks can cause detrimental damage to global model performance
- Dynamic model perturbation shows potential for simultaneously ensuring privacy protection, poisoning resilience, and model performance
- Additional risk factors include data skewness, algorithmic biases, and misinformation in training data
**Limitations**: The study focuses primarily on empirical observations without extensive real-world deployment validation; specific quantitative thresholds for optimal noise levels are not fully established.

### Yashwanth et al. (2026)

**Research question**: How can federated learning sustain client participation when clients are rational agents who may prioritize local model performance over global model performance?
**Methodology**: Introduces FedUCA, a framework that formalizes the server's role as an optimizer seeking to maximize global model performance by sustaining client participation through utility-constrained stochastic aggregation.
**Key findings**:
- FedUCA achieves significantly higher client retention compared to traditional FL approaches
- Higher client retention leads to superior global model performance
- The framework effectively addresses client attrition in cross-silo environments with significant statistical heterogeneity
- Extensive experiments on standard datasets demonstrate the framework's effectiveness
**Limitations**: The paper does not explicitly discuss limitations, but the approach may be primarily validated on standard datasets and may require further testing in diverse real-world cross-silo scenarios.

## References

Banse, A., Kreischer, J., & Oliva i Jürgens, X. (2024). Federated learning with differential privacy. arXiv. https://arxiv.org/abs/2402.02230

Hayashitani, M., Mori, J., & Teranishi, I. (2024). Survey of privacy threats and countermeasures in federated learning. arXiv. https://arxiv.org/abs/2402.00342

Hewa Kaluannakkage, C. A. S., & Buyya, R. (2025). Incentive-based federated learning: Architectural elements and future directions. arXiv. https://arxiv.org/abs/2510.14208

Ho, E. S. L. (2026). Uncertainty-aware federated learning for infant movement analysis. arXiv. https://arxiv.org/abs/2609.31463

Legler, T., Hegiste, V., & Ruskowski, M. (2024). Seamless integration: Sampling strategies in federated learning systems. arXiv. https://arxiv.org/abs/2408.09545

Németh, G. D., Fanì, E., Ng, Y. J., Caputo, B., Lozano, M. Á., Oliver, N., & Quadrianto, N. (2025). FedDiverse: Tackling data heterogeneity in federated learning with diversity-driven client selection. arXiv. https://arxiv.org/abs/2504.11216

Pokhrel, S. R., Yash, N., Kua, J., Li, G., & Pan, L. (2024). Quantum federated learning experiments in the cloud with data encoding. arXiv. https://arxiv.org/abs/2405.00909

Rangwala, M., Venugopal, K. R., & Buyya, R. (2025). Blockchain-enabled federated learning. arXiv. https://arxiv.org/abs/2508.06406

Wei, W., Huang, T., Yahn, Z., Singhal, A., Loper, M., & Liu, L. (2024). Data poisoning and leakage analysis in federated learning. arXiv. https://arxiv.org/abs/2409.13004

Yashwanth, M., Singh, A., Nayak, A., Bulusu, S. K., & Chakraborty, A. (2026). Federated learning by utility-constrained stochastic aggregation for improving rational participation. arXiv. https://arxiv.org/abs/2605.18020
