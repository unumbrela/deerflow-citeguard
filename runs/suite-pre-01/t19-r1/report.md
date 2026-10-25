# Systematic Literature Review: Federated Learning

**Date**: 2026-10-25
**Papers surveyed**: 10
**Scope**: "federated learning" in cs.LG, published between 2024-01-01 and 2026-10-25
**Citation format**: APA 7th edition

## Executive Summary

This systematic literature review examines 10 recent arXiv papers on federated learning published between 2024 and 2026, revealing a field rapidly maturing beyond foundational algorithms toward practical deployment challenges. The surveyed literature collectively demonstrates that federated learning has evolved from a privacy-preserving training paradigm to a complex ecosystem requiring solutions for security threats, client participation incentives, data heterogeneity management, and architectural innovations. Multiple papers converge on the finding that non-IID data distributions and privacy-utility trade-offs remain central obstacles, while proposing diverse solutions ranging from differential privacy mechanisms to blockchain-enabled coordination and incentive-compatible aggregation strategies. The literature reveals significant momentum in domain-specific applications, particularly in healthcare, alongside emerging frontiers in quantum federated learning. However, gaps persist in real-world deployment validation, standardized evaluation benchmarks, and comprehensive frameworks addressing multiple challenges simultaneously.

## Methodology

This review surveyed 10 arXiv papers retrieved on 2026-10-25 using the query "federated learning" filtered to category cs.LG, published between 2024-01-01 and 2026-10-25. Papers were sorted by relevance and the top 10 were included. Metadata extraction (research question, methodology, key findings, limitations) was performed by language-model agents, with cross-paper synthesis performed by the lead agent.

**Limitations of this review**: arXiv preprints are not peer-reviewed; some included papers may not reflect their final published form. Coverage is limited to arXiv — papers published directly in venues without arXiv preprints are not represented.

## Themes

### Theme 1: Privacy and Security Threats

A substantial portion of recent federated learning research focuses on understanding and mitigating privacy and security vulnerabilities inherent in distributed training. Despite FL's foundational promise of preserving data privacy by avoiding direct data exchange, multiple papers demonstrate that significant risks persist through gradient leakage and poisoning attacks.

Wei et al. (2024) provide comprehensive analysis of two dominating threats: training data privacy intrusion and training data poisoning. Their empirical study reveals that training data can be reconstructed from gradient updates shared during federated training rounds, challenging the assumption that parameter sharing is inherently safe. The authors demonstrate that adding controlled randomized noise to gradients before sharing effectively mitigates leakage threats, while dynamic model perturbation can simultaneously address both privacy and poisoning concerns. This work establishes that privacy in FL requires active defense mechanisms rather than passive reliance on the federated architecture itself.

Hayashitani et al. (2024) extend this analysis through a systematic survey categorizing privacy threats across horizontal, vertical, and transfer federated learning architectures. Their key contribution is demonstrating that different FL types face distinct and unique privacy threats requiring tailored countermeasures, rather than one-size-fits-all solutions. This categorization framework enables practitioners to identify which threats are most relevant to their specific FL deployment and select appropriate defenses accordingly.

Banse et al. (2024) empirically benchmark the performance trade-offs introduced by differential privacy mechanisms in federated learning. Their critical finding is that non-IID and small datasets exhibit the highest performance degradation in differentially private settings, revealing a fundamental tension between privacy guarantees and model utility in realistic FL scenarios where data heterogeneity is the norm rather than the exception.

### Theme 2: Client Selection and Participation Incentives

The literature reveals growing recognition that federated learning success depends critically on sustaining client participation, particularly in cross-silo environments where clients are rational agents with their own utility functions. This represents a shift from viewing clients as passive participants to understanding them as strategic actors whose continued engagement must be actively maintained.

Yashwanth et al. (2026) introduce FedUCA (Federated Learning by Utility-Constrained Stochastic Aggregation), a framework that formalizes the server's role as an optimizer seeking to maximize global model performance by sustaining client participation. Their work addresses the critical observation that in settings with significant statistical heterogeneity, rational clients may opt out of federation if perceived benefits fail to meet local utility thresholds, potentially causing federated training collapse. FedUCA achieves significantly higher client retention and superior global model performance by prioritizing participation feasibility in aggregation decisions.

Hewa Kaluannakkage and Buyya (2025) provide comprehensive taxonomy of incentive mechanisms for federated learning, demonstrating that well-designed incentives are essential components rather than optional features for sustainable FL ecosystems. Their analysis spans centralized and decentralized architectures, incorporating economic theory, game theory, blockchain, and deep reinforcement learning approaches. The participation dilemma—where entities are unwilling to contribute without receiving benefits, or may free-ride on others' contributions—is identified as a fundamental barrier to practical FL adoption requiring systematic incentive design.

Németh et al. (2025) propose FEDDIVERSE, a diversity-driven client selection algorithm that addresses data heterogeneity by promoting collaboration between clients with complementary data distributions. Their approach characterizes statistical heterogeneity through six metrics of global and client attribute imbalance, class imbalance, and spurious correlations, then leverages this characterization to select clients whose data distributions complement rather than conflict with existing participants. Experiments across seven computer vision datasets demonstrate enhanced performance and robustness with low communication and computational overhead.

### Theme 3: Data Heterogeneity and Non-IID Challenges

Statistical heterogeneity across clients emerges as a pervasive challenge throughout the surveyed literature, affecting convergence speed, model generalization, and client retention. Multiple papers propose complementary approaches to managing non-IID data distributions that characterize real-world FL deployments.

Legler et al. (2024) investigate the complexities of integrating new clients into existing FL systems, revealing that data heterogeneity and varying non-IID distributions significantly affect model training, system efficiency, scalability, and stability. Their work emphasizes that production environments typically have fewer clients than original FL applications like Gboard, making each new client's information more valuable and necessitating effective client selection strategies. The authors propose practical approaches for seamless client integration that enhance data diversity while maintaining system stability.

The FedUCA framework (Yashwanth et al., 2026) and FEDDIVERSE algorithm (Németh et al., 2025) both address heterogeneity through different mechanisms—FedUCA by constraining aggregation to maintain client participation, and FEDDIVERSE by actively selecting clients with complementary distributions. Together, these works demonstrate that heterogeneity management requires both algorithmic innovations and strategic client selection.

Banse et al. (2024) add the critical insight that differential privacy mechanisms interact with data heterogeneity, with non-IID and small datasets suffering the highest performance degradation. This finding suggests that privacy-preserving FL in heterogeneous settings requires careful calibration of privacy budgets and potentially heterogeneity-aware DP mechanisms.

### Theme 4: Emerging Architectures and Paradigms

The surveyed literature reveals significant innovation in FL architectural designs, extending beyond traditional centralized aggregation to blockchain-enabled coordination and quantum federated learning, reflecting the field's expansion into new computational paradigms.

Rangwala et al. (2025) provide comprehensive architectural analysis of blockchain-enabled federated learning (BCFL) systems through a four-dimensional taxonomy examining coordination structures, consensus mechanisms, storage architectures, and trust models. Their work demonstrates how computational work can be repurposed from arbitrary cryptographic puzzles to productive machine learning tasks through consensus mechanisms like Proof of Quality and Proof of Federated Learning. The TrustMesh case study illustrates practical implementation achieving performance comparable to centralized approaches while providing enhanced security guarantees and enabling trustless collaborative intelligence across healthcare consortiums, financial services, and IoT security applications.

Pokhrel et al. (2024) explore quantum federated learning (QFL), an emerging paradigm unfolding FL over quantum networks to enable collaborative quantum model training with local data privacy. Their proof-of-concept implementation using data-encoding-driven QFL with genomic datasets on quantum simulators demonstrates feasibility despite quantum-specific intricacies and cloud platform limitations. This work positions FL at the intersection of quantum computing and distributed learning, opening new research directions for privacy-preserving quantum machine learning.

### Theme 5: Domain-Specific Applications and Production Deployment

The literature demonstrates FL's transition from theoretical framework to practical deployment across diverse domains, with particular emphasis on healthcare applications and production environments where privacy constraints and data governance make centralized training infeasible.

Ho (2026) presents the first federated learning framework for automated infant movement analysis and General Movement Assessment using skeletal motion data, addressing privacy and data-sharing constraints that make centralized training impractical in clinical settings. The proposed Uncertainty-Aware Federated Averaging (UA-FedAvg) strategy incorporates predictive entropy from Monte Carlo Dropout into the aggregation process, enabling client contributions to be adjusted according to predictive uncertainty. Results demonstrate that FL substantially improves classification performance compared to independently trained local models while achieving performance approaching centralized training, validating FL's viability for privacy-sensitive healthcare applications.

Legler et al. (2024) emphasize production environment considerations, noting that FL adoption requires addressing new client integration challenges to advance beyond research settings. Their work using optical quality inspection as a case study provides practical approaches for maintaining system stability and efficiency during client onboarding, contributing to FL's maturation toward industrial deployment.

Hewa Kaluannakkage and Buyya (2025) survey emerging industrial applications spanning healthcare, smart infrastructure, vehicular networks, and blockchain-based decentralized systems, demonstrating FL's expanding applicability across domains where data privacy, governance, or distribution make centralized training impractical or impossible.

## Convergences and Disagreements

**Convergences**: The surveyed literature demonstrates strong convergence on several key findings. First, all papers acknowledge that non-IID data distributions are the norm in real-world FL deployments and significantly impact model performance, convergence speed, and system stability. Second, multiple papers converge on the finding that privacy in FL requires active defense mechanisms—differential privacy, gradient perturbation, or architectural safeguards—rather than passive reliance on the federated architecture itself (Wei et al., 2024; Hayashitani et al., 2024; Banse et al., 2024). Third, there is consensus that client participation cannot be assumed and must be actively sustained through incentive mechanisms or utility-aware aggregation strategies (Yashwanth et al., 2026; Hewa Kaluannakkage & Buyya, 2025). Fourth, papers across themes agree that FL has matured beyond research prototypes toward practical deployment, with multiple works validating approaches on real-world datasets and production scenarios.

**Disagreements**: The literature shows fewer explicit disagreements, reflecting the survey nature of several papers and the complementary rather than competing nature of proposed solutions. However, tensions exist between different approaches to heterogeneity management—FedUCA (Yashwanth et al., 2026) prioritizes participation feasibility through utility-constrained aggregation, while FEDDIVERSE (Németh et al., 2025) actively selects clients based on data distribution complementarity. These represent different philosophical approaches: one adapts aggregation to retain all clients, the other curates participation to optimize collaboration. Additionally, while blockchain-enabled FL is presented as addressing trust and coordination challenges (Rangwala et al., 2025), the computational and scalability trade-offs of blockchain integration are not thoroughly compared against simpler centralized coordination with cryptographic verification, leaving open questions about when blockchain complexity is justified.

## Gaps and Open Questions

The collective literature reveals several significant gaps and open questions for future research:

**Real-world deployment validation**: Multiple papers acknowledge limitations in experimental validation, with approaches tested primarily on standard datasets rather than production deployments (Yashwanth et al., 2026; Rangwala et al., 2025). The gap between controlled experiments and real-world FL deployments—with their unpredictable client behavior, network conditions, and data characteristics—remains substantial.

**Comprehensive frameworks addressing multiple challenges**: While individual papers address privacy, heterogeneity, incentives, or architectural innovations, few propose integrated frameworks simultaneously addressing multiple challenges. Real-world FL deployments require solutions that jointly optimize for privacy, security, heterogeneity, participation incentives, and computational efficiency, yet the literature remains siloed along these dimensions.

**Standardized evaluation benchmarks**: The creation of seven FL datasets by Németh et al. (2025) acknowledges the lack of standardized benchmarks for evaluating FL methods under realistic heterogeneity conditions. The field would benefit from broader benchmark suites covering diverse domains beyond computer vision, enabling reproducible comparison of FL algorithms.

**Scalability of emerging architectures**: Blockchain-enabled FL (Rangwala et al., 2025) and quantum FL (Pokhrel et al., 2024) introduce architectural complexity whose scalability characteristics remain unexplored at large scale. Questions about transaction throughput, storage requirements, and quantum network feasibility at hundreds or thousands of clients remain open.

**Domain generalization**: FEDDIVERSE's focus on computer vision (Németh et al., 2025) and the healthcare-specific applications (Ho, 2026) highlight the need for cross-domain validation. Approaches demonstrated in one domain may not generalize to others with different heterogeneity patterns, privacy requirements, or computational constraints.

**Mitigation strategies for DP performance degradation**: While Banse et al. (2024) identify that non-IID and small datasets suffer highest performance degradation with differential privacy, their work lacks guidance on mitigating these effects. Developing heterogeneity-aware DP mechanisms or adaptive privacy budgets represents an important open direction.

## Per-Paper Annotations

### Banse et al. (2024)

**Research question**: How do the number of clients and differential privacy mechanisms affect model performance in federated learning across different data types and distributions?

**Methodology**: Empirical benchmark studying the effect of client count and differential privacy mechanisms on model performance across different data types, examining performance degradation patterns in distributed and differentially private settings.

**Key findings**:
- Non-i.i.d and small datasets exhibit the highest decrease in performance in distributed and differentially private settings
- DP mechanisms introduce measurable performance trade-offs that vary by data characteristics
- Number of clients significantly affects model performance in DP-FL configurations
- Performance degradation patterns differ across data types in privacy-preserving FL
- Empirical benchmark provides actionable insights for balancing privacy and utility in FL deployments

**Limitations**: Report format suggests limited scope; specific DP mechanisms and their comparative effectiveness not thoroughly explored; lacks guidance on mitigating performance degradation.

### Hayashitani et al. (2024)

**Research question**: What are the common and unique privacy threats across different types of federated learning, and how can they be systematically categorized with corresponding countermeasures?

**Methodology**: Comprehensive survey paper that categorizes and describes privacy threats and countermeasures across three typical types of federated learning: horizontal, vertical, and transfer federated learning.

**Key findings**:
- Federated learning is not inherently privacy-safe despite the absence of direct data exchange between clients
- Different FL architectures (horizontal, vertical, transfer) face distinct and unique privacy threats requiring tailored countermeasures
- Privacy threats and countermeasures have not been comprehensively categorized in existing literature prior to this work
- Systematic categorization enables better understanding of which countermeasures apply to specific FL types
- Privacy risks persist across all FL variants and require ongoing research attention

**Limitations**: As a survey paper, it synthesizes existing work rather than presenting novel empirical results or experimental validation of the categorized threats and countermeasures.

### Hewa Kaluannakkage and Buyya (2025)

**Research question**: What are the fundamental challenges in designing incentive mechanisms for federated learning systems, and how can economic and game-theoretic concepts address the participation dilemma?

**Methodology**: Comprehensive taxonomy development examining both centralized and decentralized architectures using foundational concepts from economics, game theory, blockchain, and deep reinforcement learning, presented through application-specific case studies.

**Key findings**:
- Participation dilemma critically limits practical FL adoption as entities are unwilling to contribute without receiving benefits
- Free-riding behavior, where entities pretend to participate while benefiting from others' contributions, undermines FL system effectiveness
- Economics and game theory provide foundational theoretical frameworks for designing effective incentive mechanisms
- Technology-driven solutions including blockchain and deep reinforcement learning offer practical implementation pathways
- Well-designed incentive mechanisms are essential components, not optional features, for sustainable and fair FL ecosystems
- Applications span healthcare, smart infrastructure, vehicular networks, and blockchain-based decentralized systems

**Limitations**: Significant challenges remain in building truly sustainable, fair, and robust federated learning ecosystems, and practical implementation complexities for incentive mechanisms are not fully resolved.

### Ho (2026)

**Research question**: How can federated learning be applied to infant movement analysis while accounting for model uncertainty in clinical settings with privacy and data-sharing constraints?

**Methodology**: Presents the first federated learning framework for automated infant movement analysis using skeletal motion data; employs Monte Carlo Dropout for uncertainty estimation and proposes Uncertainty-Aware Federated Averaging (UA-FedAvg) that incorporates predictive entropy into the federated aggregation process.

**Key findings**:
- Federated learning substantially improves classification performance compared with independently trained local models
- FL achieves performance approaching that of centralized training while preserving privacy
- UA-FedAvg and its variant incorporating validation loss generally outperform conventional FedAvg across evaluated data-split configurations
- First federated learning framework specifically designed for infant movement analysis and General Movement Assessment
- Framework effectively handles cross-subject evaluation under three-client federated learning setting

**Limitations**: Evaluated only on fidgety movement classification task; three-client setting may not reflect larger-scale clinical deployments.

### Legler et al. (2024)

**Research question**: How can new clients be seamlessly integrated into existing federated learning systems while maintaining stability and efficiency despite data heterogeneity and varying computational capabilities?

**Methodology**: Investigation of client integration complexities focusing on data heterogeneity, non-IID distributions, and their effects on model training, with practical sampling strategies demonstrated through optical quality inspection image data as a case study.

**Key findings**:
- Dynamic FL systems face significant challenges from ongoing incorporation of new clients with diverse data distributions and computational capabilities
- Data heterogeneity and non-IID distributions among clients significantly affect model training, system efficiency, scalability, and stability
- Production environments typically have fewer clients than original FL applications like Gboard, making each new client's information more valuable
- Effective client selection strategies can enhance data diversity, improve learning performance, and leverage distributed computational power
- Addressing new client integration challenges is crucial for advancing FL adoption in production environments

**Limitations**: Practical approaches are demonstrated through a specific use case (optical quality inspection) which may not fully generalize to all federated learning application domains and deployment scenarios.

### Németh et al. (2025)

**Research question**: How can data heterogeneity in federated learning be characterized and managed to improve model generalization capabilities and convergence across clients?

**Methodology**: Characterizes statistical data heterogeneity using 6 metrics of global and client attribute imbalance, class imbalance, and spurious correlations; creates 7 computer vision datasets covering broad range of heterogeneity; proposes FEDDIVERSE client selection algorithm designed to manage and leverage data heterogeneity by promoting collaboration between clients with complementary data distributions.

**Key findings**:
- FEDDIVERSE enhances performance and robustness of various FL methods across heterogeneous data distributions
- Algorithm demonstrates low communication and computational overhead
- 7 new FL datasets created and shared covering binary and multiclass image classification tasks with diverse heterogeneity patterns
- Effectively manages non-IID and imbalanced data that typically slows convergence and reduces performance
- Promoting collaboration between clients with complementary distributions improves generalization capabilities

**Limitations**: Focus primarily on computer vision tasks; generalizability to other domains such as NLP or tabular data not demonstrated.

### Pokhrel et al. (2024)

**Research question**: How can quantum federated learning be deployed on cloud platforms, and what are the technical challenges and viable solutions for practical QFL implementation?

**Methodology**: Proof-of-concept implementation using data-encoding-driven quantum federated learning with genomic datasets on quantum simulators, deployed and tested on cloud platforms with open-source code availability.

**Key findings**:
- Quantum federated learning enables collaborative quantum model training while preserving local data privacy across quantum networks
- Cloud platform deployment of QFL faces significant quantum-specific intricacies and platform limitations
- Data-encoding-driven approaches show promising results for practical QFL implementation
- Genomic data experiments on quantum simulators demonstrate feasibility of the proposed QFL approach
- Open-source implementation on GitHub provides reproducible proof of concept for the research community

**Limitations**: Experiments were conducted on quantum simulators rather than actual quantum hardware, and cloud platform constraints may limit scalability and real-world applicability of the proposed approach.

### Rangwala et al. (2025)

**Research question**: How can blockchain technology address fundamental challenges of trust, privacy, and coordination in collaborative AI systems?

**Methodology**: Provides comprehensive architectural analysis through a four-dimensional taxonomy examining coordination structures, consensus mechanisms, storage architectures, and trust models, with detailed examination of design patterns from blockchain-verified centralized coordination to fully decentralized peer-to-peer networks.

**Key findings**:
- BCFL systems achieve performance comparable to centralized approaches while providing enhanced security guarantees
- Computational work can be repurposed from arbitrary cryptographic puzzles to productive ML tasks through Proof of Quality and Proof of Federated Learning consensus mechanisms
- Multi-tier architectures successfully balance blockchain's transaction constraints with neural networks' large parameter requirements
- TrustMesh case study demonstrates effective collaborative learning across IoT devices with highly non-IID data distributions
- Real-world deployments validated across healthcare consortiums, financial services, and IoT security applications

**Limitations**: Chapter format indicates survey/overview nature rather than novel empirical contribution; scalability trade-offs in large-scale deployments require further investigation.

### Wei et al. (2024)

**Research question**: How do data poisoning and privacy leakage threats impact federated learning, and what defense strategies can effectively mitigate these risks?

**Methodology**: Empirical analytical study investigating training data privacy threats, gradient leakage vulnerabilities, and poisoning attacks through evaluation of perturbation-based defense strategies. The study examines when and how training data may be leaked during federated training rounds.

**Key findings**:
- Training data can be leaked during federated learning through gradient updates shared between clients
- Adding controlled randomized noise to gradient updates before sharing effectively mitigates privacy leakage threats
- Data poisoning attacks can induce model Trojan attacks that cause detrimental damage to global model performance
- Dynamic model perturbation can simultaneously ensure privacy protection, poisoning resilience, and maintain model performance
- Additional risk factors include data skewness, algorithmic biases, and misinformation in training data

**Limitations**: The study focuses primarily on perturbation-based defenses and may not comprehensively cover all attack vectors or defense mechanisms applicable to diverse federated learning deployments in real-world settings.

### Yashwanth et al. (2026)

**Research question**: How can federated learning sustain client participation when clients are rational agents who may prioritize their local utility over global model performance?

**Methodology**: Introduces FedUCA framework that formalizes the server's role as an optimizer seeking to maximize global model performance by sustaining client participation through utility-constrained stochastic aggregation.

**Key findings**:
- FedUCA achieves significantly higher client retention compared to traditional FL approaches
- Higher client retention leads to superior global model performance
- Framework effectively addresses client attrition in settings with significant statistical heterogeneity
- Prioritizing participation feasibility prevents collapse of federated training process
- Validated through extensive experiments on standard datasets

**Limitations**: Experimental validation limited to standard datasets; real-world cross-silo deployment challenges not fully addressed.

## References

Banse, A., Kreischer, J., & Oliva i Jürgens, X. (2024). Federated learning with differential privacy. arXiv. https://arxiv.org/abs/2402.02230v1

Hayashitani, M., Mori, J., & Teranishi, I. (2024). Survey of privacy threats and countermeasures in federated learning. arXiv. https://arxiv.org/abs/2402.00342v2

Hewa Kaluannakkage, C. A. S., & Buyya, R. (2025). Incentive-based federated learning: Architectural elements and future directions. arXiv. https://arxiv.org/abs/2510.14208v2

Ho, E. S. L. (2026). Uncertainty-aware federated learning for infant movement analysis. arXiv. https://arxiv.org/abs/2609.31463v1

Legler, T., Hegiste, V., & Ruskowski, M. (2024). Seamless integration: Sampling strategies in federated learning systems. arXiv. https://arxiv.org/abs/2408.09545v2

Németh, G. D., Fanì, E., Ng, Y. J., Caputo, B., Lozano, M. Á., Oliver, N., & Quadrianto, N. (2025). FedDiverse: Tackling data heterogeneity in federated learning with diversity-driven client selection. arXiv. https://arxiv.org/abs/2504.11216v2

Pokhrel, S. R., Yash, N., Kua, J., Li, G., & Pan, L. (2024). Quantum federated learning experiments in the cloud with data encoding. arXiv. https://arxiv.org/abs/2405.00909v1

Rangwala, M., Venugopal, K. R., & Buyya, R. (2025). Blockchain-enabled federated learning. arXiv. https://arxiv.org/abs/2508.06406v4

Wei, W., Huang, T., Yahn, Z., Singhal, A., Loper, M., & Liu, L. (2024). Data poisoning and leakage analysis in federated learning. arXiv. https://arxiv.org/abs/2409.13004v1

Yashwanth, M., Singh, A., Nayak, A., Bulusu, S. K., & Chakraborty, A. (2026). Federated learning by utility-constrained stochastic aggregation for improving rational participation. arXiv. https://arxiv.org/abs/2605.18020v1
